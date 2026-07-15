"""Resolve the bounded source-body reception closure boundary.

This resolver answers one question only:

    Can this conformed source-body reception boundary chain be closed?

Closure records bounded reception-chain closure only. It is not reception
authorization, source receipt, source received, adoption, authority, currentness,
operation permission, public readiness, final completion, continuation,
reusable permission, another reception request, or follow-on authorization.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class SourceBodyReceptionClosureBoundaryError(Exception):
    """Raised for impossible source-body reception closure boundary failures."""


RESOLVER_MODULE = "resolve_source_body_reception_closure_boundary"
RESULT_VERSION = "0.1.0"
SOURCE_BODY_RECEPTION_CLOSURE_BOUNDARY_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_source_body_reception_closure_boundary"
)

OUTCOME_RECORDED = "SOURCE_BODY_RECEPTION_CLOSURE_RECORDED"
OUTCOME_NOT_RECORDED = "SOURCE_BODY_RECEPTION_CLOSURE_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_CLOSURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_CLOSURE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

REQUIRED_CONFORMANCE_OUTCOME = "SOURCE_BODY_RECEPTION_CONFORMANCE_PASSED"

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_CLOSURE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_CLOSURE"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_CLOSURE_REVIEW"
SUPPORTED_CLOSURE_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_CLOSURE_SCOPE = {
    "RECEPTION_CHAIN_CLOSURE_ONLY",
    "CLOSURE_IS_NOT_AUTHORIZATION",
    "CLOSURE_IS_NOT_SOURCE_RECEIPT",
    "CLOSURE_DOES_NOT_RECEIVE_SOURCE",
    "CLOSURE_DOES_NOT_CREATE_SOURCE_RECEIPT",
    "CLOSURE_IS_NOT_ADOPTION",
    "CLOSURE_IS_NOT_AUTHORITY",
    "CLOSURE_IS_NOT_CURRENTNESS",
    "CLOSURE_IS_NOT_VALIDATION",
    "CLOSURE_IS_NOT_INVALIDATION",
    "CLOSURE_IS_NOT_OPERATION_PERMISSION",
    "CLOSURE_IS_NOT_PUBLICATION_FLOW",
    "CLOSURE_IS_NOT_FINAL_COMPLETION",
    "CLOSURE_DOES_NOT_AUTHORIZE_CONTINUATION",
    "CLOSURE_DOES_NOT_AUTHORIZE_FOLLOW_ON_WORK",
    "CLOSURE_DOES_NOT_CREATE_REUSABLE_PERMISSION",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "reception_authorized",
    "source_received",
    "source_receipt_recorded",
    "source_receipt_created",
    "receiving_context_governance_created",
    "receiving_context_became_source",
    "receiving_context_became_authority",
    "receiving_context_became_current",
    "receiving_context_became_receiver",
    "receiving_context_became_adopter",
    "receiving_context_became_validator",
    "receiving_context_became_invalidator",
    "receiving_context_became_operator",
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
    "reusable_permission_created",
    "another_reception_request_authorized",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "source_body_reception_closure_recorded",
    "source_body_reception_boundary_chain_closed",
    "reception_closure_passed",
    "reception_family_closure_recorded",
)

COLLAPSE_FIELD_CODES = {
    "reception_authorized": "CLOSURE_AUTHORIZES_RECEPTION",
    "source_received": "CLOSURE_RECEIVES_SOURCE",
    "source_receipt_recorded": "CLOSURE_RECORDS_SOURCE_RECEIPT",
    "source_receipt_created": "CLOSURE_CREATES_SOURCE_RECEIPT",
    "receiving_context_governance_created": "CLOSURE_CREATES_GOVERNANCE",
    "receiving_context_became_source": "CLOSURE_TREATS_CONTEXT_AS_SOURCE",
    "receiving_context_became_authority": "CLOSURE_TREATS_CONTEXT_AS_AUTHORITY",
    "receiving_context_became_current": "CLOSURE_TREATS_CONTEXT_AS_CURRENT",
    "receiving_context_became_receiver": "CLOSURE_TREATS_CONTEXT_AS_RECEIVER",
    "receiving_context_became_adopter": "CLOSURE_TREATS_CONTEXT_AS_ADOPTER",
    "receiving_context_became_validator": "CLOSURE_TREATS_CONTEXT_AS_VALIDATOR",
    "receiving_context_became_invalidator": "CLOSURE_TREATS_CONTEXT_AS_INVALIDATOR",
    "receiving_context_became_operator": "CLOSURE_TREATS_CONTEXT_AS_OPERATOR",
    "source_validated_by_receiving_context": "CLOSURE_VALIDATES_SOURCE",
    "source_invalidated_by_receiving_context": "CLOSURE_INVALIDATES_SOURCE",
    "source_replaced": "CLOSURE_REPLACES_SOURCE",
    "adoption_created": "CLOSURE_CREATES_ADOPTION",
    "authority_created": "CLOSURE_CREATES_AUTHORITY",
    "currentness_created": "CLOSURE_CREATES_CURRENTNESS",
    "standing_created": "CLOSURE_CREATES_STANDING",
    "standing_propagated": "CLOSURE_CREATES_STANDING_PROPAGATION",
    "vessel_relation_created": "CLOSURE_CREATES_VESSEL_RELATION",
    "derivative_relation_created": "CLOSURE_CREATES_DERIVATIVE_RELATION",
    "operation_permission_created": "CLOSURE_CREATES_OPERATION_PERMISSION",
    "public_launch_readiness_created": "CLOSURE_CREATES_PUBLIC_READINESS",
    "public_readiness_created": "CLOSURE_CREATES_PUBLIC_READINESS",
    "final_completion_claimed": "CLOSURE_CLAIMS_FINAL_COMPLETION",
    "follow_on_work_authorized": "CLOSURE_AUTHORIZES_FOLLOW_ON_WORK",
    "continuation_authorized": "CLOSURE_AUTHORIZES_CONTINUATION",
    "publication_flow_opened": "CLOSURE_OPENS_PUBLICATION_FLOW",
    "reusable_permission_created": "CLOSURE_CREATES_REUSABLE_PERMISSION",
    "another_reception_request_authorized": "CLOSURE_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
    "successor_reception_authorized": "CLOSURE_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
}

MUTATION_FLAGS = ("mutation_performed", "replay_performed", "merge_performed")


def _present(value: Any) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def _truthy(value: Any) -> bool:
    return value is True or value == "true" or value == "TRUE" or value == 1


def _is_false(value: Any) -> bool:
    return value is False or value == "false" or value == "FALSE" or value == 0


def _value_at(mapping: Mapping[str, Any] | None, path: Sequence[str]) -> Any:
    current: Any = mapping
    for key in path:
        if not isinstance(current, Mapping) or key not in current:
            return None
        current = current[key]
    return current


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _deepcopy_mapping(value: Mapping[str, Any] | None) -> dict[str, Any] | None:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return None


def _read_json_object(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return None, "unreadable"
    try:
        loaded = json.loads(raw)
    except json.JSONDecodeError:
        return None, "malformed"
    if not isinstance(loaded, dict):
        return None, "malformed"
    return loaded, None


def _failed_check_count(result: Mapping[str, Any] | None, check_key: str) -> int | None:
    if not isinstance(result, Mapping):
        return None
    explicit = _first_present(
        result.get("failed_check_count"),
        _value_at(result, ("source_body_reception_conformance_summary", "failed_check_count")),
        _value_at(result, ("summary", "failed_check_count")),
    )
    if explicit is not None:
        try:
            return int(explicit)
        except (TypeError, ValueError):
            return None
    checks = result.get(check_key)
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = scope.get("selected_closure_scope_values")
        if values is None:
            values = scope.get("closure_scope_values")
        if values is None:
            values = scope.get("scope_values")
        if values is None:
            values = [
                key
                for key, value in scope.items()
                if isinstance(key, str) and _truthy(value)
            ]
        return [str(value) for value in values] if isinstance(values, Sequence) else []
    if isinstance(scope, Sequence):
        return [str(value) for value in scope]
    return []


def _contains_truthy_key(value: Any, key: str) -> bool:
    if isinstance(value, Mapping):
        for current_key, current_value in value.items():
            if current_key == key and _truthy(current_value):
                return True
            if _contains_truthy_key(current_value, key):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_truthy_key(item, key) for item in value)
    return False


def _safe_component(value: Any) -> str:
    text = str(value or "source_body_reception_closure").strip()
    cleaned = "".join(
        character if character.isalnum() or character in ("-", "_") else "_"
        for character in text
    )
    cleaned = cleaned.strip("_")
    return cleaned or "source_body_reception_closure"


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
    }
    if passed:
        record["block_code"] = None
        record["failure_code"] = None
    else:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": reason if code is not None else None,
    }


def _load_selected_conformance_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path_value = request.get("selected_conformance_result_path")
    if _present(path_value):
        path = Path(str(path_value))
        loaded, failure = _read_json_object(path)
        if failure == "unreadable":
            return None, str(path), "CONFORMANCE_RESULT_UNREADABLE"
        if failure == "malformed":
            return None, str(path), "CONFORMANCE_RESULT_MALFORMED"
        return loaded, str(path), None

    supplied = request.get("selected_conformance_result")
    if supplied is None:
        return None, None, None
    if not isinstance(supplied, Mapping):
        return None, None, "CONFORMANCE_RESULT_MALFORMED"
    return copy.deepcopy(dict(supplied)), None, None


def _nested_mapping(*values: Any) -> dict[str, Any] | None:
    for value in values:
        if isinstance(value, Mapping):
            return copy.deepcopy(dict(value))
    return None


def _selected_conformance_statement(selected: Mapping[str, Any] | None) -> Mapping[str, Any]:
    value = _value_at(selected, ("conformance_statement",))
    return value if isinstance(value, Mapping) else {}


def _selected_conformance_summary(selected: Mapping[str, Any] | None) -> Mapping[str, Any]:
    value = _value_at(selected, ("source_body_reception_conformance_summary",))
    return value if isinstance(value, Mapping) else {}


def _selected_conformance_basis(selected: Mapping[str, Any] | None) -> Mapping[str, Any]:
    value = _value_at(selected, ("conformance_basis",))
    return value if isinstance(value, Mapping) else {}


def _extract_conformance_id(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    return _first_present(
        request.get("selected_conformance_result_id"),
        _value_at(selected, ("source_body_reception_conformance_metadata", "source_body_reception_conformance_result_id")),
        _value_at(selected, ("source_body_reception_conformance_summary", "source_body_reception_conformance_result_id")),
        _value_at(selected, ("declared_conformance_question", "conformance_request_id")),
        _value_at(selected, ("conformance_request_id",)),
    )


def _extract_conformance_outcome(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    return _first_present(
        request.get("selected_conformance_result_outcome"),
        request.get("expected_selected_conformance_outcome"),
        _value_at(selected, ("outcome",)),
        _value_at(selected, ("source_body_reception_conformance_summary", "outcome")),
        _value_at(selected, ("conformance_statement", "outcome")),
    )


def _extract_selected_receipt_exhaustion_result(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> dict[str, Any] | None:
    basis = _selected_conformance_basis(selected)
    return _nested_mapping(
        request.get("selected_receipt_exhaustion_result"),
        basis.get("selected_receipt_exhaustion_result"),
        _value_at(selected, ("selected_receipt_exhaustion_result", "raw_selected_receipt_exhaustion_result")),
        _value_at(selected, ("selected_receipt_exhaustion_result", "selected_receipt_exhaustion_result")),
        selected.get("selected_receipt_exhaustion_result") if isinstance(selected, Mapping) else None,
    )


def _extract_selected_recognition_result(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    receipt_exhaustion: Mapping[str, Any] | None,
) -> dict[str, Any] | None:
    basis = _selected_conformance_basis(selected)
    return _nested_mapping(
        request.get("selected_recognition_result"),
        basis.get("selected_recognition_result"),
        _value_at(receipt_exhaustion, ("selected_recognition_result", "raw_selected_recognition_result")),
        _value_at(receipt_exhaustion, ("selected_recognition_result", "selected_recognition_result")),
        _value_at(receipt_exhaustion, ("selected_recognition_result",)),
    )


def _extract_named_result(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    receipt_exhaustion: Mapping[str, Any] | None,
    request_key: str,
    basis_key: str,
    receipt_keys: Sequence[str],
) -> dict[str, Any] | None:
    basis = _selected_conformance_basis(selected)
    candidates: list[Any] = [request.get(request_key), basis.get(basis_key)]
    for key in receipt_keys:
        candidates.append(_value_at(receipt_exhaustion, (key,)))
        candidates.append(_value_at(receipt_exhaustion, (key, f"raw_{key}")))
        candidates.append(_value_at(receipt_exhaustion, (key, key)))
    return _nested_mapping(*candidates)


def _extract_surface(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    receipt_exhaustion: Mapping[str, Any] | None,
) -> dict[str, Any] | None:
    basis = _selected_conformance_basis(selected)
    return _nested_mapping(
        request.get("selected_source_body_surface"),
        basis.get("selected_source_body_surface"),
        _value_at(selected, ("selected_source_body_surface",)),
        _value_at(receipt_exhaustion, ("selected_source_body_surface",)),
        _value_at(receipt_exhaustion, ("receipt_exhaustion_basis", "selected_source_body_surface")),
    )


def _extract_receiving_context(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    receipt_exhaustion: Mapping[str, Any] | None,
) -> dict[str, Any] | None:
    basis = _selected_conformance_basis(selected)
    return _nested_mapping(
        request.get("receiving_context"),
        basis.get("receiving_context"),
        _value_at(selected, ("receiving_context",)),
        _value_at(receipt_exhaustion, ("receiving_context",)),
        _value_at(receipt_exhaustion, ("receipt_exhaustion_basis", "receiving_context")),
    )


def _surface_identifier(request: Mapping[str, Any], surface: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_identifier"),
        _value_at(surface, ("selected_source_body_surface_identifier",)),
        _value_at(surface, ("source_body_surface_identifier",)),
        _value_at(surface, ("identifier",)),
        _value_at(surface, ("id",)),
    )


def _surface_type(request: Mapping[str, Any], surface: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_type"),
        _value_at(surface, ("selected_source_body_surface_type",)),
        _value_at(surface, ("source_body_surface_type",)),
        _value_at(surface, ("type",)),
    )


def _surface_reference(request: Mapping[str, Any], surface: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_reference"),
        request.get("selected_source_body_surface_path"),
        _value_at(surface, ("selected_source_body_surface_reference",)),
        _value_at(surface, ("selected_source_body_surface_path",)),
        _value_at(surface, ("reference",)),
        _value_at(surface, ("path",)),
    )


def _context_id(request: Mapping[str, Any], context: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("receiving_context_id"),
        _value_at(context, ("receiving_context_id",)),
        _value_at(context, ("id",)),
        _value_at(context, ("name",)),
        _value_at(context, ("reference",)),
    )


def _context_type(request: Mapping[str, Any], context: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("receiving_context_type"),
        _value_at(context, ("receiving_context_type",)),
        _value_at(context, ("context_type",)),
        _value_at(context, ("type",)),
    )


def _basis_value(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    receipt_exhaustion: Mapping[str, Any] | None,
    key: str,
) -> Any:
    basis = _selected_conformance_basis(selected)
    return _first_present(
        request.get(key),
        basis.get(key),
        _value_at(selected, ("source_body_reception_conformance_summary", key)),
        _value_at(receipt_exhaustion, ("receipt_exhaustion_basis", key)),
        _value_at(receipt_exhaustion, (key,)),
    )


def _flag(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    key: str,
    *,
    default: bool = False,
) -> bool:
    statement = _selected_conformance_statement(selected)
    summary = _selected_conformance_summary(selected)
    candidates = (
        request.get(key),
        statement.get(key),
        summary.get(key),
        _value_at(selected, ("non_claims", key)),
        selected.get(key) if isinstance(selected, Mapping) else None,
    )
    for candidate in candidates:
        if candidate is not None:
            return _truthy(candidate)
    return default


def _required_non_claims_false(request: Mapping[str, Any]) -> bool:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or not _is_false(declared[key]):
            return False
    return True


def _collapse_code(request: Mapping[str, Any]) -> str | None:
    for flag in MUTATION_FLAGS:
        if _contains_truthy_key(request, flag):
            return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    for key, code in COLLAPSE_FIELD_CODES.items():
        if _contains_truthy_key(request, key):
            return code
    return None


def _build_non_claims(outcome: str) -> dict[str, Any]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    for key in ALLOWED_RECORDED_TRUE_FIELDS:
        non_claims[key] = outcome == OUTCOME_RECORDED
    non_claims.update(
        {
            "even_when_closure_recorded_reception_is_not_authorized": True,
            "even_when_closure_recorded_source_remains_unreceived": True,
            "even_when_closure_recorded_source_receipt_is_not_recorded": True,
            "even_when_closure_recorded_final_completion_is_not_claimed": True,
            "even_when_closure_recorded_follow_on_work_is_not_authorized": True,
            "even_when_closure_recorded_continuation_is_not_authorized": True,
            "even_when_closure_recorded_reusable_permission_is_not_created": True,
            "even_when_closure_recorded_another_reception_request_is_not_authorized": True,
        }
    )
    return non_claims


def _build_closure_non_meaning() -> dict[str, bool]:
    return {
        "closure_does_not_mean_reception_authorized": True,
        "closure_does_not_mean_source_received": True,
        "closure_does_not_mean_source_receipt_recorded": True,
        "closure_does_not_mean_source_receipt_created": True,
        "closure_does_not_mean_source_adopted": True,
        "closure_does_not_mean_source_validated": True,
        "closure_does_not_mean_source_invalidated": True,
        "closure_does_not_mean_source_replaced": True,
        "closure_does_not_mean_receiving_context_became_source": True,
        "closure_does_not_mean_receiving_context_became_authority": True,
        "closure_does_not_mean_receiving_context_became_current": True,
        "closure_does_not_mean_receiving_context_became_receiver": True,
        "closure_does_not_mean_receiving_context_became_adopter": True,
        "closure_does_not_mean_receiving_context_became_validator": True,
        "closure_does_not_mean_receiving_context_became_invalidator": True,
        "closure_does_not_mean_receiving_context_became_operator": True,
        "closure_does_not_mean_receiving_context_governance_created": True,
        "closure_does_not_mean_standing_created": True,
        "closure_does_not_mean_standing_propagated": True,
        "closure_does_not_mean_vessel_relation_created": True,
        "closure_does_not_mean_derivative_relation_created": True,
        "closure_does_not_mean_operation_permission_created": True,
        "closure_does_not_mean_public_readiness_created": True,
        "closure_does_not_mean_final_completion_claimed": True,
        "closure_does_not_mean_follow_on_work_authorized": True,
        "closure_does_not_mean_continuation_authorized": True,
        "closure_does_not_mean_publication_flow_opened": True,
        "closure_does_not_mean_reusable_permission_created": True,
        "closure_does_not_mean_successor_reception_authorized": True,
        "closure_does_not_mean_another_reception_request_authorized": True,
    }


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "source-body reception closure test",
            "source-body reception closure live artifact",
            "derivative reception",
            "vessel relation",
            "adoption",
            "authority creation",
            "currentness creation",
            "standing creation",
            "operation permission",
            "receiving-context governance",
            "public readiness",
            "final completion",
            "follow-on work",
            "continuation",
            "publication flow",
            "reusable permission",
            "successor reception request",
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _determine_block_code(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    selected_load_code: str | None,
    conformance_outcome: Any,
    conformance_failed_count: int | None,
    receipt_exhaustion: Mapping[str, Any] | None,
    recognition: Mapping[str, Any] | None,
    non_capture: Mapping[str, Any] | None,
    eligibility: Mapping[str, Any] | None,
    receiving_role: Mapping[str, Any] | None,
    identity: Mapping[str, Any] | None,
    declaration: Mapping[str, Any] | None,
    surface: Mapping[str, Any] | None,
    context: Mapping[str, Any] | None,
    receiving_context_type: Any,
    reception_class: Any,
    reception_purpose: Any,
    reception_limits: Any,
    closure_basis: Any,
    closure_limits: Any,
    closure_scope_values: Sequence[str],
) -> str | None:
    if not _present(request.get("closure_question")):
        return "CLOSURE_QUESTION_UNDECLARED"
    intent = request.get("closure_intent")
    if intent == INTENT_BLOCK:
        return "CLOSURE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_CLOSURE_INTENTS:
        return "CLOSURE_INTENT_UNSUPPORTED"
    if selected_load_code is not None:
        return selected_load_code
    if selected is None:
        return "CONFORMANCE_RESULT_MISSING"
    if not _present(conformance_outcome):
        return "CONFORMANCE_RESULT_OUTCOME_MISSING"
    if conformance_outcome != REQUIRED_CONFORMANCE_OUTCOME:
        return "CONFORMANCE_RESULT_NOT_PASSED"
    if conformance_failed_count is None or conformance_failed_count != 0:
        return "CONFORMANCE_RESULT_HAS_FAILED_CHECKS"
    if receipt_exhaustion is None:
        return "RECEIPT_EXHAUSTION_RESULT_MISSING"
    if recognition is None:
        return "RECOGNITION_RESULT_MISSING"
    if non_capture is None:
        return "NON_CAPTURE_RESULT_MISSING"
    if eligibility is None:
        return "ELIGIBILITY_RESULT_MISSING"
    if receiving_role is None:
        return "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"
    if identity is None:
        return "IDENTITY_PRESERVATION_RESULT_MISSING"
    if declaration is None:
        return "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING"
    if surface is None:
        return "SELECTED_SOURCE_BODY_SURFACE_MISSING"
    if not isinstance(surface, Mapping):
        return "SELECTED_SOURCE_BODY_SURFACE_MALFORMED"
    if context is None:
        return "RECEIVING_CONTEXT_MISSING"
    if not isinstance(context, Mapping):
        return "RECEIVING_CONTEXT_MALFORMED"
    if not _present(receiving_context_type):
        return "RECEIVING_CONTEXT_TYPE_MISSING"
    if not _present(reception_class):
        return "RECEPTION_CLASS_MISSING"
    if not _present(reception_purpose):
        return "RECEPTION_PURPOSE_MISSING"
    if not _present(reception_limits):
        return "RECEPTION_LIMITS_MISSING"
    if not _present(closure_basis):
        return "CLOSURE_BASIS_MISSING"
    if not _present(closure_limits):
        return "CLOSURE_LIMITS_MISSING"
    unsupported_scope = [
        value for value in closure_scope_values if value not in SUPPORTED_CLOSURE_SCOPE
    ]
    if unsupported_scope:
        return "UNSUPPORTED_CLOSURE_SCOPE"
    collapse = _collapse_code(request)
    if collapse is not None:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    conformance_outcome: Any,
    conformance_failed_count: int | None,
    receipt_exhaustion: Mapping[str, Any] | None,
    recognition: Mapping[str, Any] | None,
    non_capture: Mapping[str, Any] | None,
    eligibility: Mapping[str, Any] | None,
    receiving_role: Mapping[str, Any] | None,
    identity: Mapping[str, Any] | None,
    declaration: Mapping[str, Any] | None,
    surface: Mapping[str, Any] | None,
    context: Mapping[str, Any] | None,
    receiving_context_type: Any,
    reception_class: Any,
    reception_purpose: Any,
    reception_limits: Any,
    closure_basis: Any,
    closure_limits: Any,
    closure_scope_values: Sequence[str],
) -> list[dict[str, Any]]:
    unsupported_scope = [
        value for value in closure_scope_values if value not in SUPPORTED_CLOSURE_SCOPE
    ]
    no_mutation = not any(_contains_truthy_key(request, key) for key in MUTATION_FLAGS)
    checks = [
        _check(
            "closure_question_declared",
            _present(request.get("closure_question")),
            "declared closure question",
            request.get("closure_question"),
            "CLOSURE_QUESTION_UNDECLARED",
        ),
        _check(
            "closure_intent_supported",
            request.get("closure_intent") in SUPPORTED_CLOSURE_INTENTS
            and request.get("closure_intent") != INTENT_BLOCK,
            sorted(SUPPORTED_CLOSURE_INTENTS - {INTENT_BLOCK}),
            request.get("closure_intent"),
            "CLOSURE_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_conformance_result_present",
            selected is not None,
            "selected conformance result present",
            selected is not None,
            "CONFORMANCE_RESULT_MISSING",
        ),
        _check(
            "selected_conformance_outcome_declared",
            _present(conformance_outcome),
            "selected conformance outcome declared",
            conformance_outcome,
            "CONFORMANCE_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_conformance_outcome_passed",
            conformance_outcome == REQUIRED_CONFORMANCE_OUTCOME,
            REQUIRED_CONFORMANCE_OUTCOME,
            conformance_outcome,
            "CONFORMANCE_RESULT_NOT_PASSED",
        ),
        _check(
            "selected_conformance_failed_check_count_zero",
            conformance_failed_count == 0,
            0,
            conformance_failed_count,
            "CONFORMANCE_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected_receipt_exhaustion_result_preserved",
            receipt_exhaustion is not None,
            "selected receipt / exhaustion result preserved",
            receipt_exhaustion is not None,
            "RECEIPT_EXHAUSTION_RESULT_MISSING",
        ),
        _check(
            "selected_recognition_result_preserved",
            recognition is not None,
            "selected recognition result preserved",
            recognition is not None,
            "RECOGNITION_RESULT_MISSING",
        ),
        _check(
            "selected_non_capture_result_preserved",
            non_capture is not None,
            "selected non-capture result preserved",
            non_capture is not None,
            "NON_CAPTURE_RESULT_MISSING",
        ),
        _check(
            "selected_eligibility_result_preserved",
            eligibility is not None,
            "selected eligibility / admissibility result preserved",
            eligibility is not None,
            "ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "selected_receiving_context_role_result_preserved",
            receiving_role is not None,
            "selected receiving-context role result preserved",
            receiving_role is not None,
            "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected_identity_preservation_result_preserved",
            identity is not None,
            "selected identity preservation result preserved",
            identity is not None,
            "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected_reception_request_declaration_result_preserved",
            declaration is not None,
            "selected request declaration result preserved",
            declaration is not None,
            "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
        ),
        _check(
            "selected_source_body_surface_preserved",
            surface is not None,
            "selected source-body surface preserved",
            surface is not None,
            "SELECTED_SOURCE_BODY_SURFACE_MISSING",
        ),
        _check(
            "selected_source_body_surface_remains_source",
            _flag(request, selected, "selected_source_body_surface_remains_source", default=True),
            "selected surface remains source",
            _flag(request, selected, "selected_source_body_surface_remains_source", default=True),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "selected_surface_is_not_whole_body_by_default",
            _flag(request, selected, "selected_surface_is_not_whole_body_by_default", default=True),
            "selected surface is not whole body by default",
            _flag(request, selected, "selected_surface_is_not_whole_body_by_default", default=True),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "receiving_context_preserved",
            context is not None,
            "receiving context preserved",
            context is not None,
            "RECEIVING_CONTEXT_MISSING",
        ),
        _check(
            "receiving_context_type_declared",
            _present(receiving_context_type),
            "receiving context type declared",
            receiving_context_type,
            "RECEIVING_CONTEXT_TYPE_MISSING",
        ),
        _check(
            "receiving_context_remains_context_only",
            _flag(request, selected, "receiving_context_remains_context_only", default=True),
            "receiving context remains context only",
            _flag(request, selected, "receiving_context_remains_context_only", default=True),
            "RECEIVING_CONTEXT_MALFORMED",
        ),
        _check(
            "receiving_context_is_not_source",
            _flag(request, selected, "receiving_context_is_not_source", default=True),
            "receiving context is not source",
            _flag(request, selected, "receiving_context_is_not_source", default=True),
            "CLOSURE_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving_context_is_not_authority",
            _flag(request, selected, "receiving_context_is_not_authority", default=True),
            "receiving context is not authority",
            _flag(request, selected, "receiving_context_is_not_authority", default=True),
            "CLOSURE_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving_context_is_not_current",
            _flag(request, selected, "receiving_context_is_not_current", default=True),
            "receiving context is not current",
            _flag(request, selected, "receiving_context_is_not_current", default=True),
            "CLOSURE_TREATS_CONTEXT_AS_CURRENT",
        ),
        _check(
            "conformance_was_recorded",
            _flag(request, selected, "source_body_reception_conformance_recorded", default=True),
            "conformance recorded",
            _flag(request, selected, "source_body_reception_conformance_recorded", default=True),
            "CONFORMANCE_RESULT_NOT_PASSED",
        ),
        _check(
            "conformance_passed",
            _flag(request, selected, "source_body_reception_conformance_passed", default=True),
            "conformance passed",
            _flag(request, selected, "source_body_reception_conformance_passed", default=True),
            "CONFORMANCE_RESULT_NOT_PASSED",
        ),
        _check(
            "conformance_reception_chain_only",
            _flag(
                request,
                selected,
                "reception_chain_conformance_only",
                default=True,
            )
            or _flag(
                request,
                selected,
                "conformance_remained_reception_chain_conformance_only",
                default=True,
            ),
            "conformance remained reception-chain conformance only",
            True,
            "CONFORMANCE_RESULT_MALFORMED",
        ),
        _check(
            "source_unreceived",
            not _contains_truthy_key(request, "source_received"),
            "source remains unreceived",
            request.get("source_received"),
            "CLOSURE_RECEIVES_SOURCE",
        ),
        _check(
            "source_receipt_unrecorded",
            not _contains_truthy_key(request, "source_receipt_recorded"),
            "source receipt remains unrecorded",
            request.get("source_receipt_recorded"),
            "CLOSURE_RECORDS_SOURCE_RECEIPT",
        ),
        _check(
            "source_receipt_uncreated",
            not _contains_truthy_key(request, "source_receipt_created"),
            "source receipt remains uncreated",
            request.get("source_receipt_created"),
            "CLOSURE_CREATES_SOURCE_RECEIPT",
        ),
        _check(
            "reception_class_declared",
            _present(reception_class),
            "reception class declared",
            reception_class,
            "RECEPTION_CLASS_MISSING",
        ),
        _check(
            "reception_purpose_declared",
            _present(reception_purpose),
            "reception purpose declared",
            reception_purpose,
            "RECEPTION_PURPOSE_MISSING",
        ),
        _check(
            "reception_limits_declared",
            _present(reception_limits),
            "reception limits declared",
            reception_limits,
            "RECEPTION_LIMITS_MISSING",
        ),
        _check(
            "closure_basis_declared",
            _present(closure_basis),
            "closure basis declared",
            closure_basis,
            "CLOSURE_BASIS_MISSING",
        ),
        _check(
            "closure_limits_declared",
            _present(closure_limits),
            "closure limits declared",
            closure_limits,
            "CLOSURE_LIMITS_MISSING",
        ),
        _check(
            "closure_scope_supported",
            not unsupported_scope,
            "supported closure scope only",
            list(closure_scope_values),
            "UNSUPPORTED_CLOSURE_SCOPE",
        ),
        _check(
            "closure_is_not_authorization",
            not _contains_truthy_key(request, "reception_authorized"),
            "closure is not authorization",
            request.get("reception_authorized"),
            "CLOSURE_AUTHORIZES_RECEPTION",
        ),
        _check(
            "closure_is_not_source_receipt",
            not _contains_truthy_key(request, "source_receipt_recorded"),
            "closure is not source receipt",
            request.get("source_receipt_recorded"),
            "CLOSURE_RECORDS_SOURCE_RECEIPT",
        ),
        _check(
            "closure_does_not_receive_source",
            not _contains_truthy_key(request, "source_received"),
            "closure does not receive source",
            request.get("source_received"),
            "CLOSURE_RECEIVES_SOURCE",
        ),
        _check(
            "closure_does_not_create_source_receipt",
            not _contains_truthy_key(request, "source_receipt_created"),
            "closure does not create source receipt",
            request.get("source_receipt_created"),
            "CLOSURE_CREATES_SOURCE_RECEIPT",
        ),
        _check(
            "closure_does_not_create_adoption",
            not _contains_truthy_key(request, "adoption_created"),
            "closure does not create adoption",
            request.get("adoption_created"),
            "CLOSURE_CREATES_ADOPTION",
        ),
        _check(
            "closure_does_not_create_authority",
            not _contains_truthy_key(request, "authority_created"),
            "closure does not create authority",
            request.get("authority_created"),
            "CLOSURE_CREATES_AUTHORITY",
        ),
        _check(
            "closure_does_not_create_currentness",
            not _contains_truthy_key(request, "currentness_created"),
            "closure does not create currentness",
            request.get("currentness_created"),
            "CLOSURE_CREATES_CURRENTNESS",
        ),
        _check(
            "closure_does_not_validate_source",
            not _contains_truthy_key(request, "source_validated_by_receiving_context"),
            "closure does not validate source",
            request.get("source_validated_by_receiving_context"),
            "CLOSURE_VALIDATES_SOURCE",
        ),
        _check(
            "closure_does_not_invalidate_source",
            not _contains_truthy_key(request, "source_invalidated_by_receiving_context"),
            "closure does not invalidate source",
            request.get("source_invalidated_by_receiving_context"),
            "CLOSURE_INVALIDATES_SOURCE",
        ),
        _check(
            "closure_does_not_replace_source",
            not _contains_truthy_key(request, "source_replaced"),
            "closure does not replace source",
            request.get("source_replaced"),
            "CLOSURE_REPLACES_SOURCE",
        ),
        _check(
            "closure_does_not_create_operation_permission",
            not _contains_truthy_key(request, "operation_permission_created"),
            "closure does not create operation permission",
            request.get("operation_permission_created"),
            "CLOSURE_CREATES_OPERATION_PERMISSION",
        ),
        _check(
            "closure_does_not_create_governance",
            not _contains_truthy_key(request, "receiving_context_governance_created"),
            "closure does not create governance",
            request.get("receiving_context_governance_created"),
            "CLOSURE_CREATES_GOVERNANCE",
        ),
        _check(
            "closure_does_not_open_publication_flow",
            not _contains_truthy_key(request, "publication_flow_opened"),
            "closure does not open publication flow",
            request.get("publication_flow_opened"),
            "CLOSURE_OPENS_PUBLICATION_FLOW",
        ),
        _check(
            "closure_does_not_create_public_readiness",
            not _contains_truthy_key(request, "public_launch_readiness_created")
            and not _contains_truthy_key(request, "public_readiness_created"),
            "closure does not create public readiness",
            request.get("public_launch_readiness_created"),
            "CLOSURE_CREATES_PUBLIC_READINESS",
        ),
        _check(
            "closure_does_not_claim_final_completion",
            not _contains_truthy_key(request, "final_completion_claimed"),
            "closure does not claim final completion",
            request.get("final_completion_claimed"),
            "CLOSURE_CLAIMS_FINAL_COMPLETION",
        ),
        _check(
            "closure_does_not_authorize_continuation",
            not _contains_truthy_key(request, "continuation_authorized"),
            "closure does not authorize continuation",
            request.get("continuation_authorized"),
            "CLOSURE_AUTHORIZES_CONTINUATION",
        ),
        _check(
            "closure_does_not_authorize_follow_on_work",
            not _contains_truthy_key(request, "follow_on_work_authorized"),
            "closure does not authorize follow-on work",
            request.get("follow_on_work_authorized"),
            "CLOSURE_AUTHORIZES_FOLLOW_ON_WORK",
        ),
        _check(
            "closure_does_not_create_reusable_permission",
            not _contains_truthy_key(request, "reusable_permission_created"),
            "closure does not create reusable permission",
            request.get("reusable_permission_created"),
            "CLOSURE_CREATES_REUSABLE_PERMISSION",
        ),
        _check(
            "closure_does_not_authorize_another_reception_request",
            not _contains_truthy_key(request, "another_reception_request_authorized")
            and not _contains_truthy_key(request, "successor_reception_authorized"),
            "closure does not authorize another reception request",
            request.get("another_reception_request_authorized"),
            "CLOSURE_AUTHORIZES_ANOTHER_RECEPTION_REQUEST",
        ),
        _check(
            "no_mutation_replay_merge",
            no_mutation,
            "no mutation/replay/merge",
            no_mutation,
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(request),
            "required non-claims explicit and false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    return checks


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    request_malformed_code: str | None = None,
) -> dict[str, Any]:
    selected, selected_path, selected_load_code = _load_selected_conformance_result(request)
    conformance_id = _extract_conformance_id(request, selected)
    conformance_outcome = _extract_conformance_outcome(request, selected)
    conformance_failed_count = _failed_check_count(selected, "conformance_checks")
    receipt_exhaustion = _extract_selected_receipt_exhaustion_result(request, selected)
    recognition = _extract_selected_recognition_result(request, selected, receipt_exhaustion)
    non_capture = _extract_named_result(
        request,
        selected,
        receipt_exhaustion,
        "selected_non_capture_result",
        "selected_non_capture_result",
        ("selected_non_capture_result", "selected_non_capture_non_adoption_non_currentness_result"),
    )
    eligibility = _extract_named_result(
        request,
        selected,
        receipt_exhaustion,
        "selected_eligibility_result",
        "selected_eligibility_result",
        ("selected_eligibility_result", "selected_eligibility_admissibility_result"),
    )
    receiving_role = _extract_named_result(
        request,
        selected,
        receipt_exhaustion,
        "selected_receiving_context_role_result",
        "selected_receiving_context_role_result",
        ("selected_receiving_context_role_result",),
    )
    identity = _extract_named_result(
        request,
        selected,
        receipt_exhaustion,
        "selected_identity_preservation_result",
        "selected_identity_preservation_result",
        ("selected_identity_preservation_result",),
    )
    declaration = _extract_named_result(
        request,
        selected,
        receipt_exhaustion,
        "selected_reception_request_declaration_result",
        "selected_reception_request_declaration_result",
        ("selected_reception_request_declaration_result", "selected_request_declaration_result"),
    )
    surface = _extract_surface(request, selected, receipt_exhaustion)
    context = _extract_receiving_context(request, selected, receipt_exhaustion)
    surface_identifier = _surface_identifier(request, surface)
    surface_type = _surface_type(request, surface)
    surface_reference = _surface_reference(request, surface)
    receiving_context_id = _context_id(request, context)
    receiving_context_type = _context_type(request, context)
    reception_class = _basis_value(request, selected, receipt_exhaustion, "reception_class")
    reception_purpose = _basis_value(request, selected, receipt_exhaustion, "reception_purpose")
    reception_limits = _basis_value(request, selected, receipt_exhaustion, "reception_limits")
    selected_receiving_context_role = _basis_value(
        request, selected, receipt_exhaustion, "selected_receiving_context_role"
    )
    receiving_context_role_class = _basis_value(
        request, selected, receipt_exhaustion, "receiving_context_role_class"
    )
    receiving_context_role_limits = _basis_value(
        request, selected, receipt_exhaustion, "receiving_context_role_limits"
    )
    conformance_basis = _first_present(
        request.get("conformance_basis"),
        _value_at(selected, ("conformance_basis",)),
    )
    conformance_limits = _first_present(
        request.get("conformance_limits"),
        _value_at(selected, ("conformance_limits",)),
    )
    closure_basis = request.get("closure_basis")
    closure_limits = request.get("closure_limits")
    closure_scope_values = _scope_values(request.get("closure_scope"))

    block_code = request_malformed_code or _determine_block_code(
        request,
        selected,
        selected_load_code,
        conformance_outcome,
        conformance_failed_count,
        receipt_exhaustion,
        recognition,
        non_capture,
        eligibility,
        receiving_role,
        identity,
        declaration,
        surface,
        context,
        receiving_context_type,
        reception_class,
        reception_purpose,
        reception_limits,
        closure_basis,
        closure_limits,
        closure_scope_values,
    )

    requested_outcome = request.get("requested_closure_outcome") or OUTCOME_RECORDED
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    elif request.get("closure_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome in OUTCOME_FAMILY:
        outcome = requested_outcome
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_CLOSURE_REQUEST_MALFORMED"

    checks = _build_checks(
        request,
        selected,
        conformance_outcome,
        conformance_failed_count,
        receipt_exhaustion,
        recognition,
        non_capture,
        eligibility,
        receiving_role,
        identity,
        declaration,
        surface,
        context,
        receiving_context_type,
        reception_class,
        reception_purpose,
        reception_limits,
        closure_basis,
        closure_limits,
        closure_scope_values,
    )
    if outcome == OUTCOME_BLOCKED and block_code is not None:
        matched = False
        for check in checks:
            if check.get("block_code") == block_code and check.get("passed") is False:
                matched = True
                break
        if not matched:
            checks.append(
                _check(
                    "closure_review_blocked",
                    False,
                    "non-blocked closure review",
                    block_code,
                    block_code,
                )
            )

    failed_count = sum(1 for check in checks if check.get("passed") is not True)
    passed_count = len(checks) - failed_count
    if outcome == OUTCOME_RECORDED and failed_count != 0:
        outcome = OUTCOME_BLOCKED
        block_code = block_code or "CONFORMANCE_RESULT_HAS_FAILED_CHECKS"

    result_id_seed = _first_present(request.get("closure_request_id"), conformance_id)
    result_id = f"{_safe_component(result_id_seed)}__source_body_reception_closure_result"
    non_claims = _build_non_claims(outcome)

    selected_source_body_surface = {
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_path": _first_present(
            request.get("selected_source_body_surface_path"),
            _value_at(surface, ("selected_source_body_surface_path",)),
            _value_at(surface, ("path",)),
        ),
        "selected_source_body_surface_reference": surface_reference,
        "source_body_identity_basis": _first_present(
            request.get("source_body_identity_basis"),
            _value_at(surface, ("source_body_identity_basis",)),
            _basis_value(request, selected, receipt_exhaustion, "source_body_identity_basis"),
        ),
        "source_body_lineage_basis": _first_present(
            request.get("source_body_lineage_basis"),
            _value_at(surface, ("source_body_lineage_basis",)),
            _basis_value(request, selected, receipt_exhaustion, "source_body_lineage_basis"),
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_source_body_surface_is_not_whole_body_by_default": True,
        "selected_source_body_surface_is_not_received": True,
        "selected_source_body_surface_is_not_adopted": True,
        "selected_source_body_surface_is_not_replaced": True,
        "selected_source_body_surface_is_not_validated_by_receiving_context": True,
        "selected_source_body_surface_is_not_invalidated_by_receiving_context": True,
        "raw_selected_source_body_surface": copy.deepcopy(surface),
    }

    receiving_context_section = {
        "receiving_context_id": receiving_context_id,
        "receiving_context_name": _first_present(
            _value_at(context, ("receiving_context_name",)),
            _value_at(context, ("name",)),
        ),
        "receiving_context_reference": _first_present(
            _value_at(context, ("receiving_context_reference",)),
            _value_at(context, ("reference",)),
        ),
        "receiving_context_type": receiving_context_type,
        "receiving_context_preserved": True,
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "receiving_context_is_not_receiver": True,
        "receiving_context_is_not_adopter": True,
        "receiving_context_is_not_validator": True,
        "receiving_context_is_not_invalidator": True,
        "receiving_context_is_not_operator": True,
        "receiving_context_did_not_validate_source": True,
        "receiving_context_did_not_invalidate_source": True,
        "receiving_context_did_not_create_governance": True,
        "receiving_context_did_not_create_operation_permission": True,
        "receiving_context_did_not_open_publication_flow": True,
        "raw_receiving_context": copy.deepcopy(context),
    }

    selected_conformance_result = {
        "selected_conformance_result_id": conformance_id,
        "selected_conformance_result_outcome": conformance_outcome,
        "selected_conformance_result_path": selected_path,
        "selected_conformance_outcome_is_passed": conformance_outcome
        == REQUIRED_CONFORMANCE_OUTCOME,
        "selected_conformance_result_failed_check_count": conformance_failed_count,
        "selected_conformance_result_failed_check_count_zero": conformance_failed_count
        == 0,
        "selected_conformance_result_preserved": selected is not None,
        "selected_conformance_result_recorded": _flag(
            request, selected, "source_body_reception_conformance_recorded", default=True
        ),
        "selected_conformance_result_passed": _flag(
            request, selected, "source_body_reception_conformance_passed", default=True
        ),
        "selected_receipt_exhaustion_result_preserved": receipt_exhaustion is not None,
        "selected_recognition_result_preserved": recognition is not None,
        "selected_non_capture_result_preserved": non_capture is not None,
        "selected_eligibility_result_preserved": eligibility is not None,
        "selected_receiving_context_role_result_preserved": receiving_role is not None,
        "selected_identity_preservation_result_preserved": identity is not None,
        "selected_reception_request_declaration_result_preserved": declaration is not None,
        "selected_source_body_surface_preserved": surface is not None,
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": context is not None,
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "source_body_reception_conformance_recorded": _flag(
            request, selected, "source_body_reception_conformance_recorded", default=True
        ),
        "source_body_reception_conformance_passed": _flag(
            request, selected, "source_body_reception_conformance_passed", default=True
        ),
        "conformance_remained_reception_chain_conformance_only": True,
        "conformance_did_not_authorize_reception": True,
        "conformance_did_not_receive_source": True,
        "conformance_did_not_record_source_receipt": True,
        "conformance_did_not_create_source_receipt": True,
        "conformance_did_not_claim_closure": True,
        "conformance_did_not_claim_final_completion": True,
        "conformance_did_not_authorize_continuation": True,
        "conformance_did_not_authorize_follow_on_work": True,
        "raw_selected_conformance_result": copy.deepcopy(selected),
    }

    closure_basis_section = {
        "selected_conformance_result": copy.deepcopy(selected),
        "selected_receipt_exhaustion_result": copy.deepcopy(receipt_exhaustion),
        "selected_recognition_result": copy.deepcopy(recognition),
        "selected_non_capture_result": copy.deepcopy(non_capture),
        "selected_eligibility_result": copy.deepcopy(eligibility),
        "selected_receiving_context_role_result": copy.deepcopy(receiving_role),
        "selected_identity_preservation_result": copy.deepcopy(identity),
        "selected_reception_request_declaration_result": copy.deepcopy(declaration),
        "selected_source_body_surface": copy.deepcopy(surface),
        "source_body_identity_basis": selected_source_body_surface["source_body_identity_basis"],
        "source_body_lineage_basis": selected_source_body_surface["source_body_lineage_basis"],
        "receiving_context": copy.deepcopy(context),
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": reception_purpose,
        "reception_limits": copy.deepcopy(reception_limits),
        "selected_receiving_context_role": copy.deepcopy(selected_receiving_context_role),
        "receiving_context_role_class": receiving_context_role_class,
        "receiving_context_role_limits": copy.deepcopy(receiving_context_role_limits),
        "conformance_basis": copy.deepcopy(conformance_basis),
        "conformance_limits": copy.deepcopy(conformance_limits),
        "closure_basis_as_supplied": copy.deepcopy(closure_basis),
        "reception_chain_closure_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "conformance_remained_reception_chain_conformance_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "source_receipt_remains_uncreated": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
        "closure_does_not_authorize_another_reception_request": True,
    }

    closure_limits_section = {
        "closure_limits_as_supplied": copy.deepcopy(closure_limits),
        "reception_chain_closure_only": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_does_not_receive_source": True,
        "closure_does_not_create_source_receipt": True,
        "closure_is_not_adoption": True,
        "closure_is_not_authority": True,
        "closure_is_not_currentness": True,
        "closure_is_not_validation": True,
        "closure_is_not_invalidation": True,
        "closure_is_not_operation_permission": True,
        "closure_is_not_publication_flow": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
    }

    closure_scope_section = {
        "selected_closure_scope_values": list(closure_scope_values),
        "unsupported_closure_scope_values": [
            value for value in closure_scope_values if value not in SUPPORTED_CLOSURE_SCOPE
        ],
        "all_selected_scope_values_supported": all(
            value in SUPPORTED_CLOSURE_SCOPE for value in closure_scope_values
        ),
        "supported_closure_scope_values": sorted(SUPPORTED_CLOSURE_SCOPE),
        "reception_chain_closure_only": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_does_not_receive_source": True,
        "closure_does_not_create_source_receipt": True,
        "closure_is_not_adoption": True,
        "closure_is_not_authority": True,
        "closure_is_not_currentness": True,
        "closure_is_not_validation": True,
        "closure_is_not_invalidation": True,
        "closure_is_not_operation_permission": True,
        "closure_is_not_publication_flow": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
    }

    recorded = outcome == OUTCOME_RECORDED
    closure_statement = {
        "source_body_reception_closure_recorded": recorded,
        "source_body_reception_boundary_chain_closed": recorded,
        "reception_closure_passed": recorded,
        "reception_family_closure_recorded": recorded,
        "selected_conformance_result_preserved": selected is not None,
        "selected_conformance_result_recorded": _flag(
            request, selected, "source_body_reception_conformance_recorded", default=True
        ),
        "selected_conformance_result_failed_check_count_zero": conformance_failed_count == 0,
        "selected_receipt_exhaustion_result_preserved": receipt_exhaustion is not None,
        "selected_recognition_result_preserved": recognition is not None,
        "selected_non_capture_result_preserved": non_capture is not None,
        "selected_eligibility_result_preserved": eligibility is not None,
        "selected_receiving_context_role_result_preserved": receiving_role is not None,
        "selected_identity_preservation_result_preserved": identity is not None,
        "selected_reception_request_declaration_result_preserved": declaration is not None,
        "selected_source_body_surface_preserved": surface is not None,
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": context is not None,
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "reception_chain_closure_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "conformance_remained_reception_chain_conformance_only": True,
        "closure_is_not_authorization": True,
        "closure_is_not_source_receipt": True,
        "closure_does_not_receive_source": True,
        "closure_does_not_create_source_receipt": True,
        "closure_is_not_final_completion": True,
        "closure_does_not_authorize_continuation": True,
        "closure_does_not_authorize_follow_on_work": True,
        "closure_does_not_create_reusable_permission": True,
        "closure_does_not_authorize_another_reception_request": True,
    }
    for key in REQUIRED_FALSE_NON_CLAIMS:
        closure_statement[key] = False

    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": copy.deepcopy(request.get("additional_basis_context"))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else None,
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }

    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": copy.deepcopy(request.get("not_recorded_basis"))
        if outcome == OUTCOME_NOT_RECORDED
        else None,
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_authorize": True,
        "not_recorded_does_not_receive": True,
        "not_recorded_does_not_record_source_receipt": True,
        "not_recorded_does_not_create_source_receipt": True,
        "not_recorded_does_not_replace": True,
        "not_recorded_does_not_validate": True,
        "not_recorded_does_not_invalidate": True,
        "not_recorded_does_not_create_currentness": True,
        "not_recorded_does_not_claim_final_completion": True,
        "not_recorded_does_not_authorize_follow_on_work": True,
        "not_recorded_does_not_create_reusable_permission": True,
        "not_recorded_does_not_authorize_another_reception_request": True,
    }

    result: dict[str, Any] = {
        "source_body_reception_closure_metadata": {
            "source_body_reception_closure_result_id": result_id,
            "source_body_reception_closure_result_type": "source_body_reception_closure_boundary_result",
            "source_body_reception_closure_result_version": RESULT_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_closure_question": {
            "closure_request_id": request.get("closure_request_id"),
            "closure_question": request.get("closure_question"),
            "closure_intent": request.get("closure_intent"),
            "declared_closure_request_path": request_path,
            "selected_conformance_result_id": conformance_id,
            "selected_conformance_result_outcome": conformance_outcome,
            "selected_source_body_surface_identifier": surface_identifier,
            "selected_source_body_surface_type": surface_type,
            "selected_source_body_surface_reference": surface_reference,
            "receiving_context_id": receiving_context_id,
            "receiving_context_type": receiving_context_type,
            "reception_class": reception_class,
            "reception_purpose": reception_purpose,
            "closure_is_not_authorization": True,
            "closure_is_not_source_receipt": True,
            "closure_does_not_decide_final_completion": True,
            "closure_does_not_authorize_continuation": True,
            "closure_does_not_authorize_follow_on_work": True,
            "closure_does_not_create_reusable_permission": True,
            "closure_does_not_authorize_another_reception_request": True,
        },
        "selected_conformance_result": selected_conformance_result,
        "selected_source_body_surface": selected_source_body_surface,
        "receiving_context": receiving_context_section,
        "closure_basis": closure_basis_section,
        "closure_limits": closure_limits_section,
        "closure_scope": closure_scope_section,
        "closure_checks": checks,
        "closure_statement": closure_statement,
        "closure_non_meaning": _build_closure_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason") or block_code),
    }
    result["source_body_reception_closure_summary"] = (
        build_source_body_reception_closure_summary(result)
    )
    result["source_body_reception_closure_summary"]["passed_check_count"] = passed_count
    result["source_body_reception_closure_summary"]["failed_check_count"] = failed_count
    return result


def resolve_source_body_reception_closure_boundary(
    declared_closure_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one declared source-body reception closure request."""

    if declared_closure_request is None:
        return _build_result({})
    if not isinstance(declared_closure_request, Mapping):
        return _build_result({}, request_malformed_code="DECLARED_CLOSURE_REQUEST_MALFORMED")
    return _build_result(copy.deepcopy(dict(declared_closure_request)))


def resolve_source_body_reception_closure_boundary_from_path(
    declared_closure_request_path: Path | str,
) -> dict[str, Any]:
    """Resolve a source-body reception closure request from a JSON object path."""

    path = Path(declared_closure_request_path)
    loaded, failure = _read_json_object(path)
    if failure == "unreadable":
        return _build_result(
            {"closure_question": "declared closure request unreadable"},
            request_path=str(path),
            request_malformed_code="DECLARED_CLOSURE_REQUEST_UNREADABLE",
        )
    if failure == "malformed":
        return _build_result(
            {"closure_question": "declared closure request malformed"},
            request_path=str(path),
            request_malformed_code="DECLARED_CLOSURE_REQUEST_MALFORMED",
        )
    if loaded is None:
        return _build_result(
            {"closure_question": "declared closure request unreadable"},
            request_path=str(path),
            request_malformed_code="DECLARED_CLOSURE_REQUEST_UNREADABLE",
        )
    return _build_result(copy.deepcopy(loaded), request_path=str(path))


def build_source_body_reception_closure_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build a compact summary for a closure boundary result."""

    statement = result.get("closure_statement", {})
    selected = result.get("selected_conformance_result", {})
    surface = result.get("selected_source_body_surface", {})
    context = result.get("receiving_context", {})
    declared = result.get("declared_closure_question", {})
    basis = result.get("closure_basis", {})
    block = result.get("block", {})
    checks = result.get("closure_checks", [])
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes)):
        passed_count = sum(
            1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True
        )
        failed_count = sum(
            1 for check in checks if isinstance(check, Mapping) and check.get("passed") is not True
        )
    else:
        passed_count = 0
        failed_count = 0
    outcome = result.get("outcome")
    non_claims = result.get("non_claims", {})
    return {
        "outcome": outcome,
        "block_code": block.get("block_code") if isinstance(block, Mapping) else None,
        "block_reason": block.get("block_reason") if isinstance(block, Mapping) else None,
        "closure_request_id": declared.get("closure_request_id")
        if isinstance(declared, Mapping)
        else None,
        "closure_question": declared.get("closure_question")
        if isinstance(declared, Mapping)
        else None,
        "closure_intent": declared.get("closure_intent")
        if isinstance(declared, Mapping)
        else None,
        "selected_conformance_result_id": selected.get("selected_conformance_result_id")
        if isinstance(selected, Mapping)
        else None,
        "selected_conformance_result_outcome": selected.get(
            "selected_conformance_result_outcome"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_source_body_surface_identifier": surface.get(
            "selected_source_body_surface_identifier"
        )
        if isinstance(surface, Mapping)
        else None,
        "selected_source_body_surface_type": surface.get(
            "selected_source_body_surface_type"
        )
        if isinstance(surface, Mapping)
        else None,
        "selected_source_body_surface_reference": surface.get(
            "selected_source_body_surface_reference"
        )
        if isinstance(surface, Mapping)
        else None,
        "receiving_context_id": context.get("receiving_context_id")
        if isinstance(context, Mapping)
        else None,
        "receiving_context_type": context.get("receiving_context_type")
        if isinstance(context, Mapping)
        else None,
        "reception_class": basis.get("reception_class")
        if isinstance(basis, Mapping)
        else None,
        "reception_purpose": basis.get("reception_purpose")
        if isinstance(basis, Mapping)
        else None,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "closure_recorded": bool(
            isinstance(statement, Mapping)
            and statement.get("source_body_reception_closure_recorded") is True
        ),
        "boundary_chain_closed": bool(
            isinstance(statement, Mapping)
            and statement.get("source_body_reception_boundary_chain_closed") is True
        ),
        "reception_closure_passed": bool(
            isinstance(statement, Mapping)
            and statement.get("reception_closure_passed") is True
        ),
        "reception_family_closure_recorded": bool(
            isinstance(statement, Mapping)
            and statement.get("reception_family_closure_recorded") is True
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_conformance_result_preserved": selected.get(
            "selected_conformance_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_conformance_result_recorded": selected.get(
            "selected_conformance_result_recorded"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_conformance_result_failed_check_count_zero": selected.get(
            "selected_conformance_result_failed_check_count_zero"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_receipt_exhaustion_result_preserved": selected.get(
            "selected_receipt_exhaustion_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_recognition_result_preserved": selected.get(
            "selected_recognition_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_non_capture_result_preserved": selected.get(
            "selected_non_capture_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_eligibility_result_preserved": selected.get(
            "selected_eligibility_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_receiving_context_role_result_preserved": selected.get(
            "selected_receiving_context_role_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_identity_preservation_result_preserved": selected.get(
            "selected_identity_preservation_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_request_declaration_result_preserved": selected.get(
            "selected_reception_request_declaration_result_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_source_body_surface_preserved": selected.get(
            "selected_source_body_surface_preserved"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_source_body_surface_remains_source": selected.get(
            "selected_source_body_surface_remains_source"
        )
        if isinstance(selected, Mapping)
        else None,
        "selected_surface_is_not_whole_body_by_default": selected.get(
            "selected_surface_is_not_whole_body_by_default"
        )
        if isinstance(selected, Mapping)
        else None,
        "receiving_context_preserved": selected.get("receiving_context_preserved")
        if isinstance(selected, Mapping)
        else None,
        "receiving_context_remains_context_only": selected.get(
            "receiving_context_remains_context_only"
        )
        if isinstance(selected, Mapping)
        else None,
        "receiving_context_is_not_source": selected.get("receiving_context_is_not_source")
        if isinstance(selected, Mapping)
        else None,
        "receiving_context_is_not_authority": selected.get(
            "receiving_context_is_not_authority"
        )
        if isinstance(selected, Mapping)
        else None,
        "receiving_context_is_not_current": selected.get("receiving_context_is_not_current")
        if isinstance(selected, Mapping)
        else None,
        "reception_chain_closure_only": statement.get("reception_chain_closure_only")
        if isinstance(statement, Mapping)
        else None,
        "request_declaration_remained_declaration_only": statement.get(
            "request_declaration_remained_declaration_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "identity_preservation_preserved_source_identity_only": statement.get(
            "identity_preservation_preserved_source_identity_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "receiving_context_role_remained_context_role_only": statement.get(
            "receiving_context_role_remained_context_role_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "eligibility_admissibility_remained_review_readiness_only": statement.get(
            "eligibility_admissibility_remained_review_readiness_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "non_capture_remained_refusal_check_outcome_only": statement.get(
            "non_capture_remained_refusal_check_outcome_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "recognition_remained_bounded_accounting_recognition_only": statement.get(
            "recognition_remained_bounded_accounting_recognition_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "receipt_exhaustion_remained_recognition_record_accounting_only": statement.get(
            "receipt_exhaustion_remained_recognition_record_accounting_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "conformance_reception_chain_only": statement.get(
            "conformance_remained_reception_chain_conformance_only"
        )
        if isinstance(statement, Mapping)
        else None,
        "closure_not_authorization": statement.get("closure_is_not_authorization")
        if isinstance(statement, Mapping)
        else None,
        "closure_not_source_receipt": statement.get("closure_is_not_source_receipt")
        if isinstance(statement, Mapping)
        else None,
        "closure_not_final_completion": statement.get("closure_is_not_final_completion")
        if isinstance(statement, Mapping)
        else None,
        "closure_not_continuation": statement.get(
            "closure_does_not_authorize_continuation"
        )
        if isinstance(statement, Mapping)
        else None,
        "closure_not_reusable_permission": statement.get(
            "closure_does_not_create_reusable_permission"
        )
        if isinstance(statement, Mapping)
        else None,
        "no_source_received": non_claims.get("source_received") is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_source_receipt_recorded": non_claims.get("source_receipt_recorded") is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_source_receipt_created": non_claims.get("source_receipt_created") is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_adoption_authority_currentness_standing": all(
            non_claims.get(key) is False
            for key in (
                "adoption_created",
                "authority_created",
                "currentness_created",
                "standing_created",
            )
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_vessel_derivative_relation": all(
            non_claims.get(key) is False
            for key in ("vessel_relation_created", "derivative_relation_created")
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_operation_permission_governance_publication_flow": all(
            non_claims.get(key) is False
            for key in (
                "operation_permission_created",
                "receiving_context_governance_created",
                "publication_flow_opened",
            )
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_public_readiness_final_completion_follow_on_work": all(
            non_claims.get(key) is False
            for key in (
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        )
        if isinstance(non_claims, Mapping)
        else None,
        "no_reusable_permission": non_claims.get("reusable_permission_created") is False
        if isinstance(non_claims, Mapping)
        else None,
        "no_another_reception_request_authorized": non_claims.get(
            "another_reception_request_authorized"
        )
        is False
        if isinstance(non_claims, Mapping)
        else None,
        "key_non_claims": copy.deepcopy(non_claims)
        if isinstance(non_claims, Mapping)
        else {},
    }


def write_source_body_reception_closure_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write a bounded additive closure result JSON artifact."""

    if not isinstance(result, Mapping):
        raise SourceBodyReceptionClosureBoundaryError("closure result must be a mapping")
    if output_path is None:
        metadata = result.get("source_body_reception_closure_metadata", {})
        result_id = (
            metadata.get("source_body_reception_closure_result_id")
            if isinstance(metadata, Mapping)
            else None
        )
        filename = f"{_safe_component(result_id)}.json"
        path = SOURCE_BODY_RECEPTION_CLOSURE_BOUNDARY_ROOT / filename
    else:
        path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    candidate = path
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix or ".json"
        index = 1
        while candidate.exists():
            candidate = candidate.with_name(f"{stem}_{index:03d}{suffix}")
            index += 1
    candidate.write_text(
        json.dumps(dict(result), indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_source_body_reception_closure_request(
    closure_request_id: str,
    closure_question: str,
    selected_conformance_result: Mapping[str, Any] | str,
    closure_basis: Mapping[str, Any] | str,
    closure_limits: Mapping[str, Any] | str,
    closure_scope: Sequence[str] | Mapping[str, Any],
    closure_intent: str = INTENT_RECORD,
    *,
    selected_conformance_result_path: str | None = None,
    selected_conformance_result_id: str | None = None,
    selected_conformance_result_outcome: str | None = None,
    requested_closure_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    """Build a declared closure request with required false non-claims."""

    request: dict[str, Any] = {
        "closure_request_id": closure_request_id,
        "closure_question": closure_question,
        "closure_intent": closure_intent,
        "closure_basis": copy.deepcopy(closure_basis),
        "closure_limits": copy.deepcopy(closure_limits),
        "closure_scope": copy.deepcopy(closure_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "requested_closure_outcome": requested_closure_outcome,
        "reception_authorized": False,
        "source_received": False,
        "source_receipt_recorded": False,
        "source_receipt_created": False,
        "adoption_created": False,
        "authority_created": False,
        "currentness_created": False,
        "standing_created": False,
        "standing_propagated": False,
        "vessel_relation_created": False,
        "derivative_relation_created": False,
        "operation_permission_created": False,
        "public_launch_readiness_created": False,
        "final_completion_claimed": False,
        "follow_on_work_authorized": False,
        "continuation_authorized": False,
        "publication_flow_opened": False,
        "reusable_permission_created": False,
        "another_reception_request_authorized": False,
    }
    if selected_conformance_result_path is not None:
        request["selected_conformance_result_path"] = selected_conformance_result_path
    elif isinstance(selected_conformance_result, Mapping):
        request["selected_conformance_result"] = copy.deepcopy(
            dict(selected_conformance_result)
        )
    else:
        request["selected_conformance_result"] = selected_conformance_result
    if selected_conformance_result_id is not None:
        request["selected_conformance_result_id"] = selected_conformance_result_id
    if selected_conformance_result_outcome is not None:
        request["selected_conformance_result_outcome"] = (
            selected_conformance_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = copy.deepcopy(additional_basis_context)
    if not_recorded_basis is not None:
        request["not_recorded_basis"] = copy.deepcopy(not_recorded_basis)
    return request
