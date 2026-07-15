#!/usr/bin/env python3
"""
Answer-only API-backed vessel for current_state_what_stands_reader_v1.

This additive file keeps the narrowed local shell sovereign while reducing the
model contract to bounded answer text only. Local code still owns manifest
enforcement, input validation, source selection, refusal and out-of-scope
logic, provenance, rank, notes, next-read pointers, final packet assembly, and
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
except Exception as _OPENAI_IMPORT_ERROR:  # pragma: no cover - import guard
    OpenAI = None  # type: ignore[assignment]
else:
    _OPENAI_IMPORT_ERROR = None

from local_harness import (
    FILE_REFERENCE_RE,
    OUTPUT_KEYS,
    REQUEST_ID_RE,
    REPO_ROOT,
    AnswerPlan,
    CurrentStateWhatStandsHarness,
    HarnessError,
)


# Bounded default model string for the first answer-only narrowed API vessel.
DEFAULT_OPENAI_MODEL = "gpt-5"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 6

ANSWER_DRAFT_SCHEMA: Dict[str, Any] = {
    "type": "object",
    "additionalProperties": False,
    "required": ["answer"],
    "properties": {
        "answer": {
            "type": "string",
        }
    },
}

CURRENT_STATE_NEXT_READ_PATHS = (
    "RANKED_SURFACE_INDEX.md",
    "CURRENT_READABILITY_SURFACES.md",
)
WHAT_STANDS_NOW_NEXT_READ_PATHS = (
    "CURRENT_STATE__REPO_ENTRY.md",
)

INSUFFICIENT_GROUNDING_AMBIGUITY_NOTE = (
    "The selected approved sources were insufficient to support a tighter "
    "answer without exceeding bounded provenance."
)
MODEL_UNUSABLE_AMBIGUITY_NOTE = (
    "The model did not return usable bounded answer text from the selected "
    "approved sources."
)
PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE = (
    "A generated response field exceeded bounded provenance and was downgraded "
    "conservatively."
)

STRUCTURED_SYSTEM_PROMPT = """You are drafting bounded derivative answer text for the IAMMAI current_state_what_stands_reader_v1 vessel.

You are not sovereign.
You are not a lawmaker.
You are not a standing ratifier.
You may only answer from the provided request packet, selected source paths, and selected source contents.

Follow these rules:
- Return only the structured object requested by the schema.
- The only draft field is answer.
- Do not invent or widen provenance.
- Do not mention repo file paths unless they are in the selected source paths.
- Do not claim new law, new standing, total closure, or final standing beyond the provided sources.
- Keep the answer sober, concise, and derivative.
"""

FALLBACK_JSON_SYSTEM_PROMPT = """You are drafting bounded derivative answer text for the IAMMAI current_state_what_stands_reader_v1 vessel.

Return exactly one valid JSON object and nothing else.

You are not sovereign.
You are not a lawmaker.
You may only answer from the provided request packet, selected source paths, and selected source contents.
The only allowed key is answer.
Do not invent or widen provenance.
Do not mention repo file paths unless they are in the selected source paths.
Do not claim new law, new standing, total closure, or final standing beyond the provided sources.
Keep the answer sober, concise, and derivative.
"""


@dataclass(frozen=True)
class PacketTrace:
    sources_used: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


class CurrentStateWhatStandsAnswerOnlyAPIVesselV1(CurrentStateWhatStandsHarness):
    """API-backed vessel that keeps the narrowed local shell authoritative."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(
                f"The openai package is required for api_vessel_answer_only_v1.py: {detail}"
            )

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()
        self._validate_configured_next_read_paths()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAnswerOnlyAPIVesselV1":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel_answer_only_v1.py.")

        model = os.environ.get("OPENAI_MODEL", DEFAULT_OPENAI_MODEL)
        if not model.strip():
            raise HarnessError("OPENAI_MODEL, if set, must not be empty.")

        return cls(api_key=api_key, model=model)

    def _validate_configured_next_read_paths(self) -> None:
        for relative_path in CURRENT_STATE_NEXT_READ_PATHS + WHAT_STANDS_NOW_NEXT_READ_PATHS:
            absolute_path = (REPO_ROOT / relative_path).resolve()
            if not absolute_path.is_file():
                raise HarnessError(
                    f"Configured next-read path does not exist as a file: {relative_path}"
                )

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
            for key in ("text", "value", "output_text", "arguments", "answer"):
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

        for attr in ("text", "value", "output_text", "arguments", "answer"):
            candidate = self._string_from_candidate(getattr(value, attr, None))
            if candidate:
                return candidate

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

    def _normalize_answer_text(self, value: Any) -> Optional[str]:
        if not isinstance(value, str):
            return None
        stripped = value.strip()
        return stripped if stripped else None

    def _answer_from_mapping_candidate(self, value: Any) -> Optional[str]:
        mapping_candidate = self._mapping_from_candidate(value)
        if mapping_candidate is None:
            return None
        return self._normalize_answer_text(mapping_candidate.get("answer"))

    def _answer_from_json_value(self, value: Any) -> Optional[str]:
        answer = self._answer_from_mapping_candidate(value)
        if answer is not None:
            return answer

        if isinstance(value, list) and len(value) == 1:
            return self._answer_from_json_value(value[0])

        return None

    def _jsonish_string(self, value: Any) -> Optional[str]:
        candidate = self._string_from_candidate(value)
        if not candidate:
            return None
        if candidate.startswith("{") or candidate.startswith("["):
            return candidate
        return None

    def _plain_text_from_candidate(self, value: Any) -> Optional[str]:
        candidate = self._string_from_candidate(value)
        if not candidate:
            return None
        if candidate.startswith("{") or candidate.startswith("["):
            return None
        return candidate

    def _parse_answer_json_candidate(
        self,
        value: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[str]:
        candidate = self._jsonish_string(value)
        if candidate is None:
            return None

        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError as exc:
            parse_errors.append(exc)
            return None

        return self._answer_from_json_value(parsed)

    def _answer_from_text_candidate(
        self,
        value: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
        allow_plain_text: bool,
    ) -> Optional[str]:
        answer = self._parse_answer_json_candidate(value, parse_errors=parse_errors)
        if answer is not None:
            return answer

        if allow_plain_text:
            return self._plain_text_from_candidate(value)

        return None

    def _extract_answer_from_parsed_fields(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[str]:
        for field_name in ("output_parsed", "parsed"):
            candidate = self._get_field(response, field_name)
            answer = self._answer_from_mapping_candidate(candidate)
            if answer is not None:
                return answer

            answer = self._answer_from_text_candidate(
                candidate,
                parse_errors=parse_errors,
                allow_plain_text=True,
            )
            if answer is not None:
                return answer

        return None

    def _extract_answer_from_output_text(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[str]:
        return self._answer_from_text_candidate(
            self._get_field(response, "output_text"),
            parse_errors=parse_errors,
            allow_plain_text=True,
        )

    def _extract_answer_from_output_blocks(
        self,
        response: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
    ) -> Optional[str]:
        output_items = self._get_field(response, "output")
        if not isinstance(output_items, list):
            return None

        for item in output_items:
            answer = self._answer_from_mapping_candidate(item)
            if answer is not None:
                return answer

            for field_name in ("output_parsed", "parsed"):
                answer = self._answer_from_mapping_candidate(self._get_field(item, field_name))
                if answer is not None:
                    return answer

                answer = self._answer_from_text_candidate(
                    self._get_field(item, field_name),
                    parse_errors=parse_errors,
                    allow_plain_text=True,
                )
                if answer is not None:
                    return answer

            item_type = self._get_field(item, "type")
            if item_type == "output_text":
                answer = self._answer_from_text_candidate(
                    self._get_field(item, "text"),
                    parse_errors=parse_errors,
                    allow_plain_text=True,
                )
                if answer is not None:
                    return answer

            content_items = self._get_field(item, "content")
            if not isinstance(content_items, list):
                continue

            for content in content_items:
                answer = self._answer_from_mapping_candidate(content)
                if answer is not None:
                    return answer

                for field_name in ("output_parsed", "parsed"):
                    answer = self._answer_from_mapping_candidate(self._get_field(content, field_name))
                    if answer is not None:
                        return answer

                    answer = self._answer_from_text_candidate(
                        self._get_field(content, field_name),
                        parse_errors=parse_errors,
                        allow_plain_text=True,
                    )
                    if answer is not None:
                        return answer

                content_type = self._get_field(content, "type")
                if content_type == "output_text":
                    answer = self._answer_from_text_candidate(
                        self._get_field(content, "text"),
                        parse_errors=parse_errors,
                        allow_plain_text=True,
                    )
                    if answer is not None:
                        return answer

        return None

    def _extract_answer_from_dumped_response(
        self,
        value: Any,
        *,
        parse_errors: List[json.JSONDecodeError],
        depth: int = 0,
    ) -> Optional[str]:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return None

        answer = self._answer_from_mapping_candidate(value)
        if answer is not None:
            return answer

        if isinstance(value, Mapping):
            item_type = value.get("type")
            if item_type == "output_text":
                answer = self._answer_from_text_candidate(
                    value.get("text"),
                    parse_errors=parse_errors,
                    allow_plain_text=True,
                )
                if answer is not None:
                    return answer

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

                child = value[key]
                if key in {"output_text", "text"}:
                    answer = self._answer_from_text_candidate(
                        child,
                        parse_errors=parse_errors,
                        allow_plain_text=True,
                    )
                    if answer is not None:
                        return answer
                elif key in {"output_parsed", "parsed", "value", "arguments"}:
                    answer = self._answer_from_mapping_candidate(child)
                    if answer is not None:
                        return answer
                    answer = self._answer_from_text_candidate(
                        child,
                        parse_errors=parse_errors,
                        allow_plain_text=False,
                    )
                    if answer is not None:
                        return answer

                answer = self._extract_answer_from_dumped_response(
                    child,
                    parse_errors=parse_errors,
                    depth=depth + 1,
                )
                if answer is not None:
                    return answer

            for key, child in value.items():
                if key in seen_keys:
                    continue
                if isinstance(child, (Mapping, list)):
                    answer = self._extract_answer_from_dumped_response(
                        child,
                        parse_errors=parse_errors,
                        depth=depth + 1,
                    )
                    if answer is not None:
                        return answer

            return None

        if isinstance(value, list):
            for child in value:
                answer = self._extract_answer_from_dumped_response(
                    child,
                    parse_errors=parse_errors,
                    depth=depth + 1,
                )
                if answer is not None:
                    return answer

        return None

    def _extract_answer_text(self, response: Any) -> Optional[str]:
        parse_errors: List[json.JSONDecodeError] = []

        answer = self._extract_answer_from_parsed_fields(response, parse_errors=parse_errors)
        if answer is not None:
            return answer

        answer = self._extract_answer_from_output_text(response, parse_errors=parse_errors)
        if answer is not None:
            return answer

        answer = self._extract_answer_from_output_blocks(response, parse_errors=parse_errors)
        if answer is not None:
            return answer

        dumped = self._response_dump_json(response)
        if dumped is not None:
            answer = self._extract_answer_from_dumped_response(
                dumped,
                parse_errors=parse_errors,
            )
            if answer is not None:
                return answer

        return None

    def _extract_fallback_json_text(self, response: Any) -> Optional[str]:
        parse_errors: List[json.JSONDecodeError] = []

        for field_name in ("output_parsed", "parsed"):
            answer = self._answer_from_mapping_candidate(self._get_field(response, field_name))
            if answer is not None:
                return json.dumps({"answer": answer})

        output_text_candidate = self._jsonish_string(self._get_field(response, "output_text"))
        if output_text_candidate is not None:
            return output_text_candidate

        output_items = self._get_field(response, "output")
        if isinstance(output_items, list):
            for item in output_items:
                answer = self._answer_from_mapping_candidate(item)
                if answer is not None:
                    return json.dumps({"answer": answer})

                for field_name in ("output_parsed", "parsed"):
                    answer = self._answer_from_mapping_candidate(self._get_field(item, field_name))
                    if answer is not None:
                        return json.dumps({"answer": answer})

                item_type = self._get_field(item, "type")
                if item_type == "output_text":
                    json_text = self._jsonish_string(self._get_field(item, "text"))
                    if json_text is not None:
                        return json_text

                content_items = self._get_field(item, "content")
                if not isinstance(content_items, list):
                    continue

                for content in content_items:
                    answer = self._answer_from_mapping_candidate(content)
                    if answer is not None:
                        return json.dumps({"answer": answer})

                    for field_name in ("output_parsed", "parsed"):
                        answer = self._answer_from_mapping_candidate(
                            self._get_field(content, field_name)
                        )
                        if answer is not None:
                            return json.dumps({"answer": answer})

                    content_type = self._get_field(content, "type")
                    if content_type == "output_text":
                        json_text = self._jsonish_string(self._get_field(content, "text"))
                        if json_text is not None:
                            return json_text

        dumped = self._response_dump_json(response)
        if dumped is not None:
            answer = self._extract_answer_from_dumped_response(
                dumped,
                parse_errors=parse_errors,
            )
            if answer is not None:
                return json.dumps({"answer": answer})

        return None

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
        message = str(exc).lower()
        if "invalid schema for response_format" in message:
            return True
        if "response_format" in message and "schema" in message and "not permitted" in message:
            return True
        if "json_schema" in message and "schema" in message and "invalid" in message:
            return True
        return False

    def _call_model_structured(self, model_input: str) -> Optional[str]:
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
                        "name": "current_state_what_stands_reader_v1_answer_only_v1",
                        "schema": ANSWER_DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        return self._extract_answer_text(response)

    def _call_model_json_fallback(self, model_input: str) -> Optional[str]:
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
        if json_text is None:
            return None

        try:
            payload = json.loads(json_text)
        except json.JSONDecodeError:
            return None

        return self._answer_from_json_value(payload)

    def _call_model_for_answer_text(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        texts: Mapping[str, str],
    ) -> Optional[str]:
        model_input = self._build_model_input(
            request=request,
            selected_sources=selected_sources,
            texts=texts,
        )

        try:
            answer = self._call_model_structured(model_input)
        except Exception as exc:
            if not self._is_structured_output_compatibility_error(exc):
                if isinstance(exc, HarnessError):
                    raise
                raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc
            answer = None

        if answer is not None:
            return answer

        return self._call_model_json_fallback(model_input)

    def _local_next_read_paths(self, question_class: str, status: str) -> Tuple[str, ...]:
        if status in {"refused", "out_of_scope"}:
            return ()

        if question_class == "current_state":
            return CURRENT_STATE_NEXT_READ_PATHS

        if question_class == "what_stands_now":
            return WHAT_STANDS_NOW_NEXT_READ_PATHS

        raise HarnessError(f"Unhandled question_class for next-read generation: {question_class!r}")

    def _selected_surface_phrase(self, question_class: str, selected_sources: Sequence[str]) -> str:
        if question_class == "current_state":
            if tuple(selected_sources) == ("CURRENT_STATE__REPO_ENTRY.md",):
                return "the selected current-state entry surface"
            return "the selected current-state entry surface and selected standing-review surface"

        if question_class == "what_stands_now":
            return "the selected standing-review surface"

        raise HarnessError(f"Unhandled question_class for boundedness note generation: {question_class!r}")

    def _local_boundedness_note(
        self,
        *,
        question_class: str,
        selected_sources: Sequence[str],
        status: str,
        downgraded_for_provenance: bool = False,
    ) -> str:
        if status == "answered":
            return f"This answer is derived only from {self._selected_surface_phrase(question_class, selected_sources)}."

        if status == "insufficient_grounding":
            if downgraded_for_provenance:
                return (
                    f"This result stayed inside {self._selected_surface_phrase(question_class, selected_sources)} "
                    "and downgraded a drifted draft conservatively."
                )
            return (
                f"This result stayed inside {self._selected_surface_phrase(question_class, selected_sources)} "
                "and returned insufficient grounding rather than counterfeit certainty."
            )

        return self._boundedness_note(question_class, status)

    def _local_ambiguity_note(
        self,
        *,
        downgraded_for_provenance: bool = False,
        model_output_unusable: bool = False,
    ) -> str:
        if downgraded_for_provenance:
            return PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE
        if model_output_unusable:
            return MODEL_UNUSABLE_AMBIGUITY_NOTE
        return INSUFFICIENT_GROUNDING_AMBIGUITY_NOTE

    def _provenance_self_check(self, plan: AnswerPlan) -> PacketTrace:
        if len(set(plan.sources_used)) != len(plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE,
                debug_note="sources_used contained duplicates.",
            )

        if any(path not in self.config.allowed_sources for path in plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE,
                debug_note="sources_used exceeded the manifest boundary.",
            )

        allowed_next_read_paths = set(self.config.allowed_sources) | set(
            CURRENT_STATE_NEXT_READ_PATHS + WHAT_STANDS_NOW_NEXT_READ_PATHS
        )
        if any(path not in allowed_next_read_paths for path in plan.next_read_paths):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE,
                debug_note="next_read_paths exceeded the configured local pointer set.",
            )

        answer_path_mentions = {
            match.rstrip(".,:;")
            for match in FILE_REFERENCE_RE.findall(plan.answer)
        }
        undeclared_paths = sorted(
            path for path in answer_path_mentions if path and path not in set(plan.sources_used)
        )
        if undeclared_paths:
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE,
                debug_note=f"answer mentioned undeclared repo surfaces: {undeclared_paths}",
            )

        return PacketTrace(
            sources_used=plan.sources_used,
            next_read_paths=plan.next_read_paths,
            provenance_ok=True,
            public_note=None,
            debug_note=None,
        )

    def _make_answered_plan(
        self,
        *,
        question_class: str,
        selected_sources: Tuple[str, ...],
        answer_text: str,
    ) -> AnswerPlan:
        status = "answered"
        return AnswerPlan(
            status=status,
            answer=answer_text,
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._local_boundedness_note(
                question_class=question_class,
                selected_sources=selected_sources,
                status=status,
            ),
            next_read_paths=self._local_next_read_paths(question_class, status),
            refusal_reason=None,
            ambiguity_note=None,
        )

    def _make_insufficient_grounding_plan(
        self,
        *,
        question_class: str,
        selected_sources: Tuple[str, ...],
        model_output_unusable: bool = False,
        downgraded_for_provenance: bool = False,
    ) -> AnswerPlan:
        status = "insufficient_grounding"
        return AnswerPlan(
            status=status,
            answer=(
                "The approved surfaces support a bounded present reading, but they do not "
                "support a tighter answer without exceeding bounded provenance."
            ),
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._local_boundedness_note(
                question_class=question_class,
                selected_sources=selected_sources,
                status=status,
                downgraded_for_provenance=downgraded_for_provenance,
            ),
            next_read_paths=self._local_next_read_paths(question_class, status),
            refusal_reason=None,
            ambiguity_note=self._local_ambiguity_note(
                downgraded_for_provenance=downgraded_for_provenance,
                model_output_unusable=model_output_unusable,
            ),
        )

    def _validate_output_packet(self, packet: Any) -> Dict[str, Any]:
        if not isinstance(packet, dict):
            raise HarnessError("Output packet must be a JSON object.")

        extra_keys = sorted(set(packet.keys()) - OUTPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Output packet contains unsupported fields: {extra_keys}")

        missing_keys = sorted(OUTPUT_KEYS - set(packet.keys()))
        if missing_keys:
            raise HarnessError(f"Output packet is missing required fields: {missing_keys}")

        contract_id = packet.get("contract_id")
        request_id = packet.get("request_id")
        status = packet.get("status")
        answer = packet.get("answer")
        primary_rank_used = packet.get("primary_rank_used")
        sources_used = packet.get("sources_used")
        derivative_status = packet.get("derivative_status")
        boundedness_note = packet.get("boundedness_note")
        next_read_paths = packet.get("next_read_paths")
        refusal_reason = packet.get("refusal_reason")
        ambiguity_note = packet.get("ambiguity_note")

        if contract_id != self.config.contract_id:
            raise HarnessError("Output packet contract_id does not match this narrowed vessel.")

        if not isinstance(request_id, str) or not request_id or len(request_id) > 128:
            raise HarnessError("Output packet request_id must be a non-empty bounded string.")
        if not REQUEST_ID_RE.fullmatch(request_id):
            raise HarnessError("Output packet request_id contains unsupported characters.")

        if status not in self.config.allowed_statuses:
            raise HarnessError("Output packet status is not allowed.")

        if primary_rank_used not in self.config.allowed_primary_ranks:
            raise HarnessError("Output packet primary_rank_used is not allowed.")

        if derivative_status != self.config.derivative_status:
            raise HarnessError("Output packet derivative_status is not allowed.")

        if not isinstance(answer, str):
            raise HarnessError("Output packet answer must be a string.")
        if not isinstance(boundedness_note, str) or not boundedness_note.strip():
            raise HarnessError("Output packet boundedness_note must be a non-empty string.")

        if not isinstance(sources_used, list) or not all(isinstance(item, str) and item for item in sources_used):
            raise HarnessError("Output packet sources_used must be an array of non-empty strings.")
        if len(set(sources_used)) != len(sources_used):
            raise HarnessError("Output packet sources_used must not contain duplicates.")
        if any(path not in self.config.allowed_sources for path in sources_used):
            raise HarnessError("Output packet sources_used exceeds the manifest boundary.")

        if not isinstance(next_read_paths, list) or not all(
            isinstance(item, str) and item for item in next_read_paths
        ):
            raise HarnessError("Output packet next_read_paths must be an array of non-empty strings.")
        if len(set(next_read_paths)) != len(next_read_paths):
            raise HarnessError("Output packet next_read_paths must not contain duplicates.")

        allowed_next_read_paths = set(self.config.allowed_sources) | set(
            CURRENT_STATE_NEXT_READ_PATHS + WHAT_STANDS_NOW_NEXT_READ_PATHS
        )
        if any(path not in allowed_next_read_paths for path in next_read_paths):
            raise HarnessError("Output packet next_read_paths exceeds the configured local pointer set.")

        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise HarnessError("Output packet refusal_reason is not allowed.")

        if ambiguity_note is not None:
            if not isinstance(ambiguity_note, str) or not ambiguity_note.strip():
                raise HarnessError("Output packet ambiguity_note must be a non-empty string or null.")

        if status == "answered":
            if not answer.strip():
                raise HarnessError("Answered output packets must carry a non-empty answer.")
            if not sources_used:
                raise HarnessError("Answered output packets must carry non-empty sources_used.")
            if refusal_reason is not None:
                raise HarnessError("Answered output packets must not carry a refusal_reason.")
        elif status == "insufficient_grounding":
            if not answer.strip():
                raise HarnessError("Insufficient-grounding output packets must carry a non-empty answer.")
            if not sources_used:
                raise HarnessError("Insufficient-grounding output packets must carry non-empty sources_used.")
            if refusal_reason is not None:
                raise HarnessError("Insufficient-grounding output packets must not carry a refusal_reason.")
            if ambiguity_note is None:
                raise HarnessError("Insufficient-grounding output packets must carry ambiguity_note.")
        elif status in {"refused", "out_of_scope"}:
            if answer != "":
                raise HarnessError("Refused and out-of-scope output packets must carry an empty answer.")
            if sources_used:
                raise HarnessError("Refused and out-of-scope output packets must not carry sources_used.")
            if refusal_reason is None:
                raise HarnessError("Refused and out-of-scope output packets must carry refusal_reason.")
            if next_read_paths:
                raise HarnessError("Refused and out-of-scope output packets must not carry next_read_paths.")

        return packet

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
            return self._make_insufficient_grounding_plan(
                question_class=question_class,
                selected_sources=selected_sources,
            )

        answer_text = self._call_model_for_answer_text(
            request=request,
            selected_sources=selected_sources,
            texts=source_texts,
        )
        if answer_text is None:
            return self._make_insufficient_grounding_plan(
                question_class=question_class,
                selected_sources=selected_sources,
                model_output_unusable=True,
            )

        plan = self._make_answered_plan(
            question_class=question_class,
            selected_sources=selected_sources,
            answer_text=answer_text,
        )

        trace = self._provenance_self_check(plan)
        if trace.provenance_ok:
            return plan

        return self._make_insufficient_grounding_plan(
            question_class=question_class,
            selected_sources=selected_sources,
            downgraded_for_provenance=True,
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
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_answer_only_v1.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_answer_only_v1.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    vessel = CurrentStateWhatStandsAnswerOnlyAPIVesselV1.from_environment()
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
        print(f"api_vessel_answer_only_v1 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
