"""Bounded tests for the v0-min coexistence scenario runner.

These tests lock the current artifact-emission behavior in
``src/run_integrity_host_v0_min_coexistence_scenarios.py``. They verify the
fixed scenario set, per-scenario snapshot artifacts, manifest construction,
temporary file emission, stdout summary, overwrite refusal, and fresh-host
posture.

They do not test replay/import, registry integration, persistence
architecture, distributed behavior, cross-host continuity, CLI argument
parsing, artifact diffing, or broader workflow orchestration.
"""

from __future__ import annotations

import contextlib
import io
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

import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_SCENARIO_STEMS = [
    "01_lawful_distinct_matter_coexistence",
    "02_refused_missing_coexistence_basis",
    "03_evolve_under_coexistence",
    "04_hold_blocks_one_target_while_another_proceeds",
    "05_same_matter_post_resolution_refusal",
]

EXPECTED_SCENARIO_IDS = [
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
]

EXPECTED_REFUSED_COUNTS = {
    "lawful_distinct_matter_coexistence": 0,
    "refused_missing_coexistence_basis": 1,
    "evolve_under_coexistence": 0,
    "hold_blocks_one_target_while_another_proceeds": 1,
    "same_matter_post_resolution_refusal": 1,
}


class IntegrityHostV0MinCoexistenceScenarioRunnerTests(unittest.TestCase):
    def scenario_result(self, scenario_id: str) -> runner.ScenarioResult:
        for _, scenario_function in runner.SCENARIOS:
            result = scenario_function()
            if result.scenario_id == scenario_id:
                return result
        self.fail(f"Scenario not found: {scenario_id}")

    def scenario_artifact(self, scenario_id: str) -> dict[str, Any]:
        return runner._build_scenario_artifact(self.scenario_result(scenario_id))

    def objects_by_id(self, snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
        return {obj["object_id"]: obj for obj in snapshot["objects"]}

    def assert_record_order_matches_actions(self, artifact: dict[str, Any]) -> None:
        actions = artifact["scenario"]["action_results"]
        records = artifact["snapshot"]["transition_records"]
        self.assertEqual(
            [record["record_id"] for record in records],
            [action["record_id"] for action in actions],
        )

    def test_output_directory_allocation_is_fresh_and_local(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            stamp = "20260420T000000_000000Z"
            with (
                mock.patch.object(runner, "_repo_root", return_value=temp_root),
                mock.patch.object(runner, "_utc_path_stamp", return_value=stamp),
            ):
                first = runner._make_output_dir()
                sentinel = first / "sentinel.json"
                sentinel.write_text('{"prior": true}\n', encoding="utf-8")
                second = runner._make_output_dir()

            expected_root = temp_root / runner.ARTIFACT_ROOT
            self.assertEqual(first.parent, expected_root)
            self.assertEqual(second.parent, expected_root)
            self.assertEqual(first.name, f"run_{stamp}")
            self.assertEqual(second.name, f"run_{stamp}_001")
            self.assertTrue(first.is_dir())
            self.assertTrue(second.is_dir())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), '{"prior": true}\n')

    def test_scenario_artifact_build_shape_preserves_snapshot(self) -> None:
        artifact = self.scenario_artifact("lawful_distinct_matter_coexistence")

        self.assertEqual(set(artifact), {"scenario", "snapshot"})
        scenario = artifact["scenario"]
        snapshot = artifact["snapshot"]

        for key in (
            "scenario_id",
            "scenario_name",
            "description",
            "generated_at",
            "accepted_action_count",
            "refused_action_count",
            "action_results",
        ):
            self.assertIn(key, scenario)
        self.assertEqual(scenario["scenario_id"], "lawful_distinct_matter_coexistence")
        self.assertTrue(scenario["scenario_name"])
        self.assertTrue(scenario["description"])
        self.assertEqual(
            scenario["accepted_action_count"],
            sum(1 for action in scenario["action_results"] if action["accepted"]),
        )
        self.assertEqual(
            scenario["refused_action_count"],
            sum(1 for action in scenario["action_results"] if not action["accepted"]),
        )

        self.assertEqual(
            set(snapshot),
            {
                "metadata",
                "host",
                "objects",
                "coexistence_relations",
                "holds",
                "transition_records",
            },
        )
        self.assertGreater(len(snapshot["objects"]), 0)
        self.assertGreater(len(snapshot["transition_records"]), 0)
        self.assert_record_order_matches_actions(artifact)

    def test_canonical_scenario_coverage_is_fixed(self) -> None:
        self.assertEqual([stem for stem, _ in runner.SCENARIOS], EXPECTED_SCENARIO_STEMS)

        results = [scenario_function() for _, scenario_function in runner.SCENARIOS]
        self.assertEqual([result.scenario_id for result in results], EXPECTED_SCENARIO_IDS)
        self.assertEqual(len(results), 5)

        host_ids = [runner.build_snapshot(result.host)["host"]["host_id"] for result in results]
        self.assertEqual(len(set(host_ids)), len(host_ids))

    def test_each_scenario_executes_and_can_be_snapshotted(self) -> None:
        for _, scenario_function in runner.SCENARIOS:
            with self.subTest(scenario_function=scenario_function.__name__):
                result = scenario_function()
                self.assertTrue(result.scenario_id)
                self.assertTrue(result.scenario_name)
                self.assertTrue(result.description)
                self.assertIsNotNone(result.host)
                self.assertTrue(result.action_results)

                refused_count = sum(
                    1 for action in result.action_results if not action["accepted"]
                )
                accepted_count = sum(
                    1 for action in result.action_results if action["accepted"]
                )
                self.assertGreater(accepted_count, 0)
                self.assertEqual(
                    refused_count,
                    EXPECTED_REFUSED_COUNTS[result.scenario_id],
                )

                snapshot = runner.build_snapshot(result.host)
                self.assertIn("objects", snapshot)
                self.assertIn("transition_records", snapshot)
                self.assertEqual(
                    len(snapshot["transition_records"]),
                    len(result.action_results),
                )

    def test_lawful_distinct_matter_coexistence_artifact(self) -> None:
        artifact = self.scenario_artifact("lawful_distinct_matter_coexistence")
        snapshot = artifact["snapshot"]

        self.assertEqual(len(snapshot["objects"]), 2)
        by_matter = {obj["matter_ref"]: obj for obj in snapshot["objects"]}
        self.assertEqual(by_matter["matter-a"]["phase_state"], "STANDING")
        self.assertEqual(by_matter["matter-a"]["occurrence_ref"], "occurrence-a")
        self.assertIsNone(by_matter["matter-a"]["resolution_type"])
        self.assertEqual(by_matter["matter-b"]["phase_state"], "PRESENT")
        self.assertEqual(by_matter["matter-b"]["occurrence_ref"], "occurrence-b")
        self.assertIsNone(by_matter["matter-b"]["resolution_type"])

        relations = snapshot["coexistence_relations"]
        self.assertEqual(len(relations), 1)
        self.assertEqual(relations[0]["relation_type"], "DISTINCT_MATTER_COHOSTED")
        self.assertEqual(relations[0]["basis_ref"], "cohost-a-b")
        self.assertEqual(len(snapshot["transition_records"]), 5)
        self.assert_record_order_matches_actions(artifact)

    def test_refused_missing_coexistence_basis_artifact(self) -> None:
        artifact = self.scenario_artifact("refused_missing_coexistence_basis")
        snapshot = artifact["snapshot"]
        refused_actions = [
            action
            for action in artifact["scenario"]["action_results"]
            if not action["accepted"]
        ]

        self.assertEqual(len(snapshot["objects"]), 1)
        self.assertEqual(snapshot["objects"][0]["matter_ref"], "matter-a")
        self.assertEqual(len(refused_actions), 1)
        self.assertEqual(
            refused_actions[0]["refusal_code"],
            "UNRESOLVED_COHOST_RELATION_REQUIRED",
        )

        refusal_record = snapshot["transition_records"][-1]
        self.assertFalse(refusal_record["accepted"])
        self.assertEqual(
            refusal_record["refusal_code"],
            "UNRESOLVED_COHOST_RELATION_REQUIRED",
        )
        self.assertEqual(refusal_record["action_type"], "CREATE_OBJECT")
        self.assertEqual(snapshot["coexistence_relations"], [])

    def test_evolve_under_coexistence_artifact(self) -> None:
        artifact = self.scenario_artifact("evolve_under_coexistence")
        snapshot = artifact["snapshot"]
        objects_by_id = self.objects_by_id(snapshot)

        evolved = [
            obj for obj in snapshot["objects"] if obj["resolution_type"] == "EVOLVE"
        ]
        self.assertEqual(len(evolved), 1)
        predecessor = evolved[0]
        successors = [
            obj
            for obj in snapshot["objects"]
            if obj["predecessor_object_id"] == predecessor["object_id"]
        ]
        self.assertEqual(len(successors), 1)
        successor = successors[0]

        self.assertEqual(predecessor["phase_state"], "STANDING")
        self.assertNotIn(predecessor["object_id"], snapshot["host"]["open_object_ids"])
        self.assertEqual(successor["phase_state"], "CANDIDATE")
        self.assertIsNone(successor["resolution_type"])
        self.assertIn(successor["object_id"], snapshot["host"]["open_object_ids"])
        self.assertIn("matter-b", {obj["matter_ref"] for obj in objects_by_id.values()})

        self.assertEqual(len(snapshot["coexistence_relations"]), 2)
        evolve_record = snapshot["transition_records"][-1]
        self.assertEqual(evolve_record["action_type"], "EVOLVE")
        self.assertEqual(evolve_record["predecessor_object_id"], predecessor["object_id"])
        self.assertEqual(evolve_record["successor_object_id"], successor["object_id"])
        self.assertEqual(evolve_record["target_resolution_type"], "EVOLVE")
        self.assertEqual(len(evolve_record["created_coexistence_relations"]), 1)

    def test_hold_scenario_artifact(self) -> None:
        artifact = self.scenario_artifact(
            "hold_blocks_one_target_while_another_proceeds"
        )
        snapshot = artifact["snapshot"]
        objects = self.objects_by_id(snapshot)

        holds = snapshot["holds"]
        self.assertEqual(len(holds), 1)
        held_id = holds[0]["target_object_id"]
        self.assertTrue(holds[0]["active"])
        self.assertEqual(holds[0]["basis_ref"], "hold-a")

        blocked_records = [
            record
            for record in snapshot["transition_records"]
            if record["action_type"] == "STAND"
            and not record["accepted"]
            and record["refusal_code"] == "HOLD_BLOCKS_TRANSITION"
        ]
        accepted_stands = [
            record
            for record in snapshot["transition_records"]
            if record["action_type"] == "STAND" and record["accepted"]
        ]

        self.assertEqual(len(blocked_records), 1)
        self.assertEqual(blocked_records[0]["object_id"], held_id)
        self.assertEqual(len(accepted_stands), 1)
        self.assertNotEqual(accepted_stands[0]["object_id"], held_id)

        self.assertEqual(objects[held_id]["phase_state"], "PRESENT")
        self.assertIsNone(objects[held_id]["resolution_type"])
        self.assertNotIn("HOLD", {obj["phase_state"] for obj in objects.values()})
        self.assertNotIn(
            "HOLD",
            {obj["resolution_type"] for obj in objects.values() if obj["resolution_type"]},
        )

    def test_same_matter_post_resolution_refusal_artifact(self) -> None:
        artifact = self.scenario_artifact("same_matter_post_resolution_refusal")
        snapshot = artifact["snapshot"]

        self.assertEqual(len(snapshot["objects"]), 1)
        obj = snapshot["objects"][0]
        self.assertEqual(obj["matter_ref"], "matter-a")
        self.assertEqual(obj["phase_state"], "STANDING")
        self.assertEqual(obj["resolution_type"], "FINALIZE")
        self.assertIsNotNone(obj["resolved_by_record_id"])
        self.assertNotIn(obj["object_id"], snapshot["host"]["open_object_ids"])

        refused_actions = [
            action
            for action in artifact["scenario"]["action_results"]
            if not action["accepted"]
        ]
        self.assertEqual(len(refused_actions), 1)
        self.assertEqual(
            refused_actions[0]["refusal_code"],
            "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
        )

        refusal_record = snapshot["transition_records"][-1]
        self.assertFalse(refusal_record["accepted"])
        self.assertEqual(
            refusal_record["refusal_code"],
            "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
        )
        self.assertEqual(
            len([item for item in snapshot["objects"] if item["matter_ref"] == "matter-a"]),
            1,
        )

    def test_manifest_build_shape(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "scenario-output"
            emitted = (
                runner.EmittedScenario(
                    scenario_id="alpha",
                    scenario_name="Alpha",
                    description="First emitted artifact",
                    artifact_path=output_dir / "alpha.json",
                ),
                runner.EmittedScenario(
                    scenario_id="beta",
                    scenario_name="Beta",
                    description="Second emitted artifact",
                    artifact_path=output_dir / "beta.json",
                ),
            )
            manifest = runner._build_manifest(output_dir, emitted)

        self.assertEqual(
            set(manifest),
            {"generated_at", "output_directory", "scenario_count", "scenarios"},
        )
        self.assertTrue(manifest["generated_at"])
        self.assertTrue(manifest["output_directory"])
        self.assertEqual(manifest["scenario_count"], 2)
        self.assertEqual(len(manifest["scenarios"]), 2)
        for entry in manifest["scenarios"]:
            self.assertEqual(
                set(entry),
                {"scenario_id", "scenario_name", "description", "file_path"},
            )
            self.assertTrue(entry["scenario_id"])
            self.assertTrue(entry["scenario_name"])
            self.assertTrue(entry["file_path"])

    def test_file_writing_emits_json_artifacts_and_manifest(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "nested" / "scenario-artifacts"
            emitted = tuple(
                runner._emit_scenario(output_dir, file_stem, scenario_function)
                for file_stem, scenario_function in runner.SCENARIOS
            )
            manifest_path = output_dir / "manifest.json"
            runner._write_json(manifest_path, runner._build_manifest(output_dir, emitted))

            scenario_files = [
                path for path in output_dir.glob("*.json") if path.name != "manifest.json"
            ]
            self.assertEqual(len(scenario_files), len(runner.SCENARIOS))
            self.assertTrue(manifest_path.exists())

            for emitted_scenario in emitted:
                self.assertTrue(emitted_scenario.artifact_path.exists())
                parsed = json.loads(
                    emitted_scenario.artifact_path.read_text(encoding="utf-8")
                )
                self.assertEqual(set(parsed), {"scenario", "snapshot"})
                self.assertIn("transition_records", parsed["snapshot"])

            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            self.assertEqual(manifest["scenario_count"], len(runner.SCENARIOS))
            self.assertEqual(len(manifest["scenarios"]), len(runner.SCENARIOS))

    def test_stdout_summary_from_main(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            stream = io.StringIO()
            with (
                mock.patch.object(runner, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stream),
            ):
                runner.main()

            output = stream.getvalue()
            artifact_root = temp_root / runner.ARTIFACT_ROOT
            run_dirs = [path for path in artifact_root.iterdir() if path.is_dir()]

        self.assertEqual(len(run_dirs), 1)
        self.assertIn("Output directory:", output)
        self.assertIn(f"Scenarios emitted: {len(runner.SCENARIOS)}", output)
        for scenario_id in EXPECTED_SCENARIO_IDS:
            self.assertIn(scenario_id, output)
        self.assertIn("Manifest:", output)

    def test_non_mutation_and_overwrite_refusal_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            prior_dir = temp_root / runner.ARTIFACT_ROOT / "prior_run"
            prior_dir.mkdir(parents=True)
            prior_file = prior_dir / "prior.json"
            prior_file.write_text('{"prior": true}\n', encoding="utf-8")

            with (
                mock.patch.object(runner, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(io.StringIO()),
            ):
                runner.main()

            self.assertEqual(prior_file.read_text(encoding="utf-8"), '{"prior": true}\n')
            run_dirs = [
                path
                for path in (temp_root / runner.ARTIFACT_ROOT).iterdir()
                if path.is_dir()
            ]
            self.assertEqual(len(run_dirs), 2)

            existing = temp_root / "already-there.json"
            existing.write_text('{"kept": true}\n', encoding="utf-8")
            with self.assertRaises(RuntimeError):
                runner._write_json(existing, {"replacement": True})
            self.assertEqual(existing.read_text(encoding="utf-8"), '{"kept": true}\n')

        results = [scenario_function() for _, scenario_function in runner.SCENARIOS]
        host_ids = [
            runner.build_snapshot(result.host)["host"]["host_id"] for result in results
        ]
        self.assertEqual(len(set(host_ids)), len(host_ids))
        self.assertEqual(
            len({id(result.host) for result in results}),
            len(results),
        )


if __name__ == "__main__":
    unittest.main()
