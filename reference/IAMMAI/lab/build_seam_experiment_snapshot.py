#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the seam experiment lab family.

This script reads preserved seam outcome experiment runs and emits one additive
snapshot under lab/snapshots/. It does not rerun experiments, mutate old
outputs, or treat the resulting snapshot as protocol law.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"
EXPERIMENT_PREFIX = "seam_outcome_experiment_"
SCRIPT_PREFIX = "run_seam_outcome_experiment_"


KNOWN_EXPERIMENT_READINGS: Dict[str, Dict[str, str]] = {
    "seam_outcome_experiment_001": {
        "experiment_role": "threshold_met_seam_outcomes",
        "experiment_reading": (
            "Threshold-met seam outcome surface for contaminated-channel cases "
            "where self-carried coherence is sufficient."
        ),
    },
    "seam_outcome_experiment_002": {
        "experiment_role": "threshold_not_yet_met_seam_outcomes",
        "experiment_reading": (
            "Threshold-not-yet-met seam outcome surface for cases where lawful "
            "crossing is blocked by insufficient self-carried coherence."
        ),
    },
    "seam_outcome_experiment_003": {
        "experiment_role": "responsibility_lineage_scapegoating_seam_outcomes",
        "experiment_reading": (
            "Responsibility, lineage, and scapegoating seam outcome surface for "
            "contaminated or constrained channels."
        ),
    },
}


@dataclass(frozen=True)
class RunSelection:
    run_path: Path
    summary_path: Optional[Path]
    grounding_path: Optional[Path]
    summary_generated_at: Optional[str]
    summary_payload: Optional[Dict[str, Any]]
    selection_method: str


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def timestamp_slug() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def repo_relative(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def choose_snapshot_path() -> Path:
    base_name = f"seam_experiment_snapshot__{timestamp_slug()}"
    candidate = SNAPSHOTS_ROOT / f"{base_name}.json"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = SNAPSHOTS_ROOT / f"{base_name}__{counter}.json"
        if not candidate.exists():
            return candidate
        counter += 1


def safe_read_json(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, str(exc)

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        return None, str(exc)

    if not isinstance(parsed, dict):
        return None, f"Top-level JSON value is not an object: {type(parsed).__name__}"

    return parsed, None


def parse_generated_at(value: Any) -> Optional[datetime]:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def script_path_for_experiment(experiment_id: str) -> Path:
    suffix = experiment_id.removeprefix(EXPERIMENT_PREFIX)
    return LAB_ROOT / f"{SCRIPT_PREFIX}{suffix}.py"


def discover_experiment_ids() -> List[str]:
    if not LAB_ROOT.is_dir():
        raise FileNotFoundError(f"Lab directory is missing or unreadable: {LAB_ROOT}")

    discovered: set[str] = set()

    for path in LAB_ROOT.iterdir():
        if path.is_dir() and path.name.startswith(EXPERIMENT_PREFIX):
            discovered.add(path.name)
        elif path.is_file() and path.name.startswith(SCRIPT_PREFIX) and path.suffix == ".py":
            suffix = path.stem.removeprefix(SCRIPT_PREFIX)
            discovered.add(f"{EXPERIMENT_PREFIX}{suffix}")

    return sorted(discovered)


def list_run_paths(runs_root: Path) -> List[Path]:
    if not runs_root.is_dir():
        return []
    return sorted(path for path in runs_root.iterdir() if path.is_dir())


def select_latest_run(run_paths: Sequence[Path], notes: List[str]) -> Optional[RunSelection]:
    if not run_paths:
        return None

    best_with_timestamp: Optional[
        Tuple[datetime, Path, Optional[Path], Optional[Path], Optional[Dict[str, Any]]]
    ] = None
    fallback_with_summary: Optional[Tuple[Path, Path, Optional[Path], Dict[str, Any]]] = None
    fallback_any_run: Optional[Path] = None

    for run_path in run_paths:
        fallback_any_run = run_path
        summary_path = run_path / "summary" / "summary.json"
        grounding_path = run_path / "grounding" / "grounding.json"

        if not summary_path.is_file():
            continue

        summary_payload, summary_error = safe_read_json(summary_path)
        if summary_error is not None:
            notes.append(f"Unreadable summary for {repo_relative(run_path)}: {summary_error}")
            continue

        fallback_with_summary = (run_path, summary_path, grounding_path if grounding_path.is_file() else None, summary_payload)
        parsed_generated_at = parse_generated_at(summary_payload.get("generated_at"))
        if parsed_generated_at is None:
            notes.append(
                "Summary generated_at was missing or unreadable for "
                f"{repo_relative(summary_path)}; using summary fallback if needed."
            )
            continue

        candidate = (
            parsed_generated_at,
            run_path,
            summary_path,
            grounding_path if grounding_path.is_file() else None,
            summary_payload,
        )
        if best_with_timestamp is None or candidate[0] > best_with_timestamp[0]:
            best_with_timestamp = candidate

    if best_with_timestamp is not None:
        generated_at, run_path, summary_path, grounding_path, summary_payload = best_with_timestamp
        return RunSelection(
            run_path=run_path,
            summary_path=summary_path,
            grounding_path=grounding_path,
            summary_generated_at=generated_at.isoformat().replace("+00:00", "Z"),
            summary_payload=summary_payload,
            selection_method="latest_summary_generated_at",
        )

    if fallback_with_summary is not None:
        run_path, summary_path, grounding_path, summary_payload = fallback_with_summary
        return RunSelection(
            run_path=run_path,
            summary_path=summary_path,
            grounding_path=grounding_path,
            summary_generated_at=summary_payload.get("generated_at")
            if isinstance(summary_payload.get("generated_at"), str)
            else None,
            summary_payload=summary_payload,
            selection_method="latest_discovered_summary_without_parsed_timestamp",
        )

    if fallback_any_run is not None:
        notes.append(
            "No readable summary was found for preserved runs under "
            f"{repo_relative(fallback_any_run.parent)}."
        )
        return RunSelection(
            run_path=fallback_any_run,
            summary_path=None,
            grounding_path=None,
            summary_generated_at=None,
            summary_payload=None,
            selection_method="latest_discovered_run_without_summary",
        )

    return None


def extract_grounding_paths(grounding_payload: Mapping[str, Any]) -> List[str]:
    grounding_surfaces = grounding_payload.get("grounding_surfaces")
    if not isinstance(grounding_surfaces, list):
        return []

    paths: List[str] = []
    for item in grounding_surfaces:
        if isinstance(item, Mapping):
            path_value = item.get("path")
            if isinstance(path_value, str):
                paths.append(path_value)
    return paths


def summarize_summary_payload(summary_payload: Optional[Mapping[str, Any]]) -> Dict[str, Any]:
    if summary_payload is None:
        return {
            "total_cases": None,
            "counts_by_outcome_type": None,
            "counts_by_receipt_status": None,
            "counts_by_failed_threshold_marker": None,
            "counts_by_upstream_responsibility_class": None,
            "counts_by_downstream_sovereignty_status": None,
            "counts_by_scapegoating_status": None,
            "scapegoating_presence_counts": None,
            "mismatched_cases": None,
            "mismatched_cases_present": None,
        }

    mismatched_cases = summary_payload.get("mismatched_cases")
    if not isinstance(mismatched_cases, list):
        mismatched_cases = None

    def mapping_or_none(key: str) -> Optional[Dict[str, Any]]:
        value = summary_payload.get(key)
        return dict(value) if isinstance(value, Mapping) else None

    return {
        "total_cases": summary_payload.get("total_cases"),
        "counts_by_outcome_type": mapping_or_none("counts_by_outcome_type"),
        "counts_by_receipt_status": mapping_or_none("counts_by_receipt_status"),
        "counts_by_failed_threshold_marker": mapping_or_none("failed_threshold_marker_counts"),
        "counts_by_upstream_responsibility_class": mapping_or_none(
            "counts_by_upstream_responsibility_class"
        ),
        "counts_by_downstream_sovereignty_status": mapping_or_none(
            "counts_by_downstream_sovereignty_status"
        ),
        "counts_by_scapegoating_status": mapping_or_none("counts_by_scapegoating_status"),
        "scapegoating_presence_counts": mapping_or_none("scapegoating_presence_counts"),
        "mismatched_cases": mismatched_cases,
        "mismatched_cases_present": bool(mismatched_cases) if mismatched_cases is not None else None,
    }


def read_grounding_payload(grounding_path: Optional[Path], notes: List[str]) -> Optional[Dict[str, Any]]:
    if grounding_path is None or not grounding_path.is_file():
        return None

    grounding_payload, grounding_error = safe_read_json(grounding_path)
    if grounding_error is not None:
        notes.append(
            f"Unreadable grounding file for {repo_relative(grounding_path.parent.parent)}: {grounding_error}"
        )
        return None
    return grounding_payload


def build_experiment_record(experiment_id: str) -> Dict[str, Any]:
    script_path = script_path_for_experiment(experiment_id)
    experiment_root = LAB_ROOT / experiment_id
    runs_root = experiment_root / "runs"

    notes: List[str] = []
    run_paths = list_run_paths(runs_root)
    latest_run = select_latest_run(run_paths, notes)

    summary_payload = latest_run.summary_payload if latest_run is not None else None
    grounding_payload = read_grounding_payload(
        latest_run.grounding_path if latest_run is not None else None,
        notes,
    )

    known_reading = KNOWN_EXPERIMENT_READINGS.get(
        experiment_id,
        {
            "experiment_role": "unclassified_seam_experiment",
            "experiment_reading": "Unclassified seam experiment family member.",
        },
    )

    if not script_path.is_file():
        notes.append(f"Script file is missing for {experiment_id}.")
    if not experiment_root.is_dir():
        notes.append(f"Experiment root is missing for {experiment_id}.")
    if not runs_root.is_dir():
        notes.append(f"Runs root is missing for {experiment_id}.")
    elif not run_paths:
        notes.append(f"No preserved runs were found under {repo_relative(runs_root)}.")

    record: Dict[str, Any] = {
        "experiment_id": experiment_id,
        "script_path": repo_relative(script_path),
        "script_exists": script_path.is_file(),
        "experiment_root_path": repo_relative(experiment_root),
        "experiment_root_exists": experiment_root.is_dir(),
        "runs_root_path": repo_relative(runs_root),
        "runs_root_exists": runs_root.is_dir(),
        "run_count": len(run_paths),
        "experiment_role": known_reading["experiment_role"],
        "experiment_reading": known_reading["experiment_reading"],
        "latest_run_path": repo_relative(latest_run.run_path) if latest_run is not None else None,
        "latest_summary_path": (
            repo_relative(latest_run.summary_path)
            if latest_run is not None and latest_run.summary_path is not None
            else None
        ),
        "latest_grounding_path": (
            repo_relative(latest_run.grounding_path)
            if latest_run is not None and latest_run.grounding_path is not None
            else None
        ),
        "latest_run_selection_method": latest_run.selection_method if latest_run is not None else None,
        "latest_summary_generated_at": (
            latest_run.summary_generated_at if latest_run is not None else None
        ),
        "latest_summary_reading": summarize_summary_payload(summary_payload),
        "grounding_surfaces": extract_grounding_paths(grounding_payload or {}),
        "partial_read_notes": notes,
    }

    return record


def build_family_notes(experiment_records: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    progression_visible: List[str] = []
    partial_material_detected: List[str] = []

    roles = {record.get("experiment_role") for record in experiment_records}

    if "threshold_met_seam_outcomes" in roles:
        progression_visible.append(
            "Experiment 001 reads as the threshold-met seam outcome surface."
        )
    if "threshold_not_yet_met_seam_outcomes" in roles:
        progression_visible.append(
            "Experiment 002 reads as the threshold-not-yet-met seam outcome surface."
        )
    if "responsibility_lineage_scapegoating_seam_outcomes" in roles:
        progression_visible.append(
            "Experiment 003 reads as the responsibility, lineage, and scapegoating surface."
        )
    if {
        "threshold_met_seam_outcomes",
        "threshold_not_yet_met_seam_outcomes",
        "responsibility_lineage_scapegoating_seam_outcomes",
    }.issubset(roles):
        progression_visible.append(
            "Across the family, the seam lab presently moves from threshold-met outcomes, "
            "to threshold-not-yet-met outcomes, to responsibility and lineage attribution."
        )

    for record in experiment_records:
        experiment_id = record.get("experiment_id")
        notes = record.get("partial_read_notes")
        if isinstance(notes, list) and notes:
            partial_material_detected.append(
                f"{experiment_id}: " + " | ".join(str(note) for note in notes)
            )

    return {
        "family_differences": progression_visible,
        "partial_or_unreadable_material": partial_material_detected,
        "note": (
            "This snapshot keeps the seam experiments readable as distinct proof turns. "
            "It does not turn the lab family into protocol law or full seam doctrine."
        ),
    }


def build_snapshot_payload(snapshot_path: Path) -> Dict[str, Any]:
    experiment_ids = discover_experiment_ids()
    experiment_records = [build_experiment_record(experiment_id) for experiment_id in experiment_ids]
    total_runs = sum(
        int(record.get("run_count", 0))
        for record in experiment_records
        if isinstance(record.get("run_count"), int)
    )

    return {
        "metadata": {
            "generated_at": utc_now(),
            "snapshot_builder_path": repo_relative(SCRIPT_PATH),
            "snapshot_source_root": repo_relative(LAB_ROOT),
            "snapshot_path": repo_relative(snapshot_path),
            "implementation_posture": "implementation_local_seam_lab_readability_only",
        },
        "experiment_family_summary": {
            "experiment_family_pattern": f"{EXPERIMENT_PREFIX}*",
            "total_experiments_discovered": len(experiment_ids),
            "total_runs_discovered": total_runs,
            "experiment_ids_discovered": experiment_ids,
        },
        "experiments": {record["experiment_id"]: record for record in experiment_records},
        "family_level_notes": build_family_notes(experiment_records),
    }


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    snapshot_path = choose_snapshot_path()

    try:
        payload = build_snapshot_payload(snapshot_path)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        write_snapshot(snapshot_path, payload)
    except OSError as exc:
        print(f"Failed to write seam experiment snapshot: {exc}", file=sys.stderr)
        return 1

    family_summary = payload["experiment_family_summary"]
    print("Seam experiment snapshot written.")
    print(f"Snapshot path: {repo_relative(snapshot_path)}")
    print(
        "Experiments discovered: "
        f"{family_summary['total_experiments_discovered']}"
    )
    print(f"Total runs discovered: {family_summary['total_runs_discovered']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
