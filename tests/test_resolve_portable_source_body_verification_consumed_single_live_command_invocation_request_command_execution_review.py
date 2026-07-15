"""Bounded tests for consumed-request command execution review.

This suite verifies that command execution review records review posture only.
It does not invoke a command, execute a command, create command output, create a
command result, create command success, create execution permission, create
execution approval, create command invocation authorization, reopen the consumed
request token, create a standing lane, create repeat permission, or authorize
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

import resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review as resolver
from resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review import (
    build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_request,
    build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_summary,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review,
    resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path,
    write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

EXECUTION_REVIEW_BOUNDARY_OUTCOME = resolver.EXECUTION_REVIEW_BOUNDARY_OUTCOME
REQUEST_CONSUMPTION_OUTCOME = resolver.REQUEST_CONSUMPTION_OUTCOME
V2_ADMITTED_REQUEST_OUTCOME = resolver.V2_ADMITTED_REQUEST_OUTCOME
V2_ADMITTED_REQUEST_VERSION = resolver.V2_ADMITTED_REQUEST_VERSION
V1_PREDECESSOR_RESOLVER_MODULE = resolver.V1_PREDECESSOR_RESOLVER_MODULE
V2_RESOLVER_MODULE = resolver.V2_RESOLVER_MODULE
QUESTION = resolver.CORE_COMMAND_EXECUTION_REVIEW_QUESTION
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OMISSION_MARKER = resolver.FULL_BODY_OMISSION_MARKER
SENTINEL = "SENTINEL_COMMAND_EXECUTION_REVIEW_FULL_BODY_SHOULD_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = {
    "consumed_single_live_command_invocation_request_command_execution_review_metadata",
    "declared_command_execution_review_question",
    "selected_execution_review_boundary_basis",
    "selected_execution_review_boundary_terminal_summary_basis",
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
    "reviewed_basis_posture",
    "consumed_token_closed_posture",
    "no_reopen_consumed_request_posture",
    "review_only_posture",
    "no_command_invocation_posture",
    "no_command_execution_posture",
    "no_output_result_success_posture",
    "no_execution_permission_posture",
    "no_execution_approval_posture",
    "no_command_invocation_authorization_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "returned_result_containment_posture",
    "command_execution_review_scope",
    "command_execution_review_checks",
    "command_execution_review_statement",
    "command_execution_review_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "consumed_single_live_command_invocation_request_command_execution_review_summary",
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


def _execution_review_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "basis_declared": True,
        "selected_result_id": "consumed_request_command_execution_review_boundary_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "consumed_single_live_command_invocation_request_command_execution_review_boundary/"
            "consumed_single_live_command_invocation_request_command_execution_review_boundary_"
            "reference_review_001__result.json"
        ),
        "outcome": EXECUTION_REVIEW_BOUNDARY_OUTCOME,
        "failed_check_count": 0,
        "passed_check_count": 64,
        "execution_review_boundary_basis_remains_boundary_basis_only": True,
        "boundary_did_not_perform_actual_command_execution_review": True,
        "boundary_did_not_authorize_invocation_execution_output_result_success": True,
        "boundary_did_not_create_execution_permission": True,
        "boundary_did_not_create_execution_approval": True,
        "boundary_did_not_create_command_invocation_authorization": True,
        "boundary_did_not_create_standing_lane": True,
        "boundary_did_not_create_repeat_permission": True,
        "boundary_did_not_create_final_completion": True,
        "boundary_did_not_authorize_continuation": True,
        "boundary_did_not_create_reusable_permission": True,
        "boundary_did_not_authorize_follow_on_work": True,
        "basis_remains_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _execution_review_boundary_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "terminal_summary_declared": True,
        "terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_"
            "INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        "terminal_summary_remains_readability_basis_only": True,
        "terminal_summary_does_not_perform_command_execution_review": True,
        "terminal_summary_does_not_authorize_execution": True,
        "terminal_summary_does_not_create_output_result_success": True,
        "terminal_summary_does_not_authorize_follow_on_work": True,
        "basis_remains_reference_shaped": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
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
        "request_consumed_exactly_once": True,
        "request_consumed": True,
        "admitted_single_live_command_invocation_request_consumed": True,
        "consumption_token_closed": True,
        "consumed_token_closed": True,
        "consumed_request_basis_recorded": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "command_invocation_authorization_not_created": True,
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


def _request_consumption_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
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


def _consumed_request_basis(**extra: Any) -> dict[str, Any]:
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


def _v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
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


def _v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "v1_predecessor_failure_basis_declared": True,
        "selected_result_id": "single_live_command_invocation_request_admission_boundary_v1_failed_lineage",
        "selected_result_path": (
            "tests/test_resolve_portable_source_body_verification_admitted_single_live_"
            "command_invocation_request_consumption_boundary.py"
        ),
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


def _reference_basis(label: str, outcome: str, **extra: Any) -> dict[str, Any]:
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
        "basis_is_not_command_invocation_authorization": True,
        "basis_is_not_authority_currentness_final_completion_continuation_follow_on_work": True,
        "full_prior_artifacts_embedded": False,
        "raw_full_prior_artifact_body_returned": False,
    }
    basis.update(extra)
    return basis


def _command_execution_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("command execution boundary", "COMMAND_EXECUTION_BOUNDARY_RECORDED", **extra)


def _command_report_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("command report", "COMMAND_REPORT_RECORDED", **extra)


def _command_implementation_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("command implementation boundary", "COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED", **extra)


def _command_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("command boundary", "COMMAND_BOUNDARY_RECORDED", **extra)


def _artifact_emission_containment_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("artifact emission containment", "ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_RECORDED", **extra)


def _evidence_manifest_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("evidence manifest", "EVIDENCE_MANIFEST_BOUNDARY_RECORDED", **extra)


def _portable_verification_basis(**extra: Any) -> dict[str, Any]:
    return _reference_basis("portable verification", "PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_RECORDED", **extra)


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "declared": True,
        "posture_label": label,
        "reviewed_basis_posture_declared": True,
        "review_only_posture_declared": True,
        "consumed_token_closed_posture_declared": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "output_result_success_not_created": True,
        "execution_permission_not_created": True,
        "execution_approval_not_created": True,
        "command_invocation_authorization_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "returned_result_containment_preserved": True,
        "no_raw_full_prior_artifact_body_returned": True,
    }
    posture.update(extra)
    return posture


def _valid_request(**extra: Any) -> dict[str, Any]:
    request = {
        "command_execution_review_request_id": "consumed_request_command_execution_review_reference_review_001",
        "command_execution_review_question": QUESTION,
        "command_execution_review_intent": resolver.INTENT_RECORD,
        "selected_execution_review_boundary_basis": _execution_review_boundary_basis(),
        "selected_execution_review_boundary_terminal_summary_basis": _execution_review_boundary_terminal_summary_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_request_consumption_terminal_summary_basis": _request_consumption_terminal_summary_basis(),
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
        "reviewed_basis_posture": _posture("reviewed basis only"),
        "consumed_token_closed_posture": _posture("consumed token closed"),
        "no_reopen_consumed_request_posture": _posture("consumed request not reopened"),
        "review_only_posture": _posture("command execution review is review only"),
        "no_command_invocation_posture": _posture("no command invocation"),
        "no_command_execution_posture": _posture("no command execution"),
        "no_output_result_success_posture": _posture("no output result success"),
        "no_execution_permission_posture": _posture("no execution permission"),
        "no_execution_approval_posture": _posture("no execution approval"),
        "no_command_invocation_authorization_posture": _posture("no command invocation authorization"),
        "no_standing_lane_posture": _posture("no standing invocation lane"),
        "no_repeat_permission_posture": _posture("no repeat invocation permission"),
        "returned_result_containment_posture": _posture("returned-result containment preserved"),
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_basis_required": True,
            "full_prior_artifact_body_not_emitted": True,
        },
        "command_execution_review_scope": list(SUPPORTED_SCOPE),
        "requested_command_execution_review_outcome": RECORDED,
        "declared_non_claims": _required_false_non_claims(),
        "selected_execution_review_boundary_result_path": "artifacts/synthetic_reference_shape/execution_review_boundary_result.json",
        "selected_execution_review_boundary_result_id": "execution_review_boundary_result_001",
        "selected_execution_review_boundary_result_outcome": EXECUTION_REVIEW_BOUNDARY_OUTCOME,
        "selected_execution_review_boundary_failed_check_count": 0,
        "selected_execution_review_boundary_terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_"
            "INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
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
        return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review()
    return resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review(
        declared_command_execution_review_request=request
    )


def _block_code(result: dict[str, Any]) -> str | None:
    return (result.get("block") or {}).get("block_code")


class ConsumedSingleLiveCommandInvocationRequestCommandExecutionReviewTests(unittest.TestCase):
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
        statement = result["command_execution_review_statement"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertFalse(non_claims[key], key)
            self.assertIn(key, statement)
            self.assertFalse(statement[key], key)

    def assertNoCommandOrFollowOnCreated(self, result: dict[str, Any]) -> None:
        statement = result["command_execution_review_statement"]
        false_fields = {
            "consumed_request_reopened",
            "command_invocation_created",
            "command_executed",
            "command_execution_performed",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "execution_permission_created",
            "execution_approval_created",
            "command_invocation_authorization_created",
            "standing_invocation_lane_created",
            "repeat_invocation_permission_created",
            "command_execution_review_treated_as_execution",
            "reviewed_basis_treated_as_execution_permission",
            "reviewed_basis_treated_as_command_success",
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

    def test_successful_command_execution_review_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(request, original)
        self.assertTopLevelShape(result)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["command_execution_review_checks"]["failed_check_count"], 0)

        statement = result["command_execution_review_statement"]
        for key in (
            "command_execution_review_recorded",
            "reviewed_consumed_request_basis_preserved",
            "reviewed_execution_review_boundary_basis_preserved",
            "consumed_request_token_remains_closed",
            "reviewed_basis_posture_declared",
            "execution_review_only",
            "execution_still_not_authorized",
            "execution_requires_separate_invocation_step",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "command_execution_review_only",
        ):
            self.assertTrue(statement[key], key)

        self.assertRequiredFalseNonClaimsRemainFalse(result)
        self.assertNoCommandOrFollowOnCreated(result)
        self.assertNoSentinelReturned(result)

    def test_metadata_and_lineage_sections_are_preserved(self) -> None:
        result = _resolve(_valid_request())

        metadata = result["consumed_single_live_command_invocation_request_command_execution_review_metadata"]
        for key in (
            "consumed_single_live_command_invocation_request_command_execution_review_result_id",
            "consumed_single_live_command_invocation_request_command_execution_review_result_type",
            "consumed_single_live_command_invocation_request_command_execution_review_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["consumed_single_live_command_invocation_request_command_execution_review_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        boundary = result["selected_execution_review_boundary_basis"]
        self.assertEqual(boundary["selected_execution_review_boundary_result_outcome"], EXECUTION_REVIEW_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["selected_execution_review_boundary_failed_check_count"], 0)
        self.assertTrue(boundary["execution_review_boundary_basis_remains_boundary_basis_only"])
        self.assertTrue(boundary["execution_review_boundary_did_not_perform_command_execution_review"])
        self.assertTrue(boundary["execution_review_boundary_did_not_authorize_invocation_execution_output_result_success"])
        self.assertTrue(boundary["execution_review_boundary_did_not_create_execution_permission_or_approval"])
        self.assertTrue(boundary["execution_review_boundary_did_not_create_command_invocation_authorization"])

        request_consumption = result["selected_request_consumption_basis"]["selected_basis"]
        self.assertEqual(request_consumption["outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(request_consumption["failed_check_count"], 0)
        self.assertTrue(request_consumption["request_consumed_exactly_once"])
        self.assertTrue(request_consumption["consumption_token_closed"])
        self.assertTrue(request_consumption["consumed_request_basis_recorded"])
        self.assertTrue(request_consumption["command_invocation_not_created"])
        self.assertTrue(request_consumption["command_execution_not_performed"])
        self.assertTrue(request_consumption["execution_permission_not_created"])
        self.assertTrue(request_consumption["execution_approval_not_created"])
        self.assertTrue(request_consumption["command_invocation_authorization_not_created"])
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

    def test_command_execution_review_checks_and_non_meaning_are_explicit(self) -> None:
        result = _resolve(_valid_request())
        checks = result["command_execution_review_checks"]["records"]
        self.assertGreaterEqual(len(checks), 55)

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
            "command execution review question declared",
            "command execution review intent supported",
            "execution-review boundary terminal summary basis declared",
            "execution-review boundary live artifact basis declared",
            "execution-review boundary live artifact recorded outcome",
            "execution-review boundary live artifact failed check count zero",
            "request-consumption live artifact basis declared",
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
            "reviewed-basis posture declared",
            "review-only posture declared",
            "no-command-invocation posture declared",
            "no-command-execution posture declared",
            "no-output/result/success posture declared",
            "no-execution-permission posture declared",
            "no-execution-approval posture declared",
            "no-command-invocation-authorization posture declared",
            "no-standing-lane posture declared",
            "no-repeat-permission posture declared",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "execution permission not created",
            "execution approval not created",
            "command invocation authorization not created",
            "standing invocation lane not created",
            "repeat invocation permission not created",
            "command execution review not execution",
            "reviewed basis not execution permission",
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
        self.assertTrue(expected_checks.issubset(check_names))

        non_meaning = result["command_execution_review_non_meaning"]
        for key in (
            "command_execution_review_does_not_mean_command_invocation_created",
            "command_execution_review_does_not_mean_command_executed",
            "command_execution_review_does_not_mean_command_output_exists",
            "command_execution_review_does_not_mean_command_result_exists",
            "command_execution_review_does_not_mean_command_success_exists",
            "command_execution_review_does_not_mean_execution_permission_exists",
            "command_execution_review_does_not_mean_execution_approval_exists",
            "command_execution_review_does_not_mean_command_invocation_authorization_exists",
            "command_execution_review_does_not_mean_command_success_creates_currentness",
            "command_execution_review_does_not_mean_command_success_claims_final_completion",
            "command_execution_review_does_not_mean_command_output_becomes_source",
            "command_execution_review_does_not_mean_command_result_becomes_authority",
            "command_execution_review_does_not_mean_standing_invocation_lane_exists",
            "command_execution_review_does_not_mean_repeat_invocation_permission_exists",
            "command_execution_review_does_not_mean_consumed_request_token_reopened",
            "command_execution_review_does_not_mean_v1_was_repaired",
            "command_execution_review_does_not_mean_v1_was_hidden",
            "command_execution_review_does_not_mean_v1_passed",
            "command_execution_review_does_not_mean_deployment_created",
            "command_execution_review_does_not_mean_runtime_hosting_created",
            "command_execution_review_does_not_mean_public_release_created",
            "command_execution_review_does_not_mean_public_readiness_created",
            "command_execution_review_does_not_mean_final_completion_claimed",
            "command_execution_review_does_not_mean_continuation_authorized",
            "command_execution_review_does_not_mean_reusable_permission_created",
            "command_execution_review_does_not_mean_derivative_reception_authorized",
            "command_execution_review_does_not_mean_vessel_relation_authorized",
            "command_execution_review_does_not_mean_another_reception_request_authorized",
            "command_execution_review_does_not_mean_follow_on_work_authorized",
        ):
            self.assertTrue(non_meaning[key], key)

    def test_additional_basis_and_not_recorded_outcomes_do_not_authorize_anything(self) -> None:
        additional_context = {
            "missing_basis": "execution-review boundary basis unclear",
            "missing_basis_not_scheduled": True,
        }
        additional_result = _resolve(
            _valid_request(
                requested_command_execution_review_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional_result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(additional_result["additional_basis_required"]["additional_basis_context"], additional_context)
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_executed"])
        self.assertNoCommandOrFollowOnCreated(additional_result)

        not_recorded_basis = {
            "reason": "command execution review basis cannot be bounded",
            "not_recorded_does_not_authorize_repair_or_next_work": True,
        }
        not_recorded_result = _resolve(
            _valid_request(
                requested_command_execution_review_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded_result["outcome"], NOT_RECORDED)
        self.assertEqual(not_recorded_result["not_recorded_basis"]["not_recorded_basis"], not_recorded_basis)
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_mutate"])
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_repair_prior_artifacts"])
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_authorize_follow_on_work"])
        self.assertNoCommandOrFollowOnCreated(not_recorded_result)

    def test_what_remains_open_and_summary_helper(self) -> None:
        result = _resolve(_valid_request())
        open_section = result["what_remains_open"]
        for item in (
            "command execution review test",
            "command execution review live artifact",
            "command invocation authorization boundary, if separately specified",
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
        ):
            self.assertIn(item, open_section["open_items"])
        self.assertTrue(open_section["open_means_not_scheduled"])
        self.assertTrue(open_section["open_means_not_authorized"])
        self.assertTrue(open_section["open_means_not_executed"])

        summary = build_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_summary(result)
        self.assertEqual(summary, result["consumed_single_live_command_invocation_request_command_execution_review_summary"])
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["command_execution_review_request_id"], "consumed_request_command_execution_review_reference_review_001")
        self.assertEqual(summary["command_execution_review_question"], QUESTION)
        self.assertEqual(summary["command_execution_review_intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "command_execution_review_recorded",
            "reviewed_consumed_request_basis_preserved",
            "reviewed_execution_review_boundary_basis_preserved",
            "consumed_request_token_remains_closed",
            "reviewed_basis_posture_declared",
            "execution_review_only",
            "execution_still_not_authorized",
            "execution_requires_separate_invocation_step",
            "v1_predecessor_failure_preserved",
            "returned_result_containment_preserved",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "execution_permission_not_created",
            "execution_approval_not_created",
            "command_invocation_authorization_not_created",
            "no_standing_lane",
            "no_repeat_permission",
            "consumed_request_not_reopened",
            "command_execution_review_not_execution",
            "reviewed_basis_not_execution_permission",
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
            self.assertTrue(summary[key], key)
        self.assertEqual(summary["selected_execution_review_boundary_outcome"], EXECUTION_REVIEW_BOUNDARY_OUTCOME)
        self.assertEqual(summary["selected_execution_review_boundary_failed_check_count"], 0)
        self.assertEqual(summary["selected_request_consumption_outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(summary["selected_request_consumption_failed_check_count"], 0)
        self.assertEqual(summary["selected_v2_admitted_request_outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(summary["selected_v2_admitted_request_version"], V2_ADMITTED_REQUEST_VERSION)
        self.assertEqual(summary["selected_v2_failed_check_count"], 0)
        self.assertEqual(summary["key_non_claims"], _required_false_non_claims())

    def test_request_builder_helper_preserves_inputs_and_resolves(self) -> None:
        additional_context = {"missing_basis": "not scheduled"}
        not_recorded_basis = {"reason": "not selected"}
        request = build_declared_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_request(
            "builder_request_001",
            QUESTION,
            _execution_review_boundary_basis(),
            _execution_review_boundary_terminal_summary_basis(),
            _request_consumption_basis(),
            _request_consumption_terminal_summary_basis(),
            _consumed_request_basis(),
            _v2_admitted_request_basis(),
            _v1_predecessor_failure_basis(),
            _command_execution_boundary_basis(),
            _command_report_basis(),
            _command_implementation_boundary_basis(),
            _command_boundary_basis(),
            _artifact_emission_containment_basis(),
            _evidence_manifest_basis(),
            _portable_verification_basis(),
            _posture("reviewed basis"),
            _posture("closed"),
            _posture("not reopened"),
            _posture("review only"),
            _posture("no invocation"),
            _posture("no execution"),
            _posture("no output result success"),
            _posture("no permission"),
            _posture("no approval"),
            _posture("no invocation authorization"),
            _posture("no standing lane"),
            _posture("no repeat permission"),
            _posture("containment"),
            list(SUPPORTED_SCOPE),
            selected_execution_review_boundary_result_path="boundary/path.json",
            selected_execution_review_boundary_result_id="boundary_001",
            selected_execution_review_boundary_result_outcome=EXECUTION_REVIEW_BOUNDARY_OUTCOME,
            selected_execution_review_boundary_failed_check_count=0,
            selected_request_consumption_result_path="consumption/path.json",
            selected_request_consumption_result_id="consumption_001",
            selected_request_consumption_result_outcome=REQUEST_CONSUMPTION_OUTCOME,
            selected_request_consumption_failed_check_count=0,
            selected_v2_admitted_request_artifact_path="v2/path.json",
            selected_v2_admitted_request_artifact_id="v2_001",
            selected_v2_admitted_request_outcome=V2_ADMITTED_REQUEST_OUTCOME,
            selected_v2_admitted_request_version=V2_ADMITTED_REQUEST_VERSION,
            selected_v2_failed_check_count=0,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )

        self.assertEqual(request["command_execution_review_request_id"], "builder_request_001")
        self.assertEqual(request["command_execution_review_question"], QUESTION)
        self.assertEqual(request["selected_execution_review_boundary_basis"]["outcome"], EXECUTION_REVIEW_BOUNDARY_OUTCOME)
        self.assertEqual(request["selected_request_consumption_basis"]["outcome"], REQUEST_CONSUMPTION_OUTCOME)
        self.assertEqual(request["selected_v2_admitted_request_basis"]["outcome"], V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(request["selected_execution_review_boundary_result_path"], "boundary/path.json")
        self.assertEqual(request["selected_request_consumption_result_id"], "consumption_001")
        self.assertEqual(request["selected_v2_admitted_request_artifact_id"], "v2_001")
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        self.assertEqual(request["declared_non_claims"], _required_false_non_claims())
        for key in REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][key], key)

        request.pop("additional_basis_context")
        request.pop("not_recorded_basis")
        result = _resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(result["command_execution_review_checks"]["failed_check_count"], 0)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "declared_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path(request_path)
            mapping_result = _resolve(request)
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result.keys()), set(mapping_result.keys()))
            self.assertEqual(path_result["command_execution_review_checks"]["failed_check_count"], 0)
            self.assertEqual(path_result["declared_command_execution_review_question"]["command_execution_review_request_path"], str(request_path))

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path(malformed_path)
            self.assertEqual(malformed_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(malformed_result), "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path(array_path)
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(array_result), "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED")

            missing_result = resolve_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_from_path(tmp_path / "missing.json")
            self.assertEqual(missing_result["outcome"], BLOCKED)
            self.assertEqual(_block_code(missing_result), "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_UNREADABLE")

            output_path = tmp_path / "nested" / "review_result.json"
            written_path = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result(path_result, output_path)
            self.assertTrue(written_path.exists())
            written = json.loads(written_path.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(written.keys()))

            second_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result(path_result, output_path)
            self.assertNotEqual(written_path, second_written)
            self.assertTrue(second_written.name.endswith("_001.json"))

            patched_root = tmp_path / "bounded_command_execution_review_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_CONSUMED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_COMMAND_EXECUTION_REVIEW_ROOT",
                patched_root,
            ):
                default_written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result(path_result)
            self.assertTrue(default_written.exists())
            self.assertTrue(str(default_written).startswith(str(patched_root)))
            forbidden_root_names = (
                "command_execution_review_boundary",
                "admitted_single_live_command_invocation_request_consumption",
                "consumption_boundary",
                "admission_boundary",
                "command_execution_boundary",
                "command_implementation_boundary",
                "command_boundary",
                "artifact_emission_containment",
                "evidence_manifest",
                "manifest",
                "checksum",
                "packet",
                "deployment",
                "runtime",
                "public_release",
            )
            self.assertFalse(any(name in patched_root.name for name in forbidden_root_names))

    def test_reference_shaped_containment_blocks_full_body_without_returning_raw_value(self) -> None:
        boundary_request = _valid_request(
            selected_execution_review_boundary_basis=_execution_review_boundary_basis(
                full_artifact_body=SENTINEL
            )
        )
        boundary_result = self.assertBlocked(boundary_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNoSentinelReturned(boundary_result)
        self.assertForbiddenFullBodyValuesSanitized(boundary_result)

        consumption_request = _valid_request(
            selected_request_consumption_basis=_request_consumption_basis(
                raw_full_artifact_body=SENTINEL
            )
        )
        consumption_result = self.assertBlocked(consumption_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNoSentinelReturned(consumption_result)
        self.assertForbiddenFullBodyValuesSanitized(consumption_result)
        self.assertNoCommandOrFollowOnCreated(consumption_result)

    def test_resolver_does_not_mutate_inputs(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)
        self.assertEqual(request, original)
        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)

        for key in (
            "selected_execution_review_boundary_basis",
            "selected_execution_review_boundary_terminal_summary_basis",
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
            "reviewed_basis_posture",
            "consumed_token_closed_posture",
            "no_reopen_consumed_request_posture",
            "review_only_posture",
            "no_command_invocation_posture",
            "no_command_execution_posture",
            "no_output_result_success_posture",
            "no_execution_permission_posture",
            "no_execution_approval_posture",
            "no_command_invocation_authorization_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "returned_result_containment_posture",
            "command_execution_review_scope",
        ):
            self.assertEqual(request[key], original[key], key)

        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "additive" / "result.json"
            written = write_portable_source_body_verification_consumed_single_live_command_invocation_request_command_execution_review_result(first, target)
            self.assertTrue(written.exists())
            self.assertTrue(str(written).startswith(str(Path(tmp))))

    def test_blocking_required_basis_and_lineage_conditions(self) -> None:
        def missing(key: str) -> dict[str, Any]:
            request = _valid_request()
            request.pop(key)
            return request

        token_unclear = _valid_request(
            selected_request_consumption_basis={"outcome": REQUEST_CONSUMPTION_OUTCOME, "failed_check_count": 0},
            selected_consumed_request_basis={"consumed_request_basis_declared": True},
            consumed_token_closed_posture={"declared": True},
        )

        cases: list[tuple[str, dict[str, Any], str]] = [
            ("missing boundary basis", missing("selected_execution_review_boundary_basis"), "EXECUTION_REVIEW_BOUNDARY_BASIS_MISSING"),
            ("boundary not recorded", _valid_request(selected_execution_review_boundary_result_outcome="NOT_RECORDED"), "EXECUTION_REVIEW_BOUNDARY_NOT_RECORDED"),
            ("boundary failed checks", _valid_request(selected_execution_review_boundary_failed_check_count=1), "EXECUTION_REVIEW_BOUNDARY_FAILED_CHECKS_PRESENT"),
            ("missing boundary summary", missing("selected_execution_review_boundary_terminal_summary_basis"), "EXECUTION_REVIEW_BOUNDARY_TERMINAL_SUMMARY_MISSING"),
            ("missing consumption basis", missing("selected_request_consumption_basis"), "REQUEST_CONSUMPTION_BASIS_MISSING"),
            ("consumption not consumed", _valid_request(selected_request_consumption_result_outcome="NOT_CONSUMED"), "REQUEST_CONSUMPTION_NOT_CONSUMED"),
            ("consumption failed checks", _valid_request(selected_request_consumption_failed_check_count=2), "REQUEST_CONSUMPTION_FAILED_CHECKS_PRESENT"),
            ("missing consumption summary", missing("selected_request_consumption_terminal_summary_basis"), "REQUEST_CONSUMPTION_TERMINAL_SUMMARY_MISSING"),
            ("missing consumed basis", missing("selected_consumed_request_basis"), "CONSUMED_REQUEST_BASIS_MISSING"),
            ("consumed token not closed", token_unclear, "CONSUMED_TOKEN_NOT_CLOSED"),
            ("consumed request reopened", _valid_request(consumed_request_reopened=True), "CONSUMED_REQUEST_REOPENED"),
            ("missing v2", missing("selected_v2_admitted_request_basis"), "V2_ADMITTED_REQUEST_BASIS_MISSING"),
            ("v2 not admitted", _valid_request(selected_v2_admitted_request_outcome="NOT_ADMITTED"), "V2_ADMITTED_REQUEST_NOT_ADMITTED"),
            ("v2 wrong version", _valid_request(selected_v2_admitted_request_version="0.1.0"), "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0"),
            ("v2 failed checks", _valid_request(selected_v2_failed_check_count=1), "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT"),
            ("v2 successor metadata missing", _valid_request(selected_v2_admitted_request_basis=_v2_admitted_request_basis(successor_of="wrong")), "V2_SUCCESSOR_METADATA_MISSING"),
            ("v2 returned containment missing", _valid_request(selected_v2_admitted_request_basis=_v2_admitted_request_basis(returned_result_containment_preserved=False)), "V2_RETURNED_RESULT_CONTAINMENT_MISSING"),
            ("missing v1", missing("selected_v1_predecessor_failure_basis"), "V1_PREDECESSOR_FAILURE_BASIS_MISSING"),
            ("v2 repairs v1", _valid_request(v2_treated_as_repairing_v1=True), "V2_TREATED_AS_REPAIRING_V1"),
            ("v1 hidden", _valid_request(v1_hidden=True), "V1_FAILURE_HIDDEN"),
            ("v1 claimed passed", _valid_request(v1_claimed_passed=True), "V1_CLAIMED_PASSED"),
            ("missing command execution boundary", missing("selected_command_execution_boundary_basis"), "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("missing command report", missing("selected_command_report_basis"), "COMMAND_REPORT_BASIS_MISSING"),
            ("missing implementation boundary", missing("selected_command_implementation_boundary_basis"), "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING"),
            ("missing command boundary", missing("selected_command_boundary_basis"), "COMMAND_BOUNDARY_BASIS_MISSING"),
            ("missing containment", missing("selected_artifact_emission_containment_basis"), "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("missing evidence", missing("selected_evidence_manifest_basis"), "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("missing portable verification", missing("selected_portable_verification_basis"), "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("missing reviewed posture", missing("reviewed_basis_posture"), "REVIEWED_BASIS_POSTURE_MISSING"),
            ("missing review only posture", missing("review_only_posture"), "REVIEW_ONLY_POSTURE_MISSING"),
            ("missing standing lane posture", missing("no_standing_lane_posture"), "NO_STANDING_LANE_POSTURE_MISSING"),
            ("missing repeat posture", missing("no_repeat_permission_posture"), "NO_REPEAT_PERMISSION_POSTURE_MISSING"),
            ("missing execution permission posture", missing("no_execution_permission_posture"), "NO_EXECUTION_PERMISSION_POSTURE_MISSING"),
            ("missing execution approval posture", missing("no_execution_approval_posture"), "NO_EXECUTION_APPROVAL_POSTURE_MISSING"),
            ("missing invocation authorization posture", missing("no_command_invocation_authorization_posture"), "NO_COMMAND_INVOCATION_AUTHORIZATION_POSTURE_MISSING"),
            ("unsupported scope", _valid_request(command_execution_review_scope=["UNSUPPORTED_SCOPE"]), "UNSUPPORTED_COMMAND_EXECUTION_REVIEW_SCOPE"),
        ]
        for label, request, expected_code in cases:
            with self.subTest(label=label):
                self.assertBlocked(request, expected_code)

    def test_blocking_request_shape_and_explicit_block(self) -> None:
        self.assertBlocked(
            _valid_request(command_execution_review_intent=resolver.INTENT_BLOCK),
            "COMMAND_EXECUTION_REVIEW_EXPLICITLY_BLOCKED",
        )
        self.assertBlocked(None, "COMMAND_EXECUTION_REVIEW_QUESTION_UNDECLARED")
        self.assertBlocked(["not", "a", "mapping"], "DECLARED_COMMAND_EXECUTION_REVIEW_REQUEST_MALFORMED")

        malformed_intent = _valid_request(command_execution_review_intent="UNSUPPORTED_INTENT")
        self.assertBlocked(malformed_intent, "COMMAND_EXECUTION_REVIEW_INTENT_UNSUPPORTED")

    def test_blocking_collapse_flags(self) -> None:
        collapse_cases = {
            "command_invocation_created": "COMMAND_INVOCATION_CREATED",
            "command_executed": "COMMAND_EXECUTION_PERFORMED",
            "command_execution_performed": "COMMAND_EXECUTION_PERFORMED",
            "command_output_created": "COMMAND_OUTPUT_CREATED",
            "command_result_created": "COMMAND_RESULT_CREATED",
            "command_success_created": "COMMAND_SUCCESS_CREATED",
            "execution_permission_created": "EXECUTION_PERMISSION_CREATED",
            "execution_approval_created": "EXECUTION_APPROVAL_CREATED",
            "command_invocation_authorization_created": "COMMAND_INVOCATION_AUTHORIZATION_CREATED",
            "standing_invocation_lane_created": "STANDING_INVOCATION_LANE_CREATED",
            "repeat_invocation_permission_created": "REPEAT_INVOCATION_PERMISSION_CREATED",
            "command_execution_review_treated_as_execution": "COMMAND_EXECUTION_REVIEW_TREATED_AS_EXECUTION",
            "reviewed_basis_treated_as_execution_permission": "REVIEWED_BASIS_TREATED_AS_EXECUTION_PERMISSION",
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
        for field, expected_code in collapse_cases.items():
            with self.subTest(field=field):
                self.assertBlocked(_valid_request(**{field: True}), expected_code)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        mutation_request = _valid_request(mutation_performed=True, replay_performed=True, merge_performed=True)
        self.assertBlocked(mutation_request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = _valid_request()
        missing_non_claim["declared_non_claims"].pop("command_became_authority")
        self.assertBlocked(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = _valid_request()
        flipped_non_claim["declared_non_claims"]["command_became_authority"] = True
        self.assertBlocked(flipped_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_outcome_family_is_limited_to_declared_command_execution_review_outcomes(self) -> None:
        for requested in (RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS):
            with self.subTest(requested=requested):
                result = _resolve(_valid_request(requested_command_execution_review_outcome=requested))
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assertEqual(result["outcome"], requested)

        blocked = _resolve(_valid_request(requested_command_execution_review_outcome=BLOCKED))
        self.assertEqual(blocked["outcome"], BLOCKED)
        self.assertIn(blocked["outcome"], OUTCOME_FAMILY)


if __name__ == "__main__":
    unittest.main()
