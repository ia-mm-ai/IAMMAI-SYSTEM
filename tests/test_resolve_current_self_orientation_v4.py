"""Tests for bounded current self-orientation v4.

The v4 resolver is a narrow successor to v3. These tests verify that v4
preserves v3 self-orientation posture while recognizing body-signal recognition
v2 and body-signal acceptance only as downstream, non-operative posture.
"""

from __future__ import annotations

import copy
import contextlib
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

import resolve_current_self_orientation_v4 as resolver


TOP_LEVEL_SECTIONS = {
    "current_self_orientation_v4_metadata",
    "selected_orientation_inputs",
    "recognized_current_executable_core_line",
    "recognized_governing_effective_basis",
    "recognized_current_state_surfaces",
    "recognized_continuity_surfaces",
    "recognized_derivative_surfaces",
    "recognized_operator_facing_surfaces",
    "recognized_reentry_surfaces",
    "recognized_body_signal_surfaces",
    "recognized_open_surfaces",
    "recognized_blocked_or_refused_surfaces",
    "recognized_touch_admissibility_surfaces",
    "bounded_correspondence_checks",
    "outcome",
    "block",
    "self_orientation_basis",
    "current_self_orientation_summary",
    "non_claims",
}

V4_SIGNAL_CHECKS = {
    "body_signal_recognition_v2_is_recognized",
    "body_signal_recognition_category_is_body_pass_signal",
    "body_signal_recognition_source_family_is_v0_body_pass_result",
    "body_signal_blocked_false_permission_signal_remains_blocked",
    "body_signal_acceptance_is_accepted",
    "body_signal_acceptance_matches_selected_recognition",
    "body_signal_acceptance_declared_matter_is_current_signal_recognition_standing",
    "accepted_signal_category_matches_recognized_signal_category",
    "accepted_signal_remains_non_authoritative",
    "accepted_signal_remains_non_permission",
    "accepted_signal_remains_non_currentness",
    "accepted_signal_is_not_scoped",
    "accepted_signal_is_not_present",
    "accepted_signal_has_not_met_threshold",
    "accepted_signal_is_not_truth",
    "accepted_signal_does_not_authorize_action",
    "accepted_signal_does_not_authorize_follow_on_work",
    "accepted_signal_does_not_route_signal",
    "accepted_signal_does_not_create_workflow",
    "accepted_signal_does_not_create_body_relevance_medium",
    "body_signal_surfaces_remain_non_authoritative",
    "body_signal_surfaces_do_not_determine_current_governing_basis",
    "body_signal_line_is_not_action_route_workflow_or_continuation",
}


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


def _snapshot(paths: list[Path]) -> dict[Path, str]:
    return {path: path.read_text(encoding="utf-8") for path in paths if path.exists()}


def _v3_non_claims() -> dict[str, bool]:
    return {
        "authority_created": False,
        "continuity_completed": False,
        "final_governance_completed": False,
        "final_system_identity_completed": False,
        "standing_upgraded": False,
        "source_replaced": False,
        "source_scope_widened": False,
        "derivative_outputs_upgraded_to_source": False,
        "operator_outputs_upgraded_to_source": False,
        "general_permission_created": False,
        "follow_on_steps_authorized": False,
        "admission_reusable": False,
        "self_orientation_became_authority": False,
        "reentry_admissibility_became_authority": False,
        "receipt_became_authority": False,
        "reentry_cycle_became_workflow_lane": False,
        "latest_file_currentness": False,
        "recency_fraud": False,
        "mutation_performed": False,
        "replay_performed": False,
        "merge_performed": False,
        "roadmap_generated": False,
        "next_organ_self_generated": False,
        "workflow_engine_created": False,
        "external_reader_orientation_created": False,
        "hand_maintained_summary_seam_created": False,
    }


def _recognition_non_claims() -> dict[str, bool]:
    return {
        "action_authorized": False,
        "authority_created": False,
        "currentness_created": False,
        "derivative_upgraded_to_source": False,
        "event_bus_created": False,
        "follow_on_work_authorized": False,
        "permission_created": False,
        "receipt_turned_into_permission": False,
        "roadmap_created": False,
        "signal_router_created": False,
        "source_replaced": False,
        "workflow_created": False,
    }


def _acceptance_non_claims() -> dict[str, bool]:
    return {
        "action_authorized": False,
        "authority_created": False,
        "body_relevance_medium_created": False,
        "currentness_created": False,
        "derivative_upgraded_to_source": False,
        "event_bus_created": False,
        "follow_on_work_authorized": False,
        "permission_created": False,
        "presence_established": False,
        "receipt_turned_into_permission": False,
        "roadmap_created": False,
        "scope_assigned": False,
        "signal_router_created": False,
        "source_replaced": False,
        "threshold_met": False,
        "truth_created": False,
        "workflow_created": False,
    }


def _body_selected(body_id: str, body_path: Path) -> dict:
    return {
        "result_id": body_id,
        "result_path": str(body_path),
        "result_type": "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT",
        "result_version": "0.1.0",
        "resolver_module": "run_integrity_host_v0_min_coexistence_v0_body_pass",
        "outcome": "V0_BODY_PASS_CONFIRMED",
        "selection_mode": "synthetic_body_pass",
        "result_family": "v0_body_pass_result",
    }


def _make_stack(root: Path, **overrides: object) -> dict[str, object]:
    roots = {
        "body": root / "artifacts/integrity_host_v0_min_coexistence_v0_body_pass",
        "v3": root
        / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v3",
        "recognition": root
        / "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition_v2",
        "acceptance": root
        / "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance",
        "v4": root
        / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v4",
    }
    for artifact_root in roots.values():
        artifact_root.mkdir(parents=True, exist_ok=True)

    body_id = "body-pass-001"
    body_path = roots["body"] / "body_pass_result.json"
    body_artifact = {
        "v0_body_pass_metadata": {
            "v0_body_pass_result_id": body_id,
            "v0_body_pass_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT"
            ),
            "v0_body_pass_result_version": "0.1.0",
            "runner_module": "run_integrity_host_v0_min_coexistence_v0_body_pass",
        },
        "outcome": "V0_BODY_PASS_CONFIRMED",
    }
    _write_json(body_path, body_artifact)

    body_selected = _body_selected(body_id, body_path)
    selected_inputs = {
        "selected_body_pass_result": body_selected,
        "selected_source_surface": {
            "result_id": "source-current-state-001",
            "result_path": "artifacts/synthetic/current_state_source.json",
            "result_family": "current_state_what_stands_now_result",
            "outcome": "WHAT_STANDS_NOW_ANSWERED",
        },
        "selected_current_state_answer_read_result": {
            "result_id": "current-state-answer-001",
            "result_path": "artifacts/synthetic/current_state_answer.json",
            "outcome": "CURRENT_STATE_ANSWER_READ_ANSWERED",
        },
        "selected_current_state_what_stands_now_result": {
            "result_id": "what-stands-now-001",
            "result_path": "artifacts/synthetic/what_stands_now.json",
            "outcome": "WHAT_STANDS_NOW_ANSWERED",
        },
        "selected_effective_references": {
            "effective_authority_artifact_path": "artifacts/synthetic/authority.json",
            "effective_family_packet_path": "artifacts/synthetic/family.json",
            "effective_status_packet_path": "artifacts/synthetic/status.json",
            "effective_current_governing_packet_path": "artifacts/synthetic/governing.json",
            "effective_source_run_path": "artifacts/synthetic/source_run.json",
            "effective_ingress_run_path": "artifacts/synthetic/ingress_run.json",
        },
        "selected_self_orientation_v2_result": {
            "result_id": "self-orientation-v2-001",
            "result_path": "artifacts/synthetic/self_orientation_v2.json",
            "outcome": "SELF_ORIENTED",
        },
        "selected_reentry_admissibility_result": {
            "result_id": "reentry-admissibility-001",
            "result_path": "artifacts/synthetic/reentry_admissibility.json",
            "outcome": "REENTRY_ADMITTED",
        },
        "selected_reentry_receipt_result": {
            "result_id": "reentry-receipt-001",
            "result_path": "artifacts/synthetic/reentry_receipt.json",
            "outcome": "REENTRY_RECEIVED",
        },
        "selection_scope": {
            "body_pass_anchor_required": True,
            "self_orientation_v2_is_predecessor_recognition": True,
            "reentry_surfaces_are_downstream_only": True,
            "latest_file_recency_refused": True,
            "repo_wide_authority_scan_performed": False,
        },
    }
    v3_result = {
        "current_self_orientation_v3_metadata": {
            "self_orientation_result_id": "self-orientation-v3-001",
            "self_orientation_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V3_RESULT"
            ),
            "self_orientation_result_version": "0.3.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v3",
            "successor_of_module": "resolve_current_self_orientation_v2",
        },
        "selected_orientation_inputs": selected_inputs,
        "recognized_current_executable_core_line": {
            "recognized": True,
            "basis": "upstream_current_executable_core",
        },
        "recognized_governing_effective_basis": {
            "recognized": True,
            "basis": "explicit_current_effective_governing_surface",
            "derived_from_body_signal": False,
            "derived_from_reentry": False,
            "derived_from_derivative": False,
            "derived_from_operator": False,
        },
        "recognized_current_state_surfaces": {"what_stands_now": "recognized"},
        "recognized_continuity_surfaces": {"continuity_transfer": "recognized"},
        "recognized_derivative_surfaces": {
            "derivative_posture": "downstream_only",
            "determines_governing_basis": False,
        },
        "recognized_operator_facing_surfaces": {
            "operator_posture": "downstream_only",
            "determines_governing_basis": False,
        },
        "recognized_reentry_surfaces": {
            "recognition_posture": "downstream_closed_reentry_cycle_only",
            "selected_reentry_admissibility_result": selected_inputs[
                "selected_reentry_admissibility_result"
            ],
            "selected_reentry_receipt_result": selected_inputs[
                "selected_reentry_receipt_result"
            ],
            "closure_posture": {
                "follow_on_steps_authorized": False,
                "general_permission_created": False,
                "admission_reusable": False,
            },
        },
        "recognized_open_surfaces": {"open_surface_visible": True},
        "recognized_blocked_or_refused_surfaces": {"blocked_refused_visible": True},
        "recognized_touch_admissibility_surfaces": {"touch_admissibility_visible": True},
        "bounded_correspondence_checks": [
            {
                "check_name": "v3_current_basis_not_recency_driven",
                "passed": True,
            },
            {
                "check_name": "v3_reentry_surfaces_remain_downstream",
                "passed": True,
            },
        ],
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "self_orientation_basis": {
            "basis_kind": "v3_self_orientation_plus_closed_reentry_cycle",
            "self_orientation_creates_authority": False,
        },
        "current_self_orientation_summary": {"outcome": "SELF_ORIENTED"},
        "non_claims": _v3_non_claims(),
    }
    v3_path = roots["v3"] / "current_self_orientation_v3_result.json"
    _write_json(v3_path, v3_result)

    recognition_result_id = "body-signal-recognition-v2-001"
    recognition_path = roots["recognition"] / "body_signal_recognition_v2_result.json"
    recognition_non_claims = _recognition_non_claims()
    recognition_non_claims.update(
        overrides.get("recognition_nonclaims_update", {})  # type: ignore[arg-type]
    )
    recognition_category = str(overrides.get("recognition_category", "BODY_PASS_SIGNAL"))
    recognition_source_family = str(
        overrides.get("recognition_source_family", "v0_body_pass_result")
    )
    recognition_artifact = {
        "body_signal_recognition_v2_metadata": {
            "body_signal_recognition_result_id": recognition_result_id,
            "body_signal_recognition_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_RECOGNITION_V2_RESULT"
            ),
            "body_signal_recognition_result_version": "0.2.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_body_signal_recognition_v2",
            "successor_of_module": "resolve_body_signal_recognition",
        },
        "recognized_signal": {
            "recognized_signal_id": "recognized-body-pass-signal-001",
            "signal_category": recognition_category,
            "source_artifact_id": body_id,
            "source_artifact_path": str(body_path),
            "source_artifact_family": recognition_source_family,
            "source_artifact_outcome": "V0_BODY_PASS_CONFIRMED",
            "non_authoritative": True,
            "non_permission": True,
            "non_currentness": True,
        },
        "body_signal_recognition_basis": {
            "signal_category": recognition_category,
            "selected_source_artifact": {
                "source_artifact_id": body_id,
                "source_artifact_path": str(body_path),
                "source_artifact_family": recognition_source_family,
                "source_artifact_outcome": "V0_BODY_PASS_CONFIRMED",
            },
        },
        "body_signal_recognition_summary": {
            "failed_check_count": 0,
            "hierarchy_constraints_passed": True,
            "correspondence_requirements_passed": True,
            "non_claims_passed": True,
            "recognized_signal_category": recognition_category,
            "selected_source_artifact_family": recognition_source_family,
        },
        "outcome": str(overrides.get("recognition_outcome", "SIGNAL_RECOGNIZED")),
        "block": {"block_code": None, "block_reason": None},
        "non_claims": recognition_non_claims,
    }
    if overrides.get("recognition_malformed") is True:
        recognition_path.write_text("[1, 2, 3]\n", encoding="utf-8")
    elif overrides.get("omit_recognition") is not True:
        _write_json(recognition_path, recognition_artifact)

    blocked_path = roots["recognition"] / "blocked_permission_signal_result.json"
    blocked_artifact = copy.deepcopy(recognition_artifact)
    blocked_artifact["body_signal_recognition_v2_metadata"][
        "body_signal_recognition_result_id"
    ] = "body-signal-recognition-v2-blocked-permission-001"
    blocked_artifact["recognized_signal"] = None
    blocked_artifact["outcome"] = "BLOCKED"
    blocked_artifact["block"] = {
        "block_code": "SIGNAL_ATTEMPTS_PERMISSION",
        "block_reason": "permission-shaped signal refused",
    }
    blocked_artifact["body_signal_recognition_summary"] = {
        "failed_check_count": 1,
        "signal_category": "BODY_PASS_SIGNAL",
    }
    if overrides.get("omit_blocked_permission_signal") is not True:
        _write_json(blocked_path, blocked_artifact)

    acceptance_path = roots["acceptance"] / "body_signal_acceptance_result.json"
    acceptance_non_claims = _acceptance_non_claims()
    acceptance_non_claims.update(
        overrides.get("acceptance_nonclaims_update", {})  # type: ignore[arg-type]
    )
    accepted_signal = {
        "accepted_signal_id": "accepted-body-pass-signal-001",
        "accepted_signal_category": str(
            overrides.get("accepted_signal_category", "BODY_PASS_SIGNAL")
        ),
        "selected_signal_recognition_result_id": str(
            overrides.get("acceptance_selected_recognition_id", recognition_result_id)
        ),
        "selected_signal_recognition_result_path": str(
            overrides.get("acceptance_selected_recognition_path", recognition_path)
        ),
        "selected_signal_recognition_outcome": "SIGNAL_RECOGNIZED",
        "recognized_source_artifact_id": body_id,
        "recognized_source_artifact_path": str(body_path),
        "recognized_source_artifact_family": "v0_body_pass_result",
        "recognized_source_artifact_outcome": "V0_BODY_PASS_CONFIRMED",
        "declared_matter_id": str(
            overrides.get("acceptance_matter_id", "current_signal_recognition_standing")
        ),
        "declared_matter_family": "body_signal_acceptance_matter",
        "declared_matter_kind": "recognized_body_signal_posture",
        "declared_matter_purpose": (
            "Hold recognized body-signal posture as current signal-recognition standing."
        ),
        "non_authoritative": True,
        "non_permission": True,
        "non_currentness": True,
        "not_scoped_yet": True,
        "not_present_yet": True,
        "not_threshold_yet": True,
        "not_truth": True,
        "no_action": True,
        "no_routing": True,
        "no_workflow": True,
        "no_body_relevance_medium": True,
    }
    accepted_signal.update(overrides.get("accepted_signal_update", {}))  # type: ignore[arg-type]
    acceptance_artifact = {
        "body_signal_acceptance_metadata": {
            "body_signal_acceptance_result_id": "body-signal-acceptance-001",
            "body_signal_acceptance_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_ACCEPTANCE_RESULT"
            ),
            "body_signal_acceptance_result_version": "0.1.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_body_signal_acceptance",
        },
        "accepted_signal": accepted_signal,
        "declared_matter": {
            "matter_id": accepted_signal["declared_matter_id"],
            "matter_family": "body_signal_acceptance_matter",
            "matter_kind": "recognized_body_signal_posture",
            "matter_purpose": accepted_signal["declared_matter_purpose"],
        },
        "body_signal_acceptance_summary": {
            "failed_check_count": 0,
            "recognition_basis_passed": True,
            "matter_boundary_passed": True,
            "acceptance_scope_passed": True,
            "hierarchy_constraints_passed": True,
            "correspondence_requirements_passed": True,
            "non_claims_passed": True,
        },
        "outcome": str(overrides.get("acceptance_outcome", "SIGNAL_ACCEPTED")),
        "block": {"block_code": None, "block_reason": None},
        "non_claims": acceptance_non_claims,
    }
    if overrides.get("acceptance_malformed") is True:
        acceptance_path.write_text("[1, 2, 3]\n", encoding="utf-8")
    elif overrides.get("omit_acceptance") is not True:
        _write_json(acceptance_path, acceptance_artifact)

    return {
        "roots": roots,
        "body_path": body_path,
        "v3_path": v3_path,
        "recognition_path": recognition_path,
        "blocked_path": blocked_path,
        "acceptance_path": acceptance_path,
        "artifact_paths": [
            body_path,
            v3_path,
            recognition_path,
            blocked_path,
            acceptance_path,
        ],
    }


@contextlib.contextmanager
def _patched_stack(**overrides: object):
    with tempfile.TemporaryDirectory() as tmp:
        paths = _make_stack(Path(tmp), **overrides)
        roots = paths["roots"]
        assert isinstance(roots, dict)
        with contextlib.ExitStack() as stack:
            stack.enter_context(mock.patch.object(resolver, "V0_BODY_PASS_ROOT", roots["body"]))
            stack.enter_context(
                mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V3_ROOT", roots["v3"])
            )
            stack.enter_context(
                mock.patch.object(
                    resolver,
                    "BODY_SIGNAL_RECOGNITION_V2_ROOT",
                    roots["recognition"],
                )
            )
            stack.enter_context(
                mock.patch.object(resolver, "BODY_SIGNAL_ACCEPTANCE_ROOT", roots["acceptance"])
            )
            stack.enter_context(
                mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V4_ROOT", roots["v4"])
            )
            yield paths


class ResolveCurrentSelfOrientationV4Tests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict) -> None:
        self.assertIsInstance(result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertIsInstance(result["bounded_correspondence_checks"], list)
        self.assertIsInstance(result["current_self_orientation_summary"], dict)

    def assert_success_result(self, result: dict) -> None:
        self.assert_top_level_shape(result)
        self.assertEqual("SELF_ORIENTED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertTrue(result["recognized_current_executable_core_line"])
        self.assertTrue(result["recognized_governing_effective_basis"])
        self.assertTrue(result["recognized_body_signal_surfaces"])
        self.assertNotIn("recap", json.dumps(result).lower())

    def live_result(self) -> dict:
        result = resolver.resolve_current_self_orientation()
        self.assert_success_result(result)
        return result

    def test_real_self_oriented_v4_path_has_expected_sections(self) -> None:
        result = self.live_result()
        self.assertIn("recognized_reentry_surfaces", result)
        self.assertIn("recognized_body_signal_surfaces", result)

    def test_metadata_preserves_v4_lineage(self) -> None:
        metadata = self.live_result()["current_self_orientation_v4_metadata"]
        self.assertTrue(metadata["self_orientation_result_id"])
        self.assertEqual(
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V4_RESULT",
            metadata["self_orientation_result_type"],
        )
        self.assertEqual("0.4.0", metadata["self_orientation_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual("resolve_current_self_orientation_v4", metadata["resolver_module"])
        self.assertEqual(
            "resolve_current_self_orientation_v3",
            metadata["successor_of_module"],
        )

    def test_selected_input_set_preserves_v3_and_signal_inputs(self) -> None:
        selected = self.live_result()["selected_orientation_inputs"]
        for key in (
            "selected_body_pass_result",
            "selected_self_orientation_v3_result",
            "selected_reentry_admissibility_result",
            "selected_reentry_receipt_result",
            "selected_body_signal_recognition_result",
            "selected_body_signal_acceptance_result",
            "selected_source_surface",
        ):
            self.assertIn(key, selected)
            self.assertTrue(selected[key])
        scope = selected["selection_scope"]
        self.assertTrue(scope["body_signal_surfaces_are_downstream_only"])
        self.assertFalse(scope["repo_wide_authority_scan_performed"])

    def test_v3_architecture_sections_remain_distinct(self) -> None:
        result = self.live_result()
        for key in (
            "recognized_current_executable_core_line",
            "recognized_governing_effective_basis",
            "recognized_current_state_surfaces",
            "recognized_continuity_surfaces",
            "recognized_derivative_surfaces",
            "recognized_operator_facing_surfaces",
            "recognized_reentry_surfaces",
            "recognized_open_surfaces",
            "recognized_blocked_or_refused_surfaces",
            "recognized_touch_admissibility_surfaces",
        ):
            self.assertIsInstance(result[key], dict)
            self.assertTrue(result[key], key)
        serialized_sections = {key: json.dumps(result[key], sort_keys=True) for key in TOP_LEVEL_SECTIONS}
        self.assertNotEqual(
            serialized_sections["recognized_current_state_surfaces"],
            serialized_sections["recognized_body_signal_surfaces"],
        )

    def test_current_governing_basis_remains_upstream_derived(self) -> None:
        result = self.live_result()
        basis = result["self_orientation_basis"]
        self.assertFalse(basis["signal_recognition_creates_authority"])
        self.assertFalse(basis["signal_acceptance_creates_authority"])
        self.assertFalse(basis["recognized_signal_creates_permission"])
        self.assertFalse(basis["accepted_signal_creates_permission"])
        checks = {check["check_name"]: check for check in result["bounded_correspondence_checks"]}
        self.assertTrue(
            checks["body_signal_surfaces_do_not_establish_current_or_governing_basis"][
                "passed"
            ]
        )

    def test_body_signal_recognition_section_preserves_live_line(self) -> None:
        body_signal = self.live_result()["recognized_body_signal_surfaces"]
        recognition = body_signal["selected_body_signal_recognition_result"]
        selected_signal = body_signal["selected_recognized_signal"]
        blocked = body_signal["selected_blocked_body_signal_recognition_result"]
        blocked_posture = body_signal["blocked_permission_refusal_posture"]
        self.assertEqual("SIGNAL_RECOGNIZED", recognition["outcome"])
        self.assertEqual("BODY_PASS_SIGNAL", selected_signal["signal_category"])
        self.assertEqual("v0_body_pass_result", selected_signal["source_artifact_family"])
        self.assertEqual("V0_BODY_PASS_CONFIRMED", selected_signal["source_artifact_outcome"])
        if blocked:
            self.assertEqual("BLOCKED", blocked["outcome"])
            self.assertEqual("SIGNAL_ATTEMPTS_PERMISSION", blocked_posture["block_code"])

    def test_body_signal_acceptance_section_preserves_matter_and_checks(self) -> None:
        body_signal = self.live_result()["recognized_body_signal_surfaces"]
        acceptance = body_signal["selected_body_signal_acceptance_result"]
        accepted = body_signal["accepted_signal"]
        matter = body_signal["declared_matter"]
        self.assertEqual("SIGNAL_ACCEPTED", acceptance["outcome"])
        self.assertEqual("BODY_PASS_SIGNAL", accepted["accepted_signal_category"])
        self.assertEqual("current_signal_recognition_standing", matter["matter_id"])
        self.assertEqual("body_signal_acceptance_matter", matter["matter_family"])
        self.assertEqual("recognized_body_signal_posture", matter["matter_kind"])
        self.assertTrue(body_signal["recognition_basis_passed"])
        self.assertTrue(body_signal["matter_boundary_passed"])
        self.assertTrue(body_signal["acceptance_scope_passed"])
        self.assertTrue(body_signal["acceptance_hierarchy_constraints_passed"])
        self.assertTrue(body_signal["acceptance_correspondence_requirements_passed"])
        self.assertTrue(body_signal["acceptance_non_claims_passed"])

    def test_accepted_signal_non_collapse_posture_is_preserved(self) -> None:
        body_signal = self.live_result()["recognized_body_signal_surfaces"]
        accepted = body_signal["accepted_signal"]
        remains = body_signal["accepted_signal_remains"]
        self.assertTrue(accepted["non_authoritative"])
        self.assertTrue(accepted["non_permission"])
        self.assertTrue(accepted["non_currentness"])
        for key in (
            "non_authoritative",
            "non_permission",
            "non_currentness",
            "not_scoped",
            "not_present",
            "not_threshold",
            "not_truth",
            "no_action",
            "no_follow_on_work",
            "no_routing",
            "no_workflow",
            "no_body_relevance_medium",
        ):
            self.assertIs(remains[key], True, key)
        self.assertTrue(body_signal["body_signal_surfaces_remain_downstream"])
        self.assertFalse(body_signal["body_signal_surfaces_create_authority"])

    def test_closed_signal_line_is_downstream_and_non_operative(self) -> None:
        result = self.live_result()
        basis = result["self_orientation_basis"]
        for key in (
            "body_signal_surfaces_remain_downstream",
            "body_signal_recognition_recognized",
            "body_signal_acceptance_accepted",
        ):
            self.assertTrue(basis[key])
        for key in (
            "accepted_signal_creates_permission",
            "accepted_signal_creates_scope",
            "accepted_signal_establishes_presence",
            "accepted_signal_meets_threshold",
            "accepted_signal_creates_truth",
            "accepted_signal_authorizes_action",
            "accepted_signal_authorizes_follow_on_work",
            "accepted_signal_routes",
            "accepted_signal_creates_workflow",
            "accepted_signal_creates_body_relevance_medium",
        ):
            self.assertFalse(basis[key])

    def test_bounded_correspondence_checks_include_v3_and_v4_checks(self) -> None:
        checks = self.live_result()["bounded_correspondence_checks"]
        names = {check["check_name"] for check in checks}
        self.assertIn("v3_self_orientation_is_self_oriented", names)
        self.assertTrue(V4_SIGNAL_CHECKS.issubset(names))
        for check in checks:
            if check["check_name"] in V4_SIGNAL_CHECKS:
                self.assertTrue(check["passed"], check)

    def test_summary_helper_preserves_bounded_v4_summary(self) -> None:
        result = self.live_result()
        summary = resolver.build_current_self_orientation_summary(result)
        self.assertEqual("SELF_ORIENTED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        for key in (
            "selected_body_pass_result_id",
            "selected_self_orientation_v3_result_id",
            "selected_reentry_admissibility_result_id",
            "selected_reentry_receipt_result_id",
            "selected_body_signal_recognition_result_id",
            "selected_body_signal_acceptance_result_id",
        ):
            self.assertTrue(summary[key], key)
        for key in (
            "governing_effective_basis_recognized",
            "continuity_surfaces_recognized",
            "derivative_surfaces_recognized",
            "operator_surfaces_recognized",
            "reentry_surfaces_recognized",
            "body_signal_surfaces_recognized",
            "body_signal_recognition_recognized",
            "body_signal_acceptance_accepted",
            "accepted_signal_remains_non_authoritative",
            "accepted_signal_remains_non_permission",
            "accepted_signal_remains_non_currentness",
            "accepted_signal_remains_not_scoped",
            "accepted_signal_remains_not_present",
            "accepted_signal_remains_not_threshold",
            "accepted_signal_remains_not_truth",
            "accepted_signal_remains_no_action",
            "accepted_signal_remains_no_routing",
            "accepted_signal_remains_no_workflow",
            "accepted_signal_remains_no_body_relevance_medium",
            "correspondence_checks_passed",
        ):
            self.assertTrue(summary[key], key)
        self.assertEqual("BODY_PASS_SIGNAL", summary["accepted_signal_category"])
        self.assertEqual("current_signal_recognition_standing", summary["accepted_matter_id"])
        self.assertFalse(summary["non_claims"]["authority_created"])

    def test_path_based_resolution_selects_matching_signal_surfaces(self) -> None:
        result = self.live_result()
        body_path = result["selected_orientation_inputs"]["selected_body_pass_result"][
            "result_path"
        ]
        path_result = resolver.resolve_current_self_orientation_from_path(body_path)
        self.assert_success_result(path_result)
        self.assertEqual(
            result["selected_orientation_inputs"]["selected_body_signal_recognition_result"][
                "result_id"
            ],
            path_result["selected_orientation_inputs"][
                "selected_body_signal_recognition_result"
            ]["result_id"],
        )
        self.assertFalse(
            path_result["self_orientation_basis"][
                "signal_acceptance_creates_authority"
            ]
        )

    def test_write_behavior_with_explicit_path(self) -> None:
        result = self.live_result()
        with tempfile.TemporaryDirectory() as tmp:
            output_path = Path(tmp) / "nested" / "v4_result.json"
            written = resolver.write_current_self_orientation_result(result, output_path)
            self.assertEqual(output_path, written)
            parsed = _read_json(written)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            with self.assertRaises(FileExistsError):
                resolver.write_current_self_orientation_result(result, output_path)

    def test_default_output_path_is_bounded_and_non_overwriting(self) -> None:
        result = self.live_result()
        with tempfile.TemporaryDirectory() as tmp:
            original_default_path = resolver._safe_default_output_path

            def temp_default_path(candidate_result: dict) -> Path:
                return original_default_path(candidate_result, root=Path(tmp))

            with mock.patch.object(resolver, "_safe_default_output_path", temp_default_path):
                first = resolver.write_current_self_orientation_result(result)
                second = resolver.write_current_self_orientation_result(result)
        self.assertIn("current_self_orientation_v4_result", first.name)
        self.assertTrue(first.name.endswith(".json"))
        self.assertIn("current_self_orientation_v4_result_001.json", second.name)

    def test_non_mutation_posture_for_synthetic_stack_and_mapping_input(self) -> None:
        with _patched_stack() as paths:
            artifact_paths = [path for path in paths["artifact_paths"] if path.exists()]
            before_files = _snapshot(artifact_paths)
            body_mapping = _read_json(paths["body_path"])
            body_before = copy.deepcopy(body_mapping)
            first = resolver.resolve_current_self_orientation(body_mapping)
            second = resolver.resolve_current_self_orientation(body_mapping)
            self.assertEqual("SELF_ORIENTED", first["outcome"])
            self.assertEqual("SELF_ORIENTED", second["outcome"])
            self.assertEqual(body_before, body_mapping)
            self.assertEqual(before_files, _snapshot(artifact_paths))

    def assert_blocked_with(self, overrides: dict, expected_codes: set[str]) -> dict:
        with _patched_stack(**overrides):
            result = resolver.resolve_current_self_orientation()
        self.assert_top_level_shape(result)
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertIn(result["block"]["block_code"], expected_codes)
        return result

    def test_refused_no_matching_body_signal_recognition(self) -> None:
        result = self.assert_blocked_with(
            {"omit_recognition": True},
            {"BODY_SIGNAL_RECOGNITION_UNREADABLE"},
        )
        self.assertFalse(result["recognized_body_signal_surfaces"])
        self.assertFalse(result["self_orientation_basis"]["signal_recognition_creates_permission"])

    def test_refused_body_signal_recognition_not_recognized(self) -> None:
        self.assert_blocked_with(
            {"recognition_outcome": "BLOCKED"},
            {
                "BODY_SIGNAL_RECOGNITION_UNREADABLE",
                "BODY_SIGNAL_RECOGNITION_NOT_RECOGNIZED",
            },
        )

    def test_refused_body_signal_recognition_malformed(self) -> None:
        self.assert_blocked_with(
            {"recognition_malformed": True},
            {
                "BODY_SIGNAL_RECOGNITION_UNREADABLE",
                "BODY_SIGNAL_RECOGNITION_MALFORMED",
            },
        )

    def test_refused_body_signal_recognition_category_mismatch(self) -> None:
        self.assert_blocked_with(
            {"recognition_category": "DERIVATIVE_ACTION_PERMISSION_SIGNAL"},
            {
                "BODY_SIGNAL_RECOGNITION_UNREADABLE",
                "BODY_SIGNAL_RECOGNITION_CATEGORY_MISMATCH",
            },
        )

    def test_refused_body_signal_recognition_source_family_mismatch(self) -> None:
        self.assert_blocked_with(
            {"recognition_source_family": "received_derivative_action_permission_result"},
            {
                "BODY_SIGNAL_RECOGNITION_UNREADABLE",
                "BODY_SIGNAL_RECOGNITION_SOURCE_FAMILY_MISMATCH",
            },
        )

    def test_refused_no_matching_body_signal_acceptance(self) -> None:
        result = self.assert_blocked_with(
            {"omit_acceptance": True},
            {"BODY_SIGNAL_ACCEPTANCE_UNREADABLE"},
        )
        self.assertFalse(result["recognized_body_signal_surfaces"])
        self.assertFalse(result["self_orientation_basis"]["signal_acceptance_creates_permission"])

    def test_refused_body_signal_acceptance_not_accepted(self) -> None:
        self.assert_blocked_with(
            {"acceptance_outcome": "BLOCKED"},
            {"BODY_SIGNAL_ACCEPTANCE_UNREADABLE", "BODY_SIGNAL_ACCEPTANCE_NOT_ACCEPTED"},
        )

    def test_refused_body_signal_acceptance_malformed(self) -> None:
        self.assert_blocked_with(
            {"acceptance_malformed": True},
            {"BODY_SIGNAL_ACCEPTANCE_UNREADABLE", "BODY_SIGNAL_ACCEPTANCE_MALFORMED"},
        )

    def test_refused_acceptance_does_not_match_selected_recognition(self) -> None:
        self.assert_blocked_with(
            {
                "acceptance_selected_recognition_id": "different-recognition",
                "acceptance_selected_recognition_path": "different-recognition.json",
            },
            {
                "BODY_SIGNAL_ACCEPTANCE_UNREADABLE",
                "BODY_SIGNAL_ACCEPTANCE_DOES_NOT_MATCH_SELECTED_RECOGNITION",
            },
        )

    def test_refused_acceptance_matter_mismatch(self) -> None:
        self.assert_blocked_with(
            {"acceptance_matter_id": "general_signal_handling"},
            {"BODY_SIGNAL_ACCEPTANCE_UNREADABLE", "BODY_SIGNAL_ACCEPTANCE_MATTER_MISMATCH"},
        )

    def test_refused_acceptance_scope_presence_threshold_truth_collapse(self) -> None:
        cases = [
            ({"not_scoped_yet": False}, "BODY_SIGNAL_ACCEPTANCE_SCOPE_COLLAPSE"),
            ({"not_present_yet": False}, "BODY_SIGNAL_ACCEPTANCE_SCOPE_COLLAPSE"),
            ({"not_threshold_yet": False}, "BODY_SIGNAL_ACCEPTANCE_TRUTH_COLLAPSE"),
            ({"not_truth": False}, "BODY_SIGNAL_ACCEPTANCE_TRUTH_COLLAPSE"),
        ]
        for accepted_signal_update, expected_code in cases:
            with self.subTest(accepted_signal_update=accepted_signal_update):
                self.assert_blocked_with(
                    {"accepted_signal_update": accepted_signal_update},
                    {expected_code},
                )

    def test_refused_accepted_signal_becomes_authority_permission_currentness(self) -> None:
        cases = [
            ({"non_authoritative": False}, "BODY_SIGNAL_SURFACE_TREATED_AS_AUTHORITY"),
            ({"non_permission": False}, "BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK"),
            (
                {"non_currentness": False},
                "BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS",
            ),
        ]
        for accepted_signal_update, expected_code in cases:
            with self.subTest(accepted_signal_update=accepted_signal_update):
                self.assert_blocked_with(
                    {"accepted_signal_update": accepted_signal_update},
                    {expected_code},
                )

    def test_refused_accepted_signal_action_and_follow_on_leaks(self) -> None:
        self.assert_blocked_with(
            {"accepted_signal_update": {"no_action": False}},
            {"BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK"},
        )
        self.assert_blocked_with(
            {"acceptance_nonclaims_update": {"follow_on_work_authorized": True}},
            {
                "BODY_SIGNAL_ACCEPTANCE_UNREADABLE",
                "BODY_SIGNAL_ACCEPTANCE_FOLLOW_ON_PERMISSION_LEAK",
            },
        )

    def test_refused_routing_workflow_and_body_relevance_medium_leaks(self) -> None:
        cases = [
            ({"no_routing": False}, "BODY_SIGNAL_ACCEPTANCE_ROUTING_LEAK"),
            ({"no_workflow": False}, "BODY_SIGNAL_ACCEPTANCE_WORKFLOW_LEAK"),
            (
                {"no_body_relevance_medium": False},
                "BODY_SIGNAL_ACCEPTANCE_BODY_RELEVANCE_MEDIUM_LEAK",
            ),
        ]
        for accepted_signal_update, expected_code in cases:
            with self.subTest(accepted_signal_update=accepted_signal_update):
                self.assert_blocked_with(
                    {"accepted_signal_update": accepted_signal_update},
                    {expected_code},
                )

    def test_refused_signal_surfaces_treated_as_authority(self) -> None:
        self.assert_blocked_with(
            {"accepted_signal_update": {"non_authoritative": False}},
            {"BODY_SIGNAL_SURFACE_TREATED_AS_AUTHORITY"},
        )

    def test_refused_signal_surfaces_treated_as_current_governing_basis(self) -> None:
        self.assert_blocked_with(
            {"accepted_signal_update": {"non_currentness": False}},
            {"BODY_SIGNAL_SURFACE_TREATED_AS_CURRENT_OR_GOVERNING_BASIS"},
        )

    def test_refused_signal_line_treated_as_action_or_continuation(self) -> None:
        self.assert_blocked_with(
            {"accepted_signal_update": {"no_action": False}},
            {"BODY_SIGNAL_ACCEPTANCE_ACTION_PERMISSION_LEAK"},
        )

    def test_result_non_claims_preserve_false_posture(self) -> None:
        non_claims = self.live_result()["non_claims"]
        for key in (
            "authority_created",
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
            "general_permission_created",
            "follow_on_steps_authorized",
            "admission_reusable",
            "recency_fraud",
            "mutation_performed",
            "replay_performed",
            "merge_performed",
            "roadmap_generated",
            "workflow_engine_created",
            "signal_router_created",
            "event_bus_created",
            "body_relevance_medium_created",
            "accepted_signal_became_scope",
            "accepted_signal_became_presence",
            "accepted_signal_became_threshold",
            "accepted_signal_became_truth",
            "accepted_signal_became_action",
        ):
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)


if __name__ == "__main__":
    unittest.main()
