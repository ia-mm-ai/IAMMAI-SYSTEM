#!/usr/bin/env python3
"""
API-backed vessel v2 for current_state_what_stands_reader_v1.

This additive file keeps the narrowed local shell authoritative while fixing
draft extraction for real Responses API shapes. The model remains a bounded
derivative drafting brain only. Local code still owns manifest enforcement,
input validation, source selection, provenance, refusal visibility, final
packet assembly, and output validation.
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


# Bounded default model string for the narrowed API vessel.
DEFAULT_OPENAI_MODEL = "gpt-5"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 6

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
If the provided sources do not support a stronger answer, use insufficient_grounding.
If the request would require new law, final standing beyond the provided surfaces, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
Return JSON with exactly these keys:
- status
- answer
- refusal_reason
"""

INSUFFICIENT_GROUNDING_AMBIGUITY_NOTE = (
    "The selected approved sources were insufficient to support a single "
    "conclusive answer without exceeding bounded provenance."
)
PROVENANCE_DOWNGRADE_NOTE = (
    "A generated response field exceeded bounded provenance and was downgraded "
    "conservatively."
)


@dataclass(frozen=True)
class PacketTrace:
    sources_used: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


class DraftExtractionError(HarnessError):
    """Raised when a Responses API reply does not yield a usable draft."""


class CurrentStateWhatStandsAPIVesselV2(CurrentStateWhatStandsHarness):
    """API-backed vessel that keeps the narrowed local shell authoritative."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(f"The openai package is required for api_vessel_v2.py: {detail}")

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAPIVesselV2":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel_v2.py.")

        model = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        if not model.strip():
            raise HarnessError("OPENAI_MODEL, if set, must not be empty.")

        return cls(api_key=api_key, model=model)

    def _get_field(self, value: Any, field_name: str) -> Any:
        if isinstance(value, Mapping):
            return value.get(field_name)
        return getattr(value, field_name, None)

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
            for key in ("text", "value", "output_text", "arguments", "refusal"):
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

        for attr in ("text", "value", "output_text", "arguments", "refusal"):
            candidate = self._string_from_candidate(getattr(value, attr, None))
            if candidate:
                return candidate

        return None

    def _draft_from_mapping_candidate(self, value: Any) -> Optional[Dict[str, Any]]:
        mapping_candidate = self._mapping_from_candidate(value)
        if mapping_candidate is None:
            return None

        if not DRAFT_KEYS.issubset(mapping_candidate.keys()):
            return None

        return {key: mapping_candidate.get(key) for key in DRAFT_KEYS}

    def _draft_from_json_value(self, value: Any) -> Optional[Dict[str, Any]]:
        draft = self._draft_from_mapping_candidate(value)
        if draft is not None:
            return draft

        if isinstance(value, list) and len(value) == 1:
            return self._draft_from_json_value(value[0])

        return None

    def _jsonish_string(self, value: Any) -> Optional[str]:
        candidate = self._string_from_candidate(value)
        if not candidate:
            return None

        if candidate.startswith("{") or candidate.startswith("["):
            return candidate

        return None

    def _parse_json_candidate(
        self,
        value: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[Dict[str, Any]]:
        candidate = self._jsonish_string(value)
        if candidate is None:
            return None

        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError as exc:
            parse_errors.append(exc)
            return None

        draft = self._draft_from_json_value(parsed)
        if draft is not None:
            return draft

        return None

    def _extract_direct_parsed_payload(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[Dict[str, Any]]:
        for field_name in ("output_parsed", "parsed"):
            candidate = self._get_field(response, field_name)
            draft = self._draft_from_mapping_candidate(candidate)
            if draft is not None:
                return draft

            draft = self._parse_json_candidate(candidate, parse_errors=parse_errors)
            if draft is not None:
                return draft

        return None

    def _extract_output_text_payload(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[Dict[str, Any]]:
        return self._parse_json_candidate(
            self._get_field(response, "output_text"),
            parse_errors=parse_errors,
        )

    def _extract_output_blocks_payload(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        refusal_text: Optional[str] = None
        output_items = self._get_field(response, "output")
        if not isinstance(output_items, list):
            return None, None

        for item in output_items:
            draft = self._draft_from_mapping_candidate(item)
            if draft is not None:
                return draft, refusal_text

            for field_name in ("output_parsed", "parsed"):
                draft = self._draft_from_mapping_candidate(self._get_field(item, field_name))
                if draft is not None:
                    return draft, refusal_text
                draft = self._parse_json_candidate(
                    self._get_field(item, field_name),
                    parse_errors=parse_errors,
                )
                if draft is not None:
                    return draft, refusal_text

            item_type = self._get_field(item, "type")
            if item_type == "output_text":
                draft = self._parse_json_candidate(item, parse_errors=parse_errors)
                if draft is not None:
                    return draft, refusal_text
            elif item_type == "refusal" and refusal_text is None:
                refusal_text = self._string_from_candidate(self._get_field(item, "refusal"))

            content_items = self._get_field(item, "content")
            if not isinstance(content_items, list):
                continue

            for content in content_items:
                draft = self._draft_from_mapping_candidate(content)
                if draft is not None:
                    return draft, refusal_text

                for field_name in ("output_parsed", "parsed"):
                    draft = self._draft_from_mapping_candidate(self._get_field(content, field_name))
                    if draft is not None:
                        return draft, refusal_text
                    draft = self._parse_json_candidate(
                        self._get_field(content, field_name),
                        parse_errors=parse_errors,
                    )
                    if draft is not None:
                        return draft, refusal_text

                content_type = self._get_field(content, "type")
                if content_type == "output_text":
                    draft = self._parse_json_candidate(content, parse_errors=parse_errors)
                    if draft is not None:
                        return draft, refusal_text
                elif content_type == "refusal" and refusal_text is None:
                    refusal_text = self._string_from_candidate(self._get_field(content, "refusal"))

        return None, refusal_text

    def _extract_from_dumped_response(
        self,
        value: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
        depth: int = 0,
    ) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return None, None

        draft = self._draft_from_mapping_candidate(value)
        if draft is not None:
            return draft, None

        draft = self._parse_json_candidate(value, parse_errors=parse_errors)
        if draft is not None:
            return draft, None

        if isinstance(value, Mapping):
            if value.get("type") == "refusal":
                refusal_text = self._string_from_candidate(value.get("refusal"))
                if refusal_text:
                    return None, refusal_text

            priority_keys = (
                "output_parsed",
                "parsed",
                "output_text",
                "text",
                "output",
                "content",
                "value",
                "arguments",
            )
            seen_keys = set(priority_keys)

            for key in priority_keys:
                if key not in value:
                    continue
                draft, refusal_text = self._extract_from_dumped_response(
                    value[key],
                    parse_errors=parse_errors,
                    depth=depth + 1,
                )
                if draft is not None or refusal_text is not None:
                    return draft, refusal_text

            for key, child in value.items():
                if key in seen_keys:
                    continue
                draft, refusal_text = self._extract_from_dumped_response(
                    child,
                    parse_errors=parse_errors,
                    depth=depth + 1,
                )
                if draft is not None or refusal_text is not None:
                    return draft, refusal_text

            return None, None

        if isinstance(value, list):
            for child in value:
                draft, refusal_text = self._extract_from_dumped_response(
                    child,
                    parse_errors=parse_errors,
                    depth=depth + 1,
                )
                if draft is not None or refusal_text is not None:
                    return draft, refusal_text

        return None, None

    def _draft_from_explicit_refusal(self, refusal_text: str) -> Dict[str, Any]:
        lowered = refusal_text.lower()
        status = "refused"
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
            status = "out_of_scope"
            refusal_reason = "requires_unapproved_sources"
        elif any(trigger in lowered for trigger in mutation_triggers):
            refusal_reason = "would_mutate_or_finalize"
        elif any(trigger in lowered for trigger in rank_triggers):
            refusal_reason = "insufficient_rank_clarity"
        elif "out of scope" in lowered or "outside the scope" in lowered:
            status = "out_of_scope"

        return {
            "status": status,
            "answer": "",
            "refusal_reason": refusal_reason,
        }

    def _extract_structured_draft_payload(self, response: Any) -> Dict[str, Any]:
        parse_errors: List[json.JSONDecodeError] = []

        draft = self._extract_direct_parsed_payload(response, parse_errors=parse_errors)
        if draft is not None:
            return draft

        draft = self._extract_output_text_payload(response, parse_errors=parse_errors)
        if draft is not None:
            return draft

        draft, refusal_text = self._extract_output_blocks_payload(
            response,
            parse_errors=parse_errors,
        )
        if draft is not None:
            return draft
        if refusal_text:
            return self._draft_from_explicit_refusal(refusal_text)

        dumped = self._response_dump_json(response)
        if dumped is not None:
            draft, refusal_text = self._extract_from_dumped_response(
                dumped,
                parse_errors=parse_errors,
            )
            if draft is not None:
                return draft
            if refusal_text:
                return self._draft_from_explicit_refusal(refusal_text)

        if parse_errors:
            raise DraftExtractionError(f"Model returned invalid JSON draft: {parse_errors[-1]}")

        raise DraftExtractionError("Responses API returned no usable draft payload.")

    def _extract_fallback_json_text(self, response: Any) -> str:
        parse_errors: List[json.JSONDecodeError] = []

        draft = self._extract_direct_parsed_payload(response, parse_errors=parse_errors)
        if draft is not None:
            return json.dumps(draft)

        text_candidate = self._jsonish_string(self._get_field(response, "output_text"))
        if text_candidate is not None:
            return text_candidate

        draft, refusal_text = self._extract_output_blocks_payload(
            response,
            parse_errors=parse_errors,
        )
        if draft is not None:
            return json.dumps(draft)
        if refusal_text:
            return json.dumps(self._draft_from_explicit_refusal(refusal_text))

        dumped = self._response_dump_json(response)
        if dumped is not None:
            draft, refusal_text = self._extract_from_dumped_response(
                dumped,
                parse_errors=parse_errors,
            )
            if draft is not None:
                return json.dumps(draft)
            if refusal_text:
                return json.dumps(self._draft_from_explicit_refusal(refusal_text))

        if parse_errors:
            raise HarnessError(f"Fallback model output was not valid JSON: {parse_errors[-1]}")

        raise HarnessError("Responses API returned no usable draft payload.")

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
        answer = payload.get("answer")
        refusal_reason = payload.get("refusal_reason")

        if status not in self.config.allowed_statuses:
            raise HarnessError("Draft response status is not allowed.")

        if not isinstance(answer, str):
            raise HarnessError("Draft response answer must be a string.")

        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise HarnessError("Draft response refusal_reason is not allowed.")

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
            if refusal_reason is not None:
                raise HarnessError("Draft insufficient_grounding status must not carry a refusal reason.")

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

    def _call_model_structured(self, model_input: str) -> Dict[str, Any]:
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
                        "name": "current_state_what_stands_reader_v1_draft_v2",
                        "schema": DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        payload = self._extract_structured_draft_payload(response)
        return self._validate_draft(payload)

    def _call_model_json_fallback(self, model_input: str) -> Dict[str, Any]:
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

        json_text = self._extract_fallback_json_text(response)
        try:
            payload = json.loads(json_text)
        except json.JSONDecodeError as exc:
            raise HarnessError(f"Fallback model output was not valid JSON: {exc}") from exc

        return self._validate_draft(payload)

    def _call_model_for_draft(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        texts: Mapping[str, str],
    ) -> Dict[str, Any]:
        model_input = self._build_model_input(
            request=request,
            selected_sources=selected_sources,
            texts=texts,
        )

        try:
            return self._call_model_structured(model_input)
        except Exception as exc:
            if not self._is_structured_output_compatibility_error(exc):
                if isinstance(exc, HarnessError):
                    raise
                raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        return self._call_model_json_fallback(model_input)

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
                debug_note="sources_used exceeded the manifest boundary.",
            )

        if any(path not in self.config.allowed_sources for path in plan.next_read_paths):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_NOTE,
                debug_note="next_read_paths exceeded the manifest boundary.",
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
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_v2.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_v2.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    vessel = CurrentStateWhatStandsAPIVesselV2.from_environment()
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
    except HarnessError as exc:
        print(f"api_vessel_v2 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
