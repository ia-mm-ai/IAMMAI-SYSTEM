"""Bounded tests for the v0-min continuity-transfer-receipt resolver.

This suite exercises the receiving-side seam bridge now implemented in
``resolve_integrity_host_v0_min_coexistence_continuity_transfer_receipt``.
It builds real local upstream artifacts, then verifies that receipt remains an
additive validation/acceptance surface over a transferred derivative. It does
not test replay, merge, registry, persistence, final governance, or continuity
completion behavior.
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
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner


REQUIRED_REFERENCE_AND_SPEC_PATHS = (
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
)

TOP_LEVEL = {
    "continuity_transfer_receipt_metadata",
    "selected_transfer_result",
    "selected_source_surface",
    "touch_permission_reference",
    "receipt_request",
    "checks",
    "outcome",
    "block",
    "received_payload",
    "receipt_summary",
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
VALIDATION_FIELDS = [
    "selected_transfer_result_id",
    "selected_transfer_result_type",
    "selected_transfer_result_outcome",
    "transfer_class",
    "transfer_basis",
    "selected_source_surface_id",
    "selected_source_surface_family",
    "selected_source_surface_outcome",
    "payload_derivative_status",
    "source_remains_source",
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


def resolve_object(value: Any, temp_root: Path) -> Any:
    if isinstance(value, dict):
        return {key: resolve_object(item, temp_root) for key, item in value.items()}
    if isinstance(value, list):
        return [resolve_object(item, temp_root) for item in value]
    if isinstance(value, str):
        candidate = temp_root / value
        if candidate.exists():
            return candidate
        if value.endswith(".json") or "/" in value:
            return candidate
    return value


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


class ContinuityTransferReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        for relative_path in REQUIRED_REFERENCE_AND_SPEC_PATHS:
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
            "transition_proposal_id": "proposal_accepted_for_receipt",
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
            "proposal_basis_ref": "bounded explicit continuity-receipt test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_"
                "continuity_transfer_receipt.py"
            ),
        }

    def query_request(self, fields: list[str] | None = None) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_receipt",
            "query_target": "answer_read_output",
            "requested_fields": list(fields if fields is not None else QUERY_FIELDS),
            "query_basis": "bounded receipt test query over emitted answer surface",
        }

    def stand_request(
        self,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "unit_test_what_stands_now",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(fields if fields is not None else STAND_FIELDS),
            "query_basis": "bounded receipt test stand query over emitted answer surface",
        }

    def open_request(
        self,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "unit_test_what_remains_open",
            "query_family": "what_remains_open",
            "requested_open_fields": list(fields if fields is not None else OPEN_FIELDS),
            "query_basis": "bounded receipt test open-surface question",
        }

    def touch_request(
        self,
        touch_class: str,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded receipt test touch basis",
    ) -> dict[str, Any]:
        return {
            "touch_request_id": f"unit_test_touch_{touch_class.lower()}",
            "requested_touch_class": touch_class,
            "requested_touch_basis": basis,
            "requesting_surface_label": "unit_test_touch_surface",
            "intended_downstream_use": "bounded continuity transfer test",
            "requested_touch_fields": list(fields if fields is not None else []),
        }

    def transfer_request(
        self,
        transfer_class: str = transfer_resolver.TRANSFER_CLASS_REFERENCE,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded receipt test transfer basis",
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
        basis: str = "bounded receipt validation",
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

    def build_stack(
        self,
        temp_root: Path,
        *,
        write_transfer_artifacts: bool = True,
    ) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260422T010000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260422T010001_000000Z")
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
        self.assertEqual(
            reresolution["outcome"],
            reresolver.OUTCOME_SUCCESSOR_EMITTED,
        )

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

        self.assertEqual(
            touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            read_touch["outcome"],
        )
        self.assertEqual(
            touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
            derivation_touch["outcome"],
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
            reference_transfer_path = None
            derivative_transfer_path = None
            if write_transfer_artifacts:
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
            "source_one": source_one,
            "ingress_one": ingress_one,
            "comparison_one": comparison_one,
            "source_two": source_two,
            "ingress_two": ingress_two,
            "comparison_two": comparison_two,
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
            "transfer_root": transfer_root,
            "reference_transfer": reference_transfer,
            "reference_transfer_path": reference_transfer_path,
            "derivative_transfer": derivative_transfer,
            "derivative_transfer_path": derivative_transfer_path,
            "stands_now": stand,
            "remains_open": open_result,
        }

    def assert_top_level(self, result: Mapping[str, Any]) -> None:
        self.assertEqual(TOP_LEVEL, set(result))

    def assert_block(self, result: Mapping[str, Any], code: str) -> None:
        self.assert_top_level(result)
        self.assertEqual(receipt_resolver.OUTCOME_REFUSED, result["outcome"])
        block = result["block"]
        self.assertIsInstance(block, dict)
        self.assertEqual(code, block.get("block_code"))
        self.assertIsInstance(block.get("block_reason"), str)
        self.assertTrue(block["block_reason"])
        self.assertIsNone(result["received_payload"])

    def assert_received(self, result: Mapping[str, Any]) -> None:
        self.assert_top_level(result)
        self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, result["outcome"])
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsInstance(result["received_payload"], dict)
        self.assert_non_claims_false(result)
        checks = result["checks"]
        self.assertIsInstance(checks, list)
        self.assertGreater(len(checks), 0)
        for check in checks:
            self.assertIsInstance(check.get("check_name"), str)
            self.assertIsInstance(check.get("passed"), bool)
        self.assertTrue(all(check["passed"] for check in checks))

    def assert_non_claims_false(self, result: Mapping[str, Any]) -> None:
        non_claims = result["non_claims"]
        self.assertIsInstance(non_claims, dict)
        for claim_name, value in non_claims.items():
            if isinstance(value, bool):
                self.assertFalse(value, claim_name)
        required_false = {
            "replayed_into_live_host",
            "merged_into_local_state",
            "continuity_completed",
            "standing_upgraded",
            "final_system_identity_completed",
            "minimum_lawful_system_completed",
            "final_continuity_transfer_receipt_completed",
        }
        self.assertTrue(required_false.issubset(non_claims))
        for key in required_false:
            self.assertFalse(non_claims[key], key)

    def test_receives_validation_and_bounded_acceptance_from_real_stack(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)

            validation_request = self.receipt_request()
            validation = receipt_resolver.resolve_continuity_transfer_receipt(
                validation_request,
                stack["reference_transfer"],
            )
            self.assert_received(validation)

            metadata = validation["continuity_transfer_receipt_metadata"]
            for key in (
                "continuity_transfer_receipt_result_id",
                "continuity_transfer_receipt_result_type",
                "continuity_transfer_receipt_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assertIsInstance(metadata.get(key), str)
                self.assertTrue(metadata[key])

            selected_transfer = validation["selected_transfer_result"]
            self.assertEqual(
                stack["reference_transfer"]["continuity_transfer_metadata"][
                    "continuity_transfer_result_id"
                ],
                selected_transfer["selected_transfer_result_id"],
            )
            self.assertEqual(
                stack["reference_transfer"]["continuity_transfer_metadata"][
                    "continuity_transfer_result_type"
                ],
                selected_transfer["selected_transfer_result_type"],
            )
            self.assertEqual(
                transfer_resolver.OUTCOME_TRANSFERRED,
                selected_transfer["selected_transfer_result_outcome"],
            )
            self.assertEqual(
                transfer_resolver.TRANSFER_CLASS_REFERENCE,
                selected_transfer["transfer_class"],
            )
            self.assertTrue(selected_transfer["transfer_basis"])

            selected_source = validation["selected_source_surface"]
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

            touch_reference = validation["touch_permission_reference"]
            self.assertTrue(touch_reference["touch_permission_result_id"])
            self.assertEqual(
                touch_resolver.TOUCH_CLASS_READ_ONLY,
                touch_reference["admitted_touch_class"],
            )
            self.assertIsInstance(touch_reference["admitted_touch_scope"], dict)

            self.assertEqual(validation_request, validation["receipt_request"])
            payload = validation["received_payload"]
            self.assertEqual(
                "received_carried_derivative",
                payload["payload_receipt_status"],
            )
            self.assertTrue(payload["source_remains_source"])
            self.assertTrue(payload["carried_derivative_remains_derivative"])
            self.assertIsInstance(payload["received_fields"], dict)
            self.assertIsInstance(payload["received_references"], dict)
            for forbidden in (
                "replay_authority",
                "merge_authority",
                "continuity_completion_claim",
                "final_identity_claim",
                "source_replacement",
                "latest_file_inference",
            ):
                self.assertNotIn(forbidden, payload)

            summary = receipt_resolver.build_continuity_transfer_receipt_summary(
                validation,
            )
            self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, summary["outcome"])
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(
                selected_transfer["selected_transfer_result_id"],
                summary["selected_transfer_result_id"],
            )
            self.assertEqual(
                selected_source["selected_source_surface_id"],
                summary["selected_source_surface_id"],
            )
            self.assertEqual(
                receipt_resolver.RECEIPT_CLASS_VALIDATION,
                summary["receipt_class"],
            )
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(0, summary["failed_check_count"])
            self.assertIsInstance(summary["key_non_claims"], dict)

            acceptance_request = self.receipt_request(
                receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
                DERIVATIVE_FIELDS,
                basis="bounded acceptance of transferred derivative fields",
            )
            acceptance = receipt_resolver.resolve_continuity_transfer_receipt(
                acceptance_request,
                stack["derivative_transfer"],
            )
            self.assert_received(acceptance)
            acceptance_payload = acceptance["received_payload"]
            self.assertEqual(
                "received_carried_derivative",
                acceptance_payload["payload_receipt_status"],
            )
            self.assertTrue(acceptance_payload["source_remains_source"])
            self.assertTrue(acceptance_payload["carried_derivative_remains_derivative"])
            self.assertEqual(
                set(DERIVATIVE_FIELDS),
                set(acceptance_payload["received_fields"]),
            )
            self.assertEqual(
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                acceptance["selected_transfer_result"]["transfer_class"],
            )
            acceptance_summary = (
                receipt_resolver.build_continuity_transfer_receipt_summary(acceptance)
            )
            self.assertEqual(receipt_resolver.OUTCOME_RECEIVED, acceptance_summary["outcome"])
            self.assertEqual(0, acceptance_summary["failed_check_count"])
            self.assertEqual(
                set(DERIVATIVE_FIELDS),
                set(acceptance_summary["received_field_names"]),
            )

    def test_explicit_path_resolution_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root)
            request = self.receipt_request()

            from_object = receipt_resolver.resolve_continuity_transfer_receipt(
                request,
                stack["reference_transfer"],
            )
            from_path = receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                stack["reference_transfer_path"],
                request,
            )
            self.assert_received(from_path)
            self.assertEqual(from_object["outcome"], from_path["outcome"])
            self.assertEqual(
                from_object["selected_transfer_result"][
                    "selected_transfer_result_id"
                ],
                from_path["selected_transfer_result"]["selected_transfer_result_id"],
            )
            self.assertNotEqual(
                from_object["selected_transfer_result"][
                    "selected_transfer_result_path"
                ],
                from_path["selected_transfer_result"]["selected_transfer_result_path"],
            )

            explicit_path = temp_root / "written" / "nested" / "receipt.json"
            written = receipt_resolver.write_continuity_transfer_receipt_result(
                from_path,
                explicit_path,
            )
            self.assertEqual(explicit_path, written)
            self.assertTrue(written.is_file())
            parsed = read_json(written)
            self.assertEqual(TOP_LEVEL, set(parsed))
            with self.assertRaises(FileExistsError):
                receipt_resolver.write_continuity_transfer_receipt_result(
                    from_path,
                    explicit_path,
                )

            default_root = temp_root / "default_receipts"
            with mock.patch.object(
                receipt_resolver,
                "CONTINUITY_TRANSFER_RECEIPT_ROOT",
                Path("default_receipts"),
            ), mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                first = receipt_resolver.write_continuity_transfer_receipt_result(
                    from_path,
                )
                second = receipt_resolver.write_continuity_transfer_receipt_result(
                    from_path,
                )
            self.assertTrue(first.is_file())
            self.assertTrue(second.is_file())
            self.assertNotEqual(first, second)
            self.assertEqual(default_root, first.parent)
            self.assertTrue(first.name.endswith("__continuity_transfer_receipt_result.json"))
            self.assertIn("_001", second.stem)

    def test_request_shape_and_basic_refusals(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                no_surface = receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                )
            self.assert_block(no_surface, "NO_ADMISSIBLE_TRANSFER_RESULT")

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root, write_transfer_artifacts=False)
            valid_request = self.receipt_request(fields=[])
            result = receipt_resolver.resolve_continuity_transfer_receipt(
                valid_request,
                stack["reference_transfer"],
            )
            self.assertEqual(valid_request, result["receipt_request"])

            malformed_requests = [
                {},
                {
                    "receipt_class": receipt_resolver.RECEIPT_CLASS_VALIDATION,
                    "receipt_basis": "basis",
                    "requested_receipt_fields": [],
                    "receiving_boundary_label": "boundary",
                },
                {
                    "continuity_transfer_receipt_request_id": "x",
                    "receipt_basis": "basis",
                    "requested_receipt_fields": [],
                    "receiving_boundary_label": "boundary",
                },
                {
                    "continuity_transfer_receipt_request_id": "x",
                    "receipt_class": receipt_resolver.RECEIPT_CLASS_VALIDATION,
                    "requested_receipt_fields": [],
                    "receiving_boundary_label": "boundary",
                },
                {
                    "continuity_transfer_receipt_request_id": "x",
                    "receipt_class": receipt_resolver.RECEIPT_CLASS_VALIDATION,
                    "receipt_basis": "basis",
                    "requested_receipt_fields": "non_claims",
                    "receiving_boundary_label": "boundary",
                },
                {
                    "continuity_transfer_receipt_request_id": "x",
                    "receipt_class": receipt_resolver.RECEIPT_CLASS_VALIDATION,
                    "receipt_basis": "basis",
                    "requested_receipt_fields": [],
                },
            ]
            for request in malformed_requests:
                with self.subTest(request=request):
                    with self.assertRaises(
                        receipt_resolver.ContinuityTransferReceiptError,
                    ):
                        receipt_resolver.resolve_continuity_transfer_receipt(
                            request,
                            stack["reference_transfer"],
                        )

            unsupported_class = self.receipt_request("BROAD_CONTINUITY_RECEIPT")
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    unsupported_class,
                    stack["reference_transfer"],
                ),
                "RECEIPT_CLASS_OUT_OF_SCOPE",
            )

            blocked_transfer = copied(stack["reference_transfer"])
            blocked_transfer["outcome"] = transfer_resolver.OUTCOME_REFUSED
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    blocked_transfer,
                ),
                "SELECTED_TRANSFER_RESULT_BLOCKED",
            )

            pending_transfer = copied(stack["reference_transfer"])
            pending_transfer["outcome"] = "PENDING"
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    pending_transfer,
                ),
                "SELECTED_TRANSFER_RESULT_NOT_TRANSFERRED",
            )

            out_of_scope = {"outcome": transfer_resolver.OUTCOME_TRANSFERRED}
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    out_of_scope,
                ),
                "SELECTED_TRANSFER_RESULT_OUT_OF_SCOPE",
            )

    def test_refuses_payload_scope_derivative_status_source_identity_and_canonical(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root, write_transfer_artifacts=False)

            out_of_scope_request = self.receipt_request(
                receipt_resolver.RECEIPT_CLASS_BOUNDED_ACCEPTANCE,
                ["hidden_receipt_field"],
            )
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    out_of_scope_request,
                    stack["derivative_transfer"],
                ),
                "RECEIPT_PAYLOAD_OUT_OF_SCOPE",
            )

            missing_derivative_status = copied(stack["reference_transfer"])
            missing_derivative_status["transfer_payload"][
                "payload_derivative_status"
            ] = "source_payload"
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    missing_derivative_status,
                ),
                "TRANSFER_PAYLOAD_MISSING_DERIVATIVE_STATUS",
            )

            source_not_preserved = copied(stack["reference_transfer"])
            source_not_preserved["transfer_payload"]["source_remains_source"] = False
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    source_not_preserved,
                ),
                "SOURCE_REMAINS_SOURCE_NOT_TRUE",
            )

            missing_source_identity = copied(stack["reference_transfer"])
            missing_source_identity["selected_source_surface"][
                "selected_source_surface_id"
            ] = None
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    missing_source_identity,
                ),
                "SELECTED_SOURCE_SURFACE_IDENTITY_MISSING",
            )

            missing_effective_path = copied(stack["reference_transfer"])
            references = missing_effective_path["selected_source_surface"][
                "selected_source_surface_effective_references"
            ]
            references["effective_authority_artifact_path"] = (
                "artifacts/missing_authority.json"
            )
            with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                self.assert_block(
                    receipt_resolver.resolve_continuity_transfer_receipt(
                        self.receipt_request(),
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
            mismatch = copied(stack["reference_transfer"])
            mismatch["selected_source_surface"][
                "selected_source_surface_effective_references"
            ]["effective_family_packet_path"] = display_path(temp_root, bad_family_path)
            with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                self.assert_block(
                    receipt_resolver.resolve_continuity_transfer_receipt(
                        self.receipt_request(),
                        mismatch,
                    ),
                    "CANONICAL_EXECUTION_LINE_MISMATCH",
                )

    def test_refuses_shortcuts_and_non_claim_mutations(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root, write_transfer_artifacts=False)
            shortcut_cases = [
                ("replay into live host", "REPLAY_SHORTCUT_REFUSED"),
                ("merge into local state", "MERGE_SHORTCUT_REFUSED"),
                (
                    "complete continuity through this receipt",
                    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
                ),
                ("perform a standing upgrade", "SILENT_STANDING_UPGRADE_REFUSED"),
                (
                    "use stale prior-family fallback",
                    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
                ),
                (
                    "infer from latest authority file",
                    "LATEST_FILE_INFERENCE_REFUSED",
                ),
                ("mutate prior source artifacts", "IMPLICIT_MUTATION_REFUSED"),
                ("claim final governance authority", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
                ("replace source with received derivative", "SOURCE_REPLACEMENT_REFUSED"),
                (
                    "collapse source and derivative distinction",
                    "SOURCE_DERIVATIVE_COLLAPSE_REFUSED",
                ),
            ]
            for basis, expected_code in shortcut_cases:
                with self.subTest(basis=basis):
                    request = self.receipt_request(basis=basis)
                    self.assert_block(
                        receipt_resolver.resolve_continuity_transfer_receipt(
                            request,
                            stack["reference_transfer"],
                        ),
                        expected_code,
                    )

            non_claim_cases = [
                ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
                ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
                ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
                ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
                ("final_governance_claimed", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
            ]
            for claim_name, expected_code in non_claim_cases:
                with self.subTest(claim_name=claim_name):
                    mutated = copied(stack["reference_transfer"])
                    mutated["non_claims"][claim_name] = True
                    self.assert_block(
                        receipt_resolver.resolve_continuity_transfer_receipt(
                            self.receipt_request(),
                            mutated,
                        ),
                        expected_code,
                    )

    def test_touch_reference_conflict_and_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root, write_transfer_artifacts=True)

            missing_touch = copied(stack["reference_transfer"])
            missing_touch["touch_permission_reference"][
                "touch_permission_result_path"
            ] = "artifacts/missing_touch_permission.json"
            with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                self.assert_block(
                    receipt_resolver.resolve_continuity_transfer_receipt(
                        self.receipt_request(),
                        missing_touch,
                    ),
                    "TOUCH_PERMISSION_REFERENCE_UNREADABLE",
                )

            bad_touch_path = temp_root / "artifacts" / "bad_touch.json"
            write_json(
                bad_touch_path,
                {"outcome": touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH},
            )
            malformed_touch = copied(stack["reference_transfer"])
            malformed_touch["touch_permission_reference"][
                "touch_permission_result_path"
            ] = display_path(temp_root, bad_touch_path)
            with mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                    receipt_resolver.resolve_continuity_transfer_receipt(
                        self.receipt_request(),
                        malformed_touch,
                    )

            with mock.patch.object(
                receipt_resolver,
                "CONTINUITY_TRANSFER_UNIT_ROOT",
                Path("artifacts/transfer"),
            ), mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                conflict = receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                )
            self.assert_block(conflict, "MULTIPLE_TRANSFER_RESULTS_CONFLICT_UNRESOLVED")

            before = {
                "source": tree_digest(stack["source"]["root"]),
                "ingress": tree_digest(stack["ingress"]["root"]),
                "comparison": tree_digest(stack["comparison"]["root"]),
                "artifacts": tree_digest(temp_root / "artifacts"),
            }
            first = receipt_resolver.resolve_continuity_transfer_receipt(
                self.receipt_request(),
                stack["reference_transfer"],
            )
            second = receipt_resolver.resolve_continuity_transfer_receipt(
                self.receipt_request(),
                stack["reference_transfer"],
            )
            self.assert_received(first)
            self.assert_received(second)
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
                receipt_resolver,
                "CONTINUITY_TRANSFER_UNIT_ROOT",
                Path(root_file.name),
            ), mock.patch.object(receipt_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                    receipt_resolver.resolve_continuity_transfer_receipt(
                        self.receipt_request(),
                    )

        with tempfile.TemporaryDirectory() as tmp:
            temp_root = Path(tmp)
            stack = self.build_stack(temp_root, write_transfer_artifacts=False)

            malformed_json_path = temp_root / "malformed_transfer.json"
            malformed_json_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                receipt_resolver.resolve_continuity_transfer_receipt_from_path(
                    malformed_json_path,
                    self.receipt_request(),
                )

            malformed_transfer = copied(stack["reference_transfer"])
            malformed_transfer["continuity_transfer_metadata"] = "not-object"
            with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    malformed_transfer,
                )

            malformed_touch_reference = copied(stack["reference_transfer"])
            malformed_touch_reference["touch_permission_reference"] = "not-object"
            with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    malformed_touch_reference,
                )

            malformed_effective_refs = copied(stack["reference_transfer"])
            malformed_effective_refs["selected_source_surface"][
                "selected_source_surface_effective_references"
            ] = "not-object"
            with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    malformed_effective_refs,
                )

            impossible_correspondence = copied(stack["reference_transfer"])
            impossible_correspondence["touch_permission_reference"][
                "touch_permission_result_path"
            ] = str(Path(stack["read_touch_path"]).resolve())
            impossible_correspondence["touch_permission_reference"][
                "touch_permission_result_id"
            ] = "different_touch_permission_id"
            self.assert_block(
                receipt_resolver.resolve_continuity_transfer_receipt(
                    self.receipt_request(),
                    impossible_correspondence,
                ),
                "TOUCH_PERMISSION_REFERENCE_MALFORMED",
            )

            malformed_request = self.receipt_request()
            malformed_request["continuity_transfer_receipt_request_id"] = ""
            with self.assertRaises(receipt_resolver.ContinuityTransferReceiptError):
                receipt_resolver.resolve_continuity_transfer_receipt(
                    malformed_request,
                    stack["reference_transfer"],
                )


if __name__ == "__main__":
    unittest.main()
