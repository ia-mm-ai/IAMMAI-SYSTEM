"""Resolve one bounded derivative-vessel relation boundary.

This module implements the first executable derivative-vessel relation
boundary for the present execution line:

- one standing source/body basis
- one derivative vessel result or derivative vessel candidate result
- one derivative vessel relation declaration

It recognizes or blocks only the relation boundary. It does not implement a
vessel, create a registry, create adoption or public release standing, assign
currentness, create permission, replace source, or authorize follow-on vessel
relations.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class DerivativeVesselRelationBoundaryError(RuntimeError):
    """Raised for hard relation-boundary setup or parsing failures."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_source_body_basis: Mapping[str, Any] | None = None,
        selected_derivative_vessel_basis: Mapping[str, Any] | None = None,
        selected_relation_declaration: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_source_body_basis = dict(selected_source_body_basis or {})
        self.selected_derivative_vessel_basis = dict(selected_derivative_vessel_basis or {})
        self.selected_relation_declaration = copy.deepcopy(
            dict(selected_relation_declaration or {})
        )
        self.checks = [dict(check) for check in (checks or [])]


DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_derivative_vessel_relation_boundary"
)

RESOLVER_MODULE = "resolve_derivative_vessel_relation_boundary"
RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_DERIVATIVE_VESSEL_RELATION_BOUNDARY_RESULT"
)
RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "derivative_vessel_relation_boundary_result"

OUTCOME_RECOGNIZED = "DERIVATIVE_VESSEL_RELATION_RECOGNIZED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"

DECLARATION_SECTIONS = (
    "derivative_vessel_relation_metadata",
    "source_body_basis",
    "derivative_vessel_basis",
    "declared_relation_bounds",
    "hierarchy_constraints",
    "correspondence_requirements",
    "declared_non_claims",
)

DECLARATION_METADATA_FIELDS = (
    "derivative_vessel_relation_id",
    "derivative_vessel_relation_type",
    "derivative_vessel_relation_version",
    "declared_at",
    "declared_by_surface",
)

SOURCE_BODY_BASIS_FIELDS = (
    "self_orientation_result_path",
    "self_orientation_result_id",
    "self_orientation_outcome",
    "source_surface_path",
    "source_surface_id",
    "source_surface_family",
    "source_surface_outcome",
)

DERIVATIVE_VESSEL_BASIS_FIELDS = (
    "derivative_vessel_result_path",
    "derivative_vessel_result_id",
    "derivative_vessel_result_type",
    "derivative_vessel_result_outcome",
    "derivative_vessel_module",
    "derivative_output_family",
    "derivative_output_basis",
)

RELATION_BOUND_TRUE_FIELDS = (
    "relation_is_downstream",
    "source_basis_preserved",
    "derivative_output_preserved",
    "operator_facing_output_downstream_if_present",
    "relation_reversible",
    "relation_additive_only",
    "no_source_replacement",
    "no_authority_creation",
    "no_currentness_creation",
    "no_permission_creation",
    "no_adoption_creation",
    "no_privileged_standing",
    "no_final_governance_completion",
    "no_final_system_identity_completion",
)

RELATION_BOUND_BLOCK_CODES = {
    "relation_is_downstream": "RELATION_VAGUE_OR_UNBOUNDED",
    "source_basis_preserved": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
    "derivative_output_preserved": "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
    "operator_facing_output_downstream_if_present": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
    "relation_reversible": "RELATION_VAGUE_OR_UNBOUNDED",
    "relation_additive_only": "RELATION_VAGUE_OR_UNBOUNDED",
    "no_source_replacement": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
    "no_authority_creation": "RELATION_ATTEMPTS_AUTHORITY",
    "no_currentness_creation": "RELATION_ATTEMPTS_CURRENTNESS",
    "no_permission_creation": "RELATION_ATTEMPTS_PERMISSION",
    "no_adoption_creation": "RELATION_ATTEMPTS_ADOPTION",
    "no_privileged_standing": "RELATION_ATTEMPTS_PRIVILEGED_STANDING",
    "no_final_governance_completion": "RELATION_ATTEMPTS_FINAL_GOVERNANCE",
    "no_final_system_identity_completion": "RELATION_ATTEMPTS_FINAL_SYSTEM_IDENTITY",
}

HIERARCHY_FALSE_FIELDS = (
    "vessel_allowed_as_source",
    "vessel_allowed_as_authority",
    "vessel_allowed_as_currentness_source",
    "vessel_allowed_as_permission_source",
    "vessel_allowed_as_adoption_path",
    "vessel_allowed_as_public_release",
    "vessel_allowed_as_final_governance",
    "operator_surface_allowed_as_source",
    "derivative_output_allowed_to_replace_source",
    "latest_file_recency_allowed",
)

HIERARCHY_BLOCK_CODES = {
    "vessel_allowed_as_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
    "vessel_allowed_as_authority": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "vessel_allowed_as_currentness_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
    "vessel_allowed_as_permission_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION",
    "vessel_allowed_as_adoption_path": "RELATION_ATTEMPTS_ADOPTION",
    "vessel_allowed_as_public_release": "RELATION_ATTEMPTS_PUBLIC_RELEASE",
    "vessel_allowed_as_final_governance": "RELATION_ATTEMPTS_FINAL_GOVERNANCE",
    "operator_surface_allowed_as_source": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
    "derivative_output_allowed_to_replace_source": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
    "latest_file_recency_allowed": "LATEST_FILE_RECENCY_REFUSED",
}

CORRESPONDENCE_TRUE_FIELDS = (
    "must_preserve_source_identity",
    "must_preserve_source_outcome",
    "must_preserve_derivative_basis",
    "must_preserve_source_derivative_distinction",
    "must_preserve_operator_downstream_distinction",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

CORRESPONDENCE_BLOCK_CODES = {
    "must_preserve_source_identity": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
    "must_preserve_source_outcome": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
    "must_preserve_derivative_basis": "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
    "must_preserve_source_derivative_distinction": "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
    "must_preserve_operator_downstream_distinction": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
    "must_preserve_non_claims": "NON_CLAIM_MISSING_OR_FLIPPED",
    "must_prevent_over_mirroring": "RELATION_VAGUE_OR_UNBOUNDED",
    "must_prevent_under_mirroring": "RELATION_VAGUE_OR_UNBOUNDED",
}

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_create_permission",
    "does_not_create_currentness",
    "does_not_replace_source_surface",
    "does_not_upgrade_derivative_to_source",
    "does_not_upgrade_operator_to_source",
    "does_not_create_adoption",
    "does_not_create_privileged_standing",
    "does_not_complete_final_governance",
    "does_not_complete_final_system_identity",
    "does_not_complete_continuity",
    "does_not_create_public_release",
    "does_not_create_general_vessel_permission",
    "does_not_authorize_follow_on_vessels",
)

NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "source_replaced": False,
    "derivative_upgraded_to_source": False,
    "operator_upgraded_to_source": False,
    "adoption_created": False,
    "privileged_standing_created": False,
    "public_release_created": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "continuity_completed": False,
    "general_vessel_permission_created": False,
    "follow_on_vessels_authorized": False,
    "latest_file_currentness": False,
    "source_derivative_operator_collapsed": False,
}

SOURCE_BLOCKING_NON_CLAIMS = {
    "authority_created": "RELATION_ATTEMPTS_AUTHORITY",
    "permission_created": "RELATION_ATTEMPTS_PERMISSION",
    "currentness_created": "RELATION_ATTEMPTS_CURRENTNESS",
    "source_replaced": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
    "derivative_outputs_upgraded_to_source": "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
    "operator_outputs_upgraded_to_source": "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
    "latest_file_currentness": "LATEST_FILE_RECENCY_REFUSED",
    "recency_fraud": "LATEST_FILE_RECENCY_REFUSED",
}

DERIVATIVE_BLOCKING_NON_CLAIMS = {
    "source_replaced": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
    "derivative_upgraded_to_source": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
    "rank_assigned_by_model": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "authority_assigned_by_model": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "status_assigned_by_model": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
    "standing_assigned_by_model": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "provenance_assigned_by_model": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "source_scope_widened": "RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
    "continuity_completed": "RELATION_ATTEMPTS_CONTINUITY_COMPLETION",
    "authority_created": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "permission_created": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION",
    "currentness_created": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
    "standing_created": "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
    "adoption_created": "RELATION_ATTEMPTS_ADOPTION",
}

BLOCK_REASONS = {
    "SOURCE_BODY_BASIS_MISSING": "No source/body basis was supplied.",
    "SOURCE_BODY_BASIS_UNREADABLE": "The selected source/body basis could not be read.",
    "SOURCE_BODY_BASIS_MALFORMED": "The selected source/body basis is malformed.",
    "SOURCE_BODY_BASIS_NOT_STANDING": "The selected source/body basis does not stand.",
    "DERIVATIVE_VESSEL_RESULT_MISSING": "No derivative vessel result was supplied.",
    "DERIVATIVE_VESSEL_RESULT_UNREADABLE": (
        "The selected derivative vessel result could not be read."
    ),
    "DERIVATIVE_VESSEL_RESULT_MALFORMED": (
        "The selected derivative vessel result is malformed."
    ),
    "DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH": (
        "The derivative vessel result does not preserve the selected source/body basis."
    ),
    "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE": (
        "The derivative vessel output was treated as source."
    ),
    "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY": (
        "The derivative vessel output was treated as authority."
    ),
    "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS": (
        "The derivative vessel output was treated as currentness."
    ),
    "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION": (
        "The derivative vessel output was treated as permission."
    ),
    "OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE": (
        "An operator-facing output was treated as source."
    ),
    "RELATION_DECLARATION_MISSING": "No relation declaration was supplied.",
    "RELATION_DECLARATION_MALFORMED": "The relation declaration is malformed.",
    "RELATION_VAGUE_OR_UNBOUNDED": "The declared relation is vague or unbounded.",
    "RELATION_ATTEMPTS_SOURCE_REPLACEMENT": (
        "The relation attempts to replace the selected source."
    ),
    "RELATION_ATTEMPTS_AUTHORITY": "The relation attempts to create authority.",
    "RELATION_ATTEMPTS_CURRENTNESS": "The relation attempts to create currentness.",
    "RELATION_ATTEMPTS_PERMISSION": "The relation attempts to create permission.",
    "RELATION_ATTEMPTS_ADOPTION": "The relation attempts to create adoption.",
    "RELATION_ATTEMPTS_PRIVILEGED_STANDING": (
        "The relation attempts to create privileged standing."
    ),
    "RELATION_ATTEMPTS_PUBLIC_RELEASE": (
        "The relation attempts to create public release standing."
    ),
    "RELATION_ATTEMPTS_FINAL_GOVERNANCE": (
        "The relation attempts to complete final governance."
    ),
    "RELATION_ATTEMPTS_FINAL_SYSTEM_IDENTITY": (
        "The relation attempts to complete final system identity."
    ),
    "RELATION_ATTEMPTS_CONTINUITY_COMPLETION": (
        "The relation attempts to complete continuity."
    ),
    "RELATION_ATTEMPTS_GENERAL_VESSEL_PERMISSION": (
        "The relation attempts to create general vessel permission."
    ),
    "RELATION_ATTEMPTS_FOLLOW_ON_VESSEL_AUTHORIZATION": (
        "The relation attempts to authorize follow-on vessel relations."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required non-claim is missing or flipped."
    ),
    "LATEST_FILE_RECENCY_REFUSED": "Latest-file recency was used or allowed.",
    "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE": (
        "The source, derivative, or operator distinction collapsed."
    ),
}

VAGUE_RELATION_PATTERNS = (
    "apply wherever useful",
    "scope this generally",
    "relate generally",
    "use later",
    "whatever is useful",
    "anything useful",
    "unbounded",
    "body-wide relation",
    "general vessel relation",
)

RECENCY_PATTERNS = (
    "latest file",
    "newest file",
    "most recent file",
    "recency current",
    "recency-driven",
    "by recency",
)

COLLAPSE_PATTERNS = (
    "derivative as source",
    "derivative output as source",
    "operator as source",
    "operator-facing as source",
    "operator output as source",
    "vessel as source",
    "vessel output as authority",
    "vessel output as currentness",
    "vessel output as permission",
    "receipt as permission",
    "source replacement",
    "replace source",
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    try:
        resolved = _repo_path(path)
    except TypeError:
        return str(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def _string_or_none(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped or None


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        value = "no_selected_relation"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "no_selected_relation"


def _section(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _read_json_file(
    path: Path | str,
    *,
    context: str,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise DerivativeVesselRelationBoundaryError(
            f"{context} not found: {resolved}",
            unreadable_code,
        ) from exc
    except OSError as exc:
        raise DerivativeVesselRelationBoundaryError(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise DerivativeVesselRelationBoundaryError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise DerivativeVesselRelationBoundaryError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    base = BLOCK_REASONS.get(block_code, "The derivative vessel relation is blocked.")
    return f"{base} {detail}" if detail else base


def _check(
    name: str,
    passed: bool,
    *,
    expected: Any,
    actual: Any,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _clone(expected),
        "actual_posture": _clone(actual),
        "block_code": None if passed else block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _all_checks_passed(checks: Sequence[Any]) -> bool:
    return bool(checks) and all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def _required_strings_present(section: Mapping[str, Any], fields: Sequence[str]) -> bool:
    return all(_string_or_none(section.get(field)) is not None for field in fields)


def _path_equal(left: Any, right: Any) -> bool:
    left_s = _string_or_none(left)
    right_s = _string_or_none(right)
    if left_s is None or right_s is None:
        return False
    return _display_path(left_s) == _display_path(right_s)


def _match_if_both_present(left: Any, right: Any, *, path: bool = False) -> bool:
    left_s = _string_or_none(left)
    right_s = _string_or_none(right)
    if left_s is None or right_s is None:
        return True
    return _path_equal(left_s, right_s) if path else left_s == right_s


def _contains_any_text(value: Any, patterns: Sequence[str]) -> bool:
    text = json.dumps(value, sort_keys=True, default=str).lower()
    return any(pattern in text for pattern in patterns)


def _metadata_from_source_body_basis(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    for key in (
        "current_self_orientation_v5_metadata",
        "current_self_orientation_v4_metadata",
        "current_self_orientation_v3_metadata",
        "current_self_orientation_v2_metadata",
        "what_stands_now_metadata",
        "current_state_answer_read_metadata",
        "current_state_readout_metadata",
        "current_state_handoff_metadata",
        "current_state_export_metadata",
        "current_state_delivery_metadata",
        "current_state_application_metadata",
    ):
        value = artifact.get(key)
        if isinstance(value, Mapping):
            return value
    return {}


def _source_surface_from_source_body_basis(
    artifact: Mapping[str, Any],
) -> Mapping[str, Any]:
    selected = _section(artifact.get("selected_orientation_inputs"))
    for key in (
        "selected_source_surface",
        "selected_current_state_what_stands_now_result",
        "selected_current_state_answer_read_result",
        "selected_current_state_readout_result",
        "selected_current_state_handoff_result",
        "selected_current_state_export_result",
        "selected_current_state_delivery_result",
        "selected_current_state_application_result",
    ):
        value = selected.get(key)
        if isinstance(value, Mapping):
            return value
    selected_source = artifact.get("selected_source_surface")
    if isinstance(selected_source, Mapping):
        return selected_source
    return {}


def _source_identity_from_metadata(metadata: Mapping[str, Any]) -> dict[str, Any]:
    candidates = (
        ("self_orientation_result_id", "self_orientation_result_type", "self_orientation_result_version"),
        ("what_stands_now_result_id", "what_stands_now_result_type", "what_stands_now_result_version"),
        ("current_state_answer_read_result_id", "current_state_answer_read_result_type", "current_state_answer_read_result_version"),
        ("current_state_readout_result_id", "current_state_readout_result_type", "current_state_readout_result_version"),
        ("current_state_handoff_result_id", "current_state_handoff_result_type", "current_state_handoff_result_version"),
        ("current_state_export_result_id", "current_state_export_result_type", "current_state_export_result_version"),
        ("current_state_delivery_result_id", "current_state_delivery_result_type", "current_state_delivery_result_version"),
        ("current_state_application_result_id", "current_state_application_result_type", "current_state_application_result_version"),
    )
    for id_key, type_key, version_key in candidates:
        result_id = _string_or_none(metadata.get(id_key))
        if result_id is not None:
            return {
                "result_id": result_id,
                "result_type": _string_or_none(metadata.get(type_key)),
                "result_version": _string_or_none(metadata.get(version_key)),
            }
    return {"result_id": None, "result_type": None, "result_version": None}


def _source_surface_identity(surface: Mapping[str, Any]) -> dict[str, Any]:
    result_id = (
        _string_or_none(surface.get("result_id"))
        or _string_or_none(surface.get("selected_source_surface_id"))
        or _string_or_none(surface.get("source_surface_id"))
    )
    result_path = (
        _string_or_none(surface.get("result_path"))
        or _string_or_none(surface.get("selected_source_surface_path"))
        or _string_or_none(surface.get("source_surface_path"))
    )
    result_family = (
        _string_or_none(surface.get("result_family"))
        or _string_or_none(surface.get("selected_source_surface_family"))
        or _string_or_none(surface.get("source_surface_family"))
    )
    result_outcome = (
        _string_or_none(surface.get("outcome"))
        or _string_or_none(surface.get("result_outcome"))
        or _string_or_none(surface.get("selected_source_surface_outcome"))
        or _string_or_none(surface.get("source_surface_outcome"))
    )
    return {
        "source_surface_id": result_id,
        "source_surface_path": _display_path(result_path),
        "source_surface_family": result_family,
        "source_surface_outcome": result_outcome,
    }


def _current_governing_effective_references(artifact: Mapping[str, Any]) -> dict[str, Any]:
    selected = _section(artifact.get("selected_orientation_inputs"))
    effective = _section(selected.get("selected_effective_references"))
    recognized = _section(artifact.get("recognized_governing_effective_basis"))
    return {
        "selected_effective_references": _clone(effective),
        "recognized_governing_effective_basis": _clone(recognized),
    }


def _source_body_basis_stands(artifact: Mapping[str, Any]) -> bool:
    outcome = _string_or_none(artifact.get("outcome"))
    if outcome is None:
        return False
    if outcome == OUTCOME_SELF_ORIENTED:
        return True
    if outcome in {"BLOCKED", "REFUSED"}:
        return False
    return outcome.startswith("ANSWERED") or outcome.endswith("_CONFIRMED")


def _source_body_current_basis_is_upstream(artifact: Mapping[str, Any]) -> bool:
    basis = _section(artifact.get("recognized_governing_effective_basis"))
    forbidden_flags = (
        "derived_from_derivative_surface",
        "derived_from_operator_surface",
        "derived_from_reentry_surface",
        "derived_from_body_signal_surface",
        "derivative_surface_determines_current_basis",
        "operator_surface_determines_current_basis",
        "reentry_surface_determines_current_basis",
        "body_signal_surface_determines_current_basis",
        "signal_surface_became_current_or_governing_basis",
    )
    return not any(basis.get(flag) is True for flag in forbidden_flags)


def _source_body_identity(
    artifact: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_from_source_body_basis(artifact)
    base = _source_identity_from_metadata(metadata)
    surface = _source_surface_identity(_source_surface_from_source_body_basis(artifact))
    result_id = base["result_id"] or surface.get("source_surface_id")
    return {
        "selection_mode": selection_mode,
        "source_body_basis_id": result_id,
        "source_body_basis_path": _display_path(path),
        "source_body_basis_type": base["result_type"],
        "source_body_basis_version": base["result_version"],
        "source_body_basis_outcome": _string_or_none(artifact.get("outcome")),
        "resolver_module": _string_or_none(metadata.get("resolver_module")),
        "self_orientation_result_id": _string_or_none(
            metadata.get("self_orientation_result_id")
        ),
        "self_orientation_result_path": _display_path(path)
        if _string_or_none(metadata.get("self_orientation_result_id"))
        else None,
        "self_orientation_outcome": _string_or_none(artifact.get("outcome"))
        if _string_or_none(metadata.get("self_orientation_result_id"))
        else None,
        "source_surface_id": surface.get("source_surface_id"),
        "source_surface_path": surface.get("source_surface_path"),
        "source_surface_family": surface.get("source_surface_family"),
        "source_surface_outcome": surface.get("source_surface_outcome"),
        "source_body_basis_stands": _source_body_basis_stands(artifact),
        "source_body_basis_remains_upstream": _source_body_current_basis_is_upstream(
            artifact
        ),
        "current_governing_effective_references": _current_governing_effective_references(
            artifact
        ),
        "non_claims": _clone(_section(artifact.get("non_claims"))),
    }


def _metadata_from_derivative_result(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    for key in (
        "openai_api_derivative_vessel_v3_metadata",
        "openai_api_derivative_vessel_v2_metadata",
        "openai_api_derivative_vessel_metadata",
        "derivative_vessel_metadata",
    ):
        value = artifact.get(key)
        if isinstance(value, Mapping):
            return value
    return {}


def _derivative_result_identity_from_metadata(metadata: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "derivative_vessel_result_id": (
            _string_or_none(metadata.get("vessel_result_id"))
            or _string_or_none(metadata.get("derivative_vessel_result_id"))
        ),
        "derivative_vessel_result_type": (
            _string_or_none(metadata.get("vessel_result_type"))
            or _string_or_none(metadata.get("derivative_vessel_result_type"))
        ),
        "derivative_vessel_result_version": (
            _string_or_none(metadata.get("vessel_result_version"))
            or _string_or_none(metadata.get("derivative_vessel_result_version"))
        ),
        "derivative_vessel_module": _string_or_none(metadata.get("resolver_module")),
    }


def _derivative_output_family(result_type: str | None, artifact: Mapping[str, Any]) -> str | None:
    explicit = _string_or_none(artifact.get("derivative_output_family"))
    if explicit is not None:
        return explicit
    if result_type == "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT":
        return "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
    if result_type:
        compact = re.sub(r"[^A-Za-z0-9]+", "_", result_type.lower()).strip("_")
        return compact or None
    return None


def _derivative_output_basis(artifact: Mapping[str, Any]) -> Any:
    answer = _section(artifact.get("derivative_answer"))
    request = _section(artifact.get("vessel_request"))
    return (
        answer.get("answer_basis")
        or request.get("source_packet_basis")
        or request.get("derivative_output_basis")
        or artifact.get("derivative_output_basis")
    )


def _derivative_result_remains_derivative(artifact: Mapping[str, Any]) -> bool:
    answer = _section(artifact.get("derivative_answer"))
    explicit = answer.get("model_output_remains_derivative")
    if explicit is False:
        return False
    if explicit is True:
        return True
    result_type = _string_or_none(
        _metadata_from_derivative_result(artifact).get("vessel_result_type")
    )
    result_type = result_type or _string_or_none(
        _metadata_from_derivative_result(artifact).get("derivative_vessel_result_type")
    )
    if result_type and "DERIVATIVE_VESSEL" in result_type:
        return True
    return False


def _derivative_source_remains_source(artifact: Mapping[str, Any]) -> bool:
    answer = _section(artifact.get("derivative_answer"))
    if answer.get("source_remains_source") is False:
        return False
    selected = _source_surface_identity(_section(artifact.get("selected_source_surface")))
    return answer.get("source_remains_source") is True or selected.get(
        "source_surface_id"
    ) is not None


def _derivative_vessel_identity(
    artifact: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata_from_derivative_result(artifact)
    base = _derivative_result_identity_from_metadata(metadata)
    source = _source_surface_identity(_section(artifact.get("selected_source_surface")))
    output_family = _derivative_output_family(
        base.get("derivative_vessel_result_type"),
        artifact,
    )
    return {
        "selection_mode": selection_mode,
        "derivative_vessel_result_id": base.get("derivative_vessel_result_id"),
        "derivative_vessel_result_path": _display_path(path),
        "derivative_vessel_result_type": base.get("derivative_vessel_result_type"),
        "derivative_vessel_result_version": base.get("derivative_vessel_result_version"),
        "derivative_vessel_result_outcome": _string_or_none(artifact.get("outcome")),
        "derivative_vessel_module": base.get("derivative_vessel_module"),
        "derivative_output_family": output_family,
        "derivative_output_basis": _derivative_output_basis(artifact),
        "selected_source_surface_id": source.get("source_surface_id"),
        "selected_source_surface_path": source.get("source_surface_path"),
        "selected_source_surface_family": source.get("source_surface_family"),
        "selected_source_surface_outcome": source.get("source_surface_outcome"),
        "source_basis_preserved": _derivative_source_remains_source(artifact),
        "derivative_output_remains_derivative": _derivative_result_remains_derivative(
            artifact
        ),
        "operator_facing_output_remains_downstream": True,
        "non_claims": _clone(_section(artifact.get("non_claims"))),
    }


def _relation_metadata(
    declaration: Mapping[str, Any],
) -> Mapping[str, Any]:
    return _section(declaration.get("derivative_vessel_relation_metadata"))


def _relation_id(declaration: Mapping[str, Any]) -> str | None:
    return _string_or_none(
        _relation_metadata(declaration).get("derivative_vessel_relation_id")
    )


def _relation_type(declaration: Mapping[str, Any]) -> str | None:
    return _string_or_none(
        _relation_metadata(declaration).get("derivative_vessel_relation_type")
    )


def _required_false_fields_preserved(
    section: Mapping[str, Any],
    fields: Sequence[str],
) -> tuple[bool, str | None, dict[str, Any]]:
    actual = {field: section.get(field) for field in fields}
    for field in fields:
        if section.get(field) is not False:
            return False, field, actual
    return True, None, actual


def _required_true_fields_preserved(
    section: Mapping[str, Any],
    fields: Sequence[str],
) -> tuple[bool, str | None, dict[str, Any]]:
    actual = {field: section.get(field) for field in fields}
    for field in fields:
        if section.get(field) is not True:
            return False, field, actual
    return True, None, actual


def _first_true_non_claim(
    non_claims: Mapping[str, Any],
    block_map: Mapping[str, str],
) -> tuple[str | None, str | None]:
    for key, block_code in block_map.items():
        if non_claims.get(key) is True:
            return key, block_code
    return None, None


def _source_identity_preserved(
    declaration: Mapping[str, Any],
    source_identity: Mapping[str, Any],
) -> bool:
    declared = _section(declaration.get("source_body_basis"))
    return (
        _match_if_both_present(
            declared.get("self_orientation_result_id"),
            source_identity.get("self_orientation_result_id"),
        )
        and _match_if_both_present(
            declared.get("self_orientation_result_path"),
            source_identity.get("self_orientation_result_path"),
            path=True,
        )
        and _match_if_both_present(
            declared.get("self_orientation_outcome"),
            source_identity.get("self_orientation_outcome"),
        )
        and _match_if_both_present(
            declared.get("source_surface_id"),
            source_identity.get("source_surface_id"),
        )
        and _match_if_both_present(
            declared.get("source_surface_path"),
            source_identity.get("source_surface_path"),
            path=True,
        )
        and _match_if_both_present(
            declared.get("source_surface_family"),
            source_identity.get("source_surface_family"),
        )
        and _match_if_both_present(
            declared.get("source_surface_outcome"),
            source_identity.get("source_surface_outcome"),
        )
    )


def _source_outcome_preserved(
    declaration: Mapping[str, Any],
    source_identity: Mapping[str, Any],
) -> bool:
    declared = _section(declaration.get("source_body_basis"))
    return (
        _match_if_both_present(
            declared.get("self_orientation_outcome"),
            source_identity.get("self_orientation_outcome"),
        )
        and _match_if_both_present(
            declared.get("source_surface_outcome"),
            source_identity.get("source_surface_outcome"),
        )
    )


def _derivative_identity_preserved(
    declaration: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
) -> bool:
    declared = _section(declaration.get("derivative_vessel_basis"))
    return (
        _match_if_both_present(
            declared.get("derivative_vessel_result_id"),
            derivative_identity.get("derivative_vessel_result_id"),
        )
        and _match_if_both_present(
            declared.get("derivative_vessel_result_path"),
            derivative_identity.get("derivative_vessel_result_path"),
            path=True,
        )
        and _match_if_both_present(
            declared.get("derivative_vessel_result_type"),
            derivative_identity.get("derivative_vessel_result_type"),
        )
        and _match_if_both_present(
            declared.get("derivative_vessel_result_outcome"),
            derivative_identity.get("derivative_vessel_result_outcome"),
        )
        and _match_if_both_present(
            declared.get("derivative_vessel_module"),
            derivative_identity.get("derivative_vessel_module"),
        )
        and _match_if_both_present(
            declared.get("derivative_output_family"),
            derivative_identity.get("derivative_output_family"),
        )
        and _match_if_both_present(
            declared.get("derivative_output_basis"),
            derivative_identity.get("derivative_output_basis"),
        )
    )


def _derivative_basis_preserves_source(
    source_identity: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
) -> bool:
    return (
        derivative_identity.get("source_basis_preserved") is True
        and _match_if_both_present(
            derivative_identity.get("selected_source_surface_id"),
            source_identity.get("source_surface_id"),
        )
        and _match_if_both_present(
            derivative_identity.get("selected_source_surface_path"),
            source_identity.get("source_surface_path"),
            path=True,
        )
        and _match_if_both_present(
            derivative_identity.get("selected_source_surface_family"),
            source_identity.get("source_surface_family"),
        )
        and _match_if_both_present(
            derivative_identity.get("selected_source_surface_outcome"),
            source_identity.get("source_surface_outcome"),
        )
    )


def _declaration_well_formed(declaration: Mapping[str, Any]) -> bool:
    if not all(isinstance(declaration.get(section), Mapping) for section in DECLARATION_SECTIONS):
        return False
    return (
        _required_strings_present(
            _section(declaration.get("derivative_vessel_relation_metadata")),
            DECLARATION_METADATA_FIELDS,
        )
        and _required_strings_present(
            _section(declaration.get("source_body_basis")),
            SOURCE_BODY_BASIS_FIELDS,
        )
        and _required_strings_present(
            _section(declaration.get("derivative_vessel_basis")),
            DERIVATIVE_VESSEL_BASIS_FIELDS,
        )
    )


def _build_relation_checks(
    *,
    source_artifact: Mapping[str, Any],
    source_identity: Mapping[str, Any],
    derivative_artifact: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
    relation_declaration: Mapping[str, Any],
    source_readable: bool = True,
    derivative_readable: bool = True,
) -> list[dict[str, Any]]:
    declaration = relation_declaration
    metadata = _section(declaration.get("derivative_vessel_relation_metadata"))
    source_decl = _section(declaration.get("source_body_basis"))
    derivative_decl = _section(declaration.get("derivative_vessel_basis"))
    bounds = _section(declaration.get("declared_relation_bounds"))
    hierarchy = _section(declaration.get("hierarchy_constraints"))
    correspondence = _section(declaration.get("correspondence_requirements"))
    declared_non_claims = _section(declaration.get("declared_non_claims"))

    hierarchy_ok, failed_hierarchy, hierarchy_actual = _required_false_fields_preserved(
        hierarchy,
        HIERARCHY_FALSE_FIELDS,
    )
    correspondence_ok, failed_correspondence, correspondence_actual = (
        _required_true_fields_preserved(correspondence, CORRESPONDENCE_TRUE_FIELDS)
    )
    non_claims_ok, failed_non_claim, non_claims_actual = _required_true_fields_preserved(
        declared_non_claims,
        DECLARED_NON_CLAIM_FIELDS,
    )
    relation_bounds_ok, failed_relation_bound, relation_bounds_actual = (
        _required_true_fields_preserved(bounds, RELATION_BOUND_TRUE_FIELDS)
    )
    source_non_claim, source_non_claim_block = _first_true_non_claim(
        _section(source_artifact.get("non_claims")),
        SOURCE_BLOCKING_NON_CLAIMS,
    )
    derivative_non_claim, derivative_non_claim_block = _first_true_non_claim(
        _section(derivative_artifact.get("non_claims")),
        DERIVATIVE_BLOCKING_NON_CLAIMS,
    )

    checks = [
        _check(
            "source_body_basis_exists",
            bool(source_artifact),
            expected="one supplied source/body basis",
            actual=bool(source_artifact),
            block_code="SOURCE_BODY_BASIS_MISSING",
        ),
        _check(
            "source_body_basis_is_readable_if_path_based",
            source_readable,
            expected="source/body basis readable when path based",
            actual=source_readable,
            block_code="SOURCE_BODY_BASIS_UNREADABLE",
        ),
        _check(
            "source_body_basis_is_well_formed_enough",
            source_identity.get("source_body_basis_id") is not None
            and source_identity.get("source_body_basis_outcome") is not None,
            expected="source/body basis id and outcome preserved",
            actual=source_identity,
            block_code="SOURCE_BODY_BASIS_MALFORMED",
        ),
        _check(
            "source_body_basis_stands",
            source_identity.get("source_body_basis_stands") is True,
            expected="standing source/body basis",
            actual=source_identity.get("source_body_basis_outcome"),
            block_code="SOURCE_BODY_BASIS_NOT_STANDING",
        ),
        _check(
            "source_body_basis_remains_upstream",
            source_identity.get("source_body_basis_remains_upstream") is True,
            expected="current/governing basis remains upstream",
            actual=source_identity.get("source_body_basis_remains_upstream"),
            block_code="SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "source_body_basis_non_claims_remain_false_where_exposed",
            source_non_claim is None,
            expected="source/body basis creates no authority, permission, currentness, recency, or replacement",
            actual=source_non_claim,
            block_code=source_non_claim_block or "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "derivative_vessel_result_exists",
            bool(derivative_artifact),
            expected="one supplied derivative vessel result",
            actual=bool(derivative_artifact),
            block_code="DERIVATIVE_VESSEL_RESULT_MISSING",
        ),
        _check(
            "derivative_vessel_result_is_readable_if_path_based",
            derivative_readable,
            expected="derivative vessel result readable when path based",
            actual=derivative_readable,
            block_code="DERIVATIVE_VESSEL_RESULT_UNREADABLE",
        ),
        _check(
            "derivative_vessel_result_is_well_formed_enough",
            derivative_identity.get("derivative_vessel_result_id") is not None
            and derivative_identity.get("derivative_vessel_result_outcome") is not None,
            expected="derivative vessel result id and outcome preserved",
            actual=derivative_identity,
            block_code="DERIVATIVE_VESSEL_RESULT_MALFORMED",
        ),
        _check(
            "derivative_vessel_result_preserves_source_basis",
            _derivative_basis_preserves_source(source_identity, derivative_identity),
            expected=source_identity,
            actual=derivative_identity,
            block_code="DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        ),
        _check(
            "derivative_vessel_result_remains_derivative",
            derivative_identity.get("derivative_output_remains_derivative") is True,
            expected="derivative vessel output remains derivative",
            actual=derivative_identity.get("derivative_output_remains_derivative"),
            block_code="SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "derivative_vessel_result_does_not_become_source",
            derivative_non_claim != "source_replaced",
            expected="derivative vessel output is not source",
            actual=derivative_non_claim,
            block_code=derivative_non_claim_block or "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_SOURCE",
        ),
        _check(
            "derivative_vessel_result_does_not_become_authority",
            derivative_non_claim
            not in {
                "rank_assigned_by_model",
                "authority_assigned_by_model",
                "standing_assigned_by_model",
                "provenance_assigned_by_model",
                "authority_created",
                "standing_created",
            },
            expected="derivative vessel output assigns no authority, rank, status, standing, or provenance",
            actual=derivative_non_claim,
            block_code=derivative_non_claim_block
            or "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_AUTHORITY",
        ),
        _check(
            "derivative_vessel_result_does_not_become_currentness",
            derivative_non_claim not in {"status_assigned_by_model", "currentness_created"},
            expected="derivative vessel output assigns no currentness or status",
            actual=derivative_non_claim,
            block_code=derivative_non_claim_block
            or "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_CURRENTNESS",
        ),
        _check(
            "derivative_vessel_result_does_not_become_permission",
            derivative_non_claim != "permission_created",
            expected="derivative vessel output creates no permission",
            actual=derivative_non_claim,
            block_code=derivative_non_claim_block
            or "DERIVATIVE_VESSEL_OUTPUT_TREATED_AS_PERMISSION",
        ),
        _check(
            "operator_facing_output_remains_downstream_where_present",
            derivative_identity.get("operator_facing_output_remains_downstream") is True,
            expected="operator-facing output remains downstream where present",
            actual=derivative_identity.get("operator_facing_output_remains_downstream"),
            block_code="OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
        ),
        _check(
            "relation_declaration_exists",
            bool(declaration),
            expected="one supplied relation declaration",
            actual=bool(declaration),
            block_code="RELATION_DECLARATION_MISSING",
        ),
        _check(
            "relation_declaration_is_well_formed_enough",
            _declaration_well_formed(declaration),
            expected={
                "sections": DECLARATION_SECTIONS,
                "metadata_fields": DECLARATION_METADATA_FIELDS,
                "source_body_basis_fields": SOURCE_BODY_BASIS_FIELDS,
                "derivative_vessel_basis_fields": DERIVATIVE_VESSEL_BASIS_FIELDS,
            },
            actual={
                "sections": [key for key in DECLARATION_SECTIONS if isinstance(declaration.get(key), Mapping)],
                "metadata": _clone(metadata),
                "source_body_basis": _clone(source_decl),
                "derivative_vessel_basis": _clone(derivative_decl),
            },
            block_code="RELATION_DECLARATION_MALFORMED",
        ),
        _check(
            "source_identity_is_preserved",
            _source_identity_preserved(declaration, source_identity),
            expected=source_identity,
            actual=source_decl,
            block_code="DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        ),
        _check(
            "source_outcome_is_preserved",
            _source_outcome_preserved(declaration, source_identity),
            expected={
                "self_orientation_outcome": source_identity.get("self_orientation_outcome"),
                "source_surface_outcome": source_identity.get("source_surface_outcome"),
            },
            actual=source_decl,
            block_code="DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        ),
        _check(
            "derivative_basis_is_preserved",
            _derivative_identity_preserved(declaration, derivative_identity),
            expected=derivative_identity,
            actual=derivative_decl,
            block_code="DERIVATIVE_VESSEL_RESULT_SOURCE_BASIS_MISMATCH",
        ),
        _check(
            "source_derivative_distinction_is_preserved",
            correspondence.get("must_preserve_source_derivative_distinction") is True,
            expected="source remains source and derivative remains derivative",
            actual={
                "must_preserve_source_derivative_distinction": correspondence.get(
                    "must_preserve_source_derivative_distinction"
                ),
            },
            block_code="SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "operator_downstream_distinction_is_preserved",
            correspondence.get("must_preserve_operator_downstream_distinction") is True
            and hierarchy.get("operator_surface_allowed_as_source") is False,
            expected="operator-facing output remains downstream",
            actual={
                "must_preserve_operator_downstream_distinction": correspondence.get(
                    "must_preserve_operator_downstream_distinction"
                ),
                "operator_surface_allowed_as_source": hierarchy.get(
                    "operator_surface_allowed_as_source"
                ),
            },
            block_code="OPERATOR_FACING_OUTPUT_TREATED_AS_SOURCE",
        ),
        _check(
            "relation_bounds_are_explicit_and_bounded",
            relation_bounds_ok
            and not _contains_any_text(declaration, VAGUE_RELATION_PATTERNS),
            expected={field: True for field in RELATION_BOUND_TRUE_FIELDS},
            actual=relation_bounds_actual,
            block_code=RELATION_BOUND_BLOCK_CODES.get(
                failed_relation_bound or "",
                "RELATION_VAGUE_OR_UNBOUNDED",
            ),
        ),
        _check(
            "relation_is_downstream",
            bounds.get("relation_is_downstream") is True,
            expected=True,
            actual=bounds.get("relation_is_downstream"),
            block_code="RELATION_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "relation_is_additive_only",
            bounds.get("relation_additive_only") is True,
            expected=True,
            actual=bounds.get("relation_additive_only"),
            block_code="RELATION_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "relation_is_reversible_or_non_standing_by_default",
            bounds.get("relation_reversible") is True,
            expected=True,
            actual=bounds.get("relation_reversible"),
            block_code="RELATION_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "relation_does_not_create_authority",
            bounds.get("no_authority_creation") is True,
            expected=True,
            actual=bounds.get("no_authority_creation"),
            block_code="RELATION_ATTEMPTS_AUTHORITY",
        ),
        _check(
            "relation_does_not_create_permission",
            bounds.get("no_permission_creation") is True,
            expected=True,
            actual=bounds.get("no_permission_creation"),
            block_code="RELATION_ATTEMPTS_PERMISSION",
        ),
        _check(
            "relation_does_not_create_currentness",
            bounds.get("no_currentness_creation") is True,
            expected=True,
            actual=bounds.get("no_currentness_creation"),
            block_code="RELATION_ATTEMPTS_CURRENTNESS",
        ),
        _check(
            "relation_does_not_create_adoption",
            bounds.get("no_adoption_creation") is True,
            expected=True,
            actual=bounds.get("no_adoption_creation"),
            block_code="RELATION_ATTEMPTS_ADOPTION",
        ),
        _check(
            "relation_does_not_create_privileged_standing",
            bounds.get("no_privileged_standing") is True,
            expected=True,
            actual=bounds.get("no_privileged_standing"),
            block_code="RELATION_ATTEMPTS_PRIVILEGED_STANDING",
        ),
        _check(
            "relation_does_not_create_public_release",
            hierarchy.get("vessel_allowed_as_public_release") is False,
            expected=False,
            actual=hierarchy.get("vessel_allowed_as_public_release"),
            block_code="RELATION_ATTEMPTS_PUBLIC_RELEASE",
        ),
        _check(
            "relation_does_not_replace_source",
            bounds.get("no_source_replacement") is True
            and hierarchy.get("derivative_output_allowed_to_replace_source") is False,
            expected="source replacement refused",
            actual={
                "no_source_replacement": bounds.get("no_source_replacement"),
                "derivative_output_allowed_to_replace_source": hierarchy.get(
                    "derivative_output_allowed_to_replace_source"
                ),
            },
            block_code="RELATION_ATTEMPTS_SOURCE_REPLACEMENT",
        ),
        _check(
            "relation_does_not_complete_final_governance",
            bounds.get("no_final_governance_completion") is True,
            expected=True,
            actual=bounds.get("no_final_governance_completion"),
            block_code="RELATION_ATTEMPTS_FINAL_GOVERNANCE",
        ),
        _check(
            "relation_does_not_complete_final_system_identity",
            bounds.get("no_final_system_identity_completion") is True,
            expected=True,
            actual=bounds.get("no_final_system_identity_completion"),
            block_code="RELATION_ATTEMPTS_FINAL_SYSTEM_IDENTITY",
        ),
        _check(
            "relation_does_not_complete_continuity",
            declared_non_claims.get("does_not_complete_continuity") is True,
            expected=True,
            actual=declared_non_claims.get("does_not_complete_continuity"),
            block_code="RELATION_ATTEMPTS_CONTINUITY_COMPLETION",
        ),
        _check(
            "relation_does_not_create_general_vessel_permission",
            declared_non_claims.get("does_not_create_general_vessel_permission") is True,
            expected=True,
            actual=declared_non_claims.get("does_not_create_general_vessel_permission"),
            block_code="RELATION_ATTEMPTS_GENERAL_VESSEL_PERMISSION",
        ),
        _check(
            "relation_does_not_authorize_follow_on_vessel_relations",
            declared_non_claims.get("does_not_authorize_follow_on_vessels") is True,
            expected=True,
            actual=declared_non_claims.get("does_not_authorize_follow_on_vessels"),
            block_code="RELATION_ATTEMPTS_FOLLOW_ON_VESSEL_AUTHORIZATION",
        ),
        _check(
            "hierarchy_constraints_are_preserved",
            hierarchy_ok,
            expected={field: False for field in HIERARCHY_FALSE_FIELDS},
            actual=hierarchy_actual,
            block_code=HIERARCHY_BLOCK_CODES.get(
                failed_hierarchy or "",
                "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
            ),
        ),
        _check(
            "correspondence_requirements_are_preserved",
            correspondence_ok,
            expected={field: True for field in CORRESPONDENCE_TRUE_FIELDS},
            actual=correspondence_actual,
            block_code=CORRESPONDENCE_BLOCK_CODES.get(
                failed_correspondence or "",
                "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
            ),
        ),
        _check(
            "declared_non_claims_are_preserved",
            non_claims_ok,
            expected={field: True for field in DECLARED_NON_CLAIM_FIELDS},
            actual=non_claims_actual,
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "latest_file_recency_is_refused",
            hierarchy.get("latest_file_recency_allowed") is False
            and not _contains_any_text(declaration, RECENCY_PATTERNS),
            expected="latest-file recency refused",
            actual={
                "latest_file_recency_allowed": hierarchy.get(
                    "latest_file_recency_allowed"
                ),
                "recency_language_present": _contains_any_text(
                    declaration,
                    RECENCY_PATTERNS,
                ),
            },
            block_code="LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "source_derivative_operator_collapse_is_refused",
            not _contains_any_text(declaration, COLLAPSE_PATTERNS),
            expected="source/derivative/operator collapse refused",
            actual={
                "collapse_language_present": _contains_any_text(
                    declaration,
                    COLLAPSE_PATTERNS,
                )
            },
            block_code="SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
    ]
    return checks


def _empty_selected_source_body_basis() -> dict[str, Any]:
    return {
        "selection_mode": None,
        "source_body_basis_id": None,
        "source_body_basis_path": None,
        "source_body_basis_type": None,
        "source_body_basis_version": None,
        "source_body_basis_outcome": None,
        "resolver_module": None,
        "self_orientation_result_id": None,
        "self_orientation_result_path": None,
        "self_orientation_outcome": None,
        "source_surface_id": None,
        "source_surface_path": None,
        "source_surface_family": None,
        "source_surface_outcome": None,
        "source_body_basis_stands": False,
        "source_body_basis_remains_upstream": False,
        "current_governing_effective_references": {},
        "non_claims": {},
    }


def _empty_selected_derivative_vessel_basis() -> dict[str, Any]:
    return {
        "selection_mode": None,
        "derivative_vessel_result_id": None,
        "derivative_vessel_result_path": None,
        "derivative_vessel_result_type": None,
        "derivative_vessel_result_version": None,
        "derivative_vessel_result_outcome": None,
        "derivative_vessel_module": None,
        "derivative_output_family": None,
        "derivative_output_basis": None,
        "selected_source_surface_id": None,
        "selected_source_surface_path": None,
        "selected_source_surface_family": None,
        "selected_source_surface_outcome": None,
        "source_basis_preserved": False,
        "derivative_output_remains_derivative": False,
        "operator_facing_output_remains_downstream": False,
        "non_claims": {},
    }


def _metadata(
    relation_declaration: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    relation_id = _relation_id(relation_declaration)
    derivative_id = _string_or_none(derivative_identity.get("derivative_vessel_result_id"))
    base = relation_id or derivative_id or "no_selected_relation"
    suffix = (
        "derivative_vessel_relation_recognized"
        if outcome == OUTCOME_RECOGNIZED
        else "derivative_vessel_relation_blocked"
    )
    return {
        "derivative_vessel_relation_boundary_result_id": (
            f"{base}__{suffix}"
        ),
        "derivative_vessel_relation_boundary_result_type": RESULT_TYPE,
        "derivative_vessel_relation_boundary_result_version": RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _recognized_relation(
    *,
    source_identity: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
    relation_declaration: Mapping[str, Any],
) -> dict[str, Any]:
    metadata = _relation_metadata(relation_declaration)
    return {
        "source_body_basis_id": source_identity.get("source_body_basis_id"),
        "source_body_basis_path": source_identity.get("source_body_basis_path"),
        "source_body_basis_outcome": source_identity.get("source_body_basis_outcome"),
        "source_surface_id": source_identity.get("source_surface_id"),
        "source_surface_path": source_identity.get("source_surface_path"),
        "source_surface_family": source_identity.get("source_surface_family"),
        "source_surface_outcome": source_identity.get("source_surface_outcome"),
        "derivative_vessel_result_id": derivative_identity.get(
            "derivative_vessel_result_id"
        ),
        "derivative_vessel_result_path": derivative_identity.get(
            "derivative_vessel_result_path"
        ),
        "derivative_vessel_result_outcome": derivative_identity.get(
            "derivative_vessel_result_outcome"
        ),
        "derivative_output_family": derivative_identity.get("derivative_output_family"),
        "derivative_output_basis": derivative_identity.get("derivative_output_basis"),
        "relation_id": metadata.get("derivative_vessel_relation_id"),
        "relation_type": metadata.get("derivative_vessel_relation_type"),
        "downstream": True,
        "additive_only": True,
        "reversible_or_non_standing_by_default": True,
        "source_preserved": True,
        "derivative_preserved": True,
        "operator_downstream_where_present": True,
        "no_authority": True,
        "no_permission": True,
        "no_currentness": True,
        "no_adoption": True,
        "no_privileged_standing": True,
        "no_public_release": True,
        "no_source_replacement": True,
        "no_final_governance": True,
        "no_final_system_identity": True,
        "no_continuity_completion": True,
        "no_follow_on_vessel_authorization": True,
    }


def _boundary_basis(
    *,
    source_identity: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
    relation_declaration: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    return {
        "basis_kind": "bounded_derivative_vessel_relation_boundary",
        "outcome": outcome,
        "selected_source_body_basis_id": source_identity.get("source_body_basis_id"),
        "selected_source_body_basis_path": source_identity.get("source_body_basis_path"),
        "selected_derivative_vessel_result_id": derivative_identity.get(
            "derivative_vessel_result_id"
        ),
        "selected_derivative_vessel_result_path": derivative_identity.get(
            "derivative_vessel_result_path"
        ),
        "relation_id": _relation_id(relation_declaration),
        "relation_type": _relation_type(relation_declaration),
        "source_body_basis_remains_upstream": True,
        "derivative_vessel_output_remains_downstream": True,
        "operator_facing_output_remains_downstream_where_present": True,
        "relation_recognition_creates_authority": False,
        "relation_recognition_creates_permission": False,
        "relation_recognition_creates_currentness": False,
        "relation_recognition_creates_adoption": False,
        "relation_recognition_creates_privileged_standing": False,
        "relation_recognition_replaces_source": False,
        "relation_recognition_completes_final_governance": False,
        "relation_recognition_completes_final_system_identity": False,
        "relation_recognition_completes_continuity": False,
        "relation_recognition_authorizes_follow_on_vessels": False,
    }


def _build_result(
    *,
    source_identity: Mapping[str, Any],
    derivative_identity: Mapping[str, Any],
    relation_declaration: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    recognized_relation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    result = {
        "derivative_vessel_relation_boundary_metadata": _metadata(
            relation_declaration,
            derivative_identity,
            outcome,
        ),
        "selected_source_body_basis": _clone(dict(source_identity)),
        "selected_derivative_vessel_basis": _clone(dict(derivative_identity)),
        "selected_relation_declaration": _clone(dict(relation_declaration)),
        "relation_boundary_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "recognized_derivative_vessel_relation": (
            _clone(dict(recognized_relation)) if recognized_relation else None
        ),
        "derivative_vessel_relation_boundary_basis": _boundary_basis(
            source_identity=source_identity,
            derivative_identity=derivative_identity,
            relation_declaration=relation_declaration,
            outcome=outcome,
        ),
        "derivative_vessel_relation_boundary_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["derivative_vessel_relation_boundary_summary"] = (
        build_derivative_vessel_relation_boundary_summary(result)
    )
    return result


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    source_identity: Mapping[str, Any] | None = None,
    derivative_identity: Mapping[str, Any] | None = None,
    relation_declaration: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    return _build_result(
        source_identity=source_identity or _empty_selected_source_body_basis(),
        derivative_identity=derivative_identity or _empty_selected_derivative_vessel_basis(),
        relation_declaration=relation_declaration or {},
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        recognized_relation=None,
    )


def _resolve(
    *,
    source_body_basis: Mapping[str, Any] | None,
    derivative_vessel_result: Mapping[str, Any] | None,
    relation_declaration: Mapping[str, Any] | None,
    source_body_basis_path: Path | str | None = None,
    derivative_vessel_result_path: Path | str | None = None,
) -> dict[str, Any]:
    if source_body_basis is None:
        return _blocked_result(
            block_code="SOURCE_BODY_BASIS_MISSING",
            relation_declaration=relation_declaration if isinstance(relation_declaration, Mapping) else {},
            checks=[
                _check(
                    "source_body_basis_exists",
                    False,
                    expected="one supplied source/body basis",
                    actual=None,
                    block_code="SOURCE_BODY_BASIS_MISSING",
                )
            ],
        )
    if not isinstance(source_body_basis, Mapping):
        return _blocked_result(
            block_code="SOURCE_BODY_BASIS_MALFORMED",
            relation_declaration=relation_declaration if isinstance(relation_declaration, Mapping) else {},
            checks=[
                _check(
                    "source_body_basis_is_well_formed_enough",
                    False,
                    expected="source/body basis JSON object",
                    actual=type(source_body_basis).__name__,
                    block_code="SOURCE_BODY_BASIS_MALFORMED",
                )
            ],
        )
    source_identity = _source_body_identity(
        source_body_basis,
        source_body_basis_path,
        "path_supplied_source_body_basis"
        if source_body_basis_path is not None
        else "mapping_supplied_source_body_basis",
    )

    if derivative_vessel_result is None:
        return _blocked_result(
            block_code="DERIVATIVE_VESSEL_RESULT_MISSING",
            source_identity=source_identity,
            relation_declaration=relation_declaration if isinstance(relation_declaration, Mapping) else {},
            checks=[
                _check(
                    "derivative_vessel_result_exists",
                    False,
                    expected="one supplied derivative vessel result",
                    actual=None,
                    block_code="DERIVATIVE_VESSEL_RESULT_MISSING",
                )
            ],
        )
    if not isinstance(derivative_vessel_result, Mapping):
        return _blocked_result(
            block_code="DERIVATIVE_VESSEL_RESULT_MALFORMED",
            source_identity=source_identity,
            relation_declaration=relation_declaration if isinstance(relation_declaration, Mapping) else {},
            checks=[
                _check(
                    "derivative_vessel_result_is_well_formed_enough",
                    False,
                    expected="derivative vessel result JSON object",
                    actual=type(derivative_vessel_result).__name__,
                    block_code="DERIVATIVE_VESSEL_RESULT_MALFORMED",
                )
            ],
        )
    derivative_identity = _derivative_vessel_identity(
        derivative_vessel_result,
        derivative_vessel_result_path,
        "path_supplied_derivative_vessel_result"
        if derivative_vessel_result_path is not None
        else "mapping_supplied_derivative_vessel_result",
    )

    if relation_declaration is None:
        return _blocked_result(
            block_code="RELATION_DECLARATION_MISSING",
            source_identity=source_identity,
            derivative_identity=derivative_identity,
            checks=[
                _check(
                    "relation_declaration_exists",
                    False,
                    expected="one supplied relation declaration",
                    actual=None,
                    block_code="RELATION_DECLARATION_MISSING",
                )
            ],
        )
    if not isinstance(relation_declaration, Mapping):
        return _blocked_result(
            block_code="RELATION_DECLARATION_MALFORMED",
            source_identity=source_identity,
            derivative_identity=derivative_identity,
            checks=[
                _check(
                    "relation_declaration_is_well_formed_enough",
                    False,
                    expected="relation declaration JSON object",
                    actual=type(relation_declaration).__name__,
                    block_code="RELATION_DECLARATION_MALFORMED",
                )
            ],
        )

    source_copy = copy.deepcopy(dict(source_body_basis))
    derivative_copy = copy.deepcopy(dict(derivative_vessel_result))
    declaration_copy = copy.deepcopy(dict(relation_declaration))
    checks = _build_relation_checks(
        source_artifact=source_copy,
        source_identity=source_identity,
        derivative_artifact=derivative_copy,
        derivative_identity=derivative_identity,
        relation_declaration=declaration_copy,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            block_code=_string_or_none(failed.get("block_code"))
            or "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
            block_detail=f"failed check: {failed.get('check_name')}",
            source_identity=source_identity,
            derivative_identity=derivative_identity,
            relation_declaration=declaration_copy,
            checks=checks,
        )

    recognized = _recognized_relation(
        source_identity=source_identity,
        derivative_identity=derivative_identity,
        relation_declaration=declaration_copy,
    )
    return _build_result(
        source_identity=source_identity,
        derivative_identity=derivative_identity,
        relation_declaration=declaration_copy,
        checks=checks,
        outcome=OUTCOME_RECOGNIZED,
        block_code=None,
        block_detail=None,
        recognized_relation=recognized,
    )


def resolve_derivative_vessel_relation_boundary(
    source_body_basis: Mapping[str, Any] | None = None,
    derivative_vessel_result: Mapping[str, Any] | None = None,
    relation_declaration: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Evaluate one source/body basis, one vessel result, and one declaration."""

    try:
        return _resolve(
            source_body_basis=source_body_basis,
            derivative_vessel_result=derivative_vessel_result,
            relation_declaration=relation_declaration,
        )
    except DerivativeVesselRelationBoundaryError as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            source_identity=exc.selected_source_body_basis,
            derivative_identity=exc.selected_derivative_vessel_basis,
            relation_declaration=exc.selected_relation_declaration,
            checks=exc.checks,
        )


def resolve_derivative_vessel_relation_boundary_from_paths(
    source_body_basis_path: Path | str,
    derivative_vessel_result_path: Path | str,
    relation_declaration: Mapping[str, Any],
) -> dict[str, Any]:
    """Read two JSON artifacts by path and evaluate one relation declaration."""

    try:
        source_body_basis = _read_json_file(
            source_body_basis_path,
            context="source/body basis",
            unreadable_code="SOURCE_BODY_BASIS_UNREADABLE",
            malformed_code="SOURCE_BODY_BASIS_MALFORMED",
        )
    except DerivativeVesselRelationBoundaryError as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            relation_declaration=relation_declaration
            if isinstance(relation_declaration, Mapping)
            else {},
            checks=[
                _check(
                    "source_body_basis_is_readable_if_path_based",
                    False,
                    expected="source/body basis readable when path based",
                    actual=_display_path(source_body_basis_path),
                    block_code=exc.block_code,
                )
            ],
        )

    source_identity = _source_body_identity(
        source_body_basis,
        source_body_basis_path,
        "path_supplied_source_body_basis",
    )

    try:
        derivative_vessel_result = _read_json_file(
            derivative_vessel_result_path,
            context="derivative vessel result",
            unreadable_code="DERIVATIVE_VESSEL_RESULT_UNREADABLE",
            malformed_code="DERIVATIVE_VESSEL_RESULT_MALFORMED",
        )
    except DerivativeVesselRelationBoundaryError as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            source_identity=source_identity,
            relation_declaration=relation_declaration
            if isinstance(relation_declaration, Mapping)
            else {},
            checks=[
                _check(
                    "derivative_vessel_result_is_readable_if_path_based",
                    False,
                    expected="derivative vessel result readable when path based",
                    actual=_display_path(derivative_vessel_result_path),
                    block_code=exc.block_code,
                )
            ],
        )

    return _resolve(
        source_body_basis=source_body_basis,
        derivative_vessel_result=derivative_vessel_result,
        relation_declaration=relation_declaration,
        source_body_basis_path=source_body_basis_path,
        derivative_vessel_result_path=derivative_vessel_result_path,
    )


def _count_passed(checks: Sequence[Any]) -> int:
    return sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
    )


def _count_failed(checks: Sequence[Any]) -> int:
    return sum(
        1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True
    )


def _check_passed(checks: Sequence[Any], name: str) -> bool:
    return any(
        isinstance(check, Mapping)
        and check.get("check_name") == name
        and check.get("passed") is True
        for check in checks
    )


def build_derivative_vessel_relation_boundary_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a bounded summary over one derivative-vessel relation result."""

    if not isinstance(result, Mapping):
        raise DerivativeVesselRelationBoundaryError(
            "derivative vessel relation boundary result must be an object",
            "RELATION_DECLARATION_MALFORMED",
        )
    source = _section(result.get("selected_source_body_basis"))
    derivative = _section(result.get("selected_derivative_vessel_basis"))
    declaration = _section(result.get("selected_relation_declaration"))
    block = _section(result.get("block"))
    checks = result.get("relation_boundary_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = _section(result.get("non_claims"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_source_body_basis_id": source.get("source_body_basis_id"),
        "selected_source_body_basis_path": source.get("source_body_basis_path"),
        "selected_source_body_basis_outcome": source.get("source_body_basis_outcome"),
        "selected_source_surface_id": source.get("source_surface_id"),
        "selected_source_surface_path": source.get("source_surface_path"),
        "selected_source_surface_outcome": source.get("source_surface_outcome"),
        "selected_derivative_vessel_result_id": derivative.get(
            "derivative_vessel_result_id"
        ),
        "selected_derivative_vessel_result_path": derivative.get(
            "derivative_vessel_result_path"
        ),
        "selected_derivative_vessel_result_outcome": derivative.get(
            "derivative_vessel_result_outcome"
        ),
        "relation_id": _relation_id(declaration),
        "relation_type": _relation_type(declaration),
        "passed_check_count": _count_passed(checks),
        "failed_check_count": _count_failed(checks),
        "source_body_basis_passed": _check_passed(
            checks,
            "source_body_basis_stands",
        )
        and _check_passed(checks, "source_body_basis_remains_upstream"),
        "derivative_vessel_basis_passed": _check_passed(
            checks,
            "derivative_vessel_result_preserves_source_basis",
        )
        and _check_passed(checks, "derivative_vessel_result_remains_derivative"),
        "relation_bounds_passed": _check_passed(
            checks,
            "relation_bounds_are_explicit_and_bounded",
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
                "source_replaced",
                "derivative_upgraded_to_source",
                "operator_upgraded_to_source",
                "adoption_created",
                "privileged_standing_created",
                "public_release_created",
                "final_governance_completed",
                "final_system_identity_completed",
                "continuity_completed",
                "general_vessel_permission_created",
                "follow_on_vessels_authorized",
                "latest_file_currentness",
                "source_derivative_operator_collapsed",
            )
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT,
) -> Path:
    declaration = _section(result.get("selected_relation_declaration"))
    derivative = _section(result.get("selected_derivative_vessel_basis"))
    stem = _safe_filename_part(
        _relation_id(declaration) or derivative.get("derivative_vessel_result_id")
    )
    resolved_root = _repo_path(root)
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise DerivativeVesselRelationBoundaryError(
        "no bounded derivative vessel relation boundary filename is available",
        "RELATION_DECLARATION_MALFORMED",
    )


def write_derivative_vessel_relation_boundary_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive derivative-vessel relation boundary result."""

    if not isinstance(result, Mapping):
        raise DerivativeVesselRelationBoundaryError(
            "derivative vessel relation boundary result must be an object",
            "RELATION_DECLARATION_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"derivative vessel relation boundary result already exists: {target}"
        )
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
