"""Validated evidence and deterministic, contextual projections of an event log."""

from __future__ import annotations

import hashlib
import json
import math
import re
from datetime import datetime, timezone
from typing import Any

MAX_EVENT_BYTES = 131_072
MAX_EVENTS = 10_000
MAX_CONSULTATION_SECONDS = 86_400
LEGACY_ACTIONS = ("admit", "select", "relate", "supersede", "retract")
EVOLUTION_ACTIONS = ("regulate", "open-consultation", "close-consultation", "withdraw-relation")
READ_OPERATIONS = ("state", "lookup", "compare", "history", "verify", "capabilities", "consultation")
ZERO_HASH = "0" * 64
IDENTIFIER = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{0,127}\Z")
TIMESTAMP = re.compile(
    r"[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}"
    r"(?:\.[0-9]{1,6})?(?:Z|[+-](?:[01][0-9]|2[0-3]):[0-5][0-9])\Z"
)


class LRMError(ValueError):
    """Invalid input, unavailable evidence, conflicting revision, or corrupt log."""


def canonical(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True,
                      allow_nan=False)


def _pairs(pairs: list[tuple[str, Any]]) -> dict:
    result = {}
    for key, value in pairs:
        if key in result:
            raise LRMError(f"duplicate JSON field: {key}")
        result[key] = value
    return result


def _invalid_constant(value: str) -> None:
    raise LRMError(f"non-finite JSON number: {value}")


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise LRMError("JSON number is out of range")
    return parsed


def parse_json(text: str) -> Any:
    try:
        if len(text.encode("utf-8")) > MAX_EVENT_BYTES:
            raise LRMError("JSON input exceeds the event size limit")
        return json.loads(text, object_pairs_hook=_pairs, parse_constant=_invalid_constant,
                          parse_float=_finite_float)
    except LRMError:
        raise
    except (ValueError, RecursionError) as exc:
        raise LRMError("invalid JSON input") from exc


def fields(value: Any, required: set[str], optional: set[str] | None = None) -> dict:
    if not isinstance(value, dict):
        raise LRMError("expected a JSON object")
    keys = set(value)
    if required - keys or keys - required - (optional or set()):
        raise LRMError(f"expected fields {sorted(required)}; optional {sorted(optional or set())}")
    return value


def text(value: Any, name: str, limit: int = 4096) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > limit:
        raise LRMError(f"{name} must be nonempty text of at most {limit} characters")
    try:
        value.encode("utf-8")
    except UnicodeError as exc:
        raise LRMError(f"{name} contains invalid Unicode") from exc
    return value


def identifier(value: Any, name: str = "identifier") -> str:
    if not isinstance(value, str) or not IDENTIFIER.fullmatch(value):
        raise LRMError(f"{name} must be 1–128 ASCII letters/digits or . _ : -")
    return value


def timestamp(value: Any) -> str:
    if not isinstance(value, str) or not TIMESTAMP.fullmatch(value):
        raise LRMError("timestamps require an RFC3339 date/time with an explicit UTC offset")
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.astimezone(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")
    except (ValueError, OverflowError) as exc:
        raise LRMError("invalid timestamp") from exc


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def digest(event: dict) -> str:
    return hashlib.sha256(canonical(event).encode("utf-8")).hexdigest()


def normalize_record(value: Any) -> dict:
    record = fields(value, {"id", "scope", "subject", "body", "provenance", "observed_at"},
                    {"valid_from", "valid_until"})
    provenance = fields(record["provenance"], {"origin", "basis"})
    result = {
        "id": identifier(record["id"]),
        "scope": identifier(record["scope"], "scope"),
        "subject": text(record["subject"], "subject", 256),
        "body": text(record["body"], "body", 32_768),
        "provenance": {
            "origin": text(provenance["origin"], "origin", 2048),
            "basis": text(provenance["basis"], "relevance basis"),
        },
        "observed_at": timestamp(record["observed_at"]),
        "valid_from": timestamp(record["valid_from"]) if record.get("valid_from") is not None else None,
        "valid_until": timestamp(record["valid_until"]) if record.get("valid_until") is not None else None,
    }
    if result["valid_from"] and result["valid_until"] and result["valid_from"] >= result["valid_until"]:
        raise LRMError("valid_until must be later than valid_from")
    return result


def normalize_operation(action: str, value: Any) -> dict:
    if action == "admit":
        fields(value, {"record"})
        return {"record": normalize_record(value["record"])}
    if action == "select":
        fields(value, {"scope", "ids"})
        ids = value["ids"]
        if not isinstance(ids, list) or len(ids) > MAX_EVENTS:
            raise LRMError("selection ids must be a bounded list")
        ids = [identifier(item) for item in ids]
        if len(ids) != len(set(ids)):
            raise LRMError("selection ids must be unique")
        return {"scope": identifier(value["scope"], "scope"), "ids": sorted(ids)}
    if action == "relate":
        fields(value, {"left", "right", "kind"})
        if value["kind"] not in ("supports", "contradicts", "related"):
            raise LRMError("relation kind must be supports, contradicts, or related")
        return {"left": identifier(value["left"]), "right": identifier(value["right"]),
                "kind": value["kind"]}
    if action == "supersede":
        fields(value, {"old", "new"})
        return {"old": identifier(value["old"]), "new": identifier(value["new"])}
    if action == "retract":
        fields(value, {"id"})
        return {"id": identifier(value["id"])}
    if action == "regulate":
        fields(value, {"scope", "status"})
        if value["status"] not in ("open", "held"):
            raise LRMError("regulation status must be open or held")
        return {"scope": identifier(value["scope"], "scope"), "status": value["status"]}
    if action == "open-consultation":
        fields(value, {"id", "scope", "until"})
        return {"id": identifier(value["id"]), "scope": identifier(value["scope"], "scope"),
                "until": timestamp(value["until"])}
    if action == "close-consultation":
        fields(value, {"id"})
        return {"id": identifier(value["id"])}
    if action == "withdraw-relation":
        fields(value, {"revision"})
        if type(value["revision"]) is not int or value["revision"] < 1:
            raise LRMError("relation revision must be a positive integer")
        return {"revision": value["revision"]}
    raise LRMError("unsupported operation")


class Projection:
    """Replay state; callers receive JSON copies, never the mutable internal maps."""

    def __init__(self) -> None:
        self.records: dict[str, dict] = {}
        self.admissions: dict[str, int] = {}
        self.retractions: dict[str, dict] = {}
        self.supersessions: dict[str, dict] = {}
        self.selections: dict[str, dict] = {}
        self.relations: list[dict] = []
        self.relation_withdrawals: dict[int, dict] = {}
        self.regulations: dict[str, dict] = {}
        self.consultations: dict[str, dict] = {}
        self.revision = 0
        self.head_hash = ZERO_HASH
        self.recorded_at: str | None = None

    def require(self, record_id: str) -> dict:
        identifier(record_id)
        if record_id not in self.records:
            raise LRMError(f"unknown record: {record_id}")
        return self.records[record_id]

    def ineligibility(self, record_id: str, at: str) -> list[str]:
        record = self.require(record_id)
        reasons = []
        if record_id in self.retractions:
            reasons.append("retracted")
        if record_id in self.supersessions:
            reasons.append("superseded")
        if record["valid_from"] and at < record["valid_from"]:
            reasons.append("not_yet_valid")
        if record["valid_until"] and at >= record["valid_until"]:
            reasons.append("expired")
        return reasons

    def regulation(self, scope: str) -> dict:
        return self.regulations.get(scope, {
            "scope": scope, "status": "open", "revision": 0,
            "recorded_at": None, "reason": None,
        })

    def consultation_blockers(self, scope: str, at: str) -> list[str]:
        reasons = []
        if self.regulation(scope)["status"] == "held":
            reasons.append("scope_held")
        ids = self.selections.get(scope, {}).get("ids", [])
        if not ids:
            reasons.append("no_selection")
        if any(self.ineligibility(item, at) for item in ids):
            reasons.append("selection_lapsed")
        if self.revision >= MAX_EVENTS:
            reasons.append("event_limit_reached")
        return reasons

    def invalidate_consultations(self, scope: str, cause: str, evidence: dict,
                                 record_id: str | None = None) -> None:
        for consultation in self.consultations.values():
            if (consultation["scope"] == scope and not consultation["closed"]
                    and not consultation["invalidated"]
                    and evidence["recorded_at"] < consultation["until"]
                    and (record_id is None or record_id in consultation["ids"])):
                consultation["invalidated"] = {"cause": cause, **evidence}

    def apply(self, event: dict) -> None:
        action, data, at = event["action"], event["data"], event["recorded_at"]
        evidence = {"revision": event["sequence"], "recorded_at": at, "reason": event["reason"]}
        if action == "admit":
            record = data["record"]
            if record["id"] in self.records:
                raise LRMError("record id already exists; admit revisions under a new id")
            if record["observed_at"] > at:
                raise LRMError("observed_at cannot be later than admission")
            self.records[record["id"]] = record
            self.admissions[record["id"]] = event["sequence"]
        elif action == "select":
            if data["ids"] and self.regulation(data["scope"])["status"] == "held":
                raise LRMError("scope is held; selection may be cleared but not populated")
            for record_id in data["ids"]:
                record = self.require(record_id)
                if record["scope"] != data["scope"]:
                    raise LRMError("selection cannot cross scopes")
                if self.ineligibility(record_id, at):
                    raise LRMError(f"record is not eligible for selection: {record_id}")
            self.invalidate_consultations(data["scope"], "selection_changed", evidence)
            self.selections[data["scope"]] = {**data, **evidence}
        elif action == "relate":
            left, right = self.require(data["left"]), self.require(data["right"])
            if left["id"] == right["id"] or left["scope"] != right["scope"]:
                raise LRMError("relations require distinct records in the same scope")
            for relation in self.relations:
                if relation["revision"] in self.relation_withdrawals:
                    continue
                same_direction = (relation["left"], relation["right"]) == (data["left"], data["right"])
                reverse = (relation["left"], relation["right"]) == (data["right"], data["left"])
                if relation["kind"] == data["kind"] and (same_direction or (reverse and data["kind"] != "supports")):
                    raise LRMError("relation already exists")
            self.relations.append({**data, **evidence})
        elif action == "supersede":
            old, new = self.require(data["old"]), self.require(data["new"])
            if old["id"] == new["id"] or (old["scope"], old["subject"]) != (new["scope"], new["subject"]):
                raise LRMError("supersession requires distinct records of the same scope and subject")
            if data["old"] in self.supersessions or data["old"] in self.retractions:
                raise LRMError("old record is already superseded or retracted")
            if self.ineligibility(data["new"], at):
                raise LRMError("replacement must be eligible")
            self.supersessions[data["old"]] = {"new": data["new"], **evidence}
            self.invalidate_consultations(old["scope"], "evidence_superseded", evidence, data["old"])
        elif action == "retract":
            self.require(data["id"])
            if data["id"] in self.retractions:
                raise LRMError("record is already retracted")
            self.retractions[data["id"]] = evidence
            self.invalidate_consultations(self.records[data["id"]]["scope"],
                                          "evidence_retracted", evidence, data["id"])
        elif action == "withdraw-relation":
            if not any(item["revision"] == data["revision"] for item in self.relations):
                raise LRMError("unknown relation revision")
            if data["revision"] in self.relation_withdrawals:
                raise LRMError("relation is already withdrawn")
            self.relation_withdrawals[data["revision"]] = evidence
        elif action == "regulate":
            if self.regulation(data["scope"])["status"] == data["status"]:
                raise LRMError("scope already has that regulation status")
            self.regulations[data["scope"]] = {**data, **evidence}
            if data["status"] == "held":
                self.invalidate_consultations(data["scope"], "scope_held", evidence)
        elif action == "open-consultation":
            if data["id"] in self.consultations:
                raise LRMError("consultation id already exists; use a new id")
            duration = (datetime.fromisoformat(data["until"]) - datetime.fromisoformat(at)).total_seconds()
            if not 0 < duration <= MAX_CONSULTATION_SECONDS:
                raise LRMError("consultation must expire within 24 hours after opening")
            blockers = self.consultation_blockers(data["scope"], at)
            if blockers:
                raise LRMError("consultation cannot open: " + ", ".join(blockers))
            selection = self.selections[data["scope"]]
            self.consultations[data["id"]] = {
                **data, "ids": list(selection["ids"]), "selection_revision": selection["revision"],
                "basis_revision": self.revision, "basis_hash": self.head_hash,
                "opened": evidence, "closed": None, "invalidated": None,
            }
        elif action == "close-consultation":
            consultation = self.require_consultation(data["id"])
            if consultation["closed"]:
                raise LRMError("consultation is already closed")
            consultation["closed"] = evidence
        self.revision = event["sequence"]
        self.head_hash = digest(event)
        self.recorded_at = at

    def lookup(self, record_id: str, at: str) -> dict:
        record = self.require(record_id)
        selection = self.selections.get(record["scope"], {})
        return {
            "record": record,
            "admission_revision": self.admissions[record_id],
            "content_hash": digest(record),
            "selected": record_id in selection.get("ids", []),
            "ineligibility": self.ineligibility(record_id, at),
            "retraction": self.retractions.get(record_id),
            "supersession": self.supersessions.get(record_id),
        }

    def relation_view(self, relation: dict) -> dict:
        return {**relation, "withdrawal": self.relation_withdrawals.get(relation["revision"])}

    def require_consultation(self, consultation_id: str) -> dict:
        identifier(consultation_id, "consultation id")
        if consultation_id not in self.consultations:
            raise LRMError("unknown consultation id")
        return self.consultations[consultation_id]

    def consultation(self, consultation_id: str, at: str, *, include_records: bool = True) -> dict:
        consultation = self.require_consultation(consultation_id)
        reasons = []
        if consultation["closed"]:
            reasons.append("closed")
        if consultation["invalidated"]:
            reasons.append(consultation["invalidated"]["cause"])
        if at >= consultation["until"]:
            reasons.append("expired")
        ineligible = [{"id": item, "reasons": self.ineligibility(item, at)}
                      for item in consultation["ids"] if self.ineligibility(item, at)]
        if ineligible:
            reasons.append("evidence_lapsed")
        result = {
            **consultation, "presence": int(not reasons),
            "stop_reasons": reasons, "ineligible": ineligible,
        }
        if include_records:
            result["records"] = [self.lookup(item, at) for item in consultation["ids"]] if not reasons else []
            result["relations"] = [
                self.relation_view(item) for item in self.relations
                if item["left"] in consultation["ids"] and item["right"] in consultation["ids"]
            ] if not reasons else []
        return result

    def capabilities(self, scope: str | None, at: str) -> dict:
        result = {
            "contract": "LRM local consultation 0.2",
            "write_operations": list(LEGACY_ACTIONS + EVOLUTION_ACTIONS),
            "read_operations": list(READ_OPERATIONS),
            "event_formats": [1, 2],
            "limits": {"max_events": MAX_EVENTS, "max_event_bytes": MAX_EVENT_BYTES,
                       "max_consultation_seconds": MAX_CONSULTATION_SECONDS},
            "meaning": "software capabilities and local blockers, not permission or source capacity",
            "scope": None,
        }
        if scope is not None:
            identifier(scope, "scope")
            result["scope"] = {
                "id": scope, "regulation": self.regulation(scope),
                "selection_revision": self.selections.get(scope, {}).get("revision"),
                "consultation_blockers": self.consultation_blockers(scope, at),
            }
        return result

    def state(self, scope: str, at: str) -> dict:
        identifier(scope, "scope")
        selection = self.selections.get(scope)
        selected_ids = selection["ids"] if selection else []
        active = [item for item in selected_ids if not self.ineligibility(item, at)]
        records = []
        for record_id, record in sorted(self.records.items()):
            if record["scope"] == scope:
                records.append({
                    "id": record_id, "subject": record["subject"],
                    "provenance": record["provenance"],
                    "observed_at": record["observed_at"],
                    "valid_from": record["valid_from"], "valid_until": record["valid_until"],
                    "content_hash": digest(record),
                    "admission_revision": self.admissions[record_id],
                    "selected": record_id in selected_ids,
                    "ineligibility": self.ineligibility(record_id, at),
                })
        relations = [self.relation_view(item) for item in self.relations
                     if self.records[item["left"]]["scope"] == scope]
        conflicts = [item for item in relations if item["kind"] == "contradicts"
                     and item["withdrawal"] is None
                     and item["left"] in active and item["right"] in active]
        return {
            "scope": scope, "selection": selection,
            "regulation": self.regulation(scope),
            "consultations": [self.consultation(item["id"], at, include_records=False)
                              for item in self.consultations.values() if item["scope"] == scope],
            "active_ids": active,
            "lapsed": [{"id": item, "reasons": self.ineligibility(item, at)}
                       for item in selected_ids if item not in active],
            "records": records, "relations": relations,
            "active_declared_conflicts": conflicts,
            "selection_status": ("unselected" if selection is None else
                                 "cleared" if not selected_ids else
                                 "lapsed" if not active else
                                 "partial" if len(active) != len(selected_ids) else "active"),
        }

    def compare(self, left: str, right: str, at: str) -> dict:
        a, b = self.require(left), self.require(right)
        if left == right or a["scope"] != b["scope"]:
            raise LRMError("comparison requires distinct records in the same scope")
        return {
            "left": self.lookup(left, at), "right": self.lookup(right, at),
            "equal_fields": sorted(key for key in a if key != "id" and a[key] == b[key]),
            "different_fields": sorted(key for key in a if key != "id" and a[key] != b[key]),
            "declared_relations": [self.relation_view(item) for item in self.relations
                                   if {item["left"], item["right"]} == {left, right}],
            "judgment": "none; structural comparison only",
        }


def validate_event(event: Any, projection: Projection) -> dict:
    fields(event, {"format", "sequence", "previous_hash", "recorded_at", "action", "data", "reason"})
    if type(event["format"]) is not int or event["format"] not in (1, 2):
        raise LRMError("unsupported event format")
    actions = LEGACY_ACTIONS if event["format"] == 1 else EVOLUTION_ACTIONS
    if event["action"] not in actions:
        raise LRMError("operation is not supported by this event format")
    if type(event["sequence"]) is not int or event["sequence"] != projection.revision + 1:
        raise LRMError("event sequence is not contiguous")
    if event["previous_hash"] != projection.head_hash:
        raise LRMError("event hash chain is broken")
    at = timestamp(event["recorded_at"])
    if at != event["recorded_at"] or (projection.recorded_at and at < projection.recorded_at):
        raise LRMError("event time is noncanonical or goes backwards")
    text(event["reason"], "reason")
    normalized = normalize_operation(event["action"], event["data"])
    if canonical(normalized) != canonical(event["data"]):
        raise LRMError("event data is not canonical")
    return event
