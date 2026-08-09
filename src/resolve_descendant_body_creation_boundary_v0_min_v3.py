"""Pure V3 resolver for the descendant-body-creation consideration boundary.

The module embodies the closed executable manifest from the governing V3
specification.  It performs structural comparison only: no repository read,
hashing, discovery, persistence, upstream resolution, invocation, execution,
or descendant-body creation occurs here.
"""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_descendant_body_creation_boundary_v0_min_v3"
RESULT_VERSION = "0.3.0"

BOUNDARY_ID = "descendant_body_creation_boundary_001"
BOUNDARY_TYPE = "DESCENDANT_BODY_CREATION_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_DESCENDANT_BODY_CREATION_AFTER_CANDIDATE_STANDING_ONLY"
TARGET_BOUNDARY_CONTRACT_REFERENCE = (
    "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_SPEC.md"
)
TARGET_BOUNDARY_CONTRACT_SHA256 = (
    "0b66c2419a1fe4e480192755858268aab0d7f8d109822a99fcf83e3d785be273"
)
NEXT_ROUTE = "DESCENDANT_BODY_CREATION_BOUNDARY_THEN_DESCENDANT_BODY_CREATION_OPERATION_ONLY"
DECLARED_MATTER_USE = (
    "CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY"
)

INTENT = "RECORD_DESCENDANT_BODY_CREATION_BOUNDARY"
DECLARED_CURRENT_QUESTION = (
    "May exact DESCENDANT_BODY_CREATION_BOUNDARY target "
    "descendant_body_creation_boundary_001, under fresh admitted request "
    "descendant_body_creation_boundary_request_001 and canonical positive "
    "actual-consumption event "
    "descendant_body_creation_boundary_request_admitted_standing_basis_"
    "consumption_request_001, record "
    "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED while preserving "
    "the complete Candidate A/B pair, source semantic ownership, declared use, "
    "target contract, consumed/exhausted closure, freshness/historical "
    "non-replay, and every downstream non-claim?"
)

OUTCOME_BLOCKED = "DESCENDANT_BODY_CREATION_BOUNDARY_BLOCKED"
OUTCOME_REQUIRES_CANDIDATE_STANDING = (
    "DESCENDANT_BODY_CREATION_BOUNDARY_REQUIRES_CANDIDATE_STANDING"
)
OUTCOME_ALLOWED = "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED"
OUTCOMES = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_CANDIDATE_STANDING,
    OUTCOME_ALLOWED,
)
BOUNDARY_RESULT_ALLOWED = "DESCENDANT_BODY_CREATION_OPERATION_CONSIDERATION_ALLOWED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
    }
)
REQUIREMENT_CODES = frozenset({"CANDIDATE_STANDING_BASIS_ABSENT"})

POSITIVE_BOUNDARY_FIELDS = (
    "descendant_body_creation_boundary_recorded",
    "descendant_body_creation_boundary_result_recorded",
    "descendant_body_creation_operation_consideration_allowed",
    "candidate_standing_referenced",
    "candidate_a_standing_referenced",
    "candidate_b_standing_referenced",
    "candidate_standing_created_referenced",
)


EXPECTED_CONSTITUTIONAL_EVENT_KEY = {
    "request": {
        "request_id": "descendant_body_creation_boundary_request_001",
        "request_type": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST",
        "request_version": "0.1.0",
        "request_scope": (
            "ONE_FRESH_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_"
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONLY"
        ),
        "request_outcome": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_RECORDED",
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_v0_min/"
            "descendant_body_creation_boundary_request_001__"
            "descendant_body_creation_boundary_request_v0_min_result.json"
        ),
        "result_sha256": (
            "00ae4d23b703ac57f6eecf684e8c64d8bb7ca7fb0ff418b4d6a453813ffc5ef8"
        ),
        "declared_matter_use": DECLARED_MATTER_USE,
        "requested_target_boundary_id": BOUNDARY_ID,
    },
    "request_admission": {
        "request_admission_id": "descendant_body_creation_boundary_request_admission_001",
        "request_admission_type": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION",
        "request_admission_version": "0.1.0",
        "request_admission_scope": (
            "ONE_EXACT_RECORDED_DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION_ONLY"
        ),
        "request_admission_outcome": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED"
        ),
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_admission_v0_min_v2/"
            "descendant_body_creation_boundary_request_admission_001__"
            "descendant_body_creation_boundary_request_admission_v0_min_v2_result.json"
        ),
        "result_sha256": (
            "57c3272f7a0f3f36678397162573bae0836cf77f1db11ac2bb874efa66ff778d"
        ),
        "request_admitted": True,
        "eligible_for_later_separate_one_shot_basis_consumption_review": True,
        "bound_request_id": "descendant_body_creation_boundary_request_001",
        "bound_standing_basis_admission_id": (
            "matter_bound_selected_surface_standing_basis_admission_001"
        ),
    },
    "actual_consumption": {
        "request_consumption_request_id": (
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_request_001"
        ),
        "request_consumption_type": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMPTION"
        ),
        "request_consumption_version": "0.1.0",
        "request_consumption_scope": (
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_BODY_"
            "CREATION_BOUNDARY_REQUEST_ONE_SHOT_CONSUMPTION_AND_EXHAUSTION_ONLY"
        ),
        "outcome": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_CONSUMED"
        ),
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_admitted_standing_"
            "basis_consumption_v0_min_v2/descendant_body_creation_boundary_request_"
            "admitted_standing_basis_consumption_request_001__descendant_body_creation_"
            "boundary_request_admitted_standing_basis_consumption_v0_min_v2_result.json"
        ),
        "result_sha256": (
            "b50484a89aeb06e4e903b66e1a48d00f77cd12575a99af55c33ebcbe01f1abd5"
        ),
        "basis_consumed": True,
        "basis_exhausted": True,
        "basis_consumption_performed": True,
        "basis_exhaustion_performed": True,
        "one_shot_consumption_preserved": True,
        "one_shot_availability_closed": True,
        "consumed_request_basis_recorded": True,
        "consumption_token_closed": True,
        "exact_consumption_identity_preserved": True,
        "exact_request_preserved": True,
        "exact_request_admission_preserved": True,
        "exact_pre_consumption_boundary_preserved": True,
        "exact_standing_basis_admission_preserved": True,
        "selected_surface_complete_pair_preserved": True,
        "source_family_semantic_ownership_preserved": True,
        "declared_matter_use_preserved": True,
        "freshness_and_non_replay_preserved": True,
        "target_boundary_consideration_requires_separate_review": True,
        "invocation_and_execution_require_separate_review": True,
        "result_level_non_claims_canonical_false": True,
    },
    "pre_consumption": {
        "consumption_boundary_request_id": (
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_boundary_request_001"
        ),
        "consumption_boundary_type": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
            "CONSUMPTION_BOUNDARY"
        ),
        "consumption_boundary_version": "0.1.0",
        "consumption_boundary_scope": (
            "ONE_EXACT_ADMITTED_STANDING_BASIS_ONE_EXACT_ADMITTED_DESCENDANT_BODY_"
            "CREATION_BOUNDARY_REQUEST_ONE_FUTURE_CONSUMPTION_REVIEW_ONLY"
        ),
        "consumption_boundary_outcome": (
            "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
            "CONSUMPTION_BOUNDARY_RECORDED"
        ),
        "result_reference": (
            "artifacts/descendant_body_creation_boundary_request_admitted_standing_"
            "basis_consumption_boundary_v0_min_v2/descendant_body_creation_boundary_"
            "request_admitted_standing_basis_consumption_boundary_request_001__"
            "descendant_body_creation_boundary_request_admitted_standing_basis_"
            "consumption_boundary_v0_min_v2_result.json"
        ),
        "review_exhausted": True,
        "one_future_consumption_review_only": True,
        "actual_consumption_requires_separate_review": True,
        "target_boundary_consideration_requires_separate_review": True,
    },
    "standing_basis_admission": {
        "standing_basis_admission_id": (
            "matter_bound_selected_surface_standing_basis_admission_001"
        ),
        "standing_basis_admission_type": (
            "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
        ),
        "standing_basis_admission_version": "0.1.0",
        "standing_basis_admission_scope": (
            "ONE_SELECTED_SURFACE_ONE_EXPLICIT_DOWNSTREAM_MATTER_USE_"
            "ONE_EXACT_FAMILY_OWNED_STANDING_BASIS_ONLY"
        ),
        "standing_basis_admission_outcome": "SELECTED_SURFACE_STANDING_BASIS_ADMITTED",
        "result_reference": (
            "artifacts/matter_bound_selected_surface_standing_basis_admission_v0_min/"
            "matter_bound_selected_surface_standing_basis_admission_001__"
            "matter_bound_selected_surface_standing_basis_admission_v0_min_result.json"
        ),
        "result_sha256": (
            "e53cb86c1b76eec212bbd90c1247da7adc0cd4c4cc26da82b4a3edd2c4aa639f"
        ),
        "declared_matter_use": DECLARED_MATTER_USE,
        "review_exhausted": True,
    },
    "selected_surface": {
        "selected_surface_identity": "descendant_body_candidate_standing_operation_001",
        "selected_surface_type": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_version": "0.1.0",
        "selected_surface_scope": "EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY",
        "selected_surface_result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_"
            "standing_operation_v0_min/descendant_body_candidate_standing_operation_"
            "001__candidate_standing_operation_v0_min_result.json"
        ),
        "selected_surface_result_sha256": (
            "ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961"
        ),
        "selected_surface_family": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "selected_surface_semantic_owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION",
        "source_standing_contract_reference": (
            "spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md"
        ),
        "source_standing_contract_sha256": (
            "b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3"
        ),
        "source_standing_contract_version": "0.1.0",
        "candidate_a_record_id": "descendant_body_basis_candidate_a_001",
        "candidate_a_role": "CANDIDATE_A",
        "candidate_a_basis_id": (
            "descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis"
        ),
        "candidate_a_basis_label": "CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS",
        "candidate_b_record_id": "descendant_body_basis_candidate_b_001",
        "candidate_b_role": "CANDIDATE_B",
        "candidate_b_basis_id": (
            "descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis"
        ),
        "candidate_b_basis_label": (
            "CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS"
        ),
        "basis_pair_scope": "SEPARATE_CANDIDATE_SPECIFIC_BASIS_MATERIAL_ONLY",
        "complete_pair_preserved": True,
        "candidate_records_remain_sibling": True,
        "candidate_record_non_hierarchy_preserved": True,
        "candidate_basis_non_hierarchy_preserved": True,
        "source_custody_preserved": True,
        "source_lineage_preserved": True,
        "source_rank_preserved": True,
        "source_scope_preserved": True,
    },
    "source_applicability": {
        "source_applicability_boundary_id": (
            "descendant_body_candidate_standing_effect_applicability_boundary_001"
        ),
        "source_applicability_type": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY"
        ),
        "source_applicability_version": "0.1.0",
        "source_applicability_scope": (
            "ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_ONE_EXACT_DECLARED_"
            "DOWNSTREAM_USE_ONLY"
        ),
        "source_applicability_outcome": (
            "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED"
        ),
        "source_applicability_result_reference": (
            "artifacts/descendant_body_candidate_standing_effect_applicability_"
            "boundary_v0_min_v2/descendant_body_candidate_standing_effect_"
            "applicability_boundary_001__descendant_body_candidate_standing_effect_"
            "applicability_boundary_v0_min_v2_result.json"
        ),
        "admissible_future_route": DECLARED_MATTER_USE,
        "declared_matter_use": DECLARED_MATTER_USE,
        "complete_review_reached": True,
    },
    "target": {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "descendant_body_creation_boundary_id": BOUNDARY_ID,
        "descendant_body_creation_boundary_type": BOUNDARY_TYPE,
        "descendant_body_creation_boundary_version": BOUNDARY_VERSION,
        "descendant_body_creation_boundary_scope": BOUNDARY_SCOPE,
        "target_boundary_contract_reference": TARGET_BOUNDARY_CONTRACT_REFERENCE,
        "target_boundary_contract_sha256": TARGET_BOUNDARY_CONTRACT_SHA256,
        "next_route": NEXT_ROUTE,
        "admissible_future_route": NEXT_ROUTE,
        "declared_matter_use": DECLARED_MATTER_USE,
    },
    "freshness": {
        "fresh_request_identity_declared": True,
        "request_identity_distinct_from_target_boundary": True,
        "request_identity_distinct_from_historical_completed_lineage": True,
        "historical_request_identity_reused": False,
        "historical_request_material_reused": False,
        "historical_request_mutated": False,
        "historical_request_reopened": False,
        "historical_request_replayed": False,
        "historical_standing_basis_substituted": False,
        "historical_success_treated_as_fresh_permission": False,
    },
    "historical_target": {
        "result_reference": (
            "artifacts/integrity_host_v0_min_coexistence_descendant_body_creation_"
            "boundary_v0_min/descendant_body_creation_boundary_001__"
            "descendant_body_creation_boundary_v0_min_result.json"
        ),
        "result_sha256": (
            "9598594605e6ae20040cfea67cd6bff74263246aaa3139d0b356eef90b3752c0"
        ),
        "outcome": "DESCENDANT_BODY_CREATION_BOUNDARY_ALLOWED",
        "boundary_result": BOUNDARY_RESULT_ALLOWED,
    },
    "non_claim_attribution": {
        "request_formation_declared": {"owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"},
        "request_formation_result": {"owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST"},
        "request_admission": {"owner": "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMISSION"},
        "pre_consumption": {
            "owner": (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
                "CONSUMPTION_BOUNDARY"
            )
        },
        "standing_basis_admission": {
            "owner": "MATTER_BOUND_SELECTED_SURFACE_STANDING_BASIS_ADMISSION"
        },
        "source_applicability": {
            "owner": "DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY"
        },
        "source_family": {"owner": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"},
        "actual_consumption": {
            "owner": (
                "DESCENDANT_BODY_CREATION_BOUNDARY_REQUEST_ADMITTED_STANDING_BASIS_"
                "CONSUMPTION"
            )
        },
        "target_local": {"owner": BOUNDARY_TYPE},
    },
}


EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS = {
    "source_outcome": "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_SUPPORTED",
    "source_standing_result": "CANDIDATE_STANDING_SUPPORTED",
    "candidate_standing_supported": True,
    "candidate_standing_authorized": True,
    "candidate_standing_created": True,
    "candidate_a_standing_created": True,
    "candidate_b_standing_created": True,
    "candidate_standing_effect_applicability_recorded": True,
    "candidate_standing_effect_applicable_to_declared_use": True,
    "declared_use_exactly_matches_source_route": True,
    "source_family_semantic_ownership_preserved": True,
}


REQUEST_NON_CLAIM_KEYS = tuple(
    """
    admitted_standing_basis_consumed admitted_standing_basis_exhausted
    authority_created automatic_successor_created basis_reuse_permission_created
    boundary_consideration_allowed candidate_a_independently_selected
    candidate_b_independently_selected candidate_pair_ranked candidate_pair_split
    consumption_authorized consumption_token_closed continuation_permission_created
    correspondence_applicability_created custody_transferred descendant_body_created
    descendant_body_creation_authorized descendant_body_creation_boundary_created
    descendant_body_creation_boundary_modified descendant_body_creation_executed
    descendant_body_creation_operation_consideration_allowed
    descendant_body_creation_performed execution_permission_created
    follow_on_permission_created follow_on_work_authorized
    historical_request_identity_reused historical_request_material_reused
    historical_request_mutated historical_request_reopened historical_request_replayed
    historical_standing_basis_substituted
    historical_success_treated_as_fresh_permission invocation_authorized
    invocation_performed invocation_request_admitted invocation_token_created
    rank_upgraded repeat_permission_created request_admission_recorded request_admitted
    request_reuse_permission_created runtime_created
    selected_surface_standing_basis_admission_created semantic_ownership_transferred
    source_applicability_created standing_basis_admission_reperformed standing_created
    standing_extended standing_generalized standing_reinterpreted standing_renewed
    standing_transferred
    """.split()
)

REQUEST_ADMISSION_NON_CLAIM_KEYS = tuple(
    """
    admitted_standing_basis_consumed admitted_standing_basis_exhausted
    authority_created automatic_successor_created basis_consumption_performed
    basis_exhaustion_performed basis_reuse_permission_created
    boundary_consideration_allowed boundary_consideration_performed
    candidate_a_independently_selected candidate_b_independently_selected
    candidate_pair_ranked candidate_pair_split consumption_authorized
    consumption_token_closed consumption_token_created continuation_permission_created
    correspondence_applicability_created custody_transferred descendant_body_created
    descendant_body_creation_authorized descendant_body_creation_executed
    descendant_body_creation_operation_consideration_allowed
    descendant_body_creation_performed execution_performed execution_permission_created
    follow_on_permission_created follow_on_work_authorized
    historical_request_identity_reused historical_request_material_reused
    historical_request_mutated historical_request_reopened historical_request_replayed
    historical_standing_basis_substituted
    historical_success_treated_as_fresh_permission invocation_authorized
    invocation_performed invocation_request_admitted invocation_token_created
    later_one_shot_basis_consumption_review_authorized
    later_one_shot_basis_consumption_review_scheduled rank_upgraded
    repeat_permission_created request_reuse_permission_created runtime_created
    semantic_ownership_transferred source_applicability_created standing_created
    standing_extended standing_generalized standing_reinterpreted standing_renewed
    standing_transferred
    """.split()
)

PRE_CONSUMPTION_NON_CLAIM_KEYS = tuple(
    """
    admitted_standing_basis_consumed admitted_standing_basis_exhausted
    authority_created automatic_successor_created basis_consumption_performed
    basis_exhaustion_performed basis_reuse_permission_created
    boundary_consideration_allowed boundary_consideration_performed
    candidate_a_independently_selected candidate_b_independently_selected
    candidate_pair_ranked candidate_pair_split catalogue_created consumption_authorized
    consumption_token_closed consumption_token_created continuation_permission_created
    correspondence_applicability_created cross_family_adapter_created custody_transferred
    descendant_body_created descendant_body_creation_authorized
    descendant_body_creation_executed
    descendant_body_creation_operation_consideration_allowed
    descendant_body_creation_performed execution_performed execution_permission_created
    follow_on_permission_created follow_on_work_authorized
    generic_consumption_framework_created historical_request_identity_reused
    historical_request_material_reused historical_request_mutated
    historical_request_reopened historical_request_replayed
    historical_standing_basis_substituted
    historical_success_treated_as_fresh_permission invocation_authorized
    invocation_performed invocation_request_admitted
    later_one_shot_basis_consumption_review_authorized
    later_one_shot_basis_consumption_review_scheduled ontology_created rank_upgraded
    registry_created repeat_permission_created request_reuse_permission_created
    runtime_created semantic_ownership_transferred source_applicability_created
    standing_created standing_extended standing_generalized standing_reinterpreted
    standing_renewed standing_transferred
    """.split()
)

STANDING_BASIS_ADMISSION_NON_CLAIM_KEYS = tuple(
    """
    agency_created authority_created authority_transferred automatic_inheritance_created
    automatic_next_step_created biological_status_created canonicalization_performed
    catalogue_created centralized_standing_vocabulary_allowlist_created
    conformance_created consciousness_created continuation_authorized
    correspondence_executed coverage_authority_created currentness_created
    custody_transferred execution_authorized global_reuse_permission_created
    global_standing_ontology_created global_standing_recognized identity_created
    inventory_created mutation_performed presence_established rank_upgraded
    receiver_standing_created recency_inference_used registry_created
    repository_presence_treated_as_admission_basis self_awareness_created
    sentience_created source_family_judgment_created source_transferred
    standing_upgraded surface_standing_established surface_standing_generalized
    surface_standing_renewed threshold_met truth_created
    whole_body_coherence_established
    """.split()
)

SOURCE_APPLICABILITY_NON_CLAIM_KEYS = tuple(
    """
    adoption_created automatic_successor_created
    candidate_a_independent_standing_created candidate_a_ranked_over_candidate_b
    candidate_b_independent_standing_created candidate_b_ranked_over_candidate_a
    candidate_pair_ranked candidate_pair_split catalogue_created
    continuation_permission_created correspondence_applicability_created
    cross_family_standing_allowlist_created custody_transferred deployment_created
    descendant_body_creation_authorized descendant_body_creation_executed
    downstream_authorization_created execution_permission_created
    follow_on_permission_created follow_on_work_authorized
    generic_cross_family_standing_adapter_created global_standing_vocabulary_created
    integration_created ontology_created operation_created rank_upgraded
    recency_inference_used registry_created
    repository_presence_treated_as_applicability_basis reuse_permission_created
    runtime_created selected_surface_standing_basis_admission_created
    semantic_ownership_transferred source_family_semantics_overridden
    source_route_widened standing_created standing_extended standing_generalized
    standing_reinterpreted standing_renewed standing_transferred
    """.split()
)

SOURCE_FAMILY_NON_CLAIM_KEYS = tuple(
    """
    action_authorized affected_file_deleted affected_file_edited
    affected_file_overwritten affected_file_redeemed affected_file_repaired
    affected_file_replaced affected_file_treated_as_clean_basis api_created
    authority_created candidate_standing_boundary_bypassed
    candidate_standing_boundary_overridden contaminated_lineage_treated_as_clean_basis
    coupling_assigned_to_candidate_a coupling_assigned_to_candidate_b coupling_created
    crossing_authorized currentness_created derivative_reception_authorized
    descendant_body_a_created descendant_body_b_created descendant_body_created
    descendant_standing_check_performed
    direct_boundary_allowance_to_candidate_standing_without_operation
    direct_candidate_standing_operation_spec_to_candidate_standing_operation_completion
    direct_candidate_standing_to_authority_currentness
    direct_candidate_standing_to_coupling_creation direct_candidate_standing_to_crossing
    direct_candidate_standing_to_descendant_body_creation
    direct_candidate_standing_to_descendant_standing
    direct_candidate_standing_to_follow_on_work direct_candidate_standing_to_identity
    direct_candidate_standing_to_output_action direct_candidate_standing_to_presence
    direct_candidate_standing_to_relation direct_candidate_standing_to_runtime
    direct_candidate_standing_to_standing_descendant
    direct_candidate_standing_to_third_candidate_route
    direct_candidate_standing_to_third_model_route
    direct_supported_distinctness_to_candidate_standing_without_boundary_and_operation
    distinctness_support_recheck_operation_bypassed
    distinctness_support_recheck_operation_overridden field_machinery_created
    file_discovery_performed first_crossing_authorized follow_on_authorized
    follow_on_work_authorized hidden_repair_performed identity_created
    output_authorized presence_established prior_unsupported_candidate_a_claim_validated
    prior_unsupported_candidate_b_claim_validated
    prior_unsupported_derivation_event_claim_validated relation_created
    repair_performed repository_scan_performed runtime_created scan_performed
    silent_overwrite_performed standing_authorized standing_created
    standing_descendant_created synchronization_authorized third_candidate_created
    third_model_admitted valid_derivation_event_recorded validation_enforced
    """.split()
)

ACTUAL_CONSUMPTION_NON_CLAIM_KEYS = tuple(
    """
    artifact_existence_treated_as_consumption_law authority_created
    automatic_successor_created basis_consumed_twice basis_exhausted_twice
    basis_reuse_permission_created boundary_consideration_allowed
    boundary_consideration_performed candidate_a_independently_selected
    candidate_b_independently_selected candidate_pair_ranked candidate_pair_split
    catalogue_created consumption_identity_substituted consumption_token_created
    continuation_permission_created cross_family_adapter_created custody_transferred
    descendant_body_created descendant_body_creation_authorized
    descendant_body_creation_executed
    descendant_body_creation_operation_consideration_allowed
    descendant_body_creation_performed distinct_consumption_attempt_authorized
    execution_performed execution_permission_created file_discovery_performed
    follow_on_permission_created follow_on_work_authorized
    generic_consumption_framework_created global_uniqueness_inferred
    invocation_authorized invocation_performed invocation_request_admitted
    ontology_created pre_consumption_boundary_substituted rank_upgraded
    registry_created repeat_permission_created replay_performed
    replay_permission_created repository_scan_performed request_admission_substituted
    request_reuse_permission_created request_substituted runtime_created
    second_consumption_created selected_surface_substituted
    semantic_ownership_transferred sibling_consumption_identity_authorized
    source_applicability_created source_route_widened standing_basis_substituted
    standing_created standing_extended standing_generalized standing_reinterpreted
    standing_renewed standing_transferred
    """.split()
)

TARGET_LOCAL_NON_CLAIM_KEYS = tuple(
    """
    descendant_body_creation_performed descendant_body_a_created
    descendant_body_b_created descendant_body_created standing_descendant_created
    descendant_standing_check_performed crossing_authorized first_crossing_authorized
    relation_created field_machinery_created runtime_created api_created
    currentness_created authority_created standing_created output_authorized
    action_authorized derivative_reception_authorized synchronization_authorized
    coupling_assigned_to_candidate_a coupling_assigned_to_candidate_b coupling_created
    third_candidate_created third_model_admitted presence_established identity_created
    follow_on_authorized follow_on_work_authorized
    prior_unsupported_candidate_a_claim_validated
    prior_unsupported_candidate_b_claim_validated
    prior_unsupported_derivation_event_claim_validated valid_derivation_event_recorded
    affected_file_repaired affected_file_edited affected_file_deleted
    affected_file_overwritten affected_file_replaced affected_file_redeemed
    affected_file_treated_as_clean_basis contaminated_lineage_treated_as_clean_basis
    candidate_standing_operation_overridden candidate_standing_operation_bypassed
    scan_performed repository_scan_performed file_discovery_performed repair_performed
    validation_enforced hidden_repair_performed silent_overwrite_performed
    direct_descendant_body_creation_boundary_to_descendant_body_creation_operation_completion
    direct_candidate_standing_to_descendant_body_creation_without_boundary_and_operation
    direct_candidate_standing_to_standing_descendant
    direct_candidate_standing_to_descendant_standing
    direct_descendant_body_creation_boundary_to_descendant_body_creation
    direct_descendant_body_creation_boundary_to_crossing
    direct_descendant_body_creation_boundary_to_relation
    direct_descendant_body_creation_boundary_to_runtime
    direct_descendant_body_creation_boundary_to_authority_currentness
    direct_descendant_body_creation_boundary_to_coupling_creation
    direct_descendant_body_creation_boundary_to_third_candidate_route
    direct_descendant_body_creation_boundary_to_third_model_route
    direct_descendant_body_creation_boundary_to_presence
    direct_descendant_body_creation_boundary_to_identity
    direct_descendant_body_creation_boundary_to_output_action
    direct_descendant_body_creation_boundary_to_follow_on_work
    invocation_request_admitted invocation_authorized invocation_performed
    execution_permission_created execution_performed descendant_body_creation_authorized
    descendant_body_creation_executed source_applicability_created
    """.split()
)

EXPECTED_NON_CLAIM_KEYS = {
    "request_formation_declared": REQUEST_NON_CLAIM_KEYS,
    "request_formation_result": REQUEST_NON_CLAIM_KEYS,
    "request_admission": REQUEST_ADMISSION_NON_CLAIM_KEYS,
    "pre_consumption": PRE_CONSUMPTION_NON_CLAIM_KEYS,
    "standing_basis_admission": STANDING_BASIS_ADMISSION_NON_CLAIM_KEYS,
    "source_applicability": SOURCE_APPLICABILITY_NON_CLAIM_KEYS,
    "source_family": SOURCE_FAMILY_NON_CLAIM_KEYS,
    "actual_consumption": ACTUAL_CONSUMPTION_NON_CLAIM_KEYS,
    "target_local": TARGET_LOCAL_NON_CLAIM_KEYS,
}
EXPECTED_REQUIRED_NON_CLAIMS = {
    owner: {key: False for key in keys}
    for owner, keys in EXPECTED_NON_CLAIM_KEYS.items()
}


def _leaf_paths(value: Mapping[str, Any], prefix: str) -> tuple[str, ...]:
    paths: list[str] = []
    for key in sorted(value):
        path = f"{prefix}.{key}"
        child = value[key]
        if isinstance(child, Mapping):
            paths.extend(_leaf_paths(child, path))
        else:
            paths.append(path)
    return tuple(paths)


CONTROL_PATHS = frozenset(
    {"$::mapping_cardinality", "intent", "declared_current_question"}
)
CONSTITUTIONAL_EVENT_KEY_PATHS = frozenset(
    _leaf_paths(EXPECTED_CONSTITUTIONAL_EVENT_KEY, "constitutional_event_key")
)
ORDINARY_CANDIDATE_STANDING_BASIS_PATHS = frozenset(
    f"ordinary_candidate_standing_basis.{key}"
    for key in EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS
)
REQUIRED_NON_CLAIM_OWNER_PATHS = frozenset(
    f"required_non_claims.{owner}" for owner in EXPECTED_NON_CLAIM_KEYS
)
REQUIRED_NON_CLAIM_PATHS = REQUIRED_NON_CLAIM_OWNER_PATHS | frozenset(
    f"required_non_claims.{owner}.{key}"
    for owner, keys in EXPECTED_NON_CLAIM_KEYS.items()
    for key in keys
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_CANDIDATE_STANDING_BASIS": ORDINARY_CANDIDATE_STANDING_BASIS_PATHS,
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())
EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "declared_current_question",
        "constitutional_event_key",
        "ordinary_candidate_standing_basis",
        "required_non_claims",
    }
)


assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 139
assert len(ORDINARY_CANDIDATE_STANDING_BASIS_PATHS) == 11
assert len(REQUIRED_NON_CLAIM_OWNER_PATHS) == 9
assert len(TARGET_LOCAL_NON_CLAIM_KEYS) == 73
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & other_paths
        for other_name, other_paths in CLASS_PATHS.items()
        if other_name != _class_name
    )


def build_descendant_body_creation_boundary_v0_min_v3_envelope() -> dict[str, Any]:
    """Return the one canonical in-memory V3 executable envelope."""

    return {
        "intent": INTENT,
        "declared_current_question": DECLARED_CURRENT_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_candidate_standing_basis": deepcopy(
            EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS
        ),
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


def _same_exact_value(actual: Any, expected: Any) -> bool:
    return type(actual) is type(expected) and actual == expected


def _check(
    check_id: str,
    classification: str,
    passed: bool,
    path: str,
    failure_code: str | None = None,
    requirement_code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "classification": classification,
        "path": path,
        "passed": bool(passed),
        "failure_code": failure_code if not passed else None,
        "requirement_code": requirement_code if not passed else None,
    }


def _validate_exact_mapping(
    actual: Any,
    expected: Mapping[str, Any],
    prefix: str,
    classification: str,
    failure_code: str,
) -> tuple[bool, list[dict[str, Any]], str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(actual, Mapping):
        checks.append(
            _check(
                f"{classification.lower()}_mapping",
                classification,
                False,
                prefix,
                failure_code,
            )
        )
        return False, checks, prefix

    actual_keys = set(actual)
    expected_keys = set(expected)
    extras = sorted(actual_keys - expected_keys)
    missing = sorted(expected_keys - actual_keys)
    shape_passed = not extras and not missing
    checks.append(
        _check(
            f"{classification.lower()}_shape_{prefix.replace('.', '_')}",
            classification,
            shape_passed,
            prefix,
            failure_code,
        )
    )
    first_error = (
        f"{prefix}.{extras[0]}" if extras else f"{prefix}.{missing[0]}" if missing else None
    )

    valid = shape_passed
    for key in sorted(expected_keys & actual_keys):
        expected_value = expected[key]
        actual_value = actual[key]
        path = f"{prefix}.{key}"
        if isinstance(expected_value, Mapping):
            child_valid, child_checks, child_error = _validate_exact_mapping(
                actual_value,
                expected_value,
                path,
                classification,
                failure_code,
            )
            checks.extend(child_checks)
            valid = valid and child_valid
            if first_error is None and child_error is not None:
                first_error = child_error
        else:
            passed = _same_exact_value(actual_value, expected_value)
            checks.append(
                _check(
                    f"{classification.lower()}_{path.replace('.', '_')}",
                    classification,
                    passed,
                    path,
                    failure_code,
                )
            )
            valid = valid and passed
            if first_error is None and not passed:
                first_error = path
    return valid, checks, first_error


def _control_review(envelope: Any) -> tuple[bool, list[dict[str, Any]], str | None, str]:
    checks: list[dict[str, Any]] = []
    if not isinstance(envelope, Mapping):
        checks.append(
            _check(
                "control_single_mapping",
                "CONTROL",
                False,
                "$::mapping_cardinality",
                "REQUEST_NOT_MAPPING",
            )
        )
        return False, checks, "$::mapping_cardinality", "REQUEST_NOT_MAPPING"

    checks.append(
        _check(
            "control_single_mapping",
            "CONTROL",
            True,
            "$::mapping_cardinality",
        )
    )
    unknown = sorted(set(envelope) - EXECUTABLE_ROOT_KEYS)
    checks.append(
        _check(
            "control_root_has_no_unsupported_fields",
            "CONTROL",
            not unknown,
            "$",
            "UNSUPPORTED_INPUT",
        )
    )
    if unknown:
        return False, checks, unknown[0], "UNSUPPORTED_INPUT"

    for key, expected in (
        ("intent", INTENT),
        ("declared_current_question", DECLARED_CURRENT_QUESTION),
    ):
        passed = key in envelope and _same_exact_value(envelope[key], expected)
        checks.append(
            _check(
                f"control_{key}_is_exact",
                "CONTROL",
                passed,
                key,
                "CONTROL_INVALID",
            )
        )
        if not passed:
            return False, checks, key, "CONTROL_INVALID"
    return True, checks, None, ""


def _ordinary_review(
    envelope: Mapping[str, Any],
) -> tuple[str, list[dict[str, Any]], str | None]:
    checks: list[dict[str, Any]] = []
    if "ordinary_candidate_standing_basis" not in envelope:
        for key in EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS:
            checks.append(
                _check(
                    f"ordinary_{key}",
                    "ORDINARY_CANDIDATE_STANDING_BASIS",
                    False,
                    f"ordinary_candidate_standing_basis.{key}",
                    requirement_code="CANDIDATE_STANDING_BASIS_ABSENT",
                )
            )
        return "missing", checks, "ordinary_candidate_standing_basis"

    ordinary = envelope["ordinary_candidate_standing_basis"]
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_mapping",
                "ORDINARY_CANDIDATE_STANDING_BASIS",
                False,
                "ordinary_candidate_standing_basis",
                "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
            )
        )
        return "invalid", checks, "ordinary_candidate_standing_basis"

    extras = sorted(set(ordinary) - set(EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS))
    checks.append(
        _check(
            "ordinary_has_no_unsupported_fields",
            "ORDINARY_CANDIDATE_STANDING_BASIS",
            not extras,
            "ordinary_candidate_standing_basis",
            "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
        )
    )
    if extras:
        return "invalid", checks, f"ordinary_candidate_standing_basis.{extras[0]}"

    missing: list[str] = []
    invalid: list[str] = []
    for key, expected in EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS.items():
        path = f"ordinary_candidate_standing_basis.{key}"
        if key not in ordinary:
            missing.append(path)
            checks.append(
                _check(
                    f"ordinary_{key}",
                    "ORDINARY_CANDIDATE_STANDING_BASIS",
                    False,
                    path,
                    requirement_code="CANDIDATE_STANDING_BASIS_ABSENT",
                )
            )
            continue
        passed = _same_exact_value(ordinary[key], expected)
        if not passed:
            invalid.append(path)
        checks.append(
            _check(
                f"ordinary_{key}",
                "ORDINARY_CANDIDATE_STANDING_BASIS",
                passed,
                path,
                "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
            )
        )
    if invalid:
        return "invalid", checks, invalid[0]
    if missing:
        return "missing", checks, missing[0]
    return "exact", checks, None


def _event_projection(event_valid: bool, section: str) -> dict[str, Any] | None:
    if not event_valid:
        return None
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[section])


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    block_code: str | None,
    issue_path: str | None,
    event_valid: bool,
    non_claims_valid: bool,
    missing_ordinary_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    requires = outcome == OUTCOME_REQUIRES_CANDIDATE_STANDING
    boundary_posture = {field: allowed for field in POSITIVE_BOUNDARY_FIELDS}
    boundary_posture.update(
        {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "descendant_body_creation_boundary_result": (
                BOUNDARY_RESULT_ALLOWED if allowed else None
            ),
            "result_level_non_claims_canonical_false": True,
        }
    )

    return {
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "descendant_body_creation_boundary_result": (
            BOUNDARY_RESULT_ALLOWED if allowed else None
        ),
        "descendant_body_creation_boundary_metadata": {
            "boundary_id": BOUNDARY_ID,
            "boundary_type": BOUNDARY_TYPE,
            "boundary_version": BOUNDARY_VERSION,
            "boundary_scope": BOUNDARY_SCOPE,
            "target_boundary_contract_reference": TARGET_BOUNDARY_CONTRACT_REFERENCE,
            "target_boundary_contract_sha256": TARGET_BOUNDARY_CONTRACT_SHA256,
            "next_route": NEXT_ROUTE,
            "governing_executable_specification": (
                "spec/DESCENDANT_BODY_CREATION_BOUNDARY_V0_MIN_V3_SPEC.md"
            ),
        },
        "declared_descendant_body_creation_boundary_basis": {
            "intent": INTENT,
            "declared_current_question": DECLARED_CURRENT_QUESTION,
            "manifest": {
                "control_path_count": len(CONTROL_PATHS),
                "constitutional_event_key_path_count": len(
                    CONSTITUTIONAL_EVENT_KEY_PATHS
                ),
                "ordinary_candidate_standing_basis_path_count": len(
                    ORDINARY_CANDIDATE_STANDING_BASIS_PATHS
                ),
                "required_non_claim_owner_count": len(
                    REQUIRED_NON_CLAIM_OWNER_PATHS
                ),
                "pairwise_disjoint": True,
            },
        },
        "descendant_body_creation_boundary_statement": {
            "current_question": DECLARED_CURRENT_QUESTION,
            "consideration_only": True,
            "operation_invoked": False,
            "descendant_body_created": False,
        },
        "current_consideration_event_binding": {
            "event_key_valid": event_valid,
            "same_exact_binding_is_same_event": True,
            "resolver_call_count_is_event_count": False,
            "request_id": (
                EXPECTED_CONSTITUTIONAL_EVENT_KEY["request"]["request_id"]
                if event_valid
                else None
            ),
            "actual_consumption_identity": (
                EXPECTED_CONSTITUTIONAL_EVENT_KEY["actual_consumption"][
                    "request_consumption_request_id"
                ]
                if event_valid
                else None
            ),
        },
        "selected_request_formation_result": _event_projection(event_valid, "request"),
        "selected_request_admission_result": _event_projection(
            event_valid, "request_admission"
        ),
        "selected_actual_consumption_result": _event_projection(
            event_valid, "actual_consumption"
        ),
        "selected_pre_consumption_lineage": _event_projection(
            event_valid, "pre_consumption"
        ),
        "selected_standing_basis_admission_result": _event_projection(
            event_valid, "standing_basis_admission"
        ),
        "selected_surface_binding": _event_projection(event_valid, "selected_surface"),
        "selected_source_applicability_binding": _event_projection(
            event_valid, "source_applicability"
        ),
        "selected_target_boundary_binding": _event_projection(event_valid, "target"),
        "freshness_and_non_replay_posture": {
            "current": _event_projection(event_valid, "freshness"),
            "historical_target_evidence_only": _event_projection(
                event_valid, "historical_target"
            ),
            "historical_success_is_fresh_permission": False,
        },
        "upstream_basis": {
            "source_owned_material_reviewed": event_valid,
            "required_non_claims_reviewed": non_claims_valid,
            "ordinary_basis_complete": allowed,
            "ordinary_basis_missing": requires,
            "missing_ordinary_paths": list(missing_ordinary_paths),
        },
        "descendant_body_creation_boundary": boundary_posture,
        "descendant_body_creation_boundary_material": {
            "candidate_standing_basis_review": (
                "EXACT" if allowed else "ABSENT" if requires else "NOT_ACCEPTED"
            ),
            "ordinary_basis_expected": deepcopy(
                EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS
            ),
            "ordinary_basis_is_source_owned": True,
            "target_reinterpreted_source_semantics": False,
        },
        "descendant_body_creation_boundary_checks": checks,
        "boundary_result_detail": {
            "outcome": outcome,
            "boundary_result": BOUNDARY_RESULT_ALLOWED if allowed else None,
            "review_terminal": True,
            "review_exhausted": True,
            "operation_consideration_is_only_positive_consequence": allowed,
        },
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code,
            "issue_path": issue_path,
            "requirement_code": (
                "CANDIDATE_STANDING_BASIS_ABSENT" if requires else None
            ),
        },
        "attributed_required_non_claims": (
            deepcopy(EXPECTED_REQUIRED_NON_CLAIMS) if non_claims_valid else None
        ),
        "non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS["target_local"]),
        "descendant_body_creation_boundary_non_meaning": {
            "consideration_is_invocation": False,
            "consideration_is_execution": False,
            "consideration_is_descendant_body_creation": False,
            "historical_target_result_is_current_permission": False,
            "resolver_rerender_is_another_event": False,
        },
        "descendant_body_creation_boundary_summary": {
            "allowed": allowed,
            "requires_candidate_standing": requires,
            "blocked": outcome == OUTCOME_BLOCKED,
            "actual_consumption_recreated": False,
            "standing_created": False,
            "source_applicability_created": False,
            "invocation_authorized": False,
            "execution_performed": False,
            "descendant_body_created": False,
        },
        "permitted_future_route": NEXT_ROUTE if allowed else None,
        "blocked_routes": [
            "automatic_invocation",
            "automatic_execution",
            "automatic_descendant_body_creation",
            "historical_result_as_fresh_permission",
            "standing_or_applicability_recreation",
        ],
        "what_remains_open": {
            "open_items": ["DESCENDANT_BODY_CREATION_OPERATION"],
            "open_means_next": False,
            "open_means_authorized": False,
            "open_means_scheduled": False,
            "open_means_executed": False,
        },
    }


def resolve_descendant_body_creation_boundary_v0_min_v3(
    envelope: Any,
) -> dict[str, Any]:
    """Resolve one supplied V3 envelope without side effects or discovery."""

    checks: list[dict[str, Any]] = []
    control_valid, control_checks, issue_path, block_code = _control_review(envelope)
    checks.extend(control_checks)
    if not control_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            block_code,
            issue_path,
            event_valid=False,
            non_claims_valid=False,
        )

    event_valid, event_checks, event_issue = _validate_exact_mapping(
        envelope.get("constitutional_event_key"),
        EXPECTED_CONSTITUTIONAL_EVENT_KEY,
        "constitutional_event_key",
        "CONSTITUTIONAL_EVENT_KEY",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
    )
    checks.extend(event_checks)
    if not event_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "CONSTITUTIONAL_EVENT_KEY_INVALID",
            event_issue,
            event_valid=False,
            non_claims_valid=False,
        )

    non_claims_valid, non_claim_checks, non_claim_issue = _validate_exact_mapping(
        envelope.get("required_non_claims"),
        EXPECTED_REQUIRED_NON_CLAIMS,
        "required_non_claims",
        "REQUIRED_NON_CLAIM",
        "REQUIRED_NON_CLAIM_INVALID",
    )
    checks.extend(non_claim_checks)
    if not non_claims_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "REQUIRED_NON_CLAIM_INVALID",
            non_claim_issue,
            event_valid=True,
            non_claims_valid=False,
        )

    ordinary_status, ordinary_checks, ordinary_issue = _ordinary_review(envelope)
    checks.extend(ordinary_checks)
    if ordinary_status == "invalid":
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            "ORDINARY_CANDIDATE_STANDING_BASIS_INVALID",
            ordinary_issue,
            event_valid=True,
            non_claims_valid=True,
        )
    if ordinary_status == "missing":
        missing_paths = tuple(
            check["path"]
            for check in ordinary_checks
            if not check["passed"] and check["requirement_code"] is not None
        )
        return _build_result(
            OUTCOME_REQUIRES_CANDIDATE_STANDING,
            checks,
            None,
            ordinary_issue,
            event_valid=True,
            non_claims_valid=True,
            missing_ordinary_paths=missing_paths,
        )
    return _build_result(
        OUTCOME_ALLOWED,
        checks,
        None,
        None,
        event_valid=True,
        non_claims_valid=True,
    )


__all__ = [
    "ALL_REQUIRED_PATHS",
    "BLOCK_CODES",
    "BOUNDARY_ID",
    "BOUNDARY_SCOPE",
    "BOUNDARY_TYPE",
    "BOUNDARY_VERSION",
    "CLASS_PATHS",
    "CONSTITUTIONAL_EVENT_KEY_PATHS",
    "CONTROL_PATHS",
    "DECLARED_CURRENT_QUESTION",
    "EXPECTED_CONSTITUTIONAL_EVENT_KEY",
    "EXPECTED_NON_CLAIM_KEYS",
    "EXPECTED_ORDINARY_CANDIDATE_STANDING_BASIS",
    "EXPECTED_REQUIRED_NON_CLAIMS",
    "INTENT",
    "NEXT_ROUTE",
    "ORDINARY_CANDIDATE_STANDING_BASIS_PATHS",
    "OUTCOME_ALLOWED",
    "OUTCOME_BLOCKED",
    "OUTCOME_REQUIRES_CANDIDATE_STANDING",
    "OUTCOMES",
    "POSITIVE_BOUNDARY_FIELDS",
    "REQUIRED_NON_CLAIM_OWNER_PATHS",
    "REQUIRED_NON_CLAIM_PATHS",
    "RESOLVER_MODULE",
    "RESULT_VERSION",
    "TARGET_LOCAL_NON_CLAIM_KEYS",
    "build_descendant_body_creation_boundary_v0_min_v3_envelope",
    "resolve_descendant_body_creation_boundary_v0_min_v3",
]
