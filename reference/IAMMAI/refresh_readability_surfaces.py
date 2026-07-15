#!/usr/bin/env python3
"""
Refresh the repository readability surfaces in bounded stage order.

This script orchestrates the existing readability builders without duplicating
their logic. It refreshes proof/archive readability, constitutional
readability, and the latest top-level pointer surface in the correct order.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List, Sequence


REPO_ROOT = Path(__file__).resolve().parent
LATEST_POINTER_PATH = REPO_ROOT / "LATEST_READABILITY_SURFACES.md"


@dataclass(frozen=True)
class RefreshStage:
    name: str
    script_path: Path
    rank: str


STAGES: Sequence[RefreshStage] = (
    RefreshStage(
        name="Run lineage snapshot",
        script_path=REPO_ROOT / "v1" / "embodiment" / "run" / "build_run_lineage_snapshot.py",
        rank="proof/archive readability",
    ),
    RefreshStage(
        name="Run lineage report",
        script_path=REPO_ROOT / "v1" / "embodiment" / "run" / "build_run_lineage_report.py",
        rank="proof/archive readability",
    ),
    RefreshStage(
        name="Constitutional surface snapshot",
        script_path=REPO_ROOT / "protocol" / "build_constitutional_surface_snapshot.py",
        rank="constitutional readability",
    ),
    RefreshStage(
        name="Constitutional surface report",
        script_path=REPO_ROOT / "protocol" / "build_constitutional_surface_report.py",
        rank="constitutional readability",
    ),
    RefreshStage(
        name="Latest readability pointer",
        script_path=REPO_ROOT / "build_latest_readability_surfaces.py",
        rank="latest pointer surface",
    ),
)


def repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def ensure_stage_scripts_exist(stages: Sequence[RefreshStage]) -> None:
    missing = [stage for stage in stages if not stage.script_path.is_file()]
    if not missing:
        return

    missing_lines = ", ".join(repo_relative(stage.script_path) for stage in missing)
    raise FileNotFoundError(f"Missing readability builder script(s): {missing_lines}")


def run_stage(stage: RefreshStage) -> None:
    print(f"[start] {stage.name} ({stage.rank})")

    completed = subprocess.run(
        [sys.executable, str(stage.script_path)],
        cwd=REPO_ROOT,
        check=False,
    )

    if completed.returncode != 0:
        raise RuntimeError(
            f"{stage.name} failed with exit status {completed.returncode}."
        )

    print(f"[done] {stage.name}")


def build_success_summary(completed_stages: Sequence[RefreshStage]) -> List[str]:
    lines = [
        "Readability refresh completed.",
        "Stages completed:",
    ]

    for stage in completed_stages:
        lines.append(f"- {stage.name}: completed")

    lines.append(
        "Latest pointer surface: "
        f"{repo_relative(LATEST_POINTER_PATH) if LATEST_POINTER_PATH.is_file() else 'not found'}"
    )
    lines.append(
        "This refresh preserves readability coherence only. It does not create protocol law."
    )
    return lines


def main() -> int:
    try:
        ensure_stage_scripts_exist(STAGES)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    completed_stages: List[RefreshStage] = []

    for stage in STAGES:
        try:
            run_stage(stage)
        except RuntimeError as exc:
            print(
                f"[failed] {stage.name}: {exc}",
                file=sys.stderr,
            )
            return 1
        completed_stages.append(stage)

    for line in build_success_summary(completed_stages):
        print(line)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
