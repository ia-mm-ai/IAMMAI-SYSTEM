"""Tests for the consumed-request command invocation boundary resolver.

This suite is bounded to command invocation boundary only. The boundary may
preserve a one-shot command invocation authorization token for one future
separately bounded command invocation step, but these tests do not create
command invocation, command execution, command output, command result, command
success, execution permission, execution approval, standing lanes, repeat
permission, token spend, deployment, continuation, reusable permission,
derivative reception, vessel relation, another reception request, or follow-on
work.
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

import resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary as resolver
from resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary import (
    build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_request,
    build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_summary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path,
    write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_COMMAND_INVOCATION_BOUNDARY_QUESTION
COMMAND_INVOCATION_AUTHORIZATION_OUTCOME = resolver.COMMAND_INVOCATION_AUTHORIZATION_OUTCOME
COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME = (
    resolver.COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME
)
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_INVOCATION_BOUNDARY_FULL_BODY_MUST_NOT_RETURN_" * 8

TOP_LEVEL_SECTIONS = (
    "consumed_single_live_command_invocation_request_command_invocation_boundary_metadata",
    "declared_command_invocation_boundary_question",
    "selected_command_invocation_authorization_basis",
    "selected_command_invocation_authorization_terminal_summary_basis",
    "selected_command_invocation_authorization_boundary_basis",
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
    "invocation_boundary_only_posture",
    "one_future_invocation_step_posture",
    "authorization_token_preserved_posture",
    "authorization_token_not_spent_posture",
    "no_command_invocation_posture",
    "no_command_execution_posture",
    "no_output_result_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "returned_result_containment_posture",
    "command_invocation_boundary_scope",
    "command_invocation_boundary_checks",
    "command_invocation_boundary_statement",
    "command_invocation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "consumed_single_live_command_invocation_request_command_invocation_boundary_summary",
)

OPEN_ITEMS = (
    "command_invocation_boundary_test",
    "command_invocation_boundary_live_artifact",
    "actual_command_invocation",
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
        "basis_is_not_command_invocation": True,
        "basis_is_not_command_execution": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_execution_permission_or_approval": True,
        "basis_is_not_authority_currentness_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_standing_lane_or_repeat_permission": True,
        "basis_does_not_spend_authorization_token": True,
        "full_prior_artifact_body_not_emitted": True,
        "prior_artifacts_mutated": False,
    }
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
        authorization_token_is_one_shot=True,
        authorization_basis_preserved=True,
        command_invocation_authorization_remains_authorization_basis_only=True,
        authorization_did_not_create_command_invocation=True,
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
        terminal_summary_does_not_create_command_invocation=True,
        terminal_summary_does_not_authorize_execution=True,
        terminal_summary_does_not_create_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_invocation_authorization_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "command_invocation_authorization_boundary",
        result_id="authorization_boundary_reference_review_001",
        result_path="artifacts/synthetic_authorization_boundary_result.json",
        outcome=COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        failed_check_count=0,
        authorization_boundary_remains_boundary_basis_only=True,
        authorization_boundary_did_not_create_command_invocation_authorization=True,
        authorization_boundary_did_not_create_invocation_execution_output_result_success=True,
        authorization_boundary_did_not_create_execution_permission_or_approval=True,
        authorization_boundary_did_not_create_standing_lane_or_repeat_permission=True,
        authorization_boundary_did_not_create_final_completion_continuation_reusable_permission_follow_on_work=True,
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
        command_execution_review_did_not_authorize_invocation_execution_output_result_success=True,
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
        request_consumption_basis_does_not_authorize_invocation_execution_output_result_success=True,
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
        successor_reason="synthetic successor preserves returned-result containment",
        resolver_module="resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2",
        returned_result_containment_preserved=True,
        no_raw_full_prior_artifact_body_returned=True,
        selected_basis_is_reference_shaped=True,
    )
    basis.update(extra)
    return basis


def _v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "v1_predecessor_failure",
        v1_predecessor_failure_basis_declared=True,
        v1_predecessor_failure_remains_visible=True,
        v1_remains_visible_predecessor_failure_evidence=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
    )
    basis.update(extra)
    return basis


def _generic_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        basis_declared=True,
        basis_remains_reference_shaped=True,
        basis_is_not_execution_permission=True,
        basis_is_not_execution_approval=True,
        basis_is_not_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "posture_label": label,
        "declared": True,
        f"{label}_declared": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "authorization_token_not_spent": True,
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
        "command_invocation_boundary_request_id": "command_invocation_boundary_request_001",
        "command_invocation_boundary_question": QUESTION,
        "command_invocation_boundary_intent": resolver.INTENT_RECORD,
        "selected_command_invocation_authorization_basis": _command_invocation_authorization_basis(),
        "selected_command_invocation_authorization_terminal_summary_basis": _command_invocation_authorization_terminal_summary_basis(),
        "selected_command_invocation_authorization_boundary_basis": _command_invocation_authorization_boundary_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_basis": _generic_basis("command_execution_boundary"),
        "selected_command_report_basis": _generic_basis("command_report"),
        "selected_command_implementation_boundary_basis": _generic_basis("command_implementation_boundary"),
        "selected_command_boundary_basis": _generic_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _generic_basis("artifact_emission_containment"),
        "selected_evidence_manifest_basis": _generic_basis("evidence_manifest"),
        "selected_portable_verification_basis": _generic_basis("portable_verification"),
        "invocation_boundary_only_posture": _posture("invocation_boundary_only_posture"),
        "one_future_invocation_step_posture": _posture("one_future_invocation_step_posture"),
        "authorization_token_preserved_posture": _posture("authorization_token_preserved_posture"),
        "authorization_token_not_spent_posture": _posture("authorization_token_not_spent_posture"),
        "no_command_invocation_posture": _posture("no_command_invocation_posture"),
        "no_command_execution_posture": _posture("no_command_execution_posture"),
        "no_output_result_success_posture": _posture("no_output_result_success_posture"),
        "no_execution_permission_posture": _posture("no_execution_permission_posture"),
        "no_execution_approval_posture": _posture("no_execution_approval_posture"),
        "no_standing_lane_posture": _posture("no_standing_lane_posture"),
        "no_repeat_permission_posture": _posture("no_repeat_permission_posture"),
        "consumed_token_closed_posture": _posture("consumed_token_closed_posture"),
        "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request_posture"),
        "returned_result_containment_posture": _posture("returned_result_containment_posture"),
        "reference_shaped_input_posture": _posture("reference_shaped_input_posture"),
        "command_invocation_boundary_scope": list(SUPPORTED_SCOPE),
        "declared_non_claims": _false_non_claims(),
        "requested_command_invocation_boundary_outcome": RECORDED,
        "selected_command_invocation_authorization_result_path": "artifacts/synthetic_command_invocation_authorization_result.json",
        "selected_command_invocation_authorization_result_id": "command_invocation_authorization_reference_review_001",
        "selected_command_invocation_authorization_result_outcome": COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
        "selected_command_invocation_authorization_failed_check_count": 0,
        "selected_command_invocation_authorization_token_created": True,
        "selected_command_invocation_authorization_token_is_one_shot": True,
        "selected_command_invocation_authorization_terminal_summary_path": "spec/synthetic_command_invocation_authorization_terminal_summary.md",
        "selected_command_invocation_authorization_boundary_result_path": "artifacts/synthetic_authorization_boundary_result.json",
        "selected_command_invocation_authorization_boundary_result_id": "authorization_boundary_reference_review_001",
        "selected_command_invocation_authorization_boundary_result_outcome": COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
        "selected_command_invocation_authorization_boundary_failed_check_count": 0,
        "selected_command_execution_review_result_path": "artifacts/synthetic_command_execution_review_result.json",
        "selected_command_execution_review_result_id": "command_execution_review_reference_review_001",
        "selected_command_execution_review_result_outcome": COMMAND_EXECUTION_REVIEW_OUTCOME,
        "selected_command_execution_review_failed_check_count": 0,
        "selected_request_consumption_result_path": "artifacts/synthetic_request_consumption_result.json",
        "selected_request_consumption_result_id": "request_consumption_reference_record_001",
        "selected_request_consumption_result_outcome": REQUEST_CONSUMPTION_OUTCOME,
        "selected_request_consumption_failed_check_count": 0,
        "selected_v2_admitted_request_artifact_path": "artifacts/synthetic_v2_admission_result.json",
        "selected_v2_admitted_request_artifact_id": "v2_admission_reference_record_001",
        "selected_v2_admitted_request_outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
    }
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary(
        declared_command_invocation_boundary_request=request
    )


def _drop(request: dict[str, Any], key: str) -> dict[str, Any]:
    changed = copy.deepcopy(request)
    changed.pop(key, None)
    return changed


def _set_nested(request: dict[str, Any], section: str, **values: Any) -> dict[str, Any]:
    changed = copy.deepcopy(request)
    changed[section].update(values)
    return changed


def _with_fields(request: dict[str, Any], **values: Any) -> dict[str, Any]:
    changed = copy.deepcopy(request)
    changed.update(values)
    return changed


class CommandInvocationBoundaryResolverTests(unittest.TestCase):
    def assert_blocked(self, request: Any, expected_code: str) -> dict[str, Any]:
        if isinstance(request, dict):
            result = _resolve(request)
        else:
            result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary(
                declared_command_invocation_boundary_request=request
            )
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertEqual(expected_code, result["block"]["code"])
        self._assert_no_invocation_execution_success_or_token_spend(result)
        return result

    def _assert_no_invocation_execution_success_or_token_spend(self, result: dict[str, Any]) -> None:
        statement = result["command_invocation_boundary_statement"]
        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(non_claims[key], False, key)
        for key in (
            "command_invocation_created",
            "command_executed",
            "command_execution_performed",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "execution_permission_created",
            "execution_approval_created",
            "authorization_token_spent_here",
            "standing_invocation_lane_created",
            "repeat_invocation_permission_created",
            "invocation_boundary_treated_as_invocation",
            "invocation_boundary_treated_as_execution",
            "invocation_boundary_treated_as_command_success",
            "authorization_token_treated_as_invocation",
            "authorization_token_treated_as_command_success",
            "command_output_became_source",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "operation_permission_created",
            "public_launch_readiness_created",
            "final_completion_claimed",
            "continuation_authorized",
            "publication_flow_opened",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
        ):
            self.assertIs(statement[key], False, key)

    def test_recorded_result_is_bounded_invocation_boundary_only(self) -> None:
        result = _resolve(_valid_request())
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(0, result["command_invocation_boundary_checks"]["failed_check_count"])

        statement = result["command_invocation_boundary_statement"]
        for key in (
            "command_invocation_boundary_recorded",
            "one_future_command_invocation_step_declared",
            "command_invocation_authorization_token_preserved",
            "authorization_token_remains_one_shot",
            "authorization_token_not_spent",
            "invocation_still_not_created",
            "execution_still_not_performed",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertIs(statement[key], True, key)
        self._assert_no_invocation_execution_success_or_token_spend(result)

    def test_metadata_is_preserved(self) -> None:
        metadata = _resolve(_valid_request())[
            "consumed_single_live_command_invocation_request_command_invocation_boundary_metadata"
        ]
        for key in (
            "consumed_single_live_command_invocation_request_command_invocation_boundary_result_id",
            "consumed_single_live_command_invocation_request_command_invocation_boundary_result_type",
            "consumed_single_live_command_invocation_request_command_invocation_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["consumed_single_live_command_invocation_request_command_invocation_boundary_result_version"])
        self.assertEqual(
            "resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary",
            metadata["resolver_module"],
        )

    def test_selected_basis_lineage_is_preserved_as_reference_shape(self) -> None:
        result = _resolve(_valid_request())
        authorization = result["selected_command_invocation_authorization_basis"]
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_OUTCOME, authorization["outcome"])
        self.assertEqual(0, authorization["failed_check_count"])
        self.assertIs(authorization["selected_command_invocation_authorization_token_created"], True)
        self.assertIs(authorization["selected_command_invocation_authorization_token_is_one_shot"], True)
        self.assertIs(authorization["authorization_basis_preserved"], True)
        self.assertIs(authorization["authorization_did_not_create_command_invocation"], True)
        self.assertIs(authorization["authorization_did_not_execute_command"], True)
        self.assertIs(authorization["authorization_did_not_create_output_result_success"], True)
        self.assertIs(authorization["reference_shaped_basis"], True)

        terminal_summary = result["selected_command_invocation_authorization_terminal_summary_basis"]
        self.assertIs(terminal_summary["terminal_summary_declared"], True)
        self.assertIs(terminal_summary["terminal_summary_remains_readability_basis_only"], True)
        self.assertIs(terminal_summary["terminal_summary_does_not_create_command_invocation"], True)
        self.assertIs(terminal_summary["terminal_summary_does_not_authorize_command_execution"], True)
        self.assertIs(terminal_summary["terminal_summary_does_not_spend_authorization_token"], True)

        auth_boundary = result["selected_command_invocation_authorization_boundary_basis"]
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME, auth_boundary["outcome"])
        self.assertEqual(0, auth_boundary["failed_check_count"])
        self.assertIs(auth_boundary["authorization_boundary_remains_boundary_basis_only"], True)
        self.assertIs(auth_boundary["authorization_boundary_did_not_create_command_invocation_authorization"], True)
        self.assertIs(auth_boundary["authorization_boundary_did_not_create_invocation_execution_output_result_success"], True)

        review = result["selected_command_execution_review_basis"]
        self.assertEqual(COMMAND_EXECUTION_REVIEW_OUTCOME, review["outcome"])
        self.assertEqual(0, review["failed_check_count"])
        self.assertIs(review["command_execution_review_basis_remains_review_basis_only"], True)
        self.assertIs(review["command_execution_review_did_not_authorize_invocation_execution_output_result_success"], True)

        consumption = result["selected_request_consumption_basis"]
        self.assertEqual(REQUEST_CONSUMPTION_OUTCOME, consumption["outcome"])
        self.assertEqual(0, consumption["failed_check_count"])
        self.assertIs(consumption["request_consumed_exactly_once"], True)
        self.assertIs(consumption["consumption_token_closed"], True)
        self.assertIs(consumption["consumed_request_basis_recorded"], True)

        consumed = result["selected_consumed_request_basis"]
        self.assertIs(consumed["consumed_request_token_remains_closed"], True)
        self.assertIs(consumed["consumed_request_not_reopened"], True)
        self.assertIs(consumed["consumed_request_basis_remains_basis_only"], True)

        v2 = result["selected_v2_admitted_request_basis"]
        self.assertEqual(V2_ADMITTED_REQUEST_OUTCOME, v2["outcome"])
        self.assertEqual(V2_ADMITTED_REQUEST_VERSION, v2["result_version"])
        self.assertEqual(0, v2["failed_check_count"])
        self.assertTrue(v2["successor_of"])
        self.assertTrue(v2["successor_reason"])
        self.assertIs(v2["returned_result_containment_preserved"], True)

        v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertIs(v1["v1_predecessor_failure_remains_visible"], True)
        self.assertIs(v1["v1_repaired"], False)
        self.assertIs(v1["v1_hidden"], False)
        self.assertIs(v1["v1_claimed_passed"], False)
        self.assertIs(v1["predecessor_failure_evidence_is_lineage_evidence_only"], True)

    def test_checks_are_explicit_and_pass_for_recorded_case(self) -> None:
        checks = _resolve(_valid_request())["command_invocation_boundary_checks"]
        self.assertEqual(0, checks["failed_check_count"])
        names = {check["check_name"] for check in checks["checks"]}
        for check in checks["checks"]:
            for key in ("check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"):
                self.assertIn(key, check)
            self.assertIs(check["passed"], True, check["check_name"])
            self.assertIsNone(check["block_code"])
            self.assertIsNone(check["failure_code"])

        expected_names = {
            "command invocation boundary question declared",
            "command invocation boundary intent supported",
            "command invocation authorization terminal summary basis declared",
            "command invocation authorization live artifact basis declared",
            "command invocation authorization live artifact recorded outcome",
            "command invocation authorization live artifact failed check count zero",
            "command invocation authorization token created",
            "command invocation authorization token one-shot",
            "command invocation authorization boundary basis declared",
            "command invocation authorization boundary live artifact recorded outcome",
            "command invocation authorization boundary live artifact failed check count zero",
            "command execution review basis declared",
            "command execution review live artifact recorded outcome",
            "command execution review live artifact failed check count zero",
            "request-consumption basis declared",
            "request-consumption live artifact consumed outcome",
            "request-consumption live artifact failed check count zero",
            "consumed request basis declared",
            "consumed request token remains closed",
            "consumed request not reopened",
            "selected v2 admitted request basis declared",
            "v2 admitted request outcome admitted",
            "v2 admitted request version 0.2.0",
            "v2 admitted request failed check count zero",
            "v2 successor metadata preserved",
            "v2 returned-result containment preserved",
            "selected v1 predecessor/failure basis declared",
            "v1 predecessor failure remains visible",
            "v2 does not claim v1 passed",
            "command execution boundary basis declared",
            "command report basis declared",
            "command implementation boundary basis declared",
            "command boundary basis declared",
            "artifact emission containment basis declared",
            "evidence-manifest basis declared",
            "portable verification basis declared",
            "invocation-boundary-only posture declared",
            "one-future-invocation-step posture declared",
            "authorization-token-preserved posture declared",
            "authorization-token-not-spent posture declared",
            "no-command-invocation posture declared",
            "no-command-execution posture declared",
            "no-output/result/success posture declared",
            "no-execution-permission posture declared",
            "no-execution-approval posture declared",
            "no-standing-lane posture declared",
            "no-repeat-permission posture declared",
            "reference-shaped input posture declared",
            "command invocation boundary scope supported",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "execution permission not created",
            "execution approval not created",
            "authorization token not spent",
            "standing invocation lane not created",
            "repeat invocation permission not created",
            "invocation boundary not invocation",
            "invocation boundary not execution",
            "invocation boundary not command success",
            "authorization token not invocation",
            "authorization token not command success",
            "command output not source",
            "command result not authority",
            "command success not currentness",
            "command success not final completion",
            "raw full prior artifact body not emitted",
            "artifacts not mutated",
            "deployment/runtime/public release not created",
            "operation permission/public readiness/final completion not created",
            "continuation/reusable permission/follow-on work not authorized",
            "derivative reception/vessel relation/another reception request not authorized",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(names))

    def test_command_invocation_boundary_non_meaning(self) -> None:
        non_meaning = _resolve(_valid_request())["command_invocation_boundary_non_meaning"]
        for suffix in (
            "command_invocation_created",
            "command_executed",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "execution_permission_exists",
            "execution_approval_exists",
            "command_invocation_authorization_token_spent",
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
            self.assertIs(non_meaning[f"command_invocation_boundary_does_not_mean_{suffix}"], True)

    def test_requires_additional_basis_and_not_recorded_are_bounded(self) -> None:
        additional = {"missing_basis": ["authorization-token-not-spent posture unclear"], "reason": "needs bounded basis"}
        requires_request = _valid_request(
            requested_command_invocation_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=additional,
        )
        requires = _resolve(requires_request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, requires["outcome"])
        self.assertEqual(additional, requires["additional_basis_required"]["additional_basis_context"])
        self.assertIs(requires["additional_basis_required"]["missing_basis_not_scheduled"], True)
        self.assertIs(requires["additional_basis_required"]["missing_basis_not_authorized"], True)
        self.assertIs(requires["additional_basis_required"]["missing_basis_not_executed"], True)
        self._assert_no_invocation_execution_success_or_token_spend(requires)

        not_recorded_basis = {"reason": "invocation-boundary basis cannot be bounded"}
        not_recorded_request = _valid_request(
            requested_command_invocation_boundary_outcome=NOT_RECORDED,
            not_recorded_basis=not_recorded_basis,
        )
        not_recorded = _resolve(not_recorded_request)
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertEqual(not_recorded_basis, not_recorded["not_recorded_basis"]["not_recorded_basis"])
        self.assertIs(not_recorded["not_recorded_basis"]["not_recorded_does_not_mutate"], True)
        self.assertIs(not_recorded["not_recorded_basis"]["not_recorded_does_not_spend_authorization_token"], True)
        self.assertIs(not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize_next_work"], True)
        self._assert_no_invocation_execution_success_or_token_spend(not_recorded)

    def test_what_remains_open_is_not_scheduled_authorized_or_executed(self) -> None:
        open_section = _resolve(_valid_request())["what_remains_open"]
        for item in OPEN_ITEMS:
            self.assertIn(item, open_section["open_items"])
        self.assertIs(open_section["open_means_not_scheduled"], True)
        self.assertIs(open_section["open_means_not_authorized"], True)
        self.assertIs(open_section["open_means_not_executed"], True)

    def test_summary_helper_preserves_key_boundary_and_non_claim_fields(self) -> None:
        result = _resolve(_valid_request())
        summary = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_summary(
            result
        )
        self.assertEqual(RECORDED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual("command_invocation_boundary_request_001", summary["command_invocation_boundary_request_id"])
        self.assertEqual(QUESTION, summary["command_invocation_boundary_question"])
        self.assertEqual(resolver.INTENT_RECORD, summary["command_invocation_boundary_intent"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        for key in (
            "command_invocation_boundary_recorded",
            "one_future_command_invocation_step_declared",
            "command_invocation_authorization_token_preserved",
            "authorization_token_remains_one_shot",
            "authorization_token_not_spent",
            "invocation_still_not_created",
            "execution_still_not_performed",
            "consumed_request_token_remains_closed",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
        ):
            self.assertIs(summary[key], True, key)
        self.assertIs(summary["not_recorded"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_OUTCOME, summary["selected_command_invocation_authorization_outcome"])
        self.assertEqual(0, summary["selected_command_invocation_authorization_failed_check_count"])
        self.assertIs(summary["selected_command_invocation_authorization_token_created"], True)
        self.assertIs(summary["selected_command_invocation_authorization_token_is_one_shot"], True)
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME, summary["selected_command_invocation_authorization_boundary_outcome"])
        self.assertEqual(0, summary["selected_command_invocation_authorization_boundary_failed_check_count"])
        self.assertEqual(COMMAND_EXECUTION_REVIEW_OUTCOME, summary["selected_command_execution_review_outcome"])
        self.assertEqual(0, summary["selected_command_execution_review_failed_check_count"])
        self.assertEqual(REQUEST_CONSUMPTION_OUTCOME, summary["selected_request_consumption_outcome"])
        self.assertEqual(0, summary["selected_request_consumption_failed_check_count"])
        self.assertEqual(V2_ADMITTED_REQUEST_OUTCOME, summary["selected_v2_admitted_request_outcome"])
        self.assertEqual(V2_ADMITTED_REQUEST_VERSION, summary["selected_v2_admitted_request_version"])
        self.assertEqual(0, summary["selected_v2_failed_check_count"])
        for key in (
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_result_success_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "authorization_token_not_spent_non_claim",
            "no_standing_lane",
            "no_repeat_permission",
            "consumed_request_not_reopened",
            "invocation_boundary_not_invocation",
            "invocation_boundary_not_execution",
            "invocation_boundary_not_command_success",
            "authorization_token_not_invocation",
            "authorization_token_not_command_success",
            "v1_not_repaired_hidden_or_claimed_passed",
            "no_raw_full_prior_artifact_body_returned",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(_false_non_claims(), summary["key_non_claims"])

    def test_request_builder_helper_preserves_inputs_and_resolves(self) -> None:
        additional = {"basis": "not needed for recorded but preserved"}
        not_recorded = {"reason": "not selected"}
        request = build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_request(
            "builder_request_001",
            QUESTION,
            _command_invocation_authorization_basis(),
            _command_invocation_authorization_terminal_summary_basis(),
            _command_invocation_authorization_boundary_basis(),
            _command_execution_review_basis(),
            _request_consumption_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _generic_basis("command_execution_boundary"),
            _generic_basis("command_report"),
            _generic_basis("command_implementation_boundary"),
            _generic_basis("command_boundary"),
            _generic_basis("artifact_emission_containment"),
            _generic_basis("evidence_manifest"),
            _generic_basis("portable_verification"),
            _posture("invocation_boundary_only_posture"),
            _posture("one_future_invocation_step_posture"),
            _posture("authorization_token_preserved_posture"),
            _posture("authorization_token_not_spent_posture"),
            _posture("no_command_invocation_posture"),
            _posture("no_command_execution_posture"),
            _posture("no_output_result_success_posture"),
            _posture("no_execution_permission_posture"),
            _posture("no_execution_approval_posture"),
            _posture("no_standing_lane_posture"),
            _posture("no_repeat_permission_posture"),
            _posture("consumed_token_closed_posture"),
            _posture("no_reopen_consumed_request_posture"),
            _posture("returned_result_containment_posture"),
            list(SUPPORTED_SCOPE),
            selected_command_invocation_authorization_result_path="authorization.json",
            selected_command_invocation_authorization_result_id="authorization-id",
            selected_command_invocation_authorization_result_outcome=COMMAND_INVOCATION_AUTHORIZATION_OUTCOME,
            selected_command_invocation_authorization_failed_check_count=0,
            selected_command_invocation_authorization_token_created=True,
            selected_command_invocation_authorization_token_is_one_shot=True,
            selected_command_invocation_authorization_boundary_result_path="boundary.json",
            selected_command_invocation_authorization_boundary_result_id="boundary-id",
            selected_command_invocation_authorization_boundary_result_outcome=COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME,
            selected_command_invocation_authorization_boundary_failed_check_count=0,
            selected_command_execution_review_result_path="review.json",
            selected_command_execution_review_result_id="review-id",
            selected_command_execution_review_result_outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
            selected_command_execution_review_failed_check_count=0,
            selected_request_consumption_result_path="consumption.json",
            selected_request_consumption_result_id="consumption-id",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="v2.json",
            selected_v2_admitted_request_artifact_id="v2-id",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            requested_command_invocation_boundary_outcome=RECORDED,
            additional_basis_context=additional,
            not_recorded_basis=not_recorded,
        )
        self.assertEqual("builder_request_001", request["command_invocation_boundary_request_id"])
        self.assertEqual(QUESTION, request["command_invocation_boundary_question"])
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_OUTCOME, request["selected_command_invocation_authorization_result_outcome"])
        self.assertEqual(COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_OUTCOME, request["selected_command_invocation_authorization_boundary_result_outcome"])
        self.assertEqual(COMMAND_EXECUTION_REVIEW_OUTCOME, request["selected_command_execution_review_result_outcome"])
        self.assertEqual(REQUEST_CONSUMPTION_OUTCOME, request["selected_request_consumption_result_outcome"])
        self.assertEqual(V2_ADMITTED_REQUEST_OUTCOME, request["selected_v2_admitted_request_outcome"])
        self.assertEqual(V2_ADMITTED_REQUEST_VERSION, request["selected_v2_admitted_request_version"])
        self.assertIs(request["selected_command_invocation_authorization_token_created"], True)
        self.assertIs(request["selected_command_invocation_authorization_token_is_one_shot"], True)
        self.assertEqual(list(SUPPORTED_SCOPE), request["command_invocation_boundary_scope"])
        self.assertEqual(additional, request["additional_basis_context"])
        self.assertEqual(not_recorded, request["not_recorded_basis"])
        self.assertEqual(_false_non_claims(), request["declared_non_claims"])
        recordable_request = copy.deepcopy(request)
        recordable_request.pop("additional_basis_context", None)
        recordable_request.pop("not_recorded_basis", None)
        result = _resolve(recordable_request)
        self.assertEqual(RECORDED, result["outcome"])

    def test_path_based_resolution_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path(
                request_path
            )
            self.assertEqual(RECORDED, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(str(request_path), path_result["declared_command_invocation_boundary_question"]["request_path"])

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path(
                malformed_path
            )
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertEqual("DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_UNREADABLE", malformed["block"]["code"])

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path(
                array_path
            )
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertEqual("DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED", array_result["block"]["code"])

            missing = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(BLOCKED, missing["outcome"])
            self.assertEqual("DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_UNREADABLE", missing["block"]["code"])

            output_path = tmp_path / "nested" / "boundary_result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result(
                mapping_result, output_path
            )
            self.assertTrue(written.exists())
            loaded = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, loaded)
            second = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result(
                mapping_result, output_path
            )
            self.assertNotEqual(written, second)
            self.assertTrue(second.name.endswith("_001.json"))

            default_root = tmp_path / "bounded_command_invocation_boundary"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_BOUNDARY_ROOT",
                default_root,
            ):
                default_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result(
                    mapping_result
                )
            self.assertTrue(default_written.exists())
            self.assertEqual(default_root, default_written.parent)
            self.assertNotIn("authorization_boundary", str(default_written.parent))
            self.assertNotIn("command_execution_review", str(default_written.parent))
            self.assertNotIn("deployment", str(default_written.parent))

    def test_reference_shaped_containment_blocks_full_prior_artifact_body(self) -> None:
        authorization_request = _set_nested(
            _valid_request(),
            "selected_command_invocation_authorization_basis",
            full_artifact_body=RAW_FULL_BODY_SENTINEL,
        )
        authorization_result = self.assert_blocked(authorization_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(authorization_result))
        self._assert_no_invocation_execution_success_or_token_spend(authorization_result)

        consumption_request = _set_nested(
            _valid_request(),
            "selected_request_consumption_basis",
            raw_result=RAW_FULL_BODY_SENTINEL,
        )
        consumption_result = self.assert_blocked(consumption_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(consumption_result))
        self._assert_no_invocation_execution_success_or_token_spend(consumption_result)

    def test_resolver_does_not_mutate_inputs(self) -> None:
        request = _valid_request()
        before = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(before, request)
        self.assertEqual(first["outcome"], second["outcome"])
        self.assertEqual(before["selected_command_invocation_authorization_basis"], request["selected_command_invocation_authorization_basis"])
        self.assertEqual(before["selected_command_invocation_authorization_terminal_summary_basis"], request["selected_command_invocation_authorization_terminal_summary_basis"])
        self.assertEqual(before["selected_command_invocation_authorization_boundary_basis"], request["selected_command_invocation_authorization_boundary_basis"])
        self.assertEqual(before["selected_command_execution_review_basis"], request["selected_command_execution_review_basis"])
        self.assertEqual(before["selected_request_consumption_basis"], request["selected_request_consumption_basis"])
        self.assertEqual(before["selected_consumed_request_basis"], request["selected_consumed_request_basis"])
        self.assertEqual(before["selected_v2_admitted_request_basis"], request["selected_v2_admitted_request_basis"])
        self.assertEqual(before["selected_v1_predecessor_failure_basis"], request["selected_v1_predecessor_failure_basis"])
        self.assertEqual(before["selected_command_execution_boundary_basis"], request["selected_command_execution_boundary_basis"])
        self.assertEqual(before["selected_command_report_basis"], request["selected_command_report_basis"])
        self.assertEqual(before["selected_command_implementation_boundary_basis"], request["selected_command_implementation_boundary_basis"])
        self.assertEqual(before["selected_command_boundary_basis"], request["selected_command_boundary_basis"])
        self.assertEqual(before["selected_artifact_emission_containment_basis"], request["selected_artifact_emission_containment_basis"])
        self.assertEqual(before["selected_evidence_manifest_basis"], request["selected_evidence_manifest_basis"])
        self.assertEqual(before["selected_portable_verification_basis"], request["selected_portable_verification_basis"])
        self.assertEqual(before["invocation_boundary_only_posture"], request["invocation_boundary_only_posture"])
        self.assertEqual(before["command_invocation_boundary_scope"], request["command_invocation_boundary_scope"])

        with tempfile.TemporaryDirectory() as tmp:
            output = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_boundary_result(
                first, Path(tmp) / "boundary" / "result.json"
            )
            self.assertTrue(output.exists())
            self.assertTrue(str(output).startswith(tmp))

    def test_blocking_missing_or_malformed_request_inputs(self) -> None:
        self.assert_blocked(None, "COMMAND_INVOCATION_BOUNDARY_QUESTION_UNDECLARED")
        self.assert_blocked(["not", "mapping"], "DECLARED_COMMAND_INVOCATION_BOUNDARY_REQUEST_MALFORMED")
        explicit = _valid_request(command_invocation_boundary_intent=resolver.INTENT_BLOCK)
        blocked = _resolve(explicit)
        self.assertEqual(BLOCKED, blocked["outcome"])
        self.assertEqual("COMMAND_INVOCATION_BOUNDARY_BLOCKED_BY_REQUEST", blocked["block"]["code"])

    def test_blocking_basis_and_posture_failures(self) -> None:
        cases = (
            (_drop(_valid_request(), "selected_command_invocation_authorization_basis"), "COMMAND_INVOCATION_AUTHORIZATION_BASIS_MISSING"),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_basis", outcome="WRONG"),
                    selected_command_invocation_authorization_result_outcome="WRONG",
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_NOT_RECORDED",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_basis", failed_check_count=1),
                    selected_command_invocation_authorization_failed_check_count=1,
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_FAILED_CHECKS_PRESENT",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_basis", command_invocation_authorization_token_created=False),
                    selected_command_invocation_authorization_token_created=False,
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_MISSING",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_basis", authorization_token_is_one_shot=False),
                    selected_command_invocation_authorization_token_is_one_shot=False,
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_NOT_ONE_SHOT",
            ),
            (_valid_request(authorization_token_spent_here=True), "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
            (_drop(_valid_request(), "selected_command_invocation_authorization_terminal_summary_basis"), "COMMAND_INVOCATION_AUTHORIZATION_TERMINAL_SUMMARY_MISSING"),
            (_drop(_valid_request(), "selected_command_invocation_authorization_boundary_basis"), "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BASIS_MISSING"),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_boundary_basis", outcome="WRONG"),
                    selected_command_invocation_authorization_boundary_result_outcome="WRONG",
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_invocation_authorization_boundary_basis", failed_check_count=1),
                    selected_command_invocation_authorization_boundary_failed_check_count=1,
                ),
                "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            (_drop(_valid_request(), "selected_command_execution_review_basis"), "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_execution_review_basis", outcome="WRONG"),
                    selected_command_execution_review_result_outcome="WRONG",
                ),
                "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_command_execution_review_basis", failed_check_count=1),
                    selected_command_execution_review_failed_check_count=1,
                ),
                "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
            ),
            (_drop(_valid_request(), "selected_request_consumption_basis"), "REQUEST_CONSUMPTION_BASIS_MISSING"),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_request_consumption_basis", outcome="WRONG"),
                    selected_request_consumption_result_outcome="WRONG",
                ),
                "REQUEST_CONSUMPTION_NOT_CONSUMED",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_request_consumption_basis", failed_check_count=1),
                    selected_request_consumption_failed_check_count=1,
                ),
                "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
            ),
            (_drop(_valid_request(), "selected_consumed_request_basis"), "CONSUMED_REQUEST_BASIS_MISSING"),
            (_set_nested(_valid_request(), "selected_consumed_request_basis", consumed_request_token_remains_closed=False, consumed_token_closed=False), "CONSUMED_TOKEN_NOT_CLOSED"),
            (_set_nested(_valid_request(), "selected_consumed_request_basis", consumed_request_reopened=True), "CONSUMED_REQUEST_REOPENED"),
            (_drop(_valid_request(), "selected_v2_admitted_request_basis"), "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_v2_admitted_request_basis", outcome="WRONG"),
                    selected_v2_admitted_request_outcome="WRONG",
                ),
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_v2_admitted_request_basis", result_version="0.1.0"),
                    selected_v2_admitted_request_version="0.1.0",
                ),
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            (
                _with_fields(
                    _set_nested(_valid_request(), "selected_v2_admitted_request_basis", failed_check_count=1),
                    selected_v2_failed_check_count=1,
                ),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (_set_nested(_valid_request(), "selected_v2_admitted_request_basis", successor_of="", successor_reason="", resolver_module=""), "V2_SUCCESSOR_METADATA_MISSING"),
            (_set_nested(_valid_request(), "selected_v2_admitted_request_basis", returned_result_containment_preserved=False, no_raw_full_prior_artifact_body_returned=False), "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
            (_drop(_valid_request(), "selected_v1_predecessor_failure_basis"), "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            (_set_nested(_valid_request(), "selected_v2_admitted_request_basis", v2_treated_as_repairing_v1=True), "V2_TREATED_AS_REPAIRING_V1"),
            (_set_nested(_valid_request(), "selected_v1_predecessor_failure_basis", v1_hidden=True), "V1_FAILURE_HIDDEN"),
            (_set_nested(_valid_request(), "selected_v1_predecessor_failure_basis", v1_claimed_passed=True), "V1_CLAIMED_PASSED"),
            (_drop(_valid_request(), "selected_command_execution_boundary_basis"), "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_command_report_basis"), "COMMAND_REPORT_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_command_implementation_boundary_basis"), "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_command_boundary_basis"), "COMMAND_BOUNDARY_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_artifact_emission_containment_basis"), "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_evidence_manifest_basis"), "EVIDENCE_MANIFEST_BASIS_MISSING"),
            (_drop(_valid_request(), "selected_portable_verification_basis"), "PORTABLE_VERIFICATION_BASIS_MISSING"),
            (_drop(_valid_request(), "invocation_boundary_only_posture"), "INVOCATION_BOUNDARY_ONLY_POSTURE_MISSING"),
            (_drop(_valid_request(), "one_future_invocation_step_posture"), "ONE_FUTURE_INVOCATION_STEP_POSTURE_MISSING"),
            (_drop(_valid_request(), "authorization_token_preserved_posture"), "AUTHORIZATION_TOKEN_PRESERVED_POSTURE_MISSING"),
            (_drop(_valid_request(), "authorization_token_not_spent_posture"), "AUTHORIZATION_TOKEN_NOT_SPENT_POSTURE_MISSING"),
            (_drop(_valid_request(), "no_standing_lane_posture"), "NO_STANDING_LANE_POSTURE_MISSING"),
            (_drop(_valid_request(), "no_repeat_permission_posture"), "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
            (_valid_request(command_invocation_boundary_scope=["UNSUPPORTED_SCOPE"]), "UNSUPPORTED_COMMAND_INVOCATION_BOUNDARY_SCOPE"),
        )
        for request, expected in cases:
            with self.subTest(expected=expected):
                self.assert_blocked(request, expected)

    def test_blocking_collapse_flags(self) -> None:
        cases = (
            ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
            ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("execution_permission_created", "EXECUTION_PERMISSION_CREATED"),
            ("execution_approval_created", "EXECUTION_APPROVAL_CREATED"),
            ("authorization_token_spent_here", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
            ("authorization_token_spent", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
            ("command_invocation_authorization_token_spent", "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE"),
            ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
            ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
            ("invocation_boundary_treated_as_invocation", "INVOCATION_BOUNDARY_TREATED_AS_INVOCATION"),
            ("invocation_boundary_treated_as_execution", "INVOCATION_BOUNDARY_TREATED_AS_EXECUTION"),
            ("invocation_boundary_treated_as_command_success", "INVOCATION_BOUNDARY_TREATED_AS_COMMAND_SUCCESS"),
            ("authorization_token_treated_as_invocation", "AUTHORIZATION_TOKEN_TREATED_AS_INVOCATION"),
            ("authorization_token_treated_as_command_success", "AUTHORIZATION_TOKEN_TREATED_AS_COMMAND_SUCCESS"),
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
        for flag, expected in cases:
            request = _valid_request()
            request[flag] = True
            with self.subTest(flag=flag):
                self.assert_blocked(request, expected)

        reopened = _set_nested(_valid_request(), "selected_consumed_request_basis", consumed_request_reopened=True)
        self.assert_blocked(reopened, "CONSUMED_REQUEST_REOPENED")

        token_reuse = _valid_request()
        token_reuse["selected_command_invocation_authorization_basis"]["command_invocation_authorization_token_spent"] = True
        token_reuse["selected_command_invocation_authorization_basis"]["authorization_token_reused"] = True
        token_reuse["selected_command_invocation_authorization_basis"]["authorization_token_consumed"] = True
        token_reuse["selected_command_invocation_authorization_basis"]["authorization_token_discharged"] = True
        self.assert_blocked(token_reuse, "COMMAND_INVOCATION_AUTHORIZATION_TOKEN_SPENT_HERE")

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        request = _valid_request(mutation_performed=True, replay_performed=True, merge_performed=True)
        self.assert_blocked(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_invocation_created")
        self.assert_blocked(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["full_prior_artifacts_embedded"] = True
        self.assert_blocked(flipped_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")


if __name__ == "__main__":
    unittest.main()
