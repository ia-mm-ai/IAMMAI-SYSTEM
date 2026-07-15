"""Bounded tests for the v0-min coexistence run-family packet builder.

These tests lock the current additive preserved-run family surface in
``src/build_integrity_host_v0_min_coexistence_run_family_packet.py`` using real
source scenario runs, receiving-ingress runs, source-to-ingress comparisons,
and execution-authority resolution artifacts emitted into temporary roots.

They verify packet shape, canonical execution-line carry-through, authority
reference, preserved-run entries, currentness posture, forced-pressure signals,
non-claims, write behavior, failure posture, and read-only behavior. They do
not test replay, merge, persistence architecture, registry integration,
distributed continuity, CLI behavior, or broad governance frameworks.
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

import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder  # noqa: E402
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "family_metadata",
    "canonical_execution_line",
    "authority_reference",
    "preserved_runs",
    "currentness_status",
    "forced_system_pressure_signals",
    "non_claims",
}

EXPECTED_NON_CLAIMS = {
    "continuity_completed",
    "standing_upgraded",
    "replayed_into_live_host",
    "merged_into_local_state",
    "minimum_lawful_system_completed",
    "final_system_identity_completed",
}


class IntegrityHostV0MinCoexistenceRunFamilyPacketTests(unittest.TestCase):
    def emit_source_run(
        self,
        temp_root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[Path, dict[str, Any]]:
        source_root = temp_root / family_builder.SOURCE_RUNS_ROOT
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
                / family_builder.SOURCE_INGRESS_COMPARISON_ROOT
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

    def build_preserved_stack(
        self,
        temp_root: Path,
        run_name: str = "run_20260420T000000_000000Z",
    ) -> tuple[
        Path,
        dict[str, Any],
        Path,
        dict[str, Any],
        Path,
        dict[str, Any],
        Path,
        dict[str, Any],
    ]:
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
        resolution_path, resolution = self.emit_authority_resolution(temp_root)
        return (
            source_run_dir,
            source_manifest,
            ingress_run_dir,
            ingress_manifest,
            comparison_path,
            comparison,
            resolution_path,
            resolution,
        )

    def build_packet(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
            return family_builder.build_run_family_packet()

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

    def assert_packet_shape(self, packet: dict[str, Any]) -> None:
        self.assertEqual(set(packet), EXPECTED_TOP_LEVEL_KEYS)
        self.assertIsInstance(packet["family_metadata"], dict)
        self.assertIsInstance(packet["canonical_execution_line"], dict)
        self.assertIsInstance(packet["authority_reference"], dict)
        self.assertIsInstance(packet["preserved_runs"], list)
        self.assertIsInstance(packet["currentness_status"], dict)
        self.assertIsInstance(packet["forced_system_pressure_signals"], dict)
        self.assertIsInstance(packet["non_claims"], dict)

    def test_real_family_packet_build(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)

            packet = self.build_packet(temp_root)

            self.assert_packet_shape(packet)

    def test_family_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            metadata = packet["family_metadata"]

            for key in (
                "family_type",
                "family_version",
                "generated_at",
                "builder_module",
            ):
                self.assert_non_empty_string(metadata[key])

    def test_canonical_execution_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            canonical = packet["canonical_execution_line"]

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

    def test_authority_reference(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            (
                source_run_dir,
                _,
                ingress_run_dir,
                _,
                comparison_path,
                _,
                resolution_path,
                resolution,
            ) = self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            authority = packet["authority_reference"]

            self.assertEqual(
                self.resolve_display_path(temp_root, authority["resolution_artifact_path"]),
                resolution_path.resolve(),
            )
            self.assertEqual(
                authority["authority_decision"],
                resolution["authority_decision"]["decision"],
            )
            self.assertEqual(
                authority["authority_decision_reason"],
                resolution["authority_decision"]["decision_reason"],
            )
            self.assertEqual(
                self.resolve_display_path(temp_root, authority["selected_source_run_path"]),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(temp_root, authority["selected_ingress_run_path"]),
                ingress_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    authority["selected_comparison_artifact_path"],
                ),
                comparison_path.resolve(),
            )
            self.assertEqual(authority["candidate_run_count"], 1)
            self.assertEqual(authority["eligible_candidate_count"], 1)

    def test_preserved_runs(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, source_manifest, ingress_run_dir, _, comparison_path, _, _, _ = (
                self.build_preserved_stack(temp_root)
            )
            packet = self.build_packet(temp_root)

            self.assertEqual(len(packet["preserved_runs"]), 1)
            entry = packet["preserved_runs"][0]

            self.assertEqual(
                self.resolve_display_path(temp_root, entry["source_run_directory_path"]),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(temp_root, entry["source_manifest_path"]),
                (source_run_dir / "manifest.json").resolve(),
            )
            self.assertEqual(entry["scenario_count"], source_manifest["scenario_count"])
            self.assertEqual(
                self.resolve_display_path(temp_root, entry["matched_ingress_run_path"]),
                ingress_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    entry["matched_comparison_artifact_path"],
                ),
                comparison_path.resolve(),
            )
            self.assertIsInstance(entry["current_authority"], bool)
            self.assertTrue(entry["current_authority"])
            self.assertIsInstance(entry["candidate_eligible"], bool)
            self.assertTrue(entry["candidate_eligible"])
            self.assertIsInstance(entry["ineligibility_reasons"], list)
            self.assertEqual(entry["ineligibility_reasons"], [])

            signals = entry["preservation_signals"]
            for key in (
                "source_preserved",
                "ingress_preserved",
                "comparison_preserved",
                "authority_candidate_visible",
            ):
                self.assertIn(key, signals)
                self.assertTrue(signals[key])

    def test_currentness_status(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _, _, _, _, _ = (
                self.build_preserved_stack(temp_root)
            )
            packet = self.build_packet(temp_root)

            status = packet["currentness_status"]

            for key in (
                "current_execution_authority_exists",
                "current_execution_authority_source_run_path",
                "current_execution_authority_ingress_run_path",
                "current_execution_authority_resolved_by_explicit_checks",
                "latest_emitted_is_not_authority_by_default",
                "preserved_run_count",
                "eligible_run_count",
            ):
                self.assertIn(key, status)
            self.assertTrue(status["current_execution_authority_exists"])
            self.assertTrue(
                status["current_execution_authority_resolved_by_explicit_checks"]
            )
            self.assertTrue(status["latest_emitted_is_not_authority_by_default"])
            self.assertEqual(status["preserved_run_count"], 1)
            self.assertEqual(status["eligible_run_count"], 1)
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    status["current_execution_authority_source_run_path"],
                ),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    status["current_execution_authority_ingress_run_path"],
                ),
                ingress_run_dir.resolve(),
            )

    def test_forced_system_pressure_signals(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)
            signals = packet["forced_system_pressure_signals"]

            for key in (
                "canonical_execution_authority_pressure",
                "currentness_vs_latest_emitted_pressure",
                "preserved_run_multiplicity_pressure",
                "bounded_run_family_system_identity_pressure",
            ):
                self.assertIn(key, signals)
                self.assertTrue(signals[key])

    def test_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, packet["non_claims"])
                self.assertFalse(packet["non_claims"][key])

    def test_family_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            summary = family_builder.build_run_family_summary(packet)

            for key in (
                "core_execution_file",
                "preserved_run_count",
                "eligible_run_count",
                "current_authority_source_run_path",
                "current_authority_ingress_run_path",
                "authority_decision",
                "authority_decision_reason",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(
                summary["core_execution_file"],
                "src/integrity_host_v0_min_coexistence_v2.py",
            )
            self.assertGreaterEqual(summary["preserved_run_count"], 1)
            self.assertGreaterEqual(summary["eligible_run_count"], 1)
            self.assertEqual(summary["authority_decision"], resolver.DECISION_RESOLVED)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)
            output_path = temp_root / "nested" / "family" / "packet.json"

            with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
                written = family_builder.write_run_family_packet(packet, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(family_builder.RunFamilyPacketError):
                    family_builder.write_run_family_packet(packet, output_path)

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_packet(temp_root)

            with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
                first = family_builder.write_run_family_packet(packet)
                first_text = first.read_text(encoding="utf-8")
                second = family_builder.write_run_family_packet(packet)

            self.assertEqual(
                first,
                temp_root
                / family_builder.RUN_FAMILY_PACKET_ROOT
                / "current_run_family_packet.json",
            )
            self.assertEqual(
                second,
                temp_root
                / family_builder.RUN_FAMILY_PACKET_ROOT
                / "current_run_family_packet_001.json",
            )
            self.assertEqual(first.read_text(encoding="utf-8"), first_text)
            self.assertTrue(second.exists())

    def test_missing_authority_artifact_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root)
            ingress_run_dir, _ = self.emit_ingress_run(temp_root, source_run_dir)
            self.emit_comparison_artifact(temp_root, source_run_dir, ingress_run_dir)
            (temp_root / family_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(family_builder.RunFamilyPacketError):
                    family_builder.build_run_family_packet()

    def test_malformed_authority_artifact_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            authority_root = temp_root / family_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT
            for path in authority_root.glob("current_execution_authority_resolution*.json"):
                self.write_json(path, {"malformed": True})
                break

            with mock.patch.object(family_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(family_builder.RunFamilyPacketError):
                    family_builder.build_run_family_packet()

    def test_no_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            source_root = temp_root / family_builder.SOURCE_RUNS_ROOT
            ingress_root = temp_root / family_builder.INGRESS_RUNS_ROOT
            comparison_root = temp_root / family_builder.SOURCE_INGRESS_COMPARISON_ROOT
            authority_root = (
                temp_root / family_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT
            )
            source_before = self.json_texts(source_root)
            ingress_before = self.json_texts(ingress_root)
            comparison_before = self.json_texts(comparison_root)
            authority_before = self.json_texts(authority_root)

            first = self.build_packet(temp_root)
            source_after_first = self.json_texts(source_root)
            ingress_after_first = self.json_texts(ingress_root)
            comparison_after_first = self.json_texts(comparison_root)
            authority_after_first = self.json_texts(authority_root)
            second = self.build_packet(temp_root)
            source_after_second = self.json_texts(source_root)
            ingress_after_second = self.json_texts(ingress_root)
            comparison_after_second = self.json_texts(comparison_root)
            authority_after_second = self.json_texts(authority_root)

            self.assertEqual(source_after_first, source_before)
            self.assertEqual(source_after_second, source_before)
            self.assertEqual(ingress_after_first, ingress_before)
            self.assertEqual(ingress_after_second, ingress_before)
            self.assertEqual(comparison_after_first, comparison_before)
            self.assertEqual(comparison_after_second, comparison_before)
            self.assertEqual(authority_after_first, authority_before)
            self.assertEqual(authority_after_second, authority_before)
            self.assertEqual(first["authority_reference"], second["authority_reference"])
            self.assertEqual(
                first["canonical_execution_line"],
                second["canonical_execution_line"],
            )


if __name__ == "__main__":
    unittest.main()
