"""Bounded tests for the v0-min coexistence receiving-packet validator.

These tests lock the current validation surface in
``src/validate_integrity_host_v0_min_coexistence_receiving_packet.py`` using
real scenario artifacts and receiving packets from the current local runner and
builder.

They verify packet reading, validation-result shape, structural checks,
receiving-status posture, count coherence, visibility checks, readable failed
validation, hard malformed-packet failures, and non-mutation. They do not test
replay, merge, persistence architecture, registry behavior, distributed
continuity, CLI behavior, or speculative successor features.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import build_integrity_host_v0_min_coexistence_receiving_packet as builder  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402
import validate_integrity_host_v0_min_coexistence_receiving_packet as validator  # noqa: E402


EXPECTED_RESULT_KEYS = {
    "validation_metadata",
    "packet_identity",
    "structural_checks",
    "status_checks",
    "count_checks",
    "visibility_checks",
    "all_passed",
}

EXPECTED_STRUCTURAL_CHECKS = {
    "packet_metadata",
    "source_provenance",
    "import_identity",
    "receiving_status",
    "import_summary",
    "imported_packet",
    "imported_scenario_metadata",
    "imported_snapshot_metadata",
    "imported_host_state",
    "imported_objects",
    "imported_coexistence_relations",
    "imported_holds",
    "imported_transition_records",
}

EXPECTED_COUNT_CHECKS = {
    "object_count",
    "open_object_count",
    "coexistence_relation_count",
    "hold_count",
    "transition_record_count",
    "refusal_count",
    "accepted_action_count",
    "refused_action_count",
    "resolved_object_count",
    "successor_object_count",
    "evolve_record_count",
}

EXPECTED_VISIBILITY_CHECKS = {
    "object_ids_visible",
    "coexistence_relations_visible",
    "holds_visible",
    "refusal_records_visible",
    "predecessor_successor_lineage_visible",
}


class IntegrityHostV0MinCoexistenceReceivingPacketValidationTests(unittest.TestCase):
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

    def emit_all_scenarios(self, output_dir: Path) -> dict[str, Path]:
        output_dir.mkdir(parents=True, exist_ok=True)
        emitted_paths: dict[str, Path] = {}
        for file_stem, scenario_function in runner.SCENARIOS:
            emitted = runner._emit_scenario(output_dir, file_stem, scenario_function)
            emitted_paths[emitted.scenario_id] = emitted.artifact_path
        return emitted_paths

    def build_packet_dict(
        self,
        temp_root: Path,
        scenario_id: str,
    ) -> tuple[Path, dict[str, Any]]:
        artifact_path = self.emit_scenario(temp_root / "source", scenario_id)
        return artifact_path, builder.build_receiving_packet(artifact_path)

    def write_packet(
        self,
        temp_root: Path,
        scenario_id: str,
        file_name: str = "packet.json",
    ) -> tuple[Path, Path, dict[str, Any]]:
        artifact_path = self.emit_scenario(temp_root / "source", scenario_id)
        output_path = temp_root / "packets" / file_name
        written_path = builder.write_receiving_packet(artifact_path, output_path)
        packet = self.read_json(written_path)
        return artifact_path, written_path, packet

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

    def assert_non_empty_string(self, value: Any) -> None:
        self.assertIsInstance(value, str)
        self.assertTrue(value)

    def assert_validation_result_shape(self, result: dict[str, Any]) -> None:
        self.assertEqual(set(result), EXPECTED_RESULT_KEYS)
        self.assertIsInstance(result["validation_metadata"], dict)
        self.assertIsInstance(result["packet_identity"], dict)
        self.assertIsInstance(result["structural_checks"], dict)
        self.assertIsInstance(result["status_checks"], dict)
        self.assertIsInstance(result["count_checks"], dict)
        self.assertIsInstance(result["visibility_checks"], dict)
        self.assertIsInstance(result["all_passed"], bool)

    def assert_all_checks_pass(self, result: dict[str, Any]) -> None:
        self.assertTrue(result["all_passed"])
        self.assertTrue(all(result["structural_checks"].values()))
        for section_name in ("status_checks", "count_checks", "visibility_checks"):
            for check in result[section_name].values():
                self.assertIsInstance(check, dict)
                self.assertTrue(check["matched"])

    def test_real_packet_path_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet_path, _ = self.write_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            result = validator.validate_receiving_packet_path(packet_path)

        self.assert_validation_result_shape(result)
        self.assert_all_checks_pass(result)

    def test_packet_json_read_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, packet_path, _ = self.write_packet(
                temp_root,
                "lawful_distinct_matter_coexistence",
            )
            missing_path = temp_root / "missing.json"
            directory_path = temp_root / "directory"
            directory_path.mkdir()
            malformed_path = temp_root / "malformed.json"
            malformed_path.write_text("{not json}\n", encoding="utf-8")
            non_object_path = temp_root / "list.json"
            non_object_path.write_text("[1, 2, 3]\n", encoding="utf-8")

            parsed = validator.read_receiving_packet_json(packet_path)

            self.assertIsInstance(parsed, dict)
            self.assertIn("packet_metadata", parsed)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.read_receiving_packet_json(missing_path)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.read_receiving_packet_json(directory_path)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.read_receiving_packet_json(malformed_path)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.read_receiving_packet_json(non_object_path)

    def test_real_packet_dict_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet_dict(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            packet_path = Path(temp_dir) / "packets" / "packet.json"
            self.write_json(packet_path, packet)

            dict_result = validator.validate_receiving_packet(packet)
            path_result = validator.validate_receiving_packet_path(packet_path)

        self.assertEqual(set(dict_result), set(path_result))
        self.assertEqual(
            Path(dict_result["packet_identity"]["source_artifact_path"]).resolve(),
            artifact_path.resolve(),
        )
        self.assert_validation_result_shape(dict_result)
        self.assert_all_checks_pass(dict_result)

    def test_validation_metadata_and_packet_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet_dict(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            result = validator.validate_receiving_packet(packet)

        metadata = result["validation_metadata"]
        self.assertEqual(metadata["validation_type"], validator.VALIDATION_TYPE)
        self.assertEqual(metadata["validation_version"], validator.VALIDATION_VERSION)
        self.assert_non_empty_string(metadata["generated_at"])
        self.assertEqual(metadata["validator_module"], validator.__name__)

        identity = result["packet_identity"]
        provenance = packet["source_provenance"]
        import_identity = packet["import_identity"]
        summary = packet["import_summary"]

        self.assertEqual(identity["scenario_id"], provenance["scenario_id"])
        self.assertEqual(identity["scenario_name"], provenance["scenario_name"])
        self.assertEqual(
            Path(identity["source_artifact_path"]).resolve(),
            artifact_path.resolve(),
        )
        self.assertEqual(
            Path(identity["source_run_directory_path"]).resolve(),
            artifact_path.parent.resolve(),
        )
        self.assertEqual(import_identity["imported_scenario_id"], provenance["scenario_id"])
        self.assertEqual(
            import_identity["imported_scenario_name"],
            provenance["scenario_name"],
        )
        self.assertEqual(identity["host_id"], summary["host_id"])
        self.assert_non_empty_string(identity["host_id"])
        self.assertEqual(identity["snapshot_type"], import_identity["snapshot_type"])
        self.assertEqual(identity["snapshot_version"], import_identity["snapshot_version"])

    def test_structural_checks_pass_for_valid_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet_dict(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            result = validator.validate_receiving_packet(packet)

        structural = result["structural_checks"]
        for check_name in EXPECTED_STRUCTURAL_CHECKS:
            self.assertIn(check_name, structural)
            self.assertTrue(structural[check_name], check_name)
        self.assertTrue(all(structural.values()))

    def test_status_checks_preserve_expected_actual_and_match(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet_dict(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            result = validator.validate_receiving_packet(packet)

        status_checks = result["status_checks"]
        self.assertEqual(set(status_checks), set(validator.EXPECTED_RECEIVING_STATUS))
        for key, expected in validator.EXPECTED_RECEIVING_STATUS.items():
            check = status_checks[key]
            self.assertEqual(set(check), {"expected", "actual", "matched"})
            self.assertIs(check["expected"], expected)
            self.assertIs(check["actual"], expected)
            self.assertTrue(check["matched"])

    def test_count_checks_match_imported_packet_structure(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packets = {
                scenario_id: builder.build_receiving_packet(path)
                for scenario_id, path in self.emit_all_scenarios(
                    Path(temp_dir) / "source"
                ).items()
            }

            for scenario_id, packet in packets.items():
                with self.subTest(scenario_id=scenario_id):
                    result = validator.validate_receiving_packet(packet)
                    count_checks = result["count_checks"]
                    self.assertTrue(EXPECTED_COUNT_CHECKS.issubset(count_checks))
                    for check_name in EXPECTED_COUNT_CHECKS:
                        check = count_checks[check_name]
                        self.assertIn("expected", check)
                        self.assertIn("actual", check)
                        self.assertIn("matched", check)
                        self.assertIsInstance(check["actual"], int)
                        self.assertTrue(check["matched"], check_name)

            hold_counts = validator.validate_receiving_packet(
                packets["hold_blocks_one_target_while_another_proceeds"]
            )["count_checks"]
            self.assertGreater(hold_counts["hold_count"]["actual"], 0)
            self.assertGreater(hold_counts["refusal_count"]["actual"], 0)

            evolve_counts = validator.validate_receiving_packet(
                packets["evolve_under_coexistence"]
            )["count_checks"]
            self.assertGreater(evolve_counts["resolved_object_count"]["actual"], 0)
            self.assertGreater(evolve_counts["successor_object_count"]["actual"], 0)
            self.assertGreater(evolve_counts["evolve_record_count"]["actual"], 0)

    def test_visibility_checks_preserve_load_bearing_surfaces(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packets = {
                scenario_id: builder.build_receiving_packet(path)
                for scenario_id, path in self.emit_all_scenarios(
                    Path(temp_dir) / "source"
                ).items()
            }

            for scenario_id, packet in packets.items():
                with self.subTest(scenario_id=scenario_id):
                    result = validator.validate_receiving_packet(packet)
                    visibility = result["visibility_checks"]
                    self.assertEqual(set(visibility), EXPECTED_VISIBILITY_CHECKS)
                    self.assertTrue(visibility["object_ids_visible"]["matched"])
                    self.assertGreater(visibility["object_ids_visible"]["count"], 0)
                    for check in visibility.values():
                        self.assertTrue(check["matched"])

            lawful_visibility = validator.validate_receiving_packet(
                packets["lawful_distinct_matter_coexistence"]
            )["visibility_checks"]
            self.assertGreater(
                lawful_visibility["coexistence_relations_visible"]["count"],
                0,
            )

            hold_visibility = validator.validate_receiving_packet(
                packets["hold_blocks_one_target_while_another_proceeds"]
            )["visibility_checks"]
            self.assertGreater(hold_visibility["holds_visible"]["count"], 0)
            self.assertGreater(hold_visibility["refusal_records_visible"]["count"], 0)

            same_matter_visibility = validator.validate_receiving_packet(
                packets["same_matter_post_resolution_refusal"]
            )["visibility_checks"]
            self.assertGreater(
                same_matter_visibility["refusal_records_visible"]["count"],
                0,
            )

            evolve_visibility = validator.validate_receiving_packet(
                packets["evolve_under_coexistence"]
            )["visibility_checks"]["predecessor_successor_lineage_visible"]
            self.assertGreater(evolve_visibility["object_lineage_count"], 0)
            self.assertGreater(evolve_visibility["evolve_record_lineage_count"], 0)

    def test_validation_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet_dict(
                Path(temp_dir),
                "hold_blocks_one_target_while_another_proceeds",
            )
            result = validator.validate_receiving_packet(packet)
            summary = validator.build_validation_summary(result)

        self.assertEqual(
            set(summary),
            {
                "scenario_id",
                "scenario_name",
                "source_artifact_path",
                "host_id",
                "total_check_count",
                "failed_check_count",
                "all_passed",
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
        self.assertEqual(summary["scenario_id"], result["packet_identity"]["scenario_id"])
        self.assertEqual(summary["scenario_name"], result["packet_identity"]["scenario_name"])
        self.assertEqual(
            summary["source_artifact_path"],
            result["packet_identity"]["source_artifact_path"],
        )
        self.assertEqual(summary["host_id"], result["packet_identity"]["host_id"])
        self.assertGreater(summary["total_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["all_passed"])
        self.assertEqual(
            summary["object_count"],
            result["count_checks"]["object_count"]["actual"],
        )
        self.assertEqual(
            summary["open_object_count"],
            result["count_checks"]["open_object_count"]["actual"],
        )
        self.assertEqual(
            summary["coexistence_relation_count"],
            result["count_checks"]["coexistence_relation_count"]["actual"],
        )
        self.assertEqual(
            summary["hold_count"],
            result["count_checks"]["hold_count"]["actual"],
        )
        self.assertEqual(
            summary["transition_record_count"],
            result["count_checks"]["transition_record_count"]["actual"],
        )
        self.assertEqual(
            summary["refusal_count"],
            result["count_checks"]["refusal_count"]["actual"],
        )
        self.assertEqual(
            summary["accepted_action_count"],
            result["count_checks"]["accepted_action_count"]["actual"],
        )
        self.assertEqual(
            summary["refused_action_count"],
            result["count_checks"]["refused_action_count"]["actual"],
        )
        self.assertEqual(summary["receiving_status"], validator.EXPECTED_RECEIVING_STATUS)

    def test_structurally_readable_but_failing_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, _, packet = self.write_packet(
                temp_root,
                "hold_blocks_one_target_while_another_proceeds",
            )

            status_mismatch = copy.deepcopy(packet)
            status_mismatch["receiving_status"]["continuity_completed"] = True
            status_path = self.write_json(
                temp_root / "mismatches" / "status.json",
                status_mismatch,
            )

            count_mismatch = copy.deepcopy(packet)
            count_mismatch["import_summary"]["object_count"] += 1
            count_path = self.write_json(
                temp_root / "mismatches" / "count.json",
                count_mismatch,
            )

            status_result = validator.validate_receiving_packet_path(status_path)
            count_result = validator.validate_receiving_packet_path(count_path)

        self.assertFalse(status_result["all_passed"])
        self.assertFalse(status_result["status_checks"]["continuity_completed"]["matched"])
        status_summary = validator.build_validation_summary(status_result)
        self.assertGreater(status_summary["failed_check_count"], 0)

        self.assertFalse(count_result["all_passed"])
        self.assertFalse(count_result["count_checks"]["object_count"]["matched"])
        count_summary = validator.build_validation_summary(count_result)
        self.assertGreater(count_summary["failed_check_count"], 0)

    def test_hard_malformed_packet_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, _, packet = self.write_packet(
                temp_root,
                "lawful_distinct_matter_coexistence",
            )

            missing_section = copy.deepcopy(packet)
            missing_section.pop("imported_packet")
            missing_path = self.write_json(
                temp_root / "bad" / "missing-section.json",
                missing_section,
            )

            wrong_type = copy.deepcopy(packet)
            wrong_type["receiving_status"] = []
            wrong_type_path = self.write_json(
                temp_root / "bad" / "wrong-type.json",
                wrong_type,
            )

            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.validate_receiving_packet_path(missing_path)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.validate_receiving_packet_path(wrong_type_path)
            with self.assertRaises(validator.ReceivingPacketValidationError):
                validator.validate_receiving_packet(["not", "a", "mapping"])  # type: ignore[arg-type]

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, packet_path, packet = self.write_packet(
                temp_root,
                "same_matter_post_resolution_refusal",
            )
            before_text = packet_path.read_text(encoding="utf-8")
            packet_before = copy.deepcopy(packet)

            first_result = validator.validate_receiving_packet_path(packet_path)
            after_first_path_validation = packet_path.read_text(encoding="utf-8")
            dict_result = validator.validate_receiving_packet(packet)
            after_dict_validation = packet_path.read_text(encoding="utf-8")
            second_result = validator.validate_receiving_packet_path(packet_path)
            after_second_path_validation = packet_path.read_text(encoding="utf-8")

        self.assertEqual(after_first_path_validation, before_text)
        self.assertEqual(after_dict_validation, before_text)
        self.assertEqual(after_second_path_validation, before_text)
        self.assertEqual(packet, packet_before)
        self.assertEqual(
            first_result["packet_identity"],
            second_result["packet_identity"],
        )
        self.assertEqual(
            first_result["count_checks"],
            dict_result["count_checks"],
        )
        self.assertEqual(
            first_result["status_checks"],
            dict_result["status_checks"],
        )
        self.assertTrue(first_result["all_passed"])
        self.assertTrue(dict_result["all_passed"])


if __name__ == "__main__":
    unittest.main()
