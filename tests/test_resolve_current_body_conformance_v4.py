"""Bounded tests for current-body conformance v4.

These tests audit one surface only: current-body conformance v4 for a selected
current self-orientation v9 result. V4 checks whether v9 conforms to the
current body line after distributed standing boundary conformance closure. It
must not mutate v9, create v10, create v4 closure, authorize continuation or
operation, synchronize repositories, transfer the body, create a second body,
create permission or authority, create truth/action, claim final completion, or
schedule follow-on work.
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

import resolve_current_body_conformance_v4 as resolver  # noqa: E402


CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_CONFORMANT"
NOT_CONFORMANT = "CURRENT_BODY_CONFORMANCE_V4_NOT_CONFORMANT"
BLOCKED = "CURRENT_BODY_CONFORMANCE_V4_BLOCKED"
RECORDED = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
OUTCOME_FAMILY = {CONFORMANT, NOT_CONFORMANT, BLOCKED}

V9_ID = "current_self_orientation_v9_after_distributed_standing_boundary_conformance_closure_001"
REQUEST_ID = "current_body_conformance_v4_001"

TOP_LEVEL_SECTIONS = {
    "current_body_conformance_v4_metadata",
    "declared_conformance_question",
    "selected_current_self_orientation_v9",
    "current_body_conformance_v4_basis",
    "v9_orientation_conformance",
    "basis_preservation_conformance",
    "non_claim_conformance",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "current_body_conformance_v4_summary",
}

RESULT_NON_CLAIMS = set(resolver.REQUIRED_NON_CLAIMS)

CONFORMANCE_NON_MEANING_KEYS = {
    "continuation",
    "operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body",
    "distributed_standing_implementation",
    "distributed_operation",
    "final_completion",
    "final_governance",
    "final_continuity_completion",
    "final_system_identity",
    "public_launch_readiness",
    "permission",
    "authority",
    "truth",
    "action",
    "currentness",
    "carrier_currentness",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replacement",
    "divergence_resolution",
    "evidence_erasure",
    "current_self_orientation_v10",
    "current_body_conformance_v4_closure_by_default",
    "follow_on_work_authorization",
}

OPEN_KEYS = {
    "current_body_conformance_v4_closure",
    "any_future_self_orientation_successor_beyond_v9",
    "distributed_standing_implementation",
    "distributed_operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body_creation",
    "carrier_registry_implementation",
    "persistence_implementation",
    "standing_propagation_implementation_beyond_boundary_recording",
    "truth_law",
    "action_consequence_law",
    "presence_law",
    "threshold_law",
    "body_relevance_medium",
    "signal_series_or_accumulation_logic",
    "public_launch_readiness",
    "open_means_not_scheduled",
    "open_means_not_authorized",
    "open_means_not_executed",
}


def required_non_claims() -> dict:
    return copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)


def selected_v9_non_claims() -> dict:
    return {key: False for key in resolver.SELECTED_V9_REQUIRED_NON_CLAIMS}


def orientation_statement() -> dict:
    return {
        "current_self_orientation_v9_recorded": True,
        "prior_self_orientation_preserved": True,
        "v8_preserved_as_lineage": True,
        "distributed_standing_conformance_closure_preserved": True,
        "distributed_standing_conformance_closure_closed": True,
        "distributed_standing_conformance_closure_failed_check_count_zero": True,
        "current_body_conformance_v3_closure_basis_preserved": True,
        "what_stands_preserved": True,
        "what_does_not_stand_preserved": True,
        "what_is_closed_preserved": True,
        "what_remains_open_preserved": True,
        "orientation_did_not_create_permission": True,
        "orientation_did_not_authorize_continuation": True,
        "orientation_did_not_authorize_operation": True,
        "orientation_did_not_authorize_repository_sync": True,
        "orientation_did_not_authorize_full_body_transfer": True,
        "orientation_did_not_create_second_body": True,
        "orientation_did_not_claim_final_completion": True,
        "orientation_did_not_schedule_follow_on_work": True,
        "orientation_did_not_mutate_prior_result": True,
        "permission_created": False,
        "continuation_authorized": False,
        "distributed_operation_authorized": False,
        "repository_synchronization_authorized": False,
        "full_body_transfer_authorized": False,
        "second_body_created": False,
        "truth_created": False,
        "action_authorized": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "self_orientation_successor_scheduled": False,
        "prior_result_mutated": False,
    }


def orientation_non_meaning() -> dict:
    return {
        "permission": True,
        "continuation": True,
        "operation": True,
        "repository_synchronization": True,
        "full_body_transfer": True,
        "second_body": True,
        "distributed_operation": True,
        "implementation": True,
        "final_completion": True,
        "final_governance": True,
        "final_continuity_completion": True,
        "final_system_identity": True,
        "public_launch_readiness": True,
        "carrier_currentness": True,
        "current_carrier_selected": True,
        "winning_carrier_selected": True,
        "losing_carrier_invalidated": True,
        "source_replacement": True,
        "authority": True,
        "truth": True,
        "action": True,
        "divergence_resolution": True,
        "evidence_erasure": True,
        "prior_result_mutation": True,
        "follow_on_work_authorization": True,
        "self_orientation_successor_beyond_v9": True,
    }


def v9_orientation_basis() -> dict:
    return {
        "current_self_orientation_v8": "current_self_orientation_v8_001",
        "current_body_conformance_v3_closure": "current_body_conformance_v3_closure_001",
        "distributed_standing_boundary_result": "carrier_b_c_distributed_standing_boundary_001",
        "distributed_standing_boundary_conformance_result": "carrier_b_c_distributed_standing_boundary_conformance_001",
        "distributed_standing_boundary_conformance_closure": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
        "divergence_consequence": "cross-carrier divergence consequence",
        "currentness_successor": "cross-carrier currentness successor",
        "continuity_turn_v2": "carrier continuity-turn v2",
        "standing_propagation_v2": "standing propagation v2",
        "registry_persistence_v2": "carrier registry/persistence v2",
        "lifecycle_posture": "Carrier C lifecycle posture",
        "b_c_divergence": True,
        "carrier_b_success": True,
        "carrier_c_block": True,
        "visible_refusal": True,
        "blocked_attempts": True,
        "projection_mismatch": True,
        "relation_conformance_closure_basis": True,
        "basis_only_not_operation": True,
        "basis_only_not_continuation": True,
        "basis_only_not_final_completion": True,
    }


def selected_v9() -> dict:
    statement = orientation_statement()
    return {
        "current_self_orientation_v9_metadata": {
            "current_self_orientation_v9_result_id": V9_ID,
            "current_self_orientation_v9_result_type": "current_self_orientation_v9_result",
            "current_self_orientation_v9_result_version": "0.1.0",
            "generated_at": "2026-04-30T00:00:00+00:00",
            "resolver_module": "resolve_current_self_orientation_v9",
        },
        "declared_orientation_question": {
            "orientation_request_id": V9_ID,
            "orientation_question": "What is the body's current orientation after distributed standing boundary conformance closure?",
            "orientation_intent": "RECORD_CURRENT_SELF_ORIENTATION_V9",
        },
        "selected_prior_self_orientation": {
            "selected_prior_self_orientation_id": "current_self_orientation_v8_001",
            "selected_prior_self_orientation_outcome": "SELF_ORIENTED",
            "v8_preserved_as_lineage": True,
            "v8_erased": False,
            "v8_mutated": False,
        },
        "selected_distributed_standing_conformance_closure": {
            "selected_conformance_closure_id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            "selected_conformance_closure_outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED",
            "selected_conformance_closure_failed_check_count": 0,
            "selected_conformance_closure_failed_check_count_zero": True,
            "selected_conformance_closure_closed": True,
            "closure_did_not_authorize_continuation": True,
            "closure_did_not_authorize_operation": True,
            "closure_did_not_authorize_repository_sync": True,
            "closure_did_not_authorize_full_body_transfer": True,
            "closure_did_not_create_second_body": True,
            "closure_did_not_schedule_self_orientation_successor": True,
            "closure_did_not_claim_final_completion": True,
        },
        "orientation_basis": v9_orientation_basis(),
        "what_stands": {
            "what_stands_preserved": True,
            "current_self_orientation_v8_remains_lineage": True,
            "current_body_conformance_v3_closure_remains_basis": True,
            "distributed_standing_boundary_result_stands_as_bounded_body_side_posture_recording": True,
            "distributed_standing_boundary_conformance_stands_as_conformance": True,
            "distributed_standing_boundary_conformance_closure_stands_as_closure_of_conformance_meaning": True,
            "bounded_form_only": True,
            "does_not_combine_into_operation": True,
            "does_not_combine_into_continuation": True,
            "does_not_combine_into_synchronization": True,
            "does_not_combine_into_full_body_transfer": True,
            "does_not_combine_into_final_completion": True,
        },
        "what_does_not_stand": {
            "what_does_not_stand_preserved": True,
            "distributed_operation_does_not_stand": True,
            "repository_synchronization_does_not_stand": True,
            "full_body_transfer_does_not_stand": True,
            "second_body_does_not_stand": True,
            "continuation_does_not_stand": True,
            "carrier_currentness_does_not_stand": True,
            "current_carrier_selection_does_not_stand": True,
            "winning_carrier_selection_does_not_stand": True,
            "losing_carrier_invalidation_does_not_stand": True,
            "source_replacement_does_not_stand": True,
            "authority_creation_does_not_stand": True,
            "permission_creation_does_not_stand": True,
            "truth_action_does_not_stand": True,
            "final_governance_does_not_stand": True,
            "final_continuity_completion_does_not_stand": True,
            "final_system_identity_completion_does_not_stand": True,
            "public_launch_readiness_does_not_stand": True,
            "self_orientation_successor_beyond_v9_does_not_stand": True,
        },
        "what_is_closed": {
            "what_is_closed_preserved": True,
            "current_orientation_to_distributed_standing_boundary_conformance_closure_closed": True,
            "distributed_standing_boundary_conformance_closure_stands_as_closed_meaning": True,
            "closure_non_meaning_does_not_authorize_operation_or_continuation_closed": True,
            "v8_is_prior_orientation_lineage_not_latest_orientation": True,
            "orientation_closure_only": True,
            "not_closure_of_distributed_standing_implementation": True,
            "not_closure_of_operation": True,
            "not_closure_of_final_governance": True,
            "not_closure_of_final_continuity_completion": True,
            "not_closure_of_final_system_identity": True,
        },
        "what_remains_open": {
            "what_remains_open_preserved": True,
            "current_self_orientation_v9_implementation_refinement": "open_not_scheduled_not_authorized_not_executed",
            "any_future_self_orientation_successor_beyond_v9": "open_not_scheduled_not_authorized_not_executed",
            "distributed_standing_implementation": "open_not_scheduled_not_authorized_not_executed",
            "distributed_operation": "open_not_scheduled_not_authorized_not_executed",
            "repository_synchronization": "open_not_scheduled_not_authorized_not_executed",
            "full_body_transfer": "open_not_scheduled_not_authorized_not_executed",
            "second_body_creation": "open_not_scheduled_not_authorized_not_executed",
            "truth_law": "open_not_scheduled_not_authorized_not_executed",
            "action_consequence_law": "open_not_scheduled_not_authorized_not_executed",
            "presence_law": "open_not_scheduled_not_authorized_not_executed",
            "threshold_law": "open_not_scheduled_not_authorized_not_executed",
            "public_launch_readiness": "open_not_scheduled_not_authorized_not_executed",
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
        },
        "orientation_checks": [
            {
                "check_name": "synthetic v9 orientation check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
            }
        ],
        "orientation_statement": statement,
        "orientation_non_meaning": orientation_non_meaning(),
        "non_claims": selected_v9_non_claims(),
        "outcome": RECORDED,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "current_self_orientation_v9_summary": {
            **statement,
            "outcome": RECORDED,
            "orientation_request_id": V9_ID,
            "current_self_orientation_v9_result_id": V9_ID,
            "passed_check_count": 30,
            "failed_check_count": 0,
        },
    }


def conformance_basis() -> dict:
    return {
        "selected_current_self_orientation_v9": V9_ID,
        "selected_distributed_standing_boundary_conformance_closure": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
        "selected_current_body_conformance_v3_closure": "current_body_conformance_v3_closure_001",
        "current_self_orientation_v8_as_lineage": "current_self_orientation_v8_001",
        "distributed_standing_boundary_result": "carrier_b_c_distributed_standing_boundary_001",
        "distributed_standing_boundary_conformance_result": "carrier_b_c_distributed_standing_boundary_conformance_001",
        "divergence_consequence_result": "cross_carrier_divergence_consequence_001",
        "currentness_successor_result": "cross_carrier_currentness_successor_001",
        "continuity_turn_v2_result": "carrier_continuity_turn_v2_001",
        "standing_propagation_v2_result": "standing_propagation_v2_001",
        "registry_persistence_v2_result": "carrier_registry_persistence_v2_001",
        "lifecycle_result": "carrier_lifecycle_001",
        "b_c_divergence": True,
        "carrier_b_success": True,
        "carrier_c_block": True,
        "relation_conformance_closure_basis": True,
        "basis_is_not_permission_set": True,
        "basis_is_not_operation_plan": True,
    }


def valid_request(
    *,
    v9: dict | None = None,
    intent: str = "RECORD_CURRENT_BODY_CONFORMANCE_V4",
    selected_current_self_orientation_v9_path: str | None = None,
) -> dict:
    selected = selected_v9() if v9 is None else v9
    request = resolver.build_declared_current_body_conformance_v4_request(
        REQUEST_ID,
        "Does current self-orientation v9 conform to the current body line?",
        copy.deepcopy(selected),
        conformance_basis(),
        conformance_intent=intent,
        selected_current_self_orientation_v9_path=selected_current_self_orientation_v9_path,
        selected_current_self_orientation_v9_id=V9_ID,
        selected_current_self_orientation_v9_outcome=RECORDED,
        expected_selected_v9_outcome=RECORDED,
    )
    request.update(
        {
            "selected_prior_self_orientation_v8": {"id": "current_self_orientation_v8_001"},
            "selected_distributed_standing_conformance_closure": {
                "id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001"
            },
            "current_body_conformance_v3_closure_basis": {
                "id": "current_body_conformance_v3_closure_001"
            },
            "distributed_standing_boundary_reference": {
                "id": "carrier_b_c_distributed_standing_boundary_001"
            },
            "distributed_standing_boundary_conformance_reference": {
                "id": "carrier_b_c_distributed_standing_boundary_conformance_001"
            },
            "divergence_consequence_reference": {
                "id": "cross_carrier_divergence_consequence_001"
            },
            "currentness_successor_reference": {
                "id": "cross_carrier_currentness_successor_001"
            },
            "continuity_turn_v2_reference": {"id": "carrier_continuity_turn_v2_001"},
            "standing_propagation_v2_reference": {"id": "standing_propagation_v2_001"},
            "registry_persistence_v2_reference": {
                "id": "carrier_registry_persistence_v2_001"
            },
            "lifecycle_reference": {"id": "carrier_lifecycle_001"},
            "relation_conformance_closure_reference": {
                "id": "relation_conformance_closure_001"
            },
            "b_c_divergence": {"preserved": True},
            "carrier_b_success": {"preserved": True},
            "carrier_c_block": {"preserved": True},
            "conformance_scope": "current-body conformance v4 only",
        }
    )
    return request


def resolve_request(request: dict) -> dict:
    return resolver.resolve_current_body_conformance_v4(declared_conformance_request=request)


def failed_codes(result: dict) -> set[str]:
    codes = {
        check.get("failure_code")
        for check in result["conformance_checks"]
        if not check.get("passed") and check.get("failure_code")
    }
    block = result.get("block", {})
    if isinstance(block, dict):
        if block.get("block_code"):
            codes.add(block["block_code"])
        if block.get("first_failure_code"):
            codes.add(block["first_failure_code"])
    return codes


def with_statement_change(changes: dict) -> dict:
    v9 = selected_v9()
    v9["orientation_statement"].update(changes)
    v9["current_self_orientation_v9_summary"].update(changes)
    return v9


class CurrentBodyConformanceV4Tests(unittest.TestCase):
    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertConformant(self, result: dict) -> None:
        self.assertEqual(CONFORMANT, result["outcome"])
        self.assertIsNone(result["block"].get("block_code"))
        self.assertIsNone(result["block"].get("block_reason"))
        self.assertEqual(0, result["current_body_conformance_v4_summary"]["failed_check_count"])
        self.assertTrue(result["conformance_statement"]["current_body_conformance_v4_conformant"])

    def assertCode(self, result: dict, code: str) -> None:
        self.assertIn(code, failed_codes(result))

    def assertResultNonClaimsFalse(self, result: dict) -> None:
        for key in RESULT_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_v4_conformance_from_mapping(self) -> None:
        result = resolve_request(valid_request())

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertOutcomeFamily(result)
        self.assertConformant(result)

        statement = result["conformance_statement"]
        self.assertTrue(statement["selected_v9_preserved"])
        self.assertTrue(statement["selected_v9_identity_preserved"])
        self.assertTrue(statement["selected_v9_outcome_preserved"])
        self.assertTrue(statement["selected_v9_is_current_self_orientation_v9"])
        self.assertTrue(statement["selected_v9_recorded"])
        self.assertTrue(statement["selected_v9_failed_check_count_zero"])
        self.assertTrue(statement["v9_orientation_conformant"])
        self.assertTrue(statement["basis_preservation_conformant"])
        self.assertTrue(statement["non_claim_conformant"])
        self.assertTrue(statement["conformance_did_not_mutate_v9"])
        self.assertTrue(statement["conformance_did_not_authorize_continuation"])
        self.assertTrue(statement["conformance_did_not_authorize_operation"])
        self.assertTrue(statement["conformance_did_not_create_permission"])
        self.assertTrue(statement["conformance_did_not_claim_final_completion"])
        self.assertTrue(statement["conformance_did_not_schedule_follow_on_work"])

    def test_metadata_declared_question_and_selected_v9_sections(self) -> None:
        result = resolve_request(valid_request())
        metadata = result["current_body_conformance_v4_metadata"]
        declared = result["declared_conformance_question"]
        selected = result["selected_current_self_orientation_v9"]

        for key in (
            "current_body_conformance_v4_result_id",
            "current_body_conformance_v4_result_type",
            "current_body_conformance_v4_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["current_body_conformance_v4_result_version"])
        self.assertEqual("resolve_current_body_conformance_v4", metadata["resolver_module"])

        self.assertEqual(REQUEST_ID, declared["conformance_request_id"])
        self.assertIn("current self-orientation v9", declared["conformance_question"])
        self.assertEqual("RECORD_CURRENT_BODY_CONFORMANCE_V4", declared["conformance_intent"])
        self.assertTrue(declared["conformance_is_not_permission"])
        self.assertTrue(declared["conformance_is_not_continuation"])
        self.assertTrue(declared["conformance_is_not_operation"])
        self.assertTrue(declared["conformance_is_not_final_completion"])
        self.assertTrue(declared["conformance_does_not_mutate_v9"])

        self.assertEqual(V9_ID, selected["selected_current_self_orientation_v9_id"])
        self.assertEqual(RECORDED, selected["selected_current_self_orientation_v9_outcome"])
        self.assertIsNone(selected["selected_current_self_orientation_v9_path"])
        self.assertTrue(selected["selected_v9_is_current_self_orientation_v9"])
        self.assertTrue(selected["selected_v9_recorded"])
        self.assertTrue(selected["selected_v9_failed_check_count_zero"])
        self.assertEqual(
            selected_v9(),
            selected["raw_selected_current_self_orientation_v9"],
        )

    def test_v9_orientation_basis_and_non_claim_conformance_sections(self) -> None:
        result = resolve_request(valid_request())
        orientation = result["v9_orientation_conformance"]
        basis = result["basis_preservation_conformance"]
        non_claims = result["non_claim_conformance"]

        for key in (
            "selected_v9_preserved_v8_as_lineage",
            "selected_v9_preserved_distributed_standing_conformance_closure",
            "selected_v9_preserved_distributed_standing_conformance_closure_closed",
            "selected_v9_preserved_current_body_conformance_v3_closure_basis",
            "selected_v9_preserved_what_stands",
            "selected_v9_preserved_what_does_not_stand",
            "selected_v9_preserved_what_is_closed",
            "selected_v9_preserved_what_remains_open",
            "selected_v9_preserved_orientation_non_meaning",
            "selected_v9_preserved_orientation_statement",
            "selected_v9_did_not_rely_on_recency_or_majority_shortcut",
            "v9_orientation_conformant",
        ):
            self.assertTrue(orientation[key], key)

        for key in (
            "v8_as_prior_lineage_preserved",
            "v9_as_selected_orientation_preserved",
            "current_body_conformance_v3_closure_basis_preserved",
            "distributed_standing_boundary_result_preserved",
            "distributed_standing_boundary_conformance_result_preserved",
            "distributed_standing_boundary_conformance_closure_result_preserved",
            "divergence_consequence_preserved",
            "currentness_successor_preserved",
            "continuity_turn_v2_preserved",
            "standing_propagation_v2_preserved",
            "registry_persistence_v2_preserved",
            "lifecycle_posture_preserved",
            "b_c_divergence_preserved",
            "carrier_b_success_preserved",
            "carrier_c_block_preserved",
            "visible_refusal_preserved_where_exposed",
            "blocked_attempts_preserved_where_exposed",
            "projection_mismatch_preserved_where_exposed",
            "relation_conformance_closure_basis_preserved",
            "what_stands_preserved",
            "what_does_not_stand_preserved",
            "what_is_closed_preserved",
            "what_remains_open_preserved",
            "all_surfaces_remain_basis_only_not_operation_continuation_or_final_completion",
            "basis_preservation_conformant",
        ):
            self.assertTrue(basis[key], key)

        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)
        self.assertTrue(non_claims["declared_non_claims_conformant"])
        self.assertTrue(non_claims["selected_v9_non_claims_conformant"])
        self.assertTrue(non_claims["mutation_replay_or_merge_absent"])
        self.assertTrue(non_claims["non_claim_conformant"])

    def test_checks_non_meaning_open_surfaces_summary_and_non_claims(self) -> None:
        result = resolve_request(valid_request())

        for check in result["conformance_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("failure_code", check)
            self.assertTrue(check["passed"], check["check_name"])

        check_names = {check["check_name"] for check in result["conformance_checks"]}
        for expected in (
            "conformance question declared",
            "conformance intent supported",
            "selected current self-orientation v9 present",
            "selected v9 identity present",
            "selected v9 outcome present",
            "selected v9 outcome recorded",
            "selected v9 failed check count zero",
            "selected v9 preserves v8 lineage",
            "selected v9 preserves distributed standing boundary conformance closure",
            "selected v9 preserves distributed standing boundary conformance closure closed",
            "selected v9 preserves current-body conformance v3 closure basis",
            "selected v9 preserves what stands",
            "selected v9 preserves what does not stand",
            "selected v9 preserves what is closed",
            "selected v9 preserves what remains open",
            "selected v9 preserves orientation non-claims",
            "selected v9 does not authorize continuation",
            "selected v9 does not authorize operation",
            "selected v9 does not authorize repository synchronization",
            "selected v9 does not authorize full body transfer",
            "selected v9 does not create second body",
            "selected v9 does not create permission",
            "selected v9 does not create authority",
            "selected v9 does not create truth/action",
            "selected v9 does not claim final completion",
            "selected v9 does not schedule follow-on work",
            "selected v9 does not schedule self-orientation successor beyond v9",
            "selected v9 does not mutate prior result",
            "conformance does not authorize continuation",
            "conformance does not authorize operation",
            "conformance does not create permission",
            "conformance does not claim final completion",
            "no mutation replay or merge",
            "non-claims remain false",
        ):
            self.assertIn(expected, check_names)

        for key in CONFORMANCE_NON_MEANING_KEYS:
            self.assertTrue(result["conformance_non_meaning"][key], key)
        for key in OPEN_KEYS:
            self.assertIn(key, result["what_remains_open"])
        self.assertTrue(result["what_remains_open"]["open_means_not_scheduled"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])
        self.assertTrue(result["what_remains_open"]["open_means_not_executed"])

        summary = resolver.build_current_body_conformance_v4_summary(result)
        for key in (
            "outcome",
            "block_code",
            "block_reason",
            "conformance_request_id",
            "conformance_question",
            "conformance_intent",
            "selected_v9_id",
            "selected_v9_outcome",
            "passed_check_count",
            "failed_check_count",
            "current_body_conformance_v4_conformant",
            "selected_v9_preserved",
            "selected_v9_identity_preserved",
            "selected_v9_outcome_preserved",
            "selected_v9_is_current_self_orientation_v9",
            "selected_v9_recorded",
            "selected_v9_failed_check_count_zero",
            "v9_orientation_conformant",
            "basis_preservation_conformant",
            "non_claim_conformant",
            "conformance_did_not_mutate_v9",
            "conformance_did_not_authorize_continuation",
            "conformance_did_not_authorize_operation",
            "conformance_did_not_create_permission",
            "conformance_did_not_claim_final_completion",
            "conformance_did_not_schedule_follow_on_work",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(CONFORMANT, summary["outcome"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["current_body_conformance_v4_conformant"])
        self.assertResultNonClaimsFalse(result)

    def test_result_level_non_claims_for_conformant_not_conformant_and_blocked(self) -> None:
        conformant = resolve_request(valid_request())
        failing_v9 = selected_v9()
        failing_v9["current_self_orientation_v9_summary"]["failed_check_count"] = 1
        not_conformant = resolve_request(valid_request(v9=failing_v9))
        blocked = resolver.resolve_current_body_conformance_v4()

        self.assertEqual(CONFORMANT, conformant["outcome"])
        self.assertEqual(NOT_CONFORMANT, not_conformant["outcome"])
        self.assertEqual(BLOCKED, blocked["outcome"])
        for result in (conformant, not_conformant, blocked):
            self.assertOutcomeFamily(result)
            self.assertResultNonClaimsFalse(result)

    def test_request_builder_helper(self) -> None:
        request = resolver.build_declared_current_body_conformance_v4_request(
            "current_body_conformance_v4_helper_001",
            "Does current self-orientation v9 conform to the current body line?",
            selected_v9(),
            conformance_basis(),
            selected_current_self_orientation_v9_path="/tmp/selected_v9.json",
            selected_current_self_orientation_v9_id=V9_ID,
            selected_current_self_orientation_v9_outcome=RECORDED,
        )
        request.update(valid_request())
        request["conformance_request_id"] = "current_body_conformance_v4_helper_001"
        request["selected_current_self_orientation_v9_path"] = None

        self.assertEqual("current_body_conformance_v4_helper_001", request["conformance_request_id"])
        self.assertIn("current self-orientation v9", request["conformance_question"])
        self.assertEqual(selected_v9(), request["selected_current_self_orientation_v9"])
        self.assertEqual(conformance_basis(), request["current_body_conformance_v4_basis"])
        self.assertEqual(V9_ID, request["selected_current_self_orientation_v9_id"])
        self.assertEqual(RECORDED, request["selected_current_self_orientation_v9_outcome"])
        self.assertEqual(RECORDED, request["expected_selected_v9_outcome"])
        self.assertEqual(required_non_claims(), request["declared_non_claims"])
        self.assertConformant(resolve_request(request))

    def test_path_based_selected_v9_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "selected_v9.json"
            path.write_text(json.dumps(selected_v9()), encoding="utf-8")
            request = valid_request(selected_current_self_orientation_v9_path=str(path))

            result = resolve_request(request)

            self.assertConformant(result)
            selected = result["selected_current_self_orientation_v9"]
            self.assertEqual(str(path), selected["selected_current_self_orientation_v9_path"])
            self.assertEqual(V9_ID, selected["selected_current_self_orientation_v9_id"])
            self.assertEqual(RECORDED, selected["selected_current_self_orientation_v9_outcome"])

    def test_path_based_conformance_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "conformance_request.json"
            path.write_text(json.dumps(valid_request()), encoding="utf-8")

            result = resolver.resolve_current_body_conformance_v4_from_path(path)

            self.assertConformant(result)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
            self.assertEqual(str(path), result["declared_conformance_question"]["declared_conformance_request_path"])

    def test_write_behavior_and_default_output_path(self) -> None:
        result = resolve_request(valid_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "v4_result.json"
            written = resolver.write_current_body_conformance_v4_result(result, explicit)
            self.assertEqual(explicit, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            self.assertNotIn("current_self_orientation_v9", str(resolver.CURRENT_BODY_CONFORMANCE_V4_ROOT))
            with patch.object(resolver, "CURRENT_BODY_CONFORMANCE_V4_ROOT", Path(tmp) / "v4_root"):
                first = resolver.write_current_body_conformance_v4_result(result)
                second = resolver.write_current_body_conformance_v4_result(result)
                self.assertEqual(Path(tmp) / "v4_root", first.parent)
                self.assertTrue(first.name.endswith("__current_body_conformance_v4_result.json"))
                self.assertTrue(second.name.endswith("_001.json"))
                self.assertNotEqual(first, second)

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        request_before = copy.deepcopy(request)
        v9_before = copy.deepcopy(request["selected_current_self_orientation_v9"])

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(request_before, request)
        self.assertEqual(v9_before, request["selected_current_self_orientation_v9"])
        self.assertEqual(first["selected_current_self_orientation_v9"]["raw_selected_current_self_orientation_v9"], v9_before)
        self.assertEqual(second["selected_current_self_orientation_v9"]["raw_selected_current_self_orientation_v9"], v9_before)

        with tempfile.TemporaryDirectory() as tmp:
            selected_path = Path(tmp) / "selected_v9.json"
            selected_path.write_text(json.dumps(v9_before, sort_keys=True), encoding="utf-8")
            before_text = selected_path.read_text(encoding="utf-8")
            resolver.write_current_body_conformance_v4_result(first, Path(tmp) / "out" / "v4.json")
            self.assertEqual(before_text, selected_path.read_text(encoding="utf-8"))

    def test_not_conformant_readable_selected_v9(self) -> None:
        failed_v9 = selected_v9()
        failed_v9["current_self_orientation_v9_summary"]["failed_check_count"] = 1
        result = resolve_request(valid_request(v9=failed_v9))
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertGreater(result["current_body_conformance_v4_summary"]["failed_check_count"], 0)
        self.assertCode(result, "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS")
        self.assertTrue(result["selected_current_self_orientation_v9"]["selected_v9_preserved"])

        continuation_v9 = selected_v9()
        continuation_v9["orientation_authorizes_continuation"] = True
        result = resolve_request(valid_request(v9=continuation_v9))
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "V9_AUTHORIZES_CONTINUATION")
        self.assertEqual(continuation_v9, valid_request(v9=continuation_v9)["selected_current_self_orientation_v9"])

    def test_blocking_intent_missing_and_malformed_request(self) -> None:
        explicit = resolve_request(valid_request(intent="BLOCK_CURRENT_BODY_CONFORMANCE_V4"))
        self.assertEqual(BLOCKED, explicit["outcome"])
        self.assertCode(explicit, "CONFORMANCE_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(explicit["conformance_statement"]["current_body_conformance_v4_conformant"])

        missing = resolver.resolve_current_body_conformance_v4()
        self.assertEqual(BLOCKED, missing["outcome"])
        self.assertCode(missing, "CONFORMANCE_QUESTION_UNDECLARED")

        malformed = resolver.resolve_current_body_conformance_v4(declared_conformance_request=[])
        self.assertEqual(BLOCKED, malformed["outcome"])
        self.assertCode(malformed, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

    def test_path_unreadable_and_malformed_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_request = resolver.resolve_current_body_conformance_v4_from_path(
                tmp_path / "missing_request.json"
            )
            self.assertEqual(BLOCKED, missing_request["outcome"])
            self.assertCode(missing_request, "DECLARED_CONFORMANCE_REQUEST_UNREADABLE")

            bad_request_path = tmp_path / "bad_request.json"
            bad_request_path.write_text("{bad json", encoding="utf-8")
            bad_request = resolver.resolve_current_body_conformance_v4_from_path(bad_request_path)
            self.assertEqual(BLOCKED, bad_request["outcome"])
            self.assertCode(bad_request, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

            array_request_path = tmp_path / "array_request.json"
            array_request_path.write_text("[]", encoding="utf-8")
            array_request = resolver.resolve_current_body_conformance_v4_from_path(array_request_path)
            self.assertEqual(BLOCKED, array_request["outcome"])
            self.assertCode(array_request, "DECLARED_CONFORMANCE_REQUEST_MALFORMED")

            request = valid_request(selected_current_self_orientation_v9_path=str(tmp_path / "missing_v9.json"))
            selected_missing = resolve_request(request)
            self.assertEqual(BLOCKED, selected_missing["outcome"])
            self.assertCode(selected_missing, "CURRENT_SELF_ORIENTATION_V9_UNREADABLE")

            bad_v9_path = tmp_path / "bad_v9.json"
            bad_v9_path.write_text("{bad json", encoding="utf-8")
            selected_bad = resolve_request(valid_request(selected_current_self_orientation_v9_path=str(bad_v9_path)))
            self.assertEqual(BLOCKED, selected_bad["outcome"])
            self.assertCode(selected_bad, "CURRENT_SELF_ORIENTATION_V9_MALFORMED")

            array_v9_path = tmp_path / "array_v9.json"
            array_v9_path.write_text("[]", encoding="utf-8")
            selected_array = resolve_request(valid_request(selected_current_self_orientation_v9_path=str(array_v9_path)))
            self.assertEqual(BLOCKED, selected_array["outcome"])
            self.assertCode(selected_array, "CURRENT_SELF_ORIENTATION_V9_MALFORMED")

    def test_selected_v9_identity_outcome_and_failed_check_failures(self) -> None:
        missing_id = selected_v9()
        del missing_id["current_self_orientation_v9_metadata"]["current_self_orientation_v9_result_id"]
        del missing_id["current_self_orientation_v9_summary"]["current_self_orientation_v9_result_id"]
        del missing_id["current_self_orientation_v9_summary"]["orientation_request_id"]
        request = valid_request(v9=missing_id)
        del request["selected_current_self_orientation_v9_id"]
        result = resolve_request(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertCode(result, "CURRENT_SELF_ORIENTATION_V9_IDENTITY_MISSING")

        missing_outcome = selected_v9()
        del missing_outcome["outcome"]
        del missing_outcome["current_self_orientation_v9_summary"]["outcome"]
        request = valid_request(v9=missing_outcome)
        del request["selected_current_self_orientation_v9_outcome"]
        result = resolve_request(request)
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertCode(result, "CURRENT_SELF_ORIENTATION_V9_OUTCOME_MISSING")

        not_recorded = selected_v9()
        not_recorded["outcome"] = "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"
        not_recorded["current_self_orientation_v9_summary"]["outcome"] = "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"
        request = valid_request(v9=not_recorded)
        request["selected_current_self_orientation_v9_outcome"] = "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"
        result = resolve_request(request)
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED")

        failed = selected_v9()
        failed["orientation_checks"].append(
            {
                "check_name": "synthetic failed v9 check",
                "passed": False,
                "expected_posture": True,
                "actual_posture": False,
                "block_code": "SYNTHETIC_FAILURE",
            }
        )
        failed["current_self_orientation_v9_summary"]["failed_check_count"] = 1
        result = resolve_request(valid_request(v9=failed))
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "CURRENT_SELF_ORIENTATION_V9_HAS_FAILED_CHECKS")

    def test_not_conformant_missing_basis_sections(self) -> None:
        cases = [
            ("V8_LINEAGE_MISSING", {"v8_preserved_as_lineage": False}),
            (
                "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
                {"distributed_standing_conformance_closure_preserved": False},
            ),
            (
                "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_NOT_CLOSED",
                {"distributed_standing_conformance_closure_closed": False},
            ),
            (
                "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING",
                {"current_body_conformance_v3_closure_basis_preserved": False},
            ),
            ("WHAT_STANDS_MISSING", {"what_stands_preserved": False}),
            ("WHAT_DOES_NOT_STAND_MISSING", {"what_does_not_stand_preserved": False}),
            ("WHAT_IS_CLOSED_MISSING", {"what_is_closed_preserved": False}),
            ("WHAT_REMAINS_OPEN_MISSING", {"what_remains_open_preserved": False}),
        ]
        for code, changes in cases:
            with self.subTest(code=code):
                v9 = with_statement_change(changes)
                if "what_stands_preserved" in changes:
                    v9["what_stands"]["what_stands_preserved"] = False
                if "what_does_not_stand_preserved" in changes:
                    v9["what_does_not_stand"]["what_does_not_stand_preserved"] = False
                if "what_is_closed_preserved" in changes:
                    v9["what_is_closed"]["what_is_closed_preserved"] = False
                if "what_remains_open_preserved" in changes:
                    v9["what_remains_open"]["what_remains_open_preserved"] = False
                result = resolve_request(valid_request(v9=v9))
                self.assertEqual(NOT_CONFORMANT, result["outcome"])
                self.assertCode(result, code)

    def test_not_conformant_v9_collapse_flags(self) -> None:
        cases = [
            ("V9_AUTHORIZES_CONTINUATION", "orientation_authorizes_continuation"),
            ("V9_AUTHORIZES_OPERATION", "orientation_authorizes_operation"),
            ("V9_AUTHORIZES_REPOSITORY_SYNC", "orientation_authorizes_repository_sync"),
            ("V9_AUTHORIZES_FULL_BODY_TRANSFER", "orientation_authorizes_full_body_transfer"),
            ("V9_CREATES_SECOND_BODY", "orientation_creates_second_body"),
            ("V9_CREATES_PERMISSION", "orientation_creates_permission"),
            ("V9_CREATES_AUTHORITY", "orientation_creates_authority"),
            ("V9_CREATES_TRUTH_OR_ACTION", "orientation_creates_truth"),
            ("V9_CLAIMS_FINAL_COMPLETION", "orientation_claims_final_completion"),
            ("V9_SCHEDULES_FOLLOW_ON_WORK", "orientation_schedules_follow_on_work"),
            ("V9_SCHEDULES_SELF_ORIENTATION_SUCCESSOR", "orientation_schedules_self_orientation_successor"),
            ("V9_MUTATES_PRIOR_RESULT", "orientation_mutates_prior_result"),
        ]
        for code, key in cases:
            with self.subTest(code=code):
                v9 = selected_v9()
                v9[key] = True
                result = resolve_request(valid_request(v9=v9))
                self.assertEqual(NOT_CONFORMANT, result["outcome"])
                self.assertCode(result, code)

    def test_not_conformant_conformance_collapse_and_mutation_flags(self) -> None:
        cases = [
            ("CONFORMANCE_AUTHORIZES_CONTINUATION", "conformance_authorizes_continuation"),
            ("CONFORMANCE_AUTHORIZES_OPERATION", "conformance_authorizes_operation"),
            ("CONFORMANCE_CREATES_PERMISSION", "conformance_creates_permission"),
            ("CONFORMANCE_CLAIMS_FINAL_COMPLETION", "conformance_claims_final_completion"),
            ("MUTATION_REPLAY_OR_MERGE_DETECTED", "mutation_performed"),
            ("MUTATION_REPLAY_OR_MERGE_DETECTED", "replay_performed"),
            ("MUTATION_REPLAY_OR_MERGE_DETECTED", "merge_performed"),
        ]
        for code, key in cases:
            with self.subTest(code=code, key=key):
                request = valid_request()
                request[key] = True
                result = resolve_request(request)
                self.assertEqual(NOT_CONFORMANT, result["outcome"])
                self.assertCode(result, code)

    def test_required_non_claim_missing_or_flipped(self) -> None:
        missing = valid_request()
        del missing["declared_non_claims"]["permission_created"]
        result = resolve_request(missing)
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "NON_CLAIM_MISSING_OR_FLIPPED")

        flipped = valid_request()
        flipped["declared_non_claims"]["permission_created"] = True
        result = resolve_request(flipped)
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "NON_CLAIM_MISSING_OR_FLIPPED")

        selected_flipped = selected_v9()
        selected_flipped["non_claims"]["permission_created"] = True
        result = resolve_request(valid_request(v9=selected_flipped))
        self.assertEqual(NOT_CONFORMANT, result["outcome"])
        self.assertCode(result, "NON_CLAIM_MISSING_OR_FLIPPED")


if __name__ == "__main__":
    unittest.main()
