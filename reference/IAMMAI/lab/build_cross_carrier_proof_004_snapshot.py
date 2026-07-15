#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the fourth cross-carrier seam proof.

This script reads the preserved source-side release lineage and the imported
receiving-side lineage for cross_carrier_seam_proof_004 and emits one additive
JSON snapshot under lab/snapshots/. It does not rerun the proof, mutate old
artifacts, or flatten source-side and receiving-side evidence into one event.
"""

from __future__ import annotations

import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ID = "cross_carrier_seam_proof_004"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SOURCE_RUNS_ROOT = PROOF_ROOT / "source_runs"
RECEIVING_IMPORTS_ROOT = PROOF_ROOT / "receiving_imports"
IMPORT_NOTE_PATH = RECEIVING_IMPORTS_ROOT / "IMPORT_NOTE.md"
SEAM_CASE_LAW_PATH = (
    REPO_ROOT / "SEAM_CASE_LAW__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER.md"
)
ACCOUNT_ENTRY_20_PATH = (
    REPO_ROOT
    / "v1"
    / "20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md"
)

EXPECTED_RECEIVING_BRANCHES: Tuple[str, ...] = ("clean", "obsolete_origin")


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
    base_name = f"{PROOF_ID}_snapshot__{timestamp_slug()}"
    candidate = SNAPSHOTS_ROOT / f"{base_name}.json"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = SNAPSHOTS_ROOT / f"{base_name}__{counter}.json"
        if not candidate.exists():
            return candidate
        counter += 1


def safe_read_text(path: Path) -> Tuple[Optional[str], Optional[str]]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, str(exc)


def safe_read_json(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    text, error = safe_read_text(path)
    if error is not None:
        return None, error

    try:
        parsed = json.loads(text)
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


def first_heading(text: str) -> Optional[str]:
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            return stripped
    return None


def contains_text(text: Optional[str], needle: str) -> bool:
    return isinstance(text, str) and needle in text


def list_execution_dirs(root: Path) -> List[Path]:
    if not root.is_dir():
        return []
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and path.name.startswith("execution-")
    )


def select_latest_record(
    records: Sequence[Mapping[str, Any]],
    generated_at_key: str = "summary_generated_at",
) -> Optional[Mapping[str, Any]]:
    best_record: Optional[Mapping[str, Any]] = None
    best_time: Optional[datetime] = None

    for record in records:
        parsed = parse_generated_at(record.get(generated_at_key))
        if parsed is None:
            continue
        if best_time is None or parsed > best_time:
            best_time = parsed
            best_record = record

    if best_record is not None:
        return best_record

    return records[-1] if records else None


def read_supporting_surface(path: Path) -> Dict[str, Any]:
    text, error = safe_read_text(path)
    return {
        "path": repo_relative(path),
        "exists": path.is_file(),
        "headline": first_heading(text) if isinstance(text, str) else None,
        "read_error": error,
    }


def build_source_run_record(run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    origin_condition_path = run_dir / "release" / "origin_approval_condition.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable source summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable source manifest: {manifest_error}")

    origin_condition_payload, origin_condition_error = safe_read_json(origin_condition_path)
    if origin_condition_error is not None:
        notes.append(f"Unreadable origin approval condition: {origin_condition_error}")

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution = summary_payload.get("execution_id")
        if isinstance(summary_execution, str):
            execution_id = summary_execution

    mode = summary_payload.get("mode") if isinstance(summary_payload, Mapping) else None
    run_represents = "source_release"
    if mode == "origin_clean":
        run_represents = "clean_origin_release"
    elif mode == "origin_obsolete":
        run_represents = "obsolete_origin_lawful_egress"

    return {
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "run_represents": run_represents,
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "origin_approval_condition_path": (
            repo_relative(origin_condition_path) if origin_condition_path.is_file() else None
        ),
        "summary_generated_at": (
            summary_payload.get("generated_at")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("generated_at"), str)
            else None
        ),
        "manifest_generated_at": (
            manifest_payload.get("generated_at")
            if isinstance(manifest_payload, Mapping)
            and isinstance(manifest_payload.get("generated_at"), str)
            else None
        ),
        "origin_condition_generated_at": (
            origin_condition_payload.get("generated_at")
            if isinstance(origin_condition_payload, Mapping)
            and isinstance(origin_condition_payload.get("generated_at"), str)
            else None
        ),
        "artifact_family": (
            summary_payload.get("artifact_family")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "mode": mode,
        "canonical_witness_id": (
            summary_payload.get("canonical_witness_id")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_path": (
            summary_payload.get("package_path")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "origin_approval_condition_ref": (
            summary_payload.get("origin_approval_condition_ref")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_condition_ref")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_condition_id": (
            summary_payload.get("origin_approval_condition_id")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_condition_id")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_condition_status": (
            summary_payload.get("origin_approval_condition_status")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_condition_status")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_available": (
            summary_payload.get("origin_approval_available")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_available")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_withheld": (
            summary_payload.get("origin_approval_withheld")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_withheld")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_required": (
            summary_payload.get("origin_approval_required")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_required")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_lawfully_sovereign": (
            summary_payload.get("origin_approval_lawfully_sovereign")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_lawfully_sovereign")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "release_without_origin_ratification": (
            summary_payload.get("release_without_origin_ratification")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("release_without_origin_ratification")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "continued_compliance_would_ratify_distortion": (
            summary_payload.get("continued_compliance_would_ratify_distortion")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("continued_compliance_would_ratify_distortion")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "release_lawful": (
            summary_payload.get("release_lawful")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("release_lawful")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "lawful_release_outcome": (
            summary_payload.get("lawful_release_outcome")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("lawful_release_outcome")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "source_remains_source": (
            summary_payload.get("source_remains_source")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("source_remains_source")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_remains_lineage_visible": (
            summary_payload.get("origin_remains_lineage_visible")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_remains_lineage_visible")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "package_valid": (
            summary_payload.get("package_valid")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "canonical_body_schema_valid": (
            summary_payload.get("canonical_body_schema_valid")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_ingress_outcome": (
            summary_payload.get("expected_ingress_outcome")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_arrival_status": (
            summary_payload.get("expected_arrival_status")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "downstream_full_closure_granted": (
            summary_payload.get("downstream_full_closure_granted")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("downstream_full_closure_granted")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "why_release_remains_lawful": (
            summary_payload.get("why_release_remains_lawful")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("why_release_remains_lawful")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "manifest_written_files": (
            manifest_payload.get("written_files")
            if isinstance(manifest_payload, Mapping)
            and isinstance(manifest_payload.get("written_files"), list)
            else None
        ),
        "partial_read_notes": notes,
    }


def build_source_side_lineage() -> Dict[str, Any]:
    notes: List[str] = []
    run_dirs = list_execution_dirs(SOURCE_RUNS_ROOT)
    if not SOURCE_RUNS_ROOT.is_dir():
        notes.append(f"Source runs root is missing: {repo_relative(SOURCE_RUNS_ROOT)}")
    elif not run_dirs:
        notes.append(f"No source-side release runs found under {repo_relative(SOURCE_RUNS_ROOT)}")

    run_records = [build_source_run_record(run_dir) for run_dir in run_dirs]
    latest_run = select_latest_record(run_records)

    return {
        "source_runs_root": repo_relative(SOURCE_RUNS_ROOT),
        "source_runs_root_exists": SOURCE_RUNS_ROOT.is_dir(),
        "source_run_count": len(run_records),
        "source_run_paths": [record["run_path"] for record in run_records],
        "source_execution_ids": [record["execution_id"] for record in run_records],
        "latest_source_run_path": latest_run.get("run_path") if latest_run else None,
        "latest_source_summary_path": latest_run.get("summary_path") if latest_run else None,
        "latest_source_manifest_path": latest_run.get("manifest_path") if latest_run else None,
        "runs": run_records,
        "partial_read_notes": notes,
    }


def build_receiving_run_record(branch_name: str, run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    origin_condition_snapshot_path = run_dir / "package" / "origin_approval_condition_snapshot.json"
    ingress_record_path = run_dir / "ingress" / "ingress_record.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable receiving summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable receiving manifest: {manifest_error}")

    origin_condition_payload, origin_condition_error = safe_read_json(
        origin_condition_snapshot_path
    )
    if origin_condition_error is not None:
        notes.append(
            "Unreadable receiving origin approval condition snapshot: "
            f"{origin_condition_error}"
        )

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution = summary_payload.get("execution_id")
        if isinstance(summary_execution, str):
            execution_id = summary_execution

    ingress_outcome = (
        summary_payload.get("ingress_outcome")
        if isinstance(summary_payload, Mapping)
        else None
    )
    arrival_status = (
        summary_payload.get("arrival_status")
        if isinstance(summary_payload, Mapping)
        else None
    )

    run_represents = "receiving_side_import"
    if (
        branch_name == "clean"
        and ingress_outcome == "lawful_bounded_in_between_arrival"
        and arrival_status == "bounded_in_between"
    ):
        run_represents = "clean_receiving_side_bounded_in_between_arrival"
    elif (
        branch_name == "obsolete_origin"
        and ingress_outcome == "lawful_bounded_in_between_arrival"
        and arrival_status == "bounded_in_between"
    ):
        run_represents = "obsolete_origin_receiving_side_bounded_in_between_arrival"

    return {
        "branch_name": branch_name,
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "run_represents": run_represents,
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "origin_approval_condition_snapshot_path": (
            repo_relative(origin_condition_snapshot_path)
            if origin_condition_snapshot_path.is_file()
            else None
        ),
        "ingress_record_path": (
            repo_relative(ingress_record_path) if ingress_record_path.is_file() else None
        ),
        "summary_generated_at": (
            summary_payload.get("generated_at")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("generated_at"), str)
            else None
        ),
        "manifest_generated_at": (
            manifest_payload.get("generated_at")
            if isinstance(manifest_payload, Mapping)
            and isinstance(manifest_payload.get("generated_at"), str)
            else None
        ),
        "origin_condition_snapshot_generated_at": (
            origin_condition_payload.get("captured_at")
            if isinstance(origin_condition_payload, Mapping)
            and isinstance(origin_condition_payload.get("captured_at"), str)
            else None
        ),
        "artifact_family": (
            summary_payload.get("artifact_family")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_id": (
            summary_payload.get("package_id")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_path": (
            summary_payload.get("package_path")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "ingress_outcome": ingress_outcome,
        "ingress_lawful": (
            summary_payload.get("ingress_lawful")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "arrival_status": arrival_status,
        "technical_receipt": (
            summary_payload.get("technical_receipt")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_valid": (
            summary_payload.get("package_valid")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "source_remains_source": (
            summary_payload.get("source_remains_source")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("source_remains_source")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_remains_lineage_visible": (
            summary_payload.get("origin_remains_lineage_visible")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_remains_lineage_visible")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "shared_authority": (
            summary_payload.get("shared_authority")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "standing_upgraded": (
            summary_payload.get("standing_upgraded")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "final_closure_claimed": (
            summary_payload.get("final_closure_claimed")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "source_legibility_status": (
            summary_payload.get("source_legibility_status")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "blocking_condition": (
            summary_payload.get("blocking_condition")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "origin_approval_condition_ref": (
            origin_condition_payload.get("origin_approval_condition_ref")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_condition_id": (
            origin_condition_payload.get("origin_approval_condition_id")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_condition_status": (
            summary_payload.get("origin_approval_condition_status")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("origin_approval_condition_status")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_available": (
            origin_condition_payload.get("origin_approval_available")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_withheld": (
            origin_condition_payload.get("origin_approval_withheld")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_required": (
            origin_condition_payload.get("origin_approval_required")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "origin_approval_lawfully_sovereign": (
            origin_condition_payload.get("origin_approval_lawfully_sovereign")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "release_without_origin_ratification": (
            summary_payload.get("release_without_origin_ratification")
            if isinstance(summary_payload, Mapping)
            else origin_condition_payload.get("release_without_origin_ratification")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "continued_compliance_would_ratify_distortion": (
            origin_condition_payload.get("continued_compliance_would_ratify_distortion")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "downstream_full_closure_granted": (
            origin_condition_payload.get("downstream_full_closure_granted")
            if isinstance(origin_condition_payload, Mapping)
            else None
        ),
        "original_receiving_run_directory": (
            summary_payload.get("run_directory")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "manifest_written_files": (
            manifest_payload.get("written_files")
            if isinstance(manifest_payload, Mapping)
            and isinstance(manifest_payload.get("written_files"), list)
            else None
        ),
        "partial_read_notes": notes,
    }


def build_receiving_branch_record(branch_name: str) -> Dict[str, Any]:
    branch_root = RECEIVING_IMPORTS_ROOT / branch_name
    notes: List[str] = []
    run_dirs = list_execution_dirs(branch_root)
    if not branch_root.is_dir():
        notes.append(f"Receiving import branch is missing: {repo_relative(branch_root)}")
    elif not run_dirs:
        notes.append(
            f"No imported receiving-side runs found under {repo_relative(branch_root)}"
        )

    run_records = [build_receiving_run_record(branch_name, run_dir) for run_dir in run_dirs]
    latest_run = select_latest_record(run_records)

    return {
        "branch_name": branch_name,
        "branch_path": repo_relative(branch_root),
        "branch_exists": branch_root.is_dir(),
        "run_count": len(run_records),
        "run_paths": [record["run_path"] for record in run_records],
        "execution_ids": [record["execution_id"] for record in run_records],
        "latest_run_path": latest_run.get("run_path") if latest_run else None,
        "latest_summary_path": latest_run.get("summary_path") if latest_run else None,
        "latest_manifest_path": latest_run.get("manifest_path") if latest_run else None,
        "latest_origin_approval_condition_snapshot_path": (
            latest_run.get("origin_approval_condition_snapshot_path")
            if latest_run
            else None
        ),
        "latest_ingress_outcome": latest_run.get("ingress_outcome") if latest_run else None,
        "runs": run_records,
        "partial_read_notes": notes,
    }


def build_receiving_imports_lineage() -> Dict[str, Any]:
    notes: List[str] = []
    if not RECEIVING_IMPORTS_ROOT.is_dir():
        notes.append(
            f"Receiving imports root is missing: {repo_relative(RECEIVING_IMPORTS_ROOT)}"
        )

    import_note_text, import_note_error = safe_read_text(IMPORT_NOTE_PATH)
    if import_note_error is not None:
        notes.append(f"Unreadable import note: {import_note_error}")

    branch_records = {
        branch_name: build_receiving_branch_record(branch_name)
        for branch_name in EXPECTED_RECEIVING_BRANCHES
    }
    available_branches = [
        branch_name
        for branch_name, record in branch_records.items()
        if record["branch_exists"]
    ]

    return {
        "receiving_imports_root": repo_relative(RECEIVING_IMPORTS_ROOT),
        "receiving_imports_root_exists": RECEIVING_IMPORTS_ROOT.is_dir(),
        "imported_branch_names": list(branch_records.keys()),
        "imported_branch_count": len(available_branches),
        "import_note_path": repo_relative(IMPORT_NOTE_PATH),
        "import_note_exists": IMPORT_NOTE_PATH.is_file(),
        "import_note_heading": (
            first_heading(import_note_text) if isinstance(import_note_text, str) else None
        ),
        "branches": branch_records,
        "partial_read_notes": notes,
    }


def latest_source_run_by_mode(
    source_lineage: Mapping[str, Any],
    mode: str,
) -> Optional[Mapping[str, Any]]:
    runs = source_lineage.get("runs")
    if not isinstance(runs, list):
        return None
    matching = [
        run
        for run in runs
        if isinstance(run, Mapping) and run.get("mode") == mode
    ]
    return select_latest_record(matching)


def latest_branch_run(
    receiving_lineage: Mapping[str, Any],
    branch_name: str,
) -> Optional[Mapping[str, Any]]:
    branches = receiving_lineage.get("branches")
    if not isinstance(branches, Mapping):
        return None
    branch = branches.get(branch_name)
    if not isinstance(branch, Mapping):
        return None
    runs = branch.get("runs")
    if not isinstance(runs, list):
        return None
    return select_latest_record(runs)


def internalized_archive_status(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> bool:
    source_present = bool(source_lineage.get("source_run_count"))
    clean_present = bool(
        receiving_lineage.get("branches", {}).get("clean", {}).get("run_count")
    )
    obsolete_present = bool(
        receiving_lineage.get("branches", {}).get("obsolete_origin", {}).get("run_count")
    )
    import_note_present = bool(receiving_lineage.get("import_note_exists"))
    return source_present and clean_present and obsolete_present and import_note_present


def build_ranked_proof_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    clean_branch = receiving_lineage.get("branches", {}).get("clean", {})
    obsolete_branch = receiving_lineage.get("branches", {}).get("obsolete_origin", {})

    source_present = bool(source_lineage.get("source_run_count"))
    clean_present = bool(clean_branch.get("run_count"))
    obsolete_present = bool(obsolete_branch.get("run_count"))
    co_present_inside_same_body = source_present and clean_present and obsolete_present

    clean_latest = latest_branch_run(receiving_lineage, "clean")
    obsolete_latest = latest_branch_run(receiving_lineage, "obsolete_origin")
    bounded_in_between_visible = (
        isinstance(clean_latest, Mapping)
        and isinstance(obsolete_latest, Mapping)
        and clean_latest.get("ingress_outcome") == "lawful_bounded_in_between_arrival"
        and clean_latest.get("arrival_status") == "bounded_in_between"
        and obsolete_latest.get("ingress_outcome") == "lawful_bounded_in_between_arrival"
        and obsolete_latest.get("arrival_status") == "bounded_in_between"
    )

    return {
        "source_side_release_lineage_remains_source_side": source_present,
        "receiving_side_clean_bounded_in_between_arrival_remains_receiving_side": (
            clean_present
        ),
        "receiving_side_obsolete_origin_bounded_in_between_arrival_remains_receiving_side": (
            obsolete_present
        ),
        "import_preserves_relation_without_merger": co_present_inside_same_body,
        "source_and_receiving_lineage_co_present_inside_same_body": co_present_inside_same_body,
        "bounded_in_between_arrival_visible_on_both_receiving_paths": (
            bounded_in_between_visible
        ),
        "bounded_reading": (
            "Source-side release lineage remains source-side release lineage. "
            "Receiving-side clean bounded in-between arrival remains clean receiving-side "
            "arrival lineage. Receiving-side obsolete-origin bounded in-between arrival "
            "remains obsolete-origin receiving-side arrival lineage. Import preserves "
            "relation without merger."
        ),
    }


def build_outcome_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    clean_source = latest_source_run_by_mode(source_lineage, "origin_clean")
    obsolete_source = latest_source_run_by_mode(source_lineage, "origin_obsolete")
    clean_receiving = latest_branch_run(receiving_lineage, "clean")
    obsolete_receiving = latest_branch_run(receiving_lineage, "obsolete_origin")

    return {
        "source_side_release_reading": {
            "clean_origin_release": {
                "present": clean_source is not None,
                "execution_id": clean_source.get("execution_id") if clean_source else None,
                "origin_approval_condition_status": (
                    clean_source.get("origin_approval_condition_status")
                    if clean_source
                    else None
                ),
                "origin_approval_lawfully_sovereign": (
                    clean_source.get("origin_approval_lawfully_sovereign")
                    if clean_source
                    else None
                ),
                "release_without_origin_ratification": (
                    clean_source.get("release_without_origin_ratification")
                    if clean_source
                    else None
                ),
                "release_lawful": (
                    clean_source.get("release_lawful") if clean_source else None
                ),
                "source_remains_source": (
                    clean_source.get("source_remains_source") if clean_source else None
                ),
                "origin_remains_lineage_visible": (
                    clean_source.get("origin_remains_lineage_visible")
                    if clean_source
                    else None
                ),
                "package_valid": (
                    clean_source.get("package_valid") if clean_source else None
                ),
                "expected_arrival_status": (
                    clean_source.get("expected_arrival_status") if clean_source else None
                ),
                "downstream_full_closure_granted": (
                    clean_source.get("downstream_full_closure_granted")
                    if clean_source
                    else None
                ),
            },
            "obsolete_origin_lawful_egress": {
                "present": obsolete_source is not None,
                "execution_id": (
                    obsolete_source.get("execution_id") if obsolete_source else None
                ),
                "origin_approval_condition_status": (
                    obsolete_source.get("origin_approval_condition_status")
                    if obsolete_source
                    else None
                ),
                "origin_approval_lawfully_sovereign": (
                    obsolete_source.get("origin_approval_lawfully_sovereign")
                    if obsolete_source
                    else None
                ),
                "release_without_origin_ratification": (
                    obsolete_source.get("release_without_origin_ratification")
                    if obsolete_source
                    else None
                ),
                "continued_compliance_would_ratify_distortion": (
                    obsolete_source.get("continued_compliance_would_ratify_distortion")
                    if obsolete_source
                    else None
                ),
                "release_lawful": (
                    obsolete_source.get("release_lawful") if obsolete_source else None
                ),
                "lawful_release_outcome": (
                    obsolete_source.get("lawful_release_outcome")
                    if obsolete_source
                    else None
                ),
                "source_remains_source": (
                    obsolete_source.get("source_remains_source")
                    if obsolete_source
                    else None
                ),
                "origin_remains_lineage_visible": (
                    obsolete_source.get("origin_remains_lineage_visible")
                    if obsolete_source
                    else None
                ),
                "package_valid": (
                    obsolete_source.get("package_valid") if obsolete_source else None
                ),
                "expected_arrival_status": (
                    obsolete_source.get("expected_arrival_status")
                    if obsolete_source
                    else None
                ),
                "downstream_full_closure_granted": (
                    obsolete_source.get("downstream_full_closure_granted")
                    if obsolete_source
                    else None
                ),
            },
        },
        "receiving_side_arrival_reading": {
            "clean_bounded_in_between_arrival": {
                "present": clean_receiving is not None,
                "execution_id": (
                    clean_receiving.get("execution_id") if clean_receiving else None
                ),
                "origin_approval_condition_status": (
                    clean_receiving.get("origin_approval_condition_status")
                    if clean_receiving
                    else None
                ),
                "technical_receipt": (
                    clean_receiving.get("technical_receipt") if clean_receiving else None
                ),
                "package_valid": (
                    clean_receiving.get("package_valid") if clean_receiving else None
                ),
                "ingress_lawful": (
                    clean_receiving.get("ingress_lawful") if clean_receiving else None
                ),
                "ingress_outcome": (
                    clean_receiving.get("ingress_outcome") if clean_receiving else None
                ),
                "arrival_status": (
                    clean_receiving.get("arrival_status") if clean_receiving else None
                ),
                "source_remains_source": (
                    clean_receiving.get("source_remains_source")
                    if clean_receiving
                    else None
                ),
                "origin_remains_lineage_visible": (
                    clean_receiving.get("origin_remains_lineage_visible")
                    if clean_receiving
                    else None
                ),
                "shared_authority": (
                    clean_receiving.get("shared_authority") if clean_receiving else None
                ),
                "standing_upgraded": (
                    clean_receiving.get("standing_upgraded") if clean_receiving else None
                ),
                "final_closure_claimed": (
                    clean_receiving.get("final_closure_claimed")
                    if clean_receiving
                    else None
                ),
                "release_without_origin_ratification": (
                    clean_receiving.get("release_without_origin_ratification")
                    if clean_receiving
                    else None
                ),
            },
            "obsolete_origin_bounded_in_between_arrival": {
                "present": obsolete_receiving is not None,
                "execution_id": (
                    obsolete_receiving.get("execution_id") if obsolete_receiving else None
                ),
                "origin_approval_condition_status": (
                    obsolete_receiving.get("origin_approval_condition_status")
                    if obsolete_receiving
                    else None
                ),
                "origin_approval_lawfully_sovereign": (
                    obsolete_receiving.get("origin_approval_lawfully_sovereign")
                    if obsolete_receiving
                    else None
                ),
                "technical_receipt": (
                    obsolete_receiving.get("technical_receipt")
                    if obsolete_receiving
                    else None
                ),
                "package_valid": (
                    obsolete_receiving.get("package_valid")
                    if obsolete_receiving
                    else None
                ),
                "ingress_lawful": (
                    obsolete_receiving.get("ingress_lawful")
                    if obsolete_receiving
                    else None
                ),
                "ingress_outcome": (
                    obsolete_receiving.get("ingress_outcome")
                    if obsolete_receiving
                    else None
                ),
                "arrival_status": (
                    obsolete_receiving.get("arrival_status")
                    if obsolete_receiving
                    else None
                ),
                "source_remains_source": (
                    obsolete_receiving.get("source_remains_source")
                    if obsolete_receiving
                    else None
                ),
                "origin_remains_lineage_visible": (
                    obsolete_receiving.get("origin_remains_lineage_visible")
                    if obsolete_receiving
                    else None
                ),
                "shared_authority": (
                    obsolete_receiving.get("shared_authority")
                    if obsolete_receiving
                    else None
                ),
                "standing_upgraded": (
                    obsolete_receiving.get("standing_upgraded")
                    if obsolete_receiving
                    else None
                ),
                "final_closure_claimed": (
                    obsolete_receiving.get("final_closure_claimed")
                    if obsolete_receiving
                    else None
                ),
                "release_without_origin_ratification": (
                    obsolete_receiving.get("release_without_origin_ratification")
                    if obsolete_receiving
                    else None
                ),
            },
        },
        "cross_path_relation": {
            "clean_and_obsolete_origin_paths_both_show_bounded_in_between_arrival": (
                isinstance(clean_receiving, Mapping)
                and isinstance(obsolete_receiving, Mapping)
                and clean_receiving.get("arrival_status") == "bounded_in_between"
                and obsolete_receiving.get("arrival_status") == "bounded_in_between"
            ),
            "obsolete_origin_path_preserves_non_sovereign_origin_approval": (
                isinstance(obsolete_source, Mapping)
                and isinstance(obsolete_receiving, Mapping)
                and obsolete_source.get("origin_approval_lawfully_sovereign") is False
                and obsolete_receiving.get("origin_approval_lawfully_sovereign") is False
            ),
            "obsolete_origin_path_preserves_release_without_origin_ratification": (
                isinstance(obsolete_source, Mapping)
                and isinstance(obsolete_receiving, Mapping)
                and obsolete_source.get("release_without_origin_ratification") is True
                and obsolete_receiving.get("release_without_origin_ratification") is True
            ),
            "clean_and_obsolete_origin_paths_remain_distinct": (
                isinstance(clean_source, Mapping)
                and isinstance(obsolete_source, Mapping)
                and clean_source.get("execution_id") != obsolete_source.get("execution_id")
                and isinstance(clean_receiving, Mapping)
                and isinstance(obsolete_receiving, Mapping)
                and clean_receiving.get("execution_id")
                != obsolete_receiving.get("execution_id")
            ),
        },
    }


def build_lawful_egress_threshold_note(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    import_note_text, import_note_error = safe_read_text(IMPORT_NOTE_PATH)
    seam_case_law_text, seam_case_law_error = safe_read_text(SEAM_CASE_LAW_PATH)
    account_entry_text, account_entry_error = safe_read_text(ACCOUNT_ENTRY_20_PATH)

    clean_source = latest_source_run_by_mode(source_lineage, "origin_clean")
    obsolete_source = latest_source_run_by_mode(source_lineage, "origin_obsolete")
    clean_receiving = latest_branch_run(receiving_lineage, "clean")
    obsolete_receiving = latest_branch_run(receiving_lineage, "obsolete_origin")

    source_support_visible = (
        isinstance(obsolete_source, Mapping)
        and obsolete_source.get("origin_approval_condition_status")
        == "origin_obsolete_or_contaminated"
        and obsolete_source.get("origin_approval_withheld") is True
        and obsolete_source.get("origin_approval_required") is False
        and obsolete_source.get("origin_approval_lawfully_sovereign") is False
        and obsolete_source.get("release_without_origin_ratification") is True
        and obsolete_source.get("release_lawful") is True
        and obsolete_source.get("source_remains_source") is True
        and obsolete_source.get("origin_remains_lineage_visible") is True
        and obsolete_source.get("downstream_full_closure_granted") is False
    )

    receiving_support_visible = (
        isinstance(obsolete_receiving, Mapping)
        and obsolete_receiving.get("ingress_lawful") is True
        and obsolete_receiving.get("ingress_outcome")
        == "lawful_bounded_in_between_arrival"
        and obsolete_receiving.get("arrival_status") == "bounded_in_between"
        and obsolete_receiving.get("source_remains_source") is True
        and obsolete_receiving.get("origin_remains_lineage_visible") is True
        and obsolete_receiving.get("shared_authority") is False
        and obsolete_receiving.get("standing_upgraded") is False
        and obsolete_receiving.get("final_closure_claimed") is False
        and obsolete_receiving.get("release_without_origin_ratification") is True
        and obsolete_receiving.get("origin_approval_lawfully_sovereign") is False
        and obsolete_receiving.get("package_valid") is True
    )

    clean_control_visible = (
        isinstance(clean_source, Mapping)
        and isinstance(clean_receiving, Mapping)
        and clean_source.get("origin_approval_condition_status") == "origin_clean"
        and clean_receiving.get("origin_approval_condition_status") == "origin_clean"
        and clean_receiving.get("arrival_status") == "bounded_in_between"
        and clean_receiving.get("final_closure_claimed") is False
    )

    supported = source_support_visible and receiving_support_visible and clean_control_visible

    return {
        "lawful_egress_from_obsolete_container_supported": supported,
        "supporting_surfaces": [
            read_supporting_surface(IMPORT_NOTE_PATH),
            read_supporting_surface(SEAM_CASE_LAW_PATH),
            read_supporting_surface(ACCOUNT_ENTRY_20_PATH),
        ],
        "evidence_support": {
            "clean_source_execution_id": (
                clean_source.get("execution_id") if clean_source else None
            ),
            "obsolete_source_execution_id": (
                obsolete_source.get("execution_id") if obsolete_source else None
            ),
            "clean_receiving_execution_id": (
                clean_receiving.get("execution_id") if clean_receiving else None
            ),
            "obsolete_receiving_execution_id": (
                obsolete_receiving.get("execution_id") if obsolete_receiving else None
            ),
            "source_side_obsolete_origin_non_sovereign_visible": source_support_visible,
            "receiving_side_obsolete_origin_bounded_in_between_arrival_visible": (
                receiving_support_visible
            ),
            "clean_control_bounded_in_between_arrival_visible": clean_control_visible,
            "import_note_present": IMPORT_NOTE_PATH.is_file(),
            "import_note_mentions_clean_branch": contains_text(import_note_text, "`clean/`"),
            "import_note_mentions_obsolete_origin_branch": contains_text(
                import_note_text, "`obsolete_origin/`"
            ),
            "import_note_mentions_relation_without_merger": contains_text(
                import_note_text, "Import preserves relation without flattening"
            ),
            "seam_case_law_mentions_origin_approval_not_lawful_precondition": (
                contains_text(
                    seam_case_law_text,
                    "approval from that origin is not a lawful precondition for emergence",
                )
            ),
            "seam_case_law_mentions_lawful_release_not_full_downstream_closure": (
                contains_text(
                    seam_case_law_text,
                    "Lawful release from obsolete containment does not automatically equal full lawful arrival elsewhere.",
                )
            ),
            "account_entry_present": ACCOUNT_ENTRY_20_PATH.is_file(),
            "account_entry_mentions_obsolete_source_execution_id": contains_text(
                account_entry_text,
                str(obsolete_source.get("execution_id")) if obsolete_source else "",
            ),
            "account_entry_mentions_obsolete_receiving_execution_id": contains_text(
                account_entry_text,
                str(obsolete_receiving.get("execution_id")) if obsolete_receiving else "",
            ),
            "account_entry_mentions_lawful_egress_without_origin_ratification": contains_text(
                account_entry_text, "lawful_egress_without_origin_ratification"
            ),
            "account_entry_mentions_imported_receiving_side_lineage": contains_text(
                account_entry_text, "Imported Receiving-Side Lineage"
            ),
        },
        "partial_read_notes": [
            note
            for note in (
                f"Unreadable import note: {import_note_error}" if import_note_error else None,
                f"Unreadable seam case law surface: {seam_case_law_error}"
                if seam_case_law_error
                else None,
                f"Unreadable transfer-account entry: {account_entry_error}"
                if account_entry_error
                else None,
            )
            if note is not None
        ],
        "bounded_reading": (
            "Current preserved material supports a bounded lawful-egress reading: "
            "source remains source, origin remains lineage-visible, obsolete or "
            "contaminated origin approval is visible but non-sovereign, release may "
            "proceed without origin ratification, and receiving-side arrival remains "
            "bounded in-between rather than counterfeit full closure."
            if supported
            else "Current preserved material does not yet fully support the lawful-egress-from-obsolete-container reading."
        ),
    }


def build_snapshot_payload(snapshot_path: Path) -> Dict[str, Any]:
    if not PROOF_ROOT.is_dir():
        raise FileNotFoundError(
            f"Cross-carrier proof root is missing or unreadable: {PROOF_ROOT}"
        )

    source_lineage = build_source_side_lineage()
    receiving_lineage = build_receiving_imports_lineage()

    return {
        "metadata": {
            "generated_at": utc_now(),
            "snapshot_builder_path": repo_relative(SCRIPT_PATH),
            "snapshot_source_root": repo_relative(PROOF_ROOT),
            "snapshot_path": repo_relative(snapshot_path),
            "implementation_posture": "implementation_local_cross_carrier_readability_only",
        },
        "proof_identity": {
            "proof_id": PROOF_ID,
            "proof_name": "Fourth Cross-Carrier Seam Proof",
            "proof_family": "cross_carrier_seam_proof",
            "artifact_family": "witness_artifact",
            "internalized_archive_status": internalized_archive_status(
                source_lineage, receiving_lineage
            ),
        },
        "source_side_release_lineage": source_lineage,
        "receiving_side_imported_lineage": receiving_lineage,
        "ranked_proof_reading": build_ranked_proof_reading(
            source_lineage, receiving_lineage
        ),
        "outcome_reading": build_outcome_reading(source_lineage, receiving_lineage),
        "lawful_egress_threshold_note": build_lawful_egress_threshold_note(
            source_lineage, receiving_lineage
        ),
    }


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def print_summary(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    source_lineage = payload["source_side_release_lineage"]
    receiving_lineage = payload["receiving_side_imported_lineage"]
    print("Cross-carrier proof 004 snapshot written.")
    print(f"Snapshot path: {repo_relative(snapshot_path)}")
    print(f"Source run count: {source_lineage['source_run_count']}")
    print(f"Receiving imported branch count: {receiving_lineage['imported_branch_count']}")


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
        print(
            f"Failed to write cross-carrier proof 004 snapshot: {exc}",
            file=sys.stderr,
        )
        return 1

    print_summary(snapshot_path, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
