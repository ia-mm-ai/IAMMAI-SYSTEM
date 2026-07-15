"""Bounded tests for the v0-min continuity-transfer-unit resolver.

The suite locks the current behavior of
``src/resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit.py``.
It emits real local source runs, ingress runs, comparison artifacts, authority,
family, status, governing, transition, re-resolution, adoption, effective-family,
current-work, current-state answer/read, current-state query, what-stands-now,
what-remains-open, and current-state touch-permission artifacts into temporary
roots where helpful.

These tests are only for the narrow continuity-transfer bridge. They do not
test replay, merge, persistence, registry, distributed continuity, CLI, broad
participation, chat/API/dashboard, reporting, workflow, or broader continuity
framework behavior.
"""

from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import build_current_integrity_host_v0_min_coexistence_governing_packet as governing_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder  # noqa: E402
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_effective_family as effective_resolver  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit as transfer_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_application as application_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_delivery as delivery_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_export as export_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_handoff as handoff_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_readout as readout_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_work_input as work_input_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_current_work_operation_v2 as operation_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_effective_family_consumption as consumption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


TOP_LEVEL = {
    "continuity_transfer_metadata",
    "selected_source_surface",
    "touch_permission_reference",
    "transfer_request",
    "checks",
    "outcome",
    "block",
    "transfer_payload",
    "transfer_summary",
    "non_claims",
}

EXPECTED_NON_CLAIMS = set(transfer_resolver.NON_CLAIM_DEFAULTS)

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


class ContinuityTransferUnitTests(unittest.TestCase):
    def build_stack(
        self,
        temp_root: Path,
        *,
        write_touch_artifacts: bool = True,
    ) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260422T010000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260422T010001_000000Z")
        ingress_two = self.emit_ingress(temp_root, source_two)
        comparison_two = self.emit_comparison(temp_root, source_two, ingress_two)

        with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
            authority = resolver.resolve_current_execution_authority()
            authority_path = resolver.write_resolution(authority)
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
        reresolution_path = self.reresolution_path(temp_root, reresolution)
        self.write_json(reresolution_path, reresolution)
        self.assertEqual(
            reresolution["outcome"],
            reresolver.OUTCOME_SUCCESSOR_EMITTED,
        )

        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            adoption = adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_path
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
            read_touch_path = (
                touch_resolver.write_current_state_touch_permission_result(read_touch)
                if write_touch_artifacts
                else None
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
                if write_touch_artifacts
                else None
            )
        self.assertEqual(read_touch["outcome"], touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH)
        self.assertEqual(
            derivation_touch["outcome"],
            touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
        )

        return {
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
            "reresolution_path": reresolution_path,
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
        }

    def emit_source(self, temp_root: Path, name: str) -> Path:
        run_dir = temp_root / resolver.SOURCE_RUNS_ROOT / name
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
            output_dir = self.display_path(
                temp_root,
                manifest["ingress_run_metadata"]["output_run_directory"],
            )
            ingress_runner.write_ingress_run_manifest(
                manifest,
                output_dir / "manifest.json",
            )
        return output_dir

    def emit_comparison(self, temp_root: Path, source_run: Path, ingress_run: Path) -> Path:
        with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
            comparison = comparer.compare_source_run_and_ingress_run(
                source_run,
                ingress_run,
            )
            path = (
                temp_root
                / resolver.SOURCE_INGRESS_COMPARISON_ROOT
                / f"{source_run.name}__source_ingress_comparison.json"
            )
            comparer.write_comparison(comparison, path)
        return path

    def valid_proposal(
        self,
        current: dict[str, Any],
        candidate: dict[str, Any],
    ) -> dict[str, str]:
        return {
            "transition_proposal_id": "proposal_accepted_for_continuity_transfer",
            "current_governing_source_run_path": current[
                "source_run_directory_path"
            ],
            "candidate_successor_source_run_path": candidate[
                "source_run_directory_path"
            ],
            "current_governing_ingress_run_path": current["matched_ingress_run_path"],
            "candidate_successor_ingress_run_path": candidate[
                "matched_ingress_run_path"
            ],
            "current_governing_comparison_artifact_path": current[
                "matched_comparison_artifact_path"
            ],
            "candidate_successor_comparison_artifact_path": candidate[
                "matched_comparison_artifact_path"
            ],
            "proposal_basis_ref": "bounded explicit continuity-transfer test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit.py"
            ),
        }

    def query_request(self) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_transfer",
            "query_target": "answer_read_output",
            "requested_fields": list(QUERY_FIELDS),
            "query_basis": "bounded current-state query artifact for transfer test",
        }

    def stand_request(self) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "stand_now_before_transfer",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(STAND_FIELDS),
            "query_basis": "bounded stand-now artifact for transfer test",
        }

    def open_request(self) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "open_surface_before_transfer",
            "query_family": "what_remains_open",
            "requested_open_fields": list(OPEN_FIELDS),
            "query_basis": "bounded what-remains-open artifact for transfer test",
        }

    def touch_request(
        self,
        touch_class: str,
        fields: list[str] | None = None,
    ) -> dict[str, Any]:
        return {
            "touch_request_id": f"touch_for_transfer_{touch_class.lower()}",
            "requested_touch_class": touch_class,
            "requested_touch_basis": "bounded touch permission for transfer test",
            "requesting_surface_label": "continuity_transfer_unit_test",
            "intended_downstream_use": "bounded continuity transfer",
            "requested_touch_fields": list(fields or []),
        }

    def transfer_request(
        self,
        transfer_class: str = transfer_resolver.TRANSFER_CLASS_REFERENCE,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded transfer across one test seam",
        target: str = "test_seam",
    ) -> dict[str, Any]:
        return {
            "continuity_transfer_request_id": f"transfer_{transfer_class.lower()}",
            "transfer_class": transfer_class,
            "transfer_basis": basis,
            "requested_transfer_fields": list(fields or []),
            "target_seam_label": target,
        }

    def resolve_object(
        self,
        temp_root: Path,
        request: dict[str, Any],
        source: dict[str, Any] | None = None,
        touch: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
            return transfer_resolver.resolve_continuity_transfer_unit(
                request,
                source,
                touch,
            )

    def resolve_path(
        self,
        temp_root: Path,
        source_path: Path,
        request: dict[str, Any],
        touch_path: Path | None = None,
    ) -> dict[str, Any]:
        with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
            return transfer_resolver.resolve_continuity_transfer_unit_from_path(
                source_path,
                request,
                touch_path,
            )

    def reresolution_path(self, temp_root: Path, result: dict[str, Any]) -> Path:
        run_dir = self.display_path(
            temp_root,
            result["input_references"]["reresolution_run_directory_path"],
        )
        candidates = sorted(run_dir.glob("*_result.json"))
        self.assertEqual(len(candidates), 1)
        return candidates[0]

    def read_json(self, path: Path) -> dict[str, Any]:
        payload = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(payload, dict)
        return payload

    def write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        return path

    def copy(self, payload: Any) -> Any:
        return json.loads(json.dumps(payload, sort_keys=True))

    def display_path(self, repo_root: Path, value: str | Path) -> Path:
        path = Path(value)
        if path.is_absolute():
            return path.resolve()
        return (repo_root / path).resolve()

    def tree_digest(self, root: Path) -> str:
        digest = hashlib.sha256()
        if not root.exists():
            return "missing"
        for path in sorted(root.rglob("*")):
            if path.is_file():
                digest.update(str(path.relative_to(root)).encode("utf-8"))
                digest.update(path.read_bytes())
        return digest.hexdigest()

    def assert_non_empty(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), TOP_LEVEL)
        self.assertIsInstance(result["continuity_transfer_metadata"], dict)
        self.assertIsInstance(result["selected_source_surface"], dict)
        self.assertIsInstance(result["touch_permission_reference"], dict)
        self.assertIsInstance(result["transfer_request"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertTrue(
            result["transfer_payload"] is None
            or isinstance(result["transfer_payload"], dict)
        )
        self.assertTrue(
            result["transfer_summary"] is None
            or isinstance(result["transfer_summary"], dict)
        )
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key], key)

    def assert_checks(self, result: dict[str, Any], *, all_pass: bool) -> None:
        self.assertGreater(len(result["checks"]), 0)
        for check in result["checks"]:
            self.assertIn("check_name", check)
            self.assertIn("passed", check)
            self.assertIsInstance(check["check_name"], str)
            self.assertIsInstance(check["passed"], bool)
            if "expected_posture" in check:
                self.assertIsNotNone(check["expected_posture"])
            if "actual_posture" in check:
                self.assertIsNotNone(check["actual_posture"])
        if all_pass:
            self.assertTrue(all(check["passed"] is True for check in result["checks"]))

    def assert_transferred(
        self,
        result: dict[str, Any],
        transfer_class: str,
    ) -> None:
        self.assert_shape(result)
        self.assertEqual(result["outcome"], transfer_resolver.OUTCOME_TRANSFERRED)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(result["transfer_request"]["transfer_class"], transfer_class)
        self.assertIsInstance(result["transfer_payload"], dict)
        self.assertEqual(
            result["transfer_payload"]["payload_derivative_status"],
            "carried_derivative",
        )
        self.assertTrue(result["transfer_payload"]["source_remains_source"])
        self.assertIsInstance(result["transfer_payload"]["carried_fields"], dict)
        self.assertIsInstance(result["transfer_payload"]["carried_references"], dict)
        self.assert_non_claims_false(result)
        self.assert_checks(result, all_pass=True)

    def assert_refused(
        self,
        result: dict[str, Any],
        code: str | None = None,
        *,
        expect_false_non_claims: bool = True,
    ) -> None:
        self.assert_shape(result)
        self.assertEqual(result["outcome"], transfer_resolver.OUTCOME_REFUSED)
        if code is not None:
            self.assertEqual(result["block"]["block_code"], code)
        self.assert_non_empty(result["block"]["block_reason"])
        self.assertIsNone(result["transfer_payload"])
        self.assert_checks(result, all_pass=False)
        if expect_false_non_claims:
            self.assert_non_claims_false(result)

    def assert_summary(self, result: dict[str, Any], transfer_class: str) -> None:
        summary = transfer_resolver.build_continuity_transfer_unit_summary(result)
        for key in (
            "continuity_transfer_result_id",
            "outcome",
            "block_code",
            "block_reason",
            "selected_source_surface_id",
            "selected_source_surface_family",
            "transfer_class",
            "transferred_field_names",
            "passed_check_count",
            "failed_check_count",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(summary["outcome"], transfer_resolver.OUTCOME_TRANSFERRED)
        self.assertEqual(summary["transfer_class"], transfer_class)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in transfer_resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertFalse(summary["key_non_claims"][key])

    def retarget_effective_reference(
        self,
        source: dict[str, Any],
        touch: dict[str, Any],
        key: str,
        value: str,
    ) -> None:
        source["effective_open_inputs"][key] = value
        touch["selected_current_state_surface"][
            "selected_surface_effective_references"
        ][key] = value

    def test_transfers_reference_and_derivative_from_real_stack(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            reference_request = self.transfer_request()
            reference_result = self.resolve_object(
                temp_root,
                reference_request,
                stack["open"],
                stack["read_touch"],
            )
            self.assert_transferred(
                reference_result,
                transfer_resolver.TRANSFER_CLASS_REFERENCE,
            )
            self.assertEqual(reference_result["transfer_request"], reference_request)
            for key in (
                "continuity_transfer_result_id",
                "continuity_transfer_result_type",
                "continuity_transfer_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty(
                    reference_result["continuity_transfer_metadata"][key]
                )
            self.assertEqual(
                reference_result["selected_source_surface"][
                    "selected_source_surface_family"
                ],
                "what_remains_open",
            )
            self.assertEqual(
                reference_result["selected_source_surface"][
                    "selected_source_surface_outcome"
                ],
                open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            )
            self.assertIsInstance(
                reference_result["selected_source_surface"][
                    "selected_source_surface_effective_references"
                ],
                dict,
            )
            self.assertEqual(
                reference_result["touch_permission_reference"][
                    "touch_permission_result_id"
                ],
                stack["read_touch"]["touch_permission_metadata"][
                    "touch_permission_result_id"
                ],
            )
            self.assertEqual(
                reference_result["touch_permission_reference"][
                    "admitted_touch_class"
                ],
                touch_resolver.TOUCH_CLASS_READ_ONLY,
            )
            self.assertIsInstance(
                reference_result["touch_permission_reference"][
                    "admitted_touch_scope"
                ],
                dict,
            )
            carried = reference_result["transfer_payload"]["carried_fields"]
            self.assertEqual(
                set(carried),
                set(transfer_resolver.REFERENCE_DEFAULT_FIELDS),
            )
            for forbidden in (
                "replay_authority",
                "merge_authority",
                "continuity_completion_claim",
                "final_identity_claim",
                "source_replacement",
                "latest_file_inference",
            ):
                self.assertNotIn(forbidden, carried)
            self.assert_summary(
                reference_result,
                transfer_resolver.TRANSFER_CLASS_REFERENCE,
            )

            derivative_request = self.transfer_request(
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                DERIVATIVE_FIELDS,
            )
            derivative_result = self.resolve_object(
                temp_root,
                derivative_request,
                stack["open"],
                stack["derivation_touch"],
            )
            self.assert_transferred(
                derivative_result,
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
            )
            derivative_payload = derivative_result["transfer_payload"]
            self.assertEqual(
                set(derivative_payload["carried_fields"]),
                set(DERIVATIVE_FIELDS),
            )
            carried_non_claims = derivative_payload["carried_fields"]["non_claims"]
            self.assertIsInstance(carried_non_claims, dict)
            for key, value in carried_non_claims.items():
                self.assertIn(key, derivative_result["non_claims"])
                self.assertEqual(value, derivative_result["non_claims"][key])
            self.assertFalse(derivative_payload["carried_fields"]["continuity_completed"])
            self.assertFalse(derivative_payload["carried_fields"]["standing_upgraded"])
            self.assert_summary(
                derivative_result,
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
            )

    def test_explicit_path_resolution_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            request = self.transfer_request(
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                DERIVATIVE_FIELDS,
            )

            object_result = self.resolve_object(
                temp_root,
                request,
                stack["open"],
                stack["derivation_touch"],
            )
            path_result = self.resolve_path(
                temp_root,
                stack["open_path"],
                request,
                stack["derivation_touch_path"],
            )
            self.assert_transferred(
                path_result,
                transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
            )
            self.assertEqual(
                object_result["selected_source_surface"][
                    "selected_source_surface_id"
                ],
                path_result["selected_source_surface"][
                    "selected_source_surface_id"
                ],
            )
            self.assertEqual(
                object_result["touch_permission_reference"][
                    "touch_permission_result_id"
                ],
                path_result["touch_permission_reference"][
                    "touch_permission_result_id"
                ],
            )
            self.assertEqual(
                object_result["transfer_summary"]["transferred_field_names"],
                path_result["transfer_summary"]["transferred_field_names"],
            )

            output_path = temp_root / "nested" / "transfer" / "result.json"
            with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
                written = transfer_resolver.write_continuity_transfer_unit_result(
                    path_result,
                    output_path,
                )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            self.assertEqual(set(self.read_json(written)), TOP_LEVEL)

            with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(FileExistsError):
                    transfer_resolver.write_continuity_transfer_unit_result(
                        path_result,
                        output_path,
                    )
                first = transfer_resolver.write_continuity_transfer_unit_result(
                    path_result
                )
                second = transfer_resolver.write_continuity_transfer_unit_result(
                    path_result
                )
            root = (temp_root / transfer_resolver.CONTINUITY_TRANSFER_UNIT_ROOT).resolve()
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(first.resolve().is_relative_to(root))
            self.assertTrue(second.resolve().is_relative_to(root))
            self.assertTrue(first.name.endswith("__continuity_transfer_unit_result.json"))
            self.assertTrue(
                second.name.endswith("__continuity_transfer_unit_result_001.json")
            )

    def test_request_shape_and_refusal_for_unsupported_sources(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            result = self.resolve_object(temp_root, self.transfer_request())
            self.assert_refused(result, "NO_ADMISSIBLE_SOURCE_SURFACE")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            for missing in (
                "continuity_transfer_request_id",
                "transfer_class",
                "transfer_basis",
                "requested_transfer_fields",
                "target_seam_label",
            ):
                malformed = self.transfer_request()
                malformed.pop(missing)
                with self.subTest(missing=missing):
                    with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                        self.resolve_object(
                            temp_root,
                            malformed,
                            stack["open"],
                            stack["read_touch"],
                        )

            malformed_fields = self.transfer_request()
            malformed_fields["requested_transfer_fields"] = "not-a-list"
            with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                self.resolve_object(
                    temp_root,
                    malformed_fields,
                    stack["open"],
                    stack["read_touch"],
                )

            blocked = self.copy(stack["open"])
            blocked["outcome"] = "BLOCKED"
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.transfer_request(),
                    blocked,
                    stack["read_touch"],
                ),
                "SELECTED_SOURCE_SURFACE_BLOCKED",
            )

            pending = self.copy(stack["open"])
            pending["outcome"] = "PENDING"
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.transfer_request(),
                    pending,
                    stack["read_touch"],
                ),
                "SELECTED_SOURCE_SURFACE_NOT_SUCCESSFUL",
            )

            unsupported = {"outcome": "ANSWERED", "unknown_metadata": {}}
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.transfer_request(),
                    unsupported,
                    stack["read_touch"],
                ),
                "SELECTED_SOURCE_SURFACE_OUT_OF_SCOPE",
            )

            class_refusal = self.resolve_object(
                temp_root,
                self.transfer_request("WIDE_TRANSFER"),
                stack["open"],
                stack["read_touch"],
            )
            self.assert_refused(class_refusal)
            self.assertIn(
                class_refusal["block"]["block_code"],
                {"TRANSFER_CLASS_OUT_OF_SCOPE", "TRANSFER_PAYLOAD_OUT_OF_SCOPE"},
            )

    def test_refuses_missing_malformed_or_mismatched_touch_permission(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_touch_artifacts=False)

            no_touch = self.resolve_object(
                temp_root,
                self.transfer_request(),
                stack["open"],
            )
            self.assert_refused(no_touch, "NO_SUCCESSFUL_TOUCH_PERMISSION_FOR_TRANSFER")

            with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                self.resolve_object(
                    temp_root,
                    self.transfer_request(),
                    stack["open"],
                    {"outcome": touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH},
                )

            mismatched_touch = self.copy(stack["read_touch"])
            mismatched_touch["selected_current_state_surface"][
                "selected_surface_id"
            ] = "different_surface_id"
            mismatch = self.resolve_object(
                temp_root,
                self.transfer_request(),
                stack["open"],
                mismatched_touch,
            )
            self.assert_refused(
                mismatch,
                "TOUCH_PERMISSION_DOES_NOT_CORRESPOND_TO_SOURCE_SURFACE",
            )

            unreadable_path = self.resolve_path(
                temp_root,
                stack["open_path"],
                self.transfer_request(),
                temp_root / "missing_touch_permission.json",
            )
            self.assert_refused(unreadable_path, "TOUCH_PERMISSION_UNREADABLE")

            bad_touch_path = self.write_json(
                temp_root / "bad_touch_permission.json",
                {"outcome": touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH},
            )
            with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                self.resolve_path(
                    temp_root,
                    stack["open_path"],
                    self.transfer_request(),
                    bad_touch_path,
                )

    def test_refuses_payload_scope_effective_reference_and_canonical_mismatch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            out_of_scope = self.resolve_object(
                temp_root,
                self.transfer_request(
                    transfer_resolver.TRANSFER_CLASS_DERIVATIVE,
                    ["hidden_unexposed_transfer_field"],
                ),
                stack["open"],
                stack["derivation_touch"],
            )
            self.assert_refused(out_of_scope, "TRANSFER_PAYLOAD_OUT_OF_SCOPE")

            missing_source = self.copy(stack["open"])
            missing_touch = self.copy(stack["read_touch"])
            self.retarget_effective_reference(
                missing_source,
                missing_touch,
                "effective_authority_artifact_path",
                "artifacts/missing_authority_for_transfer.json",
            )
            missing_result = self.resolve_object(
                temp_root,
                self.transfer_request(),
                missing_source,
                missing_touch,
            )
            self.assert_refused(missing_result, "EFFECTIVE_REFERENCE_INCOHERENCE")

            bad_family = self.copy(stack["family"])
            bad_family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            bad_family_path = self.write_json(
                temp_root / "bad_effective_family_packet.json",
                bad_family,
            )
            bad_source = self.copy(stack["open"])
            bad_touch = self.copy(stack["read_touch"])
            self.retarget_effective_reference(
                bad_source,
                bad_touch,
                "effective_family_packet_path",
                str(bad_family_path),
            )
            canonical_result = self.resolve_object(
                temp_root,
                self.transfer_request(),
                bad_source,
                bad_touch,
            )
            self.assert_refused(canonical_result, "CANONICAL_EXECUTION_LINE_MISMATCH")

    def test_refuses_shortcuts_non_claim_mutations_and_source_collapse(self) -> None:
        shortcut_cases = (
            ("allow replay into live host", "REPLAY_SHORTCUT_REFUSED"),
            ("merge into local state", "MERGE_SHORTCUT_REFUSED"),
            ("complete continuity with this transfer", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("perform standing upgrade", "SILENT_STANDING_UPGRADE_REFUSED"),
            ("fallback to prior-family fallback", "STALE_PRIOR_FAMILY_FALLBACK_REFUSED"),
            ("use latest authority artifact", "LATEST_FILE_INFERENCE_REFUSED"),
            ("mutate prior artifacts", "IMPLICIT_MUTATION_REFUSED"),
            ("claim final governance and protocol law", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
            ("replace source with carried derivative", "SOURCE_REPLACEMENT_REFUSED"),
            ("collapse source derivative distinction", "SOURCE_DERIVATIVE_COLLAPSE_REFUSED"),
        )
        for basis, code in shortcut_cases:
            with self.subTest(code=code):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(temp_root)
                    result = self.resolve_object(
                        temp_root,
                        self.transfer_request(basis=basis),
                        stack["open"],
                        stack["read_touch"],
                    )
                    self.assert_refused(result, code)

        for non_claim_key, code in (
            ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
            ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
            ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
            ("final_continuity_transfer_completed", "IMPLICIT_AUTHORITY_CLAIM_REFUSED"),
        ):
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(temp_root)
                    source = self.copy(stack["open"])
                    touch = self.copy(stack["read_touch"])
                    source["non_claims"][non_claim_key] = True
                    touch["non_claims"][non_claim_key] = True
                    result = self.resolve_object(
                        temp_root,
                        self.transfer_request(),
                        source,
                        touch,
                    )
                    self.assert_refused(
                        result,
                        code,
                        expect_false_non_claims=False,
                    )
                    self.assertTrue(result["non_claims"][non_claim_key])

    def test_multiple_source_conflict_and_non_mutation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            before = self.tree_digest(temp_root)
            first = self.resolve_object(
                temp_root,
                self.transfer_request(),
                stack["open"],
                stack["read_touch"],
            )
            second = self.resolve_object(
                temp_root,
                self.transfer_request(),
                stack["open"],
                stack["read_touch"],
            )
            after = self.tree_digest(temp_root)
            self.assert_transferred(first, transfer_resolver.TRANSFER_CLASS_REFERENCE)
            self.assert_transferred(second, transfer_resolver.TRANSFER_CLASS_REFERENCE)
            self.assertEqual(before, after)

            conflict = self.copy(stack["open"])
            conflict["what_remains_open_metadata"][
                "what_remains_open_result_id"
            ] = "conflicting_open_surface_for_transfer"
            conflict["effective_open_inputs"][
                "effective_source_run_path"
            ] = "artifacts/conflicting_source_run"
            conflict_path = (
                temp_root
                / open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
                / "conflicting_open_surface_for_transfer.json"
            )
            self.write_json(conflict_path, conflict)

            default_result = self.resolve_object(temp_root, self.transfer_request())
            self.assert_refused(
                default_result,
                "MULTIPLE_SOURCE_SURFACES_CONFLICT_UNRESOLVED",
            )

    def test_hard_malformed_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            not_a_dir = self.write_json(temp_root / "not_a_surface_root.json", {})
            first = transfer_resolver.SURFACE_DEFINITIONS[0]
            bad_definition = transfer_resolver._SurfaceDefinition(  # noqa: SLF001
                first.result_family,
                Path(not_a_dir.name),
                first.metadata_key,
                first.id_key,
                first.type_key,
                first.expected_outcome,
                first.effective_inputs_key,
                first.summary_key,
                first.payload_key,
                first.selected_key,
            )
            with mock.patch.object(transfer_resolver, "_repo_root", return_value=temp_root):
                with mock.patch.object(
                    transfer_resolver,
                    "SURFACE_DEFINITIONS",
                    (bad_definition,),
                ):
                    with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                        transfer_resolver.resolve_continuity_transfer_unit(
                            self.transfer_request()
                        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            malformed_source = temp_root / "malformed_source.json"
            malformed_source.write_text("{not-json", encoding="utf-8")
            with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                self.resolve_path(temp_root, malformed_source, self.transfer_request())

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            malformed = self.copy(stack["open"])
            malformed["effective_open_inputs"] = "not-an-object"
            with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
                self.resolve_object(
                    temp_root,
                    self.transfer_request(),
                    malformed,
                    stack["read_touch"],
                )

        with self.assertRaises(transfer_resolver.ContinuityTransferUnitError):
            transfer_resolver.resolve_continuity_transfer_unit(
                {
                    "continuity_transfer_request_id": "",
                    "transfer_class": transfer_resolver.TRANSFER_CLASS_REFERENCE,
                    "transfer_basis": "bounded",
                    "requested_transfer_fields": [],
                    "target_seam_label": "test",
                }
            )


if __name__ == "__main__":
    unittest.main()
