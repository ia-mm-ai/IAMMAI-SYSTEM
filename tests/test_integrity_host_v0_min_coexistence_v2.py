"""Bounded executable tests for the v0-min coexistence successor host.

These tests lock the current in-memory behavior in
``src/integrity_host_v0_min_coexistence_v2.py``. They test the bounded
same-host coexistence slice only: distinct-matter unresolved coexistence with
explicit pairwise marking, same-matter unresolved refusal, same-matter
post-resolution refusal after FINALIZE or INVALIDATE, EVOLVE lineage,
target-specific HOLD, append-only records, and explicit refusal.

They do not test persistence, distributed behavior, cross-host continuity,
full relation doctrine, full presence doctrine, governance, witness families,
or minimum lawful system closure.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from integrity_host_v0_min_coexistence_v2 import (  # noqa: E402
    ActionType,
    IntegrityHostV0MinCoexistenceV2,
    PhaseState,
    RefusalCode,
    RelationType,
    ResolutionType,
)


class IntegrityHostV0MinCoexistenceV2Tests(unittest.TestCase):
    def make_host(self) -> IntegrityHostV0MinCoexistenceV2:
        return IntegrityHostV0MinCoexistenceV2("test-host")

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
        self.assertTrue(result.state_changed)
        self.assertIsNotNone(result.object_id)
        return result.object_id or ""

    def create_cohosted_pair(
        self, host: IntegrityHostV0MinCoexistenceV2
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
        occurrence_ref: str = "occurrence",
    ) -> None:
        result = host.present(object_id, occurrence_ref, f"present-{occurrence_ref}")
        self.assertTrue(result.accepted)

    def stand_object(
        self,
        host: IntegrityHostV0MinCoexistenceV2,
        object_id: str,
        threshold_basis_ref: str = "threshold-basis",
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

    def test_first_object_create_success(self) -> None:
        host = self.make_host()

        result = host.create_object(
            "matter-a",
            "payload-a",
            basis_ref="create-a",
        )

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        self.assertIsNotNone(result.object_id)

        object_id = result.object_id or ""
        obj = host.get_object(object_id)
        self.assertIsNotNone(obj)
        self.assertEqual(obj.phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(obj.resolution_type)
        self.assertIn(object_id, host.get_state().open_object_ids)

        records = host.get_transition_records()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].action_type, ActionType.CREATE_OBJECT)
        self.assertTrue(records[0].accepted)
        self.assertEqual(records[0].object_id, object_id)
        self.assertEqual(records[0].target_phase_state, PhaseState.CANDIDATE)
        self.assertEqual(records[0].created_coexistence_relations, ())
        self.assertEqual(host.get_coexistence_relations(), ())

    def test_lawful_distinct_matter_unresolved_coexistence(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-a", "payload-a")

        result = host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-b",
            cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
        )

        self.assertTrue(result.accepted)
        second_id = result.object_id or ""
        state = host.get_state()
        self.assertIn(first_id, state.open_object_ids)
        self.assertIn(second_id, state.open_object_ids)
        self.assertIsNone(host.get_object(first_id).resolution_type)
        self.assertIsNone(host.get_object(second_id).resolution_type)

        relations = host.get_coexistence_relations()
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertEqual(relation.relation_type, RelationType.DISTINCT_MATTER_COHOSTED)
        self.assertEqual(relation.object_id, second_id)
        self.assertEqual(relation.related_object_id, first_id)
        self.assertEqual(relation.basis_ref, "cohost-a-b")

        records = host.get_transition_records()
        self.assertEqual(len(records), 2)
        self.assertEqual(records[-1].related_open_object_ids, (first_id,))
        self.assertEqual(records[-1].created_coexistence_relations, relations)

    def test_missing_coexistence_relation_basis_is_refused(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-a", "payload-a")
        before_object = host.get_object(first_id)
        before_ids = set(host.get_state().objects)

        missing_mapping = host.create_object("matter-b", "payload-b")

        self.assertFalse(missing_mapping.accepted)
        self.assertFalse(missing_mapping.state_changed)
        self.assertEqual(
            missing_mapping.refusal_code,
            RefusalCode.UNRESOLVED_COHOST_RELATION_REQUIRED,
        )
        self.assertIsNone(missing_mapping.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)
        self.assertEqual(host.get_object(first_id), before_object)
        self.assertEqual(len(host.get_transition_records()), 2)

        blank_basis = host.create_object(
            "matter-b",
            "payload-b",
            cohost_basis_by_open_object_id={first_id: "   "},
        )

        self.assertFalse(blank_basis.accepted)
        self.assertFalse(blank_basis.state_changed)
        self.assertEqual(
            blank_basis.refusal_code,
            RefusalCode.MISSING_COHOST_RELATION_BASIS,
        )
        self.assertIsNone(blank_basis.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)
        self.assertEqual(host.get_object(first_id), before_object)
        self.assertEqual(len(host.get_transition_records()), 3)

    def test_relation_target_mismatch_is_refused(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-a", "payload-a")
        before_ids = set(host.get_state().objects)

        nonexistent_target = host.create_object(
            "matter-b",
            "payload-b",
            cohost_basis_by_open_object_id={"missing-object": "basis"},
        )

        self.assertFalse(nonexistent_target.accepted)
        self.assertEqual(
            nonexistent_target.refusal_code,
            RefusalCode.RELATION_TARGET_NOT_OPEN,
        )
        self.assertIsNone(nonexistent_target.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)
        self.assertEqual(len(host.get_transition_records()), 2)

        host.present(first_id, "occurrence-a", "present-a")
        host.stand(first_id, "threshold-a")
        host.finalize(first_id, "finalize-a")
        before_ids = set(host.get_state().objects)

        non_open_target = host.create_object(
            "matter-b",
            "payload-b",
            cohost_basis_by_open_object_id={first_id: "basis"},
        )

        self.assertFalse(non_open_target.accepted)
        self.assertEqual(
            non_open_target.refusal_code,
            RefusalCode.RELATION_TARGET_NOT_OPEN,
        )
        self.assertIsNone(non_open_target.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)

    def test_same_matter_unresolved_coexistence_is_refused(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-x", "payload-a")
        before_object = host.get_object(first_id)
        before_ids = set(host.get_state().objects)

        result = host.create_object(
            "matter-x",
            "payload-b",
            cohost_basis_by_open_object_id={first_id: "cohost-basis"},
        )

        self.assertFalse(result.accepted)
        self.assertFalse(result.state_changed)
        self.assertEqual(
            result.refusal_code,
            RefusalCode.SAME_MATTER_UNRESOLVED_COHOST_REFUSED,
        )
        self.assertIsNone(result.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)
        self.assertEqual(host.get_object(first_id), before_object)
        self.assertEqual(host.get_state().open_object_ids, (first_id,))

    def test_overlap_asserted_unresolved_coexistence_is_refused(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-a", "payload-a")
        before_ids = set(host.get_state().objects)

        result = host.create_object(
            "matter-b",
            "payload-b",
            cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
            overlapping_open_object_ids={first_id},
        )

        self.assertFalse(result.accepted)
        self.assertFalse(result.state_changed)
        self.assertEqual(
            result.refusal_code,
            RefusalCode.OVERLAPPING_MATTER_UNRESOLVED_COHOST_REFUSED,
        )
        self.assertIsNone(result.object_id)
        self.assertEqual(set(host.get_state().objects), before_ids)
        self.assertEqual(len(host.get_transition_records()), 2)

    def test_present_behavior_under_coexistence(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)

        first_present = host.present(first_id, "occurrence-a", "present-a")

        self.assertTrue(first_present.accepted)
        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.PRESENT)
        self.assertEqual(host.get_object(first_id).occurrence_ref, "occurrence-a")
        self.assertEqual(host.get_object(second_id).phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(host.get_object(second_id).occurrence_ref)
        self.assertIn(first_id, host.get_state().open_object_ids)
        self.assertIn(second_id, host.get_state().open_object_ids)

        second_present = host.present(second_id, "occurrence-b", "present-b")

        self.assertTrue(second_present.accepted)
        self.assertEqual(host.get_object(second_id).phase_state, PhaseState.PRESENT)
        self.assertEqual(host.get_object(second_id).occurrence_ref, "occurrence-b")

        missing_occurrence_host = self.make_host()
        candidate_id = self.create_object(
            missing_occurrence_host, "matter-a", "payload-a"
        )
        missing_occurrence = missing_occurrence_host.present(
            candidate_id, "", "present-a"
        )
        self.assertFalse(missing_occurrence.accepted)
        self.assertEqual(
            missing_occurrence.refusal_code,
            RefusalCode.MISSING_OCCURRENCE_REF,
        )

        missing_basis = missing_occurrence_host.present(
            candidate_id, "occurrence-a", ""
        )
        self.assertFalse(missing_basis.accepted)
        self.assertEqual(missing_basis.refusal_code, RefusalCode.MISSING_BASIS_REF)

        nonexistent = host.present("missing-object", "occurrence", "basis")
        self.assertFalse(nonexistent.accepted)
        self.assertEqual(nonexistent.refusal_code, RefusalCode.OBJECT_NOT_FOUND)

        wrong_phase = host.present(first_id, "occurrence-again", "basis")
        self.assertFalse(wrong_phase.accepted)
        self.assertEqual(wrong_phase.refusal_code, RefusalCode.INVALID_PHASE_FOR_ACTION)

        resolved_host = self.make_host()
        resolved_id = self.create_standing_object(
            resolved_host, "matter-r", "payload-r"
        )
        resolved_host.finalize(resolved_id, "finalize-r")
        resolved_present = resolved_host.present(
            resolved_id, "occurrence-r2", "present-r2"
        )
        self.assertFalse(resolved_present.accepted)
        self.assertEqual(resolved_present.refusal_code, RefusalCode.ALREADY_RESOLVED)

    def test_stand_behavior_under_coexistence(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        self.present_object(host, first_id, "occurrence-a")
        self.present_object(host, second_id, "occurrence-b")

        failed = host.stand(first_id, "threshold-a", threshold_met=False)
        self.assertFalse(failed.accepted)
        self.assertEqual(failed.refusal_code, RefusalCode.THRESHOLD_NOT_MET)
        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.PRESENT)

        second_stand = host.stand(second_id, "threshold-b")
        self.assertTrue(second_stand.accepted)
        self.assertEqual(host.get_object(second_id).phase_state, PhaseState.STANDING)
        self.assertIsNone(host.get_object(second_id).resolution_type)

        first_stand = host.stand(first_id, "threshold-a")
        self.assertTrue(first_stand.accepted)
        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.STANDING)
        stand_record = host.get_transition_records()[-1]
        self.assertEqual(stand_record.action_type, ActionType.STAND)
        self.assertNotEqual(stand_record.action_type, ActionType.FINALIZE)

        direct_host = self.make_host()
        candidate_id = self.create_object(direct_host, "matter-c", "payload-c")
        direct = direct_host.stand(candidate_id, "threshold-c")
        self.assertFalse(direct.accepted)
        self.assertEqual(direct.refusal_code, RefusalCode.PRESENCE_REQUIRED)

        self.present_object(direct_host, candidate_id, "occurrence-c")
        missing_basis = direct_host.stand(candidate_id, "")
        self.assertFalse(missing_basis.accepted)
        self.assertEqual(
            missing_basis.refusal_code,
            RefusalCode.THRESHOLD_BASIS_MISSING,
        )

        nonexistent = direct_host.stand("missing-object", "threshold")
        self.assertFalse(nonexistent.accepted)
        self.assertEqual(nonexistent.refusal_code, RefusalCode.OBJECT_NOT_FOUND)

        hold_host = self.make_host()
        held_id = self.create_object(hold_host, "matter-h", "payload-h")
        self.present_object(hold_host, held_id, "occurrence-h")
        self.assertTrue(hold_host.set_hold(held_id, "hold-h").accepted)
        blocked = hold_host.stand(held_id, "threshold-h")
        self.assertFalse(blocked.accepted)
        self.assertEqual(blocked.refusal_code, RefusalCode.HOLD_BLOCKS_TRANSITION)

    def test_finalize_and_invalidate_under_coexistence(self) -> None:
        for method_name, resolution_type in (
            ("finalize", ResolutionType.FINALIZE),
            ("invalidate", ResolutionType.INVALIDATE),
        ):
            with self.subTest(method_name=method_name):
                host = self.make_host()
                first_id, second_id = self.create_cohosted_pair(host)
                self.present_object(host, first_id, "occurrence-a")
                self.stand_object(host, first_id, "threshold-a")
                before_second = host.get_object(second_id)

                result = getattr(host, method_name)(first_id, f"{method_name}-a")

                self.assertTrue(result.accepted)
                self.assertTrue(result.state_changed)
                first = host.get_object(first_id)
                self.assertEqual(first.phase_state, PhaseState.STANDING)
                self.assertEqual(first.resolution_type, resolution_type)
                self.assertIsNotNone(first.resolved_by_record_id)
                self.assertNotIn(first_id, host.get_state().open_object_ids)
                self.assertIn(second_id, host.get_state().open_object_ids)
                self.assertEqual(host.get_object(second_id), before_second)

        for method_name in ("finalize", "invalidate"):
            with self.subTest(refusal=method_name):
                host = self.make_host()
                object_id = self.create_object(host, "matter-r", "payload-r")

                candidate = getattr(host, method_name)(object_id, "basis")
                self.assertFalse(candidate.accepted)
                self.assertEqual(candidate.refusal_code, RefusalCode.STANDING_REQUIRED)

                self.present_object(host, object_id, "occurrence-r")
                present = getattr(host, method_name)(object_id, "basis")
                self.assertFalse(present.accepted)
                self.assertEqual(present.refusal_code, RefusalCode.STANDING_REQUIRED)

                self.stand_object(host, object_id, "threshold-r")
                resolved = getattr(host, method_name)(object_id, "basis")
                self.assertTrue(resolved.accepted)
                already = getattr(host, method_name)(object_id, "basis-again")
                self.assertFalse(already.accepted)
                self.assertEqual(already.refusal_code, RefusalCode.ALREADY_RESOLVED)

    def test_evolve_behavior_and_coexistence_guard(self) -> None:
        host = self.make_host()
        predecessor_id = self.create_standing_object(
            host, "matter-a", "payload-a"
        )

        result = host.evolve(
            predecessor_id,
            "successor-payload-a",
            "evolve-a",
        )

        self.assertTrue(result.accepted)
        successor_id = result.successor_object_id or ""
        predecessor = host.get_object(predecessor_id)
        successor = host.get_object(successor_id)
        self.assertEqual(predecessor.resolution_type, ResolutionType.EVOLVE)
        self.assertIsNotNone(predecessor.resolved_by_record_id)
        self.assertNotIn(predecessor_id, host.get_state().open_object_ids)
        self.assertEqual(successor.phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(successor.resolution_type)
        self.assertEqual(successor.predecessor_object_id, predecessor_id)
        self.assertIn(successor_id, host.get_state().open_object_ids)

        record = host.get_transition_records()[-1]
        self.assertEqual(record.action_type, ActionType.EVOLVE)
        self.assertEqual(record.predecessor_object_id, predecessor_id)
        self.assertEqual(record.successor_object_id, successor_id)
        self.assertEqual(record.target_resolution_type, ResolutionType.EVOLVE)

        coexistence_host = self.make_host()
        first_id, other_id = self.create_cohosted_pair(coexistence_host)
        self.present_object(coexistence_host, first_id, "occurrence-a")
        self.stand_object(coexistence_host, first_id, "threshold-a")

        missing_basis = coexistence_host.evolve(
            first_id,
            "successor-payload-a",
            "evolve-a",
        )

        self.assertFalse(missing_basis.accepted)
        self.assertEqual(
            missing_basis.refusal_code,
            RefusalCode.UNRESOLVED_COHOST_RELATION_REQUIRED,
        )
        self.assertIsNone(missing_basis.successor_object_id)

        accepted = coexistence_host.evolve(
            first_id,
            "successor-payload-a",
            "evolve-a",
            cohost_basis_by_open_object_id={other_id: "cohost-successor-other"},
        )

        self.assertTrue(accepted.accepted)
        accepted_record = coexistence_host.get_transition_records()[-1]
        self.assertEqual(accepted_record.related_open_object_ids, (other_id,))
        self.assertEqual(len(accepted_record.created_coexistence_relations), 1)
        self.assertEqual(
            accepted_record.created_coexistence_relations[0].related_object_id,
            other_id,
        )

    def test_same_matter_post_resolution_refusal(self) -> None:
        for method_name, refusal_code in (
            (
                "finalize",
                RefusalCode.SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED,
            ),
            (
                "invalidate",
                RefusalCode.SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED,
            ),
        ):
            with self.subTest(method_name=method_name):
                host = self.make_host()
                object_id = self.create_standing_object(
                    host, "matter-x", "payload-x"
                )
                getattr(host, method_name)(object_id, f"{method_name}-x")
                before_ids = set(host.get_state().objects)

                result = host.create_object("matter-x", "payload-x2")

                self.assertFalse(result.accepted)
                self.assertFalse(result.state_changed)
                self.assertEqual(result.refusal_code, refusal_code)
                self.assertIsNone(result.object_id)
                self.assertEqual(set(host.get_state().objects), before_ids)

        evolve_host = self.make_host()
        predecessor_id = self.create_standing_object(
            evolve_host, "matter-x", "payload-x"
        )
        evolve = evolve_host.evolve(
            predecessor_id,
            "successor-payload-x",
            "evolve-x",
        )
        self.assertTrue(evolve.accepted)
        self.assertIsNotNone(evolve.successor_object_id)

    def test_resolved_standing_coexists_as_preserved_trace(self) -> None:
        host = self.make_host()
        resolved_id = self.create_standing_object(
            host, "matter-a", "payload-a"
        )
        host.finalize(resolved_id, "finalize-a")
        preserved_before = host.get_object(resolved_id)

        result = host.create_object(
            "matter-b",
            "payload-b",
            basis_ref="create-b",
        )

        self.assertTrue(result.accepted)
        second_id = result.object_id or ""
        self.assertIn(resolved_id, host.get_state().objects)
        self.assertNotIn(resolved_id, host.get_state().open_object_ids)
        self.assertIn(second_id, host.get_state().open_object_ids)
        self.assertEqual(host.get_object(resolved_id), preserved_before)
        self.assertEqual(host.get_object(second_id).phase_state, PhaseState.CANDIDATE)
        self.assertEqual(host.get_coexistence_relations(), ())

    def test_hold_under_coexistence(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)
        before_first = host.get_object(first_id)

        first_hold = host.set_hold(first_id, "hold-a")
        second_hold = host.set_hold(second_id, "hold-b")

        self.assertTrue(first_hold.accepted)
        self.assertTrue(second_hold.accepted)
        state = host.get_state()
        self.assertIn(first_id, state.holds_by_object_id)
        self.assertIn(second_id, state.holds_by_object_id)
        self.assertEqual(state.holds_by_object_id[first_id].target_object_id, first_id)
        self.assertEqual(state.holds_by_object_id[second_id].target_object_id, second_id)

        duplicate = host.set_hold(first_id, "hold-a-again")
        self.assertFalse(duplicate.accepted)
        self.assertEqual(duplicate.refusal_code, RefusalCode.DUPLICATE_HOLD_ON_TARGET)
        self.assertEqual(host.get_object(first_id), before_first)

        released = host.release_hold(first_id, "release-a")
        self.assertTrue(released.accepted)
        self.assertNotIn(first_id, host.get_state().holds_by_object_id)
        self.assertIn(second_id, host.get_state().holds_by_object_id)
        self.assertEqual(host.get_object(first_id).phase_state, before_first.phase_state)
        self.assertEqual(
            host.get_object(first_id).resolution_type,
            before_first.resolution_type,
        )

        stand_host = self.make_host()
        held_id, free_id = self.create_cohosted_pair(stand_host)
        self.present_object(stand_host, held_id, "occurrence-held")
        self.present_object(stand_host, free_id, "occurrence-free")
        stand_host.set_hold(held_id, "hold-held")

        blocked = stand_host.stand(held_id, "threshold-held")
        free = stand_host.stand(free_id, "threshold-free")

        self.assertFalse(blocked.accepted)
        self.assertEqual(blocked.refusal_code, RefusalCode.HOLD_BLOCKS_TRANSITION)
        self.assertTrue(free.accepted)
        self.assertEqual(stand_host.get_object(held_id).phase_state, PhaseState.PRESENT)
        self.assertEqual(stand_host.get_object(free_id).phase_state, PhaseState.STANDING)

        for action_name in ("finalize", "invalidate", "evolve"):
            with self.subTest(action_name=action_name):
                action_host = self.make_host()
                held_id, free_id = self.create_cohosted_pair(action_host)
                for object_id, suffix in ((held_id, "held"), (free_id, "free")):
                    self.present_object(action_host, object_id, f"occurrence-{suffix}")
                    self.stand_object(action_host, object_id, f"threshold-{suffix}")
                action_host.set_hold(held_id, "hold-held")
                before_held = action_host.get_object(held_id)

                if action_name == "evolve":
                    blocked_action = action_host.evolve(
                        held_id,
                        "successor-held",
                        "evolve-held",
                    )
                    free_action = action_host.evolve(
                        free_id,
                        "successor-free",
                        "evolve-free",
                        cohost_basis_by_open_object_id={
                            held_id: "cohost-successor-free-held"
                        },
                    )
                else:
                    blocked_action = getattr(action_host, action_name)(
                        held_id,
                        f"{action_name}-held",
                    )
                    free_action = getattr(action_host, action_name)(
                        free_id,
                        f"{action_name}-free",
                    )

                self.assertFalse(blocked_action.accepted)
                self.assertEqual(
                    blocked_action.refusal_code,
                    RefusalCode.HOLD_BLOCKS_TRANSITION,
                )
                self.assertEqual(action_host.get_object(held_id), before_held)
                self.assertTrue(free_action.accepted)

    def test_append_only_refusal_visibility(self) -> None:
        host = self.make_host()
        attempts = []

        def attempt(call):
            result = call()
            attempts.append(result)
            self.assertEqual(len(host.get_transition_records()), len(attempts))
            return result

        first = attempt(
            lambda: host.create_object(
                "matter-a",
                "payload-a",
                basis_ref="create-a",
            )
        )
        first_id = first.object_id or ""
        attempt(lambda: host.create_object("matter-b", "payload-b"))
        second = attempt(
            lambda: host.create_object(
                "matter-b",
                "payload-b",
                cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
            )
        )
        second_id = second.object_id or ""
        attempt(
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
        attempt(lambda: host.stand(first_id, ""))
        attempt(lambda: host.stand(first_id, "threshold-a"))
        attempt(lambda: host.finalize(first_id, "finalize-a"))
        attempt(lambda: host.create_object("matter-a", "payload-a3"))

        records = host.get_transition_records()
        self.assertIsInstance(records, tuple)
        self.assertEqual([r.record_id for r in records], [a.record_id for a in attempts])

        phase_values = {phase.value for phase in PhaseState}
        resolution_values = {resolution.value for resolution in ResolutionType}
        relation_values = {relation.value for relation in RelationType}

        for result, record in zip(attempts, records):
            self.assertEqual(result.accepted, record.accepted)
            if result.accepted:
                self.assertIsNone(result.refusal_code)
                self.assertIsNone(record.refusal_code)
            else:
                self.assertFalse(result.state_changed)
                self.assertIsNotNone(result.refusal_code)
                self.assertEqual(result.refusal_code, record.refusal_code)
                self.assertEqual(record.created_coexistence_relations, ())
                self.assertNotIn(result.refusal_code.value, phase_values)
                self.assertNotIn(result.refusal_code.value, resolution_values)
                self.assertNotIn(result.refusal_code.value, relation_values)

    def test_coexistence_relation_visibility(self) -> None:
        host = self.make_host()
        first_id = self.create_object(host, "matter-a", "payload-a")
        second = host.create_object(
            "matter-b",
            "payload-b",
            cohost_basis_by_open_object_id={first_id: "cohost-a-b"},
        )
        second_id = second.object_id or ""

        relations = host.get_coexistence_relations()
        self.assertEqual(len(relations), 1)
        relation = relations[0]
        self.assertEqual(relation.relation_type, RelationType.DISTINCT_MATTER_COHOSTED)
        self.assertEqual(relation.object_id, second_id)
        self.assertEqual(relation.related_object_id, first_id)
        self.assertEqual(relation.basis_ref, "cohost-a-b")

        record = host.get_transition_records()[-1]
        self.assertEqual(record.created_coexistence_relations, relations)
        self.assertEqual(record.created_coexistence_relations[0].object_id, second_id)
        self.assertEqual(
            record.created_coexistence_relations[0].related_object_id,
            first_id,
        )

    def test_state_access_helpers_are_inspectable_without_mutating_host(self) -> None:
        host = self.make_host()
        first_id, second_id = self.create_cohosted_pair(host)

        obj_copy = host.get_object(first_id)
        self.assertIsNotNone(obj_copy)
        obj_copy.phase_state = PhaseState.STANDING
        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.CANDIDATE)

        records = host.get_transition_records()
        relations = host.get_coexistence_relations()
        self.assertIsInstance(records, tuple)
        self.assertIsInstance(relations, tuple)
        self.assertEqual(len(records), 2)
        self.assertEqual(len(relations), 1)

        state_copy = host.get_state()
        self.assertIn(first_id, state_copy.objects)
        self.assertIn(second_id, state_copy.objects)
        state_copy.objects[first_id].phase_state = PhaseState.STANDING
        state_copy.open_object_ids = ()
        state_copy.coexistence_relations = ()

        self.assertEqual(host.get_object(first_id).phase_state, PhaseState.CANDIDATE)
        self.assertIn(first_id, host.get_state().open_object_ids)
        self.assertIn(second_id, host.get_state().open_object_ids)
        self.assertEqual(len(host.get_coexistence_relations()), 1)


if __name__ == "__main__":
    unittest.main()
