"""Pure descendant-body candidate-standing effect applicability resolver.

The resolver consumes one closed in-memory envelope and checks the exact
source-family result, complete pair preservation, supplied lineage/custody/
rank bindings, canonical non-claims, and literal route equality. It performs
no filesystem access, hashing, persistence, operation invocation, standing
derivation, or semantic interpretation.
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any


RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_standing_effect_applicability_"
    "boundary_v0_min"
)
RESULT_VERSION = "0.1.0"

BOUNDARY_ID = (
    "descendant_body_candidate_standing_effect_applicability_boundary_001"
)
BOUNDARY_TYPE = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY"
)
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_"
    "ONE_EXACT_DECLARED_DOWNSTREAM_USE_ONLY"
)

OUTCOME_RECORDED = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
)
OUTCOME_NOT_APPLICABLE = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_NOT_APPLICABLE"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_REVIEW_BLOCKED = (
    "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_REVIEW_BLOCKED"
)
OUTCOMES = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_APPLICABLE,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_REVIEW_BLOCKED,
)

SOURCE_FAMILY = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"
SOURCE_SEMANTIC_OWNER = SOURCE_FAMILY
SOURCE_CONTRACT_IDENTITY = SOURCE_FAMILY
SOURCE_CONTRACT_TYPE = SOURCE_FAMILY
SOURCE_CONTRACT_VERSION = "0.1.0"
SOURCE_CONTRACT_REFERENCE = (
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
)
SOURCE_CONTRACT_CONTENT_IDENTITY = (
    "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
)
SOURCE_ARTIFACT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_"
    "standing_operation_v0_min/descendant_body_candidate_standing_operation_"
    "001__candidate_standing_operation_v0_min_result.json"
)
SOURCE_ARTIFACT_CONTENT_IDENTITY = (
    "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
)
SOURCE_OUTCOME = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED"
SOURCE_RESULT_VERSION = "0.1.0"
SOURCE_RESOLVER_MODULE = (
    "resolve_descendant_body_candidate_standing_operation_v0_min"
)
SOURCE_FAILED_CHECK_COUNT = 0
SOURCE_PASSED_CHECK_COUNT = 176

SOURCE_OPERATION_ID = "descendant_body_candidate_standing_operation_001"
SOURCE_OPERATION_TYPE = SOURCE_FAMILY
SOURCE_OPERATION_VERSION = "0.1.0"
SOURCE_OPERATION_SCOPE = (
    "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY"
)
SOURCE_CANDIDATE_STANDING_RESULT = "CANDIDATE_STANDING_SUPPORTED"
BASIS_PAIR_SCOPE = "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY"
ADMISSIBLE_FUTURE_ROUTE = (
    "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
)

CANDIDATE_A_RECORD_ID = "descendant_body_basis_candidate_a_001"
CANDIDATE_A_ROLE = "CANDIDATE_A"
CANDIDATE_A_BASIS_ID = (
    "descendant_body_basis_candidate_a_001__motion_side_admissible_"
    "variation_basis"
)
CANDIDATE_A_BASIS_LABEL = (
    "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS"
)
CANDIDATE_B_RECORD_ID = "descendant_body_basis_candidate_b_001"
CANDIDATE_B_ROLE = "CANDIDATE_B"
CANDIDATE_B_BASIS_ID = (
    "descendant_body_basis_candidate_b_001__regulation_side_admissibility_"
    "bounds_basis"
)
CANDIDATE_B_BASIS_LABEL = (
    "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
)

STANDING_EFFECT_LOCATIONS = (
    "descendant_body_candidate_standing_operation.candidate_standing_result",
    "descendant_body_candidate_standing_operation.candidate_standing_supported",
    "descendant_body_candidate_standing_operation.candidate_standing_authorized",
    "descendant_body_candidate_standing_operation.candidate_standing_created",
    "descendant_body_candidate_standing_operation.candidate_a_standing_created",
    "descendant_body_candidate_standing_operation.candidate_b_standing_created",
    "candidate_standing_operation_material.candidate_a_standing_evaluation",
    "candidate_standing_operation_material.candidate_b_standing_evaluation",
    "candidate_standing_operation_material.standing_pair_evaluation",
    "descendant_body_candidate_standing_operation.admissible_future_route",
)

SOURCE_LINEAGE_REFERENCES = (
    SOURCE_CONTRACT_REFERENCE,
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_STANDING_BOUNDARY_TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_SUPPORT_RECHECK_"
    "OPERATION_TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_SPECIFIC_DISTINCTNESS_BASIS_EMISSION_"
    "SUCCESSOR_OPERATION_TERMINAL_SUMMARY_V0.md",
    "spec/EXISTENCE_CLAIM_EVIDENCE_CHECK_TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_RECORD_DISTINCTNESS_OPERATION_"
    "TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "SUCCESSOR_CLOSURE_OPERATION_TERMINAL_SUMMARY_V0.md",
    "spec/DESCENDANT_BODY_CANDIDATE_NON_COSMETIC_SCOPE_DIVISION_DECLARATION_"
    "OPERATION_TERMINAL_SUMMARY_V0.md",
    SOURCE_ARTIFACT_REFERENCE,
)

SOURCE_REQUIRED_FALSE_NON_CLAIMS = (
    "action_authorized",
    "affected_file_deleted",
    "affected_file_edited",
    "affected_file_overwritten",
    "affected_file_redeemed",
    "affected_file_repaired",
    "affected_file_replaced",
    "affected_file_treated_as_clean_basis",
    "api_created",
    "authority_created",
    "candidate_standing_boundary_bypassed",
    "candidate_standing_boundary_overridden",
    "contaminated_lineage_treated_as_clean_basis",
    "coupling_assigned_to_candidate_a",
    "coupling_assigned_to_candidate_b",
    "coupling_created",
    "crossing_authorized",
    "currentness_created",
    "derivative_reception_authorized",
    "descendant_body_a_created",
    "descendant_body_b_created",
    "descendant_body_created",
    "descendant_standing_check_performed",
    "direct_boundary_allowance_to_candidate_standing_without_operation",
    "direct_candidate_standing_operation_spec_to_candidate_standing_operation_completion",
    "direct_candidate_standing_to_authority_currentness",
    "direct_candidate_standing_to_coupling_creation",
    "direct_candidate_standing_to_crossing",
    "direct_candidate_standing_to_descendant_body_creation",
    "direct_candidate_standing_to_descendant_standing",
    "direct_candidate_standing_to_follow_on_work",
    "direct_candidate_standing_to_identity",
    "direct_candidate_standing_to_output_action",
    "direct_candidate_standing_to_presence",
    "direct_candidate_standing_to_relation",
    "direct_candidate_standing_to_runtime",
    "direct_candidate_standing_to_standing_descendant",
    "direct_candidate_standing_to_third_candidate_route",
    "direct_candidate_standing_to_third_model_route",
    "direct_supported_distinctness_to_candidate_standing_without_boundary_and_operation",
    "distinctness_support_recheck_operation_bypassed",
    "distinctness_support_recheck_operation_overridden",
    "field_machinery_created",
    "file_discovery_performed",
    "first_crossing_authorized",
    "follow_on_authorized",
    "follow_on_work_authorized",
    "hidden_repair_performed",
    "identity_created",
    "output_authorized",
    "presence_established",
    "prior_unsupported_candidate_a_claim_validated",
    "prior_unsupported_candidate_b_claim_validated",
    "prior_unsupported_derivation_event_claim_validated",
    "relation_created",
    "repair_performed",
    "repository_scan_performed",
    "runtime_created",
    "scan_performed",
    "silent_overwrite_performed",
    "standing_authorized",
    "standing_created",
    "standing_descendant_created",
    "synchronization_authorized",
    "third_candidate_created",
    "third_model_admitted",
    "valid_derivation_event_recorded",
    "validation_enforced",
)

REQUIRED_FALSE_NON_CLAIMS = (
    "standing_created",
    "standing_renewed",
    "standing_extended",
    "standing_reinterpreted",
    "standing_transferred",
    "standing_generalized",
    "candidate_a_independent_standing_created",
    "candidate_b_independent_standing_created",
    "candidate_pair_split",
    "candidate_pair_ranked",
    "candidate_a_ranked_over_candidate_b",
    "candidate_b_ranked_over_candidate_a",
    "source_family_semantics_overridden",
    "semantic_ownership_transferred",
    "global_standing_vocabulary_created",
    "cross_family_standing_allowlist_created",
    "correspondence_applicability_created",
    "selected_surface_standing_basis_admission_created",
    "downstream_authorization_created",
    "operation_created",
    "execution_permission_created",
    "runtime_created",
    "deployment_created",
    "adoption_created",
    "integration_created",
    "continuation_permission_created",
    "reuse_permission_created",
    "follow_on_permission_created",
    "automatic_successor_created",
    "custody_transferred",
    "rank_upgraded",
    "source_route_widened",
    "descendant_body_creation_authorized",
    "descendant_body_creation_executed",
    "generic_cross_family_standing_adapter_created",
    "registry_created",
    "catalogue_created",
    "ontology_created",
    "repository_presence_treated_as_applicability_basis",
    "recency_inference_used",
    "follow_on_work_authorized",
)

BOUNDARY_IDENTITY_FIELDS = (
    "descendant_body_candidate_standing_effect_applicability_boundary_id",
    "descendant_body_candidate_standing_effect_applicability_boundary_type",
    "descendant_body_candidate_standing_effect_applicability_boundary_version",
    "descendant_body_candidate_standing_effect_applicability_boundary_scope",
)
SOURCE_CONTRACT_FIELDS = (
    "source_standing_contract_identity",
    "source_standing_contract_type",
    "source_standing_contract_version",
    "source_standing_contract_reference",
    "source_standing_contract_content_identity",
    "source_family",
    "source_family_semantic_owner",
)
SOURCE_ARTIFACT_FIELDS = (
    "source_artifact_reference",
    "source_artifact_content_identity",
    "source_outcome",
    "source_result_version",
    "source_resolver_module",
    "source_failed_check_count",
    "source_passed_check_count",
)
SOURCE_OPERATION_FIELDS = (
    "candidate_standing_operation_id",
    "candidate_standing_operation_type",
    "candidate_standing_operation_version",
    "candidate_standing_operation_scope",
    "candidate_standing_result",
    "candidate_standing_supported",
    "candidate_standing_authorized",
    "candidate_standing_created",
    "candidate_a_standing_created",
    "candidate_b_standing_created",
    "basis_pair_scope",
    "admissible_future_route",
)
CANDIDATE_FIELDS = (
    "candidate_record_id",
    "candidate_role",
    "candidate_basis_id",
    "candidate_basis_label",
    "candidate_standing_created",
)
CANDIDATE_PAIR_FIELDS = (
    "candidate_a",
    "candidate_b",
    "basis_pair_scope",
)
SOURCE_CUSTODY_FIELDS = (
    "source_artifact_reference",
    "source_artifact_content_identity",
    "source_custody_preserved",
    "custody_transferred",
)
SOURCE_RANK_FIELDS = (
    "candidate_standing_result",
    "candidate_standing_operation_scope",
    "candidate_records_remain_sibling",
    "candidate_record_non_hierarchy_preserved",
    "candidate_basis_non_hierarchy_preserved",
    "standing_created",
    "descendant_body_created",
    "rank_upgraded",
)
SOURCE_SCOPE_FIELDS = (
    "source_family",
    "candidate_standing_operation_scope",
    "basis_pair_scope",
    "admissible_future_route",
)
CROSS_OBJECT_BINDING_FIELDS = (
    "source_family",
    "source_family_semantic_owner",
    "source_standing_contract_reference",
    "source_artifact_reference",
    "source_artifact_content_identity",
    "candidate_standing_operation_id",
    "candidate_record_ids",
    "candidate_basis_ids",
    "standing_pair_evaluation",
    "admissible_future_route",
    "declared_downstream_matter_use",
    "source_lineage",
    "source_custody",
    "source_rank",
    "source_scope",
    "complete_pair_preserved",
)
NO_STANDING_CHANGE_FIELDS = (
    "standing_creation_requested",
    "standing_renewal_requested",
    "standing_extension_requested",
    "candidate_pair_split_requested",
    "candidate_pair_ranking_requested",
    "standing_transfer_requested",
    "standing_generalization_requested",
    "standing_reinterpretation_requested",
    "candidate_singleton_reuse_requested",
    "downstream_authorization_requested",
    "descendant_body_creation_authorization_claimed",
    "descendant_body_creation_execution_claimed",
    "correspondence_applicability_claimed",
    "selected_surface_standing_basis_admission_claimed",
)

REQUEST_KEYS = frozenset(
    {
        "boundary_identity",
        "source_family",
        "source_family_semantic_owner",
        "source_standing_contract",
        "standing_effect_locations",
        "source_artifact",
        "source_operation",
        "candidate_pair",
        "candidate_standing_operation_material",
        "source_lineage",
        "source_custody",
        "source_rank",
        "source_scope",
        "source_family_non_claims",
        "admissible_future_route",
        "declared_downstream_matter_use",
        "declared_use_exactly_matches_source_route",
        "cross_object_binding",
        "no_standing_change_declaration",
        "declared_non_claims",
    }
)


def _candidate_a() -> dict[str, Any]:
    return {
        "candidate_record_id": CANDIDATE_A_RECORD_ID,
        "candidate_role": CANDIDATE_A_ROLE,
        "candidate_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_standing_created": True,
    }


def _candidate_b() -> dict[str, Any]:
    return {
        "candidate_record_id": CANDIDATE_B_RECORD_ID,
        "candidate_role": CANDIDATE_B_ROLE,
        "candidate_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_basis_label": CANDIDATE_B_BASIS_LABEL,
        "candidate_standing_created": True,
    }


def _candidate_a_evaluation() -> dict[str, Any]:
    return {
        "candidate_basis_id": CANDIDATE_A_BASIS_ID,
        "candidate_basis_label": CANDIDATE_A_BASIS_LABEL,
        "candidate_basis_non_standing_at_emission": True,
        "candidate_basis_scope": "Motion-side admissible variation",
        "candidate_basis_separate": True,
        "candidate_record_distinct": True,
        "candidate_record_id": CANDIDATE_A_RECORD_ID,
        "candidate_role": CANDIDATE_A_ROLE,
        "candidate_standing_authorized": True,
        "candidate_standing_created": True,
        "candidate_standing_supported": True,
        "descendant_body_created": False,
        "identity_created": False,
        "presence_established": False,
        "relation_created": False,
    }


def _candidate_b_evaluation() -> dict[str, Any]:
    return {
        "candidate_basis_id": CANDIDATE_B_BASIS_ID,
        "candidate_basis_label": CANDIDATE_B_BASIS_LABEL,
        "candidate_basis_non_standing_at_emission": True,
        "candidate_basis_scope": "Regulation-side admissibility bounds",
        "candidate_basis_separate": True,
        "candidate_record_distinct": True,
        "candidate_record_id": CANDIDATE_B_RECORD_ID,
        "candidate_role": CANDIDATE_B_ROLE,
        "candidate_standing_authorized": True,
        "candidate_standing_created": True,
        "candidate_standing_supported": True,
        "descendant_body_created": False,
        "identity_created": False,
        "presence_established": False,
        "relation_created": False,
    }


def _standing_pair_evaluation() -> dict[str, Any]:
    return {
        "both_candidate_standings_authorized": True,
        "both_candidate_standings_created": True,
        "both_candidate_standings_supported": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "candidate_record_non_hierarchy_preserved": True,
        "candidate_records_remain_sibling": True,
        "candidate_standing_evaluated": True,
        "coupling_assigned": False,
        "coupling_created": False,
        "descendant_body_created": False,
        "follow_on_authorized": False,
        "identity_created": False,
        "motion_does_not_erase_regulation": True,
        "presence_established": False,
        "regulation_not_sovereign_over_motion": True,
        "relation_created": False,
        "third_candidate_created": False,
        "third_model_admitted": False,
    }


def _source_material() -> dict[str, Any]:
    return {
        "candidate_a_standing_evaluation": _candidate_a_evaluation(),
        "candidate_b_standing_evaluation": _candidate_b_evaluation(),
        "standing_pair_evaluation": _standing_pair_evaluation(),
    }


def _source_operation() -> dict[str, Any]:
    return {
        "candidate_standing_operation_id": SOURCE_OPERATION_ID,
        "candidate_standing_operation_type": SOURCE_OPERATION_TYPE,
        "candidate_standing_operation_version": SOURCE_OPERATION_VERSION,
        "candidate_standing_operation_scope": SOURCE_OPERATION_SCOPE,
        "candidate_standing_result": SOURCE_CANDIDATE_STANDING_RESULT,
        "candidate_standing_supported": True,
        "candidate_standing_authorized": True,
        "candidate_standing_created": True,
        "candidate_a_standing_created": True,
        "candidate_b_standing_created": True,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _source_custody() -> dict[str, Any]:
    return {
        "source_artifact_reference": SOURCE_ARTIFACT_REFERENCE,
        "source_artifact_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
        "source_custody_preserved": True,
        "custody_transferred": False,
    }


def _source_rank() -> dict[str, Any]:
    return {
        "candidate_standing_result": SOURCE_CANDIDATE_STANDING_RESULT,
        "candidate_standing_operation_scope": SOURCE_OPERATION_SCOPE,
        "candidate_records_remain_sibling": True,
        "candidate_record_non_hierarchy_preserved": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "standing_created": False,
        "descendant_body_created": False,
        "rank_upgraded": False,
    }


def _source_scope() -> dict[str, Any]:
    return {
        "source_family": SOURCE_FAMILY,
        "candidate_standing_operation_scope": SOURCE_OPERATION_SCOPE,
        "basis_pair_scope": BASIS_PAIR_SCOPE,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
    }


def _canonical_source_non_claims() -> dict[str, bool]:
    return {key: False for key in SOURCE_REQUIRED_FALSE_NON_CLAIMS}


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _cross_object_binding(declared_use: str) -> dict[str, Any]:
    return {
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        "source_standing_contract_reference": SOURCE_CONTRACT_REFERENCE,
        "source_artifact_reference": SOURCE_ARTIFACT_REFERENCE,
        "source_artifact_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
        "candidate_standing_operation_id": SOURCE_OPERATION_ID,
        "candidate_record_ids": [CANDIDATE_A_RECORD_ID, CANDIDATE_B_RECORD_ID],
        "candidate_basis_ids": [CANDIDATE_A_BASIS_ID, CANDIDATE_B_BASIS_ID],
        "standing_pair_evaluation": _standing_pair_evaluation(),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "declared_downstream_matter_use": declared_use,
        "source_lineage": list(SOURCE_LINEAGE_REFERENCES),
        "source_custody": _source_custody(),
        "source_rank": _source_rank(),
        "source_scope": _source_scope(),
        "complete_pair_preserved": True,
    }


def build_declared_descendant_body_candidate_standing_effect_applicability_boundary_v0_min_request(
    declared_downstream_matter_use: str = ADMISSIBLE_FUTURE_ROUTE,
    **overrides: Any,
) -> dict[str, Any]:
    """Build one explicit canonical in-memory applicability envelope."""

    request: dict[str, Any] = {
        "boundary_identity": {
            "descendant_body_candidate_standing_effect_applicability_boundary_id": BOUNDARY_ID,
            "descendant_body_candidate_standing_effect_applicability_boundary_type": BOUNDARY_TYPE,
            "descendant_body_candidate_standing_effect_applicability_boundary_version": BOUNDARY_VERSION,
            "descendant_body_candidate_standing_effect_applicability_boundary_scope": BOUNDARY_SCOPE,
        },
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        "source_standing_contract": {
            "source_standing_contract_identity": SOURCE_CONTRACT_IDENTITY,
            "source_standing_contract_type": SOURCE_CONTRACT_TYPE,
            "source_standing_contract_version": SOURCE_CONTRACT_VERSION,
            "source_standing_contract_reference": SOURCE_CONTRACT_REFERENCE,
            "source_standing_contract_content_identity": SOURCE_CONTRACT_CONTENT_IDENTITY,
            "source_family": SOURCE_FAMILY,
            "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
        },
        "standing_effect_locations": list(STANDING_EFFECT_LOCATIONS),
        "source_artifact": {
            "source_artifact_reference": SOURCE_ARTIFACT_REFERENCE,
            "source_artifact_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
            "source_outcome": SOURCE_OUTCOME,
            "source_result_version": SOURCE_RESULT_VERSION,
            "source_resolver_module": SOURCE_RESOLVER_MODULE,
            "source_failed_check_count": SOURCE_FAILED_CHECK_COUNT,
            "source_passed_check_count": SOURCE_PASSED_CHECK_COUNT,
        },
        "source_operation": _source_operation(),
        "candidate_pair": {
            "candidate_a": _candidate_a(),
            "candidate_b": _candidate_b(),
            "basis_pair_scope": BASIS_PAIR_SCOPE,
        },
        "candidate_standing_operation_material": _source_material(),
        "source_lineage": list(SOURCE_LINEAGE_REFERENCES),
        "source_custody": _source_custody(),
        "source_rank": _source_rank(),
        "source_scope": _source_scope(),
        "source_family_non_claims": _canonical_source_non_claims(),
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "declared_downstream_matter_use": declared_downstream_matter_use,
        "declared_use_exactly_matches_source_route": (
            declared_downstream_matter_use == ADMISSIBLE_FUTURE_ROUTE
        ),
        "cross_object_binding": _cross_object_binding(
            declared_downstream_matter_use
        ),
        "no_standing_change_declaration": {
            key: False for key in NO_STANDING_CHANGE_FIELDS
        },
        "declared_non_claims": _canonical_non_claims(),
    }
    request.update(_copy_value(overrides))
    return request


STOP_REASONS = {
    "REQUEST_NOT_MAPPING": "The request must be one closed in-memory mapping.",
    "REQUEST_KEYS_INVALID": "The request contains unknown top-level fields.",
    "REQUEST_FIELDS_INCOMPLETE": "The closed envelope lacks a required field.",
    "BOUNDARY_IDENTITY_ADDITIONAL_BASIS_REQUIRED": "Exact boundary identity is required.",
    "BOUNDARY_IDENTITY_MISMATCH": "Boundary identity does not match this boundary.",
    "SOURCE_FAMILY_ADDITIONAL_BASIS_REQUIRED": "Exact source family is required.",
    "SOURCE_FAMILY_MISMATCH": "Source family is falsely attributed.",
    "SEMANTIC_OWNER_ADDITIONAL_BASIS_REQUIRED": "Exact source semantic owner is required.",
    "SEMANTIC_OWNER_MISMATCH": "Semantic ownership is falsely attributed.",
    "SOURCE_CONTRACT_ADDITIONAL_BASIS_REQUIRED": "Exact source contract basis is required.",
    "SOURCE_CONTRACT_MALFORMED": "Source contract shape is malformed.",
    "SOURCE_CONTRACT_MISMATCH": "Source contract binding is contradictory.",
    "EFFECT_LOCATIONS_ADDITIONAL_BASIS_REQUIRED": "The complete effect-location set is required.",
    "EFFECT_LOCATIONS_MALFORMED": "Effect locations are malformed.",
    "EFFECT_LOCATIONS_MISMATCH": "Effect locations differ from the source contract.",
    "SOURCE_ARTIFACT_ADDITIONAL_BASIS_REQUIRED": "Exact source artifact basis is required.",
    "SOURCE_ARTIFACT_MALFORMED": "Source artifact shape is malformed.",
    "SOURCE_ARTIFACT_MISMATCH": "Source artifact identity or result posture is contradictory.",
    "SOURCE_OPERATION_ADDITIONAL_BASIS_REQUIRED": "Exact source operation basis is required.",
    "SOURCE_OPERATION_MALFORMED": "Source operation shape is malformed.",
    "SOURCE_OPERATION_MISMATCH": "Source operation posture is contradictory.",
    "CANDIDATE_PAIR_SPLIT_OR_MALFORMED": "The complete exact sibling candidate pair is required.",
    "SOURCE_MATERIAL_SPLIT_OR_MALFORMED": "The complete exact pair material is required.",
    "SOURCE_LINEAGE_ADDITIONAL_BASIS_REQUIRED": "Complete exact source lineage is required.",
    "SOURCE_LINEAGE_MISMATCH": "Source lineage is substituted or contradictory.",
    "SOURCE_CUSTODY_ADDITIONAL_BASIS_REQUIRED": "Exact source custody is required.",
    "SOURCE_CUSTODY_MALFORMED": "Source custody shape is malformed.",
    "SOURCE_CUSTODY_MISMATCH": "Source custody is transferred or contradictory.",
    "SOURCE_RANK_ADDITIONAL_BASIS_REQUIRED": "Exact structural source rank is required.",
    "SOURCE_RANK_MALFORMED": "Source rank shape is malformed.",
    "SOURCE_RANK_MISMATCH": "Source rank is upgraded or contradictory.",
    "SOURCE_SCOPE_ADDITIONAL_BASIS_REQUIRED": "Exact source scope is required.",
    "SOURCE_SCOPE_MALFORMED": "Source scope shape is malformed.",
    "SOURCE_SCOPE_MISMATCH": "Source scope is widened or contradictory.",
    "SOURCE_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED": "The complete 68-field source non-claim set is required.",
    "SOURCE_NON_CLAIMS_MALFORMED": "Source non-claims contain unknown, non-boolean, or true posture.",
    "SOURCE_ROUTE_ADDITIONAL_BASIS_REQUIRED": "The exact source route is required.",
    "SOURCE_ROUTE_MISMATCH": "The source route is altered or widened.",
    "DECLARED_USE_ADDITIONAL_BASIS_REQUIRED": "One exact declared downstream use is required.",
    "DECLARED_USE_MALFORMED": "The declared use is multiple, ambiguous, or malformed.",
    "ROUTE_RELATION_ADDITIONAL_BASIS_REQUIRED": "Exact route equality posture is required.",
    "ROUTE_RELATION_MISMATCH": "Caller route-equality posture contradicts literal equality.",
    "CROSS_OBJECT_BINDING_ADDITIONAL_BASIS_REQUIRED": "The complete cross-object binding is required.",
    "CROSS_OBJECT_BINDING_MALFORMED": "Cross-object binding shape is malformed.",
    "CROSS_OBJECT_BINDING_MISMATCH": "Cross-object binding is contradictory.",
    "CROSS_OBJECT_PAIR_APPROPRIATION": "Cross-object binding splits, selects, or ranks the candidate pair.",
    "NO_STANDING_CHANGE_ADDITIONAL_BASIS_REQUIRED": "The complete no-standing-change declaration is required.",
    "NO_STANDING_CHANGE_OVERREACH": "The request creates, changes, reuses, or authorizes standing or downstream work.",
    "NON_CLAIM_ADDITIONAL_BASIS_REQUIRED": "The complete boundary non-claim set is required.",
    "NON_CLAIM_MISSING_OR_FLIPPED": "Boundary non-claims contain unknown, non-boolean, or true posture.",
    "DECLARED_USE_NOT_APPLICABLE": "The exact declared use differs from the exact source route.",
}
STOP_CODES = frozenset(STOP_REASONS)
BLOCK_CODES = frozenset(
    code
    for code in STOP_CODES
    if code.endswith("MALFORMED")
    or code.endswith("MISMATCH")
    or code
    in {
        "REQUEST_NOT_MAPPING",
        "REQUEST_KEYS_INVALID",
        "SOURCE_FAMILY_MISMATCH",
        "SEMANTIC_OWNER_MISMATCH",
        "CANDIDATE_PAIR_SPLIT_OR_MALFORMED",
        "SOURCE_MATERIAL_SPLIT_OR_MALFORMED",
        "CROSS_OBJECT_PAIR_APPROPRIATION",
        "NO_STANDING_CHANGE_OVERREACH",
        "SOURCE_NON_CLAIMS_MALFORMED",
        "NON_CLAIM_MISSING_OR_FLIPPED",
    }
)

OPEN_ITEMS = (
    "live_applicability_artifact",
    "terminal_summary",
    "receipt",
    "generic_selected_surface_standing_basis_admission_resolver",
    "correspondence_applicability",
    "other_source_owned_routes",
    "downstream_authorization_or_execution",
    "other_standing_producing_families",
)


def resolve_descendant_body_candidate_standing_effect_applicability_boundary_v0_min(
    request: Mapping[str, Any] | None,
) -> dict[str, Any]:
    """Resolve one exact source-family applicability envelope."""

    checks: list[dict[str, Any]] = []
    normalized: dict[str, Any] = {}
    state = {"source_validated": False, "pair_validated": False}

    def passed(check_id: str) -> None:
        checks.append(
            {
                "check_id": check_id,
                "passed": True,
                "failure_code": None,
                "outcome_if_failed": None,
                "block_code": None,
            }
        )

    def stopped(check_id: str, outcome: str, code: str) -> dict[str, Any]:
        checks.append(
            {
                "check_id": check_id,
                "passed": False,
                "failure_code": code,
                "outcome_if_failed": outcome,
                "block_code": code if outcome == OUTCOME_REVIEW_BLOCKED else None,
            }
        )
        return _build_result(outcome, normalized, checks, code, state)

    if not isinstance(request, Mapping):
        return stopped(
            "request_is_one_mapping", OUTCOME_REVIEW_BLOCKED, "REQUEST_NOT_MAPPING"
        )

    request_keys = frozenset(request)
    if request_keys - REQUEST_KEYS:
        return stopped(
            "request_has_no_unknown_fields",
            OUTCOME_REVIEW_BLOCKED,
            "REQUEST_KEYS_INVALID",
        )
    missing_top = REQUEST_KEYS - request_keys
    if missing_top:
        pair_fields = {"candidate_pair", "candidate_standing_operation_material"}
        if missing_top & pair_fields:
            return stopped(
                "complete_pair_is_supplied",
                OUTCOME_REVIEW_BLOCKED,
                "CANDIDATE_PAIR_SPLIT_OR_MALFORMED",
            )
        return stopped(
            "request_has_complete_closed_envelope",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "REQUEST_FIELDS_INCOMPLETE",
        )
    passed("request_has_complete_closed_envelope")

    identity, status = _fixed_mapping(
        request.get("boundary_identity"), BOUNDARY_IDENTITY_FIELDS
    )
    if status == "missing":
        return stopped(
            "boundary_identity_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "BOUNDARY_IDENTITY_ADDITIONAL_BASIS_REQUIRED",
        )
    if status == "invalid":
        return stopped(
            "boundary_identity_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "BOUNDARY_IDENTITY_MISMATCH",
        )
    expected_identity = {
        BOUNDARY_IDENTITY_FIELDS[0]: BOUNDARY_ID,
        BOUNDARY_IDENTITY_FIELDS[1]: BOUNDARY_TYPE,
        BOUNDARY_IDENTITY_FIELDS[2]: BOUNDARY_VERSION,
        BOUNDARY_IDENTITY_FIELDS[3]: BOUNDARY_SCOPE,
    }
    if not _exact_value(identity, expected_identity):
        return stopped(
            "boundary_identity_matches",
            OUTCOME_REVIEW_BLOCKED,
            "BOUNDARY_IDENTITY_MISMATCH",
        )
    normalized["boundary_identity"] = identity
    passed("boundary_identity_matches")

    for field, expected, missing_code, mismatch_code in (
        (
            "source_family",
            SOURCE_FAMILY,
            "SOURCE_FAMILY_ADDITIONAL_BASIS_REQUIRED",
            "SOURCE_FAMILY_MISMATCH",
        ),
        (
            "source_family_semantic_owner",
            SOURCE_SEMANTIC_OWNER,
            "SEMANTIC_OWNER_ADDITIONAL_BASIS_REQUIRED",
            "SEMANTIC_OWNER_MISMATCH",
        ),
    ):
        value = request.get(field)
        if not _has_text(value):
            return stopped(
                f"{field}_is_present",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                missing_code,
            )
        if value != expected:
            return stopped(
                f"{field}_matches_source",
                OUTCOME_REVIEW_BLOCKED,
                mismatch_code,
            )
        normalized[field] = value
        passed(f"{field}_matches_source")

    contract, status = _fixed_mapping(
        request.get("source_standing_contract"), SOURCE_CONTRACT_FIELDS
    )
    if status == "missing":
        return stopped(
            "source_contract_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_CONTRACT_ADDITIONAL_BASIS_REQUIRED",
        )
    if status == "invalid":
        return stopped(
            "source_contract_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_CONTRACT_MALFORMED",
        )
    expected_contract = {
        "source_standing_contract_identity": SOURCE_CONTRACT_IDENTITY,
        "source_standing_contract_type": SOURCE_CONTRACT_TYPE,
        "source_standing_contract_version": SOURCE_CONTRACT_VERSION,
        "source_standing_contract_reference": SOURCE_CONTRACT_REFERENCE,
        "source_standing_contract_content_identity": SOURCE_CONTRACT_CONTENT_IDENTITY,
        "source_family": SOURCE_FAMILY,
        "source_family_semantic_owner": SOURCE_SEMANTIC_OWNER,
    }
    if not _exact_value(contract, expected_contract):
        return stopped(
            "source_contract_matches",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_CONTRACT_MISMATCH",
        )
    normalized["source_standing_contract"] = contract
    passed("source_contract_matches")

    locations = request.get("standing_effect_locations")
    if locations is None or locations == []:
        return stopped(
            "effect_locations_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "EFFECT_LOCATIONS_ADDITIONAL_BASIS_REQUIRED",
        )
    if not isinstance(locations, list) or not all(_has_text(v) for v in locations):
        return stopped(
            "effect_locations_are_exact",
            OUTCOME_REVIEW_BLOCKED,
            "EFFECT_LOCATIONS_MALFORMED",
        )
    expected_locations = list(STANDING_EFFECT_LOCATIONS)
    if locations != expected_locations and _ordered_subsequence(
        locations, expected_locations
    ):
        return stopped(
            "effect_locations_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "EFFECT_LOCATIONS_ADDITIONAL_BASIS_REQUIRED",
        )
    if not _exact_value(locations, expected_locations):
        return stopped(
            "effect_locations_match_source",
            OUTCOME_REVIEW_BLOCKED,
            "EFFECT_LOCATIONS_MISMATCH",
        )
    normalized["standing_effect_locations"] = list(locations)
    passed("effect_locations_match_source")

    artifact, status = _fixed_mapping(
        request.get("source_artifact"), SOURCE_ARTIFACT_FIELDS
    )
    if status == "missing":
        return stopped(
            "source_artifact_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_ARTIFACT_ADDITIONAL_BASIS_REQUIRED",
        )
    if status == "invalid":
        return stopped(
            "source_artifact_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_ARTIFACT_MALFORMED",
        )
    expected_artifact = {
        "source_artifact_reference": SOURCE_ARTIFACT_REFERENCE,
        "source_artifact_content_identity": SOURCE_ARTIFACT_CONTENT_IDENTITY,
        "source_outcome": SOURCE_OUTCOME,
        "source_result_version": SOURCE_RESULT_VERSION,
        "source_resolver_module": SOURCE_RESOLVER_MODULE,
        "source_failed_check_count": SOURCE_FAILED_CHECK_COUNT,
        "source_passed_check_count": SOURCE_PASSED_CHECK_COUNT,
    }
    if not _exact_value(artifact, expected_artifact):
        return stopped(
            "source_artifact_matches",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_ARTIFACT_MISMATCH",
        )
    normalized["source_artifact"] = artifact
    passed("source_artifact_matches")

    operation, status = _fixed_mapping(
        request.get("source_operation"), SOURCE_OPERATION_FIELDS
    )
    if status == "missing":
        return stopped(
            "source_operation_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_OPERATION_ADDITIONAL_BASIS_REQUIRED",
        )
    if status == "invalid":
        return stopped(
            "source_operation_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_OPERATION_MALFORMED",
        )
    if not _exact_value(operation, _source_operation()):
        return stopped(
            "source_operation_matches",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_OPERATION_MISMATCH",
        )
    normalized["source_operation"] = operation
    passed("source_operation_matches")

    pair = request.get("candidate_pair")
    if not isinstance(pair, Mapping) or frozenset(pair) != frozenset(
        CANDIDATE_PAIR_FIELDS
    ):
        return stopped(
            "candidate_pair_is_complete",
            OUTCOME_REVIEW_BLOCKED,
            "CANDIDATE_PAIR_SPLIT_OR_MALFORMED",
        )
    candidate_a, a_status = _fixed_mapping(pair.get("candidate_a"), CANDIDATE_FIELDS)
    candidate_b, b_status = _fixed_mapping(pair.get("candidate_b"), CANDIDATE_FIELDS)
    if (
        a_status is not None
        or b_status is not None
        or not _exact_value(candidate_a, _candidate_a())
        or not _exact_value(candidate_b, _candidate_b())
        or pair.get("basis_pair_scope") != BASIS_PAIR_SCOPE
    ):
        return stopped(
            "candidate_pair_matches_complete_sibling_pair",
            OUTCOME_REVIEW_BLOCKED,
            "CANDIDATE_PAIR_SPLIT_OR_MALFORMED",
        )
    normalized["candidate_pair"] = _copy_value(pair)
    passed("candidate_pair_matches_complete_sibling_pair")

    material = request.get("candidate_standing_operation_material")
    if not isinstance(material, Mapping) or not _exact_value(
        material, _source_material()
    ):
        return stopped(
            "source_material_preserves_complete_pair",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_MATERIAL_SPLIT_OR_MALFORMED",
        )
    normalized["candidate_standing_operation_material"] = _copy_value(material)
    state["pair_validated"] = True
    passed("source_material_preserves_complete_pair")

    lineage = request.get("source_lineage")
    if lineage is None or lineage == []:
        return stopped(
            "source_lineage_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_LINEAGE_ADDITIONAL_BASIS_REQUIRED",
        )
    if not isinstance(lineage, list) or not all(_has_text(v) for v in lineage):
        return stopped(
            "source_lineage_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_LINEAGE_MISMATCH",
        )
    expected_lineage = list(SOURCE_LINEAGE_REFERENCES)
    if lineage != expected_lineage:
        if _ordered_subsequence(lineage, expected_lineage):
            return stopped(
                "source_lineage_is_complete",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                "SOURCE_LINEAGE_ADDITIONAL_BASIS_REQUIRED",
            )
        return stopped(
            "source_lineage_matches",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_LINEAGE_MISMATCH",
        )
    normalized["source_lineage"] = list(lineage)
    passed("source_lineage_matches")

    for section_name, fields, expected, additional_code, malformed_code, mismatch_code in (
        (
            "source_custody",
            SOURCE_CUSTODY_FIELDS,
            _source_custody(),
            "SOURCE_CUSTODY_ADDITIONAL_BASIS_REQUIRED",
            "SOURCE_CUSTODY_MALFORMED",
            "SOURCE_CUSTODY_MISMATCH",
        ),
        (
            "source_rank",
            SOURCE_RANK_FIELDS,
            _source_rank(),
            "SOURCE_RANK_ADDITIONAL_BASIS_REQUIRED",
            "SOURCE_RANK_MALFORMED",
            "SOURCE_RANK_MISMATCH",
        ),
        (
            "source_scope",
            SOURCE_SCOPE_FIELDS,
            _source_scope(),
            "SOURCE_SCOPE_ADDITIONAL_BASIS_REQUIRED",
            "SOURCE_SCOPE_MALFORMED",
            "SOURCE_SCOPE_MISMATCH",
        ),
    ):
        value, status = _fixed_mapping(request.get(section_name), fields)
        if status == "missing":
            return stopped(
                f"{section_name}_is_complete",
                OUTCOME_REQUIRES_ADDITIONAL_BASIS,
                additional_code,
            )
        if status == "invalid":
            return stopped(
                f"{section_name}_is_exact",
                OUTCOME_REVIEW_BLOCKED,
                malformed_code,
            )
        if not _exact_value(value, expected):
            return stopped(
                f"{section_name}_matches",
                OUTCOME_REVIEW_BLOCKED,
                mismatch_code,
            )
        normalized[section_name] = value
        passed(f"{section_name}_matches")

    source_non_claims_status = _non_claim_status(
        request.get("source_family_non_claims"), SOURCE_REQUIRED_FALSE_NON_CLAIMS
    )
    if source_non_claims_status == "missing":
        return stopped(
            "source_non_claims_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_NON_CLAIMS_ADDITIONAL_BASIS_REQUIRED",
        )
    if source_non_claims_status == "invalid":
        return stopped(
            "source_non_claims_are_canonical_false",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_NON_CLAIMS_MALFORMED",
        )
    normalized["source_family_non_claims"] = _canonical_source_non_claims()
    passed("source_non_claims_are_canonical_false")

    source_route = request.get("admissible_future_route")
    if not _has_text(source_route):
        return stopped(
            "source_route_is_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "SOURCE_ROUTE_ADDITIONAL_BASIS_REQUIRED",
        )
    if source_route != ADMISSIBLE_FUTURE_ROUTE:
        return stopped(
            "source_route_matches",
            OUTCOME_REVIEW_BLOCKED,
            "SOURCE_ROUTE_MISMATCH",
        )
    normalized["admissible_future_route"] = source_route
    state["source_validated"] = True
    passed("source_route_matches")

    declared_use = request.get("declared_downstream_matter_use")
    if declared_use is None or declared_use == "":
        return stopped(
            "declared_use_is_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "DECLARED_USE_ADDITIONAL_BASIS_REQUIRED",
        )
    if not _has_text(declared_use):
        return stopped(
            "declared_use_is_one_exact_value",
            OUTCOME_REVIEW_BLOCKED,
            "DECLARED_USE_MALFORMED",
        )
    normalized["declared_downstream_matter_use"] = declared_use
    passed("declared_use_is_one_exact_value")

    declared_relation = request.get("declared_use_exactly_matches_source_route")
    if declared_relation is None:
        return stopped(
            "route_relation_is_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "ROUTE_RELATION_ADDITIONAL_BASIS_REQUIRED",
        )
    if type(declared_relation) is not bool:
        return stopped(
            "route_relation_is_boolean",
            OUTCOME_REVIEW_BLOCKED,
            "ROUTE_RELATION_MISMATCH",
        )
    route_matches = declared_use == source_route
    if declared_relation is not route_matches:
        return stopped(
            "route_relation_matches_literal_equality",
            OUTCOME_REVIEW_BLOCKED,
            "ROUTE_RELATION_MISMATCH",
        )
    normalized["declared_use_exactly_matches_source_route"] = declared_relation
    passed("route_relation_matches_literal_equality")

    binding = request.get("cross_object_binding")
    if binding is None:
        return stopped(
            "cross_object_binding_is_present",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "CROSS_OBJECT_BINDING_ADDITIONAL_BASIS_REQUIRED",
        )
    if not isinstance(binding, Mapping):
        return stopped(
            "cross_object_binding_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "CROSS_OBJECT_BINDING_MALFORMED",
        )
    binding_keys = frozenset(binding)
    expected_binding_keys = frozenset(CROSS_OBJECT_BINDING_FIELDS)
    if binding_keys - expected_binding_keys:
        return stopped(
            "cross_object_binding_has_no_unknown_fields",
            OUTCOME_REVIEW_BLOCKED,
            "CROSS_OBJECT_BINDING_MALFORMED",
        )
    if expected_binding_keys - binding_keys:
        return stopped(
            "cross_object_binding_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "CROSS_OBJECT_BINDING_ADDITIONAL_BASIS_REQUIRED",
        )
    candidate_ids = binding.get("candidate_record_ids")
    basis_ids = binding.get("candidate_basis_ids")
    if candidate_ids != [CANDIDATE_A_RECORD_ID, CANDIDATE_B_RECORD_ID] or basis_ids != [
        CANDIDATE_A_BASIS_ID,
        CANDIDATE_B_BASIS_ID,
    ]:
        return stopped(
            "cross_object_binding_preserves_complete_ordered_pair",
            OUTCOME_REVIEW_BLOCKED,
            "CROSS_OBJECT_PAIR_APPROPRIATION",
        )
    expected_binding = _cross_object_binding(declared_use)
    if not _exact_value(binding, expected_binding):
        return stopped(
            "cross_object_binding_matches",
            OUTCOME_REVIEW_BLOCKED,
            "CROSS_OBJECT_BINDING_MISMATCH",
        )
    normalized["cross_object_binding"] = _copy_value(binding)
    passed("cross_object_binding_matches")

    no_change, status = _fixed_mapping(
        request.get("no_standing_change_declaration"), NO_STANDING_CHANGE_FIELDS
    )
    if status == "missing":
        return stopped(
            "no_standing_change_declaration_is_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "NO_STANDING_CHANGE_ADDITIONAL_BASIS_REQUIRED",
        )
    if status == "invalid" or any(type(value) is not bool for value in no_change.values()):
        return stopped(
            "no_standing_change_declaration_is_exact",
            OUTCOME_REVIEW_BLOCKED,
            "NO_STANDING_CHANGE_OVERREACH",
        )
    if any(no_change.values()):
        return stopped(
            "no_standing_change_declaration_remains_false",
            OUTCOME_REVIEW_BLOCKED,
            "NO_STANDING_CHANGE_OVERREACH",
        )
    normalized["no_standing_change_declaration"] = no_change
    passed("no_standing_change_declaration_remains_false")

    non_claim_status = _non_claim_status(
        request.get("declared_non_claims"), REQUIRED_FALSE_NON_CLAIMS
    )
    if non_claim_status == "missing":
        return stopped(
            "boundary_non_claims_are_complete",
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            "NON_CLAIM_ADDITIONAL_BASIS_REQUIRED",
        )
    if non_claim_status == "invalid":
        return stopped(
            "boundary_non_claims_are_canonical_false",
            OUTCOME_REVIEW_BLOCKED,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    normalized["declared_non_claims"] = _canonical_non_claims()
    passed("boundary_non_claims_are_canonical_false")

    if not route_matches:
        return stopped(
            "declared_use_matches_exact_source_route",
            OUTCOME_NOT_APPLICABLE,
            "DECLARED_USE_NOT_APPLICABLE",
        )
    passed("declared_use_matches_exact_source_route")
    return _build_result(OUTCOME_RECORDED, normalized, checks, None, state)


def _fixed_mapping(
    value: Any, fields: tuple[str, ...]
) -> tuple[dict[str, Any] | None, str | None]:
    if value is None:
        return None, "missing"
    if not isinstance(value, Mapping):
        return None, "invalid"
    actual = frozenset(value)
    expected = frozenset(fields)
    if actual - expected:
        return None, "invalid"
    if expected - actual or any(value.get(field) is None for field in fields):
        return None, "missing"
    return {field: _copy_value(value[field]) for field in fields}, None


def _non_claim_status(value: Any, required: tuple[str, ...]) -> str | None:
    if value is None:
        return "missing"
    if not isinstance(value, Mapping):
        return "invalid"
    actual = frozenset(value)
    expected = frozenset(required)
    if expected - actual:
        return "missing"
    if actual - expected:
        return "invalid"
    if any(type(value[key]) is not bool or value[key] is not False for key in required):
        return "invalid"
    return None


def _ordered_subsequence(actual: list[str], expected: list[str]) -> bool:
    if len(actual) >= len(expected):
        return False
    iterator = iter(expected)
    return all(any(item == candidate for candidate in iterator) for item in actual)


def _exact_value(actual: Any, expected: Any) -> bool:
    if isinstance(expected, Mapping):
        if not isinstance(actual, Mapping) or frozenset(actual) != frozenset(expected):
            return False
        return all(_exact_value(actual[key], expected[key]) for key in expected)
    if isinstance(expected, list):
        return isinstance(actual, list) and len(actual) == len(expected) and all(
            _exact_value(left, right) for left, right in zip(actual, expected)
        )
    if type(expected) is bool:
        return type(actual) is bool and actual is expected
    if type(expected) is int:
        return type(actual) is int and actual == expected
    return type(actual) is type(expected) and actual == expected


def _copy_value(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _copy_value(item) for key, item in value.items()}
    if isinstance(value, list):
        return [_copy_value(item) for item in value]
    if isinstance(value, tuple):
        return [_copy_value(item) for item in value]
    return value


def _has_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _build_result(
    outcome: str,
    normalized: Mapping[str, Any],
    checks: list[dict[str, Any]],
    stopping_code: str | None,
    state: Mapping[str, bool],
) -> dict[str, Any]:
    source_validated = state.get("source_validated") is True
    pair_validated = state.get("pair_validated") is True
    recorded = outcome == OUTCOME_RECORDED
    complete_review = outcome in {OUTCOME_RECORDED, OUTCOME_NOT_APPLICABLE}
    declared_use = normalized.get("declared_downstream_matter_use")
    route_matches = (
        source_validated
        and isinstance(declared_use, str)
        and declared_use == ADMISSIBLE_FUTURE_ROUTE
    )
    return {
        "boundary": {
            "descendant_body_candidate_standing_effect_applicability_boundary_id": BOUNDARY_ID,
            "descendant_body_candidate_standing_effect_applicability_boundary_type": BOUNDARY_TYPE,
            "descendant_body_candidate_standing_effect_applicability_boundary_version": BOUNDARY_VERSION,
            "descendant_body_candidate_standing_effect_applicability_boundary_scope": BOUNDARY_SCOPE,
            "review_exhausted": True,
        },
        "source_binding": {
            "source_family": SOURCE_FAMILY if source_validated else None,
            "source_family_semantic_owner": (
                SOURCE_SEMANTIC_OWNER if source_validated else None
            ),
            "source_standing_contract_reference": (
                SOURCE_CONTRACT_REFERENCE if source_validated else None
            ),
            "source_artifact_reference": (
                SOURCE_ARTIFACT_REFERENCE if source_validated else None
            ),
            "source_artifact_content_identity": (
                SOURCE_ARTIFACT_CONTENT_IDENTITY if source_validated else None
            ),
            "candidate_standing_operation_id": (
                SOURCE_OPERATION_ID if source_validated else None
            ),
            "candidate_standing_result": (
                SOURCE_CANDIDATE_STANDING_RESULT if source_validated else None
            ),
            "source_standing_created": source_validated,
            "candidate_a_record_id": CANDIDATE_A_RECORD_ID if pair_validated else None,
            "candidate_b_record_id": CANDIDATE_B_RECORD_ID if pair_validated else None,
            "candidate_a_basis_id": CANDIDATE_A_BASIS_ID if pair_validated else None,
            "candidate_b_basis_id": CANDIDATE_B_BASIS_ID if pair_validated else None,
            "complete_pair_preserved": pair_validated,
            "source_custody_preserved": source_validated,
            "source_rank_preserved": source_validated,
            "source_lineage_preserved": source_validated,
        },
        "applicability": {
            "candidate_standing_effect_applicability_recorded": recorded,
            "candidate_standing_effect_applicable_to_declared_use": recorded,
            "declared_use_exactly_matches_source_route": route_matches,
            "declared_downstream_matter_use": declared_use,
            "admissible_future_route": (
                ADMISSIBLE_FUTURE_ROUTE if source_validated else None
            ),
            "source_family_semantic_ownership_preserved": source_validated,
            "source_standing_revoked": False,
            "source_result_invalidated": False,
            "candidate_a_altered": False,
            "candidate_b_altered": False,
            "standing_created": False,
            "descendant_body_creation_authorized": False,
            "descendant_body_creation_executed": False,
            "correspondence_applicability_created": False,
            "selected_surface_standing_basis_admission_created": False,
            "downstream_authorization_created": False,
            "lawful_terminal_outcome_recorded": True,
            "complete_review_reached": complete_review,
        },
        "checks": _copy_value(checks),
        "source_family_non_claims": _canonical_source_non_claims(),
        "non_claims": _canonical_non_claims(),
        "what_remains_open": list(OPEN_ITEMS),
        "outcome": outcome,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "stopping_code": stopping_code,
        "stopping_reason": STOP_REASONS.get(stopping_code),
        "block": {
            "blocked": outcome == OUTCOME_REVIEW_BLOCKED,
            "code": stopping_code if outcome == OUTCOME_REVIEW_BLOCKED else None,
        },
    }
