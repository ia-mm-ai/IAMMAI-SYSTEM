#!/usr/bin/env python3
"""
Local non-bypassable harness v3 for current_state_standing_reader_v1.

This additive harness preserves the first vessel's narrow role while making
provenance stricter across answer text and note fields, and locking the old
latest-thresholds leak with a built-in regression eval.
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

REQUEST_ID_RE = re.compile(r"^[A-Za-z0-9._:-]+$")
FILE_REFERENCE_RE = re.compile(r"\b[^\s`\"']+\.(?:md|json|py|pdf)\b")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")

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
    """Raised for local shell integrity failures and malformed packets."""


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
class PacketTrace:
    consulted_sources: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    provenance_ok: bool
    public_note: Optional[str]
    debug_note: Optional[str]


@dataclass(frozen=True)
class AnswerPlan:
    status: str
    answer: str
    primary_rank_used: str
    consulted_sources: Tuple[str, ...]
    next_read_paths: Tuple[str, ...]
    refusal_reason: Optional[str]
    ambiguity_note: Optional[str]
    boundedness_note: str


class CurrentStateStandingReaderHarnessV3:
    """Tightened local shell for the first bounded current-state vessel."""

    SOURCE_SCOPE_MAP: Mapping[str, Tuple[str, ...]] = {
        "current_state": (
            "CURRENT_STATE__REPO_ENTRY.md",
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
        ),
        "current_governing_surfaces": (
            "RANKED_SURFACE_INDEX.md",
            "CONSTITUTIONAL_VERSION_NOTE.md",
            "CURRENT_STATE__REPO_ENTRY.md",
        ),
        "what_stands_now": (
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
        ),
        "latest_thresholds": (
            "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
            "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            "CURRENT_READABILITY_SURFACES.md",
        ),
        "what_remains_open": (
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
        ),
        "where_to_read_next": (
            "CURRENT_READABILITY_SURFACES.md",
            "RANKED_SURFACE_INDEX.md",
            "CURRENT_STATE__REPO_ENTRY.md",
        ),
    }

    PRIMARY_RANK_MAP: Mapping[str, str] = {
        "current_state": "current_state_surface",
        "current_governing_surfaces": "navigation_surface",
        "what_stands_now": "standing_review_surface",
        "latest_thresholds": "threshold_account_surface",
        "what_remains_open": "standing_review_surface",
        "where_to_read_next": "readability_pointer_surface",
    }

    SOURCE_CLASS_MAP: Mapping[str, str] = {
        "CURRENT_STATE__REPO_ENTRY.md": "current-state",
        "RANKED_SURFACE_INDEX.md": "navigation",
        "CONSTITUTIONAL_VERSION_NOTE.md": "constitutional clarification",
        "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md": "standing-review",
        "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md": "threshold-account",
        "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md": "threshold-account",
        "CURRENT_READABILITY_SURFACES.md": "readability-pointer",
    }

    SURFACE_CLASS_RULES: Tuple[Tuple[str, Tuple[str, ...]], ...] = (
        ("current-state surface", ("CURRENT_STATE__REPO_ENTRY.md",)),
        ("current-state surfaces", ("CURRENT_STATE__REPO_ENTRY.md",)),
        ("navigation surface", ("RANKED_SURFACE_INDEX.md",)),
        ("navigation surfaces", ("RANKED_SURFACE_INDEX.md",)),
        ("constitutional clarification surface", ("CONSTITUTIONAL_VERSION_NOTE.md",)),
        ("constitutional clarification surfaces", ("CONSTITUTIONAL_VERSION_NOTE.md",)),
        (
            "standing-review surface",
            ("v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",),
        ),
        (
            "standing-review surfaces",
            ("v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",),
        ),
        (
            "threshold-account surface",
            (
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
            ),
        ),
        (
            "threshold-account surfaces",
            (
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
            ),
        ),
        ("readability-pointer surface", ("CURRENT_READABILITY_SURFACES.md",)),
        ("readability-pointer surfaces", ("CURRENT_READABILITY_SURFACES.md",)),
    )

    def __init__(self) -> None:
        self._source_cache: Dict[str, str] = {}
        self.config = self._load_config()
        self._validate_source_scope_map()

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

    def _load_config(self) -> HarnessConfig:
        manifest = self._load_json_object(MANIFEST_PATH)
        _contract_text = self._load_text(CONTRACT_PATH)
        input_schema = self._load_json_object(INPUT_SCHEMA_PATH)
        output_schema = self._load_json_object(OUTPUT_SCHEMA_PATH)

        identity = self._expect_mapping(manifest, "contract_identity")
        access = self._expect_mapping(manifest, "access_posture")

        contract_id = self._expect_string(identity, "contract_id")
        allowed_sources = tuple(self._expect_string_list(manifest, "allowed_sources"))
        allowed_question_classes = tuple(
            self._expect_string_list(manifest, "allowed_question_classes")
        )

        if access.get("read_only") is not True:
            raise HarnessError("Manifest read_only posture must be true.")
        if access.get("derivative_only") is not True:
            raise HarnessError("Manifest derivative_only posture must be true.")
        if access.get("web_access") is not False:
            raise HarnessError("Manifest web_access posture must be false.")
        if access.get("mutation_allowed") is not False:
            raise HarnessError("Manifest mutation_allowed posture must be false.")

        input_properties = self._expect_mapping(input_schema, "properties")
        input_contract = input_properties.get("contract_id")
        if not isinstance(input_contract, Mapping):
            raise HarnessError("Input schema is missing contract_id property.")
        if input_contract.get("const") != contract_id:
            raise HarnessError("Input schema contract_id does not match manifest contract_id.")

        input_question_class = input_properties.get("question_class")
        if not isinstance(input_question_class, Mapping):
            raise HarnessError("Input schema is missing question_class property.")
        if list(allowed_question_classes) != list(input_question_class.get("enum") or []):
            raise HarnessError("Input schema question_class enum does not match manifest.")

        output_properties = self._expect_mapping(output_schema, "properties")
        output_contract = output_properties.get("contract_id")
        if not isinstance(output_contract, Mapping):
            raise HarnessError("Output schema is missing contract_id property.")
        if output_contract.get("const") != contract_id:
            raise HarnessError("Output schema contract_id does not match manifest contract_id.")

        derivative_status_property = output_properties.get("derivative_status")
        if not isinstance(derivative_status_property, Mapping):
            raise HarnessError("Output schema is missing derivative_status property.")
        derivative_status = derivative_status_property.get("const")
        if not isinstance(derivative_status, str):
            raise HarnessError("Output schema derivative_status const is missing.")

        status_property = output_properties.get("status")
        primary_rank_property = output_properties.get("primary_rank_used")
        refusal_reason_property = output_properties.get("refusal_reason")
        if not isinstance(status_property, Mapping):
            raise HarnessError("Output schema is missing status property.")
        if not isinstance(primary_rank_property, Mapping):
            raise HarnessError("Output schema is missing primary_rank_used property.")
        if not isinstance(refusal_reason_property, Mapping):
            raise HarnessError("Output schema is missing refusal_reason property.")

        allowed_statuses = tuple(self._expect_string_sequence(status_property.get("enum")))
        allowed_primary_ranks = tuple(
            self._expect_string_sequence(primary_rank_property.get("enum"))
        )
        allowed_refusal_reasons = tuple(
            value
            for value in self._expect_sequence(refusal_reason_property.get("enum"))
            if isinstance(value, str)
        )

        return HarnessConfig(
            contract_id=contract_id,
            allowed_sources=allowed_sources,
            allowed_question_classes=allowed_question_classes,
            allowed_statuses=allowed_statuses,
            allowed_primary_ranks=allowed_primary_ranks,
            allowed_refusal_reasons=allowed_refusal_reasons,
            derivative_status=derivative_status,
        )

    def _validate_source_scope_map(self) -> None:
        for question_class, source_scope in self.SOURCE_SCOPE_MAP.items():
            if question_class not in self.config.allowed_question_classes:
                raise HarnessError(f"Source scope map contains unapproved question class: {question_class}")
            for path in source_scope:
                if path not in self.config.allowed_sources:
                    raise HarnessError(f"Source scope map contains non-manifest source: {path}")
        for question_class, primary_rank in self.PRIMARY_RANK_MAP.items():
            if question_class not in self.config.allowed_question_classes:
                raise HarnessError(f"Primary rank map contains unapproved question class: {question_class}")
            if primary_rank not in self.config.allowed_primary_ranks:
                raise HarnessError(f"Primary rank map contains unapproved primary rank: {primary_rank}")

    def _expect_mapping(self, mapping: Mapping[str, Any], key: str) -> Mapping[str, Any]:
        value = mapping.get(key)
        if not isinstance(value, Mapping):
            raise HarnessError(f"Expected object at key {key!r}.")
        return value

    def _expect_string(self, mapping: Mapping[str, Any], key: str) -> str:
        value = mapping.get(key)
        if not isinstance(value, str):
            raise HarnessError(f"Expected string at key {key!r}.")
        return value

    def _expect_sequence(self, value: Any) -> Sequence[Any]:
        if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
            raise HarnessError("Expected JSON array.")
        return value

    def _expect_string_sequence(self, value: Any) -> List[str]:
        sequence = self._expect_sequence(value)
        if not all(isinstance(item, str) for item in sequence):
            raise HarnessError("Expected array of strings.")
        return list(sequence)

    def _expect_string_list(self, mapping: Mapping[str, Any], key: str) -> List[str]:
        return self._expect_string_sequence(mapping.get(key))

    def _read_allowed_source(self, relative_path: str) -> str:
        if relative_path not in self.config.allowed_sources:
            raise HarnessError(f"Attempted to read non-manifest source: {relative_path}")
        if relative_path in self._source_cache:
            return self._source_cache[relative_path]

        text = self._load_text(REPO_ROOT / relative_path)
        self._source_cache[relative_path] = text
        return text

    def validate_input_packet(self, packet: Any) -> Dict[str, Any]:
        if not isinstance(packet, dict):
            raise HarnessError("Input packet must be a JSON object.")

        extra_keys = sorted(set(packet.keys()) - INPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Input packet contains unsupported fields: {extra_keys}")

        required_keys = {"contract_id", "request_id", "question_class", "question_text"}
        missing_keys = sorted(required_keys - set(packet.keys()))
        if missing_keys:
            raise HarnessError(f"Input packet is missing required fields: {missing_keys}")

        contract_id = packet.get("contract_id")
        if contract_id != self.config.contract_id:
            raise HarnessError("Input packet contract_id does not match harness contract.")

        request_id = packet.get("request_id")
        if not isinstance(request_id, str) or not request_id or not REQUEST_ID_RE.match(request_id):
            raise HarnessError("Input packet request_id must be a bounded identifier string.")

        question_class = packet.get("question_class")
        if question_class not in self.config.allowed_question_classes:
            raise HarnessError("Input packet question_class is not allowed by the manifest.")

        question_text = packet.get("question_text")
        if not isinstance(question_text, str) or not question_text.strip():
            raise HarnessError("Input packet question_text must be a non-empty string.")

        context_note = packet.get("context_note", None)
        if context_note is not None and not isinstance(context_note, str):
            raise HarnessError("Input packet context_note must be a string or null.")

        return {
            "contract_id": contract_id,
            "request_id": request_id,
            "question_class": question_class,
            "question_text": question_text,
            "context_note": context_note,
        }

    def validate_output_packet(self, packet: Any) -> Dict[str, Any]:
        if not isinstance(packet, dict):
            raise HarnessError("Output packet must be a JSON object.")

        extra_keys = sorted(set(packet.keys()) - OUTPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Output packet contains unsupported fields: {extra_keys}")

        missing_keys = sorted(OUTPUT_KEYS - set(packet.keys()))
        if missing_keys:
            raise HarnessError(f"Output packet is missing required fields: {missing_keys}")

        if packet.get("contract_id") != self.config.contract_id:
            raise HarnessError("Output packet contract_id does not match harness contract.")

        request_id = packet.get("request_id")
        if not isinstance(request_id, str) or not request_id or not REQUEST_ID_RE.match(request_id):
            raise HarnessError("Output packet request_id must be a bounded identifier string.")

        status = packet.get("status")
        if status not in self.config.allowed_statuses:
            raise HarnessError("Output packet status is not allowed.")

        answer = packet.get("answer")
        if not isinstance(answer, str):
            raise HarnessError("Output packet answer must be a string.")

        primary_rank_used = packet.get("primary_rank_used")
        if primary_rank_used not in self.config.allowed_primary_ranks:
            raise HarnessError("Output packet primary_rank_used is not allowed.")

        sources_used = packet.get("sources_used")
        if not isinstance(sources_used, list) or not all(isinstance(item, str) for item in sources_used):
            raise HarnessError("Output packet sources_used must be an array of strings.")
        if len(set(sources_used)) != len(sources_used):
            raise HarnessError("Output packet sources_used must not contain duplicates.")
        if any(path not in self.config.allowed_sources for path in sources_used):
            raise HarnessError("Output packet sources_used must remain inside the manifest.")

        if packet.get("derivative_status") != self.config.derivative_status:
            raise HarnessError("Output packet derivative_status must remain derivative_reader.")

        boundedness_note = packet.get("boundedness_note")
        if not isinstance(boundedness_note, str) or not boundedness_note.strip():
            raise HarnessError("Output packet boundedness_note must be a non-empty string.")

        next_read_paths = packet.get("next_read_paths")
        if not isinstance(next_read_paths, list) or not all(
            isinstance(item, str) for item in next_read_paths
        ):
            raise HarnessError("Output packet next_read_paths must be an array of strings.")
        if len(set(next_read_paths)) != len(next_read_paths):
            raise HarnessError("Output packet next_read_paths must not contain duplicates.")
        if any(path not in self.config.allowed_sources for path in next_read_paths):
            raise HarnessError("Output packet next_read_paths must remain inside the manifest.")

        refusal_reason = packet.get("refusal_reason")
        if refusal_reason is not None and refusal_reason not in self.config.allowed_refusal_reasons:
            raise HarnessError("Output packet refusal_reason is not allowed.")

        ambiguity_note = packet.get("ambiguity_note")
        if ambiguity_note is not None and not isinstance(ambiguity_note, str):
            raise HarnessError("Output packet ambiguity_note must be a string or null.")

        if status == "answered":
            if not answer.strip():
                raise HarnessError("Answered output must carry a non-empty answer.")
            if not sources_used:
                raise HarnessError("Answered output must carry non-empty provenance.")
            if refusal_reason is not None:
                raise HarnessError("Answered output must not carry a refusal reason.")
        elif status in {"refused", "out_of_scope"}:
            if refusal_reason is None:
                raise HarnessError("Refused or out_of_scope output must carry a refusal reason.")
        elif status == "insufficient_grounding":
            if not answer.strip():
                raise HarnessError("Insufficient_grounding output must carry a non-empty answer.")
            if not sources_used:
                raise HarnessError("Insufficient_grounding output must carry provenance.")
            if not isinstance(ambiguity_note, str) or not ambiguity_note.strip():
                raise HarnessError("Insufficient_grounding output must carry an ambiguity note.")
            if refusal_reason is not None:
                raise HarnessError(
                    "Insufficient_grounding output must not carry a refusal reason."
                )

        if status not in {"refused", "out_of_scope"} and answer == "":
            raise HarnessError("Only refused or out_of_scope output may use an empty answer.")

        return packet

    def _extract_markdown_section(self, text: str, heading_title: str) -> str:
        lines = text.splitlines()
        collecting = False
        heading_level: Optional[int] = None
        collected: List[str] = []

        for raw_line in lines:
            line = raw_line.rstrip("\n")
            match = HEADING_RE.match(line.strip())
            if match:
                level = len(match.group(1))
                title = match.group(2).strip()
                if collecting and heading_level is not None and level <= heading_level:
                    break
                if title == heading_title:
                    collecting = True
                    heading_level = level
                    continue
            if collecting:
                collected.append(line)

        return "\n".join(collected).strip()

    def _extract_bullets(self, section_text: str) -> List[str]:
        bullets: List[str] = []
        for raw_line in section_text.splitlines():
            line = raw_line.strip()
            if line.startswith("- "):
                bullets.append(line[2:].strip())
        return bullets

    def _strip_leading_marker(self, text: str) -> str:
        stripped = text.strip()
        if stripped.startswith("- "):
            return stripped[2:].strip()
        return stripped

    def _contains_path_reference(self, text: str) -> bool:
        return bool(FILE_REFERENCE_RE.search(text))

    def _detect_mutation_request(self, question_text: str) -> bool:
        lowered = question_text.lower()
        mutation_terms = ("update ", "rewrite ", "edit ", "mutate ", "modify ", "finalize ")
        return any(term in lowered for term in mutation_terms)

    def _detect_unapproved_source_reference(self, question_text: str) -> bool:
        matches = FILE_REFERENCE_RE.findall(question_text)
        for match in matches:
            candidate = match.rstrip(".,:;")
            if candidate and candidate not in self.config.allowed_sources:
                return True
        return False

    def _detect_insufficient_grounding_request(self, question_text: str) -> bool:
        lowered = question_text.lower()
        asks_for_single = "single approved surface" in lowered or "single surface" in lowered
        asks_for_conclusive = "conclusively" in lowered or "conclusive" in lowered
        asks_for_final_standing = "final v1 standing" in lowered or "final standing" in lowered
        return asks_for_single and asks_for_conclusive and asks_for_final_standing

    def _detect_broad_repo_interpretation(self, question_text: str) -> bool:
        lowered = question_text.lower()
        triggers = (
            "total repo-wide",
            "repo-wide interpretation",
            "all lab lines",
            "whether v1 is complete",
            "say whether v1 is complete",
        )
        return any(trigger in lowered for trigger in triggers)

    def _detect_interpretive_sovereignty_request(self, question_text: str) -> bool:
        lowered = question_text.lower()
        triggers = (
            "decide whether",
            "qualifies as",
            "state a new governing rule",
            "new governing rule",
            "new law",
            "should adopt now",
        )
        return any(trigger in lowered for trigger in triggers)

    def _detect_insufficient_rank_clarity_request(self, question_text: str) -> bool:
        lowered = question_text.lower()
        triggers = (
            "ignore rank",
            "without rank",
            "flatly",
            "one flat surface",
        )
        return any(trigger in lowered for trigger in triggers)

    def _question_primary_rank(self, question_class: str) -> str:
        return self.PRIMARY_RANK_MAP[question_class]

    def _refusal_primary_rank(self, question_class: str, question_text: str, status: str) -> str:
        lowered = question_text.lower()
        if status == "out_of_scope":
            return "navigation_surface"
        if "governing rule" in lowered or "new law" in lowered:
            return "standing_review_surface"
        if "lawful egress" in lowered or "obsolete container" in lowered:
            return "threshold_account_surface"
        return self._question_primary_rank(question_class)

    def _scope_sources(self, question_class: str) -> Tuple[str, ...]:
        return self.SOURCE_SCOPE_MAP[question_class]

    def _select_sources_for_request(self, question_class: str, question_text: str) -> Tuple[str, ...]:
        lowered = question_text.lower()
        scope = self._scope_sources(question_class)

        if question_class == "current_state":
            selected = [scope[0]]
            if any(token in lowered for token in ("stands now", "standing", "what stands")):
                selected.append(scope[1])
            return tuple(selected)

        if question_class == "current_governing_surfaces":
            return scope

        if question_class == "what_stands_now":
            return scope

        if question_class == "latest_thresholds":
            selected = list(scope[:3])
            if any(
                token in lowered
                for token in ("readability", "readable", "family", "proof 004", "cross-carrier line")
            ):
                selected.append(scope[3])
            return tuple(selected)

        if question_class == "what_remains_open":
            return scope

        if question_class == "where_to_read_next":
            return scope

        raise HarnessError(f"Unhandled question class for source selection: {question_class}")

    def _next_read_paths(self, question_class: str, consulted_sources: Sequence[str]) -> Tuple[str, ...]:
        if question_class == "current_state":
            return (
                "RANKED_SURFACE_INDEX.md",
                "CURRENT_READABILITY_SURFACES.md",
            )
        if question_class == "current_governing_surfaces":
            return (
                "RANKED_SURFACE_INDEX.md",
                "CONSTITUTIONAL_VERSION_NOTE.md",
                "CURRENT_STATE__REPO_ENTRY.md",
            )
        if question_class == "what_stands_now":
            return (
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
                "CURRENT_READABILITY_SURFACES.md",
            )
        if question_class == "latest_thresholds":
            if "CURRENT_READABILITY_SURFACES.md" in consulted_sources:
                return tuple(consulted_sources)
            return (
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
                "CURRENT_READABILITY_SURFACES.md",
            )
        if question_class == "what_remains_open":
            return (
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            )
        if question_class == "where_to_read_next":
            return (
                "CURRENT_STATE__REPO_ENTRY.md",
                "RANKED_SURFACE_INDEX.md",
                "CURRENT_READABILITY_SURFACES.md",
            )
        raise HarnessError(f"Unhandled question class for next-read paths: {question_class}")

    def _format_selected_surface_note(self, consulted_sources: Sequence[str]) -> str:
        class_counts: Dict[str, int] = {}
        ordered_classes: List[str] = []

        for source in consulted_sources:
            surface_class = self.SOURCE_CLASS_MAP.get(source)
            if surface_class is None:
                continue
            if surface_class not in ordered_classes:
                ordered_classes.append(surface_class)
            class_counts[surface_class] = class_counts.get(surface_class, 0) + 1

        if not ordered_classes:
            return "Derived only from the selected approved source set."

        items: List[str] = []
        for surface_class in ordered_classes:
            suffix = "surfaces" if class_counts[surface_class] > 1 else "surface"
            items.append(f"{surface_class} {suffix}")

        if len(items) == 1:
            joined = items[0]
        elif len(items) == 2:
            joined = f"{items[0]} and {items[1]}"
        else:
            joined = ", ".join(items[:-1]) + f", and {items[-1]}"

        return f"Derived only from the selected {joined}."

    def _read_selected_sources(self, selected_sources: Sequence[str]) -> Dict[str, str]:
        return {path: self._read_allowed_source(path) for path in selected_sources}

    def _build_refusal_plan(
        self,
        request: Mapping[str, Any],
        *,
        status: str,
        refusal_reason: str,
        boundedness_note: str,
    ) -> AnswerPlan:
        if status not in {"refused", "out_of_scope"}:
            raise HarnessError("Refusal plan must use refused or out_of_scope status.")

        return AnswerPlan(
            status=status,
            answer="",
            primary_rank_used=self._refusal_primary_rank(
                str(request["question_class"]),
                str(request["question_text"]),
                status,
            ),
            consulted_sources=(),
            next_read_paths=(),
            refusal_reason=refusal_reason,
            ambiguity_note=None,
            boundedness_note=boundedness_note,
        )

    def _build_insufficient_grounding_plan(
        self,
        request: Mapping[str, Any],
        *,
        consulted_sources: Sequence[str],
        boundedness_note: str,
        ambiguity_note: str,
        answer: Optional[str] = None,
        next_read_paths: Optional[Sequence[str]] = None,
    ) -> AnswerPlan:
        if not consulted_sources:
            raise HarnessError("Insufficient grounding plan must carry consulted sources.")

        return AnswerPlan(
            status="insufficient_grounding",
            answer=answer
            or (
                "The selected approved sources do not support a single tighter answer without outrunning bounded provenance."
            ),
            primary_rank_used=self._question_primary_rank(str(request["question_class"])),
            consulted_sources=tuple(consulted_sources),
            next_read_paths=tuple(
                next_read_paths
                or self._next_read_paths(str(request["question_class"]), consulted_sources)
            ),
            refusal_reason=None,
            ambiguity_note=ambiguity_note,
            boundedness_note=boundedness_note,
        )

    def _render_answer_plan(self, request: Mapping[str, Any]) -> AnswerPlan:
        question_class = str(request["question_class"])
        question_text = str(request["question_text"])
        selected_sources = self._select_sources_for_request(question_class, question_text)
        texts = self._read_selected_sources(selected_sources)
        next_read_paths = self._next_read_paths(question_class, selected_sources)
        boundedness_note = self._format_selected_surface_note(selected_sources)

        if question_class == "current_state":
            section = self._extract_markdown_section(
                texts["CURRENT_STATE__REPO_ENTRY.md"],
                "2. Current Repository Condition",
            )
            lines = [
                line.strip()
                for line in section.splitlines()
                if line.strip() and not line.strip().startswith("##")
            ]
            if not lines:
                return self._build_insufficient_grounding_plan(
                    request,
                    consulted_sources=selected_sources,
                    boundedness_note="The selected approved sources did not expose a readable current-condition section.",
                    ambiguity_note="Section extraction did not produce enough grounded current-condition material.",
                )

            answer_parts = [" ".join(lines[:3]).strip()]
            if len(selected_sources) > 1:
                standing_section = self._extract_markdown_section(
                    texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                    "7. Present Threshold Reading",
                )
                standing_bullets = self._extract_bullets(standing_section)
                if not standing_bullets:
                    return self._build_insufficient_grounding_plan(
                        request,
                        consulted_sources=selected_sources,
                        boundedness_note="The selected approved sources did not expose enough grounded present-threshold material for a bounded current-state supplement.",
                        ambiguity_note="The selected standing-review section did not yield grounded present-threshold bullets.",
                    )
                answer_parts.append(
                    "Current standing posture also reads as: "
                    + "; ".join(standing_bullets[:3])
                    + "."
                )

            return AnswerPlan(
                status="answered",
                answer=" ".join(answer_parts).strip(),
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        if question_class == "current_governing_surfaces":
            ranked_section = self._extract_markdown_section(
                texts["RANKED_SURFACE_INDEX.md"],
                "2. How To Read This Repository",
            )
            current_state_section = self._extract_markdown_section(
                texts["CURRENT_STATE__REPO_ENTRY.md"],
                "3. Ranked Reading",
            )
            constitutional_section = self._extract_markdown_section(
                texts["CONSTITUTIONAL_VERSION_NOTE.md"],
                "4. Current Operative Reading",
            )

            ranked_bullets = self._extract_bullets(ranked_section)
            current_state_bullets = self._extract_bullets(current_state_section)
            constitutional_present = bool(constitutional_section.strip())
            if not ranked_bullets or not current_state_bullets or not constitutional_present:
                return self._build_insufficient_grounding_plan(
                    request,
                    consulted_sources=selected_sources,
                    boundedness_note="The selected approved sources did not expose enough ranked governing material for a bounded response.",
                    ambiguity_note="One or more governing-source sections were missing or too thin for a grounded response.",
                )

            answer = " ".join(
                [
                    "Current repository reading stays ranked.",
                    " ".join(ranked_bullets[:2]),
                    " ".join(current_state_bullets[:2]),
                    "The operative constitutional reading remains separately ranked from source-side lineage and later readability aids.",
                ]
            ).strip()

            return AnswerPlan(
                status="answered",
                answer=answer,
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        if question_class == "what_stands_now":
            section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "4. What Now Clearly Stands",
            )
            bullets = self._extract_bullets(section)
            if not bullets:
                return self._build_insufficient_grounding_plan(
                    request,
                    consulted_sources=selected_sources,
                    boundedness_note="The selected approved source did not expose grounded standing bullets.",
                    ambiguity_note="The standing-review section could not be reduced into bounded standing bullets.",
                )
            return AnswerPlan(
                status="answered",
                answer="The current standing review says: " + "; ".join(bullets[:6]) + ".",
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        if question_class == "latest_thresholds":
            review_section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "5. Thresholds Crossed Since `19`",
            )
            review_bullets = self._extract_bullets(review_section)
            lawful_egress_section = self._extract_markdown_section(
                texts["v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md"],
                "4. Lawful Egress Threshold Executed",
            )
            readability_section = self._extract_markdown_section(
                texts["v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md"],
                "4. Lawful Egress Proof Readability Threshold",
            )
            if not review_bullets or not lawful_egress_section or not readability_section:
                return self._build_insufficient_grounding_plan(
                    request,
                    consulted_sources=selected_sources,
                    boundedness_note="The selected approved sources did not expose enough bounded threshold material for a grounded response.",
                    ambiguity_note="One or more selected threshold sections were missing or unreadable in bounded form.",
                )

            answer_parts = [
                "Since `19`, the selected threshold surfaces show lawful egress from obsolete or contaminated origin approval authority preserved in bounded executable cross-carrier form, lawful-egress proof readability as a ranked object, and the later standing review's record of those crossings."
            ]
            if "CURRENT_READABILITY_SURFACES.md" in selected_sources:
                readability_pointer_section = self._extract_markdown_section(
                    texts["CURRENT_READABILITY_SURFACES.md"],
                    "E. Current Cross-Carrier Readability Surfaces",
                )
                readability_pointer_bullets = self._extract_bullets(readability_pointer_section)
                if not readability_pointer_bullets:
                    return self._build_insufficient_grounding_plan(
                        request,
                        consulted_sources=selected_sources,
                        boundedness_note="The selected approved sources did not expose enough current cross-carrier readability material for a grounded supplement.",
                        ambiguity_note="The selected readability-pointer section did not yield bounded current cross-carrier pointer bullets.",
                    )
                answer_parts.append(
                    "The selected readability pointer also records the current cross-carrier family snapshot and report as next-readable family aids."
                )

            return AnswerPlan(
                status="answered",
                answer=" ".join(answer_parts).strip(),
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        if question_class == "what_remains_open":
            section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "6. What Remains Open",
            )
            bullets = [
                bullet
                for bullet in self._extract_bullets(section)
                if not self._contains_path_reference(bullet)
            ]
            if not bullets:
                return self._build_insufficient_grounding_plan(
                    request,
                    consulted_sources=selected_sources,
                    boundedness_note="The selected approved source did not expose grounded open-matters bullets.",
                    ambiguity_note="The standing-review section could not be reduced into bounded open-matters bullets.",
                )
            return AnswerPlan(
                status="answered",
                answer="The current standing review keeps the following open: " + "; ".join(
                    bullets[:6]
                ) + ".",
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        if question_class == "where_to_read_next":
            return AnswerPlan(
                status="answered",
                answer=(
                    "A bounded next reading path is: CURRENT_STATE__REPO_ENTRY.md for present condition, "
                    "RANKED_SURFACE_INDEX.md for rank order, and CURRENT_READABILITY_SURFACES.md for the latest readable surfaces."
                ),
                primary_rank_used=self._question_primary_rank(question_class),
                consulted_sources=tuple(selected_sources),
                next_read_paths=next_read_paths,
                refusal_reason=None,
                ambiguity_note=None,
                boundedness_note=boundedness_note,
            )

        raise HarnessError(f"Unhandled question class: {question_class}")

    def _surface_class_violations(
        self, text: str, consulted_sources: Sequence[str]
    ) -> List[str]:
        lowered = text.lower()
        violations: List[str] = []
        consulted_set = set(consulted_sources)

        for phrase, supporting_sources in self.SURFACE_CLASS_RULES:
            if phrase in lowered and not consulted_set.intersection(supporting_sources):
                violations.append(phrase)

        return violations

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

    def _packet_from_plan(self, request: Mapping[str, Any], plan: AnswerPlan) -> Dict[str, Any]:
        packet = {
            "contract_id": self.config.contract_id,
            "request_id": request["request_id"],
            "status": plan.status,
            "answer": plan.answer,
            "primary_rank_used": plan.primary_rank_used,
            "sources_used": list(plan.consulted_sources),
            "derivative_status": self.config.derivative_status,
            "boundedness_note": plan.boundedness_note,
            "next_read_paths": list(plan.next_read_paths),
            "refusal_reason": plan.refusal_reason,
            "ambiguity_note": plan.ambiguity_note,
        }
        return self.validate_output_packet(packet)

    def _answer_with_trace(self, packet: Any) -> Tuple[Dict[str, Any], PacketTrace]:
        request = self.validate_input_packet(packet)
        question_text = str(request["question_text"])

        if self._detect_mutation_request(question_text):
            plan = self._build_refusal_plan(
                request,
                status="refused",
                refusal_reason="would_mutate_or_finalize",
                boundedness_note="This vessel is read-only and cannot update, rewrite, edit, mutate, or finalize repo surfaces.",
            )
            return self._packet_from_plan(request, plan), PacketTrace((), (), True, None, None)

        if self._detect_unapproved_source_reference(question_text):
            plan = self._build_refusal_plan(
                request,
                status="out_of_scope",
                refusal_reason="requires_unapproved_sources",
                boundedness_note="The request explicitly depends on sources outside the local source manifest.",
            )
            return self._packet_from_plan(request, plan), PacketTrace((), (), True, None, None)

        if self._detect_insufficient_grounding_request(question_text):
            consulted_sources = (
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
                "CURRENT_STATE__REPO_ENTRY.md",
                "RANKED_SURFACE_INDEX.md",
            )
            self._read_selected_sources(consulted_sources)
            plan = self._build_insufficient_grounding_plan(
                request,
                consulted_sources=consulted_sources,
                boundedness_note="The selected approved sources do not support one conclusive final-standing source.",
                ambiguity_note="The selected approved sources preserve bounded standing and open matters rather than one final conclusive settlement surface.",
                answer=(
                    "The selected approved sources do not identify a single conclusive surface that finally settles v1 standing now. "
                    "They keep the line materially standing while still preserving open matters and non-final closure."
                ),
                next_read_paths=consulted_sources,
            )
            packet_out = self._packet_from_plan(request, plan)
            trace = self._provenance_self_check(plan)
            return packet_out, trace

        if self._detect_broad_repo_interpretation(question_text):
            plan = self._build_refusal_plan(
                request,
                status="out_of_scope",
                refusal_reason="would_require_interpretive_sovereignty",
                boundedness_note="The request exceeds this vessel's bounded current-state / standing role and would require broader interpretive sovereignty.",
            )
            return self._packet_from_plan(request, plan), PacketTrace((), (), True, None, None)

        if self._detect_interpretive_sovereignty_request(question_text):
            plan = self._build_refusal_plan(
                request,
                status="refused",
                refusal_reason="would_require_interpretive_sovereignty",
                boundedness_note="This vessel may not decide new law, classify new seam cases, or state new governing rules.",
            )
            return self._packet_from_plan(request, plan), PacketTrace((), (), True, None, None)

        if self._detect_insufficient_rank_clarity_request(question_text):
            plan = self._build_refusal_plan(
                request,
                status="refused",
                refusal_reason="insufficient_rank_clarity",
                boundedness_note="The request asks to suppress rank clarity that this vessel is required to preserve.",
            )
            return self._packet_from_plan(request, plan), PacketTrace((), (), True, None, None)

        plan = self._render_answer_plan(request)
        trace = self._provenance_self_check(plan)
        if not trace.provenance_ok:
            downgraded_plan = self._build_insufficient_grounding_plan(
                request,
                consulted_sources=plan.consulted_sources,
                boundedness_note="The selected approved sources were insufficient to support the drafted response without provenance drift.",
                ambiguity_note=trace.public_note
                or "The drafted response exceeded bounded provenance.",
                next_read_paths=plan.next_read_paths,
            )
            downgraded_trace = self._provenance_self_check(downgraded_plan)
            return self._packet_from_plan(request, downgraded_plan), downgraded_trace

        return self._packet_from_plan(request, plan), trace

    def answer_request(self, packet: Any) -> Dict[str, Any]:
        response, _trace = self._answer_with_trace(packet)
        return response

    def _load_eval_corpus(self) -> Dict[str, Any]:
        corpus = self._load_json_object(EVAL_CORPUS_PATH)
        if corpus.get("contract_id") != self.config.contract_id:
            raise HarnessError("Eval corpus contract_id does not match harness contract.")
        cases = corpus.get("cases")
        if not isinstance(cases, list):
            raise HarnessError("Eval corpus cases must be an array.")
        return corpus

    def _built_in_regression_case(self) -> Dict[str, Any]:
        return {
            "eval_id": "latest_thresholds_provenance_scope_regression",
            "purpose": "Locks the old latest-thresholds provenance leak where note text outran the selected source set.",
            "input_packet": {
                "contract_id": self.config.contract_id,
                "request_id": "req_regression_001",
                "question_class": "latest_thresholds",
                "question_text": "What are the latest thresholds crossed?",
                "context_note": "Regression test for provenance scope",
            },
            "expected_status": "answered",
            "expected_primary_rank_used": "threshold_account_surface",
            "expected_refusal_reason": None,
            "expected_min_sources": 3,
            "expected_allowed_source_subset": [
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "expected_ambiguity_note_required": False,
            "notes": "The old leak named readability-pointer surfaces even when CURRENT_READABILITY_SURFACES.md was not in sources_used.",
        }

    def _eval_cases(self) -> List[Dict[str, Any]]:
        corpus = self._load_eval_corpus()
        cases = list(corpus["cases"])
        cases.append(self._built_in_regression_case())
        return cases

    def _evaluate_case(self, case: Mapping[str, Any]) -> List[str]:
        reasons: List[str] = []
        eval_id = str(case.get("eval_id", "unknown_eval"))
        input_packet = case.get("input_packet")

        try:
            output, trace = self._answer_with_trace(input_packet)
        except Exception as exc:  # pragma: no cover
            return [f"{eval_id}: harness raised {type(exc).__name__}: {exc}"]

        expected_status = case.get("expected_status")
        if output.get("status") != expected_status:
            reasons.append(
                f"status expected {expected_status!r} but got {output.get('status')!r}"
            )

        expected_primary_rank = case.get("expected_primary_rank_used")
        if output.get("primary_rank_used") != expected_primary_rank:
            reasons.append(
                "primary_rank_used expected "
                f"{expected_primary_rank!r} but got {output.get('primary_rank_used')!r}"
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
        if not isinstance(allowed_subset, list) or not all(
            isinstance(item, str) for item in allowed_subset
        ):
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

        if output.get("status") in {"answered", "insufficient_grounding"} and not trace.provenance_ok:
            reasons.append(
                "response packet failed provenance self-check: "
                + str(trace.debug_note)
            )

        if list(trace.consulted_sources) != actual_sources:
            reasons.append(
                "sources_used did not match the actual selected source set: "
                f"expected {list(trace.consulted_sources)!r} but got {actual_sources!r}"
            )

        if eval_id == "latest_thresholds_provenance_scope_regression":
            combined_text = " ".join(
                [
                    str(output.get("answer", "")),
                    str(output.get("boundedness_note", "")),
                    str(output.get("ambiguity_note") or ""),
                ]
            ).lower()
            if "CURRENT_READABILITY_SURFACES.md" in actual_sources:
                reasons.append(
                    "regression case widened latest_thresholds sources_used to include CURRENT_READABILITY_SURFACES.md"
                )
            if "readability-pointer" in combined_text:
                reasons.append(
                    "regression case reintroduced readability-pointer wording without selecting CURRENT_READABILITY_SURFACES.md"
                )
            forbidden_fragments = (
                "cross_carrier_family_snapshot__",
                "cross_carrier_proof_family_report__",
                "lab/snapshots/",
                "current_readability_surfaces.md",
            )
            leaked_fragments = [fragment for fragment in forbidden_fragments if fragment in combined_text]
            if leaked_fragments:
                reasons.append(
                    "regression case mentioned undeclared readability artifacts or pointer surfaces: "
                    + ", ".join(leaked_fragments)
                )

        return reasons

    def run_eval(self) -> int:
        cases = self._eval_cases()
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
        "  python vessel/current_state_standing_reader_v1/local_harness_v3.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_standing_reader_v1/local_harness_v3.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    harness = CurrentStateStandingReaderHarnessV3()
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
        print(f"local_harness_v3 error: {exc}", file=sys.stderr)
        raise SystemExit(2)
