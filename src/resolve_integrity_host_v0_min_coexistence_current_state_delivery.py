"""Resolve one bounded current-state delivery for the v0-min coexistence line.

This module consumes an exported current-state result, verifies the effective
artifacts named by that result, and emits one additive delivery result surface.
It does not replay, merge, mutate prior artifacts, or claim continuity
completion.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from resolve_integrity_host_v0_min_coexistence_current_state_export import (
    CANONICAL_CORE_EXECUTION_FILE,
    CURRENT_STATE_EXPORT_ROOT,
    NON_CLAIM_DEFAULTS as EXPORT_NON_CLAIM_DEFAULTS,
    OUTCOME_EXPORTED as CURRENT_STATE_EXPORT_EXPORTED,
    build_current_governing_summary,
    build_current_state_export_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


class CurrentStateDeliveryError(RuntimeError):
    """Raised when delivery input artifacts are malformed or impossible to use."""


CURRENT_STATE_DELIVERY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_delivery"
)

DELIVERY_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_DELIVERY_RESULT"
)
DELIVERY_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_integrity_host_v0_min_coexistence_current_state_delivery"

OUTCOME_DELIVERED = "DELIVERED"
OUTCOME_BLOCKED = "BLOCKED"

DEFAULT_DELIVERY_RESULT_STEM = "current_state_delivery_result"

PATH_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
)

DELIVERY_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

EXPORT_OUTPUT_PATH_KEYS = {
    "effective_authority_artifact_path": "current_authority_artifact_path",
    "effective_family_packet_path": "current_family_packet_path",
    "effective_status_packet_path": "current_status_packet_path",
    "effective_current_governing_packet_path": "current_governing_packet_path",
}

BLOCK_REASONS = {
    "NO_CURRENT_STATE_EXPORT_RESULT": (
        "No exported current-state result is available for delivery."
    ),
    "CURRENT_STATE_EXPORT_UNREADABLE": (
        "The selected current-state export result could not be read."
    ),
    "CURRENT_STATE_EXPORT_NOT_EXPORTED": (
        "The selected current-state export result is not exported."
    ),
    "EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE": (
        "One or more effective delivery artifacts are unreadable."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "Effective delivery artifacts do not preserve the canonical execution line."
    ),
    "EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT": (
        "Effective delivery inputs are not internally coherent."
    ),
    "EFFECTIVE_DELIVERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "Effective delivery inputs do not correspond to the selected export result."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based delivery is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based delivery is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity completion by delivery is refused."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Silent standing upgrade by delivery is refused."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Silent fallback to stale prior-family artifacts is refused."
    ),
    "MULTIPLE_CURRENT_STATE_EXPORT_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple exported current-state results conflict without an explicit "
        "bounded selection surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **EXPORT_NON_CLAIM_DEFAULTS,
    "final_current_state_delivery_completed": False,
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
        raise CurrentStateDeliveryError(
            f"{context} is unreadable: {resolved}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateDeliveryError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(payload, dict):
        raise CurrentStateDeliveryError(
            f"{context} must be a JSON object: {resolved}"
        )
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
        raise CurrentStateDeliveryError(f"{context} non_claims must be an object")
    result: dict[str, bool] = {}
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateDeliveryError(
                f"{context} non_claims keys must be strings"
            )
        if not isinstance(value, bool):
            raise CurrentStateDeliveryError(
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
    export: Mapping[str, Any],
    effective_artifacts: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, bool]:
    surfaces: list[Mapping[str, bool]] = [
        _non_claims_from(export, "current-state export result")
    ]
    if effective_artifacts is not None:
        for name, artifact in effective_artifacts.items():
            if name.startswith("_"):
                continue
            surfaces.append(_non_claims_from(artifact, f"effective {name} artifact"))
    return _merge_non_claims(*surfaces)


def _validate_current_state_export_result(export: Mapping[str, Any]) -> None:
    if not _is_mapping(export.get("export_metadata")):
        raise CurrentStateDeliveryError("current-state export metadata is missing")
    if not _is_mapping(export.get("selected_current_state_handoff")):
        raise CurrentStateDeliveryError(
            "selected current-state handoff section is missing"
        )
    if not _is_mapping(export.get("effective_export_inputs")):
        raise CurrentStateDeliveryError("effective export inputs are missing")
    if "outcome" not in export:
        raise CurrentStateDeliveryError("current-state export outcome is missing")
    if not _is_mapping(export.get("block")):
        raise CurrentStateDeliveryError("current-state export block section is missing")
    if not isinstance(export.get("checks"), list):
        raise CurrentStateDeliveryError("current-state export checks must be a list")
    if not _is_mapping(export.get("non_claims")):
        raise CurrentStateDeliveryError("current-state export non_claims are missing")

    metadata = export["export_metadata"]
    if not isinstance(metadata.get("export_result_id"), str) or not metadata.get(
        "export_result_id"
    ):
        raise CurrentStateDeliveryError("current-state export result id is missing")

    if export.get("outcome") == CURRENT_STATE_EXPORT_EXPORTED:
        if not _is_mapping(export.get("export_output")):
            raise CurrentStateDeliveryError(
                "exported current-state result must include export_output"
            )
        inputs = export["effective_export_inputs"]
        for key in PATH_INPUT_KEYS:
            if not isinstance(inputs.get(key), str) or not inputs.get(key):
                raise CurrentStateDeliveryError(
                    f"exported current-state result is missing {key}"
                )

    try:
        build_current_state_export_summary(export)
    except Exception as exc:
        raise CurrentStateDeliveryError(
            "current-state export summary could not be built"
        ) from exc


def _looks_like_current_state_export_result(payload: Mapping[str, Any]) -> bool:
    return (
        _is_mapping(payload.get("export_metadata"))
        and "export_result_id" in payload["export_metadata"]
        and "effective_export_inputs" in payload
        and "outcome" in payload
    )


def _selected_current_state_export(
    export: Mapping[str, Any] | None,
    export_path: Path | str | None,
) -> dict[str, Any]:
    if export is None:
        return {
            "current_state_export_result_path": (
                str(_repo_path(export_path)) if export_path is not None else None
            ),
            "current_state_export_result_id": None,
            "outcome": None,
            "selected_current_state_handoff_id": None,
        }

    metadata = export.get("export_metadata", {})
    selected_handoff = export.get("selected_current_state_handoff", {})
    return {
        "current_state_export_result_path": (
            str(_repo_path(export_path)) if export_path is not None else None
        ),
        "current_state_export_result_id": metadata.get("export_result_id"),
        "outcome": export.get("outcome"),
        "selected_current_state_handoff_id": selected_handoff.get(
            "current_state_handoff_result_id"
        )
        if isinstance(selected_handoff, Mapping)
        else None,
    }


def _effective_delivery_inputs_from(export: Mapping[str, Any] | None) -> dict[str, Any]:
    inputs = export.get("effective_export_inputs", {}) if export is not None else {}
    if not isinstance(inputs, Mapping):
        inputs = {}
    return {key: inputs.get(key) for key in DELIVERY_INPUT_KEYS}


def _delivery_result_id(export: Mapping[str, Any] | None, outcome: str) -> str:
    if export is not None and _is_mapping(export.get("export_metadata")):
        base = export["export_metadata"].get("export_result_id")
    else:
        base = None
    if not isinstance(base, str) or not base:
        base = "no_current_state_export_result"
    suffix = (
        "current_state_delivery_delivered"
        if outcome == OUTCOME_DELIVERED
        else "current_state_delivery_blocked"
    )
    return f"{base}__{suffix}"


def _blocked_summary(
    export: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    inputs = _effective_delivery_inputs_from(export)
    passed, failed = _count_checks(checks)
    return {
        "selected_current_state_export_id": (
            export.get("export_metadata", {}).get("export_result_id")
            if export is not None and _is_mapping(export.get("export_metadata"))
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
        "delivery_basis": None,
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def _result(
    *,
    export: Mapping[str, Any] | None,
    export_path: Path | str | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    delivery_output: Mapping[str, Any] | None,
    delivery_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    result_non_claims = dict(non_claims or NON_CLAIM_DEFAULTS)
    for key in NON_CLAIM_DEFAULTS:
        result_non_claims.setdefault(key, False)

    selected = _selected_current_state_export(export, export_path)
    effective_inputs = _effective_delivery_inputs_from(export)
    check_list = [dict(check) for check in checks]
    summary = dict(delivery_summary or _blocked_summary(export, check_list))

    return {
        "delivery_metadata": {
            "delivery_result_id": _delivery_result_id(export, outcome),
            "delivery_result_type": DELIVERY_RESULT_TYPE,
            "delivery_result_version": DELIVERY_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_export": selected,
        "effective_delivery_inputs": effective_inputs,
        "checks": check_list,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "delivery_output": (
            dict(delivery_output) if delivery_output is not None else None
        ),
        "delivery_summary": summary,
        "non_claims": result_non_claims,
    }


def _blocked_result(
    *,
    export: Mapping[str, Any] | None,
    export_path: Path | str | None,
    block_code: str,
    block_reason: str | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    check_list = list(checks or [])
    return _result(
        export=export,
        export_path=export_path,
        checks=check_list,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason or BLOCK_REASONS.get(block_code, block_code),
        delivery_output=None,
        delivery_summary=_blocked_summary(export, check_list),
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _candidate_json_files(root: Path | str) -> list[Path]:
    resolved_root = _repo_path(root)
    if not resolved_root.exists():
        return []
    if not resolved_root.is_dir():
        raise CurrentStateDeliveryError(
            f"current-state export root is not a directory: {resolved_root}"
        )
    return sorted(path for path in resolved_root.glob("*.json") if path.is_file())


def _load_current_state_export_from_path(path: Path | str) -> dict[str, Any]:
    export = _read_json_file(path, "current-state export result")
    _validate_current_state_export_result(export)
    return export


def discover_latest_exported_current_state_export_result(
    root: Path | str = CURRENT_STATE_EXPORT_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Return the lexically latest exported result when unambiguous."""

    candidates = _candidate_json_files(root)
    if not candidates:
        raise FileNotFoundError("no current-state export result artifacts found")

    exported: list[tuple[dict[str, Any], Path]] = []
    for path in candidates:
        payload = _read_json_file(path, "current-state export result")
        if not _looks_like_current_state_export_result(payload):
            continue
        _validate_current_state_export_result(payload)
        if payload.get("outcome") == CURRENT_STATE_EXPORT_EXPORTED:
            exported.append((payload, path))

    if not exported:
        raise FileNotFoundError("no exported current-state result artifacts found")

    distinct_ids = {
        payload["export_metadata"].get("export_result_id")
        for payload, _path in exported
    }
    if len(distinct_ids) > 1:
        raise CurrentStateDeliveryError(
            BLOCK_REASONS["MULTIPLE_CURRENT_STATE_EXPORT_RESULTS_CONFLICT_UNRESOLVED"]
        )
    return exported[-1]


discover_latest_current_state_export_result = (
    discover_latest_exported_current_state_export_result
)


def _select_default_current_state_export() -> tuple[
    dict[str, Any] | None,
    Path | None,
    str | None,
]:
    try:
        export, path = discover_latest_exported_current_state_export_result()
        return export, path, None
    except FileNotFoundError:
        return None, None, "NO_CURRENT_STATE_EXPORT_RESULT"
    except CurrentStateDeliveryError as exc:
        if (
            BLOCK_REASONS["MULTIPLE_CURRENT_STATE_EXPORT_RESULTS_CONFLICT_UNRESOLVED"]
            in str(exc)
        ):
            return (
                None,
                None,
                "MULTIPLE_CURRENT_STATE_EXPORT_RESULTS_CONFLICT_UNRESOLVED",
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
        raise CurrentStateDeliveryError(f"{context} is malformed") from exc
    if not isinstance(summary, dict):
        raise CurrentStateDeliveryError(f"{context} summary must be an object")
    return summary


def _load_effective_delivery_artifacts(
    export: Mapping[str, Any],
) -> dict[str, Any]:
    inputs = export.get("effective_export_inputs")
    if not isinstance(inputs, Mapping):
        raise CurrentStateDeliveryError("effective export inputs must be an object")

    missing = [
        key
        for key in PATH_INPUT_KEYS
        if not isinstance(inputs.get(key), str) or not inputs.get(key)
    ]
    if missing:
        raise FileNotFoundError(
            "missing effective delivery artifact path(s): " + ", ".join(missing)
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

    artifacts: dict[str, Any] = {
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
    artifacts: Mapping[str, Any],
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


def _canonical_core_values(artifacts: Mapping[str, Any]) -> list[Any]:
    return _summary_values(
        artifacts,
        (
            "canonical_core_execution_file",
            "canonical_execution_file",
            "core_execution_file",
        ),
    )


def _source_values(artifacts: Mapping[str, Any]) -> list[Any]:
    return _summary_values(
        artifacts,
        (
            "current_governing_source_run_path",
            "effective_source_run_path",
            "source_run_path",
            "current_source_run_path",
        ),
    )


def _ingress_values(artifacts: Mapping[str, Any]) -> list[Any]:
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
    export: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    inputs = export.get("effective_export_inputs", {})
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


def _export_output_paths_correspond(
    export: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    output = export.get("export_output", {})
    inputs = export.get("effective_export_inputs", {})
    if not isinstance(output, Mapping) or not isinstance(inputs, Mapping):
        return False

    for input_key, output_key in EXPORT_OUTPUT_PATH_KEYS.items():
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

    return _input_paths_correspond(export, artifacts)


def _prior_family_preserved(export: Mapping[str, Any]) -> bool:
    for section_name in ("export_summary", "export_output"):
        section = export.get(section_name)
        if isinstance(section, Mapping):
            value = section.get("prior_family_remained_preserved")
            if value is False:
                return False
    return True


def _stale_prior_family_fallback_attempted(
    export: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    return not _export_output_paths_correspond(export, artifacts)


def _export_basis(export: Mapping[str, Any]) -> Any:
    output = export.get("export_output", {})
    summary = export.get("export_summary", {})
    if isinstance(output, Mapping) and output.get("export_basis") is not None:
        return output.get("export_basis")
    if isinstance(summary, Mapping) and summary.get("export_basis") is not None:
        return summary.get("export_basis")
    return "exported_current_state_result"


def _delivery_checks(
    *,
    export: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    export_path: Path | str | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    canonical_values = _canonical_core_values(artifacts)
    source_values = _source_values(artifacts)
    ingress_values = _ingress_values(artifacts)
    summaries = artifacts.get("_summaries", {})
    effective_inputs = export.get("effective_export_inputs", {})

    canonical_match = bool(canonical_values) and all(
        str(value) == CANONICAL_CORE_EXECUTION_FILE for value in canonical_values
    )
    input_correspondence = _input_paths_correspond(export, artifacts)
    output_correspondence = _export_output_paths_correspond(export, artifacts)

    return [
        _check(
            "current_state_export_result_readable",
            True,
            expected="readable exported current-state result",
            actual=str(_repo_path(export_path)) if export_path is not None else None,
        ),
        _check(
            "current_state_export_outcome_exported",
            export.get("outcome") == CURRENT_STATE_EXPORT_EXPORTED,
            expected=CURRENT_STATE_EXPORT_EXPORTED,
            actual=export.get("outcome"),
            block_code="CURRENT_STATE_EXPORT_NOT_EXPORTED",
        ),
        _check(
            "effective_execution_authority_artifact_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("authority"), Mapping),
            expected="readable coherent effective authority artifact",
            actual=effective_inputs.get("effective_authority_artifact_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_run_family_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("family"), Mapping),
            expected="readable coherent effective family packet",
            actual=effective_inputs.get("effective_family_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_preserved_run_status_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("status"), Mapping),
            expected="readable coherent effective status packet",
            actual=effective_inputs.get("effective_status_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_current_governing_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("governing"), Mapping),
            expected="readable coherent effective current-governing packet",
            actual=effective_inputs.get("effective_current_governing_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_delivery_inputs_correspond_to_current_state_export_result",
            input_correspondence and output_correspondence,
            expected="effective inputs named by current-state export result",
            actual={
                "effective_input_paths_correspond": input_correspondence,
                "export_output_paths_correspond": output_correspondence,
            },
            block_code="EFFECTIVE_DELIVERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
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
            block_code="EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_inputs_share_current_governing_ingress_run_where_exposed",
            _same_present_values(ingress_values),
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT",
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
            expected=(
                "replay, merge, continuity completion, and standing upgrade "
                "remain false"
            ),
            actual={
                "replayed_into_live_host": non_claims.get("replayed_into_live_host"),
                "merged_into_local_state": non_claims.get("merged_into_local_state"),
                "continuity_completed": non_claims.get("continuity_completed"),
                "standing_upgraded": non_claims.get("standing_upgraded"),
            },
            block_code="EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "prior_family_preservation_visible_where_exposed",
            _prior_family_preserved(export),
            expected="prior family remains preserved where exposed",
            actual={
                "export_summary": export.get("export_summary", {}),
                "export_output": export.get("export_output", {}),
            },
            block_code="EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "uses_exported_current_state_result_explicitly",
            True,
            expected="delivery selected from exported current-state result",
            actual=str(_repo_path(export_path))
            if export_path is not None
            else "mapping input",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            not _stale_prior_family_fallback_attempted(export, artifacts),
            expected="no stale prior-family fallback",
            actual={
                "fallback_attempted": _stale_prior_family_fallback_attempted(
                    export, artifacts
                )
            },
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
    ]


def _delivery_output(
    export: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> dict[str, Any]:
    output = export.get("export_output", {})
    if not isinstance(output, Mapping):
        output = {}
    summaries = artifacts.get("_summaries", {})
    authority = summaries.get("authority", {}) if isinstance(summaries, Mapping) else {}
    family = summaries.get("family", {}) if isinstance(summaries, Mapping) else {}
    status = summaries.get("status", {}) if isinstance(summaries, Mapping) else {}
    governing = summaries.get("governing", {}) if isinstance(summaries, Mapping) else {}
    inputs = export.get("effective_export_inputs", {})
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
        "readout_basis": output.get("readout_basis"),
        "handoff_basis": output.get("handoff_basis"),
        "export_basis": _export_basis(export),
        "delivery_basis": "exported_current_state_result",
    }


def _delivery_summary(
    export: Mapping[str, Any],
    output: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    passed, failed = _count_checks(checks)
    return {
        "selected_current_state_export_id": export.get(
            "export_metadata", {}
        ).get("export_result_id")
        if _is_mapping(export.get("export_metadata"))
        else None,
        "effective_current_governing_source_run_path": output.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": output.get(
            "current_governing_ingress_run_path"
        ),
        "preserved_run_count": output.get("preserved_run_count"),
        "current_authority_run_count": output.get("current_authority_run_count"),
        "export_basis": output.get("export_basis"),
        "delivery_basis": output.get("delivery_basis"),
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def resolve_current_state_delivery(
    current_state_export: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded delivery result from an exported current-state result."""

    if current_state_export is None:
        export, export_path, block_code = _select_default_current_state_export()
        if block_code is not None:
            return _blocked_result(
                export=None,
                export_path=None,
                block_code=block_code,
            )
    else:
        if not isinstance(current_state_export, Mapping):
            raise CurrentStateDeliveryError("current_state_export must be a mapping")
        export = dict(current_state_export)
        export_path = None

    _validate_current_state_export_result(export)

    if export.get("outcome") != CURRENT_STATE_EXPORT_EXPORTED:
        checks = [
            _check(
                "current_state_export_outcome_exported",
                False,
                expected=CURRENT_STATE_EXPORT_EXPORTED,
                actual=export.get("outcome"),
                block_code="CURRENT_STATE_EXPORT_NOT_EXPORTED",
            )
        ]
        return _blocked_result(
            export=export,
            export_path=export_path,
            block_code="CURRENT_STATE_EXPORT_NOT_EXPORTED",
            checks=checks,
            non_claims=_combined_non_claims(export),
        )

    try:
        artifacts = _load_effective_delivery_artifacts(export)
    except FileNotFoundError as exc:
        checks = [
            _check(
                "effective_delivery_artifacts_readable",
                False,
                expected=(
                    "effective authority, family, status, and governing artifacts "
                    "readable"
                ),
                actual=str(exc),
                block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
            )
        ]
        return _blocked_result(
            export=export,
            export_path=export_path,
            block_code="EFFECTIVE_DELIVERY_ARTIFACT_UNREADABLE",
            checks=checks,
            non_claims=_combined_non_claims(export),
        )

    non_claims = _combined_non_claims(export, artifacts)
    checks = _delivery_checks(
        export=export,
        artifacts=artifacts,
        export_path=export_path,
        non_claims=non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        block_code = str(
            failed.get("block_code")
            or "EFFECTIVE_DELIVERY_INPUT_NOT_INTERNALLY_COHERENT"
        )
        return _blocked_result(
            export=export,
            export_path=export_path,
            block_code=block_code,
            block_reason=BLOCK_REASONS.get(block_code, block_code),
            checks=checks,
            non_claims=non_claims,
        )

    output = _delivery_output(export, artifacts)
    return _result(
        export=export,
        export_path=export_path,
        checks=checks,
        outcome=OUTCOME_DELIVERED,
        block_code=None,
        block_reason=None,
        delivery_output=output,
        delivery_summary=_delivery_summary(export, output, checks),
        non_claims=non_claims,
    )


def resolve_current_state_delivery_from_path(path: Path | str) -> dict[str, Any]:
    """Read one current-state export artifact and resolve one delivery result."""

    resolved_path = _repo_path(path)
    try:
        export = _load_current_state_export_from_path(resolved_path)
    except FileNotFoundError:
        return _blocked_result(
            export=None,
            export_path=resolved_path,
            block_code="CURRENT_STATE_EXPORT_UNREADABLE",
        )

    result = resolve_current_state_delivery(export)
    result["selected_current_state_export"][
        "current_state_export_result_path"
    ] = str(resolved_path)
    return result


def build_current_state_delivery_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a small inspection-friendly summary of a delivery result."""

    if not isinstance(result, Mapping):
        raise CurrentStateDeliveryError("delivery result must be a mapping")
    metadata = result.get("delivery_metadata", {})
    selected = result.get("selected_current_state_export", {})
    effective = result.get("effective_delivery_inputs", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateDeliveryError("delivery checks must be a list")
    passed, failed = _count_checks(checks)

    return {
        "delivery_result_id": metadata.get("delivery_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "selected_current_state_export_id": selected.get(
            "current_state_export_result_id"
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


def _safe_default_output_path(root: Path | str = CURRENT_STATE_DELIVERY_ROOT) -> Path:
    resolved_root = _repo_path(root)
    candidate = resolved_root / f"{DEFAULT_DELIVERY_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{DEFAULT_DELIVERY_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise CurrentStateDeliveryError(
        "no bounded current-state delivery filename available"
    )


def write_current_state_delivery_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-state delivery result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentStateDeliveryError("delivery result must be a mapping")

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path()
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current-state delivery result already exists: {target}")

    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
