"""Build a bounded current-governing packet for v0-min coexistence.

This module reads one current execution-authority resolution artifact, one
run-family packet artifact, and one preserved-run status packet artifact. It
verifies that the three artifacts correspond, then emits one additive packet
that makes the current governing preserved run and preserved non-governing
runs explicit.

The packet is a local engineering surface only. It does not replay source
actions into a live host, merge preserved runs, create persistence or registry
doctrine, complete continuity, or promote bounded current authority into final
system governance.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from build_integrity_host_v0_min_coexistence_preserved_run_status_packet import (
    PreservedRunStatusPacketError,
    build_preserved_run_status_summary,
)
from build_integrity_host_v0_min_coexistence_run_family_packet import (
    RunFamilyPacketError,
    build_run_family_summary,
)
from resolve_current_integrity_host_v0_min_coexistence_execution_authority import (
    DECISION_RESOLVED,
    ExecutionAuthorityResolutionError,
    build_execution_authority_summary,
)


EXECUTION_AUTHORITY_RESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_execution_authority"
)
RUN_FAMILY_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_run_family_packets"
)
PRESERVED_RUN_STATUS_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_preserved_run_status_packets"
)
CURRENT_GOVERNING_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_governing_packets"
)

GOVERNING_PACKET_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_CURRENT_GOVERNING_PACKET"
)
GOVERNING_PACKET_VERSION = "0.1.0"

ROLE_CURRENT_AUTHORITY = "CURRENT_EXECUTION_AUTHORITY"

NON_CLAIM_DEFAULTS = {
    "continuity_completed": False,
    "standing_upgraded": False,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
    "minimum_lawful_system_completed": False,
    "final_system_identity_completed": False,
    "final_preserved_run_governance_completed": False,
    "final_governing_scope_completed": False,
}


class CurrentGoverningPacketError(RuntimeError):
    """Raised when a bounded current-governing packet cannot be built."""


def discover_latest_authority_resolution(root: Path) -> Path:
    """Return the lexically latest authority-resolution artifact."""

    artifacts = _discover_json_artifacts(
        root,
        "current_execution_authority_resolution*.json",
        "execution-authority resolution root",
    )
    if not artifacts:
        raise CurrentGoverningPacketError(
            "No execution-authority resolution artifact found under "
            f"{_display_path(_repo_relative_path(root))}"
        )
    return artifacts[-1]


def discover_latest_run_family_packet(root: Path) -> Path:
    """Return the lexically latest run-family packet artifact."""

    artifacts = _discover_json_artifacts(
        root,
        "current_run_family_packet*.json",
        "run-family packet root",
    )
    if not artifacts:
        raise CurrentGoverningPacketError(
            f"No run-family packet artifact found under {_display_path(_repo_relative_path(root))}"
        )
    return artifacts[-1]


def discover_latest_preserved_run_status_packet(root: Path) -> Path:
    """Return the lexically latest preserved-run status packet artifact."""

    artifacts = _discover_json_artifacts(
        root,
        "current_preserved_run_status_packet*.json",
        "preserved-run status packet root",
    )
    if not artifacts:
        raise CurrentGoverningPacketError(
            "No preserved-run status packet artifact found under "
            f"{_display_path(_repo_relative_path(root))}"
        )
    return artifacts[-1]


def build_current_governing_packet() -> dict[str, Any]:
    """Build one bounded current-governing packet from existing artifacts."""

    authority_path = discover_latest_authority_resolution(
        EXECUTION_AUTHORITY_RESOLUTION_ROOT
    )
    family_path = discover_latest_run_family_packet(RUN_FAMILY_PACKET_ROOT)
    status_path = discover_latest_preserved_run_status_packet(
        PRESERVED_RUN_STATUS_PACKET_ROOT
    )

    authority = _read_authority_resolution(authority_path)
    family = _read_run_family_packet(family_path)
    status = _read_preserved_run_status_packet(status_path)

    authority_summary = _authority_summary(authority)
    family_summary = _family_summary(family)
    status_summary = _status_summary(status)

    _verify_artifact_correspondence(
        authority,
        family,
        status,
        authority_summary,
        family_summary,
        status_summary,
        authority_path,
        family_path,
    )

    current_entry = _current_authority_entry(status)
    non_governing_entries = _non_governing_entries(status)
    non_claims = _non_claims(authority, family, status)
    canonical = _canonical_execution_line(family)

    return {
        "governing_packet_metadata": {
            "governing_packet_type": GOVERNING_PACKET_TYPE,
            "governing_packet_version": GOVERNING_PACKET_VERSION,
            "generated_at": _utc_timestamp(),
            "builder_module": __name__,
        },
        "canonical_execution_line": canonical,
        "authority_reference": _authority_reference(
            authority,
            authority_summary,
            authority_path,
            family_path,
            status_path,
        ),
        "current_governing_run": _current_governing_run(current_entry, non_claims),
        "preserved_non_governing_runs": non_governing_entries,
        "governing_scope": _governing_scope(canonical, current_entry),
        "forced_system_pressure_signals": _pressure_signals(authority, family, status),
        "non_claims": non_claims,
    }


def write_current_governing_packet(
    packet: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one UTF-8 JSON current-governing packet without overwriting."""

    if not isinstance(packet, Mapping):
        raise CurrentGoverningPacketError("Current-governing packet must be a mapping")

    target = (
        _next_default_governing_packet_path()
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise CurrentGoverningPacketError(
            f"Refusing to overwrite current-governing packet: {_display_path(target)}"
        )
    target.write_text(_json_text(packet), encoding="utf-8")
    return target


def build_current_governing_summary(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one governing packet."""

    canonical = _require_mapping(
        packet,
        "canonical_execution_line",
        "current-governing packet",
    )
    authority = _require_mapping(
        packet,
        "authority_reference",
        "current-governing packet",
    )
    current = _require_mapping(
        packet,
        "current_governing_run",
        "current-governing packet",
    )
    non_governing = _require_list(
        packet,
        "preserved_non_governing_runs",
        "current-governing packet",
    )
    scope = _require_mapping(packet, "governing_scope", "current-governing packet")
    non_claims = _require_mapping(packet, "non_claims", "current-governing packet")

    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "current-governing packet.canonical_execution_line",
        ),
        "current_governing_source_run_path": _require_string(
            current,
            "source_run_directory_path",
            "current-governing packet.current_governing_run",
        ),
        "current_governing_ingress_run_path": _require_string(
            current,
            "matched_ingress_run_path",
            "current-governing packet.current_governing_run",
        ),
        "preserved_non_governing_run_count": len(non_governing),
        "authority_decision": _require_string(
            authority,
            "authority_decision",
            "current-governing packet.authority_reference",
        ),
        "authority_decision_reason": _require_string(
            authority,
            "authority_decision_reason",
            "current-governing packet.authority_reference",
        ),
        "governing_scope_flags": {
            "governing_is_bounded": _require_bool(
                scope,
                "governing_is_bounded",
                "current-governing packet.governing_scope",
            ),
            "governing_applies_to_current_execution_line": _require_bool(
                scope,
                "governing_applies_to_current_execution_line",
                "current-governing packet.governing_scope",
            ),
            "preserved_non_governing_runs_remain_preserved": _require_bool(
                scope,
                "preserved_non_governing_runs_remain_preserved",
                "current-governing packet.governing_scope",
            ),
            "current_authority_does_not_erase_preserved_runs": _require_bool(
                scope,
                "current_authority_does_not_erase_preserved_runs",
                "current-governing packet.governing_scope",
            ),
        },
        "non_claims": {
            key: _require_bool(non_claims, key, "current-governing packet.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _current_governing_run(
    entry: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "source_run_directory_path": _require_string(
            entry,
            "source_run_directory_path",
            "preserved-run status entry",
        ),
        "source_manifest_path": _require_string(
            entry,
            "source_manifest_path",
            "preserved-run status entry",
        ),
        "matched_ingress_run_path": _require_string(
            entry,
            "matched_ingress_run_path",
            "preserved-run status entry",
        ),
        "matched_comparison_artifact_path": _require_string(
            entry,
            "matched_comparison_artifact_path",
            "preserved-run status entry",
        ),
        "status_role": _require_string(entry, "status_role", "preserved-run status entry"),
        "current_authority": _require_bool(
            entry,
            "current_authority",
            "preserved-run status entry",
        ),
        "candidate_eligible": _require_bool(
            entry,
            "candidate_eligible",
            "preserved-run status entry",
        ),
        "governing_reason": "CURRENT_AUTHORITY_ENTRY_FROM_PRESERVED_RUN_STATUS_PACKET",
        "preservation_signals": _preservation_signals(entry),
        "non_claims": dict(non_claims),
    }


def _non_governing_entries(status: Mapping[str, Any]) -> list[dict[str, Any]]:
    entries = _require_list(
        status,
        "preserved_run_status_entries",
        "preserved-run status packet",
    )
    non_governing: list[dict[str, Any]] = []
    for index, value in enumerate(entries):
        entry = _require_mapping(
            value,
            f"preserved-run status packet.preserved_run_status_entries[{index}]",
        )
        if _require_string(entry, "status_role", "preserved-run status entry") == ROLE_CURRENT_AUTHORITY:
            continue
        non_governing.append(
            {
                "source_run_directory_path": _require_string(
                    entry,
                    "source_run_directory_path",
                    "preserved-run status entry",
                ),
                "source_manifest_path": _require_string(
                    entry,
                    "source_manifest_path",
                    "preserved-run status entry",
                ),
                "matched_ingress_run_path": _optional_string(
                    entry,
                    "matched_ingress_run_path",
                    "preserved-run status entry",
                ),
                "matched_comparison_artifact_path": _optional_string(
                    entry,
                    "matched_comparison_artifact_path",
                    "preserved-run status entry",
                ),
                "status_role": _require_string(
                    entry,
                    "status_role",
                    "preserved-run status entry",
                ),
                "current_authority": _require_bool(
                    entry,
                    "current_authority",
                    "preserved-run status entry",
                ),
                "candidate_eligible": _require_bool(
                    entry,
                    "candidate_eligible",
                    "preserved-run status entry",
                ),
                "status_reason": _require_string(
                    entry,
                    "status_reason",
                    "preserved-run status entry",
                ),
                "ineligibility_reasons": _string_list(
                    entry,
                    "ineligibility_reasons",
                    "preserved-run status entry",
                ),
                "preservation_signals": _preservation_signals(entry),
            }
        )
    return non_governing


def _current_authority_entry(status: Mapping[str, Any]) -> Mapping[str, Any]:
    entries = _require_list(
        status,
        "preserved_run_status_entries",
        "preserved-run status packet",
    )
    current_entries: list[Mapping[str, Any]] = []
    for index, value in enumerate(entries):
        entry = _require_mapping(
            value,
            f"preserved-run status packet.preserved_run_status_entries[{index}]",
        )
        if _require_string(entry, "status_role", "preserved-run status entry") == ROLE_CURRENT_AUTHORITY:
            current_entries.append(entry)

    if len(current_entries) != 1:
        raise CurrentGoverningPacketError(
            "Current-governing packet requires exactly one current authority entry"
        )
    current = current_entries[0]
    if _require_bool(current, "current_authority", "current authority entry") is not True:
        raise CurrentGoverningPacketError(
            "Current authority entry must be marked current_authority"
        )
    if _require_bool(current, "candidate_eligible", "current authority entry") is not True:
        raise CurrentGoverningPacketError(
            "Current authority entry must remain candidate eligible"
        )
    return current


def _governing_scope(
    canonical: Mapping[str, Any],
    current_entry: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "governing_core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "current-governing packet.canonical_execution_line",
        ),
        "governing_source_run_path": _require_string(
            current_entry,
            "source_run_directory_path",
            "current authority entry",
        ),
        "governing_ingress_run_path": _require_string(
            current_entry,
            "matched_ingress_run_path",
            "current authority entry",
        ),
        "governing_comparison_artifact_path": _require_string(
            current_entry,
            "matched_comparison_artifact_path",
            "current authority entry",
        ),
        "governing_is_bounded": True,
        "governing_applies_to_current_execution_line": True,
        "preserved_non_governing_runs_remain_preserved": True,
        "current_authority_does_not_erase_preserved_runs": True,
    }


def _verify_artifact_correspondence(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    status: Mapping[str, Any],
    authority_summary: Mapping[str, Any],
    family_summary: Mapping[str, Any],
    status_summary: Mapping[str, Any],
    authority_path: Path,
    family_path: Path,
) -> None:
    authority_decision = _require_mapping(
        authority,
        "authority_decision",
        "authority resolution",
    )
    if _require_string(authority_decision, "decision", "authority resolution.authority_decision") != DECISION_RESOLVED:
        raise CurrentGoverningPacketError(
            "Current-governing packet requires a resolved current authority"
        )

    authority_core = _core_execution_file(authority, "authority resolution")
    family_core = _core_execution_file(family, "run-family packet")
    status_core = _core_execution_file(status, "preserved-run status packet")
    if authority_core != family_core or authority_core != status_core:
        raise CurrentGoverningPacketError(
            "Canonical core execution file does not match across governing artifacts"
        )

    status_authority = _require_mapping(
        status,
        "authority_reference",
        "preserved-run status packet",
    )
    if not _same_path(
        _require_string(
            status_authority,
            "authority_artifact_path",
            "preserved-run status packet.authority_reference",
        ),
        authority_path,
    ):
        raise CurrentGoverningPacketError(
            "Preserved-run status packet does not reference the selected authority artifact"
        )
    if not _same_path(
        _require_string(
            status_authority,
            "run_family_packet_artifact_path",
            "preserved-run status packet.authority_reference",
        ),
        family_path,
    ):
        raise CurrentGoverningPacketError(
            "Preserved-run status packet does not reference the selected run-family artifact"
        )

    family_authority = _require_mapping(
        family,
        "authority_reference",
        "run-family packet",
    )
    if not _same_path(
        _require_string(
            family_authority,
            "resolution_artifact_path",
            "run-family packet.authority_reference",
        ),
        authority_path,
    ):
        raise CurrentGoverningPacketError(
            "Run-family packet does not reference the selected authority artifact"
        )

    _require_matching_optional_paths(
        (
            authority_summary.get("selected_source_run_directory_path"),
            family_summary.get("current_authority_source_run_path"),
            status_summary.get("selected_current_authority_source_run_path"),
            status_authority.get("selected_source_run_path"),
        ),
        "selected current authority source run path",
    )
    _require_matching_optional_paths(
        (
            authority_summary.get("selected_ingress_run_directory_path"),
            family_summary.get("current_authority_ingress_run_path"),
            status_authority.get("selected_ingress_run_path"),
        ),
        "selected current authority ingress run path",
    )
    _require_matching_optional_paths(
        (
            authority_summary.get("selected_comparison_artifact_path"),
            family_authority.get("selected_comparison_artifact_path"),
            status_authority.get("selected_comparison_artifact_path"),
        ),
        "selected current authority comparison artifact path",
    )

    eligible_counts = (
        _require_int(
            authority_decision,
            "eligible_candidate_count",
            "authority resolution.authority_decision",
        ),
        _require_int(
            family_authority,
            "eligible_candidate_count",
            "run-family packet.authority_reference",
        ),
        _require_int(
            status_authority,
            "eligible_candidate_count",
            "preserved-run status packet.authority_reference",
        ),
        status_summary["eligible_run_count"],
    )
    if len(set(eligible_counts)) != 1:
        raise CurrentGoverningPacketError(
            "Eligible candidate count does not align across governing artifacts"
        )

    family_preserved_count = family_summary["preserved_run_count"]
    status_entries = _require_list(
        status,
        "preserved_run_status_entries",
        "preserved-run status packet",
    )
    status_preserved_count = status_summary["preserved_run_count"]
    if family_preserved_count != status_preserved_count or family_preserved_count != len(status_entries):
        raise CurrentGoverningPacketError(
            "Preserved run count does not align between family and status artifacts"
        )
    if status_summary["current_authority_run_count"] != 1:
        raise CurrentGoverningPacketError(
            "Preserved-run status packet must carry exactly one current authority run"
        )


def _canonical_execution_line(family: Mapping[str, Any]) -> dict[str, Any]:
    canonical = _require_mapping(family, "canonical_execution_line", "run-family packet")
    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "run-family packet.canonical_execution_line",
        ),
        "derivative_support_scope": _string_list(
            canonical,
            "derivative_support_scope",
            "run-family packet.canonical_execution_line",
        ),
        "lineage_predecessor_files": _string_list(
            canonical,
            "lineage_predecessor_files",
            "run-family packet.canonical_execution_line",
        ),
    }


def _authority_reference(
    authority: Mapping[str, Any],
    authority_summary: Mapping[str, Any],
    authority_path: Path,
    family_path: Path,
    status_path: Path,
) -> dict[str, Any]:
    decision = _require_mapping(authority, "authority_decision", "authority resolution")
    return {
        "authority_artifact_path": _display_path(authority_path),
        "run_family_packet_artifact_path": _display_path(family_path),
        "preserved_run_status_packet_artifact_path": _display_path(status_path),
        "authority_decision": _require_string(
            decision,
            "decision",
            "authority resolution.authority_decision",
        ),
        "authority_decision_reason": _require_string(
            decision,
            "decision_reason",
            "authority resolution.authority_decision",
        ),
        "selected_source_run_path": authority_summary.get(
            "selected_source_run_directory_path"
        ),
        "selected_ingress_run_path": authority_summary.get(
            "selected_ingress_run_directory_path"
        ),
        "selected_comparison_artifact_path": authority_summary.get(
            "selected_comparison_artifact_path"
        ),
        "candidate_run_count": _require_int(
            decision,
            "candidate_run_count",
            "authority resolution.authority_decision",
        ),
        "eligible_candidate_count": _require_int(
            decision,
            "eligible_candidate_count",
            "authority resolution.authority_decision",
        ),
    }


def _pressure_signals(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    status: Mapping[str, Any],
) -> dict[str, Any]:
    signals = _json_ready(
        dict(
            _require_mapping(
                status,
                "forced_system_pressure_signals",
                "preserved-run status packet",
            )
        )
    )
    for artifact, label in (
        (family, "run-family packet"),
        (authority, "authority resolution"),
    ):
        incoming = _require_mapping(artifact, "forced_system_pressure_signals", label)
        for key, value in incoming.items():
            signals.setdefault(str(key), _json_ready(value))
    signals["current_governing_scope_pressure"] = (
        "The selected current authority now needs one bounded governing scope "
        "surface that states what governs without erasing preserved "
        "non-governing runs or claiming final governance."
    )
    return signals


def _non_claims(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    status: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for label, artifact in (
        ("authority resolution", authority),
        ("run-family packet", family),
        ("preserved-run status packet", status),
    ):
        incoming = _require_mapping(artifact, "non_claims", label)
        for key in NON_CLAIM_DEFAULTS:
            if key in incoming:
                value = _require_bool(incoming, key, f"{label}.non_claims")
                if value is not False:
                    raise CurrentGoverningPacketError(
                        f"{label}.non_claims.{key} must remain false"
                    )
                non_claims[key] = False
    return non_claims


def _preservation_signals(entry: Mapping[str, Any]) -> dict[str, bool]:
    signals = _require_mapping(entry, "preservation_signals", "preserved-run status entry")
    return {
        "source_preserved": _require_bool(
            signals,
            "source_preserved",
            "preserved-run status entry.preservation_signals",
        ),
        "ingress_preserved": _require_bool(
            signals,
            "ingress_preserved",
            "preserved-run status entry.preservation_signals",
        ),
        "comparison_preserved": _require_bool(
            signals,
            "comparison_preserved",
            "preserved-run status entry.preservation_signals",
        ),
        "authority_candidate_visible": _require_bool(
            signals,
            "authority_candidate_visible",
            "preserved-run status entry.preservation_signals",
        ),
    }


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise CurrentGoverningPacketError(
            "Authority resolution artifact is malformed"
        ) from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise CurrentGoverningPacketError("Run-family packet artifact is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except PreservedRunStatusPacketError as exc:
        raise CurrentGoverningPacketError(
            "Preserved-run status packet artifact is malformed"
        ) from exc


def _read_authority_resolution(path: Path) -> dict[str, Any]:
    resolution = _read_json_object(path, "execution-authority resolution")
    _require_mapping(resolution, "resolution_metadata", "authority resolution")
    _require_mapping(resolution, "canonical_execution_line", "authority resolution")
    _require_list(resolution, "candidate_runs", "authority resolution")
    _require_mapping(resolution, "authority_decision", "authority resolution")
    _require_mapping(
        resolution,
        "forced_system_pressure_signals",
        "authority resolution",
    )
    _require_mapping(resolution, "non_claims", "authority resolution")
    return resolution


def _read_run_family_packet(path: Path) -> dict[str, Any]:
    packet = _read_json_object(path, "run-family packet")
    _require_mapping(packet, "family_metadata", "run-family packet")
    _require_mapping(packet, "canonical_execution_line", "run-family packet")
    _require_mapping(packet, "authority_reference", "run-family packet")
    _require_list(packet, "preserved_runs", "run-family packet")
    _require_mapping(packet, "currentness_status", "run-family packet")
    _require_mapping(packet, "forced_system_pressure_signals", "run-family packet")
    _require_mapping(packet, "non_claims", "run-family packet")
    return packet


def _read_preserved_run_status_packet(path: Path) -> dict[str, Any]:
    packet = _read_json_object(path, "preserved-run status packet")
    _require_mapping(packet, "status_packet_metadata", "preserved-run status packet")
    _require_mapping(packet, "canonical_execution_line", "preserved-run status packet")
    _require_mapping(packet, "authority_reference", "preserved-run status packet")
    _require_list(packet, "preserved_run_status_entries", "preserved-run status packet")
    _require_mapping(packet, "aggregate_status_counts", "preserved-run status packet")
    _require_mapping(
        packet,
        "forced_system_pressure_signals",
        "preserved-run status packet",
    )
    _require_mapping(packet, "non_claims", "preserved-run status packet")
    return packet


def _discover_json_artifacts(root: Path, pattern: str, label: str) -> list[Path]:
    root_path = _require_directory(root, label)
    try:
        return sorted(path for path in root_path.glob(pattern) if path.is_file())
    except OSError as exc:
        raise CurrentGoverningPacketError(
            f"Could not read {label}: {_display_path(root_path)}"
        ) from exc


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_relative_path(path)
    if not file_path.exists():
        raise CurrentGoverningPacketError(
            f"{label.title()} is missing: {_display_path(file_path)}"
        )
    if not file_path.is_file():
        raise CurrentGoverningPacketError(
            f"{label.title()} path is not a file: {_display_path(file_path)}"
        )
    try:
        parsed = json.loads(file_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise CurrentGoverningPacketError(
            f"Could not read {label}: {_display_path(file_path)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentGoverningPacketError(
            f"{label.title()} is not valid JSON: {_display_path(file_path)}"
        ) from exc
    if not isinstance(parsed, dict):
        raise CurrentGoverningPacketError(f"{label.title()} must be a JSON object")
    return parsed


def _require_directory(root: Path, label: str) -> Path:
    path = _repo_relative_path(root)
    if not path.exists():
        raise CurrentGoverningPacketError(
            f"{label.title()} does not exist: {_display_path(path)}"
        )
    if not path.is_dir():
        raise CurrentGoverningPacketError(
            f"{label.title()} is not a directory: {_display_path(path)}"
        )
    return path


def _require_matching_optional_paths(values: tuple[Any, ...], label: str) -> None:
    resolved: list[Path | None] = []
    for value in values:
        if value is None:
            resolved.append(None)
            continue
        if not isinstance(value, str) or not value:
            raise CurrentGoverningPacketError(f"{label} must be a string or null")
        resolved.append(_resolve_path_text(value, base_dir=_repo_root()))

    if any(value is None for value in resolved):
        raise CurrentGoverningPacketError(f"{label} is missing from one artifact")
    first = resolved[0]
    if any(value != first for value in resolved[1:]):
        raise CurrentGoverningPacketError(f"{label} does not align across artifacts")


def _same_path(left: str | Path, right: str | Path) -> bool:
    left_path = (
        left.resolve()
        if isinstance(left, Path)
        else _resolve_path_text(left, base_dir=_repo_root())
    )
    right_path = (
        right.resolve()
        if isinstance(right, Path)
        else _resolve_path_text(right, base_dir=_repo_root())
    )
    return left_path == right_path


def _resolve_path_text(path_text: str, *, base_dir: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()
    candidates = (
        (base_dir / path).resolve(),
        (_repo_root() / path).resolve(),
    )
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[-1]


def _core_execution_file(packet: Mapping[str, Any], label: str) -> str:
    canonical = _require_mapping(packet, "canonical_execution_line", label)
    return _require_string(
        canonical,
        "core_execution_file",
        f"{label}.canonical_execution_line",
    )


def _next_default_governing_packet_path() -> Path:
    output_root = _repo_root() / CURRENT_GOVERNING_PACKET_ROOT
    candidate = output_root / "current_governing_packet.json"
    if not candidate.exists():
        return candidate
    for suffix in range(1, 1000):
        candidate = output_root / f"current_governing_packet_{suffix:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentGoverningPacketError(
        "Could not allocate a fresh current-governing packet path"
    )


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_relative_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (_repo_root() / path).resolve()


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(_repo_root()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, Path):
        return _display_path(value)
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, set):
        return sorted((_json_ready(item) for item in value), key=repr)
    raise TypeError(f"Unsupported JSON value type: {type(value).__name__}")


def _require_mapping(value: Any, key: str, context: str | None = None) -> Mapping[str, Any]:
    if context is None:
        context = key
        if isinstance(value, Mapping):
            return value
    else:
        if isinstance(value, Mapping):
            item = value.get(key)
            if isinstance(item, Mapping):
                return item
            raise CurrentGoverningPacketError(f"{context}.{key} must be an object")
    raise CurrentGoverningPacketError(f"{context} must be an object")


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise CurrentGoverningPacketError(f"{context}.{key} must be a list")
    return value


def _string_list(mapping: Mapping[str, Any], key: str, context: str) -> list[str]:
    values = _require_list(mapping, key, context)
    strings: list[str] = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or not value:
            raise CurrentGoverningPacketError(
                f"{context}.{key}[{index}] must be a non-empty string"
            )
        strings.append(value)
    return strings


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise CurrentGoverningPacketError(f"{context}.{key} must be a non-empty string")
    return value


def _optional_string(mapping: Mapping[str, Any], key: str, context: str) -> str | None:
    value = mapping.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise CurrentGoverningPacketError(f"{context}.{key} must be a string or null")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise CurrentGoverningPacketError(f"{context}.{key} must be an integer")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise CurrentGoverningPacketError(f"{context}.{key} must be a boolean")
    return value
