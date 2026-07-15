"""Tests for bounded current self-orientation v6.

The v6 resolver is a narrow successor to v5. These tests verify that v6
preserves v5 self-orientation posture while recognizing derivative-vessel
relation boundary only as downstream relation-boundary posture.
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

import resolve_current_self_orientation_v6 as resolver


TOP_LEVEL_SECTIONS = {
    "current_self_orientation_v6_metadata",
    "selected_orientation_inputs",
    "recognized_current_executable_core_line",
    "recognized_governing_effective_basis",
    "recognized_current_state_surfaces",
    "recognized_continuity_surfaces",
    "recognized_derivative_surfaces",
    "recognized_operator_facing_surfaces",
    "recognized_reentry_surfaces",
    "recognized_body_signal_surfaces",
    "recognized_derivative_vessel_relation_surfaces",
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

V6_RELATION_CHECKS = {
    "selected_derivative_vessel_relation_boundary_result_is_derivative_vessel_relation_recognized",
    "derivative_vessel_relation_boundary_preserves_selected_source_body_basis",
    "derivative_vessel_relation_boundary_preserves_selected_derivative_vessel_basis",
    "blocked_derivative_vessel_relation_boundary_refusal_remains_visible_where_selected",
    "recognized_relation_remains_downstream",
    "recognized_relation_remains_additive_only",
    "source_body_basis_remains_upstream",
    "derivative_vessel_result_remains_downstream",
    "operator_facing_output_remains_downstream_where_present",
    "relation_does_not_create_authority",
    "relation_does_not_create_permission",
    "relation_does_not_create_currentness",
    "relation_does_not_create_adoption",
    "relation_does_not_create_privileged_standing",
    "relation_does_not_create_public_release",
    "relation_does_not_replace_source",
    "relation_does_not_complete_final_governance",
    "relation_does_not_complete_final_system_identity",
    "relation_does_not_complete_continuity",
    "relation_does_not_create_general_vessel_permission",
    "relation_does_not_authorize_follow_on_vessel_relations",
    "derivative_vessel_relation_boundary_surface_does_not_become_authority",
    "derivative_vessel_relation_boundary_surface_does_not_determine_current_governing_basis",
}

FALSE_NON_CLAIMS = (
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
    "signal_scope_became_authority",
    "derivative_vessel_relation_became_authority",
    "derivative_vessel_relation_became_currentness",
    "derivative_vessel_relation_became_permission",
    "derivative_vessel_relation_became_current_or_governing_basis",
    "derivative_vessel_relation_created_adoption",
    "derivative_vessel_relation_created_privileged_standing",
    "derivative_vessel_relation_created_public_release",
    "derivative_vessel_relation_replaced_source",
    "derivative_vessel_relation_completed_final_governance",
    "derivative_vessel_relation_completed_final_system_identity",
    "derivative_vessel_relation_completed_continuity",
    "derivative_vessel_relation_created_general_vessel_permission",
    "derivative_vessel_relation_authorized_follow_on_vessels",
    "general_permission_created",
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
)

BODY_ID = "body-pass-001"
V5_ID = "body-pass-001__current_self_orientation_v5_self_oriented"
SOURCE_ID = "current-state-source-001"
DERIVATIVE_ID = "bounded-current-state-read-v3-001"
RELATION_RESULT_ID = "derivative-vessel-relation-boundary-recognized-001"
BLOCKED_RELATION_RESULT_ID = "derivative-vessel-relation-boundary-blocked-001"
RELATION_ID = "bounded-derivative-vessel-relation-001"
RELATION_TYPE = "DERIVATIVE_VESSEL_RELATION_DECLARATION"


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


def _relation_non_claims(**updates: bool) -> dict[str, bool]:
    non_claims = {
        "authority_created": False,
        "permission_created": False,
        "currentness_created": False,
        "source_replaced": False,
        "derivative_upgraded_to_source": False,
        "operator_upgraded_to_source": False,
        "adoption_created": False,
        "privileged_standing_created": False,
        "public_release_created": False,
        "final_governance_completed": False,
        "final_system_identity_completed": False,
        "continuity_completed": False,
        "general_vessel_permission_created": False,
        "follow_on_vessels_authorized": False,
        "latest_file_currentness": False,
        "source_derivative_operator_collapsed": False,
    }
    non_claims.update(updates)
    return non_claims


def _make_stack(
    root: Path,
    *,
    include_recognized: bool = True,
    include_blocked: bool = True,
    relation_updates: dict[str, object] | None = None,
    relation_non_claim_updates: dict[str, bool] | None = None,
    malformed_relation: bool = False,
) -> dict[str, object]:
    roots = {
        "body": root / "artifacts/integrity_host_v0_min_coexistence_v0_body_pass",
        "v5": root
        / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v5",
        "relation": root
        / "artifacts/integrity_host_v0_min_coexistence_derivative_vessel_relation_boundary",
        "v6": root
        / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6",
    }
    for artifact_root in roots.values():
        artifact_root.mkdir(parents=True, exist_ok=True)

    source_path = str(root / "artifacts/current_state_what_stands_now_result.json")
    derivative_path = str(root / "artifacts/bounded_current_state_vessel_v3_result.json")
    operator_path = str(root / "artifacts/operator_terminal_brief_result.json")
    body_path = roots["body"] / "body_pass_result.json"
    v5_path = roots["v5"] / "current_self_orientation_v5_result.json"
    relation_path = roots["relation"] / "relation_recognized.json"
    blocked_path = roots["relation"] / "relation_blocked.json"

    body = {
        "v0_body_pass_metadata": {
            "v0_body_pass_result_id": BODY_ID,
            "v0_body_pass_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT"
            ),
            "v0_body_pass_result_version": "0.1.0",
            "generated_at": "2026-04-26T00:00:00Z",
        },
        "selected_source_surface": {
            "selected_source_surface_id": SOURCE_ID,
            "selected_source_surface_path": source_path,
            "selected_source_surface_family": "current_state_what_stands_now_result",
            "selected_source_surface_outcome": "ANSWERED_WHAT_STANDS_NOW",
        },
        "outcome": "V0_BODY_PASS_CONFIRMED",
        "block": {"block_code": None, "block_reason": None},
        "non_claims": {"latest_file_currentness": False, "recency_fraud": False},
    }
    _write_json(body_path, body)

    v5_non_claims = dict(resolver.NON_CLAIM_DEFAULTS)
    v5 = {
        "current_self_orientation_v5_metadata": {
            "self_orientation_result_id": V5_ID,
            "self_orientation_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V5_RESULT"
            ),
            "self_orientation_result_version": "0.5.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v5",
            "successor_of_module": "resolve_current_self_orientation_v4",
        },
        "selected_orientation_inputs": {
            "selected_body_pass_result": {
                "result_id": BODY_ID,
                "result_path": str(body_path),
                "result_type": (
                    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT"
                ),
                "result_family": "v0_body_pass_result",
                "outcome": "V0_BODY_PASS_CONFIRMED",
            },
            "selected_source_surface": {
                "result_id": SOURCE_ID,
                "result_path": source_path,
                "result_family": "current_state_what_stands_now_result",
                "result_type": (
                    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_STANDS_NOW_RESULT"
                ),
                "outcome": "ANSWERED_WHAT_STANDS_NOW",
            },
            "selected_effective_references": {
                "effective_authority_artifact_path": str(root / "artifacts/authority.json"),
                "effective_current_governing_packet_path": str(
                    root / "artifacts/governing.json"
                ),
            },
            "selected_reentry_admissibility_result": {
                "result_id": "reentry-admissibility-001",
                "result_path": str(root / "artifacts/reentry_admissibility.json"),
                "outcome": "REENTRY_ADMISSIBLE",
            },
            "selected_reentry_receipt_result": {
                "result_id": "reentry-receipt-001",
                "result_path": str(root / "artifacts/reentry_receipt.json"),
                "outcome": "REENTRY_RECEIVED",
            },
            "selected_body_signal_recognition_result": {
                "result_id": "body-signal-recognition-001",
                "result_path": str(root / "artifacts/body_signal_recognition.json"),
                "outcome": "SIGNAL_RECOGNIZED",
                "recognized_signal_category": "BODY_PASS_SIGNAL",
            },
            "selected_body_signal_acceptance_result": {
                "result_id": "body-signal-acceptance-001",
                "result_path": str(root / "artifacts/body_signal_acceptance.json"),
                "outcome": "SIGNAL_ACCEPTED",
                "accepted_matter_id": "current_signal_recognition_standing",
            },
            "selected_body_signal_scope_result": {
                "result_id": "body-signal-scope-001",
                "result_path": str(root / "artifacts/body_signal_scope.json"),
                "outcome": "SIGNAL_SCOPED",
                "declared_scope_id": (
                    "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"
                ),
            },
            "selected_vessel_results": [
                {
                    "result_id": DERIVATIVE_ID,
                    "result_path": derivative_path,
                    "result_family": (
                        "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
                    ),
                    "result_type": (
                        "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT"
                    ),
                    "outcome": "ANSWERED_DERIVATIVE_READ",
                    "source_surface_id": SOURCE_ID,
                    "source_surface_family": "current_state_what_stands_now_result",
                }
            ],
            "selected_operator_terminal_brief_results": [
                {
                    "result_id": "operator-terminal-brief-001",
                    "result_path": operator_path,
                    "result_family": "operator_terminal_brief_result",
                    "outcome": "BRIEF_RENDERED",
                    "source_surface_id": SOURCE_ID,
                }
            ],
        },
        "recognized_current_executable_core_line": {
            "core_execution_file": "src/integrity_host_v0_min_coexistence_v2.py",
        },
        "recognized_governing_effective_basis": {
            "basis_family": "current_state_what_stands_now_result",
            "basis_result_id": SOURCE_ID,
            "currentness_source": "explicit_current_effective_basis",
        },
        "recognized_current_state_surfaces": {
            "selected_source_surface_id": SOURCE_ID,
            "selected_source_surface_path": source_path,
        },
        "recognized_continuity_surfaces": {"continuity_surfaces_recognized": True},
        "recognized_derivative_surfaces": {
            "openai_api_derivative_vessel_v3_results": [
                {"result_id": DERIVATIVE_ID, "downstream": True}
            ],
        },
        "recognized_operator_facing_surfaces": {
            "operator_terminal_brief_results": [
                {"result_id": "operator-terminal-brief-001", "downstream": True}
            ],
        },
        "recognized_reentry_surfaces": {
            "reentry_admissibility_result": {"outcome": "REENTRY_ADMISSIBLE"},
            "reentry_receipt_result": {"outcome": "REENTRY_RECEIVED"},
            "reentry_surfaces_remain_downstream": True,
        },
        "recognized_body_signal_surfaces": {
            "recognized_signal": {
                "recognized_signal_category": "BODY_PASS_SIGNAL",
                "outcome": "SIGNAL_RECOGNIZED",
            },
            "accepted_signal": {
                "accepted_signal_category": "BODY_PASS_SIGNAL",
                "declared_matter_id": "current_signal_recognition_standing",
            },
            "scoped_signal": {
                "scoped_signal_category": "BODY_PASS_SIGNAL",
                "declared_scope_id": (
                    "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"
                ),
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
                "no_application_outside_declared_scope": True,
            },
        },
        "recognized_open_surfaces": {"what_remains_open": True},
        "recognized_blocked_or_refused_surfaces": {
            "blocked_false_permission_signal": {"outcome": "BLOCKED"},
        },
        "recognized_touch_admissibility_surfaces": {
            "touch_permission_result": {"outcome": "ADMITTED_FOR_TOUCH"},
        },
        "bounded_correspondence_checks": [
            {
                "check_name": "v5_body_signal_scope_is_scoped",
                "passed": True,
                "expected_posture": True,
                "actual_posture": True,
                "block_code": None,
            }
        ],
        "outcome": "SELF_ORIENTED",
        "block": {"block_code": None, "block_reason": None},
        "self_orientation_basis": {"basis_kind": "synthetic_v5_self_orientation"},
        "current_self_orientation_summary": {},
        "non_claims": v5_non_claims,
    }
    _write_json(v5_path, v5)

    relation = {
        "source_body_basis_id": V5_ID,
        "source_body_basis_path": str(v5_path),
        "source_body_basis_outcome": "SELF_ORIENTED",
        "source_surface_id": SOURCE_ID,
        "source_surface_path": source_path,
        "source_surface_family": "current_state_what_stands_now_result",
        "source_surface_outcome": "ANSWERED_WHAT_STANDS_NOW",
        "derivative_vessel_result_id": DERIVATIVE_ID,
        "derivative_vessel_result_path": derivative_path,
        "derivative_vessel_result_outcome": "ANSWERED_DERIVATIVE_READ",
        "derivative_output_family": (
            "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
        ),
        "derivative_output_basis": "bounded_source_payload",
        "relation_id": RELATION_ID,
        "relation_type": RELATION_TYPE,
        "downstream": True,
        "additive_only": True,
        "reversible_or_non_standing_by_default": True,
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
        "no_follow_on_vessel_authorization": True,
    }
    relation = _deep_update(relation, relation_updates)
    relation_artifact = {
        "derivative_vessel_relation_boundary_metadata": {
            "derivative_vessel_relation_boundary_result_id": RELATION_RESULT_ID,
            "derivative_vessel_relation_boundary_result_type": (
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_DERIVATIVE_VESSEL_RELATION_BOUNDARY_RESULT"
            ),
            "derivative_vessel_relation_boundary_result_version": "0.1.0",
            "generated_at": "2026-04-26T00:00:00Z",
            "resolver_module": "resolve_derivative_vessel_relation_boundary",
        },
        "selected_source_body_basis": {
            "self_orientation_result_id": V5_ID,
            "self_orientation_result_path": str(v5_path),
            "self_orientation_outcome": "SELF_ORIENTED",
            "source_body_basis_id": V5_ID,
            "source_body_basis_path": str(v5_path),
            "source_body_basis_outcome": "SELF_ORIENTED",
            "source_surface_id": SOURCE_ID,
            "source_surface_path": source_path,
            "source_surface_family": "current_state_what_stands_now_result",
            "source_surface_outcome": "ANSWERED_WHAT_STANDS_NOW",
        },
        "selected_derivative_vessel_basis": {
            "derivative_vessel_result_id": DERIVATIVE_ID,
            "derivative_vessel_result_path": derivative_path,
            "derivative_vessel_result_outcome": "ANSWERED_DERIVATIVE_READ",
            "derivative_output_family": (
                "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
            ),
            "derivative_output_basis": "bounded_source_payload",
        },
        "recognized_derivative_vessel_relation": relation,
        "outcome": "DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
        "block": {"block_code": None, "block_reason": None},
        "relation_boundary_checks": [],
        "derivative_vessel_relation_boundary_summary": {
            "relation_id": RELATION_ID,
            "relation_type": RELATION_TYPE,
        },
        "non_claims": _relation_non_claims(**(relation_non_claim_updates or {})),
    }
    if malformed_relation:
        (roots["relation"] / "malformed.json").write_text("{bad json", encoding="utf-8")
    elif include_recognized:
        _write_json(relation_path, relation_artifact)

    if include_blocked:
        blocked_artifact = copy.deepcopy(relation_artifact)
        blocked_artifact["derivative_vessel_relation_boundary_metadata"][
            "derivative_vessel_relation_boundary_result_id"
        ] = BLOCKED_RELATION_RESULT_ID
        blocked_artifact["outcome"] = "BLOCKED"
        blocked_artifact["block"] = {
            "block_code": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
            "block_reason": "synthetic derivative basis mismatch",
        }
        blocked_artifact["recognized_derivative_vessel_relation"] = None
        _write_json(blocked_path, blocked_artifact)

    return {
        "roots": roots,
        "body_path": body_path,
        "v5_path": v5_path,
        "relation_path": relation_path,
        "blocked_path": blocked_path,
    }


def _patched_roots(stack: dict[str, object]) -> mock._patch:
    roots = stack["roots"]
    assert isinstance(roots, dict)
    return mock.patch.multiple(
        resolver,
        V0_BODY_PASS_ROOT=roots["body"],
        CURRENT_SELF_ORIENTATION_V5_ROOT=roots["v5"],
        DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT=roots["relation"],
        CURRENT_SELF_ORIENTATION_V6_ROOT=roots["v6"],
    )


class CurrentSelfOrientationV6Tests(unittest.TestCase):
    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))

    def assert_self_oriented(self, result: dict) -> None:
        self.assertEqual("SELF_ORIENTED", result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])

    def assert_relation_noncollapse(self, result: dict) -> None:
        surfaces = result["recognized_derivative_vessel_relation_surfaces"]
        remains = surfaces["relation_remains"]
        for key in (
            "downstream",
            "additive_only",
            "source_body_basis_upstream",
            "derivative_vessel_result_downstream",
            "operator_facing_output_downstream_where_present",
            "source_preserved",
            "derivative_preserved",
            "no_authority",
            "no_permission",
            "no_currentness",
            "no_adoption",
            "no_privileged_standing",
            "no_public_release",
            "no_source_replacement",
            "no_final_governance",
            "no_final_system_identity",
            "no_continuity_completion",
            "no_general_vessel_permission",
            "no_follow_on_vessel_authorization",
            "surface_remains_downstream_and_non_authoritative",
        ):
            self.assertIs(remains[key], True, key)
        for key in (
            "downstream",
            "additive_only",
            "source_preserved",
            "derivative_preserved",
            "operator_downstream_where_present",
            "no_authority",
            "no_permission",
            "no_currentness",
            "no_adoption",
            "no_privileged_standing",
            "no_public_release",
            "no_source_replacement",
            "no_final_governance",
            "no_final_system_identity",
            "no_continuity_completion",
            "no_general_vessel_permission",
            "no_follow_on_vessel_authorization",
            "derivative_vessel_relation_boundary_surfaces_remain_downstream",
            "derivative_vessel_relation_boundary_surfaces_remain_non_authoritative",
        ):
            self.assertIs(surfaces[key], True, key)

    def test_real_self_oriented_v6_path_and_sections(self) -> None:
        result = resolver.resolve_current_self_orientation()
        self.assertIsInstance(result, dict)
        self.assert_top_level_shape(result)
        self.assert_self_oriented(result)
        self.assertIsInstance(result["recognized_derivative_vessel_relation_surfaces"], dict)
        self.assertNotIn("recap", json.dumps(result).lower())

    def test_metadata_selected_inputs_and_v5_architecture_are_preserved(self) -> None:
        result = resolver.resolve_current_self_orientation()
        metadata = result["current_self_orientation_v6_metadata"]
        self.assertTrue(metadata["self_orientation_result_id"])
        self.assertEqual(
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V6_RESULT",
            metadata["self_orientation_result_type"],
        )
        self.assertEqual("0.6.0", metadata["self_orientation_result_version"])
        self.assertTrue(metadata["generated_at"])
        self.assertEqual("resolve_current_self_orientation_v6", metadata["resolver_module"])
        self.assertEqual("resolve_current_self_orientation_v5", metadata["successor_of_module"])

        selected = result["selected_orientation_inputs"]
        for key in (
            "selected_body_pass_result",
            "selected_self_orientation_v5_result",
            "selected_source_surface",
            "selected_reentry_admissibility_result",
            "selected_reentry_receipt_result",
            "selected_body_signal_recognition_result",
            "selected_body_signal_acceptance_result",
            "selected_body_signal_scope_result",
            "selected_derivative_vessel_relation_boundary_result",
            "selected_blocked_derivative_vessel_relation_boundary_result",
        ):
            self.assertIn(key, selected)
            self.assertIsInstance(selected[key], dict)

        for key in (
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
        ):
            self.assertIsInstance(result[key], dict)
            self.assertTrue(result[key], key)

    def test_current_governing_basis_remains_upstream_derived(self) -> None:
        result = resolver.resolve_current_self_orientation()
        governing = result["recognized_governing_effective_basis"]
        relation = result["recognized_derivative_vessel_relation_surfaces"]
        checks = {check["check_name"]: check for check in result["bounded_correspondence_checks"]}

        self.assertTrue(governing)
        self.assertNotIn("derivative_vessel_relation_boundary", json.dumps(governing))
        self.assertIs(relation["derivative_vessel_relation_boundary_surfaces_remain_downstream"], True)
        self.assertIs(
            checks[
                "derivative_operator_reentry_signal_and_relation_surfaces_do_not_determine_current_governing_basis"
            ]["passed"],
            True,
        )
        self.assertIs(
            checks[
                "derivative_vessel_relation_boundary_surface_does_not_determine_current_governing_basis"
            ]["passed"],
            True,
        )

    def test_derivative_vessel_relation_boundary_section(self) -> None:
        result = resolver.resolve_current_self_orientation()
        surfaces = result["recognized_derivative_vessel_relation_surfaces"]
        self.assertEqual(
            "downstream_derivative_vessel_relation_boundary_only",
            surfaces["recognition_posture"],
        )
        self.assertEqual(
            "DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
            surfaces["selected_derivative_vessel_relation_boundary_result"]["outcome"],
        )
        blocked = surfaces["selected_blocked_derivative_vessel_relation_boundary_result"]
        self.assertEqual("BLOCKED", blocked.get("outcome"))
        self.assertTrue(blocked.get("block_code"))
        self.assertEqual("SELF_ORIENTED", surfaces["selected_source_body_basis_outcome"])
        self.assertTrue(surfaces["selected_source_body_basis_id"])
        self.assertTrue(surfaces["selected_source_body_basis_path"])
        self.assertTrue(surfaces["selected_source_surface_id"])
        self.assertTrue(surfaces["selected_source_surface_path"])
        self.assertTrue(surfaces["selected_derivative_vessel_result_id"])
        self.assertTrue(surfaces["selected_derivative_vessel_result_path"])
        self.assertTrue(surfaces["relation_id"])
        self.assertTrue(surfaces["relation_type"])
        self.assert_relation_noncollapse(result)

    def test_correspondence_checks_and_summary(self) -> None:
        result = resolver.resolve_current_self_orientation()
        check_names = {check["check_name"] for check in result["bounded_correspondence_checks"]}
        self.assertTrue(V6_RELATION_CHECKS.issubset(check_names))
        for check in result["bounded_correspondence_checks"]:
            self.assertIs(check["passed"], True, check["check_name"])

        summary = resolver.build_current_self_orientation_summary(result)
        self.assertEqual("SELF_ORIENTED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        for key in (
            "selected_body_pass_result_id",
            "selected_source_surface_id",
            "selected_self_orientation_v5_result_id",
            "selected_reentry_admissibility_result_id",
            "selected_reentry_receipt_result_id",
            "selected_body_signal_recognition_result_id",
            "selected_body_signal_acceptance_result_id",
            "selected_body_signal_scope_result_id",
            "selected_derivative_vessel_relation_boundary_result_id",
        ):
            self.assertTrue(summary[key], key)
        for key in (
            "governing_effective_basis_recognized",
            "continuity_surfaces_recognized",
            "derivative_surfaces_recognized",
            "operator_surfaces_recognized",
            "reentry_surfaces_recognized",
            "body_signal_surfaces_recognized",
            "derivative_vessel_relation_boundary_recognized",
            "derivative_vessel_relation_remains_downstream",
            "source_body_basis_remains_upstream",
            "derivative_vessel_result_remains_downstream",
            "operator_facing_output_remains_downstream_where_present",
            "relation_remains_additive_only",
            "relation_creates_no_authority",
            "relation_creates_no_permission",
            "relation_creates_no_currentness",
            "relation_creates_no_adoption",
            "relation_creates_no_privileged_standing",
            "relation_creates_no_public_release",
            "relation_replaces_no_source",
            "relation_completes_no_final_governance",
            "relation_completes_no_final_system_identity",
            "relation_completes_no_continuity",
            "relation_creates_no_general_vessel_permission",
            "relation_authorizes_no_follow_on_vessels",
            "correspondence_checks_passed",
        ):
            self.assertIs(summary[key], True, key)

    def test_path_based_resolution(self) -> None:
        base = resolver.resolve_current_self_orientation()
        body_path = REPO_ROOT / base["selected_orientation_inputs"]["selected_body_pass_result"][
            "result_path"
        ]
        result = resolver.resolve_current_self_orientation_from_path(body_path)
        self.assert_top_level_shape(result)
        self.assert_self_oriented(result)
        self.assertEqual(
            base["selected_orientation_inputs"][
                "selected_derivative_vessel_relation_boundary_result"
            ]["result_id"],
            result["selected_orientation_inputs"][
                "selected_derivative_vessel_relation_boundary_result"
            ]["result_id"],
        )
        self.assertIs(
            result["current_self_orientation_summary"][
                "derivative_vessel_relation_boundary_recognized"
            ],
            True,
        )

    def test_write_behavior_and_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            stack = _make_stack(Path(tmp))
            with _patched_roots(stack):
                result = resolver.resolve_current_self_orientation()
                explicit = Path(tmp) / "nested" / "v6_result.json"
                written = resolver.write_current_self_orientation_result(result, explicit)
                self.assertEqual(explicit, written)
                self.assertTrue(written.exists())
                self.assert_top_level_shape(_read_json(written))

                default_one = resolver.write_current_self_orientation_result(result)
                default_two = resolver.write_current_self_orientation_result(result)
                roots = stack["roots"]
                self.assertTrue(str(default_one).startswith(str(roots["v6"])))
                self.assertTrue(str(default_two).startswith(str(roots["v6"])))
                self.assertNotEqual(default_one, default_two)
                self.assertTrue(default_two.stem.endswith("_001"))

    def test_non_mutation_posture(self) -> None:
        result = resolver.resolve_current_self_orientation()
        selected = result["selected_orientation_inputs"]
        paths = [
            REPO_ROOT / selected["selected_body_pass_result"]["result_path"],
            REPO_ROOT / selected["selected_self_orientation_v5_result"]["result_path"],
            REPO_ROOT
            / selected["selected_derivative_vessel_relation_boundary_result"]["result_path"],
            REPO_ROOT
            / selected["selected_blocked_derivative_vessel_relation_boundary_result"][
                "result_path"
            ],
        ]
        before = _snapshot(paths)
        resolver.resolve_current_self_orientation()
        after = _snapshot(paths)
        self.assertEqual(before, after)

        body = _read_json(paths[0])
        body_before = copy.deepcopy(body)
        resolver.resolve_current_self_orientation(body)
        self.assertEqual(body_before, body)

    def test_refuses_no_matching_or_nonrecognized_relation_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            stack = _make_stack(Path(tmp), include_recognized=False, include_blocked=True)
            with _patched_roots(stack):
                result = resolver.resolve_current_self_orientation()
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual(
            "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
            result["block"]["block_code"],
        )
        self.assertFalse(result["recognized_derivative_vessel_relation_surfaces"])
        self.assertTrue(result["selected_orientation_inputs"]["selected_self_orientation_v5_result"])

    def test_refuses_malformed_relation_boundary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            stack = _make_stack(Path(tmp), include_recognized=False, malformed_relation=True)
            with _patched_roots(stack):
                result = resolver.resolve_current_self_orientation()
        self.assertEqual("BLOCKED", result["outcome"])
        self.assertEqual(
            "DERIVATIVE_VESSEL_RELATION_BOUNDARY_MALFORMED",
            result["block"]["block_code"],
        )

    def test_refuses_source_or_derivative_basis_mismatch(self) -> None:
        cases = (
            (
                {"source_body_basis_id": "other-v5", "source_body_basis_path": "other.json"},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
            ),
            (
                {"derivative_vessel_result_id": "other-derivative"},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
            ),
        )
        for relation_updates, expected_code in cases:
            with self.subTest(expected_code=expected_code, updates=relation_updates):
                with tempfile.TemporaryDirectory() as tmp:
                    stack = _make_stack(Path(tmp), relation_updates=relation_updates)
                    with _patched_roots(stack):
                        result = resolver.resolve_current_self_orientation()
                self.assertEqual("BLOCKED", result["outcome"])
                self.assertEqual(expected_code, result["block"]["block_code"])

    def test_refuses_downstream_and_source_replacement_leaks(self) -> None:
        cases = (
            (
                {"downstream": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
            ),
            (
                {"additive_only": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
            ),
            (
                {"source_preserved": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
            ),
            (
                {"no_source_replacement": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_REPLACEMENT_LEAK",
            ),
            (
                {},
                {"source_replaced": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_REPLACEMENT_LEAK",
            ),
        )
        self._assert_relation_blocks(cases)

    def test_refuses_authority_currentness_permission_leaks(self) -> None:
        cases = (
            (
                {"no_authority": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_AUTHORITY_LEAK",
            ),
            (
                {},
                {"authority_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_AUTHORITY_LEAK",
            ),
            (
                {"no_currentness": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CURRENTNESS_LEAK",
            ),
            (
                {},
                {"currentness_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CURRENTNESS_LEAK",
            ),
            (
                {"no_permission": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PERMISSION_LEAK",
            ),
            (
                {},
                {"permission_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PERMISSION_LEAK",
            ),
        )
        self._assert_relation_blocks(cases)

    def test_refuses_adoption_privileged_standing_and_public_release_leaks(self) -> None:
        cases = (
            (
                {"no_adoption": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_ADOPTION_LEAK",
            ),
            (
                {},
                {"adoption_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_ADOPTION_LEAK",
            ),
            (
                {"no_privileged_standing": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PRIVILEGED_STANDING_LEAK",
            ),
            (
                {},
                {"privileged_standing_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PRIVILEGED_STANDING_LEAK",
            ),
            (
                {"no_public_release": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PUBLIC_RELEASE_LEAK",
            ),
            (
                {},
                {"public_release_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PUBLIC_RELEASE_LEAK",
            ),
        )
        self._assert_relation_blocks(cases)

    def test_refuses_finality_general_permission_and_follow_on_leaks(self) -> None:
        cases = (
            (
                {"no_final_governance": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_GOVERNANCE_LEAK",
            ),
            (
                {},
                {"final_governance_completed": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_GOVERNANCE_LEAK",
            ),
            (
                {"no_final_system_identity": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_SYSTEM_IDENTITY_LEAK",
            ),
            (
                {},
                {"final_system_identity_completed": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_SYSTEM_IDENTITY_LEAK",
            ),
            (
                {"no_continuity_completion": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CONTINUITY_COMPLETION_LEAK",
            ),
            (
                {},
                {"continuity_completed": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CONTINUITY_COMPLETION_LEAK",
            ),
            (
                {},
                {"general_vessel_permission_created": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_GENERAL_PERMISSION_LEAK",
            ),
            (
                {"no_follow_on_vessel_authorization": False},
                {},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FOLLOW_ON_AUTHORIZATION_LEAK",
            ),
            (
                {},
                {"follow_on_vessels_authorized": True},
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FOLLOW_ON_AUTHORIZATION_LEAK",
            ),
        )
        self._assert_relation_blocks(cases)

    def test_non_claims_remain_false_for_self_oriented_and_blocked_results(self) -> None:
        success = resolver.resolve_current_self_orientation()
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, success["non_claims"])
            self.assertIs(success["non_claims"][key], False, key)

        with tempfile.TemporaryDirectory() as tmp:
            stack = _make_stack(Path(tmp), relation_updates={"no_authority": False})
            with _patched_roots(stack):
                blocked = resolver.resolve_current_self_orientation()
        self.assertEqual("BLOCKED", blocked["outcome"])
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, blocked["non_claims"])
            self.assertIs(blocked["non_claims"][key], False, key)

    def _assert_relation_blocks(
        self,
        cases: tuple[tuple[dict[str, object], dict[str, bool], str], ...],
    ) -> None:
        for relation_updates, non_claim_updates, expected_code in cases:
            with self.subTest(expected_code=expected_code, updates=relation_updates):
                with tempfile.TemporaryDirectory() as tmp:
                    stack = _make_stack(
                        Path(tmp),
                        relation_updates=relation_updates,
                        relation_non_claim_updates=non_claim_updates,
                    )
                    with _patched_roots(stack):
                        result = resolver.resolve_current_self_orientation()
                self.assertEqual("BLOCKED", result["outcome"])
                self.assertEqual(expected_code, result["block"]["block_code"])
                self.assert_top_level_shape(result)


if __name__ == "__main__":
    unittest.main()
