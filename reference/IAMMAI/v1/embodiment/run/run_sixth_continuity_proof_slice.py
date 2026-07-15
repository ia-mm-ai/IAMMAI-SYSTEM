#!/usr/bin/env python3
"""
Bounded v1 runner for the sixth continuity proof slice.

This script forms one successor continuity turn body anchored to preserved
ordinary v1 canonical artifacts and explicitly linked to a prior lawful
continuity turn selected through the shared source-selection surface. It
validates the canonical continuity body and explicit execution relation through
the shared conformance surface, generates run identities through the shared
identifier surface, and preserves all outputs through the shared
implementation-local preservation layout helper under
v1/registry/runs/<execution-identity>/continuity/.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence

try:
    from conformance_checks import (
        CONTINUITY_SCHEMA_NAME,
        ConformanceChecksError,
        check_execution_relation_conformance,
        load_schema_catalog,
        validate_continuity_body,
    )
    from identifier_generation import (
        new_continuity_turn_id,
        new_execution_id,
        new_execution_relation_id,
        new_preservation_id,
        new_source_note_id,
    )
    from preservation_layout import (
        PreservationLayoutError,
        RUNS_DIR as LAYOUT_RUNS_DIR,
        RunLayout,
        WrittenOutput,
        build_manifest_payload,
        create_continuity_run_layout,
        write_fixture,
        write_json,
        write_manifest,
        write_source_note,
        write_summary,
    )
    from source_selection import (
        SourceSelectionError,
        SuccessorContinuitySources,
        select_successor_continuity_sources,
    )
except ImportError:  # pragma: no cover - package import fallback
    from v1.embodiment.run.conformance_checks import (  # type: ignore
        CONTINUITY_SCHEMA_NAME,
        ConformanceChecksError,
        check_execution_relation_conformance,
        load_schema_catalog,
        validate_continuity_body,
    )
    from v1.embodiment.run.identifier_generation import (  # type: ignore
        new_continuity_turn_id,
        new_execution_id,
        new_execution_relation_id,
        new_preservation_id,
        new_source_note_id,
    )
    from v1.embodiment.run.preservation_layout import (  # type: ignore
        PreservationLayoutError,
        RUNS_DIR as LAYOUT_RUNS_DIR,
        RunLayout,
        WrittenOutput,
        build_manifest_payload,
        create_continuity_run_layout,
        write_fixture,
        write_json,
        write_manifest,
        write_source_note,
        write_summary,
    )
    from v1.embodiment.run.source_selection import (  # type: ignore
        SourceSelectionError,
        SuccessorContinuitySources,
        select_successor_continuity_sources,
    )


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNS_DIR = REPO_ROOT / "v1" / "registry" / "runs"


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def track_output(
    written_outputs: List[WrittenOutput],
    output: WrittenOutput,
) -> WrittenOutput:
    written_outputs.append(output)
    return output


def build_positive_continuity_body(
    turn_id: str,
    sources: SuccessorContinuitySources,
    recorded_at: str,
) -> Dict[str, Any]:
    body = {
        "turn_id": turn_id,
        "matter_ref": sources.ordinary_anchor.matter_ref,
        "recorded_at": recorded_at,
        "predecessor_turn_ref": sources.continuity_predecessor.turn_id,
    }
    body.update(sources.ordinary_anchor.anchor_refs)
    return body


def build_negative_successor_without_anchor_fixture(
    matter_ref: str,
    predecessor_turn_ref: str,
    recorded_at: str,
) -> Dict[str, Any]:
    return {
        "turn_id": new_continuity_turn_id(),
        "matter_ref": matter_ref,
        "recorded_at": recorded_at,
        "predecessor_turn_ref": predecessor_turn_ref,
    }


def build_execution_relation(
    execution_relation_id: str,
    execution_id: str,
    continuity_turn_id: str,
    continuity_body_ref: str,
    sources: SuccessorContinuitySources,
    recorded_at: str,
) -> Dict[str, Any]:
    return {
        "execution_relation_id": execution_relation_id,
        "relation_type": "continuity_execution_relation",
        "execution_identity": execution_id,
        "continuity_turn_identity": continuity_turn_id,
        "continuity_body_ref": continuity_body_ref,
        "anchor_source_run_ref": repo_relative(sources.ordinary_anchor.run_dir),
        "predecessor_source_run_ref": repo_relative(
            sources.continuity_predecessor.run_dir
        ),
        "predecessor_turn_ref": sources.continuity_predecessor.turn_id,
        "recorded_at": recorded_at,
    }


def build_source_note(
    note_id: str,
    source_role: str,
    source_record: Mapping[str, Any],
) -> Dict[str, Any]:
    return {
        "source_note_id": note_id,
        "source_note_type": "selected_source_record",
        "source_role": source_role,
        "recorded_at": utc_now(),
        "selected_source": dict(source_record),
    }


def evaluate_preservation_conformance(
    layout: RunLayout,
    sources: SuccessorContinuitySources,
    written_outputs: Sequence[WrittenOutput],
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

    add_check(
        "written_files_exist",
        all(output.path.exists() for output in written_outputs),
        "All preserved continuity files recorded before preservation conformance must exist.",
    )
    add_check(
        "continuity_body_separate_from_execution_relation",
        any(output.layer == "canonical_body" for output in written_outputs)
        and any(output.layer == "execution_relation" for output in written_outputs),
        "Continuity body and explicit execution relation must both be preserved separately.",
    )
    add_check(
        "conformance_layer_present",
        any(output.layer == "conformance" for output in written_outputs),
        "Conformance material must remain explicitly preserved as its own readable layer.",
    )
    add_check(
        "source_notes_present",
        sum(1 for output in written_outputs if output.layer == "source_notes") >= 2,
        "Preserved source notes for both ordinary anchor source and predecessor continuity source must remain readable.",
    )
    add_check(
        "negative_fixture_separated",
        any(output.layer == "fixtures" for output in written_outputs)
        and all(
            "/fixture_outputs/negative/" in repo_relative(output.path)
            for output in written_outputs
            if output.layer == "fixtures"
        ),
        "Negative successor-continuity fixture material must remain under an explicitly separate negative fixture branch.",
    )
    add_check(
        "shared_layout_surface_used",
        layout.kind == "continuity"
        and layout.naming_posture == "implementation_local_default"
        and layout.root_dir.name == "continuity",
        "Continuity outputs must be preserved through the shared implementation-local layout surface.",
    )
    add_check(
        "selector_coherence_present",
        bool(sources.coherence_checks),
        "Shared source selection must preserve explicit coherence checks for the selected source pair.",
    )
    add_check(
        "anchor_source_still_exists",
        sources.ordinary_anchor.run_dir.is_dir()
        and all(
            path.is_file()
            for path in sources.ordinary_anchor.canonical_body_paths.values()
        ),
        "The selected ordinary proof-slice anchor source and its canonical bodies must remain available.",
    )
    add_check(
        "predecessor_source_still_exists",
        sources.continuity_predecessor.continuity_dir.is_dir()
        and sources.continuity_predecessor.continuity_body_path.is_file()
        and sources.continuity_predecessor.body_conformance_path.is_file()
        and sources.continuity_predecessor.anchor_source_note_path.is_file(),
        "The selected predecessor continuity source, positive continuity body, and recorded anchor note must remain available.",
    )
    add_check(
        "selected_sources_remain_coherent",
        sources.continuity_predecessor.anchor_source_run_dir
        == sources.ordinary_anchor.run_dir
        and sources.continuity_predecessor.matter_ref
        == sources.ordinary_anchor.matter_ref,
        "The selected predecessor continuity source must remain coherent with the selected ordinary anchor source.",
    )
    add_check(
        "continuity_directory_bounded_to_v1_registry",
        layout.root_dir.name == "continuity"
        and layout.root_dir.parent.parent == RUNS_DIR,
        "The local continuity preservation surface must remain bounded to v1/registry/runs/<execution-identity>/continuity/.",
    )

    errors = [check for check in checks if check["status"] == "fail"]
    return {
        "surface": "continuity_preservation_conformance",
        "status": "pass" if not errors else "fail",
        "checked_at": utc_now(),
        "continuity_run_directory": repo_relative(layout.root_dir),
        "preservation_layout": layout.as_record(),
        "checks": checks,
    }


def build_run_summary(
    execution_id: str,
    continuity_turn_id: str,
    layout: RunLayout,
    sources: SuccessorContinuitySources,
    positive_body_result: Mapping[str, Any],
    execution_relation_result: Mapping[str, Any],
    negative_result: Mapping[str, Any],
    fixture_classification_ref: str,
    anchor_source_note_ref: str,
    predecessor_source_note_ref: str,
    preservation_result_ref: str,
    preservation_status: str,
) -> Dict[str, Any]:
    anchor_source_record = sources.ordinary_anchor.as_record()
    predecessor_source_record = sources.continuity_predecessor.as_record()

    return {
        "summary_type": "v1_sixth_continuity_proof_slice_summary",
        "execution_identity": execution_id,
        "continuity_turn_identity": continuity_turn_id,
        "continuity_run_directory": repo_relative(layout.root_dir),
        "source_selection": {
            "source_class": sources.source_class,
            "selection_basis": sources.selection_basis,
            "coherence_checks": [
                check.as_record() for check in sources.coherence_checks
            ],
        },
        "anchor_source_used": {
            "source_class": anchor_source_record["source_class"],
            "selected_run_directory": anchor_source_record["run_directory"],
            "selected_summary_ref": anchor_source_record["selected_summary_ref"],
            "selected_preservation_conformance_ref": anchor_source_record[
                "selected_preservation_conformance_ref"
            ],
            "matter_ref": anchor_source_record["matter_ref"],
            "selection_basis": anchor_source_record["selection_basis"],
            "source_note_ref": anchor_source_note_ref,
        },
        "predecessor_source_used": {
            "source_class": predecessor_source_record["source_class"],
            "selected_run_directory": predecessor_source_record["run_directory"],
            "selected_continuity_directory": predecessor_source_record[
                "selected_continuity_directory"
            ],
            "selected_summary_ref": predecessor_source_record["selected_summary_ref"],
            "selected_body_conformance_ref": predecessor_source_record[
                "selected_body_conformance_ref"
            ],
            "matter_ref": predecessor_source_record["matter_ref"],
            "predecessor_turn_identity": predecessor_source_record[
                "predecessor_turn_identity"
            ],
            "selection_basis": predecessor_source_record["selection_basis"],
            "source_note_ref": predecessor_source_note_ref,
        },
        "layer_outcomes": {
            "continuity_body_conformance": {
                "positive": [
                    {
                        "status": positive_body_result["status"],
                        "matched_expectation": positive_body_result[
                            "matched_expectation"
                        ],
                        "result_ref": positive_body_result["result_ref"],
                    }
                ],
                "negative": [
                    {
                        "status": negative_result["status"],
                        "matched_expectation": negative_result[
                            "matched_expectation"
                        ],
                        "result_ref": negative_result["result_ref"],
                    }
                ],
            },
            "execution_relation_conformance": {
                "positive": [
                    {
                        "status": execution_relation_result["status"],
                        "matched_expectation": execution_relation_result[
                            "matched_expectation"
                        ],
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
            "positive_path": "read by continuity body, execution relation, conformance, source-note, and preservation layers",
            "negative_fixture": "read as a successor-without-anchor continuity body failure, not as accidental architectural incoherence",
        },
    }


def main() -> int:
    try:
        sources = select_successor_continuity_sources(RUNS_DIR)
    except SourceSelectionError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    try:
        schema_catalog = load_schema_catalog((CONTINUITY_SCHEMA_NAME,))
    except ConformanceChecksError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    execution_id = new_execution_id()
    preservation_id = new_preservation_id()
    continuity_turn_id = new_continuity_turn_id()
    execution_relation_id = new_execution_relation_id()
    anchor_source_note_id = new_source_note_id()
    predecessor_source_note_id = new_source_note_id()
    recorded_at = utc_now()

    positive_body = build_positive_continuity_body(
        turn_id=continuity_turn_id,
        sources=sources,
        recorded_at=recorded_at,
    )
    negative_body = build_negative_successor_without_anchor_fixture(
        matter_ref=sources.ordinary_anchor.matter_ref,
        predecessor_turn_ref=sources.continuity_predecessor.turn_id,
        recorded_at=recorded_at,
    )

    try:
        layout = create_continuity_run_layout(
            execution_id,
            LAYOUT_RUNS_DIR,
            exist_ok=False,
        )
        written_outputs: List[WrittenOutput] = []

        anchor_source_note = build_source_note(
            note_id=anchor_source_note_id,
            source_role="ordinary_anchor_source",
            source_record=sources.ordinary_anchor.as_record(),
        )
        anchor_source_note_output = track_output(
            written_outputs,
            write_source_note(layout, "anchor_source_note.json", anchor_source_note),
        )

        predecessor_source_note = build_source_note(
            note_id=predecessor_source_note_id,
            source_role="continuity_predecessor_source",
            source_record=sources.continuity_predecessor.as_record(),
        )
        predecessor_source_note_output = track_output(
            written_outputs,
            write_source_note(
                layout,
                "predecessor_source_note.json",
                predecessor_source_note,
            ),
        )

        positive_body_output = track_output(
            written_outputs,
            write_json(
                layout,
                "canonical_body",
                "positive/continuity_turn.body.json",
                positive_body,
            ),
        )

        positive_body_result = validate_continuity_body(
            schema_catalog,
            positive_body,
            body_ref=positive_body_output.path,
            fixture_classification="positive_fixture",
            expected_status="pass",
        ).as_record()
        positive_body_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "body/positive/continuity_turn.json",
                positive_body_result,
            ),
        )
        positive_body_result["result_ref"] = repo_relative(
            positive_body_result_output.path
        )

        execution_relation = build_execution_relation(
            execution_relation_id=execution_relation_id,
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            continuity_body_ref=repo_relative(positive_body_output.path),
            sources=sources,
            recorded_at=recorded_at,
        )
        execution_relation_output = track_output(
            written_outputs,
            write_json(
                layout,
                "execution_relation",
                "positive/continuity_execution_relation.json",
                execution_relation,
            ),
        )

        execution_relation_result = check_execution_relation_conformance(
            execution_relation,
            execution_identity=execution_id,
            continuity_turn_identity=continuity_turn_id,
            continuity_body_ref=positive_body_output.path,
            execution_relation_ref=execution_relation_output.path,
            anchor_source_run_ref=sources.ordinary_anchor.run_dir,
            predecessor_source_run_ref=sources.continuity_predecessor.run_dir,
            predecessor_turn_ref=sources.continuity_predecessor.turn_id,
            expected_status="pass",
        ).as_record()
        execution_relation_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "execution_relation/positive/continuity_execution_relation.json",
                execution_relation_result,
            ),
        )
        execution_relation_result["result_ref"] = repo_relative(
            execution_relation_result_output.path
        )

        negative_body_output = track_output(
            written_outputs,
            write_fixture(
                layout,
                "negative/body/successor_without_anchor.body.json",
                negative_body,
            ),
        )

        negative_classification = {
            "fixture_class": "conformance_failure",
            "scope": "sixth_successor_continuity_proof_slice",
            "artifact_family": "continuity_turn",
            "expected_surface": "continuity_body_conformance",
            "expected_status": "fail",
            "body_ref": repo_relative(negative_body_output.path),
            "note": "This fixture fails because predecessor succession does not replace canonical artifact anchoring.",
        }
        negative_classification_output = track_output(
            written_outputs,
            write_fixture(layout, "negative/classification.json", negative_classification),
        )

        negative_result = validate_continuity_body(
            schema_catalog,
            negative_body,
            body_ref=negative_body_output.path,
            fixture_classification="conformance_failure",
            expected_status="fail",
        ).as_record()
        negative_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "body/negative/successor_without_anchor_continuity_turn.json",
                negative_result,
            ),
        )
        negative_result["result_ref"] = repo_relative(negative_result_output.path)

        preservation_result = evaluate_preservation_conformance(
            layout=layout,
            sources=sources,
            written_outputs=written_outputs,
        )
        preservation_result_output = track_output(
            written_outputs,
            write_json(
                layout,
                "conformance",
                "preservation/run_write_outcome.json",
                preservation_result,
            ),
        )

        summary = build_run_summary(
            execution_id=execution_id,
            continuity_turn_id=continuity_turn_id,
            layout=layout,
            sources=sources,
            positive_body_result=positive_body_result,
            execution_relation_result=execution_relation_result,
            negative_result=negative_result,
            fixture_classification_ref=repo_relative(
                negative_classification_output.path
            ),
            anchor_source_note_ref=repo_relative(anchor_source_note_output.path),
            predecessor_source_note_ref=repo_relative(
                predecessor_source_note_output.path
            ),
            preservation_result_ref=repo_relative(preservation_result_output.path),
            preservation_status=preservation_result["status"],
        )
        summary_output = track_output(
            written_outputs,
            write_summary(layout, summary),
        )

        manifest_payload = build_manifest_payload(
            layout,
            written_outputs,
            manifest_type="v1_sixth_continuity_preservation_manifest",
            extra={
                "preservation_identity": preservation_id,
                "continuity_turn_identity": continuity_turn_id,
                "source_selection": sources.as_record(),
                "preservation_result_ref": repo_relative(
                    preservation_result_output.path
                ),
                "summary_ref": repo_relative(summary_output.path),
            },
        )
        track_output(
            written_outputs,
            write_manifest(layout, manifest_payload),
        )
    except PreservationLayoutError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    positive_body_failed = positive_body_result["status"] != "pass"
    execution_relation_failed = execution_relation_result["status"] != "pass"
    unexpected_negative_status = negative_result["status"] != "fail"
    unexpected_negative_expectation = negative_result["matched_expectation"] is not True
    preservation_failed = preservation_result["status"] != "pass"

    print("Bounded v1 sixth continuity proof slice completed.")
    print(f"Continuity run directory: {repo_relative(layout.root_dir)}")
    print(
        "Anchor-source ordinary run used: "
        f"{repo_relative(sources.ordinary_anchor.run_dir)}"
    )
    print(
        "Predecessor continuity run used: "
        f"{repo_relative(sources.continuity_predecessor.continuity_dir)}"
    )
    print(
        "Predecessor continuity turn used: "
        f"{sources.continuity_predecessor.turn_id}"
    )
    print(f"Positive continuity body conformance: {positive_body_result['status']}.")
    print(
        "Positive execution-relation conformance: "
        f"{execution_relation_result['status']}."
    )
    print(
        "Negative fixture body conformance: "
        f"{negative_result['status']} (expected fail)."
    )
    print(f"Continuity preservation conformance: {preservation_result['status']}.")

    if (
        positive_body_failed
        or execution_relation_failed
        or unexpected_negative_status
        or unexpected_negative_expectation
        or preservation_failed
    ):
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
