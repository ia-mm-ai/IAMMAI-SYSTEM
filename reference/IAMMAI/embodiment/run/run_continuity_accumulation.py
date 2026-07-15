#!/usr/bin/env python3
"""
Run the first bounded Level 5 continuity accumulation batch for IAMMAI.

This helper stays derivative. It invokes the existing bounded runner for each
planned matter in order, records the resulting derivative execution summaries,
and writes one derivative batch summary for human audit.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple


REPO_ROOT = Path(__file__).resolve().parents[2]
EMBODIMENT_DIR = REPO_ROOT / "embodiment"
OUTPUT_DIR = EMBODIMENT_DIR / "output"
PLAN_PATH = EMBODIMENT_DIR / "CONTINUITY_ACCUMULATION_PLAN_v0.md"
BOUNDED_RUNNER = EMBODIMENT_DIR / "run" / "run_bounded_cycle.py"

BATCH: List[str] = [
    "embodiment/input/matter_004.json",
    "embodiment/input/matter_005.json",
    "embodiment/input/matter_006.json",
    "embodiment/input/matter_007.json",
    "embodiment/input/matter_008.json",
    "embodiment/input/matter_edge_001.json",
    "embodiment/input/matter_edge_002.json",
]

HUMAN_AUDIT_REMINDER = (
    "Architectural seam detection, stop-condition judgment, drift reading, "
    "and stability claims still require human audit."
)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the fixed Level 5 continuity accumulation batch and write one "
            "derivative batch summary."
        )
    )
    return parser.parse_args(argv)


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
    return str(path.relative_to(REPO_ROOT))


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def list_execution_summaries() -> Set[Path]:
    if not OUTPUT_DIR.exists():
        return set()
    return {
        path.resolve()
        for path in OUTPUT_DIR.glob("*.execution_summary.json")
        if path.is_file()
    }


def load_execution_summary(path: Path) -> Tuple[Optional[Dict[str, Any]], List[str]]:
    notes: List[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        notes.append("summary_read_error")
        return None, notes
    except json.JSONDecodeError:
        notes.append("summary_json_invalid")
        return None, notes

    if not isinstance(payload, dict):
        notes.append("summary_not_object")
        return None, notes

    return payload, notes


def locate_new_summary(before: Set[Path]) -> Tuple[Optional[Path], List[str]]:
    notes: List[str] = []
    after = list_execution_summaries()
    new_paths = sorted(
        after - before,
        key=lambda path: path.stat().st_mtime_ns,
    )

    if not new_paths:
        notes.append("no_new_execution_summary_detected")
        return None, notes

    if len(new_paths) > 1:
        notes.append(f"multiple_new_execution_summaries_detected:{len(new_paths)}")

    return new_paths[-1], notes


def run_step(index: int, matter_file: str) -> Tuple[Dict[str, Any], List[str]]:
    before = list_execution_summaries()
    command = [sys.executable, "-B", str(BOUNDED_RUNNER), matter_file]
    completed = subprocess.run(
        command,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    summary_path, notes = locate_new_summary(before)
    summary_payload: Optional[Dict[str, Any]] = None
    if summary_path is not None:
        summary_payload, load_notes = load_execution_summary(summary_path)
        notes.extend(load_notes)

    actual_status = "summary_missing"
    stopped_at: Optional[str] = None
    continuity_emitted = False

    if summary_payload is not None:
        actual_status = str(summary_payload.get("status", "summary_status_missing"))
        raw_stopped_at = summary_payload.get("stopped_at")
        if isinstance(raw_stopped_at, str) and raw_stopped_at:
            stopped_at = raw_stopped_at
        continuity_emitted = bool(summary_payload.get("continuity_turn_ref"))

    step_mismatches: List[str] = []
    if actual_status != "success":
        step_mismatches.append(f"expected_status_success_got_{actual_status}")
    if summary_payload is not None and not continuity_emitted:
        step_mismatches.append("expected_continuity_turn_missing")
    if completed.returncode != 0:
        step_mismatches.append(f"expected_exit_0_got_{completed.returncode}")
    if summary_path is None:
        step_mismatches.append("missing_execution_summary")

    step_record: Dict[str, Any] = {
        "step_number": index,
        "matter_file": matter_file,
        "actual_status": actual_status,
        "stopped_at": stopped_at,
        "continuity_emitted": continuity_emitted,
        "summary_ref": repo_relative(summary_path) if summary_path is not None else None,
        "subprocess_exit_code": completed.returncode,
        "stdout": completed.stdout.strip(),
        "stderr": completed.stderr.strip(),
        "matched_successful_continuity_expectation": (
            actual_status == "success"
            and continuity_emitted
            and completed.returncode == 0
        ),
    }
    if notes:
        step_record["notes"] = notes

    return step_record, step_mismatches


def build_batch_summary(
    *,
    summary_path: Path,
    steps: List[Dict[str, Any]],
    mismatches: List[Dict[str, Any]],
) -> Dict[str, Any]:
    batch_matched_expectation = not mismatches and all(
        bool(step.get("matched_successful_continuity_expectation"))
        for step in steps
    )

    return {
        "summary_type": "continuity_accumulation_summary",
        "canonical": False,
        "plan_ref": repo_relative(PLAN_PATH),
        "runner_ref": repo_relative(BOUNDED_RUNNER),
        "ordered_run_list": list(BATCH),
        "steps": steps,
        "batch_matched_expectation": batch_matched_expectation,
        "obvious_mismatches": mismatches,
        "human_review_required": True,
        "human_review_reminder": HUMAN_AUDIT_REMINDER,
        "written_at": utc_now(),
        "summary_ref": repo_relative(summary_path),
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = OUTPUT_DIR / f"continuity_accumulation_{timestamp_slug()}.json"

    steps: List[Dict[str, Any]] = []
    mismatches: List[Dict[str, Any]] = []

    for index, matter_file in enumerate(BATCH, start=1):
        step_record, step_mismatches = run_step(index=index, matter_file=matter_file)
        steps.append(step_record)
        for mismatch in step_mismatches:
            mismatches.append(
                {
                    "step_number": index,
                    "matter_file": matter_file,
                    "issue": mismatch,
                }
            )

    batch_summary = build_batch_summary(
        summary_path=summary_path,
        steps=steps,
        mismatches=mismatches,
    )
    write_json(summary_path, batch_summary)

    print(
        "Continuity accumulation batch completed. Derivative batch summary "
        f"written to {repo_relative(summary_path)}."
    )
    if mismatches:
        print(
            "Batch mismatches were detected. Human architectural audit is "
            "required before drawing stronger conclusions.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
