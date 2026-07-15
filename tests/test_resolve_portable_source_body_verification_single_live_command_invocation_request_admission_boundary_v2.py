"""Bounded v2 successor tests for single live command invocation admission.

These tests prove that v2 preserves the v1 request/admission boundary while
correcting returned-result containment. V2 must detect forbidden full prior
artifact bodies, omit raw values from every emitted result fragment, and keep
request/admission distinct from invocation, execution, output, result, success,
standing invocation lane, repeat permission, deployment, runtime hosting,
public release, final completion, continuation, reusable permission, derivative
reception, vessel relation, another reception request, and follow-on work.
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

import resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2 as resolver  # noqa: E402
from resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2 import (  # noqa: E402
    build_portable_source_body_verification_single_live_command_invocation_request_admission_summary_v2,
    resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2,
    resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2_from_path,
    write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2,
)


ADMITTED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMITTED"
NOT_ADMITTED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_NOT_ADMITTED"
REQUIRES_ADDITIONAL_BASIS = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
BLOCKED = "SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW_BLOCKED"
FULL_BODY_BLOCK = "FULL_PRIOR_ARTIFACTS_EMBEDDED"
OMISSION_MARKER = (
    "[OMITTED: full prior artifact body blocked by single live command invocation "
    "request/admission boundary v2]"
)
SENTINEL = "SENTINEL_FULL_ARTIFACT_BODY_SHOULD_NEVER_RETURN_" * 8
V1_RESOLVER_PATH = (
    SRC_ROOT
    / "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary.py"
)
V2_RESOLVER_PATH = (
    SRC_ROOT
    / "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2.py"
)

FORBIDDEN_KEYS = (
    "full_artifact_body",
    "raw_artifact",
    "raw_result",
    "embedded_artifact",
    "selected_full_artifact",
    "complete_artifact_body",
)
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_REQUEST_ADMISSION_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)

QUESTION = (
    "Can one future live command invocation request be admitted for later "
    "execution without invoking, executing, creating command output, creating "
    "command result, creating command success, creating a standing invocation "
    "lane, creating repeat invocation permission, or authorizing follow-on work?"
)

TOP_LEVEL_SECTIONS = {
    "single_live_command_invocation_request_admission_metadata",
    "declared_invocation_request_admission_question",
    "selected_command_execution_boundary_basis",
    "selected_command_report_basis",
    "selected_command_implementation_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "proposed_one_shot_invocation_mode",
    "proposed_invocation_surface",
    "proposed_input_reference_bundle",
    "proposed_output_report_destination",
    "single_invocation_scope",
    "no_repeat_posture",
    "no_standing_invocation_lane_posture",
    "refusal_conditions",
    "output_limits",
    "result_limits",
    "success_limits",
    "request_admission_scope",
    "request_admission_checks",
    "request_admission_statement",
    "request_admission_non_meaning",
    "additional_basis_required",
    "not_admitted_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "single_live_command_invocation_request_admission_summary",
}


def _json_text(value: object) -> str:
    return json.dumps(value, sort_keys=True)


def _walk(value: object):
    yield value
    if isinstance(value, dict):
        for nested in value.values():
            yield from _walk(nested)
    elif isinstance(value, list):
        for nested in value:
            yield from _walk(nested)


def _find_forbidden_key_values(value: object) -> list[tuple[str, object]]:
    found: list[tuple[str, object]] = []
    if isinstance(value, dict):
        for key, nested in value.items():
            if key in FORBIDDEN_KEYS:
                found.append((key, nested))
            found.extend(_find_forbidden_key_values(nested))
    elif isinstance(value, list):
        for nested in value:
            found.extend(_find_forbidden_key_values(nested))
    return found


def _assert_no_sentinel(testcase: unittest.TestCase, result: object) -> None:
    testcase.assertNotIn(SENTINEL, _json_text(result))
    for item in _walk(result):
        if isinstance(item, str):
            testcase.assertNotIn(SENTINEL, item)


def _assert_forbidden_keys_sanitized(testcase: unittest.TestCase, result: object) -> None:
    for key, value in _find_forbidden_key_values(result):
        testcase.assertEqual(value, OMISSION_MARKER, key)


def _assert_no_command_or_follow_on_created(testcase: unittest.TestCase, result: dict) -> None:
    statement = result["request_admission_statement"]
    for key in (
        "command_invocation_not_created",
        "command_execution_not_performed",
        "command_output_not_created",
        "command_result_not_created",
        "command_success_not_created",
        "no_standing_invocation_lane_created",
        "no_repeat_invocation_permission_created",
        "invocation_requires_separate_execution_step",
        "invocation_must_use_reference_shaped_input",
        "invocation_must_not_mutate_artifacts",
        "invocation_must_not_embed_full_prior_artifacts",
    ):
        testcase.assertTrue(statement[key], key)
    _assert_common_non_claims_false(testcase, result)


def _assert_common_non_claims_false(testcase: unittest.TestCase, result: dict) -> None:
    for key in REQUIRED_NON_CLAIMS:
        testcase.assertIs(result["non_claims"][key], False, key)
        testcase.assertIs(result["request_admission_statement"][key], False, key)


def _assert_no_leakage(testcase: unittest.TestCase, result: object) -> None:
    _assert_no_sentinel(testcase, result)
    _assert_forbidden_keys_sanitized(testcase, result)


def _required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def _selected_result_reference(result_id: str, outcome: str, family: str, summary: dict) -> dict:
    return {
        "selected_result_id": result_id,
        "selected_result_path": f"artifacts/{family}/{result_id}.json",
        "selected_result_outcome": outcome,
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 12,
        "selected_result_summary": copy.deepcopy(summary),
        "selected_result_non_claims": _required_false_non_claims(),
        "selected_result_basis_reference": f"{family}:{result_id}",
        "selected_result_artifact_family": family,
        "selected_result_artifact_size_class": "bounded-kb-reference",
        "reference_shaped_basis_only": True,
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
    }


def _selected_command_execution_boundary_basis() -> dict:
    return _selected_result_reference(
        "portable_source_body_verification_command_execution_boundary_reference_review_001",
        "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_RECORDED",
        "portable_source_body_verification_command_execution_boundary",
        {
            "execution_boundary_recorded": True,
            "command_execution_conditions_declared": True,
            "command_invocation_must_be_bounded": True,
            "command_output_must_be_non_authoritative": True,
            "command_success_must_not_create_currentness": True,
            "command_success_must_not_claim_final_completion": True,
            "command_executed": False,
            "command_invocation_created": False,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "basis_is_reference_shaped": True,
        },
    )


def _selected_command_report_basis() -> dict:
    basis = _selected_result_reference(
        "portable_source_body_verification_command_report_reference_review_001_corrected",
        "PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT",
        "portable_source_body_verification_command_report",
        {
            "corrected_report_artifact_selected": True,
            "report_remains_non_authoritative": True,
            "report_built_status_is_not_command_success": True,
            "command_execution_not_authorized": True,
            "command_invocation_not_created": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "basis_is_reference_shaped": True,
        },
    )
    basis["selected_result_status"] = "PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT"
    return basis


def _selected_command_implementation_basis() -> dict:
    return {
        "command_implementation_spec_declared": True,
        "command_module_reference_declared": True,
        "command_module_path": "src/portable_source_body_verification_command.py",
        "implementation_remains_report_building_module_only": True,
        "implementation_did_not_authorize_execution": True,
        "no_implementation_file_may_be_treated_as_permission_to_run": True,
        "reference_shaped_basis_only": True,
        "full_prior_artifacts_embedded": False,
    }


def _selected_artifact_emission_containment_basis() -> dict:
    return _selected_result_reference(
        "artifact_emission_containment_reference_review_001",
        "ARTIFACT_EMISSION_CONTAINMENT_RECORDED",
        "artifact_emission_containment_boundary",
        {
            "reference_only_selected_basis_required": True,
            "recursive_full_artifact_embedding_blocked": True,
            "prior_artifacts_preserved_by_reference": True,
            "artifacts_not_mutated": True,
        },
    )


def _selected_evidence_manifest_basis() -> dict:
    return _selected_result_reference(
        "portable_source_body_verification_evidence_manifest_reference_review_001",
        "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED",
        "portable_source_body_verification_evidence_manifest_boundary",
        {
            "evidence_manifest_basis_declared": True,
            "evidence_only": True,
            "does_not_authorize_command_invocation_or_execution": True,
        },
    )


def _selected_portable_verification_basis() -> dict:
    return _selected_result_reference(
        "portable_source_body_verification_reference_review_001",
        "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        "portable_source_body_verification_boundary",
        {
            "portable_verification_recorded": True,
            "verification_only": True,
            "does_not_authorize_command_invocation_or_execution": True,
        },
    )


def _clean_request(extra: dict | None = None) -> dict:
    request = {
        "invocation_request_admission_id": "single_live_command_invocation_request_admission_v2_001",
        "invocation_request_admission_question": QUESTION,
        "invocation_request_admission_intent": "ADMIT_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST",
        "selected_command_execution_boundary_basis": _selected_command_execution_boundary_basis(),
        "selected_command_report_basis": _selected_command_report_basis(),
        "selected_command_implementation_basis": _selected_command_implementation_basis(),
        "selected_command_module_reference": {
            "command_module_reference_declared": True,
            "module_path": "src/portable_source_body_verification_command.py",
            "module_reference_is_reference_only": True,
            "module_reference_does_not_authorize_invocation": True,
            "module_reference_does_not_authorize_execution": True,
        },
        "selected_test_surface_reference": {
            "test_surface_reference_declared": True,
            "path": "tests/test_portable_source_body_verification_command.py",
            "test_surface_reference_is_reference_only": True,
            "test_pass_does_not_authorize_invocation": True,
            "test_pass_does_not_authorize_execution": True,
        },
        "selected_artifact_emission_containment_basis": _selected_artifact_emission_containment_basis(),
        "selected_evidence_manifest_basis": _selected_evidence_manifest_basis(),
        "selected_portable_verification_basis": _selected_portable_verification_basis(),
        "proposed_one_shot_invocation_mode": {
            "one_shot_invocation_mode_declared": True,
            "one_bounded_invocation_candidate_only": True,
            "proposed_mode_is_future_only": True,
            "proposal_is_not_invocation": True,
            "proposal_is_not_execution": True,
        },
        "proposed_invocation_surface": {
            "proposed_invocation_surface_declared": True,
            "future_explicit_local_function_invocation_if_separately_authorized": True,
            "proposal_is_not_invocation": True,
            "proposal_does_not_authorize_execution": True,
        },
        "proposed_input_reference_bundle": {
            "proposed_input_reference_bundle_declared": True,
            "reference_shaped_input_required": True,
            "full_prior_artifacts_embedded": False,
            "input_bundle_does_not_create_authority_currentness": True,
        },
        "proposed_output_report_destination": {
            "proposed_output_report_destination_declared": True,
            "future_bounded_additive_execution_report_destination_if_separately_authorized": True,
            "destination_is_future_only": True,
            "destination_does_not_create_output_result_success_here": True,
        },
        "single_invocation_scope": {
            "single_invocation_scope_declared": True,
            "one_shot_invocation_request_only": True,
            "one_invocation_candidate_only": True,
            "no_standing_invocation_lane": True,
            "no_repeat_permission": True,
        },
        "no_repeat_posture": {
            "no_repeat_posture_declared": True,
            "repeat_invocation_permission_created": False,
            "reusable_permission_created": False,
        },
        "no_standing_invocation_lane_posture": {
            "no_standing_invocation_lane_posture_declared": True,
            "standing_invocation_lane_created": False,
            "no_general_invocation_lane_created": True,
        },
        "refusal_conditions": {
            "refusal_conditions_declared": True,
            "refuse_if_full_artifact_bodies_required": True,
            "refuse_if_artifact_mutation_required": True,
            "refuse_if_invocation_would_create_authority_currentness_final_completion": True,
            "refuse_if_repeat_permission_requested": True,
            "refuse_if_standing_lane_requested": True,
        },
        "output_limits": {
            "output_limits_declared": True,
            "command_output_not_created": True,
            "command_output_must_be_non_source": True,
        },
        "result_limits": {
            "result_limits_declared": True,
            "command_result_not_created": True,
            "command_result_must_be_non_authority": True,
        },
        "success_limits": {
            "success_limits_declared": True,
            "command_success_not_created": True,
            "command_success_must_not_create_currentness": True,
            "command_success_must_not_claim_final_completion": True,
        },
        "non_authority_posture": {
            "non_authority_posture_declared": True,
            "output_must_remain_non_source": True,
            "result_must_remain_non_authority": True,
        },
        "non_currentness_posture": {
            "non_currentness_posture_declared": True,
            "success_must_not_create_currentness": True,
        },
        "non_final_completion_posture": {
            "non_final_completion_posture_declared": True,
            "success_must_not_claim_final_completion": True,
        },
        "request_admission_scope": list(SUPPORTED_SCOPE),
        "requested_invocation_request_admission_outcome": ADMITTED,
        "declared_non_claims": _required_false_non_claims(),
    }
    if extra:
        request.update(extra)
    return request


def _inject_full_body_at_path(request: dict, path: tuple[str, ...], key: str = "full_artifact_body") -> dict:
    modified = copy.deepcopy(request)
    target = modified
    for part in path:
        target = target.setdefault(part, {})
    target[key] = SENTINEL
    return modified


def _inject_full_body_in_section(section: str, key: str = "full_artifact_body") -> dict:
    request = _clean_request()
    if section not in request or not isinstance(request[section], dict):
        request[section] = {}
    request[section].setdefault("v2_nested_probe", {})[key] = SENTINEL
    return request


class SingleLiveCommandInvocationRequestAdmissionBoundaryV2Tests(unittest.TestCase):
    def assert_clean_admitted(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(result["outcome"], ADMITTED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["request_admission_checks"]["failed_check_count"], 0)
        self.assertGreater(result["request_admission_checks"]["passed_check_count"], 0)

        statement = result["request_admission_statement"]
        for key in (
            "single_live_command_invocation_request_admitted",
            "single_invocation_request_declared",
            "single_invocation_scope_bounded",
            "single_invocation_admission_conditions_declared",
            "single_invocation_execution_still_not_performed",
            "single_invocation_requires_separate_execution_step",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "no_standing_invocation_lane_created",
            "no_repeat_invocation_permission_created",
            "request_admission_only",
            "one_shot_invocation_request_only",
            "invocation_requires_separate_execution_step",
            "invocation_must_use_reference_shaped_input",
            "invocation_must_not_mutate_artifacts",
            "invocation_must_not_embed_full_prior_artifacts",
        ):
            self.assertTrue(statement[key], key)
        _assert_common_non_claims_false(self, result)
        _assert_no_leakage(self, result)

    def assert_full_body_blocked_without_leakage(self, result: dict) -> None:
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], FULL_BODY_BLOCK)
        checks = result["request_admission_checks"]["checks"]
        self.assertTrue(
            any(
                check.get("block_code") == FULL_BODY_BLOCK
                or check.get("failure_code") == FULL_BODY_BLOCK
                for check in checks
            )
        )
        self.assertTrue(result["request_admission_statement"]["forbidden_full_body_posture_detected"])
        _assert_no_leakage(self, result)
        _assert_no_command_or_follow_on_created(self, result)

    def test_clean_request_admission_recorded(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            declared_invocation_request_admission=_clean_request()
        )
        self.assert_clean_admitted(result)

    def test_v2_metadata_and_successor_lineage(self) -> None:
        before_v1_source = V1_RESOLVER_PATH.read_text(encoding="utf-8")
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _clean_request()
        )
        after_v1_source = V1_RESOLVER_PATH.read_text(encoding="utf-8")
        metadata = result["single_live_command_invocation_request_admission_metadata"]

        self.assertTrue(metadata["single_live_command_invocation_request_admission_result_id"])
        self.assertTrue(metadata["single_live_command_invocation_request_admission_result_type"])
        self.assertEqual(
            metadata["single_live_command_invocation_request_admission_result_version"],
            "0.2.0",
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2",
        )
        self.assertEqual(
            metadata["successor_of"],
            "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary",
        )
        self.assertEqual(
            metadata["successor_reason"],
            "v1 returned-result containment flaw: raw full prior artifact body could be echoed into result",
        )
        self.assertTrue(
            result["request_admission_statement"]["successor_preserves_v1_as_historical_predecessor"]
        )
        self.assertTrue(result["request_admission_statement"]["successor_does_not_repair_or_hide_v1"])
        self.assertTrue(result["request_admission_statement"]["successor_does_not_claim_v1_passed"])
        self.assertEqual(before_v1_source, after_v1_source)

    def test_forbidden_full_body_in_command_report_basis_is_omitted(self) -> None:
        request = _inject_full_body_at_path(
            _clean_request(),
            ("selected_command_report_basis", "selected_basis"),
            "full_artifact_body",
        )
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            request
        )
        self.assert_full_body_blocked_without_leakage(result)
        self.assertEqual(
            result["selected_command_report_basis"]["selected_basis"]["selected_basis"][
                "full_artifact_body"
            ],
            OMISSION_MARKER,
        )
        for check in result["request_admission_checks"]["checks"]:
            self.assertNotIn(SENTINEL, _json_text(check.get("actual_posture")))
        self.assertNotIn(SENTINEL, _json_text(result["single_live_command_invocation_request_admission_summary"]))
        self.assertNotIn(SENTINEL, _json_text(result["block"]))
        self.assertNotIn(SENTINEL, _json_text(result["not_admitted_basis"]))
        self.assertNotIn(SENTINEL, _json_text(result["additional_basis_required"]))

    def test_recursive_containment_across_all_forbidden_keys(self) -> None:
        for forbidden_key in FORBIDDEN_KEYS:
            with self.subTest(forbidden_key=forbidden_key):
                request = _inject_full_body_at_path(
                    _clean_request(),
                    ("selected_command_execution_boundary_basis", "selected_basis"),
                    forbidden_key,
                )
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
                    request
                )
                self.assert_full_body_blocked_without_leakage(result)
                values = _find_forbidden_key_values(result)
                self.assertTrue(any(key == forbidden_key for key, _value in values))

    def test_recursive_containment_across_preserved_sections(self) -> None:
        sections = (
            "selected_command_execution_boundary_basis",
            "selected_command_report_basis",
            "selected_command_implementation_basis",
            "selected_artifact_emission_containment_basis",
            "selected_evidence_manifest_basis",
            "selected_portable_verification_basis",
            "proposed_one_shot_invocation_mode",
            "proposed_invocation_surface",
            "proposed_input_reference_bundle",
            "proposed_output_report_destination",
            "single_invocation_scope",
            "no_repeat_posture",
            "no_standing_invocation_lane_posture",
            "refusal_conditions",
            "output_limits",
            "result_limits",
            "success_limits",
            "non_authority_posture",
            "non_currentness_posture",
            "non_final_completion_posture",
            "additional_basis_context",
            "not_admitted_basis",
        )
        for section in sections:
            with self.subTest(section=section):
                request = _inject_full_body_in_section(section)
                before = copy.deepcopy(request)
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
                    request
                )
                self.assertEqual(request, before)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], FULL_BODY_BLOCK)
                _assert_no_leakage(self, result)
                _assert_no_command_or_follow_on_created(self, result)

    def test_clean_reference_shaped_request_does_not_trigger_containment_block(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _clean_request()
        )
        self.assert_clean_admitted(result)
        self.assertFalse(result["request_admission_statement"]["forbidden_full_body_posture_detected"])
        self.assertNotIn(FULL_BODY_BLOCK, _json_text(result["request_admission_checks"]))
        self.assertNotIn(OMISSION_MARKER, _json_text(result))

    def test_unsupported_scope_blocks_without_leakage(self) -> None:
        request = _clean_request({"request_admission_scope": ["UNSUPPORTED_SCOPE"]})
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {
                "UNSUPPORTED_INVOCATION_REQUEST_ADMISSION_SCOPE",
                "UNSUPPORTED_SINGLE_INVOCATION_REQUEST_ADMISSION_SCOPE",
            },
        )
        _assert_no_command_or_follow_on_created(self, result)
        _assert_no_leakage(self, result)

    def test_explicit_block_intent_blocks_without_admission(self) -> None:
        request = _clean_request(
            {
                "invocation_request_admission_intent": (
                    "BLOCK_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW"
                )
            }
        )
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {"INVOCATION_REQUEST_ADMISSION_REVIEW_EXPLICITLY_BLOCKED", "INVOCATION_REQUEST_ADMISSION_INTENT_BLOCKED"},
        )
        for key in (
            "single_live_command_invocation_request_admitted",
            "single_invocation_request_declared",
            "single_invocation_scope_bounded",
            "single_invocation_admission_conditions_declared",
            "single_invocation_execution_still_not_performed",
            "single_invocation_requires_separate_execution_step",
        ):
            self.assertFalse(result["request_admission_statement"][key], key)
        _assert_no_command_or_follow_on_created(self, result)
        _assert_no_leakage(self, result)

    def test_not_admitted_and_requires_additional_basis_outcomes(self) -> None:
        not_admitted_request = _clean_request(
            {
                "requested_invocation_request_admission_outcome": NOT_ADMITTED,
                "not_admitted_basis": {"reason": "one-shot scope not admitted"},
            }
        )
        not_admitted = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            not_admitted_request
        )
        self.assertEqual(not_admitted["outcome"], NOT_ADMITTED)
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted"])
        self.assertEqual(
            not_admitted["not_admitted_basis"]["not_admitted_basis"]["reason"],
            "one-shot scope not admitted",
        )
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted_does_not_authorize_follow_on_work"])
        _assert_no_command_or_follow_on_created(self, not_admitted)
        _assert_no_leakage(self, not_admitted)

        additional_request = _clean_request(
            {
                "requested_invocation_request_admission_outcome": REQUIRES_ADDITIONAL_BASIS,
                "additional_basis_context": {"missing_basis": "input reference precision"},
            }
        )
        additional = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            additional_request
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"]["missing_basis"],
            "input reference precision",
        )
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_executed"])
        _assert_no_command_or_follow_on_created(self, additional)
        _assert_no_leakage(self, additional)

        for outcome, context_key in (
            (NOT_ADMITTED, "not_admitted_basis"),
            (REQUIRES_ADDITIONAL_BASIS, "additional_basis_context"),
        ):
            with self.subTest(outcome=outcome):
                request = _clean_request({"requested_invocation_request_admission_outcome": outcome})
                request[context_key] = {"full_artifact_body": SENTINEL}
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
                    request
                )
                self.assert_full_body_blocked_without_leakage(result)

    def test_missing_or_malformed_requests_block(self) -> None:
        cases = [
            (
                None,
                {"INVOCATION_REQUEST_ADMISSION_QUESTION_UNDECLARED"},
            ),
            (
                "not a mapping",
                {"DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED"},
            ),
        ]
        for request, expected_codes in cases:
            with self.subTest(request=request):
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
                    request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["block"]["block_code"], expected_codes)
                _assert_no_leakage(self, result)

        field_cases = [
            ("invocation_request_admission_question", "INVOCATION_REQUEST_ADMISSION_QUESTION_UNDECLARED"),
            ("invocation_request_admission_intent", "INVOCATION_REQUEST_ADMISSION_INTENT_UNSUPPORTED"),
            ("selected_command_execution_boundary_basis", "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("proposed_one_shot_invocation_mode", "PROPOSED_INVOCATION_MODE_MISSING"),
            ("single_invocation_scope", "SINGLE_INVOCATION_SCOPE_MISSING"),
            ("no_repeat_posture", "NO_REPEAT_POSTURE_MISSING"),
            ("no_standing_invocation_lane_posture", "NO_STANDING_INVOCATION_LANE_POSTURE_MISSING"),
            ("declared_non_claims", "NON_CLAIM_MISSING_OR_FLIPPED"),
        ]
        for field, code in field_cases:
            with self.subTest(field=field):
                request = _clean_request()
                request.pop(field)
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
                    request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], code)
                _assert_no_leakage(self, result)

        unsupported_intent = _clean_request({"invocation_request_admission_intent": "RUN_THE_COMMAND_NOW"})
        unsupported_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            unsupported_intent
        )
        self.assertEqual(unsupported_result["outcome"], BLOCKED)
        self.assertEqual(
            unsupported_result["block"]["block_code"],
            "INVOCATION_REQUEST_ADMISSION_INTENT_UNSUPPORTED",
        )

        flipped = _clean_request()
        flipped["declared_non_claims"]["follow_on_work_authorized"] = True
        flipped_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            flipped
        )
        self.assertEqual(flipped_result["outcome"], BLOCKED)
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "FOLLOW_ON_WORK_AUTHORIZED"},
        )
        _assert_no_leakage(self, flipped_result)

    def test_path_based_request_blocks_malformed_and_array_inputs(self) -> None:
        mapping_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _clean_request()
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(_clean_request()), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2_from_path(
                request_path
            )
            self.assert_clean_admitted(path_result)
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                path_result["declared_invocation_request_admission_question"][
                    "declared_invocation_request_admission_path"
                ],
                str(request_path),
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], BLOCKED)
            self.assertEqual(
                malformed["block"]["block_code"],
                "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED",
            )
            _assert_no_leakage(self, malformed)

            array_path = tmp_path / "array.json"
            array_path.write_text(json.dumps([_clean_request()]), encoding="utf-8")
            array_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED",
            )

    def test_write_behavior_is_additive_and_sanitized(self) -> None:
        blocked_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _inject_full_body_at_path(
                _clean_request(),
                ("selected_command_report_basis", "selected_basis"),
                "full_artifact_body",
            )
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            explicit_path = tmp_path / "nested" / "blocked_result.json"
            written = write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2(
                blocked_result,
                explicit_path,
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], BLOCKED)
            _assert_no_leakage(self, parsed)

            default_root = (
                tmp_path
                / "integrity_host_v0_min_coexistence_portable_source_body_verification_"
                "single_live_command_invocation_request_admission_boundary_v2"
            )
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_V2_ROOT",
                default_root,
            ):
                first = write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2(
                    blocked_result
                )
                second = write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2(
                    blocked_result
                )
            self.assertTrue(str(first).startswith(str(default_root)))
            self.assertTrue(str(second).startswith(str(default_root)))
            self.assertNotEqual(first, second)
            self.assertIn("single_live_command_invocation_request_admission_result_v2.json", first.name)
            self.assertIn("_001.json", second.name)
            self.assertIn("boundary_v2", str(first))
            self.assertNotIn("request_admission_boundary/", str(first))
            self.assertNotIn("command_execution_boundary", str(first))
            self.assertNotIn("command_report", str(first))
            self.assertNotIn("deployment", str(first))
            self.assertNotIn("runtime", str(first))
            self.assertNotIn("public_release", str(first))

    def test_summary_helper_preserves_v2_posture_without_leakage(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _clean_request()
        )
        summary = build_portable_source_body_verification_single_live_command_invocation_request_admission_summary_v2(
            result
        )
        self.assertEqual(summary["outcome"], ADMITTED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["invocation_request_admission_id"],
            "single_live_command_invocation_request_admission_v2_001",
        )
        self.assertEqual(summary["invocation_request_admission_question"], QUESTION)
        self.assertEqual(
            summary["invocation_request_admission_intent"],
            "ADMIT_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "single_invocation_request_admitted",
            "single_invocation_request_declared",
            "single_invocation_scope_bounded",
            "admission_conditions_declared",
            "execution_still_not_performed",
            "requires_separate_execution_step",
            "request_admission_only",
            "one_shot_invocation_request_only",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "no_standing_invocation_lane",
            "no_repeat_invocation_permission",
            "output_not_source",
            "result_not_authority",
            "success_not_currentness",
            "success_not_final_completion",
            "reference_shaped_input_required",
            "no_full_prior_artifacts_embedded",
            "no_artifact_mutation",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work",
        ):
            self.assertTrue(summary[key], key)
        for key in (
            "selected_command_execution_boundary_basis_preserved",
            "selected_command_report_basis_preserved",
            "selected_command_implementation_basis_preserved",
            "artifact_emission_containment_basis_preserved",
            "evidence_manifest_basis_preserved",
            "portable_verification_basis_preserved",
        ):
            self.assertTrue(summary[key], key)
        self.assertFalse(summary["not_admitted"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertEqual(
            summary["successor_of"],
            "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary",
        )
        self.assertTrue(summary["successor_does_not_repair_or_hide_v1"])
        self.assertTrue(summary["successor_does_not_claim_v1_passed"])
        _assert_no_leakage(self, summary)

        blocked = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            _inject_full_body_at_path(
                _clean_request(),
                ("selected_command_execution_boundary_basis", "selected_basis"),
                "raw_result",
            )
        )
        blocked_summary = build_portable_source_body_verification_single_live_command_invocation_request_admission_summary_v2(
            blocked
        )
        self.assertEqual(blocked_summary["block_code"], FULL_BODY_BLOCK)
        self.assertTrue(blocked_summary["forbidden_full_body_posture_detected"])
        _assert_no_leakage(self, blocked_summary)

    def test_non_mutation_posture(self) -> None:
        request = _inject_full_body_at_path(
            _clean_request(),
            ("selected_command_report_basis", "selected_basis"),
            "complete_artifact_body",
        )
        before = copy.deepcopy(request)
        selected_before = {
            key: copy.deepcopy(request[key])
            for key in (
                "selected_command_execution_boundary_basis",
                "selected_command_report_basis",
                "selected_command_implementation_basis",
                "selected_artifact_emission_containment_basis",
                "selected_evidence_manifest_basis",
                "selected_portable_verification_basis",
                "proposed_one_shot_invocation_mode",
                "proposed_invocation_surface",
                "proposed_input_reference_bundle",
                "proposed_output_report_destination",
                "single_invocation_scope",
                "no_repeat_posture",
                "no_standing_invocation_lane_posture",
                "refusal_conditions",
                "output_limits",
                "result_limits",
                "success_limits",
                "request_admission_scope",
            )
        }
        first = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            request
        )
        second = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_v2(
            request
        )
        self.assert_full_body_blocked_without_leakage(first)
        self.assert_full_body_blocked_without_leakage(second)
        self.assertEqual(request, before)
        for key, value in selected_before.items():
            self.assertEqual(request[key], value, key)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "additive_v2_result.json"
            write_portable_source_body_verification_single_live_command_invocation_request_admission_result_v2(
                first,
                output_path,
            )
            self.assertTrue(output_path.exists())
            self.assertEqual(request, before)

    def test_source_safety_has_no_obvious_shell_network_or_openai_calls(self) -> None:
        source = V2_RESOLVER_PATH.read_text(encoding="utf-8")
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
