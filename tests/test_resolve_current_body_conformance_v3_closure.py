"""Tests for bounded current-body conformance v3 closure.

This suite audits closure over one selected current-body conformance v3
BODY_CONFORMANT result only. Closure records meaning and non-meaning. It does
not perform conformance, create self-orientation, create currentness, create
distributed standing, authorize another carrier experiment, authorize
distributed operation, or force another successor.
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

import resolve_current_body_conformance_v3_closure as resolver


TOP_LEVEL_SECTIONS = {
    "current_body_conformance_v3_closure_metadata",
    "declared_closure_question",
    "selected_v3_conformance",
    "selected_v8_orientation",
    "selected_relation_band",
    "closure_basis",
    "closure_checks",
    "closure_statement",
    "closure_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "current_body_conformance_v3_closure_summary",
}

EXPECTED_CHECK_NAMES = {
    "selected_v3_conformance_result_exists",
    "selected_v3_conformance_result_parseable_mapping",
    "selected_v3_conformance_result_outcome_body_conformant",
    "selected_v8_id_path_outcome_preserved",
    "selected_relation_band_basis_preserved",
    "conformance_checks_passed",
    "failed_check_count_zero_where_exposed",
    "v3_conformance_statement_preserved",
    "v3_conformance_non_meaning_preserved",
    "current_governing_basis_remained_upstream",
    "downstream_surfaces_remained_downstream",
    "closed_multi_carrier_relation_band_remained_downstream",
    "relation_closure_meaning_preserved",
    "relation_closure_non_meaning_preserved",
    "carrier_b_receiving_evidence_only",
    "returned_evidence_preserved",
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
    "successor_not_forced",
    "closure_does_not_create_authority",
    "closure_does_not_create_permission",
    "closure_does_not_create_currentness",
    "closure_does_not_create_distributed_standing",
    "closure_does_not_authorize_continuation",
    "closure_does_not_authorize_expansion",
    "hidden_refusal_false",
    "hidden_divergence_false",
    "mutation_replay_merge_false",
    "required_non_claims_remain_false",
}

CLOSURE_NON_MEANING_KEYS = {
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
    "does_not_mean_follow_on_work_authorization",
    "does_not_mean_self_orientation_successor_forced",
    "does_not_mean_conformance_successor_forced",
}

OPEN_KEYS = {
    "current_body_conformance_v3_closure_implementation_refinement",
    "additional_physical_carrier_experiment_only_if_separately_declared_and_bounded",
    "distributed_standing",
    "persistence_registry_law",
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

FALSE_NON_CLAIMS = tuple(resolver.REQUIRED_NON_CLAIMS)

V3_ID = "current_body_conformance_pass_v3_test_body_conformant"
V8_ID = "current_self_orientation_v8_test_self_oriented"
V7_ID = "current_self_orientation_v7_test_self_oriented"
V2_ID = "current_body_conformance_pass_v2_test_body_conformant"
RELATION_ID = "multi_carrier_relation_test_recognized"
RELATION_CONFORMANCE_ID = "multi_carrier_relation_conformance_test_conformant"
RELATION_CLOSURE_ID = "multi_carrier_relation_conformance_closure_test_closed"


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
    claims = {key: False for key in resolver.REQUIRED_NON_CLAIMS}
    claims.update(updates)
    return claims


def _selected(result_id: str | None, outcome: str | None, path: str | None) -> dict[str, object]:
    return {
        "result_id": result_id,
        "path": path,
        "result_path": path,
        "outcome": outcome,
        "result_type": "synthetic_bounded_result",
        "result_version": "0.1.0",
        "resolver_module": "synthetic_bounded_resolver",
        "selected": bool(result_id),
        "downstream_only": True,
        "current_or_governing_basis": False,
    }


def valid_v3_conformance(**updates: object) -> dict[str, object]:
    non_claims = _non_claims()
    conformance_checks = [
        {
            "check_name": "v8_body_posture_coherent",
            "passed": True,
            "expected_posture": "v8 posture coheres as current body mirror",
            "actual_posture": True,
            "block_code": None,
        },
        {
            "check_name": "closed_relation_band_downstream",
            "passed": True,
            "expected_posture": "closed relation band remains downstream",
            "actual_posture": True,
            "block_code": None,
        },
        {
            "check_name": "non_claims_false",
            "passed": True,
            "expected_posture": "required non-claims remain false",
            "actual_posture": True,
            "block_code": None,
        },
    ]
    result: dict[str, object] = {
        "current_body_conformance_pass_v3_metadata": {
            "current_body_conformance_pass_v3_result_id": V3_ID,
            "current_body_conformance_pass_v3_result_type": "current_body_conformance_pass_v3_result",
            "current_body_conformance_pass_v3_result_version": "0.3.0",
            "generated_at": "2026-04-29T00:00:00Z",
            "resolver_module": "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v3",
            "successor_of_module": "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2",
        },
        "selected_conformance_inputs": {
            "selected_current_self_orientation_v8_result": _selected(
                V8_ID, "SELF_ORIENTED", "artifacts/test/v8.json"
            ),
            "selected_current_self_orientation_v7_result": _selected(
                V7_ID, "SELF_ORIENTED", "artifacts/test/v7.json"
            ),
            "selected_current_body_conformance_v2_result": _selected(
                V2_ID, "BODY_CONFORMANT", "artifacts/test/v2.json"
            ),
            "selected_multi_carrier_relation_result": _selected(
                RELATION_ID,
                "MULTI_CARRIER_RELATION_RECOGNIZED",
                "artifacts/test/relation.json",
            ),
            "selected_multi_carrier_relation_conformance_result": _selected(
                RELATION_CONFORMANCE_ID,
                "MULTI_CARRIER_RELATION_CONFORMANT",
                "artifacts/test/relation_conformance.json",
            ),
            "selected_multi_carrier_relation_conformance_closure_result": _selected(
                RELATION_CLOSURE_ID,
                "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
                "artifacts/test/relation_closure.json",
            ),
        },
        "v8_orientation_basis": {
            "selected_v8_id": V8_ID,
            "selected_v8_path": "artifacts/test/v8.json",
            "selected_v8_outcome": "SELF_ORIENTED",
            "selected_v7_id": V7_ID,
            "selected_current_body_conformance_v2_id": V2_ID,
            "selected_multi_carrier_relation_id": RELATION_ID,
            "selected_multi_carrier_relation_conformance_id": RELATION_CONFORMANCE_ID,
            "selected_multi_carrier_relation_conformance_closure_id": RELATION_CLOSURE_ID,
            "current_governing_basis_source": "inherited_from_v7_upstream_basis",
            "current_governing_basis_remains_upstream": True,
            "downstream_surfaces_remain_downstream": True,
            "v8_is_conformance_input_not_authority": True,
            "latest_file_currentness_used": False,
            "v8_self_orientation_basis": {
                "multi_carrier_relation_band_posture": "downstream_only",
                "closed_relation_band_determines_current_or_governing_basis": False,
            },
        },
        "recognized_integrated_body_posture": {
            "v8_posture_coherent_as_current_body_mirror": True,
            "current_governing_basis_remains_upstream": True,
            "carrier_receipt_admission_divergence_currentness_relation_conformance_closure_surfaces_remain_downstream": True,
            "closed_multi_carrier_relation_band_remains_closed_in_meaning_only": True,
            "relation_conformance_closure_meaning_preserved": True,
            "relation_conformance_closure_non_meaning_preserved": True,
            "carrier_b_remains_receiving_carrier_evidence_only": True,
            "returned_receipt_evidence_preserved": True,
            "visible_refusal_evidence_preserved": True,
            "visible_divergence_evidence_preserved": True,
            "currentness_participation_remained_participation": True,
            "returned_evidence_did_not_replace_source": True,
            "returned_evidence_did_not_create_currentness": True,
            "all_selected_non_claims_remain_false": True,
        },
        "conformance_checks": conformance_checks,
        "conformance_statement": {
            "v8_body_posture_conformant": True,
            "current_governing_basis_remains_upstream": True,
            "downstream_surfaces_remain_downstream": True,
            "closed_multi_carrier_relation_band_remains_downstream": True,
            "relation_conformance_closure_meaning_preserved": True,
            "relation_conformance_closure_non_meaning_preserved": True,
            "carrier_b_remained_receiving_carrier_evidence_only": True,
            "returned_receipt_evidence_preserved": True,
            "visible_refusal_evidence_preserved": True,
            "visible_divergence_evidence_preserved": True,
            "currentness_participation_remained_participation": True,
            "no_current_carrier_selected": True,
            "no_winning_carrier_selected": True,
            "no_losing_carrier_invalidated": True,
            "no_carrier_hierarchy_created": True,
            "no_authority_created": True,
            "no_permission_created": True,
            "no_currentness_created": True,
            "no_source_replaced": True,
            "no_distributed_standing_created": True,
            "no_presence_threshold_truth_action_consequence_created": True,
            "no_continuation_authorized": True,
            "no_additional_carrier_experiment_authorized": True,
            "no_distributed_operation_authorized": True,
            "no_successor_forced": True,
        },
        "conformance_non_meaning": {
            "authority": True,
            "permission": True,
            "currentness": True,
            "next_step_authorization": True,
            "continuation": True,
            "additional_carrier_experiment_authorization": True,
            "distributed_operation_authorization": True,
            "distributed_standing": True,
            "carrier_registry": True,
            "repository_synchronization": True,
            "full_body_transfer": True,
            "second_body": True,
            "presence": True,
            "threshold": True,
            "truth": True,
            "action": True,
            "consequence": True,
            "final_governance": True,
            "final_system_identity": True,
            "continuity_completion": True,
            "current_carrier_selected": True,
            "winning_carrier_selected": True,
            "losing_carrier_invalidated": True,
            "carrier_hierarchy": True,
            "relation_band_became_governing_basis": True,
            "self_orientation_successor_forced": True,
            "conformance_successor_forced": True,
        },
        "current_body_conformance_pass_v3_summary": {
            "outcome": "BODY_CONFORMANT",
            "selected_v3_conformance_id": V3_ID,
            "selected_v8_id": V8_ID,
            "selected_v8_path": "artifacts/test/v8.json",
            "selected_v8_outcome": "SELF_ORIENTED",
            "selected_v7_id": V7_ID,
            "selected_current_body_conformance_v2_id": V2_ID,
            "selected_multi_carrier_relation_id": RELATION_ID,
            "selected_multi_carrier_relation_conformance_id": RELATION_CONFORMANCE_ID,
            "selected_multi_carrier_relation_conformance_closure_id": RELATION_CLOSURE_ID,
            "passed_check_count": len(conformance_checks),
            "failed_check_count": 0,
            "v8_body_posture_conformant": True,
            "current_governing_basis_upstream": True,
            "downstream_surfaces_downstream": True,
            "closed_multi_carrier_relation_band_downstream": True,
            "relation_closure_meaning_preserved": True,
            "relation_closure_non_meaning_preserved": True,
            "carrier_b_receiving_evidence_only": True,
            "returned_evidence_preserved": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "currentness_participation_remained_participation": True,
            "no_current_winning_losing_carrier_collapse": True,
            "no_carrier_hierarchy": True,
            "no_authority_permission_currentness_source_replacement": True,
            "no_distributed_standing": True,
            "no_presence_threshold_truth_action_consequence": True,
            "no_continuation": True,
            "no_additional_carrier_experiment": True,
            "no_distributed_operation": True,
            "no_successor_forced": True,
            "key_non_claims": copy.deepcopy(non_claims),
        },
        "non_claims": copy.deepcopy(non_claims),
        "outcome": "BODY_CONFORMANT",
        "block": {"block_code": None, "block_reason": None, "code": None, "reason": None},
    }
    result.update(updates)
    return result


def resolve(conformance: object | None = None) -> dict:
    if conformance is None:
        return resolver.resolve_current_body_conformance_v3_closure()
    return resolver.resolve_current_body_conformance_v3_closure(
        selected_v3_conformance_result=conformance
    )


class CurrentBodyConformanceV3ClosureTests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result), result.keys())
        self.assertIn(
            result["outcome"],
            {
                "CURRENT_BODY_CONFORMANCE_V3_CLOSED",
                "CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED",
                "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED",
            },
        )

    def assert_false_non_claims(self, result: dict) -> None:
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
            self.assertIs(result["non_claims"][key], False, key)

    def assert_block(self, conformance: object, expected: str | set[str]) -> dict:
        result = resolve(conformance)
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED")
        code = result["block"]["block_code"]
        if isinstance(expected, set):
            self.assertIn(code, expected)
        else:
            self.assertEqual(code, expected)
        self.assert_false_non_claims(result)
        self.assertIn("non_claims_where_available", result["closure_statement"])
        return result

    def test_successful_mapping_closes_and_preserves_bounded_shape(self) -> None:
        conformance = valid_v3_conformance()
        result = resolve(conformance)
        self.assertIsInstance(result, dict)
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

        metadata = result["current_body_conformance_v3_closure_metadata"]
        for key in (
            "current_body_conformance_v3_closure_result_id",
            "current_body_conformance_v3_closure_result_type",
            "current_body_conformance_v3_closure_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertTrue(metadata.get(key), key)
        self.assertEqual(metadata["current_body_conformance_v3_closure_result_version"], "0.1.0")
        self.assertEqual(metadata["resolver_module"], "resolve_current_body_conformance_v3_closure")

        question = result["declared_closure_question"]
        self.assertIn("BODY_CONFORMANT", question["closure_question"])
        self.assertEqual(question["selected_v3_conformance_result_id"], V3_ID)
        self.assertEqual(question["selected_v3_conformance_outcome"], "BODY_CONFORMANT")
        self.assertEqual(question["selected_v8_id"], V8_ID)
        self.assertEqual(question["selected_multi_carrier_relation_id"], RELATION_ID)
        self.assertEqual(
            question["selected_multi_carrier_relation_conformance_id"],
            RELATION_CONFORMANCE_ID,
        )
        self.assertEqual(
            question["selected_multi_carrier_relation_conformance_closure_id"],
            RELATION_CLOSURE_ID,
        )
        self.assertTrue(question["closure_is_over_one_selected_body_conformant_v3_result"])
        self.assertFalse(question["closure_performs_conformance"])
        self.assertFalse(question["closure_authorizes_continuation"])
        self.assertFalse(question["closure_authorizes_additional_carrier_experiment"])
        self.assertFalse(question["closure_authorizes_distributed_operation"])
        self.assertFalse(question["closure_authorizes_follow_on_work"])

        selected_v3 = result["selected_v3_conformance"]
        self.assertEqual(selected_v3["selected_v3_conformance_result_id"], V3_ID)
        self.assertEqual(selected_v3["selected_v3_conformance_outcome"], "BODY_CONFORMANT")
        self.assertEqual(selected_v3["selected_v8_id"], V8_ID)
        self.assertFalse(selected_v3["closure_performed_conformance"])
        self.assertFalse(selected_v3["closure_created_self_orientation"])
        self.assertFalse(selected_v3["closure_widened_conformance_scope"])

        selected_v8 = result["selected_v8_orientation"]
        self.assertEqual(selected_v8["selected_v8_id"], V8_ID)
        self.assertEqual(selected_v8["selected_v8_outcome"], "SELF_ORIENTED")
        self.assertEqual(selected_v8["selected_v7_id"], V7_ID)
        self.assertTrue(selected_v8["selected_v8_preserved"])
        self.assertTrue(selected_v8["v8_is_conformance_input_not_authority"])
        self.assertFalse(selected_v8["latest_file_currentness_used"])

        relation_band = result["selected_relation_band"]
        self.assertEqual(relation_band["selected_multi_carrier_relation_id"], RELATION_ID)
        self.assertEqual(
            relation_band["selected_multi_carrier_relation_conformance_id"],
            RELATION_CONFORMANCE_ID,
        )
        self.assertEqual(
            relation_band["selected_multi_carrier_relation_conformance_closure_id"],
            RELATION_CLOSURE_ID,
        )
        self.assertTrue(relation_band["closed_multi_carrier_relation_band_remained_downstream"])
        self.assertTrue(relation_band["relation_closure_meaning_preserved"])
        self.assertTrue(relation_band["relation_closure_non_meaning_preserved"])
        self.assertTrue(relation_band["relation_band_is_downstream_only"])
        self.assertTrue(relation_band["selected_relation_band_preserved"])

        basis = result["closure_basis"]
        self.assertEqual(basis["selected_v3_conformance_result_id"], V3_ID)
        self.assertEqual(basis["selected_v8_id"], V8_ID)
        self.assertEqual(basis["selected_multi_carrier_relation_id"], RELATION_ID)
        self.assertEqual(basis["passed_conformance_check_count"], 3)
        self.assertEqual(basis["failed_conformance_check_count"], 0)
        self.assertTrue(basis["v3_conformance_statement_preserved"])
        self.assertTrue(basis["v3_conformance_non_meaning_preserved"])
        self.assertTrue(basis["current_governing_basis_remained_upstream"])
        self.assertTrue(basis["downstream_surfaces_remained_downstream"])
        self.assertTrue(basis["closed_multi_carrier_relation_band_remained_downstream"])
        self.assertTrue(basis["relation_closure_meaning_preserved"])
        self.assertTrue(basis["relation_closure_non_meaning_preserved"])
        self.assertTrue(basis["carrier_b_receiving_evidence_only"])
        self.assertTrue(basis["returned_evidence_preserved"])
        self.assertTrue(basis["visible_refusal_preserved"])
        self.assertTrue(basis["visible_divergence_preserved"])
        self.assertTrue(basis["currentness_participation_remained_participation"])
        self.assertFalse(basis["current_carrier_selected"])
        self.assertFalse(basis["winning_carrier_selected"])
        self.assertFalse(basis["losing_carrier_invalidated"])
        self.assertFalse(basis["additional_carrier_experiment_authorized"])
        self.assertFalse(basis["distributed_operation_authorized"])
        self.assertFalse(basis["successor_forced"])

        checks = result["closure_checks"]
        self.assertTrue(checks)
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({check["check_name"] for check in checks}))
        self.assertTrue(all(check["passed"] is True for check in checks))
        for check in checks:
            self.assertTrue(
                {"check_name", "passed", "expected_posture", "actual_posture", "block_code"}.issubset(check),
                check,
            )

        statement = result["closure_statement"]
        true_statement_keys = (
            "current_body_conformance_v3_closed",
            "selected_v3_conformance_preserved",
            "selected_v8_preserved",
            "selected_relation_band_preserved",
            "conformance_meaning_recorded",
            "conformance_non_meaning_recorded",
            "current_governing_basis_remained_upstream",
            "downstream_surfaces_remained_downstream",
            "closed_multi_carrier_relation_band_remained_downstream",
            "relation_closure_meaning_preserved",
            "relation_closure_non_meaning_preserved",
            "carrier_b_receiving_evidence_only",
            "returned_evidence_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "currentness_participation_remained_participation",
        )
        for key in true_statement_keys:
            self.assertTrue(statement[key], key)
        for key in (
            "current_carrier_selected",
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
            "successor_forced",
        ):
            self.assertFalse(statement[key], key)

        for key in CLOSURE_NON_MEANING_KEYS:
            self.assertTrue(result["closure_non_meaning"][key], key)
        for key in OPEN_KEYS:
            self.assertTrue(result["what_remains_open"][key], key)
        self.assert_false_non_claims(result)

    def test_summary_helper_preserves_closed_meaning_and_non_claims(self) -> None:
        result = resolve(valid_v3_conformance())
        summary = resolver.build_current_body_conformance_v3_closure_summary(result)
        self.assertEqual(summary["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["selected_v3_conformance_id"], V3_ID)
        self.assertEqual(summary["selected_v3_conformance_outcome"], "BODY_CONFORMANT")
        self.assertEqual(summary["selected_v8_id"], V8_ID)
        self.assertEqual(summary["selected_v8_outcome"], "SELF_ORIENTED")
        self.assertEqual(summary["selected_multi_carrier_relation_id"], RELATION_ID)
        self.assertEqual(
            summary["selected_multi_carrier_relation_conformance_id"],
            RELATION_CONFORMANCE_ID,
        )
        self.assertEqual(
            summary["selected_multi_carrier_relation_conformance_closure_id"],
            RELATION_CLOSURE_ID,
        )
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "current_body_conformance_v3_closed",
            "selected_v3_conformance_preserved",
            "selected_v8_preserved",
            "selected_relation_band_preserved",
            "conformance_meaning_recorded",
            "conformance_non_meaning_recorded",
            "current_governing_basis_upstream",
            "downstream_surfaces_downstream",
            "closed_multi_carrier_relation_band_downstream",
            "relation_closure_meaning_preserved",
            "relation_closure_non_meaning_preserved",
            "carrier_b_receiving_evidence_only",
            "returned_evidence_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "currentness_participation_remained_participation",
        ):
            self.assertTrue(summary[key], key)
        for key in (
            "current_carrier_selected",
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "distributed_standing_created",
            "source_currentness_authority_permission_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
            "successor_forced",
        ):
            self.assertFalse(summary[key], key)
        self.assertTrue(summary["key_non_claims"])
        for key, value in summary["key_non_claims"].items():
            self.assertIn(key, resolver.REQUIRED_NON_CLAIMS, key)
            self.assertIs(value, False, key)

    def test_real_artifact_discovery_path_when_live_v3_artifact_exists(self) -> None:
        if not self._has_live_body_conformant_v3_artifact():
            self.skipTest("No live BODY_CONFORMANT v3 artifact is present.")
        result = resolver.resolve_current_body_conformance_v3_closure()
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSED")
        self.assertIsNone(result["block"]["block_code"])
        self.assert_false_non_claims(result)
        self.assertFalse(result["non_claims"]["latest_file_currentness"])
        self.assertFalse(result["non_claims"]["distributed_standing_created"])
        self.assertFalse(result["non_claims"]["continuation_authorized"])
        self.assertFalse(result["non_claims"]["additional_carrier_experiment_authorized"])
        self.assertFalse(result["non_claims"]["distributed_operation_authorized"])

    def test_path_resolution_write_default_output_and_non_mutation(self) -> None:
        conformance = valid_v3_conformance()
        original = copy.deepcopy(conformance)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "selected_v3.json"
            _write_json(path, conformance)
            path_result = resolver.resolve_current_body_conformance_v3_closure_from_path(path)
            mapping_result = resolve(conformance)
            self.assert_top_level_shape(path_result)
            self.assertEqual(path_result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSED")
            self.assertEqual(set(path_result), set(mapping_result))
            self.assertTrue(
                str(path_result["selected_v3_conformance"]["selected_v3_conformance_result_path"]).endswith(
                    "selected_v3.json"
                )
            )

            explicit = Path(tmp) / "nested" / "closure.json"
            written = resolver.write_current_body_conformance_v3_closure_result(path_result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(_read_json(written)))

            with mock.patch.object(
                resolver,
                "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_ROOT",
                Path(tmp) / "default_root",
            ):
                first = resolver.write_current_body_conformance_v3_closure_result(path_result)
                second = resolver.write_current_body_conformance_v3_closure_result(path_result)
                self.assertNotEqual(first, second)
                self.assertTrue(str(first).startswith(str(Path(tmp) / "default_root")))
                self.assertTrue(first.name.endswith("__current_body_conformance_v3_closure_result.json"))
                self.assertIn("__current_body_conformance_v3_closure_result_001.json", second.name)

        self.assertEqual(conformance, original)
        repeated = resolve(conformance)
        self.assertEqual(repeated["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSED")
        self.assertEqual(conformance, original)

    def test_not_closed_readable_body_conformant_posture(self) -> None:
        conformance = valid_v3_conformance(closure_requested=False)
        result = resolve(conformance)
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_NOT_CLOSED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertTrue(result["closure_statement"]["current_body_conformance_v3_not_closed"])
        self.assertTrue(result["closure_statement"]["selected_body_conformant_basis_preserved"])
        self.assertTrue(result["closure_statement"]["non_collapse_posture_preserved"])
        self.assert_false_non_claims(result)

    def test_blocks_missing_malformed_and_path_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            empty_root = Path(tmp) / "empty"
            empty_root.mkdir()
            with mock.patch.object(resolver, "CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT", empty_root):
                result = resolver.resolve_current_body_conformance_v3_closure()
        self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED")
        self.assertEqual(result["block"]["block_code"], "SELECTED_V3_CONFORMANCE_MISSING")
        self.assert_false_non_claims(result)

        self.assert_block(["not", "a", "mapping"], "SELECTED_V3_CONFORMANCE_MALFORMED")

        with tempfile.TemporaryDirectory() as tmp:
            missing = Path(tmp) / "missing.json"
            result = resolver.resolve_current_body_conformance_v3_closure_from_path(missing)
            self.assertEqual(result["outcome"], "CURRENT_BODY_CONFORMANCE_V3_CLOSURE_BLOCKED")
            self.assertEqual(result["block"]["block_code"], "SELECTED_V3_CONFORMANCE_UNREADABLE")

            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            result = resolver.resolve_current_body_conformance_v3_closure_from_path(malformed)
            self.assertEqual(result["block"]["block_code"], "SELECTED_V3_CONFORMANCE_MALFORMED")

            array_path = Path(tmp) / "array.json"
            _write_json(array_path, [])
            result = resolver.resolve_current_body_conformance_v3_closure_from_path(array_path)
            self.assertEqual(result["block"]["block_code"], "SELECTED_V3_CONFORMANCE_MALFORMED")

    def test_blocks_non_body_conformant_missing_basis_and_failed_checks(self) -> None:
        conformance = valid_v3_conformance(outcome="BLOCKED")
        self.assert_block(conformance, "SELECTED_V3_CONFORMANCE_NOT_BODY_CONFORMANT")

        conformance = valid_v3_conformance()
        conformance["selected_conformance_inputs"]["selected_current_self_orientation_v8_result"] = {}
        conformance["v8_orientation_basis"]["selected_v8_id"] = None
        conformance["v8_orientation_basis"]["selected_v8_outcome"] = None
        conformance["current_body_conformance_pass_v3_summary"]["selected_v8_id"] = None
        conformance["current_body_conformance_pass_v3_summary"]["selected_v8_outcome"] = None
        self.assert_block(conformance, "SELECTED_V8_BASIS_MISSING")

        conformance = valid_v3_conformance()
        for key in (
            "selected_multi_carrier_relation_id",
            "selected_multi_carrier_relation_conformance_id",
            "selected_multi_carrier_relation_conformance_closure_id",
        ):
            conformance["v8_orientation_basis"][key] = None
            conformance["current_body_conformance_pass_v3_summary"][key] = None
        conformance["selected_conformance_inputs"]["selected_multi_carrier_relation_result"] = {}
        conformance["selected_conformance_inputs"]["selected_multi_carrier_relation_conformance_result"] = {}
        conformance["selected_conformance_inputs"]["selected_multi_carrier_relation_conformance_closure_result"] = {}
        self.assert_block(conformance, "SELECTED_RELATION_BAND_BASIS_MISSING")

        conformance = valid_v3_conformance()
        conformance["conformance_checks"][0]["passed"] = False
        conformance["conformance_checks"][0]["block_code"] = "SYNTHETIC_FAILED_CHECK"
        self.assert_block(conformance, "CONFORMANCE_CHECKS_FAILED_OR_HIDDEN")

    def test_blocks_hidden_refusal_divergence_currentness_and_carrier_collapse(self) -> None:
        cases = (
            ({"refusal_hidden": True}, "CLOSURE_HIDES_REFUSAL"),
            ({"divergence_hidden": True}, "CLOSURE_HIDES_DIVERGENCE"),
            ({"mismatch_hidden": True}, "CLOSURE_HIDES_DIVERGENCE"),
            ({"latest_file_currentness": True}, "CLOSURE_CURRENTNESS_SHORTCUT"),
            ({"recency_fraud": True}, "CLOSURE_CURRENTNESS_SHORTCUT"),
            ({"currentness_created": True}, "CLOSURE_CREATES_CURRENTNESS"),
            ({"current_carrier_selected": True}, "CLOSURE_SELECTS_CURRENT_CARRIER"),
            ({"winning_carrier_selected": True}, "CLOSURE_SELECTS_WINNING_CARRIER"),
            ({"losing_carrier_invalidated": True}, "CLOSURE_INVALIDATES_LOSING_CARRIER"),
            ({"carrier_hierarchy_created": True}, "CLOSURE_CREATES_CARRIER_HIERARCHY"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                conformance = valid_v3_conformance(non_claims=_non_claims(**claims))
                result = self.assert_block(conformance, code)
                available = result["closure_statement"]["non_claims_where_available"]
                for key, value in claims.items():
                    self.assertIs(available[key], value, key)

    def test_blocks_source_authority_permission_body_and_signal_family_collapse(self) -> None:
        cases = (
            ({"source_replaced": True}, "CLOSURE_REPLACES_SOURCE"),
            ({"authority_created": True}, "CLOSURE_CREATES_AUTHORITY"),
            ({"permission_created": True}, "CLOSURE_CREATES_PERMISSION"),
            ({"current_body_conformance_v3_closure_created_successor": True}, "CLOSURE_CREATES_SUCCESSOR"),
            ({"current_body_conformance_v3_closure_created_body": True}, "CLOSURE_CREATES_BODY"),
            ({"signal_created_by_default": True}, "CLOSURE_CREATES_SIGNAL_BY_DEFAULT"),
            ({"presence_established": True}, "CLOSURE_ESTABLISHES_PRESENCE"),
            ({"threshold_met": True}, "CLOSURE_ESTABLISHES_THRESHOLD"),
            ({"truth_created": True}, "CLOSURE_CREATES_TRUTH"),
            ({"action_authorized": True}, "CLOSURE_AUTHORIZES_ACTION"),
            ({"consequence_created": True}, "CLOSURE_CREATES_CONSEQUENCE"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                conformance = valid_v3_conformance(non_claims=_non_claims(**claims))
                self.assert_block(conformance, code)

    def test_blocks_distributed_continuation_operation_successor_and_non_claim_failures(self) -> None:
        cases = (
            ({"distributed_standing_created": True}, "CLOSURE_CREATES_DISTRIBUTED_STANDING"),
            ({"continuation_authorized": True}, "CLOSURE_AUTHORIZES_CONTINUATION"),
            (
                {"additional_carrier_experiment_authorized": True},
                "CLOSURE_AUTHORIZES_ADDITIONAL_CARRIER_EXPERIMENT",
            ),
            ({"distributed_operation_authorized": True}, "CLOSURE_AUTHORIZES_DISTRIBUTED_OPERATION"),
            (
                {"closure_forced_self_orientation_successor": True},
                "CLOSURE_FORCES_SELF_ORIENTATION_SUCCESSOR",
            ),
            (
                {"closure_forced_conformance_successor": True},
                "CLOSURE_FORCES_CONFORMANCE_SUCCESSOR",
            ),
            ({"closure_authorized_expansion": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"mutation_performed": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"replay_performed": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"merge_performed": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                conformance = valid_v3_conformance(non_claims=_non_claims(**claims))
                self.assert_block(conformance, code)

        conformance = valid_v3_conformance()
        del conformance["non_claims"]["authority_created"]
        self.assert_block(conformance, "NON_CLAIM_MISSING_OR_FLIPPED")

        conformance = valid_v3_conformance()
        conformance["non_claims"]["authority_created"] = True
        self.assert_block(conformance, "CLOSURE_CREATES_AUTHORITY")

    def _has_live_body_conformant_v3_artifact(self) -> bool:
        root = resolver.CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT
        if not root.exists():
            return False
        for path in root.rglob("*.json"):
            try:
                loaded = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if isinstance(loaded, dict) and loaded.get("outcome") == "BODY_CONFORMANT":
                return True
        return False


if __name__ == "__main__":
    unittest.main()
