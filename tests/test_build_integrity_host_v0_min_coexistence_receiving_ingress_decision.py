"""Bounded tests for the v0-min coexistence receiving-ingress decision builder.

These tests lock the current additive decision surface in
``src/build_integrity_host_v0_min_coexistence_receiving_ingress_decision.py``
using real scenario artifacts and receiving packets from the current local
runner and packet builder.

They verify decision shape, source provenance, packet identity, validation
carry-through, receive/reject decision logic, status carry-forward, JSON
writing, default output behavior, preserved packet detail, hard error posture,
and non-mutation. They do not test replay, merge, persistence architecture,
registry behavior, distributed continuity, CLI behavior, broad policy engines,
or speculative successor features.
"""

from __future__ import annotations

import copy
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

import build_integrity_host_v0_min_coexistence_receiving_ingress_decision as decision_builder  # noqa: E402
import build_integrity_host_v0_min_coexistence_receiving_packet as packet_builder  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


EXPECTED_DECISION_KEYS = {
    "decision_metadata",
    "source_provenance",
    "packet_identity",
    "validation_summary",
    "validation_result",
    "ingress_decision",
    "receiving_status_carry_forward",
    "receiving_packet",
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


class IntegrityHostV0MinCoexistenceReceivingIngressDecisionTests(unittest.TestCase):
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

    def build_packet(
        self,
        temp_root: Path,
        scenario_id: str,
    ) -> tuple[Path, dict[str, Any]]:
        artifact_path = self.emit_scenario(temp_root / "source", scenario_id)
        packet = packet_builder.build_receiving_packet(artifact_path)
        return artifact_path, packet

    def write_packet(
        self,
        temp_root: Path,
        scenario_id: str,
        file_name: str = "packet.json",
    ) -> tuple[Path, Path, dict[str, Any]]:
        artifact_path = self.emit_scenario(temp_root / "source", scenario_id)
        packet_path = temp_root / "packets" / file_name
        written_path = packet_builder.write_receiving_packet(artifact_path, packet_path)
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

    def assert_decision_shape(self, decision: dict[str, Any]) -> None:
        self.assertEqual(set(decision), EXPECTED_DECISION_KEYS)
        self.assertIsInstance(decision["decision_metadata"], dict)
        self.assertIsInstance(decision["source_provenance"], dict)
        self.assertIsInstance(decision["packet_identity"], dict)
        self.assertIsInstance(decision["validation_summary"], dict)
        self.assertIsInstance(decision["validation_result"], dict)
        self.assertIsInstance(decision["ingress_decision"], dict)
        self.assertIsInstance(decision["receiving_status_carry_forward"], dict)
        self.assertIsInstance(decision["receiving_packet"], dict)

    def test_real_decision_build_from_packet_dict(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            decision = decision_builder.build_ingress_decision(packet)

        self.assert_decision_shape(decision)
        self.assertEqual(
            decision["source_provenance"]["scenario_id"],
            "lawful_distinct_matter_coexistence",
        )
        self.assertIsNone(decision["packet_identity"]["receiving_packet_path"])

    def test_real_decision_build_from_packet_path(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet_path, _ = self.write_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )

            decision = decision_builder.build_ingress_decision_from_packet_path(
                packet_path
            )

        self.assert_decision_shape(decision)
        self.assertEqual(
            Path(decision["packet_identity"]["receiving_packet_path"]).resolve(),
            packet_path.resolve(),
        )

    def test_real_decision_build_from_source_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = self.emit_scenario(
                Path(temp_dir) / "source",
                "lawful_distinct_matter_coexistence",
            )

            decision = decision_builder.build_ingress_decision_from_source_artifact(
                artifact_path
            )

        self.assert_decision_shape(decision)
        self.assertEqual(
            Path(decision["source_provenance"]["source_artifact_path"]).resolve(),
            artifact_path.resolve(),
        )
        self.assertEqual(
            decision["ingress_decision"]["decision"],
            decision_builder.DECISION_RECEIVE,
        )
        self.assertFalse(decision["ingress_decision"]["requires_replay"])
        self.assertFalse(decision["ingress_decision"]["requires_merge"])

    def test_decision_metadata_source_provenance_and_packet_identity(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision(packet)

        metadata = decision["decision_metadata"]
        self.assertEqual(metadata["decision_type"], decision_builder.DECISION_TYPE)
        self.assertEqual(metadata["decision_version"], decision_builder.DECISION_VERSION)
        self.assert_non_empty_string(metadata["generated_at"])
        self.assertEqual(metadata["decision_builder_module"], decision_builder.__name__)

        source = decision["source_provenance"]
        self.assertEqual(
            Path(source["source_artifact_path"]).resolve(),
            artifact_path.resolve(),
        )
        self.assertEqual(
            Path(source["source_run_directory_path"]).resolve(),
            artifact_path.parent.resolve(),
        )
        self.assertEqual(source["scenario_id"], "lawful_distinct_matter_coexistence")
        self.assertEqual(source["scenario_name"], "Lawful Distinct-Matter Coexistence")
        self.assert_non_empty_string(source["scenario_description"])
        self.assert_non_empty_string(source["source_generated_at"])

        identity = decision["packet_identity"]
        self.assertEqual(identity["scenario_id"], source["scenario_id"])
        self.assertEqual(identity["scenario_name"], source["scenario_name"])
        self.assert_non_empty_string(identity["host_id"])
        self.assertEqual(
            identity["snapshot_type"],
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT",
        )
        self.assertEqual(identity["snapshot_version"], "0.1.0")
        self.assertEqual(identity["packet_type"], packet_builder.PACKET_TYPE)
        self.assertEqual(identity["packet_version"], packet_builder.PACKET_VERSION)
        self.assertEqual(identity["expected_packet_type"], packet_builder.PACKET_TYPE)
        self.assertEqual(identity["expected_packet_version"], packet_builder.PACKET_VERSION)

    def test_validation_summary_carry_through(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "hold_blocks_one_target_while_another_proceeds",
            )
            decision = decision_builder.build_ingress_decision(packet)

        summary = decision["validation_summary"]
        for key in (
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
        ):
            self.assertIn(key, summary)

        self.assertEqual(summary["scenario_id"], "hold_blocks_one_target_while_another_proceeds")
        self.assertGreater(summary["total_check_count"], 0)
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["all_passed"])
        self.assertGreater(summary["hold_count"], 0)
        self.assertGreater(summary["refusal_count"], 0)
        self.assertEqual(summary["receiving_status"], EXPECTED_RECEIVING_STATUS)

    def test_ingress_decision_logic_on_valid_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision(packet)

        ingress = decision["ingress_decision"]
        self.assertEqual(ingress["decision"], decision_builder.DECISION_RECEIVE)
        self.assert_non_empty_string(ingress["decision_reason"])
        self.assertTrue(ingress["validation_passed"])
        self.assertTrue(ingress["eligible_for_bounded_receiving_handling"])
        self.assertFalse(ingress["requires_replay"])
        self.assertFalse(ingress["requires_merge"])
        self.assertFalse(ingress["continuity_completed"])
        self.assertFalse(ingress["standing_upgraded"])

    def test_ingress_decision_logic_on_failed_but_readable_packet(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, _, packet = self.write_packet(
                temp_root,
                "lawful_distinct_matter_coexistence",
            )
            mismatched = copy.deepcopy(packet)
            mismatched["import_summary"]["object_count"] += 1
            mismatched_path = self.write_json(
                temp_root / "packets" / "mismatched.json",
                mismatched,
            )

            decision = decision_builder.build_ingress_decision_from_packet_path(
                mismatched_path
            )

        self.assert_decision_shape(decision)
        self.assertFalse(decision["validation_summary"]["all_passed"])
        self.assertGreater(decision["validation_summary"]["failed_check_count"], 0)
        ingress = decision["ingress_decision"]
        self.assertEqual(ingress["decision"], decision_builder.DECISION_REJECT)
        self.assertFalse(ingress["validation_passed"])
        self.assertFalse(ingress["eligible_for_bounded_receiving_handling"])
        self.assertFalse(ingress["continuity_completed"])
        self.assertFalse(ingress["standing_upgraded"])

    def test_hard_malformed_packet_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            missing_packet_path = temp_root / "missing-packet.json"
            malformed_packet_path = temp_root / "malformed-packet.json"
            malformed_packet_path.write_text("{not json}\n", encoding="utf-8")
            missing_source_path = temp_root / "missing-source.json"

            with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                decision_builder.build_ingress_decision(["not", "mapping"])  # type: ignore[arg-type]
            with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                decision_builder.build_ingress_decision_from_packet_path(
                    missing_packet_path
                )
            with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                decision_builder.build_ingress_decision_from_packet_path(
                    malformed_packet_path
                )
            with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                decision_builder.build_ingress_decision_from_source_artifact(
                    missing_source_path
                )

    def test_receiving_status_carry_forward(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet = self.build_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision(packet)

        self.assertEqual(
            decision["receiving_status_carry_forward"],
            EXPECTED_RECEIVING_STATUS,
        )
        self.assertTrue(decision["receiving_status_carry_forward"]["source_remains_source"])
        self.assertFalse(
            decision["receiving_status_carry_forward"]["replayed_into_live_host"]
        )
        self.assertFalse(
            decision["receiving_status_carry_forward"]["merged_into_local_state"]
        )
        self.assertFalse(
            decision["receiving_status_carry_forward"]["continuity_completed"]
        )
        self.assertFalse(decision["receiving_status_carry_forward"]["standing_upgraded"])

    def test_decision_summary_helper(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            _, packet_path, _ = self.write_packet(
                Path(temp_dir),
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision_from_packet_path(
                packet_path
            )
            summary = decision_builder.build_ingress_decision_summary(decision)

        self.assertEqual(summary["scenario_id"], decision["source_provenance"]["scenario_id"])
        self.assertEqual(summary["scenario_name"], decision["source_provenance"]["scenario_name"])
        self.assertEqual(
            summary["source_artifact_path"],
            decision["source_provenance"]["source_artifact_path"],
        )
        self.assertEqual(
            Path(summary["receiving_packet_path"]).resolve(),
            packet_path.resolve(),
        )
        self.assertEqual(summary["host_id"], decision["packet_identity"]["host_id"])
        self.assertEqual(summary["decision"], decision_builder.DECISION_RECEIVE)
        self.assert_non_empty_string(summary["decision_reason"])
        self.assertTrue(summary["validation_passed"])
        self.assertTrue(summary["eligible_for_bounded_receiving_handling"])
        self.assertEqual(summary["failed_check_count"], 0)
        self.assertTrue(summary["all_passed"])
        for key in (
            "object_count",
            "open_object_count",
            "coexistence_relation_count",
            "hold_count",
            "transition_record_count",
            "refusal_count",
            "accepted_action_count",
            "refused_action_count",
        ):
            self.assertIsInstance(summary[key], int)
        self.assertEqual(summary["receiving_status"], EXPECTED_RECEIVING_STATUS)

    def test_write_ingress_decision_explicit_output(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, packet = self.build_packet(
                temp_root,
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision(packet)
            output_path = temp_root / "decisions" / "nested" / "decision.json"

            written = decision_builder.write_ingress_decision(decision, output_path)

            self.assertEqual(written, output_path)
            self.assertTrue(written.exists())
            parsed = self.read_json(written)
            self.assertEqual(set(parsed), EXPECTED_DECISION_KEYS)
            with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                decision_builder.write_ingress_decision(decision, output_path)

    def test_default_output_path_behavior(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            _, packet_path, _ = self.write_packet(
                temp_root,
                "lawful_distinct_matter_coexistence",
            )
            decision = decision_builder.build_ingress_decision_from_packet_path(
                packet_path
            )

            with mock.patch.object(decision_builder, "_repo_root", return_value=temp_root):
                written = decision_builder.write_ingress_decision(decision)
                expected = (
                    temp_root
                    / decision_builder.OUTPUT_ROOT
                    / f"{packet_path.stem}__receiving_ingress_decision.json"
                )

                self.assertEqual(written, expected)
                self.assertTrue(written.exists())
                self.assertEqual(set(self.read_json(written)), EXPECTED_DECISION_KEYS)
                with self.assertRaises(decision_builder.ReceivingIngressDecisionError):
                    decision_builder.write_ingress_decision(decision)

    def test_decision_preserves_packet_refusal_hold_coexistence_and_lineage(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            packets = {
                scenario_id: packet_builder.build_receiving_packet(path)
                for scenario_id, path in self.emit_all_scenarios(
                    Path(temp_dir) / "source"
                ).items()
            }
            decisions = {
                scenario_id: decision_builder.build_ingress_decision(packet)
                for scenario_id, packet in packets.items()
            }

        lawful_packet = decisions[
            "lawful_distinct_matter_coexistence"
        ]["receiving_packet"]["imported_packet"]
        self.assertGreater(len(lawful_packet["coexistence_relations"]), 0)

        hold_packet = decisions[
            "hold_blocks_one_target_while_another_proceeds"
        ]["receiving_packet"]["imported_packet"]
        self.assertGreater(len(hold_packet["holds"]), 0)
        self.assertGreater(
            len(
                [
                    record
                    for record in hold_packet["transition_records"]
                    if record["refusal_code"] is not None
                ]
            ),
            0,
        )

        same_matter_packet = decisions[
            "same_matter_post_resolution_refusal"
        ]["receiving_packet"]["imported_packet"]
        self.assertIn(
            "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
            {
                record["refusal_code"]
                for record in same_matter_packet["transition_records"]
                if record["refusal_code"] is not None
            },
        )

        evolve_packet = decisions["evolve_under_coexistence"]["receiving_packet"][
            "imported_packet"
        ]
        self.assertGreater(
            len(
                [
                    obj
                    for obj in evolve_packet["objects"]
                    if obj["predecessor_object_id"] is not None
                ]
            ),
            0,
        )
        self.assertGreater(
            len(
                [
                    record
                    for record in evolve_packet["transition_records"]
                    if record["action_type"] == "EVOLVE"
                    and record["predecessor_object_id"] is not None
                    and record["successor_object_id"] is not None
                ]
            ),
            0,
        )

    def test_non_mutation_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_root = Path(temp_dir)
            artifact_path, packet_path, packet = self.write_packet(
                temp_root,
                "same_matter_post_resolution_refusal",
            )
            source_before = artifact_path.read_text(encoding="utf-8")
            packet_before_text = packet_path.read_text(encoding="utf-8")
            packet_before = copy.deepcopy(packet)

            first_decision = decision_builder.build_ingress_decision_from_packet_path(
                packet_path
            )
            after_first_packet_text = packet_path.read_text(encoding="utf-8")
            dict_decision = decision_builder.build_ingress_decision(packet)
            after_dict_packet_text = packet_path.read_text(encoding="utf-8")
            second_decision = decision_builder.build_ingress_decision_from_packet_path(
                packet_path
            )
            after_second_packet_text = packet_path.read_text(encoding="utf-8")

            decision_before_write = copy.deepcopy(first_decision)
            output_path = temp_root / "decisions" / "decision.json"
            decision_builder.write_ingress_decision(first_decision, output_path)

            self.assertEqual(artifact_path.read_text(encoding="utf-8"), source_before)
            self.assertEqual(after_first_packet_text, packet_before_text)
            self.assertEqual(after_dict_packet_text, packet_before_text)
            self.assertEqual(after_second_packet_text, packet_before_text)
            self.assertEqual(packet_path.read_text(encoding="utf-8"), packet_before_text)
            self.assertEqual(packet, packet_before)
            self.assertEqual(first_decision, decision_before_write)
            self.assertEqual(
                first_decision["source_provenance"],
                second_decision["source_provenance"],
            )
            self.assertEqual(
                first_decision["packet_identity"],
                second_decision["packet_identity"],
            )
            self.assertEqual(
                first_decision["ingress_decision"],
                dict_decision["ingress_decision"],
            )


if __name__ == "__main__":
    unittest.main()
