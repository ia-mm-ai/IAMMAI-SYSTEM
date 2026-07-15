"""Bounded tests for the v0-min coexistence preserved-run status packet.

These tests lock the current additive preserved-run status surface in
``src/build_integrity_host_v0_min_coexistence_preserved_run_status_packet.py``
using real source scenario runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, and run-family packets emitted
into temporary roots.

They verify status packet shape, canonical execution-line carry-through,
authority reference, preserved-run role assignment, no-authority posture,
bounded pressure signals, non-claims, write behavior, clear malformed input
failures, and read-only behavior. They do not test replay, merge, persistence
architecture, registry integration, distributed continuity, CLI behavior, or
broad governance frameworks.
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

import build_integrity_host_v0_min_coexistence_preserved_run_status_packet as status_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_run_family_packet as family_builder  # noqa: E402
import compare_integrity_host_v0_min_coexistence_source_and_ingress_run as comparer  # noqa: E402
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "status_packet_metadata",
    "canonical_execution_line",
    "authority_reference",
    "preserved_run_status_entries",
    "aggregate_status_counts",
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
    "final_preserved_run_governance_completed",
}


class IntegrityHostV0MinCoexistencePreservedRunStatusPacketTests(
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
        family_path, family_packet = self.emit_family_packet(temp_root)
        return (
            source_run_dir,
            source_manifest,
            ingress_run_dir,
            ingress_manifest,
            comparison_path,
            comparison,
            resolution_path,
            resolution,
            family_path,
            family_packet,
        )

    def build_multi_run_preserved_stack(
        self,
        temp_root: Path,
    ) -> tuple[Path, Path, Path, dict[str, Any], Path, dict[str, Any]]:
        first_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000000_000000Z",
        )
        first_ingress_run, _ = self.emit_ingress_run(temp_root, first_source_run)
        self.emit_comparison_artifact(temp_root, first_source_run, first_ingress_run)

        latest_source_run, _ = self.emit_source_run(
            temp_root,
            "run_20260420T000001_000000Z",
        )
        latest_ingress_run, _ = self.emit_ingress_run(temp_root, latest_source_run)
        self.emit_comparison_artifact(temp_root, latest_source_run, latest_ingress_run)

        resolution_path, resolution = self.emit_authority_resolution(temp_root)
        family_path, family_packet = self.emit_family_packet(temp_root)
        return (
            first_source_run,
            latest_source_run,
            resolution_path,
            resolution,
            family_path,
            family_packet,
        )

    def build_no_authority_stack(
        self,
        temp_root: Path,
    ) -> tuple[Path, Path, dict[str, Any], Path, dict[str, Any]]:
        source_run_dir, _ = self.emit_source_run(temp_root)
        (temp_root / resolver.INGRESS_RUNS_ROOT).mkdir(parents=True, exist_ok=True)
        (temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT).mkdir(
            parents=True,
            exist_ok=True,
        )
        resolution_path, resolution = self.emit_authority_resolution(temp_root)
        family_path, family_packet = self.emit_family_packet(temp_root)
        return source_run_dir, resolution_path, resolution, family_path, family_packet

    def build_status_packet(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
            return status_builder.build_preserved_run_status_packet()

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
        self.assertIsInstance(packet["status_packet_metadata"], dict)
        self.assertIsInstance(packet["canonical_execution_line"], dict)
        self.assertIsInstance(packet["authority_reference"], dict)
        self.assertIsInstance(packet["preserved_run_status_entries"], list)
        self.assertIsInstance(packet["aggregate_status_counts"], dict)
        self.assertIsInstance(packet["forced_system_pressure_signals"], dict)
        self.assertIsInstance(packet["non_claims"], dict)

    def roles(self, packet: dict[str, Any]) -> list[str]:
        return [
            entry["status_role"]
            for entry in packet["preserved_run_status_entries"]
        ]

    def test_real_preserved_run_status_packet_build(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)

            packet = self.build_status_packet(temp_root)

            self.assert_packet_shape(packet)

    def test_status_packet_metadata_and_canonical_execution_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)

            metadata = packet["status_packet_metadata"]
            canonical = packet["canonical_execution_line"]

            for key in (
                "status_packet_type",
                "status_packet_version",
                "generated_at",
                "builder_module",
            ):
                self.assert_non_empty_string(metadata[key])
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

    def test_authority_reference_aligns_with_resolution_artifact(self) -> None:
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
                family_path,
                _,
            ) = self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)

            authority = packet["authority_reference"]

            self.assertEqual(
                self.resolve_display_path(temp_root, authority["authority_artifact_path"]),
                resolution_path.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    authority["run_family_packet_artifact_path"],
                ),
                family_path.resolve(),
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

    def test_preserved_run_status_entries_and_single_run_role(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _, ingress_run_dir, _, comparison_path, _, _, _, _, _ = (
                self.build_preserved_stack(temp_root)
            )
            packet = self.build_status_packet(temp_root)

            self.assertEqual(len(packet["preserved_run_status_entries"]), 1)
            entry = packet["preserved_run_status_entries"][0]

            self.assertEqual(
                self.resolve_display_path(temp_root, entry["source_run_directory_path"]),
                source_run_dir.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(temp_root, entry["source_manifest_path"]),
                (source_run_dir / "manifest.json").resolve(),
            )
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
            self.assertEqual(
                entry["status_role"],
                status_builder.ROLE_CURRENT_AUTHORITY,
            )
            self.assertTrue(entry["current_authority"])
            self.assertTrue(entry["candidate_eligible"])
            self.assert_non_empty_string(entry["status_reason"])
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

    def test_multi_run_role_assignment_and_aggregate_counts(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            first_run, latest_run, _, resolution, _, _ = (
                self.build_multi_run_preserved_stack(temp_root)
            )
            packet = self.build_status_packet(temp_root)

            entries = packet["preserved_run_status_entries"]
            roles = self.roles(packet)
            aggregate = packet["aggregate_status_counts"]
            current_entries = [
                entry
                for entry in entries
                if entry["status_role"] == status_builder.ROLE_CURRENT_AUTHORITY
            ]
            eligible_non_authority = [
                entry
                for entry in entries
                if entry["status_role"] == status_builder.ROLE_ELIGIBLE_NON_AUTHORITY
            ]

            self.assertEqual(len(entries), 2)
            self.assertEqual(len(current_entries), 1)
            self.assertEqual(len(eligible_non_authority), 1)
            self.assertNotIn(status_builder.ROLE_INELIGIBLE, roles)
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    current_entries[0]["source_run_directory_path"],
                ),
                latest_run.resolve(),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    packet["authority_reference"]["selected_source_run_path"],
                ),
                self.resolve_display_path(
                    temp_root,
                    resolution["authority_decision"][
                        "selected_source_run_directory_path"
                    ],
                ),
            )
            self.assertEqual(
                self.resolve_display_path(
                    temp_root,
                    eligible_non_authority[0]["source_run_directory_path"],
                ),
                first_run.resolve(),
            )
            self.assertEqual(aggregate["preserved_run_count"], 2)
            self.assertEqual(aggregate["eligible_run_count"], 2)
            self.assertEqual(aggregate["current_authority_run_count"], 1)
            self.assertEqual(
                aggregate["preserved_eligible_non_authority_count"],
                1,
            )
            self.assertEqual(aggregate["preserved_ineligible_count"], 0)

    def test_forced_system_pressure_signals_and_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)

            signals = packet["forced_system_pressure_signals"]
            for key in (
                "canonical_execution_authority_pressure",
                "currentness_vs_latest_emitted_pressure",
                "preserved_run_multiplicity_pressure",
                "preserved_run_status_pressure",
            ):
                self.assertIn(key, signals)
                self.assertTrue(signals[key])

            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, packet["non_claims"])
                self.assertFalse(packet["non_claims"][key])

    def test_status_logic_without_current_authority(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_no_authority_stack(temp_root)

            packet = self.build_status_packet(temp_root)

            roles = self.roles(packet)
            self.assertNotIn(status_builder.ROLE_CURRENT_AUTHORITY, roles)
            self.assertIn(status_builder.ROLE_INELIGIBLE, roles)
            self.assertIsNone(
                packet["authority_reference"]["selected_source_run_path"]
            )
            self.assertEqual(
                packet["authority_reference"]["authority_decision"],
                resolver.DECISION_NONE,
            )
            self.assertEqual(
                packet["aggregate_status_counts"]["current_authority_run_count"],
                0,
            )
            for entry in packet["preserved_run_status_entries"]:
                self.assertIsInstance(entry["candidate_eligible"], bool)
                self.assertIsInstance(entry["ineligibility_reasons"], list)
                self.assert_non_empty_string(entry["status_reason"])

    def test_family_authority_correspondence_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            family_root = temp_root / status_builder.RUN_FAMILY_PACKET_ROOT
            family_path = next(
                family_root.glob("current_run_family_packet*.json")
            )
            family_packet = self.read_json(family_path)
            family_packet["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            self.write_json(family_path, family_packet)

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    status_builder.PreservedRunStatusPacketError
                ):
                    status_builder.build_preserved_run_status_packet()

    def test_missing_artifact_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            (temp_root / status_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )
            (temp_root / status_builder.RUN_FAMILY_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    status_builder.PreservedRunStatusPacketError
                ):
                    status_builder.build_preserved_run_status_packet()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root)
            ingress_run_dir, _ = self.emit_ingress_run(temp_root, source_run_dir)
            self.emit_comparison_artifact(temp_root, source_run_dir, ingress_run_dir)
            self.emit_authority_resolution(temp_root)
            (temp_root / status_builder.RUN_FAMILY_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    status_builder.PreservedRunStatusPacketError
                ):
                    status_builder.build_preserved_run_status_packet()

    def test_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)

            summary = status_builder.build_preserved_run_status_summary(packet)

            for key in (
                "core_execution_file",
                "preserved_run_count",
                "eligible_run_count",
                "current_authority_run_count",
                "preserved_eligible_non_authority_count",
                "preserved_ineligible_count",
                "selected_current_authority_source_run_path",
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
            self.assertEqual(summary["current_authority_run_count"], 1)
            self.assertEqual(
                summary["authority_decision"],
                resolver.DECISION_RESOLVED,
            )
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)
            output_path = temp_root / "nested" / "status" / "packet.json"

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                written = status_builder.write_preserved_run_status_packet(
                    packet,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(
                    status_builder.PreservedRunStatusPacketError
                ):
                    status_builder.write_preserved_run_status_packet(
                        packet,
                        output_path,
                    )

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_status_packet(temp_root)

            with mock.patch.object(status_builder, "_repo_root", return_value=temp_root):
                first = status_builder.write_preserved_run_status_packet(packet)
                first_text = first.read_text(encoding="utf-8")
                second = status_builder.write_preserved_run_status_packet(packet)

            self.assertEqual(
                first,
                temp_root
                / status_builder.PRESERVED_RUN_STATUS_PACKET_ROOT
                / "current_preserved_run_status_packet.json",
            )
            self.assertEqual(
                second,
                temp_root
                / status_builder.PRESERVED_RUN_STATUS_PACKET_ROOT
                / "current_preserved_run_status_packet_001.json",
            )
            self.assertEqual(first.read_text(encoding="utf-8"), first_text)
            self.assertTrue(second.exists())

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            source_root = temp_root / resolver.SOURCE_RUNS_ROOT
            ingress_root = temp_root / resolver.INGRESS_RUNS_ROOT
            comparison_root = temp_root / resolver.SOURCE_INGRESS_COMPARISON_ROOT
            authority_root = temp_root / status_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT
            family_root = temp_root / status_builder.RUN_FAMILY_PACKET_ROOT

            before = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
            }

            first = self.build_status_packet(temp_root)
            after_first = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
            }
            second = self.build_status_packet(temp_root)
            after_second = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["authority_reference"], second["authority_reference"])
            self.assertEqual(
                first["preserved_run_status_entries"],
                second["preserved_run_status_entries"],
            )
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
