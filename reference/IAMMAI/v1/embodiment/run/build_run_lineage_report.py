#!/usr/bin/env python3
"""
Bounded additive report builder for the preserved v1 run archive.

This script reads the current preserved run archive through the shared
run-inventory helper and writes one implementation-local human-readable report
under v1/registry/snapshots/ without rewriting any preserved run material.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, List, Optional, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
REPORTS_DIR = REPO_ROOT / "v1" / "registry" / "snapshots"
REPORT_TYPE = "v1_run_lineage_report"
IMPLEMENTATION_POSTURE = "implementation_local_readability_only"


try:
    from run_inventory import (  # type: ignore
        LINE_CONTINUITY,
        LINE_ORDINARY,
        RUNS_DIR,
        InventorySnapshot,
        RunRecord,
        build_inventory_snapshot,
    )
except ImportError:
    try:
        from v1.embodiment.run.run_inventory import (  # type: ignore
            LINE_CONTINUITY,
            LINE_ORDINARY,
            RUNS_DIR,
            InventorySnapshot,
            RunRecord,
            build_inventory_snapshot,
        )
    except ImportError as exc:
        LINE_CONTINUITY = "continuity"
        LINE_ORDINARY = "ordinary"
        RUNS_DIR = REPO_ROOT / "v1" / "registry" / "runs"
        InventorySnapshot = Any  # type: ignore[assignment]
        RunRecord = Any  # type: ignore[assignment]
        build_inventory_snapshot = None  # type: ignore[assignment]
        _INVENTORY_IMPORT_ERROR: Optional[ImportError] = exc
    else:
        _INVENTORY_IMPORT_ERROR = None
else:
    _INVENTORY_IMPORT_ERROR = None


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
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def choose_report_path(report_dir: Path) -> Path:
    base_name = f"run_lineage_report__{timestamp_slug()}"
    candidate = report_dir / f"{base_name}.md"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = report_dir / f"{base_name}__{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def render_report(
    inventory_snapshot: InventorySnapshot,
    *,
    report_path: Path,
) -> str:
    lines: List[str] = []
    lines.append("# IAMMAI v1 Run Lineage Report")
    lines.append("")
    lines.append(
        "This report is an implementation-local human-readable companion surface "
        "for the preserved v1 run archive. It does not rewrite preserved runs, "
        "normalize prior outputs by mutation, or claim protocol-law archival form."
    )
    lines.append("")
    lines.extend(render_metadata_section(inventory_snapshot, report_path))
    lines.extend(render_archive_summary_section(inventory_snapshot))
    lines.extend(render_line_section("Ordinary Line", inventory_snapshot.ordinary_runs))
    lines.extend(render_line_section("Continuity Line", inventory_snapshot.continuity_runs))
    lines.extend(render_unknown_section(inventory_snapshot.unknown_runs))
    lines.extend(render_notes_section(inventory_snapshot))
    return "\n".join(lines).rstrip() + "\n"


def render_metadata_section(
    inventory_snapshot: InventorySnapshot,
    report_path: Path,
) -> List[str]:
    return [
        "## Metadata",
        "",
        f"- Report type: `{REPORT_TYPE}`",
        f"- Generated at: `{utc_now()}`",
        f"- Implementation posture: `{IMPLEMENTATION_POSTURE}`",
        f"- Source archive root: `{repo_relative(inventory_snapshot.runs_dir)}`",
        f"- Report path: `{repo_relative(report_path)}`",
        "- Ordering note: entries follow the current `run_inventory.py` readability ordering. This is implementation-local support only.",
        "",
    ]


def render_archive_summary_section(inventory_snapshot: InventorySnapshot) -> List[str]:
    return [
        "## Archive Summary",
        "",
        f"- Ordinary runs: `{len(inventory_snapshot.ordinary_runs)}`",
        f"- Continuity runs: `{len(inventory_snapshot.continuity_runs)}`",
        f"- Unknown or unreadable runs: `{len(inventory_snapshot.unknown_runs)}`",
        "- Ordinary and continuity lines remain distinct in this report rather than flattened into one generic run list.",
        "",
    ]


def render_line_section(title: str, records: Sequence[RunRecord]) -> List[str]:
    lines: List[str] = [f"## {title}", ""]

    if not records:
        lines.append("- No preserved runs were discovered for this line.")
        lines.append("")
        return lines

    line_notes = collect_line_notes(records)
    for note in line_notes:
        lines.append(f"- {note}")
    lines.append("")

    for record in records:
        lines.extend(render_run_entry(record))

    return lines


def collect_line_notes(records: Sequence[RunRecord]) -> List[str]:
    notes: List[str] = []

    if any(record.layout_variant_notes for record in records):
        notes.append(
            "This line includes implementation-local layout variation that remains readable as lineage rather than contradiction."
        )

    if any(is_threshold_turn(record) for record in records):
        notes.append(
            "This line includes at least one preserved shared-implementation threshold turn."
        )

    if any("shared_preservation_layout" in record.operative_surfaces for record in records):
        notes.append("Shared preservation layout is operative on at least part of this line.")

    if any("shared_conformance" in record.operative_surfaces for record in records):
        notes.append("Shared conformance is operative on at least part of this line.")

    if any("shared_identifier_generation" in record.operative_surfaces for record in records):
        notes.append("Shared identifier generation is operative on at least part of this line.")

    if any("shared_source_selection" in record.operative_surfaces for record in records):
        notes.append("Shared source selection is operative on at least part of this line.")

    if any(record.anchor_source_run_ref for record in records):
        notes.append("Anchor-source readability is preserved where the archive supports it.")

    if any(record.predecessor_source_run_ref for record in records):
        notes.append("Predecessor-source readability is preserved where the archive supports it.")

    return notes


def render_run_entry(record: RunRecord) -> List[str]:
    lines: List[str] = []
    heading = record.turn_reading or record.execution_identity or repo_relative(record.run_directory)
    lines.append(f"### {heading}")
    lines.append("")
    lines.append(f"- Run class: `{record.run_class}`")
    if record.execution_identity:
        lines.append(f"- Execution identity: `{record.execution_identity}`")
    lines.append(f"- Run directory: `{repo_relative(record.run_directory)}`")
    if record.continuity_directory is not None:
        lines.append(f"- Continuity directory: `{repo_relative(record.continuity_directory)}`")
    if record.summary_type:
        lines.append(f"- Summary type: `{record.summary_type}`")
    if record.manifest_type:
        lines.append(f"- Manifest type: `{record.manifest_type}`")
    if record.summary_path is not None:
        lines.append(f"- Summary path: `{repo_relative(record.summary_path)}`")
    if record.manifest_path is not None:
        lines.append(f"- Manifest path: `{repo_relative(record.manifest_path)}`")
    if record.turn_rank is not None and record.turn_label:
        lines.append(f"- Turn rank: `{record.turn_rank}` (`{record.turn_label}`)")
    if record.matter_ref:
        lines.append(f"- Matter reference: `{record.matter_ref}`")
    if record.anchor_source_run_ref:
        lines.append(f"- Anchor source used: `{record.anchor_source_run_ref}`")
    if record.predecessor_source_run_ref:
        lines.append(f"- Predecessor source used: `{record.predecessor_source_run_ref}`")
    if record.predecessor_turn_identity:
        lines.append(f"- Predecessor turn identity: `{record.predecessor_turn_identity}`")
    if record.source_selection_basis:
        lines.append(f"- Source selection basis: `{record.source_selection_basis}`")

    lines.append(
        f"- Operative shared surfaces: {format_code_list(record.operative_surfaces) or 'none readable from preserved evidence'}"
    )
    lines.append(
        f"- Fixture material present: {'yes' if record.fixture_paths else 'no'}"
    )
    lines.append(
        f"- Preserved counts: canonical body `{len(record.canonical_body_paths)}`, "
        f"envelope `{len(record.envelope_paths)}`, execution relation `{len(record.execution_relation_paths)}`, "
        f"conformance `{len(record.conformance_paths)}`, source notes `{len(record.source_note_paths)}`"
    )

    surface_notes = render_surface_notes(record)
    for note in surface_notes:
        lines.append(f"- Surface note: {note}")

    for note in record.lineage_notes:
        lines.append(f"- Lineage note: {note}")

    for note in record.layout_variant_notes:
        lines.append(f"- Layout note: {note}")

    for note in record.unreadable_notes:
        lines.append(f"- Readability note: {note}")

    lines.append("")
    return lines


def render_surface_notes(record: RunRecord) -> List[str]:
    notes: List[str] = []
    for surface_name, evidence in sorted(record.operative_surface_evidence.items()):
        if not evidence:
            continue
        notes.append(f"`{surface_name}`: {evidence[0]}")
    return notes


def render_unknown_section(records: Sequence[RunRecord]) -> List[str]:
    lines: List[str] = ["## Unknown Or Unreadable Runs", ""]

    if not records:
        lines.append("- No unknown or unreadable run directories were discovered.")
        lines.append("")
        return lines

    lines.append(
        "- These entries remain visible as lineage material rather than being hidden because they are only partially readable."
    )
    lines.append("")

    for record in records:
        lines.append(f"### {record.execution_identity or repo_relative(record.run_directory)}")
        lines.append("")
        lines.append(f"- Run directory: `{repo_relative(record.run_directory)}`")
        if record.turn_reading:
            lines.append(f"- Reading: {record.turn_reading}")
        for note in record.unreadable_notes:
            lines.append(f"- Readability note: {note}")
        lines.append("")

    return lines


def render_notes_section(inventory_snapshot: InventorySnapshot) -> List[str]:
    lines: List[str] = ["## Bounded Notes", ""]
    notes = list(inventory_snapshot.snapshot_notes)
    notes.extend(
        [
            "This report is a companion readability surface to the JSON snapshot surface, not a replacement for it.",
            "The report remains implementation-local. It does not convert present readability heuristics into final protocol law.",
        ]
    )

    for note in unique_strings(notes):
        lines.append(f"- {note}")
    lines.append("")
    return lines


def format_code_list(values: Sequence[str]) -> str:
    if not values:
        return ""
    return ", ".join(f"`{value}`" for value in values)


def is_threshold_turn(record: RunRecord) -> bool:
    return any(
        "shared-implementation threshold turn" in note
        for note in record.lineage_notes
    )


def unique_strings(values: Iterable[str]) -> List[str]:
    seen = set()
    ordered: List[str] = []
    for value in values:
        if not value or value in seen:
            continue
        seen.add(value)
        ordered.append(value)
    return ordered


def write_report(report_path: Path, content: str) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(content, encoding="utf-8")


def main() -> int:
    if _INVENTORY_IMPORT_ERROR is not None or build_inventory_snapshot is None:
        print(
            "Failed to import the local run-inventory helper. Ensure "
            "v1/embodiment/run/run_inventory.py is importable before building a run-lineage report.",
            file=sys.stderr,
        )
        if _INVENTORY_IMPORT_ERROR is not None:
            print(str(_INVENTORY_IMPORT_ERROR), file=sys.stderr)
        return 1

    try:
        inventory_snapshot = build_inventory_snapshot(RUNS_DIR)
    except Exception as exc:
        print(
            "Failed to build a readable run inventory from v1/registry/runs/.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    report_path = choose_report_path(REPORTS_DIR)
    report_content = render_report(
        inventory_snapshot,
        report_path=report_path,
    )

    try:
        write_report(report_path, report_content)
    except OSError as exc:
        print(
            "Failed to write the run-lineage report under v1/registry/snapshots/.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    print("Bounded v1 run-lineage report written.")
    print(f"Report path: {repo_relative(report_path)}")
    print(f"Ordinary runs: {len(inventory_snapshot.ordinary_runs)}")
    print(f"Continuity runs: {len(inventory_snapshot.continuity_runs)}")
    print(f"Unknown runs: {len(inventory_snapshot.unknown_runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
