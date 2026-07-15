"""Bounded tests for the successor current self-orientation resolver.

This suite exercises
``src/resolve_current_self_orientation_v2.py`` as one bounded internal
self-recognition successor over already-standing artifacts.

It verifies that current self-orientation v2 remains:

- internal rather than external-reader-facing
- derived rather than authoritative
- proportioned to its selected source surfaces
- non-mutating
- explicit about source, derivative, and operator-facing distinction
- explicit about currentness without recency shortcuts
- aligned to the live continuity-transfer-receipt receipt shape
- preserving already-selected basis on downstream blocked outcomes

This is not a whole-body recap suite, a README/orientation layer, a governance
doctrine suite, or a workflow/orchestration harness.
"""

from __future__ import annotations

import contextlib
import copy
import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any, Iterator, Mapping
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO_ROOT / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))


import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_builder
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder
import openai_api_vessel__bounded_current_state_read_v3 as vessel_resolver
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as authority_resolver
import resolve_current_self_orientation_v2 as orientation_v2
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import resolve_operator_facing_terminal_brief__bounded_current_state_read as brief_resolver
import run_integrity_host_v0_min_coexistence_v0_body_pass as body_pass_resolver


EXPECTED_RESULT_KEYS = {
    "current_self_orientation_v2_metadata",
    "selected_orientation_inputs",
    "recognized_current_executable_core_line",
    "recognized_governing_effective_basis",
    "recognized_current_state_surfaces",
    "recognized_continuity_surfaces",
    "recognized_derivative_surfaces",
    "recognized_operator_facing_surfaces",
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

EXPECTED_SELECTED_INPUT_KEYS = {
    "selected_body_pass_result",
    "selected_seam_result",
    "selected_action_permission_result",
    "selected_participation_result",
    "selected_receipt_result",
    "selected_transfer_result",
    "selected_touch_permission_result",
    "selected_source_surface",
    "selected_current_state_answer_read_result",
    "selected_current_state_query_results",
    "selected_current_state_what_stands_now_result",
    "selected_current_state_what_remains_open_results",
    "selected_vessel_results",
    "selected_operator_terminal_brief_results",
    "selected_effective_references",
}

EXPECTED_SUCCESS_CHECK_NAMES = {
    "current_self_orientation_uses_explicit_anchor_or_successful_filtered_discovery",
    "current_body_pass_posture_booleans_are_true",
    "every_named_source_surface_is_readable",
    "governing_effective_basis_is_explicit_not_latest_file_guessing",
    "current_state_answer_read_is_answered_and_corresponds",
    "current_state_query_results_are_visible_and_coherent",
    "what_stands_now_result_is_answered_and_current",
    "what_remains_open_results_are_visible_and_open",
    "touch_permission_is_admissibility_not_general_authority",
    "continuity_transfer_and_receipt_remain_transfer_and_receipt",
    "received_derivative_participation_and_action_permission_remain_derivative",
    "continuity_memory_seam_and_v0_body_pass_remain_non_final",
    "bounded_vessel_results_are_present_and_derivative",
    "operator_terminal_brief_results_are_present_and_operator_facing_derivative",
    "open_surfaces_are_not_converted_to_completed",
    "blocked_or_refused_surfaces_remain_visible_when_present",
    "non_claims_remain_false_and_carried_forward",
    "self_orientation_distinguishes_current_governing_derivative_open_blocked_touch_categories",
    "self_orientation_does_not_over_mirror_into_whole_body_replacement",
    "self_orientation_does_not_under_mirror_required_standing_posture",
}

DECLARED_BLOCK_CODES = {
    "NO_SELF_ORIENTATION_SOURCE_BASIS",
    "REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
    "SOURCE_ARTIFACT_MALFORMED",
    "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS",
    "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED",
    "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING",
    "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
    "LATEST_FILE_RECENCY_REFUSED",
    "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY",
    "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY",
    "OPEN_SURFACE_TREATED_AS_COMPLETED",
    "BLOCKED_OR_REFUSED_SURFACE_HIDDEN",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "CORRESPONDENCE_CHECK_FAILED",
    "OVER_MIRRORING_REFUSED",
    "UNDER_MIRRORING_REFUSED",
    "MULTIPLE_CANDIDATE_CURRENT_SURFACES_CONFLICT_UNRESOLVED",
    "EXTERNAL_READER_ORIENTATION_ATTEMPTED",
    "HAND_MAINTAINED_SUMMARY_SEAM_ATTEMPTED",
}

REQUIRED_FALSE_NON_CLAIMS = {
    "continuity_completed",
    "source_replaced",
    "standing_upgraded",
    "latest_file_currentness",
    "recency_fraud",
    "replayed_into_live_host",
    "merged_into_local_state",
    "authority_assigned_by_model",
    "authority_assigned_by_brief",
}

PATH_EQUIVALENCE_KEYS = [
    "selected_orientation_inputs",
    "recognized_current_executable_core_line",
    "recognized_governing_effective_basis",
    "recognized_current_state_surfaces",
    "recognized_continuity_surfaces",
    "recognized_derivative_surfaces",
    "recognized_operator_facing_surfaces",
    "recognized_open_surfaces",
    "recognized_blocked_or_refused_surfaces",
    "recognized_touch_admissibility_surfaces",
    "current_self_orientation_summary",
    "non_claims",
]


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
    digests: dict[str, str] = {}
    if not root.exists():
        return digests
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digests[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


class CurrentSelfOrientationV2Tests(unittest.TestCase):
    maxDiff = None
    _live_result_cache: dict[str, Any] | None = None

    def live_result(self) -> dict[str, Any]:
        cls = type(self)
        if cls._live_result_cache is None:
            cls._live_result_cache = orientation_v2.resolve_current_self_orientation()
        return copy.deepcopy(cls._live_result_cache)

    def relative_path(self, temp_root: Path, path: Path | str) -> str:
        return str(Path(path).resolve().relative_to(temp_root.resolve()))

    def effective_references(
        self,
        temp_root: Path,
        paths: Mapping[str, Path],
    ) -> dict[str, str]:
        return {
            "effective_authority_artifact_path": self.relative_path(
                temp_root,
                paths["authority"],
            ),
            "effective_family_packet_path": self.relative_path(
                temp_root,
                paths["family"],
            ),
            "effective_status_packet_path": self.relative_path(
                temp_root,
                paths["status"],
            ),
            "effective_current_governing_packet_path": self.relative_path(
                temp_root,
                paths["governing"],
            ),
            "effective_source_run_path": self.relative_path(
                temp_root,
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_scenarios"
                / "run_20260424T000000_000000Z",
            ),
            "effective_ingress_run_path": self.relative_path(
                temp_root,
                temp_root
                / "artifacts"
                / "integrity_host_v0_min_coexistence_receiving_ingress"
                / "run_20260424T000000_000000Z",
            ),
        }

    def non_claims(self, defaults: Mapping[str, Any]) -> dict[str, bool]:
        return {key: False for key in defaults}

    def write_marker_files(self, temp_root: Path) -> None:
        source_run = (
            temp_root
            / "artifacts"
            / "integrity_host_v0_min_coexistence_scenarios"
            / "run_20260424T000000_000000Z"
        )
        ingress_run = (
            temp_root
            / "artifacts"
            / "integrity_host_v0_min_coexistence_receiving_ingress"
            / "run_20260424T000000_000000Z"
        )
        comparison = (
            temp_root
            / "artifacts"
            / "integrity_host_v0_min_coexistence_source_and_ingress_run_comparison"
            / "comparison_20260424T000000_000000Z.json"
        )
        source_run.mkdir(parents=True, exist_ok=True)
        ingress_run.mkdir(parents=True, exist_ok=True)
        write_json(
            comparison,
            {
                "comparison_id": "comparison_20260424T000000_000000Z",
                "source_run_path": str(source_run.relative_to(temp_root)),
                "ingress_run_path": str(ingress_run.relative_to(temp_root)),
                "outcome": "MATCHED",
            },
        )

    def canonical_core_execution_file(self) -> str:
        return orientation_v2.CANONICAL_CORE_EXECUTION_FILE

    def authority_artifact(
        self,
        effective_refs: Mapping[str, str],
    ) -> dict[str, Any]:
        return {
            "canonical_execution_line": {
                "core_execution_file": self.canonical_core_execution_file(),
            },
            "candidate_runs": [
                {"run_directory_path": effective_refs["effective_source_run_path"]},
                {
                    "run_directory_path": (
                        "artifacts/integrity_host_v0_min_coexistence_scenarios/older_run"
                    )
                },
            ],
            "authority_decision": {
                "eligible_candidate_count": 1,
                "selected_source_run_directory_path": effective_refs[
                    "effective_source_run_path"
                ],
                "selected_ingress_run_directory_path": effective_refs[
                    "effective_ingress_run_path"
                ],
                "selected_comparison_artifact_path": (
                    "artifacts/"
                    "integrity_host_v0_min_coexistence_source_and_ingress_run_comparison/"
                    "comparison_20260424T000000_000000Z.json"
                ),
                "decision": "single_eligible_candidate_selected",
                "decision_reason": "bounded current execution authority",
            },
        }

    def run_family_packet(
        self,
        effective_refs: Mapping[str, str],
    ) -> dict[str, Any]:
        return {
            "canonical_execution_line": {
                "core_execution_file": self.canonical_core_execution_file(),
            },
            "authority_reference": {
                "selected_source_run_path": effective_refs["effective_source_run_path"],
                "selected_ingress_run_path": effective_refs["effective_ingress_run_path"],
                "authority_decision": "single_eligible_candidate_selected",
                "authority_decision_reason": "bounded current execution authority",
            },
            "currentness_status": {
                "preserved_run_count": 2,
                "eligible_run_count": 1,
            },
            "non_claims": self.non_claims(family_builder.NON_CLAIM_DEFAULTS),
        }

    def preserved_run_status_packet(
        self,
        effective_refs: Mapping[str, str],
    ) -> dict[str, Any]:
        return {
            "canonical_execution_line": {
                "core_execution_file": self.canonical_core_execution_file(),
            },
            "authority_reference": {
                "selected_source_run_path": effective_refs["effective_source_run_path"],
                "authority_decision": "single_eligible_candidate_selected",
                "authority_decision_reason": "bounded current execution authority",
            },
            "aggregate_status_counts": {
                "preserved_run_count": 2,
                "eligible_run_count": 1,
                "current_authority_run_count": 1,
                "preserved_eligible_non_authority_count": 1,
                "preserved_ineligible_count": 0,
            },
            "non_claims": self.non_claims(status_builder.NON_CLAIM_DEFAULTS),
        }

    def current_governing_packet(
        self,
        effective_refs: Mapping[str, str],
    ) -> dict[str, Any]:
        return {
            "canonical_execution_line": {
                "core_execution_file": self.canonical_core_execution_file(),
            },
            "authority_reference": {
                "authority_decision": "single_eligible_candidate_selected",
                "authority_decision_reason": "bounded current execution authority",
            },
            "current_governing_run": {
                "source_run_directory_path": effective_refs["effective_source_run_path"],
                "matched_ingress_run_path": effective_refs["effective_ingress_run_path"],
            },
            "preserved_non_governing_runs": [
                {
                    "source_run_directory_path": (
                        "artifacts/integrity_host_v0_min_coexistence_scenarios/older_run"
                    )
                }
            ],
            "governing_scope": {
                "governing_is_bounded": True,
                "governing_applies_to_current_execution_line": True,
                "preserved_non_governing_runs_remain_preserved": True,
                "current_authority_does_not_erase_preserved_runs": True,
            },
            "non_claims": self.non_claims(governing_builder.NON_CLAIM_DEFAULTS),
        }

    def answer_read_result(
        self,
        effective_refs: Mapping[str, str],
        *,
        answer_read_id: str,
    ) -> dict[str, Any]:
        output = dict(effective_refs)
        output.update(
            {
                "application_basis": "bounded_application_basis",
                "answer_read_basis": "bounded_answer_read_basis",
            }
        )
        return {
            "answer_read_metadata": {
                "answer_read_result_id": answer_read_id,
                "answer_read_result_type": "IAMMAI_CURRENT_STATE_ANSWER_READ_RESULT",
                "answer_read_result_version": "0.1.0",
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": answer_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_application": {
                "current_state_application_result_id": "current_state_application_001",
            },
            "effective_answer_read_inputs": dict(effective_refs),
            "checks": [
                {"check_name": "current_state_application_result_readable", "passed": True}
            ],
            "outcome": answer_resolver.OUTCOME_ANSWERED,
            "block": {"block_code": None, "block_reason": None},
            "answer_read_output": output,
            "non_claims": self.non_claims(answer_resolver.NON_CLAIM_DEFAULTS),
        }

    def query_result(
        self,
        effective_refs: Mapping[str, str],
        *,
        query_id: str,
        answer_read_id: str,
        outcome: str = query_resolver.OUTCOME_ANSWERED_QUERY,
        block_code: str | None = None,
    ) -> dict[str, Any]:
        return {
            "query_metadata": {
                "query_result_id": query_id,
                "query_result_type": "IAMMAI_CURRENT_STATE_QUERY_RESULT",
                "query_result_version": "0.1.0",
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": query_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_answer_read": {
                "current_state_answer_read_result_id": answer_read_id,
            },
            "query_request": {
                "query_target": "bounded_current_state",
            },
            "effective_query_inputs": dict(effective_refs),
            "checks": [{"check_name": "bounded_query_scope", "passed": True}],
            "outcome": outcome,
            "block": {
                "block_code": block_code,
                "block_reason": None if block_code is None else "blocked query",
            },
            "query_answer": {
                "answered_field_names": [
                    "current_authority_artifact_path",
                    "answer_read_basis",
                ],
            },
            "non_claims": self.non_claims(query_resolver.NON_CLAIM_DEFAULTS),
        }

    def what_stands_now_result(
        self,
        temp_root: Path,
        effective_refs: Mapping[str, str],
        answer_path: Path,
        *,
        stand_id: str,
        answer_read_id: str,
    ) -> dict[str, Any]:
        return {
            "what_stands_now_metadata": {
                "what_stands_now_result_id": stand_id,
                "what_stands_now_result_type": "IAMMAI_CURRENT_STATE_WHAT_STANDS_NOW_RESULT",
                "what_stands_now_result_version": "0.1.0",
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": stand_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_answer_read": {
                "current_state_answer_read_result_path": self.relative_path(
                    temp_root,
                    answer_path,
                ),
                "current_state_answer_read_result_id": answer_read_id,
            },
            "what_stands_now_request": {
                "requested_stand_now_fields": [
                    "current_authority_artifact_path",
                    "answer_read_basis",
                ],
            },
            "effective_stand_now_inputs": dict(effective_refs),
            "checks": [{"check_name": "bounded_stand_now_scope", "passed": True}],
            "outcome": stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            "block": {"block_code": None, "block_reason": None},
            "what_stands_now_answer": {
                "current_authority_artifact_path": effective_refs[
                    "effective_authority_artifact_path"
                ],
                "answer_read_basis": "bounded_answer_read_basis",
            },
            "what_stands_now_summary": {
                "selected_current_state_answer_read_id": answer_read_id,
                "outcome": stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            },
            "non_claims": self.non_claims(stand_resolver.NON_CLAIM_DEFAULTS),
        }

    def what_remains_open_result(
        self,
        *,
        open_id: str,
        answer_read_id: str,
        effective_refs: Mapping[str, str],
        outcome: str,
        block_code: str | None,
    ) -> dict[str, Any]:
        answer = (
            {
                "continuity_completed": False,
                "standing_upgraded": False,
                "answer_read_basis": "bounded_answer_read_basis",
            }
            if outcome == open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN
            else {}
        )
        return {
            "what_remains_open_metadata": {
                "what_remains_open_result_id": open_id,
                "what_remains_open_result_type": (
                    "IAMMAI_CURRENT_STATE_WHAT_REMAINS_OPEN_RESULT"
                ),
                "what_remains_open_result_version": "0.1.0",
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": open_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_answer_read": {
                "current_state_answer_read_result_id": answer_read_id,
            },
            "what_remains_open_request": {
                "requested_open_fields": [
                    "continuity_completed",
                    "standing_upgraded",
                    "answer_read_basis",
                ],
            },
            "effective_open_inputs": dict(effective_refs),
            "checks": [{"check_name": "bounded_open_scope", "passed": True}],
            "outcome": outcome,
            "block": {
                "block_code": block_code,
                "block_reason": (
                    None if block_code is None else "blocked open surface"
                ),
            },
            "what_remains_open_answer": answer,
            "what_remains_open_summary": {
                "selected_current_state_answer_read_id": answer_read_id,
                "outcome": outcome,
            },
            "non_claims": self.non_claims(open_resolver.NON_CLAIM_DEFAULTS),
        }

    def touch_permission_result(
        self,
        temp_root: Path,
        stand_path: Path,
        *,
        touch_id: str,
        stand_id: str,
    ) -> dict[str, Any]:
        return {
            "touch_permission_metadata": {
                "touch_permission_result_id": touch_id,
                "touch_permission_result_type": touch_resolver.TOUCH_PERMISSION_RESULT_TYPE,
                "touch_permission_result_version": (
                    touch_resolver.TOUCH_PERMISSION_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": touch_resolver.RESOLVER_MODULE,
            },
            "selected_current_state_surface": {
                "selected_surface_path": self.relative_path(temp_root, stand_path),
                "selected_surface_id": stand_id,
                "selected_surface_result_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
            },
            "touch_request": {"requested_touch_class": "derivative"},
            "checks": [{"check_name": "touch_is_bounded", "passed": True}],
            "outcome": touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            "block": {"block_code": None, "block_reason": None},
            "admitted_touch_scope": {
                "admitted_touch_class": "derivative",
                "admitted_source_surface_id": stand_id,
            },
            "non_claims": self.non_claims(touch_resolver.NON_CLAIM_DEFAULTS),
        }

    def transfer_result(
        self,
        temp_root: Path,
        stand_path: Path,
        touch_path: Path,
        effective_refs: Mapping[str, str],
        *,
        transfer_id: str,
        touch_id: str,
        stand_id: str,
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_metadata": {
                "continuity_transfer_result_id": transfer_id,
                "continuity_transfer_result_type": (
                    transfer_resolver.CONTINUITY_TRANSFER_RESULT_TYPE
                ),
                "continuity_transfer_result_version": (
                    transfer_resolver.CONTINUITY_TRANSFER_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": transfer_resolver.RESOLVER_MODULE,
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_outcome": (
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "touch_permission_reference": {
                "touch_permission_result_path": self.relative_path(temp_root, touch_path),
                "touch_permission_result_id": touch_id,
            },
            "transfer_request": {
                "continuity_transfer_request_id": "continuity_transfer_request_001",
                "transfer_class": "derivative",
                "requested_transfer_fields": ["answer_read_basis"],
                "transfer_basis": "bounded derivative transfer",
            },
            "checks": [{"check_name": "transfer_is_bounded", "passed": True}],
            "outcome": transfer_resolver.OUTCOME_TRANSFERRED,
            "block": {"block_code": None, "block_reason": None},
            "transfer_payload": {
                "payload_derivative_status": "carried_derivative",
                "source_remains_source": True,
                "carried_fields": {"answer_read_basis": "bounded_answer_read_basis"},
                "carried_references": {
                    "selected_source_surface_path": self.relative_path(
                        temp_root,
                        stand_path,
                    ),
                    "selected_source_surface_effective_references": dict(effective_refs),
                    "touch_permission_result_path": self.relative_path(
                        temp_root,
                        touch_path,
                    ),
                    "touch_permission_result_id": touch_id,
                },
            },
            "transfer_summary": {
                "transferred_field_names": ["answer_read_basis"],
            },
            "non_claims": self.non_claims(transfer_resolver.NON_CLAIM_DEFAULTS),
        }

    def receipt_result(
        self,
        temp_root: Path,
        transfer_path: Path,
        stand_path: Path,
        touch_path: Path,
        effective_refs: Mapping[str, str],
        *,
        receipt_id: str,
        transfer_id: str,
        touch_id: str,
        stand_id: str,
        payload_mode: str = "received_payload",
    ) -> dict[str, Any]:
        payload = {
            "payload_receipt_status": "received_carried_derivative",
            "source_remains_source": True,
            "carried_derivative_remains_derivative": True,
            "received_fields": {"answer_read_basis": "bounded_answer_read_basis"},
            "received_references": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
                "selected_source_surface_path": self.relative_path(
                    temp_root,
                    stand_path,
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
                "touch_permission_result_path": self.relative_path(
                    temp_root,
                    touch_path,
                ),
                "touch_permission_result_id": touch_id,
            },
        }
        result = {
            "continuity_transfer_receipt_metadata": {
                "continuity_transfer_receipt_result_id": receipt_id,
                "continuity_transfer_receipt_result_type": (
                    receipt_resolver.CONTINUITY_TRANSFER_RECEIPT_RESULT_TYPE
                ),
                "continuity_transfer_receipt_result_version": (
                    receipt_resolver.CONTINUITY_TRANSFER_RECEIPT_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": receipt_resolver.RESOLVER_MODULE,
            },
            "selected_transfer_result": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
                "selected_transfer_result_outcome": transfer_resolver.OUTCOME_TRANSFERRED,
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_outcome": (
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "touch_permission_reference": {
                "touch_permission_result_path": self.relative_path(temp_root, touch_path),
                "touch_permission_result_id": touch_id,
            },
            "receipt_request": {
                "continuity_transfer_receipt_request_id": (
                    "continuity_transfer_receipt_request_001"
                ),
                "receipt_class": "bounded_acceptance",
                "requested_receipt_fields": ["answer_read_basis"],
            },
            "checks": [{"check_name": "receipt_is_bounded", "passed": True}],
            "outcome": receipt_resolver.OUTCOME_RECEIVED,
            "block": {"block_code": None, "block_reason": None},
            "receipt_summary": {
                "received_field_names": ["answer_read_basis"],
            },
            "non_claims": self.non_claims(receipt_resolver.NON_CLAIM_DEFAULTS),
        }
        if payload_mode in {"receipt_payload", "both"}:
            result["receipt_payload"] = dict(payload)
        if payload_mode in {"received_payload", "both"}:
            result["received_payload"] = dict(payload)
        return result

    def participation_result(
        self,
        temp_root: Path,
        receipt_path: Path,
        transfer_path: Path,
        stand_path: Path,
        effective_refs: Mapping[str, str],
        *,
        participation_id: str,
        receipt_id: str,
        transfer_id: str,
        stand_id: str,
    ) -> dict[str, Any]:
        return {
            "received_derivative_participation_metadata": {
                "received_derivative_participation_result_id": participation_id,
                "received_derivative_participation_result_type": (
                    participation_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_RESULT_TYPE
                ),
                "received_derivative_participation_result_version": (
                    participation_resolver.RECEIVED_DERIVATIVE_PARTICIPATION_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": participation_resolver.RESOLVER_MODULE,
            },
            "selected_receipt_result": {
                "selected_receipt_result_path": self.relative_path(temp_root, receipt_path),
                "selected_receipt_result_id": receipt_id,
            },
            "selected_transfer_result": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_outcome": (
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "participation_request": {
                "received_derivative_participation_request_id": (
                    "received_derivative_participation_request_001"
                ),
                "participant_class": "local_derivation",
                "use_class": "derivative",
            },
            "checks": [{"check_name": "participation_is_bounded", "passed": True}],
            "outcome": participation_resolver.OUTCOME_PARTICIPATED,
            "block": {"block_code": None, "block_reason": None},
            "participation_payload": {
                "payload_participation_status": "participated_received_derivative",
                "source_remains_source": True,
                "receipt_remains_receipt": True,
                "transfer_remains_transfer": True,
                "participation_payload_remains_derivative": True,
            },
            "participation_summary": {
                "participated_field_names": ["answer_read_basis"],
            },
            "non_claims": self.non_claims(participation_resolver.NON_CLAIM_DEFAULTS),
        }

    def action_permission_result(
        self,
        temp_root: Path,
        participation_path: Path,
        receipt_path: Path,
        transfer_path: Path,
        stand_path: Path,
        effective_refs: Mapping[str, str],
        *,
        action_id: str,
        participation_id: str,
        receipt_id: str,
        transfer_id: str,
        stand_id: str,
    ) -> dict[str, Any]:
        return {
            "received_derivative_action_permission_metadata": {
                "received_derivative_action_permission_result_id": action_id,
                "received_derivative_action_permission_result_type": (
                    action_resolver.RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_TYPE
                ),
                "received_derivative_action_permission_result_version": (
                    action_resolver.RECEIVED_DERIVATIVE_ACTION_PERMISSION_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": action_resolver.RESOLVER_MODULE,
            },
            "selected_participation_result": {
                "selected_participation_result_path": self.relative_path(
                    temp_root,
                    participation_path,
                ),
                "selected_participation_result_id": participation_id,
            },
            "selected_receipt_result": {
                "selected_receipt_result_path": self.relative_path(temp_root, receipt_path),
                "selected_receipt_result_id": receipt_id,
            },
            "selected_transfer_result": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "action_permission_request": {
                "received_derivative_action_permission_request_id": (
                    "received_derivative_action_permission_request_001"
                ),
                "actor_class": "local_derivation",
                "action_class": "bounded_read",
            },
            "checks": [{"check_name": "action_permission_is_bounded", "passed": True}],
            "outcome": action_resolver.OUTCOME_ACTION_PERMITTED,
            "block": {"block_code": None, "block_reason": None},
            "action_permission_payload": {
                "payload_action_permission_status": (
                    "permitted_received_derivative_action"
                ),
                "source_remains_source": True,
                "receipt_remains_receipt": True,
                "transfer_remains_transfer": True,
                "participation_remains_participation": True,
                "action_permission_payload_remains_derivative": True,
            },
            "action_permission_summary": {
                "permitted_action_field_names": ["answer_read_basis"],
            },
            "non_claims": self.non_claims(action_resolver.NON_CLAIM_DEFAULTS),
        }

    def seam_result(
        self,
        temp_root: Path,
        action_path: Path,
        participation_path: Path,
        receipt_path: Path,
        transfer_path: Path,
        stand_path: Path,
        effective_refs: Mapping[str, str],
        *,
        seam_id: str,
        action_id: str,
        participation_id: str,
        receipt_id: str,
        transfer_id: str,
        stand_id: str,
    ) -> dict[str, Any]:
        return {
            "continuity_memory_seam_metadata": {
                "continuity_memory_seam_result_id": seam_id,
                "continuity_memory_seam_result_type": (
                    seam_resolver.CONTINUITY_MEMORY_SEAM_RESULT_TYPE
                ),
                "continuity_memory_seam_result_version": (
                    seam_resolver.CONTINUITY_MEMORY_SEAM_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": seam_resolver.RESOLVER_MODULE,
            },
            "selected_action_permission_result": {
                "selected_action_permission_result_path": self.relative_path(
                    temp_root,
                    action_path,
                ),
                "selected_action_permission_result_id": action_id,
                "selected_action_permission_result_outcome": (
                    action_resolver.OUTCOME_ACTION_PERMITTED
                ),
            },
            "selected_participation_result": {
                "selected_participation_result_path": self.relative_path(
                    temp_root,
                    participation_path,
                ),
                "selected_participation_result_id": participation_id,
                "selected_participation_result_outcome": (
                    participation_resolver.OUTCOME_PARTICIPATED
                ),
            },
            "selected_receipt_result": {
                "selected_receipt_result_path": self.relative_path(temp_root, receipt_path),
                "selected_receipt_result_id": receipt_id,
                "selected_receipt_result_outcome": receipt_resolver.OUTCOME_RECEIVED,
            },
            "selected_transfer_result": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
                "selected_transfer_result_outcome": transfer_resolver.OUTCOME_TRANSFERRED,
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_outcome": (
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "closure_posture": {
                "preserved_lineage_without_overwrite": True,
                "correction_by_successor_not_edit": True,
                "currentness_without_recency_fraud": True,
                "derivative_carry_without_source_collapse": True,
                "standing_memory_distinct_from_interpretation_surfaces": True,
            },
            "checks": [
                {"check_name": "continuity_memory_seam_is_bounded", "passed": True}
            ],
            "outcome": seam_resolver.OUTCOME_SEAM_CLOSED,
            "block": {"block_code": None, "block_reason": None},
            "continuity_memory_seam_summary": {
                "selected_action_permission_result_id": action_id,
                "selected_source_surface_id": stand_id,
                "closure_posture": {
                    "currentness_without_recency_fraud": True,
                },
            },
            "non_claims": self.non_claims(seam_resolver.NON_CLAIM_DEFAULTS),
        }

    def body_pass_result(
        self,
        temp_root: Path,
        seam_path: Path,
        action_path: Path,
        participation_path: Path,
        receipt_path: Path,
        transfer_path: Path,
        touch_path: Path,
        stand_path: Path,
        effective_refs: Mapping[str, str],
        *,
        body_pass_id: str,
        seam_id: str,
        action_id: str,
        participation_id: str,
        receipt_id: str,
        transfer_id: str,
        touch_id: str,
        stand_id: str,
        outcome: str = body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED,
    ) -> dict[str, Any]:
        posture = {
            "closure_seam_stands": True,
            "currentness_without_recency_fraud": True,
            "derivative_carry_without_source_collapse": True,
            "lineage_preserved": True,
            "organs_present_and_successful": True,
            "v0_body_reads_as_one_bounded_body": True,
        }
        block = {"block_code": None, "block_reason": None}
        if outcome != body_pass_resolver.OUTCOME_V0_BODY_PASS_CONFIRMED:
            block = {
                "block_code": "TEST_BLOCK",
                "block_reason": "blocked body-pass noise",
            }
        return {
            "v0_body_pass_metadata": {
                "v0_body_pass_result_id": body_pass_id,
                "v0_body_pass_result_type": body_pass_resolver.V0_BODY_PASS_RESULT_TYPE,
                "v0_body_pass_result_version": (
                    body_pass_resolver.V0_BODY_PASS_RESULT_VERSION
                ),
                "generated_at": "2026-04-24T00:00:00Z",
                "runner_module": body_pass_resolver.RUNNER_MODULE,
            },
            "selected_seam_result": {
                "selected_seam_result_path": self.relative_path(temp_root, seam_path),
                "selected_seam_result_id": seam_id,
                "selected_seam_result_outcome": seam_resolver.OUTCOME_SEAM_CLOSED,
            },
            "selected_action_permission_result": {
                "selected_action_permission_result_path": self.relative_path(
                    temp_root,
                    action_path,
                ),
                "selected_action_permission_result_id": action_id,
                "selected_action_permission_result_outcome": (
                    action_resolver.OUTCOME_ACTION_PERMITTED
                ),
            },
            "selected_participation_result": {
                "selected_participation_result_path": self.relative_path(
                    temp_root,
                    participation_path,
                ),
                "selected_participation_result_id": participation_id,
                "selected_participation_result_outcome": (
                    participation_resolver.OUTCOME_PARTICIPATED
                ),
            },
            "selected_receipt_result": {
                "selected_receipt_result_path": self.relative_path(temp_root, receipt_path),
                "selected_receipt_result_id": receipt_id,
                "selected_receipt_result_outcome": receipt_resolver.OUTCOME_RECEIVED,
            },
            "selected_transfer_result": {
                "selected_transfer_result_path": self.relative_path(
                    temp_root,
                    transfer_path,
                ),
                "selected_transfer_result_id": transfer_id,
                "selected_transfer_result_outcome": transfer_resolver.OUTCOME_TRANSFERRED,
            },
            "selected_touch_permission_result": {
                "selected_touch_permission_result_path": self.relative_path(
                    temp_root,
                    touch_path,
                ),
                "selected_touch_permission_result_id": touch_id,
                "selected_touch_permission_result_outcome": (
                    touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH
                ),
            },
            "selected_source_surface": {
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_outcome": (
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
                ),
                "selected_source_surface_effective_references": dict(effective_refs),
            },
            "body_pass_posture": posture,
            "checks": [{"check_name": "v0_body_pass_is_bounded", "passed": True}],
            "outcome": outcome,
            "block": block,
            "v0_body_pass_summary": {
                "selected_seam_result_id": seam_id,
                "selected_source_surface_id": stand_id,
                "body_pass_posture": dict(posture),
            },
            "non_claims": self.non_claims(body_pass_resolver.NON_CLAIM_DEFAULTS),
        }

    def vessel_result(
        self,
        temp_root: Path,
        stand_path: Path,
        effective_refs: Mapping[str, str],
        *,
        vessel_id: str,
        stand_id: str,
        outcome: str,
    ) -> dict[str, Any]:
        selected_source = {
            "selected_source_surface_path": self.relative_path(temp_root, stand_path),
            "selected_source_surface_id": stand_id,
            "selected_source_surface_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
            "selected_source_surface_outcome": (
                stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW
            ),
        }
        block = {"block_code": None, "block_reason": None}
        answer_text: str | None = "bounded derivative answer"
        if outcome != vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ:
            block = {
                "block_code": "TEST_REFUSAL",
                "block_reason": "refused derivative vessel",
            }
            answer_text = None
        return {
            "openai_api_derivative_vessel_v3_metadata": {
                "vessel_result_id": vessel_id,
                "vessel_result_type": vessel_resolver.VESSEL_RESULT_TYPE,
                "vessel_result_version": vessel_resolver.VESSEL_RESULT_VERSION,
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": vessel_resolver.RESOLVER_MODULE,
                "successor_of_module": vessel_resolver.SUCCESSOR_OF_MODULE,
            },
            "selected_source_surface": selected_source,
            "vessel_request": {
                "vessel_request_id": f"{vessel_id}__request",
                "vessel_use_case": vessel_resolver.VESSEL_USE_CASE,
                "admitted_use_class": vessel_resolver.SUPPORTED_USE_CLASS,
                "allowed_source_family": vessel_resolver.ALLOWED_SOURCE_FAMILY,
                "selected_source_surface_id": stand_id,
                "selected_source_surface_path": self.relative_path(temp_root, stand_path),
                "question": "What stands now?",
                "bounded_source_payload": {
                    "effective_authority_artifact_path": effective_refs[
                        "effective_authority_artifact_path"
                    ],
                    "effective_source_run_path": effective_refs[
                        "effective_source_run_path"
                    ],
                    "effective_ingress_run_path": effective_refs[
                        "effective_ingress_run_path"
                    ],
                    "answer_read_basis": "bounded_answer_read_basis",
                },
                "instructions": "bounded derivative read",
            },
            "api_runtime": {
                "model_name_used": "bounded-test-model",
                "api_key_present": False,
            },
            "model_output": {
                "raw_output_text": (
                    None if answer_text is None else json.dumps({"answer": answer_text})
                ),
                "parsed_output": None if answer_text is None else {"answer": answer_text},
                "refusal_signal": None,
            },
            "outcome": outcome,
            "block": block,
            "derivative_answer": {
                "answer": answer_text,
                "answer_basis": "bounded_source_payload",
                "source_remains_source": True,
                "model_output_remains_derivative": True,
            },
            "vessel_summary": {
                "selected_source_surface_id": stand_id,
                "question": "What stands now?",
                "outcome": outcome,
                "block_code": block["block_code"],
                "block_reason": block["block_reason"],
            },
            "non_claims": self.non_claims(vessel_resolver.NON_CLAIM_DEFAULTS),
        }

    def operator_brief_result(
        self,
        temp_root: Path,
        *,
        brief_id: str,
        vessel_path: Path,
        vessel_id: str,
        stand_id: str,
        outcome: str,
    ) -> dict[str, Any]:
        block = {"block_code": None, "block_reason": None}
        brief_text: str | None = "bounded operator terminal brief"
        if outcome != brief_resolver.OUTCOME_BRIEF_RENDERED:
            block = {
                "block_code": "TEST_REFUSAL",
                "block_reason": "refused operator brief",
            }
            brief_text = None
        return {
            "operator_terminal_brief_metadata": {
                "brief_result_id": brief_id,
                "brief_result_type": brief_resolver.BRIEF_RESULT_TYPE,
                "brief_result_version": brief_resolver.BRIEF_RESULT_VERSION,
                "generated_at": "2026-04-24T00:00:00Z",
                "resolver_module": brief_resolver.RESOLVER_MODULE,
            },
            "selected_vessel_result": {
                "selected_vessel_result_path": self.relative_path(temp_root, vessel_path),
                "selected_vessel_result_id": vessel_id,
                "selected_source_surface_id": stand_id,
                "selected_source_surface_family": (
                    brief_resolver.UPSTREAM_ALLOWED_SOURCE_FAMILY
                ),
            },
            "brief_request": {
                "brief_request_id": f"{brief_id}__request",
                "question": "What stands now?",
                "derivative_answer": "bounded derivative answer",
            },
            "brief_output": {
                "brief_text": brief_text,
                "brief_basis": "bounded_derivative_vessel_result",
                "source_remains_source": True,
                "vessel_output_remains_derivative": True,
                "brief_remains_derivative": True,
            },
            "outcome": outcome,
            "block": block,
            "brief_summary": {
                "selected_vessel_result_id": vessel_id,
                "selected_source_surface_id": stand_id,
                "outcome": outcome,
                "block_code": block["block_code"],
                "block_reason": block["block_reason"],
            },
            "non_claims": self.non_claims(brief_resolver.NON_CLAIM_DEFAULTS),
        }

    def build_valid_stack(
        self,
        temp_root: Path,
        *,
        include_blocked_visibility: bool = True,
        include_noise: bool = True,
        receipt_payload_mode: str = "received_payload",
    ) -> dict[str, Any]:
        self.write_marker_files(temp_root)

        paths = {
            "authority": (
                temp_root
                / orientation_v2.EXECUTION_AUTHORITY_ROOT
                / "authority_001.json"
            ),
            "family": (
                temp_root / orientation_v2.RUN_FAMILY_PACKET_ROOT / "family_001.json"
            ),
            "status": (
                temp_root
                / orientation_v2.PRESERVED_RUN_STATUS_PACKET_ROOT
                / "status_001.json"
            ),
            "governing": (
                temp_root
                / orientation_v2.CURRENT_GOVERNING_PACKET_ROOT
                / "governing_001.json"
            ),
            "answer": (
                temp_root
                / orientation_v2.CURRENT_STATE_ANSWER_SURFACE_ROOT
                / "answer_read_001.json"
            ),
            "query": (
                temp_root / orientation_v2.CURRENT_STATE_QUERY_ROOT / "query_001.json"
            ),
            "query_noise": (
                temp_root
                / orientation_v2.CURRENT_STATE_QUERY_ROOT
                / "zzz_query_other.json"
            ),
            "stand": (
                temp_root
                / orientation_v2.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
                / "what_stands_now_001.json"
            ),
            "open": (
                temp_root
                / orientation_v2.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
                / "what_remains_open_001.json"
            ),
            "open_blocked": (
                temp_root
                / orientation_v2.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
                / "what_remains_open_blocked_001.json"
            ),
            "open_noise": (
                temp_root
                / orientation_v2.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
                / "zzz_other_open.json"
            ),
            "touch": (
                temp_root
                / orientation_v2.CURRENT_STATE_TOUCH_PERMISSION_ROOT
                / "touch_permission_001.json"
            ),
            "transfer": (
                temp_root
                / orientation_v2.CONTINUITY_TRANSFER_UNIT_ROOT
                / "transfer_001.json"
            ),
            "receipt": (
                temp_root
                / orientation_v2.CONTINUITY_TRANSFER_RECEIPT_ROOT
                / "receipt_001.json"
            ),
            "participation": (
                temp_root
                / orientation_v2.RECEIVED_DERIVATIVE_PARTICIPATION_ROOT
                / "participation_001.json"
            ),
            "action": (
                temp_root
                / orientation_v2.RECEIVED_DERIVATIVE_ACTION_PERMISSION_ROOT
                / "action_001.json"
            ),
            "seam": (
                temp_root
                / orientation_v2.CONTINUITY_MEMORY_SEAM_ROOT
                / "seam_001.json"
            ),
            "body_pass": (
                temp_root / orientation_v2.V0_BODY_PASS_ROOT / "body_pass_001.json"
            ),
            "body_pass_noise": (
                temp_root
                / orientation_v2.V0_BODY_PASS_ROOT
                / "zzz_body_pass_blocked.json"
            ),
            "vessel_answered": (
                temp_root
                / orientation_v2.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT
                / "vessel_answered_001.json"
            ),
            "vessel_refused": (
                temp_root
                / orientation_v2.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT
                / "vessel_refused_001.json"
            ),
            "vessel_noise": (
                temp_root
                / orientation_v2.OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT
                / "zzz_other_vessel.json"
            ),
            "brief_rendered": (
                temp_root
                / orientation_v2.OPERATOR_TERMINAL_BRIEF_ROOT
                / "brief_rendered_001.json"
            ),
            "brief_refused": (
                temp_root
                / orientation_v2.OPERATOR_TERMINAL_BRIEF_ROOT
                / "brief_refused_001.json"
            ),
            "brief_noise": (
                temp_root
                / orientation_v2.OPERATOR_TERMINAL_BRIEF_ROOT
                / "zzz_other_brief.json"
            ),
            "authority_noise": (
                temp_root
                / orientation_v2.EXECUTION_AUTHORITY_ROOT
                / "zzz_authority_other.json"
            ),
            "family_noise": (
                temp_root
                / orientation_v2.RUN_FAMILY_PACKET_ROOT
                / "zzz_family_other.json"
            ),
            "status_noise": (
                temp_root
                / orientation_v2.PRESERVED_RUN_STATUS_PACKET_ROOT
                / "zzz_status_other.json"
            ),
            "governing_noise": (
                temp_root
                / orientation_v2.CURRENT_GOVERNING_PACKET_ROOT
                / "zzz_governing_other.json"
            ),
        }

        ids = {
            "answer": "current_state_answer_read_001",
            "query": "current_state_query_001",
            "stand": "what_stands_now_result_001",
            "open": "what_remains_open_result_001",
            "open_blocked": "what_remains_open_result_blocked_001",
            "touch": "touch_permission_result_001",
            "transfer": "continuity_transfer_result_001",
            "receipt": "continuity_transfer_receipt_result_001",
            "participation": "received_derivative_participation_result_001",
            "action": "received_derivative_action_permission_result_001",
            "seam": "continuity_memory_seam_result_001",
            "body_pass": "v0_body_pass_result_001",
            "vessel_answered": "bounded_current_state_vessel_result_001",
            "vessel_refused": "bounded_current_state_vessel_result_002",
            "brief_rendered": "operator_terminal_brief_result_001",
            "brief_refused": "operator_terminal_brief_result_002",
        }

        effective_refs = self.effective_references(temp_root, paths)

        write_json(paths["authority"], self.authority_artifact(effective_refs))
        write_json(paths["family"], self.run_family_packet(effective_refs))
        write_json(paths["status"], self.preserved_run_status_packet(effective_refs))
        write_json(paths["governing"], self.current_governing_packet(effective_refs))

        write_json(
            paths["answer"],
            self.answer_read_result(effective_refs, answer_read_id=ids["answer"]),
        )
        write_json(
            paths["query"],
            self.query_result(
                effective_refs,
                query_id=ids["query"],
                answer_read_id=ids["answer"],
            ),
        )
        write_json(
            paths["stand"],
            self.what_stands_now_result(
                temp_root,
                effective_refs,
                paths["answer"],
                stand_id=ids["stand"],
                answer_read_id=ids["answer"],
            ),
        )
        write_json(
            paths["open"],
            self.what_remains_open_result(
                open_id=ids["open"],
                answer_read_id=ids["answer"],
                effective_refs=effective_refs,
                outcome=open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                block_code=None,
            ),
        )
        if include_blocked_visibility:
            write_json(
                paths["open_blocked"],
                self.what_remains_open_result(
                    open_id=ids["open_blocked"],
                    answer_read_id=ids["answer"],
                    effective_refs=effective_refs,
                    outcome=open_resolver.OUTCOME_BLOCKED,
                    block_code="OPEN_ITEMS_REMAIN",
                ),
            )
        write_json(
            paths["touch"],
            self.touch_permission_result(
                temp_root,
                paths["stand"],
                touch_id=ids["touch"],
                stand_id=ids["stand"],
            ),
        )
        write_json(
            paths["transfer"],
            self.transfer_result(
                temp_root,
                paths["stand"],
                paths["touch"],
                effective_refs,
                transfer_id=ids["transfer"],
                touch_id=ids["touch"],
                stand_id=ids["stand"],
            ),
        )
        write_json(
            paths["receipt"],
            self.receipt_result(
                temp_root,
                paths["transfer"],
                paths["stand"],
                paths["touch"],
                effective_refs,
                receipt_id=ids["receipt"],
                transfer_id=ids["transfer"],
                touch_id=ids["touch"],
                stand_id=ids["stand"],
                payload_mode=receipt_payload_mode,
            ),
        )
        write_json(
            paths["participation"],
            self.participation_result(
                temp_root,
                paths["receipt"],
                paths["transfer"],
                paths["stand"],
                effective_refs,
                participation_id=ids["participation"],
                receipt_id=ids["receipt"],
                transfer_id=ids["transfer"],
                stand_id=ids["stand"],
            ),
        )
        write_json(
            paths["action"],
            self.action_permission_result(
                temp_root,
                paths["participation"],
                paths["receipt"],
                paths["transfer"],
                paths["stand"],
                effective_refs,
                action_id=ids["action"],
                participation_id=ids["participation"],
                receipt_id=ids["receipt"],
                transfer_id=ids["transfer"],
                stand_id=ids["stand"],
            ),
        )
        write_json(
            paths["seam"],
            self.seam_result(
                temp_root,
                paths["action"],
                paths["participation"],
                paths["receipt"],
                paths["transfer"],
                paths["stand"],
                effective_refs,
                seam_id=ids["seam"],
                action_id=ids["action"],
                participation_id=ids["participation"],
                receipt_id=ids["receipt"],
                transfer_id=ids["transfer"],
                stand_id=ids["stand"],
            ),
        )
        write_json(
            paths["vessel_answered"],
            self.vessel_result(
                temp_root,
                paths["stand"],
                effective_refs,
                vessel_id=ids["vessel_answered"],
                stand_id=ids["stand"],
                outcome=vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ,
            ),
        )
        if include_blocked_visibility:
            write_json(
                paths["vessel_refused"],
                self.vessel_result(
                    temp_root,
                    paths["stand"],
                    effective_refs,
                    vessel_id=ids["vessel_refused"],
                    stand_id=ids["stand"],
                    outcome=vessel_resolver.OUTCOME_REFUSED,
                ),
            )
        write_json(
            paths["brief_rendered"],
            self.operator_brief_result(
                temp_root,
                brief_id=ids["brief_rendered"],
                vessel_path=paths["vessel_answered"],
                vessel_id=ids["vessel_answered"],
                stand_id=ids["stand"],
                outcome=brief_resolver.OUTCOME_BRIEF_RENDERED,
            ),
        )
        if include_blocked_visibility:
            write_json(
                paths["brief_refused"],
                self.operator_brief_result(
                    temp_root,
                    brief_id=ids["brief_refused"],
                    vessel_path=paths["vessel_refused"],
                    vessel_id=ids["vessel_refused"],
                    stand_id=ids["stand"],
                    outcome=brief_resolver.OUTCOME_REFUSED,
                ),
            )

        write_json(
            paths["body_pass"],
            self.body_pass_result(
                temp_root,
                paths["seam"],
                paths["action"],
                paths["participation"],
                paths["receipt"],
                paths["transfer"],
                paths["touch"],
                paths["stand"],
                effective_refs,
                body_pass_id=ids["body_pass"],
                seam_id=ids["seam"],
                action_id=ids["action"],
                participation_id=ids["participation"],
                receipt_id=ids["receipt"],
                transfer_id=ids["transfer"],
                touch_id=ids["touch"],
                stand_id=ids["stand"],
            ),
        )

        if include_noise:
            noise_refs = dict(effective_refs)
            noise_refs["effective_source_run_path"] = (
                "artifacts/"
                "integrity_host_v0_min_coexistence_scenarios/"
                "run_20990101T000000_000000Z"
            )
            noise_refs["effective_ingress_run_path"] = (
                "artifacts/"
                "integrity_host_v0_min_coexistence_receiving_ingress/"
                "run_20990101T000000_000000Z"
            )
            write_json(paths["authority_noise"], self.authority_artifact(noise_refs))
            write_json(paths["family_noise"], self.run_family_packet(noise_refs))
            write_json(
                paths["status_noise"],
                self.preserved_run_status_packet(noise_refs),
            )
            write_json(paths["governing_noise"], self.current_governing_packet(noise_refs))
            write_json(
                paths["query_noise"],
                self.query_result(
                    effective_refs,
                    query_id="current_state_query_other",
                    answer_read_id="current_state_answer_read_other",
                ),
            )
            write_json(
                paths["open_noise"],
                self.what_remains_open_result(
                    open_id="what_remains_open_other",
                    answer_read_id="current_state_answer_read_other",
                    effective_refs=effective_refs,
                    outcome=open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                    block_code=None,
                ),
            )
            write_json(
                paths["vessel_noise"],
                self.vessel_result(
                    temp_root,
                    paths["stand"],
                    effective_refs,
                    vessel_id="bounded_current_state_vessel_other",
                    stand_id="what_stands_now_other",
                    outcome=vessel_resolver.OUTCOME_ANSWERED_DERIVATIVE_READ,
                ),
            )
            write_json(
                paths["brief_noise"],
                self.operator_brief_result(
                    temp_root,
                    brief_id="operator_terminal_brief_other",
                    vessel_path=paths["vessel_noise"],
                    vessel_id="bounded_current_state_vessel_other",
                    stand_id="what_stands_now_other",
                    outcome=brief_resolver.OUTCOME_BRIEF_RENDERED,
                ),
            )
            write_json(
                paths["body_pass_noise"],
                self.body_pass_result(
                    temp_root,
                    paths["seam"],
                    paths["action"],
                    paths["participation"],
                    paths["receipt"],
                    paths["transfer"],
                    paths["touch"],
                    paths["stand"],
                    effective_refs,
                    body_pass_id="v0_body_pass_result_blocked_noise",
                    seam_id=ids["seam"],
                    action_id=ids["action"],
                    participation_id=ids["participation"],
                    receipt_id=ids["receipt"],
                    transfer_id=ids["transfer"],
                    touch_id=ids["touch"],
                    stand_id=ids["stand"],
                    outcome=body_pass_resolver.OUTCOME_BLOCKED,
                ),
            )

        return {
            "paths": paths,
            "ids": ids,
            "effective_references": effective_refs,
        }

    @contextlib.contextmanager
    def patched_repo_root(self, temp_root: Path) -> Iterator[None]:
        with mock.patch.object(orientation_v2, "_repo_root", return_value=temp_root):
            yield

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertTrue(
            set(orientation_v2.NON_CLAIM_DEFAULTS).issubset(set(non_claims))
        )
        for key, value in non_claims.items():
            self.assertIs(value, False, key)
        for key in REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, non_claims)
            self.assertIs(non_claims[key], False, key)

    def assert_success(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(orientation_v2.OUTCOME_SELF_ORIENTED, result["outcome"])
        self.assertEqual({"block_code": None, "block_reason": None}, result["block"])
        self.assertEqual(
            EXPECTED_SELECTED_INPUT_KEYS,
            set(result["selected_orientation_inputs"]),
        )

        metadata = result["current_self_orientation_v2_metadata"]
        self.assertEqual(
            {
                "self_orientation_result_id",
                "self_orientation_result_type",
                "self_orientation_result_version",
                "generated_at",
                "resolver_module",
                "successor_of_module",
            },
            set(metadata),
        )
        for key, value in metadata.items():
            self.assertIsInstance(value, str)
            self.assertTrue(value, key)
        self.assertEqual(
            orientation_v2.CURRENT_SELF_ORIENTATION_RESULT_TYPE,
            metadata["self_orientation_result_type"],
        )
        self.assertEqual(
            orientation_v2.CURRENT_SELF_ORIENTATION_RESULT_VERSION,
            metadata["self_orientation_result_version"],
        )
        self.assertEqual(orientation_v2.RESOLVER_MODULE, metadata["resolver_module"])
        self.assertEqual(
            orientation_v2.SUCCESSOR_OF_MODULE,
            metadata["successor_of_module"],
        )

        self.assertIsInstance(result["current_self_orientation_summary"], dict)
        self.assertIsInstance(result["recognized_current_executable_core_line"], dict)
        self.assertIsInstance(result["recognized_governing_effective_basis"], dict)
        self.assertIsInstance(result["recognized_current_state_surfaces"], dict)
        self.assertIsInstance(result["recognized_continuity_surfaces"], dict)
        self.assertIsInstance(result["recognized_derivative_surfaces"], dict)
        self.assertIsInstance(result["recognized_operator_facing_surfaces"], dict)
        self.assertIsInstance(result["recognized_open_surfaces"], dict)
        self.assertIsInstance(result["recognized_blocked_or_refused_surfaces"], list)
        self.assertIsInstance(result["recognized_touch_admissibility_surfaces"], dict)
        self.assertIsInstance(result["bounded_correspondence_checks"], list)
        self.assertIsInstance(result["self_orientation_basis"], dict)
        self.assert_non_claims_false(result)

    def assert_blocked(self, result: Mapping[str, Any], block_code: str) -> None:
        self.assertEqual(EXPECTED_RESULT_KEYS, set(result))
        self.assertEqual(orientation_v2.OUTCOME_BLOCKED, result["outcome"])
        self.assertEqual(block_code, result["block"]["block_code"])
        self.assertIsInstance(result["block"]["block_reason"], str)
        self.assertTrue(result["block"]["block_reason"])
        self.assertEqual(
            EXPECTED_SELECTED_INPUT_KEYS,
            set(result["selected_orientation_inputs"]),
        )
        self.assertIsInstance(result["current_self_orientation_summary"], dict)
        self.assertEqual(
            block_code,
            result["current_self_orientation_summary"]["block_code"],
        )
        self.assert_non_claims_false(result)

    def test_live_repo_default_resolution_accepts_live_received_payload_shape(self) -> None:
        result = self.live_result()
        self.assert_success(result)

        selected = result["selected_orientation_inputs"]
        receipt_rel = selected["selected_receipt_result"]["result_path"]
        body_pass_rel = selected["selected_body_pass_result"]["result_path"]
        self.assertIsInstance(receipt_rel, str)
        self.assertTrue(receipt_rel)
        self.assertIsInstance(body_pass_rel, str)
        self.assertTrue(body_pass_rel)

        receipt_path = REPO_ROOT / receipt_rel
        body_pass_path = REPO_ROOT / body_pass_rel
        self.assertTrue(receipt_path.is_file())
        self.assertTrue(body_pass_path.is_file())

        receipt = read_json(receipt_path)
        self.assertIn("received_payload", receipt)
        self.assertIsInstance(receipt["received_payload"], dict)
        self.assertEqual(
            "received_carried_derivative",
            receipt["received_payload"]["payload_receipt_status"],
        )
        self.assertIsNone(receipt.get("receipt_payload"))
        self.assertEqual(
            selected["selected_receipt_result"]["result_id"],
            result["recognized_continuity_surfaces"][
                "continuity_transfer_receipt_result"
            ]["result_id"],
        )

        path_result = orientation_v2.resolve_current_self_orientation_from_path(
            body_pass_path
        )
        self.assert_success(path_result)
        for key in PATH_EQUIVALENCE_KEYS:
            self.assertEqual(result[key], path_result[key], key)
        self.assertEqual(
            [
                (check["check_name"], check["passed"], check.get("block_code"))
                for check in result["bounded_correspondence_checks"]
            ],
            [
                (check["check_name"], check["passed"], check.get("block_code"))
                for check in path_result["bounded_correspondence_checks"]
            ],
        )
        self.assertEqual(
            "successful_body_pass_discovery",
            result["self_orientation_basis"]["orientation_selection_mode"],
        )
        self.assertEqual(
            "explicit_body_pass_result_path",
            path_result["self_orientation_basis"]["orientation_selection_mode"],
        )

    def test_synthetic_success_path_preserves_sections_basis_and_checks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation()

            self.assert_success(result)
            selected = result["selected_orientation_inputs"]
            ids = stack["ids"]
            effective_refs = stack["effective_references"]

            self.assertEqual(ids["body_pass"], selected["selected_body_pass_result"]["result_id"])
            self.assertEqual(ids["seam"], selected["selected_seam_result"]["result_id"])
            self.assertEqual(ids["action"], selected["selected_action_permission_result"]["result_id"])
            self.assertEqual(ids["participation"], selected["selected_participation_result"]["result_id"])
            self.assertEqual(ids["receipt"], selected["selected_receipt_result"]["result_id"])
            self.assertEqual(ids["transfer"], selected["selected_transfer_result"]["result_id"])
            self.assertEqual(ids["touch"], selected["selected_touch_permission_result"]["result_id"])
            self.assertEqual(ids["stand"], selected["selected_source_surface"]["result_id"])
            self.assertEqual(
                ids["stand"],
                selected["selected_current_state_what_stands_now_result"]["result_id"],
            )
            self.assertEqual(
                ids["answer"],
                selected["selected_current_state_answer_read_result"]["result_id"],
            )
            self.assertEqual(effective_refs, selected["selected_effective_references"])
            self.assertEqual(1, len(selected["selected_current_state_query_results"]))
            self.assertEqual(
                ids["query"],
                selected["selected_current_state_query_results"][0]["result_id"],
            )
            self.assertEqual(
                {ids["open"], ids["open_blocked"]},
                {
                    item["result_id"]
                    for item in selected["selected_current_state_what_remains_open_results"]
                },
            )
            self.assertEqual(
                {ids["vessel_answered"], ids["vessel_refused"]},
                {item["result_id"] for item in selected["selected_vessel_results"]},
            )
            self.assertEqual(
                {ids["brief_rendered"], ids["brief_refused"]},
                {
                    item["result_id"]
                    for item in selected["selected_operator_terminal_brief_results"]
                },
            )

            governing = result["recognized_governing_effective_basis"]
            self.assertIs(governing["recognized_from_explicit_effective_references"], True)
            self.assertEqual(effective_refs, governing["effective_references"])
            self.assertEqual(
                effective_refs["effective_authority_artifact_path"],
                governing["current_execution_authority_artifact_path"],
            )
            self.assertEqual(
                effective_refs["effective_current_governing_packet_path"],
                governing["current_governing_packet_path"],
            )
            self.assertNotIn("openai_api_derivative_vessel_v3_results", governing)
            self.assertNotIn("operator_terminal_brief_results", governing)

            current_line = result["recognized_current_executable_core_line"]
            self.assertEqual(
                self.canonical_core_execution_file(),
                current_line["canonical_core_execution_file"],
            )
            self.assertEqual(ids["body_pass"], current_line["selected_body_pass_result_id"])
            self.assertEqual(ids["stand"], current_line["selected_source_surface_id"])

            derivative = result["recognized_derivative_surfaces"]
            self.assertEqual(
                ids["participation"],
                derivative["received_derivative_participation_result"]["result_id"],
            )
            self.assertEqual(
                ids["action"],
                derivative["received_derivative_action_permission_result"]["result_id"],
            )
            self.assertEqual(
                {ids["vessel_answered"], ids["vessel_refused"]},
                {
                    item["result_id"]
                    for item in derivative["openai_api_derivative_vessel_v3_results"]
                },
            )
            operator_surfaces = result["recognized_operator_facing_surfaces"]
            self.assertEqual(
                {ids["brief_rendered"], ids["brief_refused"]},
                {
                    item["result_id"]
                    for item in operator_surfaces["operator_terminal_brief_results"]
                },
            )

            open_surfaces = result["recognized_open_surfaces"]["what_remains_open_results"]
            self.assertEqual(
                {
                    open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                    open_resolver.OUTCOME_BLOCKED,
                },
                {item["outcome"] for item in open_surfaces},
            )

            blocked = result["recognized_blocked_or_refused_surfaces"]
            self.assertEqual(
                {ids["open_blocked"], ids["vessel_refused"], ids["brief_refused"]},
                {item["surface_id"] for item in blocked},
            )

            checks = result["bounded_correspondence_checks"]
            self.assertEqual(
                EXPECTED_SUCCESS_CHECK_NAMES,
                {check["check_name"] for check in checks},
            )
            self.assertTrue(all(check["passed"] is True for check in checks))

    def test_summary_helper_returns_bounded_summary(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )
                summary = orientation_v2.build_current_self_orientation_summary(result)

            self.assertEqual(orientation_v2.OUTCOME_SELF_ORIENTED, summary["outcome"])
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(stack["ids"]["body_pass"], summary["selected_body_pass_result_id"])
            self.assertEqual(stack["ids"]["stand"], summary["selected_source_surface_id"])
            self.assertEqual(stack["ids"]["answer"], summary["selected_current_state_answer_read_id"])
            self.assertTrue(summary["current_executable_core_line_recognized"])
            self.assertTrue(summary["governing_effective_basis_recognized"])
            self.assertTrue(summary["continuity_surfaces_recognized"])
            self.assertTrue(summary["derivative_surfaces_recognized"])
            self.assertTrue(summary["operator_surfaces_recognized"])
            self.assertTrue(summary["correspondence_checks_passed"])
            self.assertEqual(set(orientation_v2.NON_CLAIM_DEFAULTS), set(summary["non_claims"]))

    def test_receipt_backward_compatibility_read_accepts_receipt_payload_only(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(
                temp_root,
                receipt_payload_mode="receipt_payload",
            )
            receipt = read_json(stack["paths"]["receipt"])
            self.assertIn("receipt_payload", receipt)
            self.assertNotIn("received_payload", receipt)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_success(result)
            self.assertEqual(
                stack["ids"]["receipt"],
                result["recognized_continuity_surfaces"][
                    "continuity_transfer_receipt_result"
                ]["result_id"],
            )

    def test_preserves_selected_basis_on_downstream_block(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)

            vessel = read_json(stack["paths"]["vessel_answered"])
            vessel["selected_source_surface"]["selected_source_surface_id"] = "other_stand_now"
            write_json(stack["paths"]["vessel_answered"], vessel)
            refused = read_json(stack["paths"]["vessel_refused"])
            refused["selected_source_surface"]["selected_source_surface_id"] = "other_stand_now"
            write_json(stack["paths"]["vessel_refused"], refused)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING")
            selected = result["selected_orientation_inputs"]
            ids = stack["ids"]
            self.assertEqual(ids["body_pass"], selected["selected_body_pass_result"]["result_id"])
            self.assertEqual(ids["seam"], selected["selected_seam_result"]["result_id"])
            self.assertEqual(ids["action"], selected["selected_action_permission_result"]["result_id"])
            self.assertEqual(ids["participation"], selected["selected_participation_result"]["result_id"])
            self.assertEqual(ids["receipt"], selected["selected_receipt_result"]["result_id"])
            self.assertEqual(ids["transfer"], selected["selected_transfer_result"]["result_id"])
            self.assertEqual(ids["touch"], selected["selected_touch_permission_result"]["result_id"])
            self.assertEqual(ids["stand"], selected["selected_source_surface"]["result_id"])
            self.assertEqual(
                ids["answer"],
                selected["selected_current_state_answer_read_result"]["result_id"],
            )
            self.assertEqual(
                stack["effective_references"],
                selected["selected_effective_references"],
            )
            summary = result["current_self_orientation_summary"]
            self.assertEqual(ids["body_pass"], summary["selected_body_pass_result_id"])
            self.assertEqual(ids["stand"], summary["selected_source_surface_id"])
            self.assertEqual("DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING", summary["block_code"])

    def test_non_mutating_and_additive_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            before_tree = tree_digest(temp_root)
            before_body_pass_digest = file_digest(stack["paths"]["body_pass"])
            body_pass_mapping = read_json(stack["paths"]["body_pass"])
            body_pass_before = copy.deepcopy(body_pass_mapping)

            with self.patched_repo_root(temp_root):
                first = orientation_v2.resolve_current_self_orientation()
                second = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )
                third = orientation_v2.resolve_current_self_orientation(body_pass_mapping)

            self.assert_success(first)
            self.assert_success(second)
            self.assert_success(third)
            self.assertEqual(body_pass_before, body_pass_mapping)
            self.assertEqual(before_tree, tree_digest(temp_root))
            self.assertEqual(before_body_pass_digest, file_digest(stack["paths"]["body_pass"]))
            self.assertFalse((temp_root / orientation_v2.CURRENT_SELF_ORIENTATION_V2_ROOT).exists())

    def test_write_helper_and_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

                explicit_path = (
                    temp_root / "written" / "nested" / "current_self_orientation_v2.json"
                )
                written = orientation_v2.write_current_self_orientation_result(
                    result,
                    explicit_path,
                )
                self.assertEqual(explicit_path, written)
                self.assertTrue(written.is_file())
                self.assertEqual(EXPECTED_RESULT_KEYS, set(read_json(written)))
                with self.assertRaises(FileExistsError):
                    orientation_v2.write_current_self_orientation_result(result, explicit_path)

                first_default = orientation_v2.write_current_self_orientation_result(result)
                second_default = orientation_v2.write_current_self_orientation_result(result)

            self.assertEqual(
                temp_root / orientation_v2.CURRENT_SELF_ORIENTATION_V2_ROOT,
                first_default.parent,
            )
            self.assertTrue(
                first_default.name.endswith("__current_self_orientation_v2_result.json")
            )
            self.assertIn("_001", second_default.stem)
            self.assertNotEqual(first_default, second_default)

    def test_declares_full_block_family_and_proportion_checks(self) -> None:
        self.assertTrue(DECLARED_BLOCK_CODES.issubset(set(orientation_v2.BLOCK_REASONS)))

        result = self.live_result()
        self.assert_success(result)
        checks = {
            check["check_name"]: check
            for check in result["bounded_correspondence_checks"]
        }
        self.assertEqual(EXPECTED_SUCCESS_CHECK_NAMES, set(checks))
        self.assertIs(
            checks["governing_effective_basis_is_explicit_not_latest_file_guessing"][
                "passed"
            ],
            True,
        )
        self.assertIs(
            checks["open_surfaces_are_not_converted_to_completed"]["passed"],
            True,
        )
        self.assertIs(
            checks["non_claims_remain_false_and_carried_forward"]["passed"],
            True,
        )
        self.assertIs(
            checks["self_orientation_does_not_over_mirror_into_whole_body_replacement"][
                "passed"
            ],
            True,
        )
        self.assertIs(
            checks["self_orientation_does_not_under_mirror_required_standing_posture"][
                "passed"
            ],
            True,
        )

    def test_blocks_when_no_self_orientation_source_basis_exists(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation()
                summary = orientation_v2.build_current_self_orientation_summary(result)

            self.assert_blocked(result, "NO_SELF_ORIENTATION_SOURCE_BASIS")
            self.assertEqual(orientation_v2.OUTCOME_BLOCKED, summary["outcome"])
            self.assertEqual("NO_SELF_ORIENTATION_SOURCE_BASIS", summary["block_code"])

    def test_blocks_when_required_source_artifact_is_unreadable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            stack["paths"]["receipt"].unlink()

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "REQUIRED_SOURCE_ARTIFACT_UNREADABLE")

    def test_blocks_when_selected_source_artifact_is_malformed_json(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            stack["paths"]["receipt"].write_text("{", encoding="utf-8")

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "SOURCE_ARTIFACT_MALFORMED")

    def test_blocks_when_receipt_payload_shape_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            receipt = read_json(stack["paths"]["receipt"])
            receipt.pop("received_payload", None)
            receipt.pop("receipt_payload", None)
            write_json(stack["paths"]["receipt"], receipt)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "SOURCE_ARTIFACT_MALFORMED")
            self.assertIn(
                "received_payload or receipt_payload",
                result["block"]["block_reason"],
            )

    def test_blocks_when_current_effective_basis_is_absent_or_ambiguous(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            body_pass = read_json(stack["paths"]["body_pass"])
            body_pass["selected_source_surface"]["selected_source_surface_effective_references"] = []
            write_json(stack["paths"]["body_pass"], body_pass)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "CURRENT_EFFECTIVE_BASIS_ABSENT_OR_AMBIGUOUS")

    def test_blocks_when_required_current_state_surface_is_absent(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            stack["paths"]["query"].unlink()

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "CURRENT_STATE_SURFACE_ABSENT_WHERE_REQUIRED")

    def test_blocks_when_derivative_surface_source_basis_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            vessel = read_json(stack["paths"]["vessel_answered"])
            vessel["selected_source_surface"]["selected_source_surface_id"] = "other_stand_now"
            write_json(stack["paths"]["vessel_answered"], vessel)
            refused = read_json(stack["paths"]["vessel_refused"])
            refused["selected_source_surface"]["selected_source_surface_id"] = "other_stand_now"
            write_json(stack["paths"]["vessel_refused"], refused)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "DERIVATIVE_SURFACE_SOURCE_BASIS_MISSING")

    def test_blocks_when_operator_surface_derivative_or_source_basis_is_missing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            brief = read_json(stack["paths"]["brief_rendered"])
            brief["selected_vessel_result"]["selected_vessel_result_id"] = "other_vessel_result"
            write_json(stack["paths"]["brief_rendered"], brief)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(
                result,
                "OPERATOR_SURFACE_DERIVATIVE_OR_SOURCE_BASIS_MISSING",
            )

    def test_latest_file_recency_noise_does_not_override_selected_confirmed_body_pass(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root, include_noise=True)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation()

            self.assert_success(result)
            self.assertEqual(
                stack["ids"]["body_pass"],
                result["selected_orientation_inputs"]["selected_body_pass_result"][
                    "result_id"
                ],
            )
            self.assertNotEqual(
                "v0_body_pass_result_blocked_noise",
                result["selected_orientation_inputs"]["selected_body_pass_result"][
                    "result_id"
                ],
            )
            checks = {
                check["check_name"]: check
                for check in result["bounded_correspondence_checks"]
            }
            self.assertIs(
                checks[
                    "current_self_orientation_uses_explicit_anchor_or_successful_filtered_discovery"
                ]["passed"],
                True,
            )

    def test_blocks_when_derivative_surface_is_treated_as_authority(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            transfer = read_json(stack["paths"]["transfer"])
            transfer["transfer_payload"]["source_remains_source"] = False
            write_json(stack["paths"]["transfer"], transfer)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "DERIVATIVE_TREATED_AS_SOURCE_AUTHORITY")

    def test_blocks_when_operator_surface_is_treated_as_authority(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            brief = read_json(stack["paths"]["brief_rendered"])
            brief["brief_output"]["source_remains_source"] = False
            write_json(stack["paths"]["brief_rendered"], brief)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "OPERATOR_SURFACE_TREATED_AS_SOURCE_AUTHORITY")

    def test_blocks_when_open_surface_is_treated_as_completed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            open_result = read_json(stack["paths"]["open"])
            open_result["outcome"] = "COMPLETED"
            write_json(stack["paths"]["open"], open_result)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "OPEN_SURFACE_TREATED_AS_COMPLETED")

    def test_blocked_or_refused_surfaces_remain_visible_when_present(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root, include_blocked_visibility=True)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_success(result)
            blocked = result["recognized_blocked_or_refused_surfaces"]
            self.assertEqual(
                {stack["ids"]["open_blocked"], stack["ids"]["vessel_refused"], stack["ids"]["brief_refused"]},
                {item["surface_id"] for item in blocked},
            )
            checks = {
                check["check_name"]: check
                for check in result["bounded_correspondence_checks"]
            }
            self.assertIs(
                checks["blocked_or_refused_surfaces_remain_visible_when_present"][
                    "passed"
                ],
                True,
            )

    def test_blocks_when_non_claim_is_missing_or_flipped(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            body_pass = read_json(stack["paths"]["body_pass"])
            body_pass["non_claims"]["recency_fraud"] = True
            write_json(stack["paths"]["body_pass"], body_pass)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "NON_CLAIM_MISSING_OR_FLIPPED")

    def test_blocks_when_correspondence_check_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            answer = read_json(stack["paths"]["answer"])
            answer["answer_read_output"][
                "effective_authority_artifact_path"
            ] = self.relative_path(temp_root, stack["paths"]["authority_noise"])
            write_json(stack["paths"]["answer"], answer)

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation_from_path(
                    stack["paths"]["body_pass"]
                )

            self.assert_blocked(result, "CORRESPONDENCE_CHECK_FAILED")

    def test_blocks_when_external_reader_orientation_is_attempted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            body_pass = read_json(stack["paths"]["body_pass"])
            body_pass["repo_map"] = {"attempt": "external-reader orientation"}

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation(body_pass)

            self.assert_blocked(result, "EXTERNAL_READER_ORIENTATION_ATTEMPTED")

    def test_blocks_when_hand_maintained_summary_seam_is_attempted(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_valid_stack(temp_root)
            body_pass = read_json(stack["paths"]["body_pass"])
            body_pass["summary_seam"] = {"attempt": "manual summary seam"}

            with self.patched_repo_root(temp_root):
                result = orientation_v2.resolve_current_self_orientation(body_pass)

            self.assert_blocked(result, "HAND_MAINTAINED_SUMMARY_SEAM_ATTEMPTED")


if __name__ == "__main__":
    unittest.main()
