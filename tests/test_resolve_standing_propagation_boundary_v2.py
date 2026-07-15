"""Tests for the standing propagation boundary v2 successor resolver.

This suite audits one lineage-preserving v2 resolver. V1 remains standing and
is not mutated. V2 records standing propagation posture only and improves the
truthful projection of nested refusal, divergence, and receipt/refusal/return/
admission posture into statement and summary fields. It does not create
distributed standing, currentness, source replacement, authority, permission,
carrier hierarchy, repository synchronization, full body transfer,
continuation, distributed operation, receipt-standing, admission-standing, or
registry-standing.
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

import resolve_standing_propagation_boundary_v2 as propagation  # noqa: E402


TOP_LEVEL_SECTIONS = {
    "standing_propagation_metadata",
    "declared_standing_propagation_question",
    "selected_standing_surface_or_artifact",
    "source_standing_basis",
    "selected_carriers",
    "carried_surface_or_packet_basis",
    "standing_propagation_basis",
    "standing_propagation_posture",
    "related_carrier_evidence",
    "propagation_checks",
    "propagation_statement",
    "propagation_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "standing_propagation_summary",
}

OUTCOME_FAMILY = {
    "STANDING_PROPAGATION_POSTURE_RECORDED",
    "STANDING_PROPAGATION_POSTURE_NOT_RECORDED",
    "STANDING_PROPAGATION_POSTURE_BLOCKED",
}

SUPPORTED_POSTURES = [
    "SOURCE_STANDING_PRESERVED",
    "STANDING_CARRIED_AS_EVIDENCE",
    "CARRIED_STANDING_RECEIVED",
    "CARRIED_STANDING_REFUSED_OR_BLOCKED",
    "CARRIED_STANDING_RETURNED",
    "CARRIED_STANDING_ADMITTED_AS_EVIDENCE",
    "CARRIED_STANDING_DIVERGENCE_RECORDED",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_ELIGIBLE",
    "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_EXCLUDED",
    "CARRIED_STANDING_RELATION_RECOGNIZED",
    "CARRIED_STANDING_RELATION_CONFORMANT",
    "CARRIED_STANDING_RELATION_CLOSED",
    "CARRIED_STANDING_LIFECYCLE_REFERENCED",
    "CARRIED_STANDING_REGISTRY_REFERENCED",
    "CARRIED_STANDING_STALE",
    "CARRIED_STANDING_CORRUPTED",
    "CARRIED_STANDING_EXCLUDED_FROM_RELIANCE",
    "STANDING_PROPAGATION_BLOCKED",
]

EXPECTED_CHECK_NAMES = {
    "declared_standing_propagation_request_parseable_mapping",
    "standing_propagation_question_declared",
    "standing_propagation_intent_supported",
    "selected_standing_surface_or_artifact_present",
    "selected_standing_surface_or_artifact_parseable",
    "selected_standing_surface_or_artifact_identity_present",
    "requested_propagation_posture_supported",
    "standing_propagation_basis_declared",
    "source_standing_basis_preserved_where_required",
    "carrier_identity_preserved_where_required_or_supplied",
    "carried_surface_or_packet_basis_preserved_where_required",
    "receipt_refusal_return_admission_posture_preserved_where_required",
    "lineage_preserved",
    "visible_refusal_preserved_where_applicable",
    "visible_divergence_preserved_where_applicable",
    "visible_corruption_preserved_where_applicable",
    "visible_staleness_preserved_where_applicable",
    "no_source_replacement",
    "no_currentness",
    "no_authority",
    "no_permission",
    "no_carrier_hierarchy",
    "no_current_carrier_selected",
    "no_winning_carrier_selected",
    "no_losing_carrier_invalidated",
    "no_divergence_resolution",
    "no_evidence_erasure",
    "no_repair_by_overwrite",
    "no_distributed_standing",
    "no_repository_synchronization",
    "no_full_body_transfer",
    "no_second_body",
    "no_continuation",
    "no_distributed_operation",
    "no_registry_reference_standing",
    "no_receipt_standing",
    "no_admission_standing",
    "no_latest_copy_currentness",
    "no_latest_file_currentness_or_recency_fraud",
    "no_mutation_replay_or_merge",
    "non_claims_remain_false",
}

NON_MEANING_KEYS = {
    "does_not_mean_distributed_standing",
    "does_not_mean_currentness",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_standing_on_every_carrier",
    "does_not_mean_standing_on_receiving_carrier",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_carrier_priority",
    "does_not_mean_carrier_sovereignty",
    "does_not_mean_current_carrier_selected",
    "does_not_mean_winning_carrier_selected",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_divergence_resolved",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_carrier_registry_authority",
    "does_not_mean_persistence_as_standing",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
    "does_not_mean_automatic_admission",
    "does_not_mean_automatic_relation",
    "does_not_mean_automatic_currentness",
    "does_not_mean_automatic_conformance",
    "does_not_mean_automatic_closure",
    "does_not_mean_distributed_operation",
    "does_not_mean_success_means_propagation",
    "does_not_mean_registry_reference_means_propagation",
    "does_not_mean_receipt_means_standing",
    "does_not_mean_admission_means_standing",
    "does_not_mean_latest_propagated_record_currentness",
    "does_not_mean_majority_carrier_standing",
    "does_not_mean_successful_receipt_count_standing",
}

OPEN_KEYS = {
    "standing_propagation_implementation_refinement",
    "cross_carrier_currentness_successor_law",
    "divergence_consequence_law",
    "distributed_standing_boundary",
    "distributed_standing",
    "carrier_registry_implementation",
    "persistence_implementation",
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

V1_OUTPUT_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_standing_propagation_boundary"
)


def _read_json(path: Path) -> dict[str, object]:
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
    claims = copy.deepcopy(propagation.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _selected_surface(**updates: object) -> dict[str, object]:
    surface: dict[str, object] = {
        "artifact_id": "standing_surface_current_body_closure_001",
        "artifact_type": "standing_surface",
        "artifact_class": "standing_related_artifact",
        "outcome": "BODY_CONFORMANT",
        "artifact_status": "standing_related_evidence",
    }
    surface.update(updates)
    return surface


def _source_basis(**updates: object) -> dict[str, object]:
    basis: dict[str, object] = {
        "source_standing_basis_id": "current_body_conformance_v3_closure_source_basis",
        "source_standing_surface_id": "standing_surface_current_body_closure_001",
        "source_standing_basis_preserved_upstream": True,
        "source_standing_preserved": True,
        "source_standing_remains_upstream": True,
        "carrying_does_not_move_source_standing": True,
        "receipt_does_not_replace_source_standing": True,
        "return_admission_relation_lifecycle_registry_do_not_move_source_standing": True,
    }
    basis.update(updates)
    return basis


def _selected_carriers() -> list[dict[str, object]]:
    return [
        {
            "carrier_id": "carrier_A_current_body_context",
            "carrier_label": "Carrier A",
            "carrier_role": "source_context",
        },
        {
            "carrier_id": "carrier_B_successful_receipt_context",
            "carrier_label": "Carrier B",
            "carrier_role": "receiving_evidence_context",
        },
        {
            "carrier_id": "carrier_C_blocked_receipt_context",
            "carrier_label": "Carrier C",
            "carrier_role": "receiving_evidence_context",
        },
    ]


def _carried_basis(**updates: object) -> dict[str, object]:
    basis: dict[str, object] = {
        "carried_surface_or_packet_id": "standing_related_packet_001",
        "source_basis": "current body closure remains upstream",
        "receipt_basis": "receipt/refusal evidence remains evidence",
        "refusal_basis": "blocked carrier posture remains visible",
        "carried_basis_does_not_create_currentness": True,
        "carried_basis_does_not_replace_source": True,
    }
    basis.update(updates)
    return basis


def _related_evidence() -> list[dict[str, object]]:
    return [
        {
            "evidence_id": "carrier_B_successful_receipt_evidence",
            "outcome": "CARRIED_SURFACE_RECEIVED",
            "carrier_id": "carrier_B_successful_receipt_context",
            "evidence_role": "successful_receipt_evidence",
            "evidence_class": "receipt_evidence",
        },
        {
            "evidence_id": "carrier_C_blocked_receipt_evidence",
            "outcome": "RECEIPT_BLOCK",
            "carrier_id": "carrier_C_blocked_receipt_context",
            "evidence_role": "blocked_receipt_evidence",
            "evidence_class": "refusal_evidence",
        },
        {
            "evidence_id": "carrier_B_C_visible_divergence_evidence",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
            "evidence_role": "visible_divergence_evidence",
            "evidence_class": "divergence_evidence",
        },
        {
            "evidence_id": "carrier_C_currentness_participation_evidence",
            "outcome": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
            "carrier_id": "carrier_C_blocked_receipt_context",
            "evidence_role": "currentness_participation_evidence",
        },
        {
            "evidence_id": "carrier_C_lifecycle_refused_or_blocked_001",
            "outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
            "evidence_role": "lifecycle_evidence",
            "evidence_class": "carrier_lifecycle_status_recorded",
        },
        {
            "evidence_id": "carrier_C_registry_persistence_v2_reference_001",
            "outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
            "evidence_role": "registry_persistence_reference_evidence",
            "evidence_class": "carrier_registry_persistence_boundary_recorded",
        },
    ]


def _postures() -> dict[str, dict[str, object]]:
    return {
        "receipt_posture": {
            "posture": "CARRIED_STANDING_RECEIVED",
            "preserved": True,
        },
        "refusal_posture": {
            "posture": "CARRIED_STANDING_REFUSED_OR_BLOCKED",
            "preserved": True,
            "visible_refusal_preserved": True,
        },
        "return_posture": {
            "posture": "CARRIED_STANDING_RETURNED",
            "preserved": True,
            "return_did_not_create_admission": True,
        },
        "admission_posture": {
            "posture": "CARRIED_STANDING_ADMITTED_AS_EVIDENCE",
            "preserved": True,
            "admission_as_evidence_only": True,
        },
        "divergence_posture": {
            "posture": "CARRIED_STANDING_DIVERGENCE_RECORDED",
            "preserved": True,
            "visible_divergence_preserved": True,
        },
        "currentness_participation_posture": {
            "posture": "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_ELIGIBLE",
            "preserved": True,
            "participation_only": True,
        },
        "relation_posture": {
            "posture": "CARRIED_STANDING_RELATION_CLOSED",
            "preserved": True,
            "relation_closure_is_meaning_only": True,
        },
        "lifecycle_posture": {
            "posture": "CARRIER_REFUSED_OR_BLOCKED",
            "preserved": True,
            "requested_lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
        },
        "registry_persistence_posture": {
            "posture": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            "preserved": True,
            "lifecycle_reference_preserved": True,
            "registry_reference_is_not_standing": True,
            "persistence_is_not_currentness": True,
        },
    }


def _standing_basis(**updates: object) -> dict[str, object]:
    postures = _postures()
    basis: dict[str, object] = {
        "standing_propagation_basis_id": "standing_propagation_basis_v2_001",
        "source_standing_basis": _source_basis(),
        "source_standing_preserved": True,
        "receipt_refusal_return_admission_posture": {
            "carrier_c_returned_blocked_receipt_preserved": True,
            "return_did_not_create_admission": True,
            "admission_as_evidence_only": True,
            "receipt_preserved": True,
            "refusal_preserved": True,
            "return_preserved": True,
            "admission_preserved": True,
        },
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "receipt_posture": copy.deepcopy(postures["receipt_posture"]),
        "refusal_posture": copy.deepcopy(postures["refusal_posture"]),
        "return_posture": copy.deepcopy(postures["return_posture"]),
        "admission_posture": copy.deepcopy(postures["admission_posture"]),
        "divergence_posture": copy.deepcopy(postures["divergence_posture"]),
        "currentness_participation_posture": copy.deepcopy(
            postures["currentness_participation_posture"]
        ),
        "relation_posture": copy.deepcopy(postures["relation_posture"]),
        "lifecycle_posture": copy.deepcopy(postures["lifecycle_posture"]),
        "registry_persistence_posture": copy.deepcopy(
            postures["registry_persistence_posture"]
        ),
        "lineage_basis": {
            "lineage_preserved": True,
            "source_standing_remains_upstream": True,
        },
        "visible_refusal_basis": {
            "visible_refusal_preserved": True,
            "refusal_preserved": True,
        },
        "visible_divergence_basis": {
            "visible_divergence_preserved": True,
            "divergence_preserved": True,
        },
        "visible_corruption_basis": {
            "visible_corruption_preserved": True,
            "corruption_preserved": True,
        },
        "visible_staleness_basis": {
            "visible_staleness_preserved": True,
            "staleness_preserved": True,
        },
        "non_claims_preserved": True,
    }
    basis.update(updates)
    return basis


def valid_request(
    *,
    posture: str = "CARRIED_STANDING_REGISTRY_REFERENCED",
    intent: str = "RECORD_STANDING_PROPAGATION_POSTURE",
    standing_basis: object | None = None,
    related_carrier_evidence: object | None = None,
    non_claims: dict[str, bool] | None = None,
    include_explicit_postures: bool = True,
    **updates: object,
) -> dict[str, object]:
    selected_carriers = _selected_carriers()
    postures = _postures()
    request: dict[str, object] = {
        "standing_propagation_request_id": "standing_propagation_v2_request_001",
        "standing_propagation_question": (
            "What posture does standing-related evidence have when carried across carriers?"
        ),
        "standing_propagation_intent": intent,
        "selected_standing_surface_or_artifact": _selected_surface(),
        "requested_propagation_posture": posture,
        "source_standing_basis": _source_basis(),
        "selected_carriers": selected_carriers,
        "source_carrier": selected_carriers[0],
        "receiving_carrier": selected_carriers[2],
        "carried_surface_or_packet_basis": _carried_basis(),
        "related_carrier_evidence": _related_evidence()
        if related_carrier_evidence is None
        else related_carrier_evidence,
        "lineage_basis": {
            "lineage_preserved": True,
            "source_standing_remains_upstream": True,
        },
        "visible_refusal_basis": {
            "visible_refusal_preserved": True,
            "refusal_preserved": True,
        },
        "visible_divergence_basis": {
            "visible_divergence_preserved": True,
            "divergence_preserved": True,
        },
        "visible_corruption_basis": {
            "visible_corruption_preserved": True,
            "corruption_preserved": True,
        },
        "visible_staleness_basis": {
            "visible_staleness_preserved": True,
            "staleness_preserved": True,
        },
        "standing_propagation_basis": _standing_basis()
        if standing_basis is None
        else standing_basis,
        "declared_non_claims": _non_claims() if non_claims is None else non_claims,
    }
    if include_explicit_postures:
        request.update(copy.deepcopy(postures))
    request.update(updates)
    return request


def _remove_nested(request: dict[str, object], *keys: str) -> None:
    for key in keys:
        request.pop(key, None)
        basis = request.get("standing_propagation_basis")
        if isinstance(basis, dict):
            basis.pop(key, None)


class StandingPropagationBoundaryV2Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.request = valid_request()
        self.result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=self.request
        )

    def assert_bounded_shape(self, result: dict[str, object]) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assert_recorded(self, result: dict[str, object]) -> None:
        self.assert_bounded_shape(result)
        self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(0, result["standing_propagation_summary"]["failed_check_count"])
        self.assertIs(
            result["propagation_statement"]["standing_propagation_posture_recorded"],
            True,
        )

    def assert_block_code(
        self,
        request: object,
        expected_code: str,
    ) -> dict[str, object]:
        result = propagation.resolve_standing_propagation_boundary(  # type: ignore[arg-type]
            declared_propagation_request=request
        )
        self.assert_bounded_shape(result)
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", result["outcome"])
        self.assertEqual(expected_code, result["block"]["block_code"])
        self.assert_all_required_non_claims_false(result)
        return result

    def assert_all_required_non_claims_false(self, result: dict[str, object]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for key in propagation.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_no_collapse_statement(self, statement: dict[str, object]) -> None:
        false_keys = (
            "source_replaced",
            "currentness_created",
            "authority_created",
            "permission_created",
            "carrier_hierarchy_created",
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "divergence_resolved",
            "evidence_erased",
            "repaired_by_overwrite",
            "distributed_standing_created",
            "repository_synchronization_authorized",
            "full_body_transfer_authorized",
            "second_body_created",
            "continuation_authorized",
            "distributed_operation_authorized",
            "standing_propagation_made_registry_reference_standing",
            "standing_propagation_made_receipt_standing",
            "standing_propagation_made_admission_standing",
            "standing_on_receiving_carrier_created",
            "received_standing_evidence_became_standing_on_receiver",
            "returned_standing_evidence_became_admission",
            "admitted_standing_evidence_became_source",
            "latest_copy_currentness",
            "latest_file_currentness",
            "recency_fraud",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
        )
        for key in false_keys:
            self.assertIs(statement[key], False, key)

    def assert_v2_projection_true(self, result: dict[str, object]) -> None:
        statement = result["propagation_statement"]
        summary = result["standing_propagation_summary"]
        for key in (
            "source_standing_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "receipt_refusal_return_admission_posture_preserved",
            "divergence_posture_preserved",
            "lifecycle_posture_preserved",
            "registry_persistence_posture_preserved",
            "lineage_preserved",
        ):
            self.assertIs(statement[key], True, key)
            self.assertIs(summary[key], True, key)

    def test_successful_v2_standing_propagation_posture_recording(self) -> None:
        self.assert_recorded(self.result)
        statement = self.result["propagation_statement"]
        self.assertIs(statement["selected_standing_surface_or_artifact_preserved"], True)
        self.assertIs(statement["requested_propagation_posture_preserved"], True)
        self.assertIs(statement["selected_carriers_preserved"], True)
        self.assertIs(statement["carried_surface_or_packet_basis_preserved"], True)
        self.assertIs(statement["currentness_participation_posture_preserved"], True)
        self.assertIs(statement["relation_posture_preserved"], True)
        self.assertIs(statement["visible_corruption_preserved"], True)
        self.assertIs(statement["visible_staleness_preserved"], True)
        self.assert_v2_projection_true(self.result)
        self.assert_no_collapse_statement(statement)

    def test_metadata_successor_lineage_and_public_api_shape(self) -> None:
        metadata = self.result["standing_propagation_metadata"]
        self.assertTrue(metadata["standing_propagation_result_id"])
        self.assertTrue(metadata["standing_propagation_result_type"])
        self.assertTrue(metadata["standing_propagation_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertTrue(metadata["resolver_module"])
        self.assertTrue(metadata["successor_of_module"])
        self.assertEqual("0.2.0", metadata["standing_propagation_result_version"])
        self.assertEqual(
            "resolve_standing_propagation_boundary_v2",
            metadata["resolver_module"],
        )
        self.assertEqual(
            "resolve_standing_propagation_boundary",
            metadata["successor_of_module"],
        )
        self.assertEqual(
            "resolve_standing_propagation_boundary",
            self.result["standing_propagation_summary"]["successor_of_module"],
        )
        for name in (
            "resolve_standing_propagation_boundary",
            "resolve_standing_propagation_boundary_from_path",
            "write_standing_propagation_result",
            "build_standing_propagation_summary",
            "build_declared_standing_propagation_request",
        ):
            self.assertTrue(callable(getattr(propagation, name)))

    def test_declared_question_selected_surface_source_carriers_and_carried_basis(
        self,
    ) -> None:
        question = self.result["declared_standing_propagation_question"]
        self.assertEqual(
            "standing_propagation_v2_request_001",
            question["standing_propagation_request_id"],
        )
        self.assertEqual(
            self.request["standing_propagation_question"],
            question["standing_propagation_question"],
        )
        self.assertEqual(
            "RECORD_STANDING_PROPAGATION_POSTURE",
            question["standing_propagation_intent"],
        )
        self.assertEqual(question["declared_non_claims"], self.request["declared_non_claims"])
        self.assertIs(question["standing_propagation_is_not_distributed_standing"], True)
        self.assertIs(question["standing_propagation_is_not_currentness"], True)
        self.assertIs(question["standing_propagation_is_not_authority"], True)
        self.assertIs(question["standing_propagation_does_not_replace_source"], True)
        self.assertIs(
            question[
                "standing_propagation_does_not_authorize_sync_full_body_transfer_or_distributed_operation"
            ],
            True,
        )

        posture = self.result["standing_propagation_posture"]
        self.assertEqual(
            "CARRIED_STANDING_REGISTRY_REFERENCED",
            posture["requested_propagation_posture"],
        )
        self.assertIs(posture["requested_propagation_posture_supported"], True)
        self.assertIs(posture["posture_does_not_mean_standing_on_receiving_carrier"], True)

        selected = self.result["selected_standing_surface_or_artifact"]
        self.assertEqual(
            "standing_surface_current_body_closure_001",
            selected["selected_standing_surface_or_artifact_id"],
        )
        raw_selected = selected["raw_selected_standing_surface_or_artifact"]
        self.assertEqual("BODY_CONFORMANT", raw_selected["outcome"])
        self.assertEqual("standing_surface", raw_selected["artifact_type"])
        self.assertTrue(selected["selected_standing_surface_or_artifact_identity_present"])
        self.assertTrue(selected["selected_artifact_remains_evidence_or_reference"])
        self.assertTrue(selected["selected_artifact_does_not_create_currentness"])
        self.assertTrue(selected["selected_artifact_does_not_become_distributed_standing"])

        source = self.result["source_standing_basis"]
        self.assertTrue(source["source_standing_basis_declared"])
        self.assertTrue(source["source_standing_basis_preserved"])
        self.assertTrue(source["source_standing_preserved"])
        self.assertTrue(source["source_standing_remains_upstream"])
        self.assertTrue(source["carrying_does_not_move_source_standing"])
        self.assertTrue(source["receipt_does_not_replace_source_standing"])
        self.assertTrue(source["admission_does_not_move_source_standing"])
        self.assertTrue(source["registry_reference_does_not_move_source_standing"])

        carriers = self.result["selected_carriers"]
        carrier_ids = set(carriers["selected_carrier_ids"])
        self.assertIn("carrier_A_current_body_context", carrier_ids)
        self.assertIn("carrier_B_successful_receipt_context", carrier_ids)
        self.assertIn("carrier_C_blocked_receipt_context", carrier_ids)
        self.assertTrue(carriers["carrier_identity_preserved_where_supplied"])
        self.assertTrue(carriers["carriers_do_not_become_currentness"])
        self.assertTrue(carriers["carriers_do_not_create_distributed_standing"])

        carried = self.result["carried_surface_or_packet_basis"]
        self.assertTrue(carried["carried_surface_or_packet_basis_declared"])
        self.assertTrue(carried["carried_surface_or_packet_basis_preserved"])
        self.assertEqual(
            "standing_related_packet_001",
            carried["raw_carried_surface_or_packet_basis"][
                "carried_surface_or_packet_id"
            ],
        )
        self.assertTrue(carried["carried_surface_does_not_become_currentness"])
        self.assertTrue(carried["carried_surface_does_not_become_standing_on_receiver"])

    def test_v2_projection_from_nested_standing_propagation_basis_only(self) -> None:
        request = valid_request(include_explicit_postures=False)
        for key in (
            "visible_refusal_basis",
            "visible_divergence_basis",
            "visible_corruption_basis",
            "visible_staleness_basis",
        ):
            request.pop(key, None)

        result = propagation.resolve_standing_propagation_boundary(request)

        self.assert_recorded(result)
        self.assert_v2_projection_true(result)
        raw_basis = result["standing_propagation_basis"]["raw_standing_propagation_basis"]
        self.assertTrue(raw_basis["visible_refusal_preserved"])
        self.assertTrue(raw_basis["visible_divergence_preserved"])
        self.assertTrue(
            raw_basis["receipt_refusal_return_admission_posture"][
                "carrier_c_returned_blocked_receipt_preserved"
            ]
        )

    def test_v2_projection_from_related_evidence(self) -> None:
        minimal_basis = {
            "standing_propagation_basis_id": "related_evidence_projection_basis",
            "source_standing_preserved": True,
            "lineage_basis": {"lineage_preserved": True},
        }
        request = valid_request(
            standing_basis=minimal_basis,
            include_explicit_postures=False,
        )
        for key in (
            "visible_refusal_basis",
            "visible_divergence_basis",
            "visible_corruption_basis",
            "visible_staleness_basis",
        ):
            request.pop(key, None)

        result = propagation.resolve_standing_propagation_boundary(request)

        self.assert_recorded(result)
        self.assertIs(
            result["standing_propagation_summary"]["visible_refusal_preserved"],
            True,
        )
        self.assertIs(
            result["standing_propagation_summary"]["visible_divergence_preserved"],
            True,
        )
        self.assertIs(result["propagation_statement"]["visible_refusal_preserved"], True)
        self.assertIs(result["propagation_statement"]["visible_divergence_preserved"], True)
        self.assertFalse(result["propagation_statement"]["standing_propagation_made_receipt_standing"])

    def test_v2_projection_from_explicit_top_level_posture_fields(self) -> None:
        request = valid_request(
            standing_basis={
                "standing_propagation_basis_id": "explicit_projection_basis",
                "source_standing_preserved": True,
                "lineage_basis": {"lineage_preserved": True},
            },
            include_explicit_postures=False,
            refusal_posture={"visible_refusal_preserved": True},
            divergence_posture={"visible_divergence_preserved": True},
            return_posture={"return_did_not_create_admission": True},
            admission_posture={"admission_as_evidence_only": True},
        )
        request.pop("visible_refusal_basis", None)
        request.pop("visible_divergence_basis", None)

        result = propagation.resolve_standing_propagation_boundary(request)

        self.assert_recorded(result)
        self.assertIs(
            result["standing_propagation_summary"]["visible_refusal_preserved"],
            True,
        )
        self.assertIs(
            result["standing_propagation_summary"]["visible_divergence_preserved"],
            True,
        )
        self.assertIs(
            result["standing_propagation_summary"][
                "receipt_refusal_return_admission_posture_preserved"
            ],
            True,
        )

    def test_regression_for_live_v1_mismatch_shape(self) -> None:
        basis = _standing_basis(
            visible_refusal_preserved=True,
            visible_divergence_preserved=True,
            receipt_refusal_return_admission_posture={
                "carrier_c_returned_blocked_receipt_preserved": True,
                "return_did_not_create_admission": True,
                "admission_as_evidence_only": True,
            },
            divergence_posture={"visible_divergence_preserved": True},
            registry_persistence_posture={"lifecycle_reference_preserved": True},
        )
        request = valid_request(
            standing_basis=basis,
            include_explicit_postures=False,
        )

        result = propagation.resolve_standing_propagation_boundary(request)
        summary = result["standing_propagation_summary"]

        self.assert_recorded(result)
        self.assertIs(summary["visible_refusal_preserved"], True)
        self.assertIs(summary["visible_divergence_preserved"], True)
        self.assertIs(
            summary["receipt_refusal_return_admission_posture_preserved"],
            True,
        )
        self.assertIs(summary["divergence_posture_preserved"], True)
        self.assertIs(summary["lifecycle_posture_preserved"], True)
        self.assertIs(summary["registry_persistence_posture_preserved"], True)
        self.assertIs(summary["source_standing_preserved"], True)
        self.assertIs(summary["lineage_preserved"], True)

    def test_standing_propagation_basis_and_related_evidence_preservation(self) -> None:
        basis = self.result["standing_propagation_basis"]
        self.assertTrue(basis["standing_propagation_basis_declared"])
        self.assertTrue(basis["standing_propagation_basis_preserved"])
        for key in (
            "receipt_posture",
            "refusal_posture",
            "return_posture",
            "admission_posture",
            "divergence_posture",
            "currentness_participation_posture",
            "relation_posture",
            "lifecycle_posture",
            "registry_persistence_posture",
        ):
            self.assertIn(key, basis)
            self.assertTrue(basis[key]["preserved"], key)
        self.assertTrue(basis["lineage_preserved"])
        self.assertTrue(basis["visible_refusal_preserved"])
        self.assertTrue(basis["visible_divergence_preserved"])
        self.assertTrue(basis["visible_corruption_preserved"])
        self.assertTrue(basis["visible_staleness_preserved"])
        self.assertTrue(basis["propagation_preserves_evidence_not_force"])
        self.assertTrue(basis["propagation_does_not_create_distributed_standing"])
        self.assertTrue(basis["propagation_does_not_authorize_continuation"])
        raw_basis = basis["raw_standing_propagation_basis"]
        self.assertEqual(
            "current_body_conformance_v3_closure_source_basis",
            raw_basis["source_standing_basis"]["source_standing_basis_id"],
        )
        self.assertTrue(raw_basis["non_claims_preserved"])

        related = self.result["related_carrier_evidence"]
        self.assertTrue(related["related_carrier_evidence_preserved"])
        evidence_ids = set(related["related_carrier_evidence_ids"])
        self.assertIn("carrier_B_successful_receipt_evidence", evidence_ids)
        self.assertIn("carrier_C_blocked_receipt_evidence", evidence_ids)
        self.assertIn("carrier_B_C_visible_divergence_evidence", evidence_ids)
        self.assertIn("carrier_C_currentness_participation_evidence", evidence_ids)
        self.assertIn("carrier_C_lifecycle_refused_or_blocked_001", evidence_ids)
        self.assertIn("carrier_C_registry_persistence_v2_reference_001", evidence_ids)
        self.assertIn("RECEIPT_BLOCK", related["related_carrier_evidence_outcomes"])
        self.assertIn(
            "CARRIER_DIVERGENCE_RECORDED",
            related["related_carrier_evidence_outcomes"],
        )
        self.assertIn(
            "carrier_C_blocked_receipt_context",
            related["related_carrier_ids"],
        )
        self.assertTrue(related["evidence_remains_evidence"])
        self.assertTrue(related["evidence_does_not_create_standing_by_relation"])

    def test_checks_statement_non_meaning_open_and_summary(self) -> None:
        checks = self.result["propagation_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertIs(check["passed"], True, check)
        self.assertEqual(EXPECTED_CHECK_NAMES, {check["check_name"] for check in checks})

        statement = self.result["propagation_statement"]
        self.assertIs(statement["standing_propagation_posture_recorded"], True)
        self.assertIs(statement["selected_standing_surface_or_artifact_preserved"], True)
        self.assertIs(statement["requested_propagation_posture_preserved"], True)
        self.assertIs(statement["source_standing_basis_preserved"], True)
        self.assertIs(statement["selected_carriers_preserved"], True)
        self.assertIs(statement["carried_surface_or_packet_basis_preserved"], True)
        self.assertIs(
            statement["receipt_refusal_return_admission_posture_preserved"],
            True,
        )
        self.assertIs(statement["divergence_posture_preserved"], True)
        self.assertIs(statement["currentness_participation_posture_preserved"], True)
        self.assertIs(statement["relation_posture_preserved"], True)
        self.assertIs(statement["lifecycle_posture_preserved"], True)
        self.assertIs(statement["registry_persistence_posture_preserved"], True)
        self.assertIs(statement["lineage_preserved"], True)
        self.assertIs(statement["visible_refusal_preserved"], True)
        self.assertIs(statement["visible_divergence_preserved"], True)
        self.assertIs(statement["visible_corruption_preserved"], True)
        self.assertIs(statement["visible_staleness_preserved"], True)
        self.assert_no_collapse_statement(statement)

        non_meaning = self.result["propagation_non_meaning"]
        for key in NON_MEANING_KEYS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], True, key)

        remains_open = self.result["what_remains_open"]
        for key in OPEN_KEYS:
            self.assertIn(key, remains_open)
            self.assertIs(remains_open[key], True, key)

        summary = propagation.build_standing_propagation_summary(self.result)
        self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            "standing_propagation_v2_request_001",
            summary["standing_propagation_request_id"],
        )
        self.assertEqual(
            self.request["standing_propagation_question"],
            summary["standing_propagation_question"],
        )
        self.assertEqual(
            "RECORD_STANDING_PROPAGATION_POSTURE",
            summary["standing_propagation_intent"],
        )
        self.assertEqual(
            "CARRIED_STANDING_REGISTRY_REFERENCED",
            summary["requested_propagation_posture"],
        )
        self.assertEqual(
            "standing_surface_current_body_closure_001",
            summary["selected_standing_surface_or_artifact_id"],
        )
        self.assertIn("carrier_A_current_body_context", summary["selected_carrier_ids"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertIs(summary["standing_propagation_posture_recorded"], True)
        self.assert_v2_projection_true(self.result)
        self.assertIs(summary["currentness_participation_posture_preserved"], True)
        self.assertIs(summary["relation_posture_preserved"], True)
        self.assertIs(summary["visible_corruption_preserved"], True)
        self.assertIs(summary["visible_staleness_preserved"], True)
        self.assertIs(summary["no_source_currentness_authority_permission"], True)
        self.assertIs(summary["no_carrier_hierarchy"], True)
        self.assertIs(summary["no_current_winning_losing_carrier_collapse"], True)
        self.assertIs(summary["no_divergence_resolution"], True)
        self.assertIs(summary["no_evidence_erasure"], True)
        self.assertIs(summary["no_repair_by_overwrite"], True)
        self.assertIs(summary["no_distributed_standing"], True)
        self.assertIs(summary["no_sync_full_body_transfer_second_body"], True)
        self.assertIs(summary["no_continuation"], True)
        self.assertIs(summary["no_distributed_operation"], True)
        self.assertIs(summary["no_registry_reference_receipt_admission_standing"], True)
        self.assertIs(summary["no_latest_copy_file_currentness"], True)
        self.assertFalse(summary["key_non_claims"]["source_replaced"])
        self.assertFalse(summary["key_non_claims"]["distributed_standing_created"])
        self.assertEqual(
            "resolve_standing_propagation_boundary",
            summary["successor_of_module"],
        )

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(
        self,
    ) -> None:
        self.assert_all_required_non_claims_false(self.result)

        not_recorded = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=valid_request(
                intent="DO_NOT_RECORD_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual(
            "STANDING_PROPAGATION_POSTURE_NOT_RECORDED",
            not_recorded["outcome"],
        )
        self.assert_all_required_non_claims_false(not_recorded)

        blocked = propagation.resolve_standing_propagation_boundary()
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", blocked["outcome"])
        self.assert_all_required_non_claims_false(blocked)

    def test_supported_propagation_postures_record(self) -> None:
        self.assertEqual(set(SUPPORTED_POSTURES), propagation.SUPPORTED_PROPAGATION_POSTURES)
        for posture in SUPPORTED_POSTURES:
            with self.subTest(posture=posture):
                result = propagation.resolve_standing_propagation_boundary(
                    declared_propagation_request=valid_request(posture=posture)
                )
                self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", result["outcome"])

    def test_request_builder_helper_records_and_projects_nested_basis(self) -> None:
        basis = _standing_basis()
        request = propagation.build_declared_standing_propagation_request(
            "standing_propagation_v2_request_builder_001",
            "What posture does standing-related evidence have when carried across carriers?",
            _selected_surface(),
            "CARRIED_STANDING_REGISTRY_REFERENCED",
            basis,
            source_standing_basis=_source_basis(),
            selected_carriers=_selected_carriers(),
            related_carrier_evidence=_related_evidence(),
        )

        self.assertEqual(
            "standing_propagation_v2_request_builder_001",
            request["standing_propagation_request_id"],
        )
        self.assertEqual(
            "What posture does standing-related evidence have when carried across carriers?",
            request["standing_propagation_question"],
        )
        self.assertEqual(_selected_surface(), request["selected_standing_surface_or_artifact"])
        self.assertEqual(
            "CARRIED_STANDING_REGISTRY_REFERENCED",
            request["requested_propagation_posture"],
        )
        self.assertEqual(basis, request["standing_propagation_basis"])
        self.assertEqual(_source_basis(), request["source_standing_basis"])
        self.assertEqual(_selected_carriers(), request["selected_carriers"])
        self.assertEqual(_related_evidence(), request["related_carrier_evidence"])
        for key in propagation.REQUIRED_NON_CLAIMS:
            self.assertIs(request["declared_non_claims"][key], False, key)

        result = propagation.resolve_standing_propagation_boundary(request)
        self.assert_recorded(result)
        self.assert_v2_projection_true(result)

    def test_path_based_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            request_path = Path(tmpdir) / "standing_propagation_v2_request.json"
            _write_json(request_path, self.request)
            result = propagation.resolve_standing_propagation_boundary_from_path(
                request_path
            )

        self.assert_recorded(result)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(
            str(request_path),
            result["declared_standing_propagation_question"][
                "standing_propagation_request_path"
            ],
        )

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "standing_v2_result.json"
            written_path = propagation.write_standing_propagation_result(
                self.result,
                output_path=output_path,
            )
            self.assertEqual(output_path, written_path)
            self.assertTrue(written_path.exists())
            written = _read_json(written_path)

        self.assertEqual(TOP_LEVEL_SECTIONS, set(written))
        self.assertEqual("STANDING_PROPAGATION_POSTURE_RECORDED", written["outcome"])

    def test_default_output_path_non_overwrite_and_v2_root(self) -> None:
        self.assertNotEqual(propagation.STANDING_PROPAGATION_BOUNDARY_ROOT, V1_OUTPUT_ROOT)
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            with patch.object(propagation, "STANDING_PROPAGATION_BOUNDARY_ROOT", root):
                first = propagation.write_standing_propagation_result(self.result)
                second = propagation.write_standing_propagation_result(self.result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__standing_propagation_v2_result.json"))
            self.assertTrue(second.name.endswith(".json"))
            self.assertIn("__standing_propagation_v2_result_001", second.stem)

    def test_non_mutation_posture_and_v1_artifacts_untouched(self) -> None:
        request = valid_request()
        selected_before = copy.deepcopy(request["selected_standing_surface_or_artifact"])
        related_before = copy.deepcopy(request["related_carrier_evidence"])
        request_before = copy.deepcopy(request)
        v1_snapshot = {}
        if V1_OUTPUT_ROOT.exists():
            v1_snapshot = {
                path.relative_to(V1_OUTPUT_ROOT): path.stat().st_mtime_ns
                for path in V1_OUTPUT_ROOT.rglob("*")
                if path.is_file()
            }

        first = propagation.resolve_standing_propagation_boundary(request)
        second = propagation.resolve_standing_propagation_boundary(request)

        self.assertEqual(request_before, request)
        self.assertEqual(selected_before, request["selected_standing_surface_or_artifact"])
        self.assertEqual(related_before, request["related_carrier_evidence"])
        self.assert_recorded(first)
        self.assert_recorded(second)

        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            with patch.object(propagation, "STANDING_PROPAGATION_BOUNDARY_ROOT", root):
                written = propagation.write_standing_propagation_result(first)
            self.assertTrue(written.exists())
            self.assertEqual(root, written.parent)

        if V1_OUTPUT_ROOT.exists():
            after_snapshot = {
                path.relative_to(V1_OUTPUT_ROOT): path.stat().st_mtime_ns
                for path in V1_OUTPUT_ROOT.rglob("*")
                if path.is_file()
            }
            self.assertEqual(v1_snapshot, after_snapshot)

    def test_not_recorded_readable_request(self) -> None:
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=valid_request(
                intent="DO_NOT_RECORD_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual("STANDING_PROPAGATION_POSTURE_NOT_RECORDED", result["outcome"])
        statement = result["propagation_statement"]
        self.assertIs(statement["standing_propagation_posture_recorded"], False)
        self.assertTrue(statement["not_recorded_reason"])
        self.assert_no_collapse_statement(statement)

    def test_explicit_block_intent(self) -> None:
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=valid_request(
                intent="BLOCK_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", result["outcome"])
        self.assertEqual(
            "STANDING_PROPAGATION_REQUEST_EXPLICITLY_BLOCKED",
            result["block"]["block_code"],
        )
        self.assertIs(
            result["propagation_statement"]["standing_propagation_posture_recorded"],
            False,
        )

    def test_blocking_missing_and_malformed_requests(self) -> None:
        missing = propagation.resolve_standing_propagation_boundary()
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", missing["outcome"])
        self.assertEqual(
            "STANDING_PROPAGATION_QUESTION_UNDECLARED",
            missing["block"]["block_code"],
        )

        malformed = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=["not", "a", "mapping"]
        )
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", malformed["outcome"])
        self.assertEqual(
            "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
            malformed["block"]["block_code"],
        )

    def test_blocking_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_path = Path(tmpdir) / "missing.json"
            missing = propagation.resolve_standing_propagation_boundary_from_path(
                missing_path
            )
            self.assertEqual(
                "DECLARED_STANDING_PROPAGATION_REQUEST_UNREADABLE",
                missing["block"]["block_code"],
            )

            malformed_path = Path(tmpdir) / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = propagation.resolve_standing_propagation_boundary_from_path(
                malformed_path
            )
            self.assertEqual(
                "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
                malformed["block"]["block_code"],
            )

            array_path = Path(tmpdir) / "array.json"
            _write_json(array_path, [self.request])
            array_result = propagation.resolve_standing_propagation_boundary_from_path(
                array_path
            )
            self.assertEqual(
                "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
                array_result["block"]["block_code"],
            )

    def test_blocking_question_intent_and_posture(self) -> None:
        request = valid_request()
        request["standing_propagation_question"] = ""
        self.assert_block_code(request, "STANDING_PROPAGATION_QUESTION_UNDECLARED")

        self.assert_block_code(
            valid_request(standing_propagation_intent="UNSUPPORTED"),
            "STANDING_PROPAGATION_INTENT_UNSUPPORTED",
        )
        self.assert_block_code(
            valid_request(requested_propagation_posture="UNSUPPORTED"),
            "PROPAGATION_POSTURE_UNSUPPORTED",
        )

    def test_blocking_selected_surface_artifact(self) -> None:
        request = valid_request()
        request.pop("selected_standing_surface_or_artifact")
        self.assert_block_code(request, "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MISSING")

        self.assert_block_code(
            valid_request(selected_standing_surface_or_artifact=["not", "a", "mapping"]),
            "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MALFORMED",
        )
        self.assert_block_code(
            valid_request(
                selected_standing_surface_or_artifact={"outcome": "BODY_CONFORMANT"}
            ),
            "SELECTED_STANDING_SURFACE_OR_ARTIFACT_IDENTITY_MISSING",
        )

    def test_blocking_source_basis_carrier_identity_and_carried_packet_basis(
        self,
    ) -> None:
        request = valid_request(posture="SOURCE_STANDING_PRESERVED")
        _remove_nested(request, "source_standing_basis")
        basis = request.get("standing_propagation_basis")
        if isinstance(basis, dict):
            basis.pop("source_standing_preserved", None)
        self.assert_block_code(request, "SOURCE_STANDING_BASIS_MISSING")

        self.assert_block_code(
            valid_request(selected_carriers=[{"carrier_label": "Carrier without id"}]),
            "CARRIER_IDENTITY_MISSING",
        )

        request = valid_request(posture="STANDING_CARRIED_AS_EVIDENCE")
        _remove_nested(request, "carried_surface_or_packet_basis")
        self.assert_block_code(request, "CARRIED_SURFACE_OR_PACKET_BASIS_MISSING")

    def test_blocking_receipt_refusal_return_admission_posture_missing(self) -> None:
        request = valid_request(posture="CARRIED_STANDING_RECEIVED")
        _remove_nested(
            request,
            "receipt_posture",
            "refusal_posture",
            "return_posture",
            "admission_posture",
            "receipt_refusal_return_admission_posture",
        )
        self.assert_block_code(
            request,
            "RECEIPT_REFUSAL_RETURN_ADMISSION_POSTURE_MISSING",
        )

    def test_blocking_hidden_visibility_and_lineage(self) -> None:
        cases = [
            (
                "visible_divergence_basis",
                {"divergence_hidden": True},
                "PROPAGATION_HIDES_DIVERGENCE",
            ),
            (
                "visible_refusal_basis",
                {"refusal_hidden": True},
                "PROPAGATION_HIDES_REFUSAL",
            ),
            (
                "visible_corruption_basis",
                {"corruption_hidden": True},
                "PROPAGATION_HIDES_CORRUPTION",
            ),
            (
                "visible_staleness_basis",
                {"staleness_hidden": True},
                "PROPAGATION_HIDES_STALENESS",
            ),
        ]
        for field, value, block_code in cases:
            with self.subTest(block_code=block_code):
                self.assert_block_code(valid_request(**{field: value}), block_code)

        self.assert_block_code(
            valid_request(lineage_basis={"lineage_preserved": False}),
            "PROPAGATION_LINEAGE_MISSING",
        )

    def test_blocking_collapse_flags(self) -> None:
        cases = [
            ({"source_replaced": True}, "PROPAGATION_REPLACES_SOURCE"),
            ({"currentness_created": True}, "PROPAGATION_CREATES_CURRENTNESS"),
            ({"authority_created": True}, "PROPAGATION_CREATES_AUTHORITY"),
            ({"permission_created": True}, "PROPAGATION_CREATES_PERMISSION"),
            ({"carrier_hierarchy_created": True}, "PROPAGATION_CREATES_CARRIER_HIERARCHY"),
            ({"current_carrier_selected": True}, "PROPAGATION_SELECTS_CURRENT_CARRIER"),
            ({"winning_carrier_selected": True}, "PROPAGATION_SELECTS_WINNING_CARRIER"),
            ({"losing_carrier_invalidated": True}, "PROPAGATION_INVALIDATES_LOSING_CARRIER"),
            ({"divergence_resolved": True}, "PROPAGATION_RESOLVES_DIVERGENCE"),
            ({"evidence_erased": True}, "PROPAGATION_ERASES_EVIDENCE"),
            ({"repaired_by_overwrite": True}, "PROPAGATION_REPAIRS_BY_OVERWRITE"),
            ({"distributed_standing_created": True}, "PROPAGATION_CREATES_DISTRIBUTED_STANDING"),
            (
                {"repository_synchronization_authorized": True},
                "PROPAGATION_AUTHORIZES_REPOSITORY_SYNC",
            ),
            ({"full_body_transfer_authorized": True}, "PROPAGATION_AUTHORIZES_FULL_BODY_TRANSFER"),
            ({"second_body_created": True}, "PROPAGATION_CREATES_SECOND_BODY"),
            ({"continuation_authorized": True}, "PROPAGATION_AUTHORIZES_CONTINUATION"),
            (
                {"distributed_operation_authorized": True},
                "PROPAGATION_AUTHORIZES_DISTRIBUTED_OPERATION",
            ),
            (
                {"standing_propagation_made_registry_reference_standing": True},
                "PROPAGATION_MAKES_REGISTRY_REFERENCE_STANDING",
            ),
            (
                {"standing_propagation_made_receipt_standing": True},
                "PROPAGATION_MAKES_RECEIPT_STANDING",
            ),
            (
                {"standing_propagation_made_admission_standing": True},
                "PROPAGATION_MAKES_ADMISSION_STANDING",
            ),
            ({"latest_copy_currentness": True}, "LATEST_COPY_CURRENTNESS"),
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS"),
            ({"recency_fraud": True}, "LATEST_FILE_CURRENTNESS"),
            ({"mutation_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"merge_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        ]
        for updates, block_code in cases:
            with self.subTest(block_code=block_code):
                self.assert_block_code(valid_request(**updates), block_code)

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        request = valid_request()
        request["declared_non_claims"].pop("authority_created")
        self.assert_block_code(request, "NON_CLAIM_MISSING_OR_FLIPPED")

        request = valid_request()
        request["declared_non_claims"]["source_replaced"] = True
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )
        self.assertEqual("STANDING_PROPAGATION_POSTURE_BLOCKED", result["outcome"])
        self.assertIn(
            result["block"]["block_code"],
            {"PROPAGATION_REPLACES_SOURCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertIs(result["non_claims"]["source_replaced"], False)


if __name__ == "__main__":
    unittest.main()
