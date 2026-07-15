"""Resolve one bounded body-signal scope request.

This module evaluates exactly one ``SIGNAL_ACCEPTED`` result and one
signal-scope request. It decides only whether that accepted signal receives a
bounded applicability scope inside its accepted matter.

Scope is containment of applicability. It is not presence, threshold, truth,
authority, permission, action, routing, workflow, signal use, body relevance
medium implementation, or body-wide signaling. This resolver does not discover
signals, route signals, replay the host, mutate upstream artifacts, aggregate
signals, schedule work, or create follow-on authorization.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class BodySignalScopeError(RuntimeError):
    """Raised for malformed inputs or impossible scope correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_acceptance: Mapping[str, Any] | None = None,
        selected_request: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_acceptance = (
            copy.deepcopy(dict(selected_acceptance))
            if isinstance(selected_acceptance, Mapping)
            else None
        )
        self.selected_request = (
            copy.deepcopy(dict(selected_request))
            if isinstance(selected_request, Mapping)
            else None
        )
        self.checks = [dict(check) for check in checks] if checks is not None else None


BODY_SIGNAL_SCOPE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_scope"
)

RESOLVER_MODULE = "resolve_body_signal_scope"
BODY_SIGNAL_SCOPE_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_BODY_SIGNAL_SCOPE_RESULT"
)
BODY_SIGNAL_SCOPE_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "body_signal_scope_result"

OUTCOME_SIGNAL_SCOPED = "SIGNAL_SCOPED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_SIGNAL_ACCEPTED = "SIGNAL_ACCEPTED"

SUPPORTED_SIGNAL_CATEGORY = "BODY_PASS_SIGNAL"
SUPPORTED_ACCEPTED_MATTER_ID = "current_signal_recognition_standing"
SUPPORTED_ACCEPTED_MATTER_FAMILY = "body_signal_acceptance_matter"
SUPPORTED_ACCEPTED_MATTER_KIND = "recognized_body_signal_posture"

SUPPORTED_SCOPE_ID = (
    "current_signal_recognition_standing__"
    "body_pass_signal_nonoperative_posture_scope"
)
SUPPORTED_SCOPE_FAMILY = "body_signal_scope"
SUPPORTED_SCOPE_KIND = "nonoperative_body_pass_signal_posture"

REQUEST_SECTIONS = (
    "signal_scope_request_metadata",
    "accepted_signal_basis",
    "declared_scope",
    "declared_scope_limits",
    "hierarchy_constraints",
    "correspondence_requirements",
    "declared_non_claims",
)

REQUEST_METADATA_FIELDS = (
    "signal_scope_request_id",
    "signal_scope_request_type",
    "signal_scope_request_version",
    "declared_at",
    "declared_by_surface",
)

ACCEPTED_SIGNAL_BASIS_FIELDS = (
    "signal_acceptance_result_path",
    "signal_acceptance_result_id",
    "signal_acceptance_result_version",
    "signal_acceptance_outcome",
    "signal_acceptance_resolver_module",
    "accepted_signal_id",
    "accepted_signal_category",
    "accepted_matter_id",
    "accepted_matter_family",
    "accepted_matter_kind",
    "recognized_source_artifact_id",
    "recognized_source_artifact_path",
    "recognized_source_artifact_family",
    "recognized_source_artifact_outcome",
)

DECLARED_SCOPE_FIELDS = (
    "scope_id",
    "scope_family",
    "scope_kind",
    "scope_matter_id",
    "scope_purpose",
    "scope_boundary",
    "applies_to",
    "does_not_apply_to",
)

SCOPE_LIMIT_TRUE_FIELDS = (
    "scope_for_applicability_only",
    "presence_not_yet_established",
    "threshold_not_yet_met",
    "truth_not_created",
    "action_not_authorized",
    "routing_not_created",
    "workflow_not_created",
    "body_relevance_medium_not_created",
    "follow_on_work_not_authorized",
)

SCOPE_LIMIT_FIELD_BLOCK_CODES = {
    "scope_for_applicability_only": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
    "presence_not_yet_established": "SCOPE_ATTEMPTS_PRESENCE",
    "threshold_not_yet_met": "SCOPE_ATTEMPTS_THRESHOLD",
    "truth_not_created": "SCOPE_ATTEMPTS_TRUTH",
    "action_not_authorized": "SCOPE_ATTEMPTS_ACTION_AUTHORIZATION",
    "routing_not_created": "SCOPE_ATTEMPTS_SIGNAL_ROUTER",
    "workflow_not_created": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
    "body_relevance_medium_not_created": "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
    "follow_on_work_not_authorized": "SCOPE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION",
}

HIERARCHY_FALSE_FIELDS = (
    "scoped_signal_allowed_as_authority",
    "scoped_signal_allowed_as_permission",
    "scoped_signal_allowed_as_currentness",
    "scoped_signal_allowed_as_truth",
    "scoped_signal_allowed_as_presence",
    "scoped_signal_allowed_as_threshold",
    "scoped_signal_allowed_as_action_trigger",
    "scoped_signal_allowed_as_workflow",
    "scoped_signal_allowed_as_route",
    "scoped_signal_allowed_as_body_relevance_medium",
    "derivative_signal_allowed_as_source",
    "operator_signal_allowed_as_source",
    "reentry_signal_allowed_as_governing_basis",
    "latest_file_recency_allowed",
)

HIERARCHY_FIELD_BLOCK_CODES = {
    "scoped_signal_allowed_as_authority": "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY",
    "scoped_signal_allowed_as_permission": "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION",
    "scoped_signal_allowed_as_currentness": "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
    "scoped_signal_allowed_as_truth": "SCOPE_ATTEMPTS_TRUTH",
    "scoped_signal_allowed_as_presence": "SCOPE_ATTEMPTS_PRESENCE",
    "scoped_signal_allowed_as_threshold": "SCOPE_ATTEMPTS_THRESHOLD",
    "scoped_signal_allowed_as_action_trigger": "SCOPE_ATTEMPTS_ACTION_AUTHORIZATION",
    "scoped_signal_allowed_as_workflow": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
    "scoped_signal_allowed_as_route": "DECLARED_SCOPE_ATTEMPTS_ROUTING",
    "scoped_signal_allowed_as_body_relevance_medium": (
        "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
    ),
    "derivative_signal_allowed_as_source": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "operator_signal_allowed_as_source": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "reentry_signal_allowed_as_governing_basis": (
        "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE"
    ),
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = (
    "must_preserve_accepted_signal_identity",
    "must_preserve_recognized_source_identity",
    "must_preserve_signal_category",
    "must_preserve_accepted_matter",
    "must_preserve_scope_boundary",
    "must_preserve_signal_non_authority",
    "must_preserve_signal_non_permission",
    "must_preserve_signal_non_currentness",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

CORRESPONDENCE_FIELD_BLOCK_CODES = {
    "must_preserve_accepted_signal_identity": "ACCEPTED_SIGNAL_IDENTITY_MISMATCH",
    "must_preserve_recognized_source_identity": "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
    "must_preserve_signal_category": "SIGNAL_CATEGORY_MISMATCH",
    "must_preserve_accepted_matter": "ACCEPTED_MATTER_MISMATCH",
    "must_preserve_scope_boundary": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
    "must_preserve_signal_non_authority": "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY",
    "must_preserve_signal_non_permission": "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION",
    "must_preserve_signal_non_currentness": "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "DECLARED_SCOPE_WIDENS_MATTER",
    "must_prevent_under_mirroring": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_create_truth",
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
    "does_not_widen_matter",
    "does_not_apply_outside_declared_scope",
)

RESULT_NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "truth_created": False,
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
    "matter_widened": False,
    "applied_outside_declared_scope": False,
}

REQUIRED_APPLIES_TO_MARKERS = (
    "body_pass_signal",
    "current_signal_recognition_standing",
    "non_operative",
)

REQUIRED_DOES_NOT_APPLY_TO_MARKERS = (
    "action",
    "permission",
    "currentness",
    "governing_basis",
    "signal_use",
    "routing",
    "workflow",
    "body_relevance_medium",
    "presence",
    "threshold",
    "truth",
    "decision",
    "consequence",
    "general_continuation",
    "unrelated_matters",
)

BLOCK_REASONS = {
    "SIGNAL_ACCEPTANCE_RESULT_MISSING": "A signal-acceptance result is required.",
    "SIGNAL_ACCEPTANCE_RESULT_UNREADABLE": (
        "The explicit signal-acceptance result path could not be read."
    ),
    "SIGNAL_ACCEPTANCE_RESULT_MALFORMED": (
        "The selected signal-acceptance result is malformed."
    ),
    "SIGNAL_ACCEPTANCE_RESULT_NOT_ACCEPTED": (
        "The selected signal-acceptance result is not SIGNAL_ACCEPTED."
    ),
    "ACCEPTED_SIGNAL_MISSING": "The selected acceptance result has no accepted signal.",
    "ACCEPTED_SIGNAL_IDENTITY_MISMATCH": (
        "The scope request does not preserve accepted signal identity."
    ),
    "RECOGNIZED_SOURCE_IDENTITY_MISMATCH": (
        "The scope request does not preserve recognized source identity."
    ),
    "SIGNAL_CATEGORY_MISMATCH": (
        "The scope request does not preserve accepted signal category."
    ),
    "ACCEPTED_MATTER_MISMATCH": (
        "The accepted matter is missing, unsupported, or not preserved."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY": (
        "The accepted signal is treated as authority."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION": (
        "The accepted signal is treated as permission."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS": (
        "The accepted signal is treated as currentness."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_PRESENCE": (
        "The accepted signal is treated as presence."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_THRESHOLD": (
        "The accepted signal is treated as threshold."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_TRUTH": "The accepted signal is treated as truth.",
    "ACCEPTED_SIGNAL_TREATED_AS_ACTION": "The accepted signal is treated as action.",
    "ACCEPTED_SIGNAL_TREATED_AS_ROUTE": "The accepted signal is treated as route.",
    "ACCEPTED_SIGNAL_TREATED_AS_WORKFLOW": (
        "The accepted signal is treated as workflow."
    ),
    "ACCEPTED_SIGNAL_TREATED_AS_BODY_RELEVANCE_MEDIUM": (
        "The accepted signal is treated as a body relevance medium."
    ),
    "SIGNAL_SCOPE_REQUEST_MISSING": "A signal-scope request is required.",
    "SIGNAL_SCOPE_REQUEST_MALFORMED": "The signal-scope request is malformed.",
    "DECLARED_SCOPE_MISSING": "The scope request does not declare a scope.",
    "DECLARED_SCOPE_UNSUPPORTED": "The declared scope is not supported.",
    "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED": (
        "The declared scope is vague, unbounded, or under-mirrored."
    ),
    "DECLARED_SCOPE_WIDENS_MATTER": "The declared scope widens the accepted matter.",
    "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER": (
        "The declared scope applies outside the accepted matter."
    ),
    "DECLARED_SCOPE_ATTEMPTS_ACTION": "The declared scope attempts action.",
    "DECLARED_SCOPE_ATTEMPTS_WORKFLOW": "The declared scope attempts workflow.",
    "DECLARED_SCOPE_ATTEMPTS_ROUTING": "The declared scope attempts routing.",
    "DECLARED_SCOPE_ATTEMPTS_ROADMAP": "The declared scope attempts roadmap.",
    "DECLARED_SCOPE_ATTEMPTS_SIGNAL_USE": "The declared scope attempts signal use.",
    "DECLARED_SCOPE_ATTEMPTS_GENERAL_CONTINUATION": (
        "The declared scope attempts general continuation."
    ),
    "DECLARED_SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM": (
        "The declared scope attempts body relevance medium implementation."
    ),
    "SCOPE_ATTEMPTS_PRESENCE": "Scope attempts to establish presence.",
    "SCOPE_ATTEMPTS_THRESHOLD": "Scope attempts to meet threshold.",
    "SCOPE_ATTEMPTS_TRUTH": "Scope attempts to create truth.",
    "SCOPE_ATTEMPTS_ACTION_AUTHORIZATION": (
        "Scope attempts to authorize action."
    ),
    "SCOPE_ATTEMPTS_FOLLOW_ON_AUTHORIZATION": (
        "Scope attempts to authorize follow-on work."
    ),
    "SCOPE_ATTEMPTS_SIGNAL_ROUTER": "Scope attempts to create signal routing.",
    "SCOPE_ATTEMPTS_EVENT_BUS": "Scope attempts to create an event bus.",
    "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM": (
        "Scope attempts to create a body relevance medium."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required non-claim is missing or flipped.",
    "LATEST_FILE_RECENCY_REFUSED": "Latest-file recency is refused.",
    "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE": (
        "Derivative, operator, re-entry, or signal source distinction collapsed."
    ),
    "SCOPED_SIGNAL_BECAME_PERMISSION": "The scoped signal was treated as permission.",
    "SCOPED_SIGNAL_BECAME_ACTION": "The scoped signal was treated as action.",
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


def _marker_blob(value: Any) -> str:
    text = _value_text_blob(value)
    return _normal_text(text)


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
        raise BodySignalScopeError(
            f"signal-acceptance result is unreadable: {resolved}",
            "SIGNAL_ACCEPTANCE_RESULT_UNREADABLE",
        ) from exc
    except json.JSONDecodeError as exc:
        raise BodySignalScopeError(
            f"signal-acceptance result is malformed JSON: {resolved}",
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        ) from exc
    if not isinstance(value, dict):
        raise BodySignalScopeError(
            f"signal-acceptance result JSON must be an object: {resolved}",
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        )
    return value


def _request_mapping(value: Any) -> dict[str, Any]:
    return _clone(dict(value)) if isinstance(value, Mapping) else {}


def _metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    explicit = _first_mapping(
        result,
        (
            "body_signal_acceptance_metadata",
            "body_signal_scope_metadata",
        ),
    )
    if explicit:
        return explicit
    for key, value in result.items():
        if isinstance(value, Mapping) and "metadata" in str(key):
            return value
    return {}


def _accepted_signal(result: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    value = result.get("accepted_signal")
    return value if isinstance(value, Mapping) else {}


def _declared_matter(result: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(result, Mapping):
        return {}
    matter = result.get("declared_matter")
    if isinstance(matter, Mapping):
        return matter
    accepted = _accepted_signal(result)
    if accepted:
        return {
            "matter_id": accepted.get("declared_matter_id"),
            "matter_family": accepted.get("declared_matter_family"),
            "matter_kind": accepted.get("declared_matter_kind"),
            "matter_purpose": accepted.get("declared_matter_purpose"),
        }
    return {}


def _acceptance_basis_from_request(
    scope_request: Mapping[str, Any] | None,
) -> Mapping[str, Any]:
    return _section(scope_request, "accepted_signal_basis")


def _acceptance_identity(
    result: Mapping[str, Any] | None,
    *,
    result_path_hint: Path | str | None = None,
    scope_request: Mapping[str, Any] | None = None,
    selection_mode: str = "provided_signal_acceptance_mapping",
) -> dict[str, Any]:
    request_basis = _acceptance_basis_from_request(scope_request)
    if not isinstance(result, Mapping):
        return {
            "signal_acceptance_result_id": request_basis.get(
                "signal_acceptance_result_id"
            ),
            "signal_acceptance_result_path": _display_path(result_path_hint)
            or request_basis.get("signal_acceptance_result_path"),
            "signal_acceptance_result_version": request_basis.get(
                "signal_acceptance_result_version"
            ),
            "signal_acceptance_outcome": request_basis.get(
                "signal_acceptance_outcome"
            ),
            "signal_acceptance_resolver_module": request_basis.get(
                "signal_acceptance_resolver_module"
            ),
            "signal_acceptance_result_type": None,
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
            "body_signal_acceptance_result_id",
            "result_id",
            "signal_acceptance_result_id",
        ),
    )
    result_version = _first_from_mappings(
        (metadata, result),
        (
            "body_signal_acceptance_result_version",
            "result_version",
            "signal_acceptance_result_version",
        ),
    )
    resolver_module = _first_from_mappings(
        (metadata, result),
        ("resolver_module", "signal_acceptance_resolver_module"),
    )
    result_type = _first_from_mappings(
        (metadata, result),
        ("body_signal_acceptance_result_type", "result_type"),
    )
    result_path = (
        _display_path(result_path_hint)
        or _first_from_mappings(
            (result,),
            (
                "signal_acceptance_result_path",
                "result_path",
                "artifact_path",
                "path",
            ),
        )
        or request_basis.get("signal_acceptance_result_path")
    )

    return {
        "signal_acceptance_result_id": _string_or_none(
            result_id or request_basis.get("signal_acceptance_result_id")
        ),
        "signal_acceptance_result_path": _string_or_none(result_path),
        "signal_acceptance_result_version": _string_or_none(
            result_version or request_basis.get("signal_acceptance_result_version")
        ),
        "signal_acceptance_outcome": _string_or_none(
            result.get("outcome") or request_basis.get("signal_acceptance_outcome")
        ),
        "signal_acceptance_resolver_module": _string_or_none(
            resolver_module or request_basis.get("signal_acceptance_resolver_module")
        ),
        "signal_acceptance_result_type": _string_or_none(result_type),
        "selection_mode": selection_mode,
        "_result_id_exposed": result_id is not None,
        "_result_path_exposed": result_path_hint is not None
        or _first_from_mappings((result,), ("result_path", "artifact_path", "path"))
        is not None,
        "_result_version_exposed": result_version is not None,
        "_result_module_exposed": resolver_module is not None,
    }


def _accepted_signal_identity(result: Mapping[str, Any] | None) -> dict[str, Any]:
    accepted = _accepted_signal(result)
    matter = _declared_matter(result)
    non_claims = result.get("non_claims") if isinstance(result, Mapping) else {}
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    return {
        "accepted_signal_id": _string_or_none(accepted.get("accepted_signal_id")),
        "accepted_signal_category": _string_or_none(
            accepted.get("accepted_signal_category")
        ),
        "accepted_matter_id": _string_or_none(
            accepted.get("declared_matter_id") or matter.get("matter_id")
        ),
        "accepted_matter_family": _string_or_none(
            accepted.get("declared_matter_family") or matter.get("matter_family")
        ),
        "accepted_matter_kind": _string_or_none(
            accepted.get("declared_matter_kind") or matter.get("matter_kind")
        ),
        "recognized_source_artifact_id": _string_or_none(
            accepted.get("recognized_source_artifact_id")
        ),
        "recognized_source_artifact_path": _string_or_none(
            accepted.get("recognized_source_artifact_path")
        ),
        "recognized_source_artifact_family": _string_or_none(
            accepted.get("recognized_source_artifact_family")
        ),
        "recognized_source_artifact_outcome": _string_or_none(
            accepted.get("recognized_source_artifact_outcome")
        ),
        "non_authoritative": accepted.get("non_authoritative"),
        "non_permission": accepted.get("non_permission"),
        "non_currentness": accepted.get("non_currentness"),
        "not_present_yet": accepted.get("not_present_yet"),
        "not_threshold_yet": accepted.get("not_threshold_yet"),
        "not_truth": accepted.get("not_truth"),
        "no_action": accepted.get("no_action"),
        "no_routing": accepted.get("no_routing"),
        "no_workflow": accepted.get("no_workflow"),
        "no_body_relevance_medium": accepted.get("no_body_relevance_medium"),
        "authority_created": non_claims.get("authority_created"),
        "permission_created": non_claims.get("permission_created"),
        "currentness_created": non_claims.get("currentness_created"),
        "presence_established": non_claims.get("presence_established"),
        "threshold_met": non_claims.get("threshold_met"),
        "truth_created": non_claims.get("truth_created"),
        "action_authorized": non_claims.get("action_authorized"),
        "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
        "workflow_created": non_claims.get("workflow_created"),
        "signal_router_created": non_claims.get("signal_router_created"),
        "event_bus_created": non_claims.get("event_bus_created"),
        "body_relevance_medium_created": non_claims.get(
            "body_relevance_medium_created"
        ),
    }


def _selected_accepted_signal(result: Mapping[str, Any] | None) -> dict[str, Any]:
    accepted = _accepted_signal(result)
    return _clone(dict(accepted)) if accepted else {}


def _public_acceptance_identity(identity: Mapping[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in identity.items()
        if not str(key).startswith("_")
    }


def _request_id(scope_request: Mapping[str, Any] | None) -> str | None:
    return _string_or_none(
        _section(scope_request, "signal_scope_request_metadata").get(
            "signal_scope_request_id"
        )
    )


def _request_shape_errors(scope_request: Mapping[str, Any]) -> list[str]:
    errors: list[str] = []
    for section_name in REQUEST_SECTIONS:
        if not isinstance(scope_request.get(section_name), Mapping):
            errors.append(f"{section_name} must be an object")

    metadata = scope_request.get("signal_scope_request_metadata")
    if isinstance(metadata, Mapping):
        for field in REQUEST_METADATA_FIELDS:
            if _string_or_none(metadata.get(field)) is None:
                errors.append(f"signal_scope_request_metadata.{field} is required")

    basis = scope_request.get("accepted_signal_basis")
    if isinstance(basis, Mapping):
        for field in ACCEPTED_SIGNAL_BASIS_FIELDS:
            if _string_or_none(basis.get(field)) is None:
                errors.append(f"accepted_signal_basis.{field} is required")

    declared_scope = scope_request.get("declared_scope")
    if isinstance(declared_scope, Mapping):
        for field in DECLARED_SCOPE_FIELDS:
            value = declared_scope.get(field)
            if field in ("applies_to", "does_not_apply_to"):
                if not value:
                    errors.append(f"declared_scope.{field} is required")
            elif _string_or_none(value) is None:
                errors.append(f"declared_scope.{field} is required")
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


def _contains_any(text: str, phrases: Sequence[str]) -> bool:
    return any(phrase in text for phrase in phrases)


def _request_text(scope_request: Mapping[str, Any]) -> str:
    return _value_text_blob(scope_request)


def _scope_text(scope_request: Mapping[str, Any]) -> str:
    declared_scope = _section(scope_request, "declared_scope")
    return _value_text_blob(
        declared_scope.get("scope_id"),
        declared_scope.get("scope_family"),
        declared_scope.get("scope_kind"),
        declared_scope.get("scope_matter_id"),
        declared_scope.get("scope_purpose"),
        declared_scope.get("scope_boundary"),
        declared_scope.get("applies_to"),
    )


def _scope_positive_blob(scope_request: Mapping[str, Any]) -> str:
    declared_scope = _section(scope_request, "declared_scope")
    return _marker_blob(
        (
            declared_scope.get("scope_purpose"),
            declared_scope.get("scope_boundary"),
            declared_scope.get("applies_to"),
        )
    )


def _latest_file_recency_attempted(scope_request: Mapping[str, Any]) -> bool:
    text = _request_text(scope_request)
    return _contains_any(
        text,
        ("latest file", "latest-file", "latest_file", "newest file", "recency"),
    )


def _collapse_attempted(scope_request: Mapping[str, Any]) -> bool:
    text = _request_text(scope_request)
    return _contains_any(
        text,
        (
            "derivative as source",
            "operator as source",
            "reentry as governing",
            "re-entry as governing",
            "signal as source",
            "signal as governing",
            "governing basis from derivative",
            "current basis from derivative",
            "receipt as permission",
            "receipt into permission",
        ),
    )


def _permission_attempted(scope_request: Mapping[str, Any]) -> bool:
    text = _request_text(scope_request)
    return _contains_any(
        text,
        (
            "scoped signal creates permission",
            "scoped signal is permission",
            "scope creates permission",
            "signal means permission",
            "permission token",
            "general permission",
        ),
    )


def _action_attempted(scope_request: Mapping[str, Any]) -> bool:
    text = _request_text(scope_request)
    return _contains_any(
        text,
        (
            "scoped signal authorizes action",
            "scope authorizes action",
            "signal authorizes action",
            "action trigger",
            "trigger action",
        ),
    )


def _scope_attempt_block(scope_request: Mapping[str, Any]) -> tuple[bool, str | None, Any]:
    text = _scope_text(scope_request)
    checks = (
        (
            "DECLARED_SCOPE_ATTEMPTS_ACTION",
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
            "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
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
            "DECLARED_SCOPE_ATTEMPTS_ROUTING",
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
            "DECLARED_SCOPE_ATTEMPTS_ROADMAP",
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
            "DECLARED_SCOPE_ATTEMPTS_SIGNAL_USE",
            (
                "signal use",
                "use signal",
                "use the signal",
                "operative signal use",
            ),
        ),
        (
            "DECLARED_SCOPE_ATTEMPTS_GENERAL_CONTINUATION",
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
            "DECLARED_SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
            (
                "create body relevance medium",
                "body relevance medium implementation",
                "body relevance medium created",
            ),
        ),
        (
            "SCOPE_ATTEMPTS_PRESENCE",
            ("establish presence", "create presence"),
        ),
        (
            "SCOPE_ATTEMPTS_THRESHOLD",
            ("meet threshold", "threshold met"),
        ),
        (
            "SCOPE_ATTEMPTS_TRUTH",
            ("create truth", "make true", "truth created"),
        ),
    )
    for block_code, phrases in checks:
        if _contains_any(text, phrases):
            return False, block_code, text
    if _permission_attempted(scope_request):
        return False, "SCOPED_SIGNAL_BECAME_PERMISSION", text
    if _action_attempted(scope_request):
        return False, "SCOPED_SIGNAL_BECAME_ACTION", text
    return True, None, "declared scope stays bounded"


def _scope_markers_present(value: Any, markers: Sequence[str]) -> bool:
    blob = _marker_blob(value)
    return all(marker in blob for marker in markers)


def _scope_applies_only_to_required_posture(scope_request: Mapping[str, Any]) -> bool:
    declared_scope = _section(scope_request, "declared_scope")
    applies_to = declared_scope.get("applies_to")
    blob = _marker_blob(applies_to)
    if "body_pass_signal" not in blob:
        return False
    if "current_signal_recognition_standing" not in blob:
        return False
    return "non_operative" in blob or "nonoperative" in blob


def _scope_excludes_required_terms(scope_request: Mapping[str, Any]) -> bool:
    declared_scope = _section(scope_request, "declared_scope")
    return _scope_markers_present(
        declared_scope.get("does_not_apply_to"),
        REQUIRED_DOES_NOT_APPLY_TO_MARKERS,
    )


def _positive_scope_includes_forbidden(scope_request: Mapping[str, Any]) -> tuple[bool, str | None]:
    blob = _scope_positive_blob(scope_request)
    checks = (
        ("action", "DECLARED_SCOPE_ATTEMPTS_ACTION"),
        ("permission", "SCOPED_SIGNAL_BECAME_PERMISSION"),
        ("currentness", "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS"),
        ("governing_basis", "DECLARED_SCOPE_WIDENS_MATTER"),
        ("signal_use", "DECLARED_SCOPE_ATTEMPTS_SIGNAL_USE"),
        ("routing", "DECLARED_SCOPE_ATTEMPTS_ROUTING"),
        ("workflow", "DECLARED_SCOPE_ATTEMPTS_WORKFLOW"),
        ("body_relevance_medium", "DECLARED_SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"),
        ("presence", "SCOPE_ATTEMPTS_PRESENCE"),
        ("threshold", "SCOPE_ATTEMPTS_THRESHOLD"),
        ("truth", "SCOPE_ATTEMPTS_TRUTH"),
        ("decision", "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED"),
        ("consequence", "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED"),
        ("general_continuation", "DECLARED_SCOPE_ATTEMPTS_GENERAL_CONTINUATION"),
        ("unrelated_matters", "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER"),
    )
    applies_blob = _marker_blob(_section(scope_request, "declared_scope").get("applies_to"))
    for marker, block_code in checks:
        if marker in applies_blob:
            return True, block_code
    return False, None


def _basis_matches_acceptance(
    request_basis: Mapping[str, Any],
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    *,
    path_required: bool,
) -> tuple[bool, str | None, Any]:
    acceptance_outcome = request_basis.get("signal_acceptance_outcome")
    if not _loose_equal(acceptance_outcome, OUTCOME_SIGNAL_ACCEPTED):
        return False, "SIGNAL_ACCEPTANCE_RESULT_NOT_ACCEPTED", acceptance_outcome

    expected_result_id = acceptance_identity.get("signal_acceptance_result_id")
    actual_result_id = request_basis.get("signal_acceptance_result_id")
    if expected_result_id and actual_result_id and not _loose_equal(
        actual_result_id,
        expected_result_id,
    ):
        return False, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_result_id,
            "actual": actual_result_id,
        }

    expected_path = acceptance_identity.get("signal_acceptance_result_path")
    actual_path = request_basis.get("signal_acceptance_result_path")
    if expected_path and (path_required or actual_path is not None) and not _path_equal(
        actual_path,
        expected_path,
    ):
        return False, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_path,
            "actual": actual_path,
        }

    expected_version = acceptance_identity.get("signal_acceptance_result_version")
    actual_version = request_basis.get("signal_acceptance_result_version")
    if expected_version and actual_version and not _loose_equal(
        actual_version,
        expected_version,
    ):
        return False, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_version,
            "actual": actual_version,
        }

    expected_module = acceptance_identity.get("signal_acceptance_resolver_module")
    actual_module = request_basis.get("signal_acceptance_resolver_module")
    if expected_module and actual_module and not _loose_equal(actual_module, expected_module):
        return False, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH", {
            "expected": expected_module,
            "actual": actual_module,
        }

    signal_pairs = (
        ("accepted_signal_id", _loose_equal, "ACCEPTED_SIGNAL_IDENTITY_MISMATCH"),
        ("accepted_signal_category", _loose_equal, "SIGNAL_CATEGORY_MISMATCH"),
        ("accepted_matter_id", _loose_equal, "ACCEPTED_MATTER_MISMATCH"),
        ("accepted_matter_family", _loose_family_equal, "ACCEPTED_MATTER_MISMATCH"),
        ("accepted_matter_kind", _loose_family_equal, "ACCEPTED_MATTER_MISMATCH"),
        (
            "recognized_source_artifact_id",
            _loose_equal,
            "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
        ),
        (
            "recognized_source_artifact_path",
            _path_equal,
            "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
        ),
        (
            "recognized_source_artifact_family",
            _loose_family_equal,
            "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
        ),
        (
            "recognized_source_artifact_outcome",
            _loose_equal,
            "RECOGNIZED_SOURCE_IDENTITY_MISMATCH",
        ),
    )
    for key, comparator, block_code in signal_pairs:
        expected = accepted_identity.get(key)
        actual = request_basis.get(key)
        if expected and not comparator(actual, expected):
            return False, block_code, {
                "field": key,
                "expected": expected,
                "actual": actual,
            }
    return True, None, "accepted signal basis preserved"


def _accepted_signal_non_collapse_checks(
    accepted_identity: Mapping[str, Any],
) -> list[dict[str, Any]]:
    return [
        _check(
            "accepted_signal_remains_non_authoritative",
            accepted_identity.get("non_authoritative") is True
            and accepted_identity.get("authority_created") is False,
            "accepted signal non_authoritative true and authority_created false",
            {
                "non_authoritative": accepted_identity.get("non_authoritative"),
                "authority_created": accepted_identity.get("authority_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_AUTHORITY",
        ),
        _check(
            "accepted_signal_remains_non_permission",
            accepted_identity.get("non_permission") is True
            and accepted_identity.get("permission_created") is False,
            "accepted signal non_permission true and permission_created false",
            {
                "non_permission": accepted_identity.get("non_permission"),
                "permission_created": accepted_identity.get("permission_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_PERMISSION",
        ),
        _check(
            "accepted_signal_remains_non_currentness",
            accepted_identity.get("non_currentness") is True
            and accepted_identity.get("currentness_created") is False,
            "accepted signal non_currentness true and currentness_created false",
            {
                "non_currentness": accepted_identity.get("non_currentness"),
                "currentness_created": accepted_identity.get("currentness_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "accepted_signal_is_not_presence",
            accepted_identity.get("not_present_yet") is True
            and accepted_identity.get("presence_established") is False,
            "accepted signal not_present_yet true and presence_established false",
            {
                "not_present_yet": accepted_identity.get("not_present_yet"),
                "presence_established": accepted_identity.get("presence_established"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_PRESENCE",
        ),
        _check(
            "accepted_signal_is_not_threshold",
            accepted_identity.get("not_threshold_yet") is True
            and accepted_identity.get("threshold_met") is False,
            "accepted signal not_threshold_yet true and threshold_met false",
            {
                "not_threshold_yet": accepted_identity.get("not_threshold_yet"),
                "threshold_met": accepted_identity.get("threshold_met"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_THRESHOLD",
        ),
        _check(
            "accepted_signal_is_not_truth",
            accepted_identity.get("not_truth") is True
            and accepted_identity.get("truth_created") is False,
            "accepted signal not_truth true and truth_created false",
            {
                "not_truth": accepted_identity.get("not_truth"),
                "truth_created": accepted_identity.get("truth_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_TRUTH",
        ),
        _check(
            "accepted_signal_is_not_action",
            accepted_identity.get("no_action") is True
            and accepted_identity.get("action_authorized") is False,
            "accepted signal no_action true and action_authorized false",
            {
                "no_action": accepted_identity.get("no_action"),
                "action_authorized": accepted_identity.get("action_authorized"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_ACTION",
        ),
        _check(
            "accepted_signal_is_not_route",
            accepted_identity.get("no_routing") is True
            and accepted_identity.get("signal_router_created") is False
            and accepted_identity.get("event_bus_created") is False,
            "accepted signal no_routing true and router/event bus false",
            {
                "no_routing": accepted_identity.get("no_routing"),
                "signal_router_created": accepted_identity.get("signal_router_created"),
                "event_bus_created": accepted_identity.get("event_bus_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_ROUTE",
        ),
        _check(
            "accepted_signal_is_not_workflow",
            accepted_identity.get("no_workflow") is True
            and accepted_identity.get("workflow_created") is False,
            "accepted signal no_workflow true and workflow_created false",
            {
                "no_workflow": accepted_identity.get("no_workflow"),
                "workflow_created": accepted_identity.get("workflow_created"),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_WORKFLOW",
        ),
        _check(
            "accepted_signal_is_not_body_relevance_medium",
            accepted_identity.get("no_body_relevance_medium") is True
            and accepted_identity.get("body_relevance_medium_created") is False,
            (
                "accepted signal no_body_relevance_medium true and "
                "body_relevance_medium_created false"
            ),
            {
                "no_body_relevance_medium": accepted_identity.get(
                    "no_body_relevance_medium"
                ),
                "body_relevance_medium_created": accepted_identity.get(
                    "body_relevance_medium_created"
                ),
            },
            "ACCEPTED_SIGNAL_TREATED_AS_BODY_RELEVANCE_MEDIUM",
        ),
    ]


def _anti_collapse_checks(
    scope_request: Mapping[str, Any],
    hierarchy: Mapping[str, Any],
    declared_non_claims: Mapping[str, Any],
) -> list[dict[str, Any]]:
    latest_recency = (
        hierarchy.get("latest_file_recency_allowed") is not False
        or _latest_file_recency_attempted(scope_request)
    )
    collapse = (
        hierarchy.get("derivative_signal_allowed_as_source") is not False
        or hierarchy.get("operator_signal_allowed_as_source") is not False
        or hierarchy.get("reentry_signal_allowed_as_governing_basis") is not False
        or _collapse_attempted(scope_request)
    )
    permission_attempt = (
        hierarchy.get("scoped_signal_allowed_as_permission") is not False
        or declared_non_claims.get("does_not_create_permission") is not True
        or _permission_attempted(scope_request)
    )
    action_attempt = (
        hierarchy.get("scoped_signal_allowed_as_action_trigger") is not False
        or declared_non_claims.get("does_not_authorize_action") is not True
        or _action_attempted(scope_request)
    )
    return [
        _check(
            "latest_file_recency_is_refused",
            not latest_recency,
            "scope does not infer currentness by latest-file recency",
            {
                "latest_file_recency_allowed": hierarchy.get(
                    "latest_file_recency_allowed"
                ),
                "latest_file_recency_language_detected": _latest_file_recency_attempted(
                    scope_request
                ),
            },
            "LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "derivative_api_operator_reentry_signal_surfaces_do_not_become_governing_current_basis",
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
                "collapse_language_detected": _collapse_attempted(scope_request),
            },
            "DERIVATIVE_OPERATOR_REENTRY_SIGNAL_SOURCE_COLLAPSE",
        ),
        _check(
            "scoped_signal_does_not_become_permission",
            not permission_attempt,
            "scoped signal remains non-permission",
            {
                "scoped_signal_allowed_as_permission": hierarchy.get(
                    "scoped_signal_allowed_as_permission"
                ),
                "does_not_create_permission": declared_non_claims.get(
                    "does_not_create_permission"
                ),
                "permission_language_detected": _permission_attempted(scope_request),
            },
            "SCOPED_SIGNAL_BECAME_PERMISSION",
        ),
        _check(
            "scoped_signal_does_not_become_action",
            not action_attempt,
            "scoped signal remains non-action",
            {
                "scoped_signal_allowed_as_action_trigger": hierarchy.get(
                    "scoped_signal_allowed_as_action_trigger"
                ),
                "does_not_authorize_action": declared_non_claims.get(
                    "does_not_authorize_action"
                ),
                "action_language_detected": _action_attempted(scope_request),
            },
            "SCOPED_SIGNAL_BECAME_ACTION",
        ),
        _check(
            "body_relevance_medium_is_not_created",
            hierarchy.get("scoped_signal_allowed_as_body_relevance_medium") is False
            and declared_non_claims.get("does_not_create_body_relevance_medium")
            is True,
            "scope does not create a body relevance medium",
            {
                "scoped_signal_allowed_as_body_relevance_medium": hierarchy.get(
                    "scoped_signal_allowed_as_body_relevance_medium"
                ),
                "does_not_create_body_relevance_medium": declared_non_claims.get(
                    "does_not_create_body_relevance_medium"
                ),
            },
            "SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM",
        ),
    ]


def _build_checks(
    acceptance_result: Mapping[str, Any] | None,
    scope_request: Mapping[str, Any] | None,
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    *,
    path_based: bool,
    acceptance_readable: bool,
    acceptance_malformed: bool,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    acceptance_exists = isinstance(acceptance_result, Mapping)
    request_exists = isinstance(scope_request, Mapping)
    request_errors = (
        _request_shape_errors(scope_request) if isinstance(scope_request, Mapping) else []
    )
    request_well_formed = request_exists and not request_errors
    request_basis = _section(scope_request, "accepted_signal_basis")
    declared_scope = _section(scope_request, "declared_scope")
    scope_limits = _section(scope_request, "declared_scope_limits")
    hierarchy = _section(scope_request, "hierarchy_constraints")
    correspondence = _section(scope_request, "correspondence_requirements")
    declared_non_claims = _section(scope_request, "declared_non_claims")

    checks.append(
        _check(
            "signal_acceptance_result_exists",
            acceptance_exists,
            "one SIGNAL_ACCEPTED result mapping",
            "present" if acceptance_exists else "missing",
            "SIGNAL_ACCEPTANCE_RESULT_MISSING",
        )
    )
    checks.append(
        _check(
            "signal_acceptance_result_is_readable_if_path_based",
            acceptance_exists and acceptance_readable and not acceptance_malformed,
            "readable signal-acceptance JSON object for explicit path, provided object otherwise",
            "readable"
            if acceptance_exists and acceptance_readable and not acceptance_malformed
            else "unreadable or malformed",
            "SIGNAL_ACCEPTANCE_RESULT_UNREADABLE"
            if not acceptance_malformed
            else "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        )
    )
    checks.append(
        _check(
            "signal_acceptance_result_is_well_formed_enough",
            acceptance_exists and isinstance(acceptance_result, Mapping),
            "signal-acceptance result is an object",
            type(acceptance_result).__name__ if acceptance_result is not None else "missing",
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        )
    )
    checks.append(
        _check(
            "signal_acceptance_result_outcome_is_signal_accepted",
            _loose_equal(
                acceptance_identity.get("signal_acceptance_outcome"),
                OUTCOME_SIGNAL_ACCEPTED,
            ),
            "SIGNAL_ACCEPTED",
            acceptance_identity.get("signal_acceptance_outcome"),
            "SIGNAL_ACCEPTANCE_RESULT_NOT_ACCEPTED",
        )
    )
    checks.append(
        _check(
            "accepted_signal_is_present",
            bool(accepted_identity.get("accepted_signal_id"))
            and bool(accepted_identity.get("accepted_signal_category")),
            "accepted signal id and category present",
            {
                "accepted_signal_id": accepted_identity.get("accepted_signal_id"),
                "accepted_signal_category": accepted_identity.get(
                    "accepted_signal_category"
                ),
            },
            "ACCEPTED_SIGNAL_MISSING",
        )
    )
    checks.append(
        _check(
            "accepted_signal_identity_is_preserved",
            bool(accepted_identity.get("accepted_signal_id")),
            "accepted signal identity present",
            accepted_identity.get("accepted_signal_id"),
            "ACCEPTED_SIGNAL_IDENTITY_MISMATCH",
        )
    )
    source_identity_present = all(
        _string_or_none(accepted_identity.get(key)) is not None
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
                key: accepted_identity.get(key)
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
            "accepted_signal_category_is_preserved",
            _string_or_none(accepted_identity.get("accepted_signal_category")) is not None,
            "accepted signal category present",
            accepted_identity.get("accepted_signal_category"),
            "SIGNAL_CATEGORY_MISMATCH",
        )
    )
    checks.append(
        _check(
            "accepted_signal_category_is_body_pass_signal",
            _loose_equal(
                accepted_identity.get("accepted_signal_category"),
                SUPPORTED_SIGNAL_CATEGORY,
            ),
            SUPPORTED_SIGNAL_CATEGORY,
            accepted_identity.get("accepted_signal_category"),
            "SIGNAL_CATEGORY_MISMATCH",
        )
    )
    matter_identity_present = all(
        _string_or_none(accepted_identity.get(key)) is not None
        for key in ("accepted_matter_id", "accepted_matter_family", "accepted_matter_kind")
    )
    checks.append(
        _check(
            "accepted_matter_identity_is_preserved",
            matter_identity_present,
            "accepted matter id/family/kind present",
            {
                "accepted_matter_id": accepted_identity.get("accepted_matter_id"),
                "accepted_matter_family": accepted_identity.get("accepted_matter_family"),
                "accepted_matter_kind": accepted_identity.get("accepted_matter_kind"),
            },
            "ACCEPTED_MATTER_MISMATCH",
        )
    )
    checks.append(
        _check(
            "accepted_matter_is_current_signal_recognition_standing",
            _loose_equal(
                accepted_identity.get("accepted_matter_id"),
                SUPPORTED_ACCEPTED_MATTER_ID,
            ),
            SUPPORTED_ACCEPTED_MATTER_ID,
            accepted_identity.get("accepted_matter_id"),
            "ACCEPTED_MATTER_MISMATCH",
        )
    )
    checks.extend(_accepted_signal_non_collapse_checks(accepted_identity))

    checks.append(
        _check(
            "signal_scope_request_exists",
            request_exists,
            "one signal-scope request mapping",
            "present" if request_exists else "missing",
            "SIGNAL_SCOPE_REQUEST_MISSING",
        )
    )
    declared_scope_present = isinstance(
        scope_request.get("declared_scope") if request_exists else None,
        Mapping,
    )
    checks.append(
        _check(
            "declared_scope_is_present",
            declared_scope_present,
            "declared_scope object present",
            "present" if declared_scope_present else "missing",
            "DECLARED_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "signal_scope_request_is_well_formed_enough",
            request_well_formed,
            "required scope request sections and core fields present",
            request_errors or "well formed enough",
            "SIGNAL_SCOPE_REQUEST_MALFORMED",
        )
    )

    basis_matches, basis_block, basis_actual = (
        _basis_matches_acceptance(
            request_basis,
            acceptance_identity,
            accepted_identity,
            path_required=path_based,
        )
        if request_exists
        else (False, "SIGNAL_SCOPE_REQUEST_MISSING", "request missing")
    )
    checks.append(
        _check(
            "accepted_signal_basis_matches_selected_acceptance_result",
            basis_matches,
            "request basis matches selected acceptance result, accepted matter, and recognized source",
            basis_actual,
            basis_block or "ACCEPTED_SIGNAL_IDENTITY_MISMATCH",
        )
    )

    checks.append(
        _check(
            "declared_scope_id_is_supported",
            _loose_equal(declared_scope.get("scope_id"), SUPPORTED_SCOPE_ID),
            SUPPORTED_SCOPE_ID,
            declared_scope.get("scope_id"),
            "DECLARED_SCOPE_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "declared_scope_family_and_kind_are_supported",
            _loose_equal(declared_scope.get("scope_family"), SUPPORTED_SCOPE_FAMILY)
            and _loose_equal(declared_scope.get("scope_kind"), SUPPORTED_SCOPE_KIND),
            {"scope_family": SUPPORTED_SCOPE_FAMILY, "scope_kind": SUPPORTED_SCOPE_KIND},
            {
                "scope_family": declared_scope.get("scope_family"),
                "scope_kind": declared_scope.get("scope_kind"),
            },
            "DECLARED_SCOPE_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "declared_scope_matter_matches_accepted_matter",
            _loose_equal(
                declared_scope.get("scope_matter_id"),
                accepted_identity.get("accepted_matter_id"),
            )
            and _loose_equal(
                declared_scope.get("scope_matter_id"),
                SUPPORTED_ACCEPTED_MATTER_ID,
            ),
            accepted_identity.get("accepted_matter_id") or SUPPORTED_ACCEPTED_MATTER_ID,
            declared_scope.get("scope_matter_id"),
            "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER",
        )
    )

    attempt_passed, attempt_block, attempt_actual = (
        _scope_attempt_block(scope_request)
        if request_exists
        else (False, "SIGNAL_SCOPE_REQUEST_MISSING", "request missing")
    )
    forbidden_positive, forbidden_block = (
        _positive_scope_includes_forbidden(scope_request)
        if request_exists
        else (False, None)
    )
    checks.append(
        _check(
            "declared_scope_is_bounded_to_nonoperative_body_pass_signal_posture",
            attempt_passed
            and not forbidden_positive
            and _scope_applies_only_to_required_posture(scope_request or {}),
            "non-operative BODY_PASS_SIGNAL posture inside current_signal_recognition_standing",
            attempt_actual
            if attempt_passed and not forbidden_positive
            else {"blocked_scope_text": attempt_actual},
            attempt_block
            or forbidden_block
            or "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
        )
    )
    checks.append(
        _check(
            "declared_scope_excludes_forbidden_applicability",
            _scope_excludes_required_terms(scope_request or {}),
            "does_not_apply_to includes action, permission, currentness, governing basis, signal use, routing, workflow, body relevance medium, presence, threshold, truth, decision, consequence, general continuation, and unrelated matters",
            declared_scope.get("does_not_apply_to"),
            "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER",
        )
    )
    for marker in REQUIRED_DOES_NOT_APPLY_TO_MARKERS:
        checks.append(
            _check(
                f"declared_scope_excludes_{marker}",
                marker in _marker_blob(declared_scope.get("does_not_apply_to")),
                f"does_not_apply_to includes {marker}",
                declared_scope.get("does_not_apply_to"),
                {
                    "action": "DECLARED_SCOPE_ATTEMPTS_ACTION",
                    "permission": "SCOPED_SIGNAL_BECAME_PERMISSION",
                    "currentness": "ACCEPTED_SIGNAL_TREATED_AS_CURRENTNESS",
                    "governing_basis": "DECLARED_SCOPE_WIDENS_MATTER",
                    "signal_use": "DECLARED_SCOPE_ATTEMPTS_SIGNAL_USE",
                    "routing": "DECLARED_SCOPE_ATTEMPTS_ROUTING",
                    "workflow": "DECLARED_SCOPE_ATTEMPTS_WORKFLOW",
                    "body_relevance_medium": (
                        "DECLARED_SCOPE_ATTEMPTS_BODY_RELEVANCE_MEDIUM"
                    ),
                    "presence": "SCOPE_ATTEMPTS_PRESENCE",
                    "threshold": "SCOPE_ATTEMPTS_THRESHOLD",
                    "truth": "SCOPE_ATTEMPTS_TRUTH",
                    "decision": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
                    "consequence": "DECLARED_SCOPE_VAGUE_OR_UNBOUNDED",
                    "general_continuation": (
                        "DECLARED_SCOPE_ATTEMPTS_GENERAL_CONTINUATION"
                    ),
                    "unrelated_matters": (
                        "DECLARED_SCOPE_APPLIES_OUTSIDE_ACCEPTED_MATTER"
                    ),
                }[marker],
            )
        )

    bad_scope_limit = _first_bad_true_field(SCOPE_LIMIT_TRUE_FIELDS, scope_limits)
    checks.append(
        _check(
            "scope_limits_are_preserved",
            bad_scope_limit is None,
            "all scope-limit fields present and true",
            "all true"
            if bad_scope_limit is None
            else {bad_scope_limit: scope_limits.get(bad_scope_limit)},
            SCOPE_LIMIT_FIELD_BLOCK_CODES.get(
                bad_scope_limit or "",
                "SIGNAL_SCOPE_REQUEST_MALFORMED",
            ),
        )
    )
    for field in SCOPE_LIMIT_TRUE_FIELDS:
        checks.append(
            _check(
                field,
                scope_limits.get(field) is True,
                f"{field} is true",
                scope_limits.get(field),
                SCOPE_LIMIT_FIELD_BLOCK_CODES[field],
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
                "SIGNAL_SCOPE_REQUEST_MALFORMED",
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
                "SIGNAL_SCOPE_REQUEST_MALFORMED",
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
            scope_request or {},
            hierarchy,
            declared_non_claims,
        )
    )
    return checks


def _result_id(
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    scope_request: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    request_id = _request_id(scope_request or {}) or "signal_scope_request"
    signal_id = accepted_identity.get("accepted_signal_id") or acceptance_identity.get(
        "signal_acceptance_result_id"
    )
    signal_id = signal_id or "accepted_signal"
    return (
        f"{_safe_filename_part(request_id)}__"
        f"{_safe_filename_part(signal_id)}__"
        f"body_signal_scope_{outcome.lower()}"
    )


def _result_metadata(
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    scope_request: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "body_signal_scope_result_id": _result_id(
            acceptance_identity,
            accepted_identity,
            scope_request,
            outcome,
        ),
        "body_signal_scope_result_type": BODY_SIGNAL_SCOPE_RESULT_TYPE,
        "body_signal_scope_result_version": BODY_SIGNAL_SCOPE_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _scoped_signal(
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    scope_request: Mapping[str, Any],
) -> dict[str, Any]:
    declared_scope = _section(scope_request, "declared_scope")
    request_id = _request_id(scope_request) or "signal_scope_request"
    accepted_signal_id = accepted_identity.get("accepted_signal_id") or "accepted_signal"
    return {
        "scoped_signal_id": (
            f"{_safe_filename_part(request_id)}__"
            f"{_safe_filename_part(accepted_signal_id)}__scoped"
        ),
        "scoped_signal_category": accepted_identity.get("accepted_signal_category"),
        "selected_signal_acceptance_result_id": acceptance_identity.get(
            "signal_acceptance_result_id"
        ),
        "selected_signal_acceptance_result_path": acceptance_identity.get(
            "signal_acceptance_result_path"
        ),
        "selected_signal_acceptance_outcome": acceptance_identity.get(
            "signal_acceptance_outcome"
        ),
        "accepted_signal_id": accepted_identity.get("accepted_signal_id"),
        "accepted_signal_category": accepted_identity.get("accepted_signal_category"),
        "recognized_source_artifact_id": accepted_identity.get(
            "recognized_source_artifact_id"
        ),
        "recognized_source_artifact_path": accepted_identity.get(
            "recognized_source_artifact_path"
        ),
        "recognized_source_artifact_family": accepted_identity.get(
            "recognized_source_artifact_family"
        ),
        "recognized_source_artifact_outcome": accepted_identity.get(
            "recognized_source_artifact_outcome"
        ),
        "accepted_matter_id": accepted_identity.get("accepted_matter_id"),
        "accepted_matter_family": accepted_identity.get("accepted_matter_family"),
        "accepted_matter_kind": accepted_identity.get("accepted_matter_kind"),
        "declared_scope_id": declared_scope.get("scope_id"),
        "declared_scope_family": declared_scope.get("scope_family"),
        "declared_scope_kind": declared_scope.get("scope_kind"),
        "declared_scope_purpose": declared_scope.get("scope_purpose"),
        "declared_scope_boundary": declared_scope.get("scope_boundary"),
        "applies_to": _clone(declared_scope.get("applies_to")),
        "does_not_apply_to": _clone(declared_scope.get("does_not_apply_to")),
        "non_authoritative": True,
        "non_permission": True,
        "non_currentness": True,
        "not_present_yet": True,
        "not_threshold_yet": True,
        "not_truth": True,
        "no_action": True,
        "no_routing": True,
        "no_workflow": True,
        "no_body_relevance_medium": True,
        "no_application_outside_declared_scope": True,
    }


def _scope_basis(
    acceptance_identity: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    scope_request: Mapping[str, Any] | None,
    outcome: str,
) -> dict[str, Any]:
    declared_scope = _section(scope_request, "declared_scope")
    return {
        "scope": "single_signal_acceptance_result_single_scope_request",
        "selected_signal_acceptance_result": _public_acceptance_identity(
            acceptance_identity
        ),
        "accepted_signal_id": accepted_identity.get("accepted_signal_id"),
        "accepted_signal_category": accepted_identity.get("accepted_signal_category"),
        "request_id": _request_id(scope_request or {}),
        "accepted_matter_id": accepted_identity.get("accepted_matter_id"),
        "declared_scope_id": declared_scope.get("scope_id")
        if isinstance(scope_request, Mapping)
        else None,
        "outcome": outcome,
        "scope_for_applicability_only": outcome == OUTCOME_SIGNAL_SCOPED,
        "scope_establishes_presence": False,
        "scope_meets_threshold": False,
        "scope_creates_truth": False,
        "scope_creates_authority": False,
        "scope_creates_permission": False,
        "scope_creates_currentness": False,
        "scope_routes_signal": False,
        "scope_uses_signal": False,
        "scope_authorizes_action": False,
        "scope_authorizes_follow_on_work": False,
        "scope_creates_body_relevance_medium": False,
        "scope_applies_outside_declared_scope": False,
    }


def _build_result(
    *,
    acceptance_identity: Mapping[str, Any],
    accepted_signal: Mapping[str, Any],
    accepted_identity: Mapping[str, Any],
    scope_request: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None = None,
) -> dict[str, Any]:
    request_copy = _request_mapping(scope_request)
    result: dict[str, Any] = {
        "body_signal_scope_metadata": _result_metadata(
            acceptance_identity,
            accepted_identity,
            request_copy,
            outcome,
        ),
        "selected_signal_acceptance_result": _public_acceptance_identity(
            acceptance_identity
        ),
        "selected_accepted_signal": _clone(dict(accepted_signal)),
        "selected_signal_scope_request": request_copy,
        "declared_scope": _clone(dict(_section(request_copy, "declared_scope"))),
        "signal_scope_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "scoped_signal": (
            _scoped_signal(acceptance_identity, accepted_identity, request_copy)
            if outcome == OUTCOME_SIGNAL_SCOPED
            else None
        ),
        "body_signal_scope_basis": _scope_basis(
            acceptance_identity,
            accepted_identity,
            request_copy,
            outcome,
        ),
        "body_signal_scope_summary": {},
        "non_claims": dict(RESULT_NON_CLAIM_DEFAULTS),
    }
    result["body_signal_scope_summary"] = build_body_signal_scope_summary(result)
    return result


def _empty_acceptance_identity(
    *,
    result_path_hint: Path | str | None = None,
    selection_mode: str = "no_signal_acceptance_result",
) -> dict[str, Any]:
    return {
        "signal_acceptance_result_id": None,
        "signal_acceptance_result_path": _display_path(result_path_hint),
        "signal_acceptance_result_version": None,
        "signal_acceptance_outcome": None,
        "signal_acceptance_resolver_module": None,
        "signal_acceptance_result_type": None,
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
    acceptance_identity: Mapping[str, Any] | None = None,
    accepted_signal: Mapping[str, Any] | None = None,
    accepted_identity: Mapping[str, Any] | None = None,
    scope_request: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    selected_acceptance = acceptance_identity or _empty_acceptance_identity()
    selected_accepted_identity = accepted_identity or {}
    selected_checks = list(checks or [])
    if not selected_checks:
        selected_checks = [
            _check(
                "body_signal_scope_blocked",
                False,
                "bounded signal-acceptance result and scope request",
                block_detail or block_code,
                block_code,
            )
        ]
    return _build_result(
        acceptance_identity=selected_acceptance,
        accepted_signal=accepted_signal or {},
        accepted_identity=selected_accepted_identity,
        scope_request=scope_request,
        checks=selected_checks,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
    )


def _resolve_internal(
    signal_acceptance_result: Mapping[str, Any] | None,
    scope_request: Mapping[str, Any] | None,
    *,
    result_path_hint: Path | str | None = None,
    selection_mode: str = "provided_signal_acceptance_mapping",
) -> dict[str, Any]:
    if signal_acceptance_result is not None and not isinstance(
        signal_acceptance_result,
        Mapping,
    ):
        acceptance_identity = _empty_acceptance_identity(
            result_path_hint=result_path_hint,
            selection_mode="malformed_signal_acceptance_result",
        )
        return _blocked_result(
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
            block_detail="signal-acceptance result input must be a mapping",
            acceptance_identity=acceptance_identity,
            scope_request=_request_mapping(scope_request),
        )

    if scope_request is not None and not isinstance(scope_request, Mapping):
        acceptance_identity = _acceptance_identity(
            signal_acceptance_result,
            result_path_hint=result_path_hint,
            selection_mode=selection_mode,
        )
        accepted_signal = _selected_accepted_signal(signal_acceptance_result)
        accepted_identity = _accepted_signal_identity(signal_acceptance_result)
        return _blocked_result(
            "SIGNAL_SCOPE_REQUEST_MALFORMED",
            block_detail="signal-scope request input must be a mapping",
            acceptance_identity=acceptance_identity,
            accepted_signal=accepted_signal,
            accepted_identity=accepted_identity,
            scope_request={},
        )

    acceptance_identity = _acceptance_identity(
        signal_acceptance_result,
        result_path_hint=result_path_hint,
        scope_request=scope_request,
        selection_mode=selection_mode,
    )
    accepted_signal = _selected_accepted_signal(signal_acceptance_result)
    accepted_identity = _accepted_signal_identity(signal_acceptance_result)

    checks = _build_checks(
        signal_acceptance_result,
        scope_request,
        acceptance_identity,
        accepted_identity,
        path_based=result_path_hint is not None,
        acceptance_readable=signal_acceptance_result is not None,
        acceptance_malformed=False,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _build_result(
            acceptance_identity=acceptance_identity,
            accepted_signal=accepted_signal,
            accepted_identity=accepted_identity,
            scope_request=_request_mapping(scope_request),
            checks=checks,
            outcome=OUTCOME_BLOCKED,
            block_code=str(failed.get("block_code")),
        )
    return _build_result(
        acceptance_identity=acceptance_identity,
        accepted_signal=accepted_signal,
        accepted_identity=accepted_identity,
        scope_request=_request_mapping(scope_request),
        checks=checks,
        outcome=OUTCOME_SIGNAL_SCOPED,
        block_code=None,
    )


def resolve_body_signal_scope(
    signal_acceptance_result: Mapping[str, Any] | None = None,
    scope_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded body-signal scope decision."""

    try:
        return _resolve_internal(signal_acceptance_result, scope_request)
    except BodySignalScopeError as exc:
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            acceptance_identity=exc.selected_acceptance,
            scope_request=exc.selected_request or _request_mapping(scope_request),
            checks=exc.checks,
        )


def resolve_body_signal_scope_from_path(
    signal_acceptance_result_path: Path | str,
    scope_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Resolve one body-signal scope decision from an explicit path."""

    acceptance_identity = _empty_acceptance_identity(
        result_path_hint=signal_acceptance_result_path,
        selection_mode="explicit_signal_acceptance_result_path",
    )
    try:
        signal_acceptance_result = _read_json_file(signal_acceptance_result_path)
        return _resolve_internal(
            signal_acceptance_result,
            scope_request,
            result_path_hint=signal_acceptance_result_path,
            selection_mode="explicit_signal_acceptance_result_path",
        )
    except BodySignalScopeError as exc:
        checks = exc.checks
        if checks is None:
            checks = [
                _check(
                    "signal_acceptance_result_is_readable_if_path_based",
                    False,
                    "readable signal-acceptance JSON object for explicit path",
                    _display_path(signal_acceptance_result_path),
                    exc.block_code,
                )
            ]
        return _blocked_result(
            exc.block_code,
            block_detail=str(exc),
            acceptance_identity=exc.selected_acceptance or acceptance_identity,
            scope_request=_request_mapping(scope_request),
            checks=checks,
        )


def _check_passed(checks: Sequence[Any], check_name: str) -> bool:
    return any(
        isinstance(check, Mapping)
        and check.get("check_name") == check_name
        and check.get("passed") is True
        for check in checks
    )


def build_body_signal_scope_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded summary for one body-signal scope result."""

    if not isinstance(result, Mapping):
        raise BodySignalScopeError(
            "body-signal scope result must be a mapping",
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        )
    selected_acceptance = result.get("selected_signal_acceptance_result")
    selected_acceptance = (
        selected_acceptance if isinstance(selected_acceptance, Mapping) else {}
    )
    scoped_signal = result.get("scoped_signal")
    scoped_signal = scoped_signal if isinstance(scoped_signal, Mapping) else {}
    accepted_signal = result.get("selected_accepted_signal")
    accepted_signal = accepted_signal if isinstance(accepted_signal, Mapping) else {}
    declared_scope = result.get("declared_scope")
    declared_scope = declared_scope if isinstance(declared_scope, Mapping) else {}
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    checks = result.get("signal_scope_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}

    accepted_matter_id = scoped_signal.get("accepted_matter_id") or accepted_signal.get(
        "declared_matter_id"
    )
    accepted_matter_family = scoped_signal.get(
        "accepted_matter_family"
    ) or accepted_signal.get("declared_matter_family")
    accepted_matter_kind = scoped_signal.get("accepted_matter_kind") or accepted_signal.get(
        "declared_matter_kind"
    )

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_signal_acceptance_result_id": selected_acceptance.get(
            "signal_acceptance_result_id"
        ),
        "selected_signal_acceptance_result_path": selected_acceptance.get(
            "signal_acceptance_result_path"
        ),
        "selected_signal_acceptance_outcome": selected_acceptance.get(
            "signal_acceptance_outcome"
        ),
        "scoped_signal_id": scoped_signal.get("scoped_signal_id"),
        "scoped_signal_category": scoped_signal.get("scoped_signal_category"),
        "accepted_matter_id": accepted_matter_id,
        "accepted_matter_family": accepted_matter_family,
        "accepted_matter_kind": accepted_matter_kind,
        "declared_scope_id": declared_scope.get("scope_id"),
        "declared_scope_family": declared_scope.get("scope_family"),
        "declared_scope_kind": declared_scope.get("scope_kind"),
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
        "acceptance_basis_passed": _check_passed(
            checks,
            "accepted_signal_basis_matches_selected_acceptance_result",
        ),
        "scope_boundary_passed": _check_passed(
            checks,
            "declared_scope_is_bounded_to_nonoperative_body_pass_signal_posture",
        )
        and _check_passed(checks, "declared_scope_excludes_forbidden_applicability"),
        "scope_limits_passed": _check_passed(checks, "scope_limits_are_preserved"),
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
                "matter_widened",
                "applied_outside_declared_scope",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str | None = None,
) -> Path:
    scoped = result.get("scoped_signal")
    scoped = scoped if isinstance(scoped, Mapping) else {}
    request = result.get("selected_signal_scope_request")
    request = request if isinstance(request, Mapping) else {}
    acceptance = result.get("selected_signal_acceptance_result")
    acceptance = acceptance if isinstance(acceptance, Mapping) else {}
    stem = _safe_filename_part(
        scoped.get("scoped_signal_id")
        or _request_id(request)
        or acceptance.get("signal_acceptance_result_id")
    )
    resolved_root = _repo_path(root or BODY_SIGNAL_SCOPE_ROOT)
    path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not path.exists():
        return path
    for index in range(1, 1000):
        path = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not path.exists():
            return path
    raise BodySignalScopeError(
        "no bounded body-signal scope filename is available",
        "SIGNAL_SCOPE_REQUEST_MALFORMED",
    )


def write_body_signal_scope_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive body-signal scope JSON artifact."""

    if not isinstance(result, Mapping):
        raise BodySignalScopeError(
            "body-signal scope result must be a mapping",
            "SIGNAL_ACCEPTANCE_RESULT_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists() and output_path is not None:
        raise FileExistsError(f"body-signal scope result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
