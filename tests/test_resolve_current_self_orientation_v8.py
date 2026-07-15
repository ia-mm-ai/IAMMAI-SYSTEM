"""Tests for bounded current self-orientation v8.

V8 is a narrow successor to v7. It preserves the v7 self-orientation
architecture and adds recognition of the closed multi-carrier relation band as
downstream posture only. These tests keep relation, conformance, closure,
Carrier B evidence, divergence, currentness participation, and carrier
role/emission out of source, currentness, permission, authority, continuation,
distributed standing, and expansion.
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

import resolve_current_self_orientation_v8 as resolver


TOP_LEVEL_SECTIONS = {
    "current_self_orientation_v8_metadata",
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
    "recognized_carrier_role_emission_surfaces",
    "recognized_carrier_local_emission_admission_surfaces",
    "recognized_cross_carrier_divergence_surfaces",
    "recognized_cross_carrier_currentness_surfaces",
    "recognized_multi_carrier_relation_surfaces",
    "recognized_multi_carrier_relation_conformance_surfaces",
    "recognized_multi_carrier_relation_conformance_closure_surfaces",
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

EXPECTED_CHECK_NAMES = {
    "selected_v7_stands",
    "selected_v7_is_self_oriented",
    "current_governing_basis_remains_upstream",
    "current_body_conformance_v2_exists",
    "current_body_conformance_v2_body_conformant",
    "multi_carrier_relation_exists",
    "multi_carrier_relation_recognized",
    "multi_carrier_relation_conformance_exists",
    "multi_carrier_relation_conformance_conformant",
    "multi_carrier_relation_conformance_closure_exists",
    "multi_carrier_relation_conformance_closure_closed",
    "relation_closure_recorded_meaning",
    "relation_closure_recorded_non_meaning",
    "visible_refusal_preserved",
    "visible_divergence_preserved",
    "currentness_participation_remained_participation",
    "relation_band_remains_downstream",
    "current_carrier_not_selected",
    "winning_losing_carrier_collapse_absent",
    "carrier_hierarchy_absent",
    "distributed_standing_absent",
    "source_currentness_authority_permission_absent",
    "continuation_absent",
    "additional_carrier_experiment_absent",
    "distributed_operation_absent",
    "successor_pressure_absent",
    "divergence_resolution_absent",
    "latest_file_currentness_absent",
    "mutation_replay_merge_absent",
    "required_non_claims_remain_false",
}

FALSE_NON_CLAIMS = (
    "authority_created",
    "permission_created",
    "currentness_created",
    "source_replaced",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "derivative_upgraded_to_source",
    "operator_upgraded_to_source",
    "carrier_receipt_created_authority",
    "carrier_relation_created_currentness",
    "carrier_relation_created_hierarchy",
    "relation_conformance_created_authority",
    "relation_conformance_created_permission",
    "relation_conformance_closure_created_currentness",
    "relation_conformance_closure_created_authority",
    "relation_conformance_closure_created_permission",
    "distributed_standing_created",
    "carrier_hierarchy_created",
    "continuation_authorized",
    "additional_carrier_experiment_authorized",
    "distributed_operation_authorized",
    "closure_forced_self_orientation_successor",
    "closure_forced_conformance_successor",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

V7_ID = "current_self_orientation_v7_test_self_oriented"
V2_ID = "current_body_conformance_v2_test_body_conformant"
RELATION_ID = "carrier_b_refusal_success_relation_test"
CONFORMANCE_ID = "carrier_b_refusal_success_relation_conformance_test"
CLOSURE_ID = "carrier_b_refusal_success_relation_closure_test"


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


def _repo_path(path: str | None) -> Path | None:
    if not path:
        return None
    candidate = Path(path)
    return candidate if candidate.is_absolute() else REPO_ROOT / candidate


def _snapshot(paths: list[Path]) -> dict[Path, str]:
    return {path: path.read_text(encoding="utf-8") for path in paths if path.exists()}


def _non_claims(**updates: bool) -> dict[str, bool]:
    claims = copy.deepcopy(resolver.NON_CLAIMS)
    claims.update(updates)
    return claims


def _pass_check(name: str) -> dict[str, object]:
    return {
        "check_name": name,
        "passed": True,
        "expected_posture": "bounded",
        "actual_posture": "bounded",
        "block_code": None,
    }


def _carrier(carrier_id: str, role: str) -> dict[str, object]:
    return {
        "carrier_id": carrier_id,
        "carrier_role": role,
        "role_operation_local": True,
        "current_carrier_selected": False,
        "carrier_hierarchy_created": False,
    }


def _evidence(evidence_id: str, outcome: str) -> dict[str, object]:
    return {
        "evidence_id": evidence_id,
        "evidence_outcome": outcome,
        "carrier_id": "carrier_B_physical_macbook",
        "carrier_role": "RECEIVING_CARRIER",
        "evidence_class": "RETURNED_RECEIPT_EVIDENCE",
        "emission_class": "CARRIER_LOCAL_RECEIPT_EMISSION",
        "source_or_carried_basis": "current_body_standing_closure_post_conformance",
        "admission_status": "CARRIER_LOCAL_EMISSION_ADMITTED_AS_EVIDENCE",
        "divergence_status": "CARRIER_DIVERGENCE_RECORDED",
        "currentness_participation_status": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
        "downstream_evidence_posture": True,
        "non_claims": _non_claims(),
    }


def _v7(outcome: str = "SELF_ORIENTED", *, upstream: bool = True) -> dict[str, object]:
    return {
        "current_self_orientation_v7_metadata": {
            "self_orientation_result_id": V7_ID,
            "self_orientation_result_type": "CURRENT_SELF_ORIENTATION_V7_RESULT",
            "self_orientation_result_version": "0.7.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "resolve_current_self_orientation_v7",
        },
        "selected_orientation_inputs": {
            "selected_current_governing_basis": {
                "result_id": "governing_effective_basis_test",
                "outcome": "CURRENT_GOVERNING_BASIS_RECOGNIZED",
            },
            "selected_current_state_surface": {
                "result_id": "current_state_surface_test",
                "outcome": "CURRENT_STATE_RECOGNIZED",
            },
        },
        "recognized_current_executable_core_line": {"recognized": True},
        "recognized_governing_effective_basis": {"recognized": True} if upstream else {},
        "recognized_current_state_surfaces": {"recognized": True},
        "recognized_continuity_surfaces": {"recognized": True},
        "recognized_derivative_surfaces": {"recognized": True, "downstream_only": True},
        "recognized_operator_facing_surfaces": {"recognized": True, "downstream_only": True},
        "recognized_reentry_surfaces": {"recognized": True, "downstream_only": True},
        "recognized_body_signal_surfaces": {"recognized": True, "downstream_only": True},
        "recognized_derivative_vessel_relation_surfaces": {
            "recognized": True,
            "downstream_only": True,
        },
        "recognized_current_body_conformance_surfaces": {
            "recognized": True,
            "downstream_only": True,
        },
        "recognized_post_conformance_closure_surfaces": {
            "recognized": True,
            "downstream_only": True,
        },
        "recognized_cross_surface_correspondence_surfaces": {
            "recognized": True,
            "downstream_only": True,
        },
        "recognized_cross_carrier_receipt_surfaces": {
            "recognized": True,
            "carrier_b_returned_receipt_evidence_remains_downstream": True,
        },
        "recognized_open_surfaces": {"recognized": True},
        "recognized_blocked_or_refused_surfaces": {"visible_refusal_preserved": True},
        "recognized_touch_admissibility_surfaces": {"recognized": True},
        "bounded_correspondence_checks": [_pass_check("v7_prior_check")],
        "outcome": outcome,
        "block": {"blocked": outcome != "SELF_ORIENTED", "block_code": None, "block_reason": None},
        "self_orientation_basis": {"current_governing_basis_source": "upstream"},
        "current_self_orientation_summary": {
            "current_governing_basis_recognized": upstream,
            "failed_check_count": 0,
            "passed_check_count": 1,
        },
        "non_claims": _non_claims(),
    }


def _v2(outcome: str = "BODY_CONFORMANT") -> dict[str, object]:
    return {
        "current_body_conformance_pass_v2_metadata": {
            "current_body_conformance_pass_v2_result_id": V2_ID,
            "current_body_conformance_pass_v2_result_type": (
                "CURRENT_BODY_CONFORMANCE_PASS_V2_RESULT"
            ),
            "current_body_conformance_pass_v2_result_version": "0.2.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "run_integrity_host_v0_min_coexistence_current_body_conformance_pass_v2",
        },
        "selected_conformance_inputs": {
            "selected_current_self_orientation_v7_result": {
                "result_id": V7_ID,
                "outcome": "SELF_ORIENTED",
            }
        },
        "v7_orientation_basis": {
            "selected_v7_result_id": V7_ID,
            "selected_v7_outcome": "SELF_ORIENTED",
        },
        "recognized_integrated_body_posture": {
            "v7_integrated": True,
            "downstream_surfaces_remain_downstream": True,
        },
        "conformance_statement": {
            "v7_body_posture_conformant": outcome == "BODY_CONFORMANT",
            "current_governing_basis_remains_upstream": True,
            "downstream_surfaces_remain_downstream": True,
            "no_authority_created": True,
            "no_permission_created": True,
            "no_currentness_created": True,
            "no_distributed_standing_created": True,
            "no_continuation_authorized": True,
        },
        "conformance_checks": [_pass_check("v2_body_conformant")],
        "current_body_conformance_pass_v2_summary": {
            "failed_check_count": 0,
            "passed_check_count": 1,
        },
        "outcome": outcome,
        "block": {"blocked": outcome != "BODY_CONFORMANT", "block_code": None, "block_reason": None},
        "non_claims": _non_claims(),
    }


def _relation() -> dict[str, object]:
    selected_carriers = [
        _carrier("carrier_A_source", "SOURCE_CARRIER_FOR_PACKET"),
        _carrier("carrier_B_physical_macbook", "RECEIVING_CARRIER"),
    ]
    selected_evidence = [
        _evidence("returned_blocked_receipt", "BLOCKED"),
        _evidence("returned_successful_receipt", "CARRIED_SURFACE_RECEIVED"),
    ]
    summary = {
        "relation_request_id": "relation_request_test",
        "relation_question": "When may Carrier A and Carrier B refusal-success evidence stand in relation?",
        "relation_type": "REFUSAL_SUCCESS_RELATION",
        "relation_recognized": True,
        "selected_carrier_count": 2,
        "selected_evidence_count": 2,
        "selected_carrier_ids": ["carrier_A_source", "carrier_B_physical_macbook"],
        "selected_evidence_ids": ["returned_blocked_receipt", "returned_successful_receipt"],
        "selected_evidence_outcomes": ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
        "passed_check_count": 1,
        "failed_check_count": 0,
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "downstream_evidence_posture_preserved": True,
        "current_carrier_not_selected": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "source_currentness_authority_permission_created": False,
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "carrier_hierarchy_created": False,
        "distributed_standing_created": False,
        "continuation_authorized": False,
    }
    return {
        "multi_carrier_relation_metadata": {
            "multi_carrier_relation_result_id": RELATION_ID,
            "multi_carrier_relation_result_type": "MULTI_CARRIER_RELATION_RESULT",
            "multi_carrier_relation_result_version": "0.1.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "resolve_multi_carrier_relation_boundary",
        },
        "declared_relation_question": {
            "relation_question": summary["relation_question"],
            "relation_type": summary["relation_type"],
        },
        "selected_carriers": selected_carriers,
        "selected_carrier_evidence": selected_evidence,
        "relation_basis": {
            "selected_carrier_ids": summary["selected_carrier_ids"],
            "selected_evidence_ids": summary["selected_evidence_ids"],
            "selected_evidence_outcomes": summary["selected_evidence_outcomes"],
        },
        "relation_checks": [_pass_check("relation_recognized")],
        "relation_result": copy.deepcopy(summary),
        "multi_carrier_relation_summary": summary,
        "outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "non_claims": _non_claims(),
    }


def _conformance(relation_path: Path | None = None) -> dict[str, object]:
    selected_relation_path = str(relation_path) if relation_path else None
    summary = {
        "selected_relation_id": RELATION_ID,
        "selected_relation_path": selected_relation_path,
        "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
        "selected_relation_type": "REFUSAL_SUCCESS_RELATION",
        "selected_relation_question": "When may Carrier A and Carrier B refusal-success evidence stand in relation?",
        "selected_carrier_count": 2,
        "selected_evidence_count": 2,
        "selected_carrier_ids": ["carrier_A_source", "carrier_B_physical_macbook"],
        "selected_evidence_ids": ["returned_blocked_receipt", "returned_successful_receipt"],
        "selected_evidence_outcomes": ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
        "passed_check_count": 1,
        "failed_check_count": 0,
        "relation_conformant": True,
        "selected_relation_preserved": True,
        "selected_carriers_preserved": True,
        "selected_evidence_preserved": True,
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "currentness_participation_remained_participation": True,
        "current_carrier_not_selected": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "distributed_standing_created": False,
        "continuation_authorized": False,
        "additional_carrier_experiment_authorized": False,
        "distributed_operation_authorized": False,
    }
    return {
        "multi_carrier_relation_conformance_metadata": {
            "multi_carrier_relation_conformance_result_id": CONFORMANCE_ID,
            "multi_carrier_relation_conformance_result_type": (
                "MULTI_CARRIER_RELATION_CONFORMANCE_RESULT"
            ),
            "multi_carrier_relation_conformance_result_version": "0.1.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "run_multi_carrier_relation_conformance",
        },
        "selected_relation": {
            "selected_relation_result_id": RELATION_ID,
            "selected_relation_result_path": selected_relation_path,
            "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "selected_relation_type": "REFUSAL_SUCCESS_RELATION",
            "selected_relation_question": summary["selected_relation_question"],
        },
        "selected_relation_basis": copy.deepcopy(summary),
        "selected_carriers": _relation()["selected_carriers"],
        "selected_carrier_evidence": _relation()["selected_carrier_evidence"],
        "relation_conformance_checks": [_pass_check("relation_conformant")],
        "relation_conformance_statement": copy.deepcopy(summary),
        "relation_conformance_non_meaning": {
            "does_not_mean_distributed_standing": True,
            "does_not_mean_currentness": True,
        },
        "multi_carrier_relation_conformance_summary": summary,
        "outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "non_claims": _non_claims(),
    }


def _closure(
    conformance_path: Path | None = None,
    relation_path: Path | None = None,
    **updates: bool,
) -> dict[str, object]:
    conformance_result_path = str(conformance_path) if conformance_path else None
    relation_result_path = str(relation_path) if relation_path else None
    statement = {
        "relation_conformance_closed": True,
        "selected_conformance_preserved": True,
        "selected_relation_preserved": True,
        "selected_carriers_preserved": True,
        "selected_evidence_preserved": True,
        "conformance_meaning_recorded": True,
        "conformance_non_meaning_recorded": True,
        "visible_refusal_preserved": True,
        "visible_divergence_preserved": True,
        "currentness_participation_remained_participation": True,
        "current_carrier_not_selected": True,
        "winning_carrier_selected": False,
        "losing_carrier_invalidated": False,
        "carrier_hierarchy_created": False,
        "distributed_standing_created": False,
        "source_replaced": False,
        "currentness_created": False,
        "authority_created": False,
        "permission_created": False,
        "source_currentness_authority_permission_created": False,
        "continuation_authorized": False,
        "additional_carrier_experiment_authorized": False,
        "distributed_operation_authorized": False,
        "closure_authorized_expansion": False,
        "self_orientation_successor_forced": False,
        "conformance_successor_forced": False,
        "selected_conformance_id": CONFORMANCE_ID,
        "selected_conformance_path": conformance_result_path,
        "selected_conformance_outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
        "selected_relation_id": RELATION_ID,
        "selected_relation_path": relation_result_path,
        "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
        "selected_relation_type": "REFUSAL_SUCCESS_RELATION",
        "selected_relation_question": "When may Carrier A and Carrier B refusal-success evidence stand in relation?",
        "selected_carrier_count": 2,
        "selected_evidence_count": 2,
        "selected_carrier_ids": ["carrier_A_source", "carrier_B_physical_macbook"],
        "selected_evidence_ids": ["returned_blocked_receipt", "returned_successful_receipt"],
        "selected_evidence_outcomes": ["BLOCKED", "CARRIED_SURFACE_RECEIVED"],
        "passed_check_count": 1,
        "failed_check_count": 0,
    }
    statement.update(updates)
    return {
        "multi_carrier_relation_conformance_closure_metadata": {
            "multi_carrier_relation_conformance_closure_result_id": CLOSURE_ID,
            "multi_carrier_relation_conformance_closure_result_type": (
                "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_RESULT"
            ),
            "multi_carrier_relation_conformance_closure_result_version": "0.1.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "resolve_multi_carrier_relation_conformance_closure",
        },
        "selected_conformance": {
            "selected_conformance_result_id": CONFORMANCE_ID,
            "selected_conformance_result_path": conformance_result_path,
            "selected_conformance_outcome": "MULTI_CARRIER_RELATION_CONFORMANT",
        },
        "selected_relation": {
            "selected_relation_result_id": RELATION_ID,
            "selected_relation_result_path": relation_result_path,
            "selected_relation_outcome": "MULTI_CARRIER_RELATION_RECOGNIZED",
            "selected_relation_type": "REFUSAL_SUCCESS_RELATION",
            "selected_relation_question": statement["selected_relation_question"],
        },
        "selected_carriers": _relation()["selected_carriers"],
        "selected_carrier_evidence": _relation()["selected_carrier_evidence"],
        "closure_basis": copy.deepcopy(statement),
        "closure_checks": [_pass_check("closure_closed")],
        "closure_statement": copy.deepcopy(statement),
        "closure_non_meaning": {
            "does_not_mean_distributed_standing": True,
            "does_not_mean_currentness": True,
            "does_not_mean_continuation": True,
            "does_not_mean_permission_for_another_carrier": True,
            "does_not_mean_permission_for_distributed_operation": True,
        },
        "multi_carrier_relation_conformance_closure_summary": copy.deepcopy(statement),
        "outcome": "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSED",
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "non_claims": _non_claims(**updates),
    }


def _optional_artifact(result_id: str, outcome: str) -> dict[str, object]:
    return {
        "optional_surface_metadata": {
            "optional_surface_result_id": result_id,
            "optional_surface_result_type": "OPTIONAL_DOWNSTREAM_SURFACE",
            "optional_surface_result_version": "0.1.0",
            "generated_at": "2026-04-29T00:00:00+00:00",
            "resolver_module": "synthetic_test_surface",
        },
        "summary": {
            "result_id": result_id,
            "downstream_only": True,
            "visible_divergence_preserved": True,
            "hidden_divergence": False,
            "currentness_participation_status": "CURRENTNESS_PARTICIPATION_ELIGIBLE",
        },
        "outcome": outcome,
        "block": {"blocked": False, "block_code": None, "block_reason": None},
        "non_claims": _non_claims(),
    }


def _write_artifact_set(root: Path, *, closure_updates: dict[str, bool] | None = None) -> dict[str, Path]:
    paths = {
        "v2": root / "v2" / "current_body_conformance_v2.json",
        "relation": root / "relation" / "multi_carrier_relation.json",
        "conformance": root / "conformance" / "multi_carrier_relation_conformance.json",
        "closure": root / "closure" / "multi_carrier_relation_conformance_closure.json",
        "role": root / "role" / "carrier_role_emission.json",
        "admission": root / "admission" / "carrier_local_emission_admission.json",
        "divergence": root / "divergence" / "cross_carrier_divergence.json",
        "currentness": root / "currentness" / "cross_carrier_currentness.json",
        "receipt": root / "receipt" / "cross_carrier_receipt.json",
        "returned_blocked": root / "returned" / "returned_blocked_receipt.json",
        "returned_success": root / "returned" / "returned_success_receipt.json",
        "correspondence": root / "correspondence" / "cross_surface_correspondence.json",
    }
    _write_json(paths["v2"], _v2())
    _write_json(paths["relation"], _relation())
    _write_json(paths["conformance"], _conformance(paths["relation"]))
    _write_json(
        paths["closure"],
        _closure(paths["conformance"], paths["relation"], **(closure_updates or {})),
    )
    _write_json(paths["role"], _optional_artifact("role_emission_test", "CARRIER_ROLE_RECOGNIZED"))
    _write_json(
        paths["admission"],
        _optional_artifact("admission_test", "CARRIER_LOCAL_EMISSION_ADMITTED"),
    )
    _write_json(
        paths["divergence"],
        _optional_artifact("divergence_test", "CROSS_CARRIER_DIVERGENCE_RECORDED"),
    )
    _write_json(
        paths["currentness"],
        _optional_artifact("currentness_test", "CURRENTNESS_PARTICIPATION_ELIGIBLE"),
    )
    _write_json(paths["receipt"], _optional_artifact("receipt_test", "CARRIED_SURFACE_RECEIVED"))
    _write_json(paths["returned_blocked"], _optional_artifact("blocked_receipt_test", "BLOCKED"))
    _write_json(
        paths["returned_success"],
        _optional_artifact("success_receipt_test", "CARRIED_SURFACE_RECEIVED"),
    )
    _write_json(
        paths["correspondence"],
        _optional_artifact("correspondence_test", "CORRESPONDENCE_RECOGNIZED"),
    )
    return paths


class CurrentSelfOrientationV8Tests(unittest.TestCase):
    def _patch_roots(self, root: Path):
        return mock.patch.multiple(
            resolver,
            CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT=root / "v2",
            MULTI_CARRIER_RELATION_ROOT=root / "relation",
            MULTI_CARRIER_RELATION_CONFORMANCE_ROOT=root / "conformance",
            MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_ROOT=root / "closure",
            CARRIER_ROLE_EMISSION_ROOT=root / "role",
            CARRIER_LOCAL_EMISSION_ADMISSION_ROOT=root / "admission",
            CROSS_CARRIER_DIVERGENCE_ROOT=root / "divergence",
            CROSS_CARRIER_CURRENTNESS_ROOT=root / "currentness",
            CROSS_CARRIER_SURFACE_RECEIPT_ROOT=root / "receipt",
            RETURNED_CARRIER_B_RECEIPT_ROOT=root / "returned",
            CROSS_SURFACE_CORRESPONDENCE_ROOT=root / "correspondence",
        )

    def _synthetic_success(self) -> dict:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            with self._patch_roots(root):
                return resolver.resolve_current_self_orientation(body_pass_result=_v7())

    def assert_top_level_shape(self, result: dict) -> None:
        self.assertTrue(TOP_LEVEL_SECTIONS.issubset(result))
        self.assertIn(result["outcome"], {"SELF_ORIENTED", "BLOCKED"})
        self.assertIsInstance(result["bounded_correspondence_checks"], list)
        self.assertIsInstance(result["current_self_orientation_summary"], dict)

    def assert_false_non_claims(self, result: dict) -> None:
        non_claims = result["non_claims"]
        for key in FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def test_real_self_oriented_v8_path_has_bounded_shape(self) -> None:
        result = resolver.resolve_current_self_orientation()
        self.assertIsInstance(result, dict)
        self.assert_top_level_shape(result)
        self.assertEqual(result["outcome"], "SELF_ORIENTED")
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsInstance(result["recognized_current_executable_core_line"], dict)
        self.assertIsInstance(result["recognized_multi_carrier_relation_surfaces"], dict)

    def test_metadata_declares_v8_successor_of_v7(self) -> None:
        result = self._synthetic_success()
        metadata = result["current_self_orientation_v8_metadata"]
        self.assertTrue(metadata["self_orientation_result_id"])
        self.assertEqual(metadata["self_orientation_result_type"], "CURRENT_SELF_ORIENTATION_V8_RESULT")
        self.assertEqual(metadata["self_orientation_result_version"], "0.8.0")
        self.assertTrue(metadata["generated_at"])
        self.assertEqual(metadata["resolver_module"], "resolve_current_self_orientation_v8")
        self.assertEqual(metadata["successor_of_module"], "resolve_current_self_orientation_v7")

    def test_selected_input_set_preserves_v7_and_relation_band_inputs(self) -> None:
        result = self._synthetic_success()
        inputs = result["selected_orientation_inputs"]
        for key in (
            "selected_current_self_orientation_v7_result",
            "selected_current_body_conformance_v2_result",
            "selected_multi_carrier_relation_result",
            "selected_multi_carrier_relation_conformance_result",
            "selected_multi_carrier_relation_conformance_closure_result",
            "selected_cross_carrier_currentness_result",
            "selected_cross_carrier_divergence_result",
            "selected_carrier_local_emission_admission_result",
            "selected_carrier_role_emission_result",
            "selected_cross_carrier_receipt_result",
            "selected_returned_carrier_b_blocked_receipt_result",
            "selected_returned_carrier_b_successful_receipt_result",
            "inherited_v7_selected_orientation_inputs",
        ):
            self.assertIn(key, inputs)
        self.assertTrue(inputs["selection_posture"]["multi_carrier_relation_band_downstream_only"])
        self.assertTrue(inputs["selection_posture"]["latest_file_currentness_refused"])

    def test_v7_architecture_sections_remain_distinct(self) -> None:
        result = self._synthetic_success()
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
            "recognized_current_body_conformance_surfaces",
            "recognized_post_conformance_closure_surfaces",
            "recognized_cross_surface_correspondence_surfaces",
            "recognized_cross_carrier_receipt_surfaces",
            "recognized_open_surfaces",
            "recognized_blocked_or_refused_surfaces",
            "recognized_touch_admissibility_surfaces",
        ):
            self.assertIsInstance(result[key], dict, key)
        self.assertNotEqual(
            result["recognized_current_executable_core_line"],
            result["recognized_multi_carrier_relation_surfaces"],
        )

    def test_current_governing_basis_remains_upstream_derived(self) -> None:
        result = self._synthetic_success()
        summary = result["current_self_orientation_summary"]
        self.assertTrue(summary["current_governing_basis_recognized"])
        self.assertEqual(
            result["self_orientation_basis"]["current_governing_basis_source"],
            "inherited_from_v7_upstream_basis",
        )
        downstream_sections = (
            "recognized_current_body_conformance_surfaces",
            "recognized_carrier_role_emission_surfaces",
            "recognized_carrier_local_emission_admission_surfaces",
            "recognized_cross_carrier_divergence_surfaces",
            "recognized_cross_carrier_currentness_surfaces",
            "recognized_multi_carrier_relation_surfaces",
            "recognized_multi_carrier_relation_conformance_surfaces",
            "recognized_multi_carrier_relation_conformance_closure_surfaces",
        )
        for key in downstream_sections:
            self.assertFalse(result[key]["current_or_governing_basis"], key)
            self.assertTrue(result[key]["downstream_only"], key)

    def test_carrier_role_and_admission_divergence_currentness_are_downstream(self) -> None:
        result = self._synthetic_success()
        role = result["recognized_carrier_role_emission_surfaces"]
        admission = result["recognized_carrier_local_emission_admission_surfaces"]
        divergence = result["recognized_cross_carrier_divergence_surfaces"]
        currentness = result["recognized_cross_carrier_currentness_surfaces"]

        self.assertTrue(role["recognized"])
        self.assertIn("operation-local", role["posture"])
        self.assertTrue(admission["recognized"])
        self.assertIn("downstream evidence", admission["posture"])
        self.assertTrue(divergence["recognized"])
        self.assertIn("unresolved", divergence["posture"])
        self.assertTrue(currentness["recognized"])
        self.assertIn("participation only", currentness["posture"])

        for section in (role, admission, divergence, currentness):
            self.assertTrue(section["downstream_only"])
            self.assertFalse(section["current_or_governing_basis"])

    def test_multi_carrier_relation_recognition_preserves_non_collapse(self) -> None:
        result = self._synthetic_success()
        relation = result["recognized_multi_carrier_relation_surfaces"]
        self.assertTrue(relation["recognized"])
        self.assertEqual(relation["relation_type"], "REFUSAL_SUCCESS_RELATION")
        self.assertTrue(relation["relation_question"])
        self.assertEqual(relation["selected_carrier_ids"], ["carrier_A_source", "carrier_B_physical_macbook"])
        self.assertEqual(relation["selected_evidence_outcomes"], ["BLOCKED", "CARRIED_SURFACE_RECEIVED"])
        self.assertTrue(relation["visible_refusal_preserved"])
        self.assertTrue(relation["visible_divergence_preserved"])
        self.assertTrue(relation["downstream_evidence_posture_preserved"])
        self.assertTrue(relation["current_carrier_not_selected"])
        self.assertFalse(relation["winning_carrier_selected"])
        self.assertFalse(relation["losing_carrier_invalidated"])
        self.assertFalse(relation["carrier_hierarchy_created"])
        self.assertFalse(relation["distributed_standing_created"])
        self.assertFalse(relation["currentness_created"])
        self.assertFalse(relation["authority_created"])
        self.assertFalse(relation["permission_created"])
        self.assertFalse(relation["continuation_authorized"])

    def test_relation_conformance_recognition_preserves_coherence_only(self) -> None:
        result = self._synthetic_success()
        conformance = result["recognized_multi_carrier_relation_conformance_surfaces"]
        self.assertTrue(conformance["recognized"])
        self.assertEqual(conformance["selected_relation_id"], RELATION_ID)
        self.assertEqual(conformance["selected_relation_outcome"], "MULTI_CARRIER_RELATION_RECOGNIZED")
        self.assertEqual(conformance["selected_relation_type"], "REFUSAL_SUCCESS_RELATION")
        self.assertEqual(conformance["selected_carrier_count"], 2)
        self.assertEqual(conformance["selected_evidence_count"], 2)
        self.assertEqual(conformance["failed_check_count"], 0)
        self.assertTrue(conformance["relation_conformant"])
        self.assertTrue(conformance["selected_relation_preserved"])
        self.assertTrue(conformance["selected_carriers_preserved"])
        self.assertTrue(conformance["selected_evidence_preserved"])
        self.assertTrue(conformance["visible_refusal_preserved"])
        self.assertTrue(conformance["visible_divergence_preserved"])
        self.assertTrue(conformance["currentness_participation_remained_participation"])
        self.assertTrue(conformance["current_carrier_not_selected"])
        self.assertFalse(conformance["winning_carrier_selected"])
        self.assertFalse(conformance["losing_carrier_invalidated"])
        self.assertFalse(conformance["carrier_hierarchy_created"])
        self.assertFalse(conformance["distributed_standing_created"])
        self.assertFalse(conformance["continuation_authorized"])
        self.assertFalse(conformance["additional_carrier_experiment_authorized"])
        self.assertFalse(conformance["distributed_operation_authorized"])

    def test_relation_conformance_closure_recognition_preserves_meaning_only(self) -> None:
        result = self._synthetic_success()
        closure = result["recognized_multi_carrier_relation_conformance_closure_surfaces"]
        self.assertTrue(closure["recognized"])
        self.assertEqual(closure["selected_conformance_id"], CONFORMANCE_ID)
        self.assertEqual(closure["selected_conformance_outcome"], "MULTI_CARRIER_RELATION_CONFORMANT")
        self.assertEqual(closure["selected_relation_id"], RELATION_ID)
        self.assertTrue(closure["relation_conformance_closed"])
        self.assertTrue(closure["conformance_meaning_recorded"])
        self.assertTrue(closure["conformance_non_meaning_recorded"])
        self.assertTrue(closure["selected_carriers_preserved"])
        self.assertTrue(closure["selected_evidence_preserved"])
        self.assertTrue(closure["visible_refusal_preserved"])
        self.assertTrue(closure["visible_divergence_preserved"])
        self.assertTrue(closure["currentness_participation_remained_participation"])
        self.assertTrue(closure["current_carrier_not_selected"])
        for key in (
            "winning_carrier_selected",
            "losing_carrier_invalidated",
            "carrier_hierarchy_created",
            "distributed_standing_created",
            "source_replaced",
            "currentness_created",
            "authority_created",
            "permission_created",
            "continuation_authorized",
            "additional_carrier_experiment_authorized",
            "distributed_operation_authorized",
            "closure_authorized_expansion",
            "self_orientation_successor_forced",
            "conformance_successor_forced",
        ):
            self.assertFalse(closure[key], key)

    def test_bounded_correspondence_checks_include_v8_specific_checks(self) -> None:
        result = self._synthetic_success()
        checks = result["bounded_correspondence_checks"]
        names = {check["check_name"] for check in checks}
        self.assertTrue(EXPECTED_CHECK_NAMES.issubset(names))
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertEqual(result["current_self_orientation_summary"]["failed_check_count"], 0)

    def test_summary_helper_preserves_bounded_v8_posture(self) -> None:
        result = self._synthetic_success()
        summary = resolver.build_current_self_orientation_summary(result)
        for key in (
            "outcome",
            "block_code",
            "block_reason",
            "selected_top_level_basis_ids",
            "selected_v7_self_orientation_id",
            "selected_current_body_conformance_v2_id",
            "selected_multi_carrier_relation_id",
            "selected_multi_carrier_relation_conformance_id",
            "selected_multi_carrier_relation_conformance_closure_id",
            "current_governing_basis_recognized",
            "current_body_conformance_v2_recognized",
            "carrier_role_emission_recognized",
            "carrier_local_emission_admission_recognized",
            "cross_carrier_divergence_recognized",
            "cross_carrier_currentness_participation_recognized",
            "multi_carrier_relation_recognized",
            "multi_carrier_relation_conformance_recognized",
            "multi_carrier_relation_conformance_closure_recognized",
            "relation_conformance_closure_meaning_recorded",
            "relation_conformance_closure_non_meaning_recorded",
            "carrier_b_returned_receipt_evidence_remains_downstream",
            "visible_refusal_remains_visible",
            "visible_divergence_remains_visible",
            "currentness_participation_remained_participation",
            "current_carrier_not_selected",
            "no_winning_losing_carrier_collapse_occurred",
            "carrier_hierarchy_stayed_false",
            "distributed_standing_stayed_false",
            "source_currentness_authority_permission_stayed_false",
            "continuation_stayed_false",
            "additional_carrier_experiment_authorization_stayed_false",
            "distributed_operation_authorization_stayed_false",
            "self_orientation_conformance_successor_not_forced",
            "correspondence_checks_passed",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(summary["outcome"], "SELF_ORIENTED")
        self.assertTrue(summary["correspondence_checks_passed"])
        self.assertTrue(summary["source_currentness_authority_permission_stayed_false"])

    def test_path_based_resolution_uses_v7_path_without_upgrading_relation_band(self) -> None:
        result = resolver.resolve_current_self_orientation()
        if result["outcome"] != "SELF_ORIENTED":
            self.skipTest("No standing v8 self-oriented artifact line is available")
        v7_path = _repo_path(
            result["selected_orientation_inputs"]["selected_current_self_orientation_v7_result"]["path"]
        )
        if v7_path is None or not v7_path.exists():
            self.skipTest("No standing v7 artifact path exposed")
        from_path = resolver.resolve_current_self_orientation_from_path(v7_path)
        self.assert_top_level_shape(from_path)
        self.assertEqual(from_path["outcome"], "SELF_ORIENTED")
        self.assertTrue(from_path["recognized_multi_carrier_relation_conformance_closure_surfaces"]["recognized"])
        self.assertFalse(
            from_path["recognized_multi_carrier_relation_conformance_closure_surfaces"][
                "current_or_governing_basis"
            ]
        )

    def test_write_behavior_with_explicit_path(self) -> None:
        result = self._synthetic_success()
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "nested" / "v8_result.json"
            written = resolver.write_current_self_orientation_result(result, output)
            self.assertEqual(written, output)
            self.assertTrue(written.exists())
            parsed = _read_json(written)
            self.assertTrue(TOP_LEVEL_SECTIONS.issubset(parsed))
            self.assertEqual(parsed["outcome"], "SELF_ORIENTED")

    def test_default_write_uses_v8_root_and_numeric_suffix(self) -> None:
        result = self._synthetic_success()
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "v8_output"
            with mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V8_ROOT", root):
                first = resolver.write_current_self_orientation_result(result)
                second = resolver.write_current_self_orientation_result(result)
            self.assertEqual(first.parent, root)
            self.assertEqual(second.parent, root)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__current_self_orientation_v8_result.json"))
            self.assertTrue(second.stem.endswith("_001"))

    def test_non_mutation_posture_for_inputs_and_artifacts(self) -> None:
        input_v7 = _v7()
        original = copy.deepcopy(input_v7)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            paths = sorted(root.rglob("*.json"))
            before = _snapshot(paths)
            with self._patch_roots(root):
                first = resolver.resolve_current_self_orientation(body_pass_result=input_v7)
                second = resolver.resolve_current_self_orientation(body_pass_result=input_v7)
            after = _snapshot(paths)
        self.assertEqual(input_v7, original)
        self.assertEqual(before, after)
        self.assertEqual(first["outcome"], "SELF_ORIENTED")
        self.assertEqual(second["outcome"], "SELF_ORIENTED")

    def test_missing_v7_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(resolver, "CURRENT_SELF_ORIENTATION_V7_ROOT", Path(tmp) / "empty"):
                result = resolver.resolve_current_self_orientation()
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "SELF_ORIENTATION_V7_MISSING")

    def test_v7_not_self_oriented_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            with self._patch_roots(root):
                result = resolver.resolve_current_self_orientation(body_pass_result=_v7("BLOCKED"))
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "SELF_ORIENTATION_V7_NOT_SELF_ORIENTED")

    def test_current_body_conformance_v2_missing_or_not_conformant_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            empty_v2 = root / "empty_v2"
            empty_v2.mkdir()
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "CURRENT_BODY_CONFORMANCE_PASS_V2_ROOT",
                empty_v2,
            ):
                missing = resolver.resolve_current_self_orientation(body_pass_result=_v7())
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_body_conformance_v2",
                return_value=(None, _v2("BLOCKED")),
            ):
                not_conformant = resolver.resolve_current_self_orientation(body_pass_result=_v7())
        self.assertEqual(missing["block"]["block_code"], "CURRENT_BODY_CONFORMANCE_V2_MISSING")
        self.assertEqual(
            not_conformant["block"]["block_code"],
            "CURRENT_BODY_CONFORMANCE_V2_NOT_BODY_CONFORMANT",
        )

    def test_relation_missing_or_not_recognized_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            invalid_relation = _relation()
            invalid_relation["outcome"] = "NO_MULTI_CARRIER_RELATION"
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation",
                return_value=(None, None),
            ):
                missing = resolver.resolve_current_self_orientation(body_pass_result=_v7())
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation",
                return_value=(None, invalid_relation),
            ):
                not_recognized = resolver.resolve_current_self_orientation(body_pass_result=_v7())
        self.assertEqual(missing["block"]["block_code"], "MULTI_CARRIER_RELATION_MISSING")
        self.assertEqual(not_recognized["block"]["block_code"], "MULTI_CARRIER_RELATION_NOT_RECOGNIZED")

    def test_relation_conformance_missing_or_not_conformant_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            invalid = _conformance()
            invalid["outcome"] = "MULTI_CARRIER_RELATION_NONCONFORMANT"
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation_conformance",
                return_value=(None, None),
            ):
                missing = resolver.resolve_current_self_orientation(body_pass_result=_v7())
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation_conformance",
                return_value=(None, invalid),
            ):
                not_conformant = resolver.resolve_current_self_orientation(body_pass_result=_v7())
        self.assertEqual(missing["block"]["block_code"], "MULTI_CARRIER_RELATION_CONFORMANCE_MISSING")
        self.assertEqual(
            not_conformant["block"]["block_code"],
            "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CONFORMANT",
        )

    def test_relation_conformance_closure_missing_or_not_closed_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            invalid = _closure()
            invalid["outcome"] = "MULTI_CARRIER_RELATION_CONFORMANCE_NOT_CLOSED"
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation_closure",
                return_value=(None, None),
            ):
                missing = resolver.resolve_current_self_orientation(body_pass_result=_v7())
            with self._patch_roots(root), mock.patch.object(
                resolver,
                "_select_relation_closure",
                return_value=(None, invalid),
            ):
                not_closed = resolver.resolve_current_self_orientation(body_pass_result=_v7())
        self.assertEqual(
            missing["block"]["block_code"],
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_MISSING",
        )
        self.assertEqual(
            not_closed["block"]["block_code"],
            "MULTI_CARRIER_RELATION_CONFORMANCE_CLOSURE_NOT_CLOSED",
        )

    def test_relation_closure_leak_blocks(self) -> None:
        cases = [
            (
                {"distributed_standing_created": True},
                "RELATION_CLOSURE_DISTRIBUTED_STANDING_LEAK",
            ),
            ({"current_carrier_selected": True}, "RELATION_CLOSURE_CURRENTNESS_LEAK"),
            ({"authority_created": True}, "RELATION_CLOSURE_AUTHORITY_PERMISSION_LEAK"),
            ({"carrier_hierarchy_created": True}, "RELATION_CLOSURE_CARRIER_HIERARCHY_LEAK"),
            ({"continuation_authorized": True}, "RELATION_CLOSURE_CONTINUATION_LEAK"),
            (
                {"additional_carrier_experiment_authorized": True},
                "RELATION_CLOSURE_ADDITIONAL_CARRIER_EXPERIMENT_LEAK",
            ),
            (
                {"distributed_operation_authorized": True},
                "RELATION_CLOSURE_DISTRIBUTED_OPERATION_LEAK",
            ),
            (
                {
                    "self_orientation_successor_forced": True,
                    "closure_authorized_expansion": True,
                },
                "RELATION_CLOSURE_SUCCESSOR_PRESSURE_LEAK",
            ),
        ]
        for updates, expected_code in cases:
            with self.subTest(expected_code=expected_code), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                _write_artifact_set(root, closure_updates=updates)
                with self._patch_roots(root):
                    result = resolver.resolve_current_self_orientation(body_pass_result=_v7())
                self.assertEqual(result["outcome"], "BLOCKED")
                self.assertEqual(result["block"]["block_code"], expected_code)

    def test_relation_band_upgraded_to_governing_basis_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root)
            with self._patch_roots(root):
                result = resolver.resolve_current_self_orientation(
                    body_pass_result=_v7(upstream=False)
                )
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "RELATION_BAND_UPGRADED_TO_GOVERNING_BASIS")

    def test_latest_file_currentness_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            _write_artifact_set(root, closure_updates={"latest_file_currentness": True})
            with self._patch_roots(root):
                result = resolver.resolve_current_self_orientation(body_pass_result=_v7())
        self.assertEqual(result["outcome"], "BLOCKED")
        self.assertEqual(result["block"]["block_code"], "LATEST_FILE_CURRENTNESS_REFUSED")

    def test_non_claims_are_false_for_success(self) -> None:
        result = self._synthetic_success()
        self.assert_false_non_claims(result)


if __name__ == "__main__":
    unittest.main()
