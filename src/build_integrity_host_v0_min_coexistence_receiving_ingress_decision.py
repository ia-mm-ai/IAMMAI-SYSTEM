"""Bounded receiving ingress decision builder for coexistence packets.

This module builds one local receiving-side decision artifact from one
receiving packet. It validates the packet through
``validate_integrity_host_v0_min_coexistence_receiving_packet`` and then records
whether the packet is eligible for bounded receiving handling.

The decision artifact is additive inspection output only. It does not replay
actions into a live host, merge imported state, define persistence or registry
law, complete continuity, or upgrade received material into local standing.
Source remains source, validation remains validation, and ingress decision
remains a local receiving-side decision.
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
    build_receiving_packet,
)
from validate_integrity_host_v0_min_coexistence_receiving_packet import (
    ReceivingPacketValidationError,
    build_validation_summary,
    read_receiving_packet_json,
    validate_receiving_packet,
)


OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiving_ingress_decisions"
)
DECISION_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_RECEIVING_INGRESS_DECISION"
DECISION_VERSION = "0.1.0"
DECISION_RECEIVE = "RECEIVE_BOUNDED_PACKET"
DECISION_REJECT = "REJECT_PACKET"


class ReceivingIngressDecisionError(ValueError):
    """Raised when an ingress decision cannot be built or written."""


def build_ingress_decision(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Build one ingress decision from an already-built receiving packet."""

    return _build_ingress_decision(packet, receiving_packet_path=None)


def build_ingress_decision_from_packet_path(path: str | Path) -> dict[str, Any]:
    """Read one receiving packet JSON file and build an ingress decision."""

    packet_path = Path(path)
    try:
        packet = read_receiving_packet_json(packet_path)
    except ReceivingPacketValidationError as exc:
        raise ReceivingIngressDecisionError(
            f"Cannot read receiving packet for ingress decision: {packet_path}"
        ) from exc

    return _build_ingress_decision(packet, receiving_packet_path=packet_path)


def build_ingress_decision_from_source_artifact(path: str | Path) -> dict[str, Any]:
    """Build a receiving packet from a source artifact, then decide ingress."""

    try:
        packet = build_receiving_packet(path)
    except RuntimeError as exc:
        raise ReceivingIngressDecisionError(
            f"Cannot build receiving packet from source artifact: {path}"
        ) from exc

    return _build_ingress_decision(packet, receiving_packet_path=None)


def write_ingress_decision(
    decision: Mapping[str, Any],
    output_path: str | Path | None = None,
) -> Path:
    """Write one UTF-8 JSON ingress decision artifact without overwriting."""

    if not isinstance(decision, Mapping):
        raise ReceivingIngressDecisionError("Ingress decision must be a mapping")

    target_path = (
        _default_output_path(decision)
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target_path.parent.mkdir(parents=True, exist_ok=True)
    if target_path.exists():
        raise ReceivingIngressDecisionError(
            f"Refusing to overwrite ingress decision: {_display_path(target_path)}"
        )

    target_path.write_text(_json_text(decision), encoding="utf-8")
    return target_path


def build_ingress_decision_summary(decision: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one ingress decision."""

    source = _require_mapping(decision, "source_provenance", "ingress decision")
    packet_identity = _require_mapping(
        decision,
        "packet_identity",
        "ingress decision",
    )
    validation_summary = _require_mapping(
        decision,
        "validation_summary",
        "ingress decision",
    )
    ingress = _require_mapping(decision, "ingress_decision", "ingress decision")
    status = _require_mapping(
        decision,
        "receiving_status_carry_forward",
        "ingress decision",
    )

    return {
        "scenario_id": _optional_value(source, "scenario_id"),
        "scenario_name": _optional_value(source, "scenario_name"),
        "source_artifact_path": _optional_value(source, "source_artifact_path"),
        "receiving_packet_path": _optional_value(
            packet_identity,
            "receiving_packet_path",
        ),
        "host_id": _optional_value(packet_identity, "host_id"),
        "decision": _optional_value(ingress, "decision"),
        "decision_reason": _optional_value(ingress, "decision_reason"),
        "validation_passed": _optional_value(ingress, "validation_passed"),
        "eligible_for_bounded_receiving_handling": _optional_value(
            ingress,
            "eligible_for_bounded_receiving_handling",
        ),
        "failed_check_count": _optional_value(
            validation_summary,
            "failed_check_count",
        ),
        "all_passed": _optional_value(validation_summary, "all_passed"),
        "object_count": _optional_value(validation_summary, "object_count"),
        "open_object_count": _optional_value(
            validation_summary,
            "open_object_count",
        ),
        "coexistence_relation_count": _optional_value(
            validation_summary,
            "coexistence_relation_count",
        ),
        "hold_count": _optional_value(validation_summary, "hold_count"),
        "transition_record_count": _optional_value(
            validation_summary,
            "transition_record_count",
        ),
        "refusal_count": _optional_value(validation_summary, "refusal_count"),
        "accepted_action_count": _optional_value(
            validation_summary,
            "accepted_action_count",
        ),
        "refused_action_count": _optional_value(
            validation_summary,
            "refused_action_count",
        ),
        "receiving_status": _json_ready(status),
    }


def _build_ingress_decision(
    packet: Mapping[str, Any],
    *,
    receiving_packet_path: Path | None,
) -> dict[str, Any]:
    if not isinstance(packet, Mapping):
        raise ReceivingIngressDecisionError("Receiving packet must be a mapping")

    try:
        validation_result = validate_receiving_packet(packet)
        validation_summary = build_validation_summary(validation_result)
    except ReceivingPacketValidationError as exc:
        raise ReceivingIngressDecisionError(
            "Receiving packet failed hard validation before ingress decision"
        ) from exc

    source_provenance = _source_provenance(packet)
    packet_identity = _packet_identity(packet, validation_summary, receiving_packet_path)
    ingress_decision = _ingress_decision(validation_summary)
    receiving_status = _receiving_status_carry_forward(validation_summary)

    return {
        "decision_metadata": {
            "decision_type": DECISION_TYPE,
            "decision_version": DECISION_VERSION,
            "generated_at": _utc_timestamp(),
            "decision_builder_module": __name__,
        },
        "source_provenance": source_provenance,
        "packet_identity": packet_identity,
        "validation_summary": _json_ready(validation_summary),
        "validation_result": _json_ready(validation_result),
        "ingress_decision": ingress_decision,
        "receiving_status_carry_forward": receiving_status,
        "receiving_packet": _json_ready(packet),
    }


def _source_provenance(packet: Mapping[str, Any]) -> dict[str, Any]:
    source = _mapping_or_empty(packet.get("source_provenance"))
    return {
        "source_artifact_path": source.get("source_artifact_path"),
        "source_run_directory_path": source.get("source_run_directory_path"),
        "scenario_id": source.get("scenario_id"),
        "scenario_name": source.get("scenario_name"),
        "scenario_description": source.get("scenario_description"),
        "source_generated_at": source.get("source_generated_at"),
    }


def _packet_identity(
    packet: Mapping[str, Any],
    validation_summary: Mapping[str, Any],
    receiving_packet_path: Path | None,
) -> dict[str, Any]:
    packet_metadata = _mapping_or_empty(packet.get("packet_metadata"))
    import_identity = _mapping_or_empty(packet.get("import_identity"))

    return {
        "scenario_id": validation_summary.get("scenario_id"),
        "scenario_name": validation_summary.get("scenario_name"),
        "host_id": validation_summary.get("host_id"),
        "snapshot_type": import_identity.get("snapshot_type"),
        "snapshot_version": import_identity.get("snapshot_version"),
        "packet_type": packet_metadata.get("packet_type"),
        "packet_version": packet_metadata.get("packet_version"),
        "expected_packet_type": PACKET_TYPE,
        "expected_packet_version": PACKET_VERSION,
        "receiving_packet_path": (
            _display_path(receiving_packet_path)
            if receiving_packet_path is not None
            else None
        ),
    }


def _ingress_decision(validation_summary: Mapping[str, Any]) -> dict[str, Any]:
    validation_passed = validation_summary.get("all_passed") is True
    failed_count = validation_summary.get("failed_check_count")
    no_failed_checks = isinstance(failed_count, int) and failed_count == 0
    eligible = validation_passed and no_failed_checks

    if eligible:
        decision = DECISION_RECEIVE
        reason = "VALIDATION_PASSED_FOR_BOUNDED_RECEIVING_HANDLING"
    else:
        decision = DECISION_REJECT
        reason = "VALIDATION_FAILED_FOR_BOUNDED_RECEIVING_HANDLING"

    return {
        "decision": decision,
        "decision_reason": reason,
        "validation_passed": validation_passed,
        "eligible_for_bounded_receiving_handling": eligible,
        "requires_replay": False,
        "requires_merge": False,
        "continuity_completed": False,
        "standing_upgraded": False,
    }


def _receiving_status_carry_forward(
    validation_summary: Mapping[str, Any],
) -> dict[str, Any]:
    status = _mapping_or_empty(validation_summary.get("receiving_status"))
    return {
        "receiving_packet_exists": status.get("receiving_packet_exists"),
        "imported_packet_read_only_here": status.get(
            "imported_packet_read_only_here"
        ),
        "source_remains_source": status.get("source_remains_source"),
        "replayed_into_live_host": status.get("replayed_into_live_host"),
        "merged_into_local_state": status.get("merged_into_local_state"),
        "continuity_completed": status.get("continuity_completed"),
        "standing_upgraded": status.get("standing_upgraded"),
        "preserved_structure_visible": status.get("preserved_structure_visible"),
    }


def _default_output_path(decision: Mapping[str, Any]) -> Path:
    stem_source = _decision_filename_source(decision)
    return _repo_root() / OUTPUT_ROOT / f"{stem_source}__receiving_ingress_decision.json"


def _decision_filename_source(decision: Mapping[str, Any]) -> str:
    packet_identity = _mapping_or_empty(decision.get("packet_identity"))
    source = _mapping_or_empty(decision.get("source_provenance"))

    for key, mapping in (
        ("receiving_packet_path", packet_identity),
        ("source_artifact_path", source),
        ("scenario_id", source),
    ):
        value = mapping.get(key)
        if isinstance(value, str) and value:
            stem = Path(value).stem
            return stem or "receiving_packet"

    raise ReceivingIngressDecisionError(
        "Cannot derive default ingress decision filename"
    )


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


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_json_ready(item) for item in value]
    if isinstance(value, tuple):
        return [_json_ready(item) for item in value]
    if isinstance(value, set):
        return sorted((_json_ready(item) for item in value), key=repr)
    if isinstance(value, Path):
        return _display_path(value)
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    return str(value)


def _require_mapping(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise ReceivingIngressDecisionError(f"Malformed {context}: {key} must be object")
    return value


def _mapping_or_empty(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _optional_value(mapping: Mapping[str, Any], key: str) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    return mapping.get(key)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
