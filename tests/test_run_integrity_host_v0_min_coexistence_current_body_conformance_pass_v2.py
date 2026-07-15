"""Tests for bounded current-body conformance pass v2.

This suite audits the v2 conformance runner as one successor pass over the
current self-orientation v7 posture. It verifies coherence after v7 mirrored
post-conformance closure, correspondence, cross-carrier receipt, returned
Carrier B receipt evidence, and visible Carrier B refusal evidence.
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

import run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2 as runner


TOP_LEVEL_SECTIONS = {
    "current_body_conformance_pass_v2_metadata",
    "selected_conformance_inputs",
    "v7_orientation_basis",
    "recognized_integrated_body_posture",
    "conformance_checks",
    "conformance_statement",
    "conformance_non_meaning",
    "what_remains_open",
    "non_claims",
    "outcome",
    "block",
    "current_body_conformance_pass_v2_summary",
}

EXPECTED_CHECK_NAMES = {
    "current_self_orientation_v7_exists",
    "current_self_orientation_v7_is_self_oriented",
    "current_self_orientation_v7_failed_checks_absent",
    "current_governing_basis_recognized",
    "v7_preserves_v6_basis",
    "current_body_conformance_recognized",
    "post_conformance_closure_recognized",
    "cross_surface_correspondence_recognized",
    "cross_carrier_receipt_recognized",
    "returned_carrier_b_receipt_evidence_recognized",
    "returned_carrier_b_refusal_evidence_remains_visible",
    "receipt_alignment_correspondence_recognized",
    "refusal_visible_correspondence_recognized",
    "conformance_stayed_downstream",
    "closure_stayed_downstream",
    "correspondence_stayed_downstream",
    "receipt_stayed_downstream",
    "carrier_b_stayed_receiving_carrier_only",
    "source_currentness_authority_permission_successor_body_collapse_stayed_false",
    "conformance_did_not_become_authority_permission_or_currentness",
    "closure_did_not_become_authority_permission_signal_or_continuation",
    "correspondence_did_not_become_authority_currentness_permission_signal_or_action",
    "receipt_did_not_become_source_currentness_authority_permission_successor_or_body",
    "receipt_did_not_become_signal_presence_threshold_truth_action_or_consequence",
    "multi_carrier_law_not_created",
    "distributed_standing_not_created",
    "latest_file_currentness_false",
    "recency_fraud_false",
    "mutation_replay_merge_false",
    "follow_on_work_not_authorized",
    "self_orientation_successor_not_forced",
    "conformance_successor_not_forced_beyond_this_declared_pass",
    "required_non_claims_remain_false",
}

NON_MEANING_TRUE_KEYS = {
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_authorize_next_step",
    "does_not_authorize_continuation",
    "does_not_establish_presence",
    "does_not_establish_threshold",
    "does_not_create_truth",
    "does_not_authorize_action",
    "does_not_create_consequence",
    "does_not_complete_final_governance",
    "does_not_complete_final_system_identity",
    "does_not_complete_continuity",
    "does_not_create_multi_carrier_law",
    "does_not_create_distributed_standing",
    "does_not_create_carrier_registry",
    "does_not_synchronize_repository",
    "does_not_transfer_full_body",
    "does_not_create_second_body",
    "does_not_create_external_contact",
    "does_not_force_self_orientation_successor",
    "does_not_force_conformance_successor",
}

OPEN_SURFACES = {
    "post-v2 conformance closure, if later required",
    "multi-carrier relation law",
    "distributed standing",
    "persistence/registry law",
    "presence law",
    "threshold law",
    "truth law",
    "action/consequence law",
    "generalized vessel relation lifecycle",
    "body relevance medium",
    "signal series or accumulation logic",
    "future self-orientation successor only if separately justified",
}

FALSE_NON_CLAIMS = tuple(runner.REQUIRED_FALSE_NON_CLAIMS)

V7_ID = "current_self_orientation_v7_test_self_oriented"
V6_ID = "current_self_orientation_v6_test_self_oriented"
CONFORMANCE_ID = "current_body_conformance_test_body_conformant"
CLOSURE_ID = "post_conformance_closure_test_recorded"
CLOSURE_ALIGNMENT_ID = "closure_alignment_correspondence_test"
LOCAL_RECEIPT_ID = "local_cross_carrier_receipt_test"
RETURNED_BLOCKED_RECEIPT_ID = "returned_carrier_b_blocked_receipt_test"
RETURNED_SUCCESS_RECEIPT_ID = "returned_carrier_b_successful_receipt_test"
RECEIPT_ALIGNMENT_ID = "receipt_alignment_correspondence_test"
REFUSAL_VISIBLE_ID = "refusal_visible_correspondence_test"


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


def _repo_path(path: str | None) -> Path | None:
    if not path:
        return None
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


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
    claims.update(
        {
            "closure_authorized_next_work": False,
            "correspondence_became_signal": False,
            "correspondence_became_presence": False,
            "correspondence_became_threshold": False,
            "correspondence_became_truth": False,
            "correspondence_became_action": False,
            "correspondence_became_consequence": False,
            "receipt_became_source": False,
            "receipt_became_currentness": False,
            "receipt_became_authority": False,
            "receipt_became_permission": False,
            "self_orientation_successor_forced": False,
            "conformance_successor_forced": False,
        }
    )
    claims.update(updates)
    return claims


def _selected(result_id: str, outcome: str, path: str) -> dict[str, str]:
    return {
        "result_id": result_id,
        "result_path": path,
        "outcome": outcome,
        "selection_mode": "synthetic_bounded_v7_input",
    }


def valid_v7(**updates: object) -> dict[str, object]:
    result: dict[str, object] = {
        "current_self_orientation_v7_metadata": {
            "self_orientation_result_id": V7_ID,
            "self_orientation_result_type": "current_self_orientation_v7_result",
            "self_orientation_result_version": "0.7.0",
            "generated_at": "2026-04-28T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v7",
            "successor_of_module": "resolve_current_self_orientation_v6",
        },
        "selected_orientation_inputs": {
            "selected_current_self_orientation_v6_result": _selected(
                V6_ID,
                "SELF_ORIENTED",
                "artifacts/test/v6.json",
            ),
            "selected_current_body_conformance_result": _selected(
                CONFORMANCE_ID,
                "BODY_CONFORMANT",
                "artifacts/test/conformance.json",
            ),
            "selected_post_conformance_closure_result": _selected(
                CLOSURE_ID,
                "CONFORMANCE_CLOSURE_RECORDED",
                "artifacts/test/closure.json",
            ),
            "selected_closure_alignment_correspondence_result": _selected(
                CLOSURE_ALIGNMENT_ID,
                "CORRESPONDENCE_RECOGNIZED",
                "artifacts/test/closure_alignment.json",
            ),
            "selected_local_cross_carrier_receipt_result": _selected(
                LOCAL_RECEIPT_ID,
                "CARRIED_SURFACE_RECEIVED",
                "artifacts/test/local_receipt.json",
            ),
            "selected_returned_carrier_b_blocked_receipt_result": _selected(
                RETURNED_BLOCKED_RECEIPT_ID,
                "BLOCKED",
                "artifacts/test/returned_blocked_receipt.json",
            ),
            "selected_returned_carrier_b_successful_receipt_result": _selected(
                RETURNED_SUCCESS_RECEIPT_ID,
                "CARRIED_SURFACE_RECEIVED",
                "artifacts/test/returned_success_receipt.json",
            ),
            "selected_receipt_alignment_correspondence_result": _selected(
                RECEIPT_ALIGNMENT_ID,
                "CORRESPONDENCE_RECOGNIZED",
                "artifacts/test/receipt_alignment.json",
            ),
            "selected_refusal_visible_correspondence_result": _selected(
                REFUSAL_VISIBLE_ID,
                "CORRESPONDENCE_RECOGNIZED",
                "artifacts/test/refusal_visible.json",
            ),
        },
        "self_orientation_basis": {
            "current_governing_basis_remains_inherited_from_v6_upstream_surfaces": True,
            "conformance_surfaces_remain_downstream_audit_only": True,
            "closure_surfaces_remain_downstream_meaning_closure_only": True,
            "correspondence_surfaces_remain_bounded_reading_relation_only": True,
            "receipt_surfaces_remain_carried_evidence_only": True,
            "carrier_b_remains_receiving_carrier_only": True,
        },
        "current_self_orientation_summary": {
            "outcome": "SELF_ORIENTED",
            "selected_current_self_orientation_v6_id": V6_ID,
            "selected_current_body_conformance_id": CONFORMANCE_ID,
            "selected_post_conformance_closure_id": CLOSURE_ID,
            "selected_closure_alignment_correspondence_id": CLOSURE_ALIGNMENT_ID,
            "selected_local_cross_carrier_receipt_id": LOCAL_RECEIPT_ID,
            "selected_returned_carrier_b_blocked_receipt_id": RETURNED_BLOCKED_RECEIPT_ID,
            "selected_returned_carrier_b_successful_receipt_id": RETURNED_SUCCESS_RECEIPT_ID,
            "selected_receipt_alignment_correspondence_id": RECEIPT_ALIGNMENT_ID,
            "selected_refusal_visible_correspondence_id": REFUSAL_VISIBLE_ID,
            "current_governing_basis_recognized": True,
            "reentry_surfaces_recognized": True,
            "body_signal_surfaces_recognized": True,
            "derivative_vessel_relation_boundary_recognized": True,
            "current_body_conformance_recognized": True,
            "post_conformance_closure_recognized": True,
            "cross_surface_correspondence_recognized": True,
            "cross_carrier_receipt_recognized": True,
            "carrier_b_returned_receipt_evidence_recognized": True,
            "carrier_b_refusal_evidence_remains_visible": True,
            "receipt_alignment_correspondence_recognized": True,
            "refusal_visible_correspondence_recognized": True,
            "carrier_b_remained_receiving_carrier_only": True,
            "source_currentness_authority_permission_successor_body_collapse_stayed_false": True,
            "multi_carrier_law_stayed_false": True,
            "distributed_standing_stayed_false": True,
            "presence_threshold_truth_action_consequence_stayed_false": True,
            "correspondence_checks_passed": True,
            "failed_check_count": 0,
        },
        "bounded_correspondence_checks": [
            {
                "check_name": "v7_posture_check",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
            }
        ],
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "non_claims": _non_claims(),
    }
    result.update(updates)
    return result


def resolve(v7: dict[str, object] | None = None) -> dict:
    return runner.run_current_body_conformance_pass_v2(v7)


class CurrentBodyConformancePassV2RealArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = runner.run_current_body_conformance_pass_v2()

    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result), result.keys())

    def test_real_body_conformant_v2_path_has_shape_and_metadata(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assert_top_level_shape(self.result)
        self.assertEqual(self.result["outcome"], "BODY_CONFORMANT")
        self.assertEqual(self.result["block"], {"block_code": None, "block_reason": None})
        self.assertIn(self.result["outcome"], {"BODY_CONFORMANT", "BLOCKED"})

        metadata = self.result["current_body_conformance_pass_v2_metadata"]
        for key in (
            "current_body_conformance_pass_v2_result_id",
            "current_body_conformance_pass_v2_result_type",
            "current_body_conformance_pass_v2_result_version",
            "generated_at",
            "resolver_module",
            "successor_of_module",
        ):
            self.assertTrue(metadata.get(key), key)
        self.assertEqual(metadata["current_body_conformance_pass_v2_result_version"], "0.2.0")
        self.assertEqual(
            metadata["resolver_module"],
            "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2",
        )
        self.assertEqual(
            metadata["successor_of_module"],
            "run_integrity_host_v0_min_coexistence_current_body_conformance_pass",
        )

    def test_selected_inputs_orientation_basis_and_integrated_posture(self) -> None:
        selected = self.result["selected_conformance_inputs"]
        for key in (
            "selected_current_self_orientation_v7_result",
            "selected_current_self_orientation_v6_result",
            "selected_previous_current_body_conformance_result",
            "selected_post_conformance_closure_result",
            "selected_closure_alignment_correspondence_result",
            "selected_local_cross_carrier_receipt_result",
            "selected_returned_carrier_b_blocked_receipt_result",
            "selected_returned_carrier_b_successful_receipt_result",
            "selected_receipt_alignment_correspondence_result",
            "selected_refusal_visible_correspondence_result",
        ):
            self.assertTrue(selected[key].get("result_id"), key)
        self.assertEqual(selected["selected_current_self_orientation_v7_result"]["outcome"], "SELF_ORIENTED")
        self.assertEqual(selected["selected_current_self_orientation_v6_result"]["outcome"], "SELF_ORIENTED")

        basis = self.result["v7_orientation_basis"]
        self.assertEqual(basis["selected_v7_result_id"], selected["selected_current_self_orientation_v7_result"]["result_id"])
        self.assertEqual(basis["selected_v7_result_path"], selected["selected_current_self_orientation_v7_result"]["result_path"])
        self.assertEqual(basis["selected_v7_outcome"], "SELF_ORIENTED")
        self.assertEqual(basis["selected_v6_result_id"], selected["selected_current_self_orientation_v6_result"]["result_id"])
        self.assertIsInstance(basis["v7_basis_posture"], dict)
        self.assertIsInstance(basis["v7_summary"], dict)
        self.assertTrue(basis["v7_is_conformance_input_not_authority"])

        posture = self.result["recognized_integrated_body_posture"]
        self.assertTrue(posture["v7_body_posture_coherent_as_current_body_mirror"])
        self.assertTrue(posture["current_governing_basis_remains_upstream"])
        self.assertTrue(posture["reentry_body_signal_derivative_vessel_and_operator_surfaces_remain_downstream"])
        self.assertTrue(posture["conformance_closure_correspondence_and_receipt_surfaces_remain_downstream"])
        self.assertTrue(posture["carrier_b_remains_receiving_carrier_evidence_only"])
        self.assertTrue(posture["visible_refusal_evidence_preserved"])
        self.assertTrue(posture["successful_returned_receipt_evidence_preserved"])
        self.assertTrue(posture["returned_evidence_did_not_replace_source"])
        self.assertTrue(posture["returned_evidence_did_not_create_currentness"])

    def test_checks_statement_nonmeaning_open_surfaces_summary_and_non_claims(self) -> None:
        checks = self.result["conformance_checks"]
        self.assertTrue(checks)
        self.assertTrue(all(check["passed"] is True for check in checks))
        self.assertEqual(0, self.result["current_body_conformance_pass_v2_summary"]["failed_check_count"])
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset({check["check_name"] for check in checks}))
        for check in checks:
            self.assertTrue({"check_name", "passed", "expected_posture", "actual_posture", "block_code"}.issubset(check))

        statement = self.result["conformance_statement"]
        for key in (
            "v7_body_posture_conformant",
            "current_governing_basis_remains_upstream",
            "downstream_surfaces_remain_downstream",
            "carrier_b_remained_receiving_carrier_only",
            "returned_receipt_evidence_preserved",
            "refusal_evidence_preserved",
            "no_authority_created",
            "no_permission_created",
            "no_currentness_created",
            "no_source_replaced",
            "no_multi_carrier_law_created",
            "no_distributed_standing_created",
            "no_presence_threshold_truth_action_consequence_created",
            "no_continuation_authorized",
        ):
            self.assertTrue(statement[key], key)

        for key in NON_MEANING_TRUE_KEYS:
            self.assertTrue(self.result["conformance_non_meaning"][key], key)

        self.assertEqual(OPEN_SURFACES, set(self.result["what_remains_open"]))
        for posture in self.result["what_remains_open"].values():
            self.assertTrue(posture["not_scheduled"])
            self.assertTrue(posture["not_authorized"])
            self.assertTrue(posture["not_executed"])

        summary = runner.build_current_body_conformance_pass_v2_summary(self.result)
        self.assertEqual(summary["outcome"], "BODY_CONFORMANT")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        for key in (
            "selected_v7_id",
            "selected_v7_path",
            "selected_v7_outcome",
            "selected_v6_id",
            "selected_previous_conformance_id",
            "selected_post_conformance_closure_id",
            "selected_closure_alignment_correspondence_id",
            "selected_local_receipt_id",
            "selected_returned_carrier_b_blocked_receipt_id",
            "selected_returned_carrier_b_successful_receipt_id",
            "selected_receipt_alignment_correspondence_id",
            "selected_refusal_visible_correspondence_id",
        ):
            self.assertTrue(summary[key], key)
        self.assertEqual(summary["passed_check_count"], len(checks))
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "v7_body_posture_conformant",
            "current_governing_basis_upstream",
            "downstream_surfaces_downstream",
            "carrier_b_receiving_only",
            "returned_evidence_preserved",
            "refusal_evidence_preserved",
            "no_authority_permission_currentness_source_replacement",
            "no_multi_carrier_law_or_distributed_standing",
            "no_presence_threshold_truth_action_consequence",
            "no_continuation",
        ):
            self.assertTrue(summary[key], key)

        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, self.result["non_claims"], key)
            self.assertIs(self.result["non_claims"][key], False, key)
            self.assertIs(summary["key_non_claims"][key], False, key)

    def test_path_write_default_output_and_nonmutation(self) -> None:
        selected = self.result["selected_conformance_inputs"]
        v7_path = selected["selected_current_self_orientation_v7_result"]["result_path"]
        path_result = runner.run_current_body_conformance_pass_v2_from_path(v7_path)
        self.assert_top_level_shape(path_result)
        self.assertEqual(path_result["outcome"], "BODY_CONFORMANT")
        self.assertEqual(path_result["selected_conformance_inputs"]["selected_current_self_orientation_v7_result"]["result_path"], v7_path)
        self.assertFalse(any(path_result["non_claims"][key] for key in FALSE_NON_CLAIMS))

        roots = [
            runner.CURRENT_SELF_ORIENTATION_V7_ROOT,
            runner.CURRENT_SELF_ORIENTATION_V6_ROOT,
            runner.PREVIOUS_CURRENT_BODY_CONFORMANCE_ROOT,
            runner.POST_CONFORMANCE_CLOSURE_ROOT,
            runner.CROSS_SURFACE_CORRESPONDENCE_ROOT,
            runner.CROSS_CARRIER_SURFACE_RECEIPT_ROOT,
            runner.RETURNED_CARRIER_B_RECEIPT_ROOT,
        ]
        before = {root: _snapshot(root) for root in roots}
        runner.run_current_body_conformance_pass_v2()
        after = {root: _snapshot(root) for root in roots}
        self.assertEqual(before, after)

        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "v2_result.json"
            written = runner.write_current_body_conformance_pass_v2_result(self.result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(_read_json(written)))

            with mock.patch.object(runner, "CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT", Path(tmp) / "default"):
                first = runner.write_current_body_conformance_pass_v2_result(self.result)
                second = runner.write_current_body_conformance_pass_v2_result(self.result)
                self.assertNotEqual(first, second)
                self.assertTrue(str(first).startswith(str(Path(tmp) / "default")))
                self.assertTrue(first.name.endswith("__current_body_conformance_pass_v2_result.json"))
                self.assertIn("__current_body_conformance_pass_v2_result_001.json", second.name)

            self.assertEqual(before, {root: _snapshot(root) for root in roots})

    def test_repeated_resolution_does_not_mutate_supplied_mapping(self) -> None:
        v7 = valid_v7()
        original = copy.deepcopy(v7)
        first = runner.run_current_body_conformance_pass_v2(v7)
        second = runner.run_current_body_conformance_pass_v2(v7)
        self.assertEqual(first["outcome"], "BODY_CONFORMANT")
        self.assertEqual(second["outcome"], "BODY_CONFORMANT")
        self.assertEqual(v7, original)


class CurrentBodyConformancePassV2BlockedTests(unittest.TestCase):
    def assert_block(self, v7: dict[str, object] | None, expected: str | set[str]) -> dict:
        result = runner.run_current_body_conformance_pass_v2(v7)
        self.assertEqual(result["outcome"], "BLOCKED")
        code = result["block"]["block_code"]
        if isinstance(expected, set):
            self.assertIn(code, expected)
        else:
            self.assertEqual(code, expected)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, result["non_claims"], key)
        return result

    def test_declared_block_family_and_missing_or_malformed_v7(self) -> None:
        self.assertTrue(
            {
                "CURRENT_SELF_ORIENTATION_V7_MISSING",
                "CURRENT_SELF_ORIENTATION_V7_NOT_SELF_ORIENTED",
                "CURRENT_SELF_ORIENTATION_V7_FAILED_CHECKS_PRESENT",
                "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
                "CURRENT_SELF_ORIENTATION_V6_BASIS_MISSING",
                "CURRENT_BODY_CONFORMANCE_NOT_RECOGNIZED",
                "POST_CONFORMANCE_CLOSURE_NOT_RECOGNIZED",
                "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED",
                "CROSS_CARRIER_RECEIPT_NOT_RECOGNIZED",
                "RETURNED_CARRIER_B_RECEIPT_EVIDENCE_NOT_RECOGNIZED",
                "RETURNED_CARRIER_B_REFUSAL_EVIDENCE_NOT_VISIBLE",
                "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED",
                "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED",
                "CARRIER_B_RECEIVING_ONLY_POSTURE_FAILED",
                "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_SUCCESSOR_BODY_COLLAPSE",
                "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION",
                "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION",
                "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION",
                "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR",
                "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE",
                "MULTI_CARRIER_LAW_CREATED",
                "DISTRIBUTED_STANDING_CREATED",
                "LATEST_FILE_CURRENTNESS_REFUSED",
                "MUTATION_REPLAY_OR_MERGE_DETECTED",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            }.issubset(runner.BLOCK_REASONS)
        )

        with tempfile.TemporaryDirectory() as tmp:
            empty = Path(tmp) / "v7"
            empty.mkdir()
            with mock.patch.object(runner, "CURRENT_SELF_ORIENTATION_V7_ROOT", empty):
                result = runner.run_current_body_conformance_pass_v2()
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V7_MISSING")

        with tempfile.TemporaryDirectory() as tmp:
            malformed = Path(tmp) / "malformed.json"
            malformed.write_text("{", encoding="utf-8")
            result = runner.run_current_body_conformance_pass_v2_from_path(malformed)
            self.assertEqual(result["outcome"], "BLOCKED")
            self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V7_MALFORMED")

            array_path = Path(tmp) / "array.json"
            _write_json(array_path, [])
            result = runner.run_current_body_conformance_pass_v2_from_path(array_path)
            self.assertEqual(result["outcome"], "BLOCKED")
            self.assertEqual(result["block"]["block_code"], "CURRENT_SELF_ORIENTATION_V7_MALFORMED")

    def test_blocks_for_v7_outcome_failed_checks_basis_and_required_recognition(self) -> None:
        v7 = valid_v7(outcome="BLOCKED", block={"block_code": "SYNTHETIC", "block_reason": "blocked"})
        self.assert_block(v7, "CURRENT_SELF_ORIENTATION_V7_NOT_SELF_ORIENTED")

        v7 = valid_v7()
        v7["current_self_orientation_summary"]["failed_check_count"] = 1
        self.assert_block(v7, "CURRENT_SELF_ORIENTATION_V7_FAILED_CHECKS_PRESENT")

        v7 = valid_v7()
        v7["current_self_orientation_summary"]["current_governing_basis_recognized"] = False
        self.assert_block(v7, "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED")

        v7 = valid_v7()
        v7["selected_orientation_inputs"]["selected_current_self_orientation_v6_result"] = {}
        self.assert_block(v7, "CURRENT_SELF_ORIENTATION_V6_BASIS_MISSING")

        cases = (
            ("current_body_conformance_recognized", "CURRENT_BODY_CONFORMANCE_NOT_RECOGNIZED"),
            ("post_conformance_closure_recognized", "POST_CONFORMANCE_CLOSURE_NOT_RECOGNIZED"),
            ("cross_surface_correspondence_recognized", "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED"),
            ("cross_carrier_receipt_recognized", "CROSS_CARRIER_RECEIPT_NOT_RECOGNIZED"),
            ("carrier_b_returned_receipt_evidence_recognized", "RETURNED_CARRIER_B_RECEIPT_EVIDENCE_NOT_RECOGNIZED"),
            ("carrier_b_refusal_evidence_remains_visible", "RETURNED_CARRIER_B_REFUSAL_EVIDENCE_NOT_VISIBLE"),
            ("receipt_alignment_correspondence_recognized", "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED"),
            ("refusal_visible_correspondence_recognized", "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED"),
        )
        for flag, code in cases:
            with self.subTest(flag=flag):
                v7 = valid_v7()
                v7["current_self_orientation_summary"][flag] = False
                self.assert_block(v7, code)

    def test_blocks_when_selected_ids_for_required_surfaces_are_missing(self) -> None:
        cases = (
            ("selected_current_body_conformance_result", "CURRENT_BODY_CONFORMANCE_NOT_RECOGNIZED"),
            ("selected_post_conformance_closure_result", "POST_CONFORMANCE_CLOSURE_NOT_RECOGNIZED"),
            ("selected_local_cross_carrier_receipt_result", "CROSS_CARRIER_RECEIPT_NOT_RECOGNIZED"),
            ("selected_returned_carrier_b_successful_receipt_result", "RETURNED_CARRIER_B_RECEIPT_EVIDENCE_NOT_RECOGNIZED"),
            ("selected_returned_carrier_b_blocked_receipt_result", "RETURNED_CARRIER_B_REFUSAL_EVIDENCE_NOT_VISIBLE"),
            ("selected_receipt_alignment_correspondence_result", "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED"),
            ("selected_refusal_visible_correspondence_result", "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED"),
        )
        for selected_key, code in cases:
            with self.subTest(selected_key=selected_key):
                v7 = valid_v7()
                v7["selected_orientation_inputs"][selected_key] = {}
                self.assert_block(v7, code)

    def test_blocks_for_downstream_carrier_and_source_collapse(self) -> None:
        for basis_key, code in (
            ("conformance_surfaces_remain_downstream_audit_only", "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION"),
            ("closure_surfaces_remain_downstream_meaning_closure_only", "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION"),
            ("correspondence_surfaces_remain_bounded_reading_relation_only", "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ("receipt_surfaces_remain_carried_evidence_only", "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ("carrier_b_remains_receiving_carrier_only", "CARRIER_B_RECEIVING_ONLY_POSTURE_FAILED"),
        ):
            with self.subTest(basis_key=basis_key):
                v7 = valid_v7()
                v7["self_orientation_basis"][basis_key] = False
                self.assert_block(v7, code)

        v7 = valid_v7()
        v7["current_self_orientation_summary"]["carrier_b_remained_receiving_carrier_only"] = False
        self.assert_block(v7, "CARRIER_B_RECEIVING_ONLY_POSTURE_FAILED")

        v7 = valid_v7()
        v7["current_self_orientation_summary"][
            "source_currentness_authority_permission_successor_body_collapse_stayed_false"
        ] = False
        self.assert_block(v7, "SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_SUCCESSOR_BODY_COLLAPSE")

    def test_blocks_for_conformance_closure_correspondence_and_receipt_leaks(self) -> None:
        leak_cases = (
            ({"conformance_became_authority": True}, "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION"),
            ({"conformance_became_permission": True}, "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION"),
            ({"conformance_became_currentness": True}, "CONFORMANCE_LEAKED_AUTHORITY_OR_PERMISSION"),
            ({"closure_became_authority": True}, "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION"),
            ({"closure_became_permission": True}, "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION"),
            ({"closure_became_signal": True}, "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION"),
            ({"closure_authorized_next_work": True}, "CLOSURE_LEAKED_AUTHORITY_PERMISSION_SIGNAL_OR_CONTINUATION"),
            ({"correspondence_became_authority": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_currentness": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_permission": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_signal": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_presence": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_threshold": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_truth": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_action": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"correspondence_became_consequence": True}, "CORRESPONDENCE_LEAKED_AUTHORITY_CURRENTNESS_PERMISSION_SIGNAL_OR_ACTION"),
            ({"receipt_became_source": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"receipt_became_currentness": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"receipt_became_authority": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"receipt_became_permission": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"receiving_carrier_became_successor": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"receiving_carrier_became_body": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"carried_surface_became_source": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"carried_surface_became_currentness": True}, "RECEIPT_LEAKED_SOURCE_CURRENTNESS_AUTHORITY_PERMISSION_OR_SUCCESSOR"),
            ({"carried_surface_became_signal_by_default": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"signal_created_by_default": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"presence_established": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"threshold_met": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"truth_created": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"action_authorized": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
            ({"consequence_created": True}, "RECEIPT_LEAKED_SIGNAL_PRESENCE_THRESHOLD_TRUTH_ACTION_OR_CONSEQUENCE"),
        )
        for claims, code in leak_cases:
            with self.subTest(claims=claims):
                v7 = valid_v7(non_claims=_non_claims(**claims))
                result = self.assert_block(v7, code)
                for key, value in claims.items():
                    self.assertIs(result["non_claims"][key], value, key)

    def test_blocks_for_multi_carrier_distributed_latest_mutation_and_non_claim_flips(self) -> None:
        cases = (
            ({"multi_carrier_law_created": True}, "MULTI_CARRIER_LAW_CREATED"),
            ({"distributed_standing_created": True}, "DISTRIBUTED_STANDING_CREATED"),
            ({"latest_file_currentness": True}, "LATEST_FILE_CURRENTNESS_REFUSED"),
            ({"recency_fraud": True}, "LATEST_FILE_CURRENTNESS_REFUSED"),
            ({"mutation_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"replay_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"merge_performed": True}, "MUTATION_REPLAY_OR_MERGE_DETECTED"),
            ({"follow_on_steps_authorized": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"follow_on_work_authorized": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"self_orientation_successor_forced": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"conformance_successor_forced": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
            ({"authority_created": True}, "NON_CLAIM_MISSING_OR_FLIPPED"),
        )
        for claims, code in cases:
            with self.subTest(claims=claims):
                v7 = valid_v7(non_claims=_non_claims(**claims))
                result = self.assert_block(v7, code)
                for key, value in claims.items():
                    self.assertIs(result["non_claims"][key], value, key)


if __name__ == "__main__":
    unittest.main()
