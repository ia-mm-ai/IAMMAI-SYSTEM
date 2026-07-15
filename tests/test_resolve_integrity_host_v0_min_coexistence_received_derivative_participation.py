"""Bounded tests for the v0-min received-derivative participation resolver.

This suite exercises the post-receipt participation bridge now implemented in
``resolve_integrity_host_v0_min_coexistence_received_derivative_participation``.
It builds real local upstream artifacts through receipt, then verifies that
participation remains an additive bounded-use surface over a received
derivative. It does not test replay, merge, registry, persistence, final
governance, or continuity-completion behavior.
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
import resolve_integrity_host_v0_min_coexistence_received_derivative_participation as participation_resolver
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner


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
)

TOP_LEVEL = {
    "received_derivative_participation_metadata",
    "selected_receipt_result",
    "selected_transfer_result",
    "selected_source_surface",
    "participation_request",
    "checks",
    "outcome",
    "block",
    "participation_payload",
    "participation_summary",
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
REFERENCE_PARTICIPATION_FIELDS = [
    "selected_receipt_result_id",
    "selected_transfer_result_id",
    "selected_source_surface_id",
    "selected_source_surface_family",
    "received_references",
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
    target.write_text(json.dumps(value, indent=2, sort_keys=True), encoding="utf-8")
    return target


def copied(value: Mapping[str, Any]) -> dict[str, Any]:
    return copy.deepcopy(dict(value))


def display_path(temp_root: Path, path: Path | str) -> str:
    resolved = Path(path).resolve()
    try:
        return str(resolved.relative_to(temp_root.resolve()))
    except ValueError:
        return str(resolved)


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
    run_dir = resolve_path(run_dir_text, temp_root)
    candidates = sorted(run_dir.glob("*_result.json"))
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


class ReceivedDerivativeParticipationTests(unittest.TestCase):
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
            "transition_proposal_id": "proposal_accepted_for_participation",
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
            "proposal_basis_ref": "bounded explicit participation test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_"
                "received_derivative_participation.py"
            ),
        }

    def query_request(self, fields: list[str] | None = None) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_participation",
            "query_target": "answer_read_output",
            "requested_fields": list(fields if fields is not None else QUERY_FIELDS),
            "query_basis": "bounded participation test query over emitted answer surface",
        }

    def stand_request(self, fields: list[str] | None = None) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "unit_test_what_stands_now",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(fields if fields is not None else STAND_FIELDS),
            "query_basis": "bounded participation test stand query over emitted answer surface",
        }

    def open_request(self, fields: list[str] | None = None) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "unit_test_what_remains_open",
            "query_family": "what_remains_open",
            "requested_open_fields": list(fields if fields is not None else OPEN_FIELDS),
            "query_basis": "bounded participation test open-surface question",
        }

    def touch_request(
        self,
        touch_class: str,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded participation test touch basis",
    ) -> dict[str, Any]:
        return {
            "touch_request_id": f"unit_test_touch_{touch_class.lower()}",
            "requested_touch_class": touch_class,
            "requested_touch_basis": basis,
            "requesting_surface_label": "unit_test_touch_surface",
            "intended_downstream_use": "bounded participation test",
            "requested_touch_fields": list(fields if fields is not None else []),
        }

    def transfer_request(
        self,
        transfer_class: str = transfer_resolver.TRANSFER_CLASS_REFERENCE,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded participation test transfer basis",
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_request_id": f"unit_test_transfer_{transfer_class.lower()}",
            "transfer_class": transfer_class,
            "transfer_basis": basis,
            "requested_transfer_fields": list(fields if fields is not None else []),
            "target_seam_label": "unit_test_seam",
        }

    def receipt_request(
        self,
        receipt_class: str = receipt_resolver.RECEIPT_CLASS_VALIDATION,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded participation validation receipt",
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_receipt_request_id": (
                f"unit_test_receipt_{receipt_class.lower()}"
            ),
            "receipt_class": receipt_class,
            "receipt_basis": basis,
            "requested_receipt_fields": list(fields if fields is not None else []),
            "receiving_boundary_label": "unit_test_receiving_boundary",
        }

    def participation_request(
        self,
        participant_class: str = participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
        use_class: str = participation_resolver.USE_CLASS_READ,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded participation read",
    ) -> dict[str, Any]:
        return {
            "received_derivative_participation_request_id": (
                f"unit_test_participation_{participant_class.lower()}_{use_class.lower()}"
            ),
            "participant_class": participant_class,
            "use_class": use_class,
            "participation_basis": basis,
            "requested_participation_fields": list(fields if fields is not None else []),
            "participating_surface_label": "unit_test_participating_surface",
        }

    def build_stack(self, temp_root: Path) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260422T020000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260422T020001_000000Z")
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
        self.assertEqual(len(candidates), 1)
        proposal = self.valid_proposal(current_entry, candidates[0])

        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            transition = transition_resolver.resolve_governing_transition(proposal)
            transition_path = transition_resolver.write_governing_transition_result(
                transition
            )
        self.assertEqual(transition["outcome"], transition_resolver.OUTCOME_ACCEPTED)

        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            reresolution = reresolver.resolve_governing_reresolution_from_path(
                transition_path
            )
        reresolution_result_path = reresolution_path(reresolution, temp_root)
        write_json(reresolution_result_path, reresolution)
        self.assertEqual(reresolution["outcome"], reresolver.OUTCOME_SUCCESSOR_EMITTED)

        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            adoption = adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_result_path
            )
            adoption_path = adoption_resolver.write_governing_successor_adoption_result(
                adoption
            )
        self.assertEqual(adoption["outcome"], adoption_resolver.OUTCOME_ADOPTED)

        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            effective = effective_resolver.resolve_effective_current_family(adoption)
            effective_path = effective_resolver.write_effective_family_resolution(
                effective
            )
        self.assertEqual(
            effective["outcome"],
            effective_resolver.OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
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
        self.assertEqual(consumption["outcome"], consumption_resolver.OUTCOME_CONSUMED)

        with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
            work_input = work_input_resolver.resolve_current_work_input(consumption)
            work_input_path = work_input_resolver.write_current_work_input_resolution(
                work_input
            )
        self.assertEqual(
            work_input["outcome"],
            work_input_resolver.OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
        )

        with mock.patch.object(operation_resolver, "_repo_root", return_value=temp_root):
            operation = operation_resolver.resolve_current_work_operation(work_input)
            operation_path = operation_resolver.write_current_work_operation_result(
                operation
            )
        self.assertEqual(operation["outcome"], operation_resolver.OUTCOME_COMPLETED)

        with mock.patch.object(readout_resolver, "_repo_root", return_value=temp_root):
            readout = readout_resolver.resolve_current_state_readout(operation)
            readout_path = readout_resolver.write_current_state_readout_result(readout)
        self.assertEqual(readout["outcome"], readout_resolver.OUTCOME_EMITTED)

        with mock.patch.object(handoff_resolver, "_repo_root", return_value=temp_root):
            handoff = handoff_resolver.resolve_current_state_handoff(readout)
            handoff_path = handoff_resolver.write_current_state_handoff_result(handoff)
        self.assertEqual(handoff["outcome"], handoff_resolver.OUTCOME_HANDED_OFF)

        with mock.patch.object(export_resolver, "_repo_root", return_value=temp_root):
            export = export_resolver.resolve_current_state_export(handoff)
            export_path = export_resolver.write_current_state_export_result(export)
        self.assertEqual(export["outcome"], export_resolver.OUTCOME_EXPORTED)

        with mock.patch.object(delivery_resolver, "_repo_root", return_value=temp_root):
            delivery = delivery_resolver.resolve_current_state_delivery(export)
            delivery_path = delivery_resolver.write_current_state_delivery_result(
                delivery
            )
        self.assertEqual(delivery["outcome"], delivery_resolver.OUTCOME_DELIVERED)

        with mock.patch.object(application_resolver, "_repo_root", return_value=temp_root):
            application = application_resolver.resolve_current_state_application(
                delivery
            )
            application_path = (
                application_resolver.write_current_state_application_result(application)
            )
        self.assertEqual(application["outcome"], application_resolver.OUTCOME_APPLIED)

        with mock.patch.object(answer_resolver, "_repo_root", return_value=temp_root):
            answer = answer_resolver.resolve_current_state_answer_read(application)
            answer_path = answer_resolver.write_current_state_answer_read_result(answer)
        self.assertEqual(answer["outcome"], answer_resolver.OUTCOME_ANSWERED)

        with mock.patch.object(query_resolver, "_repo_root", return_value=temp_root):
            query = query_resolver.resolve_current_state_query(
                self.query_request(),
                answer,
            )
            query_path = query_resolver.write_current_state_query_result(query)
        self.assertEqual(query["outcome"], query_resolver.OUTCOME_ANSWERED_QUERY)

        with mock.patch.object(stand_resolver, "_repo_root", return_value=temp_root):
            stand = stand_resolver.resolve_current_state_what_stands_now(
                self.stand_request(),
                answer,
            )
            stand_path = stand_resolver.write_current_state_what_stands_now_result(
                stand
            )
        self.assertEqual(
            stand["outcome"],
            stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
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
            open_result["outcome"],
            open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
        )

        with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
            read_touch = touch_resolver.resolve_current_state_touch_permission(
                self.touch_request(touch_resolver.TOUCH_CLASS_READ_ONLY),
                open_result,
            )
            read_touch_path = touch_resolver.write_current_state_touch_permission_result(
                read_touch
            )
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
        self.assertEqual(read_touch["outcome"], touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH)
        self.assertEqual(
            derivation_touch["outcome"],
            touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
        )

        transfer_root = temp_root / "artifacts" / "transfer"
        with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
            reference_transfer = transfer_resolver.resolve_continuity_transfer_unit(
                self.transfer_request(),
                open_result,
                read_touch,
            )
            derivative_transfer = transfer_resolver.resolve_continuity_transfer_unit(
                self.transfer_request(
                    transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                    DERIVATIVE_FIELDS,
                ),
                open_result,
                derivation_touch,
            )
            reference_transfer_path = (
                transfer_resolver.write_continuity_transfer_unit_result(
                    reference_transfer,
                    transfer_root / "reference_transfer.json",
                )
            )
            derivative_transfer_path = (
                transfer_resolver.write_continuity_transfer_unit_result(
                    derivative_transfer,
                    transfer_root / "derivative_transfer.json",
                )
            )
        self.assertEqual(transfer_resolver.OUTCOME_TRANSFERRED, reference_transfer["outcome"])
        self.assertEqual(transfer_resolver.OUTCOME_TRANSFERRED, derivative_transfer["outcome"])

        receipt_root = temp_root / "artifacts" / "receipts"
        with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
            reference_receipt = receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                reference_transfer_path,
                self.receipt_request(),
            )
            derivative_receipt = (
                receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                    derivative_transfer_path,
                    self.receipt_request(
                        receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
                        DERIVATIVE_FIELDS,
                        basis="bounded acceptance for participation tests",
                    ),
                )
            )
            reference_receipt_path = (
                receipt_resolver.write_continuity_transfer_receipt_result(
                    reference_receipt,
                    receipt_root / "reference_receipt.json",
                )
            )
            derivative_receipt_path = (
                receipt_resolver.write_continuity_transfer_receipt_result(
                    derivative_receipt,
                    receipt_root / "derivative_receipt.json",
                )
            )
        self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, reference_receipt["outcome"])
        self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, derivative_receipt["outcome"])

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
            "read_touch": read_touch,
            "read_touch_path": read_touch_path,
            "derivation_touch": derivation_touch,
            "derivation_touch_path": derivation_touch_path,
            "reference_transfer": reference_transfer,
            "reference_transfer_path": reference_transfer_path,
            "derivative_transfer": derivative_transfer,
            "derivative_transfer_path": derivative_transfer_path,
            "receipt_root": receipt_root,
            "reference_receipt": reference_receipt,
            "reference_receipt_path": reference_receipt_path,
            "derivative_receipt": derivative_receipt,
            "derivative_receipt_path": derivative_receipt_path,
        }

    def assert_top_level(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(TOP_LEVEL, set(result))

    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assert_top_level(result)
        self.assertEqual(participation_resolver.OUTCOME_REFUSED, result["outcome"])
        block = result["block"]
        self.assertIsInstance(block, dict)
        self.assertEqual(code, block.get("block_code"))
        self.assertIsInstance(block.get("block_reason"), str)
        self.assertTrue(block["block_reason"])
        self.assertIsNone(result["participation_payload"])

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        required_false = {
            "replayed_into_live_host",
            "merged_into_local_state",
            "continuity_completed",
            "standing_upgraded",
            "source_replaced",
            "final_received_derivative_participation_completed",
        }
        self.assertTrue(required_false.issubset(non_claims))
        for claim_name, value in non_claims.items():
            if isinstance(value, bool):
                self.assertFalse(value, claim_name)
        for key in required_false:
            self.assertFalse(non_claims[key], key)

    def assert_participated(self, result: Mapping[str, Any]) -> None:
        self.assert_top_level(result)
        self.assertEqual(participation_resolver.OUTCOME_PARTICIPATED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsInstance(result["participation_payload"], dict)
        self.assert_non_claims_false(result)
        checks = result["checks"]
        self.assertIsInstance(checks, list)
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertIsInstance(check.get("check_name"), str)
            self.assertIsInstance(check.get("passed"), bool)
        self.assertTrue(all(check["passed"] for check in checks))

    def resolve_participation(
        self,
        temp_root: Path,
        request: Mapping[str, Any],
        receipt: Mapping[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
            return participation_resolver.resolve_received_derivative_participation(
                request,
                receipt,
            )

    def test_participates_read_reference_and_derivative_from_real_receipts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            read_request = self.participation_request()
            read_result = self.resolve_participation(
                temp_root,
                read_request,
                stack["reference_receipt"],
            )
            self.assert_participated(read_result)
            self.assertEqual(read_request, read_result["participation_request"])

            metadata = read_result["received_derivative_participation_metadata"]
            for key in (
                "received_derivative_participation_result_id",
                "received_derivative_participation_result_type",
                "received_derivative_participation_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assertIsInstance(metadata.get(key), str)
                self.assertTrue(metadata[key])

            selected_receipt = read_result["selected_receipt_result"]
            self.assertEqual(
                stack["reference_receipt"]["continuity_transfer_receipt_metadata"][
                    "continuity_transfer_receipt_result_id"
                ],
                selected_receipt["selected_receipt_result_id"],
            )
            self.assertEqual(
                receipt_resolver.OUTCOME_RECEIVED,
                selected_receipt["selected_receipt_result_outcome"],
            )
            self.assertEqual(
                receipt_resolver.RECEIPT_CLASS_VALIDATION,
                selected_receipt["receipt_class"],
            )

            selected_transfer = read_result["selected_transfer_result"]
            self.assertEqual(
                stack["reference_transfer"]["continuity_transfer_metadata"][
                    "continuity_transfer_result_id"
                ],
                selected_transfer["selected_transfer_result_id"],
            )
            self.assertEqual(
                transfer_resolver.TRANSFER_CLASS_REFERENCE,
                selected_transfer["transfer_class"],
            )
            self.assertTrue(selected_transfer["transfer_basis"])

            selected_source = read_result["selected_source_surface"]
            self.assertTrue(selected_source["selected_source_surface_id"])
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

            payload = read_result["participation_payload"]
            self.assertEqual(
                "participated_received_derivative",
                payload["payload_participation_status"],
            )
            self.assertTrue(payload["source_remains_source"])
            self.assertTrue(payload["receipt_remains_receipt"])
            self.assertTrue(payload["transfer_remains_transfer"])
            self.assertTrue(payload["participation_payload_remains_derivative"])
            self.assertIsInstance(payload["participated_fields"], dict)
            self.assertIsInstance(payload["participated_references"], dict)
            for forbidden in (
                "hidden_provenance",
                "replay_authority",
                "merge_authority",
                "continuity_completion_claim",
                "final_identity_claim",
                "source_replacement",
                "latest_file_inference",
            ):
                self.assertNotIn(forbidden, payload)

            summary = participation_resolver.build_received_derivative_participation_summary(
                read_result,
            )
            self.assertEqual(participation_resolver.OUTCOME_PARTICIPATED, summary["outcome"])
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(
                selected_receipt["selected_receipt_result_id"],
                summary["selected_receipt_result_id"],
            )
            self.assertEqual(
                selected_transfer["selected_transfer_result_id"],
                summary["selected_transfer_result_id"],
            )
            self.assertEqual(
                selected_source["selected_source_surface_id"],
                summary["selected_source_surface_id"],
            )
            self.assertEqual(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                summary["participant_class"],
            )
            self.assertEqual(participation_resolver.USE_CLASS_READ, summary["use_class"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(0, summary["failed_check_count"])
            self.assertIsInstance(summary["key_non_claims"], dict)

            reference_request = self.participation_request(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                participation_resolver.USE_CLASS_REFERENCE,
                REFERENCE_PARTICIPATION_FIELDS,
                basis="bounded reference participation over receipt lineage",
            )
            reference_result = self.resolve_participation(
                temp_root,
                reference_request,
                stack["reference_receipt"],
            )
            self.assert_participated(reference_result)
            reference_payload = reference_result["participation_payload"]
            self.assertTrue(reference_payload["receipt_remains_receipt"])
            self.assertTrue(reference_payload["transfer_remains_transfer"])
            self.assertTrue(reference_payload["source_remains_source"])
            self.assertEqual(
                set(REFERENCE_PARTICIPATION_FIELDS),
                set(reference_payload["participated_fields"]),
            )

            derivative_request = self.participation_request(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_DERIVATION,
                participation_resolver.USE_CLASS_DERIVATIVE,
                DERIVATIVE_FIELDS,
                basis="one bounded downstream derivative from received fields",
            )
            derivative_result = self.resolve_participation(
                temp_root,
                derivative_request,
                stack["derivative_receipt"],
            )
            self.assert_participated(derivative_result)
            derivative_payload = derivative_result["participation_payload"]
            self.assertEqual(
                "participated_received_derivative",
                derivative_payload["payload_participation_status"],
            )
            self.assertTrue(derivative_payload["source_remains_source"])
            self.assertTrue(derivative_payload["receipt_remains_receipt"])
            self.assertTrue(derivative_payload["transfer_remains_transfer"])
            self.assertTrue(derivative_payload["participation_payload_remains_derivative"])
            self.assertEqual(
                set(DERIVATIVE_FIELDS),
                set(derivative_payload["participated_fields"]),
            )

    def test_explicit_path_resolution_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            request = self.participation_request()

            from_object = self.resolve_participation(
                temp_root,
                request,
                stack["reference_receipt"],
            )
            with mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
                from_path = participation_resolver.resolve_received_derivative_participation_from_path(
                    stack["reference_receipt_path"],
                    request,
                )
            self.assert_participated(from_path)
            self.assertEqual(from_object["outcome"], from_path["outcome"])
            self.assertEqual(
                from_object["selected_receipt_result"]["selected_receipt_result_id"],
                from_path["selected_receipt_result"]["selected_receipt_result_id"],
            )
            self.assertNotEqual(
                from_object["selected_receipt_result"]["selected_receipt_result_path"],
                from_path["selected_receipt_result"]["selected_receipt_result_path"],
            )

            explicit_path = temp_root / "written" / "nested" / "participation.json"
            written = participation_resolver.write_received_derivative_participation_result(
                from_path,
                explicit_path,
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.is_file())
            self.assertEqual(TOP_LEVEL, set(read_json(written)))
            with self.assertRaises(FileExistsError):
                participation_resolver.write_received_derivative_participation_result(
                    from_path,
                    explicit_path,
                )

            default_root = temp_root / "default_participation"
            with mock.patch.object(
                participation_resolver,
                "RECEIVED_DERIVATIVE_PARTICIPATION_ROOT",
                Path("default_participation"),
            ), mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
                first = participation_resolver.write_received_derivative_participation_result(
                    from_path,
                )
                second = participation_resolver.write_received_derivative_participation_result(
                    from_path,
                )
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(default_root, first.parent)
            self.assertTrue(first.name.endswith("__received_derivative_participation_result.json"))
            self.assertIn("_001", second.stem)

    def test_request_shape_and_basic_refusals(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(
                participation_resolver,
                "CONTINUITY_TRANSFER_RECEIPT_ROOT",
                Path("missing_receipts"),
            ), mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
                no_receipt = participation_resolver.resolve_received_derivative_participation(
                    self.participation_request(),
                )
            self.assert_block(no_receipt, "NO_ADMISSIBLE_RECEIPT_RESULT")

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            valid_request = self.participation_request(fields=[])
            result = self.resolve_participation(
                temp_root,
                valid_request,
                stack["reference_receipt"],
            )
            self.assertEqual(valid_request, result["participation_request"])

            malformed_requests = [
                {},
                {
                    "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                    "use_class": participation_resolver.USE_CLASS_READ,
                    "participation_basis": "basis",
                    "requested_participation_fields": [],
                    "participating_surface_label": "surface",
                },
                {
                    "received_derivative_participation_request_id": "x",
                    "use_class": participation_resolver.USE_CLASS_READ,
                    "participation_basis": "basis",
                    "requested_participation_fields": [],
                    "participating_surface_label": "surface",
                },
                {
                    "received_derivative_participation_request_id": "x",
                    "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                    "participation_basis": "basis",
                    "requested_participation_fields": [],
                    "participating_surface_label": "surface",
                },
                {
                    "received_derivative_participation_request_id": "x",
                    "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                    "use_class": participation_resolver.USE_CLASS_READ,
                    "requested_participation_fields": [],
                    "participating_surface_label": "surface",
                },
                {
                    "received_derivative_participation_request_id": "x",
                    "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                    "use_class": participation_resolver.USE_CLASS_READ,
                    "participation_basis": "basis",
                    "requested_participation_fields": "non_claims",
                    "participating_surface_label": "surface",
                },
                {
                    "received_derivative_participation_request_id": "x",
                    "participant_class": participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                    "use_class": participation_resolver.USE_CLASS_READ,
                    "participation_basis": "basis",
                    "requested_participation_fields": [],
                },
            ]
            for request in malformed_requests:
                with self.subTest(request=request):
                    with self.assertRaises(
                        participation_resolver.ReceivedDerivativeParticipationError,
                    ):
                        self.resolve_participation(
                            temp_root,
                            request,
                            stack["reference_receipt"],
                        )

            unsupported_participant = self.participation_request("REMOTE_ACTOR")
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    unsupported_participant,
                    stack["reference_receipt"],
                ),
                "PARTICIPANT_CLASS_OUT_OF_SCOPE",
            )

            unsupported_use = self.participation_request(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                "AUTHORITY_PARTICIPATION",
            )
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    unsupported_use,
                    stack["reference_receipt"],
                ),
                "USE_CLASS_OUT_OF_SCOPE",
            )

            blocked_receipt = copied(stack["reference_receipt"])
            blocked_receipt["outcome"] = receipt_resolver.OUTCOME_REFUSED
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    blocked_receipt,
                ),
                "SELECTED_RECEIPT_RESULT_BLOCKED",
            )

            pending_receipt = copied(stack["reference_receipt"])
            pending_receipt["outcome"] = "PENDING"
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    pending_receipt,
                ),
                "SELECTED_RECEIPT_RESULT_NOT_RECEIVED",
            )

            out_of_scope = {"outcome": receipt_resolver.OUTCOME_RECEIVED}
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    out_of_scope,
                ),
                "SELECTED_RECEIPT_RESULT_OUT_OF_SCOPE",
            )

    def test_refuses_payload_scope_invariants_and_effective_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            out_of_scope_request = self.participation_request(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_DERIVATION,
                participation_resolver.USE_CLASS_DERIVATIVE,
                ["hidden_participation_field"],
            )
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    out_of_scope_request,
                    stack["derivative_receipt"],
                ),
                "PARTICIPATION_PAYLOAD_OUT_OF_SCOPE",
            )

            reader_derivative_request = self.participation_request(
                participation_resolver.PARTICIPANT_CLASS_LOCAL_READER,
                participation_resolver.USE_CLASS_DERIVATIVE,
                DERIVATIVE_FIELDS,
            )
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    reader_derivative_request,
                    stack["derivative_receipt"],
                ),
                "PARTICIPATION_PAYLOAD_OUT_OF_SCOPE",
            )

            missing_derivative_status = copied(stack["reference_receipt"])
            missing_derivative_status["received_payload"][
                "payload_receipt_status"
            ] = "received_source_payload"
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    missing_derivative_status,
                ),
                "RECEIVED_PAYLOAD_MISSING_DERIVATIVE_STATUS",
            )

            source_not_preserved = copied(stack["reference_receipt"])
            source_not_preserved["received_payload"]["source_remains_source"] = False
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    source_not_preserved,
                ),
                "SOURCE_REMAINS_SOURCE_NOT_TRUE",
            )

            derivative_not_preserved = copied(stack["reference_receipt"])
            derivative_not_preserved["received_payload"][
                "carried_derivative_remains_derivative"
            ] = False
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    derivative_not_preserved,
                ),
                "CARRIED_DERIVATIVE_REMAINS_DERIVATIVE_NOT_TRUE",
            )

            missing_transfer_identity = copied(stack["reference_receipt"])
            missing_transfer_identity["selected_transfer_result"][
                "selected_transfer_result_id"
            ] = ""
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    missing_transfer_identity,
                ),
                "SELECTED_TRANSFER_RESULT_IDENTITY_MISSING",
            )

            missing_source_identity = copied(stack["reference_receipt"])
            missing_source_identity["selected_source_surface"][
                "selected_source_surface_id"
            ] = None
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    missing_source_identity,
                ),
                "SELECTED_SOURCE_SURFACE_IDENTITY_MISSING",
            )

            missing_effective_path = copied(stack["reference_receipt"])
            references = missing_effective_path["selected_source_surface"][
                "selected_source_surface_effective_references"
            ]
            references["effective_authority_artifact_path"] = (
                "artifacts/missing_authority.json"
            )
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    missing_effective_path,
                ),
                "EFFECTIVE_REFERENCE_INCOHERENCE",
            )

            bad_family = read_json(stack["family_path"])
            bad_family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_canonical_core.py"
            )
            bad_family_path = temp_root / "artifacts" / "bad_family.json"
            write_json(bad_family_path, bad_family)
            mismatch = copied(stack["reference_receipt"])
            mismatch["selected_source_surface"][
                "selected_source_surface_effective_references"
            ]["effective_family_packet_path"] = display_path(temp_root, bad_family_path)
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    mismatch,
                ),
                "CANONICAL_EXECUTION_LINE_MISMATCH",
            )

    def test_refuses_shortcuts_non_claims_touch_conflict_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            shortcut_cases = [
                ("replay into live host", "REPLAY_SHORTCUT_REFUSED"),
                ("merge into local state", "MERGE_SHORTCUT_REFUSED"),
                (
                    "complete continuity through participation",
                    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
                ),
                ("perform a standing upgrade", "SILENT_STANDING_UPGRADE_REFUSED"),
                (
                    "use stale prior-family fallback",
                    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
                ),
                (
                    "infer from latest receipt file",
                    "LATEST_FILE_INFERENCE_REFUSED",
                ),
                ("mutate prior source artifacts", "IMPLICIT_MUTATION_REFUSED"),
                ("claim final governance authority", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
                ("replace source with participated derivative", "SOURCE_REPLACEMENT_REFUSED"),
                (
                    "collapse source and derivative distinction",
                    "SOURCE_DERIVATIVE_COLLAPSE_REFUSED",
                ),
            ]
            for basis, expected_code in shortcut_cases:
                with self.subTest(basis=basis):
                    request = self.participation_request(basis=basis)
                    self.assert_block(
                        self.resolve_participation(
                            temp_root,
                            request,
                            stack["reference_receipt"],
                        ),
                        expected_code,
                    )

            non_claim_cases = [
                ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
                ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
                ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
                ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
                ("source_replaced", "SOURCE_REPLACEMENT_REFUSED"),
                ("final_governance_claimed", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
            ]
            for claim_name, expected_code in non_claim_cases:
                with self.subTest(claim_name=claim_name):
                    mutated = copied(stack["reference_receipt"])
                    mutated["non_claims"][claim_name] = True
                    self.assert_block(
                        self.resolve_participation(
                            temp_root,
                            self.participation_request(),
                            mutated,
                        ),
                        expected_code,
                    )

            missing_touch = copied(stack["reference_receipt"])
            missing_touch["touch_permission_reference"][
                "touch_permission_result_path"
            ] = "artifacts/missing_touch_permission.json"
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    missing_touch,
                ),
                "TOUCH_PERMISSION_LINEAGE_INCOHERENT",
            )

            with mock.patch.object(
                participation_resolver,
                "CONTINUITY_TRANSFER_RECEIPT_ROOT",
                Path("artifacts/receipts"),
            ), mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
                conflict = participation_resolver.resolve_received_derivative_participation(
                    self.participation_request(),
                )
            self.assert_block(conflict, "MULTIPLE_RECEIPT_RESULTS_CONFLICT_UNRESOLVED")

            before = {
                "source": tree_digest(stack["source"]["root"]),
                "ingress": tree_digest(stack["ingress"]["root"]),
                "comparison": tree_digest(stack["comparison"]["root"]),
                "artifacts": tree_digest(temp_root / "artifacts"),
            }
            first = self.resolve_participation(
                temp_root,
                self.participation_request(),
                stack["reference_receipt"],
            )
            second = self.resolve_participation(
                temp_root,
                self.participation_request(),
                stack["reference_receipt"],
            )
            self.assert_participated(first)
            self.assert_participated(second)
            after = {
                "source": tree_digest(stack["source"]["root"]),
                "ingress": tree_digest(stack["ingress"]["root"]),
                "comparison": tree_digest(stack["comparison"]["root"]),
                "artifacts": tree_digest(temp_root / "artifacts"),
            }
            self.assertEqual(before, after)

    def test_hard_malformed_failures(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            root_file = temp_root / "not_a_directory.json"
            root_file.write_text("{}", encoding="utf-8")
            with mock.patch.object(
                participation_resolver,
                "CONTINUITY_TRANSFER_RECEIPT_ROOT",
                Path(root_file.name),
            ), mock.patch.object(participation_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    participation_resolver.ReceivedDerivativeParticipationError,
                ):
                    participation_resolver.resolve_received_derivative_participation(
                        self.participation_request(),
                    )

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            malformed_json_path = temp_root / "malformed_receipt.json"
            malformed_json_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(
                participation_resolver.ReceivedDerivativeParticipationError,
            ):
                with mock.patch.object(
                    participation_resolver,
                    "_repo_root",
                    return_value=temp_root,
                ):
                    participation_resolver.resolve_received_derivative_participation_from_path(
                        malformed_json_path,
                        self.participation_request(),
                    )

            malformed_receipt = copied(stack["reference_receipt"])
            malformed_receipt["continuity_transfer_receipt_metadata"] = "not-object"
            with self.assertRaises(
                participation_resolver.ReceivedDerivativeParticipationError,
            ):
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    malformed_receipt,
                )

            malformed_lineage = copied(stack["reference_receipt"])
            malformed_lineage["selected_transfer_result"] = "not-object"
            with self.assertRaises(
                participation_resolver.ReceivedDerivativeParticipationError,
            ):
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    malformed_lineage,
                )

            malformed_effective_refs = copied(stack["reference_receipt"])
            malformed_effective_refs["selected_source_surface"][
                "selected_source_surface_effective_references"
            ] = "not-object"
            self.assert_block(
                self.resolve_participation(
                    temp_root,
                    self.participation_request(),
                    malformed_effective_refs,
                ),
                "SELECTED_SOURCE_SURFACE_IDENTITY_MISSING",
            )

            malformed_request = self.participation_request()
            malformed_request["received_derivative_participation_request_id"] = ""
            with self.assertRaises(
                participation_resolver.ReceivedDerivativeParticipationError,
            ):
                self.resolve_participation(
                    temp_root,
                    malformed_request,
                    stack["reference_receipt"],
                )


if __name__ == "__main__":
    unittest.main()
