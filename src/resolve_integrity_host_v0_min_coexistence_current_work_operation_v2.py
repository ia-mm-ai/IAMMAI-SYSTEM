"""Resolve one bounded current-work operation from current-work-input.

This module reads one current-work-input resolution and the effective authority,
run-family, preserved-run status, and current-governing artifacts named by that
resolution. It emits one explicit current-work-operation result stating whether
one bounded downstream work step completed or blocked.

This v2 successor preserves the v1 result shape, checks, and anti-collapse
posture while repairing one concrete runtime issue: default artifact writing no
longer uses the full work-result lineage id as a filesystem path component. Full
ids remain inside the JSON payload; default filenames stay short and bounded.

The resolver is additive engineering. It does not replay source actions into a
live host, merge preserved runs, mutate prior artifacts, complete continuity,
upgrade standing, define persistence or registry law, or treat a completed work
operation as final governance.
"""

from __future__ import annotations

import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from resolve_integrity_host_v0_min_coexistence_current_work_input import (
    CURRENT_WORK_INPUT_ROOT,
    NON_CLAIM_DEFAULTS as CURRENT_WORK_INPUT_NON_CLAIMS,
    OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
    build_current_governing_summary,
    build_current_work_input_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


CURRENT_WORK_OPERATION_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_work_operation"
)

WORK_RESULT_TYPE = "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_CURRENT_WORK_OPERATION_RESULT"
WORK_RESULT_VERSION = "0.2.0"

DEFAULT_WORK_OPERATION_RESULT_STEM = "current_work_operation_result"

OUTCOME_COMPLETED = "COMPLETED"
OUTCOME_BLOCKED = "BLOCKED"

CANONICAL_CORE_EXECUTION_FILE = "src/integrity_host_v0_min_coexistence_v2.py"

NON_CLAIM_DEFAULTS = {
    **CURRENT_WORK_INPUT_NON_CLAIMS,
    "final_current_work_operation_completed": False,
}

WORK_INPUT_KEYS = (
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
    "NO_CURRENT_WORK_INPUT_RESOLUTION": "No resolved current-work-input resolution is available.",
    "CURRENT_WORK_INPUT_UNREADABLE": "The selected current-work-input resolution is unreadable.",
    "CURRENT_WORK_INPUT_NOT_RESOLVED": "The selected current-work-input result is not resolved.",
    "EFFECTIVE_WORK_INPUT_ARTIFACT_UNREADABLE": "One or more effective work-input artifacts named by the current-work-input result are unreadable.",
    "CANONICAL_EXECUTION_LINE_MISMATCH": "The effective work-input artifacts do not preserve the current canonical core execution line.",
    "EFFECTIVE_WORK_INPUT_NOT_INTERNALLY_COHERENT": "The effective work-input artifacts do not name one coherent current governing run.",
    "EFFECTIVE_WORK_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": "The effective work-input artifacts do not correspond to the selected current-work-input result.",
    "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT": "Prior-family preservation is not evident in the selected current-work-input result.",
    "REPLAY_SHORTCUT_REFUSED": "Current-work-operation cannot proceed with replay marked true.",
    "MERGE_SHORTCUT_REFUSED": "Current-work-operation cannot proceed with merge marked true.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Current-work-operation cannot claim continuity completion.",
    "SILENT_STANDING_UPGRADE_REFUSED": "Current-work-operation cannot silently upgrade standing.",
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": "Current-work-operation cannot fall back to stale prior-family artifacts.",
    "MULTIPLE_CURRENT_WORK_INPUT_RESULTS_CONFLICT_UNRESOLVED": "Multiple resolved current-work-input results conflict without a bounded selection surface.",
}


class CurrentWorkOperationError(RuntimeError):
    """Raised when bounded current-work-operation resolution cannot proceed."""


class _UnreadableArtifact(RuntimeError):
    """Private marker for ordinary readable-artifact block cases."""


def discover_latest_resolved_current_work_input_result(root: Path) -> Path:
    """Return the lexically latest resolved current-work-input result."""

    selection = _select_default_current_work_input(root)
    selected = selection.get("selected_current_work_input_path")
    if not isinstance(selected, Path):
        raise CurrentWorkOperationError("No resolved current-work-input result found")
    return selected


def discover_latest_current_work_input_resolution(root: Path) -> Path:
    """Compatibility alias for the bounded current-work-input discovery helper."""

    return discover_latest_resolved_current_work_input_result(root)


def resolve_current_work_operation(
    current_work_input: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded downstream current-work operation."""

    if current_work_input is None:
        selection = _select_default_current_work_input(CURRENT_WORK_INPUT_ROOT)
        block = selection.get("block")
        if isinstance(block, Mapping):
            return _blocked_result(
                work_input=None,
                work_input_path=None,
                block_code=_str(block, "block_code", "selection block"),
                block_reason=_str(block, "block_reason", "selection block"),
                checks=[
                    _check(
                        "resolved_current_work_input_selected",
                        "one resolved current-work-input result",
                        selection.get("actual"),
                        False,
                        _str(block, "block_code", "selection block"),
                    )
                ],
            )

        selected_path = selection.get("selected_current_work_input_path")
        if not isinstance(selected_path, Path):
            raise CurrentWorkOperationError(
                "Selected current-work-input path is malformed"
            )
        try:
            work_input = _read_current_work_input_result(selected_path)
        except _UnreadableArtifact:
            return _blocked_result(
                work_input=None,
                work_input_path=selected_path,
                block_code="CURRENT_WORK_INPUT_UNREADABLE",
                block_reason=BLOCK_REASONS["CURRENT_WORK_INPUT_UNREADABLE"],
                checks=[
                    _check(
                        "current_work_input_readable",
                        "readable current-work-input result",
                        _display(selected_path),
                        False,
                        "CURRENT_WORK_INPUT_UNREADABLE",
                    )
                ],
            )
        return _resolve_selected(work_input, selected_path, selection)

    if not isinstance(current_work_input, Mapping):
        raise CurrentWorkOperationError(
            "Current-work-input result must be a mapping or None"
        )
    work_input = _validate_current_work_input_result(dict(current_work_input))
    return _resolve_selected(
        work_input,
        None,
        {"input_references": {"current_work_input_source": "provided_mapping"}},
    )


def resolve_current_work_operation_from_path(path: Path | str) -> dict[str, Any]:
    """Read one current-work-input result and resolve one bounded work operation."""

    work_input_path = _repo_path(Path(path))
    try:
        work_input = _read_current_work_input_result(work_input_path)
    except _UnreadableArtifact:
        return _blocked_result(
            work_input=None,
            work_input_path=work_input_path,
            block_code="CURRENT_WORK_INPUT_UNREADABLE",
            block_reason=BLOCK_REASONS["CURRENT_WORK_INPUT_UNREADABLE"],
            checks=[
                _check(
                    "current_work_input_readable",
                    "readable current-work-input result",
                    _display(work_input_path),
                    False,
                    "CURRENT_WORK_INPUT_UNREADABLE",
                )
            ],
        )
    return _resolve_selected(
        work_input,
        work_input_path,
        {
            "input_references": {
                "selected_current_work_input_artifact_path": _display(work_input_path)
            }
        },
    )


def write_current_work_operation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive UTF-8 current-work-operation result artifact."""

    if not isinstance(result, Mapping):
        raise CurrentWorkOperationError(
            "Current-work-operation result must be a mapping"
        )
    if output_path is None:
        _obj(result, "work_operation_metadata", "work-operation result")
        target = _next_default_work_operation_path(
            _repo_root() / CURRENT_WORK_OPERATION_ROOT
        )
    else:
        target = _repo_path(Path(output_path))
        if target.exists():
            raise CurrentWorkOperationError(
                f"Refusing to overwrite current-work-operation result: {_display(target)}"
            )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(_json_text(result), encoding="utf-8")
    return target


def build_current_work_operation_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one current-work-operation result."""

    metadata = _obj(result, "work_operation_metadata", "work-operation result")
    selected = _obj(result, "selected_current_work_input", "work-operation result")
    inputs = _obj(result, "effective_inputs", "work-operation result")
    block = _obj(result, "block", "work-operation result")
    checks = _list(result, "checks", "work-operation result")
    non_claims = _obj(result, "non_claims", "work-operation result")
    return {
        "work_result_id": _str(metadata, "work_result_id", "work-operation metadata"),
        "outcome": _str(result, "outcome", "work-operation result"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_current_work_input_id": selected.get(
            "current_work_input_resolution_id"
        ),
        "effective_authority_artifact_path": inputs.get(
            "effective_authority_artifact_path"
        ),
        "effective_family_packet_path": inputs.get("effective_family_packet_path"),
        "effective_status_packet_path": inputs.get("effective_status_packet_path"),
        "effective_current_governing_packet_path": inputs.get(
            "effective_current_governing_packet_path"
        ),
        "effective_source_run_path": inputs.get("effective_source_run_path"),
        "effective_ingress_run_path": inputs.get("effective_ingress_run_path"),
        "passed_check_count": sum(1 for check in checks if check.get("passed") is True),
        "failed_check_count": sum(
            1 for check in checks if check.get("passed") is not True
        ),
        "non_claims": {
            key: _bool(non_claims, key, "work-operation result.non_claims")
            for key in NON_CLAIM_DEFAULTS
        },
    }


def _resolve_selected(
    work_input: Mapping[str, Any],
    work_input_path: Path | None,
    selection: Mapping[str, Any],
) -> dict[str, Any]:
    non_claims = _current_work_input_non_claims(work_input)
    outcome = _str(work_input, "outcome", "current-work-input result")
    if outcome != OUTCOME_CURRENT_WORK_INPUT_RESOLVED:
        return _blocked_result(
            work_input=work_input,
            work_input_path=work_input_path,
            block_code="CURRENT_WORK_INPUT_NOT_RESOLVED",
            block_reason=BLOCK_REASONS["CURRENT_WORK_INPUT_NOT_RESOLVED"],
            checks=[
                _check(
                    "current_work_input_outcome_resolved",
                    OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
                    outcome,
                    False,
                    "CURRENT_WORK_INPUT_NOT_RESOLVED",
                )
            ],
            non_claims=non_claims,
        )

    try:
        effective_family = _load_effective_family_from_result(work_input)
    except _UnreadableArtifact:
        return _blocked_result(
            work_input=work_input,
            work_input_path=work_input_path,
            block_code="EFFECTIVE_WORK_INPUT_ARTIFACT_UNREADABLE",
            block_reason=BLOCK_REASONS["EFFECTIVE_WORK_INPUT_ARTIFACT_UNREADABLE"],
            checks=[
                _check(
                    "effective_work_input_artifacts_readable",
                    "effective authority, family, status, and governing artifacts readable",
                    _resolved_work_input_references(work_input),
                    False,
                    "EFFECTIVE_WORK_INPUT_ARTIFACT_UNREADABLE",
                )
            ],
            non_claims=non_claims,
        )

    non_claims = _combined_non_claims(non_claims, effective_family)
    checks = _work_checks(
        work_input,
        work_input_path,
        effective_family,
        non_claims,
        selection,
    )
    failed = _first_failed(checks)
    if failed is not None:
        return _blocked_result(
            work_input=work_input,
            work_input_path=work_input_path,
            block_code=failed["block_code"],
            block_reason=BLOCK_REASONS.get(
                failed["block_code"],
                f"Current-work-operation check failed: {failed['check']}",
            ),
            checks=checks,
            non_claims=non_claims,
        )

    return _completed_result(
        work_input=work_input,
        work_input_path=work_input_path,
        effective_family=effective_family,
        checks=checks,
        non_claims=non_claims,
    )


def _select_default_current_work_input(root: Path) -> dict[str, Any]:
    root_path = _repo_path(root)
    if not root_path.exists():
        return _selection_block(
            "NO_CURRENT_WORK_INPUT_RESOLUTION",
            BLOCK_REASONS["NO_CURRENT_WORK_INPUT_RESOLUTION"],
            root_path,
            0,
            0,
        )
    if not root_path.is_dir():
        raise CurrentWorkOperationError(
            f"Current-work-input root is not a directory: {_display(root_path)}"
        )

    candidates = sorted(path for path in root_path.rglob("*.json") if path.is_file())
    if not candidates:
        return _selection_block(
            "NO_CURRENT_WORK_INPUT_RESOLUTION",
            BLOCK_REASONS["NO_CURRENT_WORK_INPUT_RESOLUTION"],
            root_path,
            0,
            0,
        )

    resolved: list[tuple[Path, dict[str, Any]]] = []
    blocked_count = 0
    ignored_count = 0
    for path in candidates:
        try:
            raw = _read_json(path, "current-work-input result")
        except _UnreadableArtifact:
            raise CurrentWorkOperationError(
                f"Unreadable current-work-input result found during selection: {_display(path)}"
            )
        if not _looks_like_current_work_input_result(raw):
            ignored_count += 1
            continue
        result = _validate_current_work_input_result(raw)
        if result.get("outcome") == OUTCOME_CURRENT_WORK_INPUT_RESOLVED:
            resolved.append((path, result))
        else:
            blocked_count += 1

    if not resolved:
        return _selection_block(
            "NO_CURRENT_WORK_INPUT_RESOLUTION",
            BLOCK_REASONS["NO_CURRENT_WORK_INPUT_RESOLUTION"],
            root_path,
            len(candidates),
            blocked_count,
            ignored_count=ignored_count,
        )

    identities = {_current_work_input_identity(result) for _, result in resolved}
    if len(identities) > 1:
        return _selection_block(
            "MULTIPLE_CURRENT_WORK_INPUT_RESULTS_CONFLICT_UNRESOLVED",
            BLOCK_REASONS["MULTIPLE_CURRENT_WORK_INPUT_RESULTS_CONFLICT_UNRESOLVED"],
            root_path,
            len(candidates),
            blocked_count,
            [_display(path) for path, _ in resolved],
            ignored_count=ignored_count,
        )

    selected = resolved[-1][0]
    return {
        "selected_current_work_input_path": selected,
        "actual": {
            "current_work_input_artifact_count": len(candidates),
            "resolved_current_work_input_count": len(resolved),
            "blocked_current_work_input_count": blocked_count,
            "ignored_json_artifact_count": ignored_count,
            "selected_current_work_input_artifact_path": _display(selected),
        },
        "input_references": {
            "current_work_input_root_path": _display(root_path),
            "resolved_current_work_input_artifact_paths": [
                _display(path) for path, _ in resolved
            ],
        },
    }


def _selection_block(
    code: str,
    reason: str,
    root: Path,
    artifact_count: int,
    blocked_count: int,
    resolved_paths: list[str] | None = None,
    ignored_count: int = 0,
) -> dict[str, Any]:
    return {
        "selected_current_work_input_path": None,
        "actual": {
            "current_work_input_artifact_count": artifact_count,
            "resolved_current_work_input_count": len(resolved_paths or []),
            "blocked_current_work_input_count": blocked_count,
            "ignored_json_artifact_count": ignored_count,
            "reason": reason,
        },
        "input_references": {
            "current_work_input_root_path": _display(root),
            "resolved_current_work_input_artifact_paths": resolved_paths or [],
        },
        "block": {
            "block_code": code,
            "block_reason": reason,
        },
    }


def _load_effective_family_from_result(
    work_input: Mapping[str, Any],
) -> dict[str, Any]:
    refs = _obj(
        work_input,
        "resolved_work_input_references",
        "current-work-input result",
    )
    paths = {
        key: _repo_path(Path(_str(refs, key, "resolved work-input references")))
        for key in PATH_INPUT_KEYS
    }
    authority = _read_json(
        paths["effective_authority_artifact_path"],
        "effective authority artifact",
    )
    family = _read_json(paths["effective_family_packet_path"], "effective family packet")
    status = _read_json(paths["effective_status_packet_path"], "effective status packet")
    governing = _read_json(
        paths["effective_current_governing_packet_path"],
        "effective current-governing packet",
    )
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


def _work_checks(
    work_input: Mapping[str, Any],
    work_input_path: Path | None,
    effective_family: Mapping[str, Any],
    non_claims: Mapping[str, bool],
    selection: Mapping[str, Any],
) -> list[dict[str, Any]]:
    outcome = _str(work_input, "outcome", "current-work-input result")
    core_values = _core_values(effective_family)
    source_values = _source_values(effective_family)
    ingress_values = _ingress_values(effective_family)
    refs_match = _resolved_refs_match_loaded_paths(work_input, effective_family)
    refs_match_effective_inputs = _resolved_refs_match_effective_inputs(work_input)
    prior_preserved = _prior_family_preserved(work_input)
    stale_fallback = _stale_prior_family_fallback(work_input)

    return [
        _check(
            "current_work_input_result_exists_and_readable",
            "readable resolved current-work-input result",
            _display(work_input_path) if work_input_path else "provided mapping",
            True,
            "CURRENT_WORK_INPUT_UNREADABLE",
        ),
        _check(
            "current_work_input_outcome_resolved",
            OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
            outcome,
            outcome == OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
            "CURRENT_WORK_INPUT_NOT_RESOLVED",
        ),
        _check(
            "effective_work_input_artifacts_readable",
            "effective authority, family, status, and governing artifacts readable",
            _loaded_family_paths(effective_family),
            True,
            "EFFECTIVE_WORK_INPUT_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_work_input_references_match_result",
            "loaded artifact paths match resolved references and effective inputs",
            {
                "resolved_work_input_references": _resolved_work_input_references(
                    work_input
                ),
                "effective_inputs": _effective_inputs(work_input),
                "loaded_paths": _loaded_family_paths(effective_family),
            },
            refs_match and refs_match_effective_inputs,
            "EFFECTIVE_WORK_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
        ),
        _check(
            "effective_work_input_canonical_core_matches",
            CANONICAL_CORE_EXECUTION_FILE,
            core_values,
            len(set(core_values.values())) == 1
            and next(iter(core_values.values())) == CANONICAL_CORE_EXECUTION_FILE,
            "CANONICAL_EXECUTION_LINE_MISMATCH",
        ),
        _check(
            "effective_work_input_current_source_paths_align",
            "same current governing source run across effective artifacts",
            source_values,
            _all_same_non_empty(source_values.values()),
            "EFFECTIVE_WORK_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_work_input_current_ingress_paths_align",
            "same current governing ingress run across effective artifacts that expose ingress",
            ingress_values,
            _all_same_non_empty(ingress_values.values()),
            "EFFECTIVE_WORK_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_work_input_replay_remains_false",
            False,
            non_claims.get("replayed_into_live_host"),
            non_claims.get("replayed_into_live_host") is False,
            "REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_work_input_merge_remains_false",
            False,
            non_claims.get("merged_into_local_state"),
            non_claims.get("merged_into_local_state") is False,
            "MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_work_input_continuity_completion_remains_false",
            False,
            non_claims.get("continuity_completed"),
            non_claims.get("continuity_completed") is False,
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "effective_work_input_standing_upgrade_remains_false",
            False,
            non_claims.get("standing_upgraded"),
            non_claims.get("standing_upgraded") is False,
            "SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "effective_work_input_all_non_claims_remain_false",
            "all bounded non-claims false",
            non_claims,
            _all_non_claims_false(non_claims),
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "prior_family_remains_preserved_after_work_input_resolution",
            "current-work-input result preserves prior-family preservation where exposed",
            _obj(work_input, "work_input_summary", "current-work-input result").get(
                "prior_family_remained_preserved"
            ),
            prior_preserved,
            "PRIOR_FAMILY_PRESERVATION_NOT_EVIDENT",
        ),
        _check(
            "current_work_operation_uses_explicit_current_work_input",
            "resolver uses current-work-input references instead of latest artifact inference",
            selection.get("input_references"),
            True,
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            "work inputs must match resolved current-work-input references",
            {"stale_prior_family_fallback": stale_fallback},
            not stale_fallback,
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
    ]


def _completed_result(
    *,
    work_input: Mapping[str, Any],
    work_input_path: Path | None,
    effective_family: Mapping[str, Any],
    checks: list[dict[str, Any]],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    return _result(
        work_input=work_input,
        work_input_path=work_input_path,
        outcome=OUTCOME_COMPLETED,
        block_code=None,
        block_reason=None,
        checks=checks,
        work_output=_work_output(work_input, effective_family),
        summary=_work_summary(work_input, effective_family),
        non_claims=non_claims,
    )


def _blocked_result(
    *,
    work_input: Mapping[str, Any] | None,
    work_input_path: Path | None,
    block_code: str,
    block_reason: str,
    checks: list[dict[str, Any]],
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    return _result(
        work_input=work_input,
        work_input_path=work_input_path,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason,
        checks=checks,
        work_output=None,
        summary=_blocked_summary(work_input),
        non_claims=non_claims or dict(NON_CLAIM_DEFAULTS),
    )


def _result(
    *,
    work_input: Mapping[str, Any] | None,
    work_input_path: Path | None,
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    checks: list[dict[str, Any]],
    work_output: Mapping[str, Any] | None,
    summary: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, Any]:
    result_id = _work_result_id(work_input, outcome)
    return {
        "work_operation_metadata": {
            "work_result_id": result_id,
            "work_result_type": WORK_RESULT_TYPE,
            "work_result_version": WORK_RESULT_VERSION,
            "generated_at": _utc_timestamp(),
            "resolver_module": __name__,
        },
        "selected_current_work_input": _selected_work_input_summary(
            work_input,
            work_input_path,
        ),
        "effective_inputs": _effective_inputs(work_input),
        "checks": checks,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "work_output": dict(work_output) if work_output is not None else None,
        "work_summary": dict(summary),
        "non_claims": dict(non_claims),
    }


def _selected_work_input_summary(
    work_input: Mapping[str, Any] | None,
    work_input_path: Path | None,
) -> dict[str, Any]:
    if work_input is None:
        return {
            "current_work_input_result_artifact_path": (
                _display(work_input_path) if work_input_path is not None else None
            ),
            "current_work_input_resolution_id": None,
            "current_work_input_resolution_type": None,
            "current_work_input_resolution_version": None,
            "outcome": None,
            "selected_effective_family_resolution_id": None,
        }
    metadata = _obj(work_input, "work_input_metadata", "current-work-input result")
    selected = _obj(
        work_input,
        "selected_effective_family_consumption",
        "current-work-input result",
    )
    return {
        "current_work_input_result_artifact_path": (
            _display(work_input_path) if work_input_path is not None else None
        ),
        "current_work_input_resolution_id": metadata.get(
            "current_work_input_resolution_id"
        ),
        "current_work_input_resolution_type": metadata.get(
            "current_work_input_resolution_type"
        ),
        "current_work_input_resolution_version": metadata.get(
            "current_work_input_resolution_version"
        ),
        "outcome": work_input.get("outcome"),
        "selected_effective_family_resolution_id": selected.get(
            "selected_effective_family_resolution_id"
        ),
    }


def _effective_inputs(work_input: Mapping[str, Any] | None) -> dict[str, Any]:
    if work_input is None:
        return _null_work_inputs()
    inputs = _obj(work_input, "effective_work_inputs", "current-work-input result")
    result: dict[str, Any] = {}
    for key in WORK_INPUT_KEYS:
        value = inputs.get(key)
        result[key] = value if isinstance(value, str) else None
    return result


def _resolved_work_input_references(
    work_input: Mapping[str, Any] | None,
) -> dict[str, Any]:
    if work_input is None:
        return _null_work_inputs()
    refs = _obj(
        work_input,
        "resolved_work_input_references",
        "current-work-input result",
    )
    result: dict[str, Any] = {}
    for key in WORK_INPUT_KEYS:
        value = refs.get(key)
        result[key] = value if isinstance(value, str) else None
    return result


def _null_work_inputs() -> dict[str, None]:
    return {key: None for key in WORK_INPUT_KEYS}


def _work_output(
    work_input: Mapping[str, Any],
    effective_family: Mapping[str, Any],
) -> dict[str, Any]:
    authority_summary = _obj(effective_family, "authority_summary", "effective family")
    status_summary = _obj(effective_family, "status_summary", "effective family")
    governing_summary = _obj(effective_family, "governing_summary", "effective family")
    return {
        "current_governing_source_run_path": governing_summary.get(
            "current_governing_source_run_path"
        ),
        "current_governing_ingress_run_path": governing_summary.get(
            "current_governing_ingress_run_path"
        ),
        "current_authority_artifact_path": _display(
            _path_value(effective_family, "authority_path")
        ),
        "current_family_packet_path": _display(
            _path_value(effective_family, "family_path")
        ),
        "current_status_packet_path": _display(
            _path_value(effective_family, "status_path")
        ),
        "current_governing_packet_path": _display(
            _path_value(effective_family, "governing_path")
        ),
        "preserved_run_count": status_summary.get("preserved_run_count"),
        "current_authority_run_count": status_summary.get(
            "current_authority_run_count"
        ),
        "preserved_eligible_non_authority_count": status_summary.get(
            "preserved_eligible_non_authority_count"
        ),
        "preserved_ineligible_count": status_summary.get(
            "preserved_ineligible_count"
        ),
        "current_authority_candidate_run_count": authority_summary.get(
            "candidate_run_count"
        ),
        "current_work_basis": _current_work_basis(work_input),
    }


def _work_summary(
    work_input: Mapping[str, Any],
    effective_family: Mapping[str, Any],
) -> dict[str, Any]:
    status_summary = _obj(effective_family, "status_summary", "effective family")
    governing_summary = _obj(effective_family, "governing_summary", "effective family")
    work_input_summary = _obj(
        work_input,
        "work_input_summary",
        "current-work-input result",
    )
    return {
        "effective_current_governing_source_run_path": governing_summary.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": governing_summary.get(
            "current_governing_ingress_run_path"
        ),
        "preserved_run_count": status_summary.get("preserved_run_count"),
        "current_authority_run_count": status_summary.get(
            "current_authority_run_count"
        ),
        "current_work_basis": _current_work_basis(work_input),
        "prior_family_remained_preserved": work_input_summary.get(
            "prior_family_remained_preserved"
        ),
    }


def _blocked_summary(work_input: Mapping[str, Any] | None) -> dict[str, Any]:
    if work_input is None:
        return {
            "effective_current_governing_source_run_path": None,
            "effective_current_governing_ingress_run_path": None,
            "preserved_run_count": None,
            "current_authority_run_count": None,
            "current_work_basis": None,
            "prior_family_remained_preserved": None,
        }
    inputs = _effective_inputs(work_input)
    summary = _obj(work_input, "work_input_summary", "current-work-input result")
    return {
        "effective_current_governing_source_run_path": inputs.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": inputs.get(
            "effective_ingress_run_path"
        ),
        "preserved_run_count": None,
        "current_authority_run_count": None,
        "current_work_basis": summary.get("consumed_current_family_basis")
        or OUTCOME_CURRENT_WORK_INPUT_RESOLVED,
        "prior_family_remained_preserved": summary.get(
            "prior_family_remained_preserved"
        ),
    }


def _validate_current_work_input_result(payload: dict[str, Any]) -> dict[str, Any]:
    for key in (
        "work_input_metadata",
        "selected_effective_family_consumption",
        "effective_work_inputs",
        "checks",
        "outcome",
        "block",
        "resolved_work_input_references",
        "work_input_summary",
        "non_claims",
    ):
        if key == "checks":
            _list(payload, key, "current-work-input result")
        elif key == "outcome":
            _str(payload, key, "current-work-input result")
        else:
            _obj(payload, key, "current-work-input result")

    metadata = _obj(payload, "work_input_metadata", "current-work-input result")
    _str(metadata, "current_work_input_resolution_id", "work-input metadata")
    if payload.get("outcome") == OUTCOME_CURRENT_WORK_INPUT_RESOLVED:
        refs = _obj(
            payload,
            "resolved_work_input_references",
            "current-work-input result",
        )
        inputs = _obj(payload, "effective_work_inputs", "current-work-input result")
        for key in PATH_INPUT_KEYS:
            _str(refs, key, "current-work-input result.resolved_work_input_references")
            _str(inputs, key, "current-work-input result.effective_work_inputs")
    _current_work_input_non_claims(payload)
    try:
        build_current_work_input_summary(payload)
    except Exception as exc:
        raise CurrentWorkOperationError(
            "Current-work-input result artifact is malformed"
        ) from exc
    return payload


def _looks_like_current_work_input_result(payload: Mapping[str, Any]) -> bool:
    return (
        isinstance(payload.get("work_input_metadata"), Mapping)
        and isinstance(payload.get("outcome"), str)
        and (
            "resolved_work_input_references" in payload
            or "effective_work_inputs" in payload
        )
    )


def _read_current_work_input_result(path: Path) -> dict[str, Any]:
    return _validate_current_work_input_result(
        _read_json(path, "current-work-input result")
    )


def _read_json(path: Path, label: str) -> dict[str, Any]:
    file_path = _repo_path(path)
    try:
        value = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise _UnreadableArtifact(
            f"{label} file does not exist: {_display(file_path)}"
        ) from exc
    except OSError as exc:
        raise _UnreadableArtifact(f"Could not read {label}: {_display(file_path)}") from exc
    except json.JSONDecodeError as exc:
        raise CurrentWorkOperationError(
            f"{label.title()} is not valid JSON: {_display(file_path)}"
        ) from exc
    if not isinstance(value, dict):
        raise CurrentWorkOperationError(
            f"{label.title()} JSON must be an object: {_display(file_path)}"
        )
    return value


def _authority_summary(authority: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_execution_authority_summary(authority)
    except Exception as exc:
        raise CurrentWorkOperationError(
            "Effective authority artifact is malformed"
        ) from exc


def _family_summary(family: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_run_family_summary(family)
    except Exception as exc:
        raise CurrentWorkOperationError("Effective family packet is malformed") from exc


def _status_summary(status: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_preserved_run_status_summary(status)
    except Exception as exc:
        raise CurrentWorkOperationError("Effective status packet is malformed") from exc


def _governing_summary(governing: Mapping[str, Any]) -> dict[str, Any]:
    try:
        return build_current_governing_summary(governing)
    except Exception as exc:
        raise CurrentWorkOperationError(
            "Effective current-governing packet is malformed"
        ) from exc


def _current_work_input_non_claims(work_input: Mapping[str, Any]) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    _merge_non_claims(
        non_claims,
        _obj(work_input, "non_claims", "current-work-input result"),
        "current-work-input result",
    )
    return non_claims


def _combined_non_claims(
    base_non_claims: Mapping[str, bool],
    effective_family: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    _merge_non_claims(non_claims, base_non_claims, "current-work-input result")
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
            raise CurrentWorkOperationError(f"{context}.non_claims.{key} must be a boolean")
        target[key] = value


def _all_non_claims_false(non_claims: Mapping[str, Any]) -> bool:
    return all(non_claims.get(key) is False for key in NON_CLAIM_DEFAULTS)


def _core_values(effective_family: Mapping[str, Any]) -> dict[str, str]:
    return {
        "authority": _core(
            _obj(effective_family, "authority", "effective family"),
            "authority",
        ),
        "family": _core(
            _obj(effective_family, "family", "effective family"),
            "family",
        ),
        "status": _core(
            _obj(effective_family, "status", "effective family"),
            "status",
        ),
        "governing": _core(
            _obj(effective_family, "governing", "effective family"),
            "governing",
        ),
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


def _resolved_refs_match_loaded_paths(
    work_input: Mapping[str, Any],
    effective_family: Mapping[str, Any],
) -> bool:
    refs = _obj(
        work_input,
        "resolved_work_input_references",
        "current-work-input result",
    )
    return all(
        _same(_path_value(effective_family, stack_key), refs.get(result_key))
        for stack_key, result_key in (
            ("authority_path", "effective_authority_artifact_path"),
            ("family_path", "effective_family_packet_path"),
            ("status_path", "effective_status_packet_path"),
            ("governing_path", "effective_current_governing_packet_path"),
        )
    )


def _resolved_refs_match_effective_inputs(work_input: Mapping[str, Any]) -> bool:
    refs = _obj(
        work_input,
        "resolved_work_input_references",
        "current-work-input result",
    )
    inputs = _obj(work_input, "effective_work_inputs", "current-work-input result")
    return all(_same(refs.get(key), inputs.get(key)) for key in PATH_INPUT_KEYS)


def _loaded_family_paths(effective_family: Mapping[str, Any]) -> dict[str, str]:
    return {
        "effective_authority_artifact_path": _display(
            _path_value(effective_family, "authority_path")
        ),
        "effective_family_packet_path": _display(
            _path_value(effective_family, "family_path")
        ),
        "effective_status_packet_path": _display(
            _path_value(effective_family, "status_path")
        ),
        "effective_current_governing_packet_path": _display(
            _path_value(effective_family, "governing_path")
        ),
    }


def _prior_family_preserved(work_input: Mapping[str, Any]) -> bool:
    summary = _obj(work_input, "work_input_summary", "current-work-input result")
    value = summary.get("prior_family_remained_preserved")
    return value is True or value is None


def _stale_prior_family_fallback(work_input: Mapping[str, Any]) -> bool:
    return not _resolved_refs_match_effective_inputs(work_input)


def _current_work_input_identity(work_input: Mapping[str, Any]) -> tuple[Any, ...]:
    selected = _obj(
        work_input,
        "selected_effective_family_consumption",
        "current-work-input result",
    )
    refs = _obj(
        work_input,
        "resolved_work_input_references",
        "current-work-input result",
    )
    return (
        work_input.get("outcome"),
        selected.get("selected_effective_family_resolution_id"),
        refs.get("effective_authority_artifact_path"),
        refs.get("effective_family_packet_path"),
        refs.get("effective_status_packet_path"),
        refs.get("effective_current_governing_packet_path"),
    )


def _work_result_id(work_input: Mapping[str, Any] | None, outcome: str) -> str:
    if work_input is None:
        base = "no_current_work_input_resolution"
    else:
        metadata = _obj(work_input, "work_input_metadata", "current-work-input result")
        base = _str(
            metadata,
            "current_work_input_resolution_id",
            "work-input metadata",
        )
    suffix = "completed" if outcome == OUTCOME_COMPLETED else "blocked"
    return f"{base}__{suffix}_current_work_operation"


def _current_work_basis(work_input: Mapping[str, Any]) -> str:
    summary = _obj(work_input, "work_input_summary", "current-work-input result")
    value = summary.get("consumed_current_family_basis")
    return value if isinstance(value, str) and value else OUTCOME_CURRENT_WORK_INPUT_RESOLVED


def _first_failed(checks: list[Mapping[str, Any]]) -> dict[str, str] | None:
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code")
        name = check.get("check")
        return {
            "check": str(name) if name else "unknown_check",
            "block_code": str(code)
            if code
            else "EFFECTIVE_WORK_INPUT_NOT_INTERNALLY_COHERENT",
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
        raise CurrentWorkOperationError(f"{key} must be a Path")
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
    index = 1
    while True:
        candidate = root / f"{stem}_{index:03d}.json"
        if not candidate.exists():
            return candidate
        index += 1


def _next_default_work_operation_path(root: Path) -> Path:
    return _next_json_path(root, DEFAULT_WORK_OPERATION_RESULT_STEM)


def _safe(value: str) -> str:
    return "".join(char if char.isalnum() or char in "._-" else "_" for char in value)


def _obj(mapping: Mapping[str, Any], key: str, context: str) -> Mapping[str, Any]:
    value = mapping.get(key)
    if not isinstance(value, Mapping):
        raise CurrentWorkOperationError(f"{context}.{key} must be an object")
    return value


def _list(mapping: Mapping[str, Any], key: str, context: str) -> list[Any]:
    value = mapping.get(key)
    if not isinstance(value, list):
        raise CurrentWorkOperationError(f"{context}.{key} must be a list")
    return value


def _str(mapping: Mapping[str, Any], key: str, context: str) -> str:
    value = mapping.get(key)
    if not isinstance(value, str) or not value:
        raise CurrentWorkOperationError(f"{context}.{key} must be a non-empty string")
    return value


def _bool(mapping: Mapping[str, Any], key: str, context: str) -> bool:
    value = mapping.get(key)
    if not isinstance(value, bool):
        raise CurrentWorkOperationError(f"{context}.{key} must be a boolean")
    return value
