#!/usr/bin/env python3
"""
Bounded additive snapshot builder for the preserved v1 run archive.

This script reads the current preserved run archive through the shared
run-inventory helper and writes one implementation-local readability snapshot
under v1/registry/snapshots/ without rewriting any preserved run material.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[3]
SNAPSHOTS_DIR = REPO_ROOT / "v1" / "registry" / "snapshots"
SNAPSHOT_TYPE = "v1_run_lineage_snapshot"
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


def build_snapshot_payload(
    inventory_snapshot: InventorySnapshot,
    *,
    snapshot_path: Path,
) -> Dict[str, Any]:
    ordinary_line = build_line_section(
        line_name=LINE_ORDINARY,
        records=inventory_snapshot.ordinary_runs,
    )
    continuity_line = build_line_section(
        line_name=LINE_CONTINUITY,
        records=inventory_snapshot.continuity_runs,
    )
    unknown_entries = [build_unknown_entry(record) for record in inventory_snapshot.unknown_runs]

    return {
        "metadata": {
            "snapshot_type": SNAPSHOT_TYPE,
            "generated_at": utc_now(),
            "implementation_posture": IMPLEMENTATION_POSTURE,
            "snapshot_path": repo_relative(snapshot_path),
            "snapshot_source_root": repo_relative(inventory_snapshot.runs_dir),
            "snapshot_root": repo_relative(snapshot_path.parent),
            "ordering_note": (
                "Entries are ordered by run_inventory turn-rank readability, then "
                "execution identity, then run directory. This is "
                "implementation-local readability support only."
            ),
            "counts": {
                "ordinary_runs": len(inventory_snapshot.ordinary_runs),
                "continuity_runs": len(inventory_snapshot.continuity_runs),
                "unknown_runs": len(inventory_snapshot.unknown_runs),
            },
        },
        "ordinary_line": ordinary_line,
        "continuity_line": continuity_line,
        "unknown_runs": {
            "run_count": len(unknown_entries),
            "entries": unknown_entries,
        },
        "notes": unique_strings(
            list(inventory_snapshot.snapshot_notes)
            + [
                "This snapshot is an implementation-local readability artifact. It does not rewrite preserved runs or claim protocol-law archival form.",
                "Ordinary and continuity lines remain distinct in this snapshot rather than flattened into one generic run list.",
            ]
        ),
    }


def build_line_section(
    *,
    line_name: str,
    records: Sequence[RunRecord],
) -> Dict[str, Any]:
    entries = [build_line_entry(record) for record in records]
    threshold_entries = [build_threshold_entry(record) for record in records if is_threshold_turn(record)]
    operative_surfaces_seen = sorted(
        {surface for record in records for surface in record.operative_surfaces}
    )
    layout_variant_notes = unique_strings(
        note for record in records for note in record.layout_variant_notes
    )

    return {
        "line_name": line_name,
        "run_count": len(records),
        "operative_surfaces_seen": operative_surfaces_seen,
        "threshold_entries": threshold_entries,
        "entries": entries,
        "notes": build_line_notes(
            line_name=line_name,
            records=records,
            layout_variant_notes=layout_variant_notes,
            threshold_entries=threshold_entries,
        ),
    }


def build_line_entry(record: RunRecord) -> Dict[str, Any]:
    return {
        "run_class": record.run_class,
        "execution_identity": record.execution_identity,
        "run_directory": repo_relative(record.run_directory),
        "continuity_directory": (
            repo_relative(record.continuity_directory)
            if record.continuity_directory is not None
            else None
        ),
        "summary_path": repo_relative(record.summary_path) if record.summary_path else None,
        "manifest_path": repo_relative(record.manifest_path) if record.manifest_path else None,
        "summary_type": record.summary_type,
        "manifest_type": record.manifest_type,
        "turn_kind": record.turn_kind,
        "turn_rank": record.turn_rank,
        "turn_label": record.turn_label,
        "turn_reading": record.turn_reading,
        "matter_ref": record.matter_ref,
        "anchor_source_run_ref": record.anchor_source_run_ref,
        "predecessor_source_run_ref": record.predecessor_source_run_ref,
        "predecessor_turn_identity": record.predecessor_turn_identity,
        "source_selection_basis": record.source_selection_basis,
        "operative_surfaces": list(record.operative_surfaces),
        "operative_surface_evidence": {
            key: list(values)
            for key, values in sorted(record.operative_surface_evidence.items())
        },
        "fixture_present": bool(record.fixture_paths),
        "canonical_body_count": len(record.canonical_body_paths),
        "envelope_count": len(record.envelope_paths),
        "execution_relation_count": len(record.execution_relation_paths),
        "source_note_count": len(record.source_note_paths),
        "conformance_count": len(record.conformance_paths),
        "layout_variant_notes": list(record.layout_variant_notes),
        "lineage_notes": list(record.lineage_notes),
        "unreadable_notes": list(record.unreadable_notes),
    }


def build_unknown_entry(record: RunRecord) -> Dict[str, Any]:
    return {
        "run_class": record.run_class,
        "execution_identity": record.execution_identity,
        "run_directory": repo_relative(record.run_directory),
        "turn_reading": record.turn_reading,
        "unreadable_notes": list(record.unreadable_notes),
    }


def build_threshold_entry(record: RunRecord) -> Dict[str, Any]:
    return {
        "execution_identity": record.execution_identity,
        "run_directory": repo_relative(record.run_directory),
        "summary_type": record.summary_type,
        "turn_reading": record.turn_reading,
        "operative_surfaces": list(record.operative_surfaces),
    }


def build_line_notes(
    *,
    line_name: str,
    records: Sequence[RunRecord],
    layout_variant_notes: Sequence[str],
    threshold_entries: Sequence[Mapping[str, Any]],
) -> List[str]:
    notes: List[str] = []

    if not records:
        notes.append(f"No preserved {line_name} runs were discovered.")
        return notes

    if layout_variant_notes:
        notes.append(
            "This line includes implementation-local layout variation that remains readable as lineage rather than contradiction."
        )

    if threshold_entries:
        notes.append(
            "This line includes at least one preserved shared-implementation threshold turn."
        )

    if line_name == LINE_ORDINARY:
        if any("shared_preservation_layout" in record.operative_surfaces for record in records):
            notes.append(
                "Ordinary-line preserved runs show the additive progression from early proof slices into shared preservation layout."
            )
        if any("shared_conformance" in record.operative_surfaces for record in records):
            notes.append(
                "Ordinary-line preserved runs show later additive progression into shared conformance."
            )
        if any("shared_identifier_generation" in record.operative_surfaces for record in records):
            notes.append(
                "Ordinary-line preserved runs include later additive progression into shared identifier generation."
            )

    if line_name == LINE_CONTINUITY:
        if any(record.anchor_source_run_ref for record in records):
            notes.append(
                "Continuity-line preserved runs keep canonical anchor-source readability where the preserved material supports it."
            )
        if any(record.predecessor_source_run_ref for record in records):
            notes.append(
                "Continuity-line preserved runs keep predecessor-source readability where the preserved material supports it."
            )
        if any("shared_source_selection" in record.operative_surfaces for record in records):
            notes.append(
                "Continuity-line preserved runs show additive progression into shared source-selection posture."
            )
        if any("shared_preservation_layout" in record.operative_surfaces for record in records):
            notes.append(
                "Continuity-line preserved runs show later additive progression into shared preservation layout."
            )
        if any("shared_conformance" in record.operative_surfaces for record in records):
            notes.append(
                "Continuity-line preserved runs show later additive progression into shared conformance."
            )
        if any("shared_identifier_generation" in record.operative_surfaces for record in records):
            notes.append(
                "Continuity-line preserved runs include later additive progression into shared identifier generation."
            )

    return notes


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


def choose_snapshot_path(snapshot_dir: Path) -> Path:
    base_name = f"run_lineage_snapshot__{timestamp_slug()}"
    candidate = snapshot_dir / f"{base_name}.json"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = snapshot_dir / f"{base_name}__{counter}.json"
        if not candidate.exists():
            return candidate
        counter += 1


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(
        json.dumps(payload, indent=2) + "\n",
        encoding="utf-8",
    )


def main() -> int:
    if _INVENTORY_IMPORT_ERROR is not None or build_inventory_snapshot is None:
        print(
            "Failed to import the local run-inventory helper. Ensure "
            "v1/embodiment/run/run_inventory.py is importable before building a run-lineage snapshot.",
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

    snapshot_path = choose_snapshot_path(SNAPSHOTS_DIR)
    payload = build_snapshot_payload(
        inventory_snapshot,
        snapshot_path=snapshot_path,
    )

    try:
        write_snapshot(snapshot_path, payload)
    except OSError as exc:
        print(
            "Failed to write the run-lineage snapshot under v1/registry/snapshots/.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    print("Bounded v1 run-lineage snapshot written.")
    print(f"Snapshot path: {repo_relative(snapshot_path)}")
    print(f"Ordinary runs: {len(inventory_snapshot.ordinary_runs)}")
    print(f"Continuity runs: {len(inventory_snapshot.continuity_runs)}")
    print(f"Unknown runs: {len(inventory_snapshot.unknown_runs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
