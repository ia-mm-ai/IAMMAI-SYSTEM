"""Tests for portable source-body verification command output boundary.

This suite is bounded to command output boundary only. It is downstream of
recorded command output containment and proves that one future command output
boundary can be recorded without creating command output, capturing output,
creating an output/report artifact, creating command result, creating command
success, mutating artifacts, deploying, publishing, continuing, or authorizing
follow-on work.
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

import resolve_portable_source_body_verification_command_output_boundary as resolver
from resolve_portable_source_body_verification_command_output_boundary import (
    build_declared_portable_source_body_verification_command_output_boundary_request,
    build_portable_source_body_verification_command_output_boundary_summary,
    resolve_portable_source_body_verification_command_output_boundary,
    resolve_portable_source_body_verification_command_output_boundary_from_path,
    write_portable_source_body_verification_command_output_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

QUESTION = resolver.CORE_COMMAND_OUTPUT_BOUNDARY_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = "RAW_COMMAND_OUTPUT_BOUNDARY_FULL_BODY_MUST_NOT_RETURN_" * 6

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_output_boundary_metadata",
    "declared_command_output_boundary_question",
    "selected_command_output_containment_basis",
    "selected_command_output_containment_terminal_summary_basis",
    "selected_command_output_containment_boundary_basis",
    "selected_post_invocation_command_execution_basis",
    "selected_post_invocation_command_execution_terminal_summary_basis",
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
    "command_output_boundary_only_posture",
    "one_future_command_output_step_posture",
    "command_output_containment_basis_preserved_posture",
    "bounded_output_containment_event_preserved_posture",
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
    "command_output_boundary_scope",
    "command_output_boundary_checks",
    "command_output_boundary_statement",
    "command_output_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_output_boundary_summary",
)

POSTURE_KEYS = (
    "command_output_boundary_only_posture",
    "one_future_command_output_step_posture",
    "command_output_containment_basis_preserved_posture",
    "bounded_output_containment_event_preserved_posture",
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
)

OPEN_ITEMS = (
    "command output boundary test",
    "command output boundary live artifact",
    "command output step, if separately specified",
    "command output",
    "output capture",
    "command output/report artifact",
    "command result",
    "command success",
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
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _reference_shape(label: str, **extra: Any) -> dict[str, Any]:
    basis = {
        "declared": True,
        "basis_label": label,
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
        "full_prior_artifact_body_not_emitted": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    basis.update(extra)
    return basis


def _command_output_containment_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_command_output_containment_basis",
        result_id="command-output-containment-result-001",
        result_path="artifacts/synthetic/command_output_containment.json",
        outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME,
        failed_check_count=0,
        passed_check_count=64,
        command_output_containment_recorded=True,
        bounded_command_output_containment_event_recorded=True,
        one_bounded_command_output_containment_event_recorded=True,
        command_output_boundary_basis_preserved=True,
        recorded_command_execution_event_preserved=True,
        execution_trace_audit_only_preserved=True,
        command_output_created=False,
        output_capture_created=False,
        command_output_report_artifact_created=False,
        command_result_created=False,
        command_success_created=False,
        command_output_not_created=True,
        command_output_still_not_created=True,
        output_capture_not_created=True,
        command_output_report_artifact_not_created=True,
        output_report_artifact_not_created=True,
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_success_not_created=True,
        command_success_still_not_created=True,
        authorization_token_reuse_blocked=True,
        consumed_request_token_remains_closed=True,
        v1_predecessor_failure_preserved=True,
        returned_result_containment_preserved=True,
    )
    basis.update(extra)
    return basis


def _terminal_summary_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        terminal_summary_declared=True,
        terminal_summary_path=f"spec/{label}.md",
        readability_basis_only=True,
        does_not_create_command_output=True,
        does_not_create_output_capture=True,
        does_not_create_output_report_artifact=True,
        does_not_create_command_output_report_artifact=True,
        does_not_create_command_result=True,
        does_not_create_command_success=True,
        does_not_authorize_follow_on_work=True,
    )
    basis.update(extra)
    return basis


def _command_output_containment_boundary_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_command_output_containment_boundary_basis",
        outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        failed_check_count=0,
        one_future_command_output_containment_step_declared=True,
        one_future_output_containment_step_declared=True,
        command_output_not_created=True,
        output_capture_not_created=True,
        command_output_report_artifact_not_created=True,
        command_result_not_created=True,
        command_success_not_created=True,
    )
    basis.update(extra)
    return basis


def _post_invocation_execution_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_post_invocation_command_execution_basis",
        outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        failed_check_count=0,
        one_bounded_command_execution_event_recorded=True,
        bounded_command_execution_event_recorded=True,
        recorded_command_execution_event_preserved=True,
        execution_trace_audit_only=True,
        execution_trace_audit_only_preserved=True,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        command_output_not_created=True,
        command_result_not_created=True,
        command_success_not_created=True,
        execution_trace_treated_as_output=False,
        execution_trace_treated_as_result=False,
        execution_trace_treated_as_success=False,
        execution_trace_treated_as_source=False,
        execution_trace_treated_as_authority=False,
    )
    basis.update(extra)
    return basis


def _command_invocation_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_command_invocation_basis",
        outcome=resolver.COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        bounded_command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
        command_output_not_created=True,
        command_result_not_created=True,
        command_success_not_created=True,
    )
    basis.update(extra)
    return basis


def _command_execution_review_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_command_execution_review_basis",
        outcome=resolver.COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        review_basis_only=True,
        command_output_not_created=True,
        command_result_not_created=True,
        command_success_not_created=True,
    )
    basis.update(extra)
    return basis


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_request_consumption_basis",
        outcome=resolver.REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        request_consumed=True,
        consumption_token_closed=True,
        consumed_request_basis_recorded=True,
    )
    basis.update(extra)
    return basis


def _consumed_request_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_consumed_request_basis",
        consumed_request_basis_declared=True,
        consumed_request_token_remains_closed=True,
        consumed_request_is_not_reopened=True,
        consumed_request_reopened=False,
        consumed_request_basis_is_basis_only=True,
    )
    basis.update(extra)
    return basis


def _v2_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_v2_admitted_request_basis",
        outcome=resolver.V2_ADMITTED_REQUEST_OUTCOME,
        result_version=resolver.V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        successor_metadata_preserved=True,
        returned_result_containment_preserved=True,
        v2_does_not_claim_v1_passed=True,
        v2_successor_does_not_repair_v1=True,
        v2_treated_as_repairing_v1=False,
        v2_repairs_v1=False,
    )
    basis.update(extra)
    return basis


def _v1_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_v1_predecessor_failure_basis",
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
    )
    basis.update(extra)
    return basis


def _older_lineage_basis(**extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        "selected_older_command_execution_boundary_lineage_basis",
        basis_remains_prior_scaffolding_only=True,
        lineage_basis_not_treated_as_current_execution=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
    )
    basis.update(extra)
    return basis


def _generic_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = _reference_shape(
        label,
        basis_is_not_command_output=True,
        basis_is_not_command_result=True,
        basis_is_not_command_success=True,
        basis_is_not_source=True,
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
        "declared": True,
        "posture_declared": True,
        "posture_label": label,
        label: True,
        "command_output_boundary_only": True,
        "one_future_command_output_step_only": True,
        "command_output_containment_basis_preserved": True,
        "bounded_output_containment_event_preserved": True,
        "recorded_command_execution_event_preserved": True,
        "execution_trace_audit_only": True,
        "execution_trace_audit_only_preserved": True,
        "command_output_created": False,
        "output_capture_created": False,
        "command_output_report_artifact_created": False,
        "output_report_artifact_created": False,
        "command_result_created": False,
        "command_success_created": False,
        "command_output_not_created": True,
        "command_output_still_not_created": True,
        "output_capture_not_created": True,
        "command_output_report_artifact_not_created": True,
        "output_report_artifact_not_created": True,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "boundary_treated_as_output": False,
        "boundary_treated_as_output_capture": False,
        "boundary_treated_as_output_report_artifact": False,
        "boundary_treated_as_result": False,
        "boundary_treated_as_success": False,
        "containment_treated_as_output": False,
        "containment_treated_as_output_capture": False,
        "containment_treated_as_output_report_artifact": False,
        "containment_treated_as_result": False,
        "containment_treated_as_success": False,
        "execution_trace_treated_as_output": False,
        "execution_trace_treated_as_result": False,
        "execution_trace_treated_as_success": False,
        "execution_trace_treated_as_source": False,
        "execution_trace_treated_as_authority": False,
        "command_output_became_source": False,
        "command_result_became_authority": False,
        "command_success_created_currentness": False,
        "command_success_claimed_final_completion": False,
        "authorization_token_reused": False,
        "authorization_token_reuse_blocked": True,
        "consumed_request_reopened": False,
        "consumed_request_token_remains_closed": True,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
    }
    posture.update(extra)
    return posture


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request: dict[str, Any] = {
        "command_output_boundary_request_id": "command-output-boundary-request-001",
        "command_output_boundary_question": QUESTION,
        "command_output_boundary_intent": resolver.INTENT_RECORD,
        "selected_command_output_containment_basis": _command_output_containment_basis(),
        "selected_command_output_containment_terminal_summary_basis": _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_output_containment_boundary_basis": _command_output_containment_boundary_basis(),
        "selected_post_invocation_command_execution_basis": _post_invocation_execution_basis(),
        "selected_post_invocation_command_execution_terminal_summary_basis": _terminal_summary_basis(
            "PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_EXECUTION_TERMINAL_SUMMARY_V0"
        ),
        "selected_command_invocation_basis": _command_invocation_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_basis(),
        "selected_v1_predecessor_failure_basis": _v1_basis(),
        "selected_older_command_execution_boundary_lineage_basis": _older_lineage_basis(),
        "selected_command_report_basis": _generic_basis("selected_command_report_basis"),
        "selected_command_implementation_boundary_basis": _generic_basis(
            "selected_command_implementation_boundary_basis"
        ),
        "selected_command_boundary_basis": _generic_basis("selected_command_boundary_basis"),
        "selected_artifact_emission_containment_basis": _generic_basis(
            "selected_artifact_emission_containment_basis"
        ),
        "selected_evidence_manifest_basis": _generic_basis("selected_evidence_manifest_basis"),
        "selected_portable_verification_basis": _generic_basis("selected_portable_verification_basis"),
        "command_output_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_command_output_boundary_outcome": RECORDED,
        "declared_non_claims": _false_non_claims(),
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_input_posture": True,
            "full_prior_artifact_body_not_emitted": True,
        },
    }
    for key in POSTURE_KEYS:
        request[key] = _posture(key)
    request.update(overrides)
    return request


def _resolve(request: dict[str, Any]) -> dict[str, Any]:
    return resolve_portable_source_body_verification_command_output_boundary(
        declared_command_output_boundary_request=request
    )


class CommandOutputBoundaryResolverTests(unittest.TestCase):
    def assertBlocked(self, request: dict[str, Any], expected_code: str | set[str]) -> dict[str, Any]:
        result = _resolve(request)
        self.assertEqual(BLOCKED, result["outcome"])
        codes = {expected_code} if isinstance(expected_code, str) else expected_code
        self.assertIn(result["block"]["code"], codes)
        statement = result["command_output_boundary_statement"]
        for false_key in (
            "command_output_created",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
            "boundary_treated_as_output",
            "containment_treated_as_output",
            "execution_trace_treated_as_output",
            "command_output_became_source",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
            "follow_on_work_authorized",
        ):
            self.assertFalse(statement[false_key])
        return result

    def test_recorded_result_preserves_boundary_only_shape(self) -> None:
        request = _valid_request()
        result = _resolve(request)

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(0, result["portable_source_body_verification_command_output_boundary_summary"]["failed_check_count"])

        metadata = result["portable_source_body_verification_command_output_boundary_metadata"]
        self.assertEqual("0.1.0", metadata["portable_source_body_verification_command_output_boundary_result_version"])
        self.assertEqual("resolve_portable_source_body_verification_command_output_boundary", metadata["resolver_module"])
        self.assertTrue(metadata["short_resolver_filename_preserved"])
        self.assertTrue(metadata["full_upstream_lineage_preserved_in_selected_basis"])

        statement = result["command_output_boundary_statement"]
        for key in (
            "command_output_boundary_recorded",
            "one_future_command_output_step_declared",
            "command_output_containment_basis_preserved",
            "bounded_output_containment_event_preserved",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
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
            self.assertTrue(statement[key], key)
        for key in (
            "command_output_created",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
            "boundary_treated_as_output",
            "boundary_treated_as_output_capture",
            "boundary_treated_as_output_report_artifact",
            "boundary_treated_as_result",
            "boundary_treated_as_success",
            "containment_treated_as_output",
            "containment_treated_as_output_capture",
            "containment_treated_as_output_report_artifact",
            "containment_treated_as_result",
            "containment_treated_as_success",
            "execution_trace_treated_as_output",
            "execution_trace_treated_as_result",
            "execution_trace_treated_as_success",
            "execution_trace_treated_as_source",
            "execution_trace_treated_as_authority",
            "command_output_became_source",
            "command_result_became_authority",
            "command_success_created_currentness",
            "command_success_claimed_final_completion",
        ):
            self.assertFalse(statement[key], key)

        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)

        containment = result["selected_command_output_containment_basis"]
        self.assertEqual(resolver.COMMAND_OUTPUT_CONTAINMENT_OUTCOME, containment["outcome"])
        self.assertEqual(0, containment["failed_check_count"])
        self.assertTrue(containment["bounded_output_containment_event_recorded"])
        self.assertTrue(containment["command_output_boundary_basis_preserved"])
        self.assertTrue(containment["command_output_not_created"])
        self.assertTrue(containment["output_capture_not_created"])
        self.assertTrue(containment["command_output_report_artifact_not_created"])
        self.assertTrue(containment["command_result_not_created"])
        self.assertTrue(containment["command_success_not_created"])
        self.assertTrue(containment["reference_shaped_basis"])

        post_invocation = result["selected_post_invocation_command_execution_basis"]
        self.assertEqual(resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME, post_invocation["outcome"])
        self.assertEqual(0, post_invocation["failed_check_count"])
        self.assertTrue(post_invocation["bounded_command_execution_event_recorded"])
        self.assertTrue(post_invocation["execution_trace_audit_only"])

        older = result["selected_older_command_execution_boundary_lineage_basis"]
        self.assertTrue(older["lineage_basis_not_treated_as_current_execution"])

        for check in result["command_output_boundary_checks"]:
            for key in ("check_name", "passed", "expected_posture", "actual_posture", "block_code", "failure_code"):
                self.assertIn(key, check)
            self.assertTrue(check["passed"], check)

        check_names = {check["check_name"] for check in result["command_output_boundary_checks"]}
        for expected in (
            "command output boundary question declared",
            "command output boundary intent supported",
            "command output containment terminal summary basis declared",
            "command output containment live artifact basis declared",
            "command output containment outcome recorded",
            "command output containment failed check count zero",
            "command output containment event recorded",
            "command output containment boundary basis preserved",
            "post-invocation command execution basis declared",
            "post-invocation command execution trace audit-only",
            "command output boundary scope supported",
            "raw full prior artifact body not emitted",
            "required non-claims explicit and false",
        ):
            self.assertIn(expected, check_names)

        for value in result["command_output_boundary_non_meaning"].values():
            self.assertFalse(value)
        for item in OPEN_ITEMS:
            self.assertIn(item, result["what_remains_open"]["items"])
        self.assertTrue(result["what_remains_open"]["open_means_not_scheduled"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])
        self.assertTrue(result["what_remains_open"]["open_means_not_executed"])

    def test_outcome_family_not_recorded_requires_additional_basis_and_summary(self) -> None:
        not_recorded_request = _valid_request(
            requested_command_output_boundary_outcome=NOT_RECORDED,
            not_recorded_basis={"failed_review_reason": "synthetic readable boundary did not record"},
        )
        not_recorded = _resolve(not_recorded_request)
        self.assertIn(not_recorded["outcome"], OUTCOME_FAMILY)
        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertFalse(not_recorded["command_output_boundary_statement"]["command_output_created"])
        self.assertFalse(not_recorded["command_output_boundary_statement"]["follow_on_work_authorized"])

        additional_request = _valid_request(
            requested_command_output_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context={"missing": "synthetic command output boundary posture detail"},
        )
        additional = _resolve(additional_request)
        self.assertIn(additional["outcome"], OUTCOME_FAMILY)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, additional["outcome"])
        self.assertTrue(additional["additional_basis_required"]["required"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])

        summary = build_portable_source_body_verification_command_output_boundary_summary(
            _resolve(_valid_request())
        )
        for key in (
            "outcome",
            "request_id",
            "question",
            "intent",
            "passed_check_count",
            "failed_check_count",
            "command_output_boundary_recorded",
            "one_future_command_output_step_declared",
            "command_output_containment_basis_preserved",
            "bounded_output_containment_event_preserved",
            "execution_trace_audit_only_preserved",
            "selected_command_output_containment_outcome",
            "selected_post_invocation_execution_outcome",
            "selected_v2_outcome",
            "boundary_not_output_capture_output_report_result_success",
            "containment_not_output_capture_output_report_result_success",
            "execution_trace_not_output_result_success_source_authority",
            "no_raw_full_prior_artifact_body",
            "no_artifact_mutation",
            "key_non_claims",
        ):
            self.assertIn(key, summary)

    def test_request_builder_helper_preserves_sections_and_resolves(self) -> None:
        request = build_declared_portable_source_body_verification_command_output_boundary_request(
            command_output_boundary_request_id="builder-command-output-boundary-request",
            selected_command_output_containment_basis=_command_output_containment_basis(),
            selected_command_output_containment_terminal_summary_basis=_terminal_summary_basis(
                "command_output_containment_terminal_summary"
            ),
            selected_command_output_containment_boundary_basis=_command_output_containment_boundary_basis(),
            selected_post_invocation_command_execution_basis=_post_invocation_execution_basis(),
            selected_post_invocation_command_execution_terminal_summary_basis=_terminal_summary_basis(
                "post_invocation_command_execution_terminal_summary"
            ),
            selected_command_invocation_basis=_command_invocation_basis(),
            selected_command_execution_review_basis=_command_execution_review_basis(),
            selected_request_consumption_basis=_request_consumption_basis(),
            selected_consumed_request_basis=_consumed_request_basis(),
            selected_v2_admitted_request_basis=_v2_basis(),
            selected_v1_predecessor_failure_basis=_v1_basis(),
            selected_older_command_execution_boundary_lineage_basis=_older_lineage_basis(),
            selected_command_report_basis=_generic_basis("selected_command_report_basis"),
            selected_command_implementation_boundary_basis=_generic_basis(
                "selected_command_implementation_boundary_basis"
            ),
            selected_command_boundary_basis=_generic_basis("selected_command_boundary_basis"),
            selected_artifact_emission_containment_basis=_generic_basis(
                "selected_artifact_emission_containment_basis"
            ),
            selected_evidence_manifest_basis=_generic_basis("selected_evidence_manifest_basis"),
            selected_portable_verification_basis=_generic_basis("selected_portable_verification_basis"),
            command_output_boundary_only_posture=_posture("command_output_boundary_only_posture"),
            one_future_command_output_step_posture=_posture("one_future_command_output_step_posture"),
            command_output_containment_basis_preserved_posture=_posture(
                "command_output_containment_basis_preserved_posture"
            ),
            bounded_output_containment_event_preserved_posture=_posture(
                "bounded_output_containment_event_preserved_posture"
            ),
            execution_trace_audit_only_posture=_posture("execution_trace_audit_only_posture"),
            no_command_output_posture=_posture("no_command_output_posture"),
            no_output_capture_posture=_posture("no_output_capture_posture"),
            no_output_report_artifact_posture=_posture("no_output_report_artifact_posture"),
            no_command_result_posture=_posture("no_command_result_posture"),
            no_command_success_posture=_posture("no_command_success_posture"),
            no_output_as_source_posture=_posture("no_output_as_source_posture"),
            no_result_as_authority_posture=_posture("no_result_as_authority_posture"),
            no_success_as_currentness_posture=_posture("no_success_as_currentness_posture"),
            no_final_completion_posture=_posture("no_final_completion_posture"),
            authorization_token_reuse_blocked_posture=_posture(
                "authorization_token_reuse_blocked_posture"
            ),
            consumed_token_closed_posture=_posture("consumed_token_closed_posture"),
            no_reopen_consumed_request_posture=_posture("no_reopen_consumed_request_posture"),
            returned_result_containment_posture=_posture("returned_result_containment_posture"),
            command_output_boundary_scope=SUPPORTED_SCOPE,
            reference_shaped_input_posture={"declared": True, "reference_shaped_input_posture": True},
        )

        self.assertEqual("builder-command-output-boundary-request", request["command_output_boundary_request_id"])
        self.assertEqual(QUESTION, request["command_output_boundary_question"])
        self.assertEqual(resolver.INTENT_RECORD, request["command_output_boundary_intent"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, request["declared_non_claims"])
            self.assertFalse(request["declared_non_claims"][key])

        result = _resolve(request)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertTrue(result["command_output_boundary_statement"]["command_output_boundary_recorded"])

    def test_path_and_write_behavior_is_additive(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            result = resolve_portable_source_body_verification_command_output_boundary_from_path(request_path)
            self.assertEqual(RECORDED, result["outcome"])
            self.assertEqual(str(request_path), result["declared_command_output_boundary_question"]["declared_request_path"])

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_command_output_boundary_from_path(malformed_path)
            self.assertEqual(BLOCKED, malformed["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED", malformed["block"]["code"])

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_command_output_boundary_from_path(array_path)
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED", array_result["block"]["code"])

            missing = resolve_portable_source_body_verification_command_output_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(BLOCKED, missing["outcome"])
            self.assertEqual("DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_UNREADABLE", missing["block"]["code"])

            output_path = tmp_path / "nested" / "result.json"
            written = write_portable_source_body_verification_command_output_boundary_result(
                result, output_path
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, parsed)
            second = write_portable_source_body_verification_command_output_boundary_result(
                result, output_path
            )
            self.assertNotEqual(written, second)
            self.assertTrue(second.name.endswith("_001.json"))

            default_root = tmp_path / "command_output_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_BOUNDARY_ROOT",
                default_root,
            ):
                default_written = write_portable_source_body_verification_command_output_boundary_result(result)
            self.assertTrue(default_written.is_relative_to(default_root))
            self.assertNotIn("command_output_containment_boundary", str(default_written))
            self.assertNotIn("post_invocation_command_execution", str(default_written))

    def test_full_body_and_reference_shape_block_without_returning_raw_value(self) -> None:
        request = _valid_request(full_artifact_body=RAW_FULL_BODY_SENTINEL)
        result = self.assertBlocked(request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, json.dumps(result, sort_keys=True))

        selected_body_request = _valid_request()
        selected_body_request["selected_command_output_containment_basis"]["full_artifact_body"] = {
            "omitted": "synthetic"
        }
        selected_body_result = self.assertBlocked(
            selected_body_request, "FULL_PRIOR_ARTIFACT_BODY_EMITTED"
        )
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, json.dumps(selected_body_result, sort_keys=True))

    def test_resolver_does_not_mutate_request_or_selected_basis(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        selected_object_ids = {
            key: id(request[key])
            for key in (
                "selected_command_output_containment_basis",
                "selected_command_output_containment_terminal_summary_basis",
                "selected_command_output_containment_boundary_basis",
                "selected_post_invocation_command_execution_basis",
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
                "command_output_boundary_scope",
            )
        }
        _resolve(request)
        _resolve(request)
        self.assertEqual(original, request)
        for key, object_id in selected_object_ids.items():
            self.assertEqual(object_id, id(request[key]), key)

    def test_blocked_malformed_request_intent_and_scope(self) -> None:
        explicit = _valid_request(command_output_boundary_intent=resolver.INTENT_BLOCK)
        explicit_result = _resolve(explicit)
        self.assertEqual(BLOCKED, explicit_result["outcome"])
        self.assertEqual("COMMAND_OUTPUT_BOUNDARY_BLOCKED_BY_REQUEST", explicit_result["block"]["code"])

        missing = resolve_portable_source_body_verification_command_output_boundary()
        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertEqual("COMMAND_OUTPUT_BOUNDARY_QUESTION_UNDECLARED", missing["block"]["code"])

        malformed = resolve_portable_source_body_verification_command_output_boundary(
            declared_command_output_boundary_request=["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertEqual("DECLARED_COMMAND_OUTPUT_BOUNDARY_REQUEST_MALFORMED", malformed["block"]["code"])

        unsupported_intent = _valid_request(command_output_boundary_intent="UNSUPPORTED")
        self.assertBlocked(unsupported_intent, "COMMAND_OUTPUT_BOUNDARY_INTENT_UNSUPPORTED")

        unsupported_scope = _valid_request(command_output_boundary_scope=["NOT_A_BOUNDARY_SCOPE"])
        self.assertBlocked(unsupported_scope, "UNSUPPORTED_COMMAND_OUTPUT_BOUNDARY_SCOPE")

    def test_blocking_selected_basis_requirements(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], None], str]] = [
            (
                "missing containment basis",
                lambda r: r.pop("selected_command_output_containment_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_MISSING",
            ),
            (
                "containment not recorded",
                lambda r: r["selected_command_output_containment_basis"].update(outcome="NOT_RECORDED"),
                "COMMAND_OUTPUT_CONTAINMENT_NOT_RECORDED",
            ),
            (
                "containment failed checks",
                lambda r: r["selected_command_output_containment_basis"].update(failed_check_count=1),
                "COMMAND_OUTPUT_CONTAINMENT_FAILED_CHECKS_PRESENT",
            ),
            (
                "containment event not recorded",
                lambda r: r["selected_command_output_containment_basis"].update(
                    bounded_command_output_containment_event_recorded=False,
                    command_output_containment_recorded=False,
                    one_bounded_command_output_containment_event_recorded=False,
                ),
                "COMMAND_OUTPUT_CONTAINMENT_EVENT_NOT_RECORDED",
            ),
            (
                "containment boundary basis not preserved",
                lambda r: r["selected_command_output_containment_basis"].update(
                    command_output_boundary_basis_preserved=False
                ),
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_NOT_PRESERVED",
            ),
            (
                "containment created output",
                lambda r: r["selected_command_output_containment_basis"].update(command_output_created=True),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT",
            ),
            (
                "containment created output capture",
                lambda r: r["selected_command_output_containment_basis"].update(output_capture_created=True),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            (
                "containment created report artifact",
                lambda r: r["selected_command_output_containment_basis"].update(
                    command_output_report_artifact_created=True
                ),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "containment created result",
                lambda r: r["selected_command_output_containment_basis"].update(command_result_created=True),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_RESULT",
            ),
            (
                "containment created success",
                lambda r: r["selected_command_output_containment_basis"].update(command_success_created=True),
                "COMMAND_OUTPUT_CONTAINMENT_ALREADY_CREATED_SUCCESS",
            ),
            (
                "missing containment boundary basis",
                lambda r: r.pop("selected_command_output_containment_boundary_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing post invocation execution basis",
                lambda r: r.pop("selected_post_invocation_command_execution_basis"),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            (
                "post invocation not recorded",
                lambda r: r["selected_post_invocation_command_execution_basis"].update(outcome="NOT_RECORDED"),
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            (
                "post invocation failed checks",
                lambda r: r["selected_post_invocation_command_execution_basis"].update(failed_check_count=1),
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            (
                "post invocation trace not audit-only",
                lambda r: r["selected_post_invocation_command_execution_basis"].update(
                    execution_trace_audit_only=False,
                    execution_trace_audit_only_preserved=False,
                ),
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            (
                "v2 basis missing",
                lambda r: r.pop("selected_v2_admitted_request_basis"),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            (
                "v2 failed checks",
                lambda r: r["selected_v2_admitted_request_basis"].update(failed_check_count=1),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "v1 basis missing",
                lambda r: r.pop("selected_v1_predecessor_failure_basis"),
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            (
                "older lineage current execution",
                lambda r: r["selected_older_command_execution_boundary_lineage_basis"].update(
                    older_command_execution_boundary_lineage_treated_as_current_execution=True
                ),
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            (
                "command report missing",
                lambda r: r.pop("selected_command_report_basis"),
                "COMMAND_REPORT_BASIS_MISSING",
            ),
            (
                "command implementation boundary missing",
                lambda r: r.pop("selected_command_implementation_boundary_basis"),
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            (
                "command boundary missing",
                lambda r: r.pop("selected_command_boundary_basis"),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            (
                "artifact containment missing",
                lambda r: r.pop("selected_artifact_emission_containment_basis"),
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            (
                "evidence manifest missing",
                lambda r: r.pop("selected_evidence_manifest_basis"),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            (
                "portable verification missing",
                lambda r: r.pop("selected_portable_verification_basis"),
                "PORTABLE_VERIFICATION_BASIS_MISSING",
            ),
        ]
        for name, mutate, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self.assertBlocked(request, code)

    def test_blocking_posture_and_collapse_flags(self) -> None:
        cases: list[tuple[str, Callable[[dict[str, Any]], None], str | set[str]]] = [
            (
                "missing boundary posture",
                lambda r: r.pop("command_output_boundary_only_posture"),
                "COMMAND_OUTPUT_BOUNDARY_ONLY_POSTURE_MISSING",
            ),
            (
                "missing future step posture",
                lambda r: r.pop("one_future_command_output_step_posture"),
                "ONE_FUTURE_COMMAND_OUTPUT_STEP_POSTURE_MISSING",
            ),
            (
                "missing containment basis preserved posture",
                lambda r: r.pop("command_output_containment_basis_preserved_posture"),
                "COMMAND_OUTPUT_CONTAINMENT_BASIS_PRESERVED_POSTURE_MISSING",
            ),
            (
                "missing bounded event posture",
                lambda r: r.pop("bounded_output_containment_event_preserved_posture"),
                "BOUNDED_OUTPUT_CONTAINMENT_EVENT_PRESERVED_POSTURE_MISSING",
            ),
            (
                "missing execution trace posture",
                lambda r: r.pop("execution_trace_audit_only_posture"),
                "EXECUTION_TRACE_AUDIT_ONLY_POSTURE_MISSING",
            ),
            (
                "missing no output posture",
                lambda r: r.pop("no_command_output_posture"),
                "NO_COMMAND_OUTPUT_POSTURE_MISSING",
            ),
            (
                "missing no capture posture",
                lambda r: r.pop("no_output_capture_posture"),
                "NO_OUTPUT_CAPTURE_POSTURE_MISSING",
            ),
            (
                "missing no report posture",
                lambda r: r.pop("no_output_report_artifact_posture"),
                "NO_OUTPUT_REPORT_ARTIFACT_POSTURE_MISSING",
            ),
            (
                "missing no result posture",
                lambda r: r.pop("no_command_result_posture"),
                "NO_COMMAND_RESULT_POSTURE_MISSING",
            ),
            (
                "missing no success posture",
                lambda r: r.pop("no_command_success_posture"),
                "NO_COMMAND_SUCCESS_POSTURE_MISSING",
            ),
            (
                "boundary treated as output",
                lambda r: r.update(boundary_treated_as_output=True),
                "BOUNDARY_TREATED_AS_OUTPUT",
            ),
            (
                "boundary treated as capture",
                lambda r: r.update(boundary_treated_as_output_capture=True),
                "BOUNDARY_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "boundary treated as report",
                lambda r: r.update(boundary_treated_as_output_report_artifact=True),
                "BOUNDARY_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "boundary treated as result",
                lambda r: r.update(boundary_treated_as_result=True),
                "BOUNDARY_TREATED_AS_RESULT",
            ),
            (
                "boundary treated as success",
                lambda r: r.update(boundary_treated_as_success=True),
                "BOUNDARY_TREATED_AS_SUCCESS",
            ),
            (
                "containment treated as output",
                lambda r: r.update(containment_treated_as_output=True),
                "CONTAINMENT_TREATED_AS_OUTPUT",
            ),
            (
                "containment treated as capture",
                lambda r: r.update(containment_treated_as_output_capture=True),
                "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE",
            ),
            (
                "containment treated as report",
                lambda r: r.update(containment_treated_as_output_report_artifact=True),
                "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "containment treated as result",
                lambda r: r.update(containment_treated_as_result=True),
                "CONTAINMENT_TREATED_AS_RESULT",
            ),
            (
                "containment treated as success",
                lambda r: r.update(containment_treated_as_success=True),
                "CONTAINMENT_TREATED_AS_SUCCESS",
            ),
            ("command output created", lambda r: r.update(command_output_created=True), "COMMAND_OUTPUT_CREATED"),
            ("output capture created", lambda r: r.update(output_capture_created=True), "OUTPUT_CAPTURE_CREATED"),
            (
                "output report artifact created",
                lambda r: r.update(command_output_report_artifact_created=True),
                "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            ),
            ("command result created", lambda r: r.update(command_result_created=True), "COMMAND_RESULT_CREATED"),
            ("command success created", lambda r: r.update(command_success_created=True), "COMMAND_SUCCESS_CREATED"),
            (
                "trace treated as output",
                lambda r: r.update(execution_trace_treated_as_output=True),
                "EXECUTION_TRACE_TREATED_AS_OUTPUT",
            ),
            (
                "trace treated as result",
                lambda r: r.update(execution_trace_treated_as_result=True),
                "EXECUTION_TRACE_TREATED_AS_RESULT",
            ),
            (
                "trace treated as success",
                lambda r: r.update(execution_trace_treated_as_success=True),
                "EXECUTION_TRACE_TREATED_AS_SUCCESS",
            ),
            (
                "trace treated as source",
                lambda r: r.update(execution_trace_treated_as_source=True),
                "EXECUTION_TRACE_TREATED_AS_SOURCE",
            ),
            (
                "trace treated as authority",
                lambda r: r.update(execution_trace_treated_as_authority=True),
                "EXECUTION_TRACE_TREATED_AS_AUTHORITY",
            ),
            (
                "output became source",
                lambda r: r.update(command_output_became_source=True),
                "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            ),
            (
                "result became authority",
                lambda r: r.update(command_result_became_authority=True),
                "COMMAND_RESULT_TREATED_AS_AUTHORITY",
            ),
            (
                "success currentness",
                lambda r: r.update(command_success_created_currentness=True),
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "success final completion",
                lambda r: r.update(command_success_claimed_final_completion=True),
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            (
                "consumed request reopened",
                lambda r: r.update(consumed_request_reopened=True),
                "CONSUMED_REQUEST_REOPENED",
            ),
            (
                "authorization token reused",
                lambda r: r.update(authorization_token_reused=True),
                "AUTHORIZATION_TOKEN_REUSED",
            ),
            ("v1 repaired", lambda r: r.update(v1_repaired=True), "V2_TREATED_AS_REPAIRING_V1"),
            ("v1 hidden", lambda r: r.update(v1_hidden=True), "V1_FAILURE_HIDDEN"),
            ("v1 claimed passed", lambda r: r.update(v1_claimed_passed=True), "V1_CLAIMED_PASSED"),
            ("artifacts mutated", lambda r: r.update(prior_artifacts_mutated=True), "ARTIFACTS_MUTATED"),
            ("deployment", lambda r: r.update(deployment_created=True), "DEPLOYMENT_CREATED"),
            ("runtime", lambda r: r.update(runtime_hosting_created=True), "RUNTIME_HOSTING_CREATED"),
            ("public release", lambda r: r.update(public_release_created=True), "PUBLIC_RELEASE_CREATED"),
            ("operation", lambda r: r.update(operation_permission_created=True), "OPERATION_CREATED"),
            ("public readiness", lambda r: r.update(public_launch_readiness_created=True), "PUBLIC_READINESS_CREATED"),
            ("final completion", lambda r: r.update(final_completion_claimed=True), "FINAL_COMPLETION_CLAIMED"),
            ("continuation", lambda r: r.update(continuation_authorized=True), "CONTINUATION_AUTHORIZED"),
            ("reusable permission", lambda r: r.update(reusable_permission_created=True), "REUSABLE_PERMISSION_CREATED"),
            (
                "derivative reception",
                lambda r: r.update(derivative_reception_authorized=True),
                "DERIVATIVE_RECEPTION_AUTHORIZED",
            ),
            ("vessel relation", lambda r: r.update(vessel_relation_authorized=True), "VESSEL_RELATION_AUTHORIZED"),
            (
                "another reception",
                lambda r: r.update(another_reception_request_authorized=True),
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            ),
            ("follow-on", lambda r: r.update(follow_on_work_authorized=True), "FOLLOW_ON_WORK_AUTHORIZED"),
            ("mutation", lambda r: r.update(mutation_performed=True), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ("replay", lambda r: r.update(replay_performed=True), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ("merge", lambda r: r.update(merge_performed=True), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        ]
        for name, mutate, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self.assertBlocked(request, code)

    def test_required_non_claims_missing_or_flipped_block(self) -> None:
        missing = _valid_request()
        missing["declared_non_claims"].pop("command_output_created")
        self.assertBlocked(missing, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = _valid_request()
        flipped["declared_non_claims"]["command_output_created"] = True
        self.assertBlocked(flipped, {"COMMAND_OUTPUT_CREATED", "NON_CLAIM_MISSING_OR_FLIPPED"})


if __name__ == "__main__":
    unittest.main()
