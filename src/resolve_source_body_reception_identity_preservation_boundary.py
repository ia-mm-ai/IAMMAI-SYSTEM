"""Resolve source-body reception identity preservation boundary.

This resolver records identity preservation for one selected source-body
surface in one declared reception request only. It does not recognize or
authorize reception, receive source, define final source-body identity, inflate
the selected surface into whole-body identity, replace source, validate or
invalidate source, create adoption, authority, currentness, standing, vessel or
derivative relation, operation permission, public readiness, final completion,
continuation, publication flow, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class SourceBodyReceptionIdentityPreservationBoundaryError(Exception):
    """Raised for hard source-body reception identity preservation failures."""


RESOLVER_MODULE = "resolve_source_body_reception_identity_preservation_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "source_body_reception_identity_preservation_result"
RESULT_ID_PREFIX = "source_body_reception_identity_preservation"

SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_identity_preservation_boundary"
)

REQUEST_DECLARATION_OUTCOME = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"

OUTCOME_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"
OUTCOME_NOT_PRESERVED = "SOURCE_BODY_RECEPTION_IDENTITY_NOT_PRESERVED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_IDENTITY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_IDENTITY_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_PRESERVED,
    OUTCOME_NOT_PRESERVED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_IDENTITY_PRESERVATION_SCOPE = (
    "SELECTED_SOURCE_BODY_SURFACE_REMAINS_SOURCE",
    "SELECTED_SURFACE_IS_NOT_WHOLE_BODY_BY_DEFAULT",
    "IDENTITY_PRESERVATION_IS_NOT_RECEPTION",
    "IDENTITY_PRESERVATION_IS_NOT_AUTHORIZATION",
    "RECEIVING_CONTEXT_REMAINS_CONTEXT_ONLY",
    "RECEIVING_CONTEXT_IS_NOT_SOURCE",
    "RECEIVING_CONTEXT_IS_NOT_AUTHORITY",
    "RECEIVING_CONTEXT_IS_NOT_CURRENT",
    "CLOSURE_CONTEXT_IS_CONTEXT_ONLY",
    "TERMINAL_SUMMARY_CONTEXT_IS_CONTEXT_ONLY",
    "REQUEST_DECLARATION_IS_CONTEXT_ONLY",
    "NO_SOURCE_REPLACEMENT",
    "NO_SOURCE_VALIDATION_BY_RECEIVING_CONTEXT",
    "NO_SOURCE_INVALIDATION_BY_RECEIVING_CONTEXT",
)

REQUIRED_NON_CLAIMS = (
    "reception_recognized",
    "reception_authorized",
    "source_received",
    "final_source_body_identity_defined",
    "selected_surface_inflated_to_whole_body",
    "source_replaced",
    "source_validated_by_receiving_context",
    "source_invalidated_by_receiving_context",
    "receiving_context_became_source",
    "receiving_context_became_authority",
    "receiving_context_became_current",
    "closure_artifact_became_source",
    "terminal_summary_became_source",
    "latest_artifact_became_source",
    "carrier_possession_became_source",
    "registry_reference_replaced_source",
    "adoption_created",
    "authority_created",
    "currentness_created",
    "standing_created",
    "standing_propagated",
    "vessel_relation_created",
    "derivative_relation_created",
    "operation_permission_created",
    "public_launch_readiness_created",
    "final_completion_claimed",
    "follow_on_work_authorized",
    "continuation_authorized",
    "publication_flow_opened",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

COLLAPSE_FIELDS = {
    "IDENTITY_PRESERVATION_RECOGNIZES_RECEPTION": (
        "reception_recognized",
        "source_body_reception_recognized",
        "reception_recorded",
    ),
    "IDENTITY_PRESERVATION_AUTHORIZES_RECEPTION": (
        "reception_authorized",
        "source_body_reception_authorized",
        "reception_permission_created",
    ),
    "IDENTITY_PRESERVATION_RECEIVES_SOURCE": (
        "source_received",
        "source_body_received",
        "reception_received_source",
    ),
    "IDENTITY_PRESERVATION_DEFINES_FINAL_SOURCE_BODY_IDENTITY": (
        "final_source_body_identity_defined",
        "final_source_body_identity_created",
        "whole_body_identity_defined",
    ),
    "IDENTITY_PRESERVATION_INFLATES_SELECTED_SURFACE_TO_WHOLE_BODY": (
        "selected_surface_inflated_to_whole_body",
        "selected_source_body_surface_is_whole_body",
        "whole_body_identity_claimed",
    ),
    "IDENTITY_PRESERVATION_REPLACES_SOURCE": (
        "source_replaced",
        "source_body_replaced",
        "source_replacement_created",
    ),
    "IDENTITY_PRESERVATION_VALIDATES_SOURCE": (
        "source_validated_by_receiving_context",
        "source_validated",
        "receiving_context_validates_source",
    ),
    "IDENTITY_PRESERVATION_INVALIDATES_SOURCE": (
        "source_invalidated_by_receiving_context",
        "source_invalidated",
        "receiving_context_invalidates_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE": (
        "receiving_context_became_source",
        "receiving_context_treated_as_source",
        "receiving_context_is_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY": (
        "receiving_context_became_authority",
        "receiving_context_treated_as_authority",
        "receiving_context_is_authority",
    ),
    "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT": (
        "receiving_context_became_current",
        "receiving_context_treated_as_current",
        "receiving_context_is_current",
    ),
    "IDENTITY_PRESERVATION_TREATS_CLOSURE_ARTIFACT_AS_SOURCE": (
        "closure_artifact_became_source",
        "distributed_operation_closure_artifact_became_source",
        "closure_artifact_treated_as_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_TERMINAL_SUMMARY_AS_SOURCE": (
        "terminal_summary_became_source",
        "terminal_summary_treated_as_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_REQUEST_DECLARATION_AS_SOURCE": (
        "request_declaration_became_source",
        "request_declaration_artifact_became_source",
        "request_declaration_treated_as_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_LATEST_ARTIFACT_AS_SOURCE": (
        "latest_artifact_became_source",
        "latest_file_became_source",
        "latest_turn_became_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_CARRIER_POSSESSION_AS_SOURCE": (
        "carrier_possession_became_source",
        "carrier_possession_treated_as_source",
    ),
    "IDENTITY_PRESERVATION_TREATS_REGISTRY_REFERENCE_AS_SOURCE_REPLACEMENT": (
        "registry_reference_replaced_source",
        "registry_reference_became_source_replacement",
    ),
    "IDENTITY_PRESERVATION_CREATES_ADOPTION": (
        "adoption_created",
        "source_adopted",
    ),
    "IDENTITY_PRESERVATION_CREATES_AUTHORITY": (
        "authority_created",
        "source_authority_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_CURRENTNESS": (
        "currentness_created",
        "source_currentness_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_STANDING": (
        "standing_created",
        "source_standing_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_STANDING_PROPAGATION": (
        "standing_propagated",
        "standing_propagation_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_VESSEL_RELATION": (
        "vessel_relation_created",
        "vessel_relation_authorized",
    ),
    "IDENTITY_PRESERVATION_CREATES_DERIVATIVE_RELATION": (
        "derivative_relation_created",
        "derivative_reception_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_OPERATION_PERMISSION": (
        "operation_permission_created",
        "operation_authorized",
        "permission_created",
    ),
    "IDENTITY_PRESERVATION_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
        "public_launch_ready",
    ),
    "IDENTITY_PRESERVATION_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_system_completion_claimed",
        "final_completion_created",
    ),
    "IDENTITY_PRESERVATION_AUTHORIZES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "successor_scheduled",
    ),
    "IDENTITY_PRESERVATION_AUTHORIZES_CONTINUATION": (
        "continuation_authorized",
        "continuation_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "IDENTITY_PRESERVATION_OPENS_PUBLICATION_FLOW": (
        "publication_flow_opened",
        "publication_authorized",
        "public_flow_opened",
    ),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED": (
        "Declared identity preservation request is malformed."
    ),
    "DECLARED_IDENTITY_PRESERVATION_REQUEST_UNREADABLE": (
        "Declared identity preservation request path is unreadable."
    ),
    "IDENTITY_PRESERVATION_QUESTION_UNDECLARED": (
        "Identity preservation question is undeclared."
    ),
    "IDENTITY_PRESERVATION_INTENT_UNSUPPORTED": (
        "Identity preservation intent is unsupported."
    ),
    "IDENTITY_PRESERVATION_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Identity preservation review was explicitly blocked by request intent."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING": (
        "Selected reception request declaration result is missing."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_UNREADABLE": (
        "Selected reception request declaration result path is unreadable."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED": (
        "Selected reception request declaration result is malformed."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_OUTCOME_MISSING": (
        "Selected reception request declaration outcome is missing."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_NOT_DECLARED": (
        "Selected reception request declaration outcome is not declared."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_HAS_FAILED_CHECKS": (
        "Selected reception request declaration has failed checks."
    ),
    "SELECTED_SOURCE_BODY_SURFACE_MISSING": (
        "Selected source-body surface is missing."
    ),
    "SELECTED_SOURCE_BODY_SURFACE_MALFORMED": (
        "Selected source-body surface is malformed."
    ),
    "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING": (
        "Selected source-body surface identifier is missing."
    ),
    "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING": (
        "Selected source-body surface type is missing."
    ),
    "SELECTED_SOURCE_BODY_SURFACE_REFERENCE_MISSING": (
        "Selected source-body surface path or reference is missing."
    ),
    "SOURCE_BODY_IDENTITY_BASIS_MISSING": "Source-body identity basis is missing.",
    "SOURCE_BODY_LINEAGE_BASIS_MISSING": "Source-body lineage basis is missing.",
    "RECEIVING_CONTEXT_MISSING": "Receiving context is missing.",
    "RECEIVING_CONTEXT_MALFORMED": "Receiving context is malformed.",
    "RECEIVING_CONTEXT_TYPE_MISSING": "Receiving context type is missing.",
    "RECEPTION_CLASS_MISSING": "Reception class is missing.",
    "RECEPTION_PURPOSE_MISSING": "Reception purpose is missing.",
    "RECEPTION_LIMITS_MISSING": "Reception limits are missing.",
    "UNSUPPORTED_IDENTITY_PRESERVATION_SCOPE": (
        "Identity preservation scope is missing or unsupported."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required identity preservation non-claim is missing or true."
    ),
}

for _code in COLLAPSE_FIELDS:
    BLOCK_REASON_BY_CODE.setdefault(_code, _code.replace("_", " ").lower())


def _utc_now() -> str:
    return datetime.datetime.now(datetime.UTC).replace(microsecond=0).isoformat()


def _copy(value: Any) -> Any:
    return copy.deepcopy(value)


def _present(value: Any) -> bool:
    if value is None or value == "":
        return False
    if isinstance(value, (dict, list, tuple, set)) and not value:
        return False
    return True


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, Mapping) else {}


def _first(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _first_key(mapping: Any, keys: Sequence[str]) -> Any:
    if not isinstance(mapping, Mapping):
        return None
    for key in keys:
        value = mapping.get(key)
        if _present(value):
            return value
    return None


def _get(mapping: Any, path: Sequence[str], default: Any = None) -> Any:
    current = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return default
        current = current[key]
    return current


def _claim_true(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str) and value.strip().lower() in {"true", "yes", "1"}:
        return True
    return False


def _any_claim_true(mapping: Any, keys: Sequence[str]) -> bool:
    return isinstance(mapping, Mapping) and any(_claim_true(mapping.get(key)) for key in keys)


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None, str | None]:
    resolved = Path(path)
    try:
        with resolved.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return None, "unreadable", f"Path not found: {resolved}"
    except OSError as exc:
        return None, "unreadable", str(exc)
    except json.JSONDecodeError as exc:
        return None, "malformed", str(exc)
    if not isinstance(payload, dict):
        return None, "malformed", "JSON payload is not an object."
    return payload, None, None


def _safe_component(value: Any) -> str:
    text = str(value or RESULT_ID_PREFIX).strip()
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in text)
    return safe.strip("_") or RESULT_ID_PREFIX


def _as_payload(value: Any, reference_key: str, id_key: str) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return _copy(dict(value))
    if isinstance(value, str) and value:
        return {id_key: value, reference_key: value}
    return {}


def _context_only(value: Any) -> bool:
    if not _present(value):
        return True
    if not isinstance(value, Mapping):
        return True
    if value.get("context_only") is False or value.get("evidence_only") is False:
        return False
    forbidden = (
        "selected_as_source_body_surface",
        "treated_as_source_body_surface",
        "source_body_surface_selected",
        "source_body_reception_authorized",
        "reception_authorized",
        "source_received",
        "adoption_created",
        "authority_created",
        "currentness_created",
        "standing_created",
        "source_replaced",
        "source_validated_by_receiving_context",
        "source_invalidated_by_receiving_context",
        "closure_artifact_became_source",
        "terminal_summary_became_source",
        "request_declaration_became_source",
    )
    return not _any_claim_true(value, forbidden)


def _selected_declaration_failed_count(declaration: Mapping[str, Any]) -> int | None:
    summary_count = _get(
        declaration,
        ("source_body_reception_request_summary", "failed_check_count"),
    )
    if isinstance(summary_count, int):
        return summary_count
    checks = declaration.get("declaration_checks")
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _load_selected_declaration(
    request: Mapping[str, Any],
) -> tuple[Any, str | None, str | None, str | None]:
    path = request.get("selected_reception_request_declaration_path")
    if _present(path):
        payload, error, detail = _read_json_object(str(path))
        if error == "unreadable":
            return {}, "RECEPTION_REQUEST_DECLARATION_RESULT_UNREADABLE", detail, str(path)
        if error == "malformed":
            return {}, "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED", detail, str(path)
        assert payload is not None
        return payload, None, None, str(path)
    raw = request.get("selected_reception_request_declaration")
    if isinstance(raw, Mapping):
        return _copy(dict(raw)), None, None, None
    if isinstance(raw, str) and raw:
        return {
            "selected_reception_request_declaration_id": raw,
            "selected_reception_request_declaration_reference": raw,
        }, None, None, None
    if _present(raw):
        return {}, "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED", None, None
    return {}, None, None, None


def _selected_declaration_section(
    request: Mapping[str, Any],
    declaration: Any,
    load_code: str | None,
    load_detail: str | None,
    path: str | None,
) -> dict[str, Any]:
    declaration_map = _mapping(declaration)
    declared_question = _mapping(declaration_map.get("declared_reception_question"))
    summary = _mapping(declaration_map.get("source_body_reception_request_summary"))
    metadata = _mapping(declaration_map.get("source_body_reception_request_metadata"))
    statement = _mapping(declaration_map.get("declaration_statement"))
    non_claims = _mapping(declaration_map.get("non_claims"))
    selected_id = _first(
        request.get("selected_reception_request_declaration_id"),
        declared_question.get("reception_request_id"),
        summary.get("reception_request_id"),
        metadata.get("source_body_reception_request_result_id"),
        declaration_map.get("selected_reception_request_declaration_id"),
    )
    outcome = _first(
        request.get("selected_reception_request_declaration_outcome"),
        request.get("expected_selected_reception_request_declaration_outcome"),
        declaration_map.get("outcome"),
        summary.get("outcome"),
    )
    failed_count = _first(
        request.get("selected_reception_request_declaration_failed_check_count"),
        _selected_declaration_failed_count(declaration_map),
    )
    declaration_present = _present(request.get("selected_reception_request_declaration")) or _present(path)
    sections = (declaration_map, statement, non_claims, summary)
    return {
        "selected_reception_request_declaration": _copy(declaration),
        "selected_reception_request_declaration_path": path,
        "selected_reception_request_declaration_id": selected_id,
        "selected_reception_request_declaration_outcome": outcome,
        "expected_selected_reception_request_declaration_outcome": request.get(
            "expected_selected_reception_request_declaration_outcome",
            REQUEST_DECLARATION_OUTCOME,
        ),
        "selected_reception_request_declaration_preserved": declaration_present
        and load_code is None,
        "selected_reception_request_declaration_recorded": outcome == REQUEST_DECLARATION_OUTCOME,
        "selected_reception_request_declaration_failed_check_count": failed_count,
        "selected_reception_request_declaration_failed_check_count_zero": failed_count == 0,
        "selected_reception_request_declaration_load_block_code": load_code,
        "selected_reception_request_declaration_load_block_reason": load_detail,
        "request_declaration_did_not_recognize_reception": not any(
            _any_claim_true(item, ("reception_recognized",)) for item in sections
        ),
        "request_declaration_did_not_authorize_reception": not any(
            _any_claim_true(item, ("reception_authorized",)) for item in sections
        ),
        "request_declaration_did_not_receive_source": not any(
            _any_claim_true(item, ("source_received",)) for item in sections
        ),
        "request_declaration_remains_context_evidence_only": not any(
            _any_claim_true(
                item,
                (
                    "request_declaration_became_source",
                    "request_declaration_artifact_became_source",
                    "request_declaration_treated_as_source",
                ),
            )
            for item in sections
        ),
        "request_declaration_did_not_mutate_replay_or_merge": not any(
            _any_claim_true(item, ("mutation_performed", "replay_performed", "merge_performed"))
            for item in sections
        ),
        "selected_source_body_surface_preserved_by_request_declaration": _first(
            statement.get("selected_source_body_surface_preserved"),
            summary.get("selected_source_body_surface_preserved"),
        ),
        "selected_source_body_surface_remains_source_by_request_declaration": _first(
            statement.get("selected_source_body_surface_remains_source"),
            summary.get("selected_source_body_surface_remains_source"),
        ),
        "receiving_context_declared_by_request_declaration": _first(
            statement.get("receiving_context_declared"),
            summary.get("receiving_context_declared"),
        ),
        "receiving_context_remains_context_only_by_request_declaration": _first(
            statement.get("receiving_context_remains_context_only"),
            summary.get("receiving_context_remains_context_only"),
        ),
    }


def _declaration_map(section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(section.get("selected_reception_request_declaration"))


def _selected_source_surface_section(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> dict[str, Any]:
    declaration_map = _declaration_map(selected_declaration)
    declaration_surface = _mapping(declaration_map.get("selected_source_body_surface"))
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        declaration_surface.get("selected_source_body_surface"),
        declaration_surface if declaration_surface else None,
    )
    payload = _as_payload(
        raw_surface,
        "selected_source_body_surface_reference",
        "selected_source_body_surface_identifier",
    )
    identifier = _first(
        request.get("selected_source_body_surface_identifier"),
        _first_key(payload, ("selected_source_body_surface_identifier", "source_body_surface_identifier", "surface_id", "id")),
        declaration_surface.get("selected_source_body_surface_identifier"),
    )
    surface_type = _first(
        request.get("selected_source_body_surface_type"),
        _first_key(payload, ("selected_source_body_surface_type", "source_body_surface_type", "surface_type", "type")),
        declaration_surface.get("selected_source_body_surface_type"),
        "SOURCE_BODY_SURFACE_REFERENCE" if isinstance(raw_surface, str) else None,
    )
    surface_path = _first(
        request.get("selected_source_body_surface_path"),
        _first_key(payload, ("selected_source_body_surface_path", "source_body_surface_path", "surface_path", "path")),
        declaration_surface.get("selected_source_body_surface_path"),
    )
    surface_reference = _first(
        request.get("selected_source_body_surface_reference"),
        _first_key(payload, ("selected_source_body_surface_reference", "source_body_surface_reference", "surface_reference", "reference")),
        declaration_surface.get("selected_source_body_surface_reference"),
        raw_surface if isinstance(raw_surface, str) else None,
    )
    identity_basis = _first(
        request.get("source_body_identity_basis"),
        _first_key(payload, ("source_body_identity_basis", "identity_basis")),
        declaration_surface.get("source_body_identity_basis"),
    )
    lineage_basis = _first(
        request.get("source_body_lineage_basis"),
        _first_key(payload, ("source_body_lineage_basis", "lineage_basis")),
        declaration_surface.get("source_body_lineage_basis"),
    )
    sections = (
        request,
        payload,
        declaration_surface,
        _mapping(identity_basis),
        _mapping(lineage_basis),
        _mapping(request.get("identity_preservation_basis")),
        _mapping(request.get("declared_non_claims")),
    )
    source_remains_source = not any(
        item.get("selected_source_body_surface_remains_source") is False
        or item.get("source_body_surface_remains_source") is False
        or _any_claim_true(
            item,
            (
                "source_received",
                "adoption_created",
                "source_replaced",
                "source_validated_by_receiving_context",
                "source_invalidated_by_receiving_context",
            ),
        )
        for item in sections
    )
    not_whole_body = not any(
        _any_claim_true(
            item,
            (
                "selected_surface_inflated_to_whole_body",
                "selected_source_body_surface_is_whole_body",
                "whole_body_identity_defined",
                "final_source_body_identity_defined",
            ),
        )
        for item in sections
    )
    return {
        "selected_source_body_surface": payload if payload else _copy(raw_surface),
        "selected_source_body_surface_identifier": identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_path": surface_path,
        "selected_source_body_surface_reference": surface_reference,
        "source_body_identity_basis": _copy(identity_basis),
        "source_body_lineage_basis": _copy(lineage_basis),
        "selected_source_body_surface_preserved": _present(raw_surface)
        or _present(identifier),
        "selected_source_body_surface_remains_source": source_remains_source,
        "selected_surface_is_not_whole_body_by_default": not_whole_body,
        "selected_source_body_surface_not_received": not any(
            _any_claim_true(item, ("source_received", "reception_recognized"))
            for item in sections
        ),
        "selected_source_body_surface_not_adopted": not any(
            _any_claim_true(item, ("adoption_created", "source_adopted"))
            for item in sections
        ),
        "selected_source_body_surface_not_replaced": not any(
            _any_claim_true(item, ("source_replaced", "source_body_replaced"))
            for item in sections
        ),
        "selected_source_body_surface_not_validated_by_receiving_context": not any(
            _any_claim_true(item, ("source_validated_by_receiving_context",))
            for item in sections
        ),
        "selected_source_body_surface_not_invalidated_by_receiving_context": not any(
            _any_claim_true(item, ("source_invalidated_by_receiving_context",))
            for item in sections
        ),
        "final_source_body_identity_defined": False,
        "whole_body_identity_defined": False,
        "currentness_created": False,
        "authority_created": False,
    }


def _receiving_context_section(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> dict[str, Any]:
    declaration_map = _declaration_map(selected_declaration)
    declaration_context = _mapping(declaration_map.get("receiving_context"))
    raw_context = _first(
        request.get("receiving_context"),
        declaration_context.get("receiving_context"),
        declaration_context if declaration_context else None,
    )
    payload = _as_payload(raw_context, "receiving_context_reference", "receiving_context_id")
    context_id = _first(
        request.get("receiving_context_id"),
        _first_key(payload, ("receiving_context_id", "receiving_context_name", "receiving_context_reference", "context_id", "id", "name")),
        declaration_context.get("receiving_context_id"),
        raw_context if isinstance(raw_context, str) else None,
    )
    context_type = _first(
        request.get("receiving_context_type"),
        _first_key(payload, ("receiving_context_type", "context_type", "type")),
        declaration_context.get("receiving_context_type"),
        "RECEIVING_CONTEXT" if isinstance(raw_context, str) else None,
    )
    sections = (request, payload, declaration_context, _mapping(request.get("declared_non_claims")))
    context_only = _context_only(payload) and not any(
        item.get("receiving_context_remains_context_only") is False
        or _any_claim_true(
            item,
            (
                "receiving_context_became_source",
                "receiving_context_became_authority",
                "receiving_context_became_current",
                "source_validated_by_receiving_context",
                "source_invalidated_by_receiving_context",
                "adoption_created",
                "operation_permission_created",
                "publication_flow_opened",
            ),
        )
        for item in sections
    )
    return {
        "receiving_context": payload if payload else _copy(raw_context),
        "receiving_context_id": context_id,
        "receiving_context_type": context_type,
        "receiving_context_preserved": _present(raw_context) or _present(context_id),
        "receiving_context_remains_context_only": context_only,
        "receiving_context_is_not_source": not any(
            _any_claim_true(item, ("receiving_context_became_source",)) for item in sections
        ),
        "receiving_context_is_not_authority": not any(
            _any_claim_true(item, ("receiving_context_became_authority",)) for item in sections
        ),
        "receiving_context_is_not_current": not any(
            _any_claim_true(item, ("receiving_context_became_current",)) for item in sections
        ),
        "receiving_context_did_not_validate_source": not any(
            _any_claim_true(item, ("source_validated_by_receiving_context",)) for item in sections
        ),
        "receiving_context_did_not_invalidate_source": not any(
            _any_claim_true(item, ("source_invalidated_by_receiving_context",)) for item in sections
        ),
        "receiving_context_did_not_create_adoption": not any(
            _any_claim_true(item, ("adoption_created",)) for item in sections
        ),
        "receiving_context_did_not_create_operation_permission": not any(
            _any_claim_true(item, ("operation_permission_created",)) for item in sections
        ),
        "receiving_context_did_not_open_publication_flow": not any(
            _any_claim_true(item, ("publication_flow_opened",)) for item in sections
        ),
    }


def _closure_context_value(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> Any:
    declaration = _declaration_map(selected_declaration)
    declaration_surface = _mapping(declaration.get("selected_source_body_surface"))
    return _first(
        request.get("distributed_operation_closure_context"),
        declaration_surface.get("distributed_operation_closure_context"),
    )


def _terminal_summary_context_value(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> Any:
    declaration = _declaration_map(selected_declaration)
    declaration_surface = _mapping(declaration.get("selected_source_body_surface"))
    return _first(
        request.get("terminal_summary_context"),
        declaration_surface.get("terminal_summary_context"),
    )


def _request_declaration_context_only(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> bool:
    return (
        selected_declaration.get("request_declaration_remains_context_evidence_only")
        is True
        and _context_only(request.get("request_declaration_context"))
    )


def _reception_class_value(request: Mapping[str, Any], selected_declaration: Mapping[str, Any]) -> Any:
    declaration = _declaration_map(selected_declaration)
    class_section = _mapping(declaration.get("reception_class"))
    return _first(
        request.get("reception_class"),
        class_section.get("selected_reception_class"),
        _get(declaration, ("source_body_reception_request_summary", "reception_class")),
    )


def _reception_purpose_value(request: Mapping[str, Any], selected_declaration: Mapping[str, Any]) -> Any:
    declaration = _declaration_map(selected_declaration)
    purpose_section = _mapping(declaration.get("reception_purpose"))
    return _first(
        request.get("reception_purpose"),
        purpose_section.get("reception_purpose"),
        _get(declaration, ("source_body_reception_request_summary", "reception_purpose")),
    )


def _reception_limits_value(request: Mapping[str, Any], selected_declaration: Mapping[str, Any]) -> Any:
    declaration = _declaration_map(selected_declaration)
    limits_section = _mapping(declaration.get("reception_limits"))
    return _first(request.get("reception_limits"), limits_section.get("reception_limits"))


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    return all(key in non_claims and non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _scope_values(request: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    raw_scope = request.get("identity_preservation_scope")
    if isinstance(raw_scope, str):
        values = [raw_scope]
    elif isinstance(raw_scope, Mapping):
        selected = _first(
            raw_scope.get("selected_identity_preservation_scope_values"),
            raw_scope.get("identity_preservation_scope_values"),
            raw_scope.get("scope_values"),
            raw_scope.get("values"),
        )
        if isinstance(selected, str):
            values = [selected]
        elif isinstance(selected, Sequence) and not isinstance(selected, (bytes, bytearray)):
            values = [str(value) for value in selected]
        else:
            values = [str(key) for key, value in raw_scope.items() if value is True]
    elif isinstance(raw_scope, Sequence) and not isinstance(raw_scope, (bytes, bytearray)):
        values = [str(value) for value in raw_scope]
    else:
        values = []
    unsupported = [
        value for value in values if value not in SUPPORTED_IDENTITY_PRESERVATION_SCOPE
    ]
    return values, unsupported


def _collapse_sections(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> list[Mapping[str, Any]]:
    declaration = _declaration_map(selected_declaration)
    return [
        request,
        _mapping(request.get("identity_preservation_basis")),
        _mapping(request.get("identity_preservation_scope")),
        _mapping(request.get("declared_non_claims")),
        _mapping(request.get("additional_basis_context")),
        _mapping(request.get("not_preserved_basis")),
        selected_declaration,
        declaration,
        _mapping(declaration.get("non_claims")),
        _mapping(declaration.get("declaration_statement")),
        _mapping(declaration.get("selected_source_body_surface")),
        _mapping(declaration.get("receiving_context")),
        selected_surface,
        _mapping(selected_surface.get("selected_source_body_surface")),
        _mapping(selected_surface.get("source_body_identity_basis")),
        _mapping(selected_surface.get("source_body_lineage_basis")),
        receiving_context,
        _mapping(receiving_context.get("receiving_context")),
        _mapping(request.get("distributed_operation_closure_context")),
        _mapping(request.get("terminal_summary_context")),
        _mapping(request.get("request_declaration_context")),
    ]


def _collapse_code(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> str | None:
    for code, fields in COLLAPSE_FIELDS.items():
        for section in _collapse_sections(request, selected_declaration, selected_surface, receiving_context):
            if _any_claim_true(section, fields):
                return code
    return None


def _check(
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None,
) -> dict[str, Any]:
    return {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": expected,
        "actual_posture": actual,
        "block_code": None if passed else code,
        "failure_code": None if passed else code,
    }


def _build_checks(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> list[dict[str, Any]]:
    declaration_load_code = selected_declaration.get(
        "selected_reception_request_declaration_load_block_code"
    )
    raw_declaration = request.get("selected_reception_request_declaration")
    declaration_shape_valid = (
        not _present(raw_declaration) or isinstance(raw_declaration, (Mapping, str))
    )
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        _get(
            selected_declaration,
            (
                "selected_reception_request_declaration",
                "selected_source_body_surface",
            ),
        ),
    )
    raw_context = _first(
        request.get("receiving_context"),
        _get(
            selected_declaration,
            ("selected_reception_request_declaration", "receiving_context"),
        ),
    )
    surface_shape_valid = (
        not _present(raw_surface) or isinstance(raw_surface, (Mapping, str))
    )
    context_shape_valid = (
        not _present(raw_context) or isinstance(raw_context, (Mapping, str))
    )
    reception_class = _reception_class_value(request, selected_declaration)
    reception_purpose = _reception_purpose_value(request, selected_declaration)
    reception_limits = _reception_limits_value(request, selected_declaration)
    scope_values, unsupported_scope = _scope_values(request)
    collapse_code = _collapse_code(request, selected_declaration, selected_surface, receiving_context)
    checks = [
        _check(
            "identity preservation question declared",
            _present(request.get("identity_preservation_question")),
            "declared identity preservation question",
            request.get("identity_preservation_question"),
            "IDENTITY_PRESERVATION_QUESTION_UNDECLARED",
        ),
        _check(
            "identity preservation intent supported",
            request.get("identity_preservation_intent", INTENT_RECORD) in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            request.get("identity_preservation_intent", INTENT_RECORD),
            "IDENTITY_PRESERVATION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected reception request declaration result present",
            selected_declaration.get("selected_reception_request_declaration_preserved") is True,
            "selected reception request declaration result",
            selected_declaration.get("selected_reception_request_declaration_id"),
            declaration_load_code or "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
        ),
        _check(
            "selected reception request declaration result well formed",
            declaration_shape_valid and declaration_load_code is None,
            "mapping, reference string, or readable JSON object",
            declaration_load_code or type(raw_declaration).__name__,
            declaration_load_code or "RECEPTION_REQUEST_DECLARATION_RESULT_MALFORMED",
        ),
        _check(
            "selected reception request declaration outcome declared",
            _present(selected_declaration.get("selected_reception_request_declaration_outcome")),
            "selected reception request declaration outcome",
            selected_declaration.get("selected_reception_request_declaration_outcome"),
            "RECEPTION_REQUEST_DECLARATION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected reception request declaration outcome declared request",
            selected_declaration.get("selected_reception_request_declaration_recorded") is True,
            REQUEST_DECLARATION_OUTCOME,
            selected_declaration.get("selected_reception_request_declaration_outcome"),
            "RECEPTION_REQUEST_DECLARATION_RESULT_NOT_DECLARED",
        ),
        _check(
            "selected reception request declaration failed check count zero",
            selected_declaration.get("selected_reception_request_declaration_failed_check_count_zero") is True,
            0,
            selected_declaration.get("selected_reception_request_declaration_failed_check_count"),
            "RECEPTION_REQUEST_DECLARATION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected source-body surface preserved",
            selected_surface.get("selected_source_body_surface_preserved") is True,
            "selected source-body surface",
            selected_surface.get("selected_source_body_surface"),
            "SELECTED_SOURCE_BODY_SURFACE_MISSING",
        ),
        _check(
            "selected source-body surface well formed",
            surface_shape_valid,
            "mapping or string selected source-body surface",
            type(raw_surface).__name__ if _present(raw_surface) else "missing",
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "selected source-body surface identifier preserved",
            _present(selected_surface.get("selected_source_body_surface_identifier")),
            "selected source-body surface identifier",
            selected_surface.get("selected_source_body_surface_identifier"),
            "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING",
        ),
        _check(
            "selected source-body surface type preserved",
            _present(selected_surface.get("selected_source_body_surface_type")),
            "selected source-body surface type",
            selected_surface.get("selected_source_body_surface_type"),
            "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING",
        ),
        _check(
            "selected source-body surface path/reference preserved",
            _present(selected_surface.get("selected_source_body_surface_path"))
            or _present(selected_surface.get("selected_source_body_surface_reference")),
            "selected source-body surface path or reference",
            _first(
                selected_surface.get("selected_source_body_surface_path"),
                selected_surface.get("selected_source_body_surface_reference"),
            ),
            "SELECTED_SOURCE_BODY_SURFACE_REFERENCE_MISSING",
        ),
        _check(
            "source-body identity basis preserved",
            _present(selected_surface.get("source_body_identity_basis")),
            "source-body identity basis",
            selected_surface.get("source_body_identity_basis"),
            "SOURCE_BODY_IDENTITY_BASIS_MISSING",
        ),
        _check(
            "source-body lineage basis preserved",
            _present(selected_surface.get("source_body_lineage_basis")),
            "source-body lineage basis",
            selected_surface.get("source_body_lineage_basis"),
            "SOURCE_BODY_LINEAGE_BASIS_MISSING",
        ),
        _check(
            "selected source-body surface remains source",
            selected_surface.get("selected_source_body_surface_remains_source") is True,
            True,
            selected_surface.get("selected_source_body_surface_remains_source"),
            collapse_code or "IDENTITY_PRESERVATION_REPLACES_SOURCE",
        ),
        _check(
            "selected source-body surface is not whole body by default",
            selected_surface.get("selected_surface_is_not_whole_body_by_default") is True,
            True,
            selected_surface.get("selected_surface_is_not_whole_body_by_default"),
            collapse_code or "IDENTITY_PRESERVATION_INFLATES_SELECTED_SURFACE_TO_WHOLE_BODY",
        ),
        _check(
            "receiving context well formed",
            context_shape_valid,
            "mapping or string receiving context",
            type(raw_context).__name__ if _present(raw_context) else "missing",
            "RECEIVING_CONTEXT_MALFORMED",
        ),
        _check(
            "receiving context preserved",
            receiving_context.get("receiving_context_preserved") is True,
            "receiving context",
            receiving_context.get("receiving_context_id"),
            "RECEIVING_CONTEXT_MISSING",
        ),
        _check(
            "receiving context type preserved",
            _present(receiving_context.get("receiving_context_type")),
            "receiving context type",
            receiving_context.get("receiving_context_type"),
            "RECEIVING_CONTEXT_TYPE_MISSING",
        ),
        _check(
            "receiving context remains context only",
            receiving_context.get("receiving_context_remains_context_only") is True,
            True,
            receiving_context.get("receiving_context_remains_context_only"),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not source",
            receiving_context.get("receiving_context_is_not_source") is True,
            True,
            receiving_context.get("receiving_context_is_not_source"),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not authority",
            receiving_context.get("receiving_context_is_not_authority") is True,
            True,
            receiving_context.get("receiving_context_is_not_authority"),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving context is not current",
            receiving_context.get("receiving_context_is_not_current") is True,
            True,
            receiving_context.get("receiving_context_is_not_current"),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT",
        ),
        _check(
            "reception class preserved",
            _present(reception_class),
            "reception class",
            reception_class,
            "RECEPTION_CLASS_MISSING",
        ),
        _check(
            "reception purpose preserved",
            _present(reception_purpose),
            "reception purpose",
            reception_purpose,
            "RECEPTION_PURPOSE_MISSING",
        ),
        _check(
            "reception limits preserved",
            _present(reception_limits),
            "reception limits",
            reception_limits,
            "RECEPTION_LIMITS_MISSING",
        ),
        _check(
            "distributed-operation closure context remains context/evidence only where supplied",
            _context_only(_closure_context_value(request, selected_declaration)),
            True,
            _context_only(_closure_context_value(request, selected_declaration)),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_CLOSURE_ARTIFACT_AS_SOURCE",
        ),
        _check(
            "terminal summary context remains context/evidence only where supplied",
            _context_only(_terminal_summary_context_value(request, selected_declaration)),
            True,
            _context_only(_terminal_summary_context_value(request, selected_declaration)),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_TERMINAL_SUMMARY_AS_SOURCE",
        ),
        _check(
            "request declaration remains context/evidence only",
            _request_declaration_context_only(request, selected_declaration),
            True,
            _request_declaration_context_only(request, selected_declaration),
            collapse_code or "IDENTITY_PRESERVATION_TREATS_REQUEST_DECLARATION_AS_SOURCE",
        ),
        _check(
            "no source replacement",
            selected_surface.get("selected_source_body_surface_not_replaced") is True,
            True,
            selected_surface.get("selected_source_body_surface_not_replaced"),
            collapse_code or "IDENTITY_PRESERVATION_REPLACES_SOURCE",
        ),
        _check(
            "no source validation by receiving context",
            selected_surface.get("selected_source_body_surface_not_validated_by_receiving_context") is True,
            True,
            selected_surface.get("selected_source_body_surface_not_validated_by_receiving_context"),
            collapse_code or "IDENTITY_PRESERVATION_VALIDATES_SOURCE",
        ),
        _check(
            "no source invalidation by receiving context",
            selected_surface.get("selected_source_body_surface_not_invalidated_by_receiving_context") is True,
            True,
            selected_surface.get("selected_source_body_surface_not_invalidated_by_receiving_context"),
            collapse_code or "IDENTITY_PRESERVATION_INVALIDATES_SOURCE",
        ),
        _check(
            "declaration still does not recognize reception",
            selected_declaration.get("request_declaration_did_not_recognize_reception") is True,
            True,
            selected_declaration.get("request_declaration_did_not_recognize_reception"),
            collapse_code or "IDENTITY_PRESERVATION_RECOGNIZES_RECEPTION",
        ),
        _check(
            "declaration still does not authorize reception",
            selected_declaration.get("request_declaration_did_not_authorize_reception") is True,
            True,
            selected_declaration.get("request_declaration_did_not_authorize_reception"),
            collapse_code or "IDENTITY_PRESERVATION_AUTHORIZES_RECEPTION",
        ),
        _check(
            "latest artifact not source",
            collapse_code != "IDENTITY_PRESERVATION_TREATS_LATEST_ARTIFACT_AS_SOURCE",
            False,
            collapse_code == "IDENTITY_PRESERVATION_TREATS_LATEST_ARTIFACT_AS_SOURCE",
            "IDENTITY_PRESERVATION_TREATS_LATEST_ARTIFACT_AS_SOURCE",
        ),
        _check(
            "carrier possession not source",
            collapse_code != "IDENTITY_PRESERVATION_TREATS_CARRIER_POSSESSION_AS_SOURCE",
            False,
            collapse_code == "IDENTITY_PRESERVATION_TREATS_CARRIER_POSSESSION_AS_SOURCE",
            "IDENTITY_PRESERVATION_TREATS_CARRIER_POSSESSION_AS_SOURCE",
        ),
        _check(
            "registry/reference not source replacement",
            collapse_code != "IDENTITY_PRESERVATION_TREATS_REGISTRY_REFERENCE_AS_SOURCE_REPLACEMENT",
            False,
            collapse_code == "IDENTITY_PRESERVATION_TREATS_REGISTRY_REFERENCE_AS_SOURCE_REPLACEMENT",
            "IDENTITY_PRESERVATION_TREATS_REGISTRY_REFERENCE_AS_SOURCE_REPLACEMENT",
        ),
        _check(
            "identity preservation scope supported",
            bool(scope_values) and not unsupported_scope,
            list(SUPPORTED_IDENTITY_PRESERVATION_SCOPE),
            scope_values if scope_values else "missing",
            "UNSUPPORTED_IDENTITY_PRESERVATION_SCOPE",
        ),
    ]
    false_checks = (
        ("identity preservation does not recognize reception", "IDENTITY_PRESERVATION_RECOGNIZES_RECEPTION"),
        ("identity preservation does not authorize reception", "IDENTITY_PRESERVATION_AUTHORIZES_RECEPTION"),
        ("identity preservation does not receive source", "IDENTITY_PRESERVATION_RECEIVES_SOURCE"),
        ("identity preservation does not define final source-body identity", "IDENTITY_PRESERVATION_DEFINES_FINAL_SOURCE_BODY_IDENTITY"),
        ("identity preservation does not inflate selected surface to whole body", "IDENTITY_PRESERVATION_INFLATES_SELECTED_SURFACE_TO_WHOLE_BODY"),
        ("identity preservation does not replace source", "IDENTITY_PRESERVATION_REPLACES_SOURCE"),
        ("identity preservation does not validate source", "IDENTITY_PRESERVATION_VALIDATES_SOURCE"),
        ("identity preservation does not invalidate source", "IDENTITY_PRESERVATION_INVALIDATES_SOURCE"),
        ("identity preservation does not treat receiving context as source", "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE"),
        ("identity preservation does not treat receiving context as authority", "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY"),
        ("identity preservation does not treat receiving context as current", "IDENTITY_PRESERVATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT"),
        ("identity preservation does not treat closure artifact as source", "IDENTITY_PRESERVATION_TREATS_CLOSURE_ARTIFACT_AS_SOURCE"),
        ("identity preservation does not treat terminal summary as source", "IDENTITY_PRESERVATION_TREATS_TERMINAL_SUMMARY_AS_SOURCE"),
        ("identity preservation does not treat request declaration as source", "IDENTITY_PRESERVATION_TREATS_REQUEST_DECLARATION_AS_SOURCE"),
        ("identity preservation does not create adoption", "IDENTITY_PRESERVATION_CREATES_ADOPTION"),
        ("identity preservation does not create authority", "IDENTITY_PRESERVATION_CREATES_AUTHORITY"),
        ("identity preservation does not create currentness", "IDENTITY_PRESERVATION_CREATES_CURRENTNESS"),
        ("identity preservation does not create standing", "IDENTITY_PRESERVATION_CREATES_STANDING"),
        ("identity preservation does not create standing propagation", "IDENTITY_PRESERVATION_CREATES_STANDING_PROPAGATION"),
        ("identity preservation does not create vessel relation", "IDENTITY_PRESERVATION_CREATES_VESSEL_RELATION"),
        ("identity preservation does not create derivative relation", "IDENTITY_PRESERVATION_CREATES_DERIVATIVE_RELATION"),
        ("identity preservation does not create operation permission", "IDENTITY_PRESERVATION_CREATES_OPERATION_PERMISSION"),
        ("identity preservation does not create public readiness", "IDENTITY_PRESERVATION_CREATES_PUBLIC_READINESS"),
        ("identity preservation does not claim final completion", "IDENTITY_PRESERVATION_CLAIMS_FINAL_COMPLETION"),
        ("identity preservation does not authorize follow-on work", "IDENTITY_PRESERVATION_AUTHORIZES_FOLLOW_ON_WORK"),
        ("identity preservation does not authorize continuation", "IDENTITY_PRESERVATION_AUTHORIZES_CONTINUATION"),
        ("identity preservation does not open publication flow", "IDENTITY_PRESERVATION_OPENS_PUBLICATION_FLOW"),
        ("no mutation/replay/merge", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
    )
    checks.extend(
        _check(name, collapse_code != code, False, collapse_code == code, code)
        for name, code in false_checks
    )
    checks.append(
        _check(
            "non-claims remain false",
            _declared_non_claims_valid(request),
            "all required identity preservation non-claims false",
            _declared_non_claims(request),
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if request.get("identity_preservation_intent", INTENT_RECORD) == INTENT_BLOCK:
        checks.append(
            _check(
                "identity preservation review explicitly unblocked",
                False,
                "review not explicitly blocked",
                INTENT_BLOCK,
                "IDENTITY_PRESERVATION_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
            )
        )
    return checks


def _first_failed_code(checks: Sequence[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _block_reason(code: str | None, explicit: Any = None) -> str | None:
    if _present(explicit):
        return str(explicit)
    if code is None:
        return None
    return BLOCK_REASON_BY_CODE.get(code, code.replace("_", " ").lower())


def _metadata(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> dict[str, str]:
    basis = _first(
        request.get("identity_preservation_request_id"),
        selected_declaration.get("selected_reception_request_declaration_id"),
        RESULT_ID_PREFIX,
    )
    return {
        "source_body_reception_identity_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "source_body_reception_identity_result_type": RESULT_TYPE,
        "source_body_reception_identity_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["source_body_reception_identity_preserved"] = outcome == OUTCOME_PRESERVED
    return non_claims


def _declared_question_section(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "identity_preservation_request_id": request.get("identity_preservation_request_id"),
        "identity_preservation_question": request.get("identity_preservation_question"),
        "identity_preservation_intent": request.get("identity_preservation_intent", INTENT_RECORD),
        "declared_identity_preservation_request_path": request.get(
            "declared_identity_preservation_request_path"
        ),
        "requested_identity_preservation_outcome": request.get(
            "requested_identity_preservation_outcome", OUTCOME_PRESERVED
        ),
        "selected_reception_request_declaration_id": selected_declaration.get(
            "selected_reception_request_declaration_id"
        ),
        "selected_reception_request_declaration_outcome": selected_declaration.get(
            "selected_reception_request_declaration_outcome"
        ),
        "identity_preservation_is_not_reception": True,
        "identity_preservation_is_not_authorization": True,
        "identity_preservation_is_not_final_source_body_identity": True,
        "identity_preservation_is_not_whole_body_identity": True,
        "identity_preservation_is_not_adoption": True,
        "identity_preservation_is_not_authority": True,
        "identity_preservation_is_not_currentness": True,
        "identity_preservation_is_not_public_readiness": True,
        "identity_preservation_is_not_final_completion": True,
        "identity_preservation_is_not_follow_on_work": True,
    }


def _identity_preservation_basis(
    request: Mapping[str, Any],
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> dict[str, Any]:
    basis = _copy(request.get("identity_preservation_basis"))
    return {
        "declared_identity_preservation_basis": basis,
        "selected_reception_request_declaration": _copy(
            selected_declaration.get("selected_reception_request_declaration")
        ),
        "selected_source_body_surface": _copy(selected_surface),
        "source_body_identity_basis": _copy(selected_surface.get("source_body_identity_basis")),
        "source_body_lineage_basis": _copy(selected_surface.get("source_body_lineage_basis")),
        "receiving_context": _copy(receiving_context),
        "reception_class": _copy(_reception_class_value(request, selected_declaration)),
        "reception_purpose": _copy(_reception_purpose_value(request, selected_declaration)),
        "reception_limits": _copy(_reception_limits_value(request, selected_declaration)),
        "distributed_operation_closure_context": _copy(
            _closure_context_value(request, selected_declaration)
        ),
        "terminal_summary_context": _copy(
            _terminal_summary_context_value(request, selected_declaration)
        ),
        "request_declaration_context": _copy(request.get("request_declaration_context")),
        "closure_context_is_context_only": _context_only(
            _closure_context_value(request, selected_declaration)
        ),
        "terminal_summary_context_is_context_only": _context_only(
            _terminal_summary_context_value(request, selected_declaration)
        ),
        "request_declaration_is_context_only": _request_declaration_context_only(
            request, selected_declaration
        ),
        "selected_source_body_surface_remains_source": selected_surface.get(
            "selected_source_body_surface_remains_source"
        )
        is True,
        "receiving_context_remains_non_source": receiving_context.get(
            "receiving_context_is_not_source"
        )
        is True,
        "no_source_replacement": selected_surface.get(
            "selected_source_body_surface_not_replaced"
        )
        is True,
        "no_source_validation_by_receiving_context": selected_surface.get(
            "selected_source_body_surface_not_validated_by_receiving_context"
        )
        is True,
        "no_source_invalidation_by_receiving_context": selected_surface.get(
            "selected_source_body_surface_not_invalidated_by_receiving_context"
        )
        is True,
        "latest_artifact_not_source": True,
        "carrier_possession_not_source": True,
        "registry_reference_not_source_replacement": True,
        "identity_preservation_is_not_reception": True,
        "identity_preservation_is_not_authorization": True,
        "identity_preservation_does_not_define_final_identity": True,
        "identity_preservation_does_not_inflate_selected_surface_to_whole_body": True,
    }


def _identity_preservation_scope(request: Mapping[str, Any]) -> dict[str, Any]:
    values, unsupported = _scope_values(request)
    return {
        "selected_identity_preservation_scope_values": values,
        "unsupported_identity_preservation_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "supported_identity_preservation_scope_values": list(
            SUPPORTED_IDENTITY_PRESERVATION_SCOPE
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "identity_preservation_is_not_reception": True,
        "identity_preservation_is_not_authorization": True,
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "closure_context_is_context_only": True,
        "terminal_summary_context_is_context_only": True,
        "request_declaration_is_context_only": True,
        "no_source_replacement": True,
        "no_source_validation_by_receiving_context": True,
        "no_source_invalidation_by_receiving_context": True,
    }


def _identity_preservation_statement(
    outcome: str,
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    preserved = outcome == OUTCOME_PRESERVED
    statement = {
        "source_body_reception_identity_preserved": preserved,
        "selected_reception_request_declaration_preserved": selected_declaration.get(
            "selected_reception_request_declaration_preserved"
        )
        is True,
        "selected_reception_request_declaration_recorded": selected_declaration.get(
            "selected_reception_request_declaration_recorded"
        )
        is True,
        "selected_reception_request_declaration_failed_check_count_zero": selected_declaration.get(
            "selected_reception_request_declaration_failed_check_count_zero"
        )
        is True,
        "selected_source_body_surface_preserved": selected_surface.get(
            "selected_source_body_surface_preserved"
        )
        is True,
        "selected_source_body_surface_remains_source": selected_surface.get(
            "selected_source_body_surface_remains_source"
        )
        is True,
        "selected_surface_is_not_whole_body_by_default": selected_surface.get(
            "selected_surface_is_not_whole_body_by_default"
        )
        is True,
        "receiving_context_preserved": receiving_context.get("receiving_context_preserved")
        is True,
        "receiving_context_remains_context_only": receiving_context.get(
            "receiving_context_remains_context_only"
        )
        is True,
        "receiving_context_is_not_source": receiving_context.get("receiving_context_is_not_source")
        is True,
        "receiving_context_is_not_authority": receiving_context.get(
            "receiving_context_is_not_authority"
        )
        is True,
        "receiving_context_is_not_current": receiving_context.get("receiving_context_is_not_current")
        is True,
        "reception_class_preserved": _present(_reception_class_value(request, selected_declaration)),
        "reception_purpose_preserved": _present(_reception_purpose_value(request, selected_declaration)),
        "reception_limits_preserved": _present(_reception_limits_value(request, selected_declaration)),
        "closure_context_is_context_only": _context_only(
            _closure_context_value(request, selected_declaration)
        ),
        "terminal_summary_context_is_context_only": _context_only(
            _terminal_summary_context_value(request, selected_declaration)
        ),
        "request_declaration_is_context_only": _request_declaration_context_only(
            request, selected_declaration
        ),
        "not_preserved_reason": request.get("not_preserved_basis"),
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


def _identity_preservation_non_meaning() -> dict[str, bool]:
    meanings = {
        "reception_recognized": True,
        "reception_authorized": True,
        "source_received": True,
        "final_source_body_identity_defined": True,
        "whole_body_identity_defined": True,
        "selected_source_body_surface_became_whole_body": True,
        "source_adopted": True,
        "source_validated": True,
        "source_invalidated": True,
        "source_replaced": True,
        "receiving_context_became_source": True,
        "receiving_context_became_authority": True,
        "receiving_context_became_current": True,
        "closure_artifact_became_source": True,
        "terminal_summary_became_source": True,
        "request_declaration_artifact_became_source": True,
        "latest_artifact_became_source": True,
        "carrier_possession_became_source": True,
        "registry_reference_replaced_source": True,
        "standing_created": True,
        "standing_propagated": True,
        "vessel_relation_created": True,
        "derivative_relation_created": True,
        "operation_permission_created": True,
        "public_readiness_created": True,
        "final_completion_claimed": True,
        "follow_on_work_authorized": True,
        "continuation_authorized": True,
        "publication_flow_opened": True,
    }
    meanings.update({f"does_not_mean_{key}": value for key, value in meanings.items()})
    return meanings


def _additional_basis_required(request: Mapping[str, Any], outcome: str) -> dict[str, Any]:
    additional = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    context = request.get("additional_basis_context")
    return {
        "additional_basis_required": additional,
        "additional_basis_context": _copy(context) if additional else {},
        "additional_basis_scheduled": False,
        "additional_basis_authorized": False,
        "additional_basis_executed": False,
        "missing_basis_does_not_recognize_reception": True,
        "missing_basis_does_not_authorize_reception": True,
        "missing_basis_does_not_receive_source": True,
        "missing_basis_does_not_replace_source": True,
        "missing_basis_does_not_validate_source": True,
        "missing_basis_does_not_invalidate_source": True,
        "missing_basis_does_not_define_final_identity": True,
        "missing_basis_does_not_create_currentness": True,
        "missing_basis_does_not_create_authority": True,
        "missing_basis_does_not_create_standing": True,
        "missing_basis_does_not_create_operation_permission": True,
        "missing_basis_does_not_create_public_readiness": True,
        "missing_basis_does_not_claim_final_completion": True,
        "missing_basis_does_not_authorize_follow_on_work": True,
    }


def _not_preserved_basis(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_preserved = outcome == OUTCOME_NOT_PRESERVED
    failed_checks = [
        _copy(dict(check))
        for check in checks
        if isinstance(check, Mapping) and check.get("passed") is not True
    ]
    return {
        "identity_not_preserved": not_preserved,
        "not_preserved_basis": _copy(request.get("not_preserved_basis"))
        if not_preserved
        else {},
        "failed_identity_preservation_checks": failed_checks if not_preserved else [],
        "not_preserved_does_not_mutate": True,
        "not_preserved_does_not_repair": True,
        "not_preserved_does_not_authorize": True,
        "not_preserved_does_not_receive_source": True,
        "not_preserved_does_not_replace_source": True,
        "not_preserved_does_not_validate_source": True,
        "not_preserved_does_not_invalidate_source": True,
        "not_preserved_does_not_create_currentness": True,
        "not_preserved_does_not_recognize_reception": True,
    }


def _what_remains_open() -> dict[str, bool]:
    return {
        "source_body_reception_identity_preservation_test": True,
        "source_body_reception_identity_preservation_live_artifact": True,
        "receiving_context_role_boundary": True,
        "reception_eligibility_admissibility_boundary": True,
        "non_capture_non_adoption_non_currentness_boundary": True,
        "source_body_reception_recognition_boundary": True,
        "source_body_reception_receipt_exhaustion_boundary": True,
        "source_body_reception_conformance_boundary": True,
        "source_body_reception_closure_boundary": True,
        "derivative_reception": True,
        "vessel_relation": True,
        "adoption": True,
        "authority_creation": True,
        "currentness_creation": True,
        "standing_creation": True,
        "operation_permission": True,
        "public_readiness": True,
        "final_completion": True,
        "follow_on_work": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def build_source_body_reception_identity_preservation_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("identity_preservation_checks")
    check_list = (
        list(checks)
        if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray))
        else []
    )
    passed_count = sum(
        1 for check in check_list if isinstance(check, Mapping) and check.get("passed") is True
    )
    failed_count = sum(
        1 for check in check_list if isinstance(check, Mapping) and check.get("passed") is not True
    )
    question = _mapping(result.get("declared_identity_preservation_question"))
    selected_declaration = _mapping(result.get("selected_reception_request_declaration"))
    selected_surface = _mapping(result.get("selected_source_body_surface"))
    receiving_context = _mapping(result.get("receiving_context"))
    basis = _mapping(result.get("identity_preservation_basis"))
    statement = _mapping(result.get("identity_preservation_statement"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "identity_preservation_request_id": question.get("identity_preservation_request_id"),
        "identity_preservation_question": question.get("identity_preservation_question"),
        "identity_preservation_intent": question.get("identity_preservation_intent"),
        "selected_reception_request_declaration_id": selected_declaration.get(
            "selected_reception_request_declaration_id"
        ),
        "selected_reception_request_declaration_outcome": selected_declaration.get(
            "selected_reception_request_declaration_outcome"
        ),
        "selected_source_body_surface_identifier": selected_surface.get(
            "selected_source_body_surface_identifier"
        ),
        "selected_source_body_surface_type": selected_surface.get(
            "selected_source_body_surface_type"
        ),
        "selected_source_body_surface_reference": _first(
            selected_surface.get("selected_source_body_surface_reference"),
            selected_surface.get("selected_source_body_surface_path"),
        ),
        "receiving_context_id": receiving_context.get("receiving_context_id"),
        "receiving_context_type": receiving_context.get("receiving_context_type"),
        "reception_class": basis.get("reception_class"),
        "reception_purpose": basis.get("reception_purpose"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "identity_preserved": outcome == OUTCOME_PRESERVED,
        "source_body_reception_identity_preserved": outcome == OUTCOME_PRESERVED,
        "not_preserved": outcome == OUTCOME_NOT_PRESERVED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_request_declaration_preserved": statement.get(
            "selected_reception_request_declaration_preserved"
        ),
        "selected_request_declaration_recorded": statement.get(
            "selected_reception_request_declaration_recorded"
        ),
        "selected_request_declaration_failed_check_count_zero": statement.get(
            "selected_reception_request_declaration_failed_check_count_zero"
        ),
        "selected_source_body_surface_preserved": statement.get(
            "selected_source_body_surface_preserved"
        ),
        "selected_source_body_surface_remains_source": statement.get(
            "selected_source_body_surface_remains_source"
        ),
        "selected_surface_is_not_whole_body_by_default": statement.get(
            "selected_surface_is_not_whole_body_by_default"
        ),
        "receiving_context_preserved": statement.get("receiving_context_preserved"),
        "receiving_context_remains_context_only": statement.get(
            "receiving_context_remains_context_only"
        ),
        "receiving_context_is_not_source": statement.get("receiving_context_is_not_source"),
        "receiving_context_is_not_authority": statement.get(
            "receiving_context_is_not_authority"
        ),
        "receiving_context_is_not_current": statement.get("receiving_context_is_not_current"),
        "reception_class_preserved": statement.get("reception_class_preserved"),
        "reception_purpose_preserved": statement.get("reception_purpose_preserved"),
        "reception_limits_preserved": statement.get("reception_limits_preserved"),
        "closure_context_only_where_supplied": statement.get("closure_context_is_context_only"),
        "terminal_summary_context_only_where_supplied": statement.get(
            "terminal_summary_context_is_context_only"
        ),
        "request_declaration_context_only": statement.get(
            "request_declaration_is_context_only"
        ),
        "no_source_replacement": non_claims.get("source_replaced") is False,
        "no_source_validation": non_claims.get("source_validated_by_receiving_context")
        is False,
        "no_source_invalidation": non_claims.get("source_invalidated_by_receiving_context")
        is False,
        "no_reception_recognized": non_claims.get("reception_recognized") is False,
        "no_reception_authorized": non_claims.get("reception_authorized") is False,
        "no_source_received": non_claims.get("source_received") is False,
        "no_final_source_body_identity_defined": non_claims.get(
            "final_source_body_identity_defined"
        )
        is False,
        "no_whole_body_identity_inflation": non_claims.get(
            "selected_surface_inflated_to_whole_body"
        )
        is False,
        "no_adoption": non_claims.get("adoption_created") is False,
        "no_authority": non_claims.get("authority_created") is False,
        "no_currentness": non_claims.get("currentness_created") is False,
        "no_standing": non_claims.get("standing_created") is False,
        "no_vessel_relation": non_claims.get("vessel_relation_created") is False,
        "no_derivative_relation": non_claims.get("derivative_relation_created") is False,
        "no_operation_permission": non_claims.get("operation_permission_created") is False,
        "no_public_readiness": (
            non_claims.get("public_launch_readiness_created") is False
        ),
        "no_final_completion": non_claims.get("final_completion_claimed") is False,
        "no_follow_on_work": non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": {key: non_claims.get(key) for key in REQUIRED_NON_CLAIMS},
    }


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
    block_code: str | None,
    block_reason: str | None,
    selected_declaration: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> dict[str, Any]:
    result = {
        "source_body_reception_identity_metadata": _metadata(request, selected_declaration),
        "declared_identity_preservation_question": _declared_question_section(
            request, selected_declaration
        ),
        "selected_reception_request_declaration": _copy(dict(selected_declaration)),
        "selected_source_body_surface": _copy(dict(selected_surface)),
        "receiving_context": _copy(dict(receiving_context)),
        "identity_preservation_basis": _identity_preservation_basis(
            request, selected_declaration, selected_surface, receiving_context
        ),
        "identity_preservation_scope": _identity_preservation_scope(request),
        "identity_preservation_checks": [_copy(dict(check)) for check in checks],
        "identity_preservation_statement": _identity_preservation_statement(
            outcome, selected_declaration, selected_surface, receiving_context, request
        ),
        "identity_preservation_non_meaning": _identity_preservation_non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "not_preserved_basis": _not_preserved_basis(request, outcome, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["source_body_reception_identity_summary"] = (
        build_source_body_reception_identity_preservation_summary(result)
    )
    return result


def _minimal_blocked_result(
    code: str,
    reason: str | None = None,
    *,
    request_path: str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {}
    if request_path is not None:
        request["declared_identity_preservation_request_path"] = request_path
    selected_declaration = _selected_declaration_section(request, {}, None, None, None)
    selected_surface = _selected_source_surface_section(request, selected_declaration)
    receiving_context = _receiving_context_section(request, selected_declaration)
    checks = [
        _check(
            code.replace("_", " ").lower(),
            False,
            "bounded source-body reception identity preservation request",
            reason or code,
            code,
        )
    ]
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        code,
        _block_reason(code, reason),
        selected_declaration,
        selected_surface,
        receiving_context,
    )


def resolve_source_body_reception_identity_preservation_boundary(
    declared_identity_preservation_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_identity_preservation_request is None:
        return _minimal_blocked_result("IDENTITY_PRESERVATION_QUESTION_UNDECLARED")
    if not isinstance(declared_identity_preservation_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED"
        )

    request = _copy(dict(declared_identity_preservation_request))
    declaration_payload, load_code, load_detail, declaration_path = _load_selected_declaration(request)
    selected_declaration = _selected_declaration_section(
        request,
        declaration_payload,
        load_code,
        load_detail,
        declaration_path,
    )
    selected_surface = _selected_source_surface_section(request, selected_declaration)
    receiving_context = _receiving_context_section(request, selected_declaration)
    checks = _build_checks(request, selected_declaration, selected_surface, receiving_context)
    block_code = _first_failed_code(checks)
    requested_outcome = request.get(
        "requested_identity_preservation_outcome", OUTCOME_PRESERVED
    )
    intent = request.get("identity_preservation_intent", INTENT_RECORD)
    if requested_outcome not in OUTCOME_FAMILY:
        block_code = block_code or "DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED"

    if block_code:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_PRESERVED
    elif requested_outcome == OUTCOME_NOT_PRESERVED:
        outcome = OUTCOME_NOT_PRESERVED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_PRESERVED

    return _build_result(
        request,
        outcome,
        checks,
        block_code if outcome == OUTCOME_BLOCKED else None,
        _block_reason(block_code, request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED
        else None,
        selected_declaration,
        selected_surface,
        receiving_context,
    )


def resolve_source_body_reception_identity_preservation_boundary_from_path(
    declared_identity_preservation_request_path: Path | str,
) -> dict:
    payload, error, detail = _read_json_object(declared_identity_preservation_request_path)
    if error == "unreadable":
        return _minimal_blocked_result(
            "DECLARED_IDENTITY_PRESERVATION_REQUEST_UNREADABLE",
            detail,
            request_path=str(declared_identity_preservation_request_path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_IDENTITY_PRESERVATION_REQUEST_MALFORMED",
            detail,
            request_path=str(declared_identity_preservation_request_path),
        )
    assert payload is not None
    request = _copy(payload)
    request["declared_identity_preservation_request_path"] = str(
        declared_identity_preservation_request_path
    )
    return resolve_source_body_reception_identity_preservation_boundary(request)


def _default_filename(result: Mapping[str, Any]) -> str:
    request_id = _first(
        _get(
            result,
            (
                "declared_identity_preservation_question",
                "identity_preservation_request_id",
            ),
        ),
        _get(
            result,
            (
                "selected_reception_request_declaration",
                "selected_reception_request_declaration_id",
            ),
        ),
        _get(
            result,
            (
                "source_body_reception_identity_metadata",
                "source_body_reception_identity_result_id",
            ),
        ),
        RESULT_ID_PREFIX,
    )
    return (
        f"{_safe_component(request_id)}"
        "__source_body_reception_identity_preservation_result.json"
    )


def _unique_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_source_body_reception_identity_preservation_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionIdentityPreservationBoundaryError(
            "Result must be a mapping before it can be written."
        )
    filename = _default_filename(result)
    if output_path is None:
        target = SOURCE_BODY_RECEPTION_IDENTITY_PRESERVATION_ROOT / filename
    else:
        supplied = Path(output_path)
        target = supplied / filename if supplied.suffix == "" else supplied
    target = _unique_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return target


def build_declared_source_body_reception_identity_preservation_request(
    identity_preservation_request_id: str,
    identity_preservation_question: str,
    selected_reception_request_declaration: Mapping[str, Any] | str,
    identity_preservation_basis: Mapping[str, Any] | str,
    identity_preservation_scope: Sequence[str] | Mapping[str, Any],
    identity_preservation_intent: str = INTENT_RECORD,
    *,
    selected_reception_request_declaration_path: str | None = None,
    selected_reception_request_declaration_id: str | None = None,
    selected_reception_request_declaration_outcome: str | None = None,
    requested_identity_preservation_outcome: str = OUTCOME_PRESERVED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_preserved_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    declaration = (
        _copy(dict(selected_reception_request_declaration))
        if isinstance(selected_reception_request_declaration, Mapping)
        else {"selected_reception_request_declaration_reference": selected_reception_request_declaration}
    )
    declaration_section = _selected_declaration_section(
        {
            "selected_reception_request_declaration": declaration,
            "selected_reception_request_declaration_path": selected_reception_request_declaration_path,
            "selected_reception_request_declaration_id": selected_reception_request_declaration_id,
            "selected_reception_request_declaration_outcome": (
                selected_reception_request_declaration_outcome
            ),
        },
        declaration,
        None,
        None,
        selected_reception_request_declaration_path,
    )
    selected_surface = _selected_source_surface_section({}, declaration_section)
    receiving_context = _receiving_context_section({}, declaration_section)
    return {
        "identity_preservation_request_id": identity_preservation_request_id,
        "identity_preservation_question": identity_preservation_question,
        "identity_preservation_intent": identity_preservation_intent,
        "selected_reception_request_declaration": _copy(selected_reception_request_declaration),
        "selected_reception_request_declaration_path": selected_reception_request_declaration_path,
        "selected_reception_request_declaration_id": _first(
            selected_reception_request_declaration_id,
            declaration_section.get("selected_reception_request_declaration_id"),
        ),
        "selected_reception_request_declaration_outcome": _first(
            selected_reception_request_declaration_outcome,
            declaration_section.get("selected_reception_request_declaration_outcome"),
        ),
        "selected_source_body_surface": _copy(
            selected_surface.get("selected_source_body_surface")
        ),
        "selected_source_body_surface_identifier": selected_surface.get(
            "selected_source_body_surface_identifier"
        ),
        "selected_source_body_surface_type": selected_surface.get(
            "selected_source_body_surface_type"
        ),
        "selected_source_body_surface_path": selected_surface.get(
            "selected_source_body_surface_path"
        ),
        "selected_source_body_surface_reference": selected_surface.get(
            "selected_source_body_surface_reference"
        ),
        "source_body_identity_basis": _copy(selected_surface.get("source_body_identity_basis")),
        "source_body_lineage_basis": _copy(selected_surface.get("source_body_lineage_basis")),
        "receiving_context": _copy(receiving_context.get("receiving_context")),
        "receiving_context_id": receiving_context.get("receiving_context_id"),
        "receiving_context_type": receiving_context.get("receiving_context_type"),
        "reception_class": _reception_class_value({}, declaration_section),
        "reception_purpose": _copy(_reception_purpose_value({}, declaration_section)),
        "reception_limits": _copy(_reception_limits_value({}, declaration_section)),
        "distributed_operation_closure_context": _get(
            declaration,
            ("selected_source_body_surface", "distributed_operation_closure_context"),
        ),
        "terminal_summary_context": _get(
            declaration,
            ("selected_source_body_surface", "terminal_summary_context"),
        ),
        "request_declaration_context": {
            "request_declaration_context_only": True,
            "request_declaration_does_not_replace_source": True,
        },
        "identity_preservation_basis": _copy(identity_preservation_basis),
        "identity_preservation_scope": _copy(identity_preservation_scope),
        "requested_identity_preservation_outcome": requested_identity_preservation_outcome,
        "additional_basis_context": _copy(additional_basis_context),
        "not_preserved_basis": _copy(not_preserved_basis),
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
