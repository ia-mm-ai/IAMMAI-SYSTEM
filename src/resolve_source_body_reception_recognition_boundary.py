"""Resolve the source-body reception recognition boundary.

This module records bounded recognition of one non-capture-passed
source-body reception request / relation candidate for later
reception-family accounting. Recognition is not authorization, source
receipt, adoption, authority, currentness, operation permission,
receipt / exhaustion, conformance, or closure.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class SourceBodyReceptionRecognitionBoundaryError(Exception):
    """Raised for hard recognition-boundary path or shape failures."""


RESOLVER_MODULE = "resolve_source_body_reception_recognition_boundary"
RESULT_VERSION = "0.1.0"

SOURCE_BODY_RECEPTION_RECOGNITION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_recognition_boundary"
)

OUTCOME_RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED"
OUTCOME_NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECOGNITION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECOGNITION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_RECOGNITION_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

REQUIRED_NON_CAPTURE_OUTCOME = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_RECOGNITION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_RECOGNITION"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_RECOGNITION_REVIEW"
SUPPORTED_RECOGNITION_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_RECOGNITION_SCOPE = {
    "RECOGNITION_REVIEW_ONLY",
    "RECOGNITION_IS_NOT_AUTHORIZATION",
    "RECOGNITION_IS_NOT_SOURCE_RECEIPT",
    "RECOGNITION_IS_NOT_ADOPTION",
    "RECOGNITION_IS_NOT_AUTHORITY",
    "RECOGNITION_IS_NOT_CURRENTNESS",
    "RECOGNITION_IS_NOT_VALIDATION",
    "RECOGNITION_IS_NOT_INVALIDATION",
    "RECOGNITION_IS_NOT_OPERATION_PERMISSION",
    "RECOGNITION_IS_NOT_PUBLICATION_FLOW",
    "RECEIPT_EXHAUSTION_REQUIRES_SEPARATE_BOUNDARY",
    "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
}

REQUIRED_FALSE_NON_CLAIMS = (
    "reception_authorized",
    "source_received",
    "source_receipt_recorded",
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
    "receipt_exhaustion_passed",
    "reception_conformance_passed",
    "reception_closure_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "source_body_reception_recognition_recorded",
    "reception_recognized",
)

COLLAPSE_FIELD_CODES = (
    ("reception_authorized", "RECOGNITION_AUTHORIZES_RECEPTION"),
    ("source_received", "RECOGNITION_RECEIVES_SOURCE"),
    ("source_receipt_recorded", "RECOGNITION_CREATES_SOURCE_RECEIPT"),
    (
        "receiving_context_governance_created",
        "RECOGNITION_CREATES_GOVERNANCE",
    ),
    ("receiving_context_became_source", "RECOGNITION_TREATS_CONTEXT_AS_SOURCE"),
    (
        "receiving_context_became_authority",
        "RECOGNITION_TREATS_CONTEXT_AS_AUTHORITY",
    ),
    (
        "receiving_context_became_current",
        "RECOGNITION_TREATS_CONTEXT_AS_CURRENT",
    ),
    (
        "receiving_context_became_receiver",
        "RECOGNITION_TREATS_CONTEXT_AS_RECEIVER",
    ),
    (
        "receiving_context_became_adopter",
        "RECOGNITION_TREATS_CONTEXT_AS_ADOPTER",
    ),
    (
        "receiving_context_became_validator",
        "RECOGNITION_TREATS_CONTEXT_AS_VALIDATOR",
    ),
    (
        "receiving_context_became_invalidator",
        "RECOGNITION_TREATS_CONTEXT_AS_INVALIDATOR",
    ),
    (
        "receiving_context_became_operator",
        "RECOGNITION_TREATS_CONTEXT_AS_OPERATOR",
    ),
    (
        "source_validated_by_receiving_context",
        "RECOGNITION_VALIDATES_SOURCE",
    ),
    (
        "source_invalidated_by_receiving_context",
        "RECOGNITION_INVALIDATES_SOURCE",
    ),
    ("source_replaced", "RECOGNITION_REPLACES_SOURCE"),
    ("adoption_created", "RECOGNITION_CREATES_ADOPTION"),
    ("authority_created", "RECOGNITION_CREATES_AUTHORITY"),
    ("currentness_created", "RECOGNITION_CREATES_CURRENTNESS"),
    ("standing_created", "RECOGNITION_CREATES_STANDING"),
    ("standing_propagated", "RECOGNITION_CREATES_STANDING_PROPAGATION"),
    ("vessel_relation_created", "RECOGNITION_CREATES_VESSEL_RELATION"),
    (
        "derivative_relation_created",
        "RECOGNITION_CREATES_DERIVATIVE_RELATION",
    ),
    (
        "operation_permission_created",
        "RECOGNITION_CREATES_OPERATION_PERMISSION",
    ),
    (
        "public_launch_readiness_created",
        "RECOGNITION_CREATES_PUBLIC_READINESS",
    ),
    ("final_completion_claimed", "RECOGNITION_CLAIMS_FINAL_COMPLETION"),
    ("follow_on_work_authorized", "RECOGNITION_AUTHORIZES_FOLLOW_ON_WORK"),
    ("continuation_authorized", "RECOGNITION_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "RECOGNITION_OPENS_PUBLICATION_FLOW"),
    (
        "receipt_exhaustion_passed",
        "RECOGNITION_CLAIMS_RECEIPT_EXHAUSTION_PASSED",
    ),
    (
        "reception_conformance_passed",
        "RECOGNITION_CLAIMS_CONFORMANCE_PASSED",
    ),
    ("reception_closure_passed", "RECOGNITION_CLAIMS_CLOSURE_PASSED"),
)


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str) and not value.strip():
        return False
    if isinstance(value, (Sequence, Mapping)) and not isinstance(value, str):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "passed", "recorded"}
    return bool(value)


def _value_at(mapping: Any, *path: str) -> Any:
    current = mapping
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


def _deepcopy_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return copy.deepcopy(dict(value))
    return {}


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    json_path = Path(path)
    try:
        with json_path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except FileNotFoundError:
        return None, "unreadable"
    except OSError:
        return None, "unreadable"
    except json.JSONDecodeError:
        return None, "malformed"
    if not isinstance(payload, Mapping):
        return None, "malformed"
    return copy.deepcopy(dict(payload)), None


def _failed_check_count(result: Mapping[str, Any]) -> int | None:
    explicit = _first_present(
        _value_at(result, "failed_check_count"),
        _value_at(result, "source_body_reception_non_capture_summary", "failed_check_count"),
        _value_at(result, "summary", "failed_check_count"),
    )
    if isinstance(explicit, int):
        return explicit
    checks = _first_present(
        _value_at(result, "non_capture_checks"),
        _value_at(result, "checks"),
    )
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes)):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and not _truthy(check.get("passed"))
        )
    return None


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, Mapping):
        raw = _first_present(
            scope.get("selected_recognition_scope_values"),
            scope.get("recognition_scope_values"),
            scope.get("scope_values"),
            scope.get("values"),
        )
        if raw is None:
            raw = [key for key, value in scope.items() if _truthy(value)]
    else:
        raw = scope
    if isinstance(raw, str):
        return [raw]
    if isinstance(raw, Sequence) and not isinstance(raw, (str, bytes)):
        return [str(value) for value in raw]
    return []


def _contains_truthy_key(value: Any, key: str) -> bool:
    if isinstance(value, Mapping):
        for map_key, map_value in value.items():
            if map_key == key and _truthy(map_value):
                return True
            if _contains_truthy_key(map_value, key):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        return any(_contains_truthy_key(item, key) for item in value)
    return False


def _safe_component(value: Any, fallback: str) -> str:
    raw = str(value or fallback).strip() or fallback
    safe = "".join(char if char.isalnum() or char in "-_." else "_" for char in raw)
    return safe[:180] or fallback


def _check(
    check_name: str,
    passed: bool,
    expected_posture: str,
    actual_posture: Any,
    block_code: str | None = None,
    failure_code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None if passed else block_code,
        "failure_code": None if passed else failure_code,
    }


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {
        "blocked": code is not None,
        "block_code": code,
        "block_reason": reason,
    }


def _load_selected_non_capture_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    result_path = request.get("selected_non_capture_result_path")
    if _present(result_path):
        loaded, error = _read_json_object(str(result_path))
        if error == "unreadable":
            return None, str(result_path), "NON_CAPTURE_RESULT_UNREADABLE"
        if error == "malformed":
            return None, str(result_path), "NON_CAPTURE_RESULT_MALFORMED"
        return loaded, str(result_path), None
    selected = request.get("selected_non_capture_result")
    if isinstance(selected, Mapping):
        return copy.deepcopy(dict(selected)), None, None
    if _present(selected):
        return None, None, "NON_CAPTURE_RESULT_MALFORMED"
    return None, None, None


def _extract_non_capture_outcome(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_non_capture_result_outcome"),
        request.get("expected_selected_non_capture_outcome"),
        selected.get("outcome"),
        _value_at(selected, "source_body_reception_non_capture_summary", "outcome"),
        _value_at(selected, "non_capture_statement", "outcome"),
    )


def _extract_non_capture_id(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_non_capture_result_id"),
        _value_at(
            selected,
            "source_body_reception_non_capture_metadata",
            "source_body_reception_non_capture_result_id",
        ),
        _value_at(
            selected,
            "source_body_reception_non_capture_summary",
            "source_body_reception_non_capture_result_id",
        ),
        selected.get("source_body_reception_non_capture_result_id"),
        selected.get("non_capture_request_id"),
        _value_at(selected, "declared_non_capture_question", "non_capture_request_id"),
    )


def _nested_selected_eligibility(selected: Mapping[str, Any]) -> Any:
    return _first_present(
        _value_at(selected, "non_capture_basis", "selected_eligibility_result"),
        _value_at(selected, "selected_eligibility_result", "raw_selected_eligibility_result"),
        selected.get("selected_eligibility_result"),
    )


def _nested_role_result(selected: Mapping[str, Any], eligibility: Any) -> Any:
    return _first_present(
        _value_at(selected, "non_capture_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "eligibility_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "selected_receiving_context_role_result"),
        _value_at(eligibility, "selected_receiving_context_role_result", "raw_result"),
    )


def _nested_identity_result(
    selected: Mapping[str, Any], eligibility: Any, role_result: Any
) -> Any:
    return _first_present(
        _value_at(selected, "non_capture_basis", "selected_identity_preservation_result"),
        _value_at(eligibility, "eligibility_basis", "selected_identity_preservation_result"),
        _value_at(role_result, "receiving_context_role_basis", "selected_identity_preservation_result"),
        _value_at(role_result, "selected_identity_preservation_result"),
    )


def _nested_request_declaration(
    selected: Mapping[str, Any],
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        _value_at(
            selected,
            "non_capture_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            eligibility,
            "eligibility_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            role_result,
            "receiving_context_role_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            identity_result,
            "identity_preservation_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(identity_result, "selected_reception_request_declaration_result"),
    )


def _nested_surface(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        request.get("selected_source_body_surface"),
        _value_at(selected, "non_capture_basis", "selected_source_body_surface"),
        _value_at(selected, "selected_source_body_surface", "selected_source_body_surface"),
        selected.get("selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface"),
        _value_at(role_result, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(identity_result, "selected_source_body_surface", "selected_source_body_surface"),
    )


def _nested_receiving_context(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    eligibility: Any,
    role_result: Any,
) -> Any:
    return _first_present(
        request.get("receiving_context"),
        _value_at(selected, "non_capture_basis", "receiving_context"),
        _value_at(selected, "receiving_context", "receiving_context"),
        selected.get("receiving_context"),
        _value_at(eligibility, "receiving_context", "receiving_context"),
        _value_at(eligibility, "receiving_context"),
        _value_at(role_result, "receiving_context", "receiving_context"),
        _value_at(role_result, "receiving_context"),
    )


def _surface_identifier(request: Mapping[str, Any], surface: Any) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_identifier"),
        _value_at(surface, "selected_source_body_surface_identifier"),
        _value_at(surface, "source_body_surface_identifier"),
        _value_at(surface, "identifier"),
        _value_at(surface, "id"),
    )


def _surface_type(request: Mapping[str, Any], surface: Any) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_type"),
        _value_at(surface, "selected_source_body_surface_type"),
        _value_at(surface, "source_body_surface_type"),
        _value_at(surface, "type"),
    )


def _surface_reference(request: Mapping[str, Any], surface: Any) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_reference"),
        request.get("selected_source_body_surface_path"),
        _value_at(surface, "selected_source_body_surface_reference"),
        _value_at(surface, "selected_source_body_surface_path"),
        _value_at(surface, "reference"),
        _value_at(surface, "path"),
    )


def _context_id(request: Mapping[str, Any], context: Any) -> Any:
    return _first_present(
        request.get("receiving_context_id"),
        _value_at(context, "receiving_context_id"),
        _value_at(context, "id"),
        _value_at(context, "name"),
        _value_at(context, "reference"),
    )


def _context_type(request: Mapping[str, Any], context: Any, selected: Mapping[str, Any]) -> Any:
    return _first_present(
        request.get("receiving_context_type"),
        _value_at(context, "receiving_context_type"),
        _value_at(context, "type"),
        _value_at(selected, "non_capture_basis", "receiving_context_type"),
        _value_at(selected, "source_body_reception_non_capture_summary", "receiving_context_type"),
    )


def _preserved_flag(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
    key: str,
    default: bool = False,
) -> bool:
    value = _first_present(
        request.get(key),
        _value_at(selected, "non_capture_statement", key),
        _value_at(selected, "selected_non_capture_result", key),
        _value_at(selected, "selected_eligibility_result", key),
        _value_at(selected, "source_body_reception_non_capture_summary", key),
        _value_at(selected, "non_claims", key),
        selected.get(key),
    )
    if value is None:
        return default
    return _truthy(value)


def _required_non_claims_false(request: Mapping[str, Any]) -> bool:
    non_claims = request.get("declared_non_claims")
    if not isinstance(non_claims, Mapping):
        return False
    return all(key in non_claims and non_claims[key] is False for key in REQUIRED_FALSE_NON_CLAIMS)


def _collapse_code(request: Mapping[str, Any], selected: Mapping[str, Any] | None) -> str | None:
    scan_targets: list[Any] = [request]
    if isinstance(selected, Mapping):
        scan_targets.append(selected)
    for key, code in COLLAPSE_FIELD_CODES:
        if any(_contains_truthy_key(target, key) for target in scan_targets):
            return code
    if any(
        _contains_truthy_key(target, key)
        for target in scan_targets
        for key in ("mutation_performed", "replay_performed", "merge_performed")
    ):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    return None


def _build_non_claims(recorded: bool) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims.update(
        {
            "source_body_reception_recognition_recorded": bool(recorded),
            "reception_recognized": bool(recorded),
        }
    )
    return non_claims


def _build_recognition_non_meaning() -> dict[str, bool]:
    meanings = (
        "reception_authorized",
        "source_received",
        "source_receipt_recorded",
        "source_adopted",
        "source_validated",
        "source_invalidated",
        "source_replaced",
        "receiving_context_became_source",
        "receiving_context_became_authority",
        "receiving_context_became_current",
        "receiving_context_became_receiver",
        "receiving_context_became_adopter",
        "receiving_context_became_validator",
        "receiving_context_became_invalidator",
        "receiving_context_became_operator",
        "receiving_context_governance_created",
        "standing_created",
        "standing_propagated",
        "vessel_relation_created",
        "derivative_relation_created",
        "operation_permission_created",
        "receipt_exhaustion_completed",
        "conformance_passed",
        "closure_recorded",
        "public_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
        "continuation_authorized",
        "publication_flow_opened",
    )
    result = {f"does_not_mean_{name}": True for name in meanings}
    result["recognition_is_not_authorization"] = True
    result["recognition_is_not_source_receipt"] = True
    result["recognition_is_not_adoption"] = True
    result["recognition_is_not_currentness"] = True
    result["recognition_is_not_operation_permission"] = True
    return result


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "source-body reception recognition test",
            "source-body reception recognition live artifact",
            "source-body reception receipt / exhaustion boundary",
            "source-body reception conformance boundary",
            "source-body reception closure boundary",
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
        ],
        "open_means_not_scheduled": True,
        "open_means_not_authorized": True,
        "open_means_not_executed": True,
    }


def _determine_block_code(
    request: Mapping[str, Any],
    selected_non_capture: Mapping[str, Any] | None,
    selected_non_capture_path: str | None,
    selected_load_code: str | None,
    selected_non_capture_outcome: Any,
    selected_non_capture_failed_count: int | None,
    selected_eligibility_result: Any,
    selected_receiving_context_role_result: Any,
    selected_identity_preservation_result: Any,
    selected_request_declaration_result: Any,
    selected_source_body_surface: Any,
    receiving_context: Any,
    receiving_context_type: Any,
    reception_class: Any,
    reception_purpose: Any,
    reception_limits: Any,
    recognition_basis: Any,
    recognition_limits: Any,
    unsupported_scope: Sequence[str],
) -> str | None:
    if not _present(request.get("recognition_question")):
        return "RECOGNITION_QUESTION_UNDECLARED"
    if request.get("recognition_intent") == INTENT_BLOCK:
        return "RECOGNITION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if request.get("recognition_intent") not in SUPPORTED_RECOGNITION_INTENTS:
        return "RECOGNITION_INTENT_UNSUPPORTED"
    if selected_load_code:
        return selected_load_code
    if not _present(selected_non_capture):
        return "NON_CAPTURE_RESULT_MISSING"
    if selected_non_capture_path and not isinstance(selected_non_capture, Mapping):
        return "NON_CAPTURE_RESULT_MALFORMED"
    if not _present(selected_non_capture_outcome):
        return "NON_CAPTURE_RESULT_OUTCOME_MISSING"
    if selected_non_capture_outcome != REQUIRED_NON_CAPTURE_OUTCOME:
        return "NON_CAPTURE_RESULT_NOT_PASSED"
    if selected_non_capture_failed_count not in (0, None):
        return "NON_CAPTURE_RESULT_HAS_FAILED_CHECKS"
    if selected_non_capture_failed_count is None:
        return "NON_CAPTURE_RESULT_HAS_FAILED_CHECKS"
    if not _present(selected_eligibility_result):
        return "ELIGIBILITY_RESULT_MISSING"
    if not _present(selected_receiving_context_role_result):
        return "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"
    if not _present(selected_identity_preservation_result):
        return "IDENTITY_PRESERVATION_RESULT_MISSING"
    if not _present(selected_request_declaration_result):
        return "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING"
    if not _present(selected_source_body_surface):
        return "SELECTED_SOURCE_BODY_SURFACE_MISSING"
    if not isinstance(selected_source_body_surface, Mapping):
        return "SELECTED_SOURCE_BODY_SURFACE_MALFORMED"
    if not _present(receiving_context):
        return "RECEIVING_CONTEXT_MISSING"
    if not isinstance(receiving_context, Mapping):
        return "RECEIVING_CONTEXT_MALFORMED"
    if not _present(receiving_context_type):
        return "RECEIVING_CONTEXT_TYPE_MISSING"
    if not _present(reception_class):
        return "RECEPTION_CLASS_MISSING"
    if not _present(reception_purpose):
        return "RECEPTION_PURPOSE_MISSING"
    if not _present(reception_limits):
        return "RECEPTION_LIMITS_MISSING"
    if not _present(recognition_basis):
        return "RECOGNITION_BASIS_MISSING"
    if not _present(recognition_limits):
        return "RECOGNITION_LIMITS_MISSING"
    if unsupported_scope:
        return "UNSUPPORTED_RECOGNITION_SCOPE"
    collapse = _collapse_code(request, selected_non_capture)
    if collapse:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    block_code: str | None,
    request: Mapping[str, Any],
    selected_non_capture: Mapping[str, Any] | None,
    selected_non_capture_outcome: Any,
    selected_non_capture_failed_count: int | None,
    selected_eligibility_result: Any,
    selected_receiving_context_role_result: Any,
    selected_identity_preservation_result: Any,
    selected_request_declaration_result: Any,
    selected_source_body_surface: Any,
    receiving_context: Any,
    receiving_context_type: Any,
    recognition_basis: Any,
    recognition_limits: Any,
    unsupported_scope: Sequence[str],
) -> list[dict[str, Any]]:
    selected = selected_non_capture or {}
    checks = [
        _check(
            "recognition_question_declared",
            _present(request.get("recognition_question")),
            "recognition question declared",
            request.get("recognition_question"),
            "RECOGNITION_QUESTION_UNDECLARED",
        ),
        _check(
            "recognition_intent_supported",
            request.get("recognition_intent") in SUPPORTED_RECOGNITION_INTENTS
            and request.get("recognition_intent") != INTENT_BLOCK,
            "recognition intent records bounded recognition review",
            request.get("recognition_intent"),
            "RECOGNITION_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected_non_capture_result_present",
            _present(selected_non_capture),
            "selected non-capture result present",
            _present(selected_non_capture),
            "NON_CAPTURE_RESULT_MISSING",
        ),
        _check(
            "selected_non_capture_outcome_declared",
            _present(selected_non_capture_outcome),
            "selected non-capture outcome declared",
            selected_non_capture_outcome,
            "NON_CAPTURE_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_non_capture_outcome_passed",
            selected_non_capture_outcome == REQUIRED_NON_CAPTURE_OUTCOME,
            REQUIRED_NON_CAPTURE_OUTCOME,
            selected_non_capture_outcome,
            "NON_CAPTURE_RESULT_NOT_PASSED",
        ),
        _check(
            "selected_non_capture_failed_check_count_zero",
            selected_non_capture_failed_count == 0,
            "selected non-capture failed check count is zero",
            selected_non_capture_failed_count,
            "NON_CAPTURE_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected_eligibility_result_preserved",
            _present(selected_eligibility_result)
            and _preserved_flag(selected, request, "selected_eligibility_result_preserved", True),
            "selected eligibility / admissibility result preserved",
            _present(selected_eligibility_result),
            "ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "selected_receiving_context_role_result_preserved",
            _present(selected_receiving_context_role_result)
            and _preserved_flag(
                selected,
                request,
                "selected_receiving_context_role_result_preserved",
                True,
            ),
            "selected receiving-context role result preserved",
            _present(selected_receiving_context_role_result),
            "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected_identity_preservation_result_preserved",
            _present(selected_identity_preservation_result)
            and _preserved_flag(
                selected,
                request,
                "selected_identity_preservation_result_preserved",
                True,
            ),
            "selected identity preservation result preserved",
            _present(selected_identity_preservation_result),
            "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected_request_declaration_result_preserved",
            _present(selected_request_declaration_result)
            and _preserved_flag(
                selected,
                request,
                "selected_reception_request_declaration_result_preserved",
                True,
            ),
            "selected request declaration result preserved",
            _present(selected_request_declaration_result),
            "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
        ),
        _check(
            "selected_source_body_surface_preserved",
            isinstance(selected_source_body_surface, Mapping)
            and _preserved_flag(selected, request, "selected_source_body_surface_preserved", True),
            "selected source-body surface preserved",
            _present(selected_source_body_surface),
            "SELECTED_SOURCE_BODY_SURFACE_MISSING",
        ),
        _check(
            "selected_source_body_surface_remains_source",
            _preserved_flag(selected, request, "selected_source_body_surface_remains_source", True),
            "selected source-body surface remains source",
            _preserved_flag(selected, request, "selected_source_body_surface_remains_source", True),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "selected_surface_is_not_whole_body_by_default",
            _preserved_flag(
                selected,
                request,
                "selected_surface_is_not_whole_body_by_default",
                True,
            ),
            "selected surface is not whole body by default",
            _preserved_flag(
                selected,
                request,
                "selected_surface_is_not_whole_body_by_default",
                True,
            ),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "receiving_context_preserved",
            isinstance(receiving_context, Mapping)
            and _preserved_flag(selected, request, "receiving_context_preserved", True),
            "receiving context preserved",
            _present(receiving_context),
            "RECEIVING_CONTEXT_MISSING",
        ),
        _check(
            "receiving_context_remains_context_only",
            _preserved_flag(selected, request, "receiving_context_remains_context_only", True),
            "receiving context remains context only",
            _preserved_flag(selected, request, "receiving_context_remains_context_only", True),
            "RECEIVING_CONTEXT_MALFORMED",
        ),
        _check(
            "receiving_context_is_not_source",
            _preserved_flag(selected, request, "receiving_context_is_not_source", True),
            "receiving context is not source",
            _preserved_flag(selected, request, "receiving_context_is_not_source", True),
            "RECOGNITION_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving_context_is_not_authority",
            _preserved_flag(selected, request, "receiving_context_is_not_authority", True),
            "receiving context is not authority",
            _preserved_flag(selected, request, "receiving_context_is_not_authority", True),
            "RECOGNITION_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving_context_is_not_current",
            _preserved_flag(selected, request, "receiving_context_is_not_current", True),
            "receiving context is not current",
            _preserved_flag(selected, request, "receiving_context_is_not_current", True),
            "RECOGNITION_TREATS_CONTEXT_AS_CURRENT",
        ),
        _check(
            "eligibility_admissibility_review_readiness_only",
            _preserved_flag(
                selected,
                request,
                "eligibility_admissibility_is_review_readiness_only",
                True,
            ),
            "eligibility / admissibility remains review-readiness only",
            _preserved_flag(
                selected,
                request,
                "eligibility_admissibility_is_review_readiness_only",
                True,
            ),
            "ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "non_capture_passed_refusal_check_only",
            _preserved_flag(
                selected,
                request,
                "non_capture_passed_as_refusal_check_outcome_only",
                True,
            )
            or _truthy(_value_at(selected, "non_capture_statement", "non_capture_passed")),
            "non-capture passed as refusal/check outcome only",
            True,
        ),
        _check(
            "non_adoption_passed_refusal_check_only",
            _preserved_flag(
                selected,
                request,
                "non_adoption_passed_as_refusal_check_outcome_only",
                True,
            )
            or _truthy(_value_at(selected, "non_capture_statement", "non_adoption_passed")),
            "non-adoption passed as refusal/check outcome only",
            True,
        ),
        _check(
            "non_currentness_passed_refusal_check_only",
            _preserved_flag(
                selected,
                request,
                "non_currentness_passed_as_refusal_check_outcome_only",
                True,
            )
            or _truthy(_value_at(selected, "non_capture_statement", "non_currentness_passed")),
            "non-currentness passed as refusal/check outcome only",
            True,
        ),
        _check(
            "recognition_basis_declared",
            _present(recognition_basis),
            "recognition basis declared",
            recognition_basis,
            "RECOGNITION_BASIS_MISSING",
        ),
        _check(
            "recognition_limits_declared",
            _present(recognition_limits),
            "recognition limits declared",
            recognition_limits,
            "RECOGNITION_LIMITS_MISSING",
        ),
        _check(
            "recognition_scope_supported",
            not unsupported_scope,
            "all selected recognition scope values supported",
            list(unsupported_scope),
            "UNSUPPORTED_RECOGNITION_SCOPE",
        ),
        _check(
            "recognition_is_not_authorization",
            not _contains_truthy_key(request, "reception_authorized"),
            "recognition is not authorization",
            request.get("reception_authorized"),
            "RECOGNITION_AUTHORIZES_RECEPTION",
        ),
        _check(
            "recognition_does_not_receive_source",
            not _contains_truthy_key(request, "source_received"),
            "recognition does not receive source",
            request.get("source_received"),
            "RECOGNITION_RECEIVES_SOURCE",
        ),
        _check(
            "recognition_does_not_create_source_receipt",
            not _contains_truthy_key(request, "source_receipt_recorded"),
            "recognition does not create source receipt",
            request.get("source_receipt_recorded"),
            "RECOGNITION_CREATES_SOURCE_RECEIPT",
        ),
        _check(
            "recognition_does_not_create_adoption",
            not _contains_truthy_key(request, "adoption_created"),
            "recognition does not create adoption",
            request.get("adoption_created"),
            "RECOGNITION_CREATES_ADOPTION",
        ),
        _check(
            "recognition_does_not_create_authority",
            not _contains_truthy_key(request, "authority_created"),
            "recognition does not create authority",
            request.get("authority_created"),
            "RECOGNITION_CREATES_AUTHORITY",
        ),
        _check(
            "recognition_does_not_create_currentness",
            not _contains_truthy_key(request, "currentness_created"),
            "recognition does not create currentness",
            request.get("currentness_created"),
            "RECOGNITION_CREATES_CURRENTNESS",
        ),
        _check(
            "recognition_does_not_validate_source",
            not _contains_truthy_key(request, "source_validated_by_receiving_context"),
            "recognition does not validate source",
            request.get("source_validated_by_receiving_context"),
            "RECOGNITION_VALIDATES_SOURCE",
        ),
        _check(
            "recognition_does_not_invalidate_source",
            not _contains_truthy_key(request, "source_invalidated_by_receiving_context"),
            "recognition does not invalidate source",
            request.get("source_invalidated_by_receiving_context"),
            "RECOGNITION_INVALIDATES_SOURCE",
        ),
        _check(
            "recognition_does_not_replace_source",
            not _contains_truthy_key(request, "source_replaced"),
            "recognition does not replace source",
            request.get("source_replaced"),
            "RECOGNITION_REPLACES_SOURCE",
        ),
        _check(
            "recognition_does_not_create_operation_permission",
            not _contains_truthy_key(request, "operation_permission_created"),
            "recognition does not create operation permission",
            request.get("operation_permission_created"),
            "RECOGNITION_CREATES_OPERATION_PERMISSION",
        ),
        _check(
            "recognition_does_not_create_governance",
            not _contains_truthy_key(request, "receiving_context_governance_created"),
            "recognition does not create governance",
            request.get("receiving_context_governance_created"),
            "RECOGNITION_CREATES_GOVERNANCE",
        ),
        _check(
            "recognition_does_not_open_publication_flow",
            not _contains_truthy_key(request, "publication_flow_opened"),
            "recognition does not open publication flow",
            request.get("publication_flow_opened"),
            "RECOGNITION_OPENS_PUBLICATION_FLOW",
        ),
        _check(
            "recognition_does_not_create_public_readiness",
            not _contains_truthy_key(request, "public_launch_readiness_created"),
            "recognition does not create public readiness",
            request.get("public_launch_readiness_created"),
            "RECOGNITION_CREATES_PUBLIC_READINESS",
        ),
        _check(
            "recognition_does_not_claim_final_completion",
            not _contains_truthy_key(request, "final_completion_claimed"),
            "recognition does not claim final completion",
            request.get("final_completion_claimed"),
            "RECOGNITION_CLAIMS_FINAL_COMPLETION",
        ),
        _check(
            "recognition_does_not_authorize_continuation",
            not _contains_truthy_key(request, "continuation_authorized"),
            "recognition does not authorize continuation",
            request.get("continuation_authorized"),
            "RECOGNITION_AUTHORIZES_CONTINUATION",
        ),
        _check(
            "recognition_does_not_authorize_follow_on_work",
            not _contains_truthy_key(request, "follow_on_work_authorized"),
            "recognition does not authorize follow-on work",
            request.get("follow_on_work_authorized"),
            "RECOGNITION_AUTHORIZES_FOLLOW_ON_WORK",
        ),
        _check(
            "receipt_exhaustion_remains_future_work",
            not _contains_truthy_key(request, "receipt_exhaustion_passed"),
            "receipt / exhaustion remains future work",
            request.get("receipt_exhaustion_passed"),
            "RECOGNITION_CLAIMS_RECEIPT_EXHAUSTION_PASSED",
        ),
        _check(
            "conformance_remains_future_work",
            not _contains_truthy_key(request, "reception_conformance_passed"),
            "conformance remains future work",
            request.get("reception_conformance_passed"),
            "RECOGNITION_CLAIMS_CONFORMANCE_PASSED",
        ),
        _check(
            "closure_remains_future_work",
            not _contains_truthy_key(request, "reception_closure_passed"),
            "closure remains future work",
            request.get("reception_closure_passed"),
            "RECOGNITION_CLAIMS_CLOSURE_PASSED",
        ),
        _check(
            "no_mutation_replay_merge",
            not any(
                _contains_truthy_key(request, key)
                for key in ("mutation_performed", "replay_performed", "merge_performed")
            ),
            "no mutation, replay, or merge",
            {
                "mutation_performed": request.get("mutation_performed"),
                "replay_performed": request.get("replay_performed"),
                "merge_performed": request.get("merge_performed"),
            },
            "MUTATION_REPLAY_OR_MERGE_DETECTED",
        ),
        _check(
            "non_claims_remain_false",
            _required_non_claims_false(request),
            "required recognition non-claims explicit and false",
            request.get("declared_non_claims"),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        ),
    ]
    if block_code:
        for check in checks:
            if check.get("block_code") == block_code:
                check["passed"] = False
                check["actual_posture"] = block_code
                break
    return checks


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
) -> dict[str, Any]:
    selected_non_capture, selected_non_capture_path, selected_load_code = (
        _load_selected_non_capture_result(request)
    )
    selected_non_capture_dict = selected_non_capture or {}
    selected_non_capture_outcome = _extract_non_capture_outcome(
        request, selected_non_capture
    )
    selected_non_capture_id = _extract_non_capture_id(request, selected_non_capture)
    selected_non_capture_failed_count = (
        _failed_check_count(selected_non_capture_dict)
        if selected_non_capture is not None
        else None
    )

    selected_eligibility_result = _first_present(
        request.get("selected_eligibility_result"),
        _nested_selected_eligibility(selected_non_capture_dict),
    )
    selected_receiving_context_role_result = _first_present(
        request.get("selected_receiving_context_role_result"),
        _nested_role_result(selected_non_capture_dict, selected_eligibility_result),
    )
    selected_identity_preservation_result = _first_present(
        request.get("selected_identity_preservation_result"),
        _nested_identity_result(
            selected_non_capture_dict,
            selected_eligibility_result,
            selected_receiving_context_role_result,
        ),
    )
    selected_request_declaration_result = _first_present(
        request.get("selected_reception_request_declaration_result"),
        _nested_request_declaration(
            selected_non_capture_dict,
            selected_eligibility_result,
            selected_receiving_context_role_result,
            selected_identity_preservation_result,
        ),
    )
    selected_source_body_surface = _nested_surface(
        request,
        selected_non_capture_dict,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
    )
    receiving_context = _nested_receiving_context(
        request,
        selected_non_capture_dict,
        selected_eligibility_result,
        selected_receiving_context_role_result,
    )

    receiving_context_type = _context_type(
        request, receiving_context, selected_non_capture_dict
    )
    reception_class = _first_present(
        request.get("reception_class"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "reception_class"),
        _value_at(
            selected_non_capture_dict,
            "source_body_reception_non_capture_summary",
            "reception_class",
        ),
    )
    reception_purpose = _first_present(
        request.get("reception_purpose"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "reception_purpose"),
        _value_at(
            selected_non_capture_dict,
            "source_body_reception_non_capture_summary",
            "reception_purpose",
        ),
    )
    reception_limits = _first_present(
        request.get("reception_limits"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "reception_limits"),
    )
    selected_receiving_context_role = _first_present(
        request.get("selected_receiving_context_role"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "selected_receiving_context_role",
        ),
    )
    receiving_context_role_class = _first_present(
        request.get("receiving_context_role_class"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "receiving_context_role_class",
        ),
    )
    receiving_context_role_limits = _first_present(
        request.get("receiving_context_role_limits"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "receiving_context_role_limits",
        ),
    )
    eligibility_basis = _first_present(
        request.get("eligibility_basis"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "eligibility_basis"),
    )
    admissibility_basis = _first_present(
        request.get("admissibility_basis"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "admissibility_basis"),
    )
    review_readiness_limits = _first_present(
        request.get("review_readiness_limits"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "review_readiness_limits",
        ),
    )
    non_capture_basis = _first_present(
        request.get("non_capture_basis"),
        _value_at(selected_non_capture_dict, "non_capture_basis", "non_capture_basis"),
        selected_non_capture_dict.get("non_capture_basis"),
    )
    non_adoption_basis = _first_present(
        request.get("non_adoption_basis"),
        selected_non_capture_dict.get("non_adoption_basis"),
    )
    non_currentness_basis = _first_present(
        request.get("non_currentness_basis"),
        selected_non_capture_dict.get("non_currentness_basis"),
    )
    recognition_basis = request.get("recognition_basis")
    recognition_limits = request.get("recognition_limits")
    scope_values = _scope_values(request.get("recognition_scope"))
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_RECOGNITION_SCOPE
    ]

    block_code = _determine_block_code(
        request,
        selected_non_capture,
        selected_non_capture_path,
        selected_load_code,
        selected_non_capture_outcome,
        selected_non_capture_failed_count,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
        selected_request_declaration_result,
        selected_source_body_surface,
        receiving_context,
        receiving_context_type,
        reception_class,
        reception_purpose,
        reception_limits,
        recognition_basis,
        recognition_limits,
        unsupported_scope,
    )

    requested_outcome = request.get("requested_recognition_outcome") or OUTCOME_RECORDED
    if block_code:
        outcome = OUTCOME_BLOCKED
    elif request.get("recognition_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_RECORDED:
        outcome = OUTCOME_RECORDED
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_RECOGNITION_REQUEST_MALFORMED"

    recorded = outcome == OUTCOME_RECORDED
    checks = _build_checks(
        block_code,
        request,
        selected_non_capture,
        selected_non_capture_outcome,
        selected_non_capture_failed_count,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
        selected_request_declaration_result,
        selected_source_body_surface,
        receiving_context,
        receiving_context_type,
        recognition_basis,
        recognition_limits,
        unsupported_scope,
    )
    passed_check_count = sum(1 for check in checks if check["passed"])
    failed_check_count = sum(1 for check in checks if not check["passed"])

    result_id_seed = _safe_component(
        request.get("recognition_request_id") or selected_non_capture_id,
        "source_body_reception_recognition",
    )
    metadata = {
        "source_body_reception_recognition_result_id": (
            f"{result_id_seed}__source_body_reception_recognition_result"
        ),
        "source_body_reception_recognition_result_type": (
            "source_body_reception_recognition_boundary_result"
        ),
        "source_body_reception_recognition_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }

    source_body_identity_basis = _first_present(
        request.get("source_body_identity_basis"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "source_body_identity_basis",
        ),
        _value_at(selected_source_body_surface, "source_body_identity_basis"),
    )
    source_body_lineage_basis = _first_present(
        request.get("source_body_lineage_basis"),
        _value_at(
            selected_non_capture_dict,
            "non_capture_basis",
            "source_body_lineage_basis",
        ),
        _value_at(selected_source_body_surface, "source_body_lineage_basis"),
    )
    surface_identifier = _surface_identifier(request, selected_source_body_surface)
    surface_type = _surface_type(request, selected_source_body_surface)
    surface_reference = _surface_reference(request, selected_source_body_surface)
    receiving_context_id = _context_id(request, receiving_context)

    selected_surface_section = {
        "selected_source_body_surface": copy.deepcopy(selected_source_body_surface),
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_path": _first_present(
            request.get("selected_source_body_surface_path"),
            _value_at(selected_source_body_surface, "selected_source_body_surface_path"),
            _value_at(selected_source_body_surface, "path"),
        ),
        "selected_source_body_surface_reference": surface_reference,
        "source_body_identity_basis": copy.deepcopy(source_body_identity_basis),
        "source_body_lineage_basis": copy.deepcopy(source_body_lineage_basis),
        "selected_source_body_surface_remains_source": True,
        "selected_source_body_surface_is_not_whole_body_by_default": True,
        "selected_source_body_surface_is_not_received": True,
        "selected_source_body_surface_is_not_adopted": True,
        "selected_source_body_surface_is_not_replaced": True,
        "selected_source_body_surface_is_not_validated_by_receiving_context": True,
        "selected_source_body_surface_is_not_invalidated_by_receiving_context": True,
    }

    receiving_context_section = {
        "receiving_context": copy.deepcopy(receiving_context),
        "receiving_context_id": receiving_context_id,
        "receiving_context_name": _value_at(receiving_context, "name"),
        "receiving_context_reference": _value_at(receiving_context, "reference"),
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
    }

    selected_non_capture_section = {
        "selected_non_capture_result_id": selected_non_capture_id,
        "selected_non_capture_result_outcome": selected_non_capture_outcome,
        "selected_non_capture_result_path": selected_non_capture_path,
        "selected_non_capture_outcome_is_passed": (
            selected_non_capture_outcome == REQUIRED_NON_CAPTURE_OUTCOME
        ),
        "selected_non_capture_result_failed_check_count_zero": (
            selected_non_capture_failed_count == 0
        ),
        "selected_non_capture_result_preserved": selected_non_capture is not None,
        "selected_non_capture_result_recorded": selected_non_capture is not None,
        "selected_eligibility_result_preserved": _present(selected_eligibility_result),
        "selected_receiving_context_role_result_preserved": _present(
            selected_receiving_context_role_result
        ),
        "selected_identity_preservation_result_preserved": _present(
            selected_identity_preservation_result
        ),
        "selected_reception_request_declaration_result_preserved": _present(
            selected_request_declaration_result
        ),
        "selected_source_body_surface_preserved": isinstance(
            selected_source_body_surface, Mapping
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": isinstance(receiving_context, Mapping),
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "non_capture_passed_as_refusal_check_outcome_only": True,
        "non_adoption_passed_as_refusal_check_outcome_only": True,
        "non_currentness_passed_as_refusal_check_outcome_only": True,
        "non_capture_did_not_authorize_reception": True,
        "non_capture_did_not_receive_source": True,
        "non_capture_did_not_claim_recognition_passed": True,
        "raw_selected_non_capture_result": copy.deepcopy(selected_non_capture),
    }

    declared_question = {
        "recognition_request_id": request.get("recognition_request_id"),
        "recognition_question": request.get("recognition_question"),
        "recognition_intent": request.get("recognition_intent"),
        "declared_recognition_request_path": request_path,
        "selected_non_capture_result_id": selected_non_capture_id,
        "selected_non_capture_result_outcome": selected_non_capture_outcome,
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_reference": surface_reference,
        "receiving_context_id": receiving_context_id,
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": reception_purpose,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_authority": True,
        "recognition_is_not_currentness": True,
        "recognition_is_not_operation_permission": True,
    }

    recognition_basis_section = {
        "selected_non_capture_result": copy.deepcopy(selected_non_capture),
        "selected_eligibility_result": copy.deepcopy(selected_eligibility_result),
        "selected_receiving_context_role_result": copy.deepcopy(
            selected_receiving_context_role_result
        ),
        "selected_identity_preservation_result": copy.deepcopy(
            selected_identity_preservation_result
        ),
        "selected_reception_request_declaration_result": copy.deepcopy(
            selected_request_declaration_result
        ),
        "selected_source_body_surface": copy.deepcopy(selected_source_body_surface),
        "source_body_identity_basis": copy.deepcopy(source_body_identity_basis),
        "source_body_lineage_basis": copy.deepcopy(source_body_lineage_basis),
        "receiving_context": copy.deepcopy(receiving_context),
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": reception_purpose,
        "reception_limits": copy.deepcopy(reception_limits),
        "selected_receiving_context_role": copy.deepcopy(selected_receiving_context_role),
        "receiving_context_role_class": receiving_context_role_class,
        "receiving_context_role_limits": copy.deepcopy(receiving_context_role_limits),
        "eligibility_basis": copy.deepcopy(eligibility_basis),
        "admissibility_basis": copy.deepcopy(admissibility_basis),
        "review_readiness_limits": copy.deepcopy(review_readiness_limits),
        "non_capture_basis": copy.deepcopy(non_capture_basis),
        "non_adoption_basis": copy.deepcopy(non_adoption_basis),
        "non_currentness_basis": copy.deepcopy(non_currentness_basis),
        "recognition_basis": copy.deepcopy(recognition_basis),
        "bounded_recognition_only": True,
        "recognized_for_later_reception_family_accounting_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_currentness": True,
        "recognition_does_not_validate_source": True,
        "recognition_does_not_invalidate_source": True,
        "recognition_does_not_create_operation_permission": True,
        "receipt_exhaustion_requires_separate_boundary": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }

    recognition_limits_section = {
        "recognition_limits": copy.deepcopy(recognition_limits),
        "recognition_review_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_authority": True,
        "recognition_is_not_currentness": True,
        "recognition_is_not_validation": True,
        "recognition_is_not_invalidation": True,
        "recognition_is_not_operation_permission": True,
        "recognition_is_not_publication_flow": True,
        "receipt_exhaustion_requires_separate_boundary": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }

    recognition_scope_section = {
        "selected_recognition_scope_values": scope_values,
        "all_selected_scope_values_supported": not unsupported_scope,
        "unsupported_recognition_scope_values": list(unsupported_scope),
        "recognition_review_only": "RECOGNITION_REVIEW_ONLY" in scope_values,
        "recognition_is_not_authorization": "RECOGNITION_IS_NOT_AUTHORIZATION" in scope_values,
        "recognition_is_not_source_receipt": "RECOGNITION_IS_NOT_SOURCE_RECEIPT" in scope_values,
        "recognition_is_not_adoption": "RECOGNITION_IS_NOT_ADOPTION" in scope_values,
        "recognition_is_not_authority": "RECOGNITION_IS_NOT_AUTHORITY" in scope_values,
        "recognition_is_not_currentness": "RECOGNITION_IS_NOT_CURRENTNESS" in scope_values,
        "recognition_is_not_validation": "RECOGNITION_IS_NOT_VALIDATION" in scope_values,
        "recognition_is_not_invalidation": "RECOGNITION_IS_NOT_INVALIDATION" in scope_values,
        "recognition_is_not_operation_permission": (
            "RECOGNITION_IS_NOT_OPERATION_PERMISSION" in scope_values
        ),
        "recognition_is_not_publication_flow": "RECOGNITION_IS_NOT_PUBLICATION_FLOW" in scope_values,
        "receipt_exhaustion_requires_separate_boundary": (
            "RECEIPT_EXHAUSTION_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
        "conformance_requires_separate_boundary": (
            "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
    }

    non_claims = _build_non_claims(recorded)
    recognition_statement = {
        "source_body_reception_recognition_recorded": recorded,
        "reception_recognized": recorded,
        "selected_non_capture_result_preserved": selected_non_capture is not None,
        "selected_non_capture_result_recorded": selected_non_capture is not None,
        "selected_non_capture_result_failed_check_count_zero": (
            selected_non_capture_failed_count == 0
        ),
        "selected_eligibility_result_preserved": _present(selected_eligibility_result),
        "selected_receiving_context_role_result_preserved": _present(
            selected_receiving_context_role_result
        ),
        "selected_identity_preservation_result_preserved": _present(
            selected_identity_preservation_result
        ),
        "selected_reception_request_declaration_result_preserved": _present(
            selected_request_declaration_result
        ),
        "selected_source_body_surface_preserved": isinstance(
            selected_source_body_surface, Mapping
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": isinstance(receiving_context, Mapping),
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "eligibility_admissibility_is_review_readiness_only": True,
        "non_capture_passed_as_refusal_check_outcome_only": True,
        "non_adoption_passed_as_refusal_check_outcome_only": True,
        "non_currentness_passed_as_refusal_check_outcome_only": True,
        "bounded_recognition_for_accounting_only": True,
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "recognition_is_not_adoption": True,
        "recognition_is_not_authority": True,
        "recognition_is_not_currentness": True,
        "recognition_is_not_validation": True,
        "recognition_is_not_invalidation": True,
        "recognition_is_not_operation_permission": True,
        "recognition_is_not_publication_flow": True,
        "receipt_exhaustion_requires_separate_boundary": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
        **{key: False for key in REQUIRED_FALSE_NON_CLAIMS},
    }

    additional_basis_required = {
        "additional_basis_required": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "additional_basis_context": copy.deepcopy(
            request.get("additional_basis_context")
        ),
        "missing_basis_is_not_scheduled": True,
        "missing_basis_is_not_authorized": True,
        "missing_basis_is_not_executed": True,
    }
    not_recorded_basis = {
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "not_recorded_basis": copy.deepcopy(request.get("not_recorded_basis")),
        "not_recorded_does_not_mutate": True,
        "not_recorded_does_not_repair": True,
        "not_recorded_does_not_authorize": True,
        "not_recorded_does_not_receive": True,
        "not_recorded_does_not_replace": True,
        "not_recorded_does_not_validate": True,
        "not_recorded_does_not_invalidate": True,
        "not_recorded_does_not_create_currentness": True,
        "not_recorded_does_not_create_source_receipt": True,
        "not_recorded_does_not_claim_conformance_or_closure": True,
    }

    result: dict[str, Any] = {
        "source_body_reception_recognition_metadata": metadata,
        "declared_recognition_question": declared_question,
        "selected_non_capture_result": selected_non_capture_section,
        "selected_source_body_surface": selected_surface_section,
        "receiving_context": receiving_context_section,
        "recognition_basis": recognition_basis_section,
        "recognition_limits": recognition_limits_section,
        "recognition_scope": recognition_scope_section,
        "recognition_checks": checks,
        "recognition_statement": recognition_statement,
        "recognition_non_meaning": _build_recognition_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason") or block_code),
    }
    result["source_body_reception_recognition_summary"] = (
        build_source_body_reception_recognition_summary(result)
    )
    result["source_body_reception_recognition_summary"]["passed_check_count"] = (
        passed_check_count
    )
    result["source_body_reception_recognition_summary"]["failed_check_count"] = (
        failed_check_count
    )
    return result


def resolve_source_body_reception_recognition_boundary(
    declared_recognition_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared source-body reception recognition request."""
    if declared_recognition_request is None:
        return _build_result({})
    if not isinstance(declared_recognition_request, Mapping):
        return _blocked_malformed_request("DECLARED_RECOGNITION_REQUEST_MALFORMED")
    return _build_result(copy.deepcopy(dict(declared_recognition_request)))


def resolve_source_body_reception_recognition_boundary_from_path(
    declared_recognition_request_path: Path | str,
) -> dict:
    """Load and resolve one declared source-body reception recognition request."""
    request, error = _read_json_object(declared_recognition_request_path)
    if error == "unreadable":
        return _blocked_malformed_request(
            "DECLARED_RECOGNITION_REQUEST_UNREADABLE",
            str(declared_recognition_request_path),
        )
    if error == "malformed":
        return _blocked_malformed_request(
            "DECLARED_RECOGNITION_REQUEST_MALFORMED",
            str(declared_recognition_request_path),
        )
    return _build_result(request or {}, request_path=str(declared_recognition_request_path))


def _blocked_malformed_request(code: str, request_path: str | None = None) -> dict:
    request = {
        "recognition_request_id": None,
        "recognition_question": None,
        "recognition_intent": None,
        "selected_non_capture_result": None,
        "recognition_basis": None,
        "recognition_limits": None,
        "recognition_scope": [],
        "declared_non_claims": {},
        "block_reason": code,
    }
    result = _build_result(request, request_path=request_path)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = _block(code, request_path or code)
    result["source_body_reception_recognition_summary"] = (
        build_source_body_reception_recognition_summary(result)
    )
    return result


def build_source_body_reception_recognition_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the bounded summary for a recognition boundary result."""
    checks = result.get("recognition_checks") or []
    passed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and _truthy(check.get("passed"))
    )
    failed_check_count = sum(
        1
        for check in checks
        if isinstance(check, Mapping) and not _truthy(check.get("passed"))
    )
    question = result.get("declared_recognition_question") or {}
    selected = result.get("selected_non_capture_result") or {}
    surface = result.get("selected_source_body_surface") or {}
    context = result.get("receiving_context") or {}
    statement = result.get("recognition_statement") or {}
    block = result.get("block") or {}
    non_claims = result.get("non_claims") or {}
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "recognition_request_id": question.get("recognition_request_id"),
        "recognition_question": question.get("recognition_question"),
        "recognition_intent": question.get("recognition_intent"),
        "selected_non_capture_result_id": selected.get("selected_non_capture_result_id"),
        "selected_non_capture_result_outcome": selected.get(
            "selected_non_capture_result_outcome"
        ),
        "selected_source_body_surface_identifier": surface.get(
            "selected_source_body_surface_identifier"
        ),
        "selected_source_body_surface_type": surface.get(
            "selected_source_body_surface_type"
        ),
        "selected_source_body_surface_reference": surface.get(
            "selected_source_body_surface_reference"
        ),
        "receiving_context_id": context.get("receiving_context_id"),
        "receiving_context_type": context.get("receiving_context_type"),
        "reception_class": question.get("reception_class"),
        "reception_purpose": question.get("reception_purpose"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "recognition_recorded": _truthy(
            statement.get("source_body_reception_recognition_recorded")
        ),
        "reception_recognized": _truthy(statement.get("reception_recognized")),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_non_capture_result_preserved": statement.get(
            "selected_non_capture_result_preserved"
        ),
        "selected_non_capture_result_recorded": statement.get(
            "selected_non_capture_result_recorded"
        ),
        "selected_non_capture_result_failed_check_count_zero": statement.get(
            "selected_non_capture_result_failed_check_count_zero"
        ),
        "selected_eligibility_result_preserved": statement.get(
            "selected_eligibility_result_preserved"
        ),
        "selected_receiving_context_role_result_preserved": statement.get(
            "selected_receiving_context_role_result_preserved"
        ),
        "selected_identity_preservation_result_preserved": statement.get(
            "selected_identity_preservation_result_preserved"
        ),
        "selected_request_declaration_result_preserved": statement.get(
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
        "receiving_context_is_not_source": statement.get(
            "receiving_context_is_not_source"
        ),
        "receiving_context_is_not_authority": statement.get(
            "receiving_context_is_not_authority"
        ),
        "receiving_context_is_not_current": statement.get(
            "receiving_context_is_not_current"
        ),
        "eligibility_admissibility_review_readiness_only": statement.get(
            "eligibility_admissibility_is_review_readiness_only"
        ),
        "non_capture_passed_as_refusal_check_outcome_only": statement.get(
            "non_capture_passed_as_refusal_check_outcome_only"
        ),
        "non_adoption_passed_as_refusal_check_outcome_only": statement.get(
            "non_adoption_passed_as_refusal_check_outcome_only"
        ),
        "non_currentness_passed_as_refusal_check_outcome_only": statement.get(
            "non_currentness_passed_as_refusal_check_outcome_only"
        ),
        "bounded_recognition_for_accounting_only": statement.get(
            "bounded_recognition_for_accounting_only"
        ),
        "recognition_is_not_authorization": statement.get(
            "recognition_is_not_authorization"
        ),
        "recognition_is_not_source_receipt": statement.get(
            "recognition_is_not_source_receipt"
        ),
        "recognition_is_not_adoption": statement.get("recognition_is_not_adoption"),
        "recognition_is_not_authority": statement.get("recognition_is_not_authority"),
        "recognition_is_not_currentness": statement.get(
            "recognition_is_not_currentness"
        ),
        "recognition_is_not_validation": statement.get(
            "recognition_is_not_validation"
        ),
        "recognition_is_not_invalidation": statement.get(
            "recognition_is_not_invalidation"
        ),
        "recognition_is_not_operation_permission": statement.get(
            "recognition_is_not_operation_permission"
        ),
        "recognition_is_not_publication_flow": statement.get(
            "recognition_is_not_publication_flow"
        ),
        "receipt_exhaustion_future": statement.get(
            "receipt_exhaustion_requires_separate_boundary"
        ),
        "conformance_future": statement.get("conformance_requires_separate_boundary"),
        "closure_future": statement.get("closure_requires_separate_boundary"),
        "no_reception_authorization": non_claims.get("reception_authorized") is False,
        "no_source_received": non_claims.get("source_received") is False,
        "no_source_receipt": non_claims.get("source_receipt_recorded") is False,
        "no_source_validation": non_claims.get(
            "source_validated_by_receiving_context"
        )
        is False,
        "no_source_invalidation": non_claims.get(
            "source_invalidated_by_receiving_context"
        )
        is False,
        "no_source_replacement": non_claims.get("source_replaced") is False,
        "no_adoption_authority_currentness_standing": all(
            non_claims.get(key) is False
            for key in (
                "adoption_created",
                "authority_created",
                "currentness_created",
                "standing_created",
            )
        ),
        "no_vessel_derivative_relation": all(
            non_claims.get(key) is False
            for key in ("vessel_relation_created", "derivative_relation_created")
        ),
        "no_operation_permission_governance_publication_flow": all(
            non_claims.get(key) is False
            for key in (
                "operation_permission_created",
                "receiving_context_governance_created",
                "publication_flow_opened",
            )
        ),
        "no_public_readiness_final_completion_follow_on_work": all(
            non_claims.get(key) is False
            for key in (
                "public_launch_readiness_created",
                "final_completion_claimed",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": copy.deepcopy(non_claims),
    }


def write_source_body_reception_recognition_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive source-body reception recognition result artifact."""
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionRecognitionBoundaryError(
            "Recognition result must be a mapping."
        )
    if output_path is None:
        summary = result.get("source_body_reception_recognition_summary") or {}
        stem = _safe_component(
            summary.get("recognition_request_id")
            or summary.get("selected_non_capture_result_id"),
            "source_body_reception_recognition",
        )
        output_path = (
            SOURCE_BODY_RECEPTION_RECOGNITION_BOUNDARY_ROOT
            / f"{stem}__source_body_reception_recognition_result.json"
        )
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    candidate = output
    if candidate.exists():
        stem = output.stem
        suffix = output.suffix
        counter = 1
        while candidate.exists():
            candidate = output.with_name(f"{stem}_{counter:03d}{suffix}")
            counter += 1
    with candidate.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return candidate


def build_declared_source_body_reception_recognition_request(
    recognition_request_id: str,
    recognition_question: str,
    selected_non_capture_result: Mapping[str, Any] | str,
    recognition_basis: Mapping[str, Any] | str,
    recognition_limits: Mapping[str, Any] | str,
    recognition_scope: Sequence[str] | Mapping[str, Any],
    recognition_intent: str = INTENT_RECORD,
    *,
    selected_non_capture_result_path: str | None = None,
    selected_non_capture_result_id: str | None = None,
    selected_non_capture_result_outcome: str | None = None,
    requested_recognition_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared recognition request with required non-claims false."""
    request: dict[str, Any] = {
        "recognition_request_id": recognition_request_id,
        "recognition_question": recognition_question,
        "recognition_intent": recognition_intent,
        "recognition_basis": copy.deepcopy(recognition_basis),
        "recognition_limits": copy.deepcopy(recognition_limits),
        "recognition_scope": copy.deepcopy(recognition_scope),
        "declared_non_claims": {
            key: False for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "requested_recognition_outcome": requested_recognition_outcome,
    }
    if selected_non_capture_result_path is not None:
        request["selected_non_capture_result_path"] = selected_non_capture_result_path
    elif isinstance(selected_non_capture_result, Mapping):
        request["selected_non_capture_result"] = copy.deepcopy(
            dict(selected_non_capture_result)
        )
    else:
        request["selected_non_capture_result"] = selected_non_capture_result
    if selected_non_capture_result_id is not None:
        request["selected_non_capture_result_id"] = selected_non_capture_result_id
    if selected_non_capture_result_outcome is not None:
        request["selected_non_capture_result_outcome"] = (
            selected_non_capture_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = copy.deepcopy(additional_basis_context)
    if not_recorded_basis is not None:
        request["not_recorded_basis"] = copy.deepcopy(not_recorded_basis)
    return request
