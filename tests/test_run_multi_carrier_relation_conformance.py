"""Tests for bounded multi-carrier relation conformance.

This suite audits one conformance runner. It verifies that one selected
recognized multi-carrier relation may be tested for bounded coherence without
becoming relation creation, currentness, carrier hierarchy, distributed
standing, divergence resolution, continuation, another carrier experiment, or
distributed operation.
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

import run_multi_carrier_relation_conformance as runner


TOP_LEVEL_SECTIONS = {
    "multi_carrier_relation_conformance_metadata",
    "declared_conformance_question",
    "selected_relation",
    "selected_relation_basis",
    "selected_carriers",
    "selected_carrier_evidence",
    "relation_conformance_checks",
    "relation_conformance_statement",
    "relation_conformance_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "multi_carrier_relation_conformance_summary",
}

EXPECTED_CHECK_NAMES = {
    "selected_relation_result_exists",
    "selected_relation_result_parseable_mapping",
    "selected_relation_result_outcome_recognized",
    "selected_relation_type_supported",
    "selected_relation_question_declared",
    "selected_carriers_preserved",
    "selected_carrier_evidence_preserved",
    "selected_evidence_identities_preserved",
    "selected_evidence_outcomes_preserved",
    "carrier_roles_preserved",
    "local_outcomes_preserved",
    "relation_basis_preserved",
    "relation_checks_passed_or_preserved",
    "downstream_evidence_posture_preserved",
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
    "divergence_not_resolved_by_majority_latest_success_count",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "mutation_replay_merge_false",
    "additional_carrier_experiment_not_authorized",
    "distributed_operation_not_authorized",
    "required_non_claims_remain_false",
}

NON_MEANING_TRUE_KEYS = {
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
}

OPEN_SURFACES = {
    "multi-carrier relation conformance implementation refinement",
    "multi-carrier relation closure",
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
}

OUTCOME_FAMILY = {
    "MULTI_CARRIER_RELATION_CONFORMANT",
    "MULTI_CARRIER_RELATION_NONCONFORMANT",
    "MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED",
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


def _relation_non_claims(**updates: bool) -> dict[str, bool]:
    claims = {key: False for key in runner.RELATION_BOUNDARY_NON_CLAIM_KEYS}
    claims.update(updates)
    return claims


def _conformance_non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(runner.REQUIRED_NON_CLAIMS)
    claims.update(updates)
    return claims


def _carrier(carrier_id: str, role: str) -> dict[str, object]:
    return {
        "carrier_id": carrier_id,
        "carrier_role": role,
        "role_bounded": True,
        "role_declared": True,
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
        "block_code": "CARRIED_SURFACE_MALFORMED" if outcome == "BLOCKED" else None,
        "non_claims": copy.deepcopy(non_claims or _relation_non_claims()),
    }


def _relation_check(name: str) -> dict[str, object]:
    return {
        "check_name": name,
        "passed": True,
        "expected_posture": f"{name} passes",
        "actual_posture": True,
        "block_code": None,
    }


def _selected_relation(**overrides: object) -> dict[str, object]:
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
    selected_evidence_ids = [item["evidence_id"] for item in evidence]
    selected_evidence_outcomes = [item["evidence_outcome"] for item in evidence]
    question = (
        "May Carrier B returned blocked receipt evidence and returned successful "
        "receipt evidence stand in bounded multi-carrier relation without creating "
        "currentness, hierarchy, distributed standing, truth, action, or continuation?"
    )
    relation_type = "REFUSAL_SUCCESS_RELATION"
    non_claims = _relation_non_claims()
    relation_checks = [
        _relation_check("relation_question_declared"),
        _relation_check("relation_type_supported"),
        _relation_check("sufficient_selected_carriers_or_evidence"),
        _relation_check("evidence_identity_present"),
        _relation_check("evidence_outcome_present"),
        _relation_check("non_claims_remain_false"),
    ]
    relation_result = {
        "multi_carrier_relation_recognized": True,
        "no_multi_carrier_relation": False,
        "relation_type": relation_type,
        "relation_claim": "selected carrier evidence stands in bounded refusal-success relation",
        "selected_carrier_count": 2,
        "selected_evidence_count": 2,
        "selected_carrier_ids": selected_carrier_ids,
        "selected_evidence_ids": selected_evidence_ids,
        "selected_evidence_outcomes": selected_evidence_outcomes,
        "relation_evidence": {
            "has_refusal_evidence": True,
            "has_success_evidence": True,
            "has_divergence_evidence": True,
            "has_currentness_participation_evidence": True,
            "shared_basis_present": True,
        },
        "carrier_roles_preserved": True,
        "evidence_identities_preserved": True,
        "local_outcomes_preserved": True,
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "downstream_evidence_posture_preserved": True,
        "current_carrier_not_selected": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_not_replaced": True,
        "currentness_not_created": True,
        "authority_not_created": True,
        "permission_not_created": True,
        "carrier_hierarchy_not_created": True,
        "distributed_standing_not_created": True,
        "truth_not_created": True,
        "action_not_authorized": True,
        "continuation_not_authorized": True,
    }
    relation = {
        "multi_carrier_relation_metadata": {
            "multi_carrier_relation_result_id": (
                "carrier_b_refusal_success_multi_carrier_relation_001__"
                "multi_carrier_relation_recognized__multi_carrier_relation_result"
            ),
            "multi_carrier_relation_result_type": "multi_carrier_relation_boundary_result",
            "multi_carrier_relation_result_version": "0.1.0",
            "generated_at": "2026-04-28T00:00:00+00:00",
            "resolver_module": "resolve_multi_carrier_relation_boundary",
        },
        "declared_relation_question": {
            "relation_request_id": "carrier_b_refusal_success_multi_carrier_relation_001",
            "relation_question": question,
            "relation_type": relation_type,
            "selected_carrier_count": 2,
            "selected_evidence_count": 2,
            "declared_non_claims": copy.deepcopy(non_claims),
        },
        "selected_carriers": carriers,
        "selected_carrier_evidence": evidence,
        "relation_basis": {
            "relation_question": question,
            "relation_type": relation_type,
            "supported_relation_types": sorted(runner.SUPPORTED_RELATION_TYPES),
            "selected_carrier_ids": selected_carrier_ids,
            "selected_evidence_ids": selected_evidence_ids,
            "selected_evidence_outcomes": selected_evidence_outcomes,
            "selected_currentness_participation_statuses": [
                "CURRENTNESS_PARTICIPATION_EXCLUDED",
                "CURRENTNESS_PARTICIPATION_ELIGIBLE",
            ],
            "relation_detection": {
                "relation_supported": True,
                "visible_refusal_preserved": True,
                "visible_divergence_preserved": True,
                "relation_evidence": copy.deepcopy(relation_result["relation_evidence"]),
            },
            "visible_divergence_remains_visible": True,
            "hidden_divergence": False,
            "refusal_hidden": False,
            "required_non_claims": copy.deepcopy(non_claims),
        },
        "relation_checks": relation_checks,
        "relation_result": relation_result,
        "non_claims": non_claims,
        "outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
        "block": {
            "code": None,
            "reason": None,
            "block_code": None,
            "block_reason": None,
        },
        "multi_carrier_relation_summary": {
            "outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "block_code": None,
            "block_reason": None,
            "relation_request_id": "carrier_b_refusal_success_multi_carrier_relation_001",
            "relation_question": question,
            "relation_type": relation_type,
            "relation_recognized": True,
            "no_relation": False,
            "selected_carrier_count": 2,
            "selected_evidence_count": 2,
            "selected_carrier_ids": selected_carrier_ids,
            "selected_evidence_ids": selected_evidence_ids,
            "selected_evidence_outcomes": selected_evidence_outcomes,
            "passed_check_count": len(relation_checks),
            "failed_check_count": 0,
            "carrier_roles_preserved": True,
            "evidence_identities_preserved": True,
            "local_outcomes_preserved": True,
            "visible_refusal_preserved": True,
            "visible_divergence_preserved": True,
            "downstream_evidence_posture_preserved": True,
            "current_carrier_not_selected": True,
            "winning_carrier_selected": False,
            "losing_carrier_invalidated": False,
            "source_created": False,
            "currentness_created": False,
            "authority_created": False,
            "permission_created": False,
            "carrier_hierarchy_created": False,
            "distributed_standing_created": False,
            "presence_threshold_truth_action_consequence_created": False,
            "continuation_authorized": False,
            "key_non_claims": copy.deepcopy(non_claims),
        },
    }
    _deep_update(relation, overrides)
    return relation


def _deep_update(target: dict, updates: dict) -> None:
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _deep_update(target[key], value)
        else:
            target[key] = value


class MultiCarrierRelationConformanceTests(unittest.TestCase):
    def _resolve(self, relation: dict | None = None) -> dict:
        return runner.run_multi_carrier_relation_conformance(
            selected_relation_result=_selected_relation() if relation is None else relation
        )

    def _assert_top_level_shape(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertEqual(TOP_LEVEL_SECTIONS, set(result))
        self.assertIn(result["outcome"], OUTCOME_FAMILY)

    def _assert_conformant(self, result: dict) -> None:
        self._assert_top_level_shape(result)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertTrue(result["relation_conformance_statement"]["relation_conformant"])
        self.assertEqual(0, result["multi_carrier_relation_conformance_summary"]["failed_check_count"])

    def _assert_blocked(self, result: dict, expected_codes: set[str]) -> None:
        self._assert_top_level_shape(result)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANCE_BLOCKED", result["outcome"])
        self.assertIn(result["block"]["block_code"], expected_codes)
        self.assertFalse(result["relation_conformance_statement"]["relation_conformant"])

    def _assert_false_non_claims(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in runner.REQUIRED_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_successful_conformant_mapping_path(self) -> None:
        result = self._resolve()

        self._assert_conformant(result)
        metadata = result["multi_carrier_relation_conformance_metadata"]
        self.assertTrue(metadata["multi_carrier_relation_conformance_result_id"])
        self.assertTrue(metadata["multi_carrier_relation_conformance_result_type"])
        self.assertEqual("0.1.0", metadata["multi_carrier_relation_conformance_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual("run_multi_carrier_relation_conformance", metadata["resolver_module"])

    def test_declared_question_and_selected_relation_are_preserved(self) -> None:
        result = self._resolve()
        question = result["declared_conformance_question"]
        selected = result["selected_relation"]
        basis = result["selected_relation_basis"]

        self.assertIn("Does this selected recognized multi-carrier relation cohere", question["conformance_question"])
        self.assertEqual(selected["selected_relation_result_id"], question["selected_relation_result_id"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", question["selected_relation_type"])
        self.assertEqual(selected["selected_relation_question"], question["selected_relation_question"])
        self.assertFalse(question["conformance_creates_relation"])
        self.assertFalse(question["conformance_creates_currentness"])
        self.assertFalse(question["conformance_creates_distributed_standing"])
        self.assertFalse(question["conformance_authorizes_continuation"])
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", selected["selected_relation_outcome"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", selected["selected_relation_type"])
        self.assertEqual(2, basis["selected_carrier_count"])
        self.assertEqual(2, basis["selected_evidence_count"])
        self.assertEqual(0, basis["failed_relation_check_count"])
        self.assertGreater(basis["passed_relation_check_count"], 0)

    def test_selected_relation_basis_carriers_and_evidence_are_preserved(self) -> None:
        result = self._resolve()
        basis = result["selected_relation_basis"]
        carriers = result["selected_carriers"]
        evidence = result["selected_carrier_evidence"]

        self.assertEqual(["carrier_A_current_macbook", "carrier_B_physical_macbook"], basis["selected_carrier_ids"])
        self.assertEqual(
            [
                "carrier_B_returned_blocked__current_body_standing_closure_post_conformance__receipt",
                "carrier_B_returned_received__current_body_standing_closure_post_conformance__receipt",
            ],
            basis["selected_evidence_ids"],
        )
        self.assertEqual(["BLOCKED", "CARRIED_SURFACE_RECEIVED"], basis["selected_evidence_outcomes"])
        self.assertTrue(basis["visible_refusal_preserved"])
        self.assertTrue(basis["visible_divergence_preserved"])
        self.assertTrue(basis["downstream_evidence_posture_preserved"])
        self.assertTrue(basis["current_carrier_not_selected"])
        self.assertFalse(basis["winning_carrier_selected"])
        self.assertFalse(basis["losing_carrier_invalidated"])
        self.assertEqual(2, len(carriers))
        self.assertEqual(2, len(evidence))
        self.assertTrue(all(item["carrier_role"] for item in carriers))
        self.assertTrue(all(item["evidence_id"] for item in evidence))
        self.assertTrue(all(item["evidence_outcome"] for item in evidence))

    def test_conformance_checks_are_complete_and_pass_for_conformant_case(self) -> None:
        result = self._resolve()
        checks = result["relation_conformance_checks"]
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

    def test_conformance_statement_preserves_non_collapse_posture(self) -> None:
        statement = self._resolve()["relation_conformance_statement"]

        for key in (
            "relation_conformant",
            "selected_relation_preserved",
            "selected_carriers_preserved",
            "selected_evidence_preserved",
            "carrier_roles_preserved",
            "local_outcomes_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "downstream_evidence_posture_preserved",
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
            "presence_threshold_truth_action_consequence_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
        ):
            self.assertIs(statement[key], False, key)

    def test_conformance_non_meaning_and_open_surfaces_are_preserved(self) -> None:
        result = self._resolve()
        non_meaning = result["relation_conformance_non_meaning"]
        open_section = result["what_remains_open"]

        for key in NON_MEANING_TRUE_KEYS:
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
        summary = runner.build_multi_carrier_relation_conformance_summary(result)

        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertTrue(summary["selected_relation_id"])
        self.assertEqual("MULTI_CARRIER_RELATION_RECOGNIZED", summary["selected_relation_outcome"])
        self.assertEqual("REFUSAL_SUCCESS_RELATION", summary["selected_relation_type"])
        self.assertEqual(2, summary["selected_carrier_count"])
        self.assertEqual(2, summary["selected_evidence_count"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        for key in (
            "relation_conformant",
            "selected_relation_preserved",
            "selected_carriers_preserved",
            "selected_evidence_preserved",
            "carrier_roles_preserved",
            "local_outcomes_preserved",
            "visible_refusal_preserved",
            "visible_divergence_preserved",
            "downstream_evidence_posture_preserved",
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
            "presence_threshold_truth_action_consequence_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
        ):
            self.assertIs(summary[key], False, key)
        self.assertIsInstance(summary["key_non_claims"], dict)

    def test_result_level_non_claims_are_false_for_all_outcome_families(self) -> None:
        conformant = self._resolve()
        nonconformant_relation = _selected_relation(
            relation_result={"local_outcomes_preserved": False},
            multi_carrier_relation_summary={"local_outcomes_preserved": False},
        )
        nonconformant = self._resolve(nonconformant_relation)
        blocked = runner.run_multi_carrier_relation_conformance(selected_relation_result={})

        self.assertEqual("MULTI_CARRIER_RELATION_NONCONFORMANT", nonconformant["outcome"])
        self._assert_false_non_claims(conformant)
        self._assert_false_non_claims(nonconformant)
        self._assert_false_non_claims(blocked)

    def test_real_artifact_discovery_path_when_available(self) -> None:
        root = REPO_ROOT / "artifacts" / "integrity_host_v0_min_coexistence_multi_carrier_relation_boundary"
        recognized = []
        for path in root.glob("*.json"):
            try:
                loaded = _read_json(path)
            except (OSError, json.JSONDecodeError, AssertionError):
                continue
            if loaded.get("outcome") == "MULTI_CARRIER_RELATION_RECOGNIZED":
                recognized.append(path)
        if not recognized:
            self.skipTest("No standing MULTI_CARRIER_RELATION_RECOGNIZED artifact is present.")

        result = runner.run_multi_carrier_relation_conformance()

        self._assert_conformant(result)
        statement = result["relation_conformance_statement"]
        self.assertFalse(result["non_claims"]["latest_file_currentness"])
        self.assertFalse(statement["distributed_standing_created"])
        self.assertFalse(statement["continuation_authorized"])
        self.assertFalse(statement["additional_carrier_experiment_authorized"])

    def test_path_based_resolution_preserves_path_and_shape(self) -> None:
        relation = _selected_relation()
        mapping_result = self._resolve(relation)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "relation.json"
            _write_json(path, relation)

            path_result = runner.run_multi_carrier_relation_conformance_from_path(path)

        self._assert_conformant(path_result)
        self.assertEqual(set(mapping_result), set(path_result))
        self.assertEqual(str(path), path_result["selected_relation"]["selected_relation_result_path"])

    def test_write_behavior_and_default_output_path_are_additive(self) -> None:
        result = self._resolve()
        with tempfile.TemporaryDirectory() as tmp:
            explicit_path = Path(tmp) / "nested" / "result.json"
            written = runner.write_multi_carrier_relation_conformance_result(result, explicit_path)
            self.assertEqual(explicit_path, written)
            loaded = _read_json(written)
            self.assertEqual(TOP_LEVEL_SECTIONS, set(loaded))

            with mock.patch.object(runner, "MULTI_CARRIER_RELATION_CONFORMANCE_ROOT", Path(tmp) / "default"):
                first = runner.write_multi_carrier_relation_conformance_result(result)
                second = runner.write_multi_carrier_relation_conformance_result(result)

        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__multi_carrier_relation_conformance_result.json"))
        self.assertIn("_001", second.stem)

    def test_non_mutation_posture(self) -> None:
        relation = _selected_relation()
        before = copy.deepcopy(relation)

        first = self._resolve(relation)
        second = self._resolve(relation)

        self.assertEqual(before, relation)
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", first["outcome"])
        self.assertEqual("MULTI_CARRIER_RELATION_CONFORMANT", second["outcome"])

    def test_missing_and_malformed_relation_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(runner, "MULTI_CARRIER_RELATION_BOUNDARY_ROOT", Path(tmp)):
                missing = runner.run_multi_carrier_relation_conformance()
        malformed = runner.run_multi_carrier_relation_conformance(selected_relation_result=["not", "mapping"])  # type: ignore[arg-type]

        self._assert_blocked(missing, {"SELECTED_RELATION_MISSING"})
        self._assert_blocked(malformed, {"SELECTED_RELATION_MALFORMED"})

    def test_path_unreadable_and_malformed_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            tmp_path = Path(tmp)
            missing = runner.run_multi_carrier_relation_conformance_from_path(tmp_path / "missing.json")
            malformed_path = tmp_path / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            malformed = runner.run_multi_carrier_relation_conformance_from_path(malformed_path)
            array_path = tmp_path / "array.json"
            _write_json(array_path, [])
            array_result = runner.run_multi_carrier_relation_conformance_from_path(array_path)

        self._assert_blocked(missing, {"SELECTED_RELATION_UNREADABLE", "SELECTED_RELATION_MISSING"})
        self._assert_blocked(malformed, {"SELECTED_RELATION_MALFORMED"})
        self._assert_blocked(array_result, {"SELECTED_RELATION_MALFORMED"})

    def test_relation_not_recognized_blocks(self) -> None:
        for outcome in ("NO_MULTI_CARRIER_RELATION", "MULTI_CARRIER_RELATION_BLOCKED"):
            relation = _selected_relation(outcome=outcome)
            result = self._resolve(relation)
            self._assert_blocked(result, {"SELECTED_RELATION_NOT_RECOGNIZED"})

    def test_unsupported_relation_type_blocks(self) -> None:
        relation = _selected_relation(
            declared_relation_question={"relation_type": "UNSUPPORTED_RELATION"},
            relation_result={"relation_type": "UNSUPPORTED_RELATION"},
            relation_basis={"relation_type": "UNSUPPORTED_RELATION"},
            multi_carrier_relation_summary={"relation_type": "UNSUPPORTED_RELATION"},
        )

        result = self._resolve(relation)

        self._assert_blocked(result, {"RELATION_TYPE_UNSUPPORTED"})

    def test_selected_carriers_and_evidence_missing_block(self) -> None:
        no_carriers = self._resolve(_selected_relation(selected_carriers=[]))
        no_evidence = self._resolve(_selected_relation(selected_carrier_evidence=[]))

        self._assert_blocked(no_carriers, {"SELECTED_CARRIERS_MISSING"})
        self._assert_blocked(no_evidence, {"SELECTED_EVIDENCE_MISSING"})

    def test_evidence_identity_and_outcome_missing_block(self) -> None:
        missing_id = _selected_relation()
        missing_id["selected_carrier_evidence"][0]["evidence_id"] = None
        missing_outcome = _selected_relation()
        missing_outcome["selected_carrier_evidence"][0]["evidence_outcome"] = None

        self._assert_blocked(self._resolve(missing_id), {"EVIDENCE_IDENTITY_MISSING"})
        self._assert_blocked(self._resolve(missing_outcome), {"EVIDENCE_OUTCOME_MISSING"})

    def test_failed_or_hidden_relation_checks_block(self) -> None:
        failed = _selected_relation()
        failed["relation_checks"][0]["passed"] = False
        failed["relation_checks"][0]["block_code"] = "RELATION_TYPE_UNSUPPORTED"
        hidden = _selected_relation(relation_checks=[])

        self._assert_blocked(self._resolve(failed), {"RELATION_CHECKS_FAILED_OR_HIDDEN"})
        self._assert_blocked(self._resolve(hidden), {"RELATION_CHECKS_FAILED_OR_HIDDEN"})

    def test_hidden_refusal_and_divergence_block(self) -> None:
        refusal_hidden = _selected_relation(
            relation_result={"visible_refusal_preserved": False},
            multi_carrier_relation_summary={"visible_refusal_preserved": False},
        )
        divergence_hidden = _selected_relation(
            relation_result={"visible_divergence_preserved": False},
            multi_carrier_relation_summary={"visible_divergence_preserved": False},
        )
        mismatch_hidden = _selected_relation(non_claims=_relation_non_claims(mismatch_hidden=True))

        self._assert_blocked(self._resolve(refusal_hidden), {"CONFORMANCE_HIDES_REFUSAL"})
        self._assert_blocked(self._resolve(divergence_hidden), {"CONFORMANCE_HIDES_DIVERGENCE"})
        self._assert_blocked(self._resolve(mismatch_hidden), {"NON_CLAIM_MISSING_OR_FLIPPED"})

    def test_currentness_shortcuts_block(self) -> None:
        latest = _selected_relation(non_claims=_relation_non_claims(latest_file_currentness=True))
        currentness = _selected_relation(non_claims=_relation_non_claims(currentness_created=True))
        current_carrier = _selected_relation()
        current_carrier["relation_result"]["current_carrier_selected"] = True

        self._assert_blocked(self._resolve(latest), {"CONFORMANCE_CURRENTNESS_SHORTCUT", "NON_CLAIM_MISSING_OR_FLIPPED"})
        self._assert_blocked(self._resolve(currentness), {"CONFORMANCE_CREATES_CURRENTNESS", "NON_CLAIM_MISSING_OR_FLIPPED"})
        self._assert_blocked(self._resolve(current_carrier), {"CONFORMANCE_CURRENTNESS_SHORTCUT"})

    def test_carrier_hierarchy_winning_and_losing_collapse_block(self) -> None:
        cases = [
            (_selected_relation(non_claims=_relation_non_claims(carrier_relation_created_hierarchy=True)), {"CONFORMANCE_CREATES_CARRIER_HIERARCHY", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(winning_carrier_selected=True)), {"CONFORMANCE_SELECTS_WINNING_CARRIER", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(losing_carrier_invalidated=True)), {"CONFORMANCE_INVALIDATES_LOSING_CARRIER", "NON_CLAIM_MISSING_OR_FLIPPED"}),
        ]
        for relation, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(relation), codes)

    def test_source_authority_permission_successor_body_collapse_blocks(self) -> None:
        cases = [
            (_selected_relation(non_claims=_relation_non_claims(source_replaced=True)), {"CONFORMANCE_REPLACES_SOURCE", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(currentness_created=True)), {"CONFORMANCE_CREATES_CURRENTNESS", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(authority_created=True)), {"CONFORMANCE_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(permission_created=True)), {"CONFORMANCE_CREATES_PERMISSION", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(carrier_relation_created_successor=True)), {"CONFORMANCE_CREATES_SUCCESSOR", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(carrier_relation_created_body=True)), {"CONFORMANCE_CREATES_BODY", "NON_CLAIM_MISSING_OR_FLIPPED"}),
        ]
        for relation, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(relation), codes)

    def test_signal_presence_threshold_truth_action_consequence_collapse_blocks(self) -> None:
        cases = [
            (_selected_relation(non_claims=_relation_non_claims(signal_created_by_default=True)), {"CONFORMANCE_CREATES_SIGNAL_BY_DEFAULT", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(presence_established=True)), {"CONFORMANCE_ESTABLISHES_PRESENCE", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(threshold_met=True)), {"CONFORMANCE_ESTABLISHES_THRESHOLD", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(truth_created=True)), {"CONFORMANCE_CREATES_TRUTH", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(action_authorized=True)), {"CONFORMANCE_AUTHORIZES_ACTION", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(consequence_created=True)), {"CONFORMANCE_CREATES_CONSEQUENCE", "NON_CLAIM_MISSING_OR_FLIPPED"}),
        ]
        for relation, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(relation), codes)

    def test_distributed_standing_and_continuation_block(self) -> None:
        distributed = _selected_relation(non_claims=_relation_non_claims(distributed_standing_created=True))
        continuation = _selected_relation(non_claims=_relation_non_claims(continuation_authorized=True))

        self._assert_blocked(self._resolve(distributed), {"CONFORMANCE_CREATES_DISTRIBUTED_STANDING", "NON_CLAIM_MISSING_OR_FLIPPED"})
        self._assert_blocked(self._resolve(continuation), {"CONFORMANCE_AUTHORIZES_CONTINUATION", "NON_CLAIM_MISSING_OR_FLIPPED"})

    def test_divergence_resolution_blocks(self) -> None:
        cases = [
            (_selected_relation(non_claims=_relation_non_claims(divergence_resolved_by_majority=True)), {"CONFORMANCE_RESOLVES_DIVERGENCE_BY_MAJORITY", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(divergence_resolved_by_latest_file=True)), {"CONFORMANCE_RESOLVES_DIVERGENCE_BY_LATEST_FILE", "NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(divergence_resolved_by_success_count=True)), {"CONFORMANCE_RESOLVES_DIVERGENCE_BY_SUCCESS_COUNT", "NON_CLAIM_MISSING_OR_FLIPPED"}),
        ]
        for relation, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(relation), codes)

    def test_additional_carrier_distributed_operation_and_mutation_block(self) -> None:
        cases = [
            (_selected_relation(relation_result={"additional_carrier_experiment_authorized": True}), {"NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(relation_result={"distributed_operation_authorized": True}), {"NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(mutation_performed=True)), {"NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(replay_performed=True)), {"NON_CLAIM_MISSING_OR_FLIPPED"}),
            (_selected_relation(non_claims=_relation_non_claims(merge_performed=True)), {"NON_CLAIM_MISSING_OR_FLIPPED"}),
        ]
        for relation, codes in cases:
            with self.subTest(codes=codes):
                self._assert_blocked(self._resolve(relation), codes)

    def test_required_non_claim_missing_or_flipped_blocks_and_preserves_visible_non_claims(self) -> None:
        missing = _selected_relation()
        missing["non_claims"] = {}
        flipped = _selected_relation(non_claims=_relation_non_claims(authority_created=True))

        missing_result = self._resolve(missing)
        flipped_result = self._resolve(flipped)

        self._assert_blocked(missing_result, {"NON_CLAIM_MISSING_OR_FLIPPED"})
        self._assert_blocked(flipped_result, {"CONFORMANCE_CREATES_AUTHORITY", "NON_CLAIM_MISSING_OR_FLIPPED"})
        self.assertIn("non_claims_where_available", missing_result["relation_conformance_statement"])
        self.assertIn("non_claims_where_available", flipped_result["relation_conformance_statement"])


if __name__ == "__main__":
    unittest.main()
