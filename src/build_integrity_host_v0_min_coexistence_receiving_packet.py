"""Bounded receiving packet builder for v0-min coexistence artifacts.

This module builds one local receiving-side packet from one source scenario
artifact by loading that artifact through
``integrity_host_v0_min_coexistence_import``. The resulting packet is an
additive inspection artifact only.

Packet creation does not replay actions into a live host, merge imported state,
define persistence or registry law, complete continuity, or upgrade imported
material into local standing. Source remains source, imported packet remains an
imported inspection view, and the receiving packet remains a local receiving
artifact.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from integrity_host_v0_min_coexistence_import import (
    ImportFormatError,
    ImportedActionResult,
    ImportedCoexistenceRelation,
    ImportedHoldState,
    ImportedIntegrityObject,
    ImportedScenarioArtifact,
    ImportedTransitionRecord,
    build_import_summary,
    load_scenario_artifact,
)


OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_receiving_packets")
PACKET_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_RECEIVING_PACKET"
PACKET_VERSION = "0.1.0"


def build_receiving_packet(source_artifact_path: Path | str) -> dict[str, Any]:
    """Build one receiving-side packet from one source scenario artifact."""

    source_path = _resolve_source_path(source_artifact_path)
    if not source_path.exists():
        raise RuntimeError(f"Source artifact is missing: {_display_path(source_path)}")
    if not source_path.is_file():
        raise RuntimeError(f"Source artifact is not a file: {_display_path(source_path)}")

    try:
        imported = load_scenario_artifact(source_path)
    except ImportFormatError as exc:
        raise RuntimeError(
            f"Source artifact failed import validation: {_display_path(source_path)}"
        ) from exc

    _validate_imported_packet(imported)
    import_summary = build_import_summary(imported)

    return {
        "packet_metadata": {
            "packet_type": PACKET_TYPE,
            "packet_version": PACKET_VERSION,
            "generated_at": _utc_timestamp(),
            "builder_module": __name__,
        },
        "source_provenance": {
            "source_artifact_path": _display_path(source_path),
            "source_run_directory_path": _display_path(source_path.parent),
            "scenario_id": imported.scenario.scenario_id,
            "scenario_name": imported.scenario.scenario_name,
            "scenario_description": imported.scenario.description,
            "source_generated_at": imported.scenario.generated_at,
        },
        "import_identity": {
            "imported_scenario_id": imported.scenario.scenario_id,
            "imported_scenario_name": imported.scenario.scenario_name,
            "import_source_path": imported.scenario.source_path,
            "snapshot_type": imported.snapshot_metadata.snapshot_type,
            "snapshot_version": imported.snapshot_metadata.snapshot_version,
            "source_host_class": imported.snapshot_metadata.source_host_class,
            "source_module": imported.snapshot_metadata.source_module,
        },
        "receiving_status": _receiving_status(),
        "import_summary": import_summary,
        "imported_packet": _imported_packet_to_dict(imported),
    }


def write_receiving_packet(
    source_artifact_path: Path | str,
    output_path: Path | str | None = None,
) -> Path:
    """Build and write one UTF-8 JSON receiving packet without overwriting."""

    source_path = _resolve_source_path(source_artifact_path)
    packet = build_receiving_packet(source_path)
    target_path = (
        _default_output_path(source_path)
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )

    target_path.parent.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        raise RuntimeError(
            f"Refusing to overwrite receiving packet: {_display_path(target_path)}"
        )

    target_path.write_text(_json_text(packet), encoding="utf-8")
    return target_path


def build_receiving_packet_summary(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one receiving packet."""

    source = _require_mapping(packet, "source_provenance", "packet")
    summary = _require_mapping(packet, "import_summary", "packet")
    status = _require_mapping(packet, "receiving_status", "packet")

    return {
        "scenario_id": _require_string(source, "scenario_id", "source_provenance"),
        "scenario_name": _require_string(
            source,
            "scenario_name",
            "source_provenance",
        ),
        "source_artifact_path": _require_string(
            source,
            "source_artifact_path",
            "source_provenance",
        ),
        "host_id": _require_string(summary, "host_id", "import_summary"),
        "object_count": _require_int(summary, "object_count", "import_summary"),
        "open_object_count": _require_int(
            summary,
            "open_object_count",
            "import_summary",
        ),
        "coexistence_relation_count": _require_int(
            summary,
            "coexistence_relation_count",
            "import_summary",
        ),
        "hold_count": _require_int(summary, "hold_count", "import_summary"),
        "transition_record_count": _require_int(
            summary,
            "record_count",
            "import_summary",
        ),
        "refusal_count": _require_int(summary, "refusal_count", "import_summary"),
        "accepted_action_count": _require_int(
            summary,
            "accepted_action_count",
            "import_summary",
        ),
        "refused_action_count": _require_int(
            summary,
            "refused_action_count",
            "import_summary",
        ),
        "receiving_status": {
            "receiving_packet_exists": _require_bool(
                status,
                "receiving_packet_exists",
                "receiving_status",
            ),
            "imported_packet_read_only_here": _require_bool(
                status,
                "imported_packet_read_only_here",
                "receiving_status",
            ),
            "source_remains_source": _require_bool(
                status,
                "source_remains_source",
                "receiving_status",
            ),
            "replayed_into_live_host": _require_bool(
                status,
                "replayed_into_live_host",
                "receiving_status",
            ),
            "merged_into_local_state": _require_bool(
                status,
                "merged_into_local_state",
                "receiving_status",
            ),
            "continuity_completed": _require_bool(
                status,
                "continuity_completed",
                "receiving_status",
            ),
            "standing_upgraded": _require_bool(
                status,
                "standing_upgraded",
                "receiving_status",
            ),
            "preserved_structure_visible": _require_bool(
                status,
                "preserved_structure_visible",
                "receiving_status",
            ),
        },
    }


def _receiving_status() -> dict[str, bool]:
    return {
        "receiving_packet_exists": True,
        "imported_packet_read_only_here": True,
        "source_remains_source": True,
        "replayed_into_live_host": False,
        "merged_into_local_state": False,
        "continuity_completed": False,
        "standing_upgraded": False,
        "preserved_structure_visible": True,
    }


def _imported_packet_to_dict(imported: ImportedScenarioArtifact) -> dict[str, Any]:
    return {
        "scenario_metadata": _scenario_metadata_to_dict(imported),
        "snapshot_metadata": {
            "snapshot_type": imported.snapshot_metadata.snapshot_type,
            "snapshot_version": imported.snapshot_metadata.snapshot_version,
            "generated_at": imported.snapshot_metadata.generated_at,
            "source_host_class": imported.snapshot_metadata.source_host_class,
            "source_module": imported.snapshot_metadata.source_module,
        },
        "host_state": {
            "host_id": imported.host.host_id,
            "open_object_ids": list(imported.host.open_object_ids),
        },
        "objects": [_object_to_dict(obj) for obj in imported.objects],
        "coexistence_relations": [
            _coexistence_relation_to_dict(relation)
            for relation in imported.coexistence_relations
        ],
        "holds": [_hold_to_dict(hold) for hold in imported.holds],
        "transition_records": [
            _transition_record_to_dict(record)
            for record in imported.transition_records
        ],
    }


def _scenario_metadata_to_dict(imported: ImportedScenarioArtifact) -> dict[str, Any]:
    return {
        "scenario_id": imported.scenario.scenario_id,
        "scenario_name": imported.scenario.scenario_name,
        "description": imported.scenario.description,
        "generated_at": imported.scenario.generated_at,
        "source_path": imported.scenario.source_path,
        "accepted_action_count": imported.scenario.accepted_action_count,
        "refused_action_count": imported.scenario.refused_action_count,
        "action_results": [
            _action_result_to_dict(action)
            for action in imported.scenario.action_results
        ],
    }


def _action_result_to_dict(action: ImportedActionResult) -> dict[str, Any]:
    return {
        "label": action.label,
        "accepted": action.accepted,
        "state_changed": action.state_changed,
        "record_id": action.record_id,
        "object_id": action.object_id,
        "successor_object_id": action.successor_object_id,
        "refusal_code": action.refusal_code,
    }


def _object_to_dict(obj: ImportedIntegrityObject) -> dict[str, Any]:
    return {
        "object_id": obj.object_id,
        "matter_ref": obj.matter_ref,
        "payload_ref": obj.payload_ref,
        "phase_state": obj.phase_state,
        "resolution_type": obj.resolution_type,
        "predecessor_object_id": obj.predecessor_object_id,
        "occurrence_ref": obj.occurrence_ref,
        "created_by_record_id": obj.created_by_record_id,
        "resolved_by_record_id": obj.resolved_by_record_id,
    }


def _coexistence_relation_to_dict(
    relation: ImportedCoexistenceRelation,
) -> dict[str, Any]:
    return {
        "relation_type": relation.relation_type,
        "object_id": relation.object_id,
        "related_object_id": relation.related_object_id,
        "basis_ref": relation.basis_ref,
        "created_by_record_id": relation.created_by_record_id,
    }


def _hold_to_dict(hold: ImportedHoldState) -> dict[str, Any]:
    return {
        "target_object_id": hold.target_object_id,
        "active": hold.active,
        "basis_ref": hold.basis_ref,
        "set_by_record_id": hold.set_by_record_id,
    }


def _transition_record_to_dict(record: ImportedTransitionRecord) -> dict[str, Any]:
    return {
        "record_id": record.record_id,
        "host_id": record.host_id,
        "action_type": record.action_type,
        "matter_ref": record.matter_ref,
        "object_id": record.object_id,
        "related_open_object_ids": list(record.related_open_object_ids),
        "created_coexistence_relations": [
            _coexistence_relation_to_dict(relation)
            for relation in record.created_coexistence_relations
        ],
        "predecessor_object_id": record.predecessor_object_id,
        "successor_object_id": record.successor_object_id,
        "source_phase_state": record.source_phase_state,
        "target_phase_state": record.target_phase_state,
        "source_resolution_type": record.source_resolution_type,
        "target_resolution_type": record.target_resolution_type,
        "payload_ref": record.payload_ref,
        "occurrence_ref": record.occurrence_ref,
        "basis_ref": record.basis_ref,
        "threshold_basis_ref": record.threshold_basis_ref,
        "hold_before": record.hold_before,
        "hold_after": record.hold_after,
        "accepted": record.accepted,
        "refusal_code": record.refusal_code,
        "acted_at": record.acted_at,
    }


def _validate_imported_packet(imported: ImportedScenarioArtifact) -> None:
    _require_non_empty(imported.scenario.scenario_id, "imported scenario id")
    _require_non_empty(imported.scenario.scenario_name, "imported scenario name")
    _require_non_empty(imported.scenario.description, "imported scenario description")
    _require_non_empty(imported.scenario.generated_at, "imported scenario timestamp")
    _require_non_empty(imported.scenario.source_path, "imported source path")
    _require_non_empty(imported.snapshot_metadata.snapshot_type, "snapshot type")
    _require_non_empty(imported.snapshot_metadata.snapshot_version, "snapshot version")
    _require_non_empty(imported.snapshot_metadata.source_host_class, "source host class")
    _require_non_empty(imported.snapshot_metadata.source_module, "source module")
    _require_non_empty(imported.host.host_id, "host id")

    action_count = len(imported.scenario.action_results)
    expected_count = (
        imported.scenario.accepted_action_count
        + imported.scenario.refused_action_count
    )
    if action_count != expected_count:
        raise RuntimeError("Imported action counts do not match action_results")


def _require_non_empty(value: str, label: str) -> None:
    if not isinstance(value, str) or value == "":
        raise RuntimeError(f"Imported packet is missing {label}")


def _default_output_path(source_path: Path) -> Path:
    return _repo_root() / OUTPUT_ROOT / f"{source_path.stem}__receiving_packet.json"


def _resolve_source_path(path: Path | str) -> Path:
    source_path = Path(path)
    if source_path.is_absolute():
        return source_path.resolve()

    cwd_candidate = source_path.resolve()
    if cwd_candidate.exists():
        return cwd_candidate

    return (_repo_root() / source_path).resolve()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_relative_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return _repo_root() / path


def _display_path(path: Path) -> str:
    resolved = Path(path).resolve()
    root = _repo_root()
    try:
        return resolved.relative_to(root).as_posix()
    except ValueError:
        return resolved.as_posix()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(payload, indent=2, sort_keys=True, allow_nan=False) + "\n"


def _require_mapping(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> Mapping[str, Any]:
    value = _require_key(mapping, key, context)
    if not isinstance(value, Mapping):
        raise RuntimeError(f"Malformed {context}: {key} must be an object")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = _require_key(mapping, key, context)
    if not isinstance(value, str) or value == "":
        raise RuntimeError(f"Malformed {context}: {key} must be a non-empty string")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = _require_key(mapping, key, context)
    if not isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be boolean")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = _require_key(mapping, key, context)
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be an integer")
    return value


def _require_key(mapping: Mapping[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise RuntimeError(f"Malformed {context}: missing {key}")
    return mapping[key]
