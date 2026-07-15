"""Tests for the admitted single live command invocation request consumption boundary.

This test surface records consumption-boundary behavior only. It does not
consume the admitted request, invoke a command, execute a command, create
command output/result/success, create a standing lane, or create repeat
permission.
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

import resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary as resolver
from resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary import (
    build_declared_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_request,
    build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_summary,
    build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_summary,
    resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary,
    resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_from_path,
    write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_result,
    write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
ADMITTED_REQUEST_OUTCOME = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
V2_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2"
)
V1_RESOLVER_MODULE = (
    "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary"
)
SUCCESSOR_REASON = (
    "v1 returned-result containment flaw: raw full prior artifact body could be echoed into result"
)
QUESTION = (
    "Can the admitted single live command invocation request be bounded for one future "
    "consumption review without consuming the request or creating command invocation, "
    "command execution, command output, command result, command success, standing "
    "invocation lane, repeat invocation permission, source, authority, currentness, "
    "final completion, continuation, reusable permission, derivative reception, vessel "
    "relation, another reception request, or follow-on work?"
)
SENTINEL = "SENTINEL_CONSUMPTION_BOUNDARY_FULL_BODY_SHOULD_NOT_RETURN_" * 6
OMISSION_MARKER = resolver.FULL_BODY_OMISSION_MARKER

SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_CONSUMPTION_BOUNDARY_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "admitted_single_live_command_invocation_request_consumption_metadata",
    "declared_consumption_boundary_question",
    "selected_v2_admitted_request_basis",
    "selected_v2_terminal_summary_basis",
    "selected_v1_predecessor_failure_basis",
    "selected_command_execution_boundary_basis",
    "selected_command_report_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "one_shot_consumption_posture",
    "no_standing_lane_posture",
    "no_repeat_permission_posture",
    "execution_separation_posture",
    "returned_result_containment_posture",
    "consumption_boundary_scope",
    "consumption_boundary_checks",
    "consumption_boundary_statement",
    "consumption_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "admitted_single_live_command_invocation_request_consumption_summary",
}


def _json_text(value: Any) -> str:
    return json.dumps(value, sort_keys=True, ensure_ascii=True)


def _walk(value: Any):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from _walk(child)
    elif isinstance(value, list):
        yield value
        for child in value:
            yield from _walk(child)
    else:
        yield value


def _find_forbidden_key_values(value: Any) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in resolver.FORBIDDEN_FULL_BODY_KEYS:
                found.append(child)
            found.extend(_find_forbidden_key_values(child))
    elif isinstance(value, list):
        for child in value:
            found.extend(_find_forbidden_key_values(child))
    return found


def _assert_no_sentinel(testcase: unittest.TestCase, result: dict[str, Any]) -> None:
    testcase.assertNotIn(SENTINEL, _json_text(result))


def _assert_forbidden_values_sanitized(testcase: unittest.TestCase, result: dict[str, Any]) -> None:
    for value in _find_forbidden_key_values(result):
        testcase.assertNotEqual(SENTINEL, value)
        if isinstance(value, str):
            testcase.assertEqual(OMISSION_MARKER, value)


def _required_false_non_claims() -> dict[str, bool]:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def _selected_v2_admitted_request_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "selected_result_id": "portable_source_body_verification_single_live_command_invocation_request_admission_reference_review_001_v2",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_"
            "single_live_command_invocation_request_admission_boundary_v2/"
            "portable_source_body_verification_single_live_command_invocation_request_admission_"
            "reference_review_001_v2__single_live_command_invocation_request_admission_result_v2.json"
        ),
        "outcome": ADMITTED_REQUEST_OUTCOME,
        "result_version": "0.2.0",
        "failed_check_count": 0,
        "passed_check_count": 48,
        "resolver_module": V2_RESOLVER_MODULE,
        "successor_of": V1_RESOLVER_MODULE,
        "successor_reason": SUCCESSOR_REASON,
        "returned_result_containment_preserved": True,
        "v2_raw_full_prior_artifact_values_omitted": True,
        "admitted_request_basis_remains_admission_evidence_only": True,
        "request_is_not_consumed_here": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "no_standing_invocation_lane": True,
        "no_repeat_invocation_permission": True,
        "no_authority_currentness_final_completion_continuation_follow_on_work": True,
        "selected_basis_is_reference_shaped": True,
        "raw_full_prior_artifact_body_returned": False,
        "full_prior_artifacts_embedded": False,
    }
    basis.update(extra)
    return basis


def _selected_v2_terminal_summary_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "terminal_summary_declared": True,
        "selected_terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_SINGLE_LIVE_COMMAND_INVOCATION_"
            "REQUEST_ADMISSION_BOUNDARY_V2_TERMINAL_SUMMARY_V0.md"
        ),
        "terminal_summary_remains_readability_basis_only": True,
        "terminal_summary_does_not_consume_request": True,
        "terminal_summary_does_not_authorize_execution": True,
        "terminal_summary_does_not_create_output_result_success": True,
        "terminal_summary_does_not_authorize_follow_on_work": True,
    }
    basis.update(extra)
    return basis


def _selected_v1_predecessor_failure_basis(**extra: Any) -> dict[str, Any]:
    basis = {
        "v1_predecessor_failure_basis_declared": True,
        "selected_v1_predecessor_artifact_id": "historical_v1_returned_result_containment_failure",
        "selected_v1_predecessor_outcome": "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW_BLOCKED",
        "v1_remains_visible_predecessor_failure_evidence": True,
        "v1_predecessor_failure_remains_visible": True,
        "v1_is_not_repaired": True,
        "v1_is_not_hidden": True,
        "v1_is_not_claimed_passed": True,
        "v2_successor_does_not_erase_v1": True,
        "predecessor_failure_evidence_is_lineage_evidence_only": True,
    }
    basis.update(extra)
    return basis


def _reference_basis(label: str, **extra: Any) -> dict[str, Any]:
    basis = {
        "basis_label": label,
        "declared": True,
        "basis_remains_reference_shaped": True,
        "basis_is_not_request_consumption": True,
        "basis_is_not_command_invocation": True,
        "basis_is_not_command_execution": True,
        "basis_is_not_command_output_result_success": True,
        "basis_is_not_authority_currentness_final_completion_continuation_follow_on_work": True,
        "request_not_consumed_here": True,
        "command_invocation_not_created": True,
        "command_execution_not_performed": True,
        "command_output_result_success_not_created": True,
        "no_standing_lane_or_repeat_permission": True,
        "no_authority_or_currentness_or_completion": True,
    }
    basis.update(extra)
    return basis


def _posture(label: str, **extra: Any) -> dict[str, Any]:
    posture = {
        "posture_label": label,
        "declared": True,
        "one_shot_consumption_posture_declared": label == "one_shot_consumption",
        "no_standing_invocation_lane_posture_declared": label == "no_standing_lane",
        "no_repeat_invocation_permission_posture_declared": label == "no_repeat_permission",
        "execution_still_requires_separate_review": label == "execution_separation",
        "returned_result_containment_preserved": label == "returned_result_containment",
        "request_is_not_consumed_here": True,
        "no_invocation_execution_output_result_success_created": True,
        "no_raw_full_prior_artifact_body_returned": True,
    }
    posture.update(extra)
    return posture


def _valid_request(**extra: Any) -> dict[str, Any]:
    request = {
        "consumption_boundary_request_id": "admitted_consumption_boundary_reference_review_001",
        "consumption_boundary_question": QUESTION,
        "consumption_boundary_intent": (
            "RECORD_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BOUNDARY"
        ),
        "selected_v2_admitted_request_basis": _selected_v2_admitted_request_basis(),
        "selected_v2_terminal_summary_basis": _selected_v2_terminal_summary_basis(),
        "selected_v1_predecessor_failure_basis": _selected_v1_predecessor_failure_basis(),
        "selected_command_execution_boundary_basis": _reference_basis(
            "command_execution_boundary"
        ),
        "selected_command_report_basis": _reference_basis("command_report"),
        "selected_command_implementation_boundary_basis": _reference_basis(
            "command_implementation_boundary"
        ),
        "selected_command_boundary_basis": _reference_basis("command_boundary"),
        "selected_artifact_emission_containment_basis": _reference_basis(
            "artifact_emission_containment"
        ),
        "selected_evidence_manifest_basis": _reference_basis("evidence_manifest"),
        "selected_portable_verification_basis": _reference_basis("portable_verification"),
        "one_shot_consumption_posture": _posture("one_shot_consumption"),
        "no_standing_lane_posture": _posture("no_standing_lane"),
        "no_repeat_permission_posture": _posture("no_repeat_permission"),
        "execution_separation_posture": _posture("execution_separation"),
        "returned_result_containment_posture": _posture("returned_result_containment"),
        "reference_shaped_input_posture": {
            "declared": True,
            "reference_shaped_basis_required": True,
        },
        "non_authority_posture": {"declared": True, "no_authority_created": True},
        "non_currentness_posture": {"declared": True, "no_currentness_created": True},
        "non_final_completion_posture": {"declared": True, "no_final_completion": True},
        "consumption_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_consumption_boundary_outcome": RECORDED,
        "declared_non_claims": _required_false_non_claims(),
    }
    request.update(extra)
    return request


def _resolve(request: dict[str, Any] | None) -> dict[str, Any]:
    return resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary(
        declared_consumption_boundary_request=request
    )


def _checks(result: dict[str, Any]) -> list[dict[str, Any]]:
    return result["consumption_boundary_checks"]["records"]


def _block_code(result: dict[str, Any]) -> str | None:
    return result["block"]["block_code"]


def _assert_result_shape(testcase: unittest.TestCase, result: dict[str, Any]) -> None:
    testcase.assertIsInstance(result, dict)
    testcase.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
    testcase.assertIn(result["outcome"], OUTCOME_FAMILY)


def _assert_common_non_claims_false(testcase: unittest.TestCase, result: dict[str, Any]) -> None:
    for name in REQUIRED_NON_CLAIMS:
        testcase.assertIn(name, result["non_claims"])
        testcase.assertFalse(result["non_claims"][name], name)


def _assert_no_request_or_command_created(testcase: unittest.TestCase, result: dict[str, Any]) -> None:
    statement = result["consumption_boundary_statement"]
    for name in (
        "request_consumed_here",
        "single_invocation_request_admission_recorded_as_execution",
        "command_invocation_created",
        "command_executed",
        "command_execution_performed",
        "command_output_created",
        "command_result_created",
        "command_success_created",
        "standing_invocation_lane_created",
        "repeat_invocation_permission_created",
        "request_admission_treated_as_execution_permission",
        "request_admission_treated_as_command_success",
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
        testcase.assertIn(name, statement)
        testcase.assertFalse(statement[name], name)


class PortableSourceBodyVerificationAdmittedRequestConsumptionBoundaryTests(
    unittest.TestCase
):
    def test_successful_consumption_boundary_recorded_result(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)

        result = _resolve(request)

        self.assertEqual(original, request)
        _assert_result_shape(self, result)
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["consumption_boundary_checks"]["failed_check_count"])
        self.assertGreater(result["consumption_boundary_checks"]["passed_check_count"], 0)

        statement = result["consumption_boundary_statement"]
        for name in (
            "admitted_single_live_command_invocation_request_consumption_boundary_recorded",
            "selected_v2_admitted_request_basis_preserved",
            "v2_successor_lineage_preserved",
            "v1_predecessor_failure_preserved",
            "single_consumption_review_conditions_declared",
            "one_shot_consumption_posture_declared",
            "execution_requires_separate_review",
            "returned_result_containment_preserved",
            "consumption_boundary_only",
        ):
            self.assertTrue(statement[name], name)

        _assert_no_request_or_command_created(self, result)
        _assert_common_non_claims_false(self, result)
        _assert_no_sentinel(self, result)

    def test_metadata_and_lineage_sections(self) -> None:
        result = _resolve(_valid_request())
        metadata = result[
            "admitted_single_live_command_invocation_request_consumption_metadata"
        ]

        for name in (
            "admitted_single_live_command_invocation_request_consumption_result_id",
            "admitted_single_live_command_invocation_request_consumption_result_type",
            "admitted_single_live_command_invocation_request_consumption_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[name], name)
        self.assertEqual("0.1.0", metadata[
            "admitted_single_live_command_invocation_request_consumption_result_version"
        ])
        self.assertEqual(resolver.RESOLVER_MODULE, metadata["resolver_module"])

        selected_v2 = result["selected_v2_admitted_request_basis"]
        self.assertEqual(
            ADMITTED_REQUEST_OUTCOME,
            selected_v2["selected_v2_admitted_request_outcome"],
        )
        self.assertEqual("0.2.0", selected_v2["selected_v2_admitted_request_version"])
        self.assertEqual(0, selected_v2["selected_v2_failed_check_count"])
        self.assertTrue(selected_v2["selected_v2_successor_metadata_preserved"])
        self.assertTrue(selected_v2["selected_v2_returned_result_containment_preserved"])
        self.assertTrue(
            selected_v2["admitted_request_basis_remains_admission_evidence_only"]
        )
        self.assertTrue(selected_v2["request_is_not_consumed_here"])
        self.assertTrue(selected_v2["selected_basis_is_reference_shaped"])
        self.assertTrue(selected_v2["full_prior_artifact_body_not_emitted"])

        selected_v1 = result["selected_v1_predecessor_failure_basis"]
        self.assertTrue(selected_v1["v1_remains_visible_predecessor_failure_evidence"])
        self.assertTrue(selected_v1["v1_is_not_repaired"])
        self.assertTrue(selected_v1["v1_is_not_hidden"])
        self.assertTrue(selected_v1["v1_is_not_claimed_passed"])
        self.assertTrue(selected_v1["successor_does_not_erase_v1"])

    def test_consumption_checks_are_complete_records(self) -> None:
        result = _resolve(_valid_request())
        records = _checks(result)

        self.assertTrue(records)
        for record in records:
            for name in (
                "check_name",
                "passed",
                "expected_posture",
                "actual_posture",
                "block_code",
                "failure_code",
            ):
                self.assertIn(name, record)
            self.assertTrue(record["passed"], record["check_name"])
        self.assertEqual(0, result["consumption_boundary_checks"]["failed_check_count"])

        names = {record["check_name"] for record in records}
        expected_names = {
            "consumption-boundary question declared",
            "consumption-boundary intent supported",
            "selected v2 admitted request basis declared",
            "v2 admitted request outcome is SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED",
            "v2 admitted request version is 0.2.0",
            "v2 admitted request failed check count zero",
            "v2 successor metadata preserved",
            "v2 returned-result containment preserved",
            "selected v2 terminal summary basis declared",
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
            "one-shot consumption posture declared",
            "no-standing-lane posture declared",
            "no-repeat-permission posture declared",
            "consumption-boundary scope supported",
            "request not consumed here",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "standing invocation lane not created",
            "repeat invocation permission not created",
            "request admission not execution permission",
            "request admission not command success",
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

    def test_consumption_boundary_non_meaning(self) -> None:
        result = _resolve(_valid_request())
        non_meaning = result["consumption_boundary_non_meaning"]

        expected_true = (
            "consumption_boundary_does_not_mean_request_consumed",
            "consumption_boundary_does_not_mean_command_invocation_created",
            "consumption_boundary_does_not_mean_command_executed",
            "consumption_boundary_does_not_mean_command_output_exists",
            "consumption_boundary_does_not_mean_command_result_exists",
            "consumption_boundary_does_not_mean_command_success_exists",
            "consumption_boundary_does_not_mean_command_success_creates_currentness",
            "consumption_boundary_does_not_mean_command_success_claims_final_completion",
            "consumption_boundary_does_not_mean_command_output_becomes_source",
            "consumption_boundary_does_not_mean_command_result_becomes_authority",
            "consumption_boundary_does_not_mean_standing_invocation_lane_exists",
            "consumption_boundary_does_not_mean_repeat_invocation_permission_exists",
            "consumption_boundary_does_not_mean_v1_was_repaired",
            "consumption_boundary_does_not_mean_v1_was_hidden",
            "consumption_boundary_does_not_mean_v1_passed",
            "consumption_boundary_does_not_mean_v2_admission_became_execution_permission",
            "consumption_boundary_does_not_mean_deployment_created",
            "consumption_boundary_does_not_mean_runtime_hosting_created",
            "consumption_boundary_does_not_mean_public_release_created",
            "consumption_boundary_does_not_mean_public_readiness_created",
            "consumption_boundary_does_not_mean_final_completion_claimed",
            "consumption_boundary_does_not_mean_continuation_authorized",
            "consumption_boundary_does_not_mean_reusable_permission_created",
            "consumption_boundary_does_not_mean_derivative_reception_authorized",
            "consumption_boundary_does_not_mean_vessel_relation_authorized",
            "consumption_boundary_does_not_mean_another_reception_request_authorized",
            "consumption_boundary_does_not_mean_follow_on_work_authorized",
        )
        for name in expected_true:
            self.assertTrue(non_meaning[name], name)

    def test_not_recorded_and_requires_additional_basis_are_bounded(self) -> None:
        additional_context = {
            "missing_basis": "selected v2 successor metadata unclear",
            "missing_basis_not_scheduled": True,
        }
        additional_request = _valid_request(
            requested_consumption_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
            additional_basis_context=additional_context,
        )
        additional_result = _resolve(additional_request)
        self.assertEqual(REQUIRES_ADDITIONAL_BASIS, additional_result["outcome"])
        self.assertTrue(
            additional_result["additional_basis_required"]["additional_basis_required"]
        )
        self.assertIn(
            "selected v2 successor metadata unclear",
            _json_text(additional_result["additional_basis_required"]),
        )
        self.assertTrue(
            additional_result["additional_basis_required"][
                "missing_basis_not_scheduled_authorized_or_executed"
            ]
        )
        _assert_no_request_or_command_created(self, additional_result)
        _assert_common_non_claims_false(self, additional_result)

        not_recorded_basis = {
            "reason": "selected v2 basis cannot be separated from execution permission",
            "not_recorded_does_not_authorize_repair_or_next_work": True,
        }
        not_recorded_request = _valid_request(
            requested_consumption_boundary_outcome=NOT_RECORDED,
            not_recorded_basis=not_recorded_basis,
        )
        not_recorded_result = _resolve(not_recorded_request)
        self.assertEqual(NOT_RECORDED, not_recorded_result["outcome"])
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded"])
        self.assertIn(
            "selected v2 basis cannot be separated from execution permission",
            _json_text(not_recorded_result["not_recorded_basis"]),
        )
        self.assertTrue(not_recorded_result["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(
            not_recorded_result["not_recorded_basis"][
                "not_recorded_does_not_authorize_follow_on_work"
            ]
        )
        _assert_no_request_or_command_created(self, not_recorded_result)
        _assert_common_non_claims_false(self, not_recorded_result)

    def test_what_remains_open(self) -> None:
        result = _resolve(_valid_request())
        remains_open = result["what_remains_open"]
        open_items = set(remains_open["open_items"])

        expected_open = {
            "admitted request consumption boundary test",
            "admitted request consumption boundary live artifact",
            "actual request consumption",
            "actual command invocation",
            "command execution review",
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
        self.assertTrue(expected_open.issubset(open_items))
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_summary_helpers_preserve_boundary_posture(self) -> None:
        result = _resolve(_valid_request())
        boundary_summary = (
            build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_summary(
                result
            )
        )
        alias_summary = (
            build_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_summary(
                result
            )
        )
        self.assertEqual(boundary_summary, alias_summary)

        expected_values = {
            "outcome": RECORDED,
            "block_code": None,
            "block_reason": None,
            "consumption_boundary_request_id": (
                "admitted_consumption_boundary_reference_review_001"
            ),
            "consumption_boundary_question": QUESTION,
            "consumption_boundary_intent": (
                "RECORD_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BOUNDARY"
            ),
            "failed_check_count": 0,
            "consumption_boundary_recorded": True,
            "selected_v2_admitted_request_basis_preserved": True,
            "v2_successor_lineage_preserved": True,
            "v1_predecessor_failure_preserved": True,
            "single_consumption_review_conditions_declared": True,
            "one_shot_consumption_posture_declared": True,
            "execution_requires_separate_review": True,
            "returned_result_containment_preserved": True,
            "not_recorded": False,
            "requires_additional_basis": False,
            "selected_v2_admitted_request_outcome": ADMITTED_REQUEST_OUTCOME,
            "selected_v2_admitted_request_version": "0.2.0",
            "selected_v2_failed_check_count": 0,
            "request_not_consumed_here": True,
            "command_invocation_not_created": True,
            "command_execution_not_performed": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "no_standing_lane": True,
            "no_repeat_permission": True,
            "request_admission_not_execution_permission": True,
            "request_admission_not_command_success": True,
            "v1_not_repaired": True,
            "v1_not_hidden": True,
            "v1_not_claimed_passed": True,
            "no_raw_full_prior_artifact_body_returned": True,
            "no_artifact_mutation": True,
            "no_deployment_runtime_public_release": True,
            "no_operation_permission_public_readiness_final_completion": True,
            "no_continuation_publication_flow_reusable_permission": True,
            "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work": True,
        }
        for name, expected in expected_values.items():
            self.assertEqual(expected, boundary_summary[name], name)
        self.assertGreater(boundary_summary["passed_check_count"], 0)
        for name in REQUIRED_NON_CLAIMS:
            self.assertFalse(boundary_summary["key_non_claims"][name], name)

    def test_request_builder_helper_builds_resolvable_request(self) -> None:
        additional_context = {"missing_basis": "none for valid request"}
        not_recorded_basis = {"reason": "none for valid request"}
        request = (
            build_declared_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_request(
                consumption_boundary_request_id="builder_consumption_review_001",
                consumption_boundary_question=QUESTION,
                selected_v2_admitted_request_basis=_selected_v2_admitted_request_basis(),
                selected_v2_terminal_summary_basis=_selected_v2_terminal_summary_basis(),
                selected_v1_predecessor_failure_basis=_selected_v1_predecessor_failure_basis(),
                selected_command_execution_boundary_basis=_reference_basis(
                    "command_execution_boundary"
                ),
                selected_command_report_basis=_reference_basis("command_report"),
                selected_command_implementation_boundary_basis=_reference_basis(
                    "command_implementation_boundary"
                ),
                selected_command_boundary_basis=_reference_basis("command_boundary"),
                selected_artifact_emission_containment_basis=_reference_basis(
                    "artifact_emission_containment"
                ),
                selected_evidence_manifest_basis=_reference_basis("evidence_manifest"),
                selected_portable_verification_basis=_reference_basis(
                    "portable_verification"
                ),
                one_shot_consumption_posture=_posture("one_shot_consumption"),
                no_standing_lane_posture=_posture("no_standing_lane"),
                no_repeat_permission_posture=_posture("no_repeat_permission"),
                execution_separation_posture=_posture("execution_separation"),
                returned_result_containment_posture=_posture(
                    "returned_result_containment"
                ),
                consumption_boundary_scope=SUPPORTED_SCOPE,
                selected_v2_admitted_request_artifact_path="artifacts/synthetic/v2_admission.json",
                selected_v2_admitted_request_artifact_id="builder_v2_admission",
                selected_v2_admitted_request_outcome=ADMITTED_REQUEST_OUTCOME,
                selected_v2_admitted_request_version="0.2.0",
                selected_v2_failed_check_count=0,
                requested_consumption_boundary_outcome=RECORDED,
                additional_basis_context=additional_context,
                not_recorded_basis=not_recorded_basis,
            )
        )

        self.assertEqual("builder_consumption_review_001", request["consumption_boundary_request_id"])
        self.assertEqual(QUESTION, request["consumption_boundary_question"])
        for key in (
            "selected_v2_admitted_request_basis",
            "selected_v2_terminal_summary_basis",
            "selected_v1_predecessor_failure_basis",
            "selected_command_execution_boundary_basis",
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "one_shot_consumption_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "execution_separation_posture",
            "returned_result_containment_posture",
        ):
            self.assertIn(key, request)
        self.assertEqual(SUPPORTED_SCOPE, tuple(request["consumption_boundary_scope"]))
        self.assertEqual("artifacts/synthetic/v2_admission.json", request[
            "selected_v2_admitted_request_artifact_path"
        ])
        self.assertEqual("builder_v2_admission", request[
            "selected_v2_admitted_request_artifact_id"
        ])
        self.assertEqual(ADMITTED_REQUEST_OUTCOME, request[
            "selected_v2_admitted_request_outcome"
        ])
        self.assertEqual("0.2.0", request["selected_v2_admitted_request_version"])
        self.assertEqual(0, request["selected_v2_failed_check_count"])
        self.assertEqual(additional_context, request["additional_basis_context"])
        self.assertEqual(not_recorded_basis, request["not_recorded_basis"])
        for name in REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][name], name)

        result = _resolve(request)
        self.assertEqual(RECORDED, result["outcome"])
        _assert_no_request_or_command_created(self, result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = _valid_request()
        mapping_result = _resolve(request)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            request_path = temp_root / "input" / "declared_consumption_request.json"
            request_path.parent.mkdir(parents=True)
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = (
                resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_from_path(
                    request_path
                )
            )
            self.assertEqual(RECORDED, path_result["outcome"])
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                str(request_path),
                path_result["declared_consumption_boundary_question"][
                    "declared_consumption_boundary_request_path"
                ],
            )

            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed_result = (
                resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_from_path(
                    malformed_path
                )
            )
            self.assertEqual(BLOCKED, malformed_result["outcome"])
            self.assertEqual(
                "DECLARED_CONSUMPTION_BOUNDARY_REQUEST_MALFORMED",
                _block_code(malformed_result),
            )

            array_path = temp_root / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = (
                resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_from_path(
                    array_path
                )
            )
            self.assertEqual(BLOCKED, array_result["outcome"])
            self.assertEqual(
                "DECLARED_CONSUMPTION_BOUNDARY_REQUEST_MALFORMED",
                _block_code(array_result),
            )

            missing_result = (
                resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_from_path(
                    temp_root / "missing.json"
                )
            )
            self.assertEqual(BLOCKED, missing_result["outcome"])
            self.assertEqual(
                "DECLARED_CONSUMPTION_BOUNDARY_REQUEST_UNREADABLE",
                _block_code(missing_result),
            )

            explicit_output = temp_root / "out" / "result.json"
            written = (
                write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_result(
                    mapping_result,
                    explicit_output,
                )
            )
            self.assertTrue(written.exists())
            loaded = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded))

            collision = (
                write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_result(
                    mapping_result,
                    explicit_output,
                )
            )
            self.assertTrue(collision.exists())
            self.assertNotEqual(written, collision)

            alias_collision = (
                write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_result(
                    mapping_result,
                    explicit_output,
                )
            )
            self.assertTrue(alias_collision.exists())
            self.assertNotEqual(collision, alias_collision)

            default_root = temp_root / "bounded_consumption_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BOUNDARY_ROOT",
                default_root,
            ):
                default_written = (
                    write_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary_result(
                        mapping_result
                    )
                )
            self.assertTrue(default_written.exists())
            self.assertTrue(default_written.is_relative_to(default_root))
            default_text = str(default_written)
            self.assertNotIn("command_execution_boundary", default_text)
            self.assertNotIn("command_implementation_boundary", default_text)
            self.assertNotIn("command_boundary/", default_text)
            self.assertNotIn("artifact_emission_containment_boundary", default_text)
            self.assertNotIn("deployment", default_text)
            self.assertNotIn("runtime", default_text)
            self.assertNotIn("public_release", default_text)

    def test_reference_shaped_containment_blocks_and_sanitizes_raw_full_body(self) -> None:
        v2_request = _valid_request()
        v2_request["selected_v2_admitted_request_basis"]["full_artifact_body"] = SENTINEL
        v2_result = _resolve(v2_request)
        self.assertEqual(BLOCKED, v2_result["outcome"])
        self.assertEqual("V2_RAW_FULL_PRIOR_ARTIFACT_BODY_RETURNED", _block_code(v2_result))
        _assert_no_sentinel(self, v2_result)
        _assert_forbidden_values_sanitized(self, v2_result)
        _assert_no_request_or_command_created(self, v2_result)

        non_v2_request = _valid_request()
        non_v2_request["selected_command_report_basis"]["full_artifact_body"] = SENTINEL
        non_v2_original = copy.deepcopy(non_v2_request)
        non_v2_result = _resolve(non_v2_request)
        self.assertEqual(non_v2_original, non_v2_request)
        self.assertEqual(BLOCKED, non_v2_result["outcome"])
        self.assertEqual("FULL_PRIOR_ARTIFACT_BODY_EMITTED", _block_code(non_v2_result))
        _assert_no_sentinel(self, non_v2_result)
        _assert_forbidden_values_sanitized(self, non_v2_result)
        _assert_no_request_or_command_created(self, non_v2_result)

    def test_resolver_does_not_mutate_declared_inputs(self) -> None:
        request = _valid_request()
        original = copy.deepcopy(request)
        first = _resolve(request)
        second = _resolve(request)

        self.assertEqual(original, request)
        self.assertEqual(RECORDED, first["outcome"])
        self.assertEqual(RECORDED, second["outcome"])
        for key in (
            "selected_v2_admitted_request_basis",
            "selected_v2_terminal_summary_basis",
            "selected_v1_predecessor_failure_basis",
            "selected_command_execution_boundary_basis",
            "selected_command_report_basis",
            "selected_command_implementation_boundary_basis",
            "selected_command_boundary_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "one_shot_consumption_posture",
            "no_standing_lane_posture",
            "no_repeat_permission_posture",
            "execution_separation_posture",
            "returned_result_containment_posture",
            "consumption_boundary_scope",
        ):
            self.assertEqual(original[key], request[key], key)

    def test_blocking_basis_and_scope_conditions(self) -> None:
        direct_missing = resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary()
        self.assertEqual(BLOCKED, direct_missing["outcome"])
        self.assertEqual("CONSUMPTION_BOUNDARY_QUESTION_UNDECLARED", _block_code(direct_missing))

        non_mapping = resolve_portable_source_body_verification_admitted_single_live_command_invocation_request_consumption_boundary(
            declared_consumption_boundary_request=["not", "a", "mapping"]  # type: ignore[arg-type]
        )
        self.assertEqual(BLOCKED, non_mapping["outcome"])
        self.assertEqual(
            "DECLARED_CONSUMPTION_BOUNDARY_REQUEST_MALFORMED",
            _block_code(non_mapping),
        )

        cases = [
            (
                "explicit block intent",
                lambda request: request.update(
                    consumption_boundary_intent=(
                        "BLOCK_ADMITTED_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_CONSUMPTION_BOUNDARY_REVIEW"
                    )
                ),
                "CONSUMPTION_BOUNDARY_REVIEW_EXPLICITLY_BLOCKED",
            ),
            (
                "missing selected v2 basis",
                lambda request: request.pop("selected_v2_admitted_request_basis"),
                "V2_ADMITTED_REQUEST_BASIS_MISSING",
            ),
            (
                "v2 outcome not admitted",
                lambda request: request["selected_v2_admitted_request_basis"].update(
                    outcome="SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_NOT_ADMITTED"
                ),
                "V2_ADMITTED_REQUEST_NOT_ADMITTED",
            ),
            (
                "v2 version wrong",
                lambda request: request["selected_v2_admitted_request_basis"].update(
                    result_version="0.1.0"
                ),
                "V2_ADMITTED_REQUEST_VERSION_NOT_0_2_0",
            ),
            (
                "v2 failed checks",
                lambda request: request["selected_v2_admitted_request_basis"].update(
                    failed_check_count=1
                ),
                "V2_ADMITTED_REQUEST_FAILED_CHECKS_PRESENT",
            ),
            (
                "missing v2 successor metadata",
                lambda request: [
                    request["selected_v2_admitted_request_basis"].pop("successor_of"),
                    request["selected_v2_admitted_request_basis"].pop("successor_reason"),
                ],
                "V2_SUCCESSOR_METADATA_MISSING",
            ),
            (
                "missing v2 containment",
                lambda request: [
                    request["selected_v2_admitted_request_basis"].pop(
                        "returned_result_containment_preserved"
                    ),
                    request["selected_v2_admitted_request_basis"].pop(
                        "v2_raw_full_prior_artifact_values_omitted"
                    ),
                    request["returned_result_containment_posture"].update(
                        returned_result_containment_preserved=False
                    ),
                ],
                "V2_RETURNED_RESULT_CONTAINMENT_MISSING",
            ),
            (
                "missing v2 terminal summary",
                lambda request: request.pop("selected_v2_terminal_summary_basis"),
                "V2_TERMINAL_SUMMARY_BASIS_MISSING",
            ),
            (
                "missing v1 predecessor",
                lambda request: request.pop("selected_v1_predecessor_failure_basis"),
                "V1_PREDECESSOR_FAILURE_BASIS_MISSING",
            ),
            (
                "v2 treated as repairing v1",
                lambda request: request["selected_v1_predecessor_failure_basis"].update(
                    v1_repaired=True
                ),
                "V2_TREATED_AS_REPAIRING_V1",
            ),
            (
                "v1 hidden",
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
                "missing command execution boundary",
                lambda request: request.pop("selected_command_execution_boundary_basis"),
                "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing command report",
                lambda request: request.pop("selected_command_report_basis"),
                "COMMAND_REPORT_BASIS_MISSING",
            ),
            (
                "missing command implementation boundary",
                lambda request: request.pop(
                    "selected_command_implementation_boundary_basis"
                ),
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing command boundary",
                lambda request: request.pop("selected_command_boundary_basis"),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            (
                "missing artifact containment",
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
                "missing one-shot posture",
                lambda request: request.pop("one_shot_consumption_posture"),
                "ONE_SHOT_CONSUMPTION_POSTURE_MISSING",
            ),
            (
                "missing no-standing posture",
                lambda request: request.pop("no_standing_lane_posture"),
                "NO_STANDING_LANE_POSTURE_MISSING",
            ),
            (
                "missing no-repeat posture",
                lambda request: request.pop("no_repeat_permission_posture"),
                "NO_REPEAT_PERMISSION_POSTURE_MISSING",
            ),
            (
                "unsupported scope",
                lambda request: request["consumption_boundary_scope"].append(
                    "UNSUPPORTED_SCOPE"
                ),
                "UNSUPPORTED_CONSUMPTION_BOUNDARY_SCOPE",
            ),
        ]

        for name, mutate, expected_code in cases:
            with self.subTest(name=name):
                request = _valid_request()
                mutate(request)
                result = _resolve(request)
                self.assertEqual(BLOCKED, result["outcome"])
                self.assertEqual(expected_code, _block_code(result))
                _assert_no_request_or_command_created(self, result)

    def test_blocking_collapse_flags(self) -> None:
        collapse_cases = [
            ("request_consumed_here", "REQUEST_CONSUMED_HERE"),
            (
                "single_invocation_request_admission_recorded_as_execution",
                "REQUEST_ADMISSION_TREATED_AS_EXECUTION_PERMISSION",
            ),
            ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
            ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_execution_performed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
            ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
            (
                "request_admission_treated_as_execution_permission",
                "REQUEST_ADMISSION_TREATED_AS_EXECUTION_PERMISSION",
            ),
            (
                "request_admission_treated_as_command_success",
                "REQUEST_ADMISSION_TREATED_AS_COMMAND_SUCCESS",
            ),
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
            (
                "another_reception_request_authorized",
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED",
            ),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ]

        for flag, expected_code in collapse_cases:
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                result = _resolve(request)
                self.assertEqual(BLOCKED, result["outcome"])
                self.assertEqual(expected_code, _block_code(result))
                _assert_no_request_or_command_created(self, result)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = _valid_request(**{flag: True})
                result = _resolve(request)
                self.assertEqual(BLOCKED, result["outcome"])
                self.assertEqual("MUTATION_REPLAY_OR_MERGE_DETECTED", _block_code(result))

        missing_non_claim_request = _valid_request()
        missing_non_claim_request["declared_non_claims"].pop("request_consumed_here")
        missing_result = _resolve(missing_non_claim_request)
        self.assertEqual(BLOCKED, missing_result["outcome"])
        self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", _block_code(missing_result))

        flipped_non_claim_request = _valid_request()
        flipped_non_claim_request["declared_non_claims"]["command_invocation_created"] = True
        flipped_result = _resolve(flipped_non_claim_request)
        self.assertEqual(BLOCKED, flipped_result["outcome"])
        self.assertIn(
            _block_code(flipped_result),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "COMMAND_INVOCATION_CREATED"},
        )


if __name__ == "__main__":
    unittest.main()
