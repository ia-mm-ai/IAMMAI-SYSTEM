"""Bounded tests for the artifact emission containment resolver.

These tests prove only artifact emission containment. Containment records
future artifact-emission shape: selected prior results should be represented by
reference-shaped summaries instead of recursive full-artifact embedding.
Containment is not cleanup, deletion, compaction, rewrite, migration, command
implementation, command execution, manifest, checksum, signature, packet,
deployment, runtime hosting, public release, final completion, continuation,
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

import resolve_artifact_emission_containment_boundary as resolver  # noqa: E402


RECORDED = resolver.OUTCOME_RECORDED
NOT_RECORDED = resolver.OUTCOME_NOT_RECORDED
REQUIRES_ADDITIONAL_BASIS = resolver.OUTCOME_REQUIRES_ADDITIONAL_BASIS
BLOCKED = resolver.OUTCOME_BLOCKED
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, REQUIRES_ADDITIONAL_BASIS, BLOCKED}
SUPPORTED_SCOPE = tuple(sorted(resolver.SUPPORTED_CONTAINMENT_SCOPE))
REQUIRED_NON_CLAIMS = tuple(resolver.REQUIRED_FALSE_NON_CLAIMS)
OUTPUT_FALSE_POSTURE = tuple(resolver.OUTPUT_FALSE_POSTURE)
ALLOWED_REFERENCE_FIELDS = tuple(resolver.ALLOWED_REFERENCE_FIELDS)

TOP_LEVEL_SECTIONS = {
    "artifact_emission_containment_metadata",
    "declared_containment_question",
    "selected_artifact_emission_pressure_basis",
    "affected_artifact_families",
    "future_emission_family",
    "containment_basis",
    "reference_only_selected_basis_posture",
    "summary_plus_reference_posture",
    "recursive_embedding_block",
    "prior_artifact_preservation_posture",
    "containment_scope",
    "containment_checks",
    "containment_statement",
    "containment_non_meaning",
    "additional_basis_required",
    "not_recorded_basis",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "artifact_emission_containment_summary",
}

QUESTION = (
    "Can future artifacts be required to preserve selected prior results by "
    "reference-shaped summaries rather than recursively embedding full "
    "upstream artifacts, without mutating prior artifacts or authorizing "
    "command, manifest, deployment, runtime, public release, transfer, "
    "migration, source receipt, continuation, reusable permission, derivative "
    "reception, vessel relation, another reception request, or follow-on work?"
)


def required_false_non_claims() -> dict:
    return {name: False for name in REQUIRED_NON_CLAIMS}


def synthetic_large_prior_artifact() -> tuple[dict, str]:
    sentinel = "FULL_ARTIFACT_BODY_SENTINEL_" + ("x" * 120000)
    prior_artifact = {
        "selected_result_id": "portable_verification_large_prior_001",
        "selected_result_path": (
            "artifacts/integrity_host_v0_min_coexistence_portable_source_body_"
            "verification_boundary/portable_source_body_verification_reference_review_001__"
            "portable_source_body_verification_result.json"
        ),
        "selected_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
        "selected_result_failed_check_count": 0,
        "selected_result_passed_check_count": 44,
        "selected_result_summary": {
            "portable_source_body_verification_recorded": True,
            "carrier_independent_verification_recorded": True,
        },
        "selected_result_non_claims": {
            "source_transferred": False,
            "source_migrated": False,
            "source_received": False,
            "reception_authorized": False,
            "deployment_created": False,
            "runtime_hosting_created": False,
            "public_release_created": False,
            "follow_on_work_authorized": False,
        },
        "selected_result_basis_reference": "portable-verification:reference-review-001",
        "selected_result_artifact_family": "portable_source_body_verification",
        "selected_result_artifact_size_class": "synthetic-heavy",
        "full_artifact_body": sentinel,
    }
    return prior_artifact, sentinel


def reference_record_from_prior_artifact(prior_artifact: dict) -> dict:
    return {
        field: copy.deepcopy(prior_artifact[field])
        for field in ALLOWED_REFERENCE_FIELDS
        if field in prior_artifact
    }


def selected_artifact_emission_pressure_basis(large_reference: dict | None = None) -> dict:
    return {
        "artifact_emission_pressure_basis_declared": True,
        "selected_large_artifact_reference": large_reference
        or {
            "selected_result_id": "portable_verification_large_prior_001",
            "selected_result_path": "artifacts/portable-verification-result.json",
            "selected_result_outcome": "PORTABLE_SOURCE_BODY_VERIFICATION_RECORDED",
            "selected_result_failed_check_count": 0,
            "selected_result_passed_check_count": 44,
            "selected_result_summary": {"carrier_independent_verification_recorded": True},
            "selected_result_non_claims": {"follow_on_work_authorized": False},
            "selected_result_basis_reference": "portable-verification:reference-review-001",
            "selected_result_artifact_family": "portable_source_body_verification",
            "selected_result_artifact_size_class": "standing-heavy",
        },
        "selected_heavy_artifact_evidence_where_supplied": True,
        "selected_artifact_size_pressure_basis": {
            "artifact_size_pressure_basis_declared": True,
            "recursive_embedding_pressure_observed": True,
            "artifact_size_pressure_is_not_automatic_law_failure": True,
        },
        "selected_carrier_shape_pressure_basis": {
            "carrier_shape_pressure_basis_declared": True,
            "carrier_shape_pressure_is_not_currentness_or_authority": True,
        },
        "heavy_artifacts_remain_standing_evidence_if_checks_passed": True,
        "heavy_artifact_evidence_does_not_become_source": True,
        "artifact_size_pressure_is_not_automatic_law_failure": True,
        "carrier_shape_pressure_is_not_currentness_or_authority": True,
        "containment_should_occur_before_further_recursive_live_artifact_emission": True,
    }


def affected_artifact_families() -> dict:
    return {
        "portable_source_body_verification_family": {
            "artifact_family": "portable_source_body_verification",
            "status_descriptive_only": True,
        },
        "evidence_manifest_family": {
            "artifact_family": "portable_source_body_verification_evidence_manifest",
            "status_descriptive_only": True,
        },
        "source_body_reception_closure_family": {
            "artifact_family": "source_body_reception_closure",
            "status_descriptive_only": True,
        },
        "command_boundary_future_emission_family": {
            "artifact_family": "portable_source_body_verification_command_boundary",
            "future_only": True,
        },
        "affected_family_status_is_descriptive_only": True,
        "affected_family_status_does_not_invalidate_prior_artifacts": True,
    }


def future_emission_family() -> dict:
    return {
        "command_boundary_live_artifact_family": {
            "artifact_family": "portable_source_body_verification_command_boundary",
            "future_artifact_family_only": True,
        },
        "future_artifacts_should_use_reference_only_selected_basis": True,
        "future_artifacts_should_use_summary_plus_reference_emission": True,
        "future_artifacts_should_block_recursive_full_artifact_embedding": True,
        "future_emission_family_is_not_authorized_to_emit_until_separately_reviewed": True,
    }


def containment_basis() -> dict:
    return {
        "containment_basis_declared": True,
        "reference_only_selected_basis_posture": True,
        "summary_plus_reference_posture": True,
        "prohibited_recursive_embedding_posture": True,
        "prior_artifact_preservation_posture": True,
        "no_prior_artifact_mutation_posture": True,
        "no_artifact_invalidation_by_size_posture": True,
        "containment_basis_does_not_create_cleanup": True,
        "containment_basis_does_not_create_migration": True,
        "containment_basis_does_not_create_command_manifest_implementation": True,
        "containment_basis_does_not_authorize_next_work": True,
    }


def reference_only_selected_basis_posture() -> dict:
    return {
        "reference_only_selected_basis_posture_declared": True,
        "future_selected_results_represented_by_reference_records": True,
        "allowed_reference_fields": list(ALLOWED_REFERENCE_FIELDS),
        "reference_records_do_not_become_source": True,
        "reference_records_do_not_create_currentness": True,
        "paths_do_not_create_currentness": True,
        "size_class_is_descriptive_only_and_not_validity": True,
    }


def summary_plus_reference_posture() -> dict:
    return {
        "summary_plus_reference_posture_declared": True,
        "summaries_are_bounded_excerpts": True,
        "summary_digest_is_not_cryptographic_digest_unless_separately_specified": True,
        "selected_non_claim_excerpts_preserve_anti_collapse_posture": True,
        "summary_does_not_become_source": True,
        "summary_does_not_create_authority": True,
        "summary_does_not_create_currentness": True,
    }


def recursive_embedding_block() -> dict:
    return {
        "recursive_embedding_block_declared": True,
        "recursive_full_artifact_embedding_blocked": True,
        "raw_full_artifact_body_embedding_prohibited_unless_separately_permitted": True,
        "full_artifact_bodies_should_not_be_nested_inside_future_artifacts": True,
        "prior_artifacts_preserved_by_reference": True,
        "prohibited_embedding_does_not_mutate_prior_artifacts": True,
    }


def prior_artifact_preservation_posture() -> dict:
    return {
        "prior_artifact_preservation_posture_declared": True,
        "prior_artifacts_preserved_by_reference": True,
        "prior_artifacts_not_mutated": True,
        "prior_artifacts_not_deleted": True,
        "prior_artifacts_not_compacted": True,
        "prior_artifacts_not_rewritten": True,
        "prior_artifacts_not_repaired": True,
        "prior_artifacts_not_normalized": True,
        "prior_artifacts_not_migrated": True,
        "prior_artifacts_not_invalidated_by_size": True,
        "old_artifacts_not_replaced": True,
    }


def no_prior_artifact_mutation_posture() -> dict:
    return {
        "no_prior_artifact_mutation_posture_declared": True,
        "prior_artifacts_not_mutated": True,
        "prior_artifacts_not_deleted": True,
        "prior_artifacts_not_compacted": True,
        "prior_artifacts_not_rewritten": True,
    }


def no_artifact_invalidation_by_size_posture() -> dict:
    return {
        "no_artifact_invalidation_by_size_posture_declared": True,
        "prior_artifacts_not_invalidated_by_size": True,
        "artifact_size_pressure_is_not_law_failure_by_itself": True,
    }


def declared_request(
    *,
    outcome: str = RECORDED,
    selected_large_artifact_evidence: dict | str | None = None,
) -> dict:
    large_reference = (
        selected_large_artifact_evidence
        if isinstance(selected_large_artifact_evidence, dict)
        else None
    )
    return {
        "containment_request_id": "artifact_emission_containment_reference_review_001",
        "containment_question": QUESTION,
        "containment_intent": "RECORD_ARTIFACT_EMISSION_CONTAINMENT",
        "selected_artifact_emission_pressure_basis": selected_artifact_emission_pressure_basis(
            large_reference
        ),
        "selected_large_artifact_evidence": selected_large_artifact_evidence
        or selected_artifact_emission_pressure_basis()["selected_large_artifact_reference"],
        "selected_heavy_artifact_evidence": {
            "selected_result_artifact_family": "portable_source_body_verification_evidence_manifest",
            "selected_result_artifact_size_class": "standing-heavy",
            "heavy_artifacts_remain_standing_evidence_if_checks_passed": True,
        },
        "selected_artifact_size_pressure_basis": {
            "artifact_size_pressure_basis_declared": True,
            "recursive_full_artifact_embedding_pressure": True,
            "artifact_size_pressure_is_not_automatic_law_failure": True,
        },
        "selected_carrier_shape_pressure_basis": {
            "carrier_shape_pressure_basis_declared": True,
            "carrier_shape_pressure_is_not_currentness_or_authority": True,
        },
        "affected_artifact_families": affected_artifact_families(),
        "future_emission_family": future_emission_family(),
        "containment_basis": containment_basis(),
        "reference_only_selected_basis_posture": reference_only_selected_basis_posture(),
        "summary_plus_reference_posture": summary_plus_reference_posture(),
        "recursive_embedding_block": recursive_embedding_block(),
        "prior_artifact_preservation_posture": prior_artifact_preservation_posture(),
        "no_prior_artifact_mutation_posture": no_prior_artifact_mutation_posture(),
        "no_artifact_invalidation_by_size_posture": no_artifact_invalidation_by_size_posture(),
        "containment_scope": list(SUPPORTED_SCOPE),
        "reference_record_shape": list(ALLOWED_REFERENCE_FIELDS),
        "selected_prior_result_reference_shape": {
            "allowed_reference_fields": list(ALLOWED_REFERENCE_FIELDS),
            "reference_record_became_source": False,
            "path_created_currentness": False,
        },
        "requested_containment_outcome": outcome,
        "declared_non_claims": required_false_non_claims(),
    }


class ArtifactEmissionContainmentBoundaryTests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_no_forbidden_posture(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for field in REQUIRED_NON_CLAIMS:
            self.assertIs(non_claims[field], False, field)
        for field in OUTPUT_FALSE_POSTURE:
            self.assertIs(non_claims[field], False, field)

    def recorded_result(self) -> dict:
        return resolver.resolve_artifact_emission_containment_boundary(
            declared_containment_request=declared_request()
        )

    def test_successful_containment_recorded_result(self) -> None:
        result = self.recorded_result()

        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["code"])
        self.assertIsNone(result["block"]["reason"])
        self.assertEqual(result["artifact_emission_containment_summary"]["failed_check_count"], 0)

        statement = result["containment_statement"]
        self.assertIs(statement["artifact_emission_containment_recorded"], True)
        self.assertIs(statement["reference_only_selected_basis_required"], True)
        self.assertIs(statement["recursive_full_artifact_embedding_blocked"], True)
        self.assertIs(statement["summary_plus_reference_emission_required"], True)
        self.assertIs(statement["prior_artifacts_preserved_by_reference"], True)
        self.assertIs(statement["artifact_emission_containment_only"], True)
        self.assertIs(statement["future_artifacts_should_use_reference_records"], True)
        self.assertIs(statement["future_artifacts_should_not_embed_full_prior_artifacts"], True)
        self.assertIs(statement["heavy_artifacts_remain_visible_evidence"], True)
        self.assertIs(statement["artifact_size_pressure_is_not_law_failure_by_itself"], True)
        self.assertIs(statement["carrier_shape_pressure_recorded"], True)
        self.assert_no_forbidden_posture(result)

    def test_metadata_preserved(self) -> None:
        metadata = self.recorded_result()["artifact_emission_containment_metadata"]

        for key in (
            "artifact_emission_containment_result_id",
            "artifact_emission_containment_result_type",
            "artifact_emission_containment_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["artifact_emission_containment_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_artifact_emission_containment_boundary")

    def test_reference_only_selected_basis_avoids_recursive_full_body_embedding(self) -> None:
        prior_artifact, sentinel = synthetic_large_prior_artifact()
        reference_record = reference_record_from_prior_artifact(prior_artifact)
        request = declared_request(selected_large_artifact_evidence=reference_record)

        result = resolver.resolve_artifact_emission_containment_boundary(
            declared_containment_request=request
        )
        serialized = json.dumps(result, sort_keys=True)
        selected_large = result["selected_artifact_emission_pressure_basis"][
            "selected_large_artifact_evidence"
        ]

        self.assertEqual(result["outcome"], RECORDED)
        self.assertNotIn(sentinel, serialized)
        self.assertNotIn('"full_artifact_body":', serialized)
        self.assertLess(len(serialized), len(sentinel))
        self.assertEqual(
            selected_large["selected_result_id"],
            prior_artifact["selected_result_id"],
        )
        self.assertEqual(
            selected_large["selected_result_outcome"],
            prior_artifact["selected_result_outcome"],
        )
        self.assertEqual(selected_large["selected_result_failed_check_count"], 0)
        self.assertEqual(selected_large["selected_result_passed_check_count"], 44)
        self.assertEqual(
            selected_large["selected_result_summary"],
            prior_artifact["selected_result_summary"],
        )
        self.assertEqual(
            selected_large["selected_result_non_claims"],
            prior_artifact["selected_result_non_claims"],
        )
        self.assertIs(
            result["recursive_embedding_block"]["recursive_full_artifact_embedding_blocked"],
            True,
        )
        self.assertIs(
            result["containment_statement"]["summary_plus_reference_emission_required"],
            True,
        )

    def test_containment_checks_are_explicit_and_pass_for_recorded_case(self) -> None:
        result = self.recorded_result()
        checks = result["containment_checks"]
        check_names = {check["check_name"] for check in checks}

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIn("failure_code", check)
            self.assertIs(check["passed"], True, check["check_name"])

        self.assertEqual(result["artifact_emission_containment_summary"]["failed_check_count"], 0)
        expected_checks = {
            "containment question declared",
            "containment intent supported",
            "artifact-emission pressure basis declared",
            "affected artifact family declared",
            "future emission family declared",
            "containment basis declared",
            "reference-only selected-basis posture declared",
            "summary-plus-reference posture declared",
            "recursive full-artifact embedding blocked",
            "prior artifacts preserved by reference",
            "prior artifacts not mutated",
            "prior artifacts not deleted",
            "prior artifacts not compacted",
            "prior artifacts not invalidated by size",
            "containment scope supported",
            "containment is not cleanup",
            "containment is not migration",
            "containment is not command",
            "containment is not manifest/checksum/signature/packet implementation",
            "containment does not create currentness",
            "containment does not authorize next work",
            "reference record not source",
            "summary not source",
            "path not currentness",
            "artifact existence not currentness",
            "no command implementation/execution/authorization",
            "no manifest/checksum/signature/packet implementation",
            "no deployment/runtime/public release",
            "no source transfer/migration/receipt/reception authorization",
            "no final completion/continuation/reusable permission/follow-on work",
            "no mutation/replay/merge",
            "non-claims remain false",
        }
        self.assertTrue(expected_checks.issubset(check_names))

    def test_containment_non_meaning_preserved(self) -> None:
        non_meaning = self.recorded_result()["containment_non_meaning"]
        expected_true_keys = {
            "containment_does_not_mean_existing_artifacts_invalid",
            "containment_does_not_mean_existing_artifacts_deleted",
            "containment_does_not_mean_existing_artifacts_compacted",
            "containment_does_not_mean_existing_artifacts_rewritten",
            "containment_does_not_mean_existing_artifacts_repaired",
            "containment_does_not_mean_existing_artifacts_normalized",
            "containment_does_not_mean_existing_artifacts_migrated",
            "containment_does_not_mean_old_artifacts_replaced",
            "containment_does_not_mean_smaller_artifacts_create_currentness",
            "containment_does_not_mean_reference_record_became_source",
            "containment_does_not_mean_summary_became_source",
            "containment_does_not_mean_path_created_currentness",
            "containment_does_not_mean_artifact_existence_created_currentness",
            "containment_does_not_mean_command_exists",
            "containment_does_not_mean_manifest_exists",
            "containment_does_not_mean_checksum_exists",
            "containment_does_not_mean_signature_exists",
            "containment_does_not_mean_packet_exists",
            "containment_does_not_mean_deployment_authorized",
            "containment_does_not_mean_runtime_hosting_authorized",
            "containment_does_not_mean_public_release_authorized",
            "containment_does_not_mean_final_completion_claimed",
            "containment_does_not_mean_follow_on_work_authorized",
        }
        for key in expected_true_keys:
            self.assertIs(non_meaning[key], True, key)

    def test_additional_basis_and_not_recorded_outcomes_do_not_authorize_work(self) -> None:
        additional_request = declared_request(outcome=REQUIRES_ADDITIONAL_BASIS)
        additional_request["additional_basis_context"] = {
            "missing_basis": "reference-only selected-basis posture needs review"
        }
        additional_result = resolver.resolve_artifact_emission_containment_boundary(
            declared_containment_request=additional_request
        )

        self.assertEqual(additional_result["outcome"], REQUIRES_ADDITIONAL_BASIS)
        self.assertEqual(
            additional_result["additional_basis_required"]["additional_basis_context"],
            additional_request["additional_basis_context"],
        )
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_scheduled"], False)
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_authorized"], False)
        self.assertIs(additional_result["additional_basis_required"]["missing_basis_executed"], False)
        self.assert_no_forbidden_posture(additional_result)

        not_recorded_request = declared_request(outcome=NOT_RECORDED)
        not_recorded_request["not_recorded_basis"] = {
            "not_recorded_reason": "containment basis cannot be bounded"
        }
        not_recorded_result = resolver.resolve_artifact_emission_containment_boundary(
            declared_containment_request=not_recorded_request
        )

        self.assertEqual(not_recorded_result["outcome"], NOT_RECORDED)
        self.assertEqual(
            not_recorded_result["not_recorded_basis"]["not_recorded_basis"],
            not_recorded_request["not_recorded_basis"],
        )
        self.assertIs(not_recorded_result["not_recorded_basis"]["not_recorded_authorizes_cleanup"], False)
        self.assertIs(not_recorded_result["not_recorded_basis"]["not_recorded_repairs_prior_artifacts"], False)
        self.assertIs(not_recorded_result["not_recorded_basis"]["not_recorded_authorizes_follow_on_work"], False)
        self.assert_no_forbidden_posture(not_recorded_result)

    def test_what_remains_open_is_not_scheduled_authorized_or_executed(self) -> None:
        remains_open = self.recorded_result()["what_remains_open"]
        expected_items = {
            "artifact emission containment test",
            "artifact emission containment live artifact",
            "command-boundary live artifact rerun using contained reference shape",
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
        }
        self.assertTrue(expected_items.issubset(set(remains_open["open_items"])))
        self.assertIs(remains_open["open_means_not_scheduled"], True)
        self.assertIs(remains_open["open_means_not_authorized"], True)
        self.assertIs(remains_open["open_means_not_executed"], True)

    def test_summary_helper_preserves_bounded_readback(self) -> None:
        result = self.recorded_result()
        summary = resolver.build_artifact_emission_containment_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["containment_request_id"],
            "artifact_emission_containment_reference_review_001",
        )
        self.assertEqual(summary["containment_question"], QUESTION)
        self.assertEqual(summary["containment_intent"], "RECORD_ARTIFACT_EMISSION_CONTAINMENT")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertIs(summary["artifact_emission_containment_recorded"], True)
        self.assertIs(summary["reference_only_selected_basis_required"], True)
        self.assertIs(summary["recursive_full_artifact_embedding_blocked"], True)
        self.assertIs(summary["summary_plus_reference_emission_required"], True)
        self.assertIs(summary["prior_artifacts_preserved_by_reference"], True)
        self.assertIs(summary["not_recorded"], False)
        self.assertIs(summary["requires_additional_basis"], False)
        self.assertTrue(summary["affected_artifact_families"])
        self.assertTrue(summary["future_emission_family"])
        self.assertIs(summary["containment_basis_declared"], True)
        self.assertIs(summary["reference_only_posture_declared"], True)
        self.assertIs(summary["summary_plus_reference_posture_declared"], True)
        self.assertIs(summary["recursive_embedding_blocked"], True)
        self.assertIs(summary["prior_artifacts_not_mutated"], True)
        self.assertIs(summary["prior_artifacts_not_deleted"], True)
        self.assertIs(summary["prior_artifacts_not_compacted"], True)
        self.assertIs(summary["prior_artifacts_not_rewritten"], True)
        self.assertIs(summary["prior_artifacts_not_invalidated_by_size"], True)
        self.assertIs(summary["artifact_size_pressure_not_law_failure_by_itself"], True)
        self.assertIs(summary["heavy_artifacts_remain_visible_evidence"], True)
        self.assertIs(summary["no_cleanup_compaction_deletion_rewrite_migration_authorized"], True)
        self.assertIs(summary["no_command_manifest_checksum_signature_packet_implemented"], True)
        self.assertIs(summary["no_deployment_runtime_public_release"], True)
        self.assertIs(summary["no_source_transferred_migrated_received_receipted"], True)
        self.assertIs(summary["no_operation_permission_public_readiness_final_completion"], True)
        self.assertIs(summary["no_continuation_publication_flow_reusable_permission"], True)
        self.assertIs(
            summary["no_derivative_reception_vessel_relation_another_reception_request_follow_on_work"],
            True,
        )
        self.assertTrue(summary["key_non_claims"])
        for value in summary["key_non_claims"].values():
            self.assertIs(value, False)

    def test_request_builder_helper_builds_valid_bounded_request(self) -> None:
        additional_context = {"missing_basis": "size-pressure relation needs review"}
        not_recorded_basis = {"not_recorded_reason": "basis not bounded"}
        request = resolver.build_declared_artifact_emission_containment_request(
            "builder_containment_001",
            QUESTION,
            selected_artifact_emission_pressure_basis(),
            affected_artifact_families(),
            future_emission_family(),
            containment_basis(),
            reference_only_selected_basis_posture(),
            summary_plus_reference_posture(),
            recursive_embedding_block(),
            prior_artifact_preservation_posture(),
            list(SUPPORTED_SCOPE),
            requested_containment_outcome=RECORDED,
            additional_basis_context=additional_context,
            not_recorded_basis=not_recorded_basis,
        )

        self.assertEqual(request["containment_request_id"], "builder_containment_001")
        self.assertEqual(request["containment_question"], QUESTION)
        self.assertTrue(request["selected_artifact_emission_pressure_basis"])
        self.assertTrue(request["affected_artifact_families"])
        self.assertTrue(request["future_emission_family"])
        self.assertTrue(request["containment_basis"])
        self.assertTrue(request["reference_only_selected_basis_posture"])
        self.assertTrue(request["summary_plus_reference_posture"])
        self.assertTrue(request["recursive_embedding_block"])
        self.assertTrue(request["prior_artifact_preservation_posture"])
        self.assertEqual(request["containment_scope"], list(SUPPORTED_SCOPE))
        self.assertEqual(request["requested_containment_outcome"], RECORDED)
        self.assertEqual(request["additional_basis_context"], additional_context)
        self.assertEqual(request["not_recorded_basis"], not_recorded_basis)
        for field in REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][field], False, field)

        forbidden = (
            "prior_artifacts_mutated",
            "prior_artifacts_deleted",
            "prior_artifacts_compacted",
            "prior_artifacts_rewritten",
            "prior_artifacts_invalidated_by_size",
            "command_implemented",
            "command_executed",
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
            "containment_created_currentness",
            "final_completion_claimed",
            "continuation_authorized",
            "reusable_permission_created",
            "derivative_reception_authorized",
            "vessel_relation_authorized",
            "another_reception_request_authorized",
            "follow_on_work_authorized",
        )
        for field in forbidden:
            self.assertFalse(request["declared_non_claims"][field], field)

        result = resolver.resolve_artifact_emission_containment_boundary(request)
        self.assertEqual(result["outcome"], RECORDED)
        self.assertEqual(result["artifact_emission_containment_summary"]["failed_check_count"], 0)

    def test_path_based_request_and_write_behavior(self) -> None:
        request = declared_request()
        mapping_result = resolver.resolve_artifact_emission_containment_boundary(request)

        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            request_path = tmp_path / "requests" / "containment_request.json"
            request_path.parent.mkdir(parents=True)
            request_path.write_text(json.dumps(request, indent=2), encoding="utf-8")

            path_result = resolver.resolve_artifact_emission_containment_boundary_from_path(request_path)
            self.assertEqual(path_result["outcome"], RECORDED)
            self.assertEqual(set(path_result.keys()), set(mapping_result.keys()))
            self.assertEqual(
                path_result["declared_containment_question"]["declared_containment_request_path"],
                str(request_path),
            )

            output_path = tmp_path / "nested" / "containment_result.json"
            written = resolver.write_artifact_emission_containment_result(path_result, output_path)
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed.keys()))

            original_root = str(resolver.ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_ROOT)
            self.assertIn("artifact_emission_containment_boundary", original_root)
            self.assertNotIn("portable_source_body_verification_command_boundary", original_root)
            self.assertNotIn("portable_source_body_verification_evidence_manifest_boundary", original_root)
            self.assertNotIn("portable_source_body_verification_boundary", original_root)
            self.assertNotIn("cleanup", original_root)
            self.assertNotIn("compaction", original_root)
            self.assertNotIn("migration", original_root)

            patched_root = tmp_path / "containment-default-root"
            with patch.object(resolver, "ARTIFACT_EMISSION_CONTAINMENT_BOUNDARY_ROOT", patched_root):
                first = resolver.write_artifact_emission_containment_result(path_result)
                second = resolver.write_artifact_emission_containment_result(path_result)
            self.assertEqual(first.parent, patched_root)
            self.assertEqual(second.parent, patched_root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        request = declared_request()
        selected_pressure = request["selected_artifact_emission_pressure_basis"]
        affected = request["affected_artifact_families"]
        future = request["future_emission_family"]
        basis = request["containment_basis"]
        reference_posture = request["reference_only_selected_basis_posture"]
        summary_posture = request["summary_plus_reference_posture"]
        embedding_block = request["recursive_embedding_block"]
        preservation = request["prior_artifact_preservation_posture"]
        scope = request["containment_scope"]

        snapshots = [
            (request, copy.deepcopy(request)),
            (selected_pressure, copy.deepcopy(selected_pressure)),
            (affected, copy.deepcopy(affected)),
            (future, copy.deepcopy(future)),
            (basis, copy.deepcopy(basis)),
            (reference_posture, copy.deepcopy(reference_posture)),
            (summary_posture, copy.deepcopy(summary_posture)),
            (embedding_block, copy.deepcopy(embedding_block)),
            (preservation, copy.deepcopy(preservation)),
            (scope, copy.deepcopy(scope)),
        ]

        first = resolver.resolve_artifact_emission_containment_boundary(request)
        second = resolver.resolve_artifact_emission_containment_boundary(request)

        self.assertEqual(first["outcome"], RECORDED)
        self.assertEqual(second["outcome"], RECORDED)
        for current, snapshot in snapshots:
            self.assertEqual(current, snapshot)

        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "additive" / "containment.json"
            written = resolver.write_artifact_emission_containment_result(first, output)
            self.assertTrue(written.exists())
            self.assertTrue(str(written).startswith(tmp))

    def test_blocking_missing_malformed_and_unsupported_inputs(self) -> None:
        valid = declared_request()

        block_request = copy.deepcopy(valid)
        block_request["containment_intent"] = "BLOCK_ARTIFACT_EMISSION_CONTAINMENT_REVIEW"
        result = resolver.resolve_artifact_emission_containment_boundary(block_request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], "CONTAINMENT_REVIEW_REQUEST_EXPLICITLY_BLOCKED")

        missing = resolver.resolve_artifact_emission_containment_boundary()
        self.assertEqual(missing["outcome"], BLOCKED)
        self.assertEqual(missing["block"]["code"], "CONTAINMENT_QUESTION_UNDECLARED")

        malformed = resolver.resolve_artifact_emission_containment_boundary(["not", "mapping"])
        self.assertEqual(malformed["outcome"], BLOCKED)
        self.assertEqual(malformed["block"]["code"], "DECLARED_CONTAINMENT_REQUEST_MALFORMED")

        missing_cases = (
            ("selected_artifact_emission_pressure_basis", "ARTIFACT_EMISSION_PRESSURE_BASIS_MISSING"),
            ("affected_artifact_families", "AFFECTED_ARTIFACT_FAMILY_MISSING"),
            ("future_emission_family", "FUTURE_EMISSION_FAMILY_MISSING"),
            ("containment_basis", "CONTAINMENT_BASIS_MISSING"),
            ("reference_only_selected_basis_posture", "REFERENCE_ONLY_SELECTED_BASIS_POSTURE_MISSING"),
            ("summary_plus_reference_posture", "SUMMARY_PLUS_REFERENCE_POSTURE_MISSING"),
            ("recursive_embedding_block", "RECURSIVE_EMBEDDING_BLOCK_MISSING"),
            ("prior_artifact_preservation_posture", "PRIOR_ARTIFACT_PRESERVATION_POSTURE_MISSING"),
        )
        for field, code in missing_cases:
            with self.subTest(field=field):
                request = copy.deepcopy(valid)
                request.pop(field)
                result = resolver.resolve_artifact_emission_containment_boundary(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["code"], code)

        no_mutation = copy.deepcopy(valid)
        no_mutation.pop("no_prior_artifact_mutation_posture")
        no_mutation["prior_artifact_preservation_posture"] = {
            "prior_artifact_preservation_posture_declared": True,
            "prior_artifacts_preserved_by_reference": True,
        }
        result = resolver.resolve_artifact_emission_containment_boundary(no_mutation)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], "NO_MUTATION_POSTURE_MISSING")

        unsupported_scope = copy.deepcopy(valid)
        unsupported_scope["containment_scope"] = ["UNSUPPORTED_CONTAINMENT_SCOPE_VALUE"]
        result = resolver.resolve_artifact_emission_containment_boundary(unsupported_scope)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], "UNSUPPORTED_CONTAINMENT_SCOPE")

    def test_blocking_unreadable_and_malformed_request_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_path = tmp_path / "missing.json"
            result = resolver.resolve_artifact_emission_containment_boundary_from_path(missing_path)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(result["block"]["code"], "DECLARED_CONTAINMENT_REQUEST_UNREADABLE")

            malformed_json = tmp_path / "malformed.json"
            malformed_json.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_artifact_emission_containment_boundary_from_path(malformed_json)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(result["block"]["code"], "DECLARED_CONTAINMENT_REQUEST_MALFORMED")

            array_json = tmp_path / "array.json"
            array_json.write_text(json.dumps(["not", "object"]), encoding="utf-8")
            result = resolver.resolve_artifact_emission_containment_boundary_from_path(array_json)
            self.assertEqual(result["outcome"], BLOCKED)
            self.assertEqual(result["block"]["code"], "DECLARED_CONTAINMENT_REQUEST_MALFORMED")

    def test_blocking_collapse_flags(self) -> None:
        cases = {
            "prior_artifacts_mutated": {"CONTAINMENT_MUTATES_PRIOR_ARTIFACTS"},
            "prior_artifacts_deleted": {"CONTAINMENT_DELETES_PRIOR_ARTIFACTS"},
            "prior_artifacts_compacted": {"CONTAINMENT_COMPACTS_PRIOR_ARTIFACTS"},
            "prior_artifacts_rewritten": {"CONTAINMENT_REWRITES_PRIOR_ARTIFACTS"},
            "prior_artifacts_invalidated_by_size": {"CONTAINMENT_INVALIDATES_PRIOR_ARTIFACTS_BY_SIZE"},
            "reference_record_became_source": {"REFERENCE_RECORD_TREATED_AS_SOURCE"},
            "summary_became_source": {"SUMMARY_TREATED_AS_SOURCE"},
            "path_created_currentness": {"PATH_TREATED_AS_CURRENTNESS"},
            "artifact_existence_created_currentness": {"ARTIFACT_EXISTENCE_TREATED_AS_CURRENTNESS"},
            "command_implemented": {"CONTAINMENT_AUTHORIZES_COMMAND_IMPLEMENTATION"},
            "command_executed": {"CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION"},
            "command_authorized_to_run": {"CONTAINMENT_AUTHORIZES_COMMAND_IMPLEMENTATION", "CONTAINMENT_AUTHORIZES_COMMAND_EXECUTION"},
            "manifest_implemented": {"CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION"},
            "checksum_implemented": {"CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION", "CONTAINMENT_CREATES_CHECKSUM_IMPLEMENTATION"},
            "signature_implemented": {"CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION", "CONTAINMENT_CREATES_SIGNATURE_IMPLEMENTATION"},
            "packet_implemented": {"CONTAINMENT_CREATES_MANIFEST_IMPLEMENTATION", "CONTAINMENT_CREATES_PACKET_IMPLEMENTATION"},
            "deployment_created": {"CONTAINMENT_CREATES_DEPLOYMENT"},
            "runtime_hosting_created": {"CONTAINMENT_CREATES_DEPLOYMENT", "CONTAINMENT_CREATES_RUNTIME_HOSTING"},
            "public_release_created": {"CONTAINMENT_CREATES_DEPLOYMENT", "CONTAINMENT_CREATES_PUBLIC_RELEASE"},
            "source_transferred": {"CONTAINMENT_AUTHORIZES_TRANSFER"},
            "source_migrated": {"CONTAINMENT_AUTHORIZES_TRANSFER", "CONTAINMENT_AUTHORIZES_MIGRATION"},
            "source_received": {"CONTAINMENT_AUTHORIZES_TRANSFER", "CONTAINMENT_AUTHORIZES_SOURCE_RECEIPT"},
            "source_receipt_recorded": {"CONTAINMENT_AUTHORIZES_TRANSFER", "CONTAINMENT_AUTHORIZES_SOURCE_RECEIPT"},
            "reception_authorized": {"CONTAINMENT_AUTHORIZES_TRANSFER", "CONTAINMENT_AUTHORIZES_RECEPTION"},
            "continuation_authorized": {"CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK", "CONTAINMENT_AUTHORIZES_CONTINUATION"},
            "reusable_permission_created": {"CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK", "CONTAINMENT_CREATES_REUSABLE_PERMISSION"},
            "follow_on_work_authorized": {"CONTAINMENT_AUTHORIZES_FOLLOW_ON_WORK"},
        }
        for field, expected_codes in cases.items():
            with self.subTest(field=field):
                request = declared_request()
                request[field] = True
                result = resolver.resolve_artifact_emission_containment_boundary(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertIn(result["block"]["code"], expected_codes)

    def test_blocking_mutation_replay_merge_and_non_claims(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = declared_request()
                request[field] = True
                result = resolver.resolve_artifact_emission_containment_boundary(request)
                self.assertEqual(result["outcome"], BLOCKED)
                self.assertEqual(result["block"]["code"], "MUTATION_REPLAY_OR_MERGE_DETECTED")

        missing_non_claim = declared_request()
        missing_non_claim["declared_non_claims"].pop("summary_became_source")
        result = resolver.resolve_artifact_emission_containment_boundary(missing_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["code"], "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped_non_claim = declared_request()
        flipped_non_claim["declared_non_claims"]["summary_became_source"] = True
        result = resolver.resolve_artifact_emission_containment_boundary(flipped_non_claim)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(result["block"]["code"], {"NON_CLAIM_MISSING_OR_FLIPPED", "SUMMARY_TREATED_AS_SOURCE"})


if __name__ == "__main__":
    unittest.main()
