"""Tests for the cross-carrier currentness successor boundary resolver.

This suite audits body-side currentness accounting over plural carrier evidence
only. Carrier evidence may be accounted for without becoming currentness. No
carrier becomes current, no current/winning/losing carrier is selected, and the
resolver does not create distributed standing, synchronization, full body
transfer, continuation, or distributed operation.
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

import resolve_cross_carrier_currentness_successor_boundary as successor  # noqa: E402


TOP_LEVEL_SECTIONS = {
    "cross_carrier_currentness_successor_metadata",
    "declared_currentness_successor_question",
    "selected_body_current_posture",
    "selected_carrier_evidence",
    "prior_currentness_participation_basis",
    "lifecycle_basis",
    "registry_persistence_basis",
    "standing_propagation_basis",
    "carrier_continuity_turn_basis",
    "relation_conformance_closure_basis",
    "currentness_successor_posture",
    "evidence_accounting",
    "currentness_successor_checks",
    "currentness_successor_statement",
    "currentness_successor_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "cross_carrier_currentness_successor_summary",
}

OUTCOME_FAMILY = {
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED",
    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
}

SUPPORTED_POSTURES = (
    "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
    "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
    "CARRIER_EVIDENCE_CURRENTNESS_NOT_RELEVANT",
    "CARRIER_EVIDENCE_CURRENTNESS_EXCLUDED",
    "VISIBLE_DIVERGENCE_REQUIRES_CURRENTNESS_CAUTION",
    "VISIBLE_REFUSAL_REQUIRES_CURRENTNESS_CAUTION",
    "CURRENTNESS_SUCCESSOR_NOT_RECORDED",
    "CURRENTNESS_SUCCESSOR_BLOCKED",
)

EXPECTED_CHECK_NAMES = {
    "currentness_successor_question_declared",
    "currentness_successor_intent_supported",
    "body_current_posture_present",
    "carrier_evidence_present",
    "carrier_evidence_parseable",
    "carrier_evidence_identity_present",
    "carrier_evidence_outcome_present",
    "currentness_successor_posture_supported",
    "successor_basis_declared",
    "prior_participation_basis_preserved_where_supplied",
    "lifecycle_basis_preserved_where_supplied",
    "registry_persistence_basis_preserved_where_supplied",
    "standing_propagation_basis_preserved_where_supplied",
    "continuity_turn_basis_preserved_where_supplied",
    "relation_conformance_closure_basis_preserved_where_supplied",
    "evidence_accounting_preserved",
    "visible_refusal_preserved",
    "visible_divergence_preserved",
    "blocked_attempts_preserved",
    "projection_mismatch_preserved",
    "detailed_basis_distinguishable_from_summary",
    "summary_does_not_override_detailed_basis",
    "no_carrier_currentness",
    "no_current_carrier_selected",
    "no_winning_carrier_selected",
    "no_losing_carrier_invalidated",
    "no_source_replacement",
    "no_authority",
    "no_permission",
    "no_carrier_hierarchy",
    "no_divergence_resolution",
    "no_evidence_erasure",
    "no_distributed_standing",
    "no_repository_synchronization",
    "no_full_body_transfer",
    "no_second_body",
    "no_continuation",
    "no_distributed_operation",
    "no_latest_file_currentness",
    "no_latest_turn_currentness",
    "no_majority_or_success_count_currentness",
    "no_registry_lifecycle_propagation_or_turn_currentness",
    "no_mutation_replay_or_merge",
    "non_claims_remain_false",
}

NON_MEANING_KEYS = {
    "does_not_mean_carrier_currentness",
    "does_not_mean_current_carrier_selected",
    "does_not_mean_winning_carrier_selected",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_distributed_standing",
    "does_not_mean_distributed_currentness",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_carrier_priority",
    "does_not_mean_carrier_sovereignty",
    "does_not_mean_divergence_resolved",
    "does_not_mean_refusal_erased",
    "does_not_mean_evidence_erased",
    "does_not_mean_standing_on_carrier",
    "does_not_mean_registry_currentness",
    "does_not_mean_lifecycle_currentness",
    "does_not_mean_propagation_currentness",
    "does_not_mean_continuity_turn_currentness",
    "does_not_mean_latest_file_currentness",
    "does_not_mean_latest_turn_currentness",
    "does_not_mean_majority_currentness",
    "does_not_mean_success_count_currentness",
    "does_not_mean_availability_currentness",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_continuation",
    "does_not_mean_distributed_operation",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
}

OPEN_KEYS = {
    "cross_carrier_currentness_successor_implementation_refinement",
    "divergence_consequence_law",
    "distributed_standing_boundary",
    "distributed_standing",
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_implementation_beyond_boundary_recording",
    "carrier_continuity_turn_implementation_refinement",
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
    claims = copy.deepcopy(successor.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _body_posture(**updates: object) -> dict[str, object]:
    posture: dict[str, object] = {
        "body_current_posture_id": "current_self_orientation_v8__current_body_conformance_v3__v3_closure",
        "body_current_posture_outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
        "body_current_posture": "body_side_current_posture",
        "held_by_carrier": False,
        "selects_current_carrier": False,
    }
    posture.update(updates)
    return posture


def _carrier_evidence() -> list[dict[str, object]]:
    return [
        {
            "carrier_evidence_id": "carrier_b_successful_receipt_evidence",
            "carrier_id": "carrier_B_receiving_context",
            "evidence_class": "physical_receipt_evidence",
            "evidence_role": "successful_receipt",
            "evidence_outcome": "CARRIED_SURFACE_RECEIVED",
        },
        {
            "carrier_evidence_id": "carrier_c_blocked_receipt_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "physical_receipt_attempt",
            "evidence_role": "blocked_refusal_evidence",
            "evidence_outcome": "BLOCKED",
        },
        {
            "carrier_evidence_id": "carrier_b_c_visible_divergence_evidence",
            "carrier_id": "carrier_B__carrier_C",
            "evidence_class": "visible_divergence_evidence",
            "evidence_role": "bc_divergence",
            "evidence_outcome": "CARRIER_DIVERGENCE_RECORDED",
        },
        {
            "carrier_evidence_id": "carrier_c_currentness_participation_evidence",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "currentness_participation_evidence",
            "evidence_role": "participation_only",
            "evidence_outcome": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
        },
        {
            "carrier_evidence_id": "carrier_c_lifecycle_refused_or_blocked",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "carrier_lifecycle_evidence",
            "evidence_role": "lifecycle_basis",
            "evidence_outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
            "lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
        },
        {
            "carrier_evidence_id": "carrier_c_registry_persistence_v2_reference",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "registry_persistence_reference",
            "evidence_role": "reference_locator_only",
            "evidence_outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
        },
        {
            "carrier_evidence_id": "standing_propagation_v2_reference",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "standing_propagation_boundary_v2_result",
            "evidence_role": "carried_posture_only",
            "evidence_outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
        },
        {
            "carrier_evidence_id": "carrier_continuity_turn_v2_reference",
            "carrier_id": "carrier_C_additional_physical_candidate",
            "evidence_class": "carrier_continuity_turn_boundary_v2_result",
            "evidence_role": "turn_lineage_projection_correctness_only",
            "evidence_outcome": "CARRIER_CONTINUITY_TURN_RECORDED",
        },
    ]


def _successor_basis(**updates: object) -> dict[str, object]:
    basis: dict[str, object] = {
        "id": "cross_carrier_currentness_successor_basis_001",
        "basis_statement": "Body-side current posture accounts for plural carrier evidence without making any carrier current.",
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "blocked_attempts_preserved": True,
        "projection_mismatch_visible": True,
        "detailed_basis_distinguished_from_summary": True,
        "summary_overrode_detailed_basis": False,
        "carrier_currentness_created": False,
        "current_carrier_selected": False,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "detailed_basis_reference": "currentness_successor_basis.detailed",
        "summary_projection_reference": "currentness_successor_summary",
    }
    basis.update(updates)
    return basis


def _prior_participation_basis() -> dict[str, object]:
    return {
        "id": "carrier_c_currentness_participation_basis",
        "carrier_id": "carrier_C_additional_physical_candidate",
        "participation_posture": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
        "participation_remains_participation": True,
        "eligibility_does_not_force_accounting": True,
        "exclusion_does_not_erase_evidence": True,
    }


def _lifecycle_basis() -> dict[str, object]:
    return {
        "id": "carrier_c_lifecycle_basis",
        "carrier_id": "carrier_C_additional_physical_candidate",
        "lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
        "lifecycle_may_inform_caution_relevance_or_exclusion": True,
        "lifecycle_status_currentness": False,
        "active_carrier_is_not_current_carrier": True,
        "refused_blocked_carrier_is_not_invalid_by_default": True,
    }


def _registry_basis() -> dict[str, object]:
    return {
        "id": "carrier_c_registry_persistence_v2_basis",
        "registry_reference_id": "carrier_c_registry_persistence_v2_reference",
        "registry_presence_is_not_currentness": True,
        "latest_registry_reference_currentness": False,
        "registry_completeness_currentness": False,
        "registry_decides_currentness": False,
        "registry_selects_current_carrier": False,
    }


def _standing_basis() -> dict[str, object]:
    return {
        "id": "standing_propagation_v2_basis",
        "standing_propagation_posture": "CARRIED_STANDING_REGISTRY_REFERENCED",
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "receipt_refusal_return_admission_posture_preserved": True,
        "standing_propagation_currentness": False,
        "registry_reference_is_not_standing_or_currentness": True,
        "receipt_admission_registry_reference_are_not_standing_or_currentness": True,
    }


def _continuity_basis() -> dict[str, object]:
    return {
        "id": "carrier_continuity_turn_v2_basis",
        "turn_kind": "PROJECTION_SUCCESSOR_TURN",
        "projection_mismatch_visible": True,
        "blocked_attempts_preserved": True,
        "refusal_preserved": True,
        "divergence_preserved": True,
        "detailed_basis_distinguished_from_summary": True,
        "continuity_turn_currentness": False,
        "latest_turn_currentness": False,
        "projection_successor_created_currentness": False,
    }


def _relation_basis() -> dict[str, object]:
    return {
        "id": "carrier_b_c_relation_conformance_closure_basis",
        "relation_basis_id": "carrier_b_c_divergence_bounded_relation",
        "conformance_basis_id": "carrier_b_c_relation_conformance",
        "closure_basis_id": "carrier_b_c_relation_conformance_closure",
        "relation_conformance_closure_basis_only": True,
        "relation_decides_currentness": False,
        "relation_selects_current_carrier": False,
        "relation_selects_winning_carrier": False,
        "relation_invalidates_losing_carrier": False,
    }


def _evidence_accounting() -> list[dict[str, object]]:
    return [
        {
            "carrier_evidence_id": "carrier_b_successful_receipt_evidence",
            "carrier_evidence_outcome": "CARRIED_SURFACE_RECEIVED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "successful_receipt_relevant_only_under_declared_basis": True,
            "evidence_remains_evidence": True,
        },
        {
            "carrier_evidence_id": "carrier_c_blocked_receipt_evidence",
            "carrier_evidence_outcome": "BLOCKED",
            "accounting_posture": "VISIBLE_REFUSAL_REQUIRES_CURRENTNESS_CAUTION",
            "blocked_receipt_caution_refusal_only_under_declared_basis": True,
            "refusal_preserved": True,
        },
        {
            "carrier_evidence_id": "carrier_b_c_visible_divergence_evidence",
            "carrier_evidence_outcome": "CARRIER_DIVERGENCE_RECORDED",
            "accounting_posture": "VISIBLE_DIVERGENCE_REQUIRES_CURRENTNESS_CAUTION",
            "divergence_requires_currentness_caution": True,
            "divergence_preserved": True,
        },
        {
            "carrier_evidence_id": "carrier_c_lifecycle_refused_or_blocked",
            "carrier_evidence_outcome": "CARRIER_LIFECYCLE_STATUS_RECORDED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "lifecycle_basis_only_not_currentness": True,
        },
        {
            "carrier_evidence_id": "carrier_c_registry_persistence_v2_reference",
            "carrier_evidence_outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "registry_reference_locator_only": True,
        },
        {
            "carrier_evidence_id": "standing_propagation_v2_reference",
            "carrier_evidence_outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "standing_propagation_carried_posture_only": True,
        },
        {
            "carrier_evidence_id": "carrier_continuity_turn_v2_reference",
            "carrier_evidence_outcome": "CARRIER_CONTINUITY_TURN_RECORDED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "continuity_turn_lineage_projection_correctness_only": True,
        },
        {
            "carrier_evidence_id": "carrier_b_c_relation_conformance_closure",
            "carrier_evidence_outcome": "CONFORMANCE_CLOSURE_RECORDED",
            "accounting_posture": "CARRIER_EVIDENCE_CURRENTNESS_RELEVANT",
            "relation_conformance_closure_bounded_coherence_only": True,
        },
    ]


def _valid_request(**updates: object) -> dict[str, object]:
    request: dict[str, object] = {
        "currentness_successor_request_id": "cross_carrier_currentness_successor_request_001",
        "currentness_successor_question": "How may body-side current posture account for plural carrier evidence without making a carrier current?",
        "currentness_successor_intent": "RECORD_CROSS_CARRIER_CURRENTNESS_SUCCESSOR",
        "selected_body_current_posture": _body_posture(),
        "selected_carrier_evidence": _carrier_evidence(),
        "requested_currentness_successor_posture": "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
        "currentness_successor_basis": _successor_basis(),
        "prior_currentness_participation_basis": _prior_participation_basis(),
        "lifecycle_basis": _lifecycle_basis(),
        "registry_persistence_basis": _registry_basis(),
        "standing_propagation_basis": _standing_basis(),
        "carrier_continuity_turn_basis": _continuity_basis(),
        "relation_conformance_closure_basis": _relation_basis(),
        "evidence_accounting": _evidence_accounting(),
        "visible_refusal_basis": {
            "id": "visible_refusal_basis",
            "visible_refusal_preserved": True,
        },
        "visible_divergence_basis": {
            "id": "visible_divergence_basis",
            "visible_divergence_preserved": True,
        },
        "blocked_attempt_basis": {
            "id": "blocked_attempt_basis",
            "blocked_attempts_preserved": True,
        },
        "projection_mismatch_basis": {
            "id": "projection_mismatch_basis",
            "projection_mismatch_visible": True,
        },
        "detailed_basis_reference": "currentness_successor_basis.detailed",
        "summary_projection_reference": "cross_carrier_currentness_successor_summary",
        "declared_non_claims": _non_claims(),
    }
    request.update(updates)
    return request


def _result(request: dict[str, object] | None = None) -> dict[str, object]:
    return successor.resolve_cross_carrier_currentness_successor_boundary(
        declared_currentness_successor_request=_valid_request()
        if request is None
        else request
    )


def _block_code(result: dict[str, object]) -> object:
    block = result["block"]
    assert isinstance(block, dict)
    return block.get("block_code") or block.get("code")


class CrossCarrierCurrentnessSuccessorBoundaryTests(unittest.TestCase):
    def test_successful_currentness_successor_recording(self) -> None:
        result = _result()

        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            result["outcome"],
        )
        self.assertIsNone(_block_code(result))
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            0,
            result["cross_carrier_currentness_successor_summary"][
                "failed_check_count"
            ],
        )

        statement = result["currentness_successor_statement"]
        self.assertTrue(statement["cross_carrier_currentness_successor_recorded"])
        self.assertTrue(statement["body_current_posture_preserved"])
        self.assertTrue(statement["selected_carrier_evidence_preserved"])
        self.assertTrue(statement["selected_carrier_evidence_identities_preserved"])
        self.assertTrue(statement["selected_carrier_evidence_outcomes_preserved"])
        self.assertTrue(statement["currentness_successor_posture_preserved"])
        self.assertTrue(statement["evidence_accounting_preserved"])
        self.assertTrue(statement["visible_refusal_preserved"])
        self.assertTrue(statement["visible_divergence_preserved"])
        self.assertTrue(statement["blocked_attempts_preserved"])
        self.assertTrue(statement["projection_mismatch_preserved"])
        self.assertTrue(statement["prior_currentness_participation_basis_preserved"])
        self.assertTrue(statement["lifecycle_basis_preserved"])
        self.assertTrue(statement["registry_persistence_basis_preserved"])
        self.assertTrue(statement["standing_propagation_basis_preserved"])
        self.assertTrue(statement["carrier_continuity_turn_basis_preserved"])
        self.assertTrue(statement["relation_conformance_closure_basis_preserved"])
        self.assertTrue(statement["detailed_basis_distinguished_from_summary"])
        self.assertFalse(statement["summary_overrode_detailed_basis"])
        self.assert_no_currentness_collapse(statement)

    def test_metadata(self) -> None:
        metadata = _result()["cross_carrier_currentness_successor_metadata"]
        for key in (
            "cross_carrier_currentness_successor_result_id",
            "cross_carrier_currentness_successor_result_type",
            "cross_carrier_currentness_successor_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual(
            "0.1.0",
            metadata["cross_carrier_currentness_successor_result_version"],
        )
        self.assertEqual(
            "resolve_cross_carrier_currentness_successor_boundary",
            metadata["resolver_module"],
        )

    def test_declared_currentness_successor_question(self) -> None:
        request = _valid_request()
        result = _result(request)
        question = result["declared_currentness_successor_question"]
        posture = result["currentness_successor_posture"]

        self.assertEqual(
            request["currentness_successor_request_id"],
            question["currentness_successor_request_id"],
        )
        self.assertEqual(
            request["currentness_successor_question"],
            question["currentness_successor_question"],
        )
        self.assertEqual(
            request["currentness_successor_intent"],
            question["currentness_successor_intent"],
        )
        self.assertEqual(
            request["requested_currentness_successor_posture"],
            posture["requested_currentness_successor_posture"],
        )
        self.assertEqual(
            request["declared_non_claims"],
            question["declared_non_claims"],
        )
        self.assertTrue(question["currentness_participation_is_not_currentness"])
        self.assertTrue(
            question["currentness_successor_is_not_distributed_standing"]
        )
        self.assertTrue(question["plural_carrier_evidence_is_not_majority_currentness"])
        self.assertTrue(question["successful_receipt_is_not_currentness"])
        self.assertTrue(question["blocked_receipt_is_not_exclusion_by_default"])
        self.assertTrue(question["registry_presence_is_not_currentness"])
        self.assertTrue(question["lifecycle_status_is_not_currentness"])
        self.assertTrue(question["standing_propagation_is_not_currentness"])
        self.assertTrue(question["continuity_turn_lineage_is_not_currentness"])

    def test_selected_body_current_posture(self) -> None:
        section = _result()["selected_body_current_posture"]
        raw = section["raw_selected_body_current_posture"]

        self.assertEqual(
            "current_self_orientation_v8__current_body_conformance_v3__v3_closure",
            section["selected_body_current_posture_id"],
        )
        self.assertEqual(
            "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
            section["selected_body_current_posture_outcome"],
        )
        self.assertTrue(section["body_current_posture_preserved"])
        self.assertTrue(section["body_current_posture_is_body_side"])
        self.assertTrue(section["body_current_posture_is_not_carrier_currentness"])
        self.assertFalse(raw["held_by_carrier"])
        self.assertFalse(raw["selects_current_carrier"])

    def test_selected_carrier_evidence(self) -> None:
        section = _result()["selected_carrier_evidence"]
        ids = set(section["selected_carrier_evidence_ids"])
        outcomes = set(section["selected_carrier_evidence_outcomes"])
        entries = section["selected_carrier_evidence_entries"]
        carrier_ids = {entry["carrier_id"] for entry in entries if "carrier_id" in entry}
        roles = {entry["evidence_role"] for entry in entries}

        self.assertIn("carrier_b_successful_receipt_evidence", ids)
        self.assertIn("carrier_c_blocked_receipt_evidence", ids)
        self.assertIn("carrier_b_c_visible_divergence_evidence", ids)
        self.assertIn("carrier_c_currentness_participation_evidence", ids)
        self.assertIn("carrier_c_lifecycle_refused_or_blocked", ids)
        self.assertIn("carrier_c_registry_persistence_v2_reference", ids)
        self.assertIn("standing_propagation_v2_reference", ids)
        self.assertIn("carrier_continuity_turn_v2_reference", ids)
        self.assertIn("CARRIED_SURFACE_RECEIVED", outcomes)
        self.assertIn("BLOCKED", outcomes)
        self.assertIn("CARRIER_DIVERGENCE_RECORDED", outcomes)
        self.assertIn("carrier_B_receiving_context", carrier_ids)
        self.assertIn("carrier_C_additional_physical_candidate", carrier_ids)
        self.assertIn("successful_receipt", roles)
        self.assertIn("blocked_refusal_evidence", roles)
        self.assertTrue(section["carrier_evidence_remains_evidence"])
        self.assertTrue(section["carrier_evidence_is_not_currentness"])
        self.assertTrue(section["carrier_evidence_does_not_select_carrier"])

    def test_basis_sections_preserve_non_currentness_context(self) -> None:
        result = _result()
        participation = result["prior_currentness_participation_basis"]
        lifecycle = result["lifecycle_basis"]
        registry = result["registry_persistence_basis"]
        standing = result["standing_propagation_basis"]
        continuity = result["carrier_continuity_turn_basis"]
        relation = result["relation_conformance_closure_basis"]

        self.assertTrue(
            participation["prior_currentness_participation_basis_preserved"]
        )
        self.assertTrue(
            participation["raw_prior_currentness_participation_basis"][
                "participation_remains_participation"
            ]
        )
        self.assertTrue(
            participation["raw_prior_currentness_participation_basis"][
                "eligibility_does_not_force_accounting"
            ]
        )
        self.assertTrue(
            participation["raw_prior_currentness_participation_basis"][
                "exclusion_does_not_erase_evidence"
            ]
        )

        self.assertEqual(
            "CARRIER_REFUSED_OR_BLOCKED",
            lifecycle["raw_lifecycle_basis"]["lifecycle_status"],
        )
        self.assertTrue(lifecycle["raw_lifecycle_basis"]["active_carrier_is_not_current_carrier"])
        self.assertTrue(
            lifecycle["raw_lifecycle_basis"][
                "refused_blocked_carrier_is_not_invalid_by_default"
            ]
        )
        self.assertFalse(lifecycle["raw_lifecycle_basis"]["lifecycle_status_currentness"])

        self.assertTrue(registry["raw_registry_persistence_basis"]["registry_presence_is_not_currentness"])
        self.assertFalse(registry["raw_registry_persistence_basis"]["latest_registry_reference_currentness"])
        self.assertFalse(registry["raw_registry_persistence_basis"]["registry_completeness_currentness"])
        self.assertFalse(registry["raw_registry_persistence_basis"]["registry_decides_currentness"])
        self.assertFalse(registry["raw_registry_persistence_basis"]["registry_selects_current_carrier"])

        self.assertTrue(standing["raw_standing_propagation_basis"]["visible_refusal_preserved"])
        self.assertTrue(standing["raw_standing_propagation_basis"]["visible_divergence_preserved"])
        self.assertTrue(
            standing["raw_standing_propagation_basis"][
                "receipt_refusal_return_admission_posture_preserved"
            ]
        )
        self.assertFalse(standing["raw_standing_propagation_basis"]["standing_propagation_currentness"])
        self.assertTrue(
            standing["raw_standing_propagation_basis"][
                "registry_reference_is_not_standing_or_currentness"
            ]
        )

        self.assertTrue(continuity["raw_carrier_continuity_turn_basis"]["projection_mismatch_visible"])
        self.assertTrue(continuity["raw_carrier_continuity_turn_basis"]["blocked_attempts_preserved"])
        self.assertTrue(continuity["raw_carrier_continuity_turn_basis"]["refusal_preserved"])
        self.assertTrue(continuity["raw_carrier_continuity_turn_basis"]["divergence_preserved"])
        self.assertTrue(
            continuity["raw_carrier_continuity_turn_basis"][
                "detailed_basis_distinguished_from_summary"
            ]
        )
        self.assertFalse(continuity["raw_carrier_continuity_turn_basis"]["latest_turn_currentness"])

        self.assertTrue(
            relation["raw_relation_conformance_closure_basis"][
                "relation_conformance_closure_basis_only"
            ]
        )
        self.assertFalse(relation["raw_relation_conformance_closure_basis"]["relation_decides_currentness"])
        self.assertFalse(relation["raw_relation_conformance_closure_basis"]["relation_selects_current_carrier"])
        self.assertFalse(relation["raw_relation_conformance_closure_basis"]["relation_selects_winning_carrier"])
        self.assertFalse(relation["raw_relation_conformance_closure_basis"]["relation_invalidates_losing_carrier"])

    def test_currentness_successor_posture_and_evidence_accounting(self) -> None:
        result = _result()
        posture = result["currentness_successor_posture"]
        accounting = result["evidence_accounting"]

        self.assertEqual(
            "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
            posture["requested_currentness_successor_posture"],
        )
        self.assertTrue(posture["currentness_successor_posture_supported"])
        self.assertTrue(posture["currentness_successor_posture_preserved"])
        self.assertTrue(posture["posture_is_body_side_accounting_not_carrier_currentness"])
        self.assertTrue(accounting["evidence_accounting_preserved"])
        self.assertEqual(
            result["selected_carrier_evidence"]["selected_carrier_evidence_ids"],
            accounting["selected_carrier_evidence_identities"],
        )
        self.assertEqual(
            result["selected_carrier_evidence"]["selected_carrier_evidence_outcomes"],
            accounting["selected_carrier_evidence_outcomes"],
        )
        self.assertTrue(accounting["carrier_b_successful_receipt_relevant_only_under_declared_basis"])
        self.assertTrue(accounting["carrier_c_blocked_receipt_caution_only_under_declared_basis"])
        self.assertTrue(accounting["bc_divergence_may_require_currentness_caution"])
        self.assertTrue(accounting["lifecycle_status_may_inform_but_not_decide_currentness"])
        self.assertTrue(accounting["registry_persistence_may_locate_but_not_decide_currentness"])
        self.assertTrue(accounting["standing_propagation_may_preserve_posture_but_not_decide_currentness"])
        self.assertTrue(accounting["continuity_turn_may_preserve_lineage_but_not_decide_currentness"])
        self.assertTrue(accounting["relation_conformance_closure_may_preserve_coherence_but_not_decide_currentness"])
        self.assertTrue(accounting["no_majority_success_count_latest_currentness"])

    def test_currentness_successor_checks(self) -> None:
        checks = _result()["currentness_successor_checks"]
        names = {check["check_name"] for check in checks}

        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(names))
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertTrue(check["passed"], check)
            self.assertIsNone(check["block_code"])

    def test_currentness_successor_non_meaning_and_open_surfaces(self) -> None:
        result = _result()
        non_meaning = result["currentness_successor_non_meaning"]
        remains_open = result["what_remains_open"]

        for key in NON_MEANING_KEYS:
            self.assertTrue(non_meaning[key], key)
        for key in OPEN_KEYS:
            self.assertTrue(remains_open[key], key)
        self.assertTrue(remains_open["open_means_not_scheduled"])
        self.assertTrue(remains_open["open_means_not_authorized"])
        self.assertTrue(remains_open["open_means_not_executed"])

    def test_summary_helper(self) -> None:
        result = _result()
        summary = successor.build_cross_carrier_currentness_successor_summary(result)

        self.assertEqual(result["outcome"], summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            "cross_carrier_currentness_successor_request_001",
            summary["currentness_successor_request_id"],
        )
        self.assertEqual(
            "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
            summary["requested_currentness_successor_posture"],
        )
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertTrue(summary["cross_carrier_currentness_successor_recorded"])
        self.assertTrue(summary["evidence_accounting_preserved"])
        self.assertTrue(summary["visible_refusal_preserved"])
        self.assertTrue(summary["visible_divergence_preserved"])
        self.assertTrue(summary["blocked_attempts_preserved"])
        self.assertTrue(summary["projection_mismatch_preserved"])
        self.assertTrue(summary["prior_currentness_participation_basis_preserved"])
        self.assertTrue(summary["lifecycle_basis_preserved"])
        self.assertTrue(summary["registry_persistence_basis_preserved"])
        self.assertTrue(summary["standing_propagation_basis_preserved"])
        self.assertTrue(summary["carrier_continuity_turn_basis_preserved"])
        self.assertTrue(summary["relation_conformance_closure_basis_preserved"])
        self.assertTrue(summary["detailed_basis_distinguished_from_summary"])
        self.assertFalse(summary["summary_overrode_detailed_basis"])
        self.assertFalse(summary["carrier_currentness_created"])
        self.assertFalse(summary["current_carrier_selected"])
        self.assertFalse(summary["winning_carrier_selected"])
        self.assertFalse(summary["losing_carrier_invalidated"])
        self.assertTrue(summary["no_source_currentness_authority_permission"])
        self.assertTrue(summary["no_carrier_hierarchy"])
        self.assertTrue(summary["no_divergence_resolution"])
        self.assertTrue(summary["no_evidence_erasure"])
        self.assertTrue(summary["no_distributed_standing"])
        self.assertTrue(summary["no_sync_full_body_transfer_second_body"])
        self.assertTrue(summary["no_continuation"])
        self.assertTrue(summary["no_distributed_operation"])
        self.assertTrue(summary["no_latest_file_turn_currentness"])
        self.assertTrue(summary["no_majority_success_count_currentness"])
        for key, expected in summary["key_non_claims"].items():
            self.assertFalse(expected, key)

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        recorded = _result()
        not_recorded = _result(
            _valid_request(
                currentness_successor_intent="DO_NOT_RECORD_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
            )
        )
        blocked = successor.resolve_cross_carrier_currentness_successor_boundary()

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            recorded["outcome"],
        )
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED",
            not_recorded["outcome"],
        )
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            blocked["outcome"],
        )
        for result in (recorded, not_recorded, blocked):
            for key in successor.REQUIRED_NON_CLAIMS:
                self.assertIn(key, result["non_claims"])
                self.assertFalse(result["non_claims"][key], key)

    def test_supported_currentness_successor_postures_record(self) -> None:
        for posture in SUPPORTED_POSTURES:
            with self.subTest(posture=posture):
                request = _valid_request(requested_currentness_successor_posture=posture)
                result = _result(request)
                self.assertEqual(
                    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
                    result["outcome"],
                )
                self.assertEqual(
                    posture,
                    result["currentness_successor_posture"][
                        "requested_currentness_successor_posture"
                    ],
                )

    def test_request_builder_helper(self) -> None:
        request = successor.build_declared_cross_carrier_currentness_successor_request(
            "helper_request_001",
            "How may body-side current posture account for plural carrier evidence without making a carrier current?",
            _body_posture(),
            _carrier_evidence(),
            "BODY_CURRENT_POSTURE_ACCOUNTED_FOR_CARRIER_EVIDENCE",
            _successor_basis(),
            prior_currentness_participation_basis=_prior_participation_basis(),
            lifecycle_basis=_lifecycle_basis(),
            registry_persistence_basis=_registry_basis(),
            standing_propagation_basis=_standing_basis(),
            carrier_continuity_turn_basis=_continuity_basis(),
            relation_conformance_closure_basis=_relation_basis(),
            evidence_accounting=_evidence_accounting(),
        )

        self.assertEqual("helper_request_001", request["currentness_successor_request_id"])
        self.assertEqual(_body_posture(), request["selected_body_current_posture"])
        self.assertEqual(_carrier_evidence(), request["selected_carrier_evidence"])
        self.assertEqual(_successor_basis(), request["currentness_successor_basis"])
        self.assertEqual(_prior_participation_basis(), request["prior_currentness_participation_basis"])
        self.assertEqual(_lifecycle_basis(), request["lifecycle_basis"])
        self.assertEqual(_registry_basis(), request["registry_persistence_basis"])
        self.assertEqual(_standing_basis(), request["standing_propagation_basis"])
        self.assertEqual(_continuity_basis(), request["carrier_continuity_turn_basis"])
        self.assertEqual(_relation_basis(), request["relation_conformance_closure_basis"])
        self.assertEqual(_evidence_accounting(), request["evidence_accounting"])
        for key in successor.REQUIRED_NON_CLAIMS:
            self.assertFalse(request["declared_non_claims"][key], key)

        result = _result(request)
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            result["outcome"],
        )

    def test_path_based_resolution(self) -> None:
        request = _valid_request()
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "request.json"
            _write_json(path, request)

            from_path = successor.resolve_cross_carrier_currentness_successor_boundary_from_path(path)
            from_mapping = _result(request)

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            from_path["outcome"],
        )
        self.assertEqual(set(from_mapping), set(from_path))
        self.assertTrue(
            from_path["declared_currentness_successor_question"]["request_path"]
        )

    def test_write_behavior(self) -> None:
        result = _result()
        with tempfile.TemporaryDirectory() as tmpdir:
            output_path = Path(tmpdir) / "nested" / "result.json"
            written_path = successor.write_cross_carrier_currentness_successor_result(
                result,
                output_path,
            )
            loaded = _read_json(written_path)

        self.assertEqual(output_path, written_path)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(loaded))
        self.assertEqual(result["outcome"], loaded["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = _result()
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir) / "currentness_successor_root"
            with patch.object(
                successor,
                "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BOUNDARY_ROOT",
                root,
            ):
                first = successor.write_cross_carrier_currentness_successor_result(result)
                second = successor.write_cross_carrier_currentness_successor_result(result)

            self.assertEqual(root, first.parent)
            self.assertEqual(root, second.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__cross_carrier_currentness_successor_result.json"))
            self.assertTrue(second.name.endswith("_001.json"))
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        request = _valid_request()
        request_before = copy.deepcopy(request)
        body_before = copy.deepcopy(request["selected_body_current_posture"])
        evidence_before = copy.deepcopy(request["selected_carrier_evidence"])
        basis_before = {
            key: copy.deepcopy(request[key])
            for key in (
                "currentness_successor_basis",
                "prior_currentness_participation_basis",
                "lifecycle_basis",
                "registry_persistence_basis",
                "standing_propagation_basis",
                "carrier_continuity_turn_basis",
                "relation_conformance_closure_basis",
            )
        }

        first = _result(request)
        second = _result(request)

        self.assertEqual(request_before, request)
        self.assertEqual(body_before, request["selected_body_current_posture"])
        self.assertEqual(evidence_before, request["selected_carrier_evidence"])
        for key, value in basis_before.items():
            self.assertEqual(value, request[key])
        self.assertEqual(first["outcome"], second["outcome"])

        with tempfile.TemporaryDirectory() as tmpdir:
            target = Path(tmpdir) / "result.json"
            successor.write_cross_carrier_currentness_successor_result(first, target)
            self.assertTrue(target.exists())
            self.assertEqual([target], list(Path(tmpdir).iterdir()))

    def test_not_recorded_readable_request(self) -> None:
        result = _result(
            _valid_request(
                currentness_successor_intent="DO_NOT_RECORD_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
            )
        )
        statement = result["currentness_successor_statement"]

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_NOT_RECORDED",
            result["outcome"],
        )
        self.assertFalse(statement["cross_carrier_currentness_successor_recorded"])
        self.assertTrue(statement["not_recorded_reason"])
        self.assert_no_currentness_collapse(statement)

    def test_explicit_block_intent(self) -> None:
        result = _result(
            _valid_request(
                currentness_successor_intent="BLOCK_CROSS_CARRIER_CURRENTNESS_SUCCESSOR"
            )
        )

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            result["outcome"],
        )
        self.assertEqual(
            "CURRENTNESS_SUCCESSOR_REQUEST_EXPLICITLY_BLOCKED",
            _block_code(result),
        )
        self.assertFalse(
            result["currentness_successor_statement"][
                "cross_carrier_currentness_successor_recorded"
            ]
        )

    def test_missing_and_malformed_request_block(self) -> None:
        missing = successor.resolve_cross_carrier_currentness_successor_boundary()
        malformed = successor.resolve_cross_carrier_currentness_successor_boundary(
            declared_currentness_successor_request=["not", "a", "mapping"]
        )

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            missing["outcome"],
        )
        self.assertEqual("CURRENTNESS_SUCCESSOR_QUESTION_UNDECLARED", _block_code(missing))
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            malformed["outcome"],
        )
        self.assertEqual(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            _block_code(malformed),
        )

    def test_path_unreadable_and_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            missing = Path(tmpdir) / "missing.json"
            malformed = Path(tmpdir) / "malformed.json"
            array = Path(tmpdir) / "array.json"
            malformed.write_text("{not json", encoding="utf-8")
            array.write_text("[]", encoding="utf-8")

            missing_result = successor.resolve_cross_carrier_currentness_successor_boundary_from_path(missing)
            malformed_result = successor.resolve_cross_carrier_currentness_successor_boundary_from_path(malformed)
            array_result = successor.resolve_cross_carrier_currentness_successor_boundary_from_path(array)

        self.assertEqual(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_UNREADABLE",
            _block_code(missing_result),
        )
        self.assertEqual(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            _block_code(malformed_result),
        )
        self.assertEqual(
            "DECLARED_CURRENTNESS_SUCCESSOR_REQUEST_MALFORMED",
            _block_code(array_result),
        )

    def test_question_intent_and_posture_blocks(self) -> None:
        cases = (
            (
                {"currentness_successor_question": ""},
                "CURRENTNESS_SUCCESSOR_QUESTION_UNDECLARED",
            ),
            (
                {"currentness_successor_intent": "AUTHORIZE_CARRIER_CURRENTNESS"},
                "CURRENTNESS_SUCCESSOR_INTENT_UNSUPPORTED",
            ),
            (
                {"requested_currentness_successor_posture": "CARRIER_CURRENTNESS_CREATED"},
                "CURRENTNESS_SUCCESSOR_POSTURE_UNSUPPORTED",
            ),
        )
        self.assert_block_cases(cases)

    def test_body_current_posture_and_carrier_evidence_blocks(self) -> None:
        cases = (
            (
                {"selected_body_current_posture": None},
                "BODY_CURRENT_POSTURE_MISSING",
            ),
            (
                {"selected_carrier_evidence": None},
                "SELECTED_CARRIER_EVIDENCE_MISSING",
            ),
            (
                {"selected_carrier_evidence": "not parseable"},
                "SELECTED_CARRIER_EVIDENCE_MALFORMED",
            ),
            (
                {
                    "selected_carrier_evidence": [
                        {"evidence_outcome": "CARRIED_SURFACE_RECEIVED"}
                    ]
                },
                "SELECTED_CARRIER_EVIDENCE_IDENTITY_MISSING",
            ),
            (
                {"selected_carrier_evidence": [{"carrier_evidence_id": "evidence-x"}]},
                "SELECTED_CARRIER_EVIDENCE_OUTCOME_MISSING",
            ),
        )
        self.assert_block_cases(cases)

    def test_missing_basis_blocks(self) -> None:
        cases = (
            (
                {"currentness_successor_basis": None},
                "CURRENTNESS_SUCCESSOR_BASIS_MISSING",
            ),
            (
                {
                    "prior_currentness_participation_basis": None,
                    "prior_currentness_participation_basis_required": True,
                },
                "PRIOR_CURRENTNESS_PARTICIPATION_BASIS_MISSING",
            ),
            (
                {
                    "carrier_continuity_turn_basis": None,
                    "carrier_continuity_turn_basis_required": True,
                },
                "CARRIER_CONTINUITY_TURN_BASIS_MISSING",
            ),
            (
                {
                    "lifecycle_basis": None,
                    "lifecycle_basis_required": True,
                },
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            (
                {
                    "registry_persistence_basis": None,
                    "registry_persistence_basis_required": True,
                },
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
            (
                {
                    "standing_propagation_basis": None,
                    "standing_propagation_basis_required": True,
                },
                "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING",
            ),
        )
        self.assert_block_cases(cases)

    def test_visibility_and_summary_override_blocks(self) -> None:
        cases = (
            ({"visible_refusal_hidden": True}, "CURRENTNESS_SUCCESSOR_HIDES_REFUSAL"),
            (
                {"visible_divergence_hidden": True},
                "CURRENTNESS_SUCCESSOR_HIDES_DIVERGENCE",
            ),
            (
                {"blocked_attempt_hidden": True},
                "CURRENTNESS_SUCCESSOR_HIDES_BLOCKED_ATTEMPT",
            ),
            (
                {"projection_mismatch_hidden": True},
                "CURRENTNESS_SUCCESSOR_HIDES_PROJECTION_MISMATCH",
            ),
            (
                {"summary_overrode_detailed_basis": True},
                "SUMMARY_OVERWRITES_DETAILED_BASIS",
            ),
        )
        self.assert_block_cases(cases)

    def test_carrier_currentness_and_winner_loser_blocks(self) -> None:
        cases = (
            (
                {"carrier_currentness_created": True},
                "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_CURRENTNESS",
            ),
            (
                {"current_carrier_selected": True},
                "CURRENTNESS_SUCCESSOR_SELECTS_CURRENT_CARRIER",
            ),
            (
                {"winning_carrier_selected": True},
                "CURRENTNESS_SUCCESSOR_SELECTS_WINNING_CARRIER",
            ),
            (
                {"losing_carrier_invalidated": True},
                "CURRENTNESS_SUCCESSOR_INVALIDATES_LOSING_CARRIER",
            ),
        )
        self.assert_block_cases(cases)

    def test_source_authority_permission_hierarchy_blocks(self) -> None:
        cases = (
            ({"source_replaced": True}, "CURRENTNESS_SUCCESSOR_REPLACES_SOURCE"),
            ({"authority_created": True}, "CURRENTNESS_SUCCESSOR_CREATES_AUTHORITY"),
            ({"permission_created": True}, "CURRENTNESS_SUCCESSOR_CREATES_PERMISSION"),
            (
                {"currentness_successor_created_carrier_hierarchy": True},
                "CURRENTNESS_SUCCESSOR_CREATES_CARRIER_HIERARCHY",
            ),
        )
        self.assert_block_cases(cases)

    def test_divergence_resolution_and_evidence_erasure_blocks(self) -> None:
        cases = (
            (
                {"currentness_successor_resolved_divergence": True},
                "CURRENTNESS_SUCCESSOR_RESOLVES_DIVERGENCE",
            ),
            (
                {"currentness_successor_erased_evidence": True},
                "CURRENTNESS_SUCCESSOR_ERASES_EVIDENCE",
            ),
        )
        self.assert_block_cases(cases)

    def test_distributed_sync_transfer_second_body_blocks(self) -> None:
        cases = (
            (
                {"currentness_successor_created_distributed_standing": True},
                "CURRENTNESS_SUCCESSOR_CREATES_DISTRIBUTED_STANDING",
            ),
            (
                {"repository_synchronization_authorized": True},
                "CURRENTNESS_SUCCESSOR_AUTHORIZES_REPOSITORY_SYNC",
            ),
            (
                {"full_body_transfer_authorized": True},
                "CURRENTNESS_SUCCESSOR_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ({"second_body_created": True}, "CURRENTNESS_SUCCESSOR_CREATES_SECOND_BODY"),
        )
        self.assert_block_cases(cases)

    def test_continuation_and_distributed_operation_blocks(self) -> None:
        cases = (
            (
                {"continuation_authorized": True},
                "CURRENTNESS_SUCCESSOR_AUTHORIZES_CONTINUATION",
            ),
            (
                {"distributed_operation_authorized": True},
                "CURRENTNESS_SUCCESSOR_AUTHORIZES_DISTRIBUTED_OPERATION",
            ),
        )
        self.assert_block_cases(cases)

    def test_latest_majority_and_success_count_currentness_blocks(self) -> None:
        cases = (
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS"),
            ({"latest_turn_currentness": True}, "LATEST_TURN_CURRENTNESS"),
            (
                {"majority_carrier_currentness": True},
                "MAJORITY_OR_SUCCESS_COUNT_CURRENTNESS",
            ),
            (
                {"successful_receipt_count_currentness": True},
                "MAJORITY_OR_SUCCESS_COUNT_CURRENTNESS",
            ),
        )
        self.assert_block_cases(cases)

    def test_registry_lifecycle_propagation_turn_currentness_blocks(self) -> None:
        cases = (
            (
                {"registry_record_currentness": True},
                "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS",
            ),
            (
                {"lifecycle_status_currentness": True},
                "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS",
            ),
            (
                {"standing_propagation_currentness": True},
                "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS",
            ),
            (
                {"continuity_turn_currentness": True},
                "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CURRENTNESS",
            ),
        )
        self.assert_block_cases(cases)

    def test_mutation_replay_merge_blocks(self) -> None:
        cases = (
            ({"mutation_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"merge_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        )
        self.assert_block_cases(cases)

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing_claims = _non_claims()
        missing_claims.pop("carrier_currentness_created")
        missing = _result(_valid_request(declared_non_claims=missing_claims))

        flipped_claims = _non_claims(authority_created=True)
        flipped = _result(_valid_request(declared_non_claims=flipped_claims))

        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            missing["outcome"],
        )
        self.assertEqual("NON_CLAIM_MISSING_OR_FLIPPED", _block_code(missing))
        self.assertIn(
            "carrier_currentness_created",
            missing["non_claims"]["missing_required_non_claims"],
        )
        self.assertEqual(
            "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
            flipped["outcome"],
        )
        self.assertIn(
            _block_code(flipped),
            {
                "NON_CLAIM_MISSING_OR_FLIPPED",
                "CURRENTNESS_SUCCESSOR_CREATES_AUTHORITY",
            },
        )
        self.assertTrue(flipped["non_claims"]["authority_created"])

    def assert_block_cases(
        self,
        cases: tuple[tuple[dict[str, object], str], ...],
    ) -> None:
        for updates, expected_code in cases:
            with self.subTest(expected_code=expected_code, updates=updates):
                result = _result(_valid_request(**updates))
                self.assertEqual(
                    "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_BLOCKED",
                    result["outcome"],
                )
                self.assertEqual(expected_code, _block_code(result))
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assertFalse(
                    result["currentness_successor_statement"][
                        "cross_carrier_currentness_successor_recorded"
                    ]
                )

    def assert_no_currentness_collapse(self, statement: dict[str, object]) -> None:
        self.assertFalse(statement["carrier_currentness_created"])
        self.assertFalse(statement["currentness_created"])
        self.assertFalse(statement["current_carrier_selected"])
        self.assertFalse(statement["winning_carrier_selected"])
        self.assertFalse(statement["losing_carrier_invalidated"])
        self.assertFalse(statement["source_replaced"])
        self.assertFalse(statement["authority_created"])
        self.assertFalse(statement["permission_created"])
        self.assertFalse(statement["carrier_hierarchy_created"])
        self.assertFalse(statement["divergence_resolved"])
        self.assertFalse(statement["evidence_erased"])
        self.assertFalse(statement["distributed_standing_created"])
        self.assertFalse(statement["repository_synchronization_authorized"])
        self.assertFalse(statement["full_body_transfer_authorized"])
        self.assertFalse(statement["second_body_created"])
        self.assertFalse(statement["continuation_authorized"])
        self.assertFalse(statement["distributed_operation_authorized"])
        self.assertFalse(statement["latest_file_currentness"])
        self.assertFalse(statement["latest_turn_currentness"])
        self.assertFalse(statement["majority_carrier_currentness"])
        self.assertFalse(statement["successful_receipt_count_currentness"])
        self.assertFalse(statement["registry_record_currentness"])
        self.assertFalse(statement["lifecycle_status_currentness"])
        self.assertFalse(statement["standing_propagation_currentness"])
        self.assertFalse(statement["continuity_turn_currentness"])


if __name__ == "__main__":
    unittest.main()
