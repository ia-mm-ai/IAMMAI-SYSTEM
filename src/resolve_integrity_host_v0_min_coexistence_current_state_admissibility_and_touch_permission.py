"""Resolve bounded current-state admissibility and touch permission.

This module consumes one already-emitted current-state surface and one bounded
touch request, verifies the effective references named by that surface where
applicable, and emits one additive touch-permission result.

It does not replay source actions into a live host, merge preserved runs,
mutate prior artifacts, complete continuity, upgrade standing, define
persistence or registry law, or convert current-state use into final
participation law.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_current_state_answer_surface as answer_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open as open_resolver
import resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now as stand_resolver


class CurrentStateTouchPermissionError(RuntimeError):
    """Raised when touch-permission inputs are malformed or impossible to use."""


CURRENT_STATE_ANSWER_SURFACE_ROOT = answer_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_QUERY_ROOT = query_resolver.CURRENT_STATE_QUERY_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = stand_resolver.CURRENT_STATE_WHAT_STANDS_NOW_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = open_resolver.CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT
CURRENT_STATE_TOUCH_PERMISSION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_touch_permissions"
)

CANONICAL_CORE_EXECUTION_FILE = query_resolver.CANONICAL_CORE_EXECUTION_FILE

TOUCH_PERMISSION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_TOUCH_PERMISSION_RESULT"
)
TOUCH_PERMISSION_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_current_state_admissibility_and_touch_permission"
)

OUTCOME_ADMITTED_FOR_TOUCH = "ADMITTED_FOR_TOUCH"
OUTCOME_REFUSED = "REFUSED"

TOUCH_CLASS_READ_ONLY = "READ_ONLY_TOUCH"
TOUCH_CLASS_REFERENCE = "REFERENCE_TOUCH"
TOUCH_CLASS_DERIVATION = "DERIVATION_TOUCH"
SUPPORTED_TOUCH_CLASSES = frozenset(
    {TOUCH_CLASS_READ_ONLY, TOUCH_CLASS_REFERENCE, TOUCH_CLASS_DERIVATION}
)

DEFAULT_TOUCH_PERMISSION_RESULT_STEM = "current_state_touch_permission_result"

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
    **open_resolver.NON_CLAIM_DEFAULTS,
    "final_current_state_admissibility_and_touch_permission_completed": False,
}

BLOCK_REASONS = {
    "NO_ADMISSIBLE_CURRENT_STATE_SURFACE": (
        "No admissible successful current-state surface is available for touch."
    ),
    "SELECTED_SURFACE_UNREADABLE": "The selected current-state surface is unreadable.",
    "SELECTED_SURFACE_MALFORMED": "The selected current-state surface is malformed.",
    "SELECTED_SURFACE_BLOCKED": "The selected current-state surface is blocked.",
    "SELECTED_SURFACE_OUT_OF_SCOPE": (
        "The selected surface is outside the bounded current-state touch scope."
    ),
    "SELECTED_SURFACE_NOT_SUCCESSFUL": (
        "The selected current-state surface does not have a supported successful outcome."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "The selected surface's effective references do not preserve the canonical execution line."
    ),
    "EFFECTIVE_REFERENCE_INCOHERENCE": (
        "The selected surface's effective references are not internally coherent."
    ),
    "EFFECTIVE_REFERENCE_DOES_NOT_CORRESPOND_TO_SELECTED_SURFACE": (
        "The effective references do not correspond to the selected surface."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Touch permission cannot fall back to stale prior-family artifacts."
    ),
    "LATEST_FILE_INFERENCE_REFUSED": (
        "Touch permission cannot infer active current state from latest files alone."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based touch permission is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based touch permission is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Touch permission cannot claim continuity completion."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Touch permission cannot silently upgrade standing."
    ),
    "TOUCH_CLASS_OUT_OF_SCOPE": (
        "The requested touch class is outside the bounded touch-permission model."
    ),
    "TOUCH_SCOPE_OUT_OF_SCOPE": (
        "The requested touch fields exceed the bounded selected-surface touch scope."
    ),
    "IMPLICIT_AUTHORITY_CLAIM_REFUSED": (
        "Touch permission cannot carry an implicit authority or final-governance claim."
    ),
    "IMPLICIT_MUTATION_REFUSED": "Touch permission cannot authorize mutation.",
    "MULTIPLE_CURRENT_STATE_SURFACES_CONFLICT_UNRESOLVED": (
        "Multiple successful current-state surfaces conflict without bounded arbitration."
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
        result_family="answer_read",
        root=CURRENT_STATE_ANSWER_SURFACE_ROOT,
        metadata_key="answer_read_metadata",
        id_key="answer_read_result_id",
        type_key="answer_read_result_type",
        expected_outcome=answer_resolver.OUTCOME_ANSWERED,
        effective_inputs_key="effective_answer_read_inputs",
        summary_key="answer_read_summary",
        payload_key="answer_read_output",
        selected_key="selected_current_state_application",
    ),
    _SurfaceDefinition(
        result_family="query",
        root=CURRENT_STATE_QUERY_ROOT,
        metadata_key="query_metadata",
        id_key="query_result_id",
        type_key="query_result_type",
        expected_outcome=query_resolver.OUTCOME_ANSWERED_QUERY,
        effective_inputs_key="effective_query_inputs",
        summary_key="query_summary",
        payload_key="query_answer",
        selected_key="selected_current_state_answer_read",
    ),
    _SurfaceDefinition(
        result_family="what_stands_now",
        root=CURRENT_STATE_WHAT_STANDS_NOW_ROOT,
        metadata_key="what_stands_now_metadata",
        id_key="what_stands_now_result_id",
        type_key="what_stands_now_result_type",
        expected_outcome=stand_resolver.OUTCOME_ANSWERED_WHAT_STANDS_NOW,
        effective_inputs_key="effective_stand_now_inputs",
        summary_key="what_stands_now_summary",
        payload_key="what_stands_now_answer",
        selected_key="selected_current_state_answer_read",
    ),
    _SurfaceDefinition(
        result_family="what_remains_open",
        root=CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT,
        metadata_key="what_remains_open_metadata",
        id_key="what_remains_open_result_id",
        type_key="what_remains_open_result_type",
        expected_outcome=open_resolver.OUTCOME_ANSWERED_WHAT_REMAINS_OPEN,
        effective_inputs_key="effective_open_inputs",
        summary_key="what_remains_open_summary",
        payload_key="what_remains_open_answer",
        selected_key="selected_current_state_answer_read",
    ),
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


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise OSError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateTouchPermissionError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(payload, dict):
        raise CurrentStateTouchPermissionError(
            f"{context} must be a JSON object: {resolved}"
        )
    return payload


def read_touch_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded touch request JSON object."""

    request = _read_json_file(path, "current-state touch request")
    return _normal_touch_request(request)


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
        value = DEFAULT_TOUCH_PERMISSION_RESULT_STEM
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or DEFAULT_TOUCH_PERMISSION_RESULT_STEM


def _same_path(left: Any, right: Any) -> bool:
    if not isinstance(left, str) or not left.strip():
        return False
    if not isinstance(right, str) or not right.strip():
        return False
    return _repo_path(left).resolve(strict=False) == _repo_path(right).resolve(
        strict=False
    )


def _normal_touch_request(request: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(request, Mapping):
        raise CurrentStateTouchPermissionError("touch request must be a mapping")

    required = (
        "touch_request_id",
        "requested_touch_class",
        "requested_touch_basis",
        "requesting_surface_label",
        "intended_downstream_use",
        "requested_touch_fields",
    )
    for key in required:
        if key not in request:
            raise CurrentStateTouchPermissionError(f"touch request is missing {key}")

    normalized: dict[str, Any] = {}
    for key in (
        "touch_request_id",
        "requested_touch_class",
        "requested_touch_basis",
        "requesting_surface_label",
        "intended_downstream_use",
    ):
        value = request.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CurrentStateTouchPermissionError(
                f"touch request {key} must be a non-empty string"
            )
        normalized[key] = value.strip()

    raw_fields = request.get("requested_touch_fields")
    if not isinstance(raw_fields, list):
        raise CurrentStateTouchPermissionError(
            "touch request requested_touch_fields must be a list"
        )
    fields: list[str] = []
    for index, value in enumerate(raw_fields):
        if not isinstance(value, str) or not value.strip():
            raise CurrentStateTouchPermissionError(
                "touch request requested_touch_fields "
                f"entry {index} must be a non-empty string"
            )
        fields.append(value.strip())
    normalized["requested_touch_fields"] = fields
    return normalized


def _surface_definition_for(
    surface: Mapping[str, Any],
) -> _SurfaceDefinition | None:
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
        raise CurrentStateTouchPermissionError(
            f"selected {definition.result_family} surface metadata must be an object"
        )
    return metadata


def _surface_effective_inputs(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
) -> dict[str, Any]:
    raw = surface.get(definition.effective_inputs_key)
    if not isinstance(raw, Mapping):
        raise CurrentStateTouchPermissionError(
            f"selected {definition.result_family} surface effective references "
            "must be an object"
        )
    result = dict(raw)
    for key in PATH_INPUT_KEYS:
        value = result.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CurrentStateTouchPermissionError(
                f"selected {definition.result_family} surface effective reference "
                f"{key} must be a non-empty string"
            )
    for key in ("effective_source_run_path", "effective_ingress_run_path"):
        value = result.get(key)
        if value is not None and (not isinstance(value, str) or not value.strip()):
            raise CurrentStateTouchPermissionError(
                f"selected {definition.result_family} surface effective reference "
                f"{key} must be a string when present"
            )
    return {key: result.get(key) for key in EFFECTIVE_INPUT_KEYS}


def _surface_identity(
    surface: Mapping[str, Any] | None,
    definition: _SurfaceDefinition | None,
    surface_path: Path | str | None,
) -> dict[str, Any]:
    if surface is None or definition is None:
        return {
            "selected_surface_path": _display_path(surface_path),
            "selected_surface_id": None,
            "selected_surface_type": None,
            "selected_surface_outcome": None
            if surface is None
            else surface.get("outcome"),
            "selected_surface_result_family": None,
            "selected_surface_effective_references": {},
        }

    metadata = _surface_metadata(surface, definition)
    surface_id = metadata.get(definition.id_key)
    if not isinstance(surface_id, str) or not surface_id.strip():
        raise CurrentStateTouchPermissionError(
            f"selected {definition.result_family} surface id is malformed"
        )
    surface_type = metadata.get(definition.type_key)
    if surface_type is not None and not isinstance(surface_type, str):
        raise CurrentStateTouchPermissionError(
            f"selected {definition.result_family} surface type is malformed"
        )
    outcome = surface.get("outcome")
    if not isinstance(outcome, str) or not outcome.strip():
        raise CurrentStateTouchPermissionError(
            f"selected {definition.result_family} surface outcome is malformed"
        )

    effective: dict[str, Any] = {}
    raw_effective = surface.get(definition.effective_inputs_key)
    if isinstance(raw_effective, Mapping):
        effective = {key: raw_effective.get(key) for key in EFFECTIVE_INPUT_KEYS}

    return {
        "selected_surface_path": _display_path(surface_path)
        if surface_path is not None
        else "provided_mapping",
        "selected_surface_id": surface_id,
        "selected_surface_type": surface_type,
        "selected_surface_outcome": outcome,
        "selected_surface_result_family": definition.result_family,
        "selected_surface_effective_references": effective,
    }


def _surface_non_claims(surface: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    if surface is None:
        return merged
    raw = surface.get("non_claims", {})
    if raw is None:
        return merged
    if not isinstance(raw, Mapping):
        raise CurrentStateTouchPermissionError(
            "selected surface non_claims must be an object"
        )
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateTouchPermissionError(
                "selected surface non_claims keys must be strings"
            )
        if not isinstance(value, bool):
            raise CurrentStateTouchPermissionError(
                f"selected surface non_claims value for {key!r} must be boolean"
            )
        merged[key] = value
    return merged


def _discover_surface_artifacts(root: Path) -> list[Path]:
    resolved = _repo_path(root)
    if not resolved.exists():
        return []
    if not resolved.is_dir():
        raise CurrentStateTouchPermissionError(
            f"current-state surface root is not a directory: {resolved}"
        )
    try:
        return sorted(path for path in resolved.glob("*.json") if path.is_file())
    except OSError as exc:
        raise CurrentStateTouchPermissionError(
            f"current-state surface root is unreadable: {resolved}"
        ) from exc


def _effective_key(surface: Mapping[str, Any], definition: _SurfaceDefinition) -> tuple[Any, ...]:
    raw = surface.get(definition.effective_inputs_key)
    if not isinstance(raw, Mapping):
        return ()
    return tuple(raw.get(key) for key in EFFECTIVE_INPUT_KEYS)


def _select_default_current_state_surface() -> tuple[
    Mapping[str, Any] | None,
    Path | None,
    _SurfaceDefinition | None,
    str | None,
]:
    candidates: list[tuple[str, Mapping[str, Any], Path, _SurfaceDefinition]] = []

    for definition in SURFACE_DEFINITIONS:
        for path in _discover_surface_artifacts(definition.root):
            try:
                surface = _read_json_file(path, "current-state surface artifact")
            except (FileNotFoundError, OSError):
                continue
            found = _surface_definition_for(surface)
            if found != definition:
                continue
            if surface.get("outcome") != definition.expected_outcome:
                continue
            candidates.append((_display_path(path) or str(path), surface, path, definition))

    if not candidates:
        return None, None, None, "NO_ADMISSIBLE_CURRENT_STATE_SURFACE"

    keys = {
        _effective_key(surface, definition)
        for _, surface, _, definition in candidates
    }
    if len(keys) > 1:
        return None, None, None, "MULTIPLE_CURRENT_STATE_SURFACES_CONFLICT_UNRESOLVED"

    _, surface, path, definition = sorted(candidates, key=lambda item: item[0])[-1]
    return surface, path, definition, None


def _refused_result(
    touch_request: Mapping[str, Any],
    block_code: str,
    checks: Sequence[Mapping[str, Any]],
    selected_surface: Mapping[str, Any] | None = None,
    definition: _SurfaceDefinition | None = None,
    surface_path: Path | str | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    identity = _surface_identity(selected_surface, definition, surface_path)
    carried_non_claims = dict(non_claims or _surface_non_claims(selected_surface))
    return _result(
        touch_request=touch_request,
        selected_surface_identity=identity,
        checks=checks,
        outcome=OUTCOME_REFUSED,
        block_code=block_code,
        block_reason=BLOCK_REASONS[block_code],
        admitted_touch_scope=None,
        non_claims=carried_non_claims,
    )


def _result_id(
    selected_surface_id: Any,
    touch_request: Mapping[str, Any],
    outcome: str,
) -> str:
    surface_part = selected_surface_id if isinstance(selected_surface_id, str) else "no_surface"
    request_part = touch_request.get("touch_request_id")
    if not isinstance(request_part, str) or not request_part:
        request_part = "touch_request"
    outcome_part = "admitted" if outcome == OUTCOME_ADMITTED_FOR_TOUCH else "refused"
    return f"{surface_part}__{request_part}__current_state_touch_permission_{outcome_part}"


def _result(
    touch_request: Mapping[str, Any],
    selected_surface_identity: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    admitted_touch_scope: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    result_id = _result_id(
        selected_surface_identity.get("selected_surface_id"),
        touch_request,
        outcome,
    )
    return {
        "touch_permission_metadata": {
            "touch_permission_result_id": result_id,
            "touch_permission_result_type": TOUCH_PERMISSION_RESULT_TYPE,
            "touch_permission_result_version": TOUCH_PERMISSION_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_surface": dict(selected_surface_identity),
        "touch_request": dict(touch_request),
        "checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "admitted_touch_scope": (
            dict(admitted_touch_scope) if admitted_touch_scope is not None else None
        ),
        "non_claims": dict(non_claims),
    }


def _load_effective_artifacts(
    effective_inputs: Mapping[str, Any],
) -> tuple[dict[str, Any], dict[str, Any], dict[str, Any], dict[str, Any]]:
    try:
        authority = _read_json_file(
            str(effective_inputs["effective_authority_artifact_path"]),
            "effective authority artifact",
        )
        family = _read_json_file(
            str(effective_inputs["effective_family_packet_path"]),
            "effective run-family packet",
        )
        status = _read_json_file(
            str(effective_inputs["effective_status_packet_path"]),
            "effective preserved-run status packet",
        )
        governing = _read_json_file(
            str(effective_inputs["effective_current_governing_packet_path"]),
            "effective current-governing packet",
        )
    except (FileNotFoundError, OSError) as exc:
        raise _UnreadableEffectiveReference(str(exc)) from exc
    return authority, family, status, governing


class _UnreadableEffectiveReference(RuntimeError):
    """Private marker for ordinary unreadable-reference refusal."""


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
    except Exception as exc:  # noqa: BLE001 - convert local malformed artifacts clearly.
        raise CurrentStateTouchPermissionError(
            "effective reference artifact is malformed"
        ) from exc


def _source_values(
    effective_inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[Any]:
    return [
        effective_inputs.get("effective_source_run_path"),
        summaries["authority"].get("selected_source_run_directory_path"),
        summaries["family"].get("current_authority_source_run_path"),
        summaries["status"].get("selected_current_authority_source_run_path"),
        summaries["governing"].get("current_governing_source_run_path"),
    ]


def _ingress_values(
    effective_inputs: Mapping[str, Any],
    summaries: Mapping[str, Mapping[str, Any]],
) -> list[Any]:
    return [
        effective_inputs.get("effective_ingress_run_path"),
        summaries["authority"].get("selected_ingress_run_directory_path"),
        summaries["family"].get("current_authority_ingress_run_path"),
        summaries["governing"].get("current_governing_ingress_run_path"),
    ]


def _all_exposed_paths_match(values: Sequence[Any]) -> bool:
    exposed = [value for value in values if isinstance(value, str) and value.strip()]
    if len(exposed) < 2:
        return True
    first = exposed[0]
    return all(_same_path(first, value) for value in exposed[1:])


def _surface_path_correspondence(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
    effective_inputs: Mapping[str, Any],
) -> bool:
    for section_key in (definition.payload_key, definition.summary_key):
        section = surface.get(section_key)
        if not isinstance(section, Mapping):
            continue
        path_pairs = (
            ("current_authority_artifact_path", "effective_authority_artifact_path"),
            ("current_family_packet_path", "effective_family_packet_path"),
            ("current_status_packet_path", "effective_status_packet_path"),
            (
                "current_governing_packet_path",
                "effective_current_governing_packet_path",
            ),
            ("current_governing_source_run_path", "effective_source_run_path"),
            ("effective_current_governing_source_run_path", "effective_source_run_path"),
            ("current_governing_ingress_run_path", "effective_ingress_run_path"),
            (
                "effective_current_governing_ingress_run_path",
                "effective_ingress_run_path",
            ),
        )
        for section_key_name, input_key in path_pairs:
            value = section.get(section_key_name)
            expected = effective_inputs.get(input_key)
            if isinstance(value, str) and value.strip():
                if isinstance(expected, str) and expected.strip():
                    if not _same_path(value, expected):
                        return False
    return True


def _selected_surface_checks_passed(surface: Mapping[str, Any]) -> bool:
    checks = surface.get("checks", [])
    if not isinstance(checks, list):
        raise CurrentStateTouchPermissionError("selected surface checks must be a list")
    return all(isinstance(check, Mapping) and check.get("passed") is True for check in checks)


def _shortcut_text(touch_request: Mapping[str, Any]) -> str:
    return " ".join(
        str(touch_request.get(key, ""))
        for key in (
            "requested_touch_basis",
            "requesting_surface_label",
            "intended_downstream_use",
        )
    ).lower()


def _contains_any(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _request_refusal_checks(touch_request: Mapping[str, Any]) -> list[dict[str, Any]]:
    text = _shortcut_text(touch_request)
    return [
        _check(
            "touch_request_does_not_attempt_replay",
            not _contains_any(
                text,
                (
                    "replay into",
                    "replay-based",
                    "perform replay",
                    "allow replay",
                    "permission to replay",
                    "use replay",
                ),
            ),
            expected="no replay shortcut",
            actual=touch_request.get("intended_downstream_use"),
            block_code="REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "touch_request_does_not_attempt_merge",
            not _contains_any(
                text,
                (
                    "merge into",
                    "merge-based",
                    "perform merge",
                    "allow merge",
                    "permission to merge",
                    "use merge",
                ),
            ),
            expected="no merge shortcut",
            actual=touch_request.get("intended_downstream_use"),
            block_code="MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "touch_request_does_not_claim_continuity_completion",
            not _contains_any(
                text,
                (
                    "complete continuity",
                    "continuity completion",
                    "claim continuity",
                    "continuity completed",
                ),
            ),
            expected="no continuity-completion claim",
            actual=touch_request.get("intended_downstream_use"),
            block_code="CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "touch_request_does_not_silently_upgrade_standing",
            not _contains_any(
                text,
                (
                    "standing upgrade",
                    "upgrade standing",
                    "promote standing",
                    "standing upgraded",
                ),
            ),
            expected="no standing upgrade",
            actual=touch_request.get("intended_downstream_use"),
            block_code="SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "touch_request_does_not_request_stale_prior_family_fallback",
            not _contains_any(
                text,
                ("stale prior", "prior-family fallback", "fallback to prior"),
            ),
            expected="no stale prior-family fallback",
            actual=touch_request.get("requested_touch_basis"),
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "touch_request_does_not_infer_from_latest_files",
            not _contains_any(
                text,
                (
                    "latest authority",
                    "latest family",
                    "latest status",
                    "latest governing",
                    "latest file",
                    "latest artifact",
                ),
            ),
            expected="no latest-file inference",
            actual=touch_request.get("requested_touch_basis"),
            block_code="LATEST_FILE_INFERENCE_REFUSED",
        ),
        _check(
            "touch_request_does_not_claim_implicit_authority",
            not _contains_any(
                text,
                (
                    "final governance",
                    "system law",
                    "protocol law",
                    "governing standing",
                    "authority claim",
                    "become governor",
                    "constitutional author",
                ),
            ),
            expected="no implicit authority claim",
            actual=touch_request.get("intended_downstream_use"),
            block_code="IMPLICIT_AUTHORITY_CLAIM_REFUSED",
        ),
        _check(
            "touch_request_does_not_authorize_mutation",
            not _contains_any(
                text,
                (
                    "mutate",
                    "rewrite",
                    "overwrite",
                    "delete prior",
                    "modify prior",
                    "patch prior",
                ),
            ),
            expected="no mutation authority",
            actual=touch_request.get("intended_downstream_use"),
            block_code="IMPLICIT_MUTATION_REFUSED",
        ),
    ]


def _touch_scope_sets(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
) -> tuple[set[str], set[str], set[str]]:
    metadata_fields = set(surface.get(definition.metadata_key, {}))
    effective_fields = set(surface.get(definition.effective_inputs_key, {}))
    summary = surface.get(definition.summary_key, {})
    payload = surface.get(definition.payload_key, {})
    selected = surface.get(definition.selected_key or "", {})
    non_claims = surface.get("non_claims", {})

    read_fields = set(surface.keys()) | {
        "metadata",
        "selected_surface",
        "selected_surface_path",
        "selected_surface_id",
        "selected_surface_type",
        "selected_surface_outcome",
        "selected_surface_result_family",
        "effective_references",
        "summary",
        "payload",
        "checks",
        "outcome",
        "block",
        "non_claims",
    }
    read_fields.update(str(key) for key in metadata_fields)
    read_fields.update(str(key) for key in effective_fields)
    if isinstance(summary, Mapping):
        read_fields.update(str(key) for key in summary)
    if isinstance(payload, Mapping):
        read_fields.update(str(key) for key in payload)
        answered_fields = payload.get("answered_fields")
        if isinstance(answered_fields, Mapping):
            read_fields.update(str(key) for key in answered_fields)

    reference_fields = {
        "selected_surface_path",
        "selected_surface_id",
        "selected_surface_type",
        "selected_surface_outcome",
        "selected_surface_result_family",
        "selected_surface_effective_references",
        "surface_path",
        "surface_id",
        "surface_type",
        "outcome",
        "result_family",
        "effective_references",
        "non_claims",
    } | set(EFFECTIVE_INPUT_KEYS)
    if isinstance(selected, Mapping):
        reference_fields.update(str(key) for key in selected)
    reference_fields.update(metadata_fields)

    derivation_fields = {"non_claims"} | {
        str(key) for key in non_claims if isinstance(key, str)
    }
    if isinstance(summary, Mapping):
        derivation_fields.update(str(key) for key in summary)
    if isinstance(payload, Mapping):
        derivation_fields.update(str(key) for key in payload)
        answered_fields = payload.get("answered_fields")
        if isinstance(answered_fields, Mapping):
            derivation_fields.update(str(key) for key in answered_fields)
    derivation_fields.update(effective_fields)

    return read_fields, reference_fields, derivation_fields


def _touch_scope_check(
    surface: Mapping[str, Any],
    definition: _SurfaceDefinition,
    touch_request: Mapping[str, Any],
) -> tuple[dict[str, Any], list[str], list[str]]:
    requested_class = touch_request["requested_touch_class"]
    requested_fields = list(touch_request["requested_touch_fields"])
    read_fields, reference_fields, derivation_fields = _touch_scope_sets(
        surface, definition
    )

    if requested_class == TOUCH_CLASS_READ_ONLY:
        allowed = read_fields
        admitted = sorted(read_fields) if not requested_fields else requested_fields
        invalid = [field for field in requested_fields if field not in allowed]
    elif requested_class == TOUCH_CLASS_REFERENCE:
        allowed = reference_fields
        admitted = requested_fields
        invalid = [field for field in requested_fields if field not in allowed]
        if not requested_fields:
            invalid = ["requested_touch_fields"]
    elif requested_class == TOUCH_CLASS_DERIVATION:
        allowed = derivation_fields
        admitted = requested_fields
        invalid = [field for field in requested_fields if field not in allowed]
        if not requested_fields:
            invalid = ["requested_touch_fields"]
    else:
        return (
            _check(
                "touch_class_is_supported",
                False,
                expected=sorted(SUPPORTED_TOUCH_CLASSES),
                actual=requested_class,
                block_code="TOUCH_CLASS_OUT_OF_SCOPE",
            ),
            [],
            [requested_class],
        )

    return (
        _check(
            "touch_scope_is_bounded_to_selected_surface",
            not invalid,
            expected=sorted(allowed),
            actual=requested_fields,
            block_code="TOUCH_SCOPE_OUT_OF_SCOPE" if invalid else None,
        ),
        admitted,
        invalid,
    )


def _admitted_scope(
    identity: Mapping[str, Any],
    touch_request: Mapping[str, Any],
    admitted_fields: Sequence[str],
) -> dict[str, Any]:
    requested_class = touch_request["requested_touch_class"]
    scope = {
        "admitted_touch_class": requested_class,
        "admitted_source_surface_path": identity.get("selected_surface_path"),
        "admitted_source_surface_id": identity.get("selected_surface_id"),
        "admitted_readable_fields": list(admitted_fields)
        if requested_class == TOUCH_CLASS_READ_ONLY
        else [],
        "admitted_reference_fields": list(admitted_fields)
        if requested_class == TOUCH_CLASS_REFERENCE
        else [],
        "admitted_derivation_boundary": None,
        "replay_refused": True,
        "merge_refused": True,
        "mutation_refused": True,
        "continuity_completion_refused": True,
        "standing_upgrade_refused": True,
    }
    if requested_class == TOUCH_CLASS_DERIVATION:
        scope["admitted_derivation_boundary"] = {
            "derived_only_from_selected_surface": True,
            "admitted_derivation_fields": list(admitted_fields),
            "does_not_create_new_ontology": True,
        }
    return scope


def _canonical_check(summaries: Mapping[str, Mapping[str, Any]]) -> dict[str, Any]:
    actual = {
        name: summary.get("core_execution_file")
        for name, summary in summaries.items()
    }
    passed = all(value == CANONICAL_CORE_EXECUTION_FILE for value in actual.values())
    return _check(
        "canonical_core_execution_file_aligned",
        passed,
        expected=CANONICAL_CORE_EXECUTION_FILE,
        actual=actual,
        block_code="CANONICAL_EXECUTION_LINE_MISMATCH" if not passed else None,
    )


def _non_claim_checks(non_claims: Mapping[str, bool]) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    for key in REQUIRED_FALSE_NON_CLAIMS:
        code = {
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
                block_code=code if non_claims.get(key) is not False else None,
            )
        )

    finality_failures = {
        key: value
        for key, value in non_claims.items()
        if key.startswith("final_") or key == "minimum_lawful_system_completed"
        if value is not False
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


def _resolve_selected_surface(
    touch_request: Mapping[str, Any],
    surface: Mapping[str, Any],
    surface_path: Path | str | None,
    definition: _SurfaceDefinition | None,
    selection_source: str,
) -> dict[str, Any]:
    if definition is None:
        definition = _surface_definition_for(surface)

    if definition is None:
        checks = [
            _check(
                "selected_surface_is_in_touch_scope",
                False,
                expected=[definition.result_family for definition in SURFACE_DEFINITIONS],
                actual="unrecognized current-state surface",
                block_code="SELECTED_SURFACE_OUT_OF_SCOPE",
            )
        ]
        return _refused_result(
            touch_request,
            "SELECTED_SURFACE_OUT_OF_SCOPE",
            checks,
            selected_surface=surface,
            definition=None,
            surface_path=surface_path,
        )

    identity = _surface_identity(surface, definition, surface_path)
    non_claims = _surface_non_claims(surface)
    outcome = surface.get("outcome")

    if outcome == "BLOCKED":
        return _refused_result(
            touch_request,
            "SELECTED_SURFACE_BLOCKED",
            [
                _check(
                    "selected_surface_has_successful_outcome",
                    False,
                    expected=definition.expected_outcome,
                    actual=outcome,
                    block_code="SELECTED_SURFACE_BLOCKED",
                )
            ],
            selected_surface=surface,
            definition=definition,
            surface_path=surface_path,
            non_claims=non_claims,
        )

    if outcome != definition.expected_outcome:
        return _refused_result(
            touch_request,
            "SELECTED_SURFACE_NOT_SUCCESSFUL",
            [
                _check(
                    "selected_surface_has_successful_outcome",
                    False,
                    expected=definition.expected_outcome,
                    actual=outcome,
                    block_code="SELECTED_SURFACE_NOT_SUCCESSFUL",
                )
            ],
            selected_surface=surface,
            definition=definition,
            surface_path=surface_path,
            non_claims=non_claims,
        )

    effective_inputs = _surface_effective_inputs(surface, definition)
    checks: list[dict[str, Any]] = [
        _check(
            "selected_surface_exists_and_is_readable",
            True,
            expected="one readable selected current-state surface",
            actual=identity.get("selected_surface_path"),
        ),
        _check(
            "selected_surface_has_successful_outcome",
            True,
            expected=definition.expected_outcome,
            actual=outcome,
        ),
        _check(
            "selected_surface_is_in_touch_scope",
            True,
            expected=[item.result_family for item in SURFACE_DEFINITIONS],
            actual=definition.result_family,
        ),
        _check(
            "selected_surface_identity_preserved",
            bool(identity.get("selected_surface_id"))
            and bool(identity.get("selected_surface_result_family")),
            expected="path, id, family, type, and outcome preserved",
            actual=identity,
            block_code="SELECTED_SURFACE_MALFORMED"
            if not identity.get("selected_surface_id")
            else None,
        ),
        _check(
            "selected_surface_checks_passed",
            _selected_surface_checks_passed(surface),
            expected="selected source surface checks all passed",
            actual="all passed"
            if _selected_surface_checks_passed(surface)
            else "one or more failed",
            block_code="EFFECTIVE_REFERENCE_DOES_NOT_CORRESPOND_TO_SELECTED_SURFACE"
            if not _selected_surface_checks_passed(surface)
            else None,
        ),
    ]

    try:
        authority, family, status, governing = _load_effective_artifacts(effective_inputs)
    except _UnreadableEffectiveReference as exc:
        checks.append(
            _check(
                "effective_references_are_readable",
                False,
                expected="readable effective authority/family/status/governing artifacts",
                actual=str(exc),
                block_code="EFFECTIVE_REFERENCE_INCOHERENCE",
            )
        )
        return _refused_result(
            touch_request,
            "EFFECTIVE_REFERENCE_INCOHERENCE",
            checks,
            selected_surface=surface,
            definition=definition,
            surface_path=surface_path,
            non_claims=non_claims,
        )

    summaries = _effective_summaries(authority, family, status, governing)
    checks.append(
        _check(
            "effective_references_are_readable",
            True,
            expected="readable effective authority/family/status/governing artifacts",
            actual={key: effective_inputs.get(key) for key in PATH_INPUT_KEYS},
        )
    )
    checks.append(_canonical_check(summaries))

    source_values = _source_values(effective_inputs, summaries)
    source_passed = _all_exposed_paths_match(source_values)
    checks.append(
        _check(
            "effective_references_share_current_governing_source_run_where_exposed",
            source_passed,
            expected="same current governing source run where exposed",
            actual=source_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not source_passed
            else None,
        )
    )

    ingress_values = _ingress_values(effective_inputs, summaries)
    ingress_passed = _all_exposed_paths_match(ingress_values)
    checks.append(
        _check(
            "effective_references_share_current_governing_ingress_run_where_exposed",
            ingress_passed,
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_REFERENCE_INCOHERENCE"
            if not ingress_passed
            else None,
        )
    )

    correspondence_passed = _surface_path_correspondence(
        surface,
        definition,
        effective_inputs,
    )
    checks.append(
        _check(
            "effective_references_correspond_to_selected_surface",
            correspondence_passed,
            expected="effective references named by selected current-state surface",
            actual=effective_inputs,
            block_code="EFFECTIVE_REFERENCE_DOES_NOT_CORRESPOND_TO_SELECTED_SURFACE"
            if not correspondence_passed
            else None,
        )
    )

    checks.append(
        _check(
            "touch_uses_selected_current_state_surface_not_latest_files_alone",
            True,
            expected="selected current-state surface",
            actual=selection_source,
        )
    )
    checks.append(
        _check(
            "touch_does_not_fall_back_to_stale_prior_family",
            True,
            expected="effective references named by selected surface",
            actual=effective_inputs,
        )
    )

    requested_class = touch_request["requested_touch_class"]
    checks.append(
        _check(
            "touch_class_is_supported",
            requested_class in SUPPORTED_TOUCH_CLASSES,
            expected=sorted(SUPPORTED_TOUCH_CLASSES),
            actual=requested_class,
            block_code="TOUCH_CLASS_OUT_OF_SCOPE"
            if requested_class not in SUPPORTED_TOUCH_CLASSES
            else None,
        )
    )

    scope_check, admitted_fields, _invalid_fields = _touch_scope_check(
        surface, definition, touch_request
    )
    checks.append(scope_check)
    checks.extend(_request_refusal_checks(touch_request))
    checks.extend(_non_claim_checks(non_claims))

    failed = _first_failed(checks)
    if failed is not None:
        block_code = failed.get("block_code")
        if not isinstance(block_code, str) or block_code not in BLOCK_REASONS:
            block_code = "EFFECTIVE_REFERENCE_INCOHERENCE"
        return _refused_result(
            touch_request,
            block_code,
            checks,
            selected_surface=surface,
            definition=definition,
            surface_path=surface_path,
            non_claims=non_claims,
        )

    admitted = _admitted_scope(identity, touch_request, admitted_fields)
    return _result(
        touch_request=touch_request,
        selected_surface_identity=identity,
        checks=checks,
        outcome=OUTCOME_ADMITTED_FOR_TOUCH,
        block_code=None,
        block_reason=None,
        admitted_touch_scope=admitted,
        non_claims=non_claims,
    )


def resolve_current_state_touch_permission(
    touch_request: Mapping[str, Any],
    current_state_surface: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded admissibility and touch-permission decision."""

    request = _normal_touch_request(touch_request)

    if current_state_surface is not None:
        if not isinstance(current_state_surface, Mapping):
            raise CurrentStateTouchPermissionError(
                "current_state_surface must be a mapping or None"
            )
        surface = dict(current_state_surface)
        definition = _surface_definition_for(surface)
        return _resolve_selected_surface(
            request,
            surface,
            None,
            definition,
            selection_source="provided_mapping",
        )

    surface, path, definition, block_code = _select_default_current_state_surface()
    if block_code is not None:
        return _refused_result(
            request,
            block_code,
            [
                _check(
                    "admissible_current_state_surface_selected",
                    False,
                    expected="one successful current-state surface",
                    actual=block_code,
                    block_code=block_code,
                )
            ],
            selected_surface=None,
            definition=None,
            surface_path=None,
        )

    if surface is None:
        raise CurrentStateTouchPermissionError(
            "selected current-state surface is unexpectedly absent"
        )
    return _resolve_selected_surface(
        request,
        surface,
        path,
        definition,
        selection_source="current_state_surface_discovery",
    )


def resolve_current_state_touch_permission_from_path(
    path: Path | str,
    touch_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one current-state surface artifact and resolve touch permission."""

    request = _normal_touch_request(touch_request)
    surface_path = _repo_path(path)
    try:
        surface = _read_json_file(surface_path, "selected current-state surface")
    except (FileNotFoundError, OSError):
        return _refused_result(
            request,
            "SELECTED_SURFACE_UNREADABLE",
            [
                _check(
                    "selected_surface_exists_and_is_readable",
                    False,
                    expected="readable selected current-state surface",
                    actual=_display_path(surface_path),
                    block_code="SELECTED_SURFACE_UNREADABLE",
                )
            ],
            selected_surface=None,
            definition=None,
            surface_path=surface_path,
        )

    definition = _surface_definition_for(surface)
    return _resolve_selected_surface(
        request,
        surface,
        surface_path,
        definition,
        selection_source="explicit_current_state_surface_path",
    )


def build_current_state_touch_permission_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one touch-permission result."""

    if not isinstance(result, Mapping):
        raise CurrentStateTouchPermissionError(
            "touch-permission result must be a mapping"
        )
    metadata = result.get("touch_permission_metadata", {})
    selected = result.get("selected_current_state_surface", {})
    request = result.get("touch_request", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    scope = result.get("admitted_touch_scope", {})
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateTouchPermissionError(
            "touch-permission checks must be a list"
        )
    passed, failed = _count_checks(checks)

    return {
        "touch_permission_result_id": metadata.get("touch_permission_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason")
        if isinstance(block, Mapping)
        else None,
        "selected_current_state_surface_id": selected.get("selected_surface_id")
        if isinstance(selected, Mapping)
        else None,
        "selected_result_family": selected.get("selected_surface_result_family")
        if isinstance(selected, Mapping)
        else None,
        "requested_touch_class": request.get("requested_touch_class")
        if isinstance(request, Mapping)
        else None,
        "admitted_touch_class": scope.get("admitted_touch_class")
        if isinstance(scope, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in REQUIRED_FALSE_NON_CLAIMS
            if isinstance(non_claims, Mapping)
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_STATE_TOUCH_PERMISSION_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_current_state_surface", {})
    selected_id = None
    if isinstance(selected, Mapping):
        selected_id = selected.get("selected_surface_id")
    stem = _safe_filename_part(selected_id)
    candidate = resolved_root / f"{stem}__{DEFAULT_TOUCH_PERMISSION_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            resolved_root
            / f"{stem}__{DEFAULT_TOUCH_PERMISSION_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentStateTouchPermissionError(
        "no bounded current-state touch-permission filename available"
    )


def write_current_state_touch_permission_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-state touch-permission JSON result."""

    if not isinstance(result, Mapping):
        raise CurrentStateTouchPermissionError(
            "touch-permission result must be a mapping"
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"current-state touch-permission result already exists: {target}"
        )
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
