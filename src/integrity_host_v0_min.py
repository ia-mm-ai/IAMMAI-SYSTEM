"""Bounded in-memory integrity host for the IAMMAI v0-min proof-slice.

This module implements only the local hostability slice described by
``spec/INTEGRITY_HOST_V0_MIN_SPEC.md``. It is not a constitutional rewrite,
runtime architecture, persistence layer, registry design, CLI, or product
surface.

The host preserves the proof-slice seam:

    CANDIDATE -> PRESENT -> STANDING

Standing entry is performed only by STAND. FINALIZE, INVALIDATE, and EVOLVE
are standing-only resolutions. HOLD is an orthogonal permissibility control,
not a phase and not a resolution. Every attempted action appends exactly one
transition record, including explicit refusals.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Dict, Optional, Tuple
from uuid import uuid4


class PhaseState(str, Enum):
    """Host-local compressed phase states for the proof-slice."""

    CANDIDATE = "CANDIDATE"
    PRESENT = "PRESENT"
    STANDING = "STANDING"


class ResolutionType(str, Enum):
    """Closed standing-resolution family for the proof-slice."""

    FINALIZE = "FINALIZE"
    INVALIDATE = "INVALIDATE"
    EVOLVE = "EVOLVE"


class ActionType(str, Enum):
    """Closed public action family for the v0-min proof host."""

    CREATE_OBJECT = "CREATE_OBJECT"
    PRESENT = "PRESENT"
    STAND = "STAND"
    FINALIZE = "FINALIZE"
    INVALIDATE = "INVALIDATE"
    EVOLVE = "EVOLVE"
    SET_HOLD = "SET_HOLD"
    RELEASE_HOLD = "RELEASE_HOLD"


class RefusalCode(str, Enum):
    """Closed local refusal family for v0-min conformance results."""

    OPEN_OBJECT_EXISTS = "OPEN_OBJECT_EXISTS"
    MISSING_MATTER_REF = "MISSING_MATTER_REF"
    MISSING_PAYLOAD_REF = "MISSING_PAYLOAD_REF"
    MISSING_OCCURRENCE_REF = "MISSING_OCCURRENCE_REF"
    MISSING_BASIS_REF = "MISSING_BASIS_REF"
    THRESHOLD_BASIS_MISSING = "THRESHOLD_BASIS_MISSING"
    THRESHOLD_NOT_MET = "THRESHOLD_NOT_MET"
    PRESENCE_REQUIRED = "PRESENCE_REQUIRED"
    STANDING_REQUIRED = "STANDING_REQUIRED"
    HOLD_BLOCKS_TRANSITION = "HOLD_BLOCKS_TRANSITION"
    ALREADY_RESOLVED = "ALREADY_RESOLVED"
    APPEND_ONLY_PRESERVATION_REQUIRED = "APPEND_ONLY_PRESERVATION_REQUIRED"
    RESOLUTION_FAMILY_CLOSED = "RESOLUTION_FAMILY_CLOSED"
    LINEAGE_RELATION_REQUIRED = "LINEAGE_RELATION_REQUIRED"
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    OBJECT_NOT_CURRENT_OPEN_OBJECT = "OBJECT_NOT_CURRENT_OPEN_OBJECT"
    INVALID_PHASE_FOR_ACTION = "INVALID_PHASE_FOR_ACTION"
    HOLD_ALREADY_ACTIVE = "HOLD_ALREADY_ACTIVE"
    HOLD_NOT_ACTIVE = "HOLD_NOT_ACTIVE"
    HOLD_TARGET_MISMATCH = "HOLD_TARGET_MISMATCH"


@dataclass
class IntegrityObject:
    """Matter-bound object governed by the local proof host."""

    object_id: str
    matter_ref: str
    payload_ref: str
    phase_state: PhaseState
    resolution_type: Optional[ResolutionType]
    predecessor_object_id: Optional[str]
    occurrence_ref: Optional[str]
    created_by_record_id: str
    resolved_by_record_id: Optional[str] = None


@dataclass
class HostHoldState:
    """Orthogonal HOLD posture for one local host."""

    active: bool = False
    target_object_id: Optional[str] = None
    basis_ref: Optional[str] = None
    set_by_record_id: Optional[str] = None


@dataclass(frozen=True)
class TransitionRecord:
    """Append-only record of an accepted or refused host action."""

    record_id: str
    host_id: str
    action_type: ActionType
    matter_ref: Optional[str]
    object_id: Optional[str]
    predecessor_object_id: Optional[str]
    successor_object_id: Optional[str]
    source_phase_state: Optional[PhaseState]
    target_phase_state: Optional[PhaseState]
    source_resolution_type: Optional[ResolutionType]
    target_resolution_type: Optional[ResolutionType]
    payload_ref: Optional[str]
    occurrence_ref: Optional[str]
    basis_ref: Optional[str]
    threshold_basis_ref: Optional[str]
    hold_before: bool
    hold_after: bool
    accepted: bool
    refusal_code: Optional[RefusalCode]
    acted_at: str


@dataclass(frozen=True)
class ConformanceResult:
    """Immediate result returned for every attempted host action."""

    accepted: bool
    record_id: str
    object_id: Optional[str]
    successor_object_id: Optional[str]
    refusal_code: Optional[RefusalCode]
    state_changed: bool


@dataclass
class HostState:
    """In-memory state for one local proof host."""

    host_id: str
    current_open_object_id: Optional[str] = None
    objects: Dict[str, IntegrityObject] = field(default_factory=dict)
    transition_records: Tuple[TransitionRecord, ...] = ()
    hold: HostHoldState = field(default_factory=HostHoldState)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def _clean_ref(value: Optional[str]) -> Optional[str]:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned if cleaned else None


class IntegrityHostV0Min:
    """Smallest bounded in-memory host for one integrity-kernel proof-slice.

    The one-open-object rule is a host-local proof simplification. It is not
    global IAMMAI system law.
    """

    def __init__(self, host_id: Optional[str] = None) -> None:
        self._state = HostState(host_id=_clean_ref(host_id) or _new_id("host"))

    def create_object(
        self,
        matter_ref: Optional[str],
        payload_ref: Optional[str],
        basis_ref: Optional[str] = None,
    ) -> ConformanceResult:
        matter_ref = _clean_ref(matter_ref)
        payload_ref = _clean_ref(payload_ref)
        basis_ref = _clean_ref(basis_ref)

        if matter_ref is None:
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.MISSING_MATTER_REF,
                matter_ref=None,
                payload_ref=payload_ref,
                basis_ref=basis_ref,
            )
        if payload_ref is None:
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.MISSING_PAYLOAD_REF,
                matter_ref=matter_ref,
                payload_ref=None,
                basis_ref=basis_ref,
            )
        if self._has_unresolved_open_object():
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.OPEN_OBJECT_EXISTS,
                matter_ref=matter_ref,
                object_id=self._state.current_open_object_id,
                payload_ref=payload_ref,
                basis_ref=basis_ref,
            )

        record_id = _new_id("tr")
        object_id = _new_id("obj")
        record = self._record(
            record_id=record_id,
            action_type=ActionType.CREATE_OBJECT,
            matter_ref=matter_ref,
            object_id=object_id,
            target_phase_state=PhaseState.CANDIDATE,
            payload_ref=payload_ref,
            basis_ref=basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._state.objects[object_id] = IntegrityObject(
            object_id=object_id,
            matter_ref=matter_ref,
            payload_ref=payload_ref,
            phase_state=PhaseState.CANDIDATE,
            resolution_type=None,
            predecessor_object_id=None,
            occurrence_ref=None,
            created_by_record_id=record_id,
        )
        self._state.current_open_object_id = object_id
        self._append_record(record)
        return self._result(record, object_id=object_id, state_changed=True)

    def present(
        self,
        object_id: str,
        occurrence_ref: Optional[str],
        basis_ref: Optional[str],
    ) -> ConformanceResult:
        occurrence_ref = _clean_ref(occurrence_ref)
        basis_ref = _clean_ref(basis_ref)
        obj = self._state.objects.get(object_id)

        refusal = self._require_existing_current_object(
            ActionType.PRESENT, object_id
        )
        if refusal is not None:
            return refusal
        assert obj is not None

        if obj.resolution_type is not None:
            return self._refuse_for_object(
                ActionType.PRESENT, RefusalCode.ALREADY_RESOLVED, obj
            )
        if obj.phase_state is not PhaseState.CANDIDATE:
            return self._refuse_for_object(
                ActionType.PRESENT, RefusalCode.INVALID_PHASE_FOR_ACTION, obj
            )
        if occurrence_ref is None:
            return self._refuse_for_object(
                ActionType.PRESENT,
                RefusalCode.MISSING_OCCURRENCE_REF,
                obj,
                basis_ref=basis_ref,
            )
        if basis_ref is None:
            return self._refuse_for_object(
                ActionType.PRESENT,
                RefusalCode.MISSING_BASIS_REF,
                obj,
                occurrence_ref=occurrence_ref,
            )

        source_phase = obj.phase_state
        source_resolution = obj.resolution_type
        obj.phase_state = PhaseState.PRESENT
        obj.occurrence_ref = occurrence_ref
        record = self._record(
            record_id=_new_id("tr"),
            action_type=ActionType.PRESENT,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            source_phase_state=source_phase,
            target_phase_state=obj.phase_state,
            source_resolution_type=source_resolution,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=occurrence_ref,
            basis_ref=basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def stand(
        self,
        object_id: str,
        threshold_basis_ref: Optional[str],
        threshold_met: bool = True,
    ) -> ConformanceResult:
        threshold_basis_ref = _clean_ref(threshold_basis_ref)
        obj = self._state.objects.get(object_id)

        refusal = self._require_existing_current_object(ActionType.STAND, object_id)
        if refusal is not None:
            return refusal
        assert obj is not None

        if obj.resolution_type is not None:
            return self._refuse_for_object(
                ActionType.STAND, RefusalCode.ALREADY_RESOLVED, obj
            )
        if obj.phase_state is PhaseState.CANDIDATE:
            return self._refuse_for_object(
                ActionType.STAND,
                RefusalCode.PRESENCE_REQUIRED,
                obj,
                threshold_basis_ref=threshold_basis_ref,
            )
        if obj.phase_state is not PhaseState.PRESENT:
            return self._refuse_for_object(
                ActionType.STAND,
                RefusalCode.INVALID_PHASE_FOR_ACTION,
                obj,
                threshold_basis_ref=threshold_basis_ref,
            )
        if threshold_basis_ref is None:
            return self._refuse_for_object(
                ActionType.STAND, RefusalCode.THRESHOLD_BASIS_MISSING, obj
            )
        if not threshold_met:
            return self._refuse_for_object(
                ActionType.STAND,
                RefusalCode.THRESHOLD_NOT_MET,
                obj,
                threshold_basis_ref=threshold_basis_ref,
            )
        if self._hold_blocks(obj.object_id):
            return self._refuse_for_object(
                ActionType.STAND,
                RefusalCode.HOLD_BLOCKS_TRANSITION,
                obj,
                threshold_basis_ref=threshold_basis_ref,
            )

        source_phase = obj.phase_state
        source_resolution = obj.resolution_type
        obj.phase_state = PhaseState.STANDING
        record = self._record(
            record_id=_new_id("tr"),
            action_type=ActionType.STAND,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            source_phase_state=source_phase,
            target_phase_state=obj.phase_state,
            source_resolution_type=source_resolution,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=obj.occurrence_ref,
            threshold_basis_ref=threshold_basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def finalize(
        self, object_id: str, basis_ref: Optional[str]
    ) -> ConformanceResult:
        return self._resolve(object_id, ResolutionType.FINALIZE, basis_ref)

    def invalidate(
        self, object_id: str, basis_ref: Optional[str]
    ) -> ConformanceResult:
        return self._resolve(object_id, ResolutionType.INVALIDATE, basis_ref)

    def evolve(
        self,
        predecessor_object_id: str,
        successor_payload_ref: Optional[str],
        basis_ref: Optional[str],
    ) -> ConformanceResult:
        basis_ref = _clean_ref(basis_ref)
        successor_payload_ref = _clean_ref(successor_payload_ref)
        predecessor = self._state.objects.get(predecessor_object_id)

        refusal = self._require_resolvable_standing(
            ActionType.EVOLVE, predecessor_object_id, basis_ref=basis_ref
        )
        if refusal is not None:
            return refusal
        assert predecessor is not None

        if successor_payload_ref is None:
            return self._refuse_for_object(
                ActionType.EVOLVE,
                RefusalCode.MISSING_PAYLOAD_REF,
                predecessor,
                basis_ref=basis_ref,
            )

        record_id = _new_id("tr")
        successor_object_id = _new_id("obj")
        source_resolution = predecessor.resolution_type
        predecessor.resolution_type = ResolutionType.EVOLVE
        predecessor.resolved_by_record_id = record_id

        successor = IntegrityObject(
            object_id=successor_object_id,
            matter_ref=predecessor.matter_ref,
            payload_ref=successor_payload_ref,
            phase_state=PhaseState.CANDIDATE,
            resolution_type=None,
            predecessor_object_id=predecessor.object_id,
            occurrence_ref=None,
            created_by_record_id=record_id,
        )

        self._state.objects[successor_object_id] = successor
        self._state.current_open_object_id = successor_object_id
        record = self._record(
            record_id=record_id,
            action_type=ActionType.EVOLVE,
            matter_ref=predecessor.matter_ref,
            object_id=predecessor.object_id,
            predecessor_object_id=predecessor.object_id,
            successor_object_id=successor_object_id,
            source_phase_state=PhaseState.STANDING,
            target_phase_state=PhaseState.STANDING,
            source_resolution_type=source_resolution,
            target_resolution_type=predecessor.resolution_type,
            payload_ref=successor_payload_ref,
            occurrence_ref=predecessor.occurrence_ref,
            basis_ref=basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(
            record,
            object_id=predecessor.object_id,
            successor_object_id=successor_object_id,
            state_changed=True,
        )

    def set_hold(self, object_id: str, basis_ref: Optional[str]) -> ConformanceResult:
        basis_ref = _clean_ref(basis_ref)
        obj = self._state.objects.get(object_id)
        if obj is None:
            return self._refuse(
                ActionType.SET_HOLD,
                RefusalCode.OBJECT_NOT_FOUND,
                object_id=object_id,
                basis_ref=basis_ref,
            )
        if self._state.hold.active:
            return self._refuse_for_object(
                ActionType.SET_HOLD,
                RefusalCode.HOLD_ALREADY_ACTIVE,
                obj,
                basis_ref=basis_ref,
            )
        if basis_ref is None:
            return self._refuse_for_object(
                ActionType.SET_HOLD, RefusalCode.MISSING_BASIS_REF, obj
            )

        record_id = _new_id("tr")
        hold_before = self._state.hold.active
        self._state.hold = HostHoldState(
            active=True,
            target_object_id=obj.object_id,
            basis_ref=basis_ref,
            set_by_record_id=record_id,
        )
        record = self._record(
            record_id=record_id,
            action_type=ActionType.SET_HOLD,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            source_phase_state=obj.phase_state,
            target_phase_state=obj.phase_state,
            source_resolution_type=obj.resolution_type,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=obj.occurrence_ref,
            basis_ref=basis_ref,
            hold_before=hold_before,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def release_hold(
        self, object_id: str, basis_ref: Optional[str]
    ) -> ConformanceResult:
        basis_ref = _clean_ref(basis_ref)
        if not self._state.hold.active:
            return self._refuse(
                ActionType.RELEASE_HOLD,
                RefusalCode.HOLD_NOT_ACTIVE,
                object_id=object_id,
                basis_ref=basis_ref,
            )
        if self._state.hold.target_object_id != object_id:
            held_obj = self._state.objects.get(self._state.hold.target_object_id or "")
            return self._refuse(
                ActionType.RELEASE_HOLD,
                RefusalCode.HOLD_TARGET_MISMATCH,
                matter_ref=held_obj.matter_ref if held_obj else None,
                object_id=object_id,
                basis_ref=basis_ref,
                source_phase_state=held_obj.phase_state if held_obj else None,
                target_phase_state=held_obj.phase_state if held_obj else None,
                source_resolution_type=held_obj.resolution_type if held_obj else None,
                target_resolution_type=held_obj.resolution_type if held_obj else None,
            )
        obj = self._state.objects.get(object_id)
        if obj is None:
            return self._refuse(
                ActionType.RELEASE_HOLD,
                RefusalCode.OBJECT_NOT_FOUND,
                object_id=object_id,
                basis_ref=basis_ref,
            )
        if basis_ref is None:
            return self._refuse_for_object(
                ActionType.RELEASE_HOLD, RefusalCode.MISSING_BASIS_REF, obj
            )

        hold_before = self._state.hold.active
        self._state.hold = HostHoldState()
        record = self._record(
            record_id=_new_id("tr"),
            action_type=ActionType.RELEASE_HOLD,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            source_phase_state=obj.phase_state,
            target_phase_state=obj.phase_state,
            source_resolution_type=obj.resolution_type,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=obj.occurrence_ref,
            basis_ref=basis_ref,
            hold_before=hold_before,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def get_object(self, object_id: str) -> Optional[IntegrityObject]:
        obj = self._state.objects.get(object_id)
        return deepcopy(obj) if obj is not None else None

    def get_transition_records(self) -> Tuple[TransitionRecord, ...]:
        return self._state.transition_records

    def get_state(self) -> HostState:
        return deepcopy(self._state)

    def _resolve(
        self,
        object_id: str,
        resolution_type: ResolutionType,
        basis_ref: Optional[str],
    ) -> ConformanceResult:
        basis_ref = _clean_ref(basis_ref)
        action_type_by_resolution = {
            ResolutionType.FINALIZE: ActionType.FINALIZE,
            ResolutionType.INVALIDATE: ActionType.INVALIDATE,
            ResolutionType.EVOLVE: ActionType.EVOLVE,
        }
        action_type = action_type_by_resolution.get(resolution_type)
        if action_type is None:
            return self._refuse(
                ActionType.FINALIZE,
                RefusalCode.RESOLUTION_FAMILY_CLOSED,
                object_id=object_id,
                basis_ref=basis_ref,
            )

        refusal = self._require_resolvable_standing(
            action_type, object_id, basis_ref=basis_ref
        )
        if refusal is not None:
            return refusal

        obj = self._state.objects[object_id]
        record_id = _new_id("tr")
        source_resolution = obj.resolution_type
        obj.resolution_type = resolution_type
        obj.resolved_by_record_id = record_id
        if self._state.current_open_object_id == obj.object_id:
            self._state.current_open_object_id = None

        record = self._record(
            record_id=record_id,
            action_type=action_type,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            source_phase_state=PhaseState.STANDING,
            target_phase_state=PhaseState.STANDING,
            source_resolution_type=source_resolution,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=obj.occurrence_ref,
            basis_ref=basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def _require_resolvable_standing(
        self,
        action_type: ActionType,
        object_id: str,
        basis_ref: Optional[str],
    ) -> Optional[ConformanceResult]:
        obj = self._state.objects.get(object_id)
        if obj is None:
            return self._refuse(
                action_type,
                RefusalCode.OBJECT_NOT_FOUND,
                object_id=object_id,
                basis_ref=basis_ref,
            )
        if obj.resolution_type is not None:
            return self._refuse_for_object(
                action_type, RefusalCode.ALREADY_RESOLVED, obj, basis_ref=basis_ref
            )
        if obj.phase_state is not PhaseState.STANDING:
            return self._refuse_for_object(
                action_type, RefusalCode.STANDING_REQUIRED, obj, basis_ref=basis_ref
            )
        if basis_ref is None:
            return self._refuse_for_object(
                action_type, RefusalCode.MISSING_BASIS_REF, obj
            )
        if self._hold_blocks(obj.object_id):
            return self._refuse_for_object(
                action_type,
                RefusalCode.HOLD_BLOCKS_TRANSITION,
                obj,
                basis_ref=basis_ref,
            )
        return None

    def _require_existing_current_object(
        self, action_type: ActionType, object_id: str
    ) -> Optional[ConformanceResult]:
        obj = self._state.objects.get(object_id)
        if obj is None:
            return self._refuse(
                action_type, RefusalCode.OBJECT_NOT_FOUND, object_id=object_id
            )
        if self._state.current_open_object_id != object_id:
            return self._refuse_for_object(
                action_type, RefusalCode.OBJECT_NOT_CURRENT_OPEN_OBJECT, obj
            )
        return None

    def _has_unresolved_open_object(self) -> bool:
        open_id = self._state.current_open_object_id
        if open_id is None:
            return False
        obj = self._state.objects.get(open_id)
        return obj is not None and obj.resolution_type is None

    def _hold_blocks(self, object_id: str) -> bool:
        return (
            self._state.hold.active
            and self._state.hold.target_object_id == object_id
        )

    def _append_record(self, record: TransitionRecord) -> None:
        before_count = len(self._state.transition_records)
        self._state.transition_records = self._state.transition_records + (record,)
        after_count = len(self._state.transition_records)
        if after_count != before_count + 1:
            raise RuntimeError(RefusalCode.APPEND_ONLY_PRESERVATION_REQUIRED.value)

    def _refuse_for_object(
        self,
        action_type: ActionType,
        refusal_code: RefusalCode,
        obj: IntegrityObject,
        *,
        basis_ref: Optional[str] = None,
        threshold_basis_ref: Optional[str] = None,
        occurrence_ref: Optional[str] = None,
    ) -> ConformanceResult:
        return self._refuse(
            action_type,
            refusal_code,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            predecessor_object_id=obj.predecessor_object_id,
            source_phase_state=obj.phase_state,
            target_phase_state=obj.phase_state,
            source_resolution_type=obj.resolution_type,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=occurrence_ref if occurrence_ref is not None else obj.occurrence_ref,
            basis_ref=basis_ref,
            threshold_basis_ref=threshold_basis_ref,
        )

    def _refuse(
        self,
        action_type: ActionType,
        refusal_code: RefusalCode,
        *,
        matter_ref: Optional[str] = None,
        object_id: Optional[str] = None,
        predecessor_object_id: Optional[str] = None,
        successor_object_id: Optional[str] = None,
        source_phase_state: Optional[PhaseState] = None,
        target_phase_state: Optional[PhaseState] = None,
        source_resolution_type: Optional[ResolutionType] = None,
        target_resolution_type: Optional[ResolutionType] = None,
        payload_ref: Optional[str] = None,
        occurrence_ref: Optional[str] = None,
        basis_ref: Optional[str] = None,
        threshold_basis_ref: Optional[str] = None,
    ) -> ConformanceResult:
        record = self._record(
            record_id=_new_id("tr"),
            action_type=action_type,
            matter_ref=matter_ref,
            object_id=object_id,
            predecessor_object_id=predecessor_object_id,
            successor_object_id=successor_object_id,
            source_phase_state=source_phase_state,
            target_phase_state=target_phase_state,
            source_resolution_type=source_resolution_type,
            target_resolution_type=target_resolution_type,
            payload_ref=payload_ref,
            occurrence_ref=occurrence_ref,
            basis_ref=basis_ref,
            threshold_basis_ref=threshold_basis_ref,
            hold_before=self._state.hold.active,
            hold_after=self._state.hold.active,
            accepted=False,
            refusal_code=refusal_code,
        )
        self._append_record(record)
        return self._result(
            record,
            object_id=object_id,
            successor_object_id=successor_object_id,
            state_changed=False,
        )

    def _record(
        self,
        *,
        record_id: str,
        action_type: ActionType,
        matter_ref: Optional[str],
        object_id: Optional[str] = None,
        predecessor_object_id: Optional[str] = None,
        successor_object_id: Optional[str] = None,
        source_phase_state: Optional[PhaseState] = None,
        target_phase_state: Optional[PhaseState] = None,
        source_resolution_type: Optional[ResolutionType] = None,
        target_resolution_type: Optional[ResolutionType] = None,
        payload_ref: Optional[str] = None,
        occurrence_ref: Optional[str] = None,
        basis_ref: Optional[str] = None,
        threshold_basis_ref: Optional[str] = None,
        hold_before: bool = False,
        hold_after: bool = False,
        accepted: bool = False,
        refusal_code: Optional[RefusalCode] = None,
    ) -> TransitionRecord:
        return TransitionRecord(
            record_id=record_id,
            host_id=self._state.host_id,
            action_type=action_type,
            matter_ref=matter_ref,
            object_id=object_id,
            predecessor_object_id=predecessor_object_id,
            successor_object_id=successor_object_id,
            source_phase_state=source_phase_state,
            target_phase_state=target_phase_state,
            source_resolution_type=source_resolution_type,
            target_resolution_type=target_resolution_type,
            payload_ref=payload_ref,
            occurrence_ref=occurrence_ref,
            basis_ref=basis_ref,
            threshold_basis_ref=threshold_basis_ref,
            hold_before=hold_before,
            hold_after=hold_after,
            accepted=accepted,
            refusal_code=refusal_code,
            acted_at=_utc_timestamp(),
        )

    @staticmethod
    def _result(
        record: TransitionRecord,
        *,
        object_id: Optional[str],
        state_changed: bool,
        successor_object_id: Optional[str] = None,
    ) -> ConformanceResult:
        return ConformanceResult(
            accepted=record.accepted,
            record_id=record.record_id,
            object_id=object_id,
            successor_object_id=successor_object_id,
            refusal_code=record.refusal_code,
            state_changed=state_changed,
        )
