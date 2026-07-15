"""Run one bounded OpenAI API derivative read over one current-state surface.

This module implements the first repo-local OpenAI API vessel slice for the
closed v0 body:

- one shell-owned bounded derivative read
- over one already-standing current-state surface
- with the model acting only as a derivative reader/operator over one bounded
  packet

The shell remains the law. The model does not own source selection, source
family, provenance, rank, status, refusal law, non-claims, or result wrapping.
"""

from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping

try:
    from openai import OpenAI
except ImportError as exc:  # pragma: no cover - handled explicitly at runtime
    OpenAI = None  # type: ignore[assignment]
    _OPENAI_IMPORT_ERROR = exc
else:
    _OPENAI_IMPORT_ERROR = None


class OpenAIDerivativeVesselError(RuntimeError):
    """Raised for bounded vessel setup, source, packet, or output failures."""

    def __init__(self, message: str, block_code: str | None = None) -> None:
        super().__init__(message)
        self.block_code = block_code


CURRENT_STATE_WHAT_STANDS_NOW_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_current_state_what_stands_now"
)
OPENAI_API_DERIVATIVE_VESSEL_ROOT = Path(
    "artifacts/openai_api_derivative_vessel__bounded_current_state_read"
)

ALLOWED_SOURCE_FAMILY = "current_state_what_stands_now_result"
SUPPORTED_USE_CLASS = "BOUNDED_DERIVATIVE_READ"
VESSEL_USE_CASE = "BOUNDED_CURRENT_STATE_READ"
MODEL_REFUSAL_CODE = "INSUFFICIENT_GROUNDING"

OUTCOME_ANSWERED_DERIVATIVE_READ = "ANSWERED_DERIVATIVE_READ"
OUTCOME_REFUSED = "REFUSED"

SOURCE_OUTCOME_ANSWERED = "ANSWERED_WHAT_STANDS_NOW"

DEFAULT_MODEL = "gpt-5.4-mini"
DEFAULT_QUESTION = "What stands now?"
MAX_OUTPUT_TOKENS = 160

RESOLVER_MODULE = "openai_api_vessel__bounded_current_state_read"
VESSEL_RESULT_TYPE = (
    "IAMMAI_OPENAI_API_DERIVATIVE_VESSEL_BOUNDED_CURRENT_STATE_READ_RESULT"
)
VESSEL_RESULT_VERSION = "0.1.0"
DEFAULT_RESULT_STEM = "bounded_current_state_vessel_result"

REQUIRED_PAYLOAD_FIELDS = (
    "current_governing_source_run_path",
    "current_governing_ingress_run_path",
    "current_authority_artifact_path",
    "preserved_run_count",
    "application_basis",
    "delivery_basis",
    "answer_read_basis",
)

NON_CLAIM_DEFAULTS = {
    "source_replaced": False,
    "rank_assigned_by_model": False,
    "authority_assigned_by_model": False,
    "status_assigned_by_model": False,
    "standing_assigned_by_model": False,
    "provenance_assigned_by_model": False,
    "source_scope_widened": False,
    "continuity_completed": False,
}

BLOCK_REASONS = {
    "INVALID_SOURCE_FAMILY": (
        "The selected source artifact is outside the bounded allowed source family."
    ),
    "MISSING_SOURCE_ARTIFACT": (
        "No readable answered what-stands-now source artifact is available."
    ),
    "SOURCE_ARTIFACT_UNREADABLE": (
        "The selected source artifact could not be read."
    ),
    "SOURCE_ARTIFACT_MALFORMED": (
        "The selected source artifact is malformed."
    ),
    "SOURCE_ARTIFACT_NOT_SUCCESSFUL": (
        "The selected source artifact does not have outcome ANSWERED_WHAT_STANDS_NOW."
    ),
    "UNSUPPORTED_USE_CLASS": (
        "The vessel request use class is outside the bounded supported model."
    ),
    "MALFORMED_VESSEL_PACKET": (
        "The bounded vessel request packet is malformed."
    ),
    "LOCAL_SETUP_FAILURE": (
        "The local OpenAI runtime setup is missing or incomplete."
    ),
    "API_CALL_FAILURE": "The OpenAI API call failed.",
    "MODEL_OUTPUT_MALFORMED": "The model output is malformed.",
    "MODEL_OUTPUT_OUTSIDE_CONTRACT": (
        "The model output falls outside the bounded allowed contract."
    ),
    "WIDENED_SOURCE_ATTEMPT": (
        "The vessel attempted to widen source scope beyond the bounded payload."
    ),
    MODEL_REFUSAL_CODE: (
        "The model reported insufficient grounding for the bounded payload."
    ),
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
        value = "no_selected_source_surface"
    compact = re.sub(r"[^A-Za-z0-9_.-]+", "_", value).strip("._")
    return compact[:160] or "no_selected_source_surface"


def _string_or_none(value: Any) -> str | None:
    if not isinstance(value, str):
        return None
    stripped = value.strip()
    return stripped or None


def _int_or_none(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _require_mapping(value: Any, context: str) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise OpenAIDerivativeVesselError(
            f"{context} must be an object",
            "SOURCE_ARTIFACT_MALFORMED",
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
        raise OpenAIDerivativeVesselError(
            f"{context} not found: {resolved}",
            missing_code,
        ) from exc
    except OSError as exc:
        raise OpenAIDerivativeVesselError(
            f"{context} is unreadable: {resolved}",
            unreadable_code,
        ) from exc
    except json.JSONDecodeError as exc:
        raise OpenAIDerivativeVesselError(
            f"{context} is malformed JSON: {resolved}",
            malformed_code,
        ) from exc
    if not isinstance(value, dict):
        raise OpenAIDerivativeVesselError(
            f"{context} must be a JSON object: {resolved}",
            malformed_code,
        )
    return value


def _empty_selected_source_surface(
    source_path: Path | str | None = None,
) -> dict[str, Any]:
    return {
        "selected_source_surface_path": _display_path(source_path),
        "selected_source_surface_id": None,
        "selected_source_surface_family": None,
        "selected_source_surface_outcome": None,
    }


def _normalized_source_path(source_path: Path | str | None) -> Path | str | None:
    if source_path is None:
        return None
    if isinstance(source_path, (Path, str)):
        return source_path
    raise OpenAIDerivativeVesselError(
        "source_path must be a string, Path, or None",
        "MALFORMED_VESSEL_PACKET",
    )


def _source_family_from_artifact(artifact: Mapping[str, Any]) -> str | None:
    metadata = artifact.get("what_stands_now_metadata")
    if isinstance(metadata, Mapping):
        return ALLOWED_SOURCE_FAMILY
    return None


def _selected_source_surface_from_artifact(
    artifact: Mapping[str, Any],
    path: Path | str | None,
) -> dict[str, Any]:
    metadata = artifact.get("what_stands_now_metadata")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    family = _source_family_from_artifact(artifact)
    return {
        "selected_source_surface_path": _display_path(path),
        "selected_source_surface_id": _string_or_none(
            metadata.get("what_stands_now_result_id")
        ),
        "selected_source_surface_family": family,
        "selected_source_surface_outcome": _string_or_none(artifact.get("outcome")),
    }


def _validate_source_artifact(
    artifact: Mapping[str, Any],
) -> None:
    family = _source_family_from_artifact(artifact)
    if family != ALLOWED_SOURCE_FAMILY:
        raise OpenAIDerivativeVesselError(
            "selected source artifact is not a current_state_what_stands_now_result",
            "INVALID_SOURCE_FAMILY",
        )

    metadata = _require_mapping(
        artifact.get("what_stands_now_metadata"),
        "what-stands-now metadata",
    )
    for key in (
        "what_stands_now_result_id",
        "what_stands_now_result_type",
        "what_stands_now_result_version",
    ):
        if _string_or_none(metadata.get(key)) is None:
            raise OpenAIDerivativeVesselError(
                f"selected source metadata {key} is malformed",
                "SOURCE_ARTIFACT_MALFORMED",
            )

    outcome = _string_or_none(artifact.get("outcome"))
    if outcome is None:
        raise OpenAIDerivativeVesselError(
            "selected source artifact outcome is missing",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    if outcome != SOURCE_OUTCOME_ANSWERED:
        raise OpenAIDerivativeVesselError(
            "selected source artifact is not an answered what-stands-now result",
            "SOURCE_ARTIFACT_NOT_SUCCESSFUL",
        )

    answer = artifact.get("what_stands_now_answer")
    if not isinstance(answer, Mapping):
        raise OpenAIDerivativeVesselError(
            "selected source artifact what_stands_now_answer is malformed",
            "SOURCE_ARTIFACT_MALFORMED",
        )
    _require_mapping(
        artifact.get("what_stands_now_summary"),
        "what-stands-now summary",
    )
    block = artifact.get("block")
    if not isinstance(block, Mapping):
        raise OpenAIDerivativeVesselError(
            "selected source artifact block section is malformed",
            "SOURCE_ARTIFACT_MALFORMED",
        )


def _discover_latest_answered_source() -> tuple[Path | None, dict[str, Any] | None]:
    root = _repo_path(CURRENT_STATE_WHAT_STANDS_NOW_ROOT)
    if not root.exists():
        return None, None
    if not root.is_dir():
        raise OpenAIDerivativeVesselError(
            f"what-stands-now root is not a directory: {root}",
            "SOURCE_ARTIFACT_UNREADABLE",
        )
    try:
        candidates = sorted(path for path in root.glob("*.json") if path.is_file())
    except OSError as exc:
        raise OpenAIDerivativeVesselError(
            f"what-stands-now root is unreadable: {root}",
            "SOURCE_ARTIFACT_UNREADABLE",
        ) from exc

    for path in reversed(candidates):
        try:
            artifact = _read_json_file(
                path,
                context="discovered what-stands-now artifact",
                missing_code="MISSING_SOURCE_ARTIFACT",
                unreadable_code="SOURCE_ARTIFACT_UNREADABLE",
                malformed_code="SOURCE_ARTIFACT_MALFORMED",
            )
            _validate_source_artifact(artifact)
        except OpenAIDerivativeVesselError:
            continue
        return path, artifact
    return None, None


def _select_source_artifact(
    source_path: Path | str | None,
) -> tuple[Path, dict[str, Any]]:
    if source_path is not None:
        artifact = _read_json_file(
            source_path,
            context="selected source artifact",
            missing_code="MISSING_SOURCE_ARTIFACT",
            unreadable_code="SOURCE_ARTIFACT_UNREADABLE",
            malformed_code="SOURCE_ARTIFACT_MALFORMED",
        )
        _validate_source_artifact(artifact)
        return _repo_path(source_path), artifact

    discovered_path, artifact = _discover_latest_answered_source()
    if discovered_path is None or artifact is None:
        raise OpenAIDerivativeVesselError(
            "no answered what-stands-now artifact is available",
            "MISSING_SOURCE_ARTIFACT",
        )
    return discovered_path, artifact


def _extract_bounded_source_payload(
    artifact: Mapping[str, Any],
) -> dict[str, Any]:
    answer = artifact.get("what_stands_now_answer")
    answer = answer if isinstance(answer, Mapping) else {}
    summary = artifact.get("what_stands_now_summary")
    summary = summary if isinstance(summary, Mapping) else {}
    inputs = artifact.get("effective_stand_now_inputs")
    inputs = inputs if isinstance(inputs, Mapping) else {}

    payload = {
        "current_governing_source_run_path": (
            _string_or_none(answer.get("current_governing_source_run_path"))
            or _string_or_none(summary.get("effective_current_governing_source_run_path"))
        ),
        "current_governing_ingress_run_path": (
            _string_or_none(answer.get("current_governing_ingress_run_path"))
            or _string_or_none(
                summary.get("effective_current_governing_ingress_run_path")
            )
        ),
        "current_authority_artifact_path": (
            _string_or_none(answer.get("current_authority_artifact_path"))
            or _string_or_none(inputs.get("effective_authority_artifact_path"))
        ),
        "preserved_run_count": _int_or_none(answer.get("preserved_run_count")),
        "application_basis": _string_or_none(answer.get("application_basis")),
        "delivery_basis": _string_or_none(answer.get("delivery_basis")),
        "answer_read_basis": _string_or_none(answer.get("answer_read_basis")),
    }
    return payload


def _normalized_question(question: str) -> str:
    if not isinstance(question, str):
        raise OpenAIDerivativeVesselError(
            "question must be a string",
            "MALFORMED_VESSEL_PACKET",
        )
    normalized = question.strip()
    if not normalized:
        raise OpenAIDerivativeVesselError(
            "question must be non-empty",
            "MALFORMED_VESSEL_PACKET",
        )
    return normalized


def _vessel_instructions() -> str:
    return (
        "Read only the bounded_source_payload in the provided JSON input. "
        "Do not use hidden context. Do not widen source scope. Do not assign "
        "rank, authority, provenance, status, or non-claims. Return only one "
        "JSON object with exactly one of these shapes: "
        '{"answer": "<string>"} or '
        '{"refusal_code": "INSUFFICIENT_GROUNDING"}.'
    )


def build_bounded_current_state_vessel_request(
    source_artifact: Mapping[str, Any],
    source_path: Path | str,
    question: str = DEFAULT_QUESTION,
) -> dict[str, Any]:
    """Build one bounded shell-owned vessel request packet."""

    _validate_source_artifact(source_artifact)
    normalized_question = _normalized_question(question)
    selected_source = _selected_source_surface_from_artifact(source_artifact, source_path)
    selected_id = _string_or_none(selected_source.get("selected_source_surface_id"))
    if selected_id is None:
        raise OpenAIDerivativeVesselError(
            "selected source surface id is missing",
            "MALFORMED_VESSEL_PACKET",
        )

    packet = {
        "vessel_request_id": f"{selected_id}__bounded_current_state_read_request",
        "vessel_use_case": VESSEL_USE_CASE,
        "admitted_use_class": SUPPORTED_USE_CLASS,
        "allowed_source_family": ALLOWED_SOURCE_FAMILY,
        "selected_source_surface_id": selected_id,
        "selected_source_surface_path": selected_source["selected_source_surface_path"],
        "question": normalized_question,
        "bounded_source_payload": _extract_bounded_source_payload(source_artifact),
        "instructions": _vessel_instructions(),
    }
    _validate_vessel_request(packet)
    return packet


def _validate_vessel_request(packet: Mapping[str, Any]) -> None:
    if not isinstance(packet, Mapping):
        raise OpenAIDerivativeVesselError(
            "vessel request must be a mapping",
            "MALFORMED_VESSEL_PACKET",
        )
    required = {
        "vessel_request_id",
        "vessel_use_case",
        "admitted_use_class",
        "allowed_source_family",
        "selected_source_surface_id",
        "selected_source_surface_path",
        "question",
        "bounded_source_payload",
        "instructions",
    }
    if set(packet) != required:
        raise OpenAIDerivativeVesselError(
            "vessel request shape is malformed",
            "MALFORMED_VESSEL_PACKET",
        )
    for key in (
        "vessel_request_id",
        "selected_source_surface_id",
        "selected_source_surface_path",
        "question",
        "instructions",
    ):
        if _string_or_none(packet.get(key)) is None:
            raise OpenAIDerivativeVesselError(
                f"vessel request {key} must be non-empty",
                "MALFORMED_VESSEL_PACKET",
            )
    if packet.get("vessel_use_case") != VESSEL_USE_CASE:
        raise OpenAIDerivativeVesselError(
            "unsupported vessel use case",
            "MALFORMED_VESSEL_PACKET",
        )
    if packet.get("admitted_use_class") != SUPPORTED_USE_CLASS:
        raise OpenAIDerivativeVesselError(
            "unsupported use class",
            "UNSUPPORTED_USE_CLASS",
        )
    if packet.get("allowed_source_family") != ALLOWED_SOURCE_FAMILY:
        raise OpenAIDerivativeVesselError(
            "vessel request widened source family",
            "WIDENED_SOURCE_ATTEMPT",
        )
    payload = packet.get("bounded_source_payload")
    if not isinstance(payload, Mapping):
        raise OpenAIDerivativeVesselError(
            "bounded_source_payload must be an object",
            "MALFORMED_VESSEL_PACKET",
        )
    if set(payload) != set(REQUIRED_PAYLOAD_FIELDS):
        raise OpenAIDerivativeVesselError(
            "bounded_source_payload shape is malformed",
            "MALFORMED_VESSEL_PACKET",
        )
    for key in (
        "current_governing_source_run_path",
        "current_governing_ingress_run_path",
        "current_authority_artifact_path",
        "application_basis",
        "delivery_basis",
        "answer_read_basis",
    ):
        value = payload.get(key)
        if value is not None and not isinstance(value, str):
            raise OpenAIDerivativeVesselError(
                f"bounded_source_payload {key} must be string-or-null",
                "MALFORMED_VESSEL_PACKET",
            )
    preserved_run_count = payload.get("preserved_run_count")
    if preserved_run_count is not None and not (
        isinstance(preserved_run_count, int) and not isinstance(preserved_run_count, bool)
    ):
        raise OpenAIDerivativeVesselError(
            "bounded_source_payload preserved_run_count must be integer-or-null",
            "MALFORMED_VESSEL_PACKET",
        )


def _initial_api_runtime() -> dict[str, Any]:
    model_override = _string_or_none(os.getenv("OPENAI_MODEL"))
    api_key = _string_or_none(os.getenv("OPENAI_API_KEY"))
    return {
        "model_name_used": model_override or DEFAULT_MODEL,
        "explicit_model_env_override_used": model_override is not None,
        "local_setup_present": False,
        "openai_package_present": OpenAI is not None,
        "api_key_present": api_key is not None,
    }


def _build_openai_client() -> tuple[Any, dict[str, Any]]:
    runtime = _initial_api_runtime()
    if OpenAI is None:
        detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR is not None else None
        raise OpenAIDerivativeVesselError(
            f"openai package is unavailable in the local environment: {detail}",
            "LOCAL_SETUP_FAILURE",
        )
    api_key = _string_or_none(os.getenv("OPENAI_API_KEY"))
    if api_key is None:
        raise OpenAIDerivativeVesselError(
            "OPENAI_API_KEY is missing from the local environment",
            "LOCAL_SETUP_FAILURE",
        )
    client = OpenAI(api_key=api_key)
    if not hasattr(client, "responses") or not callable(getattr(client.responses, "create", None)):
        raise OpenAIDerivativeVesselError(
            "installed openai client does not support the Responses API",
            "LOCAL_SETUP_FAILURE",
        )
    runtime["local_setup_present"] = True
    return client, runtime


def _model_input_text(packet: Mapping[str, Any]) -> str:
    input_packet = {
        "vessel_use_case": packet["vessel_use_case"],
        "admitted_use_class": packet["admitted_use_class"],
        "allowed_source_family": packet["allowed_source_family"],
        "selected_source_surface_id": packet["selected_source_surface_id"],
        "selected_source_surface_path": packet["selected_source_surface_path"],
        "question": packet["question"],
        "bounded_source_payload": packet["bounded_source_payload"],
    }
    return json.dumps(input_packet, indent=2, sort_keys=True)


def _call_openai_derivative_read(
    client: Any,
    packet: Mapping[str, Any],
    model_name: str,
) -> str:
    try:
        response = client.responses.create(
            model=model_name,
            instructions=str(packet["instructions"]),
            input=_model_input_text(packet),
            max_output_tokens=MAX_OUTPUT_TOKENS,
        )
    except Exception as exc:  # pragma: no cover - network/runtime dependent
        raise OpenAIDerivativeVesselError(
            f"OpenAI API call failed: {exc}",
            "API_CALL_FAILURE",
        ) from exc

    raw_text = getattr(response, "output_text", None)
    if not isinstance(raw_text, str) or not raw_text.strip():
        raise OpenAIDerivativeVesselError(
            "OpenAI API did not return bounded output text",
            "MODEL_OUTPUT_MALFORMED",
        )
    return raw_text.strip()


def _validate_model_output(raw_text: str) -> dict[str, Any]:
    if not isinstance(raw_text, str) or not raw_text.strip():
        raise OpenAIDerivativeVesselError(
            "model output text is empty",
            "MODEL_OUTPUT_MALFORMED",
        )
    try:
        parsed = json.loads(raw_text)
    except json.JSONDecodeError as exc:
        raise OpenAIDerivativeVesselError(
            "model output is not valid JSON",
            "MODEL_OUTPUT_MALFORMED",
        ) from exc
    if not isinstance(parsed, dict):
        raise OpenAIDerivativeVesselError(
            "model output must be a JSON object",
            "MODEL_OUTPUT_MALFORMED",
        )

    keys = set(parsed)
    if keys == {"answer"}:
        answer = parsed.get("answer")
        if not isinstance(answer, str) or not answer.strip():
            raise OpenAIDerivativeVesselError(
                "model answer must be a non-empty string",
                "MODEL_OUTPUT_OUTSIDE_CONTRACT",
            )
        return {"answer": answer.strip()}
    if keys == {"refusal_code"}:
        refusal_code = parsed.get("refusal_code")
        if refusal_code != MODEL_REFUSAL_CODE:
            raise OpenAIDerivativeVesselError(
                "model refusal code is outside the bounded contract",
                "MODEL_OUTPUT_OUTSIDE_CONTRACT",
            )
        return {"refusal_code": MODEL_REFUSAL_CODE}
    raise OpenAIDerivativeVesselError(
        "model output contains widened or unsupported fields",
        "MODEL_OUTPUT_OUTSIDE_CONTRACT",
    )


def _block_reason(block_code: str, detail: str | None = None) -> str:
    base = BLOCK_REASONS.get(block_code, block_code.replace("_", " ").lower() + ".")
    if detail is None or not detail.strip():
        return base
    detail_text = detail.strip()
    if detail_text == base:
        return base
    return f"{base} Detail: {detail_text}"


def _result_id(selected_source_id: str | None, outcome: str) -> str:
    base = selected_source_id or "no_selected_source_surface"
    suffix = (
        "bounded_current_state_read_answered"
        if outcome == OUTCOME_ANSWERED_DERIVATIVE_READ
        else "bounded_current_state_read_refused"
    )
    return f"{base}__{suffix}"


def _model_output_section(
    raw_output_text: str | None = None,
    parsed_output: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    refusal_code = None
    if isinstance(parsed_output, Mapping):
        refusal_code = parsed_output.get("refusal_code")
    return {
        "raw_output_text": raw_output_text,
        "parsed_output": dict(parsed_output) if isinstance(parsed_output, Mapping) else None,
        "refusal_code": refusal_code if isinstance(refusal_code, str) else None,
    }


def _derivative_answer_section(answer: str | None) -> dict[str, Any]:
    return {
        "answer": answer,
        "answer_basis": "bounded_source_payload",
        "source_remains_source": True,
        "model_output_remains_derivative": True,
    }


def _result_metadata(
    selected_source_id: str | None,
    outcome: str,
) -> dict[str, Any]:
    return {
        "vessel_result_id": _result_id(selected_source_id, outcome),
        "vessel_result_type": VESSEL_RESULT_TYPE,
        "vessel_result_version": VESSEL_RESULT_VERSION,
        "generated_at": _now_iso(),
        "resolver_module": RESOLVER_MODULE,
    }


def _summary_from_result(result: Mapping[str, Any]) -> dict[str, Any]:
    selected = result.get("selected_source_surface", {})
    selected = selected if isinstance(selected, Mapping) else {}
    request = result.get("vessel_request", {})
    request = request if isinstance(request, Mapping) else {}
    block = result.get("block", {})
    block = block if isinstance(block, Mapping) else {}
    return {
        "selected_source_surface_id": selected.get("selected_source_surface_id"),
        "allowed_source_family": request.get("allowed_source_family"),
        "question": request.get("question"),
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
    }


def _refused_result(
    *,
    block_code: str,
    block_detail: str | None,
    selected_source_surface: Mapping[str, Any] | None,
    vessel_request: Mapping[str, Any] | None,
    api_runtime: Mapping[str, Any] | None,
    model_output: Mapping[str, Any] | None,
) -> dict[str, Any]:
    selected = (
        dict(selected_source_surface)
        if isinstance(selected_source_surface, Mapping)
        else _empty_selected_source_surface()
    )
    request = dict(vessel_request) if isinstance(vessel_request, Mapping) else {}
    runtime = dict(api_runtime) if isinstance(api_runtime, Mapping) else _initial_api_runtime()
    output = (
        dict(model_output)
        if isinstance(model_output, Mapping)
        else _model_output_section()
    )
    metadata = _result_metadata(
        _string_or_none(selected.get("selected_source_surface_id")),
        OUTCOME_REFUSED,
    )
    result = {
        "openai_api_derivative_vessel_metadata": metadata,
        "selected_source_surface": selected,
        "vessel_request": request,
        "api_runtime": runtime,
        "model_output": output,
        "outcome": OUTCOME_REFUSED,
        "block": {
            "block_code": block_code,
            "block_reason": _block_reason(block_code, block_detail),
        },
        "derivative_answer": _derivative_answer_section(None),
        "vessel_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["vessel_summary"] = _summary_from_result(result)
    return result


def _answered_result(
    *,
    selected_source_surface: Mapping[str, Any],
    vessel_request: Mapping[str, Any],
    api_runtime: Mapping[str, Any],
    raw_output_text: str,
    parsed_output: Mapping[str, Any],
) -> dict[str, Any]:
    metadata = _result_metadata(
        _string_or_none(selected_source_surface.get("selected_source_surface_id")),
        OUTCOME_ANSWERED_DERIVATIVE_READ,
    )
    result = {
        "openai_api_derivative_vessel_metadata": metadata,
        "selected_source_surface": dict(selected_source_surface),
        "vessel_request": dict(vessel_request),
        "api_runtime": dict(api_runtime),
        "model_output": _model_output_section(raw_output_text, parsed_output),
        "outcome": OUTCOME_ANSWERED_DERIVATIVE_READ,
        "block": {"block_code": None, "block_reason": None},
        "derivative_answer": _derivative_answer_section(str(parsed_output["answer"])),
        "vessel_summary": {},
        "non_claims": dict(NON_CLAIM_DEFAULTS),
    }
    result["vessel_summary"] = _summary_from_result(result)
    return result


def resolve_bounded_current_state_read(
    source_path: Path | str | None = None,
    question: str = DEFAULT_QUESTION,
) -> dict[str, Any]:
    """Resolve one shell-owned bounded derivative read over one current-state surface."""

    selected_source_surface = _empty_selected_source_surface()
    vessel_request: dict[str, Any] | None = None
    api_runtime = _initial_api_runtime()
    model_output = _model_output_section()

    try:
        normalized_source_path = _normalized_source_path(source_path)
        selected_source_surface = _empty_selected_source_surface(normalized_source_path)
        normalized_question = _normalized_question(question)
        resolved_source_path, source_artifact = _select_source_artifact(
            normalized_source_path
        )
        selected_source_surface = _selected_source_surface_from_artifact(
            source_artifact,
            resolved_source_path,
        )
        vessel_request = build_bounded_current_state_vessel_request(
            source_artifact,
            resolved_source_path,
            normalized_question,
        )
        client, runtime = _build_openai_client()
        api_runtime.update(runtime)
        raw_output_text = _call_openai_derivative_read(
            client,
            vessel_request,
            str(api_runtime["model_name_used"]),
        )
        parsed_output = _validate_model_output(raw_output_text)
        model_output = _model_output_section(raw_output_text, parsed_output)

        if parsed_output.get("refusal_code") == MODEL_REFUSAL_CODE:
            return _refused_result(
                block_code=MODEL_REFUSAL_CODE,
                block_detail=None,
                selected_source_surface=selected_source_surface,
                vessel_request=vessel_request,
                api_runtime=api_runtime,
                model_output=model_output,
            )

        return _answered_result(
            selected_source_surface=selected_source_surface,
            vessel_request=vessel_request,
            api_runtime=api_runtime,
            raw_output_text=raw_output_text,
            parsed_output=parsed_output,
        )
    except OpenAIDerivativeVesselError as exc:
        block_code = exc.block_code or "MALFORMED_VESSEL_PACKET"
        return _refused_result(
            block_code=block_code,
            block_detail=str(exc),
            selected_source_surface=selected_source_surface,
            vessel_request=vessel_request,
            api_runtime=api_runtime,
            model_output=model_output,
        )


def build_bounded_current_state_vessel_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a small inspection-friendly summary of one vessel result."""

    if not isinstance(result, Mapping):
        raise OpenAIDerivativeVesselError("vessel result must be a mapping")
    return _summary_from_result(result)


def _safe_default_output_path(
    result: Mapping[str, Any],
    root: Path | str = OPENAI_API_DERIVATIVE_VESSEL_ROOT,
) -> Path:
    resolved_root = _repo_path(root)
    selected = result.get("selected_source_surface", {})
    selected = selected if isinstance(selected, Mapping) else {}
    stem = _safe_filename_part(selected.get("selected_source_surface_id"))
    candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}.json"
    if not candidate.exists():
        return candidate
    for index in range(1, 1000):
        candidate = resolved_root / f"{stem}__{DEFAULT_RESULT_STEM}_{index:03d}.json"
        if not candidate.exists():
            return candidate
    raise OpenAIDerivativeVesselError(
        "no bounded vessel filename is available",
        "MALFORMED_VESSEL_PACKET",
    )


def write_bounded_current_state_vessel_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive bounded current-state vessel result JSON artifact."""

    if not isinstance(result, Mapping):
        raise OpenAIDerivativeVesselError("vessel result must be a mapping")

    target = (
        _repo_path(output_path)
        if output_path is not None
        else _safe_default_output_path(result)
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(f"bounded vessel result already exists: {target}")
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target
