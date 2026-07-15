#!/usr/bin/env python3
"""
Bounded v1 runner for the second continuity proof slice.

This script forms one successor continuity turn body anchored to preserved
ordinary v1 canonical artifacts and explicitly linked to a prior lawful
continuity turn. It validates the canonical continuity body against the v1
continuity schema, preserves an explicit execution-relation surface, and writes
the result in a small local layout under
v1/registry/runs/<execution-identity>/continuity/.
"""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, MutableMapping, Optional, Sequence, Tuple
from uuid import uuid4


REPO_ROOT = Path(__file__).resolve().parents[3]
V1_DIR = REPO_ROOT / "v1"
SCHEMA_PATH = V1_DIR / "schemas" / "continuity_turn.schema.json"
RUNS_DIR = V1_DIR / "registry" / "runs"

ORDINARY_BODY_FILES: Dict[str, str] = {
    "validation_ref": "validation_artifact.body.json",
    "witness_ref": "witness_artifact.body.json",
    "governance_action_ref": "governance_action.body.json",
    "transition_ref": "transition_record.body.json",
    "state_ref": "state_record.body.json",
}

ORDINARY_ID_FIELDS: Dict[str, str] = {
    "validation_ref": "validation_id",
    "witness_ref": "witness_id",
    "governance_action_ref": "governance_action_id",
    "transition_ref": "transition_id",
    "state_ref": "state_id",
}


@dataclass(frozen=True)
class AnchorSource:
    run_dir: Path
    summary_path: Optional[Path]
    matter_ref: str
    anchor_body_paths: Dict[str, Path]
    anchor_refs: Dict[str, str]


@dataclass(frozen=True)
class PredecessorSource:
    run_dir: Path
    continuity_dir: Path
    summary_path: Optional[Path]
    body_path: Path
    body: Dict[str, Any]
    conformance_path: Path
    anchor_note_path: Path
    turn_id: str
    matter_ref: str
    anchor_source_run_ref: str


class MissingJsonSchemaDependency(RuntimeError):
    """Raised when jsonschema is unavailable for the continuity proof slice."""


class AnchorSourceNotFound(RuntimeError):
    """Raised when no ordinary proof-slice anchor source is available."""


class PredecessorSourceNotFound(RuntimeError):
    """Raised when no prior positive continuity source is available."""


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def generate_identity(prefix: str) -> str:
    return f"{prefix}-{uuid4().hex}"


def write_json(path: Path, payload: Mapping[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def read_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def first_existing_path(paths: Sequence[Path]) -> Optional[Path]:
    for path in paths:
        if path.is_file():
            return path
    return None


def load_validator_tools() -> Tuple[Any, Any]:
    try:
        from jsonschema import FormatChecker
        from jsonschema.validators import validator_for
    except ImportError as exc:  # pragma: no cover - dependency posture only
        raise MissingJsonSchemaDependency(
            "This runner requires the 'jsonschema' package. "
            "Install it with 'python -m pip install jsonschema' and rerun."
        ) from exc

    return validator_for, FormatChecker


def load_continuity_validator() -> Dict[str, Any]:
    validator_for, format_checker_class = load_validator_tools()
    schema = read_json(SCHEMA_PATH)
    validator_class = validator_for(schema)
    validator_class.check_schema(schema)
    return {
        "schema": schema,
        "schema_path": SCHEMA_PATH,
        "validator": validator_class(schema, format_checker=format_checker_class()),
    }


def record_written(
    written_files: MutableMapping[str, List[str]],
    category: str,
    path: Path,
) -> None:
    written_files.setdefault(category, []).append(repo_relative(path))


def collect_all_written_files(written_files: Mapping[str, List[str]]) -> List[str]:
    flattened: List[str] = []
    for paths in written_files.values():
        flattened.extend(paths)
    return sorted(flattened)


def candidate_run_dirs() -> List[Path]:
    if not RUNS_DIR.exists():
        return []

    candidates = [path for path in RUNS_DIR.iterdir() if path.is_dir()]
    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)


def candidate_continuity_dirs() -> List[Path]:
    continuity_dirs: List[Path] = []
    for run_dir in candidate_run_dirs():
        continuity_dir = run_dir / "continuity"
        if continuity_dir.is_dir():
            continuity_dirs.append(continuity_dir)
    return continuity_dirs


def resolve_anchor_matter(ordinary_bodies: Mapping[str, Dict[str, Any]]) -> Optional[str]:
    candidates = {
        ordinary_bodies["validation_ref"].get("target_ref"),
        ordinary_bodies["witness_ref"].get("target_ref"),
        ordinary_bodies["governance_action_ref"].get("matter_ref"),
        ordinary_bodies["transition_ref"].get("matter_ref"),
        ordinary_bodies["state_ref"].get("matter_ref"),
    }
    normalized = {
        candidate.strip()
        for candidate in candidates
        if isinstance(candidate, str) and candidate.strip()
    }
    if len(normalized) != 1:
        return None
    return normalized.pop()


def load_anchor_source_from_run(run_dir: Path) -> Optional[AnchorSource]:
    canonical_bodies_dir = run_dir / "canonical_bodies"
    if not canonical_bodies_dir.is_dir():
        return None

    body_paths = {
        ref_name: canonical_bodies_dir / filename
        for ref_name, filename in ORDINARY_BODY_FILES.items()
    }
    if not all(path.is_file() for path in body_paths.values()):
        return None

    try:
        ordinary_bodies = {
            ref_name: read_json(path)
            for ref_name, path in body_paths.items()
        }
    except (OSError, json.JSONDecodeError):
        return None

    matter_ref = resolve_anchor_matter(ordinary_bodies)
    if not matter_ref:
        return None

    anchor_refs: Dict[str, str] = {}
    for ref_name, id_field in ORDINARY_ID_FIELDS.items():
        anchor_value = ordinary_bodies[ref_name].get(id_field)
        if not isinstance(anchor_value, str) or not anchor_value.strip():
            return None
        anchor_refs[ref_name] = anchor_value.strip()

    summary_path = first_existing_path(
        [
            run_dir / "summary" / "run_summary.json",
            run_dir / "run_summary" / "run_summary.json",
        ]
    )
    return AnchorSource(
        run_dir=run_dir,
        summary_path=summary_path,
        matter_ref=matter_ref,
        anchor_body_paths=body_paths,
        anchor_refs=anchor_refs,
    )


def find_anchor_sources() -> Dict[str, AnchorSource]:
    anchor_sources: Dict[str, AnchorSource] = {}
    for run_dir in candidate_run_dirs():
        anchor_source = load_anchor_source_from_run(run_dir)
        if anchor_source is not None:
            anchor_sources[repo_relative(anchor_source.run_dir)] = anchor_source
    return anchor_sources


def continuity_body_has_matching_anchor(
    body: Mapping[str, Any],
    anchor_source: AnchorSource,
) -> bool:
    return any(
        isinstance(body.get(ref_name), str)
        and body.get(ref_name) == anchor_value
        for ref_name, anchor_value in anchor_source.anchor_refs.items()
    )


def load_predecessor_source_from_continuity_dir(
    continuity_dir: Path,
    anchor_sources: Mapping[str, AnchorSource],
) -> Optional[Tuple[PredecessorSource, AnchorSource]]:
    body_path = continuity_dir / "canonical_body" / "positive" / "continuity_turn.body.json"
    conformance_path = continuity_dir / "conformance" / "body" / "positive" / "continuity_turn.json"
    summary_path = first_existing_path(
        [
            continuity_dir / "summary" / "run_summary.json",
            continuity_dir / "run_summary" / "run_summary.json",
        ]
    )
    anchor_note_path = first_existing_path(
        [
            continuity_dir / "source_notes" / "anchor_source_note.json",
            continuity_dir / "anchor_source" / "anchor_source_note.json",
        ]
    )

    if not body_path.is_file() or not conformance_path.is_file() or anchor_note_path is None:
        return None

    try:
        body = read_json(body_path)
        conformance = read_json(conformance_path)
        anchor_note = read_json(anchor_note_path)
    except (OSError, json.JSONDecodeError):
        return None

    if conformance.get("status") != "pass":
        return None

    turn_id = body.get("turn_id")
    matter_ref = body.get("matter_ref")
    selected_run_directory = anchor_note.get("selected_run_directory")

    if not isinstance(turn_id, str) or not turn_id.strip():
        return None
    if not isinstance(matter_ref, str) or not matter_ref.strip():
        return None
    if not isinstance(selected_run_directory, str) or not selected_run_directory.strip():
        return None

    anchor_source = anchor_sources.get(selected_run_directory.strip())
    if anchor_source is None:
        return None

    if matter_ref.strip() != anchor_source.matter_ref:
        return None
    if not continuity_body_has_matching_anchor(body, anchor_source):
        return None

    predecessor_source = PredecessorSource(
        run_dir=continuity_dir.parent,
        continuity_dir=continuity_dir,
        summary_path=summary_path,
        body_path=body_path,
        body=dict(body),
        conformance_path=conformance_path,
        anchor_note_path=anchor_note_path,
        turn_id=turn_id.strip(),
        matter_ref=matter_ref.strip(),
        anchor_source_run_ref=repo_relative(anchor_source.run_dir),
    )
    return predecessor_source, anchor_source


def find_predecessor_source(
    anchor_sources: Mapping[str, AnchorSource],
) -> Tuple[PredecessorSource, AnchorSource]:
    for continuity_dir in candidate_continuity_dirs():
        loaded = load_predecessor_source_from_continuity_dir(continuity_dir, anchor_sources)
        if loaded is not None:
            return loaded

    raise PredecessorSourceNotFound(
        "No suitable positive continuity predecessor run was found under "
        "v1/registry/runs/. Run "
        "'python3 v1/embodiment/run/run_first_continuity_proof_slice.py' "
        "successfully first, then rerun this successor continuity proof slice."
    )


def build_positive_continuity_body(
    turn_id: str,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
    recorded_at: str,
) -> Dict[str, Any]:
    body = {
        "turn_id": turn_id,
        "matter_ref": anchor_source.matter_ref,
        "recorded_at": recorded_at,
        "predecessor_turn_ref": predecessor_source.turn_id,
    }
    body.update(anchor_source.anchor_refs)
    return body


def build_negative_successor_without_anchor_fixture(
    matter_ref: str,
    predecessor_turn_ref: str,
    recorded_at: str,
) -> Dict[str, Any]:
    return {
        "turn_id": generate_identity("continuity-turn"),
        "matter_ref": matter_ref,
        "recorded_at": recorded_at,
        "predecessor_turn_ref": predecessor_turn_ref,
    }


def validate_body(
    body: Mapping[str, Any],
    body_path: Path,
    schema_entry: Mapping[str, Any],
    fixture_classification: str,
    expected_status: str,
) -> Dict[str, Any]:
    validator = schema_entry["validator"]
    schema_path: Path = schema_entry["schema_path"]
    errors = sorted(validator.iter_errors(body), key=lambda error: list(error.path))
    error_items = [
        {
            "message": error.message,
            "validator": error.validator,
            "instance_path": list(error.path),
            "schema_path": list(error.schema_path),
        }
        for error in errors
    ]
    status = "pass" if not error_items else "fail"

    return {
        "surface": "continuity_body_conformance",
        "artifact_family": "continuity_turn",
        "fixture_classification": fixture_classification,
        "expected_status": expected_status,
        "status": status,
        "matched_expectation": status == expected_status,
        "checked_at": utc_now(),
        "schema_ref": repo_relative(schema_path),
        "body_ref": repo_relative(body_path),
        "errors": error_items,
    }


def build_execution_relation(
    execution_relation_id: str,
    execution_id: str,
    continuity_turn_id: str,
    continuity_body_ref: str,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
    recorded_at: str,
) -> Dict[str, Any]:
    return {
        "execution_relation_id": execution_relation_id,
        "relation_type": "continuity_execution_relation",
        "execution_identity": execution_id,
        "continuity_turn_identity": continuity_turn_id,
        "continuity_body_ref": continuity_body_ref,
        "anchor_source_run_ref": repo_relative(anchor_source.run_dir),
        "predecessor_source_run_ref": repo_relative(predecessor_source.run_dir),
        "predecessor_turn_ref": predecessor_source.turn_id,
        "recorded_at": recorded_at,
    }


def validate_execution_relation(
    execution_relation: Mapping[str, Any],
    execution_relation_path: Path,
    execution_id: str,
    continuity_turn_id: str,
    continuity_body_ref: str,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
) -> Dict[str, Any]:
    errors: List[Dict[str, Any]] = []

    if execution_relation.get("relation_type") != "continuity_execution_relation":
        errors.append({"message": "Execution relation type is missing or incorrect."})
    if execution_relation.get("execution_identity") != execution_id:
        errors.append({"message": "Execution relation does not preserve the current execution identity."})
    if execution_relation.get("continuity_turn_identity") != continuity_turn_id:
        errors.append({"message": "Execution relation does not point to the continuity turn identity."})
    if execution_relation.get("continuity_body_ref") != continuity_body_ref:
        errors.append({"message": "Execution relation does not point to the preserved continuity body."})
    if execution_relation.get("anchor_source_run_ref") != repo_relative(anchor_source.run_dir):
        errors.append({"message": "Execution relation does not preserve the selected ordinary anchor run."})
    if execution_relation.get("predecessor_source_run_ref") != repo_relative(predecessor_source.run_dir):
        errors.append({"message": "Execution relation does not preserve the selected predecessor continuity run."})
    if execution_relation.get("predecessor_turn_ref") != predecessor_source.turn_id:
        errors.append({"message": "Execution relation does not preserve the selected predecessor continuity turn."})
    if "body" in execution_relation or "continuity_body" in execution_relation:
        errors.append({"message": "Execution relation must not embed the continuity body inline."})

    return {
        "surface": "execution_relation_conformance",
        "artifact_family": "continuity_turn",
        "status": "pass" if not errors else "fail",
        "checked_at": utc_now(),
        "execution_relation_ref": repo_relative(execution_relation_path),
        "continuity_body_ref": continuity_body_ref,
        "anchor_source_run_ref": repo_relative(anchor_source.run_dir),
        "predecessor_source_run_ref": repo_relative(predecessor_source.run_dir),
        "errors": errors,
    }


def build_anchor_source_note(
    note_id: str,
    anchor_source: AnchorSource,
) -> Dict[str, Any]:
    return {
        "source_note_id": note_id,
        "source_type": "ordinary_proof_slice_anchor",
        "selected_run_directory": repo_relative(anchor_source.run_dir),
        "selected_summary_ref": (
            repo_relative(anchor_source.summary_path)
            if anchor_source.summary_path is not None
            else None
        ),
        "matter_ref": anchor_source.matter_ref,
        "anchor_body_refs": {
            ref_name: repo_relative(path)
            for ref_name, path in anchor_source.anchor_body_paths.items()
        },
        "anchor_identity_refs": dict(anchor_source.anchor_refs),
        "recorded_at": utc_now(),
    }


def build_predecessor_source_note(
    note_id: str,
    predecessor_source: PredecessorSource,
) -> Dict[str, Any]:
    predecessor_of_predecessor = predecessor_source.body.get("predecessor_turn_ref")
    return {
        "source_note_id": note_id,
        "source_type": "continuity_predecessor",
        "selected_run_directory": repo_relative(predecessor_source.run_dir),
        "selected_continuity_directory": repo_relative(predecessor_source.continuity_dir),
        "selected_summary_ref": (
            repo_relative(predecessor_source.summary_path)
            if predecessor_source.summary_path is not None
            else None
        ),
        "selected_body_ref": repo_relative(predecessor_source.body_path),
        "selected_conformance_ref": repo_relative(predecessor_source.conformance_path),
        "selected_anchor_source_note_ref": repo_relative(predecessor_source.anchor_note_path),
        "predecessor_turn_identity": predecessor_source.turn_id,
        "matter_ref": predecessor_source.matter_ref,
        "anchor_source_run_ref": predecessor_source.anchor_source_run_ref,
        "predecessor_of_predecessor_ref": (
            predecessor_of_predecessor
            if isinstance(predecessor_of_predecessor, str) and predecessor_of_predecessor.strip()
            else None
        ),
        "recorded_at": utc_now(),
    }


def evaluate_preservation_conformance(
    continuity_dir: Path,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
    written_files: Mapping[str, List[str]],
) -> Dict[str, Any]:
    checks: List[Dict[str, Any]] = []

    def add_check(name: str, condition: bool, message: str) -> None:
        checks.append(
            {
                "name": name,
                "status": "pass" if condition else "fail",
                "message": message,
            }
        )

    all_files = collect_all_written_files(written_files)
    add_check(
        "written_files_exist",
        all((REPO_ROOT / relative_path).exists() for relative_path in all_files),
        "All preserved continuity files recorded before preservation conformance must exist.",
    )
    add_check(
        "continuity_body_separate_from_execution_relation",
        bool(written_files.get("continuity_body")) and bool(written_files.get("execution_relation")),
        "Continuity body and explicit execution relation must both be preserved separately.",
    )
    add_check(
        "negative_fixture_separated",
        bool(written_files.get("negative_fixtures"))
        and all("/fixture_outputs/negative/" in path for path in written_files.get("negative_fixtures", [])),
        "Negative successor-continuity fixture material must remain under an explicitly separate negative fixture branch.",
    )
    add_check(
        "source_notes_present",
        len(written_files.get("source_notes", [])) >= 2,
        "Preserved source notes for both ordinary anchor source and predecessor continuity source must remain readable.",
    )
    add_check(
        "anchor_source_still_exists",
        anchor_source.run_dir.is_dir()
        and all(path.is_file() for path in anchor_source.anchor_body_paths.values()),
        "The selected ordinary proof-slice anchor source and its canonical bodies must remain available.",
    )
    add_check(
        "predecessor_source_still_exists",
        predecessor_source.continuity_dir.is_dir()
        and predecessor_source.body_path.is_file()
        and predecessor_source.conformance_path.is_file(),
        "The selected predecessor continuity source and its positive continuity body must remain available.",
    )
    add_check(
        "continuity_directory_bounded_to_v1_registry",
        continuity_dir.name == "continuity" and continuity_dir.parent.parent == RUNS_DIR,
        "The local continuity preservation surface must remain bounded to v1/registry/runs/<execution-identity>/continuity/.",
    )

    errors = [check for check in checks if check["status"] == "fail"]
    return {
        "surface": "continuity_preservation_conformance",
        "status": "pass" if not errors else "fail",
        "checked_at": utc_now(),
        "continuity_run_directory": repo_relative(continuity_dir),
        "checks": checks,
    }


def build_run_summary(
    execution_id: str,
    continuity_turn_id: str,
    continuity_dir: Path,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
    positive_body_result: Mapping[str, Any],
    execution_relation_result: Mapping[str, Any],
    negative_result: Mapping[str, Any],
    fixture_classification_ref: str,
    anchor_source_note_ref: str,
    predecessor_source_note_ref: str,
    preservation_result_ref: str,
    preservation_status: str,
) -> Dict[str, Any]:
    return {
        "summary_type": "v1_second_continuity_proof_slice_summary",
        "execution_identity": execution_id,
        "continuity_turn_identity": continuity_turn_id,
        "continuity_run_directory": repo_relative(continuity_dir),
        "anchor_source_used": {
            "selected_run_directory": repo_relative(anchor_source.run_dir),
            "selected_summary_ref": (
                repo_relative(anchor_source.summary_path)
                if anchor_source.summary_path is not None
                else None
            ),
            "source_note_ref": anchor_source_note_ref,
        },
        "predecessor_source_used": {
            "selected_run_directory": repo_relative(predecessor_source.run_dir),
            "selected_continuity_directory": repo_relative(predecessor_source.continuity_dir),
            "selected_summary_ref": (
                repo_relative(predecessor_source.summary_path)
                if predecessor_source.summary_path is not None
                else None
            ),
            "predecessor_turn_identity": predecessor_source.turn_id,
            "source_note_ref": predecessor_source_note_ref,
        },
        "layer_outcomes": {
            "continuity_body_conformance": {
                "positive": [
                    {
                        "status": positive_body_result["status"],
                        "matched_expectation": positive_body_result["matched_expectation"],
                        "result_ref": positive_body_result["result_ref"],
                    }
                ],
                "negative": [
                    {
                        "status": negative_result["status"],
                        "matched_expectation": negative_result["matched_expectation"],
                        "result_ref": negative_result["result_ref"],
                    }
                ],
            },
            "execution_relation_conformance": {
                "positive": [
                    {
                        "status": execution_relation_result["status"],
                        "result_ref": execution_relation_result["result_ref"],
                    }
                ]
            },
            "preservation_write_outcome": {
                "status": preservation_status,
                "result_ref": preservation_result_ref,
            },
            "fixture_classification": {
                "negative": [
                    {
                        "fixture_class": "conformance_failure",
                        "classification_ref": fixture_classification_ref,
                    }
                ]
            },
        },
        "reading_posture": {
            "positive_path": "read by continuity body, execution relation, and preservation layers",
            "negative_fixture": "read as a successor-without-anchor continuity body failure, not as accidental architectural incoherence",
        },
    }


def build_manifest(
    preservation_id: str,
    execution_id: str,
    continuity_turn_id: str,
    continuity_dir: Path,
    anchor_source: AnchorSource,
    predecessor_source: PredecessorSource,
    written_files: Mapping[str, List[str]],
) -> Dict[str, Any]:
    return {
        "manifest_type": "v1_second_continuity_preservation_manifest",
        "implementation_posture": "implementation_local_layout_only",
        "preservation_identity": preservation_id,
        "execution_identity": execution_id,
        "continuity_turn_identity": continuity_turn_id,
        "continuity_run_directory": repo_relative(continuity_dir),
        "anchor_source_run_ref": repo_relative(anchor_source.run_dir),
        "predecessor_source_run_ref": repo_relative(predecessor_source.run_dir),
        "predecessor_turn_ref": predecessor_source.turn_id,
        "written_files": {
            category: sorted(paths)
            for category, paths in sorted(written_files.items())
        },
        "note": "This local continuity layout is a bounded implementation surface, not final protocol law.",
    }


def main() -> int:
    anchor_sources = find_anchor_sources()
    if not anchor_sources:
        print(
            "No suitable ordinary proof-slice anchor run was found under "
            "v1/registry/runs/. Run "
            "'python3 v1/embodiment/run/run_first_proof_slice.py' "
            "successfully first, then rerun this successor continuity proof slice.",
            file=sys.stderr,
        )
        return 1

    try:
        predecessor_source, anchor_source = find_predecessor_source(anchor_sources)
    except PredecessorSourceNotFound as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        schema_entry = load_continuity_validator()
    except MissingJsonSchemaDependency as exc:
        print(str(exc), file=sys.stderr)
        return 1

    execution_id = generate_identity("execution")
    preservation_id = generate_identity("preservation")
    continuity_turn_id = generate_identity("continuity-turn")
    execution_relation_id = generate_identity("execution-relation")
    anchor_source_note_id = generate_identity("source-note")
    predecessor_source_note_id = generate_identity("source-note")
    recorded_at = utc_now()

    continuity_dir = RUNS_DIR / execution_id / "continuity"
    written_files: Dict[str, List[str]] = {}

    positive_body = build_positive_continuity_body(
        turn_id=continuity_turn_id,
        anchor_source=anchor_source,
        predecessor_source=predecessor_source,
        recorded_at=recorded_at,
    )
    negative_body = build_negative_successor_without_anchor_fixture(
        matter_ref=anchor_source.matter_ref,
        predecessor_turn_ref=predecessor_source.turn_id,
        recorded_at=recorded_at,
    )

    try:
        continuity_dir.mkdir(parents=True, exist_ok=False)

        anchor_source_note = build_anchor_source_note(
            note_id=anchor_source_note_id,
            anchor_source=anchor_source,
        )
        anchor_source_note_path = continuity_dir / "source_notes" / "anchor_source_note.json"
        write_json(anchor_source_note_path, anchor_source_note)
        record_written(written_files, "source_notes", anchor_source_note_path)

        predecessor_source_note = build_predecessor_source_note(
            note_id=predecessor_source_note_id,
            predecessor_source=predecessor_source,
        )
        predecessor_source_note_path = continuity_dir / "source_notes" / "predecessor_source_note.json"
        write_json(predecessor_source_note_path, predecessor_source_note)
        record_written(written_files, "source_notes", predecessor_source_note_path)

        positive_body_path = continuity_dir / "canonical_body" / "positive" / "continuity_turn.body.json"
        write_json(positive_body_path, positive_body)
        record_written(written_files, "continuity_body", positive_body_path)

        positive_body_result = validate_body(
            body=positive_body,
            body_path=positive_body_path,
            schema_entry=schema_entry,
            fixture_classification="positive_fixture",
            expected_status="pass",
        )
        positive_body_result_path = continuity_dir / "conformance" / "body" / "positive" / "continuity_turn.json"
        write_json(positive_body_result_path, positive_body_result)
        record_written(written_files, "conformance", positive_body_result_path)
        positive_body_result["result_ref"] = repo_relative(positive_body_result_path)

        execution_relation = build_execution_relation(
            execution_relation_id=execution_relation_id,
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            continuity_body_ref=repo_relative(positive_body_path),
            anchor_source=anchor_source,
            predecessor_source=predecessor_source,
            recorded_at=recorded_at,
        )
        execution_relation_path = continuity_dir / "execution_relation" / "positive" / "continuity_execution_relation.json"
        write_json(execution_relation_path, execution_relation)
        record_written(written_files, "execution_relation", execution_relation_path)

        execution_relation_result = validate_execution_relation(
            execution_relation=execution_relation,
            execution_relation_path=execution_relation_path,
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            continuity_body_ref=repo_relative(positive_body_path),
            anchor_source=anchor_source,
            predecessor_source=predecessor_source,
        )
        execution_relation_result_path = continuity_dir / "conformance" / "execution_relation" / "positive" / "continuity_execution_relation.json"
        write_json(execution_relation_result_path, execution_relation_result)
        record_written(written_files, "conformance", execution_relation_result_path)
        execution_relation_result["result_ref"] = repo_relative(execution_relation_result_path)

        negative_body_path = continuity_dir / "fixture_outputs" / "negative" / "body" / "successor_without_anchor.body.json"
        write_json(negative_body_path, negative_body)
        record_written(written_files, "negative_fixtures", negative_body_path)

        negative_classification = {
            "fixture_class": "conformance_failure",
            "scope": "successor_continuity_proof_slice",
            "artifact_family": "continuity_turn",
            "expected_surface": "continuity_body_conformance",
            "expected_status": "fail",
            "body_ref": repo_relative(negative_body_path),
            "note": "This fixture fails because predecessor succession does not replace canonical artifact anchoring.",
        }
        negative_classification_path = continuity_dir / "fixture_outputs" / "negative" / "classification.json"
        write_json(negative_classification_path, negative_classification)
        record_written(written_files, "negative_fixtures", negative_classification_path)

        negative_result = validate_body(
            body=negative_body,
            body_path=negative_body_path,
            schema_entry=schema_entry,
            fixture_classification="conformance_failure",
            expected_status="fail",
        )
        negative_result_path = continuity_dir / "conformance" / "body" / "negative" / "successor_without_anchor_continuity_turn.json"
        write_json(negative_result_path, negative_result)
        record_written(written_files, "conformance", negative_result_path)
        negative_result["result_ref"] = repo_relative(negative_result_path)

        preservation_result = evaluate_preservation_conformance(
            continuity_dir=continuity_dir,
            anchor_source=anchor_source,
            predecessor_source=predecessor_source,
            written_files=written_files,
        )
        preservation_result_path = continuity_dir / "conformance" / "preservation" / "run_write_outcome.json"
        write_json(preservation_result_path, preservation_result)
        record_written(written_files, "conformance", preservation_result_path)

        summary = build_run_summary(
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            continuity_dir=continuity_dir,
            anchor_source=anchor_source,
            predecessor_source=predecessor_source,
            positive_body_result=positive_body_result,
            execution_relation_result=execution_relation_result,
            negative_result=negative_result,
            fixture_classification_ref=repo_relative(negative_classification_path),
            anchor_source_note_ref=repo_relative(anchor_source_note_path),
            predecessor_source_note_ref=repo_relative(predecessor_source_note_path),
            preservation_result_ref=repo_relative(preservation_result_path),
            preservation_status=preservation_result["status"],
        )
        summary_path = continuity_dir / "run_summary" / "run_summary.json"
        write_json(summary_path, summary)
        record_written(written_files, "summary", summary_path)

        manifest = build_manifest(
            preservation_id=preservation_id,
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            continuity_dir=continuity_dir,
            anchor_source=anchor_source,
            predecessor_source=predecessor_source,
            written_files=written_files,
        )
        manifest_path = continuity_dir / "manifest" / "preservation_manifest.json"
        write_json(manifest_path, manifest)
        record_written(written_files, "manifest", manifest_path)
    except OSError as exc:
        print(f"Failed to write bounded v1 successor continuity proof slice outputs: {exc}", file=sys.stderr)
        return 1

    positive_body_failed = positive_body_result["status"] != "pass"
    execution_relation_failed = execution_relation_result["status"] != "pass"
    unexpected_negative_status = negative_result["status"] != "fail"
    preservation_failed = preservation_result["status"] != "pass"

    print("Bounded v1 successor continuity proof slice completed.")
    print(f"Continuity run directory: {repo_relative(continuity_dir)}")
    print(f"Anchor-source ordinary run used: {repo_relative(anchor_source.run_dir)}")
    print(f"Predecessor continuity run used: {repo_relative(predecessor_source.continuity_dir)}")
    print(f"Predecessor continuity turn used: {predecessor_source.turn_id}")
    print(f"Positive continuity body conformance: {positive_body_result['status']}.")
    print(f"Positive execution-relation conformance: {execution_relation_result['status']}.")
    print(f"Negative fixture body conformance: {negative_result['status']} (expected fail).")
    print(f"Continuity preservation conformance: {preservation_result['status']}.")

    if positive_body_failed or execution_relation_failed or unexpected_negative_status or preservation_failed:
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
