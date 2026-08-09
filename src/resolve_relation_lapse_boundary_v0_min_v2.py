"""Pure current-line resolver for one bounded RELATION_LAPSE_BOUNDARY event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_relation_lapse_boundary_v0_min_v2"
RESULT_VERSION = "0.2.0"

BOUNDARY_ID = "relation_lapse_boundary_001"
BOUNDARY_TYPE = "RELATION_LAPSE_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = (
    "CONSIDER_RELATION_LAPSE_AFTER_RELATION_REVERSIBILITY_SUPPORT_BEFORE_PRESENCE_ONLY"
)
BOUNDARY_CONTRACT_REFERENCE = "spec/RELATION_LAPSE_BOUNDARY_V0_MIN_SPEC.md"
BOUNDARY_CONTRACT_SHA256 = (
    "d60251d5e1268a6b942a6076c779630d7d2f71d714be1aeef38ad3fe4aa86e4b"
)
ADMISSIBLE_FUTURE_ROUTE = (
    "RELATION_LAPSE_BOUNDARY_THEN_RELATION_LAPSE_OPERATION_ONLY"
)

CURRENT_REVERSIBILITY_OPERATION_RESULT_REFERENCE = (
    "artifacts/relation_reversibility_operation_v0_min_v2/"
    "relation_reversibility_operation_001__relation_reversibility_operation_"
    "v0_min_v2_result.json"
)
CURRENT_REVERSIBILITY_OPERATION_RESULT_SHA256 = (
    "796dde545e55ecb1fa45761ed1744f7c1275a27fb6b3d5f14d2352afeb611e06"
)
HISTORICAL_LAPSE_BOUNDARY_RESULT_REFERENCE = (
    "artifacts/integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min/"
    "relation_lapse_boundary_001__relation_lapse_boundary_v0_min_result.json"
)
HISTORICAL_LAPSE_BOUNDARY_RESULT_SHA256 = (
    "b20f901ec80b7977388db01b7a6639b340d9a918514ff81d78ee3c69d7af003d"
)

RELATION_REVERSIBILITY_OPERATION_ID = "relation_reversibility_operation_001"
RELATION_REVERSIBILITY_ID = "relation_reversibility_001"
RELATION_ID = "relation_001"
RELATION_PAIR_SCOPE = "RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY"
RELATION_OBJECT_CARDINALITY = 1
FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
TOPOLOGY = "PAIR_SCOPED_NON_DIRECTIONAL"

INTENT_RECORD = "RECORD_RELATION_LAPSE_BOUNDARY"
BOUNDARY_QUESTION = (
    "Given the exact current RELATION_REVERSIBILITY_OPERATION occurrence in which "
    "bounded reversibility for relation_001 was supported, authorized, performed, "
    "and recorded, and given the explicit target-specific "
    "RECORD_RELATION_LAPSE_BOUNDARY operator intent, may RELATION_LAPSE_BOUNDARY "
    "allow only separately bounded RELATION_LAPSE_OPERATION consideration while "
    "preserving relation_001 and its exact lineage, without itself lapsing, "
    "dissolving, reversing, terminating, erasing, mutating, invalidating, "
    "punishing, or tearing down the relation, and without creating living relation "
    "state, historical receipt preservation, presence, coupling, standing, "
    "currentness, authority, or identity?"
)

OUTCOME_BLOCKED = "RELATION_LAPSE_BOUNDARY_BLOCKED"
OUTCOME_REQUIRES_REVERSIBILITY = "RELATION_LAPSE_BOUNDARY_REQUIRES_REVERSIBILITY"
OUTCOME_ALLOWED = "RELATION_LAPSE_BOUNDARY_ALLOWED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_REVERSIBILITY,
    OUTCOME_ALLOWED,
)

RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_REQUIRES_REVERSIBILITY = "REQUIRES_REVERSIBILITY"
RESULT_ALLOWED = "RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "UNSUPPORTED_INPUT",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_REVERSIBILITY_BASIS_INVALID",
    }
)

POSITIVE_BOUNDARY_BOOLEAN_FIELDS = tuple(
    """
    relation_lapse_boundary_recorded
    relation_lapse_boundary_result_recorded
    relation_lapse_operation_consideration_allowed
    relation_reversibility_operation_referenced
    relation_record_referenced
    relation_basis_referenced
    """.split()
)

SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS = ('relation_authorized',
 'relation_created',
 'relation_operation_performed',
 'coupling_created',
 'presence_established',
 'identity_created',
 'follow_on_authorized',
 'follow_on_work_authorized')
SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS = ('field_machinery_created',
 'runtime_created',
 'api_created',
 'currentness_created',
 'authority_created',
 'standing_created',
 'output_authorized',
 'action_authorized',
 'derivative_reception_authorized',
 'synchronization_authorized',
 'coupling_assigned_to_relation',
 'coupling_assigned_to_first_crossing_a',
 'coupling_assigned_to_first_crossing_b',
 'coupling_assigned_to_descendant_body_a',
 'coupling_assigned_to_descendant_body_b',
 'coupling_assigned_to_candidate_a',
 'coupling_assigned_to_candidate_b',
 'coupling_created',
 'third_candidate_created',
 'third_model_admitted',
 'presence_established',
 'identity_created',
 'standing_descendant_created',
 'descendant_standing_check_performed',
 'follow_on_authorized',
 'follow_on_work_authorized',
 'prior_unsupported_candidate_a_claim_validated',
 'prior_unsupported_candidate_b_claim_validated',
 'prior_unsupported_derivation_event_claim_validated',
 'valid_derivation_event_recorded',
 'affected_file_repaired',
 'affected_file_edited',
 'affected_file_deleted',
 'affected_file_overwritten',
 'affected_file_replaced',
 'affected_file_redeemed',
 'affected_file_treated_as_clean_basis',
 'contaminated_lineage_treated_as_clean_basis',
 'relation_boundary_overridden',
 'relation_boundary_bypassed',
 'first_crossing_operation_v1_repaired',
 'first_crossing_operation_v1_overwritten',
 'first_crossing_operation_v1_converted_to_standing',
 'first_crossing_operation_v2_overridden',
 'first_crossing_operation_v2_bypassed',
 'scan_performed',
 'repository_scan_performed',
 'file_discovery_performed',
 'repair_performed',
 'validation_enforced',
 'hidden_repair_performed',
 'silent_overwrite_performed',
 'direct_relation_operation_spec_to_relation_operation_completion',
 'direct_relation_boundary_allowance_to_relation_without_operation',
 'direct_first_crossing_to_relation_without_relation_boundary_and_operation',
 'direct_relation_to_field_machinery',
 'direct_relation_to_runtime',
 'direct_relation_to_authority_currentness',
 'direct_relation_to_coupling_assignment',
 'direct_relation_to_coupling_creation',
 'direct_relation_to_third_candidate_route',
 'direct_relation_to_third_model_route',
 'direct_relation_to_presence',
 'direct_relation_to_identity',
 'direct_relation_to_standing_descendant',
 'direct_relation_to_descendant_standing',
 'direct_relation_to_output_action',
 'direct_relation_to_follow_on_work')
SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_KEYS = ('relation_reversibility_authorized',
 'relation_lapse_authorized',
 'relation_dissolution_authorized',
 'relation_reversibility_performed',
 'relation_lapse_performed',
 'relation_dissolution_performed',
 'relation_erased',
 'relation_mutated',
 'relation_invalidated',
 'relation_punished',
 'relation_teardown_created',
 'relation_record_preserved_as_historical_receipt',
 'living_relation_state_created',
 'living_relation_state_lapsed',
 'living_relation_state_dissolved',
 'presence_boundary_authorized',
 'presence_established',
 'identity_created',
 'field_machinery_created',
 'runtime_created',
 'api_created',
 'currentness_created',
 'authority_created',
 'standing_created',
 'output_authorized',
 'action_authorized',
 'derivative_reception_authorized',
 'synchronization_authorized',
 'coupling_assigned_to_relation',
 'coupling_assigned_to_first_crossing_a',
 'coupling_assigned_to_first_crossing_b',
 'coupling_assigned_to_descendant_body_a',
 'coupling_assigned_to_descendant_body_b',
 'coupling_assigned_to_candidate_a',
 'coupling_assigned_to_candidate_b',
 'coupling_created',
 'third_candidate_created',
 'third_model_admitted',
 'standing_descendant_created',
 'descendant_standing_check_performed',
 'follow_on_authorized',
 'follow_on_work_authorized',
 'prior_unsupported_candidate_a_claim_validated',
 'prior_unsupported_candidate_b_claim_validated',
 'prior_unsupported_derivation_event_claim_validated',
 'valid_derivation_event_recorded',
 'affected_file_repaired',
 'affected_file_edited',
 'affected_file_deleted',
 'affected_file_overwritten',
 'affected_file_replaced',
 'affected_file_redeemed',
 'affected_file_treated_as_clean_basis',
 'contaminated_lineage_treated_as_clean_basis',
 'relation_operation_overridden',
 'relation_operation_bypassed',
 'relation_operation_invalidated',
 'relation_record_erased',
 'relation_record_mutated',
 'scan_performed',
 'repository_scan_performed',
 'file_discovery_performed',
 'repair_performed',
 'validation_enforced',
 'hidden_repair_performed',
 'silent_overwrite_performed',
 'direct_relation_reversibility_boundary_to_relation_reversibility_operation_completion',
 'direct_relation_operation_to_relation_lapse_without_reversibility_boundary_and_operation',
 'direct_relation_operation_to_relation_dissolution_without_reversibility_boundary_and_operation',
 'direct_relation_operation_to_relation_reversal_without_reversibility_boundary_and_operation',
 'direct_relation_operation_to_presence_boundary_without_reversibility_boundary_consideration',
 'direct_relation_to_presence',
 'direct_relation_to_identity',
 'direct_relation_to_coupling_assignment',
 'direct_relation_to_coupling_creation',
 'direct_relation_to_field_machinery',
 'direct_relation_to_runtime',
 'direct_relation_to_authority_currentness',
 'direct_relation_reversibility_boundary_to_relation_erasure',
 'direct_relation_reversibility_boundary_to_relation_mutation',
 'direct_relation_reversibility_boundary_to_relation_invalidation',
 'direct_relation_reversibility_boundary_to_punitive_lapse_interpretation',
 'direct_relation_reversibility_boundary_to_teardown_logic',
 'direct_relation_reversibility_boundary_to_presence_boundary_authorization',
 'direct_relation_reversibility_boundary_to_presence_establishment',
 'direct_relation_reversibility_boundary_to_follow_on_work')
SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_KEYS = ('relation_record_is_living_relation_state',
 'living_relation_state_created',
 'living_relation_state_lapsed',
 'living_relation_state_dissolved',
 'relation_lapse_authorized',
 'relation_lapse_performed',
 'relation_dissolution_authorized',
 'relation_dissolution_performed',
 'relation_reversed',
 'relation_terminated',
 'relation_erased',
 'relation_mutated',
 'relation_invalidated',
 'relation_punished',
 'relation_teardown_created',
 'historical_receipt_preservation_authorized',
 'historical_receipt_preserved',
 'presence_boundary_authorized',
 'presence_established',
 'identity_created',
 'field_machinery_created',
 'runtime_created',
 'api_created',
 'currentness_created',
 'authority_created',
 'standing_created',
 'output_authorized',
 'action_authorized',
 'derivative_reception_authorized',
 'synchronization_authorized',
 'coupling_assigned_to_relation',
 'coupling_assigned_to_first_crossing_a',
 'coupling_assigned_to_first_crossing_b',
 'coupling_assigned_to_descendant_body_a',
 'coupling_assigned_to_descendant_body_b',
 'coupling_assigned_to_candidate_a',
 'coupling_assigned_to_candidate_b',
 'coupling_created',
 'third_candidate_created',
 'third_model_admitted',
 'standing_descendant_created',
 'descendant_standing_check_performed',
 'follow_on_authorized',
 'follow_on_work_authorized',
 'prior_unsupported_candidate_a_claim_validated',
 'prior_unsupported_candidate_b_claim_validated',
 'prior_unsupported_derivation_event_claim_validated',
 'valid_derivation_event_recorded',
 'affected_file_repaired',
 'affected_file_edited',
 'affected_file_deleted',
 'affected_file_overwritten',
 'affected_file_replaced',
 'affected_file_redeemed',
 'affected_file_treated_as_clean_basis',
 'contaminated_lineage_treated_as_clean_basis',
 'relation_reversibility_boundary_overridden',
 'relation_reversibility_boundary_bypassed',
 'relation_reversibility_boundary_invalidated',
 'relation_operation_overridden',
 'relation_operation_bypassed',
 'relation_operation_invalidated',
 'relation_record_erased',
 'relation_record_mutated',
 'scan_performed',
 'repository_scan_performed',
 'file_discovery_performed',
 'repair_performed',
 'validation_enforced',
 'hidden_repair_performed',
 'silent_overwrite_performed',
 'direct_relation_reversibility_operation_spec_to_relation_reversibility_completion',
 'direct_relation_reversibility_boundary_allowance_to_relation_lapse',
 'direct_relation_reversibility_boundary_allowance_to_relation_dissolution',
 'direct_relation_reversibility_boundary_allowance_to_relation_reversal',
 'direct_relation_reversibility_boundary_allowance_to_relation_termination',
 'direct_relation_reversibility_boundary_allowance_to_relation_erasure',
 'direct_relation_reversibility_boundary_allowance_to_relation_mutation',
 'direct_relation_reversibility_boundary_allowance_to_relation_invalidation',
 'direct_relation_reversibility_boundary_allowance_to_punitive_lapse_interpretation',
 'direct_relation_reversibility_boundary_allowance_to_teardown_logic',
 'direct_relation_reversibility_boundary_allowance_to_living_relation_state',
 'direct_relation_reversibility_boundary_allowance_to_historical_receipt_preservation',
 'direct_relation_reversibility_boundary_allowance_to_presence_boundary_authorization',
 'direct_relation_reversibility_boundary_allowance_to_presence_establishment',
 'direct_relation_reversibility_operation_to_relation_lapse_without_lapse_boundary',
 'direct_relation_reversibility_operation_to_relation_dissolution_without_dissolution_boundary',
 'direct_relation_reversibility_operation_to_presence_boundary_without_separate_boundary_consideration',
 'direct_relation_to_presence',
 'direct_relation_to_identity',
 'direct_relation_to_coupling_assignment',
 'direct_relation_to_coupling_creation',
 'direct_relation_to_field_machinery',
 'direct_relation_to_runtime',
 'direct_relation_to_authority_currentness',
 'direct_relation_reversibility_operation_to_follow_on_work')
BOUNDARY_LOCAL_NON_CLAIM_KEYS = ('relation_lapse_authorized',
 'relation_lapse_performed',
 'relation_lapse_recorded',
 'relation_lapse_supported',
 'relation_dissolution_authorized',
 'relation_dissolution_performed',
 'relation_reversed',
 'relation_terminated',
 'relation_erased',
 'relation_mutated',
 'relation_invalidated',
 'relation_punished',
 'relation_teardown_created',
 'living_relation_state_created',
 'living_relation_state_lapsed',
 'living_relation_state_dissolved',
 'historical_receipt_preservation_authorized',
 'historical_receipt_preserved',
 'presence_boundary_authorized',
 'presence_established',
 'identity_created',
 'field_machinery_created',
 'runtime_created',
 'api_created',
 'currentness_created',
 'authority_created',
 'standing_created',
 'output_authorized',
 'action_authorized',
 'derivative_reception_authorized',
 'synchronization_authorized',
 'coupling_assigned_to_relation',
 'coupling_assigned_to_first_crossing_a',
 'coupling_assigned_to_first_crossing_b',
 'coupling_assigned_to_descendant_body_a',
 'coupling_assigned_to_descendant_body_b',
 'coupling_assigned_to_candidate_a',
 'coupling_assigned_to_candidate_b',
 'coupling_created',
 'third_candidate_created',
 'third_model_admitted',
 'standing_descendant_created',
 'descendant_standing_check_performed',
 'follow_on_authorized',
 'follow_on_work_authorized',
 'prior_unsupported_candidate_a_claim_validated',
 'prior_unsupported_candidate_b_claim_validated',
 'prior_unsupported_derivation_event_claim_validated',
 'valid_derivation_event_recorded',
 'affected_file_repaired',
 'affected_file_edited',
 'affected_file_deleted',
 'affected_file_overwritten',
 'affected_file_replaced',
 'affected_file_redeemed',
 'affected_file_treated_as_clean_basis',
 'contaminated_lineage_treated_as_clean_basis',
 'relation_reversibility_operation_overridden',
 'relation_reversibility_operation_bypassed',
 'relation_reversibility_operation_invalidated',
 'relation_operation_overridden',
 'relation_operation_bypassed',
 'relation_operation_invalidated',
 'relation_record_erased',
 'relation_record_mutated',
 'scan_performed',
 'repository_scan_performed',
 'file_discovery_performed',
 'repair_performed',
 'validation_enforced',
 'hidden_repair_performed',
 'silent_overwrite_performed',
 'direct_relation_lapse_boundary_to_relation_lapse_operation_completion',
 'direct_relation_reversibility_operation_to_relation_lapse_without_lapse_boundary_and_operation',
 'direct_relation_reversibility_operation_to_relation_dissolution_without_dissolution_boundary_and_operation',
 'direct_relation_reversibility_operation_to_presence_boundary_without_lapse_boundary_consideration',
 'direct_relation_lapse_boundary_to_relation_lapse',
 'direct_relation_lapse_boundary_to_relation_dissolution',
 'direct_relation_lapse_boundary_to_relation_reversal',
 'direct_relation_lapse_boundary_to_relation_termination',
 'direct_relation_lapse_boundary_to_relation_erasure',
 'direct_relation_lapse_boundary_to_relation_mutation',
 'direct_relation_lapse_boundary_to_relation_invalidation',
 'direct_relation_lapse_boundary_to_punitive_lapse_interpretation',
 'direct_relation_lapse_boundary_to_teardown_logic',
 'direct_relation_lapse_boundary_to_living_relation_state',
 'direct_relation_lapse_boundary_to_historical_receipt_preservation',
 'direct_relation_lapse_boundary_to_presence_boundary_authorization',
 'direct_relation_lapse_boundary_to_presence_establishment',
 'direct_relation_to_presence',
 'direct_relation_to_identity',
 'direct_relation_to_coupling_assignment',
 'direct_relation_to_coupling_creation',
 'direct_relation_to_field_machinery',
 'direct_relation_to_runtime',
 'direct_relation_to_authority_currentness',
 'direct_relation_lapse_boundary_to_follow_on_work')

EXPECTED_CONSTITUTIONAL_EVENT_KEY: dict[str, Any] = {'target': {'boundary_id': 'relation_lapse_boundary_001',
            'boundary_type': 'RELATION_LAPSE_BOUNDARY',
            'boundary_version': '0.1.0',
            'boundary_scope': 'CONSIDER_RELATION_LAPSE_AFTER_RELATION_REVERSIBILITY_SUPPORT_BEFORE_PRESENCE_ONLY',
            'boundary_contract_reference': 'spec/RELATION_LAPSE_BOUNDARY_V0_MIN_SPEC.md',
            'boundary_contract_sha256': 'd60251d5e1268a6b942a6076c779630d7d2f71d714be1aeef38ad3fe4aa86e4b',
            'admissible_future_route': 'RELATION_LAPSE_BOUNDARY_THEN_RELATION_LAPSE_OPERATION_ONLY'},
 'source_operation_event_key': {'target': {'boundary_id': 'relation_reversibility_boundary_001',
                                           'boundary_type': 'RELATION_REVERSIBILITY_BOUNDARY',
                                           'boundary_version': '0.1.0',
                                           'boundary_scope': 'CONSIDER_RELATION_REVERSIBILITY_AFTER_RELATION_SUPPORT_BEFORE_PRESENCE_ONLY',
                                           'boundary_contract_reference': 'spec/RELATION_REVERSIBILITY_BOUNDARY_V0_MIN_SPEC.md',
                                           'boundary_contract_sha256': '422a9ce767c9273a5c898d1d9d7da6d57a0ba7c5da4ac54ed3be9995ae2d8bd3',
                                           'admissible_future_route': 'RELATION_REVERSIBILITY_BOUNDARY_THEN_RELATION_REVERSIBILITY_OPERATION_ONLY'},
                                'current_relation_operation_result': {'result_reference': 'artifacts/relation_operation_v0_min_v3/relation_operation_001__relation_operation_v0_min_v3_result.json',
                                                                      'result_sha256': 'fac4cb9335a63d006dd5a3553b84db6a5cc36b3135586489fba22a3bea0b0eef',
                                                                      'result_version': '0.3.0',
                                                                      'resolver_module': 'resolve_relation_operation_v0_min_v3',
                                                                      'blocked': False,
                                                                      'block_code': None,
                                                                      'block_issue_path': None,
                                                                      'requires_boundary_allowance': False,
                                                                      'not_recorded': False},
                                'relation_operation': {'operation_id': 'relation_operation_001',
                                                       'operation_type': 'RELATION_OPERATION',
                                                       'operation_version': '0.1.0',
                                                       'operation_scope': 'EVALUATE_RELATION_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                                                       'operation_contract_reference': 'spec/RELATION_OPERATION_V0_MIN_SPEC.md',
                                                       'operation_contract_sha256': '75afd2d64b22654c1132c0c44901ad7375723d2a64e476feb59b8e561ea6d8f4',
                                                       'admissible_future_route': 'RELATION_OPERATION_THEN_RELATION_REVERSIBILITY_BOUNDARY_ONLY'},
                                'boundary_event': {'persistent_boundary_id': 'relation_reversibility_boundary_001',
                                                   'persistent_relation_operation_id': 'relation_operation_001',
                                                   'current_relation_operation_result_reference': 'artifacts/relation_operation_v0_min_v3/relation_operation_001__relation_operation_v0_min_v3_result.json',
                                                   'current_relation_operation_result_sha256': 'fac4cb9335a63d006dd5a3553b84db6a5cc36b3135586489fba22a3bea0b0eef',
                                                   'relation_id': 'relation_001',
                                                   'first_crossing_a_id': 'first_crossing_a_001',
                                                   'first_crossing_b_id': 'first_crossing_b_001',
                                                   'descendant_body_a_id': 'descendant_body_a_001',
                                                   'descendant_body_b_id': 'descendant_body_b_001',
                                                   'persistent_creation_operation_id': 'descendant_body_creation_operation_001',
                                                   'fresh_creation_operation_request_id': 'descendant_body_creation_operation_request_001',
                                                   'same_identity_same_binding_is_deterministic_rerender': True,
                                                   'resolver_call_count_is_event_count': False,
                                                   'sibling_event_identity_allocated': False},
                                'relation_operation_event': {'persistent_operation_id': 'relation_operation_001',
                                                             'persistent_boundary_id': 'relation_boundary_001',
                                                             'current_boundary_result_reference': 'artifacts/relation_boundary_v0_min_v2/relation_boundary_001__relation_boundary_v0_min_v2_result.json',
                                                             'current_boundary_result_sha256': '7a33a06296bcded16bec1d7d408395039072d3754fc194f87c16355b7e3df77e',
                                                             'relation_id': 'relation_001',
                                                             'first_crossing_a_id': 'first_crossing_a_001',
                                                             'first_crossing_b_id': 'first_crossing_b_001',
                                                             'descendant_body_a_id': 'descendant_body_a_001',
                                                             'descendant_body_b_id': 'descendant_body_b_001',
                                                             'persistent_creation_operation_id': 'descendant_body_creation_operation_001',
                                                             'fresh_creation_operation_request_id': 'descendant_body_creation_operation_request_001',
                                                             'same_identity_same_binding_is_deterministic_rerender': True,
                                                             'resolver_call_count_is_event_count': False,
                                                             'sibling_event_identity_allocated': False},
                                'crossing_operation': {'operation_id': 'first_crossing_operation_001',
                                                       'operation_type': 'FIRST_CROSSING_OPERATION',
                                                       'operation_version': '0.1.0',
                                                       'operation_scope': 'EVALUATE_FIRST_CROSSING_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                                                       'operation_contract_reference': 'spec/FIRST_CROSSING_OPERATION_V0_MIN_SPEC.md',
                                                       'operation_contract_sha256': '047460dc058b8d6a8655d0fef03a422e2330fd832dd4b2045b45968517896549',
                                                       'admissible_future_route': 'FIRST_CROSSING_OPERATION_THEN_RELATION_BOUNDARY_ONLY'},
                                'crossing_event': {'persistent_operation_id': 'first_crossing_operation_001',
                                                   'persistent_boundary_id': 'first_crossing_boundary_001',
                                                   'current_boundary_result_reference': 'artifacts/first_crossing_boundary_v0_min_v2/first_crossing_boundary_001__first_crossing_boundary_v0_min_v2_result.json',
                                                   'current_boundary_result_sha256': 'bdf3395d53e097f3494b930f3b95f0688149459d64e256ac41b953b4195bf1f1',
                                                   'persistent_creation_operation_id': 'descendant_body_creation_operation_001',
                                                   'fresh_creation_operation_request_id': 'descendant_body_creation_operation_request_001',
                                                   'descendant_body_a_id': 'descendant_body_a_001',
                                                   'descendant_body_b_id': 'descendant_body_b_001',
                                                   'one_shared_operation_event': True,
                                                   'separate_operation_occurrences_created': False,
                                                   'same_identity_same_binding_is_deterministic_rerender': True,
                                                   'resolver_call_count_is_event_count': False,
                                                   'sibling_event_identity_allocated': False},
                                'creation_operation': {'operation_family': 'DESCENDANT_BODY_CREATION_OPERATION',
                                                       'operation_id': 'descendant_body_creation_operation_001',
                                                       'operation_type': 'DESCENDANT_BODY_CREATION_OPERATION',
                                                       'operation_version': '0.1.0',
                                                       'operation_scope': 'EVALUATE_DESCENDANT_BODY_CREATION_AFTER_BOUNDARY_ALLOWANCE_ONLY'},
                                'creation_event': {'fresh_operation_request_id': 'descendant_body_creation_operation_request_001',
                                                   'persistent_operation_id': 'descendant_body_creation_operation_001',
                                                   'operation_request_result_reference': 'artifacts/descendant_body_creation_operation_request_v0_min/descendant_body_creation_operation_request_001__descendant_body_creation_operation_request_v0_min_result.json',
                                                   'operation_request_result_sha256': 'dd95b114773c8ff1b1f0a271530f282c2360b3aa58c07231886f111808d6e744',
                                                   'same_identity_same_binding_is_deterministic_rerender': True,
                                                   'resolver_call_count_is_event_count': False},
                                'relation': {'relation_id': 'relation_001',
                                             'relation_pair_scope': 'RELATION_BETWEEN_SEPARATE_FIRST_CROSSING_RECORDS_ONLY',
                                             'relation_object_cardinality': 1,
                                             'identity_allocation_is_relation_existence': False},
                                'first_crossing_a': {'first_crossing_id': 'first_crossing_a_001',
                                                     'descendant_body_id': 'descendant_body_a_001',
                                                     'candidate_standing_source_id': 'descendant_body_basis_candidate_a_001',
                                                     'candidate_role': 'CANDIDATE_A',
                                                     'candidate_standing_label': 'CANDIDATE_A_STANDING',
                                                     'candidate_basis_id': 'descendant_body_basis_candidate_a_001__motion_side_admissible_variation_basis',
                                                     'candidate_basis_label': 'CANDIDATE_A_MOTION_SIDE_ADMISSIBLE_VARIATION_BASIS',
                                                     'candidate_basis_scope': 'Motion-side '
                                                                              'admissible '
                                                                              'variation'},
                                'first_crossing_b': {'first_crossing_id': 'first_crossing_b_001',
                                                     'descendant_body_id': 'descendant_body_b_001',
                                                     'candidate_standing_source_id': 'descendant_body_basis_candidate_b_001',
                                                     'candidate_role': 'CANDIDATE_B',
                                                     'candidate_standing_label': 'CANDIDATE_B_STANDING',
                                                     'candidate_basis_id': 'descendant_body_basis_candidate_b_001__regulation_side_admissibility_bounds_basis',
                                                     'candidate_basis_label': 'CANDIDATE_B_REGULATION_SIDE_ADMISSIBILITY_BOUNDS_BASIS',
                                                     'candidate_basis_scope': 'Regulation-side '
                                                                              'admissibility '
                                                                              'bounds'},
                                'pair': {'first_crossing_pair_scope': 'SEPARATE_FIRST_CROSSING_RECORDS_ONLY',
                                         'descendant_body_pair_scope': 'SEPARATE_DESCENDANT_BODY_RECORDS_ONLY',
                                         'complete_pair_preserved': True,
                                         'descendant_bodies_remain_sibling': True,
                                         'descendant_body_non_hierarchy_preserved': True,
                                         'candidate_standing_non_hierarchy_preserved': True,
                                         'candidate_basis_non_hierarchy_preserved': True,
                                         'motion_does_not_erase_regulation': True,
                                         'regulation_not_sovereign_over_motion': True,
                                         'one_shared_crossing_operation_event': True,
                                         'separate_crossing_occurrences_created': False,
                                         'source_semantic_owner_transferred': False,
                                         'topology': 'PAIR_SCOPED_NON_DIRECTIONAL'},
                                'source': {'selected_surface_identity': 'descendant_body_candidate_standing_operation_001',
                                           'selected_surface_type': 'DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION',
                                           'selected_surface_version': '0.1.0',
                                           'selected_surface_scope': 'EVALUATE_CANDIDATE_STANDING_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                                           'selected_surface_family': 'DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION',
                                           'selected_surface_semantic_owner': 'DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION',
                                           'selected_surface_result_reference': 'artifacts/integrity_host_v0_min_coexistence_descendant_body_candidate_standing_operation_v0_min/descendant_body_candidate_standing_operation_001__candidate_standing_operation_v0_min_result.json',
                                           'selected_surface_result_sha256': 'ff1b5ef3559c6ca8a44d328c19dcaecc5df4c2c334680430b71a6644ea6ef961',
                                           'source_standing_contract_reference': 'spec/DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION_V0_MIN_SPEC.md',
                                           'source_standing_contract_sha256': 'b9e58008891b29d7bf28c6a9eb894f6a21c7443fbd9c436cea18d4256c9bf9f3',
                                           'source_standing_contract_version': '0.1.0',
                                           'source_custody_preserved': True,
                                           'source_lineage_preserved': True,
                                           'source_rank_preserved': True,
                                           'source_scope_preserved': True},
                                'source_applicability': {'source_applicability_id': 'descendant_body_candidate_standing_effect_applicability_boundary_001',
                                                         'source_applicability_type': 'DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_BOUNDARY',
                                                         'source_applicability_version': '0.1.0',
                                                         'source_applicability_scope': 'ONE_PAIR_PRESERVED_SOURCE_STANDING_EFFECT_ONE_EXACT_DECLARED_DOWNSTREAM_USE_ONLY',
                                                         'source_applicability_outcome': 'DESCENDANT_BODY_CANDIDATE_STANDING_EFFECT_APPLICABILITY_RECORDED',
                                                         'result_reference': 'artifacts/descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2/descendant_body_candidate_standing_effect_applicability_boundary_001__descendant_body_candidate_standing_effect_applicability_boundary_v0_min_v2_result.json',
                                                         'source_route': 'CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY',
                                                         'source_declared_matter_use': 'CANDIDATE_STANDING_OPERATION_THEN_DESCENDANT_BODY_CREATION_BOUNDARY_ONLY',
                                                         'complete_review_reached': True},
                                'source_stopping': {'automatic_successor_created': False,
                                                    'relation_operation_authorized': False,
                                                    'relation_operation_invoked': False},
                                'freshness': {'current_relation_operation_result_identity_declared': True,
                                              'current_relation_operation_result_identity_distinct_from_historical_boundary_occurrence': True,
                                              'current_boundary_event_identity_declared': True,
                                              'historical_boundary_result_is_current_permission': False,
                                              'historical_boundary_result_is_current_source': False,
                                              'historical_boundary_result_is_current_occurrence': False,
                                              'historical_boundary_occurrence_reused': False,
                                              'historical_boundary_material_reused': False,
                                              'historical_boundary_result_replayed': False,
                                              'historical_success_treated_as_fresh_permission': False},
                                'historical_boundary': {'historical_boundary_id': 'relation_reversibility_boundary_001',
                                                        'result_reference': 'artifacts/integrity_host_v0_min_coexistence_relation_reversibility_boundary_v0_min/relation_reversibility_boundary_001__relation_reversibility_boundary_v0_min_result.json',
                                                        'result_sha256': 'a6bbb707e77e86adaff158c46aa6e0655801e6f7c1f772ded9cfe15c38a5b3a0',
                                                        'outcome': 'RELATION_REVERSIBILITY_BOUNDARY_ALLOWED',
                                                        'boundary_result': 'RELATION_REVERSIBILITY_OPERATION_CONSIDERATION_ALLOWED',
                                                        'relation_id': 'relation_001',
                                                        'immediate_next_rank': 'RELATION_REVERSIBILITY_OPERATION',
                                                        'result_is_current_permission': False,
                                                        'result_is_current_source': False,
                                                        'result_is_current_occurrence': False,
                                                        'result_replayed': False},
                                'next_operation': {'operation_id': 'relation_reversibility_operation_001',
                                                   'operation_type': 'RELATION_REVERSIBILITY_OPERATION',
                                                   'operation_version': '0.1.0',
                                                   'operation_scope': 'EVALUATE_RELATION_REVERSIBILITY_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                                                   'operation_contract_reference': 'spec/RELATION_REVERSIBILITY_OPERATION_V0_MIN_SPEC.md',
                                                   'operation_contract_sha256': '388e674004d4ee0a2191fc602c3369067d1f270aae1d576d6455f548901acd2c',
                                                   'admissible_future_route': 'RELATION_REVERSIBILITY_OPERATION_THEN_RELATION_LAPSE_OR_PRESENCE_BOUNDARY_CONSIDERATION_ONLY',
                                                   'direct_boundary_to_operation_completion': False},
                                'future_identifiers': {'relation_reversibility_id': 'relation_reversibility_001',
                                                       'relation_reversibility_scope': 'RELATION_REVERSIBILITY_FOR_RELATION_RECORD_ONLY',
                                                       'relation_lapse_id': 'relation_lapse_001',
                                                       'relation_lapse_scope': 'RELATION_LAPSE_WITHOUT_PUNITIVE_CONSEQUENCE_ONLY',
                                                       'relation_dissolution_id': 'relation_dissolution_001',
                                                       'relation_dissolution_scope': 'RELATION_DISSOLUTION_WITHOUT_TEARDOWN_OR_ERASURE_ONLY'},
                                'current_boundary_result': {'result_reference': 'artifacts/relation_reversibility_boundary_v0_min_v2/relation_reversibility_boundary_001__relation_reversibility_boundary_v0_min_v2_result.json',
                                                            'result_sha256': '70407c854a16dd092cf84af2345745002cb5cb968dc3d6919d2e001b30c1e4e1',
                                                            'result_version': '0.2.0',
                                                            'resolver_module': 'resolve_relation_reversibility_boundary_v0_min_v2',
                                                            'blocked': False,
                                                            'block_code': None,
                                                            'block_issue_path': None,
                                                            'requires_relation': False},
                                'operation_event': {'persistent_operation_id': 'relation_reversibility_operation_001',
                                                    'persistent_boundary_id': 'relation_reversibility_boundary_001',
                                                    'current_boundary_result_reference': 'artifacts/relation_reversibility_boundary_v0_min_v2/relation_reversibility_boundary_001__relation_reversibility_boundary_v0_min_v2_result.json',
                                                    'current_boundary_result_sha256': '70407c854a16dd092cf84af2345745002cb5cb968dc3d6919d2e001b30c1e4e1',
                                                    'relation_reversibility_id': 'relation_reversibility_001',
                                                    'relation_id': 'relation_001',
                                                    'first_crossing_a_id': 'first_crossing_a_001',
                                                    'first_crossing_b_id': 'first_crossing_b_001',
                                                    'descendant_body_a_id': 'descendant_body_a_001',
                                                    'descendant_body_b_id': 'descendant_body_b_001',
                                                    'persistent_creation_operation_id': 'descendant_body_creation_operation_001',
                                                    'fresh_creation_operation_request_id': 'descendant_body_creation_operation_request_001',
                                                    'same_identity_same_binding_is_deterministic_rerender': True,
                                                    'resolver_call_count_is_event_count': False,
                                                    'sibling_event_identity_allocated': False},
                                'operation_freshness': {'current_boundary_result_identity_declared': True,
                                                        'current_boundary_result_identity_distinct_from_historical_operation_occurrence': True,
                                                        'current_operation_event_identity_declared': True,
                                                        'historical_operation_result_is_current_permission': False,
                                                        'historical_operation_result_is_current_source': False,
                                                        'historical_operation_result_is_current_occurrence': False,
                                                        'historical_operation_occurrence_reused': False,
                                                        'historical_operation_material_reused': False,
                                                        'historical_operation_result_replayed': False,
                                                        'historical_success_treated_as_fresh_permission': False},
                                'historical_operation': {'historical_operation_id': 'relation_reversibility_operation_001',
                                                         'result_reference': 'artifacts/integrity_host_v0_min_coexistence_relation_reversibility_operation_v0_min/relation_reversibility_operation_001__relation_reversibility_operation_v0_min_result.json',
                                                         'result_sha256': 'd59c4ce570acdf15a06199827d3e6a1432804f708949e73f6c4efab6ee278fbb',
                                                         'outcome': 'RELATION_REVERSIBILITY_OPERATION_RECORDED',
                                                         'operation_result': 'RELATION_REVERSIBILITY_SUPPORTED',
                                                         'relation_id': 'relation_001',
                                                         'relation_reversibility_id': 'relation_reversibility_001',
                                                         'immediate_next_rank': 'RELATION_LAPSE_BOUNDARY',
                                                         'result_is_current_permission': False,
                                                         'result_is_current_source': False,
                                                         'result_is_current_occurrence': False,
                                                         'result_replayed': False},
                                'non_claim_attribution': {'source_relation_boundary': {'owner': 'RELATION_BOUNDARY'},
                                                          'source_crossing_operation': {'owner': 'FIRST_CROSSING_OPERATION'},
                                                          'source_family': {'owner': 'DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION'},
                                                          'source_relation_operation': {'owner': 'RELATION_OPERATION'},
                                                          'target_local': {'owner': 'RELATION_REVERSIBILITY_BOUNDARY'},
                                                          'operation_local': {'owner': 'RELATION_REVERSIBILITY_OPERATION'}}},
 'current_operation_result': {'result_reference': 'artifacts/relation_reversibility_operation_v0_min_v2/relation_reversibility_operation_001__relation_reversibility_operation_v0_min_v2_result.json',
                              'result_sha256': '796dde545e55ecb1fa45761ed1744f7c1275a27fb6b3d5f14d2352afeb611e06',
                              'result_version': '0.2.0',
                              'resolver_module': 'resolve_relation_reversibility_operation_v0_min_v2',
                              'blocked': False,
                              'block_code': None,
                              'block_issue_path': None,
                              'requires_boundary_allowance': False},
 'source_operation': {'operation_id': 'relation_reversibility_operation_001',
                      'operation_type': 'RELATION_REVERSIBILITY_OPERATION',
                      'operation_version': '0.1.0',
                      'operation_scope': 'EVALUATE_RELATION_REVERSIBILITY_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                      'operation_contract_reference': 'spec/RELATION_REVERSIBILITY_OPERATION_V0_MIN_SPEC.md',
                      'operation_contract_sha256': '388e674004d4ee0a2191fc602c3369067d1f270aae1d576d6455f548901acd2c',
                      'admissible_future_route': 'RELATION_REVERSIBILITY_OPERATION_THEN_RELATION_LAPSE_OR_PRESENCE_BOUNDARY_CONSIDERATION_ONLY'},
 'boundary_event': {'persistent_boundary_id': 'relation_lapse_boundary_001',
                    'persistent_reversibility_operation_id': 'relation_reversibility_operation_001',
                    'current_reversibility_operation_result_reference': 'artifacts/relation_reversibility_operation_v0_min_v2/relation_reversibility_operation_001__relation_reversibility_operation_v0_min_v2_result.json',
                    'current_reversibility_operation_result_sha256': '796dde545e55ecb1fa45761ed1744f7c1275a27fb6b3d5f14d2352afeb611e06',
                    'relation_reversibility_id': 'relation_reversibility_001',
                    'relation_id': 'relation_001',
                    'first_crossing_a_id': 'first_crossing_a_001',
                    'first_crossing_b_id': 'first_crossing_b_001',
                    'descendant_body_a_id': 'descendant_body_a_001',
                    'descendant_body_b_id': 'descendant_body_b_001',
                    'persistent_creation_operation_id': 'descendant_body_creation_operation_001',
                    'fresh_creation_operation_request_id': 'descendant_body_creation_operation_request_001',
                    'same_identity_same_binding_is_deterministic_rerender': True,
                    'resolver_call_count_is_event_count': False,
                    'sibling_event_identity_allocated': False},
 'freshness': {'current_reversibility_operation_result_identity_declared': True,
               'current_reversibility_operation_result_identity_distinct_from_historical_boundary_occurrence': True,
               'current_boundary_event_identity_declared': True,
               'historical_boundary_result_is_current_permission': False,
               'historical_boundary_result_is_current_source': False,
               'historical_boundary_result_is_current_occurrence': False,
               'historical_boundary_occurrence_reused': False,
               'historical_boundary_material_reused': False,
               'historical_boundary_result_replayed': False,
               'historical_success_treated_as_fresh_permission': False},
 'historical_boundary': {'historical_boundary_id': 'relation_lapse_boundary_001',
                         'result_reference': 'artifacts/integrity_host_v0_min_coexistence_relation_lapse_boundary_v0_min/relation_lapse_boundary_001__relation_lapse_boundary_v0_min_result.json',
                         'result_sha256': 'b20f901ec80b7977388db01b7a6639b340d9a918514ff81d78ee3c69d7af003d',
                         'outcome': 'RELATION_LAPSE_BOUNDARY_ALLOWED',
                         'boundary_result': 'RELATION_LAPSE_OPERATION_CONSIDERATION_ALLOWED',
                         'relation_id': 'relation_001',
                         'immediate_next_rank': 'RELATION_LAPSE_OPERATION',
                         'result_is_current_permission': False,
                         'result_is_current_source': False,
                         'result_is_current_occurrence': False,
                         'result_replayed': False},
 'non_claim_attribution': {'boundary_local': {'owner': 'RELATION_LAPSE_BOUNDARY'}}}
EXPECTED_ORDINARY_REVERSIBILITY_BASIS = {'source_outcome': 'RELATION_REVERSIBILITY_OPERATION_RECORDED',
 'source_relation_reversibility_result': 'RELATION_REVERSIBILITY_SUPPORTED',
 'relation_reversibility_supported': True,
 'relation_reversibility_authorized': True,
 'relation_reversibility_performed': True,
 'relation_reversibility_recorded': True,
 'relation_operation_referenced': True,
 'relation_record_referenced': True,
 'relation_basis_referenced': True,
 'relation_record_confirmed_as_historical_only': True}
EXPECTED_REQUIRED_NON_CLAIMS = {
    "source_relation_boundary": {
        key: False for key in SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS
    },
    "source_relation_operation": {
        key: False for key in SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS
    },
    "source_reversibility_boundary": {
        key: False for key in SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_KEYS
    },
    "source_reversibility_operation": {
        key: False for key in SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_KEYS
    },
    "boundary_local": {key: False for key in BOUNDARY_LOCAL_NON_CLAIM_KEYS},
}

COMPLETED_PREDECESSOR_OPEN_POSTURE = {
    "relation_lapse_boundary_consideration": "OPEN_ONLY",
    "presence_boundary_consideration": "OPEN_ONLY",
    "current_branch_selected": False,
    "branch_choice_created": False,
    "next_rank_invoked": False,
    "next_rank_authorized": False,
    "automatic_successor_created": False,
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


CONTROL_PATHS = frozenset({"$::mapping_cardinality", "intent", "boundary_question"})
CONSTITUTIONAL_EVENT_KEY_PATHS = frozenset(
    _leaf_paths(EXPECTED_CONSTITUTIONAL_EVENT_KEY, "constitutional_event_key")
)
SOURCE_OPERATION_EVENT_KEY_PATHS = frozenset(
    path
    for path in CONSTITUTIONAL_EVENT_KEY_PATHS
    if path.startswith("constitutional_event_key.source_operation_event_key.")
)
ORDINARY_REVERSIBILITY_BASIS_PATHS = frozenset(
    f"ordinary_reversibility_basis.{key}"
    for key in EXPECTED_ORDINARY_REVERSIBILITY_BASIS
)
SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_relation_boundary.{key}"
    for key in SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS
)
SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_relation_operation.{key}"
    for key in SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS
)
SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_reversibility_boundary.{key}"
    for key in SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_KEYS
)
SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_reversibility_operation.{key}"
    for key in SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_KEYS
)
SOURCE_REQUIRED_NON_CLAIM_PATHS = (
    SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS
    | SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS
    | SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_PATHS
    | SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_PATHS
)
BOUNDARY_LOCAL_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.boundary_local.{key}"
    for key in BOUNDARY_LOCAL_NON_CLAIM_KEYS
)
REQUIRED_NON_CLAIM_PATHS = (
    SOURCE_REQUIRED_NON_CLAIM_PATHS | BOUNDARY_LOCAL_NON_CLAIM_PATHS
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_REVERSIBILITY_BASIS": ORDINARY_REVERSIBILITY_BASIS_PATHS,
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())
EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "boundary_question",
        "constitutional_event_key",
        "ordinary_reversibility_basis",
        "required_non_claims",
    }
)

assert len(CONTROL_PATHS) == 3
assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 287
assert len(SOURCE_OPERATION_EVENT_KEY_PATHS) == 228
assert len(ORDINARY_REVERSIBILITY_BASIS_PATHS) == 10
assert len(SOURCE_RELATION_BOUNDARY_NON_CLAIM_PATHS) == 8
assert len(SOURCE_RELATION_OPERATION_NON_CLAIM_PATHS) == 68
assert len(SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_PATHS) == 86
assert len(SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_PATHS) == 96
assert len(SOURCE_REQUIRED_NON_CLAIM_PATHS) == 258
assert len(BOUNDARY_LOCAL_NON_CLAIM_PATHS) == 97
assert len(REQUIRED_NON_CLAIM_PATHS) == 355
assert len(ALL_REQUIRED_PATHS) == 655
for _class_name, _paths in CLASS_PATHS.items():
    assert not any(
        _paths & _other_paths
        for _other_name, _other_paths in CLASS_PATHS.items()
        if _other_name != _class_name
    )
assert not set(POSITIVE_BOUNDARY_BOOLEAN_FIELDS) & set(
    BOUNDARY_LOCAL_NON_CLAIM_KEYS
)


def build_declared_relation_lapse_boundary_v0_min_v2_request() -> dict[str, Any]:
    """Return the exact candidate envelope without creating a boundary event."""

    return {
        "intent": INTENT_RECORD,
        "boundary_question": BOUNDARY_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_reversibility_basis": deepcopy(
            EXPECTED_ORDINARY_REVERSIBILITY_BASIS
        ),
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


build_relation_lapse_boundary_v0_min_v2_request = (
    build_declared_relation_lapse_boundary_v0_min_v2_request
)


def _same_exact_value(actual: Any, expected: Any) -> bool:
    return type(actual) is type(expected) and actual == expected


def _check(
    check_id: str,
    classification: str,
    path: str,
    passed: bool,
    failure_code: str | None = None,
) -> dict[str, Any]:
    return {
        "check_id": check_id,
        "classification": classification,
        "path": path,
        "passed": bool(passed),
        "failure_code": failure_code if not passed else None,
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
                f"{classification.lower()}_mapping_{prefix.replace('.', '_')}",
                classification,
                prefix,
                False,
                failure_code,
            )
        )
        return False, checks, prefix

    actual_keys = set(actual)
    expected_keys = set(expected)
    extras = sorted(actual_keys - expected_keys)
    missing = sorted(expected_keys - actual_keys)
    shape_valid = not extras and not missing
    checks.append(
        _check(
            f"{classification.lower()}_shape_{prefix.replace('.', '_')}",
            classification,
            prefix,
            shape_valid,
            failure_code,
        )
    )
    issue_path = (
        f"{prefix}.{extras[0]}"
        if extras
        else f"{prefix}.{missing[0]}"
        if missing
        else None
    )
    valid = shape_valid
    for key in sorted(actual_keys & expected_keys):
        path = f"{prefix}.{key}"
        actual_value = actual[key]
        expected_value = expected[key]
        if isinstance(expected_value, Mapping):
            child_valid, child_checks, child_issue = _validate_exact_mapping(
                actual_value,
                expected_value,
                path,
                classification,
                failure_code,
            )
            checks.extend(child_checks)
            valid = valid and child_valid
            if issue_path is None and child_issue is not None:
                issue_path = child_issue
            continue
        leaf_valid = _same_exact_value(actual_value, expected_value)
        checks.append(
            _check(
                f"{classification.lower()}_{path.replace('.', '_')}",
                classification,
                path,
                leaf_valid,
                failure_code,
            )
        )
        valid = valid and leaf_valid
        if issue_path is None and not leaf_valid:
            issue_path = path
    return valid, checks, issue_path


def _control_review(
    envelope: Any,
) -> tuple[bool, list[dict[str, Any]], str | None, str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(envelope, Mapping):
        checks.append(
            _check(
                "control_single_mapping",
                "CONTROL",
                "$::mapping_cardinality",
                False,
                "REQUEST_NOT_MAPPING",
            )
        )
        return False, checks, "$::mapping_cardinality", "REQUEST_NOT_MAPPING"

    root_keys = set(envelope)
    extras = sorted(root_keys - EXECUTABLE_ROOT_KEYS)
    missing = sorted(EXECUTABLE_ROOT_KEYS - root_keys)
    root_valid = not extras and not missing
    root_code = "UNSUPPORTED_INPUT" if extras else "CONTROL_INVALID"
    checks.append(
        _check(
            "control_root_mapping_cardinality",
            "CONTROL",
            "$::mapping_cardinality",
            root_valid,
            root_code,
        )
    )
    if not root_valid:
        return False, checks, extras[0] if extras else missing[0], root_code

    intent_valid = _same_exact_value(envelope["intent"], INTENT_RECORD)
    checks.append(
        _check(
            "control_intent_exact",
            "CONTROL",
            "intent",
            intent_valid,
            "CONTROL_INVALID",
        )
    )
    if not intent_valid:
        return False, checks, "intent", "CONTROL_INVALID"

    question_valid = _same_exact_value(envelope["boundary_question"], BOUNDARY_QUESTION)
    checks.append(
        _check(
            "control_boundary_question_exact",
            "CONTROL",
            "boundary_question",
            question_valid,
            "CONTROL_INVALID",
        )
    )
    if not question_valid:
        return False, checks, "boundary_question", "CONTROL_INVALID"
    return True, checks, None, None


def _ordinary_reversibility_review(
    ordinary: Any,
) -> tuple[str, list[dict[str, Any]], tuple[str, ...], str | None]:
    prefix = "ordinary_reversibility_basis"
    checks: list[dict[str, Any]] = []
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_reversibility_basis_mapping",
                "ORDINARY_REVERSIBILITY_BASIS",
                prefix,
                False,
                "ORDINARY_REVERSIBILITY_BASIS_INVALID",
            )
        )
        return "blocked", checks, (), prefix

    expected_keys = set(EXPECTED_ORDINARY_REVERSIBILITY_BASIS)
    extras = sorted(set(ordinary) - expected_keys)
    if extras:
        path = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                "ordinary_reversibility_basis_no_unsupported_fields",
                "ORDINARY_REVERSIBILITY_BASIS",
                path,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, (), path

    present_keys = set(ordinary) & expected_keys
    missing_paths = tuple(
        f"{prefix}.{key}" for key in sorted(expected_keys - set(ordinary))
    )
    checks.append(
        _check(
            "ordinary_reversibility_basis_complete",
            "ORDINARY_REVERSIBILITY_BASIS",
            prefix,
            not missing_paths,
        )
    )
    issue_path: str | None = None
    contradictory = False
    for key in sorted(present_keys):
        path = f"{prefix}.{key}"
        exact = _same_exact_value(
            ordinary[key], EXPECTED_ORDINARY_REVERSIBILITY_BASIS[key]
        )
        checks.append(
            _check(
                f"ordinary_reversibility_basis_{key}",
                "ORDINARY_REVERSIBILITY_BASIS",
                path,
                exact,
                "ORDINARY_REVERSIBILITY_BASIS_INVALID",
            )
        )
        contradictory = contradictory or not exact
        if issue_path is None and not exact:
            issue_path = path
    if contradictory:
        return "blocked", checks, missing_paths, issue_path
    if missing_paths:
        return "requires", checks, missing_paths, missing_paths[0]
    return "allowed", checks, (), None


def _event_projection(event_valid: bool, key: str) -> Any:
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[key]) if event_valid else None


def _source_projection(event_valid: bool, key: str) -> Any:
    if not event_valid:
        return None
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY["source_operation_event_key"][key])


def _boundary_result(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return RESULT_ALLOWED
    if outcome == OUTCOME_REQUIRES_REVERSIBILITY:
        return RESULT_REQUIRES_REVERSIBILITY
    return RESULT_NOT_EVALUATED


def _boundary_object(outcome: str) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    boundary: dict[str, Any] = {
        "boundary_id": BOUNDARY_ID,
        "boundary_type": BOUNDARY_TYPE,
        "boundary_version": BOUNDARY_VERSION,
        "boundary_scope": BOUNDARY_SCOPE,
        "boundary_contract_reference": BOUNDARY_CONTRACT_REFERENCE,
        "boundary_contract_sha256": BOUNDARY_CONTRACT_SHA256,
        "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
        "relation_reversibility_operation_id": RELATION_REVERSIBILITY_OPERATION_ID,
        "relation_reversibility_id": RELATION_REVERSIBILITY_ID,
        "relation_id": RELATION_ID,
        "relation_pair_scope": RELATION_PAIR_SCOPE,
        "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
        "topology": TOPOLOGY,
        "relation_lapse_boundary_result": _boundary_result(outcome),
        **{field: False for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS},
        **{field: False for field in BOUNDARY_LOCAL_NON_CLAIM_KEYS},
    }
    if allowed:
        boundary.update({field: True for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS})
    return boundary


def _boundary_material(outcome: str, event_valid: bool) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    source_pair = _source_projection(event_valid, "pair") or {}
    return {
        "relation_reversibility_operation_reference": {
            **deepcopy(EXPECTED_ORDINARY_REVERSIBILITY_BASIS),
            "relation_reversibility_operation_referenced": allowed,
            "relation_record_referenced": allowed,
            "relation_basis_referenced": allowed,
        },
        "relation_record_persistence": {
            "relation_id": RELATION_ID,
            "relation_pair_scope": RELATION_PAIR_SCOPE,
            "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
            "topology": TOPOLOGY,
            "relation_occurrence_remains_addressable": event_valid,
            "relation_lapsed": False,
            "relation_dissolved": False,
            "relation_reversed": False,
            "relation_terminated": False,
            "relation_erased": False,
            "relation_mutated": False,
            "relation_invalidated": False,
            "relation_punished": False,
            "relation_teardown_created": False,
        },
        "pair_and_source_preservation": {
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "descendant_body_a_id": DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": DESCENDANT_BODY_B_ID,
            "topology": TOPOLOGY,
            "complete_pair_preserved": source_pair.get("complete_pair_preserved", False),
            "descendant_bodies_remain_sibling": source_pair.get(
                "descendant_bodies_remain_sibling", False
            ),
            "descendant_body_non_hierarchy_preserved": source_pair.get(
                "descendant_body_non_hierarchy_preserved", False
            ),
            "candidate_standing_non_hierarchy_preserved": source_pair.get(
                "candidate_standing_non_hierarchy_preserved", False
            ),
            "candidate_basis_non_hierarchy_preserved": source_pair.get(
                "candidate_basis_non_hierarchy_preserved", False
            ),
            "motion_does_not_erase_regulation": source_pair.get(
                "motion_does_not_erase_regulation", False
            ),
            "regulation_not_sovereign_over_motion": source_pair.get(
                "regulation_not_sovereign_over_motion", False
            ),
            "source_semantic_owner_transferred": False,
            "coupling_created": False,
        },
        "relation_lapse_boundary_evaluation": {
            "relation_lapse_operation_consideration_allowed": allowed,
            "relation_lapse_boundary_result": _boundary_result(outcome),
            "relation_lapse_supported": False,
            "relation_lapse_authorized": False,
            "relation_lapse_performed": False,
            "relation_lapse_recorded": False,
            "relation_dissolution_authorized": False,
            "relation_dissolution_performed": False,
            "relation_reversed": False,
            "relation_terminated": False,
            "relation_erased": False,
            "relation_mutated": False,
            "relation_invalidated": False,
            "relation_punished": False,
            "relation_teardown_created": False,
            "living_relation_state_created": False,
            "living_relation_state_lapsed": False,
            "living_relation_state_dissolved": False,
            "historical_receipt_preservation_authorized": False,
            "historical_receipt_preserved": False,
            "presence_boundary_authorized": False,
            "presence_established": False,
            "identity_created": False,
            "coupling_created": False,
            "follow_on_authorized": False,
            "follow_on_work_authorized": False,
        },
    }


def _build_result(
    outcome: str,
    checks: list[dict[str, Any]],
    *,
    event_valid: bool,
    block_code: str | None = None,
    issue_path: str | None = None,
    missing_reversibility_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    boundary = _boundary_object(outcome)
    failed_check_count = sum(check["passed"] is False for check in checks)
    carried = _event_projection(event_valid, "source_operation_event_key")
    return {
        "executable_metadata": {
            "boundary_id": BOUNDARY_ID,
            "resolver_module": RESOLVER_MODULE,
            "result_version": RESULT_VERSION,
        },
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "outcome": outcome,
        "boundary_question": BOUNDARY_QUESTION,
        "operator_target_posture": {
            "intent": INTENT_RECORD,
            "operator_selection_is_boundary_result": False,
            "operator_selection_is_lapse_support": False,
            "operator_selection_is_lapse_authorization": False,
            "operator_selection_is_lapse_occurrence": False,
            "operator_selection_is_constitutional_standing": False,
        },
        "current_relation_lapse_boundary_event": _event_projection(
            event_valid, "boundary_event"
        ),
        "current_relation_reversibility_operation_result_binding": _event_projection(
            event_valid, "current_operation_result"
        ),
        "persistent_relation_lapse_boundary_contract": _event_projection(
            event_valid, "target"
        ),
        "persistent_relation_reversibility_operation_identity": _event_projection(
            event_valid, "source_operation"
        ),
        "carried_source_operation_event_key": carried,
        "current_relation_reversibility_operation_event": _source_projection(
            event_valid, "operation_event"
        ),
        "persistent_relation_identity": _source_projection(event_valid, "relation"),
        "relation_subject": (
            {
                "first_crossing_a": _source_projection(event_valid, "first_crossing_a"),
                "first_crossing_b": _source_projection(event_valid, "first_crossing_b"),
                "pair": _source_projection(event_valid, "pair"),
            }
            if event_valid
            else None
        ),
        "source_binding": _source_projection(event_valid, "source"),
        "source_applicability": _source_projection(event_valid, "source_applicability"),
        "creation_operation_identity": _source_projection(
            event_valid, "creation_operation"
        ),
        "creation_operation_event": _source_projection(event_valid, "creation_event"),
        "freshness_and_history": (
            {
                "current_boundary_freshness": _event_projection(
                    event_valid, "freshness"
                ),
                "historical_lapse_boundary": _event_projection(
                    event_valid, "historical_boundary"
                ),
                "source_operation_freshness": _source_projection(
                    event_valid, "operation_freshness"
                ),
                "source_historical_operation": _source_projection(
                    event_valid, "historical_operation"
                ),
            }
            if event_valid
            else None
        ),
        "non_claim_attribution": (
            {
                "boundary_local": _event_projection(
                    event_valid, "non_claim_attribution"
                ),
                "source_operation": _source_projection(
                    event_valid, "non_claim_attribution"
                ),
            }
            if event_valid
            else None
        ),
        "completed_predecessor_open_posture": deepcopy(
            COMPLETED_PREDECESSOR_OPEN_POSTURE
        ),
        "ordinary_reversibility_basis_review": {
            "complete": outcome == OUTCOME_ALLOWED,
            "missing_paths": list(missing_reversibility_paths),
            "requires_reversibility_creates_retry_permission": False,
            "requires_reversibility_creates_successor_permission": False,
        },
        "relation_lapse_boundary": boundary,
        "relation_lapse_boundary_material": _boundary_material(outcome, event_valid),
        "source_relation_boundary_non_claims": {
            key: False for key in SOURCE_RELATION_BOUNDARY_NON_CLAIM_KEYS
        },
        "source_relation_operation_non_claims": {
            key: False for key in SOURCE_RELATION_OPERATION_NON_CLAIM_KEYS
        },
        "source_reversibility_boundary_non_claims": {
            key: False for key in SOURCE_REVERSIBILITY_BOUNDARY_NON_CLAIM_KEYS
        },
        "source_reversibility_operation_non_claims": {
            key: False for key in SOURCE_REVERSIBILITY_OPERATION_NON_CLAIM_KEYS
        },
        "boundary_local_non_claims": {
            key: False for key in BOUNDARY_LOCAL_NON_CLAIM_KEYS
        },
        "relation_lapse_boundary_checks": checks,
        "passed_check_count": len(checks) - failed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_reversibility": outcome == OUTCOME_REQUIRES_REVERSIBILITY,
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "RELATION_LAPSE_OPERATION",
            "next_rank_invoked": False,
            "next_rank_authorized": False,
            "next_rank_scheduled": False,
            "next_rank_executed": False,
            "next_rank_completed": False,
            "automatic_successor_created": False,
        },
    }


def resolve_relation_lapse_boundary_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one exact current lapse-boundary event without I/O."""

    checks: list[dict[str, Any]] = []
    control_valid, control_checks, issue_path, block_code = _control_review(
        supplied_envelope
    )
    checks.extend(control_checks)
    if not control_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=False,
            block_code=block_code,
            issue_path=issue_path,
        )

    event_valid, event_checks, event_issue = _validate_exact_mapping(
        supplied_envelope["constitutional_event_key"],
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
            event_valid=False,
            block_code="CONSTITUTIONAL_EVENT_KEY_INVALID",
            issue_path=event_issue,
        )

    non_claims_valid, non_claim_checks, non_claim_issue = _validate_exact_mapping(
        supplied_envelope["required_non_claims"],
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
            event_valid=True,
            block_code="REQUIRED_NON_CLAIM_INVALID",
            issue_path=non_claim_issue,
        )

    basis_state, basis_checks, missing_paths, basis_issue = (
        _ordinary_reversibility_review(
            supplied_envelope["ordinary_reversibility_basis"]
        )
    )
    checks.extend(basis_checks)
    if basis_state == "blocked":
        key = basis_issue.rsplit(".", 1)[-1] if basis_issue else None
        code = (
            "UNSUPPORTED_INPUT"
            if key not in EXPECTED_ORDINARY_REVERSIBILITY_BASIS
            else "ORDINARY_REVERSIBILITY_BASIS_INVALID"
        )
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=code,
            issue_path=basis_issue,
            missing_reversibility_paths=missing_paths,
        )
    if basis_state == "requires":
        return _build_result(
            OUTCOME_REQUIRES_REVERSIBILITY,
            checks,
            event_valid=True,
            missing_reversibility_paths=missing_paths,
        )
    checks.extend(
        (
            _check(
                "boundary_result_exact",
                "BOUNDARY_RESULT",
                "relation_lapse_boundary.relation_lapse_boundary_result",
                True,
            ),
            _check(
                "downstream_stopping_point_exact",
                "STOPPING_POINT",
                "downstream_stopping_point",
                True,
            ),
        )
    )
    return _build_result(OUTCOME_ALLOWED, checks, event_valid=True)

