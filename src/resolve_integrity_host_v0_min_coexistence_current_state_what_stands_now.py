"""Resolve one bounded "what stands now" answer for the v0-min line.

This module consumes an answered current-state result and one bounded
stand-now request, delegates the shared current-state correspondence checks to
the current-state query resolver, and emits one additive concrete question
result. It does not replay, merge, mutate prior artifacts, or claim continuity
completion.
"""

from __future__ import annotations

import json
import re
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Mapping, Sequence

import resolve_integrity_host_v0_min_coexistence_current_state_query as query_resolver


class CurrentStateWhatStandsNowError(RuntimeError):
    """Raised when stand-now inputs are malformed or impossible to use."""


CURRENT_STATE_ANSWER_SURFACE_ROOT = query_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_WHAT_STANDS_NOW_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_what_stands_now"
)

WHAT_STANDS_NOW_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_STANDS_NOW_RESULT"
)
WHAT_STANDS_NOW_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_current_state_what_stands_now"
)

OUTCOME_ANSWERED_WHAT_STANDS_NOW = "ANSWERED_WHAT_STANDS_NOW"
OUTCOME_BLOCKED = "BLOCKED"

QUERY_FAMILY = "what_stands_now"
DEFAULT_WHAT_STANDS_NOW_RESULT_STEM = "current_state_what_stands_now_result"

STAND_NOW_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

ALLOWED_STAND_NOW_FIELDS = frozenset(
    {
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
        "current_work_basis",
        "readout_basis",
        "handoff_basis",
        "export_basis",
        "delivery_basis",
        "application_basis",
        "answer_read_basis",
        "non_claims",
    }
)

BLOCK_CODE_MAP = {
    "EFFECTIVE_QUERY_ARTIFACT_UNREADABLE": "EFFECTIVE_STAND_NOW_ARTIFACT_UNREADABLE",
    "EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT": (
        "EFFECTIVE_STAND_NOW_INPUT_NOT_INTERNALLY_COHERENT"
    ),
    "EFFECTIVE_QUERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "EFFECTIVE_STAND_NOW_INPUT_DOES_NOT_CORRESPOND_TO_RESULT"
    ),
    "QUERY_REQUEST_OUT_OF_SCOPE": "WHAT_STANDS_NOW_REQUEST_OUT_OF_SCOPE",
}

BLOCK_REASONS = {
    "NO_CURRENT_STATE_ANSWER_READ_RESULT": (
        "No answered current-state result is available for what-stands-now "
        "answering."
    ),
    "CURRENT_STATE_ANSWER_READ_UNREADABLE": (
        "The selected current-state answer/read result could not be read."
    ),
    "CURRENT_STATE_ANSWER_READ_NOT_ANSWERED": (
        "The selected current-state answer/read result is not answered."
    ),
    "EFFECTIVE_STAND_NOW_ARTIFACT_UNREADABLE": (
        "One or more effective stand-now artifacts are unreadable."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "Effective stand-now artifacts do not preserve the canonical execution "
        "line."
    ),
    "EFFECTIVE_STAND_NOW_INPUT_NOT_INTERNALLY_COHERENT": (
        "Effective stand-now inputs are not internally coherent."
    ),
    "EFFECTIVE_STAND_NOW_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "Effective stand-now inputs do not correspond to the selected "
        "answer/read result."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based stand-now answering is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based stand-now answering is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity completion by stand-now answering is refused."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Silent standing upgrade by stand-now answering is refused."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Silent fallback to stale prior-family artifacts is refused."
    ),
    "WHAT_STANDS_NOW_REQUEST_OUT_OF_SCOPE": (
        "The request exceeds the bounded what-stands-now surface."
    ),
    "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple answered current-state results conflict without an explicit "
        "bounded selection surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **query_resolver.NON_CLAIM_DEFAULTS,
    "final_current_state_what_stands_now_completed": False,
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


def _count_checks(checks: Sequence[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _read_json_file(path: Path | str, context: str) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"{context} not found: {resolved}") from exc
    except OSError as exc:
        raise CurrentStateWhatStandsNowError(
            f"{context} is unreadable: {resolved}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateWhatStandsNowError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(payload, dict):
        raise CurrentStateWhatStandsNowError(
            f"{context} must be a JSON object: {resolved}"
        )
    return payload


def read_what_stands_now_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded what-stands-now request JSON object."""

    request = _read_json_file(path, "what-stands-now request")
    return _normal_what_stands_now_request(request)


def _validate_what_stands_now_request_shape(
    request: Mapping[str, Any],
) -> None:
    if not isinstance(request, Mapping):
        raise CurrentStateWhatStandsNowError(
            "what_stands_now_request must be a mapping"
        )
    for key in (
        "what_stands_now_request_id",
        "query_family",
        "requested_stand_now_fields",
        "query_basis",
    ):
        if key not in request:
            raise CurrentStateWhatStandsNowError(
                f"what-stands-now request is missing {key}"
            )
    for key in ("what_stands_now_request_id", "query_family", "query_basis"):
        value = request.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CurrentStateWhatStandsNowError(
                f"what-stands-now request {key} must be non-empty"
            )
    if str(request.get("query_family")).strip() != QUERY_FAMILY:
        raise CurrentStateWhatStandsNowError(
            "what-stands-now request query_family must be 'what_stands_now'"
        )
    requested_fields = request.get("requested_stand_now_fields")
    if not isinstance(requested_fields, list) or not requested_fields:
        raise CurrentStateWhatStandsNowError(
            "what-stands-now request requested_stand_now_fields must be a "
            "non-empty list"
        )
    for field in requested_fields:
        if not isinstance(field, str) or not field.strip():
            raise CurrentStateWhatStandsNowError(
                "what-stands-now request fields must be non-empty strings"
            )


def _normal_what_stands_now_request(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    _validate_what_stands_now_request_shape(request)
    return {
        "what_stands_now_request_id": str(
            request["what_stands_now_request_id"]
        ).strip(),
        "query_family": QUERY_FAMILY,
        "requested_stand_now_fields": [
            str(field).strip() for field in request["requested_stand_now_fields"]
        ],
        "query_basis": str(request["query_basis"]).strip(),
    }


def _to_query_request(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "query_request_id": request["what_stands_now_request_id"],
        "query_target": "answer_read_output",
        "requested_fields": list(request["requested_stand_now_fields"]),
        "query_basis": request["query_basis"],
    }


def _out_of_scope_fields(request: Mapping[str, Any]) -> list[str]:
    fields = request.get("requested_stand_now_fields", [])
    if not isinstance(fields, list):
        return []
    return [
        field
        for field in fields
        if isinstance(field, str) and field not in ALLOWED_STAND_NOW_FIELDS
    ]


def _selected_from_answer_read(
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
        "current_state_answer_read_result_id": metadata.get("answer_read_result_id")
        if isinstance(metadata, Mapping)
        else None,
        "outcome": answer_read.get("outcome"),
        "selected_current_state_application_id": selected_application.get(
            "current_state_application_result_id"
        )
        if isinstance(selected_application, Mapping)
        else None,
    }


def _blocked_result(
    *,
    request: Mapping[str, Any],
    block_code: str,
    selected_answer_read: Mapping[str, Any] | None = None,
    answer_read_path: Path | str | None = None,
    checks: Sequence[Mapping[str, Any]] | None = None,
) -> dict[str, Any]:
    selected = _selected_from_answer_read(selected_answer_read, answer_read_path)
    check_list = [dict(check) for check in checks or ()]
    result_id = _stand_now_result_id(
        selected.get("current_state_answer_read_result_id"),
        request,
        OUTCOME_BLOCKED,
    )
    summary = _stand_now_summary(
        result_id=result_id,
        selected=selected,
        request=request,
        checks=check_list,
        answer=None,
        query_result={},
    )
    return {
        "what_stands_now_metadata": {
            "what_stands_now_result_id": result_id,
            "what_stands_now_result_type": WHAT_STANDS_NOW_RESULT_TYPE,
            "what_stands_now_result_version": WHAT_STANDS_NOW_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_answer_read": selected,
        "what_stands_now_request": dict(request),
        "effective_stand_now_inputs": {key: None for key in STAND_NOW_INPUT_KEYS},
        "checks": check_list,
        "outcome": OUTCOME_BLOCKED,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code, block_code),
        },
        "what_stands_now_answer": None,
        "what_stands_now_summary": summary,
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }


def _request_scope_block(
    request: Mapping[str, Any],
    selected_answer_read: Mapping[str, Any] | None = None,
    answer_read_path: Path | str | None = None,
) -> dict[str, Any] | None:
    unknown = _out_of_scope_fields(request)
    if not unknown:
        return None
    checks = [
        {
            "check_name": "what_stands_now_request_within_bounded_stand_now_surface",
            "passed": False,
            "expected_posture": "requested fields from bounded stand-now field set",
            "actual_posture": {
                "requested_stand_now_fields": request.get(
                    "requested_stand_now_fields"
                ),
                "out_of_scope_fields": sorted(unknown),
                "allowed_field_count": len(ALLOWED_STAND_NOW_FIELDS),
            },
            "block_code": "WHAT_STANDS_NOW_REQUEST_OUT_OF_SCOPE",
        }
    ]
    return _blocked_result(
        request=request,
        block_code="WHAT_STANDS_NOW_REQUEST_OUT_OF_SCOPE",
        selected_answer_read=selected_answer_read,
        answer_read_path=answer_read_path,
        checks=checks,
    )


@contextmanager
def _query_repo_root_bound() -> Iterator[None]:
    previous = query_resolver._repo_root
    query_resolver._repo_root = _repo_root
    try:
        yield
    finally:
        query_resolver._repo_root = previous


def _query_error(
    exc: query_resolver.CurrentStateQueryError,
) -> CurrentStateWhatStandsNowError:
    return CurrentStateWhatStandsNowError(str(exc))


def _resolve_query(
    query_request: Mapping[str, Any],
    current_state_answer_read: Mapping[str, Any] | None,
) -> dict[str, Any]:
    try:
        with _query_repo_root_bound():
            return query_resolver.resolve_current_state_query(
                query_request,
                current_state_answer_read,
            )
    except query_resolver.CurrentStateQueryError as exc:
        raise _query_error(exc) from exc


def _resolve_query_from_path(
    path: Path | str,
    query_request: Mapping[str, Any],
) -> dict[str, Any]:
    try:
        with _query_repo_root_bound():
            return query_resolver.resolve_current_state_query_from_path(
                path,
                query_request,
            )
    except query_resolver.CurrentStateQueryError as exc:
        raise _query_error(exc) from exc


def _map_block_code(block_code: Any) -> str | None:
    if block_code is None:
        return None
    code = str(block_code)
    return BLOCK_CODE_MAP.get(code, code)


def _map_block_reason(block_code: str | None, original_reason: Any) -> str | None:
    if block_code is None:
        return None
    return BLOCK_REASONS.get(block_code) or (
        str(original_reason) if isinstance(original_reason, str) else block_code
    )


def _stand_now_result_id(
    selected_answer_read_id: Any,
    request: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    base = selected_answer_read_id
    if not isinstance(base, str) or not base:
        base = "no_current_state_answer_read_result"
    request_id = None
    if isinstance(request, Mapping):
        request_id = request.get("what_stands_now_request_id")
    if not isinstance(request_id, str) or not request_id:
        request_id = "what_stands_now_request"
    suffix = (
        "what_stands_now_answered"
        if outcome == OUTCOME_ANSWERED_WHAT_STANDS_NOW
        else "what_stands_now_blocked"
    )
    return f"{base}__{request_id}__{suffix}"


def _non_claims_from_query_result(
    query_result: Mapping[str, Any],
) -> dict[str, bool]:
    raw = query_result.get("non_claims", {})
    if raw is None:
        raw = {}
    if not isinstance(raw, Mapping):
        raise CurrentStateWhatStandsNowError("query result non_claims must be an object")
    result = dict(NON_CLAIM_DEFAULTS)
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateWhatStandsNowError("non_claim keys must be strings")
        if not isinstance(value, bool):
            raise CurrentStateWhatStandsNowError(
                f"non_claim value for {key!r} must be boolean"
            )
        result[key] = value
    for key in NON_CLAIM_DEFAULTS:
        result.setdefault(key, False)
    return result


def _transform_check(check: Mapping[str, Any]) -> dict[str, Any]:
    transformed = dict(check)
    block_code = transformed.get("block_code")
    if block_code is not None:
        transformed["block_code"] = _map_block_code(block_code)
    name = transformed.get("check_name")
    if isinstance(name, str):
        transformed["check_name"] = (
            name.replace("effective_query", "effective_stand_now")
            .replace("query_request", "what_stands_now_request")
            .replace("query selected", "stand-now answer selected")
            .replace("query target", "stand-now request target")
        )
    if transformed.get("expected_posture") == (
        "query target and requested fields exposed by answer/read result"
    ):
        transformed["expected_posture"] = (
            "stand-now request fields exposed by answer/read result"
        )
    return transformed


def _transform_checks(query_result: Mapping[str, Any]) -> list[dict[str, Any]]:
    checks = query_result.get("checks", [])
    if not isinstance(checks, list):
        raise CurrentStateWhatStandsNowError("query result checks must be a list")
    result: list[dict[str, Any]] = []
    for check in checks:
        if not isinstance(check, Mapping):
            raise CurrentStateWhatStandsNowError("query result checks must be objects")
        result.append(_transform_check(check))
    return result


def _selected_answer_read(query_result: Mapping[str, Any]) -> dict[str, Any]:
    selected = query_result.get("selected_current_state_answer_read", {})
    if not isinstance(selected, Mapping):
        selected = {}
    return {
        "current_state_answer_read_result_path": selected.get(
            "current_state_answer_read_result_path"
        ),
        "current_state_answer_read_result_id": selected.get(
            "current_state_answer_read_result_id"
        ),
        "outcome": selected.get("outcome"),
        "selected_current_state_application_id": selected.get(
            "selected_current_state_application_id"
        ),
    }


def _effective_stand_now_inputs(query_result: Mapping[str, Any]) -> dict[str, Any]:
    inputs = query_result.get("effective_query_inputs", {})
    if not isinstance(inputs, Mapping):
        inputs = {}
    return {key: inputs.get(key) for key in STAND_NOW_INPUT_KEYS}


def _stand_now_answer(
    query_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any] | None:
    if query_result.get("outcome") != query_resolver.OUTCOME_ANSWERED_QUERY:
        return None
    query_answer = query_result.get("query_answer", {})
    if not isinstance(query_answer, Mapping):
        raise CurrentStateWhatStandsNowError("answered query result is malformed")
    fields = query_answer.get("answered_fields", {})
    if not isinstance(fields, Mapping):
        raise CurrentStateWhatStandsNowError("answered query fields are malformed")
    return {
        field: fields.get(field)
        for field in request.get("requested_stand_now_fields", [])
    }


def _stand_now_summary(
    *,
    result_id: str,
    selected: Mapping[str, Any],
    request: Mapping[str, Any] | None,
    checks: Sequence[Mapping[str, Any]],
    answer: Mapping[str, Any] | None,
    query_result: Mapping[str, Any],
) -> dict[str, Any]:
    passed, failed = _count_checks(checks)
    requested = (
        request.get("requested_stand_now_fields")
        if isinstance(request, Mapping)
        else []
    )
    if not isinstance(requested, list):
        requested = []
    answered_names = list(answer) if isinstance(answer, Mapping) else []
    query_summary = query_result.get("query_summary", {})
    if not isinstance(query_summary, Mapping):
        query_summary = {}
    return {
        "what_stands_now_result_id": result_id,
        "selected_current_state_answer_read_id": selected.get(
            "current_state_answer_read_result_id"
        ),
        "requested_field_names": list(requested),
        "answered_field_count": len(answered_names),
        "answered_field_names": answered_names,
        "stand_now_basis": "answered_current_state_result",
        "query_family": QUERY_FAMILY,
        "effective_current_governing_source_run_path": query_summary.get(
            "effective_current_governing_source_run_path"
        ),
        "effective_current_governing_ingress_run_path": query_summary.get(
            "effective_current_governing_ingress_run_path"
        ),
        "passed_check_count": passed,
        "failed_check_count": failed,
    }


def _result_from_query_result(
    query_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    selected = _selected_answer_read(query_result)
    checks = _transform_checks(query_result)
    raw_block = query_result.get("block", {})
    if not isinstance(raw_block, Mapping):
        raw_block = {}
    raw_outcome = query_result.get("outcome")
    answered = raw_outcome == query_resolver.OUTCOME_ANSWERED_QUERY
    outcome = (
        OUTCOME_ANSWERED_WHAT_STANDS_NOW
        if answered
        else OUTCOME_BLOCKED
    )
    block_code = None if answered else _map_block_code(raw_block.get("block_code"))
    block_reason = None if answered else _map_block_reason(
        block_code,
        raw_block.get("block_reason"),
    )
    answer = _stand_now_answer(query_result, request)
    result_id = _stand_now_result_id(
        selected.get("current_state_answer_read_result_id"),
        request,
        outcome,
    )
    summary = _stand_now_summary(
        result_id=result_id,
        selected=selected,
        request=request,
        checks=checks,
        answer=answer,
        query_result=query_result,
    )

    return {
        "what_stands_now_metadata": {
            "what_stands_now_result_id": result_id,
            "what_stands_now_result_type": WHAT_STANDS_NOW_RESULT_TYPE,
            "what_stands_now_result_version": WHAT_STANDS_NOW_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_answer_read": selected,
        "what_stands_now_request": dict(request),
        "effective_stand_now_inputs": _effective_stand_now_inputs(query_result),
        "checks": checks,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "what_stands_now_answer": answer,
        "what_stands_now_summary": summary,
        "non_claims": _non_claims_from_query_result(query_result),
    }


def resolve_current_state_what_stands_now(
    what_stands_now_request: Mapping[str, Any],
    current_state_answer_read: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded concrete what-stands-now answer."""

    request = _normal_what_stands_now_request(what_stands_now_request)
    scope_block = _request_scope_block(request, current_state_answer_read)
    if scope_block is not None:
        return scope_block
    query_request = _to_query_request(request)
    query_result = _resolve_query(query_request, current_state_answer_read)
    return _result_from_query_result(query_result, request)


def resolve_current_state_what_stands_now_from_path(
    path: Path | str,
    what_stands_now_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one answer/read artifact and resolve one stand-now answer."""

    request = _normal_what_stands_now_request(what_stands_now_request)
    scope_block = _request_scope_block(request, answer_read_path=path)
    if scope_block is not None:
        return scope_block
    query_request = _to_query_request(request)
    query_result = _resolve_query_from_path(path, query_request)
    return _result_from_query_result(query_result, request)


def build_current_state_what_stands_now_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a small inspection-friendly summary of a stand-now result."""

    if not isinstance(result, Mapping):
        raise CurrentStateWhatStandsNowError("what-stands-now result must be a mapping")
    metadata = result.get("what_stands_now_metadata", {})
    selected = result.get("selected_current_state_answer_read", {})
    request = result.get("what_stands_now_request", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    answer = result.get("what_stands_now_answer", {})
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateWhatStandsNowError("stand-now checks must be a list")
    passed, failed = _count_checks(checks)

    requested_names: list[Any] = []
    if isinstance(request, Mapping):
        raw_requested = request.get("requested_stand_now_fields", [])
        if isinstance(raw_requested, list):
            requested_names = list(raw_requested)

    answered_names: list[Any] = []
    if isinstance(answer, Mapping):
        answered_names = list(answer)

    return {
        "what_stands_now_result_id": metadata.get("what_stands_now_result_id")
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
        "requested_field_names": requested_names,
        "answered_field_names": answered_names,
        "passed_check_count": passed,
        "failed_check_count": failed,
        "non_claims": dict(non_claims) if isinstance(non_claims, Mapping) else {},
    }


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = DEFAULT_WHAT_STANDS_NOW_RESULT_STEM
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value)
    compact = compact.strip("._")
    return compact[:160] or DEFAULT_WHAT_STANDS_NOW_RESULT_STEM


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_STATE_WHAT_STANDS_NOW_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_current_state_answer_read", {})
    selected_id = None
    if isinstance(selected, Mapping):
        selected_id = selected.get("current_state_answer_read_result_id")
    stem = _safe_filename_part(selected_id)
    candidate = resolved_root / f"{stem}__{DEFAULT_WHAT_STANDS_NOW_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            resolved_root
            / f"{stem}__{DEFAULT_WHAT_STANDS_NOW_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentStateWhatStandsNowError(
        "no bounded current-state what-stands-now filename available"
    )


def write_current_state_what_stands_now_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive what-stands-now result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentStateWhatStandsNowError(
            "what-stands-now result must be a mapping"
        )

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"current-state what-stands-now result already exists: {target}"
        )

    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
