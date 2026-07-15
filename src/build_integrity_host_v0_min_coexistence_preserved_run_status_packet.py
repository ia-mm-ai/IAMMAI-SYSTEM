"""Build a bounded preserved-run status packet for v0-min coexistence.

This module reads one current execution-authority resolution artifact and one
run-family packet artifact, verifies that they correspond, and assigns each
preserved source run exactly one bounded status role. The result is an
additive local engineering artifact only.

It does not replay source actions into a live host, merge preserved runs,
invent persistence or registry doctrine, complete continuity, or promote
bounded authority resolution into final system governance.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from build_integrity_host_v0_min_coexistence_run_family_packet import (
    RunFamilyPacketError,
    build_run_family_summary,
)
from resolve_current_integrity_host_v0_min_coexistence_execution_authority import (
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

STATUS_PACKET_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_PRESERVED_RUN_STATUS_PACKET"
)
STATUS_PACKET_VERSION = "0.1.0"

ROLE_CURRENT_AUTHORITY = "CURRENT_EXECUTION_AUTHORITY"
ROLE_ELIGIBLE_NON_AUTHORITY = "PRESERVED_ELIGIBLE_NON_AUTHORITY"
ROLE_INELIGIBLE = "PRESERVED_INELIGIBLE"

NON_CLAIM_DEFAULTS = {
    "continuity_completed": False,
    "standing_upgraded": False,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
    "minimum_lawful_system_completed": False,
    "final_system_identity_completed": False,
    "final_preserved_run_governance_completed": False,
}


class PreservedRunStatusPacketError(RuntimeError):
    """Raised when a bounded preserved-run status packet cannot be built."""


def discover_latest_authority_resolution(root: Path) -> Path:
    """Return the lexically latest authority-resolution artifact."""

    artifacts = _discover_json_artifacts(
        root,
        "current_execution_authority_resolution*.json",
        "execution-authority resolution root",
    )
    if not artifacts:
        raise PreservedRunStatusPacketError(
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
        raise PreservedRunStatusPacketError(
            f"No run-family packet artifact found under {_display_path(_repo_relative_path(root))}"
        )
    return artifacts[-1]


def build_preserved_run_status_packet() -> dict[str, Any]:
    """Build one bounded preserved-run status packet from existing artifacts."""

    authority_path = discover_latest_authority_resolution(
        EXECUTION_AUTHORITY_RESOLUTION_ROOT
    )
    family_path = discover_latest_run_family_packet(RUN_FAMILY_PACKET_ROOT)

    authority = _read_authority_resolution(authority_path)
    family = _read_run_family_packet(family_path)
    authority_summary = _authority_summary(authority)
    family_summary = _family_summary(family)

    _verify_artifact_correspondence(
        authority,
        family,
        authority_summary,
        family_summary,
        authority_path,
    )

    non_claims = _non_claims(authority, family)
    entries = _preserved_run_status_entries(family, authority_summary, non_claims)
    aggregate_counts = _aggregate_status_counts(entries)

    return {
        "status_packet_metadata": {
            "status_packet_type": STATUS_PACKET_TYPE,
            "status_packet_version": STATUS_PACKET_VERSION,
            "generated_at": _utc_timestamp(),
            "builder_module": __name__,
        },
        "canonical_execution_line": _canonical_execution_line(family),
        "authority_reference": _authority_reference(
            authority,
            authority_summary,
            authority_path,
            family_path,
        ),
        "preserved_run_status_entries": entries,
        "aggregate_status_counts": aggregate_counts,
        "forced_system_pressure_signals": _pressure_signals(authority, family),
        "non_claims": non_claims,
    }


def write_preserved_run_status_packet(
    packet: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one UTF-8 JSON preserved-run status packet without overwriting."""

    if not isinstance(packet, Mapping):
        raise PreservedRunStatusPacketError("Preserved-run status packet must be a mapping")

    target = (
        _next_default_status_packet_path()
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise PreservedRunStatusPacketError(
            f"Refusing to overwrite preserved-run status packet: {_display_path(target)}"
        )
    target.write_text(_json_text(packet), encoding="utf-8")
    return target


def build_preserved_run_status_summary(
    packet: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one status packet."""

    canonical = _require_mapping(
        packet,
        "canonical_execution_line",
        "preserved-run status packet",
    )
    authority = _require_mapping(
        packet,
        "authority_reference",
        "preserved-run status packet",
    )
    aggregate = _require_mapping(
        packet,
        "aggregate_status_counts",
        "preserved-run status packet",
    )
    non_claims = _require_mapping(packet, "non_claims", "preserved-run status packet")

    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "preserved-run status packet.canonical_execution_line",
        ),
        "preserved_run_count": _require_int(
            aggregate,
            "preserved_run_count",
            "preserved-run status packet.aggregate_status_counts",
        ),
        "eligible_run_count": _require_int(
            aggregate,
            "eligible_run_count",
            "preserved-run status packet.aggregate_status_counts",
        ),
        "current_authority_run_count": _require_int(
            aggregate,
            "current_authority_run_count",
            "preserved-run status packet.aggregate_status_counts",
        ),
        "preserved_eligible_non_authority_count": _require_int(
            aggregate,
            "preserved_eligible_non_authority_count",
            "preserved-run status packet.aggregate_status_counts",
        ),
        "preserved_ineligible_count": _require_int(
            aggregate,
            "preserved_ineligible_count",
            "preserved-run status packet.aggregate_status_counts",
        ),
        "selected_current_authority_source_run_path": authority.get(
            "selected_source_run_path"
        ),
        "authority_decision": _require_string(
            authority,
            "authority_decision",
            "preserved-run status packet.authority_reference",
        ),
        "authority_decision_reason": _require_string(
            authority,
            "authority_decision_reason",
            "preserved-run status packet.authority_reference",
        ),
        "non_claims": {
            key: _require_bool(
                non_claims,
                key,
                "preserved-run status packet.non_claims",
            )
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _preserved_run_status_entries(
    family: Mapping[str, Any],
    authority_summary: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    preserved_runs = _require_list(family, "preserved_runs", "run-family packet")
    selected_source = authority_summary.get("selected_source_run_directory_path")
    selected_source_path = _optional_path(selected_source)
    entries: list[dict[str, Any]] = []

    for index, value in enumerate(preserved_runs):
        run = _require_mapping(value, f"run-family packet.preserved_runs[{index}]")
        source_path_text = _require_string(
            run,
            "source_run_directory_path",
            f"run-family packet.preserved_runs[{index}]",
        )
        candidate_eligible = _require_bool(
            run,
            "candidate_eligible",
            f"run-family packet.preserved_runs[{index}]",
        )
        current_authority = _require_bool(
            run,
            "current_authority",
            f"run-family packet.preserved_runs[{index}]",
        )
        ineligibility_reasons = _string_list(
            run,
            "ineligibility_reasons",
            f"run-family packet.preserved_runs[{index}]",
        )
        preservation_signals = _require_mapping(
            run,
            "preservation_signals",
            f"run-family packet.preserved_runs[{index}]",
        )

        role = _status_role(
            source_path_text,
            selected_source_path,
            current_authority,
            candidate_eligible,
            ineligibility_reasons,
        )

        entries.append(
            {
                "source_run_directory_path": source_path_text,
                "source_manifest_path": _require_string(
                    run,
                    "source_manifest_path",
                    f"run-family packet.preserved_runs[{index}]",
                ),
                "matched_ingress_run_path": _optional_string(
                    run,
                    "matched_ingress_run_path",
                    f"run-family packet.preserved_runs[{index}]",
                ),
                "matched_comparison_artifact_path": _optional_string(
                    run,
                    "matched_comparison_artifact_path",
                    f"run-family packet.preserved_runs[{index}]",
                ),
                "status_role": role,
                "current_authority": role == ROLE_CURRENT_AUTHORITY,
                "candidate_eligible": candidate_eligible,
                "status_reason": _status_reason(role),
                "ineligibility_reasons": ineligibility_reasons,
                "preservation_signals": {
                    "source_preserved": _require_bool(
                        preservation_signals,
                        "source_preserved",
                        f"run-family packet.preserved_runs[{index}].preservation_signals",
                    ),
                    "ingress_preserved": _require_bool(
                        preservation_signals,
                        "ingress_preserved",
                        f"run-family packet.preserved_runs[{index}].preservation_signals",
                    ),
                    "comparison_preserved": _require_bool(
                        preservation_signals,
                        "comparison_preserved",
                        f"run-family packet.preserved_runs[{index}].preservation_signals",
                    ),
                    "authority_candidate_visible": _require_bool(
                        preservation_signals,
                        "authority_candidate_visible",
                        f"run-family packet.preserved_runs[{index}].preservation_signals",
                    ),
                },
                "non_claims": dict(non_claims),
            }
        )

    current_count = sum(
        1 for entry in entries if entry["status_role"] == ROLE_CURRENT_AUTHORITY
    )
    if current_count > 1:
        raise PreservedRunStatusPacketError(
            "More than one preserved run was assigned current authority"
        )
    if selected_source_path is not None and current_count != 1:
        raise PreservedRunStatusPacketError(
            "Authority resolution selected a source run, but no preserved run matched it"
        )
    return entries


def _status_role(
    source_path_text: str,
    selected_source_path: Path | None,
    current_authority: bool,
    candidate_eligible: bool,
    ineligibility_reasons: list[str],
) -> str:
    source_path = _resolve_path_text(source_path_text, base_dir=_repo_root())
    selected = selected_source_path is not None and source_path == selected_source_path

    if selected:
        if not candidate_eligible:
            raise PreservedRunStatusPacketError(
                "Selected authority run is not marked eligible in the family packet"
            )
        if ineligibility_reasons:
            raise PreservedRunStatusPacketError(
                "Selected authority run carries ineligibility reasons"
            )
        if not current_authority:
            raise PreservedRunStatusPacketError(
                "Selected authority run is not marked current_authority in the family packet"
            )
        return ROLE_CURRENT_AUTHORITY

    if current_authority:
        raise PreservedRunStatusPacketError(
            "A non-selected preserved run is marked current_authority"
        )
    if candidate_eligible and not ineligibility_reasons:
        return ROLE_ELIGIBLE_NON_AUTHORITY
    return ROLE_INELIGIBLE


def _status_reason(role: str) -> str:
    if role == ROLE_CURRENT_AUTHORITY:
        return "SELECTED_BY_EXPLICIT_EXECUTION_AUTHORITY_RESOLUTION"
    if role == ROLE_ELIGIBLE_NON_AUTHORITY:
        return "ELIGIBLE_PRESERVED_RUN_NOT_SELECTED_AS_CURRENT_AUTHORITY"
    return "PRESERVED_RUN_HAS_INELIGIBILITY_REASONS_OR_IS_NOT_ELIGIBLE"


def _aggregate_status_counts(entries: list[Mapping[str, Any]]) -> dict[str, int]:
    current_count = sum(
        1 for entry in entries if entry.get("status_role") == ROLE_CURRENT_AUTHORITY
    )
    eligible_non_authority_count = sum(
        1
        for entry in entries
        if entry.get("status_role") == ROLE_ELIGIBLE_NON_AUTHORITY
    )
    ineligible_count = sum(
        1 for entry in entries if entry.get("status_role") == ROLE_INELIGIBLE
    )
    eligible_count = current_count + eligible_non_authority_count

    return {
        "preserved_run_count": len(entries),
        "eligible_run_count": eligible_count,
        "current_authority_run_count": current_count,
        "preserved_eligible_non_authority_count": eligible_non_authority_count,
        "preserved_ineligible_count": ineligible_count,
    }


def _verify_artifact_correspondence(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    authority_summary: Mapping[str, Any],
    family_summary: Mapping[str, Any],
    authority_path: Path,
) -> None:
    authority_core = _require_string(
        _require_mapping(authority, "canonical_execution_line", "authority resolution"),
        "core_execution_file",
        "authority resolution.canonical_execution_line",
    )
    family_core = _require_string(
        _require_mapping(family, "canonical_execution_line", "run-family packet"),
        "core_execution_file",
        "run-family packet.canonical_execution_line",
    )
    if authority_core != family_core:
        raise PreservedRunStatusPacketError(
            "Authority resolution and run-family packet canonical core files do not match"
        )

    family_authority = _require_mapping(
        family,
        "authority_reference",
        "run-family packet",
    )
    family_resolution_path = _require_string(
        family_authority,
        "resolution_artifact_path",
        "run-family packet.authority_reference",
    )
    if not _same_path(family_resolution_path, authority_path):
        raise PreservedRunStatusPacketError(
            "Run-family packet does not reference the selected authority artifact"
        )

    if not _nullable_same_path(
        authority_summary.get("selected_source_run_directory_path"),
        family_summary.get("current_authority_source_run_path"),
    ):
        raise PreservedRunStatusPacketError(
            "Selected source run path does not align between authority and family artifacts"
        )
    if not _nullable_same_path(
        authority_summary.get("selected_ingress_run_directory_path"),
        family_summary.get("current_authority_ingress_run_path"),
    ):
        raise PreservedRunStatusPacketError(
            "Selected ingress run path does not align between authority and family artifacts"
        )

    authority_eligible = _require_int(
        _require_mapping(authority, "authority_decision", "authority resolution"),
        "eligible_candidate_count",
        "authority resolution.authority_decision",
    )
    family_eligible = _require_int(
        family_authority,
        "eligible_candidate_count",
        "run-family packet.authority_reference",
    )
    if authority_eligible != family_eligible:
        raise PreservedRunStatusPacketError(
            "Eligible candidate count does not align between authority and family artifacts"
        )

    preserved_run_count = _require_int(
        _require_mapping(family, "currentness_status", "run-family packet"),
        "preserved_run_count",
        "run-family packet.currentness_status",
    )
    if preserved_run_count < authority_eligible:
        raise PreservedRunStatusPacketError(
            "Run-family preserved run count is smaller than eligible candidate count"
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
) -> dict[str, Any]:
    decision = _require_mapping(authority, "authority_decision", "authority resolution")
    return {
        "authority_artifact_path": _display_path(authority_path),
        "run_family_packet_artifact_path": _display_path(family_path),
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
) -> dict[str, Any]:
    signals = _json_ready(
        dict(
            _require_mapping(
                family,
                "forced_system_pressure_signals",
                "run-family packet",
            )
        )
    )
    authority_signals = _require_mapping(
        authority,
        "forced_system_pressure_signals",
        "authority resolution",
    )
    for key, value in authority_signals.items():
        signals.setdefault(str(key), _json_ready(value))
    signals["preserved_run_status_pressure"] = (
        "Preserved runs now need explicit bounded roles so current authority, "
        "eligible non-authority runs, and ineligible runs are not collapsed "
        "into lexical recency or final governance."
    )
    return signals


def _non_claims(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for label, artifact in (
        ("authority resolution", authority),
        ("run-family packet", family),
    ):
        incoming = _require_mapping(artifact, "non_claims", label)
        for key in NON_CLAIM_DEFAULTS:
            if key in incoming:
                value = _require_bool(incoming, key, f"{label}.non_claims")
                if value is not False:
                    raise PreservedRunStatusPacketError(
                        f"{label}.non_claims.{key} must remain false"
                    )
                non_claims[key] = False
    return non_claims


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except ExecutionAuthorityResolutionError as exc:
        raise PreservedRunStatusPacketError(
            "Authority resolution artifact is malformed"
        ) from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except RunFamilyPacketError as exc:
        raise PreservedRunStatusPacketError(
            "Run-family packet artifact is malformed"
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


def _discover_json_artifacts(root: Path, pattern: str, label: str) -> list[Path]:
    root_path = _require_directory(root, label)
    try:
        return sorted(path for path in root_path.glob(pattern) if path.is_file())
    except OSError as exc:
        raise PreservedRunStatusPacketError(
            f"Could not read {label}: {_display_path(root_path)}"
        ) from exc


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_relative_path(path)
    if not file_path.exists():
        raise PreservedRunStatusPacketError(
            f"{label.title()} is missing: {_display_path(file_path)}"
        )
    if not file_path.is_file():
        raise PreservedRunStatusPacketError(
            f"{label.title()} path is not a file: {_display_path(file_path)}"
        )
    try:
        parsed = json.loads(file_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise PreservedRunStatusPacketError(
            f"Could not read {label}: {_display_path(file_path)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise PreservedRunStatusPacketError(
            f"{label.title()} is not valid JSON: {_display_path(file_path)}"
        ) from exc
    if not isinstance(parsed, dict):
        raise PreservedRunStatusPacketError(f"{label.title()} must be a JSON object")
    return parsed


def _require_directory(root: Path, label: str) -> Path:
    path = _repo_relative_path(root)
    if not path.exists():
        raise PreservedRunStatusPacketError(
            f"{label.title()} does not exist: {_display_path(path)}"
        )
    if not path.is_dir():
        raise PreservedRunStatusPacketError(
            f"{label.title()} is not a directory: {_display_path(path)}"
        )
    return path


def _optional_path(value: Any) -> Path | None:
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise PreservedRunStatusPacketError("Optional authority path must be a string or null")
    return _resolve_path_text(value, base_dir=_repo_root())


def _nullable_same_path(left: Any, right: Any) -> bool:
    if left is None and right is None:
        return True
    if left is None or right is None:
        return False
    if not isinstance(left, str) or not isinstance(right, str):
        return False
    return _same_path(left, right)


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


def _next_default_status_packet_path() -> Path:
    output_root = _repo_root() / PRESERVED_RUN_STATUS_PACKET_ROOT
    candidate = output_root / "current_preserved_run_status_packet.json"
    if not candidate.exists():
        return candidate
    for suffix in range(1, 1000):
        candidate = output_root / f"current_preserved_run_status_packet_{suffix:03d}.json"
        if not candidate.exists():
            return candidate
    raise PreservedRunStatusPacketError(
        "Could not allocate a fresh preserved-run status packet path"
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
            raise PreservedRunStatusPacketError(f"{context}.{key} must be an object")
    raise PreservedRunStatusPacketError(f"{context} must be an object")


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise PreservedRunStatusPacketError(f"{context}.{key} must be a list")
    return value


def _string_list(mapping: Mapping[str, Any], key: str, context: str) -> list[str]:
    values = _require_list(mapping, key, context)
    strings: list[str] = []
    for index, value in enumerate(values):
        if not isinstance(value, str) or not value:
            raise PreservedRunStatusPacketError(
                f"{context}.{key}[{index}] must be a non-empty string"
            )
        strings.append(value)
    return strings


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise PreservedRunStatusPacketError(f"{context}.{key} must be a non-empty string")
    return value


def _optional_string(mapping: Mapping[str, Any], key: str, context: str) -> str | None:
    value = mapping.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or not value:
        raise PreservedRunStatusPacketError(f"{context}.{key} must be a string or null")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise PreservedRunStatusPacketError(f"{context}.{key} must be an integer")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise PreservedRunStatusPacketError(f"{context}.{key} must be a boolean")
    return value
