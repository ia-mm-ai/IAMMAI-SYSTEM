#!/usr/bin/env python3
"""
Build a bounded machine-readable snapshot of the visible constitutional surfaces.

This script reads the current ranked constitutional surfaces, keeps older lineage
artifacts visible without treating them as operative, and writes one additive
snapshot under protocol/snapshots/.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Mapping, Optional, Tuple


PROTOCOL_DIR = Path(__file__).resolve().parent
REPO_ROOT = PROTOCOL_DIR.parent
SNAPSHOTS_DIR = PROTOCOL_DIR / "snapshots"
SNAPSHOT_TYPE = "constitutional_surface_snapshot"
IMPLEMENTATION_POSTURE = "implementation_local_constitutional_readability_only"


@dataclass(frozen=True)
class SurfaceSpec:
    key: str
    path: Path
    surface_type: str
    rank: int
    role: str
    artifact_type: str
    required: bool
    parse_mode: str
    operative: bool
    lineage_visible: bool


OPERATIVE_TEXT_SPEC = SurfaceSpec(
    key="operative_constitutional_text_surface",
    path=PROTOCOL_DIR / "IAMMAI_Constitutional_Integrity_Protocol_v1.0.1.md",
    surface_type="operative_constitutional_text_surface",
    rank=1,
    role="current_operative_constitutional_text_source",
    artifact_type="HUMAN_CONSTITUTIONAL_TEXT",
    required=True,
    parse_mode="text",
    operative=True,
    lineage_visible=True,
)

CANON_SPEC = SurfaceSpec(
    key="machine_canon_surface",
    path=PROTOCOL_DIR / "canon.json",
    surface_type="machine_canon_surface",
    rank=2,
    role="derived_machine_canon_surface",
    artifact_type="CONSTITUTIONAL_MACHINE_CANON",
    required=True,
    parse_mode="json",
    operative=True,
    lineage_visible=True,
)

IDENTITY_SPEC = SurfaceSpec(
    key="machine_identity_surface",
    path=PROTOCOL_DIR / "protocol_identity.v1.0.1.json",
    surface_type="machine_identity_surface",
    rank=3,
    role="current_machine_identity_surface",
    artifact_type="CONSTITUTIONAL_MACHINE_IDENTITY",
    required=True,
    parse_mode="json",
    operative=True,
    lineage_visible=True,
)

PUBLICATION_SPEC = SurfaceSpec(
    key="public_publication_surface",
    path=PROTOCOL_DIR / "IAMMAI_Public_Constitutional_Protocol_v1.0.pdf",
    surface_type="public_publication_surface",
    rank=4,
    role="preserved_public_constitutional_publication_surface",
    artifact_type="PUBLIC_CONSTITUTIONAL_PUBLICATION",
    required=True,
    parse_mode="binary",
    operative=False,
    lineage_visible=True,
)

OLD_IDENTITY_SPEC = SurfaceSpec(
    key="prior_lineage_visible_machine_identity_surface",
    path=PROTOCOL_DIR / "protocol_identity.json",
    surface_type="prior_lineage_visible_machine_identity_surface",
    rank=5,
    role="lineage_visible_non_operative_machine_identity_surface",
    artifact_type="CONSTITUTIONAL_MACHINE_IDENTITY",
    required=False,
    parse_mode="json",
    operative=False,
    lineage_visible=True,
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


def sha256_digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def choose_snapshot_path(snapshot_dir: Path) -> Path:
    base_name = f"constitutional_surface_snapshot__{timestamp_slug()}"
    candidate = snapshot_dir / f"{base_name}.json"
    if not candidate.exists():
        return candidate

    counter = 2
    while True:
        candidate = snapshot_dir / f"{base_name}__{counter}.json"
        if not candidate.exists():
            return candidate
        counter += 1


def version_from_filename(path: Path) -> Optional[str]:
    match = re.search(r"v\d+\.\d+(?:\.\d+)?", path.name)
    return match.group(0) if match else None


def version_from_text(raw_text: str) -> Optional[str]:
    json_match = re.search(r'"version"\s*:\s*"([^"]+)"', raw_text)
    if json_match:
        return json_match.group(1)

    filename_match = re.search(r"v\d+\.\d+(?:\.\d+)?", raw_text)
    if filename_match:
        return filename_match.group(0)

    return None


def count_json_documents(raw_text: str) -> Optional[int]:
    decoder = json.JSONDecoder()
    index = 0
    count = 0

    while True:
        while index < len(raw_text) and raw_text[index].isspace():
            index += 1
        if index >= len(raw_text):
            return count
        try:
            _, next_index = decoder.raw_decode(raw_text, index)
        except json.JSONDecodeError:
            return count if count > 0 else None
        count += 1
        index = next_index


def inspect_surface(spec: SurfaceSpec) -> Tuple[Dict[str, Any], Optional[Dict[str, Any]]]:
    record: Dict[str, Any] = {
        "path": repo_relative(spec.path),
        "surface_type": spec.surface_type,
        "rank": spec.rank,
        "role": spec.role,
        "artifact_type": spec.artifact_type,
        "required_input": spec.required,
        "operative": spec.operative,
        "lineage_visible": spec.lineage_visible,
        "existence_status": "present" if spec.path.is_file() else "missing",
    }

    if not spec.path.is_file():
        if spec.required:
            raise FileNotFoundError(f"Required constitutional surface is missing: {spec.path}")
        record["parseability"] = {
            "mode": spec.parse_mode,
            "status": "missing",
            "json_parsed": False,
        }
        return record, None

    record["file_size_bytes"] = spec.path.stat().st_size
    record["sha256"] = sha256_digest(spec.path)

    raw_bytes = spec.path.read_bytes()
    raw_text: Optional[str] = None
    parsed_json: Optional[Dict[str, Any]] = None

    if spec.parse_mode == "binary":
        record["version"] = version_from_filename(spec.path)
        record["version_source"] = "filename_hint" if record["version"] else None
        record["parseability"] = {
            "mode": "binary",
            "status": "not_machine_parsed_binary_surface",
            "json_parsed": False,
        }
        return record, None

    try:
        raw_text = raw_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        if spec.required:
            raise ValueError(f"Failed to decode required surface as UTF-8: {spec.path}") from exc
        record["parseability"] = {
            "mode": spec.parse_mode,
            "status": "text_decode_failed",
            "json_parsed": False,
            "error": str(exc),
        }
        return record, None

    if spec.parse_mode == "text":
        version = version_from_filename(spec.path) or version_from_text(raw_text)
        record["version"] = version
        record["version_source"] = "filename_hint" if version_from_filename(spec.path) else "text_hint"
        record["parseability"] = {
            "mode": "text",
            "status": "text_surface_recorded_without_structural_parse",
            "json_parsed": False,
        }
        return record, None

    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        version = version_from_filename(spec.path) or version_from_text(raw_text)
        record["version"] = version
        record["version_source"] = "filename_hint" if version_from_filename(spec.path) else "text_hint"
        record["parseability"] = {
            "mode": "json",
            "status": "invalid_single_document_json",
            "json_parsed": False,
            "error": str(exc),
            "json_document_count_hint": count_json_documents(raw_text),
        }
        return record, None

    if not isinstance(parsed, dict):
        if spec.required:
            raise ValueError(
                f"Required constitutional surface did not parse to a JSON object: {spec.path}"
            )
        record["parseability"] = {
            "mode": "json",
            "status": "parsed_non_object_json",
            "json_parsed": True,
            "json_top_level_type": type(parsed).__name__,
        }
        return record, None

    parsed_json = parsed
    version = parsed_json.get("version")
    if not isinstance(version, str) or not version:
        version = version_from_filename(spec.path) or version_from_text(raw_text)
        version_source = "filename_or_text_hint"
    else:
        version_source = "json_field"

    record["version"] = version
    record["version_source"] = version_source
    record["declared_fields"] = {
        "protocol_id": parsed_json.get("protocol_id"),
        "protocol_name": parsed_json.get("protocol_name"),
        "artifact_id": parsed_json.get("artifact_id"),
        "artifact_type": parsed_json.get("artifact_type"),
        "status": parsed_json.get("status"),
    }
    record["parseability"] = {
        "mode": "json",
        "status": "parsed_single_document_json",
        "json_parsed": True,
        "json_top_level_type": "object",
    }
    return record, parsed_json


def build_operative_reading(
    identity_data: Mapping[str, Any],
) -> Dict[str, Any]:
    governance_priority = identity_data.get("governance_priority")
    if not isinstance(governance_priority, Mapping):
        governance_priority = {}

    return {
        "current_operational_source_of_truth_surface": governance_priority.get(
            "current_operational_source_of_truth_surface",
            repo_relative(OPERATIVE_TEXT_SPEC.path),
        ),
        "machine_canon_surface": governance_priority.get(
            "machine_canon_surface",
            repo_relative(CANON_SPEC.path),
        ),
        "current_machine_identity_surface": governance_priority.get(
            "machine_identity_surface",
            repo_relative(IDENTITY_SPEC.path),
        ),
        "public_publication_surface": governance_priority.get(
            "public_publication_surface",
            repo_relative(PUBLICATION_SPEC.path),
        ),
        "prior_lineage_visible_machine_identity_surface": {
            "path": repo_relative(OLD_IDENTITY_SPEC.path),
            "operative": False,
            "lineage_visible": True,
        },
        "priority_rule": governance_priority.get(
            "priority_rule",
            "OPERATIVE_CONSTITUTIONAL_TEXT_OVERRIDES_MACHINE_CANON_AND_MACHINE_IDENTITY",
        ),
        "ranking_source": repo_relative(IDENTITY_SPEC.path),
    }


def build_version_reading(
    identity_data: Mapping[str, Any],
    surfaces: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    current_version_reading = identity_data.get("current_version_reading")
    if not isinstance(current_version_reading, Mapping):
        current_version_reading = {}

    operative_line = identity_data.get("operative_constitutional_line")
    if not isinstance(operative_line, Mapping):
        operative_line = {}

    return {
        "operative_constitutional_line_version": current_version_reading.get(
            "operative_constitutional_line_version",
            operative_line.get("line_version"),
        ),
        "operative_constitutional_text_surface_version": surfaces[
            OPERATIVE_TEXT_SPEC.key
        ].get("version"),
        "machine_canon_surface_version": surfaces[CANON_SPEC.key].get("version"),
        "machine_identity_surface_version": surfaces[IDENTITY_SPEC.key].get("version"),
        "public_publication_surface_version": surfaces[PUBLICATION_SPEC.key].get(
            "version"
        ),
        "prior_lineage_identity_surface_version_hint": surfaces[
            OLD_IDENTITY_SPEC.key
        ].get("version"),
        "reading": current_version_reading.get(
            "reading",
            "later_editorial_increment_with_machine_synchronization_and_earlier_public_publication_surface",
        ),
        "semantic_conflict_claimed": current_version_reading.get(
            "semantic_conflict_claimed",
            False,
        ),
    }


def build_machine_validity_notes(
    surfaces: Mapping[str, Mapping[str, Any]],
) -> Dict[str, Any]:
    old_identity_parseability = surfaces[OLD_IDENTITY_SPEC.key].get("parseability", {})

    return {
        "machine_canon_surface": {
            "operative": True,
            "json_parse_status": surfaces[CANON_SPEC.key]["parseability"]["status"],
        },
        "machine_identity_surface": {
            "operative": True,
            "json_parse_status": surfaces[IDENTITY_SPEC.key]["parseability"]["status"],
        },
        "prior_lineage_visible_machine_identity_surface": {
            "operative": False,
            "lineage_visible": True,
            "json_parse_status": old_identity_parseability.get("status"),
            "parse_error": old_identity_parseability.get("error"),
            "json_document_count_hint": old_identity_parseability.get(
                "json_document_count_hint"
            ),
        },
        "snapshot_law_status": "implementation_local_readability_support_only",
    }


def build_snapshot_payload(
    snapshot_path: Path,
    surfaces: Mapping[str, Mapping[str, Any]],
    identity_data: Mapping[str, Any],
) -> Dict[str, Any]:
    return {
        "metadata": {
            "snapshot_type": SNAPSHOT_TYPE,
            "generated_at": utc_now(),
            "snapshot_builder_path": repo_relative(Path(__file__).resolve()),
            "snapshot_source_root": repo_relative(PROTOCOL_DIR),
            "snapshot_path": repo_relative(snapshot_path),
            "implementation_posture": IMPLEMENTATION_POSTURE,
        },
        "ranked_constitutional_surfaces": {
            OPERATIVE_TEXT_SPEC.key: surfaces[OPERATIVE_TEXT_SPEC.key],
            CANON_SPEC.key: surfaces[CANON_SPEC.key],
            IDENTITY_SPEC.key: surfaces[IDENTITY_SPEC.key],
            PUBLICATION_SPEC.key: surfaces[PUBLICATION_SPEC.key],
            OLD_IDENTITY_SPEC.key: surfaces[OLD_IDENTITY_SPEC.key],
        },
        "operative_reading": build_operative_reading(identity_data),
        "version_reading": build_version_reading(identity_data, surfaces),
        "machine_validity_notes": build_machine_validity_notes(surfaces),
        "bounded_notes": {
            "additive_posture": True,
            "rewrites_existing_constitutional_artifacts": False,
            "normalizes_old_artifacts_by_mutation": False,
            "treats_prior_identity_surface_as_lineage_only": True,
        },
    }


def write_snapshot(snapshot_path: Path, payload: Mapping[str, Any]) -> None:
    snapshot_path.parent.mkdir(parents=True, exist_ok=True)
    snapshot_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    surfaces: Dict[str, Dict[str, Any]] = {}

    required_specs = (
        OPERATIVE_TEXT_SPEC,
        CANON_SPEC,
        IDENTITY_SPEC,
        PUBLICATION_SPEC,
        OLD_IDENTITY_SPEC,
    )

    parsed_json_surfaces: Dict[str, Dict[str, Any]] = {}

    try:
        for spec in required_specs:
            record, parsed_json = inspect_surface(spec)
            surfaces[spec.key] = record
            if parsed_json is not None:
                parsed_json_surfaces[spec.key] = parsed_json
    except (FileNotFoundError, ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1

    identity_data = parsed_json_surfaces.get(IDENTITY_SPEC.key)

    if parsed_json_surfaces.get(CANON_SPEC.key) is None:
        print("Required machine canon surface did not parse as single-document JSON.", file=sys.stderr)
        return 1

    if identity_data is None:
        print("Required machine identity surface did not parse as single-document JSON.", file=sys.stderr)
        return 1

    snapshot_path = choose_snapshot_path(SNAPSHOTS_DIR)
    payload = build_snapshot_payload(snapshot_path, surfaces, identity_data)

    try:
        write_snapshot(snapshot_path, payload)
    except OSError as exc:
        print(f"Failed to write constitutional surface snapshot: {exc}", file=sys.stderr)
        return 1

    old_identity_status = surfaces[OLD_IDENTITY_SPEC.key]["parseability"]["status"]

    print("Bounded constitutional surface snapshot written.")
    print(f"Snapshot path: {repo_relative(snapshot_path)}")
    print(
        "Operative constitutional text: "
        f"{surfaces[OPERATIVE_TEXT_SPEC.key]['path']}"
    )
    print(
        "Operative machine identity: "
        f"{surfaces[IDENTITY_SPEC.key]['path']}"
    )
    print(f"Old lineage identity parse status: {old_identity_status}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
