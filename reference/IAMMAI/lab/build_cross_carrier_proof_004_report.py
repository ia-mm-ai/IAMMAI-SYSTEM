#!/usr/bin/env python3
"""
Build a bounded human-readable companion report for the fourth cross-carrier seam proof.

This script prefers the latest machine-readable proof 004 snapshot already
present under lab/snapshots/. If no readable snapshot is present, it falls back
to the proof 004 snapshot builder to generate one, then renders one additive
Markdown companion report without rerunning the proof or mutating prior runs.
"""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ID = "cross_carrier_seam_proof_004"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SNAPSHOT_BUILDER_PATH = LAB_ROOT / "build_cross_carrier_proof_004_snapshot.py"
SNAPSHOT_PREFIX = f"{PROOF_ID}_snapshot__"
SNAPSHOT_SUFFIX = ".json"
REPORT_PREFIX = f"{PROOF_ID}_report"
TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH = PROOF_ROOT / "receiver_local_condition.json"

TIMESTAMP_PATTERN = re.compile(r"^(?P<stamp>\d{8}T\d{6}Z)(?:__(?P<counter>\d+))?$")


@dataclass(frozen=True, order=True)
class SnapshotCandidate:
    timestamp: str
    counter: int
    filename: str
    path: Path


@dataclass(frozen=True)
class ResolvedSnapshot:
    path: Path
    payload: Dict[str, Any]
    acquisition_mode: str
    notes: Tuple[str, ...]


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


def ensure_snapshots_root() -> Path:
    resolved = SNAPSHOTS_ROOT.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Snapshots directory is missing or unreadable: {resolved}")
    return resolved


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


def iter_snapshot_candidates(snapshot_dir: Path) -> Sequence[SnapshotCandidate]:
    candidates: List[SnapshotCandidate] = []

    for path in sorted(snapshot_dir.iterdir()):
        if not path.is_file():
            continue
        if path.suffix != SNAPSHOT_SUFFIX:
            continue
        if not path.name.startswith(SNAPSHOT_PREFIX):
            continue

        stem_tail = path.name[len(SNAPSHOT_PREFIX) : -len(SNAPSHOT_SUFFIX)]
        match = TIMESTAMP_PATTERN.match(stem_tail)
        if match is None:
            continue

        candidates.append(
            SnapshotCandidate(
                timestamp=match.group("stamp"),
                counter=int(match.group("counter") or "1"),
                filename=path.name,
                path=path,
            )
        )

    return candidates


def latest_snapshot_path(snapshot_dir: Path) -> Path:
    candidates = list(iter_snapshot_candidates(snapshot_dir))
    if not candidates:
        raise FileNotFoundError(
            f"No proof 004 snapshot files were found under {snapshot_dir.resolve()}"
        )
    return max(candidates).path


def load_snapshot(path: Path) -> Dict[str, Any]:
    payload, error = safe_read_json(path)
    if error is not None:
        raise RuntimeError(f"Snapshot is unreadable: {error}")
    assert payload is not None
    return payload


def load_snapshot_builder(path: Path) -> ModuleType:
    if not path.is_file():
        raise FileNotFoundError(f"Snapshot builder is missing: {path}")

    spec = importlib.util.spec_from_file_location(
        "iammai_cross_carrier_proof_004_snapshot_builder",
        path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load snapshot builder spec from {path}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for attribute in ("choose_snapshot_path", "build_snapshot_payload", "write_snapshot"):
        if not hasattr(module, attribute):
            raise RuntimeError(
                f"Snapshot builder is missing required attribute {attribute!r}: {path}"
            )

    return module


def resolve_snapshot() -> ResolvedSnapshot:
    ensure_snapshots_root()
    notes: List[str] = []

    try:
        existing_path = latest_snapshot_path(SNAPSHOTS_ROOT)
        existing_payload = load_snapshot(existing_path)
        return ResolvedSnapshot(
            path=existing_path,
            payload=existing_payload,
            acquisition_mode="existing_snapshot",
            notes=tuple(notes),
        )
    except FileNotFoundError:
        notes.append("No readable proof 004 snapshot was present. A fresh snapshot was generated.")
    except RuntimeError as exc:
        notes.append(f"Latest proof 004 snapshot was unreadable and was replaced by a fresh snapshot: {exc}")

    builder = load_snapshot_builder(SNAPSHOT_BUILDER_PATH)
    snapshot_path = builder.choose_snapshot_path()
    payload = builder.build_snapshot_payload(snapshot_path)
    builder.write_snapshot(snapshot_path, payload)

    return ResolvedSnapshot(
        path=snapshot_path,
        payload=payload,
        acquisition_mode="generated_snapshot",
        notes=tuple(notes),
    )


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


def source_run_by_represents(
    source_lineage: Mapping[str, Any],
    run_represents: str,
) -> Optional[Mapping[str, Any]]:
    for record in as_list(source_lineage.get("runs")):
        mapping = as_mapping(record)
        if mapping.get("run_represents") == run_represents:
            return mapping
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
    latest = runs[-1]
    return as_mapping(latest)


def collect_partial_notes(
    snapshot: Mapping[str, Any],
    resolved_snapshot: ResolvedSnapshot,
) -> List[str]:
    notes: List[str] = list(resolved_snapshot.notes)

    source_lineage = as_mapping(snapshot.get("source_side_release_lineage"))
    notes.extend(str(note) for note in as_list(source_lineage.get("partial_read_notes")))
    for item in as_list(source_lineage.get("runs")):
        record = as_mapping(item)
        execution_id = record.get("execution_id") or "unknown-source-run"
        for note in as_list(record.get("partial_read_notes")):
            notes.append(f"{execution_id}: {note}")

    receiving_lineage = as_mapping(snapshot.get("receiving_side_imported_lineage"))
    notes.extend(str(note) for note in as_list(receiving_lineage.get("partial_read_notes")))
    branches = as_mapping(receiving_lineage.get("branches"))
    for branch_name, branch_value in branches.items():
        branch = as_mapping(branch_value)
        for note in as_list(branch.get("partial_read_notes")):
            notes.append(f"{branch_name}: {note}")
        for item in as_list(branch.get("runs")):
            record = as_mapping(item)
            execution_id = record.get("execution_id") or f"{branch_name}-run"
            for note in as_list(record.get("partial_read_notes")):
                notes.append(f"{execution_id}: {note}")

    threshold_note = as_mapping(snapshot.get("lawful_egress_threshold_note"))
    notes.extend(str(note) for note in as_list(threshold_note.get("partial_read_notes")))

    if not TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH.is_file():
        notes.append(
            "No top-level receiver-local condition surface is currently preserved at "
            f"{repo_relative(TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH)}."
        )

    deduped: List[str] = []
    seen = set()
    for note in notes:
        if note in seen:
            continue
        seen.add(note)
        deduped.append(note)
    return deduped


def add_metadata_section(
    lines: List[str],
    snapshot: Mapping[str, Any],
    *,
    resolved_snapshot: ResolvedSnapshot,
    report_path: Path,
) -> None:
    metadata = as_mapping(snapshot.get("metadata"))
    proof_identity = as_mapping(snapshot.get("proof_identity"))

    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Generated at: {md_code(utc_now())}")
    lines.append(f"- Report path: {md_code(repo_relative(report_path))}")
    lines.append(f"- Source snapshot path: {md_code(repo_relative(resolved_snapshot.path))}")
    lines.append(f"- Source snapshot generated at: {md_code(metadata.get('generated_at'))}")
    lines.append(f"- Snapshot acquisition mode: {md_code(resolved_snapshot.acquisition_mode)}")
    lines.append(f"- Proof root: {md_code(PROOF_ROOT.relative_to(REPO_ROOT))}")
    lines.append(f"- Proof id: {md_code(proof_identity.get('proof_id'))}")
    lines.append(f"- Proof name: {md_code(proof_identity.get('proof_name'))}")
    lines.append(
        f"- Internalized archive status: {bool_literal(proof_identity.get('internalized_archive_status'))}"
    )
    lines.append("")


def add_current_proof_reading_section(lines: List[str], snapshot: Mapping[str, Any]) -> None:
    ranked = as_mapping(snapshot.get("ranked_proof_reading"))
    source_lineage = as_mapping(snapshot.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(snapshot.get("receiving_side_imported_lineage"))
    outcome = as_mapping(snapshot.get("outcome_reading"))
    source_reading = as_mapping(outcome.get("source_side_release_reading"))
    receiving_reading = as_mapping(outcome.get("receiving_side_arrival_reading"))
    clean_source = as_mapping(source_reading.get("clean_origin_release"))
    obsolete_source = as_mapping(source_reading.get("obsolete_origin_lawful_egress"))
    clean_receiving = as_mapping(receiving_reading.get("clean_bounded_in_between_arrival"))
    obsolete_receiving = as_mapping(
        receiving_reading.get("obsolete_origin_bounded_in_between_arrival")
    )

    lines.append("## Current Proof Reading")
    lines.append("")
    lines.append(
        "The fourth cross-carrier seam proof presently reads as one ranked proof object "
        "with two source-side release turns and two imported receiving-side bounded "
        "arrival turns preserved in the same body."
    )
    lines.append("")
    lines.append(
        "- Source-side release lineage remains source-side: "
        f"{bool_literal(ranked.get('source_side_release_lineage_remains_source_side'))}"
    )
    lines.append(
        "- Receiving-side clean bounded in-between arrival remains receiving-side: "
        f"{bool_literal(ranked.get('receiving_side_clean_bounded_in_between_arrival_remains_receiving_side'))}"
    )
    lines.append(
        "- Receiving-side obsolete-origin bounded in-between arrival remains receiving-side: "
        f"{bool_literal(ranked.get('receiving_side_obsolete_origin_bounded_in_between_arrival_remains_receiving_side'))}"
    )
    lines.append(
        "- Import preserves relation without merger: "
        f"{bool_literal(ranked.get('import_preserves_relation_without_merger'))}"
    )
    lines.append(
        "- Internalized archive status: "
        f"{bool_literal(as_mapping(snapshot.get('proof_identity')).get('internalized_archive_status'))}"
    )
    lines.append(f"- Source run count: {md_code(source_lineage.get('source_run_count'))}")
    lines.append(
        f"- Imported receiving branch count: {md_code(receiving_lineage.get('imported_branch_count'))}"
    )
    lines.append(f"- Clean source execution id: {md_code(clean_source.get('execution_id'))}")
    lines.append(f"- Obsolete-origin source execution id: {md_code(obsolete_source.get('execution_id'))}")
    lines.append(
        f"- Clean receiving execution id: {md_code(clean_receiving.get('execution_id'))}"
    )
    lines.append(
        f"- Obsolete-origin receiving execution id: {md_code(obsolete_receiving.get('execution_id'))}"
    )
    lines.append("")
    bounded_reading = ranked.get("bounded_reading")
    if isinstance(bounded_reading, str):
        lines.append(bounded_reading)
        lines.append("")


def add_source_section(lines: List[str], run: Mapping[str, Any], *, title: str, summary_text: str) -> None:
    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"- Source execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Source run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Summary path: {md_code(run.get('summary_path'))}")
    lines.append(f"- Manifest path: {md_code(run.get('manifest_path'))}")
    lines.append(f"- Origin approval condition path: {md_code(run.get('origin_approval_condition_path'))}")
    lines.append(f"- Package path: {md_code(run.get('package_path'))}")
    lines.append(f"- Run represents: {md_code(run.get('run_represents'))}")
    lines.append(f"- Origin approval condition status: {md_code(run.get('origin_approval_condition_status'))}")
    lines.append(
        f"- Origin approval lawfully sovereign: {bool_literal(run.get('origin_approval_lawfully_sovereign'))}"
    )
    lines.append(
        f"- Release without origin ratification: {bool_literal(run.get('release_without_origin_ratification'))}"
    )
    if run.get("continued_compliance_would_ratify_distortion") is not None:
        lines.append(
            "- Continued compliance would ratify distortion: "
            f"{bool_literal(run.get('continued_compliance_would_ratify_distortion'))}"
        )
    lines.append(f"- Release lawful: {bool_literal(run.get('release_lawful'))}")
    if run.get("lawful_release_outcome") is not None:
        lines.append(f"- Lawful release outcome: {md_code(run.get('lawful_release_outcome'))}")
    lines.append(f"- Source remains source: {bool_literal(run.get('source_remains_source'))}")
    lines.append(
        f"- Origin remains lineage-visible: {bool_literal(run.get('origin_remains_lineage_visible'))}"
    )
    lines.append(f"- Package valid: {bool_literal(run.get('package_valid'))}")
    lines.append(f"- Expected arrival status: {md_code(run.get('expected_arrival_status'))}")
    lines.append(
        f"- Downstream full closure granted: {bool_literal(run.get('downstream_full_closure_granted'))}"
    )
    lines.append("")
    lines.append(summary_text)
    lines.append("")


def add_receiving_section(
    lines: List[str],
    *,
    branch_name: str,
    run: Mapping[str, Any],
    summary_text: str,
) -> None:
    title = (
        "Receiving-Side Clean Bounded In-Between Arrival"
        if branch_name == "clean"
        else "Receiving-Side Obsolete-Origin Bounded In-Between Arrival"
    )
    lines.append(f"## {title}")
    lines.append("")
    lines.append(f"- Imported branch: {md_code(branch_name)}")
    lines.append(f"- Receiving execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Imported run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Summary path: {md_code(run.get('summary_path'))}")
    lines.append(f"- Manifest path: {md_code(run.get('manifest_path'))}")
    lines.append(
        "- Origin approval condition snapshot path: "
        f"{md_code(run.get('origin_approval_condition_snapshot_path'))}"
    )
    lines.append(f"- Package id: {md_code(run.get('package_id'))}")
    lines.append(
        f"- Origin approval condition status: {md_code(run.get('origin_approval_condition_status'))}"
    )
    if run.get("origin_approval_lawfully_sovereign") is not None:
        lines.append(
            "- Origin approval lawfully sovereign: "
            f"{bool_literal(run.get('origin_approval_lawfully_sovereign'))}"
        )
    lines.append(f"- Technical receipt: {bool_literal(run.get('technical_receipt'))}")
    lines.append(f"- Package valid: {bool_literal(run.get('package_valid'))}")
    lines.append(f"- Ingress lawful: {bool_literal(run.get('ingress_lawful'))}")
    lines.append(f"- Ingress outcome: {md_code(run.get('ingress_outcome'))}")
    lines.append(f"- Arrival status: {md_code(run.get('arrival_status'))}")
    lines.append(f"- Source remains source: {bool_literal(run.get('source_remains_source'))}")
    lines.append(
        f"- Origin remains lineage-visible: {bool_literal(run.get('origin_remains_lineage_visible'))}"
    )
    lines.append(f"- Shared authority: {bool_literal(run.get('shared_authority'))}")
    lines.append(f"- Standing upgraded: {bool_literal(run.get('standing_upgraded'))}")
    lines.append(f"- Final closure claimed: {bool_literal(run.get('final_closure_claimed'))}")
    lines.append(
        f"- Release without origin ratification: {bool_literal(run.get('release_without_origin_ratification'))}"
    )
    lines.append("")
    lines.append(summary_text)
    lines.append("")


def add_lawful_egress_section(lines: List[str], snapshot: Mapping[str, Any]) -> None:
    threshold_note = as_mapping(snapshot.get("lawful_egress_threshold_note"))
    evidence = as_mapping(threshold_note.get("evidence_support"))
    supporting_surfaces = as_list(threshold_note.get("supporting_surfaces"))
    import_surface = as_mapping(supporting_surfaces[0]) if len(supporting_surfaces) > 0 else {}
    seam_surface = as_mapping(supporting_surfaces[1]) if len(supporting_surfaces) > 1 else {}
    account_surface = as_mapping(supporting_surfaces[2]) if len(supporting_surfaces) > 2 else {}

    lines.append("## Lawful Egress Threshold")
    lines.append("")
    lines.append(
        "The specific architectural advance in proof 004 is that origin may remain "
        "source and lineage-visible while obsolete or contaminated origin approval "
        "loses sovereignty, lawful egress proceeds without obsolete-origin "
        "ratification, and receiving-side arrival remains bounded in-between rather "
        "than counterfeit full closure."
    )
    lines.append("")
    lines.append(
        "- Lawful egress from obsolete container supported: "
        f"{bool_literal(threshold_note.get('lawful_egress_from_obsolete_container_supported'))}"
    )
    lines.append(
        "- Source-side obsolete-origin non-sovereign approval visible: "
        f"{bool_literal(evidence.get('source_side_obsolete_origin_non_sovereign_visible'))}"
    )
    lines.append(
        "- Receiving-side obsolete-origin bounded in-between arrival visible: "
        f"{bool_literal(evidence.get('receiving_side_obsolete_origin_bounded_in_between_arrival_visible'))}"
    )
    lines.append(
        "- Clean control bounded in-between arrival visible: "
        f"{bool_literal(evidence.get('clean_control_bounded_in_between_arrival_visible'))}"
    )
    lines.append(f"- Import note path: {md_code(import_surface.get('path'))}")
    lines.append(f"- Seam case law path: {md_code(seam_surface.get('path'))}")
    lines.append(f"- Transfer-account entry path: {md_code(account_surface.get('path'))}")
    lines.append("")
    bounded_reading = threshold_note.get("bounded_reading")
    if isinstance(bounded_reading, str):
        lines.append(bounded_reading)
        lines.append("")
    lines.append(
        "The import note remains a readability aid only. It makes imported "
        "receiving-side evidence easier to read, but it does not replace the "
        "underlying receiving-side run artifacts."
    )
    lines.append("")


def add_what_this_shows_section(lines: List[str]) -> None:
    lines.append("## What This Shows")
    lines.append("")
    lines.append("- Lawful release from clean origin approval remains visible as a bounded comparison case.")
    lines.append("- Lawful egress from obsolete or contaminated origin remains visible without treating withheld origin approval as sovereign veto.")
    lines.append("- Bounded in-between arrival is preserved on both receiving-side branches.")
    lines.append("- Source remains source and origin remains lineage-visible across release and imported arrival.")
    lines.append("- No silent authority inheritance, standing upgrade, or final closure is claimed on the far side.")
    lines.append("- Imported receiving-side evidence remains receiving-side evidence even after it is carried back into the main body.")
    lines.append("")


def add_what_it_does_not_show_section(lines: List[str]) -> None:
    lines.append("## What It Does Not Yet Show")
    lines.append("")
    lines.append("- Not yet a multi-carrier mesh.")
    lines.append("- Not yet bidirectional sync.")
    lines.append("- Not yet shared canonical state.")
    lines.append("- Not yet a relational field.")
    lines.append("- Not yet an exhaustion of lawful-egress or cross-carrier seam jurisprudence.")
    lines.append("- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.")
    lines.append("")


def render_report(
    snapshot: Mapping[str, Any],
    *,
    resolved_snapshot: ResolvedSnapshot,
    report_path: Path,
) -> str:
    lines: List[str] = []

    source_lineage = as_mapping(snapshot.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(snapshot.get("receiving_side_imported_lineage"))
    clean_source = as_mapping(
        source_run_by_represents(source_lineage, "clean_origin_release")
    )
    obsolete_source = as_mapping(
        source_run_by_represents(source_lineage, "obsolete_origin_lawful_egress")
    )
    clean_receiving = as_mapping(latest_branch_run(receiving_lineage, "clean"))
    obsolete_receiving = as_mapping(
        latest_branch_run(receiving_lineage, "obsolete_origin")
    )

    lines.append("# Cross-Carrier Seam Proof 004 Report")
    lines.append("")
    lines.append(
        "This report is a human-readable companion to the machine-readable "
        "cross-carrier proof 004 snapshot. It is an implementation-local "
        "readability surface only and does not function as protocol law."
    )
    lines.append("")

    add_metadata_section(
        lines,
        snapshot,
        resolved_snapshot=resolved_snapshot,
        report_path=report_path,
    )
    add_current_proof_reading_section(lines, snapshot)

    add_source_section(
        lines,
        clean_source,
        title="Source-Side Clean-Origin Release Lineage",
        summary_text=(
            "The clean-origin release remains a source-side control case. It keeps "
            "source and origin relation explicit while still refusing to convert "
            "release into downstream final standing."
        ),
    )
    add_source_section(
        lines,
        obsolete_source,
        title="Source-Side Obsolete-Origin Release Lineage",
        summary_text=(
            "The obsolete-origin release is the specific lawful-egress threshold. "
            "Source remains source, origin remains lineage-visible, withheld origin "
            "approval is not treated as sovereign veto, and the release does not "
            "pretend to grant downstream closure."
        ),
    )

    add_receiving_section(
        lines,
        branch_name="clean",
        run=clean_receiving,
        summary_text=(
            "On the clean imported branch, the package is technically received and "
            "lawfully carried as bounded in-between arrival. The result remains "
            "receiving-side lineage and does not inherit silent authority."
        ),
    )
    add_receiving_section(
        lines,
        branch_name="obsolete_origin",
        run=obsolete_receiving,
        summary_text=(
            "On the obsolete-origin imported branch, the package remains valid, "
            "arrival remains bounded in-between, and the preserved receiving-side "
            "record keeps non-sovereign origin approval distinct from downstream "
            "closure."
        ),
    )

    add_lawful_egress_section(lines, snapshot)
    add_what_this_shows_section(lines)
    add_what_it_does_not_show_section(lines)

    partial_notes = collect_partial_notes(snapshot, resolved_snapshot)
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
        "cross-carrier proof 004 snapshot. It does not replace the snapshot, it "
        "does not rewrite prior artifacts, it does not convert imported receiving-side "
        "evidence into source-side history, and it does not convert implementation-local "
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
    resolved_snapshot: ResolvedSnapshot,
    snapshot: Mapping[str, Any],
) -> None:
    proof_identity = as_mapping(snapshot.get("proof_identity"))
    print("Cross-carrier proof 004 report written.")
    print(f"Report path: {repo_relative(report_path)}")
    print(f"Source snapshot path: {repo_relative(resolved_snapshot.path)}")
    print(f"Proof id: {proof_identity.get('proof_id')}")
    print(
        "Internalized archive status: "
        f"{proof_identity.get('internalized_archive_status')}"
    )


def main() -> int:
    report_path = choose_report_path()

    try:
        resolved_snapshot = resolve_snapshot()
    except (FileNotFoundError, RuntimeError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    report = render_report(
        resolved_snapshot.payload,
        resolved_snapshot=resolved_snapshot,
        report_path=report_path,
    )

    try:
        write_report(report_path, report)
    except OSError as exc:
        print(f"Failed to write cross-carrier proof 004 report: {exc}", file=sys.stderr)
        return 1

    print_summary(
        report_path=report_path,
        resolved_snapshot=resolved_snapshot,
        snapshot=resolved_snapshot.payload,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
