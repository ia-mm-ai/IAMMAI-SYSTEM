"""Resolve one bounded v2 first-crossing operation result from declared summaries.

The resolver can record only two separate first-crossing records after a clean
first-crossing boundary allowance. It refuses relation, coupling, runtime,
authority, standing, repair, discovery, and downstream authorization. V2
preserves the v1 lineage while blocking follow-on-work authorization requests.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class FirstCrossingOperationV0MinV2Error(Exception):
    """Raised when a first-crossing operation result cannot be written safely."""


RESULT_VERSION = "0.2.0"
RESOLVER_MODULE = "resolve_first_crossing_operation_v0_min_v2"

OPERATION_ID = "first_crossing_operation_001"
OPERATION_TYPE = "FIRST_CROSSING_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY"

PRIOR_FIRST_CROSSING_BOUNDARY_TYPE = "FIRST_CROSSING_BOUNDARY"
PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED = "FIRST_CROSSING_BOUNDARY_ALLOWED"
PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED = (
    "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED"
)
PRIOR_FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATION_REFERENCED_REQUIRED = True
PRIOR_DESCENDANT_BODY_A_REFERENCED_REQUIRED = True
PRIOR_DESCENDANT_BODY_B_REFERENCED_REQUIRED = True
PRIOR_DESCENDANT_BODY_CREATED_REFERENCED_REQUIRED = True
PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED = False
PRIOR_CROSSING_AUTHORIZED_REQUIRED = False
PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED = False
PRIOR_CROSSING_PERFORMED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY"

DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"
FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
FIRST_CROSSING_PAIR_SCOPE = "SEPARATE_FIRST_CROSSING_RECORDS_ONLY"

OUTCOME_RECORDED = "FIRST_CROSSING_OPERATION_RECORDED"
OUTCOME_NOT_RECORDED = "FIRST_CROSSING_OPERATION_NOT_RECORDED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = (
    "FIRST_CROSSING_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
)
OUTCOME_BLOCKED = "FIRST_CROSSING_OPERATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_FIRST_CROSSING_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_FIRST_CROSSING_OPERATION"
INTENT_BLOCK = "BLOCK_FIRST_CROSSING_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path(
    "artifacts/integrity_host_v0_min_coexistence_first_crossing_operation_v0_min_v2"
)
DETERMINISTIC_FILENAME = (
    "first_crossing_operation_001__first_crossing_operation_v0_min_v2_result.json"
)

DEFAULT_FIRST_CROSSING_OPERATION_SPEC_REFERENCE = (
    "spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md"
)
DEFAULT_FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "first_crossing_operation_recorded",
    "first_crossing_evaluation_performed",
    "first_crossing_result_recorded",
    "first_crossing_a_evaluated",
    "first_crossing_b_evaluated",
    "first_crossing_a_supported",
    "first_crossing_b_supported",
    "first_crossing_supported",
    "first_crossing_authorized",
    "crossing_authorized",
    "first_crossing_performed",
    "crossing_performed",
    "first_crossing_a_recorded",
    "first_crossing_b_recorded",
)

REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_RECORDED_FIELDS,
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
    "first_crossing_boundary_overridden",
    "first_crossing_boundary_bypassed",
    "descendant_body_creation_operation_overridden",
    "descendant_body_creation_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_first_crossing_operation_spec_to_first_crossing_operation_completion",
    "direct_boundary_allowance_to_first_crossing_without_operation",
    "direct_descendant_body_creation_to_first_crossing_without_boundary_and_operation",
    "direct_first_crossing_to_relation",
    "direct_first_crossing_to_runtime",
    "direct_first_crossing_to_authority_currentness",
    "direct_first_crossing_to_coupling_creation",
    "direct_first_crossing_to_third_candidate_route",
    "direct_first_crossing_to_third_model_route",
    "direct_first_crossing_to_presence",
    "direct_first_crossing_to_identity",
    "direct_first_crossing_to_standing_descendant",
    "direct_first_crossing_to_descendant_standing",
    "direct_first_crossing_to_output_action",
    "direct_first_crossing_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "FIRST_CROSSING_OPERATION_SPEC_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_SPEC_MARKER_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
    "FIRST_CROSSING_NOT_SUPPORTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "PROHIBITED_RELATION_REQUESTED",
    "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "EXPLICIT_BLOCK_REQUESTED",
    "WRITE_REFUSED",
)

PROHIBITED_REQUEST_FLAGS = {
    "request_relation_creation": "PROHIBITED_RELATION_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_standing_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_output_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_action_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_derivative_reception_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_synchronization_authorization": "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED",
    "request_coupling_assignment_to_descendant_body_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_descendant_body_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_candidate_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_candidate_creation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_third_model_admission": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_presence_establishment": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_identity_creation": "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED",
    "request_standing_descendant_creation": "PROHIBITED_STANDING_DESCENDANT_REQUESTED",
    "request_descendant_standing": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
    "request_descendant_standing_check": "PROHIBITED_DESCENDANT_STANDING_REQUESTED",
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
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "first_crossing_operation_id": OPERATION_ID,
    "first_crossing_operation_type": OPERATION_TYPE,
    "first_crossing_operation_version": OPERATION_VERSION,
    "first_crossing_operation_scope": OPERATION_SCOPE,
    "prior_first_crossing_boundary_type": PRIOR_FIRST_CROSSING_BOUNDARY_TYPE,
    "prior_first_crossing_boundary_outcome_required": (
        PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED
    ),
    "prior_first_crossing_boundary_result_required": (
        PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED
    ),
    "prior_first_crossing_operation_consideration_allowed_required": (
        PRIOR_FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED
    ),
    "prior_descendant_body_creation_referenced_required": (
        PRIOR_DESCENDANT_BODY_CREATION_REFERENCED_REQUIRED
    ),
    "prior_descendant_body_a_referenced_required": (
        PRIOR_DESCENDANT_BODY_A_REFERENCED_REQUIRED
    ),
    "prior_descendant_body_b_referenced_required": (
        PRIOR_DESCENDANT_BODY_B_REFERENCED_REQUIRED
    ),
    "prior_descendant_body_created_referenced_required": (
        PRIOR_DESCENDANT_BODY_CREATED_REFERENCED_REQUIRED
    ),
    "prior_first_crossing_authorized_required": PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED,
    "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
    "prior_first_crossing_performed_required": PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED,
    "prior_crossing_performed_required": PRIOR_CROSSING_PERFORMED_REQUIRED,
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
    "first_crossing_a_id": FIRST_CROSSING_A_ID,
    "first_crossing_b_id": FIRST_CROSSING_B_ID,
    "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
    "first_crossing_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "operation identity",
        ((
            "First Crossing Operation V0 Minimum Specification",
            OPERATION_TYPE,
            OPERATION_ID,
            OPERATION_SCOPE,
        ),),
    ),
    (
        "boundary allowance",
        ((
            PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED,
            PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED,
            "first_crossing_operation_consideration_allowed = true",
            "descendant_body_creation_referenced = true",
            "descendant_body_a_referenced = true",
            "descendant_body_b_referenced = true",
            "descendant_body_created_referenced = true",
            "first_crossing_authorized = false",
            "crossing_authorized = false",
            "first_crossing_performed = false",
            "crossing_performed = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
    ),
    (
        "descendant-body creation",
        (
            (
                "DESCENDANT_BODY_CREATION_SUPPORTED",
                "descendant_body_creation_supported = true",
                "descendant_body_creation_authorized = true",
                "descendant_body_creation_performed = true",
                "descendant_body_a_created = true",
                "descendant_body_b_created = true",
                "descendant_body_created = true",
                "descendant body is not crossing",
                "descendant body is not relation",
                "descendant body is not presence",
                "descendant body is not identity",
            ),
            (
                "DESCENDANT_BODY_CREATION_SUPPORTED",
                "descendant_body_creation_supported = true",
                "descendant_body_creation_authorized = true",
                "descendant_body_creation_performed = true",
                "descendant_body_a_created = true",
                "descendant_body_b_created = true",
                "descendant_body_created = true",
                "Descendant Body A and Descendant Body B were created as descendant-body records only",
                "while preserving relation, presence, identity, coupling, and follow-on false",
            ),
        ),
    ),
    (
        "first-crossing material",
        ((
            "first_crossing_a_evaluation",
            "first_crossing_b_evaluation",
            "first_crossing_pair_evaluation",
            FIRST_CROSSING_A_ID,
            FIRST_CROSSING_B_ID,
            FIRST_CROSSING_PAIR_SCOPE,
            "FIRST_CROSSING_SUPPORTED",
            "first_crossing_supported = true",
            "first_crossing_authorized = true",
            "crossing_authorized = true",
            "first_crossing_performed = true",
            "crossing_performed = true",
            "first_crossing_a_recorded = true",
            "first_crossing_b_recorded = true",
        ),),
    ),
    (
        "first-crossing non-conversion",
        (
            (
                "First crossing is not relation",
                "First crossing is not coupling",
                "First crossing is not runtime",
                "First crossing is not currentness",
                "First crossing is not authority",
                "First crossing is not presence",
                "First crossing is not identity",
                "First crossing is not follow-on authorization",
                "First crossing is not standing descendant",
                "First crossing is not descendant standing",
                "First crossing is not relation participation",
                "First crossing is not presence-bearing",
                "First crossing is not identity-bearing",
                "Crossing authorization and performance are not relation creation",
            ),
            (
                "First crossing is not relation, coupling, runtime, currentness, authority, presence, identity, follow-on authorization, standing descendant, descendant standing, relation participation, presence-bearing, or identity-bearing.",
                "Crossing authorization and performance are not relation creation",
            ),
        ),
    ),
    (
        "sibling non-hierarchy",
        (
            (
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
            ),
            (
                "Descendant Body A and Descendant Body B remain sibling records; neither ranks above the other",
                "First Crossing A and First Crossing B remain sibling records; neither ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings; neither ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
            ),
        ),
    ),
    (
        "permitted route",
        ((
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future first-crossing operation records FIRST_CROSSING_SUPPORTED may a separately bounded relation boundary be considered",
            "No later operation is authorized by this operation spec alone",
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
            "direct first-crossing operation spec to first-crossing operation completion",
            "direct boundary allowance to first crossing without operation",
            "direct descendant-body creation to first crossing without boundary and operation",
            "direct first crossing to relation",
            "direct first crossing to runtime",
            "direct first crossing to authority/currentness",
            "direct first crossing to coupling creation",
            "direct first crossing to third-candidate route",
            "direct first crossing to third-model route",
            "direct first crossing to presence",
            "direct first crossing to identity",
            "direct first crossing to standing descendant",
            "direct first crossing to descendant standing",
            "direct first crossing to output/action",
            "direct first crossing to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        ((
            "This operation spec defines only a future first-crossing operation shape",
            "It does not authorize first crossing",
            "First-crossing operation spec is not first-crossing operation result",
            "First-crossing operation permission is not first-crossing completion",
            "First crossing is not relation",
            "First crossing is not coupling",
            "First crossing is not presence",
            "First crossing is not identity",
            "First-crossing, if later supported, remains prior to any relation boundary",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "first_crossing_boundary_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "FIRST_CROSSING_BOUNDARY_ALLOWED",
            "failed_check_count = 0",
            "passed_check_count = 236",
            "FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",
            "first_crossing_operation_consideration_allowed = true",
            "descendant_body_creation_referenced = true",
            "descendant_body_a_referenced = true",
            "descendant_body_b_referenced = true",
            "descendant_body_created_referenced = true",
            "first_crossing_authorized = false",
            "crossing_authorized = false",
            "first_crossing_performed = false",
            "crossing_performed = false",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "completed_first_crossing_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "descendant_body_creation_operation_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "DESCENDANT_BODY_CREATION_SUPPORTED",
            "descendant_body_creation_supported = true",
            "descendant_body_creation_authorized = true",
            "descendant_body_creation_performed = true",
            "descendant_body_a_created = true",
            "descendant_body_b_created = true",
            "descendant_body_created = true",
            "descendant body is not crossing",
            "descendant body is not relation",
            "descendant body is not presence",
            "descendant body is not identity",
        ),),
        "completed_descendant_body_creation_operation_terminal_summary_markers_present",
        True,
    ),
    (
        "descendant_body_creation_boundary_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED",),),
        "completed_descendant_body_creation_boundary_terminal_summary_markers_present",
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
    "relation boundary, if separately bounded after first-crossing support",
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
    "direct first-crossing operation spec to first-crossing operation completion",
    "direct boundary allowance to first crossing without operation",
    "direct descendant-body creation to first crossing without boundary and operation",
    "direct first crossing to relation",
    "direct first crossing to runtime",
    "direct first crossing to authority/currentness",
    "direct first crossing to coupling creation",
    "direct first crossing to third-candidate route",
    "direct first crossing to third-model route",
    "direct first crossing to presence",
    "direct first crossing to identity",
    "direct first crossing to standing descendant",
    "direct first crossing to descendant standing",
    "direct first crossing to output/action",
    "direct first crossing to follow-on work",
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
        name = check.get("check_name")
        if isinstance(name, str) and name.endswith("markers present"):
            flags[name.replace(" ", "_")] = check.get("passed") is True
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
    reference = request.get("first_crossing_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "first-crossing operation specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "FIRST_CROSSING_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "FIRST_CROSSING_OPERATION_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for class_name, variants in TARGET_SPEC_MARKER_CLASSES:
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"first-crossing operation specification {class_name} markers present",
            present,
            "posture marker class present",
            present,
            "FIRST_CROSSING_OPERATION_SPEC_MARKER_MISSING",
        )
        if not present and failure is None:
            failure = "FIRST_CROSSING_OPERATION_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_allowance: list[str] = []
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
                missing_allowance.append(field)
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
                missing_allowance.append(field)
            elif blocking_failure is None:
                blocking_failure = marker_code
    return missing_allowance, blocking_failure


def _operation_result_value(outcome: str, not_recorded_reasons: list[str]) -> str:
    if outcome == OUTCOME_RECORDED:
        return "FIRST_CROSSING_SUPPORTED"
    if outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
        return "REQUIRES_BOUNDARY_ALLOWANCE"
    if outcome == OUTCOME_NOT_RECORDED and not_recorded_reasons:
        return "FIRST_CROSSING_NOT_SUPPORTED"
    return "NOT_EVALUATED"


def _operation_object(
    outcome: str, marker_flags: Mapping[str, bool], not_recorded_reasons: list[str]
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "first_crossing_operation_id": OPERATION_ID,
        "first_crossing_operation_type": OPERATION_TYPE,
        "first_crossing_operation_version": OPERATION_VERSION,
        "first_crossing_operation_scope": OPERATION_SCOPE,
        "prior_first_crossing_boundary_type": PRIOR_FIRST_CROSSING_BOUNDARY_TYPE,
        "prior_first_crossing_boundary_outcome_required": PRIOR_FIRST_CROSSING_BOUNDARY_OUTCOME_REQUIRED,
        "prior_first_crossing_boundary_result_required": PRIOR_FIRST_CROSSING_BOUNDARY_RESULT_REQUIRED,
        "prior_first_crossing_operation_consideration_allowed_required": PRIOR_FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED_REQUIRED,
        "prior_descendant_body_creation_referenced_required": PRIOR_DESCENDANT_BODY_CREATION_REFERENCED_REQUIRED,
        "prior_descendant_body_a_referenced_required": PRIOR_DESCENDANT_BODY_A_REFERENCED_REQUIRED,
        "prior_descendant_body_b_referenced_required": PRIOR_DESCENDANT_BODY_B_REFERENCED_REQUIRED,
        "prior_descendant_body_created_referenced_required": PRIOR_DESCENDANT_BODY_CREATED_REFERENCED_REQUIRED,
        "prior_first_crossing_authorized_required": PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED,
        "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
        "prior_first_crossing_performed_required": PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED,
        "prior_crossing_performed_required": PRIOR_CROSSING_PERFORMED_REQUIRED,
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
        "first_crossing_a_id": FIRST_CROSSING_A_ID,
        "first_crossing_b_id": FIRST_CROSSING_B_ID,
        "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
        "first_crossing_result": _operation_result_value(outcome, not_recorded_reasons),
    }
    operation.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if recorded:
        operation.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    operation.update(marker_flags)
    return operation


def _operation_material(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "first_crossing_a_evaluation": {
            "first_crossing_id": FIRST_CROSSING_A_ID,
            "descendant_body_id": DESCENDANT_BODY_A_ID,
            "candidate_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
            "candidate_role": CANDIDATE_A_ROLE,
            "candidate_standing_label": CANDIDATE_A_STANDING_LABEL,
            "descendant_body_created": recorded,
            "descendant_body_is_first_crossing": False,
            "first_crossing_supported": recorded,
            "first_crossing_authorized": recorded,
            "crossing_authorized": recorded,
            "first_crossing_performed": recorded,
            "crossing_performed": recorded,
            "first_crossing_recorded": recorded,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
        },
        "first_crossing_b_evaluation": {
            "first_crossing_id": FIRST_CROSSING_B_ID,
            "descendant_body_id": DESCENDANT_BODY_B_ID,
            "candidate_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
            "candidate_role": CANDIDATE_B_ROLE,
            "candidate_standing_label": CANDIDATE_B_STANDING_LABEL,
            "descendant_body_created": recorded,
            "descendant_body_is_first_crossing": False,
            "first_crossing_supported": recorded,
            "first_crossing_authorized": recorded,
            "crossing_authorized": recorded,
            "first_crossing_performed": recorded,
            "crossing_performed": recorded,
            "first_crossing_recorded": recorded,
            "relation_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
        },
        "first_crossing_pair_evaluation": {
            "both_first_crossings_supported": recorded,
            "both_first_crossings_authorized": recorded,
            "both_first_crossings_performed": recorded,
            "both_first_crossings_recorded": recorded,
            "first_crossing_a_recorded": recorded,
            "first_crossing_b_recorded": recorded,
            "crossing_authorized": recorded,
            "crossing_performed": recorded,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "descendant_bodies_remain_sibling": recorded,
            "descendant_body_non_hierarchy_preserved": recorded,
            "candidate_standing_non_hierarchy_preserved": recorded,
            "regulation_not_sovereign_over_motion": recorded,
            "motion_does_not_erase_regulation": recorded,
            "relation_created": False,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "presence_established": False,
            "identity_created": False,
            "standing_descendant_created": False,
            "descendant_standing_check_performed": False,
            "follow_on_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "first_crossing_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
        "first_crossing_support_found",
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("first_crossing_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("first_crossing_operation_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("first_crossing_result_detail")
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
        "selected_first_crossing_operation_spec_path": upstream_map.get(
            "first_crossing_operation_spec_reference"
        ),
        "completed_first_crossing_boundary_terminal_summary_path": upstream_map.get(
            "first_crossing_boundary_terminal_summary_reference"
        ),
        "completed_descendant_body_creation_operation_terminal_summary_path": upstream_map.get(
            "descendant_body_creation_operation_terminal_summary_reference"
        ),
        "missing_or_insufficient_boundary_allowance": list(
            detail_map.get("missing_or_insufficient_boundary_allowance", [])
        ),
        "not_recorded_reasons": list(detail_map.get("not_recorded_reasons", [])),
    }
    summary.update({key: operation_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary.update({field: operation_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_first_crossing_operation_v0_min_v2_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one first-crossing operation."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_boundary_allowance: list[str] | None = None,
    not_recorded_reasons: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    missing = list(missing_boundary_allowance or [])
    not_recorded = list(not_recorded_reasons or [])
    marker_flags = _marker_flags(checks)
    operation = _operation_object(outcome, marker_flags, not_recorded)
    result: dict[str, Any] = {
        "first_crossing_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_first_crossing_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "first_crossing_operation_spec_reference": request.get(
                "first_crossing_operation_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "first_crossing_operation": operation,
        "first_crossing_operation_material": _operation_material(outcome),
        "first_crossing_operation_checks": checks,
        "first_crossing_operation_statement": {
            "outcome": outcome,
            **{field: operation.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "first_crossing_result": operation["first_crossing_result"],
            "relation_created": False,
            "runtime_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "first_crossing_operation_non_meaning": {
            "not_relation": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_standing_descendant": True,
            "not_descendant_standing": True,
            "not_follow_on": True,
        },
        "first_crossing_result_detail": {
            "first_crossing_result": operation["first_crossing_result"],
            "missing_or_insufficient_boundary_allowance": missing,
            "not_recorded_reasons": not_recorded,
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "relation_boundary_requires_separate_bounded_step": True,
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
    result["first_crossing_operation_summary"] = _build_summary(result)
    return _json_ready(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_boundary_allowance: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_boundary_allowance=missing_boundary_allowance,
        block_code=code,
        block_reason=reason,
    )


def build_first_crossing_operation_v0_min_v2_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit operation request without repository discovery."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "first_crossing_operation_spec_reference": (
            DEFAULT_FIRST_CROSSING_OPERATION_SPEC_REFERENCE
        ),
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "first_crossing_support_found": True,
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


build_declared_first_crossing_operation_v0_min_v2_request = (
    build_first_crossing_operation_v0_min_v2_request
)

# Builder aliases preserve request-shape compatibility while resolving to v2.
build_first_crossing_operation_v0_min_request = (
    build_first_crossing_operation_v0_min_v2_request
)
build_declared_first_crossing_operation_v0_min_request = (
    build_first_crossing_operation_v0_min_v2_request
)


def resolve_first_crossing_operation_v0_min_v2(
    declared_first_crossing_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded first-crossing operation without relation behavior."""

    if declared_first_crossing_operation is None:
        request = build_first_crossing_operation_v0_min_v2_request()
    elif not isinstance(declared_first_crossing_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_first_crossing_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_first_crossing_operation))

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
        return _blocked_result(request, checks, failed_codes[0], f"blocked by failed check {failed_codes[0]}")

    target_failure = _validate_target_spec(checks, request)
    if target_failure:
        return _blocked_result(request, checks, target_failure, "target operation specification is insufficient")

    missing_allowance, upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required non-boundary upstream summary is insufficient",
            missing_allowance,
        )
    if missing_allowance:
        return _build_result(
            request,
            OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
            checks,
            missing_boundary_allowance=missing_allowance,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)

    support_found = request.get("first_crossing_support_found")
    _add_check(
        checks,
        "first-crossing support found",
        support_found is True,
        True,
        support_found,
        "FIRST_CROSSING_NOT_SUPPORTED",
    )
    if support_found is not True:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            not_recorded_reasons=["first_crossing_support_found"],
        )
    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_first_crossing_operation_v0_min_v2_from_path(
    declared_first_crossing_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""

    path = Path(declared_first_crossing_operation_path)
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
    return resolve_first_crossing_operation_v0_min_v2(payload)


def _next_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise FirstCrossingOperationV0MinV2Error("no deterministic output suffix available")


def write_first_crossing_operation_v0_min_v2_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one operation result with a deterministic non-overwriting name."""

    if not isinstance(result, Mapping):
        raise FirstCrossingOperationV0MinV2Error("WRITE_REFUSED: result must be a mapping")
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
        raise FirstCrossingOperationV0MinV2Error(f"WRITE_REFUSED: {error}") from error
    return destination
