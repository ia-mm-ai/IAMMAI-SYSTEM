"""V2 successor for one bounded candidate non-cosmetic scope declaration operation.

V1 remains preserved lineage.  This successor changes only two live-summary
acceptance rules: equivalent clean boundary posture and equivalent
no-standing/no-descendant differentiation posture.  It records no operation
by default: missing declared scopes remain clean additional basis.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min as _v1


class DescendantBodyCandidateNonCosmeticScopeDivisionDeclarationOperationV0MinV2Error(Exception):
    """Raised for bounded v2 request-path and JSON handling errors."""


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2"

OPERATION_TYPE = _v1.OPERATION_TYPE
OPERATION_VERSION = _v1.OPERATION_VERSION
OPERATION_SCOPE = _v1.OPERATION_SCOPE
ADMISSIBLE_FUTURE_ROUTE = _v1.ADMISSIBLE_FUTURE_ROUTE

OUTCOME_RECORDED = _v1.OUTCOME_RECORDED
OUTCOME_BLOCKED = _v1.OUTCOME_BLOCKED
OUTCOME_REQUIRES_ADDITIONAL_BASIS = _v1.OUTCOME_REQUIRES_ADDITIONAL_BASIS
OUTCOME_NOT_RECORDED = _v1.OUTCOME_NOT_RECORDED
OUTCOME_FAMILY = _v1.OUTCOME_FAMILY

INTENT_RECORD = _v1.INTENT_RECORD
INTENT_DO_NOT_RECORD = _v1.INTENT_DO_NOT_RECORD
INTENT_BLOCK = _v1.INTENT_BLOCK
SUPPORTED_INTENTS = _v1.SUPPORTED_INTENTS

DEFAULT_OPERATION_ID = _v1.DEFAULT_OPERATION_ID
DEFAULT_CANDIDATE_A_ID = _v1.DEFAULT_CANDIDATE_A_ID
DEFAULT_CANDIDATE_B_ID = _v1.DEFAULT_CANDIDATE_B_ID
DEFAULT_CANDIDATE_A_ROLE = _v1.DEFAULT_CANDIDATE_A_ROLE
DEFAULT_CANDIDATE_B_ROLE = _v1.DEFAULT_CANDIDATE_B_ROLE
UPSTREAM_EMISSION_OPERATION_RESULT = _v1.UPSTREAM_EMISSION_OPERATION_RESULT

SCOPE_DECLARATION_POLICY = _v1.SCOPE_DECLARATION_POLICY
SCOPE_LABEL_LAUNDERING_POLICY = _v1.SCOPE_LABEL_LAUNDERING_POLICY
COSMETIC_SCOPE_NAMING_POLICY = _v1.COSMETIC_SCOPE_NAMING_POLICY
ID_ROLE_LABEL_DIFFERENCE_POLICY = _v1.ID_ROLE_LABEL_DIFFERENCE_POLICY
SHARED_EVIDENCE_POLICY = _v1.SHARED_EVIDENCE_POLICY
OPERATION_EVIDENCE_POLICY = _v1.OPERATION_EVIDENCE_POLICY
CONTAMINATED_LINEAGE_POLICY = _v1.CONTAMINATED_LINEAGE_POLICY

REPO_ROOT = _v1.REPO_ROOT
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_non_cosmetic_"
    "scope_division_declaration_operation_v0_min_v2"
)

DEFAULT_OPERATION_SPEC_REFERENCE = _v1.DEFAULT_OPERATION_SPEC_REFERENCE
DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_SCOPE_DIVISION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_SCOPE_DIVISION_BOUNDARY_ARTIFACT_REFERENCE = _v1.DEFAULT_SCOPE_DIVISION_BOUNDARY_ARTIFACT_REFERENCE
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_BASIS_EMISSION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    _v1.DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE
)

REQUIRED_FALSE_NON_CLAIMS = _v1.REQUIRED_FALSE_NON_CLAIMS
ALLOWED_TRUE_RECORDED_FIELDS = _v1.ALLOWED_TRUE_RECORDED_FIELDS
BLOCK_CODES = _v1.BLOCK_CODES


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _text_has_any(text: str, candidates: tuple[str, ...]) -> bool:
    lowered = text.lower()
    return any(candidate.lower() in lowered for candidate in candidates)


def _boundary_posture_classes_present(text: str | None) -> tuple[bool, list[str]]:
    """Accept clean equivalent boundary posture without brittle v1 wording."""

    class_names = (
        "boundary_recorded",
        "clean_v3_result",
        "future_operation_shape_allowed",
        "missing_upstream_scope_declarations_preserved",
        "scope_declarations_not_created",
        "scope_label_laundering_blocked",
        "scope_thesis",
    )
    if text is None:
        return False, list(class_names)

    lowered = text.lower()
    recorded = _text_has_any(
        text,
        (
            "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
            "RECORDED as the live v3 boundary outcome",
            "boundary result recorded RECORDED",
            "boundary recorded RECORDED",
            "outcome DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
            "outcome = DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",
        ),
    )
    clean_v3 = (
        all(
            marker in lowered
            for marker in (
                "failed_check_count = 0",
                "result_version = 0.3.0",
                "resolver_module = resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_boundary_v0_min_v3",
            )
        )
        or "v3 live artifact recorded cleanly" in lowered
        or (
            "v3 test execution passed" in lowered
            and "ran 16 tests" in lowered
            and "ok" in lowered
        )
    )
    future_shape = _text_has_any(
        text,
        (
            "future_scope_declaration_operation_type = DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
            "future_scope_declaration_operation_type DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION",
            "future_scope_declaration_operation_shape_allowed = true",
            "future_scope_declaration_operation_shape_allowed true",
            "allows only future scope declaration operation shape",
            "allowed only a future scope declaration operation shape",
        ),
    )
    missing_scopes = all(
        _text_has_any(text, candidates)
        for candidates in (
            (
                "candidate_a_scope_missing_upstream = true",
                "candidate_a_scope_missing_upstream true",
                "non-cosmetic candidate A scope is still missing upstream",
            ),
            (
                "candidate_b_scope_missing_upstream = true",
                "candidate_b_scope_missing_upstream true",
                "non-cosmetic candidate B scope is still missing upstream",
            ),
            (
                "basis_bearing_scope_division_missing_upstream = true",
                "basis_bearing_scope_division_missing_upstream true",
                "basis-bearing scope division is still missing upstream",
            ),
        )
    )
    not_declared = all(
        _text_has_any(text, candidates)
        for candidates in (
            (
                "candidate_a_scope_not_declared = true",
                "candidate_a_scope_not_declared true",
                "does not declare candidate A scope",
                "not candidate A scope declaration",
            ),
            (
                "candidate_b_scope_not_declared = true",
                "candidate_b_scope_not_declared true",
                "does not declare candidate B scope",
                "not candidate B scope declaration",
            ),
            (
                "basis_bearing_scope_division_not_declared = true",
                "basis_bearing_scope_division_not_declared true",
                "does not declare basis-bearing scope division",
                "not basis-bearing scope division declaration",
            ),
        )
    )
    laundering_blocked = _text_has_any(
        text,
        (
            "rupture_class_blocked = SCOPE_LABEL_LAUNDERING",
            "rupture_class_blocked SCOPE_LABEL_LAUNDERING",
            "scope_label_laundering_not_allowed = true",
            "scope_label_laundering_not_allowed true",
            "scope-label laundering remains blocked",
            "blocks scope-label laundering",
            "boundary blocks scope-label laundering",
        ),
    )
    thesis = all(
        marker in lowered
        for marker in (
            "scope declaration is not scope standing",
            "a scope label is not a scope",
            "scope division must be basis-bearing, not label-bearing",
        )
    )
    classes = {
        "boundary_recorded": recorded,
        "clean_v3_result": clean_v3,
        "future_operation_shape_allowed": future_shape,
        "missing_upstream_scope_declarations_preserved": missing_scopes,
        "scope_declarations_not_created": not_declared,
        "scope_label_laundering_blocked": laundering_blocked,
        "scope_thesis": thesis,
    }
    missing = [name for name in class_names if not classes[name]]
    return not missing, missing


def _differentiation_posture_classes_present_v2(text: str | None) -> tuple[bool, list[str]]:
    """Preserve all differentiation classes while accepting live equivalent refusal."""

    class_names = (
        "completion",
        "exactly_two_candidates",
        "non_standing_not_descendant_bodies",
        "standing_descendant_creation_not_authorized",
        "crossing_relation_not_authorized",
    )
    if text is None:
        return False, list(class_names)
    lowered = text.lower()
    no_standing_or_descendant = _text_has_any(
        text,
        (
            "standing_descendant_created = false",
            "standing_descendant_created false",
            "standing descendants were not created",
            "no standing descendants",
            "standing_descendants_not_created",
            "descendant_body_created = false",
            "descendant_body_created false",
            "descendant bodies were not created",
            "no descendant bodies",
            "candidate_standing_authorized = false",
            "candidate_standing_authorized false",
            "no candidate standing",
            "candidate records remain non-standing",
            "candidate records are non-standing",
        ),
    )
    classes = {
        "completion": "descendant_body_differentiation_operation" in lowered
        or "differentiation operation" in lowered,
        "exactly_two_candidates": "exactly two" in lowered and "candidate" in lowered,
        "non_standing_not_descendant_bodies": "non-standing" in lowered
        and ("not descendant bodies" in lowered or "descendant_body_created = false" in lowered),
        "standing_descendant_creation_not_authorized": no_standing_or_descendant,
        "crossing_relation_not_authorized": "crossing" in lowered
        and "relation" in lowered
        and ("not authorized" in lowered or "= false" in lowered),
    }
    missing = [name for name in class_names if not classes[name]]
    return not missing, missing


def _validate_boundary_summary_v2(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    text = _v1._read_declared_text(
        request.get("completed_scope_division_declaration_boundary_terminal_summary_reference")
    )
    passed, missing = _boundary_posture_classes_present(text)
    _v1._add_check(
        checks,
        "scope-division declaration boundary terminal summary markers present",
        passed,
        "all required clean boundary posture classes present",
        {"missing_boundary_posture_classes": missing},
        "COMPLETED_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    return passed


def _validate_differentiation_summary_v2(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> bool:
    text = _v1._read_declared_text(
        request.get("completed_differentiation_operation_terminal_summary_reference")
    )
    passed, missing = _differentiation_posture_classes_present_v2(text)
    _v1._add_check(
        checks,
        "differentiation operation terminal summary posture classes present",
        passed,
        "completion, exactly-two, non-standing, no standing, no crossing/relation classes",
        {"missing_posture_classes": missing},
        "COMPLETED_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    return passed


def _validate_request_v2(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    """Run the v1 request contract with only the two corrected live validators."""

    _v1._validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_type",
        OPERATION_TYPE,
        "operation type exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TYPE_NOT_EXPECTED",
    )
    _v1._validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_version",
        OPERATION_VERSION,
        "operation version exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_VERSION_NOT_0_1_0",
    )
    _v1._validate_exact(
        checks,
        request,
        "candidate_non_cosmetic_scope_division_declaration_operation_scope",
        OPERATION_SCOPE,
        "operation scope exact",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_MISSING",
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_SCOPE_NOT_EXPECTED",
    )
    _v1._validate_exact(
        checks,
        request,
        "admissible_future_route",
        ADMISSIBLE_FUTURE_ROUTE,
        "admissible future route exact",
        "ADMISSIBLE_FUTURE_ROUTE_MISSING",
        "ADMISSIBLE_FUTURE_ROUTE_NOT_EXPECTED",
    )
    for field, code in _v1.REFERENCE_FIELDS_AND_CODES:
        _v1._validate_reference_declared(checks, request, field, code)
    _v1._validate_marker_file(
        checks,
        request,
        "operation_spec_reference",
        "operation spec markers present",
        _v1.OPERATION_SPEC_MARKERS,
        "OPERATION_SPEC_MARKER_MISSING",
    )
    _validate_boundary_summary_v2(checks, request)
    _v1._validate_marker_file(
        checks,
        request,
        "completed_basis_emission_operation_terminal_summary_reference",
        "basis emission operation terminal summary markers present",
        _v1.BASIS_EMISSION_OPERATION_MARKERS,
        "COMPLETED_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _v1._validate_marker_file(
        checks,
        request,
        "completed_distinctness_operation_terminal_summary_reference",
        "distinctness operation terminal summary markers present",
        _v1.DISTINCTNESS_OPERATION_MARKERS,
        "COMPLETED_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    )
    _validate_differentiation_summary_v2(checks, request)
    exact_values = (
        ("candidate_record_a_id", DEFAULT_CANDIDATE_A_ID, "CANDIDATE_RECORD_A_ID_NOT_EXPECTED"),
        ("candidate_record_b_id", DEFAULT_CANDIDATE_B_ID, "CANDIDATE_RECORD_B_ID_NOT_EXPECTED"),
        ("candidate_record_a_role", DEFAULT_CANDIDATE_A_ROLE, "CANDIDATE_RECORD_A_ROLE_NOT_EXPECTED"),
        ("candidate_record_b_role", DEFAULT_CANDIDATE_B_ROLE, "CANDIDATE_RECORD_B_ROLE_NOT_EXPECTED"),
        (
            "upstream_emission_operation_result",
            UPSTREAM_EMISSION_OPERATION_RESULT,
            "UPSTREAM_EMISSION_OPERATION_RESULT_NOT_REQUIRES_ADDITIONAL_BASIS",
        ),
    )
    for field, expected, code in exact_values:
        _v1._validate_exact(checks, request, field, expected, f"{field} exact", code, code)
    for field, expected, check_name, code in (
        (
            "requires_additional_basis_preserved_as_clean_result",
            True,
            "REQUIRES_ADDITIONAL_BASIS preserved as clean result",
            "REQUIRES_ADDITIONAL_BASIS_NOT_PRESERVED_AS_CLEAN_RESULT",
        ),
        (
            "candidate_a_scope_missing_upstream",
            True,
            "candidate A scope missing upstream true",
            "CANDIDATE_A_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
        ),
        (
            "candidate_b_scope_missing_upstream",
            True,
            "candidate B scope missing upstream true",
            "CANDIDATE_B_SCOPE_MISSING_UPSTREAM_NOT_TRUE",
        ),
        (
            "basis_bearing_scope_division_missing_upstream",
            True,
            "basis-bearing scope division missing upstream true",
            "BASIS_BEARING_SCOPE_DIVISION_MISSING_UPSTREAM_NOT_TRUE",
        ),
    ):
        _v1._validate_bool_exact(checks, request, field, expected, check_name, code)
    for field, expected, code in (
        ("scope_declaration_policy", SCOPE_DECLARATION_POLICY, "SCOPE_DECLARATION_POLICY_NOT_EXPECTED"),
        (
            "scope_label_laundering_policy",
            SCOPE_LABEL_LAUNDERING_POLICY,
            "SCOPE_LABEL_LAUNDERING_POLICY_NOT_EXPECTED",
        ),
        ("cosmetic_scope_naming_policy", COSMETIC_SCOPE_NAMING_POLICY, "COSMETIC_SCOPE_NAMING_POLICY_NOT_EXPECTED"),
        (
            "id_role_label_difference_policy",
            ID_ROLE_LABEL_DIFFERENCE_POLICY,
            "ID_ROLE_LABEL_DIFFERENCE_POLICY_NOT_EXPECTED",
        ),
        ("shared_evidence_policy", SHARED_EVIDENCE_POLICY, "SHARED_EVIDENCE_POLICY_NOT_EXPECTED"),
        ("operation_evidence_policy", OPERATION_EVIDENCE_POLICY, "OPERATION_EVIDENCE_POLICY_NOT_EXPECTED"),
        (
            "contaminated_lineage_policy",
            CONTAMINATED_LINEAGE_POLICY,
            "CONTAMINATED_LINEAGE_POLICY_NOT_EXPECTED",
        ),
    ):
        _v1._validate_exact(checks, request, field, expected, f"{field} exact", code, code)
    for field, code in _v1.FALSE_FIELD_CODES.items():
        _v1._validate_bool_exact(checks, request, field, False, f"{field} false", code)
    _v1._validate_non_claims(checks, request)
    _v1._add_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "final result canonicalizes required false non-claims",
        "canonical false emitted by resolver",
    )


def _operation_marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    return _v1._operation_marker_flags(checks)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    additional_basis_required: list[str] | None = None,
    not_recorded_basis: list[str] | None = None,
    recorded: bool = False,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _operation_marker_flags(checks)
    operation = _v1._build_operation_object(request, recorded, marker_flags)
    operation_id = operation["candidate_non_cosmetic_scope_division_declaration_operation_id"]
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "candidate_non_cosmetic_scope_division_declaration_operation_metadata": {
            "candidate_non_cosmetic_scope_division_declaration_operation_id": operation_id,
            "operation_type": OPERATION_TYPE,
            "result_version": RESULT_VERSION,
            "generated_at": _utc_now(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_candidate_non_cosmetic_scope_division_declaration_operation_basis": _v1._sanitize_json_value(request),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            "completed_scope_division_declaration_boundary_terminal_summary_reference": request.get(
                "completed_scope_division_declaration_boundary_terminal_summary_reference"
            ),
            "completed_scope_division_declaration_boundary_artifact_reference": request.get(
                "completed_scope_division_declaration_boundary_artifact_reference"
            ),
            "completed_basis_emission_operation_terminal_summary_reference": request.get(
                "completed_basis_emission_operation_terminal_summary_reference"
            ),
            "completed_basis_emission_boundary_terminal_summary_reference": request.get(
                "completed_basis_emission_boundary_terminal_summary_reference"
            ),
            "completed_distinctness_operation_terminal_summary_reference": request.get(
                "completed_distinctness_operation_terminal_summary_reference"
            ),
            "completed_differentiation_operation_terminal_summary_reference": request.get(
                "completed_differentiation_operation_terminal_summary_reference"
            ),
            **marker_flags,
        },
        "descendant_body_candidate_non_cosmetic_scope_division_declaration_operation": operation,
        "candidate_non_cosmetic_scope_division_declaration_operation_checks": checks,
        "candidate_non_cosmetic_scope_division_declaration_operation_statement": _v1._build_statement(
            operation, outcome
        ),
        "candidate_non_cosmetic_scope_division_declaration_operation_non_meaning": _v1._build_non_meaning(),
        "additional_basis_required": additional_basis_required or [],
        "not_recorded_basis": not_recorded_basis or [],
        "what_remains_open": [
            "candidate non-cosmetic scope-division declaration resolver successor work if separately selected",
            "candidate-specific distinctness basis emission operation successor if separately bounded",
            "actual candidate-specific content emission",
            "actual separate seal material emission",
            "actual separate lineage receipt material emission",
            "actual separate digest material emission",
            "future distinctness-supported operation result if separately supported",
            "candidate standing check",
            "first crossing",
            "relation",
            "FIELD machinery",
            "runtime",
            "currentness",
            "authority",
            "output authorization",
            "action authorization",
            "derivative reception",
            "synchronization",
            "follow-on work",
        ],
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
    }
    result["candidate_non_cosmetic_scope_division_declaration_operation_summary"] = (
        build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_summary(result)
    )
    return result


def _blocked_result(
    request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _v1._add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        additional_basis_required=[],
        not_recorded_basis=[],
        recorded=False,
        block_code=code,
        block_reason=reason,
    )


def build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one v2 request using the current missing-scope live posture."""

    return _v1.build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_request(
        **overrides
    )


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(
    declared_candidate_non_cosmetic_scope_division_declaration_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one v2 operation without creating scope or descendant standing."""

    if declared_candidate_non_cosmetic_scope_division_declaration_operation is None:
        request = build_declared_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_request()
    elif not isinstance(declared_candidate_non_cosmetic_scope_division_declaration_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _v1._add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_candidate_non_cosmetic_scope_division_declaration_operation).__name__,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
            "request is not a mapping",
        )
    else:
        request = copy.deepcopy(dict(declared_candidate_non_cosmetic_scope_division_declaration_operation))

    checks: list[dict[str, Any]] = []
    intent = request.get("candidate_non_cosmetic_scope_division_declaration_operation_intent")
    _v1._add_check(
        checks,
        "operation intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        return _blocked_result(
            request,
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_BLOCK_REQUESTED",
            "block intent requested",
        )
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(
            request,
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_INTENT_UNSUPPORTED",
            "operation intent is unsupported",
        )

    _validate_request_v2(checks, request)
    _v1._validate_prohibited_requests(checks, request)
    failed_codes = _v1._failed_codes(checks)
    if failed_codes:
        code = failed_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            additional_basis_required=[],
            not_recorded_basis=["DO_NOT_RECORD intent requested"],
            recorded=False,
        )

    additional_basis_required = _v1._missing_scope_basis(request)
    if additional_basis_required:
        return _build_result(
            request,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            checks,
            additional_basis_required=additional_basis_required,
            not_recorded_basis=[],
            recorded=False,
        )

    _v1._validate_recordable_scope(checks, request)
    failed_codes = _v1._failed_codes(checks)
    if failed_codes:
        code = failed_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")
    return _build_result(
        request,
        OUTCOME_RECORDED,
        checks,
        additional_basis_required=[],
        not_recorded_basis=[],
        recorded=True,
    )


def resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_from_path(
    declared_candidate_non_cosmetic_scope_division_declaration_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one declared JSON request object and resolve it with v2 posture checks."""

    path = Path(declared_candidate_non_cosmetic_scope_division_declaration_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _v1._add_check(
            checks,
            "request path readable JSON",
            False,
            "readable JSON object",
            str(exc),
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_UNREADABLE",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_UNREADABLE",
            "request path is unreadable or not JSON",
        )
    if not isinstance(data, Mapping):
        checks = []
        _v1._add_check(
            checks,
            "request JSON object",
            False,
            "JSON object mapping",
            type(data).__name__,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
        )
        return _blocked_result(
            {},
            checks,
            "CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2(data)


def build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the v2 summary without raw Markdown-body material."""

    summary = _v1.build_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_summary(result)
    summary["result_version"] = RESULT_VERSION
    summary["resolver_module"] = RESOLVER_MODULE
    return summary


def write_descendant_body_candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write stable UTF-8 v2 JSON without overwriting an existing result."""

    operation = result.get("descendant_body_candidate_non_cosmetic_scope_division_declaration_operation", {})
    operation_id = DEFAULT_OPERATION_ID
    if isinstance(operation, Mapping):
        operation_id = str(
            operation.get("candidate_non_cosmetic_scope_division_declaration_operation_id")
            or DEFAULT_OPERATION_ID
        )
    filename = (
        f"{_v1._safe_json_filename_part(operation_id)}__"
        "candidate_non_cosmetic_scope_division_declaration_operation_v0_min_v2_result.json"
    )
    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / filename
    else:
        candidate = Path(output_path)
        base = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        path = base if base.suffix else base / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    final_path = path
    counter = 1
    while final_path.exists():
        final_path = path.with_name(f"{path.stem}_{counter:03d}{path.suffix}")
        counter += 1
    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_v1._json_ready(result), handle, ensure_ascii=True, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path
