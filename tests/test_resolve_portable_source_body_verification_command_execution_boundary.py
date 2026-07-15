"""Bounded tests for the portable verification command execution boundary.

These tests prove only the command execution-boundary resolver. The boundary
records conditions for a future bounded invocation; it is not execution,
invocation, command output, command result, command success, deployment,
runtime hosting, public release, source transfer, source migration, source
receipt, reception authorization, authority, currentness, final completion,
continuation, reusable permission, derivative reception, vessel relation,
another reception request, or follow-on work.
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

import resolve_portable_source_body_verification_command_execution_boundary as resolver  # noqa: E402
from resolve_portable_source_body_verification_command_execution_boundary import (  # noqa: E402
    build_declared_portable_source_body_verification_command_execution_boundary_request,
    build_portable_source_body_verification_command_execution_boundary_summary,
    resolve_portable_source_body_verification_command_execution_boundary,
    resolve_portable_source_body_verification_command_execution_boundary_from_path,
    write_portable_source_body_verification_command_execution_boundary_result,
)


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_COMMAND_EXECUTION_BOUNDARY_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_command_execution_boundary_metadata",
    "declared_command_execution_boundary_question",
    "selected_command_report_basis",
    "selected_command_implementation_basis",
    "selected_command_implementation_boundary_basis",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "proposed_execution_mode",
    "proposed_invocation_surface",
    "proposed_input_reference_bundle",
    "proposed_output_report_destination",
    "execution_limits",
    "output_limits",
    "result_limits",
    "success_limits",
    "refusal_conditions",
    "execution_boundary_scope",
    "execution_boundary_checks",
    "execution_boundary_statement",
    "execution_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_execution_boundary_summary",
}

QUESTION = (
    "Can conditions for a future bounded command invocation be recorded "
    "without executing, invoking, emitting output, creating a result, or "
    "creating command success?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def selected_result_reference(
    *,
    result_id: str,
    outcome: str,
    family: str,
    summary: dict,
    non_claims: dict | None = None,
    path: str | None = None,
    passed: int = 12,
) -> dict:
    return {
        "selected_result_id": result_id,
        "selected_result_path": path or f"artifacts/{family}/{result_id}.json",
        "selected_result_outcome": outcome,
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": passed,
        "selected_result_summary": summary,
        "selected_result_non_claims": non_claims or required_false_non_claims(),
        "selected_result_basis_reference": f"{family}:{result_id}",
        "selected_result_artifact_family": family,
        "selected_result_artifact_size_class": "bounded-kb-reference",
        "reference_shaped_basis_only": True,
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
    }


def selected_command_report_basis(extra: dict | None = None) -> dict:
    basis = selected_result_reference(
        result_id="portable_source_body_verification_command_report_reference_review_001_corrected",
        outcome="PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT",
        family="portable_source_body_verification_command_report",
        summary={
            "report_built": True,
            "checker_findings_built": True,
            "reference_shape_checks_passed": True,
            "non_claim_checks_passed": True,
            "report_non_authoritative": True,
            "command_execution_not_authorized": True,
            "command_invocation_not_created": True,
            "command_output_not_created": True,
            "command_result_not_created": True,
            "command_success_not_created": True,
            "report_built_status_is_not_command_success": True,
        },
        non_claims={
            "command_executed": False,
            "command_invocation_created": False,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
            "follow_on_work_authorized": False,
        },
    )
    basis["selected_result_status"] = "PORTABLE_VERIFICATION_COMMAND_REPORT_BUILT"
    if extra:
        basis.update(extra)
    return basis


def selected_command_implementation_basis(extra: dict | None = None) -> dict:
    basis = {
        "implementation_spec_declared": True,
        "implementation_spec_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_V0_MIN_SPEC.md"
        ),
        "selected_command_module_reference": "src/portable_source_body_verification_command.py",
        "selected_test_surface_reference": "tests/test_portable_source_body_verification_command.py",
        "command_module_reference_declared": True,
        "implementation_remains_checker_only": True,
        "implementation_did_not_authorize_execution": True,
        "execution_requires_separate_boundary": True,
        "reference_shaped_basis_only": True,
        "full_prior_artifacts_embedded": False,
    }
    if extra:
        basis.update(extra)
    return basis


def selected_command_implementation_boundary_basis() -> dict:
    return selected_result_reference(
        result_id="portable_source_body_verification_command_implementation_boundary_reference_review_001",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_RECORDED",
        family="portable_source_body_verification_command_implementation_boundary",
        summary={
            "implementation_boundary_recorded": True,
            "command_implementation_conditions_declared": True,
            "command_execution_requires_separate_boundary": True,
            "command_implemented": False,
            "command_executed": False,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
        },
    )


def selected_command_boundary_basis() -> dict:
    return selected_result_reference(
        result_id="portable_source_body_verification_command_boundary_reference_review_001_contained",
        outcome="PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED",
        family="portable_source_body_verification_command_boundary",
        summary={
            "checker_only_command_posture_declared": True,
            "command_not_implemented": True,
            "command_not_executed": True,
            "command_output_created": False,
            "command_result_created": False,
            "command_success_created": False,
        },
    )


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
            "does_not_authorize_command_execution": True,
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
            "does_not_authorize_command_execution": True,
        },
    )


def selected_command_module_reference() -> dict:
    return {
        "module_reference_declared": True,
        "module_path": "src/portable_source_body_verification_command.py",
        "module_reference_is_reference_only": True,
        "module_reference_does_not_authorize_execution": True,
    }


def selected_test_surface_reference() -> dict:
    return {
        "test_surface_reference_declared": True,
        "path": "tests/test_portable_source_body_verification_command.py",
        "test_surface_reference_is_reference_only": True,
        "test_pass_does_not_authorize_execution": True,
    }


def proposed_execution_mode() -> dict:
    return {
        "proposed_execution_mode_declared": True,
        "execution_mode_is_future_bounded_invocation_only": True,
        "proposal_is_not_execution": True,
        "proposal_does_not_authorize_execution": True,
    }


def proposed_invocation_surface() -> dict:
    return {
        "proposed_invocation_surface_declared": True,
        "proposed_invocation_is_future_only": True,
        "proposal_is_not_invocation": True,
    }


def proposed_input_reference_bundle() -> dict:
    return {
        "proposed_input_reference_bundle_declared": True,
        "reference_shaped_input_required": True,
        "full_prior_artifacts_embedded": False,
        "input_bundle_does_not_create_authority_currentness": True,
        "selected_results": [
            "portable_source_body_verification_command_report_reference_review_001_corrected",
            "portable_source_body_verification_command_implementation_boundary_reference_review_001",
        ],
    }


def proposed_output_report_destination() -> dict:
    return {
        "proposed_output_report_destination_declared": True,
        "destination_is_future_only": True,
        "destination_does_not_create_output_result_success_here": True,
    }


def execution_limits() -> dict:
    return {
        "execution_limits_declared": True,
        "command_execution_not_performed": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "execution_is_not_deployment_runtime_public_release": True,
        "execution_does_not_authorize_continuation_follow_on_work": True,
        "execution_requires_reference_shaped_input": True,
        "execution_must_not_mutate_artifacts": True,
        "execution_must_not_embed_full_prior_artifacts": True,
    }


def output_limits() -> dict:
    return {
        "output_limits_declared": True,
        "command_output_not_created": True,
        "command_output_is_not_source": True,
        "command_output_is_non_authoritative": True,
    }


def result_limits() -> dict:
    return {
        "result_limits_declared": True,
        "command_result_not_created": True,
        "command_result_is_not_authority": True,
    }


def success_limits() -> dict:
    return {
        "success_limits_declared": True,
        "command_success_not_created": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
    }


def refusal_conditions() -> dict:
    return {
        "refusal_conditions_declared": True,
        "refuse_if_full_artifact_bodies_required": True,
        "refuse_if_artifact_mutation_required": True,
        "refuse_if_execution_would_create_authority_currentness_final_completion": True,
    }


def valid_request(extra: dict | None = None) -> dict:
    request = {
        "command_execution_boundary_request_id": (
            "portable_source_body_verification_command_execution_boundary_reference_review_001"
        ),
        "command_execution_boundary_question": QUESTION,
        "command_execution_boundary_intent": (
            "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY"
        ),
        "selected_command_report_basis": selected_command_report_basis(),
        "selected_command_implementation_basis": selected_command_implementation_basis(),
        "selected_command_implementation_boundary_basis": (
            selected_command_implementation_boundary_basis()
        ),
        "selected_command_boundary_basis": selected_command_boundary_basis(),
        "selected_artifact_emission_containment_basis": (
            selected_artifact_emission_containment_basis()
        ),
        "selected_evidence_manifest_basis": selected_evidence_manifest_basis(),
        "selected_portable_verification_basis": selected_portable_verification_basis(),
        "selected_command_module_reference": selected_command_module_reference(),
        "selected_test_surface_reference": selected_test_surface_reference(),
        "proposed_execution_mode": proposed_execution_mode(),
        "proposed_invocation_surface": proposed_invocation_surface(),
        "proposed_input_reference_bundle": proposed_input_reference_bundle(),
        "proposed_output_report_destination": proposed_output_report_destination(),
        "execution_limits": execution_limits(),
        "output_limits": output_limits(),
        "result_limits": result_limits(),
        "success_limits": success_limits(),
        "refusal_conditions": refusal_conditions(),
        "non_authority_posture": {
            "non_authority_posture_declared": True,
            "command_output_is_not_source": True,
            "command_result_is_not_authority": True,
        },
        "non_currentness_posture": {
            "non_currentness_posture_declared": True,
            "command_success_is_not_currentness": True,
        },
        "non_final_completion_posture": {
            "non_final_completion_posture_declared": True,
            "command_success_is_not_final_completion": True,
        },
        "execution_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_command_execution_boundary_outcome": RECORDED,
        "declared_non_claims": required_false_non_claims(),
    }
    if extra:
        request.update(extra)
    return request


class PortableSourceBodyVerificationCommandExecutionBoundaryTests(unittest.TestCase):
    def assert_recorded_result(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        summary = result["portable_source_body_verification_command_execution_boundary_summary"]
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertGreater(summary["passed_check_count"], 0)

        statement = result["execution_boundary_statement"]
        self.assertTrue(
            statement["portable_source_body_verification_command_execution_boundary_recorded"]
        )
        self.assertTrue(statement["command_execution_conditions_declared"])
        self.assertTrue(statement["command_invocation_must_be_bounded"])
        self.assertTrue(statement["command_output_must_be_non_authoritative"])
        self.assertTrue(statement["command_success_must_not_create_currentness"])
        self.assertTrue(statement["command_success_must_not_claim_final_completion"])
        self.assertTrue(statement["execution_boundary_only"])
        self.assertTrue(statement["command_execution_not_performed"])
        self.assertTrue(statement["command_invocation_not_created"])
        self.assertTrue(statement["command_output_not_created"])
        self.assertTrue(statement["command_result_not_created"])
        self.assertTrue(statement["command_success_not_created"])
        self.assertTrue(statement["command_output_is_not_source"])
        self.assertTrue(statement["command_result_is_not_authority"])
        self.assertTrue(statement["command_success_is_not_currentness"])
        self.assertTrue(statement["command_success_is_not_final_completion"])
        self.assertTrue(statement["execution_requires_reference_shaped_input"])
        self.assertTrue(statement["execution_must_not_mutate_artifacts"])
        self.assertTrue(statement["execution_must_not_embed_full_prior_artifacts"])

        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_execution_boundary_recorded_result(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            declared_command_execution_boundary_request=valid_request()
        )
        self.assert_recorded_result(result)
        self.assertEqual(OUTCOME_FAMILY, resolver.OUTCOME_FAMILY)

        self.assertTrue(result["selected_command_report_basis"]["selected_command_report_basis_preserved"])
        self.assertTrue(
            result["selected_command_implementation_basis"][
                "selected_command_implementation_basis_preserved"
            ]
        )
        self.assertTrue(
            result["selected_artifact_emission_containment_basis"][
                "selected_artifact_emission_containment_basis_preserved"
            ]
        )
        self.assertTrue(result["execution_limits"]["execution_limits_declared"])
        self.assertTrue(result["output_limits"]["output_limits_declared"])
        self.assertTrue(result["result_limits"]["result_limits_declared"])
        self.assertTrue(result["success_limits"]["success_limits_declared"])
        self.assertEqual(
            result["output_limits"]["output_limits_posture"]["non_authority_posture_declared"],
            True,
        )
        self.assertEqual(
            result["result_limits"]["result_limits_posture"]["non_currentness_posture_declared"],
            True,
        )
        self.assertEqual(
            result["success_limits"]["success_limits_posture"][
                "non_final_completion_posture_declared"
            ],
            True,
        )

    def test_metadata(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            valid_request()
        )
        metadata = result["portable_source_body_verification_command_execution_boundary_metadata"]
        self.assertTrue(metadata["portable_source_body_verification_command_execution_boundary_result_id"])
        self.assertTrue(metadata["portable_source_body_verification_command_execution_boundary_result_type"])
        self.assertEqual(
            metadata["portable_source_body_verification_command_execution_boundary_result_version"],
            "0.1.0",
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_command_execution_boundary",
        )

    def test_execution_boundary_checks(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            valid_request()
        )
        checks = result["execution_boundary_checks"]
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
            "execution_boundary_question_declared",
            "execution_boundary_intent_supported",
            "selected_command_report_basis_declared",
            "selected_command_implementation_basis_declared",
            "selected_command_implementation_boundary_basis_declared",
            "selected_command_boundary_basis_declared",
            "artifact_emission_containment_basis_declared",
            "evidence_manifest_basis_declared",
            "portable_verification_basis_declared",
            "command_module_reference_declared",
            "test_surface_reference_declared",
            "proposed_execution_mode_declared",
            "proposed_invocation_surface_declared",
            "proposed_input_reference_bundle_declared",
            "proposed_output_report_destination_declared",
            "execution_limits_declared",
            "output_limits_declared",
            "result_limits_declared",
            "success_limits_declared",
            "refusal_conditions_declared",
            "execution_boundary_scope_supported",
            "command_execution_not_performed",
            "command_invocation_not_created",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_output_not_source",
            "command_result_not_authority",
            "command_success_not_currentness",
            "command_success_not_final_completion",
            "execution_not_deployment_runtime_public_release",
            "execution_does_not_authorize_continuation_follow_on_work",
            "execution_requires_reference_shaped_input",
            "execution_must_not_mutate_artifacts",
            "execution_must_not_embed_full_prior_artifacts",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_names.issubset(check_names))

    def test_execution_boundary_non_meaning(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            valid_request()
        )
        non_meaning = result["execution_boundary_non_meaning"]
        expected = {
            "execution_boundary_does_not_mean_command_executed",
            "execution_boundary_does_not_mean_command_invoked",
            "execution_boundary_does_not_mean_command_output_exists",
            "execution_boundary_does_not_mean_command_result_exists",
            "execution_boundary_does_not_mean_command_success_exists",
            "execution_boundary_does_not_mean_command_output_became_source",
            "execution_boundary_does_not_mean_command_result_became_authority",
            "execution_boundary_does_not_mean_command_success_created_currentness",
            "execution_boundary_does_not_mean_command_success_claimed_final_completion",
            "execution_boundary_does_not_mean_live_verification_completed",
            "execution_boundary_does_not_mean_deployment_created",
            "execution_boundary_does_not_mean_runtime_hosting_created",
            "execution_boundary_does_not_mean_public_release_created",
            "execution_boundary_does_not_mean_public_readiness_created",
            "execution_boundary_does_not_mean_operation_permission_created",
            "execution_boundary_does_not_mean_continuation_authorized",
            "execution_boundary_does_not_mean_reusable_permission_created",
            "execution_boundary_does_not_mean_derivative_reception_authorized",
            "execution_boundary_does_not_mean_vessel_relation_authorized",
            "execution_boundary_does_not_mean_another_reception_request_authorized",
            "execution_boundary_does_not_mean_follow_on_work_authorized",
        }
        self.assertTrue(expected.issubset(non_meaning))
        for key in expected:
            self.assertTrue(non_meaning[key], key)

    def test_requires_additional_basis_and_not_recorded(self) -> None:
        additional_request = valid_request(
            {
                "requested_command_execution_boundary_outcome": REQUIRES_ADDITIONAL_BASIS,
                "additional_basis_context": {
                    "missing_basis": "proposed output/report destination precision"
                },
            }
        )
        additional = resolve_portable_source_body_verification_command_execution_boundary(
            additional_request
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"]["missing_basis"],
            "proposed output/report destination precision",
        )
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["additional_basis_not_executed"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(additional["non_claims"][key], False, key)

        not_recorded_request = valid_request(
            {
                "requested_command_execution_boundary_outcome": NOT_RECORDED,
                "not_recorded_basis": {
                    "reason": "execution boundary cannot be bounded from supplied basis"
                },
            }
        )
        not_recorded = resolve_portable_source_body_verification_command_execution_boundary(
            not_recorded_request
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"]["reason"],
            "execution boundary cannot be bounded from supplied basis",
        )
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_run_command"])
        self.assertTrue(
            not_recorded["not_recorded_basis"][
                "not_recorded_does_not_repair_or_authorize_execution"
            ]
        )
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(not_recorded["non_claims"][key], False, key)

    def test_what_remains_open(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            valid_request()
        )
        remains = result["what_remains_open"]
        expected_items = {
            "command execution boundary test",
            "command execution boundary live artifact",
            "actual command invocation",
            "command output from live execution",
            "command result from live execution",
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
        }
        self.assertTrue(expected_items.issubset(set(remains["open_items"])))
        self.assertTrue(remains["open_means_not_scheduled"])
        self.assertTrue(remains["open_means_not_authorized"])
        self.assertTrue(remains["open_means_not_executed"])

    def test_summary_helper(self) -> None:
        result = resolve_portable_source_body_verification_command_execution_boundary(
            valid_request()
        )
        summary = build_portable_source_body_verification_command_execution_boundary_summary(
            result
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["command_execution_boundary_request_id"],
            "portable_source_body_verification_command_execution_boundary_reference_review_001",
        )
        self.assertEqual(summary["command_execution_boundary_question"], QUESTION)
        self.assertEqual(
            summary["command_execution_boundary_intent"],
            "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY",
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "execution_boundary_recorded",
            "command_execution_conditions_declared",
            "command_invocation_must_be_bounded",
            "command_output_must_be_non_authoritative",
            "command_success_must_not_create_currentness",
            "command_success_must_not_claim_final_completion",
            "selected_command_report_basis_preserved",
            "selected_command_implementation_basis_preserved",
            "selected_command_implementation_boundary_basis_preserved",
            "selected_command_boundary_basis_preserved",
            "artifact_emission_containment_basis_preserved",
            "evidence_manifest_basis_preserved",
            "portable_verification_basis_preserved",
            "execution_boundary_only",
            "command_execution_not_performed",
            "command_invocation_not_created",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_output_not_source",
            "command_result_not_authority",
            "command_success_not_currentness",
            "command_success_not_final_completion",
            "execution_not_deployment",
            "execution_not_runtime_hosting",
            "execution_not_public_release",
            "execution_requires_reference_shaped_input",
            "no_full_prior_artifacts_embedded",
            "no_artifact_mutation",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_derivative_reception_vessel_relation_another_request_follow_on_work",
        ):
            self.assertTrue(summary[key], key)
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_request_builder_helper(self) -> None:
        request = build_declared_portable_source_body_verification_command_execution_boundary_request(
            "builder_request_001",
            QUESTION,
            selected_command_report_basis(),
            selected_command_implementation_basis(),
            selected_command_implementation_boundary_basis(),
            selected_command_boundary_basis(),
            selected_artifact_emission_containment_basis(),
            selected_evidence_manifest_basis(),
            selected_portable_verification_basis(),
            proposed_execution_mode(),
            proposed_invocation_surface(),
            proposed_input_reference_bundle(),
            proposed_output_report_destination(),
            execution_limits(),
            output_limits(),
            result_limits(),
            success_limits(),
            refusal_conditions(),
            list(SUPPORTED_SCOPE),
            additional_basis_context={"basis": "kept"},
            not_recorded_basis={"reason": "kept"},
        )
        self.assertEqual(request["command_execution_boundary_request_id"], "builder_request_001")
        self.assertEqual(request["command_execution_boundary_question"], QUESTION)
        self.assertEqual(request["selected_command_report_basis"], selected_command_report_basis())
        self.assertEqual(request["selected_command_implementation_basis"], selected_command_implementation_basis())
        self.assertEqual(
            request["selected_command_implementation_boundary_basis"],
            selected_command_implementation_boundary_basis(),
        )
        self.assertEqual(request["selected_command_boundary_basis"], selected_command_boundary_basis())
        self.assertEqual(
            request["selected_artifact_emission_containment_basis"],
            selected_artifact_emission_containment_basis(),
        )
        self.assertEqual(request["selected_evidence_manifest_basis"], selected_evidence_manifest_basis())
        self.assertEqual(request["selected_portable_verification_basis"], selected_portable_verification_basis())
        self.assertEqual(request["proposed_execution_mode"], proposed_execution_mode())
        self.assertEqual(request["proposed_invocation_surface"], proposed_invocation_surface())
        self.assertEqual(request["proposed_input_reference_bundle"], proposed_input_reference_bundle())
        self.assertEqual(
            request["proposed_output_report_destination"],
            proposed_output_report_destination(),
        )
        self.assertEqual(request["execution_limits"], execution_limits())
        self.assertEqual(request["output_limits"], output_limits())
        self.assertEqual(request["result_limits"], result_limits())
        self.assertEqual(request["success_limits"], success_limits())
        self.assertEqual(request["refusal_conditions"], refusal_conditions())
        self.assertEqual(set(request["execution_boundary_scope"]), set(SUPPORTED_SCOPE))
        self.assertEqual(request["requested_command_execution_boundary_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], {"basis": "kept"})
        self.assertEqual(request["not_recorded_basis"], {"reason": "kept"})
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = resolve_portable_source_body_verification_command_execution_boundary(
            request
        )
        self.assert_recorded_result(result)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = valid_request()
        mapping_result = resolve_portable_source_body_verification_command_execution_boundary(
            request
        )
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolve_portable_source_body_verification_command_execution_boundary_from_path(
                request_path
            )
            self.assert_recorded_result(path_result)
            self.assertEqual(set(mapping_result), set(path_result))
            self.assertEqual(
                path_result["declared_command_execution_boundary_question"][
                    "declared_command_execution_boundary_request_path"
                ],
                str(request_path),
            )

            output_path = tmp_path / "nested" / "explicit_result.json"
            written = write_portable_source_body_verification_command_execution_boundary_result(
                path_result, output_path
            )
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

            default_root = tmp_path / "execution_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_ROOT",
                default_root,
            ):
                first = write_portable_source_body_verification_command_execution_boundary_result(
                    path_result
                )
                second = write_portable_source_body_verification_command_execution_boundary_result(
                    path_result
                )
            self.assertTrue(str(first).startswith(str(default_root)))
            self.assertTrue(str(second).startswith(str(default_root)))
            self.assertNotEqual(first, second)
            self.assertIn(
                "portable_source_body_verification_command_execution_boundary_result.json",
                first.name,
            )
            self.assertIn("_001.json", second.name)
            self.assertNotIn("command_report", str(first))
            self.assertNotIn("deployment", str(first))
            self.assertNotIn("runtime", str(first))
            self.assertNotIn("public_release", str(first))

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        request_before = copy.deepcopy(request)
        selected_before = {
            key: copy.deepcopy(request[key])
            for key in (
                "selected_command_report_basis",
                "selected_command_implementation_basis",
                "selected_command_implementation_boundary_basis",
                "selected_command_boundary_basis",
                "selected_artifact_emission_containment_basis",
                "selected_evidence_manifest_basis",
                "selected_portable_verification_basis",
                "proposed_execution_mode",
                "proposed_invocation_surface",
                "proposed_input_reference_bundle",
                "proposed_output_report_destination",
                "execution_limits",
                "output_limits",
                "result_limits",
                "success_limits",
                "execution_boundary_scope",
            )
        }

        first = resolve_portable_source_body_verification_command_execution_boundary(request)
        second = resolve_portable_source_body_verification_command_execution_boundary(request)
        self.assert_recorded_result(first)
        self.assert_recorded_result(second)
        self.assertEqual(request, request_before)
        for key, before in selected_before.items():
            self.assertEqual(request[key], before, key)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "result.json"
            write_portable_source_body_verification_command_execution_boundary_result(
                first, output_path
            )
            self.assertTrue(output_path.exists())
            self.assertEqual(request, request_before)

    def test_missing_and_malformed_requests_block(self) -> None:
        missing = resolve_portable_source_body_verification_command_execution_boundary(None)
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(
            missing["block"]["block_code"],
            "COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED",
        )

        malformed = resolve_portable_source_body_verification_command_execution_boundary(
            "not a mapping"
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
        )

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            bad_json = tmp_path / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad_result = resolve_portable_source_body_verification_command_execution_boundary_from_path(
                bad_json
            )
            self.assertEqual(bad_result["outcome"], BLOCKED)
            self.assertEqual(
                bad_result["block"]["block_code"],
                "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_MALFORMED",
            )

            missing_path = tmp_path / "missing.json"
            unreadable = resolve_portable_source_body_verification_command_execution_boundary_from_path(
                missing_path
            )
            self.assertEqual(unreadable["outcome"], BLOCKED)
            self.assertEqual(
                unreadable["block"]["block_code"],
                "DECLARED_COMMAND_EXECUTION_BOUNDARY_REQUEST_UNREADABLE",
            )

    def test_missing_required_fields_block(self) -> None:
        cases = [
            ("command_execution_boundary_question", "COMMAND_EXECUTION_BOUNDARY_QUESTION_UNDECLARED"),
            ("selected_command_report_basis", "COMMAND_REPORT_BASIS_MISSING"),
            ("selected_command_implementation_basis", "COMMAND_IMPLEMENTATION_SPEC_MISSING"),
            (
                "selected_command_implementation_boundary_basis",
                "COMMAND_IMPLEMENTATION_BOUNDARY_BASIS_MISSING",
            ),
            ("selected_command_boundary_basis", "COMMAND_BOUNDARY_BASIS_MISSING"),
            (
                "selected_artifact_emission_containment_basis",
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            ("selected_evidence_manifest_basis", "EVIDENCE_MANIFEST_BASIS_MISSING"),
            ("selected_portable_verification_basis", "PORTABLE_VERIFICATION_BASIS_MISSING"),
            ("selected_command_module_reference", "COMMAND_MODULE_REFERENCE_MISSING"),
            ("selected_test_surface_reference", "TEST_SURFACE_REFERENCE_MISSING"),
            ("proposed_execution_mode", "PROPOSED_EXECUTION_MODE_MISSING"),
            ("proposed_invocation_surface", "PROPOSED_INVOCATION_SURFACE_MISSING"),
            ("proposed_input_reference_bundle", "PROPOSED_INPUT_REFERENCE_BUNDLE_MISSING"),
            (
                "proposed_output_report_destination",
                "PROPOSED_OUTPUT_REPORT_DESTINATION_MISSING",
            ),
            ("execution_limits", "EXECUTION_LIMITS_MISSING"),
            ("output_limits", "OUTPUT_LIMITS_MISSING"),
            ("result_limits", "RESULT_LIMITS_MISSING"),
            ("success_limits", "SUCCESS_LIMITS_MISSING"),
            ("refusal_conditions", "REFUSAL_CONDITIONS_MISSING"),
        ]
        for field, code in cases:
            with self.subTest(field=field):
                request = valid_request()
                request.pop(field)
                if field == "selected_command_module_reference":
                    request["selected_command_implementation_basis"] = {
                        "implementation_spec_declared": True
                    }
                if field == "selected_test_surface_reference":
                    request["selected_command_implementation_basis"] = {
                        "implementation_spec_declared": True,
                        "selected_command_module_reference": (
                            "src/portable_source_body_verification_command.py"
                        ),
                    }
                result = resolve_portable_source_body_verification_command_execution_boundary(
                    request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], code)

        unsupported = valid_request({"execution_boundary_scope": ["UNSUPPORTED_SCOPE"]})
        unsupported_result = resolve_portable_source_body_verification_command_execution_boundary(
            unsupported
        )
        self.assertEqual(unsupported_result["outcome"], BLOCKED)
        self.assertEqual(
            unsupported_result["block"]["block_code"],
            "UNSUPPORTED_COMMAND_EXECUTION_BOUNDARY_SCOPE",
        )

    def test_explicit_block_intent(self) -> None:
        request = valid_request(
            {
                "command_execution_boundary_intent": (
                    "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_EXECUTION_BOUNDARY_REVIEW"
                )
            }
        )
        result = resolve_portable_source_body_verification_command_execution_boundary(
            request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "COMMAND_EXECUTION_BOUNDARY_REVIEW_EXPLICITLY_BLOCKED",
        )

    def test_blocking_collapse_flags(self) -> None:
        cases = [
            ("command_executed", "COMMAND_EXECUTION_PERFORMED"),
            ("command_invocation_created", "COMMAND_INVOCATION_CREATED"),
            ("command_output_created", "COMMAND_OUTPUT_CREATED"),
            ("command_result_created", "COMMAND_RESULT_CREATED"),
            ("command_success_created", "COMMAND_SUCCESS_CREATED"),
            ("command_output_became_source", "COMMAND_OUTPUT_TREATED_AS_SOURCE"),
            ("command_result_became_authority", "COMMAND_RESULT_TREATED_AS_AUTHORITY"),
            ("command_success_created_currentness", "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"),
            (
                "command_success_claimed_final_completion",
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            ),
            ("prior_artifacts_mutated", "ARTIFACTS_MUTATED"),
            ("full_prior_artifacts_embedded", "FULL_PRIOR_ARTIFACTS_EMBEDDED"),
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
                request = valid_request({flag: True})
                result = resolve_portable_source_body_verification_command_execution_boundary(
                    request
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], code)

    def test_full_artifact_body_is_not_embedded(self) -> None:
        request = valid_request()
        request["selected_command_report_basis"] = selected_command_report_basis(
            {"full_artifact_body": "x" * 5000}
        )
        result = resolve_portable_source_body_verification_command_execution_boundary(
            request
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], "FULL_PRIOR_ARTIFACTS_EMBEDDED")
        self.assertNotIn("x" * 5000, json.dumps(result))
        self.assertIs(result["non_claims"]["prior_artifacts_mutated"], False)

    def test_mutation_replay_merge_and_non_claim_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                result = resolve_portable_source_body_verification_command_execution_boundary(
                    valid_request({flag: True})
                )
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(
                    result["block"]["block_code"],
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claim = valid_request()
        missing_non_claim["declared_non_claims"].pop("command_executed")
        missing_result = resolve_portable_source_body_verification_command_execution_boundary(
            missing_non_claim
        )
        self.assertEqual(missing_result["outcome"], BLOCKED)
        self.assertEqual(missing_result["block"]["block_code"], "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = valid_request()
        flipped_non_claim["declared_non_claims"]["command_executed"] = True
        flipped_result = resolve_portable_source_body_verification_command_execution_boundary(
            flipped_non_claim
        )
        self.assertEqual(flipped_result["outcome"], BLOCKED)
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"COMMAND_EXECUTION_PERFORMED", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_source_safety_check(self) -> None:
        source = (SRC_ROOT / "resolve_portable_source_body_verification_command_execution_boundary.py").read_text(
            encoding="utf-8"
        )
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
