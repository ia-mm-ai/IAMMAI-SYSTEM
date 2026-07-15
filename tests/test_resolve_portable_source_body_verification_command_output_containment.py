"""Bounded tests for portable source-body command output containment only.

This suite is downstream of the recorded command output containment boundary.
It proves that one bounded output-containment event can be recorded without
creating command output, output capture, an output/report artifact, command
result, command success, source, authority, currentness, final completion, or
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

import resolve_portable_source_body_verification_command_output_containment as resolver
from resolve_portable_source_body_verification_command_output_containment import (
    build_declared_portable_source_body_verification_command_output_containment_request,
    build_portable_source_body_verification_command_output_containment_summary,
    resolve_portable_source_body_verification_command_output_containment,
    resolve_portable_source_body_verification_command_output_containment_from_path,
    write_portable_source_body_verification_command_output_containment_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
QUESTION = resolver.CORE_COMMAND_OUTPUT_CONTAINMENT_QUESTION
SUPPORTED_SCOPE = tuple(resolver.SUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE)
REQUIRED_FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
RAW_FULL_BODY_SENTINEL = (
    "RAW_COMMAND_OUTPUT_CONTAINMENT_FULL_BODY_MUST_NOT_RETURN_" * 6
)

TOP_LEVEL_SECTIONS = (
    "portable_source_body_verification_command_output_containment_metadata",
    "declared_command_output_containment_question",
    "selected_command_output_containment_boundary_basis",
    "selected_command_output_containment_boundary_terminal_summary_basis",
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
    "output_containment_only_posture",
    "one_bounded_command_output_containment_event_posture",
    "command_output_boundary_basis_preserved_posture",
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
    "command_output_containment_scope",
    "command_output_containment_checks",
    "command_output_containment_statement",
    "command_output_containment_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_output_containment_summary",
)

SELECTED_BASIS_KEYS = (
    "selected_command_output_containment_boundary_basis",
    "selected_command_output_containment_boundary_terminal_summary_basis",
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
)

POSTURE_KEYS = (
    "output_containment_only_posture",
    "one_bounded_command_output_containment_event_posture",
    "command_output_boundary_basis_preserved_posture",
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
)

OPEN_ITEMS = (
    "command_output_containment_test",
    "command_output_containment_live_artifact",
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


def _boundary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_command_output_containment_boundary_basis",
        result_id="command-output-containment-boundary-result-001",
        result_path="artifacts/synthetic/command_output_containment_boundary.json",
        outcome=resolver.COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        failed_check_count=0,
        one_future_command_output_containment_step_declared=True,
        one_future_output_containment_step_declared=True,
        command_output_containment_boundary_recorded=True,
        recorded_command_execution_event_preserved=True,
        execution_trace_audit_only_preserved=True,
        command_output_not_created=True,
        command_output_still_not_created=True,
        command_output_created=False,
        output_capture_not_created=True,
        output_capture_created=False,
        command_output_report_artifact_not_created=True,
        command_output_report_artifact_created=False,
        command_result_not_created=True,
        command_result_still_not_created=True,
        command_result_created=False,
        command_success_not_created=True,
        command_success_still_not_created=True,
        command_success_created=False,
        authorization_token_reuse_blocked=True,
        consumed_request_token_remains_closed=True,
        v1_predecessor_failure_preserved=True,
        returned_result_containment_preserved=True,
        **extra,
    )


def _boundary_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_command_output_containment_boundary_terminal_summary_basis",
        terminal_summary_declared=True,
        terminal_summary_path=(
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_"
            "BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        readability_basis_only=True,
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_output=True,
        terminal_summary_does_not_create_output_capture=True,
        terminal_summary_does_not_create_output_report_artifact=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
        command_output_created=False,
        output_capture_created=False,
        command_output_report_artifact_created=False,
        command_result_created=False,
        command_success_created=False,
        **extra,
    )


def _post_invocation_execution_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_post_invocation_command_execution_basis",
        result_id="post-invocation-command-execution-result-001",
        result_path="artifacts/synthetic/post_invocation_command_execution.json",
        outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        failed_check_count=0,
        one_bounded_command_execution_event_recorded=True,
        bounded_command_execution_event_recorded=True,
        execution_event_recorded=True,
        execution_trace_recorded_as_audit_only=True,
        execution_trace_audit_only=True,
        execution_trace_audit_only_preserved=True,
        command_output_not_created=True,
        command_output_created=False,
        command_result_not_created=True,
        command_result_created=False,
        command_success_not_created=True,
        command_success_created=False,
        execution_trace_is_not_output=True,
        execution_trace_is_not_result=True,
        execution_trace_is_not_success=True,
        execution_trace_is_not_source=True,
        execution_trace_is_not_authority=True,
        execution_trace_treated_as_output=False,
        execution_trace_treated_as_result=False,
        execution_trace_treated_as_success=False,
        execution_trace_treated_as_source=False,
        execution_trace_treated_as_authority=False,
        **extra,
    )


def _post_invocation_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_post_invocation_command_execution_terminal_summary_basis",
        terminal_summary_declared=True,
        terminal_summary_path=(
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_POST_INVOCATION_COMMAND_"
            "EXECUTION_TERMINAL_SUMMARY_V0.md"
        ),
        readability_basis_only=True,
        terminal_summary_remains_readability_basis_only=True,
        terminal_summary_does_not_create_command_output=True,
        terminal_summary_does_not_create_command_result=True,
        terminal_summary_does_not_create_command_success=True,
        terminal_summary_does_not_authorize_follow_on_work=True,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        **extra,
    )


def _post_invocation_execution_boundary_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_post_invocation_command_execution_boundary_basis",
        outcome=resolver.POST_INVOCATION_COMMAND_EXECUTION_BOUNDARY_OUTCOME,
        failed_check_count=0,
        boundary_basis_only=True,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        authority_created=False,
        currentness_created=False,
        final_completion_claimed=False,
        follow_on_work_authorized=False,
        **extra,
    )


def _command_invocation_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_command_invocation_basis",
        result_path="artifacts/synthetic/command_invocation.json",
        outcome=resolver.COMMAND_INVOCATION_OUTCOME,
        failed_check_count=0,
        bounded_command_invocation_event_recorded=True,
        authorization_token_spent_exactly_once=True,
        authorization_token_reuse_blocked=True,
        **extra,
    )


def _command_execution_review_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_command_execution_review_basis",
        result_path="artifacts/synthetic/command_execution_review.json",
        outcome=resolver.COMMAND_EXECUTION_REVIEW_OUTCOME,
        failed_check_count=0,
        review_basis_only=True,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        **extra,
    )


def _request_consumption_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_request_consumption_basis",
        result_path="artifacts/synthetic/request_consumption.json",
        outcome=resolver.REQUEST_CONSUMPTION_OUTCOME,
        failed_check_count=0,
        request_consumed_exactly_once=True,
        consumption_token_closed=True,
        consumed_request_basis_recorded=True,
        **extra,
    )


def _consumed_request_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_consumed_request_basis",
        consumed_request_basis_declared=True,
        consumed_request_token_remains_closed=True,
        consumed_request_is_not_reopened=True,
        consumed_request_not_reopened=True,
        consumed_request_reopened=False,
        consumed_request_basis_is_basis_only=True,
        **extra,
    )


def _v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_v2_admitted_request_basis",
        result_path="artifacts/synthetic/v2_admitted_request.json",
        outcome=resolver.V2_ADMITTED_REQUEST_OUTCOME,
        result_version=resolver.V2_ADMITTED_REQUEST_VERSION,
        failed_check_count=0,
        successor_metadata_preserved=True,
        returned_result_containment_preserved=True,
        v2_does_not_claim_v1_passed=True,
        v2_successor_does_not_erase_v1=True,
        v2_treated_as_repairing_v1=False,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        **extra,
    )


def _v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_v1_predecessor_failure_basis",
        result_path="artifacts/synthetic/v1_predecessor_failure.json",
        v1_predecessor_failure_basis_declared=True,
        v1_remains_visible_predecessor_failure_evidence=True,
        v1_predecessor_failure_preserved=True,
        v1_is_not_repaired=True,
        v1_is_not_hidden=True,
        v1_is_not_claimed_passed=True,
        v1_repaired=False,
        v1_hidden=False,
        v1_claimed_passed=False,
        v2_successor_does_not_erase_v1=True,
        predecessor_failure_evidence_is_lineage_evidence_only=True,
        **extra,
    )


def _older_lineage_basis(**extra: Any) -> dict[str, Any]:
    return _reference_shape(
        "selected_older_command_execution_boundary_lineage_basis",
        result_path="artifacts/synthetic/older_command_execution_boundary.json",
        basis_remains_prior_scaffolding_only=True,
        lineage_basis_not_treated_as_current_execution=True,
        older_command_execution_boundary_lineage_treated_as_current_execution=False,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        **extra,
    )


def _generic_prior_basis(label: str, **extra: Any) -> dict[str, Any]:
    return _reference_shape(
        label,
        result_path=f"artifacts/synthetic/{label}.json",
        basis_is_not_command_output=True,
        basis_is_not_command_result=True,
        basis_is_not_command_success=True,
        basis_is_not_authority=True,
        basis_is_not_currentness=True,
        basis_is_not_final_completion=True,
        basis_does_not_authorize_continuation=True,
        basis_does_not_authorize_follow_on_work=True,
        command_output_created=False,
        command_result_created=False,
        command_success_created=False,
        **extra,
    )


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "declared": True,
        "posture": label,
        "posture_declared": True,
        "containment_not_output": True,
        "containment_not_output_capture": True,
        "containment_not_output_report_artifact": True,
        "containment_not_result": True,
        "containment_not_success": True,
        "command_output_not_created": True,
        "command_output_still_not_created": True,
        "command_output_created": False,
        "output_capture_not_created": True,
        "output_capture_created": False,
        "command_output_report_artifact_not_created": True,
        "command_output_report_artifact_created": False,
        "command_result_not_created": True,
        "command_result_still_not_created": True,
        "command_result_created": False,
        "command_success_not_created": True,
        "command_success_still_not_created": True,
        "command_success_created": False,
        "execution_trace_audit_only": True,
        "execution_trace_not_output": True,
        "execution_trace_not_result": True,
        "execution_trace_not_success": True,
        "execution_trace_not_source": True,
        "execution_trace_not_authority": True,
        "output_not_source": True,
        "result_not_authority": True,
        "success_not_currentness": True,
        "success_not_final_completion": True,
        "authorization_token_reuse_blocked": True,
        "consumed_request_token_remains_closed": True,
        "consumed_request_not_reopened": True,
        "returned_result_containment_preserved": True,
        "raw_full_prior_artifact_body_returned": False,
        "prior_artifacts_mutated": False,
    }
    posture.update(extra)
    return posture


def _postures() -> dict[str, dict[str, Any]]:
    return {key: _posture(key) for key in POSTURE_KEYS}


def _valid_request(**overrides: Any) -> dict[str, Any]:
    request: dict[str, Any] = {
        "command_output_containment_request_id": "command-output-containment-request-001",
        "command_output_containment_question": QUESTION,
        "command_output_containment_intent": resolver.INTENT_RECORD,
        "selected_command_output_containment_boundary_basis": _boundary_basis(),
        "selected_command_output_containment_boundary_terminal_summary_basis": (
            _boundary_terminal_summary_basis()
        ),
        "selected_post_invocation_command_execution_basis": (
            _post_invocation_execution_basis()
        ),
        "selected_post_invocation_command_execution_terminal_summary_basis": (
            _post_invocation_terminal_summary_basis()
        ),
        "selected_post_invocation_command_execution_boundary_basis": (
            _post_invocation_execution_boundary_basis()
        ),
        "selected_command_invocation_basis": _command_invocation_basis(),
        "selected_command_execution_review_basis": _command_execution_review_basis(),
        "selected_request_consumption_basis": _request_consumption_basis(),
        "selected_consumed_request_basis": _consumed_request_basis(),
        "selected_v2_admitted_request_basis": _v2_admitted_request_basis(),
        "selected_v1_predecessor_failure_basis": _v1_predecessor_failure_basis(),
        "selected_older_command_execution_boundary_lineage_basis": _older_lineage_basis(),
        "selected_command_report_basis": _generic_prior_basis("selected_command_report_basis"),
        "selected_command_implementation_boundary_basis": _generic_prior_basis(
            "selected_command_implementation_boundary_basis"
        ),
        "selected_command_boundary_basis": _generic_prior_basis(
            "selected_command_boundary_basis"
        ),
        "selected_artifact_emission_containment_basis": _generic_prior_basis(
            "selected_artifact_emission_containment_basis"
        ),
        "selected_evidence_manifest_basis": _generic_prior_basis(
            "selected_evidence_manifest_basis"
        ),
        "selected_portable_verification_basis": _generic_prior_basis(
            "selected_portable_verification_basis"
        ),
        "command_output_containment_scope": list(SUPPORTED_SCOPE),
        "declared_non_claims": _false_non_claims(),
        "requested_command_output_containment_outcome": RECORDED,
        "selected_command_output_containment_boundary_result_path": (
            "artifacts/synthetic/command_output_containment_boundary.json"
        ),
        "selected_command_output_containment_boundary_result_id": (
            "command-output-containment-boundary-result-001"
        ),
        "selected_command_output_containment_boundary_result_outcome": (
            resolver.COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME
        ),
        "selected_command_output_containment_boundary_failed_check_count": 0,
        "selected_command_output_containment_boundary_step_declared": True,
        "selected_command_output_containment_boundary_output_created": False,
        "selected_command_output_containment_boundary_output_capture_created": False,
        "selected_command_output_containment_boundary_output_report_artifact_created": False,
        "selected_command_output_containment_boundary_result_created": False,
        "selected_command_output_containment_boundary_success_created": False,
        "selected_post_invocation_command_execution_result_path": (
            "artifacts/synthetic/post_invocation_command_execution.json"
        ),
        "selected_post_invocation_command_execution_result_id": (
            "post-invocation-command-execution-result-001"
        ),
        "selected_post_invocation_command_execution_result_outcome": (
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME
        ),
        "selected_post_invocation_command_execution_failed_check_count": 0,
        "selected_post_invocation_command_execution_event_recorded": True,
        "selected_post_invocation_command_execution_trace_audit_only": True,
        "selected_command_invocation_result_path": (
            "artifacts/synthetic/command_invocation.json"
        ),
        "selected_command_execution_review_result_path": (
            "artifacts/synthetic/command_execution_review.json"
        ),
        "selected_request_consumption_result_path": (
            "artifacts/synthetic/request_consumption.json"
        ),
        "selected_v2_admitted_request_artifact_path": (
            "artifacts/synthetic/v2_admitted_request.json"
        ),
        "selected_v2_admitted_request_outcome": resolver.V2_ADMITTED_REQUEST_OUTCOME,
        "selected_v2_admitted_request_version": resolver.V2_ADMITTED_REQUEST_VERSION,
        "selected_v2_failed_check_count": 0,
        "selected_v1_predecessor_artifact_path": (
            "artifacts/synthetic/v1_predecessor_failure.json"
        ),
        "selected_older_command_execution_boundary_lineage_result_path": (
            "artifacts/synthetic/older_command_execution_boundary.json"
        ),
        "selected_command_report_path": "artifacts/synthetic/command_report.json",
        "selected_command_implementation_boundary_result_path": (
            "artifacts/synthetic/command_implementation_boundary.json"
        ),
        "selected_command_boundary_result_path": (
            "artifacts/synthetic/command_boundary.json"
        ),
        "selected_artifact_emission_containment_result_path": (
            "artifacts/synthetic/artifact_emission_containment.json"
        ),
        "selected_evidence_manifest_result_path": (
            "artifacts/synthetic/evidence_manifest.json"
        ),
        "selected_portable_verification_result_path": (
            "artifacts/synthetic/portable_verification.json"
        ),
        "reference_shaped_input_posture": _posture("reference_shaped_input_posture"),
    }
    request.update(_postures())
    request.update(overrides)
    return request


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True)


def _check_counts(result: dict[str, Any]) -> tuple[int, int]:
    checks = result["command_output_containment_checks"]
    passed = sum(1 for check in checks if check.get("passed") is True)
    return passed, len(checks) - passed


class PortableSourceBodyVerificationCommandOutputContainmentTests(unittest.TestCase):
    def _resolve(self, request: Any) -> dict[str, Any]:
        return resolve_portable_source_body_verification_command_output_containment(
            declared_command_output_containment_request=request
        )

    def _recorded_result(self) -> dict[str, Any]:
        result = self._resolve(_valid_request())
        self.assertEqual(result["outcome"], RECORDED)
        return result

    def _assert_block(self, result: dict[str, Any], code: str | set[str]) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertEqual(result["outcome"], BLOCKED)
        codes = code if isinstance(code, set) else {code}
        self.assertIn(result["block"].get("block_code", result["block"].get("code")), codes)
        statement = result["command_output_containment_statement"]
        for key in (
            "command_output_created",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
        ):
            self.assertFalse(statement[key])

    def _assert_no_created_work(self, result: dict[str, Any]) -> None:
        statement = result["command_output_containment_statement"]
        for key in (
            "command_output_created",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
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
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertFalse(statement[key], key)

    def test_recorded_result_contains_required_sections_and_statement(self) -> None:
        result = self._recorded_result()

        self.assertIsInstance(result, dict)
        for section in TOP_LEVEL_SECTIONS:
            self.assertIn(section, result)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        _passed, failed = _check_counts(result)
        self.assertEqual(failed, 0)
        self.assertEqual(result["outcome"], RECORDED)

        statement = result["command_output_containment_statement"]
        for key in (
            "command_output_containment_recorded",
            "bounded_command_output_containment_event_recorded",
            "command_output_boundary_basis_preserved",
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

        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, statement)
            self.assertFalse(statement[key], key)
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)

        scope = result["command_output_containment_scope"]
        self.assertEqual(set(scope["selected_scope_values"]), set(SUPPORTED_SCOPE))
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self._assert_no_created_work(result)

    def test_metadata_and_selected_basis_preserve_lineage(self) -> None:
        result = self._recorded_result()
        metadata = result["portable_source_body_verification_command_output_containment_metadata"]

        for key in (
            "portable_source_body_verification_command_output_containment_result_id",
            "portable_source_body_verification_command_output_containment_result_type",
            "portable_source_body_verification_command_output_containment_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            metadata["portable_source_body_verification_command_output_containment_result_version"],
            "0.1.0",
        )
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_command_output_containment",
        )

        boundary = result["selected_command_output_containment_boundary_basis"]
        self.assertEqual(boundary["outcome"], resolver.COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME)
        self.assertEqual(boundary["failed_check_count"], 0)
        self.assertTrue(boundary["one_future_command_output_containment_step_declared"])
        self.assertTrue(boundary["command_output_not_created"])
        self.assertTrue(boundary["output_capture_not_created"])
        self.assertTrue(boundary["command_output_report_artifact_not_created"])
        self.assertTrue(boundary["command_result_not_created"])
        self.assertTrue(boundary["command_success_not_created"])
        self.assertTrue(boundary["reference_shaped_basis"])

        execution = result["selected_post_invocation_command_execution_basis"]
        self.assertEqual(execution["outcome"], resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME)
        self.assertEqual(execution["failed_check_count"], 0)
        self.assertTrue(execution["bounded_command_execution_event_recorded"])
        self.assertTrue(execution["execution_trace_audit_only"])
        self.assertFalse(execution["command_output_created"])
        self.assertFalse(execution["command_result_created"])
        self.assertFalse(execution["command_success_created"])
        self.assertTrue(execution["execution_trace_is_not_output"])
        self.assertTrue(execution["execution_trace_is_not_result"])
        self.assertTrue(execution["execution_trace_is_not_success"])
        self.assertTrue(execution["execution_trace_is_not_source"])
        self.assertTrue(execution["execution_trace_is_not_authority"])

        terminal = result["selected_post_invocation_command_execution_terminal_summary_basis"]
        self.assertTrue(terminal["terminal_summary_declared"])
        self.assertTrue(terminal["readability_basis_only"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_output"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_result"])
        self.assertTrue(terminal["terminal_summary_does_not_create_command_success"])
        self.assertTrue(terminal["terminal_summary_does_not_authorize_follow_on_work"])

        invocation = result["selected_command_invocation_basis"]
        self.assertEqual(invocation["outcome"], resolver.COMMAND_INVOCATION_OUTCOME)
        self.assertEqual(invocation["failed_check_count"], 0)
        self.assertTrue(invocation["bounded_command_invocation_event_recorded"])
        self.assertTrue(invocation["authorization_token_spent_exactly_once"])
        self.assertTrue(invocation["authorization_token_reuse_blocked"])

        consumption = result["selected_request_consumption_basis"]
        consumed = result["selected_consumed_request_basis"]
        self.assertTrue(consumption["request_consumed_exactly_once"])
        self.assertTrue(consumption["consumption_token_closed"])
        self.assertTrue(consumed["consumed_request_token_remains_closed"])
        self.assertTrue(consumed["consumed_request_is_not_reopened"])

        v2 = result["selected_v2_admitted_request_basis"]
        v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertEqual(v2["outcome"], resolver.V2_ADMITTED_REQUEST_OUTCOME)
        self.assertEqual(v2["result_version"], resolver.V2_ADMITTED_REQUEST_VERSION)
        self.assertTrue(v2["returned_result_containment_preserved"])
        self.assertTrue(v1["v1_remains_visible_predecessor_failure_evidence"])
        self.assertTrue(v1["v1_is_not_repaired"])
        self.assertTrue(v1["v1_is_not_hidden"])
        self.assertTrue(v1["v1_is_not_claimed_passed"])

        older = result["selected_older_command_execution_boundary_lineage_basis"]
        self.assertTrue(older["basis_remains_prior_scaffolding_only"])
        self.assertTrue(older["lineage_basis_not_treated_as_current_execution"])
        self.assertFalse(older["older_command_execution_boundary_lineage_treated_as_current_execution"])
        self.assertFalse(older["command_output_created"])
        self.assertFalse(older["command_result_created"])
        self.assertFalse(older["command_success_created"])

    def test_check_records_nonmeaning_and_open_items(self) -> None:
        result = self._recorded_result()
        checks = result["command_output_containment_checks"]
        passed_count, failed_count = _check_counts(result)

        self.assertEqual(failed_count, 0)
        self.assertGreater(passed_count, 0)
        for check in checks:
            self.assertTrue(check["passed"], check)
            for key in (
                "check_name",
                "passed",
                "expected_posture",
                "actual_posture",
                "block_code",
                "failure_code",
            ):
                self.assertIn(key, check)

        check_names = {check["check_name"] for check in checks}
        expected_checks = {
            "command output containment question declared",
            "command output containment intent supported",
            "command output containment boundary terminal summary basis declared",
            "command output containment boundary live artifact basis declared",
            "command output containment boundary outcome recorded",
            "command output containment boundary failed check count zero",
            "command output containment boundary step declared",
            "command output containment boundary output not created",
            "command output containment boundary output capture not created",
            "command output containment boundary output report artifact not created",
            "command output containment boundary result not created",
            "command output containment boundary success not created",
            "post-invocation command execution basis declared",
            "post-invocation command execution outcome recorded",
            "post-invocation command execution failed check count zero",
            "post-invocation command execution event recorded",
            "post-invocation command execution trace audit-only",
            "command invocation basis declared",
            "command execution review basis declared",
            "request consumption basis declared",
            "consumed request basis declared",
            "v2 admitted request basis declared",
            "v1 predecessor failure basis declared",
            "older command execution boundary lineage basis prior scaffolding only",
            "command report basis declared",
            "command implementation boundary basis declared",
            "command boundary basis declared",
            "artifact emission containment basis declared",
            "evidence-manifest basis declared",
            "portable verification basis declared",
            "output-containment-only posture declared",
            "one-bounded-command-output-containment-event posture declared",
            "command-output-boundary-basis-preserved posture declared",
            "execution-event-preserved posture declared",
            "execution-trace-audit-only posture declared",
            "execution trace not output result success source authority",
            "collapse flags absent",
            "raw full prior artifact body not emitted",
            "non-claims remain false",
        }
        self.assertTrue(expected_checks.issubset(check_names))

        non_meaning = result["command_output_containment_non_meaning"]
        for key in (
            "command_output_exists",
            "output_was_captured",
            "command_output_report_artifact_exists",
            "command_result_exists",
            "command_success_exists",
            "containment_is_output",
            "containment_is_output_capture",
            "containment_is_output_report_artifact",
            "containment_is_result",
            "containment_is_success",
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
            "public_readiness",
            "final_completion",
            "continuation",
            "reusable_permission",
            "derivative_reception",
            "vessel_relation",
            "another_reception_request",
            "follow_on_work",
        ):
            self.assertTrue(
                non_meaning[f"command_output_containment_does_not_mean_{key}"],
                key,
            )
        self.assertTrue(
            non_meaning[
                "command_output_containment_does_not_mean_v1_repaired_hidden_or_passed"
            ]
        )
        self.assertTrue(
            non_meaning[
                "command_output_containment_does_not_mean_deployment_runtime_public_release"
            ]
        )

        open_items = result["what_remains_open"]
        open_item_names = set(open_items["open_items"])
        for key in OPEN_ITEMS:
            self.assertIn(key, open_item_names)
        self.assertTrue(open_items["open_means_not_scheduled"])
        self.assertTrue(open_items["open_means_not_authorized"])
        self.assertTrue(open_items["open_means_not_executed"])

    def test_summary_helper_preserves_key_posture(self) -> None:
        result = self._recorded_result()
        summary = build_portable_source_body_verification_command_output_containment_summary(
            result
        )

        self.assertEqual(summary, result["portable_source_body_verification_command_output_containment_summary"])
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["request_id"], "command-output-containment-request-001")
        self.assertEqual(summary["question"], QUESTION)
        self.assertEqual(summary["intent"], resolver.INTENT_RECORD)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "command_output_containment_recorded",
            "bounded_output_containment_event_recorded",
            "command_output_boundary_basis_preserved",
            "recorded_command_execution_event_preserved",
            "execution_trace_audit_only_preserved",
            "command_output_still_not_created",
            "output_capture_not_created",
            "output_report_artifact_not_created",
            "command_result_still_not_created",
            "command_success_still_not_created",
            "containment_not_output_capture_output_report_result_success",
            "execution_trace_not_output_result_success_source_authority",
            "output_not_source",
            "result_not_authority",
            "success_not_currentness",
            "success_not_final_completion",
            "older_command_execution_boundary_lineage_not_treated_as_current_execution",
            "no_raw_full_prior_artifact_body",
            "no_artifact_mutation",
            "no_deployment_runtime_public_release",
            "no_operation_public_readiness_final_completion",
            "no_continuation_publication_reusable_follow_on",
        ):
            self.assertTrue(summary[key], key)
        self.assertEqual(
            summary["selected_output_containment_boundary_outcome"],
            resolver.COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_OUTCOME,
        )
        self.assertEqual(summary["selected_output_containment_boundary_failed_check_count"], 0)
        self.assertEqual(
            summary["selected_post_invocation_execution_outcome"],
            resolver.POST_INVOCATION_COMMAND_EXECUTION_OUTCOME,
        )
        self.assertEqual(summary["selected_post_invocation_execution_failed_check_count"], 0)
        self.assertEqual(
            summary["selected_v2_admitted_request_outcome"],
            resolver.V2_ADMITTED_REQUEST_OUTCOME,
        )
        self.assertEqual(
            summary["selected_v2_admitted_request_version"],
            resolver.V2_ADMITTED_REQUEST_VERSION,
        )
        self.assertEqual(summary["selected_v2_admitted_request_failed_check_count"], 0)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertFalse(summary["key_non_claims"][key], key)

    def test_request_builder_preserves_inputs_and_records(self) -> None:
        source = _valid_request(
            requested_command_output_containment_outcome=RECORDED,
            additional_basis_context={"unclear_basis": "none"},
            not_recorded_basis={"reason": "not used"},
        )
        built = build_declared_portable_source_body_verification_command_output_containment_request(
            command_output_containment_request_id=source["command_output_containment_request_id"],
            command_output_containment_question=source["command_output_containment_question"],
            command_output_containment_intent=source["command_output_containment_intent"],
            selected_command_output_containment_boundary_basis=source[
                "selected_command_output_containment_boundary_basis"
            ],
            selected_command_output_containment_boundary_terminal_summary_basis=source[
                "selected_command_output_containment_boundary_terminal_summary_basis"
            ],
            selected_post_invocation_command_execution_basis=source[
                "selected_post_invocation_command_execution_basis"
            ],
            selected_post_invocation_command_execution_terminal_summary_basis=source[
                "selected_post_invocation_command_execution_terminal_summary_basis"
            ],
            selected_post_invocation_command_execution_boundary_basis=source[
                "selected_post_invocation_command_execution_boundary_basis"
            ],
            selected_command_invocation_basis=source["selected_command_invocation_basis"],
            selected_command_execution_review_basis=source[
                "selected_command_execution_review_basis"
            ],
            selected_request_consumption_basis=source["selected_request_consumption_basis"],
            selected_consumed_request_basis=source["selected_consumed_request_basis"],
            selected_v2_admitted_request_basis=source["selected_v2_admitted_request_basis"],
            selected_v1_predecessor_failure_basis=source[
                "selected_v1_predecessor_failure_basis"
            ],
            selected_older_command_execution_boundary_lineage_basis=source[
                "selected_older_command_execution_boundary_lineage_basis"
            ],
            selected_command_report_basis=source["selected_command_report_basis"],
            selected_command_implementation_boundary_basis=source[
                "selected_command_implementation_boundary_basis"
            ],
            selected_command_boundary_basis=source["selected_command_boundary_basis"],
            selected_artifact_emission_containment_basis=source[
                "selected_artifact_emission_containment_basis"
            ],
            selected_evidence_manifest_basis=source["selected_evidence_manifest_basis"],
            selected_portable_verification_basis=source["selected_portable_verification_basis"],
            command_output_containment_scope=source["command_output_containment_scope"],
            requested_command_output_containment_outcome=source[
                "requested_command_output_containment_outcome"
            ],
            additional_basis_context=source["additional_basis_context"],
            not_recorded_basis=source["not_recorded_basis"],
            selected_command_output_containment_boundary_result_path=source[
                "selected_command_output_containment_boundary_result_path"
            ],
            selected_post_invocation_command_execution_result_path=source[
                "selected_post_invocation_command_execution_result_path"
            ],
            **{key: source[key] for key in POSTURE_KEYS},
        )

        self.assertEqual(
            built["command_output_containment_request_id"],
            "command-output-containment-request-001",
        )
        self.assertEqual(built["command_output_containment_question"], QUESTION)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(built[key], source[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(built[key], source[key], key)
        self.assertEqual(built["command_output_containment_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(built["additional_basis_context"], {"unclear_basis": "none"})
        self.assertEqual(built["not_recorded_basis"], {"reason": "not used"})
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertFalse(built["declared_non_claims"][key], key)
        for key in (
            "command_output_created",
            "output_capture_created",
            "command_output_report_artifact_created",
            "command_result_created",
            "command_success_created",
            "command_became_authority",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        ):
            self.assertFalse(built["declared_non_claims"][key], key)

        result = self._resolve(built)
        self.assertEqual(result["outcome"], RECORDED)

    def test_path_resolution_and_write_are_bounded_and_additive(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            temp_root = Path(tmpdir)
            request = _valid_request()
            request_path = temp_root / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_command_output_containment_from_path(
                request_path
            )
            mapping_result = self._resolve(request)
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result[
                    "portable_source_body_verification_command_output_containment_metadata"
                ]["declared_command_output_containment_request_path"],
                str(request_path),
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = resolve_portable_source_body_verification_command_output_containment_from_path(
                malformed_path
            )
            self._assert_block(
                malformed_result,
                {
                    "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_UNREADABLE",
                    "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED",
                },
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolve_portable_source_body_verification_command_output_containment_from_path(
                array_path
            )
            self._assert_block(
                array_result,
                "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED",
            )

            missing_result = resolve_portable_source_body_verification_command_output_containment_from_path(
                temp_root / "missing.json"
            )
            self._assert_block(
                missing_result,
                "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_UNREADABLE",
            )

            explicit_output = temp_root / "nested" / "result.json"
            written = write_portable_source_body_verification_command_output_containment_result(
                mapping_result,
                explicit_output,
            )
            self.assertEqual(written, explicit_output)
            self.assertTrue(written.exists())
            written_json = json.loads(written.read_text(encoding="utf-8"))
            for section in TOP_LEVEL_SECTIONS:
                self.assertIn(section, written_json)

            patched_root = temp_root / "command_output_containment_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_OUTPUT_CONTAINMENT_ROOT",
                patched_root,
            ):
                default_written = (
                    write_portable_source_body_verification_command_output_containment_result(
                        mapping_result
                    )
                )
                second_written = (
                    write_portable_source_body_verification_command_output_containment_result(
                        mapping_result
                    )
                )
            self.assertTrue(default_written.exists())
            self.assertTrue(second_written.exists())
            self.assertNotEqual(default_written, second_written)
            self.assertTrue(default_written.is_relative_to(patched_root))
            self.assertTrue(second_written.stem.endswith("_001"))
            self.assertNotIn("command_output_containment_boundary", str(default_written))
            self.assertNotIn("post_invocation_command_execution", str(default_written))
            self.assertNotIn("command_invocation", str(default_written))

    def test_requires_additional_basis_and_not_recorded_are_bounded(self) -> None:
        additional_context = {"missing_basis": "clarify command output containment posture"}
        additional_result = self._resolve(
            _valid_request(
                requested_command_output_containment_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional_result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(
            additional_result["additional_basis_required"]["requires_additional_basis"]
        )
        self.assertEqual(
            additional_result["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional_result["additional_basis_required"]["missing_basis_not_executed"])
        self._assert_no_created_work(additional_result)

        not_recorded_basis = {"reason": "readable containment basis failed review"}
        not_recorded_result = self._resolve(
            _valid_request(
                requested_command_output_containment_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded_result["outcome"], NOT_RECORDED)
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded"])
        self.assertEqual(
            not_recorded_result["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(
            not_recorded_result["not_recorded_basis"][
                "not_recorded_does_not_authorize_next_work"
            ]
        )
        self._assert_no_created_work(not_recorded_result)

    def test_reference_shaped_full_body_is_blocked_and_sanitized(self) -> None:
        request = _valid_request()
        request["selected_command_output_containment_boundary_basis"][
            "full_artifact_body"
        ] = RAW_FULL_BODY_SENTINEL
        result = self._resolve(request)

        self._assert_block(result, "FULL_PRIOR_ARTIFACT_BODY_EMITTED")
        self.assertNotIn(RAW_FULL_BODY_SENTINEL, _json_text(result))
        self._assert_no_created_work(result)

        for flag, code in (
            ("containment_treated_as_output", "CONTAINMENT_TREATED_AS_OUTPUT"),
            ("containment_treated_as_output_capture", "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE"),
            (
                "containment_treated_as_output_report_artifact",
                "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            ("containment_treated_as_result", "CONTAINMENT_TREATED_AS_RESULT"),
            ("containment_treated_as_success", "CONTAINMENT_TREATED_AS_SUCCESS"),
        ):
            overread_request = _valid_request(**{flag: True})
            before = copy.deepcopy(overread_request)
            overread_result = self._resolve(overread_request)
            self._assert_block(overread_result, code)
            self.assertEqual(overread_request, before)

    def test_non_mutation_of_request_and_selected_inputs(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        result_one = self._resolve(request)
        result_two = self._resolve(request)

        self.assertEqual(result_one["outcome"], RECORDED)
        self.assertEqual(result_two["outcome"], RECORDED)
        self.assertEqual(request, original)
        for key in SELECTED_BASIS_KEYS:
            self.assertEqual(request[key], original[key], key)
        for key in POSTURE_KEYS:
            self.assertEqual(request[key], original[key], key)
        self.assertEqual(request["command_output_containment_scope"], original["command_output_containment_scope"])

    def test_missing_and_malformed_request_blocks(self) -> None:
        self._assert_block(
            self._resolve(None),
            "COMMAND_OUTPUT_CONTAINMENT_QUESTION_UNDECLARED",
        )
        self._assert_block(
            self._resolve([]),
            "DECLARED_COMMAND_OUTPUT_CONTAINMENT_REQUEST_MALFORMED",
        )
        self._assert_block(
            self._resolve(
                _valid_request(command_output_containment_intent=resolver.INTENT_BLOCK)
            ),
            "COMMAND_OUTPUT_CONTAINMENT_BLOCKED_BY_REQUEST",
        )
        self._assert_block(
            self._resolve(_valid_request(command_output_containment_intent="UNSUPPORTED")),
            "COMMAND_OUTPUT_CONTAINMENT_INTENT_UNSUPPORTED",
        )
        self._assert_block(
            self._resolve(_valid_request(command_output_containment_question="")),
            "COMMAND_OUTPUT_CONTAINMENT_QUESTION_UNDECLARED",
        )

    def test_boundary_basis_blocking_conditions(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "missing boundary basis",
                lambda request: request.pop("selected_command_output_containment_boundary_basis"),
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_BASIS_MISSING",
            ),
            (
                "boundary not recorded",
                self._boundary_not_recorded,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_NOT_RECORDED",
            ),
            (
                "boundary failed checks",
                self._boundary_failed_checks,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_FAILED_CHECKS_PRESENT",
            ),
            (
                "boundary step not declared",
                self._boundary_step_not_declared,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_STEP_NOT_DECLARED",
            ),
            (
                "boundary created output",
                self._boundary_created_output,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT",
            ),
            (
                "boundary created output capture",
                self._boundary_created_output_capture,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_CAPTURE",
            ),
            (
                "boundary created output report artifact",
                self._boundary_created_output_report_artifact,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_OUTPUT_REPORT_ARTIFACT",
            ),
            (
                "boundary created result",
                self._boundary_created_result,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_RESULT",
            ),
            (
                "boundary created success",
                self._boundary_created_success,
                "COMMAND_OUTPUT_CONTAINMENT_BOUNDARY_ALREADY_CREATED_SUCCESS",
            ),
        )
        for name, mutate, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self._assert_block(self._resolve(request), code)

    @staticmethod
    def _boundary_not_recorded(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"]["outcome"] = "NOT_RECORDED"
        request["selected_command_output_containment_boundary_result_outcome"] = "NOT_RECORDED"

    @staticmethod
    def _boundary_failed_checks(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"]["failed_check_count"] = 1
        request["selected_command_output_containment_boundary_failed_check_count"] = 1

    @staticmethod
    def _boundary_step_not_declared(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "one_future_command_output_containment_step_declared"
        ] = False
        request["selected_command_output_containment_boundary_basis"][
            "one_future_output_containment_step_declared"
        ] = False
        request["selected_command_output_containment_boundary_step_declared"] = False

    @staticmethod
    def _boundary_created_output(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "command_output_created"
        ] = True
        request["selected_command_output_containment_boundary_output_created"] = True

    @staticmethod
    def _boundary_created_output_capture(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "output_capture_created"
        ] = True
        request["selected_command_output_containment_boundary_output_capture_created"] = True

    @staticmethod
    def _boundary_created_output_report_artifact(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "command_output_report_artifact_created"
        ] = True
        request[
            "selected_command_output_containment_boundary_output_report_artifact_created"
        ] = True

    @staticmethod
    def _boundary_created_result(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "command_result_created"
        ] = True
        request["selected_command_output_containment_boundary_result_created"] = True

    @staticmethod
    def _boundary_created_success(request: dict[str, Any]) -> None:
        request["selected_command_output_containment_boundary_basis"][
            "command_success_created"
        ] = True
        request["selected_command_output_containment_boundary_success_created"] = True

    def test_post_invocation_and_prior_basis_blocking_conditions(self) -> None:
        cases: tuple[tuple[str, Callable[[dict[str, Any]], None], str], ...] = (
            (
                "missing post invocation execution basis",
                lambda request: request.pop("selected_post_invocation_command_execution_basis"),
                "POST_INVOCATION_COMMAND_EXECUTION_BASIS_MISSING",
            ),
            (
                "post invocation execution not recorded",
                self._post_invocation_not_recorded,
                "POST_INVOCATION_COMMAND_EXECUTION_NOT_RECORDED",
            ),
            (
                "post invocation execution failed checks",
                self._post_invocation_failed_checks,
                "POST_INVOCATION_COMMAND_EXECUTION_FAILED_CHECKS_PRESENT",
            ),
            (
                "post invocation event not recorded",
                self._remove_execution_event,
                "POST_INVOCATION_COMMAND_EXECUTION_EVENT_NOT_RECORDED",
            ),
            (
                "post invocation trace not audit only",
                self._remove_trace_audit_only,
                "POST_INVOCATION_COMMAND_EXECUTION_TRACE_NOT_AUDIT_ONLY",
            ),
            (
                "missing v2 admitted request basis",
                lambda request: request.pop("selected_v2_admitted_request_basis"),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            (
                "v2 failed checks",
                self._v2_failed_checks,
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "missing v1 predecessor failure basis",
                lambda request: request.pop("selected_v1_predecessor_failure_basis"),
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            (
                "v2 treated as repairing v1",
                lambda request: request["selected_v2_admitted_request_basis"].update(
                    v2_treated_as_repairing_v1=True
                ),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            (
                "v1 failure hidden",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_hidden=True
                ),
                "V1_FAILURE_HIDDEN",
            ),
            (
                "v1 claimed passed",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_claimed_passed=True
                ),
                "V1_CLAIMED_PASSED",
            ),
            (
                "older lineage current execution",
                lambda request: request[
                    "selected_older_command_execution_boundary_lineage_basis"
                ].update(
                    older_command_execution_boundary_lineage_treated_as_current_execution=True
                ),
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
            (
                "missing command report basis",
                lambda request: request.pop("selected_command_report_basis"),
                "COMMAND_REPORT_BASIS_MISSING",
            ),
            (
                "missing command implementation boundary basis",
                lambda request: request.pop("selected_command_implementation_boundary_basis"),
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing command boundary basis",
                lambda request: request.pop("selected_command_boundary_basis"),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing artifact emission containment basis",
                lambda request: request.pop("selected_artifact_emission_containment_basis"),
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            (
                "missing evidence manifest basis",
                lambda request: request.pop("selected_evidence_manifest_basis"),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            (
                "missing portable verification basis",
                lambda request: request.pop("selected_portable_verification_basis"),
                "PORTABLE_VERIFICATION_BASIS_MISSING",
            ),
        )
        for name, mutate, code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                self._assert_block(self._resolve(request), code)

    @staticmethod
    def _post_invocation_not_recorded(request: dict[str, Any]) -> None:
        request["selected_post_invocation_command_execution_basis"]["outcome"] = (
            "NOT_RECORDED"
        )
        request["selected_post_invocation_command_execution_result_outcome"] = (
            "NOT_RECORDED"
        )

    @staticmethod
    def _post_invocation_failed_checks(request: dict[str, Any]) -> None:
        request["selected_post_invocation_command_execution_basis"][
            "failed_check_count"
        ] = 1
        request["selected_post_invocation_command_execution_failed_check_count"] = 1

    @staticmethod
    def _remove_execution_event(request: dict[str, Any]) -> None:
        execution = request["selected_post_invocation_command_execution_basis"]
        for key in (
            "one_bounded_command_execution_event_recorded",
            "bounded_command_execution_event_recorded",
            "execution_event_recorded",
        ):
            execution.pop(key, None)
        request["selected_post_invocation_command_execution_event_recorded"] = False

    @staticmethod
    def _remove_trace_audit_only(request: dict[str, Any]) -> None:
        execution = request["selected_post_invocation_command_execution_basis"]
        for key in (
            "execution_trace_recorded_as_audit_only",
            "execution_trace_audit_only",
            "execution_trace_audit_only_preserved",
        ):
            execution.pop(key, None)
        request["selected_post_invocation_command_execution_trace_audit_only"] = False

    @staticmethod
    def _v2_failed_checks(request: dict[str, Any]) -> None:
        request["selected_v2_admitted_request_basis"]["failed_check_count"] = 1
        request["selected_v2_failed_check_count"] = 1

    def test_required_posture_and_scope_blocks(self) -> None:
        request = _valid_request()
        request.pop("output_containment_only_posture")
        self._assert_block(self._resolve(request), "OUTPUT_CONTAINMENT_ONLY_POSTURE_MISSING")

        request = _valid_request(command_output_containment_scope=["UNSUPPORTED_SCOPE"])
        self._assert_block(self._resolve(request), "UNSUPPORTED_COMMAND_OUTPUT_CONTAINMENT_SCOPE")

        request = _valid_request()
        request["declared_non_claims"].pop("command_output_created")
        self._assert_block(self._resolve(request), "NON_CLAIM_MISSING_OR_FLIPPED")

        request = _valid_request()
        request["declared_non_claims"]["command_output_created"] = True
        self._assert_block(
            self._resolve(request),
            {"COMMAND_OUTPUT_CREATED", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_collapse_flags_block_without_creating_output(self) -> None:
        cases = (
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("output_capture_created", "OUTPUT_CAPTURE_CREATED"),
            (
                "command_output_report_artifact_created",
                "COMMAND_OUTPUT_REPORT_ARTIFACT_CREATED",
            ),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("containment_treated_as_output", "CONTAINMENT_TREATED_AS_OUTPUT"),
            ("containment_treated_as_output_capture", "CONTAINMENT_TREATED_AS_OUTPUT_CAPTURE"),
            (
                "containment_treated_as_output_report_artifact",
                "CONTAINMENT_TREATED_AS_OUTPUT_REPORT_ARTIFACT",
            ),
            ("containment_treated_as_result", "CONTAINMENT_TREATED_AS_RESULT"),
            ("containment_treated_as_success", "CONTAINMENT_TREATED_AS_SUCCESS"),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            (
                "command_success_created_currentness",
                "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            ),
            (
                "command_success_claimed_final_completion",
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            ("authorization_token_reused", "AUTHORIZATION_TOKEN_REUSED"),
            ("consumed_request_reopened", "CONSUMED_REQUEST_REOPENED"),
            (
                "older_command_execution_boundary_lineage_treated_as_current_execution",
                "OLDER_COMMAND_EXECUTION_BOUNDARY_LINEAGE_TREATED_AS_CURRENT_EXECUTION",
            ),
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
            (
                "another_reception_request_authorized",
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            ),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                if flag == "older_command_execution_boundary_lineage_treated_as_current_execution":
                    request["selected_older_command_execution_boundary_lineage_basis"][
                        flag
                    ] = True
                result = self._resolve(request)
                self._assert_block(result, code)

    def test_execution_trace_overread_blocks(self) -> None:
        cases = (
            ("execution_trace_treated_as_output", "EXECUTION_TRACE_TREATED_AS_OUTPUT"),
            ("execution_trace_treated_as_result", "EXECUTION_TRACE_TREATED_AS_RESULT"),
            ("execution_trace_treated_as_success", "EXECUTION_TRACE_TREATED_AS_SUCCESS"),
            ("execution_trace_treated_as_source", "EXECUTION_TRACE_TREATED_AS_SOURCE"),
            ("execution_trace_treated_as_authority", "EXECUTION_TRACE_TREATED_AS_AUTHORITY"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                self._assert_block(self._resolve(request), code)

    def test_mutation_replay_merge_blocks(self) -> None:
        request = _valid_request(
            mutation_performed=True,
            replay_performed=True,
            merge_performed=True,
        )
        self._assert_block(self._resolve(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")


if __name__ == "__main__":
    unittest.main()
