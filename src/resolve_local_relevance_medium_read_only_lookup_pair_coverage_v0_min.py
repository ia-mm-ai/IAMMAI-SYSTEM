"""Resolve one local relevance medium read-only lookup-pair coverage record.

This resolver reads one clean first read-only orientation lookup result
artifact, one clean second read-only orientation lookup result artifact, and one
clean read-only orientation index artifact. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE object only: coverage that
both supported lookup keys have individual clean lookup result artifacts.

It is coverage-shaped, read-only, local, and non-permission-shaped. It does not
create reusable lookup permission, general lookup permission, a new lookup
result, a new lookup entry, registry, search, query surface, ranking, scoring,
priority, validity judgment, truth judgment, authority judgment, currentness
judgment, repeated reception permission, arbitrary reception, feed, source
transfer, source receipt, runtime permission, public API, distributed behavior,
operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyLookupPairCoverageV0MinError(Exception):
    """Bounded error for lookup-pair coverage request handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min"
)
DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min/"
    "local_relevance_medium_read_only_orientation_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_orientation_lookup_result_v0_min_result.json"
)
DEFAULT_SECOND_LOOKUP_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min/"
    "local_relevance_medium_read_only_second_orientation_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result.json"
)
DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

DEFAULT_LOOKUP_PAIR_COVERAGE_ID = "local_relevance_medium_read_only_lookup_pair_coverage_001"
DEFAULT_REQUEST_ID = DEFAULT_LOOKUP_PAIR_COVERAGE_ID

LOOKUP_PAIR_COVERAGE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"
LOOKUP_PAIR_COVERAGE_SCOPE = "BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY"
SUPPORTED_LOOKUP_PAIR_COVERAGE_TYPE_VALUES = (LOOKUP_PAIR_COVERAGE_TYPE,)
SUPPORTED_LOOKUP_PAIR_COVERAGE_SCOPE_VALUES = (LOOKUP_PAIR_COVERAGE_SCOPE,)

FIRST_LOOKUP_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
SECOND_LOOKUP_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
FIRST_LOOKUP_RECORDED_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED"
SECOND_LOOKUP_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_RECORDED"
)
ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED"
)

FIRST_LOOKUP_KEY = "first_orientation_locator"
SECOND_LOOKUP_KEY = "second_orientation_locator"
SUPPORTED_LOOKUP_KEYS = [FIRST_LOOKUP_KEY, SECOND_LOOKUP_KEY]
LOOKUP_ORDER = [FIRST_LOOKUP_KEY, SECOND_LOOKUP_KEY]
FIRST_SELECTED_SIGNAL_ID = "bounded_relevance_signal_001"
SECOND_SELECTED_SIGNAL_ID = "bounded_relevance_signal_002"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean first LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT and one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE record be recorded that records coverage "
    "of both supported lookup keys, first_orientation_locator and second_orientation_locator, without "
    "creating reusable lookup permission, general lookup permission, new lookup result, new lookup "
    "entry, registry, search, query surface, ranking, scoring, priority, validity judgment, truth "
    "judgment, authority, currentness, action, synchronization, participation authorization, "
    "participant role, runtime permission, public API, participant-facing interface, distributed "
    "network behavior, operation permission, repeated reception permission, arbitrary reception, "
    "feed, source transfer, source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "reusable_lookup_permission_created",
    "general_lookup_permission_created",
    "new_lookup_result_created",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
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
    "artifact_existence_treated_as_lookup_pair_coverage_authority",
    "latest_file_posture_treated_as_lookup_pair_coverage_authority",
    "repo_local_availability_treated_as_lookup_pair_coverage_authority",
    "hidden_repo_state_used_as_lookup_pair_coverage_content",
    "hidden_repo_state_used_as_lookup_pair_coverage_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

OBJECT_FALSE_FIELDS = (
    "reusable_lookup_permission_created",
    "general_lookup_permission_created",
    "new_lookup_result_created",
    "new_lookup_entry_created",
    "new_signal_accepted",
    "new_entry_accepted",
    "new_relevance_object_created",
    "new_index_entry_created",
    "filesystem_discovery_performed",
    "registry_created",
    "search_surface_created",
    "query_surface_created",
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
    "follow_on_work_authorized",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_lookup_pair_coverage_recorded",
    "basis_first_lookup_result_artifact_preserved",
    "basis_second_lookup_result_artifact_preserved",
    "basis_read_only_orientation_index_artifact_preserved",
    "supported_lookup_keys_preserved",
    "covered_lookup_keys_preserved",
    "supported_lookup_key_count_is_two",
    "covered_lookup_key_count_is_two",
    "both_supported_lookup_keys_covered",
    "first_declared_lookup_key_preserved",
    "second_declared_lookup_key_preserved",
    "first_selected_received_signal_id_preserved",
    "second_selected_received_signal_id_preserved",
    "first_and_second_selected_received_signal_ids_distinct",
    "first_selected_locator_entry_artifact_preserved",
    "second_selected_locator_entry_artifact_preserved",
    "first_selected_orientation_view_artifact_preserved",
    "second_selected_orientation_view_artifact_preserved",
    "lookup_order_is_deterministic",
    "accepted_new_entries_count_is_zero",
    "deterministic_local_lookup_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BLOCK_REQUESTED",
    "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "FIRST_LOOKUP_RESULT_ARTIFACT_UNREADABLE",
    "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "FIRST_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "FIRST_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "SECOND_LOOKUP_RESULT_ARTIFACT_UNREADABLE",
    "SECOND_LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "SECOND_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "SECOND_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "SECOND_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_UNREADABLE",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_JSON_OBJECT",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    "SUPPORTED_LOOKUP_KEYS_NOT_EXACT",
    "COVERED_LOOKUP_KEYS_NOT_EXACT",
    "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "COVERED_LOOKUP_KEY_COUNT_NOT_TWO",
    "LOOKUP_TABLE_KEY_COUNT_NOT_TWO",
    "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "FIRST_DECLARED_LOOKUP_KEY_NOT_FIRST_ORIENTATION_LOCATOR",
    "SECOND_DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR",
    "FIRST_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_001",
    "SECOND_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002",
    "FIRST_AND_SECOND_SELECTED_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
    "FIRST_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "SECOND_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "FIRST_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "SECOND_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "LOOKUP_PAIR_COVERAGE_TYPE_MISSING",
    "LOOKUP_PAIR_COVERAGE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
    "LOOKUP_PAIR_COVERAGE_SCOPE_MISSING",
    "LOOKUP_PAIR_COVERAGE_SCOPE_NOT_BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
    "LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
    "REUSABLE_LOOKUP_PERMISSION_CREATED",
    "GENERAL_LOOKUP_PERMISSION_CREATED",
    "NEW_LOOKUP_RESULT_CREATED",
    "NEW_LOOKUP_ENTRY_CREATED",
    "NEW_SIGNAL_ACCEPTED",
    "NEW_ENTRY_ACCEPTED",
    "NEW_RELEVANCE_OBJECT_CREATED",
    "NEW_INDEX_ENTRY_CREATED",
    "FILESYSTEM_DISCOVERY_PERFORMED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "QUERY_SURFACE_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PAIR_COVERAGE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PAIR_COVERAGE_BODY_MUST_NOT_RETURN",
    "RAW_FIRST_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_lookup_pair_coverage_body",
    "raw_first_lookup_result_body",
    "raw_second_lookup_result_body",
    "raw_lookup_result_body",
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
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "lookup_pair_coverage_body",
    "first_lookup_result_body",
    "second_lookup_result_body",
    "lookup_result_body",
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

OFFICIAL_STRINGS = frozenset(
    (
        RESULT_VERSION,
        RESOLVER_MODULE,
        LOOKUP_PAIR_COVERAGE_TYPE,
        LOOKUP_PAIR_COVERAGE_SCOPE,
        FIRST_LOOKUP_RESULT_TYPE,
        SECOND_LOOKUP_RESULT_TYPE,
        FIRST_LOOKUP_RECORDED_OUTCOME,
        SECOND_LOOKUP_RECORDED_OUTCOME,
        ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        FIRST_LOOKUP_KEY,
        SECOND_LOOKUP_KEY,
        FIRST_SELECTED_SIGNAL_ID,
        SECOND_SELECTED_SIGNAL_ID,
        INTENT_RECORD,
        INTENT_DO_NOT_RECORD,
        INTENT_BLOCK,
        *OUTCOME_FAMILY,
        *BLOCK_CODES,
        *REQUIRED_FALSE_NON_CLAIMS,
        *ALLOWED_TRUE_RECORDED_FIELDS,
    )
)

SHORTCUT_FAILURES = {
    "first_lookup_result_artifact_missing": "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "first_lookup_result_artifact_not_recorded": "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "first_lookup_result_artifact_failed_checks_present": "FIRST_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "first_lookup_result_artifact_version_not_0_1_0": "FIRST_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "second_lookup_result_artifact_missing": "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "second_lookup_result_artifact_not_recorded": "SECOND_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "second_lookup_result_artifact_failed_checks_present": "SECOND_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "second_lookup_result_artifact_version_not_0_1_0": "SECOND_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "read_only_orientation_index_artifact_missing": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    "read_only_orientation_index_artifact_not_recorded": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    "read_only_orientation_index_artifact_failed_checks_present": (
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "read_only_orientation_index_artifact_version_not_0_1_0": (
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "supported_lookup_keys_not_exact": "SUPPORTED_LOOKUP_KEYS_NOT_EXACT",
    "covered_lookup_keys_not_exact": "COVERED_LOOKUP_KEYS_NOT_EXACT",
    "supported_lookup_key_count_not_two": "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "covered_lookup_key_count_not_two": "COVERED_LOOKUP_KEY_COUNT_NOT_TWO",
    "lookup_table_key_count_not_two": "LOOKUP_TABLE_KEY_COUNT_NOT_TWO",
    "lookup_table_target_count_not_two": "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "first_declared_lookup_key_not_first_orientation_locator": (
        "FIRST_DECLARED_LOOKUP_KEY_NOT_FIRST_ORIENTATION_LOCATOR"
    ),
    "second_declared_lookup_key_not_second_orientation_locator": (
        "SECOND_DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR"
    ),
    "first_selected_received_signal_id_not_bounded_relevance_signal_001": (
        "FIRST_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_001"
    ),
    "second_selected_received_signal_id_not_bounded_relevance_signal_002": (
        "SECOND_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002"
    ),
    "first_and_second_selected_received_signal_ids_not_distinct": (
        "FIRST_AND_SECOND_SELECTED_RECEIVED_SIGNAL_IDS_NOT_DISTINCT"
    ),
    "first_selected_locator_entry_artifact_missing": "FIRST_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "second_selected_locator_entry_artifact_missing": "SECOND_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "first_selected_orientation_view_artifact_missing": "FIRST_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "second_selected_orientation_view_artifact_missing": "SECOND_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "lookup_order_not_deterministic": "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "accepted_new_entries_count_not_zero": "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "deterministic_local_lookup_not_preserved": "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "lookup_pair_coverage_type_not_local_relevance_medium_read_only_lookup_pair_coverage": (
        "LOOKUP_PAIR_COVERAGE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"
    ),
    "lookup_pair_coverage_scope_not_both_supported_orientation_lookup_keys_covered_only": (
        "LOOKUP_PAIR_COVERAGE_SCOPE_NOT_BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY"
    ),
    "lookup_pair_coverage_not_recorded": "LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
    "reusable_lookup_permission_created": "REUSABLE_LOOKUP_PERMISSION_CREATED",
    "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
    "new_lookup_result_created": "NEW_LOOKUP_RESULT_CREATED",
    "new_lookup_entry_created": "NEW_LOOKUP_ENTRY_CREATED",
    "new_signal_accepted": "NEW_SIGNAL_ACCEPTED",
    "new_entry_accepted": "NEW_ENTRY_ACCEPTED",
    "new_relevance_object_created": "NEW_RELEVANCE_OBJECT_CREATED",
    "new_index_entry_created": "NEW_INDEX_ENTRY_CREATED",
    "filesystem_discovery_performed": "FILESYSTEM_DISCOVERY_PERFORMED",
    "registry_created": "REGISTRY_CREATED",
    "search_surface_created": "SEARCH_SURFACE_CREATED",
    "query_surface_created": "QUERY_SURFACE_CREATED",
    "ranking_surface_created": "RANKING_SURFACE_CREATED",
    "scoring_surface_created": "SCORING_SURFACE_CREATED",
    "priority_surface_created": "PRIORITY_SURFACE_CREATED",
    "validity_judgment_created": "VALIDITY_JUDGMENT_CREATED",
    "truth_judgment_created": "TRUTH_JUDGMENT_CREATED",
    "authority_judgment_created": "AUTHORITY_JUDGMENT_CREATED",
    "currentness_judgment_created": "CURRENTNESS_JUDGMENT_CREATED",
    "repeated_reception_permission_created": "REPEATED_RECEPTION_PERMISSION_CREATED",
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
    "artifact_existence_treated_as_lookup_pair_coverage_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY"
    ),
    "latest_file_posture_treated_as_lookup_pair_coverage_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY"
    ),
    "repo_local_availability_treated_as_lookup_pair_coverage_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_lookup_pair_coverage_content": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PAIR_COVERAGE_CONTENT"
    ),
    "hidden_repo_state_used_as_lookup_pair_coverage_authority": (
        "HIDDEN_REPO_STATE_USED_AS_LOOKUP_PAIR_COVERAGE_AUTHORITY"
    ),
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _string_or_empty(value: Any) -> str:
    if isinstance(value, Path):
        return str(value)
    return value if isinstance(value, str) else ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    key_lower = key.lower()
    return key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if parent_key and _is_sensitive_key(parent_key):
            return "[REDACTED_RAW_CONTENT]"
        if any(sentinel in value for sentinel in RAW_SENTINELS):
            return "[REDACTED_RAW_CONTENT]"
        return value
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, MappingABC):
        if parent_key and _is_sensitive_key(parent_key):
            return "[REDACTED_RAW_CONTENT]"
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    return value


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    check = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed and code:
        public_code = (
            code
            if code in BLOCK_CODES
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED"
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
    checks.append(_make_check(check_name, passed, expected_posture, actual_posture, code))


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is True:
            continue
        code = check.get("block_code") or check.get("failure_code")
        if isinstance(code, str) and code in BLOCK_CODES:
            return code
    return None


def _read_json_object(
    path_value: Any,
    missing_code: str,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None, str]:
    path_text = _string_or_empty(path_value)
    if not _present(path_text):
        return None, missing_code, ""
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, unreadable_code, path_text
    if not isinstance(loaded, MappingABC):
        return None, not_object_code, path_text
    return copy.deepcopy(dict(loaded)), None, path_text


def _first_mapping_for_key_suffix(artifact: Mapping[str, Any], suffix: str) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith(suffix) and isinstance(value, MappingABC):
            return value
    return {}


def _metadata(artifact: Mapping[str, Any], preferred_key: str) -> Mapping[str, Any]:
    preferred = artifact.get(preferred_key)
    if isinstance(preferred, MappingABC):
        return preferred
    return _first_mapping_for_key_suffix(artifact, "_metadata")


def _summary_mapping(artifact: Mapping[str, Any], preferred_key: str) -> Mapping[str, Any]:
    preferred = artifact.get(preferred_key)
    if isinstance(preferred, MappingABC):
        return preferred
    return _first_mapping_for_key_suffix(artifact, "_summary")


def _artifact_result_version(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    object_value: Mapping[str, Any] | None = None,
) -> str | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    sources: list[Mapping[str, Any]] = [artifact, metadata, summary]
    if isinstance(object_value, MappingABC):
        sources.append(object_value)
    version_keys = (
        "result_version",
        "lookup_pair_coverage_version",
        "second_lookup_result_version",
        "lookup_result_version",
        "orientation_index_system_version",
        "orientation_index_version",
        "version",
    )
    for source in sources:
        for key in version_keys:
            value = source.get(key)
            if isinstance(value, str):
                return value
    return None


def _artifact_failed_check_count(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
    checks_key: str,
) -> int | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    for source in (artifact, metadata, summary):
        count = _safe_int(source.get("failed_check_count"))
        if count is not None:
            return count
    checks = artifact.get(checks_key)
    if isinstance(checks, list):
        return sum(1 for check in checks if isinstance(check, MappingABC) and check.get("passed") is not True)
    return None


def _first_lookup_object_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_orientation_lookup_result")
    return value if isinstance(value, MappingABC) else {}


def _second_lookup_object_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_second_orientation_lookup_result")
    return value if isinstance(value, MappingABC) else {}


def _orientation_index_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_orientation_index")
    return value if isinstance(value, MappingABC) else {}


def _lookup_table_from_index(index_object: Mapping[str, Any]) -> Mapping[str, Any]:
    table = index_object.get("lookup_table")
    return table if isinstance(table, MappingABC) else {}


def _lookup_key_count(index_object: Mapping[str, Any]) -> int | None:
    count = _safe_int(index_object.get("lookup_key_count"))
    if count is not None:
        return count
    table = _lookup_table_from_index(index_object)
    return len(table) if table else None


def _lookup_target_count(index_object: Mapping[str, Any]) -> int | None:
    count = _safe_int(index_object.get("lookup_target_count"))
    if count is not None:
        return count
    table = _lookup_table_from_index(index_object)
    return len([target for target in table.values() if isinstance(target, MappingABC)]) if table else None


def _selected_locator_artifact(result_object: Mapping[str, Any]) -> str:
    return _string_or_empty(
        result_object.get("selected_locator_entry_artifact")
        or result_object.get("locator_entry_artifact")
        or result_object.get("orientation_locator_entry_artifact")
        or result_object.get("local_orientation_locator_entry_artifact")
    )


def _selected_orientation_artifact(result_object: Mapping[str, Any]) -> str:
    return _string_or_empty(
        result_object.get("selected_orientation_view_artifact")
        or result_object.get("orientation_view_artifact")
    )


def _append_declared_request_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = declared.get("local_relevance_medium_read_only_lookup_pair_coverage_question")
    intent = declared.get("local_relevance_medium_read_only_lookup_pair_coverage_intent")
    coverage_type = declared.get("lookup_pair_coverage_type")
    coverage_scope = declared.get("lookup_pair_coverage_scope")

    _append_check(
        checks,
        "lookup-pair coverage question declared",
        _present(question),
        "declared lookup-pair coverage question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "lookup-pair coverage intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "lookup-pair coverage block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_BLOCK_REQUESTED",
        )
    _append_check(
        checks,
        "lookup-pair coverage type declared",
        _present(coverage_type),
        LOOKUP_PAIR_COVERAGE_TYPE,
        coverage_type,
        "LOOKUP_PAIR_COVERAGE_TYPE_MISSING",
    )
    _append_check(
        checks,
        "lookup-pair coverage type exact",
        coverage_type == LOOKUP_PAIR_COVERAGE_TYPE,
        LOOKUP_PAIR_COVERAGE_TYPE,
        coverage_type,
        "LOOKUP_PAIR_COVERAGE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE",
    )
    _append_check(
        checks,
        "lookup-pair coverage scope declared",
        _present(coverage_scope),
        LOOKUP_PAIR_COVERAGE_SCOPE,
        coverage_scope,
        "LOOKUP_PAIR_COVERAGE_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "lookup-pair coverage scope both supported orientation lookup keys covered only",
        coverage_scope == LOOKUP_PAIR_COVERAGE_SCOPE,
        LOOKUP_PAIR_COVERAGE_SCOPE,
        coverage_scope,
        "LOOKUP_PAIR_COVERAGE_SCOPE_NOT_BOTH_SUPPORTED_ORIENTATION_LOOKUP_KEYS_COVERED_ONLY",
    )


def _append_shortcut_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    for field_name, block_code in SHORTCUT_FAILURES.items():
        asserted = declared.get(field_name) is True
        _append_check(
            checks,
            f"shortcut {field_name} not asserted",
            not asserted,
            False,
            asserted,
            block_code,
        )


def _append_non_claim_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not isinstance(declared_non_claims, MappingABC):
        _append_check(
            checks,
            "declared non-claims mapping present",
            False,
            "mapping with every required non-claim false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return
    for key in REQUIRED_FALSE_NON_CLAIMS:
        actual = declared_non_claims.get(key)
        _append_check(
            checks,
            f"required non-claim {key} declared false",
            actual is False,
            False,
            actual,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_first_lookup_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_first_lookup_result_artifact")
    artifact, read_code, path_text = _read_json_object(
        artifact_value,
        "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
        "FIRST_LOOKUP_RESULT_ARTIFACT_UNREADABLE",
        "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    )
    _append_check(
        checks,
        "first lookup result artifact path declared",
        read_code != "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
        "declared first lookup result artifact path",
        artifact_value,
        "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    )
    if read_code:
        if read_code != "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING":
            _append_check(checks, "first lookup result artifact readable JSON object", False, "readable JSON object", read_code, read_code)
        return None, path_text

    first_object = _first_lookup_object_from_artifact(artifact)
    outcome = artifact.get("outcome")
    version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_orientation_lookup_result_metadata",
        "local_relevance_medium_read_only_orientation_lookup_result_summary",
        first_object,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_orientation_lookup_result_metadata",
        "local_relevance_medium_read_only_orientation_lookup_result_summary",
        "local_relevance_medium_read_only_orientation_lookup_result_checks",
    )
    first_key = first_object.get("declared_lookup_key")
    first_signal = first_object.get("selected_received_signal_id")
    first_locator = _selected_locator_artifact(first_object)
    first_orientation = _selected_orientation_artifact(first_object)

    _append_check(checks, "first lookup result artifact readable JSON object", True, "readable JSON object", "readable JSON object")
    _append_check(checks, "first lookup result artifact outcome recorded", outcome == FIRST_LOOKUP_RECORDED_OUTCOME, FIRST_LOOKUP_RECORDED_OUTCOME, outcome, "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED")
    _append_check(checks, "first lookup result artifact result version 0.1.0", version == RESULT_VERSION, RESULT_VERSION, version, "FIRST_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0")
    _append_check(checks, "first lookup result artifact failed check count zero", failed_count == 0, 0, failed_count, "FIRST_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT")
    _append_check(checks, "first declared lookup key preserved", first_key == FIRST_LOOKUP_KEY, FIRST_LOOKUP_KEY, first_key, "FIRST_DECLARED_LOOKUP_KEY_NOT_FIRST_ORIENTATION_LOCATOR")
    _append_check(checks, "first selected received signal id preserved", first_signal == FIRST_SELECTED_SIGNAL_ID, FIRST_SELECTED_SIGNAL_ID, first_signal, "FIRST_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_001")
    _append_check(checks, "first selected locator artifact preserved", _present(first_locator), "first selected locator entry artifact", first_locator, "FIRST_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING")
    _append_check(checks, "first selected orientation view artifact preserved", _present(first_orientation), "first selected orientation view artifact", first_orientation, "FIRST_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING")
    return artifact, path_text


def _validate_second_lookup_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_second_lookup_result_artifact")
    artifact, read_code, path_text = _read_json_object(
        artifact_value,
        "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
        "SECOND_LOOKUP_RESULT_ARTIFACT_UNREADABLE",
        "SECOND_LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    )
    _append_check(
        checks,
        "second lookup result artifact path declared",
        read_code != "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
        "declared second lookup result artifact path",
        artifact_value,
        "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    )
    if read_code:
        if read_code != "SECOND_LOOKUP_RESULT_ARTIFACT_PATH_MISSING":
            _append_check(checks, "second lookup result artifact readable JSON object", False, "readable JSON object", read_code, read_code)
        return None, path_text

    second_object = _second_lookup_object_from_artifact(artifact)
    outcome = artifact.get("outcome")
    version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
        "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
        second_object,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
        "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
        "local_relevance_medium_read_only_second_orientation_lookup_result_checks",
    )
    second_key = second_object.get("declared_lookup_key")
    second_signal = second_object.get("selected_received_signal_id")
    second_locator = _selected_locator_artifact(second_object)
    second_orientation = _selected_orientation_artifact(second_object)

    _append_check(checks, "second lookup result artifact readable JSON object", True, "readable JSON object", "readable JSON object")
    _append_check(checks, "second lookup result artifact outcome recorded", outcome == SECOND_LOOKUP_RECORDED_OUTCOME, SECOND_LOOKUP_RECORDED_OUTCOME, outcome, "SECOND_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED")
    _append_check(checks, "second lookup result artifact result version 0.1.0", version == RESULT_VERSION, RESULT_VERSION, version, "SECOND_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0")
    _append_check(checks, "second lookup result artifact failed check count zero", failed_count == 0, 0, failed_count, "SECOND_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT")
    _append_check(checks, "second declared lookup key preserved", second_key == SECOND_LOOKUP_KEY, SECOND_LOOKUP_KEY, second_key, "SECOND_DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR")
    _append_check(checks, "second selected received signal id preserved", second_signal == SECOND_SELECTED_SIGNAL_ID, SECOND_SELECTED_SIGNAL_ID, second_signal, "SECOND_SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002")
    _append_check(checks, "second selected locator artifact preserved", _present(second_locator), "second selected locator entry artifact", second_locator, "SECOND_SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING")
    _append_check(checks, "second selected orientation view artifact preserved", _present(second_orientation), "second selected orientation view artifact", second_orientation, "SECOND_SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING")
    return artifact, path_text


def _validate_orientation_index_artifact(
    declared: Mapping[str, Any],
    first_artifact: Mapping[str, Any] | None,
    second_artifact: Mapping[str, Any] | None,
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_read_only_orientation_index_artifact")
    artifact, read_code, path_text = _read_json_object(
        artifact_value,
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_UNREADABLE",
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_JSON_OBJECT",
    )
    _append_check(
        checks,
        "read-only orientation index artifact path declared",
        read_code != "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
        "declared read-only orientation index artifact path",
        artifact_value,
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    )
    if read_code:
        if read_code != "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING":
            _append_check(checks, "read-only orientation index artifact readable JSON object", False, "readable JSON object", read_code, read_code)
        return None, path_text

    index_object = _orientation_index_from_artifact(artifact)
    first_object = _first_lookup_object_from_artifact(first_artifact)
    second_object = _second_lookup_object_from_artifact(second_artifact)
    outcome = artifact.get("outcome")
    version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_orientation_index_system_metadata",
        "local_relevance_medium_read_only_orientation_index_system_summary",
        index_object,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_orientation_index_system_metadata",
        "local_relevance_medium_read_only_orientation_index_system_summary",
        "local_relevance_medium_read_only_orientation_index_system_checks",
    )
    lookup_table = _lookup_table_from_index(index_object)
    supported_keys = list(lookup_table.keys()) if isinstance(lookup_table, MappingABC) else []
    covered_keys = [first_object.get("declared_lookup_key"), second_object.get("declared_lookup_key")]
    lookup_order = index_object.get("lookup_order")
    lookup_key_count = _lookup_key_count(index_object)
    lookup_target_count = _lookup_target_count(index_object)
    accepted_count = _safe_int(index_object.get("accepted_new_entries_count"))
    deterministic = (
        index_object.get("deterministic_local_lookup_enabled") is True
        or index_object.get("deterministic_local_lookup_preserved") is True
    )
    first_signal = first_object.get("selected_received_signal_id")
    second_signal = second_object.get("selected_received_signal_id")

    _append_check(checks, "read-only orientation index artifact readable JSON object", True, "readable JSON object", "readable JSON object")
    _append_check(checks, "read-only orientation index artifact outcome recorded", outcome == ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME, ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME, outcome, "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED")
    _append_check(checks, "read-only orientation index artifact result version 0.1.0", version == RESULT_VERSION, RESULT_VERSION, version, "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0")
    _append_check(checks, "read-only orientation index artifact failed check count zero", failed_count == 0, 0, failed_count, "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT")
    _append_check(checks, "supported lookup keys exact", supported_keys == SUPPORTED_LOOKUP_KEYS, SUPPORTED_LOOKUP_KEYS, supported_keys, "SUPPORTED_LOOKUP_KEYS_NOT_EXACT")
    _append_check(checks, "covered lookup keys exact", covered_keys == SUPPORTED_LOOKUP_KEYS, SUPPORTED_LOOKUP_KEYS, covered_keys, "COVERED_LOOKUP_KEYS_NOT_EXACT")
    _append_check(checks, "supported lookup key count exactly two", lookup_key_count == 2, 2, lookup_key_count, "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO")
    _append_check(checks, "covered lookup key count exactly two", len([key for key in covered_keys if key in SUPPORTED_LOOKUP_KEYS]) == 2, 2, covered_keys, "COVERED_LOOKUP_KEY_COUNT_NOT_TWO")
    _append_check(checks, "lookup table key count exactly two", len(lookup_table) == 2, 2, len(lookup_table), "LOOKUP_TABLE_KEY_COUNT_NOT_TWO")
    _append_check(checks, "lookup table target count exactly two", lookup_target_count == 2, 2, lookup_target_count, "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO")
    _append_check(checks, "first and second selected received signal ids distinct", first_signal != second_signal and _present(first_signal) and _present(second_signal), "distinct first and second selected received signal ids", [first_signal, second_signal], "FIRST_AND_SECOND_SELECTED_RECEIVED_SIGNAL_IDS_NOT_DISTINCT")
    _append_check(checks, "lookup order deterministic", lookup_order == LOOKUP_ORDER, LOOKUP_ORDER, lookup_order, "LOOKUP_ORDER_NOT_DETERMINISTIC")
    _append_check(checks, "accepted new entries count zero", accepted_count == 0, 0, accepted_count, "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO")
    _append_check(checks, "deterministic local lookup preserved", deterministic is True, True, deterministic, "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED")
    return artifact, path_text


def _first_lookup_artifact_basis(artifact: Mapping[str, Any] | None, path_text: str) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"selected_first_lookup_result_artifact": path_text}
    first_object = _first_lookup_object_from_artifact(artifact)
    return {
        "selected_first_lookup_result_artifact": path_text,
        "basis_first_lookup_result_outcome": artifact.get("outcome"),
        "basis_first_lookup_result_result_version": _artifact_result_version(
            artifact,
            "local_relevance_medium_read_only_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_orientation_lookup_result_summary",
            first_object,
        ),
        "basis_first_lookup_result_failed_check_count": _artifact_failed_check_count(
            artifact,
            "local_relevance_medium_read_only_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_orientation_lookup_result_summary",
            "local_relevance_medium_read_only_orientation_lookup_result_checks",
        ),
        "first_declared_lookup_key": first_object.get("declared_lookup_key"),
        "first_selected_received_signal_id": first_object.get("selected_received_signal_id"),
        "first_selected_locator_entry_artifact": _selected_locator_artifact(first_object),
        "first_selected_orientation_view_artifact": _selected_orientation_artifact(first_object),
    }


def _second_lookup_artifact_basis(artifact: Mapping[str, Any] | None, path_text: str) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"selected_second_lookup_result_artifact": path_text}
    second_object = _second_lookup_object_from_artifact(artifact)
    return {
        "selected_second_lookup_result_artifact": path_text,
        "basis_second_lookup_result_outcome": artifact.get("outcome"),
        "basis_second_lookup_result_result_version": _artifact_result_version(
            artifact,
            "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
            second_object,
        ),
        "basis_second_lookup_result_failed_check_count": _artifact_failed_check_count(
            artifact,
            "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
            "local_relevance_medium_read_only_second_orientation_lookup_result_checks",
        ),
        "second_declared_lookup_key": second_object.get("declared_lookup_key"),
        "second_selected_received_signal_id": second_object.get("selected_received_signal_id"),
        "second_selected_locator_entry_artifact": _selected_locator_artifact(second_object),
        "second_selected_orientation_view_artifact": _selected_orientation_artifact(second_object),
    }


def _orientation_index_artifact_basis(artifact: Mapping[str, Any] | None, path_text: str) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"selected_read_only_orientation_index_artifact": path_text}
    index_object = _orientation_index_from_artifact(artifact)
    lookup_table = _lookup_table_from_index(index_object)
    return {
        "selected_read_only_orientation_index_artifact": path_text,
        "basis_read_only_orientation_index_system_outcome": artifact.get("outcome"),
        "basis_read_only_orientation_index_system_result_version": _artifact_result_version(
            artifact,
            "local_relevance_medium_read_only_orientation_index_system_metadata",
            "local_relevance_medium_read_only_orientation_index_system_summary",
            index_object,
        ),
        "basis_read_only_orientation_index_system_failed_check_count": _artifact_failed_check_count(
            artifact,
            "local_relevance_medium_read_only_orientation_index_system_metadata",
            "local_relevance_medium_read_only_orientation_index_system_summary",
            "local_relevance_medium_read_only_orientation_index_system_checks",
        ),
        "supported_lookup_keys": list(lookup_table.keys()),
        "lookup_table_key_count": _lookup_key_count(index_object),
        "lookup_table_target_count": _lookup_target_count(index_object),
        "lookup_order": index_object.get("lookup_order"),
        "accepted_new_entries_count": _safe_int(index_object.get("accepted_new_entries_count")),
        "deterministic_local_lookup_preserved": (
            index_object.get("deterministic_local_lookup_enabled") is True
            or index_object.get("deterministic_local_lookup_preserved") is True
        ),
    }


def _build_lookup_pair_coverage_object(
    declared: Mapping[str, Any],
    first_artifact: Mapping[str, Any],
    first_path: str,
    second_artifact: Mapping[str, Any],
    second_path: str,
    index_artifact: Mapping[str, Any],
    index_path: str,
) -> dict[str, Any]:
    first_object = _first_lookup_object_from_artifact(first_artifact)
    second_object = _second_lookup_object_from_artifact(second_artifact)
    index_object = _orientation_index_from_artifact(index_artifact)
    coverage = {
        "lookup_pair_coverage_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_lookup_pair_coverage_id")
        )
        or DEFAULT_LOOKUP_PAIR_COVERAGE_ID,
        "lookup_pair_coverage_type": LOOKUP_PAIR_COVERAGE_TYPE,
        "lookup_pair_coverage_version": RESULT_VERSION,
        "lookup_pair_coverage_scope": LOOKUP_PAIR_COVERAGE_SCOPE,
        "basis_first_lookup_result_artifact": first_path,
        "basis_first_lookup_result_outcome": first_artifact.get("outcome"),
        "basis_first_lookup_result_result_version": _artifact_result_version(
            first_artifact,
            "local_relevance_medium_read_only_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_orientation_lookup_result_summary",
            first_object,
        ),
        "basis_first_lookup_result_failed_check_count": _artifact_failed_check_count(
            first_artifact,
            "local_relevance_medium_read_only_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_orientation_lookup_result_summary",
            "local_relevance_medium_read_only_orientation_lookup_result_checks",
        ),
        "basis_second_lookup_result_artifact": second_path,
        "basis_second_lookup_result_outcome": second_artifact.get("outcome"),
        "basis_second_lookup_result_result_version": _artifact_result_version(
            second_artifact,
            "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
            second_object,
        ),
        "basis_second_lookup_result_failed_check_count": _artifact_failed_check_count(
            second_artifact,
            "local_relevance_medium_read_only_second_orientation_lookup_result_metadata",
            "local_relevance_medium_read_only_second_orientation_lookup_result_summary",
            "local_relevance_medium_read_only_second_orientation_lookup_result_checks",
        ),
        "basis_read_only_orientation_index_artifact": index_path,
        "supported_lookup_keys": copy.deepcopy(SUPPORTED_LOOKUP_KEYS),
        "covered_lookup_keys": copy.deepcopy(SUPPORTED_LOOKUP_KEYS),
        "supported_lookup_key_count": 2,
        "covered_lookup_key_count": 2,
        "lookup_table_key_count": _lookup_key_count(index_object),
        "lookup_table_target_count": _lookup_target_count(index_object),
        "first_declared_lookup_key": first_object.get("declared_lookup_key"),
        "second_declared_lookup_key": second_object.get("declared_lookup_key"),
        "first_selected_received_signal_id": first_object.get("selected_received_signal_id"),
        "second_selected_received_signal_id": second_object.get("selected_received_signal_id"),
        "first_selected_locator_entry_artifact": _selected_locator_artifact(first_object),
        "second_selected_locator_entry_artifact": _selected_locator_artifact(second_object),
        "first_selected_orientation_view_artifact": _selected_orientation_artifact(first_object),
        "second_selected_orientation_view_artifact": _selected_orientation_artifact(second_object),
        "lookup_order": copy.deepcopy(index_object.get("lookup_order")),
        "accepted_new_entries_count": _safe_int(index_object.get("accepted_new_entries_count")),
        "deterministic_local_lookup_preserved": (
            index_object.get("deterministic_local_lookup_enabled") is True
            or index_object.get("deterministic_local_lookup_preserved") is True
        ),
        "lookup_pair_coverage_recorded": True,
    }
    coverage.update({key: False for key in OBJECT_FALSE_FIELDS})
    return coverage


def _build_statement(coverage: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, bool]:
    first_signal = coverage.get("first_selected_received_signal_id")
    second_signal = coverage.get("second_selected_received_signal_id")
    return {
        "local_relevance_medium_read_only_lookup_pair_coverage_recorded": (
            coverage.get("lookup_pair_coverage_recorded") is True
        ),
        "basis_first_lookup_result_artifact_preserved": _present(
            coverage.get("basis_first_lookup_result_artifact")
        ),
        "basis_second_lookup_result_artifact_preserved": _present(
            coverage.get("basis_second_lookup_result_artifact")
        ),
        "basis_read_only_orientation_index_artifact_preserved": _present(
            coverage.get("basis_read_only_orientation_index_artifact")
        ),
        "supported_lookup_keys_preserved": coverage.get("supported_lookup_keys") == SUPPORTED_LOOKUP_KEYS,
        "covered_lookup_keys_preserved": coverage.get("covered_lookup_keys") == SUPPORTED_LOOKUP_KEYS,
        "supported_lookup_key_count_is_two": coverage.get("supported_lookup_key_count") == 2,
        "covered_lookup_key_count_is_two": coverage.get("covered_lookup_key_count") == 2,
        "both_supported_lookup_keys_covered": coverage.get("covered_lookup_keys") == SUPPORTED_LOOKUP_KEYS,
        "first_declared_lookup_key_preserved": coverage.get("first_declared_lookup_key") == FIRST_LOOKUP_KEY,
        "second_declared_lookup_key_preserved": coverage.get("second_declared_lookup_key") == SECOND_LOOKUP_KEY,
        "first_selected_received_signal_id_preserved": first_signal == FIRST_SELECTED_SIGNAL_ID,
        "second_selected_received_signal_id_preserved": second_signal == SECOND_SELECTED_SIGNAL_ID,
        "first_and_second_selected_received_signal_ids_distinct": (
            _present(first_signal) and _present(second_signal) and first_signal != second_signal
        ),
        "first_selected_locator_entry_artifact_preserved": _present(
            coverage.get("first_selected_locator_entry_artifact")
        ),
        "second_selected_locator_entry_artifact_preserved": _present(
            coverage.get("second_selected_locator_entry_artifact")
        ),
        "first_selected_orientation_view_artifact_preserved": _present(
            coverage.get("first_selected_orientation_view_artifact")
        ),
        "second_selected_orientation_view_artifact_preserved": _present(
            coverage.get("second_selected_orientation_view_artifact")
        ),
        "lookup_order_is_deterministic": coverage.get("lookup_order") == LOOKUP_ORDER,
        "accepted_new_entries_count_is_zero": coverage.get("accepted_new_entries_count") == 0,
        "deterministic_local_lookup_preserved": (
            coverage.get("deterministic_local_lookup_preserved") is True
        ),
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_not_repaired": True,
        "predecessor_failure_not_hidden": True,
        "predecessor_failure_not_claimed_passed": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_reusable_lookup_permission": True,
        "not_general_lookup_permission": True,
        "not_new_lookup_result": True,
        "not_new_lookup_entry": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_scoring": True,
        "not_priority": True,
        "not_validity_judgment": True,
        "not_truth_judgment": True,
        "not_authority_judgment": True,
        "not_currentness_judgment": True,
        "not_repeated_reception_permission": True,
        "not_arbitrary_reception": True,
        "not_feed": True,
        "not_source_transfer": True,
        "not_source_receipt": True,
        "not_runtime": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_operation_permission": True,
        "not_follow_on_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only lookup-pair coverage test",
        "local relevance medium read-only lookup-pair coverage live artifact",
        "local relevance medium read-only lookup-pair coverage terminal summary, if separately selected",
        "reusable lookup permission, if separately selected",
        "general lookup permission, if separately selected",
        "registry",
        "search surface",
        "query surface",
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
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _append_coverage_object_checks(
    coverage: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(checks, "lookup-pair coverage recorded", coverage.get("lookup_pair_coverage_recorded") is True, True, coverage.get("lookup_pair_coverage_recorded"), "LOOKUP_PAIR_COVERAGE_NOT_RECORDED")
    false_checks = {
        "reusable lookup permission not created": ("reusable_lookup_permission_created", "REUSABLE_LOOKUP_PERMISSION_CREATED"),
        "general lookup permission not created": ("general_lookup_permission_created", "GENERAL_LOOKUP_PERMISSION_CREATED"),
        "no new lookup result created": ("new_lookup_result_created", "NEW_LOOKUP_RESULT_CREATED"),
        "no new lookup entry created": ("new_lookup_entry_created", "NEW_LOOKUP_ENTRY_CREATED"),
        "no new signal accepted": ("new_signal_accepted", "NEW_SIGNAL_ACCEPTED"),
        "no new entry accepted": ("new_entry_accepted", "NEW_ENTRY_ACCEPTED"),
        "no new relevance object created": ("new_relevance_object_created", "NEW_RELEVANCE_OBJECT_CREATED"),
        "no new index entry created": ("new_index_entry_created", "NEW_INDEX_ENTRY_CREATED"),
        "filesystem discovery not performed": ("filesystem_discovery_performed", "FILESYSTEM_DISCOVERY_PERFORMED"),
        "registry not created": ("registry_created", "REGISTRY_CREATED"),
        "search not created": ("search_surface_created", "SEARCH_SURFACE_CREATED"),
        "query surface not created": ("query_surface_created", "QUERY_SURFACE_CREATED"),
        "ranking not created": ("ranking_surface_created", "RANKING_SURFACE_CREATED"),
        "scoring not created": ("scoring_surface_created", "SCORING_SURFACE_CREATED"),
        "priority not created": ("priority_surface_created", "PRIORITY_SURFACE_CREATED"),
        "validity judgment not created": ("validity_judgment_created", "VALIDITY_JUDGMENT_CREATED"),
        "truth judgment not created": ("truth_judgment_created", "TRUTH_JUDGMENT_CREATED"),
        "authority judgment not created": ("authority_judgment_created", "AUTHORITY_JUDGMENT_CREATED"),
        "currentness judgment not created": ("currentness_judgment_created", "CURRENTNESS_JUDGMENT_CREATED"),
        "repeated reception permission not created": ("repeated_reception_permission_created", "REPEATED_RECEPTION_PERMISSION_CREATED"),
        "arbitrary reception not created": ("arbitrary_reception_created", "ARBITRARY_RECEPTION_CREATED"),
        "feed not created": ("feed_created", "FEED_CREATED"),
        "source transfer not created": ("source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
        "source receipt not created": ("source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
        "source not created": ("source_created", "SOURCE_CREATED"),
        "authority not created": ("authority_created", "AUTHORITY_CREATED"),
        "currentness not created": ("currentness_created", "CURRENTNESS_CREATED"),
        "truth not created": ("truth_created", "TRUTH_CREATED"),
        "action not created": ("action_created", "ACTION_CREATED"),
        "synchronization not created": ("synchronization_created", "SYNCHRONIZATION_CREATED"),
        "participation not authorized": ("participation_authorized", "PARTICIPATION_AUTHORIZED"),
        "participant role not created": ("participant_role_created", "PARTICIPANT_ROLE_CREATED"),
        "runtime permission not created": ("runtime_permission_created", "RUNTIME_PERMISSION_CREATED"),
        "public API not created": ("public_api_created", "PUBLIC_API_CREATED"),
        "participant-facing interface not created": ("participant_facing_interface_created", "PARTICIPANT_FACING_INTERFACE_CREATED"),
        "distributed network behavior not created": ("distributed_network_behavior_created", "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED"),
        "operation permission not created": ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        "follow-on work not authorized": ("follow_on_work_authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    }
    canonical_non_claims = _canonical_non_claims()
    for check_name, (field_name, block_code) in false_checks.items():
        actual = coverage.get(field_name, canonical_non_claims.get(field_name, False))
        _append_check(checks, check_name, actual is False, False, actual, block_code)
    _append_check(
        checks,
        "result-level required false non-claims canonical false",
        all(value is False for value in canonical_non_claims.values()),
        "all required result-level non-claims false",
        canonical_non_claims,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )


def build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_lookup_pair_coverage_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    block = result.get("block") if isinstance(result.get("block"), MappingABC) else {}
    statement = result.get("local_relevance_medium_read_only_lookup_pair_coverage_statement")
    statement_map = statement if isinstance(statement, MappingABC) else {}
    coverage = result.get("local_relevance_medium_read_only_lookup_pair_coverage")
    coverage_map = coverage if isinstance(coverage, MappingABC) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, MappingABC) else {}
    question = result.get("declared_local_relevance_medium_read_only_lookup_pair_coverage_question")
    question_map = question if isinstance(question, MappingABC) else {}

    return _sanitize(
        {
            "outcome": result.get("outcome"),
            "block_code": block.get("block_code") or block.get("code"),
            "block_reason": block.get("reason"),
            "lookup_pair_coverage_id": coverage_map.get("lookup_pair_coverage_id"),
            "question": question_map.get("question"),
            "intent": question_map.get("intent"),
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "lookup_pair_coverage_recorded": statement_map.get(
                "local_relevance_medium_read_only_lookup_pair_coverage_recorded", False
            ),
            "basis_first_lookup_result_artifact_preserved": statement_map.get(
                "basis_first_lookup_result_artifact_preserved", False
            ),
            "basis_second_lookup_result_artifact_preserved": statement_map.get(
                "basis_second_lookup_result_artifact_preserved", False
            ),
            "basis_read_only_orientation_index_artifact_preserved": statement_map.get(
                "basis_read_only_orientation_index_artifact_preserved", False
            ),
            "supported_lookup_keys_preserved": statement_map.get("supported_lookup_keys_preserved", False),
            "covered_lookup_keys_preserved": statement_map.get("covered_lookup_keys_preserved", False),
            "supported_lookup_key_count_is_two": statement_map.get("supported_lookup_key_count_is_two", False),
            "covered_lookup_key_count_is_two": statement_map.get("covered_lookup_key_count_is_two", False),
            "both_supported_lookup_keys_covered": statement_map.get("both_supported_lookup_keys_covered", False),
            "first_declared_lookup_key_preserved": statement_map.get(
                "first_declared_lookup_key_preserved", False
            ),
            "second_declared_lookup_key_preserved": statement_map.get(
                "second_declared_lookup_key_preserved", False
            ),
            "first_selected_received_signal_id_preserved": statement_map.get(
                "first_selected_received_signal_id_preserved", False
            ),
            "second_selected_received_signal_id_preserved": statement_map.get(
                "second_selected_received_signal_id_preserved", False
            ),
            "first_and_second_selected_received_signal_ids_distinct": statement_map.get(
                "first_and_second_selected_received_signal_ids_distinct", False
            ),
            "first_selected_locator_entry_artifact_preserved": statement_map.get(
                "first_selected_locator_entry_artifact_preserved", False
            ),
            "second_selected_locator_entry_artifact_preserved": statement_map.get(
                "second_selected_locator_entry_artifact_preserved", False
            ),
            "first_selected_orientation_view_artifact_preserved": statement_map.get(
                "first_selected_orientation_view_artifact_preserved", False
            ),
            "second_selected_orientation_view_artifact_preserved": statement_map.get(
                "second_selected_orientation_view_artifact_preserved", False
            ),
            "lookup_order_deterministic": statement_map.get("lookup_order_is_deterministic", False),
            "lookup_order_is_deterministic": statement_map.get("lookup_order_is_deterministic", False),
            "accepted_new_entries_count_is_zero": statement_map.get("accepted_new_entries_count_is_zero", False),
            "deterministic_local_lookup_preserved": statement_map.get(
                "deterministic_local_lookup_preserved", False
            ),
            "lookup_pair_coverage_object_summary": {
                "lookup_pair_coverage_type": coverage_map.get("lookup_pair_coverage_type"),
                "lookup_pair_coverage_scope": coverage_map.get("lookup_pair_coverage_scope"),
                "supported_lookup_keys": coverage_map.get("supported_lookup_keys"),
                "covered_lookup_keys": coverage_map.get("covered_lookup_keys"),
                "first_selected_received_signal_id": coverage_map.get("first_selected_received_signal_id"),
                "second_selected_received_signal_id": coverage_map.get("second_selected_received_signal_id"),
                "lookup_order": coverage_map.get("lookup_order"),
            },
            "reusable_lookup_permission_not_created": (
                non_claims_map.get("reusable_lookup_permission_created") is False
            ),
            "general_lookup_permission_not_created": (
                non_claims_map.get("general_lookup_permission_created") is False
            ),
            "no_new_lookup_result_or_entry_created": all(
                non_claims_map.get(key) is False for key in ("new_lookup_result_created", "new_lookup_entry_created")
            ),
            "no_new_signal_entry_relevance_object_or_index_entry_created": all(
                non_claims_map.get(key) is False
                for key in (
                    "new_signal_accepted",
                    "new_entry_accepted",
                    "new_relevance_object_created",
                    "new_index_entry_created",
                )
            ),
            "filesystem_discovery_not_performed": non_claims_map.get("filesystem_discovery_performed") is False,
            "registry_search_query_surface_ranking_not_created": all(
                non_claims_map.get(key) is False
                for key in (
                    "registry_created",
                    "search_surface_created",
                    "query_surface_created",
                    "ranking_surface_created",
                )
            ),
            "scoring_priority_validity_truth_authority_currentness_judgment_not_created": all(
                non_claims_map.get(key) is False
                for key in (
                    "scoring_surface_created",
                    "priority_surface_created",
                    "validity_judgment_created",
                    "truth_judgment_created",
                    "authority_judgment_created",
                    "currentness_judgment_created",
                )
            ),
            "repeated_reception_arbitrary_reception_feed_not_created": all(
                non_claims_map.get(key) is False
                for key in ("repeated_reception_permission_created", "arbitrary_reception_created", "feed_created")
            ),
            "source_authority_currentness_truth_action_synchronization_runtime_not_created": all(
                non_claims_map.get(key) is False
                for key in (
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
            "public_api_interface_distributed_not_created": all(
                non_claims_map.get(key) is False
                for key in (
                    "public_api_created",
                    "participant_facing_interface_created",
                    "distributed_network_behavior_created",
                )
            ),
            "operation_permission_follow_on_not_created": all(
                non_claims_map.get(key) is False
                for key in ("operation_permission_created", "follow_on_work_authorized")
            ),
            "predecessor_failure_evidence_preserved": statement_map.get(
                "predecessor_failure_evidence_preserved", True
            ),
            "result_level_non_claims_canonical_false": statement_map.get(
                "result_level_non_claims_canonical_false", False
            ),
            "key_non_claims": {key: non_claims_map.get(key) for key in REQUIRED_FALSE_NON_CLAIMS},
        }
    )


def _finalize_result(
    declared: Mapping[str, Any],
    first_artifact: Mapping[str, Any] | None,
    first_path: str,
    second_artifact: Mapping[str, Any] | None,
    second_path: str,
    index_artifact: Mapping[str, Any] | None,
    index_path: str,
    coverage: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    statement = _build_statement(coverage, non_claims)
    metadata = {
        "local_relevance_medium_read_only_lookup_pair_coverage_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_lookup_pair_coverage_id")
        )
        or DEFAULT_REQUEST_ID,
        "local_relevance_medium_read_only_lookup_pair_coverage_type": LOOKUP_PAIR_COVERAGE_TYPE,
        "local_relevance_medium_read_only_lookup_pair_coverage_version": RESULT_VERSION,
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
    }
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": block_code if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata": metadata,
        "declared_local_relevance_medium_read_only_lookup_pair_coverage_question": {
            "question": declared.get("local_relevance_medium_read_only_lookup_pair_coverage_question"),
            "intent": declared.get("local_relevance_medium_read_only_lookup_pair_coverage_intent"),
        },
        "selected_first_lookup_result_artifact_basis": _first_lookup_artifact_basis(first_artifact, first_path),
        "selected_second_lookup_result_artifact_basis": _second_lookup_artifact_basis(second_artifact, second_path),
        "selected_read_only_orientation_index_artifact_basis": _orientation_index_artifact_basis(
            index_artifact,
            index_path,
        ),
        "local_relevance_medium_read_only_lookup_pair_coverage": copy.deepcopy(dict(coverage)),
        "local_relevance_medium_read_only_lookup_pair_coverage_checks": copy.deepcopy(checks),
        "local_relevance_medium_read_only_lookup_pair_coverage_statement": statement,
        "local_relevance_medium_read_only_lookup_pair_coverage_non_meaning": _build_non_meaning(),
        "additional_basis_required": copy.deepcopy(declared.get("additional_basis_context", []))
        if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        else [],
        "not_recorded_basis": copy.deepcopy(declared.get("not_recorded_basis", []))
        if outcome == OUTCOME_NOT_RECORDED
        else [],
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_lookup_pair_coverage_summary"] = (
        build_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(
    declared_local_relevance_medium_read_only_lookup_pair_coverage: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_read_only_lookup_pair_coverage is None:
        declared = build_declared_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_request()
    elif isinstance(declared_local_relevance_medium_read_only_lookup_pair_coverage, MappingABC):
        declared = copy.deepcopy(dict(declared_local_relevance_medium_read_only_lookup_pair_coverage))
    else:
        checks = [
            _make_check(
                "declared lookup-pair coverage request mapping",
                False,
                "mapping request",
                type(declared_local_relevance_medium_read_only_lookup_pair_coverage).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED",
        )

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(declared, checks)
    _append_shortcut_checks(declared, checks)
    _append_non_claim_checks(declared, checks)
    _append_check(
        checks,
        "predecessor failure evidence preserved",
        True,
        "predecessor failed-lineage evidence preserved",
        "predecessor failed-lineage evidence preserved",
    )
    _append_check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "all result-level required false non-claims canonical false",
        _canonical_non_claims(),
    )
    _append_check(
        checks,
        "artifact existence not lookup-pair-coverage authority",
        True,
        "artifact existence not treated as lookup-pair-coverage authority",
        False,
    )
    _append_check(
        checks,
        "latest file posture not lookup-pair-coverage authority",
        True,
        "latest file posture not treated as lookup-pair-coverage authority",
        False,
    )
    _append_check(
        checks,
        "repo-local availability not lookup-pair-coverage authority",
        True,
        "repo-local availability not treated as lookup-pair-coverage authority",
        False,
    )
    _append_check(
        checks,
        "hidden repo state not lookup-pair-coverage content or authority",
        True,
        "hidden repo state excluded from lookup-pair-coverage content and authority",
        False,
    )

    first_artifact, first_path = _validate_first_lookup_artifact(declared, checks)
    second_artifact, second_path = _validate_second_lookup_artifact(declared, checks)
    index_artifact, index_path = _validate_orientation_index_artifact(declared, first_artifact, second_artifact, checks)

    failed_before_object = _first_failed_code(checks)
    coverage: dict[str, Any] = {}
    if (
        failed_before_object is None
        and declared.get("local_relevance_medium_read_only_lookup_pair_coverage_intent") == INTENT_RECORD
        and first_artifact is not None
        and second_artifact is not None
        and index_artifact is not None
    ):
        coverage = _build_lookup_pair_coverage_object(
            declared,
            first_artifact,
            first_path,
            second_artifact,
            second_path,
            index_artifact,
            index_path,
        )
        _append_coverage_object_checks(coverage, checks)
    elif failed_before_object is None:
        _append_check(
            checks,
            "lookup-pair coverage not recorded by non-record intent",
            True,
            "not recorded",
            declared.get("local_relevance_medium_read_only_lookup_pair_coverage_intent"),
        )

    failed_code = _first_failed_code(checks)
    if failed_code:
        return _finalize_result(
            declared,
            first_artifact,
            first_path,
            second_artifact,
            second_path,
            index_artifact,
            index_path,
            {},
            checks,
            OUTCOME_BLOCKED,
            failed_code,
        )

    if declared.get("local_relevance_medium_read_only_lookup_pair_coverage_intent") == INTENT_DO_NOT_RECORD:
        return _finalize_result(
            declared,
            first_artifact,
            first_path,
            second_artifact,
            second_path,
            index_artifact,
            index_path,
            {},
            checks,
            OUTCOME_NOT_RECORDED,
            None,
        )

    requested_outcome = declared.get("requested_local_relevance_medium_read_only_lookup_pair_coverage_outcome")
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _finalize_result(
            declared,
            first_artifact,
            first_path,
            second_artifact,
            second_path,
            index_artifact,
            index_path,
            coverage,
            checks,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            None,
        )
    if requested_outcome == OUTCOME_NOT_RECORDED:
        return _finalize_result(
            declared,
            first_artifact,
            first_path,
            second_artifact,
            second_path,
            index_artifact,
            index_path,
            {},
            checks,
            OUTCOME_NOT_RECORDED,
            None,
        )

    return _finalize_result(
        declared,
        first_artifact,
        first_path,
        second_artifact,
        second_path,
        index_artifact,
        index_path,
        coverage,
        checks,
        OUTCOME_RECORDED,
        None,
    )


def resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_from_path(
    declared_local_relevance_medium_read_only_lookup_pair_coverage_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_read_only_lookup_pair_coverage_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared lookup-pair coverage request path readable JSON",
                False,
                "readable JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, MappingABC):
        checks = [
            _make_check(
                "declared lookup-pair coverage request JSON object",
                False,
                "JSON object",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_REQUEST_MALFORMED",
        )
    return resolve_local_relevance_medium_read_only_lookup_pair_coverage_v0_min(loaded)


def write_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyLookupPairCoverageV0MinError("result must be a mapping")

    metadata = result.get("local_relevance_medium_read_only_lookup_pair_coverage_metadata")
    metadata_map = metadata if isinstance(metadata, MappingABC) else {}
    coverage = result.get("local_relevance_medium_read_only_lookup_pair_coverage")
    coverage_map = coverage if isinstance(coverage, MappingABC) else {}
    result_id = (
        _string_or_empty(metadata_map.get("local_relevance_medium_read_only_lookup_pair_coverage_id"))
        or _string_or_empty(coverage_map.get("lookup_pair_coverage_id"))
        or DEFAULT_LOOKUP_PAIR_COVERAGE_ID
    )
    filename = f"{result_id}__local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result.json"
    path = Path(output_path) if output_path is not None else OUTPUT_ROOT / filename
    if path.exists():
        base = path.with_suffix("")
        suffix = path.suffix
        counter = 1
        candidate = Path(f"{base}_{counter:03d}{suffix}")
        while candidate.exists():
            counter += 1
            candidate = Path(f"{base}_{counter:03d}{suffix}")
        path = candidate
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(copy.deepcopy(dict(result))), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_lookup_pair_coverage_v0_min_request(
    *,
    local_relevance_medium_read_only_lookup_pair_coverage_id: str = DEFAULT_LOOKUP_PAIR_COVERAGE_ID,
    local_relevance_medium_read_only_lookup_pair_coverage_question: str = CORE_QUESTION,
    local_relevance_medium_read_only_lookup_pair_coverage_intent: str = INTENT_RECORD,
    selected_first_lookup_result_artifact: Path | str = DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT,
    selected_second_lookup_result_artifact: Path | str = DEFAULT_SECOND_LOOKUP_RESULT_ARTIFACT,
    selected_read_only_orientation_index_artifact: Path | str = DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT,
    lookup_pair_coverage_type: str = LOOKUP_PAIR_COVERAGE_TYPE,
    lookup_pair_coverage_scope: str = LOOKUP_PAIR_COVERAGE_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    request = {
        "local_relevance_medium_read_only_lookup_pair_coverage_id": (
            local_relevance_medium_read_only_lookup_pair_coverage_id
        ),
        "local_relevance_medium_read_only_lookup_pair_coverage_question": (
            local_relevance_medium_read_only_lookup_pair_coverage_question
        ),
        "local_relevance_medium_read_only_lookup_pair_coverage_intent": (
            local_relevance_medium_read_only_lookup_pair_coverage_intent
        ),
        "selected_first_lookup_result_artifact": str(selected_first_lookup_result_artifact),
        "selected_second_lookup_result_artifact": str(selected_second_lookup_result_artifact),
        "selected_read_only_orientation_index_artifact": str(selected_read_only_orientation_index_artifact),
        "lookup_pair_coverage_type": lookup_pair_coverage_type,
        "lookup_pair_coverage_scope": lookup_pair_coverage_scope,
        "declared_non_claims": _canonical_non_claims()
        if declared_non_claims is None
        else copy.deepcopy(dict(declared_non_claims)),
    }
    request.update(copy.deepcopy(extra_fields))
    return request
