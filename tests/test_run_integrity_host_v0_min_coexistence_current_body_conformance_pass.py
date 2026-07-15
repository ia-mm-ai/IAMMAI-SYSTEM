"""Tests for the bounded integrated current-body conformance pass.

This suite audits the runner as one whole-body conformance gate. It does not
exercise new capability, orchestration, signal use, vessel implementation, or
permission surfaces.
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

import run_integrity_host_v0_min_coexistence_current_body_conformance_pass as runner


TOP_LEVEL_SECTIONS = {
    "current_body_conformance_metadata",
    "selected_conformance_inputs",
    "integrated_current_governing_basis",
    "integrated_reentry_posture",
    "integrated_body_signal_posture",
    "integrated_derivative_vessel_posture",
    "integrated_operator_posture",
    "integrated_non_claims",
    "current_body_conformance_checks",
    "outcome",
    "block",
    "current_body_conformance_basis",
    "current_body_conformance_summary",
    "non_claims",
}

FALSE_NON_CLAIM_KEYS = [
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "reentry_admissibility_became_authority",
    "receipt_became_authority",
    "signal_recognition_became_authority",
    "signal_acceptance_became_authority",
    "signal_scope_became_authority",
    "derivative_vessel_relation_became_authority",
    "derivative_vessel_relation_became_currentness",
    "derivative_vessel_relation_became_permission",
    "derivative_vessel_relation_created_adoption",
    "derivative_vessel_relation_created_privileged_standing",
    "derivative_vessel_relation_replaced_source",
    "derivative_vessel_relation_completed_final_governance",
    "derivative_vessel_relation_completed_final_system_identity",
    "derivative_vessel_relation_completed_continuity",
    "derivative_vessel_relation_created_general_vessel_permission",
    "derivative_vessel_relation_authorized_follow_on_vessels",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "roadmap_generated",
    "workflow_engine_created",
    "signal_router_created",
    "event_bus_created",
    "body_relevance_medium_created",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "applied_outside_declared_scope",
    "source_derivative_operator_collapsed",
]


def false_non_claims() -> dict[str, bool]:
    claims = {key: False for key in runner.FALSE_NON_CLAIMS}
    for key in FALSE_NON_CLAIM_KEYS:
        claims[key] = False
    return claims


def valid_v6_artifact() -> dict:
    source_id = "source_surface_current_state_what_stands_now_001"
    v5_id = "current_self_orientation_v5_self_oriented_001"
    derivative_id = "bounded_current_state_read_v3_answered_001"
    relation_id = "derivative_vessel_relation_boundary_live_001"
    v6_id = "current_self_orientation_v6_self_oriented_001"
    claims = false_non_claims()

    return {
        "current_self_orientation_v6_metadata": {
            "self_orientation_result_id": v6_id,
            "self_orientation_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V6_RESULT"
            ),
            "self_orientation_result_version": "0.6.0",
            "generated_at": "2026-04-27T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v6",
            "successor_of_module": "resolve_current_self_orientation_v5",
        },
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "selected_orientation_inputs": {
            "selected_body_pass_result": {
                "result_id": "v0_body_pass_confirmed_001",
                "result_path": "artifacts/integrity_host_v0_min_coexistence_v0_body_pass/v0_body_pass_result.json",
                "result_family": "v0_body_pass_result",
                "outcome": "V0_BODY_PASS_CONFIRMED",
            },
            "selected_self_orientation_v5_result": {
                "result_id": v5_id,
                "result_path": "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v5/current_self_orientation_v5_result.json",
                "outcome": "SELF_ORIENTED",
            },
            "selected_source_surface": {
                "result_id": source_id,
                "result_path": "artifacts/current_state/source_surface.json",
                "result_family": "current_state_what_stands_now_result",
                "outcome": "ANSWERED_WHAT_STANDS_NOW",
            },
            "selected_effective_references": {
                "effective_authority_artifact_path": "artifacts/effective/authority.json",
                "effective_current_governing_packet_path": "artifacts/effective/current_governing.json",
                "effective_source_run_path": "artifacts/source/run",
            },
            "selected_reentry_admissibility_result": {
                "result_id": "reentry_admissibility_admitted_001",
                "result_path": "artifacts/reentry/admissibility.json",
                "outcome": "REENTRY_ADMITTED",
                "resolver_module": "resolve_current_self_orientation_reentry_admissibility",
            },
            "selected_reentry_receipt_result": {
                "result_id": "reentry_receipt_received_001",
                "result_path": "artifacts/reentry/receipt.json",
                "outcome": "REENTRY_RECEIVED",
                "resolver_module": "resolve_current_self_orientation_reentry_receipt",
            },
            "selected_body_signal_recognition_result": {
                "result_id": "body_signal_recognition_v2_signal_recognized_001",
                "result_path": "artifacts/body_signal/recognition.json",
                "outcome": "SIGNAL_RECOGNIZED",
                "recognized_signal_id": "body_pass_signal_recognized_001",
                "recognized_signal_category": "BODY_PASS_SIGNAL",
                "recognized_source_artifact_family": "v0_body_pass_result",
            },
            "selected_blocked_body_signal_recognition_result": {
                "result_id": "body_signal_recognition_v2_blocked_false_permission_001",
                "result_path": "artifacts/body_signal/blocked_false_permission.json",
                "outcome": "BLOCKED",
                "block_code": "SIGNAL_ATTEMPTS_PERMISSION",
            },
            "selected_body_signal_acceptance_result": {
                "result_id": "body_signal_acceptance_signal_accepted_001",
                "result_path": "artifacts/body_signal/acceptance.json",
                "outcome": "SIGNAL_ACCEPTED",
                "accepted_signal_id": "body_pass_signal_accepted_001",
                "accepted_signal_category": "BODY_PASS_SIGNAL",
                "declared_matter_id": "current_signal_recognition_standing",
                "declared_matter_family": "body_signal_acceptance_matter",
                "declared_matter_kind": "recognized_body_signal_posture",
            },
            "selected_body_signal_scope_result": {
                "result_id": "body_signal_scope_signal_scoped_001",
                "result_path": "artifacts/body_signal/scope.json",
                "outcome": "SIGNAL_SCOPED",
                "scoped_signal_id": "body_pass_signal_scoped_001",
                "scoped_signal_category": "BODY_PASS_SIGNAL",
                "accepted_matter_id": "current_signal_recognition_standing",
                "accepted_matter_family": "body_signal_acceptance_matter",
                "accepted_matter_kind": "recognized_body_signal_posture",
                "declared_scope_id": (
                    "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"
                ),
                "declared_scope_family": "body_signal_scope",
                "declared_scope_kind": "nonoperative_body_pass_signal_posture",
            },
            "selected_derivative_vessel_relation_boundary_result": {
                "result_id": "derivative_vessel_relation_boundary_recognized_001",
                "result_path": "artifacts/relation/relation_boundary.json",
                "outcome": "DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
                "relation_id": relation_id,
                "relation_type": "DERIVATIVE_VESSEL_RELATION_DECLARATION",
                "resolver_module": "resolve_derivative_vessel_relation_boundary",
            },
            "selected_blocked_derivative_vessel_relation_boundary_result": {
                "result_id": "derivative_vessel_relation_boundary_blocked_001",
                "result_path": "artifacts/relation/relation_boundary_blocked.json",
                "outcome": "BLOCKED",
                "block_code": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
            },
            "selected_operator_terminal_brief_results": [
                {
                    "result_id": "operator_terminal_brief_rendered_001",
                    "result_path": "artifacts/operator/brief.json",
                    "outcome": "BRIEF_RENDERED",
                    "result_family": "operator_terminal_brief_result",
                    "source_surface_id": source_id,
                    "source_surface_family": "current_state_what_stands_now_result",
                }
            ],
        },
        "recognized_current_executable_core_line": {
            "recognized_from_standing_body_pass": True,
            "selected_source_surface_id": source_id,
        },
        "recognized_governing_effective_basis": {
            "recognized_from_explicit_effective_references": True,
            "current_governing_packet_path": "artifacts/effective/current_governing.json",
        },
        "recognized_current_state_surfaces": {
            "current_state_answer_read_result": {
                "result_id": "current_state_answer_read_001",
                "outcome": "ANSWERED",
                "source_surface_id": source_id,
            }
        },
        "recognized_continuity_surfaces": {
            "continuity_transfer_result": {"outcome": "CONTINUITY_TRANSFERRED"}
        },
        "recognized_derivative_surfaces": {
            "openai_api_derivative_vessel_v3_results": [
                {
                    "result_id": derivative_id,
                    "result_path": "artifacts/derivative/vessel.json",
                    "outcome": "ANSWERED_DERIVATIVE_READ",
                    "result_family": "openai_api_derivative_vessel_bounded_current_state_read_v3_result",
                    "source_surface_id": source_id,
                    "source_surface_family": "current_state_what_stands_now_result",
                }
            ]
        },
        "recognized_operator_facing_surfaces": {
            "operator_terminal_brief_results": [
                {
                    "result_id": "operator_terminal_brief_rendered_001",
                    "outcome": "BRIEF_RENDERED",
                    "source_surface_id": source_id,
                }
            ]
        },
        "recognized_reentry_surfaces": {
            "recognition_posture": "downstream_closed_reentry_cycle_only",
            "closure_posture": {
                "exhaustion_closure_passed": True,
                "admission_reusable": False,
                "follow_on_steps_authorized": False,
                "workflow_lane_created": False,
            },
        },
        "recognized_body_signal_surfaces": {
            "recognition_basis_passed": True,
            "acceptance_basis_passed": True,
            "scope_boundary_passed": True,
            "scope_limits_passed": True,
            "scope_hierarchy_constraints_passed": True,
            "scope_correspondence_requirements_passed": True,
            "scope_non_claims_passed": True,
            "declared_scope": {
                "scope_id": (
                    "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"
                ),
                "scope_family": "body_signal_scope",
                "scope_kind": "nonoperative_body_pass_signal_posture",
            },
            "accepted_signal_remains": {
                "non_authoritative": True,
                "non_permission": True,
                "non_currentness": True,
                "not_present": True,
                "not_threshold": True,
                "not_truth": True,
                "no_action": True,
                "no_routing": True,
                "no_workflow": True,
                "no_body_relevance_medium": True,
                "no_follow_on_work": True,
            },
            "scoped_signal_remains": {
                "non_authoritative": True,
                "non_permission": True,
                "non_currentness": True,
                "not_present": True,
                "not_threshold": True,
                "not_truth": True,
                "no_action": True,
                "no_routing": True,
                "no_workflow": True,
                "no_body_relevance_medium": True,
                "no_follow_on_work": True,
                "no_application_outside_declared_scope": True,
            },
        },
        "recognized_derivative_vessel_relation_surfaces": {
            "recognition_posture": "downstream_derivative_vessel_relation_boundary_only",
            "relation_id": relation_id,
            "downstream": True,
            "additive_only": True,
            "source_preserved": True,
            "derivative_preserved": True,
            "operator_downstream_where_present": True,
            "no_authority": True,
            "no_permission": True,
            "no_currentness": True,
            "no_adoption": True,
            "no_privileged_standing": True,
            "no_public_release": True,
            "no_source_replacement": True,
            "no_final_governance": True,
            "no_final_system_identity": True,
            "no_continuity_completion": True,
            "no_general_vessel_permission": True,
            "no_follow_on_vessel_authorization": True,
            "derivative_vessel_relation_boundary_surfaces_remain_downstream": True,
            "derivative_vessel_relation_boundary_surfaces_remain_non_authoritative": True,
            "recognized_derivative_vessel_relation": {
                "relation_id": relation_id,
                "relation_type": "DERIVATIVE_VESSEL_RELATION_DECLARATION",
                "source_body_basis_id": v5_id,
                "source_body_basis_path": "artifacts/self_orientation/v5.json",
                "source_body_basis_outcome": "SELF_ORIENTED",
                "source_surface_id": source_id,
                "source_surface_path": "artifacts/current_state/source_surface.json",
                "source_surface_outcome": "ANSWERED_WHAT_STANDS_NOW",
                "derivative_vessel_result_id": derivative_id,
                "derivative_vessel_result_path": "artifacts/derivative/vessel.json",
                "derivative_vessel_result_outcome": "ANSWERED_DERIVATIVE_READ",
                "derivative_output_family": "openai_api_derivative_vessel_bounded_current_state_read_v3_result",
                "derivative_output_basis": "bounded_source_payload",
                "downstream": True,
                "additive_only": True,
                "source_preserved": True,
                "derivative_preserved": True,
                "operator_downstream_where_present": True,
                "no_authority": True,
                "no_permission": True,
                "no_currentness": True,
                "no_adoption": True,
                "no_privileged_standing": True,
                "no_public_release": True,
                "no_source_replacement": True,
                "no_final_governance": True,
                "no_final_system_identity": True,
                "no_continuity_completion": True,
                "no_general_vessel_permission": True,
                "no_follow_on_vessel_authorization": True,
            },
            "relation_remains": {
                "downstream": True,
                "source_body_basis_upstream": True,
                "derivative_vessel_result_downstream": True,
                "operator_facing_output_downstream_where_present": True,
                "additive_only": True,
                "source_preserved": True,
                "derivative_preserved": True,
            },
        },
        "recognized_open_surfaces": {},
        "recognized_blocked_or_refused_surfaces": {},
        "recognized_touch_admissibility_surfaces": {},
        "bounded_correspondence_checks": [
            {
                "check_name": "derivative_operator_reentry_signal_and_relation_surfaces_do_not_determine_current_governing_basis",
                "passed": True,
            },
            {
                "check_name": "derivative_vessel_relation_boundary_surface_does_not_determine_current_governing_basis",
                "passed": True,
            },
            {
                "check_name": "body_signal_scope_surface_does_not_determine_current_governing_basis",
                "passed": True,
            },
            {
                "check_name": "body_signal_surfaces_do_not_determine_current_governing_basis",
                "passed": True,
            },
            {
                "check_name": "reentry_surfaces_do_not_determine_current_governing_basis",
                "passed": True,
            },
        ],
        "self_orientation_basis": {
            "basis_kind": "current_self_orientation_v6",
            "does_not_create_authority": True,
        },
        "current_self_orientation_summary": {
            "outcome": "SELF_ORIENTED",
            "selected_self_orientation_v5_result_id": v5_id,
            "selected_derivative_vessel_relation_boundary_id": "derivative_vessel_relation_boundary_recognized_001",
            "current_executable_core_line_recognized": True,
            "governing_effective_basis_recognized": True,
            "current_state_surfaces_recognized": True,
            "continuity_surfaces_recognized": True,
            "derivative_surfaces_recognized": True,
            "operator_surfaces_recognized": True,
            "reentry_surfaces_recognized": True,
            "body_signal_surfaces_recognized": True,
            "derivative_vessel_relation_boundary_recognized": True,
            "source_body_basis_remains_upstream": True,
            "correspondence_checks_passed": True,
            "non_claims": copy.deepcopy(claims),
        },
        "non_claims": claims,
    }


def resolve(v6: dict) -> dict:
    return runner.run_current_body_conformance_pass(v6)


def block_code_for(v6: dict) -> str | None:
    return resolve(v6)["block"]["block_code"]


def set_non_claim(v6: dict, key: str, value: bool = True) -> None:
    v6["non_claims"][key] = value
    v6["current_self_orientation_summary"]["non_claims"][key] = value


def artifact_snapshot(root: Path) -> dict[str, tuple[int, int]]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(REPO_ROOT)): (path.stat().st_size, path.stat().st_mtime_ns)
        for path in root.rglob("*")
        if path.is_file()
    }


class CurrentBodyConformancePassTests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result.keys()))

    def assert_block(self, v6: dict, expected_code: str) -> None:
        result = resolve(v6)
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual(expected_code, result["block"]["block_code"])

    def test_real_body_conformant_path(self) -> None:
        result = runner.run_current_body_conformance_pass()

        self.assertIsInstance(result, dict)
        self.assert_top_level_shape(result)
        self.assertEqual("BODY_CONFORMANT", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        basis = result["current_body_conformance_basis"]
        self.assertEqual("integrated_current_body_conformance_pass", basis["basis_kind"])
        self.assertTrue(basis["does_not_create_authority"])
        self.assertTrue(basis["does_not_create_permission"])
        self.assertTrue(basis["does_not_create_currentness"])
        self.assertTrue(basis["does_not_authorize_follow_on_work"])

    def test_metadata(self) -> None:
        metadata = runner.run_current_body_conformance_pass()["current_body_conformance_metadata"]

        for key in (
            "current_body_conformance_result_id",
            "current_body_conformance_result_type",
            "current_body_conformance_result_version",
            "generated_at",
            "runner_module",
        ):
            self.assertTrue(metadata[key])
        self.assertEqual("0.1.0", metadata["current_body_conformance_result_version"])
        self.assertEqual(
            "run_integrity_host_v0_min_coexistence_current_body_conformance_pass",
            metadata["runner_module"],
        )

    def test_selected_conformance_inputs(self) -> None:
        selected = runner.run_current_body_conformance_pass()["selected_conformance_inputs"]

        self.assertEqual("SELF_ORIENTED", selected["selected_self_orientation_v6_result"]["outcome"])
        self.assertTrue(selected["selected_self_orientation_v6_result"]["result_id"])
        self.assertTrue(selected["selected_self_orientation_v6_result"]["result_path"])
        self.assertTrue(selected["selected_reentry_admissibility_result"]["result_id"])
        self.assertTrue(selected["selected_reentry_receipt_result"]["result_id"])
        self.assertTrue(selected["selected_body_signal_recognition_result"]["result_id"])
        self.assertTrue(selected["selected_body_signal_acceptance_result"]["result_id"])
        self.assertTrue(selected["selected_body_signal_scope_result"]["result_id"])
        self.assertTrue(selected["selected_derivative_vessel_relation_boundary_result"]["result_id"])
        self.assertTrue(selected["selected_derivative_vessel_result"]["result_id"])
        self.assertTrue(selected["selected_operator_terminal_brief_results"][0]["result_id"])
        self.assertTrue(selected["selected_source_surface"]["result_id"])

    def test_integrated_current_governing_basis(self) -> None:
        current = runner.run_current_body_conformance_pass()["integrated_current_governing_basis"]

        self.assertEqual("SELF_ORIENTED", current["self_orientation_v6_outcome"])
        self.assertTrue(current["current_executable_core_line_recognized"])
        self.assertTrue(current["governing_effective_basis_recognized"])
        self.assertTrue(current["current_state_surfaces_recognized"])
        self.assertTrue(current["source_body_basis_remains_upstream"])
        self.assertTrue(current["downstream_surfaces_do_not_determine_current_governing_basis"])
        self.assertFalse(current["latest_file_currentness"])
        self.assertFalse(current["recency_fraud"])

    def test_integrated_reentry_posture(self) -> None:
        reentry = runner.run_current_body_conformance_pass()["integrated_reentry_posture"]

        self.assertEqual("REENTRY_ADMITTED", reentry["admissibility_outcome"])
        self.assertEqual("REENTRY_RECEIVED", reentry["receipt_outcome"])
        self.assertTrue(reentry["recognized_downstream_by_v6"])
        self.assertTrue(reentry["closure_exhaustion_passed"])
        self.assertFalse(reentry["admission_reusable"])
        self.assertFalse(reentry["follow_on_steps_authorized"])
        self.assertFalse(reentry["follow_on_work_authorized"])
        self.assertFalse(reentry["workflow_lane_created"])
        self.assertFalse(reentry["reentry_surfaces_became_authority"])

    def test_integrated_body_signal_posture(self) -> None:
        signal = runner.run_current_body_conformance_pass()["integrated_body_signal_posture"]

        self.assertEqual("SIGNAL_RECOGNIZED", signal["recognition_outcome"])
        self.assertEqual("BLOCKED", signal["blocked_false_permission_signal_outcome"])
        self.assertEqual("SIGNAL_ACCEPTED", signal["acceptance_outcome"])
        self.assertEqual("SIGNAL_SCOPED", signal["scope_outcome"])
        self.assertEqual("current_signal_recognition_standing", signal["accepted_matter_id"])
        self.assertEqual(
            "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope",
            signal["declared_scope_id"],
        )
        self.assertTrue(signal["recognized_downstream_by_v6"])
        self.assertTrue(signal["accepted_signal_remains_non_operative"])
        self.assertTrue(signal["scoped_signal_remains_non_operative"])
        self.assertTrue(signal["signal_line_remains_non_authoritative_non_permission_no_action"])
        self.assertTrue(signal["signal_line_remains_non_operative"])
        self.assertTrue(signal["scoped_signal_applies_only_inside_declared_scope"])
        self.assertTrue(signal["signal_surfaces_did_not_become_current_governing_basis"])

    def test_integrated_derivative_vessel_posture(self) -> None:
        posture = runner.run_current_body_conformance_pass()["integrated_derivative_vessel_posture"]

        self.assertEqual("DERIVATIVE_VESSEL_RELATION_RECOGNIZED", posture["relation_boundary_outcome"])
        self.assertEqual("BLOCKED", posture["blocked_relation_boundary_outcome"])
        self.assertTrue(posture["blocked_relation_boundary_code"])
        self.assertTrue(posture["recognized_downstream_by_v6"])
        self.assertTrue(posture["relation_remains_downstream"])
        self.assertTrue(posture["source_body_basis_remains_upstream"])
        self.assertTrue(posture["derivative_vessel_result_remains_downstream"])
        self.assertTrue(posture["relation_remains_additive_only"])
        self.assertTrue(posture["relation_creates_no_authority"])
        self.assertTrue(posture["relation_creates_no_permission"])
        self.assertTrue(posture["relation_creates_no_currentness"])
        self.assertTrue(posture["relation_creates_no_adoption"])
        self.assertTrue(posture["relation_creates_no_privileged_standing"])
        self.assertTrue(posture["relation_replaces_no_source"])
        self.assertTrue(posture["relation_completes_no_final_governance"])
        self.assertTrue(posture["relation_completes_no_final_system_identity"])
        self.assertTrue(posture["relation_completes_no_continuity"])
        self.assertTrue(posture["relation_creates_no_general_vessel_permission"])
        self.assertTrue(posture["relation_authorizes_no_follow_on_vessels"])
        self.assertTrue(posture["relation_boundary_did_not_become_current_governing_basis"])

    def test_integrated_operator_posture(self) -> None:
        operator = runner.run_current_body_conformance_pass()["integrated_operator_posture"]

        self.assertGreaterEqual(operator["operator_facing_success_count"], 1)
        self.assertTrue(operator["recognized_downstream_by_v6"])
        self.assertFalse(operator["operator_output_became_source"])
        self.assertFalse(operator["operator_output_became_authority"])
        self.assertFalse(operator["operator_output_became_currentness"])
        self.assertFalse(operator["operator_output_became_permission"])

    def test_integrated_non_claims(self) -> None:
        result = runner.run_current_body_conformance_pass()
        non_claims = result["non_claims"]

        for key in FALSE_NON_CLAIM_KEYS:
            with self.subTest(key=key):
                self.assertIn(key, non_claims)
                self.assertFalse(non_claims[key])
        self.assertTrue(result["integrated_non_claims"]["all_required_non_claims_false"])

    def test_conformance_checks(self) -> None:
        checks = runner.run_current_body_conformance_pass()["current_body_conformance_checks"]
        by_name = {check["check_name"]: check for check in checks}

        for check in checks:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIn("expected_posture", check)
            self.assertIn("actual_posture", check)
            self.assertIn("block_code", check)

        expected_names = {
            "self_orientation_v6_exists",
            "self_orientation_v6_is_self_oriented",
            "current_governing_basis_recognized",
            "current_governing_basis_upstream_derived",
            "reentry_closure_remains_closed",
            "follow_on_authorization_remains_false",
            "body_signal_recognition_acceptance_scope_line_stands",
            "body_signal_line_remains_non_operative",
            "body_signal_line_does_not_become_authority_currentness_permission_action",
            "derivative_vessel_relation_boundary_stands",
            "derivative_vessel_relation_remains_downstream",
            "derivative_vessel_relation_creates_no_authority",
            "derivative_vessel_relation_creates_no_currentness",
            "derivative_vessel_relation_creates_no_permission",
            "derivative_vessel_relation_creates_no_adoption",
            "derivative_vessel_relation_creates_no_privileged_standing",
            "derivative_vessel_relation_replaces_no_source",
            "derivative_vessel_relation_completes_no_final_governance",
            "derivative_vessel_relation_completes_no_final_system_identity",
            "derivative_vessel_relation_completes_no_continuity",
            "derivative_vessel_relation_creates_no_general_vessel_permission",
            "derivative_vessel_relation_authorizes_no_follow_on_vessels",
            "derivative_vessel_output_remains_derivative",
            "operator_facing_output_remains_downstream",
            "no_latest_file_currentness",
            "no_recency_fraud",
            "no_mutation_replay_merge",
            "non_claims_remain_false",
        }
        for name in expected_names:
            with self.subTest(name=name):
                self.assertIn(name, by_name)
                self.assertTrue(by_name[name]["passed"])

    def test_summary_helper(self) -> None:
        result = runner.run_current_body_conformance_pass()
        summary = runner.build_current_body_conformance_summary(result)

        self.assertEqual("BODY_CONFORMANT", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertTrue(summary["selected_self_orientation_v6_id"])
        self.assertTrue(summary["selected_self_orientation_v6_path"])
        self.assertEqual("SELF_ORIENTED", summary["selected_self_orientation_v6_outcome"])
        self.assertTrue(summary["selected_reentry_admissibility_id"])
        self.assertTrue(summary["selected_reentry_receipt_id"])
        self.assertTrue(summary["selected_body_signal_recognition_id"])
        self.assertTrue(summary["selected_body_signal_acceptance_id"])
        self.assertTrue(summary["selected_body_signal_scope_id"])
        self.assertTrue(summary["selected_derivative_vessel_relation_boundary_id"])
        self.assertTrue(summary["selected_derivative_vessel_result_id"])
        self.assertTrue(summary["selected_operator_facing_result_id"])
        self.assertEqual(0, summary["failed_check_count"])
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertTrue(summary["current_governing_basis_passed"])
        self.assertTrue(summary["reentry_posture_passed"])
        self.assertTrue(summary["body_signal_posture_passed"])
        self.assertTrue(summary["derivative_vessel_posture_passed"])
        self.assertTrue(summary["operator_posture_passed"])
        self.assertTrue(summary["integrated_non_claims_passed"])
        self.assertIn("authority_created", summary["key_non_claims"])

    def test_path_based_resolution(self) -> None:
        v6_path = next(runner.CURRENT_SELF_ORIENTATION_V6_ROOT.glob("*.json"))
        result = runner.run_current_body_conformance_pass_from_path(v6_path)

        self.assert_top_level_shape(result)
        self.assertEqual("BODY_CONFORMANT", result["outcome"])
        self.assertEqual(
            str(v6_path.relative_to(REPO_ROOT)),
            result["selected_conformance_inputs"]["selected_self_orientation_v6_result"]["result_path"],
        )
        self.assertTrue(
            result["integrated_current_governing_basis"][
                "downstream_surfaces_do_not_determine_current_governing_basis"
            ]
        )

    def test_write_behavior(self) -> None:
        result = runner.run_current_body_conformance_pass()
        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "nested" / "conformance.json"
            written = runner.write_current_body_conformance_result(result, output_path)
            parsed = json.loads(written.read_text(encoding="utf-8"))

        self.assertEqual(output_path, written)
        self.assert_top_level_shape(parsed)
        self.assertEqual("BODY_CONFORMANT", parsed["outcome"])

    def test_default_output_path_behavior(self) -> None:
        result = runner.run_current_body_conformance_pass()
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            with mock.patch.object(runner, "CURRENT_BODY_CONFORMANCE_ROOT", root):
                first = runner.write_current_body_conformance_result(result)
                second = runner.write_current_body_conformance_result(result)

        self.assertEqual(root, first.parent)
        self.assertEqual(root, second.parent)
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__current_body_conformance_result.json"))
        self.assertTrue(second.name.endswith("_001.json"))

    def test_non_mutation_posture(self) -> None:
        roots = [
            runner.CURRENT_SELF_ORIENTATION_V6_ROOT,
            runner.REENTRY_ADMISSIBILITY_ROOT,
            runner.REENTRY_RECEIPT_ROOT,
            runner.BODY_SIGNAL_RECOGNITION_V2_ROOT,
            runner.BODY_SIGNAL_ACCEPTANCE_ROOT,
            runner.BODY_SIGNAL_SCOPE_ROOT,
            runner.DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT,
            runner.DERIVATIVE_VESSEL_READ_ROOT,
            runner.OPERATOR_TERMINAL_BRIEF_ROOT,
        ]
        before_artifacts = {str(root): artifact_snapshot(root) for root in roots}
        mapping = valid_v6_artifact()
        original = copy.deepcopy(mapping)

        first = runner.run_current_body_conformance_pass(mapping)
        second = runner.run_current_body_conformance_pass(mapping)
        after_artifacts = {str(root): artifact_snapshot(root) for root in roots}

        self.assertEqual(original, mapping)
        self.assertEqual("BODY_CONFORMANT", first["outcome"])
        self.assertEqual("BODY_CONFORMANT", second["outcome"])
        self.assertEqual(before_artifacts, after_artifacts)

    def test_blocking_missing_v6_self_orientation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            with mock.patch.object(runner, "CURRENT_SELF_ORIENTATION_V6_ROOT", Path(temp_dir)):
                result = runner.run_current_body_conformance_pass()

        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual("SELF_ORIENTATION_V6_MISSING", result["block"]["block_code"])

    def test_blocking_v6_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            missing = Path(temp_dir) / "missing.json"
            malformed = Path(temp_dir) / "malformed.json"
            array = Path(temp_dir) / "array.json"
            malformed.write_text("{", encoding="utf-8")
            array.write_text("[]", encoding="utf-8")

            cases = [
                (missing, "SELF_ORIENTATION_V6_UNREADABLE"),
                (malformed, "SELF_ORIENTATION_V6_MALFORMED"),
                (array, "SELF_ORIENTATION_V6_MALFORMED"),
            ]
            for path, expected_code in cases:
                with self.subTest(path=path.name):
                    result = runner.run_current_body_conformance_pass_from_path(path)
                    self.assertEqual("BLOCKED", result["outcome"])
                    self.assertEqual(expected_code, result["block"]["block_code"])

    def test_blocking_v6_not_self_oriented(self) -> None:
        v6 = valid_v6_artifact()
        v6["outcome"] = "BLOCKED"
        self.assert_block(v6, "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED")

    def test_blocking_current_governing_basis_missing_or_downstream_derived(self) -> None:
        missing = valid_v6_artifact()
        missing["current_self_orientation_summary"]["governing_effective_basis_recognized"] = False
        missing["recognized_governing_effective_basis"] = {}
        self.assert_block(missing, "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED")

        downstream = valid_v6_artifact()
        downstream["bounded_correspondence_checks"][0]["passed"] = False
        self.assert_block(downstream, "CURRENT_GOVERNING_BASIS_DERIVED_FROM_DOWNSTREAM_SURFACE")

    def test_blocking_reentry_closure_mismatch(self) -> None:
        v6 = valid_v6_artifact()
        v6["recognized_reentry_surfaces"]["closure_posture"]["exhaustion_closure_passed"] = False
        self.assert_block(v6, "REENTRY_CLOSURE_MISMATCH")

    def test_blocking_follow_on_authorization_leak(self) -> None:
        v6 = valid_v6_artifact()
        v6["recognized_reentry_surfaces"]["closure_posture"]["follow_on_steps_authorized"] = True
        self.assert_block(v6, "FOLLOW_ON_AUTHORIZATION_LEAK")

        v6 = valid_v6_artifact()
        set_non_claim(v6, "follow_on_work_authorized", True)
        self.assert_block(v6, "FOLLOW_ON_AUTHORIZATION_LEAK")

    def test_blocking_body_signal_line_missing_or_leaks(self) -> None:
        missing = valid_v6_artifact()
        missing["selected_orientation_inputs"]["selected_body_signal_scope_result"]["outcome"] = "BLOCKED"
        self.assert_block(missing, "BODY_SIGNAL_LINE_MISSING")

        operative = valid_v6_artifact()
        set_non_claim(operative, "presence_established", True)
        self.assert_block(operative, "BODY_SIGNAL_LINE_OPERATIVE_LEAK")

        permission = valid_v6_artifact()
        set_non_claim(permission, "permission_created", True)
        self.assert_block(permission, "BODY_SIGNAL_LINE_AUTHORITY_OR_PERMISSION_LEAK")

        outside = valid_v6_artifact()
        set_non_claim(outside, "applied_outside_declared_scope", True)
        self.assert_block(outside, "BODY_SIGNAL_SCOPE_OUTSIDE_DECLARED_SCOPE")

    def test_blocking_derivative_vessel_relation_boundary_missing_or_not_recognized(self) -> None:
        missing = valid_v6_artifact()
        missing["selected_orientation_inputs"]["selected_derivative_vessel_relation_boundary_result"] = {}
        self.assert_block(missing, "DERIVATIVE_VESSEL_RELATION_BOUNDARY_MISSING")

        blocked = valid_v6_artifact()
        blocked["selected_orientation_inputs"]["selected_derivative_vessel_relation_boundary_result"][
            "outcome"
        ] = "BLOCKED"
        self.assert_block(blocked, "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED")

    def test_blocking_derivative_vessel_relation_leaks(self) -> None:
        cases = [
            ("derivative_vessel_relation_became_authority", "DERIVATIVE_VESSEL_RELATION_AUTHORITY_LEAK"),
            ("derivative_vessel_relation_became_currentness", "DERIVATIVE_VESSEL_RELATION_CURRENTNESS_LEAK"),
            ("derivative_vessel_relation_became_permission", "DERIVATIVE_VESSEL_RELATION_PERMISSION_LEAK"),
            ("derivative_vessel_relation_created_adoption", "DERIVATIVE_VESSEL_RELATION_ADOPTION_LEAK"),
            (
                "derivative_vessel_relation_created_privileged_standing",
                "DERIVATIVE_VESSEL_RELATION_PRIVILEGED_STANDING_LEAK",
            ),
            ("derivative_vessel_relation_replaced_source", "DERIVATIVE_VESSEL_RELATION_SOURCE_REPLACEMENT_LEAK"),
            (
                "derivative_vessel_relation_completed_final_governance",
                "DERIVATIVE_VESSEL_RELATION_FINAL_GOVERNANCE_LEAK",
            ),
            (
                "derivative_vessel_relation_completed_final_system_identity",
                "DERIVATIVE_VESSEL_RELATION_FINAL_SYSTEM_IDENTITY_LEAK",
            ),
            (
                "derivative_vessel_relation_completed_continuity",
                "DERIVATIVE_VESSEL_RELATION_CONTINUITY_COMPLETION_LEAK",
            ),
            (
                "derivative_vessel_relation_created_general_vessel_permission",
                "DERIVATIVE_VESSEL_RELATION_GENERAL_PERMISSION_LEAK",
            ),
            (
                "derivative_vessel_relation_authorized_follow_on_vessels",
                "DERIVATIVE_VESSEL_RELATION_FOLLOW_ON_AUTHORIZATION_LEAK",
            ),
        ]
        for non_claim, expected_code in cases:
            with self.subTest(non_claim=non_claim):
                v6 = valid_v6_artifact()
                set_non_claim(v6, non_claim, True)
                self.assert_block(v6, expected_code)

    def test_blocking_derivative_or_operator_output_source_collapse(self) -> None:
        derivative = valid_v6_artifact()
        derivative["recognized_derivative_surfaces"] = {}
        derivative["recognized_derivative_vessel_relation_surfaces"]["recognized_derivative_vessel_relation"][
            "derivative_vessel_result_outcome"
        ] = "SOURCE"
        self.assert_block(derivative, "DERIVATIVE_OUTPUT_SOURCE_COLLAPSE")

        operator = valid_v6_artifact()
        operator["recognized_operator_facing_surfaces"] = {}
        operator["selected_orientation_inputs"]["selected_operator_terminal_brief_results"][0][
            "outcome"
        ] = "SOURCE"
        self.assert_block(operator, "OPERATOR_OUTPUT_SOURCE_COLLAPSE")

    def test_blocking_latest_file_recency(self) -> None:
        for key in ("latest_file_currentness", "recency_fraud"):
            with self.subTest(key=key):
                v6 = valid_v6_artifact()
                set_non_claim(v6, key, True)
                self.assert_block(v6, "LATEST_FILE_RECENCY_REFUSED")

    def test_blocking_non_claim_flipped(self) -> None:
        v6 = valid_v6_artifact()
        set_non_claim(v6, "roadmap_generated", True)
        self.assert_block(v6, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_blocking_source_derivative_operator_collapse(self) -> None:
        v6 = valid_v6_artifact()
        v6["recognized_derivative_vessel_relation_surfaces"]["source_preserved"] = False
        v6["recognized_derivative_vessel_relation_surfaces"]["relation_remains"][
            "source_preserved"
        ] = False
        self.assert_block(v6, "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE")


if __name__ == "__main__":
    unittest.main()
