#!/usr/bin/env python3
"""
API-backed vessel v4 for current_state_what_stands_reader_v1.

This additive file preserves the narrowed vessel family while correcting the
remaining contract/output misalignment visible in api_vessel_v3.py. The local
shell remains authoritative over source manifest enforcement, request
validation, source selection, provenance, refusal visibility, final packet
assembly, and output validation. The model remains a bounded derivative
drafting surface only.
"""

from __future__ import annotations

import json
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple

try:
    from openai import OpenAI
except Exception as _OPENAI_IMPORT_ERROR:  # pragma: no cover - import guard
    OpenAI = None  # type: ignore[assignment]
else:
    _OPENAI_IMPORT_ERROR = None

from local_harness import (
    FILE_REFERENCE_RE,
    REPO_ROOT,
    AnswerPlan,
    CurrentStateWhatStandsHarness,
    HarnessError,
)


DEFAULT_OPENAI_MODEL = "gpt-5"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 6
MAX_SUMMARY_OUTPUT_ITEMS = 6
MAX_SUMMARY_CONTENT_ITEMS = 6
MAX_ATTEMPTED_PATHS = 24

SCRIPT_PATH = Path(__file__).resolve()
VESSEL_ROOT = SCRIPT_PATH.parent
DEBUG_ROOT = VESSEL_ROOT / "debug"

DRAFT_KEYS = {
    "status",
    "answer",
    "refusal_reason",
}

DRAFT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "answer",
        "refusal_reason",
    ],
    "properties": {
        "status": {
            "type": "string",
            "enum": [
                "answered",
                "refused",
                "out_of_scope",
                "insufficient_grounding",
            ],
        },
        "answer": {
            "type": "string",
        },
        "refusal_reason": {
            "type": ["string", "null"],
            "enum": [
                "question_class_not_allowed",
                "requires_unapproved_sources",
                "would_require_interpretive_sovereignty",
                "would_mutate_or_finalize",
                "insufficient_rank_clarity",
                None,
            ],
        },
    },
}

STRUCTURED_SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_what_stands_reader_v1 vessel.

You are not sovereign.
You are not a lawmaker.
You are not a standing ratifier.
You may only answer from the provided request packet, selected source paths, and selected source contents.

Follow these rules:
- Return only the structured draft object requested by the schema.
- Do not assign contract_id, request_id, primary_rank_used, sources_used, derivative_status, boundedness_note, next_read_paths, or ambiguity_note.
- Do not invent or widen source provenance.
- In answer text, do not mention repo file paths unless they are in the selected source paths.
- If the provided sources do not support a stronger answer, use insufficient_grounding rather than improvising.
- If the request would require new law, final standing beyond the provided surfaces, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
- Keep the answer sober, concise, and derivative.
"""

FALLBACK_JSON_SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_what_stands_reader_v1 vessel.

Return exactly one valid JSON object and nothing else.

You are not sovereign.
You are not a lawmaker.
You may only answer from the provided request packet, selected source paths, and selected source contents.
Do not invent or widen provenance.
In answer text, do not mention repo file paths unless they are in the selected source paths.
If the provided sources do not support a stronger answer, use insufficient_grounding rather than improvising.
If the request would require new law, final standing beyond the provided surfaces, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
Return JSON with exactly these keys:
- status
- answer
- refusal_reason
"""

INSUFFICIENT_GROUNDING_AMBIGUITY_NOTE = (
    "The selected approved sources were insufficient to support a tighter "
    "answer without exceeding bounded provenance."
)
PROVENANCE_DOWNGRADE_NOTE = (
    "A generated response field exceeded bounded provenance and was downgraded "
    "conservatively."
)

ANSWERED_INTERNAL_STATUSES = {
    "answered",
    "draft",
    "draft_answer",
    "draft_answered",
}
INSUFFICIENT_INTERNAL_STATUSES = {
    "insufficient_grounding",
    "draft_insufficient_grounding",
}
REFUSED_INTERNAL_STATUSES = {
    "refused",
    "draft_refused",
    "refusal",
}
OUT_OF_SCOPE_INTERNAL_STATUSES = {
    "out_of_scope",
    "draft_out_of_scope",
}

JSON_FENCE_RE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)


@dataclass(frozen=True)
class PacketTrace:
    sources_used: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


@dataclass(frozen=True)
class InternalDraft:
    raw_status: Any
    answer: Any
    refusal_reason: Any
    source_path: str


class DraftExtractionError(HarnessError):
    """Raised when a Responses API reply yields no usable bounded draft."""

    def __init__(self, reason: str, diagnostics: Mapping[str, Any]) -> None:
        super().__init__(reason)
        self.reason = reason
        self.diagnostics = dict(diagnostics)


class DraftFinalizationError(HarnessError):
    """Raised when an extracted internal draft cannot be finalized lawfully."""

    def __init__(self, reason: str, diagnostics: Mapping[str, Any]) -> None:
        super().__init__(reason)
        self.reason = reason
        self.diagnostics = dict(diagnostics)


class DraftContractError(HarnessError):
    """Raised when a finalized draft still violates the narrowed vessel contract."""


class CurrentStateWhatStandsAPIVesselV4(CurrentStateWhatStandsHarness):
    """API-backed vessel that keeps the narrowed local shell authoritative."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(f"The openai package is required for api_vessel_v4.py: {detail}")

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAPIVesselV4":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel_v4.py.")

        model = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        if not model.strip():
            raise HarnessError("OPENAI_MODEL, if set, must not be empty.")

        return cls(api_key=api_key, model=model)

    def _get_field(self, value: Any, field_name: str) -> Any:
        if isinstance(value, Mapping):
            return value.get(field_name)
        return getattr(value, field_name, None)

    def _repo_relative(self, path: Path) -> str:
        try:
            return str(path.resolve().relative_to(REPO_ROOT))
        except ValueError:
            return str(path)

    def _response_dump_json(self, response: Any) -> Any:
        if isinstance(response, (Mapping, list)):
            return response

        model_dump = getattr(response, "model_dump", None)
        if callable(model_dump):
            try:
                return model_dump(mode="json")
            except TypeError:
                return model_dump()

        dict_method = getattr(response, "dict", None)
        if callable(dict_method):
            return dict_method()

        return None

    def _mapping_from_candidate(self, value: Any) -> Optional[Dict[str, Any]]:
        if value is None:
            return None

        if isinstance(value, Mapping):
            return dict(value)

        dumped = self._response_dump_json(value)
        if isinstance(dumped, Mapping):
            return dict(dumped)

        return None

    def _strip_code_fence(self, text: str) -> str:
        stripped = text.strip()
        match = JSON_FENCE_RE.fullmatch(stripped)
        if match:
            return match.group(1).strip()
        return stripped

    def _string_from_candidate(self, value: Any) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, str):
            stripped = self._strip_code_fence(value)
            return stripped if stripped else None

        if isinstance(value, Mapping):
            for key in ("text", "value", "output_text", "arguments", "refusal", "content"):
                candidate = self._string_from_candidate(value.get(key))
                if candidate:
                    return candidate
            return None

        dumped = self._response_dump_json(value)
        if dumped is not None and dumped is not value:
            candidate = self._string_from_candidate(dumped)
            if candidate:
                return candidate

        for attr in ("text", "value", "output_text", "arguments", "refusal", "content"):
            candidate = self._string_from_candidate(getattr(value, attr, None))
            if candidate:
                return candidate

        return None

    def _jsonish_string(self, value: Any) -> Optional[str]:
        candidate = self._string_from_candidate(value)
        if not candidate:
            return None

        stripped = candidate.strip()
        if stripped.startswith("{") or stripped.startswith("["):
            return stripped

        return None

    def _internal_draft_from_mapping_candidate(
        self,
        value: Any,
        *,
        source_path: str,
    ) -> Optional[InternalDraft]:
        mapping_candidate = self._mapping_from_candidate(value)
        if mapping_candidate is None:
            return None

        if not DRAFT_KEYS.issubset(mapping_candidate.keys()):
            return None

        return InternalDraft(
            raw_status=mapping_candidate.get("status"),
            answer=mapping_candidate.get("answer"),
            refusal_reason=mapping_candidate.get("refusal_reason"),
            source_path=source_path,
        )

    def _internal_draft_from_json_value(
        self,
        value: Any,
        *,
        source_path: str,
    ) -> Optional[InternalDraft]:
        draft = self._internal_draft_from_mapping_candidate(value, source_path=source_path)
        if draft is not None:
            return draft

        if isinstance(value, list) and len(value) == 1:
            return self._internal_draft_from_json_value(value[0], source_path=source_path)

        return None

    def _parse_json_candidate(
        self,
        value: Any,
        *,
        source_path: str,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[InternalDraft]:
        candidate = self._jsonish_string(value)
        if candidate is None:
            return None

        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError as exc:
            parse_errors.append(exc)
            return None

        return self._internal_draft_from_json_value(parsed, source_path=source_path)

    def _refusal_text_from_candidate(self, value: Any) -> Optional[str]:
        mapping_candidate = self._mapping_from_candidate(value)
        if mapping_candidate is not None:
            item_type = mapping_candidate.get("type")
            if item_type == "refusal":
                refusal_text = self._string_from_candidate(mapping_candidate.get("refusal"))
                if refusal_text:
                    return refusal_text

            if "refusal" in mapping_candidate:
                refusal_text = self._string_from_candidate(mapping_candidate.get("refusal"))
                if refusal_text:
                    return refusal_text

        return self._string_from_candidate(self._get_field(value, "refusal"))

    def _iter_dump_nodes(
        self,
        value: Any,
        *,
        path: str,
        depth: int,
    ) -> Iterable[Tuple[str, Any]]:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return

        yield path, value

        if isinstance(value, Mapping):
            priority_keys = (
                "output_parsed",
                "parsed",
                "output_text",
                "text",
                "arguments",
                "output",
                "content",
                "value",
                "refusal",
            )
            seen: set[str] = set()

            for key in priority_keys:
                if key not in value:
                    continue
                seen.add(key)
                yield from self._iter_dump_nodes(
                    value[key],
                    path=f"{path}.{key}",
                    depth=depth + 1,
                )

            for key, child in value.items():
                if key in seen:
                    continue
                yield from self._iter_dump_nodes(
                    child,
                    path=f"{path}.{key}",
                    depth=depth + 1,
                )
            return

        if isinstance(value, list):
            for index, child in enumerate(value):
                yield from self._iter_dump_nodes(
                    child,
                    path=f"{path}[{index}]",
                    depth=depth + 1,
                )

    def _iter_candidate_nodes(self, response: Any) -> Iterable[Tuple[str, Any]]:
        yielded_paths: set[str] = set()

        def emit(path: str, value: Any) -> Iterable[Tuple[str, Any]]:
            if value is None or path in yielded_paths:
                return ()
            yielded_paths.add(path)
            return ((path, value),)

        for field_name in ("output_parsed", "parsed", "output_text"):
            for item in emit(f"response.{field_name}", self._get_field(response, field_name)):
                yield item

        output_items = self._get_field(response, "output")
        if isinstance(output_items, list):
            for index, output_item in enumerate(output_items):
                base = f"response.output[{index}]"
                for item in emit(base, output_item):
                    yield item

                for field_name in ("output_parsed", "parsed", "text", "arguments", "refusal"):
                    for item in emit(f"{base}.{field_name}", self._get_field(output_item, field_name)):
                        yield item

                content_items = self._get_field(output_item, "content")
                if not isinstance(content_items, list):
                    continue

                for content_index, content_item in enumerate(content_items):
                    content_base = f"{base}.content[{content_index}]"
                    for item in emit(content_base, content_item):
                        yield item

                    for field_name in ("output_parsed", "parsed", "text", "arguments", "refusal"):
                        for item in emit(
                            f"{content_base}.{field_name}",
                            self._get_field(content_item, field_name),
                        ):
                            yield item

        dumped = self._response_dump_json(response)
        if dumped is not None:
            for path, value in self._iter_dump_nodes(dumped, path="dump", depth=0):
                if path in yielded_paths:
                    continue
                yielded_paths.add(path)
                yield path, value

    def _string_or_none(self, value: Any) -> Optional[str]:
        if isinstance(value, str):
            stripped = value.strip()
            return stripped if stripped else None
        return None

    def _response_summary(self, response: Any) -> Dict[str, Any]:
        summary: Dict[str, Any] = {
            "response_id": self._string_or_none(self._get_field(response, "id")),
            "model": self._string_or_none(self._get_field(response, "model")),
            "has_output_text": self._jsonish_string(self._get_field(response, "output_text")) is not None,
            "has_output_parsed": self._get_field(response, "output_parsed") is not None,
            "has_parsed": self._get_field(response, "parsed") is not None,
        }

        output_items = self._get_field(response, "output")
        output_summaries: List[Dict[str, Any]] = []

        if isinstance(output_items, list):
            summary["output_count"] = len(output_items)
            for output_item in output_items[:MAX_SUMMARY_OUTPUT_ITEMS]:
                content_types: List[str] = []
                content_items = self._get_field(output_item, "content")
                if isinstance(content_items, list):
                    for content_item in content_items[:MAX_SUMMARY_CONTENT_ITEMS]:
                        content_types.append(
                            str(self._get_field(content_item, "type") or type(content_item).__name__)
                        )

                output_summaries.append(
                    {
                        "type": str(self._get_field(output_item, "type") or type(output_item).__name__),
                        "status": self._string_or_none(self._get_field(output_item, "status")),
                        "has_output_parsed": self._get_field(output_item, "output_parsed") is not None,
                        "has_parsed": self._get_field(output_item, "parsed") is not None,
                        "content_types": content_types,
                    }
                )
        else:
            summary["output_count"] = 0

        summary["output_items"] = output_summaries

        dumped = self._response_dump_json(response)
        if isinstance(dumped, Mapping):
            summary["top_level_keys"] = sorted(str(key) for key in dumped.keys())[:20]
        else:
            summary["top_level_keys"] = []

        return summary

    def _timestamp_slug(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    def _sanitize_label(self, value: str) -> str:
        return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-") or "unknown"

    def _write_debug_artifact(
        self,
        *,
        request_id: str,
        stage: str,
        payload: Mapping[str, Any],
    ) -> Optional[str]:
        try:
            DEBUG_ROOT.mkdir(parents=True, exist_ok=True)
        except OSError:
            return None

        filename = (
            f"api_vessel_v4_debug__{self._timestamp_slug()}__"
            f"{self._sanitize_label(request_id)}__{self._sanitize_label(stage)}.json"
        )
        artifact_path = DEBUG_ROOT / filename

        body = {
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "builder_path": self._repo_relative(SCRIPT_PATH),
            "request_id": request_id,
            "stage": stage,
            **dict(payload),
            "bounded_note": (
                "This debug artifact is implementation-local extraction/finalization "
                "visibility only. It is not protocol law, standing, or authority."
            ),
        }

        try:
            artifact_path.write_text(json.dumps(body, indent=2) + "\n", encoding="utf-8")
        except OSError:
            return None

        return self._repo_relative(artifact_path)

    def _extraction_error(
        self,
        *,
        request_id: str,
        stage: str,
        reason: str,
        response: Any,
        attempted_paths: Sequence[str],
        parse_errors: Sequence[json.JSONDecodeError],
    ) -> DraftExtractionError:
        parse_error = str(parse_errors[-1]) if parse_errors else None
        diagnostics = {
            "request_id": request_id,
            "reason": reason,
            "stage": stage,
            "response_summary": self._response_summary(response),
            "attempted_paths": list(attempted_paths)[:MAX_ATTEMPTED_PATHS],
            "parse_error": parse_error,
        }
        diagnostics["debug_artifact_path"] = self._write_debug_artifact(
            request_id=request_id,
            stage=f"extraction_{stage}",
            payload=diagnostics,
        )
        return DraftExtractionError(reason, diagnostics)

    def _combined_extraction_error(
        self,
        *,
        request_id: str,
        structured_failure: DraftExtractionError,
        fallback_failure: DraftExtractionError,
    ) -> DraftExtractionError:
        return DraftExtractionError(
            "Structured extraction and fallback extraction both failed.",
            {
                "request_id": request_id,
                "reason": "Structured extraction and fallback extraction both failed.",
                "structured": structured_failure.diagnostics,
                "fallback": fallback_failure.diagnostics,
            },
        )

    def _json_safe_scalar(self, value: Any) -> Any:
        if value is None or isinstance(value, (str, int, float, bool)):
            return value
        return repr(value)

    def _internal_draft_summary(self, internal_draft: InternalDraft) -> Dict[str, Any]:
        answer_length = len(internal_draft.answer) if isinstance(internal_draft.answer, str) else None
        return {
            "source_path": internal_draft.source_path,
            "raw_status": self._json_safe_scalar(internal_draft.raw_status),
            "answer_type": type(internal_draft.answer).__name__,
            "answer_length": answer_length,
            "refusal_reason": self._json_safe_scalar(internal_draft.refusal_reason),
        }

    def _finalization_error(
        self,
        *,
        request_id: str,
        reason: str,
        internal_draft: InternalDraft,
        details: Mapping[str, Any],
    ) -> DraftFinalizationError:
        diagnostics = {
            "request_id": request_id,
            "reason": reason,
            "internal_draft": self._internal_draft_summary(internal_draft),
            "details": dict(details),
        }
        diagnostics["debug_artifact_path"] = self._write_debug_artifact(
            request_id=request_id,
            stage="finalization",
            payload=diagnostics,
        )
        return DraftFinalizationError(reason, diagnostics)

    def _draft_from_explicit_refusal(
        self,
        refusal_text: str,
        *,
        source_path: str,
    ) -> InternalDraft:
        lowered = refusal_text.lower()
        raw_status = "refused"
        refusal_reason = "would_require_interpretive_sovereignty"

        source_triggers = (
            "unapproved source",
            "outside the provided sources",
            "outside provided sources",
            "outside the approved corpus",
            "source not provided",
            "missing source",
            "not in the manifest",
            "manifest",
        )
        mutation_triggers = (
            "update",
            "rewrite",
            "edit",
            "modify",
            "mutate",
            "finalize",
        )
        rank_triggers = (
            "insufficient rank",
            "insufficient rank clarity",
            "rank unclear",
        )

        if any(trigger in lowered for trigger in source_triggers):
            raw_status = "out_of_scope"
            refusal_reason = "requires_unapproved_sources"
        elif any(trigger in lowered for trigger in mutation_triggers):
            refusal_reason = "would_mutate_or_finalize"
        elif any(trigger in lowered for trigger in rank_triggers):
            refusal_reason = "insufficient_rank_clarity"
        elif "out of scope" in lowered or "outside the scope" in lowered:
            raw_status = "out_of_scope"

        return InternalDraft(
            raw_status=raw_status,
            answer="",
            refusal_reason=refusal_reason,
            source_path=source_path,
        )

    def _extract_internal_draft_from_response(
        self,
        response: Any,
        *,
        request_id: str,
        stage: str,
    ) -> InternalDraft:
        parse_errors: List[json.JSONDecodeError] = []
        attempted_paths: List[str] = []
        saw_structured_candidate = False
        refusal_text: Optional[str] = None
        refusal_source_path: Optional[str] = None

        for path, value in self._iter_candidate_nodes(response):
            if path not in attempted_paths:
                attempted_paths.append(path)

            mapping_candidate = self._mapping_from_candidate(value)
            if mapping_candidate is not None:
                saw_structured_candidate = True

            internal_draft = self._internal_draft_from_mapping_candidate(value, source_path=path)
            if internal_draft is not None:
                return internal_draft

            internal_draft = self._parse_json_candidate(
                value,
                source_path=path,
                parse_errors=parse_errors,
            )
            if internal_draft is not None:
                return internal_draft

            candidate_refusal = self._refusal_text_from_candidate(value)
            if candidate_refusal and refusal_text is None:
                refusal_text = candidate_refusal
                refusal_source_path = path

        if refusal_text:
            return self._draft_from_explicit_refusal(
                refusal_text,
                source_path=refusal_source_path or "response.refusal",
            )

        if parse_errors:
            raise self._extraction_error(
                request_id=request_id,
                stage=stage,
                reason="Responses API returned JSON-like content, but it was not valid usable draft JSON.",
                response=response,
                attempted_paths=attempted_paths,
                parse_errors=parse_errors,
            )

        if saw_structured_candidate:
            raise self._extraction_error(
                request_id=request_id,
                stage=stage,
                reason="Responses API returned structured content, but no bounded internal draft was extractable.",
                response=response,
                attempted_paths=attempted_paths,
                parse_errors=parse_errors,
            )

        raise self._extraction_error(
            request_id=request_id,
            stage=stage,
            reason="Responses API returned no usable bounded draft payload.",
            response=response,
            attempted_paths=attempted_paths,
            parse_errors=parse_errors,
        )

    def _normalized_status(self, value: Any) -> Optional[str]:
        if not isinstance(value, str):
            return None
        stripped = value.strip().lower()
        return stripped if stripped else None

    def _finalize_internal_draft(
        self,
        internal_draft: InternalDraft,
        *,
        request_id: str,
    ) -> Dict[str, Any]:
        raw_status = self._normalized_status(internal_draft.raw_status)
        refusal_reason = internal_draft.refusal_reason
        answer = internal_draft.answer

        if raw_status is None:
            raise self._finalization_error(
                request_id=request_id,
                reason="Internal draft status was missing or not a bounded string.",
                internal_draft=internal_draft,
                details={"expected_final_statuses": list(self.config.allowed_statuses)},
            )

        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise self._finalization_error(
                request_id=request_id,
                reason="Internal draft refusal_reason was outside the allowed bounded enum.",
                internal_draft=internal_draft,
                details={"allowed_refusal_reasons": list(self.config.allowed_refusal_reasons)},
            )

        if not isinstance(answer, str):
            raise self._finalization_error(
                request_id=request_id,
                reason="Internal draft answer was not a string.",
                internal_draft=internal_draft,
                details={"answer_type": type(answer).__name__},
            )

        stripped_answer = answer.strip()

        if refusal_reason is None:
            if not stripped_answer:
                raise self._finalization_error(
                    request_id=request_id,
                    reason="Internal draft lacked both refusal_reason and a non-empty answer.",
                    internal_draft=internal_draft,
                    details={},
                )

            if raw_status in ANSWERED_INTERNAL_STATUSES:
                final_status = "answered"
            elif raw_status in INSUFFICIENT_INTERNAL_STATUSES:
                final_status = "insufficient_grounding"
            else:
                raise self._finalization_error(
                    request_id=request_id,
                    reason="Internal draft status could not be lawfully finalized into an answered or insufficient-grounding packet.",
                    internal_draft=internal_draft,
                    details={
                        "allowed_answer_aliases": sorted(ANSWERED_INTERNAL_STATUSES),
                        "allowed_insufficient_aliases": sorted(INSUFFICIENT_INTERNAL_STATUSES),
                    },
                )

            return {
                "status": final_status,
                "answer": answer,
                "refusal_reason": None,
            }

        if answer != "":
            raise self._finalization_error(
                request_id=request_id,
                reason="Internal draft carried refusal_reason but also a non-empty answer.",
                internal_draft=internal_draft,
                details={},
            )

        if raw_status in OUT_OF_SCOPE_INTERNAL_STATUSES or refusal_reason == "requires_unapproved_sources":
            final_status = "out_of_scope"
        elif raw_status in REFUSED_INTERNAL_STATUSES or raw_status == "draft":
            final_status = "refused"
        else:
            raise self._finalization_error(
                request_id=request_id,
                reason="Internal refusal draft could not be lawfully finalized into refused or out-of-scope status.",
                internal_draft=internal_draft,
                details={
                    "allowed_refused_aliases": sorted(REFUSED_INTERNAL_STATUSES),
                    "allowed_out_of_scope_aliases": sorted(OUT_OF_SCOPE_INTERNAL_STATUSES),
                },
            )

        return {
            "status": final_status,
            "answer": "",
            "refusal_reason": refusal_reason,
        }

    def _validate_finalized_draft(self, payload: Any) -> Dict[str, Any]:
        if not isinstance(payload, dict):
            raise DraftContractError("Finalized draft must be a JSON object.")

        extra_keys = sorted(set(payload.keys()) - DRAFT_KEYS)
        if extra_keys:
            raise DraftContractError(f"Finalized draft contains unsupported fields: {extra_keys}")

        missing_keys = sorted(DRAFT_KEYS - set(payload.keys()))
        if missing_keys:
            raise DraftContractError(f"Finalized draft is missing required fields: {missing_keys}")

        status = payload.get("status")
        answer = payload.get("answer")
        refusal_reason = payload.get("refusal_reason")

        if status not in self.config.allowed_statuses:
            raise DraftContractError("Finalized draft status is not allowed by output_packet.schema.json.")

        if not isinstance(answer, str):
            raise DraftContractError("Finalized draft answer must be a string.")

        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise DraftContractError("Finalized draft refusal_reason is not allowed.")

        if status == "answered":
            if not answer.strip():
                raise DraftContractError("Final answered draft must carry a non-empty answer.")
            if refusal_reason is not None:
                raise DraftContractError("Final answered draft must not carry refusal_reason.")
        elif status in {"refused", "out_of_scope"}:
            if answer != "":
                raise DraftContractError("Final refused/out_of_scope draft must carry an empty answer.")
            if refusal_reason is None:
                raise DraftContractError("Final refused/out_of_scope draft must carry refusal_reason.")
        elif status == "insufficient_grounding":
            if not answer.strip():
                raise DraftContractError(
                    "Final insufficient_grounding draft must carry a non-empty answer."
                )
            if refusal_reason is not None:
                raise DraftContractError(
                    "Final insufficient_grounding draft must not carry refusal_reason."
                )

        return {
            "status": status,
            "answer": answer,
            "refusal_reason": refusal_reason,
        }

    def _build_model_input(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        texts: Mapping[str, str],
    ) -> str:
        payload: List[str] = []
        payload.append("REQUEST_PACKET")
        payload.append(json.dumps(request, indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("SELECTED_SOURCE_PATHS")
        payload.append(json.dumps(list(selected_sources), indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("SELECTED_SOURCE_CONTENTS")
        for path in selected_sources:
            payload.append(f"=== BEGIN SOURCE: {path} ===")
            payload.append(texts[path])
            payload.append(f"=== END SOURCE: {path} ===")
            payload.append("")
        return "\n".join(payload).strip()

    def _is_structured_output_compatibility_error(self, exc: Exception) -> bool:
        if isinstance(exc, DraftExtractionError):
            return True

        message = str(exc).lower()
        if "invalid schema for response_format" in message:
            return True
        if "response_format" in message and "schema" in message and "not permitted" in message:
            return True
        if "json_schema" in message and "schema" in message and "invalid" in message:
            return True
        return False

    def _call_model_structured(
        self,
        *,
        request_id: str,
        model_input: str,
    ) -> Dict[str, Any]:
        try:
            response = self._client.responses.create(
                model=self._model,
                instructions=STRUCTURED_SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                store=False,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "current_state_what_stands_reader_v1_draft_v4",
                        "schema": DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        internal_draft = self._extract_internal_draft_from_response(
            response,
            request_id=request_id,
            stage="structured",
        )
        finalized = self._finalize_internal_draft(internal_draft, request_id=request_id)
        return self._validate_finalized_draft(finalized)

    def _call_model_json_fallback(
        self,
        *,
        request_id: str,
        model_input: str,
    ) -> Dict[str, Any]:
        try:
            response = self._client.responses.create(
                model=self._model,
                instructions=FALLBACK_JSON_SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                store=False,
                text={
                    "format": {
                        "type": "json_object",
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API fallback call failed: {exc}") from exc

        internal_draft = self._extract_internal_draft_from_response(
            response,
            request_id=request_id,
            stage="fallback",
        )
        finalized = self._finalize_internal_draft(internal_draft, request_id=request_id)
        return self._validate_finalized_draft(finalized)

    def _call_model_for_draft(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        texts: Mapping[str, str],
    ) -> Dict[str, Any]:
        request_id = str(request["request_id"])
        model_input = self._build_model_input(
            request=request,
            selected_sources=selected_sources,
            texts=texts,
        )

        structured_failure: Optional[DraftExtractionError] = None

        try:
            return self._call_model_structured(
                request_id=request_id,
                model_input=model_input,
            )
        except Exception as exc:
            if not self._is_structured_output_compatibility_error(exc):
                if isinstance(exc, HarnessError):
                    raise
                raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

            if isinstance(exc, DraftExtractionError):
                structured_failure = exc

        try:
            return self._call_model_json_fallback(
                request_id=request_id,
                model_input=model_input,
            )
        except DraftExtractionError as exc:
            if structured_failure is not None:
                raise self._combined_extraction_error(
                    request_id=request_id,
                    structured_failure=structured_failure,
                    fallback_failure=exc,
                ) from exc
            raise

    def _local_ambiguity_note(
        self,
        *,
        status: str,
        downgraded_for_provenance: bool = False,
    ) -> Optional[str]:
        if downgraded_for_provenance:
            return PROVENANCE_DOWNGRADE_NOTE
        if status == "insufficient_grounding":
            return INSUFFICIENT_GROUNDING_AMBIGUITY_NOTE
        return None

    def _local_boundedness_note(
        self,
        *,
        question_class: str,
        status: str,
        downgraded_for_provenance: bool = False,
    ) -> str:
        if downgraded_for_provenance:
            return (
                "This vessel stayed inside its approved source boundary and "
                "downgraded a drifted draft conservatively."
            )
        return self._boundedness_note(question_class, status)

    def _normalize_next_read_paths(
        self,
        draft_status: str,
        question_class: str,
        selected_sources: Sequence[str],
    ) -> Tuple[str, ...]:
        return self._next_read_paths(question_class, selected_sources, draft_status)

    def _provenance_self_check(self, plan: AnswerPlan) -> PacketTrace:
        if len(set(plan.sources_used)) != len(plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_NOTE,
                debug_note="sources_used contained duplicates.",
            )

        if any(path not in self.config.allowed_sources for path in plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_NOTE,
                debug_note="sources_used exceeded the source manifest boundary.",
            )

        if any(path not in self.config.allowed_sources for path in plan.next_read_paths):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_NOTE,
                debug_note="next_read_paths exceeded the source manifest boundary.",
            )

        path_mentions = {
            match.rstrip(".,:;")
            for match in FILE_REFERENCE_RE.findall(plan.answer)
        }
        undeclared_paths = sorted(
            path for path in path_mentions if path and path not in set(plan.sources_used)
        )
        if undeclared_paths:
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_NOTE,
                debug_note=f"answer mentioned disallowed repo surfaces: {undeclared_paths}",
            )

        return PacketTrace(
            sources_used=plan.sources_used,
            next_read_paths=plan.next_read_paths,
            provenance_ok=True,
            public_note=None,
            debug_note=None,
        )

    def _downgraded_insufficient_grounding_plan(
        self,
        *,
        question_class: str,
        selected_sources: Tuple[str, ...],
    ) -> AnswerPlan:
        status = "insufficient_grounding"
        return AnswerPlan(
            status=status,
            answer=(
                "The approved surfaces did not support a tighter derivative answer "
                "without exceeding bounded provenance."
            ),
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._local_boundedness_note(
                question_class=question_class,
                status=status,
                downgraded_for_provenance=True,
            ),
            next_read_paths=self._normalize_next_read_paths(
                draft_status=status,
                question_class=question_class,
                selected_sources=selected_sources,
            ),
            refusal_reason=None,
            ambiguity_note=self._local_ambiguity_note(
                status=status,
                downgraded_for_provenance=True,
            ),
        )

    def _render_answer_plan(self, request: Mapping[str, Any]) -> AnswerPlan:
        question_class = str(request["question_class"])
        question_text = str(request["question_text"])

        if self._is_mutation_request(question_text):
            return self._refusal_plan(
                question_class=question_class,
                status="refused",
                refusal_reason="would_mutate_or_finalize",
            )

        if self._question_mentions_unapproved_sources(question_text):
            return self._refusal_plan(
                question_class=question_class,
                status="out_of_scope",
                refusal_reason="requires_unapproved_sources",
            )

        if self._is_interpretive_sovereignty_request(question_text):
            return self._refusal_plan(
                question_class=question_class,
                status="refused",
                refusal_reason="would_require_interpretive_sovereignty",
            )

        selected_sources = self._choose_sources_for_request(question_class, question_text)
        source_texts = self._read_selected_sources(selected_sources)

        if self._is_insufficient_grounding_request(question_text):
            return self._insufficient_grounding_plan(question_class, selected_sources, source_texts)

        draft = self._call_model_for_draft(
            request=request,
            selected_sources=selected_sources,
            texts=source_texts,
        )

        if draft["status"] in {"refused", "out_of_scope"}:
            return self._refusal_plan(
                question_class=question_class,
                status=str(draft["status"]),
                refusal_reason=str(draft["refusal_reason"]),
            )

        status = str(draft["status"])
        plan = AnswerPlan(
            status=status,
            answer=str(draft["answer"]),
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._local_boundedness_note(
                question_class=question_class,
                status=status,
            ),
            next_read_paths=self._normalize_next_read_paths(
                draft_status=status,
                question_class=question_class,
                selected_sources=selected_sources,
            ),
            refusal_reason=draft["refusal_reason"],
            ambiguity_note=self._local_ambiguity_note(status=status),
        )

        trace = self._provenance_self_check(plan)
        if trace.provenance_ok:
            return plan

        return self._downgraded_insufficient_grounding_plan(
            question_class=question_class,
            selected_sources=selected_sources,
        )

    def _evaluate_output_against_case(
        self,
        *,
        case: Mapping[str, Any],
        output: Mapping[str, Any],
    ) -> List[str]:
        reasons: List[str] = []

        expected_status = case.get("expected_status")
        if output.get("status") != expected_status:
            reasons.append(f"status expected {expected_status!r} but got {output.get('status')!r}")

        expected_primary_rank_used = case.get("expected_primary_rank_used")
        if output.get("primary_rank_used") != expected_primary_rank_used:
            reasons.append(
                "primary_rank_used expected "
                f"{expected_primary_rank_used!r} but got {output.get('primary_rank_used')!r}"
            )

        expected_refusal_reason = case.get("expected_refusal_reason")
        if output.get("refusal_reason") != expected_refusal_reason:
            reasons.append(
                "refusal_reason expected "
                f"{expected_refusal_reason!r} but got {output.get('refusal_reason')!r}"
            )

        actual_sources = output.get("sources_used", [])
        expected_min_sources = case.get("expected_min_sources")
        if not isinstance(expected_min_sources, int):
            reasons.append("expected_min_sources is not an integer in eval case.")
        elif len(actual_sources) < expected_min_sources:
            reasons.append(
                f"sources_used expected at least {expected_min_sources} but got {len(actual_sources)}"
            )

        allowed_subset = case.get("expected_allowed_source_subset")
        if not isinstance(allowed_subset, list) or not all(isinstance(item, str) for item in allowed_subset):
            reasons.append("expected_allowed_source_subset is not a string array in eval case.")
        else:
            allowed_set = set(allowed_subset)
            unexpected_sources = [source for source in actual_sources if source not in allowed_set]
            if unexpected_sources:
                reasons.append(f"sources_used outside expected subset: {unexpected_sources}")

        ambiguity_required = case.get("expected_ambiguity_note_required")
        ambiguity_note = output.get("ambiguity_note")
        if ambiguity_required is True:
            if not isinstance(ambiguity_note, str) or not ambiguity_note.strip():
                reasons.append("ambiguity_note was required but is missing or empty")

        if output.get("derivative_status") != self.config.derivative_status:
            reasons.append(
                "derivative_status expected "
                f"{self.config.derivative_status!r} but got {output.get('derivative_status')!r}"
            )

        return reasons

    def _evaluate_case(self, case: Mapping[str, Any]) -> Tuple[str, List[str]]:
        eval_id = str(case.get("eval_id", "unknown_eval"))
        input_packet = case.get("input_packet")

        try:
            output = self.answer_request(input_packet)
        except DraftExtractionError as exc:
            return eval_id, [
                "failure_class=extraction_failure",
                f"reason={exc.reason}",
                f"diagnostics={json.dumps(exc.diagnostics, sort_keys=True)}",
            ]
        except DraftFinalizationError as exc:
            return eval_id, [
                "failure_class=schema_or_contract_violation",
                f"reason={exc.reason}",
                f"diagnostics={json.dumps(exc.diagnostics, sort_keys=True)}",
            ]
        except DraftContractError as exc:
            return eval_id, [
                "failure_class=schema_or_contract_violation",
                f"reason={exc}",
            ]
        except HarnessError as exc:
            return eval_id, [
                "failure_class=schema_or_contract_violation",
                f"reason={exc}",
            ]
        except Exception as exc:
            return eval_id, [
                "failure_class=other_runtime_failure",
                f"reason={type(exc).__name__}: {exc}",
            ]

        reasons = self._evaluate_output_against_case(case=case, output=output)
        if reasons:
            return eval_id, ["failure_class=schema_or_contract_violation", *reasons]
        return eval_id, []

    def run_eval(self) -> int:
        corpus = self._load_eval_corpus()
        cases = corpus["cases"]
        failures: List[Tuple[str, List[str]]] = []
        extraction_failures = 0
        contract_failures = 0
        runtime_failures = 0

        for case in cases:
            if not isinstance(case, Mapping):
                failures.append(
                    (
                        "unknown_eval",
                        [
                            "failure_class=schema_or_contract_violation",
                            "Eval case is not a JSON object.",
                        ],
                    )
                )
                contract_failures += 1
                continue

            eval_id, reasons = self._evaluate_case(case)
            if not reasons:
                continue

            failures.append((eval_id, reasons))
            first_reason = reasons[0]
            if first_reason == "failure_class=extraction_failure":
                extraction_failures += 1
            elif first_reason == "failure_class=other_runtime_failure":
                runtime_failures += 1
            else:
                contract_failures += 1

        total = len(cases)
        failed = len(failures)
        passed = total - failed

        print(f"Eval summary: total={total} passed={passed} failed={failed}")
        print(
            "Failure classes: "
            f"schema_or_contract_violation={contract_failures} "
            f"extraction_failure={extraction_failures} "
            f"other_runtime_failure={runtime_failures}"
        )

        if failures:
            print("Failed cases:")
            for eval_id, reasons in failures:
                print(f"- {eval_id}")
                for reason in reasons:
                    print(f"  - {reason}")
            return 1

        return 0


def load_input_packet(path_arg: str) -> Any:
    packet_path = Path(path_arg)
    if not packet_path.is_absolute():
        packet_path = (REPO_ROOT / packet_path).resolve()

    try:
        return json.loads(packet_path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise HarnessError(f"Failed to read input packet {packet_path}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise HarnessError(f"Invalid JSON in input packet {packet_path}: {exc}") from exc


def print_usage() -> None:
    usage = (
        "Usage:\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_v4.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_v4.py eval\n"
    )
    print(usage, file=sys.stderr)


def _print_stage_error(prefix: str, exc: Any) -> None:
    print(f"{prefix}: {exc.reason}", file=sys.stderr)
    print(json.dumps(exc.diagnostics, indent=2, ensure_ascii=True), file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    vessel = CurrentStateWhatStandsAPIVesselV4.from_environment()
    mode = argv[1]

    if mode == "answer":
        if len(argv) != 3:
            print_usage()
            return 2
        packet = load_input_packet(argv[2])
        output = vessel.answer_request(packet)
        print(json.dumps(output, indent=2))
        return 0

    if mode == "eval":
        if len(argv) != 2:
            print_usage()
            return 2
        return vessel.run_eval()

    print_usage()
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except DraftExtractionError as exc:
        _print_stage_error("api_vessel_v4 extraction error", exc)
        raise SystemExit(2)
    except DraftFinalizationError as exc:
        _print_stage_error("api_vessel_v4 finalization error", exc)
        raise SystemExit(2)
    except DraftContractError as exc:
        print(f"api_vessel_v4 contract error: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except HarnessError as exc:
        print(f"api_vessel_v4 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
