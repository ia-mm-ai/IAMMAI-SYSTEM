"""Bounded source-to-review comparison for v0-min coexistence artifacts.

This runner compares one emitted source scenario run with one import-review
artifact. It verifies that the review points back to the selected source run,
then compares load-bearing counts for scenarios and aggregates.

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

from review_integrity_host_v0_min_coexistence_imports import read_run_manifest


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
REVIEW_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_import_reviews")
COMPARISON_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_comparisons"
)
COMPARISON_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_SOURCE_REVIEW_COMPARISON"
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


def find_latest_review_artifact(root: Path) -> Path:
    """Return the lexically latest ``*__import_review.json`` artifact."""

    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise RuntimeError(f"Review artifact root does not exist: {_display_path(root_path)}")
    if not root_path.is_dir():
        raise RuntimeError(
            f"Review artifact root is not a directory: {_display_path(root_path)}"
        )

    review_paths = sorted(
        path
        for path in root_path.glob("*__import_review.json")
        if path.is_file()
    )
    if not review_paths:
        raise RuntimeError(f"No import-review artifacts found under: {_display_path(root_path)}")
    return review_paths[-1]


def compare_source_run_and_review(
    source_run_dir: Path,
    review_artifact_path: Path,
) -> dict[str, Any]:
    """Compare one source scenario run with its bounded import-review artifact."""

    source_run_path = _repo_relative_path(source_run_dir)
    review_path = _repo_relative_path(review_artifact_path)
    source_manifest = read_run_manifest(source_run_path)
    review = _read_review_artifact(review_path)

    _validate_review_points_to_source_run(review, source_run_path)

    source_scenarios = _source_scenarios_by_id(source_manifest, source_run_path)
    review_scenarios = _review_scenarios_by_id(review)
    _validate_scenario_coverage(source_scenarios, review_scenarios)

    scenario_comparisons = [
        _compare_scenario(source_scenarios[scenario_id], review_scenarios[scenario_id])
        for scenario_id in source_scenarios
    ]
    aggregate_comparison = _compare_aggregates(
        source_manifest,
        review,
        scenario_comparisons,
    )
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
        "review_artifact": {
            "review_artifact_path": _display_path(review_path),
            "review_generated_at": _review_generated_at(review),
            "review_scenario_count": _review_scenario_count(review),
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
    """Compare the latest source run and latest import review artifact."""

    source_run_dir = find_latest_source_run_directory(SOURCE_RUNS_ROOT)
    review_artifact_path = find_latest_review_artifact(REVIEW_ROOT)
    comparison = compare_source_run_and_review(source_run_dir, review_artifact_path)
    output_path = _next_comparison_output_path(source_run_dir)
    written = write_comparison(comparison, output_path)

    mismatch_count = _mismatch_count(comparison)
    print(f"Source run: {_display_path(source_run_dir)}")
    print(f"Review artifact: {_display_path(review_artifact_path)}")
    print(f"Scenarios compared: {comparison['source_run']['source_scenario_count']}")
    print(f"Mismatches: {mismatch_count}")
    print(f"All matched: {comparison['all_matched']}")
    print(f"Comparison artifact: {_display_path(written)}")


def _read_review_artifact(path: Path) -> dict[str, Any]:
    review = _read_json_object(path, "review artifact")
    _require_section(review, "review_metadata", "review")
    _require_section(review, "source_run", "review")
    _require_section(review, "source_manifest", "review")
    _require_list(review, "scenario_reviews", "review")
    _require_section(review, "aggregate_counts", "review")
    return review


def _read_source_artifact(path: Path) -> dict[str, Any]:
    artifact = _read_json_object(path, "source scenario artifact")
    scenario = _require_section(artifact, "scenario", "source artifact")
    snapshot = _require_section(artifact, "snapshot", "source artifact")
    _require_string(scenario, "scenario_id", "source artifact.scenario")
    _require_string(scenario, "scenario_name", "source artifact.scenario")
    _require_int(scenario, "accepted_action_count", "source artifact.scenario")
    _require_int(scenario, "refused_action_count", "source artifact.scenario")
    _require_list(scenario, "action_results", "source artifact.scenario")
    _require_section(snapshot, "host", "source artifact.snapshot")
    _require_list(snapshot, "objects", "source artifact.snapshot")
    _require_list(snapshot, "coexistence_relations", "source artifact.snapshot")
    _require_list(snapshot, "holds", "source artifact.snapshot")
    _require_list(snapshot, "transition_records", "source artifact.snapshot")
    return artifact


def _source_scenarios_by_id(
    source_manifest: Mapping[str, Any],
    source_run_path: Path,
) -> dict[str, dict[str, Any]]:
    scenarios: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(_require_list(source_manifest, "scenarios", "manifest")):
        context = f"manifest.scenarios[{index}]"
        scenario_entry = _require_mapping(entry, context)
        scenario_id = _require_string(scenario_entry, "scenario_id", context)
        if scenario_id in scenarios:
            raise RuntimeError(f"Duplicate source scenario id: {scenario_id}")

        artifact_path = _resolve_path_text(
            _require_string(scenario_entry, "file_path", context),
            base_dir=source_run_path,
        )
        if not artifact_path.exists():
            raise RuntimeError(f"Source scenario artifact is missing: {_display_path(artifact_path)}")

        artifact = _read_source_artifact(artifact_path)
        artifact_scenario = _require_section(artifact, "scenario", "source artifact")
        artifact_id = _require_string(
            artifact_scenario,
            "scenario_id",
            "source artifact.scenario",
        )
        artifact_name = _require_string(
            artifact_scenario,
            "scenario_name",
            "source artifact.scenario",
        )
        manifest_name = _require_string(scenario_entry, "scenario_name", context)

        if artifact_id != scenario_id:
            raise RuntimeError(f"Source manifest/artifact scenario id mismatch: {scenario_id}")
        if artifact_name != manifest_name:
            raise RuntimeError(f"Source manifest/artifact scenario name mismatch: {scenario_id}")

        scenarios[scenario_id] = {
            "scenario_id": scenario_id,
            "scenario_name": manifest_name,
            "artifact_path": artifact_path,
            "counts": _source_counts(artifact),
        }
    return scenarios


def _review_scenarios_by_id(review: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    scenarios: dict[str, dict[str, Any]] = {}
    for index, item in enumerate(_require_list(review, "scenario_reviews", "review")):
        context = f"review.scenario_reviews[{index}]"
        scenario = _require_mapping(item, context)
        scenario_id = _require_string(scenario, "scenario_id", context)
        if scenario_id in scenarios:
            raise RuntimeError(f"Duplicate review scenario id: {scenario_id}")
        scenarios[scenario_id] = dict(scenario)
    return scenarios


def _compare_scenario(
    source: Mapping[str, Any],
    review: Mapping[str, Any],
) -> dict[str, Any]:
    mismatches: list[str] = []
    scenario_id = _require_string(source, "scenario_id", "source scenario")
    source_name = _require_string(source, "scenario_name", "source scenario")
    review_name = _require_string(review, "scenario_name", "review scenario")

    if review["scenario_id"] != scenario_id:
        mismatches.append("scenario_id mismatch")
    if review_name != source_name:
        mismatches.append("scenario_name mismatch")

    source_artifact_path = _require_path(source, "artifact_path", "source scenario")
    review_artifact_path_text = _require_string(
        review,
        "source_artifact_path",
        "review scenario",
    )
    review_artifact_path = _resolve_path_text(review_artifact_path_text)
    if source_artifact_path.resolve() != review_artifact_path.resolve():
        mismatches.append("source artifact path mismatch")

    source_counts = _require_mapping(source["counts"], "source scenario.counts")
    count_comparison = _compare_counts(
        source_counts,
        review,
        COUNT_KEYS,
        mismatches,
    )

    return {
        "scenario_id": scenario_id,
        "scenario_name": source_name,
        "source_artifact_path": _display_path(source_artifact_path),
        "review_source_artifact_path": review_artifact_path_text,
        "matched": not mismatches,
        "mismatches": mismatches,
        "counts": count_comparison,
    }


def _compare_aggregates(
    source_manifest: Mapping[str, Any],
    review: Mapping[str, Any],
    scenario_comparisons: list[dict[str, Any]],
) -> dict[str, Any]:
    source_totals = _aggregate_source_counts(source_manifest, scenario_comparisons)
    review_aggregate = _require_section(review, "aggregate_counts", "review")
    review_totals = {
        key: _require_int(review_aggregate, key, "review.aggregate_counts")
        for key in ("scenario_count", *COUNT_KEYS)
        if key in review_aggregate
    }

    mismatches: list[str] = []
    count_keys = ("scenario_count", *COUNT_KEYS)
    count_comparison = _compare_counts(
        source_totals,
        review_totals,
        count_keys,
        mismatches,
    )
    counts_match = not any(not item["matched"] for item in count_comparison.values())

    return {
        "source_totals": source_totals,
        "review_totals": review_totals,
        "counts_match": counts_match,
        "aggregate_match": counts_match and not mismatches,
        "mismatches": mismatches,
        "counts": count_comparison,
    }


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
        "open_object_count": len(_require_list(host, "open_object_ids", "source artifact.snapshot.host")),
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


def _aggregate_source_counts(
    source_manifest: Mapping[str, Any],
    scenario_comparisons: list[dict[str, Any]],
) -> dict[str, int]:
    totals = {
        "scenario_count": _require_int(source_manifest, "scenario_count", "manifest")
    }
    for key in COUNT_KEYS:
        totals[key] = sum(
            _require_int(comparison["counts"][key], "source", f"{key} comparison")
            for comparison in scenario_comparisons
        )
    return totals


def _compare_counts(
    source_counts: Mapping[str, Any],
    review_counts: Mapping[str, Any],
    keys: tuple[str, ...],
    mismatches: list[str],
) -> dict[str, dict[str, Any]]:
    compared: dict[str, dict[str, Any]] = {}
    for key in keys:
        source_value = _require_plain_int(source_counts.get(key), f"source.{key}")
        if key not in review_counts:
            raise RuntimeError(f"Review count is missing: {key}")
        review_value = _require_plain_int(review_counts[key], f"review.{key}")
        matched = source_value == review_value
        if not matched:
            mismatches.append(
                f"{key} mismatch: source={source_value}, review={review_value}"
            )
        compared[key] = {
            "source": source_value,
            "review": review_value,
            "matched": matched,
        }
    return compared


def _validate_review_points_to_source_run(
    review: Mapping[str, Any],
    source_run_path: Path,
) -> None:
    source_run = _require_section(review, "source_run", "review")
    recorded_path = _require_string(
        source_run,
        "source_run_directory_path",
        "review.source_run",
    )
    recorded = _resolve_path_text(recorded_path)
    if recorded.resolve() != source_run_path.resolve():
        raise RuntimeError(
            "Review artifact does not reference the selected source run: "
            f"review={recorded_path}, source={_display_path(source_run_path)}"
        )


def _validate_scenario_coverage(
    source_scenarios: Mapping[str, Any],
    review_scenarios: Mapping[str, Any],
) -> None:
    source_ids = set(source_scenarios)
    review_ids = set(review_scenarios)
    if source_ids != review_ids:
        missing = sorted(source_ids - review_ids)
        extra = sorted(review_ids - source_ids)
        raise RuntimeError(
            "Scenario coverage mismatch: "
            f"missing_from_review={missing}, extra_in_review={extra}"
        )


def _review_generated_at(review: Mapping[str, Any]) -> str | None:
    metadata = _require_section(review, "review_metadata", "review")
    value = metadata.get("generated_at")
    if value is None:
        return None
    if not isinstance(value, str) or value == "":
        raise RuntimeError("Malformed review.review_metadata: generated_at must be a string")
    return value


def _review_scenario_count(review: Mapping[str, Any]) -> int:
    aggregate = _require_section(review, "aggregate_counts", "review")
    if "scenario_count" in aggregate:
        return _require_int(aggregate, "scenario_count", "review.aggregate_counts")
    return len(_require_list(review, "scenario_reviews", "review"))


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
    stem = f"{source_run_dir.name}__source_review_comparison"
    candidate = output_root / f"{stem}.json"
    if not candidate.exists():
        return candidate

    for suffix in range(1, 1000):
        candidate = output_root / f"{stem}_{suffix:03d}.json"
        if not candidate.exists():
            return candidate

    raise RuntimeError("Could not allocate a fresh comparison artifact path")


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


def _require_plain_int(value: Any, context: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool):
        raise RuntimeError(f"Malformed {context}: expected integer")
    return value


def _require_key(mapping: Mapping[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise RuntimeError(f"Malformed {context}: missing {key}")
    return mapping[key]


def _require_path(mapping: Mapping[str, Any], key: str, context: str) -> Path:
    value = _require_key(mapping, key, context)
    if not isinstance(value, Path):
        raise RuntimeError(f"Malformed {context}: {key} must be a Path")
    return value


def _record_accepted(record: Any) -> bool:
    mapping = _require_mapping(record, "source artifact.snapshot.transition_records[]")
    value = _require_key(
        mapping,
        "accepted",
        "source artifact.snapshot.transition_records[]",
    )
    if not isinstance(value, bool):
        raise RuntimeError("Malformed transition record: accepted must be boolean")
    return value


def _optional_field(value: Any, key: str) -> Any:
    mapping = _require_mapping(value, f"field owner for {key}")
    if key not in mapping:
        raise RuntimeError(f"Malformed field owner: missing {key}")
    return mapping[key]


def _string_field(value: Any, key: str) -> str:
    mapping = _require_mapping(value, f"field owner for {key}")
    return _require_string(mapping, key, f"field owner for {key}")


if __name__ == "__main__":
    main()
