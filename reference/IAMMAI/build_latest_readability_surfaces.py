#!/usr/bin/env python3
"""
Build one convenience pointer for the latest readability surfaces.

This script inspects the proof/archive and constitutional snapshot directories,
selects the latest matching artifacts by timestamped filename, and writes one
additive top-level Markdown pointer without modifying older artifacts.
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, Optional, Sequence, Tuple


REPO_ROOT = Path(__file__).resolve().parent
POINTER_PATH = REPO_ROOT / "LATEST_READABILITY_SURFACES.md"
PROOF_SNAPSHOTS_DIR = REPO_ROOT / "v1" / "registry" / "snapshots"
CONSTITUTIONAL_SNAPSHOTS_DIR = REPO_ROOT / "protocol" / "snapshots"


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
    prefix: str
    extension: str
    directory: Path


PROOF_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Run lineage snapshot",
        prefix="run_lineage_snapshot",
        extension=".json",
        directory=PROOF_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Run lineage report",
        prefix="run_lineage_report",
        extension=".md",
        directory=PROOF_SNAPSHOTS_DIR,
    ),
)

CONSTITUTIONAL_FAMILIES: Tuple[ArtifactFamily, ...] = (
    ArtifactFamily(
        label="Constitutional surface snapshot",
        prefix="constitutional_surface_snapshot",
        extension=".json",
        directory=CONSTITUTIONAL_SNAPSHOTS_DIR,
    ),
    ArtifactFamily(
        label="Constitutional surface report",
        prefix="constitutional_surface_report",
        extension=".md",
        directory=CONSTITUTIONAL_SNAPSHOTS_DIR,
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


def iter_candidates(family: ArtifactFamily) -> Iterable[ArtifactCandidate]:
    prefix = f"{family.prefix}__"

    for path in sorted(family.directory.iterdir()):
        if not path.is_file():
            continue
        if path.suffix != family.extension:
            continue
        if not path.name.startswith(prefix):
            continue

        stem_tail = path.name[len(prefix) : -len(family.extension)]
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
) -> str:
    lines = [
        "# Latest Readability Surfaces",
        "",
        "## A. Purpose",
        "",
        "This file is a convenience pointer surface for the latest readability artifacts on both the proof/archive side and the constitutional side.",
        "",
        "It does not rewrite older snapshot or report files, does not replace earlier entry or index surfaces, and does not claim protocol-law rank. It exists only to make the current readability artifacts easier to find.",
        "",
        "## B. Latest Proof/Archive Readability Surfaces",
        "",
        render_family_entry(PROOF_FAMILIES[0], proof_latest[PROOF_FAMILIES[0].label]),
        render_family_entry(PROOF_FAMILIES[1], proof_latest[PROOF_FAMILIES[1].label]),
        "",
        "## C. Latest Constitutional Readability Surfaces",
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
        "## D. Reading Note",
        "",
        "These are latest convenience pointers selected by timestamped filename in the current snapshot directories.",
        "",
        "Older timestamped artifacts remain lineage. This file does not replace ranked surfaces, earlier snapshot/report artifacts, or the entry and index surfaces that explain how the repository should be read.",
        "",
        "## E. Generated At",
        "",
        f"- Generated at: `{utc_now()}`",
        f"- Proof/archive snapshot directory: `{repo_relative(PROOF_SNAPSHOTS_DIR)}`",
        f"- Constitutional snapshot directory: `{repo_relative(CONSTITUTIONAL_SNAPSHOTS_DIR)}`",
        "",
    ]
    return "\n".join(lines)


def write_pointer(content: str) -> None:
    POINTER_PATH.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        ensure_directory(PROOF_SNAPSHOTS_DIR)
        ensure_directory(CONSTITUTIONAL_SNAPSHOTS_DIR)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    proof_latest = gather_latest_by_family(PROOF_FAMILIES)
    constitutional_latest = gather_latest_by_family(CONSTITUTIONAL_FAMILIES)
    content = build_pointer_markdown(proof_latest, constitutional_latest)

    try:
        write_pointer(content)
    except OSError as exc:
        print(f"Failed to write {POINTER_PATH.name}: {exc}", file=sys.stderr)
        return 1

    print("Latest readability pointer written.")
    print(f"Pointer path: {repo_relative(POINTER_PATH)}")

    proof_snapshot = proof_latest[PROOF_FAMILIES[0].label]
    proof_report = proof_latest[PROOF_FAMILIES[1].label]
    constitutional_snapshot = constitutional_latest[CONSTITUTIONAL_FAMILIES[0].label]
    constitutional_report = constitutional_latest[CONSTITUTIONAL_FAMILIES[1].label]

    print(
        "Latest proof/archive snapshot: "
        f"{repo_relative(proof_snapshot.path) if proof_snapshot else 'not found'}"
    )
    print(
        "Latest proof/archive report: "
        f"{repo_relative(proof_report.path) if proof_report else 'not found'}"
    )
    print(
        "Latest constitutional snapshot: "
        f"{repo_relative(constitutional_snapshot.path) if constitutional_snapshot else 'not found'}"
    )
    print(
        "Latest constitutional report: "
        f"{repo_relative(constitutional_report.path) if constitutional_report else 'not found'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
