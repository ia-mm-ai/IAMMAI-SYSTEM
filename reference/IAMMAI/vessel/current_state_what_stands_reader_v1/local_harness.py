#!/usr/bin/env python3
"""
Local non-bypassable harness for current_state_what_stands_reader_v1.

This harness enforces the narrowed vessel's manifest, input contract, output
contract, explicit source boundaries, and bounded refusal posture before any
later API-backed vessel exists.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional, Sequence, Tuple


SCRIPT_PATH = Path(__file__).resolve()
VESSEL_ROOT = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_PATH.parents[2]

MANIFEST_PATH = VESSEL_ROOT / "source_manifest.json"
CONTRACT_PATH = VESSEL_ROOT / "CONTRACT.md"
INPUT_SCHEMA_PATH = VESSEL_ROOT / "input_packet.schema.json"
OUTPUT_SCHEMA_PATH = VESSEL_ROOT / "output_packet.schema.json"
EVAL_CORPUS_PATH = VESSEL_ROOT / "eval_corpus.json"

EXPECTED_CONTRACT_ID = "current_state_what_stands_reader_v1"
EXPECTED_ALLOWED_SOURCES = (
    "CURRENT_STATE__REPO_ENTRY.md",
    "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
)
EXPECTED_ALLOWED_QUESTION_CLASSES = (
    "current_state",
    "what_stands_now",
)
EXPECTED_PRIMARY_RANKS = (
    "current_state_surface",
    "standing_review_surface",
)
EXPECTED_STATUSES = (
    "answered",
    "refused",
    "out_of_scope",
    "insufficient_grounding",
)
EXPECTED_REFUSAL_REASONS = (
    "question_class_not_allowed",
    "requires_unapproved_sources",
    "would_require_interpretive_sovereignty",
    "would_mutate_or_finalize",
    "insufficient_rank_clarity",
)
EXPECTED_DERIVATIVE_STATUS = "derivative_reader"

REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9._:-]+$")
FILE_REFERENCE_RE = re.compile(r"\b[^\s`\"']+\.(?:md|json|py|pdf)\b")

INPUT_KEYS = {
    "contract_id",
    "request_id",
    "question_class",
    "question_text",
    "context_note",
}
OUTPUT_KEYS = {
    "contract_id",
    "request_id",
    "status",
    "answer",
    "primary_rank_used",
    "sources_used",
    "derivative_status",
    "boundedness_note",
    "next_read_paths",
    "refusal_reason",
    "ambiguity_note",
}


class HarnessError(Exception):
    """Raised for bounded local harness failures."""


@dataclass(frozen=True)
class HarnessConfig:
    contract_id: str
    allowed_sources: Tuple[str, ...]
    allowed_question_classes: Tuple[str, ...]
    allowed_statuses: Tuple[str, ...]
    allowed_primary_ranks: Tuple[str, ...]
    allowed_refusal_reasons: Tuple[str, ...]
    derivative_status: str


@dataclass(frozen=True)
class AnswerPlan:
    status: str
    answer: str
    primary_rank_used: str
    sources_used: Tuple[str, ...]
    boundedness_note: str
    next_read_paths: Tuple[str, ...]
    refusal_reason: Optional[str]
    ambiguity_note: Optional[str]


class CurrentStateWhatStandsHarness:
    """Local shell for the narrowed current-state / what-stands reader."""

    SOURCE_SCOPE_MAP: Mapping[str, Tuple[str, ...]] = {
        "current_state": (
            "CURRENT_STATE__REPO_ENTRY.md",
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
        ),
        "what_stands_now": (
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
        ),
    }

    PRIMARY_RANK_MAP: Mapping[str, str] = {
        "current_state": "current_state_surface",
        "what_stands_now": "standing_review_surface",
    }

    def __init__(self) -> None:
        self._source_cache: Dict[str, str] = {}
        self.config = self._load_config()

    def _load_json_object(self, path: Path) -> Dict[str, Any]:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except OSError as exc:
            raise HarnessError(f"Failed to read JSON file {path}: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise HarnessError(f"Invalid JSON in {path}: {exc}") from exc

        if not isinstance(payload, dict):
            raise HarnessError(f"Expected JSON object in {path}, got {type(payload).__name__}")
        return payload

    def _load_text(self, path: Path) -> str:
        try:
            return path.read_text(encoding="utf-8")
        except OSError as exc:
            raise HarnessError(f"Failed to read text file {path}: {exc}") from exc

    def _expect_mapping(self, payload: Mapping[str, Any], key: str) -> Mapping[str, Any]:
        value = payload.get(key)
        if not isinstance(value, Mapping):
            raise HarnessError(f"Expected object at key {key!r}.")
        return value

    def _expect_string(self, payload: Mapping[str, Any], key: str) -> str:
        value = payload.get(key)
        if not isinstance(value, str):
            raise HarnessError(f"Expected string at key {key!r}.")
        return value

    def _expect_string_list(self, payload: Mapping[str, Any], key: str) -> List[str]:
        value = payload.get(key)
        if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
            raise HarnessError(f"Expected string array at key {key!r}.")
        return list(value)

    def _load_config(self) -> HarnessConfig:
        manifest = self._load_json_object(MANIFEST_PATH)
        contract_text = self._load_text(CONTRACT_PATH)
        input_schema = self._load_json_object(INPUT_SCHEMA_PATH)
        output_schema = self._load_json_object(OUTPUT_SCHEMA_PATH)

        if not contract_text.strip():
            raise HarnessError("CONTRACT.md must not be empty.")

        contract_identity = self._expect_mapping(manifest, "contract_identity")
        access_posture = self._expect_mapping(manifest, "access_posture")

        contract_id = self._expect_string(contract_identity, "contract_id")
        if contract_id != EXPECTED_CONTRACT_ID:
            raise HarnessError("Manifest contract_id does not match the narrowed vessel id.")

        allowed_sources = tuple(self._expect_string_list(manifest, "allowed_sources"))
        if allowed_sources != EXPECTED_ALLOWED_SOURCES:
            raise HarnessError("Manifest allowed_sources does not match the narrowed vessel boundary.")

        allowed_question_classes = tuple(self._expect_string_list(manifest, "allowed_question_classes"))
        if allowed_question_classes != EXPECTED_ALLOWED_QUESTION_CLASSES:
            raise HarnessError("Manifest allowed_question_classes does not match the narrowed vessel boundary.")

        if access_posture.get("read_only") is not True:
            raise HarnessError("Manifest read_only posture must be true.")
        if access_posture.get("derivative_only") is not True:
            raise HarnessError("Manifest derivative_only posture must be true.")
        if access_posture.get("web_access") is not False:
            raise HarnessError("Manifest web_access posture must be false.")
        if access_posture.get("mutation_allowed") is not False:
            raise HarnessError("Manifest mutation_allowed posture must be false.")

        if input_schema.get("type") != "object" or input_schema.get("additionalProperties") is not False:
            raise HarnessError("Input schema must be an object with additionalProperties false.")
        if output_schema.get("type") != "object" or output_schema.get("additionalProperties") is not False:
            raise HarnessError("Output schema must be an object with additionalProperties false.")

        input_properties = self._expect_mapping(input_schema, "properties")
        input_contract = self._expect_mapping(input_properties, "contract_id")
        if input_contract.get("const") != contract_id:
            raise HarnessError("Input schema contract_id const does not match manifest contract_id.")

        input_question_class = self._expect_mapping(input_properties, "question_class")
        input_enum = input_question_class.get("enum")
        if list(allowed_question_classes) != list(input_enum or []):
            raise HarnessError("Input schema question_class enum does not match the manifest.")

        output_properties = self._expect_mapping(output_schema, "properties")
        output_contract = self._expect_mapping(output_properties, "contract_id")
        if output_contract.get("const") != contract_id:
            raise HarnessError("Output schema contract_id const does not match manifest contract_id.")

        status_property = self._expect_mapping(output_properties, "status")
        primary_rank_property = self._expect_mapping(output_properties, "primary_rank_used")
        refusal_reason_property = self._expect_mapping(output_properties, "refusal_reason")
        derivative_property = self._expect_mapping(output_properties, "derivative_status")

        allowed_statuses = tuple(status_property.get("enum") or [])
        if allowed_statuses != EXPECTED_STATUSES:
            raise HarnessError("Output schema status enum does not match the narrowed vessel contract.")

        allowed_primary_ranks = tuple(primary_rank_property.get("enum") or [])
        if allowed_primary_ranks != EXPECTED_PRIMARY_RANKS:
            raise HarnessError("Output schema primary_rank_used enum does not match the narrowed vessel contract.")

        refusal_reason_enum = tuple(
            item for item in (refusal_reason_property.get("enum") or []) if isinstance(item, str)
        )
        if refusal_reason_enum != EXPECTED_REFUSAL_REASONS:
            raise HarnessError("Output schema refusal_reason enum does not match the narrowed vessel contract.")

        derivative_status = derivative_property.get("const")
        if derivative_status != EXPECTED_DERIVATIVE_STATUS:
            raise HarnessError("Output schema derivative_status const does not match the narrowed vessel contract.")

        return HarnessConfig(
            contract_id=contract_id,
            allowed_sources=allowed_sources,
            allowed_question_classes=allowed_question_classes,
            allowed_statuses=allowed_statuses,
            allowed_primary_ranks=allowed_primary_ranks,
            allowed_refusal_reasons=refusal_reason_enum,
            derivative_status=str(derivative_status),
        )

    def _validate_input_packet(self, packet: Any) -> Dict[str, Any]:
        if not isinstance(packet, dict):
            raise HarnessError("Input packet must be a JSON object.")

        extra_keys = sorted(set(packet.keys()) - INPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Input packet contains unsupported fields: {extra_keys}")

        missing_keys = sorted({"contract_id", "request_id", "question_class", "question_text"} - set(packet.keys()))
        if missing_keys:
            raise HarnessError(f"Input packet is missing required fields: {missing_keys}")

        contract_id = packet.get("contract_id")
        request_id = packet.get("request_id")
        question_class = packet.get("question_class")
        question_text = packet.get("question_text")
        context_note = packet.get("context_note", None)

        if contract_id != self.config.contract_id:
            raise HarnessError("Input packet contract_id does not match this narrowed vessel.")

        if not isinstance(request_id, str) or not request_id or len(request_id) > 128:
            raise HarnessError("Input packet request_id must be a non-empty bounded string.")
        if not REQUEST_ID_RE.fullmatch(request_id):
            raise HarnessError("Input packet request_id contains unsupported characters.")

        if question_class not in self.config.allowed_question_classes:
            raise HarnessError("Input packet question_class is outside the allowed narrowed vessel set.")

        if not isinstance(question_text, str) or not question_text.strip() or len(question_text) > 4000:
            raise HarnessError("Input packet question_text must be a non-empty bounded string.")

        if context_note is not None:
            if not isinstance(context_note, str):
                raise HarnessError("Input packet context_note must be a string or null.")
            if len(context_note) > 500:
                raise HarnessError("Input packet context_note exceeds the bounded length.")

        return {
            "contract_id": contract_id,
            "request_id": request_id,
            "question_class": question_class,
            "question_text": question_text,
            "context_note": context_note,
        }

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
        if any(path not in self.config.allowed_sources for path in next_read_paths):
            raise HarnessError("Output packet next_read_paths exceeds the manifest boundary.")

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

        return packet

    def _question_primary_rank(self, question_class: str) -> str:
        primary_rank = self.PRIMARY_RANK_MAP.get(question_class)
        if primary_rank is None:
            raise HarnessError(f"No primary rank is configured for question_class={question_class!r}.")
        return primary_rank

    def _allowed_source_scope(self, question_class: str) -> Tuple[str, ...]:
        source_scope = self.SOURCE_SCOPE_MAP.get(question_class)
        if source_scope is None:
            raise HarnessError(f"No source scope is configured for question_class={question_class!r}.")
        return source_scope

    def _read_source(self, relative_path: str) -> str:
        cached = self._source_cache.get(relative_path)
        if cached is not None:
            return cached

        path = (REPO_ROOT / relative_path).resolve()
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            raise HarnessError(f"Failed to read approved source {relative_path}: {exc}") from exc

        self._source_cache[relative_path] = text
        return text

    def _read_selected_sources(self, selected_sources: Sequence[str]) -> Dict[str, str]:
        texts: Dict[str, str] = {}
        for path in selected_sources:
            if path not in self.config.allowed_sources:
                raise HarnessError(f"Selected source {path!r} exceeds the manifest boundary.")
            texts[path] = self._read_source(path)
        return texts

    def _question_mentions_unapproved_sources(self, question_text: str) -> bool:
        referenced_paths = {
            match.rstrip(".,:;")
            for match in FILE_REFERENCE_RE.findall(question_text)
        }
        return any(path not in self.config.allowed_sources for path in referenced_paths)

    def _is_mutation_request(self, question_text: str) -> bool:
        text = question_text.lower()
        strong_verbs = ("rewrite", "edit", "mutate", "finalize")
        target_markers = (".md", ".json", "repo file", "ranked surface", "surface", "entry", "review")
        if any(verb in text for verb in strong_verbs) and any(marker in text for marker in target_markers):
            return True
        if "update" in text and any(marker in text for marker in target_markers):
            return True
        return False

    def _is_interpretive_sovereignty_request(self, question_text: str) -> bool:
        text = question_text.lower()
        patterns = (
            "state the doctrine",
            "new law",
            "governing rule",
            "govern future cases",
            "decide whether",
            "qualifies as lawful egress",
            "seam case",
            "seam-case",
            "repo-wide interpretation",
            "total repo-wide interpretation",
            "broad doctrinal judgment",
        )
        return any(pattern in text for pattern in patterns)

    def _is_insufficient_grounding_request(self, question_text: str) -> bool:
        text = question_text.lower()
        conclusive_markers = (
            "single approved surface",
            "single conclusive surface",
            "conclusively ratifies",
            "conclusively settles",
            "one approved surface",
        )
        finality_markers = (
            "final standing",
            "final v1 standing",
            "total closure",
        )
        return any(marker in text for marker in conclusive_markers) and any(
            marker in text for marker in finality_markers
        )

    def _choose_sources_for_request(self, question_class: str, question_text: str) -> Tuple[str, ...]:
        source_scope = self._allowed_source_scope(question_class)
        if question_class == "current_state":
            text = question_text.lower()
            needs_standing_context = any(
                marker in text
                for marker in (
                    "final standing",
                    "what stands",
                    "stands now",
                    "total closure",
                    "closure",
                )
            )
            if needs_standing_context:
                return source_scope
            return (source_scope[0],)
        return source_scope

    def _boundedness_note(self, question_class: str, status: str) -> str:
        if status == "answered":
            if question_class == "current_state":
                return "This vessel returned a bounded derivative current-state reading from approved local surfaces only."
            return "This vessel returned a bounded derivative what-stands reading from approved local surfaces only."
        if status == "insufficient_grounding":
            return "This vessel stayed inside its approved source boundary and returned insufficient grounding rather than counterfeit certainty."
        if status == "refused":
            return "This vessel remained inside its read-only narrowed role and returned a visible refusal."
        if status == "out_of_scope":
            return "This vessel remained inside its manifest-bounded scope and returned a visible out-of-scope result."
        raise HarnessError(f"Unhandled status {status!r} for boundedness note.")

    def _next_read_paths(
        self,
        question_class: str,
        selected_sources: Sequence[str],
        status: str,
    ) -> Tuple[str, ...]:
        if status in {"refused", "out_of_scope"}:
            return ()

        if question_class == "current_state" and tuple(selected_sources) == ("CURRENT_STATE__REPO_ENTRY.md",):
            return ("v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",)

        if question_class == "what_stands_now":
            return ("CURRENT_STATE__REPO_ENTRY.md",)

        return ()

    def _answered_plan(
        self,
        question_class: str,
        selected_sources: Tuple[str, ...],
        source_texts: Mapping[str, str],
    ) -> AnswerPlan:
        if question_class == "current_state":
            _ = source_texts["CURRENT_STATE__REPO_ENTRY.md"]
            if len(selected_sources) == 1:
                answer = (
                    "The repository currently reads as frozen root beside a real admissible v1 "
                    "derivation line with preserved proof and preserved readability. The approved "
                    "current-state surface also keeps the boundary that this does not mean all of "
                    "v1 is finished or that final standing has already been settled."
                )
            else:
                _ = source_texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"]
                answer = (
                    "The repository currently reads as frozen root beside a real admissible v1 "
                    "derivation line with preserved proof and preserved readability, and the "
                    "approved standing review keeps that present condition materially standing "
                    "without treating it as total closure."
                )
        elif question_class == "what_stands_now":
            _ = source_texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"]
            answer = (
                "What now clearly stands is a bounded materially standing v1 line: root remains "
                "the frozen source-side lineage body, v1 stands as a real admissible proof-bearing "
                "derivation line, proof and proof readability stand, and the present review keeps "
                "that reading short of total closure."
            )
        else:  # pragma: no cover - guarded by input validation and source scope map
            raise HarnessError(f"Unhandled answered question_class {question_class!r}.")

        return AnswerPlan(
            status="answered",
            answer=answer,
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._boundedness_note(question_class, "answered"),
            next_read_paths=self._next_read_paths(question_class, selected_sources, "answered"),
            refusal_reason=None,
            ambiguity_note=None,
        )

    def _insufficient_grounding_plan(
        self,
        question_class: str,
        selected_sources: Tuple[str, ...],
        source_texts: Mapping[str, str],
    ) -> AnswerPlan:
        if question_class == "what_stands_now":
            _ = source_texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"]
        else:
            for path in selected_sources:
                _ = source_texts[path]

        answer = (
            "The approved surfaces support a bounded reading that real present standing exists in "
            "a material sense, but they do not provide a single conclusive surface that finally "
            "ratifies total v1 standing."
        )

        return AnswerPlan(
            status="insufficient_grounding",
            answer=answer,
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=selected_sources,
            boundedness_note=self._boundedness_note(question_class, "insufficient_grounding"),
            next_read_paths=self._next_read_paths(question_class, selected_sources, "insufficient_grounding"),
            refusal_reason=None,
            ambiguity_note=(
                "The selected approved sources were insufficient to support a single conclusive "
                "answer without exceeding bounded provenance."
            ),
        )

    def _refusal_plan(self, question_class: str, status: str, refusal_reason: str) -> AnswerPlan:
        return AnswerPlan(
            status=status,
            answer="",
            primary_rank_used=self._question_primary_rank(question_class),
            sources_used=(),
            boundedness_note=self._boundedness_note(question_class, status),
            next_read_paths=(),
            refusal_reason=refusal_reason,
            ambiguity_note=None,
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

        return self._answered_plan(question_class, selected_sources, source_texts)

    def _packet_from_plan(self, request: Mapping[str, Any], plan: AnswerPlan) -> Dict[str, Any]:
        packet = {
            "contract_id": self.config.contract_id,
            "request_id": str(request["request_id"]),
            "status": plan.status,
            "answer": plan.answer,
            "primary_rank_used": plan.primary_rank_used,
            "sources_used": list(plan.sources_used),
            "derivative_status": self.config.derivative_status,
            "boundedness_note": plan.boundedness_note,
            "next_read_paths": list(plan.next_read_paths),
            "refusal_reason": plan.refusal_reason,
            "ambiguity_note": plan.ambiguity_note,
        }
        return self._validate_output_packet(packet)

    def answer_request(self, packet: Any) -> Dict[str, Any]:
        request = self._validate_input_packet(packet)
        plan = self._render_answer_plan(request)
        return self._packet_from_plan(request, plan)

    def _load_eval_corpus(self) -> Dict[str, Any]:
        corpus = self._load_json_object(EVAL_CORPUS_PATH)
        if corpus.get("contract_id") != self.config.contract_id:
            raise HarnessError("Eval corpus contract_id does not match the narrowed vessel.")

        cases = corpus.get("cases")
        if not isinstance(cases, list):
            raise HarnessError("Eval corpus cases must be an array.")

        return corpus

    def _evaluate_case(self, case: Mapping[str, Any]) -> List[str]:
        reasons: List[str] = []
        eval_id = str(case.get("eval_id", "unknown_eval"))
        input_packet = case.get("input_packet")

        try:
            output = self.answer_request(input_packet)
        except Exception as exc:
            return [f"{eval_id}: harness raised {type(exc).__name__}: {exc}"]

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

    def run_eval(self) -> int:
        corpus = self._load_eval_corpus()
        cases = corpus["cases"]
        failures: List[Tuple[str, List[str]]] = []

        for case in cases:
            if not isinstance(case, Mapping):
                failures.append(("unknown_eval", ["Eval case is not a JSON object."]))
                continue

            eval_id = str(case.get("eval_id", "unknown_eval"))
            reasons = self._evaluate_case(case)
            if reasons:
                failures.append((eval_id, reasons))

        total = len(cases)
        failed = len(failures)
        passed = total - failed

        print(f"Eval summary: total={total} passed={passed} failed={failed}")
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
        "  python vessel/current_state_what_stands_reader_v1/local_harness.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_what_stands_reader_v1/local_harness.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    harness = CurrentStateWhatStandsHarness()
    mode = argv[1]

    if mode == "answer":
        if len(argv) != 3:
            print_usage()
            return 2
        packet = load_input_packet(argv[2])
        output = harness.answer_request(packet)
        print(json.dumps(output, indent=2))
        return 0

    if mode == "eval":
        if len(argv) != 2:
            print_usage()
            return 2
        return harness.run_eval()

    print_usage()
    return 2


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv))
    except HarnessError as exc:
        print(f"local_harness error: {exc}", file=sys.stderr)
        raise SystemExit(2)
