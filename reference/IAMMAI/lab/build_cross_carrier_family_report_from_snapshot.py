#!/usr/bin/env python3
"""
Build a bounded human-readable companion report directly from the latest
cross-carrier family snapshot.

This script reads the latest machine-readable cross-carrier family snapshot
already present under lab/snapshots/ and renders one additive Markdown report
without regenerating snapshot state.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

FAMILY_ID = "cross_carrier_proof_family"
FAMILY_NAME = "Cross-Carrier Seam Proof Family"
SNAPSHOT_PREFIX = "cross_carrier_family_snapshot__"
SNAPSHOT_SUFFIX = ".json"
REPORT_PREFIX = "cross_carrier_proof_family_report"

TIMESTAMP_PATTERN = re.compile(r"^(?P<stamp>\d{8}T\d{6}Z)(?:__(?P<counter>\d+))?$")

PROOF_TITLES: Dict[str, str] = {
    "cross_carrier_seam_proof_001": "Proof 001: First Cross-Carrier Seam Proof",
    "cross_carrier_seam_proof_002": "Proof 002: Contaminated Receiving Parser Case",
    "cross_carrier_seam_proof_003": "Proof 003: Receiver-Local Embodied Contamination",
}

PROOF_THRESHOLD_NOTES: Dict[str, str] = {
    "cross_carrier_seam_proof_001": (
        "Current visible family account posture preserves the first cross-carrier "
        "proof line through `v1/11_TRANSFER_ACCOUNT_ENTRY__FIRST_CROSS_CARRIER_SEAM_PROOF.md`, "
        "`v1/12_TRANSFER_ACCOUNT_ENTRY__CROSS_CARRIER_PROOF_INTERNALIZED.md`, and "
        "`v1/14_TRANSFER_ACCOUNT_ENTRY__CROSS_CARRIER_PROOF_READABILITY_THRESHOLD.md`."
    ),
    "cross_carrier_seam_proof_002": (
        "Within the current family archive, proof 002 stands as the distinct "
        "contaminated receiving parser/governance turn in which technical receipt "
        "remains visible while lawful ingress can still be denied."
    ),
    "cross_carrier_seam_proof_003": (
        "Current visible family account posture preserves the receiver-local proof "
        "line through `v1/16_TRANSFER_ACCOUNT_ENTRY__RECEIVER_LOCAL_CROSS_CARRIER_PROOF.md` "
        "and `v1/17_TRANSFER_ACCOUNT_ENTRY__RECEIVER_LOCAL_CROSS_CARRIER_PROOF_READABILITY_THRESHOLD.md`."
    ),
}


@dataclass(frozen=True, order=True)
class SnapshotCandidate:
    timestamp: str
    counter: int
    filename: str
    path: Path


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


def ensure_directory(path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Snapshots directory is missing or unreadable: {resolved}")
    return resolved


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
            f"No cross-carrier family snapshot files were found under {snapshot_dir.resolve()}"
        )
    return max(candidates).path


def load_snapshot(path: Path) -> Dict[str, Any]:
    try:
        raw_text = path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OSError(f"Failed to read cross-carrier family snapshot: {exc}") from exc

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Latest cross-carrier family snapshot is invalid JSON: {path}"
        ) from exc

    if not isinstance(parsed, dict):
        raise ValueError(
            "Latest cross-carrier family snapshot did not parse to a JSON object: "
            f"{path}"
        )

    return parsed


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


def format_count_map(value: Any) -> str:
    if not isinstance(value, Mapping) or not value:
        return "`not surfaced in preserved summary fields`"

    parts: List[str] = []
    for key in sorted(value):
        raw_count = value.get(key)
        if isinstance(raw_count, int):
            parts.append(f"`{key}={raw_count}`")

    if not parts:
        return "`not surfaced in preserved summary fields`"
    return ", ".join(parts)


def latest_source_run(proof: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    source_lineage = as_mapping(proof.get("source_side_release_lineage"))
    runs = as_list(source_lineage.get("runs"))
    if not runs:
        return None
    return as_mapping(runs[-1])


def branch_records_in_order(proof: Mapping[str, Any]) -> List[Mapping[str, Any]]:
    receiving_lineage = as_mapping(proof.get("receiving_side_imported_lineage"))
    branch_names = as_list(receiving_lineage.get("imported_branch_names"))
    branches = as_mapping(receiving_lineage.get("branches"))

    records: List[Mapping[str, Any]] = []
    for branch_name in branch_names:
        if not isinstance(branch_name, str):
            continue
        branch = as_mapping(branches.get(branch_name))
        if branch:
            records.append(branch)

    if records:
        return records

    return [as_mapping(branch) for branch in branches.values() if isinstance(branch, Mapping)]


def title_for_proof(proof_id: str) -> str:
    return PROOF_TITLES.get(proof_id, proof_id)


def threshold_note_for_proof(proof_id: str) -> str:
    return PROOF_THRESHOLD_NOTES.get(
        proof_id,
        "This proof stands as a distinct bounded family turn within the current cross-carrier archive.",
    )


def mismatched_case_reading(summary_reading: Mapping[str, Any]) -> str:
    if summary_reading.get("mismatched_case_support_visible") is not True:
        return "Mismatched cases are not surfaced in the preserved summary fields for this proof."

    mismatched_ids = as_list(summary_reading.get("mismatched_case_ids"))
    if not mismatched_ids:
        return "No mismatched cases are surfaced in the preserved summary fields for this proof."

    return "Mismatched case ids surfaced: " + ", ".join(
        md_code(item) for item in mismatched_ids if isinstance(item, str)
    )


def collect_partial_notes(payload: Mapping[str, Any]) -> List[str]:
    notes: List[str] = []

    family_level_notes = as_mapping(payload.get("family_level_notes"))
    notes.extend(str(note) for note in as_list(family_level_notes.get("partial_material_notes")))

    for item in as_list(payload.get("proofs")):
        proof = as_mapping(item)
        proof_id = proof.get("proof_id")
        proof_label = proof_id if isinstance(proof_id, str) else "unknown-proof"

        for note in as_list(proof.get("partial_read_notes")):
            notes.append(f"{proof_label}: {note}")

        surfaces = as_mapping(proof.get("proof_specific_readability_surfaces"))
        for surface_name in ("latest_snapshot", "latest_report"):
            surface = as_mapping(surfaces.get(surface_name))
            read_error = surface.get("read_error")
            if isinstance(read_error, str) and read_error:
                notes.append(
                    f"{proof_label}: unreadable {surface_name.replace('_', ' ')}: {read_error}"
                )

    deduped: List[str] = []
    seen = set()
    for note in notes:
        if note in seen:
            continue
        seen.add(note)
        deduped.append(note)
    return deduped


def add_family_summary_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    family_summary = as_mapping(payload.get("family_summary"))
    family_level_notes = as_mapping(payload.get("family_level_notes"))

    lines.append("## Family Summary")
    lines.append("")
    lines.append(
        "- Total cross-carrier proofs discovered: "
        f"{md_code(family_summary.get('total_cross_carrier_proofs_discovered'))}"
    )
    lines.append(
        "- Total source runs discovered across the family: "
        f"{md_code(family_summary.get('total_source_side_runs_discovered'))}"
    )
    lines.append(
        "- Total receiving imported branches discovered across the family: "
        f"{md_code(family_summary.get('total_receiving_side_imported_branches_discovered'))}"
    )
    lines.append(
        "- Total receiving imported runs discovered across the family: "
        f"{md_code(family_summary.get('total_receiving_side_imported_runs_discovered'))}"
    )

    proof_ids = [
        item for item in as_list(family_summary.get("proof_ids_discovered")) if isinstance(item, str)
    ]
    if proof_ids:
        lines.append("- Proof ids present: " + ", ".join(md_code(item) for item in proof_ids))
    else:
        lines.append("- Proof ids present: `unreadable`")

    bounded_reading = family_level_notes.get("bounded_reading")
    if isinstance(bounded_reading, str):
        lines.append("")
        lines.append(bounded_reading)
    lines.append("")


def add_family_progression_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    family_level_notes = as_mapping(payload.get("family_level_notes"))
    progression = [
        item for item in as_list(family_level_notes.get("visible_progression")) if isinstance(item, str)
    ]

    lines.append("## Family Progression")
    lines.append("")
    if progression:
        for item in progression:
            lines.append(f"- {item}")
    else:
        lines.append("- Family progression was not surfaced in the current snapshot.")
    lines.append("")


def add_proof_section(lines: List[str], proof: Mapping[str, Any]) -> None:
    proof_id = str(proof.get("proof_id") or "unreadable-proof")
    source_lineage = as_mapping(proof.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(proof.get("receiving_side_imported_lineage"))
    summary_reading = as_mapping(proof.get("summary_reading"))
    readability_surfaces = as_mapping(proof.get("proof_specific_readability_surfaces"))

    latest_source = latest_source_run(proof)
    branch_records = branch_records_in_order(proof)

    lines.append(f"## {title_for_proof(proof_id)}")
    lines.append("")
    lines.append(f"- Proof id: {md_code(proof_id)}")
    lines.append(f"- Distinct concern: {proof.get('purpose_note') or '`unreadable`'}")
    lines.append("- Script path: " f"{md_code(proof.get('script_path'))}")
    lines.append(
        "- Internalized archive status: "
        f"{bool_literal(proof.get('internalized_archive_status'))}"
    )
    lines.append("- Source run count: " f"{md_code(source_lineage.get('source_run_count'))}")
    lines.append(
        "- Receiving imported branch names: "
        + (
            ", ".join(
                md_code(item)
                for item in as_list(receiving_lineage.get("imported_branch_names"))
                if isinstance(item, str)
            )
            if as_list(receiving_lineage.get("imported_branch_names"))
            else "`unreadable`"
        )
    )
    lines.append(
        "- Latest source run path: "
        f"{md_code(proof.get('latest_source_package_path') or proof.get('latest_source_summary_path') or source_lineage.get('latest_source_run_path'))}"
    )
    lines.append(
        "- Latest source summary path: "
        f"{md_code(proof.get('latest_source_summary_path'))}"
    )

    if latest_source:
        lines.append(
            "- Latest source execution id: "
            f"{md_code(latest_source.get('execution_id'))}"
        )

    if branch_records:
        for branch in branch_records:
            branch_name = branch.get("branch_name")
            lines.append(
                "- Imported branch "
                f"{md_code(branch_name)}"
                + ": latest summary "
                + md_code(branch.get("latest_summary_path"))
                + ", latest outcome "
                + md_code(branch.get("latest_ingress_outcome"))
            )
    else:
        lines.append("- Imported receiving-side branches: `none surfaced`")

    lines.append(
        "- Receiving outcome counts: "
        f"{format_count_map(summary_reading.get('receiving_outcome_counts'))}"
    )
    lines.append(
        "- Receiving technical receipt counts: "
        f"{format_count_map(summary_reading.get('receiving_technical_receipt_counts'))}"
    )
    lines.append(
        "- Receiving arrival-status counts: "
        f"{format_count_map(summary_reading.get('receiving_arrival_status_counts'))}"
    )
    lines.append(
        "- Receiving blocking-condition counts: "
        f"{format_count_map(summary_reading.get('receiving_blocking_condition_counts'))}"
    )
    lines.append(
        "- Mismatched cases present: "
        f"{bool_literal(summary_reading.get('mismatched_cases_present'))}"
    )
    lines.append(f"- {mismatched_case_reading(summary_reading)}")

    latest_snapshot = as_mapping(readability_surfaces.get("latest_snapshot"))
    latest_report = as_mapping(readability_surfaces.get("latest_report"))
    lines.append("- Proof-specific snapshot surface: " f"{md_code(latest_snapshot.get('path'))}")
    lines.append("- Proof-specific report surface: " f"{md_code(latest_report.get('path'))}")
    lines.append("- Threshold note: " f"{threshold_note_for_proof(proof_id)}")
    lines.append("")


def render_report(
    payload: Mapping[str, Any],
    *,
    report_path: Path,
    snapshot_path: Path,
) -> str:
    lines: List[str] = []

    metadata = as_mapping(payload.get("metadata"))
    proofs = [as_mapping(item) for item in as_list(payload.get("proofs"))]
    proofs.sort(key=lambda item: str(item.get("proof_id") or ""))

    lines.append("# Cross-Carrier Proof Family Report")
    lines.append("")
    lines.append(
        "This report is a human-readable companion to the machine-readable "
        "cross-carrier family snapshot. It is built directly from the latest "
        "cross-carrier family snapshot already present under `lab/snapshots/`."
    )
    lines.append("")
    lines.append(
        "It is an implementation-local readability surface only. It does not "
        "regenerate snapshot state, rerun proofs, mutate prior artifacts, or "
        "function as protocol law."
    )
    lines.append("")

    lines.append("## Metadata")
    lines.append("")
    lines.append(f"- Generated at: {md_code(utc_now())}")
    lines.append(f"- Report path: {md_code(repo_relative(report_path))}")
    lines.append(f"- Source snapshot path: {md_code(repo_relative(snapshot_path))}")
    lines.append(f"- Source snapshot generated at: {md_code(metadata.get('generated_at'))}")
    lines.append(f"- Lab root: {md_code(repo_relative(LAB_ROOT))}")
    lines.append("")

    add_family_summary_section(lines, payload)
    add_family_progression_section(lines, payload)

    lines.append("## Current Proof Reading")
    lines.append("")
    lines.append(
        "The current cross-carrier line reads as a family of distinct bounded "
        "proof-bearing experiments rather than as one flat transfer object. Each "
        "proof keeps its own concern, its own lineage surfaces, and its own ingress "
        "or refusal structure."
    )
    lines.append("")

    for proof in proofs:
        add_proof_section(lines, proof)

    lines.append("## What The Cross-Carrier Family Now Shows")
    lines.append("")
    lines.append(
        "- The family now preserves multiple distinct cross-carrier proof turns rather than one generic carrier crossing story."
    )
    lines.append(
        "- Proof 001 preserves source validity or invalidity together with lawful derivative ingress versus visible refusal or non-passage."
    )
    lines.append(
        "- Proof 002 preserves the contaminated receiving parser or governance case in which technical receipt can remain visible while lawful ingress is denied."
    )
    lines.append(
        "- Proof 003 preserves the receiver-local embodied contamination case in which the same valid package diverges by receiver-local condition."
    )
    lines.append(
        "- Imported receiving-side evidence can remain receiving-side lineage inside the same body without being rewritten into source-side history."
    )
    lines.append(
        "- Family readability has been added without flattening source-side release lineage, receiving-side ingress lineage, and receiving-side refusal or non-passage into one undifferentiated event."
    )
    lines.append("")

    lines.append("## What It Does Not Yet Show")
    lines.append("")
    lines.append("- Not yet a multi-carrier mesh.")
    lines.append("- Not yet bidirectional sync.")
    lines.append("- Not yet shared canonical state.")
    lines.append("- Not yet a relational field.")
    lines.append("- Not yet total cross-carrier doctrine.")
    lines.append("- Not yet a warrant to treat the family report itself as protocol law.")
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
        "cross-carrier family snapshot. It does not replace the snapshot, it does not "
        "rewrite prior proofs, it does not normalize old outputs by mutation, and it "
        "does not flatten the family into one generic transfer story."
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
    family_summary = as_mapping(payload.get("family_summary"))
    print("Cross-carrier family report written from snapshot.")
    print(f"Source snapshot path: {repo_relative(snapshot_path)}")
    print(f"Report path: {repo_relative(report_path)}")
    print(
        "Cross-carrier proofs discovered: "
        f"{family_summary.get('total_cross_carrier_proofs_discovered')}"
    )
    print(
        "Total source runs discovered: "
        f"{family_summary.get('total_source_side_runs_discovered')}"
    )
    print(
        "Total receiving imported branches discovered: "
        f"{family_summary.get('total_receiving_side_imported_branches_discovered')}"
    )


def main() -> int:
    report_path = choose_report_path()

    try:
        ensure_directory(SNAPSHOTS_ROOT)
        snapshot_path = latest_snapshot_path(SNAPSHOTS_ROOT)
        payload = load_snapshot(snapshot_path)
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    report = render_report(
        payload,
        report_path=report_path,
        snapshot_path=snapshot_path,
    )

    try:
        write_report(report_path, report)
    except OSError as exc:
        print(f"Failed to write cross-carrier family report: {exc}", file=sys.stderr)
        return 1

    print_summary(report_path=report_path, snapshot_path=snapshot_path, payload=payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
