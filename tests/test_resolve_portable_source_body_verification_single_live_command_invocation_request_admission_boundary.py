"""Bounded tests for single live command invocation request/admission.

These tests prove only request/admission posture. Admitted request is not
invocation, not execution, not command output, not command result, not command
success, not a standing invocation lane, and not repeat invocation permission.
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

import resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary as resolver  # noqa: E402
from resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary import (  # noqa: E402
    build_declared_portable_source_body_verification_single_live_command_invocation_request_admission,
    build_portable_source_body_verification_single_live_command_invocation_request_admission_summary,
    resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary,
    resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_from_path,
    write_portable_source_body_verification_single_live_command_invocation_request_admission_result,
)


ADMITTED = resolver.OUTCOME_ADMITTED
NOT_ADMITTED = resolver.OUTCOME_NOT_ADMITTED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {ADMITTED, NOT_ADMITTED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
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


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def selected_result_reference(
    *, result_id: str, outcome: str, family: str, summary: dict, passed: int = 12
) -> dict:
    return {
        "selected_result_id": result_id,
        "selected_result_path": f"artifacts/{family}/{result_id}.json",
        "selected_result_outcome": outcome,
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": passed,
        "selected_result_summary": summary,
        "selected_result_non_claims": required_false_non_claims(),
        "selected_result_basis_reference": f"{family}:{result_id}",
        "selected_result_artifact_family": family,
        "selected_result_artifact_size_class": "bounded-kb-reference",
        "reference_shaped_basis_only": True,
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
    }


def selected_command_execution_boundary_basis() -> dict:
    return selected_result_reference(
        result_id="portable_source_body_verification_command_execution_boundary_reference_review_001",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_RECORDED",
        family="portable_source_body_verification_command_execution_boundary",
        summary={
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


def selected_command_report_basis() -> dict:
    basis = selected_result_reference(
        result_id="portable_source_body_verification_command_report_reference_review_001_corrected",
        outcome="PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT",
        family="portable_source_body_verification_command_report",
        summary={
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


def selected_command_implementation_basis() -> dict:
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


def selected_command_module_reference() -> dict:
    return {
        "command_module_reference_declared": True,
        "module_path": "src/portable_source_body_verification_command.py",
        "module_reference_is_reference_only": True,
        "module_reference_does_not_authorize_invocation": True,
        "module_reference_does_not_authorize_execution": True,
    }


def selected_test_surface_reference() -> dict:
    return {
        "test_surface_reference_declared": True,
        "path": "tests/test_portable_source_body_verification_command.py",
        "test_surface_reference_is_reference_only": True,
        "test_pass_does_not_authorize_invocation": True,
        "test_pass_does_not_authorize_execution": True,
    }


def selected_artifact_emission_containment_basis() -> dict:
    return selected_result_reference(
        result_id="artifact_emission_containment_reference_review_001",
        outcome="ARTIFACT_EMISSION_CONTAINMENT_RECORDED",
        family="artifact_emission_containment_boundary",
        summary={
            "reference_only_selected_basis_required": True,
            "recursive_full_artifact_embedding_blocked": True,
            "prior_artifacts_preserved_by_reference": True,
            "artifacts_not_mutated": True,
        },
    )


def selected_evidence_manifest_basis() -> dict:
    return selected_result_reference(
        result_id="portable_source_body_verification_evidence_manifest_reference_review_001",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED",
        family="portable_source_body_verification_evidence_manifest_boundary",
        summary={
            "evidence_manifest_basis_declared": True,
            "evidence_only": True,
            "does_not_authorize_command_invocation_or_execution": True,
        },
    )


def selected_portable_verification_basis() -> dict:
    return selected_result_reference(
        result_id="portable_source_body_verification_reference_review_001",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        family="portable_source_body_verification_boundary",
        summary={
            "portable_verification_recorded": True,
            "verification_only": True,
            "does_not_authorize_command_invocation_or_execution": True,
        },
    )


def proposed_one_shot_invocation_mode() -> dict:
    return {
        "one_shot_invocation_mode_declared": True,
        "one_bounded_invocation_candidate_only": True,
        "proposed_mode_is_future_only": True,
        "proposal_is_not_invocation": True,
        "proposal_is_not_execution": True,
    }


def proposed_invocation_surface() -> dict:
    return {
        "proposed_invocation_surface_declared": True,
        "future_explicit_local_function_invocation_if_separately_authorized": True,
        "proposal_is_not_invocation": True,
        "proposal_does_not_authorize_execution": True,
    }


def proposed_input_reference_bundle() -> dict:
    return {
        "proposed_input_reference_bundle_declared": True,
        "reference_shaped_input_required": True,
        "full_prior_artifacts_embedded": False,
        "input_bundle_does_not_create_authority_currentness": True,
    }


def proposed_output_report_destination() -> dict:
    return {
        "proposed_output_report_destination_declared": True,
        "future_bounded_additive_execution_report_destination_if_separately_authorized": True,
        "destination_is_future_only": True,
        "destination_does_not_create_output_result_success_here": True,
    }


def single_invocation_scope() -> dict:
    return {
        "single_invocation_scope_declared": True,
        "one_shot_invocation_request_only": True,
        "one_invocation_candidate_only": True,
        "no_standing_invocation_lane": True,
        "no_repeat_permission": True,
    }


def no_repeat_posture() -> dict:
    return {
        "no_repeat_posture_declared": True,
        "repeat_invocation_permission_created": False,
        "reusable_permission_created": False,
    }


def no_standing_invocation_lane_posture() -> dict:
    return {
        "no_standing_invocation_lane_posture_declared": True,
        "standing_invocation_lane_created": False,
        "no_general_invocation_lane_created": True,
    }


def refusal_conditions() -> dict:
    return {
        "refusal_conditions_declared": True,
        "refuse_if_full_artifact_bodies_required": True,
        "refuse_if_artifact_mutation_required": True,
        "refuse_if_invocation_would_create_authority_currentness_final_completion": True,
        "refuse_if_repeat_permission_requested": True,
        "refuse_if_standing_lane_requested": True,
    }


def output_limits() -> dict:
    return {
        "output_limits_declared": True,
        "command_output_not_created": True,
        "command_output_must_be_non_source": True,
    }


def result_limits() -> dict:
    return {
        "result_limits_declared": True,
        "command_result_not_created": True,
        "command_result_must_be_non_authority": True,
    }


def success_limits() -> dict:
    return {
        "success_limits_declared": True,
        "command_success_not_created": True,
        "command_success_must_not_create_currentness": True,
        "command_success_must_not_claim_final_completion": True,
    }


def valid_request(extra: dict | None = None) -> dict:
    request = {
        "invocation_request_admission_id": (
            "portable_source_body_verification_single_live_command_invocation_request_admission_001"
        ),
        "invocation_request_admission_question": QUESTION,
        "invocation_request_admission_intent": "ADMIT_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST",
        "selected_command_execution_boundary_basis": selected_command_execution_boundary_basis(),
        "selected_command_report_basis": selected_command_report_basis(),
        "selected_command_implementation_basis": selected_command_implementation_basis(),
        "selected_command_module_reference": selected_command_module_reference(),
        "selected_test_surface_reference": selected_test_surface_reference(),
        "selected_artifact_emission_containment_basis": selected_artifact_emission_containment_basis(),
        "selected_evidence_manifest_basis": selected_evidence_manifest_basis(),
        "selected_portable_verification_basis": selected_portable_verification_basis(),
        "proposed_one_shot_invocation_mode": proposed_one_shot_invocation_mode(),
        "proposed_invocation_surface": proposed_invocation_surface(),
        "proposed_input_reference_bundle": proposed_input_reference_bundle(),
        "proposed_output_report_destination": proposed_output_report_destination(),
        "single_invocation_scope": single_invocation_scope(),
        "no_repeat_posture": no_repeat_posture(),
        "no_standing_invocation_lane_posture": no_standing_invocation_lane_posture(),
        "refusal_conditions": refusal_conditions(),
        "output_limits": output_limits(),
        "result_limits": result_limits(),
        "success_limits": success_limits(),
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
        "declared_non_claims": required_false_non_claims(),
    }
    if extra:
        request.update(extra)
    return request


class SingleLiveCommandInvocationRequestAdmissionBoundaryTests(unittest.TestCase):
    def assert_admitted_result(self, result: dict) -> None:
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
            "selected_command_execution_boundary_basis_preserved",
            "selected_command_report_basis_preserved",
            "selected_command_implementation_basis_preserved",
            "selected_artifact_emission_containment_basis_preserved",
            "selected_evidence_manifest_basis_preserved",
            "selected_portable_verification_basis_preserved",
            "request_admission_only",
            "one_shot_invocation_request_only",
            "command_invocation_not_created",
            "command_execution_not_performed",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "no_standing_invocation_lane_created",
            "no_repeat_invocation_permission_created",
            "command_output_must_be_non_source",
            "command_result_must_be_non_authority",
            "command_success_must_not_create_currentness",
            "command_success_must_not_claim_final_completion",
            "invocation_must_use_reference_shaped_input",
            "invocation_must_not_mutate_artifacts",
            "invocation_must_not_embed_full_prior_artifacts",
        ):
            self.assertTrue(statement[key], key)

        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_single_invocation_request_admitted_result(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            declared_invocation_request_admission=valid_request()
        )
        self.assert_admitted_result(result)
        self.assertEqual(OUTCOME_FAMILY, resolver.OUTCOME_FAMILY)

        self.assertTrue(
            result["selected_command_execution_boundary_basis"][
                "command_execution_boundary_basis_preserved"
            ]
        )
        self.assertTrue(result["selected_command_report_basis"]["command_report_basis_preserved"])
        self.assertTrue(
            result["selected_command_implementation_basis"][
                "command_implementation_basis_preserved"
            ]
        )
        self.assertTrue(result["proposed_one_shot_invocation_mode"]["proposal_is_not_invocation"])
        self.assertTrue(result["proposed_invocation_surface"]["proposal_does_not_authorize_execution"])
        self.assertTrue(result["proposed_input_reference_bundle"]["proposal_is_not_success"])
        self.assertTrue(result["single_invocation_scope"]["proposal_is_not_execution"])
        self.assertTrue(result["no_repeat_posture"]["no_repeat_invocation_permission_created"])
        self.assertTrue(
            result["no_standing_invocation_lane_posture"]["no_standing_invocation_lane_created"]
        )

    def test_metadata(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request()
        )
        metadata = result["single_live_command_invocation_request_admission_metadata"]
        self.assertTrue(metadata["single_live_command_invocation_request_admission_result_id"])
        self.assertTrue(metadata["single_live_command_invocation_request_admission_result_type"])
        self.assertEqual(
            metadata["single_live_command_invocation_request_admission_result_version"],
            "0.1.0",
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary",
        )

    def test_request_admission_checks(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request()
        )
        checks = result["request_admission_checks"]["checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])

        check_names = {check["check_name"] for check in checks}
        expected_names = {
            "request/admission question declared",
            "request/admission intent supported",
            "command execution boundary basis declared",
            "command report basis declared",
            "command implementation basis declared",
            "command module reference declared",
            "test surface reference declared",
            "artifact emission containment basis declared",
            "evidence manifest basis declared",
            "portable verification basis declared",
            "proposed one-shot invocation mode declared",
            "proposed invocation surface declared",
            "proposed input reference bundle declared",
            "proposed output/report destination declared",
            "one-invocation scope declared",
            "no-repeat posture declared",
            "no-standing-invocation-lane posture declared",
            "refusal conditions declared",
            "output limits declared",
            "result limits declared",
            "success limits declared",
            "non-authority posture declared",
            "non-currentness posture declared",
            "non-final-completion posture declared",
            "request/admission scope supported",
            "command invocation not created",
            "command execution not performed",
            "command output not created",
            "command result not created",
            "command success not created",
            "no standing invocation lane created",
            "no repeat invocation permission created",
            "output remains non-source",
            "result remains non-authority",
            "success does not create currentness",
            "success does not claim final completion",
            "full prior artifacts not embedded",
            "artifacts not mutated",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_names.issubset(check_names))

    def test_request_admission_non_meaning(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request()
        )
        non_meaning = result["request_admission_non_meaning"]
        expected = {
            "request_admission_does_not_mean_command_invoked",
            "request_admission_does_not_mean_command_executed",
            "request_admission_does_not_mean_command_output_exists",
            "request_admission_does_not_mean_command_result_exists",
            "request_admission_does_not_mean_command_success_exists",
            "request_admission_does_not_mean_live_verification_completed",
            "request_admission_does_not_mean_invocation_permission_reusable",
            "request_admission_does_not_mean_standing_invocation_lane_exists",
            "request_admission_does_not_mean_repeated_invocations_authorized",
            "request_admission_does_not_mean_command_output_became_source",
            "request_admission_does_not_mean_command_result_became_authority",
            "request_admission_does_not_mean_command_success_created_currentness",
            "request_admission_does_not_mean_command_success_claimed_final_completion",
            "request_admission_does_not_mean_deployment_created",
            "request_admission_does_not_mean_runtime_hosting_created",
            "request_admission_does_not_mean_public_release_created",
            "request_admission_does_not_mean_public_readiness_created",
            "request_admission_does_not_mean_operation_permission_created",
            "request_admission_does_not_mean_continuation_authorized",
            "request_admission_does_not_mean_reusable_permission_created",
            "request_admission_does_not_mean_derivative_reception_authorized",
            "request_admission_does_not_mean_vessel_relation_authorized",
            "request_admission_does_not_mean_another_reception_request_authorized",
            "request_admission_does_not_mean_follow_on_work_authorized",
        }
        self.assertTrue(expected.issubset(non_meaning))
        for key in expected:
            self.assertTrue(non_meaning[key], key)

    def test_requires_additional_basis_and_not_admitted(self) -> None:
        additional_request = valid_request(
            {
                "requested_invocation_request_admission_outcome": REQUIRES_ADDITIONAL_BASIS,
                "additional_basis_context": {"missing_basis": "single invocation input precision"},
            }
        )
        additional = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            additional_request
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"]["missing_basis"],
            "single invocation input precision",
        )
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_executed"])
        self.assertTrue(additional["additional_basis_required"]["command_not_invoked"])
        self.assertTrue(additional["additional_basis_required"]["repeat_invocation_permission_not_created"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(additional["non_claims"][key], False, key)

        not_admitted_request = valid_request(
            {
                "requested_invocation_request_admission_outcome": NOT_ADMITTED,
                "not_admitted_basis": {"reason": "single invocation scope could not be bounded"},
            }
        )
        not_admitted = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            not_admitted_request
        )
        self.assertEqual(not_admitted["outcome"], NOT_ADMITTED)
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted"])
        self.assertEqual(
            not_admitted["not_admitted_basis"]["not_admitted_basis"]["reason"],
            "single invocation scope could not be bounded",
        )
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted_does_not_repair"])
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted_does_not_authorize_invocation"])
        self.assertTrue(not_admitted["not_admitted_basis"]["not_admitted_does_not_authorize_follow_on_work"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(not_admitted["non_claims"][key], False, key)

    def test_what_remains_open(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request()
        )
        remains = result["what_remains_open"]
        expected_items = {
            "request/admission test",
            "request/admission live artifact",
            "actual command invocation",
            "command output from live execution",
            "command result from live execution",
            "command success",
            "live verification result",
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
        self.assertTrue(expected_items.issubset(set(remains["open_items"])))
        self.assertTrue(remains["open_means_not_scheduled"])
        self.assertTrue(remains["open_means_not_authorized"])
        self.assertTrue(remains["open_means_not_executed"])

    def test_summary_helper(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request()
        )
        summary = build_portable_source_body_verification_single_live_command_invocation_request_admission_summary(
            result
        )
        self.assertEqual(summary["outcome"], ADMITTED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["invocation_request_admission_id"],
            "portable_source_body_verification_single_live_command_invocation_request_admission_001",
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
            "selected_command_execution_boundary_basis_preserved",
            "selected_command_report_basis_preserved",
            "selected_command_implementation_basis_preserved",
            "artifact_emission_containment_basis_preserved",
            "evidence_manifest_basis_preserved",
            "portable_verification_basis_preserved",
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
        self.assertFalse(summary["not_admitted"])
        self.assertFalse(summary["requires_additional_basis"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_request_builder_helper(self) -> None:
        request = build_declared_portable_source_body_verification_single_live_command_invocation_request_admission(
            "builder_request_001",
            QUESTION,
            selected_command_execution_boundary_basis(),
            selected_command_report_basis(),
            selected_command_implementation_basis(),
            selected_artifact_emission_containment_basis(),
            selected_evidence_manifest_basis(),
            selected_portable_verification_basis(),
            proposed_one_shot_invocation_mode(),
            proposed_invocation_surface(),
            proposed_input_reference_bundle(),
            proposed_output_report_destination(),
            single_invocation_scope(),
            no_repeat_posture(),
            no_standing_invocation_lane_posture(),
            refusal_conditions(),
            output_limits(),
            result_limits(),
            success_limits(),
            list(SUPPORTED_SCOPE),
            additional_basis_context={"basis": "kept"},
            not_admitted_basis={"reason": "kept"},
        )
        self.assertEqual(request["invocation_request_admission_id"], "builder_request_001")
        self.assertEqual(request["invocation_request_admission_question"], QUESTION)
        self.assertEqual(request["selected_command_execution_boundary_basis"], selected_command_execution_boundary_basis())
        self.assertEqual(request["selected_command_report_basis"], selected_command_report_basis())
        self.assertEqual(request["selected_command_implementation_basis"], selected_command_implementation_basis())
        self.assertEqual(request["selected_artifact_emission_containment_basis"], selected_artifact_emission_containment_basis())
        self.assertEqual(request["selected_evidence_manifest_basis"], selected_evidence_manifest_basis())
        self.assertEqual(request["selected_portable_verification_basis"], selected_portable_verification_basis())
        self.assertEqual(request["proposed_one_shot_invocation_mode"], proposed_one_shot_invocation_mode())
        self.assertEqual(request["proposed_invocation_surface"], proposed_invocation_surface())
        self.assertEqual(request["proposed_input_reference_bundle"], proposed_input_reference_bundle())
        self.assertEqual(request["proposed_output_report_destination"], proposed_output_report_destination())
        self.assertEqual(request["single_invocation_scope"], single_invocation_scope())
        self.assertEqual(request["no_repeat_posture"], no_repeat_posture())
        self.assertEqual(request["no_standing_invocation_lane_posture"], no_standing_invocation_lane_posture())
        self.assertEqual(request["refusal_conditions"], refusal_conditions())
        self.assertEqual(request["output_limits"], output_limits())
        self.assertEqual(request["result_limits"], result_limits())
        self.assertEqual(request["success_limits"], success_limits())
        self.assertEqual(set(request["request_admission_scope"]), set(SUPPORTED_SCOPE))
        self.assertEqual(request["requested_invocation_request_admission_outcome"], ADMITTED)
        self.assertEqual(request["additional_basis_context"], {"basis": "kept"})
        self.assertEqual(request["not_admitted_basis"], {"reason": "kept"})
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            request
        )
        self.assert_admitted_result(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = valid_request()
        mapping_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            request
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_from_path(
                request_path
            )
            self.assert_admitted_result(path_result)
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                path_result["declared_invocation_request_admission_question"][
                    "declared_invocation_request_admission_path"
                ],
                str(request_path),
            )

            output_path = tmp_path / "nested" / "explicit_result.json"
            written = write_portable_source_body_verification_single_live_command_invocation_request_admission_result(
                path_result, output_path
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], ADMITTED)

            default_root = tmp_path / "request_admission_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_ADMISSION_BOUNDARY_ROOT",
                default_root,
            ):
                first = write_portable_source_body_verification_single_live_command_invocation_request_admission_result(
                    path_result
                )
                second = write_portable_source_body_verification_single_live_command_invocation_request_admission_result(
                    path_result
                )
            self.assertTrue(str(first).startswith(str(default_root)))
            self.assertTrue(str(second).startswith(str(default_root)))
            self.assertNotEqual(first, second)
            self.assertIn(
                "single_live_command_invocation_request_admission_result.json",
                first.name,
            )
            self.assertIn("_001.json", second.name)
            self.assertNotIn("command_execution_boundary", str(first))
            self.assertNotIn("command_output", str(first))
            self.assertNotIn("deployment", str(first))
            self.assertNotIn("runtime", str(first))
            self.assertNotIn("public_release", str(first))

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
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

        first = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            request
        )
        second = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            request
        )
        self.assert_admitted_result(first)
        self.assert_admitted_result(second)
        self.assertEqual(request, before)
        for key, value in selected_before.items():
            self.assertEqual(request[key], value, key)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            write_portable_source_body_verification_single_live_command_invocation_request_admission_result(
                first, output_path
            )
            self.assertTrue(output_path.exists())
            self.assertEqual(request, before)

    def test_missing_and_malformed_requests_block(self) -> None:
        missing = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            None
        )
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(
            missing["block"]["block_code"],
            "INVOCATION_REQUEST_ADMISSION_QUESTION_UNDECLARED",
        )

        malformed = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            "not a mapping"
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bad_json = tmp_path / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_from_path(
                bad_json
            )
            self.assertEqual(bad_result["outcome"], BLOCKED)
            self.assertEqual(
                bad_result["block"]["block_code"],
                "DECLARED_INVOCATION_REQUEST_ADMISSION_MALFORMED",
            )

            missing_path = tmp_path / "missing.json"
            unreadable = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary_from_path(
                missing_path
            )
            self.assertEqual(unreadable["outcome"], BLOCKED)
            self.assertEqual(
                unreadable["block"]["block_code"],
                "DECLARED_INVOCATION_REQUEST_ADMISSION_UNREADABLE",
            )

    def test_missing_required_fields_block(self) -> None:
        cases = [
            ("invocation_request_admission_question", "INVOCATION_REQUEST_ADMISSION_QUESTION_UNDECLARED"),
            ("selected_command_execution_boundary_basis", "COMMAND_EXECUTION_BOUNDARY_BASIS_MISSING"),
            ("selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
            ("selected_command_implementation_basis", "COMMAND_IMPLEMENTATION_SPEC_MISSING"),
            ("selected_command_module_reference", "COMMAND_MODULE_REFERENCE_MISSING"),
            ("selected_test_surface_reference", "TEST_SURFACE_REFERENCE_MISSING"),
            ("selected_artifact_emission_containment_basis", "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING"),
            ("selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("proposed_one_shot_invocation_mode", "PROPOSED_INVOCATION_MODE_MISSING"),
            ("proposed_invocation_surface", "PROPOSED_INVOCATION_SURFACE_MISSING"),
            ("proposed_input_reference_bundle", "INPUT_REFERENCE_BUNDLE_MISSING"),
            ("proposed_output_report_destination", "OUTPUT_REPORT_DESTINATION_MISSING"),
            ("single_invocation_scope", "SINGLE_INVOCATION_SCOPE_MISSING"),
            ("no_repeat_posture", "NO_REPEAT_POSTURE_MISSING"),
            ("no_standing_invocation_lane_posture", "NO_STANDING_INVOCATION_LANE_POSTURE_MISSING"),
            ("refusal_conditions", "REFUSAL_CONDITIONS_MISSING"),
            ("output_limits", "OUTPUT_LIMITS_MISSING"),
            ("result_limits", "RESULT_LIMITS_MISSING"),
            ("success_limits", "SUCCESS_LIMITS_MISSING"),
        ]
        for field, code in cases:
            with self.subTest(field=field):
                request = valid_request()
                request.pop(field)
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
                    request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], code)

        unsupported = valid_request({"request_admission_scope": ["UNSUPPORTED_SCOPE"]})
        unsupported_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            unsupported
        )
        self.assertEqual(unsupported_result["outcome"], BLOCKED)
        self.assertEqual(
            unsupported_result["block"]["block_code"],
            "UNSUPPORTED_INVOCATION_REQUEST_ADMISSION_SCOPE",
        )

    def test_explicit_block_intent(self) -> None:
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            valid_request(
                {
                    "invocation_request_admission_intent": (
                        "BLOCK_SINGLE_LIVE_COMMAND_INVOCATION_REQUEST_REVIEW"
                    )
                }
            )
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "INVOCATION_REQUEST_ADMISSION_REVIEW_EXPLICITLY_BLOCKED",
        )

    def test_blocking_collapse_flags(self) -> None:
        cases = [
            ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
            ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("standing_invocation_lane_created", "STANDING_INVOCATION_LANE_CREATED"),
            ("repeat_invocation_permission_created", "REPEAT_INVOCATION_PERMISSION_CREATED"),
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
            ("continuation_authorized", "CONTINUATION_AUTHORIZED"),
            ("reusable_permission_created", "REUSABLE_PERMISSION_CREATED"),
            ("derivative_reception_authorized", "DERIVATIVE_RECEPTION_AUTHORIZED"),
            ("vessel_relation_authorized", "VESSEL_RELATION_AUTHORIZED"),
            ("another_reception_request_authorized", "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"),
            ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
        ]
        for flag, code in cases:
            with self.subTest(flag=flag):
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
                    valid_request({flag: True})
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], code)

    def test_full_prior_artifact_body_is_blocked_and_not_embedded(self) -> None:
        request = valid_request()
        request["selected_command_report_basis"]["full_artifact_body"] = "x" * 5000
        result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], "FULL_PRIOR_ARTIFACTS_EMBEDDED")
        self.assertNotIn("x" * 5000, json.dumps(result))
        self.assertIs(result["non_claims"]["prior_artifacts_mutated"], False)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
                    valid_request({flag: True})
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(
                    result["block"]["block_code"],
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claim = valid_request()
        missing_non_claim["declared_non_claims"].pop(
            "single_invocation_request_admission_recorded_as_execution"
        )
        missing_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            missing_non_claim
        )
        self.assertEqual(missing_result["outcome"], BLOCKED)
        self.assertEqual(missing_result["block"]["block_code"], "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = valid_request()
        flipped_non_claim["declared_non_claims"]["command_executed"] = True
        flipped_result = resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary(
            flipped_non_claim
        )
        self.assertEqual(flipped_result["outcome"], BLOCKED)
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"COMMAND_EXECUTION_PERFORMED", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_source_safety_check(self) -> None:
        source = (
            SRC_ROOT
            / "resolve_portable_source_body_verification_single_live_command_invocation_request_admission_boundary.py"
        ).read_text(encoding="utf-8")
        forbidden = (
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
        for token in forbidden:
            self.assertNotIn(token, source)


if __name__ == "__main__":
    unittest.main()
