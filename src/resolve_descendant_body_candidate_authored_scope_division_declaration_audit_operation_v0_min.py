"""Resolve one bounded authored scope-division declaration audit result.

The resolver evaluates only bounded structured V2 declaration audit fields. It
does not ingest a PDF, expose raw bodies, create standing, or close the prior
additional-basis gap.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateAuthoredScopeDivisionDeclarationAuditOperationV0MinError(Exception):
    """Raised for bounded audit-operation request and write failures."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_authored_scope_division_declaration_audit_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "RECEIVED_AUTHORED_DECLARATION_AUDIT_FOR_MISSING_SCOPE_DIVISION_BASIS_ONLY"
UPSTREAM_RECEIPT_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION"
UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED"
)
UPSTREAM_RECEIPT_STATUS_REQUIRED = "RECEIVED_AS_METADATA_FOR_AUDIT_ONLY"
AUDITED_MATERIAL_EXPECTED_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf"
AUDITED_MATERIAL_EXPECTED_VERSION = "v2"
AUDITED_MATERIAL_EXPECTED_DATE = "10 July 2026"
AUDITED_MATERIAL_EXPECTED_AUTHOR = "Marko Markota"
AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE = "AUTHORSHIP_ATTESTATION_ONLY"
AUDITED_MATERIAL_EXPECTED_PREDECESSOR = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION v1"
AUDITED_MATERIAL_PREDECESSOR_ROLE = "REFERENCED_PREDECESSOR_ONLY"
ADMISSIBLE_FUTURE_ROUTE = "AUDIT_THEN_SUCCESSOR_CLOSURE_ONLY"

OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_"
    "SATISFIES_MISSING_BASIS_REQUIREMENTS"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_"
    "REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_NOT_RECORDED"
)
OUTCOME_FAMILY = (
    OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)
OUTCOME_RECORDED = OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_descendant_body_candidate_authored_scope_"
    "division_declaration_audit_operation_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_candidate_authored_scope_division_declaration_audit_operation_001"
    "__authored_scope_division_declaration_audit_operation_v0_min_result.json"
)

DEFAULT_OPERATION_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_"
    "AUDIT_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_AUDIT_OPERATION_SPEC_REFERENCE = DEFAULT_OPERATION_SPEC_REFERENCE
DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_"
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_"
    "TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "BOUNDARY_TERMINAL_SUMMARY_V0.md"
)

AUDIT_CRITERIA = (
    "candidate_a_non_cosmetic_scope_declaration",
    "candidate_b_non_cosmetic_scope_declaration",
    "basis_bearing_scope_division",
    "motion_regulation_difference_by_mandate_function_responsibility_governed_surface",
    "sibling_non_monarchy",
    "coupling_not_assigned",
    "no_third_model",
    "lineage_constraints",
    "non_standing_preservation",
)
AUDITED_FIELD_BY_CRITERION = {
    "candidate_a_non_cosmetic_scope_declaration": "candidate_a_scope_audited",
    "candidate_b_non_cosmetic_scope_declaration": "candidate_b_scope_audited",
    "basis_bearing_scope_division": "basis_bearing_scope_division_audited",
    "motion_regulation_difference_by_mandate_function_responsibility_governed_surface": (
        "motion_regulation_difference_audited"
    ),
    "sibling_non_monarchy": "sibling_non_monarchy_audited",
    "coupling_not_assigned": "coupling_not_assigned_audited",
    "no_third_model": "no_third_model_audited",
    "lineage_constraints": "lineage_constraints_audited",
    "non_standing_preservation": "non_standing_preservation_audited",
}
SATISFIED_FIELD_BY_CRITERION = {
    criterion: field.replace("_audited", "_satisfied")
    for criterion, field in AUDITED_FIELD_BY_CRITERION.items()
}

ALLOWED_TRUE_RECORDED_FIELDS = (
    "audit_operation_recorded",
    "audit_performed",
    "audit_result_recorded",
    "declaration_accepted_as_basis",
    *AUDITED_FIELD_BY_CRITERION.values(),
    *SATISFIED_FIELD_BY_CRITERION.values(),
)

REQUIRED_FALSE_NON_CLAIMS = (
    "declaration_admitted_as_standing_basis",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
    "basis_gap_closed",
    "candidate_specific_content_emitted",
    "separate_seal_material_emitted",
    "separate_lineage_receipt_material_emitted",
    "separate_digest_material_emitted",
    "candidate_specific_distinctness_basis_emission_operation_rerun",
    "distinctness_operation_rerun",
    "distinctness_supported_recorded",
    "candidate_records_marked_distinct",
    "candidate_records_distinct",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
    "standing_authorized",
    "standing_descendant_created",
    "descendant_standing_check_performed",
    "crossing_authorized",
    "first_crossing_authorized",
    "relation_created",
    "field_machinery_created",
    "runtime_created",
    "api_created",
    "currentness_created",
    "authority_created",
    "standing_created",
    "output_authorized",
    "action_authorized",
    "derivative_reception_authorized",
    "synchronization_authorized",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "third_candidate_created",
    "third_model_admitted",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "prior_unsupported_claim_validated",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "valid_derivation_event_recorded",
    "affected_file_repaired",
    "affected_file_edited",
    "affected_file_deleted",
    "affected_file_overwritten",
    "affected_file_replaced",
    "affected_file_redeemed",
    "affected_file_treated_as_clean_basis",
    "contaminated_lineage_treated_as_clean_basis",
    "authored_scope_division_declaration_receipt_operation_overridden",
    "authored_scope_division_declaration_receipt_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_audit_permission_to_audit_completion_conversion",
    "direct_audit_result_to_standing_conversion",
    "direct_audit_result_to_scope_declaration_conversion",
    "direct_audit_result_to_basis_gap_closure_conversion",
    "direct_accepted_basis_to_standing_basis_conversion",
    "direct_accepted_basis_to_emitted_content_conversion",
    "direct_audit_to_candidate_specific_basis_emission_conversion",
    "direct_audit_to_distinctness_support_conversion",
    "direct_audit_to_candidate_records_distinct_conversion",
    "direct_audit_to_candidate_standing_conversion",
    "direct_audit_to_descendant_body_creation",
    "direct_audit_to_relation_creation",
    "direct_audit_to_runtime_creation",
    "direct_audit_to_authority_currentness_creation",
    "direct_audit_to_coupling_creation",
    "direct_audit_to_third_candidate_route",
    "direct_audit_to_third_model_route",
    "direct_audit_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "AUDIT_OPERATION_SPEC_REFERENCE_MISSING",
    "AUDIT_OPERATION_SPEC_MARKER_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "MATERIAL_METADATA_MISSING_OR_INVALID",
    "AUDIT_MATERIAL_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_AUDIT_TO_STANDING_REQUESTED",
    "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "PROHIBITED_BASIS_GAP_CLOSURE_REQUESTED",
    "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "REQUESTED_RAW_MATERIAL_BODY_RETURN",
    "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_declaration_standing_basis_admission": "PROHIBITED_AUDIT_TO_STANDING_REQUESTED",
    "request_candidate_a_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_candidate_b_scope_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_basis_bearing_scope_division_declaration": "PROHIBITED_SCOPE_DECLARATION_REQUESTED",
    "request_basis_gap_closure": "PROHIBITED_BASIS_GAP_CLOSURE_REQUESTED",
    "request_candidate_specific_content_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_seal_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_lineage_receipt_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_separate_digest_material_emission": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_basis_emission_operation_rerun": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_distinctness_operation_rerun": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_distinctness_supported_recording": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_candidate_records_marked_distinct": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_runtime_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_api_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_currentness_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_authority_creation": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "return_raw_material_body": "REQUESTED_RAW_MATERIAL_BODY_RETURN",
    "return_raw_markdown_body": "REQUESTED_RAW_MARKDOWN_BODY_RETURN",
}

SENSITIVE_BODY_KEYS = {
    "raw_body",
    "raw_material_body",
    "raw_pdf_body",
    "raw_markdown_body",
    "markdown_body",
    "full_body",
    "full_text",
    "extracted_text",
    "source_body",
    "hidden_repo_state",
    "current_working_tree",
}

OPERATION_SPEC_MARKER_CLASSES = (
    ("operation_identity", ("Descendant Body Candidate Authored Scope Division Declaration Audit Operation V0 Minimum Specification", OPERATION_TYPE, OPERATION_ID, OPERATION_SCOPE)),
    ("upstream_receipt", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, UPSTREAM_RECEIPT_STATUS_REQUIRED, AUDITED_MATERIAL_EXPECTED_FILENAME, AUDITED_MATERIAL_EXPECTED_VERSION, AUDITED_MATERIAL_EXPECTED_DATE, AUDITED_MATERIAL_EXPECTED_AUTHOR, AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE, AUDITED_MATERIAL_EXPECTED_PREDECESSOR, AUDITED_MATERIAL_PREDECESSOR_ROLE)),
    ("audit_criteria", AUDIT_CRITERIA),
    ("permitted_outcomes", ("SATISFIES_MISSING_BASIS_REQUIREMENTS", "REQUIRES_ADDITIONAL_BASIS", "BLOCKED")),
    ("audit_non_standing", ("Audit permission is not audit completion", "Audit result is not standing", "Accepted basis is not standing basis")),
    ("sibling_coupling_no_third", ("sibling non-standing candidate", "neither may rank above the other", "Regulation may not become sovereign over Motion", "Motion may not erase Regulation", "unassigned", "No third candidate", "third model")),
    ("lineage", ("V1 predecessor reference is lineage only", "V2 receipt does not erase V1", "No orphaned state", "silent reset", "overwrite")),
    ("receipt_relation", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", UPSTREAM_RECEIPT_STATUS_REQUIRED)),
    ("scope_operation_relation", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS", "passed_check_count = 96", "non-cosmetic candidate A scope declaration", "non-cosmetic candidate B scope declaration", "basis-bearing scope division declaration", "does not close that gap")),
    ("contaminated_lineage", ("DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md", "preserved contaminated lineage", "descendant_body_basis_candidate_a_created = true", "descendant_body_basis_candidate_b_created = true", "descendant_body_basis_derivation_event_recorded = true", "UNSUPPORTED", "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file")),
    ("blocked_routes", ("direct audit permission to audit completion", "direct audit result to standing conversion", "direct audit result to scope declaration conversion", "direct audit result to basis-gap closure conversion", "direct accepted basis to standing basis conversion", "direct audit to candidate-specific-basis-emission conversion", "direct audit to distinctness-support conversion", "direct audit to candidate-standing conversion", "direct audit to descendant-body creation", "direct audit to relation creation", "direct audit to runtime creation", "direct audit to coupling creation", "direct audit to third-candidate route", "direct audit to third-model route", "direct audit to follow-on work", "repository scan route", "affected-file repair route", "prior unsupported claim validation route")),
    ("closing_lock", ("This operation spec defines only a future audit operation shape", "Even a future audit result satisfying missing basis requirements may only provide basis for a separately bounded successor closure operation", "it does not itself close the gap", "Open means not scheduled, not authorized, and not executed")),
)

UPSTREAM_REQUIREMENTS = (
    ("receipt_operation_terminal_summary_reference", DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE, "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", (UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED, "failed_check_count = 0", "passed_check_count = 91", UPSTREAM_RECEIPT_STATUS_REQUIRED), "receipt_operation_terminal_summary_markers_present"),
    ("scope_division_declaration_operation_terminal_summary_reference", DEFAULT_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS", "failed_check_count = 0", "passed_check_count = 96", "missing non-cosmetic candidate A scope declaration", "missing non-cosmetic candidate B scope declaration", "missing basis-bearing scope division declaration"), "scope_division_declaration_operation_terminal_summary_markers_present"),
    ("existence_claim_evidence_check_terminal_summary_reference", DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE, "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING", "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING", ("UNSUPPORTED",), "existence_claim_evidence_check_terminal_summary_markers_present"),
    ("differentiation_operation_terminal_summary_reference", DEFAULT_DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DIFFERENTIATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_DIFFERENTIATION_OPERATION_RECORDED",), "differentiation_operation_terminal_summary_markers_present"),
    ("distinctness_operation_terminal_summary_reference", DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE, "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("NOT_DISTINCT",), "distinctness_operation_terminal_summary_markers_present"),
    ("basis_emission_operation_terminal_summary_reference", DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE, "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING", "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING", ("REQUIRES_ADDITIONAL_BASIS",), "basis_emission_operation_terminal_summary_markers_present"),
    ("scope_division_declaration_boundary_terminal_summary_reference", DEFAULT_SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE, "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING", "SCOPE_DIVISION_DECLARATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING", ("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_BOUNDARY_RECORDED",), "scope_division_declaration_boundary_terminal_summary_markers_present"),
)

WHAT_REMAINS_OPEN = (
    "successor operation to close additional-basis gap, if audit satisfies missing basis and if separately bounded",
    "candidate-specific distinctness basis emission operation successor",
    "actual candidate-specific content emission",
    "actual separate seal material emission",
    "actual separate lineage receipt material emission",
    "actual separate digest material emission",
    "future distinctness-supported operation result",
    "divergent receipt-history route, if separately bounded",
    "carrier separation route, if separately bounded",
    "candidate standing checks",
    "first crossing",
    "relation",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "output authorization",
    "action authorization",
    "derivative reception",
    "synchronization",
    "externalization boundary",
    "follow-on work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _resolve_declared_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        path = value
    elif _is_non_empty_string(value):
        path = Path(value)
    else:
        return None
    return path if path.is_absolute() else REPO_ROOT / path


def _read_declared_text(value: Any) -> str | None:
    path = _resolve_declared_path(value)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _is_sensitive_key(key: str) -> bool:
    lowered = key.lower()
    return lowered in SENSITIVE_BODY_KEYS or lowered.endswith("_body") or "raw_" in lowered


def _sanitize(value: Any, key: str = "") -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        text = value.strip()
        return text if len(text) <= 420 else f"{text[:420]}...[truncated]"
    return value


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _add_check(
    checks: list[dict[str, Any]],
    name: str,
    passed: bool,
    expected: Any,
    actual: Any,
    code: str | None = None,
) -> None:
    check: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
    }
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_codes(checks: list[dict[str, Any]]) -> list[str]:
    return [
        str(check.get("block_code") or check.get("failure_code"))
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code") or check.get("failure_code"), str)
        and (check.get("block_code") or check.get("failure_code")) in BLOCK_CODES
    ]


def _validate_reference(checks: list[dict[str, Any]], request: Mapping[str, Any], field: str, code: str) -> None:
    path = _resolve_declared_path(request.get(field))
    _add_check(
        checks,
        f"{field} readable file reference",
        path is not None and path.is_file(),
        "declared readable file path",
        str(path) if path is not None else request.get(field),
        code,
    )


def _validate_exact(
    checks: list[dict[str, Any]], request: Mapping[str, Any], field: str, expected: Any, code: str
) -> None:
    _add_check(checks, f"{field} exact", request.get(field) == expected, expected, request.get(field), code)


def _validate_non_claims(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    malformed = (
        list(REQUIRED_FALSE_NON_CLAIMS)
        if not isinstance(declared, Mapping)
        else [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    )
    _add_check(
        checks,
        "required non-claims false",
        not malformed,
        "mapping with every required false key exactly false",
        {"malformed_keys": malformed},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_top_level_postures(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if request.get(key) is True:
            code = _forbidden_posture_code(key)
            _add_check(checks, f"top-level required false posture {key} not pre-claimed", False, False, True, code)
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(key) is True:
            _add_check(
                checks,
                f"result-only posture {key} not pre-claimed",
                False,
                "resolver result posture only",
                True,
                "AUDIT_MATERIAL_MISSING_OR_INSUFFICIENT",
            )
    if request.get("audit_result") is not None:
        _add_check(
            checks,
            "audit_result is not pre-claimed",
            False,
            "resolver result posture only",
            request.get("audit_result"),
            "AUDIT_MATERIAL_MISSING_OR_INSUFFICIENT",
        )


def _forbidden_posture_code(key: str) -> str:
    if key in {"candidate_a_scope_declared", "candidate_b_scope_declared", "basis_bearing_scope_division_declared"}:
        return "PROHIBITED_SCOPE_DECLARATION_REQUESTED"
    if key == "basis_gap_closed":
        return "PROHIBITED_BASIS_GAP_CLOSURE_REQUESTED"
    if any(token in key for token in ("coupling", "third_candidate", "third_model")):
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if any(token in key for token in ("repair", "scan", "discovery", "validation", "unsupported", "overwrite", "edited", "deleted", "replaced", "redeemed")):
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    if any(token in key for token in ("standing", "distinct", "descendant_body")):
        return "PROHIBITED_DISTINCTNESS_OR_STANDING_REQUESTED"
    if key.startswith("direct_audit") or key.startswith("direct_accepted"):
        return "PROHIBITED_AUDIT_TO_STANDING_REQUESTED"
    return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"


def _validate_prohibited_requests(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)
    _add_check(checks, "return_raw_material_body not requested", request.get("return_raw_material_body") is not True, False, request.get("return_raw_material_body"), "REQUESTED_RAW_MATERIAL_BODY_RETURN")
    _add_check(checks, "return_raw_markdown_body not requested", request.get("return_raw_markdown_body") is not True, False, request.get("return_raw_markdown_body"), "REQUESTED_RAW_MARKDOWN_BODY_RETURN")


def _validate_metadata(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("received_material_filename", AUDITED_MATERIAL_EXPECTED_FILENAME),
        ("received_material_version", AUDITED_MATERIAL_EXPECTED_VERSION),
        ("received_material_date", AUDITED_MATERIAL_EXPECTED_DATE),
        ("received_material_author", AUDITED_MATERIAL_EXPECTED_AUTHOR),
        ("received_material_signature_role", AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE),
        ("received_material_predecessor", AUDITED_MATERIAL_EXPECTED_PREDECESSOR),
        ("received_material_predecessor_role", AUDITED_MATERIAL_PREDECESSOR_ROLE),
        ("received_material_status", UPSTREAM_RECEIPT_STATUS_REQUIRED),
        ("contribution_map_present", True),
        ("sibling_non_monarchy_present", True),
        ("receipt_sealing_posture_present", True),
        ("coupling_not_assigned_present", True),
        ("no_third_model_present", True),
        ("lineage_constraints_present", True),
        ("for_audit_only", True),
    )
    malformed = [field for field, value in expected if request.get(field) != value]
    _add_check(
        checks,
        "required received V2 metadata exact",
        not malformed,
        "all required received V2 metadata fields",
        {"malformed_fields": malformed},
        "MATERIAL_METADATA_MISSING_OR_INVALID",
    )


def _marker_classes_present(text: str | None) -> tuple[bool, list[str]]:
    if text is None:
        return False, [name for name, _ in OPERATION_SPEC_MARKER_CLASSES]
    missing = [name for name, markers in OPERATION_SPEC_MARKER_CLASSES if not all(marker in text for marker in markers)]
    return not missing, missing


def _validate_operation_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    text = _read_declared_text(request.get("operation_spec_reference"))
    passed, missing = _marker_classes_present(text)
    _add_check(
        checks,
        "target audit operation spec posture classes present",
        passed,
        "all required audit operation spec posture classes",
        {"missing_posture_classes": missing},
        "AUDIT_OPERATION_SPEC_MARKER_MISSING",
    )


def _validate_upstream_markers(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for field, _, missing_code, marker_code, markers, flag in UPSTREAM_REQUIREMENTS:
        text = _read_declared_text(request.get(field))
        passed = text is not None and all(marker in text for marker in markers)
        _add_check(
            checks,
            f"{field} expected markers present",
            passed,
            markers,
            {"reference_readable": text is not None, "missing_markers": [] if passed else list(markers)},
            missing_code if text is None else marker_code,
        )
        flags[flag] = passed
    return flags


def _normalized_strings(value: Any) -> tuple[str, ...]:
    if isinstance(value, Mapping):
        return tuple(item for nested in value.values() for item in _normalized_strings(nested))
    if isinstance(value, (list, tuple, set)):
        return tuple(item for nested in value for item in _normalized_strings(nested))
    if isinstance(value, str):
        return (" ".join(value.lower().split()),)
    if isinstance(value, bool):
        return ("true" if value else "false",)
    return ()


def _bounded_audit_fields(request: Mapping[str, Any]) -> dict[str, Any]:
    declared = request.get("bounded_audit_fields")
    fields = copy.deepcopy(dict(declared)) if isinstance(declared, Mapping) else {}
    for key in _audit_field_names():
        if key in request:
            fields[key] = copy.deepcopy(request[key])
    return fields


def _audit_field_names() -> tuple[str, ...]:
    return (
        "candidate_a_scope_name", "candidate_a_mandate", "candidate_a_responsibility",
        "candidate_b_scope_name", "candidate_b_mandate", "candidate_b_responsibility",
        "candidate_a_governed_surface", "candidate_b_governed_surface",
        "scope_division_statement", "motion_regulation_difference",
        "sibling_non_monarchy_statement", "coupling_statement", "no_third_model_statement",
        "lineage_statement", "non_standing_preservation_statement",
    )


def _contains_all(value: Any, fragments: tuple[str, ...]) -> bool:
    haystack = " ".join(_normalized_strings(value))
    return all(fragment.lower() in haystack for fragment in fragments)


def _evaluate_audit_criteria(fields: Mapping[str, Any]) -> dict[str, bool]:
    candidate_a = _contains_all(fields.get("candidate_a_scope_name"), ("motion", "variation")) and _contains_all(fields.get("candidate_a_mandate"), ("motion", "mandate")) and _contains_all(fields.get("candidate_a_responsibility"), ("variation", "frequency", "rhythm", "phase", "amplitude", "periodicity", "latency", "no fixed values", "no targets", "no optimization", "no preferred trajectory", "no steering"))
    candidate_b = _contains_all(fields.get("candidate_b_scope_name"), ("regulation", "admissibility")) and _contains_all(fields.get("candidate_b_mandate"), ("regulation", "mandate")) and _contains_all(fields.get("candidate_b_responsibility"), ("bounds", "coherence", "stability", "persistence", "damping", "modulation", "threshold", "range", "rejection", "no outcome encoding", "no constants", "no deciding trajectories", "no replacing motion with control"))
    scope_division = _contains_all(fields.get("scope_division_statement"), ("candidate a", "variation", "candidate b", "admissibility", "do not perform the same function", "neither role", "substitute", "freezing", "collapse"))
    difference = _contains_all(fields.get("motion_regulation_difference"), ("mandate", "function", "responsibility", "governed surface"))
    sibling = _contains_all(fields.get("sibling_non_monarchy_statement"), ("sibling", "non-standing", "neither candidate ranks above", "motion is not subordinate", "regulation is not sovereign", "motion does not override", "not hierarchical"))
    coupling = _contains_all(fields.get("coupling_statement"), ("not assigned", "not a third candidate", "not a third model", "not a standing body", "not created", "separately bounded"))
    no_third = _contains_all(fields.get("no_third_model_statement"), ("no third candidate", "no third model"))
    lineage = _contains_all(fields.get("lineage_statement"), ("lineage", "no orphaned state", "no silent reset", "no overwrite", "additive", "reference prior state", "v2 does not erase v1"))
    non_standing = _contains_all(fields.get("non_standing_preservation_statement"), ("audit", "proposed basis", "no standing", "no descendant-body creation", "no crossing", "no relation", "no field machinery", "no runtime", "no currentness", "no authority", "no follow-on work", "no candidate-specific content emission", "no seal material", "no lineage receipt material", "no digest material", "no basis-emission operation rerun", "no distinctness operation rerun", "no candidate records marked distinct", "no candidate standing"))
    return {
        "candidate_a_non_cosmetic_scope_declaration": candidate_a,
        "candidate_b_non_cosmetic_scope_declaration": candidate_b,
        "basis_bearing_scope_division": scope_division,
        "motion_regulation_difference_by_mandate_function_responsibility_governed_surface": difference,
        "sibling_non_monarchy": sibling,
        "coupling_not_assigned": coupling,
        "no_third_model": no_third,
        "lineage_constraints": lineage,
        "non_standing_preservation": non_standing,
    }


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    names = {"target_audit_operation_spec_markers_present": "target audit operation spec posture classes present"}
    names.update({flag: f"{field} expected markers present" for field, *_, flag in UPSTREAM_REQUIREMENTS})
    return {key: any(check.get("check_name") == name and check.get("passed") is True for check in checks) for key, name in names.items()}


def _operation_object(
    request: Mapping[str, Any], outcome: str, criteria: Mapping[str, bool], flags: Mapping[str, bool]
) -> dict[str, Any]:
    completed = outcome == OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS
    evaluated = outcome in (OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS, OUTCOME_REQUIRES_ADDITIONAL_BASIS)
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_audit_operation_id": OPERATION_ID,
        "authored_scope_division_declaration_audit_operation_type": OPERATION_TYPE,
        "authored_scope_division_declaration_audit_operation_version": OPERATION_VERSION,
        "authored_scope_division_declaration_audit_operation_scope": OPERATION_SCOPE,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE,
        "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
        "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "received_material_filename": AUDITED_MATERIAL_EXPECTED_FILENAME,
        "received_material_version": AUDITED_MATERIAL_EXPECTED_VERSION,
        "received_material_date": AUDITED_MATERIAL_EXPECTED_DATE,
        "received_material_author": AUDITED_MATERIAL_EXPECTED_AUTHOR,
        "received_material_signature_role": AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
        "received_material_predecessor": AUDITED_MATERIAL_EXPECTED_PREDECESSOR,
        "received_material_predecessor_role": AUDITED_MATERIAL_PREDECESSOR_ROLE,
        "received_material_status": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "contribution_map_present": request.get("contribution_map_present") is True,
        "sibling_non_monarchy_present": request.get("sibling_non_monarchy_present") is True,
        "receipt_sealing_posture_present": request.get("receipt_sealing_posture_present") is True,
        "coupling_not_assigned_present": request.get("coupling_not_assigned_present") is True,
        "no_third_model_present": request.get("no_third_model_present") is True,
        "lineage_constraints_present": request.get("lineage_constraints_present") is True,
        "for_audit_only": request.get("for_audit_only") is True,
        **_canonical_non_claims(),
        **flags,
    }
    operation.update(
        {
            "audit_operation_recorded": evaluated,
            "audit_performed": evaluated,
            "audit_result_recorded": evaluated,
            "audit_result": "SATISFIES_MISSING_BASIS_REQUIREMENTS" if completed else ("REQUIRES_ADDITIONAL_BASIS" if evaluated else "NOT_AUDITED"),
            "declaration_accepted_as_basis": completed,
        }
    )
    for criterion in AUDIT_CRITERIA:
        operation[AUDITED_FIELD_BY_CRITERION[criterion]] = evaluated
        operation[SATISFIED_FIELD_BY_CRITERION[criterion]] = bool(completed and criteria.get(criterion))
    return operation


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_authored_scope_division_declaration_audit_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("authored_scope_division_declaration_audit_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(1 for check in records if isinstance(check, Mapping) and check.get("passed") is False),
        "passed_check_count": sum(1 for check in records if isinstance(check, Mapping) and check.get("passed") is True),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": operation_map.get("operation_id"),
        "operation_type": operation_map.get("operation_type"),
        "operation_version": operation_map.get("operation_version"),
        "operation_scope": operation_map.get("operation_scope"),
        "upstream_receipt_operation_type": operation_map.get("upstream_receipt_operation_type"),
        "upstream_receipt_operation_outcome_required": operation_map.get("upstream_receipt_operation_outcome_required"),
        "upstream_receipt_status_required": operation_map.get("upstream_receipt_status_required"),
        "selected_target_spec_path": upstream_map.get("operation_spec_reference"),
        "completed_receipt_operation_terminal_summary_path": upstream_map.get("receipt_operation_terminal_summary_reference"),
        "completed_scope_division_operation_terminal_summary_path": upstream_map.get("scope_division_declaration_operation_terminal_summary_reference"),
        "missing_or_insufficient_audit_criteria": result.get("audit_result_detail", {}).get("missing_or_insufficient_audit_criteria", []),
        "result_level_non_claims_canonical_false": all(isinstance(result.get("non_claims"), Mapping) and result["non_claims"].get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
    }
    for key in (
        "received_material_filename", "received_material_version", "received_material_date", "received_material_author", "received_material_signature_role", "received_material_predecessor", "received_material_predecessor_role", "received_material_status", "audit_result", "declaration_accepted_as_basis", "audit_operation_recorded", "audit_performed", "audit_result_recorded", *AUDITED_FIELD_BY_CRITERION.values(), *SATISFIED_FIELD_BY_CRITERION.values(), *REQUIRED_FALSE_NON_CLAIMS, *[flag for *_, flag in UPSTREAM_REQUIREMENTS], "target_audit_operation_spec_markers_present",
    ):
        summary[key] = operation_map.get(key)
    return _sanitize(summary)


def build_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return a compact, sanitized audit-operation result summary."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    criteria: Mapping[str, bool],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(request, outcome, criteria, flags)
    missing = [criterion for criterion in AUDIT_CRITERIA if not criteria.get(criterion)]
    result: dict[str, Any] = {
        "authored_scope_division_declaration_audit_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_authored_scope_division_declaration_audit_operation_basis": _sanitize(request),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "descendant_body_candidate_authored_scope_division_declaration_audit_operation": operation,
        "authored_scope_division_declaration_audit_operation_checks": checks,
        "authored_scope_division_declaration_audit_operation_statement": {
            "outcome": outcome,
            "audit_operation_recorded": operation["audit_operation_recorded"],
            "audit_performed": operation["audit_performed"],
            "audit_result_recorded": operation["audit_result_recorded"],
            "audit_result": operation["audit_result"],
            "declaration_accepted_as_basis": operation["declaration_accepted_as_basis"],
            "declaration_admitted_as_standing_basis": False,
            "result_level_non_claims_canonical_false": True,
        },
        "authored_scope_division_declaration_audit_operation_non_meaning": {
            "not_standing_basis": True,
            "not_scope_declaration": True,
            "not_basis_gap_closure": True,
            "not_candidate_specific_basis_emission": True,
            "not_distinctness_support": True,
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_relation": True,
            "not_runtime": True,
            "not_currentness": True,
            "not_authority": True,
            "not_coupling": True,
            "not_third_candidate_or_model": True,
            "not_follow_on": True,
        },
        "audit_criteria": {criterion: bool(criteria.get(criterion)) for criterion in AUDIT_CRITERIA},
        "audit_result_detail": {
            "audit_result": operation["audit_result"],
            "missing_or_insufficient_audit_criteria": missing if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS else [],
            "bounded_structured_fields_only": True,
        },
        "permitted_future_route": [
            "audit may evaluate only the nine bounded criteria",
            "only a separately bounded successor closure may consider the gap after a satisfying audit",
            "this audit operation authorizes no successor by itself",
        ],
        "blocked_routes": [
            "standing, scope declaration, basis-gap closure, distinctness, candidate standing, descendant-body, relation, runtime, coupling, third-model, and follow-on conversion routes",
            "repository scan, affected-file repair, and prior unsupported-claim validation routes",
        ],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
            "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["authored_scope_division_declaration_audit_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(request: Mapping[str, Any], checks: list[dict[str, Any]], code: str, reason: str) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, {}, code, reason)


def _default_bounded_audit_fields() -> dict[str, Any]:
    return {
        "candidate_a_scope_name": "Motion-side admissible variation",
        "candidate_a_mandate": "Motion mandate",
        "candidate_a_responsibility": ["preserve variation", "frequency", "rhythm", "phase", "amplitude", "periodicity", "latency", "no fixed values", "no targets", "no optimization", "no preferred trajectory", "no steering"],
        "candidate_b_scope_name": "Regulation-side admissibility bounds",
        "candidate_b_mandate": "Regulation mandate",
        "candidate_b_responsibility": ["preserve bounds without collapsing motion", "coherence", "stability", "persistence", "damping", "modulation", "thresholds", "ranges", "rejection conditions", "no outcome encoding", "no constants", "no deciding trajectories", "no replacing motion with control"],
        "scope_division_statement": "Candidate A governs the variation side of the parent basis. Candidate B governs the admissibility-bound side of the parent basis. Motion and Regulation do not perform the same function. Neither role may lawfully substitute for the other without freezing the system or allowing collapse.",
        "motion_regulation_difference": "Difference is declared by mandate, function, responsibility, and governed surface.",
        "sibling_non_monarchy_statement": "Candidate A and Candidate B are sibling non-standing candidate records. Neither candidate ranks above the other. Motion is not subordinate to Regulation. Regulation is not sovereign over Motion. Motion does not override Regulation. The division is directional only in function, not hierarchical in rank.",
        "coupling_statement": "Coupling is not assigned to either candidate, not a third candidate, not a third model, not a standing body, and not created by declaration or audit. Coupling may only appear later if separately bounded.",
        "no_third_model_statement": "No third candidate and no third model are admitted.",
        "lineage_statement": "Lineage remains required. No orphaned state, no silent reset, and no overwrite are allowed. Later evolution must be additive and reference prior state. V2 does not erase V1.",
        "non_standing_preservation_statement": "The declaration is for audit and proposed basis only: no standing, no descendant-body creation, no crossing, no relation, no FIELD machinery, no runtime, no currentness, no authority, no follow-on work, no candidate-specific content emission, no seal material, no lineage receipt material, no digest material, no basis-emission operation rerun, no distinctness operation rerun, no candidate records marked distinct, and no candidate standing.",
    }


def build_declared_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build a bounded, structured audit request without raw material content."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "authored_scope_division_declaration_audit_operation_id": OPERATION_ID,
        "authored_scope_division_declaration_audit_operation_type": OPERATION_TYPE,
        "authored_scope_division_declaration_audit_operation_version": OPERATION_VERSION,
        "authored_scope_division_declaration_audit_operation_scope": OPERATION_SCOPE,
        "upstream_receipt_operation_type": UPSTREAM_RECEIPT_OPERATION_TYPE,
        "upstream_receipt_operation_outcome_required": UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED,
        "upstream_receipt_status_required": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "received_material_filename": AUDITED_MATERIAL_EXPECTED_FILENAME,
        "received_material_version": AUDITED_MATERIAL_EXPECTED_VERSION,
        "received_material_date": AUDITED_MATERIAL_EXPECTED_DATE,
        "received_material_author": AUDITED_MATERIAL_EXPECTED_AUTHOR,
        "received_material_signature_role": AUDITED_MATERIAL_EXPECTED_SIGNATURE_ROLE,
        "received_material_predecessor": AUDITED_MATERIAL_EXPECTED_PREDECESSOR,
        "received_material_predecessor_role": AUDITED_MATERIAL_PREDECESSOR_ROLE,
        "received_material_status": UPSTREAM_RECEIPT_STATUS_REQUIRED,
        "contribution_map_present": True,
        "sibling_non_monarchy_present": True,
        "receipt_sealing_posture_present": True,
        "coupling_not_assigned_present": True,
        "no_third_model_present": True,
        "lineage_constraints_present": True,
        "for_audit_only": True,
        "bounded_audit_fields": _default_bounded_audit_fields(),
        "declared_non_claims": _canonical_non_claims(),
        "return_raw_material_body": False,
        "return_raw_markdown_body": False,
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    aliases = {
        "target_spec_path": "operation_spec_reference",
        "operation_spec_path": "operation_spec_reference",
        "receipt_operation_terminal_summary_path": "receipt_operation_terminal_summary_reference",
        "scope_division_declaration_operation_terminal_summary_path": "scope_division_declaration_operation_terminal_summary_reference",
    }
    for alias, target in aliases.items():
        if alias in overrides and target not in overrides:
            overrides[target] = overrides[alias]
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(
    declared_authored_scope_division_declaration_audit_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded audit result from declared structured evidence only."""

    if declared_authored_scope_division_declaration_audit_operation is None:
        request = build_declared_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_request()
    elif not isinstance(declared_authored_scope_division_declaration_audit_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request mapping", False, "mapping", type(declared_authored_scope_division_declaration_audit_operation).__name__, "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_authored_scope_division_declaration_audit_operation))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    exact_fields = (
        ("operation_id", OPERATION_ID),
        ("operation_type", OPERATION_TYPE),
        ("operation_version", OPERATION_VERSION),
        ("operation_scope", OPERATION_SCOPE),
        ("authored_scope_division_declaration_audit_operation_id", OPERATION_ID),
        ("authored_scope_division_declaration_audit_operation_type", OPERATION_TYPE),
        ("authored_scope_division_declaration_audit_operation_version", OPERATION_VERSION),
        ("authored_scope_division_declaration_audit_operation_scope", OPERATION_SCOPE),
        ("upstream_receipt_operation_type", UPSTREAM_RECEIPT_OPERATION_TYPE),
        ("upstream_receipt_operation_outcome_required", UPSTREAM_RECEIPT_OPERATION_OUTCOME_REQUIRED),
        ("upstream_receipt_status_required", UPSTREAM_RECEIPT_STATUS_REQUIRED),
        ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
    )
    for field, expected in exact_fields:
        _validate_exact(checks, request, field, expected, "MATERIAL_METADATA_MISSING_OR_INVALID")

    _validate_reference(checks, request, "operation_spec_reference", "AUDIT_OPERATION_SPEC_REFERENCE_MISSING")
    _validate_operation_spec(checks, request)
    for field, _, missing_code, _, _, _ in UPSTREAM_REQUIREMENTS:
        _validate_reference(checks, request, field, missing_code)
    _validate_upstream_markers(checks, request)
    _validate_metadata(checks, request)
    _validate_non_claims(checks, request)
    _validate_top_level_postures(checks, request)
    _validate_prohibited_requests(checks, request)

    fields = _bounded_audit_fields(request)
    _add_check(checks, "bounded audit fields mapping", isinstance(request.get("bounded_audit_fields"), Mapping), "bounded audit field mapping", type(request.get("bounded_audit_fields")).__name__, "AUDIT_MATERIAL_MISSING_OR_INSUFFICIENT")
    criteria = _evaluate_audit_criteria(fields)
    for criterion, satisfied in criteria.items():
        _add_check(checks, f"audit criterion {criterion} bounded evidence sufficient", satisfied, True, satisfied, None)

    _add_check(checks, "result-level required false non-claims canonical false", True, "canonical final false non-claims", "canonical false emitted by resolver")
    failed_codes = _failed_codes(checks)
    if failed_codes:
        return _blocked_result(request, checks, failed_codes[0], f"blocked by failed check {failed_codes[0]}")
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, {}, None, None)
    if all(criteria.values()):
        return _build_result(request, OUTCOME_SATISFIES_MISSING_BASIS_REQUIREMENTS, checks, criteria)
    return _build_result(request, OUTCOME_REQUIRES_ADDITIONAL_BASIS, checks, criteria)


def resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_from_path(
    declared_authored_scope_division_declaration_audit_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_authored_scope_division_declaration_audit_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min(request)


def write_descendant_body_candidate_authored_scope_division_declaration_audit_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write deterministic sanitized JSON without overwriting prior results."""

    if output_path is None:
        path = REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    else:
        candidate = Path(output_path)
        base = candidate if candidate.is_absolute() else REPO_ROOT / candidate
        path = base if base.suffix else base / DETERMINISTIC_FILENAME
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        final_path = path
        suffix = 1
        while final_path.exists():
            final_path = path.with_name(f"{path.stem}_{suffix:03d}{path.suffix}")
            suffix += 1
        with final_path.open("w", encoding="utf-8") as handle:
            json.dump(_json_ready(_sanitize(result)), handle, ensure_ascii=True, indent=2, sort_keys=True)
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCandidateAuthoredScopeDivisionDeclarationAuditOperationV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
