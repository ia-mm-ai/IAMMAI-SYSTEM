"""Pure current-line resolver for one bounded PRESENCE_BOUNDARY V2 event."""

from __future__ import annotations

from collections.abc import Mapping
from copy import deepcopy
from typing import Any


RESOLVER_MODULE = "resolve_presence_boundary_v0_min_v2"
RESULT_VERSION = "0.2.0"

BOUNDARY_ID = "presence_boundary_001"
BOUNDARY_TYPE = "PRESENCE_BOUNDARY"
BOUNDARY_VERSION = "0.1.0"
BOUNDARY_SCOPE = "CONSIDER_PRESENCE_AFTER_RELATION_LAPSE_OPERATION_ONLY"
BOUNDARY_CONTRACT_REFERENCE = "spec/PRESENCE_BOUNDARY_V0_MIN_SPEC.md"
BOUNDARY_CONTRACT_SHA256 = (
    "900eeb0d104bf728208c80c2d5e487a93f408eb44c151e3c9e035ec629c6beda"
)
ADMISSIBLE_FUTURE_ROUTE = "PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY"

CURRENT_LAPSE_RESULT_REFERENCE = (
    "artifacts/relation_lapse_operation_v0_min_v2/"
    "relation_lapse_operation_001__relation_lapse_operation_v0_min_v2_result.json"
)
CURRENT_LAPSE_RESULT_SHA256 = (
    "40f41db3498b7287fb40a96863ddbee3871231ddc1269a970fbfe7f9ae59d347"
)
CURRENT_LAPSE_RESULT_VERSION = "0.2.0"
CURRENT_LAPSE_RESOLVER_MODULE = "resolve_relation_lapse_operation_v0_min_v2"
SOURCE_OUTCOME = "RELATION_LAPSE_OPERATION_RECORDED"
SOURCE_RELATION_LAPSE_RESULT = "RELATION_LAPSE_SUPPORTED"
SOURCE_OPERATION_ID = "relation_lapse_operation_001"
SOURCE_BOUNDARY_ID = "relation_lapse_boundary_001"
RELATION_LAPSE_ID = "relation_lapse_001"
RELATION_ID = "relation_001"
RELATION_OBJECT_CARDINALITY = 1
TOPOLOGY = "PAIR_SCOPED_NON_DIRECTIONAL"

FIRST_CROSSING_A_ID = "first_crossing_a_001"
FIRST_CROSSING_B_ID = "first_crossing_b_001"
DESCENDANT_BODY_A_ID = "descendant_body_a_001"
DESCENDANT_BODY_B_ID = "descendant_body_b_001"
CREATION_OPERATION_ID = "descendant_body_creation_operation_001"
CREATION_OPERATION_REQUEST_ID = "descendant_body_creation_operation_request_001"
SOURCE_SEMANTIC_OWNER = "DESCENDANT_BODY_CANDIDATE_STANDING_OPERATION"

INTENT_RECORD = "RECORD_PRESENCE_BOUNDARY"
BOUNDARY_QUESTION = (
    "Given that the completed relation lapse operation recorded "
    "RELATION_LAPSE_OPERATION_RECORDED and RELATION_LAPSE_SUPPORTED, while "
    "preserving relation lapse support as bounded non-punitive lapse support for "
    "relation_001 as historical relation record only, and while preserving no "
    "dissolution, reversal, termination, erasure, mutation, invalidation, "
    "punishment, teardown, living relation state, historical receipt preservation, "
    "presence boundary authorization, presence, identity, coupling, FIELD "
    "machinery, runtime, currentness, authority, or follow-on work, may a future "
    "presence boundary consider whether a separately bounded presence operation "
    "may be evaluated?"
)

OUTCOME_BLOCKED = "PRESENCE_BOUNDARY_BLOCKED"
OUTCOME_REQUIRES_LAPSE_OPERATION = "PRESENCE_BOUNDARY_REQUIRES_LAPSE_OPERATION"
OUTCOME_ALLOWED = "PRESENCE_BOUNDARY_ALLOWED"
OUTCOME_FAMILY = (
    OUTCOME_BLOCKED,
    OUTCOME_REQUIRES_LAPSE_OPERATION,
    OUTCOME_ALLOWED,
)

RESULT_NOT_EVALUATED = "NOT_EVALUATED"
RESULT_REQUIRES_LAPSE_OPERATION = "REQUIRES_RELATION_LAPSE_OPERATION"
RESULT_ALLOWED = "PRESENCE_OPERATION_CONSIDERATION_ALLOWED"

BLOCK_CODES = frozenset(
    {
        "REQUEST_NOT_MAPPING",
        "REQUEST_ROOTS_INVALID",
        "CONTROL_INVALID",
        "CONSTITUTIONAL_EVENT_KEY_INVALID",
        "REQUIRED_NON_CLAIM_INVALID",
        "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
        "UNSUPPORTED_INPUT",
    }
)

POSITIVE_BOUNDARY_BOOLEAN_FIELDS = (
    "presence_boundary_recorded",
    "presence_boundary_result_recorded",
    "presence_operation_consideration_allowed",
    "relation_lapse_operation_referenced",
    "relation_record_referenced",
    "relation_basis_referenced",
)

EXPECTED_CONSTITUTIONAL_EVENT_KEY: dict[str, Any] = {'target': {'boundary_id': 'presence_boundary_001',
            'boundary_type': 'PRESENCE_BOUNDARY',
            'boundary_version': '0.1.0',
            'boundary_scope': 'CONSIDER_PRESENCE_AFTER_RELATION_LAPSE_OPERATION_ONLY',
            'boundary_contract_reference': 'spec/PRESENCE_BOUNDARY_V0_MIN_SPEC.md',
            'boundary_contract_sha256': '900eeb0d104bf728208c80c2d5e487a93f408eb44c151e3c9e035ec629c6beda',
            'admissible_future_route': 'PRESENCE_BOUNDARY_THEN_PRESENCE_OPERATION_ONLY'},
 'current_lapse_operation_result': {'result_reference': 'artifacts/relation_lapse_operation_v0_min_v2/relation_lapse_operation_001__relation_lapse_operation_v0_min_v2_result.json',
                                    'result_sha256': '40f41db3498b7287fb40a96863ddbee3871231ddc1269a970fbfe7f9ae59d347',
                                    'result_version': '0.2.0',
                                    'resolver_module': 'resolve_relation_lapse_operation_v0_min_v2',
                                    'blocked': False,
                                    'block_code': None,
                                    'block_issue_path': None,
                                    'requires_boundary_allowance': False,
                                    'relation_record_persistence': {'relation_occurrence_remains_addressable': True},
                                    'downstream_stopping_point': {'admissible_future_route': 'RELATION_LAPSE_OPERATION_THEN_PRESENCE_BOUNDARY_OR_DISSOLUTION_BOUNDARY_CONSIDERATION_ONLY',
                                                                  'automatic_successor_created': False,
                                                                  'branch_choice_created': False,
                                                                  'current_branch_selected': False,
                                                                  'historical_realized_immediate_successor': 'PRESENCE_BOUNDARY',
                                                                  'historical_realized_route': 'RELATION_LAPSE_OPERATION '
                                                                                               '-> '
                                                                                               'PRESENCE_BOUNDARY',
                                                                  'next_rank_authorized': False,
                                                                  'next_rank_completed': False,
                                                                  'next_rank_executed': False,
                                                                  'next_rank_invoked': False,
                                                                  'next_rank_scheduled': False,
                                                                  'presence_boundary_consideration': 'OPEN_ONLY',
                                                                  'presence_boundary_selected': False,
                                                                  'relation_dissolution_boundary_consideration': 'OPEN_ONLY',
                                                                  'relation_dissolution_boundary_selected': False}},
 'source_operation': {'operation_id': 'relation_lapse_operation_001',
                      'operation_type': 'RELATION_LAPSE_OPERATION',
                      'operation_version': '0.1.0',
                      'operation_scope': 'EVALUATE_RELATION_LAPSE_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                      'operation_contract_reference': 'spec/RELATION_LAPSE_OPERATION_V0_MIN_SPEC.md',
                      'operation_contract_sha256': '46be083339d8722f6a1ce54f08fac463070c66979f370c5a3965b82b1d2e8bbb',
                      'admissible_future_route': 'RELATION_LAPSE_OPERATION_THEN_PRESENCE_BOUNDARY_OR_DISSOLUTION_BOUNDARY_CONSIDERATION_ONLY'},
 'source_operation_event_key': {'target': {'operation_id': 'relation_lapse_operation_001',
                                           'operation_type': 'RELATION_LAPSE_OPERATION',
                                           'operation_version': '0.1.0',
                                           'operation_scope': 'EVALUATE_RELATION_LAPSE_AFTER_BOUNDARY_ALLOWANCE_ONLY',
                                           'operation_contract_reference': 'spec/RELATION_LAPSE_OPERATION_V0_MIN_SPEC.md',
                                           'operation_contract_sha256': '46be083339d8722f6a1ce54f08fac463070c66979f370c5a3965b82b1d2e8bbb',
                                           'admissible_future_route': 'RELATION_LAPSE_OPERATION_THEN_PRESENCE_BOUNDARY_OR_DISSOLUTION_BOUNDARY_CONSIDERATION_ONLY'},
                                'source_boundary_event_key': {'target': {'boundary_id': 'relation_lapse_boundary_001',
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
                                                              'non_claim_attribution': {'boundary_local': {'owner': 'RELATION_LAPSE_BOUNDARY'}}},
                                'current_boundary_result': {'result_reference': 'artifacts/relation_lapse_boundary_v0_min_v2/relation_lapse_boundary_001__relation_lapse_boundary_v0_min_v2_result.json',
                                                            'result_sha256': 'a8a48b35d689a0c5a60f13bbfd7b5979e32264b8fff91ae973afcb1703fb705b',
                                                            'result_version': '0.2.0',
                                                            'resolver_module': 'resolve_relation_lapse_boundary_v0_min_v2',
                                                            'blocked': False,
                                                            'block_code': None,
                                                            'block_issue_path': None,
                                                            'requires_reversibility': False},
                                'source_boundary': {'boundary_id': 'relation_lapse_boundary_001',
                                                    'boundary_type': 'RELATION_LAPSE_BOUNDARY',
                                                    'boundary_version': '0.1.0',
                                                    'boundary_scope': 'CONSIDER_RELATION_LAPSE_AFTER_RELATION_REVERSIBILITY_SUPPORT_BEFORE_PRESENCE_ONLY',
                                                    'boundary_contract_reference': 'spec/RELATION_LAPSE_BOUNDARY_V0_MIN_SPEC.md',
                                                    'boundary_contract_sha256': 'd60251d5e1268a6b942a6076c779630d7d2f71d714be1aeef38ad3fe4aa86e4b',
                                                    'admissible_future_route': 'RELATION_LAPSE_BOUNDARY_THEN_RELATION_LAPSE_OPERATION_ONLY'},
                                'operation_event': {'persistent_operation_id': 'relation_lapse_operation_001',
                                                    'persistent_boundary_id': 'relation_lapse_boundary_001',
                                                    'current_boundary_result_reference': 'artifacts/relation_lapse_boundary_v0_min_v2/relation_lapse_boundary_001__relation_lapse_boundary_v0_min_v2_result.json',
                                                    'current_boundary_result_sha256': 'a8a48b35d689a0c5a60f13bbfd7b5979e32264b8fff91ae973afcb1703fb705b',
                                                    'relation_lapse_id': 'relation_lapse_001',
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
                                'historical_operation': {'historical_operation_id': 'relation_lapse_operation_001',
                                                         'result_reference': 'artifacts/integrity_host_v0_min_coexistence_relation_lapse_operation_v0_min/relation_lapse_operation_001__relation_lapse_operation_v0_min_result.json',
                                                         'result_sha256': 'f5d1b426a134ec7b10d75b7441123e99167fe7ca26552c8801ae9b13e76a7a6e',
                                                         'outcome': 'RELATION_LAPSE_OPERATION_RECORDED',
                                                         'operation_result': 'RELATION_LAPSE_SUPPORTED',
                                                         'relation_id': 'relation_001',
                                                         'relation_lapse_id': 'relation_lapse_001',
                                                         'immediate_next_rank': 'PRESENCE_BOUNDARY',
                                                         'result_is_current_permission': False,
                                                         'result_is_current_source': False,
                                                         'result_is_current_occurrence': False,
                                                         'result_replayed': False},
                                'non_claim_attribution': {'operation_local': {'owner': 'RELATION_LAPSE_OPERATION'}}},
 'boundary_event': {'persistent_boundary_id': 'presence_boundary_001',
                    'persistent_lapse_operation_id': 'relation_lapse_operation_001',
                    'current_lapse_operation_result_reference': 'artifacts/relation_lapse_operation_v0_min_v2/relation_lapse_operation_001__relation_lapse_operation_v0_min_v2_result.json',
                    'current_lapse_operation_result_sha256': '40f41db3498b7287fb40a96863ddbee3871231ddc1269a970fbfe7f9ae59d347',
                    'relation_lapse_id': 'relation_lapse_001',
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
 'freshness': {'current_lapse_operation_result_identity_declared': True,
               'current_lapse_operation_result_identity_distinct_from_historical_boundary_occurrence': True,
               'current_boundary_event_identity_declared': True,
               'historical_boundary_result_is_current_permission': False,
               'historical_boundary_result_is_current_source': False,
               'historical_boundary_result_is_current_occurrence': False,
               'historical_boundary_occurrence_reused': False,
               'historical_boundary_material_reused': False,
               'historical_boundary_result_replayed': False,
               'historical_success_treated_as_fresh_permission': False},
 'historical_boundary': {'historical_boundary_id': 'presence_boundary_001',
                         'result_reference': 'artifacts/integrity_host_v0_min_coexistence_presence_boundary_v0_min/presence_boundary_001__presence_boundary_v0_min_result.json',
                         'result_sha256': 'af62fb008965438599e07bde4b8a2fe06f946d4ba79300e8a9226ebc202f6a5b',
                         'outcome': 'PRESENCE_BOUNDARY_ALLOWED',
                         'boundary_result': 'PRESENCE_OPERATION_CONSIDERATION_ALLOWED',
                         'relation_id': 'relation_001',
                         'immediate_next_rank': 'PRESENCE_OPERATION',
                         'result_is_current_permission': False,
                         'result_is_current_source': False,
                         'result_is_current_occurrence': False,
                         'result_replayed': False},
 'non_claim_attribution': {'boundary_local': {'owner': 'PRESENCE_BOUNDARY'}}}
EXPECTED_ORDINARY_RELATION_LAPSE_BASIS: dict[str, Any] = {'source_outcome': 'RELATION_LAPSE_OPERATION_RECORDED',
 'source_relation_lapse_result': 'RELATION_LAPSE_SUPPORTED',
 'relation_lapse_supported': True,
 'relation_lapse_authorized': True,
 'relation_lapse_performed': True,
 'relation_lapse_recorded': True,
 'relation_record_confirmed_as_historical_only': True}
EXPECTED_REQUIRED_NON_CLAIMS: dict[str, Any] = {'source_relation_boundary': {'relation_authorized': False,
                              'relation_created': False,
                              'relation_operation_performed': False,
                              'coupling_created': False,
                              'presence_established': False,
                              'identity_created': False,
                              'follow_on_authorized': False,
                              'follow_on_work_authorized': False},
 'source_relation_operation': {'field_machinery_created': False,
                               'runtime_created': False,
                               'api_created': False,
                               'currentness_created': False,
                               'authority_created': False,
                               'standing_created': False,
                               'output_authorized': False,
                               'action_authorized': False,
                               'derivative_reception_authorized': False,
                               'synchronization_authorized': False,
                               'coupling_assigned_to_relation': False,
                               'coupling_assigned_to_first_crossing_a': False,
                               'coupling_assigned_to_first_crossing_b': False,
                               'coupling_assigned_to_descendant_body_a': False,
                               'coupling_assigned_to_descendant_body_b': False,
                               'coupling_assigned_to_candidate_a': False,
                               'coupling_assigned_to_candidate_b': False,
                               'coupling_created': False,
                               'third_candidate_created': False,
                               'third_model_admitted': False,
                               'presence_established': False,
                               'identity_created': False,
                               'standing_descendant_created': False,
                               'descendant_standing_check_performed': False,
                               'follow_on_authorized': False,
                               'follow_on_work_authorized': False,
                               'prior_unsupported_candidate_a_claim_validated': False,
                               'prior_unsupported_candidate_b_claim_validated': False,
                               'prior_unsupported_derivation_event_claim_validated': False,
                               'valid_derivation_event_recorded': False,
                               'affected_file_repaired': False,
                               'affected_file_edited': False,
                               'affected_file_deleted': False,
                               'affected_file_overwritten': False,
                               'affected_file_replaced': False,
                               'affected_file_redeemed': False,
                               'affected_file_treated_as_clean_basis': False,
                               'contaminated_lineage_treated_as_clean_basis': False,
                               'relation_boundary_overridden': False,
                               'relation_boundary_bypassed': False,
                               'first_crossing_operation_v1_repaired': False,
                               'first_crossing_operation_v1_overwritten': False,
                               'first_crossing_operation_v1_converted_to_standing': False,
                               'first_crossing_operation_v2_overridden': False,
                               'first_crossing_operation_v2_bypassed': False,
                               'scan_performed': False,
                               'repository_scan_performed': False,
                               'file_discovery_performed': False,
                               'repair_performed': False,
                               'validation_enforced': False,
                               'hidden_repair_performed': False,
                               'silent_overwrite_performed': False,
                               'direct_relation_operation_spec_to_relation_operation_completion': False,
                               'direct_relation_boundary_allowance_to_relation_without_operation': False,
                               'direct_first_crossing_to_relation_without_relation_boundary_and_operation': False,
                               'direct_relation_to_field_machinery': False,
                               'direct_relation_to_runtime': False,
                               'direct_relation_to_authority_currentness': False,
                               'direct_relation_to_coupling_assignment': False,
                               'direct_relation_to_coupling_creation': False,
                               'direct_relation_to_third_candidate_route': False,
                               'direct_relation_to_third_model_route': False,
                               'direct_relation_to_presence': False,
                               'direct_relation_to_identity': False,
                               'direct_relation_to_standing_descendant': False,
                               'direct_relation_to_descendant_standing': False,
                               'direct_relation_to_output_action': False,
                               'direct_relation_to_follow_on_work': False},
 'source_reversibility_boundary': {'relation_reversibility_authorized': False,
                                   'relation_lapse_authorized': False,
                                   'relation_dissolution_authorized': False,
                                   'relation_reversibility_performed': False,
                                   'relation_lapse_performed': False,
                                   'relation_dissolution_performed': False,
                                   'relation_erased': False,
                                   'relation_mutated': False,
                                   'relation_invalidated': False,
                                   'relation_punished': False,
                                   'relation_teardown_created': False,
                                   'relation_record_preserved_as_historical_receipt': False,
                                   'living_relation_state_created': False,
                                   'living_relation_state_lapsed': False,
                                   'living_relation_state_dissolved': False,
                                   'presence_boundary_authorized': False,
                                   'presence_established': False,
                                   'identity_created': False,
                                   'field_machinery_created': False,
                                   'runtime_created': False,
                                   'api_created': False,
                                   'currentness_created': False,
                                   'authority_created': False,
                                   'standing_created': False,
                                   'output_authorized': False,
                                   'action_authorized': False,
                                   'derivative_reception_authorized': False,
                                   'synchronization_authorized': False,
                                   'coupling_assigned_to_relation': False,
                                   'coupling_assigned_to_first_crossing_a': False,
                                   'coupling_assigned_to_first_crossing_b': False,
                                   'coupling_assigned_to_descendant_body_a': False,
                                   'coupling_assigned_to_descendant_body_b': False,
                                   'coupling_assigned_to_candidate_a': False,
                                   'coupling_assigned_to_candidate_b': False,
                                   'coupling_created': False,
                                   'third_candidate_created': False,
                                   'third_model_admitted': False,
                                   'standing_descendant_created': False,
                                   'descendant_standing_check_performed': False,
                                   'follow_on_authorized': False,
                                   'follow_on_work_authorized': False,
                                   'prior_unsupported_candidate_a_claim_validated': False,
                                   'prior_unsupported_candidate_b_claim_validated': False,
                                   'prior_unsupported_derivation_event_claim_validated': False,
                                   'valid_derivation_event_recorded': False,
                                   'affected_file_repaired': False,
                                   'affected_file_edited': False,
                                   'affected_file_deleted': False,
                                   'affected_file_overwritten': False,
                                   'affected_file_replaced': False,
                                   'affected_file_redeemed': False,
                                   'affected_file_treated_as_clean_basis': False,
                                   'contaminated_lineage_treated_as_clean_basis': False,
                                   'relation_operation_overridden': False,
                                   'relation_operation_bypassed': False,
                                   'relation_operation_invalidated': False,
                                   'relation_record_erased': False,
                                   'relation_record_mutated': False,
                                   'scan_performed': False,
                                   'repository_scan_performed': False,
                                   'file_discovery_performed': False,
                                   'repair_performed': False,
                                   'validation_enforced': False,
                                   'hidden_repair_performed': False,
                                   'silent_overwrite_performed': False,
                                   'direct_relation_reversibility_boundary_to_relation_reversibility_operation_completion': False,
                                   'direct_relation_operation_to_relation_lapse_without_reversibility_boundary_and_operation': False,
                                   'direct_relation_operation_to_relation_dissolution_without_reversibility_boundary_and_operation': False,
                                   'direct_relation_operation_to_relation_reversal_without_reversibility_boundary_and_operation': False,
                                   'direct_relation_operation_to_presence_boundary_without_reversibility_boundary_consideration': False,
                                   'direct_relation_to_presence': False,
                                   'direct_relation_to_identity': False,
                                   'direct_relation_to_coupling_assignment': False,
                                   'direct_relation_to_coupling_creation': False,
                                   'direct_relation_to_field_machinery': False,
                                   'direct_relation_to_runtime': False,
                                   'direct_relation_to_authority_currentness': False,
                                   'direct_relation_reversibility_boundary_to_relation_erasure': False,
                                   'direct_relation_reversibility_boundary_to_relation_mutation': False,
                                   'direct_relation_reversibility_boundary_to_relation_invalidation': False,
                                   'direct_relation_reversibility_boundary_to_punitive_lapse_interpretation': False,
                                   'direct_relation_reversibility_boundary_to_teardown_logic': False,
                                   'direct_relation_reversibility_boundary_to_presence_boundary_authorization': False,
                                   'direct_relation_reversibility_boundary_to_presence_establishment': False,
                                   'direct_relation_reversibility_boundary_to_follow_on_work': False},
 'source_reversibility_operation': {'relation_record_is_living_relation_state': False,
                                    'living_relation_state_created': False,
                                    'living_relation_state_lapsed': False,
                                    'living_relation_state_dissolved': False,
                                    'relation_lapse_authorized': False,
                                    'relation_lapse_performed': False,
                                    'relation_dissolution_authorized': False,
                                    'relation_dissolution_performed': False,
                                    'relation_reversed': False,
                                    'relation_terminated': False,
                                    'relation_erased': False,
                                    'relation_mutated': False,
                                    'relation_invalidated': False,
                                    'relation_punished': False,
                                    'relation_teardown_created': False,
                                    'historical_receipt_preservation_authorized': False,
                                    'historical_receipt_preserved': False,
                                    'presence_boundary_authorized': False,
                                    'presence_established': False,
                                    'identity_created': False,
                                    'field_machinery_created': False,
                                    'runtime_created': False,
                                    'api_created': False,
                                    'currentness_created': False,
                                    'authority_created': False,
                                    'standing_created': False,
                                    'output_authorized': False,
                                    'action_authorized': False,
                                    'derivative_reception_authorized': False,
                                    'synchronization_authorized': False,
                                    'coupling_assigned_to_relation': False,
                                    'coupling_assigned_to_first_crossing_a': False,
                                    'coupling_assigned_to_first_crossing_b': False,
                                    'coupling_assigned_to_descendant_body_a': False,
                                    'coupling_assigned_to_descendant_body_b': False,
                                    'coupling_assigned_to_candidate_a': False,
                                    'coupling_assigned_to_candidate_b': False,
                                    'coupling_created': False,
                                    'third_candidate_created': False,
                                    'third_model_admitted': False,
                                    'standing_descendant_created': False,
                                    'descendant_standing_check_performed': False,
                                    'follow_on_authorized': False,
                                    'follow_on_work_authorized': False,
                                    'prior_unsupported_candidate_a_claim_validated': False,
                                    'prior_unsupported_candidate_b_claim_validated': False,
                                    'prior_unsupported_derivation_event_claim_validated': False,
                                    'valid_derivation_event_recorded': False,
                                    'affected_file_repaired': False,
                                    'affected_file_edited': False,
                                    'affected_file_deleted': False,
                                    'affected_file_overwritten': False,
                                    'affected_file_replaced': False,
                                    'affected_file_redeemed': False,
                                    'affected_file_treated_as_clean_basis': False,
                                    'contaminated_lineage_treated_as_clean_basis': False,
                                    'relation_reversibility_boundary_overridden': False,
                                    'relation_reversibility_boundary_bypassed': False,
                                    'relation_reversibility_boundary_invalidated': False,
                                    'relation_operation_overridden': False,
                                    'relation_operation_bypassed': False,
                                    'relation_operation_invalidated': False,
                                    'relation_record_erased': False,
                                    'relation_record_mutated': False,
                                    'scan_performed': False,
                                    'repository_scan_performed': False,
                                    'file_discovery_performed': False,
                                    'repair_performed': False,
                                    'validation_enforced': False,
                                    'hidden_repair_performed': False,
                                    'silent_overwrite_performed': False,
                                    'direct_relation_reversibility_operation_spec_to_relation_reversibility_completion': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_lapse': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_dissolution': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_reversal': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_termination': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_erasure': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_mutation': False,
                                    'direct_relation_reversibility_boundary_allowance_to_relation_invalidation': False,
                                    'direct_relation_reversibility_boundary_allowance_to_punitive_lapse_interpretation': False,
                                    'direct_relation_reversibility_boundary_allowance_to_teardown_logic': False,
                                    'direct_relation_reversibility_boundary_allowance_to_living_relation_state': False,
                                    'direct_relation_reversibility_boundary_allowance_to_historical_receipt_preservation': False,
                                    'direct_relation_reversibility_boundary_allowance_to_presence_boundary_authorization': False,
                                    'direct_relation_reversibility_boundary_allowance_to_presence_establishment': False,
                                    'direct_relation_reversibility_operation_to_relation_lapse_without_lapse_boundary': False,
                                    'direct_relation_reversibility_operation_to_relation_dissolution_without_dissolution_boundary': False,
                                    'direct_relation_reversibility_operation_to_presence_boundary_without_separate_boundary_consideration': False,
                                    'direct_relation_to_presence': False,
                                    'direct_relation_to_identity': False,
                                    'direct_relation_to_coupling_assignment': False,
                                    'direct_relation_to_coupling_creation': False,
                                    'direct_relation_to_field_machinery': False,
                                    'direct_relation_to_runtime': False,
                                    'direct_relation_to_authority_currentness': False,
                                    'direct_relation_reversibility_operation_to_follow_on_work': False},
 'source_lapse_boundary': {'relation_lapse_authorized': False,
                           'relation_lapse_performed': False,
                           'relation_lapse_recorded': False,
                           'relation_lapse_supported': False,
                           'relation_dissolution_authorized': False,
                           'relation_dissolution_performed': False,
                           'relation_reversed': False,
                           'relation_terminated': False,
                           'relation_erased': False,
                           'relation_mutated': False,
                           'relation_invalidated': False,
                           'relation_punished': False,
                           'relation_teardown_created': False,
                           'living_relation_state_created': False,
                           'living_relation_state_lapsed': False,
                           'living_relation_state_dissolved': False,
                           'historical_receipt_preservation_authorized': False,
                           'historical_receipt_preserved': False,
                           'presence_boundary_authorized': False,
                           'presence_established': False,
                           'identity_created': False,
                           'field_machinery_created': False,
                           'runtime_created': False,
                           'api_created': False,
                           'currentness_created': False,
                           'authority_created': False,
                           'standing_created': False,
                           'output_authorized': False,
                           'action_authorized': False,
                           'derivative_reception_authorized': False,
                           'synchronization_authorized': False,
                           'coupling_assigned_to_relation': False,
                           'coupling_assigned_to_first_crossing_a': False,
                           'coupling_assigned_to_first_crossing_b': False,
                           'coupling_assigned_to_descendant_body_a': False,
                           'coupling_assigned_to_descendant_body_b': False,
                           'coupling_assigned_to_candidate_a': False,
                           'coupling_assigned_to_candidate_b': False,
                           'coupling_created': False,
                           'third_candidate_created': False,
                           'third_model_admitted': False,
                           'standing_descendant_created': False,
                           'descendant_standing_check_performed': False,
                           'follow_on_authorized': False,
                           'follow_on_work_authorized': False,
                           'prior_unsupported_candidate_a_claim_validated': False,
                           'prior_unsupported_candidate_b_claim_validated': False,
                           'prior_unsupported_derivation_event_claim_validated': False,
                           'valid_derivation_event_recorded': False,
                           'affected_file_repaired': False,
                           'affected_file_edited': False,
                           'affected_file_deleted': False,
                           'affected_file_overwritten': False,
                           'affected_file_replaced': False,
                           'affected_file_redeemed': False,
                           'affected_file_treated_as_clean_basis': False,
                           'contaminated_lineage_treated_as_clean_basis': False,
                           'relation_reversibility_operation_overridden': False,
                           'relation_reversibility_operation_bypassed': False,
                           'relation_reversibility_operation_invalidated': False,
                           'relation_operation_overridden': False,
                           'relation_operation_bypassed': False,
                           'relation_operation_invalidated': False,
                           'relation_record_erased': False,
                           'relation_record_mutated': False,
                           'scan_performed': False,
                           'repository_scan_performed': False,
                           'file_discovery_performed': False,
                           'repair_performed': False,
                           'validation_enforced': False,
                           'hidden_repair_performed': False,
                           'silent_overwrite_performed': False,
                           'direct_relation_lapse_boundary_to_relation_lapse_operation_completion': False,
                           'direct_relation_reversibility_operation_to_relation_lapse_without_lapse_boundary_and_operation': False,
                           'direct_relation_reversibility_operation_to_relation_dissolution_without_dissolution_boundary_and_operation': False,
                           'direct_relation_reversibility_operation_to_presence_boundary_without_lapse_boundary_consideration': False,
                           'direct_relation_lapse_boundary_to_relation_lapse': False,
                           'direct_relation_lapse_boundary_to_relation_dissolution': False,
                           'direct_relation_lapse_boundary_to_relation_reversal': False,
                           'direct_relation_lapse_boundary_to_relation_termination': False,
                           'direct_relation_lapse_boundary_to_relation_erasure': False,
                           'direct_relation_lapse_boundary_to_relation_mutation': False,
                           'direct_relation_lapse_boundary_to_relation_invalidation': False,
                           'direct_relation_lapse_boundary_to_punitive_lapse_interpretation': False,
                           'direct_relation_lapse_boundary_to_teardown_logic': False,
                           'direct_relation_lapse_boundary_to_living_relation_state': False,
                           'direct_relation_lapse_boundary_to_historical_receipt_preservation': False,
                           'direct_relation_lapse_boundary_to_presence_boundary_authorization': False,
                           'direct_relation_lapse_boundary_to_presence_establishment': False,
                           'direct_relation_to_presence': False,
                           'direct_relation_to_identity': False,
                           'direct_relation_to_coupling_assignment': False,
                           'direct_relation_to_coupling_creation': False,
                           'direct_relation_to_field_machinery': False,
                           'direct_relation_to_runtime': False,
                           'direct_relation_to_authority_currentness': False,
                           'direct_relation_lapse_boundary_to_follow_on_work': False},
 'source_lapse_operation': {'relation_lapse_is_punishment': False,
                            'relation_lapse_is_dissolution': False,
                            'relation_lapse_is_erasure': False,
                            'relation_lapse_is_teardown': False,
                            'relation_lapse_is_living_relation_state': False,
                            'relation_lapse_is_presence_boundary_authorization': False,
                            'relation_lapse_is_presence': False,
                            'relation_lapse_is_identity': False,
                            'relation_lapse_is_coupling': False,
                            'relation_lapse_is_field_machinery': False,
                            'relation_lapse_is_runtime': False,
                            'relation_lapse_is_currentness': False,
                            'relation_lapse_is_authority': False,
                            'relation_lapse_is_follow_on_authorization': False,
                            'relation_lapse_is_follow_on_work': False,
                            'relation_record_is_living_relation_state': False,
                            'living_relation_state_created': False,
                            'living_relation_state_lapsed': False,
                            'living_relation_state_dissolved': False,
                            'relation_dissolution_authorized': False,
                            'relation_dissolution_performed': False,
                            'relation_reversed': False,
                            'relation_terminated': False,
                            'relation_erased': False,
                            'relation_mutated': False,
                            'relation_invalidated': False,
                            'relation_punished': False,
                            'relation_teardown_created': False,
                            'historical_receipt_preservation_authorized': False,
                            'historical_receipt_preserved': False,
                            'presence_boundary_authorized': False,
                            'presence_established': False,
                            'identity_created': False,
                            'field_machinery_created': False,
                            'runtime_created': False,
                            'api_created': False,
                            'currentness_created': False,
                            'authority_created': False,
                            'standing_created': False,
                            'output_authorized': False,
                            'action_authorized': False,
                            'derivative_reception_authorized': False,
                            'synchronization_authorized': False,
                            'coupling_assigned_to_relation': False,
                            'coupling_assigned_to_first_crossing_a': False,
                            'coupling_assigned_to_first_crossing_b': False,
                            'coupling_assigned_to_descendant_body_a': False,
                            'coupling_assigned_to_descendant_body_b': False,
                            'coupling_assigned_to_candidate_a': False,
                            'coupling_assigned_to_candidate_b': False,
                            'coupling_created': False,
                            'third_candidate_created': False,
                            'third_model_admitted': False,
                            'standing_descendant_created': False,
                            'descendant_standing_check_performed': False,
                            'follow_on_authorized': False,
                            'follow_on_work_authorized': False,
                            'prior_unsupported_candidate_a_claim_validated': False,
                            'prior_unsupported_candidate_b_claim_validated': False,
                            'prior_unsupported_derivation_event_claim_validated': False,
                            'valid_derivation_event_recorded': False,
                            'affected_file_repaired': False,
                            'affected_file_edited': False,
                            'affected_file_deleted': False,
                            'affected_file_overwritten': False,
                            'affected_file_replaced': False,
                            'affected_file_redeemed': False,
                            'affected_file_treated_as_clean_basis': False,
                            'contaminated_lineage_treated_as_clean_basis': False,
                            'relation_lapse_boundary_overridden': False,
                            'relation_lapse_boundary_bypassed': False,
                            'relation_lapse_boundary_invalidated': False,
                            'relation_operation_overridden': False,
                            'relation_operation_bypassed': False,
                            'relation_operation_invalidated': False,
                            'relation_record_erased': False,
                            'relation_record_mutated': False,
                            'scan_performed': False,
                            'repository_scan_performed': False,
                            'file_discovery_performed': False,
                            'repair_performed': False,
                            'validation_enforced': False,
                            'hidden_repair_performed': False,
                            'silent_overwrite_performed': False,
                            'direct_relation_lapse_operation_spec_to_relation_lapse_completion': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_dissolution': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_reversal': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_termination': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_erasure': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_mutation': False,
                            'direct_relation_lapse_boundary_allowance_to_relation_invalidation': False,
                            'direct_relation_lapse_boundary_allowance_to_punitive_lapse_interpretation': False,
                            'direct_relation_lapse_boundary_allowance_to_teardown_logic': False,
                            'direct_relation_lapse_boundary_allowance_to_living_relation_state': False,
                            'direct_relation_lapse_boundary_allowance_to_historical_receipt_preservation': False,
                            'direct_relation_lapse_boundary_allowance_to_presence_boundary_authorization': False,
                            'direct_relation_lapse_boundary_allowance_to_presence_establishment': False,
                            'direct_relation_lapse_operation_to_relation_dissolution_without_dissolution_boundary': False,
                            'direct_relation_lapse_operation_to_presence_boundary_without_separate_boundary_consideration': False,
                            'direct_relation_to_presence': False,
                            'direct_relation_to_identity': False,
                            'direct_relation_to_coupling_assignment': False,
                            'direct_relation_to_coupling_creation': False,
                            'direct_relation_to_field_machinery': False,
                            'direct_relation_to_runtime': False,
                            'direct_relation_to_authority_currentness': False,
                            'direct_relation_lapse_operation_to_follow_on_work': False},
 'boundary_local': {'presence_supported': False,
                    'presence_authorized': False,
                    'presence_established': False,
                    'presence_recorded': False,
                    'presence_is_identity': False,
                    'presence_is_coupling': False,
                    'presence_is_field_machinery': False,
                    'presence_is_runtime': False,
                    'presence_is_currentness': False,
                    'presence_is_authority': False,
                    'presence_is_standing': False,
                    'identity_created': False,
                    'identity_authorized': False,
                    'coupling_assigned_to_relation': False,
                    'coupling_assigned_to_first_crossing_a': False,
                    'coupling_assigned_to_first_crossing_b': False,
                    'coupling_assigned_to_descendant_body_a': False,
                    'coupling_assigned_to_descendant_body_b': False,
                    'coupling_assigned_to_candidate_a': False,
                    'coupling_assigned_to_candidate_b': False,
                    'coupling_created': False,
                    'field_machinery_created': False,
                    'runtime_created': False,
                    'api_created': False,
                    'currentness_created': False,
                    'authority_created': False,
                    'standing_created': False,
                    'output_authorized': False,
                    'action_authorized': False,
                    'derivative_reception_authorized': False,
                    'synchronization_authorized': False,
                    'follow_on_authorized': False,
                    'follow_on_work_authorized': False,
                    'relation_dissolution_authorized': False,
                    'relation_dissolution_performed': False,
                    'relation_reversed': False,
                    'relation_terminated': False,
                    'relation_erased': False,
                    'relation_mutated': False,
                    'relation_invalidated': False,
                    'relation_punished': False,
                    'relation_teardown_created': False,
                    'living_relation_state_created': False,
                    'living_relation_state_lapsed': False,
                    'living_relation_state_dissolved': False,
                    'historical_receipt_preservation_authorized': False,
                    'historical_receipt_preserved': False,
                    'third_candidate_created': False,
                    'third_model_admitted': False,
                    'standing_descendant_created': False,
                    'descendant_standing_check_performed': False,
                    'prior_unsupported_candidate_a_claim_validated': False,
                    'prior_unsupported_candidate_b_claim_validated': False,
                    'prior_unsupported_derivation_event_claim_validated': False,
                    'valid_derivation_event_recorded': False,
                    'affected_file_repaired': False,
                    'affected_file_edited': False,
                    'affected_file_deleted': False,
                    'affected_file_overwritten': False,
                    'affected_file_replaced': False,
                    'affected_file_redeemed': False,
                    'affected_file_treated_as_clean_basis': False,
                    'contaminated_lineage_treated_as_clean_basis': False,
                    'relation_lapse_operation_overridden': False,
                    'relation_lapse_operation_bypassed': False,
                    'relation_lapse_operation_invalidated': False,
                    'relation_operation_overridden': False,
                    'relation_operation_bypassed': False,
                    'relation_operation_invalidated': False,
                    'relation_record_erased': False,
                    'relation_record_mutated': False,
                    'scan_performed': False,
                    'repository_scan_performed': False,
                    'file_discovery_performed': False,
                    'repair_performed': False,
                    'validation_enforced': False,
                    'hidden_repair_performed': False,
                    'silent_overwrite_performed': False,
                    'direct_presence_boundary_spec_to_presence_operation_completion': False,
                    'direct_relation_lapse_operation_to_presence_without_presence_boundary_and_operation': False,
                    'direct_relation_lapse_operation_to_identity': False,
                    'direct_relation_lapse_operation_to_coupling_assignment': False,
                    'direct_relation_lapse_operation_to_coupling_creation': False,
                    'direct_relation_lapse_operation_to_field_machinery': False,
                    'direct_relation_lapse_operation_to_runtime': False,
                    'direct_relation_lapse_operation_to_authority_currentness': False,
                    'direct_relation_lapse_operation_to_follow_on_work': False,
                    'direct_presence_boundary_to_presence': False,
                    'direct_presence_boundary_to_identity': False,
                    'direct_presence_boundary_to_coupling_assignment': False,
                    'direct_presence_boundary_to_coupling_creation': False,
                    'direct_presence_boundary_to_field_machinery': False,
                    'direct_presence_boundary_to_runtime': False,
                    'direct_presence_boundary_to_authority_currentness': False,
                    'direct_presence_boundary_to_standing': False,
                    'direct_presence_boundary_to_output_authorization': False,
                    'direct_presence_boundary_to_action_authorization': False,
                    'direct_presence_boundary_to_derivative_reception': False,
                    'direct_presence_boundary_to_synchronization': False,
                    'direct_presence_boundary_to_follow_on_work': False,
                    'direct_presence_boundary_to_relation_dissolution': False,
                    'direct_presence_boundary_to_relation_reversal': False,
                    'direct_presence_boundary_to_relation_termination': False,
                    'direct_presence_boundary_to_relation_erasure': False,
                    'direct_presence_boundary_to_relation_mutation': False,
                    'direct_presence_boundary_to_relation_invalidation': False,
                    'direct_presence_boundary_to_punitive_interpretation': False,
                    'direct_presence_boundary_to_teardown_logic': False,
                    'direct_presence_boundary_to_living_relation_state': False,
                    'direct_presence_boundary_to_historical_receipt_preservation': False}}

EXECUTABLE_ROOT_KEYS = frozenset(
    {
        "intent",
        "boundary_question",
        "constitutional_event_key",
        "ordinary_relation_lapse_basis",
        "required_non_claims",
    }
)


def _leaf_paths(value: Mapping[str, Any], prefix: str) -> tuple[str, ...]:
    paths: list[str] = []
    for key, child in value.items():
        path = f"{prefix}.{key}"
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
ORDINARY_RELATION_LAPSE_BASIS_PATHS = frozenset(
    f"ordinary_relation_lapse_basis.{key}"
    for key in EXPECTED_ORDINARY_RELATION_LAPSE_BASIS
)

SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_relation_boundary"]
)
SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_relation_operation"]
)
SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_reversibility_boundary"]
)
SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_reversibility_operation"]
)
SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_lapse_boundary"]
)
SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["source_lapse_operation"]
)
PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS = tuple(
    EXPECTED_REQUIRED_NON_CLAIMS["boundary_local"]
)

SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_relation_boundary.{key}"
    for key in SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_relation_operation.{key}"
    for key in SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_reversibility_boundary.{key}"
    for key in SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_reversibility_operation.{key}"
    for key in SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_lapse_boundary.{key}"
    for key in SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.source_lapse_operation.{key}"
    for key in SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_KEYS
)
PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS = frozenset(
    f"required_non_claims.boundary_local.{key}"
    for key in PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS
)
SOURCE_REQUIRED_NON_CLAIM_PATHS = frozenset().union(
    SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
    SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_PATHS,
    SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
    SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_PATHS,
    SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_PATHS,
    SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_PATHS,
)
REQUIRED_NON_CLAIM_PATHS = frozenset().union(
    SOURCE_REQUIRED_NON_CLAIM_PATHS,
    PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS,
)
CLASS_PATHS = {
    "CONTROL": CONTROL_PATHS,
    "CONSTITUTIONAL_EVENT_KEY": CONSTITUTIONAL_EVENT_KEY_PATHS,
    "ORDINARY_RELATION_LAPSE_BASIS": ORDINARY_RELATION_LAPSE_BASIS_PATHS,
    "REQUIRED_NON_CLAIM": REQUIRED_NON_CLAIM_PATHS,
}
ALL_REQUIRED_PATHS = frozenset().union(*CLASS_PATHS.values())


def _assert_manifest_lock() -> None:
    assert len(CONTROL_PATHS) == 3
    assert len(CONSTITUTIONAL_EVENT_KEY_PATHS) == 422
    assert len(SOURCE_OPERATION_EVENT_KEY_PATHS) == 347
    assert len(ORDINARY_RELATION_LAPSE_BASIS_PATHS) == 7
    assert len(SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_PATHS) == 8
    assert len(SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_PATHS) == 68
    assert len(SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_PATHS) == 86
    assert len(SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_PATHS) == 96
    assert len(SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_PATHS) == 97
    assert len(SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_PATHS) == 107
    assert len(SOURCE_REQUIRED_NON_CLAIM_PATHS) == 462
    assert len(PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_PATHS) == 110
    assert len(REQUIRED_NON_CLAIM_PATHS) == 572
    assert len(ALL_REQUIRED_PATHS) == 1004
    classes = tuple(CLASS_PATHS.values())
    for index, paths in enumerate(classes):
        for other in classes[index + 1 :]:
            assert not paths & other
    parents: set[str] = set()
    for path in ALL_REQUIRED_PATHS:
        parts = path.split(".")
        parents.update(".".join(parts[:end]) for end in range(1, len(parts)))
    assert not parents & ALL_REQUIRED_PATHS
    assert all(
        value is False
        for group in EXPECTED_REQUIRED_NON_CLAIMS.values()
        for value in group.values()
    )
    assert not (
        set(POSITIVE_BOUNDARY_BOOLEAN_FIELDS)
        & set(PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS)
    )


_assert_manifest_lock()


def build_declared_presence_boundary_v0_min_v2_request() -> dict[str, Any]:
    """Build the exact five-root request without I/O or constitutional occurrence."""

    return {
        "intent": INTENT_RECORD,
        "boundary_question": BOUNDARY_QUESTION,
        "constitutional_event_key": deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY),
        "ordinary_relation_lapse_basis": deepcopy(
            EXPECTED_ORDINARY_RELATION_LAPSE_BASIS
        ),
        "required_non_claims": deepcopy(EXPECTED_REQUIRED_NON_CLAIMS),
    }


build_presence_boundary_v0_min_v2_request = (
    build_declared_presence_boundary_v0_min_v2_request
)


def _same_exact_value(actual: Any, expected: Any) -> bool:
    return type(actual) is type(expected) and actual == expected


def _check(
    name: str,
    field_class: str,
    path: str,
    passed: bool,
    code: str | None = None,
) -> dict[str, Any]:
    return {
        "name": name,
        "field_class": field_class,
        "path": path,
        "passed": passed,
        "code": None if passed else code,
    }


def _validate_exact_mapping(
    actual: Any,
    expected: Mapping[str, Any],
    prefix: str,
    field_class: str,
    invalid_code: str,
) -> tuple[bool, list[dict[str, Any]], str | None, str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(actual, Mapping):
        checks.append(
            _check(
                f"{prefix}_mapping",
                field_class,
                prefix,
                False,
                invalid_code,
            )
        )
        return False, checks, prefix, invalid_code

    expected_keys = set(expected)
    actual_keys = set(actual)
    extras = sorted(actual_keys - expected_keys)
    if extras:
        issue = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                f"{prefix}_no_unsupported_fields",
                field_class,
                issue,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return False, checks, issue, "UNSUPPORTED_INPUT"

    missing = sorted(expected_keys - actual_keys)
    if missing:
        issue = f"{prefix}.{missing[0]}"
        checks.append(
            _check(
                f"{prefix}_complete",
                field_class,
                issue,
                False,
                invalid_code,
            )
        )
        return False, checks, issue, invalid_code

    checks.append(
        _check(
            f"{prefix}_exact_keys",
            field_class,
            prefix,
            True,
        )
    )
    for key, expected_value in expected.items():
        path = f"{prefix}.{key}"
        actual_value = actual[key]
        if isinstance(expected_value, Mapping):
            valid, nested_checks, issue, code = _validate_exact_mapping(
                actual_value,
                expected_value,
                path,
                field_class,
                invalid_code,
            )
            checks.extend(nested_checks)
            if not valid:
                return False, checks, issue, code
            continue
        exact = _same_exact_value(actual_value, expected_value)
        checks.append(
            _check(
                f"{field_class.lower()}_{path}",
                field_class,
                path,
                exact,
                invalid_code,
            )
        )
        if not exact:
            return False, checks, path, invalid_code
    return True, checks, None, None


def _control_review(
    supplied_envelope: Any,
) -> tuple[bool, list[dict[str, Any]], str | None, str | None]:
    checks: list[dict[str, Any]] = []
    if not isinstance(supplied_envelope, Mapping):
        checks.append(
            _check(
                "request_mapping",
                "CONTROL",
                "$",
                False,
                "REQUEST_NOT_MAPPING",
            )
        )
        return False, checks, "$", "REQUEST_NOT_MAPPING"

    actual_roots = set(supplied_envelope)
    extras = sorted(actual_roots - EXECUTABLE_ROOT_KEYS)
    if extras:
        issue = extras[0]
        checks.append(
            _check(
                "request_no_unsupported_roots",
                "CONTROL",
                issue,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return False, checks, issue, "UNSUPPORTED_INPUT"

    missing = sorted(EXECUTABLE_ROOT_KEYS - actual_roots)
    if missing:
        issue = missing[0]
        checks.append(
            _check(
                "request_exact_roots",
                "CONTROL",
                issue,
                False,
                "REQUEST_ROOTS_INVALID",
            )
        )
        return False, checks, issue, "REQUEST_ROOTS_INVALID"

    checks.append(_check("request_exact_roots", "CONTROL", "$", True))
    intent_valid = _same_exact_value(
        supplied_envelope["intent"],
        INTENT_RECORD,
    )
    checks.append(
        _check(
            "intent_exact",
            "CONTROL",
            "intent",
            intent_valid,
            "CONTROL_INVALID",
        )
    )
    if not intent_valid:
        return False, checks, "intent", "CONTROL_INVALID"

    question_valid = _same_exact_value(
        supplied_envelope["boundary_question"],
        BOUNDARY_QUESTION,
    )
    checks.append(
        _check(
            "boundary_question_exact",
            "CONTROL",
            "boundary_question",
            question_valid,
            "CONTROL_INVALID",
        )
    )
    if not question_valid:
        return False, checks, "boundary_question", "CONTROL_INVALID"
    return True, checks, None, None


def _ordinary_relation_lapse_basis_review(
    ordinary: Any,
) -> tuple[str, list[dict[str, Any]], tuple[str, ...], str | None, str | None]:
    prefix = "ordinary_relation_lapse_basis"
    checks: list[dict[str, Any]] = []
    if not isinstance(ordinary, Mapping):
        checks.append(
            _check(
                "ordinary_relation_lapse_basis_mapping",
                "ORDINARY_RELATION_LAPSE_BASIS",
                prefix,
                False,
                "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
            )
        )
        return (
            "blocked",
            checks,
            (),
            prefix,
            "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
        )

    expected_keys = set(EXPECTED_ORDINARY_RELATION_LAPSE_BASIS)
    extras = sorted(set(ordinary) - expected_keys)
    if extras:
        issue = f"{prefix}.{extras[0]}"
        checks.append(
            _check(
                "ordinary_relation_lapse_basis_no_unsupported_fields",
                "ORDINARY_RELATION_LAPSE_BASIS",
                issue,
                False,
                "UNSUPPORTED_INPUT",
            )
        )
        return "blocked", checks, (), issue, "UNSUPPORTED_INPUT"

    missing_paths = tuple(
        f"{prefix}.{key}" for key in sorted(expected_keys - set(ordinary))
    )
    checks.append(
        _check(
            "ordinary_relation_lapse_basis_complete",
            "ORDINARY_RELATION_LAPSE_BASIS",
            prefix,
            not missing_paths,
            "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
        )
    )

    issue_path: str | None = None
    for key in EXPECTED_ORDINARY_RELATION_LAPSE_BASIS:
        if key not in ordinary:
            continue
        path = f"{prefix}.{key}"
        exact = _same_exact_value(
            ordinary[key],
            EXPECTED_ORDINARY_RELATION_LAPSE_BASIS[key],
        )
        checks.append(
            _check(
                f"ordinary_relation_lapse_basis_{key}",
                "ORDINARY_RELATION_LAPSE_BASIS",
                path,
                exact,
                "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
            )
        )
        if not exact and issue_path is None:
            issue_path = path

    if issue_path is not None:
        return (
            "blocked",
            checks,
            missing_paths,
            issue_path,
            "ORDINARY_RELATION_LAPSE_BASIS_INVALID",
        )
    if missing_paths:
        return "requires", checks, missing_paths, missing_paths[0], None
    return "allowed", checks, (), None, None


def _event_projection(event_valid: bool, key: str) -> Any:
    if not event_valid:
        return None
    return deepcopy(EXPECTED_CONSTITUTIONAL_EVENT_KEY[key])


def _source_lineage_projection(event_valid: bool, key: str) -> Any:
    if not event_valid:
        return None
    lineage = EXPECTED_CONSTITUTIONAL_EVENT_KEY["source_operation_event_key"][
        "source_boundary_event_key"
    ]["source_operation_event_key"]
    return deepcopy(lineage[key])


def _boundary_result(outcome: str) -> str:
    if outcome == OUTCOME_ALLOWED:
        return RESULT_ALLOWED
    if outcome == OUTCOME_REQUIRES_LAPSE_OPERATION:
        return RESULT_REQUIRES_LAPSE_OPERATION
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
        "source_operation_id": SOURCE_OPERATION_ID,
        "source_boundary_id": SOURCE_BOUNDARY_ID,
        "relation_lapse_id": RELATION_LAPSE_ID,
        "relation_id": RELATION_ID,
        "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
        "topology": TOPOLOGY,
        "presence_boundary_result": _boundary_result(outcome),
        **{field: False for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS},
        **{
            field: False
            for field in PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS
        },
        "presence_evaluation_performed": False,
        "presence_operation_invoked": False,
        "presence_operation_scheduled": False,
        "presence_operation_executed": False,
        "presence_operation_completed": False,
        "automatic_successor_created": False,
    }
    if allowed:
        boundary.update({field: True for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS})
    return boundary


def _boundary_material(outcome: str, event_valid: bool) -> dict[str, Any]:
    allowed = outcome == OUTCOME_ALLOWED
    pair = _source_lineage_projection(event_valid, "pair") or {}
    source_binding = _source_lineage_projection(event_valid, "source") or {}
    return {
        "relation_lapse_operation_reference": {
            "source_operation_id": SOURCE_OPERATION_ID,
            "source_outcome": (
                SOURCE_OUTCOME if allowed else None
            ),
            "source_relation_lapse_result": (
                SOURCE_RELATION_LAPSE_RESULT if allowed else None
            ),
            **{field: allowed for field in POSITIVE_BOUNDARY_BOOLEAN_FIELDS[3:]},
        },
        "relation_record_persistence": {
            "relation_id": RELATION_ID,
            "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
            "topology": TOPOLOGY,
            "relation_record_confirmed_as_historical_only": allowed,
            "relation_occurrence_remains_addressable": event_valid,
            "relation_record_is_living_relation_state": False,
            "relation_created": False,
            "living_relation_state_created": False,
            "retained_relation_state_created": False,
            "relation_dissolved": False,
            "relation_reversed": False,
            "relation_mutated": False,
        },
        "pair_and_source_preservation": {
            "first_crossing_a_id": FIRST_CROSSING_A_ID,
            "first_crossing_b_id": FIRST_CROSSING_B_ID,
            "descendant_body_a_id": DESCENDANT_BODY_A_ID,
            "descendant_body_b_id": DESCENDANT_BODY_B_ID,
            "complete_pair_preserved": pair.get("complete_pair_preserved", False),
            "descendant_bodies_remain_sibling": pair.get(
                "descendant_bodies_remain_sibling", False
            ),
            "descendant_body_non_hierarchy_preserved": pair.get(
                "descendant_body_non_hierarchy_preserved", False
            ),
            "candidate_standing_non_hierarchy_preserved": pair.get(
                "candidate_standing_non_hierarchy_preserved", False
            ),
            "candidate_basis_non_hierarchy_preserved": pair.get(
                "candidate_basis_non_hierarchy_preserved", False
            ),
            "source_semantic_owner": source_binding.get(
                "selected_surface_semantic_owner"
            ),
            "source_semantic_owner_transferred": False,
            "coupling_created": False,
        },
        "presence_boundary_evaluation": {
            "presence_boundary_result": _boundary_result(outcome),
            "presence_operation_consideration_allowed": allowed,
            "presence_supported": False,
            "presence_authorized": False,
            "presence_established": False,
            "presence_recorded": False,
            "presence_evaluation_performed": False,
            "relation_dissolution_authorized": False,
            "relation_dissolution_performed": False,
            "living_relation_state_created": False,
            "identity_created": False,
            "coupling_created": False,
            "field_machinery_created": False,
            "runtime_created": False,
            "api_created": False,
            "currentness_created": False,
            "authority_created": False,
            "standing_created": False,
            "output_authorized": False,
            "action_authorized": False,
            "derivative_reception_authorized": False,
            "synchronization_authorized": False,
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
    missing_lapse_paths: tuple[str, ...] = (),
) -> dict[str, Any]:
    boundary = _boundary_object(outcome)
    failed_check_count = sum(check["passed"] is False for check in checks)
    source_stopping = None
    if event_valid:
        source_stopping = deepcopy(
            EXPECTED_CONSTITUTIONAL_EVENT_KEY["current_lapse_operation_result"][
                "downstream_stopping_point"
            ]
        )
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
        "persistent_presence_boundary_contract": _event_projection(
            event_valid, "target"
        ),
        "current_presence_boundary_event": _event_projection(
            event_valid, "boundary_event"
        ),
        "current_relation_lapse_operation_result_binding": _event_projection(
            event_valid, "current_lapse_operation_result"
        ),
        "persistent_relation_lapse_operation_identity": _event_projection(
            event_valid, "source_operation"
        ),
        "carried_source_operation_event_key": _event_projection(
            event_valid, "source_operation_event_key"
        ),
        "relation_subject": (
            {
                "relation_lapse_id": RELATION_LAPSE_ID,
                "relation_id": RELATION_ID,
                "relation_object_cardinality": RELATION_OBJECT_CARDINALITY,
                "topology": TOPOLOGY,
                "presence_topology": "PER_RELATION_OCCURRENCE",
                "first_crossing_a_id": FIRST_CROSSING_A_ID,
                "first_crossing_b_id": FIRST_CROSSING_B_ID,
                "descendant_body_a_id": DESCENDANT_BODY_A_ID,
                "descendant_body_b_id": DESCENDANT_BODY_B_ID,
                "creation_operation_id": CREATION_OPERATION_ID,
                "creation_operation_request_id": CREATION_OPERATION_REQUEST_ID,
                "source_semantic_owner": SOURCE_SEMANTIC_OWNER,
            }
            if event_valid
            else None
        ),
        "source_stopping_posture": source_stopping,
        "freshness_and_history": (
            {
                "freshness": _event_projection(event_valid, "freshness"),
                "historical_presence_boundary": _event_projection(
                    event_valid, "historical_boundary"
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
                "source_operation": (
                    deepcopy(
                        EXPECTED_CONSTITUTIONAL_EVENT_KEY[
                            "source_operation_event_key"
                        ]["non_claim_attribution"]
                    )
                    if event_valid
                    else None
                ),
            }
            if event_valid
            else None
        ),
        "ordinary_relation_lapse_basis_review": {
            "complete": outcome == OUTCOME_ALLOWED,
            "missing_paths": list(missing_lapse_paths),
            "reviewed_values": (
                deepcopy(EXPECTED_ORDINARY_RELATION_LAPSE_BASIS)
                if outcome == OUTCOME_ALLOWED
                else None
            ),
            "requires_lapse_operation_creates_retry_permission": False,
            "requires_lapse_operation_creates_successor_permission": False,
        },
        "presence_boundary": boundary,
        "presence_boundary_material": _boundary_material(outcome, event_valid),
        "source_relation_boundary_non_claims": {
            key: False
            for key in SOURCE_RELATION_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
        },
        "source_relation_operation_non_claims": {
            key: False
            for key in SOURCE_RELATION_OPERATION_REQUIRED_NON_CLAIM_KEYS
        },
        "source_reversibility_boundary_non_claims": {
            key: False
            for key in SOURCE_REVERSIBILITY_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
        },
        "source_reversibility_operation_non_claims": {
            key: False
            for key in SOURCE_REVERSIBILITY_OPERATION_REQUIRED_NON_CLAIM_KEYS
        },
        "source_lapse_boundary_non_claims": {
            key: False for key in SOURCE_LAPSE_BOUNDARY_REQUIRED_NON_CLAIM_KEYS
        },
        "source_lapse_operation_non_claims": {
            key: False for key in SOURCE_LAPSE_OPERATION_REQUIRED_NON_CLAIM_KEYS
        },
        "presence_boundary_local_non_claims": {
            key: False
            for key in PRESENCE_BOUNDARY_LOCAL_REQUIRED_NON_CLAIM_KEYS
        },
        "presence_boundary_checks": checks,
        "passed_check_count": len(checks) - failed_check_count,
        "failed_check_count": failed_check_count,
        "block": {
            "blocked": outcome == OUTCOME_BLOCKED,
            "code": block_code if outcome == OUTCOME_BLOCKED else None,
            "issue_path": issue_path if outcome == OUTCOME_BLOCKED else None,
            "requires_lapse_operation": (
                outcome == OUTCOME_REQUIRES_LAPSE_OPERATION
            ),
        },
        "downstream_stopping_point": {
            "admissible_future_route": ADMISSIBLE_FUTURE_ROUTE,
            "next_separately_bounded_rank": "PRESENCE_OPERATION",
            "presence_operation_consideration_allowed": (
                outcome == OUTCOME_ALLOWED
            ),
            "presence_operation_invoked": False,
            "presence_operation_authorized": False,
            "presence_operation_scheduled": False,
            "presence_operation_executed": False,
            "presence_operation_completed": False,
            "automatic_successor_created": False,
        },
    }


def resolve_presence_boundary_v0_min_v2(
    supplied_envelope: Any,
) -> dict[str, Any]:
    """Resolve one exact current Presence-boundary event without I/O."""

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

    request = deepcopy(dict(supplied_envelope))
    event_valid, event_checks, event_issue, event_code = _validate_exact_mapping(
        request["constitutional_event_key"],
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
            block_code=event_code,
            issue_path=event_issue,
        )

    non_claims_valid, non_claim_checks, non_claim_issue, non_claim_code = (
        _validate_exact_mapping(
            request["required_non_claims"],
            EXPECTED_REQUIRED_NON_CLAIMS,
            "required_non_claims",
            "REQUIRED_NON_CLAIM",
            "REQUIRED_NON_CLAIM_INVALID",
        )
    )
    checks.extend(non_claim_checks)
    if not non_claims_valid:
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=non_claim_code,
            issue_path=non_claim_issue,
        )

    basis_state, basis_checks, missing_paths, basis_issue, basis_code = (
        _ordinary_relation_lapse_basis_review(
            request["ordinary_relation_lapse_basis"]
        )
    )
    checks.extend(basis_checks)
    if basis_state == "blocked":
        return _build_result(
            OUTCOME_BLOCKED,
            checks,
            event_valid=True,
            block_code=basis_code,
            issue_path=basis_issue,
            missing_lapse_paths=missing_paths,
        )
    if basis_state == "requires":
        return _build_result(
            OUTCOME_REQUIRES_LAPSE_OPERATION,
            checks,
            event_valid=True,
            missing_lapse_paths=missing_paths,
        )

    checks.extend(
        (
            _check(
                "boundary_result_exact",
                "BOUNDARY_RESULT",
                "presence_boundary.presence_boundary_result",
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
