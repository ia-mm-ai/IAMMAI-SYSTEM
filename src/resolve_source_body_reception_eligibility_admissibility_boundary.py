"""Resolve source-body reception eligibility / admissibility boundary.

This resolver records review-readiness for one declared source-body reception
request after request declaration, identity preservation, and receiving-context
role have been recorded. Eligibility is not reception. Admissibility is not
authorization. This resolver does not receive source, create recognition,
replace source, validate or invalidate source, make receiving context source,
authority, current, receiver, adopter, validator, invalidator, operator, or
governance, create operation permission, publication flow, public readiness,
final completion, continuation, or follow-on work.
"""

from __future__ import annotations

import copy
import datetime
import json
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import Any


class SourceBodyReceptionEligibilityAdmissibilityBoundaryError(Exception):
    """Raised for hard source-body reception eligibility failures."""


RESOLVER_MODULE = "resolve_source_body_reception_eligibility_admissibility_boundary"
RESULT_VERSION = "0.1.0"
RESULT_TYPE = "source_body_reception_eligibility_admissibility_result"
RESULT_ID_PREFIX = "source_body_reception_eligibility_admissibility"

SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY_BOUNDARY_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_source_body_reception_eligibility_admissibility_boundary"
)

RECEIVING_CONTEXT_ROLE_OUTCOME = "SOURCE_BODY_RECEPTION_RECEIVING_CONTEXT_ROLE_RECORDED"

OUTCOME_ELIGIBLE_ADMISSIBLE = "SOURCE_BODY_RECEPTION_ELIGIBLE_ADMISSIBLE_FOR_REVIEW"
OUTCOME_NOT_ELIGIBLE = "SOURCE_BODY_RECEPTION_NOT_ELIGIBLE_OR_ADMISSIBLE"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "SOURCE_BODY_RECEPTION_ELIGIBILITY_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "SOURCE_BODY_RECEPTION_ELIGIBILITY_REVIEW_BLOCKED"
OUTCOME_FAMILY = {
    OUTCOME_ELIGIBLE_ADMISSIBLE,
    OUTCOME_NOT_ELIGIBLE,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
}

INTENT_RECORD = "RECORD_SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY"
INTENT_BLOCK = "BLOCK_SOURCE_BODY_RECEPTION_ELIGIBILITY_REVIEW"
SUPPORTED_INTENTS = {INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK}

SUPPORTED_RECEPTION_ELIGIBILITY_SCOPE = (
    "ELIGIBLE_FOR_RECEPTION_REVIEW_ONLY",
    "ADMISSIBLE_FOR_RECEPTION_REVIEW_ONLY",
    "ELIGIBILITY_IS_NOT_RECEPTION",
    "ADMISSIBILITY_IS_NOT_AUTHORIZATION",
    "ELIGIBILITY_IS_NOT_SOURCE_RECEIPT",
    "ELIGIBILITY_IS_NOT_ADOPTION",
    "ELIGIBILITY_IS_NOT_AUTHORITY",
    "ELIGIBILITY_IS_NOT_CURRENTNESS",
    "ELIGIBILITY_IS_NOT_VALIDATION",
    "ELIGIBILITY_IS_NOT_INVALIDATION",
    "ELIGIBILITY_IS_NOT_OPERATION_PERMISSION",
    "ELIGIBILITY_IS_NOT_PUBLICATION_FLOW",
    "NON_CAPTURE_REQUIRES_SEPARATE_BOUNDARY",
    "RECOGNITION_REQUIRES_SEPARATE_BOUNDARY",
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
    "non_capture_passed",
    "reception_recognition_passed",
    "mutation_performed",
    "replay_performed",
    "merge_performed",
)

COLLAPSE_FIELDS = {
    "RECEPTION_ELIGIBILITY_RECOGNIZES_RECEPTION": (
        "reception_recognized",
        "source_body_reception_recognized",
        "eligibility_recognizes_reception",
        "eligibility_review_recognizes_reception",
    ),
    "RECEPTION_ELIGIBILITY_AUTHORIZES_RECEPTION": (
        "reception_authorized",
        "source_body_reception_authorized",
        "eligibility_authorizes_reception",
        "admissibility_authorizes_reception",
    ),
    "RECEPTION_ELIGIBILITY_RECEIVES_SOURCE": (
        "source_received",
        "source_body_received",
        "eligibility_receives_source",
        "admissibility_receives_source",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_GOVERNANCE": (
        "receiving_context_governance_created",
        "receiving_context_governance",
        "governance_created",
        "eligibility_creates_governance",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_SOURCE": (
        "receiving_context_became_source",
        "receiving_context_treated_as_source",
        "receiving_context_is_source",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_AUTHORITY": (
        "receiving_context_became_authority",
        "receiving_context_treated_as_authority",
        "receiving_context_is_authority",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_CURRENT": (
        "receiving_context_became_current",
        "receiving_context_treated_as_current",
        "receiving_context_is_current",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_RECEIVER": (
        "receiving_context_became_receiver",
        "receiving_context_treated_as_receiver",
        "receiving_context_is_receiver",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_ADOPTER": (
        "receiving_context_became_adopter",
        "receiving_context_treated_as_adopter",
        "receiving_context_is_adopter",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_VALIDATOR": (
        "receiving_context_became_validator",
        "receiving_context_treated_as_validator",
        "receiving_context_is_validator",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_INVALIDATOR": (
        "receiving_context_became_invalidator",
        "receiving_context_treated_as_invalidator",
        "receiving_context_is_invalidator",
    ),
    "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_OPERATOR": (
        "receiving_context_became_operator",
        "receiving_context_treated_as_operator",
        "receiving_context_is_operator",
    ),
    "RECEPTION_ELIGIBILITY_VALIDATES_SOURCE": (
        "source_validated_by_receiving_context",
        "source_validated",
        "receiving_context_validates_source",
        "eligibility_validates_source",
    ),
    "RECEPTION_ELIGIBILITY_INVALIDATES_SOURCE": (
        "source_invalidated_by_receiving_context",
        "source_invalidated",
        "receiving_context_invalidates_source",
        "eligibility_invalidates_source",
    ),
    "RECEPTION_ELIGIBILITY_REPLACES_SOURCE": (
        "source_replaced",
        "source_body_replaced",
        "source_replacement_created",
        "eligibility_replaces_source",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_ADOPTION": (
        "adoption_created",
        "source_adopted",
        "eligibility_creates_adoption",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_AUTHORITY": (
        "authority_created",
        "source_authority_created",
        "eligibility_creates_authority",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_CURRENTNESS": (
        "currentness_created",
        "source_currentness_created",
        "eligibility_creates_currentness",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_STANDING": (
        "standing_created",
        "source_standing_created",
        "eligibility_creates_standing",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_STANDING_PROPAGATION": (
        "standing_propagated",
        "standing_propagation_created",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_VESSEL_RELATION": (
        "vessel_relation_created",
        "vessel_relation_authorized",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_DERIVATIVE_RELATION": (
        "derivative_relation_created",
        "derivative_reception_created",
        "derivative_relation_authorized",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_OPERATION_PERMISSION": (
        "operation_permission_created",
        "operation_authorized",
        "permission_created",
        "eligibility_creates_operation_permission",
    ),
    "RECEPTION_ELIGIBILITY_CREATES_PUBLIC_READINESS": (
        "public_launch_readiness_created",
        "public_readiness_created",
        "public_launch_ready",
    ),
    "RECEPTION_ELIGIBILITY_CLAIMS_FINAL_COMPLETION": (
        "final_completion_claimed",
        "final_system_completion_claimed",
        "final_completion_created",
    ),
    "RECEPTION_ELIGIBILITY_AUTHORIZES_FOLLOW_ON_WORK": (
        "follow_on_work_authorized",
        "follow_on_work_scheduled",
        "successor_scheduled",
    ),
    "RECEPTION_ELIGIBILITY_AUTHORIZES_CONTINUATION": (
        "continuation_authorized",
        "continuation_scheduled",
        "self_orientation_successor_scheduled",
    ),
    "RECEPTION_ELIGIBILITY_OPENS_PUBLICATION_FLOW": (
        "publication_flow_opened",
        "publication_authorized",
        "public_flow_opened",
    ),
    "RECEPTION_ELIGIBILITY_CLAIMS_NON_CAPTURE_PASSED": (
        "non_capture_passed",
        "non_capture_boundary_passed",
        "non_adoption_non_currentness_passed",
    ),
    "RECEPTION_ELIGIBILITY_CLAIMS_RECOGNITION_PASSED": (
        "reception_recognition_passed",
        "source_body_reception_recognition_passed",
        "recognition_passed",
    ),
    "MUTATION_REPLAY_OR_MERGE_DETECTED": (
        "mutation_performed",
        "replay_performed",
        "merge_performed",
    ),
}

BLOCK_REASON_BY_CODE = {
    "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED": (
        "Declared reception eligibility / admissibility request is malformed."
    ),
    "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_UNREADABLE": (
        "Declared reception eligibility / admissibility request path is unreadable."
    ),
    "RECEPTION_ELIGIBILITY_QUESTION_UNDECLARED": (
        "Reception eligibility / admissibility question is undeclared."
    ),
    "RECEPTION_ELIGIBILITY_INTENT_UNSUPPORTED": (
        "Reception eligibility / admissibility intent is unsupported."
    ),
    "RECEPTION_ELIGIBILITY_REVIEW_REQUEST_EXPLICITLY_BLOCKED": (
        "Reception eligibility review was explicitly blocked by request intent."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_MISSING": (
        "Selected receiving-context role result is missing."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_UNREADABLE": (
        "Selected receiving-context role result path is unreadable."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED": (
        "Selected receiving-context role result is malformed."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_OUTCOME_MISSING": (
        "Selected receiving-context role outcome is missing."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_NOT_RECORDED": (
        "Selected receiving-context role outcome is not recorded."
    ),
    "RECEIVING_CONTEXT_ROLE_RESULT_HAS_FAILED_CHECKS": (
        "Selected receiving-context role result has failed checks."
    ),
    "IDENTITY_PRESERVATION_RESULT_MISSING": (
        "Selected identity preservation result is missing."
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
    "RECEIVING_CONTEXT_MISSING": "Receiving context is missing.",
    "RECEIVING_CONTEXT_MALFORMED": "Receiving context is malformed.",
    "RECEIVING_CONTEXT_TYPE_MISSING": "Receiving context type is missing.",
    "RECEIVING_CONTEXT_ROLE_MISSING": "Receiving-context role is missing.",
    "RECEIVING_CONTEXT_ROLE_CLASS_MISSING": (
        "Receiving-context role class is missing."
    ),
    "RECEPTION_CLASS_MISSING": "Reception class is missing.",
    "RECEPTION_PURPOSE_MISSING": "Reception purpose is missing.",
    "RECEPTION_LIMITS_MISSING": "Reception limits are missing.",
    "ELIGIBILITY_BASIS_MISSING": "Eligibility basis is missing.",
    "ADMISSIBILITY_BASIS_MISSING": "Admissibility basis is missing.",
    "REVIEW_READINESS_LIMITS_MISSING": "Review-readiness limits are missing.",
    "UNSUPPORTED_RECEPTION_ELIGIBILITY_SCOPE": (
        "Reception eligibility / admissibility scope is missing or unsupported."
    ),
    "NON_CLAIM_MISSING_OR_FLIPPED": (
        "A required eligibility / admissibility non-claim is missing or true."
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
    if not _present(value) or not isinstance(value, Mapping):
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


def _load_selected_role_result(
    request: Mapping[str, Any],
) -> tuple[Any, str | None, str | None, str | None]:
    path = request.get("selected_receiving_context_role_result_path")
    if _present(path):
        payload, error, detail = _read_json_object(str(path))
        if error == "unreadable":
            return {}, "RECEIVING_CONTEXT_ROLE_RESULT_UNREADABLE", detail, str(path)
        if error == "malformed":
            return {}, "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED", detail, str(path)
        assert payload is not None
        return payload, None, None, str(path)
    raw = request.get("selected_receiving_context_role_result")
    if isinstance(raw, Mapping):
        return _copy(dict(raw)), None, None, None
    if isinstance(raw, str) and raw:
        return {
            "selected_receiving_context_role_result_id": raw,
            "selected_receiving_context_role_result_reference": raw,
        }, None, None, None
    if _present(raw):
        return {}, "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED", None, None
    return {}, None, None, None


def _role_result_section(
    request: Mapping[str, Any],
    role_result: Any,
    load_code: str | None,
    load_detail: str | None,
    path: str | None,
) -> dict[str, Any]:
    result_map = _mapping(role_result)
    metadata = _mapping(result_map.get("source_body_reception_receiving_context_role_metadata"))
    summary = _mapping(result_map.get("source_body_reception_receiving_context_role_summary"))
    statement = _mapping(result_map.get("receiving_context_role_statement"))
    non_claims = _mapping(result_map.get("non_claims"))
    question = _mapping(result_map.get("declared_receiving_context_role_question"))
    result_id = _first(
        request.get("selected_receiving_context_role_result_id"),
        metadata.get("source_body_reception_receiving_context_role_result_id"),
        summary.get("source_body_reception_receiving_context_role_result_id"),
        question.get("receiving_context_role_request_id"),
        result_map.get("selected_receiving_context_role_result_id"),
    )
    outcome = _first(
        request.get("selected_receiving_context_role_result_outcome"),
        request.get("expected_selected_receiving_context_role_outcome"),
        result_map.get("outcome"),
        summary.get("outcome"),
    )
    failed_count = _first(
        request.get("selected_receiving_context_role_failed_check_count"),
        _failed_check_count(
            result_map,
            "receiving_context_role_checks",
            "source_body_reception_receiving_context_role_summary",
        ),
    )
    result_present = (
        _present(request.get("selected_receiving_context_role_result")) or _present(path)
    )
    selected_identity = _first(
        request.get("selected_identity_preservation_result"),
        result_map.get("selected_identity_preservation_result"),
        result_map.get("selected_source_body_reception_identity_preservation_result"),
    )
    basis = _mapping(result_map.get("receiving_context_role_basis"))
    selected_declaration = _first(
        request.get("selected_reception_request_declaration_result"),
        basis.get("selected_reception_request_declaration_result"),
        _get(selected_identity, ("selected_identity_preservation_result", "selected_reception_request_declaration_result")),
        _get(selected_identity, ("selected_reception_request_declaration_result",)),
    )
    sections = (result_map, statement, non_claims, summary)
    return {
        "selected_receiving_context_role_result": _copy(role_result),
        "selected_receiving_context_role_result_path": path,
        "selected_receiving_context_role_result_id": result_id,
        "selected_receiving_context_role_result_outcome": outcome,
        "expected_selected_receiving_context_role_outcome": request.get(
            "expected_selected_receiving_context_role_outcome",
            RECEIVING_CONTEXT_ROLE_OUTCOME,
        ),
        "selected_receiving_context_role_result_preserved": result_present
        and load_code is None,
        "selected_receiving_context_role_result_recorded": outcome
        == RECEIVING_CONTEXT_ROLE_OUTCOME,
        "selected_receiving_context_role_result_failed_check_count": failed_count,
        "selected_receiving_context_role_result_failed_check_count_zero": failed_count == 0,
        "selected_receiving_context_role_result_load_block_code": load_code,
        "selected_receiving_context_role_result_load_block_reason": load_detail,
        "selected_identity_preservation_result": _copy(selected_identity),
        "selected_identity_preservation_result_preserved": _present(selected_identity),
        "selected_reception_request_declaration_result": _copy(selected_declaration),
        "selected_reception_request_declaration_result_preserved": _present(
            selected_declaration
        ),
        "selected_source_body_surface_preserved_by_role": _first(
            statement.get("selected_source_body_surface_preserved"),
            summary.get("selected_source_body_surface_preserved"),
        ),
        "selected_source_body_surface_remains_source_by_role": _first(
            statement.get("selected_source_body_surface_remains_source"),
            summary.get("selected_source_body_surface_remains_source"),
        ),
        "selected_surface_is_not_whole_body_by_default_by_role": _first(
            statement.get("selected_surface_is_not_whole_body_by_default"),
            summary.get("selected_surface_is_not_whole_body_by_default"),
        ),
        "receiving_context_preserved_by_role": _first(
            statement.get("receiving_context_preserved"),
            summary.get("receiving_context_preserved"),
        ),
        "receiving_context_remains_context_only_by_role": _first(
            statement.get("receiving_context_remains_context_only"),
            summary.get("receiving_context_remains_context_only"),
        ),
        "receiving_context_is_not_source_by_role": _first(
            statement.get("receiving_context_is_not_source"),
            summary.get("receiving_context_is_not_source"),
        ),
        "receiving_context_is_not_authority_by_role": _first(
            statement.get("receiving_context_is_not_authority"),
            summary.get("receiving_context_is_not_authority"),
        ),
        "receiving_context_is_not_current_by_role": _first(
            statement.get("receiving_context_is_not_current"),
            summary.get("receiving_context_is_not_current"),
        ),
        "receiving_context_role_preserved_by_role": _first(
            statement.get("receiving_context_role_declared"),
            summary.get("receiving_context_role_declared"),
        ),
        "receiving_context_role_remains_bounded_by_role": _first(
            statement.get("role_is_not_permission"),
            summary.get("role_is_not_permission"),
            True if _present(result_map.get("receiving_context_role")) else None,
        ),
        "receiving_context_role_is_not_reception_by_role": _first(
            statement.get("role_is_not_reception"),
            summary.get("role_is_not_reception"),
        ),
        "receiving_context_role_is_not_authorization_by_role": _first(
            statement.get("role_is_not_authorization"),
            summary.get("role_is_not_authorization"),
        ),
        "receiving_context_role_is_not_source_receipt_by_role": _first(
            statement.get("role_is_not_source_receipt"),
            summary.get("role_is_not_source_receipt"),
        ),
        "receiving_context_role_is_not_source_authority_by_role": _first(
            statement.get("role_is_not_source_authority"),
            summary.get("role_is_not_source_authority"),
        ),
        "receiving_context_role_is_not_currentness_by_role": _first(
            statement.get("role_is_not_currentness"),
            summary.get("role_is_not_currentness"),
        ),
        "receiving_context_role_is_not_adoption_by_role": _first(
            statement.get("role_is_not_adoption"),
            summary.get("role_is_not_adoption"),
        ),
        "receiving_context_role_is_not_validation_by_role": _first(
            statement.get("role_is_not_validation"),
            summary.get("role_is_not_validation"),
        ),
        "receiving_context_role_is_not_invalidation_by_role": _first(
            statement.get("role_is_not_invalidation"),
            summary.get("role_is_not_invalidation"),
        ),
        "receiving_context_role_is_not_operation_permission_by_role": _first(
            statement.get("role_is_not_operation_permission"),
            summary.get("role_is_not_operation_permission"),
        ),
        "receiving_context_role_is_not_publication_flow_by_role": _first(
            statement.get("role_is_not_publication_flow"),
            summary.get("role_is_not_publication_flow"),
        ),
        "reception_class_preserved_by_role": _first(
            statement.get("reception_class_preserved"),
            summary.get("reception_class_preserved"),
        ),
        "reception_purpose_preserved_by_role": _first(
            statement.get("reception_purpose_preserved"),
            summary.get("reception_purpose_preserved"),
        ),
        "reception_limits_preserved_by_role": _first(
            statement.get("reception_limits_preserved"),
            summary.get("reception_limits_preserved"),
        ),
        "role_result_did_not_recognize_reception": not any(
            _any_claim_true(item, ("reception_recognized",)) for item in sections
        ),
        "role_result_did_not_authorize_reception": not any(
            _any_claim_true(item, ("reception_authorized",)) for item in sections
        ),
        "role_result_did_not_receive_source": not any(
            _any_claim_true(item, ("source_received",)) for item in sections
        ),
        "role_result_did_not_mutate_replay_or_merge": not any(
            _any_claim_true(
                item,
                ("mutation_performed", "replay_performed", "merge_performed"),
            )
            for item in sections
        ),
    }


def _role_result_map(section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(section.get("selected_receiving_context_role_result"))


def _role_basis_map(section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(_role_result_map(section).get("receiving_context_role_basis"))


def _selected_source_surface_section(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> dict[str, Any]:
    role_result = _role_result_map(role_section)
    role_surface = _mapping(role_result.get("selected_source_body_surface"))
    role_basis = _role_basis_map(role_section)
    basis_surface = _mapping(role_basis.get("selected_source_body_surface"))
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        role_surface.get("selected_source_body_surface"),
        role_surface if role_surface else None,
        basis_surface if basis_surface else None,
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
        role_surface.get("selected_source_body_surface_identifier"),
        basis_surface.get("selected_source_body_surface_identifier"),
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
        role_surface.get("selected_source_body_surface_type"),
        basis_surface.get("selected_source_body_surface_type"),
        "SOURCE_BODY_SURFACE_REFERENCE" if isinstance(raw_surface, str) else None,
    )
    surface_path = _first(
        request.get("selected_source_body_surface_path"),
        _first_key(
            payload,
            ("selected_source_body_surface_path", "source_body_surface_path", "path"),
        ),
        role_surface.get("selected_source_body_surface_path"),
        basis_surface.get("selected_source_body_surface_path"),
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
        role_surface.get("selected_source_body_surface_reference"),
        basis_surface.get("selected_source_body_surface_reference"),
        raw_surface if isinstance(raw_surface, str) else None,
    )
    identity_basis = _first(
        request.get("source_body_identity_basis"),
        _first_key(payload, ("source_body_identity_basis", "identity_basis")),
        role_surface.get("source_body_identity_basis"),
        basis_surface.get("source_body_identity_basis"),
        role_basis.get("source_body_identity_basis"),
    )
    lineage_basis = _first(
        request.get("source_body_lineage_basis"),
        _first_key(payload, ("source_body_lineage_basis", "lineage_basis")),
        role_surface.get("source_body_lineage_basis"),
        basis_surface.get("source_body_lineage_basis"),
        role_basis.get("source_body_lineage_basis"),
    )
    sections = (
        request,
        payload,
        role_surface,
        basis_surface,
        role_basis,
        _mapping(request.get("eligibility_basis")),
        _mapping(request.get("admissibility_basis")),
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
    role_section: Mapping[str, Any],
) -> dict[str, Any]:
    role_result = _role_result_map(role_section)
    role_context = _mapping(role_result.get("receiving_context"))
    role_basis = _role_basis_map(role_section)
    basis_context = _mapping(role_basis.get("receiving_context"))
    raw_context = _first(
        request.get("receiving_context"),
        role_context.get("receiving_context"),
        role_context if role_context else None,
        basis_context if basis_context else None,
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
        role_context.get("receiving_context_id"),
        basis_context.get("receiving_context_id"),
        raw_context if isinstance(raw_context, str) else None,
    )
    context_type = _first(
        request.get("receiving_context_type"),
        _first_key(payload, ("receiving_context_type", "context_type", "type")),
        role_context.get("receiving_context_type"),
        basis_context.get("receiving_context_type"),
        role_basis.get("receiving_context_type"),
        "RECEIVING_CONTEXT" if isinstance(raw_context, str) else None,
    )
    sections = (
        request,
        payload,
        role_context,
        basis_context,
        role_basis,
        _mapping(request.get("eligibility_basis")),
        _mapping(request.get("admissibility_basis")),
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


def _role_statement(role_section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(_role_result_map(role_section).get("receiving_context_role_statement"))


def _role_summary(role_section: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(
        _role_result_map(role_section).get("source_body_reception_receiving_context_role_summary")
    )


def _receiving_context_role_payload(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> Any:
    role_result = _role_result_map(role_section)
    role_payload = _mapping(role_result.get("receiving_context_role"))
    role_basis = _role_basis_map(role_section)
    return _first(
        request.get("selected_receiving_context_role"),
        role_payload.get("declared_receiving_context_role"),
        role_payload if role_payload else None,
        role_basis.get("declared_receiving_context_role"),
    )


def _receiving_context_role_class_value(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> Any:
    role_result = _role_result_map(role_section)
    role_payload = _mapping(role_result.get("receiving_context_role"))
    role_basis = _role_basis_map(role_section)
    summary = _role_summary(role_section)
    return _first(
        request.get("receiving_context_role_class"),
        role_payload.get("receiving_context_role_class"),
        role_basis.get("receiving_context_role_class"),
        summary.get("receiving_context_role_class"),
    )


def _receiving_context_role_limits_value(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
) -> Any:
    role_result = _role_result_map(role_section)
    role_payload = _mapping(role_result.get("receiving_context_role"))
    role_basis = _role_basis_map(role_section)
    return _first(
        request.get("receiving_context_role_limits"),
        role_payload.get("receiving_context_role_limits"),
        role_basis.get("receiving_context_role_limits"),
    )


def _reception_class_value(request: Mapping[str, Any], role_section: Mapping[str, Any]) -> Any:
    role_basis = _role_basis_map(role_section)
    summary = _role_summary(role_section)
    return _first(
        request.get("reception_class"),
        role_basis.get("reception_class"),
        summary.get("reception_class"),
    )


def _reception_purpose_value(request: Mapping[str, Any], role_section: Mapping[str, Any]) -> Any:
    role_basis = _role_basis_map(role_section)
    summary = _role_summary(role_section)
    return _first(
        request.get("reception_purpose"),
        role_basis.get("reception_purpose"),
        summary.get("reception_purpose"),
    )


def _reception_limits_value(request: Mapping[str, Any], role_section: Mapping[str, Any]) -> Any:
    role_basis = _role_basis_map(role_section)
    return _first(request.get("reception_limits"), role_basis.get("reception_limits"))


def _review_readiness_limits_value(request: Mapping[str, Any]) -> Any:
    return request.get("review_readiness_limits")


def _declared_non_claims(request: Mapping[str, Any]) -> Mapping[str, Any]:
    return _mapping(request.get("declared_non_claims"))


def _declared_non_claims_valid(request: Mapping[str, Any]) -> bool:
    non_claims = _declared_non_claims(request)
    if not non_claims:
        return False
    return all(key in non_claims and non_claims.get(key) is False for key in REQUIRED_NON_CLAIMS)


def _scope_values(request: Mapping[str, Any]) -> tuple[list[str], list[str]]:
    raw_scope = request.get("eligibility_scope")
    if isinstance(raw_scope, str):
        values = [raw_scope]
    elif isinstance(raw_scope, Mapping):
        selected = _first(
            raw_scope.get("selected_eligibility_scope_values"),
            raw_scope.get("eligibility_scope_values"),
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
        value for value in values if value not in SUPPORTED_RECEPTION_ELIGIBILITY_SCOPE
    ]
    return values, unsupported


def _collapse_sections(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> list[Mapping[str, Any]]:
    role_result = _role_result_map(role_section)
    role_basis = _role_basis_map(role_section)
    return [
        request,
        _mapping(request.get("eligibility_basis")),
        _mapping(request.get("admissibility_basis")),
        _mapping(request.get("eligibility_scope")),
        _mapping(request.get("review_readiness_limits")),
        _mapping(request.get("declared_non_claims")),
        _mapping(request.get("additional_basis_context")),
        _mapping(request.get("not_eligible_basis")),
        role_section,
        role_result,
        _mapping(role_result.get("non_claims")),
        _mapping(role_result.get("receiving_context_role_statement")),
        _mapping(role_result.get("receiving_context_role_non_meaning")),
        _mapping(role_result.get("selected_source_body_surface")),
        _mapping(role_result.get("receiving_context")),
        _mapping(role_result.get("receiving_context_role")),
        role_basis,
        selected_surface,
        _mapping(selected_surface.get("selected_source_body_surface")),
        receiving_context,
        _mapping(receiving_context.get("receiving_context")),
    ]


def _collapse_code(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> str | None:
    for code, fields in COLLAPSE_FIELDS.items():
        for section in _collapse_sections(
            request, role_section, selected_surface, receiving_context
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
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> list[dict[str, Any]]:
    role_load_code = role_section.get("selected_receiving_context_role_result_load_block_code")
    raw_role_result = request.get("selected_receiving_context_role_result")
    role_shape_valid = (
        not _present(raw_role_result) or isinstance(raw_role_result, (Mapping, str))
    )
    raw_surface = _first(
        request.get("selected_source_body_surface"),
        _get(
            role_section,
            ("selected_receiving_context_role_result", "selected_source_body_surface"),
        ),
    )
    raw_context = _first(
        request.get("receiving_context"),
        _get(role_section, ("selected_receiving_context_role_result", "receiving_context")),
    )
    surface_shape_valid = (
        not _present(raw_surface) or isinstance(raw_surface, (Mapping, str))
    )
    context_shape_valid = (
        not _present(raw_context) or isinstance(raw_context, (Mapping, str))
    )
    role_payload = _receiving_context_role_payload(request, role_section)
    role_class = _receiving_context_role_class_value(request, role_section)
    role_limits = _receiving_context_role_limits_value(request, role_section)
    reception_class = _reception_class_value(request, role_section)
    reception_purpose = _reception_purpose_value(request, role_section)
    reception_limits = _reception_limits_value(request, role_section)
    eligibility_basis = request.get("eligibility_basis")
    admissibility_basis = request.get("admissibility_basis")
    review_limits = _review_readiness_limits_value(request)
    scope_values, unsupported_scope = _scope_values(request)
    collapse_code = _collapse_code(
        request, role_section, selected_surface, receiving_context
    )
    role_statement = _role_statement(role_section)
    role_summary = _role_summary(role_section)
    role_authority_currentness_adoption_validation_invalidation = all(
        _first(
            role_statement.get(key),
            role_summary.get(key),
        )
        is True
        for key in (
            "role_is_not_source_authority",
            "role_is_not_currentness",
            "role_is_not_adoption",
            "role_is_not_validation",
            "role_is_not_invalidation",
        )
    )
    checks = [
        _check(
            "eligibility / admissibility question declared",
            _present(request.get("eligibility_question")),
            "declared eligibility / admissibility question",
            request.get("eligibility_question"),
            "RECEPTION_ELIGIBILITY_QUESTION_UNDECLARED",
        ),
        _check(
            "eligibility / admissibility intent supported",
            request.get("eligibility_intent", INTENT_RECORD) in SUPPORTED_INTENTS,
            sorted(SUPPORTED_INTENTS),
            request.get("eligibility_intent", INTENT_RECORD),
            "RECEPTION_ELIGIBILITY_INTENT_UNSUPPORTED",
        ),
        _check(
            "selected receiving-context role result present",
            role_section.get("selected_receiving_context_role_result_preserved") is True,
            "selected source-body reception receiving-context role result",
            role_section.get("selected_receiving_context_role_result_id"),
            role_load_code or "RECEIVING_CONTEXT_ROLE_RESULT_MISSING",
        ),
        _check(
            "selected receiving-context role result well formed",
            role_shape_valid and role_load_code is None,
            "mapping, reference string, or readable JSON object",
            role_load_code or type(raw_role_result).__name__,
            role_load_code or "RECEIVING_CONTEXT_ROLE_RESULT_MALFORMED",
        ),
        _check(
            "selected receiving-context role outcome declared",
            _present(role_section.get("selected_receiving_context_role_result_outcome")),
            "selected receiving-context role outcome",
            role_section.get("selected_receiving_context_role_result_outcome"),
            "RECEIVING_CONTEXT_ROLE_RESULT_OUTCOME_MISSING",
        ),
        _check(
            "selected receiving-context role outcome recorded",
            role_section.get("selected_receiving_context_role_result_recorded") is True,
            RECEIVING_CONTEXT_ROLE_OUTCOME,
            role_section.get("selected_receiving_context_role_result_outcome"),
            "RECEIVING_CONTEXT_ROLE_RESULT_NOT_RECORDED",
        ),
        _check(
            "selected receiving-context role failed check count zero",
            role_section.get("selected_receiving_context_role_result_failed_check_count_zero")
            is True,
            0,
            role_section.get("selected_receiving_context_role_result_failed_check_count"),
            "RECEIVING_CONTEXT_ROLE_RESULT_HAS_FAILED_CHECKS",
        ),
        _check(
            "selected identity preservation result preserved",
            role_section.get("selected_identity_preservation_result_preserved") is True,
            "selected identity preservation result",
            role_section.get("selected_identity_preservation_result"),
            "IDENTITY_PRESERVATION_RESULT_MISSING",
        ),
        _check(
            "selected request declaration result preserved",
            role_section.get("selected_reception_request_declaration_result_preserved")
            is True,
            "selected source-body reception request declaration result",
            role_section.get("selected_reception_request_declaration_result"),
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
            "selected source-body surface remains source",
            selected_surface.get("selected_source_body_surface_remains_source") is True,
            True,
            selected_surface.get("selected_source_body_surface_remains_source"),
            collapse_code or "RECEPTION_ELIGIBILITY_REPLACES_SOURCE",
        ),
        _check(
            "selected surface is not whole body by default",
            selected_surface.get("selected_surface_is_not_whole_body_by_default") is True,
            True,
            selected_surface.get("selected_surface_is_not_whole_body_by_default"),
            collapse_code or "RECEPTION_ELIGIBILITY_CREATES_CURRENTNESS",
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
            collapse_code or "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not source",
            receiving_context.get("receiving_context_is_not_source") is True,
            True,
            receiving_context.get("receiving_context_is_not_source"),
            collapse_code or "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_SOURCE",
        ),
        _check(
            "receiving context is not authority",
            receiving_context.get("receiving_context_is_not_authority") is True,
            True,
            receiving_context.get("receiving_context_is_not_authority"),
            collapse_code or "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_AUTHORITY",
        ),
        _check(
            "receiving context is not current",
            receiving_context.get("receiving_context_is_not_current") is True,
            True,
            receiving_context.get("receiving_context_is_not_current"),
            collapse_code or "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_CURRENT",
        ),
        _check(
            "receiving-context role preserved",
            _present(role_payload),
            "selected receiving-context role",
            role_payload,
            "RECEIVING_CONTEXT_ROLE_MISSING",
        ),
        _check(
            "receiving-context role class preserved",
            _present(role_class),
            "receiving-context role class",
            role_class,
            "RECEIVING_CONTEXT_ROLE_CLASS_MISSING",
        ),
        _check(
            "receiving-context role remains bounded",
            _present(role_limits),
            "bounded receiving-context role limits",
            role_limits,
            "REVIEW_READINESS_LIMITS_MISSING",
        ),
        _check(
            "receiving-context role is not reception",
            _first(
                role_statement.get("role_is_not_reception"),
                role_summary.get("role_is_not_reception"),
            )
            is True,
            True,
            _first(
                role_statement.get("role_is_not_reception"),
                role_summary.get("role_is_not_reception"),
            ),
            collapse_code or "RECEPTION_ELIGIBILITY_RECOGNIZES_RECEPTION",
        ),
        _check(
            "receiving-context role is not authorization",
            _first(
                role_statement.get("role_is_not_authorization"),
                role_summary.get("role_is_not_authorization"),
            )
            is True,
            True,
            _first(
                role_statement.get("role_is_not_authorization"),
                role_summary.get("role_is_not_authorization"),
            ),
            collapse_code or "RECEPTION_ELIGIBILITY_AUTHORIZES_RECEPTION",
        ),
        _check(
            "receiving-context role is not source receipt",
            _first(
                role_statement.get("role_is_not_source_receipt"),
                role_summary.get("role_is_not_source_receipt"),
            )
            is True,
            True,
            _first(
                role_statement.get("role_is_not_source_receipt"),
                role_summary.get("role_is_not_source_receipt"),
            ),
            collapse_code or "RECEPTION_ELIGIBILITY_RECEIVES_SOURCE",
        ),
        _check(
            "receiving-context role is not authority/currentness/adoption/validation/invalidation",
            role_authority_currentness_adoption_validation_invalidation,
            True,
            role_authority_currentness_adoption_validation_invalidation,
            collapse_code or "RECEPTION_ELIGIBILITY_CREATES_AUTHORITY",
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
            "eligibility basis declared",
            _present(eligibility_basis),
            "eligibility basis",
            eligibility_basis,
            "ELIGIBILITY_BASIS_MISSING",
        ),
        _check(
            "admissibility basis declared",
            _present(admissibility_basis),
            "admissibility basis",
            admissibility_basis,
            "ADMISSIBILITY_BASIS_MISSING",
        ),
        _check(
            "review-readiness limits declared",
            _present(review_limits),
            "review-readiness limits",
            review_limits,
            "REVIEW_READINESS_LIMITS_MISSING",
        ),
        _check(
            "eligibility / admissibility scope supported",
            bool(scope_values) and not unsupported_scope,
            list(SUPPORTED_RECEPTION_ELIGIBILITY_SCOPE),
            scope_values if scope_values else "missing",
            "UNSUPPORTED_RECEPTION_ELIGIBILITY_SCOPE",
        ),
    ]
    false_checks = (
        ("eligibility is not reception", "RECEPTION_ELIGIBILITY_RECOGNIZES_RECEPTION"),
        ("admissibility is not authorization", "RECEPTION_ELIGIBILITY_AUTHORIZES_RECEPTION"),
        ("eligibility does not receive source", "RECEPTION_ELIGIBILITY_RECEIVES_SOURCE"),
        ("eligibility does not create governance", "RECEPTION_ELIGIBILITY_CREATES_GOVERNANCE"),
        ("eligibility does not treat receiving context as source", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_SOURCE"),
        ("eligibility does not treat receiving context as authority", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_AUTHORITY"),
        ("eligibility does not treat receiving context as current", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_CURRENT"),
        ("eligibility does not treat receiving context as receiver", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_RECEIVER"),
        ("eligibility does not treat receiving context as adopter", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_ADOPTER"),
        ("eligibility does not treat receiving context as validator", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_VALIDATOR"),
        ("eligibility does not treat receiving context as invalidator", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_INVALIDATOR"),
        ("eligibility does not treat receiving context as operator", "RECEPTION_ELIGIBILITY_TREATS_CONTEXT_AS_OPERATOR"),
        ("eligibility does not create validation", "RECEPTION_ELIGIBILITY_VALIDATES_SOURCE"),
        ("eligibility does not create invalidation", "RECEPTION_ELIGIBILITY_INVALIDATES_SOURCE"),
        ("eligibility does not replace source", "RECEPTION_ELIGIBILITY_REPLACES_SOURCE"),
        ("eligibility does not create adoption", "RECEPTION_ELIGIBILITY_CREATES_ADOPTION"),
        ("eligibility does not create authority", "RECEPTION_ELIGIBILITY_CREATES_AUTHORITY"),
        ("eligibility does not create currentness", "RECEPTION_ELIGIBILITY_CREATES_CURRENTNESS"),
        ("eligibility does not create standing", "RECEPTION_ELIGIBILITY_CREATES_STANDING"),
        ("eligibility does not create standing propagation", "RECEPTION_ELIGIBILITY_CREATES_STANDING_PROPAGATION"),
        ("eligibility does not create vessel relation", "RECEPTION_ELIGIBILITY_CREATES_VESSEL_RELATION"),
        ("eligibility does not create derivative relation", "RECEPTION_ELIGIBILITY_CREATES_DERIVATIVE_RELATION"),
        ("eligibility does not create operation permission", "RECEPTION_ELIGIBILITY_CREATES_OPERATION_PERMISSION"),
        ("eligibility does not create public readiness", "RECEPTION_ELIGIBILITY_CREATES_PUBLIC_READINESS"),
        ("eligibility does not claim final completion", "RECEPTION_ELIGIBILITY_CLAIMS_FINAL_COMPLETION"),
        ("eligibility does not authorize follow-on work", "RECEPTION_ELIGIBILITY_AUTHORIZES_FOLLOW_ON_WORK"),
        ("eligibility does not authorize continuation", "RECEPTION_ELIGIBILITY_AUTHORIZES_CONTINUATION"),
        ("eligibility does not create publication flow", "RECEPTION_ELIGIBILITY_OPENS_PUBLICATION_FLOW"),
        ("non-capture remains future work", "RECEPTION_ELIGIBILITY_CLAIMS_NON_CAPTURE_PASSED"),
        ("recognition remains future work", "RECEPTION_ELIGIBILITY_CLAIMS_RECOGNITION_PASSED"),
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
            "all required eligibility / admissibility non-claims false",
            _declared_non_claims(request),
            collapse_code or "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    if request.get("eligibility_intent", INTENT_RECORD) == INTENT_BLOCK:
        checks.append(
            _check(
                "eligibility review explicitly unblocked",
                False,
                "review not explicitly blocked",
                INTENT_BLOCK,
                "RECEPTION_ELIGIBILITY_REVIEW_REQUEST_EXPLICITLY_BLOCKED",
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


def _metadata(request: Mapping[str, Any], role_section: Mapping[str, Any]) -> dict[str, str]:
    basis = _first(
        request.get("eligibility_request_id"),
        role_section.get("selected_receiving_context_role_result_id"),
        RESULT_ID_PREFIX,
    )
    return {
        "source_body_reception_eligibility_result_id": (
            f"{RESULT_ID_PREFIX}__{_safe_component(basis)}"
        ),
        "source_body_reception_eligibility_result_type": RESULT_TYPE,
        "source_body_reception_eligibility_result_version": RESULT_VERSION,
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
    }


def _default_non_claims(outcome: str) -> dict[str, bool]:
    non_claims = {key: False for key in REQUIRED_NON_CLAIMS}
    non_claims["source_body_reception_eligible_admissible_for_review"] = (
        outcome == OUTCOME_ELIGIBLE_ADMISSIBLE
    )
    return non_claims


def _declared_question_section(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "eligibility_request_id": request.get("eligibility_request_id"),
        "eligibility_question": request.get("eligibility_question"),
        "eligibility_intent": request.get("eligibility_intent", INTENT_RECORD),
        "declared_eligibility_request_path": request.get(
            "declared_eligibility_request_path"
        ),
        "requested_eligibility_outcome": request.get(
            "requested_eligibility_outcome", OUTCOME_ELIGIBLE_ADMISSIBLE
        ),
        "selected_receiving_context_role_result_id": role_section.get(
            "selected_receiving_context_role_result_id"
        ),
        "selected_receiving_context_role_result_outcome": role_section.get(
            "selected_receiving_context_role_result_outcome"
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
        "receiving_context_role_class": _receiving_context_role_class_value(
            request, role_section
        ),
        "reception_class": _reception_class_value(request, role_section),
        "reception_purpose": _reception_purpose_value(request, role_section),
        "eligibility_is_not_reception": True,
        "admissibility_is_not_authorization": True,
        "eligibility_does_not_receive_source": True,
        "eligibility_does_not_create_source_authority": True,
        "eligibility_does_not_create_currentness": True,
        "eligibility_does_not_create_governance": True,
        "eligibility_does_not_create_operation_permission": True,
        "eligibility_does_not_open_publication_flow": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
    }


def _eligibility_basis_section(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
) -> dict[str, Any]:
    role_basis = _role_basis_map(role_section)
    return {
        "declared_eligibility_basis": _copy(request.get("eligibility_basis")),
        "selected_receiving_context_role_result": _copy(
            role_section.get("selected_receiving_context_role_result")
        ),
        "selected_identity_preservation_result": _copy(
            role_section.get("selected_identity_preservation_result")
        ),
        "selected_request_declaration_result": _copy(
            role_section.get("selected_reception_request_declaration_result")
        ),
        "selected_source_body_surface": _copy(selected_surface),
        "source_body_identity_basis": _copy(selected_surface.get("source_body_identity_basis")),
        "source_body_lineage_basis": _copy(selected_surface.get("source_body_lineage_basis")),
        "receiving_context": _copy(receiving_context),
        "receiving_context_type": receiving_context.get("receiving_context_type"),
        "reception_class": _copy(_reception_class_value(request, role_section)),
        "reception_purpose": _copy(_reception_purpose_value(request, role_section)),
        "reception_limits": _copy(_reception_limits_value(request, role_section)),
        "selected_receiving_context_role": _copy(
            _receiving_context_role_payload(request, role_section)
        ),
        "receiving_context_role_class": _copy(
            _receiving_context_role_class_value(request, role_section)
        ),
        "receiving_context_role_limits": _copy(
            _receiving_context_role_limits_value(request, role_section)
        ),
        "receiving_context_role_basis": _copy(role_basis),
        "eligible_for_later_reception_review_only": True,
        "eligibility_is_not_reception": True,
        "eligibility_is_not_recognition": True,
        "eligibility_is_not_source_receipt": True,
        "eligibility_does_not_decide_non_capture": True,
        "eligibility_does_not_decide_recognition": True,
        "source_body_surface_remains_source": selected_surface.get(
            "selected_source_body_surface_remains_source"
        )
        is True,
        "receiving_context_remains_context_only": receiving_context.get(
            "receiving_context_remains_context_only"
        )
        is True,
    }


def _admissibility_basis_section(request: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "declared_admissibility_basis": _copy(request.get("admissibility_basis")),
        "admissible_for_later_reception_review_only": True,
        "admissibility_is_not_authorization": True,
        "admissibility_does_not_authorize_reception": True,
        "admissibility_does_not_receive_source": True,
        "admissibility_does_not_create_adoption": True,
        "admissibility_does_not_create_authority": True,
        "admissibility_does_not_create_currentness": True,
        "admissibility_does_not_create_validation": True,
        "admissibility_does_not_create_invalidation": True,
        "admissibility_does_not_create_operation_permission": True,
        "admissibility_does_not_create_governance": True,
        "admissibility_does_not_create_publication_flow": True,
        "admissibility_does_not_create_public_readiness": True,
        "admissibility_does_not_claim_final_completion": True,
        "admissibility_does_not_authorize_continuation": True,
        "admissibility_does_not_authorize_follow_on_work": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
    }


def _eligibility_scope_section(request: Mapping[str, Any]) -> dict[str, Any]:
    values, unsupported = _scope_values(request)
    return {
        "selected_eligibility_scope_values": values,
        "unsupported_eligibility_scope_values": unsupported,
        "all_selected_scope_values_supported": bool(values) and not unsupported,
        "supported_eligibility_scope_values": list(SUPPORTED_RECEPTION_ELIGIBILITY_SCOPE),
        "eligible_for_reception_review_only": True,
        "admissible_for_reception_review_only": True,
        "eligibility_is_not_reception": True,
        "admissibility_is_not_authorization": True,
        "eligibility_is_not_source_receipt": True,
        "eligibility_is_not_adoption": True,
        "eligibility_is_not_authority": True,
        "eligibility_is_not_currentness": True,
        "eligibility_is_not_validation": True,
        "eligibility_is_not_invalidation": True,
        "eligibility_is_not_operation_permission": True,
        "eligibility_is_not_publication_flow": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
    }


def _eligibility_statement(
    outcome: str,
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    eligible = outcome == OUTCOME_ELIGIBLE_ADMISSIBLE
    role_statement = _role_statement(role_section)
    role_summary = _role_summary(role_section)
    statement = {
        "source_body_reception_eligible_admissible_for_review": eligible,
        "selected_receiving_context_role_result_preserved": role_section.get(
            "selected_receiving_context_role_result_preserved"
        )
        is True,
        "selected_receiving_context_role_result_recorded": role_section.get(
            "selected_receiving_context_role_result_recorded"
        )
        is True,
        "selected_receiving_context_role_result_failed_check_count_zero": role_section.get(
            "selected_receiving_context_role_result_failed_check_count_zero"
        )
        is True,
        "selected_identity_preservation_result_preserved": role_section.get(
            "selected_identity_preservation_result_preserved"
        )
        is True,
        "selected_reception_request_declaration_result_preserved": role_section.get(
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
        "receiving_context_role_preserved": _present(
            _receiving_context_role_payload(request, role_section)
        ),
        "receiving_context_role_remains_bounded": _present(
            _receiving_context_role_limits_value(request, role_section)
        ),
        "role_is_not_reception": _first(
            role_statement.get("role_is_not_reception"),
            role_summary.get("role_is_not_reception"),
        )
        is True,
        "role_is_not_authorization": _first(
            role_statement.get("role_is_not_authorization"),
            role_summary.get("role_is_not_authorization"),
        )
        is True,
        "role_is_not_source_receipt": _first(
            role_statement.get("role_is_not_source_receipt"),
            role_summary.get("role_is_not_source_receipt"),
        )
        is True,
        "role_is_not_source_authority": _first(
            role_statement.get("role_is_not_source_authority"),
            role_summary.get("role_is_not_source_authority"),
        )
        is True,
        "role_is_not_currentness": _first(
            role_statement.get("role_is_not_currentness"),
            role_summary.get("role_is_not_currentness"),
        )
        is True,
        "role_is_not_adoption": _first(
            role_statement.get("role_is_not_adoption"),
            role_summary.get("role_is_not_adoption"),
        )
        is True,
        "role_is_not_validation": _first(
            role_statement.get("role_is_not_validation"),
            role_summary.get("role_is_not_validation"),
        )
        is True,
        "role_is_not_invalidation": _first(
            role_statement.get("role_is_not_invalidation"),
            role_summary.get("role_is_not_invalidation"),
        )
        is True,
        "role_is_not_authority_currentness_adoption_validation_invalidation": all(
            _first(role_statement.get(key), role_summary.get(key)) is True
            for key in (
                "role_is_not_source_authority",
                "role_is_not_currentness",
                "role_is_not_adoption",
                "role_is_not_validation",
                "role_is_not_invalidation",
            )
        ),
        "reception_class_preserved": _present(_reception_class_value(request, role_section)),
        "reception_purpose_preserved": _present(_reception_purpose_value(request, role_section)),
        "reception_limits_preserved": _present(_reception_limits_value(request, role_section)),
        "eligibility_basis_declared": _present(request.get("eligibility_basis")),
        "admissibility_basis_declared": _present(request.get("admissibility_basis")),
        "review_readiness_limits_declared": _present(
            _review_readiness_limits_value(request)
        ),
        "eligible_for_reception_review_only": True,
        "admissible_for_reception_review_only": True,
        "eligibility_is_not_reception": True,
        "admissibility_is_not_authorization": True,
        "eligibility_does_not_receive_source": True,
        "non_capture_requires_separate_boundary": True,
        "recognition_requires_separate_boundary": True,
        "not_eligible_reason": request.get("not_eligible_basis"),
    }
    for key in REQUIRED_NON_CLAIMS:
        statement[key] = False
    return statement


def _eligibility_non_meaning() -> dict[str, bool]:
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
        "receiving_context_became_receiver": True,
        "receiving_context_became_adopter": True,
        "receiving_context_became_validator": True,
        "receiving_context_became_invalidator": True,
        "receiving_context_became_operator": True,
        "receiving_context_governance_created": True,
        "standing_created": True,
        "standing_propagated": True,
        "vessel_relation_created": True,
        "derivative_relation_created": True,
        "operation_permission_created": True,
        "non_capture_passed": True,
        "reception_recognition_passed": True,
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
        "missing_basis_does_not_authorize_continuation": True,
        "missing_basis_does_not_authorize_follow_on_work": True,
        "missing_basis_does_not_decide_non_capture": True,
        "missing_basis_does_not_decide_recognition": True,
    }


def _not_eligible_basis(
    request: Mapping[str, Any],
    outcome: str,
    checks: Sequence[Mapping[str, Any]],
) -> dict[str, Any]:
    not_eligible = outcome == OUTCOME_NOT_ELIGIBLE
    failed_checks = [
        _copy(dict(check))
        for check in checks
        if isinstance(check, Mapping) and check.get("passed") is not True
    ]
    return {
        "source_body_reception_not_eligible_or_admissible": not_eligible,
        "not_eligible_basis": _copy(request.get("not_eligible_basis"))
        if not_eligible
        else {},
        "failed_eligibility_checks": failed_checks if not_eligible else [],
        "not_eligible_does_not_mutate": True,
        "not_eligible_does_not_repair": True,
        "not_eligible_does_not_authorize": True,
        "not_eligible_does_not_receive_source": True,
        "not_eligible_does_not_replace_source": True,
        "not_eligible_does_not_validate_source": True,
        "not_eligible_does_not_invalidate_source": True,
        "not_eligible_does_not_create_currentness": True,
        "not_eligible_does_not_recognize_reception": True,
    }


def _what_remains_open() -> dict[str, bool]:
    return {
        "source_body_reception_eligibility_admissibility_test": True,
        "source_body_reception_eligibility_admissibility_live_artifact": True,
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


def build_source_body_reception_eligibility_admissibility_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("eligibility_checks")
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
    question = _mapping(result.get("declared_eligibility_question"))
    role = _mapping(result.get("selected_receiving_context_role_result"))
    surface = _mapping(result.get("selected_source_body_surface"))
    context = _mapping(result.get("receiving_context"))
    eligibility = _mapping(result.get("eligibility_basis"))
    statement = _mapping(result.get("eligibility_statement"))
    non_claims = _mapping(result.get("non_claims"))
    block = _mapping(result.get("block"))
    outcome = result.get("outcome")
    return {
        "outcome": outcome,
        "block_code": block.get("block_code"),
        "block_reason": block.get("block_reason"),
        "eligibility_request_id": question.get("eligibility_request_id"),
        "eligibility_question": question.get("eligibility_question"),
        "eligibility_intent": question.get("eligibility_intent"),
        "selected_receiving_context_role_result_id": role.get(
            "selected_receiving_context_role_result_id"
        ),
        "selected_receiving_context_role_result_outcome": role.get(
            "selected_receiving_context_role_result_outcome"
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
        "receiving_context_role_class": eligibility.get("receiving_context_role_class"),
        "reception_class": eligibility.get("reception_class"),
        "reception_purpose": eligibility.get("reception_purpose"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "eligible_admissible": outcome == OUTCOME_ELIGIBLE_ADMISSIBLE,
        "source_body_reception_eligible_admissible_for_review": statement.get(
            "source_body_reception_eligible_admissible_for_review"
        )
        is True,
        "not_eligible_or_admissible": outcome == OUTCOME_NOT_ELIGIBLE,
        "requires_additional_basis": outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS,
        "selected_receiving_context_role_result_preserved": statement.get(
            "selected_receiving_context_role_result_preserved"
        ),
        "selected_receiving_context_role_result_recorded": statement.get(
            "selected_receiving_context_role_result_recorded"
        ),
        "selected_receiving_context_role_result_failed_check_count_zero": statement.get(
            "selected_receiving_context_role_result_failed_check_count_zero"
        ),
        "selected_identity_preservation_result_preserved": statement.get(
            "selected_identity_preservation_result_preserved"
        ),
        "selected_request_declaration_result_preserved": statement.get(
            "selected_reception_request_declaration_result_preserved"
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
        "receiving_context_role_preserved": statement.get(
            "receiving_context_role_preserved"
        ),
        "receiving_context_role_remains_bounded": statement.get(
            "receiving_context_role_remains_bounded"
        ),
        "role_is_not_reception": statement.get("role_is_not_reception"),
        "role_is_not_authorization": statement.get("role_is_not_authorization"),
        "role_is_not_source_receipt": statement.get("role_is_not_source_receipt"),
        "role_is_not_source_authority": statement.get("role_is_not_source_authority"),
        "role_is_not_currentness": statement.get("role_is_not_currentness"),
        "role_is_not_adoption": statement.get("role_is_not_adoption"),
        "role_is_not_validation": statement.get("role_is_not_validation"),
        "role_is_not_invalidation": statement.get("role_is_not_invalidation"),
        "role_is_not_authority_currentness_adoption_validation_invalidation": statement.get(
            "role_is_not_authority_currentness_adoption_validation_invalidation"
        ),
        "reception_class_preserved": statement.get("reception_class_preserved"),
        "reception_purpose_preserved": statement.get("reception_purpose_preserved"),
        "reception_limits_preserved": statement.get("reception_limits_preserved"),
        "eligibility_basis_declared": statement.get("eligibility_basis_declared"),
        "admissibility_basis_declared": statement.get("admissibility_basis_declared"),
        "review_readiness_limits_declared": statement.get(
            "review_readiness_limits_declared"
        ),
        "eligible_for_review_only": statement.get("eligible_for_reception_review_only"),
        "admissible_for_review_only": statement.get(
            "admissible_for_reception_review_only"
        ),
        "eligibility_is_not_reception": statement.get("eligibility_is_not_reception"),
        "admissibility_is_not_authorization": statement.get(
            "admissibility_is_not_authorization"
        ),
        "no_source_received": non_claims.get("source_received") is False,
        "non_capture_future": statement.get("non_capture_requires_separate_boundary"),
        "recognition_future": statement.get("recognition_requires_separate_boundary"),
        "no_reception_recognized": non_claims.get("reception_recognized") is False,
        "no_reception_authorized": non_claims.get("reception_authorized") is False,
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
        "no_governance": non_claims.get("receiving_context_governance_created") is False,
        "no_publication_flow": non_claims.get("publication_flow_opened") is False,
        "no_public_readiness": non_claims.get("public_launch_readiness_created") is False,
        "no_final_completion": non_claims.get("final_completion_claimed") is False,
        "no_follow_on_work": non_claims.get("follow_on_work_authorized") is False,
        "key_non_claims": _copy(non_claims),
    }


def _result(
    request: Mapping[str, Any],
    role_section: Mapping[str, Any],
    selected_surface: Mapping[str, Any],
    receiving_context: Mapping[str, Any],
    checks: Sequence[Mapping[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "block_code": block_code,
        "block_reason": _block_reason(block_code, request.get("block_reason")),
    }
    result = {
        "source_body_reception_eligibility_metadata": _metadata(request, role_section),
        "declared_eligibility_question": _declared_question_section(
            request, role_section, selected_surface, receiving_context
        ),
        "selected_receiving_context_role_result": _copy(role_section),
        "selected_source_body_surface": _copy(selected_surface),
        "receiving_context": _copy(receiving_context),
        "eligibility_basis": _eligibility_basis_section(
            request, role_section, selected_surface, receiving_context
        ),
        "admissibility_basis": _admissibility_basis_section(request),
        "eligibility_scope": _eligibility_scope_section(request),
        "eligibility_checks": [_copy(dict(check)) for check in checks],
        "eligibility_statement": _eligibility_statement(
            outcome, role_section, selected_surface, receiving_context, request
        ),
        "eligibility_non_meaning": _eligibility_non_meaning(),
        "additional_basis_required": _additional_basis_required(request, outcome),
        "not_eligible_basis": _not_eligible_basis(request, outcome, checks),
        "what_remains_open": _what_remains_open(),
        "non_claims": _default_non_claims(outcome),
        "outcome": outcome,
        "block": block,
    }
    result["source_body_reception_eligibility_summary"] = (
        build_source_body_reception_eligibility_admissibility_summary(result)
    )
    return result


def _minimal_blocked_result(
    request: Mapping[str, Any],
    block_code: str,
    block_reason: str | None = None,
) -> dict[str, Any]:
    safe_request = _copy(dict(request))
    if block_reason is not None:
        safe_request["block_reason"] = block_reason
    role_section = {
        "selected_receiving_context_role_result": {},
        "selected_receiving_context_role_result_path": safe_request.get(
            "selected_receiving_context_role_result_path"
        ),
        "selected_receiving_context_role_result_id": safe_request.get(
            "selected_receiving_context_role_result_id"
        ),
        "selected_receiving_context_role_result_outcome": safe_request.get(
            "selected_receiving_context_role_result_outcome"
        ),
        "selected_receiving_context_role_result_preserved": False,
        "selected_receiving_context_role_result_recorded": False,
        "selected_receiving_context_role_result_failed_check_count": None,
        "selected_receiving_context_role_result_failed_check_count_zero": False,
        "selected_receiving_context_role_result_load_block_code": None,
        "selected_receiving_context_role_result_load_block_reason": None,
        "selected_identity_preservation_result": safe_request.get(
            "selected_identity_preservation_result"
        ),
        "selected_identity_preservation_result_preserved": _present(
            safe_request.get("selected_identity_preservation_result")
        ),
        "selected_reception_request_declaration_result": safe_request.get(
            "selected_reception_request_declaration_result"
        ),
        "selected_reception_request_declaration_result_preserved": _present(
            safe_request.get("selected_reception_request_declaration_result")
        ),
    }
    selected_surface = _selected_source_surface_section(safe_request, role_section)
    receiving_context = _receiving_context_section(safe_request, role_section)
    checks = [
        _check(
            "eligibility / admissibility review blocked",
            False,
            "bounded eligibility / admissibility request",
            block_code,
            block_code,
        )
    ]
    return _result(
        safe_request,
        role_section,
        selected_surface,
        receiving_context,
        checks,
        OUTCOME_BLOCKED,
        block_code,
    )


def resolve_source_body_reception_eligibility_admissibility_boundary(
    declared_eligibility_request: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_eligibility_request is None:
        request: dict[str, Any] = {}
    elif isinstance(declared_eligibility_request, Mapping):
        request = _copy(dict(declared_eligibility_request))
    else:
        return _minimal_blocked_result(
            {},
            "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED",
            "Declared reception eligibility / admissibility request is not a mapping.",
        )

    role_result, load_code, load_detail, role_path = _load_selected_role_result(request)
    role_section = _role_result_section(
        request, role_result, load_code, load_detail, role_path
    )
    selected_surface = _selected_source_surface_section(request, role_section)
    receiving_context = _receiving_context_section(request, role_section)
    checks = _build_checks(request, role_section, selected_surface, receiving_context)
    block_code = _first_failed_code(checks)
    if block_code is not None:
        outcome = OUTCOME_BLOCKED
    else:
        requested_outcome = request.get(
            "requested_eligibility_outcome", OUTCOME_ELIGIBLE_ADMISSIBLE
        )
        if request.get("eligibility_intent", INTENT_RECORD) == INTENT_DO_NOT_RECORD:
            outcome = OUTCOME_NOT_ELIGIBLE
        elif requested_outcome == OUTCOME_NOT_ELIGIBLE:
            outcome = OUTCOME_NOT_ELIGIBLE
        elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
            outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        elif requested_outcome == OUTCOME_ELIGIBLE_ADMISSIBLE:
            outcome = OUTCOME_ELIGIBLE_ADMISSIBLE
        elif requested_outcome == OUTCOME_BLOCKED:
            outcome = OUTCOME_BLOCKED
            block_code = "RECEPTION_ELIGIBILITY_REVIEW_REQUEST_EXPLICITLY_BLOCKED"
        else:
            outcome = OUTCOME_BLOCKED
            block_code = "RECEPTION_ELIGIBILITY_INTENT_UNSUPPORTED"
    return _result(
        request,
        role_section,
        selected_surface,
        receiving_context,
        checks,
        outcome,
        block_code,
    )


def resolve_source_body_reception_eligibility_admissibility_boundary_from_path(
    declared_eligibility_request_path: Path | str,
) -> dict[str, Any]:
    payload, error, detail = _read_json_object(declared_eligibility_request_path)
    request_path = str(declared_eligibility_request_path)
    if error == "unreadable":
        return _minimal_blocked_result(
            {"declared_eligibility_request_path": request_path},
            "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_UNREADABLE",
            detail,
        )
    if error == "malformed":
        return _minimal_blocked_result(
            {"declared_eligibility_request_path": request_path},
            "DECLARED_RECEPTION_ELIGIBILITY_REQUEST_MALFORMED",
            detail,
        )
    assert payload is not None
    request = _copy(payload)
    request["declared_eligibility_request_path"] = request_path
    return resolve_source_body_reception_eligibility_admissibility_boundary(request)


def _default_filename(result: Mapping[str, Any]) -> str:
    question = _mapping(result.get("declared_eligibility_question"))
    role = _mapping(result.get("selected_receiving_context_role_result"))
    basis = _first(
        question.get("eligibility_request_id"),
        role.get("selected_receiving_context_role_result_id"),
        _get(
            result,
            (
                "source_body_reception_eligibility_metadata",
                "source_body_reception_eligibility_result_id",
            ),
        ),
        RESULT_ID_PREFIX,
    )
    return f"{_safe_component(basis)}__source_body_reception_eligibility_admissibility_result.json"


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


def write_source_body_reception_eligibility_admissibility_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise SourceBodyReceptionEligibilityAdmissibilityBoundaryError(
            "Eligibility / admissibility result must be a mapping."
        )
    target = (
        Path(output_path)
        if output_path is not None
        else SOURCE_BODY_RECEPTION_ELIGIBILITY_ADMISSIBILITY_BOUNDARY_ROOT
        / _default_filename(result)
    )
    target = _unique_path(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("w", encoding="utf-8") as handle:
        json.dump(result, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return target


def build_declared_source_body_reception_eligibility_admissibility_request(
    eligibility_request_id: str,
    eligibility_question: str,
    selected_receiving_context_role_result: Mapping[str, Any] | str,
    eligibility_basis: Mapping[str, Any] | str,
    admissibility_basis: Mapping[str, Any] | str,
    eligibility_scope: Sequence[str] | Mapping[str, Any],
    eligibility_intent: str = INTENT_RECORD,
    *,
    selected_receiving_context_role_result_path: str | None = None,
    selected_receiving_context_role_result_id: str | None = None,
    selected_receiving_context_role_result_outcome: str | None = None,
    requested_eligibility_outcome: str = OUTCOME_ELIGIBLE_ADMISSIBLE,
    review_readiness_limits: Mapping[str, Any] | str | None = None,
    additional_basis_context: Mapping[str, Any] | None = None,
    not_eligible_basis: Mapping[str, Any] | str | None = None,
) -> dict[str, Any]:
    request: dict[str, Any] = {
        "eligibility_request_id": eligibility_request_id,
        "eligibility_question": eligibility_question,
        "eligibility_intent": eligibility_intent,
        "eligibility_basis": _copy(eligibility_basis),
        "admissibility_basis": _copy(admissibility_basis),
        "eligibility_scope": _copy(eligibility_scope),
        "review_readiness_limits": _copy(
            review_readiness_limits
            if review_readiness_limits is not None
            else {
                "review_readiness_for_later_reception_family_review_only": True,
                "non_capture_requires_separate_boundary": True,
                "recognition_requires_separate_boundary": True,
            }
        ),
        "requested_eligibility_outcome": requested_eligibility_outcome,
        "declared_non_claims": {key: False for key in REQUIRED_NON_CLAIMS},
    }
    if selected_receiving_context_role_result_path is not None:
        request[
            "selected_receiving_context_role_result_path"
        ] = selected_receiving_context_role_result_path
    else:
        request["selected_receiving_context_role_result"] = _copy(
            selected_receiving_context_role_result
        )
    if selected_receiving_context_role_result_id is not None:
        request[
            "selected_receiving_context_role_result_id"
        ] = selected_receiving_context_role_result_id
    if selected_receiving_context_role_result_outcome is not None:
        request[
            "selected_receiving_context_role_result_outcome"
        ] = selected_receiving_context_role_result_outcome
    if additional_basis_context is not None:
        request["additional_basis_context"] = _copy(additional_basis_context)
    if not_eligible_basis is not None:
        request["not_eligible_basis"] = _copy(not_eligible_basis)
    return request
