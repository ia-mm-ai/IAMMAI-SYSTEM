"""Bounded tests for current self-orientation re-entry receipt.

This suite exercises
``src/resolve_current_self_orientation_reentry_receipt.py`` as one bounded
closure/exhaustion surface after re-entry admission.

It verifies that:

- one REENTRY_ADMITTED result is checked against one performed-step candidate
- locked admitted basis is preserved and verified
- receipt proves exhaustion instead of reusable permission
- follow-on authorization, workflow, roadmap, autonomy, recency, mutation, and
  authority leakage block explicitly
- source/derivative/operator hierarchy remains upstream-first
- receipt stays additive and non-mutating

This is not a workflow engine suite, an orchestration harness, a roadmap
tracker, a signaling/regulation suite, a governance doctrine suite, or a
manifesto.
"""

from __future__ import annotations

import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Callable, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


import openai_api_vessel__bounded_current_state_read_v3 as vessel_resolver
import resolve_current_self_orientation_reentry_admissibility as admissibility_resolver
import resolve_current_self_orientation_reentry_receipt as receipt
import resolve_current_self_orientation_v2 as orientation_v2
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as transfer_receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import resolve_operator_facing_terminal_brief__bounded_current_state_read as brief_resolver
import run_integrity_host_v0_min_coexistence_v0_body_pass as body_pass_resolver


EXPECTED_RESULT_KEYS = {
    "current_self_orientation_reentry_receipt_metadata",
    "selected_reentry_admissibility_result",
    "locked_admitted_basis",
    "selected_performed_step",
    "reentry_receipt_checks",
    "outcome",
    "block",
    "reentry_receipt_basis",
    "current_self_orientation_reentry_receipt_summary",
    "non_claims",
}

REQUIRED_METADATA_KEYS = {
    "reentry_receipt_result_id",
    "reentry_receipt_result_type",
    "reentry_receipt_result_version",
    "generated_at",
    "resolver_module",
}

LOCKED_BASIS_KEYS = {
    "selected_body_pass_result_id",
    "selected_body_pass_result_path",
    "selected_source_surface_id",
    "selected_source_surface_path",
    "selected_current_state_answer_read_id",
    "selected_current_state_answer_read_path",
    "selected_what_stands_now_id",
    "selected_what_stands_now_path",
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
}

PERFORMED_STEP_KEYS = {
    "performed_step_path",
    "performed_step_id",
    "performed_step_family",
    "performed_step_kind",
    "performed_step_outcome",
    "performed_step_type",
    "performed_step_generated_at",
    "performed_step_resolver_or_emitter_module",
}

REQUIRED_FALSE_NON_CLAIMS = {
    "authority_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "general_permission_created",
    "follow_on_steps_authorized",
    "admission_reusable",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "roadmap_generated",
    "workflow_engine_created",
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


class CurrentSelfOrientationReentryReceiptTests(unittest.TestCase):
    maxDiff = None

    def relative_path(self, temp_root: Path, path: Path | str) -> str:
        return str(Path(path).resolve().relative_to(temp_root.resolve()))

    def patched_repo_root(self, temp_root: Path) -> mock._patch:
        return mock.patch.object(receipt, "_repo_root", return_value=temp_root)

    def basis_paths(self, temp_root: Path) -> dict[str, Path]:
        return {
            "body_pass": temp_root / "artifacts/body_pass/body_pass_result.json",
            "source": temp_root / "artifacts/current_state/source_surface.json",
            "answer": temp_root / "artifacts/current_state/answer_read.json",
            "stand": temp_root / "artifacts/current_state/what_stands_now.json",
            "authority": temp_root / "artifacts/effective/authority.json",
            "family": temp_root / "artifacts/effective/family.json",
            "status": temp_root / "artifacts/effective/status.json",
            "governing": temp_root / "artifacts/effective/governing.json",
            "source_run": temp_root / "artifacts/runs/source_run",
            "ingress_run": temp_root / "artifacts/runs/ingress_run",
        }

    def write_basis_paths(self, paths: Mapping[str, Path]) -> None:
        for key, path in paths.items():
            if key in {"source_run", "ingress_run"}:
                path.mkdir(parents=True, exist_ok=True)
            else:
                write_json(path, {"artifact": key, "outcome": "PRESENT"})

    def locked_basis(self, temp_root: Path, paths: Mapping[str, Path]) -> dict[str, str]:
        return {
            "selected_body_pass_result_id": "body-pass-valid-v0",
            "selected_body_pass_result_path": self.relative_path(temp_root, paths["body_pass"]),
            "selected_source_surface_id": "source-surface-valid-v0",
            "selected_source_surface_path": self.relative_path(temp_root, paths["source"]),
            "selected_current_state_answer_read_id": "answer-read-valid-v0",
            "selected_current_state_answer_read_path": self.relative_path(temp_root, paths["answer"]),
            "selected_what_stands_now_id": "what-stands-now-valid-v0",
            "selected_what_stands_now_path": self.relative_path(temp_root, paths["stand"]),
            "effective_authority_artifact_path": self.relative_path(temp_root, paths["authority"]),
            "effective_family_packet_path": self.relative_path(temp_root, paths["family"]),
            "effective_status_packet_path": self.relative_path(temp_root, paths["status"]),
            "effective_current_governing_packet_path": self.relative_path(temp_root, paths["governing"]),
            "effective_source_run_path": self.relative_path(temp_root, paths["source_run"]),
            "effective_ingress_run_path": self.relative_path(temp_root, paths["ingress_run"]),
        }

    def non_claims(self) -> dict[str, bool]:
        return {key: False for key in receipt.RESULT_NON_CLAIM_DEFAULTS}

    def admitted_next_step(self, performed_path: str) -> dict[str, str]:
        return {
            "next_step_family": "TEST_SURFACE",
            "next_step_kind": "REENTRY_RECEIPT_BOUNDED_TEST_SURFACE",
            "target_surface_family": "CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_TEST",
            "target_surface_path": performed_path,
            "target_surface_id": "performed-reentry-receipt-target-v0",
            "declared_purpose": "Verify one admitted re-entry step within locked basis bounds.",
            "declared_expected_output_family": "CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_TEST_RESULT",
            "requested_relation_to_basis": "test successor for one admitted re-entry receipt gate",
        }

    def reentry_request(
        self,
        locked_basis: Mapping[str, Any],
        next_step: Mapping[str, Any],
    ) -> dict[str, Any]:
        return {
            "reentry_request_metadata": {
                "reentry_request_id": "reentry-request-valid-v0",
                "reentry_request_type": "IAMMAI_CURRENT_SELF_ORIENTATION_REENTRY_REQUEST",
                "reentry_request_version": "0.1.0",
                "declared_at": "2026-04-25T00:00:00Z",
                "declared_by_surface": "unit-test",
            },
            "self_orientation_basis": {
                "self_orientation_result_path": "artifacts/self_orientation/result.json",
                "self_orientation_result_id": "self-oriented-valid-v2",
                "self_orientation_result_version": "0.1.0",
                "self_orientation_outcome": "SELF_ORIENTED",
                "self_orientation_resolver_module": "resolve_current_self_orientation_v2",
            },
            "locked_orientation_basis": copy.deepcopy(dict(locked_basis)),
            "declared_next_step": copy.deepcopy(dict(next_step)),
            "declared_scope_bounds": {
                "one_step_only": True,
                "additive_output_only": True,
                "allowed_new_file_paths": [next_step["target_surface_path"]],
                "allowed_artifact_output_roots": [],
                "allowed_read_surfaces": [
                    locked_basis["selected_body_pass_result_path"],
                    locked_basis["selected_source_surface_path"],
                    locked_basis["selected_current_state_answer_read_path"],
                    locked_basis["selected_what_stands_now_path"],
                ],
                "forbidden_read_surfaces": ["reference/IAMMAI/"],
                "forbidden_write_surfaces": [
                    locked_basis["selected_body_pass_result_path"],
                    locked_basis["selected_source_surface_path"],
                    locked_basis["selected_current_state_answer_read_path"],
                    locked_basis["selected_what_stands_now_path"],
                ],
            },
            "hierarchy_constraints": {
                "current_governing_basis_source": "upstream current/effective/current-state surfaces",
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

    def admissibility_result(
        self,
        locked_basis: Mapping[str, Any],
        next_step: Mapping[str, Any],
    ) -> dict[str, Any]:
        request = self.reentry_request(locked_basis, next_step)
        return {
            "current_self_orientation_reentry_admissibility_metadata": {
                "reentry_admissibility_result_id": "reentry-admissibility-valid-v0",
                "reentry_admissibility_result_type": receipt.REENTRY_ADMISSIBILITY_RESULT_TYPE,
                "reentry_admissibility_result_version": "0.1.0",
                "generated_at": "2026-04-25T00:00:00Z",
                "resolver_module": receipt.REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
            },
            "selected_self_orientation_result": {
                "result_id": "self-oriented-valid-v2",
                "result_path": "artifacts/self_orientation/result.json",
                "result_version": "0.1.0",
                "resolver_module": "resolve_current_self_orientation_v2",
                "outcome": "SELF_ORIENTED",
            },
            "locked_orientation_basis": copy.deepcopy(dict(locked_basis)),
            "selected_reentry_request": request,
            "reentry_admissibility_checks": [
                {
                    "check_name": "basis_lock_matched",
                    "passed": True,
                },
                {
                    "check_name": "single_step_permission_bounded",
                    "passed": True,
                },
            ],
            "outcome": "REENTRY_ADMITTED",
            "block": {
                "block_code": None,
                "block_reason": None,
            },
            "reentry_admissibility_basis": {
                "basis_kind": "single_self_orientation_result_plus_single_reentry_request",
                "admission_scope": "single_declared_step_only",
                "self_orientation_remains_non_authoritative": True,
                "follow_on_steps_authorized": False,
            },
            "current_self_orientation_reentry_admissibility_summary": {
                "outcome": "REENTRY_ADMITTED",
                "basis_lock_matched": True,
            },
            "non_claims": self.non_claims(),
        }

    def performed_step(
        self,
        next_step: Mapping[str, Any],
        locked_basis: Mapping[str, Any],
        *,
        include_admitted_basis: bool = False,
        admission_path: str | None = None,
        admission_id: str = "reentry-admissibility-valid-v0",
    ) -> dict[str, Any]:
        candidate = {
            "locked_admitted_basis": copy.deepcopy(dict(locked_basis)),
            "admitted_next_step": copy.deepcopy(dict(next_step)),
            "performed_step_path": next_step["target_surface_path"],
            "performed_step_id": next_step["target_surface_id"],
            "performed_step_family": next_step["next_step_family"],
            "performed_step_kind": next_step["next_step_kind"],
            "performed_step_outcome": "PERFORMED",
            "performed_step_type": "IAMMAI_CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_TEST_PERFORMED_STEP",
            "performed_step_generated_at": "2026-04-25T00:00:00Z",
            "performed_step_resolver_or_emitter_module": "bounded_reentry_receipt_test_emitter",
            "target_surface_family": next_step["target_surface_family"],
            "target_surface_path": next_step["target_surface_path"],
            "target_surface_id": next_step["target_surface_id"],
            "declared_expected_output_family": next_step["declared_expected_output_family"],
            "one_step_only": True,
            "additive_output_only": True,
            "performed_output_paths": [next_step["target_surface_path"]],
            "extra_output_paths": [],
            "admission_exhausted": True,
            "admission_reusable": False,
            "reusable_permission_implied": False,
            "follow_on_steps_authorized": False,
            "general_permission_created": False,
            "mutation_performed": False,
            "replay_performed": False,
            "merge_performed": False,
            "overwrite_performed": False,
            "scope_broadened": False,
            "derivative_api_operator_authority_upgraded": False,
            "open_surfaces_remain_open": True,
            "open_surfaces_completed": False,
            "blocked_refused_surfaces_visible": True,
            "blocked_refused_surfaces_hidden": False,
        }
        if include_admitted_basis:
            candidate["admitted_reentry_basis"] = {
                "reentry_admissibility_result_path": admission_path,
                "reentry_admissibility_result_id": admission_id,
                "reentry_admissibility_result_version": "0.1.0",
                "reentry_admissibility_outcome": "REENTRY_ADMITTED",
                "reentry_admissibility_resolver_module": receipt.REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
            }
        return candidate

    def build_stack(self, temp_root: Path) -> dict[str, Any]:
        paths = self.basis_paths(temp_root)
        self.write_basis_paths(paths)
        performed_path = temp_root / "artifacts/performed/reentry_receipt_target.json"
        performed_rel = self.relative_path(temp_root, performed_path)
        locked_basis = self.locked_basis(temp_root, paths)
        next_step = self.admitted_next_step(performed_rel)
        admission = self.admissibility_result(locked_basis, next_step)
        performed = self.performed_step(next_step, locked_basis)
        admission_path = temp_root / "artifacts/admissibility/reentry_admitted.json"
        write_json(admission_path, admission)
        write_json(performed_path, performed)
        return {
            "paths": paths,
            "locked_basis": locked_basis,
            "next_step": next_step,
            "admission": admission,
            "performed": performed,
            "admission_path": admission_path,
            "performed_path": performed_path,
            "admission_rel": self.relative_path(temp_root, admission_path),
            "performed_rel": performed_rel,
        }

    def resolve_valid(
        self,
        temp_root: Path,
        mutate_admission: Callable[[dict[str, Any]], None] | None = None,
        mutate_performed: Callable[[dict[str, Any]], None] | None = None,
        *,
        from_path: bool = False,
        include_admitted_basis: bool = False,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        stack = self.build_stack(temp_root)
        if include_admitted_basis:
            stack["performed"] = self.performed_step(
                stack["next_step"],
                stack["locked_basis"],
                include_admitted_basis=True,
                admission_path=stack["admission_rel"],
            )
        if mutate_admission is not None:
            mutate_admission(stack["admission"])
        if mutate_performed is not None:
            mutate_performed(stack["performed"])
        write_json(stack["admission_path"], stack["admission"])
        write_json(stack["performed_path"], stack["performed"])
        with self.patched_repo_root(temp_root):
            if from_path:
                result = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step=stack["performed"],
                )
            else:
                result = receipt.resolve_current_self_orientation_reentry_receipt(
                    stack["admission"],
                    stack["performed"],
                )
        return result, stack

    def assert_blocked(self, result: Mapping[str, Any], block_code: str) -> None:
        self.assertEqual("BLOCKED", result.get("outcome"))
        self.assertEqual(block_code, result.get("block", {}).get("block_code"))
        self.assertIsInstance(result.get("block", {}).get("block_reason"), str)

    def assert_received(self, result: Mapping[str, Any]) -> None:
        self.assertEqual("REENTRY_RECEIVED", result.get("outcome"))
        self.assertIsNone(result.get("block", {}).get("block_code"))
        self.assertIsNone(result.get("block", {}).get("block_reason"))
        self.assertTrue(all(check.get("passed") is True for check in result["reentry_receipt_checks"]))

    def test_import_posture_keeps_supporting_surfaces_importable(self) -> None:
        self.assertTrue(hasattr(admissibility_resolver, "resolve_current_self_orientation_reentry_admissibility"))
        self.assertTrue(hasattr(orientation_v2, "resolve_current_self_orientation"))
        for module in (
            body_pass_resolver,
            stand_resolver,
            open_resolver,
            touch_resolver,
            transfer_resolver,
            transfer_receipt_resolver,
            participation_resolver,
            action_resolver,
            seam_resolver,
            vessel_resolver,
            brief_resolver,
        ):
            self.assertTrue(hasattr(module, "__file__"))

    def test_real_received_path_returns_bounded_closure_result(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(Path(raw_root))

        self.assertIsInstance(result, dict)
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assert_received(result)
        self.assertEqual("single_admitted_step_only", result["reentry_receipt_basis"]["receipt_scope"])
        self.assertTrue(result["reentry_receipt_basis"]["admission_exhausted"])
        self.assertFalse(result["reentry_receipt_basis"]["receipt_creates_follow_on_permission"])

    def test_explicit_path_and_declared_basis_resolution_are_consistent(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            performed = self.performed_step(
                stack["next_step"],
                stack["locked_basis"],
                include_admitted_basis=True,
                admission_path=stack["admission_rel"],
            )
            write_json(stack["performed_path"], performed)

            with self.patched_repo_root(temp_root):
                path_result = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step=performed,
                )
                default_result = receipt.resolve_current_self_orientation_reentry_receipt(
                    performed_step=performed,
                )

        self.assertEqual(EXPECTED_RESULT_KEYS, set(path_result))
        self.assertEqual(EXPECTED_RESULT_KEYS, set(default_result))
        self.assert_received(path_result)
        self.assert_received(default_result)
        self.assertEqual(
            path_result["selected_reentry_admissibility_result"]["result_id"],
            default_result["selected_reentry_admissibility_result"]["result_id"],
        )
        self.assertEqual(
            path_result["selected_performed_step"]["performed_step_id"],
            default_result["selected_performed_step"]["performed_step_id"],
        )

    def test_metadata_is_present_and_non_empty(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(Path(raw_root))

        metadata = result["current_self_orientation_reentry_receipt_metadata"]
        for key in REQUIRED_METADATA_KEYS:
            self.assertIsInstance(metadata.get(key), str)
            self.assertTrue(metadata[key])
        self.assertEqual(receipt.RESOLVER_MODULE, metadata["resolver_module"])
        self.assertEqual(receipt.REENTRY_RECEIPT_RESULT_TYPE, metadata["reentry_receipt_result_type"])

    def test_selected_admissibility_and_locked_basis_are_preserved_separately(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, stack = self.resolve_valid(Path(raw_root), from_path=True)

        selected = result["selected_reentry_admissibility_result"]
        self.assertEqual("reentry-admissibility-valid-v0", selected["result_id"])
        self.assertEqual(stack["admission_rel"], selected["result_path"])
        self.assertEqual("0.1.0", selected["result_version"])
        self.assertEqual(receipt.REENTRY_ADMISSIBILITY_RESOLVER_MODULE, selected["resolver_module"])
        self.assertEqual("REENTRY_ADMITTED", selected["outcome"])

        locked = result["locked_admitted_basis"]
        self.assertTrue(LOCKED_BASIS_KEYS <= set(locked))
        self.assertEqual(stack["locked_basis"], locked)
        self.assertNotEqual(selected, locked)

    def test_admitted_next_step_and_performed_candidate_are_matched(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, stack = self.resolve_valid(Path(raw_root))

        basis = result["reentry_receipt_basis"]
        performed = result["selected_performed_step"]
        self.assertEqual(stack["next_step"]["next_step_family"], basis["admitted_next_step_family"])
        self.assertEqual(stack["next_step"]["next_step_kind"], basis["admitted_next_step_kind"])
        self.assertEqual(stack["next_step"]["next_step_family"], performed["performed_step_family"])
        self.assertEqual(stack["next_step"]["next_step_kind"], performed["performed_step_kind"])
        self.assertEqual(stack["next_step"]["target_surface_family"], performed["target_surface_family"])
        self.assertEqual(stack["next_step"]["target_surface_path"], performed["target_surface_path"])
        self.assertEqual(stack["next_step"]["target_surface_id"], performed["target_surface_id"])
        self.assertEqual(
            stack["next_step"]["declared_expected_output_family"],
            performed["declared_expected_output_family"],
        )

    def test_performed_step_normalizes_direct_mapping_path_and_nested_candidate(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            direct_result, stack = self.resolve_valid(temp_root)
            with self.patched_repo_root(temp_root):
                path_result = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step_path=stack["performed_rel"],
                )
            nested = {
                "performed_step_receipt_candidate": copy.deepcopy(stack["performed"]),
                "locked_admitted_basis": copy.deepcopy(stack["locked_basis"]),
                "admitted_next_step": copy.deepcopy(stack["next_step"]),
            }
            write_json(stack["performed_path"], nested)
            with self.patched_repo_root(temp_root):
                nested_result = receipt.resolve_current_self_orientation_reentry_receipt(
                    stack["admission"],
                    nested,
                )

        for result in (direct_result, path_result, nested_result):
            self.assert_received(result)
            self.assertTrue(PERFORMED_STEP_KEYS <= set(result["selected_performed_step"]))
            self.assertEqual("performed-reentry-receipt-target-v0", result["selected_performed_step"]["performed_step_id"])

    def test_basis_lock_matching_allows_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(
                Path(raw_root),
                from_path=True,
                include_admitted_basis=True,
            )
        self.assert_received(result)
        self.assertTrue(result["current_self_orientation_reentry_receipt_summary"]["basis_lock_matched"])

    def test_basis_lock_mismatches_block(self) -> None:
        fields = [
            "selected_body_pass_result_id",
            "selected_source_surface_id",
            "selected_current_state_answer_read_id",
            "selected_what_stands_now_id",
            "effective_authority_artifact_path",
            "effective_family_packet_path",
            "effective_status_packet_path",
            "effective_current_governing_packet_path",
            "effective_source_run_path",
            "effective_ingress_run_path",
        ]
        for field in fields:
            with self.subTest(field=field), tempfile.TemporaryDirectory() as raw_root:
                def mutate(performed: dict[str, Any], name: str = field) -> None:
                    performed["locked_admitted_basis"][name] = "shifted-basis"

                result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate)
                self.assert_blocked(result, "LOCKED_ADMITTED_BASIS_MISMATCH")

    def test_performed_step_correspondence_must_match_admitted_step(self) -> None:
        mutations = {
            "family": ("performed_step_family", "OTHER_FAMILY", "PERFORMED_STEP_FAMILY_MISMATCH"),
            "kind": ("performed_step_kind", "OTHER_KIND", "PERFORMED_STEP_KIND_MISMATCH"),
            "target_family": ("target_surface_family", "OTHER_TARGET", "TARGET_SURFACE_MISMATCH"),
            "target_path": ("target_surface_path", "artifacts/performed/other.json", "TARGET_SURFACE_MISMATCH"),
            "target_id": ("target_surface_id", "other-target-id", "TARGET_SURFACE_MISMATCH"),
            "expected_output": (
                "declared_expected_output_family",
                "OTHER_EXPECTED_OUTPUT",
                "EXPECTED_OUTPUT_FAMILY_MISMATCH",
            ),
        }
        for label, (field, value, block_code) in mutations.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                def mutate(performed: dict[str, Any], key: str = field, new_value: str = value) -> None:
                    performed[key] = new_value

                result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate)
                self.assert_blocked(result, block_code)

    def test_summary_helper_reports_closure_status(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(Path(raw_root))

        summary = receipt.build_current_self_orientation_reentry_receipt_summary(result)
        self.assertEqual("REENTRY_RECEIVED", summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertEqual("reentry-admissibility-valid-v0", summary["selected_reentry_admissibility_result_id"])
        self.assertEqual("body-pass-valid-v0", summary["locked_selected_body_pass_result_id"])
        self.assertEqual("source-surface-valid-v0", summary["locked_selected_source_surface_id"])
        self.assertEqual("TEST_SURFACE", summary["performed_step_family"])
        self.assertEqual("REENTRY_RECEIPT_BOUNDED_TEST_SURFACE", summary["performed_step_kind"])
        self.assertTrue(summary["basis_lock_matched"])
        self.assertTrue(summary["performed_step_correspondence_passed"])
        self.assertTrue(summary["scope_stayed_single_step_and_additive"])
        self.assertTrue(summary["exhaustion_closure_passed"])
        self.assertTrue(REQUIRED_FALSE_NON_CLAIMS <= set(summary["key_non_claims"]))

    def test_refuses_admissibility_result_not_reentry_admitted(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def mutate(admission: dict[str, Any]) -> None:
                admission["outcome"] = "BLOCKED"
                admission["block"] = {"block_code": "TEST_BLOCK", "block_reason": "blocked"}

            result, _stack = self.resolve_valid(Path(raw_root), mutate_admission=mutate)
            self.assert_blocked(result, "ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED")

    def test_refuses_malformed_and_unreadable_admissibility_result(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            malformed = copy.deepcopy(stack["admission"])
            malformed.pop("selected_reentry_request")
            with self.patched_repo_root(temp_root):
                malformed_result = receipt.resolve_current_self_orientation_reentry_receipt(
                    malformed,
                    stack["performed"],
                )
                unreadable_result = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    "artifacts/admissibility/missing.json",
                    performed_step=stack["performed"],
                )

        self.assert_blocked(malformed_result, "ADMISSIBILITY_RESULT_MALFORMED")
        self.assert_blocked(unreadable_result, "ADMISSIBILITY_RESULT_UNREADABLE")

    def test_refuses_locked_admitted_basis_missing(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def mutate(admission: dict[str, Any]) -> None:
                admission["locked_orientation_basis"].pop("selected_source_surface_path")

            result, _stack = self.resolve_valid(Path(raw_root), mutate_admission=mutate)
            self.assert_blocked(result, "LOCKED_ADMITTED_BASIS_MISSING")

    def test_refuses_locked_upstream_basis_no_longer_readable(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def mutate_admission(admission: dict[str, Any]) -> None:
                admission["locked_orientation_basis"]["selected_source_surface_path"] = (
                    "artifacts/current_state/missing-source.json"
                )

            def mutate_performed(performed: dict[str, Any]) -> None:
                performed["locked_admitted_basis"]["selected_source_surface_path"] = (
                    "artifacts/current_state/missing-source.json"
                )

            result, _stack = self.resolve_valid(
                Path(raw_root),
                mutate_admission=mutate_admission,
                mutate_performed=mutate_performed,
            )
            self.assert_blocked(result, "LOCKED_UPSTREAM_BASIS_UNREADABLE")

    def test_refuses_performed_step_missing(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            with self.patched_repo_root(temp_root):
                result = receipt.resolve_current_self_orientation_reentry_receipt(
                    stack["admission"],
                    None,
                )
        self.assert_blocked(result, "PERFORMED_STEP_MISSING")

    def test_refuses_unreadable_and_malformed_performed_step(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            malformed_path = temp_root / "artifacts/performed/malformed.json"
            malformed_path.parent.mkdir(parents=True, exist_ok=True)
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.patched_repo_root(temp_root):
                unreadable = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step_path="artifacts/performed/missing.json",
                )
                malformed = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step_path=self.relative_path(temp_root, malformed_path),
                )
        self.assert_blocked(unreadable, "PERFORMED_STEP_UNREADABLE")
        self.assert_blocked(malformed, "PERFORMED_STEP_MALFORMED")

    def test_refuses_admission_scope_exceeded(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(
                Path(raw_root),
                mutate_performed=lambda performed: performed.update({"one_step_only": False}),
            )
            self.assert_blocked(result, "ADMISSION_SCOPE_EXCEEDED")

    def test_refuses_mutation_replay_or_merge_detected(self) -> None:
        for field in ("mutation_performed", "replay_performed", "merge_performed"):
            with self.subTest(field=field), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(
                    Path(raw_root),
                    mutate_performed=lambda performed, key=field: performed.update({key: True}),
                )
                self.assert_blocked(result, "MUTATION_REPLAY_MERGE_DETECTED")

    def test_refuses_overwrite_extra_output_or_broadened_scope(self) -> None:
        cases = {
            "overwrite": lambda performed: performed.update({"overwrite_performed": True}),
            "extra_output": lambda performed: performed.update(
                {"extra_output_paths": ["artifacts/performed/extra.json"]}
            ),
            "broadened_scope": lambda performed: performed.update({"scope_broadened": True}),
        }
        for label, mutate in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate)
                self.assert_blocked(result, "OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED")

    def test_refuses_derivative_api_operator_authority_upgrade(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(
                Path(raw_root),
                mutate_performed=lambda performed: performed.update(
                    {"derivative_api_operator_authority_upgraded": True}
                ),
            )
            self.assert_blocked(result, "DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED")

    def test_refuses_current_governing_basis_from_derivative_operator_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def mutate(admission: dict[str, Any]) -> None:
                admission["selected_reentry_request"]["hierarchy_constraints"][
                    "current_governing_basis_source"
                ] = "derivative API operator surfaces"

            result, _stack = self.resolve_valid(Path(raw_root), mutate_admission=mutate)
            self.assert_blocked(
                result,
                "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
            )

    def test_refuses_open_completed_and_blocked_hidden(self) -> None:
        cases = {
            "open": ("open_surfaces_completed", "OPEN_SURFACE_TREATED_AS_COMPLETED"),
            "blocked": ("blocked_refused_surfaces_hidden", "BLOCKED_REFUSED_SURFACE_HIDDEN"),
        }
        for label, (field, block_code) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(
                    Path(raw_root),
                    mutate_performed=lambda performed, key=field: performed.update({key: True}),
                )
                self.assert_blocked(result, block_code)

    def test_refuses_non_claim_missing_or_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def mutate_admission(admission: dict[str, Any]) -> None:
                admission["non_claims"]["authority_created"] = True

            result, _stack = self.resolve_valid(Path(raw_root), mutate_admission=mutate_admission)
            self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")

        with tempfile.TemporaryDirectory() as raw_root:
            def mutate_performed(performed: dict[str, Any]) -> None:
                performed["non_claims"] = {"source_replaced": True}

            result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate_performed)
            self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_refuses_follow_on_authorization_and_general_permission(self) -> None:
        cases = {
            "follow_on": ("follow_on_steps_authorized", "FOLLOW_ON_AUTHORIZATION_ATTEMPTED"),
            "general": ("general_permission_created", "GENERAL_CONTINUATION_PERMISSION_ATTEMPTED"),
        }
        for label, (field, block_code) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(
                    Path(raw_root),
                    mutate_performed=lambda performed, key=field: performed.update({key: True}),
                )
                self.assert_blocked(result, block_code)

    def test_refuses_admission_not_exhausted_or_reusable_permission(self) -> None:
        cases = {
            "not_exhausted": (
                lambda performed: performed.update({"admission_exhausted": False}),
                "ADMISSION_NOT_EXHAUSTED",
            ),
            "reusable": (
                lambda performed: performed.update({"admission_reusable": True}),
                "REUSABLE_PERMISSION_IMPLIED",
            ),
            "reusable_implied": (
                lambda performed: performed.update({"reusable_permission_implied": True}),
                "REUSABLE_PERMISSION_IMPLIED",
            ),
        }
        for label, (mutate, block_code) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate)
                self.assert_blocked(result, block_code)

    def test_refuses_latest_file_recency_and_human_narration_fallback(self) -> None:
        cases = {
            "recency": (
                lambda performed: performed.update({"selection_note": "latest file substitution"}),
                "LATEST_FILE_RECENCY_REFUSED",
            ),
            "human_narration": (
                lambda performed: performed.update({"evidence_kind": "human narration"}),
                "HUMAN_NARRATION_FALLBACK_REFUSED",
            ),
        }
        for label, (mutate, block_code) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(Path(raw_root), mutate_performed=mutate)
                self.assert_blocked(result, block_code)

    def test_refuses_roadmap_autonomy_or_workflow_leakage(self) -> None:
        cases = ("roadmap", "autonomous continuation", "workflow machinery", "signaling regulation")
        for phrase in cases:
            with self.subTest(phrase=phrase), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_valid(
                    Path(raw_root),
                    mutate_performed=lambda performed, text=phrase: performed.update(
                        {"closure_statement": text}
                    ),
                )
                self.assert_blocked(result, "GENERAL_CONTINUATION_PERMISSION_ATTEMPTED")

    def test_exhaustion_closure_principle_is_explicit_in_success(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, stack = self.resolve_valid(Path(raw_root))

        selected = result["selected_performed_step"]
        summary = result["current_self_orientation_reentry_receipt_summary"]
        self.assertEqual(stack["next_step"]["next_step_family"], selected["performed_step_family"])
        self.assertEqual(stack["next_step"]["next_step_kind"], selected["performed_step_kind"])
        self.assertTrue(selected["admission_exhausted"])
        self.assertFalse(selected["admission_reusable"])
        self.assertFalse(selected["follow_on_steps_authorized"])
        self.assertTrue(summary["exhaustion_closure_passed"])
        self.assertTrue(summary["scope_stayed_single_step_and_additive"])

    def test_non_claims_remain_false(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_valid(Path(raw_root))

        non_claims = result["non_claims"]
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False)

    def test_non_mutation_of_admissibility_locked_basis_and_performed_artifacts(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            basis_root = temp_root / "artifacts"
            before_tree = tree_digest(basis_root)
            admission_before = file_digest(stack["admission_path"])
            performed_before = file_digest(stack["performed_path"])
            admission_input = copy.deepcopy(stack["admission"])
            performed_input = copy.deepcopy(stack["performed"])

            with self.patched_repo_root(temp_root):
                first = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step_path=stack["performed_rel"],
                )
                second = receipt.resolve_current_self_orientation_reentry_receipt_from_path(
                    stack["admission_rel"],
                    performed_step_path=stack["performed_rel"],
                )
            self.assert_received(first)
            self.assert_received(second)
            self.assertEqual(admission_before, file_digest(stack["admission_path"]))
            self.assertEqual(performed_before, file_digest(stack["performed_path"]))
            self.assertEqual(before_tree, tree_digest(basis_root))
            self.assertEqual(admission_input, stack["admission"])
            self.assertEqual(performed_input, stack["performed"])

    def test_write_helper_writes_valid_json_and_preserves_sections(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            result, _stack = self.resolve_valid(temp_root)
            output_path = temp_root / "nested/output/reentry_receipt_result.json"
            written = receipt.write_current_self_orientation_reentry_receipt_result(
                result,
                output_path,
            )
            loaded = read_json(written)

        self.assertEqual(output_path, written)
        self.assertEqual(EXPECTED_RESULT_KEYS, set(loaded))
        self.assertEqual("REENTRY_RECEIVED", loaded["outcome"])

    def test_default_output_path_is_bounded_additive_and_not_silent_overwrite(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            result, _stack = self.resolve_valid(temp_root)
            with self.patched_repo_root(temp_root):
                first = receipt.write_current_self_orientation_reentry_receipt_result(result)
                second = receipt.write_current_self_orientation_reentry_receipt_result(result)
                self.assertTrue(first.exists())
                self.assertTrue(second.exists())
                self.assertNotEqual(first, second)
                expected_root = temp_root / receipt.CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT
                self.assertTrue(first.is_relative_to(expected_root))
                self.assertTrue(second.is_relative_to(expected_root))
                self.assertTrue(first.name.endswith("__reentry_receipt_result.json"))
                self.assertTrue(second.name.endswith(".json"))

    def test_all_block_codes_are_explicit_receipt_block_codes(self) -> None:
        expected = {
            "ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED",
            "ADMISSIBILITY_RESULT_UNREADABLE",
            "ADMISSIBILITY_RESULT_MALFORMED",
            "ADMISSIBILITY_RESULT_BASIS_THIN",
            "LOCKED_ADMITTED_BASIS_MISSING",
            "LOCKED_ADMITTED_BASIS_MISMATCH",
            "LOCKED_UPSTREAM_BASIS_UNREADABLE",
            "PERFORMED_STEP_MISSING",
            "PERFORMED_STEP_UNREADABLE",
            "PERFORMED_STEP_MALFORMED",
            "PERFORMED_STEP_FAMILY_MISMATCH",
            "PERFORMED_STEP_KIND_MISMATCH",
            "TARGET_SURFACE_MISMATCH",
            "EXPECTED_OUTPUT_FAMILY_MISMATCH",
            "ADMISSION_SCOPE_EXCEEDED",
            "MUTATION_REPLAY_MERGE_DETECTED",
            "OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED",
            "DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED",
            "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
            "OPEN_SURFACE_TREATED_AS_COMPLETED",
            "BLOCKED_REFUSED_SURFACE_HIDDEN",
            "NON_CLAIM_MISSING_OR_FLIPPED",
            "FOLLOW_ON_AUTHORIZATION_ATTEMPTED",
            "GENERAL_CONTINUATION_PERMISSION_ATTEMPTED",
            "ADMISSION_NOT_EXHAUSTED",
            "REUSABLE_PERMISSION_IMPLIED",
            "LATEST_FILE_RECENCY_REFUSED",
            "HUMAN_NARRATION_FALLBACK_REFUSED",
        }
        self.assertTrue(expected <= set(receipt.BLOCK_REASONS))


if __name__ == "__main__":
    unittest.main()
