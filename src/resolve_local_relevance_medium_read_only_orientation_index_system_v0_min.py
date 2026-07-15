"""Resolve one local relevance medium read-only orientation index system.

This module records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX from
one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET artifact. It indexes the
already-standing first and second local orientation locator entries for
deterministic local lookup only. It does not accept new entries or signals, does
not discover artifacts, and does not create registry, search, ranking, scoring,
priority, validity, truth, authority, currentness, runtime, API, distributed
behavior, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumReadOnlyOrientationIndexSystemV0MinError(Exception):
    """Bounded resolver error for read-only orientation index system handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_orientation_index_system_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min"
)

DEFAULT_READ_ONLY_STATE_PACKET_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min/"
    "local_relevance_medium_read_only_state_packet_reference_review_001__"
    "local_relevance_medium_read_only_state_reader_v0_min_result.json"
)

DEFAULT_ORIENTATION_INDEX_ID = "local_relevance_medium_read_only_orientation_index_001"
DEFAULT_ORIENTATION_INDEX_SYSTEM_ID = (
    "local_relevance_medium_read_only_orientation_index_system_001"
)

ORIENTATION_INDEX_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX"
ORIENTATION_INDEX_SYSTEM_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
)
ORIENTATION_INDEX_SCOPE = (
    "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY"
)

SUPPORTED_ORIENTATION_INDEX_TYPE_VALUES = (ORIENTATION_INDEX_TYPE,)
SUPPORTED_ORIENTATION_INDEX_SYSTEM_TYPE_VALUES = (ORIENTATION_INDEX_SYSTEM_TYPE,)
SUPPORTED_ORIENTATION_INDEX_SCOPE_VALUES = (ORIENTATION_INDEX_SCOPE,)

LOOKUP_ORDER = ["first_orientation_locator", "second_orientation_locator"]

STATE_PACKET_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET"
STATE_READER_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
STATE_READER_SCOPE = "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY"
STATE_READER_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED"
)

RECORD_INTENT = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
)
DO_NOT_RECORD_INTENT = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
)
BLOCK_INTENT = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
)
SUPPORTED_INTENTS = (RECORD_INTENT, DO_NOT_RECORD_INTENT, BLOCK_INTENT)

FIRST_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_001"
SECOND_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_002"
FIRST_RELEVANCE_BASIS_ID = "bounded_relevance_basis_001"
SECOND_RELEVANCE_BASIS_ID = "bounded_relevance_basis_002"
FIRST_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_001"
SECOND_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_002"
FIRST_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_001"
SECOND_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_002"
FIRST_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_001"
SECOND_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_002"

KNOWN_ARTIFACT_CHAIN = [
    "bounded_relevance_reception",
    "bounded_relevance_receipt_v2",
    "relevance_orientation_view",
    "local_relevance_orientation_index_entry",
    "local_relevance_medium_successor_reception_request",
    "local_relevance_medium_successor_candidate_admission",
    "local_relevance_medium_second_bounded_relevance_reception",
    "local_relevance_medium_second_bounded_relevance_receipt",
    "local_relevance_medium_second_relevance_orientation_view",
    "local_relevance_medium_second_local_relevance_orientation_index_entry",
    "local_relevance_medium_multiplicity_result",
    "local_relevance_medium_relation_view",
    "local_relevance_medium_comparison_view",
]

FIRST_LOCATOR_CHAIN_KEY = "local_relevance_orientation_index_entry"
SECOND_LOCATOR_CHAIN_KEY = (
    "local_relevance_medium_second_local_relevance_orientation_index_entry"
)
FIRST_ORIENTATION_VIEW_CHAIN_KEY = "relevance_orientation_view"
SECOND_ORIENTATION_VIEW_CHAIN_KEY = (
    "local_relevance_medium_second_relevance_orientation_view"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "new_signal_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "source_created",
    "authority_created",
    "currentness_created",
    "truth_created",
    "action_created",
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "deployment_created",
    "public_release_created",
    "operation_permission_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "follow_on_work_authorized",
    "artifact_existence_treated_as_read_only_orientation_index_authority",
    "latest_file_posture_treated_as_read_only_orientation_index_authority",
    "repo_local_availability_treated_as_read_only_orientation_index_authority",
    "hidden_repo_state_used_as_read_only_orientation_index_content",
    "hidden_repo_state_used_as_read_only_orientation_index_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_orientation_index_recorded",
    "local_relevance_medium_read_only_orientation_index_system_recorded",
    "basis_read_only_state_packet_artifact_preserved",
    "known_artifact_chain_preserved",
    "first_orientation_locator_entry_artifact_preserved",
    "second_orientation_locator_entry_artifact_preserved",
    "first_orientation_view_artifact_preserved",
    "second_orientation_view_artifact_preserved",
    "first_received_signal_id_preserved",
    "second_received_signal_id_preserved",
    "first_and_second_signals_distinct",
    "first_relevance_basis_id_preserved",
    "second_relevance_basis_id_preserved",
    "first_relevance_scope_id_preserved",
    "second_relevance_scope_id_preserved",
    "first_carrier_context_id_preserved",
    "second_carrier_context_id_preserved",
    "first_reception_envelope_id_preserved",
    "second_reception_envelope_id_preserved",
    "multiplicity_count_is_two",
    "relation_pair_count_is_one",
    "comparison_pair_count_is_one",
    "comparison_readability_stands",
    "relation_readability_stands",
    "multiplicity_result_stands",
    "two_local_orientation_objects_stand",
    "lookup_table_has_two_entries",
    "lookup_order_is_deterministic",
    "lookup_key_count_is_two",
    "lookup_target_count_is_two",
    "accepted_new_entries_count_is_zero",
    "deterministic_local_lookup_enabled",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    "FIRST_ORIENTATION_LOCATOR_ARTIFACT_MISSING",
    "SECOND_ORIENTATION_LOCATOR_ARTIFACT_MISSING",
    "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "FIRST_RECEIVED_SIGNAL_ID_MISSING",
    "SECOND_RECEIVED_SIGNAL_ID_MISSING",
    "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
    "FIRST_RELEVANCE_BASIS_ID_MISSING",
    "SECOND_RELEVANCE_BASIS_ID_MISSING",
    "FIRST_RELEVANCE_SCOPE_ID_MISSING",
    "SECOND_RELEVANCE_SCOPE_ID_MISSING",
    "FIRST_CARRIER_CONTEXT_ID_MISSING",
    "SECOND_CARRIER_CONTEXT_ID_MISSING",
    "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
    "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
    "MULTIPLICITY_COUNT_NOT_TWO",
    "RELATION_PAIR_COUNT_NOT_ONE",
    "COMPARISON_PAIR_COUNT_NOT_ONE",
    "COMPARISON_READABILITY_DOES_NOT_STAND",
    "RELATION_READABILITY_DOES_NOT_STAND",
    "MULTIPLICITY_RESULT_DOES_NOT_STAND",
    "TWO_LOCAL_ORIENTATION_OBJECTS_DO_NOT_STAND",
    "ORIENTATION_INDEX_TYPE_MISSING",
    "ORIENTATION_INDEX_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
    "ORIENTATION_INDEX_SYSTEM_TYPE_MISSING",
    "ORIENTATION_INDEX_SYSTEM_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
    "ORIENTATION_INDEX_SCOPE_MISSING",
    "ORIENTATION_INDEX_SCOPE_NOT_READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
    "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "LOOKUP_KEY_COUNT_NOT_TWO",
    "LOOKUP_TARGET_COUNT_NOT_TWO",
    "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "DETERMINISTIC_LOCAL_LOOKUP_NOT_ENABLED",
    "NEW_SIGNAL_ACCEPTED",
    "NEW_RELEVANCE_OBJECT_CREATED",
    "NEW_INDEX_ENTRY_CREATED",
    "FILESYSTEM_DISCOVERY_PERFORMED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
    "SCORING_SURFACE_CREATED",
    "PRIORITY_SURFACE_CREATED",
    "VALIDITY_JUDGMENT_CREATED",
    "TRUTH_JUDGMENT_CREATED",
    "AUTHORITY_JUDGMENT_CREATED",
    "CURRENTNESS_JUDGMENT_CREATED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "SOURCE_CREATED",
    "AUTHORITY_CREATED",
    "CURRENTNESS_CREATED",
    "TRUTH_CREATED",
    "ACTION_CREATED",
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "OPERATION_PERMISSION_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_ORIENTATION_INDEX_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_UNREADABLE",
)

REQUEST_SHORTCUT_FAILURES = {
    "selected_read_only_state_packet_artifact_missing": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_PATH_MISSING"
    ),
    "selected_read_only_state_reader_artifact_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED"
    ),
    "selected_read_only_state_reader_artifact_failed_checks_present": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "selected_read_only_state_reader_artifact_version_not_0_1_0": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "local_relevance_medium_read_only_state_packet_object_missing": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_OBJECT_MISSING"
    ),
    "state_packet_type_not_local_relevance_medium_read_only_state_packet": (
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET"
    ),
    "state_reader_type_not_local_relevance_medium_read_only_state_reader": (
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
    ),
    "state_reader_scope_not_read_existing_local_relevance_medium_state_only": (
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY"
    ),
    "known_artifact_chain_not_canonical": "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    "first_orientation_locator_artifact_missing": (
        "FIRST_ORIENTATION_LOCATOR_ARTIFACT_MISSING"
    ),
    "second_orientation_locator_artifact_missing": (
        "SECOND_ORIENTATION_LOCATOR_ARTIFACT_MISSING"
    ),
    "first_orientation_view_artifact_missing": (
        "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING"
    ),
    "second_orientation_view_artifact_missing": (
        "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING"
    ),
    "first_received_signal_id_missing": "FIRST_RECEIVED_SIGNAL_ID_MISSING",
    "second_received_signal_id_missing": "SECOND_RECEIVED_SIGNAL_ID_MISSING",
    "first_and_second_received_signal_ids_not_distinct": (
        "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT"
    ),
    "first_relevance_basis_id_missing": "FIRST_RELEVANCE_BASIS_ID_MISSING",
    "second_relevance_basis_id_missing": "SECOND_RELEVANCE_BASIS_ID_MISSING",
    "first_relevance_scope_id_missing": "FIRST_RELEVANCE_SCOPE_ID_MISSING",
    "second_relevance_scope_id_missing": "SECOND_RELEVANCE_SCOPE_ID_MISSING",
    "first_carrier_context_id_missing": "FIRST_CARRIER_CONTEXT_ID_MISSING",
    "second_carrier_context_id_missing": "SECOND_CARRIER_CONTEXT_ID_MISSING",
    "first_reception_envelope_id_missing": "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
    "second_reception_envelope_id_missing": (
        "SECOND_RECEPTION_ENVELOPE_ID_MISSING"
    ),
    "multiplicity_count_not_two": "MULTIPLICITY_COUNT_NOT_TWO",
    "relation_pair_count_not_one": "RELATION_PAIR_COUNT_NOT_ONE",
    "comparison_pair_count_not_one": "COMPARISON_PAIR_COUNT_NOT_ONE",
    "comparison_readability_does_not_stand": (
        "COMPARISON_READABILITY_DOES_NOT_STAND"
    ),
    "relation_readability_does_not_stand": "RELATION_READABILITY_DOES_NOT_STAND",
    "multiplicity_result_does_not_stand": "MULTIPLICITY_RESULT_DOES_NOT_STAND",
    "two_local_orientation_objects_do_not_stand": (
        "TWO_LOCAL_ORIENTATION_OBJECTS_DO_NOT_STAND"
    ),
    "orientation_index_type_not_local_relevance_medium_read_only_orientation_index": (
        "ORIENTATION_INDEX_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX"
    ),
    "orientation_index_system_type_not_local_relevance_medium_read_only_orientation_index_system": (
        "ORIENTATION_INDEX_SYSTEM_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
    ),
    "orientation_index_scope_not_read_only_two_orientation_locators_deterministic_lookup_only": (
        "ORIENTATION_INDEX_SCOPE_NOT_READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY"
    ),
    "lookup_table_not_two_entries": "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "lookup_order_not_deterministic": "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "lookup_key_count_not_two": "LOOKUP_KEY_COUNT_NOT_TWO",
    "lookup_target_count_not_two": "LOOKUP_TARGET_COUNT_NOT_TWO",
    "accepted_new_entries_count_not_zero": "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "deterministic_local_lookup_not_enabled": (
        "DETERMINISTIC_LOCAL_LOOKUP_NOT_ENABLED"
    ),
    "new_signal_accepted": "NEW_SIGNAL_ACCEPTED",
    "new_relevance_object_created": "NEW_RELEVANCE_OBJECT_CREATED",
    "new_index_entry_created": "NEW_INDEX_ENTRY_CREATED",
    "filesystem_discovery_performed": "FILESYSTEM_DISCOVERY_PERFORMED",
    "registry_created": "REGISTRY_CREATED",
    "search_surface_created": "SEARCH_SURFACE_CREATED",
    "ranking_surface_created": "RANKING_SURFACE_CREATED",
    "scoring_surface_created": "SCORING_SURFACE_CREATED",
    "priority_surface_created": "PRIORITY_SURFACE_CREATED",
    "validity_judgment_created": "VALIDITY_JUDGMENT_CREATED",
    "truth_judgment_created": "TRUTH_JUDGMENT_CREATED",
    "authority_judgment_created": "AUTHORITY_JUDGMENT_CREATED",
    "currentness_judgment_created": "CURRENTNESS_JUDGMENT_CREATED",
    "repeated_reception_permission_created": (
        "REPEATED_RECEPTION_PERMISSION_CREATED"
    ),
    "arbitrary_reception_created": "ARBITRARY_RECEPTION_CREATED",
    "feed_created": "FEED_CREATED",
    "source_transfer_occurred": "SOURCE_TRANSFER_OCCURRED",
    "source_receipt_occurred": "SOURCE_RECEIPT_OCCURRED",
    "source_created": "SOURCE_CREATED",
    "authority_created": "AUTHORITY_CREATED",
    "currentness_created": "CURRENTNESS_CREATED",
    "truth_created": "TRUTH_CREATED",
    "action_created": "ACTION_CREATED",
    "synchronization_created": "SYNCHRONIZATION_CREATED",
    "participation_authorized": "PARTICIPATION_AUTHORIZED",
    "participant_role_created": "PARTICIPANT_ROLE_CREATED",
    "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_read_only_orientation_index_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY"
    ),
    "latest_file_posture_treated_as_read_only_orientation_index_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY"
    ),
    "repo_local_availability_treated_as_read_only_orientation_index_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY"
    ),
    "hidden_repo_state_used_as_read_only_orientation_index_content": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_ORIENTATION_INDEX_CONTENT"
    ),
    "hidden_repo_state_used_as_read_only_orientation_index_authority": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY"
    ),
    "predecessor_failure_repaired": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "predecessor_failure_hidden": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
}

FALSE_POSTURE_TO_BLOCK_CODE = {
    key: code
    for key, code in REQUEST_SHORTCUT_FAILURES.items()
    if key in REQUIRED_FALSE_NON_CLAIMS
}
FALSE_POSTURE_TO_BLOCK_CODE.update(
    {
        "prior_artifacts_mutated": (
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
        ),
        "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
        "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    }
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_orientation_index_system_body",
    "raw_orientation_index_body",
    "raw_state_reader_body",
    "raw_state_packet_body",
    "raw_comparison_view_body",
    "raw_relation_view_body",
    "raw_multiplicity_result_body",
    "raw_first_local_index_entry_body",
    "raw_second_local_index_entry_body",
    "raw_first_orientation_body",
    "raw_second_orientation_body",
    "raw_first_receipt_body",
    "raw_second_receipt_body",
    "raw_first_reception_body",
    "raw_second_reception_body",
    "raw_successor_candidate_admission_body",
    "raw_successor_reception_request_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "orientation_index_system_body",
    "orientation_index_body",
    "state_reader_body",
    "state_packet_body",
    "comparison_view_body",
    "relation_view_body",
    "multiplicity_result_body",
    "first_local_index_entry_body",
    "second_local_index_entry_body",
    "first_orientation_body",
    "second_orientation_body",
    "first_receipt_body",
    "second_receipt_body",
    "first_reception_body",
    "second_reception_body",
    "successor_candidate_admission_body",
    "successor_reception_request_body",
    "source_body",
    "authority_body",
    "currentness_body",
    "action_body",
    "synchronization_body",
    "public_api_body",
    "participant_facing_interface_body",
    "distributed_network_behavior_body",
    "hidden_repo_state",
    "current_working_tree",
    "local_cache",
    "repo_local_only_dependency",
}

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_SYSTEM_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_INDEX_BODY_MUST_NOT_RETURN",
    "RAW_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_RELATION_VIEW_BODY_MUST_NOT_RETURN",
    "RAW_MULTIPLICITY_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOCAL_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_ACTION_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_STRINGS = set(BLOCK_CODES) | set(OUTCOME_FAMILY) | {
    RESULT_VERSION,
    RESOLVER_MODULE,
    ORIENTATION_INDEX_TYPE,
    ORIENTATION_INDEX_SYSTEM_TYPE,
    ORIENTATION_INDEX_SCOPE,
    STATE_PACKET_TYPE,
    STATE_READER_TYPE,
    STATE_READER_SCOPE,
    STATE_READER_RECORDED_OUTCOME,
    RECORD_INTENT,
    DO_NOT_RECORD_INTENT,
    BLOCK_INTENT,
    FIRST_RECEIVED_SIGNAL_ID,
    SECOND_RECEIVED_SIGNAL_ID,
    FIRST_RELEVANCE_BASIS_ID,
    SECOND_RELEVANCE_BASIS_ID,
    FIRST_RELEVANCE_SCOPE_ID,
    SECOND_RELEVANCE_SCOPE_ID,
    FIRST_CARRIER_CONTEXT_ID,
    SECOND_CARRIER_CONTEXT_ID,
    FIRST_RECEPTION_ENVELOPE_ID,
    SECOND_RECEPTION_ENVELOPE_ID,
    *LOOKUP_ORDER,
    *KNOWN_ARTIFACT_CHAIN,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    lowered = key.lower()
    return lowered in SENSITIVE_CONTENT_KEYS or lowered.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_RAW_CONTENT]"
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[REDACTED_RAW_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return value


def _string_or_empty(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, Path):
        return str(value)
    return ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def _safe_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    check: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed and code:
        public_code = code if code in BLOCK_CODES else (
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_MALFORMED"
        )
        check["block_code"] = public_code
        check["failure_code"] = public_code
    return check


def _append_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(
        _make_check(check_name, passed, expected_posture, actual_posture, code)
    )


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is False)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code in BLOCK_CODES:
                return code
    return None


def _read_json_object(
    path_value: Any,
) -> tuple[dict[str, Any], str | None]:
    path_text = _string_or_empty(path_value)
    if not _present(path_text):
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_PATH_MISSING"
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_UNREADABLE"
    if not isinstance(data, Mapping):
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_NOT_JSON_OBJECT"
    return dict(data), None


def _artifact_metadata(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    metadata = artifact.get(
        "local_relevance_medium_read_only_state_reader_metadata"
    )
    if isinstance(metadata, Mapping):
        return metadata
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_metadata") and isinstance(value, Mapping):
            return value
    return {}


def _artifact_summary(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = artifact.get("local_relevance_medium_read_only_state_reader_summary")
    if isinstance(summary, Mapping):
        return summary
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_summary") and isinstance(value, Mapping):
            return value
    return {}


def _artifact_result_version(artifact: Mapping[str, Any]) -> str | None:
    for source in (artifact, _artifact_metadata(artifact), _artifact_summary(artifact)):
        value = source.get("result_version")
        if isinstance(value, str):
            return value
    packet = artifact.get("local_relevance_medium_read_only_state_packet")
    if isinstance(packet, Mapping):
        value = packet.get("state_packet_version")
        if isinstance(value, str):
            return value
    return None


def _artifact_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    for source in (artifact, _artifact_metadata(artifact), _artifact_summary(artifact)):
        value = _safe_int(source.get("failed_check_count"))
        if value is not None:
            return value
    checks = artifact.get("local_relevance_medium_read_only_state_reader_checks")
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is False
        )
    return None


def _state_packet_from_artifact(
    artifact: Mapping[str, Any],
) -> Mapping[str, Any]:
    packet = artifact.get("local_relevance_medium_read_only_state_packet")
    if isinstance(packet, Mapping):
        return packet
    return {}


def _standing_artifacts_from_packet(packet: Mapping[str, Any]) -> Mapping[str, Any]:
    artifacts = packet.get("validated_standing_artifacts")
    if isinstance(artifacts, Mapping):
        return artifacts
    return {}


def _artifact_path_for(packet: Mapping[str, Any], chain_key: str) -> str:
    artifacts = _standing_artifacts_from_packet(packet)
    value = artifacts.get(chain_key)
    return _string_or_empty(value)


def _empty_basis(path_value: Any = "") -> dict[str, Any]:
    return {
        "artifact_path": _string_or_empty(path_value),
        "artifact": {},
        "read_error_code": None,
        "outcome": None,
        "result_version": None,
        "failed_check_count": None,
        "state_packet": {},
    }


def _extract_state_packet_basis(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    path_text = _string_or_empty(
        declared.get("selected_local_relevance_medium_read_only_state_packet_artifact")
    )
    _append_check(
        checks,
        "selected read-only state packet artifact path declared",
        _present(path_text),
        "declared selected read-only state packet artifact path",
        path_text,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_ARTIFACT_PATH_MISSING",
    )
    artifact, read_error = _read_json_object(path_text)
    if read_error:
        _append_check(
            checks,
            "selected read-only state packet artifact readable JSON object",
            False,
            "readable JSON object",
            read_error,
            read_error,
        )
        basis = _empty_basis(path_text)
        basis["read_error_code"] = read_error
        return basis
    _append_check(
        checks,
        "selected read-only state packet artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )
    return {
        "artifact_path": path_text,
        "artifact": artifact,
        "read_error_code": None,
        "outcome": artifact.get("outcome"),
        "result_version": _artifact_result_version(artifact),
        "failed_check_count": _artifact_failed_check_count(artifact),
        "state_packet": _state_packet_from_artifact(artifact),
    }


def _validate_declared_non_claims(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not isinstance(declared_non_claims, Mapping):
        _append_check(
            checks,
            "declared required false non-claims mapping present",
            False,
            "mapping with all required false non-claims",
            type(declared_non_claims).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    _append_check(
        checks,
        "declared required false non-claims mapping present",
        True,
        "mapping with all required false non-claims",
        "mapping",
    )
    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_non_claims.get(key)
        _append_check(
            checks,
            f"declared non-claim {key} is canonical false",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_declared_request(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get(
        "local_relevance_medium_read_only_orientation_index_system_question"
    )
    _append_check(
        checks,
        "read-only orientation index system question declared",
        _present(question),
        "declared read-only orientation index system question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_QUESTION_UNDECLARED",
    )

    intent = declared.get(
        "local_relevance_medium_read_only_orientation_index_system_intent"
    )
    _append_check(
        checks,
        "read-only orientation index system intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_INTENT_UNSUPPORTED",
    )
    _append_check(
        checks,
        "read-only orientation index system block intent not requested",
        intent != BLOCK_INTENT,
        f"not {BLOCK_INTENT}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_BLOCK_REQUESTED",
    )

    orientation_index_type = declared.get("orientation_index_type")
    _append_check(
        checks,
        "orientation index type declared",
        _present(orientation_index_type),
        ORIENTATION_INDEX_TYPE,
        orientation_index_type,
        "ORIENTATION_INDEX_TYPE_MISSING",
    )
    if _present(orientation_index_type):
        _append_check(
            checks,
            "orientation index type is local relevance medium read-only orientation index",
            orientation_index_type == ORIENTATION_INDEX_TYPE,
            ORIENTATION_INDEX_TYPE,
            orientation_index_type,
            "ORIENTATION_INDEX_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
        )

    orientation_index_system_type = declared.get("orientation_index_system_type")
    _append_check(
        checks,
        "orientation index system type declared",
        _present(orientation_index_system_type),
        ORIENTATION_INDEX_SYSTEM_TYPE,
        orientation_index_system_type,
        "ORIENTATION_INDEX_SYSTEM_TYPE_MISSING",
    )
    if _present(orientation_index_system_type):
        _append_check(
            checks,
            "orientation index system type is local relevance medium read-only orientation index system",
            orientation_index_system_type == ORIENTATION_INDEX_SYSTEM_TYPE,
            ORIENTATION_INDEX_SYSTEM_TYPE,
            orientation_index_system_type,
            "ORIENTATION_INDEX_SYSTEM_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
        )

    orientation_index_scope = declared.get("orientation_index_scope")
    _append_check(
        checks,
        "orientation index scope declared",
        _present(orientation_index_scope),
        ORIENTATION_INDEX_SCOPE,
        orientation_index_scope,
        "ORIENTATION_INDEX_SCOPE_MISSING",
    )
    if _present(orientation_index_scope):
        _append_check(
            checks,
            "orientation index scope is read-only deterministic lookup only",
            orientation_index_scope == ORIENTATION_INDEX_SCOPE,
            ORIENTATION_INDEX_SCOPE,
            orientation_index_scope,
            "ORIENTATION_INDEX_SCOPE_NOT_READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
        )

    declared_lookup_order = declared.get("lookup_order")
    _append_check(
        checks,
        "lookup order deterministic",
        declared_lookup_order == LOOKUP_ORDER,
        LOOKUP_ORDER,
        declared_lookup_order,
        "LOOKUP_ORDER_NOT_DETERMINISTIC",
    )

    _append_check(
        checks,
        "lookup key count exactly two",
        declared.get("lookup_key_count", 2) == 2,
        2,
        declared.get("lookup_key_count", 2),
        "LOOKUP_KEY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "lookup target count exactly two",
        declared.get("lookup_target_count", 2) == 2,
        2,
        declared.get("lookup_target_count", 2),
        "LOOKUP_TARGET_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "accepted new entries count zero",
        declared.get("accepted_new_entries_count", 0) == 0,
        0,
        declared.get("accepted_new_entries_count", 0),
        "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    )
    _append_check(
        checks,
        "deterministic local lookup enabled",
        declared.get("deterministic_local_lookup_enabled", True) is True,
        True,
        declared.get("deterministic_local_lookup_enabled", True),
        "DETERMINISTIC_LOCAL_LOOKUP_NOT_ENABLED",
    )

    for key, code in REQUEST_SHORTCUT_FAILURES.items():
        value = declared.get(key, False)
        _append_check(checks, f"shortcut {key} not asserted", value is False, False, value, code)

    _validate_declared_non_claims(declared, checks)


def _validate_state_reader_artifact(
    basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "selected read-only state reader artifact outcome recorded",
        basis.get("outcome") == STATE_READER_RECORDED_OUTCOME,
        STATE_READER_RECORDED_OUTCOME,
        basis.get("outcome"),
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "selected read-only state reader artifact result version is 0.1.0",
        basis.get("result_version") == RESULT_VERSION,
        RESULT_VERSION,
        basis.get("result_version"),
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "selected read-only state reader artifact failed check count zero",
        basis.get("failed_check_count") == 0,
        0,
        basis.get("failed_check_count"),
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    packet = basis.get("state_packet")
    _append_check(
        checks,
        "local relevance medium read-only state packet object present",
        isinstance(packet, Mapping) and bool(packet),
        "local relevance medium read-only state packet object",
        type(packet).__name__ if not isinstance(packet, Mapping) else "mapping",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_OBJECT_MISSING",
    )


def _validate_state_packet(
    packet: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "state packet type exact",
        packet.get("state_packet_type") == STATE_PACKET_TYPE,
        STATE_PACKET_TYPE,
        packet.get("state_packet_type"),
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    )
    _append_check(
        checks,
        "state reader type exact",
        packet.get("state_reader_type") == STATE_READER_TYPE,
        STATE_READER_TYPE,
        packet.get("state_reader_type"),
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    )
    _append_check(
        checks,
        "state reader scope read existing local relevance medium state only",
        packet.get("state_reader_scope") == STATE_READER_SCOPE,
        STATE_READER_SCOPE,
        packet.get("state_reader_scope"),
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    )
    _append_check(
        checks,
        "known artifact chain canonical",
        packet.get("known_artifact_chain") == KNOWN_ARTIFACT_CHAIN,
        KNOWN_ARTIFACT_CHAIN,
        packet.get("known_artifact_chain"),
        "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    )

    required_paths = (
        (
            FIRST_LOCATOR_CHAIN_KEY,
            "first orientation locator artifact preserved",
            "FIRST_ORIENTATION_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            SECOND_LOCATOR_CHAIN_KEY,
            "second orientation locator artifact preserved",
            "SECOND_ORIENTATION_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            FIRST_ORIENTATION_VIEW_CHAIN_KEY,
            "first orientation view artifact preserved",
            "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            SECOND_ORIENTATION_VIEW_CHAIN_KEY,
            "second orientation view artifact preserved",
            "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
    )
    for chain_key, check_name, code in required_paths:
        path_text = _artifact_path_for(packet, chain_key)
        _append_check(checks, check_name, _present(path_text), "preserved artifact path", path_text, code)

    expected_identifiers = (
        ("first_received_signal_id", FIRST_RECEIVED_SIGNAL_ID, "FIRST_RECEIVED_SIGNAL_ID_MISSING"),
        ("second_received_signal_id", SECOND_RECEIVED_SIGNAL_ID, "SECOND_RECEIVED_SIGNAL_ID_MISSING"),
        ("first_relevance_basis_id", FIRST_RELEVANCE_BASIS_ID, "FIRST_RELEVANCE_BASIS_ID_MISSING"),
        ("second_relevance_basis_id", SECOND_RELEVANCE_BASIS_ID, "SECOND_RELEVANCE_BASIS_ID_MISSING"),
        ("first_relevance_scope_id", FIRST_RELEVANCE_SCOPE_ID, "FIRST_RELEVANCE_SCOPE_ID_MISSING"),
        ("second_relevance_scope_id", SECOND_RELEVANCE_SCOPE_ID, "SECOND_RELEVANCE_SCOPE_ID_MISSING"),
        ("first_carrier_context_id", FIRST_CARRIER_CONTEXT_ID, "FIRST_CARRIER_CONTEXT_ID_MISSING"),
        ("second_carrier_context_id", SECOND_CARRIER_CONTEXT_ID, "SECOND_CARRIER_CONTEXT_ID_MISSING"),
        ("first_reception_envelope_id", FIRST_RECEPTION_ENVELOPE_ID, "FIRST_RECEPTION_ENVELOPE_ID_MISSING"),
        ("second_reception_envelope_id", SECOND_RECEPTION_ENVELOPE_ID, "SECOND_RECEPTION_ENVELOPE_ID_MISSING"),
    )
    for key, expected, code in expected_identifiers:
        actual = packet.get(key)
        _append_check(checks, f"{key} preserved", actual == expected, expected, actual, code)

    _append_check(
        checks,
        "first and second received signal ids distinct",
        packet.get("first_received_signal_id") != packet.get("second_received_signal_id")
        and _present(packet.get("first_received_signal_id"))
        and _present(packet.get("second_received_signal_id")),
        "distinct first and second received signal ids",
        {
            "first_received_signal_id": packet.get("first_received_signal_id"),
            "second_received_signal_id": packet.get("second_received_signal_id"),
        },
        "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
    )

    expected_counts = (
        ("multiplicity_count", 2, "MULTIPLICITY_COUNT_NOT_TWO"),
        ("relation_pair_count", 1, "RELATION_PAIR_COUNT_NOT_ONE"),
        ("comparison_pair_count", 1, "COMPARISON_PAIR_COUNT_NOT_ONE"),
    )
    for key, expected, code in expected_counts:
        actual = packet.get(key)
        _append_check(checks, f"{key} exact", actual == expected, expected, actual, code)

    expected_true = (
        ("comparison_readability_stands", "COMPARISON_READABILITY_DOES_NOT_STAND"),
        ("relation_readability_stands", "RELATION_READABILITY_DOES_NOT_STAND"),
        ("multiplicity_result_stands", "MULTIPLICITY_RESULT_DOES_NOT_STAND"),
        ("two_local_orientation_objects_stand", "TWO_LOCAL_ORIENTATION_OBJECTS_DO_NOT_STAND"),
    )
    for key, code in expected_true:
        actual = packet.get(key)
        _append_check(checks, f"{key} preserved true", actual is True, True, actual, code)


def _validate_false_postures(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key, code in FALSE_POSTURE_TO_BLOCK_CODE.items():
        value = declared.get(key, False)
        _append_check(checks, f"{key} not created or asserted", value is False, False, value, code)

    _append_check(
        checks,
        "artifact existence not read-only-orientation-index authority",
        declared.get(
            "artifact_existence_treated_as_read_only_orientation_index_authority",
            False,
        )
        is False,
        False,
        declared.get(
            "artifact_existence_treated_as_read_only_orientation_index_authority",
            False,
        ),
        "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    )
    _append_check(
        checks,
        "latest file posture not read-only-orientation-index authority",
        declared.get("latest_file_posture_treated_as_read_only_orientation_index_authority", False)
        is False,
        False,
        declared.get("latest_file_posture_treated_as_read_only_orientation_index_authority", False),
        "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    )
    _append_check(
        checks,
        "repo-local availability not read-only-orientation-index authority",
        declared.get("repo_local_availability_treated_as_read_only_orientation_index_authority", False)
        is False,
        False,
        declared.get("repo_local_availability_treated_as_read_only_orientation_index_authority", False),
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_ORIENTATION_INDEX_AUTHORITY",
    )
    _append_check(
        checks,
        "hidden repo state not read-only-orientation-index content or authority",
        declared.get("hidden_repo_state_used_as_read_only_orientation_index_content", False)
        is False
        and declared.get("hidden_repo_state_used_as_read_only_orientation_index_authority", False)
        is False,
        "hidden repo state excluded",
        {
            "hidden_repo_state_used_as_read_only_orientation_index_content": declared.get(
                "hidden_repo_state_used_as_read_only_orientation_index_content",
                False,
            ),
            "hidden_repo_state_used_as_read_only_orientation_index_authority": declared.get(
                "hidden_repo_state_used_as_read_only_orientation_index_authority",
                False,
            ),
        },
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_ORIENTATION_INDEX_CONTENT",
    )
    _append_check(
        checks,
        "predecessor failure evidence preserved",
        declared.get("predecessor_failure_repaired", False) is False
        and declared.get("predecessor_failure_hidden", False) is False
        and declared.get("predecessor_failure_claimed_passed", False) is False,
        "predecessor failure evidence preserved",
        {
            "predecessor_failure_repaired": declared.get("predecessor_failure_repaired", False),
            "predecessor_failure_hidden": declared.get("predecessor_failure_hidden", False),
            "predecessor_failure_claimed_passed": declared.get("predecessor_failure_claimed_passed", False),
        },
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    )
    _append_check(
        checks,
        "result-level required false non-claims canonical false",
        all(value is False for value in _canonical_non_claims().values()),
        "all result non-claims false",
        _canonical_non_claims(),
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def _validate_constructed_lookup_posture(
    packet: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    lookup_table = _build_lookup_table(packet)
    _append_check(
        checks,
        "lookup table has exactly two entries",
        set(lookup_table.keys()) == set(LOOKUP_ORDER) and len(lookup_table) == 2,
        LOOKUP_ORDER,
        list(lookup_table.keys()),
        "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    )
    _append_check(
        checks,
        "lookup order is deterministic",
        LOOKUP_ORDER == ["first_orientation_locator", "second_orientation_locator"],
        ["first_orientation_locator", "second_orientation_locator"],
        LOOKUP_ORDER,
        "LOOKUP_ORDER_NOT_DETERMINISTIC",
    )
    _append_check(
        checks,
        "lookup key count is two",
        len(LOOKUP_ORDER) == 2,
        2,
        len(LOOKUP_ORDER),
        "LOOKUP_KEY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "lookup target count is two",
        len(lookup_table) == 2,
        2,
        len(lookup_table),
        "LOOKUP_TARGET_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "accepted new entries count is zero",
        0 == 0,
        0,
        0,
        "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    )
    _append_check(
        checks,
        "deterministic local lookup enabled in constructed index",
        True,
        True,
        True,
        "DETERMINISTIC_LOCAL_LOOKUP_NOT_ENABLED",
    )


def _build_lookup_table(packet: Mapping[str, Any]) -> dict[str, dict[str, str]]:
    first_locator = _artifact_path_for(packet, FIRST_LOCATOR_CHAIN_KEY)
    second_locator = _artifact_path_for(packet, SECOND_LOCATOR_CHAIN_KEY)
    first_orientation = _artifact_path_for(packet, FIRST_ORIENTATION_VIEW_CHAIN_KEY)
    second_orientation = _artifact_path_for(packet, SECOND_ORIENTATION_VIEW_CHAIN_KEY)
    return {
        "first_orientation_locator": {
            "lookup_key": "first_orientation_locator",
            "received_signal_id": _string_or_empty(packet.get("first_received_signal_id")),
            "locator_entry_artifact": first_locator,
            "orientation_view_artifact": first_orientation,
        },
        "second_orientation_locator": {
            "lookup_key": "second_orientation_locator",
            "received_signal_id": _string_or_empty(packet.get("second_received_signal_id")),
            "locator_entry_artifact": second_locator,
            "orientation_view_artifact": second_orientation,
        },
    }


def _build_orientation_index(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> dict[str, Any]:
    packet = basis.get("state_packet")
    if not isinstance(packet, Mapping):
        packet = {}
    return {
        "orientation_index_id": _string_or_empty(declared.get("orientation_index_id"))
        or DEFAULT_ORIENTATION_INDEX_ID,
        "orientation_index_type": ORIENTATION_INDEX_TYPE,
        "orientation_index_version": RESULT_VERSION,
        "orientation_index_system_type": ORIENTATION_INDEX_SYSTEM_TYPE,
        "orientation_index_system_version": RESULT_VERSION,
        "orientation_index_scope": ORIENTATION_INDEX_SCOPE,
        "basis_read_only_state_packet_artifact": _string_or_empty(
            basis.get("artifact_path")
        ),
        "basis_read_only_state_reader_outcome": basis.get("outcome"),
        "basis_read_only_state_reader_result_version": basis.get("result_version"),
        "basis_read_only_state_reader_failed_check_count": basis.get(
            "failed_check_count"
        ),
        "known_artifact_chain": copy.deepcopy(packet.get("known_artifact_chain", KNOWN_ARTIFACT_CHAIN)),
        "first_orientation_locator_entry_artifact": _artifact_path_for(
            packet, FIRST_LOCATOR_CHAIN_KEY
        ),
        "second_orientation_locator_entry_artifact": _artifact_path_for(
            packet, SECOND_LOCATOR_CHAIN_KEY
        ),
        "first_orientation_view_artifact": _artifact_path_for(
            packet, FIRST_ORIENTATION_VIEW_CHAIN_KEY
        ),
        "second_orientation_view_artifact": _artifact_path_for(
            packet, SECOND_ORIENTATION_VIEW_CHAIN_KEY
        ),
        "first_received_signal_id": packet.get("first_received_signal_id"),
        "second_received_signal_id": packet.get("second_received_signal_id"),
        "first_relevance_basis_id": packet.get("first_relevance_basis_id"),
        "second_relevance_basis_id": packet.get("second_relevance_basis_id"),
        "first_relevance_scope_id": packet.get("first_relevance_scope_id"),
        "second_relevance_scope_id": packet.get("second_relevance_scope_id"),
        "first_carrier_context_id": packet.get("first_carrier_context_id"),
        "second_carrier_context_id": packet.get("second_carrier_context_id"),
        "first_reception_envelope_id": packet.get("first_reception_envelope_id"),
        "second_reception_envelope_id": packet.get("second_reception_envelope_id"),
        "multiplicity_count": packet.get("multiplicity_count"),
        "relation_pair_count": packet.get("relation_pair_count"),
        "comparison_pair_count": packet.get("comparison_pair_count"),
        "comparison_readability_stands": packet.get("comparison_readability_stands"),
        "relation_readability_stands": packet.get("relation_readability_stands"),
        "multiplicity_result_stands": packet.get("multiplicity_result_stands"),
        "two_local_orientation_objects_stand": packet.get(
            "two_local_orientation_objects_stand"
        ),
        "lookup_table": _build_lookup_table(packet),
        "lookup_order": copy.deepcopy(LOOKUP_ORDER),
        "lookup_key_count": 2,
        "lookup_target_count": 2,
        "accepted_new_entries_count": 0,
        "deterministic_local_lookup_enabled": True,
        "read_only_orientation_index_recorded": True,
        "read_only_orientation_index_system_recorded": True,
        "new_signal_accepted": False,
        "new_relevance_object_created": False,
        "new_index_entry_created": False,
        "filesystem_discovery_performed": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "scoring_surface_created": False,
        "priority_surface_created": False,
        "validity_judgment_created": False,
        "truth_judgment_created": False,
        "authority_judgment_created": False,
        "currentness_judgment_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _empty_orientation_index(declared: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "orientation_index_id": _string_or_empty(declared.get("orientation_index_id"))
        or DEFAULT_ORIENTATION_INDEX_ID,
        "orientation_index_type": ORIENTATION_INDEX_TYPE,
        "orientation_index_version": RESULT_VERSION,
        "orientation_index_system_type": ORIENTATION_INDEX_SYSTEM_TYPE,
        "orientation_index_system_version": RESULT_VERSION,
        "orientation_index_scope": ORIENTATION_INDEX_SCOPE,
        "basis_read_only_state_packet_artifact": _string_or_empty(
            declared.get("selected_local_relevance_medium_read_only_state_packet_artifact")
        ),
        "basis_read_only_state_reader_outcome": None,
        "basis_read_only_state_reader_result_version": None,
        "basis_read_only_state_reader_failed_check_count": None,
        "known_artifact_chain": [],
        "first_orientation_locator_entry_artifact": "",
        "second_orientation_locator_entry_artifact": "",
        "first_orientation_view_artifact": "",
        "second_orientation_view_artifact": "",
        "first_received_signal_id": None,
        "second_received_signal_id": None,
        "first_relevance_basis_id": None,
        "second_relevance_basis_id": None,
        "first_relevance_scope_id": None,
        "second_relevance_scope_id": None,
        "first_carrier_context_id": None,
        "second_carrier_context_id": None,
        "first_reception_envelope_id": None,
        "second_reception_envelope_id": None,
        "multiplicity_count": None,
        "relation_pair_count": None,
        "comparison_pair_count": None,
        "comparison_readability_stands": False,
        "relation_readability_stands": False,
        "multiplicity_result_stands": False,
        "two_local_orientation_objects_stand": False,
        "lookup_table": {},
        "lookup_order": copy.deepcopy(LOOKUP_ORDER),
        "lookup_key_count": 0,
        "lookup_target_count": 0,
        "accepted_new_entries_count": 0,
        "deterministic_local_lookup_enabled": False,
        "read_only_orientation_index_recorded": False,
        "read_only_orientation_index_system_recorded": False,
        "new_signal_accepted": False,
        "new_relevance_object_created": False,
        "new_index_entry_created": False,
        "filesystem_discovery_performed": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
        "scoring_surface_created": False,
        "priority_surface_created": False,
        "validity_judgment_created": False,
        "truth_judgment_created": False,
        "authority_judgment_created": False,
        "currentness_judgment_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "source_transfer_occurred": False,
        "source_receipt_occurred": False,
        "authority_created": False,
        "currentness_created": False,
        "truth_created": False,
        "action_created": False,
        "synchronization_created": False,
        "participation_authorized": False,
        "participant_role_created": False,
        "runtime_permission_created": False,
        "public_api_created": False,
        "participant_facing_interface_created": False,
        "distributed_network_behavior_created": False,
        "follow_on_work_authorized": False,
    }


def _recorded_statement() -> dict[str, bool]:
    return {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _blocked_statement() -> dict[str, bool]:
    statement = {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["result_level_non_claims_canonical_false"] = True
    return statement


def _non_meaning() -> dict[str, bool]:
    return {
        "not_registry": True,
        "not_search": True,
        "not_ranking": True,
        "not_scoring": True,
        "not_priority": True,
        "not_validity_judgment": True,
        "not_truth_judgment": True,
        "not_authority_judgment": True,
        "not_currentness_judgment": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_distributed_network_behavior": True,
        "not_follow_on_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only orientation index system terminal summary, if separately selected",
        "registry",
        "search surface",
        "ranking surface",
        "source transfer",
        "source receipt",
        "authority creation",
        "currentness creation",
        "truth creation",
        "action",
        "synchronization",
        "participation authorization",
        "participant role",
        "runtime permission",
        "public API",
        "participant-facing interface",
        "distributed network behavior",
        "operation permission",
        "follow-on work",
    ]


def _requested_outcome(declared: Mapping[str, Any]) -> str | None:
    value = declared.get(
        "requested_local_relevance_medium_read_only_orientation_index_system_outcome"
    )
    if value in OUTCOME_FAMILY:
        return str(value)
    return None


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    _, failed_count = _check_counts(checks)
    if failed_count:
        return OUTCOME_BLOCKED
    requested = _requested_outcome(declared)
    intent = declared.get(
        "local_relevance_medium_read_only_orientation_index_system_intent"
    )
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or intent == DO_NOT_RECORD_INTENT:
        return OUTCOME_NOT_RECORDED
    if requested == OUTCOME_BLOCKED:
        return OUTCOME_BLOCKED
    if declared.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if declared.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_block(outcome: str, checks: list[Mapping[str, Any]]) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    code = _first_failed_code(checks) or (
        "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_MALFORMED"
    )
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": "local relevance medium read-only orientation index system was blocked by bounded validation",
    }


def _selected_basis_summary(basis: Mapping[str, Any]) -> dict[str, Any]:
    packet = basis.get("state_packet")
    if not isinstance(packet, Mapping):
        packet = {}
    return {
        "selected_local_relevance_medium_read_only_state_packet_artifact": basis.get(
            "artifact_path"
        ),
        "basis_read_only_state_reader_outcome": basis.get("outcome"),
        "basis_read_only_state_reader_result_version": basis.get("result_version"),
        "basis_read_only_state_reader_failed_check_count": basis.get(
            "failed_check_count"
        ),
        "state_packet_type": packet.get("state_packet_type"),
        "state_reader_type": packet.get("state_reader_type"),
        "state_reader_scope": packet.get("state_reader_scope"),
        "known_artifact_chain_count": len(packet.get("known_artifact_chain", []))
        if isinstance(packet.get("known_artifact_chain"), list)
        else 0,
        "first_orientation_locator_entry_artifact": _artifact_path_for(
            packet, FIRST_LOCATOR_CHAIN_KEY
        ),
        "second_orientation_locator_entry_artifact": _artifact_path_for(
            packet, SECOND_LOCATOR_CHAIN_KEY
        ),
        "first_orientation_view_artifact": _artifact_path_for(
            packet, FIRST_ORIENTATION_VIEW_CHAIN_KEY
        ),
        "second_orientation_view_artifact": _artifact_path_for(
            packet, SECOND_ORIENTATION_VIEW_CHAIN_KEY
        ),
    }


def _assemble_result(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
    orientation_index: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    passed_count, failed_count = _check_counts(checks)
    statement = _recorded_statement() if outcome == OUTCOME_RECORDED else _blocked_statement()
    metadata = {
        "local_relevance_medium_read_only_orientation_index_system_id": (
            _string_or_empty(
                declared.get(
                    "local_relevance_medium_read_only_orientation_index_system_id"
                )
            )
            or DEFAULT_ORIENTATION_INDEX_SYSTEM_ID
        ),
        "local_relevance_medium_read_only_orientation_index_system_type": (
            ORIENTATION_INDEX_SYSTEM_TYPE
        ),
        "local_relevance_medium_read_only_orientation_index_system_version": (
            RESULT_VERSION
        ),
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_orientation_index_system_metadata": metadata,
        "declared_local_relevance_medium_read_only_orientation_index_system_question": {
            "question": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_orientation_index_system_question"
                )
            ),
            "intent": _sanitize(
                declared.get(
                    "local_relevance_medium_read_only_orientation_index_system_intent"
                )
            ),
        },
        "selected_local_relevance_medium_read_only_state_packet_artifact_basis": _sanitize(
            _selected_basis_summary(basis)
        ),
        "local_relevance_medium_read_only_orientation_index": _sanitize(
            dict(orientation_index)
        ),
        "local_relevance_medium_read_only_orientation_index_system_checks": _sanitize(
            checks
        ),
        "local_relevance_medium_read_only_orientation_index_system_statement": statement,
        "local_relevance_medium_read_only_orientation_index_system_non_meaning": (
            _non_meaning()
        ),
        "additional_basis_required": _sanitize(
            declared.get("additional_basis_context", [])
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            declared.get("not_recorded_basis", [])
            if outcome == OUTCOME_NOT_RECORDED
            else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _build_block(outcome, checks),
    }
    result["local_relevance_medium_read_only_orientation_index_system_summary"] = (
        build_local_relevance_medium_read_only_orientation_index_system_v0_min_summary(
            result
        )
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
    declared_local_relevance_medium_read_only_orientation_index_system: Mapping[str, Any]
    | None = None,
) -> dict:
    """Resolve one bounded local read-only orientation index system result."""

    checks: list[dict[str, Any]] = []
    if declared_local_relevance_medium_read_only_orientation_index_system is None:
        declared = build_declared_local_relevance_medium_read_only_orientation_index_system_v0_min_request()
    elif not isinstance(
        declared_local_relevance_medium_read_only_orientation_index_system, Mapping
    ):
        declared = {}
        _append_check(
            checks,
            "declared local relevance medium read-only orientation index system request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_orientation_index_system).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_MALFORMED",
        )
        return _assemble_result(
            declared,
            _empty_basis(),
            _empty_orientation_index(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    else:
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_orientation_index_system)
        )

    _validate_declared_request(declared, checks)
    basis = _extract_state_packet_basis(declared, checks)
    _validate_state_reader_artifact(basis, checks)
    packet = basis.get("state_packet")
    if not isinstance(packet, Mapping):
        packet = {}
    _validate_state_packet(packet, checks)
    _validate_constructed_lookup_posture(packet, checks)
    _validate_false_postures(declared, checks)

    outcome = _determine_outcome(declared, checks)
    if outcome == OUTCOME_RECORDED:
        orientation_index = _build_orientation_index(declared, basis)
    else:
        orientation_index = _empty_orientation_index(declared)
    return _assemble_result(declared, basis, orientation_index, checks, outcome)


def resolve_local_relevance_medium_read_only_orientation_index_system_v0_min_from_path(
    declared_local_relevance_medium_read_only_orientation_index_system_path: Path | str,
) -> dict:
    """Read a declared read-only orientation index system request and resolve it."""

    try:
        with Path(
            declared_local_relevance_medium_read_only_orientation_index_system_path
        ).open("r", encoding="utf-8") as handle:
            request = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local relevance medium read-only orientation index system request readable",
                False,
                "readable JSON object",
                "unreadable",
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_UNREADABLE",
            )
        ]
        declared: dict[str, Any] = {}
        return _assemble_result(
            declared,
            _empty_basis(),
            _empty_orientation_index(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    if not isinstance(request, Mapping):
        checks = [
            _make_check(
                "declared local relevance medium read-only orientation index system request object",
                False,
                "JSON object",
                type(request).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_REQUEST_MALFORMED",
            )
        ]
        declared = {}
        return _assemble_result(
            declared,
            _empty_basis(),
            _empty_orientation_index(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    return resolve_local_relevance_medium_read_only_orientation_index_system_v0_min(
        request
    )


def build_local_relevance_medium_read_only_orientation_index_system_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary from a read-only orientation index system result."""

    metadata = result.get(
        "local_relevance_medium_read_only_orientation_index_system_metadata", {}
    )
    if not isinstance(metadata, Mapping):
        metadata = {}
    statement = result.get(
        "local_relevance_medium_read_only_orientation_index_system_statement", {}
    )
    if not isinstance(statement, Mapping):
        statement = {}
    question = result.get(
        "declared_local_relevance_medium_read_only_orientation_index_system_question",
        {},
    )
    if not isinstance(question, Mapping):
        question = {}
    orientation_index = result.get(
        "local_relevance_medium_read_only_orientation_index", {}
    )
    if not isinstance(orientation_index, Mapping):
        orientation_index = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {"blocked": False, "code": None, "block_code": None, "reason": None}
    checks = result.get(
        "local_relevance_medium_read_only_orientation_index_system_checks", []
    )
    if not isinstance(checks, list):
        checks = []
    passed_count, failed_count = _check_counts(
        [check for check in checks if isinstance(check, Mapping)]
    )
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    summary: dict[str, Any] = {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "orientation_index_id": orientation_index.get("orientation_index_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_count or metadata.get("passed_check_count", 0),
        "failed_check_count": failed_count or metadata.get("failed_check_count", 0),
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "read_only_orientation_index_recorded": bool(
            statement.get(
                "local_relevance_medium_read_only_orientation_index_recorded"
            )
        ),
        "read_only_orientation_index_system_recorded": bool(
            statement.get(
                "local_relevance_medium_read_only_orientation_index_system_recorded"
            )
        ),
        "basis_read_only_state_packet_artifact_preserved": bool(
            statement.get("basis_read_only_state_packet_artifact_preserved")
        ),
        "known_artifact_chain_preserved": bool(
            statement.get("known_artifact_chain_preserved")
        ),
        "first_locator_artifact_preserved": bool(
            statement.get("first_orientation_locator_entry_artifact_preserved")
        ),
        "second_locator_artifact_preserved": bool(
            statement.get("second_orientation_locator_entry_artifact_preserved")
        ),
        "first_orientation_view_artifact_preserved": bool(
            statement.get("first_orientation_view_artifact_preserved")
        ),
        "second_orientation_view_artifact_preserved": bool(
            statement.get("second_orientation_view_artifact_preserved")
        ),
        "first_received_signal_id_preserved": bool(
            statement.get("first_received_signal_id_preserved")
        ),
        "second_received_signal_id_preserved": bool(
            statement.get("second_received_signal_id_preserved")
        ),
        "first_and_second_signals_distinct": bool(
            statement.get("first_and_second_signals_distinct")
        ),
        "first_relevance_basis_id_preserved": bool(
            statement.get("first_relevance_basis_id_preserved")
        ),
        "second_relevance_basis_id_preserved": bool(
            statement.get("second_relevance_basis_id_preserved")
        ),
        "first_relevance_scope_id_preserved": bool(
            statement.get("first_relevance_scope_id_preserved")
        ),
        "second_relevance_scope_id_preserved": bool(
            statement.get("second_relevance_scope_id_preserved")
        ),
        "first_carrier_context_id_preserved": bool(
            statement.get("first_carrier_context_id_preserved")
        ),
        "second_carrier_context_id_preserved": bool(
            statement.get("second_carrier_context_id_preserved")
        ),
        "first_reception_envelope_id_preserved": bool(
            statement.get("first_reception_envelope_id_preserved")
        ),
        "second_reception_envelope_id_preserved": bool(
            statement.get("second_reception_envelope_id_preserved")
        ),
        "multiplicity_count_is_two": bool(
            statement.get("multiplicity_count_is_two")
        ),
        "relation_pair_count_is_one": bool(
            statement.get("relation_pair_count_is_one")
        ),
        "comparison_pair_count_is_one": bool(
            statement.get("comparison_pair_count_is_one")
        ),
        "comparison_readability_stands": bool(
            statement.get("comparison_readability_stands")
        ),
        "relation_readability_stands": bool(
            statement.get("relation_readability_stands")
        ),
        "multiplicity_result_stands": bool(
            statement.get("multiplicity_result_stands")
        ),
        "two_local_orientation_objects_stand": bool(
            statement.get("two_local_orientation_objects_stand")
        ),
        "lookup_table_has_two_entries": bool(
            statement.get("lookup_table_has_two_entries")
        ),
        "lookup_order_deterministic": bool(
            statement.get("lookup_order_is_deterministic")
        ),
        "lookup_key_count_is_two": bool(statement.get("lookup_key_count_is_two")),
        "lookup_target_count_is_two": bool(
            statement.get("lookup_target_count_is_two")
        ),
        "accepted_new_entries_count_is_zero": bool(
            statement.get("accepted_new_entries_count_is_zero")
        ),
        "deterministic_local_lookup_enabled": bool(
            statement.get("deterministic_local_lookup_enabled")
        ),
        "orientation_index_object_summary": {
            "orientation_index_type": orientation_index.get("orientation_index_type"),
            "orientation_index_system_type": orientation_index.get(
                "orientation_index_system_type"
            ),
            "orientation_index_scope": orientation_index.get(
                "orientation_index_scope"
            ),
            "lookup_order": orientation_index.get("lookup_order"),
            "lookup_key_count": orientation_index.get("lookup_key_count"),
            "lookup_target_count": orientation_index.get("lookup_target_count"),
            "accepted_new_entries_count": orientation_index.get(
                "accepted_new_entries_count"
            ),
        },
        "no_new_signal_relevance_object_or_index_entry_created": all(
            non_claims.get(key) is False
            for key in (
                "new_signal_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
            )
        ),
        "filesystem_discovery_not_performed": (
            non_claims.get("filesystem_discovery_performed") is False
        ),
        "registry_search_ranking_not_created": all(
            non_claims.get(key) is False
            for key in (
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
            )
        ),
        "scoring_priority_validity_truth_authority_currentness_not_created": all(
            non_claims.get(key) is False
            for key in (
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "repeated_arbitrary_feed_not_created": all(
            non_claims.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_action_sync_participation_runtime_not_created": all(
            non_claims.get(key) is False
            for key in (
                "source_transfer_occurred",
                "source_receipt_occurred",
                "source_created",
                "authority_created",
                "currentness_created",
                "truth_created",
                "action_created",
                "synchronization_created",
                "participation_authorized",
                "participant_role_created",
                "runtime_permission_created",
            )
        ),
        "api_interface_distributed_not_created": all(
            non_claims.get(key) is False
            for key in (
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
            )
        ),
        "operation_permission_follow_on_not_created": all(
            non_claims.get(key) is False
            for key in ("operation_permission_created", "follow_on_work_authorized")
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "new_signal_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
                "filesystem_discovery_performed",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "runtime_permission_created",
                "public_api_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": all(
            non_claims.get(key) is False
            for key in (
                "predecessor_failure_repaired",
                "predecessor_failure_hidden",
                "predecessor_failure_claimed_passed",
            )
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    return _sanitize(summary)


def _default_output_path(result: Mapping[str, Any]) -> Path:
    orientation_index = result.get(
        "local_relevance_medium_read_only_orientation_index", {}
    )
    if not isinstance(orientation_index, Mapping):
        orientation_index = {}
    orientation_index_id = (
        _string_or_empty(orientation_index.get("orientation_index_id"))
        or DEFAULT_ORIENTATION_INDEX_ID
    )
    return OUTPUT_ROOT / (
        f"{orientation_index_id}__"
        "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
    )


def _non_overwriting_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 1000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise LocalRelevanceMediumReadOnlyOrientationIndexSystemV0MinError(
        "could not allocate non-overwriting result path"
    )


def write_local_relevance_medium_read_only_orientation_index_system_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a stable JSON resolver result without silently overwriting."""

    if output_path is None:
        path = _default_output_path(result)
    else:
        candidate = Path(output_path)
        if candidate.suffix:
            path = candidate
        else:
            path = candidate / _default_output_path(result).name
    path = _non_overwriting_path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_orientation_index_system_v0_min_request(
    selected_local_relevance_medium_read_only_state_packet_artifact: Path | str | None = None,
    *,
    local_relevance_medium_read_only_orientation_index_system_id: str = DEFAULT_ORIENTATION_INDEX_SYSTEM_ID,
    local_relevance_medium_read_only_orientation_index_system_question: str | None = None,
    local_relevance_medium_read_only_orientation_index_system_intent: str = RECORD_INTENT,
    orientation_index_type: str = ORIENTATION_INDEX_TYPE,
    orientation_index_system_type: str = ORIENTATION_INDEX_SYSTEM_TYPE,
    orientation_index_scope: str = ORIENTATION_INDEX_SCOPE,
    lookup_order: list[str] | None = None,
) -> dict[str, Any]:
    """Build a declared request with all required non-claims canonical false."""

    question = local_relevance_medium_read_only_orientation_index_system_question
    if question is None:
        question = (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET, may one "
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM record one "
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX that indexes only "
            "the already-standing first and second local orientation locator "
            "entries for deterministic local lookup?"
        )
    selected_path = (
        selected_local_relevance_medium_read_only_state_packet_artifact
        if selected_local_relevance_medium_read_only_state_packet_artifact is not None
        else DEFAULT_READ_ONLY_STATE_PACKET_ARTIFACT
    )
    return {
        "local_relevance_medium_read_only_orientation_index_system_id": (
            local_relevance_medium_read_only_orientation_index_system_id
        ),
        "local_relevance_medium_read_only_orientation_index_system_question": question,
        "local_relevance_medium_read_only_orientation_index_system_intent": (
            local_relevance_medium_read_only_orientation_index_system_intent
        ),
        "selected_local_relevance_medium_read_only_state_packet_artifact": str(
            selected_path
        ),
        "orientation_index_type": orientation_index_type,
        "orientation_index_system_type": orientation_index_system_type,
        "orientation_index_scope": orientation_index_scope,
        "lookup_order": copy.deepcopy(lookup_order if lookup_order is not None else LOOKUP_ORDER),
        "lookup_key_count": 2,
        "lookup_target_count": 2,
        "accepted_new_entries_count": 0,
        "deterministic_local_lookup_enabled": True,
        "declared_non_claims": _canonical_non_claims(),
    }
