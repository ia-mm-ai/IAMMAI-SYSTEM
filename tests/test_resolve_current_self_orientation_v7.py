"""Tests for bounded current self-orientation v7.

V7 is a narrow successor to v6. It keeps the v6 self-orientation categories
intact and adds only downstream recognition of post-conformance closure,
cross-surface correspondence, and cross-carrier receipt evidence.
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

import resolve_current_self_orientation_v7 as resolver


TOP_LEVEL_SECTIONS = {
    "current_self_orientation_v7_metadata",
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
    "recognized_current_body_conformance_surfaces",
    "recognized_post_conformance_closure_surfaces",
    "recognized_cross_surface_correspondence_surfaces",
    "recognized_cross_carrier_receipt_surfaces",
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

V7_CHECK_NAMES = {
    "self_orientation_v6_stands",
    "self_orientation_v6_is_self_oriented",
    "current_governing_basis_remains_upstream_derived",
    "current_body_conformance_result_is_body_conformant",
    "post_conformance_closure_is_recorded",
    "post_conformance_closure_does_not_create_permission",
    "post_conformance_closure_does_not_create_authority",
    "post_conformance_closure_does_not_create_signal",
    "post_conformance_closure_does_not_authorize_next_work_or_successor",
    "closure_alignment_correspondence_is_recognized_where_selected",
    "local_cross_carrier_receipt_is_received",
    "returned_carrier_b_successful_receipt_is_received",
    "returned_carrier_b_blocked_receipt_refusal_remains_visible",
    "receipt_alignment_correspondence_is_recognized",
    "refusal_visible_correspondence_is_recognized",
    "carrier_b_remains_receiving_carrier_only",
    "carried_surface_remains_carried_evidence_only",
    "receipt_does_not_create_presence_threshold_truth_action_or_consequence",
    "receipt_does_not_create_multi_carrier_law_or_distributed_standing",
    "post_v6_correspondence_and_receipt_surfaces_do_not_determine_current_governing_basis",
    "non_claims_remain_false_and_carried_forward",
    "latest_file_currentness_is_refused",
    "mutation_replay_merge_remain_false",
}

FALSE_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "source_replaced",
    "conformance_became_authority",
    "conformance_became_permission",
    "conformance_became_currentness",
    "closure_became_authority",
    "closure_became_permission",
    "closure_became_signal",
    "correspondence_became_authority",
    "correspondence_became_currentness",
    "correspondence_became_permission",
    "correspondence_became_signal",
    "receipt_became_authority",
    "receipt_became_currentness",
    "receipt_became_source",
    "receiving_carrier_became_source",
    "receiving_carrier_became_current",
    "receiving_carrier_became_authority",
    "receiving_carrier_became_successor",
    "receiving_carrier_became_body",
    "carrier_b_became_source",
    "carrier_b_became_currentness",
    "carrier_b_became_authority",
    "carrier_b_became_successor",
    "carrier_b_became_body",
    "carried_surface_became_source",
    "carried_surface_became_currentness",
    "carried_surface_became_permission",
    "carried_surface_became_signal_by_default",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "consequence_created",
    "continuation_authorized",
    "multi_carrier_law_created",
    "distributed_standing_created",
    "returned_evidence_replaced_source",
    "returned_evidence_created_currentness",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

EXPECTED_BLOCK_CODES = {
    "SELF_ORIENTATION_V6_MISSING",
    "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED",
    "CURRENT_BODY_CONFORMANCE_MISSING",
    "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT",
    "POST_CONFORMANCE_CLOSURE_MISSING",
    "POST_CONFORMANCE_CLOSURE_NOT_RECORDED",
    "CONFORMANCE_CLOSURE_PERMISSION_LEAK",
    "CONFORMANCE_CLOSURE_AUTHORITY_LEAK",
    "CONFORMANCE_CLOSURE_SIGNAL_LEAK",
    "CONFORMANCE_CLOSURE_CONTINUATION_LEAK",
    "CROSS_SURFACE_CORRESPONDENCE_MISSING",
    "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED",
    "CROSS_CARRIER_RECEIPT_MISSING",
    "CROSS_CARRIER_RECEIPT_NOT_RECEIVED",
    "RETURNED_CARRIER_RECEIPT_MISSING",
    "RETURNED_CARRIER_RECEIPT_NOT_RECEIVED",
    "RETURNED_CARRIER_REFUSAL_NOT_VISIBLE",
    "RECEIPT_ALIGNMENT_CORRESPONDENCE_MISSING",
    "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED",
    "REFUSAL_VISIBLE_CORRESPONDENCE_MISSING",
    "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED",
    "RECEIVING_CARRIER_SOURCE_LEAK",
    "RECEIVING_CARRIER_CURRENTNESS_LEAK",
    "RECEIVING_CARRIER_AUTHORITY_LEAK",
    "RECEIVING_CARRIER_SUCCESSOR_LEAK",
    "CARRIED_SURFACE_SOURCE_OR_CURRENTNESS_LEAK",
    "CARRIED_SURFACE_PERMISSION_OR_SIGNAL_LEAK",
    "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK",
    "RECEIPT_MULTI_CARRIER_OR_DISTRIBUTED_STANDING_LEAK",
    "RETURNED_EVIDENCE_REPLACED_SOURCE",
    "RETURNED_EVIDENCE_CREATED_CURRENTNESS",
    "LATEST_FILE_CURRENTNESS_REFUSED",
}

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
        value = json.load(handle)
    assert isinstance(value, dict)
    return value


def _repo_path(path: str | None) -> Path | None:
    if not path:
        return None
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def _snapshot(paths: list[Path]) -> dict[Path, str]:
    return {path: path.read_text(encoding="utf-8") for path in paths if path.exists()}


def _false(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.NON_CLAIM_DEFAULTS)
    claims.update(updates)
    return claims


def _check(name: str) -> dict[str, object]:
    return {
        "check_name": name,
        "passed": True,
        "expected_posture": True,
        "actual_posture": True,
        "block_code": None,
    }


def _v6(outcome: str = "SELF_ORIENTED") -> dict[str, object]:
    return {
        "current_self_orientation_v6_metadata": {
            "self_orientation_result_id": V6_ID,
            "self_orientation_result_type": "current_self_orientation_v6_result",
            "self_orientation_result_version": "0.6.0",
            "generated_at": "2026-04-28T00:00:00Z",
            "resolver_module": "resolve_current_self_orientation_v6",
        },
        "selected_orientation_inputs": {
            "selected_source_surface": {
                "result_id": "upstream_current_state_source_test",
                "outcome": "ANSWERED_WHAT_STANDS_NOW",
            },
            "selected_reentry_receipt_result": {"result_id": "reentry_receipt_test"},
            "selected_body_signal_scope_result": {"result_id": "body_signal_scope_test"},
            "selected_derivative_vessel_relation_boundary_result": {
                "result_id": "derivative_vessel_relation_boundary_test"
            },
            "selection_scope": {"repo_wide_authority_scan_performed": False},
        },
        "recognized_current_executable_core_line": {"recognized": True},
        "recognized_governing_effective_basis": {"basis_source": "upstream_current_state"},
        "recognized_current_state_surfaces": {"recognized": True},
        "recognized_continuity_surfaces": {"recognized": True},
        "recognized_derivative_surfaces": {"recognition_posture": "downstream_only"},
        "recognized_operator_facing_surfaces": {"recognition_posture": "downstream_only"},
        "recognized_reentry_surfaces": {"recognition_posture": "downstream_only"},
        "recognized_body_signal_surfaces": {"recognition_posture": "non_operative"},
        "recognized_derivative_vessel_relation_surfaces": {
            "recognition_posture": "downstream_non_authoritative"
        },
        "recognized_open_surfaces": {"presence_law": "open"},
        "recognized_blocked_or_refused_surfaces": {"refusal_visible": True},
        "recognized_touch_admissibility_surfaces": {"recognition_posture": "admissibility"},
        "bounded_correspondence_checks": [_check("v6_self_orientation_stands")],
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "SELF_ORIENTED"
        else {"block_code": "SYNTHETIC_V6_BLOCK", "block_reason": "blocked"},
        "self_orientation_basis": {"latest_file_currentness": False},
        "current_self_orientation_summary": {
            "outcome": outcome,
            "current_executable_core_line_recognized": True,
            "governing_effective_basis_recognized": True,
            "current_state_surfaces_recognized": True,
            "reentry_surfaces_recognized": True,
            "body_signal_surfaces_recognized": True,
            "derivative_vessel_relation_boundary_recognized": True,
            "latest_file_currentness": False,
            "recency_fraud": False,
            "failed_check_count": 0,
        },
        "non_claims": _false(),
    }


def _conformance(outcome: str = "BODY_CONFORMANT") -> dict[str, object]:
    return {
        "current_body_conformance_metadata": {
            "current_body_conformance_result_id": CONFORMANCE_ID,
            "current_body_conformance_result_type": "current_body_conformance_result",
            "current_body_conformance_result_version": "0.1.0",
            "runner_module": "run_integrity_host_v0_min_coexistence_current_body_conformance_pass",
        },
        "selected_conformance_inputs": {
            "selected_self_orientation_v6_result": {
                "result_id": V6_ID,
                "result_path": "artifacts/test/current_self_orientation_v6_result.json",
                "outcome": "SELF_ORIENTED",
            }
        },
        "current_body_conformance_summary": {
            "passed_check_count": 1,
            "failed_check_count": 0,
            "current_governing_basis_passed": True,
            "reentry_posture_passed": True,
            "body_signal_posture_passed": True,
            "derivative_vessel_posture_passed": True,
            "operator_posture_passed": True,
            "integrated_non_claims_passed": True,
        },
        "current_body_conformance_checks": [_check("conformance_check")],
        "integrated_non_claims": _false(),
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "BODY_CONFORMANT"
        else {"block_code": "SYNTHETIC_CONFORMANCE_BLOCK", "block_reason": "blocked"},
        "non_claims": _false(),
    }


def _closure(
    outcome: str = "CONFORMANCE_CLOSURE_RECORDED",
    *,
    statement: dict[str, object] | None = None,
    claims: dict[str, bool] | None = None,
) -> dict[str, object]:
    closure_statement = {
        "conformance_question_closed": True,
        "next_work_question_opened": False,
        "conformance_recorded_as_permission": False,
        "conformance_recorded_as_authority": False,
        "conformance_recorded_as_signal": False,
        "self_orientation_successor_forced": False,
    }
    closure_statement.update(statement or {})
    return {
        "conformance_closure_metadata": {
            "conformance_closure_result_id": CLOSURE_ID,
            "conformance_closure_result_type": "post_conformance_closure_result",
            "conformance_closure_result_version": "0.1.0",
            "resolver_module": "resolve_current_body_standing_closure_post_conformance",
        },
        "selected_self_orientation_v6_basis": {
            "self_orientation_result_id": V6_ID,
            "outcome": "SELF_ORIENTED",
        },
        "selected_current_body_conformance_basis": {
            "current_body_conformance_result_id": CONFORMANCE_ID,
            "outcome": "BODY_CONFORMANT",
        },
        "closure_statement": closure_statement,
        "current_body_standing_closure_summary": {
            "passed_check_count": 1,
            "failed_check_count": 0,
        },
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "CONFORMANCE_CLOSURE_RECORDED"
        else {"block_code": "SYNTHETIC_CLOSURE_BLOCK", "block_reason": "blocked"},
        "non_claims": _false(**(claims or {})),
    }


def _correspondence(
    correspondence_type: str,
    result_id: str,
    outcomes: list[str],
    *,
    outcome: str = "CORRESPONDENCE_RECOGNIZED",
    summary: dict[str, object] | None = None,
    claims: dict[str, bool] | None = None,
) -> dict[str, object]:
    correspondence_summary = {
        "correspondence_recognized": outcome == "CORRESPONDENCE_RECOGNIZED",
        "passed_check_count": 1,
        "failed_check_count": 0,
        "rank_preserved": True,
        "source_preserved": True,
        "scope_preserved": True,
        "lineage_preserved": True,
        "non_claims_preserved": True,
        "source_rank_scope_lineage_non_claims_preserved": True,
        "correspondence_created_authority": False,
        "correspondence_created_currentness": False,
        "correspondence_created_permission": False,
        "correspondence_created_signal": False,
        "correspondence_established_presence": False,
        "correspondence_established_threshold": False,
        "correspondence_created_truth": False,
        "correspondence_authorized_action": False,
        "correspondence_created_consequence": False,
        "self_orientation_successor_forced": False,
        "conformance_successor_forced": False,
        "continuation_authorized": False,
        "key_non_claims": _false(**(claims or {})),
    }
    correspondence_summary.update(summary or {})
    return {
        "cross_surface_correspondence_metadata": {
            "cross_surface_correspondence_result_id": result_id,
            "cross_surface_correspondence_result_type": "cross_surface_correspondence_result",
            "cross_surface_correspondence_result_version": "0.1.0",
            "resolver_module": "resolve_cross_surface_correspondence_boundary",
        },
        "declared_correspondence_question": f"Does {correspondence_type} stand?",
        "correspondence_basis": {
            "correspondence_type": correspondence_type,
            "selected_surface_ids": ["surface_a", "surface_b"],
            "selected_surface_outcomes": outcomes,
        },
        "correspondence_result": {
            "correspondence_recognized": outcome == "CORRESPONDENCE_RECOGNIZED",
            "no_correspondence": False,
            "evidence": {"correspondence_type": correspondence_type},
        },
        "cross_surface_correspondence_summary": correspondence_summary,
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "CORRESPONDENCE_RECOGNIZED"
        else {"block_code": "SYNTHETIC_CORRESPONDENCE_BLOCK", "block_reason": "blocked"},
        "non_claims": _false(**(claims or {})),
    }


def _receipt(
    result_id: str,
    *,
    outcome: str = "CARRIED_SURFACE_RECEIVED",
    statement: dict[str, object] | None = None,
    claims: dict[str, bool] | None = None,
    receiving_carrier_id: str = "carrier_B_receiving",
) -> dict[str, object]:
    receipt_statement = {
        "carried_surface_received": outcome == "CARRIED_SURFACE_RECEIVED",
        "source_carrier_preserved": True,
        "receiving_carrier_declared": True,
        "carried_surface_identity_preserved": True,
        "carried_surface_outcome_preserved": True,
        "integrity_checked": True,
        "integrity_evidence_preserved": True,
        "received_as_carried_evidence": outcome == "CARRIED_SURFACE_RECEIVED",
        "receiving_carrier_became_source": False,
        "receiving_carrier_became_current": False,
        "receiving_carrier_became_authority": False,
        "receiving_carrier_became_successor": False,
        "carried_surface_became_source": False,
        "carried_surface_became_currentness": False,
        "carried_surface_became_permission": False,
        "receipt_created_signal_by_default": False,
        "receipt_established_presence": False,
        "receipt_established_threshold": False,
        "receipt_created_truth": False,
        "receipt_authorized_action": False,
        "receipt_created_consequence": False,
        "receipt_authorized_continuation": False,
        "multi_carrier_law_created": False,
        "distributed_standing_created": False,
    }
    receipt_statement.update(statement or {})
    non_claims = _false(**(claims or {}))
    return {
        "cross_carrier_surface_receipt_metadata": {
            "cross_carrier_surface_receipt_result_id": result_id,
            "cross_carrier_surface_receipt_result_type": "cross_carrier_surface_receipt_result",
            "cross_carrier_surface_receipt_result_version": "0.1.0",
            "resolver_module": "resolve_cross_carrier_surface_receipt_boundary",
        },
        "source_carrier_basis": {"carrier_id": "carrier_A_source"},
        "receiving_carrier_basis": {"carrier_id": receiving_carrier_id},
        "carried_surface_basis": {
            "surface_id": CLOSURE_ID,
            "surface_path": "artifacts/test/closure.json",
            "surface_filename": "closure.json",
            "surface_outcome": "CONFORMANCE_CLOSURE_RECORDED",
            "source_downstream_posture": "carried_evidence_downstream_only",
        },
        "carried_surface_integrity_check": {
            "integrity_checked": True,
            "integrity_evidence_preserved": True,
            "hash_algorithm": "sha256",
            "hash": "0" * 64,
        },
        "receipt_statement": receipt_statement,
        "cross_carrier_surface_receipt_summary": {
            "passed_check_count": 1 if outcome == "CARRIED_SURFACE_RECEIVED" else 0,
            "failed_check_count": 0 if outcome == "CARRIED_SURFACE_RECEIVED" else 1,
            "key_non_claims": non_claims,
        },
        "outcome": outcome,
        "block": {"block_code": None, "block_reason": None}
        if outcome == "CARRIED_SURFACE_RECEIVED"
        else {"block_code": "BYTE_TRANSFER_MISTAKEN_FOR_RECEIPT", "block_reason": "blocked"},
        "non_claims": non_claims,
    }


def _valid() -> dict[str, dict[str, object]]:
    return {
        "v6": _v6(),
        "conformance": _conformance(),
        "closure": _closure(),
        "closure_alignment": _correspondence(
            "CLOSURE_ALIGNMENT",
            CLOSURE_ALIGNMENT_ID,
            ["BODY_CONFORMANT", "CONFORMANCE_CLOSURE_RECORDED"],
        ),
        "local_receipt": _receipt(LOCAL_RECEIPT_ID, receiving_carrier_id="carrier_A_receiving"),
        "returned_blocked": _receipt(RETURNED_BLOCKED_RECEIPT_ID, outcome="BLOCKED"),
        "returned_success": _receipt(RETURNED_SUCCESS_RECEIPT_ID),
        "receipt_alignment": _correspondence(
            "NON_CLAIM_ALIGNMENT",
            RECEIPT_ALIGNMENT_ID,
            ["CARRIED_SURFACE_RECEIVED", "CARRIED_SURFACE_RECEIVED"],
        ),
        "refusal_visible": _correspondence(
            "REFUSAL_VISIBLE",
            REFUSAL_VISIBLE_ID,
            ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
        ),
    }


def _tuple(value: dict[str, object] | None, mode: str) -> tuple[None, dict[str, object] | None, str]:
    return None, copy.deepcopy(value) if value is not None else None, mode


def _resolve_selected(**overrides: dict[str, object] | None) -> dict[str, object]:
    artifacts = _valid()
    artifacts.update({key: value for key, value in overrides.items() if key in artifacts})

    def select_correspondence(correspondence_type: str, **kwargs: object) -> tuple[None, dict[str, object] | None, str]:
        key = {
            "CLOSURE_ALIGNMENT": "closure_alignment",
            "NON_CLAIM_ALIGNMENT": "receipt_alignment",
            "REFUSAL_VISIBLE": "refusal_visible",
        }[correspondence_type]
        return _tuple(artifacts.get(key), f"test_{key}_selection")

    def select_receipt(root: Path, outcome: str, selection_mode: str) -> tuple[None, dict[str, object] | None, str]:
        if selection_mode == "local_cross_carrier_receipt_discovery":
            return _tuple(artifacts.get("local_receipt"), selection_mode)
        if selection_mode == "returned_carrier_b_blocked_receipt_discovery":
            return _tuple(artifacts.get("returned_blocked"), selection_mode)
        return _tuple(artifacts.get("returned_success"), selection_mode)

    with mock.patch.object(
        resolver,
        "_select_conformance",
        return_value=_tuple(artifacts.get("conformance"), "test_conformance_selection"),
    ), mock.patch.object(
        resolver,
        "_select_closure",
        return_value=_tuple(artifacts.get("closure"), "test_closure_selection"),
    ), mock.patch.object(
        resolver,
        "_select_correspondence",
        side_effect=select_correspondence,
    ), mock.patch.object(
        resolver,
        "_select_receipt",
        side_effect=select_receipt,
    ):
        return resolver.resolve_current_self_orientation(body_pass_result=artifacts["v6"])


class CurrentSelfOrientationV7RealArtifactTests(unittest.TestCase):
    def setUp(self) -> None:
        self.result = resolver.resolve_current_self_orientation()

    def test_real_self_oriented_v7_path_has_shape_and_metadata(self) -> None:
        self.assertIsInstance(self.result, dict)
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(self.result))
        self.assertEqual(self.result["outcome"], "SELF_ORIENTED")
        self.assertEqual(self.result["block"], {"block_code": None, "block_reason": None})

        metadata = self.result["current_self_orientation_v7_metadata"]
        for key in (
            "self_orientation_result_id",
            "self_orientation_result_type",
            "self_orientation_result_version",
            "generated_at",
            "resolver_module",
            "successor_of_module",
        ):
            self.assertTrue(metadata.get(key), key)
        self.assertEqual(metadata["self_orientation_result_version"], "0.7.0")
        self.assertEqual(metadata["resolver_module"], "resolve_current_self_orientation_v7")
        self.assertEqual(metadata["successor_of_module"], "resolve_current_self_orientation_v6")

    def test_selected_inputs_and_v6_architecture_remain_intact(self) -> None:
        selected = self.result["selected_orientation_inputs"]
        for key in (
            "selected_current_self_orientation_v6_result",
            "selected_current_body_conformance_result",
            "selected_post_conformance_closure_result",
            "selected_closure_alignment_correspondence_result",
            "selected_local_cross_carrier_receipt_result",
            "selected_returned_carrier_b_blocked_receipt_result",
            "selected_returned_carrier_b_successful_receipt_result",
            "selected_receipt_alignment_correspondence_result",
            "selected_refusal_visible_correspondence_result",
        ):
            self.assertTrue(selected[key].get("result_id"), key)
            self.assertIn("selection_mode", selected[key])

        for key in (
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
        ):
            self.assertIsInstance(self.result[key], dict)
            self.assertTrue(self.result[key], key)

        basis = self.result["self_orientation_basis"]
        self.assertTrue(basis["current_governing_basis_remains_inherited_from_v6_upstream_surfaces"])
        self.assertTrue(basis["conformance_surfaces_remain_downstream_audit_only"])
        self.assertTrue(basis["closure_surfaces_remain_downstream_meaning_closure_only"])
        self.assertTrue(basis["correspondence_surfaces_remain_bounded_reading_relation_only"])
        self.assertTrue(basis["receipt_surfaces_remain_carried_evidence_only"])
        self.assertTrue(basis["carrier_b_remains_receiving_carrier_only"])
        for key in (
            "post_v6_surfaces_create_authority",
            "post_v6_surfaces_create_permission",
            "post_v6_surfaces_create_currentness",
            "post_v6_surfaces_create_signal",
            "post_v6_surfaces_create_presence_threshold_truth_action_or_consequence",
            "post_v6_surfaces_authorize_continuation",
            "post_v6_surfaces_create_multi_carrier_law",
            "post_v6_surfaces_create_distributed_standing",
        ):
            self.assertFalse(basis[key], key)

    def test_downstream_conformance_closure_correspondence_and_receipt_recognition(self) -> None:
        conformance = self.result["recognized_current_body_conformance_surfaces"]
        self.assertEqual(conformance["selected_current_body_conformance_result"]["outcome"], "BODY_CONFORMANT")
        self.assertEqual(conformance["failed_check_count"], 0)
        for key in (
            "current_governing_basis_passed",
            "reentry_posture_passed",
            "body_signal_posture_passed",
            "derivative_vessel_posture_passed",
            "operator_posture_passed",
            "integrated_non_claims_passed",
            "conformance_remains_audit_posture",
            "conformance_creates_no_authority",
            "conformance_creates_no_permission",
            "conformance_creates_no_currentness",
            "conformance_creates_no_signal",
            "conformance_authorizes_no_continuation",
            "conformance_does_not_complete_whole_body",
        ):
            self.assertTrue(conformance[key], key)

        closure = self.result["recognized_post_conformance_closure_surfaces"]
        self.assertEqual(closure["selected_post_conformance_closure_result"]["outcome"], "CONFORMANCE_CLOSURE_RECORDED")
        self.assertTrue(closure["closure_recorded"])
        self.assertTrue(closure["conformance_question_closed"])
        self.assertFalse(closure["next_work_question_opened"])
        self.assertFalse(closure["conformance_recorded_as_permission"])
        self.assertFalse(closure["conformance_recorded_as_authority"])
        self.assertFalse(closure["conformance_recorded_as_signal"])
        self.assertFalse(closure["self_orientation_successor_forced"])

        correspondence = self.result["recognized_cross_surface_correspondence_surfaces"]
        for key, relation_type in (
            ("selected_closure_alignment_correspondence", "CLOSURE_ALIGNMENT"),
            ("selected_receipt_alignment_correspondence", "NON_CLAIM_ALIGNMENT"),
            ("selected_refusal_visible_correspondence", "REFUSAL_VISIBLE"),
        ):
            selected = correspondence[key]
            self.assertEqual(selected["correspondence_type"], relation_type)
            self.assertTrue(selected["correspondence_recognized"])
            self.assertEqual(selected["failed_check_count"], 0)
            self.assertTrue(selected["rank_preserved"])
            self.assertTrue(selected["source_preserved"])
            self.assertTrue(selected["scope_preserved"])
            self.assertTrue(selected["lineage_preserved"])
            self.assertTrue(selected["non_claims_preserved"])
        self.assertTrue(correspondence["correspondence_authorizes_no_continuation"])

        receipt = self.result["recognized_cross_carrier_receipt_surfaces"]
        local = receipt["selected_local_cross_carrier_receipt"]
        returned_blocked = receipt["selected_returned_carrier_b_blocked_receipt"]
        returned_success = receipt["selected_returned_carrier_b_successful_receipt"]
        self.assertEqual(local["selected_receipt_result"]["outcome"], "CARRIED_SURFACE_RECEIVED")
        self.assertEqual(returned_success["selected_receipt_result"]["outcome"], "CARRIED_SURFACE_RECEIVED")
        self.assertEqual(returned_blocked["selected_receipt_result"]["outcome"], "BLOCKED")
        self.assertTrue(returned_success["received_as_carried_evidence"])
        self.assertFalse(returned_success["receiving_carrier_became_source"])
        self.assertFalse(returned_success["receiving_carrier_became_current"])
        self.assertFalse(returned_success["receiving_carrier_became_authority"])
        self.assertFalse(returned_success["receiving_carrier_became_successor"])
        self.assertFalse(returned_success["carried_surface_became_source"])
        self.assertFalse(returned_success["carried_surface_became_currentness"])
        self.assertFalse(returned_success["carried_surface_became_permission"])
        self.assertFalse(returned_success["receipt_created_signal_by_default"])
        self.assertFalse(returned_success["receipt_established_presence"])
        self.assertFalse(returned_success["receipt_established_threshold"])
        self.assertFalse(returned_success["receipt_created_truth"])
        self.assertFalse(returned_success["receipt_authorized_action"])
        self.assertFalse(returned_success["receipt_created_consequence"])
        self.assertFalse(returned_success["receipt_authorized_continuation"])
        self.assertFalse(returned_success["multi_carrier_law_created"])
        self.assertFalse(returned_success["distributed_standing_created"])
        self.assertTrue(receipt["carrier_b_remains_physical_receiving_carrier_evidence_only"])
        self.assertTrue(receipt["returned_evidence_does_not_replace_local_source"])
        self.assertTrue(receipt["returned_evidence_does_not_create_currentness"])

    def test_checks_summary_nonclaims_path_write_and_nonmutation(self) -> None:
        checks = self.result["bounded_correspondence_checks"]
        check_names = {check["check_name"] for check in checks}
        self.assertTrue(V7_CHECK_NAMES.issubset(check_names))
        self.assertTrue(all(check["passed"] is True for check in checks))
        for check in checks:
            self.assertTrue({"check_name", "passed", "expected_posture", "actual_posture", "block_code"}.issubset(check))

        summary = resolver.build_current_self_orientation_summary(self.result)
        self.assertEqual(summary["outcome"], "SELF_ORIENTED")
        self.assertEqual(summary["failed_check_count"], 0)
        for key in (
            "current_governing_basis_recognized",
            "reentry_surfaces_recognized",
            "body_signal_surfaces_recognized",
            "derivative_vessel_relation_boundary_recognized",
            "current_body_conformance_recognized",
            "post_conformance_closure_recognized",
            "cross_surface_correspondence_recognized",
            "cross_carrier_receipt_recognized",
            "carrier_b_returned_receipt_evidence_recognized",
            "carrier_b_refusal_evidence_remains_visible",
            "receipt_alignment_correspondence_recognized",
            "refusal_visible_correspondence_recognized",
            "carrier_b_remained_receiving_carrier_only",
            "source_currentness_authority_permission_successor_body_collapse_stayed_false",
            "multi_carrier_law_stayed_false",
            "distributed_standing_stayed_false",
            "presence_threshold_truth_action_consequence_stayed_false",
            "correspondence_checks_passed",
        ):
            self.assertTrue(summary[key], key)

        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, self.result["non_claims"], key)
            self.assertIs(self.result["non_claims"][key], False, key)

        selected = self.result["selected_orientation_inputs"]
        tracked = [
            _repo_path(value.get("result_path"))
            for value in selected.values()
            if isinstance(value, dict) and value.get("result_path")
        ]
        tracked = [path for path in tracked if path is not None and path.exists()]
        before = _snapshot(tracked)
        v6_path = selected["selected_current_self_orientation_v6_result"]["result_path"]
        path_result = resolver.resolve_current_self_orientation_from_path(v6_path)
        self.assertEqual(path_result["outcome"], "SELF_ORIENTED")
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(path_result))
        self.assertTrue(
            path_result["self_orientation_basis"][
                "current_governing_basis_remains_inherited_from_v6_upstream_surfaces"
            ]
        )
        resolver.resolve_current_self_orientation()
        self.assertEqual(before, _snapshot(tracked))

        with tempfile.TemporaryDirectory() as tmp:
            explicit = Path(tmp) / "nested" / "v7_result.json"
            written = resolver.write_current_self_orientation_result(self.result, explicit)
            self.assertEqual(written, explicit)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(_read_json(written)))
            with mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V7_ROOT", Path(tmp) / "default"):
                first = resolver.write_current_self_orientation_result(self.result)
                second = resolver.write_current_self_orientation_result(self.result)
                self.assertNotEqual(first, second)
                self.assertTrue(first.name.endswith("__current_self_orientation_v7_result.json"))
                self.assertIn("__current_self_orientation_v7_result_001.json", second.name)


class CurrentSelfOrientationV7BlockedPathTests(unittest.TestCase):
    def assertBlocked(self, result: dict[str, object], expected: str | set[str]) -> None:
        self.assertEqual(result["outcome"], "BLOCKED")
        code = result["block"]["block_code"]
        if isinstance(expected, set):
            self.assertIn(code, expected)
        else:
            self.assertEqual(code, expected)
        self.assertIn("non_claims", result)
        self.assertIsInstance(result["bounded_correspondence_checks"], list)

    def test_declared_block_family_and_v6_blocks(self) -> None:
        self.assertTrue(EXPECTED_BLOCK_CODES.issubset(resolver.BLOCK_REASONS))
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            roots = {
                "CURRENT_SELF_ORIENTATION_V6_ROOT": root / "v6",
                "CURRENT_SELF_ORIENTATION_V7_ROOT": root / "v7",
                "CURRENT_BODY_CONFORMANCE_ROOT": root / "conformance",
                "POST_CONFORMANCE_CLOSURE_ROOT": root / "closure",
                "CROSS_SURFACE_CORRESPONDENCE_ROOT": root / "correspondence",
                "CROSS_CARRIER_SURFACE_RECEIPT_ROOT": root / "receipt",
                "RETURNED_CARRIER_B_RECEIPT_ROOT": root / "returned",
            }
            for artifact_root in roots.values():
                artifact_root.mkdir(parents=True, exist_ok=True)
            with mock.patch.multiple(resolver, **roots):
                self.assertBlocked(
                    resolver.resolve_current_self_orientation(),
                    "SELF_ORIENTATION_V6_MISSING",
                )
        self.assertBlocked(
            resolver.resolve_current_self_orientation(body_pass_result=_v6("BLOCKED")),
            "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED",
        )

    def test_conformance_and_closure_blocks(self) -> None:
        self.assertBlocked(_resolve_selected(conformance=None), "CURRENT_BODY_CONFORMANCE_MISSING")
        self.assertBlocked(
            _resolve_selected(conformance=_conformance("BLOCKED")),
            "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT",
        )
        self.assertBlocked(_resolve_selected(closure=None), "POST_CONFORMANCE_CLOSURE_MISSING")
        self.assertBlocked(
            _resolve_selected(closure=_closure("BLOCKED")),
            "POST_CONFORMANCE_CLOSURE_NOT_RECORDED",
        )
        for statement, claims, code in (
            ({"conformance_recorded_as_permission": True}, {"permission_created": True}, "CONFORMANCE_CLOSURE_PERMISSION_LEAK"),
            ({"conformance_recorded_as_authority": True}, {"authority_created": True}, "CONFORMANCE_CLOSURE_AUTHORITY_LEAK"),
            ({"conformance_recorded_as_signal": True}, {"signal_created_by_default": True}, "CONFORMANCE_CLOSURE_SIGNAL_LEAK"),
            ({"next_work_question_opened": True}, {"continuation_authorized": True}, "CONFORMANCE_CLOSURE_CONTINUATION_LEAK"),
            ({"self_orientation_successor_forced": True}, {"self_orientation_successor_forced": True}, "CONFORMANCE_CLOSURE_CONTINUATION_LEAK"),
        ):
            with self.subTest(code=code):
                self.assertBlocked(
                    _resolve_selected(closure=_closure(statement=statement, claims=claims)),
                    code,
                )

    def test_correspondence_blocks(self) -> None:
        self.assertBlocked(_resolve_selected(closure_alignment=None), "CROSS_SURFACE_CORRESPONDENCE_MISSING")
        self.assertBlocked(
            _resolve_selected(
                closure_alignment=_correspondence(
                    "CLOSURE_ALIGNMENT",
                    CLOSURE_ALIGNMENT_ID,
                    ["BODY_CONFORMANT", "CONFORMANCE_CLOSURE_RECORDED"],
                    outcome="BLOCKED",
                )
            ),
            "CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED",
        )
        self.assertBlocked(
            _resolve_selected(
                closure_alignment=_correspondence(
                    "CLOSURE_ALIGNMENT",
                    CLOSURE_ALIGNMENT_ID,
                    ["BODY_CONFORMANT", "CONFORMANCE_CLOSURE_RECORDED"],
                    summary={"correspondence_created_authority": True},
                    claims={"correspondence_became_authority": True},
                )
            ),
            {"CROSS_SURFACE_CORRESPONDENCE_NOT_RECOGNIZED", "CROSS_SURFACE_CORRESPONDENCE_COLLAPSE_LEAK"},
        )
        self.assertBlocked(_resolve_selected(receipt_alignment=None), "RECEIPT_ALIGNMENT_CORRESPONDENCE_MISSING")
        self.assertBlocked(
            _resolve_selected(
                receipt_alignment=_correspondence(
                    "NON_CLAIM_ALIGNMENT",
                    RECEIPT_ALIGNMENT_ID,
                    ["CARRIED_SURFACE_RECEIVED"],
                    outcome="BLOCKED",
                )
            ),
            "RECEIPT_ALIGNMENT_CORRESPONDENCE_NOT_RECOGNIZED",
        )
        self.assertBlocked(_resolve_selected(refusal_visible=None), "REFUSAL_VISIBLE_CORRESPONDENCE_MISSING")
        self.assertBlocked(
            _resolve_selected(
                refusal_visible=_correspondence(
                    "REFUSAL_VISIBLE",
                    REFUSAL_VISIBLE_ID,
                    ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
                    outcome="BLOCKED",
                )
            ),
            "REFUSAL_VISIBLE_CORRESPONDENCE_NOT_RECOGNIZED",
        )

    def test_receipt_missing_and_not_received_blocks(self) -> None:
        self.assertBlocked(_resolve_selected(local_receipt=None), "CROSS_CARRIER_RECEIPT_MISSING")
        self.assertBlocked(
            _resolve_selected(local_receipt=_receipt(LOCAL_RECEIPT_ID, outcome="BLOCKED")),
            "CROSS_CARRIER_RECEIPT_NOT_RECEIVED",
        )
        self.assertBlocked(_resolve_selected(returned_success=None), "RETURNED_CARRIER_RECEIPT_MISSING")
        self.assertBlocked(
            _resolve_selected(returned_success=_receipt(RETURNED_SUCCESS_RECEIPT_ID, outcome="BLOCKED")),
            "RETURNED_CARRIER_RECEIPT_NOT_RECEIVED",
        )
        self.assertBlocked(_resolve_selected(returned_blocked=None), "RETURNED_CARRIER_REFUSAL_NOT_VISIBLE")

    def test_receipt_collapse_blocks(self) -> None:
        receipt_leaks = (
            ({"receiving_carrier_became_source": True}, {"receiving_carrier_became_source": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIVING_CARRIER_SOURCE_LEAK"}),
            ({"receiving_carrier_became_current": True}, {"receiving_carrier_became_current": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIVING_CARRIER_CURRENTNESS_LEAK"}),
            ({"receiving_carrier_became_authority": True}, {"receiving_carrier_became_authority": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIVING_CARRIER_AUTHORITY_LEAK"}),
            ({"receiving_carrier_became_successor": True}, {"receiving_carrier_became_successor": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIVING_CARRIER_SUCCESSOR_LEAK"}),
            ({"carried_surface_became_source": True}, {"carried_surface_became_source": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "CARRIED_SURFACE_SOURCE_OR_CURRENTNESS_LEAK"}),
            ({"carried_surface_became_currentness": True}, {"carried_surface_became_currentness": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "CARRIED_SURFACE_SOURCE_OR_CURRENTNESS_LEAK"}),
            ({"carried_surface_became_permission": True}, {"carried_surface_became_permission": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "CARRIED_SURFACE_PERMISSION_OR_SIGNAL_LEAK"}),
            ({"receipt_created_signal_by_default": True}, {"carried_surface_became_signal_by_default": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "CARRIED_SURFACE_PERMISSION_OR_SIGNAL_LEAK"}),
            ({"receipt_established_presence": True}, {"presence_established": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK"}),
            ({"receipt_established_threshold": True}, {"threshold_met": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK"}),
            ({"receipt_created_truth": True}, {"truth_created": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK"}),
            ({"receipt_authorized_action": True}, {"action_authorized": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK"}),
            ({"receipt_created_consequence": True}, {"consequence_created": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_PRESENCE_THRESHOLD_TRUTH_ACTION_LEAK"}),
            ({"multi_carrier_law_created": True}, {"multi_carrier_law_created": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_MULTI_CARRIER_OR_DISTRIBUTED_STANDING_LEAK"}),
            ({"distributed_standing_created": True}, {"distributed_standing_created": True}, {"RETURNED_CARRIER_RECEIPT_NOT_RECEIVED", "RECEIPT_MULTI_CARRIER_OR_DISTRIBUTED_STANDING_LEAK"}),
        )
        for statement, claims, expected in receipt_leaks:
            with self.subTest(statement=statement):
                self.assertBlocked(
                    _resolve_selected(
                        returned_success=_receipt(
                            RETURNED_SUCCESS_RECEIPT_ID,
                            statement=statement,
                            claims=claims,
                        )
                    ),
                    expected,
                )

        for claim, expected in (
            ("returned_evidence_replaced_source", {"NON_CLAIM_MISSING_OR_FLIPPED", "RETURNED_EVIDENCE_REPLACED_SOURCE"}),
            ("returned_evidence_created_currentness", {"NON_CLAIM_MISSING_OR_FLIPPED", "RETURNED_EVIDENCE_CREATED_CURRENTNESS"}),
            ("latest_file_currentness", {"NON_CLAIM_MISSING_OR_FLIPPED", "LATEST_FILE_CURRENTNESS_REFUSED"}),
            ("recency_fraud", {"NON_CLAIM_MISSING_OR_FLIPPED", "LATEST_FILE_CURRENTNESS_REFUSED"}),
            ("mutation_performed", {"NON_CLAIM_MISSING_OR_FLIPPED", "MUTATION_REPLAY_OR_MERGE_DETECTED"}),
            ("replay_performed", {"NON_CLAIM_MISSING_OR_FLIPPED", "MUTATION_REPLAY_OR_MERGE_DETECTED"}),
            ("merge_performed", {"NON_CLAIM_MISSING_OR_FLIPPED", "MUTATION_REPLAY_OR_MERGE_DETECTED"}),
        ):
            with self.subTest(claim=claim):
                result = _resolve_selected(
                    returned_success=_receipt(
                        RETURNED_SUCCESS_RECEIPT_ID,
                        claims={claim: True},
                    )
                )
                self.assertBlocked(result, expected)
                self.assertIs(result["non_claims"][claim], True)


if __name__ == "__main__":
    unittest.main()
