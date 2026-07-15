"""Resolve one bounded relation-boundary result from declared local references.

This resolver can record only ``RELATION_BOUNDARY`` after clean completed
first-crossing v2 support.  It allows consideration of a separately bounded
future relation operation only; it does not authorize or create relation,
coupling, runtime, authority, presence, identity, standing, or follow-on
work.  It reads only the declared Markdown references and never scans the
repository or mutates an upstream artifact.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RelationBoundaryV0MinError(Exception):
    """Raised when a relation-boundary result cannot be written safely."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_relation_boundary_v0_min"

BOUNDARY_ID = "relation_boundary_001"
BOUNDARY_TYPE = "RELATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_RELATION_AFTER_FIRST_CROSSING_ONLY"

PRIOR_FIRST_CROSSING_OPERATION_TYPE = "FIRST_CROSSING_OPERATION"
PRIOR_FIRST_CROSSING_OPERATION_OUTCOME_REQUIRED = "FIRST_CROSSING_OPERATION_RECORDED"
PRIOR_FIRST_CROSSING_RESULT_REQUIRED = "FIRST_CROSSING_SUPPORTED"
PRIOR_FIRST_CROSSING_SUPPORTED_REQUIRED = True
PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED = True
PRIOR_CROSSING_AUTHORIZED_REQUIRED = True
PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED = True
PRIOR_CROSSING_PERFORMED_REQUIRED = True
PRIOR_FIRST_CROSSING_A_RECORDED_REQUIRED = True
PRIOR_FIRST_CROSSING_B_RECORDED_REQUIRED = True
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED = False
PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "RELATION_BOUNDARY_THEN_RELATION_OPERATION_ONLY"

FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
FIRST_CROSSING_PAIR_SCOPE = "SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
DESCENDANT_BODY_PAIR_SCOPE = "SEPARATE_DESCENDANT_BODY_RECORDS_ONLY"
CANDIDATE_A_STANDING_SOURCE_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_B_STANDING_SOURCE_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_A_STANDING_LABEL = "CANDIDATE_A_STANDING"
CANDIDATE_B_STANDING_LABEL = "CANDIDATE_B_STANDING"

OUTCOME_ALLOWED = "RELATION_BOUNDARY_ALLOWED"
OUTCOME_REQUIRES_FIRST_CROSSING = "RELATION_BOUNDARY_REQUIRES_FIRST_CROSSING"
OUTCOME_BLOCKED = "RELATION_BOUNDARY_BLOCKED"
OUTCOME_NOT_RECORDED = "RELATION_BOUNDARY_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_ALLOWED,
    OUTCOME_REQUIRES_FIRST_CROSSING,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_RELATION_BOUNDARY"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RELATION_BOUNDARY"
INTENT_BLOCK = "BLOCK_RELATION_BOUNDARY"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_relation_boundary_v0_min")
DETERMINISTIC_FILENAME = "relation_boundary_001__relation_boundary_v0_min_result.json"

DEFAULT_RELATION_BOUNDARY_SPEC_REFERENCE = "spec/RELATION_BOUNDARY_V0_MIN_SPEC.md"
DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "relation_boundary_recorded",
    "relation_boundary_result_recorded",
    "relation_operation_consideration_allowed",
    "first_crossing_operation_referenced",
    "first_crossing_a_referenced",
    "first_crossing_b_referenced",
    "first_crossing_pair_referenced",
)

# This is the complete false posture from the governing boundary specification.
# The seven recorded fields are present here so incoming declarations must still
# deny them; the resolved boundary object can set only those seven true.
REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_RECORDED_FIELDS,
    "relation_authorized",
    "relation_created",
    "relation_operation_performed",
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
    "coupling_assigned_to_first_crossing_a",
    "coupling_assigned_to_first_crossing_b",
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
    "first_crossing_operation_v1_repaired",
    "first_crossing_operation_v1_overwritten",
    "first_crossing_operation_v1_converted_to_standing",
    "first_crossing_operation_v2_overridden",
    "first_crossing_operation_v2_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_relation_boundary_to_relation_operation_completion",
    "direct_first_crossing_to_relation_without_relation_boundary_and_operation",
    "direct_crossing_authorization_to_relation",
    "direct_crossing_performance_to_relation",
    "direct_relation_boundary_to_relation_authorization",
    "direct_relation_boundary_to_relation_creation",
    "direct_relation_boundary_to_field_machinery",
    "direct_relation_boundary_to_runtime",
    "direct_relation_boundary_to_authority_currentness",
    "direct_relation_boundary_to_coupling_assignment",
    "direct_relation_boundary_to_coupling_creation",
    "direct_relation_boundary_to_third_candidate_route",
    "direct_relation_boundary_to_third_model_route",
    "direct_relation_boundary_to_presence",
    "direct_relation_boundary_to_identity",
    "direct_relation_boundary_to_standing_descendant",
    "direct_relation_boundary_to_descendant_standing",
    "direct_relation_boundary_to_output_action",
    "direct_relation_boundary_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "RELATION_BOUNDARY_SPEC_REFERENCE_MISSING",
    "RELATION_BOUNDARY_SPEC_MARKER_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_MISSING_OR_INSUFFICIENT",
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
    "request_relation_authorization": "PROHIBITED_RELATION_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_REQUESTED",
    "request_relation_operation_performed": "PROHIBITED_RELATION_REQUESTED",
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
    "request_coupling_assignment_to_first_crossing_a": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
    "request_coupling_assignment_to_first_crossing_b": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
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
    "boundary_id": BOUNDARY_ID,
    "boundary_type": BOUNDARY_TYPE,
    "boundary_version": BOUNDARY_VERSION,
    "boundary_scope": BOUNDARY_SCOPE,
    "relation_boundary_id": BOUNDARY_ID,
    "relation_boundary_type": BOUNDARY_TYPE,
    "relation_boundary_version": BOUNDARY_VERSION,
    "relation_boundary_scope": BOUNDARY_SCOPE,
    "prior_first_crossing_operation_type": PRIOR_FIRST_CROSSING_OPERATION_TYPE,
    "prior_first_crossing_operation_outcome_required": (
        PRIOR_FIRST_CROSSING_OPERATION_OUTCOME_REQUIRED
    ),
    "prior_first_crossing_result_required": PRIOR_FIRST_CROSSING_RESULT_REQUIRED,
    "prior_first_crossing_supported_required": PRIOR_FIRST_CROSSING_SUPPORTED_REQUIRED,
    "prior_first_crossing_authorized_required": PRIOR_FIRST_CROSSING_AUTHORIZED_REQUIRED,
    "prior_crossing_authorized_required": PRIOR_CROSSING_AUTHORIZED_REQUIRED,
    "prior_first_crossing_performed_required": PRIOR_FIRST_CROSSING_PERFORMED_REQUIRED,
    "prior_crossing_performed_required": PRIOR_CROSSING_PERFORMED_REQUIRED,
    "prior_first_crossing_a_recorded_required": PRIOR_FIRST_CROSSING_A_RECORDED_REQUIRED,
    "prior_first_crossing_b_recorded_required": PRIOR_FIRST_CROSSING_B_RECORDED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
    "prior_standing_descendant_created_required": (
        PRIOR_STANDING_DESCENDANT_CREATED_REQUIRED
    ),
    "prior_descendant_standing_check_performed_required": (
        PRIOR_DESCENDANT_STANDING_CHECK_PERFORMED_REQUIRED
    ),
    "prior_follow_on_authorized_required": PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED,
    "prior_follow_on_work_authorized_required": PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED,
    "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    "first_crossing_a_id": FIRST_CROSSING_A_ID,
    "first_crossing_b_id": FIRST_CROSSING_B_ID,
    "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
    "descendant_body_a_id": DESCENDANT_BODY_A_ID,
    "descendant_body_b_id": DESCENDANT_BODY_B_ID,
    "descendant_body_pair_scope": DESCENDANT_BODY_PAIR_SCOPE,
    "candidate_a_standing_source_id": CANDIDATE_A_STANDING_SOURCE_ID,
    "candidate_b_standing_source_id": CANDIDATE_B_STANDING_SOURCE_ID,
    "candidate_a_role": CANDIDATE_A_ROLE,
    "candidate_b_role": CANDIDATE_B_ROLE,
    "candidate_a_standing_label": CANDIDATE_A_STANDING_LABEL,
    "candidate_b_standing_label": CANDIDATE_B_STANDING_LABEL,
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "boundary identity",
        ((
            "Relation Boundary V0 Minimum Specification",
            BOUNDARY_TYPE,
            BOUNDARY_ID,
            BOUNDARY_SCOPE,
        ),),
    ),
    (
        "first-crossing operation basis",
        ((
            PRIOR_FIRST_CROSSING_OPERATION_OUTCOME_REQUIRED,
            PRIOR_FIRST_CROSSING_RESULT_REQUIRED,
            "first_crossing_supported = true",
            "first_crossing_authorized = true",
            "crossing_authorized = true",
            "first_crossing_performed = true",
            "crossing_performed = true",
            "first_crossing_a_recorded = true",
            "first_crossing_b_recorded = true",
            "First Crossing A and First Crossing B were evaluated, supported, authorized, performed, and recorded as first-crossing records only",
        ),),
    ),
    (
        "first-crossing non-conversion",
        (
            (
                "first crossing is not relation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
                "first crossing is not follow-on authorization",
                "first crossing is not follow-on work authorization",
                "first crossing is not standing descendant",
                "first crossing is not descendant standing",
                "crossing authorization and performance are not relation creation",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
            ),
            (
                "First crossing is not relation, coupling, presence, identity, follow-on authorization, follow-on work authorization, standing descendant, or descendant standing",
                "crossing authorization and performance are not relation creation",
                "relation_created = false",
                "coupling_created = false",
                "presence_established = false",
                "identity_created = false",
                "standing_descendant_created = false",
                "descendant_standing_check_performed = false",
                "follow_on_authorized = false",
                "follow_on_work_authorized = false",
            ),
        ),
    ),
    (
        "boundary permitted result",
        ((
            OUTCOME_ALLOWED,
            OUTCOME_REQUIRES_FIRST_CROSSING,
            OUTCOME_BLOCKED,
            "RELATION_OPERATION_CONSIDERATION_ALLOWED",
            "REQUIRES_FIRST_CROSSING",
        ),),
    ),
    (
        "boundary non-conversion",
        ((
            "Relation boundary is not relation operation",
            "Relation boundary permission is not relation creation",
            "Relation operation consideration is not relation",
            "First crossing is not relation",
            "Crossing authorization is not relation creation",
            "Crossing performance is not relation creation",
            "First crossing is not coupling",
            "First crossing is not presence",
            "First crossing is not identity",
        ),),
    ),
    (
        "sibling non-hierarchy",
        (
            (
                "First Crossing A and First Crossing B remain sibling records",
                "neither first crossing ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records",
                "neither descendant body ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings",
                "neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "coupling remains unassigned",
            ),
            (
                "First Crossing A and First Crossing B remain sibling records; neither ranks above the other",
                "Descendant Body A and Descendant Body B remain sibling records; neither ranks above the other",
                "Candidate A and Candidate B remain sibling candidate standings; neither candidate standing ranks above the other",
                "Regulation may not become sovereign over Motion",
                "Motion may not erase Regulation",
                "Coupling remains unassigned",
            ),
        ),
    ),
    (
        "permitted route",
        ((
            ADMISSIBLE_FUTURE_ROUTE,
            "Only after a future relation boundary records RELATION_OPERATION_CONSIDERATION_ALLOWED may a separately bounded relation operation be considered",
            "No later operation is authorized by this boundary spec alone",
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
                "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md",
                "remains preserved contaminated lineage",
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
            "direct relation boundary to relation operation completion",
            "direct first crossing to relation without relation boundary and operation",
            "direct crossing authorization to relation",
            "direct crossing performance to relation",
            "direct relation boundary to relation authorization",
            "direct relation boundary to relation creation",
            "direct relation boundary to FIELD machinery",
            "direct relation boundary to runtime",
            "direct relation boundary to authority/currentness",
            "direct relation boundary to coupling assignment",
            "direct relation boundary to coupling creation",
            "direct relation boundary to third-candidate route",
            "direct relation boundary to third-model route",
            "direct relation boundary to presence",
            "direct relation boundary to identity",
            "direct relation boundary to standing descendant",
            "direct relation boundary to descendant standing",
            "direct relation boundary to output/action",
            "direct relation boundary to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        ((
            "This boundary spec defines only a future relation boundary shape",
            "It does not authorize relation",
            "Relation boundary is not relation operation",
            "Relation boundary permission is not relation creation",
            "Relation operation consideration is not relation",
            "First crossing is not relation",
            "Crossing authorization is not relation creation",
            "Crossing performance is not relation creation",
            "First crossing is not coupling",
            "First crossing is not presence",
            "First crossing is not identity",
            "First-crossing, if later used as relation basis, remains prior basis only",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

# The completed v2 first-crossing line is the sole basis whose absence is a
# bounded ``REQUIRES_FIRST_CROSSING`` result.  The other declared summaries
# remain required local context and are blocking if absent or malformed.
UPSTREAM_REQUIREMENTS = (
    (
        "first_crossing_operation_v2_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "FIRST_CROSSING_OPERATION_RECORDED",
            "failed_check_count = 0",
            "passed_check_count = 243",
            "FIRST_CROSSING_SUPPORTED",
            "first_crossing_supported = true",
            "first_crossing_authorized = true",
            "crossing_authorized = true",
            "first_crossing_performed = true",
            "crossing_performed = true",
            "first_crossing_a_recorded = true",
            "first_crossing_b_recorded = true",
            "First Crossing A and First Crossing B were evaluated, supported, authorized, performed, and recorded as first-crossing records only",
            "first crossing is not relation",
            "first crossing is not coupling",
            "first crossing is not presence",
            "first crossing is not identity",
            "first crossing is not follow-on authorization",
            "first crossing is not follow-on work authorization",
            "first crossing is not standing descendant",
            "first crossing is not descendant standing",
            "crossing authorization is not relation creation",
            "crossing performance is not relation creation",
            "relation_created = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "standing_descendant_created = false",
            "descendant_standing_check_performed = false",
            "follow_on_authorized = false",
            "follow_on_work_authorized = false",
        ),),
        "completed_first_crossing_operation_v2_terminal_summary_markers_present",
        True,
    ),
    (
        "first_crossing_boundary_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        (("FIRST_CROSSING_OPERATION_CONSIDERATION_ALLOWED",),),
        "completed_first_crossing_boundary_terminal_summary_markers_present",
        False,
    ),
    (
        "descendant_body_creation_operation_terminal_summary_reference",
        DEFAULT_DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DESCENDANT_BODY_CREATION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            (
                "DESCENDANT_BODY_CREATION_SUPPORTED",
                "Descendant Body A and Descendant Body B were evaluated, supported, and created as descendant-body records only",
                "while preserving relation, presence, identity, coupling, and follow-on false",
            ),
            (
                "DESCENDANT_BODY_CREATION_SUPPORTED",
                "Descendant Body A and Descendant Body B were created as descendant-body records only",
                "preserved no standing descendant, crossing, relation, presence, identity, or follow-on",
            ),
        ),
        "completed_descendant_body_creation_operation_terminal_summary_markers_present",
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
)

WHAT_REMAINS_OPEN = (
    "relation operation, if separately bounded after boundary",
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
    "direct relation boundary to relation operation completion",
    "direct first crossing to relation without relation boundary and operation",
    "direct crossing authorization to relation",
    "direct crossing performance to relation",
    "direct relation boundary to relation authorization",
    "direct relation boundary to relation creation",
    "direct relation boundary to FIELD machinery",
    "direct relation boundary to runtime",
    "direct relation boundary to authority/currentness",
    "direct relation boundary to coupling assignment",
    "direct relation boundary to coupling creation",
    "direct relation boundary to third-candidate route",
    "direct relation boundary to third-model route",
    "direct relation boundary to presence",
    "direct relation boundary to identity",
    "direct relation boundary to standing descendant",
    "direct relation boundary to descendant standing",
    "direct relation boundary to output/action",
    "direct relation boundary to follow-on work",
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
    """Return a deterministic JSON-safe projection without raw source bodies."""

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
        _add_check(
            checks,
            f"prohibited request flag {field}",
            value is not True,
            False,
            value,
            code,
        )
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
    reference = request.get("relation_boundary_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "relation-boundary specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "RELATION_BOUNDARY_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "RELATION_BOUNDARY_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for class_name, variants in TARGET_SPEC_MARKER_CLASSES:
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"relation-boundary specification {class_name} markers present",
            present,
            "posture marker class present",
            present,
            "RELATION_BOUNDARY_SPEC_MARKER_MISSING",
        )
        if not present and failure is None:
            failure = "RELATION_BOUNDARY_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_first_crossing: list[str] = []
    blocking_failure: str | None = None
    for field, _, missing_code, marker_code, variants, flag, is_first_crossing_basis in UPSTREAM_REQUIREMENTS:
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
            if is_first_crossing_basis:
                missing_first_crossing.append(field)
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
            if is_first_crossing_basis:
                missing_first_crossing.append(field)
            elif blocking_failure is None:
                blocking_failure = marker_code
    return missing_first_crossing, blocking_failure


def _boundary_result_value(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return "RELATION_OPERATION_CONSIDERATION_ALLOWED"
    if outcome == OUTCOME_REQUIRES_FIRST_CROSSING:
        return "REQUIRES_FIRST_CROSSING"
    if outcome == OUTCOME_NOT_RECORDED:
        return "NOT_RECORDED"
    return "NOT_EVALUATED"


def _boundary_object(outcome: str, marker_flags: Mapping[str, bool]) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    boundary: dict[str, Any] = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "relation_boundary_id": BOUNDARY_ID,
        "relation_boundary_type": BOUNDARY_TYPE,
        "relation_boundary_version": BOUNDARY_VERSION,
        "relation_boundary_scope": BOUNDARY_SCOPE,
        **EXPECTED_REQUEST_VALUES,
        "relation_boundary_result": _boundary_result_value(outcome),
    }
    boundary.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if allowed:
        boundary.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    boundary.update(marker_flags)
    return boundary


def _relation_boundary_material(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    return {
        "first_crossing_operation_reference": {
            "prior_first_crossing_operation_type": PRIOR_FIRST_CROSSING_OPERATION_TYPE,
            "prior_first_crossing_operation_outcome": (
                PRIOR_FIRST_CROSSING_OPERATION_OUTCOME_REQUIRED
            ),
            "prior_first_crossing_result": PRIOR_FIRST_CROSSING_RESULT_REQUIRED,
            "prior_first_crossing_supported": allowed,
            "prior_first_crossing_authorized": allowed,
            "prior_crossing_authorized": allowed,
            "prior_first_crossing_performed": allowed,
            "prior_crossing_performed": allowed,
            "prior_first_crossing_a_recorded": allowed,
            "prior_first_crossing_b_recorded": allowed,
        },
        "first_crossing_pair_reference": {
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "first_crossing_a_recorded": allowed,
            "first_crossing_b_recorded": allowed,
            "first_crossing_supported": allowed,
            "first_crossing_is_relation": False,
            "first_crossing_is_coupling": False,
            "first_crossing_is_presence": False,
            "first_crossing_is_identity": False,
            "first_crossing_is_standing_descendant": False,
            "first_crossing_is_descendant_standing": False,
            "first_crossing_pair_non_hierarchy_preserved": allowed,
            "first_crossings_remain_sibling": allowed,
            "coupling_created": False,
        },
        "relation_boundary_evaluation": {
            "relation_operation_consideration_allowed": allowed,
            "relation_boundary_result": _boundary_result_value(outcome),
            "relation_authorized": False,
            "relation_created": False,
            "relation_operation_performed": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "relation_boundary_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    boundary = result.get("relation_boundary")
    boundary_map = boundary if isinstance(boundary, Mapping) else {}
    checks = result.get("relation_boundary_checks")
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
        "selected_relation_boundary_spec_path": upstream_map.get(
            "relation_boundary_spec_reference"
        ),
        "completed_first_crossing_operation_v2_terminal_summary_path": upstream_map.get(
            "first_crossing_operation_v2_terminal_summary_reference"
        ),
        "missing_or_insufficient_first_crossing": list(
            detail_map.get("missing_or_insufficient_first_crossing", [])
        ),
    }
    summary.update({key: boundary_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary["relation_boundary_result"] = boundary_map.get("relation_boundary_result")
    summary.update({field: boundary_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_relation_boundary_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one relation boundary result."""

    return _build_summary(result)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_first_crossing: list[str] | None = None,
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    missing = list(missing_first_crossing or [])
    marker_flags = _marker_flags(checks)
    boundary = _boundary_object(outcome, marker_flags)
    result: dict[str, Any] = {
        "relation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_relation_boundary_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "relation_boundary_spec_reference": request.get(
                "relation_boundary_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "relation_boundary": boundary,
        "relation_boundary_material": _relation_boundary_material(outcome),
        "relation_boundary_checks": checks,
        "relation_boundary_statement": {
            "outcome": outcome,
            **{field: boundary.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "relation_boundary_result": boundary["relation_boundary_result"],
            "relation_authorized": False,
            "relation_created": False,
            "relation_operation_performed": False,
            "coupling_created": False,
            "runtime_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "relation_boundary_non_meaning": {
            "not_relation_authorization": True,
            "not_relation_creation": True,
            "not_relation_operation": True,
            "not_field_machinery": True,
            "not_runtime": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_standing_descendant": True,
            "not_descendant_standing": True,
            "not_follow_on": True,
        },
        "boundary_result_detail": {
            "relation_boundary_result": boundary["relation_boundary_result"],
            "missing_or_insufficient_first_crossing": missing,
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "relation_operation_requires_separate_bounded_step": True,
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
    result["relation_boundary_summary"] = _build_summary(result)
    return _json_ready(result)


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_first_crossing: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(
        request,
        OUTCOME_BLOCKED,
        checks,
        missing_first_crossing=missing_first_crossing,
        block_code=code,
        block_reason=reason,
    )


def build_relation_boundary_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit relation-boundary request without discovery."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "relation_boundary_spec_reference": DEFAULT_RELATION_BOUNDARY_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


build_declared_relation_boundary_v0_min_request = build_relation_boundary_v0_min_request


def resolve_relation_boundary_v0_min(
    declared_relation_boundary: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one local relation boundary without relation or runtime behavior."""

    if declared_relation_boundary is None:
        request = build_relation_boundary_v0_min_request()
    elif not isinstance(declared_relation_boundary, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_relation_boundary).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_relation_boundary))

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
        return _blocked_result(
            request,
            checks,
            "EXPLICIT_BLOCK_REQUESTED",
            "explicit block intent requested",
        )
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
        return _blocked_result(
            request,
            checks,
            target_failure,
            "target boundary specification is insufficient",
        )

    missing_first_crossing, upstream_failure = _validate_upstream(checks, request)
    if upstream_failure:
        return _blocked_result(
            request,
            checks,
            upstream_failure,
            "required non-first-crossing upstream summary is insufficient",
            missing_first_crossing,
        )
    if missing_first_crossing:
        return _build_result(
            request,
            OUTCOME_REQUIRES_FIRST_CROSSING,
            checks,
            missing_first_crossing=missing_first_crossing,
        )
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks)
    return _build_result(request, OUTCOME_ALLOWED, checks)


def resolve_relation_boundary_v0_min_from_path(
    declared_relation_boundary_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""

    path = Path(declared_relation_boundary_path)
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
    return resolve_relation_boundary_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if path.exists() and path.is_dir():
        raise RelationBoundaryV0MinError("WRITE_REFUSED: output path is a directory")
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RelationBoundaryV0MinError("WRITE_REFUSED: no deterministic output suffix available")


def write_relation_boundary_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one relation-boundary result without overwriting a prior result."""

    if not isinstance(result, Mapping):
        raise RelationBoundaryV0MinError("WRITE_REFUSED: result must be a mapping")
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
        raise RelationBoundaryV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination
