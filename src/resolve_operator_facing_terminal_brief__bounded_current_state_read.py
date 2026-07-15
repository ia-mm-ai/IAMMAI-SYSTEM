"""Render one bounded operator-facing terminal brief from one vessel result.

This module implements the first bounded downstream consumer of the current
v3 bounded current-state vessel line:

- one shell-owned bounded operator-facing terminal brief
- rendered from one successful bounded current-state vessel result
- with the brief remaining derivative and non-authoritative

The shell remains the law. The brief does not own source selection, source
family, provenance, rank, status, refusal law, non-claims, or result wrapping.
"""

from __future__ import annotations

import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class OperatorTerminalBriefError(RuntimeError):
    """Raised for bounded brief setup, source, packet, or output failures."""

    def __init__(self, message: str, block_code: str | None = None) -> None:
        super().__init__(message)
        self.block_code = block_code


OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT = Path(
    "artifacts/openai_api_derivative_vessel__bounded_current_state_read_v3"
)
OPERATOR_TERMINAL_BRIEF_ROOT = Path(
    "artifacts/operator_facing_terminal_brief__bounded_current_state_read"
)

ALLOWED_SOURCE_RESULT_FAMILY = (
    "openai_api_derivative_vessel_bounded_current_state_read_v3_result"
)
SUPPORTED_SOURCE_RESULT_TYPE = (
    "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_V3_RESULT"
)
UPSTREAM_ALLOWED_SOURCE_FAMILY = "current_state_what_stands_now_result"

ADMITTED_USE_CLASS = "OPERATOR_TERMINAL_BRIEF_READ"
BRIEF_USE_CASE = "BOUNDED_OPERATOR_FACING_TERMINAL_BRIEF"

SOURCE_OUTCOME_ANSWERED = "ANSWERED_DERIVATIVE_READ"
OUTCOME_BRIEF_RENDERED = "BRIEF_RENDERED"
OUTCOME_REFUSED = "REFUSED"

RESOLVER_MODULE = "resolve_operator_facing_terminal_brief__bounded_current_state_read"
BRIEF_RESULT_TYPE = (
    "IAMMAI_OPERATOR_FACING_TERMINAL_BRIEF_BOUNDED_CURRENT_STATE_READ_RESULT"
)
BRIEF_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "operator_terminal_brief_result"

BLOCK_REASONS = {
    "INVALID_SOURCE_RESULT_FAMILY": (
        "The selected vessel result is outside the bounded allowed source result family."
    ),
    "MISSING_VESSEL_RESULT": (
        "No readable answered vessel result is available for bounded terminal briefing."
    ),
    "VESSEL_RESULT_UNREADABLE": "The selected vessel result could not be read.",
    "VESSEL_RESULT_MALFORMED": "The selected vessel result is malformed.",
    "VESSEL_RESULT_NOT_SUCCESSFUL": (
        "The selected vessel result does not have outcome ANSWERED_DERIVATIVE_READ."
    ),
    "INVALID_UPSTREAM_SOURCE_FAMILY": (
        "The selected vessel result does not preserve the bounded upstream source family."
    ),
    "WIDENED_SOURCE_ATTEMPT": (
        "The terminal brief attempted to widen source scope beyond the bounded source result."
    ),
    "MALFORMED_BRIEF_PACKET": "The bounded terminal brief request packet is malformed.",
    "BRIEF_OUTPUT_OUTSIDE_CONTRACT": (
        "The terminal brief output falls outside the bounded allowed contract."
    ),
}

NON_CLAIM_DEFAULTS = {
    "source_replaced": False,
    "rank_assigned_by_brief": False,
    "authority_assigned_by_brief": False,
    "standing_assigned_by_brief": False,
    "source_scope_widened": False,
    "continuity_completed": False,
}


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def _repo_path(path: Path | str) -> Path:
    candidate = Path(path)
    return candidate if candidate.is_absolute() else _repo_root() / candidate


def _display_path(path: Path | str | None) -> str | None:
    if path is None:
        return None
    try:
        resolved = _repo_path(path)
    except TypeError:
        return str(path)
    try:
        return str(resolved.relative_to(_repo_root()))
    except ValueError:
        return str(resolved)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _safe_filename_part(value: Any) -> str:
    if not isinstance(value, str) or not value:
        value = "no_selected_vessel_result"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "no_selected_vessel_result"


def _string_or_none(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped or None


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise OperatorTerminalBriefError(
            f"{context} must be an object",
            "VESSEL_RESULT_MALFORMED",
        )
    return value


def _read_json_file(
    path: Path | str,
    *,
    context: str,
    missing_code: str,
    unreadable_code: str,
    malformed_code: str,
) -> dict[str, Any]:
    resolved = _repo_path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except FileNotFoundError as exc:
        raise OperatorTerminalBriefError(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise OperatorTerminalBriefError(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise OperatorTerminalBriefError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise OperatorTerminalBriefError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _empty_selected_vessel_result(
    source_result_path: Path | str | None = None,
) -> dict[str, Any]:
    return {
        "selected_vessel_result_path": _display_path(source_result_path),
        "selected_vessel_result_id": None,
        "selected_vessel_result_family": None,
        "selected_vessel_result_outcome": None,
        "selected_source_surface_id": None,
        "selected_source_surface_family": None,
    }


def _normalized_source_result_path(
    source_result_path: Path | str | None,
) -> Path | str | None:
    if source_result_path is None:
        return None
    if isinstance(source_result_path, (Path, str)):
        return source_result_path
    raise OperatorTerminalBriefError(
        "source_result_path must be a string, Path, or None",
        "MALFORMED_BRIEF_PACKET",
    )


def _source_result_family_from_artifact(artifact: Mapping[str, Any]) -> str | None:
    metadata = artifact.get("openai_api_derivative_vessel_v3_metadata")
    if not isinstance(metadata, Mapping):
        return None
    if _string_or_none(metadata.get("vessel_result_type")) != SUPPORTED_SOURCE_RESULT_TYPE:
        return None
    return ALLOWED_SOURCE_RESULT_FAMILY


def _selected_vessel_result_from_artifact(
    artifact: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    metadata = artifact.get("openai_api_derivative_vessel_v3_metadata")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    selected_source = artifact.get("selected_source_surface")
    selected_source = selected_source if isinstance(selected_source, Mapping) else {}
    family = _source_result_family_from_artifact(artifact)
    return {
        "selected_vessel_result_path": _display_path(path),
        "selected_vessel_result_id": _string_or_none(metadata.get("vessel_result_id")),
        "selected_vessel_result_family": family,
        "selected_vessel_result_outcome": _string_or_none(artifact.get("outcome")),
        "selected_source_surface_id": _string_or_none(
            selected_source.get("selected_source_surface_id")
        ),
        "selected_source_surface_family": _string_or_none(
            selected_source.get("selected_source_surface_family")
        ),
    }


def _validate_source_result_artifact(artifact: Mapping[str, Any]) -> None:
    family = _source_result_family_from_artifact(artifact)
    if family != ALLOWED_SOURCE_RESULT_FAMILY:
        raise OperatorTerminalBriefError(
            "selected vessel result is not a bounded current-state vessel v3 result",
            "INVALID_SOURCE_RESULT_FAMILY",
        )

    metadata = _require_mapping(
        artifact.get("openai_api_derivative_vessel_v3_metadata"),
        "vessel v3 metadata",
    )
    for key in ("vessel_result_id", "vessel_result_type", "vessel_result_version"):
        if _string_or_none(metadata.get(key)) is None:
            raise OperatorTerminalBriefError(
                f"selected vessel metadata {key} is malformed",
                "VESSEL_RESULT_MALFORMED",
            )
    if _string_or_none(metadata.get("vessel_result_type")) != SUPPORTED_SOURCE_RESULT_TYPE:
        raise OperatorTerminalBriefError(
            "selected vessel metadata type is outside the bounded source result family",
            "INVALID_SOURCE_RESULT_FAMILY",
        )

    outcome = _string_or_none(artifact.get("outcome"))
    if outcome is None:
        raise OperatorTerminalBriefError(
            "selected vessel result outcome is missing",
            "VESSEL_RESULT_MALFORMED",
        )
    if outcome != SOURCE_OUTCOME_ANSWERED:
        raise OperatorTerminalBriefError(
            "selected vessel result is not a successful answered derivative read",
            "VESSEL_RESULT_NOT_SUCCESSFUL",
        )

    selected_source = _require_mapping(
        artifact.get("selected_source_surface"),
        "selected source surface",
    )
    if _string_or_none(selected_source.get("selected_source_surface_id")) is None:
        raise OperatorTerminalBriefError(
            "selected source surface id is missing",
            "VESSEL_RESULT_MALFORMED",
        )
    if _string_or_none(selected_source.get("selected_source_surface_family")) != (
        UPSTREAM_ALLOWED_SOURCE_FAMILY
    ):
        raise OperatorTerminalBriefError(
            "selected vessel result does not preserve the bounded upstream source family",
            "INVALID_UPSTREAM_SOURCE_FAMILY",
        )

    vessel_request = _require_mapping(artifact.get("vessel_request"), "vessel request")
    if _string_or_none(vessel_request.get("allowed_source_family")) != (
        UPSTREAM_ALLOWED_SOURCE_FAMILY
    ):
        raise OperatorTerminalBriefError(
            "selected vessel request widened or lost the bounded upstream source family",
            "INVALID_UPSTREAM_SOURCE_FAMILY",
        )
    if _string_or_none(vessel_request.get("question")) is None:
        raise OperatorTerminalBriefError(
            "selected vessel request question is missing",
            "VESSEL_RESULT_MALFORMED",
        )

    derivative_answer = _require_mapping(
        artifact.get("derivative_answer"),
        "derivative answer",
    )
    answer = _string_or_none(derivative_answer.get("answer"))
    if answer is None:
        raise OperatorTerminalBriefError(
            "selected vessel derivative answer is missing",
            "VESSEL_RESULT_MALFORMED",
        )
    if derivative_answer.get("source_remains_source") is not True:
        raise OperatorTerminalBriefError(
            "selected vessel derivative answer lost source/source distinction",
            "VESSEL_RESULT_MALFORMED",
        )
    if derivative_answer.get("model_output_remains_derivative") is not True:
        raise OperatorTerminalBriefError(
            "selected vessel derivative answer lost derivative posture",
            "VESSEL_RESULT_MALFORMED",
        )

    block = artifact.get("block")
    if not isinstance(block, Mapping):
        raise OperatorTerminalBriefError(
            "selected vessel block section is malformed",
            "VESSEL_RESULT_MALFORMED",
        )


def _discover_latest_answered_vessel_result() -> tuple[Path | None, dict[str, Any] | None]:
    root = _repo_path(OPENAI_API_DERIVATIVE_VESSEL_V3_ROOT)
    if not root.exists():
        return None, None
    if not root.is_dir():
        raise OperatorTerminalBriefError(
            f"vessel v3 root is not a directory: {root}",
            "VESSEL_RESULT_UNREADABLE",
        )
    try:
        candidates = sorted(path for path in root.glob("*.json") if path.is_file())
    except OSError as exc:
        raise OperatorTerminalBriefError(
            f"vessel v3 root is unreadable: {root}",
            "VESSEL_RESULT_UNREADABLE",
        ) from exc

    for path in reversed(candidates):
        try:
            artifact = _read_json_file(
                path,
                context="discovered vessel result",
                missing_code="MISSING_VESSEL_RESULT",
                unreadable_code="VESSEL_RESULT_UNREADABLE",
                malformed_code="VESSEL_RESULT_MALFORMED",
            )
            _validate_source_result_artifact(artifact)
        except OperatorTerminalBriefError:
            continue
        return path, artifact
    return None, None


def _select_source_result_artifact(
    source_result_path: Path | str | None,
) -> tuple[Path, dict[str, Any]]:
    if source_result_path is not None:
        artifact = _read_json_file(
            source_result_path,
            context="selected vessel result",
            missing_code="MISSING_VESSEL_RESULT",
            unreadable_code="VESSEL_RESULT_UNREADABLE",
            malformed_code="VESSEL_RESULT_MALFORMED",
        )
        _validate_source_result_artifact(artifact)
        return _repo_path(source_result_path), artifact

    discovered_path, artifact = _discover_latest_answered_vessel_result()
    if discovered_path is None or artifact is None:
        raise OperatorTerminalBriefError(
            "no answered vessel v3 result is available",
            "MISSING_VESSEL_RESULT",
        )
    return discovered_path, artifact


def _brief_instructions() -> str:
    return (
        "Render one concise operator-facing terminal brief from the selected "
        "bounded derivative vessel result only. Do not widen source scope. Do "
        "not assign rank, authority, standing, provenance, or non-claims. Keep "
        "the brief derivative and non-authoritative."
    )


def build_operator_terminal_brief_request(
    source_result_artifact: Mapping[str, Any],
    source_result_path: Path | str,
) -> dict[str, Any]:
    """Build one bounded shell-owned operator terminal brief request."""

    _validate_source_result_artifact(source_result_artifact)
    selected = _selected_vessel_result_from_artifact(
        source_result_artifact,
        source_result_path,
    )
    selected_vessel_result_id = _string_or_none(selected.get("selected_vessel_result_id"))
    selected_source_surface_id = _string_or_none(selected.get("selected_source_surface_id"))
    if selected_vessel_result_id is None or selected_source_surface_id is None:
        raise OperatorTerminalBriefError(
            "selected vessel lineage is incomplete",
            "MALFORMED_BRIEF_PACKET",
        )

    vessel_request = source_result_artifact.get("vessel_request")
    vessel_request = vessel_request if isinstance(vessel_request, Mapping) else {}
    derivative_answer = source_result_artifact.get("derivative_answer")
    derivative_answer = (
        derivative_answer if isinstance(derivative_answer, Mapping) else {}
    )
    question = _string_or_none(vessel_request.get("question"))
    answer = _string_or_none(derivative_answer.get("answer"))
    if question is None or answer is None:
        raise OperatorTerminalBriefError(
            "selected vessel result does not carry the bounded question/answer pair",
            "MALFORMED_BRIEF_PACKET",
        )

    packet = {
        "brief_request_id": (
            f"{selected_vessel_result_id}__operator_terminal_brief_request"
        ),
        "brief_use_case": BRIEF_USE_CASE,
        "admitted_use_class": ADMITTED_USE_CLASS,
        "allowed_source_result_family": ALLOWED_SOURCE_RESULT_FAMILY,
        "selected_vessel_result_id": selected_vessel_result_id,
        "selected_vessel_result_path": selected["selected_vessel_result_path"],
        "selected_source_surface_id": selected_source_surface_id,
        "question": question,
        "derivative_answer": answer,
        "brief_instructions": _brief_instructions(),
    }
    _validate_brief_request(packet)
    return packet


def _validate_brief_request(packet: Mapping[str, Any]) -> None:
    if not isinstance(packet, Mapping):
        raise OperatorTerminalBriefError(
            "brief request must be a mapping",
            "MALFORMED_BRIEF_PACKET",
        )
    required = {
        "brief_request_id",
        "brief_use_case",
        "admitted_use_class",
        "allowed_source_result_family",
        "selected_vessel_result_id",
        "selected_vessel_result_path",
        "selected_source_surface_id",
        "question",
        "derivative_answer",
        "brief_instructions",
    }
    if set(packet) != required:
        raise OperatorTerminalBriefError(
            "brief request shape is malformed",
            "MALFORMED_BRIEF_PACKET",
        )
    for key in (
        "brief_request_id",
        "selected_vessel_result_id",
        "selected_vessel_result_path",
        "selected_source_surface_id",
        "question",
        "derivative_answer",
        "brief_instructions",
    ):
        if _string_or_none(packet.get(key)) is None:
            raise OperatorTerminalBriefError(
                f"brief request {key} must be non-empty",
                "MALFORMED_BRIEF_PACKET",
            )
    if packet.get("brief_use_case") != BRIEF_USE_CASE:
        raise OperatorTerminalBriefError(
            "unsupported brief use case",
            "MALFORMED_BRIEF_PACKET",
        )
    if packet.get("admitted_use_class") != ADMITTED_USE_CLASS:
        raise OperatorTerminalBriefError(
            "unsupported brief use class",
            "MALFORMED_BRIEF_PACKET",
        )
    if packet.get("allowed_source_result_family") != ALLOWED_SOURCE_RESULT_FAMILY:
        raise OperatorTerminalBriefError(
            "brief request widened source result family",
            "WIDENED_SOURCE_ATTEMPT",
        )


def _render_operator_terminal_brief(packet: Mapping[str, Any]) -> str:
    _validate_brief_request(packet)
    selected_source_surface_id = str(packet["selected_source_surface_id"]).strip()
    question = str(packet["question"]).strip()
    derivative_answer = str(packet["derivative_answer"]).strip()
    brief_text = (
        "Operator Terminal Brief\n"
        f"Selected source: {selected_source_surface_id}\n"
        f"Question: {question}\n"
        f"Derivative answer: {derivative_answer}\n"
        "Basis: bounded_derivative_vessel_result"
    )
    _validate_brief_text(brief_text)
    return brief_text


def _validate_brief_text(brief_text: Any) -> None:
    if not isinstance(brief_text, str) or not brief_text.strip():
        raise OperatorTerminalBriefError(
            "brief text must be a non-empty string",
            "BRIEF_OUTPUT_OUTSIDE_CONTRACT",
        )


def _block_reason(block_code: str, detail: str | None = None) -> str:
    base = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    if detail is None or not detail.strip():
        return base
    detail_text = detail.strip()
    if detail_text == base:
        return base
    return f"{base} Detail: {detail_text}"


def _result_id(selected_vessel_result_id: str | None, outcome: str) -> str:
    base = selected_vessel_result_id or "no_selected_vessel_result"
    suffix = (
        "operator_terminal_brief_rendered"
        if outcome == OUTCOME_BRIEF_RENDERED
        else "operator_terminal_brief_refused"
    )
    return f"{base}__{suffix}"


def _brief_output_section(brief_text: str | None) -> dict[str, Any]:
    return {
        "brief_text": brief_text,
        "brief_basis": "bounded_derivative_vessel_result",
        "source_remains_source": True,
        "vessel_output_remains_derivative": True,
        "brief_remains_derivative": True,
    }


def _result_metadata(
    selected_vessel_result_id: str | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "brief_result_id": _result_id(selected_vessel_result_id, outcome),
        "brief_result_type": BRIEF_RESULT_TYPE,
        "brief_result_version": BRIEF_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    selected = result.get("selected_vessel_result", {})
    selected = selected if isinstance(selected, Mapping) else {}
    request = result.get("brief_request", {})
    request = request if isinstance(request, Mapping) else {}
    block = result.get("block", {})
    block = block if isinstance(block, Mapping) else {}
    return {
        "selected_vessel_result_id": selected.get("selected_vessel_result_id"),
        "selected_source_surface_id": selected.get("selected_source_surface_id"),
        "question": request.get("question"),
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
    }


def _refused_result(
    *,
    block_code: str,
    block_detail: str | None,
    selected_vessel_result: Mapping[str, Any] | None,
    brief_request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    selected = (
        dict(selected_vessel_result)
        if isinstance(selected_vessel_result, Mapping)
        else _empty_selected_vessel_result()
    )
    request = dict(brief_request) if isinstance(brief_request, Mapping) else {}
    metadata = _result_metadata(
        _string_or_none(selected.get("selected_vessel_result_id")),
        OUTCOME_REFUSED,
    )
    result = {
        "operator_terminal_brief_metadata": metadata,
        "selected_vessel_result": selected,
        "brief_request": request,
        "brief_output": _brief_output_section(None),
        "outcome": OUTCOME_REFUSED,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "brief_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["brief_summary"] = _summary_from_result(result)
    return result


def _rendered_result(
    *,
    selected_vessel_result: Mapping[str, Any],
    brief_request: Mapping[str, Any],
    brief_text: str,
) -> dict[str, Any]:
    metadata = _result_metadata(
        _string_or_none(selected_vessel_result.get("selected_vessel_result_id")),
        OUTCOME_BRIEF_RENDERED,
    )
    result = {
        "operator_terminal_brief_metadata": metadata,
        "selected_vessel_result": dict(selected_vessel_result),
        "brief_request": dict(brief_request),
        "brief_output": _brief_output_section(brief_text),
        "outcome": OUTCOME_BRIEF_RENDERED,
        "block": {"block_code": None, "block_reason": None},
        "brief_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["brief_summary"] = _summary_from_result(result)
    return result


def resolve_operator_terminal_brief(
    source_result_path: Path | str | None = None,
) -> dict[str, Any]:
    """Resolve one shell-owned bounded operator-facing terminal brief."""

    selected_vessel_result = _empty_selected_vessel_result()
    brief_request: dict[str, Any] | None = None

    try:
        normalized_source_result_path = _normalized_source_result_path(source_result_path)
        selected_vessel_result = _empty_selected_vessel_result(
            normalized_source_result_path
        )
        resolved_source_result_path, source_result_artifact = _select_source_result_artifact(
            normalized_source_result_path
        )
        selected_vessel_result = _selected_vessel_result_from_artifact(
            source_result_artifact,
            resolved_source_result_path,
        )
        brief_request = build_operator_terminal_brief_request(
            source_result_artifact,
            resolved_source_result_path,
        )
        brief_text = _render_operator_terminal_brief(brief_request)
        return _rendered_result(
            selected_vessel_result=selected_vessel_result,
            brief_request=brief_request,
            brief_text=brief_text,
        )
    except OperatorTerminalBriefError as exc:
        block_code = exc.block_code or "MALFORMED_BRIEF_PACKET"
        return _refused_result(
            block_code=block_code,
            block_detail=str(exc),
            selected_vessel_result=selected_vessel_result,
            brief_request=brief_request,
        )


def build_operator_terminal_brief_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a small inspection-friendly summary of one brief result."""

    if not isinstance(result, Mapping):
        raise OperatorTerminalBriefError("brief result must be a mapping")
    return _summary_from_result(result)


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = OPERATOR_TERMINAL_BRIEF_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_vessel_result", {})
    selected = selected if isinstance(selected, Mapping) else {}
    stem = _safe_filename_part(selected.get("selected_vessel_result_id"))
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise OperatorTerminalBriefError(
        "no bounded terminal brief filename is available",
        "MALFORMED_BRIEF_PACKET",
    )


def write_operator_terminal_brief_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded operator terminal brief result JSON artifact."""

    if not isinstance(result, Mapping):
        raise OperatorTerminalBriefError("brief result must be a mapping")

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"operator terminal brief result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
