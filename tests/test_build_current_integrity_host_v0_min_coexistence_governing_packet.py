"""Bounded tests for the v0-min coexistence current-governing packet.

These tests lock the current additive governing surface in
``src/build_current_integrity_host_v0_min_coexistence_governing_packet.py``
using real source scenario runs, receiving-ingress runs, source-to-ingress
comparisons, execution-authority resolutions, run-family packets, and
preserved-run status packets emitted into temporary roots.

They verify packet shape, canonical execution-line carry-through, authority
reference, current governing run selection, preserved non-governing run
visibility, bounded governing scope, non-claims, write behavior, clear
malformed input failures, and read-only behavior. They do not test replay,
merge, persistence architecture, registry integration, distributed continuity,
CLI behavior, or broad governance frameworks.
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
import resolve_current_integrity_host_v0_min_coexistence_execution_authority as resolver  # noqa: E402
import run_integrity_host_v0_min_coexistence_receiving_ingress as ingress_runner  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as scenario_runner  # noqa: E402


EXPECTED_TOP_LEVEL_KEYS = {
    "governing_packet_metadata",
    "canonical_execution_line",
    "authority_reference",
    "current_governing_run",
    "preserved_non_governing_runs",
    "governing_scope",
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
    "final_governing_scope_completed",
}


class IntegrityHostV0MinCoexistenceCurrentGoverningPacketTests(unittest.TestCase):
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
        status_path, status_packet = self.emit_status_packet(temp_root)
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
            status_path,
            status_packet,
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
        self.emit_family_packet(temp_root)
        status_path, status_packet = self.emit_status_packet(temp_root)
        return (
            first_source_run,
            latest_source_run,
            resolution_path,
            resolution,
            status_path,
            status_packet,
        )

    def build_governing_packet(self, temp_root: Path) -> dict[str, Any]:
        with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
            return governing_builder.build_current_governing_packet()

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
        self.assertIsInstance(packet["governing_packet_metadata"], dict)
        self.assertIsInstance(packet["canonical_execution_line"], dict)
        self.assertIsInstance(packet["authority_reference"], dict)
        self.assertIsInstance(packet["current_governing_run"], dict)
        self.assertIsInstance(packet["preserved_non_governing_runs"], list)
        self.assertIsInstance(packet["governing_scope"], dict)
        self.assertIsInstance(packet["forced_system_pressure_signals"], dict)
        self.assertIsInstance(packet["non_claims"], dict)

    def test_real_current_governing_packet_build(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)

            packet = self.build_governing_packet(temp_root)

            self.assert_packet_shape(packet)

    def test_metadata_and_canonical_execution_line(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

            metadata = packet["governing_packet_metadata"]
            canonical = packet["canonical_execution_line"]

            for key in (
                "governing_packet_type",
                "governing_packet_version",
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

    def test_authority_reference_aligns_with_emitted_artifacts(self) -> None:
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
                status_path,
                _,
            ) = self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

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
                self.resolve_display_path(
                    temp_root,
                    authority["preserved_run_status_packet_artifact_path"],
                ),
                status_path.resolve(),
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

    def test_current_governing_run_is_sourced_from_status_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            _, _, _, _, _, _, _, _, _, _, _, status_packet = (
                self.build_preserved_stack(temp_root)
            )
            packet = self.build_governing_packet(temp_root)

            current = packet["current_governing_run"]
            status_current = [
                entry
                for entry in status_packet["preserved_run_status_entries"]
                if entry["status_role"] == status_builder.ROLE_CURRENT_AUTHORITY
            ][0]

            for key in (
                "source_run_directory_path",
                "source_manifest_path",
                "matched_ingress_run_path",
                "matched_comparison_artifact_path",
                "status_role",
                "governing_reason",
            ):
                self.assert_non_empty_string(current[key])
            self.assertEqual(
                self.resolve_display_path(temp_root, current["source_run_directory_path"]),
                self.resolve_display_path(
                    temp_root,
                    status_current["source_run_directory_path"],
                ),
            )
            self.assertEqual(current["status_role"], status_builder.ROLE_CURRENT_AUTHORITY)
            self.assertTrue(current["current_authority"])
            self.assertTrue(current["candidate_eligible"])
            self.assertIsInstance(current["preservation_signals"], dict)
            self.assertIsInstance(current["non_claims"], dict)

    def test_preserved_non_governing_runs_remain_visible(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            first_run, latest_run, _, _, _, status_packet = (
                self.build_multi_run_preserved_stack(temp_root)
            )
            packet = self.build_governing_packet(temp_root)

            current = packet["current_governing_run"]
            non_governing = packet["preserved_non_governing_runs"]
            status_non_current = [
                entry
                for entry in status_packet["preserved_run_status_entries"]
                if entry["status_role"] != status_builder.ROLE_CURRENT_AUTHORITY
            ]

            self.assertEqual(len(non_governing), len(status_non_current))
            self.assertEqual(len(non_governing), 1)
            self.assertEqual(
                self.resolve_display_path(temp_root, current["source_run_directory_path"]),
                latest_run.resolve(),
            )
            entry = non_governing[0]
            self.assertEqual(
                self.resolve_display_path(temp_root, entry["source_run_directory_path"]),
                first_run.resolve(),
            )
            for key in (
                "source_run_directory_path",
                "source_manifest_path",
                "status_role",
                "status_reason",
            ):
                self.assert_non_empty_string(entry[key])
            self.assertIsInstance(entry["current_authority"], bool)
            self.assertFalse(entry["current_authority"])
            self.assertIsInstance(entry["candidate_eligible"], bool)
            self.assertTrue(entry["candidate_eligible"])
            self.assertIsInstance(entry["ineligibility_reasons"], list)
            self.assertIsInstance(entry["preservation_signals"], dict)

    def test_governing_scope(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

            scope = packet["governing_scope"]
            current = packet["current_governing_run"]

            self.assertEqual(
                scope["governing_core_execution_file"],
                packet["canonical_execution_line"]["core_execution_file"],
            )
            self.assertEqual(
                scope["governing_source_run_path"],
                current["source_run_directory_path"],
            )
            self.assertEqual(
                scope["governing_ingress_run_path"],
                current["matched_ingress_run_path"],
            )
            self.assertEqual(
                scope["governing_comparison_artifact_path"],
                current["matched_comparison_artifact_path"],
            )
            for key in (
                "governing_is_bounded",
                "governing_applies_to_current_execution_line",
                "preserved_non_governing_runs_remain_preserved",
                "current_authority_does_not_erase_preserved_runs",
            ):
                self.assertIn(key, scope)
                self.assertTrue(scope[key])

    def test_forced_pressure_signals_and_non_claims(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

            signals = packet["forced_system_pressure_signals"]
            for key in (
                "canonical_execution_authority_pressure",
                "currentness_vs_latest_emitted_pressure",
                "preserved_run_multiplicity_pressure",
                "preserved_run_status_pressure",
                "current_governing_scope_pressure",
            ):
                self.assertIn(key, signals)
                self.assertTrue(signals[key])

            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, packet["non_claims"])
                self.assertFalse(packet["non_claims"][key])

    def test_governing_logic_without_current_authority_fails(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            status_path = next(
                (temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT).glob(
                    "current_preserved_run_status_packet*.json"
                )
            )
            status_packet = self.read_json(status_path)
            for entry in status_packet["preserved_run_status_entries"]:
                if entry["status_role"] == status_builder.ROLE_CURRENT_AUTHORITY:
                    entry["status_role"] = status_builder.ROLE_INELIGIBLE
                    entry["current_authority"] = False
                    entry["candidate_eligible"] = False
                    entry["status_reason"] = "TEMP_TEST_REMOVED_CURRENT_AUTHORITY"
                    entry["ineligibility_reasons"] = [
                        "temporary test removed current authority"
                    ]
            status_packet["aggregate_status_counts"]["eligible_run_count"] = 0
            status_packet["aggregate_status_counts"]["current_authority_run_count"] = 0
            status_packet["aggregate_status_counts"]["preserved_ineligible_count"] = 1
            self.write_json(status_path, status_packet)

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.build_current_governing_packet()

    def test_artifact_correspondence_failure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            status_path = next(
                (temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT).glob(
                    "current_preserved_run_status_packet*.json"
                )
            )
            status_packet = self.read_json(status_path)
            status_packet["canonical_execution_line"]["core_execution_file"] = (
                "src/not_the_current_core.py"
            )
            self.write_json(status_path, status_packet)

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.build_current_governing_packet()

    def test_missing_artifact_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            (temp_root / governing_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )
            (temp_root / governing_builder.RUN_FAMILY_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )
            (temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.build_current_governing_packet()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root)
            ingress_run_dir, _ = self.emit_ingress_run(temp_root, source_run_dir)
            self.emit_comparison_artifact(temp_root, source_run_dir, ingress_run_dir)
            self.emit_authority_resolution(temp_root)
            (temp_root / governing_builder.RUN_FAMILY_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )
            (temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.build_current_governing_packet()

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            source_run_dir, _ = self.emit_source_run(temp_root)
            ingress_run_dir, _ = self.emit_ingress_run(temp_root, source_run_dir)
            self.emit_comparison_artifact(temp_root, source_run_dir, ingress_run_dir)
            self.emit_authority_resolution(temp_root)
            self.emit_family_packet(temp_root)
            (temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT).mkdir(
                parents=True,
                exist_ok=True,
            )

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.build_current_governing_packet()

    def test_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

            summary = governing_builder.build_current_governing_summary(packet)

            for key in (
                "core_execution_file",
                "current_governing_source_run_path",
                "current_governing_ingress_run_path",
                "preserved_non_governing_run_count",
                "authority_decision",
                "authority_decision_reason",
                "governing_scope_flags",
                "non_claims",
            ):
                self.assertIn(key, summary)
            self.assertEqual(
                summary["core_execution_file"],
                "src/integrity_host_v0_min_coexistence_v2.py",
            )
            self.assertEqual(summary["authority_decision"], resolver.DECISION_RESOLVED)
            self.assertIsInstance(summary["preserved_non_governing_run_count"], int)
            for value in summary["governing_scope_flags"].values():
                self.assertTrue(value)
            for key in EXPECTED_NON_CLAIMS:
                self.assertIn(key, summary["non_claims"])
                self.assertFalse(summary["non_claims"][key])

    def test_write_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)
            output_path = temp_root / "nested" / "governing" / "packet.json"

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                written = governing_builder.write_current_governing_packet(
                    packet,
                    output_path,
                )

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_TOP_LEVEL_KEYS)

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                with self.assertRaises(governing_builder.CurrentGoverningPacketError):
                    governing_builder.write_current_governing_packet(
                        packet,
                        output_path,
                    )

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir).resolve()
            self.build_preserved_stack(temp_root)
            packet = self.build_governing_packet(temp_root)

            with mock.patch.object(governing_builder, "_repo_root", return_value=temp_root):
                first = governing_builder.write_current_governing_packet(packet)
                first_text = first.read_text(encoding="utf-8")
                second = governing_builder.write_current_governing_packet(packet)

            self.assertEqual(
                first,
                temp_root
                / governing_builder.CURRENT_GOVERNING_PACKET_ROOT
                / "current_governing_packet.json",
            )
            self.assertEqual(
                second,
                temp_root
                / governing_builder.CURRENT_GOVERNING_PACKET_ROOT
                / "current_governing_packet_001.json",
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
            authority_root = temp_root / governing_builder.EXECUTION_AUTHORITY_RESOLUTION_ROOT
            family_root = temp_root / governing_builder.RUN_FAMILY_PACKET_ROOT
            status_root = temp_root / governing_builder.PRESERVED_RUN_STATUS_PACKET_ROOT

            before = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
                "status": self.json_texts(status_root),
            }

            first = self.build_governing_packet(temp_root)
            after_first = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
                "status": self.json_texts(status_root),
            }
            second = self.build_governing_packet(temp_root)
            after_second = {
                "source": self.json_texts(source_root),
                "ingress": self.json_texts(ingress_root),
                "comparison": self.json_texts(comparison_root),
                "authority": self.json_texts(authority_root),
                "family": self.json_texts(family_root),
                "status": self.json_texts(status_root),
            }

            self.assertEqual(after_first, before)
            self.assertEqual(after_second, before)
            self.assertEqual(first["authority_reference"], second["authority_reference"])
            self.assertEqual(first["current_governing_run"], second["current_governing_run"])
            self.assertEqual(first["preserved_non_governing_runs"], second["preserved_non_governing_runs"])
            self.assertEqual(first["non_claims"], second["non_claims"])


if __name__ == "__main__":
    unittest.main()
