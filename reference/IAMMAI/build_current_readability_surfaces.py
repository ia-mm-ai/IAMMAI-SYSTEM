#!/usr/bin/env python3
"""
Build one current convenience pointer for the standing readability surfaces.

This script inspects the proof/archive, constitutional, seam-lab, and
cross-carrier snapshot directories, selects the latest matching artifacts by
timestamped filename, and writes one additive top-level Markdown pointer
without modifying older artifacts.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parent
POINTER_PATH = REPO_ROOT / "CURRENT_READABILITY_SURFACES.md"

PROOF_SNAPSHOTS_DIR = REPO_ROOT / "v1" / "registry" / "snapshots"
CONSTITUTIONAL_SNAPSHOTS_DIR = REPO_ROOT / "protocol" / "snapshots"
LAB_SNAPSHOTS_DIR = REPO_ROOT / "lab" / "snapshots"

TIMESTAMP_PATTERN = re.compile(r"^(?P<stamp>\d{8}T\d{6}Z)(?:__(?P<counter>\d+))?$")


@dataclass(frozen=True, order=True)
class ArtifactCandidate:
    timestamp: str
    counter: int
    filename: str
    path: Path


@dataclass(frozen=True)
class ArtifactFamily:
    label: str
    prefixes: Tuple[str, ...]
    extension: str
    directory: Path


PROOF_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Run lineage snapshot",
        prefixes=("run_lineage_snapshot",),
        extension=".json",
        directory=PROOF_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Run lineage report",
        prefixes=("run_lineage_report",),
        extension=".md",
        directory=PROOF_SNAPSHOTS_DIR,
    ),
)

CONSTITUTIONAL_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Constitutional surface snapshot",
        prefixes=("constitutional_surface_snapshot",),
        extension=".json",
        directory=CONSTITUTIONAL_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Constitutional surface report",
        prefixes=("constitutional_surface_report",),
        extension=".md",
        directory=CONSTITUTIONAL_SNAPSHOTS_DIR,
    ),
)

SEAM_LAB_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Seam experiment snapshot",
        prefixes=("seam_experiment_snapshot",),
        extension=".json",
        directory=LAB_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Seam experiment report",
        prefixes=("seam_experiment_report",),
        extension=".md",
        directory=LAB_SNAPSHOTS_DIR,
    ),
)

CROSS_CARRIER_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Cross-carrier family snapshot",
        prefixes=("cross_carrier_family_snapshot",),
        extension=".json",
        directory=LAB_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Cross-carrier family report",
        prefixes=(
            "cross_carrier_family_report",
            "cross_carrier_proof_family_report",
        ),
        extension=".md",
        directory=LAB_SNAPSHOTS_DIR,
    ),
)


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


def ensure_directory(path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Snapshot directory is unreadable or missing: {resolved}")
    return resolved


def matching_prefix(filename: str, family: ArtifactFamily) -> Optional[str]:
    for prefix in family.prefixes:
        expected_prefix = f"{prefix}__"
        if filename.startswith(expected_prefix) and filename.endswith(family.extension):
            return prefix
    return None


def iter_candidates(family: ArtifactFamily) -> Iterable[ArtifactCandidate]:
    for path in sorted(family.directory.iterdir()):
        if not path.is_file():
            continue

        prefix = matching_prefix(path.name, family)
        if prefix is None:
            continue

        stem_tail = path.name[len(prefix) + 2 : -len(family.extension)]
        match = TIMESTAMP_PATTERN.match(stem_tail)
        if match is None:
            continue

        counter = int(match.group("counter") or "1")
        yield ArtifactCandidate(
            timestamp=match.group("stamp"),
            counter=counter,
            filename=path.name,
            path=path,
        )


def latest_candidate(family: ArtifactFamily) -> Optional[ArtifactCandidate]:
    candidates = list(iter_candidates(family))
    if not candidates:
        return None
    return max(candidates)


def gather_latest_by_family(
    families: Sequence[ArtifactFamily],
) -> Dict[str, Optional[ArtifactCandidate]]:
    latest: Dict[str, Optional[ArtifactCandidate]] = {}
    for family in families:
        latest[family.label] = latest_candidate(family)
    return latest


def render_family_entry(
    family: ArtifactFamily,
    candidate: Optional[ArtifactCandidate],
) -> str:
    if candidate is None:
        return (
            f"- {family.label}: not found in "
            f"`{repo_relative(family.directory)}`."
        )

    return (
        f"- {family.label}: "
        f"`{repo_relative(candidate.path)}` "
        f"(timestamp `{candidate.timestamp}`, filename `{candidate.filename}`)"
    )


def build_pointer_markdown(
    proof_latest: Dict[str, Optional[ArtifactCandidate]],
    constitutional_latest: Dict[str, Optional[ArtifactCandidate]],
    seam_lab_latest: Dict[str, Optional[ArtifactCandidate]],
    cross_carrier_latest: Dict[str, Optional[ArtifactCandidate]],
) -> str:
    lines = [
        "# Current Readability Surfaces",
        "",
        "## A. Purpose",
        "",
        "This file is a current convenience pointer surface for the latest readability artifacts now standing across the proof/archive, constitutional, seam-lab family, and cross-carrier family readability lines.",
        "",
        "It does not rewrite `LATEST_READABILITY_SURFACES.md`, does not rewrite older snapshot or report files, does not flatten all readable surfaces into one unranked bundle, and does not claim protocol-law rank. It exists only to make the current readability artifacts easier to find.",
        "",
        "This file is additive. It does not replace `LATEST_READABILITY_SURFACES.md`.",
        "",
        "## B. Current Proof/Archive Readability Surfaces",
        "",
        render_family_entry(PROOF_FAMILIES[0], proof_latest[PROOF_FAMILIES[0].label]),
        render_family_entry(PROOF_FAMILIES[1], proof_latest[PROOF_FAMILIES[1].label]),
        "",
        "## C. Current Constitutional Readability Surfaces",
        "",
        render_family_entry(
            CONSTITUTIONAL_FAMILIES[0],
            constitutional_latest[CONSTITUTIONAL_FAMILIES[0].label],
        ),
        render_family_entry(
            CONSTITUTIONAL_FAMILIES[1],
            constitutional_latest[CONSTITUTIONAL_FAMILIES[1].label],
        ),
        "",
        "## D. Current Seam-Lab Readability Surfaces",
        "",
        render_family_entry(
            SEAM_LAB_FAMILIES[0],
            seam_lab_latest[SEAM_LAB_FAMILIES[0].label],
        ),
        render_family_entry(
            SEAM_LAB_FAMILIES[1],
            seam_lab_latest[SEAM_LAB_FAMILIES[1].label],
        ),
        "",
        "## E. Current Cross-Carrier Readability Surfaces",
        "",
        render_family_entry(
            CROSS_CARRIER_FAMILIES[0],
            cross_carrier_latest[CROSS_CARRIER_FAMILIES[0].label],
        ),
        render_family_entry(
            CROSS_CARRIER_FAMILIES[1],
            cross_carrier_latest[CROSS_CARRIER_FAMILIES[1].label],
        ),
        "",
        "## F. Reading Note",
        "",
        "These are current convenience pointers selected by explicit timestamped filename matching in the current snapshot directories.",
        "",
        "Older timestamped artifacts remain lineage. `LATEST_READABILITY_SURFACES.md` remains standing as an earlier readability aid. This file does not replace ranked surfaces, earlier pointer surfaces, or earlier snapshot/report artifacts.",
        "",
        "## G. Generated At",
        "",
        f"- Generated at: `{utc_now()}`",
        f"- Proof/archive snapshot directory: `{repo_relative(PROOF_SNAPSHOTS_DIR)}`",
        f"- Constitutional snapshot directory: `{repo_relative(CONSTITUTIONAL_SNAPSHOTS_DIR)}`",
        f"- Lab snapshot directory: `{repo_relative(LAB_SNAPSHOTS_DIR)}`",
        "",
    ]
    return "\n".join(lines)


def write_pointer(content: str) -> None:
    POINTER_PATH.write_text(content, encoding="utf-8")


def print_family_summary(
    family: ArtifactFamily,
    candidate: Optional[ArtifactCandidate],
) -> None:
    print(
        f"{family.label}: "
        f"{repo_relative(candidate.path) if candidate is not None else 'not found'}"
    )


def main() -> int:
    try:
        ensure_directory(PROOF_SNAPSHOTS_DIR)
        ensure_directory(CONSTITUTIONAL_SNAPSHOTS_DIR)
        ensure_directory(LAB_SNAPSHOTS_DIR)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    proof_latest = gather_latest_by_family(PROOF_FAMILIES)
    constitutional_latest = gather_latest_by_family(CONSTITUTIONAL_FAMILIES)
    seam_lab_latest = gather_latest_by_family(SEAM_LAB_FAMILIES)
    cross_carrier_latest = gather_latest_by_family(CROSS_CARRIER_FAMILIES)
    content = build_pointer_markdown(
        proof_latest,
        constitutional_latest,
        seam_lab_latest,
        cross_carrier_latest,
    )

    try:
        write_pointer(content)
    except OSError as exc:
        print(f"Failed to write {POINTER_PATH.name}: {exc}", file=sys.stderr)
        return 1

    print("Current readability pointer written.")
    print(f"Pointer path: {repo_relative(POINTER_PATH)}")
    print_family_summary(PROOF_FAMILIES[0], proof_latest[PROOF_FAMILIES[0].label])
    print_family_summary(PROOF_FAMILIES[1], proof_latest[PROOF_FAMILIES[1].label])
    print_family_summary(
        CONSTITUTIONAL_FAMILIES[0],
        constitutional_latest[CONSTITUTIONAL_FAMILIES[0].label],
    )
    print_family_summary(
        CONSTITUTIONAL_FAMILIES[1],
        constitutional_latest[CONSTITUTIONAL_FAMILIES[1].label],
    )
    print_family_summary(
        SEAM_LAB_FAMILIES[0],
        seam_lab_latest[SEAM_LAB_FAMILIES[0].label],
    )
    print_family_summary(
        SEAM_LAB_FAMILIES[1],
        seam_lab_latest[SEAM_LAB_FAMILIES[1].label],
    )
    print_family_summary(
        CROSS_CARRIER_FAMILIES[0],
        cross_carrier_latest[CROSS_CARRIER_FAMILIES[0].label],
    )
    print_family_summary(
        CROSS_CARRIER_FAMILIES[1],
        cross_carrier_latest[CROSS_CARRIER_FAMILIES[1].label],
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
