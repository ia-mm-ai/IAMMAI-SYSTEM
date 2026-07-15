#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the third cross-carrier seam proof.

This script reads the preserved source-side release lineage and the imported
receiving-side lineage for cross_carrier_seam_proof_003 and emits one additive
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

PROOF_ID = "cross_carrier_seam_proof_003"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SOURCE_RUNS_ROOT = PROOF_ROOT / "source_runs"
RECEIVING_IMPORTS_ROOT = PROOF_ROOT / "receiving_imports"
IMPORT_NOTE_PATH = RECEIVING_IMPORTS_ROOT / "IMPORT_NOTE.md"
ACCOUNT_ENTRY_16_PATH = (
    REPO_ROOT / "v1" / "16_TRANSFER_ACCOUNT_ENTRY__RECEIVER_LOCAL_CROSS_CARRIER_PROOF.md"
)
TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH = PROOF_ROOT / "receiver_local_condition.json"

EXPECTED_RECEIVING_BRANCHES: Tuple[str, ...] = ("clean", "contaminated_non_passage")


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


def safe_read_json(path: Path) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, str(exc)

    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, str(exc)

    if not isinstance(parsed, dict):
        return None, f"Top-level JSON value is not an object: {type(parsed).__name__}"

    return parsed, None


def safe_read_text(path: Path) -> Tuple[Optional[str], Optional[str]]:
    try:
        return path.read_text(encoding="utf-8"), None
    except OSError as exc:
        return None, str(exc)


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


def contains_text(text: Optional[str], needle: str) -> bool:
    return isinstance(text, str) and needle in text


def build_source_run_record(run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    package_path = run_dir / "package" / "transfer_package.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable source summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable source manifest: {manifest_error}")

    package_payload, package_error = safe_read_json(package_path)
    if package_error is not None:
        notes.append(f"Unreadable source transfer package: {package_error}")

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution = summary_payload.get("execution_id")
        if isinstance(summary_execution, str):
            execution_id = summary_execution

    release_context = (
        package_payload.get("release_context")
        if isinstance(package_payload, Mapping)
        and isinstance(package_payload.get("release_context"), Mapping)
        else {}
    )
    seam = (
        package_payload.get("seam")
        if isinstance(package_payload, Mapping)
        and isinstance(package_payload.get("seam"), Mapping)
        else {}
    )

    return {
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "run_represents": "source_release",
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "package_path": repo_relative(package_path) if package_path.is_file() else None,
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
        "artifact_family": (
            summary_payload.get("artifact_family")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "canonical_witness_id": (
            summary_payload.get("canonical_witness_id")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_id": (
            package_payload.get("package_id")
            if isinstance(package_payload, Mapping)
            else None
        ),
        "source_remains_source": (
            summary_payload.get("source_remains_source")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "shared_authority": (
            summary_payload.get("shared_authority")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "standing_transferred": (
            summary_payload.get("standing_transferred")
            if isinstance(summary_payload, Mapping)
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
        "technical_receipt_not_equal_lawful_ingress": (
            summary_payload.get("technical_receipt_not_equal_lawful_ingress")
            if isinstance(summary_payload, Mapping)
            else seam.get("technical_receipt_not_equal_lawful_ingress")
        ),
        "receiver_local_condition_ref": (
            summary_payload.get("receiver_local_condition_ref")
            if isinstance(summary_payload, Mapping)
            else release_context.get("receiver_local_condition_ref")
        ),
        "expected_ingress_under_admissible_receiver_local_condition": (
            summary_payload.get("expected_ingress_under_admissible_receiver_local_condition")
            if isinstance(summary_payload, Mapping)
            else release_context.get(
                "expected_ingress_under_admissible_receiver_local_condition"
            )
        ),
        "expected_ingress_under_contaminated_receiver_local_condition": (
            summary_payload.get("expected_ingress_under_contaminated_receiver_local_condition")
            if isinstance(summary_payload, Mapping)
            else release_context.get(
                "expected_ingress_under_contaminated_receiver_local_condition"
            )
        ),
        "receiver_local_condition_controls_admissibility": seam.get(
            "receiver_local_condition_controls_admissibility"
        ),
        "same_valid_package_may_diverge_by_receiver_local_condition": release_context.get(
            "same_valid_package_may_diverge_by_receiver_local_condition"
        ),
        "do_not_blame_source_for_receiver_local_contamination": release_context.get(
            "do_not_blame_source_for_receiver_local_contamination"
        ),
        "original_package_created_at": (
            package_payload.get("package_created_at")
            if isinstance(package_payload, Mapping)
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
        "latest_source_package_path": latest_run.get("package_path") if latest_run else None,
        "runs": run_records,
        "partial_read_notes": notes,
    }


def build_receiving_run_record(branch_name: str, run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    condition_snapshot_path = run_dir / "package" / "receiver_local_condition_snapshot.json"
    ingress_record_path = run_dir / "ingress" / "ingress_record.json"
    refusal_record_path = run_dir / "refusal" / "refusal_record.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable receiving summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable receiving manifest: {manifest_error}")

    condition_payload, condition_error = safe_read_json(condition_snapshot_path)
    if condition_error is not None:
        notes.append(f"Unreadable receiver-local condition snapshot: {condition_error}")

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

    run_represents = "receiving_side_import"
    if branch_name == "clean" and ingress_outcome == "lawful_derivative_ingress":
        run_represents = "clean_receiving_side_lawful_ingress"
    elif (
        branch_name == "contaminated_non_passage"
        and ingress_outcome == "receiver_local_contamination_non_passage"
    ):
        run_represents = "contaminated_receiving_side_non_passage"

    return {
        "branch_name": branch_name,
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "run_represents": run_represents,
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "condition_snapshot_path": (
            repo_relative(condition_snapshot_path)
            if condition_snapshot_path.is_file()
            else None
        ),
        "ingress_record_path": (
            repo_relative(ingress_record_path) if ingress_record_path.is_file() else None
        ),
        "refusal_record_path": (
            repo_relative(refusal_record_path) if refusal_record_path.is_file() else None
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
        "condition_snapshot_generated_at": (
            condition_payload.get("generated_at")
            if isinstance(condition_payload, Mapping)
            and isinstance(condition_payload.get("generated_at"), str)
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
        "ingress_outcome": ingress_outcome,
        "ingress_lawful": (
            summary_payload.get("ingress_lawful")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "arrival_status": (
            summary_payload.get("arrival_status")
            if isinstance(summary_payload, Mapping)
            else None
        ),
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
        "refusal_visible": (
            summary_payload.get("refusal_visible")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "non_passage": (
            summary_payload.get("non_passage")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "source_fault": (
            summary_payload.get("source_fault")
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
        "receiver_local_condition_ref": (
            summary_payload.get("receiver_local_condition_ref")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "condition_artifact_id": (
            summary_payload.get("condition_artifact_id")
            if isinstance(summary_payload, Mapping)
            else condition_payload.get("condition_artifact_id")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "receiver_local_condition_status": (
            summary_payload.get("receiver_local_condition_status")
            if isinstance(summary_payload, Mapping)
            else condition_payload.get("parser_governance_status")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "receiver_local_governance_admissible": (
            summary_payload.get("receiver_local_governance_admissible")
            if isinstance(summary_payload, Mapping)
            else condition_payload.get("receiver_local_governance_admissible")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "parser_contaminated": (
            summary_payload.get("parser_contaminated")
            if isinstance(summary_payload, Mapping)
            else condition_payload.get("parser_contaminated")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "same_valid_package_may_diverge_by_receiver_local_condition": (
            summary_payload.get("same_valid_package_may_diverge_by_receiver_local_condition")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "original_receiving_run_directory": (
            summary_payload.get("run_directory")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "technical_receipt_supported": (
            condition_payload.get("technical_receipt_supported")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "lineage_can_be_preserved": (
            condition_payload.get("lineage_can_be_preserved")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "rank_can_be_preserved": (
            condition_payload.get("rank_can_be_preserved")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "refusal_visible_if_blocked": (
            condition_payload.get("refusal_visible_if_blocked")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "standing_inflation_risk_present": (
            condition_payload.get("standing_inflation_risk_present")
            if isinstance(condition_payload, Mapping)
            else None
        ),
        "source_blame_shift_pressure_present": (
            condition_payload.get("source_blame_shift_pressure_present")
            if isinstance(condition_payload, Mapping)
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
        "latest_condition_snapshot_path": (
            latest_run.get("condition_snapshot_path") if latest_run else None
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


def latest_source_run(source_lineage: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    runs = source_lineage.get("runs")
    if not isinstance(runs, list):
        return None
    return select_latest_record(runs)


def latest_branch_run(
    receiving_lineage: Mapping[str, Any],
    branch_name: str,
) -> Optional[Mapping[str, Any]]:
    branch = receiving_lineage.get("branches", {}).get(branch_name)
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
    contaminated_present = bool(
        receiving_lineage.get("branches", {})
        .get("contaminated_non_passage", {})
        .get("run_count")
    )
    import_note_present = bool(receiving_lineage.get("import_note_exists"))
    return source_present and clean_present and contaminated_present and import_note_present


def build_ranked_proof_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    clean_branch = receiving_lineage.get("branches", {}).get("clean", {})
    contaminated_branch = (
        receiving_lineage.get("branches", {}).get("contaminated_non_passage", {})
    )

    source_present = bool(source_lineage.get("source_run_count"))
    clean_present = bool(clean_branch.get("run_count"))
    contaminated_present = bool(contaminated_branch.get("run_count"))
    co_present_inside_same_body = source_present and clean_present and contaminated_present

    clean_latest = latest_branch_run(receiving_lineage, "clean")
    contaminated_latest = latest_branch_run(receiving_lineage, "contaminated_non_passage")
    receiver_local_divergence_visible = (
        isinstance(clean_latest, Mapping)
        and isinstance(contaminated_latest, Mapping)
        and clean_latest.get("receiver_local_condition_status") == "admissible"
        and contaminated_latest.get("receiver_local_condition_status") == "contaminated"
        and clean_latest.get("ingress_outcome") == "lawful_derivative_ingress"
        and contaminated_latest.get("ingress_outcome")
        == "receiver_local_contamination_non_passage"
    )

    return {
        "source_side_release_lineage_remains_source_side": source_present,
        "receiving_side_clean_import_remains_receiving_side": clean_present,
        "receiving_side_contaminated_non_passage_import_remains_receiving_side": (
            contaminated_present
        ),
        "import_preserves_relation_without_merger": co_present_inside_same_body,
        "source_and_receiving_lineage_co_present_inside_same_body": co_present_inside_same_body,
        "receiver_local_embodied_contamination_visible": receiver_local_divergence_visible,
        "bounded_reading": (
            "Source-side release lineage remains source-side release lineage. "
            "Receiving-side clean lawful ingress remains clean receiving-side ingress lineage. "
            "Receiving-side contaminated non-passage remains contaminated receiving-side "
            "non-passage lineage. Import preserves relation without merger."
        ),
    }


def build_outcome_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    source_run = latest_source_run(source_lineage)
    clean_run = latest_branch_run(receiving_lineage, "clean")
    contaminated_run = latest_branch_run(receiving_lineage, "contaminated_non_passage")

    source_package_id = source_run.get("package_id") if source_run else None
    clean_package_id = clean_run.get("package_id") if clean_run else None
    contaminated_package_id = contaminated_run.get("package_id") if contaminated_run else None

    same_valid_package_across_branches = (
        isinstance(source_package_id, str)
        and source_package_id == clean_package_id
        and source_package_id == contaminated_package_id
    )

    return {
        "source_side_release_posture": {
            "present": source_run is not None,
            "package_id": source_package_id,
            "package_valid": source_run.get("package_valid") if source_run else None,
            "source_remains_source": (
                source_run.get("source_remains_source") if source_run else None
            ),
            "shared_authority": source_run.get("shared_authority") if source_run else None,
            "standing_transferred": (
                source_run.get("standing_transferred") if source_run else None
            ),
            "receiver_local_condition_controls_admissibility": (
                source_run.get("receiver_local_condition_controls_admissibility")
                if source_run
                else None
            ),
            "same_valid_package_may_diverge_by_receiver_local_condition": (
                source_run.get("same_valid_package_may_diverge_by_receiver_local_condition")
                if source_run
                else None
            ),
            "do_not_blame_source_for_receiver_local_contamination": (
                source_run.get("do_not_blame_source_for_receiver_local_contamination")
                if source_run
                else None
            ),
            "technical_receipt_not_equal_lawful_ingress": (
                source_run.get("technical_receipt_not_equal_lawful_ingress")
                if source_run
                else None
            ),
        },
        "clean_lawful_derivative_ingress": {
            "present": clean_run is not None,
            "execution_id": clean_run.get("execution_id") if clean_run else None,
            "package_id": clean_package_id,
            "receiver_local_condition_status": (
                clean_run.get("receiver_local_condition_status") if clean_run else None
            ),
            "receiver_local_governance_admissible": (
                clean_run.get("receiver_local_governance_admissible")
                if clean_run
                else None
            ),
            "technical_receipt": clean_run.get("technical_receipt") if clean_run else None,
            "ingress_lawful": clean_run.get("ingress_lawful") if clean_run else None,
            "ingress_outcome": clean_run.get("ingress_outcome") if clean_run else None,
            "arrival_status": clean_run.get("arrival_status") if clean_run else None,
            "source_remains_source": (
                clean_run.get("source_remains_source") if clean_run else None
            ),
            "shared_authority": clean_run.get("shared_authority") if clean_run else None,
            "standing_upgraded": clean_run.get("standing_upgraded") if clean_run else None,
            "package_valid": clean_run.get("package_valid") if clean_run else None,
        },
        "contaminated_non_passage": {
            "present": contaminated_run is not None,
            "execution_id": contaminated_run.get("execution_id") if contaminated_run else None,
            "package_id": contaminated_package_id,
            "receiver_local_condition_status": (
                contaminated_run.get("receiver_local_condition_status")
                if contaminated_run
                else None
            ),
            "receiver_local_governance_admissible": (
                contaminated_run.get("receiver_local_governance_admissible")
                if contaminated_run
                else None
            ),
            "technical_receipt": (
                contaminated_run.get("technical_receipt") if contaminated_run else None
            ),
            "ingress_lawful": contaminated_run.get("ingress_lawful") if contaminated_run else None,
            "ingress_outcome": contaminated_run.get("ingress_outcome") if contaminated_run else None,
            "arrival_status": contaminated_run.get("arrival_status") if contaminated_run else None,
            "refusal_visible": contaminated_run.get("refusal_visible") if contaminated_run else None,
            "non_passage": contaminated_run.get("non_passage") if contaminated_run else None,
            "blocking_condition": (
                contaminated_run.get("blocking_condition") if contaminated_run else None
            ),
            "source_remains_source": (
                contaminated_run.get("source_remains_source")
                if contaminated_run
                else None
            ),
            "shared_authority": (
                contaminated_run.get("shared_authority") if contaminated_run else None
            ),
            "standing_upgraded": (
                contaminated_run.get("standing_upgraded") if contaminated_run else None
            ),
            "package_valid": contaminated_run.get("package_valid") if contaminated_run else None,
            "source_fault": contaminated_run.get("source_fault") if contaminated_run else None,
        },
        "cross_branch_relation": {
            "same_valid_package_across_source_and_receiving": same_valid_package_across_branches,
            "clean_and_contaminated_use_distinct_condition_artifact_ids": (
                isinstance(clean_run, Mapping)
                and isinstance(contaminated_run, Mapping)
                and isinstance(clean_run.get("condition_artifact_id"), str)
                and isinstance(contaminated_run.get("condition_artifact_id"), str)
                and clean_run.get("condition_artifact_id")
                != contaminated_run.get("condition_artifact_id")
            ),
            "clean_and_contaminated_condition_statuses_diverge": (
                isinstance(clean_run, Mapping)
                and isinstance(contaminated_run, Mapping)
                and clean_run.get("receiver_local_condition_status") == "admissible"
                and contaminated_run.get("receiver_local_condition_status") == "contaminated"
            ),
        },
    }


def build_receiver_local_embodiment_note(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    import_note_text, import_note_error = safe_read_text(IMPORT_NOTE_PATH)
    account_entry_text, account_entry_error = safe_read_text(ACCOUNT_ENTRY_16_PATH)
    source_run = latest_source_run(source_lineage)
    clean_run = latest_branch_run(receiving_lineage, "clean")
    contaminated_run = latest_branch_run(receiving_lineage, "contaminated_non_passage")

    source_execution_id = source_run.get("execution_id") if source_run else None
    clean_execution_id = clean_run.get("execution_id") if clean_run else None
    contaminated_execution_id = contaminated_run.get("execution_id") if contaminated_run else None
    source_package_id = source_run.get("package_id") if source_run else None
    clean_package_id = clean_run.get("package_id") if clean_run else None
    contaminated_package_id = contaminated_run.get("package_id") if contaminated_run else None

    same_valid_package = (
        isinstance(source_package_id, str)
        and source_package_id == clean_package_id
        and source_package_id == contaminated_package_id
    )
    divergent_receiver_local_outcomes = (
        isinstance(clean_run, Mapping)
        and isinstance(contaminated_run, Mapping)
        and clean_run.get("receiver_local_condition_status") == "admissible"
        and contaminated_run.get("receiver_local_condition_status") == "contaminated"
        and clean_run.get("ingress_outcome") == "lawful_derivative_ingress"
        and contaminated_run.get("ingress_outcome")
        == "receiver_local_contamination_non_passage"
        and contaminated_run.get("blocking_condition")
        == "receiver_local_parser_governance_contamination"
        and contaminated_run.get("package_valid") is True
        and contaminated_run.get("source_fault") is False
    )
    supported = same_valid_package and divergent_receiver_local_outcomes

    return {
        "receiver_local_embodiment_supported": supported,
        "top_level_receiver_local_condition_artifact_path": repo_relative(
            TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH
        ),
        "top_level_receiver_local_condition_artifact_exists": (
            TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH.is_file()
        ),
        "supporting_surfaces": [
            read_supporting_surface(IMPORT_NOTE_PATH),
            read_supporting_surface(ACCOUNT_ENTRY_16_PATH),
        ],
        "evidence_support": {
            "source_execution_id": source_execution_id,
            "clean_execution_id": clean_execution_id,
            "contaminated_execution_id": contaminated_execution_id,
            "source_package_id": source_package_id,
            "clean_package_id": clean_package_id,
            "contaminated_package_id": contaminated_package_id,
            "same_valid_package_across_source_and_receiving": same_valid_package,
            "clean_condition_artifact_id": (
                clean_run.get("condition_artifact_id") if clean_run else None
            ),
            "contaminated_condition_artifact_id": (
                contaminated_run.get("condition_artifact_id") if contaminated_run else None
            ),
            "clean_condition_status": (
                clean_run.get("receiver_local_condition_status") if clean_run else None
            ),
            "contaminated_condition_status": (
                contaminated_run.get("receiver_local_condition_status")
                if contaminated_run
                else None
            ),
            "receiver_local_condition_divergence_visible": divergent_receiver_local_outcomes,
            "import_note_present": IMPORT_NOTE_PATH.is_file(),
            "account_entry_present": ACCOUNT_ENTRY_16_PATH.is_file(),
            "import_note_mentions_clean_branch": contains_text(import_note_text, "`clean/`"),
            "import_note_mentions_contaminated_branch": contains_text(
                import_note_text, "`contaminated_non_passage/`"
            ),
            "import_note_mentions_relation_without_merger": contains_text(
                import_note_text, "Import preserves relation between those sides without merging"
            ),
            "account_entry_mentions_source_execution_id": contains_text(
                account_entry_text, str(source_execution_id)
            ),
            "account_entry_mentions_clean_execution_id": contains_text(
                account_entry_text, str(clean_execution_id)
            ),
            "account_entry_mentions_contaminated_execution_id": contains_text(
                account_entry_text, str(contaminated_execution_id)
            ),
            "account_entry_mentions_receiver_local_embodiment": contains_text(
                account_entry_text, "receiver-local embodied contamination"
            ),
        },
        "partial_read_notes": [
            note
            for note in (
                f"Unreadable import note: {import_note_error}" if import_note_error else None,
                f"Unreadable account entry: {account_entry_error}"
                if account_entry_error
                else None,
                (
                    "Top-level receiver-local condition artifact is not currently preserved at "
                    f"{repo_relative(TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH)}."
                    if not TOP_LEVEL_RECEIVER_LOCAL_CONDITION_PATH.is_file()
                    else None
                ),
            )
            if note is not None
        ],
        "bounded_reading": (
            "The same valid released package now yields lawful derivative-only ingress under "
            "an admissible receiver-local condition and visible non-passage under a "
            "contaminated receiver-local condition. The blocking condition remains "
            "receiver-local parser or governance contamination, not source-side invalidity."
            if supported
            else "Current preserved material does not yet fully support the receiver-local embodiment reading."
        ),
    }


def build_snapshot_payload(snapshot_path: Path) -> Dict[str, Any]:
    if not PROOF_ROOT.is_dir():
        raise FileNotFoundError(
            f"Cross-carrier proof root is missing or unreadable: {PROOF_ROOT}"
        )

    source_lineage = build_source_side_lineage()
    receiving_lineage = build_receiving_imports_lineage()
    receiver_local_note = build_receiver_local_embodiment_note(
        source_lineage, receiving_lineage
    )

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
            "proof_name": "Third Cross-Carrier Seam Proof",
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
        "receiver_local_embodiment_note": receiver_local_note,
    }


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def print_summary(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    source_lineage = payload["source_side_release_lineage"]
    receiving_lineage = payload["receiving_side_imported_lineage"]
    print("Cross-carrier proof snapshot written.")
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
        print(f"Failed to write cross-carrier proof snapshot: {exc}", file=sys.stderr)
        return 1

    print_summary(snapshot_path, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
