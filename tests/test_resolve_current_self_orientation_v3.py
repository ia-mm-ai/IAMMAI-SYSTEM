"""Bounded tests for current self-orientation v3.

This suite exercises ``src/resolve_current_self_orientation_v3.py`` as one
lineage-preserving successor to v2. V3 keeps the v2 self-orientation
architecture intact and adds only downstream recognition of a closed re-entry
cycle:

- one ``REENTRY_ADMITTED`` admissibility result
- one matching ``REENTRY_RECEIVED`` receipt result
- exhausted admission
- no follow-on authorization
- no reusable admission
- no workflow-lane or general-permission upgrade

This is not a re-entry admissibility suite, a receipt suite, a workflow engine
harness, a roadmap/autonomy test, a signaling/regulation test, or a manifesto.
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


import resolve_current_self_orientation_reentry_admissibility as reentry_admissibility
import resolve_current_self_orientation_reentry_receipt as reentry_receipt
import resolve_current_self_orientation_v2 as orientation_v2
import resolve_current_self_orientation_v3 as orientation_v3


EXPECTED_RESULT_KEYS = {
    "current_self_orientation_v3_metadata",
    "selected_orientation_inputs",
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
    "bounded_correspondence_checks",
    "outcome",
    "block",
    "self_orientation_basis",
    "current_self_orientation_summary",
    "non_claims",
}

V2_RECOGNITION_KEYS = {
    "recognized_current_executable_core_line",
    "recognized_governing_effective_basis",
    "recognized_current_state_surfaces",
    "recognized_continuity_surfaces",
    "recognized_derivative_surfaces",
    "recognized_operator_facing_surfaces",
    "recognized_open_surfaces",
    "recognized_blocked_or_refused_surfaces",
    "recognized_touch_admissibility_surfaces",
}

REQUIRED_V3_CHECK_NAMES = {
    "reentry_admissibility_is_admitted",
    "reentry_receipt_is_received",
    "reentry_receipt_matches_selected_admissibility",
    "reentry_admissibility_matches_selected_self_orientation_v2",
    "reentry_admissibility_locked_basis_matches_selected_current_basis",
    "reentry_receipt_locked_basis_matches_selected_current_basis",
    "reentry_receipt_basis_lock_matched",
    "reentry_receipt_performed_step_correspondence_passed",
    "reentry_receipt_scope_stayed_single_step_and_additive",
    "reentry_receipt_exhaustion_closure_passed",
    "reentry_receipt_has_no_failed_checks",
    "reentry_receipt_does_not_leak_follow_on_permission",
    "reentry_receipt_does_not_leak_general_permission",
    "reentry_receipt_does_not_leak_reusable_admission",
    "reentry_surfaces_remain_non_authoritative",
    "closed_reentry_cycle_is_not_workflow_lane",
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
    "self_orientation_became_authority",
    "reentry_admissibility_became_authority",
    "receipt_became_authority",
    "reentry_cycle_became_workflow_lane",
    "latest_file_currentness",
    "recency_fraud",
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


class CurrentSelfOrientationV3Tests(unittest.TestCase):
    maxDiff = None
    _live_result_cache: dict[str, Any] | None = None

    def live_result(self) -> dict[str, Any]:
        cls = type(self)
        if cls._live_result_cache is None:
            cls._live_result_cache = orientation_v3.resolve_current_self_orientation()
        return copy.deepcopy(cls._live_result_cache)

    def relative_path(self, temp_root: Path, path: Path | str) -> str:
        return str(Path(path).resolve().relative_to(temp_root.resolve()))

    def patched_repo_root(self, temp_root: Path) -> mock._patch:
        return mock.patch.object(orientation_v3, "_repo_root", return_value=temp_root)

    def non_claims(self) -> dict[str, bool]:
        return {key: False for key in orientation_v3.NON_CLAIM_DEFAULTS}

    def basis_paths(self, temp_root: Path) -> dict[str, Path]:
        return {
            "body_pass": temp_root / orientation_v3.V0_BODY_PASS_ROOT / "body_pass.json",
            "source": temp_root / "artifacts/current_state/what_stands_now.json",
            "answer": temp_root / "artifacts/current_state/answer_read.json",
            "stand": temp_root / "artifacts/current_state/what_stands_now.json",
            "authority": temp_root / "artifacts/effective/authority.json",
            "family": temp_root / "artifacts/effective/family.json",
            "status": temp_root / "artifacts/effective/status.json",
            "governing": temp_root / "artifacts/effective/governing.json",
            "source_run": temp_root / "artifacts/runs/source_run",
            "ingress_run": temp_root / "artifacts/runs/ingress_run",
            "v2": temp_root / orientation_v3.CURRENT_SELF_ORIENTATION_V2_ROOT / "self_orientation_v2.json",
            "admissibility": (
                temp_root
                / orientation_v3.CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT
                / "reentry_admitted.json"
            ),
            "receipt": (
                temp_root
                / orientation_v3.CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT
                / "reentry_received.json"
            ),
        }

    def write_basis_marker_files(self, paths: Mapping[str, Path]) -> None:
        for name in (
            "source",
            "answer",
            "stand",
            "authority",
            "family",
            "status",
            "governing",
        ):
            write_json(paths[name], {"artifact": name, "outcome": "PRESENT"})
        paths["source_run"].mkdir(parents=True, exist_ok=True)
        paths["ingress_run"].mkdir(parents=True, exist_ok=True)

    def effective_references(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
    ) -> dict[str, str]:
        return {
            "effective_authority_artifact_path": self.relative_path(temp_root, paths["authority"]),
            "effective_family_packet_path": self.relative_path(temp_root, paths["family"]),
            "effective_status_packet_path": self.relative_path(temp_root, paths["status"]),
            "effective_current_governing_packet_path": self.relative_path(temp_root, paths["governing"]),
            "effective_source_run_path": self.relative_path(temp_root, paths["source_run"]),
            "effective_ingress_run_path": self.relative_path(temp_root, paths["ingress_run"]),
        }

    def identity(
        self,
        *,
        result_id: str,
        result_path: str,
        result_family: str,
        outcome: str,
        result_type: str | None = None,
        result_version: str | None = "0.1.0",
        resolver_module: str | None = None,
        source_surface_id: str | None = None,
        source_surface_family: str | None = None,
    ) -> dict[str, Any]:
        return {
            "result_id": result_id,
            "result_path": result_path,
            "result_type": result_type,
            "result_version": result_version,
            "resolver_module": resolver_module,
            "outcome": outcome,
            "result_family": result_family,
            "source_surface_id": source_surface_id,
            "source_surface_family": source_surface_family,
        }

    def body_pass_result(self, body_id: str) -> dict[str, Any]:
        return {
            "v0_body_pass_metadata": {
                "v0_body_pass_result_id": body_id,
                "v0_body_pass_result_type": "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT",
                "v0_body_pass_result_version": "0.1.0",
                "generated_at": "2026-04-25T00:00:00Z",
                "runner_module": "run_integrity_host_v0_min_coexistence_v0_body_pass",
            },
            "outcome": orientation_v3.OUTCOME_BODY_PASS_CONFIRMED,
            "block": {"block_code": None, "block_reason": None},
            "non_claims": self.non_claims(),
        }

    def locked_basis(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
        ids: Mapping[str, str],
        effective_refs: Mapping[str, str],
    ) -> dict[str, str]:
        return {
            "selected_body_pass_result_id": ids["body_pass"],
            "selected_body_pass_result_path": self.relative_path(temp_root, paths["body_pass"]),
            "selected_source_surface_id": ids["source"],
            "selected_source_surface_path": self.relative_path(temp_root, paths["stand"]),
            "selected_current_state_answer_read_id": ids["answer"],
            "selected_current_state_answer_read_path": self.relative_path(temp_root, paths["answer"]),
            "selected_what_stands_now_id": ids["source"],
            "selected_what_stands_now_path": self.relative_path(temp_root, paths["stand"]),
            **dict(effective_refs),
        }

    def v2_result(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
        ids: Mapping[str, str],
        effective_refs: Mapping[str, str],
    ) -> dict[str, Any]:
        body = self.identity(
            result_id=ids["body_pass"],
            result_path=self.relative_path(temp_root, paths["body_pass"]),
            result_family="v0_body_pass_result",
            outcome=orientation_v3.OUTCOME_BODY_PASS_CONFIRMED,
            result_type="IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_V0_BODY_PASS_RESULT",
        )
        answer = self.identity(
            result_id=ids["answer"],
            result_path=self.relative_path(temp_root, paths["answer"]),
            result_family="current_state_answer_read_result",
            outcome="ANSWERED",
        )
        stand = self.identity(
            result_id=ids["source"],
            result_path=self.relative_path(temp_root, paths["stand"]),
            result_family="current_state_what_stands_now_result",
            outcome="ANSWERED_WHAT_STANDS_NOW",
            source_surface_id=ids["answer"],
            source_surface_family="current_state_answer_read_result",
        )
        open_surface = self.identity(
            result_id=ids["open"],
            result_path="artifacts/current_state/open.json",
            result_family="current_state_what_remains_open_result",
            outcome="ANSWERED_WHAT_REMAINS_OPEN",
            source_surface_id=ids["answer"],
            source_surface_family="current_state_answer_read_result",
        )
        return {
            "current_self_orientation_v2_metadata": {
                "self_orientation_result_id": ids["v2"],
                "self_orientation_result_type": orientation_v3.SELF_ORIENTATION_V2_RESULT_TYPE,
                "self_orientation_result_version": "0.2.0",
                "generated_at": "2026-04-25T00:00:00Z",
                "resolver_module": orientation_v3.SELF_ORIENTATION_V2_RESOLVER_MODULE,
                "successor_of_module": "resolve_current_self_orientation",
            },
            "selected_orientation_inputs": {
                "selected_body_pass_result": body,
                "selected_source_surface": stand,
                "selected_current_state_answer_read_result": answer,
                "selected_current_state_what_stands_now_result": stand,
                "selected_current_state_what_remains_open_results": [open_surface],
                "selected_current_state_query_results": [],
                "selected_seam_result": self.identity(
                    result_id=ids["seam"],
                    result_path="artifacts/continuity/seam.json",
                    result_family="continuity_memory_seam_result",
                    outcome="SEAM_CLOSED",
                ),
                "selected_action_permission_result": self.identity(
                    result_id=ids["action"],
                    result_path="artifacts/derivative/action.json",
                    result_family="received_derivative_action_permission_result",
                    outcome="ACTION_PERMITTED",
                ),
                "selected_participation_result": self.identity(
                    result_id=ids["participation"],
                    result_path="artifacts/derivative/participation.json",
                    result_family="received_derivative_participation_result",
                    outcome="PARTICIPATED",
                ),
                "selected_receipt_result": self.identity(
                    result_id=ids["transfer_receipt"],
                    result_path="artifacts/continuity/receipt.json",
                    result_family="continuity_transfer_receipt_result",
                    outcome="RECEIVED",
                ),
                "selected_transfer_result": self.identity(
                    result_id=ids["transfer"],
                    result_path="artifacts/continuity/transfer.json",
                    result_family="continuity_transfer_unit_result",
                    outcome="TRANSFERRED",
                ),
                "selected_touch_permission_result": self.identity(
                    result_id=ids["touch"],
                    result_path="artifacts/touch/touch.json",
                    result_family="current_state_touch_permission_result",
                    outcome="ADMITTED_FOR_TOUCH",
                ),
                "selected_vessel_results": [
                    self.identity(
                        result_id=ids["vessel"],
                        result_path="artifacts/vessel/vessel.json",
                        result_family="openai_api_derivative_vessel_bounded_current_state_read_v3_result",
                        outcome="ANSWERED_DERIVATIVE_READ",
                        source_surface_id=ids["source"],
                        source_surface_family="current_state_what_stands_now_result",
                    )
                ],
                "selected_operator_terminal_brief_results": [
                    self.identity(
                        result_id=ids["brief"],
                        result_path="artifacts/operator/brief.json",
                        result_family="operator_terminal_brief_result",
                        outcome="BRIEF_RENDERED",
                        source_surface_id=ids["source"],
                        source_surface_family="current_state_what_stands_now_result",
                    )
                ],
                "selected_effective_references": dict(effective_refs),
            },
            "recognized_current_executable_core_line": {
                "recognized_from_standing_body_pass": True,
                "selected_body_pass_result_id": ids["body_pass"],
            },
            "recognized_governing_effective_basis": {
                "recognized_from_explicit_effective_references": True,
                "effective_references": dict(effective_refs),
                "governing_source": "upstream current/effective/current-state surfaces",
            },
            "recognized_current_state_surfaces": {
                "current_state_answer_read_result": answer,
                "current_state_what_stands_now_result": stand,
                "current_state_what_remains_open_results": [open_surface],
            },
            "recognized_continuity_surfaces": {
                "continuity_transfer_unit_result": {"result_id": ids["transfer"]},
                "continuity_transfer_receipt_result": {"result_id": ids["transfer_receipt"]},
                "continuity_memory_seam_result": {"result_id": ids["seam"]},
                "v0_body_pass_result": body,
            },
            "recognized_derivative_surfaces": {
                "received_derivative_participation_result": {"result_id": ids["participation"]},
                "received_derivative_action_permission_result": {"result_id": ids["action"]},
                "openai_api_derivative_vessel_v3_results": [{"result_id": ids["vessel"]}],
            },
            "recognized_operator_facing_surfaces": {
                "operator_terminal_brief_results": [{"result_id": ids["brief"]}]
            },
            "recognized_open_surfaces": {
                "what_remains_open_results": [open_surface],
                "carried_non_claims": self.non_claims(),
            },
            "recognized_blocked_or_refused_surfaces": [
                {
                    "surface_id": "blocked-query-v0",
                    "surface_family": "current_state_query_result",
                    "surface_outcome": "BLOCKED",
                }
            ],
            "recognized_touch_admissibility_surfaces": {
                "current_state_touch_permission_result": {"result_id": ids["touch"]}
            },
            "bounded_correspondence_checks": [
                {"check_name": "v2_current_surfaces_match_source_artifact_posture", "passed": True},
                {"check_name": "v2_derivative_surfaces_remain_derivative", "passed": True},
            ],
            "outcome": orientation_v3.OUTCOME_SELF_ORIENTED,
            "block": {"block_code": None, "block_reason": None},
            "self_orientation_basis": {
                "basis_kind": "synthetic_v2_self_orientation_for_v3_tests",
                "selected_body_pass_result_id": ids["body_pass"],
                "selected_source_surface_id": ids["source"],
                "selected_current_state_answer_read_id": ids["answer"],
                "effective_references": dict(effective_refs),
            },
            "current_self_orientation_summary": {
                "outcome": orientation_v3.OUTCOME_SELF_ORIENTED,
                "selected_body_pass_result_id": ids["body_pass"],
                "selected_source_surface_id": ids["source"],
            },
            "non_claims": self.non_claims(),
        }

    def admissibility_result(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
        ids: Mapping[str, str],
        locked_basis: Mapping[str, str],
    ) -> dict[str, Any]:
        next_step = self.admitted_next_step(ids)
        return {
            "current_self_orientation_reentry_admissibility_metadata": {
                "reentry_admissibility_result_id": ids["admissibility"],
                "reentry_admissibility_result_type": orientation_v3.REENTRY_ADMISSIBILITY_RESULT_TYPE,
                "reentry_admissibility_result_version": "0.1.0",
                "generated_at": "2026-04-25T00:00:00Z",
                "resolver_module": orientation_v3.REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
            },
            "selected_self_orientation_result": {
                "result_id": ids["v2"],
                "result_path": self.relative_path(temp_root, paths["v2"]),
                "result_type": orientation_v3.SELF_ORIENTATION_V2_RESULT_TYPE,
                "result_version": "0.2.0",
                "resolver_module": orientation_v3.SELF_ORIENTATION_V2_RESOLVER_MODULE,
                "outcome": orientation_v3.OUTCOME_SELF_ORIENTED,
            },
            "locked_orientation_basis": copy.deepcopy(dict(locked_basis)),
            "selected_reentry_request": {
                "declared_next_step": next_step,
                "declared_scope_bounds": {
                    "one_step_only": True,
                    "additive_output_only": True,
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
            },
            "reentry_admissibility_checks": [
                {"check_name": "basis_lock_matched", "passed": True},
                {"check_name": "single_step_permission_bounded", "passed": True},
            ],
            "outcome": orientation_v3.OUTCOME_REENTRY_ADMITTED,
            "block": {"block_code": None, "block_reason": None},
            "reentry_admissibility_basis": {
                "admission_scope": "single_declared_step_only",
                "self_orientation_remains_non_authoritative": True,
                "follow_on_steps_authorized": False,
            },
            "current_self_orientation_reentry_admissibility_summary": {
                "outcome": orientation_v3.OUTCOME_REENTRY_ADMITTED,
                "basis_lock_matched": True,
            },
            "non_claims": self.non_claims(),
        }

    def admitted_next_step(self, ids: Mapping[str, str]) -> dict[str, str]:
        return {
            "next_step_family": "TEST_SURFACE",
            "next_step_kind": "CURRENT_SELF_ORIENTATION_V3_TEST_SURFACE",
            "target_surface_family": "CURRENT_SELF_ORIENTATION_V3_TEST",
            "target_surface_path": "tests/test_resolve_current_self_orientation_v3.py",
            "target_surface_id": ids["performed"],
            "declared_purpose": "Audit one bounded post-receipt self-orientation successor.",
            "declared_expected_output_family": "CURRENT_SELF_ORIENTATION_V3_TEST_RESULT",
            "requested_relation_to_basis": "test successor for closed re-entry cycle recognition",
        }

    def receipt_result(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
        ids: Mapping[str, str],
        locked_basis: Mapping[str, str],
    ) -> dict[str, Any]:
        next_step = self.admitted_next_step(ids)
        performed = {
            "performed_step_path": next_step["target_surface_path"],
            "performed_step_id": ids["performed"],
            "performed_step_family": next_step["next_step_family"],
            "performed_step_kind": next_step["next_step_kind"],
            "performed_step_outcome": "PERFORMED",
            "performed_step_type": "IAMMAI_CURRENT_SELF_ORIENTATION_V3_TEST_PERFORMED_STEP",
            "performed_step_generated_at": "2026-04-25T00:00:00Z",
            "performed_step_resolver_or_emitter_module": "test_resolve_current_self_orientation_v3",
            "target_surface_family": next_step["target_surface_family"],
            "target_surface_path": next_step["target_surface_path"],
            "target_surface_id": next_step["target_surface_id"],
            "declared_expected_output_family": next_step["declared_expected_output_family"],
            "admission_exhausted": True,
            "admission_reusable": False,
            "reusable_permission_implied": False,
            "follow_on_steps_authorized": False,
            "general_permission_created": False,
        }
        return {
            "current_self_orientation_reentry_receipt_metadata": {
                "reentry_receipt_result_id": ids["receipt"],
                "reentry_receipt_result_type": orientation_v3.REENTRY_RECEIPT_RESULT_TYPE,
                "reentry_receipt_result_version": "0.1.0",
                "generated_at": "2026-04-25T00:00:00Z",
                "resolver_module": orientation_v3.REENTRY_RECEIPT_RESOLVER_MODULE,
            },
            "selected_reentry_admissibility_result": {
                "result_id": ids["admissibility"],
                "result_path": self.relative_path(temp_root, paths["admissibility"]),
                "result_type": orientation_v3.REENTRY_ADMISSIBILITY_RESULT_TYPE,
                "result_version": "0.1.0",
                "resolver_module": orientation_v3.REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
                "outcome": orientation_v3.OUTCOME_REENTRY_ADMITTED,
            },
            "locked_admitted_basis": copy.deepcopy(dict(locked_basis)),
            "selected_performed_step": performed,
            "reentry_receipt_checks": [
                {"check_name": "basis_lock_matched", "passed": True},
                {"check_name": "performed_step_correspondence_passed", "passed": True},
                {"check_name": "exhaustion_closure_passed", "passed": True},
            ],
            "outcome": orientation_v3.OUTCOME_REENTRY_RECEIVED,
            "block": {"block_code": None, "block_reason": None},
            "reentry_receipt_basis": {
                "admission_exhausted": True,
                "receipt_creates_follow_on_permission": False,
                "admissibility_remains_non_authoritative": True,
            },
            "current_self_orientation_reentry_receipt_summary": {
                "outcome": orientation_v3.OUTCOME_REENTRY_RECEIVED,
                "basis_lock_matched": True,
                "performed_step_correspondence_passed": True,
                "scope_stayed_single_step_and_additive": True,
                "exhaustion_closure_passed": True,
                "failed_check_count": 0,
            },
            "non_claims": self.non_claims(),
        }

    def build_stack(
        self,
        temp_root: Path,
        *,
        include_admissibility: bool = True,
        include_receipt: bool = True,
    ) -> dict[str, Any]:
        paths = self.basis_paths(temp_root)
        self.write_basis_marker_files(paths)
        effective_refs = self.effective_references(temp_root, paths)
        ids = {
            "body_pass": "body-pass-v3-test-001",
            "v2": "self-orientation-v2-test-001",
            "source": "what-stands-now-v3-test-001",
            "answer": "answer-read-v3-test-001",
            "open": "what-remains-open-v3-test-001",
            "touch": "touch-v3-test-001",
            "transfer": "transfer-v3-test-001",
            "transfer_receipt": "transfer-receipt-v3-test-001",
            "participation": "participation-v3-test-001",
            "action": "action-v3-test-001",
            "seam": "seam-v3-test-001",
            "vessel": "vessel-v3-test-001",
            "brief": "brief-v3-test-001",
            "admissibility": "reentry-admissibility-v3-test-001",
            "receipt": "reentry-receipt-v3-test-001",
            "performed": "performed-v3-test-001",
        }
        body = self.body_pass_result(ids["body_pass"])
        v2_result = self.v2_result(temp_root, paths, ids, effective_refs)
        basis = self.locked_basis(temp_root, paths, ids, effective_refs)
        admissibility = self.admissibility_result(temp_root, paths, ids, basis)
        receipt = self.receipt_result(temp_root, paths, ids, basis)
        write_json(paths["body_pass"], body)
        write_json(paths["v2"], v2_result)
        if include_admissibility:
            write_json(paths["admissibility"], admissibility)
        if include_receipt:
            write_json(paths["receipt"], receipt)
        return {
            "paths": paths,
            "ids": ids,
            "body": body,
            "v2": v2_result,
            "basis": basis,
            "admissibility": admissibility,
            "receipt": receipt,
        }

    def resolve_stack(
        self,
        temp_root: Path,
        *,
        mutate_admissibility: Callable[[dict[str, Any]], None] | None = None,
        mutate_receipt: Callable[[dict[str, Any]], None] | None = None,
        include_admissibility: bool = True,
        include_receipt: bool = True,
        from_path: bool = False,
    ) -> tuple[dict[str, Any], dict[str, Any]]:
        stack = self.build_stack(
            temp_root,
            include_admissibility=include_admissibility,
            include_receipt=include_receipt,
        )
        if mutate_admissibility is not None:
            mutate_admissibility(stack["admissibility"])
            write_json(stack["paths"]["admissibility"], stack["admissibility"])
        if mutate_receipt is not None:
            mutate_receipt(stack["receipt"])
            write_json(stack["paths"]["receipt"], stack["receipt"])
        with self.patched_repo_root(temp_root):
            if from_path:
                result = orientation_v3.resolve_current_self_orientation_from_path(
                    self.relative_path(temp_root, stack["paths"]["body_pass"])
                )
            else:
                result = orientation_v3.resolve_current_self_orientation()
        return result, stack

    def assert_self_oriented(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(orientation_v3.OUTCOME_SELF_ORIENTED, result["outcome"])
        self.assertEqual({"block_code": None, "block_reason": None}, result["block"])
        self.assertNotIn("roadmap", result)
        self.assertNotIn("workflow", result)
        self.assertNotIn("external_reader_orientation", result)

    def assert_blocked(
        self,
        result: Mapping[str, Any],
        expected_codes: str | set[str],
    ) -> None:
        expected = {expected_codes} if isinstance(expected_codes, str) else expected_codes
        self.assertEqual(orientation_v3.OUTCOME_BLOCKED, result["outcome"])
        self.assertIn(result.get("block", {}).get("block_code"), expected)
        self.assertIsInstance(result.get("block", {}).get("block_reason"), str)

    def assert_reentry_closed(self, result: Mapping[str, Any]) -> None:
        reentry = result["recognized_reentry_surfaces"]
        closure = reentry["closure_posture"]
        self.assertEqual("downstream_closed_reentry_cycle_only", reentry["recognition_posture"])
        self.assertEqual(
            orientation_v3.OUTCOME_REENTRY_ADMITTED,
            reentry["selected_reentry_admissibility_result"]["outcome"],
        )
        self.assertEqual(
            orientation_v3.OUTCOME_REENTRY_RECEIVED,
            reentry["selected_reentry_receipt_result"]["outcome"],
        )
        self.assertTrue(closure["basis_lock_matched"])
        self.assertTrue(closure["performed_step_correspondence_passed"])
        self.assertTrue(closure["scope_stayed_single_step_and_additive"])
        self.assertTrue(closure["exhaustion_closure_passed"])
        self.assertEqual(0, closure["failed_check_count"])
        self.assertFalse(closure["follow_on_steps_authorized"])
        self.assertFalse(closure["general_permission_created"])
        self.assertFalse(closure["admission_reusable"])
        self.assertFalse(closure["receipt_became_authority"])
        self.assertFalse(closure["reentry_admissibility_became_authority"])
        self.assertFalse(closure["workflow_lane_created"])

    def test_import_posture_keeps_successor_surfaces_importable(self) -> None:
        self.assertTrue(hasattr(orientation_v2, "resolve_current_self_orientation"))
        self.assertTrue(hasattr(reentry_admissibility, "resolve_current_self_orientation_reentry_admissibility"))
        self.assertTrue(hasattr(reentry_receipt, "resolve_current_self_orientation_reentry_receipt"))
        self.assertTrue(hasattr(orientation_v3, "resolve_current_self_orientation"))

    def test_real_self_oriented_v3_path_returns_bounded_internal_recognition(self) -> None:
        result = self.live_result()
        self.assertIsInstance(result, dict)
        self.assert_self_oriented(result)
        self.assert_reentry_closed(result)
        self.assertEqual(
            "v2_self_orientation_plus_closed_reentry_cycle",
            result["self_orientation_basis"]["basis_kind"],
        )

    def test_metadata_is_successor_specific(self) -> None:
        result = self.live_result()
        metadata = result["current_self_orientation_v3_metadata"]
        for key in (
            "self_orientation_result_id",
            "self_orientation_result_type",
            "self_orientation_result_version",
            "generated_at",
            "resolver_module",
            "successor_of_module",
        ):
            self.assertIsInstance(metadata.get(key), str)
            self.assertTrue(metadata[key])
        self.assertEqual(orientation_v3.CURRENT_SELF_ORIENTATION_RESULT_TYPE, metadata["self_orientation_result_type"])
        self.assertEqual(orientation_v3.CURRENT_SELF_ORIENTATION_RESULT_VERSION, metadata["self_orientation_result_version"])
        self.assertEqual(orientation_v3.RESOLVER_MODULE, metadata["resolver_module"])
        self.assertEqual("resolve_current_self_orientation_v2", metadata["successor_of_module"])

    def test_selected_inputs_preserve_v2_and_reentry_basis_without_repo_wide_authority_scan(self) -> None:
        result = self.live_result()
        selected = result["selected_orientation_inputs"]
        for key in (
            "selected_body_pass_result",
            "selected_self_orientation_v2_result",
            "selected_reentry_admissibility_result",
            "selected_reentry_receipt_result",
            "selected_source_surface",
            "selected_current_state_answer_read_result",
            "selected_current_state_what_stands_now_result",
            "selected_effective_references",
        ):
            self.assertIsInstance(selected.get(key), dict)
            self.assertTrue(selected[key])
        self.assertFalse(selected["selection_scope"]["repo_wide_authority_scan_performed"])
        self.assertTrue(selected["selection_scope"]["reentry_surfaces_are_downstream_only"])

    def test_v2_recognition_sections_remain_distinct(self) -> None:
        result = self.live_result()
        for key in V2_RECOGNITION_KEYS:
            self.assertIn(key, result)
            self.assertNotEqual({}, result[key], key)
        self.assertNotEqual(result["recognized_governing_effective_basis"], result["recognized_reentry_surfaces"])
        self.assertNotEqual(result["recognized_derivative_surfaces"], result["recognized_operator_facing_surfaces"])

    def test_current_governing_basis_remains_upstream_derived(self) -> None:
        result = self.live_result()
        governing = result["recognized_governing_effective_basis"]
        checks = {check["check_name"]: check for check in result["bounded_correspondence_checks"]}
        self.assertNotIn("selected_reentry_admissibility_result", governing)
        self.assertNotIn("selected_reentry_receipt_result", governing)
        self.assertTrue(checks["reentry_surfaces_do_not_determine_current_governing_basis"]["passed"])
        self.assertTrue(result["selected_orientation_inputs"]["selection_scope"]["reentry_surfaces_are_downstream_only"])

    def test_reentry_recognition_preserves_admission_receipt_step_and_closure(self) -> None:
        result = self.live_result()
        reentry = result["recognized_reentry_surfaces"]
        self.assertTrue(reentry["selected_reentry_admissibility_result"]["result_id"])
        self.assertTrue(reentry["selected_reentry_admissibility_result"]["result_path"])
        self.assertTrue(reentry["selected_reentry_receipt_result"]["result_id"])
        self.assertTrue(reentry["selected_reentry_receipt_result"]["result_path"])
        for section in ("admitted_next_step", "performed_step", "closure_posture"):
            self.assertIsInstance(reentry[section], dict)
            self.assertTrue(reentry[section])
        self.assertIn("next_step_family", reentry["admitted_next_step"])
        self.assertIn("next_step_kind", reentry["admitted_next_step"])
        self.assertIn("target_surface_family", reentry["admitted_next_step"])
        self.assertIn("performed_step_family", reentry["performed_step"])
        self.assertIn("performed_step_kind", reentry["performed_step"])
        self.assert_reentry_closed(result)

    def test_closed_cycle_is_downstream_not_permission_or_workflow(self) -> None:
        result = self.live_result()
        basis = result["self_orientation_basis"]
        closure = result["recognized_reentry_surfaces"]["closure_posture"]
        self.assertTrue(basis["reentry_cycle_recognized_as_downstream_posture"])
        self.assertTrue(basis["receipt_permission_exhausted"])
        self.assertFalse(basis["follow_on_permission_created"])
        self.assertFalse(basis["workflow_lane_created"])
        self.assertFalse(basis["self_orientation_creates_authority"])
        self.assertFalse(closure["general_permission_created"])
        self.assertFalse(closure["admission_reusable"])

    def test_bounded_correspondence_checks_include_v2_and_v3_reentry_checks(self) -> None:
        result = self.live_result()
        check_names = {
            check["check_name"]
            for check in result["bounded_correspondence_checks"]
            if isinstance(check, Mapping)
        }
        self.assertTrue(REQUIRED_V3_CHECK_NAMES <= check_names)
        self.assertTrue(any(name.startswith("v2_") for name in check_names))
        for check in result["bounded_correspondence_checks"]:
            if check["check_name"] in REQUIRED_V3_CHECK_NAMES:
                self.assertIs(check["passed"], True, check["check_name"])

    def test_summary_helper_reports_v3_basis_and_closed_cycle(self) -> None:
        result = self.live_result()
        summary = orientation_v3.build_current_self_orientation_summary(result)
        self.assertEqual(orientation_v3.OUTCOME_SELF_ORIENTED, summary["outcome"])
        self.assertIsNone(summary["block_code"])
        self.assertTrue(summary["selected_body_pass_result_id"])
        self.assertTrue(summary["selected_source_surface_id"])
        self.assertTrue(summary["selected_self_orientation_v2_result_id"])
        self.assertTrue(summary["selected_reentry_admissibility_result_id"])
        self.assertTrue(summary["selected_reentry_receipt_result_id"])
        self.assertTrue(summary["governing_effective_basis_recognized"])
        self.assertTrue(summary["continuity_surfaces_recognized"])
        self.assertTrue(summary["derivative_surfaces_recognized"])
        self.assertTrue(summary["operator_surfaces_recognized"])
        self.assertTrue(summary["reentry_surfaces_recognized"])
        self.assertTrue(summary["reentry_receipt_received"])
        self.assertTrue(summary["reentry_receipt_exhaustion_closure_passed"])
        self.assertTrue(summary["admission_remains_non_reusable"])
        self.assertTrue(summary["follow_on_authorization_remains_false"])
        self.assertTrue(REQUIRED_FALSE_NON_CLAIMS <= set(summary["non_claims"]))

    def test_path_based_resolution_selects_matching_v2_admissibility_and_receipt(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            result, stack = self.resolve_stack(temp_root, from_path=True)

        self.assert_self_oriented(result)
        selected = result["selected_orientation_inputs"]
        self.assertEqual(stack["ids"]["v2"], selected["selected_self_orientation_v2_result"]["result_id"])
        self.assertEqual(stack["ids"]["admissibility"], selected["selected_reentry_admissibility_result"]["result_id"])
        self.assertEqual(stack["ids"]["receipt"], selected["selected_reentry_receipt_result"]["result_id"])
        self.assertNotIn(
            "selected_reentry_receipt_result",
            result["recognized_governing_effective_basis"],
        )

    def test_write_helper_writes_valid_json_and_parent_directories(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            result, _stack = self.resolve_stack(temp_root)
            output_path = temp_root / "nested/output/current_self_orientation_v3.json"
            written = orientation_v3.write_current_self_orientation_result(result, output_path)
            loaded = read_json(written)

        self.assertEqual(output_path, written)
        self.assertEqual(EXPECTED_RESULT_KEYS, set(loaded))
        self.assertEqual(orientation_v3.OUTCOME_SELF_ORIENTED, loaded["outcome"])

    def test_default_output_path_is_bounded_additive_and_never_overwrites(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            result, _stack = self.resolve_stack(temp_root)
            with self.patched_repo_root(temp_root):
                first = orientation_v3.write_current_self_orientation_result(result)
                second = orientation_v3.write_current_self_orientation_result(result)
            with self.assertRaises(FileExistsError):
                orientation_v3.write_current_self_orientation_result(result, first)

        expected_root = temp_root / orientation_v3.CURRENT_SELF_ORIENTATION_V3_ROOT
        self.assertEqual(expected_root, first.parent)
        self.assertEqual(expected_root, second.parent)
        self.assertNotEqual(first, second)
        self.assertTrue(first.name.endswith("__current_self_orientation_v3_result.json"))
        self.assertTrue(second.name.endswith("__current_self_orientation_v3_result_001.json"))

    def test_resolution_is_non_mutating_and_artifact_writes_are_additive_only(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            temp_root = Path(raw_root)
            stack = self.build_stack(temp_root)
            artifact_root = temp_root / "artifacts"
            before_tree = tree_digest(artifact_root)
            v2_digest = file_digest(stack["paths"]["v2"])
            admissibility_digest = file_digest(stack["paths"]["admissibility"])
            receipt_digest = file_digest(stack["paths"]["receipt"])
            body_input = copy.deepcopy(stack["body"])

            with self.patched_repo_root(temp_root):
                first = orientation_v3.resolve_current_self_orientation()
                second = orientation_v3.resolve_current_self_orientation(
                    body_pass_result=body_input
                )
            self.assert_self_oriented(first)
            self.assert_self_oriented(second)
            self.assertEqual(before_tree, tree_digest(artifact_root))
            self.assertEqual(v2_digest, file_digest(stack["paths"]["v2"]))
            self.assertEqual(admissibility_digest, file_digest(stack["paths"]["admissibility"]))
            self.assertEqual(receipt_digest, file_digest(stack["paths"]["receipt"]))
            self.assertEqual(stack["body"], body_input)

    def test_refuses_no_matching_reentry_admissibility_without_inventing_posture(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, _stack = self.resolve_stack(
                Path(raw_root),
                include_admissibility=False,
                include_receipt=False,
            )
        self.assert_blocked(result, "REENTRY_ADMISSIBILITY_UNREADABLE")
        self.assertEqual({}, result["recognized_reentry_surfaces"])
        self.assertEqual({}, result["selected_orientation_inputs"]["selected_reentry_admissibility_result"])

    def test_refuses_reentry_admissibility_not_admitted_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def not_admitted(admission: dict[str, Any]) -> None:
                admission["outcome"] = "BLOCKED"
                admission["block"] = {"block_code": "TEST_BLOCK", "block_reason": "blocked"}

            blocked, _stack = self.resolve_stack(Path(raw_root), mutate_admissibility=not_admitted)

        with tempfile.TemporaryDirectory() as raw_root:
            def malformed(admission: dict[str, Any]) -> None:
                admission["current_self_orientation_reentry_admissibility_metadata"][
                    "reentry_admissibility_result_type"
                ] = "WRONG_TYPE"

            malformed_result, _stack = self.resolve_stack(Path(raw_root), mutate_admissibility=malformed)

        self.assert_blocked(
            blocked,
            {"REENTRY_ADMISSIBILITY_UNREADABLE", "REENTRY_ADMISSIBILITY_NOT_ADMITTED"},
        )
        self.assert_blocked(
            malformed_result,
            {"REENTRY_ADMISSIBILITY_UNREADABLE", "REENTRY_ADMISSIBILITY_MALFORMED"},
        )

    def test_refuses_no_matching_reentry_receipt_without_inventing_closure(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            result, stack = self.resolve_stack(Path(raw_root), include_receipt=False)

        self.assert_blocked(result, "REENTRY_RECEIPT_UNREADABLE")
        selected = result["selected_orientation_inputs"]
        if selected.get("selected_reentry_admissibility_result"):
            self.assertEqual(
                stack["ids"]["admissibility"],
                selected["selected_reentry_admissibility_result"]["result_id"],
            )
        self.assertNotEqual(
            True,
            result["recognized_reentry_surfaces"].get("closure_posture", {}).get(
                "exhaustion_closure_passed"
            ),
        )

    def test_refuses_reentry_receipt_not_received_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as raw_root:
            def not_received(receipt: dict[str, Any]) -> None:
                receipt["outcome"] = "BLOCKED"
                receipt["block"] = {"block_code": "TEST_BLOCK", "block_reason": "blocked"}

            blocked, _stack = self.resolve_stack(Path(raw_root), mutate_receipt=not_received)

        with tempfile.TemporaryDirectory() as raw_root:
            def malformed(receipt: dict[str, Any]) -> None:
                receipt["current_self_orientation_reentry_receipt_metadata"][
                    "reentry_receipt_result_type"
                ] = "WRONG_TYPE"

            malformed_result, _stack = self.resolve_stack(Path(raw_root), mutate_receipt=malformed)

        self.assert_blocked(blocked, {"REENTRY_RECEIPT_UNREADABLE", "REENTRY_RECEIPT_NOT_RECEIVED"})
        self.assert_blocked(malformed_result, {"REENTRY_RECEIPT_UNREADABLE", "REENTRY_RECEIPT_MALFORMED"})

    def test_refuses_receipt_or_admissibility_basis_mismatch(self) -> None:
        cases = {
            "admissibility_self_orientation_mismatch": (
                lambda admission: admission["selected_self_orientation_result"].update(
                    {
                        "result_id": "other-v2",
                        "result_path": "artifacts/other/self_orientation_v2.json",
                    }
                ),
                None,
                {"REENTRY_ADMISSIBILITY_UNREADABLE", "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS"},
            ),
            "admissibility_locked_basis_mismatch": (
                lambda admission: admission["locked_orientation_basis"].update(
                    {"selected_source_surface_id": "other-source"}
                ),
                None,
                {"REENTRY_ADMISSIBILITY_UNREADABLE", "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS"},
            ),
            "receipt_selected_admissibility_mismatch": (
                None,
                lambda receipt: receipt["selected_reentry_admissibility_result"].update(
                    {
                        "result_id": "other-admission",
                        "result_path": "artifacts/other/reentry_admitted.json",
                    }
                ),
                {"REENTRY_RECEIPT_UNREADABLE", "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_ADMISSIBILITY"},
            ),
            "receipt_locked_basis_mismatch": (
                None,
                lambda receipt: receipt["locked_admitted_basis"].update(
                    {"selected_source_surface_id": "other-source"}
                ),
                {"REENTRY_RECEIPT_UNREADABLE", "REENTRY_RECEIPT_DOES_NOT_MATCH_SELECTED_SELF_ORIENTATION_BASIS"},
            ),
        }
        for label, (mutate_admission, mutate_receipt, expected) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, _stack = self.resolve_stack(
                    Path(raw_root),
                    mutate_admissibility=mutate_admission,
                    mutate_receipt=mutate_receipt,
                )
                self.assert_blocked(result, expected)

    def test_refuses_failed_receipt_closure_checks_with_specific_codes(self) -> None:
        cases = {
            "basis": (
                lambda receipt: receipt["current_self_orientation_reentry_receipt_summary"].update(
                    {"basis_lock_matched": False}
                ),
                "REENTRY_RECEIPT_BASIS_LOCK_NOT_MATCHED",
            ),
            "correspondence": (
                lambda receipt: receipt["current_self_orientation_reentry_receipt_summary"].update(
                    {"performed_step_correspondence_passed": False}
                ),
                "REENTRY_RECEIPT_PERFORMED_STEP_CORRESPONDENCE_FAILED",
            ),
            "scope": (
                lambda receipt: receipt["current_self_orientation_reentry_receipt_summary"].update(
                    {"scope_stayed_single_step_and_additive": False}
                ),
                "REENTRY_RECEIPT_SCOPE_NOT_SINGLE_STEP_ADDITIVE",
            ),
            "exhaustion": (
                lambda receipt: receipt["current_self_orientation_reentry_receipt_summary"].update(
                    {"exhaustion_closure_passed": False}
                ),
                "REENTRY_RECEIPT_EXHAUSTION_NOT_CLOSED",
            ),
            "admission_exhausted": (
                lambda receipt: receipt["reentry_receipt_basis"].update(
                    {"admission_exhausted": False}
                ),
                "REENTRY_RECEIPT_EXHAUSTION_NOT_CLOSED",
            ),
            "failed_checks": (
                lambda receipt: receipt["current_self_orientation_reentry_receipt_summary"].update(
                    {"failed_check_count": 1}
                ),
                "REENTRY_RECEIPT_FAILED_CHECKS_PRESENT",
            ),
            "follow_on": (
                lambda receipt: receipt["non_claims"].update({"follow_on_steps_authorized": True}),
                {"NON_CLAIM_MISSING_OR_FLIPPED", "REENTRY_RECEIPT_UNREADABLE"},
            ),
            "general_permission": (
                lambda receipt: receipt["non_claims"].update({"general_permission_created": True}),
                {"NON_CLAIM_MISSING_OR_FLIPPED", "REENTRY_RECEIPT_UNREADABLE"},
            ),
            "reusable": (
                lambda receipt: receipt["selected_performed_step"].update(
                    {"reusable_permission_implied": True}
                ),
                "REENTRY_RECEIPT_REUSABLE_ADMISSION_LEAK",
            ),
            "receipt_authority": (
                lambda receipt: receipt["non_claims"].update({"receipt_became_authority": True}),
                {"NON_CLAIM_MISSING_OR_FLIPPED", "REENTRY_RECEIPT_UNREADABLE"},
            ),
            "workflow_lane": (
                lambda receipt: receipt["non_claims"].update(
                    {"reentry_cycle_became_workflow_lane": True}
                ),
                {"NON_CLAIM_MISSING_OR_FLIPPED", "REENTRY_RECEIPT_UNREADABLE"},
            ),
        }
        for label, (mutate, expected_code) in cases.items():
            with self.subTest(label=label), tempfile.TemporaryDirectory() as raw_root:
                result, stack = self.resolve_stack(Path(raw_root), mutate_receipt=mutate)
                self.assert_blocked(result, expected_code)
                selected = result["selected_orientation_inputs"]
                if selected.get("selected_reentry_admissibility_result"):
                    self.assertEqual(
                        stack["ids"]["admissibility"],
                        selected["selected_reentry_admissibility_result"]["result_id"],
                    )
                if selected.get("selected_reentry_receipt_result"):
                    self.assertEqual(
                        stack["ids"]["receipt"],
                        selected["selected_reentry_receipt_result"]["result_id"],
                    )

    def test_non_claims_remain_false_in_success(self) -> None:
        result = self.live_result()
        non_claims = result["non_claims"]
        self.assertTrue(REQUIRED_FALSE_NON_CLAIMS <= set(non_claims))
        for key, value in non_claims.items():
            self.assertIs(value, False, key)


if __name__ == "__main__":
    unittest.main()
