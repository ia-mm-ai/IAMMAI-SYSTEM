"""Resolve bounded consumption of the v0-min effective family.

This module reads one effective-family resolution artifact and the effective
authority, run-family, preserved-run status, and current-governing artifacts
named by that resolution. It emits one explicit consumption result stating
whether those effective inputs were consumed for subsequent bounded work.

The resolver is additive engineering. It does not replay source actions into a
live host, merge preserved runs, mutate prior artifacts, complete continuity,
upgrade standing, define persistence or registry law, or treat the consumed
family as final governance.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from resolve_current_integrity_host_v0_min_coexistence_effective_family import (
    EFFECTIVE_FAMILY_RESOLUTION_ROOT as CURRENT_EFFECTIVE_FAMILY_RESOLUTION_ROOT,
    NON_CLAIM_DEFAULTS as EFFECTIVE_RESOLUTION_NON_CLAIMS,
    OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
    OUTCOME_CURRENT_FAMILY_EFFECTIVE,
    build_current_governing_summary,
    build_effective_family_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


EFFECTIVE_FAMILY_RESOLUTION_ROOT = CURRENT_EFFECTIVE_FAMILY_RESOLUTION_ROOT
EFFECTIVE_FAMILY_CONSUMPTION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_effective_family_consumption"
)

CONSUMPTION_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_EFFECTIVE_FAMILY_CONSUMPTION_RESULT"
)
CONSUMPTION_RESULT_VERSION = "0.1.0"

OUTCOME_CONSUMED = "CONSUMED"
OUTCOME_BLOCKED = "BLOCKED"

CANONICAL_CORE_EXECUTION_FILE = "src/integrity_host_v0_min_coexistence_v2.py"

SUPPORTED_EFFECTIVE_OUTCOMES = {
    OUTCOME_CURRENT_FAMILY_EFFECTIVE,
    OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE,
}

NON_CLAIM_DEFAULTS = {
    **EFFECTIVE_RESOLUTION_NON_CLAIMS,
    "final_effective_family_consumption_completed": False,
}

EFFECTIVE_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

PATH_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
)

BLOCK_REASONS = {
    "NO_EFFECTIVE_FAMILY_RESOLUTION": "No effective-family resolution artifact is available.",
    "EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE": "The selected effective-family resolution artifact is unreadable.",
    "EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE": "The selected effective-family resolution does not have a supported effective outcome.",
    "EFFECTIVE_FAMILY_ARTIFACT_UNREADABLE": "One or more effective family artifacts named by the resolution are unreadable.",
    "CANONICAL_EXECUTION_LINE_MISMATCH": "The effective family does not preserve the current canonical core execution line.",
    "EFFECTIVE_FAMILY_NOT_INTERNALLY_COHERENT": "The effective family artifacts do not name one coherent current governing run.",
    "EFFECTIVE_FAMILY_DOES_NOT_CORRESPOND_TO_RESOLUTION": "The effective artifacts do not correspond to the selected effective-family resolution.",
    "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT": "The prior family references are not visibly preserved and readable.",
    "REPLAY_SHORTCUT_REFUSED": "Effective-family consumption cannot proceed with replay marked true.",
    "MERGE_SHORTCUT_REFUSED": "Effective-family consumption cannot proceed with merge marked true.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Effective-family consumption cannot claim continuity completion.",
    "SILENT_STANDING_UPGRADE_REFUSED": "Effective-family consumption cannot silently upgrade standing.",
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": "Effective-family consumption cannot fall back to stale prior-family artifacts.",
    "MULTIPLE_EFFECTIVE_FAMILY_RESOLUTIONS_CONFLICT_UNRESOLVED": "Multiple effective-family resolutions conflict without a bounded selection surface.",
}


class EffectiveFamilyConsumptionError(RuntimeError):
    """Raised when bounded effective-family consumption cannot proceed."""


class _UnreadableArtifact(RuntimeError):
    """Private marker for readable-shape block cases."""


def discover_latest_effective_family_resolution(root: Path) -> Path:
    """Return the lexically latest supported effective-family resolution artifact."""

    selection = _select_default_effective_family_resolution(root)
    selected = selection.get("selected_effective_family_resolution_path")
    if not isinstance(selected, Path):
        raise EffectiveFamilyConsumptionError("No effective-family resolution found")
    return selected


def resolve_effective_family_consumption(
    effective_family_resolution: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve bounded consumption of one effective-family resolution."""

    if effective_family_resolution is None:
        selection = _select_default_effective_family_resolution(
            EFFECTIVE_FAMILY_RESOLUTION_ROOT
        )
        block = selection.get("block")
        if isinstance(block, Mapping):
            return _blocked_result(
                resolution=None,
                resolution_path=None,
                block_code=_str(block, "block_code", "selection block"),
                block_reason=_str(block, "block_reason", "selection block"),
                checks=[
                    _check(
                        "effective_family_resolution_selected",
                        "one supported effective-family resolution",
                        selection.get("actual"),
                        False,
                        _str(block, "block_code", "selection block"),
                    )
                ],
            )
        selected_path = selection.get("selected_effective_family_resolution_path")
        if not isinstance(selected_path, Path):
            raise EffectiveFamilyConsumptionError(
                "Selected effective-family resolution path is malformed"
            )
        try:
            resolution = _read_effective_family_resolution(selected_path)
        except _UnreadableArtifact:
            return _blocked_result(
                resolution=None,
                resolution_path=selected_path,
                block_code="EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE",
                block_reason=BLOCK_REASONS["EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE"],
                checks=[
                    _check(
                        "effective_family_resolution_readable",
                        "readable effective-family resolution artifact",
                        _display(selected_path),
                        False,
                        "EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE",
                    )
                ],
            )
        return _resolve_selected(resolution, selected_path, selection)

    if not isinstance(effective_family_resolution, Mapping):
        raise EffectiveFamilyConsumptionError(
            "Effective-family resolution must be a mapping or None"
        )
    resolution = _validate_effective_family_resolution(
        dict(effective_family_resolution)
    )
    return _resolve_selected(
        resolution,
        None,
        {"input_references": {"effective_family_resolution_source": "provided_mapping"}},
    )


def resolve_effective_family_consumption_from_path(path: Path | str) -> dict[str, Any]:
    """Read one effective-family resolution artifact and consume from it."""

    resolution_path = _repo_path(Path(path))
    try:
        resolution = _read_effective_family_resolution(resolution_path)
    except _UnreadableArtifact:
        return _blocked_result(
            resolution=None,
            resolution_path=resolution_path,
            block_code="EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE",
            block_reason=BLOCK_REASONS["EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE"],
            checks=[
                _check(
                    "effective_family_resolution_readable",
                    "readable effective-family resolution artifact",
                    _display(resolution_path),
                    False,
                    "EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE",
                )
            ],
        )
    return _resolve_selected(
        resolution,
        resolution_path,
        {
            "input_references": {
                "selected_effective_family_resolution_artifact_path": _display(
                    resolution_path
                )
            }
        },
    )


def write_effective_family_consumption_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 effective-family consumption result artifact."""

    if not isinstance(result, Mapping):
        raise EffectiveFamilyConsumptionError("Consumption result must be a mapping")
    if output_path is None:
        metadata = _obj(result, "consumption_metadata", "consumption result")
        stem = _safe(
            _str(metadata, "consumption_result_id", "consumption metadata")
        )
        target = _next_json_path(
            _repo_root() / EFFECTIVE_FAMILY_CONSUMPTION_ROOT,
            f"{stem}__effective_family_consumption_result",
        )
    else:
        target = _repo_path(Path(output_path))
        if target.exists():
            raise EffectiveFamilyConsumptionError(
                f"Refusing to overwrite consumption result: {_display(target)}"
            )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_effective_family_consumption_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact inspection summary for one consumption result."""

    metadata = _obj(result, "consumption_metadata", "consumption result")
    selected = _obj(
        result,
        "selected_effective_family_resolution",
        "consumption result",
    )
    effective = _obj(result, "effective_inputs", "consumption result")
    block = _obj(result, "block", "consumption result")
    checks = _list(result, "checks", "consumption result")
    non_claims = _obj(result, "non_claims", "consumption result")
    return {
        "consumption_result_id": _str(
            metadata,
            "consumption_result_id",
            "consumption metadata",
        ),
        "outcome": _str(result, "outcome", "consumption result"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_effective_family_resolution_id": selected.get(
            "effective_family_resolution_id"
        ),
        "effective_authority_artifact_path": effective.get(
            "effective_authority_artifact_path"
        ),
        "effective_family_packet_path": effective.get("effective_family_packet_path"),
        "effective_status_packet_path": effective.get("effective_status_packet_path"),
        "effective_current_governing_packet_path": effective.get(
            "effective_current_governing_packet_path"
        ),
        "effective_source_run_path": effective.get("effective_source_run_path"),
        "effective_ingress_run_path": effective.get("effective_ingress_run_path"),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(1 for check in checks if check.get("passed") is not True),
        "non_claims": {
            key: _bool(non_claims, key, "consumption result.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _resolve_selected(
    resolution: Mapping[str, Any],
    resolution_path: Path | None,
    selection: Mapping[str, Any],
) -> dict[str, Any]:
    non_claims = _resolution_non_claims(resolution)
    outcome = _str(resolution, "outcome", "effective-family resolution")
    if outcome not in SUPPORTED_EFFECTIVE_OUTCOMES:
        return _blocked_result(
            resolution=resolution,
            resolution_path=resolution_path,
            block_code="EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE",
            block_reason=BLOCK_REASONS["EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE"],
            checks=[
                _check(
                    "effective_family_resolution_outcome_supported",
                    sorted(SUPPORTED_EFFECTIVE_OUTCOMES),
                    outcome,
                    False,
                    "EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE",
                )
            ],
            non_claims=non_claims,
        )

    try:
        effective_family = _load_effective_family_from_resolution(resolution)
    except _UnreadableArtifact:
        return _blocked_result(
            resolution=resolution,
            resolution_path=resolution_path,
            block_code="EFFECTIVE_FAMILY_ARTIFACT_UNREADABLE",
            block_reason=BLOCK_REASONS["EFFECTIVE_FAMILY_ARTIFACT_UNREADABLE"],
            checks=[
                _check(
                    "effective_family_artifacts_readable",
                    "effective authority, family, status, and governing artifacts readable",
                    _effective_inputs(resolution),
                    False,
                    "EFFECTIVE_FAMILY_ARTIFACT_UNREADABLE",
                )
            ],
            non_claims=non_claims,
        )

    non_claims = _combined_non_claims(non_claims, effective_family)
    checks = _consumption_checks(
        resolution,
        resolution_path,
        effective_family,
        non_claims,
        selection,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            resolution=resolution,
            resolution_path=resolution_path,
            block_code=failed["block_code"],
            block_reason=BLOCK_REASONS.get(
                failed["block_code"],
                f"Consumption check failed: {failed['check']}",
            ),
            checks=checks,
            non_claims=non_claims,
        )

    return _consumed_result(
        resolution=resolution,
        resolution_path=resolution_path,
        effective_family=effective_family,
        checks=checks,
        non_claims=non_claims,
    )


def _select_default_effective_family_resolution(root: Path) -> dict[str, Any]:
    root_path = _repo_path(root)
    if not root_path.exists():
        return _selection_block(
            "NO_EFFECTIVE_FAMILY_RESOLUTION",
            BLOCK_REASONS["NO_EFFECTIVE_FAMILY_RESOLUTION"],
            root_path,
            0,
            0,
        )
    if not root_path.is_dir():
        raise EffectiveFamilyConsumptionError(
            f"Effective-family resolution root is not a directory: {_display(root_path)}"
        )

    candidates = sorted(path for path in root_path.rglob("*.json") if path.is_file())
    if not candidates:
        return _selection_block(
            "NO_EFFECTIVE_FAMILY_RESOLUTION",
            BLOCK_REASONS["NO_EFFECTIVE_FAMILY_RESOLUTION"],
            root_path,
            0,
            0,
        )

    effective: list[tuple[Path, dict[str, Any]]] = []
    non_effective_count = 0
    for path in candidates:
        try:
            resolution = _read_effective_family_resolution(path)
        except _UnreadableArtifact:
            raise EffectiveFamilyConsumptionError(
                f"Unreadable effective-family resolution found during selection: {_display(path)}"
            )
        if resolution.get("outcome") in SUPPORTED_EFFECTIVE_OUTCOMES:
            effective.append((path, resolution))
        else:
            non_effective_count += 1

    if not effective:
        return _selection_block(
            "EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE",
            BLOCK_REASONS["EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE"],
            root_path,
            len(candidates),
            non_effective_count,
        )

    identities = {
        _effective_resolution_identity(resolution)
        for _, resolution in effective
    }
    if len(identities) > 1:
        return _selection_block(
            "MULTIPLE_EFFECTIVE_FAMILY_RESOLUTIONS_CONFLICT_UNRESOLVED",
            BLOCK_REASONS["MULTIPLE_EFFECTIVE_FAMILY_RESOLUTIONS_CONFLICT_UNRESOLVED"],
            root_path,
            len(candidates),
            non_effective_count,
            [_display(path) for path, _ in effective],
        )

    selected = effective[-1][0]
    return {
        "selected_effective_family_resolution_path": selected,
        "actual": {
            "effective_family_resolution_artifact_count": len(candidates),
            "supported_effective_family_resolution_count": len(effective),
            "non_effective_family_resolution_count": non_effective_count,
            "selected_effective_family_resolution_artifact_path": _display(selected),
        },
        "input_references": {
            "effective_family_resolution_root_path": _display(root_path),
            "supported_effective_family_resolution_artifact_paths": [
                _display(path) for path, _ in effective
            ],
        },
    }


def _selection_block(
    code: str,
    reason: str,
    root: Path,
    artifact_count: int,
    non_effective_count: int,
    effective_paths: list[str] | None = None,
) -> dict[str, Any]:
    return {
        "selected_effective_family_resolution_path": None,
        "actual": {
            "effective_family_resolution_artifact_count": artifact_count,
            "supported_effective_family_resolution_count": len(effective_paths or []),
            "non_effective_family_resolution_count": non_effective_count,
            "reason": reason,
        },
        "input_references": {
            "effective_family_resolution_root_path": _display(root),
            "supported_effective_family_resolution_artifact_paths": effective_paths or [],
        },
        "block": {
            "block_code": code,
            "block_reason": reason,
        },
    }


def _load_effective_family_from_resolution(
    resolution: Mapping[str, Any],
) -> dict[str, Any]:
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    paths = {
        key: _repo_path(Path(_str(effective, key, "effective-family references")))
        for key in PATH_INPUT_KEYS
    }
    authority = _read_json(paths["effective_authority_artifact_path"], "effective authority artifact")
    family = _read_json(paths["effective_family_packet_path"], "effective family packet")
    status = _read_json(paths["effective_status_packet_path"], "effective status packet")
    governing = _read_json(paths["effective_current_governing_packet_path"], "effective current-governing packet")
    return {
        "authority_path": paths["effective_authority_artifact_path"],
        "family_path": paths["effective_family_packet_path"],
        "status_path": paths["effective_status_packet_path"],
        "governing_path": paths["effective_current_governing_packet_path"],
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
        "authority_summary": _authority_summary(authority),
        "family_summary": _family_summary(family),
        "status_summary": _status_summary(status),
        "governing_summary": _governing_summary(governing),
    }


def _consumption_checks(
    resolution: Mapping[str, Any],
    resolution_path: Path | None,
    effective_family: Mapping[str, Any],
    non_claims: Mapping[str, bool],
    selection: Mapping[str, Any],
) -> list[dict[str, Any]]:
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    outcome = _str(resolution, "outcome", "effective-family resolution")
    core_values = _core_values(effective_family)
    source_values = _source_values(effective_family)
    ingress_values = _ingress_values(effective_family)
    refs_match = _effective_refs_match_loaded_paths(resolution, effective_family)
    prior_preserved = _prior_family_readable(resolution)
    stale_fallback = _stale_prior_family_fallback(resolution)
    adopted_distinction_visible = _adopted_distinction_visible(resolution)

    return [
        _check(
            "effective_family_resolution_exists_and_readable",
            "readable effective-family resolution",
            _display(resolution_path) if resolution_path else "provided mapping",
            True,
            "EFFECTIVE_FAMILY_RESOLUTION_UNREADABLE",
        ),
        _check(
            "effective_family_resolution_outcome_supported",
            sorted(SUPPORTED_EFFECTIVE_OUTCOMES),
            outcome,
            outcome in SUPPORTED_EFFECTIVE_OUTCOMES,
            "EFFECTIVE_FAMILY_RESOLUTION_NOT_EFFECTIVE",
        ),
        _check(
            "effective_family_artifacts_readable",
            "effective authority, family, status, and governing artifacts readable",
            _loaded_family_paths(effective_family),
            True,
            "EFFECTIVE_FAMILY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_family_references_match_resolution",
            "loaded artifact paths match effective-family resolution references",
            {
                "resolution_effective_inputs": _json_ready(effective),
                "loaded_paths": _loaded_family_paths(effective_family),
            },
            refs_match,
            "EFFECTIVE_FAMILY_DOES_NOT_CORRESPOND_TO_RESOLUTION",
        ),
        _check(
            "effective_family_canonical_core_matches",
            CANONICAL_CORE_EXECUTION_FILE,
            core_values,
            len(set(core_values.values())) == 1
            and next(iter(core_values.values())) == CANONICAL_CORE_EXECUTION_FILE,
            "CANONICAL_EXECUTION_LINE_MISMATCH",
        ),
        _check(
            "effective_family_current_source_paths_align",
            "same current governing source run across effective artifacts",
            source_values,
            _all_same_non_empty(source_values.values()),
            "EFFECTIVE_FAMILY_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_family_current_ingress_paths_align",
            "same current governing ingress run across effective artifacts that expose ingress",
            ingress_values,
            _all_same_non_empty(ingress_values.values()),
            "EFFECTIVE_FAMILY_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_family_replay_remains_false",
            False,
            non_claims.get("replayed_into_live_host"),
            non_claims.get("replayed_into_live_host") is False,
            "REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_family_merge_remains_false",
            False,
            non_claims.get("merged_into_local_state"),
            non_claims.get("merged_into_local_state") is False,
            "MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_family_continuity_completion_remains_false",
            False,
            non_claims.get("continuity_completed"),
            non_claims.get("continuity_completed") is False,
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_family_standing_upgrade_remains_false",
            False,
            non_claims.get("standing_upgraded"),
            non_claims.get("standing_upgraded") is False,
            "SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "effective_family_all_non_claims_remain_false",
            "all bounded non-claims false",
            non_claims,
            _all_non_claims_false(non_claims),
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "prior_family_remains_preserved",
            "prior family artifact references remain readable",
            _obj(resolution, "prior_current_family", "effective-family resolution"),
            prior_preserved,
            "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT",
        ),
        _check(
            "current_and_adopted_distinction_visible",
            "adopted effective family preserves selected adoption and prior-family distinction where applicable",
            {
                "outcome": outcome,
                "selected_adoption_result": resolution.get("selected_adoption_result"),
                "stale_prior_family_fallback": stale_fallback,
            },
            adopted_distinction_visible,
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "consumption_uses_explicit_effective_family_resolution",
            "consumer uses effective-family resolution references rather than latest artifact inference",
            selection.get("input_references"),
            True,
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            "adopted successor effective family must not consume prior-family artifacts as active inputs",
            {"stale_prior_family_fallback": stale_fallback},
            not stale_fallback,
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
    ]


def _consumed_result(
    *,
    resolution: Mapping[str, Any],
    resolution_path: Path | None,
    effective_family: Mapping[str, Any],
    checks: list[dict[str, Any]],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return _result(
        resolution=resolution,
        resolution_path=resolution_path,
        outcome=OUTCOME_CONSUMED,
        block_code=None,
        block_reason=None,
        checks=checks,
        consumed_refs=_effective_inputs(resolution),
        summary=_consumption_summary(resolution, effective_family, True),
        non_claims=non_claims,
    )


def _blocked_result(
    *,
    resolution: Mapping[str, Any] | None,
    resolution_path: Path | None,
    block_code: str,
    block_reason: str,
    checks: list[dict[str, Any]],
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        resolution=resolution,
        resolution_path=resolution_path,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason,
        checks=checks,
        consumed_refs=_null_effective_inputs(),
        summary=_blocked_summary(resolution),
        non_claims=non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _result(
    *,
    resolution: Mapping[str, Any] | None,
    resolution_path: Path | None,
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    checks: list[dict[str, Any]],
    consumed_refs: Mapping[str, Any],
    summary: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    result_id = _consumption_result_id(resolution, outcome)
    return {
        "consumption_metadata": {
            "consumption_result_id": result_id,
            "consumption_result_type": CONSUMPTION_RESULT_TYPE,
            "consumption_result_version": CONSUMPTION_RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "selected_effective_family_resolution": _selected_resolution_summary(
            resolution,
            resolution_path,
        ),
        "effective_inputs": _effective_inputs(resolution),
        "checks": checks,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "consumed_family_references": dict(consumed_refs),
        "consumption_summary": dict(summary),
        "non_claims": dict(non_claims),
    }


def _selected_resolution_summary(
    resolution: Mapping[str, Any] | None,
    resolution_path: Path | None,
) -> dict[str, Any]:
    if resolution is None:
        return {
            "effective_family_resolution_artifact_path": (
                _display(resolution_path) if resolution_path is not None else None
            ),
            "effective_family_resolution_id": None,
            "effective_family_resolution_type": None,
            "effective_family_resolution_version": None,
            "outcome": None,
            "selected_adoption_result_id": None,
        }
    metadata = _obj(resolution, "resolution_metadata", "effective-family resolution")
    selected_adoption = resolution.get("selected_adoption_result")
    selected_adoption_id = (
        selected_adoption.get("adoption_result_id")
        if isinstance(selected_adoption, Mapping)
        else None
    )
    return {
        "effective_family_resolution_artifact_path": (
            _display(resolution_path) if resolution_path is not None else None
        ),
        "effective_family_resolution_id": metadata.get("effective_family_resolution_id"),
        "effective_family_resolution_type": metadata.get("effective_family_resolution_type"),
        "effective_family_resolution_version": metadata.get("effective_family_resolution_version"),
        "outcome": resolution.get("outcome"),
        "selected_adoption_result_id": selected_adoption_id,
    }


def _effective_inputs(resolution: Mapping[str, Any] | None) -> dict[str, Any]:
    if resolution is None:
        return _null_effective_inputs()
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    result: dict[str, Any] = {}
    for key in EFFECTIVE_INPUT_KEYS:
        value = effective.get(key)
        result[key] = value if isinstance(value, str) else None
    return result


def _null_effective_inputs() -> dict[str, None]:
    return {key: None for key in EFFECTIVE_INPUT_KEYS}


def _consumption_summary(
    resolution: Mapping[str, Any],
    effective_family: Mapping[str, Any],
    prior_family_preserved: bool,
) -> dict[str, Any]:
    status_summary = _obj(effective_family, "status_summary", "effective family")
    governing_summary = _obj(effective_family, "governing_summary", "effective family")
    basis = _obj(resolution, "resolution_basis", "effective-family resolution")
    return {
        "effective_current_governing_source_run_path": governing_summary.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": governing_summary.get(
            "current_governing_ingress_run_path"
        ),
        "preserved_run_count": status_summary.get("preserved_run_count"),
        "consumed_current_family_basis": basis.get("basis"),
        "prior_family_remained_preserved": prior_family_preserved,
    }


def _blocked_summary(resolution: Mapping[str, Any] | None) -> dict[str, Any]:
    if resolution is None:
        return {
            "effective_current_governing_source_run_path": None,
            "effective_current_governing_ingress_run_path": None,
            "preserved_run_count": None,
            "consumed_current_family_basis": None,
            "prior_family_remained_preserved": None,
        }
    effective = _effective_inputs(resolution)
    basis = _obj(resolution, "resolution_basis", "effective-family resolution")
    return {
        "effective_current_governing_source_run_path": effective.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": effective.get(
            "effective_ingress_run_path"
        ),
        "preserved_run_count": None,
        "consumed_current_family_basis": basis.get("basis"),
        "prior_family_remained_preserved": _prior_family_readable(resolution),
    }


def _validate_effective_family_resolution(payload: dict[str, Any]) -> dict[str, Any]:
    for key in (
        "resolution_metadata",
        "canonical_execution_line",
        "prior_current_family",
        "effective_family",
        "resolution_basis",
        "checks",
        "outcome",
        "non_effective_preserved_families",
        "non_claims",
    ):
        if key == "checks":
            _list(payload, key, "effective-family resolution")
        elif key == "outcome":
            _str(payload, key, "effective-family resolution")
        else:
            _obj(payload, key, "effective-family resolution")

    metadata = _obj(payload, "resolution_metadata", "effective-family resolution")
    _str(metadata, "effective_family_resolution_id", "effective-family metadata")
    effective = _obj(payload, "effective_family", "effective-family resolution")
    for key in PATH_INPUT_KEYS:
        _str(effective, key, "effective-family resolution.effective_family")
    _resolution_non_claims(payload)
    try:
        build_effective_family_summary(payload)
    except Exception as exc:
        raise EffectiveFamilyConsumptionError(
            "Effective-family resolution artifact is malformed"
        ) from exc
    return payload


def _read_effective_family_resolution(path: Path) -> dict[str, Any]:
    return _validate_effective_family_resolution(
        _read_json(path, "effective-family resolution")
    )


def _read_json(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_path(path)
    try:
        value = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise _UnreadableArtifact(f"{label} file does not exist: {_display(file_path)}") from exc
    except OSError as exc:
        raise _UnreadableArtifact(f"Could not read {label}: {_display(file_path)}") from exc
    except json.JSONDecodeError as exc:
        raise EffectiveFamilyConsumptionError(
            f"{label.title()} is not valid JSON: {_display(file_path)}"
        ) from exc
    if not isinstance(value, dict):
        raise EffectiveFamilyConsumptionError(
            f"{label.title()} JSON must be an object: {_display(file_path)}"
        )
    return value


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except Exception as exc:
        raise EffectiveFamilyConsumptionError("Effective authority artifact is malformed") from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except Exception as exc:
        raise EffectiveFamilyConsumptionError("Effective family packet is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except Exception as exc:
        raise EffectiveFamilyConsumptionError("Effective status packet is malformed") from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except Exception as exc:
        raise EffectiveFamilyConsumptionError(
            "Effective current-governing packet is malformed"
        ) from exc


def _resolution_non_claims(resolution: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    _merge_non_claims(
        non_claims,
        _obj(resolution, "non_claims", "effective-family resolution"),
        "effective-family resolution",
    )
    return non_claims


def _combined_non_claims(
    base_non_claims: Mapping[str, bool],
    effective_family: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    _merge_non_claims(non_claims, base_non_claims, "effective-family resolution")
    for stack_key in ("authority", "family", "status", "governing"):
        artifact = _obj(effective_family, stack_key, "effective family")
        _merge_non_claims(
            non_claims,
            _obj(artifact, "non_claims", f"effective {stack_key} artifact"),
            f"effective {stack_key} artifact",
        )
    return non_claims


def _merge_non_claims(
    target: dict[str, bool],
    incoming: Mapping[str, Any],
    context: str,
) -> None:
    for key in NON_CLAIM_DEFAULTS:
        if key not in incoming:
            continue
        value = incoming.get(key)
        if not isinstance(value, bool):
            raise EffectiveFamilyConsumptionError(
                f"{context}.non_claims.{key} must be a boolean"
            )
        target[key] = value


def _all_non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in NON_CLAIM_DEFAULTS)


def _core_values(effective_family: Mapping[str, Any]) -> dict[str, str]:
    return {
        "authority": _core(_obj(effective_family, "authority", "effective family"), "authority"),
        "family": _core(_obj(effective_family, "family", "effective family"), "family"),
        "status": _core(_obj(effective_family, "status", "effective family"), "status"),
        "governing": _core(_obj(effective_family, "governing", "effective family"), "governing"),
    }


def _source_values(effective_family: Mapping[str, Any]) -> dict[str, Any]:
    authority = _obj(effective_family, "authority_summary", "effective family")
    family = _obj(effective_family, "family_summary", "effective family")
    status = _obj(effective_family, "status_summary", "effective family")
    governing = _obj(effective_family, "governing_summary", "effective family")
    return {
        "authority_source": authority.get("selected_source_run_directory_path"),
        "family_source": family.get("current_authority_source_run_path"),
        "status_source": status.get("selected_current_authority_source_run_path"),
        "governing_source": governing.get("current_governing_source_run_path"),
    }


def _ingress_values(effective_family: Mapping[str, Any]) -> dict[str, Any]:
    authority = _obj(effective_family, "authority_summary", "effective family")
    family = _obj(effective_family, "family_summary", "effective family")
    governing = _obj(effective_family, "governing_summary", "effective family")
    return {
        "authority_ingress": authority.get("selected_ingress_run_directory_path"),
        "family_ingress": family.get("current_authority_ingress_run_path"),
        "governing_ingress": governing.get("current_governing_ingress_run_path"),
    }


def _effective_refs_match_loaded_paths(
    resolution: Mapping[str, Any],
    effective_family: Mapping[str, Any],
) -> bool:
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    return all(
        _same(_path_value(effective_family, stack_key), effective.get(result_key))
        for stack_key, result_key in (
            ("authority_path", "effective_authority_artifact_path"),
            ("family_path", "effective_family_packet_path"),
            ("status_path", "effective_status_packet_path"),
            ("governing_path", "effective_current_governing_packet_path"),
        )
    )


def _loaded_family_paths(effective_family: Mapping[str, Any]) -> dict[str, str]:
    return {
        "effective_authority_artifact_path": _display(_path_value(effective_family, "authority_path")),
        "effective_family_packet_path": _display(_path_value(effective_family, "family_path")),
        "effective_status_packet_path": _display(_path_value(effective_family, "status_path")),
        "effective_current_governing_packet_path": _display(_path_value(effective_family, "governing_path")),
    }


def _prior_family_readable(resolution: Mapping[str, Any]) -> bool:
    prior = _obj(resolution, "prior_current_family", "effective-family resolution")
    keys = (
        "prior_authority_artifact_path",
        "prior_family_packet_path",
        "prior_status_packet_path",
        "prior_current_governing_packet_path",
    )
    return all(
        isinstance(prior.get(key), str)
        and bool(prior.get(key))
        and _resolve_path(str(prior.get(key))).is_file()
        for key in keys
    )


def _adopted_distinction_visible(resolution: Mapping[str, Any]) -> bool:
    outcome = resolution.get("outcome")
    if outcome != OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE:
        return True
    return (
        isinstance(resolution.get("selected_adoption_result"), Mapping)
        and _prior_family_readable(resolution)
        and not _stale_prior_family_fallback(resolution)
    )


def _stale_prior_family_fallback(resolution: Mapping[str, Any]) -> bool:
    if resolution.get("outcome") != OUTCOME_ADOPTED_SUCCESSOR_FAMILY_EFFECTIVE:
        return False
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    prior = _obj(resolution, "prior_current_family", "effective-family resolution")
    pairs = (
        ("effective_authority_artifact_path", "prior_authority_artifact_path"),
        ("effective_family_packet_path", "prior_family_packet_path"),
        ("effective_status_packet_path", "prior_status_packet_path"),
        ("effective_current_governing_packet_path", "prior_current_governing_packet_path"),
    )
    return all(_same(effective.get(effective_key), prior.get(prior_key)) for effective_key, prior_key in pairs)


def _effective_resolution_identity(resolution: Mapping[str, Any]) -> tuple[Any, ...]:
    selected = resolution.get("selected_adoption_result")
    selected_id = (
        selected.get("adoption_result_id") if isinstance(selected, Mapping) else None
    )
    effective = _obj(resolution, "effective_family", "effective-family resolution")
    return (
        resolution.get("outcome"),
        selected_id,
        effective.get("effective_authority_artifact_path"),
        effective.get("effective_family_packet_path"),
        effective.get("effective_status_packet_path"),
        effective.get("effective_current_governing_packet_path"),
    )


def _consumption_result_id(
    resolution: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    if resolution is None:
        base = "no_effective_family_resolution"
    else:
        metadata = _obj(resolution, "resolution_metadata", "effective-family resolution")
        base = _str(metadata, "effective_family_resolution_id", "effective-family metadata")
    suffix = "consumed" if outcome == OUTCOME_CONSUMED else "blocked"
    return f"{base}__{suffix}_effective_family_consumption"


def _first_failed(checks: list[Mapping[str, Any]]) -> dict[str, str] | None:
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code")
        name = check.get("check")
        return {
            "check": str(name) if name else "unknown_check",
            "block_code": str(code) if code else "EFFECTIVE_FAMILY_NOT_INTERNALLY_COHERENT",
        }
    return None


def _check(
    name: str,
    required: Any,
    actual: Any,
    passed: bool,
    block_code: str,
) -> dict[str, Any]:
    return {
        "check": name,
        "required": _json_ready(required),
        "actual": _json_ready(actual),
        "passed": bool(passed),
        "block_code": block_code,
    }


def _all_same_non_empty(values: Any) -> bool:
    present = list(values)
    if not present or any(not isinstance(value, str) or not value for value in present):
        return False
    first = present[0]
    return all(_same(first, value) for value in present[1:])


def _path_value(mapping: Mapping[str, Any], key: str) -> Path:
    value = mapping.get(key)
    if not isinstance(value, Path):
        raise EffectiveFamilyConsumptionError(f"{key} must be a Path")
    return value


def _core(packet: Mapping[str, Any], label: str) -> str:
    return _str(
        _obj(packet, "canonical_execution_line", label),
        "core_execution_file",
        f"{label}.canonical_execution_line",
    )


def _same(left: Any, right: Any) -> bool:
    if not isinstance(left, (str, Path)) or not isinstance(right, (str, Path)):
        return False
    return _resolve_path(str(left)) == _resolve_path(str(right))


def _resolve_path(path_text: str) -> Path:
    path = Path(path_text)
    return path.resolve() if path.is_absolute() else (_repo_root() / path).resolve()


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path) -> Path:
    return path.resolve() if path.is_absolute() else (_repo_root() / path).resolve()


def _display(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(_repo_root()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _json_text(payload: Mapping[str, Any]) -> str:
    return json.dumps(_json_ready(payload), indent=2, sort_keys=True, allow_nan=False) + "\n"


def _json_ready(value: Any) -> Any:
    if value is None or isinstance(value, (str, bool, int, float)):
        return value
    if isinstance(value, Path):
        return _display(value)
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple, set)):
        return [_json_ready(item) for item in value]
    return str(value)


def _next_json_path(root: Path, stem: str) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    first = root / f"{stem}.json"
    if not first.exists():
        return first
    index = 2
    while True:
        candidate = root / f"{stem}__{index}.json"
        if not candidate.exists():
            return candidate
        index += 1


def _safe(value: str) -> str:
    return "".join(char if char.isalnum() or char in "._-" else "_" for char in value)


def _obj(mapping: Mapping[str, Any], key: str, context: str) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise EffectiveFamilyConsumptionError(f"{context}.{key} must be an object")
    return value


def _list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise EffectiveFamilyConsumptionError(f"{context}.{key} must be a list")
    return value


def _str(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise EffectiveFamilyConsumptionError(f"{context}.{key} must be a non-empty string")
    return value


def _bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise EffectiveFamilyConsumptionError(f"{context}.{key} must be a boolean")
    return value
