"""V2 successor host for bounded same-host coexistence.

This module is a narrow successor to
``src/integrity_host_v0_min_coexistence.py``. It preserves the first
same-host coexistence host where that line already aligns with
``spec/INTEGRITY_RELATION_V0_MIN_SPEC.md`` and closes one remaining seam:
fresh same-matter creation after preserved standing resolution by FINALIZE or
INVALIDATE is refused unless the request follows an already lawful path.

The host remains an in-memory proof implementation only. It is not a full
relation engine, persistence layer, registry, distributed host, product module,
or minimum lawful IAMMAI system.

The preserved proof seam remains:

    CANDIDATE -> PRESENT -> STANDING

STAND remains distinct from FINALIZE. FINALIZE, INVALIDATE, and EVOLVE remain
standing-only resolutions. EVOLVE remains the only accepted same-matter
successor path in this slice. HOLD remains target-specific orthogonal
permissibility. Every attempted action appends one transition record, including
explicit refusals.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Collection, Dict, Mapping, Optional, Tuple
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
    """Closed public action family for the coexistence proof host."""

    CREATE_OBJECT = "CREATE_OBJECT"
    PRESENT = "PRESENT"
    STAND = "STAND"
    FINALIZE = "FINALIZE"
    INVALIDATE = "INVALIDATE"
    EVOLVE = "EVOLVE"
    SET_HOLD = "SET_HOLD"
    RELEASE_HOLD = "RELEASE_HOLD"


class RelationType(str, Enum):
    """Closed local relation marker family for this successor slice."""

    DISTINCT_MATTER_COHOSTED = "DISTINCT_MATTER_COHOSTED"


class RefusalCode(str, Enum):
    """Closed local refusal family for v0-min coexistence v2 results."""

    MISSING_MATTER_REF = "MISSING_MATTER_REF"
    MISSING_PAYLOAD_REF = "MISSING_PAYLOAD_REF"
    MISSING_OCCURRENCE_REF = "MISSING_OCCURRENCE_REF"
    MISSING_BASIS_REF = "MISSING_BASIS_REF"
    THRESHOLD_BASIS_MISSING = "THRESHOLD_BASIS_MISSING"
    THRESHOLD_NOT_MET = "THRESHOLD_NOT_MET"
    PRESENCE_REQUIRED = "PRESENCE_REQUIRED"
    STANDING_REQUIRED = "STANDING_REQUIRED"
    OBJECT_NOT_FOUND = "OBJECT_NOT_FOUND"
    OBJECT_NOT_OPEN = "OBJECT_NOT_OPEN"
    INVALID_PHASE_FOR_ACTION = "INVALID_PHASE_FOR_ACTION"
    ALREADY_RESOLVED = "ALREADY_RESOLVED"
    UNRESOLVED_COHOST_RELATION_REQUIRED = "UNRESOLVED_COHOST_RELATION_REQUIRED"
    MISSING_COHOST_RELATION_BASIS = "MISSING_COHOST_RELATION_BASIS"
    SAME_MATTER_UNRESOLVED_COHOST_REFUSED = (
        "SAME_MATTER_UNRESOLVED_COHOST_REFUSED"
    )
    SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED = (
        "SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED"
    )
    OVERLAPPING_MATTER_UNRESOLVED_COHOST_REFUSED = (
        "OVERLAPPING_MATTER_UNRESOLVED_COHOST_REFUSED"
    )
    RELATION_TARGET_NOT_OPEN = "RELATION_TARGET_NOT_OPEN"
    HOLD_BLOCKS_TRANSITION = "HOLD_BLOCKS_TRANSITION"
    DUPLICATE_HOLD_ON_TARGET = "DUPLICATE_HOLD_ON_TARGET"
    HOLD_NOT_ACTIVE = "HOLD_NOT_ACTIVE"
    APPEND_ONLY_PRESERVATION_REQUIRED = "APPEND_ONLY_PRESERVATION_REQUIRED"
    RESOLUTION_FAMILY_CLOSED = "RESOLUTION_FAMILY_CLOSED"
    LINEAGE_RELATION_REQUIRED = "LINEAGE_RELATION_REQUIRED"


@dataclass
class IntegrityObject:
    """Matter-bound object governed by the local successor host."""

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
    """Target-specific orthogonal HOLD posture."""

    active: bool
    target_object_id: str
    basis_ref: str
    set_by_record_id: str


@dataclass(frozen=True)
class CoexistenceRelation:
    """Pairwise host-local marker for distinct-matter unresolved coexistence."""

    relation_type: RelationType
    object_id: str
    related_object_id: str
    basis_ref: str
    created_by_record_id: str


@dataclass(frozen=True)
class TransitionRecord:
    """Append-only record of an accepted or refused host action."""

    record_id: str
    host_id: str
    action_type: ActionType
    matter_ref: Optional[str]
    object_id: Optional[str]
    related_open_object_ids: Tuple[str, ...]
    created_coexistence_relations: Tuple[CoexistenceRelation, ...]
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
    """In-memory state for one local coexistence proof host."""

    host_id: str
    open_object_ids: Tuple[str, ...] = ()
    objects: Dict[str, IntegrityObject] = field(default_factory=dict)
    transition_records: Tuple[TransitionRecord, ...] = ()
    coexistence_relations: Tuple[CoexistenceRelation, ...] = ()
    holds_by_object_id: Dict[str, HostHoldState] = field(default_factory=dict)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def _clean_ref(value: Optional[str]) -> Optional[str]:
    if not isinstance(value, str):
        return None
    cleaned = value.strip()
    return cleaned if cleaned else None


class IntegrityHostV0MinCoexistenceV2:
    """Bounded same-host coexistence successor with post-resolution refusal.

    Distinct-matter unresolved coexistence is a host-local proof extension. It
    is not global IAMMAI relation law. Fresh same-matter creation after a
    preserved FINALIZE or INVALIDATE is refused because that broader episode
    path is not defined in this slice.
    """

    def __init__(self, host_id: Optional[str] = None) -> None:
        self._state = HostState(host_id=_clean_ref(host_id) or _new_id("host"))

    def create_object(
        self,
        matter_ref: Optional[str],
        payload_ref: Optional[str],
        basis_ref: Optional[str] = None,
        *,
        cohost_basis_by_open_object_id: Optional[Mapping[str, str]] = None,
        overlapping_open_object_ids: Optional[Collection[str]] = None,
    ) -> ConformanceResult:
        matter_ref = _clean_ref(matter_ref)
        payload_ref = _clean_ref(payload_ref)
        basis_ref = _clean_ref(basis_ref)

        if matter_ref is None:
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.MISSING_MATTER_REF,
                payload_ref=payload_ref,
                basis_ref=basis_ref,
            )
        if payload_ref is None:
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.MISSING_PAYLOAD_REF,
                matter_ref=matter_ref,
                basis_ref=basis_ref,
            )

        same_matter_blockers = self._same_matter_post_resolution_blockers(
            matter_ref
        )
        if same_matter_blockers:
            return self._refuse(
                ActionType.CREATE_OBJECT,
                RefusalCode.SAME_MATTER_POST_RESOLUTION_PATH_NOT_DEFINED,
                matter_ref=matter_ref,
                related_open_object_ids=same_matter_blockers,
                payload_ref=payload_ref,
                basis_ref=basis_ref,
            )

        coexistence_check = self._check_unresolved_coexistence(
            ActionType.CREATE_OBJECT,
            matter_ref,
            cohost_basis_by_open_object_id,
            overlapping_open_object_ids,
            basis_ref=basis_ref,
            payload_ref=payload_ref,
        )
        refusal, related_open_ids, relation_basis_by_open_id = coexistence_check
        if refusal is not None:
            return refusal

        record_id = _new_id("tr")
        object_id = _new_id("obj")
        relations = self._build_coexistence_relations(
            object_id, relation_basis_by_open_id, record_id
        )
        record = self._record(
            record_id=record_id,
            action_type=ActionType.CREATE_OBJECT,
            matter_ref=matter_ref,
            object_id=object_id,
            related_open_object_ids=related_open_ids,
            created_coexistence_relations=relations,
            target_phase_state=PhaseState.CANDIDATE,
            payload_ref=payload_ref,
            basis_ref=basis_ref,
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
        self._add_open_object(object_id)
        self._append_relations(relations)
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

        if obj is None:
            return self._refuse(ActionType.PRESENT, RefusalCode.OBJECT_NOT_FOUND)
        if obj.resolution_type is not None:
            return self._refuse_for_object(
                ActionType.PRESENT, RefusalCode.ALREADY_RESOLVED, obj
            )
        if not self._is_open_object_id(object_id):
            return self._refuse_for_object(
                ActionType.PRESENT, RefusalCode.OBJECT_NOT_OPEN, obj
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
            hold_before=self._hold_active(obj.object_id),
            hold_after=self._hold_active(obj.object_id),
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

        if obj is None:
            return self._refuse(ActionType.STAND, RefusalCode.OBJECT_NOT_FOUND)
        if obj.resolution_type is not None:
            return self._refuse_for_object(
                ActionType.STAND, RefusalCode.ALREADY_RESOLVED, obj
            )
        if not self._is_open_object_id(object_id):
            return self._refuse_for_object(
                ActionType.STAND, RefusalCode.OBJECT_NOT_OPEN, obj
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
        if self._hold_active(obj.object_id):
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
            hold_before=False,
            hold_after=False,
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
        *,
        cohost_basis_by_open_object_id: Optional[Mapping[str, str]] = None,
        overlapping_open_object_ids: Optional[Collection[str]] = None,
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

        coexistence_check = self._check_unresolved_coexistence(
            ActionType.EVOLVE,
            predecessor.matter_ref,
            cohost_basis_by_open_object_id,
            overlapping_open_object_ids,
            excluded_open_object_id=predecessor.object_id,
            object_id=predecessor.object_id,
            predecessor_object_id=predecessor.object_id,
            basis_ref=basis_ref,
            payload_ref=successor_payload_ref,
            source_phase_state=predecessor.phase_state,
            target_phase_state=predecessor.phase_state,
            source_resolution_type=predecessor.resolution_type,
            target_resolution_type=predecessor.resolution_type,
        )
        refusal, related_open_ids, relation_basis_by_open_id = coexistence_check
        if refusal is not None:
            return refusal

        record_id = _new_id("tr")
        successor_object_id = _new_id("obj")
        source_resolution = predecessor.resolution_type
        relations = self._build_coexistence_relations(
            successor_object_id, relation_basis_by_open_id, record_id
        )

        predecessor.resolution_type = ResolutionType.EVOLVE
        predecessor.resolved_by_record_id = record_id
        self._remove_open_object(predecessor.object_id)

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
        self._add_open_object(successor_object_id)
        self._append_relations(relations)

        record = self._record(
            record_id=record_id,
            action_type=ActionType.EVOLVE,
            matter_ref=predecessor.matter_ref,
            object_id=predecessor.object_id,
            related_open_object_ids=related_open_ids,
            created_coexistence_relations=relations,
            predecessor_object_id=predecessor.object_id,
            successor_object_id=successor_object_id,
            source_phase_state=PhaseState.STANDING,
            target_phase_state=PhaseState.STANDING,
            source_resolution_type=source_resolution,
            target_resolution_type=predecessor.resolution_type,
            payload_ref=successor_payload_ref,
            occurrence_ref=predecessor.occurrence_ref,
            basis_ref=basis_ref,
            hold_before=False,
            hold_after=False,
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
        if object_id in self._state.holds_by_object_id:
            return self._refuse_for_object(
                ActionType.SET_HOLD,
                RefusalCode.DUPLICATE_HOLD_ON_TARGET,
                obj,
                basis_ref=basis_ref,
            )
        if basis_ref is None:
            return self._refuse_for_object(
                ActionType.SET_HOLD, RefusalCode.MISSING_BASIS_REF, obj
            )

        record_id = _new_id("tr")
        self._state.holds_by_object_id[object_id] = HostHoldState(
            active=True,
            target_object_id=object_id,
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
            hold_before=False,
            hold_after=True,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def release_hold(
        self, object_id: str, basis_ref: Optional[str]
    ) -> ConformanceResult:
        basis_ref = _clean_ref(basis_ref)
        obj = self._state.objects.get(object_id)

        if obj is None:
            return self._refuse(
                ActionType.RELEASE_HOLD,
                RefusalCode.OBJECT_NOT_FOUND,
                object_id=object_id,
                basis_ref=basis_ref,
            )
        if object_id not in self._state.holds_by_object_id:
            return self._refuse_for_object(
                ActionType.RELEASE_HOLD,
                RefusalCode.HOLD_NOT_ACTIVE,
                obj,
                basis_ref=basis_ref,
            )
        if basis_ref is None:
            return self._refuse_for_object(
                ActionType.RELEASE_HOLD, RefusalCode.MISSING_BASIS_REF, obj
            )

        del self._state.holds_by_object_id[object_id]
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
            hold_before=True,
            hold_after=False,
            accepted=True,
        )
        self._append_record(record)
        return self._result(record, object_id=obj.object_id, state_changed=True)

    def get_object(self, object_id: str) -> Optional[IntegrityObject]:
        obj = self._state.objects.get(object_id)
        return deepcopy(obj) if obj is not None else None

    def get_transition_records(self) -> Tuple[TransitionRecord, ...]:
        return self._state.transition_records

    def get_coexistence_relations(self) -> Tuple[CoexistenceRelation, ...]:
        return self._state.coexistence_relations

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
        self._remove_open_object(obj.object_id)

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
            hold_before=False,
            hold_after=False,
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
        if not self._is_open_object_id(object_id):
            return self._refuse_for_object(
                action_type, RefusalCode.OBJECT_NOT_OPEN, obj, basis_ref=basis_ref
            )
        if basis_ref is None:
            return self._refuse_for_object(
                action_type, RefusalCode.MISSING_BASIS_REF, obj
            )
        if self._hold_active(object_id):
            return self._refuse_for_object(
                action_type,
                RefusalCode.HOLD_BLOCKS_TRANSITION,
                obj,
                basis_ref=basis_ref,
            )
        return None

    def _check_unresolved_coexistence(
        self,
        action_type: ActionType,
        matter_ref: str,
        cohost_basis_by_open_object_id: Optional[Mapping[str, str]],
        overlapping_open_object_ids: Optional[Collection[str]],
        *,
        excluded_open_object_id: Optional[str] = None,
        object_id: Optional[str] = None,
        predecessor_object_id: Optional[str] = None,
        basis_ref: Optional[str] = None,
        payload_ref: Optional[str] = None,
        source_phase_state: Optional[PhaseState] = None,
        target_phase_state: Optional[PhaseState] = None,
        source_resolution_type: Optional[ResolutionType] = None,
        target_resolution_type: Optional[ResolutionType] = None,
    ) -> Tuple[Optional[ConformanceResult], Tuple[str, ...], Dict[str, str]]:
        open_ids = tuple(
            open_id
            for open_id in self._state.open_object_ids
            if open_id != excluded_open_object_id and self._is_open_object_id(open_id)
        )
        basis_by_open_id = self._clean_basis_mapping(cohost_basis_by_open_object_id)

        same_matter_open_ids = tuple(
            open_id
            for open_id in open_ids
            if self._state.objects[open_id].matter_ref == matter_ref
        )
        if same_matter_open_ids:
            return (
                self._refuse(
                    action_type,
                    RefusalCode.SAME_MATTER_UNRESOLVED_COHOST_REFUSED,
                    matter_ref=matter_ref,
                    object_id=object_id,
                    related_open_object_ids=same_matter_open_ids,
                    predecessor_object_id=predecessor_object_id,
                    source_phase_state=source_phase_state,
                    target_phase_state=target_phase_state,
                    source_resolution_type=source_resolution_type,
                    target_resolution_type=target_resolution_type,
                    payload_ref=payload_ref,
                    basis_ref=basis_ref,
                ),
                open_ids,
                {},
            )

        overlap_ids = self._clean_id_set(overlapping_open_object_ids)
        overlap_open_ids = tuple(
            open_id for open_id in open_ids if open_id in overlap_ids
        )
        if overlap_open_ids:
            return (
                self._refuse(
                    action_type,
                    RefusalCode.OVERLAPPING_MATTER_UNRESOLVED_COHOST_REFUSED,
                    matter_ref=matter_ref,
                    object_id=object_id,
                    related_open_object_ids=overlap_open_ids,
                    predecessor_object_id=predecessor_object_id,
                    source_phase_state=source_phase_state,
                    target_phase_state=target_phase_state,
                    source_resolution_type=source_resolution_type,
                    target_resolution_type=target_resolution_type,
                    payload_ref=payload_ref,
                    basis_ref=basis_ref,
                ),
                open_ids,
                {},
            )

        if not open_ids:
            if basis_by_open_id:
                return (
                    self._refuse(
                        action_type,
                        RefusalCode.RELATION_TARGET_NOT_OPEN,
                        matter_ref=matter_ref,
                        object_id=object_id,
                        related_open_object_ids=tuple(basis_by_open_id.keys()),
                        predecessor_object_id=predecessor_object_id,
                        source_phase_state=source_phase_state,
                        target_phase_state=target_phase_state,
                        source_resolution_type=source_resolution_type,
                        target_resolution_type=target_resolution_type,
                        payload_ref=payload_ref,
                        basis_ref=basis_ref,
                    ),
                    open_ids,
                    {},
                )
            return None, (), {}

        if cohost_basis_by_open_object_id is None:
            return (
                self._refuse(
                    action_type,
                    RefusalCode.UNRESOLVED_COHOST_RELATION_REQUIRED,
                    matter_ref=matter_ref,
                    object_id=object_id,
                    related_open_object_ids=open_ids,
                    predecessor_object_id=predecessor_object_id,
                    source_phase_state=source_phase_state,
                    target_phase_state=target_phase_state,
                    source_resolution_type=source_resolution_type,
                    target_resolution_type=target_resolution_type,
                    payload_ref=payload_ref,
                    basis_ref=basis_ref,
                ),
                open_ids,
                {},
            )

        extra_relation_targets = tuple(
            relation_target
            for relation_target in basis_by_open_id
            if relation_target not in open_ids
        )
        if extra_relation_targets:
            return (
                self._refuse(
                    action_type,
                    RefusalCode.RELATION_TARGET_NOT_OPEN,
                    matter_ref=matter_ref,
                    object_id=object_id,
                    related_open_object_ids=extra_relation_targets,
                    predecessor_object_id=predecessor_object_id,
                    source_phase_state=source_phase_state,
                    target_phase_state=target_phase_state,
                    source_resolution_type=source_resolution_type,
                    target_resolution_type=target_resolution_type,
                    payload_ref=payload_ref,
                    basis_ref=basis_ref,
                ),
                open_ids,
                {},
            )

        missing_basis_ids = tuple(
            open_id for open_id in open_ids if basis_by_open_id.get(open_id) is None
        )
        if missing_basis_ids:
            return (
                self._refuse(
                    action_type,
                    RefusalCode.MISSING_COHOST_RELATION_BASIS,
                    matter_ref=matter_ref,
                    object_id=object_id,
                    related_open_object_ids=missing_basis_ids,
                    predecessor_object_id=predecessor_object_id,
                    source_phase_state=source_phase_state,
                    target_phase_state=target_phase_state,
                    source_resolution_type=source_resolution_type,
                    target_resolution_type=target_resolution_type,
                    payload_ref=payload_ref,
                    basis_ref=basis_ref,
                ),
                open_ids,
                {},
            )

        return (
            None,
            open_ids,
            {open_id: basis_by_open_id[open_id] or "" for open_id in open_ids},
        )

    def _build_coexistence_relations(
        self,
        object_id: str,
        relation_basis_by_open_id: Mapping[str, str],
        record_id: str,
    ) -> Tuple[CoexistenceRelation, ...]:
        return tuple(
            CoexistenceRelation(
                relation_type=RelationType.DISTINCT_MATTER_COHOSTED,
                object_id=object_id,
                related_object_id=related_object_id,
                basis_ref=basis_ref,
                created_by_record_id=record_id,
            )
            for related_object_id, basis_ref in relation_basis_by_open_id.items()
        )

    def _clean_basis_mapping(
        self, basis_by_open_object_id: Optional[Mapping[str, str]]
    ) -> Dict[str, Optional[str]]:
        if basis_by_open_object_id is None:
            return {}
        cleaned: Dict[str, Optional[str]] = {}
        for raw_object_id, raw_basis in basis_by_open_object_id.items():
            object_id = _clean_ref(raw_object_id)
            if object_id is not None:
                cleaned[object_id] = _clean_ref(raw_basis)
        return cleaned

    def _clean_id_set(
        self, object_ids: Optional[Collection[str]]
    ) -> Tuple[str, ...]:
        if object_ids is None:
            return ()
        cleaned = []
        for raw_object_id in object_ids:
            object_id = _clean_ref(raw_object_id)
            if object_id is not None and object_id not in cleaned:
                cleaned.append(object_id)
        return tuple(cleaned)

    def _same_matter_post_resolution_blockers(
        self, matter_ref: str
    ) -> Tuple[str, ...]:
        return tuple(
            obj.object_id
            for obj in self._state.objects.values()
            if obj.matter_ref == matter_ref
            and obj.phase_state is PhaseState.STANDING
            and obj.resolution_type in (
                ResolutionType.FINALIZE,
                ResolutionType.INVALIDATE,
            )
        )

    def _is_unresolved_object(self, obj: IntegrityObject) -> bool:
        return obj.resolution_type is None

    def _is_unresolved_standing(self, obj: IntegrityObject) -> bool:
        return obj.phase_state is PhaseState.STANDING and obj.resolution_type is None

    def _is_resolved_standing(self, obj: IntegrityObject) -> bool:
        return obj.phase_state is PhaseState.STANDING and obj.resolution_type is not None

    def _is_open_object_id(self, object_id: str) -> bool:
        obj = self._state.objects.get(object_id)
        return (
            obj is not None
            and object_id in self._state.open_object_ids
            and self._is_unresolved_object(obj)
        )

    def _hold_active(self, object_id: str) -> bool:
        hold = self._state.holds_by_object_id.get(object_id)
        return hold is not None and hold.active

    def _add_open_object(self, object_id: str) -> None:
        if object_id not in self._state.open_object_ids:
            self._state.open_object_ids = self._state.open_object_ids + (object_id,)

    def _remove_open_object(self, object_id: str) -> None:
        self._state.open_object_ids = tuple(
            open_id for open_id in self._state.open_object_ids if open_id != object_id
        )

    def _append_relations(
        self, relations: Tuple[CoexistenceRelation, ...]
    ) -> None:
        if relations:
            self._state.coexistence_relations = (
                self._state.coexistence_relations + relations
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
        related_open_object_ids: Tuple[str, ...] = (),
        basis_ref: Optional[str] = None,
        threshold_basis_ref: Optional[str] = None,
        occurrence_ref: Optional[str] = None,
    ) -> ConformanceResult:
        return self._refuse(
            action_type,
            refusal_code,
            matter_ref=obj.matter_ref,
            object_id=obj.object_id,
            related_open_object_ids=related_open_object_ids,
            predecessor_object_id=obj.predecessor_object_id,
            source_phase_state=obj.phase_state,
            target_phase_state=obj.phase_state,
            source_resolution_type=obj.resolution_type,
            target_resolution_type=obj.resolution_type,
            payload_ref=obj.payload_ref,
            occurrence_ref=(
                occurrence_ref if occurrence_ref is not None else obj.occurrence_ref
            ),
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
        related_open_object_ids: Tuple[str, ...] = (),
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
        hold_before = self._hold_active(object_id) if object_id is not None else False
        record = self._record(
            record_id=_new_id("tr"),
            action_type=action_type,
            matter_ref=matter_ref,
            object_id=object_id,
            related_open_object_ids=related_open_object_ids,
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
            hold_after=hold_before,
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
        related_open_object_ids: Tuple[str, ...] = (),
        created_coexistence_relations: Tuple[CoexistenceRelation, ...] = (),
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
            related_open_object_ids=related_open_object_ids,
            created_coexistence_relations=created_coexistence_relations,
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
