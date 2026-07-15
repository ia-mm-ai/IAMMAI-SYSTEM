"""Tests for bounded current-body conformance pass v3.

This suite audits the v3 conformance runner as one successor pass over current
self-orientation v8. It proves the closed multi-carrier relation band remains
downstream and closed in meaning, Carrier B remains receiving evidence only,
visible refusal and divergence remain visible, currentness participation stays
participation, and no current carrier, carrier hierarchy, distributed standing,
continuation, carrier experiment, or distributed operation is created.
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

import run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v3 as runner


TOP_LEVEL_SECTIONS = {
    "current_body_conformance_pass_v3_metadata",
    "selected_conformance_inputs",
    "v8_orientation_basis",
    "recognized_integrated_body_posture",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "current_body_conformance_pass_v3_summary",
}

EXPECTED_CHECK_NAMES = {
    "current_self_orientation_v8_exists",
    "current_self_orientation_v8_is_self_oriented",
    "current_self_orientation_v8_failed_checks_absent",
    "current_governing_basis_recognized",
    "v8_preserves_v7_basis",
    "current_body_conformance_v2_recognized",
    "carrier_role_emission_posture_preserved",
    "carrier_local_emission_admission_posture_preserved",
    "cross_carrier_divergence_posture_preserved",
    "cross_carrier_currentness_participation_recognized",
    "multi_carrier_relation_recognized",
    "multi_carrier_relation_conformance_recognized",
    "multi_carrier_relation_conformance_closure_recognized",
    "relation_closure_meaning_recorded",
    "relation_closure_non_meaning_recorded",
    "carrier_b_returned_receipt_evidence_remains_downstream",
    "visible_refusal_preserved",
    "visible_divergence_preserved",
    "currentness_participation_remained_participation",
    "current_carrier_not_selected",
    "winning_carrier_not_selected",
    "losing_carrier_not_invalidated",
    "carrier_hierarchy_stayed_false",
    "distributed_standing_stayed_false",
    "source_currentness_authority_permission_stayed_false",
    "continuation_stayed_false",
    "additional_carrier_experiment_not_authorized",
    "distributed_operation_not_authorized",
    "self_orientation_conformance_successor_not_forced",
    "v8_current_governing_basis_stayed_upstream",
    "relation_band_stayed_downstream",
    "closed_relation_band_did_not_become_governing_basis",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "mutation_replay_merge_false",
    "follow_on_work_not_authorized",
    "required_non_claims_remain_false",
}

NON_MEANING_TRUE_KEYS = {
    "authority",
    "permission",
    "currentness",
    "next_step_authorization",
    "continuation",
    "additional_carrier_experiment_authorization",
    "distributed_operation_authorization",
    "distributed_standing",
    "carrier_registry",
    "repository_synchronization",
    "full_body_transfer",
    "second_body",
    "presence",
    "threshold",
    "truth",
    "action",
    "consequence",
    "final_governance",
    "final_system_identity",
    "continuity_completion",
    "current_carrier_selected",
    "winning_carrier_selected",
    "losing_carrier_invalidated",
    "carrier_hierarchy",
    "relation_band_became_governing_basis",
    "self_orientation_successor_forced",
    "conformance_successor_forced",
}

OPEN_TRUE_KEYS = {
    "post_v3_conformance_closure_if_later_required",
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

FALSE_NON_CLAIMS = tuple(runner.REQUIRED_FALSE_NON_CLAIMS)

V8_ID = "current_self_orientation_v8_test_self_oriented"
V7_ID = "current_self_orientation_v7_test_self_oriented"
V2_ID = "current_body_conformance_pass_v2_test_body_conformant"
RELATION_ID = "multi_carrier_relation_test_recognized"
RELATION_CONFORMANCE_ID = "multi_carrier_relation_conformance_test_conformant"
RELATION_CLOSURE_ID = "multi_carrier_relation_conformance_closure_test_closed"
CURRENTNESS_ID = "cross_carrier_currentness_test_participation"
DIVERGENCE_ID = "cross_carrier_divergence_test"
ADMISSION_ID = "carrier_local_emission_admission_test"
ROLE_ID = "carrier_role_emission_test"
RECEIPT_ID = "cross_carrier_receipt_test"
RETURNED_BLOCKED_ID = "returned_carrier_b_blocked_receipt_test"
RETURNED_SUCCESS_ID = "returned_carrier_b_success_receipt_test"
CORRESPONDENCE_ID = "cross_surface_correspondence_test"


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


def _snapshot(root: Path) -> dict[str, tuple[int, int]]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(REPO_ROOT)): (path.stat().st_size, path.stat().st_mtime_ns)
        for path in root.rglob("*")
        if path.is_file()
    }


def _non_claims(**updates: bool) -> dict[str, bool]:
    claims = {key: False for key in runner.REQUIRED_FALSE_NON_CLAIMS}
    claims.update(updates)
    return claims


def _selected(
    result_id: str | None,
    outcome: str | None,
    path: str | None,
    *,
    downstream_only: bool | None = True,
    current_or_governing_basis: bool | None = False,
) -> dict[str, object]:
    return {
        "artifact_label": result_id,
        "selected": bool(result_id),
        "result_id": result_id,
        "path": path,
        "result_path": path,
        "outcome": outcome,
        "result_type": "synthetic_bounded_result",
        "result_version": "0.1.0",
        "resolver_module": "synthetic_bounded_resolver",
        "downstream_only": downstream_only,
        "current_or_governing_basis": current_or_governing_basis,
    }


def valid_v8(**updates: object) -> dict[str, object]:
    non_claims = _non_claims()
    result: dict[str, object] = {
        "current_self_orientation_v8_metadata": {
            "self_orientation_result_id": V8_ID,
            "self_orientation_result_type": "current_self_orientation_v8_result",
            "self_orientation_result_version": "0.8.0",
            "generated_at": "2026-04-29T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v8",
            "successor_of_module": "resolve_current_self_orientation_v7",
        },
        "selected_orientation_inputs": {
            "selected_current_self_orientation_v7_result": _selected(
                V7_ID,
                "SELF_ORIENTED",
                "artifacts/test/v7.json",
                downstream_only=False,
            ),
            "selected_current_body_conformance_v2_result": _selected(
                V2_ID,
                "BODY_CONFORMANT",
                "artifacts/test/v2.json",
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
            "selected_cross_carrier_currentness_result": _selected(
                CURRENTNESS_ID,
                "CURRENTNESS_PARTICIPATION_ELIGIBLE",
                "artifacts/test/currentness.json",
            ),
            "selected_cross_carrier_divergence_result": _selected(
                DIVERGENCE_ID,
                "CROSS_CARRIER_DIVERGENCE_RECORDED",
                "artifacts/test/divergence.json",
            ),
            "selected_carrier_local_emission_admission_result": _selected(
                ADMISSION_ID,
                "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
                "artifacts/test/admission.json",
            ),
            "selected_carrier_role_emission_result": _selected(
                ROLE_ID,
                "CARRIER_EMISSION_RECOGNIZED",
                "artifacts/test/role.json",
            ),
            "selected_cross_carrier_receipt_result": _selected(
                RECEIPT_ID,
                "CARRIED_SURFACE_RECEIVED",
                "artifacts/test/receipt.json",
            ),
            "selected_returned_carrier_b_blocked_receipt_result": _selected(
                RETURNED_BLOCKED_ID,
                "BLOCKED",
                "artifacts/test/returned_blocked.json",
            ),
            "selected_returned_carrier_b_successful_receipt_result": _selected(
                RETURNED_SUCCESS_ID,
                "CARRIED_SURFACE_RECEIVED",
                "artifacts/test/returned_success.json",
            ),
            "selected_cross_surface_correspondence_result": _selected(
                CORRESPONDENCE_ID,
                "CORRESPONDENCE_RECOGNIZED",
                "artifacts/test/correspondence.json",
            ),
            "selection_posture": {
                "latest_file_currentness_refused": True,
                "multi_carrier_relation_band_downstream_only": True,
                "relation_band_does_not_determine_current_or_governing_basis": True,
                "v8_uses_v7_as_successor_basis": True,
            },
        },
        "self_orientation_basis": {
            "basis_statement": "Synthetic v8 basis for v3 conformance tests.",
            "current_governing_basis_source": "inherited_from_v7_upstream_basis",
            "multi_carrier_relation_band_posture": "downstream_only",
            "closed_relation_band_determines_current_or_governing_basis": False,
            "latest_file_currentness_used": False,
            "passed_check_count": 30,
            "failed_check_count": 0,
            "selected_top_level_basis_ids": {
                "current_self_orientation_v7": V7_ID,
                "current_body_conformance_v2": V2_ID,
                "multi_carrier_relation": RELATION_ID,
                "multi_carrier_relation_conformance": RELATION_CONFORMANCE_ID,
                "multi_carrier_relation_conformance_closure": RELATION_CLOSURE_ID,
            },
            "key_non_claims": copy.deepcopy(non_claims),
        },
        "recognized_multi_carrier_relation_surfaces": {
            "recognized": True,
            "downstream_only": True,
            "current_or_governing_basis": False,
            "downstream_evidence_posture_preserved": True,
        },
        "recognized_multi_carrier_relation_conformance_surfaces": {
            "recognized": True,
            "downstream_only": True,
            "current_or_governing_basis": False,
            "downstream_evidence_posture_preserved": True,
        },
        "recognized_multi_carrier_relation_conformance_closure_surfaces": {
            "recognized": True,
            "downstream_only": True,
            "current_or_governing_basis": False,
            "relation_conformance_closed": True,
            "conformance_meaning_recorded": True,
            "conformance_non_meaning_recorded": True,
        },
        "current_self_orientation_summary": {
            "outcome": "SELF_ORIENTED",
            "selected_v7_self_orientation_id": V7_ID,
            "selected_current_body_conformance_v2_id": V2_ID,
            "selected_multi_carrier_relation_id": RELATION_ID,
            "selected_multi_carrier_relation_conformance_id": RELATION_CONFORMANCE_ID,
            "selected_multi_carrier_relation_conformance_closure_id": RELATION_CLOSURE_ID,
            "current_governing_basis_recognized": True,
            "current_self_orientation_v7_recognized": True,
            "current_body_conformance_v2_recognized": True,
            "carrier_role_emission_recognized": True,
            "carrier_local_emission_admission_recognized": False,
            "cross_carrier_divergence_recognized": False,
            "cross_carrier_currentness_participation_recognized": True,
            "multi_carrier_relation_recognized": True,
            "multi_carrier_relation_conformance_recognized": True,
            "multi_carrier_relation_conformance_closure_recognized": True,
            "relation_conformance_closure_meaning_recorded": True,
            "relation_conformance_closure_non_meaning_recorded": True,
            "carrier_b_returned_receipt_evidence_remains_downstream": True,
            "visible_refusal_remains_visible": True,
            "visible_divergence_remains_visible": True,
            "currentness_participation_remained_participation": True,
            "current_carrier_not_selected": True,
            "no_winning_losing_carrier_collapse_occurred": True,
            "carrier_hierarchy_stayed_false": True,
            "distributed_standing_stayed_false": True,
            "source_currentness_authority_permission_stayed_false": True,
            "continuation_stayed_false": True,
            "additional_carrier_experiment_authorization_stayed_false": True,
            "distributed_operation_authorization_stayed_false": True,
            "self_orientation_conformance_successor_not_forced": True,
            "correspondence_checks_passed": True,
            "passed_check_count": 30,
            "failed_check_count": 0,
            "key_non_claims": copy.deepcopy(non_claims),
        },
        "bounded_correspondence_checks": [
            {
                "check_name": "v8_posture_check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
            }
        ],
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "non_claims": copy.deepcopy(non_claims),
    }
    result.update(updates)
    return result


def resolve(v8: dict[str, object] | None = None) -> dict:
    return runner.run_current_body_conformance_pass_v3(v8)


class CurrentBodyConformancePassV3RealArtifactTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.result = runner.run_current_body_conformance_pass_v3()

    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result), result.keys())

    def test_real_body_conformant_v3_path_has_shape_and_metadata(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assert_top_level_shape(self.result)
        self.assertIn(self.result["outcome"], {"BODY_CONFORMANT", "BLOCKED"})
        self.assertEqual(self.result["outcome"], "BODY_CONFORMANT")
        self.assertIsNone(self.result["block"]["block_code"])
        self.assertIsNone(self.result["block"]["block_reason"])

        metadata = self.result["current_body_conformance_pass_v3_metadata"]
        for key in (
            "current_body_conformance_pass_v3_result_id",
            "current_body_conformance_pass_v3_result_type",
            "current_body_conformance_pass_v3_result_version",
            "generated_at",
            "resolver_module",
            "successor_of_module",
        ):
            self.assertTrue(metadata.get(key), key)
        self.assertEqual(metadata["current_body_conformance_pass_v3_result_version"], "0.3.0")
        self.assertEqual(
            metadata["resolver_module"],
            "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v3",
        )
        self.assertEqual(
            metadata["successor_of_module"],
            "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2",
        )

    def test_selected_inputs_orientation_basis_and_integrated_posture(self) -> None:
        selected = self.result["selected_conformance_inputs"]
        for key in (
            "selected_current_self_orientation_v8_result",
            "selected_current_self_orientation_v7_result",
            "selected_current_body_conformance_v2_result",
            "selected_multi_carrier_relation_result",
            "selected_multi_carrier_relation_conformance_result",
            "selected_multi_carrier_relation_conformance_closure_result",
            "selected_cross_carrier_currentness_result",
            "selected_cross_carrier_divergence_result",
            "selected_carrier_local_emission_admission_result",
            "selected_carrier_role_emission_result",
        ):
            self.assertIn(key, selected)
        for key in (
            "selected_current_self_orientation_v8_result",
            "selected_current_self_orientation_v7_result",
            "selected_current_body_conformance_v2_result",
            "selected_multi_carrier_relation_result",
            "selected_multi_carrier_relation_conformance_result",
            "selected_multi_carrier_relation_conformance_closure_result",
        ):
            self.assertTrue(selected[key].get("result_id"), key)
        self.assertEqual(selected["selected_current_self_orientation_v8_result"]["outcome"], "SELF_ORIENTED")
        self.assertEqual(selected["selected_current_self_orientation_v7_result"]["outcome"], "SELF_ORIENTED")

        basis = self.result["v8_orientation_basis"]
        self.assertEqual(basis["selected_v8_id"], selected["selected_current_self_orientation_v8_result"]["result_id"])
        self.assertEqual(basis["selected_v8_path"], selected["selected_current_self_orientation_v8_result"]["result_path"])
        self.assertEqual(basis["selected_v8_outcome"], "SELF_ORIENTED")
        self.assertEqual(basis["selected_v7_id"], selected["selected_current_self_orientation_v7_result"]["result_id"])
        self.assertIsInstance(basis["v8_self_orientation_basis"], dict)
        self.assertIsInstance(basis["v8_summary"], dict)
        self.assertTrue(basis["v8_is_conformance_input_not_authority"])

        posture = self.result["recognized_integrated_body_posture"]
        for key in (
            "v8_posture_coherent_as_current_body_mirror",
            "current_governing_basis_remains_upstream",
            "reentry_body_signal_derivative_vessel_and_operator_surfaces_remain_downstream",
            "carrier_receipt_admission_divergence_currentness_relation_conformance_closure_surfaces_remain_downstream",
            "closed_multi_carrier_relation_band_remains_closed_in_meaning_only",
            "relation_conformance_closure_meaning_preserved",
            "relation_conformance_closure_non_meaning_preserved",
            "carrier_b_remains_receiving_carrier_evidence_only",
            "returned_receipt_evidence_preserved",
            "visible_refusal_evidence_preserved",
            "visible_divergence_evidence_preserved",
            "currentness_participation_remained_participation",
            "returned_evidence_did_not_replace_source",
            "returned_evidence_did_not_create_currentness",
            "all_selected_non_claims_remain_false",
        ):
            self.assertTrue(posture[key], key)

    def test_checks_statement_nonmeaning_open_surfaces_summary_and_non_claims(self) -> None:
        checks = self.result["conformance_checks"]
        self.assertTrue(checks)
        self.assertTrue(all(check["passed"] is True for check in checks))
        self.assertEqual(0, self.result["current_body_conformance_pass_v3_summary"]["failed_check_count"])
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({check["check_name"] for check in checks}))
        for check in checks:
            self.assertTrue({"check_name", "passed", "expected_posture", "actual_posture", "block_code"}.issubset(check))

        statement = self.result["conformance_statement"]
        for key in (
            "v8_body_posture_conformant",
            "current_governing_basis_remains_upstream",
            "downstream_surfaces_remain_downstream",
            "closed_multi_carrier_relation_band_remains_downstream",
            "relation_conformance_closure_meaning_preserved",
            "relation_conformance_closure_non_meaning_preserved",
            "carrier_b_remained_receiving_carrier_evidence_only",
            "returned_receipt_evidence_preserved",
            "visible_refusal_evidence_preserved",
            "visible_divergence_evidence_preserved",
            "currentness_participation_remained_participation",
            "no_current_carrier_selected",
            "no_winning_carrier_selected",
            "no_losing_carrier_invalidated",
            "no_carrier_hierarchy_created",
            "no_authority_created",
            "no_permission_created",
            "no_currentness_created",
            "no_source_replaced",
            "no_distributed_standing_created",
            "no_presence_threshold_truth_action_consequence_created",
            "no_continuation_authorized",
            "no_additional_carrier_experiment_authorized",
            "no_distributed_operation_authorized",
            "no_successor_forced",
        ):
            self.assertTrue(statement[key], key)

        for key in NON_MEANING_TRUE_KEYS:
            self.assertTrue(self.result["conformance_non_meaning"][key], key)

        for key in OPEN_TRUE_KEYS:
            self.assertTrue(self.result["what_remains_open"][key], key)

        summary = runner.build_current_body_conformance_pass_v3_summary(self.result)
        self.assertEqual(summary["outcome"], "BODY_CONFORMANT")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        for key in (
            "selected_v8_id",
            "selected_v8_path",
            "selected_v8_outcome",
            "selected_v7_id",
            "selected_current_body_conformance_v2_id",
            "selected_multi_carrier_relation_id",
            "selected_multi_carrier_relation_conformance_id",
            "selected_multi_carrier_relation_conformance_closure_id",
        ):
            self.assertTrue(summary[key], key)
        self.assertEqual(summary["passed_check_count"], len(checks))
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "v8_body_posture_conformant",
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
            "no_current_winning_losing_carrier_collapse",
            "no_carrier_hierarchy",
            "no_authority_permission_currentness_source_replacement",
            "no_distributed_standing",
            "no_presence_threshold_truth_action_consequence",
            "no_continuation",
            "no_additional_carrier_experiment",
            "no_distributed_operation",
            "no_successor_forced",
        ):
            self.assertTrue(summary[key], key)

        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, self.result["non_claims"], key)
            self.assertIs(self.result["non_claims"][key], False, key)
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_path_write_default_output_and_nonmutation(self) -> None:
        selected = self.result["selected_conformance_inputs"]
        v8_path = selected["selected_current_self_orientation_v8_result"]["result_path"]
        path_result = runner.run_current_body_conformance_pass_v3_from_path(v8_path)
        self.assert_top_level_shape(path_result)
        self.assertEqual(path_result["outcome"], "BODY_CONFORMANT")
        self.assertEqual(
            path_result["selected_conformance_inputs"]["selected_current_self_orientation_v8_result"]["result_path"],
            v8_path,
        )
        self.assertFalse(any(path_result["non_claims"][key] for key in FALSE_NON_CLAIMS))

        roots = [
            runner.CURRENT_SELF_ORIENTATION_V8_ROOT,
            runner.CURRENT_SELF_ORIENTATION_V7_ROOT,
            runner.CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT,
            runner.MULTI_CARRIER_RELATION_ROOT,
            runner.MULTI_CARRIER_RELATION_CONFORMANCE_ROOT,
            runner.MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT,
            runner.CROSS_CARRIER_CURRENTNESS_ROOT,
            runner.CROSS_CARRIER_DIVERGENCE_ROOT,
            runner.CARRIER_LOCAL_EMISSION_ADMISSION_ROOT,
            runner.CARRIER_ROLE_EMISSION_ROOT,
        ]
        before = {root: _snapshot(root) for root in roots}
        runner.run_current_body_conformance_pass_v3()
        after = {root: _snapshot(root) for root in roots}
        self.assertEqual(before, after)

        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "v3_result.json"
            written = runner.write_current_body_conformance_pass_v3_result(self.result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(_read_json(written)))

            with mock.patch.object(runner, "CURRENT_BODY_CONFORMANCE_PASS_V3_ROOT", Path(tmp) / "default"):
                first = runner.write_current_body_conformance_pass_v3_result(self.result)
                second = runner.write_current_body_conformance_pass_v3_result(self.result)
                self.assertNotEqual(first, second)
                self.assertTrue(str(first).startswith(str(Path(tmp) / "default")))
                self.assertTrue(first.name.endswith("__current_body_conformance_pass_v3_result.json"))
                self.assertIn("__current_body_conformance_pass_v3_result_001.json", second.name)

            self.assertEqual(before, {root: _snapshot(root) for root in roots})

    def test_repeated_resolution_does_not_mutate_supplied_mapping(self) -> None:
        v8 = valid_v8()
        original = copy.deepcopy(v8)
        first = runner.run_current_body_conformance_pass_v3(v8)
        second = runner.run_current_body_conformance_pass_v3(v8)
        self.assertEqual(first["outcome"], "BODY_CONFORMANT")
        self.assertEqual(second["outcome"], "BODY_CONFORMANT")
        self.assertEqual(v8, original)


class CurrentBodyConformancePassV3BlockedTests(unittest.TestCase):
    def assert_block(self, v8: dict[str, object] | None, expected: str | set[str]) -> dict:
        result = runner.run_current_body_conformance_pass_v3(v8)
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertIn(result["outcome"], {"BODY_CONFORMANT", "BLOCKED"})
        code = result["block"]["block_code"]
        if isinstance(expected, set):
            self.assertIn(code, expected)
        else:
            self.assertEqual(code, expected)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
        return result

    def test_declared_block_family_and_missing_or_malformed_v8(self) -> None:
        self.assertTrue(
            {
                "CURRENT_SELF_ORIENTATION_V8_MISSING",
                "CURRENT_SELF_ORIENTATION_V8_NOT_SELF_ORIENTED",
                "CURRENT_SELF_ORIENTATION_V8_FAILED_CHECKS_PRESENT",
                "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
                "CURRENT_SELF_ORIENTATION_V7_BASIS_MISSING",
                "CURRENT_BODY_CONFORMANCE_V2_NOT_RECOGNIZED",
                "MULTI_CARRIER_RELATION_NOT_RECOGNIZED",
                "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_RECOGNIZED",
                "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_RECOGNIZED",
                "RELATION_CLOSURE_MEANING_NOT_RECORDED",
                "RELATION_CLOSURE_NON_MEANING_NOT_RECORDED",
                "CARRIER_B_RETURNED_EVIDENCE_NOT_DOWNSTREAM",
                "VISIBLE_REFUSAL_NOT_PRESERVED",
                "VISIBLE_DIVERGENCE_NOT_PRESERVED",
                "CURRENTNESS_PARTICIPATION_COLLAPSED",
                "CURRENT_CARRIER_SELECTED",
                "WINNING_OR_LOSING_CARRIER_COLLAPSE",
                "CARRIER_HIERARCHY_CREATED",
                "DISTRIBUTED_STANDING_CREATED",
                "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE",
                "CONTINUATION_AUTHORIZED",
                "ADDITIONAL_CARRIER_EXPERIMENT_AUTHORIZED",
                "DISTRIBUTED_OPERATION_AUTHORIZED",
                "SUCCESSOR_PRESSURE_FORCED",
                "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS",
                "LATEST_FILE_CURRENTNESS_REFUSED",
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            }.issubset(runner.BLOCK_REASONS)
        )

        with tempfile.TemporaryDirectory() as tmp:
            empty = Path(tmp) / "v8"
            empty.mkdir()
            with mock.patch.object(runner, "CURRENT_SELF_ORIENTATION_V8_ROOT", empty):
                result = runner.run_current_body_conformance_pass_v3()
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V8_MISSING")

        with tempfile.TemporaryDirectory() as tmp:
            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            result = runner.run_current_body_conformance_pass_v3_from_path(malformed)
            self.assertEqual(result["outcome"], "BLOCKED")
            self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V8_MALFORMED")

            array_path = Path(tmp) / "array.json"
            _write_json(array_path, [])
            result = runner.run_current_body_conformance_pass_v3_from_path(array_path)
            self.assertEqual(result["outcome"], "BLOCKED")
            self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V8_MALFORMED")

    def test_blocks_for_v8_outcome_failed_checks_basis_and_required_recognition(self) -> None:
        v8 = valid_v8(outcome="BLOCKED", block={"block_code": "SYNTHETIC", "block_reason": "blocked"})
        self.assert_block(v8, "CURRENT_SELF_ORIENTATION_V8_NOT_SELF_ORIENTED")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["failed_check_count"] = 1
        self.assert_block(v8, "CURRENT_SELF_ORIENTATION_V8_FAILED_CHECKS_PRESENT")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["current_governing_basis_recognized"] = False
        self.assert_block(v8, "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["selected_v7_self_orientation_id"] = None
        self.assert_block(v8, "CURRENT_SELF_ORIENTATION_V7_BASIS_MISSING")

        cases = (
            ("current_body_conformance_v2_recognized", "CURRENT_BODY_CONFORMANCE_V2_NOT_RECOGNIZED"),
            ("multi_carrier_relation_recognized", "MULTI_CARRIER_RELATION_NOT_RECOGNIZED"),
            ("multi_carrier_relation_conformance_recognized", "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_RECOGNIZED"),
            ("multi_carrier_relation_conformance_closure_recognized", "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_RECOGNIZED"),
            ("relation_conformance_closure_meaning_recorded", "RELATION_CLOSURE_MEANING_NOT_RECORDED"),
            ("relation_conformance_closure_non_meaning_recorded", "RELATION_CLOSURE_NON_MEANING_NOT_RECORDED"),
            ("carrier_b_returned_receipt_evidence_remains_downstream", "CARRIER_B_RETURNED_EVIDENCE_NOT_DOWNSTREAM"),
            ("visible_refusal_remains_visible", "VISIBLE_REFUSAL_NOT_PRESERVED"),
            ("visible_divergence_remains_visible", "VISIBLE_DIVERGENCE_NOT_PRESERVED"),
            ("currentness_participation_remained_participation", "CURRENTNESS_PARTICIPATION_COLLAPSED"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                v8 = valid_v8()
                v8["current_self_orientation_summary"][
                    "carrier_local_emission_admission_recognized"
                ] = True
                v8["current_self_orientation_summary"][
                    "cross_carrier_divergence_recognized"
                ] = True
                v8["current_self_orientation_summary"][flag] = False
                self.assert_block(v8, code)

    def test_blocks_for_carrier_currentness_hierarchy_distribution_and_source_collapse(self) -> None:
        cases = (
            ({"current_carrier_selected": True}, "CURRENT_CARRIER_SELECTED"),
            ({"winning_carrier_selected": True}, "WINNING_OR_LOSING_CARRIER_COLLAPSE"),
            ({"losing_carrier_invalidated": True}, "WINNING_OR_LOSING_CARRIER_COLLAPSE"),
            ({"carrier_hierarchy_created": True}, "CARRIER_HIERARCHY_CREATED"),
            ({"distributed_standing_created": True}, "DISTRIBUTED_STANDING_CREATED"),
            ({"source_replaced": True}, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE"),
            ({"currentness_created": True}, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE"),
            ({"authority_created": True}, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE"),
            ({"permission_created": True}, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE"),
            ({"continuation_authorized": True}, "CONTINUATION_AUTHORIZED"),
            ({"additional_carrier_experiment_authorized": True}, "ADDITIONAL_CARRIER_EXPERIMENT_AUTHORIZED"),
            ({"distributed_operation_authorized": True}, "DISTRIBUTED_OPERATION_AUTHORIZED"),
            ({"self_orientation_successor_forced": True}, "SUCCESSOR_PRESSURE_FORCED"),
            ({"conformance_successor_forced": True}, "SUCCESSOR_PRESSURE_FORCED"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                v8 = valid_v8(non_claims=_non_claims(**claims))
                v8["current_self_orientation_summary"]["key_non_claims"] = _non_claims(**claims)
                v8["self_orientation_basis"]["key_non_claims"] = _non_claims(**claims)
                result = self.assert_block(v8, code)
                for key, value in claims.items():
                    self.assertIs(result["non_claims"][key], value, key)

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["current_carrier_not_selected"] = False
        self.assert_block(v8, "CURRENT_CARRIER_SELECTED")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["no_winning_losing_carrier_collapse_occurred"] = False
        self.assert_block(v8, "WINNING_OR_LOSING_CARRIER_COLLAPSE")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["carrier_hierarchy_stayed_false"] = False
        self.assert_block(v8, "CARRIER_HIERARCHY_CREATED")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["distributed_standing_stayed_false"] = False
        self.assert_block(v8, "DISTRIBUTED_STANDING_CREATED")

        v8 = valid_v8()
        v8["current_self_orientation_summary"]["source_currentness_authority_permission_stayed_false"] = False
        self.assert_block(v8, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_COLLAPSE")

    def test_blocks_for_relation_band_latest_mutation_and_required_non_claims(self) -> None:
        v8 = valid_v8()
        v8["self_orientation_basis"]["multi_carrier_relation_band_posture"] = "governing_basis"
        self.assert_block(v8, "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS")

        v8 = valid_v8()
        v8["self_orientation_basis"]["closed_relation_band_determines_current_or_governing_basis"] = True
        self.assert_block(v8, "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS")

        v8 = valid_v8()
        v8["selected_orientation_inputs"]["selection_posture"][
            "relation_band_does_not_determine_current_or_governing_basis"
        ] = False
        self.assert_block(v8, "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS")

        cases = (
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS_REFUSED"),
            ({"recency_fraud": True}, "LATEST_FILE_CURRENTNESS_REFUSED"),
            ({"mutation_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"merge_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"follow_on_steps_authorized": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"follow_on_work_authorized": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"v3_conformance_authorized_expansion": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                v8 = valid_v8(non_claims=_non_claims(**claims))
                v8["current_self_orientation_summary"]["key_non_claims"] = _non_claims(**claims)
                v8["self_orientation_basis"]["key_non_claims"] = _non_claims(**claims)
                result = self.assert_block(v8, code)
                for key, value in claims.items():
                    self.assertIs(result["non_claims"][key], value, key)

        v8 = valid_v8()
        v8["self_orientation_basis"]["latest_file_currentness_used"] = True
        self.assert_block(v8, "LATEST_FILE_CURRENTNESS_REFUSED")

    def test_relation_band_can_preserve_admission_and_divergence_when_direct_optional_flags_are_false(self) -> None:
        v8 = valid_v8()
        self.assertFalse(v8["current_self_orientation_summary"]["carrier_local_emission_admission_recognized"])
        self.assertFalse(v8["current_self_orientation_summary"]["cross_carrier_divergence_recognized"])
        result = runner.run_current_body_conformance_pass_v3(v8)
        self.assertEqual(result["outcome"], "BODY_CONFORMANT")
        summary = result["current_body_conformance_pass_v3_summary"]
        self.assertTrue(summary["carrier_local_emission_admission_posture_preserved"])
        self.assertTrue(summary["cross_carrier_divergence_posture_preserved"])


if __name__ == "__main__":
    unittest.main()
