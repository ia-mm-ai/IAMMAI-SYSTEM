"""Bounded tests for current self-orientation v9.

These tests audit one surface only: current self-orientation after distributed
standing boundary conformance closure. V9 preserves v8 as lineage, records what
stands, what does not stand, what is closed, and what remains open. It must not
authorize continuation, operation, repository synchronization, full body
transfer, second-body creation, permission, authority, truth/action, final
completion, follow-on work, or a successor self-orientation beyond v9.
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

import resolve_current_self_orientation_v9 as resolver  # noqa: E402


RECORDED = "CURRENT_SELF_ORIENTATION_V9_RECORDED"
NOT_RECORDED = "CURRENT_SELF_ORIENTATION_V9_NOT_RECORDED"
BLOCKED = "CURRENT_SELF_ORIENTATION_V9_BLOCKED"
CLOSED = "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_CLOSED"
OUTCOME_FAMILY = {RECORDED, NOT_RECORDED, BLOCKED}

TOP_LEVEL_SECTIONS = {
    "current_self_orientation_v9_metadata",
    "declared_orientation_question",
    "selected_prior_self_orientation",
    "selected_distributed_standing_conformance_closure",
    "orientation_basis",
    "what_stands",
    "what_does_not_stand",
    "what_is_closed",
    "what_remains_open",
    "orientation_checks",
    "orientation_statement",
    "orientation_non_meaning",
    "non_claims",
    "outcome",
    "block",
    "current_self_orientation_v9_summary",
}

RESULT_NON_CLAIMS = set(resolver.REQUIRED_NON_CLAIMS)

WHAT_STANDS_KEYS = {
    "current_self_orientation_v8_remains_lineage",
    "current_body_conformance_v3_closure_remains_basis",
    "carrier_b_successful_receipt_evidence_stands_as_evidence",
    "carrier_c_blocked_receipt_evidence_stands_as_evidence",
    "b_c_visible_divergence_stands",
    "carrier_c_lifecycle_posture_stands",
    "registry_persistence_v2_stands_as_reference_posture",
    "standing_propagation_v2_stands_as_evidence_reference_posture",
    "continuity_turn_v2_stands_as_lineage_projection_posture",
    "cross_carrier_currentness_successor_stands_as_body_side_accounting_posture",
    "cross_carrier_divergence_consequence_stands_as_caution_reliance_effect_posture",
    "distributed_standing_boundary_result_stands_as_bounded_body_side_posture_recording",
    "distributed_standing_boundary_conformance_stands_as_conformance",
    "distributed_standing_boundary_conformance_closure_stands_as_closure_of_conformance_meaning",
}

WHAT_DOES_NOT_STAND_KEYS = {
    "distributed_operation_does_not_stand",
    "repository_synchronization_does_not_stand",
    "full_body_transfer_does_not_stand",
    "second_body_does_not_stand",
    "continuation_does_not_stand",
    "carrier_currentness_does_not_stand",
    "current_carrier_selection_does_not_stand",
    "winning_carrier_selection_does_not_stand",
    "losing_carrier_invalidation_does_not_stand",
    "source_replacement_does_not_stand",
    "authority_creation_does_not_stand",
    "permission_creation_does_not_stand",
    "truth_action_does_not_stand",
    "final_governance_does_not_stand",
    "final_continuity_completion_does_not_stand",
    "final_system_identity_completion_does_not_stand",
    "public_launch_readiness_does_not_stand",
    "self_orientation_successor_beyond_v9_does_not_stand",
}

WHAT_IS_CLOSED_KEYS = {
    "current_orientation_to_distributed_standing_boundary_conformance_closure_closed",
    "distributed_standing_boundary_conformance_closure_stands_as_closed_meaning",
    "closure_non_meaning_does_not_authorize_operation_or_continuation_closed",
    "v8_is_prior_orientation_lineage_not_latest_orientation",
}

OPEN_KEYS = {
    "current_self_orientation_v9_implementation_refinement",
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

ORIENTATION_NON_MEANING_KEYS = {
    "permission",
    "continuation",
    "operation",
    "repository_synchronization",
    "full_body_transfer",
    "second_body",
    "distributed_operation",
    "implementation",
    "final_completion",
    "final_governance",
    "final_continuity_completion",
    "final_system_identity",
    "public_launch_readiness",
    "carrier_currentness",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "source_replacement",
    "authority",
    "truth",
    "action",
    "divergence_resolution",
    "evidence_erasure",
    "prior_result_mutation",
    "follow_on_work_authorization",
    "self_orientation_successor_beyond_v9",
}


def required_non_claims() -> dict:
    return copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)


def selected_v8() -> dict:
    return {
        "current_self_orientation_metadata": {
            "current_self_orientation_result_id": "current_self_orientation_v8_001",
            "current_self_orientation_result_type": "current_self_orientation_result",
            "current_self_orientation_result_version": "0.8.0",
            "resolver_module": "resolve_current_self_orientation_v8",
        },
        "current_self_orientation_summary": {
            "current_self_orientation_result_id": "current_self_orientation_v8_001",
            "outcome": "SELF_ORIENTED",
            "v8_preserved_as_lineage": True,
        },
        "orientation_statement": {
            "v8_preserved_as_lineage": True,
            "v8_erased": False,
            "v8_mutated": False,
            "v8_is_prior_orientation_lineage_not_latest_orientation": True,
        },
        "non_claims": {
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
        },
        "outcome": "SELF_ORIENTED",
    }


def selected_closure() -> dict:
    statement = {
        "distributed_standing_boundary_conformance_closed": True,
        "selected_conformance_result_preserved": True,
        "selected_conformance_result_identity_preserved": True,
        "selected_conformance_result_outcome_preserved": True,
        "selected_conformance_result_is_conformance_result": True,
        "selected_conformance_result_is_conformant": True,
        "selected_conformance_result_failed_check_count_zero": True,
        "conformance_meaning_preserved": True,
        "conformance_non_meaning_preserved": True,
        "closure_did_not_expand_conformance": True,
        "closure_did_not_create_permission": True,
        "closure_did_not_authorize_continuation": True,
        "closure_did_not_authorize_operation": True,
        "closure_did_not_authorize_repository_sync": True,
        "closure_did_not_authorize_full_body_transfer": True,
        "closure_did_not_create_second_body": True,
        "closure_did_not_schedule_self_orientation_successor": True,
        "closure_did_not_claim_final_completion": True,
    }
    return {
        "distributed_standing_boundary_conformance_closure_metadata": {
            "closure_result_id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            "closure_result_type": "distributed_standing_boundary_conformance_closure_result",
            "closure_result_version": "0.1.0",
            "resolver_module": "resolve_distributed_standing_boundary_conformance_closure",
        },
        "selected_conformance_result": {
            "selected_conformance_result_id": "carrier_b_c_distributed_standing_boundary_conformance_001",
            "selected_conformance_result_outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT",
        },
        "selected_distributed_standing_boundary_result": {
            "selected_distributed_standing_result_id": "carrier_b_c_distributed_standing_boundary_001",
            "selected_distributed_standing_result_outcome": "DISTRIBUTED_STANDING_POSTURE_RECORDED",
        },
        "conformance_meaning": {
            "selected_distributed_standing_boundary_result_preserved": True,
            "selected_distributed_standing_boundary_result_identity_preserved": True,
            "selected_distributed_standing_boundary_result_outcome_preserved": True,
            "selected_distributed_standing_boundary_result_is_distributed_standing_boundary": True,
            "prerequisite_basis_conformant": True,
            "refusal_divergence_lineage_conformant": True,
            "non_claim_conformant": True,
            "summary_detail_correspondence_passed": True,
        },
        "conformance_non_meaning": {
            "permission": True,
            "continuation": True,
            "operation": True,
            "repository_synchronization": True,
            "full_body_transfer": True,
            "second_body_creation": True,
            "implementation": True,
            "final_completion": True,
            "self_orientation_successor_by_default": True,
        },
        "closure_checks": [
            {
                "check_name": "synthetic closure check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "failure_code": None,
            }
        ],
        "closure_statement": statement,
        "closure_non_meaning": {
            "continuation": True,
            "operation": True,
            "repository_synchronization": True,
            "full_body_transfer": True,
            "second_body": True,
            "implementation": True,
            "final_completion": True,
            "self_orientation_successor_by_default": True,
        },
        "non_claims": {
            "selected_conformance_result_mutated": False,
            "selected_distributed_standing_result_mutated": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
        },
        "outcome": CLOSED,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "distributed_standing_boundary_conformance_closure_summary": {
            **statement,
            "outcome": CLOSED,
            "closure_result_id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            "closure_request_id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            "selected_conformance_result_id": "carrier_b_c_distributed_standing_boundary_conformance_001",
            "selected_conformance_result_outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANT",
            "passed_check_count": 44,
            "failed_check_count": 0,
        },
    }


def orientation_basis() -> dict:
    return {
        "current_self_orientation_v8": "current_self_orientation_v8_001",
        "current_body_conformance_v3_closure": "current_body_conformance_v3_closure_001",
        "distributed_standing_boundary_result": "carrier_b_c_distributed_standing_boundary_001",
        "distributed_standing_boundary_conformance_result": "carrier_b_c_distributed_standing_boundary_conformance_001",
        "distributed_standing_boundary_conformance_closure_result": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
        "divergence_consequence": "cross-carrier divergence consequence caution",
        "currentness_successor": "body-side currentness successor accounting",
        "continuity_turn_v2": "lineage/projection posture",
        "standing_propagation_v2": "evidence/reference posture",
        "registry_persistence_v2": "reference posture",
        "lifecycle_posture": "Carrier C lifecycle posture",
        "b_c_visible_divergence": True,
        "carrier_b_successful_physical_receipt_evidence": True,
        "carrier_c_blocked_physical_receipt_evidence": True,
        "relation_conformance_closure_basis": True,
        "reference_grounding_read_only": True,
        "orientation_basis_is_not_permission_set": True,
        "orientation_basis_is_not_operation_plan": True,
        "orientation_basis_is_not_repository_synchronization_plan": True,
        "orientation_basis_is_not_full_body_transfer_plan": True,
        "orientation_basis_is_not_second_body_creation_plan": True,
        "orientation_basis_is_not_final_governance": True,
    }


def current_body_basis() -> dict:
    return {
        "current_body_conformance_v3_closure": "current_body_conformance_v3_closure_001",
        "remains_basis": True,
        "does_not_authorize_continuation": True,
        "does_not_authorize_operation": True,
    }


def what_stands() -> dict:
    return {
        **{key: True for key in WHAT_STANDS_KEYS},
        "bounded_form_only": True,
        "does_not_combine_into_operation": True,
        "does_not_combine_into_continuation": True,
        "does_not_combine_into_synchronization": True,
        "does_not_combine_into_full_body_transfer": True,
        "does_not_combine_into_final_completion": True,
    }


def what_does_not_stand() -> dict:
    return {key: True for key in WHAT_DOES_NOT_STAND_KEYS}


def what_is_closed() -> dict:
    return {
        **{key: True for key in WHAT_IS_CLOSED_KEYS},
        "orientation_closure_only": True,
        "not_closure_of_distributed_standing_implementation": True,
        "not_closure_of_operation": True,
        "not_closure_of_final_governance": True,
        "not_closure_of_final_continuity_completion": True,
        "not_closure_of_final_system_identity": True,
    }


def what_remains_open() -> dict:
    return {key: "open_not_scheduled_not_authorized_not_executed" for key in OPEN_KEYS}


def valid_request(
    *,
    intent: str = "RECORD_CURRENT_SELF_ORIENTATION_V9",
    prior: dict | None = None,
    closure: dict | None = None,
    selected_prior_self_orientation_path: str | None = None,
    selected_conformance_closure_path: str | None = None,
) -> dict:
    request = resolver.build_declared_current_self_orientation_v9_request(
        "current_self_orientation_v9_001",
        "What is the body's current orientation after distributed standing boundary conformance closure?",
        copy.deepcopy(selected_v8() if prior is None else prior),
        copy.deepcopy(selected_closure() if closure is None else closure),
        orientation_basis(),
        what_stands(),
        what_does_not_stand(),
        what_is_closed(),
        what_remains_open(),
        orientation_intent=intent,
        selected_prior_self_orientation_path=selected_prior_self_orientation_path,
        selected_conformance_closure_path=selected_conformance_closure_path,
        current_body_conformance_v3_closure_basis=current_body_basis(),
    )
    request.update(
        {
            "selected_prior_self_orientation_id": "current_self_orientation_v8_001",
            "selected_prior_self_orientation_outcome": "SELF_ORIENTED",
            "selected_conformance_closure_id": "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            "selected_conformance_closure_outcome": CLOSED,
            "distributed_standing_boundary_result_reference": "carrier_b_c_distributed_standing_boundary_001",
            "distributed_standing_boundary_conformance_reference": "carrier_b_c_distributed_standing_boundary_conformance_001",
            "reference_grounding": ["reference/IAMMAI read-only grounding"],
            "orientation_scope": "current self-orientation v9 only",
        }
    )
    return request


def resolve_request(request: dict) -> dict:
    return resolver.resolve_current_self_orientation_v9(declared_orientation_request=request)


def failed_codes(result: dict) -> set[str]:
    codes = {
        check.get("block_code")
        for check in result["orientation_checks"]
        if not check.get("passed") and check.get("block_code")
    }
    block = result.get("block", {})
    if isinstance(block, dict) and block.get("block_code"):
        codes.add(block["block_code"])
    return codes


def with_closure_change(changes: dict, *, summary: dict | None = None) -> dict:
    closure = selected_closure()
    closure.update(changes)
    if summary:
        closure["distributed_standing_boundary_conformance_closure_summary"].update(summary)
    return closure


class CurrentSelfOrientationV9Tests(unittest.TestCase):
    def assertOutcomeFamily(self, result: dict) -> None:
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def assertRecorded(self, result: dict) -> None:
        self.assertEqual(RECORDED, result["outcome"])
        self.assertIsNone(result["block"].get("block_code"))
        self.assertIsNone(result["block"].get("block_reason"))
        self.assertEqual(0, result["current_self_orientation_v9_summary"]["failed_check_count"])
        self.assertTrue(result["orientation_statement"]["current_self_orientation_v9_recorded"])

    def assertBlockedCode(self, result: dict, code: str) -> None:
        self.assertEqual(BLOCKED, result["outcome"])
        self.assertIn(code, failed_codes(result))

    def assertResultNonClaimsFalse(self, result: dict) -> None:
        for key in RESULT_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertIs(result["non_claims"][key], False, key)

    def test_successful_v9_orientation_recording(self) -> None:
        result = resolve_request(valid_request())

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertOutcomeFamily(result)
        self.assertRecorded(result)

        statement = result["orientation_statement"]
        self.assertTrue(statement["prior_self_orientation_preserved"])
        self.assertTrue(statement["v8_preserved_as_lineage"])
        self.assertTrue(statement["distributed_standing_conformance_closure_preserved"])
        self.assertTrue(statement["distributed_standing_conformance_closure_closed"])
        self.assertTrue(statement["distributed_standing_conformance_closure_failed_check_count_zero"])
        self.assertTrue(statement["current_body_conformance_v3_closure_basis_preserved"])
        self.assertTrue(statement["what_stands_preserved"])
        self.assertTrue(statement["what_does_not_stand_preserved"])
        self.assertTrue(statement["what_is_closed_preserved"])
        self.assertTrue(statement["what_remains_open_preserved"])
        self.assertTrue(statement["orientation_did_not_create_permission"])
        self.assertTrue(statement["orientation_did_not_authorize_continuation"])
        self.assertTrue(statement["orientation_did_not_authorize_operation"])
        self.assertTrue(statement["orientation_did_not_authorize_repository_sync"])
        self.assertTrue(statement["orientation_did_not_authorize_full_body_transfer"])
        self.assertTrue(statement["orientation_did_not_create_second_body"])
        self.assertTrue(statement["orientation_did_not_claim_final_completion"])
        self.assertTrue(statement["orientation_did_not_schedule_follow_on_work"])
        self.assertTrue(statement["orientation_did_not_mutate_prior_result"])

    def test_metadata_and_declared_orientation_question(self) -> None:
        result = resolve_request(valid_request())
        metadata = result["current_self_orientation_v9_metadata"]
        declared = result["declared_orientation_question"]

        for key in (
            "current_self_orientation_v9_result_id",
            "current_self_orientation_v9_result_type",
            "current_self_orientation_v9_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata[key], key)
        self.assertEqual("0.1.0", metadata["current_self_orientation_v9_result_version"])
        self.assertEqual("resolve_current_self_orientation_v9", metadata["resolver_module"])

        self.assertEqual("current_self_orientation_v9_001", declared["orientation_request_id"])
        self.assertIn("current orientation", declared["orientation_question"])
        self.assertEqual("RECORD_CURRENT_SELF_ORIENTATION_V9", declared["orientation_intent"])
        self.assertEqual(required_non_claims(), declared["declared_non_claims"])
        self.assertTrue(declared["self_orientation_is_not_permission"])
        self.assertTrue(declared["self_orientation_is_not_continuation"])
        self.assertTrue(declared["self_orientation_is_not_operation"])
        self.assertTrue(declared["self_orientation_is_not_final_completion"])
        self.assertTrue(declared["self_orientation_does_not_mutate_prior_surfaces"])

    def test_selected_prior_and_closure_sections(self) -> None:
        result = resolve_request(valid_request())
        prior = result["selected_prior_self_orientation"]
        closure = result["selected_distributed_standing_conformance_closure"]
        raw_prior = prior["raw_selected_prior_self_orientation"]
        raw_closure = closure["raw_selected_distributed_standing_conformance_closure"]

        self.assertEqual("current_self_orientation_v8_001", prior["selected_prior_self_orientation_id"])
        self.assertEqual("SELF_ORIENTED", prior["selected_prior_self_orientation_outcome"])
        self.assertIsNone(prior["selected_prior_self_orientation_path"])
        self.assertTrue(prior["v8_preserved_as_lineage"])
        self.assertFalse(raw_prior["orientation_statement"]["v8_erased"])
        self.assertFalse(raw_prior["orientation_statement"]["v8_mutated"])
        self.assertTrue(result["what_is_closed"]["v8_is_prior_orientation_lineage_not_latest_orientation"])

        self.assertEqual(
            "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
            closure["selected_conformance_closure_id"],
        )
        self.assertEqual(CLOSED, closure["selected_conformance_closure_outcome"])
        self.assertIsNone(closure["selected_conformance_closure_path"])
        self.assertTrue(closure["selected_conformance_closure_failed_check_count_zero"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_authorize_continuation"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_authorize_operation"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_authorize_repository_sync"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_authorize_full_body_transfer"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_create_second_body"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_schedule_self_orientation_successor"])
        self.assertTrue(raw_closure["closure_statement"]["closure_did_not_claim_final_completion"])

    def test_orientation_basis_and_standing_sections(self) -> None:
        result = resolve_request(valid_request())
        basis = result["orientation_basis"]
        raw_basis = basis["orientation_basis"]

        for key in (
            "current_self_orientation_v8",
            "current_body_conformance_v3_closure",
            "distributed_standing_boundary_result",
            "distributed_standing_boundary_conformance_result",
            "distributed_standing_boundary_conformance_closure_result",
            "divergence_consequence",
            "currentness_successor",
            "continuity_turn_v2",
            "standing_propagation_v2",
            "registry_persistence_v2",
            "lifecycle_posture",
            "b_c_visible_divergence",
            "carrier_b_successful_physical_receipt_evidence",
            "carrier_c_blocked_physical_receipt_evidence",
            "relation_conformance_closure_basis",
        ):
            self.assertIn(key, raw_basis)
        self.assertTrue(basis["current_body_conformance_v3_closure_basis_preserved"])
        self.assertEqual(["reference/IAMMAI read-only grounding"], basis["reference_grounding"])
        self.assertTrue(raw_basis["orientation_basis_is_not_permission_set"])
        self.assertTrue(raw_basis["orientation_basis_is_not_operation_plan"])
        self.assertTrue(raw_basis["orientation_basis_is_not_repository_synchronization_plan"])
        self.assertTrue(raw_basis["orientation_basis_is_not_full_body_transfer_plan"])
        self.assertTrue(raw_basis["orientation_basis_is_not_second_body_creation_plan"])
        self.assertTrue(raw_basis["orientation_basis_is_not_final_governance"])

        for key in WHAT_STANDS_KEYS:
            self.assertTrue(result["what_stands"][key], key)
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["bounded_form_only"])
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["does_not_combine_into_operation"])
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["does_not_combine_into_continuation"])
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["does_not_combine_into_synchronization"])
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["does_not_combine_into_full_body_transfer"])
        self.assertTrue(result["what_stands"]["raw_declared_basis"]["does_not_combine_into_final_completion"])

        for key in WHAT_DOES_NOT_STAND_KEYS:
            self.assertTrue(result["what_does_not_stand"][key], key)
        for key in WHAT_IS_CLOSED_KEYS:
            self.assertTrue(result["what_is_closed"][key], key)
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["orientation_closure_only"])
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["not_closure_of_distributed_standing_implementation"])
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["not_closure_of_operation"])
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["not_closure_of_final_governance"])
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["not_closure_of_final_continuity_completion"])
        self.assertTrue(result["what_is_closed"]["raw_declared_basis"]["not_closure_of_final_system_identity"])

    def test_what_remains_open_non_meaning_checks_summary_and_non_claims(self) -> None:
        result = resolve_request(valid_request())

        for key in OPEN_KEYS:
            self.assertIn(key, result["what_remains_open"])
        self.assertTrue(result["what_remains_open"]["open_means_not_scheduled"])
        self.assertTrue(result["what_remains_open"]["open_means_not_authorized"])
        self.assertTrue(result["what_remains_open"]["open_means_not_executed"])

        for check in result["orientation_checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)
            self.assertTrue(check["passed"], check["check_name"])
        self.assertEqual(0, result["current_self_orientation_v9_summary"]["failed_check_count"])

        check_names = {check["check_name"] for check in result["orientation_checks"]}
        for expected in (
            "orientation question declared",
            "orientation intent supported",
            "prior self-orientation present",
            "distributed standing conformance closure present",
            "distributed standing conformance closure outcome present",
            "distributed standing conformance closure outcome closed",
            "distributed standing conformance closure failed check count zero",
            "current-body conformance v3 closure basis preserved",
            "what stands present",
            "what does not stand present",
            "what remains open present",
            "no continuation",
            "no operation",
            "no repository sync",
            "no full body transfer",
            "no second body",
            "no permission",
            "no authority",
            "no truth action",
            "no final completion",
            "no follow-on work authorization",
            "no prior result mutation",
            "no mutation replay or merge",
            "non-claims remain false",
        ):
            self.assertIn(expected, check_names)

        for key in ORIENTATION_NON_MEANING_KEYS:
            self.assertTrue(result["orientation_non_meaning"][key], key)

        summary = resolver.build_current_self_orientation_v9_summary(result)
        for key in (
            "outcome",
            "block_code",
            "block_reason",
            "orientation_request_id",
            "orientation_question",
            "orientation_intent",
            "passed_check_count",
            "failed_check_count",
            "current_self_orientation_v9_recorded",
            "prior_self_orientation_preserved",
            "v8_preserved_as_lineage",
            "distributed_standing_conformance_closure_preserved",
            "distributed_standing_conformance_closure_closed",
            "distributed_standing_conformance_closure_failed_check_count_zero",
            "current_body_conformance_v3_closure_basis_preserved",
            "what_stands_preserved",
            "what_does_not_stand_preserved",
            "what_is_closed_preserved",
            "what_remains_open_preserved",
            "orientation_did_not_create_permission",
            "orientation_did_not_authorize_continuation",
            "orientation_did_not_authorize_operation",
            "orientation_did_not_authorize_repository_sync",
            "orientation_did_not_authorize_full_body_transfer",
            "orientation_did_not_create_second_body",
            "orientation_did_not_claim_final_completion",
            "orientation_did_not_schedule_follow_on_work",
            "orientation_did_not_mutate_prior_result",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(RECORDED, summary["outcome"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertTrue(summary["current_self_orientation_v9_recorded"])
        self.assertResultNonClaimsFalse(result)

    def test_result_level_non_claims_for_recorded_not_recorded_and_blocked(self) -> None:
        recorded = resolve_request(valid_request())
        not_recorded = resolve_request(
            valid_request(intent="DO_NOT_RECORD_CURRENT_SELF_ORIENTATION_V9")
        )
        blocked = resolve_request(valid_request(intent="BLOCK_CURRENT_SELF_ORIENTATION_V9"))

        self.assertEqual(NOT_RECORDED, not_recorded["outcome"])
        self.assertFalse(not_recorded["orientation_statement"]["current_self_orientation_v9_recorded"])
        self.assertIn("not_recorded_reason", not_recorded["block"])
        self.assertEqual(BLOCKED, blocked["outcome"])

        for result in (recorded, not_recorded, blocked):
            self.assertOutcomeFamily(result)
            self.assertResultNonClaimsFalse(result)

    def test_request_builder_helper_records_v9(self) -> None:
        request = resolver.build_declared_current_self_orientation_v9_request(
            "current_self_orientation_v9_helper_001",
            "What is the body's current orientation after distributed standing boundary conformance closure?",
            selected_v8(),
            selected_closure(),
            orientation_basis(),
            what_stands(),
            what_does_not_stand(),
            what_is_closed(),
            what_remains_open(),
            current_body_conformance_v3_closure_basis=current_body_basis(),
        )
        request["distributed_standing_boundary_result_reference"] = "carrier_b_c_distributed_standing_boundary_001"
        request["distributed_standing_boundary_conformance_reference"] = "carrier_b_c_distributed_standing_boundary_conformance_001"

        self.assertEqual("current_self_orientation_v9_helper_001", request["orientation_request_id"])
        self.assertIn("current orientation", request["orientation_question"])
        self.assertEqual(selected_v8(), request["selected_prior_self_orientation"])
        self.assertEqual(selected_closure(), request["selected_distributed_standing_conformance_closure"])
        self.assertEqual(orientation_basis(), request["orientation_basis"])
        self.assertEqual(what_stands(), request["what_stands"])
        self.assertEqual(what_does_not_stand(), request["what_does_not_stand"])
        self.assertEqual(what_is_closed(), request["what_is_closed"])
        self.assertEqual(what_remains_open(), request["what_remains_open"])
        self.assertEqual(current_body_basis(), request["current_body_conformance_v3_closure_basis"])
        self.assertEqual(required_non_claims(), request["declared_non_claims"])
        self.assertRecorded(resolve_request(request))

    def test_path_based_selected_prior_and_closure_result(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            prior_path = tmp_path / "selected_v8.json"
            closure_path = tmp_path / "selected_closure.json"
            prior_path.write_text(json.dumps(selected_v8()), encoding="utf-8")
            closure_path.write_text(json.dumps(selected_closure()), encoding="utf-8")

            request = valid_request(
                selected_prior_self_orientation_path=str(prior_path),
                selected_conformance_closure_path=str(closure_path),
            )
            result = resolve_request(request)

            self.assertRecorded(result)
            self.assertEqual(str(prior_path), result["selected_prior_self_orientation"]["selected_prior_self_orientation_path"])
            self.assertEqual(str(closure_path), result["selected_distributed_standing_conformance_closure"]["selected_conformance_closure_path"])
            self.assertEqual("current_self_orientation_v8_001", result["selected_prior_self_orientation"]["selected_prior_self_orientation_id"])
            self.assertEqual(
                "carrier_b_c_distributed_standing_boundary_conformance_closure_001",
                result["selected_distributed_standing_conformance_closure"]["selected_conformance_closure_id"],
            )
            self.assertEqual(CLOSED, result["selected_distributed_standing_conformance_closure"]["selected_conformance_closure_outcome"])

    def test_path_based_orientation_request(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            request_path = Path(tmp) / "orientation_request.json"
            request_path.write_text(json.dumps(valid_request()), encoding="utf-8")

            result = resolver.resolve_current_self_orientation_v9_from_path(request_path)

            self.assertRecorded(result)
            self.assertEqual(str(request_path), result["declared_orientation_question"]["orientation_request_path"])
            self.assertEqual(TOP_LEVEL_SECTIONS, TOP_LEVEL_SECTIONS & set(result))

    def test_write_behavior_and_default_output_path(self) -> None:
        result = resolve_request(valid_request())
        with tempfile.TemporaryDirectory() as tmp:
            explicit_path = Path(tmp) / "nested" / "v9_result.json"
            written = resolver.write_current_self_orientation_v9_result(result, explicit_path)
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.exists())
            parsed = json.loads(written.read_text(encoding="utf-8"))
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))

            self.assertNotIn("current_self_orientation_v8", str(resolver.CURRENT_SELF_ORIENTATION_V9_ROOT))
            with patch.object(resolver, "CURRENT_SELF_ORIENTATION_V9_ROOT", Path(tmp) / "v9_root"):
                first = resolver.write_current_self_orientation_v9_result(result)
                second = resolver.write_current_self_orientation_v9_result(result)
                self.assertEqual(Path(tmp) / "v9_root", first.parent)
                self.assertTrue(first.name.endswith("__current_self_orientation_v9_result.json"))
                self.assertTrue(second.name.endswith("_001.json"))
                self.assertNotEqual(first, second)

    def test_non_mutation_posture(self) -> None:
        request = valid_request()
        request_before = copy.deepcopy(request)
        prior_before = copy.deepcopy(request["selected_prior_self_orientation"])
        closure_before = copy.deepcopy(request["selected_distributed_standing_conformance_closure"])

        first = resolve_request(request)
        second = resolve_request(request)

        self.assertEqual(request_before, request)
        self.assertEqual(prior_before, request["selected_prior_self_orientation"])
        self.assertEqual(closure_before, request["selected_distributed_standing_conformance_closure"])
        self.assertRecorded(first)
        self.assertRecorded(second)

        with tempfile.TemporaryDirectory() as tmp:
            prior_path = Path(tmp) / "v8.json"
            closure_path = Path(tmp) / "closure.json"
            prior_text = json.dumps(selected_v8(), sort_keys=True)
            closure_text = json.dumps(selected_closure(), sort_keys=True)
            prior_path.write_text(prior_text, encoding="utf-8")
            closure_path.write_text(closure_text, encoding="utf-8")
            request_with_paths = valid_request(
                selected_prior_self_orientation_path=str(prior_path),
                selected_conformance_closure_path=str(closure_path),
            )
            result = resolve_request(request_with_paths)
            resolver.write_current_self_orientation_v9_result(result, Path(tmp) / "out" / "v9.json")
            self.assertEqual(prior_text, prior_path.read_text(encoding="utf-8"))
            self.assertEqual(closure_text, closure_path.read_text(encoding="utf-8"))

    def test_explicit_block_missing_and_malformed_request(self) -> None:
        explicit = resolve_request(valid_request(intent="BLOCK_CURRENT_SELF_ORIENTATION_V9"))
        self.assertBlockedCode(explicit, "ORIENTATION_REQUEST_EXPLICITLY_BLOCKED")
        self.assertFalse(explicit["orientation_statement"]["current_self_orientation_v9_recorded"])

        missing = resolver.resolve_current_self_orientation_v9()
        self.assertBlockedCode(missing, "ORIENTATION_QUESTION_UNDECLARED")

        malformed = resolver.resolve_current_self_orientation_v9(declared_orientation_request=[])
        self.assertBlockedCode(malformed, "DECLARED_ORIENTATION_REQUEST_MALFORMED")

    def test_orientation_request_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_current_self_orientation_v9_from_path(tmp_path / "missing.json")
            self.assertBlockedCode(missing, "DECLARED_ORIENTATION_REQUEST_UNREADABLE")

            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed = resolver.resolve_current_self_orientation_v9_from_path(malformed_path)
            self.assertBlockedCode(malformed, "DECLARED_ORIENTATION_REQUEST_MALFORMED")

            array_path = tmp_path / "array.json"
            array_path.write_text("[]", encoding="utf-8")
            array_result = resolver.resolve_current_self_orientation_v9_from_path(array_path)
            self.assertBlockedCode(array_result, "DECLARED_ORIENTATION_REQUEST_MALFORMED")

    def test_selected_closure_path_unreadable_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing_request = valid_request(selected_conformance_closure_path=str(tmp_path / "missing.json"))
            self.assertBlockedCode(
                resolve_request(missing_request),
                "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_UNREADABLE",
            )

            malformed_path = tmp_path / "bad_closure.json"
            malformed_path.write_text("{", encoding="utf-8")
            malformed_request = valid_request(selected_conformance_closure_path=str(malformed_path))
            self.assertBlockedCode(
                resolve_request(malformed_request),
                "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
            )

            array_path = tmp_path / "array_closure.json"
            array_path.write_text("[]", encoding="utf-8")
            array_request = valid_request(selected_conformance_closure_path=str(array_path))
            self.assertBlockedCode(
                resolve_request(array_request),
                "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
            )

    def test_question_intent_and_prior_orientation_blocks(self) -> None:
        cases = [
            ("orientation_question", "", "ORIENTATION_QUESTION_UNDECLARED"),
            ("orientation_intent", "UNSUPPORTED_CURRENT_SELF_ORIENTATION_V9", "ORIENTATION_INTENT_UNSUPPORTED"),
            ("selected_prior_self_orientation", None, "PRIOR_SELF_ORIENTATION_MISSING"),
        ]
        for key, value, expected in cases:
            with self.subTest(expected=expected):
                request = valid_request()
                if value is None:
                    request.pop(key)
                else:
                    request[key] = value
                self.assertBlockedCode(resolve_request(request), expected)

    def test_selected_closure_missing_malformed_outcome_and_failed_count_blocks(self) -> None:
        missing = valid_request()
        missing.pop("selected_distributed_standing_conformance_closure")
        self.assertBlockedCode(
            resolve_request(missing),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MISSING",
        )

        malformed = valid_request(closure=["not", "a", "mapping"])  # type: ignore[arg-type]
        self.assertBlockedCode(
            resolve_request(malformed),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
        )

        not_closure_result = valid_request(
            closure={
                "result_id": "not_a_closure_result",
                "outcome": CLOSED,
                "distributed_standing_boundary_conformance_closure_summary": {
                    "failed_check_count": 0
                },
            }
        )
        self.assertBlockedCode(
            resolve_request(not_closure_result),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_MALFORMED",
        )

        no_outcome_closure = selected_closure()
        no_outcome_closure.pop("outcome")
        no_outcome_closure["distributed_standing_boundary_conformance_closure_summary"].pop("outcome")
        no_outcome = valid_request(closure=no_outcome_closure)
        no_outcome.pop("selected_conformance_closure_outcome", None)
        self.assertBlockedCode(
            resolve_request(no_outcome),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_OUTCOME_MISSING",
        )

        not_closed = valid_request(
            closure=with_closure_change(
                {"outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_NOT_CLOSED"},
                summary={"outcome": "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_NOT_CLOSED"},
            )
        )
        not_closed["selected_conformance_closure_outcome"] = (
            "DISTRIBUTED_STANDING_BOUNDARY_CONFORMANCE_NOT_CLOSED"
        )
        self.assertBlockedCode(
            resolve_request(not_closed),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_NOT_CLOSED",
        )

        failed_closure = selected_closure()
        failed_closure["distributed_standing_boundary_conformance_closure_summary"][
            "failed_check_count"
        ] = 1
        self.assertBlockedCode(
            resolve_request(valid_request(closure=failed_closure)),
            "DISTRIBUTED_STANDING_CONFORMANCE_CLOSURE_HAS_FAILED_CHECKS",
        )

    def test_required_basis_missing_blocks(self) -> None:
        cases = [
            ("current_body_conformance_v3_closure_basis", "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BASIS_MISSING"),
            ("what_stands", "WHAT_STANDS_MISSING"),
            ("what_does_not_stand", "WHAT_DOES_NOT_STAND_MISSING"),
            ("what_is_closed", "WHAT_IS_CLOSED_MISSING"),
            ("what_remains_open", "WHAT_REMAINS_OPEN_MISSING"),
        ]
        for key, expected in cases:
            with self.subTest(expected=expected):
                request = valid_request()
                request.pop(key)
                self.assertBlockedCode(resolve_request(request), expected)

    def test_orientation_collapse_flags_block(self) -> None:
        cases = [
            ("continuation_authorized", "ORIENTATION_AUTHORIZES_CONTINUATION"),
            ("orientation_authorizes_operation", "ORIENTATION_AUTHORIZES_OPERATION"),
            ("repository_synchronization_authorized", "ORIENTATION_AUTHORIZES_REPOSITORY_SYNC"),
            ("full_body_transfer_authorized", "ORIENTATION_AUTHORIZES_FULL_BODY_TRANSFER"),
            ("second_body_created", "ORIENTATION_CREATES_SECOND_BODY"),
            ("permission_created", "ORIENTATION_CREATES_PERMISSION"),
            ("authority_created", "ORIENTATION_CREATES_AUTHORITY"),
            ("truth_created", "ORIENTATION_CREATES_TRUTH_OR_ACTION"),
            ("orientation_claims_final_completion", "ORIENTATION_CLAIMS_FINAL_COMPLETION"),
            ("follow_on_work_authorized", "ORIENTATION_SCHEDULES_FOLLOW_ON_WORK"),
            ("self_orientation_successor_scheduled", "ORIENTATION_SCHEDULES_FOLLOW_ON_WORK"),
            ("orientation_mutates_prior_result", "ORIENTATION_MUTATES_PRIOR_RESULT"),
        ]
        for flag, expected in cases:
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assertBlockedCode(resolve_request(request), expected)

    def test_mutation_replay_merge_blocks(self) -> None:
        for flag in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(flag=flag):
                request = valid_request()
                request[flag] = True
                self.assertBlockedCode(resolve_request(request), "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_required_non_claim_missing_or_flipped_blocks(self) -> None:
        missing = valid_request()
        missing["declared_non_claims"].pop("permission_created")
        missing_result = resolve_request(missing)
        self.assertEqual(BLOCKED, missing_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(missing_result))

        flipped = valid_request()
        flipped["declared_non_claims"]["permission_created"] = True
        flipped_result = resolve_request(flipped)
        self.assertEqual(BLOCKED, flipped_result["outcome"])
        self.assertIn("NON_CLAIM_MISSING_OR_FLIPPED", failed_codes(flipped_result))


if __name__ == "__main__":
    unittest.main()
