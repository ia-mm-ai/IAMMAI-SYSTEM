"""Bounded tests for the portable verification evidence-manifest resolver.

These tests prove only the evidence-manifest boundary. Evidence-manifest
records required evidence classes; it is not manifest, checksum, signature,
packet, command, runtime, deployment, public release, source transfer,
migration, source receipt, reception authorization, authority, currentness,
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

import resolve_portable_source_body_verification_evidence_manifest_boundary as resolver  # noqa: E402


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_EVIDENCE_MANIFEST_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTPUT_FALSE_POSTURE = tuple(resolver.OUTPUT_FALSE_POSTURE)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_evidence_manifest_metadata",
    "declared_evidence_manifest_question",
    "selected_portable_verification_basis",
    "selected_source_body_basis",
    "declared_evidence_classes",
    "required_surfaces",
    "evidence_only_posture",
    "future_candidate_postures",
    "evidence_manifest_scope",
    "evidence_manifest_checks",
    "evidence_manifest_statement",
    "evidence_manifest_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_evidence_manifest_summary",
}

QUESTION = (
    "Can the evidence basis required for future portable source-body "
    "verification checks be bounded and recorded without implementing "
    "manifest, checksum, signature, packet, command, runtime, deployment, "
    "public release, transfer, migration, source receipt, authority, "
    "currentness, continuation, reusable permission, derivative reception, "
    "vessel relation, another reception request, or follow-on work?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


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
            "terminal_summary_does_not_authorize_manifest_checksum_packet_command_work": True,
        },
        "portable_verification_recorded_posture": {
            "portable_source_body_verification_recorded": True,
            "portable_source_body_basis_verified": True,
            "carrier_independent_verification_recorded": True,
            "verification_only_posture": True,
        },
        "portable_verification_terminal_summary_posture": {
            "portable_verification_terminal_summary_declared": True,
            "terminal_summary_is_readability_only": True,
            "terminal_summary_does_not_authorize_next_work": True,
        },
        "portable_verification_remains_verification_only": True,
        "portable_verification_did_not_authorize_manifest_checksum_signature_packet_command_work": True,
        "portable_verification_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work": True,
    }


def selected_source_body_basis() -> dict:
    return {
        "selected_source_body_basis_id": "closed-source-body-basis-001",
        "selected_source_body_basis_reference": "closed-source-body-basis:001",
        "selected_source_body_reception_terminal_summary": {
            "terminal_summary_declared": True,
            "terminal_summary_reference": (
                "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
            ),
            "records_closed_source_body_reception_chain": True,
            "does_not_authorize_successor_boundary": True,
            "does_not_authorize_next_work": True,
        },
        "selected_source_body_reception_closure_basis": {
            "source_body_reception_closure_artifact_id": (
                "source_body_reception_closure_reference_review_001_corrected"
            ),
            "outcome": "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED",
            "failed_check_count": 0,
            "source_body_reception_closure_recorded": True,
            "source_body_reception_boundary_chain_closed": True,
            "reception_closure_passed": True,
            "reception_family_closure_recorded": True,
            "closure_is_bounded_chain_closure_only": True,
            "closure_did_not_authorize_reception": True,
            "closure_did_not_receive_source": True,
            "closure_did_not_record_source_receipt": True,
            "closure_did_not_create_source_receipt": True,
            "closure_did_not_claim_final_completion": True,
            "closure_did_not_authorize_continuation": True,
            "closure_did_not_create_reusable_permission": True,
            "closure_did_not_authorize_another_reception_request": True,
        },
        "selected_distributed_operation_terminal_basis": {
            "distributed_operation_terminal_summary_declared": True,
            "reference": "spec/DISTRIBUTED_OPERATION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
        },
        "selected_distributed_operation_closure_basis": {
            "distributed_operation_closure_basis_declared": True,
            "reference": "spec/DISTRIBUTED_OPERATION_CLOSURE_BOUNDARY_V0_MIN_SPEC.md",
        },
        "selected_current_body_conformance_basis": {
            "current_body_conformance_basis_declared": True,
            "reference": "spec/CURRENT_BODY_CONFORMANCE_V4_CLOSURE_V0_MIN_SPEC.md",
        },
        "selected_current_self_orientation_basis": {
            "current_self_orientation_basis_declared": True,
            "reference": "spec/CURRENT_SELF_ORIENTATION_V9_V0_MIN_SPEC.md",
        },
        "selected_source_body_basis_remains_bounded_evidence_only": True,
        "selected_source_body_basis_does_not_become_source": True,
        "selected_source_body_basis_does_not_create_currentness": True,
        "selected_source_body_basis_does_not_authorize_next_work": True,
    }


def declared_evidence_classes() -> dict:
    return {
        "evidence_classes_declared": True,
        "evidence_classes": [
            "required_source_surfaces",
            "required_spec_surfaces",
            "required_resolver_surfaces",
            "required_test_surfaces",
            "required_artifact_roots",
            "required_closure_artifacts",
            "required_terminal_summaries",
            "corrected_closure_evidence",
            "failed_input_evidence_posture",
            "future_manifest_candidate",
            "future_checksum_candidate",
            "future_signature_candidate",
            "future_packet_candidate",
            "future_command_candidate",
        ],
        "source_surfaces": ["reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md"],
        "spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_V0_MIN_SPEC.md"
        ],
        "resolver_surfaces": [
            "src/resolve_portable_source_body_verification_evidence_manifest_boundary.py"
        ],
        "test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_evidence_manifest_boundary.py"
        ],
        "artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_boundary/"
        ],
        "closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "terminal_summaries": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
        ],
        "corrected_closure_evidence": {
            "corrected_closure_artifact_selected_where_relevant": True,
            "failed_input_evidence_remains_visible": True,
        },
        "failed_input_evidence_posture": {
            "failed_input_evidence_visible_only": True,
            "failed_input_evidence_does_not_become_authority": True,
        },
        "future_manifest_candidate": {"manifest_candidate_future_only": True},
        "future_checksum_candidate": {"checksum_candidate_future_only": True},
        "future_signature_candidate": {"signature_candidate_future_only": True},
        "future_packet_candidate": {"packet_candidate_future_only": True},
        "future_command_candidate": {"command_candidate_future_only": True},
        "evidence_classes_are_evidence_only": True,
        "evidence_classes_do_not_implement_anything": True,
        "evidence_classes_do_not_authorize_command": True,
    }


def required_surfaces() -> dict:
    return {
        "required_source_surfaces": [
            "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
            "reference/IAMMAI/RANKED_SURFACE_INDEX.md",
        ],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_V0_MIN_SPEC.md",
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_evidence_manifest_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_evidence_manifest_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_verification_boundary/",
            "artifacts/integrity_host_v0_min_coexistence_source_body_reception_closure_boundary/",
        ],
        "required_closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "required_terminal_summaries": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_TERMINAL_SUMMARY_V0.md",
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
        ],
        "corrected_closure_artifact_posture": {
            "corrected_closure_artifact_posture_declared": True,
            "corrected_closure_artifact_is_evidence_only": True,
        },
        "failed_input_evidence_posture": {
            "failed_input_evidence_posture_declared": True,
            "failed_input_evidence_is_visible_failed_input_only": True,
        },
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_source": True,
        "surfaces_do_not_create_authority": True,
        "surfaces_do_not_create_currentness": True,
        "surfaces_do_not_create_permission": True,
        "surfaces_do_not_create_command_execution": True,
        "surfaces_do_not_create_deployment_or_public_release": True,
    }


def evidence_only_posture() -> dict:
    return {
        "evidence_only_posture_declared": True,
        "evidence_does_not_become_source": True,
        "evidence_does_not_create_authority": True,
        "evidence_does_not_create_currentness": True,
        "evidence_does_not_create_permission": True,
        "path_does_not_create_currentness": True,
        "latest_file_does_not_create_currentness": True,
        "artifact_existence_does_not_create_currentness": True,
        "repository_copy_does_not_become_body": True,
        "carrier_possession_does_not_create_currentness": True,
        "narration_does_not_create_currentness": True,
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


def declared_request(**overrides: object) -> dict:
    surfaces = required_surfaces()
    source_body = selected_source_body_basis()
    request = {
        "evidence_manifest_request_id": "evidence-manifest-review-001",
        "evidence_manifest_question": QUESTION,
        "evidence_manifest_intent": resolver.INTENT_RECORD,
        "selected_portable_verification_basis": selected_portable_verification_basis(),
        "selected_portable_verification_result_id": (
            "portable_source_body_verification_reference_review_001"
        ),
        "selected_portable_verification_result_outcome": (
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED"
        ),
        "portable_verification_recorded_posture": {
            "portable_source_body_verification_recorded": True,
            "carrier_independent_verification_recorded": True,
        },
        "portable_verification_terminal_summary_posture": {
            "terminal_summary_declared": True,
            "terminal_summary_is_readability_only": True,
        },
        "selected_source_body_basis": source_body,
        "selected_source_body_reception_terminal_summary": source_body[
            "selected_source_body_reception_terminal_summary"
        ],
        "selected_source_body_reception_closure_basis": source_body[
            "selected_source_body_reception_closure_basis"
        ],
        "selected_distributed_operation_terminal_basis": source_body[
            "selected_distributed_operation_terminal_basis"
        ],
        "selected_distributed_operation_closure_basis": source_body[
            "selected_distributed_operation_closure_basis"
        ],
        "selected_current_body_conformance_basis": source_body[
            "selected_current_body_conformance_basis"
        ],
        "selected_current_self_orientation_basis": source_body[
            "selected_current_self_orientation_basis"
        ],
        "declared_evidence_classes": declared_evidence_classes(),
        "required_surfaces": surfaces,
        "required_source_surfaces": surfaces["required_source_surfaces"],
        "required_spec_surfaces": surfaces["required_spec_surfaces"],
        "required_resolver_surfaces": surfaces["required_resolver_surfaces"],
        "required_test_surfaces": surfaces["required_test_surfaces"],
        "required_artifact_roots": surfaces["required_artifact_roots"],
        "required_closure_artifacts": surfaces["required_closure_artifacts"],
        "required_terminal_summaries": surfaces["required_terminal_summaries"],
        "corrected_closure_artifact_posture": surfaces[
            "corrected_closure_artifact_posture"
        ],
        "failed_input_evidence_posture": surfaces["failed_input_evidence_posture"],
        "evidence_only_posture": evidence_only_posture(),
        "future_candidate_postures": future_candidate_postures(),
        "manifest_candidate_posture": {"manifest_candidate_future_only": True},
        "checksum_candidate_posture": {"checksum_candidate_future_only": True},
        "signature_candidate_posture": {"signature_candidate_future_only": True},
        "packet_candidate_posture": {"packet_candidate_future_only": True},
        "command_candidate_posture": {
            "command_candidate_future_only": True,
            "command_requires_separate_boundary": True,
        },
        "evidence_manifest_scope": list(SUPPORTED_SCOPE),
        "requested_evidence_manifest_outcome": RECORDED,
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


class PortableSourceBodyVerificationEvidenceManifestBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_portable_source_body_verification_evidence_manifest_boundary(
            declared_evidence_manifest_request=request
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["portable_source_body_verification_evidence_manifest_summary"][
                "failed_check_count"
            ],
            0,
        )
        self.assertTrue(
            all(check["passed"] is True for check in result["evidence_manifest_checks"])
        )

    def assert_false_non_claims(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in OUTPUT_FALSE_POSTURE:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_successful_evidence_manifest_recorded_result(self) -> None:
        request = declared_request()
        request_before = copy.deepcopy(request)
        result = self.resolve(request)

        self.assert_recorded(result)
        self.assertEqual(request, request_before)
        statement = result["evidence_manifest_statement"]
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(statement[key], True)
            self.assertIs(result["non_claims"][key], True)
        for key in (
            "selected_portable_verification_basis_preserved",
            "selected_source_body_basis_preserved",
            "declared_evidence_classes_preserved",
            "required_surfaces_preserved",
            "evidence_only_posture_declared",
            "future_candidate_postures_declared",
            "evidence_manifest_boundary_only",
            "evidence_manifest_is_not_manifest_implementation",
            "evidence_manifest_is_not_command",
            "evidence_manifest_is_not_checksum",
            "evidence_manifest_is_not_signature",
            "evidence_manifest_is_not_packet",
            "evidence_does_not_become_source",
            "evidence_does_not_create_authority",
            "evidence_does_not_create_currentness",
            "path_does_not_create_currentness",
            "latest_file_does_not_create_currentness",
            "artifact_existence_does_not_create_currentness",
            "repository_copy_does_not_become_body",
            "command_requires_separate_boundary",
            "recorded_true_fields_are_bounded_evidence_manifest_outcomes_only",
        ):
            self.assertIs(statement[key], True, key)
        for key in (
            "manifest_implemented",
            "checksum_implemented",
            "signature_implemented",
            "packet_implemented",
            "command_implemented",
            "command_authorized",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
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
            self.assertIs(statement[key], False, key)
        self.assert_false_non_claims(result)

    def test_metadata_and_declared_question_are_preserved(self) -> None:
        result = self.resolve(declared_request())
        metadata = result["portable_source_body_verification_evidence_manifest_metadata"]
        for key in (
            "portable_source_body_verification_evidence_manifest_result_id",
            "portable_source_body_verification_evidence_manifest_result_type",
            "portable_source_body_verification_evidence_manifest_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(
            metadata["portable_source_body_verification_evidence_manifest_result_version"],
            "0.1.0",
        )
        self.assertEqual(metadata["resolver_module"], resolver.RESOLVER_MODULE)

        question = result["declared_evidence_manifest_question"]
        self.assertEqual(question["evidence_manifest_request_id"], "evidence-manifest-review-001")
        self.assertEqual(question["evidence_manifest_question"], QUESTION)
        self.assertEqual(question["evidence_manifest_intent"], resolver.INTENT_RECORD)
        self.assertEqual(
            question["selected_portable_verification_result_id"],
            "portable_source_body_verification_reference_review_001",
        )
        self.assertEqual(
            question["selected_portable_verification_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        )
        self.assertTrue(question["evidence_manifest_is_not_manifest_implementation"])
        self.assertTrue(question["evidence_manifest_is_not_command"])
        self.assertTrue(question["evidence_manifest_is_not_checksum"])
        self.assertTrue(question["evidence_manifest_is_not_signature"])
        self.assertTrue(question["evidence_manifest_is_not_packet"])
        self.assertTrue(question["command_requires_separate_boundary"])

    def test_selected_bases_are_preserved_without_mutation(self) -> None:
        request = declared_request()
        portable_before = copy.deepcopy(request["selected_portable_verification_basis"])
        source_before = copy.deepcopy(request["selected_source_body_basis"])
        result = self.resolve(request)

        portable = result["selected_portable_verification_basis"]
        self.assertEqual(
            portable["selected_portable_verification_result_id"],
            "portable_source_body_verification_reference_review_001",
        )
        self.assertEqual(
            portable["selected_portable_verification_result_outcome"],
            "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        )
        self.assertEqual(
            portable["portable_verification_recorded_posture"],
            request["portable_verification_recorded_posture"],
        )
        self.assertTrue(portable["portable_verification_remains_verification_only"])
        self.assertTrue(
            portable[
                "portable_verification_did_not_authorize_manifest_checksum_signature_packet_command_work"
            ]
        )
        self.assertTrue(
            portable[
                "portable_verification_did_not_create_transfer_migration_source_receipt_deployment_runtime_public_release_final_completion_continuation_reusable_permission_follow_on_work"
            ]
        )

        source = result["selected_source_body_basis"]
        self.assertEqual(
            source["selected_source_body_reception_terminal_summary"],
            source_before["selected_source_body_reception_terminal_summary"],
        )
        self.assertEqual(
            source["selected_source_body_reception_closure_basis"],
            source_before["selected_source_body_reception_closure_basis"],
        )
        self.assertEqual(
            source["selected_distributed_operation_terminal_closure_basis"],
            request["selected_distributed_operation_terminal_basis"],
        )
        self.assertEqual(
            source["selected_current_body_conformance_orientation_basis"],
            request["selected_current_body_conformance_basis"],
        )
        self.assertTrue(source["selected_source_body_basis_remains_bounded_evidence_only"])
        self.assertTrue(source["selected_source_body_basis_does_not_become_source"])
        self.assertTrue(source["selected_source_body_basis_does_not_create_currentness"])
        self.assertTrue(source["selected_source_body_basis_does_not_authorize_next_work"])
        self.assertEqual(request["selected_portable_verification_basis"], portable_before)
        self.assertEqual(request["selected_source_body_basis"], source_before)

    def test_declared_evidence_classes_required_surfaces_and_postures(self) -> None:
        result = self.resolve(declared_request())
        classes = result["declared_evidence_classes"]
        self.assertGreaterEqual(classes["declared_evidence_classes_count"], 14)
        for expected in (
            "required_source_surfaces",
            "required_spec_surfaces",
            "required_resolver_surfaces",
            "required_test_surfaces",
            "required_artifact_roots",
            "required_closure_artifacts",
            "required_terminal_summaries",
            "corrected_closure_evidence",
            "failed_input_evidence_posture",
            "future_manifest_candidate",
            "future_checksum_candidate",
            "future_signature_candidate",
            "future_packet_candidate",
            "future_command_candidate",
        ):
            self.assertIn(expected, classes["declared_evidence_classes_representative"])
        self.assertTrue(classes["evidence_classes_are_evidence_only"])
        self.assertTrue(classes["evidence_classes_do_not_implement_anything"])
        self.assertTrue(classes["evidence_classes_do_not_authorize_command"])

        surfaces = result["required_surfaces"]
        for key in (
            "required_source_surfaces",
            "required_spec_surfaces",
            "required_resolver_surfaces",
            "required_test_surfaces",
            "required_artifact_roots",
            "required_closure_artifacts",
            "required_terminal_summaries",
        ):
            self.assertTrue(surfaces[key], key)
        self.assertTrue(surfaces["corrected_closure_artifact_posture"])
        self.assertTrue(surfaces["failed_input_evidence_posture"])
        self.assertTrue(surfaces["surfaces_are_evidence_only"])
        self.assertTrue(surfaces["surfaces_do_not_create_source"])
        self.assertTrue(surfaces["surfaces_do_not_create_authority"])
        self.assertTrue(surfaces["surfaces_do_not_create_currentness"])
        self.assertTrue(surfaces["surfaces_do_not_create_permission"])
        self.assertTrue(surfaces["surfaces_do_not_create_command_execution"])
        self.assertTrue(surfaces["surfaces_do_not_create_deployment_or_public_release"])

        evidence = result["evidence_only_posture"]
        for key in (
            "evidence_does_not_become_source",
            "evidence_does_not_create_authority",
            "evidence_does_not_create_currentness",
            "evidence_does_not_create_permission",
            "path_does_not_create_currentness",
            "latest_file_does_not_create_currentness",
            "artifact_existence_does_not_create_currentness",
            "repository_copy_does_not_become_body",
            "carrier_possession_does_not_create_currentness",
            "narration_does_not_create_currentness",
        ):
            self.assertTrue(evidence[key], key)

        future = result["future_candidate_postures"]
        for key in (
            "manifest_candidate_future_only",
            "checksum_candidate_future_only",
            "signature_candidate_future_only",
            "packet_candidate_future_only",
            "command_candidate_future_only",
            "manifest_not_implemented",
            "checksum_not_implemented",
            "signature_not_implemented",
            "packet_not_implemented",
            "command_not_implemented",
            "command_not_authorized",
            "command_requires_separate_boundary",
            "candidates_are_not_source",
            "candidates_are_not_authority",
            "candidates_are_not_currentness",
            "candidates_are_not_permission",
        ):
            self.assertTrue(future[key], key)

    def test_supported_scope_values_and_unsupported_scope(self) -> None:
        for scope in SUPPORTED_SCOPE:
            with self.subTest(scope=scope):
                result = self.resolve(declared_request(evidence_manifest_scope=[scope]))
                self.assertEqual(result["outcome"], RECORDED)
                self.assertEqual(
                    result["portable_source_body_verification_evidence_manifest_summary"][
                        "failed_check_count"
                    ],
                    0,
                )

        result = self.resolve(
            declared_request(evidence_manifest_scope=["EVIDENCE_MANIFEST_AS_DEPLOYMENT"])
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], "UNSUPPORTED_EVIDENCE_MANIFEST_SCOPE")

    def test_check_records_cover_expected_boundary_conditions(self) -> None:
        result = self.resolve(declared_request())
        expected_names = {
            "evidence_manifest_question_declared",
            "evidence_manifest_intent_supported",
            "selected_portable_verification_result_or_terminal_summary_declared",
            "selected_source_body_reception_terminal_summary_declared",
            "selected_source_body_reception_closure_basis_declared",
            "declared_evidence_classes_present",
            "required_source_surfaces_declared",
            "required_spec_surfaces_declared",
            "required_resolver_surfaces_declared",
            "required_test_surfaces_declared",
            "required_artifact_roots_declared",
            "required_closure_artifacts_declared",
            "terminal_summary_surfaces_declared",
            "future_candidate_postures_declared",
            "manifest_checksum_signature_packet_command_candidate_postures_future_only",
            "evidence_only_posture_declared",
            "evidence_manifest_scope_supported",
            "evidence_does_not_become_source",
            "evidence_does_not_create_authority",
            "evidence_does_not_create_currentness",
            "path_does_not_create_currentness",
            "latest_file_does_not_create_currentness",
            "artifact_existence_does_not_create_currentness",
            "repository_copy_does_not_become_body",
            "carrier_possession_does_not_create_currentness",
            "narration_does_not_create_currentness",
            "command_remains_future_work",
            "manifest_implementation_remains_future_work",
            "checksum_signature_implementation_remains_future_work",
            "packet_implementation_remains_future_work",
            "verification_command_remains_future_work",
            "evidence_review_does_not_create_transfer",
            "evidence_review_does_not_create_migration",
            "evidence_review_does_not_create_source_receipt",
            "evidence_review_does_not_authorize_reception",
            "evidence_review_does_not_create_deployment",
            "evidence_review_does_not_create_runtime_hosting",
            "evidence_review_does_not_create_public_release",
            "evidence_review_does_not_authorize_continuation",
            "evidence_review_does_not_create_reusable_permission",
            "evidence_review_does_not_authorize_derivative_reception",
            "evidence_review_does_not_authorize_vessel_relation",
            "evidence_review_does_not_authorize_another_reception_request",
            "evidence_review_does_not_authorize_follow_on_work",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        names = {check["check_name"] for check in result["evidence_manifest_checks"]}
        self.assertTrue(expected_names.issubset(names))
        for check in result["evidence_manifest_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])

    def test_evidence_manifest_non_meaning_and_open_items(self) -> None:
        result = self.resolve(declared_request())
        non_meaning = result["evidence_manifest_non_meaning"]
        for suffix in (
            "manifest_exists",
            "checksum_exists",
            "signature_exists",
            "packet_exists",
            "command_exists",
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
            "carrier_became_source",
            "evidence_became_source",
            "artifact_existence_became_currentness",
            "repository_copy_became_body",
            "local_path_became_currentness",
            "latest_file_became_currentness",
            "runtime_hosting_created",
            "deployment_created",
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
            self.assertTrue(non_meaning[f"evidence_manifest_does_not_mean_{suffix}"])

        open_section = result["what_remains_open"]
        for item in (
            "portable source-body verification evidence-manifest test",
            "portable source-body verification evidence-manifest live artifact",
            "manifest implementation",
            "checksum implementation",
            "signature implementation",
            "source-body packet implementation",
            "portable verification command boundary",
            "portable verification command implementation",
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
            self.assertIn(item, open_section["open_items"])
        self.assertTrue(open_section["open_means_not_scheduled"])
        self.assertTrue(open_section["open_means_not_authorized"])
        self.assertTrue(open_section["open_means_not_executed"])

    def test_requires_additional_basis_and_not_recorded_outcomes(self) -> None:
        additional_context = {"missing_basis": ["evidence classes too generic"]}
        additional = self.resolve(
            declared_request(
                requested_evidence_manifest_outcome=REQUIRES_ADDITIONAL_BASIS,
                additional_basis_context=additional_context,
            )
        )
        self.assertEqual(additional["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(
            additional["additional_basis_required"]["additional_basis_context"],
            additional_context,
        )
        self.assertTrue(additional["additional_basis_required"]["additional_basis_required"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_scheduled"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_authorized"])
        self.assertTrue(additional["additional_basis_required"]["missing_basis_not_executed"])
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(additional["non_claims"][key], False)
        self.assert_false_non_claims(additional)

        not_recorded_basis = {"reason": "evidence basis cannot be bounded"}
        not_recorded = self.resolve(
            declared_request(
                requested_evidence_manifest_outcome=NOT_RECORDED,
                not_recorded_basis=not_recorded_basis,
            )
        )
        self.assertEqual(not_recorded["outcome"], NOT_RECORDED)
        self.assertEqual(
            not_recorded["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_basis,
        )
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded"])
        self.assertTrue(not_recorded["not_recorded_basis"]["not_recorded_does_not_repair"])
        self.assertTrue(
            not_recorded["not_recorded_basis"]["not_recorded_does_not_authorize_follow_on_work"]
        )
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertIs(not_recorded["non_claims"][key], False)
        self.assert_false_non_claims(not_recorded)

    def test_summary_helper_preserves_key_fields(self) -> None:
        result = self.resolve(declared_request())
        summary = resolver.build_portable_source_body_verification_evidence_manifest_summary(
            result
        )
        self.assertEqual(summary, result["portable_source_body_verification_evidence_manifest_summary"])
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertEqual(summary["evidence_manifest_request_id"], "evidence-manifest-review-001")
        self.assertEqual(summary["evidence_manifest_question"], QUESTION)
        self.assertEqual(summary["evidence_manifest_intent"], resolver.INTENT_RECORD)
        self.assertEqual(
            summary["selected_portable_verification_result_id"],
            "portable_source_body_verification_reference_review_001",
        )
        self.assertEqual(
            summary["selected_source_body_basis_reference"],
            "closed-source-body-basis:001",
        )
        self.assertGreaterEqual(summary["declared_evidence_classes_count"], 14)
        self.assertTrue(summary["required_source_surfaces_declared"])
        self.assertTrue(summary["required_spec_surfaces_declared"])
        self.assertTrue(summary["required_resolver_surfaces_declared"])
        self.assertTrue(summary["required_test_surfaces_declared"])
        self.assertTrue(summary["required_artifact_roots_declared"])
        self.assertTrue(summary["required_closure_artifacts_declared"])
        self.assertTrue(summary["required_terminal_summaries_declared"])
        self.assertEqual(summary["passed_check_count"], len(result["evidence_manifest_checks"]))
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["portable_source_body_verification_evidence_manifest_recorded"])
        self.assertTrue(summary["evidence_manifest_basis_declared"])
        self.assertTrue(summary["required_verification_evidence_classes_declared"])
        self.assertFalse(summary["not_recorded"])
        self.assertFalse(summary["requires_additional_basis"])
        self.assertTrue(summary["selected_portable_verification_basis_preserved"])
        self.assertTrue(summary["selected_source_body_basis_preserved"])
        self.assertTrue(summary["declared_evidence_classes_preserved"])
        self.assertTrue(summary["required_surfaces_preserved"])
        self.assertTrue(summary["evidence_only_posture_declared"])
        self.assertTrue(summary["future_candidate_postures_declared"])
        self.assertTrue(summary["evidence_manifest_boundary_only"])
        self.assertTrue(summary["evidence_manifest_not_manifest_command_checksum_signature_packet"])
        self.assertTrue(summary["evidence_does_not_become_source_authority_currentness"])
        self.assertTrue(
            summary["path_latest_artifact_repository_carrier_narration_not_currentness_body"]
        )
        self.assertTrue(summary["command_requires_separate_boundary"])
        self.assertTrue(summary["no_manifest_checksum_signature_packet_command_implemented"])
        self.assertTrue(summary["no_source_transferred_migrated_received_receipted"])
        self.assertTrue(summary["no_deployment_runtime_public_release"])
        self.assertTrue(summary["no_operation_permission_public_readiness_final_completion"])
        self.assertTrue(summary["no_continuation_publication_flow_reusable_permission"])
        self.assertTrue(
            summary[
                "no_derivative_reception_vessel_relation_another_reception_request_follow_on_work"
            ]
        )

    def test_request_builder_helper_builds_resolvable_bounded_request(self) -> None:
        request = resolver.build_declared_portable_source_body_verification_evidence_manifest_request(
            "builder-review-001",
            QUESTION,
            selected_portable_verification_basis(),
            selected_source_body_basis(),
            declared_evidence_classes(),
            required_surfaces(),
            evidence_only_posture(),
            future_candidate_postures(),
            list(SUPPORTED_SCOPE),
            selected_portable_verification_result_path=None,
            selected_portable_verification_result_id="portable-result-builder-001",
            selected_portable_verification_result_outcome=(
                "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED"
            ),
            additional_basis_context={"note": "not scheduled"},
            not_recorded_basis={"note": "not recorded basis preserved"},
        )
        self.assertEqual(request["evidence_manifest_request_id"], "builder-review-001")
        self.assertEqual(request["evidence_manifest_question"], QUESTION)
        self.assertEqual(
            request["selected_portable_verification_result_id"],
            "portable-result-builder-001",
        )
        self.assertEqual(request["selected_portable_verification_basis"], selected_portable_verification_basis())
        self.assertEqual(request["selected_source_body_basis"], selected_source_body_basis())
        self.assertEqual(request["declared_evidence_classes"], declared_evidence_classes())
        self.assertEqual(request["required_surfaces"], required_surfaces())
        self.assertEqual(request["evidence_only_posture"], evidence_only_posture())
        self.assertEqual(request["future_candidate_postures"], future_candidate_postures())
        self.assertEqual(request["evidence_manifest_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["additional_basis_context"], {"note": "not scheduled"})
        self.assertEqual(request["not_recorded_basis"], {"note": "not recorded basis preserved"})
        for key in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False)
        result = self.resolve(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(
            result["portable_source_body_verification_evidence_manifest_summary"][
                "failed_check_count"
            ],
            0,
        )

    def test_path_based_selected_portable_basis_and_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            portable_path = tmp_path / "selected_portable_verification_basis.json"
            portable_payload = selected_portable_verification_basis()
            portable_path.write_text(json.dumps(portable_payload), encoding="utf-8")

            request = declared_request(
                selected_portable_verification_basis=None,
                selected_portable_verification_result_path=str(portable_path),
            )
            result = self.resolve(request)
            self.assertEqual(result["outcome"], RECORDED)
            self.assertEqual(
                result["selected_portable_verification_basis"][
                    "selected_portable_verification_result_path"
                ],
                str(portable_path),
            )
            self.assertEqual(
                result["selected_portable_verification_basis"][
                    "raw_selected_portable_verification_basis"
                ],
                portable_payload,
            )

            request_path = tmp_path / "declared_evidence_manifest_request.json"
            request_path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary_from_path(
                request_path
            )
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result), set(result))
            self.assertEqual(
                path_result["declared_evidence_manifest_question"]["declared_request_path"],
                str(request_path),
            )

    def test_markdown_terminal_summary_path_is_evidence_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary_path = Path(tmp) / "terminal_summary.md"
            summary_path.write_text("# Terminal Summary\n\nEvidence only.\n", encoding="utf-8")
            request = declared_request(
                selected_portable_verification_terminal_summary_path=str(summary_path),
                selected_source_body_reception_terminal_summary_path=str(summary_path),
            )
            result = self.resolve(request)
            self.assertEqual(result["outcome"], RECORDED)
            portable_raw = result["selected_portable_verification_basis"][
                "raw_selected_portable_verification_basis"
            ]
            self.assertTrue(
                portable_raw["selected_portable_verification_terminal_summary_path_metadata"][
                    "path_readable"
                ]
            )
            self.assertTrue(
                portable_raw["selected_portable_verification_terminal_summary_path_metadata"][
                    "path_is_evidence_only"
                ]
            )
            source_summary = result["selected_source_body_basis"][
                "selected_source_body_reception_terminal_summary"
            ]
            self.assertTrue(
                source_summary[
                    "selected_source_body_reception_terminal_summary_path_metadata"
                ]["path_does_not_create_currentness"]
            )
            self.assertFalse(result["non_claims"]["path_created_currentness"])

    def test_write_behavior_and_default_root_deduplication(self) -> None:
        result = self.resolve(declared_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "result.json"
            written = resolver.write_portable_source_body_verification_evidence_manifest_result(
                result, explicit
            )
            self.assertEqual(written, explicit)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertEqual(TOP_LEVEL_SECTIONS, set(parsed))
            self.assertEqual(parsed["outcome"], RECORDED)

            default_root = Path(tmp) / "evidence_manifest_root"
            self.assertNotIn("portable_source_body_verification_boundary", str(default_root))
            with patch.object(
                resolver,
                "PORTABLE_SOURCE_BODY_VERIFICATION_EVIDENCE_MANIFEST_BOUNDARY_ROOT",
                default_root,
            ):
                first = resolver.write_portable_source_body_verification_evidence_manifest_result(
                    result
                )
                second = resolver.write_portable_source_body_verification_evidence_manifest_result(
                    result
                )
            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__portable_source_body_verification_evidence_manifest_result.json"))
            self.assertIn("_001", second.stem)
            self.assertNotIn("manifest", first.parent.name.replace("evidence_manifest", ""))
            self.assertNotIn("deployment", str(first.parent))
            self.assertNotIn("runtime", str(first.parent))
            self.assertNotIn("public-release", str(first.parent))

    def test_resolver_does_not_mutate_inputs(self) -> None:
        request = declared_request()
        request_before = copy.deepcopy(request)
        portable_before = copy.deepcopy(request["selected_portable_verification_basis"])
        source_before = copy.deepcopy(request["selected_source_body_basis"])
        classes_before = copy.deepcopy(request["declared_evidence_classes"])
        surfaces_before = copy.deepcopy(request["required_surfaces"])
        evidence_before = copy.deepcopy(request["evidence_only_posture"])
        future_before = copy.deepcopy(request["future_candidate_postures"])
        scope_before = copy.deepcopy(request["evidence_manifest_scope"])

        first = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        self.assertEqual(request, request_before)
        self.assertEqual(request["selected_portable_verification_basis"], portable_before)
        self.assertEqual(request["selected_source_body_basis"], source_before)
        self.assertEqual(request["declared_evidence_classes"], classes_before)
        self.assertEqual(request["required_surfaces"], surfaces_before)
        self.assertEqual(request["evidence_only_posture"], evidence_before)
        self.assertEqual(request["future_candidate_postures"], future_before)
        self.assertEqual(request["evidence_manifest_scope"], scope_before)

    def test_explicit_block_missing_and_malformed_requests(self) -> None:
        explicit = self.resolve(
            declared_request(evidence_manifest_intent=resolver.INTENT_BLOCK)
        )
        self.assertEqual(explicit["outcome"], BLOCKED)
        self.assertEqual(
            explicit["block"]["block_code"],
            "EVIDENCE_MANIFEST_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
        )
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertFalse(explicit["non_claims"][key])

        missing = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary()
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(
            missing["block"]["block_code"],
            "EVIDENCE_MANIFEST_QUESTION_UNDECLARED",
        )

        malformed = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary(
            declared_evidence_manifest_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
        )

    def test_request_path_unreadable_malformed_and_array_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary_from_path(
                tmp_path / "missing.json"
            )
            self.assertEqual(missing["outcome"], BLOCKED)
            self.assertEqual(
                missing["block"]["block_code"],
                "DECLARED_EVIDENCE_MANIFEST_REQUEST_UNREADABLE",
            )

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["outcome"], BLOCKED)
            self.assertEqual(
                malformed["block"]["block_code"],
                "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
            )

            array_path = tmp_path / "array.json"
            array_path.write_text(json.dumps([]), encoding="utf-8")
            array_result = resolver.resolve_portable_source_body_verification_evidence_manifest_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["outcome"], BLOCKED)
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_EVIDENCE_MANIFEST_REQUEST_MALFORMED",
            )

    def test_missing_required_basis_blocks(self) -> None:
        cases = [
            (
                "selected_portable_verification_basis",
                "PORTABLE_VERIFICATION_BASIS_MISSING",
                ("selected_portable_verification_basis",),
                ("selected_portable_verification_result_path",),
            ),
            (
                "source_body_reception_terminal_summary",
                "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING",
                ("selected_source_body_reception_terminal_summary",),
                (
                    "selected_source_body_basis",
                    "selected_source_body_reception_terminal_summary",
                ),
            ),
            (
                "source_body_reception_closure_basis",
                "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING",
                ("selected_source_body_reception_closure_basis",),
                (
                    "selected_source_body_basis",
                    "selected_source_body_reception_closure_basis",
                ),
            ),
            ("declared_evidence_classes", "DECLARED_EVIDENCE_CLASSES_MISSING", ("declared_evidence_classes",)),
            (
                "required_source_surfaces",
                "REQUIRED_SOURCE_SURFACES_MISSING",
                ("required_source_surfaces",),
                ("required_surfaces", "required_source_surfaces"),
            ),
            (
                "required_spec_surfaces",
                "REQUIRED_SPEC_SURFACES_MISSING",
                ("required_spec_surfaces",),
                ("required_surfaces", "required_spec_surfaces"),
            ),
            (
                "required_resolver_surfaces",
                "REQUIRED_RESOLVER_SURFACES_MISSING",
                ("required_resolver_surfaces",),
                ("required_surfaces", "required_resolver_surfaces"),
            ),
            (
                "required_test_surfaces",
                "REQUIRED_TEST_SURFACES_MISSING",
                ("required_test_surfaces",),
                ("required_surfaces", "required_test_surfaces"),
            ),
            (
                "required_artifact_roots",
                "REQUIRED_ARTIFACT_ROOTS_MISSING",
                ("required_artifact_roots",),
                ("required_surfaces", "required_artifact_roots"),
            ),
            (
                "required_closure_artifacts",
                "REQUIRED_CLOSURE_ARTIFACTS_MISSING",
                ("required_closure_artifacts",),
                ("required_surfaces", "required_closure_artifacts"),
            ),
            ("evidence_only_posture", "EVIDENCE_ONLY_POSTURE_MISSING", ("evidence_only_posture",)),
            (
                "future_candidate_postures",
                "FUTURE_CANDIDATE_POSTURE_MISSING",
                ("future_candidate_postures",),
                ("manifest_candidate_posture",),
                ("checksum_candidate_posture",),
                ("signature_candidate_posture",),
                ("packet_candidate_posture",),
                ("command_candidate_posture",),
            ),
        ]
        for _name, expected_code, *paths in cases:
            with self.subTest(missing=_name):
                request = without_nested(declared_request(), *paths)
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_collapse_flags_block_with_representative_codes(self) -> None:
        cases = [
            ("evidence_became_source", "EVIDENCE_TREATED_AS_SOURCE"),
            ("evidence_became_authority", "EVIDENCE_TREATED_AS_AUTHORITY"),
            ("evidence_created_currentness", "EVIDENCE_TREATED_AS_CURRENTNESS"),
            ("manifest_implemented", "MANIFEST_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
            ("checksum_implemented", "CHECKSUM_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
            ("signature_implemented", "SIGNATURE_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
            ("packet_implemented", "PACKET_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
            ("command_implemented", "COMMAND_CANDIDATE_TREATED_AS_IMPLEMENTATION"),
            ("path_created_currentness", "PATH_TREATED_AS_CURRENTNESS"),
            ("latest_file_created_currentness", "LATEST_FILE_TREATED_AS_CURRENTNESS"),
            ("artifact_existence_created_currentness", "ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"),
            ("repository_copy_became_body", "REPOSITORY_COPY_TREATED_AS_BODY"),
            ("carrier_possession_created_currentness", "CARRIER_POSSESSION_TREATED_AS_CURRENTNESS"),
            ("narration_created_currentness", "NARRATION_TREATED_AS_CURRENTNESS"),
            ("source_transferred", "EVIDENCE_REVIEW_CREATES_TRANSFER"),
            ("source_migrated", "EVIDENCE_REVIEW_CREATES_MIGRATION"),
            ("source_receipt_created", "EVIDENCE_REVIEW_CREATES_SOURCE_RECEIPT"),
            ("reception_authorized", "EVIDENCE_REVIEW_AUTHORIZES_RECEPTION"),
            ("deployment_created", "EVIDENCE_REVIEW_CREATES_DEPLOYMENT"),
            ("runtime_hosting_created", "EVIDENCE_REVIEW_CREATES_RUNTIME_HOSTING"),
            ("public_release_created", "EVIDENCE_REVIEW_CREATES_PUBLIC_RELEASE"),
            ("continuation_authorized", "EVIDENCE_REVIEW_AUTHORIZES_CONTINUATION"),
            ("reusable_permission_created", "EVIDENCE_REVIEW_CREATES_REUSABLE_PERMISSION"),
            ("derivative_reception_authorized", "EVIDENCE_REVIEW_AUTHORIZES_DERIVATIVE_RECEPTION"),
            ("vessel_relation_authorized", "EVIDENCE_REVIEW_AUTHORIZES_VESSEL_RELATION"),
            ("another_reception_request_authorized", "EVIDENCE_REVIEW_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
            ("follow_on_work_authorized", "EVIDENCE_REVIEW_AUTHORIZES_FOLLOW_ON_WORK"),
        ]
        for flag, expected_code in cases:
            with self.subTest(flag=flag):
                request = declared_request(**{flag: True})
                request["declared_non_claims"][flag] = True if flag in request["declared_non_claims"] else False
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_mutation_replay_merge_and_non_claim_failures_block(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = declared_request(**{flag: True})
                request["declared_non_claims"][flag] = True
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(
                    result["block"]["block_code"],
                    "MUTATION_REPLAY_OR_MERGE_DETECTED",
                )

        missing_non_claim = declared_request()
        missing_non_claim["declared_non_claims"].pop("evidence_became_source")
        result = self.resolve(missing_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = declared_request()
        flipped_non_claim["declared_non_claims"]["operation_permission_created"] = True
        result = self.resolve(flipped_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {
                "NON_CLAIM_MISSING_OR_FLIPPED",
                "EVIDENCE_REVIEW_CREATES_OPERATION_PERMISSION",
            },
        )

    def test_outcome_family_is_closed_for_representative_results(self) -> None:
        results = [
            self.resolve(declared_request()),
            self.resolve(declared_request(requested_evidence_manifest_outcome=NOT_RECORDED)),
            self.resolve(
                declared_request(
                    requested_evidence_manifest_outcome=REQUIRES_ADDITIONAL_BASIS
                )
            ),
            self.resolve(declared_request(evidence_became_source=True)),
        ]
        for result in results:
            self.assertIn(result["outcome"], OUTCOME_FAMILY)


if __name__ == "__main__":
    unittest.main()
