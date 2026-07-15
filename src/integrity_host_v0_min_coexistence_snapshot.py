"""Bounded JSON snapshot export for the v0-min coexistence host.

This module is an additive inspection surface for
``integrity_host_v0_min_coexistence_v2``. It reads the current in-memory host
state, converts the anti-collapse-relevant structure into JSON-serializable
primitives, and can write that snapshot to a local JSON file.

The snapshot is not protocol law, final persistence architecture, registry
doctrine, replay machinery, or a CLI surface. It exists only to make the
current bounded coexistence host inspectable without mutating the host.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Mapping

from integrity_host_v0_min_coexistence_v2 import (
    CoexistenceRelation,
    HostHoldState,
    HostState,
    IntegrityHostV0MinCoexistenceV2,
    IntegrityObject,
    TransitionRecord,
)


SNAPSHOT_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SNAPSHOT"
SNAPSHOT_VERSION = "0.1.0"


def build_snapshot(host: IntegrityHostV0MinCoexistenceV2) -> dict[str, Any]:
    """Build a JSON-serializable snapshot from the current host state.

    ``get_state()`` returns a copied host state in the current implementation,
    so this function serializes that copy and does not mutate the live host.
    """

    state = host.get_state()
    return {
        "metadata": {
            "snapshot_type": SNAPSHOT_TYPE,
            "snapshot_version": SNAPSHOT_VERSION,
            "generated_at": _utc_timestamp(),
            "source_host_class": host.__class__.__name__,
            "source_module": host.__class__.__module__,
        },
        "host": _host_to_snapshot(state),
        "objects": _objects_to_snapshot(state),
        "coexistence_relations": _relations_to_snapshot(
            state.coexistence_relations
        ),
        "holds": _holds_to_snapshot(state.holds_by_object_id),
        "transition_records": [
            _transition_record_to_snapshot(record)
            for record in state.transition_records
        ],
    }


def snapshot_to_json(snapshot: Mapping[str, Any]) -> str:
    """Return pretty, stable JSON text for a snapshot-like mapping."""

    return (
        json.dumps(_json_value(snapshot), indent=2, sort_keys=True, allow_nan=False)
        + "\n"
    )


def write_snapshot(
    host: IntegrityHostV0MinCoexistenceV2,
    output_path: str | Path,
) -> Path:
    """Build and write a UTF-8 JSON snapshot, creating parent directories."""

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(snapshot_to_json(build_snapshot(host)), encoding="utf-8")
    return path


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _enum_value(value: Enum | None) -> str | None:
    if value is None:
        return None
    return value.value


def _host_to_snapshot(state: HostState) -> dict[str, Any]:
    return {
        "host_id": state.host_id,
        "open_object_ids": list(state.open_object_ids),
    }


def _objects_to_snapshot(state: HostState) -> list[dict[str, Any]]:
    return [
        _integrity_object_to_snapshot(state.objects[object_id])
        for object_id in sorted(state.objects)
    ]


def _integrity_object_to_snapshot(obj: IntegrityObject) -> dict[str, Any]:
    return {
        "object_id": obj.object_id,
        "matter_ref": obj.matter_ref,
        "payload_ref": obj.payload_ref,
        "phase_state": _enum_value(obj.phase_state),
        "resolution_type": _enum_value(obj.resolution_type),
        "predecessor_object_id": obj.predecessor_object_id,
        "occurrence_ref": obj.occurrence_ref,
        "created_by_record_id": obj.created_by_record_id,
        "resolved_by_record_id": obj.resolved_by_record_id,
    }


def _relations_to_snapshot(
    relations: tuple[CoexistenceRelation, ...],
) -> list[dict[str, Any]]:
    return [_coexistence_relation_to_snapshot(relation) for relation in relations]


def _coexistence_relation_to_snapshot(
    relation: CoexistenceRelation,
) -> dict[str, Any]:
    return {
        "relation_type": _enum_value(relation.relation_type),
        "object_id": relation.object_id,
        "related_object_id": relation.related_object_id,
        "basis_ref": relation.basis_ref,
        "created_by_record_id": relation.created_by_record_id,
    }


def _holds_to_snapshot(
    holds_by_object_id: Mapping[str, HostHoldState],
) -> list[dict[str, Any]]:
    return [
        _hold_to_snapshot(holds_by_object_id[object_id])
        for object_id in sorted(holds_by_object_id)
    ]


def _hold_to_snapshot(hold: HostHoldState) -> dict[str, Any]:
    return {
        "target_object_id": hold.target_object_id,
        "active": hold.active,
        "basis_ref": hold.basis_ref,
        "set_by_record_id": hold.set_by_record_id,
    }


def _transition_record_to_snapshot(record: TransitionRecord) -> dict[str, Any]:
    return {
        "record_id": record.record_id,
        "host_id": record.host_id,
        "action_type": _enum_value(record.action_type),
        "matter_ref": record.matter_ref,
        "object_id": record.object_id,
        "related_open_object_ids": list(record.related_open_object_ids),
        "created_coexistence_relations": [
            _coexistence_relation_to_snapshot(relation)
            for relation in record.created_coexistence_relations
        ],
        "predecessor_object_id": record.predecessor_object_id,
        "successor_object_id": record.successor_object_id,
        "source_phase_state": _enum_value(record.source_phase_state),
        "target_phase_state": _enum_value(record.target_phase_state),
        "source_resolution_type": _enum_value(record.source_resolution_type),
        "target_resolution_type": _enum_value(record.target_resolution_type),
        "payload_ref": record.payload_ref,
        "occurrence_ref": record.occurrence_ref,
        "basis_ref": record.basis_ref,
        "threshold_basis_ref": record.threshold_basis_ref,
        "hold_before": record.hold_before,
        "hold_after": record.hold_after,
        "accepted": record.accepted,
        "refusal_code": _enum_value(record.refusal_code),
        "acted_at": record.acted_at,
    }


def _json_value(value: Any) -> Any:
    """Convert supported values to JSON primitives without implicit dataclass IO."""

    if isinstance(value, Enum):
        return value.value
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, Mapping):
        return {str(_json_value(key)): _json_value(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_value(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return sorted(_json_value(item) for item in value)
    raise TypeError(f"Unsupported snapshot value type: {type(value).__name__}")
