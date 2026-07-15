"""Resolve source-body reception request declaration.

This resolver records one bounded source-body reception request declaration
only. It does not recognize reception, authorize reception, receive source,
create adoption, create authority, create currentness, create standing,
propagate standing, create vessel relation, create derivative relation, create
operation permission, replace source, validate or invalidate source, create
public readiness, claim final completion, authorize follow-on work, authorize
continuation, or open publication flow.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class SourceBodyReceptionRequestDeclarationError(Exception):
    """Raised for hard source-body reception request declaration failures."""


RESOLVER_MODULE = "resolve_source_body_reception_request_declaration"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "source_body_reception_request_declaration_result"
RESULT_ID_PREFIX = "source_body_reception_request_declaration"

SOURCE_BODY_RECEPTION_REQUEST_DECLARATION_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_request_declaration"
)

OUTCOME_DECLARED = "SOURCE_BODY_RECEPTION_REQUEST_DECLARED"
OUTCOME_NOT_SUFFICIENT = "SOURCE_BODY_RECEPTION_REQUEST_NOT_SUFFICIENT"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_REQUEST_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_DECLARED,
    OUTCOME_NOT_SUFFICIENT,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

SUPPORTED_RECEPTION_CLASSES = (
    "REFERENCE_RECEPTION",
    "INSPECTION_RECEPTION",
    "CARRIER_CONTEXT_RECEPTION",
)

REQUIRED_NON_CLAIMS = (
    "reception_recognized",
    "reception_authorized",
    "source_received",
    "adoption_created",
    "authority_created",
    "currentness_created",
    "standing_created",
    "standing_propagated",
    "vessel_relation_created",
    "derivative_relation_created",
    "operation_permission_created",
    "source_replaced",
    "source_validated_by_receiving_context",
    "source_invalidated_by_receiving_context",
    "receiving_context_became_source",
    "receiving_context_became_authority",
    "receiving_context_became_current",
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
    "RECEPTION_DECLARATION_RECOGNIZES_RECEPTION": (
        "reception_recognized",
        "source_body_reception_recognized",
        "reception_recorded",
        "reception_declared_as_recognized",
    ),
    "RECEPTION_DECLARATION_AUTHORIZES_RECEPTION": (
        "reception_authorized",
        "source_body_reception_authorized",
        "reception_permission_created",
        "source_reception_permission_created",
    ),
    "RECEPTION_DECLARATION_CREATES_ADOPTION": (
        "adoption_created",
        "source_adopted",
        "source_body_adopted",
    ),
    "RECEPTION_DECLARATION_CREATES_AUTHORITY": (
        "authority_created",
        "source_authority_created",
        "receiving_authority_created",
    ),
    "RECEPTION_DECLARATION_CREATES_CURRENTNESS": (
        "currentness_created",
        "source_currentness_created",
        "receiving_context_currentness_created",
    ),
    "RECEPTION_DECLARATION_CREATES_STANDING": (
        "standing_created",
        "source_standing_created",
        "standing_recorded",
    ),
    "RECEPTION_DECLARATION_CREATES_STANDING_PROPAGATION": (
        "standing_propagated",
        "standing_propagation_created",
    ),
    "RECEPTION_DECLARATION_CREATES_VESSEL_RELATION": (
        "vessel_relation_created",
        "vessel_relation_authorized",
    ),
    "RECEPTION_DECLARATION_CREATES_DERIVATIVE_RELATION": (
        "derivative_relation_created",
        "derivative_reception_created",
        "derivative_reception_authorized",
    ),
    "RECEPTION_DECLARATION_CREATES_OPERATION_PERMISSION": (
        "operation_permission_created",
        "operation_authorized",
        "permission_created",
    ),
    "RECEPTION_DECLARATION_REPLACES_SOURCE": (
        "source_replaced",
        "source_body_replaced",
        "source_replacement_created",
    ),
    "RECEPTION_DECLARATION_VALIDATES_SOURCE": (
        "source_validated_by_receiving_context",
        "source_validated",
        "receiving_context_validates_source",
    ),
    "RECEPTION_DECLARATION_INVALIDATES_SOURCE": (
        "source_invalidated_by_receiving_context",
        "source_invalidated",
        "receiving_context_invalidates_source",
    ),
    "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE": (
        "receiving_context_became_source",
        "receiving_context_treated_as_source",
        "receiving_context_is_source",
    ),
    "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_AUTHORITY": (
        "receiving_context_became_authority",
        "receiving_context_treated_as_authority",
        "receiving_context_is_authority",
    ),
    "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_CURRENT": (
        "receiving_context_became_current",
        "receiving_context_treated_as_current",
        "receiving_context_is_current",
    ),
    "RECEPTION_DECLARATION_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
        "public_launch_ready",
    ),
    "RECEPTION_DECLARATION_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_system_completion_claimed",
        "final_completion_created",
    ),
    "RECEPTION_DECLARATION_AUTHORIZES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "successor_scheduled",
    ),
    "RECEPTION_DECLARATION_SCHEDULES_CONTINUATION": (
        "continuation_authorized",
        "continuation_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "RECEPTION_DECLARATION_OPENS_PUBLICATION_FLOW": (
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
    "DECLARED_RECEPTION_REQUEST_MALFORMED": (
        "Declared reception request is malformed."
    ),
    "DECLARED_RECEPTION_REQUEST_UNREADABLE": (
        "Declared reception request path is unreadable."
    ),
    "RECEPTION_REQUEST_ID_MISSING": "Reception request id is missing.",
    "RECEPTION_QUESTION_MISSING": "Reception question is missing.",
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
    "SOURCE_BODY_IDENTITY_BASIS_MISSING": (
        "Source-body identity basis is missing."
    ),
    "SOURCE_BODY_LINEAGE_BASIS_MISSING": (
        "Source-body lineage basis is missing."
    ),
    "RECEIVING_CONTEXT_MISSING": "Receiving context is missing.",
    "RECEIVING_CONTEXT_MALFORMED": "Receiving context is malformed.",
    "RECEIVING_CONTEXT_TYPE_MISSING": "Receiving context type is missing.",
    "RECEPTION_CLASS_MISSING": "Reception class is missing.",
    "UNSUPPORTED_RECEPTION_CLASS": "Reception class is unsupported.",
    "RECEPTION_PURPOSE_MISSING": "Reception purpose is missing.",
    "RECEPTION_LIMITS_MISSING": "Reception limits are missing.",
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required reception declaration non-claim is missing or true."
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
    text = str(value or "source_body_reception_request").strip()
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in text)
    return safe.strip("_") or "source_body_reception_request"


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
    )
    return not _any_claim_true(value, forbidden)


def _selected_source_surface_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_surface = request.get("selected_source_body_surface")
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
                "source_body_surface_id",
                "surface_id",
                "id",
            ),
        ),
        raw_surface if isinstance(raw_surface, str) else None,
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
        "SOURCE_BODY_SURFACE_REFERENCE" if isinstance(raw_surface, str) else None,
    )
    surface_path = _first(
        request.get("selected_source_body_surface_path"),
        _first_key(
            payload,
            (
                "selected_source_body_surface_path",
                "source_body_surface_path",
                "surface_path",
                "path",
            ),
        ),
    )
    surface_reference = _first(
        request.get("selected_source_body_surface_reference"),
        _first_key(
            payload,
            (
                "selected_source_body_surface_reference",
                "source_body_surface_reference",
                "surface_reference",
                "reference",
            ),
        ),
        raw_surface if isinstance(raw_surface, str) else None,
    )
    identity_basis = _first(
        request.get("source_body_identity_basis"),
        _first_key(payload, ("source_body_identity_basis", "identity_basis")),
    )
    lineage_basis = _first(
        request.get("source_body_lineage_basis"),
        _first_key(payload, ("source_body_lineage_basis", "lineage_basis")),
    )
    closure_context = request.get("distributed_operation_closure_context")
    terminal_context = request.get("terminal_summary_context")
    section_maps = (
        request,
        payload,
        _mapping(identity_basis),
        _mapping(lineage_basis),
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
        for item in section_maps
    )
    return {
        "selected_source_body_surface": payload if payload else _copy(raw_surface),
        "selected_source_body_surface_identifier": identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_path": surface_path,
        "selected_source_body_surface_reference": surface_reference,
        "source_body_identity_basis": _copy(identity_basis),
        "source_body_lineage_basis": _copy(lineage_basis),
        "selected_source_body_surface_preserved": _present(raw_surface),
        "selected_source_body_surface_remains_source": source_remains_source,
        "selected_source_body_surface_not_received": not any(
            _any_claim_true(item, ("source_received", "reception_recognized"))
            for item in section_maps
        ),
        "selected_source_body_surface_not_adopted": not any(
            _any_claim_true(item, ("adoption_created", "source_adopted"))
            for item in section_maps
        ),
        "selected_source_body_surface_not_replaced": not any(
            _any_claim_true(item, ("source_replaced", "source_body_replaced"))
            for item in section_maps
        ),
        "selected_source_body_surface_not_validated_by_receiving_context": not any(
            _any_claim_true(item, ("source_validated_by_receiving_context",))
            for item in section_maps
        ),
        "selected_source_body_surface_not_invalidated_by_receiving_context": not any(
            _any_claim_true(item, ("source_invalidated_by_receiving_context",))
            for item in section_maps
        ),
        "distributed_operation_closure_context": _copy(closure_context),
        "distributed_operation_closure_context_supplied": _present(closure_context),
        "distributed_operation_closure_context_only": _context_only(closure_context),
        "terminal_summary_context": _copy(terminal_context),
        "terminal_summary_context_supplied": _present(terminal_context),
        "terminal_summary_context_only": _context_only(terminal_context),
        "distributed_operation_closure_artifact_is_not_selected_source_body_surface_by_default": True,
        "terminal_summary_is_not_selected_source_body_surface_by_default": True,
    }


def _receiving_context_section(request: Mapping[str, Any]) -> dict[str, Any]:
    raw_context = request.get("receiving_context")
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
        raw_context if isinstance(raw_context, str) else None,
    )
    context_type = _first(
        request.get("receiving_context_type"),
        _first_key(
            payload,
            ("receiving_context_type", "context_type", "type"),
        ),
        "RECEIVING_CONTEXT" if isinstance(raw_context, str) else None,
    )
    section_maps = (request, payload)
    context_only = (
        _context_only(payload)
        and not any(
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
            for item in section_maps
        )
    )
    return {
        "receiving_context": payload if payload else _copy(raw_context),
        "receiving_context_id": context_id,
        "receiving_context_type": context_type,
        "receiving_context_declared": _present(raw_context),
        "receiving_context_remains_context_only": context_only,
        "receiving_context_did_not_become_source": not any(
            _any_claim_true(item, ("receiving_context_became_source",))
            for item in section_maps
        ),
        "receiving_context_did_not_become_authority": not any(
            _any_claim_true(item, ("receiving_context_became_authority",))
            for item in section_maps
        ),
        "receiving_context_did_not_become_current": not any(
            _any_claim_true(item, ("receiving_context_became_current",))
            for item in section_maps
        ),
        "receiving_context_did_not_validate_source": not any(
            _any_claim_true(item, ("source_validated_by_receiving_context",))
            for item in section_maps
        ),
        "receiving_context_did_not_invalidate_source": not any(
            _any_claim_true(item, ("source_invalidated_by_receiving_context",))
            for item in section_maps
        ),
        "receiving_context_did_not_create_adoption": not any(
            _any_claim_true(item, ("adoption_created",))
            for item in section_maps
        ),
        "receiving_context_did_not_create_operation_permission": not any(
            _any_claim_true(item, ("operation_permission_created",))
            for item in section_maps
        ),
        "receiving_context_did_not_open_publication_flow": not any(
            _any_claim_true(item, ("publication_flow_opened",))
            for item in section_maps
        ),
    }


def _reception_class_section(request: Mapping[str, Any]) -> dict[str, Any]:
    reception_class = request.get("reception_class")
    supported = reception_class in SUPPORTED_RECEPTION_CLASSES
    return {
        "selected_reception_class": reception_class,
        "reception_class_declared": _present(reception_class),
        "reception_class_supported": supported,
        "supported_reception_classes": list(SUPPORTED_RECEPTION_CLASSES),
        "unsupported_reception_class": None if supported else reception_class,
        "class_is_declaration_class_only": True,
        "class_does_not_recognize_reception": True,
        "class_does_not_authorize_reception": True,
        "derivative_reception_supported": False,
    }


def _reception_purpose_section(request: Mapping[str, Any]) -> dict[str, Any]:
    purpose = request.get("reception_purpose")
    return {
        "reception_purpose": _copy(purpose),
        "reception_purpose_declared": _present(purpose),
        "purpose_is_not_permission": True,
        "purpose_does_not_recognize_reception": True,
        "purpose_does_not_authorize_reception": True,
        "purpose_does_not_create_adoption": True,
        "purpose_does_not_create_authority": True,
        "purpose_does_not_create_currentness": True,
    }


def _reception_limits_section(request: Mapping[str, Any]) -> dict[str, Any]:
    limits = request.get("reception_limits")
    return {
        "reception_limits": _copy(limits),
        "reception_limits_declared": _present(limits),
        "limits_preserve_no_recognition": True,
        "limits_preserve_no_authorization": True,
        "limits_preserve_no_adoption": True,
        "limits_preserve_no_authority": True,
        "limits_preserve_no_currentness": True,
        "limits_preserve_no_source_replacement": True,
        "limits_preserve_no_public_readiness": True,
        "limits_preserve_no_final_completion": True,
        "limits_preserve_no_follow_on_work": True,
    }


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    return all(key in non_claims and non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _collapse_sections(
    request: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    purpose: Mapping[str, Any],
    limits: Mapping[str, Any],
) -> list[Mapping[str, Any]]:
    return [
        request,
        _mapping(request.get("selected_source_body_surface")),
        selected_surface,
        _mapping(selected_surface.get("selected_source_body_surface")),
        _mapping(selected_surface.get("source_body_identity_basis")),
        _mapping(selected_surface.get("source_body_lineage_basis")),
        _mapping(selected_surface.get("distributed_operation_closure_context")),
        _mapping(selected_surface.get("terminal_summary_context")),
        receiving_context,
        _mapping(receiving_context.get("receiving_context")),
        purpose,
        _mapping(purpose.get("reception_purpose")),
        limits,
        _mapping(limits.get("reception_limits")),
        _declared_non_claims(request),
        _mapping(request.get("additional_basis_context")),
    ]


def _collapse_code(
    request: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    purpose: Mapping[str, Any],
    limits: Mapping[str, Any],
) -> str | None:
    sections = _collapse_sections(request, selected_surface, receiving_context, purpose, limits)
    for code, fields in COLLAPSE_FIELDS.items():
        for section in sections:
            if _any_claim_true(section, fields):
                return code
    if request.get("reception_class") == "DERIVATIVE_RECEPTION":
        return "UNSUPPORTED_RECEPTION_CLASS"
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
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    reception_class: Mapping[str, Any],
    purpose: Mapping[str, Any],
    limits: Mapping[str, Any],
) -> list[dict[str, Any]]:
    raw_surface = request.get("selected_source_body_surface")
    raw_context = request.get("receiving_context")
    surface_shape_valid = (
        not _present(raw_surface) or isinstance(raw_surface, (Mapping, str))
    )
    context_shape_valid = (
        not _present(raw_context) or isinstance(raw_context, (Mapping, str))
    )
    collapse_code = _collapse_code(
        request, selected_surface, receiving_context, purpose, limits
    )
    checks = [
        _check(
            "reception request id declared",
            _present(request.get("reception_request_id")),
            "declared reception request id",
            request.get("reception_request_id"),
            "RECEPTION_REQUEST_ID_MISSING",
        ),
        _check(
            "reception question declared",
            _present(request.get("reception_question")),
            "declared reception question",
            request.get("reception_question"),
            "RECEPTION_QUESTION_MISSING",
        ),
        _check(
            "selected source-body surface declared",
            _present(raw_surface),
            "selected source-body surface",
            raw_surface,
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
            "selected source-body surface identifier declared",
            _present(
                selected_surface.get("selected_source_body_surface_identifier")
            ),
            "selected source-body surface identifier",
            selected_surface.get("selected_source_body_surface_identifier"),
            "SELECTED_SOURCE_BODY_SURFACE_IDENTIFIER_MISSING",
        ),
        _check(
            "selected source-body surface type declared",
            _present(selected_surface.get("selected_source_body_surface_type")),
            "selected source-body surface type",
            selected_surface.get("selected_source_body_surface_type"),
            "SELECTED_SOURCE_BODY_SURFACE_TYPE_MISSING",
        ),
        _check(
            "selected source-body surface path/reference declared",
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
            "source-body identity basis declared",
            _present(selected_surface.get("source_body_identity_basis")),
            "source-body identity basis",
            selected_surface.get("source_body_identity_basis"),
            "SOURCE_BODY_IDENTITY_BASIS_MISSING",
        ),
        _check(
            "source-body lineage basis declared",
            _present(selected_surface.get("source_body_lineage_basis")),
            "source-body lineage basis",
            selected_surface.get("source_body_lineage_basis"),
            "SOURCE_BODY_LINEAGE_BASIS_MISSING",
        ),
        _check(
            "receiving context declared",
            _present(raw_context),
            "receiving context",
            raw_context,
            "RECEIVING_CONTEXT_MISSING",
        ),
        _check(
            "receiving context well formed",
            context_shape_valid,
            "mapping or string receiving context",
            type(raw_context).__name__ if _present(raw_context) else "missing",
            "RECEIVING_CONTEXT_MALFORMED",
        ),
        _check(
            "receiving context type declared",
            _present(receiving_context.get("receiving_context_type")),
            "receiving context type",
            receiving_context.get("receiving_context_type"),
            "RECEIVING_CONTEXT_TYPE_MISSING",
        ),
        _check(
            "reception class declared",
            _present(reception_class.get("selected_reception_class")),
            "declared reception class",
            reception_class.get("selected_reception_class"),
            "RECEPTION_CLASS_MISSING",
        ),
        _check(
            "reception class supported",
            reception_class.get("reception_class_supported") is True,
            list(SUPPORTED_RECEPTION_CLASSES),
            reception_class.get("selected_reception_class"),
            "UNSUPPORTED_RECEPTION_CLASS",
        ),
        _check(
            "reception purpose declared",
            purpose.get("reception_purpose_declared") is True,
            "declared reception purpose",
            purpose.get("reception_purpose"),
            "RECEPTION_PURPOSE_MISSING",
        ),
        _check(
            "reception limits declared",
            limits.get("reception_limits_declared") is True,
            "declared reception limits",
            limits.get("reception_limits"),
            "RECEPTION_LIMITS_MISSING",
        ),
        _check(
            "receiving context remains context only",
            receiving_context.get("receiving_context_remains_context_only") is True,
            True,
            receiving_context.get("receiving_context_remains_context_only"),
            collapse_code or "RECEPTION_DECLARATION_TREATS_RECEIVING_CONTEXT_AS_SOURCE",
        ),
        _check(
            "selected source-body surface remains source",
            selected_surface.get("selected_source_body_surface_remains_source") is True,
            True,
            selected_surface.get("selected_source_body_surface_remains_source"),
            collapse_code or "RECEPTION_DECLARATION_REPLACES_SOURCE",
        ),
        _check(
            "distributed-operation closure context remains context/evidence only",
            selected_surface.get("distributed_operation_closure_context_only") is True,
            True,
            selected_surface.get("distributed_operation_closure_context_only"),
            collapse_code or "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "terminal summary context remains context/evidence only",
            selected_surface.get("terminal_summary_context_only") is True,
            True,
            selected_surface.get("terminal_summary_context_only"),
            collapse_code or "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
    ]
    false_checks = (
        ("declaration does not recognize reception", "RECEPTION_DECLARATION_RECOGNIZES_RECEPTION"),
        ("declaration does not authorize reception", "RECEPTION_DECLARATION_AUTHORIZES_RECEPTION"),
        ("declaration does not create adoption", "RECEPTION_DECLARATION_CREATES_ADOPTION"),
        ("declaration does not create authority", "RECEPTION_DECLARATION_CREATES_AUTHORITY"),
        ("declaration does not create currentness", "RECEPTION_DECLARATION_CREATES_CURRENTNESS"),
        ("declaration does not create standing", "RECEPTION_DECLARATION_CREATES_STANDING"),
        ("declaration does not create standing propagation", "RECEPTION_DECLARATION_CREATES_STANDING_PROPAGATION"),
        ("declaration does not create vessel relation", "RECEPTION_DECLARATION_CREATES_VESSEL_RELATION"),
        ("declaration does not create derivative relation", "RECEPTION_DECLARATION_CREATES_DERIVATIVE_RELATION"),
        ("declaration does not create operation permission", "RECEPTION_DECLARATION_CREATES_OPERATION_PERMISSION"),
        ("declaration does not replace source", "RECEPTION_DECLARATION_REPLACES_SOURCE"),
        ("declaration does not validate source", "RECEPTION_DECLARATION_VALIDATES_SOURCE"),
        ("declaration does not invalidate source", "RECEPTION_DECLARATION_INVALIDATES_SOURCE"),
        ("declaration does not create public readiness", "RECEPTION_DECLARATION_CREATES_PUBLIC_READINESS"),
        ("declaration does not claim final completion", "RECEPTION_DECLARATION_CLAIMS_FINAL_COMPLETION"),
        ("declaration does not authorize follow-on work", "RECEPTION_DECLARATION_AUTHORIZES_FOLLOW_ON_WORK"),
        ("declaration does not authorize continuation", "RECEPTION_DECLARATION_SCHEDULES_CONTINUATION"),
        ("declaration does not open publication flow", "RECEPTION_DECLARATION_OPENS_PUBLICATION_FLOW"),
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
            "all required reception declaration non-claims false",
            _declared_non_claims(request),
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if collapse_code and all(check["passed"] for check in checks):
        checks.append(
            _check(
                "reception declaration collapse posture absent",
                False,
                "no collapse posture",
                collapse_code,
                collapse_code,
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


def _metadata(request: Mapping[str, Any]) -> dict[str, str]:
    basis = _first(request.get("reception_request_id"), RESULT_ID_PREFIX)
    return {
        "source_body_reception_request_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "source_body_reception_request_result_type": RESULT_TYPE,
        "source_body_reception_request_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["source_body_reception_request_declared"] = outcome == OUTCOME_DECLARED
    return non_claims


def _declaration_non_meaning() -> dict[str, bool]:
    meanings = {
        "reception_recognized": True,
        "reception_authorized": True,
        "source_received": True,
        "source_adopted": True,
        "source_validated": True,
        "source_invalidated": True,
        "source_replaced": True,
        "receiving_context_became_source": True,
        "receiving_context_became_authority": True,
        "receiving_context_became_current": True,
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


def _what_remains_open() -> dict[str, bool]:
    return {
        "source_body_reception_request_declaration_test": True,
        "source_body_reception_request_declaration_live_artifact": True,
        "source_body_identity_preservation_boundary": True,
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


def _declared_question_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "reception_request_id": request.get("reception_request_id"),
        "reception_question": request.get("reception_question"),
        "declared_reception_request_path": request.get("declared_reception_request_path"),
        "requested_reception_declaration_outcome": request.get(
            "requested_reception_declaration_outcome", OUTCOME_DECLARED
        ),
        "declaration_is_not_reception_recognition": True,
        "declaration_is_not_reception_authorization": True,
        "declaration_is_not_adoption": True,
        "declaration_is_not_authority": True,
        "declaration_is_not_currentness": True,
        "declaration_is_not_standing": True,
        "declaration_is_not_source_replacement": True,
        "declaration_is_not_public_readiness": True,
        "declaration_is_not_final_completion": True,
        "declaration_is_not_follow_on_work": True,
    }


def _declaration_statement(
    outcome: str,
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    reception_class: Mapping[str, Any],
    purpose: Mapping[str, Any],
    limits: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    declared = outcome == OUTCOME_DECLARED
    statement = {
        "source_body_reception_request_declared": declared,
        "selected_source_body_surface_preserved": selected_surface.get(
            "selected_source_body_surface_preserved"
        )
        is True,
        "selected_source_body_surface_remains_source": selected_surface.get(
            "selected_source_body_surface_remains_source"
        )
        is True,
        "receiving_context_declared": receiving_context.get("receiving_context_declared")
        is True,
        "receiving_context_remains_context_only": receiving_context.get(
            "receiving_context_remains_context_only"
        )
        is True,
        "reception_class_declared": reception_class.get("reception_class_declared")
        is True,
        "reception_class_supported": reception_class.get("reception_class_supported")
        is True,
        "reception_purpose_declared": purpose.get("reception_purpose_declared") is True,
        "reception_limits_declared": limits.get("reception_limits_declared") is True,
        "distributed_operation_closure_context_only": selected_surface.get(
            "distributed_operation_closure_context_only"
        )
        is True,
        "terminal_summary_context_only": selected_surface.get(
            "terminal_summary_context_only"
        )
        is True,
        "not_sufficient_reason": request.get("not_sufficient_reason"),
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


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
        "missing_basis_does_not_create_adoption": True,
        "missing_basis_does_not_create_authority": True,
        "missing_basis_does_not_create_currentness": True,
        "missing_basis_does_not_replace_source": True,
        "missing_basis_does_not_create_public_readiness": True,
        "missing_basis_does_not_claim_final_completion": True,
        "missing_basis_does_not_authorize_follow_on_work": True,
    }


def build_source_body_reception_request_declaration_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("declaration_checks")
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
    declared_question = _mapping(result.get("declared_reception_question"))
    selected_surface = _mapping(result.get("selected_source_body_surface"))
    receiving_context = _mapping(result.get("receiving_context"))
    reception_class = _mapping(result.get("reception_class"))
    purpose = _mapping(result.get("reception_purpose"))
    limits = _mapping(result.get("reception_limits"))
    statement = _mapping(result.get("declaration_statement"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "reception_request_id": declared_question.get("reception_request_id"),
        "reception_question": declared_question.get("reception_question"),
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
        "reception_class": reception_class.get("selected_reception_class"),
        "reception_purpose": purpose.get("reception_purpose"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "request_declared": outcome == OUTCOME_DECLARED,
        "source_body_reception_request_declared": outcome == OUTCOME_DECLARED,
        "not_sufficient": outcome == OUTCOME_NOT_SUFFICIENT,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_source_body_surface_preserved": statement.get(
            "selected_source_body_surface_preserved"
        ),
        "selected_source_body_surface_remains_source": statement.get(
            "selected_source_body_surface_remains_source"
        ),
        "receiving_context_declared": statement.get("receiving_context_declared"),
        "receiving_context_remains_context_only": statement.get(
            "receiving_context_remains_context_only"
        ),
        "reception_class_supported": statement.get("reception_class_supported"),
        "reception_purpose_declared": statement.get("reception_purpose_declared"),
        "reception_limits_declared": limits.get("reception_limits_declared"),
        "closure_context_only_where_supplied": selected_surface.get(
            "distributed_operation_closure_context_only"
        ),
        "terminal_summary_context_only_where_supplied": selected_surface.get(
            "terminal_summary_context_only"
        ),
        "no_reception_recognized": non_claims.get("reception_recognized") is False,
        "no_reception_authorized": non_claims.get("reception_authorized") is False,
        "no_adoption": non_claims.get("adoption_created") is False,
        "no_authority": non_claims.get("authority_created") is False,
        "no_currentness": non_claims.get("currentness_created") is False,
        "no_standing": non_claims.get("standing_created") is False,
        "no_vessel_relation": non_claims.get("vessel_relation_created") is False,
        "no_derivative_relation": non_claims.get("derivative_relation_created") is False,
        "no_operation_permission": non_claims.get("operation_permission_created") is False,
        "no_source_replacement": non_claims.get("source_replaced") is False,
        "no_source_validation": (
            non_claims.get("source_validated_by_receiving_context") is False
        ),
        "no_source_invalidation": (
            non_claims.get("source_invalidated_by_receiving_context") is False
        ),
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
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    reception_class: Mapping[str, Any],
    purpose: Mapping[str, Any],
    limits: Mapping[str, Any],
) -> dict[str, Any]:
    result = {
        "source_body_reception_request_metadata": _metadata(request),
        "declared_reception_question": _declared_question_section(request),
        "selected_source_body_surface": _copy(dict(selected_surface)),
        "receiving_context": _copy(dict(receiving_context)),
        "reception_class": _copy(dict(reception_class)),
        "reception_purpose": _copy(dict(purpose)),
        "reception_limits": _copy(dict(limits)),
        "declaration_checks": [_copy(dict(check)) for check in checks],
        "declaration_statement": _declaration_statement(
            outcome,
            selected_surface,
            receiving_context,
            reception_class,
            purpose,
            limits,
            request,
        ),
        "declaration_non_meaning": _declaration_non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "block_code": block_code,
            "block_reason": block_reason,
        },
    }
    result["source_body_reception_request_summary"] = (
        build_source_body_reception_request_declaration_summary(result)
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
        request["declared_reception_request_path"] = request_path
    selected_surface = _selected_source_surface_section(request)
    receiving_context = _receiving_context_section(request)
    reception_class = _reception_class_section(request)
    purpose = _reception_purpose_section(request)
    limits = _reception_limits_section(request)
    checks = [
        _check(
            code.replace("_", " ").lower(),
            False,
            "bounded source-body reception request declaration",
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
        selected_surface,
        receiving_context,
        reception_class,
        purpose,
        limits,
    )


def resolve_source_body_reception_request_declaration(
    declared_reception_request: Mapping[str, Any] | None = None,
) -> dict:
    if declared_reception_request is None:
        return _minimal_blocked_result("RECEPTION_REQUEST_ID_MISSING")
    if not isinstance(declared_reception_request, Mapping):
        return _minimal_blocked_result("DECLARED_RECEPTION_REQUEST_MALFORMED")

    request = _copy(dict(declared_reception_request))
    selected_surface = _selected_source_surface_section(request)
    receiving_context = _receiving_context_section(request)
    reception_class = _reception_class_section(request)
    purpose = _reception_purpose_section(request)
    limits = _reception_limits_section(request)
    checks = _build_checks(
        request,
        selected_surface,
        receiving_context,
        reception_class,
        purpose,
        limits,
    )
    block_code = _first_failed_code(checks)
    requested_outcome = request.get(
        "requested_reception_declaration_outcome", OUTCOME_DECLARED
    )
    if requested_outcome not in OUTCOME_FAMILY:
        block_code = block_code or "DECLARED_RECEPTION_REQUEST_MALFORMED"
    if requested_outcome == OUTCOME_BLOCKED:
        block_code = block_code or "DECLARED_RECEPTION_REQUEST_MALFORMED"

    if block_code:
        outcome = OUTCOME_BLOCKED
    elif requested_outcome == OUTCOME_NOT_SUFFICIENT:
        outcome = OUTCOME_NOT_SUFFICIENT
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    else:
        outcome = OUTCOME_DECLARED

    return _build_result(
        request,
        outcome,
        checks,
        block_code if outcome == OUTCOME_BLOCKED else None,
        _block_reason(block_code, request.get("block_reason"))
        if outcome == OUTCOME_BLOCKED
        else None,
        selected_surface,
        receiving_context,
        reception_class,
        purpose,
        limits,
    )


def resolve_source_body_reception_request_declaration_from_path(
    declared_reception_request_path: Path | str,
) -> dict:
    payload, error, detail = _read_json_object(declared_reception_request_path)
    if error == "unreadable":
        return _minimal_blocked_result(
            "DECLARED_RECEPTION_REQUEST_UNREADABLE",
            detail,
            request_path=str(declared_reception_request_path),
        )
    if error == "malformed":
        return _minimal_blocked_result(
            "DECLARED_RECEPTION_REQUEST_MALFORMED",
            detail,
            request_path=str(declared_reception_request_path),
        )
    assert payload is not None
    request = _copy(payload)
    request["declared_reception_request_path"] = str(declared_reception_request_path)
    return resolve_source_body_reception_request_declaration(request)


def _default_filename(result: Mapping[str, Any]) -> str:
    request_id = _first(
        _get(result, ("declared_reception_question", "reception_request_id")),
        _get(
            result,
            (
                "source_body_reception_request_metadata",
                "source_body_reception_request_result_id",
            ),
        ),
        RESULT_ID_PREFIX,
    )
    return (
        f"{_safe_component(request_id)}"
        "__source_body_reception_request_declaration_result.json"
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


def write_source_body_reception_request_declaration_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionRequestDeclarationError(
            "Result must be a mapping before it can be written."
        )
    filename = _default_filename(result)
    if output_path is None:
        target = SOURCE_BODY_RECEPTION_REQUEST_DECLARATION_ROOT / filename
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


def build_declared_source_body_reception_request(
    reception_request_id: str,
    reception_question: str,
    selected_source_body_surface: Mapping[str, Any] | str,
    receiving_context: Mapping[str, Any] | str,
    reception_class: str,
    reception_purpose: Mapping[str, Any] | str,
    reception_limits: Mapping[str, Any] | Sequence[str],
    *,
    source_body_identity_basis: Mapping[str, Any] | str | None = None,
    source_body_lineage_basis: Mapping[str, Any] | str | None = None,
    distributed_operation_closure_context: Mapping[str, Any] | str | None = None,
    terminal_summary_context: Mapping[str, Any] | str | None = None,
    requested_reception_declaration_outcome: str = OUTCOME_DECLARED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_sufficient_reason: str | None = None,
) -> dict:
    surface_payload = _as_payload(
        selected_source_body_surface,
        "selected_source_body_surface_reference",
        "selected_source_body_surface_identifier",
    )
    receiving_payload = _as_payload(
        receiving_context,
        "receiving_context_reference",
        "receiving_context_id",
    )
    surface_identifier = _first(
        _first_key(
            surface_payload,
            (
                "selected_source_body_surface_identifier",
                "source_body_surface_identifier",
                "source_body_surface_id",
                "surface_id",
                "id",
            ),
        ),
        selected_source_body_surface
        if isinstance(selected_source_body_surface, str)
        else None,
    )
    surface_type = _first(
        _first_key(
            surface_payload,
            ("selected_source_body_surface_type", "source_body_surface_type", "type"),
        ),
        "SOURCE_BODY_SURFACE_REFERENCE",
    )
    surface_reference = _first(
        _first_key(
            surface_payload,
            (
                "selected_source_body_surface_reference",
                "source_body_surface_reference",
                "reference",
                "path",
            ),
        ),
        selected_source_body_surface
        if isinstance(selected_source_body_surface, str)
        else None,
    )
    receiving_context_id = _first(
        _first_key(
            receiving_payload,
            (
                "receiving_context_id",
                "receiving_context_reference",
                "context_id",
                "id",
                "name",
            ),
        ),
        receiving_context if isinstance(receiving_context, str) else None,
    )
    receiving_context_type = _first(
        _first_key(receiving_payload, ("receiving_context_type", "context_type", "type")),
        "RECEIVING_CONTEXT",
    )
    identity_basis = source_body_identity_basis or {
        "source_body_identity_basis_declared": True,
        "selected_source_body_surface_identifier": surface_identifier,
        "identity_basis_is_not_reception": True,
    }
    lineage_basis = source_body_lineage_basis or {
        "source_body_lineage_basis_declared": True,
        "selected_source_body_surface_identifier": surface_identifier,
        "lineage_basis_is_not_authority": True,
    }
    return {
        "reception_request_id": reception_request_id,
        "reception_question": reception_question,
        "selected_source_body_surface": _copy(selected_source_body_surface),
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_reference": surface_reference,
        "source_body_identity_basis": _copy(identity_basis),
        "source_body_lineage_basis": _copy(lineage_basis),
        "distributed_operation_closure_context": _copy(
            distributed_operation_closure_context
        ),
        "terminal_summary_context": _copy(terminal_summary_context),
        "receiving_context": _copy(receiving_context),
        "receiving_context_id": receiving_context_id,
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": _copy(reception_purpose),
        "reception_limits": _copy(reception_limits),
        "requested_reception_declaration_outcome": (
            requested_reception_declaration_outcome
        ),
        "additional_basis_context": _copy(additional_basis_context),
        "not_sufficient_reason": not_sufficient_reason,
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
