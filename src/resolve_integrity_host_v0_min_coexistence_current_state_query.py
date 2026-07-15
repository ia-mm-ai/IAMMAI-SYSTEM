"""Resolve one bounded current-state query for the v0-min coexistence line.

This module consumes an answered current-state result and one bounded query
request, verifies the effective artifacts named by that result, and emits one
additive query result surface. It does not replay, merge, mutate prior
artifacts, or claim continuity completion.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence

from resolve_integrity_host_v0_min_coexistence_current_state_answer_surface import (
    CANONICAL_CORE_EXECUTION_FILE,
    CURRENT_STATE_ANSWER_SURFACE_ROOT,
    NON_CLAIM_DEFAULTS as ANSWER_READ_NON_CLAIM_DEFAULTS,
    OUTCOME_ANSWERED as CURRENT_STATE_ANSWER_READ_ANSWERED,
    build_current_governing_summary,
    build_current_state_answer_read_summary,
    build_execution_authority_summary,
    build_preserved_run_status_summary,
    build_run_family_summary,
)


class CurrentStateQueryError(RuntimeError):
    """Raised when query inputs are malformed or impossible to use."""


CURRENT_STATE_QUERY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_query"
)

QUERY_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_QUERY_RESULT"
)
QUERY_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_integrity_host_v0_min_coexistence_current_state_query"

OUTCOME_ANSWERED_QUERY = "ANSWERED_QUERY"
OUTCOME_BLOCKED = "BLOCKED"

DEFAULT_QUERY_RESULT_STEM = "current_state_query_result"

PATH_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
)

QUERY_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

ANSWER_READ_OUTPUT_PATH_KEYS = {
    "effective_authority_artifact_path": "current_authority_artifact_path",
    "effective_family_packet_path": "current_family_packet_path",
    "effective_status_packet_path": "current_status_packet_path",
    "effective_current_governing_packet_path": "current_governing_packet_path",
}

ALLOWED_QUERY_TARGETS = {
    "answered_current_state_result",
    "current_state_answer_read_result",
    "answer_read_output",
    "answer_read_summary",
    "effective_answer_read_inputs",
    "non_claims",
}

ANSWER_READ_OUTPUT_FIELDS = {
    "current_governing_source_run_path",
    "current_governing_ingress_run_path",
    "current_authority_artifact_path",
    "current_family_packet_path",
    "current_status_packet_path",
    "current_governing_packet_path",
    "preserved_run_count",
    "current_authority_run_count",
    "preserved_eligible_non_authority_count",
    "preserved_ineligible_count",
    "current_authority_candidate_run_count",
    "current_work_basis",
    "readout_basis",
    "handoff_basis",
    "export_basis",
    "delivery_basis",
    "application_basis",
    "answer_read_basis",
}

ANSWER_READ_SUMMARY_FIELDS = {
    "selected_current_state_application_id",
    "effective_current_governing_source_run_path",
    "effective_current_governing_ingress_run_path",
    "preserved_run_count",
    "current_authority_run_count",
    "application_basis",
    "answer_read_basis",
    "passed_check_count",
    "failed_check_count",
}

EFFECTIVE_INPUT_FIELDS = set(QUERY_INPUT_KEYS)

BLOCK_REASONS = {
    "NO_CURRENT_STATE_ANSWER_READ_RESULT": (
        "No answered current-state result is available for query answering."
    ),
    "CURRENT_STATE_ANSWER_READ_UNREADABLE": (
        "The selected current-state answer/read result could not be read."
    ),
    "CURRENT_STATE_ANSWER_READ_NOT_ANSWERED": (
        "The selected current-state answer/read result is not answered."
    ),
    "EFFECTIVE_QUERY_ARTIFACT_UNREADABLE": (
        "One or more effective query artifacts are unreadable."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "Effective query artifacts do not preserve the canonical execution line."
    ),
    "EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT": (
        "Effective query inputs are not internally coherent."
    ),
    "EFFECTIVE_QUERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "Effective query inputs do not correspond to the selected answer/read "
        "result."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based query answering is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based query answering is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity completion by query answering is refused."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Silent standing upgrade by query answering is refused."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Silent fallback to stale prior-family artifacts is refused."
    ),
    "QUERY_REQUEST_OUT_OF_SCOPE": (
        "The query request exceeds the bounded answerable current-state surface."
    ),
    "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple answered current-state results conflict without an explicit "
        "bounded selection surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **ANSWER_READ_NON_CLAIM_DEFAULTS,
    "final_current_state_query_completed": False,
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
        raise CurrentStateQueryError(f"{context} is unreadable: {resolved}") from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateQueryError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(payload, dict):
        raise CurrentStateQueryError(f"{context} must be a JSON object: {resolved}")
    return payload


def read_query_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded query request JSON object."""

    request = _read_json_file(path, "current-state query request")
    _validate_query_request_shape(request)
    return request


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
        if check.get("passed") is not True:
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
        raise CurrentStateQueryError(f"{context} non_claims must be an object")
    result: dict[str, bool] = {}
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateQueryError(f"{context} non_claims keys must be strings")
        if not isinstance(value, bool):
            raise CurrentStateQueryError(
                f"{context} non_claims value for {key!r} must be boolean"
            )
        result[key] = value
    return result


def _merge_non_claims(*surfaces: Mapping[str, bool]) -> dict[str, bool]:
    merged = dict(NON_CLAIM_DEFAULTS)
    for surface in surfaces:
        for key, value in surface.items():
            if key in merged:
                merged[key] = bool(merged[key] or value)
            else:
                merged[key] = value
    for key in NON_CLAIM_DEFAULTS:
        merged.setdefault(key, False)
    return merged


def _combined_non_claims(
    answer_read: Mapping[str, Any],
    effective_artifacts: Mapping[str, Mapping[str, Any]] | None = None,
) -> dict[str, bool]:
    surfaces: list[Mapping[str, bool]] = [
        _non_claims_from(answer_read, "current-state answer/read result")
    ]
    if effective_artifacts is not None:
        for name, artifact in effective_artifacts.items():
            if name.startswith("_"):
                continue
            surfaces.append(_non_claims_from(artifact, f"effective {name} artifact"))
    return _merge_non_claims(*surfaces)


def _validate_current_state_answer_read_result(
    answer_read: Mapping[str, Any],
) -> None:
    if not _is_mapping(answer_read.get("answer_read_metadata")):
        raise CurrentStateQueryError("current-state answer/read metadata is missing")
    if not _is_mapping(answer_read.get("selected_current_state_application")):
        raise CurrentStateQueryError(
            "selected current-state application section is missing"
        )
    if not _is_mapping(answer_read.get("effective_answer_read_inputs")):
        raise CurrentStateQueryError("effective answer/read inputs are missing")
    if "outcome" not in answer_read:
        raise CurrentStateQueryError("current-state answer/read outcome is missing")
    if not _is_mapping(answer_read.get("block")):
        raise CurrentStateQueryError(
            "current-state answer/read block section is missing"
        )
    if not isinstance(answer_read.get("checks"), list):
        raise CurrentStateQueryError(
            "current-state answer/read checks must be a list"
        )
    if not _is_mapping(answer_read.get("non_claims")):
        raise CurrentStateQueryError(
            "current-state answer/read non_claims are missing"
        )

    metadata = answer_read["answer_read_metadata"]
    if not isinstance(metadata.get("answer_read_result_id"), str) or not metadata.get(
        "answer_read_result_id"
    ):
        raise CurrentStateQueryError(
            "current-state answer/read result id is missing"
        )

    if answer_read.get("outcome") == CURRENT_STATE_ANSWER_READ_ANSWERED:
        if not _is_mapping(answer_read.get("answer_read_output")):
            raise CurrentStateQueryError(
                "answered current-state result must include answer_read_output"
            )
        inputs = answer_read["effective_answer_read_inputs"]
        for key in PATH_INPUT_KEYS:
            if not isinstance(inputs.get(key), str) or not inputs.get(key):
                raise CurrentStateQueryError(
                    f"answered current-state result is missing {key}"
                )

    try:
        build_current_state_answer_read_summary(answer_read)
    except Exception as exc:
        raise CurrentStateQueryError(
            "current-state answer/read summary could not be built"
        ) from exc


def _looks_like_current_state_answer_read_result(payload: Mapping[str, Any]) -> bool:
    return (
        _is_mapping(payload.get("answer_read_metadata"))
        and "answer_read_result_id" in payload["answer_read_metadata"]
        and "effective_answer_read_inputs" in payload
        and "outcome" in payload
    )


def _validate_query_request_shape(query_request: Mapping[str, Any]) -> None:
    if not isinstance(query_request, Mapping):
        raise CurrentStateQueryError("query_request must be a mapping")
    for key in (
        "query_request_id",
        "query_target",
        "requested_fields",
        "query_basis",
    ):
        if key not in query_request:
            raise CurrentStateQueryError(f"query request is missing {key}")
    for key in ("query_request_id", "query_target", "query_basis"):
        if not isinstance(query_request.get(key), str) or not query_request.get(
            key
        ).strip():
            raise CurrentStateQueryError(f"query request {key} must be non-empty")
    requested_fields = query_request.get("requested_fields")
    if not isinstance(requested_fields, list) or not requested_fields:
        raise CurrentStateQueryError(
            "query request requested_fields must be a non-empty list"
        )
    for field in requested_fields:
        if not isinstance(field, str) or not field.strip():
            raise CurrentStateQueryError(
                "query request requested_fields must contain non-empty strings"
            )


def _normal_query_request(query_request: Mapping[str, Any]) -> dict[str, Any]:
    _validate_query_request_shape(query_request)
    return {
        "query_request_id": str(query_request["query_request_id"]).strip(),
        "query_target": str(query_request["query_target"]).strip(),
        "requested_fields": [
            str(field).strip() for field in query_request["requested_fields"]
        ],
        "query_basis": str(query_request["query_basis"]).strip(),
    }


def _selected_current_state_answer_read(
    answer_read: Mapping[str, Any] | None,
    answer_read_path: Path | str | None,
) -> dict[str, Any]:
    if answer_read is None:
        return {
            "current_state_answer_read_result_path": (
                str(_repo_path(answer_read_path))
                if answer_read_path is not None
                else None
            ),
            "current_state_answer_read_result_id": None,
            "outcome": None,
            "selected_current_state_application_id": None,
        }

    metadata = answer_read.get("answer_read_metadata", {})
    selected_application = answer_read.get("selected_current_state_application", {})
    return {
        "current_state_answer_read_result_path": (
            str(_repo_path(answer_read_path))
            if answer_read_path is not None
            else None
        ),
        "current_state_answer_read_result_id": metadata.get("answer_read_result_id"),
        "outcome": answer_read.get("outcome"),
        "selected_current_state_application_id": selected_application.get(
            "current_state_application_result_id"
        )
        if isinstance(selected_application, Mapping)
        else None,
    }


def _effective_query_inputs_from(
    answer_read: Mapping[str, Any] | None,
) -> dict[str, Any]:
    inputs = (
        answer_read.get("effective_answer_read_inputs", {})
        if answer_read is not None
        else {}
    )
    if not isinstance(inputs, Mapping):
        inputs = {}
    return {key: inputs.get(key) for key in QUERY_INPUT_KEYS}


def _query_result_id(
    answer_read: Mapping[str, Any] | None,
    query_request: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    if answer_read is not None and _is_mapping(answer_read.get("answer_read_metadata")):
        base = answer_read["answer_read_metadata"].get("answer_read_result_id")
    else:
        base = None
    if not isinstance(base, str) or not base:
        base = "no_current_state_answer_read_result"
    request_id = None
    if isinstance(query_request, Mapping):
        request_id = query_request.get("query_request_id")
    if not isinstance(request_id, str) or not request_id:
        request_id = "query_request"
    suffix = (
        "current_state_query_answered"
        if outcome == OUTCOME_ANSWERED_QUERY
        else "current_state_query_blocked"
    )
    return f"{base}__{request_id}__{suffix}"


def _blocked_summary(
    answer_read: Mapping[str, Any] | None,
    query_request: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    inputs = _effective_query_inputs_from(answer_read)
    passed, failed = _count_checks(checks)
    requested_fields = (
        query_request.get("requested_fields") if isinstance(query_request, Mapping) else []
    )
    return {
        "selected_current_state_answer_read_id": (
            answer_read.get("answer_read_metadata", {}).get("answer_read_result_id")
            if answer_read is not None
            and _is_mapping(answer_read.get("answer_read_metadata"))
            else None
        ),
        "selected_query_target": query_request.get("query_target")
        if isinstance(query_request, Mapping)
        else None,
        "answered_field_count": 0,
        "answered_field_names": [],
        "requested_field_names": list(requested_fields)
        if isinstance(requested_fields, list)
        else [],
        "effective_current_governing_source_run_path": inputs.get(
            "effective_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": inputs.get(
            "effective_ingress_run_path"
        ),
        "query_basis": query_request.get("query_basis")
        if isinstance(query_request, Mapping)
        else None,
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def _result(
    *,
    answer_read: Mapping[str, Any] | None,
    answer_read_path: Path | str | None,
    query_request: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    query_answer: Mapping[str, Any] | None,
    query_summary: Mapping[str, Any] | None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    result_non_claims = dict(non_claims or NON_CLAIM_DEFAULTS)
    for key in NON_CLAIM_DEFAULTS:
        result_non_claims.setdefault(key, False)

    selected = _selected_current_state_answer_read(answer_read, answer_read_path)
    effective_inputs = _effective_query_inputs_from(answer_read)
    check_list = [dict(check) for check in checks]
    request = dict(query_request) if isinstance(query_request, Mapping) else None
    summary = dict(
        query_summary or _blocked_summary(answer_read, request, check_list)
    )

    return {
        "query_metadata": {
            "query_result_id": _query_result_id(answer_read, request, outcome),
            "query_result_type": QUERY_RESULT_TYPE,
            "query_result_version": QUERY_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_answer_read": selected,
        "query_request": request,
        "effective_query_inputs": effective_inputs,
        "checks": check_list,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "query_answer": dict(query_answer) if query_answer is not None else None,
        "query_summary": summary,
        "non_claims": result_non_claims,
    }


def _blocked_result(
    *,
    answer_read: Mapping[str, Any] | None,
    answer_read_path: Path | str | None,
    query_request: Mapping[str, Any] | None,
    block_code: str,
    block_reason: str | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
    non_claims: Mapping[str, bool] | None = None,
) -> dict[str, Any]:
    check_list = list(checks or [])
    return _result(
        answer_read=answer_read,
        answer_read_path=answer_read_path,
        query_request=query_request,
        checks=check_list,
        outcome=OUTCOME_BLOCKED,
        block_code=block_code,
        block_reason=block_reason or BLOCK_REASONS.get(block_code, block_code),
        query_answer=None,
        query_summary=_blocked_summary(answer_read, query_request, check_list),
        non_claims=non_claims or NON_CLAIM_DEFAULTS,
    )


def _candidate_json_files(root: Path | str) -> list[Path]:
    resolved_root = _repo_path(root)
    if not resolved_root.exists():
        return []
    if not resolved_root.is_dir():
        raise CurrentStateQueryError(
            f"current-state answer/read root is not a directory: {resolved_root}"
        )
    try:
        return sorted(path for path in resolved_root.glob("*.json") if path.is_file())
    except OSError as exc:
        raise CurrentStateQueryError(
            f"current-state answer/read root is unreadable: {resolved_root}"
        ) from exc


def _load_current_state_answer_read_from_path(path: Path | str) -> dict[str, Any]:
    answer_read = _read_json_file(path, "current-state answer/read result")
    _validate_current_state_answer_read_result(answer_read)
    return answer_read


def discover_latest_answered_current_state_answer_read_result(
    root: Path | str = CURRENT_STATE_ANSWER_SURFACE_ROOT,
) -> tuple[dict[str, Any], Path]:
    """Return the lexically latest answered result when unambiguous."""

    candidates = _candidate_json_files(root)
    if not candidates:
        raise FileNotFoundError("no current-state answer/read result artifacts found")

    answered: list[tuple[dict[str, Any], Path]] = []
    for path in candidates:
        payload = _read_json_file(path, "current-state answer/read result")
        if not _looks_like_current_state_answer_read_result(payload):
            continue
        _validate_current_state_answer_read_result(payload)
        if payload.get("outcome") == CURRENT_STATE_ANSWER_READ_ANSWERED:
            answered.append((payload, path))

    if not answered:
        raise FileNotFoundError("no answered current-state result artifacts found")

    distinct_ids = {
        payload["answer_read_metadata"].get("answer_read_result_id")
        for payload, _path in answered
    }
    if len(distinct_ids) > 1:
        raise CurrentStateQueryError(
            BLOCK_REASONS[
                "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED"
            ]
        )
    return answered[-1]


discover_latest_current_state_answer_read_result = (
    discover_latest_answered_current_state_answer_read_result
)


def _select_default_current_state_answer_read() -> tuple[
    dict[str, Any] | None,
    Path | None,
    str | None,
]:
    try:
        answer_read, path = discover_latest_answered_current_state_answer_read_result()
        return answer_read, path, None
    except FileNotFoundError:
        return None, None, "NO_CURRENT_STATE_ANSWER_READ_RESULT"
    except CurrentStateQueryError as exc:
        if (
            BLOCK_REASONS[
                "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED"
            ]
            in str(exc)
        ):
            return (
                None,
                None,
                "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED",
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
        raise CurrentStateQueryError(f"{context} is malformed") from exc
    if not isinstance(summary, dict):
        raise CurrentStateQueryError(f"{context} summary must be an object")
    return summary


def _load_effective_query_artifacts(answer_read: Mapping[str, Any]) -> dict[str, Any]:
    inputs = answer_read.get("effective_answer_read_inputs")
    if not isinstance(inputs, Mapping):
        raise CurrentStateQueryError("effective answer/read inputs must be an object")

    missing = [
        key
        for key in PATH_INPUT_KEYS
        if not isinstance(inputs.get(key), str) or not inputs.get(key)
    ]
    if missing:
        raise FileNotFoundError(
            "missing effective query artifact path(s): " + ", ".join(missing)
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


def _summary_values(artifacts: Mapping[str, Any], names: Sequence[str]) -> list[Any]:
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


def _same_path(left: Any, right: Any) -> bool:
    return isinstance(left, str) and isinstance(right, str) and (
        _repo_path(left) == _repo_path(right)
    )


def _input_paths_correspond(
    answer_read: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    inputs = answer_read.get("effective_answer_read_inputs", {})
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
            if isinstance(actual, str) and actual and not _same_path(actual, selected):
                return False
    return True


def _answer_read_output_paths_correspond(
    answer_read: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    output = answer_read.get("answer_read_output", {})
    inputs = answer_read.get("effective_answer_read_inputs", {})
    if not isinstance(output, Mapping) or not isinstance(inputs, Mapping):
        return False

    for input_key, output_key in ANSWER_READ_OUTPUT_PATH_KEYS.items():
        input_value = inputs.get(input_key)
        output_value = output.get(output_key)
        if isinstance(output_value, str) and output_value:
            if not _same_path(output_value, input_value):
                return False

    source_input = inputs.get("effective_source_run_path")
    source_output = output.get("current_governing_source_run_path")
    if isinstance(source_output, str) and source_output:
        if not _same_path(source_output, source_input):
            return False

    ingress_input = inputs.get("effective_ingress_run_path")
    ingress_output = output.get("current_governing_ingress_run_path")
    if isinstance(ingress_output, str) and ingress_output:
        if not _same_path(ingress_output, ingress_input):
            return False

    return _input_paths_correspond(answer_read, artifacts)


def _prior_family_preserved(answer_read: Mapping[str, Any]) -> bool:
    for section_name in ("answer_read_summary", "answer_read_output"):
        section = answer_read.get(section_name)
        if isinstance(section, Mapping):
            value = section.get("prior_family_remained_preserved")
            if value is False:
                return False
    return True


def _stale_prior_family_fallback_attempted(
    answer_read: Mapping[str, Any],
    artifacts: Mapping[str, Any],
) -> bool:
    return not _answer_read_output_paths_correspond(answer_read, artifacts)


def _answer_read_basis(answer_read: Mapping[str, Any]) -> Any:
    output = answer_read.get("answer_read_output", {})
    summary = answer_read.get("answer_read_summary", {})
    if isinstance(output, Mapping) and output.get("answer_read_basis") is not None:
        return output.get("answer_read_basis")
    if isinstance(summary, Mapping) and summary.get("answer_read_basis") is not None:
        return summary.get("answer_read_basis")
    return "answered_current_state_result"


def _answerable_field_sources(
    answer_read: Mapping[str, Any],
) -> dict[str, Any]:
    output = answer_read.get("answer_read_output", {})
    if not isinstance(output, Mapping):
        output = {}
    summary = answer_read.get("answer_read_summary", {})
    if not isinstance(summary, Mapping):
        summary = {}
    inputs = answer_read.get("effective_answer_read_inputs", {})
    if not isinstance(inputs, Mapping):
        inputs = {}
    metadata = answer_read.get("answer_read_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    selected_application = answer_read.get("selected_current_state_application", {})
    if not isinstance(selected_application, Mapping):
        selected_application = {}
    non_claims = answer_read.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    fields: dict[str, Any] = {}
    for key in ANSWER_READ_OUTPUT_FIELDS:
        fields[key] = output.get(key)
    for key in EFFECTIVE_INPUT_FIELDS:
        fields[key] = inputs.get(key)
    for key in ANSWER_READ_SUMMARY_FIELDS:
        fields[key] = summary.get(key)
    fields.update(
        {
            "answer_read_result_id": metadata.get("answer_read_result_id"),
            "current_state_answer_read_result_id": metadata.get(
                "answer_read_result_id"
            ),
            "current_state_application_result_path": selected_application.get(
                "current_state_application_result_path"
            ),
            "current_state_application_result_id": selected_application.get(
                "current_state_application_result_id"
            ),
            "selected_current_state_application_id": selected_application.get(
                "current_state_application_result_id"
            ),
            "outcome": answer_read.get("outcome"),
            "non_claims": dict(non_claims),
        }
    )
    for key in NON_CLAIM_DEFAULTS:
        if key in non_claims:
            fields[key] = non_claims.get(key)
    return fields


def _allowed_query_fields(answer_read: Mapping[str, Any]) -> set[str]:
    return set(_answerable_field_sources(answer_read))


def _query_request_within_scope(
    query_request: Mapping[str, Any],
    answer_read: Mapping[str, Any],
) -> bool:
    target = query_request.get("query_target")
    if target not in ALLOWED_QUERY_TARGETS and target not in _allowed_query_fields(
        answer_read
    ):
        return False
    requested_fields = query_request.get("requested_fields")
    if not isinstance(requested_fields, list):
        return False
    allowed = _allowed_query_fields(answer_read)
    return all(field in allowed for field in requested_fields)


def _query_checks(
    *,
    answer_read: Mapping[str, Any],
    artifacts: Mapping[str, Any],
    answer_read_path: Path | str | None,
    query_request: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> list[dict[str, Any]]:
    canonical_values = _canonical_core_values(artifacts)
    source_values = _source_values(artifacts)
    ingress_values = _ingress_values(artifacts)
    summaries = artifacts.get("_summaries", {})
    effective_inputs = answer_read.get("effective_answer_read_inputs", {})

    canonical_match = bool(canonical_values) and all(
        str(value) == CANONICAL_CORE_EXECUTION_FILE for value in canonical_values
    )
    input_correspondence = _input_paths_correspond(answer_read, artifacts)
    output_correspondence = _answer_read_output_paths_correspond(
        answer_read,
        artifacts,
    )
    query_scope = _query_request_within_scope(query_request, answer_read)

    return [
        _check(
            "current_state_answer_read_result_readable",
            True,
            expected="readable answered current-state result",
            actual=str(_repo_path(answer_read_path))
            if answer_read_path is not None
            else None,
        ),
        _check(
            "current_state_answer_read_outcome_answered",
            answer_read.get("outcome") == CURRENT_STATE_ANSWER_READ_ANSWERED,
            expected=CURRENT_STATE_ANSWER_READ_ANSWERED,
            actual=answer_read.get("outcome"),
            block_code="CURRENT_STATE_ANSWER_READ_NOT_ANSWERED",
        ),
        _check(
            "effective_execution_authority_artifact_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("authority"), Mapping),
            expected="readable coherent effective authority artifact",
            actual=effective_inputs.get("effective_authority_artifact_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_run_family_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("family"), Mapping),
            expected="readable coherent effective family packet",
            actual=effective_inputs.get("effective_family_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_preserved_run_status_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("status"), Mapping),
            expected="readable coherent effective status packet",
            actual=effective_inputs.get("effective_status_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_current_governing_packet_readable_and_coherent",
            isinstance(summaries, Mapping)
            and isinstance(summaries.get("governing"), Mapping),
            expected="readable coherent effective current-governing packet",
            actual=effective_inputs.get("effective_current_governing_packet_path")
            if isinstance(effective_inputs, Mapping)
            else None,
            block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
        ),
        _check(
            "effective_query_inputs_correspond_to_current_state_answer_read_result",
            input_correspondence and output_correspondence,
            expected="effective inputs named by current-state answer/read result",
            actual={
                "effective_input_paths_correspond": input_correspondence,
                "answer_read_output_paths_correspond": output_correspondence,
            },
            block_code="EFFECTIVE_QUERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT",
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
            block_code="EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "effective_inputs_share_current_governing_ingress_run_where_exposed",
            _same_present_values(ingress_values),
            expected="same current governing ingress run where exposed",
            actual=ingress_values,
            block_code="EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT",
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
            block_code="EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "prior_family_preservation_visible_where_exposed",
            _prior_family_preserved(answer_read),
            expected="prior family remains preserved where exposed",
            actual={
                "answer_read_summary": answer_read.get("answer_read_summary", {}),
                "answer_read_output": answer_read.get("answer_read_output", {}),
            },
            block_code="EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT",
        ),
        _check(
            "uses_answered_current_state_result_explicitly",
            True,
            expected="query selected from answered current-state result",
            actual=str(_repo_path(answer_read_path))
            if answer_read_path is not None
            else "mapping input",
        ),
        _check(
            "stale_prior_family_fallback_refused",
            not _stale_prior_family_fallback_attempted(answer_read, artifacts),
            expected="no stale prior-family fallback",
            actual={
                "fallback_attempted": _stale_prior_family_fallback_attempted(
                    answer_read,
                    artifacts,
                )
            },
            block_code="STALE_PRIOR_FAMILY_FALLBACK_REFUSED",
        ),
        _check(
            "query_request_within_bounded_answerable_surface",
            query_scope,
            expected="query target and requested fields exposed by answer/read result",
            actual={
                "query_target": query_request.get("query_target"),
                "requested_fields": query_request.get("requested_fields"),
                "allowed_targets": sorted(ALLOWED_QUERY_TARGETS),
                "allowed_field_count": len(_allowed_query_fields(answer_read)),
            },
            block_code="QUERY_REQUEST_OUT_OF_SCOPE",
        ),
    ]


def _query_answer(
    answer_read: Mapping[str, Any],
    query_request: Mapping[str, Any],
) -> dict[str, Any]:
    fields = _answerable_field_sources(answer_read)
    requested_fields = list(query_request["requested_fields"])
    answered_fields = {field: fields.get(field) for field in requested_fields}
    metadata = answer_read.get("answer_read_metadata", {})
    selected_application = answer_read.get("selected_current_state_application", {})

    return {
        "query_request_id": query_request.get("query_request_id"),
        "query_target": query_request.get("query_target"),
        "answered_from": "current_state_answer_read_result",
        "current_state_answer_read_result_id": metadata.get("answer_read_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "selected_current_state_application_id": selected_application.get(
            "current_state_application_result_id"
        )
        if isinstance(selected_application, Mapping)
        else None,
        "answered_fields": answered_fields,
        "answered_field_names": requested_fields,
        "answer_read_basis": _answer_read_basis(answer_read),
        "query_basis": query_request.get("query_basis"),
    }


def _query_summary(
    answer_read: Mapping[str, Any],
    query_request: Mapping[str, Any],
    query_answer: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    output = answer_read.get("answer_read_output", {})
    if not isinstance(output, Mapping):
        output = {}
    passed, failed = _count_checks(checks)
    answered_names = query_answer.get("answered_field_names", [])
    if not isinstance(answered_names, list):
        answered_names = []

    return {
        "selected_current_state_answer_read_id": query_answer.get(
            "current_state_answer_read_result_id"
        ),
        "selected_query_target": query_request.get("query_target"),
        "answered_field_count": len(answered_names),
        "answered_field_names": list(answered_names),
        "effective_current_governing_source_run_path": output.get(
            "current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": output.get(
            "current_governing_ingress_run_path"
        ),
        "query_basis": query_request.get("query_basis"),
        "answer_read_basis": query_answer.get("answer_read_basis"),
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def resolve_current_state_query(
    query_request: Mapping[str, Any],
    current_state_answer_read: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded query result from an answered current state."""

    request = _normal_query_request(query_request)

    if current_state_answer_read is None:
        answer_read, answer_read_path, block_code = (
            _select_default_current_state_answer_read()
        )
        if block_code is not None:
            return _blocked_result(
                answer_read=None,
                answer_read_path=None,
                query_request=request,
                block_code=block_code,
            )
    else:
        if not isinstance(current_state_answer_read, Mapping):
            raise CurrentStateQueryError("current_state_answer_read must be a mapping")
        answer_read = dict(current_state_answer_read)
        answer_read_path = None

    _validate_current_state_answer_read_result(answer_read)

    if answer_read.get("outcome") != CURRENT_STATE_ANSWER_READ_ANSWERED:
        checks = [
            _check(
                "current_state_answer_read_outcome_answered",
                False,
                expected=CURRENT_STATE_ANSWER_READ_ANSWERED,
                actual=answer_read.get("outcome"),
                block_code="CURRENT_STATE_ANSWER_READ_NOT_ANSWERED",
            )
        ]
        return _blocked_result(
            answer_read=answer_read,
            answer_read_path=answer_read_path,
            query_request=request,
            block_code="CURRENT_STATE_ANSWER_READ_NOT_ANSWERED",
            checks=checks,
            non_claims=_combined_non_claims(answer_read),
        )

    try:
        artifacts = _load_effective_query_artifacts(answer_read)
    except FileNotFoundError as exc:
        checks = [
            _check(
                "effective_query_artifacts_readable",
                False,
                expected=(
                    "effective authority, family, status, and governing artifacts "
                    "readable"
                ),
                actual=str(exc),
                block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
            )
        ]
        return _blocked_result(
            answer_read=answer_read,
            answer_read_path=answer_read_path,
            query_request=request,
            block_code="EFFECTIVE_QUERY_ARTIFACT_UNREADABLE",
            checks=checks,
            non_claims=_combined_non_claims(answer_read),
        )

    non_claims = _combined_non_claims(answer_read, artifacts)
    checks = _query_checks(
        answer_read=answer_read,
        artifacts=artifacts,
        answer_read_path=answer_read_path,
        query_request=request,
        non_claims=non_claims,
    )
    failed = _first_failed(checks)
    if failed is not None:
        block_code = str(
            failed.get("block_code") or "EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT"
        )
        return _blocked_result(
            answer_read=answer_read,
            answer_read_path=answer_read_path,
            query_request=request,
            block_code=block_code,
            block_reason=BLOCK_REASONS.get(block_code, block_code),
            checks=checks,
            non_claims=non_claims,
        )

    answer = _query_answer(answer_read, request)
    return _result(
        answer_read=answer_read,
        answer_read_path=answer_read_path,
        query_request=request,
        checks=checks,
        outcome=OUTCOME_ANSWERED_QUERY,
        block_code=None,
        block_reason=None,
        query_answer=answer,
        query_summary=_query_summary(answer_read, request, answer, checks),
        non_claims=non_claims,
    )


def resolve_current_state_query_from_path(
    path: Path | str,
    query_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one answer/read artifact and resolve one bounded query."""

    request = _normal_query_request(query_request)
    resolved_path = _repo_path(path)
    try:
        answer_read = _load_current_state_answer_read_from_path(resolved_path)
    except FileNotFoundError:
        return _blocked_result(
            answer_read=None,
            answer_read_path=resolved_path,
            query_request=request,
            block_code="CURRENT_STATE_ANSWER_READ_UNREADABLE",
        )

    result = resolve_current_state_query(request, answer_read)
    result["selected_current_state_answer_read"][
        "current_state_answer_read_result_path"
    ] = str(resolved_path)
    return result


def build_current_state_query_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Return a small inspection-friendly summary of a query result."""

    if not isinstance(result, Mapping):
        raise CurrentStateQueryError("query result must be a mapping")
    metadata = result.get("query_metadata", {})
    selected = result.get("selected_current_state_answer_read", {})
    query_request = result.get("query_request", {})
    effective = result.get("effective_query_inputs", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    query_answer = result.get("query_answer", {})
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateQueryError("query checks must be a list")
    passed, failed = _count_checks(checks)
    answered_names: list[Any] = []
    if isinstance(query_answer, Mapping):
        raw_names = query_answer.get("answered_field_names", [])
        if isinstance(raw_names, list):
            answered_names = list(raw_names)

    return {
        "query_result_id": metadata.get("query_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason")
        if isinstance(block, Mapping)
        else None,
        "selected_current_state_answer_read_id": selected.get(
            "current_state_answer_read_result_id"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_query_target": query_request.get("query_target")
        if isinstance(query_request, Mapping)
        else None,
        "answered_field_names": answered_names,
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


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = DEFAULT_QUERY_RESULT_STEM
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value)
    compact = compact.strip("._")
    return compact[:160] or DEFAULT_QUERY_RESULT_STEM


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_STATE_QUERY_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_current_state_answer_read", {})
    selected_id = None
    if isinstance(selected, Mapping):
        selected_id = selected.get("current_state_answer_read_result_id")
    stem = _safe_filename_part(selected_id)
    candidate = resolved_root / f"{stem}__{DEFAULT_QUERY_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            resolved_root
            / f"{stem}__{DEFAULT_QUERY_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentStateQueryError("no bounded current-state query filename available")


def write_current_state_query_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive current-state query result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentStateQueryError("query result must be a mapping")

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"current-state query result already exists: {target}")

    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
