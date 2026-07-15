"""
Bounded shared v1 implementation-local preservation layout helper.

This module provides one additive local writing surface for future proof-slice
runners without rewriting earlier runners, mutating earlier outputs, or
claiming this implementation-local layout as final protocol law.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[3]
RUNS_DIR = REPO_ROOT / "v1" / "registry" / "runs"

_LAYER_DIRECTORY_NAMES: Dict[str, str] = {
    "canonical_body": "canonical_body",
    "envelope": "envelope",
    "execution_relation": "execution_relation",
    "conformance": "conformance",
    "fixtures": "fixture_outputs",
    "summary": "run_summary",
    "manifest": "manifest",
    "source_notes": "source_notes",
}

_LAYER_ALIASES: Dict[str, str] = {
    "canonical_bodies": "canonical_body",
    "envelopes": "envelope",
    "fixture_outputs": "fixtures",
    "run_summary": "summary",
}


class PreservationLayoutError(RuntimeError):
    """Base error for the bounded implementation-local preservation surface."""


class UnknownLayerError(PreservationLayoutError):
    """Raised when a caller asks for an unsupported preservation layer."""


class PathResolutionError(PreservationLayoutError):
    """Raised when a caller provides a path that escapes the bounded layout."""


class PreservationWriteError(PreservationLayoutError):
    """Raised when a layout directory or JSON payload cannot be written."""


@dataclass(frozen=True)
class WrittenOutput:
    """A single preserved output written through the shared layout helper."""

    layer: str
    path: Path

    def as_record(self) -> Dict[str, str]:
        return {
            "layer": self.layer,
            "path": _repo_relative(self.path),
        }


@dataclass(frozen=True)
class RunLayout:
    """
    Bounded implementation-local layout for one execution run surface.

    `root_dir` is the local writing root used by the current runner. For an
    ordinary run that is `v1/registry/runs/<execution-identity>/`. For a
    continuity run that is `v1/registry/runs/<execution-identity>/continuity/`.
    """

    kind: str
    execution_identity: str
    execution_run_dir: Path
    root_dir: Path
    layer_roots: Dict[str, Path]
    naming_posture: str = field(
        default="implementation_local_default",
        init=False,
    )

    def layer_root(self, layer: str) -> Path:
        return self.layer_roots[_normalize_layer(layer)]

    def layer_path(self, layer: str, relative_path: str | Path = "") -> Path:
        layer_root = self.layer_root(layer)
        return _resolve_layer_path(layer_root, relative_path)

    def as_record(self) -> Dict[str, Any]:
        return {
            "layout_kind": self.kind,
            "execution_identity": self.execution_identity,
            "execution_run_directory": _repo_relative(self.execution_run_dir),
            "run_directory": _repo_relative(self.root_dir),
            "layer_roots": {
                layer: _repo_relative(path)
                for layer, path in sorted(self.layer_roots.items())
            },
            "naming_posture": self.naming_posture,
        }


def create_ordinary_run_layout(
    execution_identity: str,
    runs_dir: Path = RUNS_DIR,
    *,
    exist_ok: bool = False,
) -> RunLayout:
    """
    Create the bounded local layout for an ordinary proof-slice run.

    This creates the run root only. Layer directories are created lazily when
    later writes actually occur.
    """

    resolved_runs_dir = runs_dir.resolve()
    execution_run_dir = resolved_runs_dir / execution_identity
    _ensure_directory(
        execution_run_dir,
        exist_ok=exist_ok,
        label="ordinary run root",
    )
    return _build_layout(
        kind="ordinary",
        execution_identity=execution_identity,
        execution_run_dir=execution_run_dir,
        root_dir=execution_run_dir,
    )


def create_continuity_run_layout(
    execution_identity: str,
    runs_dir: Path = RUNS_DIR,
    *,
    exist_ok: bool = False,
) -> RunLayout:
    """
    Create the bounded local layout for a continuity proof-slice run.

    This creates the continuity run root under the execution run directory.
    Layer directories are created lazily when later writes actually occur.
    """

    resolved_runs_dir = runs_dir.resolve()
    execution_run_dir = resolved_runs_dir / execution_identity
    continuity_dir = execution_run_dir / "continuity"
    _ensure_directory(
        continuity_dir,
        exist_ok=exist_ok,
        label="continuity run root",
    )
    return _build_layout(
        kind="continuity",
        execution_identity=execution_identity,
        execution_run_dir=execution_run_dir,
        root_dir=continuity_dir,
    )


def write_json(
    layout: RunLayout,
    layer: str,
    relative_path: str | Path,
    payload: Mapping[str, Any],
) -> WrittenOutput:
    """
    Write one JSON payload into a named preservation layer.

    The caller remains responsible for business logic and for choosing the
    layer-relative path. This helper only preserves bounded layer separation.
    """

    normalized_layer = _normalize_layer(layer)
    target_path = layout.layer_path(normalized_layer, relative_path)
    _write_json_file(target_path, payload)
    return WrittenOutput(layer=normalized_layer, path=target_path)


def write_summary(
    layout: RunLayout,
    payload: Mapping[str, Any],
    filename: str = "run_summary.json",
) -> WrittenOutput:
    """Write the run summary into the stable local summary layer."""

    return write_json(layout, "summary", _ensure_json_filename(filename), payload)


def write_manifest(
    layout: RunLayout,
    payload: Mapping[str, Any],
    filename: str = "preservation_manifest.json",
) -> WrittenOutput:
    """Write the preservation manifest into the stable local manifest layer."""

    return write_json(layout, "manifest", _ensure_json_filename(filename), payload)


def write_source_note(
    layout: RunLayout,
    note_name: str,
    payload: Mapping[str, Any],
) -> WrittenOutput:
    """Write one structured source note into the stable local source-note layer."""

    return write_json(layout, "source_notes", _ensure_json_filename(note_name), payload)


def write_fixture(
    layout: RunLayout,
    relative_path: str | Path,
    payload: Mapping[str, Any],
) -> WrittenOutput:
    """Write one fixture payload into the stable local fixture layer."""

    return write_json(layout, "fixtures", relative_path, payload)


def build_manifest_payload(
    layout: RunLayout,
    written_outputs: Sequence[WrittenOutput],
    *,
    manifest_type: str = "v1_preservation_manifest",
    extra: Mapping[str, Any] | None = None,
) -> Dict[str, Any]:
    """
    Build a small manifest payload for outputs written through this helper.

    The returned object remains implementation-local and bounded. It records
    what was written, by layer and path, without inventing a protocol-level
    storage law.
    """

    written_records = [entry.as_record() for entry in _sorted_outputs(written_outputs)]
    written_by_layer: Dict[str, List[str]] = {}
    for entry in written_records:
        written_by_layer.setdefault(entry["layer"], []).append(entry["path"])

    manifest: Dict[str, Any] = {
        "manifest_type": manifest_type,
        "implementation_posture": "implementation_local_layout_only",
        **layout.as_record(),
        "written_outputs": written_records,
        "written_by_layer": {
            layer: paths for layer, paths in sorted(written_by_layer.items())
        },
        "note": (
            "This local preservation layout is an implementation-local default, "
            "not final protocol law."
        ),
    }
    if extra:
        manifest.update(dict(extra))
    return manifest


def _build_layout(
    *,
    kind: str,
    execution_identity: str,
    execution_run_dir: Path,
    root_dir: Path,
) -> RunLayout:
    layer_roots = {
        layer: root_dir / directory_name
        for layer, directory_name in _LAYER_DIRECTORY_NAMES.items()
    }
    return RunLayout(
        kind=kind,
        execution_identity=execution_identity,
        execution_run_dir=execution_run_dir,
        root_dir=root_dir,
        layer_roots=layer_roots,
    )


def _normalize_layer(layer: str) -> str:
    normalized = _LAYER_ALIASES.get(layer, layer)
    if normalized not in _LAYER_DIRECTORY_NAMES:
        raise UnknownLayerError(
            f"Unknown preservation layer {layer!r}. "
            f"Supported layers are: {', '.join(sorted(_LAYER_DIRECTORY_NAMES))}."
        )
    return normalized


def _resolve_layer_path(layer_root: Path, relative_path: str | Path) -> Path:
    if isinstance(relative_path, Path):
        candidate = relative_path
    else:
        candidate = Path(relative_path)

    if str(candidate) in {"", "."}:
        return layer_root
    if candidate.is_absolute():
        raise PathResolutionError(
            "Layer-relative preservation paths must be relative, not absolute."
        )
    if any(part == ".." for part in candidate.parts):
        raise PathResolutionError(
            "Layer-relative preservation paths must not escape the bounded layout."
        )
    return layer_root / candidate


def _ensure_directory(path: Path, *, exist_ok: bool, label: str) -> None:
    try:
        path.mkdir(parents=True, exist_ok=exist_ok)
    except OSError as exc:
        raise PreservationWriteError(
            f"Failed to create {label} at {_repo_relative(path)}: {exc}"
        ) from exc


def _write_json_file(path: Path, payload: Mapping[str, Any]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    except OSError as exc:
        raise PreservationWriteError(
            f"Failed to write JSON at {_repo_relative(path)}: {exc}"
        ) from exc
    except TypeError as exc:
        raise PreservationWriteError(
            f"Failed to serialize JSON for {_repo_relative(path)}: {exc}"
        ) from exc


def _ensure_json_filename(filename: str) -> str:
    stripped = filename.strip()
    if not stripped:
        raise PathResolutionError("A JSON filename must not be empty.")
    if not stripped.endswith(".json"):
        return f"{stripped}.json"
    return stripped


def _sorted_outputs(written_outputs: Sequence[WrittenOutput]) -> List[WrittenOutput]:
    return sorted(
        written_outputs,
        key=lambda entry: (entry.layer, _repo_relative(entry.path)),
    )


def _repo_relative(path: Path) -> str:
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


__all__ = [
    "PreservationLayoutError",
    "PreservationWriteError",
    "PathResolutionError",
    "RunLayout",
    "UnknownLayerError",
    "WrittenOutput",
    "RUNS_DIR",
    "build_manifest_payload",
    "create_continuity_run_layout",
    "create_ordinary_run_layout",
    "write_fixture",
    "write_json",
    "write_manifest",
    "write_source_note",
    "write_summary",
]
