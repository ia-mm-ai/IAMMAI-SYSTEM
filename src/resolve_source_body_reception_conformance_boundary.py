"""Resolve the source-body reception conformance boundary.

This module records conformance of one recorded source-body reception
boundary chain to its own prior constraints. Conformance is not reception
authorization, source receipt, source received, adoption, authority,
currentness, operation permission, public readiness, final completion, or
closure.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class SourceBodyReceptionConformanceBoundaryError(Exception):
    """Raised for hard conformance-boundary path or shape failures."""


RESOLVER_MODULE = "resolve_source_body_reception_conformance_boundary"
RESULT_VERSION = "0.1.0"

SOURCE_BODY_RECEPTION_CONFORMANCE_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_conformance_boundary"
)

OUTCOME_PASSED = "SOURCE_BODY_RECEPTION_CONFORMANCE_PASSED"
OUTCOME_NOT_PASSED = "SOURCE_BODY_RECEPTION_CONFORMANCE_NOT_PASSED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_CONFORMANCE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_CONFORMANCE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_PASSED,
    OUTCOME_NOT_PASSED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

REQUIRED_RECEIPT_EXHAUSTION_OUTCOME = (
    "SOURCE_BODY_RECEPTION_RECEIPT_EXHAUSTION_RECORDED"
)

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_CONFORMANCE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_CONFORMANCE"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_CONFORMANCE_REVIEW"
SUPPORTED_CONFORMANCE_INTENTS = {
    INTENT_RECORD,
    INTENT_DO_NOT_RECORD,
    INTENT_BLOCK,
}

SUPPORTED_CONFORMANCE_SCOPE = {
    "RECEPTION_CHAIN_CONFORMANCE_ONLY",
    "CONFORMANCE_IS_NOT_AUTHORIZATION",
    "CONFORMANCE_IS_NOT_SOURCE_RECEIPT",
    "CONFORMANCE_DOES_NOT_RECEIVE_SOURCE",
    "CONFORMANCE_DOES_NOT_CREATE_SOURCE_RECEIPT",
    "CONFORMANCE_IS_NOT_ADOPTION",
    "CONFORMANCE_IS_NOT_AUTHORITY",
    "CONFORMANCE_IS_NOT_CURRENTNESS",
    "CONFORMANCE_IS_NOT_VALIDATION",
    "CONFORMANCE_IS_NOT_INVALIDATION",
    "CONFORMANCE_IS_NOT_OPERATION_PERMISSION",
    "CONFORMANCE_IS_NOT_PUBLICATION_FLOW",
    "CONFORMANCE_IS_NOT_CLOSURE",
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
    "reception_closure_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_PASSED_TRUE_FIELDS = (
    "source_body_reception_conformance_recorded",
    "source_body_reception_conformance_passed",
    "reception_boundary_chain_conformance_passed",
    "reception_family_conformance_passed",
)

COLLAPSE_FIELD_CODES = (
    ("reception_authorized", "CONFORMANCE_AUTHORIZES_RECEPTION"),
    ("source_received", "CONFORMANCE_RECEIVES_SOURCE"),
    ("source_receipt_recorded", "CONFORMANCE_RECORDS_SOURCE_RECEIPT"),
    ("source_receipt_created", "CONFORMANCE_CREATES_SOURCE_RECEIPT"),
    ("receiving_context_governance_created", "CONFORMANCE_CREATES_GOVERNANCE"),
    ("receiving_context_became_source", "CONFORMANCE_TREATS_CONTEXT_AS_SOURCE"),
    (
        "receiving_context_became_authority",
        "CONFORMANCE_TREATS_CONTEXT_AS_AUTHORITY",
    ),
    ("receiving_context_became_current", "CONFORMANCE_TREATS_CONTEXT_AS_CURRENT"),
    ("receiving_context_became_receiver", "CONFORMANCE_TREATS_CONTEXT_AS_RECEIVER"),
    ("receiving_context_became_adopter", "CONFORMANCE_TREATS_CONTEXT_AS_ADOPTER"),
    (
        "receiving_context_became_validator",
        "CONFORMANCE_TREATS_CONTEXT_AS_VALIDATOR",
    ),
    (
        "receiving_context_became_invalidator",
        "CONFORMANCE_TREATS_CONTEXT_AS_INVALIDATOR",
    ),
    ("receiving_context_became_operator", "CONFORMANCE_TREATS_CONTEXT_AS_OPERATOR"),
    ("source_validated_by_receiving_context", "CONFORMANCE_VALIDATES_SOURCE"),
    ("source_invalidated_by_receiving_context", "CONFORMANCE_INVALIDATES_SOURCE"),
    ("source_replaced", "CONFORMANCE_REPLACES_SOURCE"),
    ("adoption_created", "CONFORMANCE_CREATES_ADOPTION"),
    ("authority_created", "CONFORMANCE_CREATES_AUTHORITY"),
    ("currentness_created", "CONFORMANCE_CREATES_CURRENTNESS"),
    ("standing_created", "CONFORMANCE_CREATES_STANDING"),
    ("standing_propagated", "CONFORMANCE_CREATES_STANDING_PROPAGATION"),
    ("vessel_relation_created", "CONFORMANCE_CREATES_VESSEL_RELATION"),
    ("derivative_relation_created", "CONFORMANCE_CREATES_DERIVATIVE_RELATION"),
    ("operation_permission_created", "CONFORMANCE_CREATES_OPERATION_PERMISSION"),
    ("public_launch_readiness_created", "CONFORMANCE_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "CONFORMANCE_CLAIMS_FINAL_COMPLETION"),
    ("follow_on_work_authorized", "CONFORMANCE_AUTHORIZES_FOLLOW_ON_WORK"),
    ("continuation_authorized", "CONFORMANCE_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "CONFORMANCE_OPENS_PUBLICATION_FLOW"),
    ("reception_closure_passed", "CONFORMANCE_CLAIMS_CLOSURE_PASSED"),
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
            "source_body_reception_receipt_exhaustion_summary",
            "failed_check_count",
        ),
        _value_at(result, "summary", "failed_check_count"),
    )
    if isinstance(explicit, int):
        return explicit
    checks = _first_present(result.get("receipt_exhaustion_checks"), result.get("checks"))
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
            scope.get("selected_conformance_scope_values"),
            scope.get("conformance_scope_values"),
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


def _load_selected_receipt_exhaustion_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    result_path = request.get("selected_receipt_exhaustion_result_path")
    if _present(result_path):
        loaded, error = _read_json_object(str(result_path))
        if error == "unreadable":
            return None, str(result_path), "RECEIPT_EXHAUSTION_RESULT_UNREADABLE"
        if error == "malformed":
            return None, str(result_path), "RECEIPT_EXHAUSTION_RESULT_MALFORMED"
        return loaded, str(result_path), None
    selected = request.get("selected_receipt_exhaustion_result")
    if isinstance(selected, Mapping):
        return copy.deepcopy(dict(selected)), None, None
    if _present(selected):
        return None, None, "RECEIPT_EXHAUSTION_RESULT_MALFORMED"
    return None, None, None


def _extract_receipt_exhaustion_outcome(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_receipt_exhaustion_result_outcome"),
        request.get("expected_selected_receipt_exhaustion_outcome"),
        selected.get("outcome"),
        _value_at(
            selected,
            "source_body_reception_receipt_exhaustion_summary",
            "outcome",
        ),
        _value_at(selected, "receipt_exhaustion_statement", "outcome"),
    )


def _extract_receipt_exhaustion_id(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None
) -> Any:
    selected = selected or {}
    return _first_present(
        request.get("selected_receipt_exhaustion_result_id"),
        _value_at(
            selected,
            "source_body_reception_receipt_exhaustion_metadata",
            "source_body_reception_receipt_exhaustion_result_id",
        ),
        _value_at(
            selected,
            "source_body_reception_receipt_exhaustion_summary",
            "source_body_reception_receipt_exhaustion_result_id",
        ),
        selected.get("source_body_reception_receipt_exhaustion_result_id"),
        selected.get("receipt_exhaustion_request_id"),
        _value_at(
            selected,
            "declared_receipt_exhaustion_question",
            "receipt_exhaustion_request_id",
        ),
    )


def _nested_selected_recognition(selected: Mapping[str, Any]) -> Any:
    return _first_present(
        _value_at(selected, "conformance_basis", "selected_recognition_result"),
        _value_at(selected, "receipt_exhaustion_basis", "selected_recognition_result"),
        _value_at(selected, "selected_recognition_result", "raw_selected_recognition_result"),
        selected.get("selected_recognition_result"),
    )


def _nested_selected_non_capture(
    selected: Mapping[str, Any], selected_recognition: Any
) -> Any:
    return _first_present(
        _value_at(selected, "conformance_basis", "selected_non_capture_result"),
        _value_at(selected, "receipt_exhaustion_basis", "selected_non_capture_result"),
        _value_at(selected_recognition, "recognition_basis", "selected_non_capture_result"),
        _value_at(
            selected_recognition,
            "selected_non_capture_result",
            "raw_selected_non_capture_result",
        ),
        _value_at(selected_recognition, "selected_non_capture_result"),
    )


def _nested_selected_eligibility(
    selected: Mapping[str, Any], selected_recognition: Any, non_capture: Any
) -> Any:
    return _first_present(
        _value_at(selected, "conformance_basis", "selected_eligibility_result"),
        _value_at(selected, "receipt_exhaustion_basis", "selected_eligibility_result"),
        _value_at(selected_recognition, "recognition_basis", "selected_eligibility_result"),
        _value_at(non_capture, "non_capture_basis", "selected_eligibility_result"),
        _value_at(non_capture, "selected_eligibility_result", "raw_selected_eligibility_result"),
        _value_at(non_capture, "selected_eligibility_result"),
    )


def _nested_role_result(
    selected: Mapping[str, Any],
    selected_recognition: Any,
    non_capture: Any,
    eligibility: Any,
) -> Any:
    return _first_present(
        _value_at(selected, "conformance_basis", "selected_receiving_context_role_result"),
        _value_at(
            selected,
            "receipt_exhaustion_basis",
            "selected_receiving_context_role_result",
        ),
        _value_at(
            selected_recognition,
            "recognition_basis",
            "selected_receiving_context_role_result",
        ),
        _value_at(non_capture, "non_capture_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "eligibility_basis", "selected_receiving_context_role_result"),
        _value_at(eligibility, "selected_receiving_context_role_result"),
    )


def _nested_identity_result(
    selected: Mapping[str, Any],
    selected_recognition: Any,
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
) -> Any:
    return _first_present(
        _value_at(selected, "conformance_basis", "selected_identity_preservation_result"),
        _value_at(
            selected,
            "receipt_exhaustion_basis",
            "selected_identity_preservation_result",
        ),
        _value_at(
            selected_recognition,
            "recognition_basis",
            "selected_identity_preservation_result",
        ),
        _value_at(non_capture, "non_capture_basis", "selected_identity_preservation_result"),
        _value_at(eligibility, "eligibility_basis", "selected_identity_preservation_result"),
        _value_at(
            role_result,
            "receiving_context_role_basis",
            "selected_identity_preservation_result",
        ),
        _value_at(role_result, "selected_identity_preservation_result"),
    )


def _nested_request_declaration(
    selected: Mapping[str, Any],
    selected_recognition: Any,
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        _value_at(
            selected,
            "conformance_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            selected,
            "receipt_exhaustion_basis",
            "selected_reception_request_declaration_result",
        ),
        _value_at(
            selected_recognition,
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
    selected_recognition: Any,
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
    identity_result: Any,
) -> Any:
    return _first_present(
        request.get("selected_source_body_surface"),
        _value_at(selected, "conformance_basis", "selected_source_body_surface"),
        _value_at(selected, "receipt_exhaustion_basis", "selected_source_body_surface"),
        _value_at(selected, "selected_source_body_surface", "selected_source_body_surface"),
        selected.get("selected_source_body_surface"),
        _value_at(selected_recognition, "recognition_basis", "selected_source_body_surface"),
        _value_at(selected_recognition, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(non_capture, "non_capture_basis", "selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(eligibility, "selected_source_body_surface"),
        _value_at(role_result, "selected_source_body_surface", "selected_source_body_surface"),
        _value_at(identity_result, "selected_source_body_surface", "selected_source_body_surface"),
    )


def _nested_receiving_context(
    request: Mapping[str, Any],
    selected: Mapping[str, Any],
    selected_recognition: Any,
    non_capture: Any,
    eligibility: Any,
    role_result: Any,
) -> Any:
    return _first_present(
        request.get("receiving_context"),
        _value_at(selected, "conformance_basis", "receiving_context"),
        _value_at(selected, "receipt_exhaustion_basis", "receiving_context"),
        _value_at(selected, "receiving_context", "receiving_context"),
        selected.get("receiving_context"),
        _value_at(selected_recognition, "recognition_basis", "receiving_context"),
        _value_at(selected_recognition, "receiving_context", "receiving_context"),
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
        _value_at(selected, "conformance_basis", "receiving_context_type"),
        _value_at(selected, "receipt_exhaustion_basis", "receiving_context_type"),
        _value_at(
            selected,
            "source_body_reception_receipt_exhaustion_summary",
            "receiving_context_type",
        ),
    )


def _flag(
    selected: Mapping[str, Any],
    request: Mapping[str, Any],
    key: str,
    default: bool = False,
) -> bool:
    value = _first_present(
        request.get(key),
        _value_at(selected, "conformance_statement", key),
        _value_at(selected, "receipt_exhaustion_statement", key),
        _value_at(selected, "selected_receipt_exhaustion_result", key),
        _value_at(selected, "source_body_reception_receipt_exhaustion_summary", key),
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


def _build_non_claims(passed: bool) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_FALSE_NON_CLAIMS}
    non_claims.update({key: bool(passed) for key in ALLOWED_PASSED_TRUE_FIELDS})
    return non_claims


def _build_conformance_non_meaning() -> dict[str, bool]:
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
        "closure_recorded",
        "public_readiness_created",
        "final_completion_claimed",
        "follow_on_work_authorized",
        "continuation_authorized",
        "publication_flow_opened",
    )
    result = {f"does_not_mean_{name}": True for name in meanings}
    result["conformance_is_not_authorization"] = True
    result["conformance_is_not_source_receipt"] = True
    result["conformance_is_not_source_received"] = True
    result["conformance_is_not_closure"] = True
    result["conformance_is_not_final_completion"] = True
    return result


def _build_what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "source-body reception conformance test",
            "source-body reception conformance live artifact",
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
    selected_receipt_exhaustion: Mapping[str, Any] | None,
    selected_load_code: str | None,
    selected_receipt_exhaustion_outcome: Any,
    selected_receipt_exhaustion_failed_count: int | None,
    selected_recognition_result: Any,
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
    conformance_basis: Any,
    conformance_limits: Any,
    unsupported_scope: Sequence[str],
) -> str | None:
    if not _present(request.get("conformance_question")):
        return "CONFORMANCE_QUESTION_UNDECLARED"
    if request.get("conformance_intent") == INTENT_BLOCK:
        return "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if request.get("conformance_intent") not in SUPPORTED_CONFORMANCE_INTENTS:
        return "CONFORMANCE_INTENT_UNSUPPORTED"
    if selected_load_code:
        return selected_load_code
    if not _present(selected_receipt_exhaustion):
        return "RECEIPT_EXHAUSTION_RESULT_MISSING"
    if not _present(selected_receipt_exhaustion_outcome):
        return "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING"
    if selected_receipt_exhaustion_outcome != REQUIRED_RECEIPT_EXHAUSTION_OUTCOME:
        return "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED"
    if selected_receipt_exhaustion_failed_count != 0:
        return "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS"
    if not _present(selected_recognition_result):
        return "RECOGNITION_RESULT_MISSING"
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
    if not _present(conformance_basis):
        return "CONFORMANCE_BASIS_MISSING"
    if not _present(conformance_limits):
        return "CONFORMANCE_LIMITS_MISSING"
    if unsupported_scope:
        return "UNSUPPORTED_CONFORMANCE_SCOPE"
    collapse = _collapse_code(request, selected_receipt_exhaustion)
    if collapse:
        return collapse
    if not _required_non_claims_false(request):
        return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    block_code: str | None,
    request: Mapping[str, Any],
    selected_receipt_exhaustion: Mapping[str, Any] | None,
    selected_receipt_exhaustion_outcome: Any,
    selected_receipt_exhaustion_failed_count: int | None,
    selected_recognition_result: Any,
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
    conformance_basis: Any,
    conformance_limits: Any,
    unsupported_scope: Sequence[str],
) -> list[dict[str, Any]]:
    selected = selected_receipt_exhaustion or {}
    intent_supported = (
        request.get("conformance_intent") in SUPPORTED_CONFORMANCE_INTENTS
        and request.get("conformance_intent") != INTENT_BLOCK
    )
    intent_block_code = (
        "CONFORMANCE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        if request.get("conformance_intent") == INTENT_BLOCK
        else "CONFORMANCE_INTENT_UNSUPPORTED"
    )
    checks = [
        _check(
            "conformance_question_declared",
            _present(request.get("conformance_question")),
            "conformance question declared",
            request.get("conformance_question"),
            "CONFORMANCE_QUESTION_UNDECLARED",
        ),
        _check(
            "conformance_intent_supported",
            intent_supported,
            "conformance intent records bounded chain conformance review",
            request.get("conformance_intent"),
            intent_block_code,
        ),
        _check(
            "selected_receipt_exhaustion_result_present",
            _present(selected_receipt_exhaustion),
            "selected receipt / exhaustion result present",
            _present(selected_receipt_exhaustion),
            "RECEIPT_EXHAUSTION_RESULT_MISSING",
        ),
        _check(
            "selected_receipt_exhaustion_outcome_declared",
            _present(selected_receipt_exhaustion_outcome),
            "selected receipt / exhaustion outcome declared",
            selected_receipt_exhaustion_outcome,
            "RECEIPT_EXHAUSTION_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected_receipt_exhaustion_outcome_recorded",
            selected_receipt_exhaustion_outcome == REQUIRED_RECEIPT_EXHAUSTION_OUTCOME,
            REQUIRED_RECEIPT_EXHAUSTION_OUTCOME,
            selected_receipt_exhaustion_outcome,
            "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected_receipt_exhaustion_failed_check_count_zero",
            selected_receipt_exhaustion_failed_count == 0,
            "selected receipt / exhaustion failed check count is zero",
            selected_receipt_exhaustion_failed_count,
            "RECEIPT_EXHAUSTION_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected_recognition_result_preserved",
            _present(selected_recognition_result)
            and _flag(selected, request, "selected_recognition_result_preserved", True),
            "selected recognition result preserved",
            _present(selected_recognition_result),
            "RECOGNITION_RESULT_MISSING",
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
            and _flag(
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
            and _flag(selected, request, "selected_identity_preservation_result_preserved", True),
            "selected identity preservation result preserved",
            _present(selected_identity_preservation_result),
            "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected_request_declaration_result_preserved",
            _present(selected_request_declaration_result)
            and _flag(
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
            "receiving_context_type_declared",
            _present(receiving_context_type),
            "receiving context type declared",
            receiving_context_type,
            "RECEIVING_CONTEXT_TYPE_MISSING",
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
            "CONFORMANCE_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving_context_is_not_authority",
            _flag(selected, request, "receiving_context_is_not_authority", True),
            "receiving context is not authority",
            _flag(selected, request, "receiving_context_is_not_authority", True),
            "CONFORMANCE_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving_context_is_not_current",
            _flag(selected, request, "receiving_context_is_not_current", True),
            "receiving context is not current",
            _flag(selected, request, "receiving_context_is_not_current", True),
            "CONFORMANCE_TREATS_CONTEXT_AS_CURRENT",
        ),
        _check(
            "recognition_was_recorded",
            _flag(selected, request, "source_body_reception_recognition_recorded", True)
            or _flag(selected, request, "reception_recognized", True),
            "recognition was recorded",
            True,
            "RECOGNITION_RESULT_MISSING",
        ),
        _check(
            "receipt_exhaustion_was_recorded",
            _flag(
                selected,
                request,
                "source_body_reception_receipt_exhaustion_recorded",
                True,
            ),
            "receipt / exhaustion was recorded",
            _flag(
                selected,
                request,
                "source_body_reception_receipt_exhaustion_recorded",
                True,
            ),
            "RECEIPT_EXHAUSTION_RESULT_NOT_RECORDED",
        ),
        _check(
            "receipt_exhaustion_recognition_accounting_only",
            _flag(
                selected,
                request,
                "receipt_exhaustion_of_recognition_accounting_only",
                True,
            )
            or _flag(
                selected,
                request,
                "receipt_exhaustion_remained_recognition_record_accounting_only",
                True,
            ),
            "receipt / exhaustion remained recognition-accounting only",
            True,
        ),
        _check(
            "source_unreceived",
            not _contains_truthy_key(request, "source_received")
            and not _contains_truthy_key(selected, "source_received"),
            "source remains unreceived",
            request.get("source_received"),
            "CONFORMANCE_RECEIVES_SOURCE",
        ),
        _check(
            "source_receipt_unrecorded",
            not _contains_truthy_key(request, "source_receipt_recorded")
            and not _contains_truthy_key(selected, "source_receipt_recorded"),
            "source receipt remains unrecorded",
            request.get("source_receipt_recorded"),
            "CONFORMANCE_RECORDS_SOURCE_RECEIPT",
        ),
        _check(
            "source_receipt_uncreated",
            not _contains_truthy_key(request, "source_receipt_created")
            and not _contains_truthy_key(selected, "source_receipt_created"),
            "source receipt remains uncreated",
            request.get("source_receipt_created"),
            "CONFORMANCE_CREATES_SOURCE_RECEIPT",
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
            "conformance_basis_declared",
            _present(conformance_basis),
            "conformance basis declared",
            conformance_basis,
            "CONFORMANCE_BASIS_MISSING",
        ),
        _check(
            "conformance_limits_declared",
            _present(conformance_limits),
            "conformance limits declared",
            conformance_limits,
            "CONFORMANCE_LIMITS_MISSING",
        ),
        _check(
            "conformance_scope_supported",
            not unsupported_scope,
            "all selected conformance scope values supported",
            list(unsupported_scope),
            "UNSUPPORTED_CONFORMANCE_SCOPE",
        ),
    ]

    anti_collapse_checks = (
        ("conformance_is_not_authorization", "reception_authorized", "CONFORMANCE_AUTHORIZES_RECEPTION"),
        ("conformance_is_not_source_receipt", "source_receipt_recorded", "CONFORMANCE_RECORDS_SOURCE_RECEIPT"),
        ("conformance_does_not_receive_source", "source_received", "CONFORMANCE_RECEIVES_SOURCE"),
        ("conformance_does_not_create_source_receipt", "source_receipt_created", "CONFORMANCE_CREATES_SOURCE_RECEIPT"),
        ("conformance_does_not_create_adoption", "adoption_created", "CONFORMANCE_CREATES_ADOPTION"),
        ("conformance_does_not_create_authority", "authority_created", "CONFORMANCE_CREATES_AUTHORITY"),
        ("conformance_does_not_create_currentness", "currentness_created", "CONFORMANCE_CREATES_CURRENTNESS"),
        ("conformance_does_not_validate_source", "source_validated_by_receiving_context", "CONFORMANCE_VALIDATES_SOURCE"),
        ("conformance_does_not_invalidate_source", "source_invalidated_by_receiving_context", "CONFORMANCE_INVALIDATES_SOURCE"),
        ("conformance_does_not_replace_source", "source_replaced", "CONFORMANCE_REPLACES_SOURCE"),
        ("conformance_does_not_create_operation_permission", "operation_permission_created", "CONFORMANCE_CREATES_OPERATION_PERMISSION"),
        ("conformance_does_not_create_governance", "receiving_context_governance_created", "CONFORMANCE_CREATES_GOVERNANCE"),
        ("conformance_does_not_open_publication_flow", "publication_flow_opened", "CONFORMANCE_OPENS_PUBLICATION_FLOW"),
        ("conformance_does_not_create_public_readiness", "public_launch_readiness_created", "CONFORMANCE_CREATES_PUBLIC_READINESS"),
        ("conformance_does_not_claim_final_completion", "final_completion_claimed", "CONFORMANCE_CLAIMS_FINAL_COMPLETION"),
        ("conformance_does_not_authorize_continuation", "continuation_authorized", "CONFORMANCE_AUTHORIZES_CONTINUATION"),
        ("conformance_does_not_authorize_follow_on_work", "follow_on_work_authorized", "CONFORMANCE_AUTHORIZES_FOLLOW_ON_WORK"),
        ("conformance_does_not_claim_closure", "reception_closure_passed", "CONFORMANCE_CLAIMS_CLOSURE_PASSED"),
        ("closure_remains_future_work", "reception_closure_passed", "CONFORMANCE_CLAIMS_CLOSURE_PASSED"),
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
                "required conformance non-claims explicit and false",
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
    selected_receipt_exhaustion, selected_receipt_exhaustion_path, selected_load_code = (
        _load_selected_receipt_exhaustion_result(request)
    )
    selected_receipt_exhaustion_dict = selected_receipt_exhaustion or {}
    selected_receipt_exhaustion_outcome = _extract_receipt_exhaustion_outcome(
        request,
        selected_receipt_exhaustion,
    )
    selected_receipt_exhaustion_id = _extract_receipt_exhaustion_id(
        request,
        selected_receipt_exhaustion,
    )
    selected_receipt_exhaustion_failed_count = (
        _failed_check_count(selected_receipt_exhaustion_dict)
        if selected_receipt_exhaustion is not None
        else None
    )

    selected_recognition_result = _first_present(
        request.get("selected_recognition_result"),
        _nested_selected_recognition(selected_receipt_exhaustion_dict),
    )
    selected_non_capture_result = _first_present(
        request.get("selected_non_capture_result"),
        _nested_selected_non_capture(
            selected_receipt_exhaustion_dict,
            selected_recognition_result,
        ),
    )
    selected_eligibility_result = _first_present(
        request.get("selected_eligibility_result"),
        _nested_selected_eligibility(
            selected_receipt_exhaustion_dict,
            selected_recognition_result,
            selected_non_capture_result,
        ),
    )
    selected_receiving_context_role_result = _first_present(
        request.get("selected_receiving_context_role_result"),
        _nested_role_result(
            selected_receipt_exhaustion_dict,
            selected_recognition_result,
            selected_non_capture_result,
            selected_eligibility_result,
        ),
    )
    selected_identity_preservation_result = _first_present(
        request.get("selected_identity_preservation_result"),
        _nested_identity_result(
            selected_receipt_exhaustion_dict,
            selected_recognition_result,
            selected_non_capture_result,
            selected_eligibility_result,
            selected_receiving_context_role_result,
        ),
    )
    selected_request_declaration_result = _first_present(
        request.get("selected_reception_request_declaration_result"),
        _nested_request_declaration(
            selected_receipt_exhaustion_dict,
            selected_recognition_result,
            selected_non_capture_result,
            selected_eligibility_result,
            selected_receiving_context_role_result,
            selected_identity_preservation_result,
        ),
    )
    selected_source_body_surface = _nested_surface(
        request,
        selected_receipt_exhaustion_dict,
        selected_recognition_result,
        selected_non_capture_result,
        selected_eligibility_result,
        selected_receiving_context_role_result,
        selected_identity_preservation_result,
    )
    receiving_context = _nested_receiving_context(
        request,
        selected_receipt_exhaustion_dict,
        selected_recognition_result,
        selected_non_capture_result,
        selected_eligibility_result,
        selected_receiving_context_role_result,
    )
    receiving_context_type = _context_type(
        request,
        receiving_context,
        selected_receipt_exhaustion_dict,
    )

    reception_class = _first_present(
        request.get("reception_class"),
        _value_at(selected_receipt_exhaustion_dict, "receipt_exhaustion_basis", "reception_class"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "source_body_reception_receipt_exhaustion_summary",
            "reception_class",
        ),
    )
    reception_purpose = _first_present(
        request.get("reception_purpose"),
        _value_at(selected_receipt_exhaustion_dict, "receipt_exhaustion_basis", "reception_purpose"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "source_body_reception_receipt_exhaustion_summary",
            "reception_purpose",
        ),
    )
    reception_limits = _first_present(
        request.get("reception_limits"),
        _value_at(selected_receipt_exhaustion_dict, "receipt_exhaustion_basis", "reception_limits"),
    )
    selected_receiving_context_role = _first_present(
        request.get("selected_receiving_context_role"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
            "selected_receiving_context_role",
        ),
    )
    receiving_context_role_class = _first_present(
        request.get("receiving_context_role_class"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
            "receiving_context_role_class",
        ),
    )
    receiving_context_role_limits = _first_present(
        request.get("receiving_context_role_limits"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
            "receiving_context_role_limits",
        ),
    )
    recognition_basis = _first_present(
        request.get("recognition_basis"),
        _value_at(selected_receipt_exhaustion_dict, "receipt_exhaustion_basis", "recognition_basis"),
        _value_at(selected_recognition_result, "recognition_basis"),
    )
    recognition_limits = _first_present(
        request.get("recognition_limits"),
        _value_at(selected_receipt_exhaustion_dict, "receipt_exhaustion_basis", "recognition_limits"),
        _value_at(selected_recognition_result, "recognition_limits"),
    )
    receipt_exhaustion_basis = _first_present(
        request.get("receipt_exhaustion_basis"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
            "receipt_exhaustion_basis",
        ),
        selected_receipt_exhaustion_dict.get("receipt_exhaustion_basis"),
    )
    recognition_record_receipt_basis = _first_present(
        request.get("recognition_record_receipt_basis"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "recognition_record_receipt_basis",
            "recognition_record_receipt_basis",
        ),
        selected_receipt_exhaustion_dict.get("recognition_record_receipt_basis"),
    )
    recognition_record_exhaustion_basis = _first_present(
        request.get("recognition_record_exhaustion_basis"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "recognition_record_exhaustion_basis",
            "recognition_record_exhaustion_basis",
        ),
        selected_receipt_exhaustion_dict.get("recognition_record_exhaustion_basis"),
    )
    conformance_basis = request.get("conformance_basis")
    conformance_limits = request.get("conformance_limits")
    scope_values = _scope_values(request.get("conformance_scope"))
    unsupported_scope = [
        value for value in scope_values if value not in SUPPORTED_CONFORMANCE_SCOPE
    ]

    block_code = _determine_block_code(
        request,
        selected_receipt_exhaustion,
        selected_load_code,
        selected_receipt_exhaustion_outcome,
        selected_receipt_exhaustion_failed_count,
        selected_recognition_result,
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
        conformance_basis,
        conformance_limits,
        unsupported_scope,
    )

    requested_outcome = request.get("requested_conformance_outcome") or OUTCOME_PASSED
    if block_code:
        outcome = OUTCOME_BLOCKED
    elif request.get("conformance_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_PASSED
    elif requested_outcome == OUTCOME_NOT_PASSED:
        outcome = OUTCOME_NOT_PASSED
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
    elif requested_outcome == OUTCOME_PASSED:
        outcome = OUTCOME_PASSED
    else:
        outcome = OUTCOME_BLOCKED
        block_code = "DECLARED_CONFORMANCE_REQUEST_MALFORMED"

    passed = outcome == OUTCOME_PASSED
    checks = _build_checks(
        block_code,
        request,
        selected_receipt_exhaustion,
        selected_receipt_exhaustion_outcome,
        selected_receipt_exhaustion_failed_count,
        selected_recognition_result,
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
        conformance_basis,
        conformance_limits,
        unsupported_scope,
    )

    result_id_seed = _safe_component(
        request.get("conformance_request_id") or selected_receipt_exhaustion_id,
        "source_body_reception_conformance",
    )
    metadata = {
        "source_body_reception_conformance_result_id": (
            f"{result_id_seed}__source_body_reception_conformance_result"
        ),
        "source_body_reception_conformance_result_type": (
            "source_body_reception_conformance_boundary_result"
        ),
        "source_body_reception_conformance_result_version": RESULT_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "resolver_module": RESOLVER_MODULE,
    }

    source_body_identity_basis = _first_present(
        request.get("source_body_identity_basis"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
            "source_body_identity_basis",
        ),
        _value_at(selected_source_body_surface, "source_body_identity_basis"),
    )
    source_body_lineage_basis = _first_present(
        request.get("source_body_lineage_basis"),
        _value_at(
            selected_receipt_exhaustion_dict,
            "receipt_exhaustion_basis",
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

    receipt_exhaustion_recorded_by_selected_result = (
        selected_receipt_exhaustion_outcome == REQUIRED_RECEIPT_EXHAUSTION_OUTCOME
        and selected_receipt_exhaustion_failed_count == 0
    )

    selected_receipt_exhaustion_section = {
        "selected_receipt_exhaustion_result_id": selected_receipt_exhaustion_id,
        "selected_receipt_exhaustion_result_outcome": selected_receipt_exhaustion_outcome,
        "selected_receipt_exhaustion_result_path": selected_receipt_exhaustion_path,
        "selected_receipt_exhaustion_outcome_is_recorded": (
            selected_receipt_exhaustion_outcome == REQUIRED_RECEIPT_EXHAUSTION_OUTCOME
        ),
        "selected_receipt_exhaustion_result_failed_check_count_zero": (
            selected_receipt_exhaustion_failed_count == 0
        ),
        "selected_receipt_exhaustion_result_preserved": (
            selected_receipt_exhaustion is not None
        ),
        "selected_receipt_exhaustion_result_recorded": (
            receipt_exhaustion_recorded_by_selected_result
        ),
        "selected_recognition_result_preserved": _present(selected_recognition_result),
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
        "source_body_reception_recognition_recorded": True,
        "source_body_reception_receipt_exhaustion_recorded": (
            receipt_exhaustion_recorded_by_selected_result
        ),
        "receipt_exhaustion_recorded": receipt_exhaustion_recorded_by_selected_result,
        "receipt_exhaustion_remained_recognition_accounting_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "receipt_exhaustion_did_not_authorize_reception": True,
        "receipt_exhaustion_did_not_receive_source": True,
        "receipt_exhaustion_did_not_record_source_receipt": True,
        "receipt_exhaustion_did_not_create_source_receipt": True,
        "receipt_exhaustion_did_not_claim_conformance": True,
        "receipt_exhaustion_did_not_claim_closure": True,
        "raw_selected_receipt_exhaustion_result": copy.deepcopy(
            selected_receipt_exhaustion
        ),
    }

    declared_question = {
        "conformance_request_id": request.get("conformance_request_id"),
        "conformance_question": request.get("conformance_question"),
        "conformance_intent": request.get("conformance_intent"),
        "declared_conformance_request_path": request_path,
        "selected_receipt_exhaustion_result_id": selected_receipt_exhaustion_id,
        "selected_receipt_exhaustion_result_outcome": selected_receipt_exhaustion_outcome,
        "selected_source_body_surface_identifier": surface_identifier,
        "selected_source_body_surface_type": surface_type,
        "selected_source_body_surface_reference": surface_reference,
        "receiving_context_id": receiving_context_id,
        "receiving_context_type": receiving_context_type,
        "reception_class": reception_class,
        "reception_purpose": reception_purpose,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_does_not_decide_closure": True,
    }

    conformance_basis_section = {
        "selected_receipt_exhaustion_result": copy.deepcopy(selected_receipt_exhaustion),
        "selected_recognition_result": copy.deepcopy(selected_recognition_result),
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
        "receipt_exhaustion_basis": copy.deepcopy(receipt_exhaustion_basis),
        "recognition_record_receipt_basis": copy.deepcopy(
            recognition_record_receipt_basis
        ),
        "recognition_record_exhaustion_basis": copy.deepcopy(
            recognition_record_exhaustion_basis
        ),
        "conformance_basis": copy.deepcopy(conformance_basis),
        "reception_chain_conformance_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "source_remains_unreceived": True,
        "source_receipt_remains_unrecorded": True,
        "source_receipt_remains_uncreated": True,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_is_not_closure": True,
        "closure_requires_separate_boundary": True,
    }

    conformance_limits_section = {
        "conformance_limits": copy.deepcopy(conformance_limits),
        "reception_chain_conformance_only": True,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_does_not_receive_source": True,
        "conformance_does_not_create_source_receipt": True,
        "conformance_is_not_adoption": True,
        "conformance_is_not_authority": True,
        "conformance_is_not_currentness": True,
        "conformance_is_not_validation": True,
        "conformance_is_not_invalidation": True,
        "conformance_is_not_operation_permission": True,
        "conformance_is_not_publication_flow": True,
        "conformance_is_not_closure": True,
        "closure_requires_separate_boundary": True,
    }

    conformance_scope_section = {
        "selected_conformance_scope_values": scope_values,
        "all_selected_scope_values_supported": not unsupported_scope,
        "unsupported_conformance_scope_values": list(unsupported_scope),
        "reception_chain_conformance_only": (
            "RECEPTION_CHAIN_CONFORMANCE_ONLY" in scope_values
        ),
        "conformance_is_not_authorization": (
            "CONFORMANCE_IS_NOT_AUTHORIZATION" in scope_values
        ),
        "conformance_is_not_source_receipt": (
            "CONFORMANCE_IS_NOT_SOURCE_RECEIPT" in scope_values
        ),
        "conformance_does_not_receive_source": (
            "CONFORMANCE_DOES_NOT_RECEIVE_SOURCE" in scope_values
        ),
        "conformance_does_not_create_source_receipt": (
            "CONFORMANCE_DOES_NOT_CREATE_SOURCE_RECEIPT" in scope_values
        ),
        "conformance_is_not_adoption": "CONFORMANCE_IS_NOT_ADOPTION" in scope_values,
        "conformance_is_not_authority": "CONFORMANCE_IS_NOT_AUTHORITY" in scope_values,
        "conformance_is_not_currentness": (
            "CONFORMANCE_IS_NOT_CURRENTNESS" in scope_values
        ),
        "conformance_is_not_validation": (
            "CONFORMANCE_IS_NOT_VALIDATION" in scope_values
        ),
        "conformance_is_not_invalidation": (
            "CONFORMANCE_IS_NOT_INVALIDATION" in scope_values
        ),
        "conformance_is_not_operation_permission": (
            "CONFORMANCE_IS_NOT_OPERATION_PERMISSION" in scope_values
        ),
        "conformance_is_not_publication_flow": (
            "CONFORMANCE_IS_NOT_PUBLICATION_FLOW" in scope_values
        ),
        "conformance_is_not_closure": "CONFORMANCE_IS_NOT_CLOSURE" in scope_values,
        "closure_requires_separate_boundary": (
            "CLOSURE_REQUIRES_SEPARATE_BOUNDARY" in scope_values
        ),
    }

    non_claims = _build_non_claims(passed)
    conformance_statement = {
        "source_body_reception_conformance_recorded": passed,
        "source_body_reception_conformance_passed": passed,
        "reception_boundary_chain_conformance_passed": passed,
        "reception_family_conformance_passed": passed,
        "selected_receipt_exhaustion_result_preserved": (
            selected_receipt_exhaustion is not None
        ),
        "selected_receipt_exhaustion_result_recorded": (
            receipt_exhaustion_recorded_by_selected_result
        ),
        "selected_receipt_exhaustion_result_failed_check_count_zero": (
            selected_receipt_exhaustion_failed_count == 0
        ),
        "selected_recognition_result_preserved": _present(selected_recognition_result),
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
            selected_source_body_surface,
            Mapping,
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_surface_is_not_whole_body_by_default": True,
        "receiving_context_preserved": isinstance(receiving_context, Mapping),
        "receiving_context_remains_context_only": True,
        "receiving_context_is_not_source": True,
        "receiving_context_is_not_authority": True,
        "receiving_context_is_not_current": True,
        "reception_chain_conformance_only": True,
        "request_declaration_remained_declaration_only": True,
        "identity_preservation_preserved_source_identity_only": True,
        "receiving_context_role_remained_context_role_only": True,
        "eligibility_admissibility_remained_review_readiness_only": True,
        "non_capture_remained_refusal_check_outcome_only": True,
        "recognition_remained_bounded_accounting_recognition_only": True,
        "receipt_exhaustion_remained_recognition_record_accounting_only": True,
        "receipt_exhaustion_remained_recognition_accounting_only": True,
        "conformance_is_not_authorization": True,
        "conformance_is_not_source_receipt": True,
        "conformance_does_not_receive_source": True,
        "conformance_does_not_create_source_receipt": True,
        "conformance_is_not_closure": True,
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
    not_passed_basis = {
        "not_passed": outcome == OUTCOME_NOT_PASSED,
        "not_passed_basis": copy.deepcopy(request.get("not_passed_basis")),
        "not_passed_does_not_mutate": True,
        "not_passed_does_not_repair": True,
        "not_passed_does_not_authorize": True,
        "not_passed_does_not_receive": True,
        "not_passed_does_not_record_source_receipt": True,
        "not_passed_does_not_create_source_receipt": True,
        "not_passed_does_not_replace": True,
        "not_passed_does_not_validate": True,
        "not_passed_does_not_invalidate": True,
        "not_passed_does_not_create_currentness": True,
        "not_passed_does_not_claim_closure": True,
    }

    result: dict[str, Any] = {
        "source_body_reception_conformance_metadata": metadata,
        "declared_conformance_question": declared_question,
        "selected_receipt_exhaustion_result": selected_receipt_exhaustion_section,
        "selected_source_body_surface": selected_surface_section,
        "receiving_context": receiving_context_section,
        "conformance_basis": conformance_basis_section,
        "conformance_limits": conformance_limits_section,
        "conformance_scope": conformance_scope_section,
        "conformance_checks": checks,
        "conformance_statement": conformance_statement,
        "conformance_non_meaning": _build_conformance_non_meaning(),
        "additional_basis_required": additional_basis_required,
        "not_passed_basis": not_passed_basis,
        "what_remains_open": _build_what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": _block(block_code, request.get("block_reason") or block_code),
    }
    result["source_body_reception_conformance_summary"] = (
        build_source_body_reception_conformance_summary(result)
    )
    return result


def resolve_source_body_reception_conformance_boundary(
    declared_conformance_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared source-body reception conformance request."""
    if declared_conformance_request is None:
        return _build_result({})
    if not isinstance(declared_conformance_request, Mapping):
        return _blocked_malformed_request("DECLARED_CONFORMANCE_REQUEST_MALFORMED")
    return _build_result(copy.deepcopy(dict(declared_conformance_request)))


def resolve_source_body_reception_conformance_boundary_from_path(
    declared_conformance_request_path: Path | str,
) -> dict:
    """Load and resolve one declared source-body reception conformance request."""
    request, error = _read_json_object(declared_conformance_request_path)
    if error == "unreadable":
        return _blocked_malformed_request(
            "DECLARED_CONFORMANCE_REQUEST_UNREADABLE",
            str(declared_conformance_request_path),
        )
    if error == "malformed":
        return _blocked_malformed_request(
            "DECLARED_CONFORMANCE_REQUEST_MALFORMED",
            str(declared_conformance_request_path),
        )
    return _build_result(
        request or {},
        request_path=str(declared_conformance_request_path),
    )


def _blocked_malformed_request(code: str, request_path: str | None = None) -> dict:
    request = {
        "conformance_request_id": None,
        "conformance_question": None,
        "conformance_intent": None,
        "selected_receipt_exhaustion_result": None,
        "conformance_basis": None,
        "conformance_limits": None,
        "conformance_scope": [],
        "declared_non_claims": {},
        "block_reason": code,
    }
    result = _build_result(request, request_path=request_path)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = _block(code, request_path or code)
    result["source_body_reception_conformance_summary"] = (
        build_source_body_reception_conformance_summary(result)
    )
    return result


def build_source_body_reception_conformance_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the bounded summary for a conformance boundary result."""
    checks = result.get("conformance_checks") or []
    passed_check_count = sum(
        1 for check in checks if isinstance(check, Mapping) and _truthy(check.get("passed"))
    )
    failed_check_count = sum(
        1
        for check in checks
        if isinstance(check, Mapping) and not _truthy(check.get("passed"))
    )
    question = result.get("declared_conformance_question") or {}
    selected = result.get("selected_receipt_exhaustion_result") or {}
    surface = result.get("selected_source_body_surface") or {}
    context = result.get("receiving_context") or {}
    statement = result.get("conformance_statement") or {}
    block = result.get("block") or {}
    non_claims = result.get("non_claims") or {}
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "conformance_request_id": question.get("conformance_request_id"),
        "conformance_question": question.get("conformance_question"),
        "conformance_intent": question.get("conformance_intent"),
        "selected_receipt_exhaustion_result_id": selected.get(
            "selected_receipt_exhaustion_result_id"
        ),
        "selected_receipt_exhaustion_result_outcome": selected.get(
            "selected_receipt_exhaustion_result_outcome"
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
        "conformance_recorded": _truthy(
            statement.get("source_body_reception_conformance_recorded")
        ),
        "conformance_passed": _truthy(
            statement.get("source_body_reception_conformance_passed")
        ),
        "reception_boundary_chain_conformance_passed": _truthy(
            statement.get("reception_boundary_chain_conformance_passed")
        ),
        "reception_family_conformance_passed": _truthy(
            statement.get("reception_family_conformance_passed")
        ),
        "not_passed": outcome == OUTCOME_NOT_PASSED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_receipt_exhaustion_result_preserved": statement.get(
            "selected_receipt_exhaustion_result_preserved"
        ),
        "selected_receipt_exhaustion_result_recorded": statement.get(
            "selected_receipt_exhaustion_result_recorded"
        ),
        "selected_receipt_exhaustion_result_failed_check_count_zero": statement.get(
            "selected_receipt_exhaustion_result_failed_check_count_zero"
        ),
        "selected_recognition_result_preserved": statement.get(
            "selected_recognition_result_preserved"
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
        "reception_chain_conformance_only": statement.get(
            "reception_chain_conformance_only"
        ),
        "request_declaration_remained_declaration_only": statement.get(
            "request_declaration_remained_declaration_only"
        ),
        "identity_preservation_preserved_source_identity_only": statement.get(
            "identity_preservation_preserved_source_identity_only"
        ),
        "receiving_context_role_remained_context_role_only": statement.get(
            "receiving_context_role_remained_context_role_only"
        ),
        "eligibility_admissibility_review_readiness_only": statement.get(
            "eligibility_admissibility_remained_review_readiness_only"
        ),
        "non_capture_refusal_check_only": statement.get(
            "non_capture_remained_refusal_check_outcome_only"
        ),
        "recognition_bounded_accounting_only": statement.get(
            "recognition_remained_bounded_accounting_recognition_only"
        ),
        "receipt_exhaustion_recognition_record_accounting_only": statement.get(
            "receipt_exhaustion_remained_recognition_record_accounting_only"
        ),
        "conformance_not_authorization": statement.get(
            "conformance_is_not_authorization"
        ),
        "conformance_not_source_receipt": statement.get(
            "conformance_is_not_source_receipt"
        ),
        "conformance_not_closure": statement.get("conformance_is_not_closure"),
        "no_source_received": non_claims.get("source_received") is False,
        "no_source_receipt_recorded": non_claims.get("source_receipt_recorded") is False,
        "no_source_receipt_created": non_claims.get("source_receipt_created") is False,
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


def write_source_body_reception_conformance_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one additive source-body reception conformance result artifact."""
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionConformanceBoundaryError(
            "Conformance result must be a mapping."
        )
    if output_path is None:
        summary = result.get("source_body_reception_conformance_summary") or {}
        stem = _safe_component(
            summary.get("conformance_request_id")
            or summary.get("selected_receipt_exhaustion_result_id"),
            "source_body_reception_conformance",
        )
        output_path = (
            SOURCE_BODY_RECEPTION_CONFORMANCE_BOUNDARY_ROOT
            / f"{stem}__source_body_reception_conformance_result.json"
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


def build_declared_source_body_reception_conformance_request(
    conformance_request_id: str,
    conformance_question: str,
    selected_receipt_exhaustion_result: Mapping[str, Any] | str,
    conformance_basis: Mapping[str, Any] | str,
    conformance_limits: Mapping[str, Any] | str,
    conformance_scope: Sequence[str] | Mapping[str, Any],
    conformance_intent: str = INTENT_RECORD,
    *,
    selected_receipt_exhaustion_result_path: str | None = None,
    selected_receipt_exhaustion_result_id: str | None = None,
    selected_receipt_exhaustion_result_outcome: str | None = None,
    requested_conformance_outcome: str = OUTCOME_PASSED,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_passed_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared conformance request with required non-claims false."""
    request: dict[str, Any] = {
        "conformance_request_id": conformance_request_id,
        "conformance_question": conformance_question,
        "conformance_intent": conformance_intent,
        "conformance_basis": copy.deepcopy(conformance_basis),
        "conformance_limits": copy.deepcopy(conformance_limits),
        "conformance_scope": copy.deepcopy(conformance_scope),
        "declared_non_claims": {key: False for key in REQUIRED_FALSE_NON_CLAIMS},
        "requested_conformance_outcome": requested_conformance_outcome,
    }
    if selected_receipt_exhaustion_result_path is not None:
        request["selected_receipt_exhaustion_result_path"] = (
            selected_receipt_exhaustion_result_path
        )
    elif isinstance(selected_receipt_exhaustion_result, Mapping):
        request["selected_receipt_exhaustion_result"] = copy.deepcopy(
            dict(selected_receipt_exhaustion_result)
        )
    else:
        request["selected_receipt_exhaustion_result"] = selected_receipt_exhaustion_result
    if selected_receipt_exhaustion_result_id is not None:
        request["selected_receipt_exhaustion_result_id"] = (
            selected_receipt_exhaustion_result_id
        )
    if selected_receipt_exhaustion_result_outcome is not None:
        request["selected_receipt_exhaustion_result_outcome"] = (
            selected_receipt_exhaustion_result_outcome
        )
    if additional_basis_context is not None:
        request["additional_basis_context"] = copy.deepcopy(additional_basis_context)
    if not_passed_basis is not None:
        request["not_passed_basis"] = copy.deepcopy(not_passed_basis)
    return request
