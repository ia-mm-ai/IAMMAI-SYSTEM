"""Bounded validator for v0-min coexistence receiving packets.

This module validates one receiving packet produced by
``build_integrity_host_v0_min_coexistence_receiving_packet.py``. It checks
packet shape, source/import identity, receiving-side non-replay posture,
summary-to-imported-packet count coherence, and visibility of load-bearing
objects, coexistence relations, HOLDs, refusal records, and lineage.

Validation here is an additive receiving-side ingress surface only. It does
not replay imported actions into a live host, merge state, define persistence
or registry law, complete continuity, or upgrade imported material into local
standing.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from build_integrity_host_v0_min_coexistence_receiving_packet import (
    PACKET_TYPE,
    PACKET_VERSION,
    build_receiving_packet_summary,
)


VALIDATION_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_RECEIVING_PACKET_VALIDATION"
VALIDATION_VERSION = "0.1.0"

TOP_LEVEL_SECTIONS = (
    "packet_metadata",
    "source_provenance",
    "import_identity",
    "receiving_status",
    "import_summary",
    "imported_packet",
)

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

SUMMARY_COUNT_KEYS = {
    "object_count": "object_count",
    "open_object_count": "open_object_count",
    "coexistence_relation_count": "coexistence_relation_count",
    "hold_count": "hold_count",
    "transition_record_count": "record_count",
    "refusal_count": "refusal_count",
    "accepted_action_count": "accepted_action_count",
    "refused_action_count": "refused_action_count",
}

DERIVED_ONLY_COUNT_KEYS = (
    "resolved_object_count",
    "successor_object_count",
    "evolve_record_count",
)


class ReceivingPacketValidationError(ValueError):
    """Raised when a receiving packet cannot be read or validated at all."""


def read_receiving_packet_json(path: str | Path) -> dict[str, Any]:
    """Read one UTF-8 receiving packet JSON file as a dictionary."""

    packet_path = Path(path)
    if not packet_path.exists():
        raise ReceivingPacketValidationError(
            f"Receiving packet is missing: {packet_path}"
        )
    if not packet_path.is_file():
        raise ReceivingPacketValidationError(
            f"Receiving packet path is not a file: {packet_path}"
        )

    try:
        parsed = json.loads(packet_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise ReceivingPacketValidationError(
            f"Could not read receiving packet: {packet_path}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise ReceivingPacketValidationError(
            f"Receiving packet is not valid JSON: {packet_path}"
        ) from exc

    if not isinstance(parsed, dict):
        raise ReceivingPacketValidationError(
            "Receiving packet JSON must be a top-level object"
        )
    return parsed


def validate_receiving_packet_path(path: str | Path) -> dict[str, Any]:
    """Read and validate one receiving packet JSON file."""

    return validate_receiving_packet(read_receiving_packet_json(path))


def validate_receiving_packet(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Validate an already-built receiving packet without mutating it."""

    if not isinstance(packet, Mapping):
        raise ReceivingPacketValidationError("Receiving packet must be a mapping")

    sections = _require_top_level_sections(packet)
    imported_packet = sections["imported_packet"]
    structural_checks = _structural_checks(sections)
    status_checks = _status_checks(sections["receiving_status"])
    count_checks = _count_checks(sections["import_summary"], imported_packet)
    visibility_checks = _visibility_checks(imported_packet)

    all_passed = (
        all(structural_checks.values())
        and all(item["matched"] for item in status_checks.values())
        and all(item["matched"] for item in count_checks.values())
        and all(item["matched"] for item in visibility_checks.values())
    )

    return {
        "validation_metadata": {
            "validation_type": VALIDATION_TYPE,
            "validation_version": VALIDATION_VERSION,
            "generated_at": _utc_timestamp(),
            "validator_module": __name__,
        },
        "packet_identity": _packet_identity(sections),
        "structural_checks": structural_checks,
        "status_checks": status_checks,
        "count_checks": count_checks,
        "visibility_checks": visibility_checks,
        "all_passed": all_passed,
    }


def build_validation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a compact inspection summary from one validation result."""

    identity = _require_mapping(result, "packet_identity", "validation result")
    status_checks = _require_mapping(result, "status_checks", "validation result")
    count_checks = _require_mapping(result, "count_checks", "validation result")

    total_checks = _total_check_count(result)
    failed_checks = _failed_check_count(result)

    return {
        "scenario_id": _optional_value(identity, "scenario_id"),
        "scenario_name": _optional_value(identity, "scenario_name"),
        "source_artifact_path": _optional_value(identity, "source_artifact_path"),
        "host_id": _optional_value(identity, "host_id"),
        "total_check_count": total_checks,
        "failed_check_count": failed_checks,
        "all_passed": _bool_or_false(_optional_value(result, "all_passed")),
        "object_count": _count_actual(count_checks, "object_count"),
        "open_object_count": _count_actual(count_checks, "open_object_count"),
        "coexistence_relation_count": _count_actual(
            count_checks,
            "coexistence_relation_count",
        ),
        "hold_count": _count_actual(count_checks, "hold_count"),
        "transition_record_count": _count_actual(
            count_checks,
            "transition_record_count",
        ),
        "refusal_count": _count_actual(count_checks, "refusal_count"),
        "accepted_action_count": _count_actual(count_checks, "accepted_action_count"),
        "refused_action_count": _count_actual(count_checks, "refused_action_count"),
        "receiving_status": {
            key: _optional_value(check, "actual")
            for key, check in status_checks.items()
            if isinstance(check, Mapping)
        },
    }


def _require_top_level_sections(
    packet: Mapping[str, Any],
) -> dict[str, Mapping[str, Any]]:
    sections: dict[str, Mapping[str, Any]] = {}
    for key in TOP_LEVEL_SECTIONS:
        value = packet.get(key)
        if not isinstance(value, Mapping):
            raise ReceivingPacketValidationError(
                f"Receiving packet missing object section: {key}"
            )
        sections[key] = value
    return sections


def _structural_checks(sections: Mapping[str, Mapping[str, Any]]) -> dict[str, bool]:
    packet_metadata = sections["packet_metadata"]
    source_provenance = sections["source_provenance"]
    import_identity = sections["import_identity"]
    import_summary = sections["import_summary"]
    imported_packet = sections["imported_packet"]

    scenario_metadata = _mapping_or_empty(imported_packet.get("scenario_metadata"))
    snapshot_metadata = _mapping_or_empty(imported_packet.get("snapshot_metadata"))
    host_state = _mapping_or_empty(imported_packet.get("host_state"))

    builder_summary_readable = _builder_summary_readable(sections)

    return {
        "packet_metadata": isinstance(packet_metadata, Mapping),
        "source_provenance": isinstance(source_provenance, Mapping),
        "import_identity": isinstance(import_identity, Mapping),
        "receiving_status": isinstance(sections["receiving_status"], Mapping),
        "import_summary": isinstance(import_summary, Mapping),
        "imported_packet": isinstance(imported_packet, Mapping),
        "packet_type_matches_builder": (
            packet_metadata.get("packet_type") == PACKET_TYPE
        ),
        "packet_version_matches_builder": (
            packet_metadata.get("packet_version") == PACKET_VERSION
        ),
        "packet_generated_at_present": _non_empty_string(
            packet_metadata.get("generated_at")
        ),
        "packet_builder_module_present": _non_empty_string(
            packet_metadata.get("builder_module")
        ),
        "imported_scenario_metadata": isinstance(
            imported_packet.get("scenario_metadata"),
            Mapping,
        ),
        "imported_snapshot_metadata": isinstance(
            imported_packet.get("snapshot_metadata"),
            Mapping,
        ),
        "imported_host_state": isinstance(imported_packet.get("host_state"), Mapping),
        "imported_objects": isinstance(imported_packet.get("objects"), list),
        "imported_coexistence_relations": isinstance(
            imported_packet.get("coexistence_relations"),
            list,
        ),
        "imported_holds": isinstance(imported_packet.get("holds"), list),
        "imported_transition_records": isinstance(
            imported_packet.get("transition_records"),
            list,
        ),
        "scenario_id_present": _non_empty_string(source_provenance.get("scenario_id")),
        "scenario_name_present": _non_empty_string(
            source_provenance.get("scenario_name")
        ),
        "source_artifact_path_present": _non_empty_string(
            source_provenance.get("source_artifact_path")
        ),
        "source_run_directory_path_present": _non_empty_string(
            source_provenance.get("source_run_directory_path")
        ),
        "import_identity_scenario_id_present": _non_empty_string(
            import_identity.get("imported_scenario_id")
        ),
        "import_identity_scenario_name_present": _non_empty_string(
            import_identity.get("imported_scenario_name")
        ),
        "import_identity_matches_source_provenance": (
            source_provenance.get("scenario_id")
            == import_identity.get("imported_scenario_id")
            and source_provenance.get("scenario_name")
            == import_identity.get("imported_scenario_name")
        ),
        "summary_matches_source_provenance": (
            source_provenance.get("scenario_id") == import_summary.get("scenario_id")
            and source_provenance.get("scenario_name")
            == import_summary.get("scenario_name")
        ),
        "imported_metadata_matches_source_provenance": (
            source_provenance.get("scenario_id")
            == scenario_metadata.get("scenario_id")
            and source_provenance.get("scenario_name")
            == scenario_metadata.get("scenario_name")
        ),
        "snapshot_type_present": _non_empty_string(
            import_identity.get("snapshot_type")
        )
        and _non_empty_string(snapshot_metadata.get("snapshot_type")),
        "snapshot_version_present": _non_empty_string(
            import_identity.get("snapshot_version")
        )
        and _non_empty_string(snapshot_metadata.get("snapshot_version")),
        "host_id_present": _non_empty_string(import_summary.get("host_id"))
        and _non_empty_string(host_state.get("host_id")),
        "builder_summary_readable": builder_summary_readable,
    }


def _builder_summary_readable(sections: Mapping[str, Mapping[str, Any]]) -> bool:
    try:
        build_receiving_packet_summary(sections)
    except (RuntimeError, TypeError, KeyError, ValueError):
        return False
    return True


def _packet_identity(sections: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    source_provenance = sections["source_provenance"]
    import_identity = sections["import_identity"]
    import_summary = sections["import_summary"]

    return {
        "scenario_id": source_provenance.get("scenario_id"),
        "scenario_name": source_provenance.get("scenario_name"),
        "source_artifact_path": source_provenance.get("source_artifact_path"),
        "source_run_directory_path": source_provenance.get(
            "source_run_directory_path"
        ),
        "host_id": import_summary.get("host_id"),
        "snapshot_type": import_identity.get("snapshot_type"),
        "snapshot_version": import_identity.get("snapshot_version"),
    }


def _status_checks(status: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        key: {
            "expected": expected,
            "actual": status.get(key),
            "matched": status.get(key) is expected,
        }
        for key, expected in EXPECTED_RECEIVING_STATUS.items()
    }


def _count_checks(
    import_summary: Mapping[str, Any],
    imported_packet: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    actual_counts = _derive_counts(imported_packet)
    checks: dict[str, dict[str, Any]] = {}

    for public_key, summary_key in SUMMARY_COUNT_KEYS.items():
        expected = _int_or_none(import_summary.get(summary_key))
        actual = actual_counts.get(public_key)
        checks[public_key] = {
            "expected": expected,
            "actual": actual,
            "matched": expected is not None and expected == actual,
            "basis": f"import_summary.{summary_key}",
        }

    for key in DERIVED_ONLY_COUNT_KEYS:
        actual = actual_counts[key]
        checks[key] = {
            "expected": actual,
            "actual": actual,
            "matched": True,
            "basis": "derived_from_imported_packet_only",
        }

    return checks


def _derive_counts(imported_packet: Mapping[str, Any]) -> dict[str, int]:
    scenario = _mapping_or_empty(imported_packet.get("scenario_metadata"))
    host = _mapping_or_empty(imported_packet.get("host_state"))
    objects = _list_or_empty(imported_packet.get("objects"))
    relations = _list_or_empty(imported_packet.get("coexistence_relations"))
    holds = _list_or_empty(imported_packet.get("holds"))
    records = _list_or_empty(imported_packet.get("transition_records"))
    action_results = _list_or_empty(scenario.get("action_results"))

    accepted_actions = sum(
        1
        for action in action_results
        if isinstance(action, Mapping) and action.get("accepted") is True
    )
    refused_actions = sum(
        1
        for action in action_results
        if isinstance(action, Mapping) and action.get("accepted") is False
    )

    return {
        "object_count": len(objects),
        "open_object_count": len(_list_or_empty(host.get("open_object_ids"))),
        "coexistence_relation_count": len(relations),
        "hold_count": len(holds),
        "transition_record_count": len(records),
        "refusal_count": sum(
            1
            for record in records
            if isinstance(record, Mapping) and record.get("refusal_code") is not None
        ),
        "accepted_action_count": accepted_actions,
        "refused_action_count": refused_actions,
        "resolved_object_count": sum(
            1
            for obj in objects
            if isinstance(obj, Mapping) and obj.get("resolution_type") is not None
        ),
        "successor_object_count": sum(
            1
            for obj in objects
            if isinstance(obj, Mapping) and obj.get("predecessor_object_id") is not None
        ),
        "evolve_record_count": sum(
            1
            for record in records
            if isinstance(record, Mapping) and record.get("action_type") == "EVOLVE"
        ),
    }


def _visibility_checks(imported_packet: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    objects = _list_or_empty(imported_packet.get("objects"))
    relations = _list_or_empty(imported_packet.get("coexistence_relations"))
    holds = _list_or_empty(imported_packet.get("holds"))
    records = _list_or_empty(imported_packet.get("transition_records"))

    object_ids = [
        obj.get("object_id")
        for obj in objects
        if isinstance(obj, Mapping) and _non_empty_string(obj.get("object_id"))
    ]
    relation_visibility = _relation_visibility(relations)
    hold_visibility = _hold_visibility(holds)
    refusal_visibility = _refusal_visibility(records)
    object_lineage = _object_lineage_visibility(objects)
    evolve_lineage = _evolve_record_visibility(records)

    return {
        "object_ids_visible": {
            "count": len(object_ids),
            "object_ids": sorted(object_ids),
            "matched": len(object_ids) == len(objects) and len(object_ids) > 0,
        },
        "coexistence_relations_visible": {
            "count": len(relation_visibility),
            "relations": relation_visibility,
            "matched": len(relation_visibility) == len(relations),
        },
        "holds_visible": {
            "count": len(hold_visibility),
            "holds": hold_visibility,
            "matched": len(hold_visibility) == len(holds),
        },
        "refusal_records_visible": {
            "count": len(refusal_visibility),
            "refusal_records": refusal_visibility,
            "matched": _refusal_records_match(records, refusal_visibility),
        },
        "predecessor_successor_lineage_visible": {
            "object_lineage_count": len(object_lineage),
            "evolve_record_lineage_count": len(evolve_lineage),
            "object_lineage": object_lineage,
            "evolve_record_lineage": evolve_lineage,
            "matched": _lineage_matches(objects, records, object_lineage, evolve_lineage),
        },
    }


def _relation_visibility(values: list[Any]) -> list[dict[str, Any]]:
    visible = []
    for value in values:
        if not isinstance(value, Mapping):
            continue
        relation = {
            "relation_type": value.get("relation_type"),
            "object_id": value.get("object_id"),
            "related_object_id": value.get("related_object_id"),
            "basis_ref": value.get("basis_ref"),
            "created_by_record_id": value.get("created_by_record_id"),
        }
        if all(_non_empty_string(item) for item in relation.values()):
            visible.append(relation)
    return _sorted_dicts(visible)


def _hold_visibility(values: list[Any]) -> list[dict[str, Any]]:
    visible = []
    for value in values:
        if not isinstance(value, Mapping):
            continue
        if not (
            _non_empty_string(value.get("target_object_id"))
            and isinstance(value.get("active"), bool)
            and _non_empty_string(value.get("basis_ref"))
            and _non_empty_string(value.get("set_by_record_id"))
        ):
            continue
        visible.append(
            {
                "target_object_id": value.get("target_object_id"),
                "active": value.get("active"),
                "basis_ref": value.get("basis_ref"),
                "set_by_record_id": value.get("set_by_record_id"),
            }
        )
    return _sorted_dicts(visible)


def _refusal_visibility(records: list[Any]) -> list[dict[str, Any]]:
    visible = []
    for record in records:
        if not isinstance(record, Mapping):
            continue
        if record.get("refusal_code") is None and record.get("accepted") is not False:
            continue
        if not (
            _non_empty_string(record.get("record_id"))
            and _non_empty_string(record.get("action_type"))
            and _non_empty_string(record.get("refusal_code"))
            and record.get("accepted") is False
        ):
            continue
        visible.append(
            {
                "record_id": record.get("record_id"),
                "action_type": record.get("action_type"),
                "refusal_code": record.get("refusal_code"),
            }
        )
    return _sorted_dicts(visible)


def _object_lineage_visibility(objects: list[Any]) -> list[dict[str, Any]]:
    lineage = []
    for obj in objects:
        if not isinstance(obj, Mapping):
            continue
        predecessor = obj.get("predecessor_object_id")
        object_id = obj.get("object_id")
        if predecessor is None:
            continue
        if _non_empty_string(predecessor) and _non_empty_string(object_id):
            lineage.append(
                {
                    "predecessor_object_id": predecessor,
                    "successor_object_id": object_id,
                }
            )
    return _sorted_dicts(lineage)


def _evolve_record_visibility(records: list[Any]) -> list[dict[str, Any]]:
    lineage = []
    for record in records:
        if not isinstance(record, Mapping) or record.get("action_type") != "EVOLVE":
            continue
        item = {
            "record_id": record.get("record_id"),
            "predecessor_object_id": record.get("predecessor_object_id"),
            "successor_object_id": record.get("successor_object_id"),
            "target_resolution_type": record.get("target_resolution_type"),
        }
        if (
            _non_empty_string(item["record_id"])
            and _non_empty_string(item["predecessor_object_id"])
            and _non_empty_string(item["successor_object_id"])
            and item["target_resolution_type"] == "EVOLVE"
        ):
            lineage.append(item)
    return _sorted_dicts(lineage)


def _refusal_records_match(
    records: list[Any],
    visible_refusals: list[dict[str, Any]],
) -> bool:
    expected_refusals = sum(
        1
        for record in records
        if isinstance(record, Mapping)
        and (record.get("refusal_code") is not None or record.get("accepted") is False)
    )
    return expected_refusals == len(visible_refusals)


def _lineage_matches(
    objects: list[Any],
    records: list[Any],
    object_lineage: list[dict[str, Any]],
    evolve_lineage: list[dict[str, Any]],
) -> bool:
    expected_object_lineage = sum(
        1
        for obj in objects
        if isinstance(obj, Mapping) and obj.get("predecessor_object_id") is not None
    )
    expected_evolve_records = sum(
        1
        for record in records
        if isinstance(record, Mapping) and record.get("action_type") == "EVOLVE"
    )
    return (
        expected_object_lineage == len(object_lineage)
        and expected_evolve_records == len(evolve_lineage)
    )


def _total_check_count(result: Mapping[str, Any]) -> int:
    return (
        len(_mapping_or_empty(result.get("structural_checks")))
        + len(_mapping_or_empty(result.get("status_checks")))
        + len(_mapping_or_empty(result.get("count_checks")))
        + len(_mapping_or_empty(result.get("visibility_checks")))
    )


def _failed_check_count(result: Mapping[str, Any]) -> int:
    failed = 0
    structural = _mapping_or_empty(result.get("structural_checks"))
    failed += sum(1 for value in structural.values() if value is not True)

    for section_name in ("status_checks", "count_checks", "visibility_checks"):
        section = _mapping_or_empty(result.get(section_name))
        failed += sum(
            1
            for value in section.values()
            if not isinstance(value, Mapping) or value.get("matched") is not True
        )
    return failed


def _count_actual(count_checks: Mapping[str, Any], key: str) -> Any:
    check = count_checks.get(key)
    if not isinstance(check, Mapping):
        return None
    return check.get("actual")


def _require_mapping(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise ReceivingPacketValidationError(
            f"Malformed {context}: {key} must be an object"
        )
    return value


def _mapping_or_empty(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _list_or_empty(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return []


def _int_or_none(value: Any) -> int | None:
    if isinstance(value, int) and not isinstance(value, bool):
        return value
    return None


def _bool_or_false(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return False


def _optional_value(mapping: Mapping[str, Any], key: str) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    return mapping.get(key)


def _non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and value != ""


def _sorted_dicts(values: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        values,
        key=lambda value: json.dumps(value, sort_keys=True, allow_nan=False),
    )


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
