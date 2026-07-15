"""Bounded tests for the v0-min coexistence import/receiver layer.

These tests lock the current read-only import surface in
``src/integrity_host_v0_min_coexistence_import.py`` against real scenario
artifacts emitted through
``src/run_integrity_host_v0_min_coexistence_scenarios.py``.

They verify that scenario identity, snapshot metadata, host posture, objects,
coexistence relations, HOLDs, lineage, refusal, and append-only transition
records remain inspectable after import. They do not test replay, host merge,
registry behavior, persistence architecture, distributed continuity, CLI
behavior, or future workflow features.
"""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from dataclasses import FrozenInstanceError
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

import integrity_host_v0_min_coexistence_import as importer  # noqa: E402
import run_integrity_host_v0_min_coexistence_scenarios as runner  # noqa: E402


class IntegrityHostV0MinCoexistenceImportTests(unittest.TestCase):
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

    def valid_artifact(self) -> dict[str, Any]:
        return runner._build_scenario_artifact(
            runner.scenario_lawful_distinct_matter_coexistence()
        )

    def write_payload(self, directory: Path, payload: Any, name: str) -> Path:
        path = directory / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
        return path

    def imported_by_scenario(self) -> dict[str, importer.ImportedScenarioArtifact]:
        with tempfile.TemporaryDirectory() as temp_dir:
            paths = self.emit_all_scenarios(Path(temp_dir) / "artifacts")
            return {
                scenario_id: importer.load_scenario_artifact(path)
                for scenario_id, path in paths.items()
            }

    def objects_by_id(
        self,
        imported_artifact: importer.ImportedScenarioArtifact,
    ) -> dict[str, importer.ImportedIntegrityObject]:
        return {obj.object_id: obj for obj in imported_artifact.objects}

    def test_read_artifact_json_posture(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            output_dir = Path(temp_dir) / "artifacts"
            artifact_path = self.emit_scenario(
                output_dir,
                "lawful_distinct_matter_coexistence",
            )

            parsed = importer.read_artifact_json(artifact_path)

            self.assertIsInstance(parsed, dict)
            self.assertIn("scenario", parsed)
            self.assertIn("snapshot", parsed)

            malformed_path = Path(temp_dir) / "malformed.json"
            malformed_path.write_text("{not json", encoding="utf-8")
            with self.assertRaises(importer.ImportFormatError):
                importer.read_artifact_json(malformed_path)

            non_object_path = Path(temp_dir) / "non-object.json"
            non_object_path.write_text("[1, 2, 3]", encoding="utf-8")
            with self.assertRaises(importer.ImportFormatError):
                importer.read_artifact_json(non_object_path)

    def test_successful_load_of_emitted_scenario_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = self.emit_scenario(
                Path(temp_dir) / "artifacts",
                "lawful_distinct_matter_coexistence",
            )

            imported = importer.load_scenario_artifact(artifact_path)

            self.assertIsInstance(imported, importer.ImportedScenarioArtifact)
            self.assertIsInstance(imported.scenario, importer.ImportedScenarioMetadata)
            self.assertIsInstance(
                imported.snapshot_metadata,
                importer.ImportedSnapshotMetadata,
            )
            self.assertIsInstance(imported.host, importer.ImportedHostState)
            self.assertGreater(len(imported.objects), 0)
            self.assertGreater(len(imported.coexistence_relations), 0)
            self.assertEqual(len(imported.holds), 0)
            self.assertGreater(len(imported.transition_records), 0)

            with self.assertRaises(FrozenInstanceError):
                imported.host.host_id = "changed"  # type: ignore[misc]

    def test_imported_scenario_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = self.emit_scenario(
                Path(temp_dir) / "artifacts",
                "refused_missing_coexistence_basis",
            )
            imported = importer.load_scenario_artifact(artifact_path)

            scenario = imported.scenario

            self.assertEqual(
                scenario.scenario_id,
                "refused_missing_coexistence_basis",
            )
            self.assertTrue(scenario.scenario_name)
            self.assertTrue(scenario.description)
            self.assertTrue(scenario.generated_at)
            self.assertEqual(scenario.source_path, artifact_path.resolve().as_posix())
            self.assertEqual(scenario.accepted_action_count, 1)
            self.assertEqual(scenario.refused_action_count, 1)
            self.assertEqual(len(scenario.action_results), 2)
            self.assertEqual(
                scenario.accepted_action_count,
                sum(1 for action in scenario.action_results if action.accepted),
            )
            self.assertEqual(
                scenario.refused_action_count,
                sum(1 for action in scenario.action_results if not action.accepted),
            )

            first_action = scenario.action_results[0]
            self.assertIsInstance(first_action.label, str)
            self.assertIsInstance(first_action.accepted, bool)
            self.assertIsInstance(first_action.state_changed, bool)
            self.assertIsInstance(first_action.record_id, str)
            self.assertIsInstance(first_action.object_id, str)
            self.assertIsNone(first_action.successor_object_id)
            self.assertIsNone(first_action.refusal_code)

            refused_action = scenario.action_results[-1]
            self.assertFalse(refused_action.accepted)
            self.assertFalse(refused_action.state_changed)
            self.assertIsNone(refused_action.object_id)
            self.assertEqual(
                refused_action.refusal_code,
                "UNRESOLVED_COHOST_RELATION_REQUIRED",
            )

    def test_imported_snapshot_metadata_and_host_state(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = self.emit_scenario(
                Path(temp_dir) / "artifacts",
                "lawful_distinct_matter_coexistence",
            )
            imported = importer.load_scenario_artifact(artifact_path)

            metadata = imported.snapshot_metadata
            self.assertEqual(
                metadata.snapshot_type,
                "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT",
            )
            self.assertEqual(metadata.snapshot_version, "0.1.0")
            self.assertTrue(metadata.generated_at)
            self.assertEqual(
                metadata.source_host_class,
                "IntegrityHostV0MinCoexistenceV2",
            )
            self.assertEqual(
                metadata.source_module,
                "integrity_host_v0_min_coexistence_v2",
            )

            self.assertEqual(imported.host.host_id, "scenario-lawful-coexistence")
            self.assertIsInstance(imported.host.open_object_ids, tuple)
            self.assertEqual(len(imported.host.open_object_ids), 2)

    def test_imported_objects_preserve_trace_and_lineage(self) -> None:
        imported = self.imported_by_scenario()["evolve_under_coexistence"]
        objects = self.objects_by_id(imported)

        predecessor = next(
            obj for obj in imported.objects if obj.resolution_type == "EVOLVE"
        )
        successor = next(
            obj
            for obj in imported.objects
            if obj.predecessor_object_id == predecessor.object_id
        )

        for obj in imported.objects:
            self.assertIsInstance(obj.object_id, str)
            self.assertIsInstance(obj.matter_ref, str)
            self.assertIsInstance(obj.payload_ref, str)
            self.assertIn(obj.phase_state, {"CANDIDATE", "PRESENT", "STANDING"})
            self.assertIsInstance(obj.created_by_record_id, str)

        self.assertIn(predecessor.object_id, objects)
        self.assertEqual(predecessor.phase_state, "STANDING")
        self.assertEqual(predecessor.resolution_type, "EVOLVE")
        self.assertIsNone(predecessor.predecessor_object_id)
        self.assertEqual(predecessor.occurrence_ref, "occurrence-a")
        self.assertIsNotNone(predecessor.resolved_by_record_id)
        self.assertNotIn(predecessor.object_id, imported.host.open_object_ids)

        self.assertEqual(successor.phase_state, "CANDIDATE")
        self.assertIsNone(successor.resolution_type)
        self.assertEqual(successor.predecessor_object_id, predecessor.object_id)
        self.assertIsNone(successor.occurrence_ref)
        self.assertIsNone(successor.resolved_by_record_id)
        self.assertIn(successor.object_id, imported.host.open_object_ids)

    def test_imported_coexistence_relations_preserve_direction(self) -> None:
        imported = self.imported_by_scenario()["lawful_distinct_matter_coexistence"]
        objects = self.objects_by_id(imported)

        self.assertEqual(len(imported.coexistence_relations), 1)
        relation = imported.coexistence_relations[0]

        self.assertEqual(relation.relation_type, "DISTINCT_MATTER_COHOSTED")
        self.assertEqual(objects[relation.object_id].matter_ref, "matter-b")
        self.assertEqual(objects[relation.related_object_id].matter_ref, "matter-a")
        self.assertEqual(relation.basis_ref, "cohost-a-b")
        self.assertIsInstance(relation.created_by_record_id, str)
        self.assertTrue(relation.created_by_record_id)

        create_b_record = next(
            record
            for record in imported.transition_records
            if record.action_type == "CREATE_OBJECT"
            and record.created_coexistence_relations
        )
        self.assertEqual(create_b_record.created_coexistence_relations, (relation,))

    def test_imported_holds_remain_separate_from_phase_and_resolution(self) -> None:
        imported = self.imported_by_scenario()[
            "hold_blocks_one_target_while_another_proceeds"
        ]
        objects = self.objects_by_id(imported)

        self.assertEqual(len(imported.holds), 1)
        hold = imported.holds[0]

        self.assertTrue(hold.active)
        self.assertEqual(hold.basis_ref, "hold-a")
        self.assertIsInstance(hold.target_object_id, str)
        self.assertIsInstance(hold.set_by_record_id, str)
        self.assertIn(hold.target_object_id, objects)

        held_object = objects[hold.target_object_id]
        self.assertEqual(held_object.phase_state, "PRESENT")
        self.assertIsNone(held_object.resolution_type)
        self.assertNotIn("HOLD", {obj.phase_state for obj in imported.objects})
        self.assertNotIn(
            "HOLD",
            {obj.resolution_type for obj in imported.objects if obj.resolution_type},
        )

    def test_imported_transition_records_preserve_detail(self) -> None:
        imported = self.imported_by_scenario()["evolve_under_coexistence"]
        record = imported.transition_records[-1]

        self.assertIsInstance(record.record_id, str)
        self.assertEqual(record.host_id, "scenario-evolve-under-coexistence")
        self.assertEqual(record.action_type, "EVOLVE")
        self.assertEqual(record.matter_ref, "matter-a")
        self.assertIsInstance(record.object_id, str)
        self.assertEqual(record.related_open_object_ids, (record.related_open_object_ids[0],))
        self.assertEqual(len(record.created_coexistence_relations), 1)
        self.assertEqual(record.predecessor_object_id, record.object_id)
        self.assertIsInstance(record.successor_object_id, str)
        self.assertEqual(record.source_phase_state, "STANDING")
        self.assertEqual(record.target_phase_state, "STANDING")
        self.assertIsNone(record.source_resolution_type)
        self.assertEqual(record.target_resolution_type, "EVOLVE")
        self.assertEqual(record.payload_ref, "payload-a-successor")
        self.assertEqual(record.occurrence_ref, "occurrence-a")
        self.assertEqual(record.basis_ref, "evolve-a")
        self.assertIsNone(record.threshold_basis_ref)
        self.assertIsInstance(record.hold_before, bool)
        self.assertIsInstance(record.hold_after, bool)
        self.assertTrue(record.accepted)
        self.assertIsNone(record.refusal_code)
        self.assertIsInstance(record.acted_at, str)
        self.assertTrue(record.acted_at)

        self.assertEqual(
            [record.record_id for record in imported.transition_records],
            [action.record_id for action in imported.scenario.action_results],
        )

    def test_refusal_visibility_on_import(self) -> None:
        imported_by_id = self.imported_by_scenario()
        missing_basis = imported_by_id["refused_missing_coexistence_basis"]
        same_matter = imported_by_id["same_matter_post_resolution_refusal"]

        missing_refusal_records = [
            record for record in missing_basis.transition_records if not record.accepted
        ]
        self.assertEqual(len(missing_refusal_records), 1)
        self.assertEqual(
            missing_refusal_records[0].refusal_code,
            "UNRESOLVED_COHOST_RELATION_REQUIRED",
        )
        self.assertEqual(len(missing_basis.objects), 1)
        self.assertEqual(missing_basis.objects[0].matter_ref, "matter-a")

        same_matter_refusals = [
            record for record in same_matter.transition_records if not record.accepted
        ]
        self.assertEqual(len(same_matter_refusals), 1)
        self.assertEqual(
            same_matter_refusals[0].refusal_code,
            "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED",
        )
        self.assertEqual(len(same_matter.objects), 1)
        self.assertEqual(same_matter.objects[0].resolution_type, "FINALIZE")
        self.assertEqual(
            len([obj for obj in same_matter.objects if obj.matter_ref == "matter-a"]),
            1,
        )

    def test_lineage_visibility_on_import(self) -> None:
        imported = self.imported_by_scenario()["evolve_under_coexistence"]
        predecessor = next(
            obj for obj in imported.objects if obj.resolution_type == "EVOLVE"
        )
        successor = next(
            obj
            for obj in imported.objects
            if obj.predecessor_object_id == predecessor.object_id
        )
        evolve_record = imported.transition_records[-1]

        self.assertEqual(evolve_record.action_type, "EVOLVE")
        self.assertEqual(evolve_record.predecessor_object_id, predecessor.object_id)
        self.assertEqual(evolve_record.successor_object_id, successor.object_id)
        self.assertEqual(predecessor.phase_state, "STANDING")
        self.assertEqual(predecessor.resolution_type, "EVOLVE")
        self.assertEqual(successor.phase_state, "CANDIDATE")
        self.assertIsNone(successor.resolution_type)
        self.assertEqual(successor.predecessor_object_id, predecessor.object_id)

    def test_import_summary(self) -> None:
        imported = self.imported_by_scenario()[
            "hold_blocks_one_target_while_another_proceeds"
        ]

        summary = importer.build_import_summary(imported)

        self.assertEqual(
            set(summary),
            {
                "scenario_id",
                "scenario_name",
                "source_path",
                "snapshot_type",
                "snapshot_version",
                "host_id",
                "object_count",
                "open_object_count",
                "coexistence_relation_count",
                "hold_count",
                "record_count",
                "refusal_count",
                "accepted_action_count",
                "refused_action_count",
            },
        )
        self.assertEqual(
            summary["scenario_id"],
            "hold_blocks_one_target_while_another_proceeds",
        )
        self.assertTrue(summary["scenario_name"])
        self.assertTrue(summary["source_path"])
        self.assertEqual(
            summary["snapshot_type"],
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT",
        )
        self.assertEqual(summary["snapshot_version"], "0.1.0")
        self.assertEqual(summary["host_id"], "scenario-target-specific-hold")
        self.assertEqual(summary["object_count"], 2)
        self.assertEqual(summary["open_object_count"], 2)
        self.assertEqual(summary["coexistence_relation_count"], 1)
        self.assertEqual(summary["hold_count"], 1)
        self.assertEqual(summary["record_count"], 7)
        self.assertEqual(summary["refusal_count"], 1)
        self.assertEqual(summary["accepted_action_count"], 6)
        self.assertEqual(summary["refused_action_count"], 1)

    def test_shape_validation_failures(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)
            cases: list[tuple[str, dict[str, Any]]] = []

            for key in ("scenario", "snapshot"):
                payload = copy.deepcopy(self.valid_artifact())
                del payload[key]
                cases.append((f"missing-{key}.json", payload))

            for key in (
                "metadata",
                "host",
                "objects",
                "coexistence_relations",
                "holds",
                "transition_records",
            ):
                payload = copy.deepcopy(self.valid_artifact())
                del payload["snapshot"][key]
                cases.append((f"missing-snapshot-{key}.json", payload))

            wrong_type = copy.deepcopy(self.valid_artifact())
            wrong_type["snapshot"]["host"]["open_object_ids"] = "not-a-list"
            cases.append(("wrong-basic-type.json", wrong_type))

            wrong_required_string = copy.deepcopy(self.valid_artifact())
            wrong_required_string["snapshot"]["metadata"]["snapshot_type"] = None
            cases.append(("wrong-required-string.json", wrong_required_string))

            wrong_count = copy.deepcopy(self.valid_artifact())
            wrong_count["scenario"]["accepted_action_count"] = 999
            cases.append(("wrong-action-count.json", wrong_count))

            for filename, payload in cases:
                with self.subTest(filename=filename):
                    path = self.write_payload(temp_path, payload, filename)
                    with self.assertRaises(importer.ImportFormatError):
                        importer.load_scenario_artifact(path)

    def test_import_does_not_mutate_source_artifact(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            artifact_path = self.emit_scenario(
                Path(temp_dir) / "artifacts",
                "same_matter_post_resolution_refusal",
            )
            before_text = artifact_path.read_text(encoding="utf-8")

            imported = importer.load_scenario_artifact(artifact_path)
            summary = importer.build_import_summary(imported)
            after_text = artifact_path.read_text(encoding="utf-8")

            self.assertEqual(after_text, before_text)
            self.assertEqual(
                summary["scenario_id"],
                "same_matter_post_resolution_refusal",
            )
            self.assertEqual(
                [record.record_id for record in imported.transition_records],
                [action.record_id for action in imported.scenario.action_results],
            )


if __name__ == "__main__":
    unittest.main()
