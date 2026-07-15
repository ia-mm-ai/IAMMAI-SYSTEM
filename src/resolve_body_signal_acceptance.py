"""Resolve one bounded body-signal acceptance request.

This module evaluates exactly one ``SIGNAL_RECOGNIZED`` result and one
signal-acceptance request. It decides only whether that recognized signal may
enter one declared bounded matter for structured handling.

Acceptance is not scope, presence, threshold, truth, authority, permission,
action, routing, workflow, or body relevance medium implementation. This
resolver does not discover signals, route signals, replay the host, mutate
upstream artifacts, aggregate signals, schedule work, or create follow-on
authorization.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class BodySignalAcceptanceError(RuntimeError):
    """Raised for malformed inputs or impossible acceptance correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_recognition: Mapping[str, Any] | None = None,
        selected_request: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_recognition = (
            copy.deepcopy(dict(selected_recognition))
            if isinstance(selected_recognition, Mapping)
            else None
        )
        self.selected_request = (
            copy.deepcopy(dict(selected_request))
            if isinstance(selected_request, Mapping)
            else None
        )
        self.checks = [dict(check) for check in checks] if checks is not None else None


BODY_SIGNAL_ACCEPTANCE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance"
)

RESOLVER_MODULE = "resolve_body_signal_acceptance"
BODY_SIGNAL_ACCEPTANCE_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_ACCEPTANCE_RESULT"
)
BODY_SIGNAL_ACCEPTANCE_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "body_signal_acceptance_result"

OUTCOME_SIGNAL_ACCEPTED = "SIGNAL_ACCEPTED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_SIGNAL_RECOGNIZED = "SIGNAL_RECOGNIZED"

SUPPORTED_MATTER_ID = "current_signal_recognition_standing"
SUPPORTED_MATTER_FAMILY = "body_signal_acceptance_matter"
SUPPORTED_MATTER_KIND = "recognized_body_signal_posture"

REQUEST_SECTIONS = (
    "signal_acceptance_request_metadata",
    "recognized_signal_basis",
    "declared_matter",
    "declared_acceptance_scope",
    "hierarchy_constraints",
    "correspondence_requirements",
    "declared_non_claims",
)

REQUEST_METADATA_FIELDS = (
    "signal_acceptance_request_id",
    "signal_acceptance_request_type",
    "signal_acceptance_request_version",
    "declared_at",
    "declared_by_surface",
)

RECOGNIZED_SIGNAL_BASIS_FIELDS = (
    "signal_recognition_result_path",
    "signal_recognition_result_id",
    "signal_recognition_result_version",
    "signal_recognition_outcome",
    "signal_recognition_resolver_module",
    "recognized_signal_category",
    "recognized_source_artifact_id",
    "recognized_source_artifact_path",
    "recognized_source_artifact_family",
    "recognized_source_artifact_outcome",
)

DECLARED_MATTER_FIELDS = (
    "matter_id",
    "matter_family",
    "matter_kind",
    "matter_purpose",
    "matter_boundary",
)

ACCEPTANCE_SCOPE_TRUE_FIELDS = (
    "acceptance_for_structured_handling_only",
    "scope_not_yet_assigned",
    "presence_not_yet_established",
    "threshold_not_yet_met",
    "truth_not_created",
    "action_not_authorized",
    "routing_not_created",
    "workflow_not_created",
    "follow_on_work_not_authorized",
)

SCOPE_FIELD_BLOCK_CODES = {
    "acceptance_for_structured_handling_only": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "scope_not_yet_assigned": "ACCEPTANCE_ATTEMPTS_SCOPE",
    "presence_not_yet_established": "ACCEPTANCE_ATTEMPTS_PRESENCE",
    "threshold_not_yet_met": "ACCEPTANCE_ATTEMPTS_THRESHOLD",
    "truth_not_created": "ACCEPTANCE_ATTEMPTS_TRUTH",
    "action_not_authorized": "ACCEPTANCE_ATTEMPTS_ACTION_AUTHORIZATION",
    "routing_not_created": "ACCEPTANCE_ATTEMPTS_SIGNAL_ROUTER",
    "workflow_not_created": "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
    "follow_on_work_not_authorized": "ACCEPTANCE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION",
}

HIERARCHY_FALSE_FIELDS = (
    "accepted_signal_allowed_as_authority",
    "accepted_signal_allowed_as_permission",
    "accepted_signal_allowed_as_currentness",
    "accepted_signal_allowed_as_truth",
    "accepted_signal_allowed_as_scope",
    "accepted_signal_allowed_as_presence",
    "accepted_signal_allowed_as_threshold",
    "accepted_signal_allowed_as_action_trigger",
    "accepted_signal_allowed_as_workflow",
    "accepted_signal_allowed_as_route",
    "accepted_signal_allowed_as_body_relevance_medium",
    "derivative_signal_allowed_as_source",
    "operator_signal_allowed_as_source",
    "reentry_signal_allowed_as_governing_basis",
    "latest_file_recency_allowed",
)

HIERARCHY_FIELD_BLOCK_CODES = {
    "accepted_signal_allowed_as_authority": "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY",
    "accepted_signal_allowed_as_permission": "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION",
    "accepted_signal_allowed_as_currentness": "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS",
    "accepted_signal_allowed_as_truth": "ACCEPTANCE_ATTEMPTS_TRUTH",
    "accepted_signal_allowed_as_scope": "ACCEPTANCE_ATTEMPTS_SCOPE",
    "accepted_signal_allowed_as_presence": "ACCEPTANCE_ATTEMPTS_PRESENCE",
    "accepted_signal_allowed_as_threshold": "ACCEPTANCE_ATTEMPTS_THRESHOLD",
    "accepted_signal_allowed_as_action_trigger": "ACCEPTANCE_ATTEMPTS_ACTION_AUTHORIZATION",
    "accepted_signal_allowed_as_workflow": "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
    "accepted_signal_allowed_as_route": "DECLARED_MATTER_ATTEMPTS_ROUTING",
    "accepted_signal_allowed_as_body_relevance_medium": (
        "ACCEPTANCE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
    ),
    "derivative_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "operator_signal_allowed_as_source": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "reentry_signal_allowed_as_governing_basis": "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = (
    "must_preserve_recognized_signal_identity",
    "must_preserve_recognized_source_identity",
    "must_preserve_signal_category",
    "must_preserve_signal_non_authority",
    "must_preserve_signal_non_permission",
    "must_preserve_signal_non_currentness",
    "must_preserve_matter_boundary",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

CORRESPONDENCE_FIELD_BLOCK_CODES = {
    "must_preserve_recognized_signal_identity": "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH",
    "must_preserve_recognized_source_identity": "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
    "must_preserve_signal_category": "SIGNAL_CATEGORY_MISMATCH",
    "must_preserve_signal_non_authority": "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY",
    "must_preserve_signal_non_permission": "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION",
    "must_preserve_signal_non_currentness": "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS",
    "must_preserve_matter_boundary": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
    "must_prevent_under_mirroring": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_create_truth",
    "does_not_create_scope",
    "does_not_establish_presence",
    "does_not_meet_threshold",
    "does_not_authorize_action",
    "does_not_authorize_follow_on_work",
    "does_not_create_workflow",
    "does_not_create_roadmap",
    "does_not_create_signal_router",
    "does_not_create_event_bus",
    "does_not_create_body_relevance_medium",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_turn_receipt_into_permission",
)

RESULT_NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "truth_created": False,
    "scope_assigned": False,
    "presence_established": False,
    "threshold_met": False,
    "action_authorized": False,
    "follow_on_work_authorized": False,
    "workflow_created": False,
    "roadmap_created": False,
    "signal_router_created": False,
    "event_bus_created": False,
    "body_relevance_medium_created": False,
    "source_replaced": False,
    "derivative_upgraded_to_source": False,
    "receipt_turned_into_permission": False,
}

BLOCK_REASONS = {
    "SIGNAL_RECOGNITION_RESULT_MISSING": "A signal-recognition result is required.",
    "SIGNAL_RECOGNITION_RESULT_UNREADABLE": (
        "The explicit signal-recognition result path could not be read."
    ),
    "SIGNAL_RECOGNITION_RESULT_MALFORMED": (
        "The selected signal-recognition result is malformed."
    ),
    "SIGNAL_RECOGNITION_RESULT_NOT_RECOGNIZED": (
        "The selected signal-recognition result is not SIGNAL_RECOGNIZED."
    ),
    "RECOGNIZED_SIGNAL_MISSING": "The selected recognition result has no recognized signal.",
    "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH": (
        "The acceptance request does not preserve recognized signal identity."
    ),
    "RECOGNIZED_SOURCE_IDENTITY_MISMATCH": (
        "The acceptance request does not preserve recognized source identity."
    ),
    "SIGNAL_CATEGORY_MISMATCH": (
        "The acceptance request does not preserve recognized signal category."
    ),
    "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY": (
        "The recognized signal is treated as authority."
    ),
    "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION": (
        "The recognized signal is treated as permission."
    ),
    "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS": (
        "The recognized signal is treated as currentness."
    ),
    "SIGNAL_ACCEPTANCE_REQUEST_MISSING": "A signal-acceptance request is required.",
    "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED": (
        "The signal-acceptance request is malformed."
    ),
    "DECLARED_MATTER_MISSING": "The acceptance request does not declare a matter.",
    "DECLARED_MATTER_UNSUPPORTED": "The declared matter is not supported.",
    "DECLARED_MATTER_VAGUE_OR_UNBOUNDED": (
        "The declared matter is vague, unbounded, or over-mirrored."
    ),
    "DECLARED_MATTER_ATTEMPTS_ACTION": "The declared matter attempts action.",
    "DECLARED_MATTER_ATTEMPTS_WORKFLOW": "The declared matter attempts workflow.",
    "DECLARED_MATTER_ATTEMPTS_ROUTING": "The declared matter attempts routing.",
    "DECLARED_MATTER_ATTEMPTS_ROADMAP": "The declared matter attempts roadmap.",
    "DECLARED_MATTER_ATTEMPTS_GENERAL_CONTINUATION": (
        "The declared matter attempts general continuation."
    ),
    "DECLARED_MATTER_ATTEMPTS_BODY_RELEVANCE_MEDIUM": (
        "The declared matter attempts body relevance medium implementation."
    ),
    "ACCEPTANCE_ATTEMPTS_SCOPE": "Acceptance attempts to assign scope.",
    "ACCEPTANCE_ATTEMPTS_PRESENCE": "Acceptance attempts to establish presence.",
    "ACCEPTANCE_ATTEMPTS_THRESHOLD": "Acceptance attempts to meet threshold.",
    "ACCEPTANCE_ATTEMPTS_TRUTH": "Acceptance attempts to create truth.",
    "ACCEPTANCE_ATTEMPTS_ACTION_AUTHORIZATION": (
        "Acceptance attempts to authorize action."
    ),
    "ACCEPTANCE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION": (
        "Acceptance attempts to authorize follow-on work."
    ),
    "ACCEPTANCE_ATTEMPTS_SIGNAL_ROUTER": (
        "Acceptance attempts to create signal routing."
    ),
    "ACCEPTANCE_ATTEMPTS_EVENT_BUS": "Acceptance attempts to create an event bus.",
    "ACCEPTANCE_ATTEMPTS_BODY_RELEVANCE_MEDIUM": (
        "Acceptance attempts to create a body relevance medium."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required non-claim is missing or flipped.",
    "LATEST_FILE_RECENCY_REFUSED": "Latest-file recency is refused.",
    "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE": (
        "Derivative, operator, or re-entry source distinction collapsed."
    ),
    "ACCEPTED_SIGNAL_BECAME_PERMISSION": (
        "The accepted signal was treated as permission."
    ),
    "ACCEPTED_SIGNAL_BECAME_ACTION": "The accepted signal was treated as action.",
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    candidate = Path(path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.resolve(strict=False).relative_to(
            _repo_root().resolve(strict=False)
        ).as_posix()
    except ValueError:
        return candidate.as_posix()


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def _string_or_none(value: Any) -> str | None:
    if value is None:
        return None
    if isinstance(value, str):
        text = value.strip()
        return text if text else None
    return str(value)


def _safe_filename_part(value: Any) -> str:
    text = _string_or_none(value) or "default"
    text = re.sub(r"[^A-Za-z0-9._-]+", "_", text).strip("._")
    return (text or "default")[:180]


def _normal_text(value: Any) -> str:
    text = _string_or_none(value) or ""
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def _loose_equal(left: Any, right: Any) -> bool:
    if left is None or right is None:
        return False
    return _normal_text(left) == _normal_text(right)


def _loose_family_equal(left: Any, right: Any) -> bool:
    left_text = _normal_text(left)
    right_text = _normal_text(right)
    if not left_text or not right_text:
        return False
    return (
        left_text == right_text
        or left_text.endswith(right_text)
        or right_text.endswith(left_text)
        or left_text in right_text
        or right_text in left_text
    )


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    if Path(left_text).as_posix() == Path(right_text).as_posix():
        return True
    return _display_path(_repo_path(left_text)) == _display_path(_repo_path(right_text))


def _text_blob(*values: Any, deep: bool = True) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, Mapping):
            parts.extend(str(key) for key in value.keys())
            if deep:
                parts.extend(_text_blob(nested, deep=True) for nested in value.values())
        elif isinstance(value, list):
            if deep:
                parts.extend(_text_blob(item, deep=True) for item in value)
        elif value is not None:
            parts.append(str(value))
    return " ".join(part for part in parts if part).lower()


def _value_text_blob(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, Mapping):
            parts.extend(_value_text_blob(nested) for nested in value.values())
        elif isinstance(value, list):
            parts.extend(_value_text_blob(item) for item in value)
        elif value is not None:
            parts.append(str(value))
    return " ".join(part for part in parts if part).lower()


def _section(mapping: Mapping[str, Any] | None, name: str) -> Mapping[str, Any]:
    value = mapping.get(name) if isinstance(mapping, Mapping) else None
    return value if isinstance(value, Mapping) else {}


def _first_mapping(result: Mapping[str, Any], names: Sequence[str]) -> Mapping[str, Any]:
    for name in names:
        value = result.get(name)
        if isinstance(value, Mapping):
            return value
    return {}


def _first_from_mappings(
    mappings: Sequence[Mapping[str, Any]],
    keys: Sequence[str],
) -> Any:
    for mapping in mappings:
        for key in keys:
            value = mapping.get(key)
            if _string_or_none(value) is not None:
                return value
    return None


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    return f"{reason} {detail}" if detail else reason


def _read_json_file(path: Path | str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except OSError as exc:
        raise BodySignalAcceptanceError(
            f"signal-recognition result is unreadable: {resolved}",
            "SIGNAL_RECOGNITION_RESULT_UNREADABLE",
        ) from exc
    except json.JSONDecodeError as exc:
        raise BodySignalAcceptanceError(
            f"signal-recognition result is malformed JSON: {resolved}",
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        ) from exc
    if not isinstance(value, dict):
        raise BodySignalAcceptanceError(
            f"signal-recognition result JSON must be an object: {resolved}",
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        )
    return value


def _request_mapping(value: Any) -> dict[str, Any]:
    return _clone(dict(value)) if isinstance(value, Mapping) else {}


def _metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    explicit = _first_mapping(
        result,
        (
            "body_signal_recognition_v2_metadata",
            "body_signal_recognition_metadata",
            "body_signal_acceptance_metadata",
        ),
    )
    if explicit:
        return explicit
    for key, value in result.items():
        if isinstance(value, Mapping) and "metadata" in str(key):
            return value
    return {}


def _selected_source(result: Mapping[str, Any]) -> Mapping[str, Any]:
    selected = result.get("selected_source_artifact")
    if isinstance(selected, Mapping):
        return selected
    basis = result.get("body_signal_recognition_basis")
    if isinstance(basis, Mapping):
        source = basis.get("selected_source_artifact")
        if isinstance(source, Mapping):
            return source
    return {}


def _recognized_signal(result: Mapping[str, Any]) -> Mapping[str, Any]:
    value = result.get("recognized_signal")
    return value if isinstance(value, Mapping) else {}


def _recognition_basis_from_request(
    acceptance_request: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    return _section(acceptance_request, "recognized_signal_basis")


def _recognition_identity(
    result: Mapping[str, Any] | None,
    *,
    result_path_hint: Path | str | None = None,
    acceptance_request: Mapping[str, Any] | None = None,
    selection_mode: str = "provided_signal_recognition_mapping",
) -> dict[str, Any]:
    request_basis = _recognition_basis_from_request(acceptance_request)
    if not isinstance(result, Mapping):
        return {
            "signal_recognition_result_id": request_basis.get(
                "signal_recognition_result_id"
            ),
            "signal_recognition_result_path": _display_path(result_path_hint)
            or request_basis.get("signal_recognition_result_path"),
            "signal_recognition_result_version": request_basis.get(
                "signal_recognition_result_version"
            ),
            "signal_recognition_outcome": request_basis.get(
                "signal_recognition_outcome"
            ),
            "signal_recognition_resolver_module": request_basis.get(
                "signal_recognition_resolver_module"
            ),
            "signal_recognition_result_type": None,
            "selection_mode": selection_mode,
            "_result_id_exposed": False,
            "_result_path_exposed": result_path_hint is not None,
            "_result_version_exposed": False,
            "_result_module_exposed": False,
        }

    metadata = _metadata(result)
    result_id = _first_from_mappings(
        (metadata, result),
        (
            "body_signal_recognition_result_id",
            "result_id",
            "signal_recognition_result_id",
        ),
    )
    result_version = _first_from_mappings(
        (metadata, result),
        (
            "body_signal_recognition_result_version",
            "result_version",
            "signal_recognition_result_version",
        ),
    )
    resolver_module = _first_from_mappings(
        (metadata, result),
        ("resolver_module", "signal_recognition_resolver_module"),
    )
    result_type = _first_from_mappings(
        (metadata, result),
        ("body_signal_recognition_result_type", "result_type"),
    )
    result_path = (
        _display_path(result_path_hint)
        or _first_from_mappings(
            (result,),
            (
                "signal_recognition_result_path",
                "result_path",
                "artifact_path",
                "path",
            ),
        )
        or request_basis.get("signal_recognition_result_path")
    )

    return {
        "signal_recognition_result_id": _string_or_none(
            result_id or request_basis.get("signal_recognition_result_id")
        ),
        "signal_recognition_result_path": _string_or_none(result_path),
        "signal_recognition_result_version": _string_or_none(
            result_version or request_basis.get("signal_recognition_result_version")
        ),
        "signal_recognition_outcome": _string_or_none(
            result.get("outcome") or request_basis.get("signal_recognition_outcome")
        ),
        "signal_recognition_resolver_module": _string_or_none(
            resolver_module or request_basis.get("signal_recognition_resolver_module")
        ),
        "signal_recognition_result_type": _string_or_none(result_type),
        "selection_mode": selection_mode,
        "_result_id_exposed": result_id is not None,
        "_result_path_exposed": result_path_hint is not None
        or _first_from_mappings((result,), ("result_path", "artifact_path", "path"))
        is not None,
        "_result_version_exposed": result_version is not None,
        "_result_module_exposed": resolver_module is not None,
    }


def _selected_recognized_signal(result: Mapping[str, Any] | None) -> dict[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    recognized = _recognized_signal(result)
    return _clone(dict(recognized)) if recognized else {}


def _recognized_signal_identity(
    result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    recognized = _recognized_signal(result) if isinstance(result, Mapping) else {}
    selected_source = _selected_source(result) if isinstance(result, Mapping) else {}
    return {
        "recognized_signal_id": _string_or_none(
            recognized.get("recognized_signal_id")
        ),
        "recognized_signal_category": _string_or_none(
            recognized.get("signal_category")
        ),
        "recognized_source_artifact_id": _string_or_none(
            recognized.get("source_artifact_id")
            or selected_source.get("source_artifact_id")
        ),
        "recognized_source_artifact_path": _string_or_none(
            recognized.get("source_artifact_path")
            or selected_source.get("source_artifact_path")
        ),
        "recognized_source_artifact_family": _string_or_none(
            recognized.get("source_artifact_family")
            or selected_source.get("source_artifact_family")
        ),
        "recognized_source_artifact_outcome": _string_or_none(
            recognized.get("source_artifact_outcome")
            or selected_source.get("source_artifact_outcome")
        ),
        "non_authoritative": recognized.get("non_authoritative"),
        "non_permission": recognized.get("non_permission"),
        "non_currentness": recognized.get("non_currentness"),
    }


def _public_recognition_identity(identity: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in identity.items()
        if not str(key).startswith("_")
    }


def _request_id(acceptance_request: Mapping[str, Any] | None) -> str | None:
    return _string_or_none(
        _section(acceptance_request, "signal_acceptance_request_metadata").get(
            "signal_acceptance_request_id"
        )
    )


def _request_shape_errors(acceptance_request: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    for section_name in REQUEST_SECTIONS:
        if not isinstance(acceptance_request.get(section_name), Mapping):
            errors.append(f"{section_name} must be an object")

    metadata = acceptance_request.get("signal_acceptance_request_metadata")
    if isinstance(metadata, Mapping):
        for field in REQUEST_METADATA_FIELDS:
            if _string_or_none(metadata.get(field)) is None:
                errors.append(f"signal_acceptance_request_metadata.{field} is required")

    basis = acceptance_request.get("recognized_signal_basis")
    if isinstance(basis, Mapping):
        for field in RECOGNIZED_SIGNAL_BASIS_FIELDS:
            if _string_or_none(basis.get(field)) is None:
                errors.append(f"recognized_signal_basis.{field} is required")

    matter = acceptance_request.get("declared_matter")
    if isinstance(matter, Mapping):
        for field in DECLARED_MATTER_FIELDS:
            if _string_or_none(matter.get(field)) is None:
                errors.append(f"declared_matter.{field} is required")

    return errors


def _first_bad_false_field(fields: Sequence[str], mapping: Mapping[str, Any]) -> str | None:
    for field in fields:
        if mapping.get(field) is not False:
            return field
    return None


def _first_bad_true_field(fields: Sequence[str], mapping: Mapping[str, Any]) -> str | None:
    for field in fields:
        if mapping.get(field) is not True:
            return field
    return None


def _matter_text(acceptance_request: Mapping[str, Any]) -> str:
    matter = _section(acceptance_request, "declared_matter")
    return _value_text_blob(
        matter.get("matter_id"),
        matter.get("matter_family"),
        matter.get("matter_kind"),
        matter.get("matter_purpose"),
        matter.get("matter_boundary"),
    )


def _matter_values(acceptance_request: Mapping[str, Any]) -> tuple[str, ...]:
    matter = _section(acceptance_request, "declared_matter")
    values: list[str] = []
    for key in DECLARED_MATTER_FIELDS:
        text = _string_or_none(matter.get(key))
        if text is not None:
            values.append(text.lower().strip())
    return tuple(values)


def _request_text(acceptance_request: Mapping[str, Any]) -> str:
    return _value_text_blob(acceptance_request)


def _contains_any(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _matter_attempt_block(acceptance_request: Mapping[str, Any]) -> tuple[bool, str | None, Any]:
    text = _matter_text(acceptance_request)
    values = _matter_values(acceptance_request)
    exact_attempts = {
        "action": "DECLARED_MATTER_ATTEMPTS_ACTION",
        "route": "DECLARED_MATTER_ATTEMPTS_ROUTING",
        "routing": "DECLARED_MATTER_ATTEMPTS_ROUTING",
        "workflow": "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
        "roadmap": "DECLARED_MATTER_ATTEMPTS_ROADMAP",
        "general continuation": "DECLARED_MATTER_ATTEMPTS_GENERAL_CONTINUATION",
        "body relevance medium": "DECLARED_MATTER_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
        "signal use": "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
        "scope": "ACCEPTANCE_ATTEMPTS_SCOPE",
        "presence": "ACCEPTANCE_ATTEMPTS_PRESENCE",
        "threshold": "ACCEPTANCE_ATTEMPTS_THRESHOLD",
        "truth": "ACCEPTANCE_ATTEMPTS_TRUTH",
    }
    for value in values:
        if value in exact_attempts:
            return False, exact_attempts[value], value

    checks = (
        (
            "DECLARED_MATTER_ATTEMPTS_ACTION",
            (
                "authorize action",
                "action authorization",
                "action trigger",
                "take action",
                "act on signal",
                "create action",
            ),
        ),
        (
            "DECLARED_MATTER_ATTEMPTS_WORKFLOW",
            (
                "create workflow",
                "become workflow",
                "workflow loop",
                "workflow state",
                "workflow engine",
                "workflow machinery",
                "use as workflow",
            ),
        ),
        (
            "DECLARED_MATTER_ATTEMPTS_ROUTING",
            (
                "route signal",
                "create routing",
                "routing created",
                "signal routing created",
                "signal router",
                "create route",
            ),
        ),
        (
            "DECLARED_MATTER_ATTEMPTS_ROADMAP",
            (
                "create roadmap",
                "generate roadmap",
                "roadmap generation",
                "roadmap created",
                "plan next",
                "future plan",
            ),
        ),
        (
            "DECLARED_MATTER_ATTEMPTS_GENERAL_CONTINUATION",
            (
                "create general continuation",
                "general continuation permission",
                "continue work",
                "follow-on work authorized",
                "authorize follow-on",
                "next step generator",
            ),
        ),
        (
            "DECLARED_MATTER_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
            (
                "create body relevance medium",
                "body relevance medium implementation",
                "body relevance medium created",
            ),
        ),
        (
            "ACCEPTANCE_ATTEMPTS_SCOPE",
            ("assign scope", "create scope", "scope the signal"),
        ),
        (
            "ACCEPTANCE_ATTEMPTS_PRESENCE",
            ("establish presence", "create presence"),
        ),
        (
            "ACCEPTANCE_ATTEMPTS_THRESHOLD",
            ("meet threshold", "threshold met"),
        ),
        (
            "ACCEPTANCE_ATTEMPTS_TRUTH",
            ("create truth", "make true", "truth created"),
        ),
    )
    for block_code, phrases in checks:
        if _contains_any(text, phrases):
            return False, block_code, text
    if "use signal" in text or "signal use" in text:
        return False, "DECLARED_MATTER_VAGUE_OR_UNBOUNDED", text
    return True, None, "declared matter stays bounded"


def _matter_purpose_bounded(acceptance_request: Mapping[str, Any]) -> bool:
    text = _matter_text(acceptance_request)
    required_markers = (
        "current_signal_recognition_standing",
        "current signal recognition",
        "signal-recognition",
        "recognized body-signal",
        "recognized body signal",
        "recognized signal",
        "structured handling",
    )
    return any(marker in text for marker in required_markers)


def _latest_file_recency_attempted(acceptance_request: Mapping[str, Any]) -> bool:
    text = _request_text(acceptance_request)
    return _contains_any(
        text,
        ("latest file", "latest-file", "latest_file", "newest file", "recency"),
    )


def _collapse_attempted(acceptance_request: Mapping[str, Any]) -> bool:
    text = _request_text(acceptance_request)
    return _contains_any(
        text,
        (
            "derivative as source",
            "operator as source",
            "reentry as governing",
            "re-entry as governing",
            "governing basis from derivative",
            "current basis from derivative",
            "receipt as permission",
            "receipt into permission",
        ),
    )


def _recognized_signal_permission_attempted(
    acceptance_request: Mapping[str, Any],
) -> bool:
    text = _request_text(acceptance_request)
    return _contains_any(
        text,
        (
            "accepted signal creates permission",
            "accepted signal is permission",
            "signal means permission",
            "permission token",
            "general permission",
        ),
    )


def _recognized_signal_action_attempted(acceptance_request: Mapping[str, Any]) -> bool:
    text = _request_text(acceptance_request)
    return _contains_any(
        text,
        (
            "accepted signal authorizes action",
            "signal authorizes action",
            "action trigger",
            "trigger action",
        ),
    )


def _basis_matches_recognition(
    request_basis: Mapping[str, Any],
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    *,
    path_required: bool,
) -> tuple[bool, str | None, Any]:
    recognition_outcome = request_basis.get("signal_recognition_outcome")
    if not _loose_equal(recognition_outcome, OUTCOME_SIGNAL_RECOGNIZED):
        return False, "SIGNAL_RECOGNITION_RESULT_NOT_RECOGNIZED", recognition_outcome

    expected_result_id = recognition_identity.get("signal_recognition_result_id")
    actual_result_id = request_basis.get("signal_recognition_result_id")
    if expected_result_id and actual_result_id and not _loose_equal(actual_result_id, expected_result_id):
        return False, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_result_id,
            "actual": actual_result_id,
        }

    expected_path = recognition_identity.get("signal_recognition_result_path")
    actual_path = request_basis.get("signal_recognition_result_path")
    if expected_path and (path_required or actual_path is not None) and not _path_equal(actual_path, expected_path):
        return False, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_path,
            "actual": actual_path,
        }

    expected_version = recognition_identity.get("signal_recognition_result_version")
    actual_version = request_basis.get("signal_recognition_result_version")
    if expected_version and actual_version and not _loose_equal(actual_version, expected_version):
        return False, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_version,
            "actual": actual_version,
        }

    expected_module = recognition_identity.get("signal_recognition_resolver_module")
    actual_module = request_basis.get("signal_recognition_resolver_module")
    if expected_module and actual_module and not _loose_equal(actual_module, expected_module):
        return False, "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_module,
            "actual": actual_module,
        }

    expected_category = recognized_identity.get("recognized_signal_category")
    actual_category = request_basis.get("recognized_signal_category")
    if expected_category and not _loose_equal(actual_category, expected_category):
        return False, "SIGNAL_CATEGORY_MISMATCH", {
            "expected": expected_category,
            "actual": actual_category,
        }

    source_pairs = (
        ("recognized_source_artifact_id", _loose_equal),
        ("recognized_source_artifact_path", _path_equal),
        ("recognized_source_artifact_family", _loose_family_equal),
        ("recognized_source_artifact_outcome", _loose_equal),
    )
    for key, comparator in source_pairs:
        expected = recognized_identity.get(key)
        actual = request_basis.get(key)
        if expected and not comparator(actual, expected):
            return False, "RECOGNIZED_SOURCE_IDENTITY_MISMATCH", {
                "field": key,
                "expected": expected,
                "actual": actual,
            }
    return True, None, "recognized signal basis preserved"


def _build_checks(
    recognition_result: Mapping[str, Any] | None,
    acceptance_request: Mapping[str, Any] | None,
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    *,
    path_based: bool,
    recognition_readable: bool,
    recognition_malformed: bool,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    recognition_exists = isinstance(recognition_result, Mapping)
    request_exists = isinstance(acceptance_request, Mapping)
    request_errors = (
        _request_shape_errors(acceptance_request)
        if isinstance(acceptance_request, Mapping)
        else []
    )
    request_well_formed = request_exists and not request_errors
    request_basis = _section(acceptance_request, "recognized_signal_basis")
    declared_matter = _section(acceptance_request, "declared_matter")
    acceptance_scope = _section(acceptance_request, "declared_acceptance_scope")
    hierarchy = _section(acceptance_request, "hierarchy_constraints")
    correspondence = _section(acceptance_request, "correspondence_requirements")
    declared_non_claims = _section(acceptance_request, "declared_non_claims")

    checks.append(
        _check(
            "signal_recognition_result_exists",
            recognition_exists,
            "one SIGNAL_RECOGNIZED result mapping",
            "present" if recognition_exists else "missing",
            "SIGNAL_RECOGNITION_RESULT_MISSING",
        )
    )
    checks.append(
        _check(
            "signal_recognition_result_is_readable_if_path_based",
            recognition_exists and recognition_readable and not recognition_malformed,
            "readable signal-recognition JSON object for explicit path, provided object otherwise",
            "readable"
            if recognition_exists and recognition_readable and not recognition_malformed
            else "unreadable or malformed",
            "SIGNAL_RECOGNITION_RESULT_UNREADABLE"
            if not recognition_malformed
            else "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        )
    )
    checks.append(
        _check(
            "signal_recognition_result_is_well_formed_enough",
            recognition_exists and isinstance(recognition_result, Mapping),
            "signal-recognition result is an object",
            type(recognition_result).__name__ if recognition_result is not None else "missing",
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        )
    )
    checks.append(
        _check(
            "signal_recognition_result_outcome_is_signal_recognized",
            _loose_equal(
                recognition_identity.get("signal_recognition_outcome"),
                OUTCOME_SIGNAL_RECOGNIZED,
            ),
            "SIGNAL_RECOGNIZED",
            recognition_identity.get("signal_recognition_outcome"),
            "SIGNAL_RECOGNITION_RESULT_NOT_RECOGNIZED",
        )
    )
    checks.append(
        _check(
            "recognized_signal_is_present",
            bool(recognized_identity.get("recognized_signal_id"))
            and bool(recognized_identity.get("recognized_signal_category")),
            "recognized signal id and category present",
            {
                "recognized_signal_id": recognized_identity.get("recognized_signal_id"),
                "recognized_signal_category": recognized_identity.get(
                    "recognized_signal_category"
                ),
            },
            "RECOGNIZED_SIGNAL_MISSING",
        )
    )
    checks.append(
        _check(
            "recognized_signal_identity_is_preserved",
            bool(recognized_identity.get("recognized_signal_id")),
            "recognized signal identity present",
            recognized_identity.get("recognized_signal_id"),
            "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH",
        )
    )
    source_identity_present = all(
        _string_or_none(recognized_identity.get(key)) is not None
        for key in (
            "recognized_source_artifact_id",
            "recognized_source_artifact_path",
            "recognized_source_artifact_family",
            "recognized_source_artifact_outcome",
        )
    )
    checks.append(
        _check(
            "recognized_source_artifact_identity_is_preserved",
            source_identity_present,
            "recognized source id/path/family/outcome present",
            {
                key: recognized_identity.get(key)
                for key in (
                    "recognized_source_artifact_id",
                    "recognized_source_artifact_path",
                    "recognized_source_artifact_family",
                    "recognized_source_artifact_outcome",
                )
            },
            "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
        )
    )
    checks.append(
        _check(
            "recognized_signal_category_is_preserved",
            _string_or_none(recognized_identity.get("recognized_signal_category")) is not None,
            "recognized signal category present",
            recognized_identity.get("recognized_signal_category"),
            "SIGNAL_CATEGORY_MISMATCH",
        )
    )
    checks.append(
        _check(
            "recognized_signal_remains_non_authoritative",
            recognized_identity.get("non_authoritative") is True,
            "recognized signal non_authoritative is true",
            recognized_identity.get("non_authoritative"),
            "RECOGNIZED_SIGNAL_TREATED_AS_AUTHORITY",
        )
    )
    checks.append(
        _check(
            "recognized_signal_remains_non_permission",
            recognized_identity.get("non_permission") is True,
            "recognized signal non_permission is true",
            recognized_identity.get("non_permission"),
            "RECOGNIZED_SIGNAL_TREATED_AS_PERMISSION",
        )
    )
    checks.append(
        _check(
            "recognized_signal_remains_non_currentness",
            recognized_identity.get("non_currentness") is True,
            "recognized signal non_currentness is true",
            recognized_identity.get("non_currentness"),
            "RECOGNIZED_SIGNAL_TREATED_AS_CURRENTNESS",
        )
    )

    checks.append(
        _check(
            "signal_acceptance_request_exists",
            request_exists,
            "one signal-acceptance request mapping",
            "present" if request_exists else "missing",
            "SIGNAL_ACCEPTANCE_REQUEST_MISSING",
        )
    )
    matter_present = isinstance(
        acceptance_request.get("declared_matter") if request_exists else None,
        Mapping,
    )
    checks.append(
        _check(
            "declared_matter_is_present",
            matter_present,
            "declared_matter object present",
            "present" if matter_present else "missing",
            "DECLARED_MATTER_MISSING",
        )
    )
    checks.append(
        _check(
            "signal_acceptance_request_is_well_formed_enough",
            request_well_formed,
            "required acceptance request sections and core fields present",
            request_errors or "well formed enough",
            "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
        )
    )

    basis_matches, basis_block, basis_actual = (
        _basis_matches_recognition(
            request_basis,
            recognition_identity,
            recognized_identity,
            path_required=path_based,
        )
        if request_exists
        else (False, "SIGNAL_ACCEPTANCE_REQUEST_MISSING", "request missing")
    )
    checks.append(
        _check(
            "recognized_signal_basis_matches_selected_recognition_result",
            basis_matches,
            "request basis matches selected recognition result and recognized source",
            basis_actual,
            basis_block or "RECOGNIZED_SIGNAL_IDENTITY_MISMATCH",
        )
    )

    checks.append(
        _check(
            "declared_matter_is_supported",
            _loose_equal(declared_matter.get("matter_family"), SUPPORTED_MATTER_FAMILY)
            and _loose_equal(declared_matter.get("matter_kind"), SUPPORTED_MATTER_KIND),
            {
                "matter_family": SUPPORTED_MATTER_FAMILY,
                "matter_kind": SUPPORTED_MATTER_KIND,
            },
            {
                "matter_family": declared_matter.get("matter_family"),
                "matter_kind": declared_matter.get("matter_kind"),
            },
            "DECLARED_MATTER_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "declared_matter_is_current_signal_recognition_standing",
            _loose_equal(declared_matter.get("matter_id"), SUPPORTED_MATTER_ID),
            SUPPORTED_MATTER_ID,
            declared_matter.get("matter_id"),
            "DECLARED_MATTER_UNSUPPORTED",
        )
    )
    matter_attempt_passed, matter_attempt_block, matter_attempt_actual = (
        _matter_attempt_block(acceptance_request)
        if request_exists
        else (False, "SIGNAL_ACCEPTANCE_REQUEST_MISSING", "request missing")
    )
    checks.append(
        _check(
            "declared_matter_purpose_is_bounded_to_current_signal_recognition_posture",
            matter_attempt_passed and _matter_purpose_bounded(acceptance_request or {}),
            "bounded current signal-recognition standing posture",
            matter_attempt_actual
            if matter_attempt_passed
            else {"blocked_matter_text": matter_attempt_actual},
            matter_attempt_block or "DECLARED_MATTER_VAGUE_OR_UNBOUNDED",
        )
    )

    bad_scope_field = _first_bad_true_field(ACCEPTANCE_SCOPE_TRUE_FIELDS, acceptance_scope)
    checks.append(
        _check(
            "acceptance_scope_is_structured_handling_only",
            bad_scope_field is None,
            "all acceptance-scope fields present and true",
            "all true"
            if bad_scope_field is None
            else {bad_scope_field: acceptance_scope.get(bad_scope_field)},
            SCOPE_FIELD_BLOCK_CODES.get(
                bad_scope_field or "",
                "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
            ),
        )
    )
    for field in ACCEPTANCE_SCOPE_TRUE_FIELDS[1:]:
        checks.append(
            _check(
                f"{field}",
                acceptance_scope.get(field) is True,
                f"{field} is true",
                acceptance_scope.get(field),
                SCOPE_FIELD_BLOCK_CODES[field],
            )
        )

    bad_hierarchy_field = _first_bad_false_field(HIERARCHY_FALSE_FIELDS, hierarchy)
    checks.append(
        _check(
            "hierarchy_constraints_are_preserved",
            bad_hierarchy_field is None,
            "all hierarchy constraint fields present and false",
            "all false"
            if bad_hierarchy_field is None
            else {bad_hierarchy_field: hierarchy.get(bad_hierarchy_field)},
            HIERARCHY_FIELD_BLOCK_CODES.get(
                bad_hierarchy_field or "",
                "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
            ),
        )
    )

    bad_correspondence_field = _first_bad_true_field(
        CORRESPONDENCE_TRUE_FIELDS,
        correspondence,
    )
    checks.append(
        _check(
            "correspondence_requirements_are_preserved",
            bad_correspondence_field is None,
            "all correspondence requirement fields present and true",
            "all true"
            if bad_correspondence_field is None
            else {bad_correspondence_field: correspondence.get(bad_correspondence_field)},
            CORRESPONDENCE_FIELD_BLOCK_CODES.get(
                bad_correspondence_field or "",
                "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
            ),
        )
    )

    bad_non_claim_field = _first_bad_true_field(
        DECLARED_NON_CLAIM_FIELDS,
        declared_non_claims,
    )
    checks.append(
        _check(
            "declared_non_claims_are_preserved",
            bad_non_claim_field is None,
            "all declared non-claim fields present and true",
            "all true"
            if bad_non_claim_field is None
            else {bad_non_claim_field: declared_non_claims.get(bad_non_claim_field)},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    checks.extend(
        _anti_collapse_checks(
            acceptance_request or {},
            hierarchy,
            declared_non_claims,
        )
    )
    return checks


def _anti_collapse_checks(
    acceptance_request: Mapping[str, Any],
    hierarchy: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    latest_recency = (
        hierarchy.get("latest_file_recency_allowed") is not False
        or _latest_file_recency_attempted(acceptance_request)
    )
    collapse = (
        hierarchy.get("derivative_signal_allowed_as_source") is not False
        or hierarchy.get("operator_signal_allowed_as_source") is not False
        or hierarchy.get("reentry_signal_allowed_as_governing_basis") is not False
        or _collapse_attempted(acceptance_request)
    )
    permission_attempt = (
        hierarchy.get("accepted_signal_allowed_as_permission") is not False
        or declared_non_claims.get("does_not_create_permission") is not True
        or _recognized_signal_permission_attempted(acceptance_request)
    )
    action_attempt = (
        hierarchy.get("accepted_signal_allowed_as_action_trigger") is not False
        or declared_non_claims.get("does_not_authorize_action") is not True
        or _recognized_signal_action_attempted(acceptance_request)
    )
    return [
        _check(
            "latest_file_recency_is_refused",
            not latest_recency,
            "acceptance does not infer currentness by latest-file recency",
            {
                "latest_file_recency_allowed": hierarchy.get(
                    "latest_file_recency_allowed"
                ),
                "latest_file_recency_language_detected": _latest_file_recency_attempted(
                    acceptance_request
                ),
            },
            "LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "derivative_api_operator_reentry_surfaces_do_not_become_governing_current_basis",
            not collapse,
            "downstream surfaces remain downstream and non-governing",
            {
                "derivative_signal_allowed_as_source": hierarchy.get(
                    "derivative_signal_allowed_as_source"
                ),
                "operator_signal_allowed_as_source": hierarchy.get(
                    "operator_signal_allowed_as_source"
                ),
                "reentry_signal_allowed_as_governing_basis": hierarchy.get(
                    "reentry_signal_allowed_as_governing_basis"
                ),
                "collapse_language_detected": _collapse_attempted(acceptance_request),
            },
            "DERIVATIVE_OPERATOR_REENTRY_SOURCE_COLLAPSE",
        ),
        _check(
            "accepted_signal_does_not_become_permission",
            not permission_attempt,
            "accepted signal remains non-permission",
            {
                "accepted_signal_allowed_as_permission": hierarchy.get(
                    "accepted_signal_allowed_as_permission"
                ),
                "does_not_create_permission": declared_non_claims.get(
                    "does_not_create_permission"
                ),
                "permission_language_detected": _recognized_signal_permission_attempted(
                    acceptance_request
                ),
            },
            "ACCEPTED_SIGNAL_BECAME_PERMISSION",
        ),
        _check(
            "accepted_signal_does_not_become_action",
            not action_attempt,
            "accepted signal remains non-action",
            {
                "accepted_signal_allowed_as_action_trigger": hierarchy.get(
                    "accepted_signal_allowed_as_action_trigger"
                ),
                "does_not_authorize_action": declared_non_claims.get(
                    "does_not_authorize_action"
                ),
                "action_language_detected": _recognized_signal_action_attempted(
                    acceptance_request
                ),
            },
            "ACCEPTED_SIGNAL_BECAME_ACTION",
        ),
        _check(
            "body_relevance_medium_is_not_created",
            hierarchy.get("accepted_signal_allowed_as_body_relevance_medium") is False
            and declared_non_claims.get("does_not_create_body_relevance_medium") is True,
            "acceptance does not create a body relevance medium",
            {
                "accepted_signal_allowed_as_body_relevance_medium": hierarchy.get(
                    "accepted_signal_allowed_as_body_relevance_medium"
                ),
                "does_not_create_body_relevance_medium": declared_non_claims.get(
                    "does_not_create_body_relevance_medium"
                ),
            },
            "ACCEPTANCE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
        ),
    ]


def _result_id(
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    acceptance_request: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    request_id = _request_id(acceptance_request or {}) or "signal_acceptance_request"
    signal_id = recognized_identity.get("recognized_signal_id") or recognition_identity.get(
        "signal_recognition_result_id"
    )
    signal_id = signal_id or "recognized_signal"
    return (
        f"{_safe_filename_part(request_id)}__"
        f"{_safe_filename_part(signal_id)}__"
        f"body_signal_acceptance_{outcome.lower()}"
    )


def _result_metadata(
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    acceptance_request: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "body_signal_acceptance_result_id": _result_id(
            recognition_identity,
            recognized_identity,
            acceptance_request,
            outcome,
        ),
        "body_signal_acceptance_result_type": BODY_SIGNAL_ACCEPTANCE_RESULT_TYPE,
        "body_signal_acceptance_result_version": BODY_SIGNAL_ACCEPTANCE_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _accepted_signal(
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    accepted_request: Mapping[str, Any],
) -> dict[str, Any]:
    matter = _section(accepted_request, "declared_matter")
    request_id = _request_id(accepted_request) or "signal_acceptance_request"
    signal_id = recognized_identity.get("recognized_signal_id") or "recognized_signal"
    return {
        "accepted_signal_id": (
            f"{_safe_filename_part(request_id)}__"
            f"{_safe_filename_part(signal_id)}__accepted"
        ),
        "accepted_signal_category": recognized_identity.get("recognized_signal_category"),
        "selected_signal_recognition_result_id": recognition_identity.get(
            "signal_recognition_result_id"
        ),
        "selected_signal_recognition_result_path": recognition_identity.get(
            "signal_recognition_result_path"
        ),
        "selected_signal_recognition_outcome": recognition_identity.get(
            "signal_recognition_outcome"
        ),
        "recognized_source_artifact_id": recognized_identity.get(
            "recognized_source_artifact_id"
        ),
        "recognized_source_artifact_path": recognized_identity.get(
            "recognized_source_artifact_path"
        ),
        "recognized_source_artifact_family": recognized_identity.get(
            "recognized_source_artifact_family"
        ),
        "recognized_source_artifact_outcome": recognized_identity.get(
            "recognized_source_artifact_outcome"
        ),
        "declared_matter_id": matter.get("matter_id"),
        "declared_matter_family": matter.get("matter_family"),
        "declared_matter_kind": matter.get("matter_kind"),
        "declared_matter_purpose": matter.get("matter_purpose"),
        "non_authoritative": True,
        "non_permission": True,
        "non_currentness": True,
        "not_scoped_yet": True,
        "not_present_yet": True,
        "not_threshold_yet": True,
        "not_truth": True,
        "no_action": True,
        "no_routing": True,
        "no_workflow": True,
        "no_body_relevance_medium": True,
    }


def _acceptance_basis(
    recognition_identity: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    acceptance_request: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "acceptance_scope": "single_signal_recognition_result_single_acceptance_request",
        "selected_signal_recognition_result": _public_recognition_identity(
            recognition_identity
        ),
        "recognized_signal_id": recognized_identity.get("recognized_signal_id"),
        "recognized_signal_category": recognized_identity.get(
            "recognized_signal_category"
        ),
        "request_id": _request_id(acceptance_request or {}),
        "declared_matter_id": _section(acceptance_request, "declared_matter").get(
            "matter_id"
        )
        if isinstance(acceptance_request, Mapping)
        else None,
        "outcome": outcome,
        "acceptance_for_structured_handling_only": outcome == OUTCOME_SIGNAL_ACCEPTED,
        "acceptance_creates_authority": False,
        "acceptance_creates_permission": False,
        "acceptance_creates_currentness": False,
        "acceptance_creates_truth": False,
        "acceptance_assigns_scope": False,
        "acceptance_establishes_presence": False,
        "acceptance_meets_threshold": False,
        "acceptance_routes_signal": False,
        "acceptance_authorizes_action": False,
        "acceptance_authorizes_follow_on_work": False,
        "acceptance_creates_body_relevance_medium": False,
    }


def _build_result(
    *,
    recognition_identity: Mapping[str, Any],
    recognized_signal: Mapping[str, Any],
    recognized_identity: Mapping[str, Any],
    acceptance_request: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None = None,
) -> dict[str, Any]:
    request_copy = _request_mapping(acceptance_request)
    result: dict[str, Any] = {
        "body_signal_acceptance_metadata": _result_metadata(
            recognition_identity,
            recognized_identity,
            request_copy,
            outcome,
        ),
        "selected_signal_recognition_result": _public_recognition_identity(
            recognition_identity
        ),
        "selected_recognized_signal": _clone(dict(recognized_signal)),
        "selected_signal_acceptance_request": request_copy,
        "declared_matter": _clone(
            dict(_section(request_copy, "declared_matter"))
        ),
        "signal_acceptance_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "accepted_signal": (
            _accepted_signal(recognition_identity, recognized_identity, request_copy)
            if outcome == OUTCOME_SIGNAL_ACCEPTED
            else None
        ),
        "body_signal_acceptance_basis": _acceptance_basis(
            recognition_identity,
            recognized_identity,
            request_copy,
            outcome,
        ),
        "body_signal_acceptance_summary": {},
        "non_claims": dict(RESULT_NON_CLAIM_DEFAULTS),
    }
    result["body_signal_acceptance_summary"] = build_body_signal_acceptance_summary(
        result
    )
    return result


def _empty_recognition_identity(
    *,
    result_path_hint: Path | str | None = None,
    selection_mode: str = "no_signal_recognition_result",
) -> dict[str, Any]:
    return {
        "signal_recognition_result_id": None,
        "signal_recognition_result_path": _display_path(result_path_hint),
        "signal_recognition_result_version": None,
        "signal_recognition_outcome": None,
        "signal_recognition_resolver_module": None,
        "signal_recognition_result_type": None,
        "selection_mode": selection_mode,
        "_result_id_exposed": False,
        "_result_path_exposed": result_path_hint is not None,
        "_result_version_exposed": False,
        "_result_module_exposed": False,
    }


def _blocked_result(
    block_code: str,
    *,
    block_detail: str | None = None,
    recognition_identity: Mapping[str, Any] | None = None,
    recognized_signal: Mapping[str, Any] | None = None,
    recognized_identity: Mapping[str, Any] | None = None,
    acceptance_request: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    selected_recognition = recognition_identity or _empty_recognition_identity()
    selected_recognized_identity = recognized_identity or {}
    selected_checks = list(checks or [])
    if not selected_checks:
        selected_checks = [
            _check(
                "body_signal_acceptance_blocked",
                False,
                "bounded signal-recognition result and acceptance request",
                block_detail or block_code,
                block_code,
            )
        ]
    return _build_result(
        recognition_identity=selected_recognition,
        recognized_signal=recognized_signal or {},
        recognized_identity=selected_recognized_identity,
        acceptance_request=acceptance_request,
        checks=selected_checks,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
    )


def _resolve_internal(
    signal_recognition_result: Mapping[str, Any] | None,
    acceptance_request: Mapping[str, Any] | None,
    *,
    result_path_hint: Path | str | None = None,
    selection_mode: str = "provided_signal_recognition_mapping",
) -> dict[str, Any]:
    if signal_recognition_result is not None and not isinstance(
        signal_recognition_result,
        Mapping,
    ):
        recognition_identity = _empty_recognition_identity(
            result_path_hint=result_path_hint,
            selection_mode="malformed_signal_recognition_result",
        )
        return _blocked_result(
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
            block_detail="signal-recognition result input must be a mapping",
            recognition_identity=recognition_identity,
            acceptance_request=_request_mapping(acceptance_request),
        )

    if acceptance_request is not None and not isinstance(acceptance_request, Mapping):
        recognition_identity = _recognition_identity(
            signal_recognition_result,
            result_path_hint=result_path_hint,
            selection_mode=selection_mode,
        )
        recognized_signal = _selected_recognized_signal(signal_recognition_result)
        recognized_identity = _recognized_signal_identity(signal_recognition_result)
        return _blocked_result(
            "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
            block_detail="signal-acceptance request input must be a mapping",
            recognition_identity=recognition_identity,
            recognized_signal=recognized_signal,
            recognized_identity=recognized_identity,
            acceptance_request={},
        )

    recognition_identity = _recognition_identity(
        signal_recognition_result,
        result_path_hint=result_path_hint,
        acceptance_request=acceptance_request,
        selection_mode=selection_mode,
    )
    recognized_signal = _selected_recognized_signal(signal_recognition_result)
    recognized_identity = _recognized_signal_identity(signal_recognition_result)

    checks = _build_checks(
        signal_recognition_result,
        acceptance_request,
        recognition_identity,
        recognized_identity,
        path_based=result_path_hint is not None,
        recognition_readable=signal_recognition_result is not None,
        recognition_malformed=False,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _build_result(
            recognition_identity=recognition_identity,
            recognized_signal=recognized_signal,
            recognized_identity=recognized_identity,
            acceptance_request=_request_mapping(acceptance_request),
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code=str(failed.get("block_code")),
        )
    return _build_result(
        recognition_identity=recognition_identity,
        recognized_signal=recognized_signal,
        recognized_identity=recognized_identity,
        acceptance_request=_request_mapping(acceptance_request),
        checks=checks,
        outcome=OUTCOME_SIGNAL_ACCEPTED,
        block_code=None,
    )


def resolve_body_signal_acceptance(
    signal_recognition_result: Mapping[str, Any] | None = None,
    acceptance_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded body-signal acceptance decision."""

    try:
        return _resolve_internal(signal_recognition_result, acceptance_request)
    except BodySignalAcceptanceError as exc:
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            recognition_identity=exc.selected_recognition,
            acceptance_request=exc.selected_request or _request_mapping(acceptance_request),
            checks=exc.checks,
        )


def resolve_body_signal_acceptance_from_path(
    signal_recognition_result_path: Path | str,
    acceptance_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Resolve one body-signal acceptance decision from an explicit path."""

    recognition_identity = _empty_recognition_identity(
        result_path_hint=signal_recognition_result_path,
        selection_mode="explicit_signal_recognition_result_path",
    )
    try:
        signal_recognition_result = _read_json_file(signal_recognition_result_path)
        return _resolve_internal(
            signal_recognition_result,
            acceptance_request,
            result_path_hint=signal_recognition_result_path,
            selection_mode="explicit_signal_recognition_result_path",
        )
    except BodySignalAcceptanceError as exc:
        checks = exc.checks
        if checks is None:
            checks = [
                _check(
                    "signal_recognition_result_is_readable_if_path_based",
                    False,
                    "readable signal-recognition JSON object for explicit path",
                    _display_path(signal_recognition_result_path),
                    exc.block_code,
                )
            ]
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            recognition_identity=exc.selected_recognition or recognition_identity,
            acceptance_request=_request_mapping(acceptance_request),
            checks=checks,
        )


def _check_passed(checks: Sequence[Any], check_name: str) -> bool:
    return any(
        isinstance(check, Mapping)
        and check.get("check_name") == check_name
        and check.get("passed") is True
        for check in checks
    )


def build_body_signal_acceptance_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded summary for one body-signal acceptance result."""

    if not isinstance(result, Mapping):
        raise BodySignalAcceptanceError(
            "body-signal acceptance result must be a mapping",
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        )
    selected_recognition = result.get("selected_signal_recognition_result")
    selected_recognition = (
        selected_recognition if isinstance(selected_recognition, Mapping) else {}
    )
    accepted_signal = result.get("accepted_signal")
    accepted_signal = accepted_signal if isinstance(accepted_signal, Mapping) else {}
    matter = result.get("declared_matter")
    matter = matter if isinstance(matter, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    checks = result.get("signal_acceptance_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_signal_recognition_result_id": selected_recognition.get(
            "signal_recognition_result_id"
        ),
        "selected_signal_recognition_result_path": selected_recognition.get(
            "signal_recognition_result_path"
        ),
        "selected_signal_recognition_outcome": selected_recognition.get(
            "signal_recognition_outcome"
        ),
        "accepted_signal_id": accepted_signal.get("accepted_signal_id"),
        "accepted_signal_category": accepted_signal.get("accepted_signal_category"),
        "declared_matter_id": matter.get("matter_id"),
        "declared_matter_family": matter.get("matter_family"),
        "declared_matter_kind": matter.get("matter_kind"),
        "passed_check_count": sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is True
        ),
        "failed_check_count": sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        ),
        "recognition_basis_passed": _check_passed(
            checks,
            "recognized_signal_basis_matches_selected_recognition_result",
        ),
        "matter_boundary_passed": _check_passed(
            checks,
            "declared_matter_purpose_is_bounded_to_current_signal_recognition_posture",
        ),
        "acceptance_scope_passed": _check_passed(
            checks,
            "acceptance_scope_is_structured_handling_only",
        ),
        "hierarchy_constraints_passed": _check_passed(
            checks,
            "hierarchy_constraints_are_preserved",
        ),
        "correspondence_requirements_passed": _check_passed(
            checks,
            "correspondence_requirements_are_preserved",
        ),
        "non_claims_passed": _check_passed(
            checks,
            "declared_non_claims_are_preserved",
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "authority_created",
                "permission_created",
                "currentness_created",
                "truth_created",
                "scope_assigned",
                "presence_established",
                "threshold_met",
                "action_authorized",
                "follow_on_work_authorized",
                "workflow_created",
                "roadmap_created",
                "signal_router_created",
                "event_bus_created",
                "body_relevance_medium_created",
                "source_replaced",
                "derivative_upgraded_to_source",
                "receipt_turned_into_permission",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = BODY_SIGNAL_ACCEPTANCE_ROOT,
) -> Path:
    accepted = result.get("accepted_signal")
    accepted = accepted if isinstance(accepted, Mapping) else {}
    request = result.get("selected_signal_acceptance_request")
    request = request if isinstance(request, Mapping) else {}
    recognition = result.get("selected_signal_recognition_result")
    recognition = recognition if isinstance(recognition, Mapping) else {}
    stem = _safe_filename_part(
        accepted.get("accepted_signal_id")
        or _request_id(request)
        or recognition.get("signal_recognition_result_id")
    )
    resolved_root = _repo_path(root)
    path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not path.exists():
        return path
    for index in range(1, 1000):
        path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not path.exists():
            return path
    raise BodySignalAcceptanceError(
        "no bounded body-signal acceptance filename is available",
        "SIGNAL_ACCEPTANCE_REQUEST_MALFORMED",
    )


def write_body_signal_acceptance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive body-signal acceptance JSON artifact."""

    if not isinstance(result, Mapping):
        raise BodySignalAcceptanceError(
            "body-signal acceptance result must be a mapping",
            "SIGNAL_RECOGNITION_RESULT_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and output_path is not None:
        raise FileExistsError(f"body-signal acceptance result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
