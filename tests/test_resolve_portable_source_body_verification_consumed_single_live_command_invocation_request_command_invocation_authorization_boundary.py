"""Tests for the consumed-request command invocation authorization boundary resolver.

This file is intentionally bounded to command invocation authorization boundary
recording only. The fixtures do not model command invocation authorization,
command invocation, command execution, command output, command result, command
success, execution permission, execution approval, deployment, runtime hosting,
public release, continuation, reusable permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.dont_write_bytecode = True

REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary as resolver
from resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary import (
    build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_request,
    build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path,
    write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_QUESTION
COMMAND_EXECUTION_REVIEW_OUTCOME = resolver.COMMAND_EXECUTION_REVIEW_OUTCOME
EXECUTION_REVIEW_BOUNDARY_OUTCOME = resolver.EXECUTION_REVIEW_BOUNDARY_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V2_RESOLVER_MODULE = resolver.V2_RESOLVER_MODULE
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE))
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
FULL_BODY_OMISSION_MARKER = resolver.FULL_BODY_OMISSION_MARKER
RAW_FULL_BODY_SENTINEL = "RAW_FULL_BODY_VALUE_MUST_NOT_RETURN_" * 8

TOP_LEVEL_SECTIONS = (
    "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_metadata",
    "declared_command_invocation_authorization_boundary_question",
    "selected_command_execution_review_basis",
    "selected_command_execution_review_terminal_summary_basis",
    "selected_execution_review_boundary_basis",
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
    "authorization_boundary_only_posture",
    "one_future_authorization_review_posture",
    "reviewed_command_execution_review_basis_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "no_command_invocation_authorization_posture",
    "no_command_invocation_posture",
    "no_command_execution_posture",
    "no_output_result_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "returned_result_containment_posture",
    "command_invocation_authorization_boundary_scope",
    "command_invocation_authorization_boundary_checks",
    "command_invocation_authorization_boundary_statement",
    "command_invocation_authorization_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary",
)

OPEN_ITEMS = (
    "command invocation authorization boundary test",
    "command invocation authorization boundary live artifact",
    "actual command invocation authorization review",
    "command invocation authorization",
    "command invocation",
    "command execution",
    "command output",
    "command result",
    "command success",
    "command output/report artifact from live execution",
    "manifest implementation",
    "checksum implementation",
    "signature implementation",
    "source-body packet implementation",
    "reproducible environment declaration",
    "runtime hosting",
    "deployment",
    "public release",
    "source transfer",
    "source migration",
    "source receipt",
    "reception authorization",
    "derivative reception",
    "vessel relation",
    "adoption",
    "authority creation",
    "currentness creation",
    "operation permission",
    "public readiness",
    "final completion",
    "continuation",
    "publication flow",
    "reusable permission",
    "successor reception request",
    "follow-on work",
)


def _false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_FALSE_NON_CLAIMS}


def _reference_shape(label: str, **extra: object) -> dict[str, object]:
    basis: dict[str, object] = {
        "basis_label": label,
        "declared": True,
        "basis_reference": f"synthetic://{label}",
        "reference_shaped_basis": True,
        "basis_remains_basis_only": True,
        "basis_is_not_command_invocation_authorization": True,
        "basis_is_not_command_invocation": True,
        "basis_is_not_command_execution": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_execution_permission_or_approval": True,
        "basis_is_not_authority_currentness_final_completion": True,
        "basis_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "basis_does_not_create_standing_lane_or_repeat_permission": True,
        "full_prior_artifact_body_not_emitted": True,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _command_execution_review_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "command_execution_review",
        result_id="command_execution_review_reference_review_001",
        result_path="artifacts/synthetic_command_execution_review_result.json",
        outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        command_execution_review_basis_remains_review_basis_only=True,
        command_execution_review_did_not_create_command_invocation_authorization=True,
        command_execution_review_did_not_authorize_invocation_execution_output_result_success=True,
        command_execution_review_did_not_create_execution_permission_or_approval=True,
        command_execution_review_did_not_create_standing_lane_repeat_permission_final_completion_continuation_reusable_permission_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_execution_review_terminal_summary_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "command_execution_review_terminal_summary",
        terminal_summary_declared=True,
        terminal_summary_path="spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_TERMINAL_SUMMARY_V0.md",
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_invocation_authorization=True,
        terminal_summary_does_not_authorize_command_invocation=True,
        terminal_summary_does_not_authorize_command_execution=True,
        terminal_summary_does_not_create_command_output_result_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _execution_review_boundary_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "execution_review_boundary",
        result_id="execution_review_boundary_reference_record_001",
        result_path="artifacts/synthetic_execution_review_boundary_result.json",
        outcome=EXECUTION_REVIEW_BOUNDARY_OUTCOME,
        failed_check_count=0,
        execution_review_boundary_basis_remains_boundary_basis_only=True,
        execution_review_boundary_did_not_perform_command_execution_review=True,
        execution_review_boundary_did_not_create_command_invocation_authorization=True,
        execution_review_boundary_did_not_authorize_invocation_execution_output_result_success=True,
        execution_review_boundary_did_not_create_execution_permission_or_approval=True,
    )
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "request_consumption",
        result_id="request_consumption_reference_record_001",
        result_path="artifacts/synthetic_request_consumption_result.json",
        outcome=REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        request_consumed=True,
        admitted_single_live_command_invocation_request_consumed=True,
        consumption_token_closed=True,
        consumed_token_closed=True,
        consumed_request_basis_recorded=True,
        request_consumption_basis_does_not_create_command_invocation_authorization=True,
        request_consumption_basis_does_not_authorize_invocation_execution_output_result_success=True,
        request_consumption_basis_does_not_create_execution_permission_or_approval=True,
        request_consumption_basis_does_not_create_standing_lane_or_repeat_permission=True,
    )
    basis.update(extra)
    return basis


def _consumed_request_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "consumed_request",
        consumed_request_basis_declared=True,
        consumed_request_basis_recorded=True,
        consumed_request_token_remains_closed=True,
        consumed_request_token_closed=True,
        consumed_request_not_reopened=True,
        consumed_request_basis_is_not_command_invocation_authorization=True,
        consumed_request_basis_is_not_command_success=True,
        consumed_request_basis_for_one_future_authorization_review_only=True,
    )
    basis.update(extra)
    return basis


def _v2_admitted_request_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "v2_admitted_request",
        result_id="v2_admission_reference_record_001",
        result_path="artifacts/synthetic_v2_admission_result.json",
        outcome=V2_ADMITTED_REQUEST_OUTCOME,
        result_version=V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        passed_check_count=37,
        successor_of=V1_PREDECESSOR_RESOLVER_MODULE,
        successor_reason="synthetic v2 successor preserves returned-result containment",
        resolver_module=V2_RESOLVER_MODULE,
        returned_result_containment_preserved=True,
        raw_full_prior_artifact_values_omitted=True,
        v2_remains_lineage_evidence_only=True,
        v2_does_not_claim_v1_passed=True,
    )
    basis.update(extra)
    return basis


def _v1_predecessor_failure_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape(
        "v1_predecessor_failure",
        selected_result_id="v1_predecessor_failure_reference_001",
        selected_result_path="artifacts/synthetic_v1_predecessor_failure_result.json",
        selected_result_outcome="SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_BLOCKED",
        v1_predecessor_failure_basis_declared=True,
        v1_predecessor_failure_remains_visible=True,
        v1_is_not_repaired=True,
        v1_is_not_hidden=True,
        v1_is_not_claimed_passed=True,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
    )
    basis.update(extra)
    return basis


def _command_execution_boundary_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("command_execution_boundary", result_path="artifacts/synthetic_command_execution_boundary_result.json")
    basis.update(extra)
    return basis


def _command_report_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("command_report", result_path="artifacts/synthetic_command_report.json")
    basis.update(extra)
    return basis


def _command_implementation_boundary_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("command_implementation_boundary", result_path="artifacts/synthetic_command_implementation_boundary_result.json")
    basis.update(extra)
    return basis


def _command_boundary_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("command_boundary", result_path="artifacts/synthetic_command_boundary_result.json")
    basis.update(extra)
    return basis


def _artifact_emission_containment_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("artifact_emission_containment", result_path="artifacts/synthetic_artifact_emission_containment_result.json")
    basis.update(extra)
    return basis


def _evidence_manifest_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("evidence_manifest", result_path="artifacts/synthetic_evidence_manifest_result.json")
    basis.update(extra)
    return basis


def _portable_verification_basis(**extra: object) -> dict[str, object]:
    basis = _reference_shape("portable_verification", result_path="artifacts/synthetic_portable_verification_result.json")
    basis.update(extra)
    return basis


def _posture(label: str, **extra: object) -> dict[str, object]:
    posture: dict[str, object] = {
        "posture_label": label,
        "declared": True,
        f"{label}_declared": True,
        "authorization_boundary_only_posture_declared": True,
        "one_future_authorization_review_posture_declared": True,
        "reviewed_command_execution_review_basis_posture_declared": True,
        "consumed_token_closed_posture_declared": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "command_invocation_authorization_not_created": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_not_returned": True,
        "reference_shaped_posture": True,
    }
    posture.update(extra)
    return posture


def _valid_request(**extra: object) -> dict[str, object]:
    request: dict[str, object] = {
        "command_invocation_authorization_boundary_request_id": "command_invocation_authorization_boundary_reference_001",
        "command_invocation_authorization_boundary_question": QUESTION,
        "command_invocation_authorization_boundary_intent": resolver.INTENT_RECORD,
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_command_execution_review_terminal_summary_basis": _command_execution_review_terminal_summary_basis(),
        "selected_execution_review_boundary_basis": _execution_review_boundary_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_basis": _command_execution_boundary_basis(),
        "selected_command_report_basis": _command_report_basis(),
        "selected_command_implementation_boundary_basis": _command_implementation_boundary_basis(),
        "selected_command_boundary_basis": _command_boundary_basis(),
        "selected_artifact_emission_containment_basis": _artifact_emission_containment_basis(),
        "selected_evidence_manifest_basis": _evidence_manifest_basis(),
        "selected_portable_verification_basis": _portable_verification_basis(),
        "authorization_boundary_only_posture": _posture("authorization_boundary_only_posture"),
        "one_future_authorization_review_posture": _posture("one_future_authorization_review_posture"),
        "reviewed_command_execution_review_basis_posture": _posture("reviewed_command_execution_review_basis_posture"),
        "consumed_token_closed_posture": _posture("consumed_token_closed_posture"),
        "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request_posture"),
        "no_command_invocation_authorization_posture": _posture("no_command_invocation_authorization_posture"),
        "no_command_invocation_posture": _posture("no_command_invocation_posture"),
        "no_command_execution_posture": _posture("no_command_execution_posture"),
        "no_output_result_success_posture": _posture("no_output_result_success_posture"),
        "no_execution_permission_posture": _posture("no_execution_permission_posture"),
        "no_execution_approval_posture": _posture("no_execution_approval_posture"),
        "no_standing_lane_posture": _posture("no_standing_lane_posture"),
        "no_repeat_permission_posture": _posture("no_repeat_permission_posture"),
        "returned_result_containment_posture": _posture("returned_result_containment_posture"),
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_basis_required": True,
            "full_prior_artifact_body_not_emitted": True,
        },
        "command_invocation_authorization_boundary_scope": list(SUPPORTED_SCOPE),
        "selected_command_execution_review_result_path": "artifacts/synthetic_command_execution_review_result.json",
        "selected_command_execution_review_result_id": "command_execution_review_reference_review_001",
        "selected_command_execution_review_result_outcome": COMMAND_EXECUTION_REVIEW_OUTCOME,
        "selected_command_execution_review_failed_check_count": 0,
        "selected_command_execution_review_terminal_summary_path": "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_TERMINAL_SUMMARY_V0.md",
        "selected_execution_review_boundary_result_path": "artifacts/synthetic_execution_review_boundary_result.json",
        "selected_execution_review_boundary_result_id": "execution_review_boundary_reference_record_001",
        "selected_execution_review_boundary_result_outcome": EXECUTION_REVIEW_BOUNDARY_OUTCOME,
        "selected_execution_review_boundary_failed_check_count": 0,
        "selected_request_consumption_result_path": "artifacts/synthetic_request_consumption_result.json",
        "selected_request_consumption_result_id": "request_consumption_reference_record_001",
        "selected_request_consumption_result_outcome": REQUEST_CONSUMPTION_OUTCOME,
        "selected_request_consumption_failed_check_count": 0,
        "selected_v2_admitted_request_artifact_path": "artifacts/synthetic_v2_admission_result.json",
        "selected_v2_admitted_request_artifact_id": "v2_admission_reference_record_001",
        "selected_v2_admitted_request_outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
        "selected_v2_successor_metadata": {
            "successor_of": V1_PREDECESSOR_RESOLVER_MODULE,
            "successor_reason": "synthetic v2 successor preserves returned-result containment",
            "resolver_module": V2_RESOLVER_MODULE,
        },
        "selected_v1_predecessor_artifact_path": "artifacts/synthetic_v1_predecessor_failure_result.json",
        "selected_v1_predecessor_artifact_id": "v1_predecessor_failure_reference_001",
        "selected_v1_predecessor_outcome": "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_BLOCKED",
        "selected_command_execution_boundary_result_path": "artifacts/synthetic_command_execution_boundary_result.json",
        "selected_command_report_path": "artifacts/synthetic_command_report.json",
        "selected_command_implementation_boundary_result_path": "artifacts/synthetic_command_implementation_boundary_result.json",
        "selected_command_boundary_result_path": "artifacts/synthetic_command_boundary_result.json",
        "selected_artifact_emission_containment_result_path": "artifacts/synthetic_artifact_emission_containment_result.json",
        "selected_evidence_manifest_result_path": "artifacts/synthetic_evidence_manifest_result.json",
        "selected_portable_verification_result_path": "artifacts/synthetic_portable_verification_result.json",
        "requested_command_invocation_authorization_boundary_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
    }
    request.update(extra)
    return request


def _resolve(request: object | None = None) -> dict[str, object]:
    if request is None:
        return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary()
    return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary(
        declared_command_invocation_authorization_boundary_request=request
    )


def _block_code(result: dict[str, object]) -> object:
    block = result.get("block")
    if isinstance(block, dict):
        return block.get("block_code")
    return None


def _summary(result: dict[str, object]) -> dict[str, object]:
    summary = result.get("consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary")
    assert isinstance(summary, dict)
    return summary


def _checks(result: dict[str, object]) -> dict[str, object]:
    checks = result.get("command_invocation_authorization_boundary_checks")
    assert isinstance(checks, dict)
    return checks


def _statement(result: dict[str, object]) -> dict[str, object]:
    statement = result.get("command_invocation_authorization_boundary_statement")
    assert isinstance(statement, dict)
    return statement


def _json_text(value: object) -> str:
    return json.dumps(value, sort_keys=True)


class ConsumedSingleLiveCommandInvocationRequestCommandInvocationAuthorizationBoundaryTests(unittest.TestCase):
    maxDiff = None

    def assertRecordedBoundaryOnly(self, result: dict[str, object]) -> None:
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(_block_code(result))
        self.assertEqual(_checks(result)["failed_check_count"], 0)
        statement = _statement(result)
        for key in resolver.ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(statement[key], True)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(statement[key], False)
            self.assertIs(result["non_claims"][key], False)
        for key in (
            "command_invocation_authorization_created",
            "command_invocation_created",
            "command_executed",
            "command_execution_performed",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "execution_permission_created",
            "execution_approval_created",
            "standing_invocation_lane_created",
            "repeat_invocation_permission_created",
            "authorization_boundary_treated_as_authorization",
            "authorization_boundary_treated_as_invocation",
            "reviewed_basis_treated_as_command_invocation_authorization",
            "reviewed_basis_treated_as_command_success",
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
        ):
            self.assertIs(statement[key], False, key)

    def assertNoAuthorizationInvocationExecutionOrFollowOn(self, result: dict[str, object]) -> None:
        statement = _statement(result)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False)
        self.assertIs(statement["command_invocation_authorization_not_created"], True)
        self.assertIs(statement["command_invocation_not_created"], True)
        self.assertIs(statement["command_execution_not_performed"], True)
        self.assertIs(statement["command_output_not_created"], True)
        self.assertIs(statement["command_result_not_created"], True)
        self.assertIs(statement["command_success_not_created"], True)
        self.assertIs(statement["execution_permission_not_created"], True)
        self.assertIs(statement["execution_approval_not_created"], True)
        self.assertIs(statement["no_standing_invocation_lane_created"], True)
        self.assertIs(statement["no_repeat_invocation_permission_created"], True)
        self.assertIs(statement["consumed_request_not_reopened"], True)
        self.assertIs(statement["artifacts_not_mutated"], True)
        self.assertIs(statement["continuation_reusable_permission_follow_on_work_not_authorized"], True)
        self.assertIs(statement["derivative_reception_vessel_relation_another_reception_request_not_authorized"], True)

    def assertBlocks(self, request: object, expected_code: str) -> None:
        result = _resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(_block_code(result), expected_code)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

    def test_successful_command_invocation_authorization_boundary_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertRecordedBoundaryOnly(result)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(result["block"]["block_code"], None)
        self.assertEqual(result["block"]["block_reason"], None)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))

    def test_metadata_and_lineage_sections_are_preserved(self) -> None:
        result = _resolve(_valid_request())
        metadata = result["consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_metadata"]
        self.assertTrue(metadata["consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_id"])
        self.assertTrue(metadata["consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_type"])
        self.assertEqual(metadata["consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result_version"], "0.1.0")
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        review = result["selected_command_execution_review_basis"]
        self.assertEqual(review["selected_command_execution_review_result_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(review["selected_command_execution_review_failed_check_count"], 0)
        self.assertIs(review["command_execution_review_basis_remains_review_basis_only"], True)
        self.assertIs(review["command_execution_review_did_not_create_command_invocation_authorization"], True)
        self.assertIs(review["command_execution_review_did_not_authorize_invocation_execution_output_result_success"], True)
        self.assertIs(review["selected_basis_is_reference_shaped"], True)

        terminal = result["selected_command_execution_review_terminal_summary_basis"]
        self.assertIs(terminal["terminal_summary_remains_readability_basis_only"], True)
        self.assertIs(terminal["terminal_summary_does_not_create_command_invocation_authorization"], True)
        self.assertIs(terminal["terminal_summary_does_not_authorize_command_invocation"], True)
        self.assertIs(terminal["terminal_summary_does_not_authorize_command_execution"], True)

        boundary = result["selected_execution_review_boundary_basis"]
        self.assertEqual(boundary["selected_execution_review_boundary_result_outcome"], EXECUTION_REVIEW_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["selected_execution_review_boundary_failed_check_count"], 0)
        self.assertIs(boundary["execution_review_boundary_basis_remains_boundary_basis_only"], True)
        self.assertIs(boundary["execution_review_boundary_did_not_create_command_invocation_authorization"], True)

        consumption = result["selected_request_consumption_basis"]
        self.assertEqual(consumption["selected_request_consumption_result_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(consumption["selected_request_consumption_failed_check_count"], 0)
        self.assertIs(consumption["request_consumed_exactly_once"], True)
        self.assertIs(consumption["consumption_token_closed"], True)
        self.assertIs(consumption["consumed_request_basis_recorded"], True)
        self.assertIs(consumption["request_consumption_basis_does_not_create_command_invocation_authorization"], True)

        consumed = result["selected_consumed_request_basis"]
        self.assertIs(consumed["consumed_request_token_remains_closed"], True)
        self.assertIs(consumed["consumed_request_not_reopened"], True)
        self.assertIs(consumed["consumed_request_basis_is_not_command_invocation_authorization"], True)
        self.assertIs(consumed["consumed_request_basis_is_not_command_success"], True)

        v2 = result["selected_v2_admitted_request_basis"]
        self.assertEqual(v2["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(v2["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(v2["selected_v2_failed_check_count"], 0)
        self.assertIs(v2["selected_v2_successor_metadata_preserved"], True)
        self.assertIs(v2["selected_v2_returned_result_containment_preserved"], True)
        self.assertIs(v2["selected_basis_is_reference_shaped"], True)

        v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertIs(v1["v1_predecessor_failure_remains_visible"], True)
        self.assertIs(v1["v1_is_not_repaired"], True)
        self.assertIs(v1["v1_is_not_hidden"], True)
        self.assertIs(v1["v1_is_not_claimed_passed"], True)
        self.assertIs(v1["v2_successor_does_not_erase_v1"], True)
        self.assertIs(v1["predecessor_failure_evidence_is_lineage_evidence_only"], True)

    def test_command_invocation_authorization_boundary_checks_are_explicit_and_pass(self) -> None:
        result = _resolve(_valid_request())
        checks = _checks(result)
        records = checks["records"]
        self.assertGreaterEqual(len(records), 60)
        self.assertEqual(checks["failed_check_count"], 0)
        self.assertTrue(all(check["passed"] is True for check in records))
        for record in records:
            self.assertIn("check_name", record)
            self.assertIn("passed", record)
            self.assertIn("expected_posture", record)
            self.assertIn("actual_posture", record)
            self.assertIn("block_code", record)
            self.assertIn("failure_code", record)

        names = {record["check_name"] for record in records}
        expected_names = {
            "command invocation authorization boundary question declared",
            "command invocation authorization boundary intent supported",
            "command execution review terminal summary basis declared",
            "command execution review live artifact basis declared",
            "command execution review live artifact recorded outcome",
            "command execution review live artifact failed check count zero",
            "execution-review boundary basis declared",
            "execution-review boundary live artifact recorded outcome",
            "execution-review boundary live artifact failed check count zero",
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
            "v2 does not repair v1",
            "command execution boundary basis declared",
            "command report basis declared",
            "command implementation boundary basis declared",
            "command boundary basis declared",
            "artifact emission containment basis declared",
            "evidence-manifest basis declared",
            "portable verification basis declared",
            "authorization-boundary-only posture declared",
            "one-future-authorization-review posture declared",
            "no-command-invocation-authorization posture declared",
            "no-command-invocation posture declared",
            "no-command-execution posture declared",
            "no-output/result/success posture declared",
            "no-execution-permission posture declared",
            "no-execution-approval posture declared",
            "no-standing-lane posture declared",
            "no-repeat-permission posture declared",
            "command invocation authorization not created",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "execution permission not created",
            "execution approval not created",
            "standing invocation lane not created",
            "repeat invocation permission not created",
            "authorization boundary not authorization",
            "authorization boundary not invocation",
            "reviewed basis not command invocation authorization",
            "reviewed basis not command success",
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

    def test_command_invocation_authorization_boundary_non_meaning_is_preserved(self) -> None:
        result = _resolve(_valid_request())
        non_meaning = result["command_invocation_authorization_boundary_non_meaning"]
        expected = (
            "authorization_boundary_does_not_mean_command_invocation_authorization_exists",
            "authorization_boundary_does_not_mean_command_invocation_permission_exists",
            "authorization_boundary_does_not_mean_command_invocation_created",
            "authorization_boundary_does_not_mean_command_executed",
            "authorization_boundary_does_not_mean_command_output_exists",
            "authorization_boundary_does_not_mean_command_result_exists",
            "authorization_boundary_does_not_mean_command_success_exists",
            "authorization_boundary_does_not_mean_execution_permission_exists",
            "authorization_boundary_does_not_mean_execution_approval_exists",
            "authorization_boundary_does_not_mean_command_success_creates_currentness",
            "authorization_boundary_does_not_mean_command_success_claims_final_completion",
            "authorization_boundary_does_not_mean_command_output_becomes_source",
            "authorization_boundary_does_not_mean_command_result_becomes_authority",
            "authorization_boundary_does_not_mean_standing_invocation_lane_exists",
            "authorization_boundary_does_not_mean_repeat_invocation_permission_exists",
            "authorization_boundary_does_not_mean_consumed_request_token_reopened",
            "authorization_boundary_does_not_mean_v1_was_repaired",
            "authorization_boundary_does_not_mean_v1_was_hidden",
            "authorization_boundary_does_not_mean_v1_passed",
            "authorization_boundary_does_not_mean_deployment_created",
            "authorization_boundary_does_not_mean_runtime_hosting_created",
            "authorization_boundary_does_not_mean_public_release_created",
            "authorization_boundary_does_not_mean_public_readiness_created",
            "authorization_boundary_does_not_mean_final_completion_claimed",
            "authorization_boundary_does_not_mean_continuation_authorized",
            "authorization_boundary_does_not_mean_reusable_permission_created",
            "authorization_boundary_does_not_mean_derivative_reception_authorized",
            "authorization_boundary_does_not_mean_vessel_relation_authorized",
            "authorization_boundary_does_not_mean_another_reception_request_authorized",
            "authorization_boundary_does_not_mean_follow_on_work_authorized",
        )
        for key in expected:
            self.assertIs(non_meaning[key], True, key)

    def test_additional_basis_outcome_preserves_missing_basis_without_authorization(self) -> None:
        request = _valid_request(
            requested_command_invocation_authorization_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={
                "command_execution_review_basis_unclear": True,
                "no_standing_lane_posture_unclear": True,
                "non_claims_incomplete_but_not_flipped": True,
            },
        )
        result = _resolve(request)

        self.assertEqual(result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertFalse(result["additional_basis_required"]["missing_basis_not_scheduled"] is False)
        self.assertIs(result["additional_basis_required"]["additional_basis_required"], True)
        self.assertEqual(
            result["additional_basis_required"]["additional_basis_context"],
            request["additional_basis_context"],
        )
        self.assertIs(result["additional_basis_required"]["missing_basis_not_authorized"], True)
        self.assertIs(result["additional_basis_required"]["missing_basis_not_executed"], True)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

    def test_not_recorded_outcome_preserves_reason_without_next_work(self) -> None:
        request = _valid_request(
            requested_command_invocation_authorization_boundary_outcome=NOT_RECORDED,
            not_recorded_basis={
                "authorization_boundary_basis_cannot_be_bounded": True,
                "returned_result_containment_cannot_be_preserved": True,
            },
        )
        result = _resolve(request)

        self.assertEqual(result["outcome"], NOT_RECORDED)
        self.assertIs(result["not_recorded_basis"]["not_recorded"], True)
        self.assertEqual(result["not_recorded_basis"]["not_recorded_basis"], request["not_recorded_basis"])
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_mutate"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_repair_prior_artifacts"], True)
        self.assertIs(result["not_recorded_basis"]["not_recorded_does_not_authorize_follow_on_work"], True)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

    def test_what_remains_open_and_summary_helper(self) -> None:
        result = _resolve(_valid_request())
        remains_open = result["what_remains_open"]
        self.assertEqual(remains_open["open_items"], list(OPEN_ITEMS))
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

        summary = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_summary(result)
        self.assertEqual(summary, _summary(result))
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["command_invocation_authorization_boundary_request_id"], "command_invocation_authorization_boundary_reference_001")
        self.assertEqual(summary["command_invocation_authorization_boundary_question"], QUESTION)
        self.assertEqual(summary["command_invocation_authorization_boundary_intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "command_invocation_authorization_boundary_recorded",
            "reviewed_command_execution_review_basis_preserved",
            "consumed_request_token_remains_closed",
            "single_authorization_review_conditions_declared",
            "authorization_still_not_created",
            "invocation_still_not_authorized",
            "invocation_requires_separate_authorization_result",
            "execution_still_not_authorized",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "command_invocation_authorization_not_created",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "no_standing_lane",
            "no_repeat_permission",
            "consumed_request_not_reopened",
            "authorization_boundary_not_authorization",
            "authorization_boundary_not_invocation",
            "reviewed_basis_not_command_invocation_authorization",
            "reviewed_basis_not_command_success",
            "v1_not_repaired",
            "v1_not_hidden",
            "v1_not_claimed_passed",
            "no_raw_full_prior_artifact_body_returned",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work",
        ):
            self.assertIs(summary[key], True, key)
        self.assertEqual(summary["selected_command_execution_review_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(summary["selected_command_execution_review_failed_check_count"], 0)
        self.assertEqual(summary["selected_execution_review_boundary_outcome"], EXECUTION_REVIEW_BOUNDARY_OUTCOME)
        self.assertEqual(summary["selected_execution_review_boundary_failed_check_count"], 0)
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_request_consumption_failed_check_count"], 0)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["selected_v2_failed_check_count"], 0)
        self.assertEqual(summary["key_non_claims"], _false_non_claims())

    def test_request_builder_helper_preserves_inputs_and_resolves(self) -> None:
        bases = {
            "selected_command_execution_review_basis": _command_execution_review_basis(),
            "selected_command_execution_review_terminal_summary_basis": _command_execution_review_terminal_summary_basis(),
            "selected_execution_review_boundary_basis": _execution_review_boundary_basis(),
            "selected_request_consumption_basis": _request_consumption_basis(),
            "selected_consumed_request_basis": _consumed_request_basis(),
            "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
            "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
            "selected_command_execution_boundary_basis": _command_execution_boundary_basis(),
            "selected_command_report_basis": _command_report_basis(),
            "selected_command_implementation_boundary_basis": _command_implementation_boundary_basis(),
            "selected_command_boundary_basis": _command_boundary_basis(),
            "selected_artifact_emission_containment_basis": _artifact_emission_containment_basis(),
            "selected_evidence_manifest_basis": _evidence_manifest_basis(),
            "selected_portable_verification_basis": _portable_verification_basis(),
        }
        postures = {
            "authorization_boundary_only_posture": _posture("authorization_boundary_only_posture"),
            "one_future_authorization_review_posture": _posture("one_future_authorization_review_posture"),
            "reviewed_command_execution_review_basis_posture": _posture("reviewed_command_execution_review_basis_posture"),
            "consumed_token_closed_posture": _posture("consumed_token_closed_posture"),
            "no_reopen_consumed_request_posture": _posture("no_reopen_consumed_request_posture"),
            "no_command_invocation_authorization_posture": _posture("no_command_invocation_authorization_posture"),
            "no_command_invocation_posture": _posture("no_command_invocation_posture"),
            "no_command_execution_posture": _posture("no_command_execution_posture"),
            "no_output_result_success_posture": _posture("no_output_result_success_posture"),
            "no_execution_permission_posture": _posture("no_execution_permission_posture"),
            "no_execution_approval_posture": _posture("no_execution_approval_posture"),
            "no_standing_lane_posture": _posture("no_standing_lane_posture"),
            "no_repeat_permission_posture": _posture("no_repeat_permission_posture"),
            "returned_result_containment_posture": _posture("returned_result_containment_posture"),
        }

        request = build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_request(
            "builder_request_001",
            QUESTION,
            bases["selected_command_execution_review_basis"],
            bases["selected_command_execution_review_terminal_summary_basis"],
            bases["selected_execution_review_boundary_basis"],
            bases["selected_request_consumption_basis"],
            bases["selected_consumed_request_basis"],
            bases["selected_v2_admitted_request_basis"],
            bases["selected_v1_predecessor_failure_basis"],
            bases["selected_command_execution_boundary_basis"],
            bases["selected_command_report_basis"],
            bases["selected_command_implementation_boundary_basis"],
            bases["selected_command_boundary_basis"],
            bases["selected_artifact_emission_containment_basis"],
            bases["selected_evidence_manifest_basis"],
            bases["selected_portable_verification_basis"],
            postures["authorization_boundary_only_posture"],
            postures["one_future_authorization_review_posture"],
            postures["reviewed_command_execution_review_basis_posture"],
            postures["consumed_token_closed_posture"],
            postures["no_reopen_consumed_request_posture"],
            postures["no_command_invocation_authorization_posture"],
            postures["no_command_invocation_posture"],
            postures["no_command_execution_posture"],
            postures["no_output_result_success_posture"],
            postures["no_execution_permission_posture"],
            postures["no_execution_approval_posture"],
            postures["no_standing_lane_posture"],
            postures["no_repeat_permission_posture"],
            postures["returned_result_containment_posture"],
            list(SUPPORTED_SCOPE),
            selected_command_execution_review_result_path="review/result.json",
            selected_command_execution_review_result_id="review-result-id",
            selected_command_execution_review_result_outcome=COMMAND_EXECUTION_REVIEW_OUTCOME,
            selected_command_execution_review_failed_check_count=0,
            selected_execution_review_boundary_result_path="boundary/result.json",
            selected_execution_review_boundary_result_id="boundary-result-id",
            selected_execution_review_boundary_result_outcome=EXECUTION_REVIEW_BOUNDARY_OUTCOME,
            selected_execution_review_boundary_failed_check_count=0,
            selected_request_consumption_result_path="consumption/result.json",
            selected_request_consumption_result_id="consumption-result-id",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="v2/result.json",
            selected_v2_admitted_request_artifact_id="v2-result-id",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            requested_command_invocation_authorization_boundary_outcome=RECORDED,
            additional_basis_context={"preserved_for_requires_case": True},
            not_recorded_basis={"preserved_for_not_recorded_case": True},
        )

        self.assertEqual(request["command_invocation_authorization_boundary_request_id"], "builder_request_001")
        self.assertEqual(request["command_invocation_authorization_boundary_question"], QUESTION)
        for key, value in bases.items():
            self.assertEqual(request[key], value)
        for key, value in postures.items():
            self.assertEqual(request[key], value)
        self.assertEqual(request["command_invocation_authorization_boundary_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_command_execution_review_result_path"], "review/result.json")
        self.assertEqual(request["selected_command_execution_review_result_id"], "review-result-id")
        self.assertEqual(request["selected_command_execution_review_result_outcome"], COMMAND_EXECUTION_REVIEW_OUTCOME)
        self.assertEqual(request["selected_command_execution_review_failed_check_count"], 0)
        self.assertEqual(request["selected_execution_review_boundary_result_path"], "boundary/result.json")
        self.assertEqual(request["selected_request_consumption_result_path"], "consumption/result.json")
        self.assertEqual(request["selected_v2_admitted_request_artifact_path"], "v2/result.json")
        self.assertEqual(request["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(request["requested_command_invocation_authorization_boundary_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], {"preserved_for_requires_case": True})
        self.assertEqual(request["not_recorded_basis"], {"preserved_for_not_recorded_case": True})
        self.assertEqual(request["declared_non_claims"], _false_non_claims())

        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        result = _resolve(request)
        self.assertRecordedBoundaryOnly(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            request_path = root / "requests" / "authorization_boundary_request.json"
            request_path.parent.mkdir(parents=True)
            request_path.write_text(json.dumps(request, indent=2, sort_keys=True), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path(request_path)
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result.keys()), set(mapping_result.keys()))
            self.assertEqual(
                path_result["declared_command_invocation_authorization_boundary_question"]["command_invocation_authorization_boundary_request_path"],
                str(request_path),
            )

            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path(malformed_path)
            self.assertEqual(malformed_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(malformed_result), "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED")

            array_path = root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path(array_path)
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(array_result), "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED")

            missing_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_from_path(root / "missing.json")
            self.assertEqual(missing_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(missing_result), "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_UNREADABLE")

            output_path = root / "written" / "result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result(path_result, output_path)
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)

            second = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result(path_result, output_path)
            self.assertTrue(second.exists())
            self.assertNotEqual(second, written)
            self.assertTrue(second.name.endswith("_001.json"))

            default_root = root / "default_authorization_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_ROOT",
                default_root,
            ):
                default_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result(path_result)
            self.assertTrue(default_written.exists())
            self.assertTrue(default_written.is_relative_to(default_root))
            self.assertIn("authorization_boundary", str(default_written))
            forbidden_roots = (
                "command_execution_review_boundary",
                "request_consumption",
                "consumption_boundary",
                "admission_boundary",
                "command_execution_boundary",
                "command_implementation_boundary",
                "command_boundary",
                "artifact_emission_containment",
                "evidence_manifest",
                "manifest_checksum_packet",
                "deployment_runtime_public_release",
            )
            self.assertFalse(any(name in str(default_written) for name in forbidden_roots))

    def test_reference_shaped_containment_blocks_full_body_without_returning_raw_value(self) -> None:
        request = _valid_request()
        request["selected_command_execution_review_basis"]["full_artifact_body"] = RAW_FULL_BODY_SENTINEL
        result = _resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(_block_code(result), "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        encoded = _json_text(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, encoded)
        self.assertIn(FULL_BODY_OMISSION_MARKER, encoded)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

        request = _valid_request()
        request["selected_request_consumption_basis"]["full_artifact_body"] = RAW_FULL_BODY_SENTINEL
        original = copy.deepcopy(request)
        result = _resolve(request)
        self.assertEqual(request, original)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(_block_code(result), "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        encoded = _json_text(result)
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, encoded)
        self.assertIn(FULL_BODY_OMISSION_MARKER, encoded)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

    def test_resolver_does_not_mutate_inputs_or_selected_basis(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        first = _resolve(request)
        second = _resolve(request)

        self.assertEqual(request, original)
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        selected_keys = (
            "selected_command_execution_review_basis",
            "selected_command_execution_review_terminal_summary_basis",
            "selected_execution_review_boundary_basis",
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
            "authorization_boundary_only_posture",
            "one_future_authorization_review_posture",
            "reviewed_command_execution_review_basis_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "no_command_invocation_authorization_posture",
            "no_command_invocation_posture",
            "no_command_execution_posture",
            "no_output_result_success_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "returned_result_containment_posture",
            "command_invocation_authorization_boundary_scope",
        )
        for key in selected_keys:
            self.assertEqual(request[key], original[key], key)

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "only_new_authorization_boundary_result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_invocation_authorization_boundary_result(first, output)
            self.assertTrue(written.exists())
            self.assertTrue(str(written).startswith(tmp))

    def test_blocking_request_shape_and_explicit_block(self) -> None:
        request = _valid_request(command_invocation_authorization_boundary_intent=resolver.INTENT_BLOCK)
        self.assertBlocks(request, "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_EXPLICITLY_BLOCKED")

        self.assertBlocks(None, "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_QUESTION_UNDECLARED")
        self.assertBlocks(["not", "a", "mapping"], "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED")
        self.assertBlocks(
            _valid_request(command_invocation_authorization_boundary_intent="UNSUPPORTED_INTENT"),
            "COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_INTENT_UNSUPPORTED",
        )
        self.assertBlocks(
            _valid_request(requested_command_invocation_authorization_boundary_outcome="NOT_A_KNOWN_OUTCOME"),
            "DECLARED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUEST_MALFORMED",
        )

    def test_blocking_required_basis_and_lineage_conditions(self) -> None:
        cases: list[tuple[str, dict[str, object], str]] = [
            ("missing command execution review basis", {"selected_command_execution_review_basis": {}}, "COMMAND_EXECUTION_REVIEW_BASIS_MISSING"),
            (
                "command execution review not recorded",
                {
                    "selected_command_execution_review_basis": _command_execution_review_basis(outcome="NOT_RECORDED"),
                    "selected_command_execution_review_result_outcome": "NOT_RECORDED",
                },
                "COMMAND_EXECUTION_REVIEW_NOT_RECORDED",
            ),
            (
                "command execution review failed checks",
                {
                    "selected_command_execution_review_basis": _command_execution_review_basis(failed_check_count=1),
                    "selected_command_execution_review_failed_check_count": 1,
                },
                "COMMAND_EXECUTION_REVIEW_FAILED_CHECKS_PRESENT",
            ),
            ("missing command execution review terminal summary", {"selected_command_execution_review_terminal_summary_basis": {}}, "COMMAND_EXECUTION_REVIEW_TERMINAL_SUMMARY_MISSING"),
            ("missing execution-review boundary basis", {"selected_execution_review_boundary_basis": {}}, "EXECUTION_REVIEW_BOUNDARY_BASIS_MISSING"),
            (
                "execution-review boundary not recorded",
                {
                    "selected_execution_review_boundary_basis": _execution_review_boundary_basis(outcome="NOT_RECORDED"),
                    "selected_execution_review_boundary_result_outcome": "NOT_RECORDED",
                },
                "EXECUTION_REVIEW_BOUNDARY_NOT_RECORDED",
            ),
            (
                "execution-review boundary failed checks",
                {
                    "selected_execution_review_boundary_basis": _execution_review_boundary_basis(failed_check_count=1),
                    "selected_execution_review_boundary_failed_check_count": 1,
                },
                "EXECUTION_REVIEW_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            ("missing request-consumption basis", {"selected_request_consumption_basis": {}}, "REQUEST_CONSUMPTION_BASIS_MISSING"),
            (
                "request-consumption not consumed",
                {
                    "selected_request_consumption_basis": _request_consumption_basis(outcome="NOT_CONSUMED"),
                    "selected_request_consumption_result_outcome": "NOT_CONSUMED",
                },
                "REQUEST_CONSUMPTION_NOT_CONSUMED",
            ),
            (
                "request-consumption failed checks",
                {
                    "selected_request_consumption_basis": _request_consumption_basis(failed_check_count=1),
                    "selected_request_consumption_failed_check_count": 1,
                },
                "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
            ),
            ("missing consumed request basis", {"selected_consumed_request_basis": {}}, "CONSUMED_REQUEST_BASIS_MISSING"),
            (
                "consumed token not closed",
                {
                    "selected_request_consumption_basis": _reference_shape("request_consumption", outcome=REQUEST_CONSUMPTION_OUTCOME, failed_check_count=0),
                    "selected_consumed_request_basis": {"consumed_request_basis_declared": True},
                    "consumed_token_closed_posture": {"declared": True},
                },
                "CONSUMED_TOKEN_NOT_CLOSED",
            ),
            (
                "consumed request reopened",
                {"declared_non_claims": {**_false_non_claims(), "consumed_request_reopened": True}},
                "CONSUMED_REQUEST_REOPENED",
            ),
            ("missing v2 basis", {"selected_v2_admitted_request_basis": {}}, "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            (
                "v2 not admitted",
                {
                    "selected_v2_admitted_request_basis": _v2_admitted_request_basis(outcome="NOT_ADMITTED"),
                    "selected_v2_admitted_request_outcome": "NOT_ADMITTED",
                },
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            (
                "v2 wrong version",
                {
                    "selected_v2_admitted_request_basis": _v2_admitted_request_basis(result_version="0.1.0"),
                    "selected_v2_admitted_request_version": "0.1.0",
                },
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            (
                "v2 failed checks",
                {
                    "selected_v2_admitted_request_basis": _v2_admitted_request_basis(failed_check_count=1),
                    "selected_v2_failed_check_count": 1,
                },
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "v2 successor metadata missing",
                {
                    "selected_v2_admitted_request_basis": _v2_admitted_request_basis(successor_of="different_predecessor"),
                    "selected_v2_successor_metadata": {},
                },
                "V2_SUCCESSOR_METADATA_MISSING",
            ),
            (
                "v2 returned-result containment missing",
                {
                    "selected_v2_admitted_request_basis": _v2_admitted_request_basis(
                        returned_result_containment_preserved=False,
                        raw_full_prior_artifact_values_omitted=False,
                        full_prior_artifact_body_not_returned=False,
                    ),
                    "returned_result_containment_posture": {"declared": True},
                },
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
            ("missing v1 predecessor failure basis", {"selected_v1_predecessor_failure_basis": {}}, "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            ( "v2 treated as repairing v1", {"v2_treated_as_repairing_v1": True}, "V2_TREATED_AS_REPAIRING_V1"),
            ( "v1 failure hidden", {"v1_hidden": True}, "V1_FAILURE_HIDDEN"),
            ( "v1 claimed passed", {"v1_claimed_passed": True}, "V1_CLAIMED_PASSED"),
            ("missing command execution boundary basis", {"selected_command_execution_boundary_basis": {}}, "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("missing command report basis", {"selected_command_report_basis": {}}, "COMMAND_REPORT_BASIS_MISSING"),
            ("missing command implementation boundary basis", {"selected_command_implementation_boundary_basis": {}}, "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            ("missing command boundary basis", {"selected_command_boundary_basis": {}}, "COMMAND_BOUNDARY_BASIS_MISSING"),
            ("missing artifact emission containment basis", {"selected_artifact_emission_containment_basis": {}}, "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("missing evidence-manifest basis", {"selected_evidence_manifest_basis": {}}, "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("missing portable verification basis", {"selected_portable_verification_basis": {}}, "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("missing authorization-boundary-only posture", {"authorization_boundary_only_posture": {}}, "AUTHORIZATION_BOUNDARY_ONLY_POSTURE_MISSING"),
            ("missing one-future-authorization-review posture", {"one_future_authorization_review_posture": {}}, "ONE_FUTURE_AUTHORIZATION_REVIEW_POSTURE_MISSING"),
            ("missing no-command-invocation-authorization posture", {"no_command_invocation_authorization_posture": {}}, "NO_COMMAND_INVOCATION_AUTHORIZATION_POSTURE_MISSING"),
            ("missing no-standing-lane posture", {"no_standing_lane_posture": {}}, "NO_STANDING_LANE_POSTURE_MISSING"),
            ("missing no-repeat-permission posture", {"no_repeat_permission_posture": {}}, "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
            ("missing no-execution-permission posture", {"no_execution_permission_posture": {}}, "NO_EXECUTION_PERMISSION_POSTURE_MISSING"),
            ("missing no-execution-approval posture", {"no_execution_approval_posture": {}}, "NO_EXECUTION_APPROVAL_POSTURE_MISSING"),
            ("unsupported scope", {"command_invocation_authorization_boundary_scope": ["UNSUPPORTED_SCOPE"]}, "UNSUPPORTED_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_SCOPE"),
        ]
        for label, overrides, expected_code in cases:
            with self.subTest(label=label):
                self.assertBlocks(_valid_request(**overrides), expected_code)

    def test_blocking_collapse_flags(self) -> None:
        cases = {
            "command_invocation_authorization_created": "COMMAND_INVOCATION_AUTHORIZATION_CREATED",
            "command_invocation_permission_created": "COMMAND_INVOCATION_AUTHORIZATION_CREATED",
            "command_invocation_created": "COMMAND_INVOCATION_CREATED",
            "command_executed": "COMMAND_EXECUTION_PERFORMED",
            "command_execution_performed": "COMMAND_EXECUTION_PERFORMED",
            "command_output_created": "COMMAND_OUTPUT_CREATED",
            "command_result_created": "COMMAND_RESULT_CREATED",
            "command_success_created": "COMMAND_SUCCESS_CREATED",
            "execution_permission_created": "EXECUTION_PERMISSION_CREATED",
            "execution_approval_created": "EXECUTION_APPROVAL_CREATED",
            "standing_invocation_lane_created": "STANDING_INVOCATION_LANE_CREATED",
            "repeat_invocation_permission_created": "REPEAT_INVOCATION_PERMISSION_CREATED",
            "authorization_boundary_treated_as_authorization": "AUTHORIZATION_BOUNDARY_TREATED_AS_AUTHORIZATION",
            "authorization_boundary_treated_as_invocation": "AUTHORIZATION_BOUNDARY_TREATED_AS_INVOCATION",
            "reviewed_basis_treated_as_command_invocation_authorization": "REVIEWED_BASIS_TREATED_AS_COMMAND_INVOCATION_AUTHORIZATION",
            "reviewed_basis_treated_as_command_success": "REVIEWED_BASIS_TREATED_AS_COMMAND_SUCCESS",
            "command_output_became_source": "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            "command_result_became_authority": "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            "command_success_created_currentness": "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command_success_claimed_final_completion": "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
            "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
            "deployment_created": "DEPLOYMENT_CREATED",
            "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
            "public_release_created": "PUBLIC_RELEASE_CREATED",
            "operation_permission_created": "OPERATION_PERMISSION_CREATED",
            "public_readiness_created": "PUBLIC_READINESS_CREATED",
            "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
            "continuation_authorized": "CONTINUATION_AUTHORIZED",
            "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
            "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
        }
        for key, expected_code in cases.items():
            with self.subTest(collapse_key=key):
                self.assertBlocks(_valid_request(**{key: True}), expected_code)

    def test_blocking_mutation_replay_merge_and_required_non_claims(self) -> None:
        self.assertBlocks(
            _valid_request(mutation_performed=True, replay_performed=True, merge_performed=True),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )

        missing_non_claims = _false_non_claims()
        missing_non_claims.pop("follow_on_work_authorized")
        self.assertBlocks(
            _valid_request(declared_non_claims=missing_non_claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

        flipped_non_claims = _false_non_claims()
        flipped_non_claims["follow_on_work_authorized"] = True
        self.assertBlocks(
            _valid_request(declared_non_claims=flipped_non_claims),
            "FOLLOW_ON_WORK_AUTHORIZED",
        )

    def test_outcome_family_is_bounded_to_authorization_boundary_only(self) -> None:
        self.assertEqual(
            OUTCOME_FAMILY,
            {
                "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_RECORDED",
                "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_NOT_RECORDED",
                "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_REQUIRES_ADDITIONAL_BASIS",
                "CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY_BLOCKED",
            },
        )
        for outcome in OUTCOME_FAMILY:
            self.assertIn("COMMAND_INVOCATION_AUTHORIZATION_BOUNDARY", outcome)
        request = _valid_request()
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(set(result["command_invocation_authorization_boundary_scope"]["selected_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertTrue(result["command_invocation_authorization_boundary_scope"]["all_selected_scope_values_supported"])

    def test_do_not_record_intent_returns_not_recorded_without_authorization(self) -> None:
        result = _resolve(
            _valid_request(
                command_invocation_authorization_boundary_intent=resolver.INTENT_DO_NOT_RECORD,
                requested_command_invocation_authorization_boundary_outcome=None,
                not_recorded_basis={"operator_declined_recording": True},
            )
        )
        self.assertEqual(result["outcome"], NOT_RECORDED)
        self.assertIs(result["not_recorded_basis"]["not_recorded"], True)
        self.assertNoAuthorizationInvocationExecutionOrFollowOn(result)

    def test_scope_requires_every_supported_value_for_recorded_shape(self) -> None:
        result = _resolve(_valid_request())
        scope = result["command_invocation_authorization_boundary_scope"]
        self.assertEqual(set(scope["selected_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_scope_values_supported"])
        expected_flags = (
            "command_invocation_authorization_boundary_only",
            "command_invocation_authorization_not_created",
            "one_future_authorization_review_only",
            "reviewed_command_execution_review_basis_preserved",
            "reviewed_consumed_request_basis_preserved",
            "consumed_request_token_remains_closed",
            "consumed_request_not_reopened",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "no_standing_invocation_lane_created",
            "no_repeat_invocation_permission_created",
            "authorization_boundary_is_not_authorization",
            "authorization_boundary_is_not_invocation",
            "reviewed_basis_is_not_command_invocation_authorization",
            "reviewed_basis_is_not_command_success",
            "v1_predecessor_failure_remains_visible",
            "v2_successor_does_not_repair_v1",
            "returned_result_containment_preserved",
            "reference_shaped_basis_required",
            "full_prior_artifact_body_not_emitted",
            "no_authority_created",
            "no_currentness_created",
            "no_final_completion",
            "no_continuation_authorized",
            "no_reusable_permission",
            "no_follow_on_work_authorized",
        )
        for key in expected_flags:
            self.assertIs(scope[key], True, key)


if __name__ == "__main__":
    unittest.main()
