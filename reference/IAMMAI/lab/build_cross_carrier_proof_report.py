#!/usr/bin/env python3
"""
Build a bounded human-readable companion report for the first cross-carrier seam proof.

This script loads the existing cross-carrier proof snapshot builder, writes a
fresh machine-readable snapshot under lab/snapshots/, and renders one additive
Markdown report from that ranked data. It does not rerun the proof, mutate old
artifacts, or flatten source-side and receiving-side evidence into one event.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ID = "cross_carrier_seam_proof_001"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SNAPSHOT_BUILDER_PATH = LAB_ROOT / "build_cross_carrier_proof_snapshot.py"


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
    base_name = f"{PROOF_ID}_report__{timestamp_slug()}"
    candidate = SNAPSHOTS_ROOT / f"{base_name}.md"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = SNAPSHOTS_ROOT / f"{base_name}__{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def load_snapshot_builder() -> ModuleType:
    if not SNAPSHOT_BUILDER_PATH.is_file():
        raise RuntimeError(
            f"Cross-carrier proof snapshot builder is missing: {SNAPSHOT_BUILDER_PATH}"
        )

    spec = importlib.util.spec_from_file_location(
        "iammai_cross_carrier_proof_snapshot_builder",
        SNAPSHOT_BUILDER_PATH,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(
            f"Could not create an import specification for {SNAPSHOT_BUILDER_PATH}"
        )

    module = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        raise RuntimeError(
            f"Failed to import the cross-carrier proof snapshot builder: {exc}"
        ) from exc

    required_names = (
        "choose_snapshot_path",
        "build_snapshot_payload",
        "write_snapshot",
    )
    missing = [name for name in required_names if not callable(getattr(module, name, None))]
    if missing:
        raise RuntimeError(
            "Cross-carrier proof snapshot builder is missing required callables: "
            + ", ".join(missing)
        )

    return module


def build_fresh_snapshot() -> Tuple[Path, Dict[str, Any]]:
    builder = load_snapshot_builder()
    snapshot_path = builder.choose_snapshot_path()
    payload = builder.build_snapshot_payload(snapshot_path)
    if not isinstance(payload, dict):
        raise RuntimeError("Snapshot builder returned a non-object payload.")
    builder.write_snapshot(snapshot_path, payload)
    return snapshot_path, payload


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


def title_for_source_run(run_represents: str) -> str:
    mapping = {
        "lawful_package_release": "Lawful Package Release",
        "invalid_package_release_for_refusal_non_passage": (
            "Invalid Package Release For Refusal / Non-Passage"
        ),
        "source_release": "Source Release",
        "source_release_invalid": "Invalid Source Release",
    }
    return mapping.get(run_represents, "Source Release Run")


def find_source_run_by_representation(
    source_lineage: Mapping[str, Any],
    run_represents: str,
) -> Optional[Mapping[str, Any]]:
    for item in as_list(source_lineage.get("runs")):
        run = as_mapping(item)
        if run.get("run_represents") == run_represents:
            return run
    return None


def latest_branch_run(
    receiving_lineage: Mapping[str, Any],
    branch_name: str,
) -> Optional[Mapping[str, Any]]:
    branches = as_mapping(receiving_lineage.get("branches"))
    branch = as_mapping(branches.get(branch_name))
    runs = as_list(branch.get("runs"))
    if not runs:
        return None

    def sort_key(item: Any) -> str:
        run = as_mapping(item)
        generated_at = run.get("summary_generated_at")
        return generated_at if isinstance(generated_at, str) else ""

    return as_mapping(sorted(runs, key=sort_key)[-1])


def collect_partial_notes(payload: Mapping[str, Any]) -> List[str]:
    notes: List[str] = []

    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    notes.extend(str(note) for note in as_list(source_lineage.get("partial_read_notes")))
    for item in as_list(source_lineage.get("runs")):
        run = as_mapping(item)
        notes.extend(str(note) for note in as_list(run.get("partial_read_notes")))

    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    notes.extend(str(note) for note in as_list(receiving_lineage.get("partial_read_notes")))
    branches = as_mapping(receiving_lineage.get("branches"))
    for branch in branches.values():
        branch_record = as_mapping(branch)
        notes.extend(str(note) for note in as_list(branch_record.get("partial_read_notes")))
        for item in as_list(branch_record.get("runs")):
            run = as_mapping(item)
            notes.extend(str(note) for note in as_list(run.get("partial_read_notes")))

    internalization_note = as_mapping(payload.get("internalization_note"))
    for item in as_list(internalization_note.get("supporting_surfaces")):
        surface = as_mapping(item)
        read_error = surface.get("read_error")
        if isinstance(read_error, str) and read_error:
            path = surface.get("path")
            notes.append(f"Unreadable supporting surface {path}: {read_error}")

    return notes


def add_source_side_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    source_runs = as_list(source_lineage.get("runs"))

    lines.append("## Source-Side Release Lineage")
    lines.append("")
    lines.append(f"- Source run count: {md_code(source_lineage.get('source_run_count'))}")
    lines.append(
        f"- Source runs root: {md_code(source_lineage.get('source_runs_root'))}"
    )

    if not source_runs:
        lines.append("- No source-side release runs were readable in the current snapshot.")
        lines.append("")
        return

    preferred_order = (
        "lawful_package_release",
        "invalid_package_release_for_refusal_non_passage",
    )
    ordered_runs: List[Mapping[str, Any]] = []
    for run_represents in preferred_order:
        run = find_source_run_by_representation(source_lineage, run_represents)
        if run is not None:
            ordered_runs.append(run)
    for item in source_runs:
        run = as_mapping(item)
        if run not in ordered_runs:
            ordered_runs.append(run)

    lines.append("")
    for run in ordered_runs:
        lines.append(f"### {title_for_source_run(str(run.get('run_represents')))}")
        lines.append("")
        lines.append(f"- Execution id: {md_code(run.get('execution_id'))}")
        lines.append(f"- Path: {md_code(run.get('run_path'))}")
        lines.append(f"- Mode: {md_code(run.get('mode'))}")
        lines.append(
            "- Expected receiving outcome: "
            f"{md_code(run.get('expected_ingress_outcome'))}"
        )
        lines.append(
            "- Package ingress lawful if received: "
            f"{bool_literal(run.get('package_ingress_lawful_if_received'))}"
        )
        lines.append(
            f"- `source_remains_source = {str(run.get('source_remains_source')).lower() if run.get('source_remains_source') in (True, False) else 'unreadable'}`"
        )
        lines.append(
            f"- `shared_authority = {str(run.get('shared_authority')).lower() if run.get('shared_authority') in (True, False) else 'unreadable'}`"
        )
        lines.append(
            f"- `standing_transferred = {str(run.get('standing_transferred')).lower() if run.get('standing_transferred') in (True, False) else 'unreadable'}`"
        )
        lines.append(
            "- Package attempted unlawful standing transfer: "
            f"{bool_literal(run.get('package_attempted_unlawful_standing_transfer'))}"
        )
        lines.append("")


def add_receiving_branch_section(
    lines: List[str],
    payload: Mapping[str, Any],
    *,
    branch_name: str,
    title: str,
) -> None:
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    branches = as_mapping(receiving_lineage.get("branches"))
    branch = as_mapping(branches.get(branch_name))
    run = latest_branch_run(receiving_lineage, branch_name)

    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"- Imported branch: {md_code(branch.get('branch_name') or branch_name)}")
    lines.append(f"- Branch path: {md_code(branch.get('branch_path'))}")
    lines.append(f"- Imported run count: {md_code(branch.get('run_count'))}")

    if run is None:
        lines.append("- No readable imported run was available for this branch in the current snapshot.")
        lines.append("")
        return

    lines.append(f"- Receiving execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Imported run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Mode: {md_code(run.get('mode'))}")
    lines.append(f"- Ingress outcome: {md_code(run.get('ingress_outcome'))}")
    lines.append(f"- Ingress lawful: {bool_literal(run.get('ingress_lawful'))}")
    lines.append(f"- Arrival status: {md_code(run.get('arrival_status'))}")
    lines.append(
        f"- `source_remains_source = {str(run.get('source_remains_source')).lower() if run.get('source_remains_source') in (True, False) else 'unreadable'}`"
    )
    lines.append(
        f"- `shared_authority = {str(run.get('shared_authority')).lower() if run.get('shared_authority') in (True, False) else 'unreadable'}`"
    )
    lines.append(
        f"- `standing_upgraded = {str(run.get('standing_upgraded')).lower() if run.get('standing_upgraded') in (True, False) else 'unreadable'}`"
    )
    if branch_name == "lawful":
        lines.append(
            "- Receiving-side lawful ingress remains derivative-only rather than becoming silent standing."
        )
    else:
        lines.append(
            f"- `refusal_visible = {str(run.get('refusal_visible')).lower() if run.get('refusal_visible') in (True, False) else 'unreadable'}`"
        )
        lines.append(
            f"- `non_passage = {str(run.get('non_passage')).lower() if run.get('non_passage') in (True, False) else 'unreadable'}`"
        )
        lines.append(
            "- Receiving-side refusal remains visible rather than being hidden inside transport success."
        )
    lines.append("")


def render_report(
    payload: Mapping[str, Any],
    *,
    report_path: Path,
    snapshot_path: Path,
) -> str:
    lines: List[str] = []

    metadata = as_mapping(payload.get("metadata"))
    proof_identity = as_mapping(payload.get("proof_identity"))
    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    ranked_reading = as_mapping(payload.get("ranked_proof_reading"))
    internalization_note = as_mapping(payload.get("internalization_note"))

    lines.append("# Cross-Carrier Seam Proof 001 Report")
    lines.append("")
    lines.append(
        "This report is a human-readable companion to the machine-readable "
        "cross-carrier proof snapshot. It is an implementation-local readability "
        "surface only and does not function as protocol law."
    )
    lines.append("")
    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Generated at: {md_code(metadata.get('generated_at') or utc_now())}")
    lines.append(f"- Report path: {md_code(repo_relative(report_path))}")
    lines.append(f"- Source snapshot path: {md_code(repo_relative(snapshot_path))}")
    lines.append(f"- Proof root: {md_code(repo_relative(PROOF_ROOT))}")
    lines.append(f"- Proof id: {md_code(proof_identity.get('proof_id'))}")
    lines.append(f"- Proof name: {md_code(proof_identity.get('proof_name'))}")
    lines.append(
        "- Internalized archive status: "
        f"{bool_literal(proof_identity.get('internalized_archive_status'))}"
    )
    lines.append("")

    lines.append("## Current Proof Reading")
    lines.append("")
    lines.append(
        "The first cross-carrier seam proof presently reads as one ranked proof object "
        "with three distinct sides preserved in the same archive body."
    )
    lines.append("")
    lines.append(
        f"- Source-side release lineage remains source-side: {bool_literal(ranked_reading.get('source_side_release_lineage_remains_source_side'))}"
    )
    lines.append(
        f"- Receiving-side lawful ingress remains receiving-side: {bool_literal(ranked_reading.get('receiving_side_lawful_import_remains_receiving_side'))}"
    )
    lines.append(
        f"- Receiving-side refusal / non-passage remains receiving-side: {bool_literal(ranked_reading.get('receiving_side_refusal_import_remains_receiving_side'))}"
    )
    lines.append(
        f"- Import preserves relation without merger: {bool_literal(ranked_reading.get('import_preserves_relation_without_merger'))}"
    )
    lines.append(
        f"- Imported receiving-side evidence readability note: {md_code(receiving_lineage.get('import_note_path'))}"
    )
    bounded_reading = ranked_reading.get("bounded_reading")
    if isinstance(bounded_reading, str):
        lines.append("")
        lines.append(bounded_reading)
    lines.append("")

    add_source_side_section(lines, payload)
    add_receiving_branch_section(
        lines,
        payload,
        branch_name="lawful",
        title="Receiving-Side Lawful Ingress",
    )
    add_receiving_branch_section(
        lines,
        payload,
        branch_name="refusal_non_passage",
        title="Receiving-Side Refusal / Non-Passage",
    )

    lines.append("## Internalized Archive Relation")
    lines.append("")
    lines.append(
        "The current archive no longer carries only the source-side release runs. "
        "It now also carries imported receiving-side lawful ingress lineage and "
        "imported receiving-side refusal or non-passage lineage."
    )
    lines.append("")
    lines.append(
        "- Source run count inside the body: "
        f"{md_code(source_lineage.get('source_run_count'))}"
    )
    lines.append(
        "- Imported receiving branch count inside the body: "
        f"{md_code(receiving_lineage.get('imported_branch_count'))}"
    )
    lines.append(
        "- Internalized archive support note: "
        f"{md_code(internalization_note.get('bounded_reading'))}"
    )
    lines.append(
        "- Import note remains a readability surface only; it does not replace the imported run artifacts."
    )
    lines.append("")

    lines.append("## What This Shows")
    lines.append("")
    lines.append(
        "- Lawful derivative-only ingress is preserved as a receiving-side outcome rather than being rewritten as source-side history."
    )
    lines.append("- Source remains source across release and receiving-side ingress.")
    lines.append("- No silent authority inheritance is required for the proof to remain legible.")
    lines.append(
        "- Visible refusal and non-passage are preserved on the invalid transfer rather than disappearing into transport success."
    )
    lines.append(
        "- The proof is now internally carried on both sides without merger between source-side and receiving-side lineage."
    )
    lines.append("")

    lines.append("## What It Does Not Yet Show")
    lines.append("")
    lines.append("- Not yet a multi-carrier mesh.")
    lines.append("- Not yet bidirectional sync.")
    lines.append("- Not yet shared canonical state.")
    lines.append("- Not yet a relational field.")
    lines.append("- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.")
    lines.append("")

    partial_notes = collect_partial_notes(payload)
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
        "cross-carrier proof snapshot. It does not replace the snapshot, it does not "
        "rewrite prior artifacts, and it does not convert implementation-local "
        "readability into protocol law."
    )
    lines.append("")

    return "\n".join(lines)


def write_report(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def print_summary(
    *,
    report_path: Path,
    snapshot_path: Path,
    payload: Mapping[str, Any],
) -> None:
    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    print("Cross-carrier proof report written.")
    print(f"Report path: {repo_relative(report_path)}")
    print(f"Source snapshot path: {repo_relative(snapshot_path)}")
    print(f"Source run count: {source_lineage.get('source_run_count')}")
    print(f"Receiving imported branch count: {receiving_lineage.get('imported_branch_count')}")


def main() -> int:
    report_path = choose_report_path()

    try:
        snapshot_path, payload = build_fresh_snapshot()
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    report = render_report(payload, report_path=report_path, snapshot_path=snapshot_path)

    try:
        write_report(report_path, report)
    except OSError as exc:
        print(f"Failed to write cross-carrier proof report: {exc}", file=sys.stderr)
        return 1

    print_summary(report_path=report_path, snapshot_path=snapshot_path, payload=payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
