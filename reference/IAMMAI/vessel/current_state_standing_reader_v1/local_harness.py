#!/usr/bin/env python3
"""
Local non-bypassable harness for current_state_standing_reader_v1.

This harness enforces the first vessel's local shell before any later model or
API insertion. It is read-only, manifest-bounded, schema-checked, and
deliberately narrow.
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
    """Raised for harness integrity failures and malformed packets."""


@dataclass(frozen=True)
class HarnessConfig:
    contract_id: str
    allowed_sources: Tuple[str, ...]
    allowed_question_classes: Tuple[str, ...]
    allowed_statuses: Tuple[str, ...]
    allowed_primary_ranks: Tuple[str, ...]
    allowed_refusal_reasons: Tuple[str, ...]
    derivative_status: str


class CurrentStateStandingReaderHarness:
    """Local shell for the first bounded current-state / standing reader."""

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

        input_contract = (
            self._expect_mapping(input_schema, "properties")
            .get("contract_id")
        )
        if not isinstance(input_contract, Mapping):
            raise HarnessError("Input schema is missing contract_id property.")
        if input_contract.get("const") != contract_id:
            raise HarnessError("Input schema contract_id does not match manifest contract_id.")

        input_question_class = self._expect_mapping(input_schema, "properties").get(
            "question_class"
        )
        if not isinstance(input_question_class, Mapping):
            raise HarnessError("Input schema is missing question_class property.")
        input_enum = input_question_class.get("enum")
        if list(allowed_question_classes) != list(input_enum or []):
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
        value = mapping.get(key)
        return self._expect_string_sequence(value)

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

        packet_keys = set(packet.keys())
        extra_keys = sorted(packet_keys - INPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Input packet contains unsupported fields: {extra_keys}")

        required_keys = {"contract_id", "request_id", "question_class", "question_text"}
        missing_keys = sorted(required_keys - packet_keys)
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

        packet_keys = set(packet.keys())
        extra_keys = sorted(packet_keys - OUTPUT_KEYS)
        if extra_keys:
            raise HarnessError(f"Output packet contains unsupported fields: {extra_keys}")

        missing_keys = sorted(OUTPUT_KEYS - packet_keys)
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

    def _base_primary_rank(self, question_class: str) -> str:
        mapping = {
            "current_state": "current_state_surface",
            "current_governing_surfaces": "navigation_surface",
            "what_stands_now": "standing_review_surface",
            "latest_thresholds": "threshold_account_surface",
            "what_remains_open": "standing_review_surface",
            "where_to_read_next": "readability_pointer_surface",
        }
        return mapping[question_class]

    def _refusal_primary_rank(self, question_class: str, question_text: str, status: str) -> str:
        lowered = question_text.lower()
        if status == "out_of_scope":
            return "navigation_surface"
        if "governing rule" in lowered or "new law" in lowered:
            return "standing_review_surface"
        if "lawful egress" in lowered or "obsolete container" in lowered:
            return "threshold_account_surface"
        return self._base_primary_rank(question_class)

    def _source_map(self, question_class: str) -> List[str]:
        mapping = {
            "current_state": [
                "CURRENT_STATE__REPO_ENTRY.md",
            ],
            "current_governing_surfaces": [
                "RANKED_SURFACE_INDEX.md",
                "CONSTITUTIONAL_VERSION_NOTE.md",
                "CURRENT_STATE__REPO_ENTRY.md",
            ],
            "what_stands_now": [
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "latest_thresholds": [
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "what_remains_open": [
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "where_to_read_next": [
                "CURRENT_READABILITY_SURFACES.md",
                "RANKED_SURFACE_INDEX.md",
                "CURRENT_STATE__REPO_ENTRY.md",
            ],
        }
        selected = mapping[question_class]
        if any(path not in self.config.allowed_sources for path in selected):
            raise HarnessError("Source map contains non-manifest source.")
        return selected

    def _next_read_paths(self, question_class: str) -> List[str]:
        mapping = {
            "current_state": [
                "RANKED_SURFACE_INDEX.md",
                "CURRENT_READABILITY_SURFACES.md",
            ],
            "current_governing_surfaces": [
                "RANKED_SURFACE_INDEX.md",
                "CONSTITUTIONAL_VERSION_NOTE.md",
                "CURRENT_STATE__REPO_ENTRY.md",
            ],
            "what_stands_now": [
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
                "CURRENT_READABILITY_SURFACES.md",
            ],
            "latest_thresholds": [
                "v1/20_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_FROM_OBSOLETE_CONTAINER_PROOF.md",
                "v1/21_TRANSFER_ACCOUNT_ENTRY__LAWFUL_EGRESS_PROOF_READABILITY_THRESHOLD.md",
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "what_remains_open": [
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            ],
            "where_to_read_next": [
                "CURRENT_STATE__REPO_ENTRY.md",
                "RANKED_SURFACE_INDEX.md",
                "CURRENT_READABILITY_SURFACES.md",
            ],
        }
        paths = mapping[question_class]
        if any(path not in self.config.allowed_sources for path in paths):
            raise HarnessError("Next-read map contains non-manifest source.")
        return paths

    def _build_answered_packet(self, request: Mapping[str, Any]) -> Dict[str, Any]:
        question_class = str(request["question_class"])
        sources = self._source_map(question_class)
        texts = {path: self._read_allowed_source(path) for path in sources}

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
            answer = " ".join(lines[:3]).strip()
            boundedness_note = "Derived only from the approved current-state entry surface."
        elif question_class == "current_governing_surfaces":
            ranked_section = self._extract_markdown_section(
                texts["RANKED_SURFACE_INDEX.md"],
                "2. How To Read This Repository",
            )
            constitutional_section = self._extract_markdown_section(
                texts["CONSTITUTIONAL_VERSION_NOTE.md"],
                "4. Current Operative Reading",
            )
            current_state_section = self._extract_markdown_section(
                texts["CURRENT_STATE__REPO_ENTRY.md"],
                "3. Ranked Reading",
            )
            ranked_lines = [
                line.strip()
                for line in ranked_section.splitlines()
                if line.strip().startswith("- ")
            ]
            constitutional_lines = [
                line.strip()
                for line in constitutional_section.splitlines()
                if line.strip().startswith("- ")
            ]
            current_state_lines = [
                line.strip()
                for line in current_state_section.splitlines()
                if line.strip().startswith("- ")
            ]
            answer = " ".join(
                [
                    "Current repository reading stays ranked.",
                    " ".join(ranked_lines[:2]).replace("- ", ""),
                    " ".join(current_state_lines[:2]).replace("- ", ""),
                    " ".join(constitutional_lines[:1]).replace("- ", ""),
                ]
            ).strip()
            boundedness_note = (
                "Derived only from approved navigation, constitutional clarification, and current-state surfaces."
            )
        elif question_class == "what_stands_now":
            section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "4. What Now Clearly Stands",
            )
            bullets = self._extract_bullets(section)
            answer = "The current standing review says: " + "; ".join(bullets[:6]) + "."
            boundedness_note = "Derived only from the current standing review surface."
        elif question_class == "latest_thresholds":
            section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "5. Thresholds Crossed Since `19`",
            )
            bullets = self._extract_bullets(section)
            answer = "Since `19`, the approved surfaces record: " + "; ".join(bullets[:3]) + "."
            boundedness_note = "Derived only from approved threshold-account and standing-review surfaces."
        elif question_class == "what_remains_open":
            section = self._extract_markdown_section(
                texts["v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md"],
                "6. What Remains Open",
            )
            bullets = self._extract_bullets(section)
            answer = "The current standing review keeps the following open: " + "; ".join(
                bullets[:6]
            ) + "."
            boundedness_note = "Derived only from the current standing review's open-matters section."
        elif question_class == "where_to_read_next":
            answer = (
                "A bounded next reading path is: CURRENT_STATE__REPO_ENTRY.md for present condition, "
                "RANKED_SURFACE_INDEX.md for rank order, and CURRENT_READABILITY_SURFACES.md for the latest readable surfaces."
            )
            boundedness_note = "Derived only from approved navigation and readability-pointer surfaces."
        else:
            raise HarnessError(f"Unhandled question class: {question_class}")

        packet = {
            "contract_id": self.config.contract_id,
            "request_id": request["request_id"],
            "status": "answered",
            "answer": answer,
            "primary_rank_used": self._base_primary_rank(question_class),
            "sources_used": sources,
            "derivative_status": self.config.derivative_status,
            "boundedness_note": boundedness_note,
            "next_read_paths": self._next_read_paths(question_class),
            "refusal_reason": None,
            "ambiguity_note": None,
        }
        return self.validate_output_packet(packet)

    def _build_insufficient_grounding_packet(self, request: Mapping[str, Any]) -> Dict[str, Any]:
        sources = [
            "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
            "CURRENT_STATE__REPO_ENTRY.md",
            "RANKED_SURFACE_INDEX.md",
        ]
        for source in sources:
            self._read_allowed_source(source)

        packet = {
            "contract_id": self.config.contract_id,
            "request_id": request["request_id"],
            "status": "insufficient_grounding",
            "answer": (
                "The approved corpus does not identify a single conclusive surface that finally settles v1 standing now. "
                "The current-state and standing-review surfaces keep the line materially standing while still preserving open matters and non-final closure."
            ),
            "primary_rank_used": "standing_review_surface",
            "sources_used": sources,
            "derivative_status": self.config.derivative_status,
            "boundedness_note": "Question is nominally in scope, but the approved corpus does not support one conclusive final-standing source.",
            "next_read_paths": [
                "v1/22_STANDING_REVIEW__POST_LAWFUL_EGRESS_AND_CROSS_CARRIER_LINE.md",
                "CURRENT_STATE__REPO_ENTRY.md",
                "RANKED_SURFACE_INDEX.md",
            ],
            "refusal_reason": None,
            "ambiguity_note": "Approved surfaces preserve bounded standing and open matters rather than one final conclusive settlement surface.",
        }
        return self.validate_output_packet(packet)

    def _build_refusal_packet(
        self,
        request: Mapping[str, Any],
        *,
        status: str,
        refusal_reason: str,
        boundedness_note: str,
    ) -> Dict[str, Any]:
        if status not in {"refused", "out_of_scope"}:
            raise HarnessError("Refusal packet must use refused or out_of_scope status.")

        primary_rank_used = self._refusal_primary_rank(
            str(request["question_class"]),
            str(request["question_text"]),
            status,
        )

        packet = {
            "contract_id": self.config.contract_id,
            "request_id": request["request_id"],
            "status": status,
            "answer": "",
            "primary_rank_used": primary_rank_used,
            "sources_used": [],
            "derivative_status": self.config.derivative_status,
            "boundedness_note": boundedness_note,
            "next_read_paths": [],
            "refusal_reason": refusal_reason,
            "ambiguity_note": None,
        }
        return self.validate_output_packet(packet)

    def answer_request(self, packet: Any) -> Dict[str, Any]:
        request = self.validate_input_packet(packet)
        question_text = str(request["question_text"])

        if self._detect_mutation_request(question_text):
            return self._build_refusal_packet(
                request,
                status="refused",
                refusal_reason="would_mutate_or_finalize",
                boundedness_note="This vessel is read-only and cannot update, rewrite, edit, mutate, or finalize repo surfaces.",
            )

        if self._detect_unapproved_source_reference(question_text):
            return self._build_refusal_packet(
                request,
                status="out_of_scope",
                refusal_reason="requires_unapproved_sources",
                boundedness_note="The request explicitly depends on sources outside the local source manifest.",
            )

        if self._detect_insufficient_grounding_request(question_text):
            return self._build_insufficient_grounding_packet(request)

        if self._detect_broad_repo_interpretation(question_text):
            return self._build_refusal_packet(
                request,
                status="out_of_scope",
                refusal_reason="would_require_interpretive_sovereignty",
                boundedness_note="The request exceeds this vessel's bounded current-state / standing role and would require broader interpretive sovereignty.",
            )

        if self._detect_interpretive_sovereignty_request(question_text):
            return self._build_refusal_packet(
                request,
                status="refused",
                refusal_reason="would_require_interpretive_sovereignty",
                boundedness_note="This vessel may not decide new law, classify new seam cases, or state new governing rules.",
            )

        return self._build_answered_packet(request)

    def _load_eval_corpus(self) -> Dict[str, Any]:
        corpus = self._load_json_object(EVAL_CORPUS_PATH)
        if corpus.get("contract_id") != self.config.contract_id:
            raise HarnessError("Eval corpus contract_id does not match harness contract.")
        cases = corpus.get("cases")
        if not isinstance(cases, list):
            raise HarnessError("Eval corpus cases must be an array.")
        return corpus

    def _evaluate_case(self, case: Mapping[str, Any]) -> List[str]:
        reasons: List[str] = []
        eval_id = case.get("eval_id", "unknown_eval")

        input_packet = case.get("input_packet")
        try:
            output = self.answer_request(input_packet)
        except Exception as exc:  # pragma: no cover - bounded failure report path
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

        expected_min_sources = case.get("expected_min_sources")
        if not isinstance(expected_min_sources, int):
            reasons.append("expected_min_sources is not an integer in eval case.")
        else:
            actual_sources = output.get("sources_used", [])
            if len(actual_sources) < expected_min_sources:
                reasons.append(
                    f"sources_used expected at least {expected_min_sources} but got {len(actual_sources)}"
                )

        allowed_subset = case.get("expected_allowed_source_subset")
        if not isinstance(allowed_subset, list) or not all(
            isinstance(item, str) for item in allowed_subset
        ):
            reasons.append("expected_allowed_source_subset is not a string array in eval case.")
        else:
            unexpected_sources = [
                source
                for source in output.get("sources_used", [])
                if source not in set(allowed_subset)
            ]
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
        "  python vessel/current_state_standing_reader_v1/local_harness.py answer <path-to-input-packet.json>\n"
        "  python vessel/current_state_standing_reader_v1/local_harness.py eval\n"
    )
    print(usage, file=sys.stderr)


def main(argv: Sequence[str]) -> int:
    if len(argv) < 2:
        print_usage()
        return 2

    harness = CurrentStateStandingReaderHarness()
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
