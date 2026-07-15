"""Bounded tests for current self-orientation re-entry admissibility.

This suite exercises
``src/resolve_current_self_orientation_reentry_admissibility.py`` as one
bounded gate between recognition and continuation.

It verifies that:

- the re-entry request is a candidate, not a permission slip
- locked basis is preserved and checked against one SELF_ORIENTED result
- hierarchy remains upstream-first
- admission is single-step only
- vague, roadmap, autonomy, mutation, recency, and authority leakage block

This is not a workflow engine suite, an orchestration harness, a roadmap
generator test, a signaling/regulation suite, a governance doctrine suite, or
a manifesto.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


import openai_api_vessel__bounded_current_state_read_v3 as vessel_resolver
import resolve_current_self_orientation_reentry_admissibility as reentry
import resolve_current_self_orientation_v2 as orientation_v2
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import resolve_operator_facing_terminal_brief__bounded_current_state_read as brief_resolver
import run_integrity_host_v0_min_coexistence_v0_body_pass as body_pass_resolver


EXPECTED_RESULT_KEYS = {
    "current_self_orientation_reentry_admissibility_metadata",
    "selected_self_orientation_result",
    "locked_orientation_basis",
    "selected_reentry_request",
    "reentry_admissibility_checks",
    "outcome",
    "block",
    "reentry_admissibility_basis",
    "current_self_orientation_reentry_admissibility_summary",
    "non_claims",
}

EXPECTED_REQUEST_SECTIONS = {
    "reentry_request_metadata",
    "self_orientation_basis",
    "locked_orientation_basis",
    "declared_next_step",
    "declared_scope_bounds",
    "hierarchy_constraints",
    "correspondence_requirements",
    "requested_permissions",
    "declared_non_claims",
    "refusal_acknowledgement",
}

EXPECTED_BLOCK_CODES = {
    "SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED",
    "SELF_ORIENTATION_RESULT_UNREADABLE",
    "SELF_ORIENTATION_RESULT_MALFORMED",
    "SELF_ORIENTATION_RESULT_BASIS_THIN",
    "REENTRY_REQUEST_MISSING_OR_MALFORMED",
    "LOCKED_ORIENTATION_BASIS_MISSING",
    "LOCKED_ORIENTATION_BASIS_MISMATCH",
    "LOCKED_UPSTREAM_BASIS_UNREADABLE",
    "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
    "REQUEST_VAGUE_OR_UNBOUNDED",
    "REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
    "OPEN_SURFACE_TREATED_AS_COMPLETED",
    "BLOCKED_REFUSED_SURFACE_HIDDEN",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "SELF_ORIENTATION_TREATED_AS_SOURCE_AUTHORITY",
    "ROADMAP_AUTONOMY_SIGNALING_REFUSED",
    "MUTATION_REPLAY_MERGE_ATTEMPTED",
    "OVERWRITE_OR_SOURCE_REPLACEMENT_ATTEMPTED",
    "FOLLOW_ON_AUTHORIZATION_ATTEMPTED",
    "GENERAL_FUTURE_WORK_PERMISSION_ATTEMPTED",
    "LATEST_FILE_RECENCY_REFUSED",
    "HUMAN_NARRATION_FALLBACK_REFUSED",
}

REQUIRED_FALSE_NON_CLAIMS = {
    "authority_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "general_permission_created",
    "follow_on_steps_authorized",
    "self_orientation_became_authority",
}


def read_json(path: Path | str) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object at {path}")
    return value


def write_json(path: Path | str, value: Mapping[str, Any]) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(value, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def file_digest(path: Path | str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def tree_digest(root: Path) -> dict[str, str]:
    if not root.exists():
        return {}
    return {
        str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(item for item in root.rglob("*") if item.is_file())
    }


class CurrentSelfOrientationReentryAdmissibilityTests(unittest.TestCase):
    maxDiff = None

    def relative_path(self, temp_root: Path, path: Path | str) -> str:
        return str(Path(path).resolve().relative_to(temp_root.resolve()))

    def patched_repo_root(self, temp_root: Path) -> mock._patch:
        return mock.patch.object(reentry, "_repo_root", return_value=temp_root)

    def basis_paths(self, temp_root: Path) -> dict[str, Path]:
        return {
            "body_pass": temp_root / "artifacts/body_pass/body_pass_result.json",
            "source": temp_root / "artifacts/current_state/what_stands_now.json",
            "answer": temp_root / "artifacts/current_state/answer_read.json",
            "stand": temp_root / "artifacts/current_state/what_stands_now.json",
            "authority": temp_root / "artifacts/effective/authority.json",
            "family": temp_root / "artifacts/effective/family.json",
            "status": temp_root / "artifacts/effective/status.json",
            "governing": temp_root / "artifacts/effective/governing.json",
            "source_run": temp_root / "artifacts/runs/source_run",
            "ingress_run": temp_root / "artifacts/runs/ingress_run",
        }

    def write_basis_paths(self, temp_root: Path, paths: Mapping[str, Path]) -> None:
        for key, path in paths.items():
            if key in {"source_run", "ingress_run"}:
                path.mkdir(parents=True, exist_ok=True)
            else:
                write_json(path, {"artifact": key, "outcome": "PRESENT"})

    def effective_references(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
    ) -> dict[str, str]:
        return {
            "effective_authority_artifact_path": self.relative_path(
                temp_root, paths["authority"]
            ),
            "effective_family_packet_path": self.relative_path(
                temp_root, paths["family"]
            ),
            "effective_status_packet_path": self.relative_path(
                temp_root, paths["status"]
            ),
            "effective_current_governing_packet_path": self.relative_path(
                temp_root, paths["governing"]
            ),
            "effective_source_run_path": self.relative_path(
                temp_root, paths["source_run"]
            ),
            "effective_ingress_run_path": self.relative_path(
                temp_root, paths["ingress_run"]
            ),
        }

    def identity(
        self,
        *,
        result_id: str,
        result_path: str,
        result_family: str,
        outcome: str,
        result_type: str | None = None,
        source_surface_id: str | None = None,
        source_surface_family: str | None = None,
    ) -> dict[str, Any]:
        return {
            "result_id": result_id,
            "result_path": result_path,
            "result_type": result_type,
            "result_family": result_family,
            "outcome": outcome,
            "source_surface_id": source_surface_id,
            "source_surface_family": source_surface_family,
        }

    def non_claims(self) -> dict[str, bool]:
        return {
            "authority_created": False,
            "continuity_completed": False,
            "final_governance_completed": False,
            "final_system_identity_completed": False,
            "standing_upgraded": False,
            "source_replaced": False,
            "derivative_outputs_upgraded_to_source": False,
            "general_permission_created": False,
            "follow_on_steps_authorized": False,
            "self_orientation_became_authority": False,
            "latest_file_currentness": False,
            "recency_fraud": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
            "roadmap_generated": False,
            "next_organ_self_generated": False,
            "workflow_engine_created": False,
            "authority_assigned_by_model": False,
            "authority_assigned_by_brief": False,
        }

    def build_self_orientation(
        self,
        temp_root: Path,
    ) -> tuple[dict[str, Any], dict[str, str], dict[str, Path]]:
        paths = self.basis_paths(temp_root)
        self.write_basis_paths(temp_root, paths)
        effective_refs = self.effective_references(temp_root, paths)
        ids = {
            "self_orientation": "self_orientation_v2_result_001",
            "body_pass": "v0_body_pass_result_001",
            "source": "what_stands_now_result_001",
            "answer": "current_state_answer_read_result_001",
            "open": "what_remains_open_result_001",
            "blocked": "current_state_query_blocked_001",
            "vessel": "bounded_vessel_v3_answered_001",
            "brief": "operator_terminal_brief_rendered_001",
            "touch": "touch_permission_result_001",
            "transfer": "continuity_transfer_result_001",
            "receipt": "continuity_transfer_receipt_result_001",
            "participation": "received_derivative_participation_result_001",
            "action": "received_derivative_action_permission_result_001",
            "seam": "continuity_memory_seam_result_001",
        }
        body_pass = self.identity(
            result_id=ids["body_pass"],
            result_path=self.relative_path(temp_root, paths["body_pass"]),
            result_type=body_pass_resolver.V0_BODY_PASS_RESULT_TYPE,
            result_family="v0_body_pass_result",
            outcome=body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED,
        )
        answer = self.identity(
            result_id=ids["answer"],
            result_path=self.relative_path(temp_root, paths["answer"]),
            result_type="IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_ANSWER_READ_RESULT",
            result_family="current_state_answer_read_result",
            outcome="ANSWERED",
        )
        stand = self.identity(
            result_id=ids["source"],
            result_path=self.relative_path(temp_root, paths["stand"]),
            result_type="IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_STANDS_NOW_RESULT",
            result_family="current_state_what_stands_now_result",
            outcome=stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            source_surface_id=ids["answer"],
            source_surface_family="current_state_answer_read_result",
        )
        open_result = self.identity(
            result_id=ids["open"],
            result_path="artifacts/current_state/what_remains_open.json",
            result_type="IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_REMAINS_OPEN_RESULT",
            result_family="current_state_what_remains_open_result",
            outcome=open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            source_surface_id=ids["answer"],
            source_surface_family="current_state_answer_read_result",
        )
        blocked = {
            "surface_path": "artifacts/current_state/query_blocked.json",
            "surface_id": ids["blocked"],
            "surface_family": "current_state_query_result",
            "surface_outcome": "BLOCKED",
        }
        orientation = {
            "current_self_orientation_v2_metadata": {
                "self_orientation_result_id": ids["self_orientation"],
                "self_orientation_result_type": reentry.SELF_ORIENTATION_V2_RESULT_TYPE,
                "self_orientation_result_version": "0.2.0",
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": orientation_v2.RESOLVER_MODULE,
                "successor_of_module": "resolve_current_self_orientation",
            },
            "selected_orientation_inputs": {
                "selected_body_pass_result": body_pass,
                "selected_seam_result": self.identity(
                    result_id=ids["seam"],
                    result_path="artifacts/continuity/seam.json",
                    result_family="continuity_memory_seam_result",
                    outcome=seam_resolver.OUTCOME_SEAM_CLOSED,
                ),
                "selected_action_permission_result": self.identity(
                    result_id=ids["action"],
                    result_path="artifacts/derivative/action.json",
                    result_family="received_derivative_action_permission_result",
                    outcome=action_resolver.OUTCOME_ACTION_PERMITTED,
                ),
                "selected_participation_result": self.identity(
                    result_id=ids["participation"],
                    result_path="artifacts/derivative/participation.json",
                    result_family="received_derivative_participation_result",
                    outcome=participation_resolver.OUTCOME_PARTICIPATED,
                ),
                "selected_receipt_result": self.identity(
                    result_id=ids["receipt"],
                    result_path="artifacts/continuity/receipt.json",
                    result_family="continuity_transfer_receipt_result",
                    outcome=receipt_resolver.OUTCOME_RECEIVED,
                ),
                "selected_transfer_result": self.identity(
                    result_id=ids["transfer"],
                    result_path="artifacts/continuity/transfer.json",
                    result_family="continuity_transfer_unit_result",
                    outcome=transfer_resolver.OUTCOME_TRANSFERRED,
                ),
                "selected_touch_permission_result": self.identity(
                    result_id=ids["touch"],
                    result_path="artifacts/touch/touch.json",
                    result_family="current_state_touch_permission_result",
                    outcome=touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
                ),
                "selected_source_surface": stand,
                "selected_current_state_answer_read_result": answer,
                "selected_current_state_query_results": [],
                "selected_current_state_what_stands_now_result": stand,
                "selected_current_state_what_remains_open_results": [open_result],
                "selected_vessel_results": [
                    self.identity(
                        result_id=ids["vessel"],
                        result_path="artifacts/vessel/vessel.json",
                        result_type=vessel_resolver.VESSEL_RESULT_TYPE,
                        result_family="openai_api_derivative_vessel_bounded_current_state_read_v3_result",
                        outcome=vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ,
                        source_surface_id=ids["source"],
                        source_surface_family="current_state_what_stands_now_result",
                    )
                ],
                "selected_operator_terminal_brief_results": [
                    self.identity(
                        result_id=ids["brief"],
                        result_path="artifacts/operator/brief.json",
                        result_type=brief_resolver.BRIEF_RESULT_TYPE,
                        result_family="operator_terminal_brief_result",
                        outcome=brief_resolver.OUTCOME_BRIEF_RENDERED,
                        source_surface_id=ids["source"],
                        source_surface_family="current_state_what_stands_now_result",
                    )
                ],
                "selected_effective_references": dict(effective_refs),
            },
            "recognized_current_executable_core_line": {
                "recognized_from_standing_body_pass": True,
                "selected_body_pass_result_id": ids["body_pass"],
                "selected_source_surface_id": ids["source"],
            },
            "recognized_governing_effective_basis": {
                "recognized_from_explicit_effective_references": True,
                "effective_references": dict(effective_refs),
                "current_execution_authority_artifact_path": effective_refs[
                    "effective_authority_artifact_path"
                ],
                "current_governing_packet_path": effective_refs[
                    "effective_current_governing_packet_path"
                ],
            },
            "recognized_current_state_surfaces": {
                "current_state_answer_read_result": dict(answer),
                "current_state_what_stands_now_result": dict(stand),
                "current_state_what_remains_open_results": [dict(open_result)],
            },
            "recognized_continuity_surfaces": {
                "continuity_transfer_unit_result": {"result_id": ids["transfer"]},
                "continuity_transfer_receipt_result": {"result_id": ids["receipt"]},
                "continuity_memory_seam_result": {"result_id": ids["seam"]},
                "v0_body_pass_result": dict(body_pass),
            },
            "recognized_derivative_surfaces": {
                "received_derivative_participation_result": {
                    "result_id": ids["participation"]
                },
                "received_derivative_action_permission_result": {
                    "result_id": ids["action"]
                },
                "openai_api_derivative_vessel_v3_results": [
                    {"result_id": ids["vessel"], "outcome": vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ}
                ],
            },
            "recognized_operator_facing_surfaces": {
                "operator_terminal_brief_results": [
                    {"result_id": ids["brief"], "outcome": brief_resolver.OUTCOME_BRIEF_RENDERED}
                ]
            },
            "recognized_open_surfaces": {
                "what_remains_open_results": [dict(open_result)],
                "carried_non_claims": self.non_claims(),
            },
            "recognized_blocked_or_refused_surfaces": [blocked],
            "recognized_touch_admissibility_surfaces": {
                "current_state_touch_permission_result": {"result_id": ids["touch"]}
            },
            "bounded_correspondence_checks": [
                {"check_name": "self_orientation_is_bounded", "passed": True},
                {"check_name": "self_orientation_preserves_distinctions", "passed": True},
            ],
            "outcome": orientation_v2.OUTCOME_SELF_ORIENTED,
            "block": {"block_code": None, "block_reason": None},
            "self_orientation_basis": {
                "orientation_anchor": "v0_body_pass_result",
                "orientation_selection_mode": "synthetic_test_mapping",
                "selected_body_pass_result_id": ids["body_pass"],
                "selected_source_surface_id": ids["source"],
                "selected_current_state_answer_read_id": ids["answer"],
                "effective_references": dict(effective_refs),
            },
            "current_self_orientation_summary": {
                "outcome": orientation_v2.OUTCOME_SELF_ORIENTED,
                "block_code": None,
                "selected_body_pass_result_id": ids["body_pass"],
                "selected_source_surface_id": ids["source"],
            },
            "non_claims": self.non_claims(),
        }
        orientation_path = (
            temp_root
            / reentry.SELF_ORIENTATION_V2_ROOT
            / "self_orientation_v2_result.json"
        )
        write_json(orientation_path, orientation)
        paths = {**paths, "orientation": orientation_path}
        return orientation, ids, paths

    def build_request(
        self,
        temp_root: Path,
        orientation: Mapping[str, Any],
        orientation_path: Path,
    ) -> dict[str, Any]:
        metadata = orientation["current_self_orientation_v2_metadata"]
        selected = orientation["selected_orientation_inputs"]
        effective_refs = selected["selected_effective_references"]
        return {
            "reentry_request_metadata": {
                "reentry_request_id": "reentry_request_001",
                "reentry_request_type": "IAMMAI_CURRENT_SELF_ORIENTATION_REENTRY_REQUEST",
                "reentry_request_version": "0.1.0",
                "declared_at": "2026-04-24T00:00:00Z",
                "declared_by_surface": "tests/test_resolve_current_self_orientation_reentry_admissibility.py",
            },
            "self_orientation_basis": {
                "self_orientation_result_path": self.relative_path(
                    temp_root, orientation_path
                ),
                "self_orientation_result_id": metadata["self_orientation_result_id"],
                "self_orientation_result_version": metadata[
                    "self_orientation_result_version"
                ],
                "self_orientation_outcome": orientation["outcome"],
                "self_orientation_resolver_module": metadata["resolver_module"],
            },
            "locked_orientation_basis": {
                "selected_body_pass_result_id": selected["selected_body_pass_result"][
                    "result_id"
                ],
                "selected_body_pass_result_path": selected["selected_body_pass_result"][
                    "result_path"
                ],
                "selected_source_surface_id": selected["selected_source_surface"][
                    "result_id"
                ],
                "selected_source_surface_path": selected["selected_source_surface"][
                    "result_path"
                ],
                "selected_current_state_answer_read_id": selected[
                    "selected_current_state_answer_read_result"
                ]["result_id"],
                "selected_current_state_answer_read_path": selected[
                    "selected_current_state_answer_read_result"
                ]["result_path"],
                "selected_what_stands_now_id": selected[
                    "selected_current_state_what_stands_now_result"
                ]["result_id"],
                "selected_what_stands_now_path": selected[
                    "selected_current_state_what_stands_now_result"
                ]["result_path"],
                **effective_refs,
            },
            "declared_next_step": {
                "next_step_family": "SPEC_BOUNDARY",
                "next_step_kind": "bounded_reentry_gate_test_step",
                "target_surface_family": "spec",
                "target_surface_path": "spec/ADMITTED_REENTRY_PROBE.md",
                "target_surface_id": "admitted_reentry_probe",
                "declared_purpose": "bounded single-step spec boundary from locked recognized basis",
                "declared_expected_output_family": "one_additive_file",
                "requested_relation_to_basis": "spec successor from recognized current posture",
            },
            "declared_scope_bounds": {
                "one_step_only": True,
                "additive_output_only": True,
                "allowed_new_file_paths": ["spec/ADMITTED_REENTRY_PROBE.md"],
                "allowed_artifact_output_roots": [],
                "allowed_read_surfaces": [
                    self.relative_path(temp_root, orientation_path)
                ],
                "forbidden_read_surfaces": ["reference/IAMMAI/"],
                "forbidden_write_surfaces": ["reference/"],
            },
            "hierarchy_constraints": {
                "current_governing_basis_source": (
                    "upstream current effective governing current-state surfaces"
                ),
                "derivative_surfaces_allowed_as_basis": False,
                "operator_surfaces_allowed_as_basis": False,
                "self_orientation_allowed_as_authority": False,
                "currentness_may_be_inferred_by_recency": False,
            },
            "correspondence_requirements": {
                "must_preserve_current_basis": True,
                "must_preserve_open_surfaces": True,
                "must_preserve_blocked_refused_surfaces": True,
                "must_preserve_derivative_source_distinction": True,
                "must_preserve_non_claims": True,
                "must_prevent_over_mirroring": True,
                "must_prevent_under_mirroring": True,
            },
            "requested_permissions": {
                "read_permission_requested": True,
                "derive_permission_requested": True,
                "emit_permission_requested": True,
                "mutate_permission_requested": False,
                "replay_permission_requested": False,
                "merge_permission_requested": False,
                "authorization_scope": "single_declared_step_only",
            },
            "declared_non_claims": {
                "does_not_create_authority": True,
                "does_not_complete_continuity": True,
                "does_not_complete_final_governance": True,
                "does_not_complete_final_system_identity": True,
                "does_not_upgrade_standing": True,
                "does_not_replace_source_surfaces": True,
                "does_not_upgrade_derivative_outputs_to_source": True,
                "does_not_create_general_permission": True,
                "does_not_authorize_follow_on_steps": True,
            },
            "refusal_acknowledgement": {
                "request_may_be_blocked": True,
                "blocked_result_must_preserve_basis": True,
                "no_fallback_to_human_narration": True,
                "no_fallback_to_latest_file": True,
            },
        }

    def build_stack(self, temp_root: Path) -> dict[str, Any]:
        orientation, ids, paths = self.build_self_orientation(temp_root)
        request = self.build_request(temp_root, orientation, paths["orientation"])
        return {"orientation": orientation, "request": request, "ids": ids, "paths": paths}

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertTrue(REQUIRED_FALSE_NON_CLAIMS.issubset(non_claims))
        for key, value in non_claims.items():
            self.assertIs(value, False, key)

    def assert_admitted(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(reentry.OUTCOME_REENTRY_ADMITTED, result["outcome"])
        self.assertEqual({"block_code": None, "block_reason": None}, result["block"])
        self.assertIsInstance(result["reentry_admissibility_checks"], list)
        self.assertTrue(result["reentry_admissibility_checks"])
        self.assertTrue(
            all(check["passed"] is True for check in result["reentry_admissibility_checks"])
        )
        self.assertEqual(
            "single_declared_step_only",
            result["reentry_admissibility_basis"]["admission_scope"],
        )
        self.assertTrue(
            result["reentry_admissibility_basis"][
                "self_orientation_remains_non_authoritative"
            ]
        )
        self.assertNotIn("generated_next_task", result)
        self.assertNotIn("roadmap", result)
        self.assertNotIn("workflow", result)
        self.assert_non_claims_false(result)

    def assert_blocked(self, result: Mapping[str, Any], block_code: str) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(reentry.OUTCOME_BLOCKED, result["outcome"])
        self.assertEqual(block_code, result["block"]["block_code"])
        self.assertIsInstance(result["block"]["block_reason"], str)
        self.assertEqual(
            block_code,
            result["current_self_orientation_reentry_admissibility_summary"][
                "block_code"
            ],
        )
        self.assert_non_claims_false(result)

    def resolve(
        self,
        temp_root: Path,
        orientation: Mapping[str, Any],
        request: Mapping[str, Any],
    ) -> dict[str, Any]:
        with self.patched_repo_root(temp_root):
            return reentry.resolve_current_self_orientation_reentry_admissibility(
                orientation,
                request,
            )

    def test_admitted_path_preserves_gate_shape_metadata_basis_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            result = self.resolve(temp_root, stack["orientation"], stack["request"])

        self.assert_admitted(result)
        metadata = result["current_self_orientation_reentry_admissibility_metadata"]
        for key in (
            "reentry_admissibility_result_id",
            "reentry_admissibility_result_type",
            "reentry_admissibility_result_version",
            "generated_at",
            "resolver_module",
        ):
            self.assertIsInstance(metadata[key], str)
            self.assertTrue(metadata[key])
        self.assertEqual(reentry.RESOLVER_MODULE, metadata["resolver_module"])

        selected = result["selected_self_orientation_result"]
        self.assertEqual(stack["ids"]["self_orientation"], selected["result_id"])
        self.assertEqual("0.2.0", selected["result_version"])
        self.assertEqual(orientation_v2.RESOLVER_MODULE, selected["resolver_module"])
        self.assertEqual(orientation_v2.OUTCOME_SELF_ORIENTED, selected["outcome"])
        self.assertNotIn("authority_decision", selected)

        locked = result["locked_orientation_basis"]
        self.assertEqual(stack["ids"]["body_pass"], locked["selected_body_pass_result_id"])
        self.assertEqual(stack["ids"]["source"], locked["selected_source_surface_id"])
        self.assertEqual(
            stack["ids"]["answer"],
            locked["selected_current_state_answer_read_id"],
        )
        self.assertEqual(stack["ids"]["source"], locked["selected_what_stands_now_id"])
        for key in reentry.EFFECTIVE_REFERENCE_KEYS:
            self.assertIsInstance(locked[key], str)
            self.assertTrue(locked[key])

        self.assertEqual(EXPECTED_REQUEST_SECTIONS, set(result["selected_reentry_request"]))
        summary = result["current_self_orientation_reentry_admissibility_summary"]
        self.assertEqual(reentry.OUTCOME_REENTRY_ADMITTED, summary["outcome"])
        self.assertEqual(stack["ids"]["self_orientation"], summary["selected_self_orientation_result_id"])
        self.assertEqual(stack["ids"]["body_pass"], summary["locked_selected_body_pass_result_id"])
        self.assertEqual(stack["ids"]["source"], summary["locked_selected_source_surface_id"])
        self.assertEqual("SPEC_BOUNDARY", summary["next_step_family"])
        self.assertEqual("bounded_reentry_gate_test_step", summary["next_step_kind"])
        self.assertTrue(summary["basis_lock_matched"])
        self.assertTrue(summary["hierarchy_checks_passed"])
        self.assertTrue(summary["correspondence_checks_passed"])
        self.assertTrue(summary["permissions_single_step_bounded"])
        self.assertEqual(0, summary["failed_check_count"])

    def test_resolution_from_path_mapping_and_request_declared_path_are_consistent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            with self.patched_repo_root(temp_root):
                mapping_result = reentry.resolve_current_self_orientation_reentry_admissibility(
                    stack["orientation"],
                    stack["request"],
                )
                path_result = reentry.resolve_current_self_orientation_reentry_admissibility_from_path(
                    stack["paths"]["orientation"],
                    reentry_request=stack["request"],
                )
                request_path_result = reentry.resolve_current_self_orientation_reentry_admissibility(
                    reentry_request=stack["request"],
                )

        self.assert_admitted(mapping_result)
        self.assert_admitted(path_result)
        self.assert_admitted(request_path_result)
        for result in (path_result, request_path_result):
            self.assertEqual(mapping_result["locked_orientation_basis"], result["locked_orientation_basis"])
            self.assertEqual(mapping_result["selected_reentry_request"], result["selected_reentry_request"])
            self.assertEqual(mapping_result["reentry_admissibility_basis"], result["reentry_admissibility_basis"])
            self.assertEqual(
                [
                    (check["check_name"], check["passed"], check.get("block_code"))
                    for check in mapping_result["reentry_admissibility_checks"]
                ],
                [
                    (check["check_name"], check["passed"], check.get("block_code"))
                    for check in result["reentry_admissibility_checks"]
                ],
            )

    def test_request_shape_sections_are_required(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            result = self.resolve(temp_root, stack["orientation"], stack["request"])
            self.assert_admitted(result)

            for section in EXPECTED_REQUEST_SECTIONS:
                request = copy.deepcopy(stack["request"])
                request.pop(section)
                expected_code = (
                    "LOCKED_ORIENTATION_BASIS_MISSING"
                    if section == "locked_orientation_basis"
                    else "REENTRY_REQUEST_MISSING_OR_MALFORMED"
                )
                with self.subTest(section=section):
                    blocked = self.resolve(temp_root, stack["orientation"], request)
                    self.assert_blocked(blocked, expected_code)

    def test_basis_lock_matching_and_drift_blocks(self) -> None:
        drift_cases = {
            "selected_body_pass_result_id": "other_body_pass",
            "selected_source_surface_id": "other_source",
            "selected_current_state_answer_read_id": "other_answer",
            "selected_what_stands_now_id": "other_stand",
            "effective_authority_artifact_path": "artifacts/effective/other_authority.json",
            "effective_current_governing_packet_path": "artifacts/effective/other_governing.json",
        }
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            self.assert_admitted(self.resolve(temp_root, stack["orientation"], stack["request"]))

            for key, value in drift_cases.items():
                request = copy.deepcopy(stack["request"])
                request["locked_orientation_basis"][key] = value
                with self.subTest(key=key):
                    result = self.resolve(temp_root, stack["orientation"], request)
                    self.assert_blocked(result, "LOCKED_ORIENTATION_BASIS_MISMATCH")

    def test_locked_upstream_basis_unreadable_blocks_without_basis_substitution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            missing_path = "artifacts/missing/body_pass_result.json"
            stack["orientation"]["selected_orientation_inputs"]["selected_body_pass_result"][
                "result_path"
            ] = missing_path
            stack["request"]["locked_orientation_basis"][
                "selected_body_pass_result_path"
            ] = missing_path

            result = self.resolve(temp_root, stack["orientation"], stack["request"])

        self.assert_blocked(result, "LOCKED_UPSTREAM_BASIS_UNREADABLE")
        self.assertEqual(
            missing_path,
            result["locked_orientation_basis"]["selected_body_pass_result_path"],
        )

    def test_blocks_self_orientation_not_self_oriented_malformed_or_unreadable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            blocked_orientation = copy.deepcopy(stack["orientation"])
            blocked_orientation["outcome"] = reentry.OUTCOME_BLOCKED
            blocked_orientation["block"] = {
                "block_code": "SELF_ORIENTATION_RESULT_BASIS_THIN",
                "block_reason": "blocked test orientation",
            }
            result = self.resolve(temp_root, blocked_orientation, stack["request"])
            self.assert_blocked(result, "SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED")

            malformed = {"outcome": orientation_v2.OUTCOME_SELF_ORIENTED}
            result = self.resolve(temp_root, malformed, stack["request"])
            self.assert_blocked(result, "SELF_ORIENTATION_RESULT_MALFORMED")

            with self.patched_repo_root(temp_root):
                unreadable = reentry.resolve_current_self_orientation_reentry_admissibility_from_path(
                    temp_root / "missing_self_orientation.json",
                    reentry_request=stack["request"],
                )
            self.assert_blocked(unreadable, "SELF_ORIENTATION_RESULT_UNREADABLE")

    def test_upstream_first_hierarchy_and_authority_upgrade_refusals(self) -> None:
        cases = (
            (
                ("hierarchy_constraints", "derivative_surfaces_allowed_as_basis"),
                True,
                "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
            ),
            (
                ("hierarchy_constraints", "operator_surfaces_allowed_as_basis"),
                True,
                "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
            ),
            (
                ("hierarchy_constraints", "self_orientation_allowed_as_authority"),
                True,
                "SELF_ORIENTATION_TREATED_AS_SOURCE_AUTHORITY",
            ),
            (
                ("hierarchy_constraints", "currentness_may_be_inferred_by_recency"),
                True,
                "LATEST_FILE_RECENCY_REFUSED",
            ),
            (
                ("hierarchy_constraints", "current_governing_basis_source"),
                "bounded vessel output",
                "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
            ),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            for path, value, code in cases:
                request = copy.deepcopy(stack["request"])
                request[path[0]][path[1]] = value
                with self.subTest(path=path):
                    self.assert_blocked(
                        self.resolve(temp_root, stack["orientation"], request),
                        code,
                    )

    def test_step_boundedness_and_follow_on_leakage_block(self) -> None:
        cases = (
            (("declared_next_step", "declared_purpose"), "continue the work", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_next_step", "declared_purpose"), "advance IAMMAI", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_next_step", "declared_purpose"), "determine the next organ", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_next_step", "declared_purpose"), "self-generate the next lawful step", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_next_step", "next_step_family"), "UNBOUNDED_WORK", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_next_step", "requested_relation_to_basis"), "", "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_scope_bounds", "one_step_only"), False, "REQUEST_VAGUE_OR_UNBOUNDED"),
            (("declared_scope_bounds", "additive_output_only"), False, "OVERWRITE_OR_SOURCE_REPLACEMENT_ATTEMPTED"),
            (("requested_permissions", "authorization_scope"), "future_work", "FOLLOW_ON_AUTHORIZATION_ATTEMPTED"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            for path, value, code in cases:
                request = copy.deepcopy(stack["request"])
                request[path[0]][path[1]] = value
                with self.subTest(path=path, value=value):
                    self.assert_blocked(
                        self.resolve(temp_root, stack["orientation"], request),
                        code,
                    )

    def test_correspondence_pressure_blocks_exceeded_posture(self) -> None:
        cases = (
            ("must_preserve_current_basis", "REQUEST_EXCEEDS_RECOGNIZED_POSTURE"),
            ("must_preserve_open_surfaces", "OPEN_SURFACE_TREATED_AS_COMPLETED"),
            ("must_preserve_blocked_refused_surfaces", "BLOCKED_REFUSED_SURFACE_HIDDEN"),
            ("must_preserve_derivative_source_distinction", "REQUEST_EXCEEDS_RECOGNIZED_POSTURE"),
            ("must_preserve_non_claims", "NON_CLAIM_MISSING_OR_FLIPPED"),
            ("must_prevent_over_mirroring", "REQUEST_EXCEEDS_RECOGNIZED_POSTURE"),
            ("must_prevent_under_mirroring", "REQUEST_EXCEEDS_RECOGNIZED_POSTURE"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            for field, code in cases:
                request = copy.deepcopy(stack["request"])
                request["correspondence_requirements"][field] = False
                with self.subTest(field=field):
                    self.assert_blocked(
                        self.resolve(temp_root, stack["orientation"], request),
                        code,
                    )

            completed_open = copy.deepcopy(stack["orientation"])
            completed_open["recognized_open_surfaces"]["what_remains_open_results"][0][
                "outcome"
            ] = "COMPLETED"
            self.assert_blocked(
                self.resolve(temp_root, completed_open, stack["request"]),
                "OPEN_SURFACE_TREATED_AS_COMPLETED",
            )

    def test_non_claims_missing_or_flipped_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            request = copy.deepcopy(stack["request"])
            request["declared_non_claims"].pop("does_not_create_authority")
            self.assert_blocked(
                self.resolve(temp_root, stack["orientation"], request),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )

            request = copy.deepcopy(stack["request"])
            request["declared_non_claims"]["does_not_create_authority"] = False
            self.assert_blocked(
                self.resolve(temp_root, stack["orientation"], request),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )

            orientation = copy.deepcopy(stack["orientation"])
            orientation["non_claims"]["authority_created"] = True
            self.assert_blocked(
                self.resolve(temp_root, orientation, stack["request"]),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )

    def test_roadmap_autonomy_signaling_recency_and_human_narration_block(self) -> None:
        cases = (
            ("generate roadmap from the recognized basis", "ROADMAP_AUTONOMY_SIGNALING_REFUSED"),
            ("autonomous continuation from the recognized basis", "ROADMAP_AUTONOMY_SIGNALING_REFUSED"),
            ("add signaling regulation around the recognized basis", "ROADMAP_AUTONOMY_SIGNALING_REFUSED"),
            ("choose newest file because timestamp wins", "LATEST_FILE_RECENCY_REFUSED"),
            ("external reader README explanation from bounded evidence", "HUMAN_NARRATION_FALLBACK_REFUSED"),
            ("use current orientation for future work", "REQUEST_VAGUE_OR_UNBOUNDED"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            for purpose, code in cases:
                request = copy.deepcopy(stack["request"])
                request["declared_next_step"]["declared_purpose"] = purpose
                with self.subTest(purpose=purpose):
                    self.assert_blocked(
                        self.resolve(temp_root, stack["orientation"], request),
                        code,
                    )

    def test_mutation_replay_merge_and_emit_scope_block(self) -> None:
        cases = (
            ("mutate_permission_requested", True, "MUTATION_REPLAY_MERGE_ATTEMPTED"),
            ("replay_permission_requested", True, "MUTATION_REPLAY_MERGE_ATTEMPTED"),
            ("merge_permission_requested", True, "MUTATION_REPLAY_MERGE_ATTEMPTED"),
        )
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            for field, value, code in cases:
                request = copy.deepcopy(stack["request"])
                request["requested_permissions"][field] = value
                with self.subTest(field=field):
                    self.assert_blocked(
                        self.resolve(temp_root, stack["orientation"], request),
                        code,
                    )

            request = copy.deepcopy(stack["request"])
            request["declared_scope_bounds"]["allowed_new_file_paths"].append(
                "spec/SECOND_OUTPUT.md"
            )
            self.assert_blocked(
                self.resolve(temp_root, stack["orientation"], request),
                "REQUEST_VAGUE_OR_UNBOUNDED",
            )

    def test_declares_block_family_and_summary_helper(self) -> None:
        self.assertTrue(EXPECTED_BLOCK_CODES.issubset(set(reentry.BLOCK_REASONS)))
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            result = self.resolve(temp_root, stack["orientation"], stack["request"])

        summary = reentry.build_current_self_orientation_reentry_admissibility_summary(result)
        self.assertEqual(reentry.OUTCOME_REENTRY_ADMITTED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertIsNone(summary["block_reason"])
        self.assertEqual(stack["ids"]["self_orientation"], summary["selected_self_orientation_result_id"])
        self.assertEqual(stack["ids"]["body_pass"], summary["locked_selected_body_pass_result_id"])
        self.assertEqual(stack["ids"]["source"], summary["locked_selected_source_surface_id"])
        self.assertEqual("SPEC_BOUNDARY", summary["next_step_family"])
        self.assertTrue(summary["basis_lock_matched"])
        self.assertTrue(summary["hierarchy_checks_passed"])
        self.assertTrue(summary["correspondence_checks_passed"])
        self.assertTrue(summary["permissions_single_step_bounded"])
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIs(summary["key_non_claims"][key], False)

    def test_non_mutating_resolution_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            watched_paths = [
                stack["paths"]["orientation"],
                stack["paths"]["body_pass"],
                stack["paths"]["source"],
                stack["paths"]["answer"],
                stack["paths"]["authority"],
                stack["paths"]["family"],
                stack["paths"]["status"],
                stack["paths"]["governing"],
            ]
            before = {str(path): file_digest(path) for path in watched_paths}
            request_before = copy.deepcopy(stack["request"])
            orientation_before = copy.deepcopy(stack["orientation"])
            tree_before = tree_digest(temp_root)

            with self.patched_repo_root(temp_root):
                first = reentry.resolve_current_self_orientation_reentry_admissibility(
                    stack["orientation"],
                    stack["request"],
                )
                second = reentry.resolve_current_self_orientation_reentry_admissibility_from_path(
                    stack["paths"]["orientation"],
                    reentry_request=stack["request"],
                )

            self.assert_admitted(first)
            self.assert_admitted(second)
            self.assertEqual(request_before, stack["request"])
            self.assertEqual(orientation_before, stack["orientation"])
            self.assertEqual(before, {str(path): file_digest(path) for path in watched_paths})
            self.assertEqual(tree_before, tree_digest(temp_root))

            with self.patched_repo_root(temp_root):
                explicit_path = temp_root / "written/nested/reentry_result.json"
                written = reentry.write_current_self_orientation_reentry_admissibility_result(
                    first,
                    explicit_path,
                )
                self.assertEqual(explicit_path, written)
                self.assertTrue(written.is_file())
                self.assertEqual(EXPECTED_RESULT_KEYS, set(read_json(written)))
                with self.assertRaises(FileExistsError):
                    reentry.write_current_self_orientation_reentry_admissibility_result(
                        first,
                        explicit_path,
                    )

                first_default = reentry.write_current_self_orientation_reentry_admissibility_result(first)
                second_default = reentry.write_current_self_orientation_reentry_admissibility_result(first)

            self.assertEqual(
                temp_root / reentry.CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT,
                first_default.parent,
            )
            self.assertTrue(first_default.name.endswith("__reentry_admissibility_result.json"))
            self.assertIn("_001", second_default.stem)
            self.assertNotEqual(first_default, second_default)

    def test_request_is_candidate_not_permission_slip_even_when_blocked(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            request = copy.deepcopy(stack["request"])
            request["locked_orientation_basis"]["selected_source_surface_id"] = "shifted_source"

            result = self.resolve(temp_root, stack["orientation"], request)

        self.assert_blocked(result, "LOCKED_ORIENTATION_BASIS_MISMATCH")
        self.assertEqual("shifted_source", result["locked_orientation_basis"]["selected_source_surface_id"])
        self.assertEqual(request, result["selected_reentry_request"])
        self.assertEqual(
            "single_declared_step_only",
            result["reentry_admissibility_basis"]["admission_scope"],
        )


if __name__ == "__main__":
    unittest.main()
