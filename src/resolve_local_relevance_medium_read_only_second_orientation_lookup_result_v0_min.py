"""Resolve one local relevance medium read-only second orientation lookup result.

This resolver reads one clean first read-only orientation lookup result artifact
as predecessor evidence and one clean local relevance medium read-only
orientation index artifact as deterministic lookup basis. It records one second
lookup result for the declared key ``second_orientation_locator`` only. It does
not create lookup-pair coverage, reusable lookup permission, registry, search,
query surface, ranking, scoring, priority, validity judgment, truth judgment,
authority judgment, currentness judgment, repeated reception permission,
arbitrary reception, feed, source transfer, source receipt, runtime permission,
public API, distributed behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlySecondOrientationLookupResultV0MinError(Exception):
    """Bounded error for second orientation lookup result path loading."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min"
)
DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min/"
    "local_relevance_medium_read_only_orientation_lookup_result_reference_review_001__"
    "local_relevance_medium_read_only_orientation_lookup_result_v0_min_result.json"
)
DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

DEFAULT_SECOND_LOOKUP_RESULT_ID = "local_relevance_medium_read_only_second_orientation_lookup_result_001"
DEFAULT_REQUEST_ID = DEFAULT_SECOND_LOOKUP_RESULT_ID

SECOND_LOOKUP_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
SECOND_LOOKUP_RESULT_SCOPE = "ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY"
SUPPORTED_SECOND_LOOKUP_RESULT_TYPE_VALUES = (SECOND_LOOKUP_RESULT_TYPE,)
SUPPORTED_SECOND_LOOKUP_RESULT_SCOPE_VALUES = (SECOND_LOOKUP_RESULT_SCOPE,)

FIRST_LOOKUP_RECORDED_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED"
ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED"
)
ORIENTATION_INDEX_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX"
ORIENTATION_INDEX_SYSTEM_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
ORIENTATION_INDEX_SCOPE = "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY"

FIRST_LOOKUP_EXPECTED_KEY = "first_orientation_locator"
REQUIRED_SECOND_LOOKUP_KEY = "second_orientation_locator"
LOOKUP_ORDER = [FIRST_LOOKUP_EXPECTED_KEY, REQUIRED_SECOND_LOOKUP_KEY]
FIRST_LOOKUP_EXPECTED_SIGNAL = "bounded_relevance_signal_001"
SECOND_LOOKUP_EXPECTED_SIGNAL = "bounded_relevance_signal_002"

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX and one clean first "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT be recorded for "
    "declared lookup key second_orientation_locator, returning exactly one already-standing "
    "second local orientation locator target, without creating reusable lookup permission, "
    "lookup-pair coverage, registry, search, ranking, scoring, priority, validity judgment, "
    "truth judgment, authority, currentness, action, synchronization, participation "
    "authorization, participant role, runtime permission, public API, participant-facing "
    "interface, distributed network behavior, operation permission, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "lookup_pair_coverage_created",
    "reusable_lookup_permission_created",
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
    "artifact_existence_treated_as_second_lookup_result_authority",
    "latest_file_posture_treated_as_second_lookup_result_authority",
    "repo_local_availability_treated_as_second_lookup_result_authority",
    "hidden_repo_state_used_as_second_lookup_result_content",
    "hidden_repo_state_used_as_second_lookup_result_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

OBJECT_FALSE_FIELDS = (
    "lookup_pair_coverage_created",
    "reusable_lookup_permission_created",
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
    "local_relevance_medium_read_only_second_orientation_lookup_result_recorded",
    "basis_first_lookup_result_artifact_preserved",
    "basis_read_only_orientation_index_artifact_preserved",
    "declared_lookup_key_preserved",
    "declared_lookup_key_is_second_orientation_locator",
    "lookup_key_supported",
    "lookup_target_found",
    "selected_received_signal_id_preserved",
    "selected_locator_entry_artifact_preserved",
    "selected_orientation_view_artifact_preserved",
    "lookup_table_has_two_entries",
    "lookup_order_is_deterministic",
    "lookup_key_count_is_two",
    "lookup_target_count_is_two",
    "accepted_new_entries_count_is_zero",
    "deterministic_local_lookup_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BLOCK_REQUESTED",
    "FIRST_LOOKUP_RESULT_ARTIFACT_PATH_MISSING",
    "FIRST_LOOKUP_RESULT_ARTIFACT_UNREADABLE",
    "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_JSON_OBJECT",
    "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    "FIRST_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "FIRST_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_UNREADABLE",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_JSON_OBJECT",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    "DECLARED_LOOKUP_KEY_MISSING",
    "DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR",
    "LOOKUP_TARGET_NOT_FOUND",
    "SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002",
    "SELECTED_SECOND_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "SELECTED_SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "SECOND_LOOKUP_RESULT_TYPE_MISSING",
    "SECOND_LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
    "SECOND_LOOKUP_RESULT_SCOPE_MISSING",
    "SECOND_LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
    "SECOND_LOOKUP_RESULT_NOT_RECORDED",
    "LOOKUP_PAIR_COVERAGE_CREATED",
    "REUSABLE_LOOKUP_PERMISSION_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_LOOKUP_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_LOOKUP_RESULT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
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

OFFICIAL_STRINGS = frozenset(
    (
        RESULT_VERSION,
        RESOLVER_MODULE,
        SECOND_LOOKUP_RESULT_TYPE,
        SECOND_LOOKUP_RESULT_SCOPE,
        FIRST_LOOKUP_RECORDED_OUTCOME,
        ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        ORIENTATION_INDEX_TYPE,
        ORIENTATION_INDEX_SYSTEM_TYPE,
        ORIENTATION_INDEX_SCOPE,
        FIRST_LOOKUP_EXPECTED_KEY,
        REQUIRED_SECOND_LOOKUP_KEY,
        FIRST_LOOKUP_EXPECTED_SIGNAL,
        SECOND_LOOKUP_EXPECTED_SIGNAL,
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
    "read_only_orientation_index_artifact_missing": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    "read_only_orientation_index_artifact_not_recorded": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    "read_only_orientation_index_artifact_failed_checks_present": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    "read_only_orientation_index_artifact_version_not_0_1_0": "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    "read_only_orientation_index_object_missing": "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    "declared_lookup_key_missing": "DECLARED_LOOKUP_KEY_MISSING",
    "declared_lookup_key_not_second_orientation_locator": "DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR",
    "lookup_target_not_found": "LOOKUP_TARGET_NOT_FOUND",
    "selected_received_signal_id_not_bounded_relevance_signal_002": "SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002",
    "selected_second_locator_entry_artifact_missing": "SELECTED_SECOND_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "selected_second_orientation_view_artifact_missing": "SELECTED_SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "lookup_table_not_two_entries": "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "lookup_table_target_count_not_two": "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "lookup_order_not_deterministic": "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "accepted_new_entries_count_not_zero": "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "deterministic_local_lookup_not_preserved": "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "second_lookup_result_type_not_local_relevance_medium_read_only_second_orientation_lookup_result": (
        "SECOND_LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT"
    ),
    "second_lookup_result_scope_not_one_declared_second_orientation_lookup_key_only": (
        "SECOND_LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY"
    ),
    "second_lookup_result_not_recorded": "SECOND_LOOKUP_RESULT_NOT_RECORDED",
    "lookup_pair_coverage_created": "LOOKUP_PAIR_COVERAGE_CREATED",
    "reusable_lookup_permission_created": "REUSABLE_LOOKUP_PERMISSION_CREATED",
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
    "artifact_existence_treated_as_second_lookup_result_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY"
    ),
    "latest_file_posture_treated_as_second_lookup_result_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY"
    ),
    "repo_local_availability_treated_as_second_lookup_result_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_LOOKUP_RESULT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_second_lookup_result_content": (
        "HIDDEN_REPO_STATE_USED_AS_SECOND_LOOKUP_RESULT_CONTENT"
    ),
    "hidden_repo_state_used_as_second_lookup_result_authority": (
        "HIDDEN_REPO_STATE_USED_AS_SECOND_LOOKUP_RESULT_AUTHORITY"
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
    return value if isinstance(value, str) else ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_int(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _is_sensitive_key(key: str) -> bool:
    key_lower = key.lower()
    return key_lower in SENSITIVE_CONTENT_KEYS or key_lower.endswith("_body")


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if isinstance(value, MappingABC):
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, str):
        if value in OFFICIAL_STRINGS:
            return value
        if parent_key and _is_sensitive_key(parent_key):
            return "[REDACTED_RAW_CONTENT]"
        if value in RAW_SENTINELS:
            return "[REDACTED_RAW_CONTENT]"
        return value
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
        check["block_code"] = code
        check["failure_code"] = code
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
    path = Path(path_text)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, unreadable_code, path_text
    if not isinstance(loaded, dict):
        return None, not_object_code, path_text
    return copy.deepcopy(loaded), None, path_text


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
        "local_relevance_medium_read_only_second_orientation_lookup_result_version",
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


def _orientation_index_from_artifact(artifact: Mapping[str, Any] | None) -> Mapping[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {}
    value = artifact.get("local_relevance_medium_read_only_orientation_index")
    return value if isinstance(value, MappingABC) else {}


def _lookup_table_from_index(index_object: Mapping[str, Any]) -> Mapping[str, Any]:
    table = index_object.get("lookup_table")
    return table if isinstance(table, MappingABC) else {}


def _target_for_second_key(index_object: Mapping[str, Any]) -> Mapping[str, Any]:
    target = _lookup_table_from_index(index_object).get(REQUIRED_SECOND_LOOKUP_KEY)
    return target if isinstance(target, MappingABC) else {}


def _target_received_signal_id(target: Mapping[str, Any]) -> str:
    for key in ("received_signal_id", "selected_received_signal_id", "signal_id"):
        value = target.get(key)
        if isinstance(value, str):
            return value
    return ""


def _target_locator_entry_artifact(target: Mapping[str, Any]) -> str:
    for key in (
        "locator_entry_artifact",
        "selected_locator_entry_artifact",
        "orientation_locator_entry_artifact",
        "local_orientation_locator_entry_artifact",
    ):
        value = target.get(key)
        if isinstance(value, str):
            return value
    return ""


def _target_orientation_view_artifact(target: Mapping[str, Any]) -> str:
    for key in ("orientation_view_artifact", "selected_orientation_view_artifact"):
        value = target.get(key)
        if isinstance(value, str):
            return value
    return ""


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


def _append_declared_request_checks(declared: Mapping[str, Any], checks: list[dict[str, Any]]) -> None:
    question = declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_question")
    intent = declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_intent")
    declared_key = declared.get("declared_lookup_key")
    second_lookup_result_type = declared.get("second_lookup_result_type")
    second_lookup_result_scope = declared.get("second_lookup_result_scope")

    _append_check(
        checks,
        "read-only second orientation lookup result question declared",
        _present(question),
        "declared read-only second orientation lookup result question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "read-only second orientation lookup result intent supported",
        intent in SUPPORTED_INTENTS,
        list(SUPPORTED_INTENTS),
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_INTENT_UNSUPPORTED",
    )
    if intent == INTENT_BLOCK:
        _append_check(
            checks,
            "read-only second orientation lookup result block intent not requested",
            False,
            f"not {INTENT_BLOCK}",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_BLOCK_REQUESTED",
        )
    _append_check(
        checks,
        "declared lookup key present",
        _present(declared_key),
        "declared second lookup key",
        declared_key,
        "DECLARED_LOOKUP_KEY_MISSING",
    )
    _append_check(
        checks,
        "declared lookup key is second orientation locator",
        declared_key == REQUIRED_SECOND_LOOKUP_KEY,
        REQUIRED_SECOND_LOOKUP_KEY,
        declared_key,
        "DECLARED_LOOKUP_KEY_NOT_SECOND_ORIENTATION_LOCATOR",
    )
    _append_check(
        checks,
        "second lookup result type declared",
        _present(second_lookup_result_type),
        SECOND_LOOKUP_RESULT_TYPE,
        second_lookup_result_type,
        "SECOND_LOOKUP_RESULT_TYPE_MISSING",
    )
    _append_check(
        checks,
        "second lookup result type exact",
        second_lookup_result_type == SECOND_LOOKUP_RESULT_TYPE,
        SECOND_LOOKUP_RESULT_TYPE,
        second_lookup_result_type,
        "SECOND_LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT",
    )
    _append_check(
        checks,
        "second lookup result scope declared",
        _present(second_lookup_result_scope),
        SECOND_LOOKUP_RESULT_SCOPE,
        second_lookup_result_scope,
        "SECOND_LOOKUP_RESULT_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "second lookup result scope one declared second lookup key only",
        second_lookup_result_scope == SECOND_LOOKUP_RESULT_SCOPE,
        SECOND_LOOKUP_RESULT_SCOPE,
        second_lookup_result_scope,
        "SECOND_LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_SECOND_ORIENTATION_LOOKUP_KEY_ONLY",
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
            _append_check(
                checks,
                "first lookup result artifact readable JSON object",
                False,
                "readable JSON object",
                read_code,
                read_code,
            )
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
    _append_check(
        checks,
        "first lookup result artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )
    _append_check(
        checks,
        "first lookup result artifact outcome recorded",
        outcome == FIRST_LOOKUP_RECORDED_OUTCOME,
        FIRST_LOOKUP_RECORDED_OUTCOME,
        outcome,
        "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "first lookup result artifact result version 0.1.0",
        version == RESULT_VERSION,
        RESULT_VERSION,
        version,
        "FIRST_LOOKUP_RESULT_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "first lookup result artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "FIRST_LOOKUP_RESULT_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    first_declared_key = first_object.get("declared_lookup_key")
    first_signal_id = first_object.get("selected_received_signal_id")
    _append_check(
        checks,
        "first lookup result predecessor key preserved if present",
        not first_object or first_declared_key == FIRST_LOOKUP_EXPECTED_KEY,
        FIRST_LOOKUP_EXPECTED_KEY,
        first_declared_key,
        "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "first lookup result predecessor signal preserved if present",
        not first_object or first_signal_id == FIRST_LOOKUP_EXPECTED_SIGNAL,
        FIRST_LOOKUP_EXPECTED_SIGNAL,
        first_signal_id,
        "FIRST_LOOKUP_RESULT_ARTIFACT_NOT_RECORDED",
    )
    return artifact, path_text


def _validate_orientation_index_artifact(
    declared: Mapping[str, Any],
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
            _append_check(
                checks,
                "read-only orientation index artifact readable JSON object",
                False,
                "readable JSON object",
                read_code,
                read_code,
            )
        return None, path_text

    index_object = _orientation_index_from_artifact(artifact)
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
    target = _target_for_second_key(index_object)
    target_signal = _target_received_signal_id(target)
    locator_artifact = _target_locator_entry_artifact(target)
    orientation_artifact = _target_orientation_view_artifact(target)
    lookup_order = index_object.get("lookup_order")
    key_count = _lookup_key_count(index_object)
    target_count = _lookup_target_count(index_object)
    accepted_count = _safe_int(index_object.get("accepted_new_entries_count"))
    deterministic = index_object.get("deterministic_local_lookup_enabled")

    _append_check(
        checks,
        "read-only orientation index artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )
    _append_check(
        checks,
        "read-only orientation index artifact outcome recorded",
        outcome == ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        outcome,
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "read-only orientation index artifact result version 0.1.0",
        version == RESULT_VERSION,
        RESULT_VERSION,
        version,
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "read-only orientation index artifact failed check count zero",
        failed_count == 0,
        0,
        failed_count,
        "READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "read-only orientation index object present",
        bool(index_object),
        "local relevance medium read-only orientation index object present",
        bool(index_object),
        "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    )
    _append_check(
        checks,
        "orientation index type local relevance medium read-only orientation index",
        index_object.get("orientation_index_type") == ORIENTATION_INDEX_TYPE,
        ORIENTATION_INDEX_TYPE,
        index_object.get("orientation_index_type"),
        "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING"
        if not index_object
        else "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    )
    _append_check(
        checks,
        "orientation index system type local relevance medium read-only orientation index system",
        index_object.get("orientation_index_system_type") == ORIENTATION_INDEX_SYSTEM_TYPE,
        ORIENTATION_INDEX_SYSTEM_TYPE,
        index_object.get("orientation_index_system_type"),
        "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    )
    _append_check(
        checks,
        "orientation index scope read-only two locators deterministic lookup only",
        index_object.get("orientation_index_scope") == ORIENTATION_INDEX_SCOPE,
        ORIENTATION_INDEX_SCOPE,
        index_object.get("orientation_index_scope"),
        "READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    )
    _append_check(
        checks,
        "lookup target found for second orientation locator",
        bool(target),
        f"lookup target for {REQUIRED_SECOND_LOOKUP_KEY}",
        target,
        "LOOKUP_TARGET_NOT_FOUND",
    )
    _append_check(
        checks,
        "selected received signal id is bounded_relevance_signal_002",
        target_signal == SECOND_LOOKUP_EXPECTED_SIGNAL,
        SECOND_LOOKUP_EXPECTED_SIGNAL,
        target_signal,
        "SELECTED_RECEIVED_SIGNAL_ID_NOT_BOUNDED_RELEVANCE_SIGNAL_002",
    )
    _append_check(
        checks,
        "selected second locator entry artifact preserved",
        _present(locator_artifact),
        "selected second locator entry artifact",
        locator_artifact,
        "SELECTED_SECOND_LOCATOR_ENTRY_ARTIFACT_MISSING",
    )
    _append_check(
        checks,
        "selected second orientation view artifact preserved",
        _present(orientation_artifact),
        "selected second orientation view artifact",
        orientation_artifact,
        "SELECTED_SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    )
    _append_check(
        checks,
        "lookup table has exactly two entries",
        isinstance(lookup_table, MappingABC) and len(lookup_table) == 2,
        2,
        len(lookup_table) if isinstance(lookup_table, MappingABC) else None,
        "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    )
    _append_check(
        checks,
        "lookup table target count exactly two",
        target_count == 2,
        2,
        target_count,
        "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "lookup order deterministic",
        lookup_order == LOOKUP_ORDER,
        LOOKUP_ORDER,
        lookup_order,
        "LOOKUP_ORDER_NOT_DETERMINISTIC",
    )
    _append_check(
        checks,
        "accepted new entries count zero",
        accepted_count == 0,
        0,
        accepted_count,
        "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    )
    _append_check(
        checks,
        "deterministic local lookup preserved",
        deterministic is True,
        True,
        deterministic,
        "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    )
    _append_check(
        checks,
        "lookup key count exactly two",
        key_count == 2,
        2,
        key_count,
        "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    )
    return artifact, path_text


def _first_lookup_artifact_basis(
    artifact: Mapping[str, Any] | None,
    path_text: str,
) -> dict[str, Any]:
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
        "first_lookup_result_object_present": bool(first_object),
        "first_lookup_result_declared_lookup_key": first_object.get("declared_lookup_key"),
        "first_lookup_result_selected_received_signal_id": first_object.get("selected_received_signal_id"),
    }


def _orientation_index_artifact_basis(
    artifact: Mapping[str, Any] | None,
    path_text: str,
) -> dict[str, Any]:
    if not isinstance(artifact, MappingABC):
        return {"selected_read_only_orientation_index_artifact": path_text}
    index_object = _orientation_index_from_artifact(artifact)
    target = _target_for_second_key(index_object)
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
        "basis_orientation_index_object_present": bool(index_object),
        "basis_orientation_index_type": index_object.get("orientation_index_type"),
        "basis_orientation_index_system_type": index_object.get("orientation_index_system_type"),
        "basis_orientation_index_scope": index_object.get("orientation_index_scope"),
        "lookup_table_key_count": _lookup_key_count(index_object),
        "lookup_table_target_count": _lookup_target_count(index_object),
        "lookup_order": index_object.get("lookup_order"),
        "accepted_new_entries_count": _safe_int(index_object.get("accepted_new_entries_count")),
        "deterministic_local_lookup_preserved": index_object.get("deterministic_local_lookup_enabled") is True,
        "selected_lookup_target_key": target.get("lookup_key"),
        "selected_received_signal_id": _target_received_signal_id(target),
        "selected_locator_entry_artifact": _target_locator_entry_artifact(target),
        "selected_orientation_view_artifact": _target_orientation_view_artifact(target),
    }


def _build_second_lookup_result_object(
    declared: Mapping[str, Any],
    first_artifact: Mapping[str, Any],
    first_path: str,
    index_artifact: Mapping[str, Any],
    index_path: str,
) -> dict[str, Any]:
    index_object = _orientation_index_from_artifact(index_artifact)
    target = _target_for_second_key(index_object)
    first_object = _first_lookup_object_from_artifact(first_artifact)
    result_object = {
        "second_lookup_result_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_id")
        )
        or DEFAULT_SECOND_LOOKUP_RESULT_ID,
        "second_lookup_result_type": SECOND_LOOKUP_RESULT_TYPE,
        "second_lookup_result_version": RESULT_VERSION,
        "second_lookup_result_scope": SECOND_LOOKUP_RESULT_SCOPE,
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
        "basis_read_only_orientation_index_artifact": index_path,
        "basis_read_only_orientation_index_system_outcome": index_artifact.get("outcome"),
        "basis_read_only_orientation_index_system_result_version": _artifact_result_version(
            index_artifact,
            "local_relevance_medium_read_only_orientation_index_system_metadata",
            "local_relevance_medium_read_only_orientation_index_system_summary",
            index_object,
        ),
        "basis_read_only_orientation_index_system_failed_check_count": _artifact_failed_check_count(
            index_artifact,
            "local_relevance_medium_read_only_orientation_index_system_metadata",
            "local_relevance_medium_read_only_orientation_index_system_summary",
            "local_relevance_medium_read_only_orientation_index_system_checks",
        ),
        "basis_orientation_index_type": index_object.get("orientation_index_type"),
        "basis_orientation_index_system_type": index_object.get("orientation_index_system_type"),
        "basis_orientation_index_scope": index_object.get("orientation_index_scope"),
        "declared_lookup_key": REQUIRED_SECOND_LOOKUP_KEY,
        "lookup_key_supported": True,
        "lookup_target_found": True,
        "selected_received_signal_id": _target_received_signal_id(target),
        "selected_locator_entry_artifact": _target_locator_entry_artifact(target),
        "selected_orientation_view_artifact": _target_orientation_view_artifact(target),
        "lookup_table_key_count": _lookup_key_count(index_object),
        "lookup_table_target_count": _lookup_target_count(index_object),
        "lookup_order": copy.deepcopy(index_object.get("lookup_order")),
        "accepted_new_entries_count": _safe_int(index_object.get("accepted_new_entries_count")),
        "deterministic_local_lookup_preserved": index_object.get("deterministic_local_lookup_enabled") is True,
        "second_lookup_result_recorded": True,
    }
    result_object.update({key: False for key in OBJECT_FALSE_FIELDS})
    return result_object


def _build_statement(second_lookup_result: Mapping[str, Any], non_claims: Mapping[str, bool]) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_second_orientation_lookup_result_recorded": (
            second_lookup_result.get("second_lookup_result_recorded") is True
        ),
        "basis_first_lookup_result_artifact_preserved": _present(
            second_lookup_result.get("basis_first_lookup_result_artifact")
        ),
        "basis_read_only_orientation_index_artifact_preserved": _present(
            second_lookup_result.get("basis_read_only_orientation_index_artifact")
        ),
        "declared_lookup_key_preserved": second_lookup_result.get("declared_lookup_key") == REQUIRED_SECOND_LOOKUP_KEY,
        "declared_lookup_key_is_second_orientation_locator": (
            second_lookup_result.get("declared_lookup_key") == REQUIRED_SECOND_LOOKUP_KEY
        ),
        "lookup_key_supported": second_lookup_result.get("lookup_key_supported") is True,
        "lookup_target_found": second_lookup_result.get("lookup_target_found") is True,
        "selected_received_signal_id_preserved": (
            second_lookup_result.get("selected_received_signal_id") == SECOND_LOOKUP_EXPECTED_SIGNAL
        ),
        "selected_locator_entry_artifact_preserved": _present(
            second_lookup_result.get("selected_locator_entry_artifact")
        ),
        "selected_orientation_view_artifact_preserved": _present(
            second_lookup_result.get("selected_orientation_view_artifact")
        ),
        "lookup_table_has_two_entries": second_lookup_result.get("lookup_table_key_count") == 2,
        "lookup_order_is_deterministic": second_lookup_result.get("lookup_order") == LOOKUP_ORDER,
        "lookup_key_count_is_two": second_lookup_result.get("lookup_table_key_count") == 2,
        "lookup_target_count_is_two": second_lookup_result.get("lookup_table_target_count") == 2,
        "accepted_new_entries_count_is_zero": second_lookup_result.get("accepted_new_entries_count") == 0,
        "deterministic_local_lookup_preserved": (
            second_lookup_result.get("deterministic_local_lookup_preserved") is True
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
        "not_general_lookup": True,
        "not_reusable_lookup_permission": True,
        "not_lookup_pair_coverage": True,
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
        "local relevance medium read-only second orientation lookup result terminal summary, if separately selected",
        "lookup-pair coverage note, if separately selected",
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
        "repeated reception permission",
        "arbitrary reception",
        "feed",
        "follow-on work",
    ]


def build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = result.get("local_relevance_medium_read_only_second_orientation_lookup_result_checks")
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    block = result.get("block") if isinstance(result.get("block"), MappingABC) else {}
    statement = result.get("local_relevance_medium_read_only_second_orientation_lookup_result_statement")
    statement_map = statement if isinstance(statement, MappingABC) else {}
    second_lookup_result = result.get("local_relevance_medium_read_only_second_orientation_lookup_result")
    second_lookup_result_map = second_lookup_result if isinstance(second_lookup_result, MappingABC) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, MappingABC) else {}

    return _sanitize(
        {
            "outcome": result.get("outcome"),
            "block_code": block.get("block_code") or block.get("code"),
            "block_reason": block.get("reason"),
            "second_lookup_result_id": second_lookup_result_map.get("second_lookup_result_id"),
            "question": result.get(
                "declared_local_relevance_medium_read_only_second_orientation_lookup_result_question", {}
            ).get("question")
            if isinstance(
                result.get("declared_local_relevance_medium_read_only_second_orientation_lookup_result_question"),
                MappingABC,
            )
            else None,
            "intent": result.get(
                "declared_local_relevance_medium_read_only_second_orientation_lookup_result_question", {}
            ).get("intent")
            if isinstance(
                result.get("declared_local_relevance_medium_read_only_second_orientation_lookup_result_question"),
                MappingABC,
            )
            else None,
            "declared_lookup_key": second_lookup_result_map.get("declared_lookup_key"),
            "passed_check_count": passed_count,
            "failed_check_count": failed_count,
            "result_version": RESULT_VERSION,
            "resolver_module": RESOLVER_MODULE,
            "second_lookup_result_recorded": statement_map.get(
                "local_relevance_medium_read_only_second_orientation_lookup_result_recorded", False
            ),
            "basis_first_lookup_result_artifact_preserved": statement_map.get(
                "basis_first_lookup_result_artifact_preserved", False
            ),
            "basis_read_only_orientation_index_artifact_preserved": statement_map.get(
                "basis_read_only_orientation_index_artifact_preserved", False
            ),
            "declared_lookup_key_preserved": statement_map.get("declared_lookup_key_preserved", False),
            "declared_lookup_key_is_second_orientation_locator": statement_map.get(
                "declared_lookup_key_is_second_orientation_locator", False
            ),
            "lookup_key_supported": statement_map.get("lookup_key_supported", False),
            "lookup_target_found": statement_map.get("lookup_target_found", False),
            "selected_received_signal_id_preserved": statement_map.get(
                "selected_received_signal_id_preserved", False
            ),
            "selected_locator_entry_artifact_preserved": statement_map.get(
                "selected_locator_entry_artifact_preserved", False
            ),
            "selected_orientation_view_artifact_preserved": statement_map.get(
                "selected_orientation_view_artifact_preserved", False
            ),
            "lookup_table_has_two_entries": statement_map.get("lookup_table_has_two_entries", False),
            "lookup_order_deterministic": statement_map.get("lookup_order_is_deterministic", False),
            "lookup_key_count_is_two": statement_map.get("lookup_key_count_is_two", False),
            "lookup_target_count_is_two": statement_map.get("lookup_target_count_is_two", False),
            "accepted_new_entries_count_is_zero": statement_map.get("accepted_new_entries_count_is_zero", False),
            "deterministic_local_lookup_preserved": statement_map.get(
                "deterministic_local_lookup_preserved", False
            ),
            "lookup_pair_coverage_not_created": non_claims_map.get("lookup_pair_coverage_created") is False,
            "reusable_lookup_permission_not_created": (
                non_claims_map.get("reusable_lookup_permission_created") is False
            ),
            "second_lookup_result_object_summary": {
                "second_lookup_result_type": second_lookup_result_map.get("second_lookup_result_type"),
                "second_lookup_result_scope": second_lookup_result_map.get("second_lookup_result_scope"),
                "selected_received_signal_id": second_lookup_result_map.get("selected_received_signal_id"),
                "selected_locator_entry_artifact": second_lookup_result_map.get("selected_locator_entry_artifact"),
                "selected_orientation_view_artifact": second_lookup_result_map.get(
                    "selected_orientation_view_artifact"
                ),
                "lookup_order": second_lookup_result_map.get("lookup_order"),
            },
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
    index_artifact: Mapping[str, Any] | None,
    index_path: str,
    second_lookup_result: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    statement = _build_statement(second_lookup_result, non_claims)
    metadata = {
        "local_relevance_medium_read_only_second_orientation_lookup_result_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_id")
        )
        or DEFAULT_REQUEST_ID,
        "local_relevance_medium_read_only_second_orientation_lookup_result_type": SECOND_LOOKUP_RESULT_TYPE,
        "local_relevance_medium_read_only_second_orientation_lookup_result_version": RESULT_VERSION,
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
        "local_relevance_medium_read_only_second_orientation_lookup_result_metadata": metadata,
        "declared_local_relevance_medium_read_only_second_orientation_lookup_result_question": {
            "question": declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_question"),
            "intent": declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_intent"),
            "declared_lookup_key": declared.get("declared_lookup_key"),
        },
        "selected_first_lookup_result_artifact_basis": _first_lookup_artifact_basis(first_artifact, first_path),
        "selected_read_only_orientation_index_artifact_basis": _orientation_index_artifact_basis(
            index_artifact,
            index_path,
        ),
        "local_relevance_medium_read_only_second_orientation_lookup_result": copy.deepcopy(
            dict(second_lookup_result)
        ),
        "local_relevance_medium_read_only_second_orientation_lookup_result_checks": copy.deepcopy(checks),
        "local_relevance_medium_read_only_second_orientation_lookup_result_statement": statement,
        "local_relevance_medium_read_only_second_orientation_lookup_result_non_meaning": _build_non_meaning(),
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
    result["local_relevance_medium_read_only_second_orientation_lookup_result_summary"] = (
        build_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(
    declared_local_relevance_medium_read_only_second_orientation_lookup_result: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    if declared_local_relevance_medium_read_only_second_orientation_lookup_result is None:
        declared = build_declared_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_request()
    elif isinstance(declared_local_relevance_medium_read_only_second_orientation_lookup_result, MappingABC):
        declared = copy.deepcopy(dict(declared_local_relevance_medium_read_only_second_orientation_lookup_result))
    else:
        checks = [
            _make_check(
                "declared read-only second orientation lookup result request mapping",
                False,
                "mapping request",
                type(declared_local_relevance_medium_read_only_second_orientation_lookup_result).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
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
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
        )

    checks: list[dict[str, Any]] = []
    _append_declared_request_checks(declared, checks)
    _append_shortcut_checks(declared, checks)
    _append_non_claim_checks(declared, checks)

    first_artifact, first_path = _validate_first_lookup_artifact(declared, checks)
    index_artifact, index_path = _validate_orientation_index_artifact(declared, checks)

    failed_before_object = _first_failed_code(checks)
    second_lookup_result: dict[str, Any] = {}
    if failed_before_object is None and first_artifact is not None and index_artifact is not None:
        second_lookup_result = _build_second_lookup_result_object(
            declared,
            first_artifact,
            first_path,
            index_artifact,
            index_path,
        )
        _append_check(
            checks,
            "second lookup result recorded",
            second_lookup_result.get("second_lookup_result_recorded") is True,
            True,
            second_lookup_result.get("second_lookup_result_recorded"),
            "SECOND_LOOKUP_RESULT_NOT_RECORDED",
        )
        _append_check(
            checks,
            "lookup-pair coverage not created",
            second_lookup_result.get("lookup_pair_coverage_created") is False,
            False,
            second_lookup_result.get("lookup_pair_coverage_created"),
            "LOOKUP_PAIR_COVERAGE_CREATED",
        )
        _append_check(
            checks,
            "reusable lookup permission not created",
            second_lookup_result.get("reusable_lookup_permission_created") is False,
            False,
            second_lookup_result.get("reusable_lookup_permission_created"),
            "REUSABLE_LOOKUP_PERMISSION_CREATED",
        )

    final_failed_code = _first_failed_code(checks)
    requested_outcome = declared.get("requested_local_relevance_medium_read_only_second_orientation_lookup_result_outcome")
    if final_failed_code:
        outcome = OUTCOME_BLOCKED
        block_code = final_failed_code
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        block_code = None
    elif declared.get("local_relevance_medium_read_only_second_orientation_lookup_result_intent") == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        block_code = None
    else:
        outcome = OUTCOME_RECORDED
        block_code = None

    return _finalize_result(
        declared,
        first_artifact,
        first_path,
        index_artifact,
        index_path,
        second_lookup_result if outcome == OUTCOME_RECORDED else {},
        checks,
        outcome,
        block_code,
    )


def resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_from_path(
    declared_local_relevance_medium_read_only_second_orientation_lookup_result_path: Path | str,
) -> dict[str, Any]:
    path = Path(declared_local_relevance_medium_read_only_second_orientation_lookup_result_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared read-only second orientation lookup result request readable",
                False,
                "readable request JSON object",
                str(path),
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_UNREADABLE",
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
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_UNREADABLE",
        )
    if not isinstance(loaded, dict):
        checks = [
            _make_check(
                "declared read-only second orientation lookup result request JSON object",
                False,
                "JSON object",
                type(loaded).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
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
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_SECOND_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
        )
    return resolve_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min(loaded)


def write_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlySecondOrientationLookupResultV0MinError(
            "result must be a mapping for JSON writing"
        )
    if output_path is not None:
        destination = Path(output_path)
        if destination.suffix != ".json":
            lookup_result = result.get("local_relevance_medium_read_only_second_orientation_lookup_result")
            result_id = DEFAULT_SECOND_LOOKUP_RESULT_ID
            if isinstance(lookup_result, MappingABC) and _present(lookup_result.get("second_lookup_result_id")):
                result_id = str(lookup_result["second_lookup_result_id"])
            destination = destination / f"{result_id}__local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result.json"
    else:
        lookup_result = result.get("local_relevance_medium_read_only_second_orientation_lookup_result")
        result_id = DEFAULT_SECOND_LOOKUP_RESULT_ID
        if isinstance(lookup_result, MappingABC) and _present(lookup_result.get("second_lookup_result_id")):
            result_id = str(lookup_result["second_lookup_result_id"])
        destination = (
            OUTPUT_ROOT
            / f"{result_id}__local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_result.json"
        )

    destination.parent.mkdir(parents=True, exist_ok=True)
    candidate = destination
    counter = 1
    while candidate.exists():
        candidate = destination.with_name(f"{destination.stem}_{counter:03d}{destination.suffix}")
        counter += 1
    with candidate.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return candidate


def build_declared_local_relevance_medium_read_only_second_orientation_lookup_result_v0_min_request(
    *,
    local_relevance_medium_read_only_second_orientation_lookup_result_id: str = DEFAULT_REQUEST_ID,
    question: str = CORE_QUESTION,
    intent: str = INTENT_RECORD,
    selected_first_lookup_result_artifact: Path | str = DEFAULT_FIRST_LOOKUP_RESULT_ARTIFACT,
    selected_read_only_orientation_index_artifact: Path | str = DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT,
    declared_lookup_key: str = REQUIRED_SECOND_LOOKUP_KEY,
    second_lookup_result_type: str = SECOND_LOOKUP_RESULT_TYPE,
    second_lookup_result_scope: str = SECOND_LOOKUP_RESULT_SCOPE,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    request = {
        "local_relevance_medium_read_only_second_orientation_lookup_result_id": (
            local_relevance_medium_read_only_second_orientation_lookup_result_id
        ),
        "local_relevance_medium_read_only_second_orientation_lookup_result_question": question,
        "local_relevance_medium_read_only_second_orientation_lookup_result_intent": intent,
        "selected_first_lookup_result_artifact": str(selected_first_lookup_result_artifact),
        "selected_read_only_orientation_index_artifact": str(selected_read_only_orientation_index_artifact),
        "declared_lookup_key": declared_lookup_key,
        "second_lookup_result_type": second_lookup_result_type,
        "second_lookup_result_scope": second_lookup_result_scope,
        "declared_non_claims": dict(declared_non_claims)
        if isinstance(declared_non_claims, MappingABC)
        else _canonical_non_claims(),
    }
    request.update(copy.deepcopy(overrides))
    return _sanitize(request)
