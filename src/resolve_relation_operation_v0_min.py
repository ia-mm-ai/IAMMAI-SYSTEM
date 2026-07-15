"""Resolve one bounded relation-operation result from declared local references.

The resolver may record one relation between the two separate first-crossing
records only after a clean relation-boundary allowance. It preserves no FIELD
machinery, runtime, authority, coupling, presence, identity, standing,
repair, discovery, validation enforcement, or follow-on behavior.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class RelationOperationV0MinError(Exception):
    """Raised when a relation-operation result cannot be written safely."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_relation_operation_v0_min"

OPERATION_ID = "relation_operation_001"
OPERATION_TYPE = "RELATION_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY"

PRIOR_RELATION_BOUNDARY_TYPE = "RELATION_BOUNDARY"
PRIOR_RELATION_BOUNDARY_OUTCOME_REQUIRED = "RELATION_BOUNDARY_ALLOWED"
PRIOR_RELATION_BOUNDARY_RESULT_REQUIRED = "RELATION_OPERATION_CONSIDERATION_ALLOWED"
PRIOR_RELATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED = True
PRIOR_FIRST_CROSSING_OPERATION_REFERENCED_REQUIRED = True
PRIOR_FIRST_CROSSING_A_REFERENCED_REQUIRED = True
PRIOR_FIRST_CROSSING_B_REFERENCED_REQUIRED = True
PRIOR_FIRST_CROSSING_PAIR_REFERENCED_REQUIRED = True
PRIOR_RELATION_AUTHORIZED_REQUIRED = False
PRIOR_RELATION_CREATED_REQUIRED = False
PRIOR_RELATION_OPERATION_PERFORMED_REQUIRED = False
PRIOR_COUPLING_CREATED_REQUIRED = False
PRIOR_PRESENCE_ESTABLISHED_REQUIRED = False
PRIOR_IDENTITY_CREATED_REQUIRED = False
PRIOR_FOLLOW_ON_AUTHORIZED_REQUIRED = False
PRIOR_FOLLOW_ON_WORK_AUTHORIZED_REQUIRED = False
ADMISSIBLE_FUTURE_ROUTE = "RELATION_OPERATION_THEN_PRESENCE_BOUNDARY_ONLY"

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
RELATION_ID = "relation_001"
RELATION_PAIR_SCOPE = "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY"

OUTCOME_RECORDED = "RELATION_OPERATION_RECORDED"
OUTCOME_NOT_RECORDED = "RELATION_OPERATION_NOT_RECORDED"
OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE = "RELATION_OPERATION_REQUIRES_BOUNDARY_ALLOWANCE"
OUTCOME_BLOCKED = "RELATION_OPERATION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_RELATION_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_RELATION_OPERATION"
INTENT_BLOCK = "BLOCK_RELATION_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_relation_operation_v0_min")
DETERMINISTIC_FILENAME = "relation_operation_001__relation_operation_v0_min_result.json"

DEFAULT_RELATION_OPERATION_SPEC_REFERENCE = "spec/RELATION_OPERATION_V0_MIN_SPEC.md"
DEFAULT_RELATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/RELATION_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE = (
    "spec/FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_V0.md"
)
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = (
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "relation_operation_recorded",
    "relation_evaluation_performed",
    "relation_result_recorded",
    "relation_supported",
    "relation_authorized",
    "relation_created",
    "relation_operation_performed",
    "relation_recorded",
    "first_crossing_a_used_as_relation_basis",
    "first_crossing_b_used_as_relation_basis",
    "first_crossing_pair_used_as_relation_basis",
)

REQUIRED_FALSE_NON_CLAIMS = (
    *ALLOWED_TRUE_RECORDED_FIELDS,
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
    "coupling_assigned_to_relation",
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
    "relation_boundary_overridden",
    "relation_boundary_bypassed",
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
    "direct_relation_operation_spec_to_relation_operation_completion",
    "direct_relation_boundary_allowance_to_relation_without_operation",
    "direct_first_crossing_to_relation_without_relation_boundary_and_operation",
    "direct_relation_to_field_machinery",
    "direct_relation_to_runtime",
    "direct_relation_to_authority_currentness",
    "direct_relation_to_coupling_assignment",
    "direct_relation_to_coupling_creation",
    "direct_relation_to_third_candidate_route",
    "direct_relation_to_third_model_route",
    "direct_relation_to_presence",
    "direct_relation_to_identity",
    "direct_relation_to_standing_descendant",
    "direct_relation_to_descendant_standing",
    "direct_relation_to_output_action",
    "direct_relation_to_follow_on_work",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "REQUEST_PATH_UNREADABLE",
    "REQUEST_JSON_INVALID",
    "UNSUPPORTED_INTENT",
    "REQUEST_VALUE_MISMATCH",
    "RESULT_POSTURE_PRECLAIMED",
    "RELATION_OPERATION_SPEC_REFERENCE_MISSING",
    "RELATION_OPERATION_SPEC_MARKER_MISSING",
    "RELATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RELATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "FIRST_CROSSING_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "BOUNDARY_ALLOWANCE_MISSING_OR_INSUFFICIENT",
    "RELATION_NOT_SUPPORTED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
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
    "request_coupling_assignment_to_relation": "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED",
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
    "operation_id": OPERATION_ID,
    "operation_type": OPERATION_TYPE,
    "operation_version": OPERATION_VERSION,
    "operation_scope": OPERATION_SCOPE,
    "relation_operation_id": OPERATION_ID,
    "relation_operation_type": OPERATION_TYPE,
    "relation_operation_version": OPERATION_VERSION,
    "relation_operation_scope": OPERATION_SCOPE,
    "prior_relation_boundary_type": PRIOR_RELATION_BOUNDARY_TYPE,
    "prior_relation_boundary_outcome_required": PRIOR_RELATION_BOUNDARY_OUTCOME_REQUIRED,
    "prior_relation_boundary_result_required": PRIOR_RELATION_BOUNDARY_RESULT_REQUIRED,
    "prior_relation_operation_consideration_allowed_required": (
        PRIOR_RELATION_OPERATION_CONSIDERATION_ALLOWED_REQUIRED
    ),
    "prior_first_crossing_operation_referenced_required": (
        PRIOR_FIRST_CROSSING_OPERATION_REFERENCED_REQUIRED
    ),
    "prior_first_crossing_a_referenced_required": PRIOR_FIRST_CROSSING_A_REFERENCED_REQUIRED,
    "prior_first_crossing_b_referenced_required": PRIOR_FIRST_CROSSING_B_REFERENCED_REQUIRED,
    "prior_first_crossing_pair_referenced_required": (
        PRIOR_FIRST_CROSSING_PAIR_REFERENCED_REQUIRED
    ),
    "prior_relation_authorized_required": PRIOR_RELATION_AUTHORIZED_REQUIRED,
    "prior_relation_created_required": PRIOR_RELATION_CREATED_REQUIRED,
    "prior_relation_operation_performed_required": (
        PRIOR_RELATION_OPERATION_PERFORMED_REQUIRED
    ),
    "prior_coupling_created_required": PRIOR_COUPLING_CREATED_REQUIRED,
    "prior_presence_established_required": PRIOR_PRESENCE_ESTABLISHED_REQUIRED,
    "prior_identity_created_required": PRIOR_IDENTITY_CREATED_REQUIRED,
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
    "relation_id": RELATION_ID,
    "relation_pair_scope": RELATION_PAIR_SCOPE,
    "relation_result": "NOT_EVALUATED",
}

TARGET_SPEC_MARKER_CLASSES = (
    (
        "operation identity",
        ((
            "Relation Operation V0 Minimum Specification",
            OPERATION_TYPE,
            OPERATION_ID,
            OPERATION_SCOPE,
        ),),
    ),
    (
        "relation boundary allowance",
        ((
            "RELATION_BOUNDARY_ALLOWED",
            "RELATION_OPERATION_CONSIDERATION_ALLOWED",
            "relation_operation_consideration_allowed = true",
            "first_crossing_operation_referenced = true",
            "first_crossing_a_referenced = true",
            "first_crossing_b_referenced = true",
            "first_crossing_pair_referenced = true",
            "relation_authorized = false",
            "relation_created = false",
            "relation_operation_performed = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
            "follow_on_work_authorized = false",
        ),),
    ),
    (
        "first-crossing basis",
        (
            (
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "first crossing is not relation",
                "crossing authorization is not relation creation",
                "crossing performance is not relation creation",
                "first crossing is not coupling",
                "first crossing is not presence",
                "first crossing is not identity",
            ),
            (
                "FIRST_CROSSING_SUPPORTED",
                "first_crossing_supported = true",
                "first_crossing_authorized = true",
                "crossing_authorized = true",
                "first_crossing_performed = true",
                "crossing_performed = true",
                "first_crossing_a_recorded = true",
                "first_crossing_b_recorded = true",
                "first crossing is not relation, coupling, presence, or identity",
                "crossing authorization and performance are not relation creation",
            ),
        ),
    ),
    (
        "relation material",
        ((
            "relation_evaluation",
            "relation_basis_evaluation",
            "relation_pair_evaluation",
            RELATION_ID,
            RELATION_PAIR_SCOPE,
            "RELATION_SUPPORTED",
            "relation_supported = true",
            "relation_authorized = true",
            "relation_created = true",
            "relation_operation_performed = true",
            "relation_recorded = true",
            "first_crossing_a_used_as_relation_basis = true",
            "first_crossing_b_used_as_relation_basis = true",
            "first_crossing_pair_used_as_relation_basis = true",
        ),),
    ),
    (
        "relation non-conversion",
        (
            (
                "Relation operation spec is not relation operation result",
                "Relation operation permission is not relation creation",
                "Relation creation, if later supported, is not FIELD machinery",
                "Relation is not runtime",
                "Relation is not API",
                "Relation is not currentness",
                "Relation is not authority",
                "Relation is not coupling",
                "Relation is not presence",
                "Relation is not identity",
                "Relation is not follow-on authorization",
                "Relation is not follow-on work authorization",
                "Relation is not standing descendant",
                "Relation is not descendant standing",
                "Relation is not presence-bearing",
                "Relation is not identity-bearing",
                "Relation does not assign coupling",
                "Relation does not create coupling",
                "Relation does not admit a third candidate",
                "Relation does not admit a third model",
                "Relation does not establish presence",
                "Relation does not create identity",
            ),
            (
                "Relation operation spec is not relation operation result",
                "Relation operation permission is not relation creation",
                "Relation creation, if later supported, is not FIELD machinery, runtime, API, currentness, authority, coupling, presence, identity, follow-on authorization, follow-on work authorization, standing descendant, descendant standing, presence-bearing, or identity-bearing",
                "Relation does not assign or create coupling, admit a third candidate or model, establish presence, or create identity",
            ),
        ),
    ),
    (
        "prior-basis and sibling non-hierarchy",
        (
            (
                "First crossing remains prior basis",
                "First crossing is not erased by relation",
                "Crossing authorization and performance are not relation creation",
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
                "First crossing remains prior basis and is not erased by relation",
                "Crossing authorization and performance are not relation creation",
                "First Crossing A/B, Descendant Body A/B, and Candidate A/B remain sibling and non-hierarchical",
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
            "Only after a future relation operation records RELATION_SUPPORTED may a separately bounded presence boundary be considered",
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
            "direct relation operation spec to relation operation completion",
            "direct relation boundary allowance to relation without operation",
            "direct first crossing to relation without relation boundary and operation",
            "direct relation to FIELD machinery",
            "direct relation to runtime",
            "direct relation to authority/currentness",
            "direct relation to coupling assignment",
            "direct relation to coupling creation",
            "direct relation to third-candidate route",
            "direct relation to third-model route",
            "direct relation to presence",
            "direct relation to identity",
            "direct relation to standing descendant",
            "direct relation to descendant standing",
            "direct relation to output/action",
            "direct relation to follow-on work",
            "repository scan route",
            "file discovery route",
            "affected-file repair route",
            "prior unsupported-claim validation route",
        ),),
    ),
    (
        "closing lock",
        ((
            "This operation spec defines only a future relation operation shape",
            "It does not authorize relation",
            "Relation operation spec is not relation operation result",
            "Relation operation permission is not relation creation",
            "Relation, if later supported, is not FIELD machinery",
            "Relation is not coupling",
            "Relation is not presence",
            "Relation is not identity",
            "Relation is not follow-on authorization",
            "Relation is not follow-on work authorization",
            "First crossing remains prior basis only",
            "Open means not scheduled, not authorized, and not executed",
        ),),
    ),
)

UPSTREAM_REQUIREMENTS = (
    (
        "relation_boundary_terminal_summary_reference",
        DEFAULT_RELATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE,
        "RELATION_BOUNDARY_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RELATION_BOUNDARY_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "RELATION_BOUNDARY_ALLOWED",
            "failed_check_count = 0",
            "passed_check_count = 250",
            "RELATION_OPERATION_CONSIDERATION_ALLOWED",
            "relation_operation_consideration_allowed = true",
            "first_crossing_operation_referenced = true",
            "first_crossing_a_referenced = true",
            "first_crossing_b_referenced = true",
            "first_crossing_pair_referenced = true",
            "relation_authorized = false",
            "relation_created = false",
            "relation_operation_performed = false",
            "coupling_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
            "follow_on_work_authorized = false",
        ),),
        "completed_relation_boundary_terminal_summary_markers_present",
        True,
    ),
    (
        "first_crossing_operation_v2_terminal_summary_reference",
        DEFAULT_FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE,
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "FIRST_CROSSING_OPERATION_V2_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "FIRST_CROSSING_SUPPORTED",
            "first_crossing_supported = true",
            "first_crossing_authorized = true",
            "crossing_authorized = true",
            "first_crossing_performed = true",
            "crossing_performed = true",
            "first_crossing_a_recorded = true",
            "first_crossing_b_recorded = true",
            "first crossing is not relation",
            "crossing authorization is not relation creation",
            "crossing performance is not relation creation",
            "first crossing is not coupling",
            "first crossing is not presence",
            "first crossing is not identity",
        ),),
        "completed_first_crossing_operation_v2_terminal_summary_markers_present",
        False,
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
    "presence boundary, if separately bounded after relation support",
    "presence",
    "FIELD machinery",
    "runtime",
    "API",
    "currentness",
    "authority",
    "standing",
    "identity boundary",
    "output authorization",
    "action authorization",
    "derivative reception",
    "synchronization",
    "externalization boundary",
    "follow-on work",
)

BLOCKED_ROUTES = (
    "direct relation operation spec to relation operation completion",
    "direct relation boundary allowance to relation without operation",
    "direct first crossing to relation without relation boundary and operation",
    "direct relation to FIELD machinery",
    "direct relation to runtime",
    "direct relation to authority/currentness",
    "direct relation to coupling assignment",
    "direct relation to coupling creation",
    "direct relation to third-candidate route",
    "direct relation to third-model route",
    "direct relation to presence",
    "direct relation to identity",
    "direct relation to standing descendant",
    "direct relation to descendant standing",
    "direct relation to output/action",
    "direct relation to follow-on work",
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
    reference = request.get("relation_operation_spec_reference")
    text = _read_text(reference)
    _add_check(
        checks,
        "relation-operation specification reference readable",
        text is not None,
        "readable Markdown file",
        reference,
        "RELATION_OPERATION_SPEC_REFERENCE_MISSING",
    )
    if text is None:
        return "RELATION_OPERATION_SPEC_REFERENCE_MISSING"
    failure: str | None = None
    for class_name, variants in TARGET_SPEC_MARKER_CLASSES:
        present = _markers_present(text, variants)
        _add_check(
            checks,
            f"relation-operation specification {class_name} markers present",
            present,
            "posture marker class present",
            present,
            "RELATION_OPERATION_SPEC_MARKER_MISSING",
        )
        if not present and failure is None:
            failure = "RELATION_OPERATION_SPEC_MARKER_MISSING"
    return failure


def _validate_upstream(
    checks: list[dict[str, Any]], request: Mapping[str, Any]
) -> tuple[list[str], str | None]:
    missing_allowance: list[str] = []
    blocking_failure: str | None = None
    for field, _, missing_code, marker_code, variants, flag, is_allowance in UPSTREAM_REQUIREMENTS:
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
            if is_allowance:
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
            if is_allowance:
                missing_allowance.append(field)
            elif blocking_failure is None:
                blocking_failure = marker_code
    return missing_allowance, blocking_failure


def _relation_result_value(outcome: str, not_recorded_reasons: list[str]) -> str:
    if outcome == OUTCOME_RECORDED:
        return "RELATION_SUPPORTED"
    if outcome == OUTCOME_REQUIRES_BOUNDARY_ALLOWANCE:
        return "REQUIRES_BOUNDARY_ALLOWANCE"
    if outcome == OUTCOME_NOT_RECORDED and not_recorded_reasons:
        return "RELATION_NOT_SUPPORTED"
    return "NOT_EVALUATED"


def _operation_object(
    outcome: str,
    marker_flags: Mapping[str, bool],
    not_recorded_reasons: list[str],
) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "relation_operation_id": OPERATION_ID,
        "relation_operation_type": OPERATION_TYPE,
        "relation_operation_version": OPERATION_VERSION,
        "relation_operation_scope": OPERATION_SCOPE,
        **EXPECTED_REQUEST_VALUES,
        "relation_result": _relation_result_value(outcome, not_recorded_reasons),
    }
    operation.update({field: False for field in REQUIRED_FALSE_NON_CLAIMS})
    if recorded:
        operation.update({field: True for field in ALLOWED_TRUE_RECORDED_FIELDS})
    operation.update(marker_flags)
    return operation


def _operation_material(outcome: str) -> dict[str, Any]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "relation_evaluation": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "relation_supported": recorded,
            "relation_authorized": recorded,
            "relation_created": recorded,
            "relation_operation_performed": recorded,
            "relation_recorded": recorded,
            "field_machinery_created": False,
            "runtime_created": False,
            "api_created": False,
            "currentness_created": False,
            "authority_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        },
        "relation_basis_evaluation": {
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "first_crossing_pair_scope": FIRST_CROSSING_PAIR_SCOPE,
            "first_crossing_a_used_as_relation_basis": recorded,
            "first_crossing_b_used_as_relation_basis": recorded,
            "first_crossing_pair_used_as_relation_basis": recorded,
            "first_crossing_a_is_relation": False,
            "first_crossing_b_is_relation": False,
            "first_crossing_pair_is_relation": False,
            "crossing_authorization_is_relation_creation": False,
            "crossing_performance_is_relation_creation": False,
            "first_crossing_is_coupling": False,
            "first_crossing_is_presence": False,
            "first_crossing_is_identity": False,
        },
        "relation_pair_evaluation": {
            "relation_supported": recorded,
            "relation_created": recorded,
            "first_crossing_pair_used_as_relation_basis": recorded,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "first_crossings_remain_sibling": recorded,
            "first_crossing_non_hierarchy_preserved": recorded,
            "descendant_body_non_hierarchy_preserved": recorded,
            "candidate_standing_non_hierarchy_preserved": recorded,
            "regulation_not_sovereign_over_motion": recorded,
            "motion_does_not_erase_regulation": recorded,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "presence_established": False,
            "identity_created": False,
            "standing_descendant_created": False,
            "descendant_standing_check_performed": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        },
    }


def _declared_basis_projection(request: Mapping[str, Any]) -> dict[str, Any]:
    keys = (
        "intent",
        *EXPECTED_REQUEST_VALUES,
        "relation_operation_spec_reference",
        *(item[0] for item in UPSTREAM_REQUIREMENTS),
        "relation_support_found",
    )
    return {key: _json_ready(request.get(key)) for key in keys}


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("relation_operation")
    operation_map = operation if isinstance(operation, Mapping) else {}
    checks = result.get("relation_operation_checks")
    records = checks if isinstance(checks, list) else []
    detail = result.get("relation_result_detail")
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
        "selected_relation_operation_spec_path": upstream_map.get(
            "relation_operation_spec_reference"
        ),
        "completed_relation_boundary_terminal_summary_path": upstream_map.get(
            "relation_boundary_terminal_summary_reference"
        ),
        "completed_first_crossing_operation_v2_terminal_summary_path": upstream_map.get(
            "first_crossing_operation_v2_terminal_summary_reference"
        ),
        "missing_or_insufficient_boundary_allowance": list(
            detail_map.get("missing_or_insufficient_boundary_allowance", [])
        ),
        "not_recorded_reasons": list(detail_map.get("not_recorded_reasons", [])),
    }
    summary.update({key: operation_map.get(key) for key in EXPECTED_REQUEST_VALUES})
    summary["relation_result"] = operation_map.get("relation_result")
    summary.update({field: operation_map.get(field) for field in REQUIRED_FALSE_NON_CLAIMS})
    summary.update(_marker_flags([item for item in records if isinstance(item, Mapping)]))
    return _json_ready(summary)


def build_relation_operation_v0_min_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    """Build the compact JSON-safe summary for one relation operation."""

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
        "relation_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_relation_operation_basis": _declared_basis_projection(request),
        "upstream_basis": {
            "relation_operation_spec_reference": request.get(
                "relation_operation_spec_reference"
            ),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **marker_flags,
        },
        "relation_operation": operation,
        "relation_operation_material": _operation_material(outcome),
        "relation_operation_checks": checks,
        "relation_operation_statement": {
            "outcome": outcome,
            **{field: operation.get(field) for field in ALLOWED_TRUE_RECORDED_FIELDS},
            "relation_result": operation["relation_result"],
            "field_machinery_created": False,
            "runtime_created": False,
            "authority_created": False,
            "coupling_created": False,
            "presence_established": False,
            "identity_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
            "result_level_non_claims_canonical_false": True,
        },
        "relation_operation_non_meaning": {
            "not_field_machinery": True,
            "not_runtime": True,
            "not_api": True,
            "not_currentness": True,
            "not_authority": True,
            "not_coupling": True,
            "not_presence": True,
            "not_identity": True,
            "not_standing_descendant": True,
            "not_descendant_standing": True,
            "not_follow_on": True,
        },
        "relation_result_detail": {
            "relation_result": operation["relation_result"],
            "missing_or_insufficient_boundary_allowance": missing,
            "not_recorded_reasons": not_recorded,
        },
        "permitted_future_route": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "presence_boundary_requires_separate_bounded_step": True,
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
    result["relation_operation_summary"] = _build_summary(result)
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


def build_relation_operation_v0_min_request(**overrides: Any) -> dict[str, Any]:
    """Build one explicit relation-operation request without discovery."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        **EXPECTED_REQUEST_VALUES,
        "relation_operation_spec_reference": DEFAULT_RELATION_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "relation_support_found": True,
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in REQUIRED_FALSE_NON_CLAIMS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


build_declared_relation_operation_v0_min_request = build_relation_operation_v0_min_request


def resolve_relation_operation_v0_min(
    declared_relation_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one relation operation without FIELD, runtime, or coupling behavior."""

    if declared_relation_operation is None:
        request = build_relation_operation_v0_min_request()
    elif not isinstance(declared_relation_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_relation_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_relation_operation))

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
            "target operation specification is insufficient",
        )

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

    support_found = request.get("relation_support_found")
    _add_check(
        checks,
        "relation support found",
        support_found is True,
        True,
        support_found,
        "RELATION_NOT_SUPPORTED",
    )
    if support_found is not True:
        return _build_result(
            request,
            OUTCOME_NOT_RECORDED,
            checks,
            not_recorded_reasons=["relation_support_found"],
        )
    return _build_result(request, OUTCOME_RECORDED, checks)


def resolve_relation_operation_v0_min_from_path(
    declared_relation_operation_path: Path | str,
) -> dict[str, Any]:
    """Resolve one explicit JSON request path without filesystem discovery."""

    path = Path(declared_relation_operation_path)
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
    return resolve_relation_operation_v0_min(payload)


def _next_output_path(path: Path) -> Path:
    if path.exists() and path.is_dir():
        raise RelationOperationV0MinError("WRITE_REFUSED: output path is a directory")
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise RelationOperationV0MinError("WRITE_REFUSED: no deterministic output suffix available")


def write_relation_operation_v0_min_result(
    result: Mapping[str, Any], output_path: Path | str | None = None
) -> Path:
    """Write one relation-operation result without overwriting a prior result."""

    if not isinstance(result, Mapping):
        raise RelationOperationV0MinError("WRITE_REFUSED: result must be a mapping")
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
        raise RelationOperationV0MinError(f"WRITE_REFUSED: {error}") from error
    return destination
