"""Build a bounded preserved-run family packet for v0-min coexistence.

This module reads preserved source runs, receiving-ingress runs,
source-to-ingress comparison artifacts, and one current execution-authority
resolution artifact. It emits one additive run-family packet that makes the
current canonical execution line, preserved run family, and explicit current
execution authority visible without replaying, merging, or claiming continuity
completion.

The packet is a local engineering surface only. It is not protocol law,
persistence architecture, registry doctrine, cross-host continuity completion,
or a generic governance framework.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from resolve_current_integrity_host_v0_min_coexistence_execution_authority import (
    DECISION_RESOLVED,
    ExecutionAuthorityResolutionError,
    build_execution_authority_summary,
)


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
INGRESS_RUNS_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiving_ingress_runs"
)
SOURCE_INGRESS_COMPARISON_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_source_ingress_comparisons"
)
EXECUTION_AUTHORITY_RESOLUTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_execution_authority"
)
RUN_FAMILY_PACKET_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_run_family_packets"
)

FAMILY_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_RUN_FAMILY_PACKET"
FAMILY_VERSION = "0.1.0"

NON_CLAIM_DEFAULTS = {
    "continuity_completed": False,
    "standing_upgraded": False,
    "replayed_into_live_host": False,
    "merged_into_local_state": False,
    "minimum_lawful_system_completed": False,
    "final_system_identity_completed": False,
}


class RunFamilyPacketError(RuntimeError):
    """Raised when a bounded run-family packet cannot be built."""


def build_run_family_packet() -> dict[str, Any]:
    """Build one bounded run-family packet from preserved local artifacts."""

    source_runs = _discover_run_directories(SOURCE_RUNS_ROOT, "source run")
    ingress_runs = _discover_run_directories(INGRESS_RUNS_ROOT, "ingress run")
    comparisons = _discover_comparison_artifacts(SOURCE_INGRESS_COMPARISON_ROOT)
    authority_path = _find_current_authority_resolution_artifact(
        EXECUTION_AUTHORITY_RESOLUTION_ROOT
    )
    authority_resolution = _read_authority_resolution(authority_path)
    authority_summary = _authority_summary(authority_resolution)

    source_manifests = {
        source_run: _read_source_manifest(source_run) for source_run in source_runs
    }
    ingress_manifests = {
        ingress_run: _read_ingress_manifest(ingress_run) for ingress_run in ingress_runs
    }
    comparison_artifacts = {
        path: _read_source_ingress_comparison(path) for path in comparisons
    }

    canonical = _canonical_execution_line(authority_resolution)
    decision = _require_mapping(
        authority_resolution,
        "authority_decision",
        "authority resolution",
    )
    candidate_runs = _preserved_runs(
        source_runs,
        source_manifests,
        ingress_manifests,
        comparison_artifacts,
        authority_resolution,
        authority_summary,
    )
    eligible_count = _require_int(
        decision,
        "eligible_candidate_count",
        "authority resolution.authority_decision",
    )

    return {
        "family_metadata": {
            "family_type": FAMILY_TYPE,
            "family_version": FAMILY_VERSION,
            "generated_at": _utc_timestamp(),
            "builder_module": __name__,
        },
        "canonical_execution_line": canonical,
        "authority_reference": {
            "resolution_artifact_path": _display_path(authority_path),
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
            "selected_source_run_path": decision.get(
                "selected_source_run_directory_path"
            ),
            "selected_ingress_run_path": decision.get(
                "selected_ingress_run_directory_path"
            ),
            "selected_comparison_artifact_path": decision.get(
                "selected_comparison_artifact_path"
            ),
            "candidate_run_count": _require_int(
                decision,
                "candidate_run_count",
                "authority resolution.authority_decision",
            ),
            "eligible_candidate_count": eligible_count,
        },
        "preserved_runs": candidate_runs,
        "currentness_status": {
            "current_execution_authority_exists": (
                authority_summary["decision"] == DECISION_RESOLVED
            ),
            "current_execution_authority_source_run_path": authority_summary[
                "selected_source_run_directory_path"
            ],
            "current_execution_authority_ingress_run_path": authority_summary[
                "selected_ingress_run_directory_path"
            ],
            "current_execution_authority_resolved_by_explicit_checks": (
                authority_summary["decision"] == DECISION_RESOLVED
                and bool(authority_summary["selected_source_run_directory_path"])
                and bool(authority_summary["selected_ingress_run_directory_path"])
                and bool(authority_summary["selected_comparison_artifact_path"])
            ),
            "latest_emitted_is_not_authority_by_default": True,
            "preserved_run_count": len(candidate_runs),
            "eligible_run_count": eligible_count,
        },
        "forced_system_pressure_signals": _pressure_signals(authority_resolution),
        "non_claims": _non_claims(authority_resolution),
    }


def write_run_family_packet(
    packet: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one UTF-8 JSON run-family packet without overwriting."""

    if not isinstance(packet, Mapping):
        raise RunFamilyPacketError("Run-family packet must be a mapping")

    target = (
        _next_default_packet_path()
        if output_path is None
        else _repo_relative_path(Path(output_path))
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise RunFamilyPacketError(
            f"Refusing to overwrite run-family packet: {_display_path(target)}"
        )
    target.write_text(_json_text(packet), encoding="utf-8")
    return target


def build_run_family_summary(packet: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one run-family packet."""

    canonical = _require_mapping(packet, "canonical_execution_line", "run family packet")
    authority = _require_mapping(packet, "authority_reference", "run family packet")
    status = _require_mapping(packet, "currentness_status", "run family packet")
    non_claims = _require_mapping(packet, "non_claims", "run family packet")

    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "run family packet.canonical_execution_line",
        ),
        "preserved_run_count": _require_int(
            status,
            "preserved_run_count",
            "run family packet.currentness_status",
        ),
        "eligible_run_count": _require_int(
            status,
            "eligible_run_count",
            "run family packet.currentness_status",
        ),
        "current_authority_source_run_path": authority.get(
            "selected_source_run_path"
        ),
        "current_authority_ingress_run_path": authority.get(
            "selected_ingress_run_path"
        ),
        "authority_decision": _require_string(
            authority,
            "authority_decision",
            "run family packet.authority_reference",
        ),
        "authority_decision_reason": _require_string(
            authority,
            "authority_decision_reason",
            "run family packet.authority_reference",
        ),
        "non_claims": {
            key: _require_bool(non_claims, key, "run family packet.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _preserved_runs(
    source_runs: list[Path],
    source_manifests: Mapping[Path, Mapping[str, Any]],
    ingress_manifests: Mapping[Path, Mapping[str, Any]],
    comparison_artifacts: Mapping[Path, Mapping[str, Any]],
    authority_resolution: Mapping[str, Any],
    authority_summary: Mapping[str, Any],
) -> list[dict[str, Any]]:
    resolution_candidates = _resolution_candidates_by_source(authority_resolution)
    selected_source_path = _optional_resolved_path(
        authority_summary.get("selected_source_run_directory_path"),
        base_dir=_repo_root(),
    )

    if selected_source_path is not None and selected_source_path not in source_runs:
        raise RunFamilyPacketError(
            "Authority resolution selects a source run that is not preserved locally"
        )

    entries: list[dict[str, Any]] = []
    for source_run in source_runs:
        manifest = source_manifests[source_run]
        candidate = resolution_candidates.get(source_run)
        matched_ingress = _candidate_path(candidate, "matched_ingress_run_directory_path")
        matched_comparison = _candidate_path(candidate, "matched_comparison_artifact_path")

        source_count = _require_int(manifest, "scenario_count", "source manifest")
        ingress_preserved = matched_ingress in ingress_manifests
        comparison_preserved = matched_comparison in comparison_artifacts

        entries.append(
            {
                "source_run_directory_path": _display_path(source_run),
                "source_manifest_path": _display_path(source_run / "manifest.json"),
                "scenario_count": source_count,
                "matched_ingress_run_path": (
                    _display_path(matched_ingress)
                    if matched_ingress is not None
                    else None
                ),
                "matched_comparison_artifact_path": (
                    _display_path(matched_comparison)
                    if matched_comparison is not None
                    else None
                ),
                "current_authority": (
                    selected_source_path is not None
                    and source_run == selected_source_path
                ),
                "candidate_eligible": (
                    bool(candidate.get("eligible")) if candidate is not None else False
                ),
                "ineligibility_reasons": (
                    list(_require_list(candidate, "ineligibility_reasons", "candidate"))
                    if candidate is not None
                    else ["source run is not present in authority resolution candidates"]
                ),
                "preservation_signals": {
                    "source_preserved": True,
                    "ingress_preserved": ingress_preserved,
                    "comparison_preserved": comparison_preserved,
                    "authority_candidate_visible": candidate is not None,
                },
            }
        )

    return entries


def _resolution_candidates_by_source(
    authority_resolution: Mapping[str, Any],
) -> dict[Path, Mapping[str, Any]]:
    candidates = _require_list(
        authority_resolution,
        "candidate_runs",
        "authority resolution",
    )
    by_source: dict[Path, Mapping[str, Any]] = {}
    for index, value in enumerate(candidates):
        candidate = _require_mapping(value, f"authority resolution.candidate_runs[{index}]")
        source_text = _require_string(
            candidate,
            "source_run_directory_path",
            f"authority resolution.candidate_runs[{index}]",
        )
        source_path = _resolve_path_text(source_text, base_dir=_repo_root())
        by_source[source_path] = candidate
    return by_source


def _canonical_execution_line(
    authority_resolution: Mapping[str, Any],
) -> dict[str, Any]:
    canonical = _require_mapping(
        authority_resolution,
        "canonical_execution_line",
        "authority resolution",
    )
    derivative = _require_list(
        canonical,
        "derivative_support_scope",
        "authority resolution.canonical_execution_line",
    )
    predecessors = _require_list(
        canonical,
        "lineage_predecessor_files",
        "authority resolution.canonical_execution_line",
    )

    return {
        "core_execution_file": _require_string(
            canonical,
            "core_execution_file",
            "authority resolution.canonical_execution_line",
        ),
        "derivative_support_scope": [
            _require_list_string(
                value,
                f"authority resolution.canonical_execution_line.derivative_support_scope[{index}]",
            )
            for index, value in enumerate(derivative)
        ],
        "lineage_predecessor_files": [
            _require_list_string(
                value,
                f"authority resolution.canonical_execution_line.lineage_predecessor_files[{index}]",
            )
            for index, value in enumerate(predecessors)
        ],
    }


def _pressure_signals(authority_resolution: Mapping[str, Any]) -> dict[str, Any]:
    incoming = _require_mapping(
        authority_resolution,
        "forced_system_pressure_signals",
        "authority resolution",
    )
    signals = _json_ready(dict(incoming))
    signals["bounded_run_family_system_identity_pressure"] = (
        "Preserved source runs, ingress runs, comparisons, and authority "
        "resolution now need one bounded family surface without becoming "
        "continuity completion or final system governance."
    )
    return signals


def _non_claims(authority_resolution: Mapping[str, Any]) -> dict[str, bool]:
    incoming = _require_mapping(authority_resolution, "non_claims", "authority resolution")
    non_claims = dict(NON_CLAIM_DEFAULTS)
    for key in NON_CLAIM_DEFAULTS:
        if key in incoming:
            non_claims[key] = _require_bool(incoming, key, "authority resolution.non_claims")
    non_claims["final_system_identity_completed"] = False
    return non_claims


def _authority_summary(authority_resolution: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority_resolution)
    except ExecutionAuthorityResolutionError as exc:
        raise RunFamilyPacketError(
            "Authority resolution artifact is malformed"
        ) from exc


def _find_current_authority_resolution_artifact(root: Path) -> Path:
    artifacts = _discover_authority_resolution_artifacts(root)
    if not artifacts:
        raise RunFamilyPacketError(
            f"No execution-authority resolution artifact found under {_display_path(_repo_relative_path(root))}"
        )
    return artifacts[-1]


def _discover_run_directories(root: Path, label: str) -> list[Path]:
    root_path = _require_directory(root, f"{label} root")
    try:
        return sorted(
            path
            for path in root_path.iterdir()
            if path.is_dir() and path.name.startswith("run_")
        )
    except OSError as exc:
        raise RunFamilyPacketError(
            f"Could not read {label} root: {_display_path(root_path)}"
        ) from exc


def _discover_comparison_artifacts(root: Path) -> list[Path]:
    root_path = _require_directory(root, "source-to-ingress comparison root")
    try:
        return sorted(
            path
            for path in root_path.glob("*__source_ingress_comparison.json")
            if path.is_file()
        )
    except OSError as exc:
        raise RunFamilyPacketError(
            f"Could not read comparison root: {_display_path(root_path)}"
        ) from exc


def _discover_authority_resolution_artifacts(root: Path) -> list[Path]:
    root_path = _require_directory(root, "execution-authority resolution root")
    try:
        return sorted(
            path
            for path in root_path.glob("current_execution_authority_resolution*.json")
            if path.is_file()
        )
    except OSError as exc:
        raise RunFamilyPacketError(
            f"Could not read authority resolution root: {_display_path(root_path)}"
        ) from exc


def _read_source_manifest(source_run_dir: Path) -> dict[str, Any]:
    manifest = _read_json_object(source_run_dir / "manifest.json", "source manifest")
    _require_string(manifest, "generated_at", "source manifest")
    _require_string(manifest, "output_directory", "source manifest")
    scenario_count = _require_int(manifest, "scenario_count", "source manifest")
    scenarios = _require_list(manifest, "scenarios", "source manifest")
    if scenario_count != len(scenarios):
        raise RunFamilyPacketError(
            "Source manifest scenario_count does not match scenarios"
        )
    for index, entry in enumerate(scenarios):
        scenario = _require_mapping(entry, f"source manifest.scenarios[{index}]")
        _require_string(scenario, "scenario_id", f"source manifest.scenarios[{index}]")
        _require_string(scenario, "scenario_name", f"source manifest.scenarios[{index}]")
        _require_string(scenario, "description", f"source manifest.scenarios[{index}]")
        _require_string(scenario, "file_path", f"source manifest.scenarios[{index}]")
    return manifest


def _read_ingress_manifest(ingress_run_dir: Path) -> dict[str, Any]:
    manifest = _read_json_object(ingress_run_dir / "manifest.json", "ingress manifest")
    _require_mapping(manifest, "ingress_run_metadata", "ingress manifest")
    source = _require_mapping(manifest, "source_run", "ingress manifest")
    aggregate = _require_mapping(manifest, "aggregate_counts", "ingress manifest")
    status = _require_mapping(manifest, "run_status", "ingress manifest")
    entries = _require_list(manifest, "scenario_ingress_entries", "ingress manifest")
    source_count = _require_int(source, "source_scenario_count", "ingress source")
    aggregate_count = _require_int(aggregate, "scenario_count", "ingress aggregate")
    if source_count != aggregate_count or source_count != len(entries):
        raise RunFamilyPacketError("Ingress manifest scenario counts do not align")
    for key in (
        "all_packets_built",
        "all_packets_validated",
        "all_decisions_emitted",
        "continuity_completed",
        "standing_upgraded",
        "replayed_into_live_host",
        "merged_into_local_state",
    ):
        _require_bool(status, key, "ingress manifest.run_status")
    return manifest


def _read_source_ingress_comparison(path: Path) -> dict[str, Any]:
    comparison = _read_json_object(path, "source-to-ingress comparison")
    source = _require_mapping(comparison, "source_run", "comparison")
    ingress = _require_mapping(comparison, "ingress_run", "comparison")
    aggregate = _require_mapping(comparison, "aggregate_comparison", "comparison")
    _require_mapping(comparison, "comparison_metadata", "comparison")
    _require_list(comparison, "scenario_comparisons", "comparison")
    _require_bool(comparison, "all_matched", "comparison")
    _require_string(source, "source_run_directory_path", "comparison.source_run")
    _require_string(source, "source_manifest_path", "comparison.source_run")
    _require_int(source, "source_scenario_count", "comparison.source_run")
    _require_string(ingress, "ingress_run_directory_path", "comparison.ingress_run")
    _require_string(ingress, "ingress_manifest_path", "comparison.ingress_run")
    _require_int(ingress, "ingress_scenario_count", "comparison.ingress_run")
    _require_bool(aggregate, "aggregate_match", "comparison.aggregate_comparison")
    _require_list(aggregate, "mismatches", "comparison.aggregate_comparison")
    return comparison


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


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_relative_path(path)
    if not file_path.exists():
        raise RunFamilyPacketError(f"{label.title()} is missing: {_display_path(file_path)}")
    if not file_path.is_file():
        raise RunFamilyPacketError(
            f"{label.title()} path is not a file: {_display_path(file_path)}"
        )
    try:
        parsed = json.loads(file_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RunFamilyPacketError(
            f"Could not read {label}: {_display_path(file_path)}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise RunFamilyPacketError(
            f"{label.title()} is not valid JSON: {_display_path(file_path)}"
        ) from exc
    if not isinstance(parsed, dict):
        raise RunFamilyPacketError(f"{label.title()} must be a JSON object")
    return parsed


def _candidate_path(candidate: Mapping[str, Any] | None, key: str) -> Path | None:
    if candidate is None:
        return None
    value = candidate.get(key)
    if value is None:
        return None
    if not isinstance(value, str) or value == "":
        raise RunFamilyPacketError(f"Authority candidate {key} must be a string or null")
    return _resolve_path_text(value, base_dir=_repo_root())


def _optional_resolved_path(value: Any, *, base_dir: Path) -> Path | None:
    if value is None:
        return None
    if not isinstance(value, str) or value == "":
        raise RunFamilyPacketError("Selected authority path must be a string or null")
    return _resolve_path_text(value, base_dir=base_dir)


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


def _require_directory(root: Path, label: str) -> Path:
    path = _repo_relative_path(root)
    if not path.exists():
        raise RunFamilyPacketError(f"{label.title()} does not exist: {_display_path(path)}")
    if not path.is_dir():
        raise RunFamilyPacketError(
            f"{label.title()} is not a directory: {_display_path(path)}"
        )
    return path


def _next_default_packet_path() -> Path:
    output_root = _repo_root() / RUN_FAMILY_PACKET_ROOT
    candidate = output_root / "current_run_family_packet.json"
    if not candidate.exists():
        return candidate
    for suffix in range(1, 1000):
        candidate = output_root / f"current_run_family_packet_{suffix:03d}.json"
        if not candidate.exists():
            return candidate
    raise RunFamilyPacketError("Could not allocate a fresh run-family packet path")


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
            raise RunFamilyPacketError(f"{context}.{key} must be an object")
    raise RunFamilyPacketError(f"{context} must be an object")


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise RunFamilyPacketError(f"{context}.{key} must be a list")
    return value


def _require_list_string(value: Any, context: str) -> str:
    if not isinstance(value, str) or not value:
        raise RunFamilyPacketError(f"{context} must be a non-empty string")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise RunFamilyPacketError(f"{context}.{key} must be a non-empty string")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise RunFamilyPacketError(f"{context}.{key} must be an integer")
    return value


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise RunFamilyPacketError(f"{context}.{key} must be a boolean")
    return value
