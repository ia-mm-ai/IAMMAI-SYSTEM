"""Bounded executable tests for the IAMMAI v0-min integrity host.

These tests lock the current in-memory proof host behavior in
``src/integrity_host_v0_min.py``. They test the hostability slice only:
phase movement, standing-only resolution, orthogonal HOLD, append-only records,
explicit refusal, one-open-object host-local simplification, and EVOLVE
lineage. They do not test persistence, runtime integration, distribution,
governance, witness families, or full IAMMAI embodiment.
"""

from __future__ import annotations

import sys
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from integrity_host_v0_min import (  # noqa: E402
    ActionType,
    IntegrityHostV0Min,
    PhaseState,
    RefusalCode,
    ResolutionType,
)


class IntegrityHostV0MinTests(unittest.TestCase):
    def make_host(self) -> IntegrityHostV0Min:
        return IntegrityHostV0Min("test-host")

    def create_candidate(self, host: IntegrityHostV0Min) -> str:
        result = host.create_object("matter-1", "payload-1", basis_ref="create-basis")
        self.assertTrue(result.accepted)
        self.assertIsNotNone(result.object_id)
        return result.object_id or ""

    def create_present(self, host: IntegrityHostV0Min) -> str:
        object_id = self.create_candidate(host)
        result = host.present(object_id, "occurrence-1", "present-basis")
        self.assertTrue(result.accepted)
        return object_id

    def create_standing(self, host: IntegrityHostV0Min) -> str:
        object_id = self.create_present(host)
        result = host.stand(object_id, "threshold-basis")
        self.assertTrue(result.accepted)
        return object_id

    def test_create_object_success(self) -> None:
        host = self.make_host()

        result = host.create_object("matter-1", "payload-1", basis_ref="create-basis")

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        self.assertIsNotNone(result.object_id)

        obj = host.get_object(result.object_id or "")
        self.assertIsNotNone(obj)
        self.assertEqual(obj.phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(obj.resolution_type)
        self.assertEqual(host.get_state().current_open_object_id, result.object_id)

        records = host.get_transition_records()
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].action_type, ActionType.CREATE_OBJECT)
        self.assertTrue(records[0].accepted)
        self.assertEqual(records[0].object_id, result.object_id)
        self.assertEqual(records[0].target_phase_state, PhaseState.CANDIDATE)

    def test_one_open_object_simplification_refuses_second_open_object(self) -> None:
        host = self.make_host()
        first_id = self.create_candidate(host)
        before = host.get_object(first_id)

        result = host.create_object("matter-2", "payload-2")

        self.assertFalse(result.accepted)
        self.assertFalse(result.state_changed)
        self.assertEqual(result.refusal_code, RefusalCode.OPEN_OBJECT_EXISTS)
        self.assertEqual(len(host.get_transition_records()), 2)

        after = host.get_object(first_id)
        self.assertEqual(after, before)
        self.assertEqual(host.get_state().current_open_object_id, first_id)

    def test_present_success_requires_occurrence_and_basis(self) -> None:
        host = self.make_host()
        object_id = self.create_candidate(host)

        result = host.present(object_id, "occurrence-1", "present-basis")

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        obj = host.get_object(object_id)
        self.assertEqual(obj.phase_state, PhaseState.PRESENT)
        self.assertEqual(obj.occurrence_ref, "occurrence-1")
        self.assertIsNone(obj.resolution_type)

        records = host.get_transition_records()
        self.assertEqual(len(records), 2)
        self.assertEqual(records[-1].action_type, ActionType.PRESENT)
        self.assertTrue(records[-1].accepted)
        self.assertEqual(records[-1].source_phase_state, PhaseState.CANDIDATE)
        self.assertEqual(records[-1].target_phase_state, PhaseState.PRESENT)
        self.assertEqual(records[-1].occurrence_ref, "occurrence-1")
        self.assertEqual(records[-1].basis_ref, "present-basis")

    def test_present_refusal_cases(self) -> None:
        host = self.make_host()
        object_id = self.create_candidate(host)
        before = host.get_object(object_id)

        missing_occurrence = host.present(object_id, "", "present-basis")
        self.assertFalse(missing_occurrence.accepted)
        self.assertEqual(
            missing_occurrence.refusal_code,
            RefusalCode.MISSING_OCCURRENCE_REF,
        )
        self.assertEqual(host.get_object(object_id), before)

        missing_basis = host.present(object_id, "occurrence-1", "")
        self.assertFalse(missing_basis.accepted)
        self.assertEqual(missing_basis.refusal_code, RefusalCode.MISSING_BASIS_REF)
        self.assertEqual(host.get_object(object_id), before)

        nonexistent = host.present("missing-object", "occurrence-1", "basis")
        self.assertFalse(nonexistent.accepted)
        self.assertEqual(nonexistent.refusal_code, RefusalCode.OBJECT_NOT_FOUND)

        accepted_present = host.present(object_id, "occurrence-1", "present-basis")
        self.assertTrue(accepted_present.accepted)

        wrong_phase = host.present(object_id, "occurrence-2", "basis-2")
        self.assertFalse(wrong_phase.accepted)
        self.assertEqual(wrong_phase.refusal_code, RefusalCode.INVALID_PHASE_FOR_ACTION)

        host.stand(object_id, "threshold-basis")
        host.finalize(object_id, "finalize-basis")
        new_result = host.create_object("matter-2", "payload-2")
        self.assertTrue(new_result.accepted)

        not_current = host.present(object_id, "occurrence-3", "basis-3")
        self.assertFalse(not_current.accepted)
        self.assertEqual(
            not_current.refusal_code,
            RefusalCode.OBJECT_NOT_CURRENT_OPEN_OBJECT,
        )

    def test_stand_success_keeps_finalization_separate(self) -> None:
        host = self.make_host()
        object_id = self.create_present(host)

        result = host.stand(object_id, "threshold-basis")

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        obj = host.get_object(object_id)
        self.assertEqual(obj.phase_state, PhaseState.STANDING)
        self.assertIsNone(obj.resolution_type)

        record = host.get_transition_records()[-1]
        self.assertEqual(record.action_type, ActionType.STAND)
        self.assertNotEqual(record.action_type, ActionType.FINALIZE)
        self.assertEqual(record.source_phase_state, PhaseState.PRESENT)
        self.assertEqual(record.target_phase_state, PhaseState.STANDING)
        self.assertEqual(record.threshold_basis_ref, "threshold-basis")
        self.assertIsNone(record.target_resolution_type)

    def test_stand_refusal_cases(self) -> None:
        host = self.make_host()
        candidate_id = self.create_candidate(host)
        before = host.get_object(candidate_id)

        direct = host.stand(candidate_id, "threshold-basis")
        self.assertFalse(direct.accepted)
        self.assertEqual(direct.refusal_code, RefusalCode.PRESENCE_REQUIRED)
        self.assertEqual(host.get_object(candidate_id), before)

        host.present(candidate_id, "occurrence-1", "present-basis")

        missing_basis = host.stand(candidate_id, "")
        self.assertFalse(missing_basis.accepted)
        self.assertEqual(
            missing_basis.refusal_code,
            RefusalCode.THRESHOLD_BASIS_MISSING,
        )

        threshold_failed = host.stand(
            candidate_id,
            "threshold-basis",
            threshold_met=False,
        )
        self.assertFalse(threshold_failed.accepted)
        self.assertEqual(threshold_failed.refusal_code, RefusalCode.THRESHOLD_NOT_MET)

        nonexistent = host.stand("missing-object", "threshold-basis")
        self.assertFalse(nonexistent.accepted)
        self.assertEqual(nonexistent.refusal_code, RefusalCode.OBJECT_NOT_FOUND)

        hold_result = host.set_hold(candidate_id, "hold-basis")
        self.assertTrue(hold_result.accepted)
        blocked = host.stand(candidate_id, "threshold-basis")
        self.assertFalse(blocked.accepted)
        self.assertEqual(blocked.refusal_code, RefusalCode.HOLD_BLOCKS_TRANSITION)

        release = host.release_hold(candidate_id, "release-basis")
        self.assertTrue(release.accepted)
        stand = host.stand(candidate_id, "threshold-basis")
        self.assertTrue(stand.accepted)
        finalize = host.finalize(candidate_id, "finalize-basis")
        self.assertTrue(finalize.accepted)
        new_candidate = host.create_object("matter-2", "payload-2")
        self.assertTrue(new_candidate.accepted)

        not_current = host.stand(candidate_id, "threshold-basis")
        self.assertFalse(not_current.accepted)
        self.assertEqual(
            not_current.refusal_code,
            RefusalCode.OBJECT_NOT_CURRENT_OPEN_OBJECT,
        )

    def test_finalize_behavior_and_refusals(self) -> None:
        host = self.make_host()
        candidate_id = self.create_candidate(host)

        finalize_candidate = host.finalize(candidate_id, "basis")
        self.assertFalse(finalize_candidate.accepted)
        self.assertEqual(finalize_candidate.refusal_code, RefusalCode.STANDING_REQUIRED)

        host.present(candidate_id, "occurrence-1", "present-basis")
        finalize_present = host.finalize(candidate_id, "basis")
        self.assertFalse(finalize_present.accepted)
        self.assertEqual(finalize_present.refusal_code, RefusalCode.STANDING_REQUIRED)

        host.stand(candidate_id, "threshold-basis")
        before_count = len(host.get_transition_records())
        result = host.finalize(candidate_id, "finalize-basis")

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        self.assertEqual(len(host.get_transition_records()), before_count + 1)

        obj = host.get_object(candidate_id)
        self.assertEqual(obj.phase_state, PhaseState.STANDING)
        self.assertEqual(obj.resolution_type, ResolutionType.FINALIZE)
        self.assertIsNotNone(obj.resolved_by_record_id)
        self.assertIsNone(host.get_state().current_open_object_id)

        record = host.get_transition_records()[-1]
        self.assertEqual(record.action_type, ActionType.FINALIZE)
        self.assertEqual(record.source_resolution_type, None)
        self.assertEqual(record.target_resolution_type, ResolutionType.FINALIZE)

        already_resolved = host.finalize(candidate_id, "again")
        self.assertFalse(already_resolved.accepted)
        self.assertEqual(already_resolved.refusal_code, RefusalCode.ALREADY_RESOLVED)

    def test_invalidate_behavior_and_refusals(self) -> None:
        host = self.make_host()
        candidate_id = self.create_candidate(host)

        invalidate_candidate = host.invalidate(candidate_id, "basis")
        self.assertFalse(invalidate_candidate.accepted)
        self.assertEqual(
            invalidate_candidate.refusal_code,
            RefusalCode.STANDING_REQUIRED,
        )

        host.present(candidate_id, "occurrence-1", "present-basis")
        invalidate_present = host.invalidate(candidate_id, "basis")
        self.assertFalse(invalidate_present.accepted)
        self.assertEqual(invalidate_present.refusal_code, RefusalCode.STANDING_REQUIRED)

        host.stand(candidate_id, "threshold-basis")
        before_count = len(host.get_transition_records())
        result = host.invalidate(candidate_id, "invalidate-basis")

        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        self.assertEqual(len(host.get_transition_records()), before_count + 1)

        obj = host.get_object(candidate_id)
        self.assertEqual(obj.phase_state, PhaseState.STANDING)
        self.assertEqual(obj.resolution_type, ResolutionType.INVALIDATE)
        self.assertIsNotNone(obj.resolved_by_record_id)
        self.assertIsNone(host.get_state().current_open_object_id)

        record = host.get_transition_records()[-1]
        self.assertEqual(record.action_type, ActionType.INVALIDATE)
        self.assertEqual(record.source_resolution_type, None)
        self.assertEqual(record.target_resolution_type, ResolutionType.INVALIDATE)

        already_resolved = host.invalidate(candidate_id, "again")
        self.assertFalse(already_resolved.accepted)
        self.assertEqual(already_resolved.refusal_code, RefusalCode.ALREADY_RESOLVED)

    def test_evolve_behavior_and_refusals(self) -> None:
        host = self.make_host()
        candidate_id = self.create_candidate(host)

        evolve_candidate = host.evolve(candidate_id, "successor-payload", "basis")
        self.assertFalse(evolve_candidate.accepted)
        self.assertEqual(evolve_candidate.refusal_code, RefusalCode.STANDING_REQUIRED)

        host.present(candidate_id, "occurrence-1", "present-basis")
        evolve_present = host.evolve(candidate_id, "successor-payload", "basis")
        self.assertFalse(evolve_present.accepted)
        self.assertEqual(evolve_present.refusal_code, RefusalCode.STANDING_REQUIRED)

        host.stand(candidate_id, "threshold-basis")
        missing_payload = host.evolve(candidate_id, "", "basis")
        self.assertFalse(missing_payload.accepted)
        self.assertEqual(missing_payload.refusal_code, RefusalCode.MISSING_PAYLOAD_REF)

        before_count = len(host.get_transition_records())
        result = host.evolve(candidate_id, "successor-payload", "evolve-basis")
        self.assertTrue(result.accepted)
        self.assertTrue(result.state_changed)
        self.assertEqual(len(host.get_transition_records()), before_count + 1)
        self.assertIsNotNone(result.successor_object_id)

        predecessor = host.get_object(candidate_id)
        successor = host.get_object(result.successor_object_id or "")
        self.assertIsNotNone(successor)

        self.assertEqual(predecessor.phase_state, PhaseState.STANDING)
        self.assertEqual(predecessor.resolution_type, ResolutionType.EVOLVE)
        self.assertIsNotNone(predecessor.resolved_by_record_id)
        self.assertEqual(successor.phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(successor.resolution_type)
        self.assertEqual(successor.predecessor_object_id, candidate_id)
        self.assertEqual(host.get_state().current_open_object_id, successor.object_id)

        record = host.get_transition_records()[-1]
        self.assertEqual(record.action_type, ActionType.EVOLVE)
        self.assertEqual(record.object_id, candidate_id)
        self.assertEqual(record.predecessor_object_id, candidate_id)
        self.assertEqual(record.successor_object_id, successor.object_id)
        self.assertEqual(record.source_phase_state, PhaseState.STANDING)
        self.assertEqual(record.target_phase_state, PhaseState.STANDING)
        self.assertIsNone(record.source_resolution_type)
        self.assertEqual(record.target_resolution_type, ResolutionType.EVOLVE)

        already_resolved = host.evolve(candidate_id, "another-payload", "again")
        self.assertFalse(already_resolved.accepted)
        self.assertEqual(already_resolved.refusal_code, RefusalCode.ALREADY_RESOLVED)

    def test_hold_orthogonality_and_release_allows_blocked_action(self) -> None:
        host = self.make_host()
        object_id = self.create_present(host)
        before = host.get_object(object_id)
        before_count = len(host.get_transition_records())

        hold = host.set_hold(object_id, "hold-basis")

        self.assertTrue(hold.accepted)
        self.assertTrue(hold.state_changed)
        self.assertEqual(len(host.get_transition_records()), before_count + 1)
        self.assertTrue(host.get_state().hold.active)
        self.assertEqual(host.get_state().hold.target_object_id, object_id)
        self.assertFalse(host.get_transition_records()[-1].hold_before)
        self.assertTrue(host.get_transition_records()[-1].hold_after)
        self.assertEqual(host.get_transition_records()[-1].basis_ref, "hold-basis")

        held_object = host.get_object(object_id)
        self.assertEqual(held_object.phase_state, before.phase_state)
        self.assertEqual(held_object.resolution_type, before.resolution_type)

        blocked = host.stand(object_id, "threshold-basis")
        self.assertFalse(blocked.accepted)
        self.assertEqual(blocked.refusal_code, RefusalCode.HOLD_BLOCKS_TRANSITION)
        self.assertEqual(host.get_object(object_id).phase_state, PhaseState.PRESENT)
        self.assertIsNone(host.get_object(object_id).resolution_type)

        release = host.release_hold(object_id, "release-basis")
        self.assertTrue(release.accepted)
        self.assertFalse(host.get_state().hold.active)
        self.assertEqual(host.get_object(object_id).phase_state, PhaseState.PRESENT)
        self.assertIsNone(host.get_object(object_id).resolution_type)
        self.assertTrue(host.get_transition_records()[-1].hold_before)
        self.assertFalse(host.get_transition_records()[-1].hold_after)
        self.assertEqual(host.get_transition_records()[-1].basis_ref, "release-basis")

        stand = host.stand(object_id, "threshold-basis")
        self.assertTrue(stand.accepted)
        self.assertEqual(host.get_object(object_id).phase_state, PhaseState.STANDING)

    def test_hold_blocks_standing_resolutions(self) -> None:
        for action_name in ("finalize", "invalidate", "evolve"):
            with self.subTest(action_name=action_name):
                host = self.make_host()
                object_id = self.create_standing(host)
                self.assertTrue(host.set_hold(object_id, "hold-basis").accepted)
                before = host.get_object(object_id)
                before_count = len(host.get_transition_records())

                if action_name == "evolve":
                    result = host.evolve(object_id, "successor-payload", "basis")
                else:
                    result = getattr(host, action_name)(object_id, "basis")

                self.assertFalse(result.accepted)
                self.assertFalse(result.state_changed)
                self.assertEqual(
                    result.refusal_code,
                    RefusalCode.HOLD_BLOCKS_TRANSITION,
                )
                self.assertEqual(len(host.get_transition_records()), before_count + 1)
                self.assertEqual(host.get_object(object_id), before)

    def test_refusal_and_append_only_trace_discipline(self) -> None:
        host = self.make_host()
        attempts = []

        result = host.create_object("matter-1", "payload-1")
        attempts.append(result)
        object_id = result.object_id or ""

        for call in (
            lambda: host.create_object("matter-2", "payload-2"),
            lambda: host.present(object_id, "", "basis"),
            lambda: host.present(object_id, "occurrence-1", "basis"),
            lambda: host.stand(object_id, "", True),
            lambda: host.stand(object_id, "threshold-basis", False),
            lambda: host.stand(object_id, "threshold-basis", True),
            lambda: host.finalize(object_id, "finalize-basis"),
            lambda: host.invalidate(object_id, "again"),
        ):
            attempts.append(call())
            self.assertEqual(len(host.get_transition_records()), len(attempts))

        records = host.get_transition_records()
        self.assertEqual(len(records), len(attempts))
        self.assertIsInstance(records, tuple)
        self.assertEqual([r.record_id for r in records], [a.record_id for a in attempts])

        for result, record in zip(attempts, records):
            self.assertEqual(result.accepted, record.accepted)
            if result.accepted:
                self.assertIsNone(result.refusal_code)
                self.assertIsNone(record.refusal_code)
            else:
                self.assertFalse(result.state_changed)
                self.assertIsNotNone(result.refusal_code)
                self.assertEqual(result.refusal_code, record.refusal_code)
                self.assertNotIn(result.refusal_code.value, {p.value for p in PhaseState})
                self.assertNotIn(
                    result.refusal_code.value,
                    {r.value for r in ResolutionType},
                )

    def test_transition_record_visibility(self) -> None:
        host = self.make_host()
        predecessor_id = self.create_standing(host)
        result = host.evolve(predecessor_id, "successor-payload", "evolve-basis")
        self.assertTrue(result.accepted)

        evolve_record = host.get_transition_records()[-1]
        self.assertEqual(evolve_record.action_type, ActionType.EVOLVE)
        self.assertEqual(evolve_record.object_id, predecessor_id)
        self.assertEqual(evolve_record.predecessor_object_id, predecessor_id)
        self.assertEqual(evolve_record.successor_object_id, result.successor_object_id)
        self.assertEqual(evolve_record.source_phase_state, PhaseState.STANDING)
        self.assertEqual(evolve_record.target_phase_state, PhaseState.STANDING)
        self.assertIsNone(evolve_record.source_resolution_type)
        self.assertEqual(evolve_record.target_resolution_type, ResolutionType.EVOLVE)
        self.assertEqual(evolve_record.occurrence_ref, "occurrence-1")
        self.assertEqual(evolve_record.basis_ref, "evolve-basis")
        self.assertFalse(evolve_record.hold_before)
        self.assertFalse(evolve_record.hold_after)
        self.assertTrue(evolve_record.accepted)
        self.assertIsNone(evolve_record.refusal_code)
        self.assertIsInstance(evolve_record.acted_at, str)
        self.assertTrue(evolve_record.acted_at)

        successor_id = result.successor_object_id or ""
        refused = host.stand(successor_id, "")
        self.assertFalse(refused.accepted)
        refusal_record = host.get_transition_records()[-1]
        self.assertEqual(refusal_record.action_type, ActionType.STAND)
        self.assertEqual(refusal_record.object_id, successor_id)
        self.assertEqual(refusal_record.source_phase_state, PhaseState.CANDIDATE)
        self.assertEqual(refusal_record.target_phase_state, PhaseState.CANDIDATE)
        self.assertIsNone(refusal_record.source_resolution_type)
        self.assertIsNone(refusal_record.target_resolution_type)
        self.assertFalse(refusal_record.accepted)
        self.assertEqual(refusal_record.refusal_code, RefusalCode.PRESENCE_REQUIRED)
        self.assertIsInstance(refusal_record.acted_at, str)
        self.assertTrue(refusal_record.acted_at)

        host.present(successor_id, "occurrence-2", "present-basis-2")
        host.stand(successor_id, "threshold-basis-2")
        stand_record = host.get_transition_records()[-1]
        self.assertEqual(stand_record.threshold_basis_ref, "threshold-basis-2")
        self.assertEqual(stand_record.source_phase_state, PhaseState.PRESENT)
        self.assertEqual(stand_record.target_phase_state, PhaseState.STANDING)

    def test_state_access_helpers_are_inspectable_and_do_not_mutate_host(self) -> None:
        host = self.make_host()
        object_id = self.create_candidate(host)

        obj_copy = host.get_object(object_id)
        self.assertIsNotNone(obj_copy)
        obj_copy.phase_state = PhaseState.STANDING
        self.assertEqual(host.get_object(object_id).phase_state, PhaseState.CANDIDATE)

        state_copy = host.get_state()
        self.assertIn(object_id, state_copy.objects)
        state_copy.objects[object_id].phase_state = PhaseState.STANDING
        state_copy.current_open_object_id = None
        self.assertEqual(host.get_object(object_id).phase_state, PhaseState.CANDIDATE)
        self.assertEqual(host.get_state().current_open_object_id, object_id)

        records = host.get_transition_records()
        self.assertIsInstance(records, tuple)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0].action_type, ActionType.CREATE_OBJECT)


if __name__ == "__main__":
    unittest.main()
