"""Bounded import surface for v0-min coexistence scenario artifacts.

This module reads one JSON artifact emitted by
``run_integrity_host_v0_min_coexistence_scenarios.py`` and reconstructs a
read-only inspection packet. It preserves scenario metadata, snapshot metadata,
host posture, objects, coexistence relations, active HOLDs, transition records,
refusal visibility, and predecessor/successor lineage.

Import here does not replay actions into a host, merge state, define
cross-host continuity, create persistence or registry doctrine, or upgrade an
artifact into local system law. The source artifact remains source material;
the imported packet is an immutable inspection view over that material.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class ImportFormatError(ValueError):
    """Raised when an artifact is not the current bounded scenario shape."""


@dataclass(frozen=True)
class ImportedActionResult:
    """Read-only copy of one scenario action result."""

    label: str
    accepted: bool
    state_changed: bool
    record_id: str
    object_id: str | None
    successor_object_id: str | None
    refusal_code: str | None


@dataclass(frozen=True)
class ImportedScenarioMetadata:
    """Read-only scenario identity and runner-facing action posture."""

    scenario_id: str
    scenario_name: str
    description: str
    generated_at: str
    source_path: str
    accepted_action_count: int
    refused_action_count: int
    action_results: tuple[ImportedActionResult, ...]


@dataclass(frozen=True)
class ImportedSnapshotMetadata:
    """Read-only snapshot metadata from the exported source artifact."""

    snapshot_type: str
    snapshot_version: str
    generated_at: str
    source_host_class: str
    source_module: str


@dataclass(frozen=True)
class ImportedHostState:
    """Read-only host identity and open-object posture."""

    host_id: str
    open_object_ids: tuple[str, ...]


@dataclass(frozen=True)
class ImportedIntegrityObject:
    """Read-only imported integrity object posture."""

    object_id: str
    matter_ref: str
    payload_ref: str
    phase_state: str
    resolution_type: str | None
    predecessor_object_id: str | None
    occurrence_ref: str | None
    created_by_record_id: str
    resolved_by_record_id: str | None


@dataclass(frozen=True)
class ImportedCoexistenceRelation:
    """Read-only imported same-host coexistence relation marker."""

    relation_type: str
    object_id: str
    related_object_id: str
    basis_ref: str
    created_by_record_id: str


@dataclass(frozen=True)
class ImportedHoldState:
    """Read-only imported target-specific HOLD posture."""

    target_object_id: str
    active: bool
    basis_ref: str
    set_by_record_id: str


@dataclass(frozen=True)
class ImportedTransitionRecord:
    """Read-only imported append-only transition record."""

    record_id: str
    host_id: str
    action_type: str
    matter_ref: str | None
    object_id: str | None
    related_open_object_ids: tuple[str, ...]
    created_coexistence_relations: tuple[ImportedCoexistenceRelation, ...]
    predecessor_object_id: str | None
    successor_object_id: str | None
    source_phase_state: str | None
    target_phase_state: str | None
    source_resolution_type: str | None
    target_resolution_type: str | None
    payload_ref: str | None
    occurrence_ref: str | None
    basis_ref: str | None
    threshold_basis_ref: str | None
    hold_before: bool
    hold_after: bool
    accepted: bool
    refusal_code: str | None
    acted_at: str


@dataclass(frozen=True)
class ImportedScenarioArtifact:
    """Read-only imported scenario packet with source and snapshot kept distinct."""

    scenario: ImportedScenarioMetadata
    snapshot_metadata: ImportedSnapshotMetadata
    host: ImportedHostState
    objects: tuple[ImportedIntegrityObject, ...]
    coexistence_relations: tuple[ImportedCoexistenceRelation, ...]
    holds: tuple[ImportedHoldState, ...]
    transition_records: tuple[ImportedTransitionRecord, ...]


def read_artifact_json(path: str | Path) -> dict[str, Any]:
    """Read and parse a UTF-8 scenario artifact as a JSON object."""

    artifact_path = Path(path)
    try:
        raw = artifact_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise ImportFormatError(f"Could not read artifact: {artifact_path}") from exc

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ImportFormatError(f"Artifact is not valid JSON: {artifact_path}") from exc

    if not isinstance(parsed, dict):
        raise ImportFormatError("artifact must be a JSON object")
    return parsed


def load_scenario_artifact(path: str | Path) -> ImportedScenarioArtifact:
    """Load one emitted scenario artifact into a read-only inspection packet."""

    artifact_path = Path(path)
    artifact = read_artifact_json(artifact_path)
    scenario = _require_section(artifact, "scenario", "artifact")
    snapshot = _require_section(artifact, "snapshot", "artifact")

    snapshot_metadata = _parse_snapshot_metadata(
        _require_section(snapshot, "metadata", "artifact.snapshot")
    )
    host = _parse_host_state(_require_section(snapshot, "host", "artifact.snapshot"))
    objects = tuple(
        _parse_integrity_object(item, f"artifact.snapshot.objects[{index}]")
        for index, item in enumerate(
            _require_list(snapshot, "objects", "artifact.snapshot")
        )
    )
    coexistence_relations = tuple(
        _parse_coexistence_relation(
            item,
            f"artifact.snapshot.coexistence_relations[{index}]",
        )
        for index, item in enumerate(
            _require_list(snapshot, "coexistence_relations", "artifact.snapshot")
        )
    )
    holds = tuple(
        _parse_hold_state(item, f"artifact.snapshot.holds[{index}]")
        for index, item in enumerate(
            _require_list(snapshot, "holds", "artifact.snapshot")
        )
    )
    transition_records = tuple(
        _parse_transition_record(
            item,
            f"artifact.snapshot.transition_records[{index}]",
        )
        for index, item in enumerate(
            _require_list(snapshot, "transition_records", "artifact.snapshot")
        )
    )

    return ImportedScenarioArtifact(
        scenario=_parse_scenario_metadata(
            scenario,
            source_path=artifact_path.resolve().as_posix(),
        ),
        snapshot_metadata=snapshot_metadata,
        host=host,
        objects=objects,
        coexistence_relations=coexistence_relations,
        holds=holds,
        transition_records=transition_records,
    )


def build_import_summary(imported_artifact: ImportedScenarioArtifact) -> dict[str, Any]:
    """Build a small inspection summary without flattening the imported packet."""

    refusal_count = sum(
        1 for record in imported_artifact.transition_records if not record.accepted
    )
    return {
        "scenario_id": imported_artifact.scenario.scenario_id,
        "scenario_name": imported_artifact.scenario.scenario_name,
        "source_path": imported_artifact.scenario.source_path,
        "snapshot_type": imported_artifact.snapshot_metadata.snapshot_type,
        "snapshot_version": imported_artifact.snapshot_metadata.snapshot_version,
        "host_id": imported_artifact.host.host_id,
        "object_count": len(imported_artifact.objects),
        "open_object_count": len(imported_artifact.host.open_object_ids),
        "coexistence_relation_count": len(imported_artifact.coexistence_relations),
        "hold_count": len(imported_artifact.holds),
        "record_count": len(imported_artifact.transition_records),
        "refusal_count": refusal_count,
        "accepted_action_count": imported_artifact.scenario.accepted_action_count,
        "refused_action_count": imported_artifact.scenario.refused_action_count,
    }


def _parse_scenario_metadata(
    value: Mapping[str, Any],
    *,
    source_path: str,
) -> ImportedScenarioMetadata:
    context = "artifact.scenario"
    action_results = tuple(
        _parse_action_result(item, f"{context}.action_results[{index}]")
        for index, item in enumerate(_require_list(value, "action_results", context))
    )
    accepted_count = _require_int(value, "accepted_action_count", context)
    refused_count = _require_int(value, "refused_action_count", context)

    observed_accepted = sum(1 for action in action_results if action.accepted)
    observed_refused = len(action_results) - observed_accepted
    if accepted_count != observed_accepted:
        raise ImportFormatError(
            f"{context}.accepted_action_count does not match action_results"
        )
    if refused_count != observed_refused:
        raise ImportFormatError(
            f"{context}.refused_action_count does not match action_results"
        )

    return ImportedScenarioMetadata(
        scenario_id=_require_string(value, "scenario_id", context),
        scenario_name=_require_string(value, "scenario_name", context),
        description=_require_string(value, "description", context),
        generated_at=_require_string(value, "generated_at", context),
        source_path=source_path,
        accepted_action_count=accepted_count,
        refused_action_count=refused_count,
        action_results=action_results,
    )


def _parse_action_result(value: Any, context: str) -> ImportedActionResult:
    mapping = _require_mapping_value(value, context)
    return ImportedActionResult(
        label=_require_string(mapping, "label", context),
        accepted=_require_bool(mapping, "accepted", context),
        state_changed=_require_bool(mapping, "state_changed", context),
        record_id=_require_string(mapping, "record_id", context),
        object_id=_require_optional_string(mapping, "object_id", context),
        successor_object_id=_require_optional_string(
            mapping,
            "successor_object_id",
            context,
        ),
        refusal_code=_require_optional_string(mapping, "refusal_code", context),
    )


def _parse_snapshot_metadata(value: Mapping[str, Any]) -> ImportedSnapshotMetadata:
    context = "artifact.snapshot.metadata"
    return ImportedSnapshotMetadata(
        snapshot_type=_require_string(value, "snapshot_type", context),
        snapshot_version=_require_string(value, "snapshot_version", context),
        generated_at=_require_string(value, "generated_at", context),
        source_host_class=_require_string(value, "source_host_class", context),
        source_module=_require_string(value, "source_module", context),
    )


def _parse_host_state(value: Mapping[str, Any]) -> ImportedHostState:
    context = "artifact.snapshot.host"
    return ImportedHostState(
        host_id=_require_string(value, "host_id", context),
        open_object_ids=_require_string_list(value, "open_object_ids", context),
    )


def _parse_integrity_object(value: Any, context: str) -> ImportedIntegrityObject:
    mapping = _require_mapping_value(value, context)
    return ImportedIntegrityObject(
        object_id=_require_string(mapping, "object_id", context),
        matter_ref=_require_string(mapping, "matter_ref", context),
        payload_ref=_require_string(mapping, "payload_ref", context),
        phase_state=_require_string(mapping, "phase_state", context),
        resolution_type=_require_optional_string(mapping, "resolution_type", context),
        predecessor_object_id=_require_optional_string(
            mapping,
            "predecessor_object_id",
            context,
        ),
        occurrence_ref=_require_optional_string(mapping, "occurrence_ref", context),
        created_by_record_id=_require_string(
            mapping,
            "created_by_record_id",
            context,
        ),
        resolved_by_record_id=_require_optional_string(
            mapping,
            "resolved_by_record_id",
            context,
        ),
    )


def _parse_coexistence_relation(
    value: Any,
    context: str,
) -> ImportedCoexistenceRelation:
    mapping = _require_mapping_value(value, context)
    return ImportedCoexistenceRelation(
        relation_type=_require_string(mapping, "relation_type", context),
        object_id=_require_string(mapping, "object_id", context),
        related_object_id=_require_string(mapping, "related_object_id", context),
        basis_ref=_require_string(mapping, "basis_ref", context),
        created_by_record_id=_require_string(
            mapping,
            "created_by_record_id",
            context,
        ),
    )


def _parse_hold_state(value: Any, context: str) -> ImportedHoldState:
    mapping = _require_mapping_value(value, context)
    return ImportedHoldState(
        target_object_id=_require_string(mapping, "target_object_id", context),
        active=_require_bool(mapping, "active", context),
        basis_ref=_require_string(mapping, "basis_ref", context),
        set_by_record_id=_require_string(mapping, "set_by_record_id", context),
    )


def _parse_transition_record(value: Any, context: str) -> ImportedTransitionRecord:
    mapping = _require_mapping_value(value, context)
    created_relations = tuple(
        _parse_coexistence_relation(
            item,
            f"{context}.created_coexistence_relations[{index}]",
        )
        for index, item in enumerate(
            _require_list(mapping, "created_coexistence_relations", context)
        )
    )

    return ImportedTransitionRecord(
        record_id=_require_string(mapping, "record_id", context),
        host_id=_require_string(mapping, "host_id", context),
        action_type=_require_string(mapping, "action_type", context),
        matter_ref=_require_optional_string(mapping, "matter_ref", context),
        object_id=_require_optional_string(mapping, "object_id", context),
        related_open_object_ids=_require_string_list(
            mapping,
            "related_open_object_ids",
            context,
        ),
        created_coexistence_relations=created_relations,
        predecessor_object_id=_require_optional_string(
            mapping,
            "predecessor_object_id",
            context,
        ),
        successor_object_id=_require_optional_string(
            mapping,
            "successor_object_id",
            context,
        ),
        source_phase_state=_require_optional_string(
            mapping,
            "source_phase_state",
            context,
        ),
        target_phase_state=_require_optional_string(
            mapping,
            "target_phase_state",
            context,
        ),
        source_resolution_type=_require_optional_string(
            mapping,
            "source_resolution_type",
            context,
        ),
        target_resolution_type=_require_optional_string(
            mapping,
            "target_resolution_type",
            context,
        ),
        payload_ref=_require_optional_string(mapping, "payload_ref", context),
        occurrence_ref=_require_optional_string(mapping, "occurrence_ref", context),
        basis_ref=_require_optional_string(mapping, "basis_ref", context),
        threshold_basis_ref=_require_optional_string(
            mapping,
            "threshold_basis_ref",
            context,
        ),
        hold_before=_require_bool(mapping, "hold_before", context),
        hold_after=_require_bool(mapping, "hold_after", context),
        accepted=_require_bool(mapping, "accepted", context),
        refusal_code=_require_optional_string(mapping, "refusal_code", context),
        acted_at=_require_string(mapping, "acted_at", context),
    )


def _require_section(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> Mapping[str, Any]:
    value = _require_key(mapping, key, context)
    return _require_mapping_value(value, f"{context}.{key}")


def _require_key(mapping: Mapping[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise ImportFormatError(f"{context}.{key} is required")
    return mapping[key]


def _require_mapping_value(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ImportFormatError(f"{context} must be an object")
    return value


def _require_list(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> list[Any]:
    value = _require_key(mapping, key, context)
    if not isinstance(value, list):
        raise ImportFormatError(f"{context}.{key} must be a list")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = _require_key(mapping, key, context)
    if not isinstance(value, str) or value == "":
        raise ImportFormatError(f"{context}.{key} must be a non-empty string")
    return value


def _require_optional_string(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> str | None:
    value = _require_key(mapping, key, context)
    if value is None:
        return None
    if not isinstance(value, str) or value == "":
        raise ImportFormatError(f"{context}.{key} must be a string or null")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = _require_key(mapping, key, context)
    if not isinstance(value, bool):
        raise ImportFormatError(f"{context}.{key} must be a boolean")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = _require_key(mapping, key, context)
    if not isinstance(value, int) or isinstance(value, bool):
        raise ImportFormatError(f"{context}.{key} must be an integer")
    return value


def _require_string_list(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> tuple[str, ...]:
    values = _require_list(mapping, key, context)
    imported: list[str] = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or value == "":
            raise ImportFormatError(
                f"{context}.{key}[{index}] must be a non-empty string"
            )
        imported.append(value)
    return tuple(imported)
