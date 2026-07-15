#!/usr/bin/env python3
"""
Run the first bounded Level 4 sequential pressure sequence for IAMMAI.

This helper stays derivative. It invokes the existing bounded runner for each
planned matter in order, records the resulting derivative execution summaries,
and writes one derivative sequence summary for human audit.
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
PLAN_PATH = EMBODIMENT_DIR / "SEQUENTIAL_PRESSURE_PLAN_v0.md"
BOUNDED_RUNNER = EMBODIMENT_DIR / "run" / "run_bounded_cycle.py"

SEQUENCE: List[Dict[str, str]] = [
    {
        "matter_file": "embodiment/input/matter_006.json",
        "expected_status": "success",
    },
    {
        "matter_file": "embodiment/input/matter_edge_001.json",
        "expected_status": "success",
    },
    {
        "matter_file": "embodiment/input/matter_invalid_002.json",
        "expected_status": "non_passing",
    },
    {
        "matter_file": "embodiment/input/matter_004.json",
        "expected_status": "success",
    },
    {
        "matter_file": "embodiment/input/matter_edge_002.json",
        "expected_status": "success",
    },
]

EXPECTED_EXIT_CODES = {
    "success": 0,
    "non_passing": 1,
}

HUMAN_AUDIT_REMINDER = (
    "Architectural stop conditions, drift signals, continuity truthfulness, "
    "and stability judgment still require human audit."
)


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run the fixed Level 4 sequential pressure sequence and write one "
            "derivative sequence summary."
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


def expected_continuity(expected_status: str) -> bool:
    return expected_status == "success"


def run_step(index: int, matter_file: str, expected_status: str) -> Tuple[Dict[str, Any], List[str]]:
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
    if actual_status != expected_status:
        step_mismatches.append(
            f"expected_status_{expected_status}_got_{actual_status}"
        )

    continuity_expected = expected_continuity(expected_status)
    if summary_payload is not None and continuity_emitted != continuity_expected:
        step_mismatches.append(
            "continuity_expectation_mismatch"
        )

    expected_exit_code = EXPECTED_EXIT_CODES.get(expected_status)
    if expected_exit_code is not None and completed.returncode != expected_exit_code:
        step_mismatches.append(
            f"expected_exit_{expected_exit_code}_got_{completed.returncode}"
        )

    if summary_path is None:
        step_mismatches.append("missing_execution_summary")

    stdout_text = completed.stdout.strip()
    stderr_text = completed.stderr.strip()

    step_record: Dict[str, Any] = {
        "step_number": index,
        "matter_file": matter_file,
        "expected_class": expected_status,
        "actual_status": actual_status,
        "stopped_at": stopped_at,
        "continuity_emitted": continuity_emitted,
        "summary_ref": repo_relative(summary_path) if summary_path is not None else None,
        "subprocess_exit_code": completed.returncode,
        "matched_expected_status": actual_status == expected_status,
        "stdout": stdout_text,
        "stderr": stderr_text,
    }
    if notes:
        step_record["notes"] = notes

    return step_record, step_mismatches


def build_sequence_summary(
    *,
    summary_path: Path,
    steps: List[Dict[str, Any]],
    mismatches: List[Dict[str, Any]],
) -> Dict[str, Any]:
    ordered_run_list = [step["matter_file"] for step in SEQUENCE]
    plan_matched = not mismatches and all(
        bool(step.get("matched_expected_status")) for step in steps
    )

    return {
        "summary_type": "sequential_pressure_summary",
        "canonical": False,
        "plan_ref": repo_relative(PLAN_PATH),
        "runner_ref": repo_relative(BOUNDED_RUNNER),
        "ordered_run_list": ordered_run_list,
        "steps": steps,
        "basic_plan_match": plan_matched,
        "obvious_mismatches": mismatches,
        "human_review_required": True,
        "human_review_reminder": HUMAN_AUDIT_REMINDER,
        "written_at": utc_now(),
        "summary_ref": repo_relative(summary_path),
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parse_args(argv)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    summary_path = OUTPUT_DIR / f"sequential_pressure_{timestamp_slug()}.json"

    steps: List[Dict[str, Any]] = []
    mismatches: List[Dict[str, Any]] = []

    for index, step in enumerate(SEQUENCE, start=1):
        step_record, step_mismatches = run_step(
            index=index,
            matter_file=step["matter_file"],
            expected_status=step["expected_status"],
        )
        steps.append(step_record)
        for mismatch in step_mismatches:
            mismatches.append(
                {
                    "step_number": index,
                    "matter_file": step["matter_file"],
                    "issue": mismatch,
                }
            )

    sequence_summary = build_sequence_summary(
        summary_path=summary_path,
        steps=steps,
        mismatches=mismatches,
    )
    write_json(summary_path, sequence_summary)

    print(
        "Sequential pressure sequence completed. Derivative sequence summary "
        f"written to {repo_relative(summary_path)}."
    )
    if mismatches:
        print(
            "Basic plan mismatches were detected. Human architectural audit is "
            "required before drawing stronger conclusions.",
            file=sys.stderr,
        )
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
