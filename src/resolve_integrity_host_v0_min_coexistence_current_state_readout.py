"""Resolve one bounded current-state readout from a completed work result.

This module is an additive downstream consumer for the v0-min coexistence
execution line. It reads one completed current-work-operation result and the
effective artifacts named by that result, then emits one bounded readout result.

It does not replay preserved runs, merge host state, mutate prior artifacts,
complete continuity, upgrade standing, or define final governance.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from resolve_integrity_host_v0_min_coexistence_current_work_operation_v2 import (
    CANONICAL_CORE_EXECUTION_FILE,
    CURRENT_WORK_OPERATION_ROOT,
    NON_CLAIM_DEFAULTS as WORK_OPERATION_NON_CLAIM_DEFAULTS,
    OUTCOME_COMPLETED as CURRENT_WORK_OPERATION_COMPLETED,
    build_current_governing_summary,
    build_current_work_operation_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


class CurrentStateReadoutError(RuntimeError):
    """Raised when required current-state readout inputs are malformed."""


CURRENT_STATE_READOUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_readout"
)

READOUT_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COHOST_CURRENT_STATE_READOUT_RESULT"
)
READOUT_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_integrity_host_v0_min_coexistence_current_state_readout"

OUTCOME_EMITTED = "EMITTED"
OUTCOME_BLOCKED = "BLOCKED"

DEFAULT_READOUT_RESULT_STEM = "current_state_readout_result"

READOUT_INPUT_KEYS = (
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

WORK_OUTPUT_PATH_KEYS = {
    "effective_authority_artifact_path": "current_authority_artifact_path",
    "effective_family_packet_path": "current_family_packet_path",
    "effective_status_packet_path": "current_status_packet_path",
    "effective_current_governing_packet_path": "current_governing_packet_path",
}

BLOCK_REASONS = {
    "NO_CURRENT_WORK_OPERATION_RESULT": "No completed current-work-operation result is available.",
    "CURRENT_WORK_OPERATION_UNREADABLE": "The selected current-work-operation result is unreadable.",
    "CURRENT_WORK_OPERATION_NOT_COMPLETED": "The selected current-work-operation result is not completed.",
    "EFFECTIVE_READOUT_ARTIFACT_UNREADABLE": "One or more effective readout artifacts are unreadable.",
    "CANONICAL_EXECUTION_LINE_MISMATCH": "Effective readout artifacts do not share the canonical execution line.",
    "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT": "Effective readout inputs are not internally coherent.",
    "EFFECTIVE_READOUT_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": "Effective readout inputs do not correspond to the selected current-work-operation result.",
    "REPLAY_SHORTCUT_REFUSED": "Current-state readout cannot proceed through replay into a live host.",
    "MERGE_SHORTCUT_REFUSED": "Current-state readout cannot proceed through merged preserved state.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": "Current-state readout cannot claim continuity completion.",
    "SILENT_STANDING_UPGRADE_REFUSED": "Current-state readout cannot silently upgrade local standing.",
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": "Current-state readout cannot fall back to stale prior-family artifacts.",
    "MULTIPLE_CURRENT_WORK_OPERATION_RESULTS_CONFLICT_UNRESOLVED": "Multiple completed current-work-operation results conflict without an explicit selection surface.",
}

NON_CLAIM_DEFAULTS: dict[str, bool] = {
    **WORK_OPERATION_NON_CLAIM_DEFAULTS,
    "final_current_state_readout_completed": False,
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    resolved = Path(path)
    if resolved.is_absolute():
        return resolved
    return _repo_root() / resolved


def _now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _read_json_file(path: Path | str, error_context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{error_context} does not exist: {resolved}") from exc
    except OSError as exc:
        raise OSError(f"{error_context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateReadoutError(
            f"{error_context} is malformed JSON: {resolved}"
        ) from exc

    if not isinstance(payload, dict):
        raise CurrentStateReadoutError(f"{error_context} must be a JSON object: {resolved}")
    return payload


def _looks_like_current_work_operation_result(payload: Mapping[str, Any]) -> bool:
    return (
        _is_mapping(payload.get("work_operation_metadata"))
        and isinstance(payload.get("outcome"), str)
        and (
            _is_mapping(payload.get("effective_inputs"))
            or _is_mapping(payload.get("work_output"))
        )
    )


def _validate_current_work_operation_result(payload: Mapping[str, Any]) -> None:
    required_keys = (
        "work_operation_metadata",
        "selected_current_work_input",
        "effective_inputs",
        "checks",
        "outcome",
        "block",
        "work_output",
        "work_summary",
        "non_claims",
    )
    for key in required_keys:
        if key not in payload:
            raise CurrentStateReadoutError(
                f"Current-work-operation result is missing required section: {key}"
            )

    if not _is_mapping(payload["work_operation_metadata"]):
        raise CurrentStateReadoutError("Current-work-operation metadata must be an object.")
    if not _is_mapping(payload["selected_current_work_input"]):
        raise CurrentStateReadoutError(
            "Selected current-work-input section must be an object."
        )
    if not _is_mapping(payload["effective_inputs"]):
        raise CurrentStateReadoutError("Effective inputs section must be an object.")
    if not isinstance(payload["checks"], list):
        raise CurrentStateReadoutError("Current-work-operation checks must be a list.")
    if not isinstance(payload["outcome"], str):
        raise CurrentStateReadoutError("Current-work-operation outcome must be a string.")
    if not _is_mapping(payload["block"]):
        raise CurrentStateReadoutError("Current-work-operation block must be an object.")
    if not _is_mapping(payload["work_summary"]):
        raise CurrentStateReadoutError("Current-work-operation summary must be an object.")
    if not _is_mapping(payload["non_claims"]):
        raise CurrentStateReadoutError("Current-work-operation non-claims must be an object.")

    metadata = payload["work_operation_metadata"]
    if not isinstance(metadata.get("work_result_id"), str) or not metadata.get(
        "work_result_id"
    ):
        raise CurrentStateReadoutError(
            "Current-work-operation result must preserve a non-empty work_result_id."
        )

    if payload["outcome"] == CURRENT_WORK_OPERATION_COMPLETED:
        if not _is_mapping(payload["work_output"]):
            raise CurrentStateReadoutError(
                "Completed current-work-operation result must preserve work_output."
            )
        for key in PATH_INPUT_KEYS:
            value = payload["effective_inputs"].get(key)
            if not isinstance(value, str) or not value:
                raise CurrentStateReadoutError(
                    f"Completed current-work-operation result is missing {key}."
                )
    elif payload["work_output"] is not None and not _is_mapping(payload["work_output"]):
        raise CurrentStateReadoutError(
            "Blocked current-work-operation work_output must be null or an object."
        )

    try:
        build_current_work_operation_summary(payload)
    except Exception as exc:  # noqa: BLE001 - normalize malformed dependency shape.
        raise CurrentStateReadoutError(
            "Current-work-operation result summary cannot be built."
        ) from exc


def _check(
    name: str,
    passed: bool,
    expected_posture: Any = None,
    actual_posture: Any = None,
    block_code: str | None = None,
) -> dict[str, Any]:
    result: dict[str, Any] = {"check_name": name, "passed": bool(passed)}
    if expected_posture is not None:
        result["expected_posture"] = expected_posture
    if actual_posture is not None:
        result["actual_posture"] = actual_posture
    if block_code is not None:
        result["block_code"] = block_code
    return result


def _first_failed(checks: Sequence[Mapping[str, Any]]) -> Mapping[str, Any] | None:
    for check in checks:
        if check.get("passed") is not True:
            return check
    return None


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = len(checks) - passed
    return passed, failed


def _non_claims_from(value: Mapping[str, Any] | None) -> dict[str, bool]:
    result = dict(NON_CLAIM_DEFAULTS)
    if value:
        for key in result:
            if key in value:
                result[key] = bool(value[key])
    return result


def _merge_non_claims(
    target: dict[str, bool],
    incoming: Mapping[str, Any],
    context: str,
) -> None:
    for key in target:
        if key in incoming:
            value = incoming[key]
            if not isinstance(value, bool):
                raise CurrentStateReadoutError(f"{context}.non_claims.{key} must be a boolean.")
            target[key] = value


def _combined_non_claims(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
) -> dict[str, bool]:
    non_claims = dict(NON_CLAIM_DEFAULTS)
    work_non_claims = current_work_operation.get("non_claims", {})
    if not _is_mapping(work_non_claims):
        raise CurrentStateReadoutError(
            "Current-work-operation non_claims must be an object."
        )
    _merge_non_claims(non_claims, work_non_claims, "current-work-operation result")

    for artifact_key in ("authority", "family", "status", "governing"):
        artifact = effective_artifacts[artifact_key]
        artifact_non_claims = artifact.get("non_claims", {})
        if not _is_mapping(artifact_non_claims):
            raise CurrentStateReadoutError(
                f"Effective {artifact_key} artifact non_claims must be an object."
            )
        _merge_non_claims(
            non_claims,
            artifact_non_claims,
            f"effective {artifact_key} artifact",
        )

    return non_claims


def _selected_current_work_operation(
    current_work_operation: Mapping[str, Any] | None,
    operation_path: Path | str | None,
) -> dict[str, Any]:
    if not current_work_operation:
        return {
            "current_work_operation_result_path": str(operation_path)
            if operation_path is not None
            else None,
            "current_work_operation_result_id": None,
            "outcome": None,
            "selected_current_work_input_id": None,
        }

    metadata = current_work_operation.get("work_operation_metadata", {})
    selected = current_work_operation.get("selected_current_work_input", {})
    return {
        "current_work_operation_result_path": str(operation_path)
        if operation_path is not None
        else None,
        "current_work_operation_result_id": metadata.get("work_result_id"),
        "outcome": current_work_operation.get("outcome"),
        "selected_current_work_input_id": selected.get("current_work_input_result_id"),
        "selected_effective_family_resolution_id": selected.get(
            "selected_effective_family_resolution_id"
        ),
    }


def _effective_readout_inputs_from(
    current_work_operation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    inputs = current_work_operation.get("effective_inputs", {}) if current_work_operation else {}
    if not _is_mapping(inputs):
        inputs = {}
    return {key: inputs.get(key) for key in READOUT_INPUT_KEYS}


def _readout_result_id(
    current_work_operation: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    if current_work_operation:
        metadata = current_work_operation.get("work_operation_metadata", {})
        base = metadata.get("work_result_id") or "unknown_current_work_operation"
    else:
        base = "no_current_work_operation_result"
    suffix = "emitted" if outcome == OUTCOME_EMITTED else "blocked"
    return f"{base}__{suffix}_current_state_readout"


def _result(
    *,
    current_work_operation: Mapping[str, Any] | None,
    operation_path: Path | str | None,
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
    readout_output: Mapping[str, Any] | None,
    readout_summary: Mapping[str, Any],
    non_claims: Mapping[str, bool] | None,
) -> dict[str, Any]:
    return {
        "readout_metadata": {
            "readout_result_id": _readout_result_id(current_work_operation, outcome),
            "readout_result_type": READOUT_RESULT_TYPE,
            "readout_result_version": READOUT_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_work_operation": _selected_current_work_operation(
            current_work_operation, operation_path
        ),
        "effective_readout_inputs": _effective_readout_inputs_from(current_work_operation),
        "checks": list(checks),
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "readout_output": dict(readout_output) if readout_output is not None else None,
        "readout_summary": dict(readout_summary),
        "non_claims": _non_claims_from(non_claims),
    }


def _blocked_result(
    *,
    current_work_operation: Mapping[str, Any] | None,
    operation_path: Path | str | None,
    block_code: str,
    block_reason: str | None = None,
    checks: Sequence[Mapping[str, Any]] = (),
    non_claims_override: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    if non_claims_override is None:
        non_claims = _non_claims_from(
            current_work_operation.get("non_claims", {})
            if _is_mapping(current_work_operation)
            else {}
        )
    else:
        non_claims = _non_claims_from(non_claims_override)
    return _result(
        current_work_operation=current_work_operation,
        operation_path=operation_path,
        outcome=OUTCOME_BLOCKED,
        checks=checks,
        block_code=block_code,
        block_reason=block_reason or BLOCK_REASONS[block_code],
        readout_output=None,
        readout_summary=_blocked_summary(current_work_operation),
        non_claims=non_claims,
    )


def _blocked_summary(
    current_work_operation: Mapping[str, Any] | None,
) -> dict[str, Any]:
    inputs = _effective_readout_inputs_from(current_work_operation)
    passed = failed = 0
    if current_work_operation and isinstance(current_work_operation.get("checks"), list):
        passed, failed = _count_checks(current_work_operation["checks"])
    return {
        "effective_current_governing_source_run_path": inputs.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": inputs.get(
            "effective_ingress_run_path"
        ),
        "preserved_run_count": None,
        "current_authority_run_count": None,
        "readout_basis": None,
        "upstream_passed_check_count": passed,
        "upstream_failed_check_count": failed,
    }


def _candidate_json_files(root: Path) -> list[Path]:
    if not root.exists():
        return []
    if not root.is_dir():
        raise CurrentStateReadoutError(
            f"Current-work-operation root is not a directory: {root}"
        )
    return sorted(path for path in root.glob("*.json") if path.is_file())


def _load_current_work_operation_from_path(path: Path | str) -> dict[str, Any]:
    payload = _read_json_file(path, "Current-work-operation result artifact")
    _validate_current_work_operation_result(payload)
    return payload


def discover_latest_completed_current_work_operation_result(
    root: Path | str = CURRENT_WORK_OPERATION_ROOT,
) -> Path:
    """Return the lexically latest completed current-work-operation artifact."""

    resolved_root = _repo_path(root)
    candidates = _candidate_json_files(resolved_root)
    if not candidates:
        raise FileNotFoundError(
            f"No current-work-operation result artifacts found under {resolved_root}"
        )

    completed: list[tuple[Path, str]] = []
    for path in candidates:
        try:
            payload = _read_json_file(path, "Current-work-operation result artifact")
        except CurrentStateReadoutError:
            raise
        except OSError as exc:
            raise CurrentStateReadoutError(
                f"Current-work-operation result is unreadable: {path}"
            ) from exc

        if not _looks_like_current_work_operation_result(payload):
            continue
        _validate_current_work_operation_result(payload)
        if payload.get("outcome") == CURRENT_WORK_OPERATION_COMPLETED:
            completed.append(
                (path, payload["work_operation_metadata"]["work_result_id"])
            )

    if not completed:
        raise FileNotFoundError(
            f"No completed current-work-operation result artifacts found under {resolved_root}"
        )

    identities = {identity for _, identity in completed}
    if len(identities) > 1:
        raise CurrentStateReadoutError(
            BLOCK_REASONS["MULTIPLE_CURRENT_WORK_OPERATION_RESULTS_CONFLICT_UNRESOLVED"]
        )

    return completed[-1][0]


def discover_latest_current_work_operation_result(
    root: Path | str = CURRENT_WORK_OPERATION_ROOT,
) -> Path:
    """Alias for the bounded completed-result discovery surface."""

    return discover_latest_completed_current_work_operation_result(root)


def _select_default_current_work_operation() -> tuple[dict[str, Any] | None, Path | None, str | None]:
    root = _repo_path(CURRENT_WORK_OPERATION_ROOT)
    try:
        path = discover_latest_completed_current_work_operation_result(root)
    except FileNotFoundError:
        return None, None, "NO_CURRENT_WORK_OPERATION_RESULT"
    except CurrentStateReadoutError as exc:
        if (
            BLOCK_REASONS["MULTIPLE_CURRENT_WORK_OPERATION_RESULTS_CONFLICT_UNRESOLVED"]
            in str(exc)
        ):
            return None, None, "MULTIPLE_CURRENT_WORK_OPERATION_RESULTS_CONFLICT_UNRESOLVED"
        raise

    try:
        return _load_current_work_operation_from_path(path), path, None
    except (FileNotFoundError, OSError):
        return None, path, "CURRENT_WORK_OPERATION_UNREADABLE"


def _load_effective_readout_artifacts(
    current_work_operation: Mapping[str, Any],
) -> dict[str, Any]:
    inputs = current_work_operation.get("effective_inputs", {})
    if not _is_mapping(inputs):
        raise CurrentStateReadoutError("Effective inputs section must be an object.")

    paths: dict[str, Path] = {}
    for key in PATH_INPUT_KEYS:
        value = inputs.get(key)
        if not isinstance(value, str) or not value:
            raise FileNotFoundError(f"Missing effective readout artifact path: {key}")
        paths[key] = _repo_path(value)

    try:
        authority = _read_json_file(
            paths["effective_authority_artifact_path"],
            "Effective authority artifact",
        )
        family = _read_json_file(
            paths["effective_family_packet_path"],
            "Effective family packet",
        )
        status = _read_json_file(
            paths["effective_status_packet_path"],
            "Effective preserved-run status packet",
        )
        governing = _read_json_file(
            paths["effective_current_governing_packet_path"],
            "Effective current-governing packet",
        )
    except (FileNotFoundError, OSError):
        raise
    except CurrentStateReadoutError:
        raise

    try:
        authority_summary = build_execution_authority_summary(authority)
        family_summary = build_run_family_summary(family)
        status_summary = build_preserved_run_status_summary(status)
        governing_summary = build_current_governing_summary(governing)
    except Exception as exc:  # noqa: BLE001 - normalize malformed dependency shape.
        raise CurrentStateReadoutError(
            "Effective readout artifacts are malformed or incoherent."
        ) from exc

    return {
        "paths": paths,
        "authority": authority,
        "family": family,
        "status": status,
        "governing": governing,
        "authority_summary": authority_summary,
        "family_summary": family_summary,
        "status_summary": status_summary,
        "governing_summary": governing_summary,
    }


def _canonical_core_values(effective_artifacts: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "authority": effective_artifacts["authority"]
        .get("canonical_execution_line", {})
        .get("core_execution_file"),
        "family": effective_artifacts["family"]
        .get("canonical_execution_line", {})
        .get("core_execution_file"),
        "status": effective_artifacts["status"]
        .get("canonical_execution_line", {})
        .get("core_execution_file"),
        "governing": effective_artifacts["governing"]
        .get("canonical_execution_line", {})
        .get("core_execution_file"),
    }


def _source_values(effective_artifacts: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "authority": effective_artifacts["authority_summary"].get(
            "selected_source_run_directory_path"
        ),
        "family": effective_artifacts["family_summary"].get(
            "current_authority_source_run_path"
        ),
        "status": effective_artifacts["status_summary"].get(
            "selected_current_authority_source_run_path"
        ),
        "governing": effective_artifacts["governing_summary"].get(
            "current_governing_source_run_path"
        ),
    }


def _ingress_values(effective_artifacts: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "authority": effective_artifacts["authority_summary"].get(
            "selected_ingress_run_directory_path"
        ),
        "family": effective_artifacts["family_summary"].get(
            "current_authority_ingress_run_path"
        ),
        "governing": effective_artifacts["governing_summary"].get(
            "current_governing_ingress_run_path"
        ),
    }


def _same_present_values(values: Mapping[str, Any]) -> bool:
    present = [value for value in values.values() if value not in (None, "")]
    return bool(present) and len(set(present)) == 1


def _all_false(non_claims: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return all(non_claims.get(key) is False for key in keys)


def _input_paths_correspond(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
) -> bool:
    inputs = current_work_operation.get("effective_inputs", {})
    if not _is_mapping(inputs):
        return False
    for key, loaded_path in effective_artifacts["paths"].items():
        if str(_repo_path(inputs.get(key, ""))) != str(loaded_path):
            return False
    return True


def _work_output_paths_correspond(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
) -> bool:
    work_output = current_work_operation.get("work_output", {})
    if not _is_mapping(work_output):
        return False

    for input_key, output_key in WORK_OUTPUT_PATH_KEYS.items():
        expected = effective_artifacts["paths"][input_key]
        actual = work_output.get(output_key)
        if not isinstance(actual, str) or str(_repo_path(actual)) != str(expected):
            return False
    return True


def _prior_family_preserved(current_work_operation: Mapping[str, Any]) -> bool:
    summary = current_work_operation.get("work_summary", {})
    output = current_work_operation.get("work_output", {})
    values = []
    if _is_mapping(summary):
        values.append(summary.get("prior_family_remained_preserved"))
    if _is_mapping(output):
        values.append(output.get("prior_family_remained_preserved"))
    explicit = [value for value in values if value is not None]
    return not explicit or any(value is True for value in explicit)


def _stale_prior_family_fallback_attempted(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
) -> bool:
    if not _input_paths_correspond(current_work_operation, effective_artifacts):
        return True
    if not _work_output_paths_correspond(current_work_operation, effective_artifacts):
        return True
    return False


def _readout_basis(current_work_operation: Mapping[str, Any]) -> Any:
    output = current_work_operation.get("work_output", {})
    summary = current_work_operation.get("work_summary", {})
    if _is_mapping(output) and output.get("current_work_basis") is not None:
        return output.get("current_work_basis")
    if _is_mapping(summary) and summary.get("current_work_basis") is not None:
        return summary.get("current_work_basis")
    return "completed_current_work_operation"


def _readout_checks(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
    operation_path: Path | str | None,
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    canonical_values = _canonical_core_values(effective_artifacts)
    source_values = _source_values(effective_artifacts)
    ingress_values = _ingress_values(effective_artifacts)

    readout_refs_correspond = _input_paths_correspond(
        current_work_operation, effective_artifacts
    ) and _work_output_paths_correspond(current_work_operation, effective_artifacts)

    return [
        _check(
            "current_work_operation_result_readable",
            True,
            "readable current-work-operation result",
            str(operation_path) if operation_path is not None else "provided mapping",
        ),
        _check(
            "current_work_operation_outcome_completed",
            current_work_operation.get("outcome") == CURRENT_WORK_OPERATION_COMPLETED,
            CURRENT_WORK_OPERATION_COMPLETED,
            current_work_operation.get("outcome"),
            "CURRENT_WORK_OPERATION_NOT_COMPLETED",
        ),
        _check(
            "effective_authority_artifact_readable_and_coherent",
            True,
            "readable coherent authority artifact",
            effective_artifacts["authority_summary"].get("resolution_id"),
        ),
        _check(
            "effective_family_packet_readable_and_coherent",
            True,
            "readable coherent family packet",
            effective_artifacts["family_summary"].get("family_packet_id"),
        ),
        _check(
            "effective_status_packet_readable_and_coherent",
            True,
            "readable coherent status packet",
            effective_artifacts["status_summary"].get("status_packet_id"),
        ),
        _check(
            "effective_current_governing_packet_readable_and_coherent",
            True,
            "readable coherent current-governing packet",
            effective_artifacts["governing_summary"].get("current_governing_packet_id"),
        ),
        _check(
            "effective_readout_inputs_correspond_to_current_work_operation_result",
            readout_refs_correspond,
            "effective inputs and work output paths match loaded artifacts",
            {
                "effective_inputs_match_loaded_paths": _input_paths_correspond(
                    current_work_operation, effective_artifacts
                ),
                "work_output_match_loaded_paths": _work_output_paths_correspond(
                    current_work_operation, effective_artifacts
                ),
            },
            "EFFECTIVE_READOUT_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
        ),
        _check(
            "canonical_core_execution_file_matches",
            all(value == CANONICAL_CORE_EXECUTION_FILE for value in canonical_values.values()),
            CANONICAL_CORE_EXECUTION_FILE,
            canonical_values,
            "CANONICAL_EXECUTION_LINE_MISMATCH",
        ),
        _check(
            "current_governing_source_run_matches_where_exposed",
            _same_present_values(source_values),
            "same source run where exposed",
            source_values,
            "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "current_governing_ingress_run_matches_where_exposed",
            _same_present_values(ingress_values),
            "same ingress run where exposed",
            ingress_values,
            "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "replay_shortcut_not_claimed",
            non_claims.get("replayed_into_live_host") is False,
            False,
            non_claims.get("replayed_into_live_host"),
            "REPLAY_SHORTCUT_REFUSED",
        ),
        _check(
            "merge_shortcut_not_claimed",
            non_claims.get("merged_into_local_state") is False,
            False,
            non_claims.get("merged_into_local_state"),
            "MERGE_SHORTCUT_REFUSED",
        ),
        _check(
            "continuity_completion_not_claimed",
            non_claims.get("continuity_completed") is False,
            False,
            non_claims.get("continuity_completed"),
            "CONTINUITY_COMPLETION_SHORTCUT_REFUSED",
        ),
        _check(
            "standing_upgrade_not_claimed",
            non_claims.get("standing_upgraded") is False,
            False,
            non_claims.get("standing_upgraded"),
            "SILENT_STANDING_UPGRADE_REFUSED",
        ),
        _check(
            "bounded_non_claims_remain_false",
            _all_false(non_claims, tuple(NON_CLAIM_DEFAULTS.keys())),
            "all bounded non-claims false",
            non_claims,
            "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "prior_family_preservation_visible_where_exposed",
            _prior_family_preserved(current_work_operation),
            "prior family remains preserved where exposed",
            current_work_operation.get("work_summary", {}).get(
                "prior_family_remained_preserved"
            )
            if _is_mapping(current_work_operation.get("work_summary"))
            else None,
            "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "uses_completed_current_work_operation_explicitly",
            True,
            "explicit completed current-work-operation input",
            str(operation_path) if operation_path is not None else "provided mapping",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            not _stale_prior_family_fallback_attempted(
                current_work_operation, effective_artifacts
            ),
            "no stale prior-family fallback",
            {
                "fallback_attempted": _stale_prior_family_fallback_attempted(
                    current_work_operation, effective_artifacts
                )
            },
            "STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
    ]


def _readout_output(
    current_work_operation: Mapping[str, Any],
    effective_artifacts: Mapping[str, Any],
) -> dict[str, Any]:
    work_output = current_work_operation.get("work_output", {})
    if not _is_mapping(work_output):
        work_output = {}

    governing_summary = effective_artifacts["governing_summary"]
    family_summary = effective_artifacts["family_summary"]
    authority_summary = effective_artifacts["authority_summary"]

    return {
        "current_governing_source_run_path": governing_summary.get(
            "current_governing_source_run_path"
        ),
        "current_governing_ingress_run_path": governing_summary.get(
            "current_governing_ingress_run_path"
        ),
        "current_authority_artifact_path": str(
            effective_artifacts["paths"]["effective_authority_artifact_path"]
        ),
        "current_family_packet_path": str(
            effective_artifacts["paths"]["effective_family_packet_path"]
        ),
        "current_status_packet_path": str(
            effective_artifacts["paths"]["effective_status_packet_path"]
        ),
        "current_governing_packet_path": str(
            effective_artifacts["paths"]["effective_current_governing_packet_path"]
        ),
        "preserved_run_count": family_summary.get("preserved_run_count")
        or work_output.get("preserved_run_count"),
        "current_authority_run_count": authority_summary.get(
            "current_authority_run_count"
        )
        or work_output.get("current_authority_run_count"),
        "preserved_eligible_non_authority_count": family_summary.get(
            "preserved_eligible_non_authority_count"
        )
        or work_output.get("preserved_eligible_non_authority_count"),
        "preserved_ineligible_count": family_summary.get("preserved_ineligible_count")
        or work_output.get("preserved_ineligible_count"),
        "current_authority_candidate_run_count": authority_summary.get(
            "candidate_run_count"
        )
        or work_output.get("current_authority_candidate_run_count"),
        "current_work_basis": _readout_basis(current_work_operation),
        "readout_basis": "completed_current_work_operation",
    }


def _readout_summary(
    current_work_operation: Mapping[str, Any],
    output: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "effective_current_governing_source_run_path": output.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": output.get(
            "current_governing_ingress_run_path"
        ),
        "preserved_run_count": output.get("preserved_run_count"),
        "current_authority_run_count": output.get("current_authority_run_count"),
        "readout_basis": output.get("readout_basis"),
        "current_work_basis": output.get("current_work_basis"),
        "selected_current_work_operation_id": current_work_operation.get(
            "work_operation_metadata", {}
        ).get("work_result_id"),
    }


def resolve_current_state_readout(
    current_work_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one current-state readout from a completed work operation."""

    operation_path: Path | None = None

    if current_work_operation is None:
        selected, operation_path, block_code = _select_default_current_work_operation()
        if block_code is not None:
            return _blocked_result(
                current_work_operation=selected,
                operation_path=operation_path,
                block_code=block_code,
                checks=[
                    _check(
                        "completed_current_work_operation_available",
                        False,
                        "one completed current-work-operation result",
                        block_code,
                        block_code,
                    )
                ],
            )
        current_work_operation = selected

    if not _is_mapping(current_work_operation):
        raise CurrentStateReadoutError(
            "Current-state readout requires a current-work-operation mapping."
        )

    _validate_current_work_operation_result(current_work_operation)

    if current_work_operation.get("outcome") != CURRENT_WORK_OPERATION_COMPLETED:
        return _blocked_result(
            current_work_operation=current_work_operation,
            operation_path=operation_path,
            block_code="CURRENT_WORK_OPERATION_NOT_COMPLETED",
            checks=[
                _check(
                    "current_work_operation_outcome_completed",
                    False,
                    CURRENT_WORK_OPERATION_COMPLETED,
                    current_work_operation.get("outcome"),
                    "CURRENT_WORK_OPERATION_NOT_COMPLETED",
                )
            ],
        )

    try:
        effective_artifacts = _load_effective_readout_artifacts(current_work_operation)
    except (FileNotFoundError, OSError):
        return _blocked_result(
            current_work_operation=current_work_operation,
            operation_path=operation_path,
            block_code="EFFECTIVE_READOUT_ARTIFACT_UNREADABLE",
            checks=[
                _check(
                    "effective_readout_artifacts_readable",
                    False,
                    "all effective readout artifacts readable",
                    "missing or unreadable artifact",
                    "EFFECTIVE_READOUT_ARTIFACT_UNREADABLE",
                )
            ],
        )

    combined_non_claims = _combined_non_claims(current_work_operation, effective_artifacts)
    checks = _readout_checks(
        current_work_operation,
        effective_artifacts,
        operation_path,
        combined_non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        block_code = str(
            failed.get("block_code") or "EFFECTIVE_READOUT_INPUT_NOT_INTERNALLY_COHERENT"
        )
        return _blocked_result(
            current_work_operation=current_work_operation,
            operation_path=operation_path,
            block_code=block_code,
            block_reason=BLOCK_REASONS.get(block_code),
            checks=checks,
            non_claims_override=combined_non_claims,
        )

    output = _readout_output(current_work_operation, effective_artifacts)
    return _result(
        current_work_operation=current_work_operation,
        operation_path=operation_path,
        outcome=OUTCOME_EMITTED,
        checks=checks,
        block_code=None,
        block_reason=None,
        readout_output=output,
        readout_summary=_readout_summary(current_work_operation, output),
        non_claims=combined_non_claims,
    )


def resolve_current_state_readout_from_path(path: Path | str) -> dict[str, Any]:
    """Read one current-work-operation result artifact and resolve its readout."""

    resolved_path = _repo_path(path)
    try:
        current_work_operation = _load_current_work_operation_from_path(resolved_path)
    except (FileNotFoundError, OSError):
        return _blocked_result(
            current_work_operation=None,
            operation_path=resolved_path,
            block_code="CURRENT_WORK_OPERATION_UNREADABLE",
            checks=[
                _check(
                    "current_work_operation_result_readable",
                    False,
                    "readable current-work-operation result",
                    str(resolved_path),
                    "CURRENT_WORK_OPERATION_UNREADABLE",
                )
            ],
        )

    result = resolve_current_state_readout(current_work_operation)
    result["selected_current_work_operation"][
        "current_work_operation_result_path"
    ] = str(resolved_path)
    return result


def build_current_state_readout_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a compact inspection summary for one readout result."""

    if not _is_mapping(result):
        raise CurrentStateReadoutError("Current-state readout result must be a mapping.")

    metadata = result.get("readout_metadata", {})
    selected = result.get("selected_current_work_operation", {})
    inputs = result.get("effective_readout_inputs", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateReadoutError("Current-state readout checks must be a list.")

    passed, failed = _count_checks(checks)
    if not _is_mapping(inputs):
        inputs = {}
    if not _is_mapping(block):
        block = {}
    if not _is_mapping(selected):
        selected = {}
    if not _is_mapping(metadata):
        metadata = {}
    if not _is_mapping(non_claims):
        non_claims = {}

    return {
        "readout_result_id": metadata.get("readout_result_id"),
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "selected_current_work_operation_id": selected.get(
            "current_work_operation_result_id"
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
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": _non_claims_from(non_claims),
    }


def _safe_default_output_path(root: Path) -> Path:
    root.mkdir(parents=True, exist_ok=True)
    candidate = root / f"{DEFAULT_READOUT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate

    for index in range(1, 1000):
        candidate = root / f"{DEFAULT_READOUT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate

    raise CurrentStateReadoutError(
        f"No bounded non-colliding current-state readout output path is available under {root}."
    )


def write_current_state_readout_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-state readout result artifact."""

    if not _is_mapping(result):
        raise CurrentStateReadoutError("Current-state readout result must be a mapping.")

    if output_path is None:
        resolved_path = _safe_default_output_path(_repo_path(CURRENT_STATE_READOUT_ROOT))
    else:
        resolved_path = _repo_path(output_path)
        resolved_path.parent.mkdir(parents=True, exist_ok=True)
        if resolved_path.exists():
            raise FileExistsError(f"Refusing to overwrite existing file: {resolved_path}")

    with resolved_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")

    return resolved_path
