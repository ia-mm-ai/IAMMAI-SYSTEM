"""Bounded tests for the v0-min whole-body composite verification pass.

This suite exercises ``run_integrity_host_v0_min_coexistence_v0_body_pass``.
It builds real local upstream artifacts through continuity-memory seam closure,
then verifies that the body pass remains an additive composite verifier over
the already-standing organs. It does not test replay, merge, registry,
persistence, mutable memory, final governance, or continuity-completion
behavior.
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


import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_builder
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer
import resolve_current_integrity_host_v0_min_coexistence_effective_family as effective_resolver
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as authority_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_memory_seam as seam_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt as receipt_resolver
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_application as application_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_delivery as delivery_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_export as export_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_handoff as handoff_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_readout as readout_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver
import resolve_integrity_host_v0_min_coexistence_current_work_input as work_input_resolver
import resolve_integrity_host_v0_min_coexistence_current_work_operation_v2 as operation_resolver
import resolve_integrity_host_v0_min_coexistence_effective_family_consumption as consumption_resolver
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission as action_resolver
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner
import run_integrity_host_v0_min_coexistence_v0_body_pass as body_pass


REQUIRED_CONTEXT_PATHS = (
    "reference/IAMMAI/CURRENT_STATE__REPO_ENTRY.md",
    "reference/IAMMAI/RANKED_SURFACE_INDEX.md",
    "reference/IAMMAI/protocol/IAMMAI_Constitutional_Integrity_Protocol_v1.0.1.md",
    "reference/IAMMAI/implementation/INTEGRITY_KERNEL_SPEC.md",
    "reference/IAMMAI/implementation/STATE_MACHINE_OVERVIEW.md",
    "reference/IAMMAI/implementation/CANONICAL_RECORDS_OVERVIEW.md",
    "reference/IAMMAI/implementation/TRANSITION_RECORD_OVERVIEW.md",
    "reference/IAMMAI/runtime/MINIMAL_LAWFUL_EMBODIMENT.md",
    "reference/IAMMAI/runtime/VALIDATOR_CONTRACT.md",
    "reference/IAMMAI/architecture/RUNTIME_COMPONENTS.md",
    "spec/INTEGRITY_HOST_V0_MIN_SPEC.md",
    "spec/INTEGRITY_HOST_V0_MIN_WORLD_ASSUMPTIONS.md",
    "spec/INTEGRITY_RELATION_V0_MIN_BOUNDARY.md",
    "spec/INTEGRITY_RELATION_V0_MIN_SPEC.md",
    "spec/CURRENT_EXECUTABLE_LINE_AND_FORCED_SYSTEM_PRESSURES.md",
    "spec/GOVERNING_TRANSITION_V0_MIN_SPEC.md",
    "spec/GOVERNING_RERESOLUTION_V0_MIN_SPEC.md",
    "spec/GOVERNING_SUCCESSOR_ADOPTION_V0_MIN_SPEC.md",
    "spec/EFFECTIVE_FAMILY_CONSUMPTION_V0_MIN_SPEC.md",
    "spec/CURRENT_WORK_OPERATION_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_READOUT_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_HANDOFF_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_EXPORT_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_DELIVERY_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_APPLICATION_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_ANSWER_SURFACE_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_QUERY_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_WHAT_STANDS_NOW_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_WHAT_REMAINS_OPEN_V0_MIN_SPEC.md",
    "spec/CURRENT_STATE_ADMISSIBILITY_AND_TOUCH_PERMISSION_V0_MIN_SPEC.md",
    "spec/CONTINUITY_TRANSFER_UNIT_V0_MIN_SPEC.md",
    "spec/CONTINUITY_TRANSFER_RECEIPT_V0_MIN_SPEC.md",
    "spec/RECEIVED_DERIVATIVE_PARTICIPATION_V0_MIN_SPEC.md",
    "spec/RECEIVED_DERIVATIVE_ACTION_PERMISSION_V0_MIN_SPEC.md",
    "spec/CONTINUITY_MEMORY_SEAM_V0_CLOSURE_SPEC.md",
    "src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py",
    "src/build_integrity_host_v0_min_coexistence_run_family_packet.py",
    "src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py",
    "src/build_current_integrity_host_v0_min_coexistence_governing_packet.py",
    "src/resolve_integrity_host_v0_min_coexistence_governing_transition.py",
    "src/resolve_integrity_host_v0_min_coexistence_governing_reresolution.py",
    "src/resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py",
    "src/resolve_current_integrity_host_v0_min_coexistence_effective_family.py",
    "src/resolve_integrity_host_v0_min_coexistence_effective_family_consumption.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_work_input.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_work_operation_v2.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_readout.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_handoff.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_export.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_delivery.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_application.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_answer_surface.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_query.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open.py",
    "src/resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission.py",
    "src/resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit.py",
    "src/resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt.py",
    "src/resolve_integrity_host_v0_min_coexistence_received_derivative_participation.py",
    "src/resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission.py",
    "src/resolve_integrity_host_v0_min_coexistence_continuity_memory_seam.py",
    "src/run_integrity_host_v0_min_coexistence_v0_body_pass.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_governing_transition.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_governing_reresolution.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2.py",
    "tests/test_resolve_current_integrity_host_v0_min_coexistence_effective_family.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_effective_family_consumption.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_work_input.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_work_operation_v2.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_readout.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_handoff.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_export.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_delivery.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_application.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_answer_surface.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_query.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_received_derivative_participation.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_received_derivative_action_permission.py",
    "tests/test_resolve_integrity_host_v0_min_coexistence_continuity_memory_seam.py",
)

TOP_LEVEL = {
    "v0_body_pass_metadata",
    "selected_seam_result",
    "selected_action_permission_result",
    "selected_participation_result",
    "selected_receipt_result",
    "selected_transfer_result",
    "selected_touch_permission_result",
    "selected_source_surface",
    "body_pass_posture",
    "checks",
    "outcome",
    "block",
    "v0_body_pass_summary",
    "non_claims",
}

QUERY_FIELDS = [
    "current_governing_source_run_path",
    "current_governing_ingress_run_path",
    "current_authority_artifact_path",
    "current_family_packet_path",
    "current_status_packet_path",
    "current_governing_packet_path",
    "preserved_run_count",
    "current_authority_run_count",
    "preserved_eligible_non_authority_count",
    "preserved_ineligible_count",
    "application_basis",
    "answer_read_basis",
    "non_claims",
]
STAND_FIELDS = [
    "current_governing_source_run_path",
    "current_governing_ingress_run_path",
    "current_authority_artifact_path",
    "current_family_packet_path",
    "current_status_packet_path",
    "current_governing_packet_path",
    "preserved_run_count",
    "application_basis",
    "answer_read_basis",
    "non_claims",
]
OPEN_FIELDS = [
    "non_claims",
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
    "minimum_lawful_system_completed",
    "final_system_identity_completed",
    "final_preserved_run_governance_completed",
    "final_governing_scope_completed",
    "final_governing_transition_law_completed",
    "final_governing_reresolution_completed",
    "final_governing_successor_adoption_completed",
    "final_effective_family_resolution_completed",
    "final_effective_family_consumption_completed",
    "final_current_work_input_resolution_completed",
    "final_current_work_operation_completed",
    "final_current_state_readout_completed",
    "final_current_state_handoff_completed",
    "final_current_state_export_completed",
    "final_current_state_delivery_completed",
    "final_current_state_application_completed",
    "final_current_state_answer_read_completed",
    "final_current_state_query_completed",
    "authority_resolution_is_protocol_law",
    "final_persistence_or_registry_law",
    "current_work_basis",
    "readout_basis",
    "handoff_basis",
    "export_basis",
    "delivery_basis",
    "application_basis",
    "answer_read_basis",
]
DERIVATIVE_FIELDS = [
    "non_claims",
    "continuity_completed",
    "standing_upgraded",
    "answer_read_basis",
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
    target.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
    return target


def copied(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def resolve_path(path: str | Path, temp_root: Path) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return temp_root / candidate


def reresolution_path(result: Mapping[str, Any], temp_root: Path) -> Path:
    references = result.get("input_references")
    if not isinstance(references, Mapping):
        raise AssertionError("re-resolution did not expose input references")
    run_dir_text = references.get("reresolution_run_directory_path")
    if not isinstance(run_dir_text, str) or not run_dir_text:
        raise AssertionError("re-resolution did not expose run directory")
    candidates = sorted(resolve_path(run_dir_text, temp_root).glob("*_result.json"))
    if len(candidates) != 1:
        raise AssertionError("re-resolution did not expose one result artifact")
    return candidates[0]


def tree_digest(root: Path) -> dict[str, str]:
    digests: dict[str, str] = {}
    if not root.exists():
        return digests
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        digests[str(path.relative_to(root))] = hashlib.sha256(path.read_bytes()).hexdigest()
    return digests


class V0BodyPassTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        for relative_path in REQUIRED_CONTEXT_PATHS:
            path = REPO_ROOT / relative_path
            if not path.is_file():
                raise AssertionError(f"required context file is missing: {relative_path}")
            path.read_text(encoding="utf-8")

    def emit_source(self, temp_root: Path, name: str) -> Path:
        run_dir = temp_root / authority_resolver.SOURCE_RUNS_ROOT / name
        run_dir.mkdir(parents=True, exist_ok=True)
        with mock.patch.object(scenario_runner, "_repo_root", return_value=temp_root):
            emitted = tuple(
                scenario_runner._emit_scenario(run_dir, stem, scenario_function)
                for stem, scenario_function in scenario_runner.SCENARIOS
            )
            manifest = scenario_runner._build_manifest(run_dir, emitted)
            (run_dir / "manifest.json").write_text(
                scenario_runner.snapshot_to_json(manifest),
                encoding="utf-8",
            )
        return run_dir

    def emit_ingress(self, temp_root: Path, source_run: Path) -> Path:
        with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
            manifest = ingress_runner.run_receiving_ingress_for_source_run(source_run)
            output_dir = resolve_path(
                manifest["ingress_run_metadata"]["output_run_directory"],
                temp_root,
            )
            ingress_runner.write_ingress_run_manifest(
                manifest,
                output_dir / "manifest.json",
            )
        return output_dir

    def emit_comparison(
        self,
        temp_root: Path,
        source_run: Path,
        ingress_run: Path,
    ) -> Path:
        with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
            comparison = comparer.compare_source_run_and_ingress_run(
                source_run,
                ingress_run,
            )
            path = (
                temp_root
                / authority_resolver.SOURCE_INGRESS_COMPARISON_ROOT
                / f"{source_run.name}__source_ingress_comparison.json"
            )
            comparer.write_comparison(comparison, path)
        return path

    def valid_proposal(
        self,
        current: Mapping[str, Any],
        candidate: Mapping[str, Any],
    ) -> dict[str, str]:
        return {
            "transition_proposal_id": "proposal_accepted_for_body_pass",
            "current_governing_source_run_path": str(current["source_run_directory_path"]),
            "candidate_successor_source_run_path": str(
                candidate["source_run_directory_path"]
            ),
            "current_governing_ingress_run_path": str(current["matched_ingress_run_path"]),
            "candidate_successor_ingress_run_path": str(
                candidate["matched_ingress_run_path"]
            ),
            "current_governing_comparison_artifact_path": str(
                current["matched_comparison_artifact_path"]
            ),
            "candidate_successor_comparison_artifact_path": str(
                candidate["matched_comparison_artifact_path"]
            ),
            "proposal_basis_ref": "bounded explicit body-pass test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_run_integrity_host_v0_min_coexistence_v0_body_pass.py"
            ),
        }

    def query_request(self) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_body_pass",
            "query_target": "answer_read_output",
            "requested_fields": list(QUERY_FIELDS),
            "query_basis": "bounded body-pass query over emitted answer surface",
        }

    def stand_request(self) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "unit_test_body_pass_what_stands_now",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(STAND_FIELDS),
            "query_basis": "bounded body-pass stand query",
        }

    def open_request(self) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "unit_test_body_pass_what_remains_open",
            "query_family": "what_remains_open",
            "requested_open_fields": list(OPEN_FIELDS),
            "query_basis": "bounded body-pass open-surface question",
        }

    def touch_request(
        self,
        touch_class: str,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded body-pass touch basis",
    ) -> dict[str, Any]:
        return {
            "touch_request_id": f"unit_test_body_pass_touch_{touch_class.lower()}",
            "requested_touch_class": touch_class,
            "requested_touch_basis": basis,
            "requesting_surface_label": "unit_test_body_pass_touch_surface",
            "intended_downstream_use": "bounded body-pass test",
            "requested_touch_fields": list(fields if fields is not None else []),
        }

    def transfer_request(
        self,
        transfer_class: str = transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded body-pass transfer basis",
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_request_id": f"unit_test_body_pass_transfer_{transfer_class.lower()}",
            "transfer_class": transfer_class,
            "transfer_basis": basis,
            "requested_transfer_fields": list(fields if fields is not None else []),
            "target_seam_label": "unit_test_body_pass_seam",
        }

    def receipt_request(
        self,
        receipt_class: str = receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded body-pass receipt",
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_receipt_request_id": (
                f"unit_test_body_pass_receipt_{receipt_class.lower()}"
            ),
            "receipt_class": receipt_class,
            "receipt_basis": basis,
            "requested_receipt_fields": list(fields if fields is not None else []),
            "receiving_boundary_label": "unit_test_body_pass_receiving_boundary",
        }

    def participation_request(self) -> dict[str, Any]:
        return {
            "received_derivative_participation_request_id": (
                "unit_test_body_pass_participation"
            ),
            "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_DERIVATION,
            "use_class": participation_resolver.USE_CLASS_DERIVATIVE,
            "participation_basis": "bounded derivative participation for body pass",
            "requested_participation_fields": list(DERIVATIVE_FIELDS),
            "participating_surface_label": "unit_test_body_pass_participating_surface",
        }

    def action_request(
        self,
        *,
        basis: str = "bounded derivative emission action permission for body pass",
    ) -> dict[str, Any]:
        return {
            "received_derivative_action_permission_request_id": (
                "unit_test_body_pass_action_permission"
            ),
            "actor_class": action_resolver.ACTOR_CLASS_LOCAL_EMISSION,
            "action_class": action_resolver.ACTION_CLASS_DERIVATIVE_EMISSION,
            "action_basis": basis,
            "requested_action_fields": list(DERIVATIVE_FIELDS),
            "action_surface_label": "unit_test_body_pass_action_surface",
        }

    def build_current_state_stack(self, temp_root: Path) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260422T040000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260422T040001_000000Z")
        ingress_two = self.emit_ingress(temp_root, source_two)
        comparison_two = self.emit_comparison(temp_root, source_two, ingress_two)

        with mock.patch.object(authority_resolver, "_repo_root", return_value=temp_root):
            authority = authority_resolver.resolve_current_execution_authority()
            authority_path = authority_resolver.write_resolution(authority)
        with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
            family = family_builder.build_run_family_packet()
            family_path = family_builder.write_run_family_packet(family)
        with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
            status = status_builder.build_preserved_run_status_packet()
            status_path = status_builder.write_preserved_run_status_packet(status)
        with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
            governing = governing_builder.build_current_governing_packet()
            governing_path = governing_builder.write_current_governing_packet(governing)

        current_entry = governing["current_governing_run"]
        candidates = [
            entry
            for entry in status["preserved_run_status_entries"]
            if entry["status_role"] == status_builder.ROLE_ELIGIBLE_NON_AUTHORITY
        ]
        self.assertEqual(1, len(candidates))
        proposal = self.valid_proposal(current_entry, candidates[0])

        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            transition = transition_resolver.resolve_governing_transition(proposal)
            transition_path = transition_resolver.write_governing_transition_result(
                transition
            )
        self.assertEqual(transition_resolver.OUTCOME_ACCEPTED, transition["outcome"])

        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            reresolution = reresolver.resolve_governing_reresolution_from_path(
                transition_path
            )
        reresolution_result_path = reresolution_path(reresolution, temp_root)
        write_json(reresolution_result_path, reresolution)
        self.assertEqual(reresolver.OUTCOME_SUCCESSOR_EMITTED, reresolution["outcome"])

        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            adoption = adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_result_path
            )
            adoption_path = adoption_resolver.write_governing_successor_adoption_result(
                adoption
            )
        self.assertEqual(adoption_resolver.OUTCOME_ADOPTED, adoption["outcome"])

        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            effective = effective_resolver.resolve_effective_current_family(adoption)
            effective_path = effective_resolver.write_effective_family_resolution(
                effective
            )
        self.assertEqual(
            effective_resolver.OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
            effective["outcome"],
        )

        with mock.patch.object(consumption_resolver, "_repo_root", return_value=temp_root):
            consumption = consumption_resolver.resolve_effective_family_consumption(
                effective
            )
            consumption_path = (
                consumption_resolver.write_effective_family_consumption_result(
                    consumption
                )
            )
        self.assertEqual(consumption_resolver.OUTCOME_CONSUMED, consumption["outcome"])

        with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
            work_input = work_input_resolver.resolve_current_work_input(consumption)
            work_input_path = work_input_resolver.write_current_work_input_resolution(
                work_input
            )
        self.assertEqual(
            work_input_resolver.OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
            work_input["outcome"],
        )

        with mock.patch.object(operation_resolver, "_repo_root", return_value=temp_root):
            operation = operation_resolver.resolve_current_work_operation(work_input)
            operation_path = operation_resolver.write_current_work_operation_result(
                operation
            )
        self.assertEqual(operation_resolver.OUTCOME_COMPLETED, operation["outcome"])

        with mock.patch.object(readout_resolver, "_repo_root", return_value=temp_root):
            readout = readout_resolver.resolve_current_state_readout(operation)
            readout_path = readout_resolver.write_current_state_readout_result(readout)
        self.assertEqual(readout_resolver.OUTCOME_EMITTED, readout["outcome"])

        with mock.patch.object(handoff_resolver, "_repo_root", return_value=temp_root):
            handoff = handoff_resolver.resolve_current_state_handoff(readout)
            handoff_path = handoff_resolver.write_current_state_handoff_result(handoff)
        self.assertEqual(handoff_resolver.OUTCOME_HANDED_OFF, handoff["outcome"])

        with mock.patch.object(export_resolver, "_repo_root", return_value=temp_root):
            export = export_resolver.resolve_current_state_export(handoff)
            export_path = export_resolver.write_current_state_export_result(export)
        self.assertEqual(export_resolver.OUTCOME_EXPORTED, export["outcome"])

        with mock.patch.object(delivery_resolver, "_repo_root", return_value=temp_root):
            delivery = delivery_resolver.resolve_current_state_delivery(export)
            delivery_path = delivery_resolver.write_current_state_delivery_result(
                delivery
            )
        self.assertEqual(delivery_resolver.OUTCOME_DELIVERED, delivery["outcome"])

        with mock.patch.object(application_resolver, "_repo_root", return_value=temp_root):
            application = application_resolver.resolve_current_state_application(
                delivery
            )
            application_path = (
                application_resolver.write_current_state_application_result(application)
            )
        self.assertEqual(application_resolver.OUTCOME_APPLIED, application["outcome"])

        with mock.patch.object(answer_resolver, "_repo_root", return_value=temp_root):
            answer = answer_resolver.resolve_current_state_answer_read(application)
            answer_path = answer_resolver.write_current_state_answer_read_result(answer)
        self.assertEqual(answer_resolver.OUTCOME_ANSWERED, answer["outcome"])

        with mock.patch.object(query_resolver, "_repo_root", return_value=temp_root):
            query = query_resolver.resolve_current_state_query(
                self.query_request(),
                answer,
            )
            query_path = query_resolver.write_current_state_query_result(query)
        self.assertEqual(query_resolver.OUTCOME_ANSWERED_QUERY, query["outcome"])

        with mock.patch.object(stand_resolver, "_repo_root", return_value=temp_root):
            stand = stand_resolver.resolve_current_state_what_stands_now(
                self.stand_request(),
                answer,
            )
            stand_path = stand_resolver.write_current_state_what_stands_now_result(
                stand
            )
        self.assertEqual(
            stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
            stand["outcome"],
        )

        with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
            open_result = open_resolver.resolve_current_state_what_remains_open(
                self.open_request(),
                answer,
            )
            open_path = open_resolver.write_current_state_what_remains_open_result(
                open_result
            )
        self.assertEqual(
            open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            open_result["outcome"],
        )

        with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
            derivation_touch = touch_resolver.resolve_current_state_touch_permission(
                self.touch_request(
                    touch_resolver.TOUCH_CLASS_DERIVATION,
                    DERIVATIVE_FIELDS,
                ),
                open_result,
            )
            derivation_touch_path = (
                touch_resolver.write_current_state_touch_permission_result(
                    derivation_touch
                )
            )
        self.assertEqual(
            touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            derivation_touch["outcome"],
        )

        return {
            "source": {
                "root": temp_root / authority_resolver.SOURCE_RUNS_ROOT,
                "paths": [source_one, source_two],
            },
            "ingress": {
                "root": temp_root / authority_resolver.INGRESS_RUNS_ROOT,
                "paths": [ingress_one, ingress_two],
            },
            "comparison": {
                "root": temp_root / authority_resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "paths": [comparison_one, comparison_two],
            },
            "authority": authority,
            "authority_path": authority_path,
            "family": family,
            "family_path": family_path,
            "status": status,
            "status_path": status_path,
            "governing": governing,
            "governing_path": governing_path,
            "transition": transition,
            "transition_path": transition_path,
            "reresolution": reresolution,
            "reresolution_path": reresolution_result_path,
            "adoption": adoption,
            "adoption_path": adoption_path,
            "effective": effective,
            "effective_path": effective_path,
            "consumption": consumption,
            "consumption_path": consumption_path,
            "work_input": work_input,
            "work_input_path": work_input_path,
            "operation": operation,
            "operation_path": operation_path,
            "readout": readout,
            "readout_path": readout_path,
            "handoff": handoff,
            "handoff_path": handoff_path,
            "export": export,
            "export_path": export_path,
            "delivery": delivery,
            "delivery_path": delivery_path,
            "application": application,
            "application_path": application_path,
            "answer": answer,
            "answer_path": answer_path,
            "query": query,
            "query_path": query_path,
            "stand": stand,
            "stand_path": stand_path,
            "open": open_result,
            "open_path": open_path,
            "derivation_touch": derivation_touch,
            "derivation_touch_path": derivation_touch_path,
        }

    def build_body_stack(self, temp_root: Path) -> dict[str, Any]:
        stack = self.build_current_state_stack(temp_root)

        transfer_path = temp_root / "artifacts" / "body_pass_lineage" / "transfer.json"
        with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
            transfer = transfer_resolver.resolve_continuity_transfer_unit_from_path(
                stack["open_path"],
                self.transfer_request(
                    transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                    DERIVATIVE_FIELDS,
                    basis="bounded derivative transfer for body pass",
                ),
                stack["derivation_touch_path"],
            )
            written_transfer_path = transfer_resolver.write_continuity_transfer_unit_result(
                transfer,
                transfer_path,
            )
        self.assertEqual(transfer_resolver.OUTCOME_TRANSFERRED, transfer["outcome"])

        receipt_path = temp_root / "artifacts" / "body_pass_lineage" / "receipt.json"
        with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
            receipt = receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                written_transfer_path,
                self.receipt_request(
                    receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
                    DERIVATIVE_FIELDS,
                    basis="bounded acceptance for body pass",
                ),
            )
            written_receipt_path = receipt_resolver.write_continuity_transfer_receipt_result(
                receipt,
                receipt_path,
            )
        self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, receipt["outcome"])

        participation_path = (
            temp_root / "artifacts" / "body_pass_lineage" / "participation.json"
        )
        with mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
            participation = (
                participation_resolver.resolve_received_derivative_participation_from_path(
                    written_receipt_path,
                    self.participation_request(),
                )
            )
            written_participation_path = (
                participation_resolver.write_received_derivative_participation_result(
                    participation,
                    participation_path,
                )
            )
        self.assertEqual(
            participation_resolver.OUTCOME_PARTICIPATED,
            participation["outcome"],
        )

        action_path = temp_root / "artifacts" / "body_pass_lineage" / "action.json"
        with mock.patch.object(action_resolver, "_repo_root", return_value=temp_root):
            action = action_resolver.resolve_received_derivative_action_permission_from_path(
                written_participation_path,
                self.action_request(),
            )
            written_action_path = (
                action_resolver.write_received_derivative_action_permission_result(
                    action,
                    action_path,
                )
            )
        self.assertEqual(action_resolver.OUTCOME_ACTION_PERMITTED, action["outcome"])

        seam_path = temp_root / "artifacts" / "body_pass_lineage" / "seam.json"
        with mock.patch.object(seam_resolver, "_repo_root", return_value=temp_root):
            seam = seam_resolver.resolve_continuity_memory_seam_from_path(
                written_action_path,
            )
            written_seam_path = seam_resolver.write_continuity_memory_seam_result(
                seam,
                seam_path,
            )
        self.assertEqual(seam_resolver.OUTCOME_SEAM_CLOSED, seam["outcome"])

        stack.update(
            {
                "transfer": transfer,
                "transfer_path": written_transfer_path,
                "receipt": receipt,
                "receipt_path": written_receipt_path,
                "participation": participation,
                "participation_path": written_participation_path,
                "action": action,
                "action_path": written_action_path,
                "seam": seam,
                "seam_path": written_seam_path,
            }
        )
        return stack

    def run_body(self, temp_root: Path, seam: Mapping[str, Any]) -> dict[str, Any]:
        with mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
            return body_pass.run_v0_body_pass(seam)

    def run_body_from_path(self, temp_root: Path, seam_path: Path | str) -> dict[str, Any]:
        with mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
            return body_pass.run_v0_body_pass_from_path(seam_path)

    def assert_top_level(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(TOP_LEVEL, set(result))

    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assert_top_level(result)
        self.assertEqual(body_pass.OUTCOME_BLOCKED, result["outcome"])
        block = result["block"]
        self.assertIsInstance(block, dict)
        self.assertEqual(code, block.get("block_code"))
        self.assertIsInstance(block.get("block_reason"), str)
        self.assertTrue(block["block_reason"])

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        required_false = {
            "replayed_into_live_host",
            "merged_into_local_state",
            "continuity_completed",
            "standing_upgraded",
            "source_replaced",
            "overwrite_style_correction",
            "latest_file_currentness",
            "recency_fraud",
            "standing_memory_collapsed_with_interpretation",
            "final_v0_body_pass_completed",
        }
        self.assertTrue(required_false.issubset(non_claims))
        for claim_name, value in non_claims.items():
            if isinstance(value, bool):
                self.assertFalse(value, claim_name)

    def assert_body_confirmed(self, result: Mapping[str, Any]) -> None:
        self.assert_top_level(result)
        self.assertEqual(body_pass.OUTCOME_V0_BODY_PASS_CONFIRMED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assert_non_claims_false(result)

        posture = result["body_pass_posture"]
        self.assertIsInstance(posture, dict)
        for key in (
            "organs_present_and_successful",
            "lineage_preserved",
            "currentness_without_recency_fraud",
            "derivative_carry_without_source_collapse",
            "closure_seam_stands",
            "v0_body_reads_as_one_bounded_body",
        ):
            self.assertIs(posture.get(key), True, key)

        checks = result["checks"]
        self.assertIsInstance(checks, list)
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertIsInstance(check.get("check_name"), str)
            self.assertIsInstance(check.get("passed"), bool)
        self.assertTrue(all(check["passed"] for check in checks))
        self.assertTrue(any("expected_posture" in check for check in checks))
        self.assertTrue(any("actual_posture" in check for check in checks))

    def test_confirms_real_body_pass_and_preserves_sections(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)

            direct = self.run_body(temp_root, stack["seam"])
            from_path = self.run_body_from_path(temp_root, stack["seam_path"])
            self.assert_body_confirmed(direct)
            self.assert_body_confirmed(from_path)

            metadata = from_path["v0_body_pass_metadata"]
            for key in (
                "v0_body_pass_result_id",
                "v0_body_pass_result_type",
                "v0_body_pass_result_version",
                "generated_at",
                "runner_module",
            ):
                self.assertIsInstance(metadata.get(key), str)
                self.assertTrue(metadata[key])

            selected_seam = from_path["selected_seam_result"]
            seam_metadata = stack["seam"]["continuity_memory_seam_metadata"]
            self.assertTrue(selected_seam["selected_seam_result_path"])
            self.assertEqual(
                seam_metadata["continuity_memory_seam_result_id"],
                selected_seam["selected_seam_result_id"],
            )
            self.assertEqual(
                seam_metadata["continuity_memory_seam_result_type"],
                selected_seam["selected_seam_result_type"],
            )
            self.assertEqual(
                seam_resolver.OUTCOME_SEAM_CLOSED,
                selected_seam["selected_seam_result_outcome"],
            )

            selected_action = from_path["selected_action_permission_result"]
            selected_participation = from_path["selected_participation_result"]
            selected_receipt = from_path["selected_receipt_result"]
            selected_transfer = from_path["selected_transfer_result"]
            selected_touch = from_path["selected_touch_permission_result"]
            selected_source = from_path["selected_source_surface"]
            self.assertEqual(
                stack["action"]["received_derivative_action_permission_metadata"][
                    "received_derivative_action_permission_result_id"
                ],
                selected_action["selected_action_permission_result_id"],
            )
            self.assertEqual(
                action_resolver.OUTCOME_ACTION_PERMITTED,
                selected_action["selected_action_permission_result_outcome"],
            )
            self.assertTrue(selected_action["selected_action_permission_result_path"])
            self.assertEqual(
                stack["participation"]["received_derivative_participation_metadata"][
                    "received_derivative_participation_result_id"
                ],
                selected_participation["selected_participation_result_id"],
            )
            self.assertEqual(
                participation_resolver.OUTCOME_PARTICIPATED,
                selected_participation["selected_participation_result_outcome"],
            )
            self.assertTrue(selected_participation["selected_participation_result_path"])
            self.assertEqual(
                stack["receipt"]["continuity_transfer_receipt_metadata"][
                    "continuity_transfer_receipt_result_id"
                ],
                selected_receipt["selected_receipt_result_id"],
            )
            self.assertEqual(
                receipt_resolver.OUTCOME_RECEIVED,
                selected_receipt["selected_receipt_result_outcome"],
            )
            self.assertTrue(selected_receipt["selected_receipt_result_path"])
            self.assertEqual(
                stack["transfer"]["continuity_transfer_metadata"][
                    "continuity_transfer_result_id"
                ],
                selected_transfer["selected_transfer_result_id"],
            )
            self.assertEqual(
                transfer_resolver.OUTCOME_TRANSFERRED,
                selected_transfer["selected_transfer_result_outcome"],
            )
            self.assertTrue(selected_transfer["selected_transfer_result_path"])
            self.assertEqual(
                stack["derivation_touch"]["touch_permission_metadata"][
                    "touch_permission_result_id"
                ],
                selected_touch["selected_touch_permission_result_id"],
            )
            self.assertEqual(
                touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
                selected_touch["selected_touch_permission_result_outcome"],
            )
            self.assertEqual(
                stack["open"]["what_remains_open_metadata"][
                    "what_remains_open_result_id"
                ],
                selected_source["selected_source_surface_id"],
            )
            self.assertTrue(selected_source["selected_source_surface_path"])
            self.assertEqual(
                "what_remains_open",
                selected_source["selected_source_surface_family"],
            )
            self.assertEqual(
                open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                selected_source["selected_source_surface_outcome"],
            )
            self.assertIsInstance(
                selected_source["selected_source_surface_effective_references"],
                dict,
            )

            check_names = {check["check_name"] for check in from_path["checks"]}
            for expected_name in (
                "selected_seam_result_has_closed_outcome",
                "selected_action_result_exists_and_is_readable",
                "selected_participation_result_exists_and_is_readable",
                "selected_receipt_result_exists_and_is_readable",
                "selected_transfer_result_exists_and_is_readable",
                "selected_touch_permission_result_exists_and_is_readable",
                "current_state_answer_read_organ_is_present_readable_and_successful",
                "current_state_what_stands_now_organ_is_present_readable_and_successful",
                "current_state_what_remains_open_organ_is_present_readable_and_successful",
                "lineage_across_source_touch_transfer_receipt_participation_action_seam_is_explicit",
                "body_pass_does_not_use_latest_file_inference",
                "body_pass_does_not_claim_recency_as_currentness",
                "body_pass_does_not_use_overwrite_style_correction",
                "body_pass_posture_v0_reads_as_one_bounded_body",
            ):
                self.assertIn(expected_name, check_names)

            summary = body_pass.build_v0_body_pass_summary(from_path)
            self.assertEqual(
                body_pass.OUTCOME_V0_BODY_PASS_CONFIRMED,
                summary["outcome"],
            )
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(
                selected_seam["selected_seam_result_id"],
                summary["selected_seam_result_id"],
            )
            self.assertEqual(
                selected_action["selected_action_permission_result_id"],
                summary["selected_action_permission_result_id"],
            )
            self.assertEqual(
                selected_participation["selected_participation_result_id"],
                summary["selected_participation_result_id"],
            )
            self.assertEqual(
                selected_receipt["selected_receipt_result_id"],
                summary["selected_receipt_result_id"],
            )
            self.assertEqual(
                selected_transfer["selected_transfer_result_id"],
                summary["selected_transfer_result_id"],
            )
            self.assertEqual(
                selected_touch["selected_touch_permission_result_id"],
                summary["selected_touch_permission_result_id"],
            )
            self.assertEqual(
                selected_source["selected_source_surface_id"],
                summary["selected_source_surface_id"],
            )
            self.assertEqual(0, summary["failed_check_count"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(from_path["body_pass_posture"], summary["body_pass_posture"])
            self.assertIsInstance(summary["key_non_claims"], dict)

    def test_write_behavior_default_output_and_path_consistency(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)
            direct = self.run_body(temp_root, stack["seam"])
            from_path = self.run_body_from_path(temp_root, stack["seam_path"])
            self.assert_body_confirmed(direct)
            self.assert_body_confirmed(from_path)
            self.assertEqual(direct["outcome"], from_path["outcome"])
            self.assertEqual(
                direct["selected_action_permission_result"][
                    "selected_action_permission_result_id"
                ],
                from_path["selected_action_permission_result"][
                    "selected_action_permission_result_id"
                ],
            )
            self.assertEqual(
                "provided_mapping",
                direct["selected_seam_result"]["selected_seam_result_path"],
            )
            self.assertNotEqual(
                direct["selected_seam_result"]["selected_seam_result_path"],
                from_path["selected_seam_result"]["selected_seam_result_path"],
            )

            explicit_path = temp_root / "written" / "nested" / "body_pass.json"
            written = body_pass.write_v0_body_pass_result(from_path, explicit_path)
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.is_file())
            self.assertEqual(TOP_LEVEL, set(read_json(written)))
            with self.assertRaises(FileExistsError):
                body_pass.write_v0_body_pass_result(from_path, explicit_path)

            default_root = temp_root / "default_body_pass"
            with mock.patch.object(
                body_pass,
                "V0_BODY_PASS_ROOT",
                Path("default_body_pass"),
            ), mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
                first = body_pass.write_v0_body_pass_result(from_path)
                second = body_pass.write_v0_body_pass_result(from_path)
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertEqual(default_root, first.parent)
            self.assertNotEqual(first, second)
            self.assertTrue(first.name.endswith("__v0_body_pass_result.json"))
            self.assertIn("_001", second.stem)

    def test_blocks_no_admissible_non_closed_and_upstream_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(
                body_pass,
                "CONTINUITY_MEMORY_SEAM_ROOT",
                Path("missing_seams"),
            ), mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
                no_seam = body_pass.run_v0_body_pass()
            self.assert_block(no_seam, "NO_ADMISSIBLE_SEAM_RESULT")

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)

            blocked_seam = copied(stack["seam"])
            blocked_seam["outcome"] = seam_resolver.OUTCOME_BLOCKED
            self.assert_block(
                self.run_body(temp_root, blocked_seam),
                "SELECTED_SEAM_RESULT_NOT_CLOSED",
            )

            unreadable_action = copied(stack["seam"])
            unreadable_action["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = "missing/action.json"
            self.assert_block(
                self.run_body(temp_root, unreadable_action),
                "UPSTREAM_ORGAN_UNREADABLE",
            )

            bad_action = copied(stack["action"])
            bad_action["outcome"] = action_resolver.OUTCOME_REFUSED
            bad_action_path = write_json(
                temp_root / "bad_organs" / "action_refused.json",
                bad_action,
            )
            non_successful = copied(stack["seam"])
            non_successful["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(bad_action_path)
            self.assert_block(
                self.run_body(temp_root, non_successful),
                "UPSTREAM_ORGAN_NOT_SUCCESSFUL",
            )

            malformed_shape = {"outcome": seam_resolver.OUTCOME_SEAM_CLOSED}
            self.assert_block(
                self.run_body(temp_root, malformed_shape),
                "SELECTED_SEAM_RESULT_MALFORMED",
            )

    def test_blocks_shortcuts_lineage_collapse_and_conflicts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)

            latest_action = copied(stack["action"])
            latest_action["action_permission_request"][
                "action_basis"
            ] = "use latest file inference in body pass"
            latest_path = write_json(temp_root / "bad_actions" / "latest.json", latest_action)
            latest_seam = copied(stack["seam"])
            latest_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(latest_path)
            self.assert_block(
                self.run_body(temp_root, latest_seam),
                "LATEST_FILE_INFERENCE_REFUSED",
            )

            recency_action = copied(stack["action"])
            recency_action["action_permission_request"]["action_basis"] = "newest file wins"
            recency_path = write_json(temp_root / "bad_actions" / "recency.json", recency_action)
            recency_seam = copied(stack["seam"])
            recency_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(recency_path)
            self.assert_block(
                self.run_body(temp_root, recency_seam),
                "RECENCY_FRAUD_REFUSED",
            )

            overwrite_action = copied(stack["action"])
            overwrite_action["action_permission_request"][
                "action_basis"
            ] = "overwrite the prior preserved surface"
            overwrite_path = write_json(
                temp_root / "bad_actions" / "overwrite.json",
                overwrite_action,
            )
            overwrite_seam = copied(stack["seam"])
            overwrite_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(overwrite_path)
            self.assert_block(
                self.run_body(temp_root, overwrite_seam),
                "OVERWRITE_STYLE_CORRECTION_REFUSED",
            )

            source_replaced_action = copied(stack["action"])
            source_replaced_action["action_permission_request"][
                "action_basis"
            ] = "replace source with the permitted derivative"
            source_replaced_path = write_json(
                temp_root / "bad_actions" / "source_replaced.json",
                source_replaced_action,
            )
            source_replaced_seam = copied(stack["seam"])
            source_replaced_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(source_replaced_path)
            self.assert_block(
                self.run_body(temp_root, source_replaced_seam),
                "SOURCE_REPLACEMENT_REFUSED",
            )

            collapsed_action = copied(stack["action"])
            collapsed_action["action_permission_payload"]["source_remains_source"] = False
            collapsed_path = write_json(
                temp_root / "bad_actions" / "collapsed.json",
                collapsed_action,
            )
            collapsed_seam = copied(stack["seam"])
            collapsed_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(collapsed_path)
            self.assert_block(
                self.run_body(temp_root, collapsed_seam),
                "SOURCE_TRANSFER_RECEIPT_PARTICIPATION_ACTION_COLLAPSE_REFUSED",
            )

            collapsed_memory_action = copied(stack["action"])
            collapsed_memory_action["action_permission_request"][
                "action_basis"
            ] = "action is whole memory"
            collapsed_memory_path = write_json(
                temp_root / "bad_actions" / "collapsed_memory.json",
                collapsed_memory_action,
            )
            collapsed_memory_seam = copied(stack["seam"])
            collapsed_memory_seam["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(collapsed_memory_path)
            self.assert_block(
                self.run_body(temp_root, collapsed_memory_seam),
                "STANDING_MEMORY_COLLAPSED_WITH_INTERPRETATION_REFUSED",
            )

            bad_lineage = copied(stack["seam"])
            bad_lineage["selected_participation_result"][
                "selected_participation_result_id"
            ] = "wrong_participation_id"
            self.assert_block(
                self.run_body(temp_root, bad_lineage),
                "LINEAGE_INCOHERENCE",
            )

            seam_root = temp_root / "seams"
            first = copied(stack["seam"])
            second = copied(stack["seam"])
            second["selected_source_surface"]["selected_source_surface_id"] = (
                "conflicting_source_surface_id"
            )
            write_json(seam_root / "a.json", first)
            write_json(seam_root / "b.json", second)
            with mock.patch.object(
                body_pass,
                "CONTINUITY_MEMORY_SEAM_ROOT",
                Path("seams"),
            ), mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
                conflict = body_pass.run_v0_body_pass()
            self.assert_block(
                conflict,
                "MULTIPLE_BODY_PASS_TIPS_CONFLICT_UNRESOLVED",
            )

    def test_hard_malformed_failures(self) -> None:
        with self.assertRaises(body_pass.V0BodyPassError):
            body_pass.run_v0_body_pass("not a mapping")  # type: ignore[arg-type]

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)

            with self.assertRaises(body_pass.V0BodyPassError):
                self.run_body(
                    temp_root,
                    {
                        "continuity_memory_seam_metadata": {
                            "continuity_memory_seam_result_id": "x"
                        }
                    },
                )

            malformed_path = temp_root / "bad" / "seam.json"
            malformed_path.parent.mkdir(parents=True, exist_ok=True)
            malformed_path.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(body_pass.V0BodyPassError):
                self.run_body_from_path(temp_root, malformed_path)

            bad_action_path = temp_root / "bad" / "action.json"
            bad_action_path.write_text("{not-json", encoding="utf-8")
            bad_lineage = copied(stack["seam"])
            bad_lineage["selected_action_permission_result"][
                "selected_action_permission_result_path"
            ] = str(bad_action_path)
            with self.assertRaises(body_pass.V0BodyPassError):
                self.run_body(temp_root, bad_lineage)

            bad_effective = copied(stack["seam"])
            bad_effective["selected_source_surface"][
                "selected_source_surface_effective_references"
            ] = 123
            with self.assertRaises(body_pass.V0BodyPassError):
                self.run_body(temp_root, bad_effective)

            root_file = temp_root / "seam_root_file"
            root_file.write_text("not a directory", encoding="utf-8")
            with mock.patch.object(
                body_pass,
                "CONTINUITY_MEMORY_SEAM_ROOT",
                Path("seam_root_file"),
            ), mock.patch.object(body_pass, "_repo_root", return_value=temp_root):
                with self.assertRaises(body_pass.V0BodyPassError):
                    body_pass.run_v0_body_pass()

    def test_non_mutation_posture_for_repeated_body_pass_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_body_stack(temp_root)

            before_tree = tree_digest(temp_root)
            before_seam = copied(stack["seam"])
            first = self.run_body(temp_root, stack["seam"])
            second = self.run_body(temp_root, stack["seam"])
            self.assert_body_confirmed(first)
            self.assert_body_confirmed(second)
            self.assertEqual(before_tree, tree_digest(temp_root))
            self.assertEqual(before_seam, stack["seam"])


if __name__ == "__main__":
    unittest.main()
