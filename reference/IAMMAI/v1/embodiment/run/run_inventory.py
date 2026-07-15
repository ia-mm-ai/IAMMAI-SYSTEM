"""
Bounded shared v1 run-inventory and run-lineage readability helper.

This module provides one additive implementation-local surface for discovering
and reading preserved runs under v1/registry/runs/ as ranked proof-bearing
turns rather than as a flat bag of folders.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNS_DIR = REPO_ROOT / "v1" / "registry" / "runs"

RUN_CLASS_ORDINARY = "ordinary_run"
RUN_CLASS_CONTINUITY = "continuity_run"
RUN_CLASS_UNKNOWN = "unknown_run"

LINE_ORDINARY = "ordinary"
LINE_CONTINUITY = "continuity"
LINE_UNKNOWN = "unknown"

SURFACE_SHARED_SOURCE_SELECTION = "shared_source_selection"
SURFACE_SHARED_PRESERVATION_LAYOUT = "shared_preservation_layout"
SURFACE_SHARED_CONFORMANCE = "shared_conformance"
SURFACE_SHARED_IDENTIFIER_GENERATION = "shared_identifier_generation"

_TURN_LABELS: Dict[str, int] = {
    "first": 1,
    "second": 2,
    "third": 3,
    "fourth": 4,
    "fifth": 5,
    "sixth": 6,
    "seventh": 7,
    "eighth": 8,
    "ninth": 9,
    "tenth": 10,
}

_PREFERRED_LAYER_DIRS: Dict[str, str] = {
    "canonical_body": "canonical_body",
    "envelope": "envelope",
    "execution_relation": "execution_relation",
    "conformance": "conformance",
    "fixtures": "fixture_outputs",
    "summary": "run_summary",
    "manifest": "manifest",
    "source_notes": "source_notes",
}

_LAYER_DIR_CANDIDATES: Dict[str, Tuple[str, ...]] = {
    "canonical_body": ("canonical_body", "canonical_bodies"),
    "envelope": ("envelope", "envelopes"),
    "execution_relation": ("execution_relation",),
    "conformance": ("conformance",),
    "fixtures": ("fixture_outputs", "fixtures"),
    "summary": ("run_summary", "summary"),
    "manifest": ("manifest",),
    "source_notes": ("source_notes", "anchor_source"),
}


@dataclass(frozen=True)
class RunRecord:
    """Readable bounded record for one preserved run or continuity turn."""

    run_class: str
    line_name: str
    run_directory: Path
    execution_run_directory: Path
    continuity_directory: Optional[Path]
    execution_identity: Optional[str]
    summary_path: Optional[Path]
    manifest_path: Optional[Path]
    canonical_body_paths: Dict[str, Path]
    envelope_paths: Dict[str, Path]
    execution_relation_paths: Dict[str, Path]
    conformance_paths: Dict[str, Path]
    source_note_paths: Dict[str, Path]
    fixture_paths: Dict[str, Path]
    summary_type: Optional[str]
    manifest_type: Optional[str]
    turn_kind: Optional[str]
    turn_rank: Optional[int]
    turn_label: Optional[str]
    matter_ref: Optional[str]
    anchor_source_run_ref: Optional[str]
    predecessor_source_run_ref: Optional[str]
    predecessor_turn_identity: Optional[str]
    source_selection_basis: Optional[str]
    operative_surfaces: Tuple[str, ...]
    operative_surface_evidence: Dict[str, Tuple[str, ...]]
    layout_variant_notes: Tuple[str, ...]
    turn_reading: Optional[str]
    lineage_notes: Tuple[str, ...]
    unreadable_notes: Tuple[str, ...] = field(default_factory=tuple)

    def as_record(self) -> Dict[str, Any]:
        return {
            "run_class": self.run_class,
            "line_name": self.line_name,
            "run_directory": _repo_relative(self.run_directory),
            "execution_run_directory": _repo_relative(self.execution_run_directory),
            "continuity_directory": (
                _repo_relative(self.continuity_directory)
                if self.continuity_directory is not None
                else None
            ),
            "execution_identity": self.execution_identity,
            "summary_path": (
                _repo_relative(self.summary_path)
                if self.summary_path is not None
                else None
            ),
            "manifest_path": (
                _repo_relative(self.manifest_path)
                if self.manifest_path is not None
                else None
            ),
            "canonical_body_paths": _record_paths(self.canonical_body_paths),
            "envelope_paths": _record_paths(self.envelope_paths),
            "execution_relation_paths": _record_paths(self.execution_relation_paths),
            "conformance_paths": _record_paths(self.conformance_paths),
            "source_note_paths": _record_paths(self.source_note_paths),
            "fixture_paths": _record_paths(self.fixture_paths),
            "summary_type": self.summary_type,
            "manifest_type": self.manifest_type,
            "turn_kind": self.turn_kind,
            "turn_rank": self.turn_rank,
            "turn_label": self.turn_label,
            "matter_ref": self.matter_ref,
            "anchor_source_run_ref": self.anchor_source_run_ref,
            "predecessor_source_run_ref": self.predecessor_source_run_ref,
            "predecessor_turn_identity": self.predecessor_turn_identity,
            "source_selection_basis": self.source_selection_basis,
            "operative_surfaces": list(self.operative_surfaces),
            "operative_surface_evidence": {
                key: list(values)
                for key, values in sorted(self.operative_surface_evidence.items())
            },
            "layout_variant_notes": list(self.layout_variant_notes),
            "turn_reading": self.turn_reading,
            "lineage_notes": list(self.lineage_notes),
            "unreadable_notes": list(self.unreadable_notes),
        }


@dataclass(frozen=True)
class InventorySnapshot:
    """Bounded grouped snapshot of preserved run inventory."""

    runs_dir: Path
    ordinary_runs: Tuple[RunRecord, ...]
    continuity_runs: Tuple[RunRecord, ...]
    unknown_runs: Tuple[RunRecord, ...]
    snapshot_notes: Tuple[str, ...] = field(default_factory=tuple)

    def as_record(self) -> Dict[str, Any]:
        return {
            "runs_directory": _repo_relative(self.runs_dir),
            "ordinary_runs": [record.as_record() for record in self.ordinary_runs],
            "continuity_runs": [record.as_record() for record in self.continuity_runs],
            "unknown_runs": [record.as_record() for record in self.unknown_runs],
            "snapshot_notes": list(self.snapshot_notes),
        }


def discover_runs(runs_dir: Path = RUNS_DIR) -> List[RunRecord]:
    """Discover preserved ordinary and continuity runs under v1/registry/runs/."""

    resolved_runs_dir = _resolve_runs_dir(runs_dir)
    records: List[RunRecord] = []

    for execution_run_dir in _candidate_execution_run_dirs(resolved_runs_dir):
        ordinary_record = _read_execution_run_record(execution_run_dir)
        continuity_dir = execution_run_dir / "continuity"
        has_continuity = continuity_dir.is_dir()

        if ordinary_record is not None:
            records.append(ordinary_record)
        if has_continuity:
            records.append(_read_continuity_run_record(continuity_dir))
        if ordinary_record is None and not has_continuity:
            records.append(_read_unknown_run_record(execution_run_dir))

    return _sort_run_records(records)


def discover_ordinary_runs(runs_dir: Path = RUNS_DIR) -> List[RunRecord]:
    """Discover preserved ordinary proof-slice runs."""

    return [record for record in discover_runs(runs_dir) if record.line_name == LINE_ORDINARY]


def discover_continuity_runs(runs_dir: Path = RUNS_DIR) -> List[RunRecord]:
    """Discover preserved continuity proof-slice runs."""

    return [
        record for record in discover_runs(runs_dir) if record.line_name == LINE_CONTINUITY
    ]


def read_run_record(run_path: str | Path, runs_dir: Path = RUNS_DIR) -> RunRecord:
    """
    Read one preserved run record from an execution run directory or continuity directory.
    """

    resolved_runs_dir = _resolve_runs_dir(runs_dir)
    resolved_path = _resolve_run_path(run_path, resolved_runs_dir)

    if resolved_path.name == "continuity" and resolved_path.is_dir():
        return _read_continuity_run_record(resolved_path)

    if not resolved_path.is_dir():
        raise FileNotFoundError(f"Run path does not exist as a readable directory: {run_path}")

    ordinary_record = _read_execution_run_record(resolved_path)
    if ordinary_record is not None:
        return ordinary_record

    continuity_dir = resolved_path / "continuity"
    if continuity_dir.is_dir():
        return _read_continuity_run_record(continuity_dir)

    return _read_unknown_run_record(resolved_path)


def build_inventory_snapshot(runs_dir: Path = RUNS_DIR) -> InventorySnapshot:
    """Build a grouped readable snapshot of the preserved run inventory."""

    resolved_runs_dir = _resolve_runs_dir(runs_dir)
    records = discover_runs(resolved_runs_dir)
    ordinary_runs = tuple(record for record in records if record.line_name == LINE_ORDINARY)
    continuity_runs = tuple(
        record for record in records if record.line_name == LINE_CONTINUITY
    )
    unknown_runs = tuple(record for record in records if record.line_name == LINE_UNKNOWN)

    return InventorySnapshot(
        runs_dir=resolved_runs_dir,
        ordinary_runs=ordinary_runs,
        continuity_runs=continuity_runs,
        unknown_runs=unknown_runs,
        snapshot_notes=_build_snapshot_notes(
            ordinary_runs,
            continuity_runs,
            unknown_runs,
        ),
    )


def _resolve_runs_dir(runs_dir: Path) -> Path:
    resolved = runs_dir.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Runs directory does not exist: {resolved}")
    return resolved


def _candidate_execution_run_dirs(runs_dir: Path) -> List[Path]:
    return sorted(path for path in runs_dir.iterdir() if path.is_dir())


def _read_execution_run_record(execution_run_dir: Path) -> Optional[RunRecord]:
    if not _has_ordinary_material(execution_run_dir):
        return None
    return _read_run_record_internal(
        run_root=execution_run_dir,
        execution_run_dir=execution_run_dir,
        line_name=LINE_ORDINARY,
        run_class=RUN_CLASS_ORDINARY,
        continuity_directory=None,
    )


def _read_continuity_run_record(continuity_dir: Path) -> RunRecord:
    return _read_run_record_internal(
        run_root=continuity_dir,
        execution_run_dir=continuity_dir.parent,
        line_name=LINE_CONTINUITY,
        run_class=RUN_CLASS_CONTINUITY,
        continuity_directory=continuity_dir,
    )


def _read_unknown_run_record(run_dir: Path) -> RunRecord:
    notes = ("Run directory does not expose readable ordinary or continuity indicators.",)
    return RunRecord(
        run_class=RUN_CLASS_UNKNOWN,
        line_name=LINE_UNKNOWN,
        run_directory=run_dir,
        execution_run_directory=run_dir,
        continuity_directory=None,
        execution_identity=_read_execution_identity(run_dir, None, None),
        summary_path=None,
        manifest_path=None,
        canonical_body_paths={},
        envelope_paths={},
        execution_relation_paths={},
        conformance_paths={},
        source_note_paths={},
        fixture_paths={},
        summary_type=None,
        manifest_type=None,
        turn_kind=None,
        turn_rank=None,
        turn_label=None,
        matter_ref=None,
        anchor_source_run_ref=None,
        predecessor_source_run_ref=None,
        predecessor_turn_identity=None,
        source_selection_basis=None,
        operative_surfaces=(),
        operative_surface_evidence={},
        layout_variant_notes=(),
        turn_reading="Unreadable or unknown preserved run.",
        lineage_notes=(),
        unreadable_notes=notes,
    )


def _read_run_record_internal(
    *,
    run_root: Path,
    execution_run_dir: Path,
    line_name: str,
    run_class: str,
    continuity_directory: Optional[Path],
) -> RunRecord:
    layout_variant_notes: List[str] = []
    unreadable_notes: List[str] = []

    summary_dir, summary_notes = _discover_layer_dir(run_root, "summary")
    manifest_dir, manifest_notes = _discover_layer_dir(run_root, "manifest")
    canonical_body_dir, canonical_notes = _discover_layer_dir(run_root, "canonical_body")
    envelope_dir, envelope_notes = _discover_layer_dir(run_root, "envelope")
    execution_relation_dir, execution_relation_notes = _discover_layer_dir(
        run_root,
        "execution_relation",
    )
    conformance_dir, conformance_notes = _discover_layer_dir(run_root, "conformance")
    fixture_dir, fixture_notes = _discover_layer_dir(run_root, "fixtures")
    source_note_dir, source_note_notes = _discover_layer_dir(run_root, "source_notes")

    layout_variant_notes.extend(summary_notes)
    layout_variant_notes.extend(manifest_notes)
    layout_variant_notes.extend(canonical_notes)
    layout_variant_notes.extend(envelope_notes)
    layout_variant_notes.extend(execution_relation_notes)
    layout_variant_notes.extend(conformance_notes)
    layout_variant_notes.extend(fixture_notes)
    layout_variant_notes.extend(source_note_notes)

    summary_path = _discover_singleton_json(summary_dir, "run_summary.json")
    manifest_path = _discover_singleton_json(manifest_dir, "preservation_manifest.json")
    if summary_dir is not None and summary_path is None:
        unreadable_notes.append(
            f"Summary directory exists but no summary JSON was found at {_repo_relative(summary_dir)}."
        )
    if manifest_dir is not None and manifest_path is None:
        unreadable_notes.append(
            f"Manifest directory exists but no manifest JSON was found at {_repo_relative(manifest_dir)}."
        )

    summary_data, summary_error = _read_json_file(summary_path)
    manifest_data, manifest_error = _read_json_file(manifest_path)
    if summary_error is not None:
        unreadable_notes.append(summary_error)
    if manifest_error is not None:
        unreadable_notes.append(manifest_error)

    canonical_body_paths = _collect_json_paths(canonical_body_dir)
    envelope_paths = _collect_json_paths(envelope_dir)
    execution_relation_paths = _collect_json_paths(execution_relation_dir)
    conformance_paths = _collect_json_paths(conformance_dir)
    source_note_paths = _collect_json_paths(source_note_dir)
    fixture_paths = _collect_json_paths(fixture_dir)

    canonical_body_records, canonical_body_errors = _read_json_map(canonical_body_paths)
    conformance_records, conformance_errors = _read_json_map(conformance_paths)
    source_note_records, source_note_errors = _read_json_map(source_note_paths)
    unreadable_notes.extend(canonical_body_errors)
    unreadable_notes.extend(conformance_errors)
    unreadable_notes.extend(source_note_errors)

    summary_type = _as_string(summary_data.get("summary_type")) if summary_data else None
    manifest_type = _as_string(manifest_data.get("manifest_type")) if manifest_data else None
    turn_kind, turn_rank, turn_label = _parse_turn_identity(summary_type)
    execution_identity = _read_execution_identity(run_root, summary_data, manifest_data)
    matter_ref = _read_matter_ref(
        line_name=line_name,
        summary_data=summary_data,
        manifest_data=manifest_data,
        canonical_body_records=canonical_body_records,
        source_note_records=source_note_records,
    )
    anchor_source_run_ref = _read_anchor_source_run_ref(
        summary_data,
        manifest_data,
        source_note_records,
    )
    predecessor_source_run_ref = _read_predecessor_source_run_ref(
        summary_data,
        manifest_data,
        source_note_records,
    )
    predecessor_turn_identity = _read_predecessor_turn_identity(
        summary_data,
        manifest_data,
        source_note_records,
        canonical_body_records,
    )
    source_selection_basis = _read_source_selection_basis(summary_data, manifest_data)

    operative_surface_evidence = _infer_operative_surfaces(
        line_name=line_name,
        turn_kind=turn_kind,
        turn_rank=turn_rank,
        summary_type=summary_type,
        summary_data=summary_data,
        manifest_data=manifest_data,
        conformance_records=conformance_records,
        source_note_records=source_note_records,
    )
    operative_surfaces = tuple(sorted(operative_surface_evidence))

    lineage_notes = _build_lineage_notes(
        line_name=line_name,
        summary_type=summary_type,
        turn_kind=turn_kind,
        turn_label=turn_label,
        operative_surfaces=operative_surfaces,
        layout_variant_notes=layout_variant_notes,
    )
    turn_reading = _build_turn_reading(
        line_name=line_name,
        turn_kind=turn_kind,
        turn_label=turn_label,
        operative_surfaces=operative_surfaces,
    )

    return RunRecord(
        run_class=run_class,
        line_name=line_name,
        run_directory=run_root,
        execution_run_directory=execution_run_dir,
        continuity_directory=continuity_directory,
        execution_identity=execution_identity,
        summary_path=summary_path,
        manifest_path=manifest_path,
        canonical_body_paths=canonical_body_paths,
        envelope_paths=envelope_paths,
        execution_relation_paths=execution_relation_paths,
        conformance_paths=conformance_paths,
        source_note_paths=source_note_paths,
        fixture_paths=fixture_paths,
        summary_type=summary_type,
        manifest_type=manifest_type,
        turn_kind=turn_kind,
        turn_rank=turn_rank,
        turn_label=turn_label,
        matter_ref=matter_ref,
        anchor_source_run_ref=anchor_source_run_ref,
        predecessor_source_run_ref=predecessor_source_run_ref,
        predecessor_turn_identity=predecessor_turn_identity,
        source_selection_basis=source_selection_basis,
        operative_surfaces=operative_surfaces,
        operative_surface_evidence={
            key: tuple(values)
            for key, values in sorted(operative_surface_evidence.items())
        },
        layout_variant_notes=tuple(layout_variant_notes),
        turn_reading=turn_reading,
        lineage_notes=tuple(lineage_notes),
        unreadable_notes=tuple(unreadable_notes),
    )


def _has_ordinary_material(execution_run_dir: Path) -> bool:
    for key, names in _LAYER_DIR_CANDIDATES.items():
        if key in {"source_notes", "execution_relation"}:
            continue
        if any((execution_run_dir / name).exists() for name in names):
            return True
    return False


def _discover_layer_dir(run_root: Path, key: str) -> Tuple[Optional[Path], Tuple[str, ...]]:
    preferred_name = _PREFERRED_LAYER_DIRS[key]

    for candidate_name in _LAYER_DIR_CANDIDATES[key]:
        candidate = run_root / candidate_name
        if candidate.is_dir():
            if candidate_name == preferred_name:
                return candidate, ()
            return (
                candidate,
                (
                    f"Local layout variant uses '{candidate_name}' for {key.replace('_', ' ')} material.",
                ),
            )

    return None, ()


def _discover_singleton_json(layer_dir: Optional[Path], preferred_filename: str) -> Optional[Path]:
    if layer_dir is None:
        return None

    preferred = layer_dir / preferred_filename
    if preferred.is_file():
        return preferred

    candidates = sorted(path for path in layer_dir.glob("*.json") if path.is_file())
    if candidates:
        return candidates[0]
    return None


def _collect_json_paths(layer_dir: Optional[Path]) -> Dict[str, Path]:
    if layer_dir is None:
        return {}

    return {
        path.relative_to(layer_dir).as_posix(): path
        for path in sorted(layer_dir.rglob("*.json"))
        if path.is_file()
    }


def _read_json_file(path: Optional[Path]) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
    if path is None:
        return None, None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return None, f"Failed to read JSON at {_repo_relative(path)}: {exc}"

    if not isinstance(data, dict):
        return None, f"JSON at {_repo_relative(path)} is not an object."

    return data, None


def _read_json_map(
    discovered_paths: Mapping[str, Path],
) -> Tuple[Dict[str, Dict[str, Any]], Tuple[str, ...]]:
    readable: Dict[str, Dict[str, Any]] = {}
    errors: List[str] = []

    for key, path in sorted(discovered_paths.items()):
        data, error = _read_json_file(path)
        if error is not None:
            errors.append(error)
            continue
        if data is not None:
            readable[key] = data

    return readable, tuple(errors)


def _read_execution_identity(
    run_root: Path,
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
) -> Optional[str]:
    for container in (summary_data, manifest_data):
        if not container:
            continue
        execution_identity = _as_string(container.get("execution_identity"))
        if execution_identity:
            return execution_identity

    for path_candidate in (run_root, run_root.parent):
        if path_candidate.name.startswith("execution-"):
            return path_candidate.name
    return None


def _read_matter_ref(
    *,
    line_name: str,
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
    canonical_body_records: Mapping[str, Mapping[str, Any]],
    source_note_records: Mapping[str, Mapping[str, Any]],
) -> Optional[str]:
    for container in (summary_data, manifest_data):
        if not container:
            continue
        matter_identity = _as_string(container.get("matter_identity"))
        if matter_identity:
            return matter_identity

    if summary_data and line_name == LINE_CONTINUITY:
        for key in ("anchor_source_used", "predecessor_source_used"):
            value = summary_data.get(key)
            if isinstance(value, Mapping):
                matter_ref = _as_string(value.get("matter_ref"))
                if matter_ref:
                    return matter_ref

    for source_note in source_note_records.values():
        matter_ref = _read_source_note_matter_ref(source_note)
        if matter_ref:
            return matter_ref

    for body in canonical_body_records.values():
        for field in ("matter_ref", "target_ref"):
            matter_ref = _as_string(body.get(field))
            if matter_ref:
                return matter_ref

    return None


def _read_anchor_source_run_ref(
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
    source_note_records: Mapping[str, Mapping[str, Any]],
) -> Optional[str]:
    if summary_data:
        anchor = summary_data.get("anchor_source_used")
        if isinstance(anchor, Mapping):
            selected_run_directory = _as_string(anchor.get("selected_run_directory"))
            if selected_run_directory:
                return selected_run_directory

    if manifest_data:
        anchor_source_run_ref = _as_string(manifest_data.get("anchor_source_run_ref"))
        if anchor_source_run_ref:
            return anchor_source_run_ref

    for source_note in source_note_records.values():
        source_role = _as_string(source_note.get("source_role"))
        source_type = _as_string(source_note.get("anchor_source_type"))
        if source_role == "ordinary_anchor_source" or source_type == "ordinary_proof_slice_anchor":
            run_ref = _read_source_note_run_ref(source_note)
            if run_ref:
                return run_ref

    return None


def _read_predecessor_source_run_ref(
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
    source_note_records: Mapping[str, Mapping[str, Any]],
) -> Optional[str]:
    if summary_data:
        predecessor = summary_data.get("predecessor_source_used")
        if isinstance(predecessor, Mapping):
            selected_run_directory = _as_string(predecessor.get("selected_run_directory"))
            if selected_run_directory:
                return selected_run_directory

    if manifest_data:
        predecessor_source_run_ref = _as_string(
            manifest_data.get("predecessor_source_run_ref")
        )
        if predecessor_source_run_ref:
            return predecessor_source_run_ref

    for source_note in source_note_records.values():
        source_role = _as_string(source_note.get("source_role"))
        if source_role == "continuity_predecessor_source":
            run_ref = _read_source_note_run_ref(source_note)
            if run_ref:
                return run_ref

    return None


def _read_predecessor_turn_identity(
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
    source_note_records: Mapping[str, Mapping[str, Any]],
    canonical_body_records: Mapping[str, Mapping[str, Any]],
) -> Optional[str]:
    if summary_data:
        predecessor = summary_data.get("predecessor_source_used")
        if isinstance(predecessor, Mapping):
            predecessor_turn_identity = _as_string(predecessor.get("predecessor_turn_identity"))
            if predecessor_turn_identity:
                return predecessor_turn_identity

    if manifest_data:
        predecessor_turn_identity = _as_string(manifest_data.get("predecessor_turn_ref"))
        if predecessor_turn_identity:
            return predecessor_turn_identity

    for source_note in source_note_records.values():
        selected_source = source_note.get("selected_source")
        if isinstance(selected_source, Mapping):
            predecessor_turn_identity = _as_string(
                selected_source.get("predecessor_turn_identity")
            )
            if predecessor_turn_identity:
                return predecessor_turn_identity

    for body in canonical_body_records.values():
        predecessor_turn_ref = _as_string(body.get("predecessor_turn_ref"))
        if predecessor_turn_ref:
            return predecessor_turn_ref

    return None


def _read_source_selection_basis(
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
) -> Optional[str]:
    for container in (summary_data, manifest_data):
        if not container:
            continue
        source_selection = container.get("source_selection")
        if isinstance(source_selection, Mapping):
            selection_basis = _as_string(source_selection.get("selection_basis"))
            if selection_basis:
                return selection_basis
    return None


def _read_source_note_run_ref(source_note: Mapping[str, Any]) -> Optional[str]:
    selected_run_directory = _as_string(source_note.get("selected_run_directory"))
    if selected_run_directory:
        return selected_run_directory

    selected_source = source_note.get("selected_source")
    if isinstance(selected_source, Mapping):
        run_directory = _as_string(selected_source.get("run_directory"))
        if run_directory:
            return run_directory

    return None


def _read_source_note_matter_ref(source_note: Mapping[str, Any]) -> Optional[str]:
    matter_ref = _as_string(source_note.get("matter_ref"))
    if matter_ref:
        return matter_ref

    selected_source = source_note.get("selected_source")
    if isinstance(selected_source, Mapping):
        nested_matter_ref = _as_string(selected_source.get("matter_ref"))
        if nested_matter_ref:
            return nested_matter_ref

    return None


def _infer_operative_surfaces(
    *,
    line_name: str,
    turn_kind: Optional[str],
    turn_rank: Optional[int],
    summary_type: Optional[str],
    summary_data: Optional[Mapping[str, Any]],
    manifest_data: Optional[Mapping[str, Any]],
    conformance_records: Mapping[str, Mapping[str, Any]],
    source_note_records: Mapping[str, Mapping[str, Any]],
) -> Dict[str, List[str]]:
    evidence: Dict[str, List[str]] = {}

    if summary_data and isinstance(summary_data.get("preservation_layout"), Mapping):
        _add_surface_evidence(
            evidence,
            SURFACE_SHARED_PRESERVATION_LAYOUT,
            "Run summary carries explicit preservation_layout material.",
        )
    if manifest_data and (
        _as_string(manifest_data.get("layout_kind"))
        or _as_string(manifest_data.get("naming_posture"))
        or isinstance(manifest_data.get("layer_roots"), Mapping)
        or isinstance(manifest_data.get("written_by_layer"), Mapping)
    ):
        _add_surface_evidence(
            evidence,
            SURFACE_SHARED_PRESERVATION_LAYOUT,
            "Manifest preserves shared layout fields such as layout_kind, naming_posture, layer_roots, or written_by_layer.",
        )

    if any("conformance_kind" in record for record in conformance_records.values()):
        _add_surface_evidence(
            evidence,
            SURFACE_SHARED_CONFORMANCE,
            "Conformance outputs expose conformance_kind, which is the shared conformance result shape.",
        )

    if line_name == LINE_CONTINUITY:
        if summary_data and isinstance(summary_data.get("source_selection"), Mapping):
            _add_surface_evidence(
                evidence,
                SURFACE_SHARED_SOURCE_SELECTION,
                "Continuity summary carries explicit source_selection material.",
            )
        if manifest_data and isinstance(manifest_data.get("source_selection"), Mapping):
            _add_surface_evidence(
                evidence,
                SURFACE_SHARED_SOURCE_SELECTION,
                "Continuity manifest carries structured source_selection material.",
            )
        if any(
            _as_string(record.get("source_note_type")) == "selected_source_record"
            for record in source_note_records.values()
        ):
            _add_surface_evidence(
                evidence,
                SURFACE_SHARED_SOURCE_SELECTION,
                "Source-note material uses selected_source_record structure.",
            )

    if manifest_data and _as_string(manifest_data.get("manifest_identity")):
        _add_surface_evidence(
            evidence,
            SURFACE_SHARED_IDENTIFIER_GENERATION,
            "Manifest carries explicit manifest_identity.",
        )

    for surface_name, message in _surface_hints_from_turn(
        turn_kind=turn_kind,
        turn_rank=turn_rank,
        summary_type=summary_type,
    ):
        _add_surface_evidence(evidence, surface_name, message)

    return evidence


def _surface_hints_from_turn(
    *,
    turn_kind: Optional[str],
    turn_rank: Optional[int],
    summary_type: Optional[str],
) -> Tuple[Tuple[str, str], ...]:
    if turn_kind is None or turn_rank is None or summary_type is None:
        return ()

    hints: List[Tuple[str, str]] = []
    stage_message = (
        f"Summary type {summary_type} marks the preserved additive runner stage where "
        "this shared surface is operative."
    )

    if turn_kind == "ordinary_proof_slice":
        if turn_rank >= 2:
            hints.append((SURFACE_SHARED_PRESERVATION_LAYOUT, stage_message))
        if turn_rank >= 3:
            hints.append((SURFACE_SHARED_CONFORMANCE, stage_message))
        if turn_rank >= 4:
            hints.append((SURFACE_SHARED_IDENTIFIER_GENERATION, stage_message))

    if turn_kind == "continuity_proof_slice":
        if turn_rank >= 3:
            hints.append((SURFACE_SHARED_SOURCE_SELECTION, stage_message))
        if turn_rank >= 4:
            hints.append((SURFACE_SHARED_PRESERVATION_LAYOUT, stage_message))
        if turn_rank >= 5:
            hints.append((SURFACE_SHARED_CONFORMANCE, stage_message))
        if turn_rank >= 6:
            hints.append((SURFACE_SHARED_IDENTIFIER_GENERATION, stage_message))

    return tuple(hints)


def _add_surface_evidence(
    evidence: Dict[str, List[str]],
    surface_name: str,
    message: str,
) -> None:
    messages = evidence.setdefault(surface_name, [])
    if message not in messages:
        messages.append(message)


def _build_lineage_notes(
    *,
    line_name: str,
    summary_type: Optional[str],
    turn_kind: Optional[str],
    turn_label: Optional[str],
    operative_surfaces: Sequence[str],
    layout_variant_notes: Sequence[str],
) -> List[str]:
    notes: List[str] = []

    if summary_type and turn_kind and turn_label:
        notes.append(
            f"Preserved summary type {summary_type} makes this run readable as the {turn_label} {line_name} proof-slice turn."
        )
    elif summary_type:
        notes.append(f"Preserved summary type {summary_type} contributes turn readability.")

    if line_name == LINE_ORDINARY and {
        SURFACE_SHARED_PRESERVATION_LAYOUT,
        SURFACE_SHARED_CONFORMANCE,
        SURFACE_SHARED_IDENTIFIER_GENERATION,
    }.issubset(operative_surfaces):
        notes.append(
            "This ordinary run reads as a shared-implementation threshold turn on the ordinary line."
        )

    if line_name == LINE_CONTINUITY and {
        SURFACE_SHARED_SOURCE_SELECTION,
        SURFACE_SHARED_PRESERVATION_LAYOUT,
        SURFACE_SHARED_CONFORMANCE,
        SURFACE_SHARED_IDENTIFIER_GENERATION,
    }.issubset(operative_surfaces):
        notes.append(
            "This continuity run reads as a shared-implementation threshold turn on the continuity line."
        )

    if layout_variant_notes:
        notes.append(
            "Local layout variation remains readable as lineage rather than as contradiction."
        )

    return notes


def _build_turn_reading(
    *,
    line_name: str,
    turn_kind: Optional[str],
    turn_label: Optional[str],
    operative_surfaces: Sequence[str],
) -> Optional[str]:
    if turn_kind == "ordinary_proof_slice" and turn_label:
        if SURFACE_SHARED_IDENTIFIER_GENERATION in operative_surfaces:
            return f"{turn_label.capitalize()} ordinary proof-slice turn with shared identifier generation operative."
        if SURFACE_SHARED_CONFORMANCE in operative_surfaces:
            return f"{turn_label.capitalize()} ordinary proof-slice turn with shared conformance operative."
        if SURFACE_SHARED_PRESERVATION_LAYOUT in operative_surfaces:
            return f"{turn_label.capitalize()} ordinary proof-slice turn with shared preservation layout operative."
        return f"{turn_label.capitalize()} ordinary proof-slice turn."

    if turn_kind == "continuity_proof_slice" and turn_label:
        if SURFACE_SHARED_IDENTIFIER_GENERATION in operative_surfaces:
            return f"{turn_label.capitalize()} continuity proof-slice turn with shared identifier generation operative."
        if SURFACE_SHARED_CONFORMANCE in operative_surfaces:
            return f"{turn_label.capitalize()} continuity proof-slice turn with shared conformance operative."
        if SURFACE_SHARED_PRESERVATION_LAYOUT in operative_surfaces:
            return f"{turn_label.capitalize()} continuity proof-slice turn with shared preservation layout operative."
        if SURFACE_SHARED_SOURCE_SELECTION in operative_surfaces:
            return f"{turn_label.capitalize()} continuity proof-slice turn with shared source selection operative."
        return f"{turn_label.capitalize()} continuity proof-slice turn."

    if line_name == LINE_ORDINARY:
        return "Ordinary preserved run."
    if line_name == LINE_CONTINUITY:
        return "Continuity preserved run."
    return None


def _build_snapshot_notes(
    ordinary_runs: Sequence[RunRecord],
    continuity_runs: Sequence[RunRecord],
    unknown_runs: Sequence[RunRecord],
) -> Tuple[str, ...]:
    notes: List[str] = []

    if any(record.layout_variant_notes for record in (*ordinary_runs, *continuity_runs)):
        notes.append(
            "Preserved runs include implementation-local naming variation such as canonical_bodies/canonical_body, envelopes/envelope, fixtures/fixture_outputs, summary/run_summary, and anchor_source/source_notes. These are read as lineage variation, not architectural contradiction."
        )

    if ordinary_runs and continuity_runs:
        notes.append(
            "The preserved archive now carries both an ordinary line and a continuity line. They remain grouped separately rather than flattened into one generic run list."
        )

    if any(
        "shared-implementation threshold turn on the ordinary line."
        in record.lineage_notes
        for record in ordinary_runs
    ):
        notes.append(
            "The ordinary line includes a preserved threshold turn where shared preservation layout, shared conformance, and shared identifier generation are all operative."
        )

    if any(
        "shared-implementation threshold turn on the continuity line."
        in record.lineage_notes
        for record in continuity_runs
    ):
        notes.append(
            "The continuity line includes a preserved threshold turn where shared source selection, shared preservation layout, shared conformance, and shared identifier generation are all operative."
        )

    if unknown_runs:
        notes.append(
            "Some preserved directories remain only partially readable. They are preserved as unknown lineage material rather than silently hidden."
        )

    return tuple(notes)


def _parse_turn_identity(
    summary_type: Optional[str],
) -> Tuple[Optional[str], Optional[int], Optional[str]]:
    if (
        not summary_type
        or not summary_type.startswith("v1_")
        or not summary_type.endswith("_summary")
    ):
        return None, None, None

    middle = summary_type[len("v1_") : -len("_summary")]
    for label, rank in _TURN_LABELS.items():
        prefix = f"{label}_"
        if middle.startswith(prefix):
            remainder = middle[len(prefix) :]
            if remainder == "proof_slice":
                return "ordinary_proof_slice", rank, label
            if remainder == "continuity_proof_slice":
                return "continuity_proof_slice", rank, label
            return remainder, rank, label

    return None, None, None


def _resolve_run_path(run_path: str | Path, runs_dir: Path) -> Path:
    candidate = Path(run_path)
    if candidate.is_absolute():
        return candidate.resolve()

    if (runs_dir / candidate).exists():
        return (runs_dir / candidate).resolve()
    return (REPO_ROOT / candidate).resolve()


def _sort_run_records(records: Iterable[RunRecord]) -> List[RunRecord]:
    line_order = {LINE_ORDINARY: 0, LINE_CONTINUITY: 1, LINE_UNKNOWN: 2}
    return sorted(
        records,
        key=lambda record: (
            line_order.get(record.line_name, 9),
            record.turn_rank if record.turn_rank is not None else 999,
            record.execution_identity or "",
            _repo_relative(record.run_directory),
        ),
    )


def _record_paths(discovered_paths: Mapping[str, Path]) -> Dict[str, str]:
    return {key: _repo_relative(path) for key, path in sorted(discovered_paths.items())}


def _as_string(value: Any) -> Optional[str]:
    if isinstance(value, str) and value.strip():
        return value
    return None


def _repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = list(argv or sys.argv[1:])
    runs_dir = RUNS_DIR if not args else Path(args[0])
    snapshot = build_inventory_snapshot(runs_dir)

    print(f"Runs directory: {_repo_relative(snapshot.runs_dir)}")
    print(f"Ordinary runs: {len(snapshot.ordinary_runs)}")
    for record in snapshot.ordinary_runs:
        print(
            f"  - {_repo_relative(record.run_directory)}"
            f" [{record.summary_type or 'no-summary'}]"
        )
    print(f"Continuity runs: {len(snapshot.continuity_runs)}")
    for record in snapshot.continuity_runs:
        print(
            f"  - {_repo_relative(record.run_directory)}"
            f" [{record.summary_type or 'no-summary'}]"
        )
    print(f"Unknown runs: {len(snapshot.unknown_runs)}")
    return 0


__all__ = [
    "InventorySnapshot",
    "RUNS_DIR",
    "RunRecord",
    "SURFACE_SHARED_CONFORMANCE",
    "SURFACE_SHARED_IDENTIFIER_GENERATION",
    "SURFACE_SHARED_PRESERVATION_LAYOUT",
    "SURFACE_SHARED_SOURCE_SELECTION",
    "build_inventory_snapshot",
    "discover_continuity_runs",
    "discover_ordinary_runs",
    "discover_runs",
    "read_run_record",
]


if __name__ == "__main__":  # pragma: no cover - optional local readability path
    raise SystemExit(main())
