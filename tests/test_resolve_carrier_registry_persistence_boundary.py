"""Tests for bounded carrier registry/persistence preservation.

This suite audits one registry/persistence boundary resolver. It verifies that
registry/persistence records reference preservation posture only. It does not
implement registry storage, persistence, currentness, authority, distributed
standing, repository synchronization, full body transfer, continuation,
distributed operation, or evidence erasure.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_carrier_registry_persistence_boundary as registry  # noqa: E402


TOP_LEVEL_SECTIONS = {
    "carrier_registry_persistence_metadata",
    "declared_registry_question",
    "persistence_purpose",
    "selected_record_category",
    "selected_carrier",
    "selected_referenced_artifacts",
    "registry_persistence_basis",
    "persistence_preservation_rules",
    "registry_non_authority_rules",
    "registry_persistence_checks",
    "registry_persistence_statement",
    "registry_persistence_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "carrier_registry_persistence_summary",
}

OUTCOME_FAMILY = {
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED",
    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED",
}

SUPPORTED_CATEGORIES = [
    "CARRIER_IDENTITY_RECORD",
    "CARRIER_LIFECYCLE_STATUS_RECORD",
    "CARRIER_EVIDENCE_REFERENCE_RECORD",
    "CARRIER_RELATION_REFERENCE_RECORD",
    "CARRIER_DIVERGENCE_REFERENCE_RECORD",
    "CARRIER_CURRENTNESS_PARTICIPATION_REFERENCE_RECORD",
    "CARRIER_EXPERIMENT_REFERENCE_RECORD",
    "CARRIER_INTEGRITY_REFERENCE_RECORD",
    "CARRIER_REGISTRY_NON_CLAIM_RECORD",
    "CARRIER_REGISTRY_BLOCK_RECORD",
]

EXPECTED_CHECK_NAMES = {
    "declared_registry_request_parseable_mapping",
    "registry_question_declared",
    "persistence_purpose_declared",
    "registry_intent_supported",
    "record_category_supported",
    "selected_carrier_identity_present_where_required",
    "referenced_artifacts_present_where_required",
    "referenced_artifact_parseable_where_supplied",
    "referenced_artifact_identity_present_where_required",
    "referenced_artifact_outcome_present_where_required",
    "lifecycle_reference_preserved_where_supplied",
    "relation_reference_preserved_where_supplied",
    "divergence_reference_preserved_where_supplied",
    "currentness_participation_reference_preserved_where_supplied",
    "admission_reference_preserved_where_supplied",
    "receipt_reference_preserved_where_supplied",
    "experiment_reference_preserved_where_supplied",
    "evidence_reference_preserved_where_supplied",
    "persistence_preservation_rules_preserved",
    "registry_non_authority_rules_preserved",
    "registry_does_not_decide_source",
    "registry_does_not_decide_currentness",
    "registry_does_not_create_authority",
    "registry_does_not_create_permission",
    "registry_does_not_create_carrier_hierarchy",
    "registry_does_not_select_current_carrier",
    "registry_does_not_select_winning_carrier",
    "registry_does_not_invalidate_losing_carrier",
    "registry_does_not_resolve_divergence",
    "registry_does_not_erase_evidence",
    "registry_does_not_hide_refusal",
    "registry_does_not_hide_divergence",
    "registry_does_not_hide_corruption",
    "registry_does_not_repair_by_overwrite",
    "registry_does_not_create_distributed_standing",
    "registry_does_not_authorize_repository_sync",
    "registry_does_not_authorize_full_body_transfer",
    "registry_does_not_create_second_body",
    "registry_does_not_authorize_continuation",
    "registry_does_not_authorize_distributed_operation",
    "no_latest_record_currentness",
    "no_latest_file_currentness",
    "no_mutation_replay_merge",
    "non_claims_remain_false",
}

NON_MEANING_KEYS = {
    "does_not_mean_source",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_standing",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_current_carrier_selected",
    "does_not_mean_winning_carrier_selected",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_divergence_resolved",
    "does_not_mean_evidence_erased",
    "does_not_mean_repair_by_overwrite",
    "does_not_mean_distributed_standing",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_distributed_operation",
    "does_not_mean_continuation",
    "does_not_mean_future_experiments_authorized",
    "does_not_mean_latest_record_currentness",
    "does_not_mean_completeness_authority",
    "does_not_mean_availability_priority",
    "does_not_mean_majority_currentness",
    "does_not_mean_registry_presence_as_standing",
    "does_not_mean_registry_absence_as_invalidation",
}

OPEN_KEYS = {
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_law",
    "cross_carrier_currentness_successor_law",
    "divergence_consequence_law",
    "distributed_standing_boundary",
    "distributed_standing",
    "presence_law",
    "threshold_law",
    "truth_law",
    "action_consequence_law",
    "generalized_vessel_relation_lifecycle",
    "body_relevance_medium",
    "signal_series_or_accumulation_logic",
    "successor_carrier_law",
    "future_self_orientation_successor_only_if_separately_justified",
    "distributed_operation_only_if_separately_declared_and_bounded",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}

REQUEST_ID = "carrier_registry_persistence_request_001"
CARRIER_ID = "carrier_C_additional_physical_candidate"
LIFECYCLE_ARTIFACT_ID = "carrier_C_lifecycle_status_recorded_result_001"


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert isinstance(loaded, dict)
    return loaded


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(registry.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _selected_carrier(**updates: object) -> dict[str, object]:
    carrier = {
        "carrier_id": CARRIER_ID,
        "carrier_label": "Carrier C",
        "carrier_identity_basis": "bounded lifecycle subject only",
        "registry_record_is_not_authority": True,
    }
    carrier.update(updates)
    return carrier


def _referenced_artifact(**updates: object) -> dict[str, object]:
    artifact = {
        "artifact_id": LIFECYCLE_ARTIFACT_ID,
        "outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
        "artifact_path": (
            "artifacts/integrity_host_v0_min_coexistence_carrier_lifecycle_boundary/"
            "carrier_C_lifecycle_status_recorded_result_001.json"
        ),
        "carrier_id": CARRIER_ID,
        "record_category": "CARRIER_LIFECYCLE_STATUS_RECORD",
        "listed_artifact_does_not_upgrade_artifact": True,
    }
    artifact.update(updates)
    return artifact


def _reference(
    artifact_id: str,
    outcome: str,
    **updates: object,
) -> dict[str, object]:
    reference = {
        "artifact_id": artifact_id,
        "outcome": outcome,
        "carrier_id": CARRIER_ID,
        "reference_preserved_as_reference_only": True,
    }
    reference.update(updates)
    return reference


def valid_request(
    *,
    category: str = "CARRIER_LIFECYCLE_STATUS_RECORD",
    intent: str = "RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
    selected_carrier: object | None = None,
    selected_referenced_artifacts: object | None = None,
    non_claims: dict[str, bool] | None = None,
    **updates: object,
) -> dict[str, object]:
    request: dict[str, object] = {
        "registry_request_id": REQUEST_ID,
        "registry_question": (
            "What may registry/persistence preserve about Carrier C lifecycle posture?"
        ),
        "persistence_purpose": (
            "Preserve bounded carrier lifecycle and evidence references without authority."
        ),
        "registry_intent": intent,
        "selected_record_category": category,
        "selected_carrier": _selected_carrier()
        if selected_carrier is None
        else selected_carrier,
        "selected_referenced_artifacts": [_referenced_artifact()]
        if selected_referenced_artifacts is None
        else selected_referenced_artifacts,
        "registry_persistence_basis": {
            "basis_id": "carrier_C_registry_persistence_basis_001",
            "basis": "Preserve Carrier C lifecycle status reference without registry authority.",
            "reference_preservation_only": True,
            "does_not_create_authority": True,
            "does_not_create_currentness": True,
            "does_not_create_distributed_standing": True,
        },
        "lifecycle_status_reference": _reference(
            "carrier_C_lifecycle_status_recorded_result_001",
            "CARRIER_LIFECYCLE_STATUS_RECORDED",
            lifecycle_status="CARRIER_REFUSED_OR_BLOCKED",
        ),
        "relation_reference": _reference(
            "carrier_B_C_divergence_bounded_relation_result_001",
            "MULTI_CARRIER_RELATION_RECOGNIZED",
            relation_type="DIVERGENCE_BOUNDED_RELATION",
        ),
        "divergence_reference": _reference(
            "carrier_B_C_visible_divergence_result_001",
            "CARRIER_DIVERGENCE_RECORDED",
            divergence_visible=True,
        ),
        "currentness_participation_reference": _reference(
            "carrier_C_currentness_participation_result_001",
            "CURRENTNESS_PARTICIPATION_ELIGIBLE",
            participation_only=True,
        ),
        "admission_reference": _reference(
            "carrier_C_returned_blocked_evidence_admission_result_001",
            "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
            evidence_only=True,
        ),
        "receipt_reference": _reference(
            "carrier_C_returned_blocked_receipt_evidence_001",
            "RECEIPT_BLOCK",
            refusal_visible=True,
        ),
        "experiment_reference": _reference(
            "additional_physical_carrier_experiment_declared_result_001",
            "ADDITIONAL_PHYSICAL_CARRIER_EXPERIMENT_DECLARED",
            declaration_only=True,
        ),
        "integrity_reference": _reference(
            "carrier_C_lifecycle_integrity_reference_001",
            "INTEGRITY_REFERENCE_PRESERVED",
            hash_basis_preserved=True,
        ),
        "persistence_preservation_rules": copy.deepcopy(
            registry.DEFAULT_PERSISTENCE_PRESERVATION_RULES
        ),
        "registry_non_authority_rules": copy.deepcopy(
            registry.DEFAULT_REGISTRY_NON_AUTHORITY_RULES
        ),
        "declared_non_claims": _non_claims() if non_claims is None else non_claims,
    }
    request.update(updates)
    return request


class CarrierRegistryPersistenceBoundaryTests(unittest.TestCase):
    def assert_bounded_shape(self, result: dict[str, object]) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_all_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in registry.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_block_code(self, request: object, expected_code: str) -> dict[str, object]:
        result = registry.resolve_carrier_registry_persistence_boundary(request)  # type: ignore[arg-type]
        self.assert_bounded_shape(result)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED",
            result["outcome"],
        )
        self.assertEqual(expected_code, result["block"]["block_code"])
        self.assert_all_non_claims_false(result)
        return result

    def test_successful_lifecycle_reference_record(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )

        self.assert_bounded_shape(result)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            result["outcome"],
        )
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            0,
            result["carrier_registry_persistence_summary"]["failed_check_count"],
        )

        statement = result["registry_persistence_statement"]
        self.assertIs(statement["carrier_registry_persistence_boundary_recorded"], True)
        self.assertIs(statement["selected_record_category_preserved"], True)
        self.assertIs(statement["selected_carrier_preserved"], True)
        self.assertIs(statement["referenced_artifact_identity_preserved"], True)
        self.assertIs(statement["referenced_artifact_outcome_preserved"], True)
        self.assertIs(statement["lifecycle_reference_preserved"], True)
        self.assertIs(statement["non_claims_preserved"], True)
        self.assertIs(statement["registry_created_source"], False)
        self.assertIs(statement["registry_created_currentness"], False)
        self.assertIs(statement["registry_created_authority"], False)
        self.assertIs(statement["registry_created_permission"], False)
        self.assertIs(statement["registry_created_carrier_hierarchy"], False)
        self.assertIs(statement["registry_created_distributed_standing"], False)
        self.assertIs(statement["registry_authorized_sync"], False)
        self.assertIs(statement["registry_authorized_full_body_transfer"], False)
        self.assertIs(statement["registry_created_second_body"], False)
        self.assertIs(statement["registry_authorized_continuation"], False)
        self.assertIs(statement["registry_authorized_distributed_operation"], False)
        self.assertIs(statement["registry_erased_evidence"], False)
        self.assertIs(statement["registry_hid_refusal"], False)
        self.assertIs(statement["registry_hid_divergence"], False)
        self.assertIs(statement["registry_hid_corruption"], False)
        self.assertIs(statement["registry_implemented_storage"], False)
        self.assertIs(statement["persistence_engine_implemented"], False)
        self.assertIs(statement["database_created"], False)

    def test_metadata(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        metadata = result["carrier_registry_persistence_metadata"]

        self.assertTrue(metadata["carrier_registry_persistence_result_id"])
        self.assertTrue(metadata["carrier_registry_persistence_result_type"])
        self.assertTrue(metadata["carrier_registry_persistence_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            "0.1.0",
            metadata["carrier_registry_persistence_result_version"],
        )
        self.assertEqual(
            "resolve_carrier_registry_persistence_boundary",
            metadata["resolver_module"],
        )

    def test_declared_registry_question(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        question = result["declared_registry_question"]

        self.assertEqual(REQUEST_ID, question["registry_request_id"])
        self.assertTrue(question["registry_question"])
        self.assertEqual(
            "RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
            question["registry_intent"],
        )
        self.assertIsInstance(question["declared_non_claims"], dict)
        self.assertIs(question["registry_is_not_authority"], True)
        self.assertIs(question["persistence_is_not_standing"], True)
        self.assertIs(question["indexing_is_not_currentness"], True)
        self.assertIs(question["record_presence_is_not_permission"], True)
        self.assertIs(question["registry_membership_is_not_distributed_standing"], True)
        self.assertIs(question["does_not_implement_registry_storage"], True)
        self.assertIs(
            question["does_not_authorize_sync_full_body_transfer_or_distributed_operation"],
            True,
        )

    def test_persistence_purpose(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        purpose = result["persistence_purpose"]

        self.assertTrue(purpose["persistence_purpose_declared"])
        self.assertTrue(purpose["persistence_purpose_preserved"])
        self.assertIs(purpose["persistence_does_not_create_standing"], True)
        self.assertIs(purpose["persistence_does_not_create_authority"], True)
        self.assertIs(purpose["persistence_does_not_create_currentness"], True)
        self.assertIs(purpose["persistence_does_not_create_distributed_standing"], True)

    def test_selected_record_category(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        category = result["selected_record_category"]

        self.assertEqual(
            "CARRIER_LIFECYCLE_STATUS_RECORD",
            category["selected_record_category"],
        )
        self.assertIs(category["selected_record_category_supported"], True)
        self.assertIs(category["category_is_not_database_schema"], True)
        self.assertIs(category["category_is_not_registry_authority"], True)

    def test_selected_carrier(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        selected_carrier = result["selected_carrier"]

        self.assertEqual(CARRIER_ID, selected_carrier["selected_carrier_id"])
        self.assertIs(selected_carrier["carrier_identity_declared"], True)
        self.assertIs(selected_carrier["carrier_record_is_not_source"], True)
        self.assertIs(selected_carrier["carrier_record_is_not_currentness"], True)
        self.assertIs(selected_carrier["carrier_record_is_not_authority"], True)
        self.assertIs(selected_carrier["carrier_record_is_not_distributed_standing"], True)

    def test_selected_referenced_artifacts(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request(category="CARRIER_EVIDENCE_REFERENCE_RECORD")
        )
        artifacts = result["selected_referenced_artifacts"]
        entries = artifacts["referenced_artifact_entries"]

        self.assertTrue(entries)
        self.assertIn(LIFECYCLE_ARTIFACT_ID, artifacts["referenced_artifact_ids"])
        self.assertIn(
            "CARRIER_LIFECYCLE_STATUS_RECORDED",
            artifacts["referenced_artifact_outcomes"],
        )
        self.assertTrue(entries[0]["referenced_artifact_path"])
        self.assertEqual(CARRIER_ID, entries[0]["carrier_id"])
        self.assertIs(artifacts["referenced_artifacts_preserved"], True)
        self.assertIs(artifacts["referenced_artifact_identity_preserved"], True)
        self.assertIs(artifacts["referenced_artifact_outcome_preserved"], True)
        self.assertIs(
            result["registry_persistence_basis"]["registry_does_not_upgrade_references"],
            True,
        )

    def test_registry_persistence_basis(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        basis = result["registry_persistence_basis"]

        self.assertIs(basis["registry_persistence_basis_declared"], True)
        self.assertIs(basis["lifecycle_reference_preserved"], True)
        self.assertIs(basis["relation_reference_preserved"], True)
        self.assertIs(basis["divergence_reference_preserved"], True)
        self.assertIs(basis["currentness_participation_reference_preserved"], True)
        self.assertIs(basis["admission_reference_preserved"], True)
        self.assertIs(basis["receipt_reference_preserved"], True)
        self.assertIs(basis["experiment_reference_preserved"], True)
        self.assertIs(basis["integrity_reference_preserved"], True)
        self.assertIs(basis["registry_preserves_references_only"], True)
        self.assertIs(basis["registry_does_not_upgrade_references"], True)
        self.assertIs(basis["registry_does_not_create_authority"], True)

    def test_preservation_and_non_authority_rules(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        preservation = result["persistence_preservation_rules"][
            "effective_persistence_preservation_rules"
        ]
        non_authority = result["registry_non_authority_rules"][
            "effective_registry_non_authority_rules"
        ]

        for key in (
            "referenced_artifact_identity_preserved",
            "referenced_artifact_outcome_preserved",
            "carrier_identity_preserved_where_available",
            "lifecycle_posture_preserved_where_available",
            "relation_posture_preserved_where_available",
            "divergence_posture_preserved_where_available",
            "currentness_participation_posture_preserved_where_available",
            "admission_posture_preserved_where_available",
            "receipt_or_refusal_posture_preserved_where_available",
            "does_not_mutate_referenced_artifact",
            "does_not_repair_by_overwrite",
            "does_not_hide_blocked_refused_corrupted_or_stale_posture",
            "latest_persisted_record_not_current",
        ):
            self.assertIs(preservation[key], True, key)

        for key in (
            "registry_presence_is_not_standing",
            "registry_absence_is_not_invalidation",
            "registry_freshness_is_not_currentness",
            "registry_completeness_is_not_authority",
            "registry_majority_is_not_truth",
            "registry_availability_is_not_priority",
            "registry_order_is_not_rank",
            "registry_label_is_not_role",
            "registry_role_history_is_not_permanent_role",
            "registry_lifecycle_status_is_not_source",
            "registry_lifecycle_status_is_not_currentness",
            "registry_lifecycle_status_is_not_permission",
        ):
            self.assertIs(non_authority[key], True, key)

    def test_registry_persistence_checks(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        checks = result["registry_persistence_checks"]

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True, check["check_name"])

        self.assertEqual(0, result["carrier_registry_persistence_summary"]["failed_check_count"])
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({c["check_name"] for c in checks}))

    def test_registry_persistence_statement(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        statement = result["registry_persistence_statement"]

        expected_true_keys = (
            "carrier_registry_persistence_boundary_recorded",
            "selected_record_category_preserved",
            "selected_carrier_preserved",
            "referenced_artifacts_preserved",
            "referenced_artifact_identity_preserved",
            "referenced_artifact_outcome_preserved",
            "lifecycle_reference_preserved",
            "relation_reference_preserved",
            "divergence_reference_preserved",
            "currentness_participation_reference_preserved",
            "evidence_reference_preserved",
            "non_claims_preserved",
        )
        for key in expected_true_keys:
            self.assertIs(statement[key], True, key)

        expected_false_keys = (
            "registry_presence_created_standing",
            "registry_created_source",
            "registry_created_currentness",
            "registry_created_authority",
            "registry_created_permission",
            "registry_created_carrier_hierarchy",
            "registry_created_distributed_standing",
            "registry_authorized_sync",
            "registry_authorized_full_body_transfer",
            "registry_created_second_body",
            "registry_authorized_continuation",
            "registry_authorized_distributed_operation",
            "registry_erased_evidence",
            "registry_repaired_by_overwrite",
        )
        for key in expected_false_keys:
            self.assertIs(statement[key], False, key)

    def test_registry_persistence_non_meaning(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        non_meaning = result["registry_persistence_non_meaning"]

        self.assertTrue(NON_MEANING_KEYS.issubset(non_meaning))
        for key in NON_MEANING_KEYS:
            self.assertIs(non_meaning[key], True, key)

    def test_what_remains_open(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        open_items = result["what_remains_open"]

        self.assertTrue(OPEN_KEYS.issubset(open_items))
        for key in OPEN_KEYS:
            self.assertIs(open_items[key], True, key)

    def test_summary_helper(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        summary = registry.build_carrier_registry_persistence_summary(result)

        self.assertEqual(result["outcome"], summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(REQUEST_ID, summary["registry_request_id"])
        self.assertTrue(summary["registry_question"])
        self.assertTrue(summary["persistence_purpose"])
        self.assertEqual(
            "RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
            summary["registry_intent"],
        )
        self.assertEqual(
            "CARRIER_LIFECYCLE_STATUS_RECORD",
            summary["selected_record_category"],
        )
        self.assertEqual(CARRIER_ID, summary["selected_carrier_id"])
        self.assertIn(LIFECYCLE_ARTIFACT_ID, summary["selected_referenced_artifact_ids"])
        self.assertIn(
            "CARRIER_LIFECYCLE_STATUS_RECORDED",
            summary["selected_referenced_artifact_outcomes"],
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(0, summary["failed_check_count"])
        self.assertIs(summary["carrier_registry_persistence_boundary_recorded"], True)
        self.assertIs(summary["referenced_artifact_identity_preserved"], True)
        self.assertIs(summary["referenced_artifact_outcome_preserved"], True)
        self.assertIs(summary["lifecycle_reference_preserved"], True)
        self.assertIs(summary["relation_reference_preserved"], True)
        self.assertIs(summary["divergence_reference_preserved"], True)
        self.assertIs(summary["currentness_participation_reference_preserved"], True)
        self.assertIs(summary["evidence_reference_preserved"], True)
        self.assertIs(summary["non_claims_preserved"], True)
        self.assertIs(summary["no_source_currentness_authority_permission"], True)
        self.assertIs(summary["no_carrier_hierarchy"], True)
        self.assertIs(summary["no_current_winning_losing_carrier_collapse"], True)
        self.assertIs(summary["no_divergence_resolution"], True)
        self.assertIs(summary["no_evidence_erasure"], True)
        self.assertIs(summary["no_hidden_refusal_divergence_corruption"], True)
        self.assertIs(summary["no_distributed_standing"], True)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation"], True)
        self.assertIs(summary["no_distributed_operation"], True)
        self.assertIs(summary["no_latest_record_file_currentness"], True)
        for key in registry.REQUIRED_NON_CLAIMS:
            self.assertIn(key, summary["key_non_claims"])

    def test_result_level_non_claims_for_all_outcomes(self) -> None:
        recorded = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        not_recorded = registry.resolve_carrier_registry_persistence_boundary(
            valid_request(
                intent="DO_NOT_RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
                not_recorded_reason="Registry/persistence posture intentionally not recorded.",
            )
        )
        blocked = registry.resolve_carrier_registry_persistence_boundary(None)

        for result in (recorded, not_recorded, blocked):
            self.assert_bounded_shape(result)
            self.assert_all_non_claims_false(result)

    def test_supported_record_categories(self) -> None:
        for category in SUPPORTED_CATEGORIES:
            with self.subTest(category=category):
                result = registry.resolve_carrier_registry_persistence_boundary(
                    valid_request(category=category)
                )
                self.assert_bounded_shape(result)
                self.assertEqual(
                    "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
                    result["outcome"],
                )

    def test_request_builder_helper(self) -> None:
        request = registry.build_declared_carrier_registry_persistence_request(
            registry_request_id="builder_registry_request_001",
            registry_question="What reference may be preserved without authority?",
            persistence_purpose="Preserve one evidence reference only.",
            selected_record_category="CARRIER_EVIDENCE_REFERENCE_RECORD",
            selected_carrier=_selected_carrier(),
            selected_referenced_artifacts=[_referenced_artifact()],
            registry_persistence_basis={
                "basis": "builder request preserves reference only",
            },
        )

        self.assertEqual("builder_registry_request_001", request["registry_request_id"])
        self.assertTrue(request["registry_question"])
        self.assertTrue(request["persistence_purpose"])
        self.assertEqual(
            "CARRIER_EVIDENCE_REFERENCE_RECORD",
            request["selected_record_category"],
        )
        self.assertEqual(
            "RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
            request["registry_intent"],
        )
        self.assertEqual(CARRIER_ID, request["selected_carrier"]["carrier_id"])
        self.assertEqual(
            LIFECYCLE_ARTIFACT_ID,
            request["selected_referenced_artifacts"][0]["artifact_id"],
        )
        self.assertTrue(request["registry_persistence_basis"])
        self.assertTrue(request["persistence_preservation_rules"])
        self.assertTrue(request["registry_non_authority_rules"])
        for key in registry.REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = registry.resolve_carrier_registry_persistence_boundary(request)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            result["outcome"],
        )

    def test_path_based_resolution(self) -> None:
        request = valid_request()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "registry_request.json"
            _write_json(path, request)

            path_result = registry.resolve_carrier_registry_persistence_boundary_from_path(path)
            mapping_result = registry.resolve_carrier_registry_persistence_boundary(request)

        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            path_result["outcome"],
        )
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertTrue(path_result["declared_registry_question"]["registry_request_path"])

    def test_write_behavior(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        with tempfile.TemporaryDirectory() as directory:
            output_path = Path(directory) / "nested" / "registry_result.json"
            written = registry.write_carrier_registry_persistence_result(
                result,
                output_path,
            )

            self.assertEqual(output_path, written)
            self.assertTrue(written.exists())
            loaded = _read_json(written)

        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded))
        self.assertEqual(result["outcome"], loaded["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request()
        )
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            with patch.object(registry, "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_ROOT", root):
                first = registry.write_carrier_registry_persistence_result(result)
                second = registry.write_carrier_registry_persistence_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertTrue(first.name.endswith("__carrier_registry_persistence_result.json"))
            self.assertTrue(second.stem.endswith("_001"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        original = copy.deepcopy(request)
        result = registry.resolve_carrier_registry_persistence_boundary(request)
        second = registry.resolve_carrier_registry_persistence_boundary(request)

        self.assertEqual(original, request)
        self.assertEqual(original["selected_carrier"], request["selected_carrier"])
        self.assertEqual(
            original["selected_referenced_artifacts"],
            request["selected_referenced_artifacts"],
        )
        self.assertEqual(result["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as directory:
            written = registry.write_carrier_registry_persistence_result(
                result,
                Path(directory) / "additive_result.json",
            )
            self.assertTrue(written.exists())
        self.assertEqual(original, request)

    def test_not_recorded_readable_request(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request(
                intent="DO_NOT_RECORD_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY",
                not_recorded_reason="Readable request does not record registry/persistence posture.",
            )
        )

        self.assert_bounded_shape(result)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_NOT_RECORDED",
            result["outcome"],
        )
        self.assertIs(
            result["registry_persistence_statement"][
                "carrier_registry_persistence_boundary_recorded"
            ],
            False,
        )
        self.assertEqual(
            "Readable request does not record registry/persistence posture.",
            result["registry_persistence_statement"]["not_recorded_reason"],
        )
        self.assertIsNone(result["block"]["block_code"])
        self.assertIs(result["registry_persistence_statement"]["registry_created_source"], False)
        self.assertIs(
            result["registry_persistence_statement"]["registry_created_currentness"],
            False,
        )

    def test_explicit_block_intent(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request(intent="BLOCK_CARRIER_REGISTRY_PERSISTENCE_BOUNDARY")
        )

        self.assert_bounded_shape(result)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED",
            result["outcome"],
        )
        self.assertEqual(
            "REGISTRY_REQUEST_EXPLICITLY_BLOCKED",
            result["block"]["block_code"],
        )
        self.assertIs(
            result["registry_persistence_statement"][
                "carrier_registry_persistence_boundary_recorded"
            ],
            False,
        )

    def test_blocking_missing_request(self) -> None:
        result = registry.resolve_carrier_registry_persistence_boundary()
        self.assert_bounded_shape(result)
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED",
            result["outcome"],
        )
        self.assertEqual("REGISTRY_QUESTION_UNDECLARED", result["block"]["block_code"])

    def test_blocking_malformed_request(self) -> None:
        self.assert_block_code(["not", "a", "mapping"], "DECLARED_REGISTRY_REQUEST_MALFORMED")

    def test_blocking_path_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            missing = registry.resolve_carrier_registry_persistence_boundary_from_path(
                root / "missing.json"
            )
            malformed_path = root / "malformed.json"
            malformed_path.write_text("{not-json", encoding="utf-8")
            malformed = registry.resolve_carrier_registry_persistence_boundary_from_path(
                malformed_path
            )
            array_path = root / "array.json"
            _write_json(array_path, [valid_request()])
            array_result = registry.resolve_carrier_registry_persistence_boundary_from_path(
                array_path
            )

        self.assertEqual(
            "DECLARED_REGISTRY_REQUEST_UNREADABLE",
            missing["block"]["block_code"],
        )
        self.assertEqual(
            "DECLARED_REGISTRY_REQUEST_MALFORMED",
            malformed["block"]["block_code"],
        )
        self.assertEqual(
            "DECLARED_REGISTRY_REQUEST_MALFORMED",
            array_result["block"]["block_code"],
        )

    def test_blocking_registry_question_purpose_intent(self) -> None:
        request = valid_request()
        request.pop("registry_question")
        self.assert_block_code(request, "REGISTRY_QUESTION_UNDECLARED")

        request = valid_request()
        request.pop("persistence_purpose")
        self.assert_block_code(request, "PERSISTENCE_PURPOSE_UNDECLARED")

        request = valid_request(registry_intent="UNSUPPORTED_INTENT")
        self.assert_block_code(request, "REGISTRY_INTENT_UNSUPPORTED")

    def test_blocking_carrier_identity_missing_for_required_category(self) -> None:
        self.assert_block_code(
            valid_request(
                category="CARRIER_IDENTITY_RECORD",
                selected_carrier={"carrier_label": "Carrier C"},
            ),
            "CARRIER_IDENTITY_MISSING",
        )

    def test_blocking_unsupported_record_category(self) -> None:
        self.assert_block_code(
            valid_request(category="UNSUPPORTED_RECORD_CATEGORY"),
            "RECORD_CATEGORY_UNSUPPORTED",
        )

    def test_blocking_referenced_artifact_missing_malformed_identity_outcome(self) -> None:
        missing_artifact = valid_request(category="CARRIER_EVIDENCE_REFERENCE_RECORD")
        missing_artifact.pop("selected_referenced_artifacts")
        self.assert_block_code(missing_artifact, "REFERENCED_ARTIFACT_MISSING")
        self.assert_block_code(
            valid_request(
                category="CARRIER_EVIDENCE_REFERENCE_RECORD",
                selected_referenced_artifacts="not-an-artifact",
            ),
            "REFERENCED_ARTIFACT_MALFORMED",
        )
        self.assert_block_code(
            valid_request(
                category="CARRIER_EVIDENCE_REFERENCE_RECORD",
                selected_referenced_artifacts=[{"outcome": "RECORDED"}],
            ),
            "REFERENCED_ARTIFACT_IDENTITY_MISSING",
        )
        self.assert_block_code(
            valid_request(
                category="CARRIER_EVIDENCE_REFERENCE_RECORD",
                selected_referenced_artifacts=[{"artifact_id": "artifact_without_outcome"}],
            ),
            "REFERENCED_ARTIFACT_OUTCOME_MISSING",
        )

    def test_blocking_registry_decides_source_or_currentness(self) -> None:
        self.assert_block_code(
            valid_request(registry_decides_source=True),
            "REGISTRY_DECIDES_SOURCE",
        )
        self.assert_block_code(
            valid_request(registry_decides_currentness=True),
            "REGISTRY_DECIDES_CURRENTNESS",
        )
        self.assert_block_code(
            valid_request(registry_created_source=True),
            "REGISTRY_DECIDES_SOURCE",
        )
        self.assert_block_code(
            valid_request(registry_created_currentness=True),
            "REGISTRY_DECIDES_CURRENTNESS",
        )

    def test_blocking_authority_permission_hierarchy(self) -> None:
        self.assert_block_code(
            valid_request(registry_created_authority=True),
            "REGISTRY_CREATES_AUTHORITY",
        )
        self.assert_block_code(
            valid_request(registry_created_permission=True),
            "REGISTRY_CREATES_PERMISSION",
        )
        self.assert_block_code(
            valid_request(registry_created_carrier_hierarchy=True),
            "REGISTRY_CREATES_CARRIER_HIERARCHY",
        )

    def test_blocking_current_winning_losing_carrier(self) -> None:
        self.assert_block_code(
            valid_request(current_carrier_selected=True),
            "REGISTRY_SELECTS_CURRENT_CARRIER",
        )
        self.assert_block_code(
            valid_request(winning_carrier_selected=True),
            "REGISTRY_SELECTS_WINNING_CARRIER",
        )
        self.assert_block_code(
            valid_request(losing_carrier_invalidated=True),
            "REGISTRY_INVALIDATES_LOSING_CARRIER",
        )

    def test_blocking_divergence_erasure_hidden_posture(self) -> None:
        self.assert_block_code(
            valid_request(registry_resolves_divergence=True),
            "REGISTRY_RESOLVES_DIVERGENCE",
        )
        self.assert_block_code(
            valid_request(registry_erased_evidence=True),
            "REGISTRY_ERASES_EVIDENCE",
        )
        self.assert_block_code(
            valid_request(registry_hid_refusal=True),
            "REGISTRY_HIDES_REFUSAL",
        )
        self.assert_block_code(
            valid_request(registry_hid_divergence=True),
            "REGISTRY_HIDES_DIVERGENCE",
        )
        self.assert_block_code(
            valid_request(registry_hid_corruption=True),
            "REGISTRY_HIDES_CORRUPTION",
        )

    def test_blocking_repair_by_overwrite_mutation_replay_merge(self) -> None:
        self.assert_block_code(
            valid_request(registry_repaired_by_overwrite=True),
            "REGISTRY_REPAIRS_BY_OVERWRITE",
        )
        self.assert_block_code(
            valid_request(mutation_performed=True),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
        self.assert_block_code(
            valid_request(replay_performed=True),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )
        self.assert_block_code(
            valid_request(merge_performed=True),
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        )

    def test_blocking_distributed_standing_sync_transfer_second_body(self) -> None:
        self.assert_block_code(
            valid_request(registry_created_distributed_standing=True),
            "REGISTRY_CREATES_DISTRIBUTED_STANDING",
        )
        self.assert_block_code(
            valid_request(registry_authorized_sync=True),
            "REGISTRY_AUTHORIZES_REPOSITORY_SYNC",
        )
        self.assert_block_code(
            valid_request(registry_authorized_full_body_transfer=True),
            "REGISTRY_AUTHORIZES_FULL_BODY_TRANSFER",
        )
        self.assert_block_code(
            valid_request(registry_created_second_body=True),
            "REGISTRY_CREATES_SECOND_BODY",
        )

    def test_blocking_continuation_distributed_operation(self) -> None:
        self.assert_block_code(
            valid_request(registry_authorized_continuation=True),
            "REGISTRY_AUTHORIZES_CONTINUATION",
        )
        self.assert_block_code(
            valid_request(registry_authorized_distributed_operation=True),
            "REGISTRY_AUTHORIZES_DISTRIBUTED_OPERATION",
        )

    def test_blocking_latest_record_file_currentness(self) -> None:
        self.assert_block_code(
            valid_request(latest_record_currentness=True),
            "LATEST_RECORD_CURRENTNESS",
        )
        self.assert_block_code(
            valid_request(latest_file_currentness=True),
            "LATEST_FILE_CURRENTNESS",
        )
        self.assert_block_code(
            valid_request(recency_fraud=True),
            "LATEST_FILE_CURRENTNESS",
        )

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        claims = _non_claims()
        claims.pop("registry_created_source")
        missing_result = self.assert_block_code(
            valid_request(non_claims=claims),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        self.assertIn(
            "declared_non_claims",
            missing_result["declared_registry_question"],
        )

        claims = _non_claims(registry_created_authority=True)
        flipped_result = registry.resolve_carrier_registry_persistence_boundary(
            valid_request(non_claims=claims)
        )
        self.assertEqual(
            "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_BLOCKED",
            flipped_result["outcome"],
        )
        self.assertIn(
            flipped_result["block"]["block_code"],
            {"REGISTRY_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assert_all_non_claims_false(flipped_result)


if __name__ == "__main__":
    unittest.main()
