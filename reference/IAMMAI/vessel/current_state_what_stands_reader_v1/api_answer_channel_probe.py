#!/usr/bin/env python3
"""
Implementation-local answer-channel probe for current_state_what_stands_reader_v1.

This additive file probes one representative failing answered case under the
same narrowed vessel family posture, but it stops before any vessel-output
finalization. Its job is only to determine whether the current Responses API
channel exposes any answer-bearing content at all for that bounded matter.
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
    REPO_ROOT,
    CurrentStateWhatStandsHarness,
    HarnessError,
)


DEFAULT_OPENAI_MODEL = "gpt-5"
DEFAULT_PROBE_CASE_ID = "eval_003_what_stands_now_answered"
PROBE_CHANNEL = "structured_responses_json_schema"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 6
MAX_SUMMARY_OUTPUT_ITEMS = 6
MAX_SUMMARY_CONTENT_ITEMS = 6
MAX_CANDIDATE_NOTES = 12
MAX_TOP_LEVEL_KEYS = 20
TEXT_EXTRACTION_MAX_DEPTH = 5
MAX_TEXT_PREVIEW = 180
MIN_TEXT_WORDS = 5
MIN_TEXT_ALPHA_CHARS = 20

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

SCHEMAISH_PATH_SEGMENTS = {
    "schema",
    "schema_",
    "properties",
    "format",
    "json_schema",
    "response_format",
}

SCHEMAISH_MAPPING_KEYS = {
    "$schema",
    "additionalProperties",
    "allOf",
    "anyOf",
    "const",
    "description",
    "enum",
    "examples",
    "items",
    "name",
    "oneOf",
    "properties",
    "required",
    "schema",
    "strict",
    "title",
    "type",
}

ANSWER_BEARING_MARKERS = (
    "repository",
    "repo",
    "v1",
    "current state",
    "current repository",
    "current condition",
    "stands now",
    "what stands",
    "standing",
    "approved surface",
    "approved surfaces",
    "derivative line",
    "proof-bearing",
    "proof readable",
    "total closure",
    "final standing",
    "frozen root",
    "current line",
)

META_TEXT_MARKERS = (
    "json object",
    "request packet",
    "selected source",
    "selected sources",
    "selected source paths",
    "selected source contents",
    "contract_id",
    "request_id",
    "primary_rank_used",
    "derivative_status",
    "boundedness_note",
    "next_read_paths",
    "refusal_reason",
    "follow these rules",
    "return exactly",
    "return json",
    "need to answer",
    "should answer",
    "must answer",
)

REFUSAL_TEXT_MARKERS = (
    "would require interpretive sovereignty",
    "broader doctrinal generation",
    "outside the provided sources",
    "outside provided sources",
    "requires unapproved sources",
    "not in the manifest",
    "out of scope",
    "refuse",
    "refusal",
)

JSON_FENCE_RE = re.compile(r"^```(?:json)?\s*(.*?)\s*```$", re.DOTALL)
DEBUG_FILENAME_RE = re.compile(
    r"^api_vessel_v[56]_debug__.+__(eval_req_\d+)__extraction_(?:structured|fallback)\.json$"
)


@dataclass(frozen=True)
class CandidateNote:
    location: str
    candidate_kind: str
    later_vessel_output_compatibility: str
    bounded_reason: str
    shape_summary: Dict[str, Any]
    text_preview: Optional[str]

    def as_dict(self) -> Dict[str, Any]:
        return {
            "location": self.location,
            "candidate_kind": self.candidate_kind,
            "later_vessel_output_compatibility": self.later_vessel_output_compatibility,
            "bounded_reason": self.bounded_reason,
            "shape_summary": dict(self.shape_summary),
            "text_preview": self.text_preview,
        }


class ProbeExecutionError(HarnessError):
    """Raised when the bounded probe cannot execute or summarize a response."""


class CurrentStateWhatStandsAnswerChannelProbe(CurrentStateWhatStandsHarness):
    """Implementation-local probe for one bounded answered-case channel only."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(
                f"The openai package is required for api_answer_channel_probe.py: {detail}"
            )

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAnswerChannelProbe":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_answer_channel_probe.py.")

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
            for key in ("text", "value", "output_text", "arguments", "summary", "content"):
                candidate = self._string_from_candidate(value.get(key))
                if candidate:
                    return candidate
            return None

        dumped = self._response_dump_json(value)
        if dumped is not None and dumped is not value:
            candidate = self._string_from_candidate(dumped)
            if candidate:
                return candidate

        for attr in ("text", "value", "output_text", "arguments", "summary", "content"):
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

    def _path_segments(self, source_path: str) -> Tuple[str, ...]:
        parts = re.split(r"[.\[\]]+", source_path)
        return tuple(part for part in parts if part and not part.isdigit())

    def _looks_like_schema_mapping(self, value: Any) -> bool:
        if not isinstance(value, Mapping):
            return False

        keys = {str(key) for key in value.keys()}
        if not keys:
            return False

        if keys.issubset(SCHEMAISH_MAPPING_KEYS):
            return True

        if "type" in value and any(key in value for key in ("enum", "properties", "items", "required", "const")):
            return True

        return False

    def _extract_text_fragments(self, value: Any, *, depth: int = 0) -> List[str]:
        if value is None or depth > TEXT_EXTRACTION_MAX_DEPTH:
            return []

        if isinstance(value, str):
            stripped = self._strip_code_fence(value).strip()
            return [stripped] if stripped else []

        if isinstance(value, list):
            fragments: List[str] = []
            for item in value:
                fragments.extend(self._extract_text_fragments(item, depth=depth + 1))
            return fragments

        if isinstance(value, Mapping):
            fragments: List[str] = []
            for key in ("text", "answer", "value", "output_text", "arguments", "summary", "content"):
                if key in value:
                    fragments.extend(self._extract_text_fragments(value.get(key), depth=depth + 1))
            return fragments

        dumped = self._response_dump_json(value)
        if dumped is not None and dumped is not value:
            return self._extract_text_fragments(dumped, depth=depth + 1)

        fragments = []
        for attr in ("text", "answer", "value", "output_text", "arguments", "summary", "content"):
            attr_value = getattr(value, attr, None)
            if attr_value is not None:
                fragments.extend(self._extract_text_fragments(attr_value, depth=depth + 1))
        return fragments

    def _dedupe_text_fragments(self, fragments: Iterable[str]) -> List[str]:
        seen: set[str] = set()
        unique: List[str] = []
        for fragment in fragments:
            normalized = re.sub(r"\s+", " ", fragment).strip()
            if not normalized or normalized in seen:
                continue
            seen.add(normalized)
            unique.append(normalized)
        return unique

    def _joined_text_candidate(self, value: Any) -> Optional[str]:
        fragments = self._dedupe_text_fragments(self._extract_text_fragments(value))
        if not fragments:
            return None
        return "\n".join(fragments)

    def _word_count(self, text: str) -> int:
        return len(re.findall(r"[A-Za-z0-9]+", text))

    def _alpha_count(self, text: str) -> int:
        return sum(1 for char in text if char.isalpha())

    def _text_preview(self, text: str) -> str:
        compact = re.sub(r"\s+", " ", text).strip()
        if len(compact) <= MAX_TEXT_PREVIEW:
            return compact
        return compact[: MAX_TEXT_PREVIEW - 3] + "..."

    def _sanitize_label(self, value: str) -> str:
        return re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._-") or "unknown"

    def _timestamp_slug(self) -> str:
        return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

    def _visible_failing_answered_request_ids(self) -> Tuple[str, ...]:
        if not DEBUG_ROOT.exists():
            return ()

        request_ids: set[str] = set()
        try:
            for path in DEBUG_ROOT.iterdir():
                if not path.is_file():
                    continue
                match = DEBUG_FILENAME_RE.fullmatch(path.name)
                if match:
                    request_ids.add(match.group(1))
        except OSError:
            return ()

        return tuple(sorted(request_ids))

    def _select_default_case(self, cases: Sequence[Mapping[str, Any]]) -> Mapping[str, Any]:
        answered_cases = [
            case for case in cases
            if case.get("expected_status") == "answered" and isinstance(case.get("input_packet"), Mapping)
        ]
        if not answered_cases:
            raise ProbeExecutionError("Eval corpus contains no answered cases to probe.")

        for case in answered_cases:
            if case.get("eval_id") == DEFAULT_PROBE_CASE_ID:
                default_case = case
                break
        else:
            default_case = answered_cases[0]

        failing_request_ids = set(self._visible_failing_answered_request_ids())
        if not failing_request_ids:
            return default_case

        failing_cases = []
        for case in answered_cases:
            input_packet = case.get("input_packet")
            if not isinstance(input_packet, Mapping):
                continue
            request_id = input_packet.get("request_id")
            if isinstance(request_id, str) and request_id in failing_request_ids:
                failing_cases.append(case)

        if not failing_cases:
            return default_case

        for case in failing_cases:
            if case.get("eval_id") == DEFAULT_PROBE_CASE_ID:
                return case

        def sort_key(case: Mapping[str, Any]) -> Tuple[int, str]:
            expected_min_sources = case.get("expected_min_sources")
            min_sources = expected_min_sources if isinstance(expected_min_sources, int) else 99
            eval_id = str(case.get("eval_id", ""))
            return (min_sources, eval_id)

        return sorted(failing_cases, key=sort_key)[0]

    def _load_probe_case(self, case_id_override: Optional[str]) -> Mapping[str, Any]:
        corpus = self._load_eval_corpus()
        cases = corpus["cases"]
        if not isinstance(cases, list):
            raise ProbeExecutionError("Eval corpus cases must be an array.")

        mapping_cases = [case for case in cases if isinstance(case, Mapping)]
        if case_id_override:
            for case in mapping_cases:
                if case.get("eval_id") == case_id_override:
                    if case.get("expected_status") != "answered":
                        raise ProbeExecutionError(
                            f"Probe case {case_id_override!r} is not an answered eval case."
                        )
                    return case
            raise ProbeExecutionError(f"Probe case {case_id_override!r} was not found in eval_corpus.json.")

        return self._select_default_case(mapping_cases)

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

    def _call_probe_channel(self, model_input: str) -> Any:
        try:
            return self._client.responses.create(
                model=self._model,
                instructions=STRUCTURED_SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                store=False,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "current_state_what_stands_reader_v1_answer_channel_probe",
                        "schema": DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise ProbeExecutionError(f"OpenAI Responses API probe call failed: {exc}") from exc

    def _iter_explicit_probe_nodes(self, response: Any) -> Iterable[Tuple[str, Any]]:
        yielded_paths: set[str] = set()

        def emit(path: str, value: Any) -> Iterable[Tuple[str, Any]]:
            if value is None or path in yielded_paths:
                return ()
            yielded_paths.add(path)
            return ((path, value),)

        for field_name in ("output_parsed", "parsed", "output_text", "summary"):
            for item in emit(f"response.{field_name}", self._get_field(response, field_name)):
                yield item

        output_items = self._get_field(response, "output")
        if not isinstance(output_items, list):
            return

        for index, output_item in enumerate(output_items):
            base = f"response.output[{index}]"
            for item in emit(base, output_item):
                yield item

            for field_name in ("output_parsed", "parsed", "summary", "text", "arguments", "output_text", "content"):
                for item in emit(f"{base}.{field_name}", self._get_field(output_item, field_name)):
                    yield item

            content_items = self._get_field(output_item, "content")
            if not isinstance(content_items, list):
                continue

            for content_index, content_item in enumerate(content_items):
                content_base = f"{base}.content[{content_index}]"
                for item in emit(content_base, content_item):
                    yield item

                for field_name in ("output_parsed", "parsed", "summary", "text", "arguments", "output_text"):
                    for item in emit(
                        f"{content_base}.{field_name}",
                        self._get_field(content_item, field_name),
                    ):
                        yield item

    def _iter_dump_nodes(self, value: Any, *, path: str, depth: int) -> Iterable[Tuple[str, Any]]:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return

        yield path, value

        if isinstance(value, Mapping):
            priority_keys = (
                "output_parsed",
                "parsed",
                "output_text",
                "summary",
                "text",
                "arguments",
                "output",
                "content",
                "value",
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

    def _iter_dump_probe_nodes(self, response: Any) -> Iterable[Tuple[str, Any]]:
        dumped = self._response_dump_json(response)
        if not isinstance(dumped, Mapping):
            return

        yielded_paths: set[str] = set()

        def emit(path: str, value: Any) -> Iterable[Tuple[str, Any]]:
            if value is None or path in yielded_paths:
                return ()
            yielded_paths.add(path)
            return ((path, value),)

        for field_name in ("output_parsed", "parsed", "output_text", "summary"):
            if field_name in dumped:
                for item in emit(f"dump.{field_name}", dumped.get(field_name)):
                    yield item

        output_items = dumped.get("output")
        if isinstance(output_items, list):
            for index, output_item in enumerate(output_items):
                base = f"dump.output[{index}]"
                for path, value in self._iter_dump_nodes(output_item, path=base, depth=1):
                    if path in yielded_paths:
                        continue
                    yielded_paths.add(path)
                    yield path, value

    def _iter_probe_nodes(self, response: Any) -> Iterable[Tuple[str, Any]]:
        yielded_paths: set[str] = set()
        for iterator in (
            self._iter_explicit_probe_nodes(response),
            self._iter_dump_probe_nodes(response),
        ):
            for path, value in iterator:
                if path in yielded_paths:
                    continue
                yielded_paths.add(path)
                yield path, value

    def _mapping_candidate_note(self, path: str, mapping_candidate: Mapping[str, Any]) -> Optional[CandidateNote]:
        if not DRAFT_KEYS.issubset(mapping_candidate.keys()):
            return None

        status = mapping_candidate.get("status")
        answer = mapping_candidate.get("answer")
        refusal_reason = mapping_candidate.get("refusal_reason")
        path_segments = set(self._path_segments(path))

        if path_segments & SCHEMAISH_PATH_SEGMENTS:
            compatibility = "no"
            reason = "Draft-shaped mapping was found inside schema or config structure rather than actual response payload."
        elif self._looks_like_schema_mapping(mapping_candidate):
            compatibility = "no"
            reason = "Draft-shaped mapping itself looked like schema or config structure."
        elif not isinstance(status, str) or not isinstance(answer, str) or (
            refusal_reason is not None and not isinstance(refusal_reason, str)
        ):
            compatibility = "no"
            reason = "Draft-shaped mapping had non-payload field types and does not yet look usable."
        else:
            compatibility = "potential"
            reason = "Draft-shaped mapping was present at a non-schema location and may be compatible with later vessel handling."

        answer_preview = answer[:MAX_TEXT_PREVIEW] if isinstance(answer, str) and answer else None
        return CandidateNote(
            location=path,
            candidate_kind="draft_shaped_mapping",
            later_vessel_output_compatibility=compatibility,
            bounded_reason=reason,
            shape_summary={
                "keys": sorted(str(key) for key in mapping_candidate.keys() if str(key) in DRAFT_KEYS),
                "status_type": type(status).__name__,
                "answer_type": type(answer).__name__,
                "refusal_reason_type": type(refusal_reason).__name__,
            },
            text_preview=answer_preview,
        )

    def _text_candidate_note(self, path: str, text: str) -> CandidateNote:
        stripped = self._strip_code_fence(text).strip()
        lowered = stripped.lower()
        path_segments = set(self._path_segments(path))
        word_count = self._word_count(stripped)
        alpha_count = self._alpha_count(stripped)

        compatibility = "no"
        reason = "Structured text was present but does not presently look compatible with later vessel handling."

        if path_segments & SCHEMAISH_PATH_SEGMENTS:
            reason = "Text-bearing structure sits inside schema or config branches."
        elif stripped.startswith("{") or stripped.startswith("["):
            reason = "Text-bearing structure looked like JSON or config payload rather than answer-bearing content."
        elif any(marker in lowered for marker in META_TEXT_MARKERS):
            reason = "Text-bearing structure looked like prompt or protocol scaffolding rather than answer content."
        elif word_count < MIN_TEXT_WORDS or alpha_count < MIN_TEXT_ALPHA_CHARS:
            reason = "Text-bearing structure was too slight to treat as a meaningful answer channel."
        elif any(marker in lowered for marker in REFUSAL_TEXT_MARKERS):
            compatibility = "no"
            reason = "Text-bearing structure was readable, but it pointed toward refusal or out-of-scope behavior rather than an answered channel."
        elif any(marker in lowered for marker in ANSWER_BEARING_MARKERS):
            compatibility = "potential"
            reason = "Text-bearing structure contained bounded answer-like language about the current repo state or what now stands."
        else:
            compatibility = "unclear"
            reason = "Readable text was present, but it did not clearly bind to the bounded answered channel without further vessel-family decisions."

        return CandidateNote(
            location=path,
            candidate_kind="text_bearing_structure",
            later_vessel_output_compatibility=compatibility,
            bounded_reason=reason,
            shape_summary={
                "word_count": word_count,
                "alpha_count": alpha_count,
                "path_depth": len(self._path_segments(path)),
            },
            text_preview=self._text_preview(stripped),
        )

    def _collect_candidate_notes(self, response: Any) -> Tuple[List[CandidateNote], List[str]]:
        notes: List[CandidateNote] = []
        attempted_paths: List[str] = []
        seen_text_notes: set[Tuple[str, str]] = set()
        seen_mapping_paths: set[str] = set()

        for path, value in self._iter_probe_nodes(response):
            if path not in attempted_paths:
                attempted_paths.append(path)

            mapping_candidate = self._mapping_from_candidate(value)
            if mapping_candidate is not None and path not in seen_mapping_paths:
                seen_mapping_paths.add(path)
                note = self._mapping_candidate_note(path, mapping_candidate)
                if note is not None:
                    notes.append(note)

            text_candidate = self._joined_text_candidate(value)
            if text_candidate is None:
                continue

            dedupe_key = (path, text_candidate)
            if dedupe_key in seen_text_notes:
                continue
            seen_text_notes.add(dedupe_key)
            notes.append(self._text_candidate_note(path, text_candidate))

        return notes[:MAX_CANDIDATE_NOTES], attempted_paths

    def _response_summary(self, response: Any) -> Dict[str, Any]:
        summary: Dict[str, Any] = {
            "probe_channel": PROBE_CHANNEL,
            "response_id": self._string_from_candidate(self._get_field(response, "id")),
            "model": self._string_from_candidate(self._get_field(response, "model")),
            "has_output_text": self._string_from_candidate(self._get_field(response, "output_text")) is not None,
            "has_output_parsed": self._get_field(response, "output_parsed") is not None,
            "has_parsed": self._get_field(response, "parsed") is not None,
        }

        output_items = self._get_field(response, "output")
        output_summaries: List[Dict[str, Any]] = []
        any_reasoning_items = False

        if isinstance(output_items, list):
            summary["output_count"] = len(output_items)
            for output_item in output_items[:MAX_SUMMARY_OUTPUT_ITEMS]:
                item_type = str(self._get_field(output_item, "type") or type(output_item).__name__)
                if item_type == "reasoning":
                    any_reasoning_items = True

                content_types: List[str] = []
                content_items = self._get_field(output_item, "content")
                if isinstance(content_items, list):
                    for content_item in content_items[:MAX_SUMMARY_CONTENT_ITEMS]:
                        content_types.append(
                            str(self._get_field(content_item, "type") or type(content_item).__name__)
                        )

                summary_value = self._get_field(output_item, "summary")
                output_summaries.append(
                    {
                        "type": item_type,
                        "status": self._string_from_candidate(self._get_field(output_item, "status")),
                        "has_summary": summary_value is not None,
                        "summary_count": len(summary_value) if isinstance(summary_value, list) else 0,
                        "has_output_parsed": self._get_field(output_item, "output_parsed") is not None,
                        "has_parsed": self._get_field(output_item, "parsed") is not None,
                        "content_types": content_types,
                    }
                )
        else:
            summary["output_count"] = 0

        summary["output_items"] = output_summaries
        summary["any_reasoning_items"] = any_reasoning_items

        dumped = self._response_dump_json(response)
        if isinstance(dumped, Mapping):
            summary["top_level_keys"] = sorted(str(key) for key in dumped.keys())[:MAX_TOP_LEVEL_KEYS]
        else:
            summary["top_level_keys"] = []

        return summary

    def _answer_channel_finding(
        self,
        response_summary: Mapping[str, Any],
        candidate_notes: Sequence[CandidateNote],
        attempted_paths: Sequence[str],
    ) -> Dict[str, Any]:
        potential_locations = [
            note.location for note in candidate_notes if note.later_vessel_output_compatibility == "potential"
        ]
        unclear_locations = [
            note.location for note in candidate_notes if note.later_vessel_output_compatibility == "unclear"
        ]

        if potential_locations:
            return {
                "answer_channel_status": "answer_bearing_content_found",
                "candidate_locations": potential_locations,
                "bounded_reason": (
                    "At least one bounded candidate location exposed draft-shaped or text-bearing "
                    "content that looks potentially compatible with later vessel-family handling."
                ),
                "inspected_locations": list(attempted_paths),
            }

        if unclear_locations:
            return {
                "answer_channel_status": "ambiguous",
                "candidate_locations": unclear_locations,
                "bounded_reason": (
                    "Readable structured content was present, but it did not clearly resolve into "
                    "a bounded answered channel without further vessel-family decisions."
                ),
                "inspected_locations": list(attempted_paths),
            }

        if response_summary.get("any_reasoning_items") is True and response_summary.get("output_count", 0):
            return {
                "answer_channel_status": "reasoning_only",
                "candidate_locations": [],
                "bounded_reason": (
                    "The response exposed reasoning-shaped structure, but this bounded probe did "
                    "not observe any answer-bearing channel that looked usable later."
                ),
                "inspected_locations": list(attempted_paths),
            }

        return {
            "answer_channel_status": "ambiguous",
            "candidate_locations": [],
            "bounded_reason": (
                "The response was readable at top level, but this bounded probe did not find a "
                "clear answer-bearing channel or a clean reasoning-only shape."
            ),
            "inspected_locations": list(attempted_paths),
        }

    def _write_probe_artifact(
        self,
        *,
        request_id: str,
        eval_id: str,
        payload: Mapping[str, Any],
    ) -> Path:
        DEBUG_ROOT.mkdir(parents=True, exist_ok=True)
        filename = (
            f"answer_channel_probe__{self._timestamp_slug()}__"
            f"{self._sanitize_label(eval_id)}__{self._sanitize_label(request_id)}.json"
        )
        artifact_path = DEBUG_ROOT / filename
        artifact_path.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        return artifact_path

    def _build_probe_artifact(
        self,
        *,
        case: Mapping[str, Any],
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        response_summary: Mapping[str, Any],
        answer_channel_finding: Mapping[str, Any],
        candidate_notes: Sequence[CandidateNote],
        api_error: Optional[str] = None,
    ) -> Dict[str, Any]:
        input_packet = case.get("input_packet")
        eval_id = str(case.get("eval_id", "unknown_eval"))

        artifact: Dict[str, Any] = {
            "metadata": {
                "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "probe_builder_path": self._repo_relative(SCRIPT_PATH),
                "probe_channel": PROBE_CHANNEL,
                "selected_case_id": eval_id,
                "selected_question_class": request["question_class"],
                "selected_request_id": request["request_id"],
            },
            "selected_input_summary": {
                "input_packet": input_packet,
                "question_text": request["question_text"],
                "selected_sources": list(selected_sources),
                "allowed_sources_boundary": list(self.config.allowed_sources),
                "allowed_question_classes": list(self.config.allowed_question_classes),
            },
            "response_surface_summary": dict(response_summary),
            "answer_channel_finding": dict(answer_channel_finding),
            "structured_candidate_notes": [note.as_dict() for note in candidate_notes],
            "anti_collapse_note": (
                "This probe is implementation-local diagnostic support only. It does not create "
                "vessel success, does not finalize output, does not widen contract, and does not "
                "create final standing, canon, constitutional force, publication rank, governance "
                "authorization, or consequence."
            ),
        }
        if api_error is not None:
            artifact["response_surface_summary"]["api_error"] = api_error
        return artifact

    def run_probe(self, case_id_override: Optional[str]) -> int:
        case = self._load_probe_case(case_id_override)
        input_packet = case.get("input_packet")
        request = self._validate_input_packet(input_packet)

        if case.get("expected_status") != "answered":
            raise ProbeExecutionError("Probe target must be an answered eval case.")

        question_text = str(request["question_text"])
        question_class = str(request["question_class"])

        if self._is_mutation_request(question_text):
            raise ProbeExecutionError("Probe target unexpectedly triggered mutation refusal posture.")
        if self._question_mentions_unapproved_sources(question_text):
            raise ProbeExecutionError("Probe target unexpectedly referenced unapproved sources.")
        if self._is_interpretive_sovereignty_request(question_text):
            raise ProbeExecutionError("Probe target unexpectedly triggered interpretive-sovereignty refusal posture.")
        if self._is_insufficient_grounding_request(question_text):
            raise ProbeExecutionError("Probe target unexpectedly triggered insufficient-grounding posture.")

        selected_sources = self._choose_sources_for_request(question_class, question_text)
        source_texts = self._read_selected_sources(selected_sources)
        model_input = self._build_model_input(request, selected_sources, source_texts)

        try:
            response = self._call_probe_channel(model_input)
        except ProbeExecutionError as exc:
            response_summary = {
                "probe_channel": PROBE_CHANNEL,
                "model": self._model,
                "response_id": None,
                "output_count": 0,
                "output_items": [],
                "has_output_text": False,
                "has_output_parsed": False,
                "has_parsed": False,
                "top_level_keys": [],
                "any_reasoning_items": False,
            }
            finding = {
                "answer_channel_status": "response_unreadable",
                "candidate_locations": [],
                "bounded_reason": "The API call failed before any bounded response summary could be inspected.",
                "inspected_locations": [],
            }
            artifact = self._build_probe_artifact(
                case=case,
                request=request,
                selected_sources=selected_sources,
                response_summary=response_summary,
                answer_channel_finding=finding,
                candidate_notes=[],
                api_error=str(exc),
            )
            artifact_path = self._write_probe_artifact(
                request_id=str(request["request_id"]),
                eval_id=str(case.get("eval_id", "unknown_eval")),
                payload=artifact,
            )
            print(
                f"Probe {case.get('eval_id')}: response_unreadable. "
                f"artifact={self._repo_relative(artifact_path)}",
                file=sys.stderr,
            )
            return 2

        response_summary = self._response_summary(response)
        candidate_notes, attempted_paths = self._collect_candidate_notes(response)
        finding = self._answer_channel_finding(response_summary, candidate_notes, attempted_paths)

        artifact = self._build_probe_artifact(
            case=case,
            request=request,
            selected_sources=selected_sources,
            response_summary=response_summary,
            answer_channel_finding=finding,
            candidate_notes=candidate_notes,
        )
        artifact_path = self._write_probe_artifact(
            request_id=str(request["request_id"]),
            eval_id=str(case.get("eval_id", "unknown_eval")),
            payload=artifact,
        )

        candidate_locations = finding.get("candidate_locations") or []
        location_note = candidate_locations[0] if candidate_locations else "none"
        print(
            f"Probe {case.get('eval_id')}: {finding['answer_channel_status']}. "
            f"first_candidate={location_note}. artifact={self._repo_relative(artifact_path)}"
        )
        return 0


def print_usage() -> None:
    usage = (
        "Usage:\n"
        "  python vessel/current_state_what_stands_reader_v1/api_answer_channel_probe.py\n"
        "  python vessel/current_state_what_stands_reader_v1/api_answer_channel_probe.py <eval_id>\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) > 2:
        print_usage()
        return 2

    case_id_override = argv[1] if len(argv) == 2 else None
    probe = CurrentStateWhatStandsAnswerChannelProbe.from_environment()
    return probe.run_probe(case_id_override)


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except ProbeExecutionError as exc:
        print(f"api_answer_channel_probe error: {exc}", file=sys.stderr)
        raise SystemExit(2)
    except HarnessError as exc:
        print(f"api_answer_channel_probe error: {exc}", file=sys.stderr)
        raise SystemExit(2)
