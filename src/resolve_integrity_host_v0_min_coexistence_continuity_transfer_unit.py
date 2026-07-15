"""Resolve bounded continuity-transfer units for the v0-min line.

This module emits one additive seam-crossing transfer result from one
successful current-state source surface, one bounded transfer request, and one
successful touch-permission result. It preserves source-vs-derivative identity
and carries only exposed, admitted fields.

It does not replay source actions into a live host, merge preserved runs,
mutate prior artifacts, complete continuity, upgrade standing, replace the
source surface, define persistence or registry law, or turn transfer into final
governance.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission as touch_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver


class ContinuityTransferUnitError(RuntimeError):
    """Raised for malformed transfer inputs or impossible correspondence."""


CURRENT_STATE_ANSWER_SURFACE_ROOT = answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = query_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = touch_resolver.CURRENT_STATE_TOUCH_PERMISSION_ROOT
CONTINUITY_TRANSFER_UNIT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_continuity_transfer_units"
)

CANONICAL_CORE_EXECUTION_FILE = query_resolver.CANONICAL_CORE_EXECUTION_FILE
RESOLVER_MODULE = "resolve_integrity_host_v0_min_coexistence_continuity_transfer_unit"
CONTINUITY_TRANSFER_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CONTINUITY_TRANSFER_UNIT_RESULT"
)
CONTINUITY_TRANSFER_RESULT_VERSION = "0.1.0"

OUTCOME_TRANSFERRED = "TRANSFERRED"
OUTCOME_REFUSED = "REFUSED"

TRANSFER_CLASS_REFERENCE = "REFERENCE_TRANSFER"
TRANSFER_CLASS_DERIVATIVE = "DERIVATIVE_TRANSFER"
SUPPORTED_TRANSFER_CLASSES = frozenset(
    {TRANSFER_CLASS_REFERENCE, TRANSFER_CLASS_DERIVATIVE}
)

PATH_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
)
EFFECTIVE_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)
REQUIRED_FALSE_NON_CLAIMS = (
    "replayed_into_live_host",
    "merged_into_local_state",
    "continuity_completed",
    "standing_upgraded",
)

NON_CLAIM_DEFAULTS = {
    **touch_resolver.NON_CLAIM_DEFAULTS,
    "final_continuity_transfer_completed": False,
}

BLOCK_REASONS = {
    "NO_ADMISSIBLE_SOURCE_SURFACE": (
        "No admissible successful current-state source surface is available."
    ),
    "SELECTED_SOURCE_SURFACE_UNREADABLE": (
        "The selected current-state source surface is unreadable."
    ),
    "SELECTED_SOURCE_SURFACE_MALFORMED": (
        "The selected current-state source surface is malformed."
    ),
    "SELECTED_SOURCE_SURFACE_BLOCKED": (
        "The selected current-state source surface is blocked."
    ),
    "SELECTED_SOURCE_SURFACE_OUT_OF_SCOPE": (
        "The selected source surface is outside the bounded transfer scope."
    ),
    "SELECTED_SOURCE_SURFACE_NOT_SUCCESSFUL": (
        "The selected source surface does not have a supported successful outcome."
    ),
    "NO_SUCCESSFUL_TOUCH_PERMISSION_FOR_TRANSFER": (
        "No successful corresponding touch-permission result exists for transfer."
    ),
    "TOUCH_PERMISSION_UNREADABLE": "The touch-permission result is unreadable.",
    "TOUCH_PERMISSION_MALFORMED": "The touch-permission result is malformed.",
    "TOUCH_PERMISSION_DOES_NOT_CORRESPOND_TO_SOURCE_SURFACE": (
        "The touch-permission result does not correspond to the selected source surface."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "The effective references do not preserve the canonical execution line."
    ),
    "EFFECTIVE_REFERENCE_INCOHERENCE": (
        "The selected source surface's effective references are not internally coherent."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Continuity-transfer cannot fall back to stale prior-family artifacts."
    ),
    "LATEST_FILE_INFERENCE_REFUSED": (
        "Continuity-transfer cannot infer active current state from latest files alone."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based transfer is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based transfer is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity-transfer cannot claim continuity completion."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Continuity-transfer cannot silently upgrade standing."
    ),
    "IMPLICIT_MUTATION_REFUSED": "Continuity-transfer cannot authorize mutation.",
    "IMPLICIT_AUTHORITY_CLAIM_REFUSED": (
        "Continuity-transfer cannot carry implicit authority or final-governance claims."
    ),
    "TRANSFER_CLASS_OUT_OF_SCOPE": (
        "The requested transfer class is outside the bounded transfer model."
    ),
    "TRANSFER_PAYLOAD_OUT_OF_SCOPE": (
        "The requested transfer payload exceeds exposed and admitted fields."
    ),
    "SOURCE_REPLACEMENT_REFUSED": (
        "Continuity-transfer cannot replace the selected source surface."
    ),
    "SOURCE_DERIVATIVE_COLLAPSE_REFUSED": (
        "Continuity-transfer cannot collapse source and carried derivative."
    ),
    "MULTIPLE_SOURCE_SURFACES_CONFLICT_UNRESOLVED": (
        "Multiple successful source surfaces conflict without bounded arbitration."
    ),
}


@dataclass(frozen=True)
class _SurfaceDefinition:
    result_family: str
    root: Path
    metadata_key: str
    id_key: str
    type_key: str
    expected_outcome: str
    effective_inputs_key: str
    summary_key: str
    payload_key: str
    selected_key: str | None


SURFACE_DEFINITIONS = (
    _SurfaceDefinition(
        "answer_read",
        CURRENT_STATE_ANSWER_SURFACE_ROOT,
        "answer_read_metadata",
        "answer_read_result_id",
        "answer_read_result_type",
        answer_resolver.OUTCOME_ANSWERED,
        "effective_answer_read_inputs",
        "answer_read_summary",
        "answer_read_output",
        "selected_current_state_application",
    ),
    _SurfaceDefinition(
        "query",
        CURRENT_STATE_QUERY_ROOT,
        "query_metadata",
        "query_result_id",
        "query_result_type",
        query_resolver.OUTCOME_ANSWERED_QUERY,
        "effective_query_inputs",
        "query_summary",
        "query_answer",
        "selected_current_state_answer_read",
    ),
    _SurfaceDefinition(
        "what_stands_now",
        CURRENT_STATE_WHAT_STANDS_NOW_ROOT,
        "what_stands_now_metadata",
        "what_stands_now_result_id",
        "what_stands_now_result_type",
        stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
        "effective_stand_now_inputs",
        "what_stands_now_summary",
        "what_stands_now_answer",
        "selected_current_state_answer_read",
    ),
    _SurfaceDefinition(
        "what_remains_open",
        CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT,
        "what_remains_open_metadata",
        "what_remains_open_result_id",
        "what_remains_open_result_type",
        open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
        "effective_open_inputs",
        "what_remains_open_summary",
        "what_remains_open_answer",
        "selected_current_state_answer_read",
    ),
)

REFERENCE_DEFAULT_FIELDS = (
    "selected_source_surface_path",
    "selected_source_surface_id",
    "selected_source_surface_family",
    "selected_source_surface_outcome",
    "selected_source_surface_effective_references",
    "touch_permission_result_id",
    "admitted_touch_class",
    "non_claims",
)
REFERENCE_INTRINSIC_FIELDS = frozenset(
    {*REFERENCE_DEFAULT_FIELDS, "touch_permission_result_path"}
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = _repo_path(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise OSError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise ContinuityTransferUnitError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(value, dict):
        raise ContinuityTransferUnitError(f"{context} must be a JSON object: {resolved}")
    return value


def read_continuity_transfer_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded continuity-transfer request."""

    return _normal_transfer_request(_read_json_file(path, "continuity-transfer request"))


def _check(
    name: str,
    passed: bool,
    expected: Any | None = None,
    actual: Any | None = None,
    block_code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check_name": name, "passed": bool(passed)}
    if expected is not None:
        result["expected_posture"] = expected
    if actual is not None:
        result["actual_posture"] = actual
    if block_code is not None:
        result["block_code"] = block_code
    return result


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "continuity_transfer_unit_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "continuity_transfer_unit_result"


def _same_path(left: Any, right: Any) -> bool:
    if not isinstance(left, str) or not left.strip():
        return False
    if not isinstance(right, str) or not right.strip():
        return False
    return _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(
        strict=False
    )


def _normal_transfer_request(request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise ContinuityTransferUnitError("continuity-transfer request must be a mapping")
    required = (
        "continuity_transfer_request_id",
        "transfer_class",
        "transfer_basis",
        "requested_transfer_fields",
        "target_seam_label",
    )
    for key in required:
        if key not in request:
            raise ContinuityTransferUnitError(
                f"continuity-transfer request is missing {key}"
            )
    normalized: dict[str, Any] = {}
    for key in (
        "continuity_transfer_request_id",
        "transfer_class",
        "transfer_basis",
        "target_seam_label",
    ):
        value = request.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferUnitError(
                f"continuity-transfer request {key} must be a non-empty string"
            )
        normalized[key] = value.strip()
    fields = request.get("requested_transfer_fields")
    if not isinstance(fields, list):
        raise ContinuityTransferUnitError(
            "continuity-transfer request requested_transfer_fields must be a list"
        )
    normalized_fields: list[str] = []
    for index, value in enumerate(fields):
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferUnitError(
                "continuity-transfer request requested_transfer_fields "
                f"entry {index} must be a non-empty string"
            )
        normalized_fields.append(value.strip())
    normalized["requested_transfer_fields"] = normalized_fields
    return normalized


def _surface_definition_for(surface: Mapping[str, Any]) -> _SurfaceDefinition | None:
    for definition in SURFACE_DEFINITIONS:
        if definition.metadata_key in surface or definition.effective_inputs_key in surface:
            return definition
    return None


def _surface_metadata(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
) -> Mapping[str, Any]:
    metadata = surface.get(definition.metadata_key)
    if not isinstance(metadata, Mapping):
        raise ContinuityTransferUnitError(
            f"selected {definition.result_family} source metadata must be an object"
        )
    return metadata


def _surface_effective_inputs(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
) -> dict[str, Any]:
    raw = surface.get(definition.effective_inputs_key)
    if not isinstance(raw, Mapping):
        raise ContinuityTransferUnitError(
            f"selected {definition.result_family} source effective references "
            "must be an object"
        )
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        value = result.get(key)
        if not isinstance(value, str) or not value.strip():
            raise ContinuityTransferUnitError(
                f"selected source effective reference {key} must be a non-empty string"
            )
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        value = result.get(key)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise ContinuityTransferUnitError(
                f"selected source effective reference {key} must be a string when present"
            )
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _source_surface_identity(
    surface: Mapping[str, Any] | None,
    definition: _SurfaceDefinition | None,
    source_path: Path | str | None,
) -> dict[str, Any]:
    if surface is None or definition is None:
        return {
            "selected_source_surface_path": _display_path(source_path),
            "selected_source_surface_id": None,
            "selected_source_surface_family": None,
            "selected_source_surface_outcome": None
            if surface is None
            else surface.get("outcome"),
            "selected_source_surface_effective_references": {},
        }
    metadata = _surface_metadata(surface, definition)
    result_id = metadata.get(definition.id_key)
    if not isinstance(result_id, str) or not result_id.strip():
        raise ContinuityTransferUnitError("selected source surface id is malformed")
    outcome = surface.get("outcome")
    if not isinstance(outcome, str) or not outcome.strip():
        raise ContinuityTransferUnitError("selected source surface outcome is malformed")
    raw_effective = surface.get(definition.effective_inputs_key, {})
    effective = (
        {key: raw_effective.get(key) for key in EFFECTIVE_INPUT_KEYS}
        if isinstance(raw_effective, Mapping)
        else {}
    )
    return {
        "selected_source_surface_path": _display_path(source_path)
        if source_path is not None
        else "provided_mapping",
        "selected_source_surface_id": result_id,
        "selected_source_surface_family": definition.result_family,
        "selected_source_surface_outcome": outcome,
        "selected_source_surface_effective_references": effective,
    }


def _merge_non_claims(
    source: Mapping[str, Any] | None,
    touch: Mapping[str, Any] | None = None,
) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for label, artifact in (("selected source", source), ("touch-permission", touch)):
        if artifact is None:
            continue
        raw = artifact.get("non_claims", {})
        if raw is None:
            continue
        if not isinstance(raw, Mapping):
            raise ContinuityTransferUnitError(f"{label} non_claims must be an object")
        for key, value in raw.items():
            if not isinstance(key, str):
                raise ContinuityTransferUnitError(f"{label} non_claims keys must be strings")
            if not isinstance(value, bool):
                raise ContinuityTransferUnitError(
                    f"{label} non_claims value for {key!r} must be boolean"
                )
            merged[key] = value
    return merged


def _discover_artifacts(root: Path | str, context: str) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise ContinuityTransferUnitError(f"{context} root is not a directory: {resolved}")
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise ContinuityTransferUnitError(f"{context} root is unreadable: {resolved}") from exc


def _effective_key(surface: Mapping[str, Any], definition: _SurfaceDefinition) -> tuple[Any, ...]:
    raw = surface.get(definition.effective_inputs_key)
    if not isinstance(raw, Mapping):
        return ()
    return tuple(raw.get(key) for key in EFFECTIVE_INPUT_KEYS)


def _select_default_source_surface() -> tuple[
    Mapping[str, Any] | None,
    Path | None,
    _SurfaceDefinition | None,
    str | None,
]:
    candidates: list[tuple[str, Mapping[str, Any], Path, _SurfaceDefinition]] = []
    for definition in SURFACE_DEFINITIONS:
        for path in _discover_artifacts(definition.root, "current-state source surface"):
            surface = _read_json_file(path, "current-state source surface")
            found = _surface_definition_for(surface)
            if found != definition:
                continue
            if surface.get("outcome") != definition.expected_outcome:
                continue
            candidates.append((_display_path(path) or str(path), surface, path, definition))
    if not candidates:
        return None, None, None, "NO_ADMISSIBLE_SOURCE_SURFACE"
    keys = {_effective_key(surface, definition) for _, surface, _, definition in candidates}
    if len(keys) > 1:
        return None, None, None, "MULTIPLE_SOURCE_SURFACES_CONFLICT_UNRESOLVED"
    _, surface, path, definition = sorted(candidates, key=lambda item: item[0])[-1]
    return surface, path, definition, None


def _touch_metadata(touch: Mapping[str, Any]) -> Mapping[str, Any]:
    metadata = touch.get("touch_permission_metadata")
    if not isinstance(metadata, Mapping):
        raise ContinuityTransferUnitError("touch-permission metadata must be an object")
    return metadata


def _touch_scope(touch: Mapping[str, Any]) -> Mapping[str, Any]:
    scope = touch.get("admitted_touch_scope")
    if not isinstance(scope, Mapping):
        raise ContinuityTransferUnitError("touch-permission admitted_touch_scope must be an object")
    return scope


def _touch_selected_surface(touch: Mapping[str, Any]) -> Mapping[str, Any]:
    selected = touch.get("selected_current_state_surface")
    if not isinstance(selected, Mapping):
        raise ContinuityTransferUnitError(
            "touch-permission selected current-state surface must be an object"
        )
    return selected


def _touch_id(touch: Mapping[str, Any]) -> str:
    value = _touch_metadata(touch).get("touch_permission_result_id")
    if not isinstance(value, str) or not value.strip():
        raise ContinuityTransferUnitError("touch-permission result id is malformed")
    return value


def _touch_reference(
    touch: Mapping[str, Any] | None,
    touch_path: Path | str | None,
) -> dict[str, Any]:
    if touch is None:
        return {
            "touch_permission_result_path": _display_path(touch_path),
            "touch_permission_result_id": None,
            "admitted_touch_class": None,
            "admitted_touch_scope": None,
        }
    scope = dict(_touch_scope(touch))
    admitted_class = scope.get("admitted_touch_class")
    if not isinstance(admitted_class, str) or not admitted_class.strip():
        raise ContinuityTransferUnitError("touch-permission admitted touch class is malformed")
    return {
        "touch_permission_result_path": _display_path(touch_path)
        if touch_path is not None
        else "provided_mapping",
        "touch_permission_result_id": _touch_id(touch),
        "admitted_touch_class": admitted_class,
        "admitted_touch_scope": scope,
    }


def _admitted_fields(touch: Mapping[str, Any]) -> set[str]:
    scope = _touch_scope(touch)
    fields: set[str] = set()
    for key in ("admitted_readable_fields", "admitted_reference_fields"):
        values = scope.get(key, [])
        if isinstance(values, list):
            fields.update(value for value in values if isinstance(value, str))
    boundary = scope.get("admitted_derivation_boundary")
    if isinstance(boundary, Mapping):
        values = boundary.get("admitted_derivation_fields", [])
        if isinstance(values, list):
            fields.update(value for value in values if isinstance(value, str))
    return fields


def _field_aliases(field: str) -> tuple[str, ...]:
    aliases = {
        "selected_source_surface_path": ("selected_surface_path", "surface_path"),
        "selected_source_surface_id": ("selected_surface_id", "surface_id"),
        "selected_source_surface_family": (
            "selected_surface_result_family",
            "result_family",
        ),
        "selected_source_surface_outcome": ("selected_surface_outcome", "outcome"),
        "selected_source_surface_effective_references": (
            "selected_surface_effective_references",
            "effective_references",
        ),
        "touch_permission_result_id": ("touch_permission_result_id",),
        "admitted_touch_class": ("admitted_touch_class",),
    }
    return (field, *aliases.get(field, ()))


def _field_admitted(field: str, admitted: set[str]) -> bool:
    return any(alias in admitted for alias in _field_aliases(field))


def _field_requires_touch_admission(field: str, transfer_class: str) -> bool:
    return not (
        transfer_class == TRANSFER_CLASS_REFERENCE
        and field in REFERENCE_INTRINSIC_FIELDS
    )


def _touch_class_supports_transfer(transfer_class: str, touch: Mapping[str, Any]) -> bool:
    admitted_class = _touch_scope(touch).get("admitted_touch_class")
    if transfer_class == TRANSFER_CLASS_REFERENCE:
        return admitted_class in {
            touch_resolver.TOUCH_CLASS_READ_ONLY,
            touch_resolver.TOUCH_CLASS_REFERENCE,
            touch_resolver.TOUCH_CLASS_DERIVATION,
        }
    if transfer_class == TRANSFER_CLASS_DERIVATIVE:
        return admitted_class in {
            touch_resolver.TOUCH_CLASS_REFERENCE,
            touch_resolver.TOUCH_CLASS_DERIVATION,
        }
    return False


def _touch_corresponds_to_source(
    touch: Mapping[str, Any],
    identity: Mapping[str, Any],
    effective_inputs: Mapping[str, Any],
) -> bool:
    if touch.get("outcome") != touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH:
        return False
    selected = _touch_selected_surface(touch)
    comparisons = (
        ("selected_surface_id", "selected_source_surface_id"),
        ("selected_surface_result_family", "selected_source_surface_family"),
        ("selected_surface_outcome", "selected_source_surface_outcome"),
    )
    for touch_key, source_key in comparisons:
        touch_value = selected.get(touch_key)
        source_value = identity.get(source_key)
        if isinstance(touch_value, str) and isinstance(source_value, str):
            if touch_value != source_value:
                return False
    refs = selected.get("selected_surface_effective_references", {})
    if isinstance(refs, Mapping):
        for key in EFFECTIVE_INPUT_KEYS:
            touch_value = refs.get(key)
            source_value = effective_inputs.get(key)
            if isinstance(touch_value, str) and touch_value.strip():
                if isinstance(source_value, str) and source_value.strip():
                    if not _same_path(touch_value, source_value):
                        return False
    scope_id = _touch_scope(touch).get("admitted_source_surface_id")
    if isinstance(scope_id, str) and scope_id.strip():
        if scope_id != identity.get("selected_source_surface_id"):
            return False
    return True


def _checks_all_passed(artifact: Mapping[str, Any], label: str) -> bool:
    checks = artifact.get("checks", [])
    if not isinstance(checks, list):
        raise ContinuityTransferUnitError(f"{label} checks must be a list")
    return all(isinstance(check, Mapping) and check.get("passed") is True for check in checks)


def _load_effective_artifacts(
    effective_inputs: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        return (
            _read_json_file(
                str(effective_inputs["effective_authority_artifact_path"]),
                "effective authority artifact",
            ),
            _read_json_file(
                str(effective_inputs["effective_family_packet_path"]),
                "effective run-family packet",
            ),
            _read_json_file(
                str(effective_inputs["effective_status_packet_path"]),
                "effective preserved-run status packet",
            ),
            _read_json_file(
                str(effective_inputs["effective_current_governing_packet_path"]),
                "effective current-governing packet",
            ),
        )
    except (FileNotFoundError, OSError) as exc:
        raise FileNotFoundError(str(exc)) from exc


def _effective_summaries(
    authority: Mapping[str, Any],
    family: Mapping[str, Any],
    status: Mapping[str, Any],
    governing: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    try:
        return {
            "authority": query_resolver.build_execution_authority_summary(authority),
            "family": query_resolver.build_run_family_summary(family),
            "status": query_resolver.build_preserved_run_status_summary(status),
            "governing": query_resolver.build_current_governing_summary(governing),
        }
    except Exception as exc:  # noqa: BLE001 - malformed artifacts fail clearly.
        raise ContinuityTransferUnitError("effective reference artifact is malformed") from exc


def _exposed_paths_match(values: Sequence[Any]) -> bool:
    exposed = [value for value in values if isinstance(value, str) and value.strip()]
    if len(exposed) < 2:
        return True
    first = exposed[0]
    return all(_same_path(first, value) for value in exposed[1:])


def _effective_currentness_checks(
    effective_inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[dict[str, Any]]:
    canonical_actual = {
        name: summary.get("core_execution_file")
        for name, summary in summaries.items()
    }
    source_values = [
        effective_inputs.get("effective_source_run_path"),
        summaries["authority"].get("selected_source_run_directory_path"),
        summaries["family"].get("current_authority_source_run_path"),
        summaries["status"].get("selected_current_authority_source_run_path"),
        summaries["governing"].get("current_governing_source_run_path"),
    ]
    ingress_values = [
        effective_inputs.get("effective_ingress_run_path"),
        summaries["authority"].get("selected_ingress_run_directory_path"),
        summaries["family"].get("current_authority_ingress_run_path"),
        summaries["governing"].get("current_governing_ingress_run_path"),
    ]
    canonical_passed = all(
        value == CANONICAL_CORE_EXECUTION_FILE for value in canonical_actual.values()
    )
    source_passed = _exposed_paths_match(source_values)
    ingress_passed = _exposed_paths_match(ingress_values)
    return [
        _check(
            "canonical_core_execution_file_aligned",
            canonical_passed,
            expected=CANONICAL_CORE_EXECUTION_FILE,
            actual=canonical_actual,
            block_code="CANONICAL_EXECUTION_LINE_MISMATCH"
            if not canonical_passed
            else None,
        ),
        _check(
            "effective_references_share_current_governing_source_run_where_exposed",
            source_passed,
            expected="same current governing source run where exposed",
            actual=source_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE" if not source_passed else None,
        ),
        _check(
            "effective_references_share_current_governing_ingress_run_where_exposed",
            ingress_passed,
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE" if not ingress_passed else None,
        ),
    ]


def _surface_path_correspondence(
    source: Mapping[str, Any],
    definition: _SurfaceDefinition,
    effective_inputs: Mapping[str, Any],
) -> bool:
    pairs = (
        ("current_authority_artifact_path", "effective_authority_artifact_path"),
        ("current_family_packet_path", "effective_family_packet_path"),
        ("current_status_packet_path", "effective_status_packet_path"),
        ("current_governing_packet_path", "effective_current_governing_packet_path"),
        ("current_governing_source_run_path", "effective_source_run_path"),
        ("effective_current_governing_source_run_path", "effective_source_run_path"),
        ("current_governing_ingress_run_path", "effective_ingress_run_path"),
        ("effective_current_governing_ingress_run_path", "effective_ingress_run_path"),
    )
    for section_key in (definition.payload_key, definition.summary_key):
        section = source.get(section_key)
        if not isinstance(section, Mapping):
            continue
        for section_path_key, input_key in pairs:
            value = section.get(section_path_key)
            expected = effective_inputs.get(input_key)
            if isinstance(value, str) and value.strip():
                if isinstance(expected, str) and expected.strip():
                    if not _same_path(value, expected):
                        return False
    return True


def _request_text(request: Mapping[str, Any]) -> str:
    parts = [
        str(request.get("transfer_basis", "")),
        str(request.get("target_seam_label", "")),
        " ".join(str(field) for field in request.get("requested_transfer_fields", [])),
    ]
    return " ".join(parts).lower()


def _contains(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _request_refusal_checks(request: Mapping[str, Any]) -> list[dict[str, Any]]:
    text = _request_text(request)
    return [
        _check(
            "transfer_request_does_not_attempt_replay",
            not _contains(text, ("replay into", "replay-based", "allow replay", "use replay")),
            expected="no replay shortcut",
            actual=request.get("transfer_basis"),
            block_code="REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "transfer_request_does_not_attempt_merge",
            not _contains(text, ("merge into", "merge-based", "allow merge", "use merge")),
            expected="no merge shortcut",
            actual=request.get("transfer_basis"),
            block_code="MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "transfer_request_does_not_claim_continuity_completion",
            not _contains(
                text,
                ("complete continuity", "continuity completion", "claim continuity"),
            ),
            expected="no continuity-completion claim",
            actual=request.get("transfer_basis"),
            block_code="CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "transfer_request_does_not_silently_upgrade_standing",
            not _contains(text, ("standing upgrade", "upgrade standing", "promote standing")),
            expected="no standing upgrade",
            actual=request.get("transfer_basis"),
            block_code="SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "transfer_request_does_not_request_stale_prior_family_fallback",
            not _contains(text, ("stale prior", "prior-family fallback", "fallback to prior")),
            expected="no stale prior-family fallback",
            actual=request.get("transfer_basis"),
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "transfer_request_does_not_infer_from_latest_files",
            not _contains(
                text,
                ("latest authority", "latest family", "latest status", "latest governing"),
            ),
            expected="no latest-file inference",
            actual=request.get("transfer_basis"),
            block_code="LATEST_FILE_INFERENCE_REFUSED",
        ),
        _check(
            "transfer_request_does_not_authorize_mutation",
            not _contains(text, ("mutate", "rewrite", "overwrite", "delete prior", "modify prior")),
            expected="no mutation authority",
            actual=request.get("transfer_basis"),
            block_code="IMPLICIT_MUTATION_REFUSED",
        ),
        _check(
            "transfer_request_does_not_claim_implicit_authority",
            not _contains(
                text,
                (
                    "final governance",
                    "system law",
                    "protocol law",
                    "governing standing",
                    "authority claim",
                    "final identity",
                    "constitutional author",
                ),
            ),
            expected="no implicit authority claim",
            actual=request.get("transfer_basis"),
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED",
        ),
        _check(
            "transfer_request_does_not_replace_source",
            not _contains(text, ("replace source", "source replacement", "become source")),
            expected="source remains source",
            actual=request.get("transfer_basis"),
            block_code="SOURCE_REPLACEMENT_REFUSED",
        ),
        _check(
            "transfer_request_preserves_source_derivative_distinction",
            not _contains(
                text,
                ("collapse source", "collapse derivative", "derivative becomes source"),
            ),
            expected="source and carried derivative remain distinct",
            actual=request.get("transfer_basis"),
            block_code="SOURCE_DERIVATIVE_COLLAPSE_REFUSED",
        ),
    ]


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        block_code = {
            "replayed_into_live_host": "REPLAY_SHORTCUT_REFUSED",
            "merged_into_local_state": "MERGE_SHORTCUT_REFUSED",
            "continuity_completed": "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
            "standing_upgraded": "SILENT_STANDING_UPGRADE_REFUSED",
        }[key]
        checks.append(
            _check(
                f"non_claim_{key}_remains_false",
                non_claims.get(key) is False,
                expected=False,
                actual=non_claims.get(key),
                block_code=block_code if non_claims.get(key) is not False else None,
            )
        )
    finality_failures = {
        key: value
        for key, value in non_claims.items()
        if (key.startswith("final_") or key == "minimum_lawful_system_completed")
        and value is not False
    }
    checks.append(
        _check(
            "broader_finality_non_claims_remain_false",
            not finality_failures,
            expected="all carried finality non-claims false",
            actual=finality_failures,
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED"
            if finality_failures
            else None,
        )
    )
    return checks


def _exposed_transfer_values(
    source: Mapping[str, Any],
    definition: _SurfaceDefinition,
    identity: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    values: dict[str, Any] = {
        "selected_source_surface_path": identity.get("selected_source_surface_path"),
        "selected_source_surface_id": identity.get("selected_source_surface_id"),
        "selected_source_surface_family": identity.get("selected_source_surface_family"),
        "selected_source_surface_outcome": identity.get("selected_source_surface_outcome"),
        "selected_source_surface_effective_references": identity.get(
            "selected_source_surface_effective_references"
        ),
        "touch_permission_result_path": touch_reference.get("touch_permission_result_path"),
        "touch_permission_result_id": touch_reference.get("touch_permission_result_id"),
        "admitted_touch_class": touch_reference.get("admitted_touch_class"),
        "non_claims": dict(non_claims),
    }
    for key, value in identity.get("selected_source_surface_effective_references", {}).items():
        values[str(key)] = value
    for key, value in non_claims.items():
        values[key] = value
    for section_key in (
        definition.metadata_key,
        definition.effective_inputs_key,
        definition.summary_key,
        definition.payload_key,
        definition.selected_key or "",
    ):
        section = source.get(section_key)
        if not isinstance(section, Mapping):
            continue
        for key, value in section.items():
            if isinstance(key, str):
                values[key] = value
        answered_fields = section.get("answered_fields")
        if isinstance(answered_fields, Mapping):
            for key, value in answered_fields.items():
                if isinstance(key, str):
                    values[key] = value
    values["outcome"] = source.get("outcome")
    return values


def _requested_fields_for_transfer(request: Mapping[str, Any]) -> list[str]:
    requested = list(request["requested_transfer_fields"])
    if request["transfer_class"] == TRANSFER_CLASS_REFERENCE and not requested:
        return list(REFERENCE_DEFAULT_FIELDS)
    return requested


def _transfer_payload_scope(
    request: Mapping[str, Any],
    source: Mapping[str, Any],
    definition: _SurfaceDefinition,
    identity: Mapping[str, Any],
    touch: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> tuple[dict[str, Any], dict[str, Any] | None, list[str]]:
    transfer_class = str(request["transfer_class"])
    fields = _requested_fields_for_transfer(request)
    exposed = _exposed_transfer_values(source, definition, identity, touch_reference, non_claims)
    if transfer_class not in SUPPORTED_TRANSFER_CLASSES:
        return (
            _check(
                "transfer_class_is_supported",
                False,
                expected=sorted(SUPPORTED_TRANSFER_CLASSES),
                actual=transfer_class,
                block_code="TRANSFER_CLASS_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    if transfer_class == TRANSFER_CLASS_DERIVATIVE and not fields:
        return (
            _check(
                "transfer_payload_scope_is_bounded",
                False,
                expected="non-empty requested_transfer_fields for derivative transfer",
                actual=fields,
                block_code="TRANSFER_PAYLOAD_OUT_OF_SCOPE",
            ),
            None,
            fields,
        )
    admitted = _admitted_fields(touch)
    invalid_exposed = [field for field in fields if field not in exposed]
    invalid_admitted = [
        field
        for field in fields
        if _field_requires_touch_admission(field, transfer_class)
        and not _field_admitted(field, admitted)
    ]
    class_supported = _touch_class_supports_transfer(transfer_class, touch)
    passed = class_supported and not invalid_exposed and not invalid_admitted
    check = _check(
        "transfer_payload_scope_is_bounded",
        passed,
        expected="already exposed and already admitted fields",
        actual={
            "requested_transfer_fields": list(request["requested_transfer_fields"]),
            "transfer_fields": fields,
            "invalid_exposed_fields": invalid_exposed,
            "invalid_admitted_fields": invalid_admitted,
            "touch_class_supports_transfer": class_supported,
        },
        block_code="TRANSFER_PAYLOAD_OUT_OF_SCOPE" if not passed else None,
    )
    if not passed:
        return check, None, fields
    payload = {
        "payload_derivative_status": "carried_derivative",
        "source_remains_source": True,
        "carried_fields": {field: exposed[field] for field in fields},
        "carried_references": {
            "selected_source_surface_path": identity.get("selected_source_surface_path"),
            "selected_source_surface_effective_references": identity.get(
                "selected_source_surface_effective_references"
            ),
            "touch_permission_result_path": touch_reference.get(
                "touch_permission_result_path"
            ),
            "touch_permission_result_id": touch_reference.get(
                "touch_permission_result_id"
            ),
        },
    }
    return check, payload, fields


def _transfer_fields_within_touch_scope(
    request: Mapping[str, Any],
    source: Mapping[str, Any],
    definition: _SurfaceDefinition,
    identity: Mapping[str, Any],
    touch: Mapping[str, Any],
    effective_inputs: Mapping[str, Any],
) -> bool:
    touch_reference = _touch_reference(touch, None)
    non_claims = _merge_non_claims(source, touch)
    exposed = _exposed_transfer_values(source, definition, identity, touch_reference, non_claims)
    fields = _requested_fields_for_transfer(request)
    transfer_class = str(request["transfer_class"])
    if transfer_class not in SUPPORTED_TRANSFER_CLASSES:
        return False
    if transfer_class == TRANSFER_CLASS_DERIVATIVE and not fields:
        return False
    if not _touch_class_supports_transfer(transfer_class, touch):
        return False
    admitted = _admitted_fields(touch)
    for field in fields:
        if field not in exposed:
            return False
        if _field_requires_touch_admission(field, transfer_class):
            if not _field_admitted(field, admitted):
                return False
    return _touch_corresponds_to_source(touch, identity, effective_inputs)


def _select_matching_touch_permission(
    request: Mapping[str, Any],
    source: Mapping[str, Any],
    definition: _SurfaceDefinition,
    identity: Mapping[str, Any],
    effective_inputs: Mapping[str, Any],
) -> tuple[Mapping[str, Any] | None, Path | None, str | None]:
    candidates: list[tuple[str, Mapping[str, Any], Path]] = []
    for path in _discover_artifacts(CURRENT_STATE_TOUCH_PERMISSION_ROOT, "touch-permission"):
        touch = _read_json_file(path, "touch-permission result")
        if touch.get("outcome") != touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH:
            continue
        if not _transfer_fields_within_touch_scope(
            request,
            source,
            definition,
            identity,
            touch,
            effective_inputs,
        ):
            continue
        candidates.append((_display_path(path) or str(path), touch, path))
    if not candidates:
        return None, None, "NO_SUCCESSFUL_TOUCH_PERMISSION_FOR_TRANSFER"
    _, touch, path = sorted(candidates, key=lambda item: item[0])[-1]
    return touch, path, None


def _result_id(identity: Mapping[str, Any], request: Mapping[str, Any], outcome: str) -> str:
    source_id = identity.get("selected_source_surface_id")
    if not isinstance(source_id, str) or not source_id.strip():
        source_id = "no_source_surface"
    request_id = request.get("continuity_transfer_request_id")
    if not isinstance(request_id, str) or not request_id.strip():
        request_id = "continuity_transfer_request"
    suffix = "transferred" if outcome == OUTCOME_TRANSFERRED else "refused"
    return f"{source_id}__{request_id}__continuity_transfer_unit_{suffix}"


def _result(
    request: Mapping[str, Any],
    identity: Mapping[str, Any],
    touch_reference: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    transfer_payload: Mapping[str, Any] | None,
    transfer_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return {
        "continuity_transfer_metadata": {
            "continuity_transfer_result_id": _result_id(identity, request, outcome),
            "continuity_transfer_result_type": CONTINUITY_TRANSFER_RESULT_TYPE,
            "continuity_transfer_result_version": CONTINUITY_TRANSFER_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_source_surface": dict(identity),
        "touch_permission_reference": dict(touch_reference),
        "transfer_request": dict(request),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code) if block_code else None,
        },
        "transfer_payload": dict(transfer_payload) if transfer_payload is not None else None,
        "transfer_summary": dict(transfer_summary) if transfer_summary is not None else None,
        "non_claims": dict(non_claims),
    }


def _refused_result(
    request: Mapping[str, Any],
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    identity: Mapping[str, Any] | None = None,
    touch_reference: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        request,
        identity or _source_surface_identity(None, None, None),
        touch_reference or _touch_reference(None, None),
        checks,
        OUTCOME_REFUSED,
        block_code,
        None,
        None,
        non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _resolve_selected_source(
    request: Mapping[str, Any],
    source: Mapping[str, Any],
    source_path: Path | str | None,
    definition: _SurfaceDefinition | None,
    selection_source: str,
    touch_permission: Mapping[str, Any] | None,
    touch_permission_path: Path | str | None,
) -> dict[str, Any]:
    if definition is None:
        identity = _source_surface_identity(source, None, source_path)
        return _refused_result(
            request,
            "SELECTED_SOURCE_SURFACE_OUT_OF_SCOPE",
            [
                _check(
                    "selected_source_surface_is_in_transfer_scope",
                    False,
                    expected=[item.result_family for item in SURFACE_DEFINITIONS],
                    actual="unrecognized current-state source surface",
                    block_code="SELECTED_SOURCE_SURFACE_OUT_OF_SCOPE",
                )
            ],
            identity=identity,
            non_claims=_merge_non_claims(source),
        )

    identity = _source_surface_identity(source, definition, source_path)
    source_non_claims = _merge_non_claims(source)
    outcome = source.get("outcome")
    if outcome == "BLOCKED":
        return _refused_result(
            request,
            "SELECTED_SOURCE_SURFACE_BLOCKED",
            [
                _check(
                    "selected_source_surface_has_successful_outcome",
                    False,
                    expected=definition.expected_outcome,
                    actual=outcome,
                    block_code="SELECTED_SOURCE_SURFACE_BLOCKED",
                )
            ],
            identity=identity,
            non_claims=source_non_claims,
        )
    if outcome != definition.expected_outcome:
        return _refused_result(
            request,
            "SELECTED_SOURCE_SURFACE_NOT_SUCCESSFUL",
            [
                _check(
                    "selected_source_surface_has_successful_outcome",
                    False,
                    expected=definition.expected_outcome,
                    actual=outcome,
                    block_code="SELECTED_SOURCE_SURFACE_NOT_SUCCESSFUL",
                )
            ],
            identity=identity,
            non_claims=source_non_claims,
        )

    effective_inputs = _surface_effective_inputs(source, definition)
    checks: list[dict[str, Any]] = [
        _check(
            "selected_source_surface_exists_and_is_readable",
            True,
            expected="one readable selected current-state source surface",
            actual=identity.get("selected_source_surface_path"),
        ),
        _check(
            "selected_source_surface_has_successful_outcome",
            True,
            expected=definition.expected_outcome,
            actual=outcome,
        ),
        _check(
            "selected_source_surface_is_in_transfer_scope",
            True,
            expected=[item.result_family for item in SURFACE_DEFINITIONS],
            actual=definition.result_family,
        ),
        _check(
            "selected_source_surface_checks_passed",
            _checks_all_passed(source, "selected source surface"),
            expected="selected source surface checks all passed",
            actual="all passed"
            if _checks_all_passed(source, "selected source surface")
            else "one or more failed",
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not _checks_all_passed(source, "selected source surface")
            else None,
        ),
    ]

    if touch_permission is None:
        touch_permission, touch_permission_path, touch_block = _select_matching_touch_permission(
            request,
            source,
            definition,
            identity,
            effective_inputs,
        )
        if touch_block is not None:
            checks.append(
                _check(
                    "successful_touch_permission_for_transfer_exists",
                    False,
                    expected="one admitted touch-permission result corresponding to source",
                    actual=touch_block,
                    block_code=touch_block,
                )
            )
            return _refused_result(
                request,
                touch_block,
                checks,
                identity=identity,
                non_claims=source_non_claims,
            )

    if not isinstance(touch_permission, Mapping):
        raise ContinuityTransferUnitError("touch_permission must be a mapping or None")
    touch_reference = _touch_reference(touch_permission, touch_permission_path)
    non_claims = _merge_non_claims(source, touch_permission)
    touch_corresponds = _touch_corresponds_to_source(
        touch_permission,
        identity,
        effective_inputs,
    )
    touch_checks_passed = _checks_all_passed(touch_permission, "touch-permission")
    checks.extend(
        [
            _check(
                "touch_permission_result_exists_and_is_readable",
                True,
                expected="one readable touch-permission result",
                actual=touch_reference.get("touch_permission_result_path"),
            ),
            _check(
                "touch_permission_result_is_successful",
                touch_permission.get("outcome")
                == touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
                expected=touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH,
                actual=touch_permission.get("outcome"),
                block_code="NO_SUCCESSFUL_TOUCH_PERMISSION_FOR_TRANSFER"
                if touch_permission.get("outcome")
                != touch_resolver.OUTCOME_ADMITTED_FOR_TOUCH
                else None,
            ),
            _check(
                "touch_permission_result_corresponds_to_source_surface",
                touch_corresponds,
                expected="touch result selected surface matches transfer source",
                actual={
                    "source": identity,
                    "touch_selected_surface": touch_permission.get(
                        "selected_current_state_surface"
                    ),
                },
                block_code="TOUCH_PERMISSION_DOES_NOT_CORRESPOND_TO_SOURCE_SURFACE"
                if not touch_corresponds
                else None,
            ),
            _check(
                "touch_permission_checks_passed",
                touch_checks_passed,
                expected="touch-permission checks all passed",
                actual="all passed" if touch_checks_passed else "one or more failed",
                block_code="TOUCH_PERMISSION_DOES_NOT_CORRESPOND_TO_SOURCE_SURFACE"
                if not touch_checks_passed
                else None,
            ),
            _check(
                "touch_class_supports_requested_transfer_class",
                _touch_class_supports_transfer(str(request["transfer_class"]), touch_permission),
                expected="admitted touch class compatible with requested transfer class",
                actual=touch_reference.get("admitted_touch_class"),
                block_code="TRANSFER_PAYLOAD_OUT_OF_SCOPE"
                if not _touch_class_supports_transfer(
                    str(request["transfer_class"]),
                    touch_permission,
                )
                else None,
            ),
        ]
    )

    try:
        effective_artifacts = _load_effective_artifacts(effective_inputs)
    except (FileNotFoundError, OSError) as exc:
        checks.append(
            _check(
                "effective_references_are_readable",
                False,
                expected="readable authority/family/status/governing artifacts",
                actual=str(exc),
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE",
            )
        )
        return _refused_result(
            request,
            "EFFECTIVE_REFERENCE_INCOHERENCE",
            checks,
            identity=identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    summaries = _effective_summaries(*effective_artifacts)
    checks.append(
        _check(
            "effective_references_are_readable",
            True,
            expected="readable authority/family/status/governing artifacts",
            actual={key: effective_inputs.get(key) for key in PATH_INPUT_KEYS},
        )
    )
    checks.extend(_effective_currentness_checks(effective_inputs, summaries))
    correspondence = _surface_path_correspondence(source, definition, effective_inputs)
    checks.extend(
        [
            _check(
                "effective_references_correspond_to_source_surface",
                correspondence,
                expected="effective references named by selected source surface",
                actual=effective_inputs,
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
                if not correspondence
                else None,
            ),
            _check(
                "transfer_uses_selected_source_surface_not_latest_files_alone",
                True,
                expected="selected current-state source surface",
                actual=selection_source,
            ),
            _check(
                "transfer_does_not_fall_back_to_stale_prior_family",
                True,
                expected="effective references named by selected source surface",
                actual=effective_inputs,
            ),
            _check(
                "transfer_class_is_supported",
                request["transfer_class"] in SUPPORTED_TRANSFER_CLASSES,
                expected=sorted(SUPPORTED_TRANSFER_CLASSES),
                actual=request["transfer_class"],
                block_code="TRANSFER_CLASS_OUT_OF_SCOPE"
                if request["transfer_class"] not in SUPPORTED_TRANSFER_CLASSES
                else None,
            ),
        ]
    )

    scope_check, payload, fields = _transfer_payload_scope(
        request,
        source,
        definition,
        identity,
        touch_permission,
        touch_reference,
        non_claims,
    )
    checks.append(scope_check)
    checks.extend(_request_refusal_checks(request))
    checks.extend(_non_claim_checks(non_claims))
    checks.append(
        _check(
            "source_derivative_distinction_preserved",
            payload is None
            or (
                payload.get("payload_derivative_status") == "carried_derivative"
                and payload.get("source_remains_source") is True
            ),
            expected="source remains source and payload remains carried derivative",
            actual=payload,
            block_code="SOURCE_DERIVATIVE_COLLAPSE_REFUSED"
            if payload is not None
            and (
                payload.get("payload_derivative_status") != "carried_derivative"
                or payload.get("source_remains_source") is not True
            )
            else None,
        )
    )

    failed = _first_failed(checks)
    if failed is not None:
        block_code = failed.get("block_code")
        if not isinstance(block_code, str) or block_code not in BLOCK_REASONS:
            block_code = "EFFECTIVE_REFERENCE_INCOHERENCE"
        return _refused_result(
            request,
            block_code,
            checks,
            identity=identity,
            touch_reference=touch_reference,
            non_claims=non_claims,
        )

    transfer_summary = {
        "transferred_field_count": len(fields),
        "transferred_field_names": list(fields),
        "source_surface_id": identity.get("selected_source_surface_id"),
        "source_surface_family": identity.get("selected_source_surface_family"),
        "touch_permission_result_id": touch_reference.get("touch_permission_result_id"),
        "transfer_basis": request.get("transfer_basis"),
        "target_seam_label": request.get("target_seam_label"),
    }
    return _result(
        request,
        identity,
        touch_reference,
        checks,
        OUTCOME_TRANSFERRED,
        None,
        payload,
        transfer_summary,
        non_claims,
    )


def resolve_continuity_transfer_unit(
    transfer_request: Mapping[str, Any],
    source_surface: Mapping[str, Any] | None = None,
    touch_permission: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded continuity-transfer-unit decision."""

    request = _normal_transfer_request(transfer_request)
    if source_surface is not None:
        if not isinstance(source_surface, Mapping):
            raise ContinuityTransferUnitError("source_surface must be a mapping or None")
        source = dict(source_surface)
        return _resolve_selected_source(
            request,
            source,
            None,
            _surface_definition_for(source),
            "provided_mapping",
            touch_permission,
            None,
        )

    source, path, definition, block_code = _select_default_source_surface()
    if block_code is not None:
        return _refused_result(
            request,
            block_code,
            [
                _check(
                    "admissible_source_surface_selected",
                    False,
                    expected="one successful current-state source surface",
                    actual=block_code,
                    block_code=block_code,
                )
            ],
        )
    if source is None:
        raise ContinuityTransferUnitError("selected source surface is unexpectedly absent")
    return _resolve_selected_source(
        request,
        source,
        path,
        definition,
        "current_state_source_surface_discovery",
        touch_permission,
        None,
    )


def resolve_continuity_transfer_unit_from_path(
    source_surface_path: Path | str,
    transfer_request: Mapping[str, Any],
    touch_permission_path: Path | str | None = None,
) -> dict[str, Any]:
    """Read one source surface and optional touch result, then resolve transfer."""

    request = _normal_transfer_request(transfer_request)
    resolved_source_path = _repo_path(source_surface_path)
    try:
        source = _read_json_file(resolved_source_path, "selected source surface")
    except (FileNotFoundError, OSError):
        return _refused_result(
            request,
            "SELECTED_SOURCE_SURFACE_UNREADABLE",
            [
                _check(
                    "selected_source_surface_exists_and_is_readable",
                    False,
                    expected="readable selected source surface",
                    actual=_display_path(resolved_source_path),
                    block_code="SELECTED_SOURCE_SURFACE_UNREADABLE",
                )
            ],
            identity=_source_surface_identity(None, None, resolved_source_path),
        )

    touch: Mapping[str, Any] | None = None
    resolved_touch_path: Path | None = None
    if touch_permission_path is not None:
        resolved_touch_path = _repo_path(touch_permission_path)
        try:
            touch = _read_json_file(resolved_touch_path, "touch-permission result")
        except (FileNotFoundError, OSError):
            definition = _surface_definition_for(source)
            identity = _source_surface_identity(source, definition, resolved_source_path)
            return _refused_result(
                request,
                "TOUCH_PERMISSION_UNREADABLE",
                [
                    _check(
                        "touch_permission_result_exists_and_is_readable",
                        False,
                        expected="readable touch-permission result",
                        actual=_display_path(resolved_touch_path),
                        block_code="TOUCH_PERMISSION_UNREADABLE",
                    )
                ],
                identity=identity,
                touch_reference=_touch_reference(None, resolved_touch_path),
                non_claims=_merge_non_claims(source),
            )

    return _resolve_selected_source(
        request,
        source,
        resolved_source_path,
        _surface_definition_for(source),
        "explicit_source_surface_path",
        touch,
        resolved_touch_path,
    )


def build_continuity_transfer_unit_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one transfer result."""

    if not isinstance(result, Mapping):
        raise ContinuityTransferUnitError("continuity-transfer result must be a mapping")
    metadata = result.get("continuity_transfer_metadata", {})
    selected = result.get("selected_source_surface", {})
    request = result.get("transfer_request", {})
    touch = result.get("touch_permission_reference", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    summary = result.get("transfer_summary", {})
    non_claims = result.get("non_claims", {})
    if not isinstance(checks, list):
        raise ContinuityTransferUnitError("continuity-transfer checks must be a list")
    passed, failed = _count_checks(checks)
    return {
        "continuity_transfer_result_id": metadata.get("continuity_transfer_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "selected_source_surface_id": selected.get("selected_source_surface_id")
        if isinstance(selected, Mapping)
        else None,
        "selected_source_surface_family": selected.get("selected_source_surface_family")
        if isinstance(selected, Mapping)
        else None,
        "transfer_class": request.get("transfer_class")
        if isinstance(request, Mapping)
        else None,
        "touch_permission_result_id": touch.get("touch_permission_result_id")
        if isinstance(touch, Mapping)
        else None,
        "transferred_field_names": summary.get("transferred_field_names")
        if isinstance(summary, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if isinstance(non_claims, Mapping)
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    selected = result.get("selected_source_surface", {})
    selected_id = selected.get("selected_source_surface_id") if isinstance(selected, Mapping) else None
    stem = _safe_filename_part(selected_id)
    root = _repo_path(CONTINUITY_TRANSFER_UNIT_ROOT)
    candidate = root / f"{stem}__continuity_transfer_unit_result.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = root / f"{stem}__continuity_transfer_unit_result_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise ContinuityTransferUnitError(
        "no bounded continuity-transfer-unit filename available"
    )


def write_continuity_transfer_unit_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive continuity-transfer-unit JSON result."""

    if not isinstance(result, Mapping):
        raise ContinuityTransferUnitError("continuity-transfer result must be a mapping")
    target = _repo_path(output_path) if output_path is not None else _default_output_path(result)
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"continuity-transfer result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
