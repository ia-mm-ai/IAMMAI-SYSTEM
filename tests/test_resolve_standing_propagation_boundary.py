"""Tests for the bounded standing propagation boundary resolver.

These tests verify boundary recording only. They do not create distributed
standing, registry state, persistence state, synchronization, full body
transfer, continuation, or distributed operation.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

import resolve_standing_propagation_boundary as propagation  # noqa: E402


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


def _non_claims(**updates):
    claims = copy.deepcopy(propagation.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _selected_surface(**updates):
    surface = {
        "artifact_id": "standing_surface_current_body_closure_001",
        "artifact_type": "standing_surface",
        "artifact_class": "standing_related_artifact",
        "outcome": "BODY_CONFORMANT",
        "artifact_status": "standing_related_evidence",
    }
    surface.update(updates)
    return surface


def _source_basis():
    return {
        "source_standing_basis_id": "current_body_conformance_v3_closure_source_basis",
        "source_standing_surface_id": "standing_surface_current_body_closure_001",
        "source_standing_remains_upstream": True,
        "carrying_does_not_move_source_standing": True,
        "receipt_does_not_replace_source_standing": True,
        "return_admission_relation_lifecycle_registry_do_not_move_source_standing": True,
    }


def _selected_carriers():
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


def _carried_basis():
    return {
        "carried_surface_or_packet_id": "standing_related_packet_001",
        "source_basis": "current body closure remains upstream",
        "receipt_basis": "receipt/refusal evidence remains evidence",
        "refusal_basis": "blocked carrier posture remains visible",
        "carried_basis_does_not_create_currentness": True,
        "carried_basis_does_not_replace_source": True,
    }


def _related_evidence():
    return [
        {
            "evidence_id": "carrier_B_successful_receipt_evidence",
            "outcome": "CARRIED_SURFACE_RECEIVED",
            "carrier_id": "carrier_B_successful_receipt_context",
        },
        {
            "evidence_id": "carrier_C_blocked_receipt_evidence",
            "outcome": "RECEIPT_BLOCK",
            "carrier_id": "carrier_C_blocked_receipt_context",
        },
        {
            "evidence_id": "carrier_B_C_visible_divergence_evidence",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
        },
        {
            "evidence_id": "carrier_C_currentness_participation_evidence",
            "outcome": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
            "carrier_id": "carrier_C_blocked_receipt_context",
        },
        {
            "evidence_id": "carrier_C_lifecycle_refused_or_blocked_001",
            "outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
        },
        {
            "evidence_id": "carrier_C_registry_persistence_v2_reference_001",
            "outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            "carrier_id": "carrier_C_blocked_receipt_context",
        },
    ]


def _valid_request(
    posture="CARRIED_STANDING_REGISTRY_REFERENCED",
    intent="RECORD_STANDING_PROPAGATION_POSTURE",
    **updates,
):
    source_basis = _source_basis()
    selected_carriers = _selected_carriers()
    carried_basis = _carried_basis()
    receipt_posture = {"posture": "CARRIED_STANDING_RECEIVED", "preserved": True}
    refusal_posture = {
        "posture": "CARRIED_STANDING_REFUSED_OR_BLOCKED",
        "preserved": True,
    }
    return_posture = {"posture": "CARRIED_STANDING_RETURNED", "preserved": True}
    admission_posture = {
        "posture": "CARRIED_STANDING_ADMITTED_AS_EVIDENCE",
        "preserved": True,
    }
    divergence_posture = {
        "posture": "CARRIED_STANDING_DIVERGENCE_RECORDED",
        "preserved": True,
    }
    currentness_posture = {
        "posture": "CARRIED_STANDING_CURRENTNESS_PARTICIPATION_ELIGIBLE",
        "preserved": True,
        "participation_only": True,
    }
    relation_posture = {
        "posture": "CARRIED_STANDING_RELATION_CLOSED",
        "preserved": True,
    }
    lifecycle_posture = {
        "posture": "CARRIER_REFUSED_OR_BLOCKED",
        "preserved": True,
    }
    registry_posture = {
        "posture": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
        "preserved": True,
        "v2_lifecycle_reference_projection": True,
    }
    lineage_basis = {
        "lineage_preserved": True,
        "source_standing_remains_upstream": True,
    }
    visible_refusal_basis = {"refusal_preserved": True}
    visible_divergence_basis = {"divergence_preserved": True}
    visible_corruption_basis = {"corruption_preserved": True}
    visible_staleness_basis = {"staleness_preserved": True}
    propagation_basis = {
        "standing_propagation_basis_id": "standing_propagation_basis_001",
        "source_standing_basis": copy.deepcopy(source_basis),
        "receipt_posture": copy.deepcopy(receipt_posture),
        "refusal_posture": copy.deepcopy(refusal_posture),
        "return_posture": copy.deepcopy(return_posture),
        "admission_posture": copy.deepcopy(admission_posture),
        "divergence_posture": copy.deepcopy(divergence_posture),
        "currentness_participation_posture": copy.deepcopy(currentness_posture),
        "relation_posture": copy.deepcopy(relation_posture),
        "lifecycle_posture": copy.deepcopy(lifecycle_posture),
        "registry_persistence_posture": copy.deepcopy(registry_posture),
        "lineage_basis": copy.deepcopy(lineage_basis),
        "visible_refusal_basis": copy.deepcopy(visible_refusal_basis),
        "visible_divergence_basis": copy.deepcopy(visible_divergence_basis),
        "visible_corruption_basis": copy.deepcopy(visible_corruption_basis),
        "visible_staleness_basis": copy.deepcopy(visible_staleness_basis),
        "non_claims_preserved": True,
    }
    request = {
        "standing_propagation_request_id": "standing_propagation_request_001",
        "standing_propagation_question": (
            "What posture does standing-related evidence have when carried across carriers?"
        ),
        "standing_propagation_intent": intent,
        "selected_standing_surface_or_artifact": _selected_surface(),
        "requested_propagation_posture": posture,
        "source_standing_basis": source_basis,
        "selected_carriers": selected_carriers,
        "source_carrier": selected_carriers[0],
        "receiving_carrier": selected_carriers[2],
        "carried_surface_or_packet_basis": carried_basis,
        "receipt_posture": receipt_posture,
        "refusal_posture": refusal_posture,
        "return_posture": return_posture,
        "admission_posture": admission_posture,
        "divergence_posture": divergence_posture,
        "currentness_participation_posture": currentness_posture,
        "relation_posture": relation_posture,
        "lifecycle_posture": lifecycle_posture,
        "registry_persistence_posture": registry_posture,
        "related_carrier_evidence": _related_evidence(),
        "lineage_basis": lineage_basis,
        "visible_refusal_basis": visible_refusal_basis,
        "visible_divergence_basis": visible_divergence_basis,
        "visible_corruption_basis": visible_corruption_basis,
        "visible_staleness_basis": visible_staleness_basis,
        "standing_propagation_basis": propagation_basis,
        "declared_non_claims": _non_claims(),
    }
    request.update(updates)
    return request


def _remove_nested(request, *keys):
    for key in keys:
        request.pop(key, None)
        basis = request.get("standing_propagation_basis")
        if isinstance(basis, dict):
            basis.pop(key, None)


class StandingPropagationBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.request = _valid_request()
        self.result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=self.request
        )

    def assertRecorded(self, result):
        self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_RECORDED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["standing_propagation_summary"]["failed_check_count"], 0)
        self.assertTrue(
            result["propagation_statement"]["standing_propagation_posture_recorded"]
        )

    def assertBlocked(self, request, block_code):
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )
        self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertEqual(result["block"]["block_code"], block_code)
        self.assertFalse(
            result["propagation_statement"]["standing_propagation_posture_recorded"]
        )
        return result

    def assertAllRequiredNonClaimsFalse(self, result):
        for key in propagation.REQUIRED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)

    def test_successful_standing_propagation_posture_recording(self):
        self.assertIsInstance(self.result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(self.result))
        self.assertRecorded(self.result)

        statement = self.result["propagation_statement"]
        self.assertTrue(statement["selected_standing_surface_or_artifact_preserved"])
        self.assertTrue(statement["requested_propagation_posture_preserved"])
        self.assertTrue(statement["lineage_preserved"])
        self.assertFalse(statement["source_replaced"])
        self.assertFalse(statement["currentness_created"])
        self.assertFalse(statement["authority_created"])
        self.assertFalse(statement["permission_created"])
        self.assertFalse(statement["carrier_hierarchy_created"])
        self.assertFalse(statement["distributed_standing_created"])
        self.assertFalse(statement["repository_synchronization_authorized"])
        self.assertFalse(statement["full_body_transfer_authorized"])
        self.assertFalse(statement["second_body_created"])
        self.assertFalse(statement["continuation_authorized"])
        self.assertFalse(statement["distributed_operation_authorized"])
        self.assertFalse(statement["standing_propagation_made_registry_reference_standing"])
        self.assertFalse(statement["standing_propagation_made_receipt_standing"])
        self.assertFalse(statement["standing_propagation_made_admission_standing"])

    def test_metadata(self):
        metadata = self.result["standing_propagation_metadata"]
        self.assertTrue(metadata["standing_propagation_result_id"])
        self.assertTrue(metadata["standing_propagation_result_type"])
        self.assertEqual(metadata["standing_propagation_result_version"], "0.1.0")
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(metadata["resolver_module"], "resolve_standing_propagation_boundary")

    def test_declared_question_and_requested_posture(self):
        question = self.result["declared_standing_propagation_question"]
        self.assertEqual(
            question["standing_propagation_request_id"],
            self.request["standing_propagation_request_id"],
        )
        self.assertEqual(
            question["standing_propagation_question"],
            self.request["standing_propagation_question"],
        )
        self.assertEqual(
            question["standing_propagation_intent"],
            "RECORD_STANDING_PROPAGATION_POSTURE",
        )
        self.assertEqual(question["declared_non_claims"], self.request["declared_non_claims"])
        self.assertTrue(question["standing_propagation_is_not_distributed_standing"])
        self.assertTrue(question["standing_propagation_is_not_currentness"])
        self.assertTrue(question["standing_propagation_is_not_authority"])
        self.assertTrue(question["standing_propagation_does_not_replace_source"])
        self.assertTrue(
            question[
                "standing_propagation_does_not_authorize_sync_full_body_transfer_or_distributed_operation"
            ]
        )

        posture = self.result["standing_propagation_posture"]
        self.assertEqual(
            posture["requested_propagation_posture"],
            "CARRIED_STANDING_REGISTRY_REFERENCED",
        )
        self.assertTrue(posture["requested_propagation_posture_supported"])
        self.assertTrue(posture["requested_propagation_posture_preserved"])

    def test_selected_surface_source_carriers_and_carried_basis(self):
        selected = self.result["selected_standing_surface_or_artifact"]
        self.assertEqual(
            selected["selected_standing_surface_or_artifact_id"],
            "standing_surface_current_body_closure_001",
        )
        self.assertEqual(
            selected["raw_selected_standing_surface_or_artifact"]["outcome"],
            "BODY_CONFORMANT",
        )
        self.assertEqual(
            selected["raw_selected_standing_surface_or_artifact"]["artifact_type"],
            "standing_surface",
        )
        self.assertTrue(selected["selected_standing_surface_or_artifact_identity_present"])
        self.assertTrue(selected["selected_artifact_remains_evidence_or_reference"])
        self.assertTrue(selected["selected_artifact_does_not_create_currentness"])
        self.assertTrue(selected["selected_artifact_does_not_become_distributed_standing"])

        source = self.result["source_standing_basis"]
        self.assertTrue(source["source_standing_basis_declared"])
        self.assertTrue(source["source_standing_remains_upstream"])
        self.assertTrue(source["carrying_does_not_move_source_standing"])
        self.assertTrue(source["receipt_does_not_replace_source_standing"])
        self.assertTrue(source["admission_does_not_move_source_standing"])
        self.assertTrue(source["registry_reference_does_not_move_source_standing"])

        carriers = self.result["selected_carriers"]
        carrier_ids = {entry["carrier_id"] for entry in carriers["selected_carrier_entries"]}
        self.assertIn("carrier_A_current_body_context", carrier_ids)
        self.assertIn("carrier_B_successful_receipt_context", carrier_ids)
        self.assertIn("carrier_C_blocked_receipt_context", carrier_ids)
        self.assertTrue(carriers["carrier_identity_preserved_where_supplied"])
        self.assertTrue(carriers["carriers_do_not_become_currentness"])
        self.assertTrue(carriers["carriers_do_not_create_distributed_standing"])

        carried = self.result["carried_surface_or_packet_basis"]
        self.assertTrue(carried["carried_surface_or_packet_basis_declared"])
        self.assertEqual(
            carried["raw_carried_surface_or_packet_basis"]["carried_surface_or_packet_id"],
            "standing_related_packet_001",
        )
        self.assertTrue(carried["carried_surface_does_not_become_currentness"])
        self.assertTrue(carried["carried_surface_does_not_become_standing_on_receiver"])

    def test_standing_basis_and_related_evidence(self):
        basis = self.result["standing_propagation_basis"]
        self.assertTrue(basis["standing_propagation_basis_declared"])
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
        self.assertEqual(
            basis["raw_standing_propagation_basis"]["source_standing_basis"][
                "source_standing_basis_id"
            ],
            "current_body_conformance_v3_closure_source_basis",
        )
        self.assertTrue(basis["propagation_preserves_evidence_not_force"])
        self.assertTrue(basis["propagation_does_not_create_distributed_standing"])

        related = self.result["related_carrier_evidence"]
        self.assertTrue(related["related_carrier_evidence_preserved"])
        evidence_ids = {
            entry["evidence_id"] for entry in related["related_carrier_evidence_entries"]
        }
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

    def test_checks_statement_non_meaning_open_and_summary(self):
        checks = self.result["propagation_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertTrue(check["passed"], check)
        self.assertEqual(
            {check["check_name"] for check in checks},
            EXPECTED_CHECK_NAMES,
        )

        statement = self.result["propagation_statement"]
        self.assertTrue(statement["source_standing_basis_preserved"])
        self.assertTrue(statement["selected_carriers_preserved"])
        self.assertTrue(statement["carried_surface_or_packet_basis_preserved"])
        self.assertTrue(statement["receipt_refusal_return_admission_posture_preserved"])
        self.assertTrue(statement["divergence_posture_preserved"])
        self.assertTrue(statement["currentness_participation_posture_preserved"])
        self.assertTrue(statement["relation_posture_preserved"])
        self.assertTrue(statement["lifecycle_posture_preserved"])
        self.assertTrue(statement["registry_persistence_posture_preserved"])
        self.assertTrue(statement["visible_refusal_preserved"])
        self.assertTrue(statement["visible_divergence_preserved"])
        self.assertTrue(statement["visible_corruption_preserved"])
        self.assertTrue(statement["visible_staleness_preserved"])

        non_meaning = self.result["propagation_non_meaning"]
        for key in NON_MEANING_KEYS:
            self.assertIn(key, non_meaning)
            self.assertTrue(non_meaning[key], key)

        remains_open = self.result["what_remains_open"]
        for key in OPEN_KEYS:
            self.assertIn(key, remains_open)
            self.assertTrue(remains_open[key], key)

        summary = propagation.build_standing_propagation_summary(self.result)
        self.assertEqual(summary["outcome"], "STANDING_PROPAGATION_POSTURE_RECORDED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["standing_propagation_request_id"],
            "standing_propagation_request_001",
        )
        self.assertEqual(
            summary["standing_propagation_question"],
            self.request["standing_propagation_question"],
        )
        self.assertEqual(
            summary["standing_propagation_intent"],
            "RECORD_STANDING_PROPAGATION_POSTURE",
        )
        self.assertEqual(
            summary["requested_propagation_posture"],
            "CARRIED_STANDING_REGISTRY_REFERENCED",
        )
        self.assertEqual(
            summary["selected_standing_surface_or_artifact_id"],
            "standing_surface_current_body_closure_001",
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["standing_propagation_posture_recorded"])
        self.assertTrue(summary["lineage_preserved"])
        self.assertTrue(summary["source_standing_preserved"])
        self.assertTrue(summary["visible_refusal_preserved"])
        self.assertTrue(summary["visible_divergence_preserved"])
        self.assertTrue(summary["visible_corruption_preserved"])
        self.assertTrue(summary["visible_staleness_preserved"])
        self.assertTrue(summary["receipt_refusal_return_admission_posture_preserved"])
        self.assertTrue(summary["divergence_posture_preserved"])
        self.assertTrue(summary["currentness_participation_posture_preserved"])
        self.assertTrue(summary["relation_posture_preserved"])
        self.assertTrue(summary["lifecycle_posture_preserved"])
        self.assertTrue(summary["registry_persistence_posture_preserved"])
        self.assertTrue(summary["no_source_currentness_authority_permission"])
        self.assertTrue(summary["no_carrier_hierarchy"])
        self.assertTrue(summary["no_current_winning_losing_carrier_collapse"])
        self.assertTrue(summary["no_divergence_resolution"])
        self.assertTrue(summary["no_evidence_erasure"])
        self.assertTrue(summary["no_repair_by_overwrite"])
        self.assertTrue(summary["no_distributed_standing"])
        self.assertTrue(summary["no_sync_full_body_transfer_second_body"])
        self.assertTrue(summary["no_continuation"])
        self.assertTrue(summary["no_distributed_operation"])
        self.assertTrue(summary["no_registry_reference_receipt_admission_standing"])
        self.assertTrue(summary["no_latest_copy_file_currentness"])
        self.assertFalse(summary["key_non_claims"]["source_replaced"])
        self.assertFalse(summary["key_non_claims"]["distributed_standing_created"])

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self):
        self.assertAllRequiredNonClaimsFalse(self.result)

        not_recorded = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=_valid_request(
                intent="DO_NOT_RECORD_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual(not_recorded["outcome"], "STANDING_PROPAGATION_POSTURE_NOT_RECORDED")
        self.assertAllRequiredNonClaimsFalse(not_recorded)

        blocked = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=None
        )
        self.assertEqual(blocked["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertAllRequiredNonClaimsFalse(blocked)

    def test_supported_propagation_postures_record(self):
        self.assertEqual(set(SUPPORTED_POSTURES), set(propagation.SUPPORTED_PROPAGATION_POSTURES))
        for posture in SUPPORTED_POSTURES:
            with self.subTest(posture=posture):
                result = propagation.resolve_standing_propagation_boundary(
                    declared_propagation_request=_valid_request(posture=posture)
                )
                self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_RECORDED")

    def test_request_builder_helper_records(self):
        request = propagation.build_declared_standing_propagation_request(
            "standing_propagation_request_builder_001",
            "What posture does standing-related evidence have when carried across carriers?",
            _selected_surface(),
            "CARRIED_STANDING_RECEIVED",
            {
                "standing_propagation_basis_id": "builder_basis",
                "receipt_posture": {"posture": "CARRIED_STANDING_RECEIVED"},
            },
            source_standing_basis=_source_basis(),
            selected_carriers=_selected_carriers(),
            related_carrier_evidence=_related_evidence(),
        )
        request["carried_surface_or_packet_basis"] = _carried_basis()
        request["receipt_posture"] = {"posture": "CARRIED_STANDING_RECEIVED"}
        request["lineage_basis"] = {"lineage_preserved": True}

        self.assertEqual(
            request["standing_propagation_request_id"],
            "standing_propagation_request_builder_001",
        )
        self.assertEqual(
            request["standing_propagation_question"],
            "What posture does standing-related evidence have when carried across carriers?",
        )
        self.assertEqual(
            request["requested_propagation_posture"],
            "CARRIED_STANDING_RECEIVED",
        )
        self.assertEqual(request["selected_standing_surface_or_artifact"], _selected_surface())
        self.assertIn("standing_propagation_basis", request)
        self.assertIn("source_standing_basis", request)
        self.assertIn("selected_carriers", request)
        self.assertIn("related_carrier_evidence", request)
        for key in propagation.REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][key], key)

        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )
        self.assertRecorded(result)

    def test_path_based_resolution(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            request_path = Path(tmpdir) / "standing_propagation_request.json"
            request_path.write_text(json.dumps(self.request, indent=2), encoding="utf-8")

            result = propagation.resolve_standing_propagation_boundary_from_path(request_path)

        self.assertRecorded(result)
        self.assertEqual(set(result), TOP_LEVEL_SECTIONS)
        self.assertEqual(
            result["declared_standing_propagation_question"][
                "standing_propagation_request_path"
            ],
            str(request_path),
        )

    def test_write_behavior(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "standing_result.json"
            written_path = propagation.write_standing_propagation_result(
                self.result, output_path=output_path
            )
            self.assertEqual(written_path, output_path)
            self.assertTrue(written_path.exists())
            written = json.loads(written_path.read_text(encoding="utf-8"))

        self.assertEqual(set(written), TOP_LEVEL_SECTIONS)
        self.assertEqual(written["outcome"], "STANDING_PROPAGATION_POSTURE_RECORDED")

    def test_default_output_path_non_overwrite(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            with mock.patch.object(propagation, "STANDING_PROPAGATION_BOUNDARY_ROOT", root):
                first = propagation.write_standing_propagation_result(self.result)
                second = propagation.write_standing_propagation_result(self.result)

            self.assertEqual(first.parent, root)
            self.assertEqual(second.parent, root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__standing_propagation_result.json"))
            self.assertTrue(second.name.endswith(".json"))
            self.assertIn("__standing_propagation_result_001", second.stem)

    def test_non_mutation_posture(self):
        request = _valid_request()
        selected_before = copy.deepcopy(request["selected_standing_surface_or_artifact"])
        related_before = copy.deepcopy(request["related_carrier_evidence"])
        request_before = copy.deepcopy(request)

        first = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )
        second = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )

        self.assertEqual(request, request_before)
        self.assertEqual(request["selected_standing_surface_or_artifact"], selected_before)
        self.assertEqual(request["related_carrier_evidence"], related_before)
        self.assertRecorded(first)
        self.assertRecorded(second)

        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "additive_result.json"
            propagation.write_standing_propagation_result(first, output_path=output_path)
            self.assertTrue(output_path.exists())

    def test_not_recorded_readable_request(self):
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=_valid_request(
                intent="DO_NOT_RECORD_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_NOT_RECORDED")
        self.assertFalse(result["propagation_statement"]["standing_propagation_posture_recorded"])
        self.assertTrue(result["propagation_statement"]["not_recorded_reason"])
        self.assertFalse(result["propagation_statement"]["source_replaced"])
        self.assertFalse(result["propagation_statement"]["currentness_created"])
        self.assertFalse(result["propagation_statement"]["authority_created"])
        self.assertFalse(result["propagation_statement"]["permission_created"])
        self.assertFalse(result["propagation_statement"]["distributed_standing_created"])

    def test_explicit_block_intent(self):
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=_valid_request(
                intent="BLOCK_STANDING_PROPAGATION_POSTURE"
            )
        )
        self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertEqual(
            result["block"]["block_code"],
            "STANDING_PROPAGATION_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assertFalse(result["propagation_statement"]["standing_propagation_posture_recorded"])

    def test_blocking_missing_and_malformed_requests(self):
        missing = propagation.resolve_standing_propagation_boundary()
        self.assertEqual(missing["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertEqual(
            missing["block"]["block_code"],
            "STANDING_PROPAGATION_QUESTION_UNDECLARED",
        )

        malformed = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=["not", "a", "mapping"]
        )
        self.assertEqual(malformed["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertEqual(
            malformed["block"]["block_code"],
            "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED",
        )

    def test_blocking_path_unreadable_and_malformed(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            missing_path = Path(tmpdir) / "missing.json"
            missing = propagation.resolve_standing_propagation_boundary_from_path(missing_path)
            self.assertEqual(missing["block"]["block_code"], "DECLARED_STANDING_PROPAGATION_REQUEST_UNREADABLE")

            malformed_path = Path(tmpdir) / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = propagation.resolve_standing_propagation_boundary_from_path(
                malformed_path
            )
            self.assertEqual(malformed["block"]["block_code"], "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED")

            array_path = Path(tmpdir) / "array.json"
            array_path.write_text(json.dumps([self.request]), encoding="utf-8")
            array_result = propagation.resolve_standing_propagation_boundary_from_path(
                array_path
            )
            self.assertEqual(array_result["block"]["block_code"], "DECLARED_STANDING_PROPAGATION_REQUEST_MALFORMED")

    def test_blocking_question_intent_posture(self):
        request = _valid_request()
        request["standing_propagation_question"] = ""
        self.assertBlocked(request, "STANDING_PROPAGATION_QUESTION_UNDECLARED")

        request = _valid_request(standing_propagation_intent="UNSUPPORTED")
        self.assertBlocked(request, "STANDING_PROPAGATION_INTENT_UNSUPPORTED")

        request = _valid_request(requested_propagation_posture="UNSUPPORTED")
        self.assertBlocked(request, "PROPAGATION_POSTURE_UNSUPPORTED")

    def test_blocking_selected_surface_artifact(self):
        request = _valid_request()
        request.pop("selected_standing_surface_or_artifact")
        self.assertBlocked(request, "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MISSING")

        request = _valid_request(selected_standing_surface_or_artifact=["not", "a", "mapping"])
        self.assertBlocked(request, "SELECTED_STANDING_SURFACE_OR_ARTIFACT_MALFORMED")

        request = _valid_request(selected_standing_surface_or_artifact={"outcome": "BODY_CONFORMANT"})
        self.assertBlocked(request, "SELECTED_STANDING_SURFACE_OR_ARTIFACT_IDENTITY_MISSING")

    def test_blocking_basis_requirements(self):
        request = _valid_request(posture="SOURCE_STANDING_PRESERVED")
        _remove_nested(request, "source_standing_basis")
        self.assertBlocked(request, "SOURCE_STANDING_BASIS_MISSING")

        request = _valid_request(selected_carriers=[{"carrier_label": "Carrier without id"}])
        self.assertBlocked(request, "CARRIER_IDENTITY_MISSING")

        request = _valid_request(posture="STANDING_CARRIED_AS_EVIDENCE")
        _remove_nested(request, "carried_surface_or_packet_basis")
        self.assertBlocked(request, "CARRIED_SURFACE_OR_PACKET_BASIS_MISSING")

    def test_blocking_receipt_refusal_return_admission_missing(self):
        request = _valid_request(posture="CARRIED_STANDING_RECEIVED")
        _remove_nested(request, "receipt_posture")
        self.assertBlocked(request, "RECEIPT_REFUSAL_RETURN_ADMISSION_POSTURE_MISSING")

    def test_blocking_hidden_visibility_and_lineage(self):
        cases = [
            ("visible_divergence_basis", {"divergence_hidden": True}, "PROPAGATION_HIDES_DIVERGENCE"),
            ("visible_refusal_basis", {"refusal_hidden": True}, "PROPAGATION_HIDES_REFUSAL"),
            ("visible_corruption_basis", {"corruption_hidden": True}, "PROPAGATION_HIDES_CORRUPTION"),
            ("visible_staleness_basis", {"staleness_hidden": True}, "PROPAGATION_HIDES_STALENESS"),
        ]
        for field, value, block_code in cases:
            with self.subTest(block_code=block_code):
                request = _valid_request(**{field: value})
                self.assertBlocked(request, block_code)

        request = _valid_request(lineage_basis={"lineage_preserved": False})
        self.assertBlocked(request, "PROPAGATION_LINEAGE_MISSING")

    def test_blocking_collapse_flags(self):
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
            ({"repository_synchronization_authorized": True}, "PROPAGATION_AUTHORIZES_REPOSITORY_SYNC"),
            ({"full_body_transfer_authorized": True}, "PROPAGATION_AUTHORIZES_FULL_BODY_TRANSFER"),
            ({"second_body_created": True}, "PROPAGATION_CREATES_SECOND_BODY"),
            ({"continuation_authorized": True}, "PROPAGATION_AUTHORIZES_CONTINUATION"),
            ({"distributed_operation_authorized": True}, "PROPAGATION_AUTHORIZES_DISTRIBUTED_OPERATION"),
            ({"standing_propagation_made_registry_reference_standing": True}, "PROPAGATION_MAKES_REGISTRY_REFERENCE_STANDING"),
            ({"standing_propagation_made_receipt_standing": True}, "PROPAGATION_MAKES_RECEIPT_STANDING"),
            ({"standing_propagation_made_admission_standing": True}, "PROPAGATION_MAKES_ADMISSION_STANDING"),
            ({"latest_copy_currentness": True}, "LATEST_COPY_CURRENTNESS"),
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS"),
            ({"recency_fraud": True}, "LATEST_FILE_CURRENTNESS"),
            ({"mutation_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"merge_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        ]
        for updates, block_code in cases:
            with self.subTest(block_code=block_code):
                request = _valid_request(**updates)
                self.assertBlocked(request, block_code)

    def test_blocking_non_claim_missing_or_flipped(self):
        request = _valid_request()
        request["declared_non_claims"].pop("authority_created")
        self.assertBlocked(request, "NON_CLAIM_MISSING_OR_FLIPPED")

        request = _valid_request()
        request["declared_non_claims"]["source_replaced"] = True
        result = propagation.resolve_standing_propagation_boundary(
            declared_propagation_request=request
        )
        self.assertEqual(result["outcome"], "STANDING_PROPAGATION_POSTURE_BLOCKED")
        self.assertIn(
            result["block"]["block_code"],
            {"PROPAGATION_REPLACES_SOURCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertFalse(result["non_claims"]["source_replaced"])


if __name__ == "__main__":
    unittest.main()
