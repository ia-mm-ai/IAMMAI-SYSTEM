"""Tests for post-conformance standing closure.

This suite audits one closure recorder. It verifies that BODY_CONFORMANT can be
recorded as bounded closure without becoming authority, permission, currentness,
signal, presence, threshold, truth, action, completion, or continuation.
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

import resolve_current_body_standing_closure_post_conformance as resolver


TOP_LEVEL_SECTIONS = {
    "conformance_closure_metadata",
    "selected_self_orientation_v6_basis",
    "selected_current_body_conformance_basis",
    "closure_checks",
    "closure_statement",
    "what_conformance_means",
    "what_conformance_does_not_mean",
    "what_remains_open",
    "outcome",
    "block",
    "current_body_standing_closure_summary",
    "non_claims",
}

SOURCE_NON_CLAIM_KEYS = [
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "source_derivative_operator_collapsed",
]

RESULT_NON_CLAIM_KEYS = SOURCE_NON_CLAIM_KEYS + [
    "conformance_became_authority",
    "conformance_became_permission",
    "conformance_became_currentness",
    "conformance_became_presence",
    "conformance_became_threshold",
    "conformance_became_truth",
    "conformance_became_action",
    "conformance_became_completion",
    "conformance_authorized_next_step",
    "conformance_became_signal_by_default",
    "self_orientation_successor_forced",
]

EXPECTED_CHECK_NAMES = {
    "self_orientation_v6_exists",
    "self_orientation_v6_is_self_oriented",
    "current_body_conformance_exists",
    "current_body_conformance_is_body_conformant",
    "conformance_has_zero_failed_checks",
    "selected_v6_matches_conformance_selected_v6_basis",
    "conformance_current_governing_basis_passed",
    "conformance_reentry_posture_passed",
    "conformance_body_signal_posture_passed",
    "conformance_derivative_vessel_posture_passed",
    "conformance_operator_posture_passed",
    "integrated_non_claims_passed",
    "conformance_is_not_treated_as_authority",
    "conformance_is_not_treated_as_permission",
    "conformance_is_not_treated_as_currentness_creation",
    "conformance_is_not_treated_as_presence",
    "conformance_is_not_treated_as_threshold",
    "conformance_is_not_treated_as_truth",
    "conformance_is_not_treated_as_action",
    "conformance_is_not_treated_as_final_completion",
    "conformance_is_not_treated_as_next_step_authorization",
    "conformance_is_not_treated_as_signal_by_default",
    "conformance_does_not_force_self_orientation_successor",
    "source_derivative_operator_collapse_remains_false",
    "latest_file_currentness_remains_false",
    "mutation_replay_merge_remain_false",
}

V6_ID = "current_self_orientation_v6_self_oriented_test_001"
V6_PATH = "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6/test_v6.json"
CONFORMANCE_ID = "current_body_conformance_body_conformant_test_001"
CONFORMANCE_PATH = (
    "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass/"
    "test_conformance.json"
)


def _write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")


def _read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    assert isinstance(value, dict)
    return value


def _false_non_claims(**updates: bool) -> dict[str, bool]:
    claims = {key: False for key in RESULT_NON_CLAIM_KEYS}
    claims.update(updates)
    return claims


def _deep_update(target: dict, updates: dict[str, object] | None) -> dict:
    copied = copy.deepcopy(target)
    if not updates:
        return copied
    for key, value in updates.items():
        if isinstance(value, dict) and isinstance(copied.get(key), dict):
            copied[key] = _deep_update(copied[key], value)
        else:
            copied[key] = value
    return copied


def _valid_v6_result(**updates: object) -> dict:
    result = {
        "current_self_orientation_v6_metadata": {
            "self_orientation_result_id": V6_ID,
            "self_orientation_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V6_RESULT"
            ),
            "self_orientation_result_version": "0.6.0",
            "generated_at": "2026-04-27T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v6",
            "successor_of_module": "resolve_current_self_orientation_v5",
        },
        "selected_orientation_inputs": {
            "selected_body_pass_result": {
                "result_id": "body_pass_confirmed_test_001",
                "result_path": "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/test.json",
                "outcome": "V0_BODY_PASS_CONFIRMED",
            },
            "selected_source_surface": {
                "result_id": "source_surface_test_001",
                "result_path": "artifacts/current_state/source_surface_test.json",
                "result_family": "current_state_what_stands_now_result",
                "outcome": "ANSWERED_WHAT_STANDS_NOW",
            },
            "selected_reentry_admissibility_result": {
                "result_id": "reentry_admissibility_admitted_test_001",
                "outcome": "REENTRY_ADMITTED",
            },
            "selected_reentry_receipt_result": {
                "result_id": "reentry_receipt_received_test_001",
                "outcome": "REENTRY_RECEIVED",
            },
            "selected_body_signal_recognition_result": {
                "result_id": "body_signal_recognition_signal_recognized_test_001",
                "outcome": "SIGNAL_RECOGNIZED",
            },
            "selected_body_signal_acceptance_result": {
                "result_id": "body_signal_acceptance_signal_accepted_test_001",
                "outcome": "SIGNAL_ACCEPTED",
            },
            "selected_body_signal_scope_result": {
                "result_id": "body_signal_scope_signal_scoped_test_001",
                "outcome": "SIGNAL_SCOPED",
            },
            "selected_derivative_vessel_relation_boundary_result": {
                "result_id": "derivative_vessel_relation_boundary_recognized_test_001",
                "outcome": "DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
            },
        },
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "non_claims": _false_non_claims(),
    }
    return _deep_update(result, updates)


def _valid_conformance_result(
    *,
    selected_v6_id: str = V6_ID,
    selected_v6_path: str = V6_PATH,
    outcome: str = "BODY_CONFORMANT",
    failed_check_count: int = 0,
    summary_updates: dict[str, object] | None = None,
    non_claim_updates: dict[str, bool] | None = None,
    include_all_required_non_claims: bool = True,
) -> dict:
    claims = _false_non_claims(**(non_claim_updates or {}))
    if not include_all_required_non_claims:
        claims.pop("authority_created", None)
    summary = {
        "outcome": outcome,
        "block_code": None,
        "block_reason": None,
        "selected_self_orientation_v6_id": selected_v6_id,
        "selected_self_orientation_v6_path": selected_v6_path,
        "selected_self_orientation_v6_outcome": "SELF_ORIENTED",
        "failed_check_count": failed_check_count,
        "current_governing_basis_passed": True,
        "reentry_posture_passed": True,
        "body_signal_posture_passed": True,
        "derivative_vessel_posture_passed": True,
        "operator_posture_passed": True,
        "integrated_non_claims_passed": True,
        "key_non_claims": copy.deepcopy(claims),
    }
    if summary_updates:
        summary = _deep_update(summary, summary_updates)
    result = {
        "current_body_conformance_metadata": {
            "current_body_conformance_result_id": CONFORMANCE_ID,
            "current_body_conformance_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_BODY_CONFORMANCE_RESULT"
            ),
            "current_body_conformance_result_version": "0.1.0",
            "generated_at": "2026-04-27T00:00:00Z",
            "runner_module": "run_integrity_host_v0_min_coexistence_current_body_conformance_pass",
        },
        "selected_conformance_inputs": {
            "selected_self_orientation_v6_result": {
                "result_id": selected_v6_id,
                "result_path": selected_v6_path,
                "outcome": "SELF_ORIENTED",
            },
            "selected_reentry_admissibility_result": {
                "result_id": "reentry_admissibility_admitted_test_001",
                "outcome": "REENTRY_ADMITTED",
            },
            "selected_reentry_receipt_result": {
                "result_id": "reentry_receipt_received_test_001",
                "outcome": "REENTRY_RECEIVED",
            },
            "selected_body_signal_recognition_result": {
                "result_id": "body_signal_recognition_signal_recognized_test_001",
                "outcome": "SIGNAL_RECOGNIZED",
            },
            "selected_body_signal_acceptance_result": {
                "result_id": "body_signal_acceptance_signal_accepted_test_001",
                "outcome": "SIGNAL_ACCEPTED",
            },
            "selected_body_signal_scope_result": {
                "result_id": "body_signal_scope_signal_scoped_test_001",
                "outcome": "SIGNAL_SCOPED",
            },
            "selected_derivative_vessel_relation_boundary_result": {
                "result_id": "derivative_vessel_relation_boundary_recognized_test_001",
                "outcome": "DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
            },
        },
        "current_body_conformance_basis": {
            "selected_self_orientation_v6_result_id": selected_v6_id,
            "selected_self_orientation_v6_result_path": selected_v6_path,
            "selected_self_orientation_v6_outcome": "SELF_ORIENTED",
        },
        "current_body_conformance_summary": summary,
        "current_body_conformance_checks": [
            {
                "check_name": "self_orientation_v6_is_self_oriented",
                "passed": failed_check_count == 0,
                "expected_posture": "SELF_ORIENTED",
                "actual_posture": "SELF_ORIENTED",
                "block_code": None if failed_check_count == 0 else "TEST_FAILED_CHECK",
            }
        ],
        "integrated_non_claims": {
            "all_required_non_claims_false": True,
            "false_non_claims": copy.deepcopy(claims),
        },
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None},
        "non_claims": copy.deepcopy(claims),
    }
    if not include_all_required_non_claims:
        for container in (
            result["non_claims"],
            result["integrated_non_claims"]["false_non_claims"],
            result["current_body_conformance_summary"]["key_non_claims"],
        ):
            container.pop("authority_created", None)
    return result


class CurrentBodyStandingClosurePostConformanceTests(unittest.TestCase):
    def _resolve_valid(self) -> dict:
        return resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(),
        )

    def assert_blocked(self, result: dict, block_code: str) -> None:
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], block_code)
        self.assertIn("non_claims", result)

    def test_successful_mapping_based_closure(self) -> None:
        result = self._resolve_valid()

        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertEqual(result["outcome"], "CONFORMANCE_CLOSURE_RECORDED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(
            result["closure_statement"],
            {
                "conformance_question_closed": True,
                "next_work_question_opened": False,
                "conformance_recorded_as_permission": False,
                "conformance_recorded_as_authority": False,
                "conformance_recorded_as_signal": False,
                "self_orientation_successor_forced": False,
            },
        )

    def test_metadata(self) -> None:
        metadata = self._resolve_valid()["conformance_closure_metadata"]

        self.assertTrue(metadata["conformance_closure_result_id"])
        self.assertTrue(metadata["conformance_closure_result_type"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(metadata["conformance_closure_result_version"], "0.1.0")
        self.assertEqual(
            metadata["resolver_module"],
            "resolve_current_body_standing_closure_post_conformance",
        )

    def test_selected_bases_preserve_identity_and_posture(self) -> None:
        result = self._resolve_valid()
        selected_v6 = result["selected_self_orientation_v6_basis"]
        selected_conformance = result["selected_current_body_conformance_basis"]

        self.assertEqual(selected_v6["self_orientation_result_id"], V6_ID)
        self.assertEqual(selected_v6["outcome"], "SELF_ORIENTED")
        self.assertEqual(selected_v6["selection_mode"], "provided_mapping")
        self.assertEqual(selected_conformance["current_body_conformance_result_id"], CONFORMANCE_ID)
        self.assertEqual(selected_conformance["outcome"], "BODY_CONFORMANT")
        self.assertEqual(selected_conformance["failed_check_count"], 0)
        self.assertEqual(selected_conformance["selected_self_orientation_v6_result_id"], V6_ID)
        self.assertEqual(selected_conformance["selected_self_orientation_v6_result_path"], V6_PATH)
        self.assertEqual(selected_conformance["selected_self_orientation_v6_outcome"], "SELF_ORIENTED")
        self.assertTrue(selected_conformance["current_governing_basis_passed"])
        self.assertTrue(selected_conformance["reentry_posture_passed"])
        self.assertTrue(selected_conformance["body_signal_posture_passed"])
        self.assertTrue(selected_conformance["derivative_vessel_posture_passed"])
        self.assertTrue(selected_conformance["operator_posture_passed"])
        self.assertTrue(selected_conformance["integrated_non_claims_passed"])

    def test_meaning_non_meaning_and_open_surfaces(self) -> None:
        result = self._resolve_valid()

        for key in [
            "selected_current_body_surfaces_cohere_under_conformance_pass",
            "current_governing_basis_is_upstream_derived",
            "downstream_surfaces_remain_downstream",
            "reentry_posture_remains_closed_and_non_reusable",
            "body_signal_posture_remains_non_operative",
            "derivative_vessel_relation_posture_remains_downstream_and_non_authoritative",
            "operator_facing_posture_remains_downstream_where_present",
            "source_derivative_operator_collapse_did_not_occur",
            "checked_non_claims_remain_false",
        ]:
            self.assertIs(result["what_conformance_means"][key], True)

        for key in [
            "does_not_create_authority",
            "does_not_create_permission",
            "does_not_create_currentness",
            "does_not_authorize_next_step",
            "does_not_authorize_follow_on_work",
            "does_not_create_reusable_admission",
            "does_not_replace_source",
            "does_not_establish_presence",
            "does_not_establish_threshold",
            "does_not_create_truth",
            "does_not_authorize_action",
            "does_not_create_consequence",
            "does_not_complete_continuity",
            "does_not_complete_final_governance",
            "does_not_complete_final_system_identity",
            "does_not_create_generalized_vessel_permission",
            "does_not_create_body_relevance_medium",
            "does_not_create_signal_routing",
            "does_not_create_workflow",
            "does_not_create_roadmap",
            "does_not_complete_the_whole_body",
            "does_not_become_signal_by_default",
            "does_not_force_self_orientation_successor",
        ]:
            self.assertIs(result["what_conformance_does_not_mean"][key], True)

        open_posture = result["what_remains_open"]
        for surface in [
            "presence law",
            "threshold law",
            "truth law",
            "action/consequence law",
            "multi-carrier relation law",
            "persistence/registry law",
            "generalized vessel relation lifecycle",
            "body relevance medium",
            "further external contact surfaces",
            "future signal series or accumulation logic",
            "future self-orientation successor only if a new surface materially changes current posture",
        ]:
            self.assertIn(surface, open_posture["open_surfaces"])
        self.assertTrue(open_posture["open_means_not_scheduled"])
        self.assertTrue(open_posture["open_means_not_authorized"])
        self.assertTrue(open_posture["open_means_not_executed"])

    def test_closure_checks_are_explicit_and_pass_for_valid_case(self) -> None:
        checks = self._resolve_valid()["closure_checks"]
        names = {check["check_name"] for check in checks}

        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(names))
        for check in checks:
            self.assertTrue({"check_name", "passed", "expected_posture", "actual_posture", "block_code"}.issubset(check))
            self.assertIs(check["passed"], True)
            self.assertIsNone(check["block_code"])

    def test_summary_helper(self) -> None:
        result = self._resolve_valid()
        summary = resolver.build_current_body_standing_closure_summary(result)

        self.assertEqual(summary["outcome"], "CONFORMANCE_CLOSURE_RECORDED")
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(summary["selected_self_orientation_v6_id"], V6_ID)
        self.assertEqual(summary["selected_self_orientation_v6_outcome"], "SELF_ORIENTED")
        self.assertEqual(summary["selected_conformance_id"], CONFORMANCE_ID)
        self.assertEqual(summary["selected_conformance_outcome"], "BODY_CONFORMANT")
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["conformance_closure_recorded"])
        self.assertTrue(summary["conformance_question_closed"])
        self.assertFalse(summary["next_work_question_opened"])
        self.assertFalse(summary["conformance_recorded_as_permission"])
        self.assertFalse(summary["conformance_recorded_as_authority"])
        self.assertFalse(summary["conformance_recorded_as_signal"])
        self.assertFalse(summary["self_orientation_successor_forced"])
        for key in [
            "authority_created",
            "permission_created",
            "currentness_created",
            "continuity_completed",
            "final_governance_completed",
            "final_system_identity_completed",
            "source_replaced",
            "follow_on_steps_authorized",
            "follow_on_work_authorized",
            "latest_file_currentness",
            "recency_fraud",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "source_derivative_operator_collapsed",
            "conformance_became_authority",
            "conformance_became_permission",
            "conformance_became_currentness",
            "conformance_became_presence",
            "conformance_became_threshold",
            "conformance_became_truth",
            "conformance_became_action",
            "conformance_became_completion",
            "conformance_authorized_next_step",
            "conformance_became_signal_by_default",
            "self_orientation_successor_forced",
        ]:
            self.assertIn(key, summary["key_non_claims"])

    def test_path_based_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            v6_path = root / "v6.json"
            conformance_path = root / "conformance.json"
            v6 = _valid_v6_result()
            conformance = _valid_conformance_result(selected_v6_path=str(v6_path))
            _write_json(v6_path, v6)
            _write_json(conformance_path, conformance)

            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                v6_path,
                conformance_path,
            )

        self.assertEqual(result["outcome"], "CONFORMANCE_CLOSURE_RECORDED")
        self.assertEqual(result["selected_self_orientation_v6_basis"]["result_path"], str(v6_path))
        self.assertEqual(
            result["selected_current_body_conformance_basis"]["result_path"],
            str(conformance_path),
        )
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))

    def test_write_behavior(self) -> None:
        result = self._resolve_valid()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "closure.json"
            written = resolver.write_current_body_standing_closure_result(result, output_path)
            self.assertTrue(written.exists())
            loaded = _read_json(written)

        self.assertEqual(written, output_path)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(loaded))
        self.assertEqual(loaded["outcome"], "CONFORMANCE_CLOSURE_RECORDED")

    def test_default_output_path_is_bounded_and_additive(self) -> None:
        result = self._resolve_valid()
        with tempfile.TemporaryDirectory() as tmp:
            patched_root = Path(tmp) / "closure_root"
            with mock.patch.object(
                resolver,
                "CURRENT_BODY_STANDING_CLOSURE_POST_CONFORMANCE_ROOT",
                patched_root,
            ):
                first = resolver.write_current_body_standing_closure_result(result)
                second = resolver.write_current_body_standing_closure_result(result)

            self.assertEqual(first.parent, patched_root)
            self.assertEqual(second.parent, patched_root)
            self.assertNotEqual(first, second)
            self.assertIn(CONFORMANCE_ID, first.name)
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        v6 = _valid_v6_result()
        conformance = _valid_conformance_result()
        original_v6 = copy.deepcopy(v6)
        original_conformance = copy.deepcopy(conformance)

        first = resolver.resolve_current_body_standing_closure_post_conformance(v6, conformance)
        second = resolver.resolve_current_body_standing_closure_post_conformance(v6, conformance)

        self.assertEqual(v6, original_v6)
        self.assertEqual(conformance, original_conformance)
        self.assertEqual(first["outcome"], second["outcome"])
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "closure.json"
            resolver.write_current_body_standing_closure_result(first, output)
            self.assertEqual([path.name for path in Path(tmp).iterdir()], ["closure.json"])

    def test_missing_v6_blocks_when_discovery_has_no_v6(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V6_ROOT", Path(tmp)):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    None,
                    _valid_conformance_result(),
                )

        self.assert_blocked(result, "SELF_ORIENTATION_V6_MISSING")

    def test_missing_conformance_blocks_when_discovery_has_no_conformance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(resolver, "CURRENT_BODY_CONFORMANCE_ROOT", Path(tmp)):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    None,
                )

        self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_MISSING")

    def test_v6_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            missing = root / "missing.json"
            valid_conformance = root / "conformance.json"
            _write_json(valid_conformance, _valid_conformance_result(selected_v6_path=str(missing)))

            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                missing,
                valid_conformance,
            )
            self.assert_blocked(result, "SELF_ORIENTATION_V6_UNREADABLE")

            malformed = root / "malformed.json"
            malformed.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                malformed,
                valid_conformance,
            )
            self.assert_blocked(result, "SELF_ORIENTATION_V6_MALFORMED")

            array_path = root / "array.json"
            array_path.write_text("[]\n", encoding="utf-8")
            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                array_path,
                valid_conformance,
            )
            self.assert_blocked(result, "SELF_ORIENTATION_V6_MALFORMED")

    def test_conformance_path_unreadable_or_malformed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            v6_path = root / "v6.json"
            _write_json(v6_path, _valid_v6_result())

            missing = root / "missing_conformance.json"
            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                v6_path,
                missing,
            )
            self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_UNREADABLE")

            malformed = root / "malformed_conformance.json"
            malformed.write_text("{not-json", encoding="utf-8")
            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                v6_path,
                malformed,
            )
            self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_MALFORMED")

            array_path = root / "array_conformance.json"
            array_path.write_text("[]\n", encoding="utf-8")
            result = resolver.resolve_current_body_standing_closure_post_conformance_from_paths(
                v6_path,
                array_path,
            )
            self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_MALFORMED")

    def test_v6_not_self_oriented_blocks(self) -> None:
        result = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(outcome="BLOCKED"),
            _valid_conformance_result(),
        )

        self.assert_blocked(result, "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED")

    def test_conformance_not_body_conformant_blocks(self) -> None:
        result = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(outcome="BLOCKED"),
        )

        self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT")

    def test_conformance_failed_checks_present_blocks(self) -> None:
        result = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(failed_check_count=1),
        )

        self.assert_blocked(result, "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT")

    def test_v6_conformance_basis_mismatch_blocks(self) -> None:
        result = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(selected_v6_id="different-v6-id"),
        )

        self.assert_blocked(result, "SELF_ORIENTATION_V6_CONFORMANCE_BASIS_MISMATCH")

    def test_integrated_posture_flag_flips_block(self) -> None:
        for flag in [
            "current_governing_basis_passed",
            "reentry_posture_passed",
            "body_signal_posture_passed",
            "derivative_vessel_posture_passed",
            "operator_posture_passed",
            "integrated_non_claims_passed",
        ]:
            with self.subTest(flag=flag):
                conformance = _valid_conformance_result(summary_updates={flag: False})
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    conformance,
                )
                self.assertEqual(result["outcome"], "BLOCKED")
                self.assertIn(
                    result["block"]["block_code"],
                    {
                        "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
                        "INTEGRATED_NON_CLAIM_MISSING_OR_FLIPPED",
                    },
                )

    def test_conformance_authority_permission_currentness_leaks_block(self) -> None:
        cases = [
            ("conformance_became_authority", "CONFORMANCE_TREATED_AS_AUTHORITY"),
            ("authority_created", "CONFORMANCE_TREATED_AS_AUTHORITY"),
            ("conformance_became_permission", "CONFORMANCE_TREATED_AS_PERMISSION"),
            ("permission_created", "CONFORMANCE_TREATED_AS_PERMISSION"),
            ("conformance_became_currentness", "CONFORMANCE_TREATED_AS_CURRENTNESS_CREATION"),
            ("currentness_created", "CONFORMANCE_TREATED_AS_CURRENTNESS_CREATION"),
        ]
        for claim, block_code in cases:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, block_code)

    def test_conformance_presence_threshold_truth_action_leaks_block(self) -> None:
        cases = [
            ("presence_established", "CONFORMANCE_TREATED_AS_PRESENCE"),
            ("conformance_became_presence", "CONFORMANCE_TREATED_AS_PRESENCE"),
            ("threshold_met", "CONFORMANCE_TREATED_AS_THRESHOLD"),
            ("conformance_became_threshold", "CONFORMANCE_TREATED_AS_THRESHOLD"),
            ("truth_created", "CONFORMANCE_TREATED_AS_TRUTH"),
            ("conformance_became_truth", "CONFORMANCE_TREATED_AS_TRUTH"),
            ("action_authorized", "CONFORMANCE_TREATED_AS_ACTION"),
            ("conformance_became_action", "CONFORMANCE_TREATED_AS_ACTION"),
        ]
        for claim, block_code in cases:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, block_code)

    def test_final_completion_leaks_block(self) -> None:
        for claim in [
            "continuity_completed",
            "final_governance_completed",
            "final_system_identity_completed",
            "conformance_became_completion",
        ]:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, "CONFORMANCE_TREATED_AS_FINAL_COMPLETION")

    def test_next_step_authorization_blocks(self) -> None:
        for claim in [
            "follow_on_steps_authorized",
            "follow_on_work_authorized",
            "conformance_authorized_next_step",
        ]:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, "CONFORMANCE_TREATED_AS_NEXT_STEP_AUTHORIZATION")

    def test_signal_by_default_and_forced_successor_block(self) -> None:
        cases = [
            ("conformance_became_signal_by_default", "CONFORMANCE_TREATED_AS_SIGNAL_BY_DEFAULT"),
            ("self_orientation_successor_forced", "CONFORMANCE_FORCES_SELF_ORIENTATION_SUCCESSOR"),
        ]
        for claim, block_code in cases:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, block_code)

    def test_source_derivative_operator_collapse_blocks(self) -> None:
        for claim in [
            "source_replaced",
            "derivative_outputs_upgraded_to_source",
            "operator_outputs_upgraded_to_source",
            "source_derivative_operator_collapsed",
        ]:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE")

    def test_latest_file_currentness_blocks(self) -> None:
        for claim in ["latest_file_currentness", "recency_fraud"]:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, "LATEST_FILE_CURRENTNESS")

    def test_mutation_replay_merge_blocks(self) -> None:
        for claim in ["mutation_performed", "replay_performed", "merge_performed"]:
            with self.subTest(claim=claim):
                result = resolver.resolve_current_body_standing_closure_post_conformance(
                    _valid_v6_result(),
                    _valid_conformance_result(non_claim_updates={claim: True}),
                )
                self.assert_blocked(result, "MUTATION_REPLAY_OR_MERGE_DETECTED")

    def test_missing_integrated_non_claim_blocks(self) -> None:
        result = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(include_all_required_non_claims=False),
        )

        self.assert_blocked(result, "INTEGRATED_NON_CLAIM_MISSING_OR_FLIPPED")

    def test_preserved_non_claims_for_recorded_and_blocked_results(self) -> None:
        recorded = self._resolve_valid()
        blocked = resolver.resolve_current_body_standing_closure_post_conformance(
            _valid_v6_result(),
            _valid_conformance_result(non_claim_updates={"conformance_became_authority": True}),
        )

        for result in [recorded, blocked]:
            for key in RESULT_NON_CLAIM_KEYS:
                self.assertIn(key, result["non_claims"])
            if result["outcome"] == "CONFORMANCE_CLOSURE_RECORDED":
                for key in RESULT_NON_CLAIM_KEYS:
                    self.assertIs(result["non_claims"][key], False)
            else:
                self.assertIs(result["non_claims"]["conformance_became_authority"], True)


if __name__ == "__main__":
    unittest.main()
