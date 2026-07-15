"""Bounded tests for the v0-min current-state "what remains open" resolver.

The suite locks the current behavior of
``src/resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open.py``.
It emits real local source runs, ingress runs, comparison artifacts, authority,
family, status, governing, transition, re-resolution, adoption, effective-family,
current-work, current-state answer/read, current-state query, and
what-stands-now artifacts into temporary roots.

These tests are only for the bounded concrete open-surface resolver. They do
not test replay, merge, persistence, registry, distributed continuity, CLI,
chat/API/dashboard, reporting, or workflow behavior.
"""

from __future__ import annotations

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
    "what_remains_open_metadata",
    "selected_current_state_answer_read",
    "what_remains_open_request",
    "effective_open_inputs",
    "checks",
    "outcome",
    "block",
    "what_remains_open_answer",
    "what_remains_open_summary",
    "non_claims",
}

OPEN_INPUT_KEYS = {
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
}

PATH_INPUT_KEYS = {
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
}

EXPECTED_NON_CLAIMS = {
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
    "final_current_state_what_stands_now_completed",
    "final_current_state_what_remains_open_completed",
}

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


class CurrentStateWhatRemainsOpenTests(unittest.TestCase):
    def build_stack(
        self,
        temp_root: Path,
        *,
        write_answer: bool = True,
        write_query: bool = True,
        write_stand: bool = True,
    ) -> dict[str, Any]:
        source_one = self.emit_source(temp_root, "run_20260420T000000_000000Z")
        ingress_one = self.emit_ingress(temp_root, source_one)
        comparison_one = self.emit_comparison(temp_root, source_one, ingress_one)
        source_two = self.emit_source(temp_root, "run_20260420T000001_000000Z")
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

        with mock.patch.object(
            consumption_resolver,
            "_repo_root",
            return_value=temp_root,
        ):
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
            answer_path = (
                answer_resolver.write_current_state_answer_read_result(answer)
                if write_answer
                else None
            )
        self.assertEqual(answer["outcome"], answer_resolver.OUTCOME_ANSWERED)

        with mock.patch.object(query_resolver, "_repo_root", return_value=temp_root):
            query = query_resolver.resolve_current_state_query(
                self.query_request(),
                answer,
            )
            query_path = (
                query_resolver.write_current_state_query_result(query)
                if write_query
                else None
            )
        self.assertEqual(query["outcome"], query_resolver.OUTCOME_ANSWERED_QUERY)

        with mock.patch.object(stand_resolver, "_repo_root", return_value=temp_root):
            stand = stand_resolver.resolve_current_state_what_stands_now(
                self.stand_request(),
                answer,
            )
            stand_path = (
                stand_resolver.write_current_state_what_stands_now_result(stand)
                if write_stand
                else None
            )
        self.assertEqual(
            stand["outcome"],
            stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
        )

        return {
            "source_one": source_one,
            "ingress_one": ingress_one,
            "comparison_one": comparison_one,
            "source_two": source_two,
            "ingress_two": ingress_two,
            "comparison_two": comparison_two,
            "authority_path": authority_path,
            "authority": authority,
            "family_path": family_path,
            "family": family,
            "status_path": status_path,
            "status": status,
            "governing_path": governing_path,
            "governing": governing,
            "current_entry": current_entry,
            "candidate_entry": candidates[0],
            "transition_path": transition_path,
            "transition": transition,
            "reresolution_path": reresolution_path,
            "reresolution": reresolution,
            "adoption_path": adoption_path,
            "adoption": adoption,
            "effective_path": effective_path,
            "effective": effective,
            "consumption_path": consumption_path,
            "consumption": consumption,
            "work_input_path": work_input_path,
            "work_input": work_input,
            "operation_path": operation_path,
            "operation": operation,
            "readout_path": readout_path,
            "readout": readout,
            "handoff_path": handoff_path,
            "handoff": handoff,
            "export_path": export_path,
            "export": export,
            "delivery_path": delivery_path,
            "delivery": delivery,
            "application_path": application_path,
            "application": application,
            "answer_path": answer_path,
            "answer": answer,
            "query_path": query_path,
            "query": query,
            "stand_path": stand_path,
            "stand": stand,
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
            "transition_proposal_id": "proposal_accepted_for_what_remains_open",
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
            "proposal_basis_ref": "bounded explicit what-remains-open test basis",
            "proposed_at": "2026-04-22T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open.py"
            ),
        }

    def query_request(self) -> dict[str, Any]:
        return {
            "query_request_id": "query_current_state_paths_for_open_surface",
            "query_target": "answer_read_output",
            "requested_fields": list(QUERY_FIELDS),
            "query_basis": "bounded current-state query artifact for open-surface test",
        }

    def stand_request(self) -> dict[str, Any]:
        return {
            "what_stands_now_request_id": "stand_now_before_open_surface",
            "query_family": "what_stands_now",
            "requested_stand_now_fields": list(STAND_FIELDS),
            "query_basis": "bounded stand-now artifact for open-surface test",
        }

    def open_request(self, fields: list[str] | None = None) -> dict[str, Any]:
        return {
            "what_remains_open_request_id": "open_current_state",
            "query_family": "what_remains_open",
            "requested_open_fields": list(fields or OPEN_FIELDS),
            "query_basis": "bounded what-remains-open test basis",
        }

    def resolve_default(self, temp_root: Path, request: dict[str, Any]) -> dict[str, Any]:
        with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
            return open_resolver.resolve_current_state_what_remains_open(request)

    def resolve_object(
        self,
        temp_root: Path,
        request: dict[str, Any],
        answer: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
            return open_resolver.resolve_current_state_what_remains_open(
                request,
                answer,
            )

    def resolve_path(
        self,
        temp_root: Path,
        path: Path,
        request: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
            return open_resolver.resolve_current_state_what_remains_open_from_path(
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

    def json_texts(self, root: Path) -> dict[str, str]:
        if not root.exists():
            return {}
        return {
            str(path.relative_to(root)): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*.json"))
        }

    def assert_non_empty(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_paths_same(self, temp_root: Path, left: str | Path, right: str | Path) -> None:
        self.assertEqual(self.display_path(temp_root, left), self.display_path(temp_root, right))

    def assert_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), TOP_LEVEL)
        self.assertIsInstance(result["what_remains_open_metadata"], dict)
        self.assertIsInstance(result["selected_current_state_answer_read"], dict)
        self.assertTrue(
            result["what_remains_open_request"] is None
            or isinstance(result["what_remains_open_request"], dict)
        )
        self.assertIsInstance(result["effective_open_inputs"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertIsInstance(result["what_remains_open_summary"], dict)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_answered(self, result: dict[str, Any]) -> None:
        self.assert_shape(result)
        self.assertEqual(
            result["outcome"],
            open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
        )
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertIsInstance(result["what_remains_open_answer"], dict)
        self.assertEqual(set(result["effective_open_inputs"]), OPEN_INPUT_KEYS)
        for value in result["effective_open_inputs"].values():
            self.assert_non_empty(value)
        self.assert_non_claims_false(result)

    def assert_blocked(
        self,
        result: dict[str, Any],
        code: str,
        *,
        expect_false_non_claims: bool = True,
    ) -> None:
        self.assert_shape(result)
        self.assertEqual(result["outcome"], open_resolver.OUTCOME_BLOCKED)
        self.assertEqual(result["block"]["block_code"], code)
        self.assert_non_empty(result["block"]["block_reason"])
        self.assertIsNone(result["what_remains_open_answer"])
        if expect_false_non_claims:
            self.assert_non_claims_false(result)

    def assert_inputs_match_answer(
        self,
        temp_root: Path,
        result: dict[str, Any],
        answer: dict[str, Any],
    ) -> None:
        for key in OPEN_INPUT_KEYS:
            self.assert_paths_same(
                temp_root,
                result["effective_open_inputs"][key],
                answer["effective_answer_read_inputs"][key],
            )

    def effective_files(self, temp_root: Path, result: dict[str, Any]) -> dict[str, Any]:
        parsed = {}
        for key in PATH_INPUT_KEYS:
            path = self.display_path(temp_root, result["effective_open_inputs"][key])
            self.assertTrue(path.is_file(), key)
            parsed[key] = self.read_json(path)
        return parsed

    def test_answered_default_path_object_request_answer_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            request = self.open_request()

            default_result = self.resolve_default(temp_root, request)
            object_result = self.resolve_object(temp_root, request, stack["answer"])
            path_result = self.resolve_path(temp_root, stack["answer_path"], request)

            for result in (default_result, object_result, path_result):
                self.assert_answered(result)
                self.assertEqual(result["what_remains_open_request"], request)
                metadata = result["what_remains_open_metadata"]
                for key in (
                    "what_remains_open_result_id",
                    "what_remains_open_result_type",
                    "what_remains_open_result_version",
                    "generated_at",
                    "resolver_module",
                ):
                    self.assert_non_empty(metadata[key])

            self.assert_paths_same(
                temp_root,
                default_result["selected_current_state_answer_read"][
                    "current_state_answer_read_result_path"
                ],
                stack["answer_path"],
            )
            self.assertIsNone(
                object_result["selected_current_state_answer_read"][
                    "current_state_answer_read_result_path"
                ]
            )
            self.assert_paths_same(
                temp_root,
                path_result["selected_current_state_answer_read"][
                    "current_state_answer_read_result_path"
                ],
                stack["answer_path"],
            )
            for result in (default_result, object_result, path_result):
                selected = result["selected_current_state_answer_read"]
                self.assertEqual(
                    selected["current_state_answer_read_result_id"],
                    stack["answer"]["answer_read_metadata"]["answer_read_result_id"],
                )
                self.assertEqual(selected["outcome"], answer_resolver.OUTCOME_ANSWERED)
                self.assertEqual(
                    selected["selected_current_state_application_id"],
                    stack["application"]["application_metadata"]["application_result_id"],
                )
                self.assert_inputs_match_answer(temp_root, result, stack["answer"])

            answer = object_result["what_remains_open_answer"]
            self.assertEqual(set(answer), set(request["requested_open_fields"]))
            output = stack["answer"]["answer_read_output"]
            for field in (
                "current_work_basis",
                "readout_basis",
                "handoff_basis",
                "export_basis",
                "delivery_basis",
            ):
                self.assertEqual(answer[field], output.get(field))
            self.assertEqual(answer["application_basis"], "delivered_current_state_result")
            self.assertEqual(answer["answer_read_basis"], "applied_current_state_result")
            self.assertFalse(answer["authority_resolution_is_protocol_law"])
            self.assertFalse(answer["final_persistence_or_registry_law"])
            self.assertEqual(answer["non_claims"], object_result["non_claims"])
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, answer["non_claims"])
                self.assertFalse(answer["non_claims"][key])
                if key in answer:
                    self.assertFalse(answer[key])

            self.assertGreater(len(object_result["checks"]), 0)
            for check in object_result["checks"]:
                self.assertIn("check_name", check)
                self.assertIn("passed", check)
                self.assertIsInstance(check["check_name"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])
                if "expected_posture" in check:
                    self.assertIsNotNone(check["expected_posture"])
                if "actual_posture" in check:
                    self.assertIsNotNone(check["actual_posture"])

            summary = open_resolver.build_current_state_what_remains_open_summary(
                object_result
            )
            for key in (
                "what_remains_open_result_id",
                "outcome",
                "block_code",
                "block_reason",
                "selected_current_state_answer_read_id",
                "requested_field_names",
                "answered_field_names",
                "passed_check_count",
                "failed_check_count",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(
                summary["outcome"],
                open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
            )
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(summary["requested_field_names"], request["requested_open_fields"])
            self.assertEqual(summary["answered_field_names"], request["requested_open_fields"])
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["failed_check_count"], 0)
            self.assertEqual(
                object_result["what_remains_open_summary"]["open_surface_basis"],
                "answered_current_state_result",
            )
            self.assertEqual(
                object_result["what_remains_open_summary"]["query_family"],
                "what_remains_open",
            )

    def test_semantics_prior_family_and_non_mutation(self) -> None:
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
                "effective": temp_root / consumption_resolver.EFFECTIVE_FAMILY_RESOLUTION_ROOT,
                "consumption": temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT,
                "current_work_input": temp_root / work_input_resolver.CURRENT_WORK_INPUT_ROOT,
                "current_work_operation": temp_root / operation_resolver.CURRENT_WORK_OPERATION_ROOT,
                "current_state_readout": temp_root / readout_resolver.CURRENT_STATE_READOUT_ROOT,
                "current_state_handoff": temp_root / handoff_resolver.CURRENT_STATE_HANDOFF_ROOT,
                "current_state_export": temp_root / export_resolver.CURRENT_STATE_EXPORT_ROOT,
                "current_state_delivery": temp_root / delivery_resolver.CURRENT_STATE_DELIVERY_ROOT,
                "current_state_application": temp_root / application_resolver.CURRENT_STATE_APPLICATION_ROOT,
                "current_state_answer_read": temp_root / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT,
                "current_state_query": temp_root / query_resolver.CURRENT_STATE_QUERY_ROOT,
                "current_state_what_stands_now": temp_root
                / stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT,
            }
            before = {label: self.json_texts(root) for label, root in roots.items()}
            request = self.open_request()

            object_result = self.resolve_object(temp_root, request, stack["answer"])
            after_object = {label: self.json_texts(root) for label, root in roots.items()}
            path_result = self.resolve_path(temp_root, stack["answer_path"], request)
            after_path = {label: self.json_texts(root) for label, root in roots.items()}

            self.assert_answered(object_result)
            self.assert_answered(path_result)
            self.assertEqual(after_object, before)
            self.assertEqual(after_path, before)
            self.assertEqual(object_result["outcome"], path_result["outcome"])
            self.assertEqual(
                object_result["effective_open_inputs"],
                path_result["effective_open_inputs"],
            )
            self.assertEqual(
                object_result["what_remains_open_answer"],
                path_result["what_remains_open_answer"],
            )
            self.assertEqual(
                object_result["what_remains_open_summary"],
                path_result["what_remains_open_summary"],
            )

            for effective_key, prior_key in (
                ("effective_authority_artifact_path", "prior_authority_artifact_path"),
                ("effective_family_packet_path", "prior_family_packet_path"),
                ("effective_status_packet_path", "prior_status_packet_path"),
                (
                    "effective_current_governing_packet_path",
                    "prior_current_governing_packet_path",
                ),
            ):
                self.assertNotEqual(
                    self.display_path(
                        temp_root,
                        object_result["effective_open_inputs"][effective_key],
                    ),
                    self.display_path(
                        temp_root,
                        stack["effective"]["prior_current_family"][prior_key],
                    ),
                )

            parsed = self.effective_files(temp_root, object_result)
            effective_status = parsed["effective_status_packet_path"]
            effective_governing = parsed["effective_current_governing_packet_path"]
            prior_source = stack["current_entry"]["source_run_directory_path"]
            successor_source = stack["candidate_entry"]["source_run_directory_path"]
            prior_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
                if self.display_path(temp_root, entry["source_run_directory_path"])
                == self.display_path(temp_root, prior_source)
            ]
            successor_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
                if self.display_path(temp_root, entry["source_run_directory_path"])
                == self.display_path(temp_root, successor_source)
            ]
            self.assertEqual(len(prior_entries), 1)
            self.assertEqual(len(successor_entries), 1)
            self.assertFalse(prior_entries[0]["current_authority"])
            self.assertTrue(successor_entries[0]["current_authority"])
            self.assert_paths_same(
                temp_root,
                effective_governing["current_governing_run"][
                    "source_run_directory_path"
                ],
                successor_source,
            )
            for key in (
                "replayed_into_live_host",
                "merged_into_local_state",
                "continuity_completed",
                "standing_upgraded",
                "final_current_state_what_remains_open_completed",
            ):
                self.assertFalse(object_result["non_claims"][key])

    def test_no_answer_or_blocked_answer_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            result = self.resolve_default(Path(temp_dir).resolve(), self.open_request())
            self.assert_blocked(result, "NO_CURRENT_STATE_ANSWER_READ_RESULT")
            self.assertIsNone(
                result["selected_current_state_answer_read"][
                    "current_state_answer_read_result_id"
                ]
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(
                temp_root,
                write_answer=False,
                write_query=False,
                write_stand=False,
            )
            blocked = self.copy(stack["answer"])
            blocked["outcome"] = answer_resolver.OUTCOME_BLOCKED
            blocked["block"] = {
                "block_code": "TEST_BLOCKED_ANSWER_READ",
                "block_reason": "Blocked current-state answer/read fixture.",
            }
            blocked["answer_read_output"] = None
            answer_root = temp_root / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
            self.write_json(answer_root / "blocked_current_state_answer_read.json", blocked)
            default_result = self.resolve_default(temp_root, self.open_request())
            object_result = self.resolve_object(temp_root, self.open_request(), blocked)
            self.assert_blocked(default_result, "NO_CURRENT_STATE_ANSWER_READ_RESULT")
            self.assert_blocked(object_result, "CURRENT_STATE_ANSWER_READ_NOT_ANSWERED")

    def test_malformed_answer_and_request_failures(self) -> None:
        malformed_requests: tuple[tuple[str, Any], ...] = (
            (
                "missing_request_id",
                {
                    "query_family": "what_remains_open",
                    "requested_open_fields": ["non_claims"],
                    "query_basis": "bounded",
                },
            ),
            (
                "missing_query_family",
                {
                    "what_remains_open_request_id": "open_without_family",
                    "requested_open_fields": ["non_claims"],
                    "query_basis": "bounded",
                },
            ),
            (
                "wrong_query_family",
                {
                    "what_remains_open_request_id": "open_wrong_family",
                    "query_family": "what_stands_now",
                    "requested_open_fields": ["non_claims"],
                    "query_basis": "bounded",
                },
            ),
            (
                "empty_requested_fields",
                {
                    "what_remains_open_request_id": "open_without_fields",
                    "query_family": "what_remains_open",
                    "requested_open_fields": [],
                    "query_basis": "bounded",
                },
            ),
            (
                "missing_query_basis",
                {
                    "what_remains_open_request_id": "open_without_basis",
                    "query_family": "what_remains_open",
                    "requested_open_fields": ["non_claims"],
                },
            ),
            (
                "wrong_requested_fields_type",
                {
                    "what_remains_open_request_id": "open_wrong_fields",
                    "query_family": "what_remains_open",
                    "requested_open_fields": "non_claims",
                    "query_basis": "bounded",
                },
            ),
            ("not_a_mapping", ["not", "a", "mapping"]),
        )
        for label, request in malformed_requests:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    with self.assertRaises(
                        open_resolver.CurrentStateWhatRemainsOpenError
                    ):
                        with mock.patch.object(
                            open_resolver,
                            "_repo_root",
                            return_value=Path(temp_dir).resolve(),
                        ):
                            open_resolver.resolve_current_state_what_remains_open(
                                request,  # type: ignore[arg-type]
                            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            missing = temp_root / "missing_current_state_answer_read.json"
            result = self.resolve_path(temp_root, missing, self.open_request())
            self.assert_blocked(result, "CURRENT_STATE_ANSWER_READ_UNREADABLE")

            malformed = temp_root / "malformed_current_state_answer_read.json"
            malformed.write_text("[1, 2, 3]\n", encoding="utf-8")
            with self.assertRaises(open_resolver.CurrentStateWhatRemainsOpenError):
                self.resolve_path(temp_root, malformed, self.open_request())

        for label, payload in (
            ("non_mapping_input", "not a mapping"),
            (
                "missing_effective_answer_read_inputs",
                {"outcome": answer_resolver.OUTCOME_ANSWERED},
            ),
        ):
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    with self.assertRaises(
                        open_resolver.CurrentStateWhatRemainsOpenError
                    ):
                        with mock.patch.object(
                            open_resolver,
                            "_repo_root",
                            return_value=Path(temp_dir).resolve(),
                        ):
                            open_resolver.resolve_current_state_what_remains_open(
                                self.open_request(),
                                payload,  # type: ignore[arg-type]
                            )

    def test_request_out_of_scope_blocks(self) -> None:
        for fields in (
            ["not_exposed_by_open_surface"],
            ["replay_into_live_host"],
            ["merge_preserved_runs_into_live_state"],
            ["continuity_completed_as_world_completion"],
            ["hidden_provenance"],
            ["final_system_identity_completed_by_open_surface"],
        ):
            with self.subTest(fields=fields):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(
                        temp_root,
                        write_answer=False,
                        write_query=True,
                        write_stand=True,
                    )
                    result = self.resolve_object(
                        temp_root,
                        self.open_request(fields),
                        stack["answer"],
                    )
                    self.assert_blocked(
                        result,
                        "WHAT_REMAINS_OPEN_REQUEST_OUT_OF_SCOPE",
                    )

    def test_effective_artifact_unreadable_malformed_and_schema_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            answer = self.copy(stack["answer"])
            missing_status = self.display_path(
                temp_root,
                answer["effective_answer_read_inputs"]["effective_status_packet_path"],
            )
            missing_status.unlink()
            result = self.resolve_object(temp_root, self.open_request(), answer)
            self.assert_blocked(result, "EFFECTIVE_OPEN_SURFACE_ARTIFACT_UNREADABLE")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            answer = self.copy(stack["answer"])
            malformed_authority = self.display_path(
                temp_root,
                answer["effective_answer_read_inputs"][
                    "effective_authority_artifact_path"
                ],
            )
            malformed_authority.write_text("{not valid json\n", encoding="utf-8")
            with self.assertRaises(open_resolver.CurrentStateWhatRemainsOpenError):
                self.resolve_object(temp_root, self.open_request(), answer)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            answer = self.copy(stack["answer"])
            status_path = self.display_path(
                temp_root,
                answer["effective_answer_read_inputs"]["effective_status_packet_path"],
            )
            status = self.read_json(status_path)
            status.pop("aggregate_status_counts", None)
            self.write_json(status_path, status)
            with self.assertRaises(open_resolver.CurrentStateWhatRemainsOpenError):
                self.resolve_object(temp_root, self.open_request(), answer)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            root_file = temp_root / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
            root_file.parent.mkdir(parents=True, exist_ok=True)
            root_file.write_text("not a directory\n", encoding="utf-8")
            with self.assertRaises(open_resolver.CurrentStateWhatRemainsOpenError):
                self.resolve_default(temp_root, self.open_request())

    def test_canonical_stale_and_nonclaim_shortcuts_block(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            answer = self.copy(stack["answer"])
            family_path = self.display_path(
                temp_root,
                answer["effective_answer_read_inputs"]["effective_family_packet_path"],
            )
            family = self.read_json(family_path)
            family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            self.write_json(family_path, family)
            result = self.resolve_object(temp_root, self.open_request(), answer)
            self.assert_blocked(result, "CANONICAL_EXECUTION_LINE_MISMATCH")

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            self.assert_answered(
                self.resolve_object(temp_root, self.open_request(), stack["answer"])
            )
            stale = self.copy(stack["answer"])
            stale["effective_answer_read_inputs"].update(
                {
                    "effective_authority_artifact_path": stack["effective"][
                        "prior_current_family"
                    ]["prior_authority_artifact_path"],
                    "effective_family_packet_path": stack["effective"][
                        "prior_current_family"
                    ]["prior_family_packet_path"],
                    "effective_status_packet_path": stack["effective"][
                        "prior_current_family"
                    ]["prior_status_packet_path"],
                    "effective_current_governing_packet_path": stack["effective"][
                        "prior_current_family"
                    ]["prior_current_governing_packet_path"],
                    "effective_source_run_path": stack["current_entry"][
                        "source_run_directory_path"
                    ],
                    "effective_ingress_run_path": stack["current_entry"][
                        "matched_ingress_run_path"
                    ],
                }
            )
            result = self.resolve_object(temp_root, self.open_request(), stale)
            self.assert_blocked(
                result,
                "EFFECTIVE_OPEN_SURFACE_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
            )

        for non_claim_key, code in (
            ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
            ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
            ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
        ):
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_stack(temp_root, write_answer=False)
                    answer = self.copy(stack["answer"])
                    governing_path = self.display_path(
                        temp_root,
                        answer["effective_answer_read_inputs"][
                            "effective_current_governing_packet_path"
                        ],
                    )
                    governing = self.read_json(governing_path)
                    governing["non_claims"][non_claim_key] = True
                    self.write_json(governing_path, governing)
                    result = self.resolve_object(temp_root, self.open_request(), answer)
                    self.assert_blocked(
                        result,
                        code,
                        expect_false_non_claims=False,
                    )
                    self.assertTrue(result["non_claims"][non_claim_key])

    def test_multiple_current_state_answer_read_result_conflict_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root)
            conflict = self.copy(stack["answer"])
            conflict["answer_read_metadata"]["answer_read_result_id"] = (
                "conflicting_current_state_answer_read_for_open_surface"
            )
            self.write_json(
                temp_root
                / answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
                / "conflicting_current_state_answer_read_for_open_surface.json",
                conflict,
            )
            result = self.resolve_default(temp_root, self.open_request())
            self.assert_blocked(
                result,
                "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED",
            )

    def test_write_behavior_and_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_stack(temp_root, write_answer=False)
            result = self.resolve_object(temp_root, self.open_request(), stack["answer"])
            output_path = temp_root / "nested" / "open_surface" / "result.json"

            with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
                written = open_resolver.write_current_state_what_remains_open_result(
                    result,
                    output_path,
                )
            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            self.assertEqual(set(self.read_json(written)), TOP_LEVEL)

            with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(FileExistsError):
                    open_resolver.write_current_state_what_remains_open_result(
                        result,
                        output_path,
                    )

            with mock.patch.object(open_resolver, "_repo_root", return_value=temp_root):
                first = open_resolver.write_current_state_what_remains_open_result(
                    result
                )
                second = open_resolver.write_current_state_what_remains_open_result(
                    result
                )
            self.assertTrue(first.exists())
            self.assertTrue(second.exists())
            self.assertNotEqual(first, second)
            root = (
                temp_root / open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
            ).resolve()
            self.assertTrue(first.resolve().is_relative_to(root))
            self.assertTrue(second.resolve().is_relative_to(root))
            self.assertTrue(first.name.endswith("__current_state_what_remains_open_result.json"))
            self.assertTrue(
                second.name.endswith("__current_state_what_remains_open_result_001.json")
            )
            self.assertLess(len(first.name), 255)
            self.assertLess(len(second.name), 255)
            parsed = self.read_json(first)
            self.assertEqual(set(parsed), TOP_LEVEL)
            self.assertEqual(
                parsed["what_remains_open_metadata"][
                    "what_remains_open_result_version"
                ],
                open_resolver.WHAT_REMAINS_OPEN_RESULT_VERSION,
            )


if __name__ == "__main__":
    unittest.main()
