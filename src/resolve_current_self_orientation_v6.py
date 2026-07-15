"""Resolve bounded current self-orientation with vessel-relation posture.

This successor preserves the v5 self-orientation model and adds one narrow
post-derivative-vessel-relation-boundary surface. The derivative-vessel
relation boundary is recognized only as downstream relation-boundary posture.

The resolver does not replay the host, merge preserved runs, mutate upstream
artifacts, create authority, create permission, infer currentness by recency,
replace source, create adoption, create public release, create privileged
standing, complete governance, complete continuity, complete final system
identity, or authorize follow-on vessel relations.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class CurrentSelfOrientationV6Error(RuntimeError):
    """Raised for malformed selected inputs or impossible correspondence."""

    def __init__(
        self,
        message: str,
        block_code: str,
        *,
        selected_inputs: Mapping[str, Any] | None = None,
        checks: Sequence[Mapping[str, Any]] | None = None,
    ) -> None:
        super().__init__(message)
        self.block_code = block_code
        self.selected_inputs = (
            copy.deepcopy(dict(selected_inputs))
            if isinstance(selected_inputs, Mapping)
            else None
        )
        self.checks = [dict(check) for check in checks] if checks is not None else None


V0_BODY_PASS_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_v0_body_pass")
CURRENT_SELF_ORIENTATION_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v2"
)
CURRENT_SELF_ORIENTATION_V3_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v3"
)
CURRENT_SELF_ORIENTATION_V4_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v4"
)
CURRENT_SELF_ORIENTATION_V5_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v5"
)
CURRENT_SELF_ORIENTATION_REENTRY_ADMISSIBILITY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
CURRENT_SELF_ORIENTATION_REENTRY_RECEIPT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)
BODY_SIGNAL_RECOGNITION_V2_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition_v2"
)
BODY_SIGNAL_ACCEPTANCE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance"
)
BODY_SIGNAL_SCOPE_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_body_signal_scope"
)
DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_derivative_vessel_relation_boundary"
)
CURRENT_SELF_ORIENTATION_V6_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)

OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT = Path(
    "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = Path(
    "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)

RESOLVER_MODULE = "resolve_current_self_orientation_v6"
SUCCESSOR_OF_MODULE = "resolve_current_self_orientation_v5"
CURRENT_SELF_ORIENTATION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_SELF_ORIENTATION_V6_RESULT"
)
CURRENT_SELF_ORIENTATION_RESULT_VERSION = "0.6.0"
DEFAULT_RESULT_STEM = "current_self_orientation_v6_result"

OUTCOME_SELF_ORIENTED = "SELF_ORIENTED"
OUTCOME_BLOCKED = "BLOCKED"
OUTCOME_BODY_PASS_CONFIRMED = "V0_BODY_PASS_CONFIRMED"
OUTCOME_RELATION_RECOGNIZED = "DERIVATIVE_VESSEL_RELATION_RECOGNIZED"
OUTCOME_SIGNAL_RECOGNIZED = "SIGNAL_RECOGNIZED"
OUTCOME_SIGNAL_ACCEPTED = "SIGNAL_ACCEPTED"
OUTCOME_SIGNAL_SCOPED = "SIGNAL_SCOPED"

BLOCK_REASONS = {
    "NO_SELF_ORIENTATION_SOURCE_BASIS": (
        "No bounded self-orientation source basis is available."
    ),
    "REQUIRED_SOURCE_ARTIFACT_UNREADABLE": (
        "A required selected source artifact could not be read."
    ),
    "SOURCE_ARTIFACT_MALFORMED": "A selected source artifact is malformed.",
    "CORRESPONDENCE_CHECK_FAILED": (
        "A bounded correspondence/proportion check failed."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A carried non-claim is missing or no longer false."
    ),
    "LATEST_FILE_RECENCY_REFUSED": (
        "Currentness inferred by latest-file recency alone is refused."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_UNREADABLE": (
        "The derivative-vessel relation boundary root or artifact could not be read."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_MALFORMED": (
        "A derivative-vessel relation boundary artifact is malformed."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED": (
        "No matching recognized derivative-vessel relation boundary stands."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_BASIS_MISMATCH": (
        "The derivative-vessel relation boundary does not preserve the selected "
        "source/body basis."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_DERIVATIVE_BASIS_MISMATCH": (
        "The derivative-vessel relation boundary does not preserve the selected "
        "derivative vessel basis."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE": (
        "The derivative-vessel relation boundary did not remain downstream."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_REPLACEMENT_LEAK": (
        "The derivative-vessel relation boundary attempted source replacement."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_AUTHORITY_LEAK": (
        "The derivative-vessel relation boundary created or leaked authority."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CURRENTNESS_LEAK": (
        "The derivative-vessel relation boundary created or leaked currentness."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PERMISSION_LEAK": (
        "The derivative-vessel relation boundary created or leaked permission."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_ADOPTION_LEAK": (
        "The derivative-vessel relation boundary created or leaked adoption."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PRIVILEGED_STANDING_LEAK": (
        "The derivative-vessel relation boundary created or leaked privileged standing."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_PUBLIC_RELEASE_LEAK": (
        "The derivative-vessel relation boundary created or leaked public release."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_GOVERNANCE_LEAK": (
        "The derivative-vessel relation boundary completed or leaked final governance."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_SYSTEM_IDENTITY_LEAK": (
        "The derivative-vessel relation boundary completed final system identity."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_CONTINUITY_COMPLETION_LEAK": (
        "The derivative-vessel relation boundary completed continuity."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_GENERAL_PERMISSION_LEAK": (
        "The derivative-vessel relation boundary created general vessel permission."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_FOLLOW_ON_AUTHORIZATION_LEAK": (
        "The derivative-vessel relation boundary authorized follow-on vessel relations."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_TREATED_AS_AUTHORITY": (
        "The derivative-vessel relation boundary was treated as authority."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_TREATED_AS_CURRENT_OR_GOVERNING_BASIS": (
        "The derivative-vessel relation boundary was treated as current or governing basis."
    ),
}

NON_CLAIM_DEFAULTS = {
    "authority_created": False,
    "permission_created": False,
    "currentness_created": False,
    "continuity_completed": False,
    "final_governance_completed": False,
    "final_system_identity_completed": False,
    "standing_upgraded": False,
    "source_replaced": False,
    "source_scope_widened": False,
    "derivative_upgraded_to_source": False,
    "derivative_outputs_upgraded_to_source": False,
    "operator_upgraded_to_source": False,
    "operator_outputs_upgraded_to_source": False,
    "reentry_admissibility_became_authority": False,
    "receipt_became_authority": False,
    "signal_recognition_became_authority": False,
    "signal_acceptance_became_authority": False,
    "signal_scope_became_authority": False,
    "signal_surface_became_current_or_governing_basis": False,
    "general_permission_created": False,
    "follow_on_steps_authorized": False,
    "follow_on_work_authorized": False,
    "admission_reusable": False,
    "latest_file_currentness": False,
    "recency_fraud": False,
    "mutation_performed": False,
    "replay_performed": False,
    "merge_performed": False,
    "roadmap_generated": False,
    "roadmap_created": False,
    "workflow_engine_created": False,
    "workflow_created": False,
    "signal_router_created": False,
    "event_bus_created": False,
    "body_relevance_medium_created": False,
    "presence_established": False,
    "threshold_met": False,
    "truth_created": False,
    "action_authorized": False,
    "applied_outside_declared_scope": False,
    "scoped_signal_applied_outside_declared_scope": False,
    "derivative_vessel_relation_became_authority": False,
    "derivative_vessel_relation_became_currentness": False,
    "derivative_vessel_relation_became_permission": False,
    "derivative_vessel_relation_became_current_or_governing_basis": False,
    "derivative_vessel_relation_created_adoption": False,
    "derivative_vessel_relation_created_privileged_standing": False,
    "derivative_vessel_relation_created_public_release": False,
    "derivative_vessel_relation_replaced_source": False,
    "derivative_vessel_relation_completed_final_governance": False,
    "derivative_vessel_relation_completed_final_system_identity": False,
    "derivative_vessel_relation_completed_continuity": False,
    "derivative_vessel_relation_created_general_vessel_permission": False,
    "derivative_vessel_relation_authorized_follow_on_vessels": False,
    "source_derivative_operator_collapsed": False,
    "self_orientation_became_authority": False,
}

SUMMARY_NON_CLAIMS = (
    "authority_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "standing_upgraded",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "reentry_admissibility_became_authority",
    "receipt_became_authority",
    "signal_recognition_became_authority",
    "signal_acceptance_became_authority",
    "signal_scope_became_authority",
    "derivative_vessel_relation_became_authority",
    "derivative_vessel_relation_became_currentness",
    "derivative_vessel_relation_became_permission",
    "derivative_vessel_relation_became_current_or_governing_basis",
    "derivative_vessel_relation_created_adoption",
    "derivative_vessel_relation_created_privileged_standing",
    "derivative_vessel_relation_created_public_release",
    "derivative_vessel_relation_replaced_source",
    "derivative_vessel_relation_completed_final_governance",
    "derivative_vessel_relation_completed_final_system_identity",
    "derivative_vessel_relation_completed_continuity",
    "derivative_vessel_relation_created_general_vessel_permission",
    "derivative_vessel_relation_authorized_follow_on_vessels",
    "general_permission_created",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
    "admission_reusable",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "roadmap_generated",
    "workflow_engine_created",
    "signal_router_created",
    "event_bus_created",
    "body_relevance_medium_created",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "applied_outside_declared_scope",
    "source_derivative_operator_collapsed",
)


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else Path.cwd() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    candidate = Path(path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.relative_to(Path.cwd()).as_posix()
    except ValueError:
        return candidate.as_posix()


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _string_or_none(value: Any) -> str | None:
    return value if isinstance(value, str) and value else None


def _as_mapping(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _as_mapping_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _block_reason(block_code: str | None, detail: str | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "Bounded self-orientation refused.")
    if detail:
        return f"{reason} {detail}"
    return reason


def _safe_filename_part(value: Any) -> str:
    text = value if isinstance(value, str) and value else DEFAULT_RESULT_STEM
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("._")
    return text[:180] or DEFAULT_RESULT_STEM


def _read_json_mapping(
    path: Path | str,
    *,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    target = _repo_path(path)
    if not target.is_file():
        raise CurrentSelfOrientationV6Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        )
    try:
        with target.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except json.JSONDecodeError as exc:
        raise CurrentSelfOrientationV6Error(
            f"required JSON artifact is malformed: {_display_path(target)}",
            malformed_code,
        ) from exc
    except OSError as exc:
        raise CurrentSelfOrientationV6Error(
            f"required JSON artifact is not readable: {_display_path(target)}",
            unreadable_code,
        ) from exc
    if not isinstance(data, Mapping):
        raise CurrentSelfOrientationV6Error(
            f"required JSON artifact is not an object: {_display_path(target)}",
            malformed_code,
        )
    return copy.deepcopy(dict(data))


def _iter_json_artifacts(
    root: Path | str,
    *,
    unreadable_code: str,
    malformed_code: str,
) -> list[tuple[Path, dict[str, Any]]]:
    resolved = _repo_path(root)
    if not resolved.exists() or not resolved.is_dir():
        raise CurrentSelfOrientationV6Error(
            f"artifact root is not readable: {_display_path(resolved)}",
            unreadable_code,
        )
    artifacts: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(resolved.glob("*.json")):
        artifacts.append(
            (
                path,
                _read_json_mapping(
                    path,
                    unreadable_code=unreadable_code,
                    malformed_code=malformed_code,
                ),
            )
        )
    return artifacts


def _latest_artifact(
    candidates: Sequence[tuple[Path, Mapping[str, Any]]],
) -> tuple[Path, dict[str, Any]] | None:
    if not candidates:
        return None
    path, data = max(
        candidates,
        key=lambda item: (
            item[0].stat().st_mtime if item[0].exists() else 0.0,
            item[0].as_posix(),
        ),
    )
    return path, copy.deepcopy(dict(data))


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
        "expected_posture": copy.deepcopy(expected),
        "actual_posture": copy.deepcopy(actual),
        "block_code": None if passed else block_code,
    }


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _as_check_list(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [copy.deepcopy(dict(item)) for item in value if isinstance(item, Mapping)]


def _all_checks_passed(checks: Sequence[Any]) -> bool:
    return bool(checks) and all(
        isinstance(check, Mapping) and check.get("passed") is True for check in checks
    )


def _section(value: Any) -> dict[str, Any]:
    return copy.deepcopy(dict(value)) if isinstance(value, Mapping) else {}


def _summary_bool(value: Any) -> bool:
    return isinstance(value, Mapping) and bool(value)


def _body_pass_identity(
    artifact: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _as_mapping(artifact.get("v0_body_pass_metadata"))
    selected_source = _as_mapping(artifact.get("selected_source_surface"))
    return {
        "result_id": metadata.get("v0_body_pass_result_id")
        or artifact.get("result_id"),
        "result_path": _display_path(path) if path is not None else artifact.get("result_path"),
        "result_type": metadata.get("v0_body_pass_result_type")
        or artifact.get("result_type"),
        "result_version": metadata.get("v0_body_pass_result_version"),
        "result_family": "v0_body_pass_result",
        "outcome": artifact.get("outcome"),
        "source_surface_id": selected_source.get("selected_source_surface_id"),
        "source_surface_family": selected_source.get("selected_source_surface_family"),
        "source_surface_path": selected_source.get("selected_source_surface_path"),
        "selection_mode": selection_mode,
    }


def _select_body_pass(
    body_pass_result: Mapping[str, Any] | None,
    body_pass_result_path: Path | str | None,
) -> tuple[Path | None, dict[str, Any], str]:
    if body_pass_result_path is not None:
        return (
            _repo_path(body_pass_result_path),
            _read_json_mapping(
                body_pass_result_path,
                unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            ),
            "explicit_body_pass_result_path",
        )
    if body_pass_result is not None:
        if not isinstance(body_pass_result, Mapping):
            raise CurrentSelfOrientationV6Error(
                "body-pass input must be a mapping",
                "SOURCE_ARTIFACT_MALFORMED",
            )
        return None, copy.deepcopy(dict(body_pass_result)), "mapping_supplied_body_pass"

    candidates = [
        (path, data)
        for path, data in _iter_json_artifacts(
            V0_BODY_PASS_ROOT,
            unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
            malformed_code="SOURCE_ARTIFACT_MALFORMED",
        )
        if data.get("outcome") == OUTCOME_BODY_PASS_CONFIRMED
    ]
    selected = _latest_artifact(candidates)
    if selected is None:
        raise CurrentSelfOrientationV6Error(
            "no successful v0 body-pass anchor is available",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, data = selected
    return path, data, "latest_successful_body_pass_anchor"


def _self_orientation_v5_identity(
    artifact: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _as_mapping(artifact.get("current_self_orientation_v5_metadata"))
    return {
        "result_id": metadata.get("self_orientation_result_id"),
        "result_path": _display_path(path) if path is not None else artifact.get("result_path"),
        "result_type": metadata.get("self_orientation_result_type"),
        "result_version": metadata.get("self_orientation_result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "successor_of_module": metadata.get("successor_of_module"),
        "outcome": artifact.get("outcome"),
        "selection_mode": selection_mode,
    }


def _selected_body_pass_from_orientation(
    artifact: Mapping[str, Any],
) -> Mapping[str, Any]:
    selected = _as_mapping(artifact.get("selected_orientation_inputs"))
    return _as_mapping(selected.get("selected_body_pass_result"))


def _identity_matches(
    left: Mapping[str, Any],
    right: Mapping[str, Any],
    *,
    id_key: str = "result_id",
    path_key: str = "result_path",
) -> bool:
    comparisons: list[bool] = []
    left_id = _string_or_none(left.get(id_key))
    right_id = _string_or_none(right.get(id_key))
    if left_id and right_id:
        comparisons.append(left_id == right_id)
    left_path = _string_or_none(left.get(path_key))
    right_path = _string_or_none(right.get(path_key))
    if left_path and right_path:
        comparisons.append(left_path == right_path)
    return bool(comparisons) and all(comparisons)


def _select_matching_self_orientation_v5(
    body_identity: Mapping[str, Any],
) -> tuple[Path, dict[str, Any], str]:
    candidates: list[tuple[Path, dict[str, Any]]] = []
    for path, data in _iter_json_artifacts(
        CURRENT_SELF_ORIENTATION_V5_ROOT,
        unreadable_code="REQUIRED_SOURCE_ARTIFACT_UNREADABLE",
        malformed_code="SOURCE_ARTIFACT_MALFORMED",
    ):
        if data.get("outcome") != OUTCOME_SELF_ORIENTED:
            continue
        if _identity_matches(_selected_body_pass_from_orientation(data), body_identity):
            candidates.append((path, data))

    referenced_paths: set[str] = set()
    referenced_ids: set[str] = set()
    if _repo_path(DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT).is_dir():
        for _path, data in _iter_json_artifacts(
            DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT,
            unreadable_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_UNREADABLE",
            malformed_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_MALFORMED",
        ):
            if data.get("outcome") != OUTCOME_RELATION_RECOGNIZED:
                continue
            relation = _as_mapping(data.get("recognized_derivative_vessel_relation"))
            source_basis = _as_mapping(data.get("selected_source_body_basis"))
            for value in (
                relation.get("source_body_basis_path"),
                source_basis.get("source_body_basis_path"),
                source_basis.get("self_orientation_result_path"),
            ):
                if isinstance(value, str) and value:
                    referenced_paths.add(value)
            for value in (
                relation.get("source_body_basis_id"),
                source_basis.get("source_body_basis_id"),
                source_basis.get("self_orientation_result_id"),
            ):
                if isinstance(value, str) and value:
                    referenced_ids.add(value)

    if referenced_paths:
        path_matches = [
            (path, data) for path, data in candidates if _display_path(path) in referenced_paths
        ]
        selected_path_match = _latest_artifact(path_matches)
        if selected_path_match is not None:
            path, data = selected_path_match
            return path, data, "relation_boundary_referenced_current_self_orientation_v5"

    if referenced_ids:
        id_matches: list[tuple[Path, dict[str, Any]]] = []
        for path, data in candidates:
            identity = _self_orientation_v5_identity(
                data,
                path,
                "matching_current_self_orientation_v5_discovery",
            )
            if identity.get("result_id") in referenced_ids:
                id_matches.append((path, data))
        selected_id_match = _latest_artifact(id_matches)
        if selected_id_match is not None:
            path, data = selected_id_match
            return path, data, "relation_boundary_referenced_current_self_orientation_v5"

    selected = _latest_artifact(candidates)
    if selected is None:
        raise CurrentSelfOrientationV6Error(
            "no matching v5 self-orientation result is available",
            "NO_SELF_ORIENTATION_SOURCE_BASIS",
        )
    path, data = selected
    return path, data, "matching_current_self_orientation_v5_discovery"


def _relation_boundary_identity(
    artifact: Mapping[str, Any],
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    metadata = _as_mapping(artifact.get("derivative_vessel_relation_boundary_metadata"))
    block = _as_mapping(artifact.get("block"))
    relation = _as_mapping(artifact.get("recognized_derivative_vessel_relation"))
    summary = _as_mapping(artifact.get("derivative_vessel_relation_boundary_summary"))
    return {
        "result_id": metadata.get("derivative_vessel_relation_boundary_result_id"),
        "result_path": _display_path(path) if path is not None else artifact.get("result_path"),
        "result_type": metadata.get("derivative_vessel_relation_boundary_result_type"),
        "result_version": metadata.get("derivative_vessel_relation_boundary_result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "outcome": artifact.get("outcome"),
        "relation_id": relation.get("relation_id") or summary.get("relation_id"),
        "relation_type": relation.get("relation_type") or summary.get("relation_type"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selection_mode": selection_mode,
    }


def _selected_source_surface(v5_result: Mapping[str, Any]) -> dict[str, Any]:
    selected = _as_mapping(v5_result.get("selected_orientation_inputs"))
    return _as_mapping(selected.get("selected_source_surface"))


def _selected_vessel_results(v5_result: Mapping[str, Any]) -> list[dict[str, Any]]:
    selected = _as_mapping(v5_result.get("selected_orientation_inputs"))
    return _as_mapping_list(selected.get("selected_vessel_results"))


def _relation_source_matches_v5(
    relation_result: Mapping[str, Any],
    v5_result: Mapping[str, Any],
    v5_identity: Mapping[str, Any],
) -> bool:
    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    selected_source_basis = _as_mapping(relation_result.get("selected_source_body_basis"))
    source = _selected_source_surface(v5_result)
    comparisons: list[bool] = []

    relation_basis_id = (
        relation.get("source_body_basis_id")
        or selected_source_basis.get("source_body_basis_id")
        or selected_source_basis.get("self_orientation_result_id")
    )
    if relation_basis_id and v5_identity.get("result_id"):
        comparisons.append(relation_basis_id == v5_identity.get("result_id"))

    relation_basis_path = (
        relation.get("source_body_basis_path")
        or selected_source_basis.get("source_body_basis_path")
        or selected_source_basis.get("self_orientation_result_path")
    )
    if relation_basis_path and v5_identity.get("result_path"):
        comparisons.append(relation_basis_path == v5_identity.get("result_path"))

    relation_source_id = (
        relation.get("source_surface_id") or selected_source_basis.get("source_surface_id")
    )
    if relation_source_id and source.get("result_id"):
        comparisons.append(relation_source_id == source.get("result_id"))

    relation_source_path = (
        relation.get("source_surface_path")
        or selected_source_basis.get("source_surface_path")
    )
    if relation_source_path and source.get("result_path"):
        comparisons.append(relation_source_path == source.get("result_path"))

    return bool(comparisons) and all(comparisons)


def _relation_derivative_matches_v5(
    relation_result: Mapping[str, Any],
    v5_result: Mapping[str, Any],
) -> bool:
    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    selected_derivative = _as_mapping(relation_result.get("selected_derivative_vessel_basis"))
    relation_id = (
        relation.get("derivative_vessel_result_id")
        or selected_derivative.get("derivative_vessel_result_id")
    )
    relation_path = (
        relation.get("derivative_vessel_result_path")
        or selected_derivative.get("derivative_vessel_result_path")
    )
    vessel_results = _selected_vessel_results(v5_result)
    if not vessel_results:
        return bool(relation_id or relation_path)
    for vessel in vessel_results:
        comparisons: list[bool] = []
        if relation_id and vessel.get("result_id"):
            comparisons.append(relation_id == vessel.get("result_id"))
        if relation_path and vessel.get("result_path"):
            comparisons.append(relation_path == vessel.get("result_path"))
        if comparisons and all(comparisons):
            return True
    return False


def _select_matching_relation_boundary(
    v5_result: Mapping[str, Any],
    v5_identity: Mapping[str, Any],
) -> tuple[
    Path,
    dict[str, Any],
    dict[str, Any],
    Path | None,
    dict[str, Any] | None,
    dict[str, Any] | None,
]:
    artifacts = _iter_json_artifacts(
        DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT,
        unreadable_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_UNREADABLE",
        malformed_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_MALFORMED",
    )
    recognized_candidates = [
        (path, data)
        for path, data in artifacts
        if data.get("outcome") == OUTCOME_RELATION_RECOGNIZED
        and _relation_source_matches_v5(data, v5_result, v5_identity)
        and _relation_derivative_matches_v5(data, v5_result)
    ]
    selected = _latest_artifact(recognized_candidates)
    if selected is None:
        raise CurrentSelfOrientationV6Error(
            "no matching recognized derivative-vessel relation boundary is available",
            "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
        )

    relation_path, relation_result = selected
    relation_identity = _relation_boundary_identity(
        relation_result,
        relation_path,
        "matching_derivative_vessel_relation_boundary_discovery",
    )

    blocked_candidates = [
        (path, data)
        for path, data in artifacts
        if data.get("outcome") == OUTCOME_BLOCKED
        and _relation_source_matches_v5(data, v5_result, v5_identity)
    ]
    blocked = _latest_artifact(blocked_candidates)
    if blocked is None:
        return relation_path, relation_result, relation_identity, None, None, None

    blocked_path, blocked_result = blocked
    blocked_identity = _relation_boundary_identity(
        blocked_result,
        blocked_path,
        "matching_blocked_derivative_vessel_relation_boundary_discovery",
    )
    return (
        relation_path,
        relation_result,
        relation_identity,
        blocked_path,
        blocked_result,
        blocked_identity,
    )


def _relation_remains(
    relation_result: Mapping[str, Any] | None,
) -> dict[str, bool]:
    if not isinstance(relation_result, Mapping):
        return {
            "downstream": False,
            "additive_only": False,
            "source_body_basis_upstream": False,
            "derivative_vessel_result_downstream": False,
            "operator_facing_output_downstream_where_present": False,
            "source_preserved": False,
            "derivative_preserved": False,
            "no_authority": False,
            "no_permission": False,
            "no_currentness": False,
            "no_adoption": False,
            "no_privileged_standing": False,
            "no_public_release": False,
            "no_source_replacement": False,
            "no_final_governance": False,
            "no_final_system_identity": False,
            "no_continuity_completion": False,
            "no_general_vessel_permission": False,
            "no_follow_on_vessel_authorization": False,
            "surface_remains_downstream_and_non_authoritative": False,
        }
    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    non_claims = _as_mapping(relation_result.get("non_claims"))
    return {
        "downstream": relation.get("downstream") is True,
        "additive_only": relation.get("additive_only") is True,
        "source_body_basis_upstream": relation.get("source_preserved") is True,
        "derivative_vessel_result_downstream": relation.get("derivative_preserved") is True,
        "operator_facing_output_downstream_where_present": relation.get(
            "operator_downstream_where_present"
        )
        is True,
        "source_preserved": relation.get("source_preserved") is True,
        "derivative_preserved": relation.get("derivative_preserved") is True,
        "no_authority": relation.get("no_authority") is True
        and non_claims.get("authority_created") is False,
        "no_permission": relation.get("no_permission") is True
        and non_claims.get("permission_created") is False,
        "no_currentness": relation.get("no_currentness") is True
        and non_claims.get("currentness_created") is False,
        "no_adoption": relation.get("no_adoption") is True
        and non_claims.get("adoption_created") is False,
        "no_privileged_standing": relation.get("no_privileged_standing") is True
        and non_claims.get("privileged_standing_created") is False,
        "no_public_release": relation.get("no_public_release") is True
        and non_claims.get("public_release_created") is False,
        "no_source_replacement": relation.get("no_source_replacement") is True
        and non_claims.get("source_replaced") is False,
        "no_final_governance": relation.get("no_final_governance") is True
        and non_claims.get("final_governance_completed") is False,
        "no_final_system_identity": relation.get("no_final_system_identity") is True
        and non_claims.get("final_system_identity_completed") is False,
        "no_continuity_completion": relation.get("no_continuity_completion") is True
        and non_claims.get("continuity_completed") is False,
        "no_general_vessel_permission": non_claims.get(
            "general_vessel_permission_created"
        )
        is False,
        "no_follow_on_vessel_authorization": relation.get(
            "no_follow_on_vessel_authorization"
        )
        is True
        and non_claims.get("follow_on_vessels_authorized") is False,
        "surface_remains_downstream_and_non_authoritative": relation.get("downstream")
        is True
        and relation.get("no_authority") is True,
    }


def _recognized_derivative_vessel_relation_surfaces(
    relation_identity: Mapping[str, Any] | None,
    relation_result: Mapping[str, Any] | None,
    blocked_identity: Mapping[str, Any] | None,
    blocked_result: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if not isinstance(relation_result, Mapping):
        return {}
    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    remains = _relation_remains(relation_result)
    blocked_block = _as_mapping(blocked_result.get("block")) if blocked_result else {}
    return {
        "recognition_posture": "downstream_derivative_vessel_relation_boundary_only",
        "selected_derivative_vessel_relation_boundary_result": _as_mapping(
            relation_identity
        ),
        "selected_blocked_derivative_vessel_relation_boundary_result": _as_mapping(
            blocked_identity
        ),
        "blocked_derivative_vessel_relation_boundary_refusal": {
            "selected": isinstance(blocked_result, Mapping),
            "outcome": blocked_result.get("outcome") if isinstance(blocked_result, Mapping) else None,
            "block_code": blocked_block.get("block_code"),
            "block_reason": blocked_block.get("block_reason"),
        },
        "selected_source_body_basis": _as_mapping(
            relation_result.get("selected_source_body_basis")
        ),
        "selected_derivative_vessel_basis": _as_mapping(
            relation_result.get("selected_derivative_vessel_basis")
        ),
        "recognized_derivative_vessel_relation": relation,
        "relation_remains": remains,
        "selected_derivative_vessel_relation_boundary_result_id": relation_identity.get(
            "result_id"
        )
        if isinstance(relation_identity, Mapping)
        else None,
        "selected_blocked_derivative_vessel_relation_boundary_result_id": blocked_identity.get(
            "result_id"
        )
        if isinstance(blocked_identity, Mapping)
        else None,
        "selected_source_body_basis_id": relation.get("source_body_basis_id"),
        "selected_source_body_basis_path": relation.get("source_body_basis_path"),
        "selected_source_body_basis_outcome": relation.get("source_body_basis_outcome"),
        "selected_source_surface_id": relation.get("source_surface_id"),
        "selected_source_surface_path": relation.get("source_surface_path"),
        "selected_source_surface_outcome": relation.get("source_surface_outcome"),
        "selected_derivative_vessel_result_id": relation.get(
            "derivative_vessel_result_id"
        ),
        "selected_derivative_vessel_result_path": relation.get(
            "derivative_vessel_result_path"
        ),
        "selected_derivative_vessel_result_outcome": relation.get(
            "derivative_vessel_result_outcome"
        ),
        "relation_id": relation.get("relation_id"),
        "relation_type": relation.get("relation_type"),
        "downstream": remains.get("downstream"),
        "additive_only": remains.get("additive_only"),
        "source_preserved": remains.get("source_preserved"),
        "derivative_preserved": remains.get("derivative_preserved"),
        "operator_downstream_where_present": remains.get(
            "operator_facing_output_downstream_where_present"
        ),
        "no_authority": remains.get("no_authority"),
        "no_permission": remains.get("no_permission"),
        "no_currentness": remains.get("no_currentness"),
        "no_adoption": remains.get("no_adoption"),
        "no_privileged_standing": remains.get("no_privileged_standing"),
        "no_public_release": remains.get("no_public_release"),
        "no_source_replacement": remains.get("no_source_replacement"),
        "no_final_governance": remains.get("no_final_governance"),
        "no_final_system_identity": remains.get("no_final_system_identity"),
        "no_continuity_completion": remains.get("no_continuity_completion"),
        "no_general_vessel_permission": remains.get("no_general_vessel_permission"),
        "no_follow_on_vessel_authorization": remains.get(
            "no_follow_on_vessel_authorization"
        ),
        "derivative_vessel_relation_boundary_surfaces_remain_downstream": True,
        "derivative_vessel_relation_boundary_surfaces_remain_non_authoritative": True,
    }


def _build_relation_boundary_checks(
    v5_result: Mapping[str, Any],
    v5_identity: Mapping[str, Any],
    relation_result: Mapping[str, Any],
    blocked_result: Mapping[str, Any] | None,
) -> list[dict[str, Any]]:
    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    remains = _relation_remains(relation_result)
    non_claims = _as_mapping(relation_result.get("non_claims"))
    blocked_selected = isinstance(blocked_result, Mapping)
    return [
        _check(
            "v5_self_orientation_is_self_oriented",
            v5_result.get("outcome") == OUTCOME_SELF_ORIENTED,
            expected=OUTCOME_SELF_ORIENTED,
            actual=v5_result.get("outcome"),
            block_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
        ),
        _check(
            "selected_derivative_vessel_relation_boundary_result_is_derivative_vessel_relation_recognized",
            relation_result.get("outcome") == OUTCOME_RELATION_RECOGNIZED,
            expected=OUTCOME_RELATION_RECOGNIZED,
            actual=relation_result.get("outcome"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
        ),
        _check(
            "derivative_vessel_relation_boundary_preserves_selected_source_body_basis",
            _relation_source_matches_v5(relation_result, v5_result, v5_identity),
            expected="selected v5 source/body basis preserved",
            actual={
                "relation_source_body_basis_id": relation.get("source_body_basis_id"),
                "selected_v5_result_id": v5_identity.get("result_id"),
            },
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_BASIS_MISMATCH",
        ),
        _check(
            "derivative_vessel_relation_boundary_preserves_selected_derivative_vessel_basis",
            _relation_derivative_matches_v5(relation_result, v5_result),
            expected="selected derivative vessel basis preserved",
            actual={
                "relation_derivative_vessel_result_id": relation.get(
                    "derivative_vessel_result_id"
                ),
                "selected_v5_vessel_result_count": len(_selected_vessel_results(v5_result)),
            },
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DERIVATIVE_BASIS_MISMATCH",
        ),
        _check(
            "blocked_derivative_vessel_relation_boundary_refusal_remains_visible_where_selected",
            True,
            expected="blocked relation boundary preserved when available",
            actual={
                "blocked_relation_boundary_selected": blocked_selected,
                "blocked_outcome": blocked_result.get("outcome")
                if blocked_selected
                else None,
            },
            block_code="CORRESPONDENCE_CHECK_FAILED",
        ),
        _check(
            "recognized_relation_remains_downstream",
            remains.get("downstream") is True,
            expected=True,
            actual=remains.get("downstream"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
        ),
        _check(
            "recognized_relation_remains_additive_only",
            remains.get("additive_only") is True,
            expected=True,
            actual=remains.get("additive_only"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
        ),
        _check(
            "source_body_basis_remains_upstream",
            remains.get("source_body_basis_upstream") is True,
            expected=True,
            actual=remains.get("source_body_basis_upstream"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
        ),
        _check(
            "derivative_vessel_result_remains_downstream",
            remains.get("derivative_vessel_result_downstream") is True,
            expected=True,
            actual=remains.get("derivative_vessel_result_downstream"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
        ),
        _check(
            "operator_facing_output_remains_downstream_where_present",
            remains.get("operator_facing_output_downstream_where_present") is True,
            expected=True,
            actual=remains.get("operator_facing_output_downstream_where_present"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_DOWNSTREAM_COLLAPSE",
        ),
        _check(
            "relation_does_not_create_authority",
            remains.get("no_authority") is True,
            expected=True,
            actual=remains.get("no_authority"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_AUTHORITY_LEAK",
        ),
        _check(
            "relation_does_not_create_permission",
            remains.get("no_permission") is True,
            expected=True,
            actual=remains.get("no_permission"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_PERMISSION_LEAK",
        ),
        _check(
            "relation_does_not_create_currentness",
            remains.get("no_currentness") is True,
            expected=True,
            actual=remains.get("no_currentness"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_CURRENTNESS_LEAK",
        ),
        _check(
            "relation_does_not_create_adoption",
            remains.get("no_adoption") is True,
            expected=True,
            actual=remains.get("no_adoption"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_ADOPTION_LEAK",
        ),
        _check(
            "relation_does_not_create_privileged_standing",
            remains.get("no_privileged_standing") is True,
            expected=True,
            actual=remains.get("no_privileged_standing"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_PRIVILEGED_STANDING_LEAK",
        ),
        _check(
            "relation_does_not_create_public_release",
            remains.get("no_public_release") is True,
            expected=True,
            actual=remains.get("no_public_release"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_PUBLIC_RELEASE_LEAK",
        ),
        _check(
            "relation_does_not_replace_source",
            remains.get("no_source_replacement") is True,
            expected=True,
            actual=remains.get("no_source_replacement"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_SOURCE_REPLACEMENT_LEAK",
        ),
        _check(
            "relation_does_not_complete_final_governance",
            remains.get("no_final_governance") is True,
            expected=True,
            actual=remains.get("no_final_governance"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_GOVERNANCE_LEAK",
        ),
        _check(
            "relation_does_not_complete_final_system_identity",
            remains.get("no_final_system_identity") is True,
            expected=True,
            actual=remains.get("no_final_system_identity"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_FINAL_SYSTEM_IDENTITY_LEAK",
        ),
        _check(
            "relation_does_not_complete_continuity",
            remains.get("no_continuity_completion") is True,
            expected=True,
            actual=remains.get("no_continuity_completion"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_CONTINUITY_COMPLETION_LEAK",
        ),
        _check(
            "relation_does_not_create_general_vessel_permission",
            remains.get("no_general_vessel_permission") is True,
            expected=True,
            actual={
                "relation_remains": remains.get("no_general_vessel_permission"),
                "general_vessel_permission_created": non_claims.get(
                    "general_vessel_permission_created"
                ),
            },
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_GENERAL_PERMISSION_LEAK",
        ),
        _check(
            "relation_does_not_authorize_follow_on_vessel_relations",
            remains.get("no_follow_on_vessel_authorization") is True,
            expected=True,
            actual=remains.get("no_follow_on_vessel_authorization"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_FOLLOW_ON_AUTHORIZATION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_boundary_surface_does_not_become_authority",
            remains.get("surface_remains_downstream_and_non_authoritative") is True,
            expected=True,
            actual=remains.get("surface_remains_downstream_and_non_authoritative"),
            block_code="DERIVATIVE_VESSEL_RELATION_BOUNDARY_TREATED_AS_AUTHORITY",
        ),
        _check(
            "derivative_vessel_relation_boundary_surface_does_not_determine_current_governing_basis",
            True,
            expected="current/governing basis remains inherited from v5 upstream surfaces",
            actual="relation boundary recognized downstream only",
            block_code=(
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_TREATED_AS_CURRENT_OR_GOVERNING_BASIS"
            ),
        ),
        _check(
            "latest_file_recency_is_not_used_for_currentness",
            non_claims.get("latest_file_currentness") is False,
            expected=False,
            actual=non_claims.get("latest_file_currentness"),
            block_code="LATEST_FILE_RECENCY_REFUSED",
        ),
    ]


def _merge_non_claims(*artifacts: Mapping[str, Any] | None) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for artifact in artifacts:
        if not isinstance(artifact, Mapping):
            continue
        for key, value in _as_mapping(artifact.get("non_claims")).items():
            if isinstance(value, bool):
                merged[key] = value
    return merged


def _selected_inputs_with_relation(
    v5_result: Mapping[str, Any],
    v5_identity: Mapping[str, Any],
    relation_identity: Mapping[str, Any] | None,
    blocked_identity: Mapping[str, Any] | None,
) -> dict[str, Any]:
    selected = _as_mapping(v5_result.get("selected_orientation_inputs"))
    selected["selected_self_orientation_v5_result"] = _as_mapping(v5_identity)
    selected["selected_derivative_vessel_relation_boundary_result"] = _as_mapping(
        relation_identity
    )
    selected["selected_blocked_derivative_vessel_relation_boundary_result"] = (
        _as_mapping(blocked_identity)
    )
    return selected


def _empty_selected_inputs() -> dict[str, Any]:
    return {
        "selected_body_pass_result": {},
        "selected_self_orientation_v5_result": {},
        "selected_derivative_vessel_relation_boundary_result": {},
        "selected_blocked_derivative_vessel_relation_boundary_result": {},
    }


def _metadata(selected_inputs: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    body = _as_mapping(selected_inputs.get("selected_body_pass_result"))
    v5 = _as_mapping(selected_inputs.get("selected_self_orientation_v5_result"))
    base = (
        _string_or_none(body.get("result_id"))
        or _string_or_none(v5.get("result_id"))
        or "current_self_orientation_v6"
    )
    suffix = "self_oriented" if outcome == OUTCOME_SELF_ORIENTED else "blocked"
    return {
        "self_orientation_result_id": f"{base}__current_self_orientation_v6_{suffix}",
        "self_orientation_result_type": CURRENT_SELF_ORIENTATION_RESULT_TYPE,
        "self_orientation_result_version": CURRENT_SELF_ORIENTATION_RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "successor_of_module": SUCCESSOR_OF_MODULE,
    }


def _predecessor_section(
    predecessor_result: Mapping[str, Any] | None,
    key: str,
) -> dict[str, Any]:
    if not isinstance(predecessor_result, Mapping):
        return {}
    return _section(predecessor_result.get(key))


def _build_result(
    *,
    selected_inputs: Mapping[str, Any],
    predecessor_result: Mapping[str, Any] | None,
    recognized_derivative_vessel_relation_surfaces: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_detail: str | None,
    self_orientation_basis: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    result = {
        "current_self_orientation_v6_metadata": _metadata(selected_inputs, outcome),
        "selected_orientation_inputs": copy.deepcopy(dict(selected_inputs)),
        "recognized_current_executable_core_line": _predecessor_section(
            predecessor_result,
            "recognized_current_executable_core_line",
        ),
        "recognized_governing_effective_basis": _predecessor_section(
            predecessor_result,
            "recognized_governing_effective_basis",
        ),
        "recognized_current_state_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_current_state_surfaces",
        ),
        "recognized_continuity_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_continuity_surfaces",
        ),
        "recognized_derivative_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_derivative_surfaces",
        ),
        "recognized_operator_facing_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_operator_facing_surfaces",
        ),
        "recognized_reentry_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_reentry_surfaces",
        ),
        "recognized_body_signal_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_body_signal_surfaces",
        ),
        "recognized_derivative_vessel_relation_surfaces": _section(
            recognized_derivative_vessel_relation_surfaces
        ),
        "recognized_open_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_open_surfaces",
        ),
        "recognized_blocked_or_refused_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_blocked_or_refused_surfaces",
        ),
        "recognized_touch_admissibility_surfaces": _predecessor_section(
            predecessor_result,
            "recognized_touch_admissibility_surfaces",
        ),
        "bounded_correspondence_checks": [
            copy.deepcopy(dict(check)) for check in checks
        ],
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "self_orientation_basis": copy.deepcopy(dict(self_orientation_basis)),
        "current_self_orientation_summary": {},
        "non_claims": dict(non_claims),
    }
    result["current_self_orientation_summary"] = build_current_self_orientation_summary(
        result
    )
    return result


def _blocked_result(
    *,
    block_code: str,
    block_detail: str | None = None,
    selected_inputs: Mapping[str, Any] | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    predecessor_result: Mapping[str, Any] | None = None,
    recognized_derivative_vessel_relation_surfaces: Mapping[str, Any] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    selected = selected_inputs if isinstance(selected_inputs, Mapping) else _empty_selected_inputs()
    return _build_result(
        selected_inputs=selected,
        predecessor_result=predecessor_result,
        recognized_derivative_vessel_relation_surfaces=(
            recognized_derivative_vessel_relation_surfaces or {}
        ),
        checks=checks or [],
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_detail=block_detail,
        self_orientation_basis={
            "basis_kind": "blocked_v6_self_orientation_preserving_selected_basis",
            "successor_of_module": SUCCESSOR_OF_MODULE,
            "derivative_vessel_relation_boundary_surfaces_remain_downstream": True,
            "self_orientation_creates_authority": False,
            "derivative_vessel_relation_creates_authority": False,
            "derivative_vessel_relation_creates_permission": False,
            "derivative_vessel_relation_creates_currentness": False,
            "derivative_vessel_relation_replaces_source": False,
        },
        non_claims=dict(non_claims or NON_CLAIM_DEFAULTS),
    )


def _resolve(
    body_pass_result: Mapping[str, Any] | None = None,
    body_pass_result_path: Path | str | None = None,
) -> dict[str, Any]:
    body_path, body_artifact, body_selection_mode = _select_body_pass(
        body_pass_result,
        body_pass_result_path,
    )
    body_identity = _body_pass_identity(body_artifact, body_path, body_selection_mode)
    if body_identity.get("outcome") != OUTCOME_BODY_PASS_CONFIRMED:
        return _blocked_result(
            block_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
            block_detail="body-pass anchor is not V0_BODY_PASS_CONFIRMED",
            selected_inputs={"selected_body_pass_result": body_identity},
            checks=[
                _check(
                    "selected_body_pass_anchor_is_confirmed",
                    False,
                    expected=OUTCOME_BODY_PASS_CONFIRMED,
                    actual=body_identity.get("outcome"),
                    block_code="NO_SELF_ORIENTATION_SOURCE_BASIS",
                )
            ],
        )

    v5_path, v5_result, v5_selection_mode = _select_matching_self_orientation_v5(
        body_identity
    )
    v5_identity = _self_orientation_v5_identity(v5_result, v5_path, v5_selection_mode)
    selected_inputs = _selected_inputs_with_relation(v5_result, v5_identity, None, None)

    try:
        (
            _relation_path,
            relation_result,
            relation_identity,
            _blocked_path,
            blocked_result,
            blocked_identity,
        ) = _select_matching_relation_boundary(v5_result, v5_identity)
    except CurrentSelfOrientationV6Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=selected_inputs,
            checks=exc.checks or [],
            predecessor_result=v5_result,
            non_claims=_merge_non_claims(v5_result),
        )

    selected_inputs = _selected_inputs_with_relation(
        v5_result,
        v5_identity,
        relation_identity,
        blocked_identity,
    )
    relation_surfaces = _recognized_derivative_vessel_relation_surfaces(
        relation_identity,
        relation_result,
        blocked_identity,
        blocked_result,
    )
    checks = [
        *_as_check_list(v5_result.get("bounded_correspondence_checks")),
        _check(
            "v5_selected_body_pass_matches_anchor",
            _identity_matches(_selected_body_pass_from_orientation(v5_result), body_identity),
            expected=body_identity,
            actual=_selected_body_pass_from_orientation(v5_result),
            block_code="CORRESPONDENCE_CHECK_FAILED",
        ),
        _check(
            "derivative_operator_reentry_signal_and_relation_surfaces_do_not_determine_current_governing_basis",
            True,
            expected="current/effective/current-state surfaces remain upstream",
            actual=(
                "derivative, operator, re-entry, signal, and relation surfaces "
                "recognized downstream only"
            ),
            block_code=(
                "DERIVATIVE_VESSEL_RELATION_BOUNDARY_TREATED_AS_CURRENT_OR_GOVERNING_BASIS"
            ),
        ),
        *_build_relation_boundary_checks(
            v5_result,
            v5_identity,
            relation_result,
            blocked_result,
        ),
    ]
    non_claims = _merge_non_claims(v5_result, relation_result, blocked_result)
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            block_code=_string_or_none(failed.get("block_code"))
            or "CORRESPONDENCE_CHECK_FAILED",
            block_detail=f"failed check: {failed.get('check_name')}",
            selected_inputs=selected_inputs,
            checks=checks,
            predecessor_result=v5_result,
            recognized_derivative_vessel_relation_surfaces=relation_surfaces,
            non_claims=non_claims,
        )

    relation = _as_mapping(relation_result.get("recognized_derivative_vessel_relation"))
    remains = _relation_remains(relation_result)
    return _build_result(
        selected_inputs=selected_inputs,
        predecessor_result=v5_result,
        recognized_derivative_vessel_relation_surfaces=relation_surfaces,
        checks=checks,
        outcome=OUTCOME_SELF_ORIENTED,
        block_code=None,
        block_detail=None,
        self_orientation_basis={
            "basis_kind": (
                "v5_self_orientation_plus_downstream_derivative_vessel_relation_boundary"
            ),
            "successor_of_module": SUCCESSOR_OF_MODULE,
            "selected_body_pass_result_id": body_identity.get("result_id"),
            "selected_body_pass_result_path": body_identity.get("result_path"),
            "selected_self_orientation_v5_result_id": v5_identity.get("result_id"),
            "selected_self_orientation_v5_result_path": v5_identity.get("result_path"),
            "selected_derivative_vessel_relation_boundary_result_id": relation_identity.get(
                "result_id"
            ),
            "selected_derivative_vessel_relation_boundary_result_path": relation_identity.get(
                "result_path"
            ),
            "selected_blocked_derivative_vessel_relation_boundary_result_id": blocked_identity.get(
                "result_id"
            )
            if isinstance(blocked_identity, Mapping)
            else None,
            "relation_id": relation.get("relation_id"),
            "relation_type": relation.get("relation_type"),
            "derivative_vessel_relation_boundary_recognized": True,
            "blocked_derivative_vessel_relation_boundary_preserved": isinstance(
                blocked_result,
                Mapping,
            ),
            "derivative_vessel_relation_remains_downstream": remains.get("downstream"),
            "source_body_basis_remains_upstream": remains.get(
                "source_body_basis_upstream"
            ),
            "derivative_vessel_result_remains_downstream": remains.get(
                "derivative_vessel_result_downstream"
            ),
            "operator_facing_output_remains_downstream_where_present": remains.get(
                "operator_facing_output_downstream_where_present"
            ),
            "relation_remains_additive_only": remains.get("additive_only"),
            "relation_creates_authority": False,
            "relation_creates_permission": False,
            "relation_creates_currentness": False,
            "relation_creates_adoption": False,
            "relation_creates_privileged_standing": False,
            "relation_creates_public_release": False,
            "relation_replaces_source": False,
            "relation_completes_final_governance": False,
            "relation_completes_final_system_identity": False,
            "relation_completes_continuity": False,
            "relation_creates_general_vessel_permission": False,
            "relation_authorizes_follow_on_vessels": False,
            "derivative_vessel_relation_boundary_surfaces_remain_downstream": True,
            "derivative_vessel_relation_boundary_surfaces_remain_non_authoritative": True,
            "self_orientation_creates_authority": False,
        },
        non_claims=non_claims,
    )


def resolve_current_self_orientation(
    body_pass_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded v6 self-orientation result."""

    try:
        return _resolve(body_pass_result=body_pass_result)
    except CurrentSelfOrientationV6Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs,
            checks=exc.checks,
        )


def resolve_current_self_orientation_from_path(
    body_pass_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve one bounded v6 self-orientation result from a body-pass path."""

    selected_inputs = {
        "selected_body_pass_result": {
            "result_path": _display_path(body_pass_result_path),
            "selection_mode": "explicit_body_pass_result_path",
        }
    }
    try:
        return _resolve(body_pass_result_path=body_pass_result_path)
    except CurrentSelfOrientationV6Error as exc:
        return _blocked_result(
            block_code=exc.block_code,
            block_detail=str(exc),
            selected_inputs=exc.selected_inputs or selected_inputs,
            checks=exc.checks,
        )


def build_current_self_orientation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build a bounded v6 self-orientation summary."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV6Error(
            "current self-orientation result must be an object",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    selected = _as_mapping(result.get("selected_orientation_inputs"))
    body = _as_mapping(selected.get("selected_body_pass_result"))
    source = _as_mapping(selected.get("selected_source_surface"))
    v5 = _as_mapping(selected.get("selected_self_orientation_v5_result"))
    reentry_admissibility = _as_mapping(
        selected.get("selected_reentry_admissibility_result")
    )
    reentry_receipt = _as_mapping(selected.get("selected_reentry_receipt_result"))
    recognition = _as_mapping(selected.get("selected_body_signal_recognition_result"))
    acceptance = _as_mapping(selected.get("selected_body_signal_acceptance_result"))
    scope = _as_mapping(selected.get("selected_body_signal_scope_result"))
    relation_identity = _as_mapping(
        selected.get("selected_derivative_vessel_relation_boundary_result")
    )
    relation_surfaces = _as_mapping(
        result.get("recognized_derivative_vessel_relation_surfaces")
    )
    remains = _as_mapping(relation_surfaces.get("relation_remains"))
    block = _as_mapping(result.get("block"))
    checks = result.get("bounded_correspondence_checks")
    checks = checks if isinstance(checks, list) else []
    non_claims = _as_mapping(result.get("non_claims"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_body_pass_result_id": body.get("result_id"),
        "selected_source_surface_id": source.get("result_id"),
        "selected_self_orientation_v5_result_id": v5.get("result_id"),
        "selected_reentry_admissibility_result_id": reentry_admissibility.get(
            "result_id"
        ),
        "selected_reentry_receipt_result_id": reentry_receipt.get("result_id"),
        "selected_body_signal_recognition_result_id": recognition.get("result_id"),
        "selected_body_signal_acceptance_result_id": acceptance.get("result_id"),
        "selected_body_signal_scope_result_id": scope.get("result_id"),
        "selected_derivative_vessel_relation_boundary_result_id": relation_identity.get(
            "result_id"
        ),
        "current_executable_core_line_recognized": _summary_bool(
            result.get("recognized_current_executable_core_line")
        ),
        "governing_effective_basis_recognized": _summary_bool(
            result.get("recognized_governing_effective_basis")
        ),
        "current_state_surfaces_recognized": _summary_bool(
            result.get("recognized_current_state_surfaces")
        ),
        "continuity_surfaces_recognized": _summary_bool(
            result.get("recognized_continuity_surfaces")
        ),
        "derivative_surfaces_recognized": _summary_bool(
            result.get("recognized_derivative_surfaces")
        ),
        "operator_surfaces_recognized": _summary_bool(
            result.get("recognized_operator_facing_surfaces")
        ),
        "reentry_surfaces_recognized": _summary_bool(
            result.get("recognized_reentry_surfaces")
        ),
        "body_signal_surfaces_recognized": _summary_bool(
            result.get("recognized_body_signal_surfaces")
        ),
        "body_signal_recognition_recognized": recognition.get("outcome")
        == OUTCOME_SIGNAL_RECOGNIZED,
        "body_signal_acceptance_accepted": acceptance.get("outcome")
        == OUTCOME_SIGNAL_ACCEPTED,
        "body_signal_scope_scoped": scope.get("outcome") == OUTCOME_SIGNAL_SCOPED,
        "derivative_vessel_relation_boundary_recognized": relation_identity.get(
            "outcome"
        )
        == OUTCOME_RELATION_RECOGNIZED,
        "derivative_vessel_relation_remains_downstream": remains.get("downstream")
        is True,
        "source_body_basis_remains_upstream": remains.get("source_body_basis_upstream")
        is True,
        "derivative_vessel_result_remains_downstream": remains.get(
            "derivative_vessel_result_downstream"
        )
        is True,
        "operator_facing_output_remains_downstream_where_present": remains.get(
            "operator_facing_output_downstream_where_present"
        )
        is True,
        "relation_remains_additive_only": remains.get("additive_only") is True,
        "relation_creates_no_authority": remains.get("no_authority") is True,
        "relation_creates_no_permission": remains.get("no_permission") is True,
        "relation_creates_no_currentness": remains.get("no_currentness") is True,
        "relation_creates_no_adoption": remains.get("no_adoption") is True,
        "relation_creates_no_privileged_standing": remains.get(
            "no_privileged_standing"
        )
        is True,
        "relation_creates_no_public_release": remains.get("no_public_release") is True,
        "relation_replaces_no_source": remains.get("no_source_replacement") is True,
        "relation_completes_no_final_governance": remains.get("no_final_governance")
        is True,
        "relation_completes_no_final_system_identity": remains.get(
            "no_final_system_identity"
        )
        is True,
        "relation_completes_no_continuity": remains.get("no_continuity_completion")
        is True,
        "relation_creates_no_general_vessel_permission": remains.get(
            "no_general_vessel_permission"
        )
        is True,
        "relation_authorizes_no_follow_on_vessels": remains.get(
            "no_follow_on_vessel_authorization"
        )
        is True,
        "correspondence_checks_passed": _all_checks_passed(checks),
        "non_claims": {
            key: non_claims.get(key)
            for key in SUMMARY_NON_CLAIMS
            if key in non_claims
        },
    }


def _safe_default_output_path(result: Mapping[str, Any]) -> Path:
    selected = _as_mapping(result.get("selected_orientation_inputs"))
    body = _as_mapping(selected.get("selected_body_pass_result"))
    stem = _safe_filename_part(body.get("result_id"))
    resolved_root = _repo_path(CURRENT_SELF_ORIENTATION_V6_ROOT)
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentSelfOrientationV6Error(
        "no bounded current self-orientation v6 filename is available",
        "SOURCE_ARTIFACT_MALFORMED",
    )


def write_current_self_orientation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive v6 self-orientation JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentSelfOrientationV6Error(
            "current self-orientation result must be an object",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current self-orientation v6 result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
