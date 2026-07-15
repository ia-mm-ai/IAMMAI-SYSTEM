"""Bounded tests for the v0-min current-work-input resolver.

These tests lock the current behavior of
``src/resolve_integrity_host_v0_min_coexistence_current_work_input.py``.
They use real local source runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, run-family packets, preserved-run
status packets, current-governing packets, governing-transition results,
governing re-resolution results, successor-adoption results, effective-family
resolutions, and effective-family consumption results emitted into temporary
roots.

The suite verifies resolution of explicit consumed effective-family inputs only.
It does not test replay, merge, persistence architecture, registry integration,
distributed continuity, CLI behavior, or broad governance/workflow frameworks.
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
import resolve_integrity_host_v0_min_coexistence_current_work_input as work_input_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_effective_family_consumption as consumption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_reresolution as reresolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_successor_adoption_v2 as adoption_resolver  # noqa: E402
import resolve_integrity_host_v0_min_coexistence_governing_transition as transition_resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "work_input_metadata",
    "selected_effective_family_consumption",
    "effective_work_inputs",
    "checks",
    "outcome",
    "block",
    "resolved_work_input_references",
    "work_input_summary",
    "non_claims",
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
}

WORK_INPUT_KEYS = {
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


class IntegrityHostV0MinCoexistenceCurrentWorkInputTests(unittest.TestCase):
    def emit_source_run(
        self,
        temp_root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, dict[str, Any]]:
        source_root = temp_root / resolver.SOURCE_RUNS_ROOT
        run_dir = source_root / run_name
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
        return run_dir, manifest

    def emit_ingress_run(
        self,
        temp_root: Path,
        source_run_dir: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
            manifest = ingress_runner.run_receiving_ingress_for_source_run(
                source_run_dir
            )
            output_dir = self.resolve_display_path(
                temp_root,
                manifest["ingress_run_metadata"]["output_run_directory"],
            )
            ingress_runner.write_ingress_run_manifest(
                manifest,
                output_dir / "manifest.json",
            )
        return output_dir, manifest

    def emit_comparison_artifact(
        self,
        temp_root: Path,
        source_run_dir: Path,
        ingress_run_dir: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
            comparison = comparer.compare_source_run_and_ingress_run(
                source_run_dir,
                ingress_run_dir,
            )
            output_path = (
                temp_root
                / resolver.SOURCE_INGRESS_COMPARISON_ROOT
                / f"{source_run_dir.name}__source_ingress_comparison.json"
            )
            comparer.write_comparison(comparison, output_path)
        return output_path, comparison

    def emit_authority_resolution(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
            resolution = resolver.resolve_current_execution_authority()
            output_path = resolver.write_resolution(resolution)
        return output_path, resolution

    def emit_family_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
            packet = family_builder.build_run_family_packet()
            output_path = family_builder.write_run_family_packet(packet)
        return output_path, packet

    def emit_status_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
            packet = status_builder.build_preserved_run_status_packet()
            output_path = status_builder.write_preserved_run_status_packet(packet)
        return output_path, packet

    def emit_governing_packet(
        self,
        temp_root: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
            packet = governing_builder.build_current_governing_packet()
            output_path = governing_builder.write_current_governing_packet(packet)
        return output_path, packet

    def emit_transition_result(
        self,
        temp_root: Path,
        proposal: dict[str, Any],
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(transition_resolver, "_repo_root", return_value=temp_root):
            result = transition_resolver.resolve_governing_transition(proposal)
            path = transition_resolver.write_governing_transition_result(result)
        return path, result

    def emit_reresolution_result_from_path(
        self,
        temp_root: Path,
        transition_path: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(reresolver, "_repo_root", return_value=temp_root):
            result = reresolver.resolve_governing_reresolution_from_path(
                transition_path
            )
        output_path = self.reresolution_result_path(temp_root, result)
        result = self.current_shape_reresolution_result(result)
        self.write_json(output_path, result)
        return output_path, result

    def emit_adoption_result_from_path(
        self,
        temp_root: Path,
        reresolution_path: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(adoption_resolver, "_repo_root", return_value=temp_root):
            result = adoption_resolver.resolve_governing_successor_adoption_from_path(
                reresolution_path
            )
            path = adoption_resolver.write_governing_successor_adoption_result(result)
        return path, result

    def emit_effective_family_result_from_object(
        self,
        temp_root: Path,
        adoption_result: dict[str, Any],
        *,
        write_artifact: bool = True,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(effective_resolver, "_repo_root", return_value=temp_root):
            result = effective_resolver.resolve_effective_current_family(
                adoption_result
            )
            path = (
                effective_resolver.write_effective_family_resolution(result)
                if write_artifact
                else None
            )
        return path, result

    def emit_consumption_result_from_object(
        self,
        temp_root: Path,
        effective_result: dict[str, Any],
        *,
        write_artifact: bool = True,
    ) -> tuple[Path | None, dict[str, Any]]:
        with mock.patch.object(
            consumption_resolver,
            "_repo_root",
            return_value=temp_root,
        ):
            result = consumption_resolver.resolve_effective_family_consumption(
                effective_result
            )
            path = (
                consumption_resolver.write_effective_family_consumption_result(result)
                if write_artifact
                else None
            )
        return path, result

    def build_multi_run_stack(
        self,
        temp_root: Path,
        *,
        write_effective_artifact: bool = True,
        write_consumption_artifact: bool = True,
    ) -> dict[str, Any]:
        first_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000000_000000Z",
        )
        first_ingress_run, _ = self.emit_ingress_run(temp_root, first_source_run)
        first_comparison_path, _ = self.emit_comparison_artifact(
            temp_root,
            first_source_run,
            first_ingress_run,
        )

        latest_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000001_000000Z",
        )
        latest_ingress_run, _ = self.emit_ingress_run(temp_root, latest_source_run)
        latest_comparison_path, _ = self.emit_comparison_artifact(
            temp_root,
            latest_source_run,
            latest_ingress_run,
        )

        authority_path, authority = self.emit_authority_resolution(temp_root)
        family_path, family = self.emit_family_packet(temp_root)
        status_path, status = self.emit_status_packet(temp_root)
        governing_path, governing = self.emit_governing_packet(temp_root)

        current_entry = governing["current_governing_run"]
        candidates = [
            entry
            for entry in status["preserved_run_status_entries"]
            if entry["status_role"] == status_builder.ROLE_ELIGIBLE_NON_AUTHORITY
        ]
        self.assertEqual(len(candidates), 1)

        proposal = self.valid_proposal(current_entry, candidates[0])
        transition_path, transition_result = self.emit_transition_result(
            temp_root,
            proposal,
        )
        self.assertEqual(
            transition_result["outcome"],
            transition_resolver.OUTCOME_ACCEPTED,
        )

        reresolution_path, reresolution_result = self.emit_reresolution_result_from_path(
            temp_root,
            transition_path,
        )
        self.assertEqual(
            reresolution_result["outcome"],
            reresolver.OUTCOME_SUCCESSOR_EMITTED,
        )

        adoption_path, adoption_result = self.emit_adoption_result_from_path(
            temp_root,
            reresolution_path,
        )
        self.assertEqual(adoption_result["outcome"], adoption_resolver.OUTCOME_ADOPTED)

        effective_path, effective_result = self.emit_effective_family_result_from_object(
            temp_root,
            adoption_result,
            write_artifact=write_effective_artifact,
        )
        self.assertEqual(
            effective_result["outcome"],
            effective_resolver.OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
        )

        consumption_path, consumption_result = self.emit_consumption_result_from_object(
            temp_root,
            effective_result,
            write_artifact=write_consumption_artifact,
        )
        self.assertEqual(
            consumption_result["outcome"],
            consumption_resolver.OUTCOME_CONSUMED,
        )

        return {
            "first_source_run": first_source_run,
            "first_ingress_run": first_ingress_run,
            "first_comparison_path": first_comparison_path,
            "latest_source_run": latest_source_run,
            "latest_ingress_run": latest_ingress_run,
            "latest_comparison_path": latest_comparison_path,
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
            "proposal": proposal,
            "transition_path": transition_path,
            "transition_result": transition_result,
            "reresolution_path": reresolution_path,
            "reresolution_result": reresolution_result,
            "adoption_path": adoption_path,
            "adoption_result": adoption_result,
            "effective_path": effective_path,
            "effective_result": effective_result,
            "consumption_path": consumption_path,
            "consumption_result": consumption_result,
        }

    def valid_proposal(
        self,
        current: dict[str, Any],
        candidate: dict[str, Any],
    ) -> dict[str, str]:
        return {
            "transition_proposal_id": "proposal_accepted_for_current_work_input",
            "current_governing_source_run_path": current[
                "source_run_directory_path"
            ],
            "candidate_successor_source_run_path": candidate[
                "source_run_directory_path"
            ],
            "current_governing_ingress_run_path": current[
                "matched_ingress_run_path"
            ],
            "candidate_successor_ingress_run_path": candidate[
                "matched_ingress_run_path"
            ],
            "current_governing_comparison_artifact_path": current[
                "matched_comparison_artifact_path"
            ],
            "candidate_successor_comparison_artifact_path": candidate[
                "matched_comparison_artifact_path"
            ],
            "proposal_basis_ref": "bounded explicit current-work-input test basis",
            "proposed_at": "2026-04-21T00:00:00Z",
            "proposed_by_surface": (
                "tests/test_resolve_integrity_host_v0_min_coexistence_current_work_input.py"
            ),
        }

    def resolve_work_input_default(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
            return work_input_resolver.resolve_current_work_input()

    def resolve_work_input_object(
        self,
        temp_root: Path,
        consumption_result: dict[str, Any],
    ) -> dict[str, Any]:
        with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
            return work_input_resolver.resolve_current_work_input(consumption_result)

    def resolve_work_input_from_path(
        self,
        temp_root: Path,
        consumption_path: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
            return work_input_resolver.resolve_current_work_input_from_path(
                consumption_path
            )

    def reresolution_result_path(
        self,
        temp_root: Path,
        result: dict[str, Any],
    ) -> Path:
        run_dir = self.resolve_display_path(
            temp_root,
            result["input_references"]["reresolution_run_directory_path"],
        )
        candidates = sorted(run_dir.glob("*_result.json"))
        self.assertEqual(len(candidates), 1)
        return candidates[0]

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

    def write_json(self, path: Path, payload: Any) -> Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n",
            encoding="utf-8",
        )
        return path

    def current_shape_reresolution_result(
        self,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        result = self.copy_payload(payload)
        self.assertIn("selected_transition_result", result)
        self.assertNotIn("selected_reresolution_result", result)
        selected = result["selected_transition_result"]
        self.assertTrue(selected is None or isinstance(selected, dict))
        return result

    def copy_payload(self, payload: Any) -> Any:
        return json.loads(json.dumps(payload, sort_keys=True))

    def resolve_display_path(self, repo_root: Path, value: str | Path) -> Path:
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

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_paths_same(self, temp_root: Path, left: str | Path, right: str | Path) -> None:
        self.assertEqual(
            self.resolve_display_path(temp_root, left),
            self.resolve_display_path(temp_root, right),
        )

    def assert_result_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(result["work_input_metadata"], dict)
        self.assertIsInstance(result["selected_effective_family_consumption"], dict)
        self.assertIsInstance(result["effective_work_inputs"], dict)
        self.assertIsInstance(result["checks"], list)
        self.assertIsInstance(result["block"], dict)
        self.assertIsInstance(result["resolved_work_input_references"], dict)
        self.assertIsInstance(result["work_input_summary"], dict)
        self.assertIsInstance(result["non_claims"], dict)

    def assert_non_claims_false(self, result: dict[str, Any]) -> None:
        for key in EXPECTED_NON_CLAIMS:
            self.assertIn(key, result["non_claims"])
            self.assertFalse(result["non_claims"][key])

    def assert_resolved_result(self, result: dict[str, Any]) -> None:
        self.assert_result_shape(result)
        self.assertEqual(
            result["outcome"],
            work_input_resolver.OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
        )
        self.assertIsNone(result["block"]["block_code"])
        self.assertIsNone(result["block"]["block_reason"])
        self.assertEqual(set(result["effective_work_inputs"]), WORK_INPUT_KEYS)
        self.assertEqual(set(result["resolved_work_input_references"]), WORK_INPUT_KEYS)
        for value in result["effective_work_inputs"].values():
            self.assert_non_empty_string(value)
        for value in result["resolved_work_input_references"].values():
            self.assert_non_empty_string(value)
        self.assert_non_claims_false(result)

    def assert_blocked_result(
        self,
        result: dict[str, Any],
        expected_code: str | None = None,
        *,
        expect_non_claims_false: bool = True,
    ) -> None:
        self.assert_result_shape(result)
        self.assertEqual(result["outcome"], work_input_resolver.OUTCOME_BLOCKED)
        self.assert_non_empty_string(result["block"]["block_code"])
        self.assert_non_empty_string(result["block"]["block_reason"])
        if expected_code is not None:
            self.assertEqual(result["block"]["block_code"], expected_code)
        for value in result["resolved_work_input_references"].values():
            self.assertIsNone(value)
        if expect_non_claims_false:
            self.assert_non_claims_false(result)

    def assert_work_inputs_match_consumption(
        self,
        temp_root: Path,
        result: dict[str, Any],
        consumption: dict[str, Any],
    ) -> None:
        for key in WORK_INPUT_KEYS:
            self.assert_paths_same(
                temp_root,
                result["effective_work_inputs"][key],
                consumption["effective_inputs"][key],
            )
            self.assert_paths_same(
                temp_root,
                result["resolved_work_input_references"][key],
                consumption["consumed_family_references"][key],
            )

    def assert_under_work_input_root(self, temp_root: Path, path: Path) -> None:
        root = (temp_root / work_input_resolver.CURRENT_WORK_INPUT_ROOT).resolve()
        try:
            path.resolve().relative_to(root)
        except ValueError as exc:
            self.fail(f"{path} was not written under {root}: {exc}")

    def parse_effective_family_files(
        self,
        temp_root: Path,
        result: dict[str, Any],
    ) -> dict[str, dict[str, Any]]:
        parsed: dict[str, dict[str, Any]] = {}
        for key in PATH_INPUT_KEYS:
            path = self.resolve_display_path(
                temp_root,
                result["effective_work_inputs"][key],
            )
            self.assertTrue(path.is_file(), key)
            parsed[key] = self.read_json(path)
        return parsed

    def test_real_resolved_current_work_input_default_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_work_input_default(temp_root)

            self.assert_resolved_result(result)
            selected = result["selected_effective_family_consumption"]
            self.assert_paths_same(
                temp_root,
                selected["consumption_result_artifact_path"],
                stack["consumption_path"],
            )
            self.assertEqual(
                selected["consumption_result_id"],
                stack["consumption_result"]["consumption_metadata"][
                    "consumption_result_id"
                ],
            )
            self.assertEqual(selected["outcome"], consumption_resolver.OUTCOME_CONSUMED)
            self.assertEqual(
                selected["selected_effective_family_resolution_id"],
                stack["effective_result"]["resolution_metadata"][
                    "effective_family_resolution_id"
                ],
            )
            self.assert_work_inputs_match_consumption(
                temp_root,
                result,
                stack["consumption_result"],
            )
            metadata = result["work_input_metadata"]
            for key in (
                "current_work_input_resolution_id",
                "current_work_input_resolution_type",
                "current_work_input_resolution_version",
                "generated_at",
                "resolver_module",
            ):
                self.assert_non_empty_string(metadata[key])

    def test_resolution_from_path_and_object_are_consistent(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            object_result = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )
            path_result = self.resolve_work_input_from_path(
                temp_root,
                stack["consumption_path"],
            )

            self.assert_resolved_result(object_result)
            self.assert_resolved_result(path_result)
            self.assertIsNone(
                object_result["selected_effective_family_consumption"][
                    "consumption_result_artifact_path"
                ]
            )
            self.assert_paths_same(
                temp_root,
                path_result["selected_effective_family_consumption"][
                    "consumption_result_artifact_path"
                ],
                stack["consumption_path"],
            )
            self.assertEqual(object_result["outcome"], path_result["outcome"])
            self.assertEqual(
                object_result["effective_work_inputs"],
                path_result["effective_work_inputs"],
            )
            self.assertEqual(
                object_result["resolved_work_input_references"],
                path_result["resolved_work_input_references"],
            )

    def test_discovery_helper_selects_latest_consumed_result(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            root = temp_root / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT
            root.mkdir(parents=True, exist_ok=True)
            (root / "unrelated.txt").write_text("ignored\n", encoding="utf-8")
            first_copy = self.write_json(
                root / "aaa_consumed_copy.json",
                stack["consumption_result"],
            )
            latest_copy = self.write_json(
                root / "zzz_consumed_copy.json",
                stack["consumption_result"],
            )

            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                selected = (
                    work_input_resolver.discover_latest_consumed_effective_family_result(
                        root
                    )
                )

            self.assertNotEqual(first_copy, latest_copy)
            self.assertEqual(selected, latest_copy)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    work_input_resolver.CurrentWorkInputResolutionError
                ):
                    work_input_resolver.discover_latest_consumed_effective_family_result(
                        temp_root / "missing"
                    )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            root_file = temp_root / "not_a_directory"
            root_file.write_text("not a directory\n", encoding="utf-8")
            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    work_input_resolver.CurrentWorkInputResolutionError
                ):
                    work_input_resolver.discover_latest_consumed_effective_family_result(
                        root_file
                    )

    def test_selected_consumption_inputs_checks_and_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )

            self.assert_resolved_result(result)
            self.assertGreater(len(result["checks"]), 0)
            for check in result["checks"]:
                self.assertIn("check", check)
                self.assertIn("passed", check)
                self.assertIn("required", check)
                self.assertIn("actual", check)
                self.assertIsInstance(check["check"], str)
                self.assertIsInstance(check["passed"], bool)
                self.assertTrue(check["passed"])

            summary = work_input_resolver.build_current_work_input_summary(result)
            for key in (
                "current_work_input_resolution_id",
                "outcome",
                "block_code",
                "block_reason",
                "selected_consumption_result_id",
                "effective_authority_artifact_path",
                "effective_family_packet_path",
                "effective_status_packet_path",
                "effective_current_governing_packet_path",
                "effective_source_run_path",
                "effective_ingress_run_path",
                "passed_check_count",
                "failed_check_count",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(
                summary["outcome"],
                work_input_resolver.OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
            )
            self.assertIsNone(summary["block_code"])
            self.assertIsNone(summary["block_reason"])
            self.assertEqual(
                summary["selected_consumption_result_id"],
                stack["consumption_result"]["consumption_metadata"][
                    "consumption_result_id"
                ],
            )
            self.assertGreater(summary["passed_check_count"], 0)
            self.assertEqual(summary["failed_check_count"], 0)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_resolved_references_and_semantics_preserve_prior_family(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            result = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )

            self.assert_resolved_result(result)
            self.assert_work_inputs_match_consumption(
                temp_root,
                result,
                stack["consumption_result"],
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
                    self.resolve_display_path(
                        temp_root,
                        result["resolved_work_input_references"][effective_key],
                    ),
                    self.resolve_display_path(
                        temp_root,
                        stack["effective_result"]["prior_current_family"][prior_key],
                    ),
                )

            parsed = self.parse_effective_family_files(temp_root, result)
            effective_status = parsed["effective_status_packet_path"]
            effective_governing = parsed["effective_current_governing_packet_path"]
            prior_source = stack["current_entry"]["source_run_directory_path"]
            successor_source = stack["candidate_entry"]["source_run_directory_path"]

            prior_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, prior_source)
            ]
            successor_entries = [
                entry
                for entry in effective_status["preserved_run_status_entries"]
                if self.resolve_display_path(
                    temp_root,
                    entry["source_run_directory_path"],
                )
                == self.resolve_display_path(temp_root, successor_source)
            ]
            self.assertEqual(len(prior_entries), 1)
            self.assertEqual(len(successor_entries), 1)
            self.assertEqual(
                prior_entries[0]["status_role"],
                status_builder.ROLE_ELIGIBLE_NON_AUTHORITY,
            )
            self.assertFalse(prior_entries[0]["current_authority"])
            self.assertEqual(
                successor_entries[0]["status_role"],
                status_builder.ROLE_CURRENT_AUTHORITY,
            )
            self.assertTrue(successor_entries[0]["current_authority"])
            self.assert_paths_same(
                temp_root,
                effective_governing["current_governing_run"][
                    "source_run_directory_path"
                ],
                successor_source,
            )
            self.assertTrue(
                result["work_input_summary"]["prior_family_remained_preserved"]
            )
            self.assertEqual(
                result["work_input_summary"]["consumed_current_family_basis"],
                effective_resolver.BASIS_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
            )

    def test_no_consumed_effective_family_result_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()

            result = self.resolve_work_input_default(temp_root)

            self.assert_blocked_result(result, "NO_CONSUMED_EFFECTIVE_FAMILY_RESULT")
            selected = result["selected_effective_family_consumption"]
            self.assertIsNone(selected["consumption_result_id"])
            self.assertIsNone(selected["outcome"])
            for value in result["resolved_work_input_references"].values():
                self.assertIsNone(value)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            blocked_consumption = self.copy_payload(stack["consumption_result"])
            blocked_consumption["outcome"] = consumption_resolver.OUTCOME_BLOCKED
            root = temp_root / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT
            self.write_json(root / "blocked_consumption.json", blocked_consumption)

            result = self.resolve_work_input_default(temp_root)

            self.assert_blocked_result(result, "NO_CONSUMED_EFFECTIVE_FAMILY_RESULT")

    def test_consumption_result_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            malformed_path = temp_root / "malformed_consumption_result.json"
            malformed_path.write_text("[1, 2, 3]\n", encoding="utf-8")

            with self.assertRaises(
                work_input_resolver.CurrentWorkInputResolutionError
            ):
                self.resolve_work_input_from_path(temp_root, malformed_path)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            blocked_consumption = self.copy_payload(stack["consumption_result"])
            blocked_consumption["outcome"] = consumption_resolver.OUTCOME_BLOCKED

            result = self.resolve_work_input_object(temp_root, blocked_consumption)

            self.assert_blocked_result(result, "CONSUMPTION_RESULT_NOT_CONSUMED")

    def test_consumed_family_artifact_unreadable_or_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            consumption = self.copy_payload(stack["consumption_result"])
            missing_path = self.resolve_display_path(
                temp_root,
                consumption["consumed_family_references"][
                    "effective_status_packet_path"
                ],
            )
            missing_path.unlink()

            result = self.resolve_work_input_object(temp_root, consumption)

            self.assert_blocked_result(
                result,
                "CONSUMED_FAMILY_ARTIFACT_UNREADABLE",
            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            consumption = self.copy_payload(stack["consumption_result"])
            malformed_path = self.resolve_display_path(
                temp_root,
                consumption["consumed_family_references"][
                    "effective_authority_artifact_path"
                ],
            )
            malformed_path.write_text("{not valid json\n", encoding="utf-8")

            with self.assertRaises(
                work_input_resolver.CurrentWorkInputResolutionError
            ):
                self.resolve_work_input_object(temp_root, consumption)

    def test_canonical_execution_line_mismatch_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            consumption = self.copy_payload(stack["consumption_result"])
            family_path = self.resolve_display_path(
                temp_root,
                consumption["consumed_family_references"][
                    "effective_family_packet_path"
                ],
            )
            family = self.read_json(family_path)
            family["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            self.write_json(family_path, family)

            result = self.resolve_work_input_object(temp_root, consumption)

            self.assert_blocked_result(result, "CANONICAL_EXECUTION_LINE_MISMATCH")

    def test_stale_prior_family_fallback_is_not_used(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )

            result = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )

            self.assert_resolved_result(result)
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
                    self.resolve_display_path(
                        temp_root,
                        result["resolved_work_input_references"][effective_key],
                    ),
                    self.resolve_display_path(
                        temp_root,
                        stack["effective_result"]["prior_current_family"][prior_key],
                    ),
                )

            stale = self.copy_payload(stack["consumption_result"])
            stale_refs = {
                "effective_authority_artifact_path": stack["effective_result"][
                    "prior_current_family"
                ]["prior_authority_artifact_path"],
                "effective_family_packet_path": stack["effective_result"][
                    "prior_current_family"
                ]["prior_family_packet_path"],
                "effective_status_packet_path": stack["effective_result"][
                    "prior_current_family"
                ]["prior_status_packet_path"],
                "effective_current_governing_packet_path": stack["effective_result"][
                    "prior_current_family"
                ]["prior_current_governing_packet_path"],
                "effective_source_run_path": stack["current_entry"][
                    "source_run_directory_path"
                ],
                "effective_ingress_run_path": stack["current_entry"][
                    "matched_ingress_run_path"
                ],
            }
            stale["consumed_family_references"] = stale_refs

            blocked = self.resolve_work_input_object(temp_root, stale)

            self.assert_blocked_result(
                blocked,
                "CONSUMED_FAMILY_DOES_NOT_CORRESPOND_TO_RESULT",
            )

    def test_non_claim_shortcuts_block_resolution(self) -> None:
        cases = (
            ("replayed_into_live_host", "REPLAY_SHORTCUT_REFUSED"),
            ("merged_into_local_state", "MERGE_SHORTCUT_REFUSED"),
            ("continuity_completed", "CONTINUITY_COMPLETION_SHORTCUT_REFUSED"),
            ("standing_upgraded", "SILENT_STANDING_UPGRADE_REFUSED"),
        )
        for non_claim_key, expected_code in cases:
            with self.subTest(non_claim_key=non_claim_key):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    stack = self.build_multi_run_stack(
                        temp_root,
                        write_consumption_artifact=False,
                    )
                    consumption = self.copy_payload(stack["consumption_result"])
                    governing_path = self.resolve_display_path(
                        temp_root,
                        consumption["consumed_family_references"][
                            "effective_current_governing_packet_path"
                        ],
                    )
                    governing = self.read_json(governing_path)
                    governing["non_claims"][non_claim_key] = True
                    self.write_json(governing_path, governing)

                    result = self.resolve_work_input_object(temp_root, consumption)

                    self.assert_blocked_result(
                        result,
                        expected_code,
                        expect_non_claims_false=False,
                    )
                    self.assertTrue(result["non_claims"][non_claim_key])

    def test_multiple_consumption_result_conflict_blocks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)
            conflict = self.copy_payload(stack["consumption_result"])
            conflict["consumption_metadata"]["consumption_result_id"] = (
                "conflicting_effective_family_consumption"
            )
            conflict["consumed_family_references"][
                "effective_current_governing_packet_path"
            ] = "artifacts/conflicting_effective_governing_packet.json"
            conflict_path = (
                temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT
                / "conflicting_effective_family_consumption.json"
            )
            self.write_json(conflict_path, conflict)

            result = self.resolve_work_input_default(temp_root)

            self.assert_blocked_result(
                result,
                "MULTIPLE_CONSUMPTION_RESULTS_CONFLICT_UNRESOLVED",
            )

    def test_hard_malformed_artifact_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            root_file = temp_root / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT
            root_file.parent.mkdir(parents=True, exist_ok=True)
            root_file.write_text("not a directory\n", encoding="utf-8")

            with self.assertRaises(
                work_input_resolver.CurrentWorkInputResolutionError
            ):
                self.resolve_work_input_default(temp_root)

        malformed_consumption_cases = (
            ("non_mapping_input", "not a mapping"),
            ("missing_effective_inputs", {"outcome": consumption_resolver.OUTCOME_CONSUMED}),
        )
        for label, payload in malformed_consumption_cases:
            with self.subTest(label=label):
                with tempfile.TemporaryDirectory() as temp_dir:
                    temp_root = Path(temp_dir).resolve()
                    with self.assertRaises(
                        work_input_resolver.CurrentWorkInputResolutionError
                    ):
                        with mock.patch.object(
                            work_input_resolver,
                            "_repo_root",
                            return_value=temp_root,
                        ):
                            work_input_resolver.resolve_current_work_input(
                                payload  # type: ignore[arg-type]
                            )

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            consumption = self.copy_payload(stack["consumption_result"])
            status_path = self.resolve_display_path(
                temp_root,
                consumption["consumed_family_references"][
                    "effective_status_packet_path"
                ],
            )
            status = self.read_json(status_path)
            status.pop("aggregate_status_counts", None)
            self.write_json(status_path, status)

            with self.assertRaises(
                work_input_resolver.CurrentWorkInputResolutionError
            ):
                self.resolve_work_input_object(temp_root, consumption)

    def test_write_behavior_and_default_output_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(
                temp_root,
                write_consumption_artifact=False,
            )
            result = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )
            output_path = temp_root / "nested" / "work_input" / "result.json"

            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                written = work_input_resolver.write_current_work_input_resolution(
                    result,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    work_input_resolver.CurrentWorkInputResolutionError
                ):
                    work_input_resolver.write_current_work_input_resolution(
                        result,
                        output_path,
                    )

            with mock.patch.object(work_input_resolver, "_repo_root", return_value=temp_root):
                default_first = work_input_resolver.write_current_work_input_resolution(
                    result
                )
                default_second = work_input_resolver.write_current_work_input_resolution(
                    result
                )

            self.assertTrue(default_first.exists())
            self.assertTrue(default_second.exists())
            self.assertNotEqual(default_first, default_second)
            self.assert_under_work_input_root(temp_root, default_first)
            self.assert_under_work_input_root(temp_root, default_second)
            self.assertIn(
                result["work_input_metadata"]["current_work_input_resolution_id"],
                default_first.name,
            )
            self.assertEqual(set(self.read_json(default_first)), EXPECTED_TOP_LEVEL_KEYS)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            stack = self.build_multi_run_stack(temp_root)

            roots = {
                "source": temp_root / resolver.SOURCE_RUNS_ROOT,
                "ingress": temp_root / resolver.INGRESS_RUNS_ROOT,
                "comparison": temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT,
                "authority": temp_root
                / effective_resolver.EXECUTION_AUTHORITY_RESOLUTION_ROOT,
                "family": temp_root / effective_resolver.RUN_FAMILY_PACKET_ROOT,
                "status": temp_root
                / effective_resolver.PRESERVED_RUN_STATUS_PACKET_ROOT,
                "governing": temp_root
                / effective_resolver.CURRENT_GOVERNING_PACKET_ROOT,
                "transition": temp_root
                / transition_resolver.GOVERNING_TRANSITION_RESULT_ROOT,
                "reresolution": temp_root / reresolver.GOVERNING_RERESOLUTION_ROOT,
                "adoption": temp_root
                / effective_resolver.GOVERNING_SUCCESSOR_ADOPTION_ROOT,
                "effective": temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_RESOLUTION_ROOT,
                "consumption": temp_root
                / consumption_resolver.EFFECTIVE_FAMILY_CONSUMPTION_ROOT,
            }
            before = {label: self.json_texts(root) for label, root in roots.items()}

            first = self.resolve_work_input_object(
                temp_root,
                stack["consumption_result"],
            )
            after_first = {
                label: self.json_texts(root) for label, root in roots.items()
            }
            second = self.resolve_work_input_from_path(
                temp_root,
                stack["consumption_path"],
            )
            after_second = {
                label: self.json_texts(root) for label, root in roots.items()
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["outcome"], second["outcome"])
            self.assertEqual(
                first["selected_effective_family_consumption"][
                    "consumption_result_id"
                ],
                second["selected_effective_family_consumption"][
                    "consumption_result_id"
                ],
            )
            self.assertEqual(first["effective_work_inputs"], second["effective_work_inputs"])
            self.assertEqual(
                first["resolved_work_input_references"],
                second["resolved_work_input_references"],
            )
            self.assertEqual(first["work_input_summary"], second["work_input_summary"])
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
