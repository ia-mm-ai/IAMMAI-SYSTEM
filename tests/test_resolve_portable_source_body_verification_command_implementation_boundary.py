"""Bounded tests for the portable verification command implementation boundary.

These tests prove only the command implementation-boundary. The boundary
records conditions for a future checker-only implementation; it is not command
implementation, command execution, command invocation, command output, command
result, command success, manifest, checksum, signature, packet, deployment,
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

import resolve_portable_source_body_verification_command_implementation_boundary as resolver  # noqa: E402


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTPUT_FALSE_POSTURE = tuple(resolver.OUTPUT_FALSE_POSTURE)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_command_implementation_boundary_metadata",
    "declared_command_implementation_boundary_question",
    "selected_command_boundary_basis",
    "selected_artifact_emission_containment_basis",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "checker_only_implementation_basis",
    "implementation_limits",
    "output_limits",
    "execution_limits",
    "implementation_boundary_scope",
    "implementation_boundary_checks",
    "implementation_boundary_statement",
    "implementation_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_implementation_boundary_summary",
}

QUESTION = (
    "Can conditions for a future checker-only portable source-body "
    "verification command implementation be bounded without implementing, "
    "executing, invoking, or authorizing the command?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def selected_command_boundary_basis(extra: dict | None = None) -> dict:
    basis = {
        "selected_result_id": "portable_source_body_verification_command_boundary_reference_review_001_contained",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_command_boundary/portable_source_body_verification_command_"
            "boundary_reference_review_001_contained__portable_source_body_verification_"
            "command_boundary_result.json"
        ),
        "selected_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED"
        ),
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 52,
        "selected_result_summary": {
            "portable_source_body_verification_command_boundary_recorded": True,
            "verification_command_checker_role_bounded": True,
            "command_requires_declared_evidence_manifest": True,
        },
        "selected_result_non_claims": {
            "command_implemented": False,
            "command_executed": False,
            "command_output_created": False,
            "command_success_created": False,
            "deployment_created": False,
            "runtime_hosting_created": False,
            "public_release_created": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": "command-boundary:reference-review-001-contained",
        "selected_result_artifact_family": (
            "portable_source_body_verification_command_boundary"
        ),
        "selected_result_artifact_size_class": "contained-kb-level",
        "command_boundary_recorded_posture": True,
        "command_boundary_remains_checker_only_posture": True,
        "command_boundary_did_not_authorize_command_implementation": True,
        "command_boundary_did_not_authorize_command_execution": True,
        "command_boundary_did_not_create_command_output_success": True,
        "command_boundary_did_not_create_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
        "selected_basis_is_reference_shaped": True,
    }
    if extra:
        basis.update(extra)
    return basis


def selected_artifact_emission_containment_basis() -> dict:
    return {
        "selected_result_id": "artifact_emission_containment_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_artifact_emission_"
            "containment_boundary/artifact_emission_containment_reference_review_001__"
            "artifact_emission_containment_result.json"
        ),
        "selected_result_outcome": "ARTIFACT_EMISSION_CONTAINMENT_RECORDED",
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 32,
        "selected_result_summary": {
            "artifact_emission_containment_recorded": True,
            "reference_only_selected_basis_required": True,
            "recursive_full_artifact_embedding_blocked": True,
            "summary_plus_reference_emission_required": True,
            "prior_artifacts_preserved_by_reference": True,
        },
        "selected_result_non_claims": {
            "prior_artifacts_mutated": False,
            "prior_artifacts_invalidated_by_size": False,
            "command_implemented": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": "artifact-emission-containment:reference-review-001",
        "selected_result_artifact_family": "artifact_emission_containment_boundary",
        "selected_result_artifact_size_class": "contained-reference-shape",
        "containment_recorded_posture": True,
        "reference_only_selected_basis_required": True,
        "recursive_full_artifact_embedding_blocked": True,
        "summary_plus_reference_emission_required": True,
        "prior_artifacts_preserved_by_reference": True,
        "existing_artifacts_not_mutated": True,
        "existing_artifacts_not_invalidated_by_size": True,
        "contained_artifact_emission_required_for_future_implementation_boundary_artifacts": True,
    }


def selected_evidence_manifest_basis() -> dict:
    return {
        "selected_result_id": "portable_source_body_verification_evidence_manifest_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_evidence_manifest_boundary/portable_source_body_verification_"
            "evidence_manifest_reference_review_001__portable_source_body_verification_"
            "evidence_manifest_result.json"
        ),
        "selected_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED"
        ),
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 47,
        "selected_result_summary": {
            "evidence_manifest_recorded": True,
            "required_evidence_classes_declared": True,
        },
        "selected_result_non_claims": {
            "command_implemented": False,
            "command_executed": False,
            "command_output_created": False,
            "source_transferred": False,
            "source_received": False,
            "deployment_created": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": "evidence-manifest:reference-review-001",
        "selected_result_artifact_family": (
            "portable_source_body_verification_evidence_manifest_boundary"
        ),
        "selected_result_artifact_size_class": "standing-heavy-reference",
        "evidence_manifest_recorded_posture": True,
        "evidence_manifest_remains_evidence_only": True,
        "evidence_manifest_does_not_authorize_implementation_execution_output_success": True,
        "evidence_manifest_does_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
        "reference_shaped_basis_only": True,
        "declared_evidence_classes": selected_required_evidence_classes(),
        "required_surfaces": selected_required_surfaces(),
    }


def selected_portable_verification_basis() -> dict:
    return {
        "selected_result_id": "portable_source_body_verification_reference_review_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_boundary/portable_source_body_verification_reference_review_001__"
            "portable_source_body_verification_result.json"
        ),
        "selected_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 44,
        "selected_result_summary": {
            "portable_verification_recorded": True,
            "carrier_independent_verification_recorded": True,
        },
        "selected_result_non_claims": {
            "command_implemented": False,
            "command_executed": False,
            "command_output_created": False,
            "source_transferred": False,
            "source_received": False,
            "deployment_created": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": "portable-verification:reference-review-001",
        "selected_result_artifact_family": "portable_source_body_verification_boundary",
        "selected_result_artifact_size_class": "standing-heavy-reference",
        "portable_verification_recorded_posture": True,
        "portable_verification_remains_verification_only": True,
        "portable_verification_does_not_authorize_implementation_execution_output_success": True,
        "portable_verification_does_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_follow_on_work": True,
        "reference_shaped_basis_only": True,
    }


def selected_required_evidence_classes() -> dict:
    return {
        "selected_required_evidence_classes_declared": True,
        "required_source_surfaces": ["reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md"],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_V0_MIN_SPEC.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_V0_MIN_SPEC.md",
            "spec/ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_V0_MIN_SPEC.md",
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_command_implementation_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_command_implementation_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_boundary/",
            "artifacts/integrity_host_v0_min_coexistence_artifact_emission_containment_boundary/",
        ],
        "required_closure_artifacts": [
            "portable_source_body_verification_command_boundary_reference_review_001_contained__portable_source_body_verification_command_boundary_result.json"
        ],
        "required_terminal_summaries": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ],
        "evidence_classes_are_evidence_only": True,
        "evidence_classes_do_not_authorize_implementation_or_execution": True,
    }


def selected_required_surfaces() -> dict:
    return {
        "selected_required_surfaces_declared": True,
        "required_source_surfaces": ["reference/IAMMAI/RANKED_SURFACE_INDEX.md"],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_V0_MIN_SPEC.md"
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_command_implementation_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_command_implementation_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_command_implementation_boundary/"
        ],
        "required_closure_artifacts": [],
        "required_terminal_summaries": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ],
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_source_authority_currentness_permission_command_execution_deployment_public_release": True,
    }


def selected_reference_shaped_input_requirements() -> dict:
    return {
        "selected_reference_shaped_input_requirements_declared": True,
        "contained_reference_shape_required": True,
        "full_prior_artifacts_embedded": False,
        "future_selected_results_represented_by_reference_records": True,
        "reference_records_do_not_become_source": True,
        "summaries_do_not_become_source": True,
        "paths_do_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
    }


def checker_only_implementation_basis() -> dict:
    return {
        "checker_only_implementation_basis_declared": True,
        "future_code_may_only_inspect_declared_evidence_if_separately_implemented": True,
        "future_code_may_only_report_bounded_findings_if_separately_implemented_and_separately_executed": True,
        "implementation_must_require_declared_evidence_manifest_basis": True,
        "implementation_must_require_contained_reference_shape": True,
        "implementation_must_not_embed_full_prior_artifacts": True,
        "implementation_must_not_mutate_artifacts": True,
        "implementation_must_not_create_authority_currentness_final_completion": True,
        "execution_remains_separate_future_boundary": True,
        "contained_artifact_emission_posture": contained_artifact_emission_posture(),
    }


def no_command_authority_posture() -> dict:
    return {
        "no_command_authority_posture_declared": True,
        "command_does_not_become_authority": True,
    }


def no_output_source_posture() -> dict:
    return {
        "no_output_source_posture_declared": True,
        "command_output_does_not_become_source": True,
    }


def no_success_currentness_posture() -> dict:
    return {
        "no_success_currentness_posture_declared": True,
        "command_success_does_not_create_currentness": True,
    }


def no_success_final_completion_posture() -> dict:
    return {
        "no_success_final_completion_posture_declared": True,
        "command_success_does_not_claim_final_completion": True,
    }


def contained_artifact_emission_posture() -> dict:
    return {
        "contained_artifact_emission_posture_declared": True,
        "reference_shape_required": True,
        "recursive_full_artifact_embedding_blocked": True,
        "full_prior_artifacts_embedded": False,
        "prior_artifacts_mutated": False,
    }


def implementation_limits() -> dict:
    return {
        "implementation_limits_declared": True,
        "implementation_boundary_only": True,
        "command_implementation_not_created": True,
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_is_not_authority": True,
        "command_requires_evidence_manifest": True,
        "command_requires_contained_reference_shape": True,
        "full_prior_artifact_embedding_blocked": True,
        "artifact_mutation_blocked": True,
        "deployment_runtime_public_release_not_created": True,
        "source_transfer_migration_receipt_reception_authorization_not_created": True,
        "no_command_authority_posture": no_command_authority_posture(),
        "contained_artifact_emission_posture": contained_artifact_emission_posture(),
    }


def output_limits() -> dict:
    return {
        "output_limits_declared": True,
        "command_output_not_created": True,
        "command_result_not_created": True,
        "command_success_not_created": True,
        "command_output_is_not_source": True,
        "command_output_is_not_authority": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_output_cannot_create_operation_permission_public_readiness_continuation_follow_on_work": True,
        "no_output_source_posture": no_output_source_posture(),
        "no_success_currentness_posture": no_success_currentness_posture(),
        "no_success_final_completion_posture": no_success_final_completion_posture(),
    }


def execution_limits() -> dict:
    return {
        "execution_limits_declared": True,
        "command_execution_not_authorized": True,
        "command_invocation_not_created": True,
        "command_authorized_to_run": False,
        "execution_requires_separate_boundary": True,
        "execution_cannot_be_inferred_from_implementation_boundary": True,
        "execution_cannot_create_output_success_currentness_final_completion_here": True,
    }


def declared_request(**overrides: object) -> dict:
    request = {
        "command_implementation_boundary_request_id": "command-implementation-boundary-review-001",
        "command_implementation_boundary_question": QUESTION,
        "command_implementation_boundary_intent": resolver.INTENT_RECORD,
        "selected_command_boundary_basis": selected_command_boundary_basis(),
        "selected_command_boundary_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_command_boundary/portable_source_body_verification_command_"
            "boundary_reference_review_001_contained__portable_source_body_verification_"
            "command_boundary_result.json"
        ),
        "selected_command_boundary_result_id": (
            "portable_source_body_verification_command_boundary_reference_review_001_contained"
        ),
        "selected_command_boundary_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED"
        ),
        "selected_command_boundary_terminal_summary_path": (
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ),
        "selected_artifact_emission_containment_basis": selected_artifact_emission_containment_basis(),
        "selected_artifact_emission_containment_result_id": (
            "artifact_emission_containment_reference_review_001"
        ),
        "selected_artifact_emission_containment_result_outcome": (
            "ARTIFACT_EMISSION_CONTAINMENT_RECORDED"
        ),
        "selected_evidence_manifest_basis": selected_evidence_manifest_basis(),
        "selected_evidence_manifest_result_id": (
            "portable_source_body_verification_evidence_manifest_reference_review_001"
        ),
        "selected_evidence_manifest_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED"
        ),
        "selected_portable_verification_basis": selected_portable_verification_basis(),
        "selected_portable_verification_result_id": (
            "portable_source_body_verification_reference_review_001"
        ),
        "selected_portable_verification_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED"
        ),
        "selected_required_evidence_classes": selected_required_evidence_classes(),
        "selected_required_surfaces": selected_required_surfaces(),
        "selected_reference_shaped_input_requirements": (
            selected_reference_shaped_input_requirements()
        ),
        "checker_only_implementation_basis": checker_only_implementation_basis(),
        "implementation_limits": implementation_limits(),
        "output_limits": output_limits(),
        "execution_limits": execution_limits(),
        "no_command_authority_posture": no_command_authority_posture(),
        "no_output_source_posture": no_output_source_posture(),
        "no_success_currentness_posture": no_success_currentness_posture(),
        "no_success_final_completion_posture": no_success_final_completion_posture(),
        "contained_artifact_emission_posture": contained_artifact_emission_posture(),
        "implementation_boundary_scope": list(SUPPORTED_SCOPE),
        "requested_command_implementation_boundary_outcome": RECORDED,
        "declared_non_claims": required_false_non_claims(),
    }
    request.update(overrides)
    return request


def without_fields(request: dict, *fields: str) -> dict:
    result = copy.deepcopy(request)
    for field in fields:
        result.pop(field, None)
    return result


class PortableSourceBodyVerificationCommandImplementationBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_portable_source_body_verification_command_implementation_boundary(
            declared_command_implementation_boundary_request=request
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result[
                "portable_source_body_verification_command_implementation_boundary_summary"
            ]["failed_check_count"],
            0,
        )
        self.assertTrue(
            all(check["passed"] is True for check in result["implementation_boundary_checks"])
        )

    def assert_required_non_claims_false(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        for key in OUTPUT_FALSE_POSTURE:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_command_or_downstream_flags(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in (
            "command_implemented",
            "command_executed",
            "command_authorized_to_run",
            "command_invocation_created",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "full_prior_artifacts_embedded",
            "prior_artifacts_mutated",
            "manifest_implemented",
            "checksum_implemented",
            "signature_implemented",
            "packet_implemented",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
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
            self.assertIs(non_claims[key], False, key)

    def assert_block_code(self, request: dict | None, code: str) -> None:
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], code)
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def test_successful_command_implementation_boundary_recorded_result(self) -> None:
        request = declared_request()
        request_before = copy.deepcopy(request)
        result = self.resolve(request)

        self.assert_recorded(result)
        self.assertEqual(request, request_before)
        statement = result["implementation_boundary_statement"]
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)
            self.assertIs(result["non_claims"][key], True, key)
        for key in (
            "selected_command_boundary_basis_preserved",
            "selected_artifact_emission_containment_basis_preserved",
            "selected_evidence_manifest_basis_preserved",
            "selected_portable_verification_basis_preserved",
            "checker_only_implementation_basis_declared",
            "implementation_limits_declared",
            "output_limits_declared",
            "execution_limits_declared",
            "implementation_boundary_only",
            "command_implementation_not_created",
            "command_execution_not_authorized",
            "command_invocation_not_created",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_output_is_not_source",
            "command_output_is_not_authority",
            "command_success_is_not_currentness",
            "command_success_is_not_final_completion",
            "command_is_not_authority",
            "command_requires_declared_evidence_manifest",
            "command_requires_contained_reference_shape",
            "command_must_not_embed_full_prior_artifacts",
            "command_must_not_mutate_artifacts",
            "execution_requires_separate_boundary",
            "recorded_true_fields_are_bounded_implementation_boundary_outcomes_only",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_required_non_claims_false(result)
        self.assert_no_command_or_downstream_flags(result)

    def test_metadata_and_declared_question_are_preserved(self) -> None:
        result = self.resolve(declared_request())
        metadata = result[
            "portable_source_body_verification_command_implementation_boundary_metadata"
        ]
        for key in (
            "portable_source_body_verification_command_implementation_boundary_result_id",
            "portable_source_body_verification_command_implementation_boundary_result_type",
            "portable_source_body_verification_command_implementation_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(
            metadata[
                "portable_source_body_verification_command_implementation_boundary_result_version"
            ],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        question = result["declared_command_implementation_boundary_question"]
        self.assertEqual(
            question["command_implementation_boundary_request_id"],
            "command-implementation-boundary-review-001",
        )
        self.assertEqual(question["command_implementation_boundary_question"], QUESTION)
        self.assertEqual(
            question["command_implementation_boundary_intent"], resolver.INTENT_RECORD
        )
        self.assertTrue(question["command_implementation_boundary_is_not_implementation"])
        self.assertTrue(question["command_is_not_executed"])
        self.assertTrue(question["command_output_is_not_source"])
        self.assertTrue(question["command_success_is_not_currentness"])
        self.assertTrue(question["command_success_is_not_final_completion"])
        self.assertTrue(question["command_execution_requires_separate_boundary"])

    def test_selected_bases_checker_basis_limits_and_scope_are_preserved(self) -> None:
        result = self.resolve(declared_request())
        command_basis = result["selected_command_boundary_basis"]
        containment_basis = result["selected_artifact_emission_containment_basis"]
        evidence_basis = result["selected_evidence_manifest_basis"]
        portable_basis = result["selected_portable_verification_basis"]
        checker_basis = result["checker_only_implementation_basis"]
        impl_limits = result["implementation_limits"]
        out_limits = result["output_limits"]
        exec_limits = result["execution_limits"]
        scope = result["implementation_boundary_scope"]

        self.assertEqual(
            command_basis["selected_command_boundary_result_id"],
            "portable_source_body_verification_command_boundary_reference_review_001_contained",
        )
        self.assertEqual(
            command_basis["selected_command_boundary_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED",
        )
        self.assertTrue(command_basis["selected_command_boundary_basis_is_reference_shaped"])
        self.assertTrue(command_basis["selected_command_boundary_full_artifact_body_not_embedded"])
        self.assertTrue(command_basis["command_boundary_remains_checker_only_posture"])
        self.assertTrue(command_basis["command_boundary_did_not_authorize_command_implementation"])
        self.assertTrue(command_basis["command_boundary_did_not_authorize_command_execution"])
        self.assertTrue(command_basis["command_boundary_did_not_create_command_output_or_success"])

        for key in (
            "reference_only_selected_basis_required",
            "recursive_full_artifact_embedding_blocked",
            "summary_plus_reference_emission_required",
            "prior_artifacts_preserved_by_reference",
            "existing_artifacts_not_mutated",
            "existing_artifacts_not_invalidated_by_size",
            "contained_artifact_emission_required_for_future_implementation_boundary_artifacts",
        ):
            self.assertIs(containment_basis[key], True, key)
        self.assertTrue(evidence_basis["basis_remains_evidence_only"])
        self.assertTrue(evidence_basis["basis_does_not_authorize_implementation_execution_output_success"])
        self.assertTrue(portable_basis["basis_remains_verification_only"])
        self.assertTrue(portable_basis["basis_does_not_authorize_implementation_execution_output_success"])

        for key in (
            "future_code_may_only_inspect_declared_evidence_if_separately_implemented",
            "future_code_may_only_report_bounded_findings_if_separately_implemented_and_separately_executed",
            "implementation_must_require_declared_evidence_manifest_basis",
            "implementation_must_require_contained_reference_shape",
            "implementation_must_not_embed_full_prior_artifacts",
            "implementation_must_not_mutate_artifacts",
            "implementation_must_not_create_authority_currentness_final_completion",
            "execution_remains_separate_future_boundary",
        ):
            self.assertIs(checker_basis[key], True, key)
        for key in (
            "implementation_boundary_only",
            "command_implementation_not_created",
            "command_execution_not_authorized",
            "command_invocation_not_created",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_is_not_authority",
            "command_requires_evidence_manifest",
            "command_requires_contained_reference_shape",
            "full_prior_artifact_embedding_blocked",
            "artifact_mutation_blocked",
            "deployment_runtime_public_release_not_created",
            "source_transfer_migration_receipt_reception_authorization_not_created",
        ):
            self.assertIs(impl_limits[key], True, key)
        for key in (
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_output_is_not_source",
            "command_output_is_not_authority",
            "command_success_is_not_currentness",
            "command_success_is_not_final_completion",
            "command_output_cannot_create_operation_permission_public_readiness_continuation_follow_on_work",
        ):
            self.assertIs(out_limits[key], True, key)
        self.assertTrue(exec_limits["command_execution_not_authorized"])
        self.assertTrue(exec_limits["command_invocation_not_created"])
        self.assertIs(exec_limits["command_authorized_to_run"], False)
        self.assertTrue(exec_limits["execution_requires_separate_boundary"])
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self.assertEqual(set(scope["selected_scope_values"]), set(SUPPORTED_SCOPE))

    def test_implementation_boundary_checks_are_explicit_and_pass_for_recorded_case(self) -> None:
        result = self.resolve(declared_request())
        checks = result["implementation_boundary_checks"]
        check_names = {check["check_name"] for check in checks}

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertIs(check["passed"], True, check["check_name"])
        self.assertEqual(
            result[
                "portable_source_body_verification_command_implementation_boundary_summary"
            ]["failed_check_count"],
            0,
        )
        expected_checks = {
            "implementation_boundary_question_declared",
            "implementation_boundary_intent_supported",
            "selected_command_boundary_basis_declared",
            "artifact_emission_containment_basis_declared",
            "evidence_manifest_basis_declared",
            "portable_verification_basis_declared",
            "required_evidence_classes_declared",
            "required_surfaces_declared",
            "reference_shaped_input_requirements_declared",
            "checker_only_implementation_basis_declared",
            "implementation_limits_declared",
            "output_limits_declared",
            "execution_limits_declared",
            "implementation_boundary_scope_supported",
            "no_command_authority_posture_declared",
            "no_output_source_posture_declared",
            "no_success_currentness_posture_declared",
            "no_success_final_completion_posture_declared",
            "contained_artifact_emission_posture_declared",
            "command_implementation_not_created",
            "command_execution_not_authorized",
            "command_invocation_not_created",
            "command_output_not_created",
            "command_result_not_created",
            "command_success_not_created",
            "command_output_not_source",
            "command_output_not_authority",
            "command_success_not_currentness",
            "command_success_not_final_completion",
            "command_not_authority",
            "full_prior_artifacts_not_embedded",
            "artifacts_not_mutated",
            "deployment_not_created",
            "runtime_hosting_not_created",
            "public_release_not_created",
            "source_transfer_not_created",
            "source_migration_not_created",
            "source_receipt_not_created",
            "reception_not_authorized",
            "operation_permission_not_created",
            "public_readiness_not_created",
            "final_completion_not_claimed",
            "continuation_not_authorized",
            "reusable_permission_not_created",
            "derivative_reception_not_authorized",
            "vessel_relation_not_authorized",
            "another_reception_request_not_authorized",
            "follow_on_work_not_authorized",
            "command_requires_declared_evidence_manifest",
            "command_requires_contained_reference_shape",
            "execution_requires_separate_boundary",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(expected_checks.issubset(check_names))

    def test_each_supported_scope_records_and_unsupported_scope_blocks(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            with self.subTest(scope=scope_value):
                self.assert_recorded(
                    self.resolve(declared_request(implementation_boundary_scope=[scope_value]))
                )
        self.assert_block_code(
            declared_request(
                implementation_boundary_scope=["COMMAND_IMPLEMENTATION_IS_DEPLOYMENT"]
            ),
            "UNSUPPORTED_COMMAND_IMPLEMENTATION_BOUNDARY_SCOPE",
        )

    def test_reference_shaped_containment_avoids_full_prior_artifact_embedding(self) -> None:
        sentinel = "FULL_PRIOR_ARTIFACT_SENTINEL_" + ("x" * 120000)
        request = declared_request(
            selected_command_boundary_basis=selected_command_boundary_basis(
                {
                    "full_artifact_body": sentinel,
                    "raw_result": {"full_artifact_body": sentinel},
                }
            )
        )
        result = self.resolve(request)
        serialized = json.dumps(result, sort_keys=True)
        command_basis = result["selected_command_boundary_basis"][
            "selected_command_boundary_basis_as_reference_shape"
        ]

        self.assert_recorded(result)
        self.assertNotIn(sentinel, serialized)
        self.assertNotIn('"full_artifact_body":', serialized)
        self.assertLess(len(serialized), len(sentinel))
        self.assertTrue(command_basis["full_artifact_body_not_embedded"])
        self.assertIn("full_artifact_body", command_basis["omitted_full_artifact_body_keys"])
        self.assertIs(result["non_claims"]["full_prior_artifacts_embedded"], False)
        self.assertTrue(
            result["implementation_boundary_statement"][
                "command_requires_contained_reference_shape"
            ]
        )
        self.assertTrue(
            result["implementation_boundary_statement"][
                "command_must_not_embed_full_prior_artifacts"
            ]
        )
        self.assertIs(result["non_claims"]["prior_artifacts_mutated"], False)

    def test_implementation_boundary_non_meaning_and_what_remains_open(self) -> None:
        result = self.resolve(declared_request())
        non_meaning = result["implementation_boundary_non_meaning"]
        for name in (
            "command_exists",
            "command_implemented",
            "command_can_run",
            "command_invocation_exists",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "command_success_creates_currentness",
            "command_success_creates_final_completion",
            "command_output_becomes_source",
            "command_output_becomes_authority",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "operation_permission_created",
            "public_readiness_created",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(
                non_meaning[f"implementation_boundary_does_not_mean_{name}"],
                True,
                name,
            )

        remains_open = result["what_remains_open"]
        for item in (
            "command implementation boundary test",
            "command implementation boundary live artifact",
            "actual command implementation",
            "command execution boundary",
            "command invocation",
            "command output",
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
        ):
            self.assertIn(item, remains_open["open_items"])
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_additional_basis_and_not_recorded_outcomes_do_not_authorize_work(self) -> None:
        additional_context = {
            "checker_only_implementation_basis_unclear": True,
            "execution_boundary_dependency_unclear": True,
        }
        additional = self.resolve(
            declared_request(
                requested_command_implementation_boundary_outcome=(
                    REQUIRES_ADDITIONAL_BASIS
                ),
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        self.assert_required_non_claims_false(additional)
        self.assert_no_command_or_downstream_flags(additional)

        not_recorded_basis = {
            "reason": "implementation boundary cannot be bounded",
            "repair_authorized": False,
            "next_work_authorized": False,
        }
        not_recorded = self.resolve(
            declared_request(
                requested_command_implementation_boundary_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_mutate"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_implement"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_execute"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_invoke"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_emit_output"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_create_success"])
        self.assert_required_non_claims_false(not_recorded)
        self.assert_no_command_or_downstream_flags(not_recorded)

        for result in (additional, not_recorded):
            for key in ALLOWED_RECORDED_TRUE_FIELDS:
                self.assertIs(result["implementation_boundary_statement"][key], False, key)
                self.assertIs(result["non_claims"][key], False, key)

    def test_summary_helper_preserves_command_implementation_boundary_posture(self) -> None:
        result = self.resolve(declared_request())
        summary = (
            resolver.build_portable_source_body_verification_command_implementation_boundary_summary(
                result
            )
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["command_implementation_boundary_request_id"],
            "command-implementation-boundary-review-001",
        )
        self.assertEqual(summary["command_implementation_boundary_question"], QUESTION)
        self.assertEqual(
            summary["command_implementation_boundary_intent"], resolver.INTENT_RECORD
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["command_implementation_boundary_recorded"])
        self.assertTrue(summary["checker_command_implementation_conditions_declared"])
        self.assertTrue(summary["command_implementation_must_be_checker_only"])
        self.assertTrue(summary["command_implementation_requires_contained_reference_shape"])
        self.assertTrue(summary["command_execution_requires_separate_boundary"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertTrue(summary["selected_command_boundary_basis_preserved"])
        self.assertTrue(summary["artifact_emission_containment_basis_preserved"])
        self.assertTrue(summary["evidence_manifest_basis_preserved"])
        self.assertTrue(summary["portable_verification_basis_preserved"])
        self.assertTrue(summary["checker_only_implementation_basis_declared"])
        self.assertTrue(summary["implementation_limits_declared"])
        self.assertTrue(summary["output_limits_declared"])
        self.assertTrue(summary["execution_limits_declared"])
        self.assertTrue(summary["implementation_boundary_only"])
        self.assertTrue(summary["command_implementation_not_created"])
        self.assertTrue(summary["command_execution_not_authorized"])
        self.assertTrue(summary["command_invocation_output_result_success_not_created"])
        self.assertTrue(summary["command_output_not_source_or_authority"])
        self.assertTrue(summary["command_success_not_currentness_or_final_completion"])
        self.assertTrue(summary["command_not_authority"])
        self.assertTrue(summary["command_requires_evidence_manifest_and_contained_reference_shape"])
        self.assertTrue(summary["no_full_prior_artifacts_embedded"])
        self.assertTrue(summary["no_artifact_mutation"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_permission_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_flow_reusable_permission"])
        self.assertTrue(
            summary[
                "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work"
            ]
        )
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_request_builder_helper_builds_bounded_recordable_request(self) -> None:
        additional_context = {"output_limits_unclear": True}
        not_recorded_basis = {"reason": "not used in recorded case"}
        request = (
            resolver.build_declared_portable_source_body_verification_command_implementation_boundary_request(
                "builder-command-implementation-boundary-001",
                QUESTION,
                selected_command_boundary_basis(),
                selected_artifact_emission_containment_basis(),
                selected_evidence_manifest_basis(),
                selected_portable_verification_basis(),
                checker_only_implementation_basis(),
                implementation_limits(),
                output_limits(),
                execution_limits(),
                list(SUPPORTED_SCOPE),
                selected_command_boundary_result_path="command_boundary_result.json",
                selected_command_boundary_result_id="command-boundary-id-from-builder",
                selected_command_boundary_result_outcome=(
                    "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_RECORDED"
                ),
                requested_command_implementation_boundary_outcome=RECORDED,
                additional_basis_context=additional_context,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(
            request["command_implementation_boundary_request_id"],
            "builder-command-implementation-boundary-001",
        )
        self.assertEqual(request["command_implementation_boundary_question"], QUESTION)
        self.assertEqual(
            request["selected_command_boundary_result_path"],
            "command_boundary_result.json",
        )
        self.assertEqual(
            request["selected_command_boundary_result_id"],
            "command-boundary-id-from-builder",
        )
        self.assertEqual(request["requested_command_implementation_boundary_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False, key)
        for key in (
            "command_implemented",
            "command_executed",
            "command_invocation_created",
            "command_output_created",
            "command_result_created",
            "command_success_created",
            "manifest_implemented",
            "checksum_implemented",
            "signature_implemented",
            "packet_implemented",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "operation_permission_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = self.resolve(request)
        self.assert_recorded(result)
        self.assertEqual(
            result["selected_command_boundary_basis"]["selected_command_boundary_result_id"],
            "command-boundary-id-from-builder",
        )

    def test_path_based_request_and_write_behavior_are_additive(self) -> None:
        request = declared_request()
        mapping_result = self.resolve(request)
        self.assert_recorded(mapping_result)

        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            request_path = tmp_dir / "requests" / "command_implementation_boundary_request.json"
            request_path.parent.mkdir(parents=True)
            request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")

            path_result = (
                resolver.resolve_portable_source_body_verification_command_implementation_boundary_from_path(
                    request_path
                )
            )
            self.assert_recorded(path_result)
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertEqual(
                path_result["declared_command_implementation_boundary_question"][
                    "request_path"
                ],
                str(request_path),
            )

            output_path = tmp_dir / "nested" / "command_implementation_boundary_result.json"
            written = (
                resolver.write_portable_source_body_verification_command_implementation_boundary_result(
                    path_result,
                    output_path,
                )
            )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

            original_root = str(
                resolver.PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_ROOT
            )
            self.assertIn("command_implementation_boundary", original_root)
            self.assertNotIn("command_execution", original_root)
            self.assertNotIn("manifest", original_root)
            self.assertNotIn("checksum", original_root)
            self.assertNotIn("packet", original_root)
            self.assertNotIn("deployment", original_root)
            self.assertNotIn("runtime", original_root)
            self.assertNotIn("public_release", original_root)

            patched_root = tmp_dir / "implementation-boundary-default-root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_IMPLEMENTATION_BOUNDARY_ROOT",
                patched_root,
            ):
                first = (
                    resolver.write_portable_source_body_verification_command_implementation_boundary_result(
                        path_result
                    )
                )
                second = (
                    resolver.write_portable_source_body_verification_command_implementation_boundary_result(
                        path_result
                    )
                )
            self.assertEqual(first.parent, patched_root)
            self.assertEqual(second.parent, patched_root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertTrue(
                first.name.endswith(
                    "__portable_source_body_verification_command_implementation_boundary_result.json"
                )
            )
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        snapshots = [
            (request, copy.deepcopy(request)),
            (request["selected_command_boundary_basis"], copy.deepcopy(request["selected_command_boundary_basis"])),
            (
                request["selected_artifact_emission_containment_basis"],
                copy.deepcopy(request["selected_artifact_emission_containment_basis"]),
            ),
            (request["selected_evidence_manifest_basis"], copy.deepcopy(request["selected_evidence_manifest_basis"])),
            (request["selected_portable_verification_basis"], copy.deepcopy(request["selected_portable_verification_basis"])),
            (request["checker_only_implementation_basis"], copy.deepcopy(request["checker_only_implementation_basis"])),
            (request["implementation_limits"], copy.deepcopy(request["implementation_limits"])),
            (request["output_limits"], copy.deepcopy(request["output_limits"])),
            (request["execution_limits"], copy.deepcopy(request["execution_limits"])),
            (request["implementation_boundary_scope"], copy.deepcopy(request["implementation_boundary_scope"])),
        ]

        first = self.resolve(request)
        second = self.resolve(request)
        self.assert_recorded(first)
        self.assert_recorded(second)
        for current, snapshot in snapshots:
            self.assertEqual(current, snapshot)

        with tempfile.TemporaryDirectory() as tmp_dir_name:
            output = Path(tmp_dir_name) / "additive" / "result.json"
            written = (
                resolver.write_portable_source_body_verification_command_implementation_boundary_result(
                    first,
                    output,
                )
            )
            self.assertTrue(written.exists())
            self.assertEqual(request, snapshots[0][1])

    def test_blocking_missing_malformed_and_unsupported_inputs(self) -> None:
        self.assert_block_code(
            declared_request(
                command_implementation_boundary_intent=resolver.INTENT_BLOCK
            ),
            "COMMAND_IMPLEMENTATION_BOUNDARY_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assert_block_code(None, "COMMAND_IMPLEMENTATION_BOUNDARY_QUESTION_UNDECLARED")

        malformed = (
            resolver.resolve_portable_source_body_verification_command_implementation_boundary(
                declared_command_implementation_boundary_request=["not", "a", "mapping"]
            )
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED",
        )

        missing_cases = (
            (
                (
                    "selected_command_boundary_basis",
                    "selected_command_boundary_result_path",
                    "selected_command_boundary_result_id",
                    "selected_command_boundary_result_outcome",
                    "selected_command_boundary_terminal_summary_path",
                ),
                "COMMAND_BOUNDARY_BASIS_MISSING",
            ),
            (
                (
                    "selected_artifact_emission_containment_basis",
                    "selected_artifact_emission_containment_result_id",
                    "selected_artifact_emission_containment_result_outcome",
                ),
                "ARTIFACT_EMISSION_CONTAINMENT_BASIS_MISSING",
            ),
            (
                (
                    "selected_evidence_manifest_basis",
                    "selected_evidence_manifest_result_id",
                    "selected_evidence_manifest_result_outcome",
                ),
                "EVIDENCE_MANIFEST_BASIS_MISSING",
            ),
            (
                (
                    "selected_portable_verification_basis",
                    "selected_portable_verification_result_id",
                    "selected_portable_verification_result_outcome",
                ),
                "PORTABLE_VERIFICATION_BASIS_MISSING",
            ),
            (("checker_only_implementation_basis",), "CHECKER_ONLY_IMPLEMENTATION_BASIS_MISSING"),
            (("implementation_limits",), "IMPLEMENTATION_LIMITS_MISSING"),
            (("output_limits",), "OUTPUT_LIMITS_MISSING"),
            (("execution_limits",), "EXECUTION_LIMITS_MISSING"),
        )
        for fields, code in missing_cases:
            with self.subTest(code=code):
                self.assert_block_code(without_fields(declared_request(), *fields), code)

        missing_classes = without_fields(
            declared_request(), "selected_required_evidence_classes"
        )
        missing_classes["selected_evidence_manifest_basis"].pop(
            "declared_evidence_classes", None
        )
        self.assert_block_code(missing_classes, "REQUIRED_EVIDENCE_CLASSES_MISSING")

        missing_surfaces = without_fields(
            declared_request(), "selected_required_surfaces"
        )
        missing_surfaces["selected_evidence_manifest_basis"].pop(
            "required_surfaces", None
        )
        self.assert_block_code(missing_surfaces, "REQUIRED_SURFACES_MISSING")
        self.assert_block_code(
            without_fields(declared_request(), "selected_reference_shaped_input_requirements"),
            "REFERENCE_SHAPED_INPUT_REQUIREMENTS_MISSING",
        )
        missing_authority = without_fields(
            declared_request(), "no_command_authority_posture"
        )
        missing_authority["implementation_limits"].pop(
            "no_command_authority_posture", None
        )
        self.assert_block_code(
            missing_authority, "NO_COMMAND_AUTHORITY_POSTURE_MISSING"
        )

        missing_output_source = without_fields(
            declared_request(), "no_output_source_posture"
        )
        missing_output_source["output_limits"].pop("no_output_source_posture", None)
        self.assert_block_code(
            missing_output_source, "NO_OUTPUT_SOURCE_POSTURE_MISSING"
        )

        missing_success_currentness = without_fields(
            declared_request(), "no_success_currentness_posture"
        )
        missing_success_currentness["output_limits"].pop(
            "no_success_currentness_posture", None
        )
        self.assert_block_code(
            missing_success_currentness, "NO_SUCCESS_CURRENTNESS_POSTURE_MISSING"
        )

        missing_success_completion = without_fields(
            declared_request(), "no_success_final_completion_posture"
        )
        missing_success_completion["output_limits"].pop(
            "no_success_final_completion_posture", None
        )
        self.assert_block_code(
            missing_success_completion, "NO_SUCCESS_FINAL_COMPLETION_POSTURE_MISSING"
        )

        missing_contained_emission = without_fields(
            declared_request(), "contained_artifact_emission_posture"
        )
        missing_contained_emission["implementation_limits"].pop(
            "contained_artifact_emission_posture", None
        )
        missing_contained_emission["checker_only_implementation_basis"].pop(
            "contained_artifact_emission_posture", None
        )
        self.assert_block_code(
            missing_contained_emission, "CONTAINED_ARTIFACT_EMISSION_POSTURE_MISSING"
        )

    def test_blocking_unreadable_and_malformed_request_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            missing = (
                resolver.resolve_portable_source_body_verification_command_implementation_boundary_from_path(
                    tmp_dir / "missing.json"
                )
            )
            self.assertEqual(missing["outcome"], BLOCKED)
            self.assertEqual(
                missing["block"]["block_code"],
                "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_UNREADABLE",
            )

            bad_json = tmp_dir / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = (
                resolver.resolve_portable_source_body_verification_command_implementation_boundary_from_path(
                    bad_json
                )
            )
            self.assertEqual(bad["outcome"], BLOCKED)
            self.assertEqual(
                bad["block"]["block_code"],
                "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED",
            )

            array_json = tmp_dir / "array.json"
            array_json.write_text(json.dumps(["not", "object"]), encoding="utf-8")
            array_result = (
                resolver.resolve_portable_source_body_verification_command_implementation_boundary_from_path(
                    array_json
                )
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_COMMAND_IMPLEMENTATION_BOUNDARY_REQUEST_MALFORMED",
            )

    def test_blocking_collapse_flags(self) -> None:
        collapse_cases = {
            "command_implemented": {"COMMAND_IMPLEMENTATION_CREATED"},
            "command_executed": {"COMMAND_EXECUTION_AUTHORIZED"},
            "command_authorized_to_run": {"COMMAND_EXECUTION_AUTHORIZED"},
            "command_invocation_created": {"COMMAND_INVOCATION_CREATED"},
            "command_output_created": {"COMMAND_OUTPUT_CREATED"},
            "command_result_created": {"COMMAND_RESULT_CREATED"},
            "command_success_created": {"COMMAND_SUCCESS_CREATED"},
            "command_output_became_source": {"COMMAND_OUTPUT_TREATED_AS_SOURCE"},
            "command_output_became_authority": {"COMMAND_OUTPUT_TREATED_AS_AUTHORITY"},
            "command_success_created_currentness": {"COMMAND_SUCCESS_TREATED_AS_CURRENTNESS"},
            "command_success_claimed_final_completion": {
                "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION"
            },
            "command_became_authority": {"COMMAND_TREATED_AS_AUTHORITY"},
            "full_prior_artifacts_embedded": {"FULL_PRIOR_ARTIFACT_EMBEDDING_PERMITTED"},
            "prior_artifacts_mutated": {"ARTIFACTS_MUTATED"},
            "manifest_implemented": {"MANIFEST_IMPLEMENTATION_CREATED"},
            "checksum_implemented": {"CHECKSUM_IMPLEMENTATION_CREATED"},
            "signature_implemented": {"SIGNATURE_IMPLEMENTATION_CREATED"},
            "packet_implemented": {"PACKET_IMPLEMENTATION_CREATED"},
            "deployment_created": {"DEPLOYMENT_CREATED"},
            "runtime_hosting_created": {"RUNTIME_HOSTING_CREATED"},
            "public_release_created": {"PUBLIC_RELEASE_CREATED"},
            "source_transferred": {"SOURCE_TRANSFER_CREATED"},
            "source_migrated": {"SOURCE_MIGRATION_CREATED"},
            "source_received": {"SOURCE_RECEIPT_CREATED"},
            "source_receipt_recorded": {"SOURCE_RECEIPT_CREATED"},
            "reception_authorized": {"RECEPTION_AUTHORIZED"},
            "operation_permission_created": {"OPERATION_PERMISSION_CREATED"},
            "public_launch_readiness_created": {"PUBLIC_READINESS_CREATED"},
            "continuation_authorized": {"CONTINUATION_AUTHORIZED"},
            "publication_flow_opened": {"CONTINUATION_AUTHORIZED"},
            "reusable_permission_created": {"REUSABLE_PERMISSION_CREATED"},
            "derivative_reception_authorized": {"DERIVATIVE_RECEPTION_AUTHORIZED"},
            "vessel_relation_authorized": {"VESSEL_RELATION_AUTHORIZED"},
            "another_reception_request_authorized": {
                "ANOTHER_RECEPTION_REQUEST_AUTHORIZED"
            },
            "follow_on_work_authorized": {"FOLLOW_ON_WORK_AUTHORIZED"},
            "path_created_currentness": {"PATH_TREATED_AS_CURRENTNESS"},
            "latest_file_created_currentness": {"LATEST_FILE_TREATED_AS_CURRENTNESS"},
            "artifact_existence_created_currentness": {
                "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"
            },
            "repository_copy_became_body": {"REPOSITORY_COPY_TREATED_AS_BODY"},
            "carrier_possession_created_currentness": {
                "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"
            },
            "narration_created_currentness": {"NARRATION_TREATED_AS_CURRENTNESS"},
        }
        for flag, expected_codes in collapse_cases.items():
            with self.subTest(flag=flag):
                result = self.resolve(declared_request(**{flag: True}))
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["block"]["block_code"], expected_codes)

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                self.assert_block_code(
                    declared_request(**{flag: True}),
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claim = declared_request()
        missing_non_claim["declared_non_claims"].pop("command_executed")
        self.assert_block_code(missing_non_claim, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = declared_request()
        flipped_non_claim["declared_non_claims"]["command_output_created"] = True
        result = self.resolve(flipped_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "COMMAND_OUTPUT_CREATED"},
        )


if __name__ == "__main__":
    unittest.main()
