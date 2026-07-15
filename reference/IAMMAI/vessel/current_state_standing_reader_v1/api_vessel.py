#!/usr/bin/env python3
"""
API-backed vessel for current_state_standing_reader_v1.

This file inserts the OpenAI Responses API inside the already-proved local
shell. The local shell remains sovereign over manifest access, packet
validation, source selection, provenance, refusal visibility, and final packet
assembly. The model only drafts bounded answer content.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple

from openai import OpenAI

from local_harness_v3 import (
    FILE_REFERENCE_RE,
    REPO_ROOT,
    AnswerPlan,
    CurrentStateStandingReaderHarnessV3,
    HarnessError,
    PacketTrace,
)


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
            "maxLength": 6000,
        },
        "boundedness_note": {
            "type": "string",
            "minLength": 1,
            "maxLength": 500,
        },
        "next_read_paths": {
            "type": "array",
            "items": {
                "type": "string",
                "minLength": 1,
            },
            "uniqueItems": True,
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
            "maxLength": 500,
        },
    },
}

SYSTEM_PROMPT = """You are drafting bounded derivative answer content for the IAMMAI current_state_standing_reader_v1 vessel.

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


class CurrentStateStandingReaderAPIVessel(CurrentStateStandingReaderHarnessV3):
    """API-backed vessel that preserves the v3 local shell as the higher authority."""

    def __init__(self, *, api_key: str, model: str) -> None:
        self._api_key = api_key
        self._model = model
        self._client = OpenAI(api_key=api_key)
        super().__init__()

    @classmethod
    def from_environment(cls) -> "CurrentStateStandingReaderAPIVessel":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise HarnessError("OPENAI_API_KEY is required for api_vessel.py.")

        model = os.environ.get("OPENAI_MODEL", "gpt-5.4")
        if not model.strip():
            raise HarnessError("OPENAI_MODEL, if set, must not be empty.")

        return cls(api_key=api_key, model=model)

    def _extract_response_text(self, response: Any) -> str:
        output_text = getattr(response, "output_text", None)
        if isinstance(output_text, str) and output_text.strip():
            return output_text

        output_items = getattr(response, "output", None)
        collected: List[str] = []
        if isinstance(output_items, list):
            for item in output_items:
                content_items = getattr(item, "content", None)
                if not isinstance(content_items, list):
                    continue
                for content in content_items:
                    if getattr(content, "type", None) == "output_text":
                        text_value = getattr(content, "text", None)
                        if isinstance(text_value, str) and text_value:
                            collected.append(text_value)

        combined = "".join(collected).strip()
        if combined:
            return combined

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
        if len(set(next_read_paths)) != len(next_read_paths):
            raise HarnessError("Draft response next_read_paths must not contain duplicates.")

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
            "next_read_paths": next_read_paths,
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
            response = self._client.responses.create(
                model=self._model,
                instructions=SYSTEM_PROMPT,
                input=model_input,
                max_output_tokens=1200,
                temperature=0,
                store=False,
                text={
                    "format": {
                        "type": "json_schema",
                        "name": "current_state_standing_reader_v1_draft",
                        "schema": DRAFT_SCHEMA,
                        "strict": True,
                    }
                },
            )
        except Exception as exc:
            raise HarnessError(f"OpenAI Responses API call failed: {exc}") from exc

        try:
            draft_text = self._extract_response_text(response)
        except HarnessError:
            raise
        except Exception as exc:
            raise HarnessError(f"Failed to extract draft output text: {exc}") from exc

        try:
            draft_payload = json.loads(draft_text)
        except json.JSONDecodeError as exc:
            raise HarnessError(f"Model returned invalid JSON draft: {exc}") from exc

        return self._validate_draft(draft_payload)

    def _provenance_self_check(self, plan: AnswerPlan) -> PacketTrace:
        allowed_path_mentions = set(plan.consulted_sources) | set(plan.next_read_paths)
        text_fields = {
            "answer": plan.answer,
            "boundedness_note": plan.boundedness_note,
            "ambiguity_note": plan.ambiguity_note or "",
        }

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

        consulted_sources: Tuple[str, ...] = tuple(selected_sources)

        return AnswerPlan(
            status=str(draft["status"]),
            answer=str(draft["answer"]),
            primary_rank_used=self._question_primary_rank(question_class),
            consulted_sources=consulted_sources,
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
        "  python vessel/current_state_standing_reader_v1/api_vessel.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_standing_reader_v1/api_vessel.py eval\n"
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

    vessel = CurrentStateStandingReaderAPIVessel.from_environment()

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
        print(f"api_vessel error: {exc}", file=sys.stderr)
        raise SystemExit(2)
