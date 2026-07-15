"""Resolve one bounded descendant-body candidate-standing boundary result.

This resolver records only a candidate-standing boundary after a declared,
completed distinctness-support recheck. It permits consideration of a separate
future operation only. It does not perform standing checks or create standing,
bodies, relations, runtime, authority, coupling, presence, identity, repair,
discovery, validation enforcement, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateStandingBoundaryV0MinError(Exception):
    """Raised when bounded candidate-standing boundary result writing fails."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_standing_boundary_v0_min"

BOUNDARY_ID = "descendant_body_candidate_standing_boundary_001"
BOUNDARY_TYPE = "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_CANDIDATE_STANDING_AFTER_SUPPORTED_DISTINCTNESS_ONLY"
PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION"
)
PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_SUPPORTED"
)
PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED = "DISTINCTNESS_SUPPORT_RECHECKED"
PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED = "DISTINCTNESS_SUPPORTED"
PRIOR_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED = True
PRIOR_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED = True
PRIOR_CANDIDATE_RECORDS_DISTINCT_REQUIRED = True
PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED = False
PRIOR_DESCENDANT_BODY_CREATED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_STANDING_BOUNDARY_THEN_CANDIDATE_STANDING_OPERATION_ONLY"
)

CANDIDATE_A_BASIS_ID = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
)
CANDIDATE_B_BASIS_ID = (
    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
)
BASIS_PAIR_SCOPE = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"

OUTCOME_ALLOWED = "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_REQUIRES_SUPPORTED_DISTINCTNESS"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_boundary_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_candidate_standing_boundary_001__candidate_standing_boundary_v0_min_result.json"
)

DEFAULT_CANDIDATE_STANDING_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "candidate_standing_boundary_recorded",
    "candidate_standing_boundary_result_recorded",
    "candidate_standing_operation_consideration_allowed",
    "supported_distinctness_referenced",
    "candidate_records_distinct_referenced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_standing_check_performed",
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
    "presence_established",
    "identity_created",
    "follow_on_authorized",
    "follow_on_work_authorized",
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
    "distinctness_support_recheck_operation_overridden",
    "distinctness_support_recheck_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_candidate_standing_boundary_to_candidate_standing_operation_completion",
    "direct_supported_distinctness_to_candidate_standing",
    "direct_supported_distinctness_to_descendant_body_creation",
    "direct_supported_distinctness_to_relation",
    "direct_supported_distinctness_to_presence",
    "direct_supported_distinctness_to_identity",
    "direct_candidate_records_distinct_to_candidate_standing",
    "direct_candidate_records_distinct_to_descendant_body_creation",
    "direct_candidate_records_distinct_to_relation",
    "direct_candidate_records_distinct_to_presence",
    "direct_candidate_records_distinct_to_identity",
    "direct_candidate_standing_boundary_to_descendant_body_creation",
    "direct_candidate_standing_boundary_to_crossing",
    "direct_candidate_standing_boundary_to_relation",
    "direct_candidate_standing_boundary_to_runtime",
    "direct_candidate_standing_boundary_to_authority_currentness",
    "direct_candidate_standing_boundary_to_coupling_creation",
    "direct_candidate_standing_boundary_to_third_candidate_route",
    "direct_candidate_standing_boundary_to_third_model_route",
    "direct_candidate_standing_boundary_to_presence",
    "direct_candidate_standing_boundary_to_identity",
    "direct_candidate_standing_boundary_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "CANDIDATE_STANDING_BOUNDARY_SPEC_REFERENCE_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_SPEC_MARKER_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUPPORTED_DISTINCTNESS_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_CANDIDATE_STANDING_CHECK_REQUESTED",
    "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_candidate_standing_check": "PROHIBITED_CANDIDATE_STANDING_CHECK_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_candidate_standing_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_a_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_b_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_standing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_CANDIDATE_STANDING_CHECK_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_first_crossing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_identity_creation": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_follow_on_work_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

EXPECTED_REQUEST_VALUES = {
    "boundary_id": BOUNDARY_ID,
    "boundary_type": BOUNDARY_TYPE,
    "boundary_version": BOUNDARY_VERSION,
    "boundary_scope": BOUNDARY_SCOPE,
    "candidate_standing_boundary_id": BOUNDARY_ID,
    "candidate_standing_boundary_type": BOUNDARY_TYPE,
    "candidate_standing_boundary_version": BOUNDARY_VERSION,
    "candidate_standing_boundary_scope": BOUNDARY_SCOPE,
    "prior_distinctness_support_recheck_operation_type": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE,
    "prior_distinctness_support_recheck_operation_outcome_required": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED,
    "prior_distinctness_support_recheck_result_required": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED,
    "prior_distinctness_support_result_required": PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED,
    "prior_distinctness_supported_recorded_required": PRIOR_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED,
    "prior_candidate_records_marked_distinct_required": PRIOR_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED,
    "prior_candidate_records_distinct_required": PRIOR_CANDIDATE_RECORDS_DISTINCT_REQUIRED,
    "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
    "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "candidate_a_basis_id_required": CANDIDATE_A_BASIS_ID,
    "candidate_b_basis_id_required": CANDIDATE_B_BASIS_ID,
    "basis_pair_scope_required": BASIS_PAIR_SCOPE,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

BOUNDARY_SPEC_MARKER_CLASSES = (
    ("boundary_identity", ((
        "Descendant Body Candidate Standing Boundary V0 Minimum Specification",
        BOUNDARY_TYPE,
        BOUNDARY_ID,
        BOUNDARY_SCOPE,
    ),)),
    ("supported_distinctness_basis", ((
        PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED,
        PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED,
        PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED,
        "distinctness_supported_recorded = true",
        "candidate_records_marked_distinct = true",
        "candidate_records_distinct = true",
    ),)),
    ("non_standing_candidate_records", ((
        "candidate records marked distinct still not standing candidates",
        "candidate records marked distinct still not standing candidates, descendant bodies, relation participants, presence-bearing, or identity-bearing",
        "Candidate records marked distinct remain non-standing candidate records",
    ),)),
    ("prior_false_posture", ((
        "candidate_standing_authorized = false",
        "descendant_body_created = false",
        "relation_created = false",
        "coupling_created = false",
        "presence_established = false",
        "identity_created = false",
        "follow_on_authorized = false",
    ),)),
    ("candidate_basis_references", ((
        CANDIDATE_A_BASIS_ID,
        CANDIDATE_B_BASIS_ID,
        "both non-standing at emission time",
        BASIS_PAIR_SCOPE,
        "basis-pair non-hierarchy preserved",
    ),)),
    ("permitted_results", ((
        OUTCOME_ALLOWED,
        OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS,
        OUTCOME_BLOCKED,
        "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
        "REQUIRES_SUPPORTED_DISTINCTNESS",
    ),)),
    ("non_conversion", ((
        "Candidate-standing boundary is not candidate-standing operation",
        "Candidate-standing boundary permission is not candidate-standing completion",
        "Candidate-standing operation consideration is not candidate standing",
        "Supported distinctness is not candidate standing",
        "Candidate records distinct is not candidate standing",
        "Candidate records distinct is not descendant-body creation",
        "Candidate records distinct is not relation",
        "Candidate records distinct is not presence",
        "Candidate records distinct is not identity",
    ),)),
    ("sibling_non_hierarchy", ((
        "Candidate A and Candidate B remain sibling non-standing candidate records",
        "sibling non-standing basis materials",
        "Neither ranks above the other",
        "Regulation may not become sovereign over Motion",
        "Motion may not erase Regulation",
        "Coupling remains unassigned",
    ),)),
    ("permitted_route", ((
        ADMISSIBLE_FUTURE_ROUTE,
        "Only after a future boundary records CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED may a separately bounded candidate-standing operation be considered",
        "No later operation is authorized by this specification alone",
    ),)),
    ("contaminated_lineage", ((
        "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage",
        "descendant_body_basis_candidate_a_created = true",
        "descendant_body_basis_candidate_b_created = true",
        "descendant_body_basis_derivation_event_recorded = true",
        "UNSUPPORTED",
        "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
    ),)),
    ("blocked_routes", ((
        "direct candidate-standing boundary to candidate-standing operation completion",
        "direct supported distinctness or candidate records distinct to candidate standing, descendant-body creation, relation, presence, or identity",
        "direct candidate-standing boundary to descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, or follow-on work",
        "repository scan; file discovery; affected-file repair; and prior unsupported-claim validation",
    ),)),
    ("closing_lock", ((
        "This boundary spec defines only a future candidate-standing boundary shape",
        "It does not perform candidate-standing checks",
        "Candidate-standing boundary is not candidate-standing operation",
        "Candidate-standing operation consideration is not candidate standing",
        "Supported distinctness is not candidate standing",
        "Candidate records distinct is not candidate standing",
        "Candidate records marked distinct remain non-standing candidate records",
        "Only after a future boundary records CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED may a separately bounded candidate-standing operation be considered",
        "Open means not scheduled, not authorized, and not executed",
    ),)),
)

UPSTREAM_REQUIREMENTS = (
    (
        "distinctness_support_recheck_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 96",
            PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED,
            PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED,
            "distinctness_supported_recorded = true",
            "candidate_records_marked_distinct = true",
            "candidate_records_distinct = true",
            "Candidate records marked distinct are still not standing candidates",
            "Distinctness support is not candidate standing",
            "candidate_standing_authorized = false",
            "descendant_body_created = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "distinctness_support_recheck_terminal_summary_markers_present",
        True,
    ),
    (
        "successor_basis_emission_terminal_summary_reference",
        DEFAULT_SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_BASIS_EMISSION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED",
            "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
        ),),
        "successor_basis_emission_terminal_summary_markers_present",
        False,
    ),
    (
        "prior_distinctness_operation_terminal_summary_reference",
        DEFAULT_PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRIOR_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",),),
        "prior_distinctness_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("UNSUPPORTED",),),
        "existence_claim_evidence_check_terminal_summary_markers_present",
        False,
    ),
    (
        "basis_emission_operation_terminal_summary_reference",
        DEFAULT_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),),
        "basis_emission_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "successor_closure_operation_terminal_summary_reference",
        DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED",),),
        "successor_closure_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "scope_division_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),),
        "scope_division_operation_terminal_summary_markers_present",
        False,
    ),
)

WHAT_REMAINS_OPEN = (
    "candidate-standing operation, if separately bounded after boundary allowance",
    "candidate-standing checks",
    "divergent receipt-history route, if separately bounded",
    "carrier separation route, if separately bounded",
    "first crossing",
    "relation",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "presence boundary",
    "identity boundary",
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


def _resolve_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        path = value
    elif isinstance(value, str) and value.strip():
        path = Path(value)
    else:
        return None
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(value: Any) -> str | None:
    path = _resolve_path(value)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except OSError:
        return None


def _is_sensitive_key(key: str) -> bool:
    normalized = key.casefold()
    return normalized.startswith("raw_") or normalized.endswith("_body") or normalized in {
        "payload", "file_bytes", "full_body", "full_text", "source_body",
    }


def _sanitize(value: Any, key: str = "") -> Any:
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(name): _sanitize(item, str(name)) for name, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _is_sensitive_key(key) and value.strip():
            return "[REDACTED_SENSITIVE_BODY]"
        return value if len(value) <= 4096 else f"{value[:4096]}...[truncated]"
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
    upstream: bool = False,
) -> None:
    check: dict[str, Any] = {
        "check_name": name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected),
        "actual_posture": _sanitize(actual),
        "upstream_basis_check": upstream,
    }
    if not passed and code:
        check["block_code"] = code
        check["failure_code"] = code
    checks.append(check)


def _failed_codes(checks: list[dict[str, Any]], upstream: bool | None = None) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code"), str)
        and check["block_code"] in BLOCK_CODES
        and (upstream is None or check.get("upstream_basis_check") is upstream)
    ]


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for key, expected in EXPECTED_REQUEST_VALUES.items():
        _add_check(
            checks,
            f"declared {key} exact",
            request.get(key) == expected,
            expected,
            request.get(key),
            "UNSUPPORTED_INTENT",
        )


def _code_for_false_posture(key: str) -> str:
    if key in {"candidate_standing_check_performed", "descendant_standing_check_performed"}:
        return "PROHIBITED_CANDIDATE_STANDING_CHECK_REQUESTED"
    if key in {
        "candidate_standing_authorized", "candidate_standing_created",
        "descendant_body_a_created", "descendant_body_b_created", "descendant_body_created",
        "standing_authorized", "standing_descendant_created", "crossing_authorized",
        "first_crossing_authorized", "standing_created",
    }:
        return "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED"
    if key in {
        "relation_created", "field_machinery_created", "runtime_created", "api_created",
        "currentness_created", "authority_created",
    }:
        return "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED"
    if key in {
        "coupling_assigned_to_candidate_a", "coupling_assigned_to_candidate_b",
        "coupling_created", "third_candidate_created", "third_model_admitted",
    }:
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if key in {"presence_established", "identity_created"}:
        return "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED"
    if key in {
        "output_authorized", "action_authorized", "derivative_reception_authorized",
        "synchronization_authorized", "follow_on_authorized", "follow_on_work_authorized",
    }:
        return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"
    if key in {
        "scan_performed", "repository_scan_performed", "file_discovery_performed",
        "repair_performed", "validation_enforced", "hidden_repair_performed",
        "silent_overwrite_performed", "affected_file_repaired", "affected_file_edited",
        "affected_file_deleted", "affected_file_overwritten", "affected_file_replaced",
        "affected_file_redeemed", "prior_unsupported_candidate_a_claim_validated",
        "prior_unsupported_candidate_b_claim_validated",
        "prior_unsupported_derivation_event_claim_validated",
    }:
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "NON_CLAIM_MISSING_OR_FLIPPED"


def _validate_request_posture(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared_non_claims = request.get("declared_non_claims")
    if not isinstance(declared_non_claims, Mapping):
        _add_check(
            checks,
            "declared non-claims mapping",
            False,
            "mapping with canonical false posture",
            type(declared_non_claims).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    else:
        for key in REQUIRED_FALSE_NON_CLAIMS:
            value = declared_non_claims.get(key)
            _add_check(
                checks,
                f"declared non-claim {key} false",
                value is False,
                False,
                value,
                "NON_CLAIM_MISSING_OR_FLIPPED",
            )

    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if key in request:
            _add_check(
                checks,
                f"result posture {key} not pre-claimed",
                request.get(key) is False,
                False,
                request.get(key),
                "RESULT_POSTURE_PRECLAIMED",
            )
    if "candidate_standing_boundary_result" in request:
        _add_check(
            checks,
            "candidate-standing boundary result not pre-claimed",
            False,
            "resolver-derived boundary result only",
            request.get("candidate_standing_boundary_result"),
            "RESULT_POSTURE_PRECLAIMED",
        )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key in request:
            _add_check(
                checks,
                f"top-level false posture {key}",
                request.get(key) is False,
                False,
                request.get(key),
                _code_for_false_posture(key),
            )
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(
            checks,
            f"prohibited request flag {field} false",
            request.get(field) is False,
            False,
            request.get(field),
            code,
        )


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    reference = request.get("candidate_standing_boundary_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "candidate-standing boundary specification reference readable",
        text is not None,
        "readable declared specification",
        reference,
        "CANDIDATE_STANDING_BOUNDARY_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return
    for class_name, variants in BOUNDARY_SPEC_MARKER_CLASSES:
        _add_check(
            checks,
            f"candidate-standing boundary specification {class_name} markers present",
            _markers_present(text, variants),
            "posture marker class present",
            class_name,
            "CANDIDATE_STANDING_BOUNDARY_SPEC_MARKER_MISSING",
        )


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> list[str]:
    missing_supported_distinctness: list[str] = []
    for field, _, missing_code, marker_code, variants, flag, is_support_basis in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        readable = text is not None
        _add_check(
            checks,
            f"{field} readable",
            readable,
            "readable declared terminal summary",
            reference,
            missing_code,
            upstream=True,
        )
        markers_present = _markers_present(text, variants)
        _add_check(
            checks,
            f"{flag}",
            markers_present,
            "required terminal-summary posture markers",
            reference if text is None else flag,
            marker_code,
            upstream=True,
        )
        if is_support_basis and not markers_present:
            missing_supported_distinctness.append(flag)
    return missing_supported_distinctness


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for check in checks:
        name = check.get("check_name")
        if isinstance(name, str) and name.endswith("markers present"):
            flags[name.replace(" ", "_")] = check.get("passed") is True
    return flags


def _boundary_result_value(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED"
    if outcome == OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS:
        return "REQUIRES_SUPPORTED_DISTINCTNESS"
    if outcome == OUTCOME_BLOCKED:
        return "BLOCKED"
    return "NOT_RECORDED"


def _boundary_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    boundary: dict[str, Any] = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "candidate_standing_boundary_id": BOUNDARY_ID,
        "candidate_standing_boundary_type": BOUNDARY_TYPE,
        "candidate_standing_boundary_version": BOUNDARY_VERSION,
        "candidate_standing_boundary_scope": BOUNDARY_SCOPE,
        "prior_distinctness_support_recheck_operation_type": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE,
        "prior_distinctness_support_recheck_operation_outcome_required": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED,
        "prior_distinctness_support_recheck_result_required": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED,
        "prior_distinctness_support_result_required": PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED,
        "prior_distinctness_supported_recorded_required": PRIOR_DISTINCTNESS_SUPPORTED_RECORDED_REQUIRED,
        "prior_candidate_records_marked_distinct_required": PRIOR_CANDIDATE_RECORDS_MARKED_DISTINCT_REQUIRED,
        "prior_candidate_records_distinct_required": PRIOR_CANDIDATE_RECORDS_DISTINCT_REQUIRED,
        "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
        "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
        "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
        "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "candidate_a_basis_id_required": CANDIDATE_A_BASIS_ID,
        "candidate_b_basis_id_required": CANDIDATE_B_BASIS_ID,
        "basis_pair_scope_required": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(),
        **marker_flags,
    }
    boundary.update({
        "candidate_standing_boundary_recorded": allowed,
        "candidate_standing_boundary_result_recorded": allowed,
        "candidate_standing_boundary_result": _boundary_result_value(outcome),
        "candidate_standing_operation_consideration_allowed": allowed,
        "supported_distinctness_referenced": allowed,
        "candidate_records_distinct_referenced": allowed,
    })
    return boundary


def _boundary_material(supported_basis: bool, outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    return {
        "supported_distinctness_reference": {
            "prior_distinctness_support_recheck_operation_type": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TYPE,
            "prior_distinctness_support_recheck_operation_outcome": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_OUTCOME_REQUIRED,
            "prior_distinctness_support_recheck_result": PRIOR_DISTINCTNESS_SUPPORT_RECHECK_RESULT_REQUIRED,
            "prior_distinctness_support_result": PRIOR_DISTINCTNESS_SUPPORT_RESULT_REQUIRED,
            "prior_distinctness_supported_recorded": supported_basis,
            "prior_candidate_records_marked_distinct": supported_basis,
            "prior_candidate_records_distinct": supported_basis,
        },
        "candidate_records_reference": {
            "candidate_records_marked_distinct": supported_basis,
            "candidate_records_distinct": supported_basis,
            "candidate_records_are_standing_candidates": False,
            "candidate_records_are_descendant_bodies": False,
            "candidate_records_are_relation_participants": False,
            "candidate_records_are_presence_bearing": False,
            "candidate_records_are_identity_bearing": False,
            "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
            "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
            "basis_pair_scope": BASIS_PAIR_SCOPE,
            "basis_pair_non_hierarchy_preserved": supported_basis,
        },
        "boundary_evaluation": {
            "candidate_standing_operation_consideration_allowed": allowed,
            "candidate_standing_boundary_result": _boundary_result_value(outcome),
            "supported_distinctness_is_candidate_standing": False,
            "candidate_records_distinct_is_candidate_standing": False,
            "candidate_standing_check_performed": False,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
        },
    }


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("descendant_body_candidate_standing_boundary")
    details = boundary if isinstance(boundary, Mapping) else {}
    checks = result.get("candidate_standing_boundary_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    detail = result.get("boundary_result_detail")
    result_detail = detail if isinstance(detail, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            check.get("passed") is False for check in records if isinstance(check, Mapping)
        ),
        "passed_check_count": sum(
            check.get("passed") is True for check in records if isinstance(check, Mapping)
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "boundary_id": details.get("boundary_id"),
        "boundary_type": details.get("boundary_type"),
        "boundary_version": details.get("boundary_version"),
        "boundary_scope": details.get("boundary_scope"),
        "prior_distinctness_support_recheck_operation_type": details.get("prior_distinctness_support_recheck_operation_type"),
        "prior_distinctness_support_recheck_operation_outcome_required": details.get("prior_distinctness_support_recheck_operation_outcome_required"),
        "prior_distinctness_support_recheck_result_required": details.get("prior_distinctness_support_recheck_result_required"),
        "prior_distinctness_support_result_required": details.get("prior_distinctness_support_result_required"),
        "prior_candidate_records_marked_distinct_required": details.get("prior_candidate_records_marked_distinct_required"),
        "prior_candidate_records_distinct_required": details.get("prior_candidate_records_distinct_required"),
        "candidate_standing_boundary_result": details.get("candidate_standing_boundary_result"),
        "candidate_standing_operation_consideration_allowed": details.get("candidate_standing_operation_consideration_allowed"),
        "supported_distinctness_referenced": details.get("supported_distinctness_referenced"),
        "candidate_records_distinct_referenced": details.get("candidate_records_distinct_referenced"),
        "selected_target_spec_path": basis.get("candidate_standing_boundary_spec_reference"),
        "completed_distinctness_support_recheck_terminal_summary_path": basis.get("distinctness_support_recheck_terminal_summary_reference"),
        "missing_or_insufficient_supported_distinctness": result_detail.get("missing_or_insufficient_supported_distinctness", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, *REQUIRED_FALSE_NON_CLAIMS):
        summary[key] = details.get(key)
    for flag in _marker_flags(
        [check for check in records if isinstance(check, Mapping)]
    ):
        summary[flag] = details.get(flag)
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_supported_distinctness: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _marker_flags(checks)
    boundary = _boundary_object(outcome, marker_flags)
    supported_basis = not missing_supported_distinctness
    allowed = outcome == OUTCOME_ALLOWED
    result: dict[str, Any] = {
        "candidate_standing_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_candidate_standing_boundary_basis": _sanitize(request),
        "upstream_basis": {
            "candidate_standing_boundary_spec_reference": request.get("candidate_standing_boundary_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "descendant_body_candidate_standing_boundary": boundary,
        "candidate_standing_boundary_material": _boundary_material(supported_basis, outcome),
        "candidate_standing_boundary_checks": checks,
        "candidate_standing_boundary_statement": {
            "outcome": outcome,
            "candidate_standing_boundary_recorded": boundary["candidate_standing_boundary_recorded"],
            "candidate_standing_boundary_result_recorded": boundary["candidate_standing_boundary_result_recorded"],
            "candidate_standing_operation_consideration_allowed": boundary["candidate_standing_operation_consideration_allowed"],
            "supported_distinctness_referenced": boundary["supported_distinctness_referenced"],
            "candidate_records_distinct_referenced": boundary["candidate_records_distinct_referenced"],
            "candidate_standing_check_performed": False,
            "candidate_standing_authorized": False,
            "descendant_body_created": False,
            "result_level_non_claims_canonical_false": True,
        },
        "candidate_standing_boundary_non_meaning": {
            "not_candidate_standing_check": True,
            "not_candidate_standing": True,
            "not_descendant_body_creation": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_follow_on": True,
        },
        "boundary_result_detail": {
            "candidate_standing_boundary_result": boundary["candidate_standing_boundary_result"],
            "missing_or_insufficient_supported_distinctness": list(missing_supported_distinctness),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "candidate_standing_operation_requires_separate_bounded_step": True,
        },
        "blocked_routes": [
            "standing checks, standing, bodies, relation, runtime, authority, coupling, presence, identity, repair, discovery, validation, and downstream authorization",
        ],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
            "reason": block_reason if outcome == OUTCOME_BLOCKED else None,
        },
    }
    result["candidate_standing_boundary_summary"] = _build_summary(result)
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_supported_distinctness: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_supported_distinctness or [],
        code,
        reason,
    )


def build_declared_descendant_body_candidate_standing_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one declared, no-discovery request for the candidate-standing boundary."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "candidate_standing_boundary_spec_reference": DEFAULT_CANDIDATE_STANDING_BOUNDARY_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in ALLOWED_TRUE_RECORDED_FIELDS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_standing_boundary_v0_min(
    declared_candidate_standing_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one boundary result without standing checks or downstream conversion."""

    if declared_candidate_standing_boundary is None:
        request = build_declared_descendant_body_candidate_standing_boundary_v0_min_request()
    elif not isinstance(declared_candidate_standing_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_candidate_standing_boundary).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_candidate_standing_boundary))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(
        checks,
        "intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "UNSUPPORTED_INTENT",
    )
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    _validate_exact_values(checks, request)
    _validate_request_posture(checks, request)
    _validate_target_spec(checks, request)
    missing_supported_distinctness = _validate_upstream(checks, request)

    non_upstream_failures = _failed_codes(checks, upstream=False)
    if non_upstream_failures:
        code = non_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed check {code}",
            missing_supported_distinctness,
        )

    support_codes = {
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    }
    other_upstream_failures = [
        code for code in _failed_codes(checks, upstream=True) if code not in support_codes
    ]
    if other_upstream_failures:
        code = other_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed upstream check {code}",
            missing_supported_distinctness,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            missing_supported_distinctness,
        )
    if missing_supported_distinctness:
        return _build_result(
            request,
            OUTCOME_REQUIRES_SUPPORTED_DISTINCTNESS,
            checks,
            missing_supported_distinctness,
        )
    return _build_result(request, OUTCOME_ALLOWED, checks, [])


def resolve_descendant_body_candidate_standing_boundary_v0_min_from_path(
    declared_candidate_standing_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_candidate_standing_boundary_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request path readable JSON",
            False,
            "readable JSON object",
            str(exc),
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_standing_boundary_v0_min(request)


def build_descendant_body_candidate_standing_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact metadata for one bounded candidate-standing boundary."""

    return _build_summary(result)


def write_descendant_body_candidate_standing_boundary_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write deterministic sanitized JSON without silently overwriting files."""

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
        raise DescendantBodyCandidateStandingBoundaryV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
