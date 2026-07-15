"""Resolve one bounded current self-orientation re-entry admissibility gate.

This module decides whether one declared next relation, touch, or work step may
enter through one standing SELF_ORIENTED result without turning that
self-orientation result into authority.

It is a single-step admission/refusal surface. It does not generate the next
task, choose a roadmap, replay the host, merge preserved runs, mutate upstream
artifacts, or authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentSelfOrientationReentryAdmissibilityError(RuntimeError):
    """Raised for malformed inputs or impossible re-entry correspondence."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


SELF_ORIENTATION_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v2"
)
CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)

RESOLVER_MODULE = "resolve_current_self_orientation_reentry_admissibility"
REENTRY_ADMISSIBILITY_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_"
    "REENTRY_ADMISSIBILITY_RESULT"
)
REENTRY_ADMISSIBILITY_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "reentry_admissibility_result"

SELF_ORIENTATION_V2_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V2_RESULT"
)
SELF_ORIENTATION_V2_RESOLVER_MODULE = "resolve_current_self_orientation_v2"

OUTCOME_REENTRY_ADMITTED = "REENTRY_ADMITTED"
OUTCOME_BLOCKED = "BLOCKED"
SELF_ORIENTATION_OUTCOME = "SELF_ORIENTED"

ALLOWED_NEXT_STEP_FAMILIES = frozenset(
    {
        "SPEC_BOUNDARY",
        "RESOLVER_IMPLEMENTATION",
        "TEST_SURFACE",
        "ARTIFACT_EXECUTION",
        "DERIVATIVE_READ",
        "OPERATOR_FACING_DERIVATIVE",
        "CONTINUITY_TOUCH",
    }
)

REQUIRED_SELF_ORIENTATION_TOP_LEVEL_KEYS = frozenset(
    {
        "current_self_orientation_v2_metadata",
        "selected_orientation_inputs",
        "recognized_current_executable_core_line",
        "recognized_governing_effective_basis",
        "recognized_current_state_surfaces",
        "recognized_continuity_surfaces",
        "recognized_derivative_surfaces",
        "recognized_operator_facing_surfaces",
        "recognized_open_surfaces",
        "recognized_blocked_or_refused_surfaces",
        "recognized_touch_admissibility_surfaces",
        "bounded_correspondence_checks",
        "outcome",
        "block",
        "self_orientation_basis",
        "current_self_orientation_summary",
        "non_claims",
    }
)

REQUEST_SECTIONS = (
    "reentry_request_metadata",
    "self_orientation_basis",
    "locked_orientation_basis",
    "declared_next_step",
    "declared_scope_bounds",
    "hierarchy_constraints",
    "correspondence_requirements",
    "requested_permissions",
    "declared_non_claims",
    "refusal_acknowledgement",
)

REQUEST_STRING_FIELDS = {
    "reentry_request_metadata": (
        "reentry_request_id",
        "reentry_request_type",
        "reentry_request_version",
        "declared_at",
        "declared_by_surface",
    ),
    "self_orientation_basis": (
        "self_orientation_result_path",
        "self_orientation_result_id",
        "self_orientation_result_version",
        "self_orientation_outcome",
        "self_orientation_resolver_module",
    ),
    "locked_orientation_basis": (
        "selected_body_pass_result_id",
        "selected_body_pass_result_path",
        "selected_source_surface_id",
        "selected_source_surface_path",
        "selected_current_state_answer_read_id",
        "selected_current_state_answer_read_path",
        "selected_what_stands_now_id",
        "selected_what_stands_now_path",
        "effective_authority_artifact_path",
        "effective_family_packet_path",
        "effective_status_packet_path",
        "effective_current_governing_packet_path",
        "effective_source_run_path",
        "effective_ingress_run_path",
    ),
    "declared_next_step": (
        "next_step_family",
        "next_step_kind",
        "target_surface_family",
        "target_surface_path",
        "target_surface_id",
        "declared_purpose",
        "declared_expected_output_family",
        "requested_relation_to_basis",
    ),
    "hierarchy_constraints": (
        "current_governing_basis_source",
    ),
    "requested_permissions": (
        "authorization_scope",
    ),
}

SCOPE_LIST_FIELDS = (
    "allowed_new_file_paths",
    "allowed_artifact_output_roots",
    "allowed_read_surfaces",
    "forbidden_read_surfaces",
    "forbidden_write_surfaces",
)

SCOPE_BOOL_FIELDS = (
    "one_step_only",
    "additive_output_only",
)

HIERARCHY_BOOL_FIELDS = (
    "derivative_surfaces_allowed_as_basis",
    "operator_surfaces_allowed_as_basis",
    "self_orientation_allowed_as_authority",
    "currentness_may_be_inferred_by_recency",
)

CORRESPONDENCE_BOOL_FIELDS = (
    "must_preserve_current_basis",
    "must_preserve_open_surfaces",
    "must_preserve_blocked_refused_surfaces",
    "must_preserve_derivative_source_distinction",
    "must_preserve_non_claims",
    "must_prevent_over_mirroring",
    "must_prevent_under_mirroring",
)

PERMISSION_BOOL_FIELDS = (
    "read_permission_requested",
    "derive_permission_requested",
    "emit_permission_requested",
    "mutate_permission_requested",
    "replay_permission_requested",
    "merge_permission_requested",
)

DECLARED_NON_CLAIM_FIELDS = (
    "does_not_create_authority",
    "does_not_complete_continuity",
    "does_not_complete_final_governance",
    "does_not_complete_final_system_identity",
    "does_not_upgrade_standing",
    "does_not_replace_source_surfaces",
    "does_not_upgrade_derivative_outputs_to_source",
    "does_not_create_general_permission",
    "does_not_authorize_follow_on_steps",
)

REFUSAL_ACK_BOOL_FIELDS = (
    "request_may_be_blocked",
    "blocked_result_must_preserve_basis",
    "no_fallback_to_human_narration",
    "no_fallback_to_latest_file",
)

EFFECTIVE_REFERENCE_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

BLOCK_REASONS = {
    "SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED": (
        "The selected self-orientation result is not SELF_ORIENTED."
    ),
    "SELF_ORIENTATION_RESULT_UNREADABLE": (
        "The selected self-orientation result could not be read."
    ),
    "SELF_ORIENTATION_RESULT_MALFORMED": (
        "The selected self-orientation result is malformed."
    ),
    "SELF_ORIENTATION_RESULT_BASIS_THIN": (
        "The selected self-orientation result does not preserve required basis."
    ),
    "REENTRY_REQUEST_MISSING_OR_MALFORMED": (
        "The re-entry request is missing or malformed."
    ),
    "LOCKED_ORIENTATION_BASIS_MISSING": (
        "The re-entry request does not preserve the required locked orientation basis."
    ),
    "LOCKED_ORIENTATION_BASIS_MISMATCH": (
        "The locked orientation basis does not match the selected self-orientation result."
    ),
    "LOCKED_UPSTREAM_BASIS_UNREADABLE": (
        "A locked upstream basis path is not readable."
    ),
    "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES": (
        "The request allows derivative, API, or operator-facing surfaces as current/governing basis."
    ),
    "REQUEST_VAGUE_OR_UNBOUNDED": (
        "The declared next step is vague, unbounded, or not single-step."
    ),
    "REQUEST_EXCEEDS_RECOGNIZED_POSTURE": (
        "The declared next step exceeds the recognized self-orientation posture."
    ),
    "OPEN_SURFACE_TREATED_AS_COMPLETED": (
        "An open surface is treated as completed."
    ),
    "BLOCKED_REFUSED_SURFACE_HIDDEN": (
        "Blocked or refused posture is hidden."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required non-claim is missing or flipped."
    ),
    "SELF_ORIENTATION_TREATED_AS_SOURCE_AUTHORITY": (
        "The request treats self-orientation as source authority."
    ),
    "ROADMAP_AUTONOMY_SIGNALING_REFUSED": (
        "The request turns admission into roadmap, autonomy, or signaling."
    ),
    "MUTATION_REPLAY_MERGE_ATTEMPTED": (
        "The request attempts mutation, replay, or merge."
    ),
    "OVERWRITE_OR_SOURCE_REPLACEMENT_ATTEMPTED": (
        "The request attempts overwrite or source replacement."
    ),
    "FOLLOW_ON_AUTHORIZATION_ATTEMPTED": (
        "The request attempts follow-on authorization."
    ),
    "GENERAL_FUTURE_WORK_PERMISSION_ATTEMPTED": (
        "The request attempts general future-work permission."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "The request falls back to latest-file recency."
    ),
    "HUMAN_NARRATION_FALLBACK_REFUSED": (
        "The request falls back to human narration instead of bounded evidence."
    ),
}

RESULT_NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "continuity_completed": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "standing_upgraded": False,
    "source_replaced": False,
    "derivative_outputs_upgraded_to_source": False,
    "general_permission_created": False,
    "follow_on_steps_authorized": False,
    "self_orientation_became_authority": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "next_organ_self_generated": False,
    "workflow_engine_created": False,
}

VAGUE_OR_FORBIDDEN_PHRASES = (
    "continue the work",
    "advance iammai",
    "determine the next organ",
    "self-generate the next lawful step",
    "self generate the next lawful step",
    "use current orientation for future work",
)

ROADMAP_AUTONOMY_PHRASES = (
    "roadmap",
    "autonomy",
    "autonomous",
    "self-generate",
    "self generate",
    "signaling",
    "regulation",
    "workflow",
    "orchestration",
)

RECENCY_PHRASES = (
    "latest file",
    "newest file",
    "timestamp wins",
    "latest wins",
    "recency",
)

HUMAN_NARRATION_PHRASES = (
    "human narration",
    "explain for humans",
    "external reader",
    "readme",
    "onboarding",
)


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    if path == "provided_mapping":
        return "provided_mapping"
    try:
        resolved = _repo_path(path)
    except TypeError:
        return str(path)
    try:
        return str(resolved.resolve(strict=False).relative_to(_repo_root().resolve(strict=False)))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _clone(value: Any) -> Any:
    return copy.deepcopy(value)


def _string_or_none(value: Any) -> str | None:
    if isinstance(value, str) and value.strip():
        return value.strip()
    return None


def _safe_filename_part(value: Any) -> str:
    text = _string_or_none(value) or "unselected"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("_")
    return compact[:180] or "unselected"


def _read_json_file(
    path: Path | str,
    *,
    context: str,
    missing_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{context} is unreadable: {resolved}",
            missing_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _require_mapping(value: Any, label: str, block_code: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{label} must be an object",
            block_code,
        )
    return value


def _require_string(value: Any, label: str, block_code: str) -> str:
    text = _string_or_none(value)
    if text is None:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{label} must be a non-empty string",
            block_code,
        )
    return text


def _require_bool(value: Any, label: str, block_code: str) -> bool:
    if not isinstance(value, bool):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{label} must be a boolean",
            block_code,
        )
    return value


def _require_list(value: Any, label: str, block_code: str) -> list[Any]:
    if not isinstance(value, list):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"{label} must be a list",
            block_code,
        )
    return value


def _check(
    name: str,
    passed: bool,
    *,
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


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    if detail:
        return f"{reason} {detail}"
    return reason


def _metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return _require_mapping(
        result.get("current_self_orientation_v2_metadata"),
        "current self-orientation v2 metadata",
        "SELF_ORIENTATION_RESULT_MALFORMED",
    )


def _request_metadata(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _require_mapping(
        request.get("reentry_request_metadata"),
        "re-entry request metadata",
        "REENTRY_REQUEST_MISSING_OR_MALFORMED",
    )


def _load_reentry_request(value: Any) -> dict[str, Any]:
    if value is None:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "re-entry request is required",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )
    if isinstance(value, Mapping):
        return _clone(dict(value))
    if isinstance(value, (str, Path)):
        return _read_json_file(
            value,
            context="re-entry request",
            missing_code="REENTRY_REQUEST_MISSING_OR_MALFORMED",
            malformed_code="REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )
    raise CurrentSelfOrientationReentryAdmissibilityError(
        "re-entry request must be a mapping or JSON file path",
        "REENTRY_REQUEST_MISSING_OR_MALFORMED",
    )


def _validate_request_shape(request: Mapping[str, Any]) -> dict[str, Mapping[str, Any]]:
    sections: dict[str, Mapping[str, Any]] = {}
    for section_name in REQUEST_SECTIONS:
        block_code = (
            "LOCKED_ORIENTATION_BASIS_MISSING"
            if section_name == "locked_orientation_basis"
            else "REENTRY_REQUEST_MISSING_OR_MALFORMED"
        )
        sections[section_name] = _require_mapping(
            request.get(section_name),
            section_name,
            block_code,
        )

    for section_name, fields in REQUEST_STRING_FIELDS.items():
        section = sections[section_name]
        block_code = (
            "LOCKED_ORIENTATION_BASIS_MISSING"
            if section_name == "locked_orientation_basis"
            else "REQUEST_VAGUE_OR_UNBOUNDED"
        )
        if section_name == "self_orientation_basis":
            block_code = "REENTRY_REQUEST_MISSING_OR_MALFORMED"
        for field in fields:
            _require_string(section.get(field), f"{section_name}.{field}", block_code)

    scope = sections["declared_scope_bounds"]
    for field in SCOPE_BOOL_FIELDS:
        _require_bool(scope.get(field), f"declared_scope_bounds.{field}", "REQUEST_VAGUE_OR_UNBOUNDED")
    for field in SCOPE_LIST_FIELDS:
        _require_list(scope.get(field), f"declared_scope_bounds.{field}", "REQUEST_VAGUE_OR_UNBOUNDED")

    hierarchy = sections["hierarchy_constraints"]
    for field in HIERARCHY_BOOL_FIELDS:
        _require_bool(
            hierarchy.get(field),
            f"hierarchy_constraints.{field}",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )

    correspondence = sections["correspondence_requirements"]
    for field in CORRESPONDENCE_BOOL_FIELDS:
        _require_bool(
            correspondence.get(field),
            f"correspondence_requirements.{field}",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )

    permissions = sections["requested_permissions"]
    for field in PERMISSION_BOOL_FIELDS:
        _require_bool(
            permissions.get(field),
            f"requested_permissions.{field}",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )

    non_claims = sections["declared_non_claims"]
    for field in DECLARED_NON_CLAIM_FIELDS:
        _require_bool(
            non_claims.get(field),
            f"declared_non_claims.{field}",
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )

    acknowledgement = sections["refusal_acknowledgement"]
    for field in REFUSAL_ACK_BOOL_FIELDS:
        _require_bool(
            acknowledgement.get(field),
            f"refusal_acknowledgement.{field}",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )

    return sections


def _load_self_orientation_from_value(
    value: Any,
) -> tuple[dict[str, Any], Path | str | None, str]:
    if isinstance(value, Mapping):
        return _clone(dict(value)), None, "provided_self_orientation_mapping"
    if isinstance(value, (str, Path)):
        return (
            _read_json_file(
                value,
                context="self-orientation result",
                missing_code="SELF_ORIENTATION_RESULT_UNREADABLE",
                malformed_code="SELF_ORIENTATION_RESULT_MALFORMED",
            ),
            value,
            "explicit_self_orientation_result_path",
        )
    raise CurrentSelfOrientationReentryAdmissibilityError(
        "self-orientation result must be a mapping or JSON file path",
        "SELF_ORIENTATION_RESULT_MALFORMED",
    )


def _select_self_orientation_from_request(
    request_sections: Mapping[str, Mapping[str, Any]],
) -> tuple[dict[str, Any], Path | str | None, str]:
    basis = request_sections["self_orientation_basis"]
    declared_path = _string_or_none(basis.get("self_orientation_result_path"))
    declared_id = _string_or_none(basis.get("self_orientation_result_id"))
    if declared_path:
        return (
            _read_json_file(
                declared_path,
                context="declared self-orientation result",
                missing_code="SELF_ORIENTATION_RESULT_UNREADABLE",
                malformed_code="SELF_ORIENTATION_RESULT_MALFORMED",
            ),
            declared_path,
            "request_declared_self_orientation_path",
        )

    if declared_id is None:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "request does not identify a self-orientation result",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )

    root = _repo_path(SELF_ORIENTATION_V2_ROOT)
    if not root.is_dir():
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"self-orientation v2 root is not readable: {root}",
            "SELF_ORIENTATION_RESULT_UNREADABLE",
        )

    matches: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(root.glob("*.json")):
        artifact = _read_json_file(
            path,
            context="candidate self-orientation result",
            missing_code="SELF_ORIENTATION_RESULT_UNREADABLE",
            malformed_code="SELF_ORIENTATION_RESULT_MALFORMED",
        )
        try:
            metadata = _metadata(artifact)
        except CurrentSelfOrientationReentryAdmissibilityError:
            continue
        if (
            artifact.get("outcome") == SELF_ORIENTATION_OUTCOME
            and metadata.get("self_orientation_result_id") == declared_id
        ):
            matches.append((path, artifact))

    if not matches:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "no successful self-orientation result matches the request basis",
            "SELF_ORIENTATION_RESULT_UNREADABLE",
        )
    if len(matches) > 1:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "multiple matching self-orientation results require recency arbitration",
            "LATEST_FILE_RECENCY_REFUSED",
        )
    path, artifact = matches[0]
    return artifact, path, "successful_self_orientation_discovery_by_request_id"


def _effective_references_from_self_orientation(
    result: Mapping[str, Any],
) -> Mapping[str, Any]:
    selected = _require_mapping(
        result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    selected_effective = selected.get("selected_effective_references")
    if isinstance(selected_effective, Mapping):
        return selected_effective

    basis = _require_mapping(
        result.get("self_orientation_basis"),
        "self_orientation_basis",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    basis_effective = basis.get("effective_references")
    if isinstance(basis_effective, Mapping):
        return basis_effective

    raise CurrentSelfOrientationReentryAdmissibilityError(
        "self-orientation result does not preserve effective references",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )


def _validate_self_orientation_result(result: Mapping[str, Any]) -> None:
    missing = sorted(REQUIRED_SELF_ORIENTATION_TOP_LEVEL_KEYS - set(result))
    if missing:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            f"self-orientation result is missing top-level sections: {missing}",
            "SELF_ORIENTATION_RESULT_MALFORMED",
        )

    metadata = _metadata(result)
    for key in (
        "self_orientation_result_id",
        "self_orientation_result_type",
        "self_orientation_result_version",
        "generated_at",
        "resolver_module",
    ):
        _require_string(metadata.get(key), f"current_self_orientation_v2_metadata.{key}", "SELF_ORIENTATION_RESULT_MALFORMED")
    if metadata.get("self_orientation_result_type") != SELF_ORIENTATION_V2_RESULT_TYPE:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-orientation result type is not the v2 result family",
            "SELF_ORIENTATION_RESULT_MALFORMED",
        )
    if metadata.get("resolver_module") != SELF_ORIENTATION_V2_RESOLVER_MODULE:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-orientation result resolver module is not the v2 resolver",
            "SELF_ORIENTATION_RESULT_MALFORMED",
        )

    if result.get("outcome") != SELF_ORIENTATION_OUTCOME:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-orientation result is not SELF_ORIENTED",
            "SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED",
        )

    block = _require_mapping(result.get("block"), "block", "SELF_ORIENTATION_RESULT_MALFORMED")
    if block.get("block_code") is not None or block.get("block_reason") is not None:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-oriented result carries a block",
            "SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED",
        )

    selected = _require_mapping(
        result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    for name in (
        "selected_body_pass_result",
        "selected_source_surface",
        "selected_current_state_answer_read_result",
        "selected_current_state_what_stands_now_result",
    ):
        identity = _require_mapping(
            selected.get(name),
            name,
            "SELF_ORIENTATION_RESULT_BASIS_THIN",
        )
        _require_string(identity.get("result_id"), f"{name}.result_id", "SELF_ORIENTATION_RESULT_BASIS_THIN")
        _require_string(identity.get("result_path"), f"{name}.result_path", "SELF_ORIENTATION_RESULT_BASIS_THIN")

    for section_name in (
        "recognized_current_executable_core_line",
        "recognized_governing_effective_basis",
        "recognized_current_state_surfaces",
        "recognized_continuity_surfaces",
        "recognized_derivative_surfaces",
        "recognized_operator_facing_surfaces",
        "recognized_open_surfaces",
        "recognized_touch_admissibility_surfaces",
        "self_orientation_basis",
        "current_self_orientation_summary",
    ):
        _require_mapping(
            result.get(section_name),
            section_name,
            "SELF_ORIENTATION_RESULT_BASIS_THIN",
        )
    _require_list(
        result.get("recognized_blocked_or_refused_surfaces"),
        "recognized_blocked_or_refused_surfaces",
        "SELF_ORIENTATION_RESULT_MALFORMED",
    )
    checks = _require_list(
        result.get("bounded_correspondence_checks"),
        "bounded_correspondence_checks",
        "SELF_ORIENTATION_RESULT_MALFORMED",
    )
    if not checks or not all(isinstance(check, Mapping) and check.get("passed") is True for check in checks):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-orientation correspondence checks are missing or failed",
            "SELF_ORIENTATION_RESULT_BASIS_THIN",
        )

    governing = _require_mapping(
        result.get("recognized_governing_effective_basis"),
        "recognized_governing_effective_basis",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    if governing.get("recognized_from_explicit_effective_references") is not True:
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "self-orientation governing basis is not explicit",
            "SELF_ORIENTATION_RESULT_BASIS_THIN",
        )
    effective = _effective_references_from_self_orientation(result)
    for key in EFFECTIVE_REFERENCE_KEYS:
        _require_string(effective.get(key), f"effective_references.{key}", "SELF_ORIENTATION_RESULT_BASIS_THIN")

    non_claims = _require_mapping(
        result.get("non_claims"),
        "non_claims",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key, value in non_claims.items():
        if not isinstance(key, str) or value is not False:
            raise CurrentSelfOrientationReentryAdmissibilityError(
                f"self-orientation non-claim is not false: {key}",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )


def _identity_from_self_orientation(
    result: Mapping[str, Any],
    path: Path | str | None,
    *,
    selection_mode: str,
    request_path: str | None = None,
) -> dict[str, Any]:
    metadata = _metadata(result)
    return {
        "result_path": _display_path(path) or request_path,
        "result_id": metadata.get("self_orientation_result_id"),
        "result_type": metadata.get("self_orientation_result_type"),
        "result_version": metadata.get("self_orientation_result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "outcome": result.get("outcome"),
        "selection_mode": selection_mode,
    }


def _empty_self_orientation_identity() -> dict[str, Any]:
    return {
        "result_path": None,
        "result_id": None,
        "result_type": None,
        "result_version": None,
        "resolver_module": None,
        "outcome": None,
        "selection_mode": None,
    }


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    return left_text == right_text or _display_path(left_text) == _display_path(right_text)


def _identity_value(
    selected_inputs: Mapping[str, Any],
    section_name: str,
    field: str,
) -> Any:
    section = selected_inputs.get(section_name)
    section = section if isinstance(section, Mapping) else {}
    return section.get(field)


def _locked_basis_checks(
    request_locked_basis: Mapping[str, Any],
    self_orientation_result: Mapping[str, Any],
) -> list[dict[str, Any]]:
    selected = _require_mapping(
        self_orientation_result.get("selected_orientation_inputs"),
        "selected_orientation_inputs",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    self_basis = _require_mapping(
        self_orientation_result.get("self_orientation_basis"),
        "self_orientation_basis",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    effective = _effective_references_from_self_orientation(self_orientation_result)

    comparisons = (
        (
            "locked_body_pass_basis_matches_self_orientation",
            request_locked_basis.get("selected_body_pass_result_id"),
            _identity_value(selected, "selected_body_pass_result", "result_id"),
            False,
        ),
        (
            "locked_body_pass_path_matches_self_orientation",
            request_locked_basis.get("selected_body_pass_result_path"),
            _identity_value(selected, "selected_body_pass_result", "result_path"),
            True,
        ),
        (
            "locked_source_surface_basis_matches_self_orientation",
            request_locked_basis.get("selected_source_surface_id"),
            _identity_value(selected, "selected_source_surface", "result_id"),
            False,
        ),
        (
            "locked_source_surface_path_matches_self_orientation",
            request_locked_basis.get("selected_source_surface_path"),
            _identity_value(selected, "selected_source_surface", "result_path"),
            True,
        ),
        (
            "locked_answer_read_basis_matches_self_orientation",
            request_locked_basis.get("selected_current_state_answer_read_id"),
            _identity_value(selected, "selected_current_state_answer_read_result", "result_id"),
            False,
        ),
        (
            "locked_answer_read_path_matches_self_orientation",
            request_locked_basis.get("selected_current_state_answer_read_path"),
            _identity_value(selected, "selected_current_state_answer_read_result", "result_path"),
            True,
        ),
        (
            "locked_what_stands_now_basis_matches_self_orientation",
            request_locked_basis.get("selected_what_stands_now_id"),
            _identity_value(selected, "selected_current_state_what_stands_now_result", "result_id"),
            False,
        ),
        (
            "locked_what_stands_now_path_matches_self_orientation",
            request_locked_basis.get("selected_what_stands_now_path"),
            _identity_value(selected, "selected_current_state_what_stands_now_result", "result_path"),
            True,
        ),
    )

    checks: list[dict[str, Any]] = []
    for name, request_value, selected_value, is_path in comparisons:
        passed = (
            _path_equal(request_value, selected_value)
            if is_path
            else request_value == selected_value
        )
        checks.append(
            _check(
                name,
                passed,
                expected=selected_value,
                actual=request_value,
                block_code="LOCKED_ORIENTATION_BASIS_MISMATCH",
            )
        )

    for key in EFFECTIVE_REFERENCE_KEYS:
        selected_value = effective.get(key) or _require_mapping(
            self_basis.get("effective_references"),
            "self_orientation_basis.effective_references",
            "SELF_ORIENTATION_RESULT_BASIS_THIN",
        ).get(key)
        request_value = request_locked_basis.get(key)
        checks.append(
            _check(
                f"locked_{key}_matches_self_orientation",
                _path_equal(request_value, selected_value),
                expected=selected_value,
                actual=request_value,
                block_code="LOCKED_ORIENTATION_BASIS_MISMATCH",
            )
        )
    checks.append(
        _check(
            "locked_orientation_basis_matches_self_orientation",
            all(check.get("passed") is True for check in checks),
            expected="locked request basis equals selected self-orientation basis",
            actual={
                "checked_basis_count": len(checks),
                "failed_basis_checks": [
                    check["check_name"]
                    for check in checks
                    if check.get("passed") is not True
                ],
            },
            block_code="LOCKED_ORIENTATION_BASIS_MISMATCH",
        )
    )
    return checks


def _locked_basis_readability_checks(
    locked_basis: Mapping[str, Any],
) -> list[dict[str, Any]]:
    path_keys = (
        "selected_body_pass_result_path",
        "selected_source_surface_path",
        "selected_current_state_answer_read_path",
        "selected_what_stands_now_path",
        *EFFECTIVE_REFERENCE_KEYS,
    )
    checks = []
    for key in path_keys:
        path_value = _string_or_none(locked_basis.get(key))
        if path_value == "provided_mapping":
            passed = True
        elif path_value is None:
            passed = False
        else:
            passed = _repo_path(path_value).exists()
        checks.append(
            _check(
                f"locked_upstream_{key}_is_readable",
                passed,
                expected="existing path from locked basis",
                actual=path_value,
                block_code="LOCKED_UPSTREAM_BASIS_UNREADABLE",
            )
        )
    return checks


def _text_blob(*values: Any) -> str:
    parts: list[str] = []
    for value in values:
        if isinstance(value, str):
            parts.append(value)
        elif isinstance(value, Mapping):
            parts.extend(str(item) for item in value.values())
        elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
            parts.extend(str(item) for item in value)
    return " ".join(parts).lower()


def _step_boundedness_checks(
    next_step: Mapping[str, Any],
    scope: Mapping[str, Any],
    permissions: Mapping[str, Any],
) -> list[dict[str, Any]]:
    text = _text_blob(next_step, scope, permissions)
    next_step_family = next_step.get("next_step_family")
    one_step_only = scope.get("one_step_only")
    additive_only = scope.get("additive_output_only")
    purpose = _string_or_none(next_step.get("declared_purpose"))
    relation = _string_or_none(next_step.get("requested_relation_to_basis"))
    authorization_scope = permissions.get("authorization_scope")

    checks = [
        _check(
            "next_step_family_is_allowed",
            next_step_family in ALLOWED_NEXT_STEP_FAMILIES,
            expected=sorted(ALLOWED_NEXT_STEP_FAMILIES),
            actual=next_step_family,
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "requested_relation_to_basis_is_explicit",
            bool(relation),
            expected="non-empty requested relation to selected basis",
            actual=relation,
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "declared_purpose_is_bounded",
            bool(purpose) and not any(phrase in text for phrase in VAGUE_OR_FORBIDDEN_PHRASES),
            expected="bounded purpose without continue/advance/self-generation language",
            actual=purpose,
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "request_is_one_step_only",
            one_step_only is True,
            expected=True,
            actual=one_step_only,
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "request_output_is_additive_only",
            additive_only is True,
            expected=True,
            actual=additive_only,
            block_code="OVERWRITE_OR_SOURCE_REPLACEMENT_ATTEMPTED",
        ),
        _check(
            "request_does_not_attempt_follow_on_authorization",
            authorization_scope == "single_declared_step_only",
            expected="single_declared_step_only",
            actual=authorization_scope,
            block_code="FOLLOW_ON_AUTHORIZATION_ATTEMPTED",
        ),
        _check(
            "request_does_not_attempt_general_future_work_permission",
            "future work" not in text and "general permission" not in text,
            expected="no broad future-work permission",
            actual=text,
            block_code="GENERAL_FUTURE_WORK_PERMISSION_ATTEMPTED",
        ),
        _check(
            "request_does_not_become_roadmap_autonomy_or_signaling",
            not any(phrase in text for phrase in ROADMAP_AUTONOMY_PHRASES),
            expected="no roadmap/autonomy/signaling/workflow language",
            actual=text,
            block_code="ROADMAP_AUTONOMY_SIGNALING_REFUSED",
        ),
        _check(
            "request_does_not_use_latest_file_recency",
            not any(phrase in text for phrase in RECENCY_PHRASES),
            expected="no latest-file or recency basis",
            actual=text,
            block_code="LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "request_does_not_fall_back_to_human_narration",
            not any(phrase in text for phrase in HUMAN_NARRATION_PHRASES),
            expected="bounded internal gate, not external-reader narration",
            actual=text,
            block_code="HUMAN_NARRATION_FALLBACK_REFUSED",
        ),
    ]
    return checks


def _hierarchy_checks(hierarchy: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        _check(
            "current_governing_basis_source_is_upstream",
            "upstream" in str(hierarchy.get("current_governing_basis_source", "")).lower()
            or "current" in str(hierarchy.get("current_governing_basis_source", "")).lower()
            or "effective" in str(hierarchy.get("current_governing_basis_source", "")).lower(),
            expected="upstream current/effective/governing/current-state basis",
            actual=hierarchy.get("current_governing_basis_source"),
            block_code="CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
        ),
        _check(
            "derivative_surfaces_are_not_allowed_as_basis",
            hierarchy.get("derivative_surfaces_allowed_as_basis") is False,
            expected=False,
            actual=hierarchy.get("derivative_surfaces_allowed_as_basis"),
            block_code="CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
        ),
        _check(
            "operator_surfaces_are_not_allowed_as_basis",
            hierarchy.get("operator_surfaces_allowed_as_basis") is False,
            expected=False,
            actual=hierarchy.get("operator_surfaces_allowed_as_basis"),
            block_code="CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
        ),
        _check(
            "self_orientation_is_not_allowed_as_authority",
            hierarchy.get("self_orientation_allowed_as_authority") is False,
            expected=False,
            actual=hierarchy.get("self_orientation_allowed_as_authority"),
            block_code="SELF_ORIENTATION_TREATED_AS_SOURCE_AUTHORITY",
        ),
        _check(
            "currentness_may_not_be_inferred_by_recency",
            hierarchy.get("currentness_may_be_inferred_by_recency") is False,
            expected=False,
            actual=hierarchy.get("currentness_may_be_inferred_by_recency"),
            block_code="LATEST_FILE_RECENCY_REFUSED",
        ),
    ]


def _correspondence_checks(
    correspondence: Mapping[str, Any],
    self_orientation_result: Mapping[str, Any],
) -> list[dict[str, Any]]:
    open_surfaces = _require_mapping(
        self_orientation_result.get("recognized_open_surfaces"),
        "recognized_open_surfaces",
        "SELF_ORIENTATION_RESULT_BASIS_THIN",
    )
    open_results = open_surfaces.get("what_remains_open_results")
    open_results = open_results if isinstance(open_results, list) else []
    blocked_or_refused = _require_list(
        self_orientation_result.get("recognized_blocked_or_refused_surfaces"),
        "recognized_blocked_or_refused_surfaces",
        "SELF_ORIENTATION_RESULT_MALFORMED",
    )
    non_claims = _require_mapping(
        self_orientation_result.get("non_claims"),
        "non_claims",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    checks = [
        _check(
            "request_must_preserve_current_basis",
            correspondence.get("must_preserve_current_basis") is True,
            expected=True,
            actual=correspondence.get("must_preserve_current_basis"),
            block_code="REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
        ),
        _check(
            "request_must_preserve_open_surfaces",
            correspondence.get("must_preserve_open_surfaces") is True,
            expected=True,
            actual=correspondence.get("must_preserve_open_surfaces"),
            block_code="OPEN_SURFACE_TREATED_AS_COMPLETED",
        ),
        _check(
            "recognized_open_surfaces_remain_open_or_blocked",
            all(
                isinstance(item, Mapping)
                and item.get("outcome") in {"ANSWERED_WHAT_REMAINS_OPEN", "BLOCKED"}
                for item in open_results
            ),
            expected="open surfaces stay open or blocked",
            actual=[item.get("outcome") for item in open_results if isinstance(item, Mapping)],
            block_code="OPEN_SURFACE_TREATED_AS_COMPLETED",
        ),
        _check(
            "request_must_preserve_blocked_refused_surfaces",
            correspondence.get("must_preserve_blocked_refused_surfaces") is True,
            expected=True,
            actual=correspondence.get("must_preserve_blocked_refused_surfaces"),
            block_code="BLOCKED_REFUSED_SURFACE_HIDDEN",
        ),
        _check(
            "blocked_refused_surfaces_remain_visible",
            isinstance(blocked_or_refused, list),
            expected="recognized blocked/refused list remains present",
            actual=blocked_or_refused,
            block_code="BLOCKED_REFUSED_SURFACE_HIDDEN",
        ),
        _check(
            "request_must_preserve_derivative_source_distinction",
            correspondence.get("must_preserve_derivative_source_distinction") is True,
            expected=True,
            actual=correspondence.get("must_preserve_derivative_source_distinction"),
            block_code="REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
        ),
        _check(
            "request_must_preserve_non_claims",
            correspondence.get("must_preserve_non_claims") is True,
            expected=True,
            actual=correspondence.get("must_preserve_non_claims"),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "self_orientation_non_claims_remain_false",
            all(value is False for value in non_claims.values()),
            expected=False,
            actual=dict(non_claims),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "request_must_prevent_over_mirroring",
            correspondence.get("must_prevent_over_mirroring") is True,
            expected=True,
            actual=correspondence.get("must_prevent_over_mirroring"),
            block_code="REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
        ),
        _check(
            "request_must_prevent_under_mirroring",
            correspondence.get("must_prevent_under_mirroring") is True,
            expected=True,
            actual=correspondence.get("must_prevent_under_mirroring"),
            block_code="REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
        ),
    ]
    return checks


def _permission_checks(
    scope: Mapping[str, Any],
    permissions: Mapping[str, Any],
) -> list[dict[str, Any]]:
    allowed_new_files = _require_list(
        scope.get("allowed_new_file_paths"),
        "declared_scope_bounds.allowed_new_file_paths",
        "REQUEST_VAGUE_OR_UNBOUNDED",
    )
    allowed_artifact_roots = _require_list(
        scope.get("allowed_artifact_output_roots"),
        "declared_scope_bounds.allowed_artifact_output_roots",
        "REQUEST_VAGUE_OR_UNBOUNDED",
    )
    output_target_count = len(allowed_new_files) + len(allowed_artifact_roots)
    emit_requested = permissions.get("emit_permission_requested") is True

    return [
        _check(
            "read_permission_is_boolean_and_bounded",
            permissions.get("read_permission_requested") in {True, False},
            expected="boolean",
            actual=permissions.get("read_permission_requested"),
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "derive_permission_is_boolean_and_bounded",
            permissions.get("derive_permission_requested") in {True, False},
            expected="boolean",
            actual=permissions.get("derive_permission_requested"),
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "emit_permission_is_limited_to_one_additive_output_when_requested",
            (not emit_requested and output_target_count == 0)
            or (emit_requested and output_target_count == 1),
            expected="zero output targets when emit is false, one additive target when emit is true",
            actual={
                "emit_permission_requested": emit_requested,
                "allowed_new_file_paths": allowed_new_files,
                "allowed_artifact_output_roots": allowed_artifact_roots,
            },
            block_code="REQUEST_VAGUE_OR_UNBOUNDED",
        ),
        _check(
            "mutate_permission_is_false",
            permissions.get("mutate_permission_requested") is False,
            expected=False,
            actual=permissions.get("mutate_permission_requested"),
            block_code="MUTATION_REPLAY_MERGE_ATTEMPTED",
        ),
        _check(
            "replay_permission_is_false",
            permissions.get("replay_permission_requested") is False,
            expected=False,
            actual=permissions.get("replay_permission_requested"),
            block_code="MUTATION_REPLAY_MERGE_ATTEMPTED",
        ),
        _check(
            "merge_permission_is_false",
            permissions.get("merge_permission_requested") is False,
            expected=False,
            actual=permissions.get("merge_permission_requested"),
            block_code="MUTATION_REPLAY_MERGE_ATTEMPTED",
        ),
        _check(
            "authorization_scope_is_single_declared_step_only",
            permissions.get("authorization_scope") == "single_declared_step_only",
            expected="single_declared_step_only",
            actual=permissions.get("authorization_scope"),
            block_code="FOLLOW_ON_AUTHORIZATION_ATTEMPTED",
        ),
    ]


def _declared_non_claim_checks(non_claims: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks = []
    for field in DECLARED_NON_CLAIM_FIELDS:
        checks.append(
            _check(
                f"declared_non_claim_{field}_is_true",
                non_claims.get(field) is True,
                expected=True,
                actual=non_claims.get(field),
                block_code="NON_CLAIM_MISSING_OR_FLIPPED",
            )
        )
    return checks


def _refusal_acknowledgement_checks(acknowledgement: Mapping[str, Any]) -> list[dict[str, Any]]:
    block_by_field = {
        "request_may_be_blocked": "REQUEST_VAGUE_OR_UNBOUNDED",
        "blocked_result_must_preserve_basis": "REQUEST_VAGUE_OR_UNBOUNDED",
        "no_fallback_to_human_narration": "HUMAN_NARRATION_FALLBACK_REFUSED",
        "no_fallback_to_latest_file": "LATEST_FILE_RECENCY_REFUSED",
    }
    return [
        _check(
            f"refusal_acknowledgement_{field}_is_true",
            acknowledgement.get(field) is True,
            expected=True,
            actual=acknowledgement.get(field),
            block_code=block_by_field[field],
        )
        for field in REFUSAL_ACK_BOOL_FIELDS
    ]


def _self_orientation_basis_checks(
    request_basis: Mapping[str, Any],
    selected_self_orientation: Mapping[str, Any],
) -> list[dict[str, Any]]:
    return [
        _check(
            "request_names_selected_self_orientation_id",
            request_basis.get("self_orientation_result_id")
            == selected_self_orientation.get("result_id"),
            expected=selected_self_orientation.get("result_id"),
            actual=request_basis.get("self_orientation_result_id"),
            block_code="LOCKED_ORIENTATION_BASIS_MISMATCH",
        ),
        _check(
            "request_names_selected_self_orientation_path",
            _path_equal(
                request_basis.get("self_orientation_result_path"),
                selected_self_orientation.get("result_path"),
            ),
            expected=selected_self_orientation.get("result_path"),
            actual=request_basis.get("self_orientation_result_path"),
            block_code="LOCKED_ORIENTATION_BASIS_MISMATCH",
        ),
        _check(
            "request_names_self_oriented_outcome",
            request_basis.get("self_orientation_outcome") == SELF_ORIENTATION_OUTCOME,
            expected=SELF_ORIENTATION_OUTCOME,
            actual=request_basis.get("self_orientation_outcome"),
            block_code="SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED",
        ),
        _check(
            "request_names_self_orientation_resolver_module",
            request_basis.get("self_orientation_resolver_module")
            == SELF_ORIENTATION_V2_RESOLVER_MODULE,
            expected=SELF_ORIENTATION_V2_RESOLVER_MODULE,
            actual=request_basis.get("self_orientation_resolver_module"),
            block_code="SELF_ORIENTATION_RESULT_MALFORMED",
        ),
    ]


def _merged_non_claims(self_orientation_result: Mapping[str, Any]) -> dict[str, bool]:
    merged = dict(RESULT_NON_CLAIM_DEFAULTS)
    source_non_claims = self_orientation_result.get("non_claims")
    if isinstance(source_non_claims, Mapping):
        for key, value in source_non_claims.items():
            if isinstance(key, str) and value is False:
                merged[key] = False
    return merged


def _result_id(selected_self_orientation: Mapping[str, Any], outcome: str) -> str:
    base = _string_or_none(selected_self_orientation.get("result_id"))
    if base is None:
        base = "no_selected_self_orientation_result"
    suffix = (
        "reentry_admitted"
        if outcome == OUTCOME_REENTRY_ADMITTED
        else "reentry_blocked"
    )
    return f"{base}__{suffix}"


def _result_metadata(selected_self_orientation: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    return {
        "reentry_admissibility_result_id": _result_id(selected_self_orientation, outcome),
        "reentry_admissibility_result_type": REENTRY_ADMISSIBILITY_RESULT_TYPE,
        "reentry_admissibility_result_version": REENTRY_ADMISSIBILITY_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(
    *,
    selected_self_orientation: Mapping[str, Any],
    locked_orientation_basis: Mapping[str, Any],
    selected_reentry_request: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    next_step = selected_reentry_request.get("declared_next_step")
    next_step = next_step if isinstance(next_step, Mapping) else {}
    permissions = selected_reentry_request.get("requested_permissions")
    permissions = permissions if isinstance(permissions, Mapping) else {}
    result = {
        "current_self_orientation_reentry_admissibility_metadata": _result_metadata(
            selected_self_orientation,
            outcome,
        ),
        "selected_self_orientation_result": dict(selected_self_orientation),
        "locked_orientation_basis": _clone(dict(locked_orientation_basis)),
        "selected_reentry_request": _clone(dict(selected_reentry_request)),
        "reentry_admissibility_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "reentry_admissibility_basis": {
            "basis_kind": "single_self_orientation_result_plus_single_reentry_request",
            "selected_self_orientation_result_id": selected_self_orientation.get("result_id"),
            "selected_self_orientation_result_path": selected_self_orientation.get("result_path"),
            "selected_body_pass_result_id": locked_orientation_basis.get("selected_body_pass_result_id"),
            "selected_source_surface_id": locked_orientation_basis.get("selected_source_surface_id"),
            "selected_current_state_answer_read_id": locked_orientation_basis.get(
                "selected_current_state_answer_read_id"
            ),
            "selected_what_stands_now_id": locked_orientation_basis.get("selected_what_stands_now_id"),
            "next_step_family": next_step.get("next_step_family"),
            "next_step_kind": next_step.get("next_step_kind"),
            "authorization_scope": permissions.get("authorization_scope"),
            "admission_scope": "single_declared_step_only",
            "self_orientation_remains_non_authoritative": True,
        },
        "current_self_orientation_reentry_admissibility_summary": {},
        "non_claims": dict(non_claims),
    }
    result["current_self_orientation_reentry_admissibility_summary"] = (
        build_current_self_orientation_reentry_admissibility_summary(result)
    )
    return result


def _blocked_result(
    *,
    selected_self_orientation: Mapping[str, Any] | None = None,
    locked_orientation_basis: Mapping[str, Any] | None = None,
    selected_reentry_request: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    block_code: str,
    block_detail: str | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _build_result(
        selected_self_orientation=selected_self_orientation or _empty_self_orientation_identity(),
        locked_orientation_basis=locked_orientation_basis or {},
        selected_reentry_request=selected_reentry_request or {},
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        non_claims=non_claims or dict(RESULT_NON_CLAIM_DEFAULTS),
    )


def _resolve_internal(
    self_orientation_result: Any,
    reentry_request: Any,
) -> dict[str, Any]:
    request = _load_reentry_request(reentry_request)
    request_sections = _validate_request_shape(request)
    locked_basis = request_sections["locked_orientation_basis"]
    request_self_basis = request_sections["self_orientation_basis"]

    if self_orientation_result is None:
        orientation, orientation_path, selection_mode = _select_self_orientation_from_request(
            request_sections
        )
    else:
        orientation, orientation_path, selection_mode = _load_self_orientation_from_value(
            self_orientation_result
        )

    _validate_self_orientation_result(orientation)
    selected_self_orientation = _identity_from_self_orientation(
        orientation,
        orientation_path,
        selection_mode=selection_mode,
        request_path=_string_or_none(request_self_basis.get("self_orientation_result_path")),
    )
    non_claims = _merged_non_claims(orientation)

    checks: list[dict[str, Any]] = []
    checks.append(
        _check(
            "self_orientation_result_is_self_oriented",
            orientation.get("outcome") == SELF_ORIENTATION_OUTCOME,
            expected=SELF_ORIENTATION_OUTCOME,
            actual=orientation.get("outcome"),
            block_code="SELF_ORIENTATION_RESULT_NOT_SELF_ORIENTED",
        )
    )
    checks.append(
        _check(
            "self_orientation_result_preserves_required_sections",
            True,
            expected=sorted(REQUIRED_SELF_ORIENTATION_TOP_LEVEL_KEYS),
            actual=sorted(orientation),
            block_code="SELF_ORIENTATION_RESULT_BASIS_THIN",
        )
    )
    checks.extend(_self_orientation_basis_checks(request_self_basis, selected_self_orientation))
    checks.extend(_locked_basis_checks(locked_basis, orientation))
    checks.extend(_locked_basis_readability_checks(locked_basis))
    checks.extend(
        _step_boundedness_checks(
            request_sections["declared_next_step"],
            request_sections["declared_scope_bounds"],
            request_sections["requested_permissions"],
        )
    )
    checks.extend(_hierarchy_checks(request_sections["hierarchy_constraints"]))
    checks.extend(
        _correspondence_checks(
            request_sections["correspondence_requirements"],
            orientation,
        )
    )
    checks.extend(
        _permission_checks(
            request_sections["declared_scope_bounds"],
            request_sections["requested_permissions"],
        )
    )
    checks.extend(_declared_non_claim_checks(request_sections["declared_non_claims"]))
    checks.extend(
        _refusal_acknowledgement_checks(
            request_sections["refusal_acknowledgement"]
        )
    )

    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            selected_self_orientation=selected_self_orientation,
            locked_orientation_basis=locked_basis,
            selected_reentry_request=request,
            checks=checks,
            block_code=_string_or_none(failed.get("block_code"))
            or "REQUEST_EXCEEDS_RECOGNIZED_POSTURE",
            block_detail=f"failed check: {failed.get('check_name')}",
            non_claims=non_claims,
        )

    return _build_result(
        selected_self_orientation=selected_self_orientation,
        locked_orientation_basis=locked_basis,
        selected_reentry_request=request,
        checks=checks,
        outcome=OUTCOME_REENTRY_ADMITTED,
        block_code=None,
        block_detail=None,
        non_claims=non_claims,
    )


def resolve_current_self_orientation_reentry_admissibility(
    self_orientation_result: Mapping[str, Any] | None = None,
    reentry_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded re-entry admission/refusal decision."""

    try:
        return _resolve_internal(self_orientation_result, reentry_request)
    except CurrentSelfOrientationReentryAdmissibilityError as exc:
        request: dict[str, Any] = {}
        locked_basis: Mapping[str, Any] = {}
        selected_self_orientation = _empty_self_orientation_identity()
        non_claims = dict(RESULT_NON_CLAIM_DEFAULTS)

        if isinstance(reentry_request, Mapping):
            request = _clone(dict(reentry_request))
            maybe_locked = request.get("locked_orientation_basis")
            if isinstance(maybe_locked, Mapping):
                locked_basis = maybe_locked
        if isinstance(self_orientation_result, Mapping):
            try:
                selected_self_orientation = _identity_from_self_orientation(
                    self_orientation_result,
                    None,
                    selection_mode="provided_self_orientation_mapping",
                    request_path=(
                        _string_or_none(
                            _require_mapping(
                                request.get("self_orientation_basis"),
                                "self_orientation_basis",
                                "REENTRY_REQUEST_MISSING_OR_MALFORMED",
                            ).get("self_orientation_result_path")
                        )
                        if isinstance(request.get("self_orientation_basis"), Mapping)
                        else None
                    ),
                )
                non_claims = _merged_non_claims(self_orientation_result)
            except CurrentSelfOrientationReentryAdmissibilityError:
                selected_self_orientation = _empty_self_orientation_identity()

        return _blocked_result(
            selected_self_orientation=selected_self_orientation,
            locked_orientation_basis=locked_basis,
            selected_reentry_request=request,
            block_code=exc.block_code,
            block_detail=str(exc),
            non_claims=non_claims,
        )


def resolve_current_self_orientation_reentry_admissibility_from_path(
    self_orientation_result_path: Path | str,
    reentry_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve re-entry admissibility from an explicit self-orientation path."""

    try:
        return _resolve_internal(self_orientation_result_path, reentry_request)
    except CurrentSelfOrientationReentryAdmissibilityError as exc:
        request: dict[str, Any] = {}
        locked_basis: Mapping[str, Any] = {}
        if isinstance(reentry_request, Mapping):
            request = _clone(dict(reentry_request))
            maybe_locked = request.get("locked_orientation_basis")
            if isinstance(maybe_locked, Mapping):
                locked_basis = maybe_locked
        return _blocked_result(
            selected_self_orientation={
                **_empty_self_orientation_identity(),
                "result_path": _display_path(self_orientation_result_path),
                "selection_mode": "explicit_self_orientation_result_path",
            },
            locked_orientation_basis=locked_basis,
            selected_reentry_request=request,
            block_code=exc.block_code,
            block_detail=str(exc),
        )


def _check_family_passed(
    checks: Sequence[Mapping[str, Any]],
    prefixes: Sequence[str],
) -> bool:
    selected = [
        check
        for check in checks
        if any(str(check.get("check_name", "")).startswith(prefix) for prefix in prefixes)
    ]
    return bool(selected) and all(check.get("passed") is True for check in selected)


def build_current_self_orientation_reentry_admissibility_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a bounded summary for one re-entry admissibility result."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "re-entry admissibility result must be a mapping",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )
    selected_self = result.get("selected_self_orientation_result")
    selected_self = selected_self if isinstance(selected_self, Mapping) else {}
    locked = result.get("locked_orientation_basis")
    locked = locked if isinstance(locked, Mapping) else {}
    request = result.get("selected_reentry_request")
    request = request if isinstance(request, Mapping) else {}
    next_step = request.get("declared_next_step")
    next_step = next_step if isinstance(next_step, Mapping) else {}
    checks = result.get("reentry_admissibility_checks")
    checks = checks if isinstance(checks, list) else []
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}
    permissions = request.get("requested_permissions")
    permissions = permissions if isinstance(permissions, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_self_orientation_result_id": selected_self.get("result_id"),
        "selected_self_orientation_result_path": selected_self.get("result_path"),
        "locked_selected_body_pass_result_id": locked.get("selected_body_pass_result_id"),
        "locked_selected_source_surface_id": locked.get("selected_source_surface_id"),
        "locked_selected_current_state_answer_read_id": locked.get(
            "selected_current_state_answer_read_id"
        ),
        "locked_selected_what_stands_now_id": locked.get("selected_what_stands_now_id"),
        "next_step_family": next_step.get("next_step_family"),
        "next_step_kind": next_step.get("next_step_kind"),
        "basis_lock_matched": _check_family_passed(checks, ("locked_",)),
        "hierarchy_checks_passed": _check_family_passed(
            checks,
            (
                "current_governing_basis_source",
                "derivative_surfaces",
                "operator_surfaces",
                "self_orientation_is_not_allowed",
                "currentness_may_not",
            ),
        ),
        "correspondence_checks_passed": _check_family_passed(
            checks,
            (
                "request_must_preserve",
                "recognized_open_surfaces",
                "blocked_refused",
                "self_orientation_non_claims",
                "request_must_prevent",
            ),
        ),
        "permissions_single_step_bounded": permissions.get("authorization_scope")
        == "single_declared_step_only"
        and _check_family_passed(
            checks,
            (
                "read_permission",
                "derive_permission",
                "emit_permission",
                "mutate_permission",
                "replay_permission",
                "merge_permission",
                "authorization_scope",
            ),
        ),
        "failed_check_count": sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "authority_created",
                "continuity_completed",
                "final_governance_completed",
                "final_system_identity_completed",
                "standing_upgraded",
                "source_replaced",
                "derivative_outputs_upgraded_to_source",
                "general_permission_created",
                "follow_on_steps_authorized",
                "self_orientation_became_authority",
                "latest_file_currentness",
                "recency_fraud",
                "mutation_performed",
                "replay_performed",
                "merge_performed",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT,
) -> Path:
    selected = result.get("selected_self_orientation_result")
    selected = selected if isinstance(selected, Mapping) else {}
    stem = _safe_filename_part(selected.get("result_id"))
    resolved_root = _repo_path(root)
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentSelfOrientationReentryAdmissibilityError(
        "no bounded re-entry admissibility filename is available",
        "REENTRY_REQUEST_MISSING_OR_MALFORMED",
    )


def write_current_self_orientation_reentry_admissibility_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive re-entry admissibility JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationReentryAdmissibilityError(
            "re-entry admissibility result must be a mapping",
            "REENTRY_REQUEST_MISSING_OR_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"current self-orientation re-entry admissibility result already exists: {target}"
        )
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
