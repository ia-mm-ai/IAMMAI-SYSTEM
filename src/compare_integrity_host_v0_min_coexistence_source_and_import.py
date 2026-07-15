"""Bounded source-to-import comparison for v0-min coexistence artifacts.

This runner compares one emitted source scenario run with the imported packets
created from those same source artifacts. It reads the source manifest and
scenario JSON, loads each scenario artifact through the current import layer,
and compares load-bearing counts plus bounded structural visibility.

The comparison artifact is an additive engineering surface only. It does not
replay actions into a host, merge imported packets, define persistence or
registry law, complete continuity, or become a generic diff engine.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from integrity_host_v0_min_coexistence_import import (
    ImportFormatError,
    ImportedScenarioArtifact,
    load_scenario_artifact,
)


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
COMPARISON_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_source_import_comparisons"
)
COMPARISON_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SOURCE_IMPORT_COMPARISON"
COMPARISON_VERSION = "0.1.0"

COUNT_KEYS = (
    "object_count",
    "open_object_count",
    "coexistence_relation_count",
    "hold_count",
    "transition_record_count",
    "refusal_count",
    "accepted_action_count",
    "refused_action_count",
    "resolved_object_count",
    "successor_object_count",
    "evolve_record_count",
)


def find_latest_source_run_directory(root: Path) -> Path:
    """Return the lexically latest ``run_*`` directory under ``root``."""

    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise RuntimeError(f"Source run root does not exist: {_display_path(root_path)}")
    if not root_path.is_dir():
        raise RuntimeError(f"Source run root is not a directory: {_display_path(root_path)}")

    run_dirs = sorted(
        path
        for path in root_path.iterdir()
        if path.is_dir() and path.name.startswith("run_")
    )
    if not run_dirs:
        raise RuntimeError(f"No source run directories found under: {_display_path(root_path)}")
    return run_dirs[-1]


def read_source_manifest(run_dir: Path) -> dict[str, Any]:
    """Read and validate the bounded manifest for one emitted source run."""

    run_path = _repo_relative_path(run_dir)
    manifest_path = run_path / "manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Source manifest is missing: {_display_path(manifest_path)}")

    manifest = _read_json_object(manifest_path, "source manifest")
    _require_string(manifest, "generated_at", "manifest")
    _require_string(manifest, "output_directory", "manifest")
    scenario_count = _require_int(manifest, "scenario_count", "manifest")
    scenarios = _require_list(manifest, "scenarios", "manifest")

    if scenario_count != len(scenarios):
        raise RuntimeError("Malformed manifest: scenario_count does not match scenarios")

    seen_ids: set[str] = set()
    for index, item in enumerate(scenarios):
        context = f"manifest.scenarios[{index}]"
        scenario = _require_mapping(item, context)
        scenario_id = _require_string(scenario, "scenario_id", context)
        if scenario_id in seen_ids:
            raise RuntimeError(f"Duplicate source scenario id: {scenario_id}")
        seen_ids.add(scenario_id)
        _require_string(scenario, "scenario_name", context)
        _require_string(scenario, "description", context)
        _require_string(scenario, "file_path", context)

    return manifest


def compare_source_run_and_import(source_run_dir: Path) -> dict[str, Any]:
    """Compare one source scenario run directly against imported packets."""

    source_run_path = _repo_relative_path(source_run_dir)
    source_manifest = read_source_manifest(source_run_path)
    scenario_comparisons = _scenario_comparisons(source_manifest, source_run_path)
    aggregate_comparison = _compare_aggregates(source_manifest, scenario_comparisons)
    all_matched = aggregate_comparison["aggregate_match"] and all(
        comparison["matched"] for comparison in scenario_comparisons
    )

    return {
        "comparison_metadata": {
            "comparison_type": COMPARISON_TYPE,
            "comparison_version": COMPARISON_VERSION,
            "generated_at": _utc_timestamp(),
            "comparator_module": __name__,
        },
        "source_run": {
            "source_run_directory_path": _display_path(source_run_path),
            "source_manifest_path": _display_path(source_run_path / "manifest.json"),
            "source_scenario_count": source_manifest["scenario_count"],
        },
        "scenario_comparisons": scenario_comparisons,
        "aggregate_comparison": aggregate_comparison,
        "all_matched": all_matched,
    }


def write_comparison(comparison: dict[str, Any], output_path: Path) -> Path:
    """Write one UTF-8 JSON comparison artifact without overwriting output."""

    path = _repo_relative_path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite comparison artifact: {_display_path(path)}")
    path.write_text(_json_text(comparison), encoding="utf-8")
    return path


def main() -> None:
    """Compare the latest source run and print a short summary."""

    source_run_dir = find_latest_source_run_directory(SOURCE_RUNS_ROOT)
    comparison = compare_source_run_and_import(source_run_dir)
    output_path = _next_comparison_output_path(source_run_dir)
    written = write_comparison(comparison, output_path)

    print(f"Source run: {_display_path(source_run_dir)}")
    print(f"Scenarios compared: {comparison['source_run']['source_scenario_count']}")
    print(f"Mismatches: {_mismatch_count(comparison)}")
    print(f"All matched: {comparison['all_matched']}")
    print(f"Comparison artifact: {_display_path(written)}")


def _scenario_comparisons(
    source_manifest: Mapping[str, Any],
    source_run_path: Path,
) -> list[dict[str, Any]]:
    comparisons: list[dict[str, Any]] = []
    for index, item in enumerate(_require_list(source_manifest, "scenarios", "manifest")):
        context = f"manifest.scenarios[{index}]"
        manifest_entry = _require_mapping(item, context)
        artifact_path = _resolve_path_text(
            _require_string(manifest_entry, "file_path", context),
            base_dir=source_run_path,
        )
        if not artifact_path.exists():
            raise RuntimeError(f"Source scenario artifact is missing: {_display_path(artifact_path)}")

        source_artifact = _read_source_artifact(artifact_path)
        _validate_manifest_artifact_match(manifest_entry, source_artifact, artifact_path)

        try:
            imported = load_scenario_artifact(artifact_path)
        except ImportFormatError as exc:
            raise RuntimeError(
                "Scenario artifact failed import validation: "
                f"{_display_path(artifact_path)}"
            ) from exc

        comparisons.append(
            _compare_scenario(
                source_artifact,
                imported,
                artifact_path,
            )
        )
    return comparisons


def _compare_scenario(
    source_artifact: Mapping[str, Any],
    imported: ImportedScenarioArtifact,
    artifact_path: Path,
) -> dict[str, Any]:
    mismatches: list[str] = []
    source_scenario = _require_section(source_artifact, "scenario", "source artifact")
    source_id = _require_string(source_scenario, "scenario_id", "source artifact.scenario")
    source_name = _require_string(
        source_scenario,
        "scenario_name",
        "source artifact.scenario",
    )

    if imported.scenario.scenario_id != source_id:
        mismatches.append("scenario_id mismatch")
    if imported.scenario.scenario_name != source_name:
        mismatches.append("scenario_name mismatch")
    if Path(imported.scenario.source_path).resolve() != artifact_path.resolve():
        mismatches.append("import source path mismatch")

    source_counts = _source_counts(source_artifact)
    import_counts = _import_counts(imported)
    count_comparison = _compare_counts(
        source_counts,
        import_counts,
        COUNT_KEYS,
        mismatches,
    )
    visibility_comparison = _compare_visibility(source_artifact, imported, mismatches)

    return {
        "scenario_id": source_id,
        "scenario_name": source_name,
        "source_artifact_path": _display_path(artifact_path),
        "matched": not mismatches,
        "mismatches": mismatches,
        "counts": count_comparison,
        "visibility": visibility_comparison,
    }


def _compare_aggregates(
    source_manifest: Mapping[str, Any],
    scenario_comparisons: list[dict[str, Any]],
) -> dict[str, Any]:
    source_totals = {
        "scenario_count": _require_int(source_manifest, "scenario_count", "manifest")
    }
    import_totals = {"scenario_count": len(scenario_comparisons)}
    for key in COUNT_KEYS:
        source_totals[key] = sum(
            _require_int(comparison["counts"][key], "source", f"{key} comparison")
            for comparison in scenario_comparisons
        )
        import_totals[key] = sum(
            _require_int(comparison["counts"][key], "import", f"{key} comparison")
            for comparison in scenario_comparisons
        )

    mismatches: list[str] = []
    count_comparison = _compare_counts(
        source_totals,
        import_totals,
        ("scenario_count", *COUNT_KEYS),
        mismatches,
    )
    counts_match = not any(not item["matched"] for item in count_comparison.values())

    return {
        "source_totals": source_totals,
        "import_totals": import_totals,
        "counts_match": counts_match,
        "aggregate_match": counts_match and not mismatches,
        "mismatches": mismatches,
        "counts": count_comparison,
    }


def _read_source_artifact(path: Path) -> dict[str, Any]:
    artifact = _read_json_object(path, "source scenario artifact")
    scenario = _require_section(artifact, "scenario", "source artifact")
    snapshot = _require_section(artifact, "snapshot", "source artifact")

    accepted_count = _require_int(
        scenario,
        "accepted_action_count",
        "source artifact.scenario",
    )
    refused_count = _require_int(
        scenario,
        "refused_action_count",
        "source artifact.scenario",
    )
    actions = _require_list(scenario, "action_results", "source artifact.scenario")
    observed_accepted = 0
    for index, action in enumerate(actions):
        mapping = _require_mapping(action, f"source artifact.scenario.action_results[{index}]")
        if _require_bool(mapping, "accepted", f"source artifact.scenario.action_results[{index}]"):
            observed_accepted += 1
    observed_refused = len(actions) - observed_accepted
    if accepted_count != observed_accepted:
        raise RuntimeError(
            "Malformed source artifact.scenario: accepted_action_count "
            "does not match action_results"
        )
    if refused_count != observed_refused:
        raise RuntimeError(
            "Malformed source artifact.scenario: refused_action_count "
            "does not match action_results"
        )

    _require_string(scenario, "scenario_id", "source artifact.scenario")
    _require_string(scenario, "scenario_name", "source artifact.scenario")
    _require_section(snapshot, "host", "source artifact.snapshot")
    _require_list(snapshot, "objects", "source artifact.snapshot")
    _require_list(snapshot, "coexistence_relations", "source artifact.snapshot")
    _require_list(snapshot, "holds", "source artifact.snapshot")
    _require_list(snapshot, "transition_records", "source artifact.snapshot")
    return artifact


def _validate_manifest_artifact_match(
    manifest_entry: Mapping[str, Any],
    source_artifact: Mapping[str, Any],
    artifact_path: Path,
) -> None:
    manifest_id = _require_string(manifest_entry, "scenario_id", "manifest.scenarios[]")
    manifest_name = _require_string(
        manifest_entry,
        "scenario_name",
        "manifest.scenarios[]",
    )
    scenario = _require_section(source_artifact, "scenario", "source artifact")
    artifact_id = _require_string(
        scenario,
        "scenario_id",
        "source artifact.scenario",
    )
    artifact_name = _require_string(
        scenario,
        "scenario_name",
        "source artifact.scenario",
    )
    if artifact_id != manifest_id:
        raise RuntimeError(
            "Source manifest/artifact scenario id mismatch: "
            f"{manifest_id} at {_display_path(artifact_path)}"
        )
    if artifact_name != manifest_name:
        raise RuntimeError(
            "Source manifest/artifact scenario name mismatch: "
            f"{manifest_id} at {_display_path(artifact_path)}"
        )


def _source_counts(source_artifact: Mapping[str, Any]) -> dict[str, int]:
    scenario = _require_section(source_artifact, "scenario", "source artifact")
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    host = _require_section(snapshot, "host", "source artifact.snapshot")
    objects = _require_list(snapshot, "objects", "source artifact.snapshot")
    relations = _require_list(
        snapshot,
        "coexistence_relations",
        "source artifact.snapshot",
    )
    holds = _require_list(snapshot, "holds", "source artifact.snapshot")
    records = _require_list(snapshot, "transition_records", "source artifact.snapshot")

    return {
        "object_count": len(objects),
        "open_object_count": len(
            _require_list(host, "open_object_ids", "source artifact.snapshot.host")
        ),
        "coexistence_relation_count": len(relations),
        "hold_count": len(holds),
        "transition_record_count": len(records),
        "refusal_count": sum(1 for record in records if not _record_accepted(record)),
        "accepted_action_count": _require_int(
            scenario,
            "accepted_action_count",
            "source artifact.scenario",
        ),
        "refused_action_count": _require_int(
            scenario,
            "refused_action_count",
            "source artifact.scenario",
        ),
        "resolved_object_count": sum(
            1 for obj in objects if _optional_field(obj, "resolution_type") is not None
        ),
        "successor_object_count": sum(
            1
            for obj in objects
            if _optional_field(obj, "predecessor_object_id") is not None
        ),
        "evolve_record_count": sum(
            1 for record in records if _string_field(record, "action_type") == "EVOLVE"
        ),
    }


def _import_counts(imported: ImportedScenarioArtifact) -> dict[str, int]:
    return {
        "object_count": len(imported.objects),
        "open_object_count": len(imported.host.open_object_ids),
        "coexistence_relation_count": len(imported.coexistence_relations),
        "hold_count": len(imported.holds),
        "transition_record_count": len(imported.transition_records),
        "refusal_count": sum(1 for record in imported.transition_records if not record.accepted),
        "accepted_action_count": imported.scenario.accepted_action_count,
        "refused_action_count": imported.scenario.refused_action_count,
        "resolved_object_count": sum(
            1 for obj in imported.objects if obj.resolution_type is not None
        ),
        "successor_object_count": sum(
            1 for obj in imported.objects if obj.predecessor_object_id is not None
        ),
        "evolve_record_count": sum(
            1 for record in imported.transition_records if record.action_type == "EVOLVE"
        ),
    }


def _compare_counts(
    source_counts: Mapping[str, Any],
    import_counts: Mapping[str, Any],
    keys: tuple[str, ...],
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    compared: dict[str, dict[str, Any]] = {}
    for key in keys:
        source_value = _require_plain_int(source_counts.get(key), f"source.{key}")
        if key not in import_counts:
            raise RuntimeError(f"Import count is missing: {key}")
        import_value = _require_plain_int(import_counts[key], f"import.{key}")
        matched = source_value == import_value
        if not matched:
            mismatches.append(
                f"{key} mismatch: source={source_value}, import={import_value}"
            )
        compared[key] = {
            "source": source_value,
            "import": import_value,
            "matched": matched,
        }
    return compared


def _compare_visibility(
    source_artifact: Mapping[str, Any],
    imported: ImportedScenarioArtifact,
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    checks = {
        "object_ids": (_source_object_ids(source_artifact), _import_object_ids(imported)),
        "coexistence_relations": (
            _source_relation_visibility(source_artifact),
            _import_relation_visibility(imported),
        ),
        "holds": (_source_hold_visibility(source_artifact), _import_hold_visibility(imported)),
        "refusal_records": (
            _source_refusal_visibility(source_artifact),
            _import_refusal_visibility(imported),
        ),
        "successor_lineage": (
            _source_successor_lineage_visibility(source_artifact),
            _import_successor_lineage_visibility(imported),
        ),
        "evolve_record_lineage": (
            _source_evolve_record_visibility(source_artifact),
            _import_evolve_record_visibility(imported),
        ),
    }

    compared: dict[str, dict[str, Any]] = {}
    for key, (source_value, import_value) in checks.items():
        matched = source_value == import_value
        if not matched:
            mismatches.append(f"{key} visibility mismatch")
        compared[key] = {
            "source": source_value,
            "import": import_value,
            "matched": matched,
        }
    return compared


def _source_object_ids(source_artifact: Mapping[str, Any]) -> list[str]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    return sorted(
        _string_field(obj, "object_id")
        for obj in _require_list(snapshot, "objects", "source artifact.snapshot")
    )


def _import_object_ids(imported: ImportedScenarioArtifact) -> list[str]:
    return sorted(obj.object_id for obj in imported.objects)


def _source_relation_visibility(source_artifact: Mapping[str, Any]) -> list[dict[str, Any]]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    return _sorted_dicts(
        {
            "relation_type": _string_field(relation, "relation_type"),
            "object_id": _string_field(relation, "object_id"),
            "related_object_id": _string_field(relation, "related_object_id"),
            "basis_ref": _string_field(relation, "basis_ref"),
            "created_by_record_id": _string_field(relation, "created_by_record_id"),
        }
        for relation in _require_list(
            snapshot,
            "coexistence_relations",
            "source artifact.snapshot",
        )
    )


def _import_relation_visibility(imported: ImportedScenarioArtifact) -> list[dict[str, Any]]:
    return _sorted_dicts(
        {
            "relation_type": relation.relation_type,
            "object_id": relation.object_id,
            "related_object_id": relation.related_object_id,
            "basis_ref": relation.basis_ref,
            "created_by_record_id": relation.created_by_record_id,
        }
        for relation in imported.coexistence_relations
    )


def _source_hold_visibility(source_artifact: Mapping[str, Any]) -> list[dict[str, Any]]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    return _sorted_dicts(
        {
            "target_object_id": _string_field(hold, "target_object_id"),
            "active": _bool_field(hold, "active"),
            "basis_ref": _string_field(hold, "basis_ref"),
            "set_by_record_id": _string_field(hold, "set_by_record_id"),
        }
        for hold in _require_list(snapshot, "holds", "source artifact.snapshot")
    )


def _import_hold_visibility(imported: ImportedScenarioArtifact) -> list[dict[str, Any]]:
    return _sorted_dicts(
        {
            "target_object_id": hold.target_object_id,
            "active": hold.active,
            "basis_ref": hold.basis_ref,
            "set_by_record_id": hold.set_by_record_id,
        }
        for hold in imported.holds
    )


def _source_refusal_visibility(source_artifact: Mapping[str, Any]) -> list[dict[str, Any]]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    refusals = []
    for record in _require_list(snapshot, "transition_records", "source artifact.snapshot"):
        mapping = _require_mapping(record, "source artifact.snapshot.transition_records[]")
        if _require_bool(mapping, "accepted", "source artifact.snapshot.transition_records[]"):
            continue
        refusals.append(
            {
                "record_id": _require_string(
                    mapping,
                    "record_id",
                    "source artifact.snapshot.transition_records[]",
                ),
                "action_type": _require_string(
                    mapping,
                    "action_type",
                    "source artifact.snapshot.transition_records[]",
                ),
                "refusal_code": _optional_field(mapping, "refusal_code"),
            }
        )
    return _sorted_dicts(refusals)


def _import_refusal_visibility(imported: ImportedScenarioArtifact) -> list[dict[str, Any]]:
    return _sorted_dicts(
        {
            "record_id": record.record_id,
            "action_type": record.action_type,
            "refusal_code": record.refusal_code,
        }
        for record in imported.transition_records
        if not record.accepted
    )


def _source_successor_lineage_visibility(
    source_artifact: Mapping[str, Any],
) -> list[dict[str, Any]]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    lineage = []
    for obj in _require_list(snapshot, "objects", "source artifact.snapshot"):
        predecessor = _optional_field(obj, "predecessor_object_id")
        if predecessor is None:
            continue
        lineage.append(
            {
                "predecessor_object_id": predecessor,
                "successor_object_id": _string_field(obj, "object_id"),
            }
        )
    return _sorted_dicts(lineage)


def _import_successor_lineage_visibility(
    imported: ImportedScenarioArtifact,
) -> list[dict[str, Any]]:
    return _sorted_dicts(
        {
            "predecessor_object_id": obj.predecessor_object_id,
            "successor_object_id": obj.object_id,
        }
        for obj in imported.objects
        if obj.predecessor_object_id is not None
    )


def _source_evolve_record_visibility(source_artifact: Mapping[str, Any]) -> list[dict[str, Any]]:
    snapshot = _require_section(source_artifact, "snapshot", "source artifact")
    evolve_records = []
    for record in _require_list(snapshot, "transition_records", "source artifact.snapshot"):
        mapping = _require_mapping(record, "source artifact.snapshot.transition_records[]")
        if _require_string(
            mapping,
            "action_type",
            "source artifact.snapshot.transition_records[]",
        ) != "EVOLVE":
            continue
        evolve_records.append(
            {
                "record_id": _require_string(
                    mapping,
                    "record_id",
                    "source artifact.snapshot.transition_records[]",
                ),
                "predecessor_object_id": _optional_field(
                    mapping,
                    "predecessor_object_id",
                ),
                "successor_object_id": _optional_field(mapping, "successor_object_id"),
                "target_resolution_type": _optional_field(
                    mapping,
                    "target_resolution_type",
                ),
            }
        )
    return _sorted_dicts(evolve_records)


def _import_evolve_record_visibility(imported: ImportedScenarioArtifact) -> list[dict[str, Any]]:
    return _sorted_dicts(
        {
            "record_id": record.record_id,
            "predecessor_object_id": record.predecessor_object_id,
            "successor_object_id": record.successor_object_id,
            "target_resolution_type": record.target_resolution_type,
        }
        for record in imported.transition_records
        if record.action_type == "EVOLVE"
    )


def _sorted_dicts(values: Any) -> list[dict[str, Any]]:
    return sorted(
        (dict(value) for value in values),
        key=lambda value: json.dumps(value, sort_keys=True, allow_nan=False),
    )


def _mismatch_count(comparison: Mapping[str, Any]) -> int:
    scenario_mismatches = sum(
        len(_require_list(item, "mismatches", "scenario comparison"))
        for item in _require_list(comparison, "scenario_comparisons", "comparison")
    )
    aggregate = _require_section(comparison, "aggregate_comparison", "comparison")
    return scenario_mismatches + len(
        _require_list(aggregate, "mismatches", "aggregate comparison")
    )


def _next_comparison_output_path(source_run_dir: Path) -> Path:
    output_root = _repo_root() / COMPARISON_OUTPUT_ROOT
    stem = f"{source_run_dir.name}__source_import_comparison"
    candidate = output_root / f"{stem}.json"
    if not candidate.exists():
        return candidate

    for suffix in range(1, 1000):
        candidate = output_root / f"{stem}_{suffix:03d}.json"
        if not candidate.exists():
            return candidate

    raise RuntimeError("Could not allocate a fresh source-import comparison artifact path")


def _read_json_object(path: Path, label: str) -> dict[str, Any]:
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise RuntimeError(f"Could not read {label}: {_display_path(path)}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"{label} is not valid JSON: {_display_path(path)}") from exc

    if not isinstance(parsed, dict):
        raise RuntimeError(f"Malformed {label}: expected object")
    return parsed


def _resolve_path_text(path_text: str, base_dir: Path | None = None) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path.resolve()

    candidates = []
    if base_dir is not None:
        candidates.append((base_dir / path).resolve())
    candidates.append((_repo_root() / path).resolve())

    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_relative_path(path: Path) -> Path:
    path = Path(path)
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


def _require_section(
    mapping: Mapping[str, Any],
    key: str,
    context: str,
) -> Mapping[str, Any]:
    value = _require_key(mapping, key, context)
    return _require_mapping(value, f"{context}.{key}")


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise RuntimeError(f"Malformed {context}: expected object")
    return value


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = _require_key(mapping, key, context)
    if not isinstance(value, list):
        raise RuntimeError(f"Malformed {context}: {key} must be a list")
    return value


def _require_string(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = _require_key(mapping, key, context)
    if not isinstance(value, str) or value == "":
        raise RuntimeError(f"Malformed {context}: {key} must be a non-empty string")
    return value


def _require_int(mapping: Mapping[str, Any], key: str, context: str) -> int:
    value = _require_key(mapping, key, context)
    return _require_plain_int(value, f"{context}.{key}")


def _require_bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = _require_key(mapping, key, context)
    if not isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: {key} must be boolean")
    return value


def _require_plain_int(value: Any, context: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: expected integer")
    return value


def _require_key(mapping: Mapping[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise RuntimeError(f"Malformed {context}: missing {key}")
    return mapping[key]


def _record_accepted(record: Any) -> bool:
    mapping = _require_mapping(record, "source artifact.snapshot.transition_records[]")
    return _require_bool(
        mapping,
        "accepted",
        "source artifact.snapshot.transition_records[]",
    )


def _optional_field(value: Any, key: str) -> Any:
    mapping = _require_mapping(value, f"field owner for {key}")
    if key not in mapping:
        raise RuntimeError(f"Malformed field owner: missing {key}")
    return mapping[key]


def _string_field(value: Any, key: str) -> str:
    mapping = _require_mapping(value, f"field owner for {key}")
    return _require_string(mapping, key, f"field owner for {key}")


def _bool_field(value: Any, key: str) -> bool:
    mapping = _require_mapping(value, f"field owner for {key}")
    return _require_bool(mapping, key, f"field owner for {key}")


if __name__ == "__main__":
    main()
