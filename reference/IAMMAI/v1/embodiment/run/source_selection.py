"""
Bounded shared v1 source-selection implementation surface.

This module makes current v1 source admissibility and implementation-local
default selection explicit for proof-slice runners that depend on preserved
prior runs under v1/registry/runs/.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field, replace
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNS_DIR = REPO_ROOT / "v1" / "registry" / "runs"


@dataclass(frozen=True)
class OrdinaryArtifactSpec:
    ref_name: str
    family_name: str
    body_filename: str
    id_field: str
    matter_field: str


ORDINARY_SPECS: Tuple[OrdinaryArtifactSpec, ...] = (
    OrdinaryArtifactSpec(
        ref_name="validation_ref",
        family_name="validation_artifact",
        body_filename="validation_artifact.body.json",
        id_field="validation_id",
        matter_field="target_ref",
    ),
    OrdinaryArtifactSpec(
        ref_name="witness_ref",
        family_name="witness_artifact",
        body_filename="witness_artifact.body.json",
        id_field="witness_id",
        matter_field="target_ref",
    ),
    OrdinaryArtifactSpec(
        ref_name="governance_action_ref",
        family_name="governance_action",
        body_filename="governance_action.body.json",
        id_field="governance_action_id",
        matter_field="matter_ref",
    ),
    OrdinaryArtifactSpec(
        ref_name="transition_ref",
        family_name="transition_record",
        body_filename="transition_record.body.json",
        id_field="transition_id",
        matter_field="matter_ref",
    ),
    OrdinaryArtifactSpec(
        ref_name="state_ref",
        family_name="state_record",
        body_filename="state_record.body.json",
        id_field="state_id",
        matter_field="matter_ref",
    ),
)


@dataclass(frozen=True)
class AdmissibilityCheck:
    name: str
    message: str

    def as_record(self) -> Dict[str, str]:
        return {"name": self.name, "message": self.message}


@dataclass(frozen=True)
class OrdinaryAnchorSource:
    run_dir: Path
    summary_path: Path
    preservation_conformance_path: Path
    canonical_body_paths: Dict[str, Path]
    positive_body_conformance_paths: Dict[str, Path]
    matter_ref: str
    anchor_refs: Dict[str, str]
    admissibility_checks: Tuple[AdmissibilityCheck, ...]
    selection_basis: str
    source_class: str = field(default="ordinary_anchor_source", init=False)

    def as_record(self) -> Dict[str, Any]:
        return {
            "source_class": self.source_class,
            "run_directory": _repo_relative(self.run_dir),
            "selected_summary_ref": _repo_relative(self.summary_path),
            "selected_preservation_conformance_ref": _repo_relative(
                self.preservation_conformance_path
            ),
            "selected_canonical_body_refs": {
                key: _repo_relative(path)
                for key, path in sorted(self.canonical_body_paths.items())
            },
            "selected_body_conformance_refs": {
                key: _repo_relative(path)
                for key, path in sorted(self.positive_body_conformance_paths.items())
            },
            "matter_ref": self.matter_ref,
            "anchor_identity_refs": dict(sorted(self.anchor_refs.items())),
            "admissibility_checks": [
                check.as_record() for check in self.admissibility_checks
            ],
            "selection_basis": self.selection_basis,
        }


@dataclass(frozen=True)
class ContinuityPredecessorSource:
    run_dir: Path
    continuity_dir: Path
    summary_path: Path
    continuity_body_path: Path
    body_conformance_path: Path
    preservation_conformance_path: Path
    anchor_source_note_path: Path
    matter_ref: str
    turn_id: str
    anchor_source_run_dir: Path
    matched_anchor_refs: Dict[str, str]
    admissibility_checks: Tuple[AdmissibilityCheck, ...]
    selection_basis: str
    source_class: str = field(default="continuity_predecessor_source", init=False)

    def as_record(self) -> Dict[str, Any]:
        return {
            "source_class": self.source_class,
            "run_directory": _repo_relative(self.run_dir),
            "selected_continuity_directory": _repo_relative(self.continuity_dir),
            "selected_summary_ref": _repo_relative(self.summary_path),
            "selected_continuity_body_ref": _repo_relative(self.continuity_body_path),
            "selected_body_conformance_ref": _repo_relative(self.body_conformance_path),
            "selected_preservation_conformance_ref": _repo_relative(
                self.preservation_conformance_path
            ),
            "selected_anchor_source_note_ref": _repo_relative(
                self.anchor_source_note_path
            ),
            "matter_ref": self.matter_ref,
            "predecessor_turn_identity": self.turn_id,
            "anchor_source_run_ref": _repo_relative(self.anchor_source_run_dir),
            "matched_anchor_refs": dict(sorted(self.matched_anchor_refs.items())),
            "admissibility_checks": [
                check.as_record() for check in self.admissibility_checks
            ],
            "selection_basis": self.selection_basis,
        }


@dataclass(frozen=True)
class SuccessorContinuitySources:
    ordinary_anchor: OrdinaryAnchorSource
    continuity_predecessor: ContinuityPredecessorSource
    coherence_checks: Tuple[AdmissibilityCheck, ...]
    selection_basis: str
    source_class: str = field(default="successor_continuity_sources", init=False)

    def as_record(self) -> Dict[str, Any]:
        return {
            "source_class": self.source_class,
            "ordinary_anchor_source": self.ordinary_anchor.as_record(),
            "continuity_predecessor_source": self.continuity_predecessor.as_record(),
            "coherence_checks": [check.as_record() for check in self.coherence_checks],
            "selection_basis": self.selection_basis,
        }


class SourceSelectionError(RuntimeError):
    """Base error for bounded v1 source selection."""


class OrdinaryAnchorSourceNotFound(SourceSelectionError):
    """Raised when no admissible ordinary anchor source is available."""


class ContinuityPredecessorSourceNotFound(SourceSelectionError):
    """Raised when no admissible continuity predecessor source is available."""


class SourceCoherenceError(SourceSelectionError):
    """Raised when selected anchor and predecessor sources are not coherent."""


def select_ordinary_anchor_source(
    runs_dir: Path = RUNS_DIR,
    *,
    selected_run_dir: Optional[Path | str] = None,
    required_matter_ref: Optional[str] = None,
) -> OrdinaryAnchorSource:
    """
    Select an admissible ordinary proof-slice run as canonical anchor source.

    Local default selection uses the latest admissible preserved run. That is an
    implementation-local default only. Admissibility is always checked first.
    """

    resolved_runs_dir = runs_dir.resolve()
    if selected_run_dir is not None:
        explicit_run_dir = _resolve_run_dir(selected_run_dir, resolved_runs_dir)
        source, failures = _assess_ordinary_anchor_source(
            explicit_run_dir,
            required_matter_ref=required_matter_ref,
        )
        if source is None:
            raise OrdinaryAnchorSourceNotFound(
                "Explicitly selected ordinary anchor source is not admissible: "
                f"{_repo_relative(explicit_run_dir)}. {_join_failures(failures)}"
            )
        return replace(source, selection_basis="explicit_selected_run_directory")

    candidates = _collect_admissible_ordinary_anchor_sources(
        resolved_runs_dir,
        required_matter_ref=required_matter_ref,
    )
    if candidates:
        return replace(candidates[0], selection_basis="local_default_latest_admissible")

    raise OrdinaryAnchorSourceNotFound(
        "No admissible ordinary anchor source was found under "
        f"{_repo_relative(resolved_runs_dir)}. An admissible ordinary anchor "
        "source requires preserved canonical body material, readable run summary "
        "and conformance surfaces, successful positive ordinary body conformance, "
        "a readable matter relation, and positive preservation outcome."
    )


def select_continuity_predecessor_source(
    runs_dir: Path = RUNS_DIR,
    *,
    selected_continuity_dir: Optional[Path | str] = None,
    required_matter_ref: Optional[str] = None,
    anchor_source: Optional[OrdinaryAnchorSource] = None,
) -> ContinuityPredecessorSource:
    """
    Select an admissible continuity predecessor source.

    Local default selection uses the latest admissible preserved continuity run
    only after positive continuity standing and retained canonical anchoring
    have been confirmed.
    """

    resolved_runs_dir = runs_dir.resolve()
    admissible_anchor_sources = (
        [anchor_source]
        if anchor_source is not None
        else _collect_admissible_ordinary_anchor_sources(
            resolved_runs_dir,
            required_matter_ref=required_matter_ref,
        )
    )
    if not admissible_anchor_sources:
        raise ContinuityPredecessorSourceNotFound(
            "No admissible continuity predecessor source can be selected because "
            "no admissible ordinary anchor source is available under "
            f"{_repo_relative(resolved_runs_dir)}."
        )

    if selected_continuity_dir is not None:
        explicit_continuity_dir = _resolve_continuity_dir(
            selected_continuity_dir,
            resolved_runs_dir,
        )
        source, failures = _assess_continuity_predecessor_source(
            explicit_continuity_dir,
            anchor_sources=admissible_anchor_sources,
            required_matter_ref=required_matter_ref,
            required_anchor_source=anchor_source,
        )
        if source is None:
            raise ContinuityPredecessorSourceNotFound(
                "Explicitly selected continuity predecessor source is not admissible: "
                f"{_repo_relative(explicit_continuity_dir)}. {_join_failures(failures)}"
            )
        return replace(source, selection_basis="explicit_selected_continuity_directory")

    for continuity_dir in _candidate_continuity_dirs(resolved_runs_dir):
        source, _ = _assess_continuity_predecessor_source(
            continuity_dir,
            anchor_sources=admissible_anchor_sources,
            required_matter_ref=required_matter_ref,
            required_anchor_source=anchor_source,
        )
        if source is not None:
            return replace(source, selection_basis="local_default_latest_admissible")

    raise ContinuityPredecessorSourceNotFound(
        "No admissible continuity predecessor source was found under "
        f"{_repo_relative(resolved_runs_dir)}. An admissible predecessor source "
        "requires readable positive continuity body material, successful positive "
        "continuity body conformance, readable anchor-source note material, "
        "positive preservation outcome, and coherent matter and anchor relation."
    )


def select_successor_continuity_sources(
    runs_dir: Path = RUNS_DIR,
    *,
    selected_anchor_run_dir: Optional[Path | str] = None,
    selected_predecessor_continuity_dir: Optional[Path | str] = None,
    required_matter_ref: Optional[str] = None,
) -> SuccessorContinuitySources:
    """
    Select an ordinary anchor source and a coherent continuity predecessor source.

    When no explicit source is provided, the implementation-local default is the
    latest admissible continuity predecessor source, with the ordinary anchor
    source derived from that predecessor's recorded anchor relation.
    """

    resolved_runs_dir = runs_dir.resolve()

    if selected_anchor_run_dir is not None:
        ordinary_anchor = select_ordinary_anchor_source(
            resolved_runs_dir,
            selected_run_dir=selected_anchor_run_dir,
            required_matter_ref=required_matter_ref,
        )
        continuity_predecessor = select_continuity_predecessor_source(
            resolved_runs_dir,
            selected_continuity_dir=selected_predecessor_continuity_dir,
            required_matter_ref=ordinary_anchor.matter_ref,
            anchor_source=ordinary_anchor,
        )
        coherence_checks = _build_source_coherence_checks(
            ordinary_anchor,
            continuity_predecessor,
            required_matter_ref=ordinary_anchor.matter_ref,
        )
        selection_basis = (
            "explicit_anchor_plus_explicit_predecessor"
            if selected_predecessor_continuity_dir is not None
            else "explicit_anchor_plus_local_default_predecessor"
        )
        return SuccessorContinuitySources(
            ordinary_anchor=ordinary_anchor,
            continuity_predecessor=continuity_predecessor,
            coherence_checks=coherence_checks,
            selection_basis=selection_basis,
        )

    continuity_predecessor = select_continuity_predecessor_source(
        resolved_runs_dir,
        selected_continuity_dir=selected_predecessor_continuity_dir,
        required_matter_ref=required_matter_ref,
    )
    ordinary_anchor = select_ordinary_anchor_source(
        resolved_runs_dir,
        selected_run_dir=continuity_predecessor.anchor_source_run_dir,
        required_matter_ref=continuity_predecessor.matter_ref,
    )
    ordinary_anchor = replace(
        ordinary_anchor,
        selection_basis=(
            "derived_from_selected_continuity_predecessor"
            if selected_predecessor_continuity_dir is not None
            else "derived_from_latest_admissible_continuity_predecessor"
        ),
    )
    coherence_checks = _build_source_coherence_checks(
        ordinary_anchor,
        continuity_predecessor,
        required_matter_ref=continuity_predecessor.matter_ref,
    )
    selection_basis = (
        "explicit_predecessor_plus_derived_anchor"
        if selected_predecessor_continuity_dir is not None
        else "local_default_predecessor_plus_derived_anchor"
    )
    return SuccessorContinuitySources(
        ordinary_anchor=ordinary_anchor,
        continuity_predecessor=continuity_predecessor,
        coherence_checks=coherence_checks,
        selection_basis=selection_basis,
    )


def _collect_admissible_ordinary_anchor_sources(
    runs_dir: Path,
    *,
    required_matter_ref: Optional[str],
) -> List[OrdinaryAnchorSource]:
    candidates: List[OrdinaryAnchorSource] = []
    for run_dir in _candidate_run_dirs(runs_dir):
        source, _ = _assess_ordinary_anchor_source(
            run_dir,
            required_matter_ref=required_matter_ref,
        )
        if source is not None:
            candidates.append(source)
    return candidates


def _assess_ordinary_anchor_source(
    run_dir: Path,
    *,
    required_matter_ref: Optional[str],
) -> Tuple[Optional[OrdinaryAnchorSource], List[str]]:
    passed_checks: List[AdmissibilityCheck] = []
    failures: List[str] = []

    canonical_body_paths = {
        spec.ref_name: run_dir / "canonical_bodies" / spec.body_filename
        for spec in ORDINARY_SPECS
    }
    missing_body_paths = [
        _repo_relative(path)
        for path in canonical_body_paths.values()
        if not path.is_file()
    ]
    if missing_body_paths:
        failures.append(
            "missing preserved canonical body files: "
            + ", ".join(sorted(missing_body_paths))
        )
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "canonical_body_material",
                "Preserved ordinary canonical body files are present for all five families.",
            )
        )

    summary_path = _first_existing_path(
        [
            run_dir / "summary" / "run_summary.json",
            run_dir / "run_summary" / "run_summary.json",
        ]
    )
    if summary_path is None:
        failures.append("missing readable ordinary run summary.")
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "run_summary_present",
                f"Ordinary run summary is present at {_repo_relative(summary_path)}.",
            )
        )

    ordinary_bodies: Dict[str, Dict[str, Any]] = {}
    if not missing_body_paths:
        unreadable_body_paths: List[str] = []
        for ref_name, path in canonical_body_paths.items():
            payload = _read_json_file(path)
            if payload is None:
                unreadable_body_paths.append(_repo_relative(path))
            else:
                ordinary_bodies[ref_name] = payload
        if unreadable_body_paths:
            failures.append(
                "unreadable ordinary canonical body JSON: "
                + ", ".join(sorted(unreadable_body_paths))
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "canonical_body_json_readable",
                    "Ordinary canonical body JSON is readable for all five families.",
                )
            )

    summary: Optional[Dict[str, Any]] = None
    if summary_path is not None:
        summary = _read_json_file(summary_path)
        if summary is None:
            failures.append(
                f"ordinary run summary is not readable JSON: {_repo_relative(summary_path)}"
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "run_summary_json_readable",
                    "Ordinary run summary JSON is readable.",
                )
            )

    matter_ref: Optional[str] = None
    if ordinary_bodies:
        matter_ref = _resolve_ordinary_matter(ordinary_bodies)
        if matter_ref is None:
            failures.append(
                "ordinary canonical body material does not expose one coherent matter relation."
            )
        else:
            summary_matter = _normalized_text(summary.get("matter_identity")) if summary else None
            if summary_matter is not None and summary_matter != matter_ref:
                failures.append(
                    "ordinary run summary matter identity does not match canonical body matter relation."
                )
            else:
                passed_checks.append(
                    AdmissibilityCheck(
                        "matter_relation_coherent",
                        f"Ordinary canonical body material exposes coherent matter relation {matter_ref}.",
                    )
                )

    if required_matter_ref is not None:
        normalized_required_matter_ref = _normalized_text(required_matter_ref)
        if normalized_required_matter_ref is None or matter_ref != normalized_required_matter_ref:
            failures.append(
                f"ordinary source does not satisfy required matter relation {required_matter_ref!r}."
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "required_matter_relation",
                    f"Ordinary source satisfies required matter relation {matter_ref}.",
                )
            )

    anchor_refs: Dict[str, str] = {}
    if ordinary_bodies:
        missing_anchor_ids: List[str] = []
        for spec in ORDINARY_SPECS:
            anchor_value = _normalized_text(ordinary_bodies[spec.ref_name].get(spec.id_field))
            if anchor_value is None:
                missing_anchor_ids.append(spec.ref_name)
            else:
                anchor_refs[spec.ref_name] = anchor_value
        if missing_anchor_ids:
            failures.append(
                "ordinary canonical bodies do not expose readable anchor identities for: "
                + ", ".join(sorted(missing_anchor_ids))
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "anchor_identities_readable",
                    "Ordinary canonical bodies expose readable anchor identities for all five families.",
                )
            )

    positive_body_conformance_paths: Dict[str, Path] = {}
    if summary is not None:
        positive_body_entries = _ordinary_positive_body_entries(summary)
        expected_families = {spec.family_name for spec in ORDINARY_SPECS}
        if set(positive_body_entries) != expected_families:
            failures.append(
                "ordinary run summary does not expose positive body-conformance entries for all five families."
            )
        else:
            unreadable_or_failed: List[str] = []
            for spec in ORDINARY_SPECS:
                entry = positive_body_entries[spec.family_name]
                result_ref = _normalized_text(entry.get("result_ref"))
                result_path = _resolve_repo_ref(result_ref)
                if entry.get("status") != "pass" or entry.get("matched_expectation") is not True:
                    unreadable_or_failed.append(spec.family_name)
                    continue
                if result_path is None or not result_path.is_file():
                    unreadable_or_failed.append(spec.family_name)
                    continue
                conformance = _read_json_file(result_path)
                if (
                    conformance is None
                    or conformance.get("status") != "pass"
                    or conformance.get("matched_expectation") is not True
                ):
                    unreadable_or_failed.append(spec.family_name)
                    continue
                positive_body_conformance_paths[spec.family_name] = result_path
            if unreadable_or_failed:
                failures.append(
                    "ordinary positive body-conformance material is missing or failing for: "
                    + ", ".join(sorted(unreadable_or_failed))
                )
            else:
                passed_checks.append(
                    AdmissibilityCheck(
                        "positive_body_conformance",
                        "Ordinary positive body-conformance material is readable and passing for all five families.",
                    )
                )

    preservation_conformance_path: Optional[Path] = None
    if summary is not None:
        preservation_entry = _preservation_entry(summary)
        preservation_ref = (
            _normalized_text(preservation_entry.get("result_ref"))
            if preservation_entry is not None
            else None
        )
        preservation_conformance_path = _resolve_repo_ref(preservation_ref)
        if (
            preservation_entry is None
            or preservation_entry.get("status") != "pass"
            or preservation_conformance_path is None
            or not preservation_conformance_path.is_file()
        ):
            failures.append(
                "ordinary preservation outcome is missing, unreadable, or not passing."
            )
        else:
            preservation_conformance = _read_json_file(preservation_conformance_path)
            if preservation_conformance is None or preservation_conformance.get("status") != "pass":
                failures.append(
                    "ordinary preservation conformance file is unreadable or not passing."
                )
            else:
                passed_checks.append(
                    AdmissibilityCheck(
                        "preservation_outcome",
                        "Ordinary preservation outcome is readable and passing.",
                    )
                )

    if failures:
        return None, failures

    return (
        OrdinaryAnchorSource(
            run_dir=run_dir,
            summary_path=summary_path,
            preservation_conformance_path=preservation_conformance_path,
            canonical_body_paths=canonical_body_paths,
            positive_body_conformance_paths=positive_body_conformance_paths,
            matter_ref=matter_ref,
            anchor_refs=anchor_refs,
            admissibility_checks=tuple(passed_checks),
            selection_basis="admissible_candidate",
        ),
        [],
    )


def _assess_continuity_predecessor_source(
    continuity_dir: Path,
    *,
    anchor_sources: Sequence[OrdinaryAnchorSource],
    required_matter_ref: Optional[str],
    required_anchor_source: Optional[OrdinaryAnchorSource],
) -> Tuple[Optional[ContinuityPredecessorSource], List[str]]:
    passed_checks: List[AdmissibilityCheck] = []
    failures: List[str] = []

    summary_path = _first_existing_path(
        [
            continuity_dir / "summary" / "run_summary.json",
            continuity_dir / "run_summary" / "run_summary.json",
        ]
    )
    if summary_path is None:
        failures.append("missing readable continuity run summary.")
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "run_summary_present",
                f"Continuity run summary is present at {_repo_relative(summary_path)}.",
            )
        )

    summary: Optional[Dict[str, Any]] = None
    if summary_path is not None:
        summary = _read_json_file(summary_path)
        if summary is None:
            failures.append(
                f"continuity run summary is not readable JSON: {_repo_relative(summary_path)}"
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "run_summary_json_readable",
                    "Continuity run summary JSON is readable.",
                )
            )

    body_conformance_path = _resolve_continuity_body_conformance_path(
        continuity_dir,
        summary,
    )
    if body_conformance_path is None or not body_conformance_path.is_file():
        failures.append("missing readable positive continuity body-conformance material.")
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "positive_body_conformance_present",
                f"Positive continuity body conformance is present at {_repo_relative(body_conformance_path)}.",
            )
        )

    body_conformance: Optional[Dict[str, Any]] = None
    if body_conformance_path is not None and body_conformance_path.is_file():
        body_conformance = _read_json_file(body_conformance_path)
        if body_conformance is None:
            failures.append(
                f"continuity body-conformance JSON is unreadable: {_repo_relative(body_conformance_path)}"
            )
        elif body_conformance.get("status") != "pass" or body_conformance.get("matched_expectation") is not True:
            failures.append("continuity positive body conformance is not passing.")
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "positive_body_conformance",
                    "Continuity positive body conformance is readable and passing.",
                )
            )

    continuity_body_path = _resolve_continuity_body_path(
        continuity_dir,
        body_conformance,
    )
    if continuity_body_path is None or not continuity_body_path.is_file():
        failures.append("missing readable positive continuity body material.")
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "continuity_body_present",
                f"Positive continuity body is present at {_repo_relative(continuity_body_path)}.",
            )
        )

    continuity_body: Optional[Dict[str, Any]] = None
    if continuity_body_path is not None and continuity_body_path.is_file():
        continuity_body = _read_json_file(continuity_body_path)
        if continuity_body is None:
            failures.append(
                f"positive continuity body JSON is unreadable: {_repo_relative(continuity_body_path)}"
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "continuity_body_json_readable",
                    "Positive continuity body JSON is readable.",
                )
            )

    anchor_note_path = _resolve_anchor_source_note_path(continuity_dir, summary)
    if anchor_note_path is None or not anchor_note_path.is_file():
        failures.append("missing readable anchor-source note material for continuity source.")
    else:
        passed_checks.append(
            AdmissibilityCheck(
                "anchor_source_note_present",
                f"Anchor-source note is present at {_repo_relative(anchor_note_path)}.",
            )
        )

    anchor_note: Optional[Dict[str, Any]] = None
    if anchor_note_path is not None and anchor_note_path.is_file():
        anchor_note = _read_json_file(anchor_note_path)
        if anchor_note is None:
            failures.append(
                f"anchor-source note JSON is unreadable: {_repo_relative(anchor_note_path)}"
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "anchor_source_note_json_readable",
                    "Anchor-source note JSON is readable.",
                )
            )

    turn_id: Optional[str] = None
    matter_ref: Optional[str] = None
    if continuity_body is not None:
        turn_id = _normalized_text(continuity_body.get("turn_id"))
        matter_ref = _normalized_text(continuity_body.get("matter_ref"))
        if turn_id is None:
            failures.append("continuity body does not expose a readable turn identity.")
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "continuity_turn_identity",
                    f"Continuity body exposes readable turn identity {turn_id}.",
                )
            )
        if matter_ref is None:
            failures.append("continuity body does not expose a readable matter relation.")

    anchor_source_from_note: Optional[OrdinaryAnchorSource] = None
    if anchor_note is not None:
        selected_run_directory = _normalized_text(anchor_note.get("selected_run_directory"))
        if selected_run_directory is None:
            failures.append("anchor-source note does not record selected_run_directory.")
        else:
            anchor_run_dir = _resolve_run_dir(selected_run_directory, RUNS_DIR)
            anchor_source_from_note = _find_anchor_source(anchor_sources, anchor_run_dir)
            if anchor_source_from_note is None:
                failures.append(
                    "anchor-source note does not point to an admissible ordinary anchor source."
                )
            elif (
                required_anchor_source is not None
                and anchor_source_from_note.run_dir != required_anchor_source.run_dir
            ):
                failures.append(
                    "continuity source anchor relation does not match the required ordinary anchor source."
                )
            else:
                passed_checks.append(
                    AdmissibilityCheck(
                        "anchor_source_admissible",
                        f"Continuity source retains admissible canonical anchor relation to {_repo_relative(anchor_source_from_note.run_dir)}.",
                    )
                )

        note_matter_ref = _normalized_text(anchor_note.get("matter_ref"))
        if note_matter_ref is None:
            failures.append("anchor-source note does not expose a readable matter relation.")
        elif matter_ref is not None and note_matter_ref != matter_ref:
            failures.append(
                "anchor-source note matter relation does not match continuity body matter relation."
            )
        elif (
            anchor_source_from_note is not None
            and note_matter_ref != anchor_source_from_note.matter_ref
        ):
            failures.append(
                "anchor-source note matter relation does not match the selected ordinary anchor source."
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "matter_relation_coherent",
                    f"Continuity source exposes coherent matter relation {note_matter_ref}.",
                )
            )

        note_anchor_identity_refs = anchor_note.get("anchor_identity_refs")
        note_anchor_body_refs = anchor_note.get("anchor_body_refs")
        note_preserves_anchor_detail = False
        if note_anchor_identity_refs is not None and not isinstance(note_anchor_identity_refs, dict):
            failures.append("anchor-source note anchor_identity_refs is not a readable object.")
        elif (
            note_anchor_identity_refs is not None
            and anchor_source_from_note is not None
            and not _anchor_identity_refs_match(
                note_anchor_identity_refs,
                anchor_source_from_note.anchor_refs,
            )
        ):
            failures.append(
                "anchor-source note anchor identities do not match the selected ordinary anchor source."
            )
        elif note_anchor_identity_refs is not None and anchor_source_from_note is not None:
            note_preserves_anchor_detail = True
            passed_checks.append(
                AdmissibilityCheck(
                    "anchor_source_note_identity_alignment",
                    "Anchor-source note identity refs match the selected ordinary anchor source.",
                )
            )

        if note_anchor_body_refs is not None and not isinstance(note_anchor_body_refs, dict):
            failures.append("anchor-source note anchor_body_refs is not a readable object.")
        elif (
            note_anchor_body_refs is not None
            and anchor_source_from_note is not None
            and not _anchor_body_refs_match(
                note_anchor_body_refs,
                anchor_source_from_note.canonical_body_paths,
            )
        ):
            failures.append(
                "anchor-source note body refs do not match the selected ordinary anchor source."
            )
        elif note_anchor_body_refs is not None and anchor_source_from_note is not None:
            note_preserves_anchor_detail = True
            passed_checks.append(
                AdmissibilityCheck(
                    "anchor_source_note_body_alignment",
                    "Anchor-source note body refs match the selected ordinary anchor source.",
                )
            )

        if not note_preserves_anchor_detail:
            failures.append(
                "anchor-source note does not preserve readable anchor-specific body or identity detail."
            )

    matched_anchor_refs: Dict[str, str] = {}
    if continuity_body is not None and anchor_source_from_note is not None:
        matched_anchor_refs, mismatched_anchor_fields = _matched_anchor_refs(
            continuity_body,
            anchor_source_from_note,
        )
        if mismatched_anchor_fields:
            failures.append(
                "continuity body anchor refs do not match the selected ordinary anchor source for: "
                + ", ".join(sorted(mismatched_anchor_fields))
            )
        elif not matched_anchor_refs:
            failures.append(
                "continuity body does not retain any canonical anchor refs to the selected ordinary anchor source."
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "anchor_relation_retained",
                    "Continuity body retains canonical artifact anchoring without reducing continuity to predecessor succession alone.",
                )
            )

    if required_matter_ref is not None:
        normalized_required_matter_ref = _normalized_text(required_matter_ref)
        if normalized_required_matter_ref is None or matter_ref != normalized_required_matter_ref:
            failures.append(
                f"continuity source does not satisfy required matter relation {required_matter_ref!r}."
            )
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "required_matter_relation",
                    f"Continuity source satisfies required matter relation {matter_ref}.",
                )
            )

    if summary is not None:
        summary_anchor_run_dir = _summary_anchor_run_dir(summary)
        if (
            summary_anchor_run_dir is not None
            and anchor_source_from_note is not None
            and summary_anchor_run_dir != anchor_source_from_note.run_dir
        ):
            failures.append(
                "continuity run summary anchor source does not match anchor-source note material."
            )

        execution_relation_failures = _check_optional_execution_relation_surface(summary)
        if execution_relation_failures:
            failures.extend(execution_relation_failures)
        else:
            passed_checks.append(
                AdmissibilityCheck(
                    "execution_relation_surface",
                    "Any preserved explicit execution-relation surface is readable and non-failing.",
                )
            )

    preservation_conformance_path: Optional[Path] = None
    if summary is not None:
        preservation_entry = _preservation_entry(summary)
        preservation_ref = (
            _normalized_text(preservation_entry.get("result_ref"))
            if preservation_entry is not None
            else None
        )
        preservation_conformance_path = _resolve_repo_ref(preservation_ref)
        if (
            preservation_entry is None
            or preservation_entry.get("status") != "pass"
            or preservation_conformance_path is None
            or not preservation_conformance_path.is_file()
        ):
            failures.append(
                "continuity preservation outcome is missing, unreadable, or not passing."
            )
        else:
            preservation_conformance = _read_json_file(preservation_conformance_path)
            if preservation_conformance is None or preservation_conformance.get("status") != "pass":
                failures.append(
                    "continuity preservation conformance file is unreadable or not passing."
                )
            else:
                passed_checks.append(
                    AdmissibilityCheck(
                        "preservation_outcome",
                        "Continuity preservation outcome is readable and passing.",
                    )
                )

    if failures:
        return None, failures

    return (
        ContinuityPredecessorSource(
            run_dir=continuity_dir.parent,
            continuity_dir=continuity_dir,
            summary_path=summary_path,
            continuity_body_path=continuity_body_path,
            body_conformance_path=body_conformance_path,
            preservation_conformance_path=preservation_conformance_path,
            anchor_source_note_path=anchor_note_path,
            matter_ref=matter_ref,
            turn_id=turn_id,
            anchor_source_run_dir=anchor_source_from_note.run_dir,
            matched_anchor_refs=matched_anchor_refs,
            admissibility_checks=tuple(passed_checks),
            selection_basis="admissible_candidate",
        ),
        [],
    )


def _build_source_coherence_checks(
    ordinary_anchor: OrdinaryAnchorSource,
    continuity_predecessor: ContinuityPredecessorSource,
    *,
    required_matter_ref: Optional[str],
) -> Tuple[AdmissibilityCheck, ...]:
    checks: List[AdmissibilityCheck] = []
    failures: List[str] = []

    if ordinary_anchor.run_dir != continuity_predecessor.anchor_source_run_dir:
        failures.append(
            "selected continuity predecessor source does not point back to the selected ordinary anchor source."
        )
    else:
        checks.append(
            AdmissibilityCheck(
                "anchor_source_relation",
                "Continuity predecessor source points back to the selected ordinary anchor source.",
            )
        )

    if ordinary_anchor.matter_ref != continuity_predecessor.matter_ref:
        failures.append(
            "selected ordinary anchor source and continuity predecessor source do not share one coherent matter relation."
        )
    else:
        checks.append(
            AdmissibilityCheck(
                "matter_relation",
                f"Selected sources share coherent matter relation {ordinary_anchor.matter_ref}.",
            )
        )

    if required_matter_ref is not None:
        normalized_required_matter_ref = _normalized_text(required_matter_ref)
        if normalized_required_matter_ref is None or ordinary_anchor.matter_ref != normalized_required_matter_ref:
            failures.append(
                f"selected sources do not satisfy required matter relation {required_matter_ref!r}."
            )
        else:
            checks.append(
                AdmissibilityCheck(
                    "required_matter_relation",
                    f"Selected sources satisfy required matter relation {ordinary_anchor.matter_ref}.",
                )
            )

    if failures:
        raise SourceCoherenceError(_join_failures(failures))

    return tuple(checks)


def _candidate_run_dirs(runs_dir: Path) -> List[Path]:
    if not runs_dir.exists():
        return []

    candidates = [path for path in runs_dir.iterdir() if path.is_dir() and not path.name.startswith(".")]
    return sorted(candidates, key=_safe_mtime, reverse=True)


def _candidate_continuity_dirs(runs_dir: Path) -> List[Path]:
    continuity_dirs = []
    for run_dir in _candidate_run_dirs(runs_dir):
        continuity_dir = run_dir / "continuity"
        if continuity_dir.is_dir():
            continuity_dirs.append(continuity_dir)
    return continuity_dirs


def _resolve_run_dir(value: Path | str, runs_dir: Path) -> Path:
    path = _resolve_selection_path(value, runs_dir)
    return path.resolve()


def _resolve_continuity_dir(value: Path | str, runs_dir: Path) -> Path:
    path = _resolve_selection_path(value, runs_dir)
    if path.name == "continuity":
        return path.resolve()
    continuity_path = path / "continuity"
    return continuity_path.resolve()


def _resolve_selection_path(value: Path | str, runs_dir: Path) -> Path:
    path = Path(value)
    if path.is_absolute():
        return path
    if path.parts[:3] == ("v1", "registry", "runs"):
        return REPO_ROOT / path
    return runs_dir / path


def _resolve_repo_ref(value: Optional[str]) -> Optional[Path]:
    normalized_value = _normalized_text(value)
    if normalized_value is None:
        return None
    return (REPO_ROOT / normalized_value).resolve()


def _resolve_ordinary_matter(
    ordinary_bodies: Mapping[str, Mapping[str, Any]]
) -> Optional[str]:
    candidates = {
        _normalized_text(ordinary_bodies[spec.ref_name].get(spec.matter_field))
        for spec in ORDINARY_SPECS
    }
    normalized_candidates = {
        candidate for candidate in candidates if candidate is not None
    }
    if len(normalized_candidates) != 1:
        return None
    return normalized_candidates.pop()


def _ordinary_positive_body_entries(
    summary: Mapping[str, Any]
) -> Dict[str, Mapping[str, Any]]:
    entries: Dict[str, Mapping[str, Any]] = {}
    for entry in _positive_entries(summary, "body_conformance"):
        family_name = _normalized_text(entry.get("artifact_family"))
        if family_name is not None:
            entries[family_name] = entry
    return entries


def _positive_entries(
    summary: Mapping[str, Any],
    surface_name: str,
) -> List[Mapping[str, Any]]:
    layer_outcomes = summary.get("layer_outcomes")
    if not isinstance(layer_outcomes, dict):
        return []
    surface = layer_outcomes.get(surface_name)
    if not isinstance(surface, dict):
        return []
    positive = surface.get("positive")
    if not isinstance(positive, list):
        return []
    return [entry for entry in positive if isinstance(entry, dict)]


def _preservation_entry(summary: Mapping[str, Any]) -> Optional[Mapping[str, Any]]:
    layer_outcomes = summary.get("layer_outcomes")
    if not isinstance(layer_outcomes, dict):
        return None
    preservation = layer_outcomes.get("preservation_write_outcome")
    if not isinstance(preservation, dict):
        return None
    return preservation


def _resolve_continuity_body_conformance_path(
    continuity_dir: Path,
    summary: Optional[Mapping[str, Any]],
) -> Optional[Path]:
    candidates: List[Path] = []
    if summary is not None:
        positive_entries = _positive_entries(summary, "continuity_body_conformance")
        if positive_entries:
            result_ref = _normalized_text(positive_entries[0].get("result_ref"))
            result_path = _resolve_repo_ref(result_ref)
            if result_path is not None:
                candidates.append(result_path)
    candidates.append(
        continuity_dir / "conformance" / "body" / "positive" / "continuity_turn.json"
    )
    return _first_existing_path(candidates)


def _resolve_continuity_body_path(
    continuity_dir: Path,
    body_conformance: Optional[Mapping[str, Any]],
) -> Optional[Path]:
    candidates = [continuity_dir / "canonical_body" / "positive" / "continuity_turn.body.json"]
    if body_conformance is not None:
        body_ref = _normalized_text(body_conformance.get("body_ref"))
        body_path = _resolve_repo_ref(body_ref)
        if body_path is not None:
            candidates.append(body_path)
    return _first_existing_path(candidates)


def _resolve_anchor_source_note_path(
    continuity_dir: Path,
    summary: Optional[Mapping[str, Any]],
) -> Optional[Path]:
    candidates: List[Path] = []
    if summary is not None:
        anchor_source_used = summary.get("anchor_source_used")
        if isinstance(anchor_source_used, dict):
            for key in ("source_note_ref", "anchor_source_note_ref"):
                note_ref = _normalized_text(anchor_source_used.get(key))
                note_path = _resolve_repo_ref(note_ref)
                if note_path is not None:
                    candidates.append(note_path)
    candidates.extend(
        [
            continuity_dir / "source_notes" / "anchor_source_note.json",
            continuity_dir / "anchor_source" / "anchor_source_note.json",
        ]
    )
    return _first_existing_path(candidates)


def _summary_anchor_run_dir(summary: Mapping[str, Any]) -> Optional[Path]:
    anchor_source_used = summary.get("anchor_source_used")
    if not isinstance(anchor_source_used, dict):
        return None
    selected_run_directory = _normalized_text(anchor_source_used.get("selected_run_directory"))
    if selected_run_directory is None:
        return None
    return _resolve_run_dir(selected_run_directory, RUNS_DIR)


def _check_optional_execution_relation_surface(
    summary: Mapping[str, Any]
) -> List[str]:
    failures: List[str] = []
    execution_entries = _positive_entries(summary, "execution_relation_conformance")
    if not execution_entries:
        return failures

    for entry in execution_entries:
        result_ref = _normalized_text(entry.get("result_ref"))
        result_path = _resolve_repo_ref(result_ref)
        if entry.get("status") != "pass" or result_path is None or not result_path.is_file():
            failures.append(
                "continuity execution-relation surface is missing, unreadable, or not passing."
            )
            return failures
        payload = _read_json_file(result_path)
        if payload is None or payload.get("status") != "pass":
            failures.append(
                "continuity execution-relation conformance file is unreadable or not passing."
            )
            return failures
    return failures


def _find_anchor_source(
    anchor_sources: Sequence[OrdinaryAnchorSource],
    run_dir: Path,
) -> Optional[OrdinaryAnchorSource]:
    resolved_run_dir = run_dir.resolve()
    for source in anchor_sources:
        if source.run_dir.resolve() == resolved_run_dir:
            return source
    return None


def _matched_anchor_refs(
    continuity_body: Mapping[str, Any],
    anchor_source: OrdinaryAnchorSource,
) -> Tuple[Dict[str, str], List[str]]:
    matched: Dict[str, str] = {}
    mismatched: List[str] = []
    for spec in ORDINARY_SPECS:
        body_value = _normalized_text(continuity_body.get(spec.ref_name))
        if body_value is None:
            continue
        expected_value = anchor_source.anchor_refs.get(spec.ref_name)
        if body_value == expected_value:
            matched[spec.ref_name] = body_value
        else:
            mismatched.append(spec.ref_name)
    return matched, mismatched


def _anchor_identity_refs_match(
    note_anchor_identity_refs: Mapping[str, Any],
    anchor_refs: Mapping[str, str],
) -> bool:
    for key, expected_value in anchor_refs.items():
        if key not in note_anchor_identity_refs:
            continue
        if _normalized_text(note_anchor_identity_refs.get(key)) != expected_value:
            return False
    return True


def _anchor_body_refs_match(
    note_anchor_body_refs: Mapping[str, Any],
    canonical_body_paths: Mapping[str, Path],
) -> bool:
    for key, expected_path in canonical_body_paths.items():
        if key not in note_anchor_body_refs:
            continue
        candidate_path = _resolve_repo_ref(_normalized_text(note_anchor_body_refs.get(key)))
        if candidate_path is None or candidate_path.resolve() != expected_path.resolve():
            return False
    return True


def _first_existing_path(paths: Sequence[Optional[Path]]) -> Optional[Path]:
    for path in paths:
        if path is not None and path.is_file():
            return path
    return None


def _read_json_file(path: Path) -> Optional[Dict[str, Any]]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _normalized_text(value: Any) -> Optional[str]:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped or None


def _repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def _safe_mtime(path: Path) -> float:
    try:
        return path.stat().st_mtime
    except OSError:
        return float("-inf")


def _join_failures(failures: Sequence[str]) -> str:
    if not failures:
        return "No admissibility detail is available."
    return "; ".join(failures)


__all__ = [
    "AdmissibilityCheck",
    "ContinuityPredecessorSource",
    "ContinuityPredecessorSourceNotFound",
    "OrdinaryAnchorSource",
    "OrdinaryAnchorSourceNotFound",
    "SourceCoherenceError",
    "SourceSelectionError",
    "SuccessorContinuitySources",
    "select_continuity_predecessor_source",
    "select_ordinary_anchor_source",
    "select_successor_continuity_sources",
]
