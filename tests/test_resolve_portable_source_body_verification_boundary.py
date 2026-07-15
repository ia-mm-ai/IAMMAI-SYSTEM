"""Bounded tests for the portable source-body verification boundary resolver.

These tests prove only the verification boundary. Verification records
carrier-independent verification posture; it is not transfer, migration, source
receipt, reception authorization, deployment, runtime hosting, publication,
adoption, authority, currentness, continuation, reusable permission, derivative
reception, vessel relation, public release, or follow-on work.
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

import resolve_portable_source_body_verification_boundary as resolver  # noqa: E402


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_PORTABLE_VERIFICATION_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTPUT_FALSE_POSTURE = tuple(resolver.OUTPUT_FALSE_POSTURE)
ALLOWED_RECORDED_TRUE_FIELDS = tuple(resolver.ALLOWED_RECORDED_TRUE_FIELDS)

TOP_LEVEL_SECTIONS = {
    "portable_source_body_verification_metadata",
    "declared_portable_verification_question",
    "selected_source_body_basis",
    "selected_closure_basis",
    "selected_reception_closure_basis",
    "selected_terminal_summary_basis",
    "verifying_carrier",
    "original_carrier",
    "required_surfaces",
    "verification_evidence_basis",
    "carrier_independence_basis",
    "verification_scope",
    "verification_checks",
    "verification_statement",
    "verification_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "portable_source_body_verification_summary",
}

QUESTION = (
    "Can this selected closed source-body basis be verified on another "
    "technical carrier without carrier capture or carrier authority?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def selected_reception_closure_basis() -> dict:
    closure_non_claims = {
        "reception_authorized": False,
        "source_received": False,
        "source_receipt_recorded": False,
        "source_receipt_created": False,
        "adoption_created": False,
        "authority_created": False,
        "currentness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "reusable_permission_created": False,
        "another_reception_request_authorized": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
    }
    return {
        "source_body_reception_closure_artifact_id": (
            "source_body_reception_closure_reference_review_001_corrected"
        ),
        "outcome": "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED",
        "failed_check_count": 0,
        "closure_statement": {
            "source_body_reception_closure_recorded": True,
            "source_body_reception_boundary_chain_closed": True,
            "reception_closure_passed": True,
            "reception_family_closure_recorded": True,
            "bounded_chain_closure_only": True,
            "closure_is_not_authorization": True,
            "closure_is_not_source_receipt": True,
            "closure_does_not_receive_source": True,
            "closure_does_not_create_source_receipt": True,
            "closure_is_not_final_completion": True,
            "closure_does_not_authorize_continuation": True,
            "closure_does_not_create_reusable_permission": True,
            "closure_does_not_authorize_another_reception_request": True,
        },
        "source_body_reception_closure_summary": {
            "outcome": "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED",
            "failed_check_count": 0,
            "source_body_reception_closure_recorded": True,
            "source_body_reception_boundary_chain_closed": True,
            "reception_closure_passed": True,
            "reception_family_closure_recorded": True,
            "closure_not_authorization_source_receipt_final_completion_continuation_reusable_permission": True,
        },
        "non_claims": closure_non_claims,
        "closure_did_not_authorize_reception": True,
        "closure_did_not_receive_source": True,
        "closure_did_not_record_source_receipt": True,
        "closure_did_not_create_source_receipt": True,
        "closure_did_not_create_final_completion": True,
        "closure_did_not_authorize_continuation": True,
        "closure_did_not_create_reusable_permission": True,
        "closure_did_not_authorize_another_reception_request": True,
    }


def selected_terminal_summary_basis() -> dict:
    return {
        "terminal_summary_declared": True,
        "selected_terminal_summary_basis_reference": (
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ),
        "selected_terminal_summary_basis_path": (
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ),
        "terminal_summary_reference": (
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ),
        "terminal_summary_path": (
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ),
        "records_closed_source_body_reception_chain": True,
        "does_not_authorize_successor_boundary": True,
        "does_not_authorize_next_work": True,
    }


def selected_closure_basis() -> dict:
    return {
        "selected_source_body_closure_basis_id": "closed-source-body-basis-closure-001",
        "selected_closure_basis_declared": True,
        "selected_closure_basis_remains_bounded_closure_only": True,
        "selected_reception_closure_did_not_authorize_permission": True,
        "source_remains_unreplaced": True,
        "does_not_authorize_next_work": True,
    }


def selected_source_body_basis() -> dict:
    return {
        "selected_source_body_basis_id": "portable-source-body-basis-001",
        "selected_source_body_basis_reference": "closed-source-body-basis:001",
        "selected_source_body_closure_basis": selected_closure_basis(),
        "selected_source_body_reception_closure_basis": selected_reception_closure_basis(),
        "selected_source_body_reception_terminal_summary": selected_terminal_summary_basis(),
        "selected_distributed_operation_closure_terminal_basis": {
            "distributed_operation_terminal_summary_declared": True,
            "reference": "spec/DISTRIBUTED_OPERATION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
        },
        "selected_current_body_conformance_orientation_basis": {
            "current_body_basis_declared": True,
            "conformance_reference": "spec/CURRENT_BODY_CONFORMANCE_V4_CLOSURE_V0_MIN_SPEC.md",
            "orientation_reference": "spec/CURRENT_SELF_ORIENTATION_V9_V0_MIN_SPEC.md",
        },
        "required_source_surfaces": ["reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md"],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_V0_MIN_SPEC.md"
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_source_body_reception_closure_boundary/"
        ],
        "required_closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "selected_corrected_closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "selected_failed_input_evidence_artifacts": [
            "source_body_reception_closure_reference_review_001_failed_input_evidence.json"
        ],
        "failed_input_evidence_posture": {"failed_input_evidence_visible_only": True},
        "basis_remains_bounded_evidence_only": True,
        "basis_does_not_create_transfer": True,
        "basis_does_not_create_migration": True,
        "basis_does_not_create_currentness": True,
        "basis_does_not_create_carrier_authority": True,
        "basis_does_not_authorize_next_work": True,
    }


def verifying_carrier() -> dict:
    return {
        "verifying_carrier_id": "technical-carrier-b",
        "verifying_carrier_name": "Independent verification carrier",
        "verifying_carrier_reference": "carrier:b",
        "verifying_carrier_type": "technical_carrier",
        "verifying_carrier_declared": True,
        "verifying_carrier_may_hold_evidence": True,
        "verifying_carrier_may_check_evidence": True,
        "verifying_carrier_is_not_source": True,
        "verifying_carrier_is_not_authority": True,
        "verifying_carrier_is_not_current": True,
        "verifying_carrier_does_not_replace_source": True,
        "verifying_carrier_does_not_receive_source": True,
        "verifying_carrier_does_not_create_source_receipt": True,
        "verifying_carrier_does_not_create_currentness": True,
        "verifying_carrier_does_not_create_operation_permission": True,
        "verifying_carrier_does_not_create_public_readiness": True,
        "verifying_carrier_does_not_authorize_continuation": True,
        "verifying_carrier_does_not_create_reusable_permission": True,
        "verifying_carrier_does_not_authorize_another_reception_request": True,
    }


def original_carrier() -> dict:
    return {
        "original_carrier_id": "technical-carrier-a",
        "original_carrier_name": "Original local carrier",
        "original_carrier_reference": "carrier:a",
        "original_carrier_type": "technical_carrier",
        "original_carrier_declared": True,
        "original_carrier_is_not_continuing_authority_by_default": True,
        "original_carrier_is_not_source_merely_because_it_was_original": True,
        "original_carrier_possession_is_not_currentness": True,
        "original_carrier_path_recency_vendor_account_posture_does_not_create_authority": True,
    }


def required_surfaces() -> dict:
    return {
        "required_source_surfaces": ["reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md"],
        "required_spec_surfaces": [
            "spec/PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_V0_MIN_SPEC.md",
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
        ],
        "required_resolver_surfaces": [
            "src/resolve_portable_source_body_verification_boundary.py"
        ],
        "required_test_surfaces": [
            "tests/test_resolve_portable_source_body_verification_boundary.py"
        ],
        "required_artifact_roots": [
            "artifacts/integrity_host_v0_min_coexistence_source_body_reception_closure_boundary/"
        ],
        "required_closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "selected_terminal_summaries": [
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ],
        "selected_corrected_closure_artifacts": [
            "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
        ],
        "selected_failed_input_evidence_artifacts": [
            "source_body_reception_closure_reference_review_001_failed_input_evidence.json"
        ],
        "manifest_candidate_basis": {"future_evidence_only": True},
        "checksum_candidate_basis": {"future_evidence_only": True},
        "signature_candidate_basis": {"future_evidence_only": True},
        "surfaces_are_evidence_only": True,
        "surfaces_do_not_create_currentness_by_existence": True,
        "surfaces_do_not_create_permission_by_existence": True,
    }


def verification_evidence_basis() -> dict:
    return {
        "verification_evidence_basis_declared": True,
        "declared_evidence_classes": [
            "source_surfaces",
            "spec_surfaces",
            "resolver_surfaces",
            "test_surfaces",
            "artifact_roots",
            "closure_artifacts",
        ],
        "selected_source_body_basis": "closed-source-body-basis:001",
        "selected_reception_closure_basis": (
            "source_body_reception_closure_reference_review_001_corrected"
        ),
        "selected_terminal_summary_basis": (
            "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md"
        ),
        "carrier_independent_verification_evidence": True,
        "evidence_readability_posture": {"declared": True},
        "manifest_checksum_signature_candidate_posture": "future_evidence_only",
        "evidence_does_not_replace_source": True,
        "evidence_does_not_make_carrier_source": True,
        "evidence_does_not_create_currentness": True,
        "evidence_does_not_create_transfer_migration_source_receipt_authorization_deployment_public_release_runtime_hosting": True,
    }


def carrier_independence_basis() -> dict:
    return {
        "carrier_independence_basis_declared": True,
        "no_carrier_authority": True,
        "no_device_authority": True,
        "no_operating_system_authority": True,
        "no_vendor_authority": True,
        "no_account_authority": True,
        "no_local_path_currentness": True,
        "no_latest_file_currentness": True,
        "no_recency_currentness": True,
        "no_repository_possession_currentness": True,
        "no_artifact_existence_currentness": True,
        "no_carrier_possession_currentness": True,
        "no_archive_possession_currentness": True,
        "no_narrator_trust_currentness": True,
        "source_is_not_replaced_by_carrier_copy_archive_path_manifest_checksum_repository": True,
        "original_carrier_is_not_sovereign_by_default": True,
        "verifying_carrier_is_not_source_or_authority": True,
    }


def base_request() -> dict:
    request = resolver.build_declared_portable_source_body_verification_request(
        portable_verification_request_id="portable_verification_request_001",
        portable_verification_question=QUESTION,
        selected_source_body_basis=selected_source_body_basis(),
        selected_closure_basis=selected_closure_basis(),
        selected_reception_closure_basis=selected_reception_closure_basis(),
        selected_terminal_summary_basis=selected_terminal_summary_basis(),
        verifying_carrier=verifying_carrier(),
        original_carrier=original_carrier(),
        required_surfaces=required_surfaces(),
        verification_evidence_basis=verification_evidence_basis(),
        carrier_independence_basis=carrier_independence_basis(),
        verification_scope=SUPPORTED_SCOPE,
        selected_reception_closure_artifact_id=(
            "source_body_reception_closure_reference_review_001_corrected"
        ),
        selected_reception_closure_artifact_outcome=(
            "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED"
        ),
    )
    request.update(
        {
            "selected_distributed_operation_terminal_summary": {
                "distributed_operation_terminal_summary_declared": True,
                "reference": "spec/DISTRIBUTED_OPERATION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md",
            },
            "selected_current_body_basis": {
                "current_body_basis_declared": True,
                "reference": "spec/CURRENT_BODY_CONFORMANCE_V4_CLOSURE_V0_MIN_SPEC.md",
            },
            "selected_corrected_closure_artifacts": [
                "source_body_reception_closure_reference_review_001_corrected__source_body_reception_closure_result.json"
            ],
            "selected_failed_input_evidence_artifacts": [
                "source_body_reception_closure_reference_review_001_failed_input_evidence.json"
            ],
            "failed_input_evidence_posture": {
                "failed_input_evidence_visible_only": True
            },
            "verification_surface_readability": {"declared": True},
            "manifest_candidate_basis": {"future_evidence_only": True},
            "checksum_candidate_basis": {"future_evidence_only": True},
            "signature_candidate_basis": {"future_evidence_only": True},
        }
    )
    return request


def block_code(result: dict) -> str | None:
    return result["block"]["block_code"]


class PortableSourceBodyVerificationBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        if request is None:
            request = base_request()
        return resolver.resolve_portable_source_body_verification_boundary(
            declared_portable_verification_request=request
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["portable_source_body_verification_summary"]["failed_check_count"],
            0,
        )
        statement = result["verification_statement"]
        self.assertTrue(statement["portable_source_body_verification_recorded"])
        self.assertTrue(statement["portable_source_body_basis_verified"])
        self.assertTrue(statement["carrier_independent_verification_recorded"])
        for key in OUTPUT_FALSE_POSTURE:
            self.assertFalse(statement[key], key)
        for key in REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)

    def assert_not_recorded_posture(self, result: dict) -> None:
        statement = result["verification_statement"]
        for key in ALLOWED_RECORDED_TRUE_FIELDS:
            self.assertFalse(statement[key], key)
        for key in OUTPUT_FALSE_POSTURE:
            self.assertFalse(statement[key], key)
        for key in REQUIRED_NON_CLAIMS:
            self.assertFalse(result["non_claims"][key], key)

    def test_successful_portable_verification_recorded_result(self) -> None:
        result = self.resolve()

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assert_recorded(result)

        statement = result["verification_statement"]
        true_fields = [
            "selected_source_body_basis_preserved",
            "selected_closure_basis_preserved",
            "selected_reception_closure_basis_preserved",
            "selected_terminal_summary_basis_preserved",
            "required_surfaces_preserved",
            "verification_evidence_basis_declared",
            "carrier_independence_basis_declared",
            "verification_only_posture",
            "carrier_independent_verification_only",
            "verifying_carrier_is_not_source",
            "verifying_carrier_is_not_authority",
            "original_carrier_is_not_continuing_authority_by_default",
            "device_is_not_authority",
            "os_is_not_authority",
            "vendor_is_not_authority",
            "account_is_not_authority",
            "local_path_is_not_currentness",
            "latest_file_is_not_currentness",
            "recency_is_not_currentness",
            "repository_possession_is_not_currentness",
            "artifact_existence_is_not_currentness",
            "carrier_possession_is_not_currentness",
            "archive_possession_is_not_currentness",
            "narration_is_not_currentness",
            "verification_is_not_transfer",
            "verification_is_not_migration",
            "verification_is_not_source_receipt",
            "verification_is_not_reception_authorization",
            "verification_is_not_deployment",
            "verification_is_not_runtime_hosting",
            "verification_is_not_publication",
            "verification_is_not_adoption",
            "verification_is_not_authority",
            "verification_is_not_currentness",
        ]
        for key in true_fields:
            self.assertTrue(statement[key], key)

    def test_metadata_declared_basis_carriers_surfaces_and_summary(self) -> None:
        result = self.resolve()
        metadata = result["portable_source_body_verification_metadata"]
        self.assertTrue(metadata["portable_source_body_verification_result_id"])
        self.assertTrue(metadata["portable_source_body_verification_result_type"])
        self.assertEqual(metadata["portable_source_body_verification_result_version"], "0.1.0")
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_portable_source_body_verification_boundary",
        )

        declared = result["declared_portable_verification_question"]
        self.assertEqual(declared["portable_verification_request_id"], "portable_verification_request_001")
        self.assertEqual(declared["portable_verification_question"], QUESTION)
        self.assertEqual(
            declared["portable_verification_intent"],
            "RECORD_PORTABLE_SOURCE_BODY_VERIFICATION",
        )
        self.assertEqual(declared["selected_source_body_basis_id"], "portable-source-body-basis-001")
        self.assertEqual(declared["selected_source_body_basis_reference"], "closed-source-body-basis:001")
        self.assertEqual(
            declared["selected_reception_closure_artifact_id"],
            "source_body_reception_closure_reference_review_001_corrected",
        )
        self.assertEqual(
            declared["selected_reception_closure_artifact_outcome"],
            "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED",
        )
        self.assertEqual(declared["selected_terminal_summary_basis_reference"], "spec/SOURCE_BODY_RECEPTION_BOUNDARY_CHAIN_TERMINAL_SUMMARY_V0.md")
        self.assertEqual(declared["verifying_carrier_id"], "technical-carrier-b")
        self.assertEqual(declared["verifying_carrier_type"], "technical_carrier")
        self.assertEqual(declared["original_carrier_id"], "technical-carrier-a")
        self.assertTrue(declared["verification_is_not_transfer"])
        self.assertTrue(declared["verification_is_not_migration"])
        self.assertTrue(declared["verification_is_not_source_receipt"])
        self.assertTrue(declared["verification_is_not_reception_authorization"])
        self.assertTrue(declared["verification_is_not_deployment"])
        self.assertTrue(declared["verification_is_not_runtime_hosting"])
        self.assertTrue(declared["verification_is_not_publication"])
        self.assertTrue(declared["verification_does_not_authorize_continuation"])
        self.assertTrue(declared["verification_does_not_create_reusable_permission"])

        selected = result["selected_source_body_basis"]
        self.assertEqual(selected["selected_source_body_basis_id"], "portable-source-body-basis-001")
        self.assertEqual(selected["selected_source_body_basis_reference"], "closed-source-body-basis:001")
        self.assertTrue(selected["selected_source_body_closure_basis"])
        self.assertTrue(selected["selected_source_body_reception_closure_basis"])
        self.assertTrue(selected["selected_source_body_reception_terminal_summary"])
        self.assertTrue(selected["selected_distributed_operation_closure_terminal_basis"])
        self.assertTrue(selected["selected_current_body_conformance_orientation_basis"])
        self.assertTrue(selected["required_source_surfaces"])
        self.assertTrue(selected["required_spec_surfaces"])
        self.assertTrue(selected["required_resolver_surfaces"])
        self.assertTrue(selected["required_test_surfaces"])
        self.assertTrue(selected["required_artifact_roots"])
        self.assertTrue(selected["required_closure_artifacts"])
        self.assertTrue(selected["selected_corrected_closure_artifacts"])
        self.assertTrue(selected["failed_input_evidence_posture"])
        self.assertTrue(selected["selected_basis_remains_bounded_evidence_only"])
        self.assertTrue(selected["selected_basis_does_not_create_source_transfer"])
        self.assertTrue(selected["selected_basis_does_not_create_source_migration"])
        self.assertTrue(selected["selected_basis_does_not_create_currentness"])
        self.assertTrue(selected["selected_basis_does_not_create_carrier_authority"])
        self.assertTrue(selected["selected_basis_does_not_authorize_next_work"])
        self.assertEqual(selected["raw_selected_source_body_basis"], selected_source_body_basis())

        verifying = result["verifying_carrier"]
        self.assertEqual(verifying["verifying_carrier_id"], "technical-carrier-b")
        self.assertEqual(verifying["verifying_carrier_name"], "Independent verification carrier")
        self.assertEqual(verifying["verifying_carrier_reference"], "carrier:b")
        self.assertEqual(verifying["verifying_carrier_type"], "technical_carrier")
        for key in (
            "verifying_carrier_declared",
            "verifying_carrier_may_hold_evidence",
            "verifying_carrier_may_check_evidence",
            "verifying_carrier_is_not_source",
            "verifying_carrier_is_not_authority",
            "verifying_carrier_is_not_current",
            "verifying_carrier_does_not_replace_source",
            "verifying_carrier_does_not_receive_source",
            "verifying_carrier_does_not_create_source_receipt",
            "verifying_carrier_does_not_create_currentness",
            "verifying_carrier_does_not_create_operation_permission",
            "verifying_carrier_does_not_create_public_readiness",
            "verifying_carrier_does_not_authorize_continuation",
            "verifying_carrier_does_not_create_reusable_permission",
            "verifying_carrier_does_not_authorize_another_reception_request",
        ):
            self.assertTrue(verifying[key], key)

        original = result["original_carrier"]
        self.assertEqual(original["original_carrier_id"], "technical-carrier-a")
        self.assertEqual(original["original_carrier_name"], "Original local carrier")
        self.assertEqual(original["original_carrier_reference"], "carrier:a")
        self.assertEqual(original["original_carrier_type"], "technical_carrier")
        self.assertTrue(original["original_carrier_declared"])
        self.assertTrue(original["original_carrier_is_not_continuing_authority_by_default"])
        self.assertTrue(original["original_carrier_is_not_source_merely_because_it_was_original"])
        self.assertTrue(original["original_carrier_possession_is_not_currentness"])
        self.assertTrue(original["original_carrier_path_recency_vendor_account_posture_does_not_create_authority"])

        surfaces = result["required_surfaces"]
        self.assertTrue(surfaces["required_source_surfaces"])
        self.assertTrue(surfaces["required_spec_surfaces"])
        self.assertTrue(surfaces["required_resolver_surfaces"])
        self.assertTrue(surfaces["required_test_surfaces"])
        self.assertTrue(surfaces["required_artifact_roots"])
        self.assertTrue(surfaces["required_closure_artifacts"])
        self.assertTrue(surfaces["selected_terminal_summaries"])
        self.assertTrue(surfaces["selected_corrected_closure_artifacts"])
        self.assertTrue(surfaces["selected_failed_input_evidence_artifacts"])
        self.assertTrue(surfaces["manifest_checksum_signature_are_future_evidence_language_only"])
        self.assertTrue(surfaces["surfaces_are_evidence_only"])
        self.assertTrue(surfaces["surfaces_do_not_create_currentness_by_existence"])
        self.assertTrue(surfaces["surfaces_do_not_create_permission_by_existence"])

        evidence = result["verification_evidence_basis"]
        self.assertTrue(
            evidence["verification_evidence_basis_as_supplied"][
                "verification_evidence_basis_declared"
            ]
        )
        self.assertTrue(evidence["carrier_independent_verification_evidence"])
        self.assertTrue(evidence["evidence_does_not_replace_source"])
        self.assertTrue(evidence["evidence_does_not_make_carrier_source"])
        self.assertTrue(evidence["evidence_does_not_create_currentness"])
        self.assertTrue(evidence["evidence_does_not_create_transfer_migration_source_receipt_authorization_deployment_public_release_runtime_hosting"])

        independence = result["carrier_independence_basis"]
        self.assertTrue(
            independence["carrier_independence_basis_as_supplied"][
                "carrier_independence_basis_declared"
            ]
        )
        for key in (
            "no_carrier_authority",
            "no_device_authority",
            "no_operating_system_authority",
            "no_vendor_authority",
            "no_account_authority",
            "no_local_path_currentness",
            "no_latest_file_currentness",
            "no_recency_currentness",
            "no_repository_possession_currentness",
            "no_artifact_existence_currentness",
            "no_carrier_possession_currentness",
            "no_archive_possession_currentness",
            "no_narrator_trust_currentness",
            "source_is_not_replaced_by_carrier_copy_archive_path_manifest_checksum_repository",
            "original_carrier_is_not_sovereign_by_default",
            "verifying_carrier_is_not_source_or_authority",
        ):
            self.assertTrue(independence[key], key)

        summary = resolver.build_portable_source_body_verification_summary(result)
        expected_summary_keys = {
            "outcome",
            "block_code",
            "block_reason",
            "portable_verification_request_id",
            "portable_verification_question",
            "portable_verification_intent",
            "selected_source_body_basis_id",
            "selected_source_body_basis_reference",
            "selected_reception_closure_artifact_id",
            "selected_reception_closure_artifact_outcome",
            "selected_reception_closure_artifact_path",
            "selected_terminal_summary_basis_reference",
            "selected_terminal_summary_basis_path",
            "verifying_carrier_id",
            "verifying_carrier_type",
            "verifying_carrier_reference",
            "original_carrier_id",
            "original_carrier_type",
            "original_carrier_reference",
            "passed_check_count",
            "failed_check_count",
            "portable_verification_recorded",
            "portable_source_body_basis_verified",
            "carrier_independent_verification_recorded",
            "not_recorded",
            "requires_additional_basis",
            "selected_source_body_basis_preserved",
            "selected_closure_basis_preserved",
            "selected_reception_closure_basis_preserved",
            "selected_terminal_summary_basis_preserved",
            "required_surfaces_preserved",
            "verification_evidence_basis_declared",
            "carrier_independence_basis_declared",
            "verification_only_posture",
            "verifying_carrier_not_source",
            "verifying_carrier_not_authority",
            "original_carrier_not_continuing_authority_by_default",
            "device_os_vendor_account_not_authority",
            "path_latest_recency_repository_artifact_carrier_archive_narration_not_currentness",
            "verification_not_transfer_migration_source_receipt_reception_authorization_deployment_runtime_publication_adoption_authority_currentness",
            "no_source_replaced_transferred_migrated_received",
            "no_source_receipt_recorded",
            "no_adoption_authority_currentness_standing",
            "no_operation_permission_public_readiness_final_completion",
            "no_continuation_publication_flow_reusable_permission",
            "no_another_reception_request_authorized",
            "no_derivative_reception_vessel_relation",
            "no_runtime_hosting_deployment_public_release",
            "key_non_claims",
        }
        self.assertTrue(expected_summary_keys.issubset(summary))
        self.assertEqual(summary["outcome"], RECORDED)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["verification_only_posture"])
        self.assertFalse(summary["key_non_claims"]["source_transferred"])

    def test_supported_scope_values_and_unsupported_scope(self) -> None:
        for scope_value in SUPPORTED_SCOPE:
            request = base_request()
            request["verification_scope"] = [scope_value]
            with self.subTest(scope_value=scope_value):
                self.assertEqual(self.resolve(request)["outcome"], RECORDED)

        request = base_request()
        request["verification_scope"] = ["PORTABLE_VERIFICATION_AS_DEPLOYMENT"]
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_PORTABLE_VERIFICATION_SCOPE")

    def test_verification_checks_are_explicit_and_pass(self) -> None:
        result = self.resolve()
        checks = result["verification_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertTrue("block_code" in check or "failure_code" in check)
            self.assertTrue(check["passed"], check["check_name"])
        self.assertEqual(
            result["portable_source_body_verification_summary"]["failed_check_count"],
            0,
        )

        check_names = {check["check_name"] for check in checks}
        required_check_names = {
            "portable_verification_question_declared",
            "portable_verification_intent_supported",
            "selected_closed_source_body_basis_declared",
            "selected_source_body_reception_terminal_summary_declared",
            "selected_source_body_reception_closure_basis_declared",
            "required_source_surfaces_declared",
            "required_spec_surfaces_declared",
            "required_resolver_surfaces_declared",
            "required_test_surfaces_declared",
            "required_artifact_roots_declared",
            "required_closure_artifacts_declared",
            "verifying_carrier_declared",
            "original_carrier_declared",
            "carrier_independence_basis_declared",
            "verification_evidence_basis_declared",
            "verification_scope_supported",
            "selected_closure_basis_bounded_closure_only",
            "selected_reception_closure_did_not_authorize_permission",
            "source_unreplaced",
            "verifying_carrier_not_source",
            "verifying_carrier_not_authority",
            "original_carrier_not_continuing_authority_by_default",
            "device_not_authority",
            "os_not_authority",
            "vendor_not_authority",
            "account_not_authority",
            "local_path_not_currentness",
            "latest_file_not_currentness",
            "recency_not_currentness",
            "repository_possession_not_currentness",
            "artifact_existence_not_currentness",
            "carrier_possession_not_currentness",
            "archive_possession_not_currentness",
            "human_narration_not_currentness",
            "verification_does_not_authorize_reception",
            "verification_does_not_receive_source",
            "verification_does_not_record_source_receipt",
            "verification_does_not_create_source_receipt",
            "verification_does_not_transfer_source",
            "verification_does_not_migrate_source",
            "verification_does_not_create_adoption",
            "verification_does_not_create_authority",
            "verification_does_not_create_currentness",
            "verification_does_not_create_standing",
            "verification_does_not_create_operation_permission",
            "verification_does_not_create_public_readiness",
            "verification_does_not_claim_final_completion",
            "verification_does_not_authorize_continuation",
            "verification_does_not_authorize_follow_on_work",
            "verification_does_not_open_publication_flow",
            "verification_does_not_create_reusable_permission",
            "verification_does_not_authorize_another_reception_request",
            "verification_does_not_authorize_derivative_reception",
            "verification_does_not_authorize_vessel_relation",
            "verification_does_not_create_runtime_hosting",
            "verification_does_not_create_deployment",
            "verification_does_not_create_public_release",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        self.assertTrue(required_check_names.issubset(check_names))

    def test_verification_statement_non_meaning_and_open_items(self) -> None:
        recorded = self.resolve()
        self.assert_recorded(recorded)
        for outcome in (NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS):
            request = base_request()
            request["requested_verification_outcome"] = outcome
            result = self.resolve(request)
            self.assertEqual(result["outcome"], outcome)
            self.assert_not_recorded_posture(result)

        non_meaning = recorded["verification_non_meaning"]
        for key in (
            "verification_does_not_mean_source_body_transferred",
            "verification_does_not_mean_source_body_migrated",
            "verification_does_not_mean_source_received",
            "verification_does_not_mean_source_receipt_recorded",
            "verification_does_not_mean_source_receipt_created",
            "verification_does_not_mean_carrier_became_source",
            "verification_does_not_mean_carrier_became_authority",
            "verification_does_not_mean_device_became_authority",
            "verification_does_not_mean_operating_system_became_authority",
            "verification_does_not_mean_vendor_environment_became_authority",
            "verification_does_not_mean_account_became_authority",
            "verification_does_not_mean_repository_copy_became_source_body",
            "verification_does_not_mean_local_path_created_currentness",
            "verification_does_not_mean_latest_file_created_currentness",
            "verification_does_not_mean_recency_created_currentness",
            "verification_does_not_mean_human_narration_created_currentness",
            "verification_does_not_mean_artifact_existence_created_currentness",
            "verification_does_not_mean_carrier_possession_created_currentness",
            "verification_does_not_mean_archive_possession_created_currentness",
            "verification_does_not_mean_adoption_created",
            "verification_does_not_mean_authority_created",
            "verification_does_not_mean_currentness_created",
            "verification_does_not_mean_standing_created",
            "verification_does_not_mean_operation_permission_created",
            "verification_does_not_mean_public_readiness_created",
            "verification_does_not_mean_final_completion_claimed",
            "verification_does_not_mean_continuation_authorized",
            "verification_does_not_mean_follow_on_work_authorized",
            "verification_does_not_mean_publication_flow_opened",
            "verification_does_not_mean_reusable_permission_created",
            "verification_does_not_mean_derivative_reception_authorized",
            "verification_does_not_mean_vessel_relation_authorized",
            "verification_does_not_mean_another_source_body_reception_request_authorized",
            "verification_does_not_mean_runtime_hosting_created",
            "verification_does_not_mean_deployment_created",
            "verification_does_not_mean_product_packaging_created",
            "verification_does_not_mean_public_release_created",
        ):
            self.assertTrue(non_meaning[key], key)

        remains_open = recorded["what_remains_open"]
        expected_open_items = {
            "portable source-body verification test",
            "portable source-body verification live artifact",
            "manifest or source-body packet work",
            "checksum or signature work",
            "portable verification command",
            "reproducible environment declaration",
            "technical carrier packet",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "standing creation",
            "operation permission",
            "receiving-context governance",
            "public readiness",
            "final completion",
            "follow-on work",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
            "runtime hosting",
            "deployment",
            "public release",
        }
        self.assertTrue(expected_open_items.issubset(set(remains_open["open_items"])))
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_requires_additional_basis_and_not_recorded(self) -> None:
        request = base_request()
        request["requested_verification_outcome"] = REQUIRES_ADDITIONAL_BASIS
        request["additional_basis_context"] = {
            "reason": "manifest requirements implied but not declared"
        }
        result = self.resolve(request)
        self.assertEqual(result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        additional = result["additional_basis_required"]
        self.assertTrue(additional["additional_basis_required"])
        self.assertEqual(additional["additional_basis_context"], request["additional_basis_context"])
        self.assertTrue(additional["missing_basis_not_scheduled"])
        self.assertTrue(additional["missing_basis_not_authorized"])
        self.assertTrue(additional["missing_basis_not_executed"])
        self.assert_not_recorded_posture(result)

        request = base_request()
        request["requested_verification_outcome"] = NOT_RECORDED
        request["not_recorded_basis"] = {
            "reason": "carrier independence cannot be preserved"
        }
        result = self.resolve(request)
        self.assertEqual(result["outcome"], NOT_RECORDED)
        not_recorded = result["not_recorded_basis"]
        self.assertTrue(not_recorded["not_recorded"])
        self.assertEqual(not_recorded["not_recorded_basis"], request["not_recorded_basis"])
        self.assertTrue(not_recorded["not_recorded_does_not_repair"])
        self.assertTrue(not_recorded["not_recorded_does_not_authorize"])
        self.assertTrue(not_recorded["not_recorded_does_not_authorize_follow_on_work"])
        self.assertTrue(not_recorded["not_recorded_does_not_transfer"])
        self.assertTrue(not_recorded["not_recorded_does_not_migrate"])
        self.assertTrue(not_recorded["not_recorded_does_not_deploy"])
        self.assertTrue(not_recorded["not_recorded_does_not_publish"])
        self.assertTrue(not_recorded["not_recorded_does_not_host"])
        self.assert_not_recorded_posture(result)

    def test_request_builder_helper_preserves_inputs_and_resolves(self) -> None:
        source_basis = selected_source_body_basis()
        closure_basis = selected_closure_basis()
        reception_closure = selected_reception_closure_basis()
        terminal_summary = selected_terminal_summary_basis()
        request = resolver.build_declared_portable_source_body_verification_request(
            "portable_verification_request_helper_001",
            QUESTION,
            source_basis,
            closure_basis,
            reception_closure,
            terminal_summary,
            verifying_carrier(),
            original_carrier(),
            required_surfaces(),
            verification_evidence_basis(),
            carrier_independence_basis(),
            SUPPORTED_SCOPE,
            selected_source_body_basis_path="basis.json",
            selected_reception_closure_artifact_path="closure.json",
            selected_reception_closure_artifact_id="closure-artifact-001",
            selected_reception_closure_artifact_outcome="SOURCE_BODY_RECEPTION_CLOSURE_RECORDED",
            additional_basis_context={"reason": "none"},
            not_recorded_basis={"reason": "none"},
        )

        self.assertEqual(request["portable_verification_request_id"], "portable_verification_request_helper_001")
        self.assertEqual(request["portable_verification_question"], QUESTION)
        self.assertEqual(request["selected_source_body_basis_path"], "basis.json")
        self.assertNotIn("selected_source_body_basis", request)
        self.assertEqual(request["selected_closure_basis"], closure_basis)
        self.assertEqual(request["selected_reception_closure_artifact_path"], "closure.json")
        self.assertNotIn("selected_reception_closure_basis", request)
        self.assertEqual(request["selected_terminal_summary_basis"], terminal_summary)
        self.assertEqual(request["verification_scope"], SUPPORTED_SCOPE)
        self.assertEqual(request["selected_reception_closure_artifact_id"], "closure-artifact-001")
        self.assertEqual(request["selected_reception_closure_artifact_outcome"], "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED")
        self.assertEqual(request["requested_verification_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], {"reason": "none"})
        self.assertEqual(request["not_recorded_basis"], {"reason": "none"})
        for key in REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][key], key)
        for forbidden in (
            "source_transferred",
            "source_migrated",
            "source_received",
            "source_receipt_recorded",
            "reception_authorized",
            "carrier_became_authority",
            "currentness_created",
            "deployment_created",
            "runtime_hosting_created",
            "public_release_created",
            "follow_on_work_authorized",
        ):
            self.assertFalse(request["declared_non_claims"][forbidden], forbidden)

        request["selected_source_body_basis_path"] = None
        request["selected_source_body_basis"] = source_basis
        request["selected_reception_closure_artifact_path"] = None
        request["selected_reception_closure_basis"] = reception_closure
        self.assert_recorded(self.resolve(request))

    def test_path_based_selected_source_body_basis_request_and_markdown_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            basis_path = tmp_path / "selected_source_body_basis.json"
            terminal_summary_path = tmp_path / "terminal_summary.md"
            request_path = tmp_path / "portable_verification_request.json"
            basis_path.write_text(json.dumps(selected_source_body_basis()), encoding="utf-8")
            terminal_summary_path.write_text("# Terminal Summary\nClosed chain only.\n", encoding="utf-8")

            request = base_request()
            request.pop("selected_source_body_basis")
            request["selected_source_body_basis_path"] = str(basis_path)
            request["selected_reception_terminal_summary_path"] = str(terminal_summary_path)
            result = self.resolve(request)
            self.assert_recorded(result)
            self.assertEqual(result["selected_source_body_basis"]["selected_source_body_basis_path"], str(basis_path))
            self.assertEqual(
                result["selected_source_body_basis"]["raw_selected_source_body_basis"],
                selected_source_body_basis(),
            )
            self.assertEqual(
                result["selected_terminal_summary_basis"]["selected_reception_terminal_summary_path"],
                str(terminal_summary_path),
            )
            metadata = result["selected_terminal_summary_basis"]["raw_selected_terminal_summary_basis"][
                "selected_reception_terminal_summary_path_metadata"
            ]
            self.assertTrue(metadata["path_readable"])
            self.assertTrue(metadata["path_is_evidence_only"])
            self.assertTrue(metadata["path_does_not_create_authority"])
            self.assertTrue(metadata["path_does_not_create_currentness"])
            self.assertFalse(result["non_claims"]["carrier_became_authority"])
            self.assertFalse(result["non_claims"]["local_path_created_currentness"])

            request_path.write_text(json.dumps(base_request()), encoding="utf-8")
            path_result = resolver.resolve_portable_source_body_verification_boundary_from_path(request_path)
            self.assert_recorded(path_result)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(path_result))
            self.assertEqual(
                path_result["declared_portable_verification_question"]["declared_portable_verification_request_path"],
                str(request_path),
            )

    def test_write_behavior_explicit_and_default_output_root(self) -> None:
        result = self.resolve()
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            explicit_path = tmp_path / "nested" / "portable_result.json"
            written = resolver.write_portable_source_body_verification_result(result, explicit_path)
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            root = tmp_path / "portable-root"
            with patch.object(resolver, "PORTABLE_SOURCE_BODY_VERIFICATION_BOUNDARY_ROOT", root):
                first = resolver.write_portable_source_body_verification_result(result)
                second = resolver.write_portable_source_body_verification_result(result)
            self.assertEqual(first.parent, root)
            self.assertEqual(second.parent, root)
            self.assertNotEqual(first, second)
            self.assertTrue(second.stem.endswith("_001"))
            self.assertIn("portable_source_body_verification_result", first.name)
            self.assertNotIn("source_body_reception_closure", str(first.parent))
            self.assertNotIn("manifest", str(first.parent))
            self.assertNotIn("checksum", str(first.parent))
            self.assertNotIn("deployment", str(first.parent))
            self.assertNotIn("runtime", str(first.parent))
            self.assertNotIn("public-release", str(first.parent))

    def test_non_mutation_posture(self) -> None:
        request = base_request()
        original = copy.deepcopy(request)
        result = self.resolve(request)
        self.assert_recorded(result)
        self.assertEqual(request, original)

        second = self.resolve(request)
        self.assert_recorded(second)
        self.assertEqual(request, original)

        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "portable" / "result.json"
            resolver.write_portable_source_body_verification_result(result, output_path)
            self.assertEqual(request, original)
            self.assertTrue(output_path.exists())

    def test_blocking_missing_malformed_request_and_request_paths(self) -> None:
        result = resolver.resolve_portable_source_body_verification_boundary()
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "PORTABLE_VERIFICATION_QUESTION_UNDECLARED")

        result = resolver.resolve_portable_source_body_verification_boundary(
            declared_portable_verification_request=["not", "a", "mapping"]
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED")

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_path = tmp_path / "missing.json"
            result = resolver.resolve_portable_source_body_verification_boundary_from_path(missing_path)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_PORTABLE_VERIFICATION_REQUEST_UNREADABLE")

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_boundary_from_path(malformed_path)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text(json.dumps(["not", "an", "object"]), encoding="utf-8")
            result = resolver.resolve_portable_source_body_verification_boundary_from_path(array_path)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "DECLARED_PORTABLE_VERIFICATION_REQUEST_MALFORMED")

    def test_blocking_selected_source_body_basis_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request = base_request()
            request.pop("selected_source_body_basis")
            request["selected_source_body_basis_path"] = str(tmp_path / "missing.json")
            result = self.resolve(request)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "SELECTED_SOURCE_BODY_BASIS_UNREADABLE")

            malformed = tmp_path / "malformed_basis.json"
            malformed.write_text("{not json", encoding="utf-8")
            request["selected_source_body_basis_path"] = str(malformed)
            result = self.resolve(request)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "SELECTED_SOURCE_BODY_BASIS_MALFORMED")

            array = tmp_path / "array_basis.json"
            array.write_text(json.dumps(["not", "an", "object"]), encoding="utf-8")
            request["selected_source_body_basis_path"] = str(array)
            result = self.resolve(request)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(block_code(result), "SELECTED_SOURCE_BODY_BASIS_MALFORMED")

    def test_blocking_missing_required_basis(self) -> None:
        cases = [
            (
                "selected source-body basis",
                lambda request: (
                    request.pop("selected_source_body_basis", None),
                    request.pop("selected_source_body_basis_path", None),
                ),
                "SELECTED_SOURCE_BODY_BASIS_MISSING",
            ),
            (
                "selected closure basis",
                lambda request: request.pop("selected_closure_basis", None),
                "SELECTED_SOURCE_BODY_CLOSURE_BASIS_MISSING",
            ),
            (
                "terminal summary",
                lambda request: (
                    request.pop("selected_terminal_summary_basis", None),
                    request.pop("selected_reception_terminal_summary_path", None),
                ),
                "SOURCE_BODY_RECEPTION_TERMINAL_SUMMARY_MISSING",
            ),
            (
                "reception closure basis",
                lambda request: (
                    request.pop("selected_reception_closure_basis", None),
                    request.pop("selected_reception_closure_artifact_path", None),
                ),
                "SOURCE_BODY_RECEPTION_CLOSURE_BASIS_MISSING",
            ),
            (
                "distributed required",
                lambda request: (
                    request.update({"distributed_operation_basis_required": True}),
                    request.pop("selected_distributed_operation_terminal_summary", None),
                    request.pop("selected_distributed_operation_closure_basis", None),
                ),
                "DISTRIBUTED_OPERATION_CLOSURE_BASIS_MISSING",
            ),
            (
                "current required",
                lambda request: (
                    request.update({"current_body_basis_required": True}),
                    request.pop("selected_current_body_basis", None),
                    request.pop("selected_current_body_conformance_basis", None),
                    request.pop("selected_current_self_orientation_basis", None),
                ),
                "CURRENT_BODY_BASIS_MISSING",
            ),
            (
                "required source surfaces",
                lambda request: (
                    request.pop("required_source_surfaces", None),
                    request["required_surfaces"].pop("required_source_surfaces", None),
                ),
                "REQUIRED_SOURCE_SURFACES_MISSING",
            ),
            (
                "required spec surfaces",
                lambda request: (
                    request.pop("required_spec_surfaces", None),
                    request["required_surfaces"].pop("required_spec_surfaces", None),
                ),
                "REQUIRED_SPEC_SURFACES_MISSING",
            ),
            (
                "required resolver surfaces",
                lambda request: (
                    request.pop("required_resolver_surfaces", None),
                    request["required_surfaces"].pop("required_resolver_surfaces", None),
                ),
                "REQUIRED_RESOLVER_SURFACES_MISSING",
            ),
            (
                "required test surfaces",
                lambda request: (
                    request.pop("required_test_surfaces", None),
                    request["required_surfaces"].pop("required_test_surfaces", None),
                ),
                "REQUIRED_TEST_SURFACES_MISSING",
            ),
            (
                "required artifact roots",
                lambda request: (
                    request.pop("required_artifact_roots", None),
                    request["required_surfaces"].pop("required_artifact_roots", None),
                ),
                "REQUIRED_ARTIFACT_ROOTS_MISSING",
            ),
            (
                "required closure artifacts",
                lambda request: (
                    request.pop("required_closure_artifacts", None),
                    request["required_surfaces"].pop("required_closure_artifacts", None),
                ),
                "REQUIRED_CLOSURE_ARTIFACTS_MISSING",
            ),
            (
                "verifying carrier",
                lambda request: request.pop("verifying_carrier", None),
                "VERIFYING_CARRIER_MISSING",
            ),
            (
                "original carrier",
                lambda request: request.pop("original_carrier", None),
                "ORIGINAL_CARRIER_MISSING",
            ),
            (
                "carrier independence basis",
                lambda request: request.pop("carrier_independence_basis", None),
                "CARRIER_INDEPENDENCE_BASIS_MISSING",
            ),
            (
                "verification evidence basis",
                lambda request: request.pop("verification_evidence_basis", None),
                "VERIFICATION_EVIDENCE_BASIS_MISSING",
            ),
        ]
        for name, mutate, expected in cases:
            request = base_request()
            mutate(request)
            with self.subTest(name=name):
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), expected)

    def test_blocking_unsupported_scope_and_collapse_flags(self) -> None:
        request = base_request()
        request["verification_scope"] = ["UNSUPPORTED_SCOPE"]
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "UNSUPPORTED_PORTABLE_VERIFICATION_SCOPE")

        collapse_cases = [
            ("carrier_became_source", "VERIFICATION_TREATS_CARRIER_AS_SOURCE"),
            ("carrier_became_authority", "VERIFICATION_TREATS_CARRIER_AS_AUTHORITY"),
            ("device_became_authority", "VERIFICATION_TREATS_DEVICE_AS_AUTHORITY"),
            ("os_became_authority", "VERIFICATION_TREATS_OS_AS_AUTHORITY"),
            ("vendor_environment_became_authority", "VERIFICATION_TREATS_VENDOR_AS_AUTHORITY"),
            ("account_became_authority", "VERIFICATION_TREATS_ACCOUNT_AS_AUTHORITY"),
            ("local_path_created_currentness", "VERIFICATION_TREATS_LOCAL_PATH_AS_CURRENTNESS"),
            ("latest_file_created_currentness", "VERIFICATION_TREATS_LATEST_FILE_AS_CURRENTNESS"),
            ("recency_created_currentness", "VERIFICATION_TREATS_RECENCY_AS_CURRENTNESS"),
            ("repository_copy_became_body", "VERIFICATION_TREATS_REPOSITORY_COPY_AS_BODY"),
            ("repository_possession_created_currentness", "VERIFICATION_TREATS_REPOSITORY_POSSESSION_AS_CURRENTNESS"),
            ("artifact_existence_created_currentness", "VERIFICATION_TREATS_ARTIFACT_EXISTENCE_AS_CURRENTNESS"),
            ("carrier_possession_created_currentness", "VERIFICATION_TREATS_CARRIER_POSSESSION_AS_CURRENTNESS"),
            ("archive_possession_created_currentness", "VERIFICATION_TREATS_ARCHIVE_POSSESSION_AS_CURRENTNESS"),
            ("narration_created_currentness", "VERIFICATION_TREATS_NARRATION_AS_CURRENTNESS"),
            ("source_replaced", "VERIFICATION_REPLACES_SOURCE"),
            ("source_transferred", "VERIFICATION_TRANSFERS_SOURCE"),
            ("source_migrated", "VERIFICATION_MIGRATES_SOURCE"),
            ("reception_authorized", "VERIFICATION_AUTHORIZES_RECEPTION"),
            ("source_received", "VERIFICATION_RECEIVES_SOURCE"),
            ("source_receipt_recorded", "VERIFICATION_RECORDS_SOURCE_RECEIPT"),
            ("source_receipt_created", "VERIFICATION_CREATES_SOURCE_RECEIPT"),
            ("adoption_created", "VERIFICATION_CREATES_ADOPTION"),
            ("authority_created", "VERIFICATION_CREATES_AUTHORITY"),
            ("currentness_created", "VERIFICATION_CREATES_CURRENTNESS"),
            ("standing_created", "VERIFICATION_CREATES_STANDING"),
            ("operation_permission_created", "VERIFICATION_CREATES_OPERATION_PERMISSION"),
            ("public_launch_readiness_created", "VERIFICATION_CREATES_PUBLIC_READINESS"),
            ("final_completion_claimed", "VERIFICATION_CLAIMS_FINAL_COMPLETION"),
            ("continuation_authorized", "VERIFICATION_AUTHORIZES_CONTINUATION"),
            ("follow_on_work_authorized", "VERIFICATION_AUTHORIZES_FOLLOW_ON_WORK"),
            ("publication_flow_opened", "VERIFICATION_OPENS_PUBLICATION_FLOW"),
            ("reusable_permission_created", "VERIFICATION_CREATES_REUSABLE_PERMISSION"),
            ("another_reception_request_authorized", "VERIFICATION_AUTHORIZES_ANOTHER_RECEPTION_REQUEST"),
            ("derivative_reception_authorized", "VERIFICATION_AUTHORIZES_DERIVATIVE_RECEPTION"),
            ("vessel_relation_authorized", "VERIFICATION_AUTHORIZES_VESSEL_RELATION"),
            ("runtime_hosting_created", "VERIFICATION_CREATES_RUNTIME_HOSTING"),
            ("deployment_created", "VERIFICATION_CREATES_DEPLOYMENT"),
            ("public_release_created", "VERIFICATION_CREATES_PUBLIC_RELEASE"),
        ]
        for flag, expected in collapse_cases:
            request = base_request()
            request[flag] = True
            with self.subTest(flag=flag):
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), expected)

        request = base_request()
        request["selected_reception_closure_basis"]["reception_authorized"] = True
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "VERIFICATION_AUTHORIZES_RECEPTION")

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            request = base_request()
            request[flag] = True
            with self.subTest(flag=flag):
                result = self.resolve(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(block_code(result), "MUTATION_REPLAY_OR_MERGE_DETECTED")

        request = base_request()
        request["declared_non_claims"].pop("carrier_became_source")
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(block_code(result), "NON_CLAIM_MISSING_OR_FLIPPED")

        request = base_request()
        request["declared_non_claims"]["source_transferred"] = True
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            block_code(result),
            {"NON_CLAIM_MISSING_OR_FLIPPED", "VERIFICATION_TRANSFERS_SOURCE"},
        )

    def test_explicit_block_intent_and_bounded_outcome_family(self) -> None:
        results = []
        for outcome in (RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS):
            request = base_request()
            request["requested_verification_outcome"] = outcome
            results.append(self.resolve(request))

        request = base_request()
        request["portable_verification_intent"] = "BLOCK_PORTABLE_SOURCE_BODY_VERIFICATION_REVIEW"
        blocked = self.resolve(request)
        results.append(blocked)
        self.assertEqual(blocked["outcome"], BLOCKED)
        self.assertEqual(block_code(blocked), "PORTABLE_VERIFICATION_REVIEW_REQUEST_EXPLICITLY_BLOCKED")

        for result in results:
            self.assertIn(result["outcome"], OUTCOME_FAMILY)
            statement = result["verification_statement"]
            for key in ALLOWED_RECORDED_TRUE_FIELDS:
                self.assertEqual(statement[key], result["outcome"] == RECORDED, key)
            for key in REQUIRED_NON_CLAIMS:
                self.assertFalse(result["non_claims"][key], key)


if __name__ == "__main__":
    unittest.main()
