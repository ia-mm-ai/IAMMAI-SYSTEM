"""Bounded tests for the v0-min source-to-import comparison runner.

These tests lock the current comparison surface in
``src/compare_integrity_host_v0_min_coexistence_source_and_import.py`` using
fresh source scenario runs emitted through the current local scenario runner.

They verify discovery, source manifest validation, direct source/import
comparison, per-scenario count and visibility comparison, aggregate comparison,
JSON writing, stdout summary, mismatch visibility, error posture, and
non-mutation of source artifacts. They do not test replay, host merge,
registry behavior, persistence architecture, distributed continuity, CLI
argument parsing, broad recursive diffing, or future workflow features.
"""

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from dataclasses import replace
from pathlib import Path
from typing import Any
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import compare_integrity_host_v0_min_coexistence_source_and_import as comparator  # noqa: E402
import integrity_host_v0_min_coexistence_import as importer  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_SCENARIO_IDS = [
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
]

VISIBILITY_KEYS = {
    "object_ids",
    "coexistence_relations",
    "holds",
    "refusal_records",
    "successor_lineage",
    "evolve_record_lineage",
}


class IntegrityHostV0MinCoexistenceSourceImportComparisonTests(unittest.TestCase):
    def emit_run(self, run_dir: Path) -> Path:
        run_dir.mkdir(parents=True, exist_ok=True)
        emitted = tuple(
            runner._emit_scenario(run_dir, file_stem, scenario_function)
            for file_stem, scenario_function in runner.SCENARIOS
        )
        manifest = runner._build_manifest(run_dir, emitted)
        runner._write_json(run_dir / "manifest.json", manifest)
        return run_dir

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

    def write_json(self, path: Path, payload: dict[str, Any]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def comparison_by_id(self, comparison: dict[str, Any]) -> dict[str, dict[str, Any]]:
        return {
            item["scenario_id"]: item
            for item in comparison["scenario_comparisons"]
        }

    def manifest_artifact_paths(self, run_dir: Path) -> list[Path]:
        manifest = self.read_json(run_dir / "manifest.json")
        paths: list[Path] = []
        for entry in manifest["scenarios"]:
            path = Path(entry["file_path"])
            if not path.is_absolute():
                repo_candidate = REPO_ROOT / path
                path = repo_candidate if repo_candidate.exists() else run_dir / path
            paths.append(path)
        return paths

    def source_file_texts(self, run_dir: Path) -> dict[Path, str]:
        paths = [run_dir / "manifest.json", *self.manifest_artifact_paths(run_dir)]
        return {path: path.read_text(encoding="utf-8") for path in paths}

    def assert_count_entry(self, entry: dict[str, Any]) -> None:
        self.assertEqual(set(entry), {"source", "import", "matched"})
        self.assertIsInstance(entry["source"], int)
        self.assertIsInstance(entry["import"], int)
        self.assertIsInstance(entry["matched"], bool)

    def assert_visibility_entry(self, entry: dict[str, Any]) -> None:
        self.assertEqual(set(entry), {"source", "import", "matched"})
        self.assertIsInstance(entry["source"], list)
        self.assertIsInstance(entry["import"], list)
        self.assertIsInstance(entry["matched"], bool)

    def test_latest_source_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "runs"
            root.mkdir()
            (root / "notes").mkdir()
            older = root / "run_20260420T000000_000000Z"
            latest = root / "run_20260420T000001_000000Z"
            older.mkdir()
            latest.mkdir()

            self.assertEqual(comparator.find_latest_source_run_directory(root), latest)

            empty_root = Path(temp_dir) / "empty"
            empty_root.mkdir()
            (empty_root / "zz_not_a_run").mkdir()
            with self.assertRaises(RuntimeError):
                comparator.find_latest_source_run_directory(empty_root)

            with self.assertRaises(RuntimeError):
                comparator.find_latest_source_run_directory(Path(temp_dir) / "missing")

    def test_read_source_manifest_valid_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            run_dir = self.emit_run(temp_root / "run_valid")

            manifest = comparator.read_source_manifest(run_dir)

            self.assertIn("generated_at", manifest)
            self.assertIn("output_directory", manifest)
            self.assertIn("scenario_count", manifest)
            self.assertIn("scenarios", manifest)
            self.assertEqual(manifest["scenario_count"], len(runner.SCENARIOS))
            self.assertEqual(len(manifest["scenarios"]), len(runner.SCENARIOS))

            missing_manifest_dir = temp_root / "run_missing_manifest"
            missing_manifest_dir.mkdir()
            with self.assertRaises(RuntimeError):
                comparator.read_source_manifest(missing_manifest_dir)

            malformed_dir = temp_root / "run_malformed_manifest"
            malformed_dir.mkdir()
            self.write_json(
                malformed_dir / "manifest.json",
                {
                    "generated_at": "now",
                    "output_directory": "somewhere",
                    "scenario_count": 2,
                    "scenarios": [],
                },
            )
            with self.assertRaises(RuntimeError):
                comparator.read_source_manifest(malformed_dir)

            wrong_type_dir = temp_root / "run_wrong_manifest_type"
            wrong_type_dir.mkdir()
            (wrong_type_dir / "manifest.json").write_text("[1, 2, 3]", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                comparator.read_source_manifest(wrong_type_dir)

            duplicate_dir = self.emit_run(temp_root / "run_duplicate_manifest")
            duplicate_manifest_path = duplicate_dir / "manifest.json"
            duplicate_manifest = self.read_json(duplicate_manifest_path)
            duplicate_manifest["scenarios"][1]["scenario_id"] = (
                duplicate_manifest["scenarios"][0]["scenario_id"]
            )
            self.write_json(duplicate_manifest_path, duplicate_manifest)
            with self.assertRaises(RuntimeError):
                comparator.read_source_manifest(duplicate_dir)

    def test_real_source_import_comparison_shape_and_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir = self.emit_run(Path(temp_dir) / "run_compare")

            comparison = comparator.compare_source_run_and_import(source_run_dir)

            self.assertEqual(
                set(comparison),
                {
                    "comparison_metadata",
                    "source_run",
                    "scenario_comparisons",
                    "aggregate_comparison",
                    "all_matched",
                },
            )
            self.assertEqual(
                comparison["comparison_metadata"]["comparison_type"],
                comparator.COMPARISON_TYPE,
            )
            self.assertEqual(
                Path(comparison["source_run"]["source_run_directory_path"]).resolve(),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                Path(comparison["source_run"]["source_manifest_path"]).resolve(),
                (source_run_dir / "manifest.json").resolve(),
            )
            self.assertEqual(
                comparison["source_run"]["source_scenario_count"],
                len(runner.SCENARIOS),
            )
            self.assertEqual(
                len(comparison["scenario_comparisons"]),
                comparison["source_run"]["source_scenario_count"],
            )
            self.assertEqual(
                [item["scenario_id"] for item in comparison["scenario_comparisons"]],
                EXPECTED_SCENARIO_IDS,
            )

    def test_per_scenario_comparison_content(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir = self.emit_run(Path(temp_dir) / "run_content")
            comparison = comparator.compare_source_run_and_import(source_run_dir)

            for scenario_comparison in comparison["scenario_comparisons"]:
                self.assertTrue(scenario_comparison["scenario_id"])
                self.assertTrue(scenario_comparison["scenario_name"])
                self.assertTrue(Path(scenario_comparison["source_artifact_path"]).exists())
                self.assertIsInstance(scenario_comparison["matched"], bool)
                self.assertIsInstance(scenario_comparison["mismatches"], list)
                self.assertTrue(scenario_comparison["matched"])
                self.assertEqual(scenario_comparison["mismatches"], [])

                counts = scenario_comparison["counts"]
                self.assertEqual(set(counts), set(comparator.COUNT_KEYS))
                for key in comparator.COUNT_KEYS:
                    with self.subTest(scenario=scenario_comparison["scenario_id"], key=key):
                        self.assert_count_entry(counts[key])
                        self.assertTrue(counts[key]["matched"])

                visibility = scenario_comparison["visibility"]
                self.assertEqual(set(visibility), VISIBILITY_KEYS)
                for key in VISIBILITY_KEYS:
                    with self.subTest(
                        scenario=scenario_comparison["scenario_id"],
                        visibility=key,
                    ):
                        self.assert_visibility_entry(visibility[key])
                        self.assertTrue(visibility[key]["matched"])

    def test_aggregate_comparison_clean_match(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir = self.emit_run(Path(temp_dir) / "run_aggregate")
            comparison = comparator.compare_source_run_and_import(source_run_dir)
            aggregate = comparison["aggregate_comparison"]

            self.assertIn("source_totals", aggregate)
            self.assertIn("import_totals", aggregate)
            self.assertIn("counts_match", aggregate)
            self.assertIn("aggregate_match", aggregate)
            self.assertIn("mismatches", aggregate)
            self.assertIn("counts", aggregate)
            self.assertTrue(aggregate["counts_match"])
            self.assertTrue(aggregate["aggregate_match"])
            self.assertEqual(aggregate["mismatches"], [])
            self.assertTrue(comparison["all_matched"])
            self.assertEqual(
                aggregate["source_totals"]["scenario_count"],
                len(runner.SCENARIOS),
            )
            self.assertEqual(
                aggregate["source_totals"]["scenario_count"],
                aggregate["import_totals"]["scenario_count"],
            )
            self.assertEqual(
                set(aggregate["counts"]),
                {"scenario_count", *comparator.COUNT_KEYS},
            )
            for key, count_entry in aggregate["counts"].items():
                with self.subTest(key=key):
                    self.assert_count_entry(count_entry)
                    self.assertTrue(count_entry["matched"])

    def test_scenario_specific_comparison_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir = self.emit_run(Path(temp_dir) / "run_signals")
            by_id = self.comparison_by_id(
                comparator.compare_source_run_and_import(source_run_dir)
            )

            lawful = by_id["lawful_distinct_matter_coexistence"]
            self.assertEqual(lawful["counts"]["object_count"]["source"], 2)
            self.assertEqual(
                lawful["counts"]["coexistence_relation_count"]["source"],
                1,
            )
            self.assertEqual(lawful["counts"]["refusal_count"]["source"], 0)
            self.assertGreater(
                lawful["counts"]["transition_record_count"]["source"],
                0,
            )
            self.assertTrue(lawful["visibility"]["object_ids"]["source"])
            self.assertTrue(lawful["visibility"]["coexistence_relations"]["source"])

            missing_basis = by_id["refused_missing_coexistence_basis"]
            self.assertEqual(missing_basis["counts"]["object_count"]["source"], 1)
            self.assertGreater(missing_basis["counts"]["refusal_count"]["source"], 0)
            self.assertTrue(missing_basis["visibility"]["refusal_records"]["source"])

            evolve = by_id["evolve_under_coexistence"]
            self.assertEqual(evolve["counts"]["object_count"]["source"], 3)
            self.assertEqual(evolve["counts"]["successor_object_count"]["source"], 1)
            self.assertEqual(evolve["counts"]["evolve_record_count"]["source"], 1)
            self.assertTrue(evolve["visibility"]["successor_lineage"]["source"])
            self.assertTrue(evolve["visibility"]["evolve_record_lineage"]["source"])

            hold = by_id["hold_blocks_one_target_while_another_proceeds"]
            self.assertGreater(hold["counts"]["hold_count"]["source"], 0)
            self.assertGreater(hold["counts"]["refusal_count"]["source"], 0)
            self.assertTrue(hold["visibility"]["holds"]["source"])

            same_matter = by_id["same_matter_post_resolution_refusal"]
            self.assertEqual(same_matter["counts"]["object_count"]["source"], 1)
            self.assertGreater(same_matter["counts"]["refusal_count"]["source"], 0)
            self.assertTrue(same_matter["visibility"]["refusal_records"]["source"])

    def test_write_comparison_writes_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir = self.emit_run(temp_root / "run_write")
            comparison = comparator.compare_source_run_and_import(source_run_dir)
            output_path = temp_root / "comparisons" / "nested" / "comparison.json"

            written = comparator.write_comparison(comparison, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(
                set(parsed),
                {
                    "comparison_metadata",
                    "source_run",
                    "scenario_comparisons",
                    "aggregate_comparison",
                    "all_matched",
                },
            )
            with self.assertRaises(RuntimeError):
                comparator.write_comparison(comparison, output_path)

    def test_main_runner_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_root = temp_root / comparator.SOURCE_RUNS_ROOT
            older = self.emit_run(source_root / "run_20260420T000000_000000Z")
            latest = self.emit_run(source_root / "run_20260420T000001_000000Z")
            self.assertTrue(older.exists())

            stream = io.StringIO()
            with (
                mock.patch.object(comparator, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stream),
            ):
                comparator.main()

            output = stream.getvalue()
            comparison_root = temp_root / comparator.COMPARISON_OUTPUT_ROOT
            comparison_files = list(comparison_root.glob("*.json"))

            self.assertEqual(len(comparison_files), 1)
            self.assertIn("Source run:", output)
            self.assertIn(latest.name, output)
            self.assertIn(f"Scenarios compared: {len(runner.SCENARIOS)}", output)
            self.assertIn("Mismatches:", output)
            self.assertIn("All matched: True", output)
            self.assertIn("Comparison artifact:", output)
            self.assertIn(comparison_files[0].name, output)

    def test_mismatch_visibility(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir = self.emit_run(Path(temp_dir) / "run_mismatch")
            original_load = comparator.load_scenario_artifact

            def load_with_missing_object(path: Path) -> importer.ImportedScenarioArtifact:
                imported = original_load(path)
                if imported.scenario.scenario_id == "lawful_distinct_matter_coexistence":
                    return replace(imported, objects=imported.objects[:-1])
                return imported

            with mock.patch.object(
                comparator,
                "load_scenario_artifact",
                side_effect=load_with_missing_object,
            ):
                comparison = comparator.compare_source_run_and_import(source_run_dir)

            lawful = self.comparison_by_id(comparison)[
                "lawful_distinct_matter_coexistence"
            ]
            aggregate = comparison["aggregate_comparison"]

            self.assertFalse(lawful["matched"])
            self.assertTrue(lawful["mismatches"])
            self.assertFalse(lawful["counts"]["object_count"]["matched"])
            self.assertFalse(lawful["visibility"]["object_ids"]["matched"])
            self.assertTrue(
                any("object_count mismatch" in item for item in lawful["mismatches"])
            )
            self.assertFalse(aggregate["aggregate_match"])
            self.assertFalse(aggregate["counts"]["object_count"]["matched"])
            self.assertTrue(aggregate["mismatches"])
            self.assertFalse(comparison["all_matched"])

    def test_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)

            malformed_manifest_run = temp_root / "run_malformed_manifest"
            malformed_manifest_run.mkdir()
            self.write_json(
                malformed_manifest_run / "manifest.json",
                {
                    "generated_at": "now",
                    "output_directory": "somewhere",
                    "scenario_count": 1,
                    "scenarios": [],
                },
            )
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_import(malformed_manifest_run)

            missing_artifact_run = self.emit_run(temp_root / "run_missing_artifact")
            missing_manifest_path = missing_artifact_run / "manifest.json"
            missing_manifest = self.read_json(missing_manifest_path)
            missing_manifest["scenarios"][0]["file_path"] = (
                missing_artifact_run / "missing-scenario.json"
            ).as_posix()
            self.write_json(missing_manifest_path, missing_manifest)
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_import(missing_artifact_run)

            bad_artifact_run = self.emit_run(temp_root / "run_bad_artifact")
            bad_artifact_path = self.manifest_artifact_paths(bad_artifact_run)[0]
            bad_artifact_path.write_text(
                json.dumps({"scenario": {}, "snapshot": {}}),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_import(bad_artifact_run)

            import_failure_run = self.emit_run(temp_root / "run_import_failure")
            with mock.patch.object(
                comparator,
                "load_scenario_artifact",
                side_effect=importer.ImportFormatError("bad import"),
            ):
                with self.assertRaises(RuntimeError):
                    comparator.compare_source_run_and_import(import_failure_run)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir = self.emit_run(temp_root / "run_non_mutation")
            before_texts = self.source_file_texts(source_run_dir)

            first = comparator.compare_source_run_and_import(source_run_dir)
            second = comparator.compare_source_run_and_import(source_run_dir)
            output_path = temp_root / "comparisons" / "comparison.json"
            comparator.write_comparison(first, output_path)

            after_texts = self.source_file_texts(source_run_dir)

            self.assertEqual(after_texts, before_texts)
            self.assertEqual(
                first["scenario_comparisons"],
                second["scenario_comparisons"],
            )
            self.assertEqual(
                first["aggregate_comparison"],
                second["aggregate_comparison"],
            )
            self.assertTrue(output_path.exists())


if __name__ == "__main__":
    unittest.main()
