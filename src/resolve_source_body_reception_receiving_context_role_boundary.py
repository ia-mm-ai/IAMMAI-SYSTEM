"""Resolve source-body reception receiving-context role boundary.

This resolver records one bounded role for the declared receiving context after
source-body reception identity preservation only. It does not recognize or
authorize reception, receive source, replace source, validate or invalidate
source, make receiving context source, authority, current, receiver, adopter,
validator, invalidator, operator, vessel, derivative, governance, permission,
publication flow, or follow-on authority.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class SourceBodyReceptionReceivingContextRoleBoundaryError(Exception):
    """Raised for hard source-body reception receiving-context role failures."""


RESOLVER_MODULE = "resolve_source_body_reception_receiving_context_role_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "source_body_reception_receiving_context_role_result"
RESULT_ID_PREFIX = "source_body_reception_receiving_context_role"

SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_receiving_context_role_boundary"
)

IDENTITY_PRESERVATION_OUTCOME = "SOURCE_BODY_RECEPTION_IDENTITY_PRESERVED"

OUTCOME_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"
OUTCOME_NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES = (
    "REQUEST_DECLARATION_CONTEXT",
    "REFERENCE_REVIEW_CONTEXT",
    "INSPECTION_REVIEW_CONTEXT",
    "CARRIER_CONTEXT_REVIEW",
)

UNSUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES = (
    "SOURCE_RECEIVER",
    "SOURCE_ADOPTER",
    "SOURCE_VALIDATOR",
    "SOURCE_INVALIDATOR",
    "SOURCE_AUTHORITY",
    "CURRENT_CONTEXT",
    "OPERATION_OPERATOR",
    "VESSEL_CONTEXT",
    "DERIVATIVE_CONTEXT",
    "PUBLICATION_CONTEXT",
)

SUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE = (
    "RECEIVING_CONTEXT_REMAINS_CONTEXT_ONLY",
    "ROLE_IS_NOT_RECEPTION",
    "ROLE_IS_NOT_AUTHORIZATION",
    "ROLE_IS_NOT_SOURCE_RECEIPT",
    "ROLE_IS_NOT_SOURCE_AUTHORITY",
    "ROLE_IS_NOT_CURRENTNESS",
    "ROLE_IS_NOT_ADOPTION",
    "ROLE_IS_NOT_VALIDATION",
    "ROLE_IS_NOT_INVALIDATION",
    "ROLE_IS_NOT_OPERATION_PERMISSION",
    "ROLE_IS_NOT_VESSEL_RELATION",
    "ROLE_IS_NOT_DERIVATIVE_RELATION",
    "ROLE_IS_NOT_PUBLICATION_FLOW",
    "SOURCE_BODY_SURFACE_REMAINS_SOURCE",
)

REQUIRED_NON_CLAIMS = (
    "reception_recognized",
    "reception_authorized",
    "source_received",
    "receiving_context_governance_created",
    "receiving_context_became_source",
    "receiving_context_became_authority",
    "receiving_context_became_current",
    "receiving_context_became_receiver",
    "receiving_context_became_adopter",
    "receiving_context_became_validator",
    "receiving_context_became_invalidator",
    "receiving_context_became_operator",
    "receiving_context_became_vessel",
    "receiving_context_became_derivative",
    "source_validated_by_receiving_context",
    "source_invalidated_by_receiving_context",
    "source_replaced",
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
    "RECEIVING_CONTEXT_ROLE_RECOGNIZES_RECEPTION": (
        "reception_recognized",
        "source_body_reception_recognized",
        "receiving_context_role_recognizes_reception",
        "role_recognizes_reception",
    ),
    "RECEIVING_CONTEXT_ROLE_AUTHORIZES_RECEPTION": (
        "reception_authorized",
        "source_body_reception_authorized",
        "receiving_context_role_authorizes_reception",
        "role_authorizes_reception",
    ),
    "RECEIVING_CONTEXT_ROLE_RECEIVES_SOURCE": (
        "source_received",
        "source_body_received",
        "receiving_context_role_receives_source",
        "role_receives_source",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_GOVERNANCE": (
        "receiving_context_governance_created",
        "receiving_context_governance",
        "governance_created",
        "role_creates_governance",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_SOURCE": (
        "receiving_context_became_source",
        "receiving_context_treated_as_source",
        "receiving_context_is_source",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_AUTHORITY": (
        "receiving_context_became_authority",
        "receiving_context_treated_as_authority",
        "receiving_context_is_authority",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_CURRENT": (
        "receiving_context_became_current",
        "receiving_context_treated_as_current",
        "receiving_context_is_current",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_RECEIVER": (
        "receiving_context_became_receiver",
        "receiving_context_treated_as_receiver",
        "receiving_context_is_receiver",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_ADOPTER": (
        "receiving_context_became_adopter",
        "receiving_context_treated_as_adopter",
        "receiving_context_is_adopter",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VALIDATOR": (
        "receiving_context_became_validator",
        "receiving_context_treated_as_validator",
        "receiving_context_is_validator",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_INVALIDATOR": (
        "receiving_context_became_invalidator",
        "receiving_context_treated_as_invalidator",
        "receiving_context_is_invalidator",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_OPERATOR": (
        "receiving_context_became_operator",
        "receiving_context_treated_as_operator",
        "receiving_context_is_operator",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VESSEL": (
        "receiving_context_became_vessel",
        "receiving_context_treated_as_vessel",
        "receiving_context_is_vessel",
    ),
    "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_DERIVATIVE": (
        "receiving_context_became_derivative",
        "receiving_context_treated_as_derivative",
        "receiving_context_is_derivative",
    ),
    "RECEIVING_CONTEXT_ROLE_VALIDATES_SOURCE": (
        "source_validated_by_receiving_context",
        "source_validated",
        "receiving_context_validates_source",
        "role_validates_source",
    ),
    "RECEIVING_CONTEXT_ROLE_INVALIDATES_SOURCE": (
        "source_invalidated_by_receiving_context",
        "source_invalidated",
        "receiving_context_invalidates_source",
        "role_invalidates_source",
    ),
    "RECEIVING_CONTEXT_ROLE_REPLACES_SOURCE": (
        "source_replaced",
        "source_body_replaced",
        "source_replacement_created",
        "role_replaces_source",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_ADOPTION": (
        "adoption_created",
        "source_adopted",
        "role_creates_adoption",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_AUTHORITY": (
        "authority_created",
        "source_authority_created",
        "role_creates_authority",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_CURRENTNESS": (
        "currentness_created",
        "source_currentness_created",
        "role_creates_currentness",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_STANDING": (
        "standing_created",
        "source_standing_created",
        "role_creates_standing",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_STANDING_PROPAGATION": (
        "standing_propagated",
        "standing_propagation_created",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_VESSEL_RELATION": (
        "vessel_relation_created",
        "vessel_relation_authorized",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_DERIVATIVE_RELATION": (
        "derivative_relation_created",
        "derivative_reception_created",
        "derivative_relation_authorized",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_OPERATION_PERMISSION": (
        "operation_permission_created",
        "operation_authorized",
        "permission_created",
        "role_creates_operation_permission",
    ),
    "RECEIVING_CONTEXT_ROLE_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
        "public_launch_ready",
    ),
    "RECEIVING_CONTEXT_ROLE_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_system_completion_claimed",
        "final_completion_created",
    ),
    "RECEIVING_CONTEXT_ROLE_AUTHORIZES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "successor_scheduled",
    ),
    "RECEIVING_CONTEXT_ROLE_AUTHORIZES_CONTINUATION": (
        "continuation_authorized",
        "continuation_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "RECEIVING_CONTEXT_ROLE_OPENS_PUBLICATION_FLOW": (
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
    "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED": (
        "Declared receiving-context role request is malformed."
    ),
    "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_UNREADABLE": (
        "Declared receiving-context role request path is unreadable."
    ),
    "RECEIVING_CONTEXT_ROLE_QUESTION_UNDECLARED": (
        "Receiving-context role question is undeclared."
    ),
    "RECEIVING_CONTEXT_ROLE_INTENT_UNSUPPORTED": (
        "Receiving-context role intent is unsupported."
    ),
    "RECEIVING_CONTEXT_ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Receiving-context role review was explicitly blocked by request intent."
    ),
    "IDENTITY_PRESERVATION_RESULT_MISSING": (
        "Selected identity preservation result is missing."
    ),
    "IDENTITY_PRESERVATION_RESULT_UNREADABLE": (
        "Selected identity preservation result path is unreadable."
    ),
    "IDENTITY_PRESERVATION_RESULT_MALFORMED": (
        "Selected identity preservation result is malformed."
    ),
    "IDENTITY_PRESERVATION_RESULT_OUTCOME_MISSING": (
        "Selected identity preservation outcome is missing."
    ),
    "IDENTITY_PRESERVATION_RESULT_NOT_PRESERVED": (
        "Selected identity preservation outcome is not preserved."
    ),
    "IDENTITY_PRESERVATION_RESULT_HAS_FAILED_CHECKS": (
        "Selected identity preservation result has failed checks."
    ),
    "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING": (
        "Selected reception request declaration result is missing."
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
    "IDENTITY_PRESERVATION_BASIS_MISSING": (
        "Identity preservation basis is missing."
    ),
    "RECEIVING_CONTEXT_ROLE_MISSING": "Receiving-context role is missing.",
    "RECEIVING_CONTEXT_ROLE_CLASS_MISSING": (
        "Receiving-context role class is missing."
    ),
    "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_CLASS": (
        "Receiving-context role class is unsupported."
    ),
    "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE": (
        "Receiving-context role scope is missing or unsupported."
    ),
    "RECEIVING_CONTEXT_ROLE_LIMITS_MISSING": (
        "Receiving-context role limits are missing."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required receiving-context role non-claim is missing or true."
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
        "reception_recognized",
        "reception_authorized",
        "source_received",
        "receiving_context_governance_created",
        "receiving_context_became_source",
        "receiving_context_became_authority",
        "receiving_context_became_current",
        "receiving_context_became_receiver",
        "receiving_context_became_adopter",
        "receiving_context_became_validator",
        "receiving_context_became_invalidator",
        "receiving_context_became_operator",
        "receiving_context_became_vessel",
        "receiving_context_became_derivative",
        "source_validated_by_receiving_context",
        "source_invalidated_by_receiving_context",
        "source_replaced",
        "operation_permission_created",
        "publication_flow_opened",
    )
    return not _any_claim_true(value, forbidden)


def _failed_check_count(result: Mapping[str, Any], checks_key: str, summary_key: str) -> int | None:
    summary_count = _get(result, (summary_key, "failed_check_count"))
    if isinstance(summary_count, int):
        return summary_count
    checks = result.get(checks_key)
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _load_selected_identity_result(
    request: Mapping[str, Any],
) -> tuple[Any, str | None, str | None, str | None]:
    path = request.get("selected_identity_preservation_result_path")
    if _present(path):
        payload, error, detail = _read_json_object(str(path))
        if error == "unreadable":
            return {}, "IDENTITY_PRESERVATION_RESULT_UNREADABLE", detail, str(path)
        if error == "malformed":
            return {}, "IDENTITY_PRESERVATION_RESULT_MALFORMED", detail, str(path)
        assert payload is not None
        return payload, None, None, str(path)
    raw = request.get("selected_identity_preservation_result")
    if isinstance(raw, Mapping):
        return _copy(dict(raw)), None, None, None
    if isinstance(raw, str) and raw:
        return {
            "selected_identity_preservation_result_id": raw,
            "selected_identity_preservation_result_reference": raw,
        }, None, None, None
    if _present(raw):
        return {}, "IDENTITY_PRESERVATION_RESULT_MALFORMED", None, None
    return {}, None, None, None


def _identity_result_section(
    request: Mapping[str, Any],
    identity_result: Any,
    load_code: str | None,
    load_detail: str | None,
    path: str | None,
) -> dict[str, Any]:
    result_map = _mapping(identity_result)
    metadata = _mapping(result_map.get("source_body_reception_identity_metadata"))
    summary = _mapping(result_map.get("source_body_reception_identity_summary"))
    statement = _mapping(result_map.get("identity_preservation_statement"))
    non_claims = _mapping(result_map.get("non_claims"))
    question = _mapping(result_map.get("declared_identity_preservation_question"))
    result_id = _first(
        request.get("selected_identity_preservation_result_id"),
        metadata.get("source_body_reception_identity_result_id"),
        summary.get("source_body_reception_identity_result_id"),
        question.get("identity_preservation_request_id"),
        result_map.get("selected_identity_preservation_result_id"),
    )
    outcome = _first(
        request.get("selected_identity_preservation_result_outcome"),
        request.get("expected_selected_identity_preservation_outcome"),
        result_map.get("outcome"),
        summary.get("outcome"),
    )
    failed_count = _first(
        request.get("selected_identity_preservation_failed_check_count"),
        _failed_check_count(
            result_map,
            "identity_preservation_checks",
            "source_body_reception_identity_summary",
        ),
    )
    result_present = _present(request.get("selected_identity_preservation_result")) or _present(path)
    sections = (result_map, statement, non_claims, summary)
    selected_declaration = _first(
        request.get("selected_reception_request_declaration_result"),
        result_map.get("selected_reception_request_declaration"),
    )
    return {
        "selected_identity_preservation_result": _copy(identity_result),
        "selected_identity_preservation_result_path": path,
        "selected_identity_preservation_result_id": result_id,
        "selected_identity_preservation_result_outcome": outcome,
        "expected_selected_identity_preservation_outcome": request.get(
            "expected_selected_identity_preservation_outcome",
            IDENTITY_PRESERVATION_OUTCOME,
        ),
        "selected_identity_preservation_result_preserved": result_present
        and load_code is None,
        "selected_identity_preservation_result_recorded": outcome == IDENTITY_PRESERVATION_OUTCOME,
        "selected_identity_preservation_result_failed_check_count": failed_count,
        "selected_identity_preservation_result_failed_check_count_zero": failed_count == 0,
        "selected_identity_preservation_result_load_block_code": load_code,
        "selected_identity_preservation_result_load_block_reason": load_detail,
        "selected_reception_request_declaration_result": _copy(selected_declaration),
        "selected_reception_request_declaration_result_preserved": _present(
            selected_declaration
        ),
        "selected_source_body_surface_preserved_by_identity": _first(
            statement.get("selected_source_body_surface_preserved"),
            summary.get("selected_source_body_surface_preserved"),
        ),
        "selected_source_body_surface_remains_source_by_identity": _first(
            statement.get("selected_source_body_surface_remains_source"),
            summary.get("selected_source_body_surface_remains_source"),
        ),
        "selected_surface_is_not_whole_body_by_default_by_identity": _first(
            statement.get("selected_surface_is_not_whole_body_by_default"),
            summary.get("selected_surface_is_not_whole_body_by_default"),
        ),
        "receiving_context_preserved_by_identity": _first(
            statement.get("receiving_context_preserved"),
            summary.get("receiving_context_preserved"),
        ),
        "receiving_context_remains_context_only_by_identity": _first(
            statement.get("receiving_context_remains_context_only"),
            summary.get("receiving_context_remains_context_only"),
        ),
        "receiving_context_is_not_source_by_identity": _first(
            statement.get("receiving_context_is_not_source"),
            summary.get("receiving_context_is_not_source"),
        ),
        "receiving_context_is_not_authority_by_identity": _first(
            statement.get("receiving_context_is_not_authority"),
            summary.get("receiving_context_is_not_authority"),
        ),
        "receiving_context_is_not_current_by_identity": _first(
            statement.get("receiving_context_is_not_current"),
            summary.get("receiving_context_is_not_current"),
        ),
        "reception_class_preserved_by_identity": _first(
            statement.get("reception_class_preserved"),
            summary.get("reception_class_preserved"),
        ),
        "reception_purpose_preserved_by_identity": _first(
            statement.get("reception_purpose_preserved"),
            summary.get("reception_purpose_preserved"),
        ),
        "reception_limits_preserved_by_identity": _first(
            statement.get("reception_limits_preserved"),
            summary.get("reception_limits_preserved"),
        ),
        "identity_preservation_did_not_recognize_reception": not any(
            _any_claim_true(item, ("reception_recognized",)) for item in sections
        ),
        "identity_preservation_did_not_authorize_reception": not any(
            _any_claim_true(item, ("reception_authorized",)) for item in sections
        ),
        "identity_preservation_did_not_receive_source": not any(
            _any_claim_true(item, ("source_received",)) for item in sections
        ),
        "identity_preservation_did_not_define_final_identity": not any(
            _any_claim_true(
                item,
                (
                    "final_source_body_identity_defined",
                    "selected_surface_inflated_to_whole_body",
                ),
            )
            for item in sections
        ),
        "identity_preservation_did_not_mutate_replay_or_merge": not any(
            _any_claim_true(
                item,
                ("mutation_performed", "replay_performed", "merge_performed"),
            )
            for item in sections
        ),
    }


def _identity_result_map(section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(section.get("selected_identity_preservation_result"))


def _identity_basis_value(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
) -> Any:
    result = _identity_result_map(identity_section)
    return _first(request.get("identity_preservation_basis"), result.get("identity_preservation_basis"))


def _selected_source_surface_section(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
) -> dict[str, Any]:
    identity_result = _identity_result_map(identity_section)
    identity_surface = _mapping(identity_result.get("selected_source_body_surface"))
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        identity_surface.get("selected_source_body_surface"),
        identity_surface if identity_surface else None,
    )
    payload = _as_payload(
        raw_surface,
        "selected_source_body_surface_reference",
        "selected_source_body_surface_identifier",
    )
    identifier = _first(
        request.get("selected_source_body_surface_identifier"),
        _first_key(
            payload,
            (
                "selected_source_body_surface_identifier",
                "source_body_surface_identifier",
                "surface_id",
                "id",
            ),
        ),
        identity_surface.get("selected_source_body_surface_identifier"),
    )
    surface_type = _first(
        request.get("selected_source_body_surface_type"),
        _first_key(
            payload,
            (
                "selected_source_body_surface_type",
                "source_body_surface_type",
                "surface_type",
                "type",
            ),
        ),
        identity_surface.get("selected_source_body_surface_type"),
        "SOURCE_BODY_SURFACE_REFERENCE" if isinstance(raw_surface, str) else None,
    )
    surface_path = _first(
        request.get("selected_source_body_surface_path"),
        _first_key(
            payload,
            ("selected_source_body_surface_path", "source_body_surface_path", "path"),
        ),
        identity_surface.get("selected_source_body_surface_path"),
    )
    surface_reference = _first(
        request.get("selected_source_body_surface_reference"),
        _first_key(
            payload,
            (
                "selected_source_body_surface_reference",
                "source_body_surface_reference",
                "reference",
            ),
        ),
        identity_surface.get("selected_source_body_surface_reference"),
        raw_surface if isinstance(raw_surface, str) else None,
    )
    identity_basis = _first(
        request.get("source_body_identity_basis"),
        _first_key(payload, ("source_body_identity_basis", "identity_basis")),
        identity_surface.get("source_body_identity_basis"),
    )
    lineage_basis = _first(
        request.get("source_body_lineage_basis"),
        _first_key(payload, ("source_body_lineage_basis", "lineage_basis")),
        identity_surface.get("source_body_lineage_basis"),
    )
    sections = (
        request,
        payload,
        identity_surface,
        _mapping(request.get("receiving_context_role_basis")),
        _mapping(request.get("declared_non_claims")),
    )
    remains_source = not any(
        item.get("selected_source_body_surface_remains_source") is False
        or item.get("source_body_surface_remains_source") is False
        or _any_claim_true(
            item,
            (
                "source_received",
                "source_replaced",
                "source_validated_by_receiving_context",
                "source_invalidated_by_receiving_context",
                "adoption_created",
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
        "selected_source_body_surface_remains_source": remains_source,
        "selected_surface_is_not_whole_body_by_default": not_whole_body,
        "selected_source_body_surface_not_received": not any(
            _any_claim_true(item, ("source_received",)) for item in sections
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
    }


def _receiving_context_section(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
) -> dict[str, Any]:
    identity_result = _identity_result_map(identity_section)
    identity_context = _mapping(identity_result.get("receiving_context"))
    raw_context = _first(
        request.get("receiving_context"),
        identity_context.get("receiving_context"),
        identity_context if identity_context else None,
    )
    payload = _as_payload(raw_context, "receiving_context_reference", "receiving_context_id")
    context_id = _first(
        request.get("receiving_context_id"),
        _first_key(
            payload,
            (
                "receiving_context_id",
                "receiving_context_name",
                "receiving_context_reference",
                "context_id",
                "id",
                "name",
            ),
        ),
        identity_context.get("receiving_context_id"),
        raw_context if isinstance(raw_context, str) else None,
    )
    context_type = _first(
        request.get("receiving_context_type"),
        _first_key(payload, ("receiving_context_type", "context_type", "type")),
        identity_context.get("receiving_context_type"),
        "RECEIVING_CONTEXT" if isinstance(raw_context, str) else None,
    )
    sections = (
        request,
        payload,
        identity_context,
        _mapping(request.get("receiving_context_role_basis")),
        _mapping(request.get("declared_non_claims")),
    )
    return {
        "receiving_context": payload if payload else _copy(raw_context),
        "receiving_context_id": context_id,
        "receiving_context_name": _first_key(payload, ("receiving_context_name", "name")),
        "receiving_context_reference": _first_key(
            payload, ("receiving_context_reference", "reference")
        ),
        "receiving_context_type": context_type,
        "receiving_context_preserved": _present(raw_context) or _present(context_id),
        "receiving_context_remains_context_only": _context_only(payload)
        and not any(
            item.get("receiving_context_remains_context_only") is False
            or _any_claim_true(
                item,
                (
                    "receiving_context_became_source",
                    "receiving_context_became_authority",
                    "receiving_context_became_current",
                    "receiving_context_became_receiver",
                    "receiving_context_became_adopter",
                    "receiving_context_became_validator",
                    "receiving_context_became_invalidator",
                    "receiving_context_became_operator",
                    "receiving_context_became_vessel",
                    "receiving_context_became_derivative",
                    "receiving_context_governance_created",
                    "operation_permission_created",
                    "publication_flow_opened",
                ),
            )
            for item in sections
        ),
        "receiving_context_is_not_source": not any(
            _any_claim_true(item, ("receiving_context_became_source",))
            for item in sections
        ),
        "receiving_context_is_not_authority": not any(
            _any_claim_true(item, ("receiving_context_became_authority",))
            for item in sections
        ),
        "receiving_context_is_not_current": not any(
            _any_claim_true(item, ("receiving_context_became_current",))
            for item in sections
        ),
        "receiving_context_is_not_receiver": not any(
            _any_claim_true(item, ("receiving_context_became_receiver",))
            for item in sections
        ),
        "receiving_context_is_not_adopter": not any(
            _any_claim_true(item, ("receiving_context_became_adopter",))
            for item in sections
        ),
        "receiving_context_is_not_validator": not any(
            _any_claim_true(item, ("receiving_context_became_validator",))
            for item in sections
        ),
        "receiving_context_is_not_invalidator": not any(
            _any_claim_true(item, ("receiving_context_became_invalidator",))
            for item in sections
        ),
        "receiving_context_is_not_operator": not any(
            _any_claim_true(item, ("receiving_context_became_operator",))
            for item in sections
        ),
        "receiving_context_is_not_vessel": not any(
            _any_claim_true(item, ("receiving_context_became_vessel",))
            for item in sections
        ),
        "receiving_context_is_not_derivative": not any(
            _any_claim_true(item, ("receiving_context_became_derivative",))
            for item in sections
        ),
        "receiving_context_did_not_validate_source": not any(
            _any_claim_true(item, ("source_validated_by_receiving_context",))
            for item in sections
        ),
        "receiving_context_did_not_invalidate_source": not any(
            _any_claim_true(item, ("source_invalidated_by_receiving_context",))
            for item in sections
        ),
        "receiving_context_did_not_create_governance": not any(
            _any_claim_true(item, ("receiving_context_governance_created",))
            for item in sections
        ),
        "receiving_context_did_not_create_operation_permission": not any(
            _any_claim_true(item, ("operation_permission_created",))
            for item in sections
        ),
        "receiving_context_did_not_open_publication_flow": not any(
            _any_claim_true(item, ("publication_flow_opened",))
            for item in sections
        ),
    }


def _reception_class_value(request: Mapping[str, Any], identity_section: Mapping[str, Any]) -> Any:
    identity_result = _identity_result_map(identity_section)
    basis = _mapping(identity_result.get("identity_preservation_basis"))
    summary = _mapping(identity_result.get("source_body_reception_identity_summary"))
    return _first(request.get("reception_class"), basis.get("reception_class"), summary.get("reception_class"))


def _reception_purpose_value(request: Mapping[str, Any], identity_section: Mapping[str, Any]) -> Any:
    identity_result = _identity_result_map(identity_section)
    basis = _mapping(identity_result.get("identity_preservation_basis"))
    summary = _mapping(identity_result.get("source_body_reception_identity_summary"))
    return _first(request.get("reception_purpose"), basis.get("reception_purpose"), summary.get("reception_purpose"))


def _reception_limits_value(request: Mapping[str, Any], identity_section: Mapping[str, Any]) -> Any:
    identity_result = _identity_result_map(identity_section)
    basis = _mapping(identity_result.get("identity_preservation_basis"))
    return _first(request.get("reception_limits"), basis.get("reception_limits"))


def _role_basis_payload(request: Mapping[str, Any]) -> dict[str, Any]:
    raw = request.get("receiving_context_role_basis")
    if isinstance(raw, Mapping):
        return _copy(dict(raw))
    if isinstance(raw, str) and raw:
        return {
            "receiving_context_role_basis_id": raw,
            "receiving_context_role_basis_reference": raw,
        }
    return {}


def _receiving_context_role_section(request: Mapping[str, Any]) -> dict[str, Any]:
    basis = _role_basis_payload(request)
    role_payload = _as_payload(
        _first(request.get("declared_receiving_context_role"), basis.get("declared_receiving_context_role")),
        "declared_receiving_context_role_reference",
        "declared_receiving_context_role_id",
    )
    role_class = _first(
        request.get("receiving_context_role_class"),
        basis.get("receiving_context_role_class"),
        _first_key(role_payload, ("receiving_context_role_class", "role_class")),
    )
    role_limits = _first(
        request.get("receiving_context_role_limits"),
        basis.get("receiving_context_role_limits"),
        _first_key(role_payload, ("receiving_context_role_limits", "role_limits")),
    )
    return {
        "declared_receiving_context_role": role_payload
        if role_payload
        else _copy(_first(request.get("declared_receiving_context_role"), basis.get("declared_receiving_context_role"))),
        "receiving_context_role_class": role_class,
        "receiving_context_role_limits": _copy(role_limits),
        "receiving_context_role_class_supported": role_class in SUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES,
        "receiving_context_role_class_unsupported": role_class
        in UNSUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES
        or (_present(role_class) and role_class not in SUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES),
        "receiving_context_role_limits_present": _present(role_limits),
        "role_is_bounded_review_posture_only": True,
        "role_is_not_permission": True,
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_is_not_source_receipt": True,
        "role_is_not_source_authority": True,
        "role_is_not_currentness": True,
        "role_is_not_adoption": True,
        "role_is_not_validation": True,
        "role_is_not_invalidation": True,
        "role_is_not_operation_permission": True,
        "role_is_not_vessel_relation": True,
        "role_is_not_derivative_relation": True,
        "role_is_not_publication_flow": True,
    }


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    return all(key in non_claims and non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _scope_values(request: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    raw_scope = request.get("receiving_context_role_scope")
    if isinstance(raw_scope, str):
        values = [raw_scope]
    elif isinstance(raw_scope, Mapping):
        selected = _first(
            raw_scope.get("selected_receiving_context_role_scope_values"),
            raw_scope.get("receiving_context_role_scope_values"),
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
        value for value in values if value not in SUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE
    ]
    return values, unsupported


def _collapse_sections(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> list[Mapping[str, Any]]:
    identity_result = _identity_result_map(identity_section)
    return [
        request,
        _mapping(request.get("receiving_context_role_basis")),
        _mapping(request.get("receiving_context_role_scope")),
        _mapping(request.get("declared_non_claims")),
        _mapping(request.get("additional_basis_context")),
        _mapping(request.get("not_recorded_basis")),
        identity_section,
        identity_result,
        _mapping(identity_result.get("non_claims")),
        _mapping(identity_result.get("identity_preservation_statement")),
        _mapping(identity_result.get("selected_source_body_surface")),
        _mapping(identity_result.get("receiving_context")),
        selected_surface,
        _mapping(selected_surface.get("selected_source_body_surface")),
        receiving_context,
        _mapping(receiving_context.get("receiving_context")),
        role_section,
        _mapping(role_section.get("declared_receiving_context_role")),
        _mapping(role_section.get("receiving_context_role_limits")),
    ]


def _collapse_code(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> str | None:
    for code, fields in COLLAPSE_FIELDS.items():
        for section in _collapse_sections(
            request, identity_section, selected_surface, receiving_context, role_section
        ):
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
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> list[dict[str, Any]]:
    identity_load_code = identity_section.get("selected_identity_preservation_result_load_block_code")
    raw_identity = request.get("selected_identity_preservation_result")
    identity_shape_valid = (
        not _present(raw_identity) or isinstance(raw_identity, (Mapping, str))
    )
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        _get(
            identity_section,
            ("selected_identity_preservation_result", "selected_source_body_surface"),
        ),
    )
    raw_context = _first(
        request.get("receiving_context"),
        _get(identity_section, ("selected_identity_preservation_result", "receiving_context")),
    )
    surface_shape_valid = (
        not _present(raw_surface) or isinstance(raw_surface, (Mapping, str))
    )
    context_shape_valid = (
        not _present(raw_context) or isinstance(raw_context, (Mapping, str))
    )
    reception_class = _reception_class_value(request, identity_section)
    reception_purpose = _reception_purpose_value(request, identity_section)
    reception_limits = _reception_limits_value(request, identity_section)
    identity_basis = _identity_basis_value(request, identity_section)
    role_class = role_section.get("receiving_context_role_class")
    scope_values, unsupported_scope = _scope_values(request)
    collapse_code = _collapse_code(
        request, identity_section, selected_surface, receiving_context, role_section
    )
    checks = [
        _check(
            "receiving-context role question declared",
            _present(request.get("receiving_context_role_question")),
            "declared receiving-context role question",
            request.get("receiving_context_role_question"),
            "RECEIVING_CONTEXT_ROLE_QUESTION_UNDECLARED",
        ),
        _check(
            "receiving-context role intent supported",
            request.get("receiving_context_role_intent", INTENT_RECORD) in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            request.get("receiving_context_role_intent", INTENT_RECORD),
            "RECEIVING_CONTEXT_ROLE_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected identity preservation result present",
            identity_section.get("selected_identity_preservation_result_preserved") is True,
            "selected source-body reception identity preservation result",
            identity_section.get("selected_identity_preservation_result_id"),
            identity_load_code or "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected identity preservation result well formed",
            identity_shape_valid and identity_load_code is None,
            "mapping, reference string, or readable JSON object",
            identity_load_code or type(raw_identity).__name__,
            identity_load_code or "IDENTITY_PRESERVATION_RESULT_MALFORMED",
        ),
        _check(
            "selected identity preservation outcome declared",
            _present(identity_section.get("selected_identity_preservation_result_outcome")),
            "selected identity preservation outcome",
            identity_section.get("selected_identity_preservation_result_outcome"),
            "IDENTITY_PRESERVATION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected identity preservation outcome preserved",
            identity_section.get("selected_identity_preservation_result_recorded") is True,
            IDENTITY_PRESERVATION_OUTCOME,
            identity_section.get("selected_identity_preservation_result_outcome"),
            "IDENTITY_PRESERVATION_RESULT_NOT_PRESERVED",
        ),
        _check(
            "selected identity preservation failed check count zero",
            identity_section.get("selected_identity_preservation_result_failed_check_count_zero") is True,
            0,
            identity_section.get("selected_identity_preservation_result_failed_check_count"),
            "IDENTITY_PRESERVATION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected reception request declaration result preserved",
            identity_section.get("selected_reception_request_declaration_result_preserved") is True,
            "selected reception request declaration result",
            identity_section.get("selected_reception_request_declaration_result"),
            "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
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
            collapse_code or "RECEIVING_CONTEXT_ROLE_REPLACES_SOURCE",
        ),
        _check(
            "selected surface is not whole body by default",
            selected_surface.get("selected_surface_is_not_whole_body_by_default") is True,
            True,
            selected_surface.get("selected_surface_is_not_whole_body_by_default"),
            collapse_code or "RECEIVING_CONTEXT_ROLE_CREATES_CURRENTNESS",
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
            collapse_code or "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not source",
            receiving_context.get("receiving_context_is_not_source") is True,
            True,
            receiving_context.get("receiving_context_is_not_source"),
            collapse_code or "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not authority",
            receiving_context.get("receiving_context_is_not_authority") is True,
            True,
            receiving_context.get("receiving_context_is_not_authority"),
            collapse_code or "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving context is not current",
            receiving_context.get("receiving_context_is_not_current") is True,
            True,
            receiving_context.get("receiving_context_is_not_current"),
            collapse_code or "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_CURRENT",
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
            "identity preservation basis preserved",
            _present(identity_basis),
            "identity preservation basis",
            identity_basis,
            "IDENTITY_PRESERVATION_BASIS_MISSING",
        ),
        _check(
            "declared receiving-context role present",
            _present(role_section.get("declared_receiving_context_role")),
            "declared receiving-context role",
            role_section.get("declared_receiving_context_role"),
            "RECEIVING_CONTEXT_ROLE_MISSING",
        ),
        _check(
            "receiving-context role class present",
            _present(role_class),
            "receiving-context role class",
            role_class,
            "RECEIVING_CONTEXT_ROLE_CLASS_MISSING",
        ),
        _check(
            "receiving-context role class supported",
            role_section.get("receiving_context_role_class_supported") is True,
            list(SUPPORTED_RECEIVING_CONTEXT_ROLE_CLASSES),
            role_class,
            "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_CLASS",
        ),
        _check(
            "receiving-context role limits present",
            role_section.get("receiving_context_role_limits_present") is True,
            "receiving-context role limits",
            role_section.get("receiving_context_role_limits"),
            "RECEIVING_CONTEXT_ROLE_LIMITS_MISSING",
        ),
        _check(
            "receiving-context role scope supported",
            bool(scope_values) and not unsupported_scope,
            list(SUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE),
            scope_values if scope_values else "missing",
            "UNSUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE",
        ),
    ]
    false_checks = (
        ("role is not reception", "RECEIVING_CONTEXT_ROLE_RECOGNIZES_RECEPTION"),
        ("role is not authorization", "RECEIVING_CONTEXT_ROLE_AUTHORIZES_RECEPTION"),
        ("role is not source receipt", "RECEIVING_CONTEXT_ROLE_RECEIVES_SOURCE"),
        ("role does not create receiving-context governance", "RECEIVING_CONTEXT_ROLE_CREATES_GOVERNANCE"),
        ("role does not treat receiving context as source", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_SOURCE"),
        ("role does not treat receiving context as authority", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_AUTHORITY"),
        ("role does not treat receiving context as current", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_CURRENT"),
        ("role does not treat receiving context as receiver", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_RECEIVER"),
        ("role does not treat receiving context as adopter", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_ADOPTER"),
        ("role does not treat receiving context as validator", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VALIDATOR"),
        ("role does not treat receiving context as invalidator", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_INVALIDATOR"),
        ("role does not treat receiving context as operator", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_OPERATOR"),
        ("role does not treat receiving context as vessel", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_VESSEL"),
        ("role does not treat receiving context as derivative", "RECEIVING_CONTEXT_ROLE_TREATS_CONTEXT_AS_DERIVATIVE"),
        ("role is not validation", "RECEIVING_CONTEXT_ROLE_VALIDATES_SOURCE"),
        ("role is not invalidation", "RECEIVING_CONTEXT_ROLE_INVALIDATES_SOURCE"),
        ("role does not replace source", "RECEIVING_CONTEXT_ROLE_REPLACES_SOURCE"),
        ("role is not adoption", "RECEIVING_CONTEXT_ROLE_CREATES_ADOPTION"),
        ("role is not source authority", "RECEIVING_CONTEXT_ROLE_CREATES_AUTHORITY"),
        ("role is not currentness", "RECEIVING_CONTEXT_ROLE_CREATES_CURRENTNESS"),
        ("role does not create standing", "RECEIVING_CONTEXT_ROLE_CREATES_STANDING"),
        ("role does not create standing propagation", "RECEIVING_CONTEXT_ROLE_CREATES_STANDING_PROPAGATION"),
        ("role is not vessel relation", "RECEIVING_CONTEXT_ROLE_CREATES_VESSEL_RELATION"),
        ("role is not derivative relation", "RECEIVING_CONTEXT_ROLE_CREATES_DERIVATIVE_RELATION"),
        ("role is not operation permission", "RECEIVING_CONTEXT_ROLE_CREATES_OPERATION_PERMISSION"),
        ("role does not create public readiness", "RECEIVING_CONTEXT_ROLE_CREATES_PUBLIC_READINESS"),
        ("role does not claim final completion", "RECEIVING_CONTEXT_ROLE_CLAIMS_FINAL_COMPLETION"),
        ("role does not authorize follow-on work", "RECEIVING_CONTEXT_ROLE_AUTHORIZES_FOLLOW_ON_WORK"),
        ("role does not authorize continuation", "RECEIVING_CONTEXT_ROLE_AUTHORIZES_CONTINUATION"),
        ("role is not publication flow", "RECEIVING_CONTEXT_ROLE_OPENS_PUBLICATION_FLOW"),
        ("no mutation/replay/merge", "MUTATION_REPLAY_OR_MERGE_DETECTED"),
    )
    checks.extend(
        _check(name, collapse_code != code, False, collapse_code == code, code)
        for name, code in false_checks
    )
    checks.append(
        _check(
            "source-body surface remains source",
            selected_surface.get("selected_source_body_surface_remains_source") is True,
            True,
            selected_surface.get("selected_source_body_surface_remains_source"),
            collapse_code or "RECEIVING_CONTEXT_ROLE_REPLACES_SOURCE",
        )
    )
    checks.append(
        _check(
            "non-claims remain false",
            _declared_non_claims_valid(request),
            "all required receiving-context role non-claims false",
            _declared_non_claims(request),
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if request.get("receiving_context_role_intent", INTENT_RECORD) == INTENT_BLOCK:
        checks.append(
            _check(
                "receiving-context role review explicitly unblocked",
                False,
                "review not explicitly blocked",
                INTENT_BLOCK,
                "RECEIVING_CONTEXT_ROLE_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
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


def _metadata(request: Mapping[str, Any], identity_section: Mapping[str, Any]) -> dict[str, str]:
    basis = _first(
        request.get("receiving_context_role_request_id"),
        identity_section.get("selected_identity_preservation_result_id"),
        RESULT_ID_PREFIX,
    )
    return {
        "source_body_reception_receiving_context_role_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "source_body_reception_receiving_context_role_result_type": RESULT_TYPE,
        "source_body_reception_receiving_context_role_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["source_body_reception_receiving_context_role_recorded"] = (
        outcome == OUTCOME_RECORDED
    )
    return non_claims


def _declared_question_section(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "receiving_context_role_request_id": request.get("receiving_context_role_request_id"),
        "receiving_context_role_question": request.get("receiving_context_role_question"),
        "receiving_context_role_intent": request.get(
            "receiving_context_role_intent", INTENT_RECORD
        ),
        "declared_receiving_context_role_request_path": request.get(
            "declared_receiving_context_role_request_path"
        ),
        "requested_receiving_context_role_outcome": request.get(
            "requested_receiving_context_role_outcome", OUTCOME_RECORDED
        ),
        "selected_identity_preservation_result_id": identity_section.get(
            "selected_identity_preservation_result_id"
        ),
        "selected_identity_preservation_result_outcome": identity_section.get(
            "selected_identity_preservation_result_outcome"
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
        "reception_class": _reception_class_value(request, identity_section),
        "reception_purpose": _reception_purpose_value(request, identity_section),
        "receiving_context_role_class": role_section.get("receiving_context_role_class"),
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_does_not_receive_source": True,
        "role_does_not_create_source_authority": True,
        "role_does_not_create_currentness": True,
        "role_does_not_create_governance": True,
        "role_does_not_create_operation_permission": True,
        "role_does_not_open_publication_flow": True,
    }


def _receiving_context_role_basis_section(
    request: Mapping[str, Any],
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "declared_receiving_context_role_basis": _copy(
            request.get("receiving_context_role_basis")
        ),
        "selected_identity_preservation_result": _copy(
            identity_section.get("selected_identity_preservation_result")
        ),
        "selected_reception_request_declaration_result": _copy(
            identity_section.get("selected_reception_request_declaration_result")
        ),
        "selected_source_body_surface": _copy(selected_surface),
        "source_body_identity_basis": _copy(selected_surface.get("source_body_identity_basis")),
        "source_body_lineage_basis": _copy(selected_surface.get("source_body_lineage_basis")),
        "receiving_context": _copy(receiving_context),
        "receiving_context_type": receiving_context.get("receiving_context_type"),
        "reception_class": _copy(_reception_class_value(request, identity_section)),
        "reception_purpose": _copy(_reception_purpose_value(request, identity_section)),
        "reception_limits": _copy(_reception_limits_value(request, identity_section)),
        "identity_preservation_basis": _copy(_identity_basis_value(request, identity_section)),
        "declared_receiving_context_role": _copy(
            role_section.get("declared_receiving_context_role")
        ),
        "receiving_context_role_class": role_section.get("receiving_context_role_class"),
        "receiving_context_role_limits": _copy(
            role_section.get("receiving_context_role_limits")
        ),
        "role_non_reception_distinction": True,
        "role_non_authorization_distinction": True,
        "role_non_authority_distinction": True,
        "role_non_currentness_distinction": True,
        "role_non_adoption_distinction": True,
        "role_non_validation_distinction": True,
        "role_non_operation_permission_distinction": True,
        "role_non_publication_flow_distinction": True,
        "source_body_surface_remains_source": selected_surface.get(
            "selected_source_body_surface_remains_source"
        )
        is True,
        "receiving_context_remains_context_only": receiving_context.get(
            "receiving_context_remains_context_only"
        )
        is True,
    }


def _receiving_context_role_scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values, unsupported = _scope_values(request)
    return {
        "selected_receiving_context_role_scope_values": values,
        "unsupported_receiving_context_role_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "supported_receiving_context_role_scope_values": list(
            SUPPORTED_RECEIVING_CONTEXT_ROLE_SCOPE
        ),
        "receiving_context_remains_context_only": True,
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_is_not_source_receipt": True,
        "role_is_not_source_authority": True,
        "role_is_not_currentness": True,
        "role_is_not_adoption": True,
        "role_is_not_validation": True,
        "role_is_not_invalidation": True,
        "role_is_not_operation_permission": True,
        "role_is_not_vessel_relation": True,
        "role_is_not_derivative_relation": True,
        "role_is_not_publication_flow": True,
        "source_body_surface_remains_source": True,
    }


def _receiving_context_role_statement(
    outcome: str,
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    statement = {
        "source_body_reception_receiving_context_role_recorded": recorded,
        "selected_identity_preservation_result_preserved": identity_section.get(
            "selected_identity_preservation_result_preserved"
        )
        is True,
        "selected_identity_preservation_result_recorded": identity_section.get(
            "selected_identity_preservation_result_recorded"
        )
        is True,
        "selected_identity_preservation_result_failed_check_count_zero": identity_section.get(
            "selected_identity_preservation_result_failed_check_count_zero"
        )
        is True,
        "selected_reception_request_declaration_result_preserved": identity_section.get(
            "selected_reception_request_declaration_result_preserved"
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
        "receiving_context_is_not_source": receiving_context.get(
            "receiving_context_is_not_source"
        )
        is True,
        "receiving_context_is_not_authority": receiving_context.get(
            "receiving_context_is_not_authority"
        )
        is True,
        "receiving_context_is_not_current": receiving_context.get(
            "receiving_context_is_not_current"
        )
        is True,
        "reception_class_preserved": _present(_reception_class_value(request, identity_section)),
        "reception_purpose_preserved": _present(_reception_purpose_value(request, identity_section)),
        "reception_limits_preserved": _present(_reception_limits_value(request, identity_section)),
        "identity_preservation_basis_preserved": _present(
            _identity_basis_value(request, identity_section)
        ),
        "receiving_context_role_declared": _present(
            role_section.get("declared_receiving_context_role")
        ),
        "receiving_context_role_class_supported": role_section.get(
            "receiving_context_role_class_supported"
        )
        is True,
        "receiving_context_role_limits_present": role_section.get(
            "receiving_context_role_limits_present"
        )
        is True,
        "role_is_not_reception": True,
        "role_is_not_authorization": True,
        "role_is_not_source_receipt": True,
        "role_is_not_source_authority": True,
        "role_is_not_currentness": True,
        "role_is_not_adoption": True,
        "role_is_not_validation": True,
        "role_is_not_invalidation": True,
        "role_is_not_operation_permission": True,
        "role_is_not_vessel_relation": True,
        "role_is_not_derivative_relation": True,
        "role_is_not_publication_flow": True,
        "not_recorded_reason": request.get("not_recorded_basis"),
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


def _receiving_context_role_non_meaning() -> dict[str, bool]:
    meanings = {
        "reception_recognized": True,
        "reception_authorized": True,
        "source_received": True,
        "receiving_context_governance_created": True,
        "receiving_context_became_source": True,
        "receiving_context_became_authority": True,
        "receiving_context_became_current": True,
        "receiving_context_became_receiver": True,
        "receiving_context_became_adopter": True,
        "receiving_context_became_validator": True,
        "receiving_context_became_invalidator": True,
        "receiving_context_became_operator": True,
        "receiving_context_became_vessel": True,
        "receiving_context_became_derivative": True,
        "source_validated_by_receiving_context": True,
        "source_invalidated_by_receiving_context": True,
        "source_replaced": True,
        "adoption_created": True,
        "authority_created": True,
        "currentness_created": True,
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
    return {
        "additional_basis_required": additional,
        "additional_basis_context": _copy(request.get("additional_basis_context"))
        if additional
        else {},
        "additional_basis_scheduled": False,
        "additional_basis_authorized": False,
        "additional_basis_executed": False,
        "missing_basis_does_not_recognize_reception": True,
        "missing_basis_does_not_authorize_reception": True,
        "missing_basis_does_not_receive_source": True,
        "missing_basis_does_not_create_governance": True,
        "missing_basis_does_not_replace_source": True,
        "missing_basis_does_not_validate_source": True,
        "missing_basis_does_not_invalidate_source": True,
        "missing_basis_does_not_create_authority": True,
        "missing_basis_does_not_create_currentness": True,
        "missing_basis_does_not_create_standing": True,
        "missing_basis_does_not_create_operation_permission": True,
        "missing_basis_does_not_create_public_readiness": True,
        "missing_basis_does_not_claim_final_completion": True,
        "missing_basis_does_not_authorize_follow_on_work": True,
    }


def _not_recorded_basis(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_recorded = outcome == OUTCOME_NOT_RECORDED
    failed_checks = [
        _copy(dict(check))
        for check in checks
        if isinstance(check, Mapping) and check.get("passed") is not True
    ]
    return {
        "receiving_context_role_not_recorded": not_recorded,
        "not_recorded_basis": _copy(request.get("not_recorded_basis"))
        if not_recorded
        else {},
        "failed_receiving_context_role_checks": failed_checks if not_recorded else [],
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_authorize": True,
        "not_recorded_does_not_receive_source": True,
        "not_recorded_does_not_replace_source": True,
        "not_recorded_does_not_validate_source": True,
        "not_recorded_does_not_invalidate_source": True,
        "not_recorded_does_not_create_currentness": True,
        "not_recorded_does_not_recognize_reception": True,
    }


def _what_remains_open() -> dict[str, bool]:
    return {
        "source_body_reception_receiving_context_role_test": True,
        "source_body_reception_receiving_context_role_live_artifact": True,
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
        "receiving_context_governance": True,
        "public_readiness": True,
        "final_completion": True,
        "follow_on_work": True,
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def build_source_body_reception_receiving_context_role_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("receiving_context_role_checks")
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
    question = _mapping(result.get("declared_receiving_context_role_question"))
    identity = _mapping(result.get("selected_identity_preservation_result"))
    surface = _mapping(result.get("selected_source_body_surface"))
    context = _mapping(result.get("receiving_context"))
    role = _mapping(result.get("receiving_context_role"))
    basis = _mapping(result.get("receiving_context_role_basis"))
    statement = _mapping(result.get("receiving_context_role_statement"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "receiving_context_role_request_id": question.get("receiving_context_role_request_id"),
        "receiving_context_role_question": question.get("receiving_context_role_question"),
        "receiving_context_role_intent": question.get("receiving_context_role_intent"),
        "selected_identity_preservation_result_id": identity.get(
            "selected_identity_preservation_result_id"
        ),
        "selected_identity_preservation_result_outcome": identity.get(
            "selected_identity_preservation_result_outcome"
        ),
        "selected_source_body_surface_identifier": surface.get(
            "selected_source_body_surface_identifier"
        ),
        "selected_source_body_surface_type": surface.get(
            "selected_source_body_surface_type"
        ),
        "selected_source_body_surface_reference": _first(
            surface.get("selected_source_body_surface_reference"),
            surface.get("selected_source_body_surface_path"),
        ),
        "receiving_context_id": context.get("receiving_context_id"),
        "receiving_context_type": context.get("receiving_context_type"),
        "reception_class": basis.get("reception_class"),
        "reception_purpose": basis.get("reception_purpose"),
        "receiving_context_role_class": role.get("receiving_context_role_class"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "role_recorded": outcome == OUTCOME_RECORDED,
        "source_body_reception_receiving_context_role_recorded": outcome == OUTCOME_RECORDED,
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_identity_preservation_result_preserved": statement.get(
            "selected_identity_preservation_result_preserved"
        ),
        "selected_identity_preservation_result_recorded": statement.get(
            "selected_identity_preservation_result_recorded"
        ),
        "selected_identity_preservation_result_failed_check_count_zero": statement.get(
            "selected_identity_preservation_result_failed_check_count_zero"
        ),
        "selected_reception_request_declaration_result_preserved": statement.get(
            "selected_reception_request_declaration_result_preserved"
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
        "identity_preservation_basis_preserved": statement.get(
            "identity_preservation_basis_preserved"
        ),
        "receiving_context_role_declared": statement.get("receiving_context_role_declared"),
        "receiving_context_role_class_supported": statement.get(
            "receiving_context_role_class_supported"
        ),
        "receiving_context_role_limits_present": statement.get(
            "receiving_context_role_limits_present"
        ),
        "role_is_not_reception": statement.get("role_is_not_reception"),
        "role_is_not_authorization": statement.get("role_is_not_authorization"),
        "role_is_not_source_receipt": statement.get("role_is_not_source_receipt"),
        "role_is_not_source_authority": statement.get("role_is_not_source_authority"),
        "role_is_not_currentness": statement.get("role_is_not_currentness"),
        "role_is_not_adoption": statement.get("role_is_not_adoption"),
        "role_is_not_validation": statement.get("role_is_not_validation"),
        "role_is_not_invalidation": statement.get("role_is_not_invalidation"),
        "role_is_not_operation_permission": statement.get(
            "role_is_not_operation_permission"
        ),
        "role_is_not_vessel_relation": statement.get("role_is_not_vessel_relation"),
        "role_is_not_derivative_relation": statement.get(
            "role_is_not_derivative_relation"
        ),
        "role_is_not_publication_flow": statement.get("role_is_not_publication_flow"),
        "no_reception_recognized": non_claims.get("reception_recognized") is False,
        "no_reception_authorized": non_claims.get("reception_authorized") is False,
        "no_source_received": non_claims.get("source_received") is False,
        "no_receiving_context_governance": non_claims.get(
            "receiving_context_governance_created"
        )
        is False,
        "no_source_validation": non_claims.get("source_validated_by_receiving_context")
        is False,
        "no_source_invalidation": non_claims.get("source_invalidated_by_receiving_context")
        is False,
        "no_source_replacement": non_claims.get("source_replaced") is False,
        "no_adoption": non_claims.get("adoption_created") is False,
        "no_authority": non_claims.get("authority_created") is False,
        "no_currentness": non_claims.get("currentness_created") is False,
        "no_standing": non_claims.get("standing_created") is False,
        "no_vessel_relation": non_claims.get("vessel_relation_created") is False,
        "no_derivative_relation": non_claims.get("derivative_relation_created") is False,
        "no_operation_permission": non_claims.get("operation_permission_created") is False,
        "no_public_readiness": non_claims.get("public_launch_readiness_created") is False,
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
    identity_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> dict[str, Any]:
    result = {
        "source_body_reception_receiving_context_role_metadata": _metadata(
            request, identity_section
        ),
        "declared_receiving_context_role_question": _declared_question_section(
            request, identity_section, selected_surface, receiving_context, role_section
        ),
        "selected_identity_preservation_result": _copy(dict(identity_section)),
        "selected_source_body_surface": _copy(dict(selected_surface)),
        "receiving_context": _copy(dict(receiving_context)),
        "receiving_context_role": _copy(dict(role_section)),
        "receiving_context_role_basis": _receiving_context_role_basis_section(
            request, identity_section, selected_surface, receiving_context, role_section
        ),
        "receiving_context_role_scope": _receiving_context_role_scope_section(request),
        "receiving_context_role_checks": [_copy(dict(check)) for check in checks],
        "receiving_context_role_statement": _receiving_context_role_statement(
            outcome,
            identity_section,
            selected_surface,
            receiving_context,
            role_section,
            request,
        ),
        "receiving_context_role_non_meaning": _receiving_context_role_non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "not_recorded_basis": _not_recorded_basis(request, outcome, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["source_body_reception_receiving_context_role_summary"] = (
        build_source_body_reception_receiving_context_role_summary(result)
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
        request["declared_receiving_context_role_request_path"] = request_path
    identity_section = _identity_result_section(request, {}, None, None, None)
    selected_surface = _selected_source_surface_section(request, identity_section)
    receiving_context = _receiving_context_section(request, identity_section)
    role_section = _receiving_context_role_section(request)
    checks = [
        _check(
            code.replace("_", " ").lower(),
            False,
            "bounded source-body reception receiving-context role request",
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
        identity_section,
        selected_surface,
        receiving_context,
        role_section,
    )


def resolve_source_body_reception_receiving_context_role_boundary(
    declared_receiving_context_role_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_receiving_context_role_request is None:
        return _minimal_blocked_result("RECEIVING_CONTEXT_ROLE_QUESTION_UNDECLARED")
    if not isinstance(declared_receiving_context_role_request, Mapping):
        return _minimal_blocked_result(
            "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED"
        )

    request = _copy(dict(declared_receiving_context_role_request))
    identity_payload, load_code, load_detail, identity_path = _load_selected_identity_result(request)
    identity_section = _identity_result_section(
        request, identity_payload, load_code, load_detail, identity_path
    )
    selected_surface = _selected_source_surface_section(request, identity_section)
    receiving_context = _receiving_context_section(request, identity_section)
    role_section = _receiving_context_role_section(request)
    checks = _build_checks(
        request, identity_section, selected_surface, receiving_context, role_section
    )
    block_code = _first_failed_code(checks)
    requested_outcome = request.get(
        "requested_receiving_context_role_outcome", OUTCOME_RECORDED
    )
    intent = request.get("receiving_context_role_intent", INTENT_RECORD)
    if requested_outcome not in OUTCOME_FAMILY:
        block_code = block_code or "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED"

    if block_code:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_RECORDED

    return _build_result(
        request,
        outcome,
        checks,
        block_code if outcome == OUTCOME_BLOCKED else None,
        _block_reason(block_code, request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED
        else None,
        identity_section,
        selected_surface,
        receiving_context,
        role_section,
    )


def resolve_source_body_reception_receiving_context_role_boundary_from_path(
    declared_receiving_context_role_request_path: Path | str,
) -> dict:
    payload, error, detail = _read_json_object(declared_receiving_context_role_request_path)
    if error == "unreadable":
        return _minimal_blocked_result(
            "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_UNREADABLE",
            detail,
            request_path=str(declared_receiving_context_role_request_path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_RECEIVING_CONTEXT_ROLE_REQUEST_MALFORMED",
            detail,
            request_path=str(declared_receiving_context_role_request_path),
        )
    assert payload is not None
    request = _copy(payload)
    request["declared_receiving_context_role_request_path"] = str(
        declared_receiving_context_role_request_path
    )
    return resolve_source_body_reception_receiving_context_role_boundary(request)


def _default_filename(result: Mapping[str, Any]) -> str:
    request_id = _first(
        _get(
            result,
            (
                "declared_receiving_context_role_question",
                "receiving_context_role_request_id",
            ),
        ),
        _get(
            result,
            (
                "selected_identity_preservation_result",
                "selected_identity_preservation_result_id",
            ),
        ),
        _get(
            result,
            (
                "source_body_reception_receiving_context_role_metadata",
                "source_body_reception_receiving_context_role_result_id",
            ),
        ),
        RESULT_ID_PREFIX,
    )
    return (
        f"{_safe_component(request_id)}"
        "__source_body_reception_receiving_context_role_result.json"
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


def write_source_body_reception_receiving_context_role_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionReceivingContextRoleBoundaryError(
            "Result must be a mapping before it can be written."
        )
    filename = _default_filename(result)
    if output_path is None:
        target = SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_BOUNDARY_ROOT / filename
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


def build_declared_source_body_reception_receiving_context_role_request(
    receiving_context_role_request_id: str,
    receiving_context_role_question: str,
    selected_identity_preservation_result: Mapping[str, Any] | str,
    receiving_context_role_basis: Mapping[str, Any] | str,
    receiving_context_role_scope: Sequence[str] | Mapping[str, Any],
    receiving_context_role_intent: str = INTENT_RECORD,
    *,
    selected_identity_preservation_result_path: str | None = None,
    selected_identity_preservation_result_id: str | None = None,
    selected_identity_preservation_result_outcome: str | None = None,
    requested_receiving_context_role_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    identity_result = (
        _copy(dict(selected_identity_preservation_result))
        if isinstance(selected_identity_preservation_result, Mapping)
        else {"selected_identity_preservation_result_reference": selected_identity_preservation_result}
    )
    identity_section = _identity_result_section(
        {
            "selected_identity_preservation_result": identity_result,
            "selected_identity_preservation_result_path": selected_identity_preservation_result_path,
            "selected_identity_preservation_result_id": selected_identity_preservation_result_id,
            "selected_identity_preservation_result_outcome": (
                selected_identity_preservation_result_outcome
            ),
        },
        identity_result,
        None,
        None,
        selected_identity_preservation_result_path,
    )
    selected_surface = _selected_source_surface_section({}, identity_section)
    receiving_context = _receiving_context_section({}, identity_section)
    basis_payload = (
        _copy(dict(receiving_context_role_basis))
        if isinstance(receiving_context_role_basis, Mapping)
        else {"receiving_context_role_basis_reference": receiving_context_role_basis}
    )
    role_class = _first(
        basis_payload.get("receiving_context_role_class"),
        "REQUEST_DECLARATION_CONTEXT",
    )
    role_limits = _first(
        basis_payload.get("receiving_context_role_limits"),
        {
            "role_boundary_only": True,
            "role_is_not_reception": True,
            "role_is_not_authorization": True,
            "role_is_not_source_receipt": True,
            "role_is_not_source_authority": True,
            "role_is_not_currentness": True,
            "role_is_not_adoption": True,
            "role_is_not_validation": True,
            "role_is_not_invalidation": True,
            "role_is_not_operation_permission": True,
            "role_is_not_vessel_relation": True,
            "role_is_not_derivative_relation": True,
            "role_is_not_publication_flow": True,
        },
    )
    declared_role = _first(
        basis_payload.get("declared_receiving_context_role"),
        {
            "declared_receiving_context_role_id": "bounded-receiving-context-role",
            "declared_receiving_context_role_statement": (
                "Receiving context has bounded review/context role only."
            ),
        },
    )
    return {
        "receiving_context_role_request_id": receiving_context_role_request_id,
        "receiving_context_role_question": receiving_context_role_question,
        "receiving_context_role_intent": receiving_context_role_intent,
        "selected_identity_preservation_result": _copy(selected_identity_preservation_result),
        "selected_identity_preservation_result_path": selected_identity_preservation_result_path,
        "selected_identity_preservation_result_id": _first(
            selected_identity_preservation_result_id,
            identity_section.get("selected_identity_preservation_result_id"),
        ),
        "selected_identity_preservation_result_outcome": _first(
            selected_identity_preservation_result_outcome,
            identity_section.get("selected_identity_preservation_result_outcome"),
        ),
        "selected_reception_request_declaration_result": _copy(
            identity_section.get("selected_reception_request_declaration_result")
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
        "reception_class": _reception_class_value({}, identity_section),
        "reception_purpose": _copy(_reception_purpose_value({}, identity_section)),
        "reception_limits": _copy(_reception_limits_value({}, identity_section)),
        "identity_preservation_basis": _copy(_identity_basis_value({}, identity_section)),
        "receiving_context_role_basis": basis_payload,
        "declared_receiving_context_role": declared_role,
        "receiving_context_role_class": role_class,
        "receiving_context_role_limits": role_limits,
        "receiving_context_role_scope": _copy(receiving_context_role_scope),
        "requested_receiving_context_role_outcome": requested_receiving_context_role_outcome,
        "additional_basis_context": _copy(additional_basis_context),
        "not_recorded_basis": _copy(not_recorded_basis),
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
