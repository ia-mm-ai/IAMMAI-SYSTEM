"""Bounded post-conformance standing closure resolver.

This resolver records the meaning of a current `BODY_CONFORMANT` result without
turning conformance into authority, permission, currentness, signal, action,
completion, or continuation.
"""

from __future__ import annotations

import copy
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class CurrentBodyStandingClosurePostConformanceError(Exception):
    """Hard failure for malformed explicit closure inputs."""

    def __init__(self, block_code: str, block_reason: str) -> None:
        super().__init__(block_reason)
        self.block_code = block_code
        self.block_reason = block_reason


REPO_ROOT = Path(__file__).resolve().parents[1]

CURRENT_SELF_ORIENTATION_V6_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_self_orientation_v6"
)
CURRENT_BODY_CONFORMANCE_ROOT = (
    REPO_ROOT / "artifacts/integrity_host_v0_min_coexistence_current_body_conformance_pass"
)
CURRENT_BODY_STANDING_CLOSURE_POST_CONFORMANCE_ROOT = (
    REPO_ROOT
    / "artifacts/integrity_host_v0_min_coexistence_current_body_standing_closure_post_conformance"
)

RESOLVER_MODULE = "resolve_current_body_standing_closure_post_conformance"
RESULT_VERSION = "0.1.0"

SELF_ORIENTED = "SELF_ORIENTED"
BODY_CONFORMANT = "BODY_CONFORMANT"
CONFORMANCE_CLOSURE_RECORDED = "CONFORMANCE_CLOSURE_RECORDED"
BLOCKED = "BLOCKED"

BLOCK_REASONS = {
    "SELF_ORIENTATION_V6_MISSING": "No current self-orientation v6 result was supplied or discovered.",
    "SELF_ORIENTATION_V6_UNREADABLE": "The selected current self-orientation v6 artifact could not be read.",
    "SELF_ORIENTATION_V6_MALFORMED": "The selected current self-orientation v6 artifact is malformed.",
    "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED": "The selected current self-orientation v6 result is not SELF_ORIENTED.",
    "CURRENT_BODY_CONFORMANCE_MISSING": "No current-body conformance result was supplied or discovered.",
    "CURRENT_BODY_CONFORMANCE_UNREADABLE": "The selected current-body conformance artifact could not be read.",
    "CURRENT_BODY_CONFORMANCE_MALFORMED": "The selected current-body conformance artifact is malformed.",
    "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT": "The selected current-body conformance result is not BODY_CONFORMANT.",
    "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT": "The selected conformance result has failed checks.",
    "SELF_ORIENTATION_V6_CONFORMANCE_BASIS_MISMATCH": "The selected v6 basis does not match the conformance v6 basis.",
    "INTEGRATED_NON_CLAIM_MISSING_OR_FLIPPED": "A required integrated non-claim is missing or flipped.",
    "CONFORMANCE_TREATED_AS_AUTHORITY": "Conformance is being treated as authority.",
    "CONFORMANCE_TREATED_AS_PERMISSION": "Conformance is being treated as permission.",
    "CONFORMANCE_TREATED_AS_CURRENTNESS_CREATION": "Conformance is being treated as currentness creation.",
    "CONFORMANCE_TREATED_AS_PRESENCE": "Conformance is being treated as presence.",
    "CONFORMANCE_TREATED_AS_THRESHOLD": "Conformance is being treated as threshold.",
    "CONFORMANCE_TREATED_AS_TRUTH": "Conformance is being treated as truth.",
    "CONFORMANCE_TREATED_AS_ACTION": "Conformance is being treated as action.",
    "CONFORMANCE_TREATED_AS_FINAL_COMPLETION": "Conformance is being treated as final completion.",
    "CONFORMANCE_TREATED_AS_NEXT_STEP_AUTHORIZATION": "Conformance is being treated as next-step authorization.",
    "CONFORMANCE_TREATED_AS_SIGNAL_BY_DEFAULT": "Conformance is being treated as a signal by default.",
    "CONFORMANCE_FORCES_SELF_ORIENTATION_SUCCESSOR": "Conformance is forcing a self-orientation successor.",
    "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE": "Source, derivative, or operator distinction collapsed.",
    "LATEST_FILE_CURRENTNESS": "Latest-file recency is being treated as currentness.",
    "MUTATION_REPLAY_OR_MERGE_DETECTED": "Mutation, replay, or merge was detected.",
}

SOURCE_NON_CLAIMS = {
    "authority_created",
    "permission_created",
    "currentness_created",
    "continuity_completed",
    "final_governance_completed",
    "final_system_identity_completed",
    "source_replaced",
    "derivative_outputs_upgraded_to_source",
    "operator_outputs_upgraded_to_source",
    "follow_on_steps_authorized",
    "follow_on_work_authorized",
    "latest_file_currentness",
    "recency_fraud",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
    "presence_established",
    "threshold_met",
    "truth_created",
    "action_authorized",
    "source_derivative_operator_collapsed",
}

RESULT_NON_CLAIMS = SOURCE_NON_CLAIMS | {
    "conformance_became_authority",
    "conformance_became_permission",
    "conformance_became_currentness",
    "conformance_became_presence",
    "conformance_became_threshold",
    "conformance_became_truth",
    "conformance_became_action",
    "conformance_became_completion",
    "conformance_authorized_next_step",
    "conformance_became_signal_by_default",
    "self_orientation_successor_forced",
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
    selected_path = Path(path)
    try:
        text = selected_path.read_text(encoding="utf-8")
    except OSError as exc:
        raise CurrentBodyStandingClosurePostConformanceError(
            unreadable_code,
            f"{BLOCK_REASONS[unreadable_code]} path={_display_path(selected_path)} detail={exc}",
        ) from exc
    try:
        loaded = json.loads(text)
    except json.JSONDecodeError as exc:
        raise CurrentBodyStandingClosurePostConformanceError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={_display_path(selected_path)} detail={exc}",
        ) from exc
    if not isinstance(loaded, dict):
        raise CurrentBodyStandingClosurePostConformanceError(
            malformed_code,
            f"{BLOCK_REASONS[malformed_code]} path={_display_path(selected_path)} expected object",
        )
    return loaded


def _latest_successful_artifact(
    root: Path,
    outcome: str,
    unreadable_code: str,
    malformed_code: str,
) -> tuple[dict[str, Any] | None, Path | None]:
    if not root.exists():
        return None, None
    candidates: list[tuple[float, Path, dict[str, Any]]] = []
    for path in root.glob("*.json"):
        try:
            artifact = _read_json_mapping(path, unreadable_code, malformed_code)
        except CurrentBodyStandingClosurePostConformanceError:
            continue
        if artifact.get("outcome") == outcome:
            candidates.append((path.stat().st_mtime, path, artifact))
    if not candidates:
        return None, None
    _, path, artifact = sorted(candidates, key=lambda item: (item[0], item[1].name))[-1]
    return artifact, path


def _safe_filename_part(value: Any) -> str:
    text = str(value or "current_body_standing_closure").strip()
    text = re.sub(r"[^A-Za-z0-9_.-]+", "_", text)
    return text[:180] or "current_body_standing_closure"


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str,
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
    reason = BLOCK_REASONS.get(block_code, "The post-conformance closure request was blocked.")
    if failed_check:
        return f"{reason} failed check: {failed_check.get('check_name')}"
    return reason


def _self_orientation_v6_id(result: Mapping[str, Any]) -> str | None:
    return _nested(result, "current_self_orientation_v6_metadata", "self_orientation_result_id")


def _current_body_conformance_id(result: Mapping[str, Any]) -> str | None:
    return _nested(result, "current_body_conformance_metadata", "current_body_conformance_result_id")


def _selected_v6_id_from_conformance(result: Mapping[str, Any]) -> str | None:
    return (
        _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "result_id")
        or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_result_id")
        or _nested(result, "current_body_conformance_summary", "selected_self_orientation_v6_id")
    )


def _selected_v6_path_from_conformance(result: Mapping[str, Any]) -> str | None:
    return (
        _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "result_path")
        or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_result_path")
        or _nested(result, "current_body_conformance_summary", "selected_self_orientation_v6_path")
    )


def _path_matches(left: str | None, right: str | None) -> bool:
    if not left or not right:
        return True
    return left == right or _display_path(left) == _display_path(right)


def _failed_check_count(conformance_result: Mapping[str, Any]) -> int | None:
    summary_count = _nested(conformance_result, "current_body_conformance_summary", "failed_check_count")
    if isinstance(summary_count, int):
        return summary_count
    checks = _as_list(conformance_result.get("current_body_conformance_checks"))
    if checks:
        return sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    return None


def _passed_check_count(checks: list[dict[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _collect_source_non_claim_maps(conformance_result: Mapping[str, Any]) -> list[dict[str, Any]]:
    return [
        _as_mapping(conformance_result.get("non_claims")),
        _as_mapping(_nested(conformance_result, "integrated_non_claims", "false_non_claims")),
        _as_mapping(_nested(conformance_result, "current_body_conformance_summary", "key_non_claims")),
    ]


def _combined_non_claims(conformance_result: Mapping[str, Any] | None) -> dict[str, bool]:
    result = {key: False for key in sorted(RESULT_NON_CLAIMS)}
    if not conformance_result:
        return result
    for source in _collect_source_non_claim_maps(conformance_result):
        for key in RESULT_NON_CLAIMS:
            if source.get(key) is True:
                result[key] = True
            elif source.get(key) is False and result[key] is not True:
                result[key] = False
    return result


def _missing_source_non_claims(conformance_result: Mapping[str, Any] | None) -> list[str]:
    if not conformance_result:
        return sorted(SOURCE_NON_CLAIMS)
    sources = _collect_source_non_claim_maps(conformance_result)
    missing: list[str] = []
    for key in sorted(SOURCE_NON_CLAIMS):
        if not any(key in source for source in sources):
            missing.append(key)
    return missing


def _selected_self_orientation_basis(
    self_orientation_v6_result: Mapping[str, Any] | None,
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    result = self_orientation_v6_result or {}
    metadata = _as_mapping(result.get("current_self_orientation_v6_metadata"))
    block = _as_mapping(result.get("block"))
    return {
        "self_orientation_result_id": metadata.get("self_orientation_result_id"),
        "self_orientation_result_type": metadata.get("self_orientation_result_type"),
        "self_orientation_result_version": metadata.get("self_orientation_result_version"),
        "generated_at": metadata.get("generated_at"),
        "resolver_module": metadata.get("resolver_module"),
        "successor_of_module": metadata.get("successor_of_module"),
        "outcome": result.get("outcome"),
        "result_path": _display_path(path),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selection_mode": selection_mode,
    }


def _selected_conformance_basis(
    current_body_conformance_result: Mapping[str, Any] | None,
    path: Path | str | None,
    selection_mode: str,
) -> dict[str, Any]:
    result = current_body_conformance_result or {}
    metadata = _as_mapping(result.get("current_body_conformance_metadata"))
    summary = _as_mapping(result.get("current_body_conformance_summary"))
    block = _as_mapping(result.get("block"))
    return {
        "current_body_conformance_result_id": metadata.get("current_body_conformance_result_id"),
        "current_body_conformance_result_type": metadata.get("current_body_conformance_result_type"),
        "current_body_conformance_result_version": metadata.get("current_body_conformance_result_version"),
        "generated_at": metadata.get("generated_at"),
        "runner_module": metadata.get("runner_module"),
        "outcome": result.get("outcome"),
        "result_path": _display_path(path),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "failed_check_count": _failed_check_count(result),
        "selected_self_orientation_v6_result_id": _selected_v6_id_from_conformance(result),
        "selected_self_orientation_v6_result_path": _selected_v6_path_from_conformance(result),
        "selected_self_orientation_v6_outcome": (
            _nested(result, "selected_conformance_inputs", "selected_self_orientation_v6_result", "outcome")
            or _nested(result, "current_body_conformance_basis", "selected_self_orientation_v6_outcome")
            or summary.get("selected_self_orientation_v6_outcome")
        ),
        "current_governing_basis_passed": summary.get("current_governing_basis_passed"),
        "reentry_posture_passed": summary.get("reentry_posture_passed"),
        "body_signal_posture_passed": summary.get("body_signal_posture_passed"),
        "derivative_vessel_posture_passed": summary.get("derivative_vessel_posture_passed"),
        "operator_posture_passed": summary.get("operator_posture_passed"),
        "integrated_non_claims_passed": summary.get("integrated_non_claims_passed"),
        "selection_mode": selection_mode,
    }


def _what_conformance_means() -> dict[str, bool]:
    return {
        "selected_current_body_surfaces_cohere_under_conformance_pass": True,
        "current_governing_basis_is_upstream_derived": True,
        "downstream_surfaces_remain_downstream": True,
        "reentry_posture_remains_closed_and_non_reusable": True,
        "body_signal_posture_remains_non_operative": True,
        "derivative_vessel_relation_posture_remains_downstream_and_non_authoritative": True,
        "operator_facing_posture_remains_downstream_where_present": True,
        "source_derivative_operator_collapse_did_not_occur": True,
        "checked_non_claims_remain_false": True,
    }


def _what_conformance_does_not_mean() -> dict[str, bool]:
    return {
        "does_not_create_authority": True,
        "does_not_create_permission": True,
        "does_not_create_currentness": True,
        "does_not_authorize_next_step": True,
        "does_not_authorize_follow_on_work": True,
        "does_not_create_reusable_admission": True,
        "does_not_replace_source": True,
        "does_not_establish_presence": True,
        "does_not_establish_threshold": True,
        "does_not_create_truth": True,
        "does_not_authorize_action": True,
        "does_not_create_consequence": True,
        "does_not_complete_continuity": True,
        "does_not_complete_final_governance": True,
        "does_not_complete_final_system_identity": True,
        "does_not_create_generalized_vessel_permission": True,
        "does_not_create_body_relevance_medium": True,
        "does_not_create_signal_routing": True,
        "does_not_create_workflow": True,
        "does_not_create_roadmap": True,
        "does_not_complete_the_whole_body": True,
        "does_not_become_signal_by_default": True,
        "does_not_force_self_orientation_successor": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_surfaces": [
            "presence law",
            "threshold law",
            "truth law",
            "action/consequence law",
            "multi-carrier relation law",
            "persistence/registry law",
            "generalized vessel relation lifecycle",
            "body relevance medium",
            "further external contact surfaces",
            "future signal series or accumulation logic",
            "future self-orientation successor only if a new surface materially changes current posture",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _build_closure_checks(
    self_orientation_v6_result: Mapping[str, Any] | None,
    current_body_conformance_result: Mapping[str, Any] | None,
    selected_self_orientation_v6_basis: Mapping[str, Any],
    selected_current_body_conformance_basis: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    conformance_summary = _as_mapping(
        (current_body_conformance_result or {}).get("current_body_conformance_summary")
    )
    conformance_checks = _as_list(
        (current_body_conformance_result or {}).get("current_body_conformance_checks")
    )
    missing_non_claims = _missing_source_non_claims(current_body_conformance_result)
    flipped_source_non_claims = [
        key for key in sorted(SOURCE_NON_CLAIMS) if non_claims.get(key) is True
    ]
    v6_id = selected_self_orientation_v6_basis.get("self_orientation_result_id")
    conformance_v6_id = selected_current_body_conformance_basis.get(
        "selected_self_orientation_v6_result_id"
    )
    v6_path = selected_self_orientation_v6_basis.get("result_path")
    conformance_v6_path = selected_current_body_conformance_basis.get(
        "selected_self_orientation_v6_result_path"
    )
    v6_basis_matches = (
        bool(v6_id)
        and bool(conformance_v6_id)
        and v6_id == conformance_v6_id
        and _path_matches(v6_path, conformance_v6_path)
    )
    failed_check_count = selected_current_body_conformance_basis.get("failed_check_count")
    failed_conformance_checks = [
        check.get("check_name")
        for check in conformance_checks
        if isinstance(check, Mapping) and check.get("passed") is not True
    ]
    integrated_non_claims_pass = (
        conformance_summary.get("integrated_non_claims_passed") is True
        and _nested(current_body_conformance_result or {}, "integrated_non_claims", "all_required_non_claims_false") is True
        and not missing_non_claims
        and not flipped_source_non_claims
    )

    return [
        _check(
            "self_orientation_v6_exists",
            bool(self_orientation_v6_result),
            "one current self-orientation v6 result is selected",
            bool(self_orientation_v6_result),
            "SELF_ORIENTATION_V6_MISSING",
        ),
        _check(
            "self_orientation_v6_is_self_oriented",
            (self_orientation_v6_result or {}).get("outcome") == SELF_ORIENTED,
            "selected v6 outcome is SELF_ORIENTED",
            (self_orientation_v6_result or {}).get("outcome"),
            "SELF_ORIENTATION_V6_NOT_SELF_ORIENTED",
        ),
        _check(
            "current_body_conformance_exists",
            bool(current_body_conformance_result),
            "one current-body conformance result is selected",
            bool(current_body_conformance_result),
            "CURRENT_BODY_CONFORMANCE_MISSING",
        ),
        _check(
            "current_body_conformance_is_body_conformant",
            (current_body_conformance_result or {}).get("outcome") == BODY_CONFORMANT,
            "selected conformance outcome is BODY_CONFORMANT",
            (current_body_conformance_result or {}).get("outcome"),
            "CURRENT_BODY_CONFORMANCE_NOT_BODY_CONFORMANT",
        ),
        _check(
            "conformance_has_zero_failed_checks",
            failed_check_count == 0 and not failed_conformance_checks,
            "conformance failed check count is zero",
            {
                "failed_check_count": failed_check_count,
                "failed_conformance_checks": failed_conformance_checks,
            },
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "selected_v6_matches_conformance_selected_v6_basis",
            v6_basis_matches,
            "selected v6 id/path matches conformance selected v6 basis where exposed",
            {
                "selected_v6_id": v6_id,
                "conformance_v6_id": conformance_v6_id,
                "selected_v6_path": v6_path,
                "conformance_v6_path": conformance_v6_path,
            },
            "SELF_ORIENTATION_V6_CONFORMANCE_BASIS_MISMATCH",
        ),
        _check(
            "conformance_current_governing_basis_passed",
            conformance_summary.get("current_governing_basis_passed") is True,
            "conformance current/governing basis posture passed",
            conformance_summary.get("current_governing_basis_passed"),
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "conformance_reentry_posture_passed",
            conformance_summary.get("reentry_posture_passed") is True,
            "conformance re-entry posture passed",
            conformance_summary.get("reentry_posture_passed"),
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "conformance_body_signal_posture_passed",
            conformance_summary.get("body_signal_posture_passed") is True,
            "conformance body-signal posture passed",
            conformance_summary.get("body_signal_posture_passed"),
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "conformance_derivative_vessel_posture_passed",
            conformance_summary.get("derivative_vessel_posture_passed") is True,
            "conformance derivative-vessel posture passed",
            conformance_summary.get("derivative_vessel_posture_passed"),
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "conformance_operator_posture_passed",
            conformance_summary.get("operator_posture_passed") is True,
            "conformance operator posture passed",
            conformance_summary.get("operator_posture_passed"),
            "CURRENT_BODY_CONFORMANCE_FAILED_CHECKS_PRESENT",
        ),
        _check(
            "conformance_is_not_treated_as_authority",
            not (non_claims.get("authority_created") or non_claims.get("conformance_became_authority")),
            "conformance creates no authority",
            {
                "authority_created": non_claims.get("authority_created"),
                "conformance_became_authority": non_claims.get("conformance_became_authority"),
            },
            "CONFORMANCE_TREATED_AS_AUTHORITY",
        ),
        _check(
            "conformance_is_not_treated_as_permission",
            not (non_claims.get("permission_created") or non_claims.get("conformance_became_permission")),
            "conformance creates no permission",
            {
                "permission_created": non_claims.get("permission_created"),
                "conformance_became_permission": non_claims.get("conformance_became_permission"),
            },
            "CONFORMANCE_TREATED_AS_PERMISSION",
        ),
        _check(
            "conformance_is_not_treated_as_currentness_creation",
            not (non_claims.get("currentness_created") or non_claims.get("conformance_became_currentness")),
            "conformance creates no currentness",
            {
                "currentness_created": non_claims.get("currentness_created"),
                "conformance_became_currentness": non_claims.get("conformance_became_currentness"),
            },
            "CONFORMANCE_TREATED_AS_CURRENTNESS_CREATION",
        ),
        _check(
            "conformance_is_not_treated_as_presence",
            not (non_claims.get("presence_established") or non_claims.get("conformance_became_presence")),
            "conformance establishes no presence",
            {
                "presence_established": non_claims.get("presence_established"),
                "conformance_became_presence": non_claims.get("conformance_became_presence"),
            },
            "CONFORMANCE_TREATED_AS_PRESENCE",
        ),
        _check(
            "conformance_is_not_treated_as_threshold",
            not (non_claims.get("threshold_met") or non_claims.get("conformance_became_threshold")),
            "conformance meets no threshold",
            {
                "threshold_met": non_claims.get("threshold_met"),
                "conformance_became_threshold": non_claims.get("conformance_became_threshold"),
            },
            "CONFORMANCE_TREATED_AS_THRESHOLD",
        ),
        _check(
            "conformance_is_not_treated_as_truth",
            not (non_claims.get("truth_created") or non_claims.get("conformance_became_truth")),
            "conformance creates no truth",
            {
                "truth_created": non_claims.get("truth_created"),
                "conformance_became_truth": non_claims.get("conformance_became_truth"),
            },
            "CONFORMANCE_TREATED_AS_TRUTH",
        ),
        _check(
            "conformance_is_not_treated_as_action",
            not (non_claims.get("action_authorized") or non_claims.get("conformance_became_action")),
            "conformance authorizes no action",
            {
                "action_authorized": non_claims.get("action_authorized"),
                "conformance_became_action": non_claims.get("conformance_became_action"),
            },
            "CONFORMANCE_TREATED_AS_ACTION",
        ),
        _check(
            "conformance_is_not_treated_as_final_completion",
            not (
                non_claims.get("continuity_completed")
                or non_claims.get("final_governance_completed")
                or non_claims.get("final_system_identity_completed")
                or non_claims.get("conformance_became_completion")
            ),
            "conformance completes no continuity, final governance, or final system identity",
            {
                "continuity_completed": non_claims.get("continuity_completed"),
                "final_governance_completed": non_claims.get("final_governance_completed"),
                "final_system_identity_completed": non_claims.get("final_system_identity_completed"),
                "conformance_became_completion": non_claims.get("conformance_became_completion"),
            },
            "CONFORMANCE_TREATED_AS_FINAL_COMPLETION",
        ),
        _check(
            "conformance_is_not_treated_as_next_step_authorization",
            not (
                non_claims.get("follow_on_steps_authorized")
                or non_claims.get("follow_on_work_authorized")
                or non_claims.get("conformance_authorized_next_step")
            ),
            "conformance authorizes no next step or follow-on work",
            {
                "follow_on_steps_authorized": non_claims.get("follow_on_steps_authorized"),
                "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
                "conformance_authorized_next_step": non_claims.get("conformance_authorized_next_step"),
            },
            "CONFORMANCE_TREATED_AS_NEXT_STEP_AUTHORIZATION",
        ),
        _check(
            "conformance_is_not_treated_as_signal_by_default",
            non_claims.get("conformance_became_signal_by_default") is False,
            "conformance does not become signal by default",
            non_claims.get("conformance_became_signal_by_default"),
            "CONFORMANCE_TREATED_AS_SIGNAL_BY_DEFAULT",
        ),
        _check(
            "conformance_does_not_force_self_orientation_successor",
            non_claims.get("self_orientation_successor_forced") is False,
            "conformance does not force self-orientation successor",
            non_claims.get("self_orientation_successor_forced"),
            "CONFORMANCE_FORCES_SELF_ORIENTATION_SUCCESSOR",
        ),
        _check(
            "source_derivative_operator_collapse_remains_false",
            not (
                non_claims.get("source_replaced")
                or non_claims.get("derivative_outputs_upgraded_to_source")
                or non_claims.get("operator_outputs_upgraded_to_source")
                or non_claims.get("source_derivative_operator_collapsed")
            ),
            "source, derivative, and operator distinctions remain visible",
            {
                "source_replaced": non_claims.get("source_replaced"),
                "derivative_outputs_upgraded_to_source": non_claims.get("derivative_outputs_upgraded_to_source"),
                "operator_outputs_upgraded_to_source": non_claims.get("operator_outputs_upgraded_to_source"),
                "source_derivative_operator_collapsed": non_claims.get("source_derivative_operator_collapsed"),
            },
            "SOURCE_DERIVATIVE_OPERATOR_COLLAPSE",
        ),
        _check(
            "latest_file_currentness_remains_false",
            not (non_claims.get("latest_file_currentness") or non_claims.get("recency_fraud")),
            "latest-file currentness and recency fraud remain false",
            {
                "latest_file_currentness": non_claims.get("latest_file_currentness"),
                "recency_fraud": non_claims.get("recency_fraud"),
            },
            "LATEST_FILE_CURRENTNESS",
        ),
        _check(
            "mutation_replay_merge_remain_false",
            not (
                non_claims.get("mutation_performed")
                or non_claims.get("replay_performed")
                or non_claims.get("merge_performed")
            ),
            "mutation, replay, and merge remain false",
            {
                "mutation_performed": non_claims.get("mutation_performed"),
                "replay_performed": non_claims.get("replay_performed"),
                "merge_performed": non_claims.get("merge_performed"),
            },
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "integrated_non_claims_passed",
            integrated_non_claims_pass,
            "integrated non-claims pass and required source non-claims are present and false",
            {
                "integrated_non_claims_passed": conformance_summary.get("integrated_non_claims_passed"),
                "all_required_non_claims_false": _nested(
                    current_body_conformance_result or {},
                    "integrated_non_claims",
                    "all_required_non_claims_false",
                ),
                "missing_source_non_claims": missing_non_claims,
                "flipped_source_non_claims": flipped_source_non_claims,
            },
            "INTEGRATED_NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]


def _metadata(conformance_id: str | None, outcome: str) -> dict[str, Any]:
    stem = _safe_filename_part(conformance_id or "current_body_conformance")
    suffix = "recorded" if outcome == CONFORMANCE_CLOSURE_RECORDED else "blocked"
    return {
        "conformance_closure_result_id": (
            f"{stem}__current_body_standing_closure_post_conformance_{suffix}"
        ),
        "conformance_closure_result_type": (
            "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_BODY_STANDING_CLOSURE_POST_CONFORMANCE_RESULT"
        ),
        "conformance_closure_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _closure_statement(outcome: str) -> dict[str, bool]:
    recorded = outcome == CONFORMANCE_CLOSURE_RECORDED
    return {
        "conformance_question_closed": recorded,
        "next_work_question_opened": False,
        "conformance_recorded_as_permission": False,
        "conformance_recorded_as_authority": False,
        "conformance_recorded_as_signal": False,
        "self_orientation_successor_forced": False,
    }


def _build_result(
    self_orientation_v6_result: Mapping[str, Any] | None,
    current_body_conformance_result: Mapping[str, Any] | None,
    self_orientation_v6_path: Path | str | None,
    current_body_conformance_path: Path | str | None,
    self_orientation_selection_mode: str,
    conformance_selection_mode: str,
    forced_block_code: str | None = None,
    forced_block_reason: str | None = None,
) -> dict[str, Any]:
    v6 = _copy_mapping(self_orientation_v6_result)
    conformance = _copy_mapping(current_body_conformance_result)
    selected_v6_basis = _selected_self_orientation_basis(
        v6, self_orientation_v6_path, self_orientation_selection_mode
    )
    selected_conformance_basis = _selected_conformance_basis(
        conformance, current_body_conformance_path, conformance_selection_mode
    )
    non_claims = _combined_non_claims(conformance)
    checks = _build_closure_checks(
        v6,
        conformance,
        selected_v6_basis,
        selected_conformance_basis,
        non_claims,
    )
    failed_check = _first_failed_check(checks)
    block_code = forced_block_code or (failed_check.get("block_code") if failed_check else None)
    block_reason = forced_block_reason or _block_reason(block_code, failed_check)
    outcome = BLOCKED if block_code else CONFORMANCE_CLOSURE_RECORDED
    metadata = _metadata(
        selected_conformance_basis.get("current_body_conformance_result_id"),
        outcome,
    )
    result = {
        "conformance_closure_metadata": metadata,
        "selected_self_orientation_v6_basis": selected_v6_basis,
        "selected_current_body_conformance_basis": selected_conformance_basis,
        "closure_checks": checks,
        "closure_statement": _closure_statement(outcome),
        "what_conformance_means": _what_conformance_means(),
        "what_conformance_does_not_mean": _what_conformance_does_not_mean(),
        "what_remains_open": _what_remains_open(),
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "current_body_standing_closure_summary": {},
        "non_claims": copy.deepcopy(non_claims),
    }
    result["current_body_standing_closure_summary"] = build_current_body_standing_closure_summary(result)
    return result


def resolve_current_body_standing_closure_post_conformance(
    self_orientation_v6_result: Mapping[str, Any] | None = None,
    current_body_conformance_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one post-conformance standing closure result."""

    v6_path: Path | None = None
    conformance_path: Path | None = None
    v6_selection = "provided_mapping"
    conformance_selection = "provided_mapping"

    if self_orientation_v6_result is None:
        self_orientation_v6_result, v6_path = _latest_successful_artifact(
            CURRENT_SELF_ORIENTATION_V6_ROOT,
            SELF_ORIENTED,
            "SELF_ORIENTATION_V6_UNREADABLE",
            "SELF_ORIENTATION_V6_MALFORMED",
        )
        v6_selection = "latest_successful_self_orientation_v6_artifact"
        if self_orientation_v6_result is None:
            return _build_result(
                None,
                current_body_conformance_result,
                None,
                None,
                v6_selection,
                conformance_selection,
                forced_block_code="SELF_ORIENTATION_V6_MISSING",
                forced_block_reason=BLOCK_REASONS["SELF_ORIENTATION_V6_MISSING"],
            )
    elif not isinstance(self_orientation_v6_result, Mapping):
        return _build_result(
            None,
            current_body_conformance_result,
            None,
            None,
            v6_selection,
            conformance_selection,
            forced_block_code="SELF_ORIENTATION_V6_MALFORMED",
            forced_block_reason=BLOCK_REASONS["SELF_ORIENTATION_V6_MALFORMED"],
        )

    if current_body_conformance_result is None:
        current_body_conformance_result, conformance_path = _latest_successful_artifact(
            CURRENT_BODY_CONFORMANCE_ROOT,
            BODY_CONFORMANT,
            "CURRENT_BODY_CONFORMANCE_UNREADABLE",
            "CURRENT_BODY_CONFORMANCE_MALFORMED",
        )
        conformance_selection = "latest_successful_current_body_conformance_artifact"
        if current_body_conformance_result is None:
            return _build_result(
                self_orientation_v6_result,
                None,
                v6_path,
                None,
                v6_selection,
                conformance_selection,
                forced_block_code="CURRENT_BODY_CONFORMANCE_MISSING",
                forced_block_reason=BLOCK_REASONS["CURRENT_BODY_CONFORMANCE_MISSING"],
            )
    elif not isinstance(current_body_conformance_result, Mapping):
        return _build_result(
            self_orientation_v6_result,
            None,
            v6_path,
            None,
            v6_selection,
            conformance_selection,
            forced_block_code="CURRENT_BODY_CONFORMANCE_MALFORMED",
            forced_block_reason=BLOCK_REASONS["CURRENT_BODY_CONFORMANCE_MALFORMED"],
        )

    return _build_result(
        self_orientation_v6_result,
        current_body_conformance_result,
        v6_path,
        conformance_path,
        v6_selection,
        conformance_selection,
    )


def resolve_current_body_standing_closure_post_conformance_from_paths(
    self_orientation_v6_result_path: Path | str,
    current_body_conformance_result_path: Path | str,
) -> dict[str, Any]:
    """Resolve closure from explicit self-orientation v6 and conformance paths."""

    v6_path = Path(self_orientation_v6_result_path)
    conformance_path = Path(current_body_conformance_result_path)
    try:
        v6 = _read_json_mapping(
            v6_path,
            "SELF_ORIENTATION_V6_UNREADABLE",
            "SELF_ORIENTATION_V6_MALFORMED",
        )
    except CurrentBodyStandingClosurePostConformanceError as exc:
        return _build_result(
            None,
            None,
            v6_path,
            conformance_path,
            "provided_path",
            "provided_path",
            forced_block_code=exc.block_code,
            forced_block_reason=exc.block_reason,
        )
    try:
        conformance = _read_json_mapping(
            conformance_path,
            "CURRENT_BODY_CONFORMANCE_UNREADABLE",
            "CURRENT_BODY_CONFORMANCE_MALFORMED",
        )
    except CurrentBodyStandingClosurePostConformanceError as exc:
        return _build_result(
            v6,
            None,
            v6_path,
            conformance_path,
            "provided_path",
            "provided_path",
            forced_block_code=exc.block_code,
            forced_block_reason=exc.block_reason,
        )
    return _build_result(v6, conformance, v6_path, conformance_path, "provided_path", "provided_path")


def build_current_body_standing_closure_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    checks = _as_list(result.get("closure_checks"))
    failed_count = sum(1 for check in checks if isinstance(check, Mapping) and not check.get("passed"))
    selected_v6 = _as_mapping(result.get("selected_self_orientation_v6_basis"))
    selected_conformance = _as_mapping(result.get("selected_current_body_conformance_basis"))
    statement = _as_mapping(result.get("closure_statement"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = _as_mapping(result.get("block"))
    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_self_orientation_v6_id": selected_v6.get("self_orientation_result_id"),
        "selected_self_orientation_v6_path": selected_v6.get("result_path"),
        "selected_self_orientation_v6_outcome": selected_v6.get("outcome"),
        "selected_conformance_id": selected_conformance.get("current_body_conformance_result_id"),
        "selected_conformance_path": selected_conformance.get("result_path"),
        "selected_conformance_outcome": selected_conformance.get("outcome"),
        "passed_check_count": _passed_check_count(checks),
        "failed_check_count": failed_count,
        "conformance_closure_recorded": result.get("outcome") == CONFORMANCE_CLOSURE_RECORDED,
        "conformance_question_closed": statement.get("conformance_question_closed"),
        "next_work_question_opened": statement.get("next_work_question_opened"),
        "conformance_recorded_as_permission": statement.get("conformance_recorded_as_permission"),
        "conformance_recorded_as_authority": statement.get("conformance_recorded_as_authority"),
        "conformance_recorded_as_signal": statement.get("conformance_recorded_as_signal"),
        "self_orientation_successor_forced": statement.get("self_orientation_successor_forced"),
        "key_non_claims": {
            "authority_created": non_claims.get("authority_created"),
            "permission_created": non_claims.get("permission_created"),
            "currentness_created": non_claims.get("currentness_created"),
            "continuity_completed": non_claims.get("continuity_completed"),
            "final_governance_completed": non_claims.get("final_governance_completed"),
            "final_system_identity_completed": non_claims.get("final_system_identity_completed"),
            "source_replaced": non_claims.get("source_replaced"),
            "follow_on_steps_authorized": non_claims.get("follow_on_steps_authorized"),
            "follow_on_work_authorized": non_claims.get("follow_on_work_authorized"),
            "latest_file_currentness": non_claims.get("latest_file_currentness"),
            "recency_fraud": non_claims.get("recency_fraud"),
            "mutation_performed": non_claims.get("mutation_performed"),
            "replay_performed": non_claims.get("replay_performed"),
            "merge_performed": non_claims.get("merge_performed"),
            "presence_established": non_claims.get("presence_established"),
            "threshold_met": non_claims.get("threshold_met"),
            "truth_created": non_claims.get("truth_created"),
            "action_authorized": non_claims.get("action_authorized"),
            "source_derivative_operator_collapsed": non_claims.get("source_derivative_operator_collapsed"),
            "conformance_became_authority": non_claims.get("conformance_became_authority"),
            "conformance_became_permission": non_claims.get("conformance_became_permission"),
            "conformance_became_currentness": non_claims.get("conformance_became_currentness"),
            "conformance_became_presence": non_claims.get("conformance_became_presence"),
            "conformance_became_threshold": non_claims.get("conformance_became_threshold"),
            "conformance_became_truth": non_claims.get("conformance_became_truth"),
            "conformance_became_action": non_claims.get("conformance_became_action"),
            "conformance_became_completion": non_claims.get("conformance_became_completion"),
            "conformance_authorized_next_step": non_claims.get("conformance_authorized_next_step"),
            "conformance_became_signal_by_default": non_claims.get("conformance_became_signal_by_default"),
            "self_orientation_successor_forced": non_claims.get("self_orientation_successor_forced"),
        },
    }


def _default_output_path(result: Mapping[str, Any]) -> Path:
    selected = _as_mapping(result.get("selected_current_body_conformance_basis"))
    metadata = _as_mapping(result.get("conformance_closure_metadata"))
    basis = (
        selected.get("current_body_conformance_result_id")
        or metadata.get("conformance_closure_result_id")
        or "current_body_conformance"
    )
    filename = (
        f"{_safe_filename_part(basis)}"
        "__current_body_standing_closure_post_conformance_result.json"
    )
    return CURRENT_BODY_STANDING_CLOSURE_POST_CONFORMANCE_ROOT / filename


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    parent = path.parent
    stem = path.stem
    suffix = path.suffix
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_current_body_standing_closure_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive post-conformance closure result artifact."""

    selected_path = Path(output_path) if output_path is not None else _default_output_path(result)
    selected_path = _non_overwriting_path(selected_path)
    selected_path.parent.mkdir(parents=True, exist_ok=True)
    selected_path.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return selected_path
