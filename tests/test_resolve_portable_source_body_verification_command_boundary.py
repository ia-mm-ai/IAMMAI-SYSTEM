"""Bounded tests for the portable verification command-boundary resolver.

These tests prove only the command boundary. Command boundary records a future
checker-only command posture; it is not command implementation, command
execution, command output, command success, manifest, checksum, signature,
packet, runtime, deployment, public release, source transfer, migration, source
receipt, reception authorization, authority, currentness, continuation,
reusable permission, derivative reception, vessel relation, another reception
request, or follow-on work.
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

import resolve_portable_source_body_verification_command_boundary as resolver  # noqa: E402


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_COMMAND_BOUNDARY_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTPUT_FALSE_POSTURE = tuple(resolver.OUTPUT_FALSE_POSTURE)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_command_boundary_metadata",
    "declared_command_boundary_question",
    "selected_evidence_manifest_basis",
    "selected_portable_verification_basis",
    "checker_command_basis",
    "command_limits",
    "command_scope",
    "command_boundary_checks",
    "command_boundary_statement",
    "command_boundary_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_command_boundary_summary",
}

QUESTION = (
    "Can a future portable source-body verification command posture be "
    "bounded as checker-only without implementing or authorizing a command?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def selected_required_surfaces() -> dict:
    return {
        "required_source_surfaces": [
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            "reference/IAMMAI/RANKED_SURFACE_INDEX.md",
        ],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_V0_MIN_SPEC.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_V0_MIN_SPEC.md",
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_command_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_command_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_evidence_manifest_boundary/",
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_boundary/",
        ],
        "required_closure_artifacts": [
            "portable_source_body_verification_evidence_manifest_reference_review_001__portable_source_body_verification_evidence_manifest_result.json"
        ],
        "required_terminal_summaries": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ],
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_source": True,
        "surfaces_do_not_create_authority": True,
        "surfaces_do_not_create_currentness": True,
        "surfaces_do_not_create_permission": True,
        "surfaces_do_not_create_command_execution": True,
        "surfaces_do_not_create_deployment_or_public_release": True,
    }


def selected_evidence_classes() -> dict:
    return {
        "evidence_classes_declared": True,
        "evidence_classes": [
            "portable verification result",
            "portable verification terminal summary",
            "evidence-manifest result",
            "evidence-manifest terminal summary",
            "required source surfaces",
            "required spec surfaces",
            "required resolver surfaces",
            "required test surfaces",
            "required artifact roots",
            "required closure artifacts",
            "future command candidate",
        ],
        "evidence_classes_are_evidence_only": True,
        "evidence_classes_do_not_implement_command": True,
        "evidence_classes_do_not_authorize_command": True,
    }


def future_candidate_postures() -> dict:
    return {
        "manifest_candidate_future_only": True,
        "checksum_candidate_future_only": True,
        "signature_candidate_future_only": True,
        "packet_candidate_future_only": True,
        "command_candidate_future_only": True,
        "manifest_not_implemented": True,
        "checksum_not_implemented": True,
        "signature_not_implemented": True,
        "packet_not_implemented": True,
        "command_not_implemented": True,
        "command_not_authorized": True,
        "command_requires_separate_boundary": True,
        "candidates_are_not_source": True,
        "candidates_are_not_authority": True,
        "candidates_are_not_currentness": True,
        "candidates_are_not_permission": True,
    }


def selected_evidence_manifest_basis() -> dict:
    return {
        "portable_source_body_verification_evidence_manifest_result_id": (
            "portable_source_body_verification_evidence_manifest_reference_review_001"
        ),
        "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED",
        "selected_evidence_manifest_basis_reference": (
            "portable-source-body-verification-evidence-manifest:reference-review-001"
        ),
        "selected_evidence_manifest_terminal_summary": {
            "terminal_summary_declared": True,
            "terminal_summary_reference": (
                "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_TERMINAL_SUMMARY_V0.md"
            ),
            "terminal_summary_records_evidence_definition_line": True,
            "terminal_summary_does_not_authorize_command_implementation": True,
        },
        "evidence_manifest_recorded_posture": {
            "portable_source_body_verification_evidence_manifest_recorded": True,
            "evidence_manifest_basis_declared": True,
            "required_verification_evidence_classes_declared": True,
        },
        "evidence_manifest_terminal_summary_posture": {
            "terminal_summary_declared": True,
            "terminal_summary_is_readability_only": True,
            "terminal_summary_does_not_authorize_next_work": True,
        },
        "declared_evidence_classes": selected_evidence_classes(),
        "required_surfaces": selected_required_surfaces(),
        "future_candidate_postures": future_candidate_postures(),
        "evidence_manifest_remains_evidence_definition_only": True,
        "evidence_manifest_did_not_authorize_command_implementation": True,
        "evidence_manifest_did_not_authorize_command_execution": True,
        "evidence_manifest_did_not_create_manifest_checksum_signature_packet_command": True,
        "evidence_manifest_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
    }


def selected_portable_verification_basis() -> dict:
    return {
        "portable_source_body_verification_result_id": (
            "portable_source_body_verification_reference_review_001"
        ),
        "outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        "selected_portable_verification_basis_reference": (
            "portable-source-body-verification:reference-review-001"
        ),
        "selected_portable_verification_terminal_summary": {
            "terminal_summary_declared": True,
            "terminal_summary_reference": (
                "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
            ),
            "terminal_summary_records_carrier_independent_verification": True,
            "terminal_summary_does_not_authorize_command_work": True,
        },
        "portable_verification_remains_verification_only": True,
        "portable_verification_did_not_authorize_command_manifest_checksum_signature_packet_work": True,
        "portable_verification_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
    }


def checker_command_basis() -> dict:
    return {
        "checker_only_command_basis_declared": True,
        "command_candidate_future_only": True,
        "command_is_checker_only_if_separately_implemented": True,
        "command_requires_declared_evidence_manifest_basis": True,
        "command_implementation_requires_separate_boundary": True,
        "command_execution_remains_future": True,
        "command_output_remains_future": True,
        "command_success_remains_future": True,
        "command_cannot_create_source_authority_currentness_final_completion": True,
        "command_cannot_authorize_continuation_follow_on_work": True,
    }


def command_limits() -> dict:
    return {
        "command_limits_declared": True,
        "command_boundary_only": True,
        "command_is_not_implemented": True,
        "command_is_not_executed": True,
        "command_is_not_authorized_to_run": True,
        "command_output_is_not_source": True,
        "command_success_is_not_currentness": True,
        "command_success_is_not_final_completion": True,
        "command_is_not_authority": True,
        "command_does_not_create_manifest_checksum_signature_packet": True,
        "command_does_not_create_transfer_migration_source_receipt": True,
        "command_does_not_authorize_reception": True,
        "command_does_not_create_deployment_runtime_hosting_public_release": True,
        "command_does_not_authorize_continuation_reusable_permission_follow_on_work": True,
        "path_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "command_dependency_on_evidence_manifest": {
            "command_dependency_on_evidence_manifest_declared": True,
            "command_requires_declared_evidence_manifest": True,
        },
        "no_command_authority_posture": {
            "no_command_authority_posture_declared": True,
            "command_does_not_become_authority": True,
        },
        "no_command_currentness_posture": {
            "no_command_currentness_posture_declared": True,
            "command_success_does_not_create_currentness": True,
        },
        "no_command_output_source_posture": {
            "no_command_output_source_posture_declared": True,
            "command_output_does_not_become_source": True,
        },
        "no_command_success_final_completion_posture": {
            "no_command_success_final_completion_posture_declared": True,
            "command_success_does_not_claim_final_completion": True,
        },
        "non_execution_posture": {
            "non_execution_posture_declared": True,
            "command_is_not_executed": True,
        },
    }


def declared_request(**overrides: object) -> dict:
    limits = command_limits()
    request = {
        "command_boundary_request_id": "command-boundary-review-001",
        "command_boundary_question": QUESTION,
        "command_boundary_intent": resolver.INTENT_RECORD,
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
        "selected_evidence_classes": selected_evidence_classes(),
        "selected_required_surfaces": selected_required_surfaces(),
        "selected_future_candidate_postures": future_candidate_postures(),
        "checker_command_basis": checker_command_basis(),
        "command_limits": limits,
        "command_dependency_on_evidence_manifest": limits[
            "command_dependency_on_evidence_manifest"
        ],
        "no_command_authority_posture": limits["no_command_authority_posture"],
        "no_command_currentness_posture": limits["no_command_currentness_posture"],
        "no_command_output_source_posture": limits[
            "no_command_output_source_posture"
        ],
        "no_command_success_final_completion_posture": limits[
            "no_command_success_final_completion_posture"
        ],
        "non_execution_posture": limits["non_execution_posture"],
        "command_scope": list(SUPPORTED_SCOPE),
        "requested_command_boundary_outcome": RECORDED,
        "declared_non_claims": required_false_non_claims(),
    }
    request.update(overrides)
    return request


def without_nested(mapping: dict, *paths: tuple[str, ...]) -> dict:
    result = copy.deepcopy(mapping)
    for path in paths:
        current = result
        for key in path[:-1]:
            current = current.get(key, {})
        if isinstance(current, dict):
            current.pop(path[-1], None)
    return result


class PortableSourceBodyVerificationCommandBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_portable_source_body_verification_command_boundary(
            declared_command_boundary_request=request
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["portable_source_body_verification_command_boundary_summary"][
                "failed_check_count"
            ],
            0,
        )
        self.assertTrue(
            all(check["passed"] is True for check in result["command_boundary_checks"])
        )

    def assert_false_non_claims(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in OUTPUT_FALSE_POSTURE:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_command_or_downstream_flags(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in (
            "command_implemented",
            "command_executed",
            "command_authorized_to_run",
            "command_output_created",
            "command_success_created",
            "manifest_implemented",
            "checksum_implemented",
            "signature_implemented",
            "packet_implemented",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "continuation_authorized",
            "reusable_permission_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(non_claims[key], False, key)

    def assert_block_code(self, request: dict | None, code: str) -> None:
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], code)

    def test_successful_command_boundary_recorded_result(self) -> None:
        request = declared_request()
        request_before = copy.deepcopy(request)
        result = self.resolve(request)

        self.assert_recorded(result)
        self.assertEqual(request, request_before)
        statement = result["command_boundary_statement"]
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(statement[key], True, key)
            self.assertIs(result["non_claims"][key], True, key)
        for key in (
            "selected_evidence_manifest_basis_preserved",
            "selected_portable_verification_basis_preserved",
            "checker_command_basis_declared",
            "command_limits_declared",
            "command_dependency_on_evidence_manifest_declared",
            "command_boundary_only",
            "command_is_checker_only_if_separately_implemented",
            "command_is_not_implemented",
            "command_is_not_executed",
            "command_is_not_authorized_to_run",
            "command_output_is_not_source",
            "command_success_is_not_currentness",
            "command_success_is_not_final_completion",
            "command_is_not_authority",
            "command_implementation_requires_separate_boundary",
            "recorded_true_fields_are_bounded_command_boundary_outcomes_only",
        ):
            self.assertIs(statement[key], True, key)
        self.assert_false_non_claims(result)
        self.assert_no_command_or_downstream_flags(result)

    def test_metadata_and_declared_question_are_preserved(self) -> None:
        result = self.resolve(declared_request())
        metadata = result["portable_source_body_verification_command_boundary_metadata"]
        for key in (
            "portable_source_body_verification_command_boundary_result_id",
            "portable_source_body_verification_command_boundary_result_type",
            "portable_source_body_verification_command_boundary_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(
            metadata["portable_source_body_verification_command_boundary_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        question = result["declared_command_boundary_question"]
        self.assertEqual(question["command_boundary_request_id"], "command-boundary-review-001")
        self.assertEqual(question["command_boundary_question"], QUESTION)
        self.assertEqual(question["command_boundary_intent"], resolver.INTENT_RECORD)
        self.assertEqual(
            question["selected_evidence_manifest_result_id"],
            "portable_source_body_verification_evidence_manifest_reference_review_001",
        )
        self.assertEqual(
            question["selected_portable_verification_result_id"],
            "portable_source_body_verification_reference_review_001",
        )
        self.assertTrue(question["command_boundary_is_not_command_implementation"])
        self.assertTrue(question["command_boundary_is_not_command_execution"])
        self.assertTrue(question["command_boundary_is_not_command_output"])
        self.assertTrue(question["command_boundary_is_not_source"])
        self.assertTrue(question["command_boundary_is_not_authority"])
        self.assertTrue(question["command_boundary_is_not_currentness"])
        self.assertTrue(question["command_implementation_requires_separate_boundary"])

    def test_selected_bases_are_preserved_without_mutation(self) -> None:
        request = declared_request()
        evidence_before = copy.deepcopy(request["selected_evidence_manifest_basis"])
        portable_before = copy.deepcopy(request["selected_portable_verification_basis"])
        result = self.resolve(request)

        evidence = result["selected_evidence_manifest_basis"]
        portable = result["selected_portable_verification_basis"]
        self.assertEqual(request["selected_evidence_manifest_basis"], evidence_before)
        self.assertEqual(request["selected_portable_verification_basis"], portable_before)
        self.assertEqual(
            evidence["selected_evidence_manifest_result_id"],
            "portable_source_body_verification_evidence_manifest_reference_review_001",
        )
        self.assertEqual(
            evidence["selected_evidence_manifest_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED",
        )
        self.assertTrue(evidence["evidence_manifest_remains_evidence_definition_only"])
        self.assertTrue(evidence["evidence_manifest_did_not_authorize_command_implementation"])
        self.assertTrue(evidence["evidence_manifest_did_not_authorize_command_execution"])
        self.assertTrue(
            evidence["evidence_manifest_did_not_create_manifest_checksum_signature_packet_command"]
        )
        self.assertEqual(
            portable["selected_portable_verification_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        )
        self.assertTrue(portable["portable_verification_remains_verification_only"])
        self.assertTrue(
            portable[
                "portable_verification_did_not_authorize_command_manifest_checksum_signature_packet_work"
            ]
        )

    def test_checker_command_basis_limits_scope_and_checks(self) -> None:
        result = self.resolve(declared_request())
        checker = result["checker_command_basis"]
        limits = result["command_limits"]
        scope = result["command_scope"]

        for key in (
            "command_candidate_is_future_only",
            "command_is_checker_only_if_separately_implemented",
            "command_requires_declared_evidence_manifest_basis",
            "command_implementation_requires_separate_boundary",
            "command_execution_remains_future",
            "command_output_remains_future",
            "command_success_remains_future",
            "command_cannot_create_source_authority_currentness_final_completion",
            "command_cannot_authorize_continuation_follow_on_work",
        ):
            self.assertIs(checker[key], True, key)
        for key in (
            "command_boundary_only",
            "command_is_not_implemented",
            "command_is_not_executed",
            "command_is_not_authorized_to_run",
            "command_output_is_not_source",
            "command_success_is_not_currentness",
            "command_success_is_not_final_completion",
            "command_is_not_authority",
            "command_does_not_create_manifest_checksum_signature_packet",
            "command_does_not_create_transfer_migration_source_receipt",
            "command_does_not_authorize_reception",
            "command_does_not_create_deployment_runtime_hosting_public_release",
            "command_does_not_authorize_continuation_reusable_permission_follow_on_work",
            "path_does_not_create_currentness",
            "artifact_existence_does_not_create_currentness",
            "repository_copy_does_not_become_body",
        ):
            self.assertIs(limits[key], True, key)
        self.assertTrue(scope["all_selected_scope_values_supported"])
        self.assertEqual(set(scope["selected_command_scope_values"]), set(SUPPORTED_SCOPE))

        expected_checks = {
            "command_boundary_question_declared",
            "command_boundary_intent_supported",
            "selected_evidence_manifest_result_or_terminal_summary_declared",
            "selected_portable_verification_result_or_terminal_summary_declared",
            "selected_evidence_manifest_basis_declared",
            "selected_evidence_classes_declared",
            "selected_required_surfaces_declared",
            "future_candidate_postures_declared",
            "checker_only_command_basis_declared",
            "command_limits_declared",
            "command_dependency_on_evidence_manifest_declared",
            "command_boundary_scope_supported",
            "command_not_implemented",
            "command_not_executed",
            "command_not_authorized_to_run",
            "command_output_not_created",
            "command_output_not_source",
            "command_success_not_currentness",
            "command_success_not_final_completion",
            "command_not_authority",
            "command_does_not_create_manifest",
            "command_does_not_create_checksum",
            "command_does_not_create_signature",
            "command_does_not_create_packet",
            "command_does_not_create_transfer",
            "command_does_not_create_migration",
            "command_does_not_create_source_receipt",
            "command_does_not_authorize_reception",
            "command_does_not_create_deployment",
            "command_does_not_create_runtime_hosting",
            "command_does_not_create_public_release",
            "command_does_not_authorize_continuation",
            "command_does_not_create_reusable_permission",
            "command_does_not_authorize_derivative_reception",
            "command_does_not_authorize_vessel_relation",
            "command_does_not_authorize_another_source_body_reception_request",
            "command_does_not_authorize_follow_on_work",
            "path_does_not_create_currentness",
            "latest_file_does_not_create_currentness",
            "artifact_existence_does_not_create_currentness",
            "repository_copy_does_not_become_body",
            "carrier_possession_does_not_create_currentness",
            "archive_possession_does_not_create_currentness",
            "command_success_does_not_create_currentness",
            "exit_code_does_not_create_currentness",
            "environment_state_does_not_create_authority_or_currentness",
            "os_vendor_account_do_not_create_authority",
            "narration_does_not_create_currentness",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        actual_checks = {check["check_name"] for check in result["command_boundary_checks"]}
        self.assertTrue(expected_checks <= actual_checks)
        for check in result["command_boundary_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertIs(check["passed"], True)

    def test_each_supported_scope_value_records_and_unsupported_scope_blocks(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            with self.subTest(scope=scope_value):
                self.assert_recorded(self.resolve(declared_request(command_scope=[scope_value])))
        self.assert_block_code(
            declared_request(command_scope=["COMMAND_BOUNDARY_IS_DEPLOYMENT"]),
            "UNSUPPORTED_COMMAND_BOUNDARY_SCOPE",
        )

    def test_command_boundary_non_meaning_and_what_remains_open(self) -> None:
        result = self.resolve(declared_request())
        non_meaning = result["command_boundary_non_meaning"]
        for name in (
            "command_exists",
            "command_is_implemented",
            "command_is_executable",
            "command_is_authorized_to_run",
            "command_output_exists",
            "command_result_exists",
            "command_success_exists",
            "command_success_creates_currentness",
            "command_success_creates_final_completion",
            "command_output_becomes_source",
            "manifest_exists",
            "checksum_exists",
            "signature_exists",
            "packet_exists",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "public_readiness_created",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        ):
            self.assertIs(
                non_meaning[f"command_boundary_does_not_mean_{name}"],
                True,
                name,
            )

        remains_open = result["what_remains_open"]
        for item in (
            "portable verification command boundary test",
            "portable verification command boundary live artifact",
            "portable verification command implementation",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "reproducible environment declaration",
            "runtime hosting",
            "deployment",
            "public release",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "operation permission",
            "receiving-context governance",
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

    def test_additional_basis_and_not_recorded_outcomes(self) -> None:
        additional_context = {
            "checker_only_basis_unclear": True,
            "command_limits_unclear": True,
        }
        additional = self.resolve(
            declared_request(
                requested_command_boundary_outcome=REQUIRES_ADDITIONAL_BASIS,
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
        self.assert_false_non_claims(additional)

        not_recorded_basis = {
            "reason": "command-boundary basis cannot be bounded",
            "repair_authorized": False,
            "next_work_authorized": False,
        }
        not_recorded = self.resolve(
            declared_request(
                requested_command_boundary_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_implement"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_execute"])
        self.assert_false_non_claims(not_recorded)

        for result in (additional, not_recorded):
            statement = result["command_boundary_statement"]
            for key in ALLOWED_RECORDED_TRUE_FIELDS:
                self.assertIs(statement[key], False, key)
                self.assertIs(result["non_claims"][key], False, key)
            self.assert_no_command_or_downstream_flags(result)

    def test_summary_helper_preserves_command_boundary_posture(self) -> None:
        result = self.resolve(declared_request())
        summary = resolver.build_portable_source_body_verification_command_boundary_summary(
            result
        )
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["command_boundary_request_id"], "command-boundary-review-001")
        self.assertEqual(summary["command_boundary_question"], QUESTION)
        self.assertEqual(summary["command_boundary_intent"], resolver.INTENT_RECORD)
        self.assertEqual(summary["passed_check_count"], len(result["command_boundary_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["portable_source_body_verification_command_boundary_recorded"])
        self.assertTrue(summary["verification_command_posture_declared"])
        self.assertTrue(summary["verification_command_checker_role_bounded"])
        self.assertTrue(summary["command_requires_declared_evidence_manifest"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertTrue(summary["selected_evidence_manifest_basis_preserved"])
        self.assertTrue(summary["selected_portable_verification_basis_preserved"])
        self.assertTrue(summary["checker_command_basis_declared"])
        self.assertTrue(summary["command_limits_declared"])
        self.assertTrue(summary["command_dependency_on_evidence_manifest_declared"])
        self.assertTrue(summary["command_boundary_only"])
        self.assertTrue(summary["command_checker_only_if_separately_implemented"])
        self.assertTrue(summary["command_not_implemented"])
        self.assertTrue(summary["command_not_executed"])
        self.assertTrue(summary["command_not_authorized_to_run"])
        self.assertTrue(summary["command_output_not_created"])
        self.assertTrue(summary["command_output_not_source"])
        self.assertTrue(summary["command_success_not_currentness"])
        self.assertTrue(summary["command_success_not_final_completion"])
        self.assertTrue(summary["command_not_authority"])
        self.assertTrue(summary["command_implementation_requires_separate_boundary"])
        self.assertTrue(summary["no_manifest_checksum_signature_packet_implemented"])
        self.assertTrue(summary["no_source_transferred_migrated_received_receipted"])
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
        additional_context = {"command_output_source_distinction_unclear": True}
        not_recorded_basis = {"reason": "not used in recorded case"}
        request = resolver.build_declared_portable_source_body_verification_command_boundary_request(
            "builder-command-boundary-001",
            QUESTION,
            selected_evidence_manifest_basis(),
            selected_portable_verification_basis(),
            checker_command_basis(),
            command_limits(),
            list(SUPPORTED_SCOPE),
            selected_evidence_manifest_result_path="evidence_manifest_basis.json",
            selected_evidence_manifest_result_id="evidence-manifest-id-from-builder",
            selected_evidence_manifest_result_outcome=(
                "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_RECORDED"
            ),
            requested_command_boundary_outcome=RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )
        self.assertEqual(request["command_boundary_request_id"], "builder-command-boundary-001")
        self.assertEqual(request["command_boundary_question"], QUESTION)
        self.assertEqual(
            request["selected_evidence_manifest_result_path"],
            "evidence_manifest_basis.json",
        )
        self.assertEqual(
            request["selected_evidence_manifest_result_id"],
            "evidence-manifest-id-from-builder",
        )
        self.assertEqual(request["requested_command_boundary_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, request["declared_non_claims"])
            self.assertIs(request["declared_non_claims"][key], False, key)
        for key in (
            "command_implemented",
            "command_executed",
            "command_authorized_to_run",
            "command_output_created",
            "source_transferred",
            "source_migrated",
            "source_received",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "follow_on_work_authorized",
        ):
            self.assertIs(request["declared_non_claims"][key], False, key)

        request_without_path = dict(request)
        request_without_path.pop("selected_evidence_manifest_result_path", None)
        self.assert_recorded(self.resolve(request_without_path))

    def test_path_based_request_and_selected_evidence_manifest_basis(self) -> None:
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            basis_path = tmp_dir / "selected_evidence_manifest_basis.json"
            basis_path.write_text(
                json.dumps(selected_evidence_manifest_basis(), indent=2),
                encoding="utf-8",
            )
            request = declared_request(selected_evidence_manifest_result_path=str(basis_path))
            request.pop("selected_evidence_manifest_basis")
            result = self.resolve(request)
            self.assert_recorded(result)
            self.assertEqual(
                result["selected_evidence_manifest_basis"][
                    "selected_evidence_manifest_result_path"
                ],
                str(basis_path),
            )

            request_path = tmp_dir / "declared_command_boundary_request.json"
            request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")
            path_result = resolver.resolve_portable_source_body_verification_command_boundary_from_path(
                request_path
            )
            self.assert_recorded(path_result)
            self.assertEqual(set(path_result), set(result))
            self.assertEqual(
                path_result["declared_command_boundary_question"]["declared_request_path"],
                str(request_path),
            )

    def test_write_behavior_and_default_output_path_are_additive(self) -> None:
        result = self.resolve(declared_request())
        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            output_path = tmp_dir / "nested" / "command_boundary_result.json"
            written = resolver.write_portable_source_body_verification_command_boundary_result(
                result, output_path
            )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

            default_root = tmp_dir / "command_boundary_root"
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_COMMAND_BOUNDARY_ROOT",
                default_root,
            ):
                first = resolver.write_portable_source_body_verification_command_boundary_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_command_boundary_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertTrue(first.name.endswith("__portable_source_body_verification_command_boundary_result.json"))
            self.assertTrue(second.stem.endswith("_001"))
            self.assertNotIn("evidence_manifest_boundary", str(first.parent))
            self.assertNotIn("deployment", str(first.parent))
            self.assertNotIn("runtime", str(first.parent))
            self.assertNotIn("public_release", str(first.parent))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        request_before = copy.deepcopy(request)
        evidence_before = copy.deepcopy(request["selected_evidence_manifest_basis"])
        portable_before = copy.deepcopy(request["selected_portable_verification_basis"])
        checker_before = copy.deepcopy(request["checker_command_basis"])
        limits_before = copy.deepcopy(request["command_limits"])
        scope_before = copy.deepcopy(request["command_scope"])

        first = self.resolve(request)
        second = self.resolve(request)
        self.assert_recorded(first)
        self.assert_recorded(second)
        self.assertEqual(request, request_before)
        self.assertEqual(request["selected_evidence_manifest_basis"], evidence_before)
        self.assertEqual(request["selected_portable_verification_basis"], portable_before)
        self.assertEqual(request["checker_command_basis"], checker_before)
        self.assertEqual(request["command_limits"], limits_before)
        self.assertEqual(request["command_scope"], scope_before)

        with tempfile.TemporaryDirectory() as tmp_dir_name:
            output = Path(tmp_dir_name) / "additive" / "result.json"
            resolver.write_portable_source_body_verification_command_boundary_result(
                first, output
            )
            self.assertTrue(output.exists())
            self.assertEqual(request, request_before)

    def test_blocking_basics_missing_basis_and_paths(self) -> None:
        self.assert_block_code(
            declared_request(command_boundary_intent=resolver.INTENT_BLOCK),
            "COMMAND_BOUNDARY_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assert_block_code(None, "COMMAND_BOUNDARY_QUESTION_UNDECLARED")

        malformed = resolver.resolve_portable_source_body_verification_command_boundary(
            declared_command_boundary_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
        )

        with tempfile.TemporaryDirectory() as tmp_dir_name:
            tmp_dir = Path(tmp_dir_name)
            missing = resolver.resolve_portable_source_body_verification_command_boundary_from_path(
                tmp_dir / "missing.json"
            )
            self.assertEqual(
                missing["block"]["block_code"],
                "DECLARED_COMMAND_BOUNDARY_REQUEST_UNREADABLE",
            )
            bad_json = tmp_dir / "bad.json"
            bad_json.write_text("{not-json", encoding="utf-8")
            bad = resolver.resolve_portable_source_body_verification_command_boundary_from_path(
                bad_json
            )
            self.assertEqual(
                bad["block"]["block_code"],
                "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
            )
            array_json = tmp_dir / "array.json"
            array_json.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_command_boundary_from_path(
                array_json
            )
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_COMMAND_BOUNDARY_REQUEST_MALFORMED",
            )

        missing_cases = (
            (("selected_evidence_manifest_basis",), "EVIDENCE_MANIFEST_BASIS_MISSING"),
            (("selected_portable_verification_basis",), "PORTABLE_VERIFICATION_BASIS_MISSING"),
            (("checker_command_basis",), "CHECKER_COMMAND_BASIS_MISSING"),
            (("command_limits",), "COMMAND_LIMITS_MISSING"),
        )
        for paths, code in missing_cases:
            with self.subTest(code=code):
                self.assert_block_code(without_nested(declared_request(), paths), code)

        missing_dependency = without_nested(
            declared_request(),
            ("command_dependency_on_evidence_manifest",),
            ("command_limits", "command_dependency_on_evidence_manifest"),
            ("checker_command_basis", "command_dependency_on_evidence_manifest"),
        )
        self.assert_block_code(
            missing_dependency, "COMMAND_DEPENDENCY_ON_EVIDENCE_MANIFEST_MISSING"
        )

        missing_classes = declared_request()
        missing_classes.pop("selected_evidence_classes")
        missing_classes["selected_evidence_manifest_basis"] = {
            "selected_evidence_manifest_basis_reference": "basis-without-classes",
            "required_surfaces": selected_required_surfaces(),
            "future_candidate_postures": future_candidate_postures(),
        }
        self.assert_block_code(missing_classes, "EVIDENCE_CLASSES_MISSING")

        missing_surfaces = declared_request(selected_required_surfaces=None)
        missing_surfaces["selected_evidence_manifest_basis"] = {
            "selected_evidence_manifest_basis_reference": "basis-without-surfaces",
            "declared_evidence_classes": selected_evidence_classes(),
            "future_candidate_postures": future_candidate_postures(),
        }
        self.assert_block_code(missing_surfaces, "REQUIRED_SURFACES_MISSING")

        missing_postures = declared_request(selected_future_candidate_postures=None)
        missing_postures["selected_evidence_manifest_basis"] = {
            "selected_evidence_manifest_basis_reference": "basis-without-future-postures",
            "declared_evidence_classes": selected_evidence_classes(),
            "required_surfaces": selected_required_surfaces(),
        }
        self.assert_block_code(missing_postures, "FUTURE_CANDIDATE_POSTURES_MISSING")

    def test_blocking_collapse_flags(self) -> None:
        collapse_cases = {
            "command_implemented": "COMMAND_TREATED_AS_IMPLEMENTED",
            "command_executed": "COMMAND_TREATED_AS_EXECUTABLE",
            "command_authorized_to_run": "COMMAND_TREATED_AS_AUTHORIZED_TO_RUN",
            "command_output_became_source": "COMMAND_OUTPUT_TREATED_AS_SOURCE",
            "command_success_created_currentness": "COMMAND_SUCCESS_TREATED_AS_CURRENTNESS",
            "command_success_claimed_final_completion": "COMMAND_SUCCESS_TREATED_AS_FINAL_COMPLETION",
            "command_became_authority": "COMMAND_TREATED_AS_AUTHORITY",
            "manifest_implemented": "COMMAND_CREATES_MANIFEST",
            "checksum_implemented": "COMMAND_CREATES_CHECKSUM",
            "signature_implemented": "COMMAND_CREATES_SIGNATURE",
            "packet_implemented": "COMMAND_CREATES_PACKET",
            "source_transferred": "COMMAND_CREATES_TRANSFER",
            "source_migrated": "COMMAND_CREATES_MIGRATION",
            "source_receipt_recorded": "COMMAND_CREATES_SOURCE_RECEIPT",
            "reception_authorized": "COMMAND_AUTHORIZES_RECEPTION",
            "deployment_created": "COMMAND_CREATES_DEPLOYMENT",
            "runtime_hosting_created": "COMMAND_CREATES_RUNTIME_HOSTING",
            "public_release_created": "COMMAND_CREATES_PUBLIC_RELEASE",
            "continuation_authorized": "COMMAND_AUTHORIZES_CONTINUATION",
            "reusable_permission_created": "COMMAND_CREATES_REUSABLE_PERMISSION",
            "derivative_reception_authorized": "COMMAND_AUTHORIZES_DERIVATIVE_RECEPTION",
            "vessel_relation_authorized": "COMMAND_AUTHORIZES_VESSEL_RELATION",
            "another_reception_request_authorized": "COMMAND_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
            "follow_on_work_authorized": "COMMAND_AUTHORIZES_FOLLOW_ON_WORK",
            "path_created_currentness": "PATH_TREATED_AS_CURRENTNESS",
            "latest_file_created_currentness": "LATEST_FILE_TREATED_AS_CURRENTNESS",
            "artifact_existence_created_currentness": "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS",
            "repository_copy_became_body": "REPOSITORY_COPY_TREATED_AS_BODY",
            "carrier_possession_created_currentness": "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS",
            "archive_possession_created_currentness": "ARCHIVE_POSSESSION_TREATED_AS_CURRENTNESS",
            "exit_code_created_currentness": "EXIT_CODE_TREATED_AS_CURRENTNESS",
            "environment_state_created_authority": "ENVIRONMENT_STATE_TREATED_AS_AUTHORITY_OR_CURRENTNESS",
            "os_became_authority": "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY",
            "vendor_environment_became_authority": "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY",
            "account_became_authority": "OS_VENDOR_ACCOUNT_TREATED_AS_AUTHORITY",
            "narration_created_currentness": "NARRATION_TREATED_AS_CURRENTNESS",
        }
        for flag, code in collapse_cases.items():
            with self.subTest(flag=flag):
                self.assert_block_code(declared_request(**{flag: True}), code)

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
        flipped_non_claim["declared_non_claims"]["command_implemented"] = True
        result = self.resolve(flipped_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {"NON_CLAIM_MISSING_OR_FLIPPED", "COMMAND_TREATED_AS_IMPLEMENTED"},
        )


if __name__ == "__main__":
    unittest.main()
