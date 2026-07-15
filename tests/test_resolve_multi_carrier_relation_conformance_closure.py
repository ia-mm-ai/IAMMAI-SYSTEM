"""Tests for bounded multi-carrier relation conformance closure.

This suite audits one closure resolver. It verifies that closure records the
meaning of one selected MULTI_CARRIER_RELATION_CONFORMANT result only, without
performing conformance, creating relation, selecting carriers, creating
currentness, resolving divergence, creating distributed standing, authorizing
continuation, authorizing another carrier experiment, authorizing distributed
operation, or forcing a successor.
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

import resolve_multi_carrier_relation_conformance_closure as resolver


TOP_LEVEL_SECTIONS = {
    "multi_carrier_relation_conformance_closure_metadata",
    "declared_closure_question",
    "selected_conformance",
    "selected_relation",
    "selected_carriers",
    "selected_carrier_evidence",
    "closure_basis",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "multi_carrier_relation_conformance_closure_summary",
}

EXPECTED_CHECK_NAMES = {
    "selected_conformance_result_exists",
    "selected_conformance_result_parseable_mapping",
    "selected_conformance_result_outcome_conformant",
    "selected_relation_id_type_question_preserved",
    "selected_relation_basis_preserved",
    "selected_carriers_preserved",
    "selected_evidence_preserved",
    "conformance_checks_passed",
    "failed_check_count_zero_where_exposed",
    "relation_conformance_statement_preserved",
    "relation_conformance_non_meaning_preserved",
    "visible_refusal_preserved_where_applicable",
    "visible_divergence_preserved_where_applicable",
    "currentness_participation_remained_participation",
    "current_carrier_not_selected",
    "winning_carrier_not_selected",
    "losing_carrier_not_invalidated",
    "carrier_hierarchy_not_created",
    "source_not_replaced",
    "currentness_not_created",
    "authority_not_created",
    "permission_not_created",
    "successor_not_created",
    "body_not_created",
    "signal_not_created_by_default",
    "presence_not_established",
    "threshold_not_met",
    "truth_not_created",
    "action_not_authorized",
    "consequence_not_created",
    "distributed_standing_not_created",
    "continuation_not_authorized",
    "additional_carrier_experiment_not_authorized",
    "distributed_operation_not_authorized",
    "closure_does_not_create_authority",
    "closure_does_not_create_permission",
    "closure_does_not_create_currentness",
    "closure_does_not_create_distributed_standing",
    "closure_does_not_authorize_continuation",
    "closure_does_not_authorize_expansion",
    "closure_does_not_force_self_orientation_successor",
    "closure_does_not_force_conformance_successor",
    "hidden_refusal_false",
    "hidden_divergence_false",
    "divergence_not_resolved",
    "mutation_replay_merge_false",
    "required_non_claims_remain_false",
}

CLOSURE_NON_MEANING_TRUE_KEYS = {
    "does_not_mean_distributed_standing",
    "does_not_mean_currentness",
    "does_not_mean_authority",
    "does_not_mean_permission",
    "does_not_mean_source_replacement",
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
    "does_not_mean_carrier_registry",
    "does_not_mean_persistence",
    "does_not_mean_signal_by_default",
    "does_not_mean_presence",
    "does_not_mean_threshold",
    "does_not_mean_truth",
    "does_not_mean_action",
    "does_not_mean_consequence",
    "does_not_mean_continuation",
    "does_not_mean_permission_for_another_carrier",
    "does_not_mean_permission_for_distributed_operation",
    "does_not_mean_final_governance",
    "does_not_mean_final_system_identity",
    "does_not_mean_continuity_completion",
    "does_not_mean_conformance_created_permission",
    "does_not_mean_conformance_created_authority",
    "does_not_mean_conformance_created_currentness",
    "does_not_mean_conformance_authorized_continuation",
    "does_not_mean_closure_authorized_expansion",
    "does_not_mean_self_orientation_successor_forced",
    "does_not_mean_conformance_successor_forced",
}

OPEN_SURFACES = {
    "multi-carrier relation conformance closure implementation refinement",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "successor carrier law",
    "future self-orientation successor only if separately justified",
    "additional physical-carrier experiment only if separately declared and bounded",
    "distributed operation only if separately declared and bounded",
}

OUTCOME_FAMILY = {
    "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
    "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED",
    "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED",
}


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    assert isinstance(loaded, dict)
    return loaded


def _selected_non_claims(**updates: bool) -> dict[str, bool]:
    claims = {key: False for key in resolver.SELECTED_CONFORMANCE_REQUIRED_NON_CLAIMS}
    claims.update(updates)
    return claims


def _closure_non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _carrier(carrier_id: str, role: str) -> dict[str, object]:
    return {
        "carrier_id": carrier_id,
        "carrier_role": role,
        "role_bounded": True,
        "role_operation_local": True,
        "selected_only_for_relation_conformance": True,
        "current_carrier_selected": False,
        "carrier_hierarchy_created": False,
    }


def _evidence(
    evidence_id: str,
    *,
    outcome: str,
    evidence_class: str,
    emission_class: str,
    currentness_status: str,
    non_claims: dict[str, bool] | None = None,
) -> dict[str, object]:
    return {
        "evidence_id": evidence_id,
        "evidence_outcome": outcome,
        "carrier_id": "carrier_B_physical_macbook",
        "carrier_role": "RECEIVING_CARRIER",
        "evidence_class": evidence_class,
        "emission_class": emission_class,
        "source_or_carried_basis": "current_body_standing_closure_post_conformance",
        "admission_status": (
            "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE"
            if outcome == "CARRIED_SURFACE_RECEIVED"
            else "CARRIER_LOCAL_EMISSION_NOT_ADMITTED"
        ),
        "correspondence_status": (
            "CORRESPONDENCE_RECOGNIZED"
            if outcome == "CARRIED_SURFACE_RECEIVED"
            else None
        ),
        "divergence_status": "CARRIER_DIVERGENCE_RECORDED",
        "currentness_participation_status": currentness_status,
        "return_path": (
            "artifacts/integrity_host_v0_min_coexistence_cross_carrier_surface_receipt_boundary/"
            "returned_from_carrier_B/current_body_standing_closure_post_conformance__cross_carrier_surface_receipt_result.json"
            if outcome == "CARRIED_SURFACE_RECEIVED"
            else None
        ),
        "return_context": {
            "return_posture": "returned_evidence_remains_downstream",
            "visible_refusal_preserved": outcome == "BLOCKED",
        },
        "integrity_evidence": {
            "hash_algorithm": "sha256",
            "hash": "b" * 64,
            "integrity_posture": "preserved_where_supplied",
        },
        "block_code": "CARRIED_SURFACE_MALFORMED" if outcome == "BLOCKED" else None,
        "non_claims": copy.deepcopy(non_claims or _selected_non_claims()),
    }


def _conformance_check(name: str) -> dict[str, object]:
    return {
        "check_name": name,
        "passed": True,
        "expected_posture": f"{name} passes",
        "actual_posture": True,
        "block_code": None,
    }


def _selected_conformance(**overrides: object) -> dict[str, object]:
    carriers = [
        _carrier("carrier_A_current_macbook", "SOURCE_CARRIER_FOR_PACKET"),
        _carrier("carrier_B_physical_macbook", "RECEIVING_CARRIER"),
    ]
    evidence = [
        _evidence(
            "carrier_B_returned_blocked__current_body_standing_closure_post_conformance__receipt",
            outcome="BLOCKED",
            evidence_class="RETURNED_BLOCKED_RECEIPT_EVIDENCE",
            emission_class="RECEIPT_BLOCK",
            currentness_status="CURRENTNESS_PARTICIPATION_EXCLUDED",
        ),
        _evidence(
            "carrier_B_returned_received__current_body_standing_closure_post_conformance__receipt",
            outcome="CARRIED_SURFACE_RECEIVED",
            evidence_class="RETURNED_SUCCESSFUL_RECEIPT_EVIDENCE",
            emission_class="CARRIED_SURFACE_RECEIPT",
            currentness_status="CURRENTNESS_PARTICIPATION_ELIGIBLE",
        ),
    ]
    selected_carrier_ids = [
        "carrier_A_current_macbook",
        "carrier_B_physical_macbook",
    ]
    selected_evidence_ids = [str(item["evidence_id"]) for item in evidence]
    selected_evidence_outcomes = [str(item["evidence_outcome"]) for item in evidence]
    relation_question = (
        "May Carrier B returned blocked receipt evidence and returned successful "
        "receipt evidence stand in bounded multi-carrier relation without creating "
        "currentness, hierarchy, distributed standing, truth, action, or continuation?"
    )
    relation_type = "REFUSAL_SUCCESS_RELATION"
    relation_id = (
        "carrier_b_refusal_success_multi_carrier_relation_001__"
        "multi_carrier_relation_recognized__multi_carrier_relation_result"
    )
    conformance_id = (
        "carrier_b_refusal_success_multi_carrier_relation_001__"
        "multi_carrier_relation_conformant__multi_carrier_relation_conformance_result"
    )
    non_claims = _selected_non_claims()
    conformance_checks = [
        _conformance_check("selected_relation_result_exists"),
        _conformance_check("selected_relation_result_parseable_mapping"),
        _conformance_check("selected_relation_result_outcome_recognized"),
        _conformance_check("selected_relation_type_supported"),
        _conformance_check("selected_relation_question_declared"),
        _conformance_check("selected_carriers_preserved"),
        _conformance_check("selected_carrier_evidence_preserved"),
        _conformance_check("selected_evidence_identities_preserved"),
        _conformance_check("selected_evidence_outcomes_preserved"),
        _conformance_check("carrier_roles_preserved"),
        _conformance_check("local_outcomes_preserved"),
        _conformance_check("relation_basis_preserved"),
        _conformance_check("visible_refusal_preserved_where_applicable"),
        _conformance_check("visible_divergence_preserved_where_applicable"),
        _conformance_check("currentness_participation_remained_participation"),
        _conformance_check("current_carrier_not_selected"),
        _conformance_check("winning_carrier_not_selected"),
        _conformance_check("losing_carrier_not_invalidated"),
        _conformance_check("carrier_hierarchy_not_created"),
        _conformance_check("source_not_replaced"),
        _conformance_check("currentness_not_created"),
        _conformance_check("authority_not_created"),
        _conformance_check("permission_not_created"),
        _conformance_check("distributed_standing_not_created"),
        _conformance_check("continuation_not_authorized"),
        _conformance_check("additional_carrier_experiment_not_authorized"),
        _conformance_check("distributed_operation_not_authorized"),
        _conformance_check("required_non_claims_remain_false"),
    ]
    conformance = {
        "multi_carrier_relation_conformance_metadata": {
            "multi_carrier_relation_conformance_result_id": conformance_id,
            "multi_carrier_relation_conformance_result_type": "multi_carrier_relation_conformance_result",
            "multi_carrier_relation_conformance_result_version": "0.1.0",
            "generated_at": "2026-04-28T00:00:00+00:00",
            "resolver_module": "run_multi_carrier_relation_conformance",
        },
        "declared_conformance_question": {
            "conformance_question": "Does this selected recognized multi-carrier relation cohere without collapse?",
            "selected_relation_result_id": relation_id,
            "selected_relation_type": relation_type,
            "selected_relation_question": relation_question,
            "conformance_is_over_one_selected_recognized_relation": True,
            "conformance_does_not_close_itself": True,
            "conformance_authorizes_continuation": False,
        },
        "selected_relation": {
            "selected_relation_result_id": relation_id,
            "selected_relation_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary/"
                f"{relation_id}.json"
            ),
            "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "selected_relation_type": relation_type,
            "selected_relation_question": relation_question,
            "selected_relation_preserved": True,
            "selected_relation_only": True,
            "selected_relation_not_currentness": True,
            "selected_relation_not_distributed_standing": True,
        },
        "selected_relation_basis": {
            "selected_relation_result_id": relation_id,
            "selected_relation_result_path": (
                "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary/"
                f"{relation_id}.json"
            ),
            "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "selected_relation_type": relation_type,
            "selected_relation_question": relation_question,
            "selected_relation_recognized": True,
            "selected_relation_basis_preserved": True,
            "relation_checks_preserved": True,
            "selected_carrier_count": 2,
            "selected_evidence_count": 2,
            "selected_carrier_ids": selected_carrier_ids,
            "selected_evidence_ids": selected_evidence_ids,
            "selected_evidence_outcomes": selected_evidence_outcomes,
            "relation_evidence": {
                "has_refusal_evidence": True,
                "has_success_evidence": True,
                "has_visible_divergence": True,
                "has_currentness_participation_evidence": True,
            },
            "passed_relation_check_count": 28,
            "failed_relation_check_count": 0,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "downstream_evidence_posture_preserved": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "relation_non_claims_false": True,
            "selected_relation_non_claims": copy.deepcopy(non_claims),
        },
        "selected_carriers": carriers,
        "selected_carrier_evidence": evidence,
        "relation_conformance_checks": conformance_checks,
        "relation_conformance_statement": {
            "relation_conformant": True,
            "selected_relation_preserved": True,
            "selected_carriers_preserved": True,
            "selected_evidence_preserved": True,
            "carrier_roles_preserved": True,
            "local_outcomes_preserved": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "downstream_evidence_posture_preserved": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "carrier_hierarchy_created": False,
            "distributed_standing_created": False,
            "source_replaced": False,
            "currentness_created": False,
            "authority_created": False,
            "permission_created": False,
            "presence_threshold_truth_action_consequence_created": False,
            "continuation_authorized": False,
            "additional_carrier_experiment_authorized": False,
            "distributed_operation_authorized": False,
        },
        "relation_conformance_non_meaning": {
            "does_not_mean_distributed_standing": True,
            "does_not_mean_currentness": True,
            "does_not_mean_authority": True,
            "does_not_mean_permission": True,
            "does_not_mean_source_replacement": True,
            "does_not_mean_carrier_hierarchy": True,
            "does_not_mean_current_carrier_selected": True,
            "does_not_mean_winning_carrier_selected": True,
            "does_not_mean_losing_carrier_invalidated": True,
            "does_not_mean_divergence_resolved": True,
            "does_not_mean_continuation": True,
            "does_not_mean_permission_for_another_carrier": True,
            "does_not_mean_permission_for_distributed_operation": True,
        },
        "what_remains_open": {
            "open_items": [
                {"name": "multi-carrier relation conformance closure", "scheduled": False, "authorized": False, "executed": False},
                {"name": "distributed standing", "scheduled": False, "authorized": False, "executed": False},
            ],
            "open_means_not_scheduled": True,
            "open_means_not_authorized": True,
            "open_means_not_executed": True,
        },
        "non_claims": non_claims,
        "outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
        "block": {
            "code": None,
            "reason": None,
            "block_code": None,
            "block_reason": None,
        },
        "multi_carrier_relation_conformance_summary": {
            "outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
            "block_code": None,
            "block_reason": None,
            "selected_relation_id": relation_id,
            "selected_relation_path": (
                "artifacts/integrity_host_v0_min_coexistence_multi_carrier_relation_boundary/"
                f"{relation_id}.json"
            ),
            "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "selected_relation_type": relation_type,
            "selected_relation_question": relation_question,
            "selected_carrier_count": 2,
            "selected_evidence_count": 2,
            "selected_carrier_ids": selected_carrier_ids,
            "selected_evidence_ids": selected_evidence_ids,
            "selected_evidence_outcomes": selected_evidence_outcomes,
            "passed_check_count": len(conformance_checks),
            "failed_check_count": 0,
            "relation_conformant": True,
            "selected_relation_preserved": True,
            "selected_carriers_preserved": True,
            "selected_evidence_preserved": True,
            "carrier_roles_preserved": True,
            "local_outcomes_preserved": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "downstream_evidence_posture_preserved": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "carrier_hierarchy_created": False,
            "distributed_standing_created": False,
            "source_currentness_authority_permission_created": False,
            "presence_threshold_truth_action_consequence_created": False,
            "continuation_authorized": False,
            "additional_carrier_experiment_authorized": False,
            "distributed_operation_authorized": False,
            "key_non_claims": copy.deepcopy(non_claims),
        },
    }
    _deep_update(conformance, overrides)
    return conformance


def _deep_update(target: dict, updates: dict) -> None:
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_update(target[key], value)
        else:
            target[key] = value


def _failed_conformance_count(artifact: dict) -> int:
    checks = artifact.get("relation_conformance_checks")
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, dict) and check.get("passed") is False
        )
    summary = artifact.get("multi_carrier_relation_conformance_summary")
    if isinstance(summary, dict) and isinstance(summary.get("failed_check_count"), int):
        return int(summary["failed_check_count"])
    return 0


class MultiCarrierRelationConformanceClosureTests(unittest.TestCase):
    def _resolve(self, conformance: dict | None = None) -> dict:
        return resolver.resolve_multi_carrier_relation_conformance_closure(
            selected_conformance_result=(
                _selected_conformance() if conformance is None else conformance
            )
        )

    def _assert_top_level_shape(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def _assert_closed(self, result: dict) -> None:
        self._assert_top_level_shape(result)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertTrue(result["closure_statement"]["relation_conformance_closed"])
        self.assertEqual(
            0,
            result["multi_carrier_relation_conformance_closure_summary"]["failed_check_count"],
        )

    def _assert_blocked(self, result: dict, expected_codes: set[str]) -> None:
        self._assert_top_level_shape(result)
        self.assertEqual(
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_BLOCKED",
            result["outcome"],
        )
        self.assertIn(result["block"]["block_code"], expected_codes)
        self.assertFalse(result["closure_statement"]["relation_conformance_closed"])

    def _assert_false_non_claims(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in resolver.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_successful_closure_mapping_path(self) -> None:
        result = self._resolve()

        self._assert_closed(result)
        metadata = result["multi_carrier_relation_conformance_closure_metadata"]
        self.assertTrue(metadata["multi_carrier_relation_conformance_closure_result_id"])
        self.assertTrue(metadata["multi_carrier_relation_conformance_closure_result_type"])
        self.assertEqual(
            "0.1.0",
            metadata["multi_carrier_relation_conformance_closure_result_version"],
        )
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(
            "resolve_multi_carrier_relation_conformance_closure",
            metadata["resolver_module"],
        )

    def test_declared_question_and_selected_conformance_are_preserved(self) -> None:
        result = self._resolve()
        question = result["declared_closure_question"]
        selected = result["selected_conformance"]

        self.assertIn("What does this selected", question["closure_question"])
        self.assertEqual(
            selected["selected_conformance_result_id"],
            question["selected_conformance_result_id"],
        )
        self.assertEqual(
            "MULTI_CARRIER_RELATION_CONFORMANT",
            question["selected_conformance_outcome"],
        )
        self.assertEqual(
            selected["selected_relation_result_id"],
            question["selected_relation_result_id"],
        )
        self.assertEqual("REFUSAL_SUCCESS_RELATION", question["selected_relation_type"])
        self.assertTrue(question["closure_is_over_one_selected_conformant_relation"])
        self.assertFalse(question["closure_performs_conformance"])
        self.assertFalse(question["closure_authorizes_continuation"])
        self.assertFalse(question["closure_authorizes_additional_carrier_experiment"])
        self.assertFalse(question["closure_authorizes_distributed_operation"])

    def test_selected_conformance_relation_carriers_and_evidence_are_preserved(self) -> None:
        result = self._resolve()
        selected_conformance = result["selected_conformance"]
        selected_relation = result["selected_relation"]
        carriers = result["selected_carriers"]
        evidence = result["selected_carrier_evidence"]

        self.assertEqual(
            "MULTI_CARRIER_RELATION_CONFORMANT",
            selected_conformance["selected_conformance_outcome"],
        )
        self.assertEqual(
            "MULTI_CARRIER_RELATION_RECOGNIZED",
            selected_relation["selected_relation_outcome"],
        )
        self.assertEqual("REFUSAL_SUCCESS_RELATION", selected_relation["selected_relation_type"])
        self.assertTrue(selected_relation["selected_relation_preserved"])
        self.assertTrue(selected_relation["selected_relation_only"])
        self.assertTrue(selected_relation["selected_relation_not_currentness"])
        self.assertTrue(selected_relation["selected_relation_not_distributed_standing"])
        self.assertEqual(2, len(carriers))
        self.assertEqual(2, len(evidence))
        self.assertTrue(all(item["carrier_id"] for item in carriers))
        self.assertTrue(all(item["carrier_role"] for item in carriers))
        self.assertTrue(all(item["evidence_id"] for item in evidence))
        self.assertEqual(
            ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
            [item["evidence_outcome"] for item in evidence],
        )
        self.assertTrue(any(item["evidence_outcome"] == "BLOCKED" for item in evidence))
        self.assertTrue(any(item["divergence_status"] == "CARRIER_DIVERGENCE_RECORDED" for item in evidence))

    def test_closure_basis_preserves_meaning_only_posture(self) -> None:
        basis = self._resolve()["closure_basis"]

        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", basis["selected_conformance_outcome"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", basis["selected_relation_type"])
        self.assertTrue(basis["selected_relation_basis_preserved"])
        self.assertEqual(2, basis["selected_carrier_count"])
        self.assertEqual(2, basis["selected_evidence_count"])
        self.assertEqual(
            ["carrier_A_current_macbook", "carrier_B_physical_macbook"],
            basis["selected_carrier_ids"],
        )
        self.assertEqual(
            ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
            basis["selected_evidence_outcomes"],
        )
        self.assertGreater(basis["passed_conformance_check_count"], 0)
        self.assertEqual(0, basis["failed_conformance_check_count"])
        self.assertTrue(basis["relation_conformance_statement_preserved"])
        self.assertTrue(basis["relation_conformance_non_meaning_preserved"])
        self.assertTrue(basis["visible_refusal_preserved"])
        self.assertTrue(basis["visible_divergence_preserved"])
        self.assertTrue(basis["downstream_evidence_posture_preserved"])
        self.assertTrue(basis["currentness_participation_remained_participation"])
        self.assertTrue(basis["current_carrier_not_selected"])
        self.assertFalse(basis["winning_carrier_selected"])
        self.assertFalse(basis["losing_carrier_invalidated"])
        self.assertFalse(basis["additional_carrier_experiment_authorized"])
        self.assertFalse(basis["distributed_operation_authorized"])
        self.assertTrue(basis["closure_requested"])

    def test_closure_checks_are_complete_and_pass_for_closed_case(self) -> None:
        result = self._resolve()
        checks = result["closure_checks"]
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

    def test_closure_statement_preserves_closed_non_collapse_posture(self) -> None:
        statement = self._resolve()["closure_statement"]

        for key in (
            "relation_conformance_closed",
            "selected_conformance_preserved",
            "selected_relation_preserved",
            "selected_carriers_preserved",
            "selected_evidence_preserved",
            "conformance_meaning_recorded",
            "conformance_non_meaning_recorded",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "currentness_participation_remained_participation",
            "current_carrier_not_selected",
        ):
            self.assertIs(statement[key], True, key)
        for key in (
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "distributed_standing_created",
            "source_replaced",
            "currentness_created",
            "authority_created",
            "permission_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
            "closure_authorized_expansion",
            "self_orientation_successor_forced",
            "conformance_successor_forced",
        ):
            self.assertIs(statement[key], False, key)

    def test_closure_non_meaning_and_open_surfaces_are_preserved(self) -> None:
        result = self._resolve()
        non_meaning = result["closure_non_meaning"]
        open_section = result["what_remains_open"]

        for key in CLOSURE_NON_MEANING_TRUE_KEYS:
            self.assertIn(key, non_meaning)
            self.assertIs(non_meaning[key], True, key)
        open_names = {item["name"] for item in open_section["open_items"]}
        self.assertTrue(OPEN_SURFACES.issubset(open_names))
        for item in open_section["open_items"]:
            self.assertFalse(item["scheduled"])
            self.assertFalse(item["authorized"])
            self.assertFalse(item["executed"])
        self.assertTrue(open_section["open_means_not_scheduled"])
        self.assertTrue(open_section["open_means_not_authorized"])
        self.assertTrue(open_section["open_means_not_executed"])

    def test_summary_helper_preserves_bounded_summary(self) -> None:
        result = self._resolve()
        summary = resolver.build_multi_carrier_relation_conformance_closure_summary(result)

        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertTrue(summary["selected_conformance_id"])
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", summary["selected_conformance_outcome"])
        self.assertTrue(summary["selected_relation_id"])
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", summary["selected_relation_outcome"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", summary["selected_relation_type"])
        self.assertEqual(2, summary["selected_carrier_count"])
        self.assertEqual(2, summary["selected_evidence_count"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        for key in (
            "relation_conformance_closed",
            "selected_conformance_preserved",
            "selected_relation_preserved",
            "selected_carriers_preserved",
            "selected_evidence_preserved",
            "conformance_meaning_recorded",
            "conformance_non_meaning_recorded",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "currentness_participation_remained_participation",
            "current_carrier_not_selected",
        ):
            self.assertIs(summary[key], True, key)
        for key in (
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "distributed_standing_created",
            "source_currentness_authority_permission_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
            "closure_authorized_expansion",
            "self_orientation_successor_forced",
            "conformance_successor_forced",
        ):
            self.assertIs(summary[key], False, key)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_are_false_for_all_outcome_families(self) -> None:
        closed = self._resolve()
        not_closed = self._resolve(_selected_conformance(closure_requested=False))
        blocked = resolver.resolve_multi_carrier_relation_conformance_closure(
            selected_conformance_result={}
        )

        self.assertEqual(
            "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED",
            not_closed["outcome"],
        )
        self._assert_false_non_claims(closed)
        self._assert_false_non_claims(not_closed)
        self._assert_false_non_claims(blocked)

    def test_real_artifact_discovery_path_when_available(self) -> None:
        root = (
            REPO_ROOT
            / "artifacts"
            / "integrity_host_v0_min_coexistence_multi_carrier_relation_conformance"
        )
        valid = []
        for path in root.glob("*.json"):
            try:
                loaded = _read_json(path)
            except (OSError, json.JSONDecodeError, AssertionError):
                continue
            if (
                loaded.get("outcome") == "MULTI_CARRIER_RELATION_CONFORMANT"
                and _failed_conformance_count(loaded) == 0
            ):
                valid.append(path)
        if not valid:
            self.skipTest("No standing MULTI_CARRIER_RELATION_CONFORMANT artifact is present.")

        result = resolver.resolve_multi_carrier_relation_conformance_closure()

        self._assert_closed(result)
        statement = result["closure_statement"]
        self.assertFalse(result["non_claims"]["latest_file_currentness"])
        self.assertFalse(statement["distributed_standing_created"])
        self.assertFalse(statement["continuation_authorized"])
        self.assertFalse(statement["additional_carrier_experiment_authorized"])
        self.assertFalse(statement["distributed_operation_authorized"])

    def test_path_based_resolution_preserves_path_and_shape(self) -> None:
        conformance = _selected_conformance()
        mapping_result = self._resolve(conformance)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "conformance.json"
            _write_json(path, conformance)

            path_result = resolver.resolve_multi_carrier_relation_conformance_closure_from_path(path)

        self._assert_closed(path_result)
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertEqual(
            str(path),
            path_result["selected_conformance"]["selected_conformance_result_path"],
        )

    def test_write_behavior_and_default_output_path_are_additive(self) -> None:
        result = self._resolve()
        with tempfile.TemporaryDirectory() as tmp:
            explicit_path = Path(tmp) / "nested" / "result.json"
            written = resolver.write_multi_carrier_relation_conformance_closure_result(
                result,
                explicit_path,
            )
            self.assertEqual(explicit_path, written)
            loaded = _read_json(written)
            self.assertEqual(TOP_LEVEL_SECTIONS, set(loaded))

            with mock.patch.object(
                resolver,
                "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT",
                Path(tmp) / "default",
            ):
                first = resolver.write_multi_carrier_relation_conformance_closure_result(result)
                second = resolver.write_multi_carrier_relation_conformance_closure_result(result)

        self.assertNotEqual(first, second)
        self.assertTrue(
            first.name.endswith("__multi_carrier_relation_conformance_closure_result.json")
        )
        self.assertIn("_001", second.stem)

    def test_non_mutation_posture(self) -> None:
        conformance = _selected_conformance()
        before = copy.deepcopy(conformance)

        first = self._resolve(conformance)
        second = self._resolve(conformance)

        self.assertEqual(before, conformance)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED", first["outcome"])
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED", second["outcome"])

    def test_not_closed_readable_conformance(self) -> None:
        result = self._resolve(_selected_conformance(closure_requested=False))

        self._assert_top_level_shape(result)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertFalse(result["closure_statement"]["relation_conformance_closed"])
        self.assertTrue(result["closure_statement"]["relation_conformance_not_closed"])
        self.assertTrue(result["closure_statement"]["selected_conformant_basis_preserved"])
        self.assertTrue(result["closure_statement"]["non_collapse_posture_preserved"])
        self.assertFalse(result["closure_statement"]["distributed_standing_created"])
        self.assertFalse(result["closure_statement"]["continuation_authorized"])

    def test_missing_and_malformed_conformance_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(
                resolver,
                "MULTI_CARRIER_RELATION_CONFORMANCE_ROOT",
                Path(tmp),
            ):
                missing = resolver.resolve_multi_carrier_relation_conformance_closure()
        malformed = resolver.resolve_multi_carrier_relation_conformance_closure(
            selected_conformance_result=["not", "mapping"]  # type: ignore[arg-type]
        )

        self._assert_blocked(missing, {"SELECTED_CONFORMANCE_MISSING"})
        self._assert_blocked(malformed, {"SELECTED_CONFORMANCE_MALFORMED"})

    def test_path_unreadable_and_malformed_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = resolver.resolve_multi_carrier_relation_conformance_closure_from_path(
                tmp_path / "missing.json"
            )
            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = resolver.resolve_multi_carrier_relation_conformance_closure_from_path(
                malformed_path
            )
            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            array_result = resolver.resolve_multi_carrier_relation_conformance_closure_from_path(
                array_path
            )

        self._assert_blocked(missing, {"SELECTED_CONFORMANCE_UNREADABLE"})
        self._assert_blocked(malformed, {"SELECTED_CONFORMANCE_MALFORMED"})
        self._assert_blocked(array_result, {"SELECTED_CONFORMANCE_MALFORMED"})

    def test_selected_conformance_not_conformant_blocks(self) -> None:
        for outcome in (
            "MULTI_CARRIER_RELATION_NONCONFORMANT",
            "MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED",
        ):
            conformance = _selected_conformance(outcome=outcome)
            with self.subTest(outcome=outcome):
                self._assert_blocked(
                    self._resolve(conformance),
                    {"SELECTED_CONFORMANCE_NOT_CONFORMANT"},
                )

    def test_selected_relation_basis_missing_blocks(self) -> None:
        missing_basis = _selected_conformance(selected_relation_basis=None)
        missing_id = _selected_conformance(
            declared_conformance_question={"selected_relation_result_id": None},
            selected_relation={"selected_relation_result_id": None},
            selected_relation_basis={"selected_relation_result_id": None},
            multi_carrier_relation_conformance_summary={"selected_relation_id": None},
        )

        self._assert_blocked(
            self._resolve(missing_basis),
            {"SELECTED_RELATION_BASIS_MISSING"},
        )
        self._assert_blocked(
            self._resolve(missing_id),
            {"SELECTED_RELATION_BASIS_MISSING"},
        )

    def test_selected_carriers_and_evidence_missing_block(self) -> None:
        no_carriers = self._resolve(_selected_conformance(selected_carriers=[]))
        no_evidence = self._resolve(_selected_conformance(selected_carrier_evidence=[]))

        self._assert_blocked(no_carriers, {"SELECTED_CARRIERS_MISSING"})
        self._assert_blocked(no_evidence, {"SELECTED_EVIDENCE_MISSING"})

    def test_conformance_checks_failed_or_hidden_block(self) -> None:
        failed = _selected_conformance()
        failed["relation_conformance_checks"][0]["passed"] = False
        failed["relation_conformance_checks"][0]["block_code"] = "SELECTED_RELATION_MISSING"
        hidden = _selected_conformance(relation_conformance_checks=[])

        self._assert_blocked(
            self._resolve(failed),
            {"CONFORMANCE_CHECKS_FAILED_OR_HIDDEN"},
        )
        self._assert_blocked(
            self._resolve(hidden),
            {"CONFORMANCE_CHECKS_FAILED_OR_HIDDEN"},
        )

    def test_hidden_refusal_and_divergence_block(self) -> None:
        refusal_hidden = _selected_conformance(non_claims=_selected_non_claims(refusal_hidden=True))
        divergence_hidden = _selected_conformance(non_claims=_selected_non_claims(divergence_hidden=True))
        mismatch_hidden = _selected_conformance(non_claims=_selected_non_claims(mismatch_hidden=True))

        self._assert_blocked(self._resolve(refusal_hidden), {"CLOSURE_HIDES_REFUSAL"})
        self._assert_blocked(self._resolve(divergence_hidden), {"CLOSURE_HIDES_DIVERGENCE"})
        self._assert_blocked(self._resolve(mismatch_hidden), {"CLOSURE_HIDES_DIVERGENCE"})

    def test_currentness_shortcut_blocks(self) -> None:
        latest = _selected_conformance(non_claims=_selected_non_claims(latest_file_currentness=True))
        currentness = _selected_conformance(non_claims=_selected_non_claims(currentness_created=True))
        current_carrier = _selected_conformance(non_claims=_selected_non_claims(current_carrier_selected=True))

        self._assert_blocked(
            self._resolve(latest),
            {"CLOSURE_CURRENTNESS_SHORTCUT", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self._assert_blocked(
            self._resolve(currentness),
            {"CLOSURE_CREATES_CURRENTNESS", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self._assert_blocked(
            self._resolve(current_carrier),
            {"CLOSURE_CURRENTNESS_SHORTCUT", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )

    def test_carrier_hierarchy_winning_losing_block(self) -> None:
        cases = [
            (
                _selected_conformance(non_claims=_selected_non_claims(carrier_hierarchy_created=True)),
                {"CLOSURE_CREATES_CARRIER_HIERARCHY", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(winning_carrier_selected=True)),
                {"CLOSURE_SELECTS_WINNING_CARRIER", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(losing_carrier_invalidated=True)),
                {"CLOSURE_INVALIDATES_LOSING_CARRIER", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
        ]
        for conformance, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(conformance), codes)

    def test_source_currentness_authority_permission_successor_body_collapse_blocks(self) -> None:
        cases = [
            (
                _selected_conformance(non_claims=_selected_non_claims(source_replaced=True)),
                {"CLOSURE_REPLACES_SOURCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(currentness_created=True)),
                {"CLOSURE_CREATES_CURRENTNESS", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(authority_created=True)),
                {"CLOSURE_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(permission_created=True)),
                {"CLOSURE_CREATES_PERMISSION", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(
                    non_claims=_selected_non_claims(relation_conformance_closure_created_successor=True)
                ),
                {"CLOSURE_CREATES_SUCCESSOR", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(
                    non_claims=_selected_non_claims(relation_conformance_closure_created_body=True)
                ),
                {"CLOSURE_CREATES_BODY", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
        ]
        for conformance, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(conformance), codes)

    def test_signal_presence_threshold_truth_action_consequence_collapse_blocks(self) -> None:
        cases = [
            (
                _selected_conformance(non_claims=_selected_non_claims(signal_created_by_default=True)),
                {"CLOSURE_CREATES_SIGNAL_BY_DEFAULT", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(presence_established=True)),
                {"CLOSURE_ESTABLISHES_PRESENCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(threshold_met=True)),
                {"CLOSURE_ESTABLISHES_THRESHOLD", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(truth_created=True)),
                {"CLOSURE_CREATES_TRUTH", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(action_authorized=True)),
                {"CLOSURE_AUTHORIZES_ACTION", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(consequence_created=True)),
                {"CLOSURE_CREATES_CONSEQUENCE", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
        ]
        for conformance, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(conformance), codes)

    def test_distributed_continuation_additional_carrier_and_operation_blocks(self) -> None:
        cases = [
            (
                _selected_conformance(non_claims=_selected_non_claims(distributed_standing_created=True)),
                {"CLOSURE_CREATES_DISTRIBUTED_STANDING", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(continuation_authorized=True)),
                {"CLOSURE_AUTHORIZES_CONTINUATION", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(
                    non_claims=_selected_non_claims(additional_carrier_experiment_authorized=True)
                ),
                {"CLOSURE_AUTHORIZES_ADDITIONAL_CARRIER_EXPERIMENT", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(distributed_operation_authorized=True)),
                {"CLOSURE_AUTHORIZES_DISTRIBUTED_OPERATION", "NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
        ]
        for conformance, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(conformance), codes)

    def test_expansion_successor_forcing_and_mutation_blocks(self) -> None:
        cases = [
            (
                _selected_conformance(non_claims=_selected_non_claims(closure_authorized_expansion=True)),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(
                    non_claims=_selected_non_claims(closure_forced_self_orientation_successor=True)
                ),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(
                    non_claims=_selected_non_claims(closure_forced_conformance_successor=True)
                ),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(mutation_performed=True)),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(replay_performed=True)),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
            (
                _selected_conformance(non_claims=_selected_non_claims(merge_performed=True)),
                {"NON_CLAIM_MISSING_OR_FLIPPED"},
            ),
        ]
        for conformance, codes in cases:
            with self.subTest(codes=codes):
                result = self._resolve(conformance)
                self._assert_blocked(result, codes)
                self.assertFalse(result["closure_statement"]["relation_conformance_closed"])

    def test_required_non_claim_missing_or_flipped_blocks_and_preserves_visible_non_claims(self) -> None:
        missing = _selected_conformance()
        missing["non_claims"].pop("authority_created")
        flipped = _selected_conformance(non_claims=_selected_non_claims(authority_created=True))

        missing_result = self._resolve(missing)
        flipped_result = self._resolve(flipped)

        self._assert_blocked(missing_result, {"NON_CLAIM_MISSING_OR_FLIPPED"})
        self._assert_blocked(
            flipped_result,
            {"CLOSURE_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"},
        )
        self.assertIn("non_claims_where_available", missing_result["closure_statement"])
        self.assertIn("non_claims_where_available", flipped_result["closure_statement"])

    def test_result_level_closure_non_claim_keys_are_all_false(self) -> None:
        result = self._resolve()
        non_claims = result["non_claims"]

        for key in _closure_non_claims():
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)


if __name__ == "__main__":
    unittest.main()
