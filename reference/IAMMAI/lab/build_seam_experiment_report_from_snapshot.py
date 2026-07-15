#!/usr/bin/env python3
"""
Build a bounded human-readable seam experiment family report from the latest snapshot.

This script reads the latest machine-readable seam experiment snapshot JSON from
lab/snapshots/ and renders one additive Markdown companion report. It does not
rerun experiments, regenerate the snapshot, mutate prior artifacts, or flatten
the seam lab into one generic doctrine object.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

SNAPSHOT_PREFIX = "seam_experiment_snapshot__"
REPORT_PREFIX = "seam_experiment_report"
SNAPSHOT_SUFFIX = ".json"

PREFERRED_EXPERIMENT_ORDER: Tuple[str, ...] = (
    "seam_outcome_experiment_001",
    "seam_outcome_experiment_002",
    "seam_outcome_experiment_003",
)


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


def choose_report_path() -> Path:
    base_name = f"{REPORT_PREFIX}__{timestamp_slug()}"
    candidate = SNAPSHOTS_ROOT / f"{base_name}.md"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = SNAPSHOTS_ROOT / f"{base_name}__{counter}.md"
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


def latest_snapshot_path() -> Path:
    if not SNAPSHOTS_ROOT.is_dir():
        raise FileNotFoundError(f"Snapshots directory is missing or unreadable: {SNAPSHOTS_ROOT}")

    candidates = [
        path
        for path in SNAPSHOTS_ROOT.iterdir()
        if path.is_file()
        and path.name.startswith(SNAPSHOT_PREFIX)
        and path.name.endswith(SNAPSHOT_SUFFIX)
    ]

    if not candidates:
        raise FileNotFoundError(
            f"No seam experiment snapshot files were found under {SNAPSHOTS_ROOT}"
        )

    try:
        return max(candidates, key=lambda path: (path.stat().st_mtime_ns, path.name))
    except OSError:
        return sorted(candidates)[-1]


def load_snapshot(path: Path) -> Dict[str, Any]:
    payload, error = safe_read_json(path)
    if error is not None:
        raise RuntimeError(f"Latest seam experiment snapshot is unreadable: {error}")
    assert payload is not None
    return payload


def as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def as_list(value: Any) -> List[Any]:
    return value if isinstance(value, list) else []


def md_code(value: Any) -> str:
    if value is None:
        return "`unreadable`"
    return f"`{value}`"


def bool_literal(value: Any) -> str:
    if value is True:
        return "`true`"
    if value is False:
        return "`false`"
    return "`unreadable`"


def format_count_map(data: Any) -> str:
    mapping = as_mapping(data)
    if not mapping:
        return "`unreadable`"
    return ", ".join(f"`{key}`={value}" for key, value in mapping.items())


def ordered_experiment_ids(experiments: Mapping[str, Any]) -> List[str]:
    ordered: List[str] = []
    for experiment_id in PREFERRED_EXPERIMENT_ORDER:
        if experiment_id in experiments:
            ordered.append(experiment_id)
    for experiment_id in sorted(experiments):
        if experiment_id not in ordered:
            ordered.append(experiment_id)
    return ordered


def experiment_heading(record: Mapping[str, Any]) -> str:
    experiment_id = record.get("experiment_id")
    experiment_role = record.get("experiment_role")
    if experiment_role == "threshold_met_seam_outcomes":
        return f"{experiment_id} - Threshold-Met Seam Outcomes"
    if experiment_role == "threshold_not_yet_met_seam_outcomes":
        return f"{experiment_id} - Threshold-Not-Yet-Met Seam Outcomes"
    if experiment_role == "responsibility_lineage_scapegoating_seam_outcomes":
        return f"{experiment_id} - Responsibility / Lineage / Scapegoating"
    return str(experiment_id)


def collect_partial_notes(snapshot: Mapping[str, Any]) -> List[str]:
    notes: List[str] = []

    experiments = as_mapping(snapshot.get("experiments"))
    for experiment_id in ordered_experiment_ids(experiments):
        record = as_mapping(experiments.get(experiment_id))
        for note in as_list(record.get("partial_read_notes")):
            notes.append(f"{experiment_id}: {note}")

    family_notes = as_mapping(snapshot.get("family_level_notes"))
    for note in as_list(family_notes.get("partial_or_unreadable_material")):
        notes.append(str(note))

    return notes


def add_experiment_section(lines: List[str], record: Mapping[str, Any]) -> None:
    summary_reading = as_mapping(record.get("latest_summary_reading"))

    lines.append(f"## {experiment_heading(record)}")
    lines.append("")
    lines.append(f"- Experiment reading: {record.get('experiment_reading', 'Unreadable experiment reading.')}")
    lines.append(f"- Script path: {md_code(record.get('script_path'))}")
    lines.append(f"- Experiment root: {md_code(record.get('experiment_root_path'))}")
    lines.append(f"- Runs root: {md_code(record.get('runs_root_path'))}")
    lines.append(f"- Run count: {md_code(record.get('run_count'))}")
    lines.append(f"- Latest run path: {md_code(record.get('latest_run_path'))}")
    lines.append(f"- Latest summary path: {md_code(record.get('latest_summary_path'))}")
    lines.append(f"- Latest summary generated at: {md_code(record.get('latest_summary_generated_at'))}")
    lines.append(
        f"- Total cases in latest readable summary: {md_code(summary_reading.get('total_cases'))}"
    )
    lines.append(
        f"- Latest outcome counts: {format_count_map(summary_reading.get('counts_by_outcome_type'))}"
    )
    lines.append(
        f"- Latest receipt counts: {format_count_map(summary_reading.get('counts_by_receipt_status'))}"
    )

    if summary_reading.get("counts_by_failed_threshold_marker") is not None:
        lines.append(
            "- Latest failed-threshold-marker counts: "
            f"{format_count_map(summary_reading.get('counts_by_failed_threshold_marker'))}"
        )
    if summary_reading.get("counts_by_upstream_responsibility_class") is not None:
        lines.append(
            "- Latest upstream-responsibility counts: "
            f"{format_count_map(summary_reading.get('counts_by_upstream_responsibility_class'))}"
        )
    if summary_reading.get("counts_by_downstream_sovereignty_status") is not None:
        lines.append(
            "- Latest downstream-sovereignty counts: "
            f"{format_count_map(summary_reading.get('counts_by_downstream_sovereignty_status'))}"
        )
    if summary_reading.get("counts_by_scapegoating_status") is not None:
        lines.append(
            "- Latest scapegoating counts: "
            f"{format_count_map(summary_reading.get('counts_by_scapegoating_status'))}"
        )
    if summary_reading.get("scapegoating_presence_counts") is not None:
        lines.append(
            "- Latest scapegoating-presence counts: "
            f"{format_count_map(summary_reading.get('scapegoating_presence_counts'))}"
        )

    lines.append(
        "- Mismatched cases present: "
        f"{bool_literal(summary_reading.get('mismatched_cases_present'))}"
    )

    mismatched_cases = summary_reading.get("mismatched_cases")
    if isinstance(mismatched_cases, list) and mismatched_cases:
        lines.append(
            "- Mismatched case ids: "
            + ", ".join(str(item) for item in mismatched_cases)
        )

    for note in as_list(record.get("partial_read_notes")):
        lines.append(f"- Partial read note: {note}")

    lines.append("")


def render_report(
    snapshot: Mapping[str, Any],
    *,
    report_path: Path,
    source_snapshot_path: Path,
) -> str:
    lines: List[str] = []

    metadata = as_mapping(snapshot.get("metadata"))
    family_summary = as_mapping(snapshot.get("experiment_family_summary"))
    experiments = as_mapping(snapshot.get("experiments"))
    family_notes = as_mapping(snapshot.get("family_level_notes"))

    lines.append("# Seam Experiment Family Report")
    lines.append("")
    lines.append(
        "This report is a human-readable companion to the machine-readable seam "
        "experiment family snapshot. It is an implementation-local readability "
        "surface only and does not function as protocol law."
    )
    lines.append("")

    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Generated at: {md_code(utc_now())}")
    lines.append(f"- Source snapshot path: {md_code(repo_relative(source_snapshot_path))}")
    lines.append(
        f"- Snapshot generated at: {md_code(metadata.get('generated_at'))}"
    )
    lines.append(
        f"- Lab root: {md_code(metadata.get('snapshot_source_root') or repo_relative(LAB_ROOT))}"
    )
    lines.append(f"- Report path: {md_code(repo_relative(report_path))}")
    lines.append("")

    lines.append("## Family Summary")
    lines.append("")
    lines.append(
        "- Total seam experiments discovered: "
        f"{md_code(family_summary.get('total_experiments_discovered'))}"
    )
    lines.append(
        "- Total runs discovered across the family: "
        f"{md_code(family_summary.get('total_runs_discovered'))}"
    )
    lines.append(
        "- Experiment ids present: "
        f"{md_code(', '.join(str(item) for item in as_list(family_summary.get('experiment_ids_discovered'))))}"
    )
    lines.append("")

    lines.append("## Family Progression")
    lines.append("")
    progression = as_list(family_notes.get("family_differences"))
    if progression:
        for note in progression:
            lines.append(f"- {note}")
    else:
        lines.append("- The current snapshot did not preserve a readable progression note.")
    lines.append("")

    for experiment_id in ordered_experiment_ids(experiments):
        add_experiment_section(lines, as_mapping(experiments.get(experiment_id)))

    lines.append("## What The Seam Lab Now Shows")
    lines.append("")
    lines.append(
        "- The seam lab presently preserves distinct executable proof turns rather than one flat seam object."
    )
    lines.append(
        "- Experiment 001 reads as threshold-met seam outcomes under contaminated-channel conditions."
    )
    lines.append(
        "- Experiment 002 reads as threshold-not-yet-met seam outcomes where lawful crossing is blocked by insufficient self-carriage."
    )
    lines.append(
        "- Experiment 003 reads as responsibility, lineage, and scapegoating outcomes under constrained or contaminated channels."
    )
    lines.append(
        "- Across the family, the lab now makes threshold state, outcome type, and attribution pressure readable without turning the experiments into protocol law."
    )
    lines.append("")

    lines.append("## What It Does Not Yet Show")
    lines.append("")
    lines.append("- Not total seam doctrine.")
    lines.append("- Not a full middleware layer.")
    lines.append("- Not all seam cases exhausted.")
    lines.append("- Not a final closure of every threshold, refusal, buffer, or attribution form.")
    lines.append("- Not permission to flatten the family into one generic seam summary.")
    lines.append("")

    partial_notes = collect_partial_notes(snapshot)
    if partial_notes:
        lines.append("## Partial Read Notes")
        lines.append("")
        for note in partial_notes:
            lines.append(f"- {note}")
        lines.append("")

    lines.append("## Boundary Note")
    lines.append("")
    lines.append(
        "This report is an additive human-readable companion to the machine-readable "
        "seam experiment snapshot. It does not replace the snapshot, it does not "
        "rewrite prior experiments, and it does not convert implementation-local "
        "readability into protocol law."
    )
    lines.append("")

    return "\n".join(lines)


def write_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def print_summary(*, source_snapshot_path: Path, report_path: Path) -> None:
    print("Seam experiment report written.")
    print(f"Source snapshot path: {repo_relative(source_snapshot_path)}")
    print(f"Report path: {repo_relative(report_path)}")


def main() -> int:
    try:
        source_snapshot_path = latest_snapshot_path()
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        snapshot = load_snapshot(source_snapshot_path)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    report_path = choose_report_path()
    report = render_report(
        snapshot,
        report_path=report_path,
        source_snapshot_path=source_snapshot_path,
    )

    try:
        write_report(report_path, report)
    except OSError as exc:
        print(f"Failed to write seam experiment report: {exc}", file=sys.stderr)
        return 1

    print_summary(source_snapshot_path=source_snapshot_path, report_path=report_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
