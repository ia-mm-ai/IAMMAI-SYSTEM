#!/usr/bin/env python3
"""
Bounded local runner for IAMMAI's controlled-variation phase.

This runner preserves the same slice class as the first proof while allowing
selection of one separately bounded local note matter inside embodiment/input/.
It keeps validation, witness, governance, transition, state, and registry
preservation distinct, and it stops visibly when a required step does not
lawfully proceed.
"""

from __future__ import annotations

import argparse
import json
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
EMBODIMENT_DIR = REPO_ROOT / "embodiment"
INPUT_DIR = EMBODIMENT_DIR / "input"
DEFAULT_INPUT_PATH = INPUT_DIR / "matter_001.json"
OUTPUT_DIR = EMBODIMENT_DIR / "output"
REGISTRY_DIR = EMBODIMENT_DIR / "registry"

EXPECTED_MATTER_TYPE = "local_note_matter"
VALIDATION_CONDITION_SET_REF = "controlled_variation_threshold_validation_v0"
GOVERNANCE_LEGITIMACY_BASIS_REF = "controlled_variation_v0:bounded_local_cycle"


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run one bounded IAMMAI controlled-variation cycle on one local note "
            "matter inside embodiment/input/."
        )
    )
    parser.add_argument(
        "matter_file",
        nargs="?",
        help=(
            "Matter file to run. Defaults to embodiment/input/matter_001.json. "
            "Relative paths without embodiment/input/ are resolved inside "
            "embodiment/input/."
        ),
    )
    return parser.parse_args(argv)


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def display_path(path: Path) -> str:
    try:
        return repo_relative(path)
    except ValueError:
        return str(path)


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def ensure_execution_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)


def is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_input_path(raw_arg: Optional[str]) -> Path:
    if not raw_arg:
        return DEFAULT_INPUT_PATH.resolve(strict=False)

    candidate = Path(raw_arg).expanduser()
    if candidate.is_absolute():
        return candidate.resolve(strict=False)

    if candidate.parts[:2] == ("embodiment", "input"):
        return (REPO_ROOT / candidate).resolve(strict=False)

    return (INPUT_DIR / candidate).resolve(strict=False)


def safe_token(value: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", value.strip())
    cleaned = cleaned.strip("_")
    return cleaned or "matter"


def generate_run_identity(matter_ref: str) -> Tuple[str, str]:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = secrets.token_hex(4)
    matter_token = safe_token(matter_ref)
    run_id = f"run:{matter_token}:{timestamp}:{suffix}"
    run_slug = f"{matter_token}__{timestamp}__{suffix}"
    return run_id, run_slug


def build_artifact_ids(run_id: str) -> Dict[str, str]:
    return {
        "validation": f"validation:{run_id}",
        "witness": f"witness:{run_id}",
        "governance": f"governance:{run_id}",
        "transition": f"transition:{run_id}",
        "state": f"state:{run_id}:truth",
        "threshold_state": f"state:{run_id}:threshold",
        "continuity": f"continuity_turn:{run_id}",
    }


def registry_files_for_run(run_registry_dir: Path) -> Dict[str, Path]:
    return {
        "validation": run_registry_dir / "validation_artifact.json",
        "witness": run_registry_dir / "witness_artifact.json",
        "governance": run_registry_dir / "governance_action.json",
        "transition": run_registry_dir / "transition_record.json",
        "state": run_registry_dir / "state_record.json",
    }


def continuity_registry_path(run_registry_dir: Path) -> Path:
    return run_registry_dir / "continuity_turn.json"


def load_input_payload(input_path: Path) -> Tuple[Optional[str], Optional[Dict[str, Any]], List[str]]:
    input_root = INPUT_DIR.resolve(strict=False)
    if not is_within(input_path, input_root):
        return None, None, ["input_path_outside_bounded_input_area"]

    if input_path.is_dir():
        return None, None, ["input_path_is_directory"]

    if not input_path.exists():
        return None, None, ["input_file_missing"]

    try:
        raw_text = input_path.read_text(encoding="utf-8")
    except OSError:
        return None, None, ["input_read_error"]

    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError:
        return raw_text, None, ["input_json_invalid"]

    if not isinstance(payload, dict):
        return raw_text, None, ["input_not_object"]

    return raw_text, payload, []


def resolved_target_ref(input_path: Path, payload: Optional[Dict[str, Any]]) -> str:
    if isinstance(payload, dict):
        matter_id = payload.get("matter_id")
        if isinstance(matter_id, str) and matter_id.strip():
            return matter_id.strip()

    stem = input_path.stem.strip()
    return stem or "selected_matter"


def validate_matter(payload: Optional[Dict[str, Any]], load_errors: List[str]) -> Tuple[str, List[str]]:
    if load_errors:
        return "fail", list(load_errors)

    reasons: List[str] = []

    if payload is None:
        reasons.append("input_missing")
        return "fail", reasons

    required_fields = ("matter_id", "matter_type", "content")
    missing_fields = [field for field in required_fields if field not in payload]
    if missing_fields:
        reasons.extend(f"missing_{field}" for field in missing_fields)

    matter_id = payload.get("matter_id")
    if not isinstance(matter_id, str) or not matter_id.strip():
        reasons.append("matter_id_invalid")

    matter_type = payload.get("matter_type")
    if not isinstance(matter_type, str) or not matter_type.strip():
        reasons.append("matter_type_invalid")
    elif matter_type != EXPECTED_MATTER_TYPE:
        reasons.append("matter_type_mismatch")

    content = payload.get("content")
    if not isinstance(content, str):
        reasons.append("content_not_string")
    elif not content.strip():
        reasons.append("content_empty")

    if reasons:
        return "fail", reasons

    return (
        "pass",
        [
            "input_file_present",
            "input_path_within_bounded_input_area",
            "required_fields_present",
            "matter_id_non_empty",
            "matter_type_matches_controlled_variation_slice",
            "content_non_empty",
        ],
    )


def build_validation_artifact(
    run_id: str,
    artifact_ids: Dict[str, str],
    target_ref: str,
    outcome: str,
    reasons: List[str],
) -> Dict[str, Any]:
    artifact = {
        "run_id": run_id,
        "validation_id": artifact_ids["validation"],
        "validation_type": "threshold_validation",
        "target_ref": target_ref,
        "condition_set_ref": VALIDATION_CONDITION_SET_REF,
        "outcome": outcome,
        "checked_at": utc_now(),
    }
    if reasons:
        artifact["reason_refs"] = reasons
    return artifact


def build_witness_artifact(
    run_id: str,
    artifact_ids: Dict[str, str],
    target_ref: str,
    input_path: Path,
) -> Dict[str, Any]:
    return {
        "run_id": run_id,
        "witness_id": artifact_ids["witness"],
        "witness_type": "validation_witness",
        "target_ref": target_ref,
        "observed_at": utc_now(),
        "claims": [
            "contact_occurred",
            "bounded_interaction_preserved",
            "validation_event_observed",
        ],
        "non_claims": [
            "not_authorship",
            "not_semantic_source",
            "not_final_authority",
            "not_automatic_truth_creation",
            "not_governance_force",
        ],
        "surface_ref": display_path(input_path),
        "related_validation_ref": artifact_ids["validation"],
    }


def build_governance_action(
    run_id: str,
    artifact_ids: Dict[str, str],
    matter_ref: str,
    witness_present: bool,
) -> Dict[str, Any]:
    artifact = {
        "run_id": run_id,
        "governance_action_id": artifact_ids["governance"],
        "action_type": "authorize",
        "authority_class": "local_operator_governor",
        "actor_ref": "local_operator_governor:default",
        "legitimacy_basis_ref": GOVERNANCE_LEGITIMACY_BASIS_REF,
        "matter_ref": matter_ref,
        "acted_at": utc_now(),
        "related_validation_ref": artifact_ids["validation"],
    }
    if witness_present:
        artifact["related_witness_ref"] = artifact_ids["witness"]
    return artifact


def build_transition_record(
    run_id: str,
    artifact_ids: Dict[str, str],
    matter_ref: str,
    witness_present: bool,
) -> Dict[str, Any]:
    artifact = {
        "run_id": run_id,
        "transition_id": artifact_ids["transition"],
        "matter_ref": matter_ref,
        "source_ref": artifact_ids["threshold_state"],
        "target_ref": artifact_ids["state"],
        "transition_type": "truth_formation",
        "occurred_at": utc_now(),
        "related_validation_ref": artifact_ids["validation"],
        "related_governance_action_ref": artifact_ids["governance"],
    }
    if witness_present:
        artifact["related_witness_ref"] = artifact_ids["witness"]
    return artifact


def build_state_record(
    run_id: str,
    artifact_ids: Dict[str, str],
    matter_ref: str,
    witness_present: bool,
) -> Dict[str, Any]:
    artifact = {
        "run_id": run_id,
        "state_id": artifact_ids["state"],
        "matter_ref": matter_ref,
        "state_family": "standing",
        "state_type": "truth",
        "recorded_at": utc_now(),
        "predecessor_ref": artifact_ids["threshold_state"],
        "related_transition_ref": artifact_ids["transition"],
        "related_governance_action_ref": artifact_ids["governance"],
        "related_validation_ref": artifact_ids["validation"],
    }
    if witness_present:
        artifact["related_witness_ref"] = artifact_ids["witness"]
    return artifact


def build_continuity_turn(
    run_id: str,
    artifact_ids: Dict[str, str],
    matter_ref: str,
    witness_present: bool,
) -> Dict[str, Any]:
    artifact = {
        "turn_id": artifact_ids["continuity"],
        "run_id": run_id,
        "matter_ref": matter_ref,
        "recorded_at": utc_now(),
        "validation_ref": artifact_ids["validation"],
        "governance_action_ref": artifact_ids["governance"],
        "transition_ref": artifact_ids["transition"],
        "state_ref": artifact_ids["state"],
    }
    if witness_present:
        artifact["witness_ref"] = artifact_ids["witness"]
    return artifact


def persist_registry_artifact(
    artifact_family: str,
    payload: Dict[str, Any],
    registry_files: Dict[str, Path],
    written_registry_files: Dict[str, str],
) -> None:
    target_path = registry_files[artifact_family]
    write_json(target_path, payload)
    written_registry_files[artifact_family] = repo_relative(target_path)


def expected_registry_paths(registry_files: Dict[str, Path]) -> List[str]:
    return [repo_relative(path) for path in registry_files.values()]


def missing_registry_paths(
    registry_files: Dict[str, Path],
    written_registry_files: Dict[str, str],
) -> List[str]:
    written_paths = set(written_registry_files.values())
    return [
        path
        for path in expected_registry_paths(registry_files)
        if path not in written_paths
    ]


def write_execution_summary(
    *,
    run_id: str,
    input_path: Path,
    summary_path: Path,
    run_registry_dir: Path,
    status: str,
    stopped_at: str,
    message: str,
    matter_ref: str,
    validation_outcome: str,
    validation_reasons: List[str],
    registry_files: Dict[str, Path],
    written_registry_files: Dict[str, str],
) -> None:
    summary = {
        "summary_type": "execution_summary",
        "canonical": False,
        "run_id": run_id,
        "matter_ref": matter_ref,
        "input_ref": display_path(input_path),
        "registry_ref": repo_relative(run_registry_dir),
        "status": status,
        "stopped_at": stopped_at,
        "message": message,
        "validation_outcome": validation_outcome,
        "validation_reason_refs": validation_reasons,
        "produced_canonical_artifacts": list(written_registry_files.values()),
        "missing_canonical_artifacts": missing_registry_paths(
            registry_files,
            written_registry_files,
        ),
        "written_at": utc_now(),
    }
    continuity_turn_ref = written_registry_files.get("continuity")
    if continuity_turn_ref:
        summary["continuity_turn_ref"] = continuity_turn_ref
    write_json(summary_path, summary)


def emit_visible_failure(
    *,
    run_id: str,
    input_path: Path,
    summary_path: Path,
    run_registry_dir: Path,
    status: str,
    stopped_at: str,
    message: str,
    matter_ref: str,
    validation_outcome: str,
    validation_reasons: List[str],
    registry_files: Dict[str, Path],
    written_registry_files: Dict[str, str],
) -> int:
    try:
        write_execution_summary(
            run_id=run_id,
            input_path=input_path,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status=status,
            stopped_at=stopped_at,
            message=message,
            matter_ref=matter_ref,
            validation_outcome=validation_outcome,
            validation_reasons=validation_reasons,
            registry_files=registry_files,
            written_registry_files=written_registry_files,
        )
    except OSError as exc:
        print(
            f"Failed to preserve execution summary after {stopped_at}: {exc}",
            file=sys.stderr,
        )

    print(message, file=sys.stderr)
    return 1


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)

    try:
        ensure_execution_dirs()
    except OSError as exc:
        print(
            f"Failed to prepare embodiment output or registry directories: {exc}",
            file=sys.stderr,
        )
        return 1

    input_path = resolve_input_path(args.matter_file)
    raw_input: Optional[str]
    matter_payload: Optional[Dict[str, Any]]
    load_errors: List[str]
    raw_input, matter_payload, load_errors = load_input_payload(input_path)

    matter_ref = resolved_target_ref(input_path, matter_payload)
    run_id, run_slug = generate_run_identity(matter_ref)
    run_registry_dir = REGISTRY_DIR / run_slug
    summary_path = OUTPUT_DIR / f"{run_slug}.execution_summary.json"
    artifact_ids = build_artifact_ids(run_id)
    registry_files = registry_files_for_run(run_registry_dir)
    written_registry_files: Dict[str, str] = {}
    validation_outcome = "indeterminate"
    validation_reasons: List[str] = ["validation_not_run"]
    witness_written = False

    try:
        run_registry_dir.mkdir(parents=False, exist_ok=False)
    except OSError as exc:
        return emit_visible_failure(
            run_id=run_id,
            input_path=input_path,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status="failed",
            stopped_at="registry_prepare",
            message=f"Failed to prepare per-run registry preservation surface: {exc}",
            matter_ref=matter_ref,
            validation_outcome=validation_outcome,
            validation_reasons=validation_reasons,
            registry_files=registry_files,
            written_registry_files=written_registry_files,
        )

    try:
        validation_outcome, validation_reasons = validate_matter(matter_payload, load_errors)
        validation_artifact = build_validation_artifact(
            run_id=run_id,
            artifact_ids=artifact_ids,
            target_ref=matter_ref,
            outcome=validation_outcome,
            reasons=validation_reasons,
        )
        persist_registry_artifact(
            "validation",
            validation_artifact,
            registry_files,
            written_registry_files,
        )

        if raw_input is not None:
            witness_artifact = build_witness_artifact(
                run_id,
                artifact_ids,
                matter_ref,
                input_path,
            )
            persist_registry_artifact(
                "witness",
                witness_artifact,
                registry_files,
                written_registry_files,
            )
            witness_written = True

        if validation_outcome != "pass":
            return emit_visible_failure(
                run_id=run_id,
                input_path=input_path,
                summary_path=summary_path,
                run_registry_dir=run_registry_dir,
                status="non_passing",
                stopped_at="validation",
                message=(
                    "Validation did not pass. Governance, transition, and state "
                    "artifacts were not lawfully produced."
                ),
                matter_ref=matter_ref,
                validation_outcome=validation_outcome,
                validation_reasons=validation_reasons,
                registry_files=registry_files,
                written_registry_files=written_registry_files,
            )

        governance_action = build_governance_action(
            run_id,
            artifact_ids,
            matter_ref,
            witness_written,
        )
        persist_registry_artifact(
            "governance",
            governance_action,
            registry_files,
            written_registry_files,
        )

        transition_record = build_transition_record(
            run_id,
            artifact_ids,
            matter_ref,
            witness_written,
        )
        persist_registry_artifact(
            "transition",
            transition_record,
            registry_files,
            written_registry_files,
        )

        state_record = build_state_record(
            run_id,
            artifact_ids,
            matter_ref,
            witness_written,
        )
        persist_registry_artifact(
            "state",
            state_record,
            registry_files,
            written_registry_files,
        )

        registry_files["continuity"] = continuity_registry_path(run_registry_dir)
        continuity_turn = build_continuity_turn(
            run_id,
            artifact_ids,
            matter_ref,
            witness_written,
        )
        persist_registry_artifact(
            "continuity",
            continuity_turn,
            registry_files,
            written_registry_files,
        )

        write_execution_summary(
            run_id=run_id,
            input_path=input_path,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status="success",
            stopped_at="complete",
            message=(
                "The bounded controlled-variation cycle completed with separate "
                "validation, witness, governance, transition, state, continuity, "
                "and registry preservation."
            ),
            matter_ref=matter_ref,
            validation_outcome=validation_outcome,
            validation_reasons=validation_reasons,
            registry_files=registry_files,
            written_registry_files=written_registry_files,
        )
    except OSError as exc:
        return emit_visible_failure(
            run_id=run_id,
            input_path=input_path,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status="failed",
            stopped_at="registry_or_output_write",
            message=f"Artifact preservation failed: {exc}",
            matter_ref=matter_ref,
            validation_outcome=validation_outcome,
            validation_reasons=validation_reasons,
            registry_files=registry_files,
            written_registry_files=written_registry_files,
        )
    except Exception as exc:  # pragma: no cover - bounded visible failure path
        return emit_visible_failure(
            run_id=run_id,
            input_path=input_path,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status="failed",
            stopped_at="unexpected_runtime_failure",
            message=f"Unexpected bounded runner failure: {exc}",
            matter_ref=matter_ref,
            validation_outcome=validation_outcome,
            validation_reasons=validation_reasons,
            registry_files=registry_files,
            written_registry_files=written_registry_files,
        )

    print(
        "Bounded controlled-variation cycle completed. Canonical artifacts were "
        f"preserved in {repo_relative(run_registry_dir)}, including a continuity "
        f"turn for this successful run, and derivative summary output in "
        f"{repo_relative(summary_path)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
