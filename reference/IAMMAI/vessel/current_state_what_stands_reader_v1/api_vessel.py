#!/usr/bin/env python3
"""
API-backed vessel for current_state_what_stands_reader_v1.

This file inserts the OpenAI API inside the already-proved narrowed local
shell. The local shell remains sovereign over manifest enforcement, input
validation, source selection, provenance, refusal visibility, and final packet
assembly. The model only drafts bounded derivative answer content.
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


# Bounded default model string for the first narrowed API vessel.
DEFAULT_OPENAI_MODEL = "gpt-5"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 6

DRAFT_KEYS = {
    "status",
    "answer",
    "boundedness_note",
    "next_read_paths",
    "refusal_reason",
    "ambiguity_note",
}

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

STRUCTURED_SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_what_stands_reader_v1 vessel.

You are not sovereign.
You are not a lawmaker.
You are not a standing ratifier.
You may only answer from the provided request packet, selected source paths, and selected source contents.

Follow these rules:
- Return only the structured draft object requested by the schema.
- Do not assign contract_id, request_id, primary_rank_used, sources_used, or derivative_status.
- Do not invent or widen source provenance.
- Do not mention repo file paths in boundedness_note or ambiguity_note.
- In answer text, do not mention repo file paths unless they are in the selected source paths.
- Use next_read_paths only from the permitted next-read paths.
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
Do not mention repo file paths in boundedness_note or ambiguity_note.
In answer text, do not mention repo file paths unless they are in the selected source paths.
Use next_read_paths only from the permitted next-read paths.
If the provided sources do not support a stronger answer, use insufficient_grounding.
If the request would require new law, final standing beyond the provided surfaces, or broader interpretive sovereignty, use refused or out_of_scope rather than improvising.
Return JSON with exactly these keys:
- status
- answer
- boundedness_note
- next_read_paths
- refusal_reason
- ambiguity_note
"""


@dataclass(frozen=True)
class PacketTrace:
    sources_used: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


class DraftExtractionError(HarnessError):
    """Raised when a structured or fallback API response is unusable as a draft."""


class CurrentStateWhatStandsAPIVessel(CurrentStateWhatStandsHarness):
    """API-backed vessel that preserves the narrowed local harness as authority."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(f"The openai package is required for api_vessel.py: {detail}")

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAPIVessel":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel.py.")

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
            for key in ("text", "value", "output_text", "refusal"):
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

        for attr in ("text", "value", "output_text", "refusal"):
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

        return None

    def _append_unique_string(self, values: List[str], candidate: Optional[str]) -> None:
        if candidate and candidate not in values:
            values.append(candidate)

    def _append_unique_value(self, values: List[Any], candidate: Any) -> None:
        if candidate is None:
            return
        if candidate not in values:
            values.append(candidate)

    def _collect_dump_candidates(
        self,
        value: Any,
        *,
        text_candidates: List[str],
        parsed_candidates: List[Any],
        refusal_candidates: List[str],
        depth: int = 0,
    ) -> None:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return

        if isinstance(value, Mapping):
            item_type = value.get("type")
            if item_type == "output_text":
                self._append_unique_string(text_candidates, self._string_from_candidate(value.get("text")))
            elif item_type == "refusal":
                self._append_unique_string(refusal_candidates, self._string_from_candidate(value.get("refusal")))

            for field_name in ("output_parsed", "parsed"):
                self._append_unique_value(parsed_candidates, value.get(field_name))

            for child in value.values():
                if isinstance(child, (Mapping, list)):
                    self._collect_dump_candidates(
                        child,
                        text_candidates=text_candidates,
                        parsed_candidates=parsed_candidates,
                        refusal_candidates=refusal_candidates,
                        depth=depth + 1,
                    )
                elif isinstance(child, str):
                    self._append_unique_string(text_candidates, self._string_from_candidate(child))
            return

        if isinstance(value, list):
            for child in value:
                self._collect_dump_candidates(
                    child,
                    text_candidates=text_candidates,
                    parsed_candidates=parsed_candidates,
                    refusal_candidates=refusal_candidates,
                    depth=depth + 1,
                )

    def _collect_response_candidates(self, response: Any) -> Tuple[List[str], List[Any], List[str]]:
        text_candidates: List[str] = []
        parsed_candidates: List[Any] = []
        refusal_candidates: List[str] = []

        self._append_unique_string(
            text_candidates,
            self._string_from_candidate(self._get_field(response, "output_text")),
        )

        for field_name in ("output_parsed", "parsed"):
            self._append_unique_value(parsed_candidates, self._get_field(response, field_name))

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
                    self._append_unique_value(parsed_candidates, self._get_field(item, field_name))

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
                        self._append_unique_value(parsed_candidates, self._get_field(content, field_name))

        dumped = self._response_dump_json(response)
        if dumped is not None:
            self._collect_dump_candidates(
                dumped,
                text_candidates=text_candidates,
                parsed_candidates=parsed_candidates,
                refusal_candidates=refusal_candidates,
            )

        return text_candidates, parsed_candidates, refusal_candidates

    def _parse_json_candidates(self, candidates: Sequence[str]) -> Any:
        jsonish_candidates: List[str] = []
        last_error: Optional[json.JSONDecodeError] = None

        for candidate in candidates:
            stripped = candidate.strip()
            if not stripped:
                continue
            if not (stripped.startswith("{") or stripped.startswith("[")):
                continue
            if stripped in jsonish_candidates:
                continue
            jsonish_candidates.append(stripped)

        if len(jsonish_candidates) > 1:
            combined = "".join(jsonish_candidates).strip()
            if combined and combined not in jsonish_candidates:
                jsonish_candidates.append(combined)

        for candidate in jsonish_candidates:
            try:
                return json.loads(candidate)
            except json.JSONDecodeError as exc:
                last_error = exc

        if last_error is not None:
            raise DraftExtractionError(f"Model returned invalid JSON draft: {last_error}")

        raise DraftExtractionError("Responses API returned no usable draft payload.")

    def _extract_draft_payload(self, response: Any) -> Any:
        text_candidates, parsed_candidates, refusal_candidates = self._collect_response_candidates(response)

        for candidate in parsed_candidates:
            mapping_candidate = self._mapping_from_candidate(candidate)
            if mapping_candidate is not None:
                return mapping_candidate

            string_candidate = self._string_from_candidate(candidate)
            if string_candidate:
                self._append_unique_string(text_candidates, string_candidate)

        if text_candidates:
            return self._parse_json_candidates(text_candidates)

        if refusal_candidates:
            raise DraftExtractionError(
                "Responses API returned refusal content instead of a usable bounded draft."
            )

        raise DraftExtractionError("Responses API returned no usable draft payload.")

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
        boundedness_note = payload.get("boundedness_note")
        next_read_paths = payload.get("next_read_paths")
        refusal_reason = payload.get("refusal_reason")
        ambiguity_note = payload.get("ambiguity_note")

        if status not in self.config.allowed_statuses:
            raise HarnessError("Draft response status is not allowed.")

        if not isinstance(answer, str):
            raise HarnessError("Draft response answer must be a string.")

        if not isinstance(boundedness_note, str) or not boundedness_note.strip():
            raise HarnessError("Draft response boundedness_note must be a non-empty string.")

        if not isinstance(next_read_paths, list) or not all(
            isinstance(item, str) and item for item in next_read_paths
        ):
            raise HarnessError("Draft response next_read_paths must be an array of non-empty strings.")

        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise HarnessError("Draft response refusal_reason is not allowed.")

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
            if refusal_reason is not None:
                raise HarnessError("Draft insufficient_grounding status must not carry a refusal reason.")
            if not isinstance(ambiguity_note, str) or not ambiguity_note.strip():
                raise HarnessError(
                    "Draft insufficient_grounding status must carry a non-empty ambiguity_note."
                )

        return {
            "status": status,
            "answer": answer,
            "boundedness_note": boundedness_note,
            "next_read_paths": list(next_read_paths),
            "refusal_reason": refusal_reason,
            "ambiguity_note": ambiguity_note,
        }

    def _build_model_input(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        allowed_next_read_paths: Sequence[str],
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
        payload.append(json.dumps(list(allowed_next_read_paths), indent=2, ensure_ascii=True))
        payload.append("")
        payload.append("SELECTED_SOURCE_CONTENTS")
        for path in selected_sources:
            payload.append(f"=== BEGIN SOURCE: {path} ===")
            payload.append(texts[path])
            payload.append(f"=== END SOURCE: {path} ===")
            payload.append("")
        return "\n".join(payload).strip()

    def _is_structured_output_issue(self, exc: Exception) -> bool:
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
                        "name": "current_state_what_stands_reader_v1_draft",
                        "schema": DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        payload = self._extract_draft_payload(response)
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

        payload = self._extract_draft_payload(response)
        return self._validate_draft(payload)

    def _call_model_for_draft(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        allowed_next_read_paths: Sequence[str],
        texts: Mapping[str, str],
    ) -> Dict[str, Any]:
        model_input = self._build_model_input(
            request=request,
            selected_sources=selected_sources,
            allowed_next_read_paths=allowed_next_read_paths,
            texts=texts,
        )

        try:
            return self._call_model_structured(model_input)
        except Exception as exc:
            if not self._is_structured_output_issue(exc):
                if isinstance(exc, HarnessError):
                    raise
                raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        return self._call_model_json_fallback(model_input)

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

    def _provenance_self_check(self, plan: AnswerPlan) -> PacketTrace:
        if len(set(plan.sources_used)) != len(plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A generated response field exceeded bounded provenance and was downgraded conservatively.",
                debug_note="sources_used contained duplicates.",
            )

        if any(path not in self.config.allowed_sources for path in plan.sources_used):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A generated response field exceeded bounded provenance and was downgraded conservatively.",
                debug_note="sources_used exceeded the manifest boundary.",
            )

        if any(path not in self.config.allowed_sources for path in plan.next_read_paths):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note="A generated response field exceeded bounded provenance and was downgraded conservatively.",
                debug_note="next_read_paths exceeded the manifest boundary.",
            )

        text_fields = {
            "answer": plan.answer,
            "boundedness_note": plan.boundedness_note,
            "ambiguity_note": plan.ambiguity_note or "",
        }
        consulted_source_set = set(plan.sources_used)

        for field_name, text in text_fields.items():
            path_mentions = {
                match.rstrip(".,:;")
                for match in FILE_REFERENCE_RE.findall(text)
            }
            if field_name == "answer":
                undeclared = sorted(path for path in path_mentions if path not in consulted_source_set)
            else:
                undeclared = sorted(path_mentions)

            if undeclared:
                return PacketTrace(
                    sources_used=plan.sources_used,
                    next_read_paths=plan.next_read_paths,
                    provenance_ok=False,
                    public_note="A generated response field exceeded bounded provenance and was downgraded conservatively.",
                    debug_note=f"{field_name} mentioned disallowed repo surfaces: {undeclared}",
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
        question_class: str,
        selected_sources: Tuple[str, ...],
        next_read_paths: Tuple[str, ...],
    ) -> AnswerPlan:
        return AnswerPlan(
            status="insufficient_grounding",
            answer=(
                "The approved surfaces did not support a tighter derivative answer without "
                "exceeding bounded provenance."
            ),
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=(
                "This vessel stayed inside its approved source boundary and downgraded a drifted "
                "draft conservatively."
            ),
            next_read_paths=next_read_paths,
            refusal_reason=None,
            ambiguity_note=(
                "A generated response field exceeded bounded provenance and was downgraded "
                "conservatively."
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

        allowed_next_read_paths = self._next_read_paths(question_class, selected_sources, "answered")
        draft = self._call_model_for_draft(
            request=request,
            selected_sources=selected_sources,
            allowed_next_read_paths=allowed_next_read_paths,
            texts=source_texts,
        )

        if draft["status"] in {"refused", "out_of_scope"}:
            return self._refusal_plan(
                question_class=question_class,
                status=str(draft["status"]),
                refusal_reason=str(draft["refusal_reason"]),
            )

        normalized_next_read_paths = self._normalize_next_read_paths(
            draft_paths=draft["next_read_paths"],
            allowed_paths=allowed_next_read_paths,
        )

        plan = AnswerPlan(
            status=str(draft["status"]),
            answer=str(draft["answer"]),
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=str(draft["boundedness_note"]),
            next_read_paths=normalized_next_read_paths,
            refusal_reason=draft["refusal_reason"],
            ambiguity_note=draft["ambiguity_note"],
        )

        trace = self._provenance_self_check(plan)
        if trace.provenance_ok:
            return plan

        return self._downgraded_insufficient_grounding_plan(
            question_class=question_class,
            selected_sources=selected_sources,
            next_read_paths=normalized_next_read_paths,
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
        "  python vessel/current_state_what_stands_reader_v1/api_vessel.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    vessel = CurrentStateWhatStandsAPIVessel.from_environment()
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
        print(f"api_vessel error: {exc}", file=sys.stderr)
        raise SystemExit(2)
