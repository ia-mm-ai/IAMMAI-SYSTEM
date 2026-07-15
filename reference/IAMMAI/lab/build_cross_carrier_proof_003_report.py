#!/usr/bin/env python3
"""
Build a bounded human-readable companion report for the third cross-carrier seam proof.

This script loads the existing cross-carrier proof 003 snapshot builder, writes
a fresh machine-readable snapshot under lab/snapshots/, and renders one
additive Markdown report from that ranked data. It does not rerun the proof,
mutate old artifacts, or flatten source-side and receiving-side evidence into
one event.
"""

from __future__ import annotations

import importlib.util
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ID = "cross_carrier_seam_proof_003"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SNAPSHOT_BUILDER_PATH = LAB_ROOT / "build_cross_carrier_proof_003_snapshot.py"
RECEIVER_LOCAL_CONDITION_PATH = PROOF_ROOT / "receiver_local_condition.json"


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
            f"Cross-carrier proof 003 snapshot builder is missing: {SNAPSHOT_BUILDER_PATH}"
        )

    spec = importlib.util.spec_from_file_location(
        "iammai_cross_carrier_proof_003_snapshot_builder",
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
            f"Failed to import the cross-carrier proof 003 snapshot builder: {exc}"
        ) from exc

    required_names = (
        "choose_snapshot_path",
        "build_snapshot_payload",
        "write_snapshot",
    )
    missing = [name for name in required_names if not callable(getattr(module, name, None))]
    if missing:
        raise RuntimeError(
            "Cross-carrier proof 003 snapshot builder is missing required callables: "
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


def latest_source_run(source_lineage: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    runs = as_list(source_lineage.get("runs"))
    if not runs:
        return None

    def sort_key(item: Any) -> str:
        run = as_mapping(item)
        generated_at = run.get("summary_generated_at")
        return generated_at if isinstance(generated_at, str) else ""

    return as_mapping(sorted(runs, key=sort_key)[-1])


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


def read_receiver_local_condition() -> Dict[str, Any]:
    payload, error = safe_read_json(RECEIVER_LOCAL_CONDITION_PATH)
    if error is not None:
        return {
            "path": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
            "exists": RECEIVER_LOCAL_CONDITION_PATH.is_file(),
            "read_error": error,
        }

    return {
        "path": repo_relative(RECEIVER_LOCAL_CONDITION_PATH),
        "exists": RECEIVER_LOCAL_CONDITION_PATH.is_file(),
        "read_error": None,
        "generated_at": payload.get("generated_at"),
        "condition_artifact_id": payload.get("condition_artifact_id"),
        "parser_governance_status": payload.get("parser_governance_status"),
        "receiver_local_governance_admissible": payload.get(
            "receiver_local_governance_admissible"
        ),
        "parser_contaminated": payload.get("parser_contaminated"),
        "technical_receipt_supported": payload.get("technical_receipt_supported"),
        "lineage_can_be_preserved": payload.get("lineage_can_be_preserved"),
        "rank_can_be_preserved": payload.get("rank_can_be_preserved"),
        "refusal_visible_if_blocked": payload.get("refusal_visible_if_blocked"),
        "standing_inflation_risk_present": payload.get(
            "standing_inflation_risk_present"
        ),
        "source_blame_shift_pressure_present": payload.get(
            "source_blame_shift_pressure_present"
        ),
        "note": payload.get("note"),
    }


def collect_partial_notes(
    payload: Mapping[str, Any],
    receiver_local_condition: Mapping[str, Any],
) -> List[str]:
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

    receiver_local_note = as_mapping(payload.get("receiver_local_embodiment_note"))
    notes.extend(str(note) for note in as_list(receiver_local_note.get("partial_read_notes")))
    for item in as_list(receiver_local_note.get("supporting_surfaces")):
        surface = as_mapping(item)
        read_error = surface.get("read_error")
        if isinstance(read_error, str) and read_error:
            path = surface.get("path")
            notes.append(f"Unreadable supporting surface {path}: {read_error}")

    read_error = receiver_local_condition.get("read_error")
    if isinstance(read_error, str) and read_error:
        notes.append(
            "Unreadable receiver-local condition artifact "
            f"{receiver_local_condition.get('path')}: {read_error}"
        )

    return notes


def add_source_side_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    run = latest_source_run(source_lineage)

    lines.append("## Source-Side Release Lineage")
    lines.append("")
    lines.append(f"- Source run count: {md_code(source_lineage.get('source_run_count'))}")
    lines.append(f"- Source runs root: {md_code(source_lineage.get('source_runs_root'))}")

    if run is None:
        lines.append("- No readable source-side release run was available in the current snapshot.")
        lines.append("")
        return

    lines.append(f"- Source execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Source run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Source package path: {md_code(run.get('package_path'))}")
    lines.append(f"- Package id: {md_code(run.get('package_id'))}")
    lines.append(
        f"- Canonical witness id: {md_code(run.get('canonical_witness_id'))}"
    )
    lines.append(f"- Package valid: {bool_literal(run.get('package_valid'))}")
    lines.append(
        f"- Canonical body schema valid: {bool_literal(run.get('canonical_body_schema_valid'))}"
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
        "- Expected clean receiver-local outcome: "
        f"{md_code(run.get('expected_ingress_under_admissible_receiver_local_condition'))}"
    )
    lines.append(
        "- Expected contaminated receiver-local outcome: "
        f"{md_code(run.get('expected_ingress_under_contaminated_receiver_local_condition'))}"
    )
    lines.append(
        "- Receiver-local condition controls admissibility: "
        f"{bool_literal(run.get('receiver_local_condition_controls_admissibility'))}"
    )
    lines.append(
        "- Same valid package may diverge by receiver-local condition: "
        f"{bool_literal(run.get('same_valid_package_may_diverge_by_receiver_local_condition'))}"
    )
    lines.append(
        "- Do not blame source for receiver-local contamination: "
        f"{bool_literal(run.get('do_not_blame_source_for_receiver_local_contamination'))}"
    )
    lines.append("")
    lines.append(
        "The source-side release remains source-side release lineage. It does not silently "
        "transfer authority, and it does not predetermine that every technically receivable "
        "arrival will become lawful receiving-side ingress."
    )
    lines.append("")


def add_clean_receiving_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    branches = as_mapping(receiving_lineage.get("branches"))
    branch = as_mapping(branches.get("clean"))
    run = latest_branch_run(receiving_lineage, "clean")

    lines.append("## Receiving-Side Clean Lawful Ingress")
    lines.append("")
    lines.append(f"- Imported branch: {md_code(branch.get('branch_name') or 'clean')}")
    lines.append(f"- Branch path: {md_code(branch.get('branch_path'))}")
    lines.append(f"- Imported run count: {md_code(branch.get('run_count'))}")

    if run is None:
        lines.append("- No readable clean imported receiving-side run was available in the current snapshot.")
        lines.append("")
        return

    lines.append(f"- Receiving execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Imported run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Summary path: {md_code(run.get('summary_path'))}")
    lines.append(
        f"- Receiver-local condition snapshot path: {md_code(run.get('condition_snapshot_path'))}"
    )
    lines.append(f"- Package id: {md_code(run.get('package_id'))}")
    lines.append(
        f"- Receiver-local condition status: {md_code(run.get('receiver_local_condition_status'))}"
    )
    lines.append(
        "- Receiver-local governance admissible: "
        f"{bool_literal(run.get('receiver_local_governance_admissible'))}"
    )
    lines.append(f"- Technical receipt: {bool_literal(run.get('technical_receipt'))}")
    lines.append(f"- Package valid: {bool_literal(run.get('package_valid'))}")
    lines.append(f"- Ingress lawful: {bool_literal(run.get('ingress_lawful'))}")
    lines.append(f"- Ingress outcome: {md_code(run.get('ingress_outcome'))}")
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
    lines.append("")
    lines.append(
        "On the clean imported branch, the same valid package is technically received and "
        "admitted lawfully as derivative-only ingress. Source remains source, shared authority "
        "does not appear, and the receiving-side result remains receiving-side lineage."
    )
    lines.append("")


def add_contaminated_receiving_section(lines: List[str], payload: Mapping[str, Any]) -> None:
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    branches = as_mapping(receiving_lineage.get("branches"))
    branch = as_mapping(branches.get("contaminated_non_passage"))
    run = latest_branch_run(receiving_lineage, "contaminated_non_passage")

    lines.append("## Receiving-Side Contaminated Non-Passage")
    lines.append("")
    lines.append(
        f"- Imported branch: {md_code(branch.get('branch_name') or 'contaminated_non_passage')}"
    )
    lines.append(f"- Branch path: {md_code(branch.get('branch_path'))}")
    lines.append(f"- Imported run count: {md_code(branch.get('run_count'))}")

    if run is None:
        lines.append("- No readable contaminated imported receiving-side run was available in the current snapshot.")
        lines.append("")
        return

    lines.append(f"- Receiving execution id: {md_code(run.get('execution_id'))}")
    lines.append(f"- Imported run path: {md_code(run.get('run_path'))}")
    lines.append(f"- Summary path: {md_code(run.get('summary_path'))}")
    lines.append(
        f"- Receiver-local condition snapshot path: {md_code(run.get('condition_snapshot_path'))}"
    )
    lines.append(f"- Package id: {md_code(run.get('package_id'))}")
    lines.append(
        f"- Receiver-local condition status: {md_code(run.get('receiver_local_condition_status'))}"
    )
    lines.append(
        "- Receiver-local governance admissible: "
        f"{bool_literal(run.get('receiver_local_governance_admissible'))}"
    )
    lines.append(f"- Technical receipt: {bool_literal(run.get('technical_receipt'))}")
    lines.append(f"- Package valid: {bool_literal(run.get('package_valid'))}")
    lines.append(f"- Ingress lawful: {bool_literal(run.get('ingress_lawful'))}")
    lines.append(f"- Ingress outcome: {md_code(run.get('ingress_outcome'))}")
    lines.append(f"- Arrival status: {md_code(run.get('arrival_status'))}")
    lines.append(f"- Refusal visible: {bool_literal(run.get('refusal_visible'))}")
    lines.append(f"- Non-passage: {bool_literal(run.get('non_passage'))}")
    lines.append(f"- Blocking condition: {md_code(run.get('blocking_condition'))}")
    lines.append(f"- Source fault: {bool_literal(run.get('source_fault'))}")
    lines.append(
        f"- `source_remains_source = {str(run.get('source_remains_source')).lower() if run.get('source_remains_source') in (True, False) else 'unreadable'}`"
    )
    lines.append(
        f"- `shared_authority = {str(run.get('shared_authority')).lower() if run.get('shared_authority') in (True, False) else 'unreadable'}`"
    )
    lines.append(
        f"- `standing_upgraded = {str(run.get('standing_upgraded')).lower() if run.get('standing_upgraded') in (True, False) else 'unreadable'}`"
    )
    lines.append("")
    lines.append(
        "On the contaminated imported branch, the same valid package is still technically "
        "received, but lawful ingress is denied. Visible refusal and non-passage remain "
        "preserved, the blocking condition stays receiver-local, and source-side validity "
        "is not rewritten into source fault."
    )
    lines.append("")


def add_receiver_local_threshold_section(
    lines: List[str],
    payload: Mapping[str, Any],
    receiver_local_condition: Mapping[str, Any],
) -> None:
    outcome_reading = as_mapping(payload.get("outcome_reading"))
    cross_branch_relation = as_mapping(outcome_reading.get("cross_branch_relation"))
    receiver_local_note = as_mapping(payload.get("receiver_local_embodiment_note"))
    source_posture = as_mapping(outcome_reading.get("source_side_release_posture"))
    clean_outcome = as_mapping(outcome_reading.get("clean_lawful_derivative_ingress"))
    contaminated_outcome = as_mapping(outcome_reading.get("contaminated_non_passage"))

    lines.append("## Receiver-Local Embodiment Threshold")
    lines.append("")
    lines.append(
        "The specific advance in proof 003 is that contamination is no longer carried only "
        "as a scenario label. The proof now preserves a receiver-local condition surface and "
        "shows the same valid package yielding different lawful outcomes because the receiving-side "
        "local condition differs."
    )
    lines.append("")
    lines.append(
        "- Receiver-local embodiment supported in the current snapshot: "
        f"{bool_literal(receiver_local_note.get('receiver_local_embodiment_supported'))}"
    )
    lines.append(
        "- Same valid package across source and receiving sides: "
        f"{bool_literal(cross_branch_relation.get('same_valid_package_across_source_and_receiving'))}"
    )
    lines.append(
        "- Clean and contaminated condition statuses diverge: "
        f"{bool_literal(cross_branch_relation.get('clean_and_contaminated_condition_statuses_diverge'))}"
    )
    lines.append(
        "- Clean condition artifact id: "
        f"{md_code(as_mapping(receiver_local_note.get('evidence_support')).get('clean_condition_artifact_id'))}"
    )
    lines.append(
        "- Contaminated condition artifact id: "
        f"{md_code(as_mapping(receiver_local_note.get('evidence_support')).get('contaminated_condition_artifact_id'))}"
    )
    lines.append(
        "- Top-level receiver-local condition artifact: "
        f"{md_code(receiver_local_condition.get('path'))}"
    )
    lines.append(
        "- Top-level receiver-local condition currently visible: "
        f"{bool_literal(receiver_local_condition.get('exists'))}"
    )
    lines.append(
        "- Top-level receiver-local parser status: "
        f"{md_code(receiver_local_condition.get('parser_governance_status'))}"
    )
    lines.append(
        "- Top-level receiver-local governance admissible: "
        f"{bool_literal(receiver_local_condition.get('receiver_local_governance_admissible'))}"
    )
    lines.append(
        "- Top-level receiver-local parser contaminated: "
        f"{bool_literal(receiver_local_condition.get('parser_contaminated'))}"
    )
    lines.append(
        "- Import note path: "
        f"{md_code(as_mapping(payload.get('receiving_side_imported_lineage')).get('import_note_path'))}"
    )
    lines.append("")
    lines.append(
        "The top-level receiver-local condition artifact remains an implementation-local surface only. "
        "It helps make receiver-local contamination visibly embodied rather than merely scenario-labeled, "
        "but it does not replace the imported receiving-side runs or convert them into protocol law."
    )
    lines.append("")
    lines.append(
        "The import note likewise remains a readability surface only. It preserves the fact that the "
        "clean and contaminated branches are imported receiving-side evidence, not source-side history."
    )
    lines.append("")
    if (
        source_posture.get("package_id") is not None
        and clean_outcome.get("package_id") is not None
        and contaminated_outcome.get("package_id") is not None
    ):
        lines.append(
            "In bounded terms: the same valid package "
            f"{md_code(source_posture.get('package_id'))} "
            "ingresses lawfully under the clean receiver-local condition and fails lawfully with "
            "visible non-passage under the contaminated receiver-local condition."
        )
        lines.append("")


def render_report(
    payload: Mapping[str, Any],
    *,
    report_path: Path,
    snapshot_path: Path,
    receiver_local_condition: Mapping[str, Any],
) -> str:
    lines: List[str] = []

    metadata = as_mapping(payload.get("metadata"))
    proof_identity = as_mapping(payload.get("proof_identity"))
    source_lineage = as_mapping(payload.get("source_side_release_lineage"))
    receiving_lineage = as_mapping(payload.get("receiving_side_imported_lineage"))
    ranked_reading = as_mapping(payload.get("ranked_proof_reading"))
    outcome_reading = as_mapping(payload.get("outcome_reading"))

    source_posture = as_mapping(outcome_reading.get("source_side_release_posture"))
    clean_outcome = as_mapping(outcome_reading.get("clean_lawful_derivative_ingress"))
    contaminated_outcome = as_mapping(outcome_reading.get("contaminated_non_passage"))

    lines.append("# Cross-Carrier Seam Proof 003 Report")
    lines.append("")
    lines.append(
        "This report is a human-readable companion to the machine-readable "
        "cross-carrier proof 003 snapshot. It is an implementation-local "
        "readability surface only and does not function as protocol law."
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
        "The third cross-carrier seam proof presently reads as one ranked proof object "
        "with distinct source-side and receiving-side lineages preserved in the same body."
    )
    lines.append("")
    lines.append(
        f"- Source-side release lineage remains source-side: {bool_literal(ranked_reading.get('source_side_release_lineage_remains_source_side'))}"
    )
    lines.append(
        f"- Receiving-side clean lawful ingress remains receiving-side: {bool_literal(ranked_reading.get('receiving_side_clean_import_remains_receiving_side'))}"
    )
    lines.append(
        f"- Receiving-side contaminated non-passage remains receiving-side: {bool_literal(ranked_reading.get('receiving_side_contaminated_non_passage_import_remains_receiving_side'))}"
    )
    lines.append(
        f"- Import preserves relation without merger: {bool_literal(ranked_reading.get('import_preserves_relation_without_merger'))}"
    )
    lines.append(
        f"- Receiver-local embodied contamination visible: {bool_literal(ranked_reading.get('receiver_local_embodied_contamination_visible'))}"
    )
    lines.append(
        f"- Source run count: {md_code(source_lineage.get('source_run_count'))}"
    )
    lines.append(
        f"- Imported receiving branch count: {md_code(receiving_lineage.get('imported_branch_count'))}"
    )
    lines.append(
        f"- Source package id: {md_code(source_posture.get('package_id'))}"
    )
    lines.append(
        f"- Clean branch outcome: {md_code(clean_outcome.get('ingress_outcome'))}"
    )
    lines.append(
        f"- Contaminated branch outcome: {md_code(contaminated_outcome.get('ingress_outcome'))}"
    )
    bounded_reading = ranked_reading.get("bounded_reading")
    if isinstance(bounded_reading, str):
        lines.append("")
        lines.append(bounded_reading)
    lines.append("")

    add_source_side_section(lines, payload)
    add_clean_receiving_section(lines, payload)
    add_contaminated_receiving_section(lines, payload)
    add_receiver_local_threshold_section(lines, payload, receiver_local_condition)

    lines.append("## What This Shows")
    lines.append("")
    lines.append(
        "- Lawful derivative-only ingress is preserved on the clean receiving side under an admissible receiver-local condition."
    )
    lines.append("- Source remains source across release and receiving-side ingress.")
    lines.append("- No silent authority inheritance is required for the proof to remain legible.")
    lines.append(
        "- Technical receipt and lawful admissibility remain distinct rather than collapsing into one transport story."
    )
    lines.append(
        "- The same valid package can remain valid while receiver-local contamination blocks lawful ingress."
    )
    lines.append(
        "- Visible refusal and non-passage are preserved on the contaminated receiving side without false blame shift back to source."
    )
    lines.append(
        "- Imported receiving-side evidence remains receiving-side evidence even after it is carried back into the main body."
    )
    lines.append("")

    lines.append("## What It Does Not Yet Show")
    lines.append("")
    lines.append("- Not yet a multi-carrier mesh.")
    lines.append("- Not yet bidirectional sync.")
    lines.append("- Not yet shared canonical state.")
    lines.append("- Not yet a relational field.")
    lines.append("- Not yet an exhaustion of cross-carrier seam jurisprudence.")
    lines.append("- Not yet a flattening of source-side and receiving-side evidence into one undifferentiated proof event.")
    lines.append("")

    partial_notes = collect_partial_notes(payload, receiver_local_condition)
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
        "cross-carrier proof 003 snapshot. It does not replace the snapshot, it does not "
        "rewrite prior artifacts, it does not convert imported receiving-side evidence into "
        "source-side history, and it does not convert implementation-local readability into "
        "protocol law."
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

    receiver_local_condition = read_receiver_local_condition()
    report = render_report(
        payload,
        report_path=report_path,
        snapshot_path=snapshot_path,
        receiver_local_condition=receiver_local_condition,
    )

    try:
        write_report(report_path, report)
    except OSError as exc:
        print(f"Failed to write cross-carrier proof 003 report: {exc}", file=sys.stderr)
        return 1

    print_summary(report_path=report_path, snapshot_path=snapshot_path, payload=payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
