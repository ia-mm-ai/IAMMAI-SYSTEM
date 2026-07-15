"""Resolve one local relevance medium read-only reusable lookup permission.

This resolver reads one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY artifact as
permission-consideration basis and one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE artifact as coverage
basis. It records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION object only.

The permission is read-only, local, bounded, and two-key-scope-only. It permits
repeated deterministic lookup only over ``first_orientation_locator`` and
``second_orientation_locator``. It does not create general lookup permission,
arbitrary lookup permission, unsupported-key permission, a new lookup result, a
new lookup entry, registry, search, query surface, ranking, scoring, priority,
validity judgment, truth judgment, authority judgment, currentness judgment,
repeated reception permission, arbitrary reception, feed, source transfer,
source receipt, runtime permission, public API, distributed behavior,
operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyReusableLookupPermissionV0MinError(Exception):
    """Bounded error for reusable read-only lookup permission request handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_v0_min"
)
DEFAULT_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min/"
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_reference_review_001__"
    "local_relevance_medium_read_only_reusable_lookup_permission_boundary_v0_min_result.json"
)
DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_lookup_pair_coverage_v0_min/"
    "local_relevance_medium_read_only_lookup_pair_coverage_reference_review_001__"
    "local_relevance_medium_read_only_lookup_pair_coverage_v0_min_result.json"
)

DEFAULT_PERMISSION_ID = "local_relevance_medium_read_only_reusable_lookup_permission_001"
DEFAULT_REQUEST_ID = DEFAULT_PERMISSION_ID

PERMISSION_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION"
PERMISSION_SCOPE = "REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY"
SUPPORTED_PERMISSION_TYPE_VALUES = (PERMISSION_TYPE,)
SUPPORTED_PERMISSION_SCOPE_VALUES = (PERMISSION_SCOPE,)

BOUNDARY_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY"
BOUNDARY_SCOPE = "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_CONSIDERATION_ONLY"
BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_RECORDED"
)
LOOKUP_PAIR_COVERAGE_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE_RECORDED"
)
LOOKUP_PAIR_COVERAGE_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE"

FIRST_LOOKUP_KEY = "first_orientation_locator"
SECOND_LOOKUP_KEY = "second_orientation_locator"
SUPPORTED_LOOKUP_KEYS = [FIRST_LOOKUP_KEY, SECOND_LOOKUP_KEY]

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BOUNDARY "
    "and one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_LOOKUP_PAIR_COVERAGE, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION be recorded that permits "
    "repeated read-only deterministic lookup over only the already-covered supported "
    "lookup keys, first_orientation_locator and second_orientation_locator, without "
    "creating general lookup permission, arbitrary lookup permission, new lookup result, "
    "new lookup entry, accepting new entries, accepting new signals, performing filesystem "
    "discovery, creating query surface, registry, search, ranking, scoring, priority, "
    "validity judgment, truth judgment, authority, currentness, action, synchronization, "
    "participation authorization, participant role, runtime permission, public API, "
    "participant-facing interface, distributed network behavior, operation permission, "
    "repeated reception permission, arbitrary reception, feed, source transfer, source "
    "receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_lookup_keys_permitted",
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
    "artifact_existence_treated_as_reusable_lookup_permission_authority",
    "latest_file_posture_treated_as_reusable_lookup_permission_authority",
    "repo_local_availability_treated_as_reusable_lookup_permission_authority",
    "hidden_repo_state_used_as_reusable_lookup_permission_content",
    "hidden_repo_state_used_as_reusable_lookup_permission_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

PERMISSION_OBJECT_FALSE_FIELDS = (
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_lookup_keys_permitted",
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
    "local_relevance_medium_read_only_reusable_lookup_permission_recorded",
    "basis_reusable_lookup_permission_boundary_artifact_preserved",
    "basis_lookup_pair_coverage_artifact_preserved",
    "supported_lookup_keys_preserved",
    "covered_lookup_keys_preserved",
    "permitted_lookup_keys_preserved",
    "supported_lookup_key_count_is_two",
    "covered_lookup_key_count_is_two",
    "permitted_lookup_key_count_is_two",
    "both_supported_lookup_keys_covered",
    "lookup_pair_coverage_recorded",
    "coverage_only_preserved",
    "boundary_recorded",
    "future_reusable_read_only_lookup_permission_was_considered",
    "reusable_read_only_lookup_permission_created",
    "reusable_read_only_lookup_permission_scope_bounded",
    "repeated_read_only_deterministic_lookup_permitted",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BLOCK_REQUESTED",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_PATH_MISSING",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_UNREADABLE",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_PATH_MISSING",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_UNREADABLE",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_NOT_JSON_OBJECT",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_NOT_RECORDED",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOOKUP_PAIR_COVERAGE_ARTIFACT_VERSION_NOT_0_1_0",
    "SUPPORTED_LOOKUP_KEYS_NOT_EXACT",
    "COVERED_LOOKUP_KEYS_NOT_EXACT",
    "PERMITTED_LOOKUP_KEYS_NOT_EXACT",
    "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "COVERED_LOOKUP_KEY_COUNT_NOT_TWO",
    "PERMITTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "BOTH_SUPPORTED_LOOKUP_KEYS_COVERED_NOT_TRUE",
    "LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
    "COVERAGE_ONLY_NOT_PRESERVED",
    "BOUNDARY_NOT_RECORDED",
    "FUTURE_REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CONSIDERED",
    "PERMISSION_TYPE_MISSING",
    "PERMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
    "PERMISSION_SCOPE_MISSING",
    "PERMISSION_SCOPE_NOT_REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
    "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CREATED",
    "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_SCOPE_NOT_BOUNDED",
    "REPEATED_READ_ONLY_DETERMINISTIC_LOOKUP_NOT_PERMITTED",
    "GENERAL_LOOKUP_PERMISSION_CREATED",
    "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_REUSABLE_LOOKUP_PERMISSION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BODY_MUST_NOT_RETURN",
    "RAW_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_BODY_MUST_NOT_RETURN",
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
    "raw_reusable_lookup_permission_body",
    "raw_reusable_lookup_permission_boundary_body",
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
    "reusable_lookup_permission_body",
    "reusable_lookup_permission_boundary_body",
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
        PERMISSION_TYPE,
        PERMISSION_SCOPE,
        BOUNDARY_TYPE,
        BOUNDARY_SCOPE,
        BOUNDARY_RECORDED_OUTCOME,
        LOOKUP_PAIR_COVERAGE_RECORDED_OUTCOME,
        LOOKUP_PAIR_COVERAGE_TYPE,
        FIRST_LOOKUP_KEY,
        SECOND_LOOKUP_KEY,
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
    "reusable_lookup_permission_boundary_artifact_missing": (
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_PATH_MISSING"
    ),
    "reusable_lookup_permission_boundary_artifact_not_recorded": (
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_NOT_RECORDED"
    ),
    "reusable_lookup_permission_boundary_artifact_failed_checks_present": (
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "reusable_lookup_permission_boundary_artifact_version_not_0_1_0": (
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "lookup_pair_coverage_artifact_missing": "LOOKUP_PAIR_COVERAGE_ARTIFACT_PATH_MISSING",
    "lookup_pair_coverage_artifact_not_recorded": "LOOKUP_PAIR_COVERAGE_ARTIFACT_NOT_RECORDED",
    "lookup_pair_coverage_artifact_failed_checks_present": (
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "lookup_pair_coverage_artifact_version_not_0_1_0": (
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "supported_lookup_keys_not_exact": "SUPPORTED_LOOKUP_KEYS_NOT_EXACT",
    "covered_lookup_keys_not_exact": "COVERED_LOOKUP_KEYS_NOT_EXACT",
    "permitted_lookup_keys_not_exact": "PERMITTED_LOOKUP_KEYS_NOT_EXACT",
    "supported_lookup_key_count_not_two": "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "covered_lookup_key_count_not_two": "COVERED_LOOKUP_KEY_COUNT_NOT_TWO",
    "permitted_lookup_key_count_not_two": "PERMITTED_LOOKUP_KEY_COUNT_NOT_TWO",
    "both_supported_lookup_keys_covered_not_true": "BOTH_SUPPORTED_LOOKUP_KEYS_COVERED_NOT_TRUE",
    "lookup_pair_coverage_not_recorded": "LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
    "coverage_only_not_preserved": "COVERAGE_ONLY_NOT_PRESERVED",
    "boundary_not_recorded": "BOUNDARY_NOT_RECORDED",
    "future_reusable_read_only_lookup_permission_not_considered": (
        "FUTURE_REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CONSIDERED"
    ),
    "permission_type_not_local_relevance_medium_read_only_reusable_lookup_permission": (
        "PERMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION"
    ),
    "permission_scope_not_reusable_read_only_lookup_over_covered_two_key_scope_only": (
        "PERMISSION_SCOPE_NOT_REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY"
    ),
    "reusable_read_only_lookup_permission_not_created": (
        "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CREATED"
    ),
    "reusable_read_only_lookup_permission_scope_not_bounded": (
        "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_SCOPE_NOT_BOUNDED"
    ),
    "repeated_read_only_deterministic_lookup_not_permitted": (
        "REPEATED_READ_ONLY_DETERMINISTIC_LOOKUP_NOT_PERMITTED"
    ),
    "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
    "arbitrary_lookup_permission_created": "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "unsupported_lookup_keys_permitted": "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
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
    "artifact_existence_treated_as_reusable_lookup_permission_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY"
    ),
    "latest_file_posture_treated_as_reusable_lookup_permission_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY"
    ),
    "repo_local_availability_treated_as_reusable_lookup_permission_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY"
    ),
    "hidden_repo_state_used_as_reusable_lookup_permission_content": (
        "HIDDEN_REPO_STATE_USED_AS_REUSABLE_LOOKUP_PERMISSION_CONTENT"
    ),
    "hidden_repo_state_used_as_reusable_lookup_permission_authority": (
        "HIDDEN_REPO_STATE_USED_AS_REUSABLE_LOOKUP_PERMISSION_AUTHORITY"
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
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED"
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


def _boundary_object_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_reusable_lookup_permission_boundary")
    return value if isinstance(value, MappingABC) else {}


def _coverage_object_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_lookup_pair_coverage")
    return value if isinstance(value, MappingABC) else {}


def _artifact_outcome(
    artifact: Mapping[str, Any],
    metadata_key: str,
    summary_key: str,
) -> str | None:
    metadata = _metadata(artifact, metadata_key)
    summary = _summary_mapping(artifact, summary_key)
    for source in (artifact, metadata, summary):
        value = source.get("outcome")
        if isinstance(value, str):
            return value
    return None


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
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_version",
        "local_relevance_medium_read_only_lookup_pair_coverage_version",
        "permission_version",
        "boundary_version",
        "lookup_pair_coverage_version",
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
        return sum(
            1
            for check in checks
            if isinstance(check, MappingABC) and check.get("passed") is not True
        )
    return None


def _read_json_artifact(
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


def _boundary_recorded(boundary_artifact: Mapping[str, Any], boundary: Mapping[str, Any]) -> bool:
    return (
        _artifact_outcome(
            boundary_artifact,
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        )
        == BOUNDARY_RECORDED_OUTCOME
        and boundary.get("boundary_type") == BOUNDARY_TYPE
        and boundary.get("boundary_scope") == BOUNDARY_SCOPE
        and boundary.get("future_reusable_read_only_lookup_permission_may_be_considered")
        is True
    )


def _boundary_future_considered(boundary_artifact: Mapping[str, Any], boundary: Mapping[str, Any]) -> bool:
    statement = boundary_artifact.get(
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_statement"
    )
    statement_map = statement if isinstance(statement, MappingABC) else {}
    return (
        boundary.get("future_reusable_read_only_lookup_permission_may_be_considered")
        is True
        or statement_map.get("future_reusable_read_only_lookup_permission_may_be_considered")
        is True
    )


def _coverage_only_preserved(coverage: Mapping[str, Any]) -> bool:
    required_false = (
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
    )
    return coverage.get("lookup_pair_coverage_recorded") is True and all(
        coverage.get(key) is False for key in required_false
    )


def _append_declared_request_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = declared.get("local_relevance_medium_read_only_reusable_lookup_permission_question")
    intent = declared.get("local_relevance_medium_read_only_reusable_lookup_permission_intent")
    permission_type = declared.get("permission_type")
    permission_scope = declared.get("permission_scope")

    _append_check(
        checks,
        "reusable lookup permission question declared",
        _present(question),
        "declared reusable lookup permission question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "permission intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "reusable lookup permission block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_BLOCK_REQUESTED",
        )
    _append_check(
        checks,
        "permission type declared",
        _present(permission_type),
        PERMISSION_TYPE,
        permission_type,
        "PERMISSION_TYPE_MISSING",
    )
    _append_check(
        checks,
        "permission type exact",
        permission_type == PERMISSION_TYPE,
        PERMISSION_TYPE,
        permission_type,
        "PERMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
    )
    _append_check(
        checks,
        "permission scope declared",
        _present(permission_scope),
        PERMISSION_SCOPE,
        permission_scope,
        "PERMISSION_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "permission scope reusable read-only lookup over covered two-key scope only",
        permission_scope == PERMISSION_SCOPE,
        PERMISSION_SCOPE,
        permission_scope,
        "PERMISSION_SCOPE_NOT_REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
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


def _validate_boundary_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_reusable_lookup_permission_boundary_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "reusable lookup permission boundary artifact path declared",
        _present(path_text),
        "selected reusable lookup permission boundary artifact path",
        path_text,
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_PATH_MISSING",
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_UNREADABLE",
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "reusable lookup permission boundary artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, path_text

    assert artifact is not None
    boundary = _boundary_object_from_artifact(artifact)
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        boundary,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks",
    )
    boundary_recorded = _boundary_recorded(artifact, boundary)
    future_considered = _boundary_future_considered(artifact, boundary)

    _append_check(
        checks,
        "reusable lookup permission boundary artifact readable JSON",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "reusable lookup permission boundary artifact outcome recorded",
        outcome == BOUNDARY_RECORDED_OUTCOME,
        BOUNDARY_RECORDED_OUTCOME,
        outcome,
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "reusable lookup permission boundary artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "reusable lookup permission boundary artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "boundary recorded true",
        boundary_recorded,
        True,
        boundary_recorded,
        "BOUNDARY_NOT_RECORDED",
    )
    _append_check(
        checks,
        "future reusable read-only lookup permission was considered",
        future_considered,
        True,
        future_considered,
        "FUTURE_REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CONSIDERED",
    )
    return artifact, path_text


def _validate_lookup_pair_coverage_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any] | None, str]:
    artifact_value = declared.get("selected_lookup_pair_coverage_artifact")
    path_text = _string_or_empty(artifact_value)
    _append_check(
        checks,
        "lookup-pair coverage artifact path declared",
        _present(path_text),
        "selected lookup-pair coverage artifact path",
        path_text,
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_PATH_MISSING",
    )
    artifact, read_code, path_text = _read_json_artifact(
        artifact_value,
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_PATH_MISSING",
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_UNREADABLE",
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_code:
        _append_check(
            checks,
            "lookup-pair coverage artifact readable JSON object",
            False,
            "readable JSON object",
            path_text or artifact_value,
            read_code,
        )
        return None, path_text

    assert artifact is not None
    coverage = _coverage_object_from_artifact(artifact)
    outcome = _artifact_outcome(
        artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
    )
    result_version = _artifact_result_version(
        artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
        coverage,
    )
    failed_count = _artifact_failed_check_count(
        artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
        "local_relevance_medium_read_only_lookup_pair_coverage_checks",
    )
    supported_keys = coverage.get("supported_lookup_keys")
    covered_keys = coverage.get("covered_lookup_keys")
    declared_permitted_keys = declared.get("permitted_lookup_keys", SUPPORTED_LOOKUP_KEYS)
    permitted_count = declared.get("permitted_lookup_key_count", 2)
    both_supported = (
        supported_keys == SUPPORTED_LOOKUP_KEYS
        and covered_keys == SUPPORTED_LOOKUP_KEYS
        and coverage.get("supported_lookup_key_count") == 2
        and coverage.get("covered_lookup_key_count") == 2
    )
    coverage_only = _coverage_only_preserved(coverage)

    _append_check(
        checks,
        "lookup-pair coverage artifact readable JSON",
        True,
        "readable JSON object",
        path_text,
    )
    _append_check(
        checks,
        "lookup-pair coverage artifact outcome recorded",
        outcome == LOOKUP_PAIR_COVERAGE_RECORDED_OUTCOME,
        LOOKUP_PAIR_COVERAGE_RECORDED_OUTCOME,
        outcome,
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "lookup-pair coverage artifact result version 0.1.0",
        result_version == RESULT_VERSION,
        RESULT_VERSION,
        result_version,
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "lookup-pair coverage artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "LOOKUP_PAIR_COVERAGE_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "supported lookup keys exact",
        supported_keys == SUPPORTED_LOOKUP_KEYS,
        SUPPORTED_LOOKUP_KEYS,
        supported_keys,
        "SUPPORTED_LOOKUP_KEYS_NOT_EXACT",
    )
    _append_check(
        checks,
        "covered lookup keys exact",
        covered_keys == SUPPORTED_LOOKUP_KEYS,
        SUPPORTED_LOOKUP_KEYS,
        covered_keys,
        "COVERED_LOOKUP_KEYS_NOT_EXACT",
    )
    _append_check(
        checks,
        "permitted lookup keys exact",
        declared_permitted_keys == SUPPORTED_LOOKUP_KEYS,
        SUPPORTED_LOOKUP_KEYS,
        declared_permitted_keys,
        "PERMITTED_LOOKUP_KEYS_NOT_EXACT",
    )
    _append_check(
        checks,
        "supported lookup key count exactly two",
        coverage.get("supported_lookup_key_count") == 2,
        2,
        coverage.get("supported_lookup_key_count"),
        "SUPPORTED_LOOKUP_KEY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "covered lookup key count exactly two",
        coverage.get("covered_lookup_key_count") == 2,
        2,
        coverage.get("covered_lookup_key_count"),
        "COVERED_LOOKUP_KEY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "permitted lookup key count exactly two",
        permitted_count == 2,
        2,
        permitted_count,
        "PERMITTED_LOOKUP_KEY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "both supported lookup keys covered true",
        both_supported,
        True,
        both_supported,
        "BOTH_SUPPORTED_LOOKUP_KEYS_COVERED_NOT_TRUE",
    )
    _append_check(
        checks,
        "lookup-pair coverage recorded true",
        coverage.get("lookup_pair_coverage_recorded") is True,
        True,
        coverage.get("lookup_pair_coverage_recorded"),
        "LOOKUP_PAIR_COVERAGE_NOT_RECORDED",
    )
    _append_check(
        checks,
        "coverage-only posture preserved",
        coverage_only,
        True,
        coverage_only,
        "COVERAGE_ONLY_NOT_PRESERVED",
    )
    return artifact, path_text


def _build_permission_object(
    declared: Mapping[str, Any],
    boundary_artifact: Mapping[str, Any],
    boundary_path: str,
    lookup_pair_coverage_artifact: Mapping[str, Any],
    lookup_pair_coverage_path: str,
) -> dict[str, Any]:
    boundary = _boundary_object_from_artifact(boundary_artifact)
    coverage = _coverage_object_from_artifact(lookup_pair_coverage_artifact)
    boundary_outcome = _artifact_outcome(
        boundary_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
    )
    boundary_version = _artifact_result_version(
        boundary_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        boundary,
    )
    boundary_failed_count = _artifact_failed_check_count(
        boundary_artifact,
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks",
    )
    coverage_outcome = _artifact_outcome(
        lookup_pair_coverage_artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
    )
    coverage_version = _artifact_result_version(
        lookup_pair_coverage_artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
        coverage,
    )
    coverage_failed_count = _artifact_failed_check_count(
        lookup_pair_coverage_artifact,
        "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
        "local_relevance_medium_read_only_lookup_pair_coverage_summary",
        "local_relevance_medium_read_only_lookup_pair_coverage_checks",
    )
    supported_keys = copy.deepcopy(coverage.get("supported_lookup_keys"))
    covered_keys = copy.deepcopy(coverage.get("covered_lookup_keys"))
    permission = {
        "permission_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_reusable_lookup_permission_id")
        )
        or DEFAULT_PERMISSION_ID,
        "permission_type": PERMISSION_TYPE,
        "permission_version": RESULT_VERSION,
        "permission_scope": PERMISSION_SCOPE,
        "basis_reusable_lookup_permission_boundary_artifact": boundary_path,
        "basis_reusable_lookup_permission_boundary_outcome": boundary_outcome,
        "basis_reusable_lookup_permission_boundary_result_version": boundary_version,
        "basis_reusable_lookup_permission_boundary_failed_check_count": boundary_failed_count,
        "basis_lookup_pair_coverage_artifact": lookup_pair_coverage_path,
        "basis_lookup_pair_coverage_outcome": coverage_outcome,
        "basis_lookup_pair_coverage_result_version": coverage_version,
        "basis_lookup_pair_coverage_failed_check_count": coverage_failed_count,
        "supported_lookup_keys": supported_keys,
        "covered_lookup_keys": covered_keys,
        "permitted_lookup_keys": copy.deepcopy(SUPPORTED_LOOKUP_KEYS),
        "supported_lookup_key_count": coverage.get("supported_lookup_key_count"),
        "covered_lookup_key_count": coverage.get("covered_lookup_key_count"),
        "permitted_lookup_key_count": 2,
        "both_supported_lookup_keys_covered": (
            supported_keys == SUPPORTED_LOOKUP_KEYS
            and covered_keys == SUPPORTED_LOOKUP_KEYS
            and coverage.get("supported_lookup_key_count") == 2
            and coverage.get("covered_lookup_key_count") == 2
        ),
        "lookup_pair_coverage_recorded": coverage.get("lookup_pair_coverage_recorded") is True,
        "coverage_only_preserved": _coverage_only_preserved(coverage),
        "boundary_recorded": _boundary_recorded(boundary_artifact, boundary),
        "future_reusable_read_only_lookup_permission_was_considered": _boundary_future_considered(
            boundary_artifact,
            boundary,
        ),
        "reusable_read_only_lookup_permission_created": True,
        "reusable_read_only_lookup_permission_scope_bounded": True,
        "repeated_read_only_deterministic_lookup_permitted": True,
    }
    permission.update({key: False for key in PERMISSION_OBJECT_FALSE_FIELDS})
    return permission


def _build_statement(permission: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_reusable_lookup_permission_recorded": (
            permission.get("permission_type") == PERMISSION_TYPE
            and permission.get("permission_scope") == PERMISSION_SCOPE
            and permission.get("reusable_read_only_lookup_permission_created") is True
        ),
        "basis_reusable_lookup_permission_boundary_artifact_preserved": _present(
            permission.get("basis_reusable_lookup_permission_boundary_artifact")
        ),
        "basis_lookup_pair_coverage_artifact_preserved": _present(
            permission.get("basis_lookup_pair_coverage_artifact")
        ),
        "supported_lookup_keys_preserved": (
            permission.get("supported_lookup_keys") == SUPPORTED_LOOKUP_KEYS
        ),
        "covered_lookup_keys_preserved": (
            permission.get("covered_lookup_keys") == SUPPORTED_LOOKUP_KEYS
        ),
        "permitted_lookup_keys_preserved": (
            permission.get("permitted_lookup_keys") == SUPPORTED_LOOKUP_KEYS
        ),
        "supported_lookup_key_count_is_two": permission.get("supported_lookup_key_count") == 2,
        "covered_lookup_key_count_is_two": permission.get("covered_lookup_key_count") == 2,
        "permitted_lookup_key_count_is_two": permission.get("permitted_lookup_key_count") == 2,
        "both_supported_lookup_keys_covered": (
            permission.get("both_supported_lookup_keys_covered") is True
        ),
        "lookup_pair_coverage_recorded": permission.get("lookup_pair_coverage_recorded") is True,
        "coverage_only_preserved": permission.get("coverage_only_preserved") is True,
        "boundary_recorded": permission.get("boundary_recorded") is True,
        "future_reusable_read_only_lookup_permission_was_considered": (
            permission.get("future_reusable_read_only_lookup_permission_was_considered") is True
        ),
        "reusable_read_only_lookup_permission_created": (
            permission.get("reusable_read_only_lookup_permission_created") is True
        ),
        "reusable_read_only_lookup_permission_scope_bounded": (
            permission.get("reusable_read_only_lookup_permission_scope_bounded") is True
        ),
        "repeated_read_only_deterministic_lookup_permitted": (
            permission.get("repeated_read_only_deterministic_lookup_permitted") is True
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_unsupported_key_permission": True,
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
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_operation_permission": True,
        "not_follow_on_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only reusable lookup permission test",
        "local relevance medium read-only reusable lookup permission live artifact",
        "local relevance medium read-only reusable lookup permission terminal summary, if needed",
        "general lookup permission",
        "registry",
        "search surface",
        "query surface",
        "ranking surface",
        "source transfer",
        "source receipt",
        "derivative reception",
        "vessel relation",
        "adoption",
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
        "receiving-context governance",
        "deployment",
        "public release",
        "publication flow",
        "broader reusable permission",
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def _boundary_artifact_basis(artifact: Mapping[str, Any] | None, path_text: str) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"artifact": path_text or None, "readable": False}
    boundary = _boundary_object_from_artifact(artifact)
    return {
        "artifact": path_text,
        "readable": True,
        "outcome": _artifact_outcome(
            artifact,
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
        ),
        "result_version": _artifact_result_version(
            artifact,
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
            boundary,
        ),
        "failed_check_count": _artifact_failed_check_count(
            artifact,
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_metadata",
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_summary",
            "local_relevance_medium_read_only_reusable_lookup_permission_boundary_checks",
        ),
        "boundary_recorded": _boundary_recorded(artifact, boundary),
        "future_reusable_read_only_lookup_permission_was_considered": _boundary_future_considered(
            artifact,
            boundary,
        ),
        "supported_lookup_keys": copy.deepcopy(boundary.get("supported_lookup_keys")),
        "covered_lookup_keys": copy.deepcopy(boundary.get("covered_lookup_keys")),
    }


def _lookup_pair_coverage_artifact_basis(
    artifact: Mapping[str, Any] | None,
    path_text: str,
) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"artifact": path_text or None, "readable": False}
    coverage = _coverage_object_from_artifact(artifact)
    return {
        "artifact": path_text,
        "readable": True,
        "outcome": _artifact_outcome(
            artifact,
            "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
            "local_relevance_medium_read_only_lookup_pair_coverage_summary",
        ),
        "result_version": _artifact_result_version(
            artifact,
            "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
            "local_relevance_medium_read_only_lookup_pair_coverage_summary",
            coverage,
        ),
        "failed_check_count": _artifact_failed_check_count(
            artifact,
            "local_relevance_medium_read_only_lookup_pair_coverage_metadata",
            "local_relevance_medium_read_only_lookup_pair_coverage_summary",
            "local_relevance_medium_read_only_lookup_pair_coverage_checks",
        ),
        "supported_lookup_keys": copy.deepcopy(coverage.get("supported_lookup_keys")),
        "covered_lookup_keys": copy.deepcopy(coverage.get("covered_lookup_keys")),
        "lookup_pair_coverage_recorded": coverage.get("lookup_pair_coverage_recorded") is True,
        "coverage_only_preserved": _coverage_only_preserved(coverage),
    }


def _append_permission_object_checks(permission: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    checks_to_add = (
        (
            "permission type exact",
            permission.get("permission_type") == PERMISSION_TYPE,
            PERMISSION_TYPE,
            permission.get("permission_type"),
            "PERMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION",
        ),
        (
            "permission scope exact",
            permission.get("permission_scope") == PERMISSION_SCOPE,
            PERMISSION_SCOPE,
            permission.get("permission_scope"),
            "PERMISSION_SCOPE_NOT_REUSABLE_READ_ONLY_LOOKUP_OVER_COVERED_TWO_KEY_SCOPE_ONLY",
        ),
        (
            "reusable read-only lookup permission created",
            permission.get("reusable_read_only_lookup_permission_created") is True,
            True,
            permission.get("reusable_read_only_lookup_permission_created"),
            "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_NOT_CREATED",
        ),
        (
            "reusable read-only lookup permission scope bounded",
            permission.get("reusable_read_only_lookup_permission_scope_bounded") is True,
            True,
            permission.get("reusable_read_only_lookup_permission_scope_bounded"),
            "REUSABLE_READ_ONLY_LOOKUP_PERMISSION_SCOPE_NOT_BOUNDED",
        ),
        (
            "repeated read-only deterministic lookup permitted",
            permission.get("repeated_read_only_deterministic_lookup_permitted") is True,
            True,
            permission.get("repeated_read_only_deterministic_lookup_permitted"),
            "REPEATED_READ_ONLY_DETERMINISTIC_LOOKUP_NOT_PERMITTED",
        ),
        (
            "permitted lookup keys exact",
            permission.get("permitted_lookup_keys") == SUPPORTED_LOOKUP_KEYS,
            SUPPORTED_LOOKUP_KEYS,
            permission.get("permitted_lookup_keys"),
            "PERMITTED_LOOKUP_KEYS_NOT_EXACT",
        ),
        (
            "permitted lookup key count exactly two",
            permission.get("permitted_lookup_key_count") == 2,
            2,
            permission.get("permitted_lookup_key_count"),
            "PERMITTED_LOOKUP_KEY_COUNT_NOT_TWO",
        ),
    )
    for check_name, passed, expected, actual, code in checks_to_add:
        _append_check(checks, check_name, passed, expected, actual, code)

    false_code_by_field = {
        "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
        "arbitrary_lookup_permission_created": "ARBITRARY_LOOKUP_PERMISSION_CREATED",
        "unsupported_lookup_keys_permitted": "UNSUPPORTED_LOOKUP_KEYS_PERMITTED",
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
        "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    }
    for field_name, block_code in false_code_by_field.items():
        _append_check(
            checks,
            f"{field_name} false",
            permission.get(field_name) is False,
            False,
            permission.get(field_name),
            block_code,
        )

    for field_name, block_code in (
        ("source_created", "SOURCE_CREATED"),
        ("deployment_created", "DEPLOYMENT_CREATED"),
        ("public_release_created", "PUBLIC_RELEASE_CREATED"),
        ("operation_permission_created", "OPERATION_PERMISSION_CREATED"),
        ("broader_reusable_permission_created", "BROADER_REUSABLE_PERMISSION_CREATED"),
    ):
        _append_check(checks, f"{field_name} false", True, False, False, block_code)


def _finalize_result(
    declared: Mapping[str, Any],
    boundary_artifact: Mapping[str, Any] | None,
    boundary_path: str,
    lookup_pair_coverage_artifact: Mapping[str, Any] | None,
    lookup_pair_coverage_path: str,
    permission: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    statement = _build_statement(permission, non_claims)
    metadata = {
        "local_relevance_medium_read_only_reusable_lookup_permission_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_reusable_lookup_permission_id")
        )
        or DEFAULT_REQUEST_ID,
        "local_relevance_medium_read_only_reusable_lookup_permission_type": PERMISSION_TYPE,
        "local_relevance_medium_read_only_reusable_lookup_permission_version": RESULT_VERSION,
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
        "local_relevance_medium_read_only_reusable_lookup_permission_metadata": metadata,
        "declared_local_relevance_medium_read_only_reusable_lookup_permission_question": {
            "question": declared.get(
                "local_relevance_medium_read_only_reusable_lookup_permission_question"
            ),
            "intent": declared.get(
                "local_relevance_medium_read_only_reusable_lookup_permission_intent"
            ),
        },
        "selected_reusable_lookup_permission_boundary_artifact_basis": _boundary_artifact_basis(
            boundary_artifact,
            boundary_path,
        ),
        "selected_lookup_pair_coverage_artifact_basis": _lookup_pair_coverage_artifact_basis(
            lookup_pair_coverage_artifact,
            lookup_pair_coverage_path,
        ),
        "local_relevance_medium_read_only_reusable_lookup_permission": copy.deepcopy(
            dict(permission)
        ),
        "local_relevance_medium_read_only_reusable_lookup_permission_checks": copy.deepcopy(checks),
        "local_relevance_medium_read_only_reusable_lookup_permission_statement": statement,
        "local_relevance_medium_read_only_reusable_lookup_permission_non_meaning": (
            _build_non_meaning()
        ),
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
    result["local_relevance_medium_read_only_reusable_lookup_permission_summary"] = (
        build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(
    declared_local_relevance_medium_read_only_reusable_lookup_permission: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_read_only_reusable_lookup_permission is None:
        declared = build_declared_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_request()
    elif isinstance(declared_local_relevance_medium_read_only_reusable_lookup_permission, MappingABC):
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_reusable_lookup_permission)
        )
    else:
        checks = [
            _make_check(
                "declared reusable lookup permission request mapping",
                False,
                "mapping request",
                type(declared_local_relevance_medium_read_only_reusable_lookup_permission).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED",
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
        "artifact existence not reusable-lookup-permission authority",
        True,
        "artifact existence not treated as reusable-lookup-permission authority",
        False,
    )
    _append_check(
        checks,
        "latest file posture not reusable-lookup-permission authority",
        True,
        "latest file posture not treated as reusable-lookup-permission authority",
        False,
    )
    _append_check(
        checks,
        "repo-local availability not reusable-lookup-permission authority",
        True,
        "repo-local availability not treated as reusable-lookup-permission authority",
        False,
    )
    _append_check(
        checks,
        "hidden repo state not reusable-lookup-permission content or authority",
        True,
        "hidden repo state excluded from reusable-lookup-permission content and authority",
        False,
    )

    boundary_artifact, boundary_path = _validate_boundary_artifact(declared, checks)
    lookup_pair_coverage_artifact, lookup_pair_coverage_path = _validate_lookup_pair_coverage_artifact(
        declared,
        checks,
    )

    failed_before_object = _first_failed_code(checks)
    permission: dict[str, Any] = {}
    if (
        failed_before_object is None
        and declared.get("local_relevance_medium_read_only_reusable_lookup_permission_intent")
        == INTENT_RECORD
        and boundary_artifact is not None
        and lookup_pair_coverage_artifact is not None
    ):
        permission = _build_permission_object(
            declared,
            boundary_artifact,
            boundary_path,
            lookup_pair_coverage_artifact,
            lookup_pair_coverage_path,
        )
        _append_permission_object_checks(permission, checks)
    elif failed_before_object is None:
        _append_check(
            checks,
            "reusable lookup permission not recorded by non-record intent",
            True,
            "not recorded",
            declared.get("local_relevance_medium_read_only_reusable_lookup_permission_intent"),
        )

    failed_code = _first_failed_code(checks)
    if failed_code:
        return _finalize_result(
            declared,
            boundary_artifact,
            boundary_path,
            lookup_pair_coverage_artifact,
            lookup_pair_coverage_path,
            permission,
            checks,
            OUTCOME_BLOCKED,
            failed_code,
        )

    requested_outcome = declared.get(
        "requested_local_relevance_medium_read_only_reusable_lookup_permission_outcome"
    )
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return _finalize_result(
            declared,
            boundary_artifact,
            boundary_path,
            lookup_pair_coverage_artifact,
            lookup_pair_coverage_path,
            permission,
            checks,
            OUTCOME_REQUIRES_ADDITIONAL_BASIS,
            None,
        )
    if requested_outcome == OUTCOME_NOT_RECORDED or declared.get(
        "local_relevance_medium_read_only_reusable_lookup_permission_intent"
    ) == INTENT_DO_NOT_RECORD:
        return _finalize_result(
            declared,
            boundary_artifact,
            boundary_path,
            lookup_pair_coverage_artifact,
            lookup_pair_coverage_path,
            {},
            checks,
            OUTCOME_NOT_RECORDED,
            None,
        )

    return _finalize_result(
        declared,
        boundary_artifact,
        boundary_path,
        lookup_pair_coverage_artifact,
        lookup_pair_coverage_path,
        permission,
        checks,
        OUTCOME_RECORDED,
        None,
    )


def resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_from_path(
    declared_local_relevance_medium_read_only_reusable_lookup_permission_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_read_only_reusable_lookup_permission_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared reusable lookup permission request path readable JSON",
                False,
                "readable JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_UNREADABLE",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, MappingABC):
        checks = [
            _make_check(
                "declared reusable lookup permission request JSON object",
                False,
                "JSON object",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED",
            )
        ]
        return _finalize_result(
            {},
            None,
            "",
            None,
            "",
            {},
            checks,
            OUTCOME_BLOCKED,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_REUSABLE_LOOKUP_PERMISSION_REQUEST_MALFORMED",
        )
    return resolve_local_relevance_medium_read_only_reusable_lookup_permission_v0_min(loaded)


def write_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyReusableLookupPermissionV0MinError(
            "result must be a mapping"
        )

    metadata = result.get("local_relevance_medium_read_only_reusable_lookup_permission_metadata")
    metadata_map = metadata if isinstance(metadata, MappingABC) else {}
    permission = result.get("local_relevance_medium_read_only_reusable_lookup_permission")
    permission_map = permission if isinstance(permission, MappingABC) else {}
    result_id = (
        _string_or_empty(
            metadata_map.get("local_relevance_medium_read_only_reusable_lookup_permission_id")
        )
        or _string_or_empty(permission_map.get("permission_id"))
        or DEFAULT_PERMISSION_ID
    )
    filename = (
        f"{result_id}__"
        "local_relevance_medium_read_only_reusable_lookup_permission_v0_min_result.json"
    )
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


def build_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_reusable_lookup_permission_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    metadata = result.get("local_relevance_medium_read_only_reusable_lookup_permission_metadata")
    metadata_map = metadata if isinstance(metadata, MappingABC) else {}
    permission = result.get("local_relevance_medium_read_only_reusable_lookup_permission")
    permission_map = permission if isinstance(permission, MappingABC) else {}
    statement = result.get("local_relevance_medium_read_only_reusable_lookup_permission_statement")
    statement_map = statement if isinstance(statement, MappingABC) else {}
    declared_question = result.get(
        "declared_local_relevance_medium_read_only_reusable_lookup_permission_question"
    )
    declared_map = declared_question if isinstance(declared_question, MappingABC) else {}
    block = result.get("block")
    block_map = block if isinstance(block, MappingABC) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, MappingABC) else {}

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code") or block_map.get("code"),
        "block_reason": block_map.get("reason"),
        "permission_id": _string_or_empty(permission_map.get("permission_id"))
        or _string_or_empty(
            metadata_map.get("local_relevance_medium_read_only_reusable_lookup_permission_id")
        ),
        "question": declared_map.get("question"),
        "intent": declared_map.get("intent"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": metadata_map.get(
            "local_relevance_medium_read_only_reusable_lookup_permission_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata_map.get("resolver_module", RESOLVER_MODULE),
        "local_relevance_medium_read_only_reusable_lookup_permission_recorded": (
            statement_map.get("local_relevance_medium_read_only_reusable_lookup_permission_recorded")
            is True
        ),
        "basis_reusable_lookup_permission_boundary_artifact_preserved": (
            statement_map.get("basis_reusable_lookup_permission_boundary_artifact_preserved")
            is True
        ),
        "basis_lookup_pair_coverage_artifact_preserved": (
            statement_map.get("basis_lookup_pair_coverage_artifact_preserved") is True
        ),
        "supported_lookup_keys_preserved": (
            statement_map.get("supported_lookup_keys_preserved") is True
        ),
        "covered_lookup_keys_preserved": (
            statement_map.get("covered_lookup_keys_preserved") is True
        ),
        "permitted_lookup_keys_preserved": (
            statement_map.get("permitted_lookup_keys_preserved") is True
        ),
        "supported_lookup_key_count_is_two": (
            statement_map.get("supported_lookup_key_count_is_two") is True
        ),
        "covered_lookup_key_count_is_two": (
            statement_map.get("covered_lookup_key_count_is_two") is True
        ),
        "permitted_lookup_key_count_is_two": (
            statement_map.get("permitted_lookup_key_count_is_two") is True
        ),
        "both_supported_lookup_keys_covered": (
            statement_map.get("both_supported_lookup_keys_covered") is True
        ),
        "lookup_pair_coverage_recorded": (
            statement_map.get("lookup_pair_coverage_recorded") is True
        ),
        "coverage_only_preserved": statement_map.get("coverage_only_preserved") is True,
        "boundary_recorded": statement_map.get("boundary_recorded") is True,
        "future_reusable_read_only_lookup_permission_was_considered": (
            statement_map.get("future_reusable_read_only_lookup_permission_was_considered")
            is True
        ),
        "reusable_read_only_lookup_permission_created": (
            statement_map.get("reusable_read_only_lookup_permission_created") is True
        ),
        "reusable_read_only_lookup_permission_scope_bounded": (
            statement_map.get("reusable_read_only_lookup_permission_scope_bounded") is True
        ),
        "repeated_read_only_deterministic_lookup_permitted": (
            statement_map.get("repeated_read_only_deterministic_lookup_permitted") is True
        ),
        "permission_object_summary": {
            "permission_type": permission_map.get("permission_type"),
            "permission_scope": permission_map.get("permission_scope"),
            "basis_reusable_lookup_permission_boundary_artifact": permission_map.get(
                "basis_reusable_lookup_permission_boundary_artifact"
            ),
            "basis_lookup_pair_coverage_artifact": permission_map.get(
                "basis_lookup_pair_coverage_artifact"
            ),
            "permitted_lookup_keys": copy.deepcopy(permission_map.get("permitted_lookup_keys")),
        },
        "general_lookup_permission_not_created": (
            permission_map.get("general_lookup_permission_created") is False
        ),
        "arbitrary_lookup_permission_not_created": (
            permission_map.get("arbitrary_lookup_permission_created") is False
        ),
        "unsupported_lookup_keys_not_permitted": (
            permission_map.get("unsupported_lookup_keys_permitted") is False
        ),
        "no_new_lookup_result_or_entry_created": (
            permission_map.get("new_lookup_result_created") is False
            and permission_map.get("new_lookup_entry_created") is False
        ),
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            permission_map.get("new_signal_accepted") is False
            and permission_map.get("new_entry_accepted") is False
            and permission_map.get("new_relevance_object_created") is False
            and permission_map.get("new_index_entry_created") is False
        ),
        "filesystem_discovery_not_performed": (
            permission_map.get("filesystem_discovery_performed") is False
        ),
        "registry_search_query_surface_ranking_not_created": (
            permission_map.get("registry_created") is False
            and permission_map.get("search_surface_created") is False
            and permission_map.get("query_surface_created") is False
            and permission_map.get("ranking_surface_created") is False
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            permission_map.get("scoring_surface_created") is False
            and permission_map.get("priority_surface_created") is False
            and permission_map.get("validity_judgment_created") is False
            and permission_map.get("truth_judgment_created") is False
            and permission_map.get("authority_judgment_created") is False
            and permission_map.get("currentness_judgment_created") is False
        ),
        "repeated_reception_permission_arbitrary_reception_feed_not_created": (
            permission_map.get("repeated_reception_permission_created") is False
            and permission_map.get("arbitrary_reception_created") is False
            and permission_map.get("feed_created") is False
        ),
        "source_authority_currentness_truth_action_synchronization_participation_runtime_not_created": (
            non_claims_map.get("source_created") is False
            and permission_map.get("authority_created") is False
            and permission_map.get("currentness_created") is False
            and permission_map.get("truth_created") is False
            and permission_map.get("action_created") is False
            and permission_map.get("synchronization_created") is False
            and permission_map.get("participation_authorized") is False
            and permission_map.get("participant_role_created") is False
            and permission_map.get("runtime_permission_created") is False
        ),
        "public_api_participant_facing_interface_distributed_network_behavior_not_created": (
            permission_map.get("public_api_created") is False
            and permission_map.get("participant_facing_interface_created") is False
            and permission_map.get("distributed_network_behavior_created") is False
        ),
        "operation_permission_follow_on_not_created": (
            non_claims_map.get("operation_permission_created") is False
            and permission_map.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims_map.get(key)
            for key in (
                "general_lookup_permission_created",
                "arbitrary_lookup_permission_created",
                "unsupported_lookup_keys_permitted",
                "new_lookup_result_created",
                "new_lookup_entry_created",
                "filesystem_discovery_performed",
                "registry_created",
                "search_surface_created",
                "query_surface_created",
                "ranking_surface_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_not_repaired": non_claims_map.get("predecessor_failure_repaired")
        is False,
        "predecessor_failure_not_hidden": non_claims_map.get("predecessor_failure_hidden")
        is False,
        "predecessor_failure_not_claimed_passed": (
            non_claims_map.get("predecessor_failure_claimed_passed") is False
        ),
        "consumed_request_token_remains_closed": (
            non_claims_map.get("consumed_request_reopened") is False
        ),
        "authorization_token_reuse_blocked": (
            non_claims_map.get("authorization_token_reused") is False
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }
    return _sanitize(summary)


def build_declared_local_relevance_medium_read_only_reusable_lookup_permission_v0_min_request(
    *,
    local_relevance_medium_read_only_reusable_lookup_permission_id: str = DEFAULT_PERMISSION_ID,
    selected_reusable_lookup_permission_boundary_artifact: Path | str = (
        DEFAULT_REUSABLE_LOOKUP_PERMISSION_BOUNDARY_ARTIFACT
    ),
    selected_lookup_pair_coverage_artifact: Path | str = DEFAULT_LOOKUP_PAIR_COVERAGE_ARTIFACT,
    permission_type: str = PERMISSION_TYPE,
    permission_scope: str = PERMISSION_SCOPE,
    intent: str = INTENT_RECORD,
    question: str = CORE_QUESTION,
    permitted_lookup_keys: list[str] | tuple[str, ...] | None = None,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    request = {
        "local_relevance_medium_read_only_reusable_lookup_permission_id": (
            local_relevance_medium_read_only_reusable_lookup_permission_id
        ),
        "local_relevance_medium_read_only_reusable_lookup_permission_question": question,
        "local_relevance_medium_read_only_reusable_lookup_permission_intent": intent,
        "selected_reusable_lookup_permission_boundary_artifact": str(
            selected_reusable_lookup_permission_boundary_artifact
        ),
        "selected_lookup_pair_coverage_artifact": str(selected_lookup_pair_coverage_artifact),
        "permission_type": permission_type,
        "permission_scope": permission_scope,
        "permitted_lookup_keys": copy.deepcopy(
            list(permitted_lookup_keys) if permitted_lookup_keys is not None else SUPPORTED_LOOKUP_KEYS
        ),
        "permitted_lookup_key_count": 2
        if permitted_lookup_keys is None
        else len(list(permitted_lookup_keys)),
        "declared_non_claims": _canonical_non_claims()
        if declared_non_claims is None
        else copy.deepcopy(dict(declared_non_claims)),
    }
    request.update(copy.deepcopy(extra_fields))
    return request
