"""Bounded tests for the cross-carrier divergence consequence boundary resolver.

These tests audit one surface only: scoped divergence consequence posture.  They
do not test divergence resolution, truth, action, carrier currentness, or
distributed standing.
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

import resolve_cross_carrier_divergence_consequence_boundary as resolver


RECORDED = "DIVERGENCE_CONSEQUENCE_RECORDED"
NOT_RECORDED = "DIVERGENCE_CONSEQUENCE_NOT_RECORDED"
BLOCKED = "DIVERGENCE_CONSEQUENCE_BLOCKED"

TOP_LEVEL_SECTIONS = {
    "divergence_consequence_metadata",
    "declared_divergence_consequence_question",
    "declared_reliance_or_use_question",
    "selected_divergence_evidence",
    "selected_carrier_evidence",
    "currentness_successor_basis",
    "carrier_continuity_turn_basis",
    "standing_propagation_basis",
    "registry_persistence_basis",
    "lifecycle_basis",
    "relation_conformance_closure_basis",
    "divergence_consequence_posture",
    "consequence_scope",
    "consequence_checks",
    "consequence_statement",
    "consequence_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "divergence_consequence_summary",
}

EXPECTED_CHECK_NAMES = {
    "divergence_consequence_question_declared",
    "divergence_consequence_intent_supported",
    "reliance_or_use_question_declared",
    "selected_divergence_evidence_present",
    "selected_divergence_evidence_parseable",
    "selected_divergence_evidence_outcome_present",
    "selected_carrier_evidence_preserved_where_required_or_supplied",
    "divergence_consequence_posture_supported",
    "divergence_consequence_basis_declared",
    "currentness_successor_basis_preserved_where_required_or_supplied",
    "carrier_continuity_turn_basis_preserved_where_required_or_supplied",
    "lifecycle_registry_propagation_basis_preserved_where_required_or_supplied",
    "relation_conformance_closure_basis_preserved_where_required_or_supplied",
    "consequence_scope_declared",
    "visible_divergence_preserved",
    "visible_refusal_preserved_where_applicable",
    "blocked_attempts_preserved_where_applicable",
    "projection_mismatch_preserved_where_applicable",
    "detailed_basis_distinguishable_from_summary_where_applicable",
    "summary_does_not_override_detailed_basis",
    "no_divergence_resolution",
    "no_winner_selection",
    "no_loser_invalidation",
    "no_carrier_currentness",
    "no_current_carrier_selection",
    "no_source_replacement",
    "no_authority",
    "no_permission",
    "no_truth",
    "no_action",
    "no_carrier_hierarchy",
    "no_evidence_erasure",
    "no_distributed_standing",
    "no_repository_sync",
    "no_full_body_transfer",
    "no_second_body",
    "no_continuation",
    "no_distributed_operation",
    "no_latest_file_or_turn_consequence",
    "no_majority_or_success_count_consequence",
    "no_registry_lifecycle_propagation_or_turn_consequence_by_itself",
    "no_mutation_replay_or_merge",
    "non_claims_remain_false",
}

FALSE_STATEMENT_KEYS = {
    "summary_overrode_detailed_basis",
    "divergence_resolved",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_currentness_created",
    "currentness_created",
    "current_carrier_selected",
    "source_replaced",
    "authority_created",
    "permission_created",
    "truth_created",
    "action_authorized",
    "carrier_hierarchy_created",
    "evidence_erased",
    "distributed_standing_created",
    "repository_synchronization_authorized",
    "full_body_transfer_authorized",
    "second_body_created",
    "continuation_authorized",
    "distributed_operation_authorized",
    "latest_file_consequence",
    "latest_turn_consequence",
    "majority_carrier_consequence",
    "successful_receipt_count_consequence",
}

NON_MEANING_TRUE_KEYS = {
    "does_not_mean_divergence_resolved",
    "does_not_mean_truth_created",
    "does_not_mean_action_authorized",
    "does_not_mean_consequence_action_law_created",
    "does_not_mean_winner_selected",
    "does_not_mean_loser_invalidated",
    "does_not_mean_carrier_hierarchy",
    "does_not_mean_current_carrier_selected",
    "does_not_mean_carrier_currentness",
    "does_not_mean_source_replacement",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_distributed_standing",
    "does_not_mean_distributed_currentness",
    "does_not_mean_evidence_erased",
    "does_not_mean_refusal_erased",
    "does_not_mean_blocked_attempt_erased",
    "does_not_mean_projection_mismatch_erased",
    "does_not_mean_registry_lifecycle_propagation_turn_currentness",
    "does_not_mean_latest_file_consequence",
    "does_not_mean_latest_turn_consequence",
    "does_not_mean_majority_consequence",
    "does_not_mean_success_count_consequence",
    "does_not_mean_repository_synchronization",
    "does_not_mean_full_body_transfer",
    "does_not_mean_second_body",
    "does_not_mean_continuation",
    "does_not_mean_distributed_operation",
}

OPEN_TRUE_KEYS = {
    "divergence_consequence_implementation_refinement",
    "distributed_standing_boundary",
    "distributed_standing",
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_implementation_beyond_boundary_recording",
    "carrier_continuity_turn_implementation_refinement",
    "future_currentness_successor_refinement_if_separately_justified",
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


def base_request(
    *,
    intent: str = "RECORD_DIVERGENCE_CONSEQUENCE",
    posture: str = "DIVERGENCE_REQUIRES_CAUTION",
) -> dict:
    declared_use = (
        "May B/C visible divergence require caution before any future "
        "distributed-standing prerequisite review?"
    )
    return {
        "divergence_consequence_request_id": "divergence_consequence_bc_caution_001",
        "divergence_consequence_question": (
            "What lawful effect may visible B/C divergence have without resolving it?"
        ),
        "divergence_consequence_intent": intent,
        "declared_reliance_or_use_question": declared_use,
        "selected_divergence_evidence": {
            "selected_divergence_evidence_id": (
                "carrier_b_success__carrier_c_blocked_receipt_divergence_001"
            ),
            "selected_divergence_evidence_outcome": "CARRIER_DIVERGENCE_RECORDED",
            "divergence_type": "RECEIPT_REFUSAL_DIVERGENCE",
            "visible_divergence_preserved": True,
            "divergence_resolved": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
        },
        "selected_carrier_evidence": [
            {
                "selected_carrier_evidence_id": "carrier_b_successful_receipt_evidence_001",
                "carrier_id": "Carrier B",
                "carrier_evidence_outcome": "CARRIED_SURFACE_RECEIVED",
                "evidence_role": "successful_receipt_evidence",
                "successful_receipt_is_not_currentness": True,
            },
            {
                "selected_carrier_evidence_id": "carrier_c_blocked_receipt_evidence_001",
                "carrier_id": "Carrier C",
                "carrier_evidence_outcome": "BLOCKED",
                "evidence_role": "blocked_refusal_receipt_evidence",
                "refusal_preserved": True,
                "blocked_attempts_preserved": True,
            },
        ],
        "requested_divergence_consequence_posture": posture,
        "divergence_consequence_basis": {
            "basis_id": "divergence_consequence_basis_bc_001",
            "visible_divergence_preserved": True,
            "visible_refusal_preserved": True,
            "blocked_attempts_preserved": True,
            "projection_mismatch_visible": True,
            "detailed_basis_distinguished_from_summary": True,
            "summary_overrode_detailed_basis": False,
            "divergence_resolved": False,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "truth_created": False,
            "action_authorized": False,
            "currentness_created": False,
            "distributed_standing_created": False,
        },
        "currentness_successor_basis": {
            "basis_id": "cross_carrier_currentness_successor_bc_001",
            "outcome": "CROSS_CARRIER_CURRENTNESS_SUCCESSOR_RECORDED",
            "evidence_accounting_is_body_side_only": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "blocked_attempts_preserved": True,
            "projection_mismatch_preserved": True,
            "divergence_resolved": False,
            "carrier_currentness_created": False,
            "current_carrier_selected": False,
        },
        "carrier_continuity_turn_basis": {
            "basis_id": "carrier_continuity_turn_v2_bc_001",
            "outcome": "CARRIER_CONTINUITY_TURN_RECORDED",
            "projection_mismatch_visible": True,
            "blocked_attempts_preserved": True,
            "refusal_preserved": True,
            "divergence_preserved": True,
            "detailed_basis_distinguished_from_summary": True,
            "summary_overrode_detailed_basis": False,
            "latest_turn_currentness": False,
        },
        "standing_propagation_basis": {
            "basis_id": "standing_propagation_v2_bc_001",
            "outcome": "STANDING_PROPAGATION_POSTURE_RECORDED",
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "standing_propagation_decides_consequence": False,
        },
        "registry_persistence_basis": {
            "basis_id": "carrier_registry_persistence_v2_bc_001",
            "outcome": "CARRIER_REGISTRY_PERSISTENCE_REFERENCE_RECORDED",
            "reference_only": True,
            "registry_presence_decides_consequence": False,
            "latest_registry_reference_decides_consequence": False,
        },
        "lifecycle_basis": {
            "basis_id": "carrier_c_lifecycle_refused_or_blocked_001",
            "carrier_id": "Carrier C",
            "lifecycle_status": "CARRIER_REFUSED_OR_BLOCKED",
            "may_inform_caution": True,
            "does_not_invalidate_carrier_c": True,
            "does_not_select_winner": True,
        },
        "relation_conformance_closure_basis": {
            "basis_id": "carrier_b_c_relation_conformance_closure_001",
            "relation": "B/C divergence-bounded relation",
            "relation_conformance_outcome": "MULTI_CARRIER_RELATION_CONFORMED",
            "closure_outcome": "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
            "relation_basis_only": True,
            "closure_is_not_permission": True,
        },
        "visible_refusal_basis": {"refusal_preserved": True},
        "visible_divergence_basis": {"divergence_preserved": True},
        "blocked_attempt_basis": {"blocked_attempts_preserved": True},
        "projection_mismatch_basis": {"projection_mismatch_visible": True},
        "detailed_basis_reference": "divergence_consequence_basis.detailed",
        "summary_projection_reference": "divergence_consequence_summary",
        "consequence_scope": {
            "scope_statement": "Caution only for the declared prerequisite review question.",
            "declared_reliance_or_use_question": declared_use,
            "selected_divergence_affected": (
                "carrier_b_success__carrier_c_blocked_receipt_divergence_001"
            ),
            "selected_evidence_affected": [
                "carrier_b_successful_receipt_evidence_001",
                "carrier_c_blocked_receipt_evidence_001",
            ],
            "consequence_is_scoped_to_declared_use": True,
            "consequence_is_not_general_invalidation": True,
            "consequence_is_not_general_permission": True,
            "consequence_is_not_global_currentness_rule": True,
            "consequence_is_not_distributed_standing_rule": True,
            "separate_review_scheduled": False,
            "separate_review_authorized": False,
            "revalidation_scheduled": False,
            "revalidation_authorized": False,
            "evidence_remains_preserved_for_other_possible_future_uses": True,
        },
        "declared_non_claims": copy.deepcopy(resolver.REQUIRED_NON_CLAIMS),
    }


class CrossCarrierDivergenceConsequenceBoundaryTests(unittest.TestCase):
    def resolve(self, request: dict | None = None) -> dict:
        return resolver.resolve_cross_carrier_divergence_consequence_boundary(
            declared_divergence_consequence_request=copy.deepcopy(
                base_request() if request is None else request
            )
        )

    def assert_recorded(self, result: dict) -> None:
        self.assertEqual(result["outcome"], RECORDED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["divergence_consequence_summary"]["failed_check_count"], 0)
        self.assertTrue(result["consequence_statement"]["divergence_consequence_recorded"])

    def assert_block(self, request: dict | None, expected_code: str) -> dict:
        result = (
            resolver.resolve_cross_carrier_divergence_consequence_boundary()
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

    def test_successful_divergence_consequence_recording(self) -> None:
        result = self.resolve()

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assert_recorded(result)

        statement = result["consequence_statement"]
        for key in (
            "declared_reliance_or_use_question_preserved",
            "selected_divergence_evidence_preserved",
            "selected_divergence_evidence_outcome_preserved",
            "selected_carrier_evidence_preserved",
            "divergence_consequence_posture_preserved",
            "consequence_scope_preserved",
            "visible_divergence_preserved",
            "visible_refusal_preserved",
            "blocked_attempts_preserved",
            "projection_mismatch_preserved",
            "currentness_successor_basis_preserved",
            "carrier_continuity_turn_basis_preserved",
            "standing_propagation_basis_preserved",
            "registry_persistence_basis_preserved",
            "lifecycle_basis_preserved",
            "relation_conformance_closure_basis_preserved",
            "detailed_basis_distinguished_from_summary",
        ):
            self.assertTrue(statement[key], key)
        self.assert_statement_false_posture(statement)
        self.assertEqual(result["outcome"], RECORDED)

    def test_metadata_and_declared_question(self) -> None:
        result = self.resolve()
        metadata = result["divergence_consequence_metadata"]

        for key in (
            "divergence_consequence_result_id",
            "divergence_consequence_result_type",
            "divergence_consequence_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual(metadata["divergence_consequence_result_version"], "0.1.0")
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_cross_carrier_divergence_consequence_boundary",
        )

        question = result["declared_divergence_consequence_question"]
        self.assertEqual(
            question["divergence_consequence_request_id"],
            "divergence_consequence_bc_caution_001",
        )
        self.assertIn("visible B/C divergence", question["divergence_consequence_question"])
        self.assertEqual(question["divergence_consequence_intent"], resolver.RECORD_INTENT)
        self.assertEqual(
            result["divergence_consequence_posture"][
                "requested_divergence_consequence_posture"
            ],
            "DIVERGENCE_REQUIRES_CAUTION",
        )
        self.assertEqual(question["declared_non_claims"], resolver.REQUIRED_NON_CLAIMS)
        self.assertTrue(question["divergence_consequence_is_not_divergence_resolution"])
        self.assertTrue(question["divergence_consequence_is_not_truth"])
        self.assertTrue(question["divergence_consequence_is_not_action"])
        self.assertTrue(question["divergence_consequence_is_not_punishment"])
        self.assertTrue(question["divergence_consequence_is_not_currentness"])
        self.assertTrue(question["divergence_consequence_is_not_distributed_standing"])

    def test_reliance_divergence_and_carrier_evidence_sections(self) -> None:
        result = self.resolve()
        reliance = result["declared_reliance_or_use_question"]
        divergence = result["selected_divergence_evidence"]
        carrier = result["selected_carrier_evidence"]

        self.assertTrue(reliance["reliance_or_use_question_declared"])
        self.assertTrue(reliance["reliance_or_use_question_preserved"])
        self.assertTrue(reliance["consequence_scope_must_remain_declared_use_only"])
        self.assertTrue(reliance["consequence_is_not_general_invalidation"])
        self.assertTrue(reliance["consequence_is_not_general_permission"])

        self.assertEqual(
            divergence["selected_divergence_evidence_id"],
            "carrier_b_success__carrier_c_blocked_receipt_divergence_001",
        )
        self.assertEqual(
            divergence["selected_divergence_evidence_outcome"],
            "CARRIER_DIVERGENCE_RECORDED",
        )
        self.assertEqual(
            divergence["selected_divergence_evidence_type_or_class"],
            "RECEIPT_REFUSAL_DIVERGENCE",
        )
        self.assertTrue(divergence["selected_divergence_evidence_preserved"])
        self.assertTrue(divergence["divergence_remains_visible_not_resolved"])

        self.assertEqual(carrier["selected_carrier_evidence_count"], 2)
        self.assertIn(
            "carrier_b_successful_receipt_evidence_001",
            carrier["selected_carrier_evidence_ids"],
        )
        self.assertIn(
            "carrier_c_blocked_receipt_evidence_001",
            carrier["selected_carrier_evidence_ids"],
        )
        self.assertIn("CARRIED_SURFACE_RECEIVED", carrier["selected_carrier_evidence_outcomes"])
        self.assertIn("BLOCKED", carrier["selected_carrier_evidence_outcomes"])
        self.assertTrue(carrier["carrier_evidence_remains_evidence"])
        self.assertTrue(carrier["carrier_evidence_does_not_become_currentness"])
        self.assertTrue(carrier["carrier_evidence_does_not_select_winner_or_loser"])

    def test_basis_sections_posture_and_scope(self) -> None:
        result = self.resolve()

        for section_name in (
            "currentness_successor_basis",
            "carrier_continuity_turn_basis",
            "standing_propagation_basis",
            "registry_persistence_basis",
            "lifecycle_basis",
            "relation_conformance_closure_basis",
        ):
            section = result[section_name]
            self.assertTrue(section[f"{section_name}_declared"], section_name)
            self.assertTrue(section[f"{section_name}_preserved"], section_name)
            self.assertTrue(section["basis_preserved_where_supplied"], section_name)
            self.assertTrue(section["basis_does_not_decide_consequence_by_itself"])

        self.assertEqual(
            result["lifecycle_basis"]["raw_lifecycle_basis"]["lifecycle_status"],
            "CARRIER_REFUSED_OR_BLOCKED",
        )
        self.assertTrue(
            result["carrier_continuity_turn_basis"]["raw_carrier_continuity_turn_basis"][
                "projection_mismatch_visible"
            ]
        )
        self.assertTrue(
            result["standing_propagation_basis"]["raw_standing_propagation_basis"][
                "visible_divergence_preserved"
            ]
        )
        self.assertTrue(
            result["registry_persistence_basis"]["raw_registry_persistence_basis"][
                "reference_only"
            ]
        )

        posture = result["divergence_consequence_posture"]
        self.assertTrue(posture["divergence_consequence_posture_supported"])
        self.assertTrue(posture["divergence_consequence_posture_preserved"])
        self.assertTrue(posture["posture_is_bounded_reliance_effect"])
        self.assertTrue(posture["posture_is_not_truth_action_currentness_or_distributed_standing"])

        scope = result["consequence_scope"]
        self.assertTrue(scope["consequence_scope_declared"])
        self.assertTrue(scope["consequence_scope_preserved"])
        self.assertTrue(scope["consequence_is_scoped_not_general_invalidation"])
        self.assertTrue(scope["consequence_is_not_general_permission"])
        self.assertTrue(scope["consequence_is_not_global_currentness_rule"])
        self.assertTrue(scope["consequence_is_not_distributed_standing_rule"])
        self.assertTrue(
            scope[
                "may_block_limit_caution_exclude_revalidate_or_require_separate_review_for_declared_use_only"
            ]
        )
        self.assertFalse(scope["separate_review_scheduled"])
        self.assertFalse(scope["separate_review_authorized"])
        self.assertFalse(scope["revalidation_scheduled"])
        self.assertFalse(scope["revalidation_authorized"])
        self.assertTrue(scope["evidence_remains_preserved_for_other_possible_future_uses"])

    def test_consequence_checks_are_explicit_and_pass(self) -> None:
        result = self.resolve()
        checks = result["consequence_checks"]
        self.assertTrue(checks)
        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertTrue(check["passed"], check)
        self.assertEqual(result["divergence_consequence_summary"]["failed_check_count"], 0)
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({c["check_name"] for c in checks}))

    def test_consequence_non_meaning_and_open_surfaces(self) -> None:
        result = self.resolve()
        non_meaning = result["consequence_non_meaning"]
        remains_open = result["what_remains_open"]

        for key in NON_MEANING_TRUE_KEYS:
            self.assertIn(key, non_meaning)
            self.assertTrue(non_meaning[key], key)
        for key in OPEN_TRUE_KEYS:
            self.assertIn(key, remains_open)
            self.assertTrue(remains_open[key], key)

    def test_summary_helper_projects_result(self) -> None:
        result = self.resolve()
        summary = resolver.build_cross_carrier_divergence_consequence_summary(result)

        self.assertEqual(summary["outcome"], RECORDED)
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(
            summary["divergence_consequence_request_id"],
            "divergence_consequence_bc_caution_001",
        )
        self.assertIn("visible B/C divergence", summary["divergence_consequence_question"])
        self.assertEqual(summary["divergence_consequence_intent"], resolver.RECORD_INTENT)
        self.assertIn("distributed-standing", summary["declared_reliance_or_use_question"])
        self.assertEqual(
            summary["requested_divergence_consequence_posture"],
            "DIVERGENCE_REQUIRES_CAUTION",
        )
        self.assertEqual(
            summary["selected_divergence_evidence_id"],
            "carrier_b_success__carrier_c_blocked_receipt_divergence_001",
        )
        self.assertEqual(
            summary["selected_divergence_evidence_outcome"],
            "CARRIER_DIVERGENCE_RECORDED",
        )
        self.assertIn(
            "carrier_b_successful_receipt_evidence_001",
            summary["selected_carrier_evidence_ids"],
        )
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["divergence_consequence_recorded"])
        self.assertTrue(summary["consequence_scope_preserved"])
        self.assertTrue(summary["visible_divergence_preserved"])
        self.assertTrue(summary["visible_refusal_preserved"])
        self.assertTrue(summary["blocked_attempts_preserved"])
        self.assertTrue(summary["projection_mismatch_preserved"])
        self.assertTrue(summary["currentness_successor_basis_preserved"])
        self.assertTrue(summary["carrier_continuity_turn_basis_preserved"])
        self.assertTrue(summary["standing_propagation_basis_preserved"])
        self.assertTrue(summary["registry_persistence_basis_preserved"])
        self.assertTrue(summary["lifecycle_basis_preserved"])
        self.assertTrue(summary["relation_conformance_closure_basis_preserved"])
        self.assertTrue(summary["detailed_basis_distinguished_from_summary"])
        self.assertFalse(summary["summary_overrode_detailed_basis"])
        self.assertFalse(summary["divergence_resolved"])
        self.assertFalse(summary["winning_carrier_selected"])
        self.assertFalse(summary["losing_carrier_invalidated"])
        self.assertTrue(summary["no_carrier_currentness_current_carrier_source_authority_permission"])
        self.assertTrue(summary["no_truth_action"])
        self.assertTrue(summary["no_carrier_hierarchy"])
        self.assertTrue(summary["no_evidence_erasure"])
        self.assertTrue(summary["no_distributed_standing"])
        self.assertTrue(summary["no_sync_full_body_transfer_second_body"])
        self.assertTrue(summary["no_continuation"])
        self.assertTrue(summary["no_distributed_operation"])
        self.assertTrue(summary["no_latest_file_turn_majority_success_count_consequence"])
        self.assertTrue(summary["key_non_claims"]["required_non_claims_preserved"])

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        recorded = self.resolve()
        not_recorded = self.resolve(
            base_request(intent="DO_NOT_RECORD_DIVERGENCE_CONSEQUENCE")
        )
        blocked = self.resolve(base_request(intent="BLOCK_DIVERGENCE_CONSEQUENCE"))

        for result in (recorded, not_recorded, blocked):
            self.assertIn(result["outcome"], {RECORDED, NOT_RECORDED, BLOCKED})
            self.assert_required_non_claims_false(result)

    def test_supported_divergence_consequence_postures_record(self) -> None:
        for posture in sorted(resolver.SUPPORTED_DIVERGENCE_CONSEQUENCE_POSTURES):
            with self.subTest(posture=posture):
                result = self.resolve(base_request(posture=posture))
                self.assertEqual(result["outcome"], RECORDED)

    def test_request_builder_helper(self) -> None:
        request = resolver.build_declared_cross_carrier_divergence_consequence_request(
            divergence_consequence_request_id="builder_divergence_consequence_001",
            divergence_consequence_question="What effect may selected divergence have?",
            declared_reliance_or_use_question="May this evidence support a future review?",
            selected_divergence_evidence=base_request()["selected_divergence_evidence"],
            requested_divergence_consequence_posture="DIVERGENCE_LIMITS_RELIANCE",
            divergence_consequence_basis=base_request()["divergence_consequence_basis"],
            selected_carrier_evidence=base_request()["selected_carrier_evidence"],
            currentness_successor_basis=base_request()["currentness_successor_basis"],
            carrier_continuity_turn_basis=base_request()["carrier_continuity_turn_basis"],
            standing_propagation_basis=base_request()["standing_propagation_basis"],
            registry_persistence_basis=base_request()["registry_persistence_basis"],
            lifecycle_basis=base_request()["lifecycle_basis"],
            relation_conformance_closure_basis=base_request()[
                "relation_conformance_closure_basis"
            ],
            consequence_scope=base_request()["consequence_scope"],
        )

        self.assertEqual(request["divergence_consequence_request_id"], "builder_divergence_consequence_001")
        self.assertEqual(request["divergence_consequence_question"], "What effect may selected divergence have?")
        self.assertEqual(request["declared_reliance_or_use_question"], "May this evidence support a future review?")
        self.assertEqual(
            request["requested_divergence_consequence_posture"],
            "DIVERGENCE_LIMITS_RELIANCE",
        )
        self.assertEqual(
            request["selected_divergence_evidence"],
            base_request()["selected_divergence_evidence"],
        )
        self.assertEqual(request["declared_non_claims"], resolver.REQUIRED_NON_CLAIMS)

        result = self.resolve(request)
        self.assert_recorded(result)

    def test_path_based_resolution(self) -> None:
        request = base_request()
        mapping_result = self.resolve(request)

        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "declared_divergence_consequence_request.json"
            path.write_text(json.dumps(request), encoding="utf-8")

            path_result = resolver.resolve_cross_carrier_divergence_consequence_boundary_from_path(
                path
            )

        self.assert_recorded(path_result)
        self.assertEqual(set(path_result), set(mapping_result))
        self.assertTrue(
            path_result["declared_divergence_consequence_question"]["request_path"].endswith(
                "declared_divergence_consequence_request.json"
            )
        )

    def test_write_behavior_and_default_output_path(self) -> None:
        result = self.resolve()

        with tempfile.TemporaryDirectory() as tmp:
            explicit_path = Path(tmp) / "nested" / "result.json"
            written = resolver.write_cross_carrier_divergence_consequence_result(
                result, explicit_path
            )
            self.assertEqual(written, explicit_path)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            default_root = Path(tmp) / "bounded_default_root"
            with patch.object(
                resolver,
                "CROSS_CARRIER_DIVERGENCE_CONSEQUENCE_BOUNDARY_ROOT",
                default_root,
            ):
                first = resolver.write_cross_carrier_divergence_consequence_result(result)
                second = resolver.write_cross_carrier_divergence_consequence_result(result)

            self.assertEqual(first.parent, default_root)
            self.assertEqual(second.parent, default_root)
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertIn("__cross_carrier_divergence_consequence_result", first.name)
            self.assertIn("__cross_carrier_divergence_consequence_result", second.name)

    def test_non_mutation_posture(self) -> None:
        request = base_request()
        original = copy.deepcopy(request)
        selected_divergence = request["selected_divergence_evidence"]
        selected_carrier = request["selected_carrier_evidence"]
        bases = {
            key: request[key]
            for key in (
                "currentness_successor_basis",
                "carrier_continuity_turn_basis",
                "standing_propagation_basis",
                "registry_persistence_basis",
                "lifecycle_basis",
                "relation_conformance_closure_basis",
            )
        }

        result = self.resolve(request)
        second = self.resolve(request)

        self.assertEqual(request, original)
        self.assertEqual(selected_divergence, original["selected_divergence_evidence"])
        self.assertEqual(selected_carrier, original["selected_carrier_evidence"])
        for key, value in bases.items():
            self.assertEqual(value, original[key])
        self.assertEqual(result["outcome"], second["outcome"])

        before_write = copy.deepcopy(result)
        with tempfile.TemporaryDirectory() as tmp:
            resolver.write_cross_carrier_divergence_consequence_result(
                result, Path(tmp) / "result.json"
            )
        self.assertEqual(result, before_write)

    def test_not_recorded_readable_request(self) -> None:
        result = self.resolve(base_request(intent="DO_NOT_RECORD_DIVERGENCE_CONSEQUENCE"))

        self.assertEqual(result["outcome"], NOT_RECORDED)
        self.assertFalse(result["consequence_statement"]["divergence_consequence_recorded"])
        self.assertEqual(
            result["declared_divergence_consequence_question"]["not_recorded_reason"],
            "declared request does not record divergence consequence posture",
        )
        self.assert_statement_false_posture(result["consequence_statement"])

    def test_explicit_block_intent(self) -> None:
        result = self.resolve(base_request(intent="BLOCK_DIVERGENCE_CONSEQUENCE"))

        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "DIVERGENCE_CONSEQUENCE_REQUEST_EXPLICITLY_BLOCKED",
        )
        self.assertFalse(result["consequence_statement"]["divergence_consequence_recorded"])

    def test_blocking_missing_and_malformed_request(self) -> None:
        self.assert_block(None, "DIVERGENCE_CONSEQUENCE_QUESTION_UNDECLARED")
        result = resolver.resolve_cross_carrier_divergence_consequence_boundary(
            declared_divergence_consequence_request=["not", "a", "mapping"]
        )
        self.assertEqual(result["outcome"], BLOCKED)
        self.assertEqual(
            result["block"]["block_code"],
            "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
        )

    def test_blocking_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            missing_result = resolver.resolve_cross_carrier_divergence_consequence_boundary_from_path(
                missing
            )
            self.assertEqual(
                missing_result["block"]["block_code"],
                "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_UNREADABLE",
            )

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{not json", encoding="utf-8")
            malformed_result = (
                resolver.resolve_cross_carrier_divergence_consequence_boundary_from_path(
                    malformed
                )
            )
            self.assertEqual(
                malformed_result["block"]["block_code"],
                "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
            )

            array_path = Path(tmp) / "array.json"
            array_path.write_text(json.dumps([]), encoding="utf-8")
            array_result = (
                resolver.resolve_cross_carrier_divergence_consequence_boundary_from_path(
                    array_path
                )
            )
            self.assertEqual(
                array_result["block"]["block_code"],
                "DECLARED_DIVERGENCE_CONSEQUENCE_REQUEST_MALFORMED",
            )

    def test_blocking_question_intent_posture(self) -> None:
        request = base_request()
        request.pop("divergence_consequence_question")
        self.assert_block(request, "DIVERGENCE_CONSEQUENCE_QUESTION_UNDECLARED")

        request = base_request(intent="UNSUPPORTED")
        self.assert_block(request, "DIVERGENCE_CONSEQUENCE_INTENT_UNSUPPORTED")

        request = base_request(posture="UNSUPPORTED_POSTURE")
        self.assert_block(request, "DIVERGENCE_CONSEQUENCE_POSTURE_UNSUPPORTED")

    def test_blocking_reliance_and_divergence_evidence(self) -> None:
        request = base_request()
        request.pop("declared_reliance_or_use_question")
        self.assert_block(request, "RELIANCE_OR_USE_QUESTION_MISSING")

        request = base_request()
        request.pop("selected_divergence_evidence")
        self.assert_block(request, "SELECTED_DIVERGENCE_EVIDENCE_MISSING")

        request = base_request()
        request["selected_divergence_evidence"] = ["malformed"]
        self.assert_block(request, "SELECTED_DIVERGENCE_EVIDENCE_MALFORMED")

        request = base_request()
        request["selected_divergence_evidence"].pop("selected_divergence_evidence_outcome")
        self.assert_block(request, "SELECTED_DIVERGENCE_EVIDENCE_OUTCOME_MISSING")

    def test_blocking_missing_bases(self) -> None:
        request = base_request()
        request["divergence_consequence_basis"]["selected_carrier_evidence_required"] = True
        request.pop("selected_carrier_evidence")
        self.assert_block(request, "SELECTED_CARRIER_EVIDENCE_MISSING")

        request = base_request()
        request.pop("divergence_consequence_basis")
        self.assert_block(request, "DIVERGENCE_CONSEQUENCE_BASIS_MISSING")

        request = base_request()
        request["divergence_consequence_basis"][
            "currentness_successor_basis_required"
        ] = True
        request.pop("currentness_successor_basis")
        self.assert_block(request, "CURRENTNESS_SUCCESSOR_BASIS_MISSING")

        request = base_request()
        request["divergence_consequence_basis"][
            "carrier_continuity_turn_basis_required"
        ] = True
        request.pop("carrier_continuity_turn_basis")
        self.assert_block(request, "CARRIER_CONTINUITY_TURN_BASIS_MISSING")

        request = base_request()
        request["divergence_consequence_basis"][
            "lifecycle_registry_propagation_basis_required"
        ] = True
        request.pop("lifecycle_basis")
        request.pop("registry_persistence_basis")
        request.pop("standing_propagation_basis")
        self.assert_block(request, "LIFECYCLE_REGISTRY_PROPAGATION_BASIS_MISSING")

        request = base_request()
        request["divergence_consequence_basis"][
            "relation_conformance_closure_basis_required"
        ] = True
        request.pop("relation_conformance_closure_basis")
        self.assert_block(request, "RELATION_CONFORMANCE_CLOSURE_BASIS_MISSING")

        request = base_request()
        request.pop("consequence_scope")
        self.assert_block(request, "CONSEQUENCE_SCOPE_MISSING")

    def test_blocking_hidden_visibility_and_summary_override(self) -> None:
        for field, code in (
            ("visible_divergence_hidden", "DIVERGENCE_CONSEQUENCE_HIDES_DIVERGENCE"),
            ("visible_refusal_hidden", "DIVERGENCE_CONSEQUENCE_HIDES_REFUSAL"),
            ("blocked_attempt_hidden", "DIVERGENCE_CONSEQUENCE_HIDES_BLOCKED_ATTEMPT"),
            (
                "projection_mismatch_hidden",
                "DIVERGENCE_CONSEQUENCE_HIDES_PROJECTION_MISMATCH",
            ),
            ("summary_overrode_detailed_basis", "SUMMARY_OVERWRITES_DETAILED_BASIS"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["divergence_consequence_basis"][field] = True
                self.assert_block(request, code)

    def test_blocking_resolves_selects_invalidates(self) -> None:
        for field, code in (
            ("divergence_resolved", "DIVERGENCE_CONSEQUENCE_RESOLVES_DIVERGENCE"),
            ("winning_carrier_selected", "DIVERGENCE_CONSEQUENCE_SELECTS_WINNER"),
            ("losing_carrier_invalidated", "DIVERGENCE_CONSEQUENCE_INVALIDATES_LOSER"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_currentness_current_source_authority_permission(self) -> None:
        for field, code in (
            (
                "carrier_currentness_created",
                "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_CURRENTNESS",
            ),
            ("current_carrier_selected", "DIVERGENCE_CONSEQUENCE_SELECTS_CURRENT_CARRIER"),
            ("source_replaced", "DIVERGENCE_CONSEQUENCE_REPLACES_SOURCE"),
            ("authority_created", "DIVERGENCE_CONSEQUENCE_CREATES_AUTHORITY"),
            ("permission_created", "DIVERGENCE_CONSEQUENCE_CREATES_PERMISSION"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_truth_action_hierarchy_evidence(self) -> None:
        for field, code in (
            ("truth_created", "DIVERGENCE_CONSEQUENCE_CREATES_TRUTH"),
            ("action_authorized", "DIVERGENCE_CONSEQUENCE_AUTHORIZES_ACTION"),
            (
                "divergence_consequence_created_carrier_hierarchy",
                "DIVERGENCE_CONSEQUENCE_CREATES_CARRIER_HIERARCHY",
            ),
            (
                "divergence_consequence_erased_evidence",
                "DIVERGENCE_CONSEQUENCE_ERASES_EVIDENCE",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_distributed_sync_transfer_second_body(self) -> None:
        for field, code in (
            (
                "distributed_standing_created",
                "DIVERGENCE_CONSEQUENCE_CREATES_DISTRIBUTED_STANDING",
            ),
            (
                "repository_synchronization_authorized",
                "DIVERGENCE_CONSEQUENCE_AUTHORIZES_REPOSITORY_SYNC",
            ),
            (
                "full_body_transfer_authorized",
                "DIVERGENCE_CONSEQUENCE_AUTHORIZES_FULL_BODY_TRANSFER",
            ),
            ("second_body_created", "DIVERGENCE_CONSEQUENCE_CREATES_SECOND_BODY"),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_continuation_distributed_operation(self) -> None:
        for field, code in (
            ("continuation_authorized", "DIVERGENCE_CONSEQUENCE_AUTHORIZES_CONTINUATION"),
            (
                "distributed_operation_authorized",
                "DIVERGENCE_CONSEQUENCE_AUTHORIZES_DISTRIBUTED_OPERATION",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_latest_majority_success_count_consequence(self) -> None:
        for field, code in (
            ("latest_file_consequence", "LATEST_FILE_OR_TURN_CONSEQUENCE"),
            ("latest_turn_consequence", "LATEST_FILE_OR_TURN_CONSEQUENCE"),
            ("majority_carrier_consequence", "MAJORITY_OR_SUCCESS_COUNT_CONSEQUENCE"),
            (
                "successful_receipt_count_consequence",
                "MAJORITY_OR_SUCCESS_COUNT_CONSEQUENCE",
            ),
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(request, code)

    def test_blocking_registry_lifecycle_propagation_turn_consequence(self) -> None:
        for field in (
            "registry_record_consequence",
            "lifecycle_status_consequence",
            "standing_propagation_consequence",
            "continuity_turn_consequence",
        ):
            with self.subTest(field=field):
                request = base_request()
                request["declared_non_claims"][field] = True
                self.assert_block(
                    request,
                    "REGISTRY_LIFECYCLE_PROPAGATION_OR_TURN_CONSEQUENCE",
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
                "DIVERGENCE_CONSEQUENCE_CREATES_PERMISSION",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            },
        )
        self.assertIn("raw_declared_non_claims", result["non_claims"])
        self.assertTrue(result["non_claims"]["raw_declared_non_claims"])


if __name__ == "__main__":
    unittest.main()
