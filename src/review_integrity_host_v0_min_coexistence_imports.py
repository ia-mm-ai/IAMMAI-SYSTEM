"""Bounded review runner for imported v0-min coexistence scenario artifacts.

This module reviews one emitted scenario run by reading its manifest, loading
each scenario artifact through ``integrity_host_v0_min_coexistence_import``,
and writing one local JSON review artifact.

The review artifact is an additive inspection surface only. It does not replay
actions into a host, merge imported packets, define persistence or registry
law, complete cross-host continuity, or upgrade imported material into local
system standing.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from integrity_host_v0_min_coexistence_import import (
    ImportFormatError,
    build_import_summary,
    load_scenario_artifact,
)


SOURCE_RUNS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_scenarios")
REVIEW_OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_import_reviews"
)
REVIEW_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_IMPORT_REVIEW"
REVIEW_VERSION = "0.1.0"


def find_latest_run_directory(root: Path) -> Path:
    """Return the lexically latest ``run_*`` directory under ``root``."""

    root_path = _repo_relative_path(root)
    if not root_path.exists():
        raise RuntimeError(f"Scenario run root does not exist: {_display_path(root_path)}")
    if not root_path.is_dir():
        raise RuntimeError(f"Scenario run root is not a directory: {root_path}")

    run_dirs = sorted(
        path for path in root_path.iterdir() if path.is_dir() and path.name.startswith("run_")
    )
    if not run_dirs:
        raise RuntimeError(f"No scenario run directories found under: {_display_path(root_path)}")
    return run_dirs[-1]


def read_run_manifest(run_dir: Path) -> dict[str, Any]:
    """Read and validate the bounded manifest for one emitted scenario run."""

    run_path = _repo_relative_path(run_dir)
    manifest_path = run_path / "manifest.json"
    if not manifest_path.exists():
        raise RuntimeError(f"Run manifest is missing: {_display_path(manifest_path)}")

    try:
        parsed = json.loads(manifest_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Run manifest is not valid JSON: {_display_path(manifest_path)}") from exc

    manifest = _require_mapping(parsed, "manifest")
    _require_string(manifest, "generated_at", "manifest")
    _require_string(manifest, "output_directory", "manifest")
    scenario_count = _require_int(manifest, "scenario_count", "manifest")
    scenarios = _require_list(manifest, "scenarios", "manifest")

    if scenario_count != len(scenarios):
        raise RuntimeError("Malformed manifest: scenario_count does not match scenarios")

    for index, entry in enumerate(scenarios):
        context = f"manifest.scenarios[{index}]"
        scenario = _require_mapping(entry, context)
        _require_string(scenario, "scenario_id", context)
        _require_string(scenario, "scenario_name", context)
        _require_string(scenario, "description", context)
        _require_string(scenario, "file_path", context)

    return dict(manifest)


def review_run_directory(run_dir: Path) -> dict[str, Any]:
    """Build one bounded import review object for an emitted scenario run."""

    run_path = _repo_relative_path(run_dir)
    manifest = read_run_manifest(run_path)
    manifest_path = run_path / "manifest.json"
    scenario_reviews = []

    for entry in manifest["scenarios"]:
        scenario_entry = _require_mapping(entry, "manifest.scenarios[]")
        artifact_path = _resolve_manifest_artifact_path(
            _require_string(scenario_entry, "file_path", "manifest.scenarios[]"),
            run_path,
        )
        if not artifact_path.exists():
            raise RuntimeError(f"Scenario artifact is missing: {_display_path(artifact_path)}")

        try:
            imported = load_scenario_artifact(artifact_path)
        except ImportFormatError as exc:
            raise RuntimeError(
                f"Scenario artifact failed import validation: {_display_path(artifact_path)}"
            ) from exc

        summary = build_import_summary(imported)
        _validate_manifest_import_match(scenario_entry, summary, artifact_path)
        scenario_reviews.append(
            _build_scenario_review(scenario_entry, artifact_path, imported, summary)
        )

    return {
        "review_metadata": {
            "review_type": REVIEW_TYPE,
            "review_version": REVIEW_VERSION,
            "generated_at": _utc_timestamp(),
            "reviewer_module": __name__,
            "source_run_directory": _display_path(run_path),
        },
        "source_run": {
            "source_run_directory_path": _display_path(run_path),
            "source_manifest_path": _display_path(manifest_path),
            "source_scenario_count": manifest["scenario_count"],
        },
        "source_manifest": _manifest_review_copy(manifest),
        "scenario_reviews": scenario_reviews,
        "aggregate_counts": _aggregate_counts(scenario_reviews),
    }


def write_review(review: dict[str, Any], output_path: Path) -> Path:
    """Write one UTF-8 JSON review artifact without overwriting prior output."""

    path = _repo_relative_path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise RuntimeError(f"Refusing to overwrite existing review artifact: {_display_path(path)}")
    path.write_text(_json_text(review), encoding="utf-8")
    return path


def main() -> None:
    """Review the latest emitted scenario run and print a short summary."""

    run_dir = find_latest_run_directory(SOURCE_RUNS_ROOT)
    review = review_run_directory(run_dir)
    output_path = _next_review_output_path(run_dir)
    written = write_review(review, output_path)
    aggregate = review["aggregate_counts"]

    print(f"Source run: {_display_path(run_dir)}")
    print(f"Scenarios reviewed: {aggregate['scenario_count']}")
    print(f"Total refusals: {aggregate['refusal_count']}")
    print(f"Review artifact: {_display_path(written)}")


def _build_scenario_review(
    scenario_entry: Mapping[str, Any],
    artifact_path: Path,
    imported: Any,
    summary: Mapping[str, Any],
) -> dict[str, Any]:
    successor_object_count = sum(
        1 for obj in imported.objects if obj.predecessor_object_id is not None
    )
    evolve_record_count = sum(
        1 for record in imported.transition_records if record.action_type == "EVOLVE"
    )
    resolved_object_count = sum(
        1 for obj in imported.objects if obj.resolution_type is not None
    )

    return {
        "scenario_id": _require_string(
            scenario_entry,
            "scenario_id",
            "manifest.scenarios[]",
        ),
        "scenario_name": _require_string(
            scenario_entry,
            "scenario_name",
            "manifest.scenarios[]",
        ),
        "source_artifact_path": _display_path(artifact_path),
        "imported_summary": dict(summary),
        "accepted_action_count": summary["accepted_action_count"],
        "refused_action_count": summary["refused_action_count"],
        "object_count": summary["object_count"],
        "open_object_count": summary["open_object_count"],
        "resolved_object_count": resolved_object_count,
        "coexistence_relation_count": summary["coexistence_relation_count"],
        "hold_count": summary["hold_count"],
        "transition_record_count": summary["record_count"],
        "refusal_count": summary["refusal_count"],
        "successor_object_count": successor_object_count,
        "evolve_record_count": evolve_record_count,
    }


def _aggregate_counts(scenario_reviews: list[dict[str, Any]]) -> dict[str, int]:
    count_keys = (
        "object_count",
        "open_object_count",
        "resolved_object_count",
        "coexistence_relation_count",
        "hold_count",
        "transition_record_count",
        "refusal_count",
        "accepted_action_count",
        "refused_action_count",
        "successor_object_count",
        "evolve_record_count",
    )
    aggregate = {"scenario_count": len(scenario_reviews)}
    for key in count_keys:
        aggregate[key] = sum(_require_plain_int(review[key], key) for review in scenario_reviews)
    return aggregate


def _manifest_review_copy(manifest: Mapping[str, Any]) -> dict[str, Any]:
    scenarios = []
    for index, entry in enumerate(manifest["scenarios"]):
        context = f"manifest.scenarios[{index}]"
        scenario = _require_mapping(entry, context)
        scenarios.append(
            {
                "scenario_id": _require_string(scenario, "scenario_id", context),
                "scenario_name": _require_string(scenario, "scenario_name", context),
                "description": _require_string(scenario, "description", context),
                "file_path": _require_string(scenario, "file_path", context),
            }
        )

    return {
        "generated_at": _require_string(manifest, "generated_at", "manifest"),
        "output_directory": _require_string(
            manifest,
            "output_directory",
            "manifest",
        ),
        "scenario_count": _require_int(manifest, "scenario_count", "manifest"),
        "scenarios": scenarios,
    }


def _validate_manifest_import_match(
    scenario_entry: Mapping[str, Any],
    summary: Mapping[str, Any],
    artifact_path: Path,
) -> None:
    manifest_id = _require_string(scenario_entry, "scenario_id", "manifest.scenarios[]")
    manifest_name = _require_string(
        scenario_entry,
        "scenario_name",
        "manifest.scenarios[]",
    )
    if summary["scenario_id"] != manifest_id:
        raise RuntimeError(
            "Scenario id mismatch between manifest and imported artifact: "
            f"{_display_path(artifact_path)}"
        )
    if summary["scenario_name"] != manifest_name:
        raise RuntimeError(
            "Scenario name mismatch between manifest and imported artifact: "
            f"{_display_path(artifact_path)}"
        )


def _resolve_manifest_artifact_path(path_text: str, run_dir: Path) -> Path:
    path = Path(path_text)
    if path.is_absolute():
        return path

    repo_candidate = _repo_root() / path
    if repo_candidate.exists():
        return repo_candidate

    run_candidate = run_dir / path
    if run_candidate.exists():
        return run_candidate

    return repo_candidate


def _next_review_output_path(run_dir: Path) -> Path:
    output_root = _repo_root() / REVIEW_OUTPUT_ROOT
    stem = f"{run_dir.name}__import_review"
    candidate = output_root / f"{stem}.json"
    if not candidate.exists():
        return candidate

    for suffix in range(1, 1000):
        candidate = output_root / f"{stem}_{suffix:03d}.json"
        if not candidate.exists():
            return candidate

    raise RuntimeError("Could not allocate a fresh import review artifact path")


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


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise RuntimeError(f"Malformed {context}: expected object")
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


def _require_list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = _require_key(mapping, key, context)
    if not isinstance(value, list):
        raise RuntimeError(f"Malformed {context}: {key} must be a list")
    return value


def _require_key(mapping: Mapping[str, Any], key: str, context: str) -> Any:
    if key not in mapping:
        raise RuntimeError(f"Malformed {context}: missing {key}")
    return mapping[key]


if __name__ == "__main__":
    main()
