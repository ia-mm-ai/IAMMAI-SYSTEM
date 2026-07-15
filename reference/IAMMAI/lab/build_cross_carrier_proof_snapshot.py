#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the first cross-carrier seam proof.

This script reads the preserved source-side release lineage and the imported
receiving-side lineage for cross_carrier_seam_proof_001 and emits one additive
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

PROOF_ID = "cross_carrier_seam_proof_001"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SOURCE_RUNS_ROOT = PROOF_ROOT / "source_runs"
RECEIVING_IMPORTS_ROOT = PROOF_ROOT / "receiving_imports"
IMPORT_NOTE_PATH = RECEIVING_IMPORTS_ROOT / "IMPORT_NOTE.md"
ACCOUNT_ENTRY_11_PATH = (
    REPO_ROOT / "v1" / "11_TRANSFER_ACCOUNT_ENTRY__FIRST_CROSS_CARRIER_SEAM_PROOF.md"
)
ACCOUNT_ENTRY_12_PATH = (
    REPO_ROOT
    / "v1"
    / "12_TRANSFER_ACCOUNT_ENTRY__CROSS_CARRIER_PROOF_INTERNALIZED.md"
)

EXPECTED_RECEIVING_BRANCHES: Tuple[str, ...] = ("lawful", "refusal_non_passage")


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


def build_source_run_record(run_dir: Path) -> Dict[str, Any]:
    summary_path = run_dir / "summary" / "summary.json"
    manifest_path = run_dir / "manifest" / "manifest.json"
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable source summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable source manifest: {manifest_error}")

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution = summary_payload.get("execution_id")
        if isinstance(summary_execution, str):
            execution_id = summary_execution

    mode = summary_payload.get("mode") if isinstance(summary_payload, Mapping) else None
    expected_ingress_outcome = (
        summary_payload.get("expected_ingress_outcome")
        if isinstance(summary_payload, Mapping)
        else None
    )
    package_ingress_lawful_if_received = (
        summary_payload.get("package_ingress_lawful_if_received")
        if isinstance(summary_payload, Mapping)
        else None
    )
    package_attempted_unlawful_standing_transfer = (
        summary_payload.get("package_attempted_unlawful_standing_transfer")
        if isinstance(summary_payload, Mapping)
        else None
    )

    run_represents = "unclassified_source_release"
    if expected_ingress_outcome == "lawful_derivative_ingress":
        run_represents = "lawful_package_release"
    elif expected_ingress_outcome == "refusal_non_passage":
        run_represents = "invalid_package_release_for_refusal_non_passage"
    elif mode == "release":
        run_represents = "source_release"
    elif mode == "release_invalid":
        run_represents = "source_release_invalid"

    return {
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "mode": mode,
        "run_represents": run_represents,
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
        "summary_generated_at": (
            summary_payload.get("generated_at")
            if isinstance(summary_payload.get("generated_at"), str)
            else None
        )
        if isinstance(summary_payload, Mapping)
        else None,
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
        "package_ingress_lawful_if_received": package_ingress_lawful_if_received,
        "package_attempted_unlawful_standing_transfer": (
            package_attempted_unlawful_standing_transfer
        ),
        "expected_ingress_outcome": expected_ingress_outcome,
        "canonical_body_schema_valid": (
            summary_payload.get("canonical_body_schema_valid")
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
    notes: List[str] = []

    summary_payload, summary_error = safe_read_json(summary_path)
    if summary_error is not None:
        notes.append(f"Unreadable receiving summary: {summary_error}")

    manifest_payload, manifest_error = safe_read_json(manifest_path)
    if manifest_error is not None:
        notes.append(f"Unreadable receiving manifest: {manifest_error}")

    execution_id = run_dir.name
    if isinstance(summary_payload, Mapping):
        summary_execution = summary_payload.get("execution_id")
        if isinstance(summary_execution, str):
            execution_id = summary_execution

    return {
        "branch_name": branch_name,
        "execution_id": execution_id,
        "run_path": repo_relative(run_dir),
        "summary_path": repo_relative(summary_path) if summary_path.is_file() else None,
        "manifest_path": repo_relative(manifest_path) if manifest_path.is_file() else None,
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
        "mode": summary_payload.get("mode") if isinstance(summary_payload, Mapping) else None,
        "artifact_family": (
            summary_payload.get("artifact_family")
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
        "package_attempted_unlawful_standing_transfer": (
            summary_payload.get("package_attempted_unlawful_standing_transfer")
            if isinstance(summary_payload, Mapping)
            else None
        ),
        "source_legibility_status": (
            summary_payload.get("source_legibility_status")
            if isinstance(summary_payload, Mapping)
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


def build_ranked_proof_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    lawful_branch = receiving_lineage.get("branches", {}).get("lawful", {})
    refusal_branch = receiving_lineage.get("branches", {}).get("refusal_non_passage", {})

    source_present = bool(source_lineage.get("source_run_count"))
    lawful_present = bool(lawful_branch.get("run_count"))
    refusal_present = bool(refusal_branch.get("run_count"))
    co_present_inside_same_body = source_present and lawful_present and refusal_present

    return {
        "source_side_release_lineage_remains_source_side": source_present,
        "receiving_side_lawful_import_remains_receiving_side": lawful_present,
        "receiving_side_refusal_import_remains_receiving_side": refusal_present,
        "import_preserves_relation_without_merger": co_present_inside_same_body,
        "source_and_receiving_lineage_co_present_inside_same_body": co_present_inside_same_body,
        "bounded_reading": (
            "Source-side release lineage remains source-side release lineage. "
            "Receiving-side lawful ingress and receiving-side refusal or non-passage "
            "remain receiving-side lineage. Import preserves relation without merger."
        ),
    }


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


def build_outcome_reading(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    source_runs = source_lineage.get("runs", [])
    lawful_run = latest_branch_run(receiving_lineage, "lawful")
    refusal_run = latest_branch_run(receiving_lineage, "refusal_non_passage")

    def all_source_values(field: str, expected: Any) -> Optional[bool]:
        values = [
            run.get(field)
            for run in source_runs
            if isinstance(run, Mapping) and field in run
        ]
        if not values:
            return None
        return all(value == expected for value in values)

    return {
        "source_side_release_posture": {
            "source_remains_source": all_source_values("source_remains_source", True),
            "shared_authority": False if all_source_values("shared_authority", False) else None,
            "standing_transferred": False
            if all_source_values("standing_transferred", False)
            else None,
        },
        "lawful_derivative_ingress": {
            "present": lawful_run is not None,
            "ingress_lawful": lawful_run.get("ingress_lawful") if lawful_run else None,
            "ingress_outcome": lawful_run.get("ingress_outcome") if lawful_run else None,
            "arrival_status": lawful_run.get("arrival_status") if lawful_run else None,
            "source_remains_source": lawful_run.get("source_remains_source") if lawful_run else None,
            "shared_authority": lawful_run.get("shared_authority") if lawful_run else None,
            "standing_upgraded": lawful_run.get("standing_upgraded") if lawful_run else None,
        },
        "refusal_non_passage": {
            "present": refusal_run is not None,
            "ingress_lawful": refusal_run.get("ingress_lawful") if refusal_run else None,
            "ingress_outcome": refusal_run.get("ingress_outcome") if refusal_run else None,
            "refusal_visible": refusal_run.get("refusal_visible") if refusal_run else None,
            "non_passage": refusal_run.get("non_passage") if refusal_run else None,
            "source_remains_source": refusal_run.get("source_remains_source") if refusal_run else None,
            "shared_authority": refusal_run.get("shared_authority") if refusal_run else None,
            "standing_upgraded": refusal_run.get("standing_upgraded") if refusal_run else None,
        },
    }


def read_supporting_surface(path: Path) -> Dict[str, Any]:
    text, error = safe_read_text(path)
    return {
        "path": repo_relative(path),
        "exists": path.is_file(),
        "headline": first_heading(text) if isinstance(text, str) else None,
        "read_error": error,
    }


def build_internalization_note(
    source_lineage: Mapping[str, Any],
    receiving_lineage: Mapping[str, Any],
) -> Dict[str, Any]:
    source_present = bool(source_lineage.get("source_run_count"))
    lawful_present = bool(
        receiving_lineage.get("branches", {}).get("lawful", {}).get("run_count")
    )
    refusal_present = bool(
        receiving_lineage.get("branches", {})
        .get("refusal_non_passage", {})
        .get("run_count")
    )
    import_note_present = bool(receiving_lineage.get("import_note_exists"))

    internalized_archive_status = (
        source_present and lawful_present and refusal_present and import_note_present
    )

    return {
        "internalized_archive_status": internalized_archive_status,
        "supporting_surfaces": [
            read_supporting_surface(IMPORT_NOTE_PATH),
            read_supporting_surface(ACCOUNT_ENTRY_11_PATH),
            read_supporting_surface(ACCOUNT_ENTRY_12_PATH),
        ],
        "evidence_support": {
            "source_side_release_lineage_present": source_present,
            "receiving_side_lawful_import_present": lawful_present,
            "receiving_side_refusal_import_present": refusal_present,
            "import_note_present": import_note_present,
            "first_cross_carrier_threshold_entry_present": ACCOUNT_ENTRY_11_PATH.is_file(),
            "internalized_archive_threshold_entry_present": ACCOUNT_ENTRY_12_PATH.is_file(),
        },
        "bounded_reading": (
            "The first cross-carrier seam proof is internally carried where source-side "
            "release lineage and imported receiving-side lineage are co-present inside "
            "the same body without merger."
            if internalized_archive_status
            else "Current preserved material does not yet support full internalized-archive status."
        ),
    }


def build_snapshot_payload(snapshot_path: Path) -> Dict[str, Any]:
    if not PROOF_ROOT.is_dir():
        raise FileNotFoundError(
            f"Cross-carrier proof root is missing or unreadable: {PROOF_ROOT}"
        )

    source_lineage = build_source_side_lineage()
    receiving_lineage = build_receiving_imports_lineage()
    ranked_reading = build_ranked_proof_reading(source_lineage, receiving_lineage)
    internalization_note = build_internalization_note(source_lineage, receiving_lineage)

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
            "proof_name": "First Cross-Carrier Seam Proof",
            "proof_family": "cross_carrier_seam_proof",
            "artifact_family": "witness_artifact",
            "internalized_archive_status": internalization_note["internalized_archive_status"],
        },
        "source_side_release_lineage": source_lineage,
        "receiving_side_imported_lineage": receiving_lineage,
        "ranked_proof_reading": ranked_reading,
        "outcome_reading": build_outcome_reading(source_lineage, receiving_lineage),
        "internalization_note": internalization_note,
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
