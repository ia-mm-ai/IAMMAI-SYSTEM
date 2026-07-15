#!/usr/bin/env python3
"""
Build a bounded human-readable report for the constitutional surface snapshot.

This script reuses the constitutional snapshot builder as the machine-readable
source of truth, writes a fresh snapshot, and then renders one additive
Markdown report under protocol/snapshots/.
"""

from __future__ import annotations

import importlib.util
import sys
from datetime import datetime, timezone
from pathlib import Path
from types import ModuleType
from typing import Any, Dict, List, Mapping, Tuple


PROTOCOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROTOCOL_DIR.parent
SNAPSHOTS_DIR = PROTOCOL_DIR / "snapshots"
REPORT_TYPE = "constitutional_surface_report"
IMPLEMENTATION_POSTURE = "implementation_local_constitutional_readability_only"
SNAPSHOT_BUILDER_PATH = PROTOCOL_DIR / "build_constitutional_surface_snapshot.py"


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


def load_snapshot_builder_module() -> ModuleType:
    try:
        import build_constitutional_surface_snapshot as snapshot_builder  # type: ignore

        return snapshot_builder
    except ImportError:
        spec = importlib.util.spec_from_file_location(
            "build_constitutional_surface_snapshot",
            SNAPSHOT_BUILDER_PATH,
        )
        if spec is None or spec.loader is None:
            raise ImportError(
                "Could not load the constitutional snapshot builder module."
            )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        return module


def build_fresh_snapshot(snapshot_builder: ModuleType) -> Tuple[Path, Dict[str, Any]]:
    try:
        specs = (
            snapshot_builder.OPERATIVE_TEXT_SPEC,
            snapshot_builder.CANON_SPEC,
            snapshot_builder.IDENTITY_SPEC,
            snapshot_builder.PUBLICATION_SPEC,
            snapshot_builder.OLD_IDENTITY_SPEC,
        )
    except AttributeError as exc:
        raise RuntimeError(
            "The constitutional snapshot builder does not expose the expected surface specs."
        ) from exc

    surfaces: Dict[str, Dict[str, Any]] = {}
    parsed_json_surfaces: Dict[str, Dict[str, Any]] = {}

    for spec in specs:
        record, parsed_json = snapshot_builder.inspect_surface(spec)
        surfaces[spec.key] = record
        if parsed_json is not None:
            parsed_json_surfaces[spec.key] = parsed_json

    if parsed_json_surfaces.get(snapshot_builder.CANON_SPEC.key) is None:
        raise RuntimeError(
            "Required machine canon surface did not parse as single-document JSON."
        )

    identity_data = parsed_json_surfaces.get(snapshot_builder.IDENTITY_SPEC.key)
    if identity_data is None:
        raise RuntimeError(
            "Required machine identity surface did not parse as single-document JSON."
        )

    snapshot_path = snapshot_builder.choose_snapshot_path(snapshot_builder.SNAPSHOTS_DIR)
    payload = snapshot_builder.build_snapshot_payload(snapshot_path, surfaces, identity_data)
    snapshot_builder.write_snapshot(snapshot_path, payload)
    return snapshot_path, payload


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
        "to the constitutional machine snapshot. It does not rewrite constitutional "
        "artifacts, normalize prior artifacts by mutation, or claim protocol-law form."
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
    metadata = snapshot_payload.get("metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}

    return [
        "## Metadata",
        "",
        f"- Report type: `{REPORT_TYPE}`",
        f"- Generated at: `{utc_now()}`",
        f"- Implementation posture: `{IMPLEMENTATION_POSTURE}`",
        f"- Source root: `{metadata.get('snapshot_source_root', repo_relative(PROTOCOL_DIR))}`",
        f"- Source snapshot path: `{repo_relative(snapshot_path)}`",
        f"- Source snapshot generated at: `{metadata.get('generated_at', 'unknown')}`",
        f"- Snapshot builder path: `{metadata.get('snapshot_builder_path', repo_relative(SNAPSHOT_BUILDER_PATH))}`",
        f"- Report path: `{repo_relative(report_path)}`",
        "",
    ]


def render_current_reading_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    operative_reading = snapshot_payload.get("operative_reading", {})
    if not isinstance(operative_reading, Mapping):
        operative_reading = {}

    prior_identity = operative_reading.get("prior_lineage_visible_machine_identity_surface")
    if not isinstance(prior_identity, Mapping):
        prior_identity = {}

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
    surfaces = snapshot_payload.get("ranked_constitutional_surfaces", {})
    if not isinstance(surfaces, Mapping):
        surfaces = {}

    lines: List[str] = ["## Ranked Surfaces", ""]
    lines.append(
        "These surfaces should be read by rank rather than as one flat constitutional bundle."
    )
    lines.append("")

    for key, title in SURFACE_ORDER:
        record = surfaces.get(key, {})
        if not isinstance(record, Mapping):
            record = {}
        lines.extend(render_surface_entry(title, record))

    return lines


def render_surface_entry(title: str, record: Mapping[str, Any]) -> List[str]:
    parseability = record.get("parseability", {})
    if not isinstance(parseability, Mapping):
        parseability = {}

    declared_fields = record.get("declared_fields", {})
    if not isinstance(declared_fields, Mapping):
        declared_fields = {}

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
    lines.append(
        f"- Parseability status: `{parseability.get('status', 'unknown')}`"
    )
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
    version_reading = snapshot_payload.get("version_reading", {})
    if not isinstance(version_reading, Mapping):
        version_reading = {}

    semantic_conflict = version_reading.get("semantic_conflict_claimed", False)

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
        f"- Semantic conflict claimed: `{semantic_conflict}`"
    )
    lines.append("")
    lines.append(
        "The current readable position is that the operative constitutional line is `v1.0.1`, while the visible public PDF remains `v1.0` as the preserved publication surface. On the current repo body this is read as later editorial increment with machine synchronization, not as demonstrated semantic contradiction."
    )
    lines.append("")
    return lines


def render_machine_validity_section(snapshot_payload: Mapping[str, Any]) -> List[str]:
    validity = snapshot_payload.get("machine_validity_notes", {})
    if not isinstance(validity, Mapping):
        validity = {}

    canon = validity.get("machine_canon_surface", {})
    identity = validity.get("machine_identity_surface", {})
    prior_identity = validity.get("prior_lineage_visible_machine_identity_surface", {})

    if not isinstance(canon, Mapping):
        canon = {}
    if not isinstance(identity, Mapping):
        identity = {}
    if not isinstance(prior_identity, Mapping):
        prior_identity = {}

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
        lines.append(
            f"- Prior identity parse note: `{prior_identity['parse_error']}`"
        )
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
    notes = snapshot_payload.get("bounded_notes", {})
    if not isinstance(notes, Mapping):
        notes = {}

    lines: List[str] = ["## Bounded Notes", ""]
    lines.append(
        f"- Additive posture: `{notes.get('additive_posture', True)}`"
    )
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
        "- This report remains implementation-local and does not convert ranked constitutional readability into protocol-law archival form."
    )
    lines.append("")
    return lines


def write_report(report_path: Path, content: str) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(content, encoding="utf-8")


def main() -> int:
    try:
        snapshot_builder = load_snapshot_builder_module()
    except ImportError as exc:
        print(
            "Failed to import the constitutional snapshot builder.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    try:
        snapshot_path, snapshot_payload = build_fresh_snapshot(snapshot_builder)
    except Exception as exc:
        print(
            "Failed to build the constitutional surface snapshot for report rendering.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    report_path = choose_report_path(SNAPSHOTS_DIR)
    report_content = render_report(snapshot_path, snapshot_payload, report_path)

    try:
        write_report(report_path, report_content)
    except OSError as exc:
        print(
            "Failed to write the constitutional surface report.",
            file=sys.stderr,
        )
        print(str(exc), file=sys.stderr)
        return 1

    validity = snapshot_payload.get("machine_validity_notes", {})
    if not isinstance(validity, Mapping):
        validity = {}
    prior_identity = validity.get("prior_lineage_visible_machine_identity_surface", {})
    if not isinstance(prior_identity, Mapping):
        prior_identity = {}

    print("Bounded constitutional surface report written.")
    print(f"Report path: {repo_relative(report_path)}")
    print(f"Source snapshot path: {repo_relative(snapshot_path)}")
    print(
        "Operative constitutional text: "
        f"{snapshot_payload['operative_reading']['current_operational_source_of_truth_surface']}"
    )
    print(
        "Operative machine identity: "
        f"{snapshot_payload['operative_reading']['current_machine_identity_surface']}"
    )
    print(
        "Old lineage identity parse status: "
        f"{prior_identity.get('json_parse_status', 'unknown')}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
