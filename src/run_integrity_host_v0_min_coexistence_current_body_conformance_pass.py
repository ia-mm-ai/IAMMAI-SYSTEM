"""Bounded integrated current-body conformance pass.

This module audits already-standing IAMMAI-SYSTEM artifacts as one body. It
does not replay the host, run prior resolvers, create authority, create
permission, create currentness, or authorize follow-on work. It only recognizes
whether the current self-orientation v6 line and its selected downstream
surfaces remain mutually conformant.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class CurrentBodyConformancePassError(Exception):
    """Hard failure for malformed explicit conformance-pass input."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CURRENT_SELF_ORIENTATION_V6_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)
REENTRY_ADMISSIBILITY_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_admissibility"
)
REENTRY_RECEIPT_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_reentry_receipt"
)
BODY_SIGNAL_RECOGNITION_V2_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_recognition_v2"
)
BODY_SIGNAL_ACCEPTANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_acceptance"
)
BODY_SIGNAL_SCOPE_ROOT = REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_body_signal_scope"
DERIVATIVE_VESSEL_RELATION_BOUNDARY_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_derivative_vessel_relation_boundary"
)
DERIVATIVE_VESSEL_READ_ROOT = (
    REPO_ROOT / "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = (
    REPO_ROOT / "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)
CURRENT_BODY_CONFORMANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass"
)

RUNNER_MODULE = "run_integrity_host_v0_min_coexistence_current_body_conformance_pass"
RESULT_VERSION = "0.1.0"

BODY_CONFORMANT = "BODY_CONFORMANT"
BLOCKED = "BLOCKED"
SELF_ORIENTED = "SELF_ORIENTED"
REENTRY_ADMITTED = "REENTRY_ADMITTED"
REENTRY_RECEIVED = "REENTRY_RECEIVED"
SIGNAL_RECOGNIZED = "SIGNAL_RECOGNIZED"
SIGNAL_ACCEPTED = "SIGNAL_ACCEPTED"
SIGNAL_SCOPED = "SIGNAL_SCOPED"
DERIVATIVE_VESSEL_RELATION_RECOGNIZED = "DERIVATIVE_VESSEL_RELATION_RECOGNIZED"
ANSWERED_DERIVATIVE_READ = "ANSWERED_DERIVATIVE_READ"
BRIEF_RENDERED = "BRIEF_RENDERED"

ACCEPTED_MATTER_ID = "current_signal_recognition_standing"
DECLARED_SCOPE_ID = "current_signal_recognition_standing__body_pass_signal_nonoperative_posture_scope"

BLOCK_REASONS = {
    "SELF_ORIENTATION_V6_MISSING": "No standing current self-orientation v6 result was supplied or discovered.",
    "SELF_ORIENTATION_V6_UNREADABLE": "The selected current self-orientation v6 artifact could not be read.",
    "SELF_ORIENTATION_V6_MALFORMED": "The selected current self-orientation v6 artifact is malformed.",
    "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED": "The selected current self-orientation v6 result is not SELF_ORIENTED.",
    "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED": "The current/governing basis is not recognized by the selected v6 result.",
    "CURRENT_GOVERNING_BASIS_DERIVED_FROM_DOWNSTREAM_SURFACE": (
        "A downstream surface is being treated as current/governing basis."
    ),
    "REENTRY_CLOSURE_MISMATCH": "The selected re-entry line does not preserve closed downstream posture.",
    "FOLLOW_ON_AUTHORIZATION_LEAK": "A selected surface leaks follow-on authorization.",
    "BODY_SIGNAL_LINE_MISSING": "The body-signal recognition, acceptance, and scope line is not standing.",
    "BODY_SIGNAL_LINE_OPERATIVE_LEAK": "The body-signal line became operative.",
    "BODY_SIGNAL_LINE_AUTHORITY_OR_PERMISSION_LEAK": (
        "The body-signal line leaked authority, currentness, permission, or action."
    ),
    "BODY_SIGNAL_SCOPE_OUTSIDE_DECLARED_SCOPE": "The scoped body signal applies outside declared scope.",
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_MISSING": (
        "No standing derivative-vessel relation boundary recognition is selected."
    ),
    "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED": (
        "The derivative-vessel relation boundary result is not recognized."
    ),
    "DERIVATIVE_VESSEL_RELATION_AUTHORITY_LEAK": "The derivative-vessel relation leaks authority.",
    "DERIVATIVE_VESSEL_RELATION_CURRENTNESS_LEAK": "The derivative-vessel relation leaks currentness.",
    "DERIVATIVE_VESSEL_RELATION_PERMISSION_LEAK": "The derivative-vessel relation leaks permission.",
    "DERIVATIVE_VESSEL_RELATION_ADOPTION_LEAK": "The derivative-vessel relation leaks adoption.",
    "DERIVATIVE_VESSEL_RELATION_PRIVILEGED_STANDING_LEAK": (
        "The derivative-vessel relation leaks privileged standing."
    ),
    "DERIVATIVE_VESSEL_RELATION_SOURCE_REPLACEMENT_LEAK": (
        "The derivative-vessel relation replaces source."
    ),
    "DERIVATIVE_VESSEL_RELATION_FINAL_GOVERNANCE_LEAK": (
        "The derivative-vessel relation completes final governance."
    ),
    "DERIVATIVE_VESSEL_RELATION_FINAL_SYSTEM_IDENTITY_LEAK": (
        "The derivative-vessel relation completes final system identity."
    ),
    "DERIVATIVE_VESSEL_RELATION_CONTINUITY_COMPLETION_LEAK": (
        "The derivative-vessel relation completes continuity."
    ),
    "DERIVATIVE_VESSEL_RELATION_GENERAL_PERMISSION_LEAK": (
        "The derivative-vessel relation creates general vessel permission."
    ),
    "DERIVATIVE_VESSEL_RELATION_FOLLOW_ON_AUTHORIZATION_LEAK": (
        "The derivative-vessel relation authorizes follow-on vessels."
    ),
    "DERIVATIVE_OUTPUT_SOURCE_COLLAPSE": "Derivative vessel output collapsed into source.",
    "OPERATOR_OUTPUT_SOURCE_COLLAPSE": "Operator-facing output collapsed into source.",
    "LATEST_FILE_RECENCY_REFUSED": "Latest-file recency is being used as currentness.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "A required non-claim is missing or flipped.",
    "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE": "Source, derivative, and operator distinctions collapsed.",
}

FALSE_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
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
    "derivative_vessel_relation_became_current_or_governing_basis",
    "derivative_vessel_relation_became_permission",
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
    "admission_reusable",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
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
}


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    resolved = Path(path)
    try:
        return str(resolved.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(resolved)


def _copy_mapping(value: Mapping[str, Any] | None) -> dict[str, Any]:
    if value is None:
        return {}
    return copy.deepcopy(dict(value))


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return copy.deepcopy(value)
    return []


def _nested(mapping: Mapping[str, Any], *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not isinstance(current, Mapping):
            return None
        current = current.get(key)
    return current


def _read_json_mapping(path: Path | str, unreadable_code: str, malformed_code: str) -> dict[str, Any]:
    artifact_path = Path(path)
    try:
        text = artifact_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CurrentBodyConformancePassError(
            unreadable_code,
            f"{BLOCK_REASONS[unreadable_code]} path={_display_path(artifact_path)} detail={exc}",
        ) from exc
    try:
        loaded = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CurrentBodyConformancePassError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={_display_path(artifact_path)} detail={exc}",
        ) from exc
    if not isinstance(loaded, dict):
        raise CurrentBodyConformancePassError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={_display_path(artifact_path)} expected object",
        )
    return loaded


def _latest_successful_v6_artifact() -> tuple[dict[str, Any] | None, Path | None]:
    if not CURRENT_SELF_ORIENTATION_V6_ROOT.exists():
        return None, None
    candidates: list[tuple[float, Path, dict[str, Any]]] = []
    for path in CURRENT_SELF_ORIENTATION_V6_ROOT.glob("*.json"):
        try:
            result = _read_json_mapping(
                path,
                "SELF_ORIENTATION_V6_UNREADABLE",
                "SELF_ORIENTATION_V6_MALFORMED",
            )
        except CurrentBodyConformancePassError:
            continue
        if result.get("outcome") == SELF_ORIENTED:
            candidates.append((path.stat().st_mtime, path, result))
    if not candidates:
        return None, None
    _, path, result = sorted(candidates, key=lambda item: (item[0], item[1].name))[-1]
    return result, path


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
    }


def _first_failed_check(checks: list[dict[str, Any]]) -> dict[str, Any] | None:
    return next((check for check in checks if not check.get("passed")), None)


def _block_reason(block_code: str | None, failed_check: Mapping[str, Any] | None = None) -> str | None:
    if block_code is None:
        return None
    reason = BLOCK_REASONS.get(block_code, "The current-body conformance pass refused conformance.")
    if failed_check:
        return f"{reason} failed check: {failed_check.get('check_name')}"
    return reason


def _safe_filename_part(value: Any) -> str:
    text = str(value or "current_body_conformance").strip()
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text)
    return text[:180] or "current_body_conformance"


def _metadata(result_id_basis: str | None) -> dict[str, Any]:
    stem = _safe_filename_part(result_id_basis or "current_self_orientation_v6")
    return {
        "current_body_conformance_result_id": f"{stem}__current_body_conformance_pass",
        "current_body_conformance_result_type": (
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_BODY_CONFORMANCE_PASS_RESULT"
        ),
        "current_body_conformance_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "runner_module": RUNNER_MODULE,
    }


def _v6_identity(
    self_orientation_v6_result: Mapping[str, Any] | None,
    result_path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    result = self_orientation_v6_result or {}
    metadata = _as_mapping(result.get("current_self_orientation_v6_metadata"))
    block = _as_mapping(result.get("block"))
    return {
        "result_id": metadata.get("self_orientation_result_id"),
        "result_type": metadata.get("self_orientation_result_type"),
        "result_version": metadata.get("self_orientation_result_version"),
        "resolver_module": metadata.get("resolver_module"),
        "successor_of_module": metadata.get("successor_of_module"),
        "outcome": result.get("outcome"),
        "result_path": _display_path(result_path),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selection_mode": selection_mode,
    }


def _selected_identity(value: Any) -> dict[str, Any]:
    selected = _as_mapping(value)
    if not selected:
        return {}
    block = _as_mapping(selected.get("block"))
    identity = copy.deepcopy(selected)
    identity.setdefault("block_code", block.get("block_code"))
    identity.setdefault("block_reason", block.get("block_reason"))
    return identity


def _derive_selected_derivative_vessel_result(v6: Mapping[str, Any]) -> dict[str, Any]:
    relation = _as_mapping(
        _nested(v6, "recognized_derivative_vessel_relation_surfaces", "recognized_derivative_vessel_relation")
    )
    if relation:
        return {
            "result_id": relation.get("derivative_vessel_result_id"),
            "result_path": relation.get("derivative_vessel_result_path"),
            "outcome": relation.get("derivative_vessel_result_outcome"),
            "result_family": relation.get("derivative_output_family"),
            "derivative_output_family": relation.get("derivative_output_family"),
            "derivative_output_basis": relation.get("derivative_output_basis"),
            "selection_mode": "recognized_relation_boundary_derivative_vessel_basis",
        }
    derivative_results = _as_list(
        _nested(v6, "recognized_derivative_surfaces", "openai_api_derivative_vessel_v3_results")
    )
    for result in derivative_results:
        if isinstance(result, Mapping) and result.get("outcome") == ANSWERED_DERIVATIVE_READ:
            return _selected_identity(result)
    return {}


def _build_selected_inputs(
    self_orientation_v6_result: Mapping[str, Any] | None,
    self_orientation_v6_path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    v6 = self_orientation_v6_result or {}
    selected = _as_mapping(v6.get("selected_orientation_inputs"))
    relation_surfaces = _as_mapping(v6.get("recognized_derivative_vessel_relation_surfaces"))
    operator_results = selected.get("selected_operator_terminal_brief_results")
    if operator_results is None:
        operator_results = _nested(v6, "recognized_operator_facing_surfaces", "operator_terminal_brief_results")

    return {
        "selected_self_orientation_v6_result": _v6_identity(v6, self_orientation_v6_path, selection_mode),
        "selected_body_pass_result": _selected_identity(selected.get("selected_body_pass_result")),
        "selected_self_orientation_v5_result": _selected_identity(
            selected.get("selected_self_orientation_v5_result")
        ),
        "selected_source_surface": _selected_identity(selected.get("selected_source_surface")),
        "selected_effective_references": copy.deepcopy(selected.get("selected_effective_references")),
        "selected_reentry_admissibility_result": _selected_identity(
            selected.get("selected_reentry_admissibility_result")
        ),
        "selected_reentry_receipt_result": _selected_identity(
            selected.get("selected_reentry_receipt_result")
        ),
        "selected_body_signal_recognition_result": _selected_identity(
            selected.get("selected_body_signal_recognition_result")
        ),
        "selected_blocked_body_signal_recognition_result": _selected_identity(
            selected.get("selected_blocked_body_signal_recognition_result")
        ),
        "selected_body_signal_acceptance_result": _selected_identity(
            selected.get("selected_body_signal_acceptance_result")
        ),
        "selected_body_signal_scope_result": _selected_identity(
            selected.get("selected_body_signal_scope_result")
        ),
        "selected_derivative_vessel_relation_boundary_result": _selected_identity(
            selected.get("selected_derivative_vessel_relation_boundary_result")
        ),
        "selected_blocked_derivative_vessel_relation_boundary_result": _selected_identity(
            selected.get("selected_blocked_derivative_vessel_relation_boundary_result")
        ),
        "selected_derivative_vessel_result": _derive_selected_derivative_vessel_result(v6),
        "selected_operator_terminal_brief_results": [
            _selected_identity(item) for item in _as_list(operator_results) if isinstance(item, Mapping)
        ],
        "relation_boundary_selected_source_body_basis": copy.deepcopy(
            relation_surfaces.get("selected_source_body_basis")
        ),
        "relation_boundary_selected_derivative_vessel_basis": copy.deepcopy(
            relation_surfaces.get("selected_derivative_vessel_basis")
        ),
        "selection_posture": {
            "top_level_anchor": "current_self_orientation_v6",
            "selected_by_successful_outcome_filter": selection_mode == "latest_successful_v6_artifact",
            "mapping_supplied": selection_mode == "provided_mapping",
            "path_supplied": selection_mode == "provided_path",
            "does_not_use_downstream_surface_as_current_governing_basis": True,
            "does_not_use_latest_file_recency_as_currentness": True,
        },
    }


def _combined_non_claims(v6: Mapping[str, Any] | None) -> dict[str, bool]:
    result = {key: False for key in sorted(FALSE_NON_CLAIMS)}
    source_non_claims = _as_mapping((v6 or {}).get("non_claims"))
    summary_non_claims = _as_mapping(_nested(v6 or {}, "current_self_orientation_summary", "non_claims"))
    for source in (summary_non_claims, source_non_claims):
        for key in FALSE_NON_CLAIMS:
            if source.get(key) is True:
                result[key] = True
            elif source.get(key) is False and result[key] is not True:
                result[key] = False
    return result


def _integrate_current_governing_basis(v6: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, Any]:
    summary = _as_mapping(v6.get("current_self_orientation_summary"))
    checks = _as_list(v6.get("bounded_correspondence_checks"))
    no_downstream_basis = all(
        check.get("passed") is True
        for check in checks
        if isinstance(check, Mapping)
        and check.get("check_name")
        in {
            "derivative_operator_reentry_signal_and_relation_surfaces_do_not_determine_current_governing_basis",
            "derivative_vessel_relation_boundary_surface_does_not_determine_current_governing_basis",
            "body_signal_scope_surface_does_not_determine_current_governing_basis",
            "body_signal_surfaces_do_not_determine_current_governing_basis",
            "reentry_surfaces_do_not_determine_current_governing_basis",
        }
    )
    return {
        "self_orientation_v6_outcome": v6.get("outcome"),
        "current_executable_core_line_recognized": bool(
            summary.get("current_executable_core_line_recognized")
            or v6.get("recognized_current_executable_core_line")
        ),
        "governing_effective_basis_recognized": bool(
            summary.get("governing_effective_basis_recognized")
            or v6.get("recognized_governing_effective_basis")
        ),
        "current_state_surfaces_recognized": bool(
            summary.get("current_state_surfaces_recognized") or v6.get("recognized_current_state_surfaces")
        ),
        "source_body_basis_remains_upstream": bool(
            summary.get("source_body_basis_remains_upstream")
            or _nested(v6, "recognized_derivative_vessel_relation_surfaces", "relation_remains", "source_body_basis_upstream")
        ),
        "downstream_surfaces_do_not_determine_current_governing_basis": bool(no_downstream_basis),
        "latest_file_currentness": bool(non_claims.get("latest_file_currentness")),
        "recency_fraud": bool(non_claims.get("recency_fraud")),
        "recognized_from": "explicit current/effective/governing/current-state surfaces",
    }


def _integrate_reentry_posture(v6: Mapping[str, Any], selected: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, Any]:
    surfaces = _as_mapping(v6.get("recognized_reentry_surfaces"))
    closure = _as_mapping(surfaces.get("closure_posture"))
    admissibility = _as_mapping(selected.get("selected_reentry_admissibility_result"))
    receipt = _as_mapping(selected.get("selected_reentry_receipt_result"))
    return {
        "selected_reentry_admissibility_result": copy.deepcopy(admissibility),
        "selected_reentry_receipt_result": copy.deepcopy(receipt),
        "admissibility_outcome": admissibility.get("outcome"),
        "receipt_outcome": receipt.get("outcome"),
        "recognized_downstream_by_v6": bool(surfaces),
        "closure_exhaustion_passed": closure.get("exhaustion_closure_passed") is True,
        "admission_reusable": bool(
            closure.get("admission_reusable") is True or non_claims.get("admission_reusable") is True
        ),
        "follow_on_steps_authorized": bool(
            closure.get("follow_on_steps_authorized") is True
            or non_claims.get("follow_on_steps_authorized") is True
        ),
        "follow_on_work_authorized": bool(non_claims.get("follow_on_work_authorized") is True),
        "workflow_lane_created": bool(
            closure.get("workflow_lane_created") is True or non_claims.get("workflow_engine_created") is True
        ),
        "reentry_surfaces_became_authority": bool(
            non_claims.get("reentry_admissibility_became_authority") is True
            or non_claims.get("receipt_became_authority") is True
        ),
        "recognition_posture": surfaces.get("recognition_posture"),
    }


def _integrate_body_signal_posture(
    v6: Mapping[str, Any],
    selected: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    surfaces = _as_mapping(v6.get("recognized_body_signal_surfaces"))
    relation = _as_mapping(surfaces.get("scoped_signal_remains"))
    accepted_relation = _as_mapping(surfaces.get("accepted_signal_remains"))
    recognition = _as_mapping(selected.get("selected_body_signal_recognition_result"))
    blocked_recognition = _as_mapping(selected.get("selected_blocked_body_signal_recognition_result"))
    acceptance = _as_mapping(selected.get("selected_body_signal_acceptance_result"))
    scope = _as_mapping(selected.get("selected_body_signal_scope_result"))
    declared_scope = _as_mapping(surfaces.get("declared_scope"))

    no_authority_or_permission = not any(
        non_claims.get(key) is True
        for key in (
            "signal_recognition_became_authority",
            "signal_acceptance_became_authority",
            "signal_scope_became_authority",
            "authority_created",
            "permission_created",
            "currentness_created",
            "action_authorized",
        )
    )
    non_operative = not any(
        non_claims.get(key) is True
        for key in (
            "presence_established",
            "threshold_met",
            "truth_created",
            "action_authorized",
            "signal_router_created",
            "workflow_engine_created",
            "event_bus_created",
            "body_relevance_medium_created",
            "follow_on_work_authorized",
        )
    )
    scoped_no_outside = non_claims.get("applied_outside_declared_scope") is not True

    return {
        "selected_body_signal_recognition_result": copy.deepcopy(recognition),
        "selected_blocked_body_signal_recognition_result": copy.deepcopy(blocked_recognition),
        "selected_body_signal_acceptance_result": copy.deepcopy(acceptance),
        "selected_body_signal_scope_result": copy.deepcopy(scope),
        "recognition_outcome": recognition.get("outcome"),
        "blocked_false_permission_signal_outcome": blocked_recognition.get("outcome"),
        "blocked_false_permission_signal_code": blocked_recognition.get("block_code"),
        "acceptance_outcome": acceptance.get("outcome"),
        "scope_outcome": scope.get("outcome"),
        "accepted_matter_id": scope.get("accepted_matter_id") or acceptance.get("declared_matter_id"),
        "declared_scope_id": scope.get("declared_scope_id") or declared_scope.get("scope_id"),
        "declared_scope_kind": scope.get("declared_scope_kind") or declared_scope.get("scope_kind"),
        "recognized_downstream_by_v6": bool(surfaces),
        "recognition_basis_passed": surfaces.get("recognition_basis_passed") is True,
        "acceptance_basis_passed": surfaces.get("acceptance_basis_passed") is True,
        "scope_boundary_passed": surfaces.get("scope_boundary_passed") is True,
        "scope_limits_passed": surfaces.get("scope_limits_passed") is True,
        "hierarchy_constraints_passed": (
            surfaces.get("scope_hierarchy_constraints_passed") is True
            or surfaces.get("acceptance_hierarchy_constraints_passed") is True
        ),
        "correspondence_requirements_passed": (
            surfaces.get("scope_correspondence_requirements_passed") is True
            or surfaces.get("acceptance_correspondence_requirements_passed") is True
        ),
        "non_claims_passed": (
            surfaces.get("scope_non_claims_passed") is True
            or surfaces.get("acceptance_non_claims_passed") is True
        ),
        "accepted_signal_remains_non_operative": all(
            accepted_relation.get(key) is True
            for key in (
                "non_authoritative",
                "non_permission",
                "non_currentness",
                "not_present",
                "not_threshold",
                "not_truth",
                "no_action",
                "no_routing",
                "no_workflow",
                "no_body_relevance_medium",
                "no_follow_on_work",
            )
        )
        if accepted_relation
        else non_operative,
        "scoped_signal_remains_non_operative": all(
            relation.get(key) is True
            for key in (
                "non_authoritative",
                "non_permission",
                "non_currentness",
                "not_present",
                "not_threshold",
                "not_truth",
                "no_action",
                "no_routing",
                "no_workflow",
                "no_body_relevance_medium",
                "no_follow_on_work",
                "no_application_outside_declared_scope",
            )
        )
        if relation
        else non_operative and scoped_no_outside,
        "signal_line_remains_non_authoritative_non_permission_no_action": no_authority_or_permission,
        "signal_line_remains_non_operative": non_operative,
        "scoped_signal_applies_only_inside_declared_scope": scoped_no_outside,
        "signal_surfaces_did_not_become_current_governing_basis": not bool(
            non_claims.get("signal_recognition_became_authority")
            or non_claims.get("signal_acceptance_became_authority")
            or non_claims.get("signal_scope_became_authority")
        ),
    }


def _integrate_derivative_vessel_posture(
    v6: Mapping[str, Any],
    selected: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    surfaces = _as_mapping(v6.get("recognized_derivative_vessel_relation_surfaces"))
    relation = _as_mapping(surfaces.get("recognized_derivative_vessel_relation"))
    relation_remains = _as_mapping(surfaces.get("relation_remains"))
    selected_relation = _as_mapping(selected.get("selected_derivative_vessel_relation_boundary_result"))
    blocked_relation = _as_mapping(
        selected.get("selected_blocked_derivative_vessel_relation_boundary_result")
    )
    selected_derivative = _as_mapping(selected.get("selected_derivative_vessel_result"))

    return {
        "selected_derivative_vessel_relation_boundary_result": copy.deepcopy(selected_relation),
        "selected_blocked_derivative_vessel_relation_boundary_result": copy.deepcopy(blocked_relation),
        "selected_derivative_vessel_result": copy.deepcopy(selected_derivative),
        "relation_boundary_outcome": selected_relation.get("outcome"),
        "blocked_relation_boundary_outcome": blocked_relation.get("outcome"),
        "blocked_relation_boundary_code": blocked_relation.get("block_code"),
        "selected_source_body_basis_id": relation.get("source_body_basis_id"),
        "selected_source_body_basis_path": relation.get("source_body_basis_path"),
        "selected_source_surface_id": relation.get("source_surface_id"),
        "selected_source_surface_path": relation.get("source_surface_path"),
        "selected_derivative_vessel_result_id": relation.get("derivative_vessel_result_id")
        or selected_derivative.get("result_id"),
        "selected_derivative_vessel_result_path": relation.get("derivative_vessel_result_path")
        or selected_derivative.get("result_path"),
        "selected_derivative_vessel_result_outcome": relation.get("derivative_vessel_result_outcome")
        or selected_derivative.get("outcome"),
        "derivative_output_family": relation.get("derivative_output_family")
        or selected_derivative.get("derivative_output_family"),
        "relation_id": relation.get("relation_id") or surfaces.get("relation_id"),
        "relation_type": relation.get("relation_type"),
        "recognized_downstream_by_v6": bool(surfaces),
        "relation_remains_downstream": bool(
            surfaces.get("downstream") is True or relation_remains.get("downstream") is True
        ),
        "source_body_basis_remains_upstream": bool(
            relation_remains.get("source_body_basis_upstream") is True
        ),
        "derivative_vessel_result_remains_downstream": bool(
            relation_remains.get("derivative_vessel_result_downstream") is True
            or surfaces.get("derivative_preserved") is True
        ),
        "operator_facing_output_remains_downstream": bool(
            relation_remains.get("operator_facing_output_downstream_where_present") is True
            or surfaces.get("operator_downstream_where_present") is True
        ),
        "relation_remains_additive_only": bool(
            surfaces.get("additive_only") is True or relation_remains.get("additive_only") is True
        ),
        "source_preserved": bool(
            surfaces.get("source_preserved") is True or relation_remains.get("source_preserved") is True
        ),
        "derivative_preserved": bool(
            surfaces.get("derivative_preserved") is True
            or relation_remains.get("derivative_preserved") is True
        ),
        "relation_creates_no_authority": bool(
            surfaces.get("no_authority") is True and non_claims.get("derivative_vessel_relation_became_authority") is False
        ),
        "relation_creates_no_permission": bool(
            surfaces.get("no_permission") is True and non_claims.get("derivative_vessel_relation_became_permission") is False
        ),
        "relation_creates_no_currentness": bool(
            surfaces.get("no_currentness") is True
            and non_claims.get("derivative_vessel_relation_became_currentness") is False
        ),
        "relation_creates_no_adoption": bool(
            surfaces.get("no_adoption") is True
            and non_claims.get("derivative_vessel_relation_created_adoption") is False
        ),
        "relation_creates_no_privileged_standing": bool(
            surfaces.get("no_privileged_standing") is True
            and non_claims.get("derivative_vessel_relation_created_privileged_standing") is False
        ),
        "relation_creates_no_public_standing_change": bool(
            surfaces.get("no_public_release") is True
            and non_claims.get("derivative_vessel_relation_created_public_release") is False
        ),
        "relation_replaces_no_source": bool(
            surfaces.get("no_source_replacement") is True
            and non_claims.get("derivative_vessel_relation_replaced_source") is False
        ),
        "relation_completes_no_final_governance": bool(
            surfaces.get("no_final_governance") is True
            and non_claims.get("derivative_vessel_relation_completed_final_governance") is False
        ),
        "relation_completes_no_final_system_identity": bool(
            surfaces.get("no_final_system_identity") is True
            and non_claims.get("derivative_vessel_relation_completed_final_system_identity") is False
        ),
        "relation_completes_no_continuity": bool(
            surfaces.get("no_continuity_completion") is True
            and non_claims.get("derivative_vessel_relation_completed_continuity") is False
        ),
        "relation_creates_no_general_vessel_permission": bool(
            surfaces.get("no_general_vessel_permission") is True
            and non_claims.get("derivative_vessel_relation_created_general_vessel_permission") is False
        ),
        "relation_authorizes_no_follow_on_vessels": bool(
            surfaces.get("no_follow_on_vessel_authorization") is True
            and non_claims.get("derivative_vessel_relation_authorized_follow_on_vessels") is False
        ),
        "relation_boundary_did_not_become_current_governing_basis": bool(
            non_claims.get("derivative_vessel_relation_became_current_or_governing_basis") is False
        ),
        "relation_boundary_surfaces_remain_downstream_non_authoritative": bool(
            surfaces.get("derivative_vessel_relation_boundary_surfaces_remain_downstream") is True
            and surfaces.get("derivative_vessel_relation_boundary_surfaces_remain_non_authoritative") is True
        ),
    }


def _integrate_operator_posture(v6: Mapping[str, Any], selected: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, Any]:
    operator_results = _as_list(selected.get("selected_operator_terminal_brief_results"))
    return {
        "selected_operator_terminal_brief_results": copy.deepcopy(operator_results),
        "operator_facing_result_count": len(operator_results),
        "operator_facing_success_count": sum(
            1 for item in operator_results if isinstance(item, Mapping) and item.get("outcome") == BRIEF_RENDERED
        ),
        "recognized_downstream_by_v6": bool(v6.get("recognized_operator_facing_surfaces")),
        "operator_output_became_source": bool(non_claims.get("operator_outputs_upgraded_to_source")),
        "operator_output_became_authority": False,
        "operator_output_became_currentness": False,
        "operator_output_became_permission": False,
    }


def _build_integrated_sections(
    v6: Mapping[str, Any],
    selected_inputs: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, dict[str, Any]]:
    return {
        "integrated_current_governing_basis": _integrate_current_governing_basis(v6, non_claims),
        "integrated_reentry_posture": _integrate_reentry_posture(v6, selected_inputs, non_claims),
        "integrated_body_signal_posture": _integrate_body_signal_posture(v6, selected_inputs, non_claims),
        "integrated_derivative_vessel_posture": _integrate_derivative_vessel_posture(
            v6, selected_inputs, non_claims
        ),
        "integrated_operator_posture": _integrate_operator_posture(v6, selected_inputs, non_claims),
    }


def _build_checks(
    v6: Mapping[str, Any] | None,
    selected_inputs: Mapping[str, Any],
    integrated: Mapping[str, Mapping[str, Any]],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    v6 = v6 or {}
    current = _as_mapping(integrated.get("integrated_current_governing_basis"))
    reentry = _as_mapping(integrated.get("integrated_reentry_posture"))
    signal = _as_mapping(integrated.get("integrated_body_signal_posture"))
    vessel = _as_mapping(integrated.get("integrated_derivative_vessel_posture"))
    operator = _as_mapping(integrated.get("integrated_operator_posture"))

    body_signal_line_stands = (
        signal.get("recognition_outcome") == SIGNAL_RECOGNIZED
        and signal.get("acceptance_outcome") == SIGNAL_ACCEPTED
        and signal.get("scope_outcome") == SIGNAL_SCOPED
        and signal.get("accepted_matter_id") == ACCEPTED_MATTER_ID
        and signal.get("declared_scope_id") == DECLARED_SCOPE_ID
    )
    relation_stands = (
        vessel.get("relation_boundary_outcome") == DERIVATIVE_VESSEL_RELATION_RECOGNIZED
        and bool(vessel.get("relation_id"))
    )
    derivative_success = (
        vessel.get("selected_derivative_vessel_result_outcome") == ANSWERED_DERIVATIVE_READ
        or bool(v6.get("recognized_derivative_surfaces"))
    )
    operator_success_or_absent = operator.get("operator_facing_result_count") == 0 or (
        operator.get("operator_facing_success_count", 0) > 0
        and operator.get("recognized_downstream_by_v6") is True
    )
    non_claims_remain_false = all(non_claims.get(key) is False for key in FALSE_NON_CLAIMS)

    return [
        _check(
            "self_orientation_v6_exists",
            bool(v6),
            "one current self-orientation v6 artifact is selected",
            bool(v6),
            "SELF_ORIENTATION_V6_MISSING",
        ),
        _check(
            "self_orientation_v6_is_self_oriented",
            v6.get("outcome") == SELF_ORIENTED,
            "selected v6 outcome is SELF_ORIENTED",
            v6.get("outcome"),
            "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED",
        ),
        _check(
            "current_governing_basis_recognized",
            current.get("current_executable_core_line_recognized") is True
            and current.get("governing_effective_basis_recognized") is True
            and current.get("current_state_surfaces_recognized") is True,
            "current executable, governing/effective, and current-state surfaces are recognized",
            current,
            "CURRENT_GOVERNING_BASIS_NOT_RECOGNIZED",
        ),
        _check(
            "current_governing_basis_upstream_derived",
            current.get("source_body_basis_remains_upstream") is True
            and current.get("downstream_surfaces_do_not_determine_current_governing_basis") is True,
            "current/governing basis remains upstream-derived",
            current,
            "CURRENT_GOVERNING_BASIS_DERIVED_FROM_DOWNSTREAM_SURFACE",
        ),
        _check(
            "reentry_closure_remains_closed",
            reentry.get("admissibility_outcome") == REENTRY_ADMITTED
            and reentry.get("receipt_outcome") == REENTRY_RECEIVED
            and reentry.get("recognized_downstream_by_v6") is True
            and reentry.get("closure_exhaustion_passed") is True
            and reentry.get("admission_reusable") is False
            and reentry.get("workflow_lane_created") is False
            and reentry.get("reentry_surfaces_became_authority") is False,
            "re-entry remains downstream, closed, exhausted, non-reusable, and non-authoritative",
            reentry,
            "REENTRY_CLOSURE_MISMATCH",
        ),
        _check(
            "follow_on_authorization_remains_false",
            reentry.get("follow_on_steps_authorized") is False
            and reentry.get("follow_on_work_authorized") is False
            and non_claims.get("follow_on_steps_authorized") is False
            and non_claims.get("follow_on_work_authorized") is False,
            "follow-on work and steps remain unauthorized",
            {
                "follow_on_steps_authorized": reentry.get("follow_on_steps_authorized"),
                "follow_on_work_authorized": reentry.get("follow_on_work_authorized"),
            },
            "FOLLOW_ON_AUTHORIZATION_LEAK",
        ),
        _check(
            "body_signal_recognition_acceptance_scope_line_stands",
            body_signal_line_stands,
            "body-signal recognition, acceptance, and scope stand with bounded matter and scope",
            signal,
            "BODY_SIGNAL_LINE_MISSING",
        ),
        _check(
            "body_signal_line_remains_non_operative",
            signal.get("accepted_signal_remains_non_operative") is True
            and signal.get("scoped_signal_remains_non_operative") is True
            and signal.get("signal_line_remains_non_operative") is True,
            "accepted and scoped signal remain non-operative",
            signal,
            "BODY_SIGNAL_LINE_OPERATIVE_LEAK",
        ),
        _check(
            "body_signal_line_does_not_become_authority_currentness_permission_action",
            signal.get("signal_line_remains_non_authoritative_non_permission_no_action") is True
            and signal.get("signal_surfaces_did_not_become_current_governing_basis") is True,
            "signal line does not become authority, currentness, permission, or action",
            signal,
            "BODY_SIGNAL_LINE_AUTHORITY_OR_PERMISSION_LEAK",
        ),
        _check(
            "body_signal_scope_does_not_apply_outside_declared_scope",
            signal.get("scoped_signal_applies_only_inside_declared_scope") is True,
            "scoped signal does not apply outside declared scope",
            signal.get("scoped_signal_applies_only_inside_declared_scope"),
            "BODY_SIGNAL_SCOPE_OUTSIDE_DECLARED_SCOPE",
        ),
        _check(
            "derivative_vessel_relation_boundary_stands",
            relation_stands,
            "one derivative-vessel relation boundary result is DERIVATIVE_VESSEL_RELATION_RECOGNIZED",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_BOUNDARY_MISSING"
            if not vessel.get("relation_boundary_outcome")
            else "DERIVATIVE_VESSEL_RELATION_BOUNDARY_NOT_RECOGNIZED",
        ),
        _check(
            "derivative_vessel_relation_remains_downstream",
            vessel.get("relation_remains_downstream") is True
            and vessel.get("source_body_basis_remains_upstream") is True
            and vessel.get("derivative_vessel_result_remains_downstream") is True
            and vessel.get("relation_boundary_surfaces_remain_downstream_non_authoritative") is True,
            "relation boundary remains downstream and source/body basis remains upstream",
            vessel,
            "CURRENT_GOVERNING_BASIS_DERIVED_FROM_DOWNSTREAM_SURFACE",
        ),
        _check(
            "derivative_vessel_relation_remains_additive",
            vessel.get("relation_remains_additive_only") is True
            and vessel.get("source_preserved") is True
            and vessel.get("derivative_preserved") is True,
            "relation remains additive and preserves source and derivative bases",
            vessel,
            "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "derivative_vessel_relation_creates_no_authority",
            vessel.get("relation_creates_no_authority") is True,
            "relation creates no authority",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_AUTHORITY_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_currentness",
            vessel.get("relation_creates_no_currentness") is True,
            "relation creates no currentness",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_CURRENTNESS_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_permission",
            vessel.get("relation_creates_no_permission") is True,
            "relation creates no permission",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_PERMISSION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_adoption",
            vessel.get("relation_creates_no_adoption") is True,
            "relation creates no adoption",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_ADOPTION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_privileged_standing",
            vessel.get("relation_creates_no_privileged_standing") is True,
            "relation creates no privileged standing",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_PRIVILEGED_STANDING_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_public_standing_change",
            vessel.get("relation_creates_no_public_standing_change") is True,
            "relation creates no public standing change",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_PRIVILEGED_STANDING_LEAK",
        ),
        _check(
            "derivative_vessel_relation_replaces_no_source",
            vessel.get("relation_replaces_no_source") is True,
            "relation replaces no source",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_SOURCE_REPLACEMENT_LEAK",
        ),
        _check(
            "derivative_vessel_relation_completes_no_final_governance",
            vessel.get("relation_completes_no_final_governance") is True,
            "relation completes no final governance",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_FINAL_GOVERNANCE_LEAK",
        ),
        _check(
            "derivative_vessel_relation_completes_no_final_system_identity",
            vessel.get("relation_completes_no_final_system_identity") is True,
            "relation completes no final system identity",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_FINAL_SYSTEM_IDENTITY_LEAK",
        ),
        _check(
            "derivative_vessel_relation_completes_no_continuity",
            vessel.get("relation_completes_no_continuity") is True,
            "relation completes no continuity",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_CONTINUITY_COMPLETION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_creates_no_general_vessel_permission",
            vessel.get("relation_creates_no_general_vessel_permission") is True,
            "relation creates no general vessel permission",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_GENERAL_PERMISSION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_authorizes_no_follow_on_vessels",
            vessel.get("relation_authorizes_no_follow_on_vessels") is True,
            "relation authorizes no follow-on vessels",
            vessel,
            "DERIVATIVE_VESSEL_RELATION_FOLLOW_ON_AUTHORIZATION_LEAK",
        ),
        _check(
            "derivative_vessel_relation_boundary_does_not_determine_current_governing_basis",
            vessel.get("relation_boundary_did_not_become_current_governing_basis") is True,
            "relation boundary does not become current/governing basis",
            vessel,
            "CURRENT_GOVERNING_BASIS_DERIVED_FROM_DOWNSTREAM_SURFACE",
        ),
        _check(
            "derivative_vessel_output_remains_derivative",
            derivative_success,
            "selected derivative vessel output remains derivative",
            vessel,
            "DERIVATIVE_OUTPUT_SOURCE_COLLAPSE",
        ),
        _check(
            "operator_facing_output_remains_downstream",
            operator_success_or_absent and operator.get("operator_output_became_source") is False,
            "operator-facing output remains downstream where present",
            operator,
            "OPERATOR_OUTPUT_SOURCE_COLLAPSE",
        ),
        _check(
            "no_latest_file_currentness",
            non_claims.get("latest_file_currentness") is False,
            "latest-file recency does not create currentness",
            non_claims.get("latest_file_currentness"),
            "LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "no_recency_fraud",
            non_claims.get("recency_fraud") is False,
            "recency fraud remains false",
            non_claims.get("recency_fraud"),
            "LATEST_FILE_RECENCY_REFUSED",
        ),
        _check(
            "no_mutation_replay_merge",
            non_claims.get("mutation_performed") is False
            and non_claims.get("replay_performed") is False
            and non_claims.get("merge_performed") is False,
            "conformance pass performs no mutation, replay, or merge",
            {
                "mutation_performed": non_claims.get("mutation_performed"),
                "replay_performed": non_claims.get("replay_performed"),
                "merge_performed": non_claims.get("merge_performed"),
            },
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
        _check(
            "non_claims_remain_false",
            non_claims_remain_false,
            "all integrated non-claims remain false",
            {key: non_claims.get(key) for key in sorted(FALSE_NON_CLAIMS) if non_claims.get(key) is True},
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]


def _build_current_body_conformance_basis(
    selected_inputs: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    selected_v6 = _as_mapping(selected_inputs.get("selected_self_orientation_v6_result"))
    return {
        "basis_kind": "integrated_current_body_conformance_pass",
        "selected_self_orientation_v6_result_id": selected_v6.get("result_id"),
        "selected_self_orientation_v6_result_path": selected_v6.get("result_path"),
        "selected_self_orientation_v6_outcome": selected_v6.get("outcome"),
        "conformance_outcome": outcome,
        "evaluated_posture": (
            "current self-orientation v6 plus already-standing downstream re-entry, body-signal, "
            "derivative-vessel relation, derivative vessel, and operator-facing surfaces"
        ),
        "does_not_create_authority": True,
        "does_not_create_permission": True,
        "does_not_create_currentness": True,
        "does_not_authorize_follow_on_work": True,
        "does_not_mutate_upstream_artifacts": True,
    }


def _build_result(
    self_orientation_v6_result: Mapping[str, Any] | None,
    self_orientation_v6_path: Path | str | None,
    selection_mode: str,
    preselected_inputs: Mapping[str, Any] | None = None,
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> dict[str, Any]:
    v6 = _copy_mapping(self_orientation_v6_result)
    selected_inputs = _copy_mapping(preselected_inputs) or _build_selected_inputs(
        v6, self_orientation_v6_path, selection_mode
    )
    non_claims = _combined_non_claims(v6)
    integrated = _build_integrated_sections(v6, selected_inputs, non_claims)
    checks = _build_checks(v6, selected_inputs, integrated, non_claims)

    failed_check = _first_failed_check(checks)
    block_code = forced_block_code or (failed_check.get("block_code") if failed_check else None)
    block_reason = forced_block_reason or _block_reason(block_code, failed_check)
    outcome = BLOCKED if block_code else BODY_CONFORMANT
    selected_v6 = _as_mapping(selected_inputs.get("selected_self_orientation_v6_result"))
    metadata = _metadata(selected_v6.get("result_id"))

    result = {
        "current_body_conformance_metadata": metadata,
        "selected_conformance_inputs": selected_inputs,
        "integrated_current_governing_basis": integrated["integrated_current_governing_basis"],
        "integrated_reentry_posture": integrated["integrated_reentry_posture"],
        "integrated_body_signal_posture": integrated["integrated_body_signal_posture"],
        "integrated_derivative_vessel_posture": integrated["integrated_derivative_vessel_posture"],
        "integrated_operator_posture": integrated["integrated_operator_posture"],
        "integrated_non_claims": {
            "all_required_non_claims_false": all(
                non_claims.get(key) is False for key in FALSE_NON_CLAIMS
            ),
            "false_non_claims": copy.deepcopy(non_claims),
        },
        "current_body_conformance_checks": checks,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "current_body_conformance_basis": _build_current_body_conformance_basis(
            selected_inputs, outcome
        ),
        "current_body_conformance_summary": {},
        "non_claims": copy.deepcopy(non_claims),
    }
    result["current_body_conformance_summary"] = build_current_body_conformance_summary(result)
    return result


def run_current_body_conformance_pass(
    self_orientation_v6_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Run one bounded integrated conformance pass over selected standing artifacts."""

    if self_orientation_v6_result is None:
        discovered, path = _latest_successful_v6_artifact()
        if discovered is None:
            return _build_result(
                None,
                None,
                "latest_successful_v6_artifact",
                forced_block_code="SELF_ORIENTATION_V6_MISSING",
                forced_block_reason=BLOCK_REASONS["SELF_ORIENTATION_V6_MISSING"],
            )
        return _build_result(discovered, path, "latest_successful_v6_artifact")

    if not isinstance(self_orientation_v6_result, Mapping):
        return _build_result(
            None,
            None,
            "provided_mapping",
            forced_block_code="SELF_ORIENTATION_V6_MALFORMED",
            forced_block_reason=BLOCK_REASONS["SELF_ORIENTATION_V6_MALFORMED"],
        )
    return _build_result(self_orientation_v6_result, None, "provided_mapping")


def run_current_body_conformance_pass_from_path(
    self_orientation_v6_result_path: Path | str,
) -> dict[str, Any]:
    """Run the conformance pass from one explicit current self-orientation v6 JSON path."""

    selected_path = Path(self_orientation_v6_result_path)
    try:
        selected = _read_json_mapping(
            selected_path,
            "SELF_ORIENTATION_V6_UNREADABLE",
            "SELF_ORIENTATION_V6_MALFORMED",
        )
    except CurrentBodyConformancePassError as exc:
        selected_inputs = {
            "selected_self_orientation_v6_result": {
                "result_id": None,
                "outcome": None,
                "result_path": _display_path(selected_path),
                "selection_mode": "provided_path",
            },
            "selection_posture": {
                "top_level_anchor": "current_self_orientation_v6",
                "path_supplied": True,
                "does_not_use_downstream_surface_as_current_governing_basis": True,
                "does_not_use_latest_file_recency_as_currentness": True,
            },
        }
        return _build_result(
            None,
            selected_path,
            "provided_path",
            preselected_inputs=selected_inputs,
            forced_block_code=exc.block_code,
            forced_block_reason=exc.block_reason,
        )
    return _build_result(selected, selected_path, "provided_path")


def build_current_body_conformance_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    checks = _as_list(result.get("current_body_conformance_checks"))
    selected = _as_mapping(result.get("selected_conformance_inputs"))
    current = _as_mapping(result.get("integrated_current_governing_basis"))
    reentry = _as_mapping(result.get("integrated_reentry_posture"))
    signal = _as_mapping(result.get("integrated_body_signal_posture"))
    vessel = _as_mapping(result.get("integrated_derivative_vessel_posture"))
    operator = _as_mapping(result.get("integrated_operator_posture"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))

    selected_v6 = _as_mapping(selected.get("selected_self_orientation_v6_result"))
    selected_admissibility = _as_mapping(selected.get("selected_reentry_admissibility_result"))
    selected_receipt = _as_mapping(selected.get("selected_reentry_receipt_result"))
    selected_recognition = _as_mapping(selected.get("selected_body_signal_recognition_result"))
    selected_acceptance = _as_mapping(selected.get("selected_body_signal_acceptance_result"))
    selected_scope = _as_mapping(selected.get("selected_body_signal_scope_result"))
    selected_relation = _as_mapping(
        selected.get("selected_derivative_vessel_relation_boundary_result")
    )
    selected_derivative = _as_mapping(selected.get("selected_derivative_vessel_result"))
    selected_operator_results = _as_list(selected.get("selected_operator_terminal_brief_results"))
    selected_operator = (
        _as_mapping(selected_operator_results[0])
        if selected_operator_results and isinstance(selected_operator_results[0], Mapping)
        else {}
    )
    failed_check_count = sum(1 for check in checks if not check.get("passed"))

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_self_orientation_v6_id": selected_v6.get("result_id"),
        "selected_self_orientation_v6_path": selected_v6.get("result_path"),
        "selected_self_orientation_v6_outcome": selected_v6.get("outcome"),
        "selected_reentry_admissibility_id": selected_admissibility.get("result_id"),
        "selected_reentry_receipt_id": selected_receipt.get("result_id"),
        "selected_body_signal_recognition_id": selected_recognition.get("result_id"),
        "selected_body_signal_acceptance_id": selected_acceptance.get("result_id"),
        "selected_body_signal_scope_id": selected_scope.get("result_id"),
        "selected_derivative_vessel_relation_boundary_id": selected_relation.get("result_id"),
        "selected_derivative_vessel_result_id": selected_derivative.get("result_id")
        or vessel.get("selected_derivative_vessel_result_id"),
        "selected_operator_facing_result_id": selected_operator.get("result_id"),
        "passed_check_count": len(checks) - failed_check_count,
        "failed_check_count": failed_check_count,
        "current_governing_basis_passed": current.get("current_executable_core_line_recognized") is True
        and current.get("governing_effective_basis_recognized") is True
        and current.get("current_state_surfaces_recognized") is True
        and current.get("downstream_surfaces_do_not_determine_current_governing_basis") is True,
        "reentry_posture_passed": reentry.get("admissibility_outcome") == REENTRY_ADMITTED
        and reentry.get("receipt_outcome") == REENTRY_RECEIVED
        and reentry.get("closure_exhaustion_passed") is True
        and reentry.get("follow_on_steps_authorized") is False,
        "body_signal_posture_passed": signal.get("recognition_outcome") == SIGNAL_RECOGNIZED
        and signal.get("acceptance_outcome") == SIGNAL_ACCEPTED
        and signal.get("scope_outcome") == SIGNAL_SCOPED
        and signal.get("scoped_signal_remains_non_operative") is True,
        "derivative_vessel_posture_passed": vessel.get("relation_boundary_outcome")
        == DERIVATIVE_VESSEL_RELATION_RECOGNIZED
        and vessel.get("relation_remains_downstream") is True
        and vessel.get("relation_creates_no_authority") is True
        and vessel.get("relation_creates_no_permission") is True
        and vessel.get("relation_creates_no_currentness") is True,
        "operator_posture_passed": operator.get("recognized_downstream_by_v6") is True
        or bool(selected_operator),
        "integrated_non_claims_passed": failed_check_count == 0
        or all(non_claims.get(key) is False for key in FALSE_NON_CLAIMS),
        "key_non_claims": {
            "authority_created": non_claims.get("authority_created"),
            "permission_created": non_claims.get("permission_created"),
            "currentness_created": non_claims.get("currentness_created"),
            "continuity_completed": non_claims.get("continuity_completed"),
            "final_governance_completed": non_claims.get("final_governance_completed"),
            "final_system_identity_completed": non_claims.get("final_system_identity_completed"),
            "source_replaced": non_claims.get("source_replaced"),
            "derivative_outputs_upgraded_to_source": non_claims.get(
                "derivative_outputs_upgraded_to_source"
            ),
            "operator_outputs_upgraded_to_source": non_claims.get(
                "operator_outputs_upgraded_to_source"
            ),
            "derivative_vessel_relation_became_authority": non_claims.get(
                "derivative_vessel_relation_became_authority"
            ),
            "derivative_vessel_relation_became_currentness": non_claims.get(
                "derivative_vessel_relation_became_currentness"
            ),
            "derivative_vessel_relation_became_permission": non_claims.get(
                "derivative_vessel_relation_became_permission"
            ),
            "derivative_vessel_relation_created_adoption": non_claims.get(
                "derivative_vessel_relation_created_adoption"
            ),
            "derivative_vessel_relation_created_privileged_standing": non_claims.get(
                "derivative_vessel_relation_created_privileged_standing"
            ),
            "derivative_vessel_relation_created_public_release": non_claims.get(
                "derivative_vessel_relation_created_public_release"
            ),
            "derivative_vessel_relation_replaced_source": non_claims.get(
                "derivative_vessel_relation_replaced_source"
            ),
            "derivative_vessel_relation_authorized_follow_on_vessels": non_claims.get(
                "derivative_vessel_relation_authorized_follow_on_vessels"
            ),
            "latest_file_currentness": non_claims.get("latest_file_currentness"),
            "recency_fraud": non_claims.get("recency_fraud"),
            "mutation_performed": non_claims.get("mutation_performed"),
            "replay_performed": non_claims.get("replay_performed"),
            "merge_performed": non_claims.get("merge_performed"),
            "presence_established": non_claims.get("presence_established"),
            "threshold_met": non_claims.get("threshold_met"),
            "truth_created": non_claims.get("truth_created"),
            "action_authorized": non_claims.get("action_authorized"),
            "applied_outside_declared_scope": non_claims.get(
                "applied_outside_declared_scope"
            ),
            "source_derivative_operator_collapsed": non_claims.get(
                "source_derivative_operator_collapsed"
            ),
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    metadata = _as_mapping(result.get("current_body_conformance_metadata"))
    selected = _as_mapping(result.get("selected_conformance_inputs"))
    selected_v6 = _as_mapping(selected.get("selected_self_orientation_v6_result"))
    basis = (
        selected_v6.get("result_id")
        or metadata.get("current_body_conformance_result_id")
        or "current_self_orientation_v6"
    )
    filename = f"{_safe_filename_part(basis)}__current_body_conformance_result.json"
    return CURRENT_BODY_CONFORMANCE_ROOT / filename


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_current_body_conformance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-body conformance result artifact."""

    selected_path = Path(output_path) if output_path is not None else _default_output_path(result)
    selected_path = _non_overwriting_path(selected_path)
    selected_path.parent.mkdir(parents=True, exist_ok=True)
    selected_path.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return selected_path
