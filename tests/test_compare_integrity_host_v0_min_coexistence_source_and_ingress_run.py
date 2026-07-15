"""Bounded tests for the v0-min coexistence source-to-ingress comparison runner.

These tests lock the current additive comparison surface in
``src/compare_integrity_host_v0_min_coexistence_source_and_ingress_run.py``
using real source scenario runs and real run-level receiving-ingress outputs.

They verify discovery, manifest reads, source/ingress correspondence, clean
comparison, scenario and aggregate comparison shape, mismatch visibility,
stdout summary, write behavior, clear failures, and non-mutation. They do not
test replay, merge, persistence architecture, registry behavior, distributed
continuity, CLI argument parsing, broad recursive diffing, or speculative
successor features.
"""

from __future__ import annotations

import contextlib
import copy
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

import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "comparison_metadata",
    "source_run",
    "ingress_run",
    "scenario_comparisons",
    "aggregate_comparison",
    "all_matched",
}

EXPECTED_SCENARIO_IDS = {
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
}

BASE_COUNT_KEYS = {
    "accepted_action_count",
    "refused_action_count",
    "object_count",
    "open_object_count",
    "coexistence_relation_count",
    "hold_count",
    "transition_record_count",
    "refusal_count",
}

NON_CLAIM_KEYS = {
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
}


class IntegrityHostV0MinCoexistenceSourceIngressComparisonTests(unittest.TestCase):
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

    def emit_ingress_run(
        self,
        temp_root: Path,
        source_run_dir: Path,
    ) -> tuple[Path, dict[str, Any]]:
        with mock.patch.object(ingress_runner, "_repo_root", return_value=temp_root):
            manifest = ingress_runner.run_receiving_ingress_for_source_run(source_run_dir)
            output_dir = self.resolve_display_path(
                temp_root,
                manifest["ingress_run_metadata"]["output_run_directory"],
            )
            ingress_runner.write_ingress_run_manifest(
                manifest,
                output_dir / "manifest.json",
            )
        return output_dir, manifest

    def compare(
        self,
        temp_root: Path,
        source_run_dir: Path,
        ingress_run_dir: Path,
    ) -> dict[str, Any]:
        with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
            return comparer.compare_source_run_and_ingress_run(
                source_run_dir,
                ingress_run_dir,
            )

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

    def json_texts(self, root: Path) -> dict[str, str]:
        return {
            str(path.relative_to(root)): path.read_text(encoding="utf-8")
            for path in sorted(root.rglob("*.json"))
        }

    def build_pair(self, temp_root: Path) -> tuple[Path, dict[str, Any], Path, dict[str, Any]]:
        source_run_dir, source_manifest = self.emit_source_run(temp_root / "source")
        ingress_run_dir, ingress_manifest = self.emit_ingress_run(
            temp_root,
            source_run_dir,
        )
        return source_run_dir, source_manifest, ingress_run_dir, ingress_manifest

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_comparison_shape(self, comparison: dict[str, Any]) -> None:
        self.assertEqual(set(comparison), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(comparison["comparison_metadata"], dict)
        self.assertIsInstance(comparison["source_run"], dict)
        self.assertIsInstance(comparison["ingress_run"], dict)
        self.assertIsInstance(comparison["scenario_comparisons"], list)
        self.assertIsInstance(comparison["aggregate_comparison"], dict)
        self.assertIsInstance(comparison["all_matched"], bool)

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

            found = comparer.find_latest_source_run_directory(root)

            self.assertEqual(found, latest.resolve())

            empty = root / "empty"
            empty.mkdir()
            with self.assertRaises(RuntimeError):
                comparer.find_latest_source_run_directory(empty)

    def test_latest_ingress_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir).resolve()
            (root / "unrelated").mkdir()
            (root / "run_20260420T000000_000000Z").mkdir()
            latest = root / "run_20260420T000001_000000Z"
            latest.mkdir()
            (root / "run_20260420T999999_000000Z.json").write_text(
                "{}\n",
                encoding="utf-8",
            )

            found = comparer.find_latest_ingress_run_directory(root)

            self.assertEqual(found, latest.resolve())

            empty = root / "empty"
            empty.mkdir()
            with self.assertRaises(RuntimeError):
                comparer.find_latest_ingress_run_directory(empty)

    def test_source_manifest_read_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root / "source")

            manifest = comparer.read_source_manifest(source_run_dir)

            for key in ("generated_at", "output_directory", "scenario_count", "scenarios"):
                self.assertIn(key, manifest)
            self.assertEqual(manifest["scenario_count"], len(scenario_runner.SCENARIOS))

            malformed = temp_root / "malformed" / "run_20260420T000000_000000Z"
            malformed.mkdir(parents=True)
            self.write_json(malformed / "manifest.json", {"generated_at": "now"})
            with self.assertRaises(RuntimeError):
                comparer.read_source_manifest(malformed)

            missing = temp_root / "missing" / "run_20260420T000000_000000Z"
            missing.mkdir(parents=True)
            with self.assertRaises(RuntimeError):
                comparer.read_source_manifest(missing)

    def test_ingress_manifest_read_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _ = self.build_pair(temp_root)

            manifest = comparer.read_ingress_manifest(ingress_run_dir)

            for key in (
                "ingress_run_metadata",
                "source_run",
                "scenario_ingress_entries",
                "aggregate_counts",
                "run_status",
            ):
                self.assertIn(key, manifest)
            self.assertEqual(
                manifest["source_run"]["source_scenario_count"],
                len(scenario_runner.SCENARIOS),
            )
            self.assertTrue(source_run_dir.exists())

            malformed = temp_root / "malformed_ingress" / "run_20260420T000000_000000Z"
            malformed.mkdir(parents=True)
            self.write_json(malformed / "manifest.json", {"source_run": {}})
            with self.assertRaises(RuntimeError):
                comparer.read_ingress_manifest(malformed)

            missing = temp_root / "missing_ingress" / "run_20260420T000000_000000Z"
            missing.mkdir(parents=True)
            with self.assertRaises(RuntimeError):
                comparer.read_ingress_manifest(missing)

    def test_source_ingress_correspondence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, ingress_manifest = self.build_pair(
                temp_root
            )

            clean = self.compare(temp_root, source_run_dir, ingress_run_dir)

            self.assertTrue(clean["all_matched"])

            other_source, _ = self.emit_source_run(
                temp_root / "other_source",
                "run_20260420T000001_000000Z",
            )
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, other_source, ingress_run_dir)

            bad_manifest = copy.deepcopy(ingress_manifest)
            bad_manifest["source_run"]["source_manifest_path"] = str(
                source_run_dir / "not_manifest.json"
            )
            self.write_json(ingress_run_dir / "manifest.json", bad_manifest)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

    def test_real_source_to_ingress_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest, ingress_run_dir, _ = self.build_pair(
                temp_root
            )

            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)

            self.assert_comparison_shape(comparison)
            self.assertEqual(
                len(comparison["scenario_comparisons"]),
                source_manifest["scenario_count"],
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    comparison["source_run"]["source_run_directory_path"],
                ),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    comparison["ingress_run"]["ingress_run_directory_path"],
                ),
                ingress_run_dir.resolve(),
            )

    def test_scenario_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _ = self.build_pair(temp_root)
            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)

            scenario_ids = {
                scenario["scenario_id"]
                for scenario in comparison["scenario_comparisons"]
            }

            self.assertEqual(scenario_ids, EXPECTED_SCENARIO_IDS)

    def test_per_scenario_comparison_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _ = self.build_pair(temp_root)
            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)

            for scenario in comparison["scenario_comparisons"]:
                with self.subTest(scenario_id=scenario["scenario_id"]):
                    self.assert_non_empty_string(scenario["scenario_id"])
                    self.assert_non_empty_string(scenario["scenario_name"])
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            scenario["source_artifact_path"],
                        ).exists()
                    )
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            scenario["ingress_receiving_packet_path"],
                        ).exists()
                    )
                    self.assertTrue(
                        self.resolve_display_path(
                            temp_root,
                            scenario["ingress_decision_path"],
                        ).exists()
                    )
                    self.assertIsInstance(scenario["matched"], bool)
                    self.assertIsInstance(scenario["mismatches"], list)

                    counts = scenario["counts"]
                    for key in BASE_COUNT_KEYS:
                        self.assertIn(key, counts)
                        self.assertIn("source", counts[key])
                        self.assertIn("ingress", counts[key])
                        self.assertIn("matched", counts[key])
                    self.assertIn("resolved_object_count", counts)
                    self.assertIn("successor_object_count", counts)
                    self.assertIn("evolve_record_count", counts)

                    visibility = scenario["visibility"]
                    for key in (
                        "source_artifact_path_visible",
                        "receiving_packet_path_present",
                        "ingress_decision_path_present",
                        "validation_summary_present",
                        "ingress_decision_summary_present",
                        "receiving_status_present",
                        "refusal_visibility_preserved",
                        "lineage_visibility_preserved",
                    ):
                        self.assertIn(key, visibility)
                        self.assertIn("matched", visibility[key])

                    non_claims = scenario["non_claims"]
                    for key in NON_CLAIM_KEYS:
                        self.assertIn(key, non_claims)
                        self.assertFalse(non_claims[key]["expected"])
                        self.assertTrue(non_claims[key]["matched"])

    def test_aggregate_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest, ingress_run_dir, _ = self.build_pair(
                temp_root
            )
            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)

            aggregate = comparison["aggregate_comparison"]

            self.assertIn("source_totals", aggregate)
            self.assertIn("ingress_totals", aggregate)
            self.assertIn("counts_match", aggregate)
            self.assertIn("aggregate_match", aggregate)
            self.assertIn("mismatches", aggregate)
            self.assertIn("counts", aggregate)
            self.assertEqual(
                aggregate["source_totals"]["scenario_count"],
                source_manifest["scenario_count"],
            )
            self.assertEqual(
                aggregate["ingress_totals"]["scenario_count"],
                source_manifest["scenario_count"],
            )
            for key in BASE_COUNT_KEYS:
                self.assertIn(key, aggregate["source_totals"])
                self.assertIn(key, aggregate["ingress_totals"])
            for key in (
                "validation_passed_scenario_count",
                "validation_failed_scenario_count",
                "ingress_accepted_scenario_count",
                "ingress_rejected_scenario_count",
            ):
                self.assertIn(key, aggregate["ingress_totals"])
            self.assertTrue(aggregate["counts_match"])
            self.assertTrue(aggregate["aggregate_match"])
            self.assertTrue(comparison["all_matched"])

    def test_comparison_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _ = self.build_pair(temp_root)
            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)
            output_path = temp_root / "comparisons" / "nested" / "comparison.json"

            with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
                written = comparer.write_comparison(comparison, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(comparer, "_repo_root", return_value=temp_root):
                with self.assertRaises(RuntimeError):
                    comparer.write_comparison(comparison, output_path)

    def test_main_runner_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_root = temp_root / comparer.SOURCE_RUNS_ROOT
            source_run_dir, _ = self.emit_source_run(source_root)
            self.emit_ingress_run(temp_root, source_run_dir)
            stdout = io.StringIO()

            with (
                mock.patch.object(comparer, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stdout),
            ):
                comparer.main()

            output = stdout.getvalue()

            self.assertIn("Source run:", output)
            self.assertIn("Ingress run:", output)
            self.assertIn("Scenarios compared: 5", output)
            self.assertIn("Mismatches: 0", output)
            self.assertIn("All matched: True", output)
            self.assertIn("Comparison artifact:", output)

    def test_mismatch_visibility(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, ingress_manifest = self.build_pair(
                temp_root
            )
            mismatched = copy.deepcopy(ingress_manifest)
            target_entry = mismatched["scenario_ingress_entries"][0]
            target_entry["object_count"] += 1
            target_entry["receiving_status"]["continuity_completed"] = True
            self.write_json(ingress_run_dir / "manifest.json", mismatched)

            comparison = self.compare(temp_root, source_run_dir, ingress_run_dir)

            affected = next(
                item
                for item in comparison["scenario_comparisons"]
                if item["scenario_id"] == target_entry["scenario_id"]
            )
            self.assertFalse(affected["matched"])
            self.assertTrue(affected["mismatches"])
            self.assertFalse(
                affected["non_claims"]["continuity_completed"]["matched"]
            )
            self.assertFalse(comparison["aggregate_comparison"]["aggregate_match"])
            self.assertTrue(comparison["aggregate_comparison"]["mismatches"])
            self.assertFalse(comparison["all_matched"])

    def test_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest, ingress_run_dir, ingress_manifest = (
                self.build_pair(temp_root)
            )

            malformed_source = copy.deepcopy(source_manifest)
            malformed_source["scenario_count"] += 1
            self.write_json(source_run_dir / "manifest.json", malformed_source)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

            self.write_json(source_run_dir / "manifest.json", source_manifest)
            malformed_ingress = copy.deepcopy(ingress_manifest)
            malformed_ingress["aggregate_counts"]["scenario_count"] += 1
            self.write_json(ingress_run_dir / "manifest.json", malformed_ingress)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

            self.write_json(ingress_run_dir / "manifest.json", ingress_manifest)
            missing_artifact_source = copy.deepcopy(source_manifest)
            missing_artifact_source["scenarios"][0]["file_path"] = str(
                source_run_dir / "missing.json"
            )
            self.write_json(source_run_dir / "manifest.json", missing_artifact_source)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

            self.write_json(source_run_dir / "manifest.json", source_manifest)
            missing_decision_ingress = copy.deepcopy(ingress_manifest)
            missing_decision_ingress["scenario_ingress_entries"][0][
                "ingress_decision_path"
            ] = str(ingress_run_dir / "missing_decision.json")
            self.write_json(ingress_run_dir / "manifest.json", missing_decision_ingress)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

            coverage_mismatch_ingress = copy.deepcopy(ingress_manifest)
            coverage_mismatch_ingress["scenario_ingress_entries"].pop()
            coverage_mismatch_ingress["aggregate_counts"]["scenario_count"] -= 1
            self.write_json(ingress_run_dir / "manifest.json", coverage_mismatch_ingress)
            with self.assertRaises(RuntimeError):
                self.compare(temp_root, source_run_dir, ingress_run_dir)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _ = self.build_pair(temp_root)
            source_before = self.json_texts(source_run_dir)
            ingress_before = self.json_texts(ingress_run_dir)

            first = self.compare(temp_root, source_run_dir, ingress_run_dir)
            source_after_first = self.json_texts(source_run_dir)
            ingress_after_first = self.json_texts(ingress_run_dir)
            second = self.compare(temp_root, source_run_dir, ingress_run_dir)
            source_after_second = self.json_texts(source_run_dir)
            ingress_after_second = self.json_texts(ingress_run_dir)

            self.assertEqual(source_after_first, source_before)
            self.assertEqual(source_after_second, source_before)
            self.assertEqual(ingress_after_first, ingress_before)
            self.assertEqual(ingress_after_second, ingress_before)
            self.assertEqual(first["source_run"], second["source_run"])
            self.assertEqual(first["ingress_run"], second["ingress_run"])
            self.assertTrue(first["all_matched"])
            self.assertTrue(second["all_matched"])


if __name__ == "__main__":
    unittest.main()
