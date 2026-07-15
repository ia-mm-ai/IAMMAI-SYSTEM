"""Bounded tests for the v0-min coexistence snapshot/export layer.

These tests lock the current inspection surface in
``src/integrity_host_v0_min_coexistence_snapshot.py`` against the current
coexistence host in ``src/integrity_host_v0_min_coexistence_v2.py``.

They verify JSON-friendly export of objects, relations, HOLD posture, lineage,
append-only records, and explicit refusal. They do not test replay, registry
integration, persistence architecture, distributed behavior, or final storage
law.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from enum import Enum
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from integrity_host_v0_min_coexistence_snapshot import (  # noqa: E402
    build_snapshot,
    snapshot_to_json,
    write_snapshot,
)
from integrity_host_v0_min_coexistence_v2 import (  # noqa: E402
    ActionType,
    IntegrityHostV0MinCoexistenceV2,
    PhaseState,
    RefusalCode,
    RelationType,
    ResolutionType,
)


class IntegrityHostV0MinCoexistenceSnapshotTests(unittest.TestCase):
    def make_host(self, host_id: str = "snapshot-test-host") -> IntegrityHostV0MinCoexistenceV2:
        return IntegrityHostV0MinCoexistenceV2(host_id)

    def create_object(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
        matter_ref: str = "matter-a",
        payload_ref: str = "payload-a",
    ) -> str:
        result = host.create_object(
            matter_ref,
            payload_ref,
            basis_ref=f"create-{matter_ref}",
        )
        self.assertTrue(result.accepted)
        self.assertIsNotNone(result.object_id)
        return result.object_id or ""

    def create_cohosted_pair(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
    ) -> tuple[str, str]:
        first_id = self.create_object(host, "matter-a", "payload-a")
        result = host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-matter-b",
            cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
        )
        self.assertTrue(result.accepted)
        self.assertIsNotNone(result.object_id)
        return first_id, result.object_id or ""

    def present_object(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
        object_id: str,
        occurrence_ref: str,
    ) -> None:
        result = host.present(object_id, occurrence_ref, f"present-{occurrence_ref}")
        self.assertTrue(result.accepted)

    def stand_object(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
        object_id: str,
        threshold_basis_ref: str,
    ) -> None:
        result = host.stand(object_id, threshold_basis_ref)
        self.assertTrue(result.accepted)

    def create_standing_object(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
        matter_ref: str = "matter-a",
        payload_ref: str = "payload-a",
    ) -> str:
        object_id = self.create_object(host, matter_ref, payload_ref)
        self.present_object(host, object_id, f"occurrence-{matter_ref}")
        self.stand_object(host, object_id, f"threshold-{matter_ref}")
        return object_id

    def snapshot_objects_by_id(self, snapshot: dict[str, Any]) -> dict[str, dict[str, Any]]:
        return {obj["object_id"]: obj for obj in snapshot["objects"]}

    def assert_no_enums(self, value: Any) -> None:
        if isinstance(value, Enum):
            self.fail(f"raw enum leaked into snapshot: {value!r}")
        if isinstance(value, dict):
            for item in value.values():
                self.assert_no_enums(item)
        elif isinstance(value, list):
            for item in value:
                self.assert_no_enums(item)

    def test_build_snapshot_on_empty_host(self) -> None:
        host = self.make_host()

        snapshot = build_snapshot(host)

        self.assertIsInstance(snapshot, dict)
        self.assertEqual(
            set(snapshot),
            {
                "metadata",
                "host",
                "objects",
                "coexistence_relations",
                "holds",
                "transition_records",
            },
        )

        metadata = snapshot["metadata"]
        for key in (
            "snapshot_type",
            "snapshot_version",
            "generated_at",
            "source_host_class",
            "source_module",
        ):
            self.assertIsInstance(metadata[key], str)
            self.assertTrue(metadata[key])

        self.assertEqual(snapshot["host"]["host_id"], "snapshot-test-host")
        self.assertEqual(snapshot["host"]["open_object_ids"], [])
        self.assertEqual(snapshot["objects"], [])
        self.assertEqual(snapshot["coexistence_relations"], [])
        self.assertEqual(snapshot["holds"], [])
        self.assertEqual(snapshot["transition_records"], [])

    def test_snapshot_preserves_basic_host_state(self) -> None:
        host = self.make_host("basic-host")
        object_id = self.create_object(host, "matter-a", "payload-a")

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        obj = objects_by_id[object_id]

        self.assertEqual(snapshot["host"]["host_id"], "basic-host")
        self.assertEqual(snapshot["host"]["open_object_ids"], [object_id])
        self.assertEqual(obj["object_id"], object_id)
        self.assertEqual(obj["matter_ref"], "matter-a")
        self.assertEqual(obj["payload_ref"], "payload-a")
        self.assertEqual(obj["phase_state"], "CANDIDATE")
        self.assertIsNone(obj["resolution_type"])
        self.assertIsNone(obj["predecessor_object_id"])
        self.assertIsNone(obj["occurrence_ref"])
        self.assertIsInstance(obj["created_by_record_id"], str)
        self.assertTrue(obj["created_by_record_id"])
        self.assertIsNone(obj["resolved_by_record_id"])
        self.assert_no_enums(snapshot)

    def test_snapshot_preserves_lawful_distinct_matter_coexistence(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)

        self.assertEqual(set(objects_by_id), {first_id, second_id})
        self.assertEqual(set(snapshot["host"]["open_object_ids"]), {first_id, second_id})

        relations = snapshot["coexistence_relations"]
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertEqual(relation["relation_type"], "DISTINCT_MATTER_COHOSTED")
        self.assertEqual(relation["object_id"], second_id)
        self.assertEqual(relation["related_object_id"], first_id)
        self.assertEqual(relation["basis_ref"], "cohost-a-b")
        self.assertIsInstance(relation["created_by_record_id"], str)
        self.assertTrue(relation["created_by_record_id"])

        create_b_record = snapshot["transition_records"][-1]
        self.assertEqual(create_b_record["related_open_object_ids"], [first_id])
        self.assertEqual(create_b_record["created_coexistence_relations"], relations)

    def test_snapshot_preserves_presentation_and_standing_detail(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        self.present_object(host, second_id, "occurrence-b")
        self.stand_object(host, first_id, "threshold-a")

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        first = objects_by_id[first_id]
        second = objects_by_id[second_id]

        self.assertEqual(first["phase_state"], "STANDING")
        self.assertEqual(first["occurrence_ref"], "occurrence-a")
        self.assertIsNone(first["resolution_type"])
        self.assertEqual(second["phase_state"], "PRESENT")
        self.assertEqual(second["occurrence_ref"], "occurrence-b")
        self.assertIsNone(second["resolution_type"])
        self.assertNotEqual(first["occurrence_ref"], second["occurrence_ref"])

    def test_snapshot_preserves_standing_resolution_detail(self) -> None:
        for method_name, expected_resolution in (
            ("finalize", "FINALIZE"),
            ("invalidate", "INVALIDATE"),
        ):
            with self.subTest(method_name=method_name):
                host = self.make_host(f"{method_name}-host")
                object_id = self.create_standing_object(
                    host,
                    f"matter-{method_name}",
                    f"payload-{method_name}",
                )

                result = getattr(host, method_name)(object_id, f"{method_name}-basis")
                self.assertTrue(result.accepted)

                snapshot = build_snapshot(host)
                obj = self.snapshot_objects_by_id(snapshot)[object_id]
                self.assertEqual(obj["phase_state"], "STANDING")
                self.assertEqual(obj["resolution_type"], expected_resolution)
                self.assertEqual(obj["resolved_by_record_id"], result.record_id)
                self.assertNotIn(object_id, snapshot["host"]["open_object_ids"])

        evolve_host = self.make_host("evolve-host")
        predecessor_id = self.create_standing_object(
            evolve_host,
            "matter-evolve",
            "payload-evolve",
        )
        evolve = evolve_host.evolve(
            predecessor_id,
            "successor-payload",
            "evolve-basis",
        )
        self.assertTrue(evolve.accepted)
        successor_id = evolve.successor_object_id or ""

        snapshot = build_snapshot(evolve_host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        predecessor = objects_by_id[predecessor_id]
        successor = objects_by_id[successor_id]

        self.assertEqual(predecessor["phase_state"], "STANDING")
        self.assertEqual(predecessor["resolution_type"], "EVOLVE")
        self.assertEqual(predecessor["resolved_by_record_id"], evolve.record_id)
        self.assertNotIn(predecessor_id, snapshot["host"]["open_object_ids"])
        self.assertEqual(successor["phase_state"], "CANDIDATE")
        self.assertIsNone(successor["resolution_type"])
        self.assertEqual(successor["predecessor_object_id"], predecessor_id)
        self.assertIn(successor_id, snapshot["host"]["open_object_ids"])

    def test_snapshot_preserves_same_matter_post_resolution_refusal_trace(self) -> None:
        host = self.make_host()
        object_id = self.create_standing_object(host, "matter-x", "payload-x")
        finalize = host.finalize(object_id, "finalize-x")
        self.assertTrue(finalize.accepted)

        refused = host.create_object("matter-x", "payload-x2")
        self.assertFalse(refused.accepted)

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        same_matter_objects = [
            obj for obj in snapshot["objects"] if obj["matter_ref"] == "matter-x"
        ]
        refusal_record = snapshot["transition_records"][-1]

        self.assertIn(object_id, objects_by_id)
        self.assertEqual(len(same_matter_objects), 1)
        self.assertEqual(objects_by_id[object_id]["resolution_type"], "FINALIZE")
        self.assertEqual(refusal_record["record_id"], refused.record_id)
        self.assertFalse(refusal_record["accepted"])
        self.assertEqual(
            refusal_record["refusal_code"],
            "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
        )
        self.assertEqual(
            [record["record_id"] for record in snapshot["transition_records"]],
            [record.record_id for record in host.get_transition_records()],
        )

    def test_snapshot_preserves_hold_detail_under_coexistence(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        self.present_object(host, second_id, "occurrence-b")

        hold_first = host.set_hold(first_id, "hold-a")
        blocked = host.stand(first_id, "threshold-a")
        free = host.stand(second_id, "threshold-b")
        self.assertTrue(hold_first.accepted)
        self.assertFalse(blocked.accepted)
        self.assertTrue(free.accepted)

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        holds_by_target = {hold["target_object_id"]: hold for hold in snapshot["holds"]}

        self.assertEqual(set(holds_by_target), {first_id})
        self.assertTrue(holds_by_target[first_id]["active"])
        self.assertEqual(holds_by_target[first_id]["basis_ref"], "hold-a")
        self.assertEqual(holds_by_target[first_id]["set_by_record_id"], hold_first.record_id)
        self.assertEqual(objects_by_id[first_id]["phase_state"], "PRESENT")
        self.assertIsNone(objects_by_id[first_id]["resolution_type"])
        self.assertEqual(objects_by_id[second_id]["phase_state"], "STANDING")
        self.assertIsNone(objects_by_id[second_id]["resolution_type"])

        blocked_record = snapshot["transition_records"][-2]
        self.assertEqual(blocked_record["action_type"], "STAND")
        self.assertEqual(blocked_record["object_id"], first_id)
        self.assertFalse(blocked_record["accepted"])
        self.assertEqual(blocked_record["refusal_code"], "HOLD_BLOCKS_TRANSITION")
        self.assertTrue(blocked_record["hold_before"])
        self.assertTrue(blocked_record["hold_after"])

    def test_snapshot_preserves_append_only_refusal_visibility(self) -> None:
        host = self.make_host()
        attempts = []

        def attempt(call):
            result = call()
            attempts.append(result)
            self.assertEqual(len(host.get_transition_records()), len(attempts))
            return result

        first = attempt(lambda: host.create_object("matter-a", "payload-a"))
        first_id = first.object_id or ""
        missing_relation = attempt(lambda: host.create_object("matter-b", "payload-b"))
        second = attempt(
            lambda: host.create_object(
                "matter-b",
                "payload-b",
                cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
            )
        )
        second_id = second.object_id or ""
        same_matter = attempt(
            lambda: host.create_object(
                "matter-a",
                "payload-a2",
                cohost_basis_by_open_object_id={
                    first_id: "cohost-a-a2",
                    second_id: "cohost-b-a2",
                },
            )
        )
        attempt(lambda: host.present(first_id, "occurrence-a", "present-a"))
        threshold_failed = attempt(
            lambda: host.stand(first_id, "threshold-a", threshold_met=False)
        )
        attempt(lambda: host.set_hold(first_id, "hold-a"))
        hold_blocked = attempt(lambda: host.stand(first_id, "threshold-a"))

        snapshot = build_snapshot(host)
        records = snapshot["transition_records"]

        self.assertEqual(len(records), len(attempts))
        self.assertEqual(
            [record["record_id"] for record in records],
            [result.record_id for result in attempts],
        )
        self.assertEqual(
            missing_relation.refusal_code,
            RefusalCode.UNRESOLVED_COHOST_RELATION_REQUIRED,
        )
        self.assertEqual(
            same_matter.refusal_code,
            RefusalCode.SAME_MATTER_UNRESOLVED_COHOST_REFUSED,
        )
        self.assertEqual(threshold_failed.refusal_code, RefusalCode.THRESHOLD_NOT_MET)
        self.assertEqual(hold_blocked.refusal_code, RefusalCode.HOLD_BLOCKS_TRANSITION)

        phase_values = {phase.value for phase in PhaseState}
        resolution_values = {resolution.value for resolution in ResolutionType}
        relation_values = {relation.value for relation in RelationType}

        for result, record in zip(attempts, records):
            self.assertEqual(record["accepted"], result.accepted)
            if result.accepted:
                self.assertIsNone(record["refusal_code"])
            else:
                self.assertIsNotNone(record["refusal_code"])
                self.assertEqual(record["refusal_code"], result.refusal_code.value)
                self.assertNotIn(record["refusal_code"], phase_values)
                self.assertNotIn(record["refusal_code"], resolution_values)
                self.assertNotIn(record["refusal_code"], relation_values)

    def test_transition_record_export_detail(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        self.stand_object(host, first_id, "threshold-a")
        evolved = host.evolve(
            first_id,
            "successor-a",
            "evolve-a",
            cohost_basis_by_open_object_id={second_id: "cohost-successor-second"},
        )
        self.assertTrue(evolved.accepted)

        snapshot = build_snapshot(host)
        record = snapshot["transition_records"][-1]

        expected_keys = {
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
        self.assertEqual(set(record), expected_keys)
        self.assertEqual(record["host_id"], "snapshot-test-host")
        self.assertEqual(record["action_type"], "EVOLVE")
        self.assertEqual(record["matter_ref"], "matter-a")
        self.assertEqual(record["object_id"], first_id)
        self.assertEqual(record["related_open_object_ids"], [second_id])
        self.assertEqual(len(record["created_coexistence_relations"]), 1)
        self.assertEqual(record["predecessor_object_id"], first_id)
        self.assertEqual(record["successor_object_id"], evolved.successor_object_id)
        self.assertEqual(record["source_phase_state"], "STANDING")
        self.assertEqual(record["target_phase_state"], "STANDING")
        self.assertIsNone(record["source_resolution_type"])
        self.assertEqual(record["target_resolution_type"], "EVOLVE")
        self.assertEqual(record["payload_ref"], "successor-a")
        self.assertEqual(record["occurrence_ref"], "occurrence-a")
        self.assertEqual(record["basis_ref"], "evolve-a")
        self.assertIsNone(record["threshold_basis_ref"])
        self.assertFalse(record["hold_before"])
        self.assertFalse(record["hold_after"])
        self.assertTrue(record["accepted"])
        self.assertIsNone(record["refusal_code"])
        self.assertIsInstance(record["acted_at"], str)
        self.assertTrue(record["acted_at"])

    def test_snapshot_to_json_returns_valid_json_text(self) -> None:
        host = self.make_host()
        self.create_cohosted_pair(host)
        snapshot = build_snapshot(host)

        text = snapshot_to_json(snapshot)
        parsed = json.loads(text)

        self.assertIsInstance(text, str)
        self.assertTrue(text.endswith("\n"))
        self.assertIn("metadata", parsed)
        self.assertIn("host", parsed)
        self.assertIn("objects", parsed)
        self.assertIn("coexistence_relations", parsed)
        self.assertIn("holds", parsed)
        self.assertIn("transition_records", parsed)
        self.assertNotIn("PhaseState.", text)
        self.assertNotIn("ResolutionType.", text)
        self.assertNotIn("ActionType.", text)
        self.assertNotIn("RefusalCode.", text)
        self.assert_no_enums(parsed)

    def test_write_snapshot_writes_valid_json_file(self) -> None:
        host = self.make_host("write-host")
        object_id = self.create_object(host, "matter-write", "payload-write")

        with tempfile.TemporaryDirectory() as temp_dir:
            output_path = Path(temp_dir) / "nested" / "snapshot.json"
            written_path = write_snapshot(host, output_path)

            self.assertEqual(written_path, output_path)
            self.assertTrue(written_path.exists())
            parsed = json.loads(written_path.read_text(encoding="utf-8"))

        self.assertEqual(parsed["host"]["host_id"], "write-host")
        self.assertEqual(parsed["host"]["open_object_ids"], [object_id])
        self.assertEqual(len(parsed["objects"]), 1)
        self.assertEqual(parsed["objects"][0]["matter_ref"], "matter-write")

    def test_export_does_not_mutate_host_state(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        self.present_object(host, second_id, "occurrence-b")
        self.stand_object(host, first_id, "threshold-a")
        host.set_hold(second_id, "hold-b")
        refused = host.stand(second_id, "threshold-b")
        self.assertFalse(refused.accepted)

        before = self.host_facts(host)
        snapshot = build_snapshot(host)
        _ = snapshot_to_json(snapshot)

        with tempfile.TemporaryDirectory() as temp_dir:
            write_snapshot(host, Path(temp_dir) / "snapshot.json")

        after = self.host_facts(host)
        self.assertEqual(after, before)
        self.assertEqual(
            [record.record_id for record in host.get_transition_records()],
            before["record_ids"],
        )

    def test_snapshot_uses_public_read_posture_without_state_rewrite(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        host.set_hold(second_id, "hold-b")

        snapshot = build_snapshot(host)
        objects_by_id = self.snapshot_objects_by_id(snapshot)
        state = host.get_state()

        self.assertEqual(set(objects_by_id), set(state.objects))
        self.assertEqual(
            snapshot["host"]["open_object_ids"],
            list(state.open_object_ids),
        )
        self.assertEqual(
            len(snapshot["coexistence_relations"]),
            len(host.get_coexistence_relations()),
        )
        self.assertEqual(len(snapshot["holds"]), len(state.holds_by_object_id))
        self.assertEqual(
            len(snapshot["transition_records"]),
            len(host.get_transition_records()),
        )

        state.objects[first_id].phase_state = PhaseState.STANDING
        state.open_object_ids = ()
        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.PRESENT)
        self.assertIn(first_id, host.get_state().open_object_ids)

    def host_facts(self, host: IntegrityHostV0MinCoexistenceV2) -> dict[str, Any]:
        state = host.get_state()
        return {
            "record_count": len(state.transition_records),
            "record_ids": [record.record_id for record in state.transition_records],
            "open_object_ids": tuple(state.open_object_ids),
            "object_count": len(state.objects),
            "object_posture": {
                object_id: (
                    obj.phase_state,
                    obj.resolution_type,
                    obj.occurrence_ref,
                    obj.resolved_by_record_id,
                )
                for object_id, obj in state.objects.items()
            },
            "relation_count": len(state.coexistence_relations),
            "hold_count": len(state.holds_by_object_id),
            "hold_ids": tuple(sorted(state.holds_by_object_id)),
        }


if __name__ == "__main__":
    unittest.main()
