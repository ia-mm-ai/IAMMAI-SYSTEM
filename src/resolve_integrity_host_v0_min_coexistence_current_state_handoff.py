"""Resolve one bounded current-state handoff for the v0-min coexistence line.

This module consumes an emitted current-state readout result, verifies the
effective artifacts named by that result, and emits one additive handoff result
surface. It does not replay, merge, mutate prior artifacts, or claim continuity
completion.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from resolve_integrity_host_v0_min_coexistence_current_state_readout import (
    CANONICAL_CORE_EXECUTION_FILE,
    CURRENT_STATE_READOUT_ROOT,
    NON_CLAIM_DEFAULTS as READOUT_NON_CLAIM_DEFAULTS,
    OUTCOME_EMITTED as CURRENT_STATE_READOUT_EMITTED,
    build_current_governing_summary,
    build_current_state_readout_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


class CurrentStateHandoffError(RuntimeError):
    """Raised when handoff input artifacts are malformed or impossible to use."""


CURRENT_STATE_HANDOFF_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_handoff"
)

HANDOFF_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_HANDOFF_RESULT"
)
HANDOFF_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_current_state_handoff"
)

OUTCOME_HANDED_OFF = "HANDED_OFF"
OUTCOME_BLOCKED = "BLOCKED"

DEFAULT_HANDOFF_RESULT_STEM = "current_state_handoff_result"

PATH_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
)

HANDOFF_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

READOUT_OUTPUT_PATH_KEYS = {
    "effective_authority_artifact_path": "current_authority_artifact_path",
    "effective_family_packet_path": "current_family_packet_path",
    "effective_status_packet_path": "current_status_packet_path",
    "effective_current_governing_packet_path": "current_governing_packet_path",
}

BLOCK_REASONS = {
    "NO_CURRENT_STATE_READOUT_RESULT": (
        "No emitted current-state readout result is available for handoff."
    ),
    "CURRENT_STATE_READOUT_UNREADABLE": (
        "The selected current-state readout result could not be read."
    ),
    "CURRENT_STATE_READOUT_NOT_EMITTED": (
        "The selected current-state readout result is not emitted."
    ),
    "EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE": (
        "One or more effective handoff artifacts are unreadable."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "Effective handoff artifacts do not preserve the canonical execution line."
    ),
    "EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT": (
        "Effective handoff inputs are not internally coherent."
    ),
    "EFFECTIVE_HANDOFF_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "Effective handoff inputs do not correspond to the selected readout result."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based handoff is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based handoff is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity completion by handoff is refused."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Silent standing upgrade by handoff is refused."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Silent fallback to stale prior-family artifacts is refused."
    ),
    "MULTIPLE_CURRENT_STATE_READOUT_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple emitted current-state readout results conflict without an explicit "
        "bounded selection surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **READOUT_NON_CLAIM_DEFAULTS,
    "final_current_state_handoff_completed": False,
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute():
        return candidate
    return _repo_root() / candidate


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise CurrentStateHandoffError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateHandoffError(f"{context} is malformed JSON: {resolved}") from exc
    if not isinstance(payload, dict):
        raise CurrentStateHandoffError(f"{context} must be a JSON object: {resolved}")
    return payload


def _check(
    name: str,
    passed: bool,
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
        if not check.get("passed"):
            return check
    return None


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _non_claims_from(payload: Mapping[str, Any], context: str) -> dict[str, bool]:
    raw = payload.get("non_claims", {})
    if raw is None:
        return {}
    if not isinstance(raw, Mapping):
        raise CurrentStateHandoffError(f"{context} non_claims must be an object")
    result: dict[str, bool] = {}
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateHandoffError(f"{context} non_claims keys must be strings")
        if not isinstance(value, bool):
            raise CurrentStateHandoffError(
                f"{context} non_claims value for {key!r} must be boolean"
            )
        result[key] = value
    return result


def _merge_non_claims(*surfaces: Mapping[str, bool]) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for surface in surfaces:
        merged.update(surface)
    for key in NON_CLAIM_DEFAULTS:
        merged.setdefault(key, False)
    return merged


def _combined_non_claims(
    readout: Mapping[str, Any],
    effective_artifacts: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, bool]:
    surfaces: list[Mapping[str, bool]] = [
        _non_claims_from(readout, "current-state readout result")
    ]
    if effective_artifacts is not None:
        for name, artifact in effective_artifacts.items():
            surfaces.append(_non_claims_from(artifact, f"effective {name} artifact"))
    return _merge_non_claims(*surfaces)


def _validate_current_state_readout_result(readout: Mapping[str, Any]) -> None:
    if not _is_mapping(readout.get("readout_metadata")):
        raise CurrentStateHandoffError("current-state readout metadata is missing")
    if not _is_mapping(readout.get("selected_current_work_operation")):
        raise CurrentStateHandoffError(
            "selected current-work-operation section is missing"
        )
    if not _is_mapping(readout.get("effective_readout_inputs")):
        raise CurrentStateHandoffError("effective readout inputs are missing")
    if "outcome" not in readout:
        raise CurrentStateHandoffError("current-state readout outcome is missing")
    if not _is_mapping(readout.get("block")):
        raise CurrentStateHandoffError("current-state readout block section is missing")
    if not isinstance(readout.get("checks"), list):
        raise CurrentStateHandoffError("current-state readout checks must be a list")
    if not _is_mapping(readout.get("non_claims")):
        raise CurrentStateHandoffError("current-state readout non_claims are missing")

    metadata = readout["readout_metadata"]
    if not isinstance(metadata.get("readout_result_id"), str) or not metadata.get(
        "readout_result_id"
    ):
        raise CurrentStateHandoffError("current-state readout result id is missing")

    if readout.get("outcome") == CURRENT_STATE_READOUT_EMITTED:
        if not _is_mapping(readout.get("readout_output")):
            raise CurrentStateHandoffError(
                "emitted current-state readout must include readout_output"
            )
        inputs = readout["effective_readout_inputs"]
        for key in PATH_INPUT_KEYS:
            if not isinstance(inputs.get(key), str) or not inputs.get(key):
                raise CurrentStateHandoffError(
                    f"emitted current-state readout is missing {key}"
                )

    try:
        build_current_state_readout_summary(readout)
    except Exception as exc:
        raise CurrentStateHandoffError(
            "current-state readout summary could not be built"
        ) from exc


def _looks_like_current_state_readout_result(payload: Mapping[str, Any]) -> bool:
    return (
        _is_mapping(payload.get("readout_metadata"))
        and "readout_result_id" in payload["readout_metadata"]
        and "effective_readout_inputs" in payload
        and "outcome" in payload
    )


def _selected_current_state_readout(
    readout: Mapping[str, Any] | None,
    readout_path: Path | str | None,
) -> dict[str, Any]:
    if readout is None:
        return {
            "current_state_readout_result_path": (
                str(_repo_path(readout_path)) if readout_path is not None else None
            ),
            "current_state_readout_result_id": None,
            "outcome": None,
            "selected_current_work_operation_id": None,
        }

    metadata = readout.get("readout_metadata", {})
    selected_work = readout.get("selected_current_work_operation", {})
    return {
        "current_state_readout_result_path": (
            str(_repo_path(readout_path)) if readout_path is not None else None
        ),
        "current_state_readout_result_id": metadata.get("readout_result_id"),
        "outcome": readout.get("outcome"),
        "selected_current_work_operation_id": selected_work.get(
            "current_work_operation_result_id"
        ),
    }


def _effective_handoff_inputs_from(readout: Mapping[str, Any] | None) -> dict[str, Any]:
    inputs = readout.get("effective_readout_inputs", {}) if readout is not None else {}
    if not isinstance(inputs, Mapping):
        inputs = {}
    return {key: inputs.get(key) for key in HANDOFF_INPUT_KEYS}


def _handoff_result_id(readout: Mapping[str, Any] | None, outcome: str) -> str:
    if readout is not None and _is_mapping(readout.get("readout_metadata")):
        base = readout["readout_metadata"].get("readout_result_id")
    else:
        base = None
    if not isinstance(base, str) or not base:
        base = "no_current_state_readout_result"
    suffix = (
        "current_state_handoff_handed_off"
        if outcome == OUTCOME_HANDED_OFF
        else "current_state_handoff_blocked"
    )
    return f"{base}__{suffix}"


def _blocked_summary(
    readout: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    inputs = _effective_handoff_inputs_from(readout)
    passed, failed = _count_checks(checks)
    return {
        "selected_current_state_readout_id": (
            readout.get("readout_metadata", {}).get("readout_result_id")
            if readout is not None and _is_mapping(readout.get("readout_metadata"))
            else None
        ),
        "effective_current_governing_source_run_path": inputs.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": inputs.get(
            "effective_ingress_run_path"
        ),
        "preserved_run_count": None,
        "current_authority_run_count": None,
        "handoff_basis": None,
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def _result(
    *,
    readout: Mapping[str, Any] | None,
    readout_path: Path | str | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    handoff_output: Mapping[str, Any] | None,
    handoff_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    result_non_claims = dict(non_claims or NON_CLAIM_DEFAULTS)
    for key in NON_CLAIM_DEFAULTS:
        result_non_claims.setdefault(key, False)

    selected = _selected_current_state_readout(readout, readout_path)
    effective_inputs = _effective_handoff_inputs_from(readout)
    check_list = [dict(check) for check in checks]
    summary = dict(handoff_summary or _blocked_summary(readout, check_list))

    return {
        "handoff_metadata": {
            "handoff_result_id": _handoff_result_id(readout, outcome),
            "handoff_result_type": HANDOFF_RESULT_TYPE,
            "handoff_result_version": HANDOFF_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_readout": selected,
        "effective_handoff_inputs": effective_inputs,
        "checks": check_list,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "handoff_output": dict(handoff_output) if handoff_output is not None else None,
        "handoff_summary": summary,
        "non_claims": result_non_claims,
    }


def _blocked_result(
    *,
    readout: Mapping[str, Any] | None,
    readout_path: Path | str | None,
    block_code: str,
    block_reason: str | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    check_list = list(checks or [])
    return _result(
        readout=readout,
        readout_path=readout_path,
        checks=check_list,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason or BLOCK_REASONS.get(block_code, block_code),
        handoff_output=None,
        handoff_summary=_blocked_summary(readout, check_list),
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _candidate_json_files(root: Path | str) -> list[Path]:
    resolved_root = _repo_path(root)
    if not resolved_root.exists():
        return []
    if not resolved_root.is_dir():
        raise CurrentStateHandoffError(
            f"current-state readout root is not a directory: {resolved_root}"
        )
    return sorted(path for path in resolved_root.glob("*.json") if path.is_file())


def _load_current_state_readout_from_path(path: Path | str) -> dict[str, Any]:
    readout = _read_json_file(path, "current-state readout result")
    _validate_current_state_readout_result(readout)
    return readout


def discover_latest_emitted_current_state_readout_result(
    root: Path | str = CURRENT_STATE_READOUT_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Return the lexically latest emitted readout when the selection is unambiguous."""

    candidates = _candidate_json_files(root)
    if not candidates:
        raise FileNotFoundError("no current-state readout result artifacts found")

    emitted: list[tuple[dict[str, Any], Path]] = []
    for path in candidates:
        payload = _read_json_file(path, "current-state readout result")
        if not _looks_like_current_state_readout_result(payload):
            continue
        _validate_current_state_readout_result(payload)
        if payload.get("outcome") == CURRENT_STATE_READOUT_EMITTED:
            emitted.append((payload, path))

    if not emitted:
        raise FileNotFoundError("no emitted current-state readout result artifacts found")

    distinct_ids = {
        payload["readout_metadata"].get("readout_result_id")
        for payload, _path in emitted
    }
    if len(distinct_ids) > 1:
        raise CurrentStateHandoffError(
            BLOCK_REASONS["MULTIPLE_CURRENT_STATE_READOUT_RESULTS_CONFLICT_UNRESOLVED"]
        )
    return emitted[-1]


discover_latest_current_state_readout_result = (
    discover_latest_emitted_current_state_readout_result
)


def _select_default_current_state_readout() -> tuple[
    dict[str, Any] | None,
    Path | None,
    str | None,
]:
    try:
        readout, path = discover_latest_emitted_current_state_readout_result()
        return readout, path, None
    except FileNotFoundError:
        return None, None, "NO_CURRENT_STATE_READOUT_RESULT"
    except CurrentStateHandoffError as exc:
        if (
            BLOCK_REASONS["MULTIPLE_CURRENT_STATE_READOUT_RESULTS_CONFLICT_UNRESOLVED"]
            in str(exc)
        ):
            return (
                None,
                None,
                "MULTIPLE_CURRENT_STATE_READOUT_RESULTS_CONFLICT_UNRESOLVED",
            )
        raise


def _build_summary(
    builder: Any,
    artifact: Mapping[str, Any],
    context: str,
) -> dict[str, Any]:
    try:
        summary = builder(artifact)
    except Exception as exc:
        raise CurrentStateHandoffError(f"{context} is malformed") from exc
    if not isinstance(summary, dict):
        raise CurrentStateHandoffError(f"{context} summary must be an object")
    return summary


def _load_effective_handoff_artifacts(
    readout: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    inputs = readout.get("effective_readout_inputs")
    if not isinstance(inputs, Mapping):
        raise CurrentStateHandoffError("effective readout inputs must be an object")

    missing = [
        key
        for key in PATH_INPUT_KEYS
        if not isinstance(inputs.get(key), str) or not inputs.get(key)
    ]
    if missing:
        raise FileNotFoundError(
            "missing effective handoff artifact path(s): " + ", ".join(missing)
        )

    authority = _read_json_file(
        inputs["effective_authority_artifact_path"],
        "effective authority artifact",
    )
    family = _read_json_file(
        inputs["effective_family_packet_path"],
        "effective family packet",
    )
    status = _read_json_file(
        inputs["effective_status_packet_path"],
        "effective preserved-run status packet",
    )
    governing = _read_json_file(
        inputs["effective_current_governing_packet_path"],
        "effective current-governing packet",
    )

    artifacts = {
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
    }
    artifacts["_summaries"] = {
        "authority": _build_summary(
            build_execution_authority_summary,
            authority,
            "effective authority artifact",
        ),
        "family": _build_summary(
            build_run_family_summary,
            family,
            "effective family packet",
        ),
        "status": _build_summary(
            build_preserved_run_status_summary,
            status,
            "effective preserved-run status packet",
        ),
        "governing": _build_summary(
            build_current_governing_summary,
            governing,
            "effective current-governing packet",
        ),
    }
    return artifacts


def _summary_values(
    artifacts: Mapping[str, Mapping[str, Any]],
    names: Sequence[str],
) -> list[Any]:
    summaries = artifacts.get("_summaries", {})
    values: list[Any] = []
    if not isinstance(summaries, Mapping):
        return values
    for summary in summaries.values():
        if not isinstance(summary, Mapping):
            continue
        for name in names:
            value = summary.get(name)
            if value not in (None, ""):
                values.append(value)
    return values


def _canonical_core_values(
    artifacts: Mapping[str, Mapping[str, Any]],
) -> list[Any]:
    return _summary_values(
        artifacts,
        (
            "canonical_core_execution_file",
            "canonical_execution_file",
            "core_execution_file",
        ),
    )


def _source_values(artifacts: Mapping[str, Mapping[str, Any]]) -> list[Any]:
    return _summary_values(
        artifacts,
        (
            "current_governing_source_run_path",
            "effective_source_run_path",
            "source_run_path",
            "current_source_run_path",
        ),
    )


def _ingress_values(artifacts: Mapping[str, Mapping[str, Any]]) -> list[Any]:
    return _summary_values(
        artifacts,
        (
            "current_governing_ingress_run_path",
            "effective_ingress_run_path",
            "ingress_run_path",
            "current_ingress_run_path",
        ),
    )


def _same_present_values(values: Sequence[Any]) -> bool:
    present = [str(value) for value in values if value not in (None, "")]
    return len(set(present)) <= 1


def _all_false(non_claims: Mapping[str, bool], names: Sequence[str]) -> bool:
    return all(non_claims.get(name) is False for name in names)


def _input_paths_correspond(
    readout: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> bool:
    inputs = readout.get("effective_readout_inputs", {})
    if not isinstance(inputs, Mapping):
        return False

    summaries = artifacts.get("_summaries", {})
    if not isinstance(summaries, Mapping):
        return False

    expectations = {
        "effective_authority_artifact_path": ("authority", "artifact_path"),
        "effective_family_packet_path": ("family", "artifact_path"),
        "effective_status_packet_path": ("status", "artifact_path"),
        "effective_current_governing_packet_path": ("governing", "artifact_path"),
    }
    for input_key, (summary_key, artifact_path_key) in expectations.items():
        selected = inputs.get(input_key)
        summary = summaries.get(summary_key, {})
        if not isinstance(selected, str) or not selected:
            return False
        if isinstance(summary, Mapping):
            actual = summary.get(artifact_path_key)
            if isinstance(actual, str) and actual and _repo_path(actual) != _repo_path(
                selected
            ):
                return False
    return True


def _readout_output_paths_correspond(
    readout: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> bool:
    output = readout.get("readout_output", {})
    inputs = readout.get("effective_readout_inputs", {})
    if not isinstance(output, Mapping) or not isinstance(inputs, Mapping):
        return False

    for input_key, output_key in READOUT_OUTPUT_PATH_KEYS.items():
        input_value = inputs.get(input_key)
        output_value = output.get(output_key)
        if isinstance(output_value, str) and output_value:
            if not isinstance(input_value, str) or not input_value:
                return False
            if _repo_path(output_value) != _repo_path(input_value):
                return False

    source_input = inputs.get("effective_source_run_path")
    source_output = output.get("current_governing_source_run_path")
    if isinstance(source_output, str) and source_output and isinstance(
        source_input, str
    ):
        if _repo_path(source_output) != _repo_path(source_input):
            return False

    ingress_input = inputs.get("effective_ingress_run_path")
    ingress_output = output.get("current_governing_ingress_run_path")
    if isinstance(ingress_output, str) and ingress_output and isinstance(
        ingress_input, str
    ):
        if _repo_path(ingress_output) != _repo_path(ingress_input):
            return False

    return _input_paths_correspond(readout, artifacts)


def _prior_family_preserved(readout: Mapping[str, Any]) -> bool:
    for section_name in ("readout_summary", "readout_output"):
        section = readout.get(section_name)
        if isinstance(section, Mapping):
            value = section.get("prior_family_remained_preserved")
            if value is False:
                return False
    return True


def _stale_prior_family_fallback_attempted(
    readout: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> bool:
    return not _readout_output_paths_correspond(readout, artifacts)


def _readout_basis(readout: Mapping[str, Any]) -> Any:
    output = readout.get("readout_output", {})
    summary = readout.get("readout_summary", {})
    if isinstance(output, Mapping) and output.get("readout_basis") is not None:
        return output.get("readout_basis")
    if isinstance(summary, Mapping) and summary.get("readout_basis") is not None:
        return summary.get("readout_basis")
    return "emitted_current_state_readout"


def _handoff_checks(
    *,
    readout: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
    readout_path: Path | str | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    canonical_values = _canonical_core_values(artifacts)
    source_values = _source_values(artifacts)
    ingress_values = _ingress_values(artifacts)
    summaries = artifacts.get("_summaries", {})
    effective_inputs = readout.get("effective_readout_inputs", {})

    canonical_match = bool(canonical_values) and all(
        str(value) == CANONICAL_CORE_EXECUTION_FILE for value in canonical_values
    )
    input_correspondence = _input_paths_correspond(readout, artifacts)
    output_correspondence = _readout_output_paths_correspond(readout, artifacts)

    return [
        _check(
            "current_state_readout_result_readable",
            True,
            expected="readable emitted current-state readout result",
            actual=str(_repo_path(readout_path)) if readout_path is not None else None,
        ),
        _check(
            "current_state_readout_outcome_emitted",
            readout.get("outcome") == CURRENT_STATE_READOUT_EMITTED,
            expected=CURRENT_STATE_READOUT_EMITTED,
            actual=readout.get("outcome"),
            block_code="CURRENT_STATE_READOUT_NOT_EMITTED",
        ),
        _check(
            "effective_execution_authority_artifact_readable_and_coherent",
            isinstance(summaries, Mapping) and isinstance(summaries.get("authority"), Mapping),
            expected="readable coherent effective authority artifact",
            actual=effective_inputs.get("effective_authority_artifact_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_run_family_packet_readable_and_coherent",
            isinstance(summaries, Mapping) and isinstance(summaries.get("family"), Mapping),
            expected="readable coherent effective family packet",
            actual=effective_inputs.get("effective_family_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_preserved_run_status_packet_readable_and_coherent",
            isinstance(summaries, Mapping) and isinstance(summaries.get("status"), Mapping),
            expected="readable coherent effective status packet",
            actual=effective_inputs.get("effective_status_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_current_governing_packet_readable_and_coherent",
            isinstance(summaries, Mapping) and isinstance(summaries.get("governing"), Mapping),
            expected="readable coherent effective current-governing packet",
            actual=effective_inputs.get("effective_current_governing_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_handoff_inputs_correspond_to_current_state_readout_result",
            input_correspondence and output_correspondence,
            expected="effective inputs named by current-state readout result",
            actual={
                "effective_input_paths_correspond": input_correspondence,
                "readout_output_paths_correspond": output_correspondence,
            },
            block_code="EFFECTIVE_HANDOFF_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
        ),
        _check(
            "effective_family_canonical_core_execution_file_matches",
            canonical_match,
            expected=CANONICAL_CORE_EXECUTION_FILE,
            actual=canonical_values,
            block_code="CANONICAL_EXECUTION_LINE_MISMATCH",
        ),
        _check(
            "effective_inputs_share_current_governing_source_run_where_exposed",
            _same_present_values(source_values),
            expected="same current governing source run where exposed",
            actual=source_values,
            block_code="EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_inputs_share_current_governing_ingress_run_where_exposed",
            _same_present_values(ingress_values),
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "replay_shortcut_refused",
            non_claims.get("replayed_into_live_host") is False,
            expected=False,
            actual=non_claims.get("replayed_into_live_host"),
            block_code="REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "merge_shortcut_refused",
            non_claims.get("merged_into_local_state") is False,
            expected=False,
            actual=non_claims.get("merged_into_local_state"),
            block_code="MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "continuity_completion_shortcut_refused",
            non_claims.get("continuity_completed") is False,
            expected=False,
            actual=non_claims.get("continuity_completed"),
            block_code="CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "silent_standing_upgrade_refused",
            non_claims.get("standing_upgraded") is False,
            expected=False,
            actual=non_claims.get("standing_upgraded"),
            block_code="SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "bounded_non_claims_remain_false",
            _all_false(
                non_claims,
                (
                    "replayed_into_live_host",
                    "merged_into_local_state",
                    "continuity_completed",
                    "standing_upgraded",
                ),
            ),
            expected="replay, merge, continuity completion, and standing upgrade remain false",
            actual={
                "replayed_into_live_host": non_claims.get("replayed_into_live_host"),
                "merged_into_local_state": non_claims.get("merged_into_local_state"),
                "continuity_completed": non_claims.get("continuity_completed"),
                "standing_upgraded": non_claims.get("standing_upgraded"),
            },
            block_code="EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "prior_family_preservation_visible_where_exposed",
            _prior_family_preserved(readout),
            expected="prior family remains preserved where exposed",
            actual={
                "readout_summary": readout.get("readout_summary", {}),
                "readout_output": readout.get("readout_output", {}),
            },
            block_code="EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "uses_emitted_current_state_readout_explicitly",
            True,
            expected="handoff selected from emitted current-state readout result",
            actual=str(_repo_path(readout_path)) if readout_path is not None else "mapping input",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            not _stale_prior_family_fallback_attempted(readout, artifacts),
            expected="no stale prior-family fallback",
            actual={
                "fallback_attempted": _stale_prior_family_fallback_attempted(
                    readout, artifacts
                )
            },
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
    ]


def _handoff_output(
    readout: Mapping[str, Any],
    artifacts: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    output = readout.get("readout_output", {})
    if not isinstance(output, Mapping):
        output = {}
    summaries = artifacts.get("_summaries", {})
    authority = summaries.get("authority", {}) if isinstance(summaries, Mapping) else {}
    family = summaries.get("family", {}) if isinstance(summaries, Mapping) else {}
    status = summaries.get("status", {}) if isinstance(summaries, Mapping) else {}
    governing = summaries.get("governing", {}) if isinstance(summaries, Mapping) else {}
    inputs = readout.get("effective_readout_inputs", {})
    if not isinstance(inputs, Mapping):
        inputs = {}

    source_path = (
        output.get("current_governing_source_run_path")
        or inputs.get("effective_source_run_path")
        or (
            governing.get("current_governing_source_run_path")
            if isinstance(governing, Mapping)
            else None
        )
    )
    ingress_path = (
        output.get("current_governing_ingress_run_path")
        or inputs.get("effective_ingress_run_path")
        or (
            governing.get("current_governing_ingress_run_path")
            if isinstance(governing, Mapping)
            else None
        )
    )

    return {
        "current_governing_source_run_path": source_path,
        "current_governing_ingress_run_path": ingress_path,
        "current_authority_artifact_path": inputs.get(
            "effective_authority_artifact_path"
        ),
        "current_family_packet_path": inputs.get("effective_family_packet_path"),
        "current_status_packet_path": inputs.get("effective_status_packet_path"),
        "current_governing_packet_path": inputs.get(
            "effective_current_governing_packet_path"
        ),
        "preserved_run_count": output.get("preserved_run_count")
        or (family.get("preserved_run_count") if isinstance(family, Mapping) else None),
        "current_authority_run_count": output.get("current_authority_run_count")
        or (
            authority.get("current_authority_run_count")
            if isinstance(authority, Mapping)
            else None
        ),
        "preserved_eligible_non_authority_count": output.get(
            "preserved_eligible_non_authority_count"
        )
        or (
            status.get("preserved_eligible_non_authority_count")
            if isinstance(status, Mapping)
            else None
        ),
        "preserved_ineligible_count": output.get("preserved_ineligible_count")
        or (
            status.get("preserved_ineligible_count")
            if isinstance(status, Mapping)
            else None
        ),
        "current_authority_candidate_run_count": output.get(
            "current_authority_candidate_run_count"
        ),
        "current_work_basis": output.get("current_work_basis"),
        "readout_basis": _readout_basis(readout),
        "handoff_basis": "emitted_current_state_readout",
    }


def _handoff_summary(
    readout: Mapping[str, Any],
    output: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed, failed = _count_checks(checks)
    return {
        "selected_current_state_readout_id": readout.get("readout_metadata", {}).get(
            "readout_result_id"
        )
        if _is_mapping(readout.get("readout_metadata"))
        else None,
        "effective_current_governing_source_run_path": output.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": output.get(
            "current_governing_ingress_run_path"
        ),
        "preserved_run_count": output.get("preserved_run_count"),
        "current_authority_run_count": output.get("current_authority_run_count"),
        "readout_basis": output.get("readout_basis"),
        "handoff_basis": output.get("handoff_basis"),
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def resolve_current_state_handoff(
    current_state_readout: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded handoff result from an emitted readout result."""

    if current_state_readout is None:
        readout, readout_path, block_code = _select_default_current_state_readout()
        if block_code is not None:
            return _blocked_result(
                readout=None,
                readout_path=None,
                block_code=block_code,
            )
    else:
        if not isinstance(current_state_readout, Mapping):
            raise CurrentStateHandoffError("current_state_readout must be a mapping")
        readout = dict(current_state_readout)
        readout_path = None

    _validate_current_state_readout_result(readout)

    if readout.get("outcome") != CURRENT_STATE_READOUT_EMITTED:
        checks = [
            _check(
                "current_state_readout_outcome_emitted",
                False,
                expected=CURRENT_STATE_READOUT_EMITTED,
                actual=readout.get("outcome"),
                block_code="CURRENT_STATE_READOUT_NOT_EMITTED",
            )
        ]
        return _blocked_result(
            readout=readout,
            readout_path=readout_path,
            block_code="CURRENT_STATE_READOUT_NOT_EMITTED",
            checks=checks,
            non_claims=_combined_non_claims(readout),
        )

    try:
        artifacts = _load_effective_handoff_artifacts(readout)
    except FileNotFoundError as exc:
        checks = [
            _check(
                "effective_handoff_artifacts_readable",
                False,
                expected="effective authority, family, status, and governing artifacts readable",
                actual=str(exc),
                block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
            )
        ]
        return _blocked_result(
            readout=readout,
            readout_path=readout_path,
            block_code="EFFECTIVE_HANDOFF_ARTIFACT_UNREADABLE",
            checks=checks,
            non_claims=_combined_non_claims(readout),
        )

    non_claims = _combined_non_claims(readout, artifacts)
    checks = _handoff_checks(
        readout=readout,
        artifacts=artifacts,
        readout_path=readout_path,
        non_claims=non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        block_code = str(
            failed.get("block_code") or "EFFECTIVE_HANDOFF_INPUT_NOT_INTERNALLY_COHERENT"
        )
        return _blocked_result(
            readout=readout,
            readout_path=readout_path,
            block_code=block_code,
            block_reason=BLOCK_REASONS.get(block_code, block_code),
            checks=checks,
            non_claims=non_claims,
        )

    output = _handoff_output(readout, artifacts)
    return _result(
        readout=readout,
        readout_path=readout_path,
        checks=checks,
        outcome=OUTCOME_HANDED_OFF,
        block_code=None,
        block_reason=None,
        handoff_output=output,
        handoff_summary=_handoff_summary(readout, output, checks),
        non_claims=non_claims,
    )


def resolve_current_state_handoff_from_path(path: Path | str) -> dict[str, Any]:
    """Read one current-state readout artifact and resolve one handoff result."""

    resolved_path = _repo_path(path)
    try:
        readout = _load_current_state_readout_from_path(resolved_path)
    except FileNotFoundError:
        return _blocked_result(
            readout=None,
            readout_path=resolved_path,
            block_code="CURRENT_STATE_READOUT_UNREADABLE",
        )

    result = resolve_current_state_handoff(readout)
    result["selected_current_state_readout"][
        "current_state_readout_result_path"
    ] = str(resolved_path)
    return result


def build_current_state_handoff_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a small inspection-friendly summary of a handoff result."""

    if not isinstance(result, Mapping):
        raise CurrentStateHandoffError("handoff result must be a mapping")
    metadata = result.get("handoff_metadata", {})
    selected = result.get("selected_current_state_readout", {})
    effective = result.get("effective_handoff_inputs", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateHandoffError("handoff checks must be a list")
    passed, failed = _count_checks(checks)

    return {
        "handoff_result_id": metadata.get("handoff_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "selected_current_state_readout_id": selected.get(
            "current_state_readout_result_id"
        )
        if isinstance(selected, Mapping)
        else None,
        "effective_authority_artifact_path": effective.get(
            "effective_authority_artifact_path"
        )
        if isinstance(effective, Mapping)
        else None,
        "effective_family_packet_path": effective.get("effective_family_packet_path")
        if isinstance(effective, Mapping)
        else None,
        "effective_status_packet_path": effective.get("effective_status_packet_path")
        if isinstance(effective, Mapping)
        else None,
        "effective_current_governing_packet_path": effective.get(
            "effective_current_governing_packet_path"
        )
        if isinstance(effective, Mapping)
        else None,
        "effective_source_run_path": effective.get("effective_source_run_path")
        if isinstance(effective, Mapping)
        else None,
        "effective_ingress_run_path": effective.get("effective_ingress_run_path")
        if isinstance(effective, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": dict(non_claims) if isinstance(non_claims, Mapping) else {},
    }


def _safe_default_output_path(root: Path | str = CURRENT_STATE_HANDOFF_ROOT) -> Path:
    resolved_root = _repo_path(root)
    candidate = resolved_root / f"{DEFAULT_HANDOFF_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{DEFAULT_HANDOFF_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentStateHandoffError("no bounded current-state handoff filename available")


def write_current_state_handoff_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-state handoff result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentStateHandoffError("handoff result must be a mapping")

    target = _repo_path(output_path) if output_path is not None else _safe_default_output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current-state handoff result already exists: {target}")

    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
