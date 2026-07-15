"""Resolve source-body reception non-capture / non-adoption / non-currentness.

This resolver answers one bounded question:

Did this eligible/admissible source-body reception request pass non-capture,
non-adoption, and non-currentness review?

The resolver records refusal/check outcomes only. Non-capture passed is not
reception recognition, not reception authorization, and not source receipt.
Reception recognition remains a separate future boundary.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Sequence


class SourceBodyReceptionNonCaptureBoundaryError(Exception):
    """Raised for impossible non-capture boundary resolver failures."""


RESOLVER_MODULE = "resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary"
RESULT_VERSION = "0.1.0"

SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_"
    "non_capture_non_adoption_non_currentness_boundary"
)

OUTCOME_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_PASSED"
OUTCOME_NOT_PASSED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_NOT_PASSED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_NON_CAPTURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_NON_CAPTURE_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_PASSED,
    OUTCOME_NOT_PASSED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

ELIGIBILITY_OUTCOME_RECORDED = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_NON_CAPTURE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_NON_CAPTURE"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_NON_CAPTURE_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_NON_CAPTURE_SCOPE_VALUES = {
    "NON_CAPTURE_REVIEW_ONLY",
    "NON_ADOPTION_REVIEW_ONLY",
    "NON_CURRENTNESS_REVIEW_ONLY",
    "NON_CAPTURE_IS_NOT_RECEPTION",
    "NON_CAPTURE_IS_NOT_AUTHORIZATION",
    "NON_CAPTURE_IS_NOT_SOURCE_RECEIPT",
    "NON_CAPTURE_IS_NOT_RECOGNITION",
    "NON_CAPTURE_DOES_NOT_VALIDATE_SOURCE",
    "NON_CAPTURE_DOES_NOT_INVALIDATE_SOURCE",
    "NO_SOURCE_REPLACEMENT",
    "NO_RECEIVING_CONTEXT_AUTHORITY",
    "NO_RECEIVING_CONTEXT_CURRENTNESS",
    "NO_RECEIVING_CONTEXT_GOVERNANCE",
    "RECOGNITION_REQUIRES_SEPARATE_BOUNDARY",
}

REQUIRED_NON_CLAIMS = (
    "reception_recognized",
    "reception_authorized",
    "source_received",
    "reception_recognition_passed",
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
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

ALLOWED_PASSED_TRUE_FIELDS = (
    "source_body_reception_non_capture_passed",
    "non_capture_boundary_recorded",
    "non_capture_passed",
    "non_adoption_passed",
    "non_currentness_passed",
)

COLLAPSE_FIELD_BLOCK_CODES = (
    ("reception_recognized", "NON_CAPTURE_RECOGNIZES_RECEPTION"),
    ("recognizes_reception", "NON_CAPTURE_RECOGNIZES_RECEPTION"),
    ("non_capture_recognizes_reception", "NON_CAPTURE_RECOGNIZES_RECEPTION"),
    ("reception_authorized", "NON_CAPTURE_AUTHORIZES_RECEPTION"),
    ("authorizes_reception", "NON_CAPTURE_AUTHORIZES_RECEPTION"),
    ("non_capture_authorizes_reception", "NON_CAPTURE_AUTHORIZES_RECEPTION"),
    ("source_received", "NON_CAPTURE_RECEIVES_SOURCE"),
    ("receives_source", "NON_CAPTURE_RECEIVES_SOURCE"),
    ("non_capture_receives_source", "NON_CAPTURE_RECEIVES_SOURCE"),
    ("reception_recognition_passed", "NON_CAPTURE_CLAIMS_RECOGNITION_PASSED"),
    ("claims_recognition_passed", "NON_CAPTURE_CLAIMS_RECOGNITION_PASSED"),
    ("receiving_context_governance_created", "NON_CAPTURE_CREATES_GOVERNANCE"),
    ("creates_governance", "NON_CAPTURE_CREATES_GOVERNANCE"),
    ("receiving_context_became_source", "NON_CAPTURE_TREATS_CONTEXT_AS_SOURCE"),
    ("treats_context_as_source", "NON_CAPTURE_TREATS_CONTEXT_AS_SOURCE"),
    ("receiving_context_became_authority", "NON_CAPTURE_TREATS_CONTEXT_AS_AUTHORITY"),
    ("treats_context_as_authority", "NON_CAPTURE_TREATS_CONTEXT_AS_AUTHORITY"),
    ("receiving_context_became_current", "NON_CAPTURE_TREATS_CONTEXT_AS_CURRENT"),
    ("treats_context_as_current", "NON_CAPTURE_TREATS_CONTEXT_AS_CURRENT"),
    ("receiving_context_became_receiver", "NON_CAPTURE_TREATS_CONTEXT_AS_RECEIVER"),
    ("treats_context_as_receiver", "NON_CAPTURE_TREATS_CONTEXT_AS_RECEIVER"),
    ("receiving_context_became_adopter", "NON_CAPTURE_TREATS_CONTEXT_AS_ADOPTER"),
    ("treats_context_as_adopter", "NON_CAPTURE_TREATS_CONTEXT_AS_ADOPTER"),
    ("receiving_context_became_validator", "NON_CAPTURE_TREATS_CONTEXT_AS_VALIDATOR"),
    ("treats_context_as_validator", "NON_CAPTURE_TREATS_CONTEXT_AS_VALIDATOR"),
    ("receiving_context_became_invalidator", "NON_CAPTURE_TREATS_CONTEXT_AS_INVALIDATOR"),
    ("treats_context_as_invalidator", "NON_CAPTURE_TREATS_CONTEXT_AS_INVALIDATOR"),
    ("receiving_context_became_operator", "NON_CAPTURE_TREATS_CONTEXT_AS_OPERATOR"),
    ("treats_context_as_operator", "NON_CAPTURE_TREATS_CONTEXT_AS_OPERATOR"),
    ("source_validated_by_receiving_context", "NON_CAPTURE_VALIDATES_SOURCE"),
    ("validates_source", "NON_CAPTURE_VALIDATES_SOURCE"),
    ("source_invalidated_by_receiving_context", "NON_CAPTURE_INVALIDATES_SOURCE"),
    ("invalidates_source", "NON_CAPTURE_INVALIDATES_SOURCE"),
    ("source_replaced", "NON_CAPTURE_REPLACES_SOURCE"),
    ("replaces_source", "NON_CAPTURE_REPLACES_SOURCE"),
    ("adoption_created", "NON_CAPTURE_CREATES_ADOPTION"),
    ("creates_adoption", "NON_CAPTURE_CREATES_ADOPTION"),
    ("authority_created", "NON_CAPTURE_CREATES_AUTHORITY"),
    ("creates_authority", "NON_CAPTURE_CREATES_AUTHORITY"),
    ("currentness_created", "NON_CAPTURE_CREATES_CURRENTNESS"),
    ("creates_currentness", "NON_CAPTURE_CREATES_CURRENTNESS"),
    ("standing_created", "NON_CAPTURE_CREATES_STANDING"),
    ("creates_standing", "NON_CAPTURE_CREATES_STANDING"),
    ("standing_propagated", "NON_CAPTURE_CREATES_STANDING_PROPAGATION"),
    ("creates_standing_propagation", "NON_CAPTURE_CREATES_STANDING_PROPAGATION"),
    ("vessel_relation_created", "NON_CAPTURE_CREATES_VESSEL_RELATION"),
    ("creates_vessel_relation", "NON_CAPTURE_CREATES_VESSEL_RELATION"),
    ("derivative_relation_created", "NON_CAPTURE_CREATES_DERIVATIVE_RELATION"),
    ("creates_derivative_relation", "NON_CAPTURE_CREATES_DERIVATIVE_RELATION"),
    ("operation_permission_created", "NON_CAPTURE_CREATES_OPERATION_PERMISSION"),
    ("creates_operation_permission", "NON_CAPTURE_CREATES_OPERATION_PERMISSION"),
    ("public_launch_readiness_created", "NON_CAPTURE_CREATES_PUBLIC_READINESS"),
    ("creates_public_readiness", "NON_CAPTURE_CREATES_PUBLIC_READINESS"),
    ("final_completion_claimed", "NON_CAPTURE_CLAIMS_FINAL_COMPLETION"),
    ("claims_final_completion", "NON_CAPTURE_CLAIMS_FINAL_COMPLETION"),
    ("follow_on_work_authorized", "NON_CAPTURE_AUTHORIZES_FOLLOW_ON_WORK"),
    ("authorizes_follow_on_work", "NON_CAPTURE_AUTHORIZES_FOLLOW_ON_WORK"),
    ("continuation_authorized", "NON_CAPTURE_AUTHORIZES_CONTINUATION"),
    ("authorizes_continuation", "NON_CAPTURE_AUTHORIZES_CONTINUATION"),
    ("publication_flow_opened", "NON_CAPTURE_OPENS_PUBLICATION_FLOW"),
    ("opens_publication_flow", "NON_CAPTURE_OPENS_PUBLICATION_FLOW"),
)

MUTATION_FIELDS = ("mutation_performed", "replay_performed", "merge_performed")


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def _deepcopy(value: Any) -> Any:
    return copy.deepcopy(value)


def _is_mapping(value: Any) -> bool:
    return isinstance(value, Mapping)


def _present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (Mapping, Sequence)) and not isinstance(value, (str, bytes, bytearray)):
        return bool(value)
    return True


def _truthy(value: Any) -> bool:
    if value is True:
        return True
    if isinstance(value, str):
        return value.strip().lower() in {"true", "yes", "1", "y"}
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value != 0
    return False


def _value_at(mapping: Mapping[str, Any] | None, key: str, default: Any = None) -> Any:
    if not _is_mapping(mapping):
        return default
    return mapping.get(key, default)


def _first_present(*values: Any) -> Any:
    for value in values:
        if _present(value):
            return value
    return None


def _nested(mapping: Mapping[str, Any] | None, *keys: str) -> Any:
    current: Any = mapping
    for key in keys:
        if not _is_mapping(current):
            return None
        current = current.get(key)
    return current


def _read_json_object(path: Path | str) -> tuple[dict[str, Any] | None, str | None]:
    candidate = Path(path)
    try:
        with candidate.open("r", encoding="utf-8") as handle:
            parsed = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None, "unreadable"
    if not isinstance(parsed, dict):
        return None, "malformed"
    return parsed, None


def _safe_component(value: Any) -> str:
    text = str(value or "source_body_reception_non_capture").strip()
    cleaned = "".join(character if character.isalnum() or character in "-_." else "_" for character in text)
    return cleaned.strip("._") or "source_body_reception_non_capture"


def _failed_check_count(result: Mapping[str, Any] | None, check_key: str) -> int | None:
    if not _is_mapping(result):
        return None
    summary = _first_present(
        _value_at(result, "source_body_reception_non_capture_summary"),
        _value_at(result, "source_body_reception_eligibility_summary"),
        _value_at(result, "source_body_reception_receiving_context_role_summary"),
        _value_at(result, "source_body_reception_identity_preservation_summary"),
        _value_at(result, "summary"),
    )
    if _is_mapping(summary):
        for key in (
            "failed_check_count",
            "selected_eligibility_result_failed_check_count",
            "selected_receiving_context_role_result_failed_check_count",
        ):
            value = summary.get(key)
            if isinstance(value, int):
                return value
    checks = _value_at(result, check_key)
    if isinstance(checks, Sequence) and not isinstance(checks, (str, bytes, bytearray)):
        return sum(1 for check in checks if _is_mapping(check) and not check.get("passed"))
    for key in ("failed_check_count", "failed_checks"):
        value = result.get(key)
        if isinstance(value, int):
            return value
    return None


def _scope_values(scope: Any) -> list[str]:
    if isinstance(scope, str):
        return [scope]
    if isinstance(scope, Mapping):
        values = scope.get("scope_values")
        if values is None:
            values = scope.get("selected_non_capture_scope_values")
        if values is None:
            values = scope.get("values")
        if values is None:
            values = [key for key, value in scope.items() if _truthy(value)]
        return [str(value) for value in values] if isinstance(values, Sequence) and not isinstance(values, (str, bytes, bytearray)) else [str(values)]
    if isinstance(scope, Sequence) and not isinstance(scope, (str, bytes, bytearray)):
        return [str(value) for value in scope]
    return []


def _contains_truthy_key(value: Any, field_name: str) -> bool:
    if isinstance(value, Mapping):
        for key, item in value.items():
            if str(key) == field_name and _truthy(item):
                return True
            if _contains_truthy_key(item, field_name):
                return True
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        return any(_contains_truthy_key(item, field_name) for item in value)
    return False


def _non_claims_from_request(request: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not _is_mapping(request):
        return {}
    non_claims = request.get("declared_non_claims")
    return non_claims if _is_mapping(non_claims) else {}


def _base_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_NON_CLAIMS}


def _result_non_claims(outcome: str) -> dict[str, Any]:
    non_claims: dict[str, Any] = _base_false_non_claims()
    for key in ALLOWED_PASSED_TRUE_FIELDS:
        non_claims[key] = outcome == OUTCOME_PASSED
    non_claims.update(
        {
            "allowed_true_fields_are_refusal_check_outcomes_only": True,
            "reception_remains_unrecognized": True,
            "reception_remains_unauthorized": True,
            "source_remains_unreceived": True,
            "recognition_remains_future_work": True,
        }
    )
    return non_claims


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
    *,
    code_key: str = "block_code",
) -> dict[str, Any]:
    record = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": expected_posture,
        "actual_posture": actual_posture,
        "block_code": None,
        "failure_code": None,
    }
    if not passed and code:
        record[code_key] = code
    return record


def _block(code: str | None, reason: str | None = None) -> dict[str, Any]:
    return {"blocked": code is not None, "code": code, "reason": reason}


def _load_selected_eligibility_result(
    request: Mapping[str, Any],
) -> tuple[dict[str, Any] | None, str | None, str | None]:
    path = request.get("selected_eligibility_result_path")
    if _present(path):
        parsed, error = _read_json_object(path)
        if error == "unreadable":
            return None, "ELIGIBILITY_RESULT_UNREADABLE", str(path)
        if error == "malformed":
            return None, "ELIGIBILITY_RESULT_MALFORMED", str(path)
        return _deepcopy(parsed), None, str(path)
    selected = request.get("selected_eligibility_result")
    if selected is None:
        return None, None, None
    if not _is_mapping(selected):
        return None, "ELIGIBILITY_RESULT_MALFORMED", None
    return _deepcopy(dict(selected)), None, None


def _eligibility_outcome(selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        _value_at(selected, "outcome"),
        _nested(selected, "source_body_reception_eligibility_summary", "outcome"),
        _nested(selected, "eligibility_statement", "outcome"),
    )


def _declared_or_selected_eligibility_outcome(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
) -> Any:
    return _first_present(
        request.get("selected_eligibility_result_outcome"),
        request.get("expected_selected_eligibility_outcome"),
        _eligibility_outcome(selected),
    )


def _eligibility_id(selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        _nested(selected, "source_body_reception_eligibility_metadata", "source_body_reception_eligibility_result_id"),
        _nested(selected, "source_body_reception_eligibility_summary", "source_body_reception_eligibility_result_id"),
        _value_at(selected, "source_body_reception_eligibility_result_id"),
        _value_at(selected, "eligibility_request_id"),
    )


def _selected_role_result(request: Mapping[str, Any], selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_receiving_context_role_result"),
        _value_at(selected, "selected_receiving_context_role_result"),
        _nested(selected, "eligibility_basis", "selected_receiving_context_role_result"),
        _nested(selected, "selected_eligibility_result", "selected_receiving_context_role_result"),
    )


def _identity_result(request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any) -> Any:
    return _first_present(
        request.get("selected_identity_preservation_result"),
        _nested(selected, "eligibility_basis", "selected_identity_preservation_result"),
        _nested(selected, "selected_receiving_context_role_result", "selected_identity_preservation_result"),
        _nested(role_result, "selected_identity_preservation_result"),
        _nested(role_result, "receiving_context_role_basis", "selected_identity_preservation_result"),
    )


def _request_declaration_result(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any, identity_result: Any
) -> Any:
    return _first_present(
        request.get("selected_reception_request_declaration_result"),
        _nested(selected, "eligibility_basis", "selected_reception_request_declaration_result"),
        _nested(role_result, "receiving_context_role_basis", "selected_reception_request_declaration_result"),
        _nested(identity_result, "identity_preservation_basis", "selected_reception_request_declaration_result"),
        _nested(identity_result, "selected_reception_request_declaration_result"),
    )


def _selected_source_surface(
    request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any, identity_result: Any
) -> Any:
    return _first_present(
        request.get("selected_source_body_surface"),
        _value_at(selected, "selected_source_body_surface"),
        _nested(selected, "eligibility_basis", "selected_source_body_surface"),
        _nested(role_result, "selected_source_body_surface"),
        _nested(role_result, "receiving_context_role_basis", "selected_source_body_surface"),
        _nested(identity_result, "selected_source_body_surface"),
    )


def _receiving_context(request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any) -> Any:
    return _first_present(
        request.get("receiving_context"),
        _value_at(selected, "receiving_context"),
        _nested(selected, "eligibility_basis", "receiving_context"),
        _nested(role_result, "receiving_context"),
        _nested(role_result, "receiving_context_role_basis", "receiving_context"),
    )


def _surface_identifier(request: Mapping[str, Any], surface: Any, selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_identifier"),
        _value_at(surface, "selected_source_body_surface_identifier"),
        _value_at(surface, "source_body_surface_identifier"),
        _value_at(surface, "identifier"),
        _nested(selected, "source_body_reception_eligibility_summary", "selected_source_body_surface_identifier"),
    )


def _surface_type(request: Mapping[str, Any], surface: Any, selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_type"),
        _value_at(surface, "selected_source_body_surface_type"),
        _value_at(surface, "source_body_surface_type"),
        _value_at(surface, "type"),
        _nested(selected, "source_body_reception_eligibility_summary", "selected_source_body_surface_type"),
    )


def _surface_reference(request: Mapping[str, Any], surface: Any, selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("selected_source_body_surface_reference"),
        request.get("selected_source_body_surface_path"),
        _value_at(surface, "selected_source_body_surface_reference"),
        _value_at(surface, "selected_source_body_surface_path"),
        _value_at(surface, "reference"),
        _value_at(surface, "path"),
        _nested(selected, "source_body_reception_eligibility_summary", "selected_source_body_surface_reference"),
    )


def _receiving_context_id(request: Mapping[str, Any], context: Any, selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("receiving_context_id"),
        _value_at(context, "receiving_context_id"),
        _value_at(context, "id"),
        _value_at(context, "name"),
        _nested(selected, "source_body_reception_eligibility_summary", "receiving_context_id"),
    )


def _receiving_context_type(request: Mapping[str, Any], context: Any, selected: Mapping[str, Any] | None) -> Any:
    return _first_present(
        request.get("receiving_context_type"),
        _value_at(context, "receiving_context_type"),
        _value_at(context, "type"),
        _nested(selected, "source_body_reception_eligibility_summary", "receiving_context_type"),
    )


def _role_class(request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any) -> Any:
    return _first_present(
        request.get("receiving_context_role_class"),
        _nested(selected, "eligibility_basis", "receiving_context_role_class"),
        _nested(selected, "source_body_reception_eligibility_summary", "receiving_context_role_class"),
        _nested(role_result, "receiving_context_role", "receiving_context_role_class"),
        _nested(role_result, "receiving_context_role_basis", "receiving_context_role_class"),
    )


def _role_limits(request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any) -> Any:
    return _first_present(
        request.get("receiving_context_role_limits"),
        _nested(selected, "eligibility_basis", "receiving_context_role_limits"),
        _nested(role_result, "receiving_context_role", "receiving_context_role_limits"),
        _nested(role_result, "receiving_context_role_basis", "receiving_context_role_limits"),
    )


def _selected_role(request: Mapping[str, Any], selected: Mapping[str, Any] | None, role_result: Any) -> Any:
    return _first_present(
        request.get("selected_receiving_context_role"),
        _nested(selected, "eligibility_basis", "selected_receiving_context_role"),
        _nested(role_result, "receiving_context_role"),
        _nested(role_result, "selected_receiving_context_role"),
    )


def _reception_value(request: Mapping[str, Any], selected: Mapping[str, Any] | None, key: str) -> Any:
    return _first_present(
        request.get(key),
        _nested(selected, "eligibility_basis", key),
        _nested(selected, "source_body_reception_eligibility_summary", key),
    )


def _selected_eligibility_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    selected_path: str | None,
) -> dict[str, Any]:
    statement = _value_at(selected, "eligibility_statement", {}) if _is_mapping(selected) else {}
    summary = _value_at(selected, "source_body_reception_eligibility_summary", {}) if _is_mapping(selected) else {}
    failed_count = _failed_check_count(selected, "eligibility_checks")
    outcome = _declared_or_selected_eligibility_outcome(request, selected)
    section = {
        "selected_eligibility_result_id": _first_present(
            request.get("selected_eligibility_result_id"),
            _eligibility_id(selected),
        ),
        "selected_eligibility_result_outcome": _first_present(
            request.get("selected_eligibility_result_outcome"),
            _eligibility_outcome(selected),
        ),
        "selected_eligibility_result_path": selected_path,
        "selected_eligibility_outcome_is_eligible_admissible": outcome == ELIGIBILITY_OUTCOME_RECORDED,
        "selected_eligibility_result_failed_check_count_zero": failed_count == 0,
        "selected_eligibility_result_preserved": bool(selected),
        "selected_eligibility_result_recorded": outcome == ELIGIBILITY_OUTCOME_RECORDED,
        "selected_receiving_context_role_result_preserved": bool(
            _first_present(
                _value_at(statement, "selected_receiving_context_role_result_preserved"),
                _value_at(summary, "selected_receiving_context_role_result_preserved"),
            )
        ),
        "selected_identity_preservation_result_preserved": bool(
            _first_present(
                _value_at(statement, "selected_identity_preservation_result_preserved"),
                _value_at(summary, "selected_identity_preservation_result_preserved"),
            )
        ),
        "selected_reception_request_declaration_result_preserved": bool(
            _first_present(
                _value_at(statement, "selected_reception_request_declaration_result_preserved"),
                _value_at(summary, "selected_request_declaration_result_preserved"),
                _value_at(summary, "selected_reception_request_declaration_result_preserved"),
            )
        ),
        "selected_source_body_surface_preserved": bool(
            _first_present(
                _value_at(statement, "selected_source_body_surface_preserved"),
                _value_at(summary, "selected_source_body_surface_preserved"),
            )
        ),
        "selected_source_body_surface_remains_source": bool(
            _first_present(
                _value_at(statement, "selected_source_body_surface_remains_source"),
                _value_at(summary, "selected_source_body_surface_remains_source"),
            )
        ),
        "selected_surface_is_not_whole_body_by_default": bool(
            _first_present(
                _value_at(statement, "selected_surface_is_not_whole_body_by_default"),
                _value_at(summary, "selected_surface_is_not_whole_body_by_default"),
            )
        ),
        "receiving_context_preserved": bool(
            _first_present(_value_at(statement, "receiving_context_preserved"), _value_at(summary, "receiving_context_preserved"))
        ),
        "receiving_context_remains_context_only": bool(
            _first_present(
                _value_at(statement, "receiving_context_remains_context_only"),
                _value_at(summary, "receiving_context_remains_context_only"),
            )
        ),
        "receiving_context_is_not_source": bool(
            _first_present(_value_at(statement, "receiving_context_is_not_source"), _value_at(summary, "receiving_context_is_not_source"))
        ),
        "receiving_context_is_not_authority": bool(
            _first_present(
                _value_at(statement, "receiving_context_is_not_authority"),
                _value_at(summary, "receiving_context_is_not_authority"),
            )
        ),
        "receiving_context_is_not_current": bool(
            _first_present(_value_at(statement, "receiving_context_is_not_current"), _value_at(summary, "receiving_context_is_not_current"))
        ),
        "eligibility_admissibility_is_review_readiness_only": bool(
            _first_present(
                _value_at(statement, "eligible_for_reception_review_only"),
                _value_at(summary, "eligible_for_review_only"),
            )
        ),
        "eligibility_did_not_recognize_reception": not _truthy(_first_present(_value_at(statement, "reception_recognized"), _value_at(summary, "reception_recognized"))),
        "eligibility_did_not_authorize_reception": not _truthy(_first_present(_value_at(statement, "reception_authorized"), _value_at(summary, "reception_authorized"))),
        "eligibility_did_not_receive_source": not _truthy(_first_present(_value_at(statement, "source_received"), _value_at(summary, "source_received"))),
        "eligibility_did_not_claim_non_capture_passed": not _contains_truthy_key(selected, "non_capture_passed"),
        "eligibility_did_not_claim_recognition_passed": not _contains_truthy_key(selected, "reception_recognition_passed"),
        "raw_selected_eligibility_result": _deepcopy(selected),
    }
    return section


def _selected_source_surface_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    surface: Any,
) -> dict[str, Any]:
    return {
        "selected_source_body_surface": _deepcopy(surface),
        "selected_source_body_surface_identifier": _surface_identifier(request, surface, selected),
        "selected_source_body_surface_type": _surface_type(request, surface, selected),
        "selected_source_body_surface_path": _first_present(
            request.get("selected_source_body_surface_path"),
            _value_at(surface, "selected_source_body_surface_path"),
            _value_at(surface, "path"),
        ),
        "selected_source_body_surface_reference": _surface_reference(request, surface, selected),
        "source_body_identity_basis": _first_present(
            request.get("source_body_identity_basis"),
            _value_at(surface, "source_body_identity_basis"),
            _nested(selected, "eligibility_basis", "source_body_identity_basis"),
        ),
        "source_body_lineage_basis": _first_present(
            request.get("source_body_lineage_basis"),
            _value_at(surface, "source_body_lineage_basis"),
            _nested(selected, "eligibility_basis", "source_body_lineage_basis"),
        ),
        "selected_source_body_surface_remains_source": True,
        "selected_source_body_surface_is_not_whole_body_by_default": True,
        "selected_source_body_surface_is_not_received": True,
        "selected_source_body_surface_is_not_adopted": True,
        "selected_source_body_surface_is_not_replaced": True,
        "selected_source_body_surface_is_not_validated_by_receiving_context": True,
        "selected_source_body_surface_is_not_invalidated_by_receiving_context": True,
    }


def _receiving_context_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    context: Any,
) -> dict[str, Any]:
    return {
        "receiving_context": _deepcopy(context),
        "receiving_context_id": _receiving_context_id(request, context, selected),
        "receiving_context_name": _value_at(context, "receiving_context_name", _value_at(context, "name")),
        "receiving_context_reference": _value_at(context, "receiving_context_reference", _value_at(context, "reference")),
        "receiving_context_type": _receiving_context_type(request, context, selected),
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


def _non_capture_basis_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    role_result: Any,
    identity_result: Any,
    declaration_result: Any,
    surface: Any,
    context: Any,
) -> dict[str, Any]:
    return {
        "selected_eligibility_result": _deepcopy(selected),
        "selected_receiving_context_role_result": _deepcopy(role_result),
        "selected_identity_preservation_result": _deepcopy(identity_result),
        "selected_reception_request_declaration_result": _deepcopy(declaration_result),
        "selected_source_body_surface": _deepcopy(surface),
        "source_body_identity_basis": _first_present(
            request.get("source_body_identity_basis"),
            _nested(selected, "eligibility_basis", "source_body_identity_basis"),
            _value_at(surface, "source_body_identity_basis"),
        ),
        "source_body_lineage_basis": _first_present(
            request.get("source_body_lineage_basis"),
            _nested(selected, "eligibility_basis", "source_body_lineage_basis"),
            _value_at(surface, "source_body_lineage_basis"),
        ),
        "receiving_context": _deepcopy(context),
        "receiving_context_type": _receiving_context_type(request, context, selected),
        "reception_class": _reception_value(request, selected, "reception_class"),
        "reception_purpose": _reception_value(request, selected, "reception_purpose"),
        "reception_limits": _reception_value(request, selected, "reception_limits"),
        "selected_receiving_context_role": _selected_role(request, selected, role_result),
        "receiving_context_role_class": _role_class(request, selected, role_result),
        "receiving_context_role_limits": _role_limits(request, selected, role_result),
        "eligibility_basis": _first_present(request.get("eligibility_basis"), _value_at(selected, "eligibility_basis")),
        "admissibility_basis": _first_present(request.get("admissibility_basis"), _value_at(selected, "admissibility_basis")),
        "review_readiness_limits": _first_present(request.get("review_readiness_limits"), _value_at(selected, "review_readiness_limits")),
        "non_capture_basis": _deepcopy(request.get("non_capture_basis")),
        "non_capture_review_only": True,
        "selected_source_body_surface_remains_uncaptured": True,
        "receiving_context_remains_context_only": True,
        "authority_capture_checked_and_refused": True,
        "validation_capture_checked_and_refused": True,
        "invalidation_capture_checked_and_refused": True,
        "source_replacement_capture_checked_and_refused": True,
        "operation_permission_capture_checked_and_refused": True,
        "governance_capture_checked_and_refused": True,
        "publication_flow_capture_checked_and_refused": True,
        "recognition_dependency": _deepcopy(request.get("recognition_dependency")),
        "recognition_dependency_preserved": _present(request.get("recognition_dependency")),
    }


def _non_adoption_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "non_adoption_basis": _deepcopy(request.get("non_adoption_basis")),
        "adoption_risk_checked_and_refused": True,
        "adoption_remains_false": True,
        "no_boundary_result_context_role_artifact_or_review_readiness_posture_adopted_the_selected_source_body_surface": True,
        "non_adoption_is_not_adoption": True,
        "non_adoption_does_not_authorize_reception": True,
        "non_adoption_does_not_receive_source": True,
    }


def _non_currentness_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "non_currentness_basis": _deepcopy(request.get("non_currentness_basis")),
        "currentness_risk_checked_and_refused": True,
        "currentness_remains_false": True,
        "selected_source_body_surface_was_not_made_current_by_this_boundary": True,
        "receiving_context_was_not_made_current_by_this_boundary": True,
        "role_result_eligibility_result_registry_reference_latest_artifact_carrier_context_or_narrative_convenience_did_not_create_currentness": True,
        "non_currentness_is_not_currentness": True,
        "non_currentness_does_not_authorize_reception": True,
        "non_currentness_does_not_receive_source": True,
    }


def _non_capture_scope_section(scope: Any) -> dict[str, Any]:
    values = _scope_values(scope)
    unsupported = [value for value in values if value not in SUPPORTED_NON_CAPTURE_SCOPE_VALUES]
    return {
        "selected_non_capture_scope_values": values,
        "all_selected_scope_values_supported": not unsupported,
        "unsupported_non_capture_scope_values": unsupported,
        "non_capture_review_only": "NON_CAPTURE_REVIEW_ONLY" in values,
        "non_adoption_review_only": "NON_ADOPTION_REVIEW_ONLY" in values,
        "non_currentness_review_only": "NON_CURRENTNESS_REVIEW_ONLY" in values,
        "non_capture_is_not_reception": "NON_CAPTURE_IS_NOT_RECEPTION" in values,
        "non_capture_is_not_authorization": "NON_CAPTURE_IS_NOT_AUTHORIZATION" in values,
        "non_capture_is_not_source_receipt": "NON_CAPTURE_IS_NOT_SOURCE_RECEIPT" in values,
        "non_capture_is_not_recognition": "NON_CAPTURE_IS_NOT_RECOGNITION" in values,
        "non_capture_does_not_validate_source": "NON_CAPTURE_DOES_NOT_VALIDATE_SOURCE" in values,
        "non_capture_does_not_invalidate_source": "NON_CAPTURE_DOES_NOT_INVALIDATE_SOURCE" in values,
        "no_source_replacement": "NO_SOURCE_REPLACEMENT" in values,
        "no_receiving_context_authority": "NO_RECEIVING_CONTEXT_AUTHORITY" in values,
        "no_receiving_context_currentness": "NO_RECEIVING_CONTEXT_CURRENTNESS" in values,
        "no_receiving_context_governance": "NO_RECEIVING_CONTEXT_GOVERNANCE" in values,
        "recognition_requires_separate_boundary": "RECOGNITION_REQUIRES_SEPARATE_BOUNDARY" in values,
    }


def _non_capture_non_meaning() -> dict[str, bool]:
    return {
        "does_not_mean_reception_recognized": True,
        "does_not_mean_reception_authorized": True,
        "does_not_mean_source_received": True,
        "does_not_mean_source_adopted": True,
        "does_not_mean_source_validated": True,
        "does_not_mean_source_invalidated": True,
        "does_not_mean_source_replaced": True,
        "does_not_mean_receiving_context_became_source": True,
        "does_not_mean_receiving_context_became_authority": True,
        "does_not_mean_receiving_context_became_current": True,
        "does_not_mean_receiving_context_became_receiver": True,
        "does_not_mean_receiving_context_became_adopter": True,
        "does_not_mean_receiving_context_became_validator": True,
        "does_not_mean_receiving_context_became_invalidator": True,
        "does_not_mean_receiving_context_became_operator": True,
        "does_not_mean_receiving_context_governance_created": True,
        "does_not_mean_standing_created": True,
        "does_not_mean_standing_propagated": True,
        "does_not_mean_vessel_relation_created": True,
        "does_not_mean_derivative_relation_created": True,
        "does_not_mean_operation_permission_created": True,
        "does_not_mean_reception_recognition_passed": True,
        "does_not_mean_public_readiness_created": True,
        "does_not_mean_final_completion_claimed": True,
        "does_not_mean_follow_on_work_authorized": True,
        "does_not_mean_continuation_authorized": True,
        "does_not_mean_publication_flow_opened": True,
    }


def _what_remains_open() -> dict[str, Any]:
    return {
        "open_items": [
            "source-body reception non-capture / non-adoption / non-currentness test",
            "source-body reception non-capture / non-adoption / non-currentness live artifact",
            "source-body reception recognition boundary",
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


def _additional_basis_required(outcome: str, request: Mapping[str, Any]) -> dict[str, Any]:
    required = outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
    return {
        "additional_basis_required": required,
        "additional_basis_context": _deepcopy(request.get("additional_basis_context")) if required else {},
        "missing_basis_not_scheduled": True,
        "missing_basis_not_authorized": True,
        "missing_basis_not_executed": True,
    }


def _not_passed_basis(outcome: str, request: Mapping[str, Any], checks: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    not_passed = outcome == OUTCOME_NOT_PASSED
    return {
        "not_passed": not_passed,
        "not_passed_basis": _deepcopy(request.get("not_passed_basis")) if not_passed else {},
        "failed_checks": [dict(check) for check in checks if not check.get("passed")] if not_passed else [],
        "does_not_mutate": True,
        "does_not_repair": True,
        "does_not_authorize": True,
        "does_not_receive": True,
        "does_not_replace": True,
        "does_not_validate": True,
        "does_not_invalidate": True,
        "does_not_create_currentness": True,
        "does_not_claim_recognition_passed": True,
        "does_not_recognize_reception": True,
    }


def _declared_question_section(
    request: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    surface: Any,
    context: Any,
    role_result: Any,
) -> dict[str, Any]:
    return {
        "non_capture_request_id": request.get("non_capture_request_id"),
        "non_capture_question": request.get("non_capture_question"),
        "non_capture_intent": request.get("non_capture_intent"),
        "selected_eligibility_result_id": _first_present(request.get("selected_eligibility_result_id"), _eligibility_id(selected)),
        "selected_eligibility_result_outcome": _declared_or_selected_eligibility_outcome(request, selected),
        "selected_source_body_surface_identifier": _surface_identifier(request, surface, selected),
        "selected_source_body_surface_type": _surface_type(request, surface, selected),
        "selected_source_body_surface_reference": _surface_reference(request, surface, selected),
        "receiving_context_id": _receiving_context_id(request, context, selected),
        "receiving_context_type": _receiving_context_type(request, context, selected),
        "receiving_context_role_class": _role_class(request, selected, role_result),
        "reception_class": _reception_value(request, selected, "reception_class"),
        "reception_purpose": _reception_value(request, selected, "reception_purpose"),
        "non_capture_is_not_reception": True,
        "non_capture_is_not_authorization": True,
        "non_capture_is_not_source_receipt": True,
        "non_capture_is_not_recognition": True,
        "recognition_requires_separate_boundary": True,
    }


def _determine_block_code(
    request: Mapping[str, Any] | None,
    selected: Mapping[str, Any] | None,
    selected_load_code: str | None,
    role_result: Any,
    identity_result: Any,
    declaration_result: Any,
    surface: Any,
    context: Any,
) -> str | None:
    if request is None:
        return "NON_CAPTURE_QUESTION_UNDECLARED"
    if not _is_mapping(request):
        return "DECLARED_NON_CAPTURE_REQUEST_MALFORMED"
    if not _present(request.get("non_capture_question")):
        return "NON_CAPTURE_QUESTION_UNDECLARED"
    intent = request.get("non_capture_intent")
    if intent == INTENT_BLOCK:
        return "NON_CAPTURE_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
    if intent not in SUPPORTED_INTENTS:
        return "NON_CAPTURE_INTENT_UNSUPPORTED"
    if selected_load_code:
        return selected_load_code
    if selected is None:
        return "ELIGIBILITY_RESULT_MISSING"
    if not _is_mapping(selected):
        return "ELIGIBILITY_RESULT_MALFORMED"
    selected_outcome = _declared_or_selected_eligibility_outcome(request, selected)
    if not _present(selected_outcome):
        return "ELIGIBILITY_RESULT_OUTCOME_MISSING"
    if selected_outcome != ELIGIBILITY_OUTCOME_RECORDED:
        return "ELIGIBILITY_RESULT_NOT_ELIGIBLE_ADMISSIBLE"
    failed_count = _failed_check_count(selected, "eligibility_checks")
    if failed_count not in (0, None):
        return "ELIGIBILITY_RESULT_HAS_FAILED_CHECKS"
    if not _present(role_result):
        return "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"
    if not _present(identity_result):
        return "IDENTITY_PRESERVATION_RESULT_MISSING"
    if not _present(declaration_result):
        return "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING"
    if not _present(surface):
        return "SELECTED_SOURCE_BODY_SURFACE_MISSING"
    if not _is_mapping(surface):
        return "SELECTED_SOURCE_BODY_SURFACE_MALFORMED"
    if not _present(context):
        return "RECEIVING_CONTEXT_MISSING"
    if not _is_mapping(context):
        return "RECEIVING_CONTEXT_MALFORMED"
    if not _present(_receiving_context_type(request, context, selected)):
        return "RECEIVING_CONTEXT_TYPE_MISSING"
    if not _present(_selected_role(request, selected, role_result)):
        return "RECEIVING_CONTEXT_ROLE_MISSING"
    if not _present(_role_class(request, selected, role_result)):
        return "RECEIVING_CONTEXT_ROLE_CLASS_MISSING"
    if not _present(_reception_value(request, selected, "reception_class")):
        return "RECEPTION_CLASS_MISSING"
    if not _present(_reception_value(request, selected, "reception_purpose")):
        return "RECEPTION_PURPOSE_MISSING"
    if not _present(_reception_value(request, selected, "reception_limits")):
        return "RECEPTION_LIMITS_MISSING"
    if not _present(request.get("non_capture_basis")):
        return "NON_CAPTURE_BASIS_MISSING"
    if not _present(request.get("non_adoption_basis")):
        return "NON_ADOPTION_BASIS_MISSING"
    if not _present(request.get("non_currentness_basis")):
        return "NON_CURRENTNESS_BASIS_MISSING"
    if not _present(request.get("recognition_dependency")):
        return "RECOGNITION_DEPENDENCY_MISSING"
    unsupported = _non_capture_scope_section(request.get("non_capture_scope"))["unsupported_non_capture_scope_values"]
    if unsupported:
        return "UNSUPPORTED_NON_CAPTURE_SCOPE"
    scan_roots = (request, selected)
    for field_name, block_code in COLLAPSE_FIELD_BLOCK_CODES:
        if any(_contains_truthy_key(root, field_name) for root in scan_roots):
            return block_code
    if any(_contains_truthy_key(root, field_name) for root in scan_roots for field_name in MUTATION_FIELDS):
        return "MUTATION_REPLAY_OR_MERGE_DETECTED"
    declared_non_claims = _non_claims_from_request(request)
    for claim in REQUIRED_NON_CLAIMS:
        if claim not in declared_non_claims or _truthy(declared_non_claims.get(claim)):
            return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _build_checks(
    request: Mapping[str, Any],
    selected_section: Mapping[str, Any],
    selected: Mapping[str, Any] | None,
    role_result: Any,
    identity_result: Any,
    declaration_result: Any,
    surface: Any,
    context: Any,
    block_code: str | None,
) -> list[dict[str, Any]]:
    intent = request.get("non_capture_intent")
    selected_outcome = _declared_or_selected_eligibility_outcome(request, selected)
    failed_count = _failed_check_count(selected, "eligibility_checks")
    scope_section = _non_capture_scope_section(request.get("non_capture_scope"))
    non_claims = _non_claims_from_request(request)
    checks = [
        _check("non_capture_question_declared", _present(request.get("non_capture_question")), "declared", request.get("non_capture_question"), "NON_CAPTURE_QUESTION_UNDECLARED"),
        _check("non_capture_intent_supported", intent in SUPPORTED_INTENTS, sorted(SUPPORTED_INTENTS), intent, "NON_CAPTURE_INTENT_UNSUPPORTED"),
        _check("selected_eligibility_result_present", _present(selected), "present", bool(selected), "ELIGIBILITY_RESULT_MISSING"),
        _check("selected_eligibility_outcome_declared", _present(selected_outcome), "declared", selected_outcome, "ELIGIBILITY_RESULT_OUTCOME_MISSING"),
        _check("selected_eligibility_outcome_eligible_admissible", selected_outcome == ELIGIBILITY_OUTCOME_RECORDED, ELIGIBILITY_OUTCOME_RECORDED, selected_outcome, "ELIGIBILITY_RESULT_NOT_ELIGIBLE_ADMISSIBLE"),
        _check("selected_eligibility_failed_check_count_zero", failed_count in (0, None), 0, failed_count, "ELIGIBILITY_RESULT_HAS_FAILED_CHECKS"),
        _check("selected_receiving_context_role_result_preserved", _present(role_result), "preserved", bool(role_result), "RECEIVING_CONTEXT_ROLE_RESULT_MISSING"),
        _check("selected_identity_preservation_result_preserved", _present(identity_result), "preserved", bool(identity_result), "IDENTITY_PRESERVATION_RESULT_MISSING"),
        _check("selected_request_declaration_result_preserved", _present(declaration_result), "preserved", bool(declaration_result), "RECEPTION_REQUEST_DECLARATION_RESULT_MISSING"),
        _check("selected_source_body_surface_preserved", _present(surface), "preserved", bool(surface), "SELECTED_SOURCE_BODY_SURFACE_MISSING"),
        _check("selected_source_body_surface_remains_source", not _contains_truthy_key(surface, "source_replaced"), "remains source", "remains source"),
        _check("selected_surface_is_not_whole_body_by_default", not _contains_truthy_key(surface, "selected_surface_is_whole_body_by_default"), "not whole body", "not whole body"),
        _check("receiving_context_preserved", _present(context), "preserved", bool(context), "RECEIVING_CONTEXT_MISSING"),
        _check("receiving_context_remains_context_only", not _contains_truthy_key(context, "receiving_context_became_source"), "context only", "context only"),
        _check("receiving_context_is_not_source", not _contains_truthy_key(context, "receiving_context_became_source"), False, _contains_truthy_key(context, "receiving_context_became_source"), "NON_CAPTURE_TREATS_CONTEXT_AS_SOURCE"),
        _check("receiving_context_is_not_authority", not _contains_truthy_key(context, "receiving_context_became_authority"), False, _contains_truthy_key(context, "receiving_context_became_authority"), "NON_CAPTURE_TREATS_CONTEXT_AS_AUTHORITY"),
        _check("receiving_context_is_not_current", not _contains_truthy_key(context, "receiving_context_became_current"), False, _contains_truthy_key(context, "receiving_context_became_current"), "NON_CAPTURE_TREATS_CONTEXT_AS_CURRENT"),
        _check("receiving_context_role_preserved", _present(_selected_role(request, selected, role_result)), "preserved", _selected_role(request, selected, role_result), "RECEIVING_CONTEXT_ROLE_MISSING"),
        _check("receiving_context_role_remains_bounded", _present(_role_class(request, selected, role_result)), "bounded", _role_class(request, selected, role_result), "RECEIVING_CONTEXT_ROLE_CLASS_MISSING"),
        _check("eligibility_admissibility_review_readiness_only", bool(selected_section.get("eligibility_admissibility_is_review_readiness_only")), True, selected_section.get("eligibility_admissibility_is_review_readiness_only")),
        _check("reception_unrecognized", not any(_contains_truthy_key(root, "reception_recognized") for root in (request, selected)), False, any(_contains_truthy_key(root, "reception_recognized") for root in (request, selected)), "NON_CAPTURE_RECOGNIZES_RECEPTION"),
        _check("reception_unauthorized", not any(_contains_truthy_key(root, "reception_authorized") for root in (request, selected)), False, any(_contains_truthy_key(root, "reception_authorized") for root in (request, selected)), "NON_CAPTURE_AUTHORIZES_RECEPTION"),
        _check("source_unreceived", not any(_contains_truthy_key(root, "source_received") for root in (request, selected)), False, any(_contains_truthy_key(root, "source_received") for root in (request, selected)), "NON_CAPTURE_RECEIVES_SOURCE"),
        _check("non_capture_basis_declared", _present(request.get("non_capture_basis")), "declared", request.get("non_capture_basis"), "NON_CAPTURE_BASIS_MISSING"),
        _check("non_adoption_basis_declared", _present(request.get("non_adoption_basis")), "declared", request.get("non_adoption_basis"), "NON_ADOPTION_BASIS_MISSING"),
        _check("non_currentness_basis_declared", _present(request.get("non_currentness_basis")), "declared", request.get("non_currentness_basis"), "NON_CURRENTNESS_BASIS_MISSING"),
        _check("recognition_dependency_declared", _present(request.get("recognition_dependency")), "declared", request.get("recognition_dependency"), "RECOGNITION_DEPENDENCY_MISSING"),
        _check("adoption_remains_false", not any(_contains_truthy_key(root, "adoption_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "adoption_created") for root in (request, selected)), "NON_CAPTURE_CREATES_ADOPTION"),
        _check("authority_remains_false", not any(_contains_truthy_key(root, "authority_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "authority_created") for root in (request, selected)), "NON_CAPTURE_CREATES_AUTHORITY"),
        _check("currentness_remains_false", not any(_contains_truthy_key(root, "currentness_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "currentness_created") for root in (request, selected)), "NON_CAPTURE_CREATES_CURRENTNESS"),
        _check("standing_remains_false", not any(_contains_truthy_key(root, "standing_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "standing_created") for root in (request, selected)), "NON_CAPTURE_CREATES_STANDING"),
        _check("source_validation_false", not any(_contains_truthy_key(root, "source_validated_by_receiving_context") for root in (request, selected)), False, any(_contains_truthy_key(root, "source_validated_by_receiving_context") for root in (request, selected)), "NON_CAPTURE_VALIDATES_SOURCE"),
        _check("source_invalidation_false", not any(_contains_truthy_key(root, "source_invalidated_by_receiving_context") for root in (request, selected)), False, any(_contains_truthy_key(root, "source_invalidated_by_receiving_context") for root in (request, selected)), "NON_CAPTURE_INVALIDATES_SOURCE"),
        _check("source_replacement_false", not any(_contains_truthy_key(root, "source_replaced") for root in (request, selected)), False, any(_contains_truthy_key(root, "source_replaced") for root in (request, selected)), "NON_CAPTURE_REPLACES_SOURCE"),
        _check("operation_permission_false", not any(_contains_truthy_key(root, "operation_permission_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "operation_permission_created") for root in (request, selected)), "NON_CAPTURE_CREATES_OPERATION_PERMISSION"),
        _check("receiving_context_governance_false", not any(_contains_truthy_key(root, "receiving_context_governance_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "receiving_context_governance_created") for root in (request, selected)), "NON_CAPTURE_CREATES_GOVERNANCE"),
        _check("publication_flow_false", not any(_contains_truthy_key(root, "publication_flow_opened") for root in (request, selected)), False, any(_contains_truthy_key(root, "publication_flow_opened") for root in (request, selected)), "NON_CAPTURE_OPENS_PUBLICATION_FLOW"),
        _check("public_readiness_false", not any(_contains_truthy_key(root, "public_launch_readiness_created") for root in (request, selected)), False, any(_contains_truthy_key(root, "public_launch_readiness_created") for root in (request, selected)), "NON_CAPTURE_CREATES_PUBLIC_READINESS"),
        _check("final_completion_false", not any(_contains_truthy_key(root, "final_completion_claimed") for root in (request, selected)), False, any(_contains_truthy_key(root, "final_completion_claimed") for root in (request, selected)), "NON_CAPTURE_CLAIMS_FINAL_COMPLETION"),
        _check("follow_on_work_false", not any(_contains_truthy_key(root, "follow_on_work_authorized") for root in (request, selected)), False, any(_contains_truthy_key(root, "follow_on_work_authorized") for root in (request, selected)), "NON_CAPTURE_AUTHORIZES_FOLLOW_ON_WORK"),
        _check("continuation_false", not any(_contains_truthy_key(root, "continuation_authorized") for root in (request, selected)), False, any(_contains_truthy_key(root, "continuation_authorized") for root in (request, selected)), "NON_CAPTURE_AUTHORIZES_CONTINUATION"),
        _check("recognition_future", True, "future boundary", "future boundary"),
        _check("recognition_passed_false", not any(_contains_truthy_key(root, "reception_recognition_passed") for root in (request, selected)), False, any(_contains_truthy_key(root, "reception_recognition_passed") for root in (request, selected)), "NON_CAPTURE_CLAIMS_RECOGNITION_PASSED"),
        _check("no_mutation_replay_merge", not any(_contains_truthy_key(root, field) for root in (request, selected) for field in MUTATION_FIELDS), False, any(_contains_truthy_key(root, field) for root in (request, selected) for field in MUTATION_FIELDS), "MUTATION_REPLAY_OR_MERGE_DETECTED"),
        _check("non_claims_remain_false", all(claim in non_claims and not _truthy(non_claims.get(claim)) for claim in REQUIRED_NON_CLAIMS), "all required non-claims false", "all required non-claims false" if non_claims else "missing", "NON_CLAIM_MISSING_OR_FLIPPED"),
        _check("non_capture_scope_supported", scope_section["all_selected_scope_values_supported"], "supported scope values", scope_section["unsupported_non_capture_scope_values"], "UNSUPPORTED_NON_CAPTURE_SCOPE"),
    ]
    if block_code:
        for check in checks:
            if check.get("block_code") == block_code:
                check["passed"] = False
                break
    return checks


def _non_capture_statement(outcome: str) -> dict[str, Any]:
    passed = outcome == OUTCOME_PASSED
    statement = {
        "source_body_reception_non_capture_passed": passed,
        "non_capture_boundary_recorded": passed,
        "non_capture_passed": passed,
        "non_adoption_passed": passed,
        "non_currentness_passed": passed,
        "selected_eligibility_result_preserved": passed,
        "selected_eligibility_result_recorded": passed,
        "selected_eligibility_result_failed_check_count_zero": passed,
        "selected_receiving_context_role_result_preserved": passed,
        "selected_identity_preservation_result_preserved": passed,
        "selected_reception_request_declaration_result_preserved": passed,
        "selected_source_body_surface_preserved": passed,
        "selected_source_body_surface_remains_source": passed,
        "selected_surface_is_not_whole_body_by_default": passed,
        "receiving_context_preserved": passed,
        "receiving_context_remains_context_only": passed,
        "receiving_context_is_not_source": passed,
        "receiving_context_is_not_authority": passed,
        "receiving_context_is_not_current": passed,
        "receiving_context_role_preserved": passed,
        "receiving_context_role_remains_bounded": passed,
        "eligibility_admissibility_is_review_readiness_only": passed,
        "adoption_risk_checked_and_refused": passed,
        "currentness_risk_checked_and_refused": passed,
        "authority_capture_checked_and_refused": passed,
        "validation_capture_checked_and_refused": passed,
        "invalidation_capture_checked_and_refused": passed,
        "source_replacement_capture_checked_and_refused": passed,
        "operation_permission_capture_checked_and_refused": passed,
        "governance_capture_checked_and_refused": passed,
        "publication_flow_capture_checked_and_refused": passed,
        "recognition_dependency_preserved": passed,
        "recognition_requires_separate_boundary": True,
    }
    statement.update(_base_false_non_claims())
    return statement


def _requested_outcome(request: Mapping[str, Any], block_code: str | None) -> str:
    if block_code:
        return OUTCOME_BLOCKED
    requested = request.get("requested_non_capture_outcome", OUTCOME_PASSED)
    if requested in {OUTCOME_PASSED, OUTCOME_NOT_PASSED, OUTCOME_REQUIRES_ADDITIONAL_BASIS}:
        return requested
    if request.get("non_capture_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_PASSED
    return OUTCOME_BLOCKED


def _build_result(
    request: Mapping[str, Any],
    *,
    request_path: str | None = None,
    selected: Mapping[str, Any] | None = None,
    selected_path: str | None = None,
    selected_load_code: str | None = None,
) -> dict[str, Any]:
    role_result = _selected_role_result(request, selected)
    identity_result = _identity_result(request, selected, role_result)
    declaration_result = _request_declaration_result(request, selected, role_result, identity_result)
    surface = _selected_source_surface(request, selected, role_result, identity_result)
    context = _receiving_context(request, selected, role_result)
    block_code = _determine_block_code(
        request,
        selected,
        selected_load_code,
        role_result,
        identity_result,
        declaration_result,
        surface,
        context,
    )
    outcome = _requested_outcome(request, block_code)
    result_id_basis = _first_present(
        request.get("non_capture_request_id"),
        request.get("selected_eligibility_result_id"),
        _eligibility_id(selected),
        "non_capture_request",
    )
    metadata = {
        "source_body_reception_non_capture_result_id": f"{result_id_basis}__source_body_reception_non_capture_result",
        "source_body_reception_non_capture_result_type": "source_body_reception_non_capture_non_adoption_non_currentness_boundary_result",
        "source_body_reception_non_capture_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }
    selected_section = _selected_eligibility_section(request, selected, selected_path)
    checks = _build_checks(request, selected_section, selected, role_result, identity_result, declaration_result, surface, context, block_code)
    block_reason = request.get("block_reason") if _present(request.get("block_reason")) else block_code
    result: dict[str, Any] = {
        "source_body_reception_non_capture_metadata": metadata,
        "declared_non_capture_question": _declared_question_section(request, selected, surface, context, role_result),
        "selected_eligibility_result": selected_section,
        "selected_source_body_surface": _selected_source_surface_section(request, selected, surface),
        "receiving_context": _receiving_context_section(request, selected, context),
        "non_capture_basis": _non_capture_basis_section(request, selected, role_result, identity_result, declaration_result, surface, context),
        "non_adoption_basis": _non_adoption_basis_section(request),
        "non_currentness_basis": _non_currentness_basis_section(request),
        "non_capture_scope": _non_capture_scope_section(request.get("non_capture_scope")),
        "non_capture_checks": checks,
        "non_capture_statement": _non_capture_statement(outcome),
        "non_capture_non_meaning": _non_capture_non_meaning(),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_passed_basis": _not_passed_basis(outcome, request, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _result_non_claims(outcome),
        "outcome": outcome,
        "block": _block(block_code, block_reason if block_code else None),
    }
    if request_path:
        result["declared_non_capture_question"]["declared_non_capture_request_path"] = request_path
    result["source_body_reception_non_capture_summary"] = build_source_body_reception_non_capture_summary(result)
    return result


def _blocked_result_for_request_error(code: str, reason: str | None, request_path: str | None = None) -> dict[str, Any]:
    request: dict[str, Any] = {
        "non_capture_request_id": "undeclared_non_capture_request",
        "non_capture_question": None,
        "non_capture_intent": None,
        "selected_eligibility_result": {},
        "non_capture_basis": {},
        "non_adoption_basis": {},
        "non_currentness_basis": {},
        "non_capture_scope": [],
        "declared_non_claims": {},
        "block_reason": reason or code,
    }
    result = _build_result(request, request_path=request_path, selected={}, selected_load_code=None)
    result["outcome"] = OUTCOME_BLOCKED
    result["block"] = _block(code, reason or code)
    result["non_capture_statement"] = _non_capture_statement(OUTCOME_BLOCKED)
    result["non_claims"] = _result_non_claims(OUTCOME_BLOCKED)
    result["source_body_reception_non_capture_summary"] = build_source_body_reception_non_capture_summary(result)
    return result


def resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary(
    declared_non_capture_request: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one declared non-capture request mapping into a bounded result."""
    if declared_non_capture_request is None:
        return _blocked_result_for_request_error("NON_CAPTURE_QUESTION_UNDECLARED", "non-capture question undeclared")
    if not _is_mapping(declared_non_capture_request):
        return _blocked_result_for_request_error(
            "DECLARED_NON_CAPTURE_REQUEST_MALFORMED",
            "declared non-capture request must be a JSON object mapping",
        )
    request = _deepcopy(dict(declared_non_capture_request))
    selected, selected_load_code, selected_path = _load_selected_eligibility_result(request)
    return _build_result(
        request,
        selected=selected,
        selected_path=selected_path,
        selected_load_code=selected_load_code,
    )


def resolve_source_body_reception_non_capture_non_adoption_non_currentness_boundary_from_path(
    declared_non_capture_request_path: Path | str,
) -> dict:
    """Resolve one declared non-capture request JSON object from a path."""
    parsed, error = _read_json_object(declared_non_capture_request_path)
    if error == "unreadable":
        return _blocked_result_for_request_error(
            "DECLARED_NON_CAPTURE_REQUEST_UNREADABLE",
            "declared non-capture request path is unreadable or not valid JSON",
            str(declared_non_capture_request_path),
        )
    if error == "malformed":
        return _blocked_result_for_request_error(
            "DECLARED_NON_CAPTURE_REQUEST_MALFORMED",
            "declared non-capture request JSON must be an object",
            str(declared_non_capture_request_path),
        )
    request = _deepcopy(parsed)
    selected, selected_load_code, selected_path = _load_selected_eligibility_result(request)
    return _build_result(
        request,
        request_path=str(declared_non_capture_request_path),
        selected=selected,
        selected_path=selected_path,
        selected_load_code=selected_load_code,
    )


def build_source_body_reception_non_capture_summary(result: Mapping[str, Any]) -> dict:
    """Build a compact summary preserving the non-capture boundary posture."""
    checks = result.get("non_capture_checks", []) if _is_mapping(result) else []
    passed_check_count = sum(1 for check in checks if _is_mapping(check) and check.get("passed"))
    failed_check_count = sum(1 for check in checks if _is_mapping(check) and not check.get("passed"))
    statement = result.get("non_capture_statement", {}) if _is_mapping(result) else {}
    question = result.get("declared_non_capture_question", {}) if _is_mapping(result) else {}
    selected = result.get("selected_eligibility_result", {}) if _is_mapping(result) else {}
    surface = result.get("selected_source_body_surface", {}) if _is_mapping(result) else {}
    context = result.get("receiving_context", {}) if _is_mapping(result) else {}
    basis = result.get("non_capture_basis", {}) if _is_mapping(result) else {}
    block = result.get("block", {}) if _is_mapping(result) else {}
    non_claims = result.get("non_claims", {}) if _is_mapping(result) else {}
    outcome = result.get("outcome") if _is_mapping(result) else None
    return {
        "outcome": outcome,
        "block_code": _value_at(block, "code"),
        "block_reason": _value_at(block, "reason"),
        "non_capture_request_id": _value_at(question, "non_capture_request_id"),
        "non_capture_question": _value_at(question, "non_capture_question"),
        "non_capture_intent": _value_at(question, "non_capture_intent"),
        "selected_eligibility_result_id": _value_at(selected, "selected_eligibility_result_id"),
        "selected_eligibility_result_outcome": _value_at(selected, "selected_eligibility_result_outcome"),
        "selected_source_body_surface_identifier": _value_at(surface, "selected_source_body_surface_identifier"),
        "selected_source_body_surface_type": _value_at(surface, "selected_source_body_surface_type"),
        "selected_source_body_surface_reference": _value_at(surface, "selected_source_body_surface_reference"),
        "receiving_context_id": _value_at(context, "receiving_context_id"),
        "receiving_context_type": _value_at(context, "receiving_context_type"),
        "reception_class": _value_at(basis, "reception_class"),
        "reception_purpose": _value_at(basis, "reception_purpose"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "non_capture_passed": outcome == OUTCOME_PASSED,
        "non_adoption_passed": bool(_value_at(statement, "non_adoption_passed")),
        "non_currentness_passed": bool(_value_at(statement, "non_currentness_passed")),
        "not_passed": outcome == OUTCOME_NOT_PASSED,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_eligibility_result_preserved": _value_at(statement, "selected_eligibility_result_preserved"),
        "selected_eligibility_result_recorded": _value_at(statement, "selected_eligibility_result_recorded"),
        "selected_eligibility_result_failed_check_count_zero": _value_at(statement, "selected_eligibility_result_failed_check_count_zero"),
        "selected_receiving_context_role_result_preserved": _value_at(statement, "selected_receiving_context_role_result_preserved"),
        "selected_identity_preservation_result_preserved": _value_at(statement, "selected_identity_preservation_result_preserved"),
        "selected_request_declaration_result_preserved": _value_at(statement, "selected_reception_request_declaration_result_preserved"),
        "selected_source_body_surface_preserved": _value_at(statement, "selected_source_body_surface_preserved"),
        "selected_source_body_surface_remains_source": _value_at(statement, "selected_source_body_surface_remains_source"),
        "selected_surface_is_not_whole_body_by_default": _value_at(statement, "selected_surface_is_not_whole_body_by_default"),
        "receiving_context_preserved": _value_at(statement, "receiving_context_preserved"),
        "receiving_context_remains_context_only": _value_at(statement, "receiving_context_remains_context_only"),
        "receiving_context_is_not_source": _value_at(statement, "receiving_context_is_not_source"),
        "receiving_context_is_not_authority": _value_at(statement, "receiving_context_is_not_authority"),
        "receiving_context_is_not_current": _value_at(statement, "receiving_context_is_not_current"),
        "receiving_context_role_preserved": _value_at(statement, "receiving_context_role_preserved"),
        "receiving_context_role_remains_bounded": _value_at(statement, "receiving_context_role_remains_bounded"),
        "eligibility_admissibility_review_readiness_only": _value_at(statement, "eligibility_admissibility_is_review_readiness_only"),
        "adoption_risk_checked_refused": _value_at(statement, "adoption_risk_checked_and_refused"),
        "currentness_risk_checked_refused": _value_at(statement, "currentness_risk_checked_and_refused"),
        "authority_capture_checked_refused": _value_at(statement, "authority_capture_checked_and_refused"),
        "validation_capture_checked_refused": _value_at(statement, "validation_capture_checked_and_refused"),
        "invalidation_capture_checked_refused": _value_at(statement, "invalidation_capture_checked_and_refused"),
        "source_replacement_capture_checked_refused": _value_at(statement, "source_replacement_capture_checked_and_refused"),
        "operation_permission_capture_checked_refused": _value_at(statement, "operation_permission_capture_checked_and_refused"),
        "governance_capture_checked_refused": _value_at(statement, "governance_capture_checked_and_refused"),
        "publication_flow_capture_checked_refused": _value_at(statement, "publication_flow_capture_checked_and_refused"),
        "recognition_dependency_preserved": _value_at(statement, "recognition_dependency_preserved"),
        "recognition_requires_separate_boundary": _value_at(statement, "recognition_requires_separate_boundary"),
        "no_reception_recognized": not _truthy(_value_at(non_claims, "reception_recognized")),
        "no_reception_authorized": not _truthy(_value_at(non_claims, "reception_authorized")),
        "no_source_received": not _truthy(_value_at(non_claims, "source_received")),
        "no_recognition_passed": not _truthy(_value_at(non_claims, "reception_recognition_passed")),
        "no_source_validation": not _truthy(_value_at(non_claims, "source_validated_by_receiving_context")),
        "no_source_invalidation": not _truthy(_value_at(non_claims, "source_invalidated_by_receiving_context")),
        "no_source_replacement": not _truthy(_value_at(non_claims, "source_replaced")),
        "no_adoption": not _truthy(_value_at(non_claims, "adoption_created")),
        "no_authority": not _truthy(_value_at(non_claims, "authority_created")),
        "no_currentness": not _truthy(_value_at(non_claims, "currentness_created")),
        "no_standing": not _truthy(_value_at(non_claims, "standing_created")),
        "no_vessel_relation": not _truthy(_value_at(non_claims, "vessel_relation_created")),
        "no_derivative_relation": not _truthy(_value_at(non_claims, "derivative_relation_created")),
        "no_operation_permission": not _truthy(_value_at(non_claims, "operation_permission_created")),
        "no_governance": not _truthy(_value_at(non_claims, "receiving_context_governance_created")),
        "no_publication_flow": not _truthy(_value_at(non_claims, "publication_flow_opened")),
        "no_public_readiness": not _truthy(_value_at(non_claims, "public_launch_readiness_created")),
        "no_final_completion": not _truthy(_value_at(non_claims, "final_completion_claimed")),
        "no_follow_on_work": not _truthy(_value_at(non_claims, "follow_on_work_authorized")),
        "key_non_claims": _deepcopy(non_claims),
    }


def write_source_body_reception_non_capture_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write an additive non-capture result artifact without overwriting."""
    if not _is_mapping(result):
        raise SourceBodyReceptionNonCaptureBoundaryError("result must be a mapping")
    if output_path is None:
        metadata = result.get("source_body_reception_non_capture_metadata", {})
        question = result.get("declared_non_capture_question", {})
        basis = _first_present(
            _value_at(question, "non_capture_request_id"),
            _value_at(question, "selected_eligibility_result_id"),
            _value_at(metadata, "source_body_reception_non_capture_result_id"),
            "non_capture_request",
        )
        filename = f"{_safe_component(basis)}__source_body_reception_non_capture_result.json"
        candidate = SOURCE_BODY_RECEPTION_NON_CAPTURE_BOUNDARY_ROOT / filename
    else:
        candidate = Path(output_path)
    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    suffix = 1
    while final_path.exists():
        final_path = candidate.with_name(f"{candidate.stem}_{suffix:03d}{candidate.suffix}")
        suffix += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_source_body_reception_non_capture_request(
    non_capture_request_id: str,
    non_capture_question: str,
    selected_eligibility_result: Mapping[str, Any] | str,
    non_capture_basis: Mapping[str, Any] | str,
    non_adoption_basis: Mapping[str, Any] | str,
    non_currentness_basis: Mapping[str, Any] | str,
    non_capture_scope: Sequence[str] | Mapping[str, Any],
    non_capture_intent: str = INTENT_RECORD,
    *,
    selected_eligibility_result_path: str | None = None,
    selected_eligibility_result_id: str | None = None,
    selected_eligibility_result_outcome: str | None = None,
    requested_non_capture_outcome: str = OUTCOME_PASSED,
    recognition_dependency: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_passed_basis: Mapping[str, Any] | str | None = None,
) -> dict:
    """Build a declared non-capture request with required non-claims false."""
    request: dict[str, Any] = {
        "non_capture_request_id": non_capture_request_id,
        "non_capture_question": non_capture_question,
        "non_capture_intent": non_capture_intent,
        "selected_eligibility_result": _deepcopy(selected_eligibility_result)
        if _is_mapping(selected_eligibility_result)
        else selected_eligibility_result,
        "non_capture_basis": _deepcopy(non_capture_basis),
        "non_adoption_basis": _deepcopy(non_adoption_basis),
        "non_currentness_basis": _deepcopy(non_currentness_basis),
        "non_capture_scope": _deepcopy(non_capture_scope),
        "declared_non_claims": _base_false_non_claims(),
        "requested_non_capture_outcome": requested_non_capture_outcome,
        "recognition_dependency": _deepcopy(recognition_dependency)
        if recognition_dependency is not None
        else {
            "recognition_requires_separate_boundary": True,
            "reception_recognition_passed": False,
        },
        "additional_basis_context": _deepcopy(additional_basis_context or {}),
        "not_passed_basis": _deepcopy(not_passed_basis or {}),
    }
    if selected_eligibility_result_path is not None:
        request["selected_eligibility_result_path"] = selected_eligibility_result_path
    if selected_eligibility_result_id is not None:
        request["selected_eligibility_result_id"] = selected_eligibility_result_id
    if selected_eligibility_result_outcome is not None:
        request["selected_eligibility_result_outcome"] = selected_eligibility_result_outcome
    return request
