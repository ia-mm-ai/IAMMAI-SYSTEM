"""Bounded tests for current-state admissibility and touch-permission.

The suite locks the current behavior of
``src/resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission.py``.
It emits real local source runs, ingress runs, comparison artifacts, authority,
family, status, governing, transition, re-resolution, adoption, effective-family,
current-work, current-state answer/read, current-state query, what-stands-now,
and what-remains-open artifacts into temporary roots.

These tests are only for the narrow current-state admissibility / touch bridge.
They do not test replay, merge, persistence, registry, distributed continuity,
CLI, broad participation, chat/API/dashboard, reporting, or workflow behavior.
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
    "touch_permission_metadata",
    "selected_current_state_surface",
    "touch_request",
    "checks",
    "outcome",
    "block",
    "admitted_touch_scope",
    "non_claims",
}

EXPECTED_NON_CLAIMS = set(touch_resolver.NON_CLAIM_DEFAULTS)

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


class CurrentStateAdmissibilityTouchPermissionTests(unittest.TestCase):
    def build_stack(self, temp_root: Path) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260422T000000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260422T000001_000000Z")
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
            "current_entry": current_entry,
            "candidate_entry": candidates[0],
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
            "transition_proposal_id": "proposal_accepted_for_touch_permission",
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
            "proposal_basis_ref": "bounded explicit touch-permission test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission.py"
            ),
        }

    def query_request(self) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_touch_permission",
            "query_target": "answer_read_output",
            "requested_fields": list(QUERY_FIELDS),
            "query_basis": "bounded current-state query artifact for touch test",
        }

    def stand_request(self) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "stand_now_before_touch_permission",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(STAND_FIELDS),
            "query_basis": "bounded stand-now artifact for touch test",
        }

    def open_request(self) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "open_surface_before_touch_permission",
            "query_family": "what_remains_open",
            "requested_open_fields": list(OPEN_FIELDS),
            "query_basis": "bounded what-remains-open artifact for touch test",
        }

    def touch_request(
        self,
        touch_class: str = touch_resolver.TOUCH_CLASS_READ_ONLY,
        fields: list[str] | None = None,
        *,
        basis: str = "bounded current-state touch permission test basis",
        label: str = "touch_permission_test",
        use: str = "bounded downstream current-state inspection",
    ) -> dict[str, Any]:
        return {
            "touch_request_id": f"touch_{touch_class.lower()}",
            "requested_touch_class": touch_class,
            "requested_touch_basis": basis,
            "requesting_surface_label": label,
            "intended_downstream_use": use,
            "requested_touch_fields": list(fields or []),
        }

    def resolve_object(
        self,
        temp_root: Path,
        request: dict[str, Any],
        surface: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
            return touch_resolver.resolve_current_state_touch_permission(
                request,
                surface,
            )

    def resolve_default(
        self,
        temp_root: Path,
        request: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
            return touch_resolver.resolve_current_state_touch_permission(request)

    def resolve_path(
        self,
        temp_root: Path,
        path: Path,
        request: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
            return touch_resolver.resolve_current_state_touch_permission_from_path(
                path,
                request,
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
        self.assertIsInstance(result["touch_permission_metadata"], dict)
        self.assertIsInstance(result["selected_current_state_surface"], dict)
        self.assertIsInstance(result["touch_request"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertTrue(
            result["admitted_touch_scope"] is None
            or isinstance(result["admitted_touch_scope"], dict)
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

    def assert_admitted(
        self,
        result: dict[str, Any],
        touch_class: str,
        result_family: str | None = None,
    ) -> None:
        self.assert_shape(result)
        self.assertEqual(result["outcome"], touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH)
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsInstance(result["admitted_touch_scope"], dict)
        self.assertEqual(
            result["admitted_touch_scope"]["admitted_touch_class"],
            touch_class,
        )
        if result_family is not None:
            self.assertEqual(
                result["selected_current_state_surface"][
                    "selected_surface_result_family"
                ],
                result_family,
            )
        for key in (
            "replay_refused",
            "merge_refused",
            "mutation_refused",
            "continuity_completion_refused",
            "standing_upgrade_refused",
        ):
            self.assertTrue(result["admitted_touch_scope"][key])
        self.assert_non_claims_false(result)
        self.assert_checks(result, all_pass=True)

    def assert_refused(
        self,
        result: dict[str, Any],
        code: str,
        *,
        expect_false_non_claims: bool = True,
    ) -> None:
        self.assert_shape(result)
        self.assertEqual(result["outcome"], touch_resolver.OUTCOME_REFUSED)
        self.assertEqual(result["block"]["block_code"], code)
        self.assert_non_empty(result["block"]["block_reason"])
        self.assertIsNone(result["admitted_touch_scope"])
        self.assert_checks(result, all_pass=False)
        if expect_false_non_claims:
            self.assert_non_claims_false(result)

    def assert_summary(self, result: dict[str, Any], touch_class: str) -> None:
        summary = touch_resolver.build_current_state_touch_permission_summary(result)
        for key in (
            "touch_permission_result_id",
            "outcome",
            "block_code",
            "block_reason",
            "selected_current_state_surface_id",
            "selected_result_family",
            "requested_touch_class",
            "admitted_touch_class",
            "passed_check_count",
            "failed_check_count",
            "key_non_claims",
        ):
            self.assertIn(key, summary)
        self.assertEqual(summary["outcome"], touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH)
        self.assertEqual(summary["requested_touch_class"], touch_class)
        self.assertEqual(summary["admitted_touch_class"], touch_class)
        self.assertGreater(summary["passed_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        for key in touch_resolver.REQUIRED_FALSE_NON_CLAIMS:
            self.assertIn(key, summary["key_non_claims"])
            self.assertFalse(summary["key_non_claims"][key])

    def test_admits_read_reference_and_derivation_touch(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            read_result = self.resolve_object(
                temp_root,
                self.touch_request(touch_resolver.TOUCH_CLASS_READ_ONLY),
                stack["open"],
            )
            self.assert_admitted(
                read_result,
                touch_resolver.TOUCH_CLASS_READ_ONLY,
                "what_remains_open",
            )
            self.assertEqual(
                read_result["selected_current_state_surface"][
                    "selected_surface_outcome"
                ],
                open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            )
            self.assertGreater(
                len(read_result["admitted_touch_scope"]["admitted_readable_fields"]),
                0,
            )

            reference_fields = [
                "selected_surface_path",
                "selected_surface_id",
                "selected_surface_type",
                "selected_surface_outcome",
                "selected_surface_result_family",
                "effective_source_run_path",
                "effective_ingress_run_path",
                "non_claims",
            ]
            reference_result = self.resolve_object(
                temp_root,
                self.touch_request(
                    touch_resolver.TOUCH_CLASS_REFERENCE,
                    reference_fields,
                ),
                stack["open"],
            )
            self.assert_admitted(
                reference_result,
                touch_resolver.TOUCH_CLASS_REFERENCE,
                "what_remains_open",
            )
            self.assertEqual(
                reference_result["admitted_touch_scope"]["admitted_reference_fields"],
                reference_fields,
            )
            self.assertEqual(
                reference_result["admitted_touch_scope"]["admitted_readable_fields"],
                [],
            )

            derivation_fields = [
                "non_claims",
                "continuity_completed",
                "standing_upgraded",
                "answer_read_basis",
            ]
            derivation_result = self.resolve_object(
                temp_root,
                self.touch_request(
                    touch_resolver.TOUCH_CLASS_DERIVATION,
                    derivation_fields,
                ),
                stack["open"],
            )
            self.assert_admitted(
                derivation_result,
                touch_resolver.TOUCH_CLASS_DERIVATION,
                "what_remains_open",
            )
            boundary = derivation_result["admitted_touch_scope"][
                "admitted_derivation_boundary"
            ]
            self.assertEqual(
                boundary["admitted_derivation_fields"],
                derivation_fields,
            )
            self.assertTrue(boundary["derived_only_from_selected_surface"])
            self.assertTrue(boundary["does_not_create_new_ontology"])
            self.assert_summary(
                derivation_result,
                touch_resolver.TOUCH_CLASS_DERIVATION,
            )

    def test_supported_source_families_and_explicit_path_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            cases = (
                (
                    "answer_read",
                    stack["answer"],
                    answer_resolver.OUTCOME_ANSWERED,
                    ["current_governing_source_run_path", "answer_read_basis"],
                ),
                (
                    "query",
                    stack["query"],
                    query_resolver.OUTCOME_ANSWERED_QUERY,
                    ["current_governing_source_run_path", "answered_field_names"],
                ),
                (
                    "what_stands_now",
                    stack["stand"],
                    stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
                    ["current_governing_source_run_path", "non_claims"],
                ),
                (
                    "what_remains_open",
                    stack["open"],
                    open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
                    ["continuity_completed", "non_claims"],
                ),
            )

            for family, surface, outcome, fields in cases:
                with self.subTest(family=family):
                    result = self.resolve_object(
                        temp_root,
                        self.touch_request(
                            touch_resolver.TOUCH_CLASS_DERIVATION,
                            fields,
                        ),
                        surface,
                    )
                    self.assert_admitted(
                        result,
                        touch_resolver.TOUCH_CLASS_DERIVATION,
                        family,
                    )
                    self.assertEqual(
                        result["selected_current_state_surface"][
                            "selected_surface_outcome"
                        ],
                        outcome,
                    )

            path_request = self.touch_request(
                touch_resolver.TOUCH_CLASS_REFERENCE,
                ["selected_surface_id", "selected_surface_outcome", "non_claims"],
            )
            object_result = self.resolve_object(temp_root, path_request, stack["open"])
            path_result = self.resolve_path(temp_root, stack["open_path"], path_request)
            self.assert_admitted(
                path_result,
                touch_resolver.TOUCH_CLASS_REFERENCE,
                "what_remains_open",
            )
            self.assertEqual(
                object_result["selected_current_state_surface"][
                    "selected_surface_id"
                ],
                path_result["selected_current_state_surface"]["selected_surface_id"],
            )
            self.assertEqual(
                object_result["selected_current_state_surface"][
                    "selected_surface_result_family"
                ],
                path_result["selected_current_state_surface"][
                    "selected_surface_result_family"
                ],
            )
            self.assertEqual(
                path_result["selected_current_state_surface"]["selected_surface_path"],
                str(stack["open_path"].relative_to(temp_root)),
            )

    def test_request_metadata_summary_and_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            request = self.touch_request(
                touch_resolver.TOUCH_CLASS_READ_ONLY,
                ["checks", "outcome", "non_claims"],
            )
            result = self.resolve_object(temp_root, request, stack["open"])
            self.assert_admitted(result, touch_resolver.TOUCH_CLASS_READ_ONLY)
            self.assertEqual(result["touch_request"], request)

            metadata = result["touch_permission_metadata"]
            for key in (
                "touch_permission_result_id",
                "touch_permission_result_type",
                "touch_permission_result_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty(metadata[key])
            self.assertEqual(
                metadata["touch_permission_result_version"],
                touch_resolver.TOUCH_PERMISSION_RESULT_VERSION,
            )
            self.assert_summary(result, touch_resolver.TOUCH_CLASS_READ_ONLY)

            selected = result["selected_current_state_surface"]
            for key in (
                "selected_surface_path",
                "selected_surface_id",
                "selected_surface_type",
                "selected_surface_outcome",
                "selected_surface_result_family",
            ):
                self.assert_non_empty(selected[key])
            self.assertIsInstance(
                selected["selected_surface_effective_references"],
                dict,
            )

            output_path = temp_root / "nested" / "touch" / "result.json"
            with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
                written = touch_resolver.write_current_state_touch_permission_result(
                    result,
                    output_path,
                )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            self.assertEqual(set(self.read_json(written)), TOP_LEVEL)

            with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(FileExistsError):
                    touch_resolver.write_current_state_touch_permission_result(
                        result,
                        output_path,
                    )

            with mock.patch.object(touch_resolver, "_repo_root", return_value=temp_root):
                first = touch_resolver.write_current_state_touch_permission_result(
                    result
                )
                second = touch_resolver.write_current_state_touch_permission_result(
                    result
                )
            root = (temp_root / touch_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT).resolve()
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            self.assertTrue(first.resolve().is_relative_to(root))
            self.assertTrue(second.resolve().is_relative_to(root))
            self.assertTrue(
                first.name.endswith("__current_state_touch_permission_result.json")
            )
            self.assertTrue(
                second.name.endswith(
                    "__current_state_touch_permission_result_001.json"
                )
            )
            self.assertLess(len(first.name), 255)
            self.assertLess(len(second.name), 255)

    def test_refuses_missing_blocked_unsuccessful_out_of_scope_and_bad_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            result = self.resolve_default(
                temp_root,
                self.touch_request(touch_resolver.TOUCH_CLASS_READ_ONLY),
            )
            self.assert_refused(result, "NO_ADMISSIBLE_CURRENT_STATE_SURFACE")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)

            blocked = self.copy(stack["open"])
            blocked["outcome"] = "BLOCKED"
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.touch_request(),
                    blocked,
                ),
                "SELECTED_SURFACE_BLOCKED",
            )

            pending = self.copy(stack["open"])
            pending["outcome"] = "PENDING"
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.touch_request(),
                    pending,
                ),
                "SELECTED_SURFACE_NOT_SUCCESSFUL",
            )

            out_of_scope_surface = {
                "outcome": "ANSWERED",
                "unknown_metadata": {"unknown_result_id": "unsupported_surface"},
                "non_claims": {},
            }
            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.touch_request(),
                    out_of_scope_surface,
                ),
                "SELECTED_SURFACE_OUT_OF_SCOPE",
            )

            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.touch_request("WRITE_TOUCH", ["outcome"]),
                    stack["open"],
                ),
                "TOUCH_CLASS_OUT_OF_SCOPE",
            )

            self.assert_refused(
                self.resolve_object(
                    temp_root,
                    self.touch_request(
                        touch_resolver.TOUCH_CLASS_REFERENCE,
                        ["what_remains_open_answer"],
                    ),
                    stack["open"],
                ),
                "TOUCH_SCOPE_OUT_OF_SCOPE",
            )

    def test_refuses_shortcuts_and_non_claim_mutations(self) -> None:
        shortcut_cases = (
            (
                "permission to replay into a live host",
                "bounded inspection",
                "REPLAY_SHORTCUT_REFUSED",
            ),
            (
                "permission to merge into local state",
                "bounded inspection",
                "MERGE_SHORTCUT_REFUSED",
            ),
            (
                "bounded basis",
                "complete continuity from this touch",
                "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
            ),
            (
                "bounded basis",
                "perform standing upgrade",
                "SILENT_STANDING_UPGRADE_REFUSED",
            ),
            (
                "fallback to prior-family fallback",
                "bounded inspection",
                "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
            ),
            (
                "use latest authority artifact",
                "bounded inspection",
                "LATEST_FILE_INFERENCE_REFUSED",
            ),
            (
                "bounded basis",
                "claim final governance and protocol law",
                "IMPLICIT_AUTHORITY_CLAIM_REFUSED",
            ),
            (
                "bounded basis",
                "mutate prior artifacts",
                "IMPLICIT_MUTATION_REFUSED",
            ),
        )
        for basis, use, code in shortcut_cases:
            with self.subTest(code=code):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(temp_root)
                    result = self.resolve_object(
                        temp_root,
                        self.touch_request(
                            touch_resolver.TOUCH_CLASS_READ_ONLY,
                            ["outcome"],
                            basis=basis,
                            use=use,
                        ),
                        stack["open"],
                    )
                    self.assert_refused(result, code)

        for non_claim_key, code in (
            ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
            ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
            ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
            (
                "final_current_state_what_remains_open_completed",
                "IMPLICIT_AUTHORITY_CLAIM_REFUSED",
            ),
        ):
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(temp_root)
                    surface = self.copy(stack["open"])
                    surface["non_claims"][non_claim_key] = True
                    result = self.resolve_object(
                        temp_root,
                        self.touch_request(
                            touch_resolver.TOUCH_CLASS_READ_ONLY,
                            ["outcome"],
                        ),
                        surface,
                    )
                    self.assert_refused(
                        result,
                        code,
                        expect_false_non_claims=False,
                    )
                    self.assertTrue(result["non_claims"][non_claim_key])

    def test_refuses_effective_reference_mismatch_and_multiple_conflict(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            missing = self.copy(stack["open"])
            missing["effective_open_inputs"]["effective_authority_artifact_path"] = (
                "artifacts/missing_authority_for_touch.json"
            )
            result = self.resolve_object(
                temp_root,
                self.touch_request(),
                missing,
            )
            self.assert_refused(result, "EFFECTIVE_REFERENCE_INCOHERENCE")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            bad_family = self.copy(stack["family"])
            bad_family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            bad_family_path = temp_root / "bad_effective_family_packet.json"
            self.write_json(bad_family_path, bad_family)
            surface = self.copy(stack["open"])
            surface["effective_open_inputs"]["effective_family_packet_path"] = str(
                bad_family_path
            )
            result = self.resolve_object(
                temp_root,
                self.touch_request(),
                surface,
            )
            self.assert_refused(result, "CANONICAL_EXECUTION_LINE_MISMATCH")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            conflict = self.copy(stack["open"])
            conflict["what_remains_open_metadata"][
                "what_remains_open_result_id"
            ] = "conflicting_open_surface_for_touch_permission"
            conflict["effective_open_inputs"]["effective_source_run_path"] = (
                "artifacts/conflicting_source_run_path"
            )
            self.write_json(
                temp_root
                / open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
                / "zz_conflicting_open_surface_for_touch_permission.json",
                conflict,
            )
            result = self.resolve_default(
                temp_root,
                self.touch_request(touch_resolver.TOUCH_CLASS_READ_ONLY),
            )
            self.assert_refused(
                result,
                "MULTIPLE_CURRENT_STATE_SURFACES_CONFLICT_UNRESOLVED",
            )

    def test_malformed_failures(self) -> None:
        malformed_requests: tuple[tuple[str, Any], ...] = (
            (
                "missing_id",
                {
                    "requested_touch_class": touch_resolver.TOUCH_CLASS_READ_ONLY,
                    "requested_touch_basis": "bounded",
                    "requesting_surface_label": "test",
                    "intended_downstream_use": "read",
                    "requested_touch_fields": [],
                },
            ),
            (
                "missing_class",
                {
                    "touch_request_id": "touch_without_class",
                    "requested_touch_basis": "bounded",
                    "requesting_surface_label": "test",
                    "intended_downstream_use": "read",
                    "requested_touch_fields": [],
                },
            ),
            (
                "missing_basis",
                {
                    "touch_request_id": "touch_without_basis",
                    "requested_touch_class": touch_resolver.TOUCH_CLASS_READ_ONLY,
                    "requesting_surface_label": "test",
                    "intended_downstream_use": "read",
                    "requested_touch_fields": [],
                },
            ),
            (
                "missing_label",
                {
                    "touch_request_id": "touch_without_label",
                    "requested_touch_class": touch_resolver.TOUCH_CLASS_READ_ONLY,
                    "requested_touch_basis": "bounded",
                    "intended_downstream_use": "read",
                    "requested_touch_fields": [],
                },
            ),
            (
                "missing_use",
                {
                    "touch_request_id": "touch_without_use",
                    "requested_touch_class": touch_resolver.TOUCH_CLASS_READ_ONLY,
                    "requested_touch_basis": "bounded",
                    "requesting_surface_label": "test",
                    "requested_touch_fields": [],
                },
            ),
            (
                "wrong_fields_type",
                {
                    "touch_request_id": "touch_bad_fields",
                    "requested_touch_class": touch_resolver.TOUCH_CLASS_READ_ONLY,
                    "requested_touch_basis": "bounded",
                    "requesting_surface_label": "test",
                    "intended_downstream_use": "read",
                    "requested_touch_fields": "outcome",
                },
            ),
            ("not_mapping", ["not", "a", "mapping"]),
        )
        for label, request in malformed_requests:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    with self.assertRaises(
                        touch_resolver.CurrentStateTouchPermissionError
                    ):
                        self.resolve_default(
                            Path(temp_dir).resolve(),
                            request,  # type: ignore[arg-type]
                        )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            malformed = temp_root / "malformed_surface.json"
            malformed.write_text("[1, 2, 3]\n", encoding="utf-8")
            with self.assertRaises(touch_resolver.CurrentStateTouchPermissionError):
                self.resolve_path(temp_root, malformed, self.touch_request())

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            malformed_effective = self.copy(stack["open"])
            malformed_effective["effective_open_inputs"] = []
            with self.assertRaises(touch_resolver.CurrentStateTouchPermissionError):
                self.resolve_object(temp_root, self.touch_request(), malformed_effective)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            root_file = temp_root / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
            root_file.parent.mkdir(parents=True, exist_ok=True)
            root_file.write_text("not a directory\n", encoding="utf-8")
            with self.assertRaises(touch_resolver.CurrentStateTouchPermissionError):
                self.resolve_default(temp_root, self.touch_request())

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root
                / effective_resolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / effective_resolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root / effective_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root / effective_resolver.CURRENT_GOVERNING_PACKET_ROOT,
                "transition": temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT,
                "reresolution": temp_root / reresolver.GOVERNING_RERESOLUTION_ROOT,
                "adoption": temp_root / effective_resolver.GOVERNING_SUCCESSOR_ADOPTION_ROOT,
                "effective": temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_RESOLUTION_ROOT,
                "consumption": temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT,
                "current_work_input": temp_root / work_input_resolver.CURRENT_WORK_INPUT_ROOT,
                "current_work_operation": temp_root
                / operation_resolver.CURRENT_WORK_OPERATION_ROOT,
                "current_state_readout": temp_root
                / readout_resolver.CURRENT_STATE_READOUT_ROOT,
                "current_state_handoff": temp_root
                / handoff_resolver.CURRENT_STATE_HANDOFF_ROOT,
                "current_state_export": temp_root
                / export_resolver.CURRENT_STATE_EXPORT_ROOT,
                "current_state_delivery": temp_root
                / delivery_resolver.CURRENT_STATE_DELIVERY_ROOT,
                "current_state_application": temp_root
                / application_resolver.CURRENT_STATE_APPLICATION_ROOT,
                "current_state_answer_read": temp_root
                / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT,
                "current_state_query": temp_root / query_resolver.CURRENT_STATE_QUERY_ROOT,
                "current_state_what_stands_now": temp_root
                / stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT,
                "current_state_what_remains_open": temp_root
                / open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT,
            }
            before = {label: self.tree_digest(root) for label, root in roots.items()}
            request = self.touch_request(
                touch_resolver.TOUCH_CLASS_DERIVATION,
                ["continuity_completed", "non_claims"],
            )

            first = self.resolve_object(temp_root, request, stack["open"])
            second = self.resolve_path(temp_root, stack["open_path"], request)
            after = {label: self.tree_digest(root) for label, root in roots.items()}

            self.assert_admitted(first, touch_resolver.TOUCH_CLASS_DERIVATION)
            self.assert_admitted(second, touch_resolver.TOUCH_CLASS_DERIVATION)
            self.assertEqual(before, after)
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(
                first["selected_current_state_surface"]["selected_surface_id"],
                second["selected_current_state_surface"]["selected_surface_id"],
            )
            for key in (
                "replayed_into_live_host",
                "merged_into_local_state",
                "continuity_completed",
                "standing_upgraded",
                "minimum_lawful_system_completed",
                "final_system_identity_completed",
            ):
                self.assertFalse(first["non_claims"][key])


if __name__ == "__main__":
    unittest.main()
