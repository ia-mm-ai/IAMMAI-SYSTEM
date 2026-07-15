#!/usr/bin/env python3
"""
Minimal local runner for IAMMAI's first bounded lawful cycle.

This runner is intentionally fixed to one selected matter and one selected
first cycle. It keeps validation, witness, governance, transition, state,
and registry preservation distinct, and it stops visibly when a required
step does not lawfully proceed.
"""

from __future__ import annotations

import json
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
EMBODIMENT_DIR = REPO_ROOT / "embodiment"
INPUT_PATH = EMBODIMENT_DIR / "input" / "matter_001.json"
OUTPUT_DIR = EMBODIMENT_DIR / "output"
REGISTRY_DIR = EMBODIMENT_DIR / "registry"

EXPECTED_MATTER_ID = "matter_001"
EXPECTED_MATTER_TYPE = "local_note_matter"
EXPECTED_CONTENT = "Signal accepted, little bitch."


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def repo_relative(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def ensure_execution_dirs() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)


def generate_run_identity() -> Tuple[str, str]:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    suffix = secrets.token_hex(4)
    run_id = f"run:{EXPECTED_MATTER_ID}:{timestamp}:{suffix}"
    run_slug = f"{EXPECTED_MATTER_ID}__{timestamp}__{suffix}"
    return run_id, run_slug


def build_artifact_ids(run_id: str) -> Dict[str, str]:
    return {
        "validation": f"validation:{run_id}",
        "witness": f"witness:{run_id}",
        "governance": f"governance:{run_id}",
        "transition": f"transition:{run_id}",
        "state": f"state:{run_id}:truth",
        "threshold_state": f"state:{run_id}:threshold",
    }


def registry_files_for_run(run_registry_dir: Path) -> Dict[str, Path]:
    return {
        "validation": run_registry_dir / "validation_artifact.json",
        "witness": run_registry_dir / "witness_artifact.json",
        "governance": run_registry_dir / "governance_action.json",
        "transition": run_registry_dir / "transition_record.json",
        "state": run_registry_dir / "state_record.json",
    }


def load_input_payload() -> Tuple[Optional[str], Optional[Dict[str, Any]], List[str]]:
    if not INPUT_PATH.exists():
        return None, None, ["input_file_missing"]

    try:
        raw_text = INPUT_PATH.read_text(encoding="utf-8")
    except OSError:
        return None, None, ["input_read_error"]

    try:
        payload = json.loads(raw_text)
    except json.JSONDecodeError:
        return raw_text, None, ["input_json_invalid"]

    if not isinstance(payload, dict):
        return raw_text, None, ["input_not_object"]

    return raw_text, payload, []


def resolved_target_ref(payload: Optional[Dict[str, Any]]) -> str:
    if isinstance(payload, dict):
        matter_id = payload.get("matter_id")
        if isinstance(matter_id, str) and matter_id.strip():
            return matter_id
    return EXPECTED_MATTER_ID


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
    elif matter_id != EXPECTED_MATTER_ID:
        reasons.append("matter_id_mismatch")

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
    elif content != EXPECTED_CONTENT:
        reasons.append("content_mismatch")

    if reasons:
        return "fail", reasons

    return (
        "pass",
        [
            "input_file_present",
            "required_fields_present",
            "matter_id_matches_first_cycle",
            "matter_type_matches_first_cycle",
            "content_non_empty",
            "content_matches_first_cycle",
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
        "condition_set_ref": "first_live_cycle_threshold_validation_v0",
        "outcome": outcome,
        "checked_at": utc_now(),
    }
    if reasons:
        artifact["reason_refs"] = reasons
    return artifact


def build_witness_artifact(run_id: str, artifact_ids: Dict[str, str], target_ref: str) -> Dict[str, Any]:
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
        "surface_ref": repo_relative(INPUT_PATH),
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
        "legitimacy_basis_ref": "embodiment_decision_v0:first_local_cycle",
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
    # This summary is derivative output only. Canonical artifacts remain in registry/.
    summary = {
        "summary_type": "execution_summary",
        "canonical": False,
        "run_id": run_id,
        "matter_ref": matter_ref,
        "input_ref": repo_relative(INPUT_PATH),
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
    write_json(summary_path, summary)


def emit_visible_failure(
    *,
    run_id: str,
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


def main() -> int:
    try:
        ensure_execution_dirs()
    except OSError as exc:
        print(f"Failed to prepare embodiment output or registry directories: {exc}", file=sys.stderr)
        return 1

    run_id, run_slug = generate_run_identity()
    run_registry_dir = REGISTRY_DIR / run_slug
    summary_path = OUTPUT_DIR / f"{run_slug}.execution_summary.json"
    artifact_ids = build_artifact_ids(run_id)
    registry_files = registry_files_for_run(run_registry_dir)
    written_registry_files: Dict[str, str] = {}
    validation_outcome = "indeterminate"
    validation_reasons: List[str] = ["validation_not_run"]
    matter_ref = EXPECTED_MATTER_ID

    try:
        run_registry_dir.mkdir(parents=False, exist_ok=False)
    except OSError as exc:
        return emit_visible_failure(
            run_id=run_id,
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

    raw_input: Optional[str] = None
    matter_payload: Optional[Dict[str, Any]] = None
    load_errors: List[str] = []
    witness_written = False

    try:
        raw_input, matter_payload, load_errors = load_input_payload()
        matter_ref = resolved_target_ref(matter_payload)

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
            witness_artifact = build_witness_artifact(run_id, artifact_ids, matter_ref)
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

        write_execution_summary(
            run_id=run_id,
            summary_path=summary_path,
            run_registry_dir=run_registry_dir,
            status="success",
            stopped_at="complete",
            message=(
                "The first bounded lawful cycle completed with separate validation, "
                "witness, governance, transition, state, and registry preservation."
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
        "First bounded lawful cycle completed. Canonical artifacts were preserved in "
        f"{repo_relative(run_registry_dir)} and derivative summary output in {repo_relative(summary_path)}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
