"""Bounded tests for the v0-min coexistence run-level receiving ingress runner.

These tests lock the current additive run-level receiving lane in
``src/run_integrity_host_v0_min_coexistence_receiving_ingress.py`` using real
source scenario artifacts emitted by the current local scenario runner.

They verify source-run discovery, manifest reading, per-scenario receiving
packet and ingress-decision emission, aggregate counts, bounded run status,
stdout summary, failure posture, and non-mutation of source artifacts. They do
not test replay, merge, persistence architecture, registry behavior,
distributed continuity, CLI argument parsing, or speculative successor
features.
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

import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "ingress_run_metadata",
    "source_run",
    "scenario_ingress_entries",
    "aggregate_counts",
    "run_status",
}

EXPECTED_SCENARIO_IDS = {
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
}

EXPECTED_COUNT_KEYS = {
    "scenario_count",
    "object_count",
    "open_object_count",
    "coexistence_relation_count",
    "hold_count",
    "transition_record_count",
    "refusal_count",
    "accepted_action_count",
    "refused_action_count",
    "validation_passed_scenario_count",
    "validation_failed_scenario_count",
    "ingress_accepted_scenario_count",
    "ingress_rejected_scenario_count",
}

EXPECTED_STATUS = {
    "all_packets_built": True,
    "all_packets_validated": True,
    "all_decisions_emitted": True,
    "continuity_completed": False,
    "standing_upgraded": False,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
}


class IntegrityHostV0MinCoexistenceReceivingIngressRunnerTests(unittest.TestCase):
    def emit_source_run(
        self,
        root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, dict[str, Any]]:
        run_dir = root / run_name
        run_dir.mkdir(parents=True, exist_ok=True)
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

    def resolve_display_path(self, repo_root: Path, value: str) -> Path:
        path = Path(value)
        if path.is_absolute():
            return path.resolve()
        return (repo_root / path).resolve()

    def run_ingress(self, temp_root: Path, source_run_dir: Path) -> dict[str, Any]:
        with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
            return ingress_runner.run_receiving_ingress_for_source_run(source_run_dir)

    def output_dir_for(self, temp_root: Path, manifest: dict[str, Any]) -> Path:
        return self.resolve_display_path(
            temp_root,
            manifest["ingress_run_metadata"]["output_run_directory"],
        )

    def source_texts(self, source_run_dir: Path) -> dict[str, str]:
        return {
            path.name: path.read_text(encoding="utf-8")
            for path in sorted(source_run_dir.glob("*.json"))
        }

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_manifest_shape(self, manifest: dict[str, Any]) -> None:
        self.assertEqual(set(manifest), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(manifest["ingress_run_metadata"], dict)
        self.assertIsInstance(manifest["source_run"], dict)
        self.assertIsInstance(manifest["scenario_ingress_entries"], list)
        self.assertIsInstance(manifest["aggregate_counts"], dict)
        self.assertIsInstance(manifest["run_status"], dict)

    def test_latest_source_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir).resolve()
            (root / "not_a_run").mkdir()
            (root / "run_20260420T000000_000000Z").mkdir()
            latest = root / "run_20260420T000001_000000Z"
            latest.mkdir()
            (root / "run_20260420T000002_000000Z.json").write_text(
                "{}\n",
                encoding="utf-8",
            )

            found = ingress_runner.find_latest_source_run_directory(root)

            self.assertEqual(found, latest.resolve())

            empty_root = root / "empty"
            empty_root.mkdir()
            with self.assertRaises(RuntimeError):
                ingress_runner.find_latest_source_run_directory(empty_root)

    def test_source_manifest_read_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            run_dir, _ = self.emit_source_run(temp_root / "source")

            manifest = ingress_runner.read_source_manifest(run_dir)

            for key in ("generated_at", "output_directory", "scenario_count", "scenarios"):
                self.assertIn(key, manifest)
            self.assertEqual(manifest["scenario_count"], len(scenario_runner.SCENARIOS))
            self.assertIsInstance(manifest["scenarios"], list)

            malformed_dir = temp_root / "malformed" / "run_20260420T000000_000000Z"
            malformed_dir.mkdir(parents=True)
            self.write_json(malformed_dir / "manifest.json", {"generated_at": "now"})
            with self.assertRaises(RuntimeError):
                ingress_runner.read_source_manifest(malformed_dir)

            missing_dir = temp_root / "missing" / "run_20260420T000000_000000Z"
            missing_dir.mkdir(parents=True)
            with self.assertRaises(RuntimeError):
                ingress_runner.read_source_manifest(missing_dir)

    def test_real_run_level_ingress_execution(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest = self.emit_source_run(temp_root / "source")

            manifest = self.run_ingress(temp_root, source_run_dir)

            self.assert_manifest_shape(manifest)
            self.assertEqual(
                len(manifest["scenario_ingress_entries"]),
                source_manifest["scenario_count"],
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    manifest["source_run"]["source_run_directory_path"],
                ),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    manifest["source_run"]["source_manifest_path"],
                ),
                (source_run_dir / "manifest.json").resolve(),
            )

    def test_scenario_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)

            scenario_ids = {
                entry["scenario_id"]
                for entry in manifest["scenario_ingress_entries"]
            }

            self.assertEqual(scenario_ids, EXPECTED_SCENARIO_IDS)

    def test_per_scenario_ingress_entry_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)

            for entry in manifest["scenario_ingress_entries"]:
                with self.subTest(scenario_id=entry["scenario_id"]):
                    self.assert_non_empty_string(entry["scenario_id"])
                    self.assert_non_empty_string(entry["scenario_name"])
                    self.assert_non_empty_string(entry["description"])
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            entry["source_artifact_path"],
                        ).exists()
                    )
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            entry["receiving_packet_path"],
                        ).exists()
                    )
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            entry["ingress_decision_path"],
                        ).exists()
                    )
                    self.assertIsInstance(entry["validation_passed"], bool)
                    self.assert_non_empty_string(entry["ingress_decision"])
                    self.assert_non_empty_string(entry["ingress_decision_reason"])
                    for key in (
                        "accepted_action_count",
                        "refused_action_count",
                        "object_count",
                        "open_object_count",
                        "coexistence_relation_count",
                        "hold_count",
                        "transition_record_count",
                        "refusal_count",
                    ):
                        self.assertIsInstance(entry[key], int)
                    self.assertIsInstance(entry["receiving_status"], dict)
                    self.assertIsInstance(entry["receiving_packet_summary"], dict)
                    self.assertIsInstance(entry["validation_summary"], dict)
                    self.assertIsInstance(entry["ingress_decision_summary"], dict)

    def test_aggregate_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)

            aggregate = manifest["aggregate_counts"]

            self.assertEqual(set(aggregate), EXPECTED_COUNT_KEYS)
            self.assertEqual(
                aggregate["scenario_count"],
                source_manifest["scenario_count"],
            )
            self.assertGreater(aggregate["object_count"], 0)
            self.assertGreater(aggregate["open_object_count"], 0)
            self.assertGreater(aggregate["coexistence_relation_count"], 0)
            self.assertGreater(aggregate["transition_record_count"], 0)
            self.assertGreater(aggregate["accepted_action_count"], 0)
            self.assertGreater(aggregate["refusal_count"], 0)
            self.assertEqual(aggregate["validation_failed_scenario_count"], 0)
            self.assertEqual(
                aggregate["validation_passed_scenario_count"],
                aggregate["scenario_count"],
            )
            self.assertEqual(aggregate["ingress_rejected_scenario_count"], 0)
            self.assertEqual(
                aggregate["ingress_accepted_scenario_count"],
                aggregate["scenario_count"],
            )

    def test_run_status_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)

            self.assertEqual(manifest["run_status"], EXPECTED_STATUS)

    def test_artifact_writing(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)
            output_dir = self.output_dir_for(temp_root, manifest)
            manifest_path = output_dir / "manifest.json"

            with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
                written_manifest = ingress_runner.write_ingress_run_manifest(
                    manifest,
                    manifest_path,
                )

            packet_files = sorted(output_dir.glob("*__receiving_packet.json"))
            decision_files = sorted(output_dir.glob("*__receiving_ingress_decision.json"))

            self.assertEqual(len(packet_files), source_manifest["scenario_count"])
            self.assertEqual(len(decision_files), source_manifest["scenario_count"])
            self.assertEqual(written_manifest, manifest_path)
            self.assertTrue(manifest_path.exists())
            for path in [*packet_files, *decision_files, manifest_path]:
                self.assertIsInstance(self.read_json(path), dict)

            with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
                with self.assertRaises(RuntimeError):
                    ingress_runner.write_ingress_run_manifest(manifest, manifest_path)

    def test_manifest_writing_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")
            manifest = self.run_ingress(temp_root, source_run_dir)
            output_path = temp_root / "nested" / "ingress" / "manifest.json"

            written = ingress_runner.write_ingress_run_manifest(manifest, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

    def test_main_runner_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_root = temp_root / ingress_runner.SOURCE_RUNS_ROOT
            self.emit_source_run(source_root)
            stdout = io.StringIO()

            with (
                mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stdout),
            ):
                ingress_runner.main()

            output = stdout.getvalue()

            self.assertIn("Source run directory:", output)
            self.assertIn("Scenarios processed: 5", output)
            self.assertIn("Validation passed scenarios: 5", output)
            self.assertIn("Ingress accepted scenarios: 5", output)
            self.assertIn("Total refusal count: 3", output)
            self.assertIn("Output run directory:", output)
            self.assertIn("Manifest:", output)

    def test_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()

            with self.assertRaises(RuntimeError):
                ingress_runner.find_latest_source_run_directory(temp_root / "empty")

            malformed_dir = temp_root / "malformed" / "run_20260420T000000_000000Z"
            malformed_dir.mkdir(parents=True)
            self.write_json(
                malformed_dir / "manifest.json",
                {
                    "generated_at": "now",
                    "output_directory": str(malformed_dir),
                    "scenario_count": 1,
                    "scenarios": [],
                },
            )
            with self.assertRaises(RuntimeError):
                ingress_runner.run_receiving_ingress_for_source_run(malformed_dir)

            missing_artifact_dir, missing_manifest = self.emit_source_run(
                temp_root / "missing_artifact"
            )
            missing_manifest["scenarios"][0]["file_path"] = str(
                missing_artifact_dir / "missing.json"
            )
            self.write_json(missing_artifact_dir / "manifest.json", missing_manifest)
            with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
                with self.assertRaises(RuntimeError):
                    ingress_runner.run_receiving_ingress_for_source_run(
                        missing_artifact_dir
                    )

            packet_failure_dir, _ = self.emit_source_run(temp_root / "packet_failure")
            with (
                mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root),
                mock.patch.object(
                    ingress_runner,
                    "build_receiving_packet",
                    side_effect=RuntimeError("forced packet build failure"),
                ),
            ):
                with self.assertRaises(RuntimeError):
                    ingress_runner.run_receiving_ingress_for_source_run(
                        packet_failure_dir
                    )

            validation_failure_dir, _ = self.emit_source_run(
                temp_root / "validation_failure"
            )
            with (
                mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root),
                mock.patch.object(
                    ingress_runner,
                    "validate_receiving_packet",
                    side_effect=ingress_runner.ReceivingPacketValidationError(
                        "forced validation failure"
                    ),
                ),
            ):
                with self.assertRaises(RuntimeError):
                    ingress_runner.run_receiving_ingress_for_source_run(
                        validation_failure_dir
                    )

            decision_failure_dir, _ = self.emit_source_run(
                temp_root / "decision_failure"
            )
            with (
                mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root),
                mock.patch.object(
                    ingress_runner,
                    "build_ingress_decision_from_packet_path",
                    side_effect=RuntimeError("forced decision failure"),
                ),
            ):
                with self.assertRaises(RuntimeError):
                    ingress_runner.run_receiving_ingress_for_source_run(
                        decision_failure_dir
                    )

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")
            before = self.source_texts(source_run_dir)

            first_manifest = self.run_ingress(temp_root, source_run_dir)
            after_first = self.source_texts(source_run_dir)
            second_manifest = self.run_ingress(temp_root, source_run_dir)
            after_second = self.source_texts(source_run_dir)

            first_output_dir = self.output_dir_for(temp_root, first_manifest)
            second_output_dir = self.output_dir_for(temp_root, second_manifest)

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertNotEqual(first_output_dir, second_output_dir)
            self.assertTrue(first_output_dir.exists())
            self.assertTrue(second_output_dir.exists())


if __name__ == "__main__":
    unittest.main()
