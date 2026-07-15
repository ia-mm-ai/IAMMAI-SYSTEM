"""Bounded tests for consumed-request command execution review boundary.

This suite verifies that the resolver records one execution-review boundary only.
It does not invoke a command, execute a command, create command output, create a
command result, create command success, create execution permission, create
execution approval, reopen the consumed request token, create a standing lane,
or authorize repeat invocation, deployment, continuation, reusable permission,
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

import resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary as resolver
from resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary import (
    build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_request,
    build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_summary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_from_path,
    write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
V2_RESOLVER_MODULE = resolver.V2_RESOLVER_MODULE
QUESTION = resolver.CORE_EXECUTION_REVIEW_BOUNDARY_QUESTION
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_EXECUTION_REVIEW_BOUNDARY_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OMISSION_MARKER = resolver.FULL_BODY_OMISSION_MARKER
SENTINEL = "SENTINEL_EXECUTION_REVIEW_FULL_BODY_SHOULD_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = {
    "consumed_single_live_command_invocation_request_command_execution_review_boundary_metadata",
    "declared_execution_review_boundary_question",
    "selected_request_consumption_basis",
    "selected_request_consumption_terminal_summary_basis",
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
    "one_future_execution_review_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "execution_review_separation_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "returned_result_containment_posture",
    "execution_review_boundary_scope",
    "execution_review_boundary_checks",
    "execution_review_boundary_statement",
    "execution_review_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "consumed_single_live_command_invocation_request_command_execution_review_boundary_summary",
}


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _find_forbidden_key_values(value: Any) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, dict):
        for key, item in value.items():
            if key in resolver.FORBIDDEN_FULL_BODY_KEYS:
                found.append(item)
            found.extend(_find_forbidden_key_values(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_find_forbidden_key_values(item))
    return found


def _required_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def _selected_request_consumption_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "basis_declared": True,
        "selected_result_id": "admitted_single_live_command_invocation_request_consumption_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "admitted_single_live_command_invocation_request_consumption/"
            "admitted_single_live_command_invocation_request_consumption_reference_review_001__"
            "admitted_single_live_command_invocation_request_consumption_result.json"
        ),
        "outcome": REQUEST_CONSUMPTION_OUTCOME,
        "failed_check_count": 0,
        "passed_check_count": 47,
        "request_consumed": True,
        "admitted_request_consumed": True,
        "consumption_token_closed": True,
        "consumed_token_closed": True,
        "consumed_request_basis_recorded": True,
        "one_shot_consumption_preserved": True,
        "execution_requires_separate_review": True,
        "v1_predecessor_failure_preserved": True,
        "returned_result_containment_preserved": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "final_completion_not_created": True,
        "continuation_not_authorized": True,
        "reusable_permission_not_created": True,
        "follow_on_work_not_authorized": True,
        "basis_remains_reference_shaped": True,
        "selected_basis_is_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_request_consumption_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "terminal_summary_declared": True,
        "terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_ADMITTED_SINGLE_LIVE_COMMAND_"
            "INVOCATION_REQUEST_CONSUMPTION_TERMINAL_SUMMARY_V0.md"
        ),
        "terminal_summary_remains_readability_basis_only": True,
        "terminal_summary_does_not_authorize_execution": True,
        "terminal_summary_does_not_create_output_result_success": True,
        "terminal_summary_does_not_authorize_follow_on_work": True,
        "basis_remains_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_consumed_request_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "consumed_request_basis_declared": True,
        "consumed_request_basis_recorded": True,
        "consumption_token_closed": True,
        "consumed_token_closed": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "consumed_request_basis_is_not_execution_permission": True,
        "consumed_request_basis_is_not_command_success": True,
        "consumed_request_basis_is_basis_only": True,
        "selected_basis_is_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "basis_declared": True,
        "selected_result_id": "single_live_command_invocation_request_admission_boundary_v2_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "single_live_command_invocation_request_admission_boundary_v2/"
            "single_live_command_invocation_request_admission_boundary_v2_reference_review_001__result.json"
        ),
        "outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "result_version": V2_ADMITTED_REQUEST_VERSION,
        "failed_check_count": 0,
        "passed_check_count": 48,
        "successor_of": V1_PREDECESSOR_RESOLVER_MODULE,
        "successor_reason": "v2 selected returned-result containment while preserving v1 failed-lineage visibility",
        "resolver_module": V2_RESOLVER_MODULE,
        "successor_metadata_preserved": True,
        "returned_result_containment_preserved": True,
        "selected_basis_is_reference_shaped": True,
        "v2_remains_lineage_evidence": True,
        "v2_does_not_claim_v1_passed": True,
        "v2_successor_does_not_erase_v1": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "v1_predecessor_failure_basis_declared": True,
        "selected_result_id": "single_live_command_invocation_request_admission_boundary_v1_failed_lineage",
        "selected_result_path": "tests/test_resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary.py",
        "selected_outcome": "PRESERVED_FAILED_LINEAGE_EVIDENCE",
        "v1_remains_visible_predecessor_failure_evidence": True,
        "v1_predecessor_failure_remains_visible": True,
        "v1_is_not_repaired": True,
        "v1_is_not_hidden": True,
        "v1_is_not_claimed_passed": True,
        "v1_repaired": False,
        "v1_hidden": False,
        "v1_claimed_passed": False,
        "v2_successor_does_not_erase_v1": True,
        "predecessor_failure_evidence_is_lineage_evidence_only": True,
        "basis_remains_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_reference_basis(label: str, outcome: str, **extra: Any) -> dict[str, Any]:
    slug = label.lower().replace(" ", "_").replace("-", "_")
    basis = {
        "basis_declared": True,
        "selected_result_id": f"{slug}_reference_basis_001",
        "selected_result_path": f"artifacts/synthetic_reference_shape/{slug}_result.json",
        "outcome": outcome,
        "failed_check_count": 0,
        "basis_label": label,
        "basis_remains_reference_shaped": True,
        "basis_is_not_command_invocation": True,
        "basis_is_not_command_execution": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_execution_permission_or_approval": True,
        "basis_is_not_authority_currentness_final_completion_continuation_follow_on_work": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _selected_command_execution_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis("command execution boundary", "COMMAND_EXECUTION_BOUNDARY_RECORDED", **extra)


def _selected_command_report_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis("command report", "COMMAND_REPORT_RECORDED", **extra)


def _selected_command_implementation_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis(
        "command implementation boundary",
        "COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED",
        **extra,
    )


def _selected_command_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis("command boundary", "COMMAND_BOUNDARY_RECORDED", **extra)


def _selected_artifact_emission_containment_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis(
        "artifact emission containment",
        "ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_RECORDED",
        **extra,
    )


def _selected_evidence_manifest_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis("evidence manifest", "EVIDENCE_MANIFEST_BOUNDARY_RECORDED", **extra)


def _selected_portable_verification_basis(**extra: Any) -> dict[str, Any]:
    return _selected_reference_basis("portable verification", "PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_RECORDED", **extra)


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "declared": True,
        "posture_label": label,
        "one_future_execution_review_posture_declared": True,
        "consumed_token_closed_posture_declared": True,
        "consumed_request_not_reopened": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "execution_review_is_not_execution": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "returned_result_containment_preserved": True,
        "no_invocation_execution_output_result_success_created": True,
        "no_raw_full_prior_artifact_body_returned": True,
    }
    posture.update(extra)
    return posture


def _valid_request(**extra: Any) -> dict[str, Any]:
    request = {
        "execution_review_boundary_request_id": "consumed_request_execution_review_boundary_reference_review_001",
        "execution_review_boundary_question": QUESTION,
        "execution_review_boundary_intent": resolver.INTENT_RECORD,
        "selected_request_consumption_basis": _selected_request_consumption_basis(),
        "selected_request_consumption_terminal_summary_basis": _selected_request_consumption_terminal_summary_basis(),
        "selected_consumed_request_basis": _selected_consumed_request_basis(),
        "selected_v2_admitted_request_basis": _selected_v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _selected_v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_basis": _selected_command_execution_boundary_basis(),
        "selected_command_report_basis": _selected_command_report_basis(),
        "selected_command_implementation_boundary_basis": _selected_command_implementation_boundary_basis(),
        "selected_command_boundary_basis": _selected_command_boundary_basis(),
        "selected_artifact_emission_containment_basis": _selected_artifact_emission_containment_basis(),
        "selected_evidence_manifest_basis": _selected_evidence_manifest_basis(),
        "selected_portable_verification_basis": _selected_portable_verification_basis(),
        "one_future_execution_review_posture": _posture("one future execution review only"),
        "consumed_token_closed_posture": _posture("consumed token closed"),
        "no_reopen_consumed_request_posture": _posture("consumed request not reopened"),
        "no_standing_lane_posture": _posture("no standing invocation lane"),
        "no_repeat_permission_posture": _posture("no repeat invocation permission"),
        "execution_review_separation_posture": _posture("execution review is not execution"),
        "no_execution_permission_posture": _posture("no execution permission"),
        "no_execution_approval_posture": _posture("no execution approval"),
        "returned_result_containment_posture": _posture("returned-result containment preserved"),
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_basis_required": True,
            "full_prior_artifact_body_not_emitted": True,
        },
        "execution_review_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_execution_review_boundary_outcome": RECORDED,
        "declared_non_claims": _required_false_non_claims(),
        "selected_request_consumption_result_path": "artifacts/synthetic_reference_shape/request_consumption_result.json",
        "selected_request_consumption_result_id": "request_consumption_result_001",
        "selected_request_consumption_result_outcome": REQUEST_CONSUMPTION_OUTCOME,
        "selected_request_consumption_failed_check_count": 0,
        "selected_request_consumption_terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_ADMITTED_SINGLE_LIVE_COMMAND_"
            "INVOCATION_REQUEST_CONSUMPTION_TERMINAL_SUMMARY_V0.md"
        ),
        "selected_v2_admitted_request_artifact_path": "artifacts/synthetic_reference_shape/v2_admitted_request_result.json",
        "selected_v2_admitted_request_artifact_id": "v2_admitted_request_result_001",
        "selected_v2_admitted_request_outcome": V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
    }
    request.update(extra)
    return request


def _resolve(request: Any = None) -> dict[str, Any]:
    if request is None:
        return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary()
    return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary(
        declared_execution_review_boundary_request=request
    )


def _block_code(result: dict[str, Any]) -> str | None:
    block = result.get("block") or {}
    return block.get("block_code")


class ConsumedSingleLiveCommandInvocationRequestExecutionReviewBoundaryTests(unittest.TestCase):
    def assertTopLevelShape(self, result: dict[str, Any]) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertNoSentinelReturned(self, result: dict[str, Any]) -> None:
        self.assertNotIn(SENTINEL, _json_text(result))

    def assertForbiddenFullBodyValuesSanitized(self, result: dict[str, Any]) -> None:
        values = _find_forbidden_key_values(result)
        self.assertTrue(values)
        for value in values:
            self.assertNotEqual(value, SENTINEL)
            if isinstance(value, str):
                self.assertEqual(value, OMISSION_MARKER)

    def assertRequiredFalseNonClaimsRemainFalse(self, result: dict[str, Any]) -> None:
        non_claims = result["non_claims"]
        statement = result["execution_review_boundary_statement"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertFalse(non_claims[key], key)
            self.assertIn(key, statement)
            self.assertFalse(statement[key], key)

    def assertNoCommandOrFollowOnCreated(self, result: dict[str, Any]) -> None:
        statement = result["execution_review_boundary_statement"]
        false_fields = {
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
            "consumed_request_reopened",
            "execution_review_treated_as_execution",
            "consumed_request_basis_treated_as_execution_permission",
            "consumed_request_basis_treated_as_command_success",
            "command_output_became_source",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "v1_repaired",
            "v1_hidden",
            "v1_claimed_passed",
            "prior_artifacts_mutated",
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
        }
        for key in false_fields:
            self.assertFalse(statement.get(key), key)

    def assertBlocked(self, request: Any, expected_code: str) -> dict[str, Any]:
        result = _resolve(request)
        self.assertTopLevelShape(result)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(_block_code(result), expected_code)
        self.assertNoCommandOrFollowOnCreated(result)
        return result

    def test_successful_execution_review_boundary_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertTopLevelShape(result)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["consumed_single_live_command_invocation_request_command_execution_review_boundary_summary"]["failed_check_count"], 0)

        statement = result["execution_review_boundary_statement"]
        for key in (
            "consumed_request_execution_review_boundary_recorded",
            "consumed_request_basis_preserved",
            "consumed_request_token_remains_closed",
            "single_execution_review_conditions_declared",
            "execution_review_requires_separate_result",
            "execution_still_not_authorized",
            "execution_requires_separate_invocation_step",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "command_execution_review_boundary_only",
            "consumed_request_not_reopened",
            "one_future_execution_review_only",
        ):
            self.assertTrue(statement[key], key)

        self.assertRequiredFalseNonClaimsRemainFalse(result)
        self.assertNoCommandOrFollowOnCreated(result)
        self.assertNoSentinelReturned(result)

    def test_metadata_and_lineage_sections_are_preserved(self) -> None:
        result = _resolve(_valid_request())

        metadata = result["consumed_single_live_command_invocation_request_command_execution_review_boundary_metadata"]
        for key in (
            "consumed_single_live_command_invocation_request_command_execution_review_boundary_result_id",
            "consumed_single_live_command_invocation_request_command_execution_review_boundary_result_type",
            "consumed_single_live_command_invocation_request_command_execution_review_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["consumed_single_live_command_invocation_request_command_execution_review_boundary_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        request_consumption = result["selected_request_consumption_basis"]["selected_basis"]
        self.assertEqual(request_consumption["outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(request_consumption["failed_check_count"], 0)
        self.assertTrue(request_consumption["request_consumed"])
        self.assertTrue(request_consumption["consumption_token_closed"])
        self.assertTrue(request_consumption["consumed_request_basis_recorded"])
        self.assertTrue(request_consumption["command_invocation_not_created"])
        self.assertTrue(request_consumption["command_execution_not_performed"])
        self.assertTrue(request_consumption["execution_permission_not_created"])
        self.assertTrue(request_consumption["execution_approval_not_created"])
        self.assertTrue(request_consumption["no_standing_invocation_lane"])
        self.assertTrue(request_consumption["no_repeat_invocation_permission"])

        consumed = result["selected_consumed_request_basis"]["selected_basis"]
        self.assertTrue(consumed["consumed_request_token_remains_closed"])
        self.assertTrue(consumed["consumed_request_not_reopened"])
        self.assertTrue(consumed["consumed_request_basis_is_not_execution_permission"])
        self.assertTrue(consumed["consumed_request_basis_is_not_command_success"])

        v2 = result["selected_v2_admitted_request_basis"]["selected_basis"]
        self.assertEqual(v2["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(v2["result_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(v2["failed_check_count"], 0)
        self.assertEqual(v2["successor_of"], V1_PREDECESSOR_RESOLVER_MODULE)
        self.assertTrue(v2["successor_reason"])
        self.assertEqual(v2["resolver_module"], V2_RESOLVER_MODULE)
        self.assertTrue(v2["returned_result_containment_preserved"])
        self.assertTrue(v2["selected_basis_is_reference_shaped"])

        v1 = result["selected_v1_predecessor_failure_basis"]["selected_basis"]
        self.assertTrue(v1["v1_remains_visible_predecessor_failure_evidence"])
        self.assertTrue(v1["v1_is_not_repaired"])
        self.assertTrue(v1["v1_is_not_hidden"])
        self.assertTrue(v1["v1_is_not_claimed_passed"])
        self.assertTrue(v1["v2_successor_does_not_erase_v1"])
        self.assertTrue(v1["predecessor_failure_evidence_is_lineage_evidence_only"])

    def test_execution_review_boundary_checks_and_non_meaning_are_explicit(self) -> None:
        result = _resolve(_valid_request())
        checks = result["execution_review_boundary_checks"]["records"]
        self.assertGreaterEqual(len(checks), 50)

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])

        check_names = {check["check_name"] for check in checks}
        expected_checks = {
            "execution-review boundary question declared",
            "execution-review boundary intent supported",
            "request-consumption terminal summary basis declared",
            "request-consumption live artifact basis declared",
            "request-consumption live artifact consumed outcome",
            "request-consumption live artifact failed check count zero",
            "consumed request basis declared",
            "consumed request basis records consumed token closed",
            "consumed request token remains closed",
            "consumed request is not reopened",
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
            "one-future-execution-review posture declared",
            "consumed-token-closed posture declared",
            "no-reopen-consumed-request posture declared",
            "no-standing-lane posture declared",
            "no-repeat-permission posture declared",
            "execution-review separation posture declared",
            "no-execution-permission posture declared",
            "no-execution-approval posture declared",
            "returned-result containment posture declared",
            "execution-review-boundary scope supported",
            "reference-shaped input posture declared or preserved",
            "no-command-invocation posture declared",
            "no-command-execution posture declared",
            "no-output/result/success posture declared",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "execution permission not created",
            "execution approval not created",
            "standing invocation lane not created",
            "repeat invocation permission not created",
            "execution review not execution",
            "consumed request basis not execution permission",
            "consumed request basis not command success",
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
        self.assertTrue(expected_checks.issubset(check_names))

        non_meaning = result["execution_review_boundary_non_meaning"]
        for key in (
            "execution_review_boundary_does_not_mean_command_invocation_created",
            "execution_review_boundary_does_not_mean_command_executed",
            "execution_review_boundary_does_not_mean_command_output_exists",
            "execution_review_boundary_does_not_mean_command_result_exists",
            "execution_review_boundary_does_not_mean_command_success_exists",
            "execution_review_boundary_does_not_mean_execution_permission_exists",
            "execution_review_boundary_does_not_mean_execution_approval_exists",
            "execution_review_boundary_does_not_mean_command_success_creates_currentness",
            "execution_review_boundary_does_not_mean_command_success_claims_final_completion",
            "execution_review_boundary_does_not_mean_command_output_becomes_source",
            "execution_review_boundary_does_not_mean_command_result_becomes_authority",
            "execution_review_boundary_does_not_mean_standing_invocation_lane_exists",
            "execution_review_boundary_does_not_mean_repeat_invocation_permission_exists",
            "execution_review_boundary_does_not_mean_consumed_request_token_reopened",
            "execution_review_boundary_does_not_mean_v1_was_repaired",
            "execution_review_boundary_does_not_mean_v1_was_hidden",
            "execution_review_boundary_does_not_mean_v1_passed",
            "execution_review_boundary_does_not_mean_deployment_created",
            "execution_review_boundary_does_not_mean_runtime_hosting_created",
            "execution_review_boundary_does_not_mean_public_release_created",
            "execution_review_boundary_does_not_mean_public_readiness_created",
            "execution_review_boundary_does_not_mean_final_completion_claimed",
            "execution_review_boundary_does_not_mean_continuation_authorized",
            "execution_review_boundary_does_not_mean_reusable_permission_created",
            "execution_review_boundary_does_not_mean_derivative_reception_authorized",
            "execution_review_boundary_does_not_mean_vessel_relation_authorized",
            "execution_review_boundary_does_not_mean_another_reception_request_authorized",
            "execution_review_boundary_does_not_mean_follow_on_work_authorized",
        ):
            self.assertTrue(non_meaning[key], key)

    def test_additional_basis_and_not_recorded_outcomes_are_bounded(self) -> None:
        additional_context = {
            "missing_basis": ["consumed request basis unclear", "no-execution-permission posture unclear"],
            "non_claims_incomplete_but_not_flipped": True,
        }
        additional_request = _valid_request(
            requested_execution_review_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=additional_context,
        )
        additional = _resolve(additional_request)
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(additional["additional_basis_required"]["additional_basis_context"], additional_context)
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assertNoCommandOrFollowOnCreated(additional)

        not_recorded_reason = {
            "reason": "execution-review-boundary basis cannot be bounded",
            "failed_basis": ["returned-result containment cannot be preserved"],
        }
        not_recorded_request = _valid_request(
            requested_execution_review_boundary_outcome=NOT_RECORDED,
            not_recorded_basis=not_recorded_reason,
        )
        not_recorded = _resolve(not_recorded_request)
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(not_recorded["not_recorded_basis"]["not_recorded_basis"], not_recorded_reason)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_mutate"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair_prior_artifacts"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize_follow_on_work"])
        self.assertNoCommandOrFollowOnCreated(not_recorded)

    def test_what_remains_open_and_summary_helper(self) -> None:
        request = _valid_request()
        result = _resolve(request)

        remains_open = result["what_remains_open"]
        expected_open = {
            "consumed-request command execution review boundary test",
            "consumed-request command execution review boundary live artifact",
            "actual command execution review",
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
        }
        self.assertTrue(expected_open.issubset(set(remains_open["open_items"])))
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

        summary = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_summary(result)
        self.assertEqual(summary, result["consumed_single_live_command_invocation_request_command_execution_review_boundary_summary"])
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["execution_review_boundary_request_id"], request["execution_review_boundary_request_id"])
        self.assertEqual(summary["execution_review_boundary_question"], QUESTION)
        self.assertEqual(summary["execution_review_boundary_intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["execution_review_boundary_recorded"])
        self.assertTrue(summary["consumed_request_basis_preserved"])
        self.assertTrue(summary["consumed_request_token_remains_closed"])
        self.assertTrue(summary["single_execution_review_conditions_declared"])
        self.assertTrue(summary["execution_review_requires_separate_result"])
        self.assertTrue(summary["execution_still_not_authorized"])
        self.assertTrue(summary["execution_requires_separate_invocation_step"])
        self.assertTrue(summary["v1_predecessor_failure_preserved"])
        self.assertTrue(summary["returned_result_containment_preserved"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_request_consumption_failed_check_count"], 0)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["selected_v2_failed_check_count"], 0)
        self.assertTrue(summary["command_invocation_not_created"])
        self.assertTrue(summary["command_execution_not_performed"])
        self.assertTrue(summary["command_output_not_created"])
        self.assertTrue(summary["command_result_not_created"])
        self.assertTrue(summary["command_success_not_created"])
        self.assertTrue(summary["execution_permission_not_created"])
        self.assertTrue(summary["execution_approval_not_created"])
        self.assertTrue(summary["no_standing_lane"])
        self.assertTrue(summary["no_repeat_permission"])
        self.assertTrue(summary["consumed_request_not_reopened"])
        self.assertTrue(summary["execution_review_not_execution"])
        self.assertTrue(summary["consumed_request_basis_not_execution_permission"])
        self.assertTrue(summary["consumed_request_basis_not_command_success"])
        self.assertTrue(summary["v1_not_repaired"])
        self.assertTrue(summary["v1_not_hidden"])
        self.assertTrue(summary["v1_not_claimed_passed"])
        self.assertTrue(summary["no_raw_full_prior_artifact_body_returned"])
        self.assertTrue(summary["no_artifact_mutation"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_permission_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_flow_reusable_permission"])
        self.assertTrue(summary["no_derivative_reception_vessel_relation_another_reception_request_follow_on_work"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, summary["key_non_claims"])
            self.assertFalse(summary["key_non_claims"][key], key)

    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        additional_context = {"missing_basis": []}
        not_recorded_basis = {"reason": "unused in recorded helper-built request"}
        request = build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_request(
            "helper_built_execution_review_boundary_001",
            QUESTION,
            _selected_request_consumption_basis(),
            _selected_request_consumption_terminal_summary_basis(),
            _selected_consumed_request_basis(),
            _selected_v2_admitted_request_basis(),
            _selected_v1_predecessor_failure_basis(),
            _selected_command_execution_boundary_basis(),
            _selected_command_report_basis(),
            _selected_command_implementation_boundary_basis(),
            _selected_command_boundary_basis(),
            _selected_artifact_emission_containment_basis(),
            _selected_evidence_manifest_basis(),
            _selected_portable_verification_basis(),
            _posture("one future execution review only"),
            _posture("consumed token closed"),
            _posture("consumed request not reopened"),
            _posture("no standing invocation lane"),
            _posture("no repeat invocation permission"),
            _posture("execution review is not execution"),
            _posture("no execution permission"),
            _posture("no execution approval"),
            _posture("returned-result containment preserved"),
            list(SUPPORTED_SCOPE),
            selected_request_consumption_result_path="artifacts/synthetic_reference_shape/request_consumption_result.json",
            selected_request_consumption_result_id="request_consumption_result_001",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="artifacts/synthetic_reference_shape/v2_admitted_request_result.json",
            selected_v2_admitted_request_artifact_id="v2_admitted_request_result_001",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            requested_execution_review_boundary_outcome=RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )

        self.assertEqual(request["execution_review_boundary_request_id"], "helper_built_execution_review_boundary_001")
        self.assertEqual(request["execution_review_boundary_question"], QUESTION)
        self.assertEqual(request["selected_request_consumption_basis"]["outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertTrue(request["selected_request_consumption_terminal_summary_basis"]["terminal_summary_declared"])
        self.assertTrue(request["selected_consumed_request_basis"]["consumed_request_not_reopened"])
        self.assertEqual(request["selected_v2_admitted_request_basis"]["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertTrue(request["selected_v1_predecessor_failure_basis"]["v1_remains_visible_predecessor_failure_evidence"])
        self.assertTrue(request["selected_command_execution_boundary_basis"]["basis_declared"])
        self.assertTrue(request["selected_command_report_basis"]["basis_declared"])
        self.assertTrue(request["selected_command_implementation_boundary_basis"]["basis_declared"])
        self.assertTrue(request["selected_command_boundary_basis"]["basis_declared"])
        self.assertTrue(request["selected_artifact_emission_containment_basis"]["basis_declared"])
        self.assertTrue(request["selected_evidence_manifest_basis"]["basis_declared"])
        self.assertTrue(request["selected_portable_verification_basis"]["basis_declared"])
        self.assertTrue(request["one_future_execution_review_posture"]["declared"])
        self.assertTrue(request["consumed_token_closed_posture"]["declared"])
        self.assertTrue(request["no_reopen_consumed_request_posture"]["declared"])
        self.assertTrue(request["no_standing_lane_posture"]["declared"])
        self.assertTrue(request["no_repeat_permission_posture"]["declared"])
        self.assertTrue(request["execution_review_separation_posture"]["declared"])
        self.assertTrue(request["no_execution_permission_posture"]["declared"])
        self.assertTrue(request["no_execution_approval_posture"]["declared"])
        self.assertTrue(request["returned_result_containment_posture"]["declared"])
        self.assertEqual(set(request["execution_review_boundary_scope"]), set(SUPPORTED_SCOPE))
        self.assertEqual(request["selected_request_consumption_result_id"], "request_consumption_result_001")
        self.assertEqual(request["selected_request_consumption_result_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(request["selected_request_consumption_failed_check_count"], 0)
        self.assertEqual(request["selected_v2_admitted_request_artifact_id"], "v2_admitted_request_result_001")
        self.assertEqual(request["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(request["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(request["selected_v2_failed_check_count"], 0)
        self.assertEqual(request["requested_execution_review_boundary_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for key in REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][key], key)

        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertNoCommandOrFollowOnCreated(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "declared_request.json"
            request_path.write_text(json.dumps(request, sort_keys=True), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result.keys()), set(mapping_result.keys()))
            self.assertEqual(
                path_result["declared_execution_review_boundary_question"]["execution_review_boundary_request_path"],
                str(request_path),
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], BLOCKED)
            self.assertEqual(_block_code(malformed), "DECLARED_EXECUTION_REVIEW_BOUNDARY_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(array_result), "DECLARED_EXECUTION_REVIEW_BOUNDARY_REQUEST_MALFORMED")

            missing_path = tmp_path / "missing.json"
            missing = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_from_path(
                missing_path
            )
            self.assertEqual(missing["outcome"], BLOCKED)
            self.assertEqual(_block_code(missing), "DECLARED_EXECUTION_REVIEW_BOUNDARY_REQUEST_UNREADABLE")

            explicit_output = tmp_path / "nested" / "execution_review_boundary_result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_result(
                mapping_result,
                explicit_output,
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed.keys()))

            second_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_result(
                mapping_result,
                explicit_output,
            )
            self.assertTrue(second_written.exists())
            self.assertNotEqual(second_written, written)
            self.assertTrue(second_written.name.endswith("_001.json"))

            root_text = str(resolver.OUTPUT_ROOT)
            self.assertIn("consumed_single_live_command_invocation_request_command_execution_review_boundary", root_text)
            for excluded in (
                "admitted_single_live_command_invocation_request_consumption/",
                "consumption_boundary",
                "admission_boundary",
                "command_implementation_boundary",
                "artifact_emission_containment_boundary",
                "deployment",
                "runtime",
                "public_release",
            ):
                self.assertNotIn(excluded, root_text)

            patched_root = tmp_path / "bounded_default_root"
            with patch.object(resolver, "OUTPUT_ROOT", patched_root):
                default_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_result(
                    mapping_result
                )
            self.assertTrue(default_written.exists())
            self.assertTrue(default_written.is_relative_to(patched_root))

    def test_reference_shaped_containment_blocks_and_sanitizes_raw_full_body(self) -> None:
        request_consumption_request = _valid_request()
        request_consumption_request["selected_request_consumption_basis"]["full_artifact_body"] = SENTINEL
        request_consumption_result = _resolve(request_consumption_request)
        self.assertEqual(request_consumption_result["outcome"], BLOCKED)
        self.assertEqual(_block_code(request_consumption_result), "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNoSentinelReturned(request_consumption_result)
        self.assertForbiddenFullBodyValuesSanitized(request_consumption_result)
        self.assertNoCommandOrFollowOnCreated(request_consumption_result)

        v2_request = _valid_request()
        v2_request["selected_v2_admitted_request_basis"]["full_artifact_body"] = SENTINEL
        v2_result = _resolve(v2_request)
        self.assertEqual(v2_result["outcome"], BLOCKED)
        self.assertEqual(_block_code(v2_result), "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNoSentinelReturned(v2_result)
        self.assertForbiddenFullBodyValuesSanitized(v2_result)
        self.assertNoCommandOrFollowOnCreated(v2_result)

    def test_resolver_does_not_mutate_declared_inputs(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(request, original)
        self.assertEqual(request["selected_request_consumption_basis"], original["selected_request_consumption_basis"])
        self.assertEqual(
            request["selected_request_consumption_terminal_summary_basis"],
            original["selected_request_consumption_terminal_summary_basis"],
        )
        self.assertEqual(request["selected_consumed_request_basis"], original["selected_consumed_request_basis"])
        self.assertEqual(request["selected_v2_admitted_request_basis"], original["selected_v2_admitted_request_basis"])
        self.assertEqual(request["selected_v1_predecessor_failure_basis"], original["selected_v1_predecessor_failure_basis"])
        self.assertEqual(request["selected_command_execution_boundary_basis"], original["selected_command_execution_boundary_basis"])
        self.assertEqual(request["selected_command_report_basis"], original["selected_command_report_basis"])
        self.assertEqual(
            request["selected_command_implementation_boundary_basis"],
            original["selected_command_implementation_boundary_basis"],
        )
        self.assertEqual(request["selected_command_boundary_basis"], original["selected_command_boundary_basis"])
        self.assertEqual(request["selected_artifact_emission_containment_basis"], original["selected_artifact_emission_containment_basis"])
        self.assertEqual(request["selected_evidence_manifest_basis"], original["selected_evidence_manifest_basis"])
        self.assertEqual(request["selected_portable_verification_basis"], original["selected_portable_verification_basis"])
        for posture_key in (
            "one_future_execution_review_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "execution_review_separation_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "returned_result_containment_posture",
        ):
            self.assertEqual(request[posture_key], original[posture_key])
        self.assertEqual(request["execution_review_boundary_scope"], original["execution_review_boundary_scope"])
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "execution_review_boundary_result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_boundary_result(
                first,
                output_path,
            )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())

    def test_blocking_basis_scope_and_lineage_conditions(self) -> None:
        missing = _resolve(None)
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(_block_code(missing), "EXECUTION_REVIEW_BOUNDARY_QUESTION_UNDECLARED")

        malformed = _resolve(["not", "a", "mapping"])
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(_block_code(malformed), "DECLARED_EXECUTION_REVIEW_BOUNDARY_REQUEST_MALFORMED")

        cases: list[tuple[str, str, Any]] = [
            (
                "explicit block intent",
                "EXECUTION_REVIEW_BOUNDARY_EXPLICITLY_BLOCKED",
                lambda request: request.update({"execution_review_boundary_intent": resolver.INTENT_BLOCK}),
            ),
            (
                "missing request-consumption terminal",
                "REQUEST_CONSUMPTION_TERMINAL_SUMMARY_MISSING",
                lambda request: request.pop("selected_request_consumption_terminal_summary_basis"),
            ),
            (
                "missing request-consumption basis",
                "REQUEST_CONSUMPTION_BASIS_MISSING",
                lambda request: request.pop("selected_request_consumption_basis"),
            ),
            (
                "request-consumption outcome not consumed",
                "REQUEST_CONSUMPTION_NOT_CONSUMED",
                self._set_request_consumption_outcome_not_consumed,
            ),
            (
                "request-consumption failed checks",
                "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT",
                self._set_request_consumption_failed_checks,
            ),
            (
                "missing consumed request basis",
                "CONSUMED_REQUEST_BASIS_MISSING",
                lambda request: request.pop("selected_consumed_request_basis"),
            ),
            (
                "consumed token not closed",
                "CONSUMED_TOKEN_NOT_CLOSED",
                self._remove_consumed_token_closed_posture,
            ),
            (
                "consumed request reopened",
                "CONSUMED_REQUEST_REOPENED",
                lambda request: request.update({"consumed_request_reopened": True}),
            ),
            (
                "missing v2 basis",
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
                lambda request: request.pop("selected_v2_admitted_request_basis"),
            ),
            (
                "v2 outcome not admitted",
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
                self._set_v2_outcome_not_admitted,
            ),
            (
                "v2 version wrong",
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
                self._set_v2_version_wrong,
            ),
            (
                "v2 failed checks",
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
                self._set_v2_failed_checks,
            ),
            (
                "missing v2 successor metadata",
                "V2_SUCCESSOR_METADATA_MISSING",
                self._remove_v2_successor_metadata,
            ),
            (
                "missing v2 returned containment",
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
                self._remove_v2_returned_result_containment,
            ),
            (
                "missing v1 predecessor",
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
                lambda request: request.pop("selected_v1_predecessor_failure_basis"),
            ),
            (
                "v2 repairing v1",
                "V2_TREATED_AS_REPAIRING_V1",
                lambda request: request.update({"v2_treated_as_repairing_v1": True}),
            ),
            (
                "v1 hidden",
                "V1_FAILURE_HIDDEN",
                lambda request: request.update({"v1_hidden": True}),
            ),
            (
                "v1 claimed passed",
                "V1_CLAIMED_PASSED",
                lambda request: request.update({"v1_claimed_passed": True}),
            ),
            (
                "missing command execution boundary",
                "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
                lambda request: request.pop("selected_command_execution_boundary_basis"),
            ),
            (
                "missing command report",
                "COMMAND_REPORT_BASIS_MISSING",
                lambda request: request.pop("selected_command_report_basis"),
            ),
            (
                "missing command implementation boundary",
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
                lambda request: request.pop("selected_command_implementation_boundary_basis"),
            ),
            (
                "missing command boundary",
                "COMMAND_BOUNDARY_BASIS_MISSING",
                lambda request: request.pop("selected_command_boundary_basis"),
            ),
            (
                "missing artifact containment",
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
                lambda request: request.pop("selected_artifact_emission_containment_basis"),
            ),
            (
                "missing evidence manifest",
                "EVIDENCE_MANIFEST_BASIS_MISSING",
                lambda request: request.pop("selected_evidence_manifest_basis"),
            ),
            (
                "missing portable verification",
                "PORTABLE_VERIFICATION_BASIS_MISSING",
                lambda request: request.pop("selected_portable_verification_basis"),
            ),
            (
                "missing one future posture",
                "ONE_FUTURE_EXECUTION_REVIEW_POSTURE_MISSING",
                lambda request: request.pop("one_future_execution_review_posture"),
            ),
            (
                "missing no-standing posture",
                "NO_STANDING_LANE_POSTURE_MISSING",
                lambda request: request.pop("no_standing_lane_posture"),
            ),
            (
                "missing no-repeat posture",
                "NO_REPEAT_PERMISSION_POSTURE_MISSING",
                lambda request: request.pop("no_repeat_permission_posture"),
            ),
            (
                "missing no-execution-permission posture",
                "NO_EXECUTION_PERMISSION_POSTURE_MISSING",
                lambda request: request.pop("no_execution_permission_posture"),
            ),
            (
                "missing no-execution-approval posture",
                "NO_EXECUTION_APPROVAL_POSTURE_MISSING",
                lambda request: request.pop("no_execution_approval_posture"),
            ),
            (
                "unsupported scope",
                "UNSUPPORTED_EXECUTION_REVIEW_BOUNDARY_SCOPE",
                lambda request: request.update({"execution_review_boundary_scope": list(SUPPORTED_SCOPE) + ["UNSUPPORTED_SCOPE"]}),
            ),
        ]
        for name, code, mutate in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self.assertBlocked(request, code)

    def _remove_consumed_token_closed_posture(self, request: dict[str, Any]) -> None:
        request.pop("consumed_token_closed_posture")
        for basis_key in ("selected_request_consumption_basis", "selected_consumed_request_basis"):
            basis = request[basis_key]
            for key in (
                "consumption_token_closed",
                "consumed_token_closed",
                "consumed_request_token_remains_closed",
                "consumed_request_basis_records_consumed_token_closed",
            ):
                basis.pop(key, None)

    def _set_request_consumption_outcome_not_consumed(self, request: dict[str, Any]) -> None:
        request["selected_request_consumption_basis"]["outcome"] = "NOT_CONSUMED"
        request["selected_request_consumption_result_outcome"] = "NOT_CONSUMED"

    def _set_request_consumption_failed_checks(self, request: dict[str, Any]) -> None:
        request["selected_request_consumption_basis"]["failed_check_count"] = 1
        request["selected_request_consumption_failed_check_count"] = 1

    def _set_v2_outcome_not_admitted(self, request: dict[str, Any]) -> None:
        request["selected_v2_admitted_request_basis"]["outcome"] = "NOT_ADMITTED"
        request["selected_v2_admitted_request_outcome"] = "NOT_ADMITTED"

    def _set_v2_version_wrong(self, request: dict[str, Any]) -> None:
        request["selected_v2_admitted_request_basis"]["result_version"] = "0.1.0"
        request["selected_v2_admitted_request_version"] = "0.1.0"

    def _set_v2_failed_checks(self, request: dict[str, Any]) -> None:
        request["selected_v2_admitted_request_basis"]["failed_check_count"] = 1
        request["selected_v2_failed_check_count"] = 1

    def _remove_v2_successor_metadata(self, request: dict[str, Any]) -> None:
        v2 = request["selected_v2_admitted_request_basis"]
        v2.pop("successor_of", None)
        v2.pop("successor_reason", None)
        v2.pop("successor_metadata_preserved", None)
        v2.pop("resolver_module", None)

    def _remove_v2_returned_result_containment(self, request: dict[str, Any]) -> None:
        request.pop("returned_result_containment_posture")
        v2 = request["selected_v2_admitted_request_basis"]
        v2.pop("returned_result_containment_preserved", None)
        v2.pop("returned_result_containment_posture_preserved", None)

    def test_blocking_collapse_flags(self) -> None:
        cases = {
            "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
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
            "execution_review_treated_as_execution": "EXECUTION_REVIEW_TREATED_AS_EXECUTION",
            "consumed_request_basis_treated_as_execution_permission": "CONSUMED_REQUEST_BASIS_TREATED_AS_EXECUTION_PERMISSION",
            "consumed_request_basis_treated_as_command_success": "CONSUMED_REQUEST_BASIS_TREATED_AS_COMMAND_SUCCESS",
            "command_output_became_source": "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            "command_result_became_authority": "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            "command_success_created_currentness": "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command_success_claimed_final_completion": "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            "prior_artifacts_mutated": "ARTIFACTS_MUTATED",
            "deployment_created": "DEPLOYMENT_CREATED",
            "runtime_hosting_created": "RUNTIME_HOSTING_CREATED",
            "public_release_created": "PUBLIC_RELEASE_CREATED",
            "operation_permission_created": "OPERATION_PERMISSION_CREATED",
            "public_launch_readiness_created": "PUBLIC_READINESS_CREATED",
            "final_completion_claimed": "FINAL_COMPLETION_CLAIMED",
            "continuation_authorized": "CONTINUATION_AUTHORIZED",
            "reusable_permission_created": "REUSABLE_PERMISSION_CREATED",
            "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
            "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
            "another_reception_request_authorized": "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
        }
        for flag, code in cases.items():
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self.assertBlocked(request, code)

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self.assertBlocked(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_invocation_created")
        self.assertBlocked(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["command_invocation_created"] = True
        flipped = _resolve(flipped_non_claim)
        self.assertEqual(flipped["outcome"], BLOCKED)
        self.assertIn(_block_code(flipped), {"NON_CLAIM_MISSING_OR_FLIPPED", "COMMAND_INVOCATION_CREATED"})

    def test_resolver_source_has_no_command_or_network_execution_surface(self) -> None:
        source = (SRC_ROOT / f"{resolver.RESOLVER_MODULE}.py").read_text(encoding="utf-8")
        forbidden_tokens = (
            "subprocess",
            "os.system",
            "Popen",
            "check_call",
            "check_output",
            "requests",
            "urllib",
            "http.client",
            "socket",
            "openai",
        )
        for token in forbidden_tokens:
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
