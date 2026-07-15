"""Bounded tests for the v0-min coexistence import-review runner.

These tests lock the current review surface in
``src/review_integrity_host_v0_min_coexistence_imports.py`` using fresh
scenario artifacts emitted through
``src/run_integrity_host_v0_min_coexistence_scenarios.py``.

They verify latest-run discovery, manifest validation, per-scenario import
review summaries, aggregate counts, JSON review writing, stdout summary, error
posture, and non-mutation of source artifacts. They do not test replay, host
merge, registry behavior, persistence architecture, distributed continuity,
CLI argument parsing, or future workflow features.
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

import review_integrity_host_v0_min_coexistence_imports as reviewer  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_SCENARIO_IDS = [
    "lawful_distinct_matter_coexistence",
    "refused_missing_coexistence_basis",
    "evolve_under_coexistence",
    "hold_blocks_one_target_while_another_proceeds",
    "same_matter_post_resolution_refusal",
]


class IntegrityHostV0MinCoexistenceImportReviewTests(unittest.TestCase):
    def emit_run(self, run_dir: Path) -> Path:
        run_dir.mkdir(parents=True, exist_ok=True)
        emitted = tuple(
            runner._emit_scenario(run_dir, file_stem, scenario_function)
            for file_stem, scenario_function in runner.SCENARIOS
        )
        runner._write_json(run_dir / "manifest.json", runner._build_manifest(run_dir, emitted))
        return run_dir

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

    def review_by_id(self, review: dict[str, Any]) -> dict[str, dict[str, Any]]:
        return {
            scenario["scenario_id"]: scenario
            for scenario in review["scenario_reviews"]
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

    def test_latest_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "runs"
            root.mkdir()
            (root / "not_a_run").mkdir()
            older = root / "run_20260420T000000_000000Z"
            latest = root / "run_20260420T000001_000000Z"
            older.mkdir()
            latest.mkdir()

            self.assertEqual(reviewer.find_latest_run_directory(root), latest)

            empty_root = Path(temp_dir) / "empty-runs"
            empty_root.mkdir()
            (empty_root / "notes").mkdir()
            with self.assertRaises(RuntimeError):
                reviewer.find_latest_run_directory(empty_root)

            with self.assertRaises(RuntimeError):
                reviewer.find_latest_run_directory(Path(temp_dir) / "missing")

    def test_read_run_manifest_valid_and_malformed(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = self.emit_run(Path(temp_dir) / "run_valid")

            manifest = reviewer.read_run_manifest(run_dir)

            self.assertIn("generated_at", manifest)
            self.assertIn("output_directory", manifest)
            self.assertIn("scenario_count", manifest)
            self.assertIn("scenarios", manifest)
            self.assertEqual(manifest["scenario_count"], len(runner.SCENARIOS))
            self.assertEqual(len(manifest["scenarios"]), len(runner.SCENARIOS))

            missing_manifest_dir = Path(temp_dir) / "run_missing_manifest"
            missing_manifest_dir.mkdir()
            with self.assertRaises(RuntimeError):
                reviewer.read_run_manifest(missing_manifest_dir)

            malformed_dir = Path(temp_dir) / "run_malformed_manifest"
            malformed_dir.mkdir()
            (malformed_dir / "manifest.json").write_text(
                json.dumps(
                    {
                        "generated_at": "now",
                        "output_directory": "somewhere",
                        "scenario_count": 2,
                        "scenarios": [],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                reviewer.read_run_manifest(malformed_dir)

            wrong_type_dir = Path(temp_dir) / "run_wrong_manifest_type"
            wrong_type_dir.mkdir()
            (wrong_type_dir / "manifest.json").write_text("[1, 2, 3]", encoding="utf-8")
            with self.assertRaises(RuntimeError):
                reviewer.read_run_manifest(wrong_type_dir)

    def test_review_run_directory_shape_and_scenario_coverage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = self.emit_run(Path(temp_dir) / "run_review")

            review = reviewer.review_run_directory(run_dir)

            self.assertEqual(
                set(review),
                {
                    "review_metadata",
                    "source_run",
                    "source_manifest",
                    "scenario_reviews",
                    "aggregate_counts",
                },
            )
            self.assertEqual(review["source_run"]["source_scenario_count"], len(runner.SCENARIOS))
            self.assertIn(run_dir.name, review["source_run"]["source_run_directory_path"])
            self.assertIn("manifest.json", review["source_run"]["source_manifest_path"])
            self.assertEqual(len(review["scenario_reviews"]), len(runner.SCENARIOS))
            self.assertEqual(
                [entry["scenario_id"] for entry in review["scenario_reviews"]],
                EXPECTED_SCENARIO_IDS,
            )
            self.assertEqual(
                [entry["scenario_id"] for entry in review["source_manifest"]["scenarios"]],
                EXPECTED_SCENARIO_IDS,
            )

    def test_per_scenario_content_and_aggregate_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = self.emit_run(Path(temp_dir) / "run_counts")
            review = reviewer.review_run_directory(run_dir)

            required_review_keys = {
                "scenario_id",
                "scenario_name",
                "source_artifact_path",
                "imported_summary",
                "accepted_action_count",
                "refused_action_count",
                "object_count",
                "open_object_count",
                "resolved_object_count",
                "coexistence_relation_count",
                "hold_count",
                "transition_record_count",
                "refusal_count",
                "successor_object_count",
                "evolve_record_count",
            }
            count_keys = {
                "accepted_action_count",
                "refused_action_count",
                "object_count",
                "open_object_count",
                "resolved_object_count",
                "coexistence_relation_count",
                "hold_count",
                "transition_record_count",
                "refusal_count",
                "successor_object_count",
                "evolve_record_count",
            }

            for scenario_review in review["scenario_reviews"]:
                self.assertTrue(required_review_keys.issubset(scenario_review))
                self.assertTrue(scenario_review["scenario_id"])
                self.assertTrue(scenario_review["scenario_name"])
                self.assertTrue(scenario_review["source_artifact_path"])
                self.assertIsInstance(scenario_review["imported_summary"], dict)
                self.assertIn("snapshot_type", scenario_review["imported_summary"])
                self.assertGreater(len(scenario_review), 5)
                for key in count_keys:
                    self.assertIsInstance(scenario_review[key], int)

            aggregate = review["aggregate_counts"]
            self.assertEqual(aggregate["scenario_count"], len(runner.SCENARIOS))
            self.assertEqual(
                aggregate["scenario_count"],
                review["source_manifest"]["scenario_count"],
            )
            self.assertGreater(aggregate["refusal_count"], 0)
            for key in count_keys:
                self.assertEqual(
                    aggregate[key],
                    sum(entry[key] for entry in review["scenario_reviews"]),
                    key,
                )

    def test_scenario_review_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = self.emit_run(Path(temp_dir) / "run_signals")
            reviews = self.review_by_id(reviewer.review_run_directory(run_dir))

            lawful = reviews["lawful_distinct_matter_coexistence"]
            self.assertEqual(lawful["object_count"], 2)
            self.assertEqual(lawful["coexistence_relation_count"], 1)
            self.assertEqual(lawful["refusal_count"], 0)
            self.assertGreater(lawful["transition_record_count"], 0)

            missing_basis = reviews["refused_missing_coexistence_basis"]
            self.assertEqual(missing_basis["object_count"], 1)
            self.assertGreater(missing_basis["refusal_count"], 0)
            self.assertGreater(missing_basis["transition_record_count"], 0)

            evolve = reviews["evolve_under_coexistence"]
            self.assertEqual(evolve["object_count"], 3)
            self.assertEqual(evolve["successor_object_count"], 1)
            self.assertEqual(evolve["evolve_record_count"], 1)
            self.assertGreater(evolve["transition_record_count"], 0)
            self.assertGreater(evolve["accepted_action_count"], 0)

            hold = reviews["hold_blocks_one_target_while_another_proceeds"]
            self.assertGreater(hold["hold_count"], 0)
            self.assertGreater(hold["refusal_count"], 0)
            self.assertGreater(hold["transition_record_count"], 0)

            same_matter = reviews["same_matter_post_resolution_refusal"]
            self.assertEqual(same_matter["object_count"], 1)
            self.assertGreater(same_matter["refusal_count"], 0)
            self.assertTrue(same_matter["source_artifact_path"])
            self.assertEqual(
                same_matter["scenario_id"],
                "same_matter_post_resolution_refusal",
            )

    def test_write_review_writes_json_without_source_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            run_dir = self.emit_run(Path(temp_dir) / "run_write")
            review = reviewer.review_run_directory(run_dir)
            output_path = Path(temp_dir) / "reviews" / "nested" / "review.json"

            written = reviewer.write_review(review, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(
                set(parsed),
                {
                    "review_metadata",
                    "source_run",
                    "source_manifest",
                    "scenario_reviews",
                    "aggregate_counts",
                },
            )
            with self.assertRaises(RuntimeError):
                reviewer.write_review(review, output_path)

    def test_main_reviews_latest_run_and_prints_summary(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            source_root = temp_root / reviewer.SOURCE_RUNS_ROOT
            older = self.emit_run(source_root / "run_20260420T000000_000000Z")
            latest = self.emit_run(source_root / "run_20260420T000001_000000Z")
            self.assertTrue(older.exists())

            stream = io.StringIO()
            with (
                mock.patch.object(reviewer, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stream),
            ):
                reviewer.main()

            output = stream.getvalue()
            review_root = temp_root / reviewer.REVIEW_OUTPUT_ROOT
            review_files = list(review_root.glob("*.json"))

            self.assertEqual(len(review_files), 1)
            self.assertIn("Source run:", output)
            self.assertIn(latest.name, output)
            self.assertIn(f"Scenarios reviewed: {len(runner.SCENARIOS)}", output)
            self.assertIn("Total refusals:", output)
            self.assertIn("Review artifact:", output)
            self.assertIn(review_files[0].name, output)

    def test_validation_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            empty_root = temp_path / "empty"
            empty_root.mkdir()
            with self.assertRaises(RuntimeError):
                reviewer.find_latest_run_directory(empty_root)

            malformed_run = temp_path / "run_malformed"
            malformed_run.mkdir()
            (malformed_run / "manifest.json").write_text(
                json.dumps(
                    {
                        "generated_at": "now",
                        "output_directory": "out",
                        "scenario_count": 1,
                        "scenarios": [{"scenario_id": "missing-name"}],
                    }
                ),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                reviewer.read_run_manifest(malformed_run)

            missing_artifact_run = self.emit_run(temp_path / "run_missing_artifact")
            manifest_path = missing_artifact_run / "manifest.json"
            manifest = self.read_json(manifest_path)
            manifest["scenarios"][0]["file_path"] = (
                missing_artifact_run / "missing-scenario.json"
            ).as_posix()
            manifest_path.write_text(
                json.dumps(manifest, indent=2, sort_keys=True) + "\n",
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                reviewer.review_run_directory(missing_artifact_run)

            bad_artifact_run = self.emit_run(temp_path / "run_bad_artifact")
            bad_artifact_path = self.manifest_artifact_paths(bad_artifact_run)[0]
            bad_artifact_path.write_text(
                json.dumps({"scenario": {}, "snapshot": {}}),
                encoding="utf-8",
            )
            with self.assertRaises(RuntimeError):
                reviewer.review_run_directory(bad_artifact_run)

    def test_review_generation_does_not_mutate_source_run(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            run_dir = self.emit_run(temp_path / "run_non_mutation")
            before_texts = self.source_file_texts(run_dir)

            first_review = reviewer.review_run_directory(run_dir)
            second_review = reviewer.review_run_directory(run_dir)
            output_path = temp_path / "reviews" / "review.json"
            reviewer.write_review(first_review, output_path)

            after_texts = self.source_file_texts(run_dir)

            self.assertEqual(after_texts, before_texts)
            self.assertEqual(
                first_review["aggregate_counts"],
                second_review["aggregate_counts"],
            )
            self.assertTrue(output_path.exists())
            self.assertEqual(
                {path.name for path in before_texts},
                {path.name for path in after_texts},
            )


if __name__ == "__main__":
    unittest.main()
