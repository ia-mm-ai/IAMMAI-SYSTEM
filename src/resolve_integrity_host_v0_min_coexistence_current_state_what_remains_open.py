"""Resolve one bounded "what remains open" answer for the v0-min line.

This module consumes an answered current-state result and one bounded
open-surface request, delegates the shared current-state correspondence checks
to the current-state query resolver, and emits one additive concrete question
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


class CurrentStateWhatRemainsOpenError(RuntimeError):
    """Raised when open-surface inputs are malformed or impossible to use."""


CURRENT_STATE_ANSWER_SURFACE_ROOT = query_resolver.CURRENT_STATE_ANSWER_SURFACE_ROOT
CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_what_remains_open"
)

WHAT_REMAINS_OPEN_RESULT_TYPE = (
    "IAMMAI_INTEGRITY_HOST_V0_MIN_COEXISTENCE_CURRENT_STATE_WHAT_REMAINS_OPEN_RESULT"
)
WHAT_REMAINS_OPEN_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_integrity_host_v0_min_coexistence_current_state_what_remains_open"
)

OUTCOME_ANSWERED_WHAT_REMAINS_OPEN = "ANSWERED_WHAT_REMAINS_OPEN"
OUTCOME_BLOCKED = "BLOCKED"

QUERY_FAMILY = "what_remains_open"
DEFAULT_WHAT_REMAINS_OPEN_RESULT_STEM = "current_state_what_remains_open_result"

OPEN_INPUT_KEYS = (
    "effective_authority_artifact_path",
    "effective_family_packet_path",
    "effective_status_packet_path",
    "effective_current_governing_packet_path",
    "effective_source_run_path",
    "effective_ingress_run_path",
)

BASIS_OPEN_FIELDS = frozenset(
    {
        "current_work_basis",
        "readout_basis",
        "handoff_basis",
        "export_basis",
        "delivery_basis",
        "application_basis",
        "answer_read_basis",
    }
)

LOCAL_FALSE_OPEN_FIELDS = frozenset(
    {
        "authority_resolution_is_protocol_law",
        "final_persistence_or_registry_law",
    }
)

ALLOWED_OPEN_FIELDS = frozenset(
    {
        "non_claims",
        "continuity_completed",
        "standing_upgraded",
        "replayed_into_live_host",
        "merged_into_local_state",
        "minimum_lawful_system_completed",
        "final_system_identity_completed",
        "final_preserved_run_governance_completed",
        "final_governing_scope_completed",
        "final_governing_transition_law_completed",
        "final_governing_reresolution_completed",
        "final_governing_successor_adoption_completed",
        "final_effective_family_resolution_completed",
        "final_effective_family_consumption_completed",
        "final_current_work_input_resolution_completed",
        "final_current_work_operation_completed",
        "final_current_state_readout_completed",
        "final_current_state_handoff_completed",
        "final_current_state_export_completed",
        "final_current_state_delivery_completed",
        "final_current_state_application_completed",
        "final_current_state_answer_read_completed",
        "final_current_state_query_completed",
        "authority_resolution_is_protocol_law",
        "final_persistence_or_registry_law",
        "current_work_basis",
        "readout_basis",
        "handoff_basis",
        "export_basis",
        "delivery_basis",
        "application_basis",
        "answer_read_basis",
    }
)

BLOCK_CODE_MAP = {
    "EFFECTIVE_QUERY_ARTIFACT_UNREADABLE": (
        "EFFECTIVE_OPEN_SURFACE_ARTIFACT_UNREADABLE"
    ),
    "EFFECTIVE_QUERY_INPUT_NOT_INTERNALLY_COHERENT": (
        "EFFECTIVE_OPEN_SURFACE_INPUT_NOT_INTERNALLY_COHERENT"
    ),
    "EFFECTIVE_QUERY_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "EFFECTIVE_OPEN_SURFACE_INPUT_DOES_NOT_CORRESPOND_TO_RESULT"
    ),
    "QUERY_REQUEST_OUT_OF_SCOPE": "WHAT_REMAINS_OPEN_REQUEST_OUT_OF_SCOPE",
}

BLOCK_REASONS = {
    "NO_CURRENT_STATE_ANSWER_READ_RESULT": (
        "No answered current-state result is available for what-remains-open "
        "answering."
    ),
    "CURRENT_STATE_ANSWER_READ_UNREADABLE": (
        "The selected current-state answer/read result could not be read."
    ),
    "CURRENT_STATE_ANSWER_READ_NOT_ANSWERED": (
        "The selected current-state answer/read result is not answered."
    ),
    "EFFECTIVE_OPEN_SURFACE_ARTIFACT_UNREADABLE": (
        "One or more effective open-surface artifacts are unreadable."
    ),
    "CANONICAL_EXECUTION_LINE_MISMATCH": (
        "Effective open-surface artifacts do not preserve the canonical "
        "execution line."
    ),
    "EFFECTIVE_OPEN_SURFACE_INPUT_NOT_INTERNALLY_COHERENT": (
        "Effective open-surface inputs are not internally coherent."
    ),
    "EFFECTIVE_OPEN_SURFACE_INPUT_DOES_NOT_CORRESPOND_TO_RESULT": (
        "Effective open-surface inputs do not correspond to the selected "
        "answer/read result."
    ),
    "REPLAY_SHORTCUT_REFUSED": "Replay-based open-surface answering is refused.",
    "MERGE_SHORTCUT_REFUSED": "Merge-based open-surface answering is refused.",
    "CONTINUITY_COMPLETION_SHORTCUT_REFUSED": (
        "Continuity completion by open-surface answering is refused."
    ),
    "SILENT_STANDING_UPGRADE_REFUSED": (
        "Silent standing upgrade by open-surface answering is refused."
    ),
    "STALE_PRIOR_FAMILY_FALLBACK_REFUSED": (
        "Silent fallback to stale prior-family artifacts is refused."
    ),
    "WHAT_REMAINS_OPEN_REQUEST_OUT_OF_SCOPE": (
        "The request exceeds the bounded what-remains-open surface."
    ),
    "MULTIPLE_CURRENT_STATE_ANSWER_READ_RESULTS_CONFLICT_UNRESOLVED": (
        "Multiple answered current-state results conflict without an explicit "
        "bounded selection surface."
    ),
}

NON_CLAIM_DEFAULTS = {
    **query_resolver.NON_CLAIM_DEFAULTS,
    "final_current_state_what_stands_now_completed": False,
    "final_current_state_what_remains_open_completed": False,
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
        raise CurrentStateWhatRemainsOpenError(
            f"{context} is unreadable: {resolved}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise CurrentStateWhatRemainsOpenError(
            f"{context} is malformed JSON: {resolved}"
        ) from exc
    if not isinstance(payload, dict):
        raise CurrentStateWhatRemainsOpenError(
            f"{context} must be a JSON object: {resolved}"
        )
    return payload


def read_what_remains_open_request(path: Path | str) -> dict[str, Any]:
    """Read one bounded what-remains-open request JSON object."""

    request = _read_json_file(path, "what-remains-open request")
    return _normal_what_remains_open_request(request)


def _validate_what_remains_open_request_shape(
    request: Mapping[str, Any],
) -> None:
    if not isinstance(request, Mapping):
        raise CurrentStateWhatRemainsOpenError(
            "what_remains_open_request must be a mapping"
        )
    for key in (
        "what_remains_open_request_id",
        "query_family",
        "requested_open_fields",
        "query_basis",
    ):
        if key not in request:
            raise CurrentStateWhatRemainsOpenError(
                f"what-remains-open request is missing {key}"
            )
    for key in ("what_remains_open_request_id", "query_family", "query_basis"):
        value = request.get(key)
        if not isinstance(value, str) or not value.strip():
            raise CurrentStateWhatRemainsOpenError(
                f"what-remains-open request {key} must be non-empty"
            )
    if str(request.get("query_family")).strip() != QUERY_FAMILY:
        raise CurrentStateWhatRemainsOpenError(
            "what-remains-open request query_family must be 'what_remains_open'"
        )
    requested_fields = request.get("requested_open_fields")
    if not isinstance(requested_fields, list) or not requested_fields:
        raise CurrentStateWhatRemainsOpenError(
            "what-remains-open request requested_open_fields must be a "
            "non-empty list"
        )
    for field in requested_fields:
        if not isinstance(field, str) or not field.strip():
            raise CurrentStateWhatRemainsOpenError(
                "what-remains-open request fields must be non-empty strings"
            )


def _normal_what_remains_open_request(
    request: Mapping[str, Any],
) -> dict[str, Any]:
    _validate_what_remains_open_request_shape(request)
    return {
        "what_remains_open_request_id": str(
            request["what_remains_open_request_id"]
        ).strip(),
        "query_family": QUERY_FAMILY,
        "requested_open_fields": [
            str(field).strip() for field in request["requested_open_fields"]
        ],
        "query_basis": str(request["query_basis"]).strip(),
    }


def _to_query_request(request: Mapping[str, Any]) -> dict[str, Any]:
    query_fields: list[str] = []
    for field in request.get("requested_open_fields", []):
        if field in BASIS_OPEN_FIELDS or field == "non_claims":
            if field not in query_fields:
                query_fields.append(field)
    if "non_claims" not in query_fields:
        query_fields.append("non_claims")
    return {
        "query_request_id": request["what_remains_open_request_id"],
        "query_target": "answer_read_output",
        "requested_fields": query_fields,
        "query_basis": request["query_basis"],
    }


def _out_of_scope_fields(request: Mapping[str, Any]) -> list[str]:
    fields = request.get("requested_open_fields", [])
    if not isinstance(fields, list):
        return []
    return [
        field
        for field in fields
        if isinstance(field, str) and field not in ALLOWED_OPEN_FIELDS
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
    result_id = _open_result_id(
        selected.get("current_state_answer_read_result_id"),
        request,
        OUTCOME_BLOCKED,
    )
    summary = _open_summary(
        result_id=result_id,
        selected=selected,
        request=request,
        checks=check_list,
        answer=None,
        query_result={},
    )
    return {
        "what_remains_open_metadata": {
            "what_remains_open_result_id": result_id,
            "what_remains_open_result_type": WHAT_REMAINS_OPEN_RESULT_TYPE,
            "what_remains_open_result_version": WHAT_REMAINS_OPEN_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_answer_read": selected,
        "what_remains_open_request": dict(request),
        "effective_open_inputs": {key: None for key in OPEN_INPUT_KEYS},
        "checks": check_list,
        "outcome": OUTCOME_BLOCKED,
        "block": {
            "block_code": block_code,
            "block_reason": BLOCK_REASONS.get(block_code, block_code),
        },
        "what_remains_open_answer": None,
        "what_remains_open_summary": summary,
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
            "check_name": (
                "what_remains_open_request_within_bounded_open_surface"
            ),
            "passed": False,
            "expected_posture": "requested fields from bounded open-surface field set",
            "actual_posture": {
                "requested_open_fields": request.get("requested_open_fields"),
                "out_of_scope_fields": sorted(unknown),
                "allowed_field_count": len(ALLOWED_OPEN_FIELDS),
            },
            "block_code": "WHAT_REMAINS_OPEN_REQUEST_OUT_OF_SCOPE",
        }
    ]
    return _blocked_result(
        request=request,
        block_code="WHAT_REMAINS_OPEN_REQUEST_OUT_OF_SCOPE",
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
) -> CurrentStateWhatRemainsOpenError:
    return CurrentStateWhatRemainsOpenError(str(exc))


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


def _open_result_id(
    selected_answer_read_id: Any,
    request: Mapping[str, Any] | None,
    outcome: str,
) -> str:
    base = selected_answer_read_id
    if not isinstance(base, str) or not base:
        base = "no_current_state_answer_read_result"
    request_id = None
    if isinstance(request, Mapping):
        request_id = request.get("what_remains_open_request_id")
    if not isinstance(request_id, str) or not request_id:
        request_id = "what_remains_open_request"
    suffix = (
        "what_remains_open_answered"
        if outcome == OUTCOME_ANSWERED_WHAT_REMAINS_OPEN
        else "what_remains_open_blocked"
    )
    return f"{base}__{request_id}__{suffix}"


def _non_claims_from_query_result(
    query_result: Mapping[str, Any],
) -> dict[str, bool]:
    raw = query_result.get("non_claims", {})
    if raw is None:
        raw = {}
    if not isinstance(raw, Mapping):
        raise CurrentStateWhatRemainsOpenError(
            "query result non_claims must be an object"
        )
    result = dict(NON_CLAIM_DEFAULTS)
    for key, value in raw.items():
        if not isinstance(key, str):
            raise CurrentStateWhatRemainsOpenError("non_claim keys must be strings")
        if not isinstance(value, bool):
            raise CurrentStateWhatRemainsOpenError(
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
            name.replace("effective_query", "effective_open_surface")
            .replace("query_request", "what_remains_open_request")
            .replace("query selected", "open-surface answer selected")
            .replace("query target", "open-surface request target")
        )
    if transformed.get("expected_posture") == (
        "query target and requested fields exposed by answer/read result"
    ):
        transformed["expected_posture"] = (
            "open-surface request fields exposed by answer/read result"
        )
    return transformed


def _request_scope_check(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "check_name": "what_remains_open_request_within_bounded_open_surface",
        "passed": True,
        "expected_posture": "requested fields from bounded open-surface field set",
        "actual_posture": {
            "requested_open_fields": list(request.get("requested_open_fields", [])),
            "allowed_field_count": len(ALLOWED_OPEN_FIELDS),
        },
    }


def _transform_checks(
    query_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> list[dict[str, Any]]:
    checks = query_result.get("checks", [])
    if not isinstance(checks, list):
        raise CurrentStateWhatRemainsOpenError("query result checks must be a list")
    result: list[dict[str, Any]] = []
    for check in checks:
        if not isinstance(check, Mapping):
            raise CurrentStateWhatRemainsOpenError(
                "query result checks must be objects"
            )
        result.append(_transform_check(check))
    result.append(_request_scope_check(request))
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


def _effective_open_inputs(query_result: Mapping[str, Any]) -> dict[str, Any]:
    inputs = query_result.get("effective_query_inputs", {})
    if not isinstance(inputs, Mapping):
        inputs = {}
    return {key: inputs.get(key) for key in OPEN_INPUT_KEYS}


def _open_field_sources(query_result: Mapping[str, Any]) -> dict[str, Any]:
    query_answer = query_result.get("query_answer", {})
    if not isinstance(query_answer, Mapping):
        query_answer = {}
    answered_fields = query_answer.get("answered_fields", {})
    if not isinstance(answered_fields, Mapping):
        answered_fields = {}

    non_claims = _non_claims_from_query_result(query_result)
    sources: dict[str, Any] = dict(answered_fields)
    sources["non_claims"] = dict(non_claims)
    for key, value in non_claims.items():
        sources[key] = value
    for key in LOCAL_FALSE_OPEN_FIELDS:
        sources[key] = False
    return sources


def _open_answer(
    query_result: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any] | None:
    if query_result.get("outcome") != query_resolver.OUTCOME_ANSWERED_QUERY:
        return None
    sources = _open_field_sources(query_result)
    return {
        field: sources.get(field)
        for field in request.get("requested_open_fields", [])
    }


def _open_summary(
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
        request.get("requested_open_fields") if isinstance(request, Mapping) else []
    )
    if not isinstance(requested, list):
        requested = []
    answered_names = list(answer) if isinstance(answer, Mapping) else []
    query_summary = query_result.get("query_summary", {})
    if not isinstance(query_summary, Mapping):
        query_summary = {}
    return {
        "what_remains_open_result_id": result_id,
        "selected_current_state_answer_read_id": selected.get(
            "current_state_answer_read_result_id"
        ),
        "requested_field_names": list(requested),
        "answered_field_count": len(answered_names),
        "answered_field_names": answered_names,
        "open_surface_basis": "answered_current_state_result",
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
    checks = _transform_checks(query_result, request)
    raw_block = query_result.get("block", {})
    if not isinstance(raw_block, Mapping):
        raw_block = {}
    raw_outcome = query_result.get("outcome")
    answered = raw_outcome == query_resolver.OUTCOME_ANSWERED_QUERY
    outcome = OUTCOME_ANSWERED_WHAT_REMAINS_OPEN if answered else OUTCOME_BLOCKED
    block_code = None if answered else _map_block_code(raw_block.get("block_code"))
    block_reason = None if answered else _map_block_reason(
        block_code,
        raw_block.get("block_reason"),
    )
    answer = _open_answer(query_result, request)
    result_id = _open_result_id(
        selected.get("current_state_answer_read_result_id"),
        request,
        outcome,
    )
    summary = _open_summary(
        result_id=result_id,
        selected=selected,
        request=request,
        checks=checks,
        answer=answer,
        query_result=query_result,
    )

    return {
        "what_remains_open_metadata": {
            "what_remains_open_result_id": result_id,
            "what_remains_open_result_type": WHAT_REMAINS_OPEN_RESULT_TYPE,
            "what_remains_open_result_version": WHAT_REMAINS_OPEN_RESULT_VERSION,
            "generated_at": _now_iso(),
            "resolver_module": RESOLVER_MODULE,
        },
        "selected_current_state_answer_read": selected,
        "what_remains_open_request": dict(request),
        "effective_open_inputs": _effective_open_inputs(query_result),
        "checks": checks,
        "outcome": outcome,
        "block": {
            "block_code": block_code,
            "block_reason": block_reason,
        },
        "what_remains_open_answer": answer,
        "what_remains_open_summary": summary,
        "non_claims": _non_claims_from_query_result(query_result),
    }


def resolve_current_state_what_remains_open(
    what_remains_open_request: Mapping[str, Any],
    current_state_answer_read: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded concrete what-remains-open answer."""

    request = _normal_what_remains_open_request(what_remains_open_request)
    scope_block = _request_scope_block(request, current_state_answer_read)
    if scope_block is not None:
        return scope_block
    query_request = _to_query_request(request)
    query_result = _resolve_query(query_request, current_state_answer_read)
    return _result_from_query_result(query_result, request)


def resolve_current_state_what_remains_open_from_path(
    path: Path | str,
    what_remains_open_request: Mapping[str, Any],
) -> dict[str, Any]:
    """Read one answer/read artifact and resolve one open-surface answer."""

    request = _normal_what_remains_open_request(what_remains_open_request)
    scope_block = _request_scope_block(request, answer_read_path=path)
    if scope_block is not None:
        return scope_block
    query_request = _to_query_request(request)
    query_result = _resolve_query_from_path(path, query_request)
    return _result_from_query_result(query_result, request)


def build_current_state_what_remains_open_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a small inspection-friendly summary of an open-surface result."""

    if not isinstance(result, Mapping):
        raise CurrentStateWhatRemainsOpenError(
            "what-remains-open result must be a mapping"
        )
    metadata = result.get("what_remains_open_metadata", {})
    selected = result.get("selected_current_state_answer_read", {})
    request = result.get("what_remains_open_request", {})
    block = result.get("block", {})
    checks = result.get("checks", [])
    answer = result.get("what_remains_open_answer", {})
    non_claims = result.get("non_claims", {})

    if not isinstance(checks, list):
        raise CurrentStateWhatRemainsOpenError("open-surface checks must be a list")
    passed, failed = _count_checks(checks)

    requested_names: list[Any] = []
    if isinstance(request, Mapping):
        raw_requested = request.get("requested_open_fields", [])
        if isinstance(raw_requested, list):
            requested_names = list(raw_requested)

    answered_names: list[Any] = []
    if isinstance(answer, Mapping):
        answered_names = list(answer)

    return {
        "what_remains_open_result_id": metadata.get("what_remains_open_result_id")
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
        value = DEFAULT_WHAT_REMAINS_OPEN_RESULT_STEM
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value)
    compact = compact.strip("._")
    return compact[:160] or DEFAULT_WHAT_REMAINS_OPEN_RESULT_STEM


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = CURRENT_STATE_WHAT_REMAINS_OPEN_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_current_state_answer_read", {})
    selected_id = None
    if isinstance(selected, Mapping):
        selected_id = selected.get("current_state_answer_read_result_id")
    stem = _safe_filename_part(selected_id)
    candidate = (
        resolved_root / f"{stem}__{DEFAULT_WHAT_REMAINS_OPEN_RESULT_STEM}.json"
    )
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = (
            resolved_root
            / f"{stem}__{DEFAULT_WHAT_REMAINS_OPEN_RESULT_STEM}_{index:03d}.json"
        )
        if not candidate.exists():
            return candidate
    raise CurrentStateWhatRemainsOpenError(
        "no bounded current-state what-remains-open filename available"
    )


def write_current_state_what_remains_open_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive what-remains-open result JSON artifact."""

    if not isinstance(result, Mapping):
        raise CurrentStateWhatRemainsOpenError(
            "what-remains-open result must be a mapping"
        )

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(
            f"current-state what-remains-open result already exists: {target}"
        )

    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
