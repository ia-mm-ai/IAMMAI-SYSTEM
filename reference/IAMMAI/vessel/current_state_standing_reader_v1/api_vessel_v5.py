#!/usr/bin/env python3
"""
API-backed vessel v5 for current_state_standing_reader_v1.

This additive file keeps the v4 shell architecture intact while making
response extraction more robust and adding one bounded retry for incomplete
JSON fallback output. The model still drafts bounded answer content only.
Local code still owns manifest enforcement, input validation, source
selection, provenance, refusal handling, final packet assembly, and final
output validation.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

try:
    from openai import OpenAI
except Exception as _OPENAI_IMPORT_EXCEPTION:  # pragma: no cover - import guard
    OpenAI = None  # type: ignore[assignment]
else:
    _OPENAI_IMPORT_EXCEPTION = None

from local_harness_v3 import (
    FILE_REFERENCE_RE,
    REPO_ROOT,
    AnswerPlan,
    CurrentStateStandingReaderHarnessV3,
    HarnessError,
    PacketTrace,
)


DEFAULT_OPENAI_MODEL = "gpt-5"
INITIAL_MAX_OUTPUT_TOKENS = 1200
RETRY_MAX_OUTPUT_TOKENS = INITIAL_MAX_OUTPUT_TOKENS * 2
RESPONSE_DUMP_MAX_DEPTH = 6

DRAFT_KEYS = {
    "status",
    "answer",
    "boundedness_note",
    "next_read_paths",
    "refusal_reason",
    "ambiguity_note",
}

# Keep the API-facing schema conservative. Local code remains stricter.
DRAFT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": [
        "status",
        "answer",
        "boundedness_note",
        "next_read_paths",
        "refusal_reason",
        "ambiguity_note",
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
        "boundedness_note": {
            "type": "string",
        },
        "next_read_paths": {
            "type": "array",
            "items": {
                "type": "string",
            },
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
        "ambiguity_note": {
            "type": ["string", "null"],
        },
    },
}

STRUCTURED_SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_standing_reader_v1 vessel.

You are not sovereign.
You are not a lawmaker.
You are not a standing ratifier.
You may only answer from the provided request packet, the selected source paths, and the selected source contents.

Follow these rules:
- Return only the structured draft object requested by the schema.
- Do not assign contract_id, request_id, primary_rank_used, sources_used, or derivative_status.
- Do not invent or widen source provenance.
- Do not mention repo surfaces in answer, boundedness_note, or ambiguity_note unless they are present in the selected source paths or the permitted next-read paths.
- If the provided sources do not support a stronger claim, use insufficient_grounding.
- If the request would require new law, new seam-case judgment, final completion, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
- Keep the answer sober, concise, and derivative.
- Keep next_read_paths within the permitted next-read list only.
"""

FALLBACK_JSON_SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_standing_reader_v1 vessel.

Return only one valid JSON object and nothing else.

You are not sovereign.
You are not a lawmaker.
You may only answer from the provided request packet, the selected source paths, and the selected source contents.
Do not invent or widen provenance.
Do not mention repo surfaces in answer, boundedness_note, or ambiguity_note unless they are present in the selected source paths or the permitted next-read paths.
If the provided sources do not support a stronger claim, use insufficient_grounding.
If the request would require new law, new seam-case judgment, final completion, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
Return JSON with exactly these keys:
- status
- answer
- boundedness_note
- next_read_paths
- refusal_reason
- ambiguity_note
"""


@dataclass(frozen=True)
class ResponseDraftCandidates:
    text_candidates: Tuple[str, ...]
    refusal_candidates: Tuple[str, ...]
    parsed_candidates: Tuple[Any, ...]


class StructuredDraftUnusableError(HarnessError):
    """Raised when structured Responses output is present but unusable as a draft."""


class CurrentStateStandingReaderAPIVesselV5(CurrentStateStandingReaderHarnessV3):
    """API-backed vessel that preserves the v3 local shell as the higher authority."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_EXCEPTION) if _OPENAI_IMPORT_EXCEPTION else "unknown import error"
            raise HarnessError(f"The openai package is required for api_vessel_v5.py: {detail}")

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateStandingReaderAPIVesselV5":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel_v5.py.")

        model = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        if not model.strip():
            raise HarnessError("OPENAI_MODEL, if set, must not be empty.")

        return cls(api_key=api_key, model=model)

    def _get_field(self, value: Any, field_name: str) -> Any:
        if isinstance(value, Mapping):
            return value.get(field_name)
        return getattr(value, field_name, None)

    def _mapping_from_candidate(self, value: Any) -> Optional[Dict[str, Any]]:
        if value is None:
            return None

        if isinstance(value, Mapping):
            return dict(value)

        model_dump = getattr(value, "model_dump", None)
        if callable(model_dump):
            dumped = model_dump(mode="json")
            if isinstance(dumped, Mapping):
                return dict(dumped)

        return None

    def _string_from_candidate(self, value: Any) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, str):
            stripped = value.strip()
            return stripped if stripped else None

        if isinstance(value, Mapping):
            for key in ("text", "value", "refusal"):
                candidate = self._string_from_candidate(value.get(key))
                if candidate:
                    return candidate
            return None

        model_dump = getattr(value, "model_dump", None)
        if callable(model_dump):
            dumped = model_dump(mode="json")
            candidate = self._string_from_candidate(dumped)
            if candidate:
                return candidate

        for attr in ("text", "value", "refusal"):
            candidate = self._string_from_candidate(getattr(value, attr, None))
            if candidate:
                return candidate

        return None

    def _append_unique_string(self, values: List[str], candidate: Optional[str]) -> None:
        if candidate and candidate not in values:
            values.append(candidate)

    def _jsonish_string(self, value: Any) -> Optional[str]:
        if not isinstance(value, str):
            return None
        stripped = value.strip()
        if not stripped:
            return None
        if stripped.startswith("{") or stripped.startswith("["):
            return stripped
        return None

    def _response_dump_json(self, response: Any) -> Any:
        if isinstance(response, (Mapping, list)):
            return response

        model_dump = getattr(response, "model_dump", None)
        if callable(model_dump):
            return model_dump(mode="json")

        dict_method = getattr(response, "dict", None)
        if callable(dict_method):
            return dict_method()

        return None

    def _collect_dump_candidates(
        self,
        value: Any,
        *,
        text_candidates: List[str],
        refusal_candidates: List[str],
        parsed_candidates: List[Any],
        depth: int = 0,
    ) -> None:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return

        if isinstance(value, Mapping):
            item_type = value.get("type")
            if item_type == "output_text":
                self._append_unique_string(text_candidates, self._string_from_candidate(value.get("text")))
            elif item_type == "refusal":
                self._append_unique_string(
                    refusal_candidates, self._string_from_candidate(value.get("refusal"))
                )

            for field_name in ("output_parsed", "parsed"):
                field_value = value.get(field_name)
                if field_value is not None:
                    parsed_candidates.append(field_value)

            for key, child in value.items():
                if key in {"text", "value", "output_text"}:
                    self._append_unique_string(text_candidates, self._jsonish_string(child))
                    if isinstance(child, (Mapping, list)):
                        self._collect_dump_candidates(
                            child,
                            text_candidates=text_candidates,
                            refusal_candidates=refusal_candidates,
                            parsed_candidates=parsed_candidates,
                            depth=depth + 1,
                        )
                    continue

                if key == "refusal":
                    self._append_unique_string(
                        refusal_candidates, self._string_from_candidate(child)
                    )
                    continue

                if isinstance(child, (Mapping, list)):
                    self._collect_dump_candidates(
                        child,
                        text_candidates=text_candidates,
                        refusal_candidates=refusal_candidates,
                        parsed_candidates=parsed_candidates,
                        depth=depth + 1,
                    )
                else:
                    self._append_unique_string(text_candidates, self._jsonish_string(child))
            return

        if isinstance(value, list):
            for child in value:
                if isinstance(child, (Mapping, list)):
                    self._collect_dump_candidates(
                        child,
                        text_candidates=text_candidates,
                        refusal_candidates=refusal_candidates,
                        parsed_candidates=parsed_candidates,
                        depth=depth + 1,
                    )
                else:
                    self._append_unique_string(text_candidates, self._jsonish_string(child))

    def _collect_response_candidates(self, response: Any) -> ResponseDraftCandidates:
        text_candidates: List[str] = []
        refusal_candidates: List[str] = []
        parsed_candidates: List[Any] = []

        self._append_unique_string(
            text_candidates,
            self._string_from_candidate(self._get_field(response, "output_text")),
        )

        for field_name in ("output_parsed", "parsed"):
            candidate = self._get_field(response, field_name)
            if candidate is not None:
                parsed_candidates.append(candidate)

        output_items = self._get_field(response, "output")
        if isinstance(output_items, list):
            for item in output_items:
                item_type = self._get_field(item, "type")
                if item_type == "output_text":
                    self._append_unique_string(
                        text_candidates,
                        self._string_from_candidate(self._get_field(item, "text")),
                    )
                elif item_type == "refusal":
                    self._append_unique_string(
                        refusal_candidates,
                        self._string_from_candidate(self._get_field(item, "refusal")),
                    )

                for field_name in ("output_parsed", "parsed"):
                    candidate = self._get_field(item, field_name)
                    if candidate is not None:
                        parsed_candidates.append(candidate)

                content_items = self._get_field(item, "content")
                if not isinstance(content_items, list):
                    continue

                for content in content_items:
                    content_type = self._get_field(content, "type")
                    if content_type == "output_text":
                        self._append_unique_string(
                            text_candidates,
                            self._string_from_candidate(self._get_field(content, "text")),
                        )
                    elif content_type == "refusal":
                        self._append_unique_string(
                            refusal_candidates,
                            self._string_from_candidate(self._get_field(content, "refusal")),
                        )

                    for field_name in ("output_parsed", "parsed"):
                        candidate = self._get_field(content, field_name)
                        if candidate is not None:
                            parsed_candidates.append(candidate)

        dumped_response = self._response_dump_json(response)
        if dumped_response is not None:
            self._collect_dump_candidates(
                dumped_response,
                text_candidates=text_candidates,
                refusal_candidates=refusal_candidates,
                parsed_candidates=parsed_candidates,
            )

        return ResponseDraftCandidates(
            text_candidates=tuple(text_candidates),
            refusal_candidates=tuple(refusal_candidates),
            parsed_candidates=tuple(parsed_candidates),
        )

    def _try_parse_json_candidates(
        self,
        candidates: Sequence[str],
    ) -> Tuple[Optional[Any], Optional[json.JSONDecodeError]]:
        ordered_candidates: List[str] = []
        saw_jsonish = any(self._jsonish_string(candidate) for candidate in candidates)

        for candidate in candidates:
            stripped = candidate.strip()
            if not stripped:
                continue
            if saw_jsonish and not self._jsonish_string(stripped):
                continue
            if stripped not in ordered_candidates:
                ordered_candidates.append(stripped)

        if len(ordered_candidates) > 1:
            combined = "".join(ordered_candidates).strip()
            if combined and combined not in ordered_candidates:
                ordered_candidates.append(combined)

        last_json_error: Optional[json.JSONDecodeError] = None
        for candidate in ordered_candidates:
            try:
                return json.loads(candidate), None
            except json.JSONDecodeError as exc:
                last_json_error = exc

        return None, last_json_error

    def _try_extract_from_parsed_candidates(
        self,
        candidates: Sequence[Any],
    ) -> Tuple[Optional[Any], Optional[json.JSONDecodeError]]:
        string_candidates: List[str] = []

        for candidate in candidates:
            mapping_candidate = self._mapping_from_candidate(candidate)
            if mapping_candidate is not None:
                return mapping_candidate, None

            string_candidate = self._string_from_candidate(candidate)
            if string_candidate:
                self._append_unique_string(string_candidates, string_candidate)

        return self._try_parse_json_candidates(string_candidates)

    def _response_status(self, response: Any) -> Optional[str]:
        status = self._get_field(response, "status")
        return status if isinstance(status, str) else None

    def _response_incomplete_reason(self, response: Any) -> Optional[str]:
        incomplete_details = self._get_field(response, "incomplete_details")
        reason = self._get_field(incomplete_details, "reason")
        return reason if isinstance(reason, str) else None

    def _is_incomplete_due_to_max_output_tokens(self, response: Any) -> bool:
        return (
            self._response_status(response) == "incomplete"
            and self._response_incomplete_reason(response) == "max_output_tokens"
        )

    def _draft_from_explicit_refusal(self, refusal_text: str) -> Dict[str, Any]:
        lowered = refusal_text.lower()
        status = "refused"
        refusal_reason = "would_require_interpretive_sovereignty"

        source_triggers = (
            "unapproved source",
            "not provided in the sources",
            "outside the provided sources",
            "outside provided sources",
            "outside the approved corpus",
            "cannot access external",
            "cannot access files outside",
            "source not provided",
            "missing source",
            "not in the manifest",
            "manifest",
        )
        mutation_triggers = (
            "update",
            "edit",
            "modify",
            "rewrite",
            "finalize",
            "mutate",
        )
        rank_triggers = (
            "insufficient rank",
            "insufficient rank clarity",
            "rank unclear",
            "without rank",
            "ignore rank",
        )

        if any(trigger in lowered for trigger in source_triggers):
            status = "out_of_scope"
            refusal_reason = "requires_unapproved_sources"
        elif any(trigger in lowered for trigger in mutation_triggers):
            refusal_reason = "would_mutate_or_finalize"
        elif any(trigger in lowered for trigger in rank_triggers):
            refusal_reason = "insufficient_rank_clarity"
        elif "out of scope" in lowered or "outside the scope" in lowered:
            status = "out_of_scope"

        draft = {
            "status": status,
            "answer": "",
            "boundedness_note": "The model returned explicit refusal content, and the shell preserved it conservatively.",
            "next_read_paths": [],
            "refusal_reason": refusal_reason,
            "ambiguity_note": None,
        }
        return self._validate_draft(draft)

    def _extract_structured_draft_payload(self, response: Any) -> Any:
        candidates = self._collect_response_candidates(response)

        payload, text_error = self._try_parse_json_candidates(candidates.text_candidates)
        if payload is not None:
            return payload

        payload, parsed_error = self._try_extract_from_parsed_candidates(candidates.parsed_candidates)
        if payload is not None:
            return payload

        if candidates.refusal_candidates:
            raise StructuredDraftUnusableError(
                "Structured response yielded refusal content instead of a draft object."
            )

        if parsed_error is not None:
            raise StructuredDraftUnusableError(f"Model returned invalid JSON draft: {parsed_error}")
        if text_error is not None:
            raise StructuredDraftUnusableError(f"Model returned invalid JSON draft: {text_error}")

        raise StructuredDraftUnusableError("Structured response yielded no parseable draft payload.")

    def _extract_fallback_draft(self, response: Any) -> Dict[str, Any]:
        candidates = self._collect_response_candidates(response)

        payload, text_error = self._try_parse_json_candidates(candidates.text_candidates)
        if payload is not None:
            return self._validate_draft(payload)

        payload, parsed_error = self._try_extract_from_parsed_candidates(candidates.parsed_candidates)
        if payload is not None:
            return self._validate_draft(payload)

        if candidates.refusal_candidates:
            return self._draft_from_explicit_refusal(candidates.refusal_candidates[0])

        if parsed_error is not None:
            raise HarnessError(f"Fallback model output was not valid JSON: {parsed_error}")
        if text_error is not None:
            raise HarnessError(f"Fallback model output was not valid JSON: {text_error}")

        raise HarnessError("Responses API returned no usable output_text.")

    def _validate_draft(self, payload: Any) -> Dict[str, Any]:
        if not isinstance(payload, dict):
            raise HarnessError("Draft response must be a JSON object.")

        extra_keys = sorted(set(payload.keys()) - DRAFT_KEYS)
        if extra_keys:
            raise HarnessError(f"Draft response contains unsupported fields: {extra_keys}")

        missing_keys = sorted(DRAFT_KEYS - set(payload.keys()))
        if missing_keys:
            raise HarnessError(f"Draft response is missing required fields: {missing_keys}")

        status = payload.get("status")
        if status not in self.config.allowed_statuses:
            raise HarnessError("Draft response status is not allowed.")

        answer = payload.get("answer")
        if not isinstance(answer, str):
            raise HarnessError("Draft response answer must be a string.")

        boundedness_note = payload.get("boundedness_note")
        if not isinstance(boundedness_note, str) or not boundedness_note.strip():
            raise HarnessError("Draft response boundedness_note must be a non-empty string.")

        next_read_paths = payload.get("next_read_paths")
        if not isinstance(next_read_paths, list) or not all(
            isinstance(item, str) and item for item in next_read_paths
        ):
            raise HarnessError("Draft response next_read_paths must be an array of non-empty strings.")

        refusal_reason = payload.get("refusal_reason")
        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise HarnessError("Draft response refusal_reason is not allowed.")

        ambiguity_note = payload.get("ambiguity_note")
        if ambiguity_note is not None and not isinstance(ambiguity_note, str):
            raise HarnessError("Draft response ambiguity_note must be a string or null.")

        if status == "answered":
            if not answer.strip():
                raise HarnessError("Draft answered status must carry a non-empty answer.")
            if refusal_reason is not None:
                raise HarnessError("Draft answered status must not carry a refusal reason.")
        elif status in {"refused", "out_of_scope"}:
            if answer != "":
                raise HarnessError("Draft refused or out_of_scope status must carry an empty answer.")
            if refusal_reason is None:
                raise HarnessError("Draft refused or out_of_scope status must carry a refusal reason.")
        elif status == "insufficient_grounding":
            if not answer.strip():
                raise HarnessError("Draft insufficient_grounding status must carry a non-empty answer.")
            if not isinstance(ambiguity_note, str) or not ambiguity_note.strip():
                raise HarnessError(
                    "Draft insufficient_grounding status must carry a non-empty ambiguity_note."
                )
            if refusal_reason is not None:
                raise HarnessError(
                    "Draft insufficient_grounding status must not carry a refusal reason."
                )

        return {
            "status": status,
            "answer": answer,
            "boundedness_note": boundedness_note,
            "next_read_paths": list(next_read_paths),
            "refusal_reason": refusal_reason,
            "ambiguity_note": ambiguity_note,
        }

    def _normalize_next_read_paths(
        self,
        draft_paths: Sequence[str],
        allowed_paths: Sequence[str],
    ) -> Tuple[str, ...]:
        allowed_set = set(allowed_paths)
        normalized: List[str] = []
        for path in draft_paths:
            if path in allowed_set and path not in normalized:
                normalized.append(path)

        if normalized:
            return tuple(normalized)

        return tuple(allowed_paths)

    def _build_model_input(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        next_read_paths: Sequence[str],
        texts: Mapping[str, str],
    ) -> str:
        payload: List[str] = []
        payload.append("REQUEST_PACKET")
        payload.append(json.dumps(request, indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("SELECTED_SOURCE_PATHS")
        payload.append(json.dumps(list(selected_sources), indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("PERMITTED_NEXT_READ_PATHS")
        payload.append(json.dumps(list(next_read_paths), indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("DRAFT_OUTPUT_SCHEMA")
        payload.append(json.dumps(DRAFT_SCHEMA, indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("SELECTED_SOURCE_CONTENTS")
        for path in selected_sources:
            payload.append(f"=== BEGIN SOURCE: {path} ===")
            payload.append(texts[path])
            payload.append(f"=== END SOURCE: {path} ===")
            payload.append("")
        return "\n".join(payload).strip()

    def _is_structured_output_compatibility_error(self, exc: Exception) -> bool:
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
        model_input: str,
    ) -> Dict[str, Any]:
        response = self._client.responses.create(
            model=self._model,
            instructions=STRUCTURED_SYSTEM_PROMPT,
            input=model_input,
            max_output_tokens=INITIAL_MAX_OUTPUT_TOKENS,
            store=False,
            text={
                "format": {
                    "type": "json_schema",
                    "name": "current_state_standing_reader_v1_draft_v5",
                    "schema": DRAFT_SCHEMA,
                    "strict": True,
                }
            },
        )

        try:
            draft_payload = self._extract_structured_draft_payload(response)
            return self._validate_draft(draft_payload)
        except StructuredDraftUnusableError:
            raise
        except HarnessError as exc:
            raise StructuredDraftUnusableError(str(exc)) from exc

    def _call_model_json_fallback_once(
        self,
        *,
        model_input: str,
        max_output_tokens: int,
    ) -> Any:
        try:
            return self._client.responses.create(
                model=self._model,
                instructions=FALLBACK_JSON_SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=max_output_tokens,
                store=False,
                text={
                    "format": {
                        "type": "json_object",
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API fallback call failed: {exc}") from exc

    def _call_model_json_fallback(
        self,
        *,
        model_input: str,
    ) -> Dict[str, Any]:
        response = self._call_model_json_fallback_once(
            model_input=model_input,
            max_output_tokens=INITIAL_MAX_OUTPUT_TOKENS,
        )

        if self._is_incomplete_due_to_max_output_tokens(response):
            response = self._call_model_json_fallback_once(
                model_input=model_input,
                max_output_tokens=RETRY_MAX_OUTPUT_TOKENS,
            )
            if self._response_status(response) == "incomplete":
                reason = self._response_incomplete_reason(response) or "unknown"
                raise HarnessError(
                    f"Fallback JSON response remained incomplete after one bounded retry: {reason}"
                )

        return self._extract_fallback_draft(response)

    def _call_model_for_draft(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        next_read_paths: Sequence[str],
        texts: Mapping[str, str],
    ) -> Dict[str, Any]:
        model_input = self._build_model_input(
            request=request,
            selected_sources=selected_sources,
            next_read_paths=next_read_paths,
            texts=texts,
        )

        try:
            return self._call_model_structured(model_input=model_input)
        except Exception as exc:
            should_fallback = self._is_structured_output_compatibility_error(exc) or isinstance(
                exc, StructuredDraftUnusableError
            )
            if not should_fallback:
                if isinstance(exc, HarnessError):
                    raise
                raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        return self._call_model_json_fallback(model_input=model_input)

    def _provenance_self_check(self, plan: AnswerPlan) -> PacketTrace:
        if plan.status not in {"answered", "insufficient_grounding"}:
            return PacketTrace(
                consulted_sources=plan.consulted_sources,
                next_read_paths=plan.next_read_paths,
                provenance_ok=True,
                public_note=None,
                debug_note=None,
            )

        if not plan.consulted_sources:
            return PacketTrace(
                consulted_sources=plan.consulted_sources,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A response field exceeded bounded provenance.",
                debug_note="Answered or insufficient-grounding output had no consulted sources.",
            )

        if len(set(plan.consulted_sources)) != len(plan.consulted_sources):
            return PacketTrace(
                consulted_sources=plan.consulted_sources,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A response field exceeded bounded provenance.",
                debug_note="Consulted sources contained duplicates.",
            )

        if any(path not in self.config.allowed_sources for path in plan.consulted_sources):
            return PacketTrace(
                consulted_sources=plan.consulted_sources,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A response field exceeded bounded provenance.",
                debug_note="Consulted sources exceeded the manifest.",
            )

        if any(path not in self.config.allowed_sources for path in plan.next_read_paths):
            return PacketTrace(
                consulted_sources=plan.consulted_sources,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A response field exceeded bounded provenance.",
                debug_note="Next-read paths exceeded the manifest.",
            )

        allowed_path_mentions = set(plan.consulted_sources) | set(plan.next_read_paths)
        text_fields = {
            "answer": plan.answer,
            "boundedness_note": plan.boundedness_note,
            "ambiguity_note": plan.ambiguity_note or "",
        }

        for field_name, text in text_fields.items():
            path_mentions = {
                match.rstrip(".,:;")
                for match in FILE_REFERENCE_RE.findall(text)
            }
            undeclared_paths = sorted(
                path for path in path_mentions if path and path not in allowed_path_mentions
            )
            if undeclared_paths:
                return PacketTrace(
                    consulted_sources=plan.consulted_sources,
                    next_read_paths=plan.next_read_paths,
                    provenance_ok=False,
                    public_note="A response field mentioned an undeclared repo surface.",
                    debug_note=(
                        f"{field_name} mentioned path-like surfaces outside sources_used and "
                        f"next_read_paths: {undeclared_paths}"
                    ),
                )

            class_violations = self._surface_class_violations(text, plan.consulted_sources)
            if class_violations:
                return PacketTrace(
                    consulted_sources=plan.consulted_sources,
                    next_read_paths=plan.next_read_paths,
                    provenance_ok=False,
                    public_note="A response field named a broader surface class than the selected source set supports.",
                    debug_note=f"{field_name} mentioned unsupported surface classes: {class_violations}",
                )

        return PacketTrace(
            consulted_sources=plan.consulted_sources,
            next_read_paths=plan.next_read_paths,
            provenance_ok=True,
            public_note=None,
            debug_note=None,
        )

    def _render_answer_plan(self, request: Mapping[str, Any]) -> AnswerPlan:
        question_class = str(request["question_class"])
        question_text = str(request["question_text"])
        selected_sources = self._select_sources_for_request(question_class, question_text)
        texts = self._read_selected_sources(selected_sources)
        local_next_read_paths = self._next_read_paths(question_class, selected_sources)
        draft = self._call_model_for_draft(
            request=request,
            selected_sources=selected_sources,
            next_read_paths=local_next_read_paths,
            texts=texts,
        )

        normalized_next_read_paths = self._normalize_next_read_paths(
            draft_paths=draft["next_read_paths"],
            allowed_paths=local_next_read_paths,
        )

        return AnswerPlan(
            status=str(draft["status"]),
            answer=str(draft["answer"]),
            primary_rank_used=self._question_primary_rank(question_class),
            consulted_sources=tuple(selected_sources),
            next_read_paths=normalized_next_read_paths,
            refusal_reason=draft["refusal_reason"],
            ambiguity_note=draft["ambiguity_note"],
            boundedness_note=str(draft["boundedness_note"]),
        )


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
        "  python vessel/current_state_standing_reader_v1/api_vessel_v5.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_standing_reader_v1/api_vessel_v5.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    mode = argv[1]
    if mode not in {"answer", "eval"}:
        print_usage()
        return 2

    vessel = CurrentStateStandingReaderAPIVesselV5.from_environment()

    if mode == "answer":
        if len(argv) != 3:
            print_usage()
            return 2
        packet = load_input_packet(argv[2])
        output = vessel.answer_request(packet)
        print(json.dumps(output, indent=2))
        return 0

    if len(argv) != 2:
        print_usage()
        return 2
    return vessel.run_eval()


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except HarnessError as exc:
        print(f"api_vessel_v5 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
