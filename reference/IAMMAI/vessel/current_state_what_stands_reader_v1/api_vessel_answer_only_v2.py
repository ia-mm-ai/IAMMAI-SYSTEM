#!/usr/bin/env python3
"""
Answer-only API-backed vessel v2 for current_state_what_stands_reader_v1.

This additive file keeps the narrowed local shell sovereign while simplifying
the API seam to plain bounded answer text. Local code still owns manifest
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
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

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


# Bounded default model string for the simplified answer-only API vessel.
DEFAULT_OPENAI_MODEL = "gpt-5"
MAX_OUTPUT_TOKENS = 1200
RESPONSE_DUMP_MAX_DEPTH = 4

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

SYSTEM_PROMPT = """You are drafting bounded derivative answer text for the IAMMAI current_state_what_stands_reader_v1 vessel.

You are not sovereign.
You are not a lawmaker.
You are not a standing ratifier.
You may only answer from the provided request packet, selected source paths, and selected source contents.

Follow these rules:
- Return plain bounded answer text only.
- Do not return JSON, field labels, notes, provenance, ranks, statuses, or next-read pointers.
- Do not invent or widen provenance.
- Do not mention repo file paths unless they are in the selected source paths.
- Do not claim new law, new standing, total closure, or final standing beyond the provided sources.
- Keep the answer sober, concise, and derivative.
"""


@dataclass(frozen=True)
class PacketTrace:
    sources_used: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


class CurrentStateWhatStandsAnswerOnlyAPIVesselV2(CurrentStateWhatStandsHarness):
    """API-backed vessel that keeps the narrowed local shell authoritative."""

    def __init__(self, *, api_key: str, model: str) -> None:
        if OpenAI is None:
            detail = str(_OPENAI_IMPORT_ERROR) if _OPENAI_IMPORT_ERROR else "unknown import error"
            raise HarnessError(
                f"The openai package is required for api_vessel_answer_only_v2.py: {detail}"
            )

        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateWhatStandsAnswerOnlyAPIVesselV2":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel_answer_only_v2.py.")

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

    def _string_from_candidate(self, value: Any) -> Optional[str]:
        if value is None:
            return None

        if isinstance(value, str):
            stripped = value.strip()
            return stripped if stripped else None

        if isinstance(value, Mapping):
            for key in ("text", "value", "output_text"):
                candidate = self._string_from_candidate(value.get(key))
                if candidate:
                    return candidate
            return None

        for attr in ("text", "value", "output_text"):
            candidate = self._string_from_candidate(getattr(value, attr, None))
            if candidate:
                return candidate

        return None

    def _strip_code_fence(self, text: str) -> str:
        stripped = text.strip()
        if not (stripped.startswith("```") and stripped.endswith("```")):
            return stripped

        lines = stripped.splitlines()
        if lines and lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines).strip()

    def _normalize_answer_text(self, value: Any) -> Optional[str]:
        candidate = self._string_from_candidate(value)
        if not candidate:
            return None

        candidate = self._strip_code_fence(candidate)
        if not candidate:
            return None

        if candidate.startswith("{") or candidate.startswith("["):
            try:
                parsed = json.loads(candidate)
            except json.JSONDecodeError:
                return None

            if isinstance(parsed, Mapping):
                answer = parsed.get("answer")
                if isinstance(answer, str):
                    answer = answer.strip()
                    return answer if answer else None
            return None

        return candidate

    def _extract_answer_from_output_item(self, item: Any) -> Optional[str]:
        item_type = self._get_field(item, "type")
        if item_type == "output_text":
            answer = self._normalize_answer_text(self._get_field(item, "text"))
            if answer is not None:
                return answer

        content_items = self._get_field(item, "content")
        if isinstance(content_items, list):
            for content in content_items:
                if self._get_field(content, "type") != "output_text":
                    continue
                answer = self._normalize_answer_text(self._get_field(content, "text"))
                if answer is not None:
                    return answer

        return None

    def _extract_answer_from_dump(self, value: Any, depth: int = 0) -> Optional[str]:
        if depth > RESPONSE_DUMP_MAX_DEPTH:
            return None

        if isinstance(value, Mapping):
            item_type = value.get("type")
            if item_type == "output_text":
                answer = self._normalize_answer_text(value.get("text"))
                if answer is not None:
                    return answer

            for key in ("output_text", "text", "value"):
                if key in value:
                    answer = self._normalize_answer_text(value[key])
                    if answer is not None:
                        return answer

            for key in ("output", "content"):
                if key not in value:
                    continue
                answer = self._extract_answer_from_dump(value[key], depth + 1)
                if answer is not None:
                    return answer
            return None

        if isinstance(value, list):
            for child in value:
                answer = self._extract_answer_from_dump(child, depth + 1)
                if answer is not None:
                    return answer

        return None

    def _extract_answer_text(self, response: Any) -> Optional[str]:
        answer = self._normalize_answer_text(self._get_field(response, "output_text"))
        if answer is not None:
            return answer

        output_items = self._get_field(response, "output")
        if isinstance(output_items, list):
            for item in output_items:
                answer = self._extract_answer_from_output_item(item)
                if answer is not None:
                    return answer

        dumped = self._response_dump_json(response)
        if dumped is not None:
            return self._extract_answer_from_dump(dumped)

        return None

    def _build_model_input(
        self,
        request: Mapping[str, Any],
        selected_sources: Sequence[str],
        texts: Mapping[str, str],
    ) -> str:
        payload = [
            "REQUEST_PACKET",
            json.dumps(request, indent=2, ensure_ascii=True),
            "",
            "SELECTED_SOURCE_PATHS",
            json.dumps(list(selected_sources), indent=2, ensure_ascii=True),
            "",
            "SELECTED_SOURCE_CONTENTS",
        ]

        for path in selected_sources:
            payload.append(f"=== BEGIN SOURCE: {path} ===")
            payload.append(texts[path])
            payload.append(f"=== END SOURCE: {path} ===")
            payload.append("")

        return "\n".join(payload).strip()

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
            response = self._client.responses.create(
                model=self._model,
                instructions=SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=MAX_OUTPUT_TOKENS,
                store=False,
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        return self._extract_answer_text(response)

    def _local_next_read_paths(self, question_class: str, status: str) -> Tuple[str, ...]:
        if status in {"refused", "out_of_scope"}:
            return ()

        if question_class == "current_state":
            return ()

        if question_class == "what_stands_now":
            return WHAT_STANDS_NOW_NEXT_READ_PATHS

        raise HarnessError(f"Unhandled question_class for next-read generation: {question_class!r}")

    def _selected_surface_phrase(self, question_class: str, selected_sources: Sequence[str]) -> str:
        if question_class == "current_state":
            if tuple(selected_sources) == ("CURRENT_STATE__REPO_ENTRY.md",):
                return "the approved current-state entry surface"
            return "the approved current-state entry surface and the approved standing-review surface"

        if question_class == "what_stands_now":
            return "the approved standing-review surface"

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
                    "and downgraded a drifted answer conservatively."
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

        if any(path not in self.config.allowed_sources for path in plan.next_read_paths):
            return PacketTrace(
                sources_used=plan.sources_used,
                next_read_paths=plan.next_read_paths,
                provenance_ok=False,
                public_note=PROVENANCE_DOWNGRADE_AMBIGUITY_NOTE,
                debug_note="next_read_paths exceeded the narrowed vessel boundary.",
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
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_answer_only_v2.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/api_vessel_answer_only_v2.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    vessel = CurrentStateWhatStandsAnswerOnlyAPIVesselV2.from_environment()
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
        print(f"api_vessel_answer_only_v2 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
