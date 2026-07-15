"""Bounded tests for the v0-min coexistence receiving-packet builder.

These tests lock the current additive receiving-packet surface in
``src/build_integrity_host_v0_min_coexistence_receiving_packet.py`` using real
scenario artifacts emitted by the current local scenario runner.

They verify packet shape, source provenance, import identity, bounded receiving
status, preserved imported structure, JSON writing, default output behavior,
validation failures, and non-mutation of source artifacts. They do not test
replay, host merge, persistence architecture, registry behavior, distributed
continuity, CLI behavior, or speculative successor features.
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

import build_integrity_host_v0_min_coexistence_receiving_packet as builder  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_PACKET_KEYS = {
    "packet_metadata",
    "source_provenance",
    "import_identity",
    "receiving_status",
    "import_summary",
    "imported_packet",
}

EXPECTED_RECEIVING_STATUS = {
    "receiving_packet_exists": True,
    "imported_packet_read_only_here": True,
    "source_remains_source": True,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
    "continuity_completed": False,
    "standing_upgraded": False,
    "preserved_structure_visible": True,
}


class IntegrityHostV0MinCoexistenceReceivingPacketTests(unittest.TestCase):
    def emit_all_scenarios(self, output_dir: Path) -> dict[str, Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        emitted_paths: dict[str, Path] = {}
        for file_stem, scenario_function in runner.SCENARIOS:
            emitted = runner._emit_scenario(output_dir, file_stem, scenario_function)
            emitted_paths[emitted.scenario_id] = emitted.artifact_path
        return emitted_paths

    def emit_scenario(self, output_dir: Path, scenario_id: str) -> Path:
        for file_stem, scenario_function in runner.SCENARIOS:
            result = scenario_function()
            if result.scenario_id == scenario_id:
                emitted = runner._emit_scenario(
                    output_dir,
                    file_stem,
                    lambda result=result: result,
                )
                return emitted.artifact_path
        self.fail(f"Scenario not found: {scenario_id}")

    def read_json(self, path: Path) -> dict[str, Any]:
        parsed = json.loads(path.read_text(encoding="utf-8"))
        self.assertIsInstance(parsed, dict)
        return parsed

    def build_packet(self, temp_dir: Path, scenario_id: str) -> tuple[Path, dict[str, Any]]:
        artifact_path = self.emit_scenario(temp_dir / "artifacts", scenario_id)
        packet = builder.build_receiving_packet(artifact_path)
        return artifact_path, packet

    def assert_top_level_packet_shape(self, packet: dict[str, Any]) -> None:
        self.assertIsInstance(packet, dict)
        self.assertEqual(set(packet), EXPECTED_PACKET_KEYS)

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def refusal_records(self, packet: dict[str, Any]) -> list[dict[str, Any]]:
        return [
            record
            for record in packet["imported_packet"]["transition_records"]
            if not record["accepted"]
        ]

    def test_real_packet_build_from_source_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            self.assert_top_level_packet_shape(packet)
            self.assertIsInstance(packet["packet_metadata"], dict)
            self.assertIsInstance(packet["source_provenance"], dict)
            self.assertIsInstance(packet["import_identity"], dict)
            self.assertIsInstance(packet["receiving_status"], dict)
            self.assertIsInstance(packet["import_summary"], dict)
            self.assertIsInstance(packet["imported_packet"], dict)

    def test_packet_metadata_source_provenance_and_import_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            metadata = packet["packet_metadata"]
            self.assertEqual(metadata["packet_type"], builder.PACKET_TYPE)
            self.assertEqual(metadata["packet_version"], builder.PACKET_VERSION)
            self.assert_non_empty_string(metadata["generated_at"])
            self.assertEqual(metadata["builder_module"], builder.__name__)

            provenance = packet["source_provenance"]
            self.assertEqual(
                Path(provenance["source_artifact_path"]).resolve(),
                artifact_path.resolve(),
            )
            self.assertEqual(
                Path(provenance["source_run_directory_path"]).resolve(),
                artifact_path.parent.resolve(),
            )
            self.assertEqual(
                provenance["scenario_id"],
                "lawful_distinct_matter_coexistence",
            )
            self.assertEqual(
                provenance["scenario_name"],
                "Lawful Distinct-Matter Coexistence",
            )
            self.assert_non_empty_string(provenance["scenario_description"])
            self.assert_non_empty_string(provenance["source_generated_at"])

            identity = packet["import_identity"]
            self.assertEqual(identity["imported_scenario_id"], provenance["scenario_id"])
            self.assertEqual(
                identity["imported_scenario_name"],
                provenance["scenario_name"],
            )
            self.assertEqual(
                Path(identity["import_source_path"]).resolve(),
                artifact_path.resolve(),
            )
            self.assertEqual(
                identity["snapshot_type"],
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT",
            )
            self.assertEqual(identity["snapshot_version"], "0.1.0")
            self.assertEqual(
                identity["source_host_class"],
                "IntegrityHostV0MinCoexistenceV2",
            )
            self.assertEqual(
                identity["source_module"],
                "integrity_host_v0_min_coexistence_v2",
            )

    def test_receiving_status_flags_preserve_non_continuity_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            self.assertEqual(packet["receiving_status"], EXPECTED_RECEIVING_STATUS)

    def test_import_summary_aligns_with_imported_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet(
                Path(temp_dir),
                "hold_blocks_one_target_while_another_proceeds",
            )

            summary = packet["import_summary"]
            imported_packet = packet["imported_packet"]
            scenario = imported_packet["scenario_metadata"]
            host = imported_packet["host_state"]
            records = imported_packet["transition_records"]

            self.assertEqual(summary["scenario_id"], scenario["scenario_id"])
            self.assertEqual(summary["scenario_name"], scenario["scenario_name"])
            self.assertEqual(Path(summary["source_path"]).resolve(), artifact_path.resolve())
            self.assertEqual(summary["snapshot_type"], "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT")
            self.assertEqual(summary["snapshot_version"], "0.1.0")
            self.assertEqual(summary["host_id"], host["host_id"])
            self.assertEqual(summary["object_count"], len(imported_packet["objects"]))
            self.assertEqual(summary["open_object_count"], len(host["open_object_ids"]))
            self.assertEqual(
                summary["coexistence_relation_count"],
                len(imported_packet["coexistence_relations"]),
            )
            self.assertEqual(summary["hold_count"], len(imported_packet["holds"]))
            self.assertEqual(summary["record_count"], len(records))
            self.assertEqual(
                summary["refusal_count"],
                sum(1 for record in records if not record["accepted"]),
            )
            self.assertEqual(
                summary["accepted_action_count"],
                sum(1 for action in scenario["action_results"] if action["accepted"]),
            )
            self.assertEqual(
                summary["refused_action_count"],
                sum(1 for action in scenario["action_results"] if not action["accepted"]),
            )

    def test_imported_packet_preserves_structural_sections(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            imported_packet = packet["imported_packet"]

            self.assertEqual(
                set(imported_packet),
                {
                    "scenario_metadata",
                    "snapshot_metadata",
                    "host_state",
                    "objects",
                    "coexistence_relations",
                    "holds",
                    "transition_records",
                },
            )

            scenario_metadata = imported_packet["scenario_metadata"]
            for key in (
                "scenario_id",
                "scenario_name",
                "description",
                "generated_at",
                "source_path",
                "accepted_action_count",
                "refused_action_count",
                "action_results",
            ):
                self.assertIn(key, scenario_metadata)
            self.assertGreater(len(scenario_metadata["action_results"]), 0)

            snapshot_metadata = imported_packet["snapshot_metadata"]
            for key in (
                "snapshot_type",
                "snapshot_version",
                "generated_at",
                "source_host_class",
                "source_module",
            ):
                self.assert_non_empty_string(snapshot_metadata[key])

            host_state = imported_packet["host_state"]
            self.assert_non_empty_string(host_state["host_id"])
            self.assertIsInstance(host_state["open_object_ids"], list)

            object_keys = {
                "object_id",
                "matter_ref",
                "payload_ref",
                "phase_state",
                "resolution_type",
                "predecessor_object_id",
                "occurrence_ref",
                "created_by_record_id",
                "resolved_by_record_id",
            }
            for obj in imported_packet["objects"]:
                self.assertEqual(set(obj), object_keys)
                self.assert_non_empty_string(obj["object_id"])
                self.assert_non_empty_string(obj["matter_ref"])
                self.assert_non_empty_string(obj["payload_ref"])

            record_keys = {
                "record_id",
                "host_id",
                "action_type",
                "matter_ref",
                "object_id",
                "related_open_object_ids",
                "created_coexistence_relations",
                "predecessor_object_id",
                "successor_object_id",
                "source_phase_state",
                "target_phase_state",
                "source_resolution_type",
                "target_resolution_type",
                "payload_ref",
                "occurrence_ref",
                "basis_ref",
                "threshold_basis_ref",
                "hold_before",
                "hold_after",
                "accepted",
                "refusal_code",
                "acted_at",
            }
            for record in imported_packet["transition_records"]:
                self.assertEqual(set(record), record_keys)
                self.assert_non_empty_string(record["record_id"])
                self.assert_non_empty_string(record["host_id"])
                self.assert_non_empty_string(record["action_type"])
                self.assertIsInstance(record["accepted"], bool)
                self.assertIsInstance(record["created_coexistence_relations"], list)

    def test_object_relation_hold_refusal_and_lineage_visibility(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packets = {
                scenario_id: builder.build_receiving_packet(path)
                for scenario_id, path in self.emit_all_scenarios(
                    Path(temp_dir) / "artifacts"
                ).items()
            }

            lawful = packets["lawful_distinct_matter_coexistence"]["imported_packet"]
            self.assertEqual(len(lawful["objects"]), 2)
            self.assertEqual(len(lawful["coexistence_relations"]), 1)
            relation = lawful["coexistence_relations"][0]
            self.assertEqual(relation["relation_type"], "DISTINCT_MATTER_COHOSTED")
            self.assertEqual(relation["basis_ref"], "cohost-a-b")
            self.assert_non_empty_string(relation["object_id"])
            self.assert_non_empty_string(relation["related_object_id"])

            hold_packet = packets[
                "hold_blocks_one_target_while_another_proceeds"
            ]["imported_packet"]
            self.assertEqual(len(hold_packet["holds"]), 1)
            hold = hold_packet["holds"][0]
            self.assertTrue(hold["active"])
            self.assertEqual(hold["basis_ref"], "hold-a")
            self.assert_non_empty_string(hold["target_object_id"])
            self.assert_non_empty_string(hold["set_by_record_id"])
            self.assertNotIn("HOLD", {obj["phase_state"] for obj in hold_packet["objects"]})
            self.assertNotIn(
                "HOLD",
                {
                    obj["resolution_type"]
                    for obj in hold_packet["objects"]
                    if obj["resolution_type"] is not None
                },
            )

            missing_basis = packets["refused_missing_coexistence_basis"]
            missing_refusals = self.refusal_records(missing_basis)
            self.assertEqual(len(missing_refusals), 1)
            self.assertEqual(
                missing_refusals[0]["refusal_code"],
                "UNRESOLVED_COHOST_RELATION_REQUIRED",
            )
            self.assertEqual(
                len(missing_basis["imported_packet"]["objects"]),
                1,
            )

            same_matter = packets["same_matter_post_resolution_refusal"]
            same_matter_refusals = self.refusal_records(same_matter)
            self.assertEqual(len(same_matter_refusals), 1)
            self.assertEqual(
                same_matter_refusals[0]["refusal_code"],
                "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
            )
            self.assertEqual(
                len(same_matter["imported_packet"]["objects"]),
                1,
            )

            evolve = packets["evolve_under_coexistence"]["imported_packet"]
            predecessor = next(
                obj for obj in evolve["objects"] if obj["resolution_type"] == "EVOLVE"
            )
            successor = next(
                obj
                for obj in evolve["objects"]
                if obj["predecessor_object_id"] == predecessor["object_id"]
            )
            evolve_record = next(
                record
                for record in evolve["transition_records"]
                if record["action_type"] == "EVOLVE"
            )
            self.assertEqual(predecessor["phase_state"], "STANDING")
            self.assertEqual(successor["phase_state"], "CANDIDATE")
            self.assertEqual(evolve_record["predecessor_object_id"], predecessor["object_id"])
            self.assertEqual(evolve_record["successor_object_id"], successor["object_id"])
            self.assertEqual(evolve_record["target_resolution_type"], "EVOLVE")

    def test_packet_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet(
                Path(temp_dir),
                "hold_blocks_one_target_while_another_proceeds",
            )

            summary = builder.build_receiving_packet_summary(packet)

            self.assertEqual(
                set(summary),
                {
                    "scenario_id",
                    "scenario_name",
                    "source_artifact_path",
                    "host_id",
                    "object_count",
                    "open_object_count",
                    "coexistence_relation_count",
                    "hold_count",
                    "transition_record_count",
                    "refusal_count",
                    "accepted_action_count",
                    "refused_action_count",
                    "receiving_status",
                },
            )
            self.assertEqual(
                Path(summary["source_artifact_path"]).resolve(),
                artifact_path.resolve(),
            )
            self.assertEqual(summary["scenario_id"], packet["import_summary"]["scenario_id"])
            self.assertEqual(summary["scenario_name"], packet["import_summary"]["scenario_name"])
            self.assertEqual(summary["host_id"], packet["import_summary"]["host_id"])
            self.assertEqual(summary["object_count"], packet["import_summary"]["object_count"])
            self.assertEqual(
                summary["open_object_count"],
                packet["import_summary"]["open_object_count"],
            )
            self.assertEqual(
                summary["coexistence_relation_count"],
                packet["import_summary"]["coexistence_relation_count"],
            )
            self.assertEqual(summary["hold_count"], packet["import_summary"]["hold_count"])
            self.assertEqual(
                summary["transition_record_count"],
                packet["import_summary"]["record_count"],
            )
            self.assertEqual(
                summary["refusal_count"],
                packet["import_summary"]["refusal_count"],
            )
            self.assertEqual(
                summary["accepted_action_count"],
                packet["import_summary"]["accepted_action_count"],
            )
            self.assertEqual(
                summary["refused_action_count"],
                packet["import_summary"]["refused_action_count"],
            )
            self.assertEqual(summary["receiving_status"], EXPECTED_RECEIVING_STATUS)

    def test_write_receiving_packet_explicit_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path = self.emit_scenario(
                temp_root / "source",
                "lawful_distinct_matter_coexistence",
            )
            output_path = temp_root / "packets" / "nested" / "packet.json"

            written = builder.write_receiving_packet(artifact_path, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assert_top_level_packet_shape(parsed)
            self.assertEqual(
                Path(parsed["source_provenance"]["source_artifact_path"]).resolve(),
                artifact_path.resolve(),
            )
            with self.assertRaises(RuntimeError):
                builder.write_receiving_packet(artifact_path, output_path)

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path = self.emit_scenario(
                temp_root / "source",
                "lawful_distinct_matter_coexistence",
            )

            with mock.patch.object(builder, "_repo_root", return_value=temp_root):
                written = builder.write_receiving_packet(artifact_path)
                expected = (
                    temp_root
                    / builder.OUTPUT_ROOT
                    / f"{artifact_path.stem}__receiving_packet.json"
                )
                self.assertEqual(written, expected)
                self.assertTrue(written.exists())
                self.assert_top_level_packet_shape(self.read_json(written))

                with self.assertRaises(RuntimeError):
                    builder.write_receiving_packet(artifact_path)

    def test_validation_error_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            missing_path = temp_root / "missing.json"
            directory_path = temp_root / "directory"
            directory_path.mkdir()
            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text('{"scenario": {}}\n', encoding="utf-8")

            with self.assertRaises(RuntimeError):
                builder.build_receiving_packet(missing_path)
            with self.assertRaises(RuntimeError):
                builder.build_receiving_packet(directory_path)
            with self.assertRaises(RuntimeError):
                builder.build_receiving_packet(malformed_path)
            with self.assertRaises(RuntimeError):
                builder.build_receiving_packet_summary({"source_provenance": {}})

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path = self.emit_scenario(
                temp_root / "source",
                "same_matter_post_resolution_refusal",
            )
            output_path = temp_root / "receiving" / "packet.json"
            before_text = artifact_path.read_text(encoding="utf-8")

            first_packet = builder.build_receiving_packet(artifact_path)
            after_first_build = artifact_path.read_text(encoding="utf-8")
            written = builder.write_receiving_packet(artifact_path, output_path)
            after_write = artifact_path.read_text(encoding="utf-8")
            second_packet = builder.build_receiving_packet(artifact_path)
            after_second_build = artifact_path.read_text(encoding="utf-8")

            self.assertEqual(after_first_build, before_text)
            self.assertEqual(after_write, before_text)
            self.assertEqual(after_second_build, before_text)
            self.assertEqual(written, output_path)
            self.assertEqual(
                first_packet["source_provenance"],
                second_packet["source_provenance"],
            )
            self.assertEqual(first_packet["import_identity"], second_packet["import_identity"])
            self.assertEqual(first_packet["receiving_status"], second_packet["receiving_status"])
            self.assertEqual(first_packet["import_summary"], second_packet["import_summary"])
            self.assertEqual(first_packet["imported_packet"], second_packet["imported_packet"])


if __name__ == "__main__":
    unittest.main()
