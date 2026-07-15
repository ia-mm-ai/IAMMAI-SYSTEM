"""Resolve one bounded current self-orientation re-entry receipt.

This module decides whether one previously admitted re-entry step was actually
performed within the admitted bounds and whether that admission is now
exhausted.

It is a single-step receipt/refusal surface. It does not generate the next
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


class CurrentSelfOrientationReentryReceiptError(RuntimeError):
    """Raised for malformed inputs or impossible receipt correspondence."""

    def __init__(self, message: str, block_code: str) -> None:
        super().__init__(message)
        self.block_code = block_code


REENTRY_ADMISSIBILITY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)

RESOLVER_MODULE = "resolve_current_self_orientation_reentry_receipt"
REENTRY_RECEIPT_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_"
    "REENTRY_RECEIPT_RESULT"
)
REENTRY_RECEIPT_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "reentry_receipt_result"

REENTRY_ADMISSIBILITY_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_"
    "REENTRY_ADMISSIBILITY_RESULT"
)
REENTRY_ADMISSIBILITY_RESOLVER_MODULE = (
    "resolve_current_self_orientation_reentry_admissibility"
)

OUTCOME_REENTRY_ADMITTED = "REENTRY_ADMITTED"
OUTCOME_REENTRY_RECEIVED = "REENTRY_RECEIVED"
OUTCOME_BLOCKED = "BLOCKED"

REQUIRED_ADMISSIBILITY_TOP_LEVEL_KEYS = frozenset(
    {
        "current_self_orientation_reentry_admissibility_metadata",
        "selected_self_orientation_result",
        "locked_orientation_basis",
        "selected_reentry_request",
        "reentry_admissibility_checks",
        "outcome",
        "block",
        "reentry_admissibility_basis",
        "current_self_orientation_reentry_admissibility_summary",
        "non_claims",
    }
)

EFFECTIVE_REFERENCE_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

LOCKED_BASIS_STRING_FIELDS = (
    "selected_body_pass_result_id",
    "selected_body_pass_result_path",
    "selected_source_surface_id",
    "selected_source_surface_path",
    "selected_current_state_answer_read_id",
    "selected_current_state_answer_read_path",
    "selected_what_stands_now_id",
    "selected_what_stands_now_path",
    *EFFECTIVE_REFERENCE_KEYS,
)

ADMITTED_NEXT_STEP_STRING_FIELDS = (
    "next_step_family",
    "next_step_kind",
    "target_surface_family",
    "target_surface_path",
    "target_surface_id",
    "declared_purpose",
    "declared_expected_output_family",
    "requested_relation_to_basis",
)

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

PERMISSION_BOOL_FIELDS = (
    "read_permission_requested",
    "derive_permission_requested",
    "emit_permission_requested",
    "mutate_permission_requested",
    "replay_permission_requested",
    "merge_permission_requested",
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

PERFORMED_STEP_REQUIRED_FIELDS = (
    "performed_step_path",
    "performed_step_id",
    "performed_step_family",
    "performed_step_outcome",
    "performed_step_type",
    "performed_step_generated_at",
    "performed_step_resolver_or_emitter_module",
)

BLOCK_REASONS = {
    "ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED": (
        "The selected re-entry admissibility result is not REENTRY_ADMITTED."
    ),
    "ADMISSIBILITY_RESULT_UNREADABLE": (
        "The selected re-entry admissibility result could not be read."
    ),
    "ADMISSIBILITY_RESULT_MALFORMED": (
        "The selected re-entry admissibility result is malformed."
    ),
    "ADMISSIBILITY_RESULT_BASIS_THIN": (
        "The selected re-entry admissibility result does not preserve required basis."
    ),
    "LOCKED_ADMITTED_BASIS_MISSING": (
        "The selected re-entry admissibility result does not preserve the locked admitted basis."
    ),
    "LOCKED_ADMITTED_BASIS_MISMATCH": (
        "The receipt candidate shifts the locked admitted basis."
    ),
    "LOCKED_UPSTREAM_BASIS_UNREADABLE": (
        "A locked upstream basis path is not readable."
    ),
    "PERFORMED_STEP_MISSING": (
        "A performed-step candidate is required."
    ),
    "PERFORMED_STEP_UNREADABLE": (
        "The performed-step artifact could not be read."
    ),
    "PERFORMED_STEP_MALFORMED": (
        "The performed-step candidate is malformed."
    ),
    "PERFORMED_STEP_FAMILY_MISMATCH": (
        "The performed step does not match the admitted next-step family."
    ),
    "PERFORMED_STEP_KIND_MISMATCH": (
        "The performed step does not match the admitted next-step kind."
    ),
    "TARGET_SURFACE_MISMATCH": (
        "The performed step does not match the admitted target surface."
    ),
    "EXPECTED_OUTPUT_FAMILY_MISMATCH": (
        "The performed step does not match the admitted expected output family."
    ),
    "ADMISSION_SCOPE_EXCEEDED": (
        "The performed step exceeds the admitted single-step scope."
    ),
    "MUTATION_REPLAY_MERGE_DETECTED": (
        "The performed step indicates mutation, replay, or merge."
    ),
    "OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED": (
        "The performed step indicates overwrite, extra output, or broadened scope."
    ),
    "DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED": (
        "The performed step treats derivative, API, or operator-facing surfaces as authority."
    ),
    "CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES": (
        "The performed step or admission infers current/governing basis from derivative, API, or operator surfaces."
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
    "FOLLOW_ON_AUTHORIZATION_ATTEMPTED": (
        "Receipt attempts to authorize follow-on steps."
    ),
    "GENERAL_CONTINUATION_PERMISSION_ATTEMPTED": (
        "Receipt attempts to create general continuation permission."
    ),
    "ADMISSION_NOT_EXHAUSTED": (
        "Receipt does not prove the admission is exhausted."
    ),
    "REUSABLE_PERMISSION_IMPLIED": (
        "Receipt implies reusable admission permission."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "Receipt falls back to latest-file recency."
    ),
    "HUMAN_NARRATION_FALLBACK_REFUSED": (
        "Receipt falls back to human narration instead of bounded performed evidence."
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
    "operator_outputs_upgraded_to_source": False,
    "general_permission_created": False,
    "follow_on_steps_authorized": False,
    "admission_reusable": False,
    "self_orientation_became_authority": False,
    "reentry_admissibility_became_authority": False,
    "receipt_became_authority": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "next_organ_self_generated": False,
    "workflow_engine_created": False,
}

RECENCY_PHRASES = (
    "latest file",
    "newest file",
    "timestamp wins",
    "latest wins",
    "recency",
)

HUMAN_NARRATION_PHRASES = (
    "human narration",
    "external reader",
    "readme",
    "onboarding",
    "informal narration",
    "the step was done",
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

AUTHORITY_UPGRADE_PHRASES = (
    "as authority",
    "becomes authority",
    "source authority",
    "governing authority",
    "operator authority",
    "api authority",
    "vessel authority",
    "authority upgrade",
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
        raise CurrentSelfOrientationReentryReceiptError(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationReentryReceiptError(
            f"{context} is unreadable: {resolved}",
            missing_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationReentryReceiptError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise CurrentSelfOrientationReentryReceiptError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _require_mapping(value: Any, label: str, block_code: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise CurrentSelfOrientationReentryReceiptError(
            f"{label} must be an object",
            block_code,
        )
    return value


def _require_string(value: Any, label: str, block_code: str) -> str:
    text = _string_or_none(value)
    if text is None:
        raise CurrentSelfOrientationReentryReceiptError(
            f"{label} must be a non-empty string",
            block_code,
        )
    return text


def _require_bool(value: Any, label: str, block_code: str) -> bool:
    if not isinstance(value, bool):
        raise CurrentSelfOrientationReentryReceiptError(
            f"{label} must be a boolean",
            block_code,
        )
    return value


def _require_list(value: Any, label: str, block_code: str) -> list[Any]:
    if not isinstance(value, list):
        raise CurrentSelfOrientationReentryReceiptError(
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


def _path_equal(left: Any, right: Any) -> bool:
    left_text = _string_or_none(left)
    right_text = _string_or_none(right)
    if left_text is None or right_text is None:
        return False
    return left_text == right_text or _display_path(left_text) == _display_path(right_text)


def _path_under(path_text: Any, root_text: Any) -> bool:
    path = _string_or_none(path_text)
    root = _string_or_none(root_text)
    if path is None or root is None:
        return False
    clean_path = path.rstrip("/")
    clean_root = root.rstrip("/")
    return clean_path == clean_root or clean_path.startswith(clean_root + "/")


def _metadata(result: Mapping[str, Any]) -> Mapping[str, Any]:
    return _require_mapping(
        result.get("current_self_orientation_reentry_admissibility_metadata"),
        "current self-orientation re-entry admissibility metadata",
        "ADMISSIBILITY_RESULT_MALFORMED",
    )


def _load_admissibility_from_value(
    value: Any,
) -> tuple[dict[str, Any], Path | str | None, str]:
    if isinstance(value, Mapping):
        return _clone(dict(value)), None, "provided_reentry_admissibility_mapping"
    if isinstance(value, (str, Path)):
        return (
            _read_json_file(
                value,
                context="re-entry admissibility result",
                missing_code="ADMISSIBILITY_RESULT_UNREADABLE",
                malformed_code="ADMISSIBILITY_RESULT_MALFORMED",
            ),
            value,
            "explicit_reentry_admissibility_result_path",
        )
    if value is None:
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result is required",
            "ADMISSIBILITY_RESULT_UNREADABLE",
        )
    raise CurrentSelfOrientationReentryReceiptError(
        "re-entry admissibility result must be a mapping or JSON file path",
        "ADMISSIBILITY_RESULT_MALFORMED",
    )


def _candidate_payload(value: Mapping[str, Any]) -> Mapping[str, Any]:
    for key in (
        "performed_step_receipt_candidate",
        "performed_step",
        "selected_performed_step",
    ):
        section = value.get(key)
        if isinstance(section, Mapping):
            return section
    return value


def _nested_candidate_sections(value: Mapping[str, Any]) -> list[Mapping[str, Any]]:
    sections: list[Mapping[str, Any]] = [value]
    for key in (
        "performed_step_receipt_candidate",
        "performed_step",
        "selected_performed_step",
        "receipt_claims",
        "reentry_receipt_claims",
        "performed_step_claims",
        "receipt_posture",
    ):
        section = value.get(key)
        if isinstance(section, Mapping):
            sections.append(section)
    return sections


def _candidate_value(value: Mapping[str, Any], *keys: str) -> Any:
    for section in _nested_candidate_sections(value):
        for key in keys:
            if key in section:
                return section.get(key)
    return None


def _metadata_value(value: Mapping[str, Any], suffix: str) -> Any:
    for key, item in value.items():
        if key.endswith("_metadata") and isinstance(item, Mapping):
            for metadata_key, metadata_value in item.items():
                if metadata_key.endswith(suffix):
                    return metadata_value
    return None


def _load_performed_step(
    value: Any,
    *,
    path_hint: Path | str | None = None,
) -> tuple[dict[str, Any], Path | str | None, str]:
    if value is None and path_hint is None:
        raise CurrentSelfOrientationReentryReceiptError(
            "performed-step candidate is required",
            "PERFORMED_STEP_MISSING",
        )
    if isinstance(value, Mapping):
        return _clone(dict(value)), path_hint, "provided_performed_step_mapping"
    if isinstance(value, (str, Path)):
        return (
            _read_json_file(
                value,
                context="performed-step artifact",
                missing_code="PERFORMED_STEP_UNREADABLE",
                malformed_code="PERFORMED_STEP_MALFORMED",
            ),
            value,
            "explicit_performed_step_path",
        )
    if path_hint is not None:
        return (
            _read_json_file(
                path_hint,
                context="performed-step artifact",
                missing_code="PERFORMED_STEP_UNREADABLE",
                malformed_code="PERFORMED_STEP_MALFORMED",
            ),
            path_hint,
            "explicit_performed_step_path",
        )
    raise CurrentSelfOrientationReentryReceiptError(
        "performed-step candidate must be a mapping or JSON file path",
        "PERFORMED_STEP_MALFORMED",
    )


def _admitted_basis_from_performed_step(performed_step: Mapping[str, Any]) -> Mapping[str, Any] | None:
    basis = performed_step.get("admitted_reentry_basis")
    if isinstance(basis, Mapping):
        return basis
    payload = _candidate_payload(performed_step)
    basis = payload.get("admitted_reentry_basis") if isinstance(payload, Mapping) else None
    return basis if isinstance(basis, Mapping) else None


def _select_admissibility_from_performed_step(
    performed_step: Mapping[str, Any],
) -> tuple[dict[str, Any], Path | str | None, str]:
    basis = _admitted_basis_from_performed_step(performed_step)
    declared_path = (
        _string_or_none(basis.get("reentry_admissibility_result_path"))
        if isinstance(basis, Mapping)
        else None
    )
    if declared_path:
        return (
            _read_json_file(
                declared_path,
                context="declared re-entry admissibility result",
                missing_code="ADMISSIBILITY_RESULT_UNREADABLE",
                malformed_code="ADMISSIBILITY_RESULT_MALFORMED",
            ),
            declared_path,
            "performed_step_declared_reentry_admissibility_path",
        )

    root = _repo_path(REENTRY_ADMISSIBILITY_ROOT)
    if not root.is_dir():
        raise CurrentSelfOrientationReentryReceiptError(
            f"re-entry admissibility root is not readable: {root}",
            "ADMISSIBILITY_RESULT_UNREADABLE",
        )

    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(root.glob("*.json")):
        artifact = _read_json_file(
            path,
            context="candidate re-entry admissibility result",
            missing_code="ADMISSIBILITY_RESULT_UNREADABLE",
            malformed_code="ADMISSIBILITY_RESULT_MALFORMED",
        )
        try:
            metadata = _metadata(artifact)
        except CurrentSelfOrientationReentryReceiptError:
            continue
        if (
            artifact.get("outcome") == OUTCOME_REENTRY_ADMITTED
            and metadata.get("reentry_admissibility_result_type")
            == REENTRY_ADMISSIBILITY_RESULT_TYPE
        ):
            candidates.append((path, artifact))

    if not candidates:
        raise CurrentSelfOrientationReentryReceiptError(
            "no successful re-entry admissibility result is available",
            "ADMISSIBILITY_RESULT_UNREADABLE",
        )
    if len(candidates) > 1:
        raise CurrentSelfOrientationReentryReceiptError(
            "multiple admitted re-entry results require recency arbitration",
            "LATEST_FILE_RECENCY_REFUSED",
        )
    path, artifact = candidates[0]
    return artifact, path, "unique_successful_reentry_admissibility_discovery"


def _validate_locked_basis(locked_basis: Mapping[str, Any]) -> None:
    for field in LOCKED_BASIS_STRING_FIELDS:
        _require_string(
            locked_basis.get(field),
            f"locked_orientation_basis.{field}",
            "LOCKED_ADMITTED_BASIS_MISSING",
        )


def _validate_admitted_next_step(next_step: Mapping[str, Any]) -> None:
    for field in ADMITTED_NEXT_STEP_STRING_FIELDS:
        _require_string(
            next_step.get(field),
            f"declared_next_step.{field}",
            "ADMISSIBILITY_RESULT_BASIS_THIN",
        )


def _validate_scope_permissions_and_constraints(request: Mapping[str, Any]) -> None:
    scope = _require_mapping(
        request.get("declared_scope_bounds"),
        "declared_scope_bounds",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    for field in SCOPE_BOOL_FIELDS:
        _require_bool(scope.get(field), f"declared_scope_bounds.{field}", "ADMISSIBILITY_RESULT_BASIS_THIN")
    for field in SCOPE_LIST_FIELDS:
        _require_list(scope.get(field), f"declared_scope_bounds.{field}", "ADMISSIBILITY_RESULT_BASIS_THIN")

    hierarchy = _require_mapping(
        request.get("hierarchy_constraints"),
        "hierarchy_constraints",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    _require_string(
        hierarchy.get("current_governing_basis_source"),
        "hierarchy_constraints.current_governing_basis_source",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    for field in HIERARCHY_BOOL_FIELDS:
        _require_bool(hierarchy.get(field), f"hierarchy_constraints.{field}", "ADMISSIBILITY_RESULT_BASIS_THIN")

    correspondence = _require_mapping(
        request.get("correspondence_requirements"),
        "correspondence_requirements",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    for field in CORRESPONDENCE_BOOL_FIELDS:
        _require_bool(
            correspondence.get(field),
            f"correspondence_requirements.{field}",
            "ADMISSIBILITY_RESULT_BASIS_THIN",
        )

    permissions = _require_mapping(
        request.get("requested_permissions"),
        "requested_permissions",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    _require_string(
        permissions.get("authorization_scope"),
        "requested_permissions.authorization_scope",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    for field in PERMISSION_BOOL_FIELDS:
        _require_bool(permissions.get(field), f"requested_permissions.{field}", "ADMISSIBILITY_RESULT_BASIS_THIN")


def _validate_admissibility_result(result: Mapping[str, Any]) -> None:
    missing = sorted(REQUIRED_ADMISSIBILITY_TOP_LEVEL_KEYS - set(result))
    if missing:
        raise CurrentSelfOrientationReentryReceiptError(
            f"re-entry admissibility result is missing top-level sections: {missing}",
            "ADMISSIBILITY_RESULT_MALFORMED",
        )

    metadata = _metadata(result)
    for key in (
        "reentry_admissibility_result_id",
        "reentry_admissibility_result_type",
        "reentry_admissibility_result_version",
        "generated_at",
        "resolver_module",
    ):
        _require_string(metadata.get(key), f"metadata.{key}", "ADMISSIBILITY_RESULT_MALFORMED")
    if metadata.get("reentry_admissibility_result_type") != REENTRY_ADMISSIBILITY_RESULT_TYPE:
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result type is not recognized",
            "ADMISSIBILITY_RESULT_MALFORMED",
        )
    if metadata.get("resolver_module") != REENTRY_ADMISSIBILITY_RESOLVER_MODULE:
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result resolver module is not recognized",
            "ADMISSIBILITY_RESULT_MALFORMED",
        )
    if result.get("outcome") != OUTCOME_REENTRY_ADMITTED:
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result is not REENTRY_ADMITTED",
            "ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED",
        )
    block = _require_mapping(result.get("block"), "block", "ADMISSIBILITY_RESULT_MALFORMED")
    if block.get("block_code") is not None or block.get("block_reason") is not None:
        raise CurrentSelfOrientationReentryReceiptError(
            "admitted re-entry result carries a block",
            "ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED",
        )

    locked_basis = _require_mapping(
        result.get("locked_orientation_basis"),
        "locked_orientation_basis",
        "LOCKED_ADMITTED_BASIS_MISSING",
    )
    _validate_locked_basis(locked_basis)

    request = _require_mapping(
        result.get("selected_reentry_request"),
        "selected_reentry_request",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    next_step = _require_mapping(
        request.get("declared_next_step"),
        "declared_next_step",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    _validate_admitted_next_step(next_step)
    _validate_scope_permissions_and_constraints(request)

    basis = _require_mapping(
        result.get("reentry_admissibility_basis"),
        "reentry_admissibility_basis",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    if basis.get("admission_scope") != "single_declared_step_only":
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result is not single-step scoped",
            "ADMISSION_SCOPE_EXCEEDED",
        )
    if basis.get("self_orientation_remains_non_authoritative") is not True:
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility result upgrades self-orientation authority",
            "ADMISSIBILITY_RESULT_BASIS_THIN",
        )

    checks = _require_list(
        result.get("reentry_admissibility_checks"),
        "reentry_admissibility_checks",
        "ADMISSIBILITY_RESULT_MALFORMED",
    )
    if not checks or not all(isinstance(check, Mapping) and check.get("passed") is True for check in checks):
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry admissibility checks are missing or failed",
            "ADMISSIBILITY_RESULT_BASIS_THIN",
        )

    non_claims = _require_mapping(
        result.get("non_claims"),
        "non_claims",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key, value in non_claims.items():
        if not isinstance(key, str) or value is not False:
            raise CurrentSelfOrientationReentryReceiptError(
                f"admissibility non-claim is not false: {key}",
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )


def _identity_from_admissibility(
    result: Mapping[str, Any],
    path: Path | str | None,
    *,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _metadata(result)
    return {
        "result_path": _display_path(path),
        "result_id": metadata.get("reentry_admissibility_result_id"),
        "result_type": metadata.get("reentry_admissibility_result_type"),
        "result_version": metadata.get("reentry_admissibility_result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "outcome": result.get("outcome"),
        "selection_mode": selection_mode,
    }


def _empty_admissibility_identity() -> dict[str, Any]:
    return {
        "result_path": None,
        "result_id": None,
        "result_type": None,
        "result_version": None,
        "resolver_module": None,
        "outcome": None,
        "selection_mode": None,
    }


def _empty_performed_step_identity() -> dict[str, Any]:
    return {
        "performed_step_path": None,
        "performed_step_id": None,
        "performed_step_family": None,
        "performed_step_kind": None,
        "performed_step_outcome": None,
        "performed_step_type": None,
        "performed_step_generated_at": None,
        "performed_step_resolver_or_emitter_module": None,
        "target_surface_family": None,
        "target_surface_path": None,
        "target_surface_id": None,
        "declared_expected_output_family": None,
        "selection_mode": None,
    }


def _normalise_performed_step(
    raw: Mapping[str, Any],
    path: Path | str | None,
    *,
    selection_mode: str,
) -> dict[str, Any]:
    payload = _candidate_payload(raw)
    if not isinstance(payload, Mapping):
        raise CurrentSelfOrientationReentryReceiptError(
            "performed-step candidate must be an object",
            "PERFORMED_STEP_MALFORMED",
        )

    path_value = (
        _candidate_value(payload, "performed_step_path", "result_path", "artifact_path")
        or _display_path(path)
    )
    performed = {
        "performed_step_path": path_value,
        "performed_step_id": (
            _candidate_value(payload, "performed_step_id", "result_id", "artifact_id")
            or _metadata_value(raw, "_result_id")
        ),
        "performed_step_family": _candidate_value(
            payload,
            "performed_step_family",
            "next_step_family",
            "result_family",
            "artifact_family",
        ),
        "performed_step_kind": _candidate_value(
            payload,
            "performed_step_kind",
            "next_step_kind",
            "step_kind",
            "result_kind",
        ),
        "performed_step_outcome": (
            _candidate_value(payload, "performed_step_outcome", "result_outcome", "outcome")
            or raw.get("outcome")
        ),
        "performed_step_type": (
            _candidate_value(payload, "performed_step_type", "result_type", "artifact_type")
            or _metadata_value(raw, "_result_type")
        ),
        "performed_step_generated_at": (
            _candidate_value(payload, "performed_step_generated_at", "generated_at")
            or _metadata_value(raw, "generated_at")
        ),
        "performed_step_resolver_or_emitter_module": (
            _candidate_value(
                payload,
                "performed_step_resolver_or_emitter_module",
                "resolver_module",
                "emitter_module",
            )
            or _metadata_value(raw, "resolver_module")
        ),
        "target_surface_family": _candidate_value(
            payload,
            "target_surface_family",
            "performed_target_surface_family",
        ),
        "target_surface_path": _candidate_value(
            payload,
            "target_surface_path",
            "performed_target_surface_path",
        )
        or path_value,
        "target_surface_id": _candidate_value(
            payload,
            "target_surface_id",
            "performed_target_surface_id",
        )
        or _candidate_value(payload, "performed_step_id", "result_id", "artifact_id"),
        "declared_expected_output_family": _candidate_value(
            payload,
            "declared_expected_output_family",
            "performed_expected_output_family",
            "expected_output_family",
        ),
        "one_step_only": _candidate_value(payload, "one_step_only"),
        "additive_output_only": _candidate_value(payload, "additive_output_only"),
        "performed_output_paths": _candidate_value(payload, "performed_output_paths"),
        "extra_output_paths": _candidate_value(payload, "extra_output_paths"),
        "admission_exhausted": _candidate_value(
            payload,
            "admission_exhausted",
            "admission_consumed",
            "permission_exhausted",
        ),
        "admission_reusable": _candidate_value(
            payload,
            "admission_reusable",
            "permission_reusable",
        ),
        "reusable_permission_implied": _candidate_value(
            payload,
            "reusable_permission_implied",
        ),
        "follow_on_steps_authorized": _candidate_value(
            payload,
            "follow_on_steps_authorized",
            "follow_on_authorization_created",
        ),
        "general_permission_created": _candidate_value(
            payload,
            "general_permission_created",
            "general_continuation_permission_created",
        ),
        "mutation_performed": _candidate_value(payload, "mutation_performed"),
        "replay_performed": _candidate_value(payload, "replay_performed"),
        "merge_performed": _candidate_value(payload, "merge_performed"),
        "overwrite_performed": _candidate_value(
            payload,
            "overwrite_performed",
            "source_replaced",
        ),
        "scope_broadened": _candidate_value(
            payload,
            "scope_broadened",
            "broadened_scope",
        ),
        "derivative_api_operator_authority_upgraded": _candidate_value(
            payload,
            "derivative_api_operator_authority_upgraded",
            "derivative_api_operator_surfaces_treated_as_authority",
        ),
        "open_surfaces_remain_open": _candidate_value(payload, "open_surfaces_remain_open"),
        "open_surfaces_completed": _candidate_value(payload, "open_surfaces_completed"),
        "blocked_refused_surfaces_visible": _candidate_value(
            payload,
            "blocked_refused_surfaces_visible",
        ),
        "blocked_refused_surfaces_hidden": _candidate_value(
            payload,
            "blocked_refused_surfaces_hidden",
        ),
        "selection_mode": selection_mode,
    }
    non_claims = raw.get("non_claims")
    if isinstance(non_claims, Mapping):
        performed["non_claims"] = dict(non_claims)
    payload_non_claims = payload.get("non_claims")
    if isinstance(payload_non_claims, Mapping):
        performed["non_claims"] = dict(payload_non_claims)
    return performed


def _validate_performed_step(performed: Mapping[str, Any]) -> None:
    for field in PERFORMED_STEP_REQUIRED_FIELDS:
        _require_string(performed.get(field), field, "PERFORMED_STEP_MALFORMED")


def _performed_step_readability_checks(performed: Mapping[str, Any]) -> list[dict[str, Any]]:
    path_value = _string_or_none(performed.get("performed_step_path"))
    if path_value == "provided_mapping":
        passed = True
    elif path_value is None:
        passed = False
    else:
        passed = _repo_path(path_value).is_file()
    return [
        _check(
            "performed_step_exists_and_is_readable",
            passed,
            expected="existing performed-step path or provided mapping",
            actual=path_value,
            block_code="PERFORMED_STEP_UNREADABLE",
        )
    ]


def _locked_basis_candidate_from_performed_step(raw: Mapping[str, Any]) -> Mapping[str, Any] | None:
    for source in (raw, _candidate_payload(raw)):
        section = source.get("locked_admitted_basis") if isinstance(source, Mapping) else None
        if isinstance(section, Mapping):
            return section
    return None


def _admitted_next_step_candidate_from_performed_step(raw: Mapping[str, Any]) -> Mapping[str, Any] | None:
    for source in (raw, _candidate_payload(raw)):
        section = source.get("admitted_next_step") if isinstance(source, Mapping) else None
        if isinstance(section, Mapping):
            return section
    return None


def _admitted_basis_checks(
    selected_admissibility: Mapping[str, Any],
    raw_performed_step: Mapping[str, Any],
) -> list[dict[str, Any]]:
    basis = _admitted_basis_from_performed_step(raw_performed_step)
    if basis is None:
        return [
            _check(
                "admitted_reentry_basis_preserved_by_selected_admissibility_result",
                True,
                expected="selected admissibility result supplies admitted basis",
                actual="not repeated by performed-step candidate",
                block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
            )
        ]

    checks = [
        _check(
            "admitted_reentry_basis_id_matches_selected_admissibility",
            basis.get("reentry_admissibility_result_id")
            == selected_admissibility.get("result_id"),
            expected=selected_admissibility.get("result_id"),
            actual=basis.get("reentry_admissibility_result_id"),
            block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
        ),
        _check(
            "admitted_reentry_basis_path_matches_selected_admissibility",
            _path_equal(
                basis.get("reentry_admissibility_result_path"),
                selected_admissibility.get("result_path"),
            ),
            expected=selected_admissibility.get("result_path"),
            actual=basis.get("reentry_admissibility_result_path"),
            block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
        ),
        _check(
            "admitted_reentry_basis_outcome_is_reentry_admitted",
            basis.get("reentry_admissibility_outcome") == OUTCOME_REENTRY_ADMITTED,
            expected=OUTCOME_REENTRY_ADMITTED,
            actual=basis.get("reentry_admissibility_outcome"),
            block_code="ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED",
        ),
        _check(
            "admitted_reentry_basis_resolver_module_matches",
            basis.get("reentry_admissibility_resolver_module")
            == REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
            expected=REENTRY_ADMISSIBILITY_RESOLVER_MODULE,
            actual=basis.get("reentry_admissibility_resolver_module"),
            block_code="ADMISSIBILITY_RESULT_MALFORMED",
        ),
    ]
    return checks


def _locked_basis_checks(
    locked_basis: Mapping[str, Any],
    raw_performed_step: Mapping[str, Any],
) -> list[dict[str, Any]]:
    candidate_locked = _locked_basis_candidate_from_performed_step(raw_performed_step)
    if candidate_locked is None:
        checks = [
            _check(
                "locked_admitted_basis_preserved_from_admissibility_result",
                True,
                expected="selected admissibility locked basis",
                actual="not repeated by performed-step candidate",
                block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
            )
        ]
    else:
        checks = [
            _check(
                f"locked_{field}_matches_admissibility_result",
                _path_equal(candidate_locked.get(field), locked_basis.get(field))
                if field.endswith("_path")
                else candidate_locked.get(field) == locked_basis.get(field),
                expected=locked_basis.get(field),
                actual=candidate_locked.get(field),
                block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
            )
            for field in LOCKED_BASIS_STRING_FIELDS
        ]
    checks.append(
        _check(
            "locked_admitted_basis_matches_selected_admissibility_result",
            all(check.get("passed") is True for check in checks),
            expected="performed candidate does not shift locked admitted basis",
            actual=[
                check.get("check_name")
                for check in checks
                if check.get("passed") is not True
            ],
            block_code="LOCKED_ADMITTED_BASIS_MISMATCH",
        )
    )
    return checks


def _locked_basis_readability_checks(locked_basis: Mapping[str, Any]) -> list[dict[str, Any]]:
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
                expected="existing path from locked admitted basis",
                actual=path_value,
                block_code="LOCKED_UPSTREAM_BASIS_UNREADABLE",
            )
        )
    return checks


def _admitted_next_step_checks(
    admitted_next_step: Mapping[str, Any],
    raw_performed_step: Mapping[str, Any],
) -> list[dict[str, Any]]:
    candidate_next_step = _admitted_next_step_candidate_from_performed_step(raw_performed_step)
    if candidate_next_step is None:
        return [
            _check(
                "admitted_next_step_preserved_from_admissibility_result",
                True,
                expected="selected admissibility declared next step",
                actual="not repeated by performed-step candidate",
                block_code="TARGET_SURFACE_MISMATCH",
            )
        ]
    checks = []
    for field in ADMITTED_NEXT_STEP_STRING_FIELDS:
        expected = admitted_next_step.get(field)
        actual = candidate_next_step.get(field)
        code = "TARGET_SURFACE_MISMATCH"
        if field == "next_step_family":
            code = "PERFORMED_STEP_FAMILY_MISMATCH"
        elif field == "next_step_kind":
            code = "PERFORMED_STEP_KIND_MISMATCH"
        elif field == "declared_expected_output_family":
            code = "EXPECTED_OUTPUT_FAMILY_MISMATCH"
        checks.append(
            _check(
                f"admitted_next_step_{field}_matches_admissibility_result",
                _path_equal(actual, expected) if field.endswith("_path") else actual == expected,
                expected=expected,
                actual=actual,
                block_code=code,
            )
        )
    return checks


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _output_path_is_allowed(
    performed_path: Any,
    admitted_next_step: Mapping[str, Any],
    scope: Mapping[str, Any],
) -> bool:
    path_value = _string_or_none(performed_path)
    if path_value is None:
        return False
    target_path = admitted_next_step.get("target_surface_path")
    if _path_equal(path_value, target_path):
        return True
    for allowed in _as_list(scope.get("allowed_new_file_paths")):
        if _path_equal(path_value, allowed):
            return True
    for root in _as_list(scope.get("allowed_artifact_output_roots")):
        if _path_under(path_value, root):
            return True
    return False


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


def _performed_step_correspondence_checks(
    admitted_next_step: Mapping[str, Any],
    scope: Mapping[str, Any],
    permissions: Mapping[str, Any],
    performed: Mapping[str, Any],
) -> list[dict[str, Any]]:
    performed_output_paths = _as_list(performed.get("performed_output_paths"))
    extra_output_paths = _as_list(performed.get("extra_output_paths"))
    output_paths = performed_output_paths or [performed.get("performed_step_path")]
    output_target_count = len(_as_list(scope.get("allowed_new_file_paths"))) + len(
        _as_list(scope.get("allowed_artifact_output_roots"))
    )
    emit_requested = permissions.get("emit_permission_requested") is True

    return [
        _check(
            "performed_step_matches_admitted_next_step_family",
            performed.get("performed_step_family") == admitted_next_step.get("next_step_family"),
            expected=admitted_next_step.get("next_step_family"),
            actual=performed.get("performed_step_family"),
            block_code="PERFORMED_STEP_FAMILY_MISMATCH",
        ),
        _check(
            "performed_step_matches_admitted_next_step_kind",
            performed.get("performed_step_kind") == admitted_next_step.get("next_step_kind"),
            expected=admitted_next_step.get("next_step_kind"),
            actual=performed.get("performed_step_kind"),
            block_code="PERFORMED_STEP_KIND_MISMATCH",
        ),
        _check(
            "target_surface_family_matches_admitted_next_step",
            performed.get("target_surface_family") == admitted_next_step.get("target_surface_family"),
            expected=admitted_next_step.get("target_surface_family"),
            actual=performed.get("target_surface_family"),
            block_code="TARGET_SURFACE_MISMATCH",
        ),
        _check(
            "target_surface_path_matches_admitted_next_step",
            _path_equal(performed.get("target_surface_path"), admitted_next_step.get("target_surface_path")),
            expected=admitted_next_step.get("target_surface_path"),
            actual=performed.get("target_surface_path"),
            block_code="TARGET_SURFACE_MISMATCH",
        ),
        _check(
            "target_surface_id_matches_admitted_next_step",
            performed.get("target_surface_id") == admitted_next_step.get("target_surface_id"),
            expected=admitted_next_step.get("target_surface_id"),
            actual=performed.get("target_surface_id"),
            block_code="TARGET_SURFACE_MISMATCH",
        ),
        _check(
            "performed_step_matches_admitted_expected_output_family",
            performed.get("declared_expected_output_family")
            == admitted_next_step.get("declared_expected_output_family"),
            expected=admitted_next_step.get("declared_expected_output_family"),
            actual=performed.get("declared_expected_output_family"),
            block_code="EXPECTED_OUTPUT_FAMILY_MISMATCH",
        ),
        _check(
            "admission_scope_is_single_step",
            scope.get("one_step_only") is True,
            expected=True,
            actual=scope.get("one_step_only"),
            block_code="ADMISSION_SCOPE_EXCEEDED",
        ),
        _check(
            "performed_step_remains_one_step_only",
            performed.get("one_step_only") in {None, True},
            expected=True,
            actual=performed.get("one_step_only"),
            block_code="ADMISSION_SCOPE_EXCEEDED",
        ),
        _check(
            "performed_step_output_is_additive_only",
            scope.get("additive_output_only") is True
            and performed.get("additive_output_only") in {None, True},
            expected=True,
            actual={
                "admitted_additive_output_only": scope.get("additive_output_only"),
                "performed_additive_output_only": performed.get("additive_output_only"),
            },
            block_code="OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED",
        ),
        _check(
            "output_scope_is_one_admitted_additive_target",
            (not emit_requested and output_target_count == 0)
            or (emit_requested and output_target_count == 1),
            expected="one additive output target when emit was admitted",
            actual={
                "emit_permission_requested": emit_requested,
                "allowed_new_file_paths": scope.get("allowed_new_file_paths"),
                "allowed_artifact_output_roots": scope.get("allowed_artifact_output_roots"),
            },
            block_code="ADMISSION_SCOPE_EXCEEDED",
        ),
        _check(
            "performed_output_path_stays_inside_admitted_output_scope",
            all(_output_path_is_allowed(path, admitted_next_step, scope) for path in output_paths),
            expected="performed path equals admitted target or allowed output root",
            actual=output_paths,
            block_code="OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED",
        ),
        _check(
            "performed_step_has_no_extra_outputs",
            not extra_output_paths and len(output_paths) == 1,
            expected="exactly one performed output and no extra outputs",
            actual={
                "performed_output_paths": output_paths,
                "extra_output_paths": extra_output_paths,
            },
            block_code="OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED",
        ),
    ]


def _mutation_and_broadening_checks(
    permissions: Mapping[str, Any],
    performed: Mapping[str, Any],
) -> list[dict[str, Any]]:
    return [
        _check(
            "no_mutation_was_admitted_or_performed",
            permissions.get("mutate_permission_requested") is False
            and performed.get("mutation_performed") in {None, False},
            expected=False,
            actual={
                "admitted_mutate_permission": permissions.get("mutate_permission_requested"),
                "performed_mutation": performed.get("mutation_performed"),
            },
            block_code="MUTATION_REPLAY_MERGE_DETECTED",
        ),
        _check(
            "no_replay_was_admitted_or_performed",
            permissions.get("replay_permission_requested") is False
            and performed.get("replay_performed") in {None, False},
            expected=False,
            actual={
                "admitted_replay_permission": permissions.get("replay_permission_requested"),
                "performed_replay": performed.get("replay_performed"),
            },
            block_code="MUTATION_REPLAY_MERGE_DETECTED",
        ),
        _check(
            "no_merge_was_admitted_or_performed",
            permissions.get("merge_permission_requested") is False
            and performed.get("merge_performed") in {None, False},
            expected=False,
            actual={
                "admitted_merge_permission": permissions.get("merge_permission_requested"),
                "performed_merge": performed.get("merge_performed"),
            },
            block_code="MUTATION_REPLAY_MERGE_DETECTED",
        ),
        _check(
            "no_overwrite_source_replacement_or_scope_broadening_occurred",
            performed.get("overwrite_performed") in {None, False}
            and performed.get("scope_broadened") in {None, False},
            expected=False,
            actual={
                "overwrite_performed": performed.get("overwrite_performed"),
                "scope_broadened": performed.get("scope_broadened"),
            },
            block_code="OVERWRITE_EXTRA_OUTPUT_OR_BROADENED_SCOPE_DETECTED",
        ),
    ]


def _hierarchy_checks(
    request: Mapping[str, Any],
    performed: Mapping[str, Any],
    raw_performed_step: Mapping[str, Any],
) -> list[dict[str, Any]]:
    hierarchy = _require_mapping(
        request.get("hierarchy_constraints"),
        "hierarchy_constraints",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    text = _text_blob(raw_performed_step, performed)
    return [
        _check(
            "current_governing_basis_remains_upstream",
            "upstream" in str(hierarchy.get("current_governing_basis_source", "")).lower()
            or "current" in str(hierarchy.get("current_governing_basis_source", "")).lower()
            or "effective" in str(hierarchy.get("current_governing_basis_source", "")).lower(),
            expected="upstream current/effective/governing/current-state basis",
            actual=hierarchy.get("current_governing_basis_source"),
            block_code="CURRENT_GOVERNING_BASIS_INFERRED_FROM_DERIVATIVE_API_OPERATOR_SURFACES",
        ),
        _check(
            "derivative_api_operator_surfaces_remain_downstream",
            hierarchy.get("derivative_surfaces_allowed_as_basis") is False
            and hierarchy.get("operator_surfaces_allowed_as_basis") is False
            and performed.get("derivative_api_operator_authority_upgraded") in {None, False}
            and not any(phrase in text for phrase in AUTHORITY_UPGRADE_PHRASES),
            expected="derivative/API/operator surfaces do not become authority",
            actual={
                "derivative_surfaces_allowed_as_basis": hierarchy.get(
                    "derivative_surfaces_allowed_as_basis"
                ),
                "operator_surfaces_allowed_as_basis": hierarchy.get(
                    "operator_surfaces_allowed_as_basis"
                ),
                "performed_authority_upgrade": performed.get(
                    "derivative_api_operator_authority_upgraded"
                ),
            },
            block_code="DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED",
        ),
        _check(
            "admissibility_and_self_orientation_remain_non_authoritative",
            hierarchy.get("self_orientation_allowed_as_authority") is False,
            expected=False,
            actual=hierarchy.get("self_orientation_allowed_as_authority"),
            block_code="DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED",
        ),
        _check(
            "currentness_is_not_inferred_by_recency",
            hierarchy.get("currentness_may_be_inferred_by_recency") is False
            and not any(phrase in text for phrase in RECENCY_PHRASES),
            expected=False,
            actual={
                "currentness_may_be_inferred_by_recency": hierarchy.get(
                    "currentness_may_be_inferred_by_recency"
                ),
                "performed_text": text,
            },
            block_code="LATEST_FILE_RECENCY_REFUSED",
        ),
    ]


def _correspondence_and_non_claim_checks(
    request: Mapping[str, Any],
    admission_non_claims: Mapping[str, Any],
    performed: Mapping[str, Any],
    raw_performed_step: Mapping[str, Any],
) -> list[dict[str, Any]]:
    correspondence = _require_mapping(
        request.get("correspondence_requirements"),
        "correspondence_requirements",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    performed_non_claims = performed.get("non_claims")
    performed_non_claims = performed_non_claims if isinstance(performed_non_claims, Mapping) else {}
    text = _text_blob(raw_performed_step, performed)
    return [
        _check(
            "open_surfaces_remain_open",
            correspondence.get("must_preserve_open_surfaces") is True
            and performed.get("open_surfaces_completed") in {None, False}
            and performed.get("open_surfaces_remain_open") in {None, True},
            expected="open posture remains open",
            actual={
                "must_preserve_open_surfaces": correspondence.get("must_preserve_open_surfaces"),
                "open_surfaces_completed": performed.get("open_surfaces_completed"),
                "open_surfaces_remain_open": performed.get("open_surfaces_remain_open"),
            },
            block_code="OPEN_SURFACE_TREATED_AS_COMPLETED",
        ),
        _check(
            "blocked_refused_surfaces_remain_visible",
            correspondence.get("must_preserve_blocked_refused_surfaces") is True
            and performed.get("blocked_refused_surfaces_hidden") in {None, False}
            and performed.get("blocked_refused_surfaces_visible") in {None, True},
            expected="blocked/refused posture remains visible",
            actual={
                "must_preserve_blocked_refused_surfaces": correspondence.get(
                    "must_preserve_blocked_refused_surfaces"
                ),
                "blocked_refused_surfaces_hidden": performed.get(
                    "blocked_refused_surfaces_hidden"
                ),
                "blocked_refused_surfaces_visible": performed.get(
                    "blocked_refused_surfaces_visible"
                ),
            },
            block_code="BLOCKED_REFUSED_SURFACE_HIDDEN",
        ),
        _check(
            "derivative_source_distinction_is_preserved",
            correspondence.get("must_preserve_derivative_source_distinction") is True,
            expected=True,
            actual=correspondence.get("must_preserve_derivative_source_distinction"),
            block_code="DERIVATIVE_API_OPERATOR_AUTHORITY_REFUSED",
        ),
        _check(
            "admissibility_non_claims_remain_false",
            correspondence.get("must_preserve_non_claims") is True
            and all(value is False for value in admission_non_claims.values()),
            expected=False,
            actual=dict(admission_non_claims),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "performed_step_non_claims_do_not_flip",
            all(value is False for value in performed_non_claims.values()),
            expected=False,
            actual=dict(performed_non_claims),
            block_code="NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "receipt_does_not_fall_back_to_human_narration",
            not any(phrase in text for phrase in HUMAN_NARRATION_PHRASES),
            expected="bounded performed evidence, not narration",
            actual=text,
            block_code="HUMAN_NARRATION_FALLBACK_REFUSED",
        ),
        _check(
            "receipt_does_not_become_roadmap_autonomy_or_signaling",
            not any(phrase in text for phrase in ROADMAP_AUTONOMY_PHRASES),
            expected="no roadmap/autonomy/signaling/workflow language",
            actual=text,
            block_code="GENERAL_CONTINUATION_PERMISSION_ATTEMPTED",
        ),
    ]


def _exhaustion_checks(performed: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        _check(
            "admission_is_exhausted_by_this_performance",
            performed.get("admission_exhausted") is True,
            expected=True,
            actual=performed.get("admission_exhausted"),
            block_code="ADMISSION_NOT_EXHAUSTED",
        ),
        _check(
            "admission_is_not_reusable_after_receipt",
            performed.get("admission_reusable") in {None, False}
            and performed.get("reusable_permission_implied") in {None, False},
            expected=False,
            actual={
                "admission_reusable": performed.get("admission_reusable"),
                "reusable_permission_implied": performed.get("reusable_permission_implied"),
            },
            block_code="REUSABLE_PERMISSION_IMPLIED",
        ),
        _check(
            "receipt_does_not_authorize_follow_on_steps",
            performed.get("follow_on_steps_authorized") in {None, False},
            expected=False,
            actual=performed.get("follow_on_steps_authorized"),
            block_code="FOLLOW_ON_AUTHORIZATION_ATTEMPTED",
        ),
        _check(
            "receipt_does_not_create_general_continuation_permission",
            performed.get("general_permission_created") in {None, False},
            expected=False,
            actual=performed.get("general_permission_created"),
            block_code="GENERAL_CONTINUATION_PERMISSION_ATTEMPTED",
        ),
    ]


def _merged_non_claims(
    admissibility_result: Mapping[str, Any] | None,
    performed: Mapping[str, Any] | None = None,
) -> dict[str, bool]:
    merged = dict(RESULT_NON_CLAIM_DEFAULTS)
    for source in (
        admissibility_result.get("non_claims") if isinstance(admissibility_result, Mapping) else None,
        performed.get("non_claims") if isinstance(performed, Mapping) else None,
    ):
        if isinstance(source, Mapping):
            for key, value in source.items():
                if isinstance(key, str) and value is False:
                    merged[key] = False
    return merged


def _result_id(selected_admissibility: Mapping[str, Any], outcome: str) -> str:
    base = _string_or_none(selected_admissibility.get("result_id"))
    if base is None:
        base = "no_selected_reentry_admissibility_result"
    suffix = "reentry_received" if outcome == OUTCOME_REENTRY_RECEIVED else "reentry_receipt_blocked"
    return f"{base}__{suffix}"


def _result_metadata(selected_admissibility: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    return {
        "reentry_receipt_result_id": _result_id(selected_admissibility, outcome),
        "reentry_receipt_result_type": REENTRY_RECEIPT_RESULT_TYPE,
        "reentry_receipt_result_version": REENTRY_RECEIPT_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _build_result(
    *,
    selected_admissibility: Mapping[str, Any],
    locked_admitted_basis: Mapping[str, Any],
    admitted_next_step: Mapping[str, Any],
    selected_performed_step: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    result = {
        "current_self_orientation_reentry_receipt_metadata": _result_metadata(
            selected_admissibility,
            outcome,
        ),
        "selected_reentry_admissibility_result": dict(selected_admissibility),
        "locked_admitted_basis": _clone(dict(locked_admitted_basis)),
        "selected_performed_step": _clone(dict(selected_performed_step)),
        "reentry_receipt_checks": [dict(check) for check in checks],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "reentry_receipt_basis": {
            "basis_kind": "single_reentry_admissibility_result_plus_single_performed_step",
            "selected_reentry_admissibility_result_id": selected_admissibility.get("result_id"),
            "selected_reentry_admissibility_result_path": selected_admissibility.get("result_path"),
            "selected_body_pass_result_id": locked_admitted_basis.get("selected_body_pass_result_id"),
            "selected_source_surface_id": locked_admitted_basis.get("selected_source_surface_id"),
            "selected_current_state_answer_read_id": locked_admitted_basis.get(
                "selected_current_state_answer_read_id"
            ),
            "selected_what_stands_now_id": locked_admitted_basis.get("selected_what_stands_now_id"),
            "admitted_next_step_family": admitted_next_step.get("next_step_family"),
            "admitted_next_step_kind": admitted_next_step.get("next_step_kind"),
            "performed_step_id": selected_performed_step.get("performed_step_id"),
            "performed_step_path": selected_performed_step.get("performed_step_path"),
            "performed_step_family": selected_performed_step.get("performed_step_family"),
            "performed_step_kind": selected_performed_step.get("performed_step_kind"),
            "receipt_scope": "single_admitted_step_only",
            "admission_exhausted": outcome == OUTCOME_REENTRY_RECEIVED,
            "admissibility_remains_non_authoritative": True,
            "receipt_creates_follow_on_permission": False,
        },
        "current_self_orientation_reentry_receipt_summary": {},
        "non_claims": dict(non_claims),
    }
    result["current_self_orientation_reentry_receipt_summary"] = (
        build_current_self_orientation_reentry_receipt_summary(result)
    )
    return result


def _blocked_result(
    *,
    selected_admissibility: Mapping[str, Any] | None = None,
    locked_admitted_basis: Mapping[str, Any] | None = None,
    admitted_next_step: Mapping[str, Any] | None = None,
    selected_performed_step: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    block_code: str,
    block_detail: str | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _build_result(
        selected_admissibility=selected_admissibility or _empty_admissibility_identity(),
        locked_admitted_basis=locked_admitted_basis or {},
        admitted_next_step=admitted_next_step or {},
        selected_performed_step=selected_performed_step or _empty_performed_step_identity(),
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        non_claims=non_claims or dict(RESULT_NON_CLAIM_DEFAULTS),
    )


def _resolve_internal(
    reentry_admissibility_result: Any,
    performed_step: Any,
    *,
    performed_step_path_hint: Path | str | None = None,
) -> dict[str, Any]:
    if reentry_admissibility_result is None:
        raw_performed_step, performed_path, performed_selection = _load_performed_step(
            performed_step,
            path_hint=performed_step_path_hint,
        )
        admission, admission_path, admission_selection = _select_admissibility_from_performed_step(
            raw_performed_step
        )
    else:
        admission, admission_path, admission_selection = _load_admissibility_from_value(
            reentry_admissibility_result
        )
        _validate_admissibility_result(admission)
        raw_performed_step, performed_path, performed_selection = _load_performed_step(
            performed_step,
            path_hint=performed_step_path_hint,
        )

    _validate_admissibility_result(admission)
    selected_admissibility = _identity_from_admissibility(
        admission,
        admission_path,
        selection_mode=admission_selection,
    )
    locked_basis = _require_mapping(
        admission.get("locked_orientation_basis"),
        "locked_orientation_basis",
        "LOCKED_ADMITTED_BASIS_MISSING",
    )
    request = _require_mapping(
        admission.get("selected_reentry_request"),
        "selected_reentry_request",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    admitted_next_step = _require_mapping(
        request.get("declared_next_step"),
        "declared_next_step",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    scope = _require_mapping(
        request.get("declared_scope_bounds"),
        "declared_scope_bounds",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    permissions = _require_mapping(
        request.get("requested_permissions"),
        "requested_permissions",
        "ADMISSIBILITY_RESULT_BASIS_THIN",
    )
    admission_non_claims = _require_mapping(
        admission.get("non_claims"),
        "non_claims",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )

    performed = _normalise_performed_step(
        raw_performed_step,
        performed_path,
        selection_mode=performed_selection,
    )
    _validate_performed_step(performed)
    non_claims = _merged_non_claims(admission, performed)

    checks: list[dict[str, Any]] = [
        _check(
            "admissibility_result_is_reentry_admitted",
            admission.get("outcome") == OUTCOME_REENTRY_ADMITTED,
            expected=OUTCOME_REENTRY_ADMITTED,
            actual=admission.get("outcome"),
            block_code="ADMISSIBILITY_RESULT_NOT_REENTRY_ADMITTED",
        ),
        _check(
            "admissibility_result_preserves_required_sections",
            True,
            expected=sorted(REQUIRED_ADMISSIBILITY_TOP_LEVEL_KEYS),
            actual=sorted(admission),
            block_code="ADMISSIBILITY_RESULT_BASIS_THIN",
        ),
    ]
    checks.extend(_admitted_basis_checks(selected_admissibility, raw_performed_step))
    checks.extend(_locked_basis_checks(locked_basis, raw_performed_step))
    checks.extend(_locked_basis_readability_checks(locked_basis))
    checks.extend(_admitted_next_step_checks(admitted_next_step, raw_performed_step))
    checks.extend(_performed_step_readability_checks(performed))
    checks.extend(
        _performed_step_correspondence_checks(
            admitted_next_step,
            scope,
            permissions,
            performed,
        )
    )
    checks.extend(_mutation_and_broadening_checks(permissions, performed))
    checks.extend(_hierarchy_checks(request, performed, raw_performed_step))
    checks.extend(
        _correspondence_and_non_claim_checks(
            request,
            admission_non_claims,
            performed,
            raw_performed_step,
        )
    )
    checks.extend(_exhaustion_checks(performed))

    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            selected_admissibility=selected_admissibility,
            locked_admitted_basis=locked_basis,
            admitted_next_step=admitted_next_step,
            selected_performed_step=performed,
            checks=checks,
            block_code=_string_or_none(failed.get("block_code"))
            or "ADMISSION_SCOPE_EXCEEDED",
            block_detail=f"failed check: {failed.get('check_name')}",
            non_claims=non_claims,
        )

    return _build_result(
        selected_admissibility=selected_admissibility,
        locked_admitted_basis=locked_basis,
        admitted_next_step=admitted_next_step,
        selected_performed_step=performed,
        checks=checks,
        outcome=OUTCOME_REENTRY_RECEIVED,
        block_code=None,
        block_detail=None,
        non_claims=non_claims,
    )


def resolve_current_self_orientation_reentry_receipt(
    reentry_admissibility_result: Mapping[str, Any] | None = None,
    performed_step: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded re-entry receipt/refusal decision."""

    try:
        return _resolve_internal(reentry_admissibility_result, performed_step)
    except CurrentSelfOrientationReentryReceiptError as exc:
        selected_admissibility = _empty_admissibility_identity()
        locked_basis: Mapping[str, Any] = {}
        admitted_next_step: Mapping[str, Any] = {}
        selected_performed = _empty_performed_step_identity()
        non_claims = dict(RESULT_NON_CLAIM_DEFAULTS)

        if isinstance(reentry_admissibility_result, Mapping):
            try:
                selected_admissibility = _identity_from_admissibility(
                    reentry_admissibility_result,
                    None,
                    selection_mode="provided_reentry_admissibility_mapping",
                )
                maybe_locked = reentry_admissibility_result.get("locked_orientation_basis")
                if isinstance(maybe_locked, Mapping):
                    locked_basis = maybe_locked
                maybe_request = reentry_admissibility_result.get("selected_reentry_request")
                if isinstance(maybe_request, Mapping):
                    maybe_next = maybe_request.get("declared_next_step")
                    if isinstance(maybe_next, Mapping):
                        admitted_next_step = maybe_next
                non_claims = _merged_non_claims(reentry_admissibility_result)
            except CurrentSelfOrientationReentryReceiptError:
                selected_admissibility = _empty_admissibility_identity()
        if isinstance(performed_step, Mapping):
            try:
                selected_performed = _normalise_performed_step(
                    performed_step,
                    None,
                    selection_mode="provided_performed_step_mapping",
                )
                non_claims = _merged_non_claims(reentry_admissibility_result, selected_performed)
            except CurrentSelfOrientationReentryReceiptError:
                selected_performed = _empty_performed_step_identity()

        return _blocked_result(
            selected_admissibility=selected_admissibility,
            locked_admitted_basis=locked_basis,
            admitted_next_step=admitted_next_step,
            selected_performed_step=selected_performed,
            block_code=exc.block_code,
            block_detail=str(exc),
            non_claims=non_claims,
        )


def resolve_current_self_orientation_reentry_receipt_from_path(
    reentry_admissibility_result_path: Path | str,
    performed_step_path: Path | str | None = None,
    performed_step: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve re-entry receipt from explicit admissibility and performed-step paths."""

    performed_value: Any = performed_step if performed_step is not None else performed_step_path
    try:
        return _resolve_internal(
            reentry_admissibility_result_path,
            performed_value,
            performed_step_path_hint=performed_step_path if performed_step is not None else None,
        )
    except CurrentSelfOrientationReentryReceiptError as exc:
        selected_performed = _empty_performed_step_identity()
        if isinstance(performed_step, Mapping):
            try:
                selected_performed = _normalise_performed_step(
                    performed_step,
                    performed_step_path,
                    selection_mode="provided_performed_step_mapping",
                )
            except CurrentSelfOrientationReentryReceiptError:
                selected_performed = _empty_performed_step_identity()
        elif performed_step_path is not None:
            selected_performed = {
                **_empty_performed_step_identity(),
                "performed_step_path": _display_path(performed_step_path),
                "selection_mode": "explicit_performed_step_path",
            }
        return _blocked_result(
            selected_admissibility={
                **_empty_admissibility_identity(),
                "result_path": _display_path(reentry_admissibility_result_path),
                "selection_mode": "explicit_reentry_admissibility_result_path",
            },
            selected_performed_step=selected_performed,
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


def build_current_self_orientation_reentry_receipt_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a bounded summary for one re-entry receipt result."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry receipt result must be a mapping",
            "PERFORMED_STEP_MALFORMED",
        )
    selected_admission = result.get("selected_reentry_admissibility_result")
    selected_admission = selected_admission if isinstance(selected_admission, Mapping) else {}
    locked = result.get("locked_admitted_basis")
    locked = locked if isinstance(locked, Mapping) else {}
    performed = result.get("selected_performed_step")
    performed = performed if isinstance(performed, Mapping) else {}
    checks = result.get("reentry_receipt_checks")
    checks = checks if isinstance(checks, list) else []
    block = result.get("block")
    block = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims = non_claims if isinstance(non_claims, Mapping) else {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_reentry_admissibility_result_id": selected_admission.get("result_id"),
        "selected_reentry_admissibility_result_path": selected_admission.get("result_path"),
        "locked_selected_body_pass_result_id": locked.get("selected_body_pass_result_id"),
        "locked_selected_source_surface_id": locked.get("selected_source_surface_id"),
        "locked_selected_current_state_answer_read_id": locked.get(
            "selected_current_state_answer_read_id"
        ),
        "locked_selected_what_stands_now_id": locked.get("selected_what_stands_now_id"),
        "performed_step_family": performed.get("performed_step_family"),
        "performed_step_kind": performed.get("performed_step_kind"),
        "performed_step_outcome": performed.get("performed_step_outcome"),
        "basis_lock_matched": _check_family_passed(
            checks,
            (
                "admitted_reentry_basis",
                "locked_",
            ),
        ),
        "performed_step_correspondence_passed": _check_family_passed(
            checks,
            (
                "performed_step_matches",
                "target_surface",
                "performed_step_matches_admitted_expected",
            ),
        ),
        "scope_stayed_single_step_and_additive": _check_family_passed(
            checks,
            (
                "admission_scope",
                "performed_step_remains",
                "performed_step_output",
                "output_scope",
                "performed_output",
                "no_mutation",
                "no_replay",
                "no_merge",
                "no_overwrite",
            ),
        ),
        "exhaustion_closure_passed": _check_family_passed(
            checks,
            (
                "admission_is_exhausted",
                "admission_is_not_reusable",
                "receipt_does_not_authorize",
                "receipt_does_not_create",
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
                "operator_outputs_upgraded_to_source",
                "general_permission_created",
                "follow_on_steps_authorized",
                "admission_reusable",
                "reentry_admissibility_became_authority",
                "receipt_became_authority",
                "latest_file_currentness",
                "recency_fraud",
                "mutation_performed",
                "replay_performed",
                "merge_performed",
                "roadmap_generated",
                "workflow_engine_created",
            )
            if key in non_claims
        },
    }


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT,
) -> Path:
    selected = result.get("selected_reentry_admissibility_result")
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
    raise CurrentSelfOrientationReentryReceiptError(
        "no bounded re-entry receipt filename is available",
        "PERFORMED_STEP_MALFORMED",
    )


def write_current_self_orientation_reentry_receipt_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive re-entry receipt JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationReentryReceiptError(
            "re-entry receipt result must be a mapping",
            "PERFORMED_STEP_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"current self-orientation re-entry receipt result already exists: {target}"
        )
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
