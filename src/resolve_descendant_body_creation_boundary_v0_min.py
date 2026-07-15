"""Resolve one bounded descendant-body creation boundary result.

This resolver permits only consideration of a separately bounded future
descendant-body creation operation. It preserves candidate standing as prior
basis and does not create descendant bodies, relations, runtime, authority,
coupling, presence, identity, or downstream authorization.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCreationBoundaryV0MinError(Exception):
    """Raised when a bounded descendant-body boundary result cannot be written."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_creation_boundary_v0_min"

BOUNDARY_ID = "descendant_body_creation_boundary_001"
BOUNDARY_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY"
PRIOR_CANDIDATE_STANDING_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED"
)
PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED = "CANDIDATE_STANDING_SUPPORTED"
PRIOR_CANDIDATE_STANDING_SUPPORTED_REQUIRED = True
PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED = True
PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED = True
PRIOR_CANDIDATE_A_STANDING_CREATED_REQUIRED = True
PRIOR_CANDIDATE_B_STANDING_CREATED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_DESCENDANT_BODY_CREATION_OPERATION_ONLY"
)

OUTCOME_ALLOWED = "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_CANDIDATE_STANDING = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUIRES_CANDIDATE_STANDING"
)
OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CREATION_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_CANDIDATE_STANDING,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CREATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CREATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_boundary_v0_min"
)
DETERMINISTIC_FILENAME = (
    "descendant_body_creation_boundary_001__descendant_body_creation_boundary_v0_min_result.json"
)

DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "descendant_body_creation_boundary_recorded",
    "descendant_body_creation_boundary_result_recorded",
    "descendant_body_creation_operation_consideration_allowed",
    "candidate_standing_referenced",
    "candidate_a_standing_referenced",
    "candidate_b_standing_referenced",
    "candidate_standing_created_referenced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "descendant_body_creation_performed",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
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
    "candidate_standing_operation_overridden",
    "candidate_standing_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_descendant_body_creation_boundary_to_descendant_body_creation_operation_completion",
    "direct_candidate_standing_to_descendant_body_creation_without_boundary_and_operation",
    "direct_candidate_standing_to_standing_descendant",
    "direct_candidate_standing_to_descendant_standing",
    "direct_descendant_body_creation_boundary_to_descendant_body_creation",
    "direct_descendant_body_creation_boundary_to_crossing",
    "direct_descendant_body_creation_boundary_to_relation",
    "direct_descendant_body_creation_boundary_to_runtime",
    "direct_descendant_body_creation_boundary_to_authority_currentness",
    "direct_descendant_body_creation_boundary_to_coupling_creation",
    "direct_descendant_body_creation_boundary_to_third_candidate_route",
    "direct_descendant_body_creation_boundary_to_third_model_route",
    "direct_descendant_body_creation_boundary_to_presence",
    "direct_descendant_body_creation_boundary_to_identity",
    "direct_descendant_body_creation_boundary_to_output_action",
    "direct_descendant_body_creation_boundary_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_MARKER_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_STANDING_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_DESCENDANT_BODY_CREATION_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_descendant_body_creation": "PROHIBITED_DESCENDANT_BODY_CREATION_REQUESTED",
    "request_descendant_body_a_creation": "PROHIBITED_DESCENDANT_BODY_CREATION_REQUESTED",
    "request_descendant_body_b_creation": "PROHIBITED_DESCENDANT_BODY_CREATION_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_first_crossing_authorization": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
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
    "descendant_body_creation_boundary_id": BOUNDARY_ID,
    "descendant_body_creation_boundary_type": BOUNDARY_TYPE,
    "descendant_body_creation_boundary_version": BOUNDARY_VERSION,
    "descendant_body_creation_boundary_scope": BOUNDARY_SCOPE,
    "prior_candidate_standing_operation_type": PRIOR_CANDIDATE_STANDING_OPERATION_TYPE,
    "prior_candidate_standing_operation_outcome_required": PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
    "prior_candidate_standing_result_required": PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
    "prior_candidate_standing_supported_required": PRIOR_CANDIDATE_STANDING_SUPPORTED_REQUIRED,
    "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
    "prior_candidate_standing_created_required": PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED,
    "prior_candidate_a_standing_created_required": PRIOR_CANDIDATE_A_STANDING_CREATED_REQUIRED,
    "prior_candidate_b_standing_created_required": PRIOR_CANDIDATE_B_STANDING_CREATED_REQUIRED,
    "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
}

BOUNDARY_SPEC_MARKER_CLASSES = (
    ("boundary_identity", ((
        "Descendant Body Creation Boundary V0 Minimum Specification",
        BOUNDARY_TYPE,
        BOUNDARY_ID,
        BOUNDARY_SCOPE,
    ),)),
    ("candidate_standing_basis", (
        (
            PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
            PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate A standing and Candidate B standing were supported, authorized, and created as candidate standing only",
        ),
        (
            PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
            PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
            "true `candidate_standing_supported`, `candidate_standing_authorized`, `candidate_standing_created`, `candidate_a_standing_created`, and `candidate_b_standing_created`",
            "both candidate standings were supported, authorized, and created as candidate standing only",
        ),
    )),
    ("candidate_standing_non_conversion", ((
        "Candidate standing is not descendant-body creation",
        "Candidate standing is not relation",
        "Candidate standing is not presence",
        "Candidate standing is not identity",
        "descendant_body_created = false",
        "descendant_body_a_created = false",
        "descendant_body_b_created = false",
        "standing_descendant_created = false",
        "descendant_standing_check_performed = false",
        "relation_created = false",
        "coupling_created = false",
        "presence_established = false",
        "identity_created = false",
        "follow_on_authorized = false",
    ),)),
    ("boundary_permitted_result", ((
        OUTCOME_ALLOWED,
        OUTCOME_REQUIRES_CANDIDATE_STANDING,
        OUTCOME_BLOCKED,
        "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
        "REQUIRES_CANDIDATE_STANDING",
    ),)),
    ("boundary_non_conversion", (
        (
            "Descendant-body creation boundary is not descendant-body creation operation",
            "Descendant-body creation boundary permission is not descendant-body creation completion",
            "Descendant-body creation operation consideration is not descendant-body creation",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not standing descendant",
            "Candidate standing is not crossing",
            "Candidate standing is not relation",
            "Candidate standing is not runtime",
            "Candidate standing is not currentness",
            "Candidate standing is not authority",
            "Candidate standing is not coupling",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
            "Candidate standing is not follow-on authorization",
        ),
        (
            "Descendant-body creation boundary is not descendant-body creation operation; boundary permission is not creation completion; operation consideration is not creation.",
            "Candidate standing is not descendant-body creation, standing descendant, crossing, relation, runtime, currentness, authority, coupling, presence, identity, or follow-on authorization.",
        ),
    )),
    ("sibling_non_hierarchy", (
        (
            "Candidate A and Candidate B remain sibling candidate standings",
            "Neither candidate standing ranks above the other",
            "Candidate A and Candidate B remain sibling candidate records",
            "Candidate A basis material and Candidate B basis material remain sibling basis materials",
            "Neither candidate basis ranks above the other",
            "Regulation may not become sovereign over Motion",
            "Motion may not erase Regulation",
            "Coupling remains unassigned",
        ),
        (
            "Candidate A and Candidate B remain sibling candidate standings and sibling candidate records. Neither standing nor basis ranks above the other. Regulation may not become sovereign over Motion; Motion may not erase Regulation.",
            "Coupling remains unassigned",
        ),
    )),
    ("permitted_route", ((
        ADMISSIBLE_FUTURE_ROUTE,
        "Only after a future boundary records DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED may a separately bounded descendant-body creation operation be considered",
        "No later operation is authorized by this boundary specification alone",
    ),)),
    ("contaminated_lineage", (
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
        (
            "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md` remains preserved contaminated lineage",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    )),
    ("blocked_routes", (
        (
            "direct descendant-body creation boundary to descendant-body creation operation completion",
            "direct candidate standing to descendant-body creation without boundary and operation",
            "direct candidate standing to standing descendant",
            "direct candidate standing to descendant standing",
            "direct descendant-body creation boundary to descendant-body creation",
            "direct descendant-body creation boundary to crossing",
            "direct descendant-body creation boundary to relation",
            "direct descendant-body creation boundary to runtime",
            "direct descendant-body creation boundary to authority/currentness",
            "direct descendant-body creation boundary to coupling creation",
            "direct descendant-body creation boundary to third-candidate route",
            "direct descendant-body creation boundary to third-model route",
            "direct descendant-body creation boundary to presence",
            "direct descendant-body creation boundary to identity",
            "direct descendant-body creation boundary to output/action",
            "direct descendant-body creation boundary to follow-on work",
            "repository scan",
            "file discovery",
            "affected-file repair",
            "prior unsupported-claim validation",
        ),
        (
            "The following are blocked: direct descendant-body creation boundary to descendant-body creation operation completion; direct candidate standing to descendant-body creation without boundary and operation; direct candidate standing to standing descendant or descendant standing; direct descendant-body creation boundary to descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, output/action, or follow-on work; repository scan; file discovery; affected-file repair; and prior unsupported-claim validation.",
        ),
    )),
    ("closing_lock", ((
        "This boundary spec defines only a future descendant-body creation boundary shape",
        "It does not create descendant bodies",
        "Descendant-body creation boundary is not descendant-body creation operation",
        "Descendant-body creation operation consideration is not descendant-body creation",
        "Candidate standing is not descendant-body creation",
        "Candidate standing is not presence",
        "Candidate standing is not identity",
        "Only after a future boundary records DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED may a separately bounded descendant-body creation operation be considered",
        "Open means not scheduled, not authorized, and not executed",
    ),)),
)

UPSTREAM_REQUIREMENTS = (
    (
        "candidate_standing_operation_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 176",
            PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
            "candidate_standing_supported = true",
            "candidate_standing_authorized = true",
            "candidate_standing_created = true",
            "candidate_a_standing_created = true",
            "candidate_b_standing_created = true",
            "Candidate A standing and Candidate B standing were supported, authorized, and created as candidate standing only",
            "Candidate standing is not descendant-body creation",
            "Candidate standing is not relation",
            "Candidate standing is not presence",
            "Candidate standing is not identity",
            "descendant_body_created = false",
            "descendant_body_a_created = false",
            "descendant_body_b_created = false",
            "standing_descendant_created = false",
            "descendant_standing_check_performed = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "candidate_standing_operation_terminal_summary_markers_present",
        True,
    ),
    (
        "candidate_standing_boundary_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_ALLOWED",
            "CANDIDATE_STANDING_OPERATION_CONSIDERATION_ALLOWED",
        ),),
        "candidate_standing_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "distinctness_support_recheck_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DISTINCTNESS_SUPPORTED", "candidate_records_distinct = true"),),
        "distinctness_support_recheck_terminal_summary_markers_present",
        True,
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
        "successor_closure_operation_terminal_summary_reference",
        DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("CLOSED",),),
        "successor_closure_operation_terminal_summary_markers_present",
        False,
    ),
    (
        "scope_division_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("REQUIRES_ADDITIONAL_BASIS",),),
        "scope_division_operation_terminal_summary_markers_present",
        False,
    ),
)

WHAT_REMAINS_OPEN = (
    "descendant-body creation operation, if separately bounded after boundary",
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
    return (
        normalized.startswith("raw_")
        or normalized.startswith("hidden_")
        or normalized.endswith("_body")
        or normalized in {"payload", "file_bytes", "full_body", "full_text", "source_body"}
    )


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


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _failed_codes(
    checks: list[dict[str, Any]], upstream: bool | None = None
) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False
        and isinstance(check.get("block_code"), str)
        and check["block_code"] in BLOCK_CODES
        and (upstream is None or check.get("upstream_basis_check") is upstream)
    ]


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for check in checks:
        name = check.get("check_name")
        if isinstance(name, str) and name.endswith("markers present"):
            flags[name.replace(" ", "_")] = check.get("passed") is True
    return flags


def _code_for_false_posture(key: str) -> str:
    if key in {
        "descendant_body_creation_performed", "descendant_body_a_created",
        "descendant_body_b_created", "descendant_body_created", "crossing_authorized",
        "first_crossing_authorized", "standing_created",
    }:
        return "PROHIBITED_DESCENDANT_BODY_CREATION_REQUESTED"
    if key in {"standing_descendant_created", "descendant_standing_check_performed"}:
        return "PROHIBITED_STANDING_DESCENDANT_REQUESTED"
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
        "affected_file_redeemed", "affected_file_treated_as_clean_basis",
        "prior_unsupported_candidate_a_claim_validated",
        "prior_unsupported_candidate_b_claim_validated",
        "prior_unsupported_derivation_event_claim_validated",
    }:
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "NON_CLAIM_MISSING_OR_FLIPPED"


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
    if "descendant_body_creation_boundary_result" in request:
        _add_check(
            checks,
            "descendant-body creation boundary result not pre-claimed",
            False,
            "resolver-derived result only",
            request.get("descendant_body_creation_boundary_result"),
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
    reference = request.get("descendant_body_creation_boundary_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "descendant-body creation boundary specification reference readable",
        text is not None,
        "readable declared specification",
        reference,
        "DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return
    for class_name, variants in BOUNDARY_SPEC_MARKER_CLASSES:
        _add_check(
            checks,
            f"descendant-body creation boundary specification {class_name} markers present",
            _markers_present(text, variants),
            "posture marker class present",
            class_name,
            "DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_MARKER_MISSING",
        )


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    missing_candidate_standing: list[str] = []
    for field, _, missing_code, marker_code, variants, flag, is_candidate_basis in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        _add_check(
            checks,
            f"{field} readable",
            text is not None,
            "readable declared terminal summary",
            reference,
            missing_code,
            upstream=True,
        )
        present = _markers_present(text, variants)
        _add_check(
            checks,
            flag,
            present,
            "required terminal-summary posture markers",
            reference if text is None else flag,
            marker_code,
            upstream=True,
        )
        if is_candidate_basis and not present:
            missing_candidate_standing.append(flag)
    return missing_candidate_standing


def _boundary_result_value(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"
    if outcome == OUTCOME_REQUIRES_CANDIDATE_STANDING:
        return "REQUIRES_CANDIDATE_STANDING"
    if outcome == OUTCOME_BLOCKED:
        return "BLOCKED"
    return "NOT_RECORDED"


def _boundary_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    return {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "descendant_body_creation_boundary_id": BOUNDARY_ID,
        "descendant_body_creation_boundary_type": BOUNDARY_TYPE,
        "descendant_body_creation_boundary_version": BOUNDARY_VERSION,
        "descendant_body_creation_boundary_scope": BOUNDARY_SCOPE,
        "prior_candidate_standing_operation_type": PRIOR_CANDIDATE_STANDING_OPERATION_TYPE,
        "prior_candidate_standing_operation_outcome_required": PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
        "prior_candidate_standing_result_required": PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
        "prior_candidate_standing_supported_required": PRIOR_CANDIDATE_STANDING_SUPPORTED_REQUIRED,
        "prior_candidate_standing_authorized_required": PRIOR_CANDIDATE_STANDING_AUTHORIZED_REQUIRED,
        "prior_candidate_standing_created_required": PRIOR_CANDIDATE_STANDING_CREATED_REQUIRED,
        "prior_candidate_a_standing_created_required": PRIOR_CANDIDATE_A_STANDING_CREATED_REQUIRED,
        "prior_candidate_b_standing_created_required": PRIOR_CANDIDATE_B_STANDING_CREATED_REQUIRED,
        "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
        "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
        "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(),
        **marker_flags,
        "descendant_body_creation_boundary_recorded": allowed,
        "descendant_body_creation_boundary_result_recorded": allowed,
        "descendant_body_creation_boundary_result": _boundary_result_value(outcome),
        "descendant_body_creation_operation_consideration_allowed": allowed,
        "candidate_standing_referenced": allowed,
        "candidate_a_standing_referenced": allowed,
        "candidate_b_standing_referenced": allowed,
        "candidate_standing_created_referenced": allowed,
    }


def _boundary_material(outcome: str, candidate_standing_present: bool) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    referenced = allowed and candidate_standing_present
    return {
        "candidate_standing_reference": {
            "prior_candidate_standing_operation_type": PRIOR_CANDIDATE_STANDING_OPERATION_TYPE,
            "prior_candidate_standing_operation_outcome": PRIOR_CANDIDATE_STANDING_OPERATION_OUTCOME_REQUIRED,
            "prior_candidate_standing_result": PRIOR_CANDIDATE_STANDING_RESULT_REQUIRED,
            "prior_candidate_standing_supported": referenced,
            "prior_candidate_standing_authorized": referenced,
            "prior_candidate_standing_created": referenced,
            "prior_candidate_a_standing_created": referenced,
            "prior_candidate_b_standing_created": referenced,
        },
        "candidate_pair_reference": {
            "candidate_a_standing_created": referenced,
            "candidate_b_standing_created": referenced,
            "candidate_a_standing_is_descendant_body": False,
            "candidate_b_standing_is_descendant_body": False,
            "candidate_standing_is_descendant_body_creation": False,
            "candidate_standing_is_standing_descendant": False,
            "candidate_standing_is_relation": False,
            "candidate_standing_is_presence": False,
            "candidate_standing_is_identity": False,
            "candidate_pair_non_hierarchy_preserved": referenced,
            "candidate_records_remain_sibling": referenced,
            "coupling_created": False,
        },
        "boundary_evaluation": {
            "descendant_body_creation_operation_consideration_allowed": allowed,
            "descendant_body_creation_boundary_result": _boundary_result_value(outcome),
            "descendant_body_creation_performed": False,
            "descendant_body_created": False,
            "standing_descendant_created": False,
            "crossing_authorized": False,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    fields = (
        "intent",
        *EXPECTED_REQUEST_VALUES.keys(),
        "descendant_body_creation_boundary_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
        *PROHIBITED_REQUEST_FLAGS.keys(),
    )
    projection = {field: request.get(field) for field in fields if field in request}
    declared = request.get("declared_non_claims")
    if isinstance(declared, Mapping):
        projection["declared_non_claims"] = {
            key: declared.get(key) for key in REQUIRED_FALSE_NON_CLAIMS
        }
    else:
        projection["declared_non_claims"] = type(declared).__name__
    return _sanitize(projection)


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("descendant_body_creation_boundary")
    details = boundary if isinstance(boundary, Mapping) else {}
    checks = result.get("descendant_body_creation_boundary_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    result_detail = result.get("boundary_result_detail")
    detail = result_detail if isinstance(result_detail, Mapping) else {}
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
        "prior_candidate_standing_operation_type": details.get("prior_candidate_standing_operation_type"),
        "prior_candidate_standing_operation_outcome_required": details.get("prior_candidate_standing_operation_outcome_required"),
        "prior_candidate_standing_result_required": details.get("prior_candidate_standing_result_required"),
        "prior_candidate_standing_supported_required": details.get("prior_candidate_standing_supported_required"),
        "prior_candidate_standing_authorized_required": details.get("prior_candidate_standing_authorized_required"),
        "prior_candidate_standing_created_required": details.get("prior_candidate_standing_created_required"),
        "prior_candidate_a_standing_created_required": details.get("prior_candidate_a_standing_created_required"),
        "prior_candidate_b_standing_created_required": details.get("prior_candidate_b_standing_created_required"),
        "descendant_body_creation_boundary_result": details.get("descendant_body_creation_boundary_result"),
        "descendant_body_creation_operation_consideration_allowed": details.get("descendant_body_creation_operation_consideration_allowed"),
        "candidate_standing_referenced": details.get("candidate_standing_referenced"),
        "candidate_a_standing_referenced": details.get("candidate_a_standing_referenced"),
        "candidate_b_standing_referenced": details.get("candidate_b_standing_referenced"),
        "candidate_standing_created_referenced": details.get("candidate_standing_created_referenced"),
        "selected_target_spec_path": basis.get("descendant_body_creation_boundary_spec_reference"),
        "completed_candidate_standing_operation_terminal_summary_path": basis.get("candidate_standing_operation_terminal_summary_reference"),
        "missing_or_insufficient_candidate_standing": detail.get("missing_or_insufficient_candidate_standing", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, *REQUIRED_FALSE_NON_CLAIMS):
        summary[key] = details.get(key)
    for key, value in _marker_flags([item for item in records if isinstance(item, Mapping)]).items():
        summary[key] = details.get(key, value)
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_candidate_standing: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _marker_flags(checks)
    boundary = _boundary_object(outcome, marker_flags)
    candidate_standing_present = not missing_candidate_standing
    result: dict[str, Any] = {
        "descendant_body_creation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_descendant_body_creation_boundary_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "descendant_body_creation_boundary_spec_reference": request.get(
                "descendant_body_creation_boundary_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "descendant_body_creation_boundary": boundary,
        "descendant_body_creation_boundary_material": _boundary_material(
            outcome, candidate_standing_present
        ),
        "descendant_body_creation_boundary_checks": checks,
        "descendant_body_creation_boundary_statement": {
            "outcome": outcome,
            **{key: boundary[key] for key in ALLOWED_TRUE_RECORDED_FIELDS},
            "descendant_body_creation_boundary_result": boundary[
                "descendant_body_creation_boundary_result"
            ],
            "descendant_body_creation_performed": False,
            "descendant_body_created": False,
            "relation_created": False,
            "runtime_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "descendant_body_creation_boundary_non_meaning": {
            "not_descendant_body_creation": True,
            "not_standing_descendant": True,
            "not_crossing": True,
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_follow_on": True,
        },
        "boundary_result_detail": {
            "descendant_body_creation_boundary_result": boundary[
                "descendant_body_creation_boundary_result"
            ],
            "missing_or_insufficient_candidate_standing": list(missing_candidate_standing),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "descendant_body_creation_operation_requires_separate_bounded_step": True,
        },
        "blocked_routes": [
            "descendant-body creation, standing descendant, crossing, relation, runtime, authority, coupling, third model, presence, identity, repair, discovery, validation, and downstream authorization",
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
    result["descendant_body_creation_boundary_summary"] = _build_summary(result)
    return _sanitize(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_candidate_standing: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_candidate_standing or [],
        code,
        reason,
    )


def build_declared_descendant_body_creation_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit, no-discovery descendant-body boundary request."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "descendant_body_creation_boundary_spec_reference": (
            DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_SPEC_REFERENCE
        ),
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in ALLOWED_TRUE_RECORDED_FIELDS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_creation_boundary_v0_min(
    declared_descendant_body_creation_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one candidate-standing-gated boundary without creation conversion."""

    if declared_descendant_body_creation_boundary is None:
        request = build_declared_descendant_body_creation_boundary_v0_min_request()
    elif not isinstance(declared_descendant_body_creation_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_descendant_body_creation_boundary).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_descendant_body_creation_boundary))

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
    missing_candidate_standing = _validate_upstream(checks, request)

    non_upstream_failures = _failed_codes(checks, upstream=False)
    if non_upstream_failures:
        code = non_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed check {code}",
            missing_candidate_standing,
        )

    candidate_basis_codes = {
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_SUPPORT_RECHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    }
    other_upstream_failures = [
        code for code in _failed_codes(checks, upstream=True) if code not in candidate_basis_codes
    ]
    if other_upstream_failures:
        code = other_upstream_failures[0]
        return _blocked_result(
            request,
            checks,
            code,
            f"blocked by failed upstream check {code}",
            missing_candidate_standing,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, missing_candidate_standing)
    if missing_candidate_standing:
        return _build_result(
            request,
            OUTCOME_REQUIRES_CANDIDATE_STANDING,
            checks,
            missing_candidate_standing,
        )
    return _build_result(request, OUTCOME_ALLOWED, checks, [])


def resolve_descendant_body_creation_boundary_v0_min_from_path(
    declared_descendant_body_creation_boundary_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_descendant_body_creation_boundary_path)
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
        return _blocked_result(
            {}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON"
        )
    return resolve_descendant_body_creation_boundary_v0_min(request)


def build_descendant_body_creation_boundary_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact metadata for one bounded descendant-body boundary."""

    return _build_summary(result)


def write_descendant_body_creation_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
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
            json.dump(
                _json_ready(_sanitize(result)),
                handle,
                ensure_ascii=True,
                indent=2,
                sort_keys=True,
            )
            handle.write("\n")
        return final_path
    except OSError as exc:
        raise DescendantBodyCreationBoundaryV0MinError(f"WRITE_REFUSED: {exc}") from exc
