"""Bounded run-level receiving ingress runner for v0-min coexistence artifacts.

This module processes one emitted source scenario run by building a receiving
packet, validation result, and ingress decision for each source scenario
artifact. It writes those receiving-side artifacts into one local run-level
output directory and returns a small manifest for inspection.

The receiving ingress run is additive engineering output only. It does not
replay source actions into a live host, merge packets into local state, define
persistence or registry law, complete continuity, or upgrade received material
into local standing.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from build_integrity_host_v0_min_coexistence_receiving_ingress_decision import (
    DECISION_RECEIVE,
    build_ingress_decision_from_packet_path,
    build_ingress_decision_summary,
)
from build_integrity_host_v0_min_coexistence_receiving_packet import (
    build_receiving_packet,
    build_receiving_packet_summary,
)
from validate_integrity_host_v0_min_coexistence_receiving_packet import (
    ReceivingPacketValidationError,
    build_validation_summary,
    validate_receiving_packet,
)


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
RECEIVING_INGRESS_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_receiving_ingress_runs"
)

INGRESS_RUN_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_RECEIVING_INGRESS_RUN"
INGRESS_RUN_VERSION = "0.1.0"


def find_latest_source_run_directory(root: Path) -> Path:
    """Return the lexically latest source ``run_*`` directory under ``root``."""

    root_path = _resolve_path(root)
    candidates = sorted(
        path for path in root_path.glob("run_*") if path.is_dir()
    )
    if not candidates:
        raise RuntimeError(f"No source run directories found under {_display_path(root_path)}")
    return candidates[-1]


def read_source_manifest(run_dir: Path) -> dict[str, Any]:
    """Read and validate the bounded source scenario run manifest."""

    source_run_dir = _resolve_path(run_dir)
    manifest_path = source_run_dir / "manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Source manifest is missing: {_display_path(manifest_path)}")
    if not manifest_path.is_file():
        raise RuntimeError(
            f"Source manifest path is not a file: {_display_path(manifest_path)}"
        )

    try:
        parsed = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"Source manifest is not valid JSON: {_display_path(manifest_path)}"
        ) from exc

    if not isinstance(parsed, dict):
        raise RuntimeError("Source manifest must be a JSON object")

    _validate_source_manifest(parsed)
    return parsed


def run_receiving_ingress_for_source_run(source_run_dir: Path) -> dict[str, Any]:
    """Build receiving packet and decision artifacts for one source run."""

    run_dir = _resolve_path(source_run_dir)
    manifest = read_source_manifest(run_dir)
    output_dir = _make_output_dir(run_dir)

    scenario_entries = tuple(
        _process_scenario_entry(run_dir, output_dir, entry)
        for entry in _scenario_entries(manifest)
    )

    aggregate_counts = _aggregate_counts(scenario_entries)
    return {
        "ingress_run_metadata": {
            "ingress_run_type": INGRESS_RUN_TYPE,
            "ingress_run_version": INGRESS_RUN_VERSION,
            "generated_at": _utc_timestamp(),
            "runner_module": __name__,
            "output_run_directory": _display_path(output_dir),
        },
        "source_run": {
            "source_run_directory_path": _display_path(run_dir),
            "source_manifest_path": _display_path(run_dir / "manifest.json"),
            "source_scenario_count": _require_int(
                manifest,
                "scenario_count",
                "source manifest",
            ),
            "source_generated_at": _require_string(
                manifest,
                "generated_at",
                "source manifest",
            ),
        },
        "scenario_ingress_entries": list(scenario_entries),
        "aggregate_counts": aggregate_counts,
        "run_status": {
            "all_packets_built": all(
                _path_exists(entry["receiving_packet_path"])
                for entry in scenario_entries
            ),
            "all_packets_validated": len(scenario_entries)
            == aggregate_counts["scenario_count"],
            "all_decisions_emitted": all(
                _path_exists(entry["ingress_decision_path"])
                for entry in scenario_entries
            ),
            "continuity_completed": False,
            "standing_upgraded": False,
            "replayed_into_live_host": False,
            "merged_into_local_state": False,
        },
    }


def write_ingress_run_manifest(manifest: dict[str, Any], output_path: Path) -> Path:
    """Write one run-level ingress manifest without overwriting."""

    return _write_json(_resolve_output_path(output_path), manifest)


def main() -> None:
    """Process the latest emitted source scenario run and print a short summary."""

    source_run_dir = find_latest_source_run_directory(_repo_root() / SOURCE_RUNS_ROOT)
    manifest = run_receiving_ingress_for_source_run(source_run_dir)
    output_dir = _path_from_display(
        _require_string(
            _require_mapping(
                manifest,
                "ingress_run_metadata",
                "ingress manifest",
            ),
            "output_run_directory",
            "ingress_run_metadata",
        )
    )
    manifest_path = write_ingress_run_manifest(manifest, output_dir / "manifest.json")

    aggregate = _require_mapping(manifest, "aggregate_counts", "ingress manifest")
    print(f"Source run directory: {_display_path(source_run_dir)}")
    print(f"Scenarios processed: {aggregate['scenario_count']}")
    print(
        "Validation passed scenarios: "
        f"{aggregate['validation_passed_scenario_count']}"
    )
    print(
        "Ingress accepted scenarios: "
        f"{aggregate['ingress_accepted_scenario_count']}"
    )
    print(f"Total refusal count: {aggregate['refusal_count']}")
    print(f"Output run directory: {_display_path(output_dir)}")
    print(f"Manifest: {_display_path(manifest_path)}")


def _process_scenario_entry(
    source_run_dir: Path,
    output_dir: Path,
    entry: Mapping[str, Any],
) -> dict[str, Any]:
    scenario_id = _require_string(entry, "scenario_id", "scenario manifest entry")
    scenario_name = _require_string(entry, "scenario_name", "scenario manifest entry")
    description = _require_string(entry, "description", "scenario manifest entry")
    source_artifact_path = _resolve_source_artifact_path(
        source_run_dir,
        _require_string(entry, "file_path", "scenario manifest entry"),
    )

    if not source_artifact_path.exists():
        raise RuntimeError(
            f"Source scenario artifact is missing: {_display_path(source_artifact_path)}"
        )
    if not source_artifact_path.is_file():
        raise RuntimeError(
            "Source scenario artifact path is not a file: "
            f"{_display_path(source_artifact_path)}"
        )

    try:
        packet = build_receiving_packet(source_artifact_path)
    except RuntimeError as exc:
        raise RuntimeError(
            "Could not build receiving packet for source artifact: "
            f"{_display_path(source_artifact_path)}"
        ) from exc

    packet_summary = build_receiving_packet_summary(packet)

    try:
        validation_result = validate_receiving_packet(packet)
        validation_summary = build_validation_summary(validation_result)
    except ReceivingPacketValidationError as exc:
        raise RuntimeError(
            "Receiving packet failed hard validation for source artifact: "
            f"{_display_path(source_artifact_path)}"
        ) from exc

    packet_path = output_dir / f"{source_artifact_path.stem}__receiving_packet.json"
    _write_json(packet_path, packet)

    decision = build_ingress_decision_from_packet_path(packet_path)
    decision_summary = build_ingress_decision_summary(decision)
    decision_path = (
        output_dir / f"{source_artifact_path.stem}__receiving_ingress_decision.json"
    )
    _write_json(decision_path, decision)

    if decision_summary.get("scenario_id") != scenario_id:
        raise RuntimeError(
            f"Ingress decision scenario id mismatch for {scenario_id}"
        )
    if decision_summary.get("scenario_name") != scenario_name:
        raise RuntimeError(
            f"Ingress decision scenario name mismatch for {scenario_id}"
        )

    return {
        "scenario_id": scenario_id,
        "scenario_name": scenario_name,
        "description": description,
        "source_artifact_path": _display_path(source_artifact_path),
        "receiving_packet_path": _display_path(packet_path),
        "ingress_decision_path": _display_path(decision_path),
        "validation_passed": validation_summary["all_passed"],
        "ingress_decision": decision_summary["decision"],
        "ingress_decision_reason": decision_summary["decision_reason"],
        "accepted_action_count": validation_summary["accepted_action_count"],
        "refused_action_count": validation_summary["refused_action_count"],
        "object_count": validation_summary["object_count"],
        "open_object_count": validation_summary["open_object_count"],
        "coexistence_relation_count": validation_summary[
            "coexistence_relation_count"
        ],
        "hold_count": validation_summary["hold_count"],
        "transition_record_count": validation_summary["transition_record_count"],
        "refusal_count": validation_summary["refusal_count"],
        "receiving_status": decision_summary["receiving_status"],
        "ingress_decision_surface": _json_ready(decision["ingress_decision"]),
        "receiving_packet_summary": packet_summary,
        "validation_summary": validation_summary,
        "ingress_decision_summary": decision_summary,
    }


def _aggregate_counts(entries: tuple[dict[str, Any], ...]) -> dict[str, int]:
    return {
        "scenario_count": len(entries),
        "object_count": _sum_int(entries, "object_count"),
        "open_object_count": _sum_int(entries, "open_object_count"),
        "coexistence_relation_count": _sum_int(
            entries,
            "coexistence_relation_count",
        ),
        "hold_count": _sum_int(entries, "hold_count"),
        "transition_record_count": _sum_int(entries, "transition_record_count"),
        "refusal_count": _sum_int(entries, "refusal_count"),
        "accepted_action_count": _sum_int(entries, "accepted_action_count"),
        "refused_action_count": _sum_int(entries, "refused_action_count"),
        "validation_passed_scenario_count": sum(
            1 for entry in entries if entry["validation_passed"] is True
        ),
        "validation_failed_scenario_count": sum(
            1 for entry in entries if entry["validation_passed"] is not True
        ),
        "ingress_accepted_scenario_count": sum(
            1 for entry in entries if entry["ingress_decision"] == DECISION_RECEIVE
        ),
        "ingress_rejected_scenario_count": sum(
            1 for entry in entries if entry["ingress_decision"] != DECISION_RECEIVE
        ),
    }


def _validate_source_manifest(manifest: Mapping[str, Any]) -> None:
    _require_string(manifest, "generated_at", "source manifest")
    _require_string(manifest, "output_directory", "source manifest")
    scenario_count = _require_int(manifest, "scenario_count", "source manifest")
    scenarios = _require_list(manifest, "scenarios", "source manifest")

    if scenario_count != len(scenarios):
        raise RuntimeError("Source manifest scenario_count does not match scenarios")

    for index, entry in enumerate(scenarios):
        if not isinstance(entry, Mapping):
            raise RuntimeError(f"Scenario manifest entry {index} must be an object")
        _require_string(entry, "scenario_id", f"scenario manifest entry {index}")
        _require_string(entry, "scenario_name", f"scenario manifest entry {index}")
        _require_string(entry, "description", f"scenario manifest entry {index}")
        _require_string(entry, "file_path", f"scenario manifest entry {index}")


def _scenario_entries(manifest: Mapping[str, Any]) -> tuple[Mapping[str, Any], ...]:
    scenarios = _require_list(manifest, "scenarios", "source manifest")
    entries: list[Mapping[str, Any]] = []
    for index, entry in enumerate(scenarios):
        if not isinstance(entry, Mapping):
            raise RuntimeError(f"Scenario manifest entry {index} must be an object")
        entries.append(entry)
    return tuple(entries)


def _make_output_dir(source_run_dir: Path) -> Path:
    base_dir = _repo_root() / RECEIVING_INGRESS_ROOT
    base_dir.mkdir(parents=True, exist_ok=True)

    stem = source_run_dir.name
    candidate = base_dir / stem
    if not candidate.exists():
        candidate.mkdir(parents=False, exist_ok=False)
        return candidate

    for suffix in range(1, 1000):
        candidate = base_dir / f"{stem}_{suffix:03d}"
        if not candidate.exists():
            candidate.mkdir(parents=False, exist_ok=False)
            return candidate

    raise RuntimeError(
        f"Could not allocate a fresh receiving ingress directory for {stem}"
    )


def _resolve_source_artifact_path(source_run_dir: Path, file_path: str) -> Path:
    path = Path(file_path)
    if path.is_absolute():
        return path.resolve()

    repo_candidate = (_repo_root() / path).resolve()
    if repo_candidate.exists():
        return repo_candidate

    cwd_candidate = path.resolve()
    if cwd_candidate.exists():
        return cwd_candidate

    run_candidate = (source_run_dir / path).resolve()
    if run_candidate.exists():
        return run_candidate

    return repo_candidate


def _write_json(path: Path, payload: Mapping[str, Any]) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite artifact: {_display_path(path)}")
    path.write_text(_json_text(payload), encoding="utf-8")
    return path


def _sum_int(entries: tuple[dict[str, Any], ...], key: str) -> int:
    total = 0
    for entry in entries:
        value = entry.get(key)
        if not isinstance(value, int) or isinstance(value, bool):
            raise RuntimeError(f"Scenario ingress entry has non-integer {key}")
        total += value
    return total


def _resolve_path(path: Path) -> Path:
    if path.is_absolute():
        return path.resolve()
    return (_repo_root() / path).resolve()


def _resolve_output_path(path: Path) -> Path:
    if path.is_absolute():
        return path
    return _repo_root() / path


def _path_from_display(path: str) -> Path:
    value = Path(path)
    if value.is_absolute():
        return value
    return _repo_root() / value


def _path_exists(path: Any) -> bool:
    return isinstance(path, str) and _path_from_display(path).exists()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


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
        raise RuntimeError(f"Malformed {context}: {key} must be an object")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or value == "":
        raise RuntimeError(f"Malformed {context}: {key} must be a non-empty string")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = mapping.get(key)
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be an integer")
    return value


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise RuntimeError(f"Malformed {context}: {key} must be a list")
    return value


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


if __name__ == "__main__":
    main()
