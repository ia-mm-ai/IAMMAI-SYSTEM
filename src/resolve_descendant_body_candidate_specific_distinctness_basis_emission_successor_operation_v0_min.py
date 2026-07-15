"""Resolve one bounded candidate-specific basis emission successor operation.

This resolver reads declared summary references only. It may emit separate,
non-standing Candidate A and Candidate B basis material after a clean successor
closure, while refusing distinctness, standing, runtime, authority, and other
downstream conversions.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class DescendantBodyCandidateSpecificDistinctnessBasisEmissionSuccessorOperationV0MinError(Exception):
    """Raised when bounded result writing cannot be completed."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min"

OPERATION_ID = "descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_001"
OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION"
OPERATION_VERSION = "0.1.0"
OPERATION_SCOPE = "EMIT_CANDIDATE_SPECIFIC_BASIS_MATERIAL_AFTER_SUCCESSOR_CLOSURE_ONLY"
PRIOR_BASIS_EMISSION_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION"
PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_REQUIRES_ADDITIONAL_BASIS"
UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_TYPE = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION"
UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED = "DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_CLOSED"
UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED = "PRIOR_ADDITIONAL_BASIS_GAP_CLOSED"
UPSTREAM_PRIOR_ADDITIONAL_BASIS_GAP_CLOSED_REQUIRED = True
UPSTREAM_CLOSURE_BASIS_RECEIVED_REQUIRED = True
UPSTREAM_CLOSURE_BASIS_AUDITED_REQUIRED = True
UPSTREAM_CLOSURE_BASIS_DIGEST_CUSTODY_SEALED_REQUIRED = True
UPSTREAM_CANDIDATE_A_MISSING_BASIS_RESOLVED_REQUIRED = True
UPSTREAM_CANDIDATE_B_MISSING_BASIS_RESOLVED_REQUIRED = True
UPSTREAM_BASIS_BEARING_SCOPE_DIVISION_MISSING_BASIS_RESOLVED_REQUIRED = True
UPSTREAM_DECLARATION_ACCEPTED_AS_BASIS_REQUIRED = True
TARGET_PRIMARY_MATERIAL_FILENAME = "AUTHORED CANDIDATE SCOPE-DIVISION DECLARATION V.2.pdf"
TARGET_PRIMARY_MATERIAL_DIGEST_SHA256 = "1ca450ea9762f2b2782b7edf3a1a08df3f292abbbd3aec78aa2890384b720dd0"
CANDIDATE_A_BASIS_ID = "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
CANDIDATE_B_BASIS_ID = "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
CANDIDATE_A_BASIS_LABEL = "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
CANDIDATE_B_BASIS_LABEL = "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
BASIS_PAIR_SCOPE = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"
ADMISSIBLE_FUTURE_ROUTE = "BASIS_EMISSION_SUCCESSOR_THEN_DISTINCTNESS_SUPPORT_RECHECK_ONLY"

OUTCOME_EMITTED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_EMITTED"
OUTCOME_REQUIRES_SUCCESSOR_CLOSURE = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_REQUIRES_SUCCESSOR_CLOSURE"
OUTCOME_BLOCKED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_BLOCKED"
OUTCOME_NOT_RECORDED = "DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_NOT_RECORDED"
OUTCOME_FAMILY = (
    OUTCOME_EMITTED,
    OUTCOME_REQUIRES_SUCCESSOR_CLOSURE,
    OUTCOME_BLOCKED,
    OUTCOME_NOT_RECORDED,
)

INTENT_RECORD = "RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION"
INTENT_BLOCK = "BLOCK_DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REPO_ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = Path("artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min")
DETERMINISTIC_FILENAME = "descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_001__basis_emission_successor_operation_v0_min_result.json"

DEFAULT_OPERATION_SPEC_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_SUCCESSOR_OPERATION_V0_MIN_SPEC.md"
DEFAULT_PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE = "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md"
DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_TERMINAL_SUMMARY_V0.md"
DEFAULT_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE = "spec/DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_V0.md"

ALLOWED_TRUE_RECORDED_FIELDS = (
    "basis_emission_successor_operation_recorded",
    "basis_emission_successor_performed",
    "basis_emission_successor_result_recorded",
    "candidate_specific_content_emitted",
    "candidate_a_basis_material_emitted",
    "candidate_b_basis_material_emitted",
    "separate_candidate_basis_material_emitted",
    "basis_pair_emitted",
    "candidate_a_basis_id_recorded",
    "candidate_b_basis_id_recorded",
    "candidate_a_basis_label_recorded",
    "candidate_b_basis_label_recorded",
    "candidate_a_basis_from_motion_scope",
    "candidate_b_basis_from_regulation_scope",
    "basis_bearing_scope_division_referenced",
    "upstream_successor_closure_referenced",
    "prior_additional_basis_gap_closed_referenced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "candidate_records_marked_distinct",
    "candidate_records_distinct",
    "distinctness_supported_recorded",
    "distinctness_operation_rerun",
    "declaration_admitted_as_standing_basis",
    "candidate_a_scope_declared",
    "candidate_b_scope_declared",
    "basis_bearing_scope_division_declared",
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
    "successor_closure_operation_overridden",
    "successor_closure_operation_bypassed",
    "scan_performed",
    "repository_scan_performed",
    "file_discovery_performed",
    "repair_performed",
    "validation_enforced",
    "hidden_repair_performed",
    "silent_overwrite_performed",
    "direct_successor_emission_permission_to_emission_completion_conversion",
    "direct_basis_emission_to_distinctness_support",
    "direct_basis_emission_to_candidate_records_distinct",
    "direct_basis_emission_to_candidate_standing",
    "direct_basis_emission_to_descendant_body_creation",
    "direct_basis_emission_to_crossing",
    "direct_basis_emission_to_relation",
    "direct_basis_emission_to_runtime",
    "direct_basis_emission_to_authority_currentness",
    "direct_basis_emission_to_coupling_creation",
    "direct_basis_emission_to_third_candidate_route",
    "direct_basis_emission_to_third_model_route",
    "direct_basis_emission_to_presence",
    "direct_basis_emission_to_identity",
    "direct_basis_emission_to_follow_on_work",
    "direct_successor_closure_to_distinctness_support_without_emission",
    "direct_successor_closure_to_standing",
    "direct_successor_closure_to_relation",
    "direct_successor_closure_to_presence",
)

BLOCK_CODES = (
    "REQUEST_NOT_MAPPING",
    "UNSUPPORTED_INTENT",
    "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_REFERENCE_MISSING",
    "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_MARKER_MISSING",
    "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
    "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
    "UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "RESULT_POSTURE_PRECLAIMED",
    "PROHIBITED_DISTINCTNESS_SUPPORT_REQUESTED",
    "PROHIBITED_CANDIDATE_RECORDS_DISTINCT_REQUESTED",
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
    "request_distinctness_supported_recording": "PROHIBITED_DISTINCTNESS_SUPPORT_REQUESTED",
    "request_candidate_records_marked_distinct": "PROHIBITED_CANDIDATE_RECORDS_DISTINCT_REQUESTED",
    "request_candidate_records_distinct": "PROHIBITED_CANDIDATE_RECORDS_DISTINCT_REQUESTED",
    "request_distinctness_operation_rerun": "PROHIBITED_DISTINCTNESS_SUPPORT_REQUESTED",
    "request_candidate_standing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_descendant_body_creation": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_crossing_authorization": "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED",
    "request_relation_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_field_machinery_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_runtime_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_api_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_currentness_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
    "request_authority_creation": "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED",
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
    "request_repository_scan": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_file_discovery": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_repair": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_affected_file_mutation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_prior_unsupported_claim_validation": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
    "request_validation_enforcement": "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED",
}

OPERATION_SPEC_MARKER_CLASSES = (
    ("operation_identity", (
        "Descendant Body Candidate Specific Distinctness Basis Emission Successor Operation V0 Minimum Specification",
        OPERATION_TYPE,
        OPERATION_ID,
        OPERATION_SCOPE,
    )),
    ("prior_basis_emission", (
        PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
        "missing non-cosmetic candidate A scope declaration",
        "missing non-cosmetic candidate B scope declaration",
        "missing basis-bearing scope division declaration",
        "candidate_specific_content_emitted = false",
        "separate_seal_material_emitted = false",
        "separate_lineage_receipt_material_emitted = false",
        "separate_digest_material_emitted = false",
    )),
    ("successor_closure", (
        UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
        UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
        "prior_additional_basis_gap_closed = true",
        "closure_basis_received = true",
        "closure_basis_audited = true",
        "closure_basis_digest_custody_sealed = true",
        "candidate_a_missing_basis_resolved = true",
        "candidate_b_missing_basis_resolved = true",
        "basis_bearing_scope_division_missing_basis_resolved = true",
        "declaration_accepted_as_basis = true",
        "declaration_admitted_as_standing_basis = false",
        "candidate_a_scope_declared = false",
        "candidate_b_scope_declared = false",
        "basis_bearing_scope_division_declared = false",
        "distinctness_supported_recorded = false",
        "candidate_records_marked_distinct = false",
        "descendant_body_created = false",
        "presence_established = false",
        "identity_created = false",
        "follow_on_authorized = false",
    )),
    ("distinctness", (
        "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
        "distinctness_result = NOT_DISTINCT",
        "distinctness_supported = false",
    )),
    ("candidate_a_basis_shape", (
        CANDIDATE_A_BASIS_ID,
        "CANDIDATE_A",
        CANDIDATE_A_BASIS_LABEL,
        "Motion-side admissible variation",
        "Motion mandate",
        "preserves variation side of parent basis",
        "preserve variation",
        "frequency",
        "rhythm",
        "phase",
        "amplitude",
        "periodicity",
        "latency",
        "no fixed values",
        "no targets",
        "no optimization",
        "no preferred trajectory",
        "no steering",
        "non_standing_basis = true",
        "standing_created = false",
        "candidate_scope_declared = false",
        "distinctness_supported = false",
    )),
    ("candidate_b_basis_shape", (
        CANDIDATE_B_BASIS_ID,
        "CANDIDATE_B",
        CANDIDATE_B_BASIS_LABEL,
        "Regulation-side admissibility bounds",
        "Regulation mandate",
        "preserves admissibility-bound side of parent basis",
        "preserve bounds without collapsing motion",
        "coherence",
        "stability",
        "persistence",
        "damping",
        "modulation",
        "thresholds/ranges/rejection conditions",
        "no outcome encoding",
        "no constants",
        "no deciding trajectories",
        "no replacing motion with control",
        "non_standing_basis = true",
        "standing_created = false",
        "candidate_scope_declared = false",
        "distinctness_supported = false",
    )),
    ("basis_pair_non_hierarchy", (
        BASIS_PAIR_SCOPE,
        "candidate_a_and_b_are_sibling_non_standing_basis_materials = true",
        "neither_candidate_ranks_above_the_other = true",
        "regulation_not_sovereign_over_motion = true",
        "motion_does_not_erase_regulation = true",
        "coupling_assigned = false",
        "coupling_created = false",
        "third_candidate_created = false",
        "third_model_admitted = false",
        "distinctness_supported_recorded = false",
        "candidate_records_marked_distinct = false",
        "candidate_standing_authorized = false",
    )),
    ("emission_non_conversion", (
        "Candidate-specific basis emission is not distinctness support",
        "Candidate-specific basis emission is not candidate records distinctness",
        "Candidate-specific basis emission is not candidate standing",
        "Candidate-specific basis emission is not descendant-body creation",
        "Candidate-specific basis emission is not relation",
        "Candidate-specific basis emission is not runtime",
        "Candidate-specific basis emission is not currentness",
        "Candidate-specific basis emission is not authority",
        "Candidate-specific basis emission is not coupling",
        "Candidate-specific basis emission is not presence",
        "Candidate-specific basis emission is not identity",
        "Candidate-specific basis emission is not follow-on authorization",
        "Emitted candidate-specific basis material remains non-standing",
    )),
    ("successor_closure_basis_chain", (
        TARGET_PRIMARY_MATERIAL_FILENAME,
        TARGET_PRIMARY_MATERIAL_DIGEST_SHA256,
        "non-standing accepted basis",
        "V2 declaration is not admitted as standing basis",
        "V2 receipt does not erase V1",
        "V1 predecessor reference remains lineage only",
    )),
    ("permitted_route", (
        ADMISSIBLE_FUTURE_ROUTE,
        "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED",
        "Only after a future successor emission records CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED may a separately bounded distinctness-support recheck be considered",
        "No later operation is authorized by this operation specification alone",
    )),
    ("contaminated_lineage", (
        "DESCENDANT_BODY_BASIS_DERIVATION_EVENT_V0_MIN_SPEC.md remains preserved contaminated lineage",
        "descendant_body_basis_candidate_a_created = true",
        "descendant_body_basis_candidate_b_created = true",
        "descendant_body_basis_derivation_event_recorded = true",
        "UNSUPPORTED",
        "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
    )),
    ("blocked_routes", (
        "direct successor emission permission to emission completion",
        "direct basis emission to distinctness support",
        "direct basis emission to candidate records distinct",
        "direct basis emission to candidate standing",
        "direct basis emission to descendant-body creation",
        "direct basis emission to crossing",
        "direct basis emission to relation",
        "direct basis emission to runtime",
        "direct basis emission to authority/currentness",
        "direct basis emission to coupling creation",
        "direct basis emission to third-candidate route",
        "direct basis emission to third-model route",
        "direct basis emission to presence",
        "direct basis emission to identity",
        "direct basis emission to follow-on work",
        "direct successor closure to distinctness support without emission",
        "direct successor closure to standing",
        "direct successor closure to relation",
        "direct successor closure to presence",
        "repository scan route",
        "file discovery route",
        "affected-file repair route",
        "prior unsupported-claim validation route",
    )),
    ("closing_lock", (
        "This operation spec defines only a future candidate-specific distinctness basis emission successor operation shape",
        "Successor emission permission is not successor emission completion",
        "Candidate-specific basis emission is not distinctness support",
        "Candidate-specific basis emission is not presence",
        "Candidate-specific basis emission is not identity",
        "Emitted candidate-specific basis material, if later emitted, remains non-standing",
        "Only after a future successor emission records CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED may a separately bounded distinctness-support recheck be considered",
        "Open means not scheduled, not authorized, and not executed",
    )),
)

# The standing specification uses compact prose for a few posture classes;
# synthetic inputs may retain the explicit marker wording from the contract.
OPERATION_SPEC_MARKER_VARIANTS: dict[str, tuple[tuple[str, ...], ...]] = {
    "emission_non_conversion": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "emission_non_conversion"),
        (
            "Candidate-specific basis emission is not distinctness support, candidate records distinctness, candidate standing, descendant-body creation, crossing, relation, runtime, currentness, authority, coupling, presence, identity, or follow-on authorization.",
            "Emitted candidate-specific basis material remains non-standing.",
        ),
    ),
    "contaminated_lineage": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "contaminated_lineage"),
        (
            "remains preserved contaminated lineage for the unsupported existence-claim class",
            "descendant_body_basis_candidate_a_created = true",
            "descendant_body_basis_candidate_b_created = true",
            "descendant_body_basis_derivation_event_recorded = true",
            "UNSUPPORTED",
            "does not repair, edit, delete, overwrite, replace, validate, redeem, or clean the affected file",
        ),
    ),
    "blocked_routes": (
        next(markers for name, markers in OPERATION_SPEC_MARKER_CLASSES if name == "blocked_routes"),
        (
            "Direct successor emission permission to emission completion.",
            "Direct basis emission to distinctness support, candidate records distinctness, candidate standing, descendant-body creation, crossing, relation, runtime, authority/currentness, coupling creation, third-candidate route, third-model route, presence, identity, or follow-on work.",
            "Direct successor closure to distinctness support without emission, standing, relation, or presence.",
            "Repository scan, file discovery, affected-file repair, and prior unsupported-claim validation routes.",
        ),
    ),
}

UPSTREAM_REQUIREMENTS = (
    (
        "prior_basis_emission_operation_terminal_summary_reference",
        DEFAULT_PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "PRIOR_BASIS_EMISSION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 161",
            "candidate_specific_content_emitted = false",
            "separate_seal_material_emitted = false",
            "separate_lineage_receipt_material_emitted = false",
            "separate_digest_material_emitted = false",
            "missing non-cosmetic candidate A scope declaration",
            "missing non-cosmetic candidate B scope declaration",
            "missing basis-bearing scope division declaration",
        ), (
            PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 161",
            "candidate_specific_content_emitted = false",
            "separate_seal_material_emitted = false",
            "separate_lineage_receipt_material_emitted = false",
            "separate_digest_material_emitted = false",
            "missing non-cosmetic candidate A scope",
            "missing non-cosmetic candidate B scope",
            "missing basis-bearing scope division",
        )),
        "prior_basis_emission_operation_terminal_summary_markers_present",
    ),
    (
        "successor_closure_operation_terminal_summary_reference",
        DEFAULT_SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
            "failed_check_count = 0",
            "passed_check_count = 93",
            UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
            "prior_additional_basis_gap_closed = true",
            "closure_basis_received = true",
            "closure_basis_audited = true",
            "closure_basis_digest_custody_sealed = true",
            "candidate_a_missing_basis_resolved = true",
            "candidate_b_missing_basis_resolved = true",
            "basis_bearing_scope_division_missing_basis_resolved = true",
            "declaration_accepted_as_basis = true",
            "declaration_admitted_as_standing_basis = false",
            "candidate_a_scope_declared = false",
            "candidate_b_scope_declared = false",
            "basis_bearing_scope_division_declared = false",
            "distinctness_supported_recorded = false",
            "candidate_records_marked_distinct = false",
            "descendant_body_created = false",
            "presence_established = false",
            "identity_created = false",
            "follow_on_authorized = false",
        ),),
        "successor_closure_operation_terminal_summary_markers_present",
    ),
    (
        "distinctness_operation_terminal_summary_reference",
        DEFAULT_DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DISTINCTNESS_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                "distinctness_result = NOT_DISTINCT",
                "distinctness_supported = false",
                "candidate-specific content, separate seal material, separate lineage receipt material, and separate digest material are missing",
            ),
            (
                "DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_NOT_DISTINCT",
                "distinctness_result = NOT_DISTINCT",
                "distinctness_supported = false",
                "candidate-specific content was absent",
                "separate seal, receipt, and digest material were absent",
            ),
        ),
        "distinctness_operation_terminal_summary_markers_present",
    ),
    (
        "existence_claim_evidence_check_terminal_summary_reference",
        DEFAULT_EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE,
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_MARKER_MISSING",
        (("UNSUPPORTED",),),
        "existence_claim_evidence_check_terminal_summary_markers_present",
    ),
    (
        "scope_division_operation_terminal_summary_reference",
        DEFAULT_SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "SCOPE_DIVISION_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_OPERATION_REQUIRES_ADDITIONAL_BASIS",),),
        "scope_division_operation_terminal_summary_markers_present",
    ),
    (
        "receipt_operation_terminal_summary_reference",
        DEFAULT_RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "RECEIPT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "RECEIPT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_RECEIPT_OPERATION_RECORDED",),),
        "receipt_operation_terminal_summary_markers_present",
    ),
    (
        "audit_operation_terminal_summary_reference",
        DEFAULT_AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "AUDIT_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "AUDIT_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        (("DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_AUDIT_OPERATION_SATISFIES_MISSING_BASIS_REQUIREMENTS",),),
        "audit_operation_terminal_summary_markers_present",
    ),
    (
        "digest_custody_operation_terminal_summary_reference",
        DEFAULT_DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE,
        "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_REFERENCE_MISSING",
        "DIGEST_CUSTODY_OPERATION_TERMINAL_SUMMARY_MARKER_MISSING",
        ((
            "DESCENDANT_BODY_CANDIDATE_AUTHORED_SCOPE_DIVISION_DECLARATION_DIGEST_CUSTODY_OPERATION_RECORDED",
            TARGET_PRIMARY_MATERIAL_DIGEST_SHA256,
        ),),
        "digest_custody_operation_terminal_summary_markers_present",
    ),
)

WHAT_REMAINS_OPEN = (
    "distinctness-support recheck, if separately bounded after successor emission",
    "future distinctness-supported operation result",
    "divergent receipt-history route, if separately bounded",
    "carrier separation route, if separately bounded",
    "candidate-standing checks",
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
    return key.casefold() in {
        "raw_pdf", "raw_pdf_body", "raw_extracted_text", "extracted_text",
        "pdf_bytes", "file_bytes", "full_text", "full_body", "source_body", "payload",
    }


def _sanitize(value: Any, key: str = "") -> Any:
    if isinstance(value, (bytes, bytearray, memoryview)):
        return "[REDACTED_BINARY_CONTENT]"
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item, str(item_key)) for item_key, item in value.items()}
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


def _markers_present(text: str, variants: tuple[tuple[str, ...], ...]) -> bool:
    normalized = text.casefold()
    return any(all(marker.casefold() in normalized for marker in markers) for markers in variants)


def _validate_exact_values(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    expected = (
        ("operation_id", OPERATION_ID),
        ("operation_type", OPERATION_TYPE),
        ("operation_version", OPERATION_VERSION),
        ("operation_scope", OPERATION_SCOPE),
        ("basis_emission_successor_operation_id", OPERATION_ID),
        ("basis_emission_successor_operation_type", OPERATION_TYPE),
        ("basis_emission_successor_operation_version", OPERATION_VERSION),
        ("basis_emission_successor_operation_scope", OPERATION_SCOPE),
        ("prior_basis_emission_operation_type", PRIOR_BASIS_EMISSION_OPERATION_TYPE),
        ("prior_basis_emission_operation_outcome_required", PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED),
        ("prior_missing_candidate_a_scope_required", True),
        ("prior_missing_candidate_b_scope_required", True),
        ("prior_missing_basis_bearing_scope_division_required", True),
        ("upstream_successor_closure_operation_type", UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_TYPE),
        ("upstream_successor_closure_operation_outcome_required", UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED),
        ("upstream_successor_closure_result_required", UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED),
        ("upstream_prior_additional_basis_gap_closed_required", True),
        ("upstream_closure_basis_received_required", True),
        ("upstream_closure_basis_audited_required", True),
        ("upstream_closure_basis_digest_custody_sealed_required", True),
        ("upstream_candidate_a_missing_basis_resolved_required", True),
        ("upstream_candidate_b_missing_basis_resolved_required", True),
        ("upstream_basis_bearing_scope_division_missing_basis_resolved_required", True),
        ("upstream_declaration_accepted_as_basis_required", True),
        ("target_primary_material_filename", TARGET_PRIMARY_MATERIAL_FILENAME),
        ("target_primary_material_digest_sha256", TARGET_PRIMARY_MATERIAL_DIGEST_SHA256),
        ("candidate_a_basis_id", CANDIDATE_A_BASIS_ID),
        ("candidate_b_basis_id", CANDIDATE_B_BASIS_ID),
        ("candidate_a_basis_label", CANDIDATE_A_BASIS_LABEL),
        ("candidate_b_basis_label", CANDIDATE_B_BASIS_LABEL),
        ("basis_pair_scope", BASIS_PAIR_SCOPE),
        ("admissible_future_route", ADMISSIBLE_FUTURE_ROUTE),
    )
    for field, value in expected:
        _add_check(
            checks,
            f"{field} exact",
            request.get(field) == value,
            value,
            request.get(field),
            "UPSTREAM_BASIS_MISSING_OR_INSUFFICIENT",
        )


def _code_for_non_claim(key: str) -> str:
    if any(token in key for token in ("records_marked_distinct", "records_distinct")):
        return "PROHIBITED_CANDIDATE_RECORDS_DISTINCT_REQUESTED"
    if "distinctness" in key:
        return "PROHIBITED_DISTINCTNESS_SUPPORT_REQUESTED"
    if any(token in key for token in ("candidate_standing", "descendant", "standing", "crossing", "scope_declared", "declaration_admitted")):
        return "PROHIBITED_CANDIDATE_STANDING_OR_DESCENDANT_BODY_REQUESTED"
    if any(token in key for token in ("relation", "runtime", "api", "currentness", "authority", "field_machinery")):
        return "PROHIBITED_RELATION_RUNTIME_OR_AUTHORITY_REQUESTED"
    if any(token in key for token in ("coupling", "third_")):
        return "PROHIBITED_COUPLING_OR_THIRD_MODEL_REQUESTED"
    if any(token in key for token in ("presence", "identity")):
        return "PROHIBITED_PRESENCE_OR_IDENTITY_REQUESTED"
    if any(token in key for token in ("repair", "scan", "discovery", "validation", "unsupported", "affected_file", "overwrite", "edited", "deleted", "replaced", "redeemed", "contaminated")):
        return "PROHIBITED_REPAIR_SCAN_OR_VALIDATION_REQUESTED"
    return "PROHIBITED_DOWNSTREAM_AUTHORIZATION_REQUESTED"


def _validate_request_posture(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    declared = request.get("declared_non_claims")
    invalid = (
        list(REQUIRED_FALSE_NON_CLAIMS)
        if not isinstance(declared, Mapping)
        else [key for key in REQUIRED_FALSE_NON_CLAIMS if declared.get(key) is not False]
    )
    _add_check(
        checks,
        "required declared non-claims false",
        not invalid,
        "every required key exactly false",
        {"invalid_keys": invalid},
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if request.get(key) is True:
            _add_check(
                checks,
                f"top-level false posture {key} not pre-claimed",
                False,
                False,
                True,
                _code_for_non_claim(key),
            )
    for key in ALLOWED_TRUE_RECORDED_FIELDS:
        if request.get(key) is True:
            _add_check(
                checks,
                f"result-only posture {key} not pre-claimed",
                False,
                "resolver output only",
                True,
                "RESULT_POSTURE_PRECLAIMED",
            )
    if request.get("basis_emission_successor_result") == "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED":
        _add_check(
            checks,
            "result-only basis emission result not pre-claimed",
            False,
            "resolver output only",
            request.get("basis_emission_successor_result"),
            "RESULT_POSTURE_PRECLAIMED",
        )
    for field, code in PROHIBITED_REQUEST_FLAGS.items():
        _add_check(checks, f"{field} not requested", request.get(field) is not True, False, request.get(field), code)


def _validate_target_spec(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> None:
    path = _resolve_path(request.get("operation_spec_reference"))
    _add_check(
        checks,
        "operation spec reference readable",
        path is not None and path.is_file(),
        "declared readable spec path",
        str(path) if path else request.get("operation_spec_reference"),
        "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_REFERENCE_MISSING",
    )
    text = _read_text(request.get("operation_spec_reference"))
    missing = [
        name
        for name, markers in OPERATION_SPEC_MARKER_CLASSES
        if text is None or not _markers_present(text, OPERATION_SPEC_MARKER_VARIANTS.get(name, (markers,)))
    ]
    _add_check(
        checks,
        "basis emission successor operation spec posture classes present",
        not missing,
        "all required marker classes",
        {"missing_posture_classes": missing},
        "BASIS_EMISSION_SUCCESSOR_OPERATION_SPEC_MARKER_MISSING",
    )


def _validate_upstream(checks: list[dict[str, Any]], request: Mapping[str, Any]) -> list[str]:
    missing_basis: list[str] = []
    for field, _, reference_code, marker_code, variants, flag in UPSTREAM_REQUIREMENTS:
        text = _read_text(request.get(field))
        readable = text is not None
        _add_check(
            checks,
            f"{field} readable",
            readable,
            "declared readable terminal summary",
            request.get(field),
            reference_code,
            True,
        )
        present = readable and _markers_present(text, variants)
        _add_check(
            checks,
            f"{field} expected markers present",
            present,
            variants,
            {"missing_markers": [] if present else list(variants[0])},
            marker_code,
            True,
        )
        if not present:
            missing_basis.append(flag)
    return missing_basis


def _marker_flags(checks: list[dict[str, Any]]) -> dict[str, bool]:
    flags = {
        "basis_emission_successor_operation_spec_markers_present": any(
            check.get("check_name") == "basis emission successor operation spec posture classes present"
            and check.get("passed") is True
            for check in checks
        )
    }
    for field, *_, flag in UPSTREAM_REQUIREMENTS:
        flags[flag] = any(
            check.get("check_name") == f"{field} expected markers present"
            and check.get("passed") is True
            for check in checks
        )
    return flags


def _operation_object(outcome: str, flags: Mapping[str, bool]) -> dict[str, Any]:
    emitted = outcome == OUTCOME_EMITTED
    requires = outcome == OUTCOME_REQUIRES_SUCCESSOR_CLOSURE
    operation: dict[str, Any] = {
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "basis_emission_successor_operation_id": OPERATION_ID,
        "basis_emission_successor_operation_type": OPERATION_TYPE,
        "basis_emission_successor_operation_version": OPERATION_VERSION,
        "basis_emission_successor_operation_scope": OPERATION_SCOPE,
        "prior_basis_emission_operation_type": PRIOR_BASIS_EMISSION_OPERATION_TYPE,
        "prior_basis_emission_operation_outcome_required": PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
        "prior_missing_candidate_a_scope_required": True,
        "prior_missing_candidate_b_scope_required": True,
        "prior_missing_basis_bearing_scope_division_required": True,
        "upstream_successor_closure_operation_type": UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_TYPE,
        "upstream_successor_closure_operation_outcome_required": UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
        "upstream_successor_closure_result_required": UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
        "upstream_prior_additional_basis_gap_closed_required": True,
        "upstream_closure_basis_received_required": True,
        "upstream_closure_basis_audited_required": True,
        "upstream_closure_basis_digest_custody_sealed_required": True,
        "upstream_candidate_a_missing_basis_resolved_required": True,
        "upstream_candidate_b_missing_basis_resolved_required": True,
        "upstream_basis_bearing_scope_division_missing_basis_resolved_required": True,
        "upstream_declaration_accepted_as_basis_required": True,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME,
        "target_primary_material_digest_sha256": TARGET_PRIMARY_MATERIAL_DIGEST_SHA256,
        "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        **_canonical_non_claims(),
        **flags,
    }
    operation.update({
        "basis_emission_successor_operation_recorded": emitted,
        "basis_emission_successor_performed": emitted,
        "basis_emission_successor_result_recorded": emitted,
        "basis_emission_successor_result": (
            "CANDIDATE_SPECIFIC_BASIS_MATERIAL_EMITTED"
            if emitted
            else "REQUIRES_SUCCESSOR_CLOSURE" if requires else "NOT_EMITTED"
        ),
        "candidate_specific_content_emitted": emitted,
        "candidate_a_basis_material_emitted": emitted,
        "candidate_b_basis_material_emitted": emitted,
        "separate_candidate_basis_material_emitted": emitted,
        "basis_pair_emitted": emitted,
        "candidate_a_basis_id_recorded": emitted,
        "candidate_b_basis_id_recorded": emitted,
        "candidate_a_basis_label_recorded": emitted,
        "candidate_b_basis_label_recorded": emitted,
        "candidate_a_basis_from_motion_scope": emitted,
        "candidate_b_basis_from_regulation_scope": emitted,
        "basis_bearing_scope_division_referenced": emitted,
        "upstream_successor_closure_referenced": emitted,
        "prior_additional_basis_gap_closed_referenced": emitted,
    })
    return operation


def _emitted_basis_material(emitted: bool) -> dict[str, Any]:
    if not emitted:
        return {"candidate_a_basis": None, "candidate_b_basis": None, "basis_pair": None}
    return {
        "candidate_a_basis": {
            "basis_id": CANDIDATE_A_BASIS_ID,
            "candidate_record_id": "descendant_body_basis_candidate_a_001",
            "candidate_role": "CANDIDATE_A",
            "basis_label": CANDIDATE_A_BASIS_LABEL,
            "source_scope": "Motion-side admissible variation",
            "source_mandate": "Motion mandate",
            "basis_function": "preserves variation side of parent basis",
            "responsibility_terms": [
                "preserve variation", "frequency", "rhythm", "phase", "amplitude", "periodicity",
                "latency", "no fixed values", "no targets", "no optimization", "no preferred trajectory", "no steering",
            ],
            "non_standing_basis": True,
            "standing_created": False,
            "candidate_scope_declared": False,
            "distinctness_supported": False,
        },
        "candidate_b_basis": {
            "basis_id": CANDIDATE_B_BASIS_ID,
            "candidate_record_id": "descendant_body_basis_candidate_b_001",
            "candidate_role": "CANDIDATE_B",
            "basis_label": CANDIDATE_B_BASIS_LABEL,
            "source_scope": "Regulation-side admissibility bounds",
            "source_mandate": "Regulation mandate",
            "basis_function": "preserves admissibility-bound side of parent basis",
            "responsibility_terms": [
                "preserve bounds without collapsing motion", "coherence", "stability", "persistence", "damping",
                "modulation", "thresholds/ranges/rejection conditions", "no outcome encoding", "no constants",
                "no deciding trajectories", "no replacing motion with control",
            ],
            "non_standing_basis": True,
            "standing_created": False,
            "candidate_scope_declared": False,
            "distinctness_supported": False,
        },
        "basis_pair": {
            "basis_pair_scope": BASIS_PAIR_SCOPE,
            "candidate_a_and_b_are_sibling_non_standing_basis_materials": True,
            "neither_candidate_ranks_above_the_other": True,
            "regulation_not_sovereign_over_motion": True,
            "motion_does_not_erase_regulation": True,
            "coupling_assigned": False,
            "coupling_created": False,
            "third_candidate_created": False,
            "third_model_admitted": False,
            "distinctness_supported_recorded": False,
            "candidate_records_marked_distinct": False,
            "candidate_standing_authorized": False,
        },
    }


def _build_summary(result: Mapping[str, Any]) -> dict[str, Any]:
    operation = result.get("descendant_body_candidate_specific_distinctness_basis_emission_successor_operation")
    op = operation if isinstance(operation, Mapping) else {}
    checks = result.get("basis_emission_successor_operation_checks")
    records = checks if isinstance(checks, list) else []
    upstream = result.get("upstream_basis")
    basis = upstream if isinstance(upstream, Mapping) else {}
    detail = result.get("emission_result_detail")
    emission_detail = detail if isinstance(detail, Mapping) else {}
    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "failed_check_count": sum(check.get("passed") is False for check in records if isinstance(check, Mapping)),
        "passed_check_count": sum(check.get("passed") is True for check in records if isinstance(check, Mapping)),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "operation_id": op.get("operation_id"),
        "operation_type": op.get("operation_type"),
        "operation_version": op.get("operation_version"),
        "operation_scope": op.get("operation_scope"),
        "prior_basis_emission_operation_type": op.get("prior_basis_emission_operation_type"),
        "prior_basis_emission_operation_outcome_required": op.get("prior_basis_emission_operation_outcome_required"),
        "upstream_successor_closure_operation_type": op.get("upstream_successor_closure_operation_type"),
        "upstream_successor_closure_operation_outcome_required": op.get("upstream_successor_closure_operation_outcome_required"),
        "upstream_successor_closure_result_required": op.get("upstream_successor_closure_result_required"),
        "target_primary_material_filename": op.get("target_primary_material_filename"),
        "target_primary_material_digest_sha256": op.get("target_primary_material_digest_sha256"),
        "candidate_a_basis_id": op.get("candidate_a_basis_id"),
        "candidate_b_basis_id": op.get("candidate_b_basis_id"),
        "candidate_a_basis_label": op.get("candidate_a_basis_label"),
        "candidate_b_basis_label": op.get("candidate_b_basis_label"),
        "basis_pair_scope": op.get("basis_pair_scope"),
        "selected_target_spec_path": basis.get("operation_spec_reference"),
        "completed_prior_basis_emission_terminal_summary_path": basis.get("prior_basis_emission_operation_terminal_summary_reference"),
        "completed_successor_closure_terminal_summary_path": basis.get("successor_closure_operation_terminal_summary_reference"),
        "completed_distinctness_terminal_summary_path": basis.get("distinctness_operation_terminal_summary_reference"),
        "missing_or_insufficient_successor_closure_basis": emission_detail.get("missing_or_insufficient_successor_closure_basis", []),
    }
    for key in (*ALLOWED_TRUE_RECORDED_FIELDS, "basis_emission_successor_result", *REQUIRED_FALSE_NON_CLAIMS):
        summary[key] = op.get(key)
    summary["basis_emission_successor_operation_spec_markers_present"] = op.get("basis_emission_successor_operation_spec_markers_present")
    for _, _, _, _, _, flag in UPSTREAM_REQUIREMENTS:
        summary[flag] = op.get(flag)
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    outcome: str,
    checks: list[dict[str, Any]],
    missing_basis: list[str],
    block_code: str | None = None,
    block_reason: str | None = None,
) -> dict[str, Any]:
    flags = _marker_flags(checks)
    operation = _operation_object(outcome, flags)
    emitted = outcome == OUTCOME_EMITTED
    result: dict[str, Any] = {
        "basis_emission_successor_operation_metadata": {
            "operation_id": OPERATION_ID,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "generated_at": _utc_now(),
        },
        "declared_basis_emission_successor_operation_basis": _sanitize(request),
        "upstream_basis": {
            "operation_spec_reference": request.get("operation_spec_reference"),
            **{field: request.get(field) for field, *_ in UPSTREAM_REQUIREMENTS},
            **flags,
        },
        "descendant_body_candidate_specific_distinctness_basis_emission_successor_operation": operation,
        "emitted_candidate_specific_basis_material": _emitted_basis_material(emitted),
        "basis_emission_successor_operation_checks": checks,
        "basis_emission_successor_operation_statement": {
            "outcome": outcome,
            "basis_emission_successor_operation_recorded": operation["basis_emission_successor_operation_recorded"],
            "candidate_specific_content_emitted": operation["candidate_specific_content_emitted"],
            "result_level_non_claims_canonical_false": True,
        },
        "basis_emission_successor_operation_non_meaning": {
            "not_distinctness_support": True,
            "not_candidate_records_distinctness": True,
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
        "emission_result_detail": {
            "basis_emission_successor_result": operation["basis_emission_successor_result"],
            "missing_or_insufficient_successor_closure_basis": list(missing_basis),
            "candidate_specific_content_emitted": operation["candidate_specific_content_emitted"],
            "upstream_successor_closure_referenced": operation["upstream_successor_closure_referenced"],
            "prior_additional_basis_gap_closed_referenced": operation["prior_additional_basis_gap_closed_referenced"],
        },
        "permitted_future_route": [
            "evaluate declared completed summaries only",
            "emit only separate non-standing Candidate A and Candidate B basis material",
            "consider a separately bounded distinctness-support recheck only after EMITTED",
        ],
        "blocked_routes": [
            "distinctness, standing, body, relation, runtime, authority, coupling, presence, identity, repair, scan, validation, and downstream conversion routes",
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
    result["basis_emission_successor_operation_summary"] = _build_summary(result)
    return result


def _blocked_result(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
    code: str,
    reason: str,
    missing_basis: list[str] | None = None,
) -> dict[str, Any]:
    if not any(check.get("passed") is False for check in checks):
        _add_check(checks, "blocked result code emitted", False, "not blocked", reason, code)
    return _build_result(request, OUTCOME_BLOCKED, checks, missing_basis or [], code, reason)


def build_declared_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_request(
    **overrides: Any,
) -> dict[str, Any]:
    """Build the declared no-discovery request for one successor emission."""

    request: dict[str, Any] = {
        "intent": INTENT_RECORD,
        "operation_id": OPERATION_ID,
        "operation_type": OPERATION_TYPE,
        "operation_version": OPERATION_VERSION,
        "operation_scope": OPERATION_SCOPE,
        "basis_emission_successor_operation_id": OPERATION_ID,
        "basis_emission_successor_operation_type": OPERATION_TYPE,
        "basis_emission_successor_operation_version": OPERATION_VERSION,
        "basis_emission_successor_operation_scope": OPERATION_SCOPE,
        "prior_basis_emission_operation_type": PRIOR_BASIS_EMISSION_OPERATION_TYPE,
        "prior_basis_emission_operation_outcome_required": PRIOR_BASIS_EMISSION_OPERATION_OUTCOME_REQUIRED,
        "prior_missing_candidate_a_scope_required": True,
        "prior_missing_candidate_b_scope_required": True,
        "prior_missing_basis_bearing_scope_division_required": True,
        "upstream_successor_closure_operation_type": UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_TYPE,
        "upstream_successor_closure_operation_outcome_required": UPSTREAM_SUCCESSOR_CLOSURE_OPERATION_OUTCOME_REQUIRED,
        "upstream_successor_closure_result_required": UPSTREAM_SUCCESSOR_CLOSURE_RESULT_REQUIRED,
        "upstream_prior_additional_basis_gap_closed_required": True,
        "upstream_closure_basis_received_required": True,
        "upstream_closure_basis_audited_required": True,
        "upstream_closure_basis_digest_custody_sealed_required": True,
        "upstream_candidate_a_missing_basis_resolved_required": True,
        "upstream_candidate_b_missing_basis_resolved_required": True,
        "upstream_basis_bearing_scope_division_missing_basis_resolved_required": True,
        "upstream_declaration_accepted_as_basis_required": True,
        "target_primary_material_filename": TARGET_PRIMARY_MATERIAL_FILENAME,
        "target_primary_material_digest_sha256": TARGET_PRIMARY_MATERIAL_DIGEST_SHA256,
        "candidate_a_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_b_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_a_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_b_basis_label": CANDIDATE_B_BASIS_LABEL,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "operation_spec_reference": DEFAULT_OPERATION_SPEC_REFERENCE,
        **{field: default for field, default, *_ in UPSTREAM_REQUIREMENTS},
        "declared_non_claims": _canonical_non_claims(),
        **{field: False for field in ALLOWED_TRUE_RECORDED_FIELDS},
        **{field: False for field in PROHIBITED_REQUEST_FLAGS},
    }
    request.update(overrides)
    return request


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(
    declared_basis_emission_successor_operation: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Resolve one bounded successor emission without discovery or conversion."""

    if declared_basis_emission_successor_operation is None:
        request = build_declared_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_request()
    elif not isinstance(declared_basis_emission_successor_operation, Mapping):
        checks: list[dict[str, Any]] = []
        _add_check(
            checks,
            "request mapping",
            False,
            "mapping",
            type(declared_basis_emission_successor_operation).__name__,
            "REQUEST_NOT_MAPPING",
        )
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request is not a mapping")
    else:
        request = copy.deepcopy(dict(declared_basis_emission_successor_operation))

    checks: list[dict[str, Any]] = []
    intent = request.get("intent")
    _add_check(checks, "intent supported", intent in SUPPORTED_INTENTS, SUPPORTED_INTENTS, intent, "UNSUPPORTED_INTENT")
    if intent == INTENT_BLOCK:
        return _blocked_result(request, checks, "EXPLICIT_BLOCK_REQUESTED", "explicit block intent requested")
    if intent not in SUPPORTED_INTENTS:
        return _blocked_result(request, checks, "UNSUPPORTED_INTENT", "intent is unsupported")

    _validate_exact_values(checks, request)
    _validate_request_posture(checks, request)
    _validate_target_spec(checks, request)
    missing_basis = _validate_upstream(checks, request)
    non_upstream_failures = _failed_codes(checks, False)
    if non_upstream_failures:
        code = non_upstream_failures[0]
        return _blocked_result(request, checks, code, f"blocked by failed check {code}", missing_basis)
    if intent == INTENT_DO_NOT_RECORD:
        return _build_result(request, OUTCOME_NOT_RECORDED, checks, missing_basis)
    if missing_basis:
        return _build_result(request, OUTCOME_REQUIRES_SUCCESSOR_CLOSURE, checks, missing_basis)
    return _build_result(request, OUTCOME_EMITTED, checks, [])


def resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_from_path(
    declared_basis_emission_successor_operation_path: Path | str,
) -> dict[str, Any]:
    """Read one explicit JSON request object and resolve it."""

    path = Path(declared_basis_emission_successor_operation_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        checks: list[dict[str, Any]] = []
        _add_check(checks, "request path readable JSON", False, "readable JSON object", str(exc), "REQUEST_NOT_MAPPING")
        return _blocked_result({}, checks, "REQUEST_NOT_MAPPING", "request path is unreadable or not JSON")
    return resolve_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min(request)


def build_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    """Return compact successor-emission result metadata."""

    return _build_summary(result)


def write_descendant_body_candidate_specific_distinctness_basis_emission_successor_operation_v0_min_result(
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
        raise DescendantBodyCandidateSpecificDistinctnessBasisEmissionSuccessorOperationV0MinError(
            f"WRITE_REFUSED: {exc}"
        ) from exc
