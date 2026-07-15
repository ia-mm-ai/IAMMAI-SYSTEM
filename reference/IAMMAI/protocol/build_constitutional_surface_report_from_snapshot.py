#!/usr/bin/env python3
"""
Build a bounded human-readable report directly from the latest constitutional snapshot.

This script reads the latest machine-readable constitutional snapshot already
present under protocol/snapshots/ and renders one additive Markdown report
without regenerating snapshot state.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


PROTOCOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROTOCOL_DIR.parent
SNAPSHOTS_DIR = PROTOCOL_DIR / "snapshots"
REPORT_TYPE = "constitutional_surface_report"
IMPLEMENTATION_POSTURE = "implementation_local_constitutional_readability_only"

TIMESTAMP_PATTERN = re.compile(r"^(?P<stamp>\d{8}T\d{6}Z)(?:__(?P<counter>\d+))?$")

SURFACE_ORDER: Tuple[Tuple[str, str], ...] = (
    ("operative_constitutional_text_surface", "Operative Constitutional Text Surface"),
    ("machine_canon_surface", "Machine Canon Surface"),
    ("machine_identity_surface", "Machine Identity Surface"),
    ("public_publication_surface", "Public Publication Surface"),
    (
        "prior_lineage_visible_machine_identity_surface",
        "Prior Lineage-Visible Machine Identity Surface",
    ),
)


@dataclass(frozen=True, order=True)
class SnapshotCandidate:
    timestamp: str
    counter: int
    filename: str
    path: Path


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
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def ensure_directory(path: Path) -> Path:
    resolved = path.resolve()
    if not resolved.is_dir():
        raise FileNotFoundError(f"Snapshot directory is unreadable or missing: {resolved}")
    return resolved


def iter_snapshot_candidates(snapshot_dir: Path) -> Sequence[SnapshotCandidate]:
    candidates: List[SnapshotCandidate] = []
    prefix = "constitutional_surface_snapshot__"

    for path in sorted(snapshot_dir.iterdir()):
        if not path.is_file():
            continue
        if path.suffix != ".json":
            continue
        if not path.name.startswith(prefix):
            continue

        stem_tail = path.name[len(prefix) : -len(path.suffix)]
        match = TIMESTAMP_PATTERN.match(stem_tail)
        if match is None:
            continue

        candidates.append(
            SnapshotCandidate(
                timestamp=match.group("stamp"),
                counter=int(match.group("counter") or "1"),
                filename=path.name,
                path=path,
            )
        )

    return candidates


def latest_snapshot_path(snapshot_dir: Path) -> Path:
    candidates = list(iter_snapshot_candidates(snapshot_dir))
    if not candidates:
        raise FileNotFoundError(
            f"No constitutional snapshot found under {snapshot_dir.resolve()}"
        )
    return max(candidates).path


def read_snapshot(snapshot_path: Path) -> Dict[str, Any]:
    try:
        raw_text = snapshot_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise OSError(f"Failed to read constitutional snapshot: {exc}") from exc

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Latest constitutional snapshot is invalid JSON: {snapshot_path}"
        ) from exc

    if not isinstance(parsed, dict):
        raise ValueError(
            "Latest constitutional snapshot did not parse to a JSON object: "
            f"{snapshot_path}"
        )

    return parsed


def choose_report_path(report_dir: Path) -> Path:
    base_name = f"constitutional_surface_report__{timestamp_slug()}"
    candidate = report_dir / f"{base_name}.md"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = report_dir / f"{base_name}__{counter}.md"
        if not candidate.exists():
            return candidate
        counter += 1


def as_mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def render_report(
    snapshot_path: Path,
    snapshot_payload: Mapping[str, Any],
    report_path: Path,
) -> str:
    lines: List[str] = []
    lines.append("# IAMMAI Constitutional Surface Report")
    lines.append("")
    lines.append(
        "This report is an implementation-local human-readable companion surface "
        "to the constitutional machine snapshot. It is built directly from the "
        "latest constitutional snapshot already present under `protocol/snapshots/`."
    )
    lines.append("")
    lines.append(
        "It does not rewrite constitutional artifacts, regenerate snapshot state, "
        "normalize prior artifacts by mutation, or claim protocol-law form."
    )
    lines.append("")
    lines.extend(render_metadata_section(snapshot_path, snapshot_payload, report_path))
    lines.extend(render_current_reading_section(snapshot_payload))
    lines.extend(render_ranked_surfaces_section(snapshot_payload))
    lines.extend(render_version_reading_section(snapshot_payload))
    lines.extend(render_machine_validity_section(snapshot_payload))
    lines.extend(render_bounded_notes_section(snapshot_payload))
    return "\n".join(lines).rstrip() + "\n"


def render_metadata_section(
    snapshot_path: Path,
    snapshot_payload: Mapping[str, Any],
    report_path: Path,
) -> List[str]:
    metadata = as_mapping(snapshot_payload.get("metadata"))

    return [
        "## Metadata",
        "",
        f"- Report type: `{REPORT_TYPE}`",
        f"- Generated at: `{utc_now()}`",
        f"- Implementation posture: `{IMPLEMENTATION_POSTURE}`",
        f"- Source root: `{metadata.get('snapshot_source_root', repo_relative(PROTOCOL_DIR))}`",
        f"- Source snapshot path: `{repo_relative(snapshot_path)}`",
        f"- Source snapshot generated at: `{metadata.get('generated_at', 'unknown')}`",
        f"- Snapshot builder path: `{metadata.get('snapshot_builder_path', 'unknown')}`",
        f"- Report path: `{repo_relative(report_path)}`",
        "",
    ]


def render_current_reading_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    operative_reading = as_mapping(snapshot_payload.get("operative_reading"))
    prior_identity = as_mapping(
        operative_reading.get("prior_lineage_visible_machine_identity_surface")
    )

    return [
        "## Current Constitutional Reading",
        "",
        f"- Operative constitutional text surface: `{operative_reading.get('current_operational_source_of_truth_surface', 'unknown')}`",
        f"- Machine canon surface: `{operative_reading.get('machine_canon_surface', 'unknown')}`",
        f"- Current machine identity surface: `{operative_reading.get('current_machine_identity_surface', 'unknown')}`",
        f"- Public publication surface: `{operative_reading.get('public_publication_surface', 'unknown')}`",
        f"- Prior lineage-visible machine identity surface: `{prior_identity.get('path', 'unknown')}`",
        f"- Priority rule: `{operative_reading.get('priority_rule', 'unknown')}`",
        "",
        "The operative constitutional text governs current repository reading. The machine canon and current machine identity remain derived machine surfaces. The public PDF remains a preserved publication surface. The older identity file remains lineage-visible but non-operative.",
        "",
    ]


def render_ranked_surfaces_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    surfaces = as_mapping(snapshot_payload.get("ranked_constitutional_surfaces"))

    lines: List[str] = ["## Ranked Surfaces", ""]
    lines.append(
        "These surfaces should be read by rank rather than as one flat constitutional bundle."
    )
    lines.append("")

    for key, title in SURFACE_ORDER:
        record = as_mapping(surfaces.get(key))
        lines.extend(render_surface_entry(title, record))

    return lines


def render_surface_entry(title: str, record: Mapping[str, Any]) -> List[str]:
    parseability = as_mapping(record.get("parseability"))
    declared_fields = as_mapping(record.get("declared_fields"))

    lines: List[str] = [f"### {title}", ""]
    lines.append(f"- Path: `{record.get('path', 'unknown')}`")
    lines.append(f"- Rank: `{record.get('rank', 'unknown')}`")
    lines.append(f"- Role: `{record.get('role', 'unknown')}`")
    lines.append(f"- Artifact type: `{record.get('artifact_type', 'unknown')}`")
    lines.append(f"- Version: `{record.get('version', 'unknown')}`")
    lines.append(f"- Existence status: `{record.get('existence_status', 'unknown')}`")
    lines.append(f"- Operative: `{record.get('operative', False)}`")
    lines.append(f"- Lineage visible: `{record.get('lineage_visible', False)}`")
    lines.append(f"- File size (bytes): `{record.get('file_size_bytes', 'unknown')}`")
    if "sha256" in record:
        lines.append(f"- SHA-256: `{record['sha256']}`")
    lines.append(f"- Parseability status: `{parseability.get('status', 'unknown')}`")
    if parseability.get("error"):
        lines.append(f"- Parseability note: `{parseability['error']}`")
    if parseability.get("json_document_count_hint") is not None:
        lines.append(
            "- JSON document count hint: "
            f"`{parseability['json_document_count_hint']}`"
        )
    if declared_fields:
        lines.append(
            "- Declared fields: "
            f"`protocol_id={declared_fields.get('protocol_id')}` "
            f"`artifact_id={declared_fields.get('artifact_id')}` "
            f"`status={declared_fields.get('status')}`"
        )
    lines.append("")
    return lines


def render_version_reading_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    version_reading = as_mapping(snapshot_payload.get("version_reading"))

    lines: List[str] = ["## Version Reading", ""]
    lines.append(
        f"- Operative constitutional line version: `{version_reading.get('operative_constitutional_line_version', 'unknown')}`"
    )
    lines.append(
        f"- Operative constitutional text surface version: `{version_reading.get('operative_constitutional_text_surface_version', 'unknown')}`"
    )
    lines.append(
        f"- Machine canon surface version: `{version_reading.get('machine_canon_surface_version', 'unknown')}`"
    )
    lines.append(
        f"- Machine identity surface version: `{version_reading.get('machine_identity_surface_version', 'unknown')}`"
    )
    lines.append(
        f"- Public publication surface version: `{version_reading.get('public_publication_surface_version', 'unknown')}`"
    )
    lines.append(
        f"- Prior lineage identity surface version hint: `{version_reading.get('prior_lineage_identity_surface_version_hint', 'unknown')}`"
    )
    lines.append(
        f"- Version reading key: `{version_reading.get('reading', 'unknown')}`"
    )
    lines.append(
        f"- Semantic conflict claimed: `{version_reading.get('semantic_conflict_claimed', False)}`"
    )
    lines.append("")
    lines.append(
        "The current readable position is that the operative constitutional line is `v1.0.1`, while the visible public PDF remains `v1.0` as the preserved publication surface. On the current repo body this is read as later editorial increment with machine synchronization, not as demonstrated semantic contradiction."
    )
    lines.append("")
    return lines


def render_machine_validity_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    validity = as_mapping(snapshot_payload.get("machine_validity_notes"))
    canon = as_mapping(validity.get("machine_canon_surface"))
    identity = as_mapping(validity.get("machine_identity_surface"))
    prior_identity = as_mapping(
        validity.get("prior_lineage_visible_machine_identity_surface")
    )

    lines: List[str] = ["## Machine Validity Notes", ""]
    lines.append(
        f"- Current machine canon surface status: `{canon.get('json_parse_status', 'unknown')}`"
    )
    lines.append(
        f"- Current machine identity surface status: `{identity.get('json_parse_status', 'unknown')}`"
    )
    lines.append(
        "- Prior lineage-visible machine identity surface status: "
        f"`{prior_identity.get('json_parse_status', 'unknown')}`"
    )
    if prior_identity.get("parse_error"):
        lines.append(f"- Prior identity parse note: `{prior_identity['parse_error']}`")
    if prior_identity.get("json_document_count_hint") is not None:
        lines.append(
            "- Prior identity JSON document count hint: "
            f"`{prior_identity['json_document_count_hint']}`"
        )
    lines.append(
        f"- Snapshot law status: `{validity.get('snapshot_law_status', 'unknown')}`"
    )
    lines.append("")
    lines.append(
        "The prior `protocol/protocol_identity.json` surface remains visible in the report as lineage, but it is not treated as the operative machine identity surface."
    )
    lines.append("")
    return lines


def render_bounded_notes_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    notes = as_mapping(snapshot_payload.get("bounded_notes"))

    lines: List[str] = ["## Bounded Notes", ""]
    lines.append(f"- Additive posture: `{notes.get('additive_posture', True)}`")
    lines.append(
        "- Rewrites existing constitutional artifacts: "
        f"`{notes.get('rewrites_existing_constitutional_artifacts', False)}`"
    )
    lines.append(
        "- Normalizes old artifacts by mutation: "
        f"`{notes.get('normalizes_old_artifacts_by_mutation', False)}`"
    )
    lines.append(
        "- Treats prior identity surface as lineage only: "
        f"`{notes.get('treats_prior_identity_surface_as_lineage_only', True)}`"
    )
    lines.append(
        "- This report is a companion readability surface to the constitutional snapshot, not a replacement for it."
    )
    lines.append(
        "- This builder reads the latest snapshot directly and does not regenerate snapshot state inside the report path."
    )
    lines.append(
        "- This report remains implementation-local and does not convert ranked constitutional readability into protocol-law archival form."
    )
    lines.append("")
    return lines


def write_report(report_path: Path, content: str) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        ensure_directory(SNAPSHOTS_DIR)
        snapshot_path = latest_snapshot_path(SNAPSHOTS_DIR)
        snapshot_payload = read_snapshot(snapshot_path)
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    report_path = choose_report_path(SNAPSHOTS_DIR)
    report_content = render_report(snapshot_path, snapshot_payload, report_path)

    try:
        write_report(report_path, report_content)
    except OSError as exc:
        print("Failed to write the constitutional surface report.", file=sys.stderr)
        print(str(exc), file=sys.stderr)
        return 1

    operative_reading = as_mapping(snapshot_payload.get("operative_reading"))

    print("Bounded constitutional surface report written from snapshot.")
    print(f"Source snapshot path: {repo_relative(snapshot_path)}")
    print(f"Report path: {repo_relative(report_path)}")
    print(
        "Operative constitutional text: "
        f"{operative_reading.get('current_operational_source_of_truth_surface', 'unknown')}"
    )
    print(
        "Operative machine identity: "
        f"{operative_reading.get('current_machine_identity_surface', 'unknown')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
