"""Resolve one bounded first-crossing boundary result from declared local summaries.

This resolver records only a first-crossing boundary allowance.  It is local,
read-only, non-hosting, non-looping, non-daemon, and refuses conversion into a
crossing, relation, runtime, authority, standing, or follow-on operation.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class FirstCrossingBoundaryV0MinError(Exception):
    """Raised when a first-crossing boundary result cannot be written safely."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_first_crossing_boundary_v0_min"

BOUNDARY_ID = "first_crossing_boundary_001"
BOUNDARY_TYPE = "FIRST_CROSSING_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_FIRST_CROSSING_AFTER_DESCENDANT_BODY_CREATION_ONLY"

PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE = "DESCENDANT_BODY_CREATION_OPERATION"
PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED = (
    "DESCENDANT_BODY_CREATION_OPERATION_CREATED"
)
PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED = "DESCENDANT_BODY_CREATION_SUPPORTED"
PRIOR_DESCENDANT_BODY_CREATION_SUPPORTED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATION_AUTHORIZED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED = True
PRIOR_DESCENDANT_BODY_A_CREATED_REQUIRED = True
PRIOR_DESCENDANT_BODY_B_CREATED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATED_REQUIRED = True
PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED = False
PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED = False
PRIOR_CROSSING_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "FIRST_CROSSING_BOUNDARY_THEN_FIRST_CROSSING_OPERATION_ONLY"

DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"

OUTCOME_ALLOWED = "FIRST_CROSSING_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION = (
    "FIRST_CROSSING_BOUNDARY_REQUIRES_DESCENDANT_BODY_CREATION"
)
OUTCOME_BLOCKED = "FIRST_CROSSING_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "FIRST_CROSSING_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_FIRST_CROSSING_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_FIRST_CROSSING_BOUNDARY"
INTENT_BLOCK = "BLOCK_FIRST_CROSSING_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_first_crossing_boundary_v0_min"
)
DETERMINISTIC_FILENAME = "first_crossing_boundary_001__first_crossing_boundary_v0_min_result.json"

DEFAULT_FIRST_CROSSING_BOUNDARY_SPEC_REFERENCE = (
    "spec/FIRST_CROSSING_BOUNDARY_V0_MIN_SPEC.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "first_crossing_boundary_recorded",
    "first_crossing_boundary_result_recorded",
    "first_crossing_operation_consideration_allowed",
    "descendant_body_creation_referenced",
    "descendant_body_a_referenced",
    "descendant_body_b_referenced",
    "descendant_body_created_referenced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_RECORDED_FIELDS,
    "first_crossing_authorized",
    "crossing_authorized",
    "first_crossing_performed",
    "crossing_performed",
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
    "coupling_assigned_to_descendant_body_a",
    "coupling_assigned_to_descendant_body_b",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "third_candidate_created",
    "third_model_admitted",
    "presence_established",
    "identity_created",
    "standing_descendant_created",
    "descendant_standing_check_performed",
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
    "descendant_body_creation_operation_overridden",
    "descendant_body_creation_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_first_crossing_boundary_to_first_crossing_operation_completion",
    "direct_descendant_body_creation_to_first_crossing_without_boundary_and_operation",
    "direct_descendant_body_to_first_crossing_without_boundary_and_operation",
    "direct_first_crossing_boundary_to_crossing_authorization",
    "direct_first_crossing_boundary_to_crossing",
    "direct_first_crossing_boundary_to_relation",
    "direct_first_crossing_boundary_to_runtime",
    "direct_first_crossing_boundary_to_authority_currentness",
    "direct_first_crossing_boundary_to_coupling_creation",
    "direct_first_crossing_boundary_to_third_candidate_route",
    "direct_first_crossing_boundary_to_third_model_route",
    "direct_first_crossing_boundary_to_presence",
    "direct_first_crossing_boundary_to_identity",
    "direct_first_crossing_boundary_to_standing_descendant",
    "direct_first_crossing_boundary_to_descendant_standing",
    "direct_first_crossing_boundary_to_output_action",
    "direct_first_crossing_boundary_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "FIRST_CROSSING_BOUNDARY_SPEC_REFERENCE_MISSING",
    "FIRST_CROSSING_BOUNDARY_SPEC_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_FIRST_CROSSING_REQUESTED",
    "PROHIBITED_CROSSING_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_first_crossing_authorization": "PROHIBITED_FIRST_CROSSING_REQUESTED",
    "request_first_crossing_performed": "PROHIBITED_FIRST_CROSSING_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_CROSSING_REQUESTED",
    "request_crossing_performed": "PROHIBITED_CROSSING_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_coupling_assignment_to_descendant_body_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_identity_creation": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_follow_on_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
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
    "first_crossing_boundary_id": BOUNDARY_ID,
    "first_crossing_boundary_type": BOUNDARY_TYPE,
    "first_crossing_boundary_version": BOUNDARY_VERSION,
    "first_crossing_boundary_scope": BOUNDARY_SCOPE,
    "prior_descendant_body_creation_operation_type": (
        PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE
    ),
    "prior_descendant_body_creation_operation_outcome_required": (
        PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED
    ),
    "prior_descendant_body_creation_result_required": (
        PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED
    ),
    "prior_descendant_body_creation_supported_required": (
        PRIOR_DESCENDANT_BODY_CREATION_SUPPORTED_REQUIRED
    ),
    "prior_descendant_body_creation_authorized_required": (
        PRIOR_DESCENDANT_BODY_CREATION_AUTHORIZED_REQUIRED
    ),
    "prior_descendant_body_creation_performed_required": (
        PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED
    ),
    "prior_descendant_body_a_created_required": PRIOR_DESCENDANT_BODY_A_CREATED_REQUIRED,
    "prior_descendant_body_b_created_required": PRIOR_DESCENDANT_BODY_B_CREATED_REQUIRED,
    "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
    "prior_standing_descendant_created_required": (
        PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED
    ),
    "prior_descendant_standing_check_performed_required": (
        PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED
    ),
    "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    "descendant_body_a_id": DESCENDANT_BODY_A_ID,
    "descendant_body_b_id": DESCENDANT_BODY_B_ID,
    "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
    "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
    "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
    "candidate_a_role": CANDIDATE_A_ROLE,
    "candidate_b_role": CANDIDATE_B_ROLE,
    "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
    "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
    "first_crossing_boundary_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "boundary identity",
        ((
            "First Crossing Boundary V0 Minimum Specification",
            BOUNDARY_TYPE,
            BOUNDARY_ID,
            BOUNDARY_SCOPE,
        ),),
    ),
    (
        "descendant body creation basis",
        ((
            PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED,
            PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED,
            "descendant_body_creation_supported = true",
            "descendant_body_creation_authorized = true",
            "descendant_body_creation_performed = true",
            "descendant_body_a_created = true",
            "descendant_body_b_created = true",
            "descendant_body_created = true",
            "Descendant Body A and Descendant Body B were created as descendant-body records only",
        ),),
    ),
    (
        "descendant body non conversion",
        ((
            "descendant-body creation is not standing descendant creation",
            "descendant body is not standing descendant",
            "descendant body is not descendant standing",
            "descendant body is not crossing",
            "descendant body is not relation",
            "descendant body is not presence",
            "descendant body is not identity",
            "standing_descendant_created = false",
            "descendant_standing_check_performed = false",
            "crossing_authorized = false",
            "first_crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
    ),
    (
        "boundary permitted result",
        ((
            OUTCOME_ALLOWED,
            OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
            OUTCOME_BLOCKED,
            "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
            "REQUIRES_DESCENDANT_BODY_CREATION",
        ),),
    ),
    (
        "boundary non conversion",
        ((
            "First-crossing boundary is not first-crossing operation",
            "First-crossing boundary permission is not first-crossing completion",
            "First-crossing operation consideration is not first crossing",
            "Descendant-body creation is not first crossing",
            "Descendant body is not first crossing",
            "Descendant body is not crossing",
            "Descendant body is not relation",
            "Descendant body is not runtime",
            "Descendant body is not currentness",
            "Descendant body is not authority",
            "Descendant body is not coupling",
            "Descendant body is not presence",
            "Descendant body is not identity",
            "Descendant body is not follow-on authorization",
            "Descendant body is not standing descendant",
            "Descendant body is not descendant standing",
        ),),
    ),
    (
        "sibling non hierarchy",
        ((
            "Descendant Body A and Descendant Body B remain sibling records",
            "Neither descendant body ranks above the other",
            "Candidate A and Candidate B remain sibling candidate standings",
            "Neither candidate standing ranks above the other",
            "Regulation may not become sovereign over Motion",
            "Motion may not erase Regulation",
            "Coupling remains unassigned",
        ),),
    ),
    (
        "permitted route",
        ((
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future boundary records FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED may a separately bounded first-crossing operation be considered",
            "No later operation is authorized by this boundary specification alone",
        ),),
    ),
    (
        "contaminated lineage preservation",
        (
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
        ),
    ),
    (
        "blocked routes",
        ((
            "direct first-crossing boundary to first-crossing operation completion",
            "direct descendant-body creation to first crossing without boundary and operation",
            "direct descendant body to first crossing without boundary and operation",
            "direct first-crossing boundary to crossing authorization",
            "direct first-crossing boundary to crossing",
            "direct first-crossing boundary to relation",
            "direct first-crossing boundary to runtime",
            "direct first-crossing boundary to authority/currentness",
            "direct first-crossing boundary to coupling creation",
            "direct first-crossing boundary to third-candidate route",
            "direct first-crossing boundary to third-model route",
            "direct first-crossing boundary to presence",
            "direct first-crossing boundary to identity",
            "direct first-crossing boundary to standing descendant",
            "direct first-crossing boundary to descendant standing",
            "direct first-crossing boundary to output/action",
            "direct first-crossing boundary to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        ((
            "This boundary spec defines only a future first-crossing boundary shape",
            "It does not authorize first crossing",
            "First-crossing boundary is not first-crossing operation",
            "First-crossing operation consideration is not first crossing",
            "Descendant-body creation is not first crossing",
            "Descendant body is not first crossing",
            "Descendant body is not crossing",
            "Descendant body is not relation",
            "Descendant body is not presence",
            "Descendant body is not identity",
            "Only after a future boundary records FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED may a separately bounded first-crossing operation be considered",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "descendant_body_creation_operation_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 253",
            PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED,
            "descendant_body_creation_supported = true",
            "descendant_body_creation_authorized = true",
            "descendant_body_creation_performed = true",
            "descendant_body_a_created = true",
            "descendant_body_b_created = true",
            "descendant_body_created = true",
            "Descendant Body A and Descendant Body B were created as descendant-body records only",
            "descendant-body creation is not standing descendant creation",
            "descendant body is not standing descendant",
            "descendant body is not descendant standing",
            "descendant body is not crossing",
            "descendant body is not relation",
            "descendant body is not presence",
            "descendant body is not identity",
            "standing_descendant_created = false",
            "descendant_standing_check_performed = false",
            "crossing_authorized = false",
            "first_crossing_authorized = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "completed_descendant_body_creation_operation_terminal_summary_markers_present",
        True,
    ),
    (
        "descendant_body_creation_boundary_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
            "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",
        ),),
        "completed_descendant_body_creation_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "candidate_standing_operation_terminal_summary_reference",
        DEFAULT_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("CANDIDATE_STANDING_SUPPORTED", "candidate_standing_created = true"),),
        "completed_candidate_standing_operation_terminal_summary_markers_present",
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
)

WHAT_REMAINS_OPEN = (
    "first-crossing operation, if separately bounded after boundary",
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

BLOCKED_ROUTES = (
    "direct first-crossing boundary to first-crossing operation completion",
    "direct descendant-body creation to first crossing without boundary and operation",
    "direct descendant body to first crossing without boundary and operation",
    "direct first-crossing boundary to crossing authorization",
    "direct first-crossing boundary to crossing",
    "direct first-crossing boundary to relation",
    "direct first-crossing boundary to runtime",
    "direct first-crossing boundary to authority/currentness",
    "direct first-crossing boundary to coupling creation",
    "direct first-crossing boundary to third-candidate route",
    "direct first-crossing boundary to third-model route",
    "direct first-crossing boundary to presence",
    "direct first-crossing boundary to identity",
    "direct first-crossing boundary to standing descendant",
    "direct first-crossing boundary to descendant standing",
    "direct first-crossing boundary to output/action",
    "direct first-crossing boundary to follow-on work",
    "repository scan route",
    "file discovery route",
    "affected-file repair route",
    "prior unsupported-claim validation route",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {field: False for field in REQUIRED_FALSE_NON_CLAIMS}


def _json_ready(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {str(key): _json_ready(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_json_ready(item) for item in value]
    if isinstance(value, Path):
        return str(value)
    return value


def _path_from_reference(reference: Any) -> Path | None:
    if not isinstance(reference, (str, Path)):
        return None
    path = Path(reference)
    return path if path.is_absolute() else REPO_ROOT / path


def _read_text(reference: Any) -> str | None:
    path = _path_from_reference(reference)
    if path is None or not path.is_file():
        return None
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return None


def _markers_present(text: str | None, variants: tuple[tuple[str, ...], ...]) -> bool:
    if text is None:
        return False
    normalized = text.casefold()
    return any(
        all(marker.casefold() in normalized for marker in marker_group)
        for marker_group in variants
    )


def _add_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str | None = None,
    upstream_basis_check: bool = False,
) -> None:
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": passed,
        "expected_posture": _json_ready(expected_posture),
        "actual_posture": _json_ready(actual_posture),
        "upstream_basis_check": upstream_basis_check,
    }
    if block_code is not None:
        check["block_code"] = block_code
    checks.append(check)


def _failed_codes(checks: list[Mapping[str, Any]]) -> list[str]:
    return [
        str(check["block_code"])
        for check in checks
        if check.get("passed") is False and isinstance(check.get("block_code"), str)
    ]


def _marker_flags(checks: list[Mapping[str, Any]]) -> dict[str, bool]:
    flags: dict[str, bool] = {}
    for check in checks:
        check_name = check.get("check_name")
        if isinstance(check_name, str) and check_name.endswith("markers present"):
            flags[check_name.replace(" ", "_")] = check.get("passed") is True
    return flags


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    for field, expected in EXPECTED_REQUEST_VALUES.items():
        actual = request.get(field)
        _add_check(
            checks,
            f"declared {field}",
            actual == expected,
            expected,
            actual,
            "REQUEST_VALUE_MISMATCH",
        )


def _validate_declared_non_claims(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> None:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        _add_check(
            checks,
            "declared non-claims mapping",
            False,
            "mapping with canonical false posture",
            type(declared).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    for field in REQUIRED_FALSE_NON_CLAIMS:
        value = declared.get(field)
        _add_check(
            checks,
            f"declared non-claim {field}",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _request_posture_failure(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> str | None:
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        value = request.get(field)
        _add_check(checks, f"prohibited request flag {field}", value is not True, False, value, code)
        if value is True:
            return code
    for field in ALLOWED_TRUE_RECORDED_FIELDS:
        value = request.get(field)
        _add_check(
            checks,
            f"result posture not pre-claimed {field}",
            value is not True,
            False,
            value,
            "RESULT_POSTURE_PRECLAIMED",
        )
        if value is True:
            return "RESULT_POSTURE_PRECLAIMED"
    for field in REQUIRED_FALSE_NON_CLAIMS:
        if field in ALLOWED_TRUE_RECORDED_FIELDS or field not in request:
            continue
        value = request.get(field)
        _add_check(
            checks,
            f"top-level false posture {field}",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        if value is not False:
            return "NON_CLAIM_MISSING_OR_FLIPPED"
    return None


def _validate_target_spec(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> str | None:
    reference = request.get("first_crossing_boundary_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "first-crossing boundary specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "FIRST_CROSSING_BOUNDARY_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "FIRST_CROSSING_BOUNDARY_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for class_name, variants in TARGET_SPEC_MARKER_CLASSES:
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"first-crossing boundary specification {class_name} markers present",
            present,
            "posture marker class present",
            present,
            "FIRST_CROSSING_BOUNDARY_SPEC_MARKER_MISSING",
        )
        if not present and failure is None:
            failure = "FIRST_CROSSING_BOUNDARY_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_descendant_body_creation: list[str] = []
    blocking_failure: str | None = None
    for field, _, missing_code, marker_code, variants, flag, allowance_class in UPSTREAM_REQUIREMENTS:
        reference = request.get(field)
        text = _read_text(reference)
        readable = text is not None
        _add_check(
            checks,
            f"{field} readable",
            readable,
            "readable terminal summary",
            reference,
            missing_code,
            True,
        )
        if not readable:
            if allowance_class:
                missing_descendant_body_creation.append(field)
            elif blocking_failure is None:
                blocking_failure = missing_code
            continue
        present = _markers_present(text, variants)
        _add_check(
            checks,
            flag.replace("_", " "),
            present,
            "required terminal-summary posture markers",
            present,
            marker_code,
            True,
        )
        if not present:
            if allowance_class:
                missing_descendant_body_creation.append(field)
            elif blocking_failure is None:
                blocking_failure = marker_code
    return missing_descendant_body_creation, blocking_failure


def _boundary_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    requires_descendant_body_creation = outcome == OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION
    boundary: dict[str, Any] = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "first_crossing_boundary_id": BOUNDARY_ID,
        "first_crossing_boundary_type": BOUNDARY_TYPE,
        "first_crossing_boundary_version": BOUNDARY_VERSION,
        "first_crossing_boundary_scope": BOUNDARY_SCOPE,
        "prior_descendant_body_creation_operation_type": (
            PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE
        ),
        "prior_descendant_body_creation_operation_outcome_required": (
            PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED
        ),
        "prior_descendant_body_creation_result_required": (
            PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED
        ),
        "prior_descendant_body_creation_supported_required": (
            PRIOR_DESCENDANT_BODY_CREATION_SUPPORTED_REQUIRED
        ),
        "prior_descendant_body_creation_authorized_required": (
            PRIOR_DESCENDANT_BODY_CREATION_AUTHORIZED_REQUIRED
        ),
        "prior_descendant_body_creation_performed_required": (
            PRIOR_DESCENDANT_BODY_CREATION_PERFORMED_REQUIRED
        ),
        "prior_descendant_body_a_created_required": PRIOR_DESCENDANT_BODY_A_CREATED_REQUIRED,
        "prior_descendant_body_b_created_required": PRIOR_DESCENDANT_BODY_B_CREATED_REQUIRED,
        "prior_descendant_body_created_required": PRIOR_DESCENDANT_BODY_CREATED_REQUIRED,
        "prior_standing_descendant_created_required": (
            PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED
        ),
        "prior_descendant_standing_check_performed_required": (
            PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED
        ),
        "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
        "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
        "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
        "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
        "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
        "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "descendant_body_a_id": DESCENDANT_BODY_A_ID,
        "descendant_body_b_id": DESCENDANT_BODY_B_ID,
        "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
        "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
        "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
        "candidate_a_role": CANDIDATE_A_ROLE,
        "candidate_b_role": CANDIDATE_B_ROLE,
        "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
        "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
        "first_crossing_boundary_result": (
            "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"
            if allowed
            else "REQUIRES_DESCENDANT_BODY_CREATION"
            if requires_descendant_body_creation
            else "NOT_EVALUATED"
        ),
    }
    boundary.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if allowed:
        boundary.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    boundary.update(marker_flags)
    return boundary


def _boundary_material(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    return {
        "descendant_body_creation_reference": {
            "prior_descendant_body_creation_operation_type": (
                PRIOR_DESCENDANT_BODY_CREATION_OPERATION_TYPE
            ),
            "prior_descendant_body_creation_operation_outcome": (
                PRIOR_DESCENDANT_BODY_CREATION_OPERATION_OUTCOME_REQUIRED
            ),
            "prior_descendant_body_creation_result": (
                PRIOR_DESCENDANT_BODY_CREATION_RESULT_REQUIRED
            ),
            "prior_descendant_body_creation_supported": allowed,
            "prior_descendant_body_creation_authorized": allowed,
            "prior_descendant_body_creation_performed": allowed,
            "prior_descendant_body_a_created": allowed,
            "prior_descendant_body_b_created": allowed,
            "prior_descendant_body_created": allowed,
        },
        "descendant_body_pair_reference": {
            "descendant_body_a_id": DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": DESCENDANT_BODY_B_ID,
            "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
            "descendant_body_a_created": allowed,
            "descendant_body_b_created": allowed,
            "descendant_body_created": allowed,
            "descendant_body_a_is_first_crossing": False,
            "descendant_body_b_is_first_crossing": False,
            "descendant_body_creation_is_first_crossing": False,
            "descendant_body_is_crossing": False,
            "descendant_body_is_relation": False,
            "descendant_body_is_presence": False,
            "descendant_body_is_identity": False,
            "descendant_body_pair_non_hierarchy_preserved": allowed,
            "descendant_bodies_remain_sibling": allowed,
            "coupling_created": False,
        },
        "boundary_evaluation": {
            "first_crossing_operation_consideration_allowed": allowed,
            "first_crossing_boundary_result": (
                "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"
                if allowed
                else "REQUIRES_DESCENDANT_BODY_CREATION"
                if outcome == OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION
                else "NOT_EVALUATED"
            ),
            "first_crossing_authorized": False,
            "crossing_authorized": False,
            "first_crossing_performed": False,
            "crossing_performed": False,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "first_crossing_boundary_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("first_crossing_boundary")
    boundary_map = boundary if isinstance(boundary, Mapping) else {}
    checks = result.get("first_crossing_boundary_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("boundary_result_detail")
    detail_map = detail if isinstance(detail, Mapping) else {}
    upstream = result.get("upstream_basis")
    upstream_map = upstream if isinstance(upstream, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(
            item.get("passed") is False for item in records if isinstance(item, Mapping)
        ),
        "passed_check_count": sum(
            item.get("passed") is True for item in records if isinstance(item, Mapping)
        ),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "selected_first_crossing_boundary_spec_path": upstream_map.get(
            "first_crossing_boundary_spec_reference"
        ),
        "completed_descendant_body_creation_operation_terminal_summary_path": upstream_map.get(
            "descendant_body_creation_operation_terminal_summary_reference"
        ),
        "missing_or_insufficient_descendant_body_creation": list(
            detail_map.get("missing_or_insufficient_descendant_body_creation", [])
        ),
    }
    summary.update({key: boundary_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary.update({field: boundary_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_first_crossing_boundary_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one boundary result."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_descendant_body_creation: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    marker_flags = _marker_flags(checks)
    boundary = _boundary_object(outcome, marker_flags)
    result: dict[str, Any] = {
        "first_crossing_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_first_crossing_boundary_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "first_crossing_boundary_spec_reference": request.get(
                "first_crossing_boundary_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "first_crossing_boundary": boundary,
        "first_crossing_boundary_material": _boundary_material(outcome),
        "first_crossing_boundary_checks": checks,
        "first_crossing_boundary_statement": {
            "outcome": outcome,
            **{field: boundary.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "first_crossing_boundary_result": boundary["first_crossing_boundary_result"],
            "first_crossing_authorized": False,
            "crossing_authorized": False,
            "first_crossing_performed": False,
            "crossing_performed": False,
            "relation_created": False,
            "runtime_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "first_crossing_boundary_non_meaning": {
            "not_first_crossing_operation": True,
            "not_first_crossing_completion": True,
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
            "first_crossing_boundary_result": boundary["first_crossing_boundary_result"],
            "missing_or_insufficient_descendant_body_creation": list(
                missing_descendant_body_creation or []
            ),
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "first_crossing_operation_requires_separate_bounded_step": True,
        },
        "blocked_routes": list(BLOCKED_ROUTES),
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
    result["first_crossing_boundary_summary"] = _build_summary(result)
    return _json_ready(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_descendant_body_creation: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_descendant_body_creation=missing_descendant_body_creation,
        block_code=code,
        block_reason=reason,
    )


def build_declared_first_crossing_boundary_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit boundary request without repository discovery."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "first_crossing_boundary_spec_reference": (
            DEFAULT_FIRST_CROSSING_BOUNDARY_SPEC_REFERENCE
        ),
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_first_crossing_boundary_v0_min(
    declared_first_crossing_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one first-crossing boundary allowance without crossing behavior."""

    if declared_first_crossing_boundary is None:
        request = build_declared_first_crossing_boundary_v0_min_request()
    elif not isinstance(declared_first_crossing_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_first_crossing_boundary).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_first_crossing_boundary))

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
    request_failure = _request_posture_failure(checks, request)
    _validate_declared_non_claims(checks, request)
    failed_codes = _failed_codes(checks)
    if request_failure:
        return _blocked_result(request, checks, request_failure, "request asks for prohibited posture")
    if failed_codes:
        code = failed_codes[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}")

    target_failure = _validate_target_spec(checks, request)
    if target_failure:
        return _blocked_result(request, checks, target_failure, "target boundary specification is insufficient")

    missing_descendant_body_creation, upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required non-boundary upstream summary is insufficient",
            missing_descendant_body_creation,
        )
    if missing_descendant_body_creation:
        return _build_result(
            request,
            OUTCOME_REQUIRES_DESCENDANT_BODY_CREATION,
            checks,
            missing_descendant_body_creation=missing_descendant_body_creation,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)
    return _build_result(request, OUTCOME_ALLOWED, checks)


def resolve_first_crossing_boundary_v0_min_from_path(
    declared_first_crossing_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""

    path = Path(declared_first_crossing_boundary_path)
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request path readable",
            False,
            "readable JSON request",
            str(path),
            "REQUEST_PATH_UNREADABLE",
        )
        return _blocked_result({}, checks, "REQUEST_PATH_UNREADABLE", "request path is unreadable")
    try:
        payload = json.loads(text)
    except json.JSONDecodeError:
        checks = []
        _add_check(
            checks,
            "request JSON parseable",
            False,
            "JSON object",
            "invalid JSON",
            "REQUEST_JSON_INVALID",
        )
        return _blocked_result({}, checks, "REQUEST_JSON_INVALID", "request JSON is invalid")
    return resolve_first_crossing_boundary_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise FirstCrossingBoundaryV0MinError("no deterministic output suffix available")


def write_first_crossing_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one result with a deterministic non-overwriting filename."""

    if not isinstance(result, Mapping):
        raise FirstCrossingBoundaryV0MinError("WRITE_REFUSED: result must be a mapping")
    requested = (
        Path(output_path)
        if output_path is not None
        else REPO_ROOT / OUTPUT_ROOT / DETERMINISTIC_FILENAME
    )
    destination = _next_output_path(requested)
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(_json_ready(result), indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except OSError as error:
        raise FirstCrossingBoundaryV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination
