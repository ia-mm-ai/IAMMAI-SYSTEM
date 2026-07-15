"""Tests for the portable source-body verification command invocation resolver.

This suite is bounded to command invocation only. Command invocation may spend
one preserved one-shot authorization token exactly once, but these tests do not
create command execution, command output, command result, command success,
execution permission, execution approval, standing lanes, repeat permission,
deployment, continuation, reusable permission, derivative reception, vessel
relation, another reception request, or follow-on work.
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

import resolve_portable_source_body_verification_command_invocation as resolver
from resolve_portable_source_body_verification_command_invocation import (
    build_declared_portable_source_body_verification_command_invocation_request,
    build_portable_source_body_verification_command_invocation_summary,
    resolve_portable_source_body_verification_command_invocation,
    resolve_portable_source_body_verification_command_invocation_from_path,
    write_portable_source_body_verification_command_invocation_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_COMMAND_INVOCATION_QUESTION
COMMAND_INVOCATION_BOUNDARY_OUTCOME = resolver.COMMAND_INVOCATION_BOUNDARY_OUTCOME
COMMAND_INVOCATION_AUTHORIZATION_OUTCOME = resolver.COMMAND_INVOCATION_AUTHORIZATION_OUTCOME
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_INVOCATION_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_INVOCATION_FULL_BODY_MUST_NOT_RETURN_" * 8

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_invocation_metadata",
    "declared_command_invocation_question",
    "selected_command_invocation_boundary_basis",
    "selected_command_invocation_boundary_terminal_summary_basis",
    "selected_command_invocation_authorization_basis",
    "selected_command_invocation_authorization_terminal_summary_basis",
    "selected_command_execution_review_basis",
    "selected_request_consumption_basis",
    "selected_consumed_request_basis",
    "selected_v2_admitted_request_basis",
    "selected_v1_predecessor_failure_basis",
    "selected_command_execution_boundary_basis",
    "selected_command_report_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "invocation_only_posture",
    "one_shot_token_spend_posture",
    "token_spent_exactly_once_posture",
    "no_token_reuse_posture",
    "no_command_execution_posture",
    "no_output_result_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "command_invocation_scope",
    "command_invocation_checks",
    "command_invocation_statement",
    "command_invocation_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_invocation_summary",
)

OPEN_ITEMS = (
    "command_invocation_test",
    "command_invocation_live_artifact",
    "command_execution_boundary_or_execution_step_if_separately_specified",
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
        "basis_does_not_create_standing_lane_or_repeat_permission": True,
        "full_upstream_lineage_preserved": True,
        "upstream_lineage": (
            "portable_source_body_verification_consumed_single_live_command_invocation_request_"
            "command_invocation_boundary_to_command_invocation"
        ),
        "full_prior_artifact_body_not_emitted": True,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _command_invocation_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_boundary",
        result_id="command_invocation_boundary_reference_review_001",
        result_path="artifacts/synthetic_command_invocation_boundary_result.json",
        outcome=COMMAND_INVOCATION_BOUNDARY_OUTCOME,
        failed_check_count=0,
        command_invocation_authorization_token_preserved=True,
        authorization_token_preserved=True,
        authorization_token_remains_one_shot=True,
        authorization_token_not_spent=True,
        command_invocation_boundary_recorded=True,
        boundary_basis_remains_boundary_basis_only=True,
        boundary_did_not_create_command_invocation=True,
        boundary_did_not_execute_command=True,
        boundary_did_not_create_output_result_success=True,
        boundary_did_not_create_execution_permission_or_approval=True,
        boundary_did_not_create_standing_lane_or_repeat_permission=True,
        boundary_did_not_create_final_completion_continuation_reusable_permission_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_boundary_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_boundary_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path=(
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_"
            "COMMAND_INVOCATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_invocation=True,
        terminal_summary_does_not_authorize_execution=True,
        terminal_summary_does_not_create_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
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
        command_invocation_authorization_token_created=True,
        authorization_token_created=True,
        authorization_token_is_one_shot=True,
        authorization_token_one_shot=True,
        authorization_basis_preserved=True,
        command_invocation_authorization_remains_authorization_basis_only=True,
        authorization_did_not_execute_command=True,
        authorization_did_not_create_output_result_success=True,
        authorization_did_not_create_execution_permission_or_approval=True,
        authorization_did_not_create_standing_lane_or_repeat_permission=True,
        authorization_did_not_create_final_completion_continuation_reusable_permission_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_authorization_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_authorization_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path=(
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_"
            "COMMAND_INVOCATION_AUTHORIZATION_TERMINAL_SUMMARY_V0.md"
        ),
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_execution=True,
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
        request_consumption_basis_does_not_create_execution_permission_or_approval=True,
        request_consumption_basis_does_not_create_standing_lane_or_repeat_permission=True,
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
        consumed_request_not_reopened=True,
        consumed_request_is_not_reopened=True,
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
        v1_predecessor_failure_remains_visible=True,
        v1_is_not_repaired=True,
        v1_is_not_hidden=True,
        v1_is_not_claimed_passed=True,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
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
        "invocation_only_posture_declared": label == "invocation_only",
        "one_shot_token_spend_posture_declared": label == "one_shot_token_spend",
        "token_spent_exactly_once_posture_declared": label == "token_spent_exactly_once",
        "no_token_reuse_posture_declared": label == "no_token_reuse",
        "command_execution_not_performed": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "returned_result_containment_preserved": True,
        "no_raw_full_prior_artifact_body_returned": True,
        "authorization_token_spent_exactly_once": label == "token_spent_exactly_once",
        "authorization_token_reuse_blocked": label == "no_token_reuse",
        "authorization_token_not_reused": label == "no_token_reuse",
    }
    posture.update(extra)
    return posture


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request = {
        "command_invocation_request_id": "command_invocation_reference_review_001",
        "command_invocation_question": QUESTION,
        "command_invocation_intent": resolver.INTENT_RECORD,
        "selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(),
        "selected_command_invocation_boundary_terminal_summary_basis": (
            _command_invocation_boundary_terminal_summary_basis()
        ),
        "selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(),
        "selected_command_invocation_authorization_terminal_summary_basis": (
            _command_invocation_authorization_terminal_summary_basis()
        ),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_basis": _command_basis("command_execution_boundary"),
        "selected_command_report_basis": _command_basis("command_report"),
        "selected_command_implementation_boundary_basis": _command_basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _command_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _command_basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _command_basis("evidence_manifest"),
        "selected_portable_verification_basis": _command_basis("portable_verification"),
        "invocation_only_posture": _posture("invocation_only", command_invocation_only=True),
        "one_shot_token_spend_posture": _posture("one_shot_token_spend"),
        "token_spent_exactly_once_posture": _posture("token_spent_exactly_once"),
        "no_token_reuse_posture": _posture("no_token_reuse"),
        "no_command_execution_posture": _posture("no_command_execution"),
        "no_output_result_success_posture": _posture("no_output_result_success"),
        "no_execution_permission_posture": _posture("no_execution_permission"),
        "no_execution_approval_posture": _posture("no_execution_approval"),
        "no_standing_lane_posture": _posture("no_standing_lane"),
        "no_repeat_permission_posture": _posture("no_repeat_permission"),
        "consumed_token_closed_posture": _posture("consumed_token_closed"),
        "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request"),
        "returned_result_containment_posture": _posture("returned_result_containment"),
        "command_invocation_scope": list(SUPPORTED_SCOPE),
        "requested_command_invocation_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
    }
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_command_invocation(
        declared_command_invocation_request=request
    )


def _failed_count(result: dict[str, Any]) -> int:
    return sum(1 for check in result["command_invocation_checks"] if not check["passed"])


class PortableSourceBodyVerificationCommandInvocationTests(unittest.TestCase):
    def assertBlocked(self, result: dict[str, Any], block_code: str) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], block_code)

    def assertNoExecutionOrFollowOnFlags(self, result: dict[str, Any]) -> None:
        statement = result["command_invocation_statement"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False, key)
            self.assertIs(result["non_claims"][key], False, key)

    def test_recorded_command_invocation_result_shape_and_statement(self) -> None:
        result = _resolve(_valid_request())
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(_failed_count(result), 0)

        statement = result["command_invocation_statement"]
        for key in (
            "command_invocation_recorded",
            "bounded_command_invocation_event_recorded",
            "authorization_token_spent_exactly_once",
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
            "authorization_token_reused",
            "standing_invocation_lane_created",
            "repeat_invocation_permission_created",
            "invocation_treated_as_execution",
            "invocation_treated_as_command_success",
            "invocation_treated_as_source",
            "invocation_treated_as_authority",
            "command_output_became_source",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
        ):
            self.assertIs(statement[key], False, key)
        self.assertNoExecutionOrFollowOnFlags(result)

    def test_metadata_and_lineage_are_preserved_with_short_resolver_name(self) -> None:
        result = _resolve(_valid_request())
        metadata = result["portable_source_body_verification_command_invocation_metadata"]
        for key in (
            "portable_source_body_verification_command_invocation_result_id",
            "portable_source_body_verification_command_invocation_result_type",
            "portable_source_body_verification_command_invocation_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["portable_source_body_verification_command_invocation_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], "resolve_portable_source_body_verification_command_invocation")
        self.assertTrue(metadata["naming_containment"]["short_resolver_filename_used_intentionally"])
        self.assertTrue(metadata["naming_containment"]["full_upstream_lineage_preserved_in_selected_basis"])
        self.assertTrue(result["selected_command_invocation_boundary_basis"]["full_upstream_lineage_preserved"])
        self.assertTrue(result["selected_command_invocation_authorization_basis"]["full_upstream_lineage_preserved"])

    def test_selected_basis_lineage_behavior(self) -> None:
        result = _resolve(_valid_request())
        boundary = result["selected_command_invocation_boundary_basis"]
        self.assertEqual(boundary["outcome"], COMMAND_INVOCATION_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertTrue(boundary["authorization_token_preserved"])
        self.assertTrue(boundary["authorization_token_not_spent"])
        self.assertTrue(boundary["boundary_basis_remains_boundary_basis_only"])
        self.assertTrue(boundary["boundary_did_not_execute_command"])
        self.assertTrue(boundary["boundary_did_not_create_output_result_success"])
        self.assertTrue(boundary["reference_shaped_basis"])

        authorization = result["selected_command_invocation_authorization_basis"]
        self.assertEqual(authorization["outcome"], COMMAND_INVOCATION_AUTHORIZATION_OUTCOME)
        self.assertEqual(authorization["failed_check_count"], 0)
        self.assertTrue(authorization["command_invocation_authorization_token_created"])
        self.assertTrue(authorization["authorization_token_is_one_shot"])
        self.assertTrue(authorization["authorization_basis_preserved"])

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

    def test_command_invocation_checks_are_explicit_and_pass_for_recorded(self) -> None:
        result = _resolve(_valid_request())
        checks = result["command_invocation_checks"]
        self.assertGreater(len(checks), 40)
        for check in checks:
            for key in ("check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"):
                self.assertIn(key, check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"])
            self.assertIsNone(check["failure_code"])
        names = {check["check_name"] for check in checks}
        expected_names = {
            "command invocation question declared",
            "command invocation intent supported",
            "command invocation boundary terminal summary basis declared",
            "command invocation boundary live artifact basis declared",
            "command invocation boundary live artifact recorded outcome",
            "command invocation boundary live artifact failed check count zero",
            "command invocation boundary authorization token preserved",
            "command invocation boundary authorization token not spent",
            "command invocation authorization basis declared",
            "command invocation authorization live artifact recorded outcome",
            "command invocation authorization live artifact failed check count zero",
            "command invocation authorization token created",
            "command invocation authorization token one-shot",
            "command execution review basis declared",
            "request-consumption basis declared",
            "consumed request basis declared",
            "consumed request token remains closed",
            "consumed request not reopened",
            "selected v2 admitted request basis declared",
            "v2 admitted request outcome admitted",
            "v2 admitted request version 0.2.0",
            "v2 successor metadata preserved",
            "v2 returned-result containment preserved",
            "selected v1 predecessor/failure basis declared",
            "v1 predecessor failure remains visible",
            "v2 does not claim v1 passed",
            "invocation-only posture declared",
            "one-shot-token-spend posture declared",
            "token-spent-exactly-once posture declared",
            "no-token-reuse posture declared",
            "authorization token spent exactly once",
            "authorization token not reused",
            "command invocation scope supported",
            "collapse flags absent",
            "raw full prior artifact body not emitted",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))
        self.assertEqual(_failed_count(result), 0)

    def test_command_invocation_non_meaning(self) -> None:
        non_meaning = _resolve(_valid_request())["command_invocation_non_meaning"]
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
            "standing_invocation_lane_exists",
            "repeat_invocation_permission_exists",
            "consumed_request_token_reopened",
            "v1_was_repaired",
            "v1_was_hidden",
            "v1_passed",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "public_readiness_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(non_meaning[f"command_invocation_does_not_mean_{suffix}"], True)

    def test_additional_basis_and_not_recorded_outcomes_are_bounded(self) -> None:
        additional_context = {"missing_basis": ["command invocation token posture unclear"]}
        request = _valid_request(
            requested_command_invocation_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=additional_context,
        )
        additional = _resolve(request)
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assertNoExecutionOrFollowOnFlags(additional)

        not_recorded_basis = {"reason": "readable invocation basis failed bounded review"}
        not_recorded = _resolve(
            _valid_request(
                requested_command_invocation_outcome=NOT_RECORDED,
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
        summary = build_portable_source_body_verification_command_invocation_summary(result)
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["command_invocation_request_id"], "command_invocation_reference_review_001")
        self.assertEqual(summary["command_invocation_question"], QUESTION)
        self.assertEqual(summary["command_invocation_intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "command_invocation_recorded",
            "bounded_command_invocation_event_recorded",
            "authorization_token_spent_exactly_once",
            "authorization_token_reuse_blocked",
            "command_execution_still_not_performed",
            "command_output_result_success_still_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "command_execution_not_performed",
            "command_output_result_success_not_created",
            "authorization_token_not_reused",
            "no_standing_lane",
            "no_repeat_permission",
            "consumed_request_not_reopened",
            "invocation_not_execution",
            "invocation_not_command_success",
            "invocation_not_source",
            "invocation_not_authority",
            "v1_not_repaired_hidden_or_claimed_passed",
            "no_raw_full_prior_artifact_body_returned",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["not_recorded"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual(summary["selected_command_invocation_boundary_outcome"], COMMAND_INVOCATION_BOUNDARY_OUTCOME)
        self.assertEqual(
            summary["selected_command_invocation_authorization_outcome"],
            COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
        )
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["key_non_claims"], _false_non_claims())

    def test_request_builder_helper(self) -> None:
        additional_context = {"basis": "token posture context"}
        not_recorded_basis = {"reason": "not recorded basis"}
        request = build_declared_portable_source_body_verification_command_invocation_request(
            "builder_request_001",
            QUESTION,
            _command_invocation_boundary_basis(),
            _command_invocation_boundary_terminal_summary_basis(),
            _command_invocation_authorization_basis(),
            _command_invocation_authorization_terminal_summary_basis(),
            _command_execution_review_basis(),
            _request_consumption_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _command_basis("command_execution_boundary"),
            _command_basis("command_report"),
            _command_basis("command_implementation_boundary"),
            _command_basis("command_boundary"),
            _command_basis("artifact_emission_containment"),
            _command_basis("evidence_manifest"),
            _command_basis("portable_verification"),
            _posture("invocation_only", command_invocation_only=True),
            _posture("one_shot_token_spend"),
            _posture("token_spent_exactly_once"),
            _posture("no_token_reuse"),
            _posture("no_command_execution"),
            _posture("no_output_result_success"),
            _posture("no_execution_permission"),
            _posture("no_execution_approval"),
            _posture("no_standing_lane"),
            _posture("no_repeat_permission"),
            _posture("consumed_token_closed"),
            _posture("no_reopen_consumed_request"),
            _posture("returned_result_containment"),
            list(SUPPORTED_SCOPE),
            selected_command_invocation_boundary_result_path="artifacts/boundary.json",
            selected_command_invocation_boundary_result_id="boundary_result_001",
            selected_command_invocation_boundary_result_outcome=COMMAND_INVOCATION_BOUNDARY_OUTCOME,
            selected_command_invocation_boundary_failed_check_count=0,
            selected_command_invocation_boundary_authorization_token_preserved=True,
            selected_command_invocation_boundary_authorization_token_not_spent=True,
            selected_command_invocation_authorization_result_path="artifacts/authorization.json",
            selected_command_invocation_authorization_result_id="authorization_result_001",
            selected_command_invocation_authorization_result_outcome=COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
            selected_command_invocation_authorization_failed_check_count=0,
            selected_command_invocation_authorization_token_created=True,
            selected_command_invocation_authorization_token_is_one_shot=True,
            selected_request_consumption_result_path="artifacts/request_consumption.json",
            selected_request_consumption_result_id="request_consumption_result_001",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="artifacts/v2.json",
            selected_v2_admitted_request_artifact_id="v2_result_001",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(request["command_invocation_request_id"], "builder_request_001")
        self.assertEqual(request["command_invocation_question"], QUESTION)
        self.assertEqual(request["selected_command_invocation_boundary_result_path"], "artifacts/boundary.json")
        self.assertEqual(request["selected_command_invocation_boundary_result_id"], "boundary_result_001")
        self.assertEqual(request["selected_command_invocation_boundary_result_outcome"], COMMAND_INVOCATION_BOUNDARY_OUTCOME)
        self.assertEqual(request["selected_command_invocation_boundary_failed_check_count"], 0)
        self.assertIs(request["selected_command_invocation_boundary_authorization_token_preserved"], True)
        self.assertIs(request["selected_command_invocation_boundary_authorization_token_not_spent"], True)
        self.assertEqual(request["selected_command_invocation_authorization_result_path"], "artifacts/authorization.json")
        self.assertEqual(request["selected_command_invocation_authorization_result_id"], "authorization_result_001")
        self.assertIs(request["selected_command_invocation_authorization_token_created"], True)
        self.assertIs(request["selected_command_invocation_authorization_token_is_one_shot"], True)
        self.assertEqual(request["selected_request_consumption_result_path"], "artifacts/request_consumption.json")
        self.assertEqual(request["selected_v2_admitted_request_artifact_path"], "artifacts/v2.json")
        self.assertEqual(request["selected_v2_admitted_request_artifact_id"], "v2_result_001")
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        self.assertEqual(request["declared_non_claims"], _false_non_claims())
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)

    def test_path_based_resolution_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")
            path_result = resolve_portable_source_body_verification_command_invocation_from_path(request_path)
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["portable_source_body_verification_command_invocation_metadata"][
                    "declared_command_invocation_request_path"
                ],
                str(request_path),
            )

            malformed = tmp_path / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_invocation_from_path(malformed),
                "DECLARED_COMMAND_INVOCATION_REQUEST_MALFORMED",
            )
            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            self.assertBlocked(
                resolve_portable_source_body_verification_command_invocation_from_path(array_path),
                "DECLARED_COMMAND_INVOCATION_REQUEST_MALFORMED",
            )
            self.assertBlocked(
                resolve_portable_source_body_verification_command_invocation_from_path(tmp_path / "missing.json"),
                "DECLARED_COMMAND_INVOCATION_REQUEST_UNREADABLE",
            )

            output_path = tmp_path / "nested" / "result.json"
            written = write_portable_source_body_verification_command_invocation_result(mapping_result, output_path)
            self.assertEqual(written, output_path)
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            root = tmp_path / "integrity_host_v0_min_coexistence_portable_source_body_verification_command_invocation"
            with patch.object(resolver, "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_INVOCATION_ROOT", root):
                default_written = write_portable_source_body_verification_command_invocation_result(mapping_result)
                second_written = write_portable_source_body_verification_command_invocation_result(mapping_result)
            self.assertEqual(default_written.parent, root)
            self.assertEqual(second_written.parent, root)
            self.assertNotEqual(default_written, second_written)
            self.assertTrue(second_written.name.endswith("_001.json"))
            self.assertNotIn("command_invocation_boundary", root.name)
            self.assertNotIn("command_invocation_authorization", root.name)
            self.assertNotIn("command_execution_review", root.name)

    def test_reference_shaped_containment_blocks_full_body(self) -> None:
        request = _valid_request()
        request["selected_command_invocation_boundary_basis"]["full_artifact_body"] = RAW_FULL_BODY_SENTINEL
        result = _resolve(request)
        self.assertBlocked(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertIs(result["command_invocation_statement"]["command_execution_performed"], False)
        self.assertIs(result["command_invocation_statement"]["command_output_created"], False)
        self.assertIs(result["command_invocation_statement"]["command_result_created"], False)
        self.assertIs(result["command_invocation_statement"]["command_success_created"], False)

        request = _valid_request()
        request["selected_request_consumption_basis"]["full_artifact_body"] = RAW_FULL_BODY_SENTINEL
        result = _resolve(request)
        self.assertBlocked(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self.assertIs(result["command_invocation_statement"]["prior_artifacts_mutated"], False)

    def test_non_mutation_posture(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertEqual(request, original)
        second = _resolve(request)
        self.assertEqual(request, original)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "command_invocation" / "result.json"
            written = write_portable_source_body_verification_command_invocation_result(result, output_path)
            self.assertTrue(written.exists())
            self.assertEqual(request, original)

    def test_blocking_basis_and_artifact_failures(self) -> None:
        cases: list[tuple[str, dict[str, Any], str]] = [
            ("missing boundary basis", {"selected_command_invocation_boundary_basis": None}, "COMMAND_INVOCATION_BOUNDARY_BASIS_MISSING"),
            ("boundary not recorded", {"selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(outcome="NO")}, "COMMAND_INVOCATION_BOUNDARY_NOT_RECORDED"),
            ("boundary failed checks", {"selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(failed_check_count=1)}, "COMMAND_INVOCATION_BOUNDARY_FAILED_CHECKS_PRESENT"),
            ("boundary token not preserved", {"selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(command_invocation_authorization_token_preserved=False, authorization_token_preserved=False, authorization_token_remains_one_shot=False)}, "COMMAND_INVOCATION_BOUNDARY_AUTHORIZATION_TOKEN_NOT_PRESERVED"),
            ("boundary token spent", {"selected_command_invocation_boundary_basis": _command_invocation_boundary_basis(authorization_token_spent=True)}, "COMMAND_INVOCATION_BOUNDARY_AUTHORIZATION_TOKEN_ALREADY_SPENT"),
            ("missing boundary terminal summary", {"selected_command_invocation_boundary_terminal_summary_basis": None}, "COMMAND_INVOCATION_BOUNDARY_TERMINAL_SUMMARY_MISSING"),
            ("missing authorization basis", {"selected_command_invocation_authorization_basis": None}, "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING"),
            ("authorization not recorded", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(outcome="NO")}, "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED"),
            ("authorization failed checks", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(failed_check_count=1)}, "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT"),
            ("authorization token missing", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(command_invocation_authorization_token_created=False, authorization_token_created=False, single_command_invocation_authorization_created=False)}, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_MISSING"),
            ("authorization token not one shot", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(authorization_token_is_one_shot=False, authorization_token_one_shot=False)}, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_ONE_SHOT"),
            ("authorization token already spent", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(authorization_token_spent=True)}, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_ALREADY_SPENT"),
            ("authorization token reused", {"selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(authorization_token_reused=True)}, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSED"),
            ("missing review basis", {"selected_command_execution_review_basis": None}, "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
            ("review not recorded", {"selected_command_execution_review_basis": _command_execution_review_basis(outcome="NO")}, "COMMAND_EXECUTION_REVIEW_NOT_RECORDED"),
            ("review failed checks", {"selected_command_execution_review_basis": _command_execution_review_basis(failed_check_count=1)}, "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT"),
            ("missing consumption basis", {"selected_request_consumption_basis": None}, "REQUEST_CONSUMPTION_BASIS_MISSING"),
            ("consumption not consumed", {"selected_request_consumption_basis": _request_consumption_basis(outcome="NO")}, "REQUEST_CONSUMPTION_NOT_CONSUMED"),
            ("consumption failed checks", {"selected_request_consumption_basis": _request_consumption_basis(failed_check_count=1)}, "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT"),
            ("missing consumed basis", {"selected_consumed_request_basis": None}, "CONSUMED_REQUEST_BASIS_MISSING"),
            ("consumed token not closed", {"selected_consumed_request_basis": _consumed_request_basis(consumed_request_token_remains_closed=False, consumption_token_closed=False, consumed_token_closed=False, token_closed=False)}, "CONSUMED_TOKEN_NOT_CLOSED"),
            ("consumed reopened", {"selected_consumed_request_basis": _consumed_request_basis(consumed_request_reopened=True)}, "CONSUMED_REQUEST_REOPENED"),
            ("missing v2", {"selected_v2_admitted_request_basis": None}, "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            ("v2 not admitted", {"selected_v2_admitted_request_basis": _v2_admitted_request_basis(outcome="NO")}, "V2_ADMITTED_REQUEST_NOT_ADMITTED"),
            ("v2 wrong version", {"selected_v2_admitted_request_basis": _v2_admitted_request_basis(result_version="0.1.0")}, "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0"),
            ("v2 failed checks", {"selected_v2_admitted_request_basis": _v2_admitted_request_basis(failed_check_count=1)}, "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT"),
            ("v2 successor metadata missing", {"selected_v2_admitted_request_basis": _reference_shape("v2", outcome=V2_ADMITTED_REQUEST_OUTCOME, result_version=V2_ADMITTED_REQUEST_VERSION, failed_check_count=0, returned_result_containment_preserved=True)}, "V2_SUCCESSOR_METADATA_MISSING"),
            ("v2 containment missing", {"selected_v2_admitted_request_basis": _v2_admitted_request_basis(returned_result_containment_preserved=False, no_raw_full_prior_artifact_body_returned=False)}, "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
            ("missing v1", {"selected_v1_predecessor_failure_basis": None}, "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            ("v2 repairs v1", {"selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(v2_treated_as_repairing_v1=True)}, "V2_TREATED_AS_REPAIRING_V1"),
            ("v1 hidden", {"selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(v1_hidden=True)}, "V1_FAILURE_HIDDEN"),
            ("v1 claimed passed", {"selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(v1_claimed_passed=True)}, "V1_CLAIMED_PASSED"),
            ("missing execution boundary", {"selected_command_execution_boundary_basis": None}, "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("missing report", {"selected_command_report_basis": None}, "COMMAND_REPORT_BASIS_MISSING"),
            ("missing implementation boundary", {"selected_command_implementation_boundary_basis": None}, "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            ("missing command boundary", {"selected_command_boundary_basis": None}, "COMMAND_BOUNDARY_BASIS_MISSING"),
            ("missing containment", {"selected_artifact_emission_containment_basis": None}, "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("missing evidence manifest", {"selected_evidence_manifest_basis": None}, "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("missing portable verification", {"selected_portable_verification_basis": None}, "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("missing invocation posture", {"invocation_only_posture": None}, "INVOCATION_ONLY_POSTURE_MISSING"),
            ("missing spend posture", {"one_shot_token_spend_posture": None}, "ONE_SHOT_TOKEN_SPEND_POSTURE_MISSING"),
            ("missing exactly once posture", {"token_spent_exactly_once_posture": None}, "TOKEN_SPENT_EXACTLY_ONCE_POSTURE_MISSING"),
            ("missing no reuse posture", {"no_token_reuse_posture": None}, "NO_TOKEN_REUSE_POSTURE_MISSING"),
            ("missing no standing posture", {"no_standing_lane_posture": None}, "NO_STANDING_LANE_POSTURE_MISSING"),
            ("missing no repeat posture", {"no_repeat_permission_posture": None}, "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
            ("unsupported scope", {"command_invocation_scope": ["UNSUPPORTED"]}, "UNSUPPORTED_COMMAND_INVOCATION_SCOPE"),
        ]
        for name, override, block_code in cases:
            with self.subTest(name=name):
                self.assertBlocked(_resolve(_valid_request(**override)), block_code)

    def test_blocking_collapse_flags(self) -> None:
        cases = (
            ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
            ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
            ("authorization_token_reused", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_REUSED"),
            ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
            ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
            ("invocation_treated_as_execution", "INVOCATION_TREATED_AS_EXECUTION"),
            ("invocation_treated_as_command_success", "INVOCATION_TREATED_AS_COMMAND_SUCCESS"),
            ("invocation_treated_as_source", "INVOCATION_TREATED_AS_SOURCE"),
            ("invocation_treated_as_authority", "INVOCATION_TREATED_AS_AUTHORITY"),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            ("command_success_claimed_final_completion", "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"),
            ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
            ("deployment_created", "DEPLOYMENT_CREATED"),
            ("runtime_hosting_created", "RUNTIME_HOSTING_CREATED"),
            ("public_release_created", "PUBLIC_RELEASE_CREATED"),
            ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
            ("public_readiness_created", "PUBLIC_READINESS_CREATED"),
            ("final_completion_claimed", "FINAL_COMPLETION_CLAIMED"),
            ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
            ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
            ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
            ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        )
        for flag, block_code in cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self.assertBlocked(_resolve(request), block_code)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                self.assertBlocked(_resolve(_valid_request(**{flag: True})), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop(REQUIRED_FALSE_NON_CLAIMS[0])
        self.assertBlocked(_resolve(missing_non_claim), "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["follow_on_work_authorized"] = True
        flipped = _resolve(flipped_non_claim)
        self.assertEqual(flipped["outcome"], BLOCKED)
        self.assertIn(flipped["block"]["code"], {"FOLLOW_ON_WORK_AUTHORIZED", "NON_CLAIM_MISSING_OR_FLIPPED"})

    def test_outcome_family_and_malformed_request_blocks(self) -> None:
        for outcome in OUTCOME_FAMILY:
            request = _valid_request(requested_command_invocation_outcome=outcome)
            if outcome == BLOCKED:
                self.assertEqual(_resolve(request)["outcome"], BLOCKED)
            else:
                self.assertEqual(_resolve(request)["outcome"], outcome)

        self.assertBlocked(
            resolve_portable_source_body_verification_command_invocation(None),
            "COMMAND_INVOCATION_QUESTION_UNDECLARED",
        )
        self.assertBlocked(
            resolve_portable_source_body_verification_command_invocation([]),  # type: ignore[arg-type]
            "DECLARED_COMMAND_INVOCATION_REQUEST_MALFORMED",
        )
        self.assertBlocked(
            _resolve(_valid_request(command_invocation_intent=resolver.INTENT_BLOCK)),
            "COMMAND_INVOCATION_BLOCKED_BY_REQUEST",
        )
        self.assertBlocked(
            _resolve(_valid_request(command_invocation_intent="UNSUPPORTED")),
            "COMMAND_INVOCATION_INTENT_UNSUPPORTED",
        )


if __name__ == "__main__":
    unittest.main()
