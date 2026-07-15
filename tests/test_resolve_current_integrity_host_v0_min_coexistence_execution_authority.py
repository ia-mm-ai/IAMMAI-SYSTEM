"""Bounded tests for the v0-min coexistence execution-authority resolver.

These tests lock the current additive currentness resolver in
``src/resolve_current_integrity_host_v0_min_coexistence_execution_authority.py``
using real source scenario runs, real run-level receiving-ingress outputs, and
real source-to-ingress comparison artifacts emitted into temporary roots.

They verify discovery, candidate eligibility, latest-is-not-enough selection,
no-authority outcome, bounded non-claims, stdout/write behavior, clear malformed
input failures, and read-only posture. They do not test replay, merge,
persistence architecture, registry behavior, distributed continuity, CLI
argument parsing, or speculative governance frameworks.
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
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "resolution_metadata",
    "canonical_execution_line",
    "candidate_runs",
    "authority_decision",
    "forced_system_pressure_signals",
    "non_claims",
}

EXPECTED_CHECK_KEYS = {
    "source_run_exists",
    "source_manifest_exists",
    "matching_ingress_run_exists",
    "matching_comparison_artifact_exists",
    "canonical_core_execution_file_preserved",
    "ingress_source_run_matches",
    "ingress_source_manifest_matches",
    "ingress_scenario_count_matches_source",
    "ingress_all_packets_built",
    "ingress_all_packets_validated",
    "ingress_all_decisions_emitted",
    "ingress_continuity_not_completed",
    "ingress_standing_not_upgraded",
    "ingress_replay_not_performed",
    "ingress_merge_not_performed",
    "comparison_source_run_matches",
    "comparison_ingress_run_matches",
    "comparison_all_matched",
    "comparison_mismatch_count_zero",
    "comparison_scenario_counts_align",
}

NON_CLAIM_KEYS = {
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
    "minimum_lawful_system_completed",
}


class IntegrityHostV0MinCoexistenceExecutionAuthorityResolverTests(
    unittest.TestCase
):
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

    def build_preserved_stack(
        self,
        temp_root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, dict[str, Any], Path, dict[str, Any], Path, dict[str, Any]]:
        source_run_dir, source_manifest = self.emit_source_run(temp_root, run_name)
        ingress_run_dir, ingress_manifest = self.emit_ingress_run(
            temp_root,
            source_run_dir,
        )
        comparison_path, comparison = self.emit_comparison_artifact(
            temp_root,
            source_run_dir,
            ingress_run_dir,
        )
        return (
            source_run_dir,
            source_manifest,
            ingress_run_dir,
            ingress_manifest,
            comparison_path,
            comparison,
        )

    def resolve(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
            return resolver.resolve_current_execution_authority()

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

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_resolution_shape(self, resolution: dict[str, Any]) -> None:
        self.assertEqual(set(resolution), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(resolution["resolution_metadata"], dict)
        self.assertIsInstance(resolution["canonical_execution_line"], dict)
        self.assertIsInstance(resolution["candidate_runs"], list)
        self.assertIsInstance(resolution["authority_decision"], dict)
        self.assertIsInstance(resolution["forced_system_pressure_signals"], dict)
        self.assertIsInstance(resolution["non_claims"], dict)

    def test_source_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir).resolve()
            (root / "not_a_run").mkdir()
            first = root / "run_20260420T000000_000000Z"
            latest = root / "run_20260420T000001_000000Z"
            latest.mkdir()
            first.mkdir()
            (root / "run_20260420T999999_000000Z.json").write_text(
                "{}\n",
                encoding="utf-8",
            )

            found = resolver.discover_source_run_directories(root)

            self.assertEqual(found, [first.resolve(), latest.resolve()])
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_source_run_directories(root / "missing")
            not_dir = root / "not_dir"
            not_dir.write_text("{}\n", encoding="utf-8")
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_source_run_directories(not_dir)

    def test_ingress_run_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir).resolve()
            (root / "unrelated").mkdir()
            first = root / "run_20260420T000000_000000Z"
            latest = root / "run_20260420T000001_000000Z"
            latest.mkdir()
            first.mkdir()
            (root / "run_20260420T999999_000000Z.json").write_text(
                "{}\n",
                encoding="utf-8",
            )

            found = resolver.discover_ingress_run_directories(root)

            self.assertEqual(found, [first.resolve(), latest.resolve()])
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_ingress_run_directories(root / "missing")
            not_dir = root / "not_dir"
            not_dir.write_text("{}\n", encoding="utf-8")
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_ingress_run_directories(not_dir)

    def test_source_ingress_comparison_discovery(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir).resolve()
            unrelated = root / "other.json"
            unrelated.write_text("{}\n", encoding="utf-8")
            first = root / "a__source_ingress_comparison.json"
            latest = root / "b__source_ingress_comparison.json"
            latest.write_text("{}\n", encoding="utf-8")
            first.write_text("{}\n", encoding="utf-8")
            (root / "run_20260420T000000_000000Z").mkdir()

            found = resolver.discover_source_ingress_comparisons(root)

            self.assertEqual(found, [first.resolve(), latest.resolve()])
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_source_ingress_comparisons(root / "missing")
            not_dir = root / "not_dir"
            not_dir.write_text("{}\n", encoding="utf-8")
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_source_ingress_comparisons(not_dir)

    def test_real_authority_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)

            resolution = self.resolve(temp_root)

            self.assert_resolution_shape(resolution)

    def test_canonical_execution_line_section(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)

            canonical = resolution["canonical_execution_line"]

            self.assertEqual(
                canonical["core_execution_file"],
                "src/integrity_host_v0_min_coexistence_v2.py",
            )
            self.assertTrue(canonical["derivative_support_scope"])
            self.assertTrue(canonical["lineage_predecessor_files"])
            self.assertNotIn(
                canonical["core_execution_file"],
                canonical["lineage_predecessor_files"],
            )

    def test_candidate_run_entries(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)

            for candidate in resolution["candidate_runs"]:
                with self.subTest(source_run=candidate["source_run_directory_path"]):
                    self.assert_non_empty_string(candidate["source_run_directory_path"])
                    self.assert_non_empty_string(candidate["source_manifest_path"])
                    self.assertIsInstance(candidate["scenario_count"], int)
                    self.assertIsInstance(candidate["eligibility_checks"], dict)
                    self.assertIsInstance(candidate["eligible"], bool)
                    self.assertIsInstance(candidate["ineligibility_reasons"], list)
                    if candidate["matched_ingress_run_directory_path"] is not None:
                        self.assert_non_empty_string(
                            candidate["matched_ingress_run_directory_path"]
                        )
                    if candidate["matched_comparison_artifact_path"] is not None:
                        self.assert_non_empty_string(
                            candidate["matched_comparison_artifact_path"]
                        )

    def test_eligible_candidate_selection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            (
                source_run_dir,
                _,
                ingress_run_dir,
                _,
                comparison_path,
                _,
            ) = self.build_preserved_stack(temp_root)

            resolution = self.resolve(temp_root)
            decision = resolution["authority_decision"]
            eligible = [
                candidate
                for candidate in resolution["candidate_runs"]
                if candidate["eligible"] is True
            ]

            self.assertEqual(len(resolution["candidate_runs"]), 1)
            self.assertEqual(len(eligible), 1)
            self.assertEqual(decision["decision"], resolver.DECISION_RESOLVED)
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    decision["selected_source_run_directory_path"],
                ),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    decision["selected_ingress_run_directory_path"],
                ),
                ingress_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    decision["selected_comparison_artifact_path"],
                ),
                comparison_path.resolve(),
            )

    def test_latest_is_not_enough_rule(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, _, _, _, _ = self.build_preserved_stack(
                temp_root,
                "run_20260420T000000_000000Z",
            )
            later_source_run, _ = self.emit_source_run(
                temp_root,
                "run_20260420T000001_000000Z",
            )

            resolution = self.resolve(temp_root)
            decision = resolution["authority_decision"]
            candidates = {
                Path(candidate["source_run_directory_path"]).name: candidate
                for candidate in resolution["candidate_runs"]
            }
            later_candidate = candidates[later_source_run.name]

            self.assertEqual(decision["decision"], resolver.DECISION_RESOLVED)
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    decision["selected_source_run_directory_path"],
                ),
                source_run_dir.resolve(),
            )
            self.assertFalse(later_candidate["eligible"])
            self.assertFalse(
                later_candidate["eligibility_checks"]["matching_ingress_run_exists"]
            )
            self.assertFalse(
                later_candidate["eligibility_checks"][
                    "matching_comparison_artifact_exists"
                ]
            )
            self.assertTrue(later_candidate["ineligibility_reasons"])

    def test_no_eligible_candidate_outcome(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.emit_source_run(temp_root)
            (temp_root / resolver.INGRESS_RUNS_ROOT).mkdir(parents=True)
            (temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT).mkdir(parents=True)

            resolution = self.resolve(temp_root)
            decision = resolution["authority_decision"]

            self.assertEqual(decision["decision"], resolver.DECISION_NONE)
            self.assertEqual(decision["eligible_candidate_count"], 0)
            self.assertIsNone(decision["selected_source_run_directory_path"])
            self.assertIsNone(decision["selected_ingress_run_directory_path"])
            self.assertIsNone(decision["selected_comparison_artifact_path"])

    def test_eligibility_checks(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)
            checks = resolution["candidate_runs"][0]["eligibility_checks"]

            self.assertEqual(set(checks), EXPECTED_CHECK_KEYS)
            for key in EXPECTED_CHECK_KEYS:
                with self.subTest(check=key):
                    self.assertTrue(checks[key], key)

    def test_forced_system_pressure_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)
            signals = resolution["forced_system_pressure_signals"]

            for key in (
                "canonical_execution_authority_pressure",
                "currentness_vs_latest_emitted_pressure",
                "preserved_run_multiplicity_pressure",
            ):
                self.assertIn(key, signals)
                self.assertTrue(signals[key])

    def test_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)

            for key in NON_CLAIM_KEYS:
                self.assertIn(key, resolution["non_claims"])
                self.assertFalse(resolution["non_claims"][key])

    def test_resolution_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)

            summary = resolver.build_execution_authority_summary(resolution)

            for key in (
                "core_execution_file",
                "candidate_run_count",
                "eligible_candidate_count",
                "selected_source_run_directory_path",
                "selected_ingress_run_directory_path",
                "selected_comparison_artifact_path",
                "decision",
                "decision_reason",
            ):
                self.assertIn(key, summary)
            self.assertEqual(summary["eligible_candidate_count"], 1)
            self.assertEqual(summary["decision"], resolver.DECISION_RESOLVED)

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)
            output_path = temp_root / "nested" / "authority" / "resolution.json"

            with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
                written = resolver.write_resolution(resolution, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                    resolver.write_resolution(resolution, output_path)

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            resolution = self.resolve(temp_root)

            with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
                first = resolver.write_resolution(resolution)
                first_text = first.read_text(encoding="utf-8")
                second = resolver.write_resolution(resolution)

            self.assertEqual(
                first,
                temp_root
                / resolver.RESOLUTION_OUTPUT_ROOT
                / "current_execution_authority_resolution.json",
            )
            self.assertEqual(
                second,
                temp_root
                / resolver.RESOLUTION_OUTPUT_ROOT
                / "current_execution_authority_resolution_001.json",
            )
            self.assertEqual(first.read_text(encoding="utf-8"), first_text)
            self.assertTrue(second.exists())

    def test_main_runner_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            stdout = io.StringIO()

            with (
                mock.patch.object(resolver, "_repo_root", return_value=temp_root),
                contextlib.redirect_stdout(stdout),
            ):
                resolver.main()

            output = stdout.getvalue()

            self.assertIn("Candidate runs: 1", output)
            self.assertIn("Eligible candidates: 1", output)
            self.assertIn("Selected source run:", output)
            self.assertIn("Selected ingress run:", output)
            self.assertIn(f"Decision: {resolver.DECISION_RESOLVED}", output)
            self.assertIn("Resolution artifact:", output)

    def test_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()

            with mock.patch.object(resolver, "_repo_root", return_value=temp_root):
                with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                    resolver.resolve_current_execution_authority()

            source_run_dir, source_manifest, _, _, _, _ = self.build_preserved_stack(
                temp_root
            )
            malformed_source = copy.deepcopy(source_manifest)
            malformed_source["scenario_count"] += 1
            self.write_json(source_run_dir / "manifest.json", malformed_source)
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                self.resolve(temp_root)

            self.write_json(source_run_dir / "manifest.json", source_manifest)
            comparison_root = temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT
            for path in comparison_root.glob("*__source_ingress_comparison.json"):
                malformed_comparison = self.read_json(path)
                malformed_comparison.pop("all_matched")
                self.write_json(path, malformed_comparison)
                break
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                self.resolve(temp_root)

            wrong_type_root = temp_root / "wrong_type_roots"
            wrong_type_root.mkdir()
            file_root = wrong_type_root / "source_root"
            file_root.write_text("{}\n", encoding="utf-8")
            with self.assertRaises(resolver.ExecutionAuthorityResolutionError):
                resolver.discover_source_run_directories(file_root)

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            source_root = temp_root / resolver.SOURCE_RUNS_ROOT
            ingress_root = temp_root / resolver.INGRESS_RUNS_ROOT
            comparison_root = temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT
            source_before = self.json_texts(source_root)
            ingress_before = self.json_texts(ingress_root)
            comparison_before = self.json_texts(comparison_root)

            first = self.resolve(temp_root)
            source_after_first = self.json_texts(source_root)
            ingress_after_first = self.json_texts(ingress_root)
            comparison_after_first = self.json_texts(comparison_root)
            second = self.resolve(temp_root)
            source_after_second = self.json_texts(source_root)
            ingress_after_second = self.json_texts(ingress_root)
            comparison_after_second = self.json_texts(comparison_root)

            self.assertEqual(source_after_first, source_before)
            self.assertEqual(source_after_second, source_before)
            self.assertEqual(ingress_after_first, ingress_before)
            self.assertEqual(ingress_after_second, ingress_before)
            self.assertEqual(comparison_after_first, comparison_before)
            self.assertEqual(comparison_after_second, comparison_before)
            self.assertEqual(first["authority_decision"], second["authority_decision"])
            self.assertEqual(
                first["canonical_execution_line"],
                second["canonical_execution_line"],
            )


if __name__ == "__main__":
    unittest.main()
