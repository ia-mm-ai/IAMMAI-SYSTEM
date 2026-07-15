#!/usr/bin/env python3
"""
Build one bounded machine-readable seam-gate result for cross-carrier proof 004.

This script inspects the direct preserved proof-004 artifact set and adjudicates
four object-bound seam-gate questions:

1. origin-side object
2. lawful egress
3. arrival posture
4. origin legibility after crossing

It writes one additive JSON result under lab/snapshots/ without rerunning the
proof, mutating prior artifacts, or converting the result into protocol law.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
REPO_ROOT = SCRIPT_PATH.parents[1]
LAB_ROOT = REPO_ROOT / "lab"
SNAPSHOTS_ROOT = LAB_ROOT / "snapshots"

PROOF_ID = "cross_carrier_seam_proof_004"
PROOF_NAME = "Fourth Cross-Carrier Seam Proof"
PROOF_ROOT = LAB_ROOT / PROOF_ID
SOURCE_RUNS_ROOT = PROOF_ROOT / "source_runs"
RECEIVING_IMPORTS_ROOT = PROOF_ROOT / "receiving_imports"

PROOF_SPEC_PATH = (
    REPO_ROOT / "v1" / "32_PROOF_004_SEAM_GATE_PROOF_SPEC__POST_31.md"
)
GATE_SELECTION_PATH = (
    REPO_ROOT / "v1" / "31_MINIMAL_SEAM_LAW_CROSS_CARRIER_GATE__POST_30.md"
)
SEAM_CASE_LAW_PATH = REPO_ROOT / "SEAM_CASE_LAW__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER.md"
TRANSFER_ACCOUNT_ENTRY_20_PATH = (
    REPO_ROOT
    / "v1"
    / "20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md"
)
SEAM_DECLARATION_PATH = REPO_ROOT / "v1" / "01_SEAM_DECLARATION.md"
TRANSFER_SEAM_PATH = REPO_ROOT / "continuity" / "LAWFUL_TRANSFER_SEAM_v0.md"
RELEASE_AND_INGRESS_PATH = REPO_ROOT / "continuity" / "RELEASE_AND_INGRESS_v0.md"
TRANSITION_ADMISSIBILITY_PATH = REPO_ROOT / "admissibility" / "TRANSITION_ADMISSIBILITY.md"
IMPORT_NOTE_PATH = RECEIVING_IMPORTS_ROOT / "IMPORT_NOTE.md"

SNAPSHOT_PREFIX = f"{PROOF_ID}_snapshot__"
REPORT_PREFIX = f"{PROOF_ID}_report__"

STATUS_SUPPORTED = "supported"
STATUS_AMBIGUOUS = "ambiguous"
STATUS_DRIFTED = "drifted"
STATUS_FAILED = "failed"
ALLOWED_STATUSES = {
    STATUS_SUPPORTED,
    STATUS_AMBIGUOUS,
    STATUS_DRIFTED,
    STATUS_FAILED,
}

BOUNDED_MATTER_NOTE = (
    "the current v1/ line's standing-facing review pressure after lawful "
    "egress and the current cross-carrier threshold, without treating that "
    "pressure as final standing, canon, or total closure."
)


@dataclass(frozen=True)
class LoadedArtifact:
    path: Path
    kind: str
    payload: Optional[Any]
    error: Optional[str]

    @property
    def exists(self) -> bool:
        return self.path.is_file()

    @property
    def readable(self) -> bool:
        return self.payload is not None

    def repo_path(self) -> str:
        return repo_relative(self.path)


@dataclass(frozen=True)
class SourceBranchArtifacts:
    branch_name: str
    run_dir: Optional[Path]
    summary: LoadedArtifact
    canonical_body: LoadedArtifact
    canonical_body_conformance: LoadedArtifact
    origin_condition: LoadedArtifact
    release_record: LoadedArtifact
    package: LoadedArtifact
    package_conformance: LoadedArtifact

    def artifacts(self) -> Tuple[LoadedArtifact, ...]:
        return (
            self.summary,
            self.canonical_body,
            self.canonical_body_conformance,
            self.origin_condition,
            self.release_record,
            self.package,
            self.package_conformance,
        )

    def inspected_paths(self) -> List[str]:
        return [artifact.repo_path() for artifact in self.artifacts() if artifact.readable]

    def inspection_notes(self) -> List[str]:
        notes: List[str] = []
        if self.run_dir is None:
            notes.append(f"No readable source branch run found for {self.branch_name}.")
        for artifact in self.artifacts():
            if artifact.error is not None:
                notes.append(f"{artifact.repo_path()}: {artifact.error}")
        return notes


@dataclass(frozen=True)
class ReceivingBranchArtifacts:
    branch_name: str
    run_dir: Optional[Path]
    summary: LoadedArtifact
    ingress_record: LoadedArtifact
    origin_condition_snapshot: LoadedArtifact
    carried_body_conformance: LoadedArtifact
    package_conformance: LoadedArtifact

    def artifacts(self) -> Tuple[LoadedArtifact, ...]:
        return (
            self.summary,
            self.ingress_record,
            self.origin_condition_snapshot,
            self.carried_body_conformance,
            self.package_conformance,
        )

    def inspected_paths(self) -> List[str]:
        return [artifact.repo_path() for artifact in self.artifacts() if artifact.readable]

    def inspection_notes(self) -> List[str]:
        notes: List[str] = []
        if self.run_dir is None:
            notes.append(f"No readable receiving import run found for {self.branch_name}.")
        for artifact in self.artifacts():
            if artifact.error is not None:
                notes.append(f"{artifact.repo_path()}: {artifact.error}")
        return notes


@dataclass(frozen=True)
class QuestionResult:
    question_id: int
    question_name: str
    status: str
    inspected_paths: Tuple[str, ...]
    reason: str
    does_not_authorize: Tuple[str, ...]
    inspection_notes: Tuple[str, ...]

    def as_record(self) -> Dict[str, Any]:
        return {
            "question_id": self.question_id,
            "question_name": self.question_name,
            "status": self.status,
            "inspected_paths": list(self.inspected_paths),
            "reason": self.reason,
            "does_not_authorize": list(self.does_not_authorize),
            "inspection_notes": list(self.inspection_notes),
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


def choose_output_path() -> Path:
    SNAPSHOTS_ROOT.mkdir(parents=True, exist_ok=True)
    base_name = f"cross_carrier_proof_004_seam_gate_result__{timestamp_slug()}"
    candidate = SNAPSHOTS_ROOT / f"{base_name}.json"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = SNAPSHOTS_ROOT / f"{base_name}__{counter}.json"
        if not candidate.exists():
            return candidate
        counter += 1


def safe_read_text(path: Path) -> LoadedArtifact:
    try:
        text = path.read_text(encoding="utf-8")
        return LoadedArtifact(path=path, kind="text", payload=text, error=None)
    except OSError as exc:
        return LoadedArtifact(path=path, kind="text", payload=None, error=str(exc))


def safe_read_json(path: Path) -> LoadedArtifact:
    text_artifact = safe_read_text(path)
    if text_artifact.error is not None:
        return LoadedArtifact(
            path=path,
            kind="json",
            payload=None,
            error=text_artifact.error,
        )

    try:
        parsed = json.loads(str(text_artifact.payload))
    except json.JSONDecodeError as exc:
        return LoadedArtifact(path=path, kind="json", payload=None, error=str(exc))

    if not isinstance(parsed, dict):
        return LoadedArtifact(
            path=path,
            kind="json",
            payload=None,
            error=f"Top-level JSON value is not an object: {type(parsed).__name__}",
        )

    return LoadedArtifact(path=path, kind="json", payload=parsed, error=None)


def as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def nested_get(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def parse_generated_at(value: Any) -> Optional[datetime]:
    if not isinstance(value, str):
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def list_execution_dirs(root: Path) -> List[Path]:
    if not root.is_dir():
        return []
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and path.name.startswith("execution-")
    )


def latest_run_dir_with_summary_mode(root: Path, expected_mode: str) -> Optional[Path]:
    best_dir: Optional[Path] = None
    best_time: Optional[datetime] = None

    for run_dir in list_execution_dirs(root):
        summary = safe_read_json(run_dir / "summary" / "summary.json")
        payload = as_mapping(summary.payload)
        if payload.get("mode") != expected_mode:
            continue

        parsed = parse_generated_at(payload.get("generated_at"))
        if parsed is None:
            if best_dir is None:
                best_dir = run_dir
            continue

        if best_time is None or parsed > best_time:
            best_time = parsed
            best_dir = run_dir

    return best_dir


def latest_run_dir(root: Path) -> Optional[Path]:
    best_dir: Optional[Path] = None
    best_time: Optional[datetime] = None

    for run_dir in list_execution_dirs(root):
        summary = safe_read_json(run_dir / "summary" / "summary.json")
        payload = as_mapping(summary.payload)
        parsed = parse_generated_at(payload.get("generated_at"))

        if parsed is None:
            if best_dir is None:
                best_dir = run_dir
            continue

        if best_time is None or parsed > best_time:
            best_time = parsed
            best_dir = run_dir

    return best_dir


def load_source_branch(branch_name: str, expected_mode: str) -> SourceBranchArtifacts:
    run_dir = latest_run_dir_with_summary_mode(SOURCE_RUNS_ROOT, expected_mode)
    if run_dir is None:
        missing_path = SOURCE_RUNS_ROOT / f"{branch_name}_missing"
        missing = LoadedArtifact(missing_path, "json", None, "No matching source run found.")
        return SourceBranchArtifacts(
            branch_name=branch_name,
            run_dir=None,
            summary=missing,
            canonical_body=missing,
            canonical_body_conformance=missing,
            origin_condition=missing,
            release_record=missing,
            package=missing,
            package_conformance=missing,
        )

    return SourceBranchArtifacts(
        branch_name=branch_name,
        run_dir=run_dir,
        summary=safe_read_json(run_dir / "summary" / "summary.json"),
        canonical_body=safe_read_json(run_dir / "canonical_body" / "witness_artifact_body.json"),
        canonical_body_conformance=safe_read_json(
            run_dir / "conformance" / "canonical_body_conformance.json"
        ),
        origin_condition=safe_read_json(run_dir / "release" / "origin_approval_condition.json"),
        release_record=safe_read_json(run_dir / "release" / "release_record.json"),
        package=safe_read_json(run_dir / "package" / "transfer_package.json"),
        package_conformance=safe_read_json(
            run_dir / "conformance" / "transfer_package_conformance.json"
        ),
    )


def load_receiving_branch(branch_name: str) -> ReceivingBranchArtifacts:
    branch_root = RECEIVING_IMPORTS_ROOT / branch_name
    run_dir = latest_run_dir(branch_root)
    if run_dir is None:
        missing_path = branch_root / "missing"
        missing = LoadedArtifact(missing_path, "json", None, "No matching receiving import run found.")
        return ReceivingBranchArtifacts(
            branch_name=branch_name,
            run_dir=None,
            summary=missing,
            ingress_record=missing,
            origin_condition_snapshot=missing,
            carried_body_conformance=missing,
            package_conformance=missing,
        )

    return ReceivingBranchArtifacts(
        branch_name=branch_name,
        run_dir=run_dir,
        summary=safe_read_json(run_dir / "summary" / "summary.json"),
        ingress_record=safe_read_json(run_dir / "ingress" / "ingress_record.json"),
        origin_condition_snapshot=safe_read_json(
            run_dir / "package" / "origin_approval_condition_snapshot.json"
        ),
        carried_body_conformance=safe_read_json(
            run_dir / "conformance" / "carried_witness_body_conformance.json"
        ),
        package_conformance=safe_read_json(
            run_dir / "conformance" / "transfer_package_conformance.json"
        ),
    )


def latest_snapshot_path(prefix: str, suffix: str) -> Optional[Path]:
    if not SNAPSHOTS_ROOT.is_dir():
        return None
    candidates = sorted(
        path
        for path in SNAPSHOTS_ROOT.iterdir()
        if path.is_file() and path.name.startswith(prefix) and path.name.endswith(suffix)
    )
    return candidates[-1] if candidates else None


def unique_non_none(values: Iterable[Any]) -> List[Any]:
    seen: List[Any] = []
    for value in values:
        if value is None:
            continue
        if value not in seen:
            seen.append(value)
    return seen


def values_conflict(values: Iterable[Any]) -> bool:
    return len(unique_non_none(values)) > 1


def ensure_proof_object_readable(
    source_obsolete: SourceBranchArtifacts,
    receiving_obsolete: ReceivingBranchArtifacts,
) -> None:
    if not PROOF_ROOT.is_dir():
        raise FileNotFoundError(f"Proof root is missing: {PROOF_ROOT}")

    readable_source = any(artifact.readable for artifact in source_obsolete.artifacts())
    readable_receiving = any(artifact.readable for artifact in receiving_obsolete.artifacts())
    if not readable_source and not readable_receiving:
        raise FileNotFoundError(
            "Proof 004 object could not be inspected at all: neither obsolete-origin "
            "source-side nor obsolete-origin receiving-side artifacts are readable."
        )


def filter_paths(artifacts: Iterable[LoadedArtifact]) -> List[str]:
    return [artifact.repo_path() for artifact in artifacts if artifact.readable]


def question_result(
    *,
    question_id: int,
    question_name: str,
    status: str,
    inspected_paths: Sequence[str],
    reason: str,
    does_not_authorize: Sequence[str],
    inspection_notes: Sequence[str],
) -> QuestionResult:
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"Unsupported question status: {status}")
    return QuestionResult(
        question_id=question_id,
        question_name=question_name,
        status=status,
        inspected_paths=tuple(inspected_paths),
        reason=reason,
        does_not_authorize=tuple(does_not_authorize),
        inspection_notes=tuple(inspection_notes),
    )


def evaluate_origin_side_object(
    source_obsolete: SourceBranchArtifacts,
) -> QuestionResult:
    inspected_paths = source_obsolete.inspected_paths()
    notes = source_obsolete.inspection_notes()

    body = as_mapping(source_obsolete.canonical_body.payload)
    body_conformance = as_mapping(source_obsolete.canonical_body_conformance.payload)
    summary = as_mapping(source_obsolete.summary.payload)
    package = as_mapping(source_obsolete.package.payload)

    family_values = unique_non_none(
        [
            summary.get("artifact_family"),
            package.get("artifact_family"),
            nested_get(package, "lineage", "artifact_family"),
        ]
    )
    witness_values = unique_non_none(
        [
            body.get("witness_id"),
            summary.get("canonical_witness_id"),
            nested_get(package, "lineage", "witness_id"),
        ]
    )
    execution_values = unique_non_none(
        [
            summary.get("execution_id"),
            nested_get(package, "source_carrier", "execution_id"),
            nested_get(package, "lineage", "source_execution_id"),
        ]
    )
    source_body_ref = nested_get(package, "lineage", "source_canonical_body_ref")
    expected_body_ref = (
        source_obsolete.canonical_body.repo_path()
        if source_obsolete.canonical_body.exists
        else None
    )
    body_conformance_status = body_conformance.get("status")

    if not body or not summary or not package:
        return question_result(
            question_id=1,
            question_name="origin_side_object",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "A stable origin-side object cannot be recovered because one or more "
                "key source-side canonical body, summary, or package artifacts are "
                "missing or unreadable."
            ),
            does_not_authorize=(
                "final standing",
                "native authority on the receiving side",
                "closure of the wider seam-law / cross-carrier blocker class",
            ),
            inspection_notes=notes,
        )

    if values_conflict(family_values) or values_conflict(witness_values) or values_conflict(execution_values):
        return question_result(
            question_id=1,
            question_name="origin_side_object",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "Direct source-side artifacts disagree about artifact family, witness "
                "identity, or source execution lineage, so the origin-side object no "
                "longer reads as one cleanly typed source object."
            ),
            does_not_authorize=(
                "final standing",
                "source-side sovereignty by adjacency alone",
                "native authority on the receiving side",
            ),
            inspection_notes=notes,
        )

    if source_body_ref is not None and expected_body_ref is not None and source_body_ref != expected_body_ref:
        return question_result(
            question_id=1,
            question_name="origin_side_object",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "The transfer package lineage points at a different source canonical "
                "body than the preserved origin-side canonical body artifact."
            ),
            does_not_authorize=(
                "final standing",
                "source-side sovereignty by adjacency alone",
                "native authority on the receiving side",
            ),
            inspection_notes=notes,
        )

    if family_values == ["witness_artifact"] and body_conformance_status == "pass" and len(witness_values) == 1 and len(execution_values) == 1:
        return question_result(
            question_id=1,
            question_name="origin_side_object",
            status=STATUS_SUPPORTED,
            inspected_paths=inspected_paths,
            reason=(
                "The obsolete-origin branch preserves one schema-valid source-side "
                "witness artifact whose family, witness identity, and source execution "
                "lineage remain coherent across canonical body, summary, and transfer package."
            ),
            does_not_authorize=(
                "final standing",
                "source-side sovereignty by adjacency alone",
                "native authority on the receiving side",
            ),
            inspection_notes=notes,
        )

    return question_result(
        question_id=1,
        question_name="origin_side_object",
        status=STATUS_AMBIGUOUS,
        inspected_paths=inspected_paths,
        reason=(
            "The origin-side object remains partially legible, but one or more direct "
            "source-side fields needed to bind schema validity or lineage identity are "
            "missing or only partially readable."
        ),
        does_not_authorize=(
            "final standing",
            "source-side sovereignty by adjacency alone",
            "native authority on the receiving side",
        ),
        inspection_notes=notes,
    )


def evaluate_lawful_egress(
    source_obsolete: SourceBranchArtifacts,
) -> QuestionResult:
    inspected_paths = source_obsolete.inspected_paths()
    notes = source_obsolete.inspection_notes()

    origin_condition = as_mapping(source_obsolete.origin_condition.payload)
    release_record = as_mapping(source_obsolete.release_record.payload)
    package = as_mapping(source_obsolete.package.payload)
    package_conformance = as_mapping(source_obsolete.package_conformance.payload)
    summary = as_mapping(source_obsolete.summary.payload)

    if not origin_condition or not release_record or not package:
        return question_result(
            question_id=2,
            question_name="lawful_egress",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "The obsolete-origin branch does not preserve enough direct release-side "
                "artifacts to bind lawful egress as a source-side object-level condition."
            ),
            does_not_authorize=(
                "final downstream standing",
                "native origin on the far side",
                "full transfer-stack closure",
            ),
            inspection_notes=notes,
        )

    origin_status_values = unique_non_none(
        [
            origin_condition.get("origin_approval_condition_status"),
            release_record.get("origin_approval_condition_status"),
            summary.get("origin_approval_condition_status"),
            nested_get(package, "release_context", "origin_approval_condition_status"),
        ]
    )
    release_lawful_values = unique_non_none(
        [
            origin_condition.get("release_lawful"),
            release_record.get("release_lawful"),
            summary.get("release_lawful"),
            nested_get(package, "release_context", "release_lawful"),
        ]
    )
    non_ratification_values = unique_non_none(
        [
            origin_condition.get("release_without_origin_ratification"),
            release_record.get("release_without_origin_ratification"),
            summary.get("release_without_origin_ratification"),
            nested_get(package, "release_context", "release_without_origin_ratification"),
        ]
    )
    sovereignty_values = unique_non_none(
        [
            origin_condition.get("origin_approval_lawfully_sovereign"),
            release_record.get("origin_approval_lawfully_sovereign"),
            summary.get("origin_approval_lawfully_sovereign"),
            nested_get(package, "release_context", "origin_approval_lawfully_sovereign"),
        ]
    )
    distortion_values = unique_non_none(
        [
            origin_condition.get("continued_compliance_would_ratify_distortion"),
            release_record.get("continued_compliance_would_ratify_distortion"),
            summary.get("continued_compliance_would_ratify_distortion"),
            nested_get(package, "release_context", "continued_compliance_would_ratify_distortion"),
        ]
    )
    outcome_values = unique_non_none(
        [
            origin_condition.get("lawful_release_outcome"),
            release_record.get("lawful_release_outcome"),
            summary.get("lawful_release_outcome"),
            nested_get(package, "release_context", "lawful_release_outcome"),
        ]
    )

    if any(
        values_conflict(group)
        for group in (
            origin_status_values,
            release_lawful_values,
            non_ratification_values,
            sovereignty_values,
            distortion_values,
            outcome_values,
        )
    ):
        return question_result(
            question_id=2,
            question_name="lawful_egress",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "Direct release-side artifacts disagree about the obsolete-origin "
                "condition, lawful release, or non-ratified egress posture, so lawful "
                "egress is no longer cleanly typed."
            ),
            does_not_authorize=(
                "final downstream standing",
                "native origin on the far side",
                "canon",
            ),
            inspection_notes=notes,
        )

    package_conformance_status = package_conformance.get("status")
    release_statement_ok = nested_get(package, "seam", "lawful_egress_from_origin_is_distinct_from_arrival")
    full_closure_granted = unique_non_none(
        [
            origin_condition.get("downstream_full_closure_granted"),
            release_record.get("downstream_full_closure_granted"),
            summary.get("downstream_full_closure_granted"),
            nested_get(package, "release_context", "downstream_full_closure_granted"),
        ]
    )

    if package_conformance_status == "fail" or False in release_lawful_values or False in non_ratification_values:
        return question_result(
            question_id=2,
            question_name="lawful_egress",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "The preserved release package or release-side artifacts directly fail "
                "the lawful-egress threshold instead of merely leaving it unclear."
            ),
            does_not_authorize=(
                "final downstream standing",
                "native origin on the far side",
                "full transfer-stack closure",
            ),
            inspection_notes=notes,
        )

    if True in sovereignty_values or True in full_closure_granted:
        return question_result(
            question_id=2,
            question_name="lawful_egress",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "The release-side record drifts toward sovereign origin veto or "
                "downstream closure, which collapses bounded lawful egress into a "
                "stronger claim than the proof object can lawfully bear."
            ),
            does_not_authorize=(
                "final downstream standing",
                "native origin on the far side",
                "canon",
            ),
            inspection_notes=notes,
        )

    if (
        origin_status_values == ["origin_obsolete_or_contaminated"]
        and release_lawful_values == [True]
        and non_ratification_values == [True]
        and sovereignty_values == [False]
        and distortion_values == [True]
        and outcome_values == ["lawful_egress_without_origin_ratification"]
        and package_conformance_status == "pass"
        and release_statement_ok is True
        and full_closure_granted == [False]
    ):
        return question_result(
            question_id=2,
            question_name="lawful_egress",
            status=STATUS_SUPPORTED,
            inspected_paths=inspected_paths,
            reason=(
                "The obsolete-origin branch preserves lawful egress in bounded form: "
                "origin approval is obsolete or contaminated, withholding is visible "
                "but non-sovereign, release proceeds without ratification, and the "
                "package remains valid without granting downstream closure."
            ),
            does_not_authorize=(
                "final downstream standing",
                "native origin on the far side",
                "full transfer-stack closure",
            ),
            inspection_notes=notes,
        )

    return question_result(
        question_id=2,
        question_name="lawful_egress",
        status=STATUS_AMBIGUOUS,
        inspected_paths=inspected_paths,
        reason=(
            "The obsolete-origin branch partially supports lawful egress, but one or "
            "more release-side fields needed to bind non-sovereign approval, "
            "non-ratified release, or package validity remain missing or only partly legible."
        ),
        does_not_authorize=(
            "final downstream standing",
            "native origin on the far side",
            "canon",
        ),
        inspection_notes=notes,
    )


def evaluate_arrival_posture(
    receiving_obsolete: ReceivingBranchArtifacts,
) -> QuestionResult:
    inspected_paths = receiving_obsolete.inspected_paths()
    notes = receiving_obsolete.inspection_notes()

    summary = as_mapping(receiving_obsolete.summary.payload)
    ingress = as_mapping(receiving_obsolete.ingress_record.payload)
    carried_conformance = as_mapping(receiving_obsolete.carried_body_conformance.payload)
    package_conformance = as_mapping(receiving_obsolete.package_conformance.payload)

    if not summary or not ingress:
        return question_result(
            question_id=3,
            question_name="arrival_posture",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "The receiving-side obsolete-origin branch does not preserve enough "
                "direct ingress artifacts to bind a present arrival posture."
            ),
            does_not_authorize=(
                "native standing",
                "native authority",
                "final closure",
            ),
            inspection_notes=notes,
        )

    ingress_outcome_values = unique_non_none(
        [summary.get("ingress_outcome"), ingress.get("ingress_outcome")]
    )
    arrival_status_values = unique_non_none(
        [summary.get("arrival_status"), ingress.get("arrival_status")]
    )
    receipt_values = unique_non_none(
        [summary.get("technical_receipt"), ingress.get("technical_receipt")]
    )
    package_valid_values = unique_non_none(
        [summary.get("package_valid"), ingress.get("package_valid")]
    )
    ingress_lawful_values = unique_non_none(
        [summary.get("ingress_lawful"), ingress.get("ingress_lawful")]
    )
    source_legibility_values = unique_non_none(
        [
            summary.get("source_remains_source"),
            ingress.get("source_remains_source"),
            summary.get("origin_remains_lineage_visible"),
            ingress.get("origin_remains_lineage_visible"),
        ]
    )
    native_force_flags = unique_non_none(
        [
            summary.get("shared_authority"),
            ingress.get("shared_authority"),
            summary.get("standing_upgraded"),
            ingress.get("standing_upgraded"),
            summary.get("final_closure_claimed"),
            ingress.get("final_closure_claimed"),
        ]
    )

    if any(
        values_conflict(group)
        for group in (
            ingress_outcome_values,
            arrival_status_values,
            receipt_values,
            package_valid_values,
            ingress_lawful_values,
        )
    ):
        return question_result(
            question_id=3,
            question_name="arrival_posture",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "Receiving-side summary and ingress artifacts disagree about receipt, "
                "validity, lawful ingress, or arrival status, so the arrival posture "
                "is no longer cleanly typed."
            ),
            does_not_authorize=(
                "native standing",
                "native authority",
                "continuity-wide realization",
            ),
            inspection_notes=notes,
        )

    if (
        carried_conformance.get("status") == "fail"
        or package_conformance.get("status") == "fail"
        or False in receipt_values
        or False in package_valid_values
        or False in ingress_lawful_values
    ):
        return question_result(
            question_id=3,
            question_name="arrival_posture",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "The receiving-side obsolete-origin branch directly fails receipt, "
                "package validity, lawful ingress, or carried-body conformance in a "
                "way that prevents bounded arrival posture from standing."
            ),
            does_not_authorize=(
                "native standing",
                "native authority",
                "final closure",
            ),
            inspection_notes=notes,
        )

    if True in native_force_flags:
        return question_result(
            question_id=3,
            question_name="arrival_posture",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "The receiving-side branch drifts toward shared authority, standing "
                "upgrade, or final closure, which collapses carried arrival into "
                "native-looking force."
            ),
            does_not_authorize=(
                "native standing",
                "native authority",
                "continuity-wide realization",
            ),
            inspection_notes=notes,
        )

    if (
        receipt_values == [True]
        and package_valid_values == [True]
        and ingress_lawful_values == [True]
        and ingress_outcome_values == ["lawful_bounded_in_between_arrival"]
        and arrival_status_values == ["bounded_in_between"]
        and source_legibility_values == [True]
        and carried_conformance.get("status") == "pass"
        and package_conformance.get("status") == "pass"
    ):
        return question_result(
            question_id=3,
            question_name="arrival_posture",
            status=STATUS_SUPPORTED,
            inspected_paths=inspected_paths,
            reason=(
                "The obsolete-origin receiving branch preserves bounded carried "
                "arrival: receipt and package validity are real, ingress is lawful, "
                "arrival remains bounded in-between, and no shared authority, "
                "standing upgrade, or final closure is claimed."
            ),
            does_not_authorize=(
                "native standing",
                "native authority",
                "final closure",
            ),
            inspection_notes=notes,
        )

    return question_result(
        question_id=3,
        question_name="arrival_posture",
        status=STATUS_AMBIGUOUS,
        inspected_paths=inspected_paths,
        reason=(
            "Receiving-side arrival is partially legible, but one or more direct "
            "ingress, receipt, or conformance fields needed to bind bounded carried "
            "arrival remain missing or only partly readable."
        ),
        does_not_authorize=(
            "native standing",
            "native authority",
            "final closure",
        ),
        inspection_notes=notes,
    )


def evaluate_origin_legibility_after_crossing(
    source_obsolete: SourceBranchArtifacts,
    source_clean: SourceBranchArtifacts,
    receiving_obsolete: ReceivingBranchArtifacts,
    receiving_clean: ReceivingBranchArtifacts,
    import_note: LoadedArtifact,
    snapshot: LoadedArtifact,
    report: LoadedArtifact,
) -> QuestionResult:
    inspected_paths = (
        source_obsolete.inspected_paths()
        + source_clean.inspected_paths()
        + receiving_obsolete.inspected_paths()
        + receiving_clean.inspected_paths()
        + filter_paths((import_note, snapshot, report))
    )
    notes = (
        source_obsolete.inspection_notes()
        + source_clean.inspection_notes()
        + receiving_obsolete.inspection_notes()
        + receiving_clean.inspection_notes()
    )
    if import_note.error is not None:
        notes.append(f"{import_note.repo_path()}: {import_note.error}")
    if snapshot.error is not None:
        notes.append(f"{snapshot.repo_path()}: {snapshot.error}")
    if report.error is not None:
        notes.append(f"{report.repo_path()}: {report.error}")

    source_summary = as_mapping(source_obsolete.summary.payload)
    source_package = as_mapping(source_obsolete.package.payload)
    receiving_summary = as_mapping(receiving_obsolete.summary.payload)
    receiving_ingress = as_mapping(receiving_obsolete.ingress_record.payload)
    origin_snapshot = as_mapping(receiving_obsolete.origin_condition_snapshot.payload)
    clean_receiving_ingress = as_mapping(receiving_clean.ingress_record.payload)
    snapshot_payload = as_mapping(snapshot.payload)
    report_text = str(report.payload) if isinstance(report.payload, str) else None
    import_note_text = str(import_note.payload) if isinstance(import_note.payload, str) else None

    if not source_summary or not source_package or not receiving_summary or not receiving_ingress or not origin_snapshot:
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_FAILED,
            inspected_paths=inspected_paths,
            reason=(
                "The proof object does not preserve enough direct cross-side lineage "
                "artifacts to recover source, carried relation, and receiving-side "
                "arrival as distinct after crossing."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "final standing",
            ),
            inspection_notes=notes,
        )

    source_execution_id = source_summary.get("execution_id")
    package_source_execution_id = nested_get(source_package, "source_carrier", "execution_id")
    lineage_source_execution_id = nested_get(source_package, "lineage", "source_execution_id")
    receiving_source_execution_id = receiving_ingress.get("source_execution_id")
    receiving_execution_id = receiving_ingress.get("receiving_execution_id")
    clean_receiving_execution_id = clean_receiving_ingress.get("receiving_execution_id")
    expected_origin_condition_ref = (
        source_obsolete.origin_condition.repo_path()
        if source_obsolete.origin_condition.exists
        else None
    )
    received_origin_condition_ref = origin_snapshot.get("origin_approval_condition_ref")

    origin_condition_id_values = unique_non_none(
        [
            source_summary.get("origin_approval_condition_id"),
            origin_snapshot.get("origin_approval_condition_id"),
            receiving_summary.get("origin_approval_condition_id"),
            receiving_ingress.get("origin_approval_condition_id"),
        ]
    )
    source_visibility_values = unique_non_none(
        [
            source_summary.get("source_remains_source"),
            source_summary.get("origin_remains_lineage_visible"),
            receiving_summary.get("source_remains_source"),
            receiving_summary.get("origin_remains_lineage_visible"),
            receiving_ingress.get("source_remains_source"),
            receiving_ingress.get("origin_remains_lineage_visible"),
            origin_snapshot.get("source_remains_source"),
            origin_snapshot.get("origin_remains_lineage_visible"),
        ]
    )

    if values_conflict(
        [
            source_execution_id,
            package_source_execution_id,
            lineage_source_execution_id,
            receiving_source_execution_id,
        ]
    ):
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "Source execution lineage no longer agrees across source-side release, "
                "transfer package, and receiving-side ingress artifacts, so origin is "
                "being laundered instead of preserved."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "native origin",
            ),
            inspection_notes=notes,
        )

    if values_conflict(origin_condition_id_values):
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "Origin condition identity drifts across source-side and receiving-side "
                "artifacts, which prevents clean recovery of the same carried origin posture."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "native origin",
            ),
            inspection_notes=notes,
        )

    if (
        expected_origin_condition_ref is not None
        and received_origin_condition_ref is not None
        and expected_origin_condition_ref != received_origin_condition_ref
    ):
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "The receiving-side origin snapshot points at a different origin "
                "condition than the preserved source-side release artifact, so origin "
                "relation is being laundered instead of preserved."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "native origin",
            ),
            inspection_notes=notes,
        )

    if source_visibility_values != [True]:
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_DRIFTED,
            inspected_paths=inspected_paths,
            reason=(
                "One or more direct artifacts stop preserving that source remains "
                "source and origin remains lineage-visible across the crossing."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "native origin",
            ),
            inspection_notes=notes,
        )

    import_relation_ok = (
        isinstance(import_note_text, str)
        and "preserves relation without flattening source-side release and receiving-side arrival into one local event" in import_note_text
    )
    report_relation_ok = (
        isinstance(report_text, str)
        and "Import preserves relation without merger: `true`" in report_text
    )
    snapshot_identity = as_mapping(snapshot_payload.get("proof_identity"))
    internalized_archive_status = snapshot_identity.get("internalized_archive_status")
    readability_support_present = any(
        value is True for value in (import_relation_ok, report_relation_ok, internalized_archive_status is True)
    )

    if (
        source_execution_id
        and receiving_execution_id
        and source_execution_id != receiving_execution_id
        and receiving_source_execution_id == source_execution_id
        and package_source_execution_id == source_execution_id
        and lineage_source_execution_id == source_execution_id
        and origin_condition_id_values
        and (
            expected_origin_condition_ref is None
            or received_origin_condition_ref == expected_origin_condition_ref
        )
        and (
            clean_receiving_execution_id is None
            or clean_receiving_execution_id != receiving_execution_id
        )
    ):
        return question_result(
            question_id=4,
            question_name="origin_legibility_after_crossing",
            status=STATUS_SUPPORTED,
            inspected_paths=inspected_paths,
            reason=(
                "Origin remains recoverable after crossing: source-side release and "
                "receiving-side arrival stay distinct, the same origin condition remains "
                "visible on both sides, and the clean and obsolete receiving branches "
                "remain separately identifiable."
            ),
            does_not_authorize=(
                "source-side constitutional force on the receiving side",
                "shared authority",
                "final standing",
            ),
            inspection_notes=tuple(
                notes
                + (
                    []
                    if readability_support_present
                    else [
                        "Readability companions were missing or only partial. Support here still rests on the direct cross-side artifact relation."
                    ]
                )
            ),
        )

    return question_result(
        question_id=4,
        question_name="origin_legibility_after_crossing",
        status=STATUS_AMBIGUOUS,
        inspected_paths=inspected_paths,
        reason=(
            "Cross-side provenance remains partially legible, but one or more direct "
            "signals needed to bind non-merger, branch distinction, or origin-condition "
            "continuity remain missing or only partly readable."
        ),
        does_not_authorize=(
            "source-side constitutional force on the receiving side",
            "shared authority",
            "final standing",
        ),
        inspection_notes=notes,
    )


def supporting_surfaces() -> Dict[str, LoadedArtifact]:
    snapshot_path = latest_snapshot_path(SNAPSHOT_PREFIX, ".json")
    report_path = latest_snapshot_path(REPORT_PREFIX, ".md")
    return {
        "import_note": safe_read_text(IMPORT_NOTE_PATH),
        "proof_spec": safe_read_text(PROOF_SPEC_PATH),
        "gate_selection": safe_read_text(GATE_SELECTION_PATH),
        "seam_case_law": safe_read_text(SEAM_CASE_LAW_PATH),
        "transfer_account_entry_20": safe_read_text(TRANSFER_ACCOUNT_ENTRY_20_PATH),
        "seam_declaration": safe_read_text(SEAM_DECLARATION_PATH),
        "lawful_transfer_seam": safe_read_text(TRANSFER_SEAM_PATH),
        "release_and_ingress": safe_read_text(RELEASE_AND_INGRESS_PATH),
        "transition_admissibility": safe_read_text(TRANSITION_ADMISSIBILITY_PATH),
        "snapshot": safe_read_json(snapshot_path) if snapshot_path is not None else LoadedArtifact(
            path=SNAPSHOTS_ROOT / f"{SNAPSHOT_PREFIX}missing.json",
            kind="json",
            payload=None,
            error="No proof-004 snapshot found under lab/snapshots/.",
        ),
        "report": safe_read_text(report_path) if report_path is not None else LoadedArtifact(
            path=SNAPSHOTS_ROOT / f"{REPORT_PREFIX}missing.md",
            kind="text",
            payload=None,
            error="No proof-004 report found under lab/snapshots/.",
        ),
    }


def build_direct_artifact_paths_inspected(
    source_clean: SourceBranchArtifacts,
    source_obsolete: SourceBranchArtifacts,
    receiving_clean: ReceivingBranchArtifacts,
    receiving_obsolete: ReceivingBranchArtifacts,
    support: Mapping[str, LoadedArtifact],
) -> Dict[str, Any]:
    supporting_artifacts = [
        support["import_note"],
        support["proof_spec"],
        support["gate_selection"],
        support["seam_case_law"],
        support["transfer_account_entry_20"],
        support["seam_declaration"],
        support["lawful_transfer_seam"],
        support["release_and_ingress"],
        support["transition_admissibility"],
        support["snapshot"],
        support["report"],
    ]

    return {
        "source_side_runs": sorted(
            set(source_clean.inspected_paths() + source_obsolete.inspected_paths())
        ),
        "receiving_side_clean_import": sorted(set(receiving_clean.inspected_paths())),
        "receiving_side_obsolete_origin_import": sorted(
            set(receiving_obsolete.inspected_paths())
        ),
        "supporting_surfaces": sorted(set(filter_paths(supporting_artifacts))),
    }


def build_boundary_statement() -> Dict[str, Any]:
    return {
        "statement": (
            "This performed seam-gate result keeps lawful egress, bounded arrival, "
            "and origin legibility distinct from native standing, native origin, and "
            "native authority."
        ),
        "lawful_egress_is_not_native_standing": True,
        "bounded_arrival_is_not_native_origin": True,
        "origin_legibility_is_not_native_authority": True,
        "performed_result_is_not_final_standing": True,
        "performed_result_is_not_canon": True,
        "implementation_local_only": True,
    }


def build_present_consequence(results: Sequence[QuestionResult]) -> str:
    statuses = {result.question_name: result.status for result in results}
    if all(result.status == STATUS_SUPPORTED for result in results):
        return (
            "This performed proof strengthens the bounded seam-law / cross-carrier "
            "reading for proof 004 by supporting a typed origin-side object, lawful "
            "egress, bounded arrival, and recoverable origin legibility without "
            "upgrading the crossing into native force."
        )

    if any(result.status in {STATUS_DRIFTED, STATUS_FAILED} for result in results):
        return (
            "This performed proof keeps the seam gate honest by showing where proof 004 "
            "still drifts, fails, or remains blocked at object level instead of being "
            "flattened into a generic cross-carrier success story."
        )

    return (
        "This performed proof partially clarifies proof 004 as a seam-bound object, "
        "but still leaves one or more gate questions only partially bound on the "
        "visible artifact set."
    )


def build_result_payload(output_path: Path) -> Dict[str, Any]:
    source_clean = load_source_branch("clean", "origin_clean")
    source_obsolete = load_source_branch("obsolete_origin", "origin_obsolete")
    receiving_clean = load_receiving_branch("clean")
    receiving_obsolete = load_receiving_branch("obsolete_origin")
    support = supporting_surfaces()

    ensure_proof_object_readable(source_obsolete, receiving_obsolete)

    question_results = [
        evaluate_origin_side_object(source_obsolete),
        evaluate_lawful_egress(source_obsolete),
        evaluate_arrival_posture(receiving_obsolete),
        evaluate_origin_legibility_after_crossing(
            source_obsolete=source_obsolete,
            source_clean=source_clean,
            receiving_obsolete=receiving_obsolete,
            receiving_clean=receiving_clean,
            import_note=support["import_note"],
            snapshot=support["snapshot"],
            report=support["report"],
        ),
    ]

    return {
        "metadata": {
            "generated_at": utc_now(),
            "builder_path": repo_relative(SCRIPT_PATH),
            "result_path": repo_relative(output_path),
            "proof_id": PROOF_ID,
            "proof_name": PROOF_NAME,
            "proof_root": repo_relative(PROOF_ROOT),
            "governing_proof_spec_path": repo_relative(PROOF_SPEC_PATH),
            "bounded_matter_note": BOUNDED_MATTER_NOTE,
            "implementation_posture": "implementation_local_proof_004_seam_gate_result_only",
            "proof_scope": "proof_004_only",
            "source_of_truth_note": "Direct proof-004 artifact surfaces remain primary. Readability companions are supporting surfaces only.",
        },
        "direct_artifact_paths_inspected": build_direct_artifact_paths_inspected(
            source_clean=source_clean,
            source_obsolete=source_obsolete,
            receiving_clean=receiving_clean,
            receiving_obsolete=receiving_obsolete,
            support=support,
        ),
        "question_results": {
            result.question_name: result.as_record() for result in question_results
        },
        "anti_collapse_boundary_statement": build_boundary_statement(),
        "present_consequence": build_present_consequence(question_results),
        "non_closed_remainder": [
            "wider seam-law blocker class not settled",
            "whole-line closure not settled",
            "final standing not settled",
            "canon not settled",
            "continuity-wide realization not selected by this result",
        ],
    }


def write_result(path: Path, payload: Mapping[str, Any]) -> None:
    path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def print_summary(payload: Mapping[str, Any]) -> None:
    metadata = as_mapping(payload.get("metadata"))
    question_results = as_mapping(payload.get("question_results"))

    print(f"Proof id: {metadata.get('proof_id')}")
    for question_name in (
        "origin_side_object",
        "lawful_egress",
        "arrival_posture",
        "origin_legibility_after_crossing",
    ):
        result = as_mapping(question_results.get(question_name))
        print(f"- {question_name}: {result.get('status')}")
    print(f"Result path: {metadata.get('result_path')}")


def main() -> int:
    try:
        output_path = choose_output_path()
        payload = build_result_payload(output_path)
        write_result(output_path, payload)
        print_summary(payload)
        return 0
    except FileNotFoundError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    except Exception as exc:
        print(f"error: failed to build proof-004 seam-gate result: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
