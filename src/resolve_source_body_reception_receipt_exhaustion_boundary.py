"""Resolve the source-body reception receipt / exhaustion boundary.

This module records receipt / exhaustion of one bounded source-body
reception recognition record for reception-family accounting only.
Receipt / exhaustion is not source receipt, reception authorization,
source received, adoption, authority, currentness, conformance, or closure.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class SourceBodyReceptionReceiptExhaustionBoundaryError(Exception):
    """Raised for hard receipt / exhaustion boundary path or shape failures."""


RESOLVER_MODULE = "resolve_source_body_reception_receipt_exhaustion_boundary"
RESULT_VERSION = "0.1.0"

SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_receipt_exhaustion_boundary"
)

OUTCOME_RECORDED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_RECORDED"
OUTCOME_NOT_RECORDED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

REQUIRED_RECOGNITION_OUTCOME = "SOURCE_BODY_RECEPTION_RECOGNITION_RECORDED"

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_REVIEW"
SUPPORTED_RECEIPT_EXHAUSTION_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_RECEIPT_EXHAUSTION_SCOPE = {
    "RECOGNITION_RECORD_RECEIPT_ONLY",
    "RECOGNITION_RECORD_EXHAUSTION_ONLY",
    "RECEIPT_EXHAUSTION_IS_NOT_SOURCE_RECEIPT",
    "RECEIPT_EXHAUSTION_IS_NOT_AUTHORIZATION",
    "RECEIPT_EXHAUSTION_DOES_NOT_RECEIVE_SOURCE",
    "RECEIPT_EXHAUSTION_DOES_NOT_CREATE_SOURCE_RECEIPT",
    "RECEIPT_EXHAUSTION_IS_NOT_ADOPTION",
    "RECEIPT_EXHAUSTION_IS_NOT_AUTHORITY",
    "RECEIPT_EXHAUSTION_IS_NOT_CURRENTNESS",
    "RECEIPT_EXHAUSTION_IS_NOT_VALIDATION",
    "RECEIPT_EXHAUSTION_IS_NOT_INVALIDATION",
    "RECEIPT_EXHAUSTION_IS_NOT_OPERATION_PERMISSION",
    "RECEIPT_EXHAUSTION_IS_NOT_PUBLICATION_FLOW",
    "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY",
    "CLOSURE_REQUIRES_SEPARATE_BOUNDARY",
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
    "reception_conformance_passed",
    "reception_closure_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_RECORDED_TRUE_FIELDS = (
    "source_body_reception_receipt_exhaustion_recorded",
    "reception_recognition_receipt_recorded",
    "reception_recognition_exhaustion_recorded",
    "recognized_reception_accounting_receipt_recorded",
    "recognized_reception_accounting_exhausted",
)

COLLAPSE_FIELD_CODES = (
    ("reception_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_RECEPTION"),
    ("source_received", "RECEIPT_EXHAUSTION_RECEIVES_SOURCE"),
    ("source_receipt_recorded", "RECEIPT_EXHAUSTION_RECORDS_SOURCE_RECEIPT"),
    ("source_receipt_created", "RECEIPT_EXHAUSTION_CREATES_SOURCE_RECEIPT"),
    (
        "receiving_context_governance_created",
        "RECEIPT_EXHAUSTION_CREATES_GOVERNANCE",
    ),
    (
        "receiving_context_became_source",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_SOURCE",
    ),
    (
        "receiving_context_became_authority",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_AUTHORITY",
    ),
    (
        "receiving_context_became_current",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_CURRENT",
    ),
    (
        "receiving_context_became_receiver",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_RECEIVER",
    ),
    (
        "receiving_context_became_adopter",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_ADOPTER",
    ),
    (
        "receiving_context_became_validator",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_VALIDATOR",
    ),
    (
        "receiving_context_became_invalidator",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_INVALIDATOR",
    ),
    (
        "receiving_context_became_operator",
        "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_OPERATOR",
    ),
    (
        "source_validated_by_receiving_context",
        "RECEIPT_EXHAUSTION_VALIDATES_SOURCE",
    ),
    (
        "source_invalidated_by_receiving_context",
        "RECEIPT_EXHAUSTION_INVALIDATES_SOURCE",
    ),
    ("source_replaced", "RECEIPT_EXHAUSTION_REPLACES_SOURCE"),
    ("adoption_created", "RECEIPT_EXHAUSTION_CREATES_ADOPTION"),
    ("authority_created", "RECEIPT_EXHAUSTION_CREATES_AUTHORITY"),
    ("currentness_created", "RECEIPT_EXHAUSTION_CREATES_CURRENTNESS"),
    ("standing_created", "RECEIPT_EXHAUSTION_CREATES_STANDING"),
    ("standing_propagated", "RECEIPT_EXHAUSTION_CREATES_STANDING_PROPAGATION"),
    ("vessel_relation_created", "RECEIPT_EXHAUSTION_CREATES_VESSEL_RELATION"),
    (
        "derivative_relation_created",
        "RECEIPT_EXHAUSTION_CREATES_DERIVATIVE_RELATION",
    ),
    (
        "operation_permission_created",
        "RECEIPT_EXHAUSTION_CREATES_OPERATION_PERMISSION",
    ),
    (
        "public_launch_readiness_created",
        "RECEIPT_EXHAUSTION_CREATES_PUBLIC_READINESS",
    ),
    ("final_completion_claimed", "RECEIPT_EXHAUSTION_CLAIMS_FINAL_COMPLETION"),
    (
        "follow_on_work_authorized",
        "RECEIPT_EXHAUSTION_AUTHORIZES_FOLLOW_ON_WORK",
    ),
    ("continuation_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "RECEIPT_EXHAUSTION_OPENS_PUBLICATION_FLOW"),
    (
        "reception_conformance_passed",
        "RECEIPT_EXHAUSTION_CLAIMS_CONFORMANCE_PASSED",
    ),
    ("reception_closure_passed", "RECEIPT_EXHAUSTION_CLAIMS_CLOSURE_PASSED"),
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
        result.get("failed_check_count"),
        _value_at(
            result,
            "source_body_reception_recognition_summary",
            "failed_check_count",
        ),
        _value_at(result, "summary", "failed_check_count"),
    )
    if isinstance(explicit, int):
        return explicit
    checks = _first_present(
        result.get("recognition_checks"),
        result.get("checks"),
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
            scope.get("selected_receipt_exhaustion_scope_values"),
            scope.get("receipt_exhaustion_scope_values"),
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


def _load_selected_recognition_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    result_path = request.get("selected_recognition_result_path")
    if _present(result_path):
        loaded, error = _read_json_object(str(result_path))
        if error == "unreadable":
            return None, str(result_path), "RECOGNITION_RESULT_UNREADABLE"
        if error == "malformed":
            return None, str(result_path), "RECOGNITION_RESULT_MALFORMED"
        return loaded, str(result_path), None
    selected = request.get("selected_recognition_result")
    if isinstance(selected, Mapping):
        return copy.deepcopy(dict(selected)), None, None
    if _present(selected):
        return None, None, "RECOGNITION_RESULT_MALFORMED"
    return None, None, None


def _extract_recognition_outcome(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_recognition_result_outcome"),
        request.get("expected_selected_recognition_outcome"),
        selected.get("outcome"),
        _value_at(selected, "source_body_reception_recognition_summary", "outcome"),
        _value_at(selected, "recognition_statement", "outcome"),
    )


def _extract_recognition_id(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_recognition_result_id"),
        _value_at(
            selected,
            "source_body_reception_recognition_metadata",
            "source_body_reception_recognition_result_id",
        ),
        _value_at(
            selected,
            "source_body_reception_recognition_summary",
            "source_body_reception_recognition_result_id",
        ),
        selected.get("source_body_reception_recognition_result_id"),
        selected.get("recognition_request_id"),
        _value_at(selected, "declared_recognition_question", "recognition_request_id"),
    )


def _nested_selected_non_capture(selected: Mapping[str, Any]) -> Any:
    return _first_present(
        _value_at(selected, "recognition_basis", "selected_non_capture_result"),
        _value_at(selected, "selected_non_capture_result", "raw_selected_non_capture_result"),
        selected.get("selected_non_capture_result"),
    )


def _nested_selected_eligibility(selected: Mapping[str, Any], non_capture: Any) -> Any:
    return _first_present(
        _value_at(selected, "recognition_basis", "selected_eligibility_result"),
        _value_at(non_capture, "non_capture_basis", "selected_eligibility_result"),
        _value_at(non_capture, "selected_eligibility_result", "raw_selected_eligibility_result"),
        _value_at(non_capture, "selected_eligibility_result"),
    )


def _nested_role_result(selected: Mapping[str, Any], non_capture: Any, eligibility: Any) -> Any:
    return _first_present(
        _value_at(selected, "recognition_basis", "selected_receiving_context_role_result"),
        _value_at(non_capture, "non_capture_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "eligibility_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "selected_receiving_context_role_result"),
    )


def _nested_identity_result(
    selected: Mapping[str, Any], non_capture: Any, eligibility: Any, role_result: Any
) -> Any:
    return _first_present(
        _value_at(selected, "recognition_basis", "selected_identity_preservation_result"),
        _value_at(non_capture, "non_capture_basis", "selected_identity_preservation_result"),
        _value_at(eligibility, "eligibility_basis", "selected_identity_preservation_result"),
        _value_at(role_result, "receiving_context_role_basis", "selected_identity_preservation_result"),
        _value_at(role_result, "selected_identity_preservation_result"),
    )


def _nested_request_declaration(
    selected: Mapping[str, Any],
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        _value_at(
            selected,
            "recognition_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            non_capture,
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
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        request.get("selected_source_body_surface"),
        _value_at(selected, "recognition_basis", "selected_source_body_surface"),
        _value_at(selected, "selected_source_body_surface", "selected_source_body_surface"),
        selected.get("selected_source_body_surface"),
        _value_at(non_capture, "non_capture_basis", "selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface"),
        _value_at(role_result, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(identity_result, "selected_source_body_surface", "selected_source_body_surface"),
    )


def _nested_receiving_context(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
) -> Any:
    return _first_present(
        request.get("receiving_context"),
        _value_at(selected, "recognition_basis", "receiving_context"),
        _value_at(selected, "receiving_context", "receiving_context"),
        selected.get("receiving_context"),
        _value_at(non_capture, "non_capture_basis", "receiving_context"),
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
        _value_at(selected, "recognition_basis", "receiving_context_type"),
        _value_at(selected, "source_body_reception_recognition_summary", "receiving_context_type"),
    )


def _flag(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
    key: str,
    default: bool = False,
) -> bool:
    value = _first_present(
        request.get(key),
        _value_at(selected, "receipt_exhaustion_statement", key),
        _value_at(selected, "recognition_statement", key),
        _value_at(selected, "selected_recognition_result", key),
        _value_at(selected, "source_body_reception_recognition_summary", key),
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
    non_claims.update({key: bool(recorded) for key in ALLOWED_RECORDED_TRUE_FIELDS})
    return non_claims


def _build_receipt_exhaustion_non_meaning() -> dict[str, bool]:
    meanings = (
        "reception_authorized",
        "source_received",
        "source_receipt_recorded",
        "source_receipt_created",
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
        "conformance_passed",
        "closure_recorded",
        "public_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
        "continuation_authorized",
        "publication_flow_opened",
    )
    result = {f"does_not_mean_{name}": True for name in meanings}
    result["receipt_exhaustion_is_not_source_receipt"] = True
    result["receipt_exhaustion_is_not_authorization"] = True
    result["receipt_exhaustion_is_not_source_received"] = True
    result["receipt_exhaustion_is_not_conformance"] = True
    result["receipt_exhaustion_is_not_closure"] = True
    return result


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "source-body reception receipt / exhaustion test",
            "source-body reception receipt / exhaustion live artifact",
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
    selected_recognition: Mapping[str, Any] | None,
    selected_load_code: str | None,
    selected_recognition_outcome: Any,
    selected_recognition_failed_count: int | None,
    selected_non_capture_result: Any,
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
    receipt_exhaustion_basis: Any,
    recognition_record_receipt_basis: Any,
    recognition_record_exhaustion_basis: Any,
    unsupported_scope: Sequence[str],
) -> str | None:
    if not _present(request.get("receipt_exhaustion_question")):
        return "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED"
    if request.get("receipt_exhaustion_intent") == INTENT_BLOCK:
        return "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if request.get("receipt_exhaustion_intent") not in SUPPORTED_RECEIPT_EXHAUSTION_INTENTS:
        return "RECEIPT_EXHAUSTION_INTENT_UNSUPPORTED"
    if selected_load_code:
        return selected_load_code
    if not _present(selected_recognition):
        return "RECOGNITION_RESULT_MISSING"
    if not _present(selected_recognition_outcome):
        return "RECOGNITION_RESULT_OUTCOME_MISSING"
    if selected_recognition_outcome != REQUIRED_RECOGNITION_OUTCOME:
        return "RECOGNITION_RESULT_NOT_RECORDED"
    if selected_recognition_failed_count != 0:
        return "RECOGNITION_RESULT_HAS_FAILED_CHECKS"
    if not _present(selected_non_capture_result):
        return "NON_CAPTURE_RESULT_MISSING"
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
    if not _present(receipt_exhaustion_basis):
        return "RECEIPT_EXHAUSTION_BASIS_MISSING"
    if not _present(recognition_record_receipt_basis):
        return "RECOGNITION_RECORD_RECEIPT_BASIS_MISSING"
    if not _present(recognition_record_exhaustion_basis):
        return "RECOGNITION_RECORD_EXHAUSTION_BASIS_MISSING"
    if unsupported_scope:
        return "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE"
    collapse = _collapse_code(request, selected_recognition)
    if collapse:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    block_code: str | None,
    request: Mapping[str, Any],
    selected_recognition: Mapping[str, Any] | None,
    selected_recognition_outcome: Any,
    selected_recognition_failed_count: int | None,
    selected_non_capture_result: Any,
    selected_eligibility_result: Any,
    selected_receiving_context_role_result: Any,
    selected_identity_preservation_result: Any,
    selected_request_declaration_result: Any,
    selected_source_body_surface: Any,
    receiving_context: Any,
    receiving_context_type: Any,
    receipt_exhaustion_basis: Any,
    recognition_record_receipt_basis: Any,
    recognition_record_exhaustion_basis: Any,
    unsupported_scope: Sequence[str],
) -> list[dict[str, Any]]:
    selected = selected_recognition or {}
    intent_supported = (
        request.get("receipt_exhaustion_intent") in SUPPORTED_RECEIPT_EXHAUSTION_INTENTS
        and request.get("receipt_exhaustion_intent") != INTENT_BLOCK
    )
    intent_block_code = (
        "RECEIPT_EXHAUSTION_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        if request.get("receipt_exhaustion_intent") == INTENT_BLOCK
        else "RECEIPT_EXHAUSTION_INTENT_UNSUPPORTED"
    )
    checks = [
        _check(
            "receipt_exhaustion_question_declared",
            _present(request.get("receipt_exhaustion_question")),
            "receipt / exhaustion question declared",
            request.get("receipt_exhaustion_question"),
            "RECEIPT_EXHAUSTION_QUESTION_UNDECLARED",
        ),
        _check(
            "receipt_exhaustion_intent_supported",
            intent_supported,
            "receipt / exhaustion intent records bounded accounting review",
            request.get("receipt_exhaustion_intent"),
            intent_block_code,
        ),
        _check(
            "selected_recognition_result_present",
            _present(selected_recognition),
            "selected recognition result present",
            _present(selected_recognition),
            "RECOGNITION_RESULT_MISSING",
        ),
        _check(
            "selected_recognition_outcome_declared",
            _present(selected_recognition_outcome),
            "selected recognition outcome declared",
            selected_recognition_outcome,
            "RECOGNITION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_recognition_outcome_recorded",
            selected_recognition_outcome == REQUIRED_RECOGNITION_OUTCOME,
            REQUIRED_RECOGNITION_OUTCOME,
            selected_recognition_outcome,
            "RECOGNITION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected_recognition_failed_check_count_zero",
            selected_recognition_failed_count == 0,
            "selected recognition failed check count is zero",
            selected_recognition_failed_count,
            "RECOGNITION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected_non_capture_result_preserved",
            _present(selected_non_capture_result)
            and _flag(selected, request, "selected_non_capture_result_preserved", True),
            "selected non-capture result preserved",
            _present(selected_non_capture_result),
            "NON_CAPTURE_RESULT_MISSING",
        ),
        _check(
            "selected_eligibility_result_preserved",
            _present(selected_eligibility_result)
            and _flag(selected, request, "selected_eligibility_result_preserved", True),
            "selected eligibility / admissibility result preserved",
            _present(selected_eligibility_result),
            "ELIGIBILITY_RESULT_MISSING",
        ),
        _check(
            "selected_receiving_context_role_result_preserved",
            _present(selected_receiving_context_role_result)
            and _flag(selected, request, "selected_receiving_context_role_result_preserved", True),
            "selected receiving-context role result preserved",
            _present(selected_receiving_context_role_result),
            "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected_identity_preservation_result_preserved",
            _present(selected_identity_preservation_result)
            and _flag(selected, request, "selected_identity_preservation_result_preserved", True),
            "selected identity preservation result preserved",
            _present(selected_identity_preservation_result),
            "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected_request_declaration_result_preserved",
            _present(selected_request_declaration_result)
            and _flag(selected, request, "selected_reception_request_declaration_result_preserved", True),
            "selected request declaration result preserved",
            _present(selected_request_declaration_result),
            "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING",
        ),
        _check(
            "selected_source_body_surface_preserved",
            isinstance(selected_source_body_surface, Mapping)
            and _flag(selected, request, "selected_source_body_surface_preserved", True),
            "selected source-body surface preserved",
            _present(selected_source_body_surface),
            "SELECTED_SOURCE_BODY_SURFACE_MISSING",
        ),
        _check(
            "selected_source_body_surface_remains_source",
            _flag(selected, request, "selected_source_body_surface_remains_source", True),
            "selected source-body surface remains source",
            _flag(selected, request, "selected_source_body_surface_remains_source", True),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "selected_surface_is_not_whole_body_by_default",
            _flag(selected, request, "selected_surface_is_not_whole_body_by_default", True),
            "selected surface is not whole body by default",
            _flag(selected, request, "selected_surface_is_not_whole_body_by_default", True),
            "SELECTED_SOURCE_BODY_SURFACE_MALFORMED",
        ),
        _check(
            "receiving_context_preserved",
            isinstance(receiving_context, Mapping)
            and _flag(selected, request, "receiving_context_preserved", True),
            "receiving context preserved",
            _present(receiving_context),
            "RECEIVING_CONTEXT_MISSING",
        ),
        _check(
            "receiving_context_remains_context_only",
            _flag(selected, request, "receiving_context_remains_context_only", True),
            "receiving context remains context only",
            _flag(selected, request, "receiving_context_remains_context_only", True),
            "RECEIVING_CONTEXT_MALFORMED",
        ),
        _check(
            "receiving_context_is_not_source",
            _flag(selected, request, "receiving_context_is_not_source", True),
            "receiving context is not source",
            _flag(selected, request, "receiving_context_is_not_source", True),
            "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving_context_is_not_authority",
            _flag(selected, request, "receiving_context_is_not_authority", True),
            "receiving context is not authority",
            _flag(selected, request, "receiving_context_is_not_authority", True),
            "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving_context_is_not_current",
            _flag(selected, request, "receiving_context_is_not_current", True),
            "receiving context is not current",
            _flag(selected, request, "receiving_context_is_not_current", True),
            "RECEIPT_EXHAUSTION_TREATS_CONTEXT_AS_CURRENT",
        ),
        _check(
            "recognition_was_recorded",
            _flag(selected, request, "source_body_reception_recognition_recorded", True),
            "recognition was recorded",
            _flag(selected, request, "source_body_reception_recognition_recorded", True),
            "RECOGNITION_RESULT_NOT_RECORDED",
        ),
        _check(
            "reception_recognized_true",
            _flag(selected, request, "reception_recognized", True),
            "reception recognized is true",
            _flag(selected, request, "reception_recognized", True),
            "RECOGNITION_RESULT_NOT_RECORDED",
        ),
        _check(
            "recognition_bounded_for_accounting_only",
            _flag(selected, request, "bounded_recognition_for_accounting_only", True)
            or _truthy(_value_at(selected, "recognition_basis", "bounded_recognition_only")),
            "recognition remains bounded for accounting only",
            True,
        ),
        _check(
            "recognition_not_authorization",
            _flag(selected, request, "recognition_is_not_authorization", True),
            "recognition is not authorization",
            _flag(selected, request, "recognition_is_not_authorization", True),
            "RECEIPT_EXHAUSTION_AUTHORIZES_RECEPTION",
        ),
        _check(
            "recognition_not_source_receipt",
            _flag(selected, request, "recognition_is_not_source_receipt", True),
            "recognition is not source receipt",
            _flag(selected, request, "recognition_is_not_source_receipt", True),
            "RECEIPT_EXHAUSTION_RECORDS_SOURCE_RECEIPT",
        ),
        _check(
            "source_unreceived",
            not _contains_truthy_key(request, "source_received")
            and not _contains_truthy_key(selected, "source_received"),
            "source remains unreceived",
            request.get("source_received"),
            "RECEIPT_EXHAUSTION_RECEIVES_SOURCE",
        ),
        _check(
            "source_receipt_unrecorded",
            not _contains_truthy_key(request, "source_receipt_recorded")
            and not _contains_truthy_key(selected, "source_receipt_recorded"),
            "source receipt remains unrecorded",
            request.get("source_receipt_recorded"),
            "RECEIPT_EXHAUSTION_RECORDS_SOURCE_RECEIPT",
        ),
        _check(
            "receipt_exhaustion_basis_declared",
            _present(receipt_exhaustion_basis),
            "receipt / exhaustion basis declared",
            receipt_exhaustion_basis,
            "RECEIPT_EXHAUSTION_BASIS_MISSING",
        ),
        _check(
            "recognition_record_receipt_basis_declared",
            _present(recognition_record_receipt_basis),
            "recognition-record receipt basis declared",
            recognition_record_receipt_basis,
            "RECOGNITION_RECORD_RECEIPT_BASIS_MISSING",
        ),
        _check(
            "recognition_record_exhaustion_basis_declared",
            _present(recognition_record_exhaustion_basis),
            "recognition-record exhaustion basis declared",
            recognition_record_exhaustion_basis,
            "RECOGNITION_RECORD_EXHAUSTION_BASIS_MISSING",
        ),
        _check(
            "receipt_exhaustion_scope_supported",
            not unsupported_scope,
            "all selected receipt / exhaustion scope values supported",
            list(unsupported_scope),
            "UNSUPPORTED_RECEIPT_EXHAUSTION_SCOPE",
        ),
    ]

    anti_collapse_checks = (
        ("receipt_exhaustion_is_not_source_receipt", "source_receipt_recorded", "RECEIPT_EXHAUSTION_RECORDS_SOURCE_RECEIPT"),
        ("receipt_exhaustion_does_not_receive_source", "source_received", "RECEIPT_EXHAUSTION_RECEIVES_SOURCE"),
        ("receipt_exhaustion_does_not_authorize_reception", "reception_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_RECEPTION"),
        ("receipt_exhaustion_does_not_create_source_receipt", "source_receipt_created", "RECEIPT_EXHAUSTION_CREATES_SOURCE_RECEIPT"),
        ("receipt_exhaustion_does_not_create_adoption", "adoption_created", "RECEIPT_EXHAUSTION_CREATES_ADOPTION"),
        ("receipt_exhaustion_does_not_create_authority", "authority_created", "RECEIPT_EXHAUSTION_CREATES_AUTHORITY"),
        ("receipt_exhaustion_does_not_create_currentness", "currentness_created", "RECEIPT_EXHAUSTION_CREATES_CURRENTNESS"),
        ("receipt_exhaustion_does_not_validate_source", "source_validated_by_receiving_context", "RECEIPT_EXHAUSTION_VALIDATES_SOURCE"),
        ("receipt_exhaustion_does_not_invalidate_source", "source_invalidated_by_receiving_context", "RECEIPT_EXHAUSTION_INVALIDATES_SOURCE"),
        ("receipt_exhaustion_does_not_replace_source", "source_replaced", "RECEIPT_EXHAUSTION_REPLACES_SOURCE"),
        ("receipt_exhaustion_does_not_create_operation_permission", "operation_permission_created", "RECEIPT_EXHAUSTION_CREATES_OPERATION_PERMISSION"),
        ("receipt_exhaustion_does_not_create_governance", "receiving_context_governance_created", "RECEIPT_EXHAUSTION_CREATES_GOVERNANCE"),
        ("receipt_exhaustion_does_not_open_publication_flow", "publication_flow_opened", "RECEIPT_EXHAUSTION_OPENS_PUBLICATION_FLOW"),
        ("receipt_exhaustion_does_not_create_public_readiness", "public_launch_readiness_created", "RECEIPT_EXHAUSTION_CREATES_PUBLIC_READINESS"),
        ("receipt_exhaustion_does_not_claim_final_completion", "final_completion_claimed", "RECEIPT_EXHAUSTION_CLAIMS_FINAL_COMPLETION"),
        ("receipt_exhaustion_does_not_authorize_continuation", "continuation_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_CONTINUATION"),
        ("receipt_exhaustion_does_not_authorize_follow_on_work", "follow_on_work_authorized", "RECEIPT_EXHAUSTION_AUTHORIZES_FOLLOW_ON_WORK"),
        ("conformance_remains_future_work", "reception_conformance_passed", "RECEIPT_EXHAUSTION_CLAIMS_CONFORMANCE_PASSED"),
        ("closure_remains_future_work", "reception_closure_passed", "RECEIPT_EXHAUSTION_CLAIMS_CLOSURE_PASSED"),
    )
    for check_name, key, code in anti_collapse_checks:
        checks.append(
            _check(
                check_name,
                not _contains_truthy_key(request, key)
                and not _contains_truthy_key(selected, key),
                check_name.replace("_", " "),
                request.get(key),
                code,
            )
        )

    checks.extend(
        [
            _check(
                "no_mutation_replay_merge",
                not any(
                    _contains_truthy_key(request, key)
                    or _contains_truthy_key(selected, key)
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
                "required receipt / exhaustion non-claims explicit and false",
                request.get("declared_non_claims"),
                "NON_CLAIM_MISSING_OR_FLIPPED",
            ),
        ]
    )
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
    selected_recognition, selected_recognition_path, selected_load_code = (
        _load_selected_recognition_result(request)
    )
    selected_recognition_dict = selected_recognition or {}
    selected_recognition_outcome = _extract_recognition_outcome(
        request, selected_recognition
    )
    selected_recognition_id = _extract_recognition_id(request, selected_recognition)
    selected_recognition_failed_count = (
        _failed_check_count(selected_recognition_dict)
        if selected_recognition is not None
        else None
    )

    selected_non_capture_result = _first_present(
        request.get("selected_non_capture_result"),
        _nested_selected_non_capture(selected_recognition_dict),
    )
    selected_eligibility_result = _first_present(
        request.get("selected_eligibility_result"),
        _nested_selected_eligibility(
            selected_recognition_dict,
            selected_non_capture_result,
        ),
    )
    selected_receiving_context_role_result = _first_present(
        request.get("selected_receiving_context_role_result"),
        _nested_role_result(
            selected_recognition_dict,
            selected_non_capture_result,
            selected_eligibility_result,
        ),
    )
    selected_identity_preservation_result = _first_present(
        request.get("selected_identity_preservation_result"),
        _nested_identity_result(
            selected_recognition_dict,
            selected_non_capture_result,
            selected_eligibility_result,
            selected_receiving_context_role_result,
        ),
    )
    selected_request_declaration_result = _first_present(
        request.get("selected_reception_request_declaration_result"),
        _nested_request_declaration(
            selected_recognition_dict,
            selected_non_capture_result,
            selected_eligibility_result,
            selected_receiving_context_role_result,
            selected_identity_preservation_result,
        ),
    )
    selected_source_body_surface = _nested_surface(
        request,
        selected_recognition_dict,
        selected_non_capture_result,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
    )
    receiving_context = _nested_receiving_context(
        request,
        selected_recognition_dict,
        selected_non_capture_result,
        selected_eligibility_result,
        selected_receiving_context_role_result,
    )
    receiving_context_type = _context_type(
        request, receiving_context, selected_recognition_dict
    )

    reception_class = _first_present(
        request.get("reception_class"),
        _value_at(selected_recognition_dict, "recognition_basis", "reception_class"),
        _value_at(
            selected_recognition_dict,
            "source_body_reception_recognition_summary",
            "reception_class",
        ),
    )
    reception_purpose = _first_present(
        request.get("reception_purpose"),
        _value_at(selected_recognition_dict, "recognition_basis", "reception_purpose"),
        _value_at(
            selected_recognition_dict,
            "source_body_reception_recognition_summary",
            "reception_purpose",
        ),
    )
    reception_limits = _first_present(
        request.get("reception_limits"),
        _value_at(selected_recognition_dict, "recognition_basis", "reception_limits"),
    )
    selected_receiving_context_role = _first_present(
        request.get("selected_receiving_context_role"),
        _value_at(
            selected_recognition_dict,
            "recognition_basis",
            "selected_receiving_context_role",
        ),
    )
    receiving_context_role_class = _first_present(
        request.get("receiving_context_role_class"),
        _value_at(
            selected_recognition_dict,
            "recognition_basis",
            "receiving_context_role_class",
        ),
    )
    receiving_context_role_limits = _first_present(
        request.get("receiving_context_role_limits"),
        _value_at(
            selected_recognition_dict,
            "recognition_basis",
            "receiving_context_role_limits",
        ),
    )
    recognition_basis = _first_present(
        request.get("recognition_basis"),
        _value_at(selected_recognition_dict, "recognition_basis", "recognition_basis"),
        selected_recognition_dict.get("recognition_basis"),
    )
    recognition_limits = _first_present(
        request.get("recognition_limits"),
        _value_at(selected_recognition_dict, "recognition_limits", "recognition_limits"),
        selected_recognition_dict.get("recognition_limits"),
    )
    recognition_scope = _first_present(
        request.get("recognition_scope"),
        selected_recognition_dict.get("recognition_scope"),
    )
    receipt_exhaustion_basis = request.get("receipt_exhaustion_basis")
    recognition_record_receipt_basis = request.get("recognition_record_receipt_basis")
    recognition_record_exhaustion_basis = request.get(
        "recognition_record_exhaustion_basis"
    )
    scope_values = _scope_values(request.get("receipt_exhaustion_scope"))
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_RECEIPT_EXHAUSTION_SCOPE
    ]

    block_code = _determine_block_code(
        request,
        selected_recognition,
        selected_load_code,
        selected_recognition_outcome,
        selected_recognition_failed_count,
        selected_non_capture_result,
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
        receipt_exhaustion_basis,
        recognition_record_receipt_basis,
        recognition_record_exhaustion_basis,
        unsupported_scope,
    )

    requested_outcome = request.get("requested_receipt_exhaustion_outcome") or OUTCOME_RECORDED
    if block_code:
        outcome = OUTCOME_BLOCKED
    elif request.get("receipt_exhaustion_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_NOT_RECORDED:
        outcome = OUTCOME_NOT_RECORDED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_RECORDED:
        outcome = OUTCOME_RECORDED
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"

    recorded = outcome == OUTCOME_RECORDED
    checks = _build_checks(
        block_code,
        request,
        selected_recognition,
        selected_recognition_outcome,
        selected_recognition_failed_count,
        selected_non_capture_result,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
        selected_request_declaration_result,
        selected_source_body_surface,
        receiving_context,
        receiving_context_type,
        receipt_exhaustion_basis,
        recognition_record_receipt_basis,
        recognition_record_exhaustion_basis,
        unsupported_scope,
    )

    result_id_seed = _safe_component(
        request.get("receipt_exhaustion_request_id") or selected_recognition_id,
        "source_body_reception_receipt_exhaustion",
    )
    metadata = {
        "source_body_reception_receipt_exhaustion_result_id": (
            f"{result_id_seed}__source_body_reception_receipt_exhaustion_result"
        ),
        "source_body_reception_receipt_exhaustion_result_type": (
            "source_body_reception_receipt_exhaustion_boundary_result"
        ),
        "source_body_reception_receipt_exhaustion_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }

    source_body_identity_basis = _first_present(
        request.get("source_body_identity_basis"),
        _value_at(
            selected_recognition_dict,
            "recognition_basis",
            "source_body_identity_basis",
        ),
        _value_at(selected_source_body_surface, "source_body_identity_basis"),
    )
    source_body_lineage_basis = _first_present(
        request.get("source_body_lineage_basis"),
        _value_at(
            selected_recognition_dict,
            "recognition_basis",
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

    recognition_recorded_by_selected_result = (
        selected_recognition_outcome == REQUIRED_RECOGNITION_OUTCOME
        and selected_recognition_failed_count == 0
    )

    selected_recognition_section = {
        "selected_recognition_result_id": selected_recognition_id,
        "selected_recognition_result_outcome": selected_recognition_outcome,
        "selected_recognition_result_path": selected_recognition_path,
        "selected_recognition_outcome_is_recorded": (
            selected_recognition_outcome == REQUIRED_RECOGNITION_OUTCOME
        ),
        "selected_recognition_result_failed_check_count_zero": (
            selected_recognition_failed_count == 0
        ),
        "selected_recognition_result_preserved": selected_recognition is not None,
        "selected_recognition_result_recorded": selected_recognition is not None,
        "selected_non_capture_result_preserved": _present(selected_non_capture_result),
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
        "source_body_reception_recognition_recorded": (
            recognition_recorded_by_selected_result
        ),
        "reception_recognized": recognition_recorded_by_selected_result,
        "recognition_bounded_for_accounting_only": (
            recognition_recorded_by_selected_result
        ),
        "recognition_is_not_authorization": True,
        "recognition_is_not_source_receipt": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "raw_selected_recognition_result": copy.deepcopy(selected_recognition),
    }

    declared_question = {
        "receipt_exhaustion_request_id": request.get("receipt_exhaustion_request_id"),
        "receipt_exhaustion_question": request.get("receipt_exhaustion_question"),
        "receipt_exhaustion_intent": request.get("receipt_exhaustion_intent"),
        "declared_receipt_exhaustion_request_path": request_path,
        "selected_recognition_result_id": selected_recognition_id,
        "selected_recognition_result_outcome": selected_recognition_outcome,
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_reference": surface_reference,
        "receiving_context_id": receiving_context_id,
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": reception_purpose,
        "receipt_exhaustion_is_not_source_receipt": True,
        "receipt_exhaustion_is_not_authorization": True,
        "receipt_exhaustion_does_not_decide_conformance": True,
        "receipt_exhaustion_does_not_decide_closure": True,
    }

    receipt_exhaustion_basis_section = {
        "selected_recognition_result": copy.deepcopy(selected_recognition),
        "selected_non_capture_result": copy.deepcopy(selected_non_capture_result),
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
        "recognition_basis": copy.deepcopy(recognition_basis),
        "recognition_limits": copy.deepcopy(recognition_limits),
        "recognition_scope": copy.deepcopy(recognition_scope),
        "receipt_exhaustion_basis": copy.deepcopy(receipt_exhaustion_basis),
        "receipt_exhaustion_of_recognition_accounting_only": True,
        "recognition_record_receipt_only": True,
        "recognition_record_exhaustion_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "receipt_exhaustion_is_not_authorization": True,
        "receipt_exhaustion_is_not_source_receipt": True,
        "receipt_exhaustion_is_not_conformance": True,
        "receipt_exhaustion_is_not_closure": True,
        "conformance_requires_separate_boundary": True,
        "closure_requires_separate_boundary": True,
    }

    recognition_record_receipt_basis_section = {
        "recognition_record_receipt_basis": copy.deepcopy(
            recognition_record_receipt_basis
        ),
        "recognition_record_receipted_for_accounting_only": True,
        "recognized_reception_accounting_receipt_recorded_only": recorded,
        "source_receipt_not_recorded": True,
        "source_received": False,
        "reception_authorization": False,
        "receipt_is_not_source_receipt": True,
        "receipt_is_not_authorization": True,
        "receipt_is_not_adoption": True,
        "receipt_is_not_conformance": True,
        "receipt_is_not_closure": True,
    }

    recognition_record_exhaustion_basis_section = {
        "recognition_record_exhaustion_basis": copy.deepcopy(
            recognition_record_exhaustion_basis
        ),
        "recognition_record_exhaustion_recorded_for_this_layer_only": recorded,
        "recognized_reception_accounting_exhausted_only": recorded,
        "exhaustion_is_not_closure": True,
        "exhaustion_is_not_final_completion": True,
        "exhaustion_is_not_conformance": True,
        "exhaustion_does_not_authorize_continuation": True,
        "exhaustion_does_not_authorize_follow_on_work": True,
    }

    receipt_exhaustion_scope_section = {
        "selected_receipt_exhaustion_scope_values": scope_values,
        "all_selected_scope_values_supported": not unsupported_scope,
        "unsupported_receipt_exhaustion_scope_values": list(unsupported_scope),
        "recognition_record_receipt_only": "RECOGNITION_RECORD_RECEIPT_ONLY" in scope_values,
        "recognition_record_exhaustion_only": "RECOGNITION_RECORD_EXHAUSTION_ONLY" in scope_values,
        "receipt_exhaustion_is_not_source_receipt": (
            "RECEIPT_EXHAUSTION_IS_NOT_SOURCE_RECEIPT" in scope_values
        ),
        "receipt_exhaustion_is_not_authorization": (
            "RECEIPT_EXHAUSTION_IS_NOT_AUTHORIZATION" in scope_values
        ),
        "receipt_exhaustion_does_not_receive_source": (
            "RECEIPT_EXHAUSTION_DOES_NOT_RECEIVE_SOURCE" in scope_values
        ),
        "receipt_exhaustion_does_not_create_source_receipt": (
            "RECEIPT_EXHAUSTION_DOES_NOT_CREATE_SOURCE_RECEIPT" in scope_values
        ),
        "receipt_exhaustion_is_not_adoption": (
            "RECEIPT_EXHAUSTION_IS_NOT_ADOPTION" in scope_values
        ),
        "receipt_exhaustion_is_not_authority": (
            "RECEIPT_EXHAUSTION_IS_NOT_AUTHORITY" in scope_values
        ),
        "receipt_exhaustion_is_not_currentness": (
            "RECEIPT_EXHAUSTION_IS_NOT_CURRENTNESS" in scope_values
        ),
        "receipt_exhaustion_is_not_validation": (
            "RECEIPT_EXHAUSTION_IS_NOT_VALIDATION" in scope_values
        ),
        "receipt_exhaustion_is_not_invalidation": (
            "RECEIPT_EXHAUSTION_IS_NOT_INVALIDATION" in scope_values
        ),
        "receipt_exhaustion_is_not_operation_permission": (
            "RECEIPT_EXHAUSTION_IS_NOT_OPERATION_PERMISSION" in scope_values
        ),
        "receipt_exhaustion_is_not_publication_flow": (
            "RECEIPT_EXHAUSTION_IS_NOT_PUBLICATION_FLOW" in scope_values
        ),
        "conformance_requires_separate_boundary": (
            "CONFORMANCE_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
    }

    non_claims = _build_non_claims(recorded)
    receipt_exhaustion_statement = {
        "source_body_reception_receipt_exhaustion_recorded": recorded,
        "reception_recognition_receipt_recorded": recorded,
        "reception_recognition_exhaustion_recorded": recorded,
        "recognized_reception_accounting_receipt_recorded": recorded,
        "recognized_reception_accounting_exhausted": recorded,
        "selected_recognition_result_preserved": selected_recognition is not None,
        "selected_recognition_result_recorded": selected_recognition is not None,
        "selected_recognition_result_failed_check_count_zero": (
            selected_recognition_failed_count == 0
        ),
        "selected_non_capture_result_preserved": _present(selected_non_capture_result),
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
        "reception_recognized": selected_recognition_outcome == REQUIRED_RECOGNITION_OUTCOME,
        "recognition_bounded_for_accounting_only": True,
        "receipt_exhaustion_of_recognition_accounting_only": True,
        "recognition_record_receipt_only": True,
        "recognition_record_exhaustion_only": True,
        "receipt_exhaustion_is_not_source_receipt": True,
        "receipt_exhaustion_is_not_authorization": True,
        "receipt_exhaustion_does_not_receive_source": True,
        "receipt_exhaustion_does_not_create_source_receipt": True,
        "receipt_exhaustion_is_not_conformance": True,
        "receipt_exhaustion_is_not_closure": True,
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
        "not_recorded_does_not_record_source_receipt": True,
        "not_recorded_does_not_create_source_receipt": True,
        "not_recorded_does_not_replace": True,
        "not_recorded_does_not_validate": True,
        "not_recorded_does_not_invalidate": True,
        "not_recorded_does_not_create_currentness": True,
        "not_recorded_does_not_claim_conformance": True,
        "not_recorded_does_not_claim_closure": True,
    }

    result: dict[str, Any] = {
        "source_body_reception_receipt_exhaustion_metadata": metadata,
        "declared_receipt_exhaustion_question": declared_question,
        "selected_recognition_result": selected_recognition_section,
        "selected_source_body_surface": selected_surface_section,
        "receiving_context": receiving_context_section,
        "receipt_exhaustion_basis": receipt_exhaustion_basis_section,
        "recognition_record_receipt_basis": recognition_record_receipt_basis_section,
        "recognition_record_exhaustion_basis": recognition_record_exhaustion_basis_section,
        "receipt_exhaustion_scope": receipt_exhaustion_scope_section,
        "receipt_exhaustion_checks": checks,
        "receipt_exhaustion_statement": receipt_exhaustion_statement,
        "receipt_exhaustion_non_meaning": _build_receipt_exhaustion_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_recorded_basis": not_recorded_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason") or block_code),
    }
    result["source_body_reception_receipt_exhaustion_summary"] = (
        build_source_body_reception_receipt_exhaustion_summary(result)
    )
    return result


def resolve_source_body_reception_receipt_exhaustion_boundary(
    declared_receipt_exhaustion_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared source-body reception receipt / exhaustion request."""
    if declared_receipt_exhaustion_request is None:
        return _build_result({})
    if not isinstance(declared_receipt_exhaustion_request, Mapping):
        return _blocked_malformed_request(
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED"
        )
    return _build_result(copy.deepcopy(dict(declared_receipt_exhaustion_request)))


def resolve_source_body_reception_receipt_exhaustion_boundary_from_path(
    declared_receipt_exhaustion_request_path: Path | str,
) -> dict:
    """Load and resolve one declared source-body reception receipt / exhaustion request."""
    request, error = _read_json_object(declared_receipt_exhaustion_request_path)
    if error == "unreadable":
        return _blocked_malformed_request(
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_UNREADABLE",
            str(declared_receipt_exhaustion_request_path),
        )
    if error == "malformed":
        return _blocked_malformed_request(
            "DECLARED_RECEIPT_EXHAUSTION_REQUEST_MALFORMED",
            str(declared_receipt_exhaustion_request_path),
        )
    return _build_result(
        request or {},
        request_path=str(declared_receipt_exhaustion_request_path),
    )


def _blocked_malformed_request(code: str, request_path: str | None = None) -> dict:
    request = {
        "receipt_exhaustion_request_id": None,
        "receipt_exhaustion_question": None,
        "receipt_exhaustion_intent": None,
        "selected_recognition_result": None,
        "receipt_exhaustion_basis": None,
        "recognition_record_receipt_basis": None,
        "recognition_record_exhaustion_basis": None,
        "receipt_exhaustion_scope": [],
        "declared_non_claims": {},
        "block_reason": code,
    }
    result = _build_result(request, request_path=request_path)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = _block(code, request_path or code)
    result["source_body_reception_receipt_exhaustion_summary"] = (
        build_source_body_reception_receipt_exhaustion_summary(result)
    )
    return result


def build_source_body_reception_receipt_exhaustion_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the bounded summary for a receipt / exhaustion boundary result."""
    checks = result.get("receipt_exhaustion_checks") or []
    passed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and _truthy(check.get("passed"))
    )
    failed_check_count = sum(
        1
        for check in checks
        if isinstance(check, Mapping) and not _truthy(check.get("passed"))
    )
    question = result.get("declared_receipt_exhaustion_question") or {}
    selected = result.get("selected_recognition_result") or {}
    surface = result.get("selected_source_body_surface") or {}
    context = result.get("receiving_context") or {}
    statement = result.get("receipt_exhaustion_statement") or {}
    block = result.get("block") or {}
    non_claims = result.get("non_claims") or {}
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "receipt_exhaustion_request_id": question.get("receipt_exhaustion_request_id"),
        "receipt_exhaustion_question": question.get("receipt_exhaustion_question"),
        "receipt_exhaustion_intent": question.get("receipt_exhaustion_intent"),
        "selected_recognition_result_id": selected.get("selected_recognition_result_id"),
        "selected_recognition_result_outcome": selected.get(
            "selected_recognition_result_outcome"
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
        "receipt_exhaustion_recorded": _truthy(
            statement.get("source_body_reception_receipt_exhaustion_recorded")
        ),
        "recognition_record_receipt_recorded": _truthy(
            statement.get("reception_recognition_receipt_recorded")
        ),
        "recognition_record_exhaustion_recorded": _truthy(
            statement.get("reception_recognition_exhaustion_recorded")
        ),
        "recognized_reception_accounting_receipt_recorded": _truthy(
            statement.get("recognized_reception_accounting_receipt_recorded")
        ),
        "recognized_reception_accounting_exhausted": _truthy(
            statement.get("recognized_reception_accounting_exhausted")
        ),
        "not_recorded": outcome == OUTCOME_NOT_RECORDED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_recognition_result_preserved": statement.get(
            "selected_recognition_result_preserved"
        ),
        "selected_recognition_result_recorded": statement.get(
            "selected_recognition_result_recorded"
        ),
        "selected_recognition_result_failed_check_count_zero": statement.get(
            "selected_recognition_result_failed_check_count_zero"
        ),
        "selected_non_capture_result_preserved": statement.get(
            "selected_non_capture_result_preserved"
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
        "reception_recognized": statement.get("reception_recognized"),
        "recognition_bounded_for_accounting_only": statement.get(
            "recognition_bounded_for_accounting_only"
        ),
        "receipt_exhaustion_of_recognition_accounting_only": statement.get(
            "receipt_exhaustion_of_recognition_accounting_only"
        ),
        "recognition_record_receipt_only": statement.get(
            "recognition_record_receipt_only"
        ),
        "recognition_record_exhaustion_only": statement.get(
            "recognition_record_exhaustion_only"
        ),
        "receipt_exhaustion_not_source_receipt": statement.get(
            "receipt_exhaustion_is_not_source_receipt"
        ),
        "receipt_exhaustion_not_authorization": statement.get(
            "receipt_exhaustion_is_not_authorization"
        ),
        "no_source_received": non_claims.get("source_received") is False,
        "no_source_receipt_recorded": non_claims.get("source_receipt_recorded") is False,
        "no_source_receipt_created": non_claims.get("source_receipt_created") is False,
        "conformance_future": statement.get("conformance_requires_separate_boundary"),
        "closure_future": statement.get("closure_requires_separate_boundary"),
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


def write_source_body_reception_receipt_exhaustion_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive source-body reception receipt / exhaustion result artifact."""
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionReceiptExhaustionBoundaryError(
            "Receipt / exhaustion result must be a mapping."
        )
    if output_path is None:
        summary = result.get("source_body_reception_receipt_exhaustion_summary") or {}
        stem = _safe_component(
            summary.get("receipt_exhaustion_request_id")
            or summary.get("selected_recognition_result_id"),
            "source_body_reception_receipt_exhaustion",
        )
        output_path = (
            SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_BOUNDARY_ROOT
            / f"{stem}__source_body_reception_receipt_exhaustion_result.json"
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


def build_declared_source_body_reception_receipt_exhaustion_request(
    receipt_exhaustion_request_id: str,
    receipt_exhaustion_question: str,
    selected_recognition_result: Mapping[str, Any] | str,
    receipt_exhaustion_basis: Mapping[str, Any] | str,
    recognition_record_receipt_basis: Mapping[str, Any] | str,
    recognition_record_exhaustion_basis: Mapping[str, Any] | str,
    receipt_exhaustion_scope: Sequence[str] | Mapping[str, Any],
    receipt_exhaustion_intent: str = INTENT_RECORD,
    *,
    selected_recognition_result_path: str | None = None,
    selected_recognition_result_id: str | None = None,
    selected_recognition_result_outcome: str | None = None,
    requested_receipt_exhaustion_outcome: str = OUTCOME_RECORDED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_recorded_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared receipt / exhaustion request with required non-claims false."""
    request: dict[str, Any] = {
        "receipt_exhaustion_request_id": receipt_exhaustion_request_id,
        "receipt_exhaustion_question": receipt_exhaustion_question,
        "receipt_exhaustion_intent": receipt_exhaustion_intent,
        "receipt_exhaustion_basis": copy.deepcopy(receipt_exhaustion_basis),
        "recognition_record_receipt_basis": copy.deepcopy(
            recognition_record_receipt_basis
        ),
        "recognition_record_exhaustion_basis": copy.deepcopy(
            recognition_record_exhaustion_basis
        ),
        "receipt_exhaustion_scope": copy.deepcopy(receipt_exhaustion_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "requested_receipt_exhaustion_outcome": requested_receipt_exhaustion_outcome,
    }
    if selected_recognition_result_path is not None:
        request["selected_recognition_result_path"] = selected_recognition_result_path
    elif isinstance(selected_recognition_result, Mapping):
        request["selected_recognition_result"] = copy.deepcopy(
            dict(selected_recognition_result)
        )
    else:
        request["selected_recognition_result"] = selected_recognition_result
    if selected_recognition_result_id is not None:
        request["selected_recognition_result_id"] = selected_recognition_result_id
    if selected_recognition_result_outcome is not None:
        request["selected_recognition_result_outcome"] = (
            selected_recognition_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = copy.deepcopy(additional_basis_context)
    if not_recorded_basis is not None:
        request["not_recorded_basis"] = copy.deepcopy(not_recorded_basis)
    return request
