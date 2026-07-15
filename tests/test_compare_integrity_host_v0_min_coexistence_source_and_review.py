"""Bounded tests for the v0-min source-to-review comparison runner.

These tests lock the current comparison surface in
``src/compare_integrity_host_v0_min_coexistence_source_and_review.py`` using
fresh source scenario runs and import-review artifacts emitted through the
current local runners.

They verify discovery, source/review correspondence, bounded validation,
per-scenario count comparison, aggregate count comparison, JSON writing,
stdout summary, mismatch visibility, and non-mutation of source/review
artifacts. They do not test replay, host merge, registry behavior,
persistence architecture, distributed continuity, CLI argument parsing, or
future workflow features.
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

import compare_integrity_host_v0_min_coexistence_source_and_review as comparator  # noqa: E402
import review_integrity_host_v0_min_coexistence_imports as reviewer  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_SCENARIO_IDS = [
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
]


class IntegrityHostV0MinCoexistenceSourceReviewComparisonTests(unittest.TestCase):
    def emit_run(self, run_dir: Path) -> Path:
        run_dir.mkdir(parents=True, exist_ok=True)
        emitted = tuple(
            runner._emit_scenario(run_dir, file_stem, scenario_function)
            for file_stem, scenario_function in runner.SCENARIOS
        )
        manifest = runner._build_manifest(run_dir, emitted)
        runner._write_json(run_dir / "manifest.json", manifest)
        return run_dir

    def emit_review_artifact(self, source_run_dir: Path, review_path: Path) -> Path:
        review = reviewer.review_run_directory(source_run_dir)
        return reviewer.write_review(review, review_path)

    def emit_source_and_review(
        self,
        root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, Path]:
        source_run_dir = self.emit_run(root / "source" / run_name)
        review_path = root / "reviews" / f"{run_name}__import_review.json"
        self.emit_review_artifact(source_run_dir, review_path)
        return source_run_dir, review_path

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

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

    def assert_count_comparison_entry(self, entry: dict[str, Any]) -> None:
        self.assertEqual(set(entry), {"source", "review", "matched"})
        self.assertIsInstance(entry["source"], int)
        self.assertIsInstance(entry["review"], int)
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

    def test_latest_review_artifact_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "reviews"
            root.mkdir()
            (root / "zz_unrelated.json").write_text("{}", encoding="utf-8")
            older = root / "run_20260420T000000_000000Z__import_review.json"
            latest = root / "run_20260420T000001_000000Z__import_review.json"
            ignored_suffix = root / "run_20260420T999999_000000Z__import_review_001.json"
            older.write_text("{}", encoding="utf-8")
            latest.write_text("{}", encoding="utf-8")
            ignored_suffix.write_text("{}", encoding="utf-8")

            self.assertEqual(comparator.find_latest_review_artifact(root), latest)

            empty_root = Path(temp_dir) / "empty-reviews"
            empty_root.mkdir()
            (empty_root / "not_review.json").write_text("{}", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                comparator.find_latest_review_artifact(empty_root)

            with self.assertRaises(RuntimeError):
                comparator.find_latest_review_artifact(Path(temp_dir) / "missing")

    def test_source_review_correspondence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            run_a, review_a = self.emit_source_and_review(
                temp_root,
                "run_20260420T000000_000000Z",
            )
            run_b = self.emit_run(temp_root / "source" / "run_20260420T000001_000000Z")

            comparison = comparator.compare_source_run_and_review(run_a, review_a)

            self.assertTrue(comparison["all_matched"])
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_review(run_b, review_a)

    def test_read_posture_and_malformed_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir, review_path = self.emit_source_and_review(temp_root)

            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                review_path,
            )

            self.assertIn("source_run", comparison)
            self.assertIn("review_artifact", comparison)

            missing_manifest_dir = temp_root / "source" / "run_missing_manifest"
            missing_manifest_dir.mkdir(parents=True)
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_review(missing_manifest_dir, review_path)

            malformed_manifest_dir = temp_root / "source" / "run_malformed_manifest"
            malformed_manifest_dir.mkdir(parents=True)
            (malformed_manifest_dir / "manifest.json").write_text(
                json.dumps(
                    {
                        "generated_at": "now",
                        "output_directory": "somewhere",
                        "scenario_count": 1,
                        "scenarios": [],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_review(
                    malformed_manifest_dir,
                    review_path,
                )

            malformed_review_path = temp_root / "reviews" / "malformed_review.json"
            malformed_review_path.parent.mkdir(parents=True, exist_ok=True)
            malformed_review_path.write_text(
                json.dumps({"review_metadata": {}, "source_run": {}}),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                comparator.compare_source_run_and_review(
                    source_run_dir,
                    malformed_review_path,
                )

    def test_real_source_review_comparison_shape_and_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir, review_path = self.emit_source_and_review(Path(temp_dir))

            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                review_path,
            )

            self.assertEqual(
                set(comparison),
                {
                    "comparison_metadata",
                    "source_run",
                    "review_artifact",
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
                Path(comparison["review_artifact"]["review_artifact_path"]).resolve(),
                review_path.resolve(),
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
            source_run_dir, review_path = self.emit_source_and_review(Path(temp_dir))
            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                review_path,
            )

            for scenario_comparison in comparison["scenario_comparisons"]:
                self.assertTrue(scenario_comparison["scenario_id"])
                self.assertTrue(scenario_comparison["scenario_name"])
                self.assertTrue(Path(scenario_comparison["source_artifact_path"]).exists())
                self.assertTrue(
                    Path(scenario_comparison["review_source_artifact_path"]).exists()
                )
                self.assertIsInstance(scenario_comparison["matched"], bool)
                self.assertIsInstance(scenario_comparison["mismatches"], list)
                self.assertTrue(scenario_comparison["matched"])
                self.assertEqual(scenario_comparison["mismatches"], [])

                counts = scenario_comparison["counts"]
                self.assertEqual(set(counts), set(comparator.COUNT_KEYS))
                for key in comparator.COUNT_KEYS:
                    self.assert_count_comparison_entry(counts[key])
                    self.assertTrue(counts[key]["matched"], key)

    def test_aggregate_comparison_clean_match(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir, review_path = self.emit_source_and_review(Path(temp_dir))
            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                review_path,
            )

            aggregate = comparison["aggregate_comparison"]

            self.assertIn("source_totals", aggregate)
            self.assertIn("review_totals", aggregate)
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
                aggregate["review_totals"]["scenario_count"],
            )
            self.assertEqual(
                set(aggregate["counts"]),
                {"scenario_count", *comparator.COUNT_KEYS},
            )
            for key, count_entry in aggregate["counts"].items():
                with self.subTest(key=key):
                    self.assert_count_comparison_entry(count_entry)
                    self.assertTrue(count_entry["matched"])

    def test_scenario_specific_comparison_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source_run_dir, review_path = self.emit_source_and_review(Path(temp_dir))
            by_id = self.comparison_by_id(
                comparator.compare_source_run_and_review(source_run_dir, review_path)
            )

            lawful = by_id["lawful_distinct_matter_coexistence"]["counts"]
            self.assertEqual(lawful["object_count"]["source"], 2)
            self.assertEqual(lawful["coexistence_relation_count"]["source"], 1)
            self.assertEqual(lawful["refusal_count"]["source"], 0)
            self.assertGreater(lawful["transition_record_count"]["source"], 0)

            missing_basis = by_id["refused_missing_coexistence_basis"]["counts"]
            self.assertEqual(missing_basis["object_count"]["source"], 1)
            self.assertGreater(missing_basis["refusal_count"]["source"], 0)
            self.assertGreater(missing_basis["transition_record_count"]["source"], 0)

            evolve = by_id["evolve_under_coexistence"]["counts"]
            self.assertEqual(evolve["object_count"]["source"], 3)
            self.assertEqual(evolve["successor_object_count"]["source"], 1)
            self.assertEqual(evolve["evolve_record_count"]["source"], 1)
            self.assertGreater(evolve["transition_record_count"]["source"], 0)

            hold = by_id["hold_blocks_one_target_while_another_proceeds"]["counts"]
            self.assertGreater(hold["hold_count"]["source"], 0)
            self.assertGreater(hold["refusal_count"]["source"], 0)
            self.assertGreater(hold["transition_record_count"]["source"], 0)

            same_matter = by_id["same_matter_post_resolution_refusal"]["counts"]
            self.assertEqual(same_matter["object_count"]["source"], 1)
            self.assertGreater(same_matter["refusal_count"]["source"], 0)

    def test_write_comparison_writes_json(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir, review_path = self.emit_source_and_review(temp_root)
            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                review_path,
            )
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
                    "review_artifact",
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
            review_root = temp_root / comparator.REVIEW_ROOT

            older = self.emit_run(source_root / "run_20260420T000000_000000Z")
            latest = self.emit_run(source_root / "run_20260420T000001_000000Z")
            self.emit_review_artifact(
                older,
                review_root / f"{older.name}__import_review.json",
            )
            latest_review = self.emit_review_artifact(
                latest,
                review_root / f"{latest.name}__import_review.json",
            )

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
            self.assertIn("Review artifact:", output)
            self.assertIn(latest_review.name, output)
            self.assertIn(f"Scenarios compared: {len(runner.SCENARIOS)}", output)
            self.assertIn("Mismatches:", output)
            self.assertIn("All matched: True", output)
            self.assertIn("Comparison artifact:", output)
            self.assertIn(comparison_files[0].name, output)

    def test_mismatch_visibility(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir, review_path = self.emit_source_and_review(temp_root)
            review = self.read_json(review_path)
            first_review = review["scenario_reviews"][0]
            first_review["object_count"] += 1
            review["aggregate_counts"]["object_count"] += 1

            mismatched_review_path = temp_root / "reviews" / "mismatched_review.json"
            mismatched_review_path.write_text(
                json.dumps(review, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )

            comparison = comparator.compare_source_run_and_review(
                source_run_dir,
                mismatched_review_path,
            )
            first_comparison = comparison["scenario_comparisons"][0]
            aggregate = comparison["aggregate_comparison"]

            self.assertFalse(first_comparison["matched"])
            self.assertTrue(first_comparison["mismatches"])
            self.assertFalse(first_comparison["counts"]["object_count"]["matched"])
            self.assertIn("object_count mismatch", first_comparison["mismatches"][0])
            self.assertFalse(aggregate["aggregate_match"])
            self.assertFalse(aggregate["counts"]["object_count"]["matched"])
            self.assertTrue(aggregate["mismatches"])
            self.assertFalse(comparison["all_matched"])

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_run_dir, review_path = self.emit_source_and_review(temp_root)
            source_before = self.source_file_texts(source_run_dir)
            review_before = review_path.read_text(encoding="utf-8")

            first = comparator.compare_source_run_and_review(source_run_dir, review_path)
            second = comparator.compare_source_run_and_review(source_run_dir, review_path)
            output_path = temp_root / "comparisons" / "comparison.json"
            comparator.write_comparison(first, output_path)

            self.assertEqual(source_before, self.source_file_texts(source_run_dir))
            self.assertEqual(review_before, review_path.read_text(encoding="utf-8"))
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
