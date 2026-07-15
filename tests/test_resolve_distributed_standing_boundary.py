"""Bounded tests for the distributed standing boundary resolver.

These tests audit one surface only: distributed standing boundary posture. The
resolver may record bounded body-side posture, require more basis, exclude a
declared scope, require revalidation, or require separate review. It must not
execute distributed operation, synchronize repositories, transfer a full body,
create carrier currentness, select carrier winners or losers, resolve
divergence, create truth or action, or let prerequisite surfaces create
standing by themselves.
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

import resolve_distributed_standing_boundary as resolver  # noqa: E402


RECORDED = "DISTRIBUTED_STANDING_POSTURE_RECORDED"
NOT_RECORDED = "DISTRIBUTED_STANDING_POSTURE_NOT_RECORDED"
BLOCKED = "DISTRIBUTED_STANDING_POSTURE_BLOCKED"
REQUIRES_ADDITIONAL_BASIS = "DISTRIBUTED_STANDING_REQUIRES_ADDITIONAL_BASIS"
EXCLUDED_FOR_SCOPE = "DISTRIBUTED_STANDING_EXCLUDED_FOR_DECLARED_SCOPE"
REQUIRES_REVALIDATION = "DISTRIBUTED_STANDING_REQUIRES_REVALIDATION"
REQUIRES_SEPARATE_REVIEW = "DISTRIBUTED_STANDING_REQUIRES_SEPARATE_REVIEW"

OUTCOME_FAMILY = {
    RECORDED,
    NOT_RECORDED,
    BLOCKED,
    REQUIRES_ADDITIONAL_BASIS,
    EXCLUDED_FOR_SCOPE,
    REQUIRES_REVALIDATION,
    REQUIRES_SEPARATE_REVIEW,
}

TOP_LEVEL_SECTIONS = {
    "distributed_standing_metadata",
    "declared_distributed_standing_question",
    "selected_body_side_standing_posture",
    "selected_carrier_evidence",
    "source_body_lineage",
    "receipt_refusal_admission_basis",
    "divergence_basis",
    "divergence_consequence_basis",
    "currentness_successor_basis",
    "carrier_continuity_turn_basis",
    "standing_propagation_basis",
    "registry_persistence_basis",
    "lifecycle_basis",
    "relation_conformance_closure_basis",
    "current_body_conformance_v3_closure_basis",
    "distributed_standing_posture",
    "distributed_standing_checks",
    "distributed_standing_statement",
    "distributed_standing_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "distributed_standing_summary",
}

EXPECTED_CHECK_NAMES = {
    "distributed_standing_question_declared",
    "distributed_standing_intent_supported",
    "selected_body_side_standing_posture_present",
    "selected_carrier_evidence_present",
    "selected_carrier_evidence_parseable",
    "selected_carrier_evidence_identities_present",
    "selected_carrier_evidence_outcomes_present",
    "distributed_standing_posture_supported",
    "distributed_standing_basis_declared",
    "source_body_lineage_preserved",
    "receipt_refusal_admission_basis_preserved_where_required_or_supplied",
    "divergence_basis_preserved_where_required_or_supplied",
    "divergence_consequence_basis_preserved",
    "currentness_successor_basis_preserved",
    "continuity_turn_basis_preserved",
    "standing_propagation_basis_preserved",
    "registry_persistence_basis_preserved",
    "lifecycle_basis_preserved",
    "relation_conformance_closure_basis_preserved_where_required_or_supplied",
    "current_body_conformance_v3_closure_basis_preserved",
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
    "no_truth",
    "no_action",
    "no_divergence_resolution",
    "no_evidence_erasure",
    "no_repository_sync",
    "no_full_body_transfer",
    "no_second_body",
    "no_continuation",
    "no_distributed_operation",
    "no_latest_file_turn_standing",
    "no_majority_success_count_standing",
    "no_registry_lifecycle_propagation_turn_currentness_or_consequence_standing",
    "no_mutation_replay_merge",
    "non_claims_remain_false",
}

FALSE_STATEMENT_KEYS = {
    "summary_overrode_detailed_basis",
    "carrier_currentness_created",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replaced",
    "currentness_created",
    "authority_created",
    "permission_created",
    "truth_created",
    "action_authorized",
    "divergence_resolved",
    "evidence_erased",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "latest_file_standing",
    "latest_turn_standing",
    "majority_carrier_standing",
    "successful_receipt_count_standing",
}

NON_MEANING_TRUE_KEYS = {
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_distributed_operation",
    "does_not_mean_carrier_currentness",
    "does_not_mean_current_carrier_selected",
    "does_not_mean_winning_carrier_selected",
    "does_not_mean_losing_carrier_invalidated",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence_action_law",
    "does_not_mean_divergence_resolved",
    "does_not_mean_refusal_erased",
    "does_not_mean_blocked_attempt_erased",
    "does_not_mean_evidence_erased",
    "does_not_mean_registry_authority",
    "does_not_mean_lifecycle_authority",
    "does_not_mean_standing_propagation_authority",
    "does_not_mean_continuity_turn_authority",
    "does_not_mean_currentness_successor_authority",
    "does_not_mean_divergence_consequence_authority",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_carrier_priority",
    "does_not_mean_carrier_sovereignty",
    "does_not_mean_majority_standing",
    "does_not_mean_success_count_standing",
    "does_not_mean_latest_file_standing",
    "does_not_mean_latest_turn_standing",
    "does_not_mean_availability_standing",
    "does_not_mean_possession_standing",
    "does_not_mean_network_standing",
    "does_not_mean_consensus_standing",
    "does_not_mean_launch_publication_readiness",
}

OPEN_TRUE_KEYS = {
    "distributed_standing_implementation",
    "actual_distributed_standing_posture_execution_beyond_this_bounded_result",
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_implementation_beyond_boundary_recording",
    "carrier_continuity_turn_implementation_refinement",
    "future_currentness_successor_refinement_if_separately_justified",
    "future_divergence_consequence_refinement_if_separately_justified",
    "presence_law",
    "threshold_law",
    "truth_law",
    "action_consequence_law",
    "generalized_vessel_relation_lifecycle",
    "body_relevance_medium",
    "signal_series_or_accumulation_logic",
    "successor_carrier_law",
    "future_self_orientation_successor_only_if_separately_justified",
    "repository_synchronization_only_if_separately_declared_and_bounded",
    "full_body_transfer_only_if_separately_declared_and_bounded",
    "distributed_operation_only_if_separately_declared_and_bounded",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}


def base_request(
    *,
    intent: str = "RECORD_DISTRIBUTED_STANDING_BOUNDARY_POSTURE",
    posture: str = RECORDED,
) -> dict:
    return {
        "distributed_standing_request_id": "distributed_standing_boundary_bc_001",
        "distributed_standing_question": (
            "What would it mean for the body to stand across carriers without "
            "source collapse?"
        ),
        "distributed_standing_intent": intent,
        "selected_body_side_standing_posture": {
            "body_side_standing_posture_id": "current_body_standing_closure_post_conformance",
            "body_side_standing_posture_outcome": "CONFORMANCE_CLOSURE_RECORDED",
            "status": "BODY_SIDE_ONLY",
            "posture_remains_body_side": True,
            "not_held_by_carrier": True,
            "not_registry_membership": True,
            "not_repository_synchronization": True,
            "not_full_body_transfer": True,
        },
        "selected_carrier_evidence": [
            {
                "selected_carrier_evidence_id": "carrier_b_successful_receipt_evidence_001",
                "carrier_id": "Carrier B",
                "carrier_evidence_outcome": "CARRIED_SURFACE_RECEIVED",
                "evidence_role": "successful_receipt_evidence",
                "receipt_does_not_create_standing": True,
            },
            {
                "selected_carrier_evidence_id": "carrier_c_blocked_receipt_evidence_001",
                "carrier_id": "Carrier C",
                "carrier_evidence_outcome": "BLOCKED",
                "evidence_role": "blocked_refusal_receipt_evidence",
                "refusal_preserved": True,
                "blocked_attempts_preserved": True,
            },
            {
                "selected_carrier_evidence_id": "carrier_b_c_visible_divergence_evidence_001",
                "carrier_evidence_outcome": "CARRIER_DIVERGENCE_RECORDED",
                "evidence_role": "visible_divergence_evidence",
                "visible_divergence_preserved": True,
            },
            {
                "selected_carrier_evidence_id": "carrier_c_lifecycle_evidence_001",
                "carrier_id": "Carrier C",
                "carrier_evidence_outcome": "CARRIER_REFUSED_OR_BLOCKED",
                "evidence_role": "lifecycle_evidence",
            },
            {
                "selected_carrier_evidence_id": "registry_persistence_v2_evidence_001",
                "carrier_evidence_outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
                "evidence_role": "registry_persistence_reference_only",
            },
            {
                "selected_carrier_evidence_id": "standing_propagation_v2_evidence_001",
                "carrier_evidence_outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
                "evidence_role": "standing_propagation_reference_posture",
            },
            {
                "selected_carrier_evidence_id": "carrier_continuity_turn_v2_evidence_001",
                "carrier_evidence_outcome": "CARRIER_CONTINUITY_TURN_RECORDED",
                "evidence_role": "continuity_turn_lineage",
                "projection_mismatch_preserved": True,
            },
            {
                "selected_carrier_evidence_id": "currentness_successor_evidence_001",
                "carrier_evidence_outcome": "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
                "evidence_role": "body_side_currentness_accounting_only",
            },
            {
                "selected_carrier_evidence_id": "divergence_consequence_evidence_001",
                "carrier_evidence_outcome": "DIVERGENCE_REQUIRES_CAUTION",
                "evidence_role": "divergence_consequence_caution_basis",
            },
            {
                "selected_carrier_evidence_id": "relation_conformance_closure_evidence_001",
                "carrier_evidence_outcome": "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
                "evidence_role": "bounded_relation_closure_basis",
            },
            {
                "selected_carrier_evidence_id": "current_body_conformance_v3_closure_evidence_001",
                "carrier_evidence_outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
                "evidence_role": "body_line_coherence_closure_basis",
            },
        ],
        "requested_distributed_standing_posture": posture,
        "distributed_standing_basis": {
            "basis_id": "distributed_standing_basis_bc_001",
            "source_body_lineage_preserved": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "blocked_attempts_preserved": True,
            "projection_mismatch_preserved": True,
            "divergence_consequence_caution_preserved": True,
            "currentness_successor_accounting_preserved": True,
            "standing_propagation_limits_preserved": True,
            "registry_persistence_reference_limits_preserved": True,
            "lifecycle_posture_limits_preserved": True,
            "continuity_turn_lineage_preserved": True,
            "relation_conformance_closure_basis_preserved": True,
            "current_body_conformance_v3_closure_basis_preserved": True,
            "detailed_basis_distinguished_from_summary": True,
            "summary_overrode_detailed_basis": False,
            "carrier_sovereignty_created": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "repository_synchronization_authorized": False,
            "full_body_transfer_authorized": False,
            "second_body_created": False,
            "continuation_authorized": False,
            "distributed_operation_authorized": False,
        },
        "source_body_lineage": {
            "basis_id": "source_body_lineage_bc_001",
            "upstream_source_body_basis": "current_self_orientation_v8__current_body_conformance_v3_closure",
            "source_body_lineage_preserved": True,
            "source_lineage_distinguishable_from_carrier_held_evidence": True,
            "source_not_replaced": True,
            "source_lineage_not_moved_by_receipt_refusal_admission_registry_propagation_turn_currentness_or_consequence": True,
        },
        "receipt_refusal_admission_basis": {
            "basis_id": "receipt_refusal_admission_basis_bc_001",
            "carrier_b_receipt_basis": "successful physical receipt evidence",
            "carrier_c_refusal_block_basis": "blocked physical receipt evidence",
            "carrier_c_returned_blocked_evidence_admitted_as_evidence_only": True,
            "receipt_does_not_create_standing_by_itself": True,
            "refusal_does_not_invalidate_by_default": True,
            "admission_as_evidence_does_not_create_source_currentness_or_standing": True,
            "visible_refusal_preserved": True,
            "blocked_attempts_preserved": True,
        },
        "divergence_basis": {
            "basis_id": "divergence_basis_bc_001",
            "divergence_evidence_id": "carrier_b_c_visible_divergence_evidence_001",
            "outcome": "CARRIER_DIVERGENCE_RECORDED",
            "visible_divergence_preserved": True,
            "divergence_resolved": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
        },
        "divergence_consequence_basis": {
            "basis_id": "divergence_consequence_basis_bc_001",
            "outcome": "DIVERGENCE_REQUIRES_CAUTION",
            "divergence_consequence_basis_preserved": True,
            "divergence_consequence_caution_preserved": True,
            "distributed_standing_must_carry_b_c_caution": True,
            "divergence_consequence_standing": False,
            "divergence_resolved": False,
            "visible_divergence_preserved": True,
            "visible_refusal_preserved": True,
        },
        "currentness_successor_basis": {
            "basis_id": "currentness_successor_basis_bc_001",
            "outcome": "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            "currentness_successor_basis_preserved": True,
            "body_side_currentness_accounting_only": True,
            "currentness_successor_standing": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "blocked_attempts_preserved": True,
            "projection_mismatch_preserved": True,
        },
        "carrier_continuity_turn_basis": {
            "basis_id": "carrier_continuity_turn_basis_bc_001",
            "outcome": "CARRIER_CONTINUITY_TURN_RECORDED",
            "carrier_continuity_turn_basis_preserved": True,
            "continuity_turn_lineage_preserved": True,
            "projection_mismatch_preserved": True,
            "blocked_attempts_preserved": True,
            "refusal_preserved": True,
            "divergence_preserved": True,
            "detailed_basis_distinguished_from_summary": True,
            "summary_overrode_detailed_basis": False,
            "latest_turn_standing": False,
            "successor_projection_is_not_distributed_standing": True,
        },
        "standing_propagation_basis": {
            "basis_id": "standing_propagation_basis_bc_001",
            "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
            "standing_propagation_basis_preserved": True,
            "standing_propagation_standing": False,
            "carried_standing_related_evidence_is_reference_only": True,
            "receipt_admission_registry_reference_remain_non_standing": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
        },
        "registry_persistence_basis": {
            "basis_id": "registry_persistence_basis_bc_001",
            "outcome": "CARRIER_REGISTRY_PERSISTENCE_BOUNDARY_RECORDED",
            "registry_persistence_basis_preserved": True,
            "registry_record_standing": False,
            "registry_reference_only": True,
            "registry_presence_is_not_distributed_standing": True,
            "latest_registry_reference_is_not_distributed_standing": True,
        },
        "lifecycle_basis": {
            "basis_id": "lifecycle_basis_bc_001",
            "carrier_id": "Carrier C",
            "lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
            "lifecycle_basis_preserved": True,
            "lifecycle_status_standing": False,
            "carrier_c_refusal_block_is_not_invalidation": True,
            "carrier_c_refusal_block_does_not_select_carrier_b_as_winner": True,
        },
        "relation_conformance_closure_basis": {
            "basis_id": "relation_conformance_closure_basis_bc_001",
            "relation": "B/C divergence-bounded relation",
            "relation_conformance_outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
            "closure_outcome": "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
            "relation_conformance_closure_basis_preserved": True,
            "relation_closure_does_not_create_distributed_standing": True,
            "closure_of_meaning_is_not_continuation": True,
            "conformance_is_not_permission": True,
            "current_carrier_selected": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
        },
        "current_body_conformance_v3_closure_basis": {
            "basis_id": "current_body_conformance_v3_closure_basis_bc_001",
            "outcome": "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
            "current_body_conformance_v3_closure_basis_preserved": True,
            "body_line_coherence_meaning_only": True,
            "does_not_authorize_continuation": True,
            "does_not_create_distributed_standing": True,
        },
        "visible_refusal_basis": {
            "visible_refusal_preserved": True,
            "refusal_remains_visible": True,
        },
        "visible_divergence_basis": {
            "visible_divergence_preserved": True,
            "divergence_remains_visible": True,
        },
        "blocked_attempt_basis": {
            "blocked_attempts_preserved": True,
            "blocked_attempt_remains_visible": True,
        },
        "projection_mismatch_basis": {
            "projection_mismatch_preserved": True,
            "projection_mismatch_remains_visible": True,
        },
        "detailed_basis_reference": "distributed_standing_basis.detailed",
        "summary_projection_reference": "distributed_standing_summary_projection",
        "declared_non_claims": copy.deepcopy(resolver.REQUIRED_NON_CLAIMS),
        "declared_scope": "future distributed-standing boundary review only",
        "required_additional_basis_explanation": (
            "additional declared source and prerequisite basis would be needed"
        ),
        "exclusion_reason": "excluded only for the declared scope",
        "revalidation_reason": "bounded revalidation would be needed before review",
        "separate_review_reason": "separate bounded review would be needed before review",
    }


class DistributedStandingBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_distributed_standing_boundary(
            declared_distributed_standing_request=copy.deepcopy(
                base_request() if request is None else request
            )
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["distributed_standing_summary"]["failed_check_count"], 0)
        self.assertTrue(
            result["distributed_standing_statement"][
                "distributed_standing_posture_recorded"
            ]
        )

    def assert_block(self, request: dict | None, expected_code: str) -> dict:
        result = (
            resolver.resolve_distributed_standing_boundary()
            if request is None
            else self.resolve(request)
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(result["block"]["block_code"], expected_code)
        return result

    def assert_required_non_claims_false(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertFalse(non_claims[key], key)
        self.assertTrue(non_claims["required_non_claims_preserved"])

    def assert_statement_false_posture(self, statement: dict) -> None:
        for key in FALSE_STATEMENT_KEYS:
            self.assertIn(key, statement)
            self.assertFalse(statement[key], key)

    def test_successful_distributed_standing_boundary_recording(self) -> None:
        result = self.resolve()

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assert_recorded(result)

        statement = result["distributed_standing_statement"]
        for key in (
            "body_side_standing_posture_preserved",
            "selected_carrier_evidence_preserved",
            "selected_carrier_evidence_identities_preserved",
            "selected_carrier_evidence_outcomes_preserved",
            "source_body_lineage_preserved",
            "receipt_refusal_admission_basis_preserved",
            "divergence_basis_preserved",
            "divergence_consequence_basis_preserved",
            "currentness_successor_basis_preserved",
            "carrier_continuity_turn_basis_preserved",
            "standing_propagation_basis_preserved",
            "registry_persistence_basis_preserved",
            "lifecycle_basis_preserved",
            "relation_conformance_closure_basis_preserved",
            "current_body_conformance_v3_closure_basis_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "blocked_attempts_preserved",
            "projection_mismatch_preserved",
            "detailed_basis_distinguished_from_summary",
        ):
            self.assertTrue(statement[key], key)
        self.assert_statement_false_posture(statement)

    def test_metadata_and_declared_question(self) -> None:
        result = self.resolve()
        metadata = result["distributed_standing_metadata"]

        for key in (
            "distributed_standing_result_id",
            "distributed_standing_result_type",
            "distributed_standing_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["distributed_standing_result_version"], "0.1.0")
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_distributed_standing_boundary",
        )

        question = result["declared_distributed_standing_question"]
        self.assertEqual(
            question["distributed_standing_request_id"],
            "distributed_standing_boundary_bc_001",
        )
        self.assertIn("stand across carriers", question["distributed_standing_question"])
        self.assertEqual(question["distributed_standing_intent"], resolver.RECORD_INTENT)
        self.assertEqual(
            result["distributed_standing_posture"][
                "requested_distributed_standing_posture"
            ],
            RECORDED,
        )
        self.assertEqual(question["declared_non_claims"], resolver.REQUIRED_NON_CLAIMS)
        self.assertTrue(question["distributed_standing_is_not_synchronization"])
        self.assertTrue(question["distributed_standing_is_not_distributed_currentness"])
        self.assertTrue(question["distributed_standing_is_not_carrier_majority"])
        self.assertTrue(question["distributed_standing_is_not_successful_receipt_count"])
        self.assertTrue(question["distributed_standing_is_not_registry_presence"])
        self.assertTrue(question["distributed_standing_is_not_body_transfer"])
        self.assertTrue(question["distributed_standing_is_not_second_body"])
        self.assertTrue(question["distributed_standing_is_not_carrier_sovereignty"])
        self.assertTrue(question["distributed_standing_is_not_current_carrier_selection"])
        self.assertTrue(question["distributed_standing_is_not_winner_loser_selection"])
        self.assertTrue(question["distributed_standing_is_not_action"])
        self.assertTrue(question["distributed_standing_is_not_truth"])

    def test_body_posture_carrier_evidence_and_source_lineage_sections(self) -> None:
        result = self.resolve()
        posture = result["selected_body_side_standing_posture"]
        carrier = result["selected_carrier_evidence"]
        source = result["source_body_lineage"]

        self.assertEqual(
            posture["selected_body_side_standing_posture_id"],
            "current_body_standing_closure_post_conformance",
        )
        self.assertEqual(
            posture["selected_body_side_standing_posture_outcome"],
            "CONFORMANCE_CLOSURE_RECORDED",
        )
        self.assertTrue(posture["body_side_posture_remains_body_side"])
        self.assertTrue(posture["body_side_posture_is_not_held_by_carrier"])
        self.assertTrue(posture["body_side_posture_does_not_select_current_carrier"])
        self.assertTrue(posture["raw_selected_body_side_standing_posture"]["not_registry_membership"])
        self.assertTrue(posture["raw_selected_body_side_standing_posture"]["not_full_body_transfer"])

        self.assertEqual(carrier["selected_carrier_evidence_count"], 11)
        for evidence_id in (
            "carrier_b_successful_receipt_evidence_001",
            "carrier_c_blocked_receipt_evidence_001",
            "carrier_b_c_visible_divergence_evidence_001",
            "carrier_c_lifecycle_evidence_001",
            "registry_persistence_v2_evidence_001",
            "standing_propagation_v2_evidence_001",
            "carrier_continuity_turn_v2_evidence_001",
            "currentness_successor_evidence_001",
            "divergence_consequence_evidence_001",
            "relation_conformance_closure_evidence_001",
            "current_body_conformance_v3_closure_evidence_001",
        ):
            self.assertIn(evidence_id, carrier["selected_carrier_evidence_ids"])
        self.assertIn("CARRIED_SURFACE_RECEIVED", carrier["selected_carrier_evidence_outcomes"])
        self.assertIn("BLOCKED", carrier["selected_carrier_evidence_outcomes"])
        self.assertTrue(carrier["carrier_evidence_remains_evidence"])
        self.assertTrue(carrier["carrier_evidence_does_not_become_source"])
        self.assertTrue(carrier["carrier_evidence_does_not_become_currentness"])
        self.assertTrue(carrier["carrier_evidence_does_not_select_winner_or_loser"])

        self.assertTrue(source["source_body_lineage_declared"])
        self.assertTrue(source["source_body_lineage_preserved"])
        self.assertTrue(
            source["raw_source_body_lineage"][
                "source_lineage_distinguishable_from_carrier_held_evidence"
            ]
        )
        self.assertTrue(source["raw_source_body_lineage"]["source_not_replaced"])

    def test_prerequisite_basis_sections_are_preserved_as_basis_only(self) -> None:
        result = self.resolve()

        for section_name in (
            "receipt_refusal_admission_basis",
            "divergence_basis",
            "divergence_consequence_basis",
            "currentness_successor_basis",
            "carrier_continuity_turn_basis",
            "standing_propagation_basis",
            "registry_persistence_basis",
            "lifecycle_basis",
            "relation_conformance_closure_basis",
            "current_body_conformance_v3_closure_basis",
        ):
            section = result[section_name]
            self.assertTrue(section[f"{section_name}_declared"], section_name)
            self.assertTrue(section[f"{section_name}_preserved"], section_name)
            self.assertTrue(section["basis_preserved_where_supplied_or_required"], section_name)
            self.assertTrue(section["basis_is_prerequisite_only"], section_name)
            self.assertTrue(section["basis_does_not_decide_distributed_standing_by_itself"], section_name)
            self.assertTrue(section["basis_does_not_authorize_sync_or_operation"], section_name)

        self.assertTrue(
            result["receipt_refusal_admission_basis"]["raw_receipt_refusal_admission_basis"][
                "carrier_c_returned_blocked_evidence_admitted_as_evidence_only"
            ]
        )
        self.assertFalse(
            result["divergence_basis"]["raw_divergence_basis"]["divergence_resolved"]
        )
        self.assertTrue(
            result["divergence_consequence_basis"]["raw_divergence_consequence_basis"][
                "distributed_standing_must_carry_b_c_caution"
            ]
        )
        self.assertFalse(
            result["currentness_successor_basis"]["raw_currentness_successor_basis"][
                "currentness_successor_standing"
            ]
        )
        self.assertTrue(
            result["carrier_continuity_turn_basis"]["raw_carrier_continuity_turn_basis"][
                "projection_mismatch_preserved"
            ]
        )
        self.assertFalse(
            result["standing_propagation_basis"]["raw_standing_propagation_basis"][
                "standing_propagation_standing"
            ]
        )
        self.assertTrue(
            result["registry_persistence_basis"]["raw_registry_persistence_basis"][
                "registry_reference_only"
            ]
        )
        self.assertEqual(
            result["lifecycle_basis"]["raw_lifecycle_basis"]["lifecycle_status"],
            "CARRIER_REFUSED_OR_BLOCKED",
        )
        self.assertTrue(
            result["relation_conformance_closure_basis"][
                "raw_relation_conformance_closure_basis"
            ]["closure_of_meaning_is_not_continuation"]
        )
        self.assertTrue(
            result["current_body_conformance_v3_closure_basis"][
                "raw_current_body_conformance_v3_closure_basis"
            ]["body_line_coherence_meaning_only"]
        )

    def test_distributed_standing_posture_and_checks(self) -> None:
        result = self.resolve()
        posture = result["distributed_standing_posture"]
        checks = result["distributed_standing_checks"]

        self.assertEqual(posture["requested_distributed_standing_posture"], RECORDED)
        self.assertTrue(posture["distributed_standing_posture_supported"])
        self.assertTrue(posture["distributed_standing_posture_preserved"])
        self.assertTrue(posture["posture_is_bounded_body_side_standing_posture"])
        self.assertTrue(posture["posture_is_not_repository_synchronization"])
        self.assertTrue(posture["posture_is_not_full_body_transfer"])
        self.assertTrue(posture["posture_is_not_distributed_operation"])

        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertTrue(check["passed"], check)
        self.assertEqual(result["distributed_standing_summary"]["failed_check_count"], 0)
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({c["check_name"] for c in checks}))

    def test_other_non_recorded_outcome_postures_are_bounded(self) -> None:
        for posture in (
            NOT_RECORDED,
            REQUIRES_ADDITIONAL_BASIS,
            EXCLUDED_FOR_SCOPE,
            REQUIRES_REVALIDATION,
            REQUIRES_SEPARATE_REVIEW,
        ):
            with self.subTest(posture=posture):
                result = self.resolve(base_request(posture=posture))
                statement = result["distributed_standing_statement"]
                self.assertEqual(result["outcome"], posture)
                self.assertFalse(statement["distributed_standing_posture_recorded"])
                self.assertTrue(statement["selected_carrier_evidence_preserved"])
                self.assert_statement_false_posture(statement)
                self.assertFalse(statement.get("additional_basis_scheduled", False))
                self.assertFalse(statement.get("additional_basis_authorized", False))
                self.assertFalse(
                    statement.get("exclusion_generalized_beyond_declared_scope", False)
                )
                self.assertFalse(statement["revalidation_scheduled"])
                self.assertFalse(statement["revalidation_authorized"])
                self.assertFalse(statement["separate_review_scheduled"])
                self.assertFalse(statement["separate_review_authorized"])

    def test_non_meaning_and_open_surfaces(self) -> None:
        result = self.resolve()

        for key in NON_MEANING_TRUE_KEYS:
            self.assertIn(key, result["distributed_standing_non_meaning"])
            self.assertTrue(result["distributed_standing_non_meaning"][key], key)
        for key in OPEN_TRUE_KEYS:
            self.assertIn(key, result["what_remains_open"])
            self.assertTrue(result["what_remains_open"][key], key)

    def test_summary_helper_projects_result(self) -> None:
        result = self.resolve()
        summary = resolver.build_distributed_standing_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["distributed_standing_request_id"],
            "distributed_standing_boundary_bc_001",
        )
        self.assertIn("stand across carriers", summary["distributed_standing_question"])
        self.assertEqual(summary["distributed_standing_intent"], resolver.RECORD_INTENT)
        self.assertEqual(summary["requested_distributed_standing_posture"], RECORDED)
        self.assertEqual(
            summary["selected_body_side_standing_posture_id"],
            "current_body_standing_closure_post_conformance",
        )
        self.assertEqual(
            summary["selected_body_side_standing_posture_outcome"],
            "CONFORMANCE_CLOSURE_RECORDED",
        )
        self.assertIn(
            "carrier_b_successful_receipt_evidence_001",
            summary["selected_carrier_evidence_ids"],
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["distributed_standing_posture_recorded"])
        self.assertTrue(summary["source_body_lineage_preserved"])
        self.assertTrue(summary["selected_carrier_evidence_preserved"])
        self.assertTrue(summary["divergence_consequence_basis_preserved"])
        self.assertTrue(summary["currentness_successor_basis_preserved"])
        self.assertTrue(summary["carrier_continuity_turn_basis_preserved"])
        self.assertTrue(summary["standing_propagation_basis_preserved"])
        self.assertTrue(summary["registry_persistence_basis_preserved"])
        self.assertTrue(summary["lifecycle_basis_preserved"])
        self.assertTrue(summary["relation_conformance_closure_basis_preserved"])
        self.assertTrue(summary["current_body_conformance_v3_closure_basis_preserved"])
        self.assertTrue(summary["visible_refusal_preserved"])
        self.assertTrue(summary["visible_divergence_preserved"])
        self.assertTrue(summary["blocked_attempts_preserved"])
        self.assertTrue(summary["projection_mismatch_preserved"])
        self.assertTrue(summary["detailed_basis_distinguished_from_summary"])
        self.assertFalse(summary["summary_overrode_detailed_basis"])
        self.assertFalse(summary["carrier_currentness_created"])
        self.assertFalse(summary["current_carrier_selected"])
        self.assertFalse(summary["winning_carrier_selected"])
        self.assertFalse(summary["losing_carrier_invalidated"])
        self.assertTrue(summary["no_source_currentness_authority_permission"])
        self.assertTrue(summary["no_truth_action"])
        self.assertTrue(summary["no_divergence_resolution"])
        self.assertTrue(summary["no_evidence_erasure"])
        self.assertTrue(summary["no_sync_full_body_transfer_second_body"])
        self.assertTrue(summary["no_continuation"])
        self.assertTrue(summary["no_distributed_operation"])
        self.assertTrue(summary["no_latest_file_turn_majority_success_count_standing"])
        self.assertFalse(summary["key_non_claims"]["authority_created"])
        self.assertFalse(summary["key_non_claims"]["distributed_operation_authorized"])
        self.assertTrue(result["non_claims"]["required_non_claims_preserved"])

    def test_result_level_non_claims_for_all_outcome_families(self) -> None:
        results = [
            self.resolve(),
            self.resolve(base_request(intent=resolver.DO_NOT_RECORD_INTENT)),
            self.resolve(base_request(posture=REQUIRES_ADDITIONAL_BASIS)),
            self.resolve(base_request(posture=EXCLUDED_FOR_SCOPE)),
            self.resolve(base_request(posture=REQUIRES_REVALIDATION)),
            self.resolve(base_request(posture=REQUIRES_SEPARATE_REVIEW)),
            self.resolve(base_request(intent=resolver.BLOCK_INTENT)),
        ]

        for result in results:
            self.assertIn(result["outcome"], OUTCOME_FAMILY)
            self.assert_required_non_claims_false(result)

    def test_supported_distributed_standing_postures_return_supported_family(self) -> None:
        for posture in sorted(resolver.SUPPORTED_DISTRIBUTED_STANDING_POSTURES):
            with self.subTest(posture=posture):
                result = self.resolve(base_request(posture=posture))
                self.assertIn(result["outcome"], OUTCOME_FAMILY)
                self.assert_required_non_claims_false(result)

    def test_request_builder_helper(self) -> None:
        source = base_request()
        request = resolver.build_declared_distributed_standing_request(
            distributed_standing_request_id="builder_distributed_standing_001",
            distributed_standing_question="What would bounded distributed standing mean?",
            selected_body_side_standing_posture=source[
                "selected_body_side_standing_posture"
            ],
            selected_carrier_evidence=source["selected_carrier_evidence"],
            requested_distributed_standing_posture=RECORDED,
            distributed_standing_basis=source["distributed_standing_basis"],
            source_body_lineage=source["source_body_lineage"],
            receipt_refusal_admission_basis=source["receipt_refusal_admission_basis"],
            divergence_basis=source["divergence_basis"],
            divergence_consequence_basis=source["divergence_consequence_basis"],
            currentness_successor_basis=source["currentness_successor_basis"],
            carrier_continuity_turn_basis=source["carrier_continuity_turn_basis"],
            standing_propagation_basis=source["standing_propagation_basis"],
            registry_persistence_basis=source["registry_persistence_basis"],
            lifecycle_basis=source["lifecycle_basis"],
            relation_conformance_closure_basis=source[
                "relation_conformance_closure_basis"
            ],
            current_body_conformance_v3_closure_basis=source[
                "current_body_conformance_v3_closure_basis"
            ],
        )

        self.assertEqual(request["distributed_standing_request_id"], "builder_distributed_standing_001")
        self.assertEqual(request["distributed_standing_question"], "What would bounded distributed standing mean?")
        self.assertEqual(
            request["selected_body_side_standing_posture"],
            source["selected_body_side_standing_posture"],
        )
        self.assertEqual(request["selected_carrier_evidence"], source["selected_carrier_evidence"])
        self.assertEqual(request["requested_distributed_standing_posture"], RECORDED)
        self.assertEqual(request["distributed_standing_basis"], source["distributed_standing_basis"])
        self.assertEqual(request["declared_non_claims"], resolver.REQUIRED_NON_CLAIMS)

        result = self.resolve(request)
        self.assert_recorded(result)

    def test_path_based_resolution(self) -> None:
        request = base_request()
        mapping_result = self.resolve(request)

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "declared_distributed_standing_request.json"
            path.write_text(json.dumps(request), encoding="utf-8")
            path_result = resolver.resolve_distributed_standing_boundary_from_path(path)

        self.assert_recorded(path_result)
        self.assertEqual(set(path_result), set(mapping_result))
        self.assertTrue(
            path_result["declared_distributed_standing_question"][
                "request_path"
            ].endswith("declared_distributed_standing_request.json")
        )

    def test_write_behavior_and_default_output_path(self) -> None:
        result = self.resolve()

        with tempfile.TemporaryDirectory() as tmp:
            explicit_path = Path(tmp) / "nested" / "result.json"
            written = resolver.write_distributed_standing_result(result, explicit_path)
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            default_root = Path(tmp) / "bounded_default_root"
            with patch.object(resolver, "DISTRIBUTED_STANDING_BOUNDARY_ROOT", default_root):
                first = resolver.write_distributed_standing_result(result)
                second = resolver.write_distributed_standing_result(result)

            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("__distributed_standing_result", first.name)
            self.assertIn("__distributed_standing_result", second.name)

    def test_non_mutation_posture(self) -> None:
        request = base_request()
        original = copy.deepcopy(request)
        selected_body = request["selected_body_side_standing_posture"]
        selected_carrier = request["selected_carrier_evidence"]
        bases = {
            key: request[key]
            for key in (
                "source_body_lineage",
                "receipt_refusal_admission_basis",
                "divergence_basis",
                "divergence_consequence_basis",
                "currentness_successor_basis",
                "carrier_continuity_turn_basis",
                "standing_propagation_basis",
                "registry_persistence_basis",
                "lifecycle_basis",
                "relation_conformance_closure_basis",
                "current_body_conformance_v3_closure_basis",
            )
        }

        result = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request, original)
        self.assertEqual(selected_body, original["selected_body_side_standing_posture"])
        self.assertEqual(selected_carrier, original["selected_carrier_evidence"])
        for key, value in bases.items():
            self.assertEqual(value, original[key])
        self.assertEqual(result["outcome"], second["outcome"])

        before_write = copy.deepcopy(result)
        with tempfile.TemporaryDirectory() as tmp:
            resolver.write_distributed_standing_result(result, Path(tmp) / "result.json")
        self.assertEqual(result, before_write)

    def test_not_recorded_readable_request(self) -> None:
        result = self.resolve(base_request(intent=resolver.DO_NOT_RECORD_INTENT))

        self.assertEqual(result["outcome"], NOT_RECORDED)
        self.assertFalse(
            result["distributed_standing_statement"][
                "distributed_standing_posture_recorded"
            ]
        )
        self.assertEqual(
            result["declared_distributed_standing_question"]["not_recorded_reason"],
            "declared request does not record distributed standing boundary posture",
        )
        self.assert_statement_false_posture(result["distributed_standing_statement"])

    def test_explicit_block_intent(self) -> None:
        result = self.resolve(base_request(intent=resolver.BLOCK_INTENT))

        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "DISTRIBUTED_STANDING_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assertFalse(
            result["distributed_standing_statement"][
                "distributed_standing_posture_recorded"
            ]
        )

    def test_blocking_missing_and_malformed_request(self) -> None:
        self.assert_block(None, "DISTRIBUTED_STANDING_QUESTION_UNDECLARED")
        result = resolver.resolve_distributed_standing_boundary(
            declared_distributed_standing_request=["not", "a", "mapping"]
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
        )

    def test_blocking_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            missing_result = resolver.resolve_distributed_standing_boundary_from_path(
                missing
            )
            self.assertEqual(
                missing_result["block"]["block_code"],
                "DECLARED_DISTRIBUTED_STANDING_REQUEST_UNREADABLE",
            )

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            malformed_result = resolver.resolve_distributed_standing_boundary_from_path(
                malformed
            )
            self.assertEqual(
                malformed_result["block"]["block_code"],
                "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
            )

            array_path = Path(tmp) / "array.json"
            array_path.write_text(json.dumps([]), encoding="utf-8")
            array_result = resolver.resolve_distributed_standing_boundary_from_path(
                array_path
            )
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_DISTRIBUTED_STANDING_REQUEST_MALFORMED",
            )

    def test_blocking_question_intent_posture(self) -> None:
        request = base_request()
        request.pop("distributed_standing_question")
        self.assert_block(request, "DISTRIBUTED_STANDING_QUESTION_UNDECLARED")

        request = base_request(intent="UNSUPPORTED")
        self.assert_block(request, "DISTRIBUTED_STANDING_INTENT_UNSUPPORTED")

        request = base_request(posture="UNSUPPORTED_POSTURE")
        self.assert_block(request, "DISTRIBUTED_STANDING_POSTURE_UNSUPPORTED")

    def test_blocking_body_posture_and_carrier_evidence(self) -> None:
        request = base_request()
        request.pop("selected_body_side_standing_posture")
        self.assert_block(request, "BODY_SIDE_STANDING_POSTURE_MISSING")

        request = base_request()
        request.pop("selected_carrier_evidence")
        self.assert_block(request, "SELECTED_CARRIER_EVIDENCE_MISSING")

        request = base_request()
        request["selected_carrier_evidence"] = "malformed"
        self.assert_block(request, "SELECTED_CARRIER_EVIDENCE_MALFORMED")

        request = base_request()
        request["selected_carrier_evidence"][0].pop("selected_carrier_evidence_id")
        self.assert_block(request, "SELECTED_CARRIER_EVIDENCE_IDENTITY_OR_OUTCOME_MISSING")

        request = base_request()
        request["selected_carrier_evidence"][0].pop("carrier_evidence_outcome")
        self.assert_block(request, "SELECTED_CARRIER_EVIDENCE_IDENTITY_OR_OUTCOME_MISSING")

    def test_blocking_missing_basis(self) -> None:
        for field, code in (
            ("distributed_standing_basis", "DISTRIBUTED_STANDING_BASIS_MISSING"),
            ("source_body_lineage", "SOURCE_BODY_LINEAGE_MISSING"),
            ("divergence_consequence_basis", "DIVERGENCE_CONSEQUENCE_BASIS_MISSING"),
            ("currentness_successor_basis", "CURRENTNESS_SUCCESSOR_BASIS_MISSING"),
            ("carrier_continuity_turn_basis", "CARRIER_CONTINUITY_TURN_BASIS_MISSING"),
            ("standing_propagation_basis", "STANDING_PROPAGATION_BASIS_MISSING"),
            ("registry_persistence_basis", "REGISTRY_PERSISTENCE_BASIS_MISSING"),
            ("lifecycle_basis", "LIFECYCLE_BASIS_MISSING"),
            (
                "current_body_conformance_v3_closure_basis",
                "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                request.pop(field)
                self.assert_block(request, code)

        request = base_request()
        request["relation_conformance_closure_basis_required"] = True
        request.pop("relation_conformance_closure_basis")
        self.assert_block(request, "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING")

    def test_blocking_hidden_visibility_and_summary_override(self) -> None:
        for field, code in (
            ("visible_refusal_hidden", "DISTRIBUTED_STANDING_HIDES_REFUSAL"),
            ("visible_divergence_hidden", "DISTRIBUTED_STANDING_HIDES_DIVERGENCE"),
            ("blocked_attempt_hidden", "DISTRIBUTED_STANDING_HIDES_BLOCKED_ATTEMPT"),
            (
                "projection_mismatch_hidden",
                "DISTRIBUTED_STANDING_HIDES_PROJECTION_MISMATCH",
            ),
            ("summary_overrode_detailed_basis", "SUMMARY_OVERWRITES_DETAILED_BASIS"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request[field] = True
                self.assert_block(request, code)

    def test_blocking_carrier_currentness_selection_and_source(self) -> None:
        for field, code in (
            (
                "carrier_currentness_created",
                "DISTRIBUTED_STANDING_CREATES_CARRIER_CURRENTNESS",
            ),
            ("current_carrier_selected", "DISTRIBUTED_STANDING_SELECTS_CURRENT_CARRIER"),
            ("winning_carrier_selected", "DISTRIBUTED_STANDING_SELECTS_WINNING_CARRIER"),
            (
                "losing_carrier_invalidated",
                "DISTRIBUTED_STANDING_INVALIDATES_LOSING_CARRIER",
            ),
            ("source_replaced", "DISTRIBUTED_STANDING_REPLACES_SOURCE"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_authority_permission_truth_action_divergence_evidence(self) -> None:
        for field, code in (
            ("authority_created", "DISTRIBUTED_STANDING_CREATES_AUTHORITY"),
            ("permission_created", "DISTRIBUTED_STANDING_CREATES_PERMISSION"),
            ("truth_created", "DISTRIBUTED_STANDING_CREATES_TRUTH"),
            ("action_authorized", "DISTRIBUTED_STANDING_AUTHORIZES_ACTION"),
            ("divergence_resolved", "DISTRIBUTED_STANDING_RESOLVES_DIVERGENCE"),
            ("distributed_standing_erased_evidence", "DISTRIBUTED_STANDING_ERASES_EVIDENCE"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_sync_transfer_second_body_continuation_operation(self) -> None:
        for field, code in (
            (
                "repository_synchronization_authorized",
                "DISTRIBUTED_STANDING_AUTHORIZES_REPOSITORY_SYNC",
            ),
            (
                "full_body_transfer_authorized",
                "DISTRIBUTED_STANDING_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "DISTRIBUTED_STANDING_CREATES_SECOND_BODY"),
            ("continuation_authorized", "DISTRIBUTED_STANDING_AUTHORIZES_CONTINUATION"),
            (
                "distributed_operation_authorized",
                "DISTRIBUTED_STANDING_AUTHORIZES_DISTRIBUTED_OPERATION",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_latest_majority_success_count_and_availability_standing(self) -> None:
        for field, code in (
            ("latest_file_standing", "LATEST_FILE_OR_TURN_STANDING"),
            ("latest_turn_standing", "LATEST_FILE_OR_TURN_STANDING"),
            ("majority_carrier_standing", "MAJORITY_OR_SUCCESS_COUNT_STANDING"),
            ("successful_receipt_count_standing", "MAJORITY_OR_SUCCESS_COUNT_STANDING"),
            (
                "availability_standing",
                "REGISTRY_LIFECYCLE_PROPAGATION_TURN_CURRENTNESS_OR_CONSEQUENCE_STANDING",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                if field in request["declared_non_claims"]:
                    request["declared_non_claims"][field] = True
                else:
                    request[field] = True
                self.assert_block(request, code)

    def test_blocking_prerequisite_standing_by_itself(self) -> None:
        for field in (
            "registry_record_standing",
            "lifecycle_status_standing",
            "standing_propagation_standing",
            "continuity_turn_standing",
            "currentness_successor_standing",
            "divergence_consequence_standing",
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(
                    request,
                    "REGISTRY_LIFECYCLE_PROPAGATION_TURN_CURRENTNESS_OR_CONSEQUENCE_STANDING",
                )

    def test_blocking_mutation_replay_merge(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_blocking_required_non_claim_missing_or_flipped(self) -> None:
        request = base_request()
        request["declared_non_claims"].pop("recency_fraud")
        result = self.assert_block(request, "NON_CLAIM_MISSING_OR_FLIPPED")
        self.assertIn("recency_fraud", result["non_claims"]["missing_required_non_claims"])

        request = base_request()
        request["declared_non_claims"]["permission_created"] = True
        result = self.resolve(request)
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertIn(
            result["block"]["block_code"],
            {
                "DISTRIBUTED_STANDING_CREATES_PERMISSION",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            },
        )
        self.assertIn("raw_declared_non_claims", result["non_claims"])
        self.assertTrue(result["non_claims"]["raw_declared_non_claims"])


if __name__ == "__main__":
    unittest.main()
