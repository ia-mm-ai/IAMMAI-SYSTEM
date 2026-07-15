#!/usr/bin/env python3
"""
Refresh the current readability layer across all standing readable families.

This script orchestrates the existing readability builders in a fixed order so
the proof/archive, constitutional, seam-lab, cross-carrier, and top-level
current pointer surfaces can be refreshed coherently without reimplementing
their internal logic.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence


REPO_ROOT = Path(__file__).resolve().parent
CURRENT_POINTER_PATH = REPO_ROOT / "CURRENT_READABILITY_SURFACES.md"


@dataclass(frozen=True)
class Stage:
    name: str
    script_path: Path
    family: str


@dataclass(frozen=True)
class StageResult:
    stage: Stage
    returncode: int
    stdout: str
    stderr: str


STAGES: Sequence[Stage] = (
    Stage(
        name="Proof/archive snapshot",
        script_path=REPO_ROOT / "v1" / "embodiment" / "run" / "build_run_lineage_snapshot.py",
        family="proof/archive",
    ),
    Stage(
        name="Proof/archive report",
        script_path=REPO_ROOT / "v1" / "embodiment" / "run" / "build_run_lineage_report.py",
        family="proof/archive",
    ),
    Stage(
        name="Constitutional snapshot",
        script_path=REPO_ROOT / "protocol" / "build_constitutional_surface_snapshot.py",
        family="constitutional",
    ),
    Stage(
        name="Constitutional report from snapshot",
        script_path=REPO_ROOT / "protocol" / "build_constitutional_surface_report_from_snapshot.py",
        family="constitutional",
    ),
    Stage(
        name="Seam-lab snapshot",
        script_path=REPO_ROOT / "lab" / "build_seam_experiment_snapshot.py",
        family="seam-lab",
    ),
    Stage(
        name="Seam-lab report from snapshot",
        script_path=REPO_ROOT / "lab" / "build_seam_experiment_report_from_snapshot.py",
        family="seam-lab",
    ),
    Stage(
        name="Cross-carrier family snapshot",
        script_path=REPO_ROOT / "lab" / "build_cross_carrier_family_snapshot.py",
        family="cross-carrier",
    ),
    Stage(
        name="Cross-carrier family report",
        script_path=REPO_ROOT / "lab" / "build_cross_carrier_family_report.py",
        family="cross-carrier",
    ),
    Stage(
        name="Current top-level readability pointer",
        script_path=REPO_ROOT / "build_current_readability_surfaces.py",
        family="current-pointer",
    ),
)


def repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def print_stream(text: str, *, is_stderr: bool) -> None:
    if not text.strip():
        return

    target = sys.stderr if is_stderr else sys.stdout
    for line in text.rstrip().splitlines():
        print(f"  {line}", file=target)


def run_stage(stage: Stage, index: int, total: int) -> StageResult:
    if not stage.script_path.is_file():
        raise FileNotFoundError(f"Stage script is missing: {stage.script_path}")

    print(f"[{index}/{total}] Starting {stage.name}")
    print(f"  Family: {stage.family}")
    print(f"  Script: {repo_relative(stage.script_path)}")

    completed = subprocess.run(
        [sys.executable, str(stage.script_path)],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )

    result = StageResult(
        stage=stage,
        returncode=completed.returncode,
        stdout=completed.stdout,
        stderr=completed.stderr,
    )

    if result.stdout:
        print_stream(result.stdout, is_stderr=False)
    if result.stderr:
        print_stream(result.stderr, is_stderr=True)

    if result.returncode == 0:
        print(f"[{index}/{total}] Completed {stage.name}")
    else:
        print(
            f"[{index}/{total}] Failed {stage.name} with exit status {result.returncode}",
            file=sys.stderr,
        )

    return result


def refresh_all() -> int:
    completed_stages: List[Stage] = []
    total = len(STAGES)

    for index, stage in enumerate(STAGES, start=1):
        try:
            result = run_stage(stage, index, total)
        except FileNotFoundError as exc:
            print(str(exc), file=sys.stderr)
            return 1
        except OSError as exc:
            print(
                f"Failed to invoke stage {stage.name}: {exc}",
                file=sys.stderr,
            )
            return 1

        if result.returncode != 0:
            return result.returncode

        completed_stages.append(stage)

    print("")
    print("Current readability refresh completed.")
    for stage in completed_stages:
        print(f"- {stage.name}: completed")
    if CURRENT_POINTER_PATH.is_file():
        print(f"- Current pointer surface: {repo_relative(CURRENT_POINTER_PATH)}")
    else:
        print("- Current pointer surface: not found after refresh")
    print("- This is a readability refresh only. It does not carry protocol-law rank.")

    return 0


def main() -> int:
    return refresh_all()


if __name__ == "__main__":
    raise SystemExit(main())
