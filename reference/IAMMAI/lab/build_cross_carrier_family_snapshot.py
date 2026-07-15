#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the cross-carrier proof family.

This script discovers preserved cross_carrier_seam_proof_* roots under lab/,
reads their source-side and receiving-side lineage where present, and emits one
additive JSON snapshot under lab/snapshots/. It does not rerun proofs, mutate
old artifacts, or flatten distinct cross-carrier proof turns into one generic
transfer story.
"""

from __future__ import annotations

import ast
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ROOT_PATTERN = "cross_carrier_seam_proof_*"
FAMILY_SNAPSHOT_PREFIX = "cross_carrier_family_snapshot"

KNOWN_PROOF_PURPOSES: Dict[str, str] = {
    "cross_carrier_seam_proof_001": (
        "Bounded first cross-carrier seam proof for source validity or invalidity "
        "and lawful ingress versus visible refusal or non-passage."
    ),
    "cross_carrier_seam_proof_002": (
        "Bounded contaminated receiving parser or governance case in which a valid "
        "package may be technically received while lawful ingress is denied."
    ),
    "cross_carrier_seam_proof_003": (
        "Bounded receiver-local embodied contamination case in which the same valid "
        "package diverges by receiving-side local condition."
    ),
}

KNOWN_READABILITY_BUILDERS: Dict[str, Dict[str, Path]] = {
    "cross_carrier_seam_proof_001": {
        "snapshot_builder_path": LAB_ROOT / "build_cross_carrier_proof_snapshot.py",
        "report_builder_path": LAB_ROOT / "build_cross_carrier_proof_report.py",
    },
    "cross_carrier_seam_proof_003": {
        "snapshot_builder_path": LAB_ROOT / "build_cross_carrier_proof_003_snapshot.py",
        "report_builder_path": LAB_ROOT / "build_cross_carrier_proof_003_report.py",
    },
}


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
    base_name = f"{FAMILY_SNAPSHOT_PREFIX}__{timestamp_slug()}"
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


def normalize_scalar(value: Any) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (int, float, str)):
        return str(value)
    return None


def count_field_values(records: Sequence[Mapping[str, Any]], field_name: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}
    for record in records:
        normalized = normalize_scalar(record.get(field_name))
        if normalized is None:
            continue
        counts[normalized] = counts.get(normalized, 0) + 1
    return counts


def merge_count_maps(records: Sequence[Mapping[str, Any]], field_name: str) -> Dict[str, int]:
    totals: Dict[str, int] = {}
    for record in records:
        value = record.get(field_name)
        if not isinstance(value, Mapping):
            continue
        for key, raw_count in value.items():
            if not isinstance(key, str):
                continue
            if not isinstance(raw_count, int):
                continue
            totals[key] = totals.get(key, 0) + raw_count
    return totals


def sum_numeric_field(records: Sequence[Mapping[str, Any]], field_name: str) -> Optional[int]:
    total = 0
    seen = False
    for record in records:
        value = record.get(field_name)
        if isinstance(value, int):
            total += value
            seen = True
    return total if seen else None


def extract_mismatched_case_ids(
    records: Sequence[Mapping[str, Any]],
) -> Tuple[bool, List[str]]:
    support_visible = False
    ids: List[str] = []

    for record in records:
        if "mismatched_case_ids" not in record:
            continue
        support_visible = True
        value = record.get("mismatched_case_ids")
        if not isinstance(value, list):
            continue
        for item in value:
            if isinstance(item, str):
                ids.append(item)

    return support_visible, sorted(set(ids))


def flatten_branch_runs(
    branch_records: Mapping[str, Mapping[str, Any]],
) -> List[Mapping[str, Any]]:
    records: List[Mapping[str, Any]] = []
    for branch in branch_records.values():
        runs = branch.get("runs")
        if not isinstance(runs, list):
            continue
        for run in runs:
            if isinstance(run, Mapping):
                records.append(run)
    return records


def script_docstring_headline(path: Path) -> Optional[str]:
    text, error = safe_read_text(path)
    if error is not None or text is None:
        return None

    try:
        module = ast.parse(text)
    except SyntaxError:
        return None

    docstring = ast.get_docstring(module)
    if not docstring:
        return None

    for line in docstring.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def find_existing_path(candidates: Sequence[Path]) -> Optional[Path]:
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    return None


def read_markdown_surface(path: Path) -> Dict[str, Any]:
    text, error = safe_read_text(path)
    return {
        "path": repo_relative(path),
        "exists": path.is_file(),
        "heading": first_heading(text) if isinstance(text, str) else None,
        "read_error": error,
    }


def latest_snapshot_artifact(
    proof_id: str,
    kind: str,
) -> Dict[str, Any]:
    if kind == "snapshot":
        pattern = f"{proof_id}_snapshot__*.json"
    else:
        pattern = f"{proof_id}_report__*.md"

    matches = sorted(path for path in SNAPSHOTS_ROOT.glob(pattern) if path.is_file())
    latest = matches[-1] if matches else None

    record: Dict[str, Any] = {
        "kind": kind,
        "path": repo_relative(latest) if latest is not None else None,
        "exists": latest is not None,
    }

    if latest is None:
        return record

    if kind == "snapshot":
        payload, error = safe_read_json(latest)
        record["read_error"] = error
        if payload is not None:
            metadata = payload.get("metadata")
            proof_identity = payload.get("proof_identity")
            if isinstance(metadata, Mapping):
                record["generated_at"] = metadata.get("generated_at")
            if isinstance(proof_identity, Mapping):
                record["internalized_archive_status"] = proof_identity.get(
                    "internalized_archive_status"
                )
    else:
        text, error = safe_read_text(latest)
        record["read_error"] = error
        if isinstance(text, str):
            record["heading"] = first_heading(text)

    return record


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
        notes.append(f"Unreadable source package: {package_error}")

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution_id = summary_payload.get("execution_id")
        if isinstance(summary_execution_id, str):
            execution_id = summary_execution_id

    return {
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "package_path": repo_relative(package_path) if package_path.is_file() else None,
        "summary_generated_at": (
            summary_payload.get("generated_at")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "manifest_generated_at": (
            manifest_payload.get("generated_at")
            if isinstance(manifest_payload, Mapping)
            else None
        ),
        "mode": summary_payload.get("mode") if isinstance(summary_payload, Mapping) else None,
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
            summary_payload.get("package_id")
            if isinstance(summary_payload, Mapping)
            else package_payload.get("package_id")
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
        "package_ingress_lawful_if_received": (
            summary_payload.get("package_ingress_lawful_if_received")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "package_attempted_unlawful_standing_transfer": (
            summary_payload.get("package_attempted_unlawful_standing_transfer")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "technical_receipt_not_equal_lawful_ingress": (
            summary_payload.get("technical_receipt_not_equal_lawful_ingress")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_ingress_outcome": (
            summary_payload.get("expected_ingress_outcome")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_clean_ingress_outcome": (
            summary_payload.get("expected_clean_ingress_outcome")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_contaminated_ingress_outcome": (
            summary_payload.get("expected_contaminated_ingress_outcome")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_ingress_under_admissible_receiver_local_condition": (
            summary_payload.get(
                "expected_ingress_under_admissible_receiver_local_condition"
            )
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "expected_ingress_under_contaminated_receiver_local_condition": (
            summary_payload.get(
                "expected_ingress_under_contaminated_receiver_local_condition"
            )
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "receiver_local_condition_ref": (
            summary_payload.get("receiver_local_condition_ref")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "total_cases": (
            summary_payload.get("total_cases")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("total_cases"), int)
            else None
        ),
        "counts_by_outcome_type": (
            summary_payload.get("counts_by_outcome_type")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("counts_by_outcome_type"), Mapping)
            else None
        ),
        "counts_by_receipt_status": (
            summary_payload.get("counts_by_receipt_status")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("counts_by_receipt_status"), Mapping)
            else None
        ),
        "mismatched_case_ids": (
            summary_payload.get("mismatched_case_ids")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("mismatched_case_ids"), list)
            else None
        ),
        "partial_read_notes": notes,
    }


def build_receiving_import_run_record(branch_name: str, run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    context_path = find_existing_path(
        (
            run_dir / "package" / "receiver_local_condition_snapshot.json",
            run_dir / "package" / "receiving_parser_governance_context.json",
        )
    )
    ingress_record_path = run_dir / "ingress" / "ingress_record.json"
    refusal_record_path = run_dir / "refusal" / "refusal_record.json"
    package_receipt_path = run_dir / "package" / "package_receipt.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable receiving summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable receiving manifest: {manifest_error}")

    context_payload: Optional[Dict[str, Any]] = None
    if context_path is not None:
        context_payload, context_error = safe_read_json(context_path)
        if context_error is not None:
            notes.append(
                f"Unreadable receiving-side condition context {repo_relative(context_path)}: {context_error}"
            )

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution_id = summary_payload.get("execution_id")
        if isinstance(summary_execution_id, str):
            execution_id = summary_execution_id

    return {
        "branch_name": branch_name,
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "package_receipt_path": (
            repo_relative(package_receipt_path) if package_receipt_path.is_file() else None
        ),
        "condition_context_path": (
            repo_relative(context_path) if context_path is not None else None
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
            else None
        ),
        "manifest_generated_at": (
            manifest_payload.get("generated_at")
            if isinstance(manifest_payload, Mapping)
            else None
        ),
        "mode": summary_payload.get("mode") if isinstance(summary_payload, Mapping) else None,
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
        "ingress_outcome": (
            summary_payload.get("ingress_outcome")
            if isinstance(summary_payload, Mapping)
            else None
        ),
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
        "blocking_condition": (
            summary_payload.get("blocking_condition")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "parser_mode": (
            summary_payload.get("parser_mode")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "parser_contaminated": (
            summary_payload.get("parser_contaminated")
            if isinstance(summary_payload, Mapping)
            else context_payload.get("parser_contaminated")
            if isinstance(context_payload, Mapping)
            else None
        ),
        "receiver_local_condition_status": (
            summary_payload.get("receiver_local_condition_status")
            if isinstance(summary_payload, Mapping)
            else context_payload.get("parser_governance_status")
            if isinstance(context_payload, Mapping)
            else None
        ),
        "receiver_local_governance_admissible": (
            summary_payload.get("receiver_local_governance_admissible")
            if isinstance(summary_payload, Mapping)
            else context_payload.get("receiver_local_governance_admissible")
            if isinstance(context_payload, Mapping)
            else None
        ),
        "condition_artifact_id": (
            summary_payload.get("condition_artifact_id")
            if isinstance(summary_payload, Mapping)
            else context_payload.get("condition_artifact_id")
            if isinstance(context_payload, Mapping)
            else None
        ),
        "package_attempted_unlawful_standing_transfer": (
            summary_payload.get("package_attempted_unlawful_standing_transfer")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "same_valid_package_may_diverge_by_receiver_local_condition": (
            summary_payload.get("same_valid_package_may_diverge_by_receiver_local_condition")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "total_cases": (
            summary_payload.get("total_cases")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("total_cases"), int)
            else None
        ),
        "counts_by_outcome_type": (
            summary_payload.get("counts_by_outcome_type")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("counts_by_outcome_type"), Mapping)
            else None
        ),
        "counts_by_receipt_status": (
            summary_payload.get("counts_by_receipt_status")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("counts_by_receipt_status"), Mapping)
            else None
        ),
        "mismatched_case_ids": (
            summary_payload.get("mismatched_case_ids")
            if isinstance(summary_payload, Mapping)
            and isinstance(summary_payload.get("mismatched_case_ids"), list)
            else None
        ),
        "partial_read_notes": notes,
    }


def build_receiving_import_branch_record(branch_dir: Path) -> Dict[str, Any]:
    notes: List[str] = []
    run_dirs = list_execution_dirs(branch_dir)
    if branch_dir.is_dir() and not run_dirs:
        notes.append(
            f"No imported receiving-side runs found under {repo_relative(branch_dir)}"
        )

    run_records = [
        build_receiving_import_run_record(branch_dir.name, run_dir) for run_dir in run_dirs
    ]
    latest_run = select_latest_record(run_records)

    return {
        "branch_name": branch_dir.name,
        "branch_path": repo_relative(branch_dir),
        "branch_exists": branch_dir.is_dir(),
        "run_count": len(run_records),
        "run_paths": [record["run_path"] for record in run_records],
        "execution_ids": [record["execution_id"] for record in run_records],
        "latest_run_path": latest_run.get("run_path") if latest_run else None,
        "latest_summary_path": latest_run.get("summary_path") if latest_run else None,
        "latest_ingress_outcome": latest_run.get("ingress_outcome") if latest_run else None,
        "runs": run_records,
        "partial_read_notes": notes,
    }


def build_source_lineage_record(source_runs_root: Path) -> Dict[str, Any]:
    notes: List[str] = []
    if not source_runs_root.is_dir():
        notes.append(f"Source runs root is missing: {repo_relative(source_runs_root)}")

    run_dirs = list_execution_dirs(source_runs_root)
    if source_runs_root.is_dir() and not run_dirs:
        notes.append(f"No source runs found under {repo_relative(source_runs_root)}")

    run_records = [build_source_run_record(run_dir) for run_dir in run_dirs]
    latest_run = select_latest_record(run_records)

    return {
        "source_runs_root_path": repo_relative(source_runs_root),
        "source_runs_root_exists": source_runs_root.is_dir(),
        "source_run_count": len(run_records),
        "source_run_paths": [record["run_path"] for record in run_records],
        "source_execution_ids": [record["execution_id"] for record in run_records],
        "latest_source_run_path": latest_run.get("run_path") if latest_run else None,
        "latest_source_summary_path": (
            latest_run.get("summary_path") if latest_run else None
        ),
        "latest_source_manifest_path": (
            latest_run.get("manifest_path") if latest_run else None
        ),
        "runs": run_records,
        "partial_read_notes": notes,
    }


def build_receiving_imports_record(receiving_imports_root: Path) -> Dict[str, Any]:
    notes: List[str] = []
    if not receiving_imports_root.is_dir():
        notes.append(
            f"Receiving imports root is missing: {repo_relative(receiving_imports_root)}"
        )

    import_note_path = receiving_imports_root / "IMPORT_NOTE.md"
    import_note = read_markdown_surface(import_note_path)
    import_note_text, _import_note_text_error = safe_read_text(import_note_path)
    if import_note["read_error"] is not None:
        notes.append(
            f"Unreadable receiving import note {import_note['path']}: {import_note['read_error']}"
        )

    branch_dirs: List[Path] = []
    if receiving_imports_root.is_dir():
        branch_dirs = sorted(
            path
            for path in receiving_imports_root.iterdir()
            if path.is_dir() and not path.name.startswith(".")
        )

    branch_records = {
        branch_dir.name: build_receiving_import_branch_record(branch_dir)
        for branch_dir in branch_dirs
    }

    return {
        "receiving_imports_root_path": repo_relative(receiving_imports_root),
        "receiving_imports_root_exists": receiving_imports_root.is_dir(),
        "import_note": {
            "path": import_note["path"],
            "exists": import_note["exists"],
            "heading": import_note["heading"],
            "read_error": import_note["read_error"],
            "states_receiving_side_import": (
                contains_text(import_note_text, "receiving-side evidence")
                or contains_text(import_note_text, "receiving side of the")
            ),
            "states_relation_without_merger": (
                contains_text(import_note_text, "without merger")
                or contains_text(import_note_text, "without merging")
                or contains_text(import_note_text, "remain distinct")
            ),
        },
        "imported_branch_names": list(branch_records.keys()),
        "imported_branch_count": len(branch_records),
        "imported_run_count": sum(
            branch.get("run_count", 0) for branch in branch_records.values()
        ),
        "branches": branch_records,
        "partial_read_notes": notes,
    }


def build_readability_surfaces_record(proof_id: str) -> Dict[str, Any]:
    builder_paths = KNOWN_READABILITY_BUILDERS.get(proof_id, {})
    snapshot_builder_path = builder_paths.get("snapshot_builder_path")
    report_builder_path = builder_paths.get("report_builder_path")

    return {
        "snapshot_builder_path": (
            repo_relative(snapshot_builder_path)
            if isinstance(snapshot_builder_path, Path)
            else None
        ),
        "snapshot_builder_exists": (
            snapshot_builder_path.is_file()
            if isinstance(snapshot_builder_path, Path)
            else False
        ),
        "report_builder_path": (
            repo_relative(report_builder_path)
            if isinstance(report_builder_path, Path)
            else None
        ),
        "report_builder_exists": (
            report_builder_path.is_file()
            if isinstance(report_builder_path, Path)
            else False
        ),
        "latest_snapshot": latest_snapshot_artifact(proof_id, "snapshot"),
        "latest_report": latest_snapshot_artifact(proof_id, "report"),
    }


def build_summary_reading(
    source_runs: Sequence[Mapping[str, Any]],
    receiving_runs: Sequence[Mapping[str, Any]],
) -> Dict[str, Any]:
    source_mismatch_support, source_mismatch_ids = extract_mismatched_case_ids(source_runs)
    receiving_mismatch_support, receiving_mismatch_ids = extract_mismatched_case_ids(
        receiving_runs
    )
    mismatch_support_visible = source_mismatch_support or receiving_mismatch_support
    mismatch_ids = sorted(set(source_mismatch_ids + receiving_mismatch_ids))

    mismatch_present: Optional[bool]
    if mismatch_support_visible:
        mismatch_present = bool(mismatch_ids)
    else:
        mismatch_present = None

    return {
        "source_summary_total_cases": sum_numeric_field(source_runs, "total_cases"),
        "source_mode_counts": count_field_values(source_runs, "mode"),
        "source_expected_outcome_counts": {
            "expected_ingress_outcome": count_field_values(
                source_runs, "expected_ingress_outcome"
            ),
            "expected_clean_ingress_outcome": count_field_values(
                source_runs, "expected_clean_ingress_outcome"
            ),
            "expected_contaminated_ingress_outcome": count_field_values(
                source_runs, "expected_contaminated_ingress_outcome"
            ),
            "expected_ingress_under_admissible_receiver_local_condition": (
                count_field_values(
                    source_runs,
                    "expected_ingress_under_admissible_receiver_local_condition",
                )
            ),
            "expected_ingress_under_contaminated_receiver_local_condition": (
                count_field_values(
                    source_runs,
                    "expected_ingress_under_contaminated_receiver_local_condition",
                )
            ),
        },
        "source_package_valid_counts": count_field_values(source_runs, "package_valid"),
        "source_package_ingress_lawful_if_received_counts": count_field_values(
            source_runs, "package_ingress_lawful_if_received"
        ),
        "source_unlawful_standing_transfer_counts": count_field_values(
            source_runs, "package_attempted_unlawful_standing_transfer"
        ),
        "source_counts_by_outcome_type": merge_count_maps(
            source_runs, "counts_by_outcome_type"
        ),
        "source_counts_by_receipt_status": merge_count_maps(
            source_runs, "counts_by_receipt_status"
        ),
        "receiving_summary_total_cases": sum_numeric_field(receiving_runs, "total_cases"),
        "receiving_mode_counts": count_field_values(receiving_runs, "mode"),
        "receiving_branch_counts": count_field_values(receiving_runs, "branch_name"),
        "receiving_outcome_counts": count_field_values(receiving_runs, "ingress_outcome"),
        "receiving_ingress_lawful_counts": count_field_values(
            receiving_runs, "ingress_lawful"
        ),
        "receiving_arrival_status_counts": count_field_values(
            receiving_runs, "arrival_status"
        ),
        "receiving_technical_receipt_counts": count_field_values(
            receiving_runs, "technical_receipt"
        ),
        "receiving_package_valid_counts": count_field_values(
            receiving_runs, "package_valid"
        ),
        "receiving_refusal_visible_counts": count_field_values(
            receiving_runs, "refusal_visible"
        ),
        "receiving_non_passage_counts": count_field_values(
            receiving_runs, "non_passage"
        ),
        "receiving_source_fault_counts": count_field_values(
            receiving_runs, "source_fault"
        ),
        "receiving_parser_mode_counts": count_field_values(
            receiving_runs, "parser_mode"
        ),
        "receiving_parser_contaminated_counts": count_field_values(
            receiving_runs, "parser_contaminated"
        ),
        "receiving_receiver_local_condition_status_counts": count_field_values(
            receiving_runs, "receiver_local_condition_status"
        ),
        "receiving_blocking_condition_counts": count_field_values(
            receiving_runs, "blocking_condition"
        ),
        "receiving_unlawful_standing_transfer_counts": count_field_values(
            receiving_runs, "package_attempted_unlawful_standing_transfer"
        ),
        "receiving_counts_by_outcome_type": merge_count_maps(
            receiving_runs, "counts_by_outcome_type"
        ),
        "receiving_counts_by_receipt_status": merge_count_maps(
            receiving_runs, "counts_by_receipt_status"
        ),
        "mismatched_case_support_visible": mismatch_support_visible,
        "mismatched_case_ids": mismatch_ids,
        "mismatched_cases_present": mismatch_present,
    }


def evaluate_proof_concern_flags(
    proof_id: str,
    source_runs: Sequence[Mapping[str, Any]],
    branch_records: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    receiving_runs = flatten_branch_runs(branch_records)
    source_modes = {record.get("mode") for record in source_runs}
    receiving_outcomes = {record.get("ingress_outcome") for record in receiving_runs}

    clean_branch = branch_records.get("clean")
    contaminated_branch = branch_records.get("contaminated_non_passage")
    lawful_branch = branch_records.get("lawful")
    refusal_branch = branch_records.get("refusal_non_passage")

    clean_latest = (
        select_latest_record(clean_branch.get("runs", []))
        if isinstance(clean_branch, Mapping)
        else None
    )
    contaminated_latest = (
        select_latest_record(contaminated_branch.get("runs", []))
        if isinstance(contaminated_branch, Mapping)
        else None
    )
    lawful_latest = (
        select_latest_record(lawful_branch.get("runs", []))
        if isinstance(lawful_branch, Mapping)
        else None
    )
    refusal_latest = (
        select_latest_record(refusal_branch.get("runs", []))
        if isinstance(refusal_branch, Mapping)
        else None
    )
    latest_source = select_latest_record(source_runs)

    proof_001_visible = (
        proof_id == "cross_carrier_seam_proof_001"
        and "release_invalid" in source_modes
        and "lawful_derivative_ingress" in receiving_outcomes
        and "refusal_non_passage" in receiving_outcomes
        and isinstance(lawful_latest, Mapping)
        and isinstance(refusal_latest, Mapping)
    )

    proof_002_visible = (
        proof_id == "cross_carrier_seam_proof_002"
        and isinstance(clean_latest, Mapping)
        and isinstance(contaminated_latest, Mapping)
        and clean_latest.get("ingress_outcome") == "lawful_derivative_ingress"
        and clean_latest.get("ingress_lawful") is True
        and contaminated_latest.get("technical_receipt") is True
        and contaminated_latest.get("ingress_lawful") is False
        and contaminated_latest.get("parser_contaminated") is True
        and contaminated_latest.get("blocking_condition")
        == "receiving_parser_governance_contamination"
    )

    proof_003_visible = (
        proof_id == "cross_carrier_seam_proof_003"
        and isinstance(clean_latest, Mapping)
        and isinstance(contaminated_latest, Mapping)
        and isinstance(latest_source, Mapping)
        and latest_source.get("package_id") is not None
        and latest_source.get("package_id") == clean_latest.get("package_id")
        and latest_source.get("package_id") == contaminated_latest.get("package_id")
        and clean_latest.get("receiver_local_condition_status") == "admissible"
        and contaminated_latest.get("receiver_local_condition_status") == "contaminated"
        and clean_latest.get("ingress_outcome") == "lawful_derivative_ingress"
        and contaminated_latest.get("ingress_outcome")
        == "receiver_local_contamination_non_passage"
        and contaminated_latest.get("blocking_condition")
        == "receiver_local_parser_governance_contamination"
        and contaminated_latest.get("source_fault") is False
    )

    return {
        "addresses_source_validity_invalidity_and_lawful_ingress_vs_refusal": (
            proof_001_visible
        ),
        "addresses_contaminated_receiving_parser_governance_case": proof_002_visible,
        "addresses_receiver_local_embodied_contamination_case": proof_003_visible,
    }


def build_proof_record(proof_root: Path) -> Dict[str, Any]:
    proof_id = proof_root.name
    script_path = LAB_ROOT / f"run_{proof_id}.py"
    source_runs_root = proof_root / "source_runs"
    receiving_imports_root = proof_root / "receiving_imports"
    receiving_runs_root = proof_root / "receiving_runs"
    receiver_local_condition_path = proof_root / "receiver_local_condition.json"

    source_lineage = build_source_lineage_record(source_runs_root)
    receiving_imports = build_receiving_imports_record(receiving_imports_root)
    branch_records = receiving_imports["branches"]
    receiving_runs = flatten_branch_runs(branch_records)
    concern_flags = evaluate_proof_concern_flags(
        proof_id,
        source_lineage["runs"],
        branch_records,
    )
    readability_surfaces = build_readability_surfaces_record(proof_id)

    notes: List[str] = []
    notes.extend(str(note) for note in source_lineage.get("partial_read_notes", []))
    notes.extend(str(note) for note in receiving_imports.get("partial_read_notes", []))
    for run in source_lineage.get("runs", []):
        notes.extend(str(note) for note in run.get("partial_read_notes", []))
    for branch in branch_records.values():
        notes.extend(str(note) for note in branch.get("partial_read_notes", []))
        for run in branch.get("runs", []):
            notes.extend(str(note) for note in run.get("partial_read_notes", []))

    latest_source = select_latest_record(source_lineage["runs"])

    return {
        "proof_id": proof_id,
        "proof_root_path": repo_relative(proof_root),
        "proof_root_exists": proof_root.is_dir(),
        "script_path": repo_relative(script_path),
        "script_exists": script_path.is_file(),
        "script_headline": script_docstring_headline(script_path),
        "purpose_note": KNOWN_PROOF_PURPOSES.get(proof_id),
        "internalized_archive_status": (
            source_lineage["source_run_count"] > 0
            and receiving_imports["imported_branch_count"] > 0
            and receiving_imports["import_note"]["exists"]
        ),
        "source_side_release_lineage": source_lineage,
        "receiving_side_imported_lineage": receiving_imports,
        "receiving_runs_root_path": repo_relative(receiving_runs_root),
        "receiving_runs_root_exists": receiving_runs_root.is_dir(),
        "receiver_local_condition_path": repo_relative(receiver_local_condition_path),
        "receiver_local_condition_exists": receiver_local_condition_path.is_file(),
        "latest_source_summary_path": (
            latest_source.get("summary_path") if latest_source else None
        ),
        "latest_source_manifest_path": (
            latest_source.get("manifest_path") if latest_source else None
        ),
        "latest_source_package_path": (
            latest_source.get("package_path") if latest_source else None
        ),
        "proof_concern_flags": concern_flags,
        "proof_specific_readability_surfaces": readability_surfaces,
        "summary_reading": build_summary_reading(
            source_lineage["runs"],
            receiving_runs,
        ),
        "partial_read_notes": notes,
    }


def discover_proof_roots() -> List[Path]:
    if not LAB_ROOT.is_dir():
        return []
    return sorted(path for path in LAB_ROOT.glob(PROOF_ROOT_PATTERN) if path.is_dir())


def build_family_level_notes(proof_records: Sequence[Mapping[str, Any]]) -> Dict[str, Any]:
    proof_ids = [str(record.get("proof_id")) for record in proof_records]
    partial_notes: List[str] = []
    for record in proof_records:
        for note in record.get("partial_read_notes", []):
            if isinstance(note, str):
                partial_notes.append(note)

    readability_present_for: List[str] = []
    for record in proof_records:
        surfaces = record.get("proof_specific_readability_surfaces")
        if not isinstance(surfaces, Mapping):
            continue
        latest_snapshot = surfaces.get("latest_snapshot")
        latest_report = surfaces.get("latest_report")
        if (
            isinstance(latest_snapshot, Mapping)
            and latest_snapshot.get("exists") is True
            and isinstance(latest_report, Mapping)
            and latest_report.get("exists") is True
        ):
            proof_id = record.get("proof_id")
            if isinstance(proof_id, str):
                readability_present_for.append(proof_id)

    visible_progression: List[str] = []
    if "cross_carrier_seam_proof_001" in proof_ids:
        visible_progression.append(
            "Proof 001 preserves the first bounded cross-carrier seam split between "
            "source validity or invalidity and visible receiving-side ingress or refusal."
        )
    if "cross_carrier_seam_proof_002" in proof_ids:
        visible_progression.append(
            "Proof 002 preserves the contaminated receiving parser or governance case in "
            "which technical receipt can occur while lawful ingress is still denied."
        )
    if "cross_carrier_seam_proof_003" in proof_ids:
        visible_progression.append(
            "Proof 003 preserves the receiver-local embodied contamination case in which "
            "the same valid package diverges by receiving-side local condition."
        )

    return {
        "proof_differentiation": [
            {
                "proof_id": record.get("proof_id"),
                "purpose_note": record.get("purpose_note"),
            }
            for record in proof_records
        ],
        "visible_progression": visible_progression,
        "proof_specific_readability_present_for": readability_present_for,
        "partial_material_notes": partial_notes,
        "bounded_reading": (
            "The family remains a set of distinct bounded cross-carrier proof turns rather "
            "than one flat transfer story. Proof 001, proof 002, and proof 003 preserve "
            "different seam concerns and together form a growing body of cross-carrier "
            "seam evidence without implying full relational field, mesh, or middleware."
        ),
    }


def build_snapshot_payload(snapshot_path: Path) -> Dict[str, Any]:
    proof_roots = discover_proof_roots()
    proof_records = [build_proof_record(proof_root) for proof_root in proof_roots]

    total_source_runs = sum(
        int(
            record.get("source_side_release_lineage", {}).get("source_run_count", 0) or 0
        )
        for record in proof_records
    )
    total_imported_branches = sum(
        int(
            record.get("receiving_side_imported_lineage", {}).get(
                "imported_branch_count", 0
            )
            or 0
        )
        for record in proof_records
    )
    total_imported_runs = sum(
        int(
            record.get("receiving_side_imported_lineage", {}).get("imported_run_count", 0)
            or 0
        )
        for record in proof_records
    )

    return {
        "metadata": {
            "generated_at": utc_now(),
            "snapshot_builder_path": repo_relative(SCRIPT_PATH),
            "snapshot_source_root": repo_relative(LAB_ROOT),
            "snapshot_path": repo_relative(snapshot_path),
            "implementation_posture": "implementation_local_cross_carrier_family_readability_only",
        },
        "family_summary": {
            "family_id": "cross_carrier_proof_family",
            "family_name": "Cross-Carrier Seam Proof Family",
            "total_cross_carrier_proofs_discovered": len(proof_records),
            "total_source_side_runs_discovered": total_source_runs,
            "total_receiving_side_imported_branches_discovered": total_imported_branches,
            "total_receiving_side_imported_runs_discovered": total_imported_runs,
            "proof_ids_discovered": [record.get("proof_id") for record in proof_records],
        },
        "proofs": proof_records,
        "family_level_notes": build_family_level_notes(proof_records),
    }


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def print_summary(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    family_summary = payload.get("family_summary", {})
    if not isinstance(family_summary, Mapping):
        family_summary = {}

    print("Cross-carrier family snapshot written.")
    print(f"Snapshot path: {repo_relative(snapshot_path)}")
    print(
        "Cross-carrier proofs discovered: "
        f"{family_summary.get('total_cross_carrier_proofs_discovered', 0)}"
    )
    print(
        "Total source runs discovered: "
        f"{family_summary.get('total_source_side_runs_discovered', 0)}"
    )
    print(
        "Total receiving imported branches discovered: "
        f"{family_summary.get('total_receiving_side_imported_branches_discovered', 0)}"
    )


def main() -> int:
    if not LAB_ROOT.is_dir():
        print(f"Lab root is missing: {LAB_ROOT}", file=sys.stderr)
        return 1

    snapshot_path = choose_snapshot_path()
    payload = build_snapshot_payload(snapshot_path)

    try:
        write_snapshot(snapshot_path, payload)
    except OSError as exc:
        print(f"Failed to write cross-carrier family snapshot: {exc}", file=sys.stderr)
        return 1

    print_summary(snapshot_path, payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
