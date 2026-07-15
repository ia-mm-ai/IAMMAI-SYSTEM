"""Resolve one local relevance medium read-only orientation lookup result.

This resolver reads one clean
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX artifact and records one
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT for one declared
lookup key.  It uses the upstream two-entry lookup table only, returns exactly
one already-standing local orientation locator target, and keeps result-level
non-claims canonical false.

It is read-only deterministic lookup-result handling only.  It accepts no new
entry or signal, creates no new relevance object or index entry, performs no
filesystem discovery, and does not create a query surface, registry, search,
ranking, scoring, priority, validity judgment, truth judgment, authority
judgment, currentness judgment, repeated reception permission, arbitrary
reception, feed, source transfer, source receipt, source, authority,
currentness, truth, action, synchronization, participation authorization,
participant role, runtime permission, public API, participant-facing interface,
distributed network behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping as MappingABC
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyOrientationLookupResultV0MinError(Exception):
    """Bounded resolver error for read-only orientation lookup result handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min"
)

OUTCOME_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_RECORDED"
)
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BLOCKED"
)
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_lookup_result_v0_min"
)

DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_orientation_index_system_v0_min/"
    "local_relevance_medium_read_only_orientation_index_reference_review_001__"
    "local_relevance_medium_read_only_orientation_index_system_v0_min_result.json"
)

DEFAULT_LOOKUP_RESULT_ID = (
    "local_relevance_medium_read_only_orientation_lookup_result_001"
)

LOOKUP_RESULT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
LOOKUP_RESULT_SCOPE = "ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY"
ORIENTATION_INDEX_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX"
ORIENTATION_INDEX_SYSTEM_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM"
)
ORIENTATION_INDEX_SCOPE = (
    "READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY"
)
ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM_RECORDED"
)

SUPPORTED_LOOKUP_RESULT_TYPE_VALUES = (LOOKUP_RESULT_TYPE,)
SUPPORTED_LOOKUP_RESULT_SCOPE_VALUES = (LOOKUP_RESULT_SCOPE,)
SUPPORTED_LOOKUP_KEYS = ("first_orientation_locator", "second_orientation_locator")
LOOKUP_ORDER = ["first_orientation_locator", "second_orientation_locator"]

RECORD_INTENT = (
    "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
)
DO_NOT_RECORD_INTENT = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
)
BLOCK_INTENT = (
    "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
)
SUPPORTED_INTENTS = (RECORD_INTENT, DO_NOT_RECORD_INTENT, BLOCK_INTENT)

REQUIRED_FALSE_NON_CLAIMS = (
    "new_signal_accepted",
    "new_entry_accepted",
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
    "artifact_existence_treated_as_read_only_lookup_result_authority",
    "latest_file_posture_treated_as_read_only_lookup_result_authority",
    "repo_local_availability_treated_as_read_only_lookup_result_authority",
    "hidden_repo_state_used_as_read_only_lookup_result_content",
    "hidden_repo_state_used_as_read_only_lookup_result_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_orientation_lookup_result_recorded",
    "basis_read_only_orientation_index_artifact_preserved",
    "declared_lookup_key_preserved",
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
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    "ORIENTATION_INDEX_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
    "ORIENTATION_INDEX_SYSTEM_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
    "ORIENTATION_INDEX_SCOPE_NOT_READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
    "DECLARED_LOOKUP_KEY_MISSING",
    "DECLARED_LOOKUP_KEY_UNSUPPORTED",
    "LOOKUP_TARGET_NOT_FOUND",
    "SELECTED_RECEIVED_SIGNAL_ID_MISSING",
    "SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "LOOKUP_RESULT_TYPE_MISSING",
    "LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
    "LOOKUP_RESULT_SCOPE_MISSING",
    "LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
    "READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
    "NEW_SIGNAL_ACCEPTED",
    "NEW_ENTRY_ACCEPTED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_LOOKUP_RESULT_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_UNREADABLE",
)

OBJECT_FALSE_FIELDS = (
    "new_signal_accepted",
    "new_entry_accepted",
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

NON_CLAIM_BLOCK_CODE_OVERRIDES = {
    "new_signal_accepted": "NEW_SIGNAL_ACCEPTED",
    "new_entry_accepted": "NEW_ENTRY_ACCEPTED",
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
    "derivative_reception_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "vessel_relation_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "adoption_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "receiving_context_governance_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "publication_flow_created": "FOLLOW_ON_WORK_AUTHORIZED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_read_only_lookup_result_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY"
    ),
    "latest_file_posture_treated_as_read_only_lookup_result_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY"
    ),
    "repo_local_availability_treated_as_read_only_lookup_result_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY"
    ),
    "hidden_repo_state_used_as_read_only_lookup_result_content": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_LOOKUP_RESULT_CONTENT"
    ),
    "hidden_repo_state_used_as_read_only_lookup_result_authority": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_LOOKUP_RESULT_AUTHORITY"
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
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

REQUEST_SHORTCUT_FAILURES = {
    "selected_read_only_orientation_index_artifact_missing": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING"
    ),
    "selected_read_only_orientation_index_artifact_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED"
    ),
    "selected_read_only_orientation_index_artifact_failed_checks_present": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "selected_read_only_orientation_index_artifact_version_not_0_1_0": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "local_relevance_medium_read_only_orientation_index_object_missing": (
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING"
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
    "declared_lookup_key_missing": "DECLARED_LOOKUP_KEY_MISSING",
    "declared_lookup_key_unsupported": "DECLARED_LOOKUP_KEY_UNSUPPORTED",
    "lookup_target_not_found": "LOOKUP_TARGET_NOT_FOUND",
    "selected_received_signal_id_missing": "SELECTED_RECEIVED_SIGNAL_ID_MISSING",
    "selected_locator_entry_artifact_missing": "SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    "selected_orientation_view_artifact_missing": "SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "lookup_table_not_two_entries": "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "lookup_key_count_not_two": "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    "lookup_table_target_count_not_two": "LOOKUP_TABLE_TARGET_COUNT_NOT_TWO",
    "lookup_order_not_deterministic": "LOOKUP_ORDER_NOT_DETERMINISTIC",
    "accepted_new_entries_count_not_zero": "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    "deterministic_local_lookup_not_preserved": "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    "lookup_result_type_not_local_relevance_medium_read_only_orientation_lookup_result": (
        "LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT"
    ),
    "lookup_result_scope_not_one_declared_orientation_lookup_key_only": (
        "LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY"
    ),
    "read_only_lookup_result_not_recorded": "READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
    "query_surface_created": "SEARCH_SURFACE_CREATED",
    "predecessor_failure_evidence_hidden_or_repaired": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    **NON_CLAIM_BLOCK_CODE_OVERRIDES,
}

SENSITIVE_CONTENT_KEYS = frozenset(
    {
        "raw_body",
        "raw_full_body",
        "full_body",
        "artifact_body",
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
)

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = frozenset(
    (
        LOOKUP_RESULT_TYPE,
        LOOKUP_RESULT_SCOPE,
        ORIENTATION_INDEX_TYPE,
        ORIENTATION_INDEX_SYSTEM_TYPE,
        ORIENTATION_INDEX_SCOPE,
        ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        RECORD_INTENT,
        DO_NOT_RECORD_INTENT,
        BLOCK_INTENT,
        *SUPPORTED_LOOKUP_KEYS,
        *LOOKUP_ORDER,
        *OUTCOME_FAMILY,
        *BLOCK_CODES,
        *REQUIRED_FALSE_NON_CLAIMS,
        "local_relevance_medium_read_only_orientation_lookup_result_metadata",
        "declared_local_relevance_medium_read_only_orientation_lookup_result_question",
        "selected_local_relevance_medium_read_only_orientation_index_artifact_basis",
        "local_relevance_medium_read_only_orientation_lookup_result",
        "local_relevance_medium_read_only_orientation_lookup_result_checks",
        "local_relevance_medium_read_only_orientation_lookup_result_statement",
        "local_relevance_medium_read_only_orientation_lookup_result_non_meaning",
        "additional_basis_required",
        "not_recorded_basis",
        "what_remains_open",
        "non_claims",
        "outcome",
        "block",
        "local_relevance_medium_read_only_orientation_lookup_result_summary",
    )
)


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _string_or_empty(value: Any) -> str:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        return value
    return ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and value.strip() != ""


def _safe_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    return None


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
    if isinstance(value, MappingABC):
        return {
            str(item_key): _sanitize(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return value


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
        public_code = (
            code
            if code in BLOCK_CODES
            else "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED"
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


def _read_json_object(path_value: Any) -> tuple[dict[str, Any], str | None]:
    path_text = _string_or_empty(path_value)
    if not _present(path_text):
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING"
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_UNREADABLE"
    if not isinstance(data, MappingABC):
        return {}, "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_JSON_OBJECT"
    return dict(data), None


def _artifact_metadata(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    metadata = artifact.get(
        "local_relevance_medium_read_only_orientation_index_system_metadata"
    )
    if isinstance(metadata, MappingABC):
        return metadata
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_metadata") and isinstance(
            value, MappingABC
        ):
            return value
    return {}


def _artifact_summary(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    summary = artifact.get(
        "local_relevance_medium_read_only_orientation_index_system_summary"
    )
    if isinstance(summary, MappingABC):
        return summary
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_summary") and isinstance(
            value, MappingABC
        ):
            return value
    return {}


def _artifact_result_version(artifact: Mapping[str, Any]) -> str | None:
    for source in (artifact, _artifact_metadata(artifact), _artifact_summary(artifact)):
        value = source.get("result_version")
        if isinstance(value, str):
            return value
    orientation_index = _orientation_index_from_artifact(artifact)
    for key in ("orientation_index_system_version", "orientation_index_version"):
        value = orientation_index.get(key)
        if isinstance(value, str):
            return value
    return None


def _artifact_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    for source in (artifact, _artifact_metadata(artifact), _artifact_summary(artifact)):
        value = _safe_int(source.get("failed_check_count"))
        if value is not None:
            return value
    checks = artifact.get(
        "local_relevance_medium_read_only_orientation_index_system_checks"
    )
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, MappingABC) and check.get("passed") is False
        )
    return None


def _orientation_index_from_artifact(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    orientation_index = artifact.get("local_relevance_medium_read_only_orientation_index")
    if isinstance(orientation_index, MappingABC):
        return orientation_index
    return {}


def _lookup_table_from_index(
    orientation_index: Mapping[str, Any],
) -> Mapping[str, Any]:
    lookup_table = orientation_index.get("lookup_table")
    if isinstance(lookup_table, MappingABC):
        return lookup_table
    return {}


def _target_for_key(
    lookup_table: Mapping[str, Any], declared_lookup_key: str
) -> Mapping[str, Any]:
    target = lookup_table.get(declared_lookup_key)
    if isinstance(target, MappingABC):
        return target
    return {}


def _target_received_signal_id(target: Mapping[str, Any]) -> str:
    return _string_or_empty(
        target.get("received_signal_id")
        or target.get("selected_received_signal_id")
        or target.get("signal_id")
    )


def _target_locator_entry_artifact(target: Mapping[str, Any]) -> str:
    return _string_or_empty(
        target.get("locator_entry_artifact")
        or target.get("orientation_locator_entry_artifact")
        or target.get("local_orientation_locator_entry_artifact")
        or target.get("selected_locator_entry_artifact")
    )


def _target_orientation_view_artifact(target: Mapping[str, Any]) -> str:
    return _string_or_empty(
        target.get("orientation_view_artifact")
        or target.get("selected_orientation_view_artifact")
    )


def _basis_dict(
    path_text: str,
    artifact: Mapping[str, Any],
    declared_lookup_key: str,
) -> dict[str, Any]:
    orientation_index = _orientation_index_from_artifact(artifact)
    lookup_table = _lookup_table_from_index(orientation_index)
    target = _target_for_key(lookup_table, declared_lookup_key)
    return {
        "selected_local_relevance_medium_read_only_orientation_index_artifact": path_text,
        "basis_read_only_orientation_index_system_outcome": artifact.get("outcome"),
        "basis_read_only_orientation_index_system_result_version": _artifact_result_version(
            artifact
        ),
        "basis_read_only_orientation_index_system_failed_check_count": (
            _artifact_failed_check_count(artifact)
        ),
        "local_relevance_medium_read_only_orientation_index_present": bool(
            orientation_index
        ),
        "basis_orientation_index_type": orientation_index.get("orientation_index_type"),
        "basis_orientation_index_system_type": orientation_index.get(
            "orientation_index_system_type"
        ),
        "basis_orientation_index_scope": orientation_index.get(
            "orientation_index_scope"
        ),
        "declared_lookup_key": declared_lookup_key,
        "lookup_table_keys": list(lookup_table.keys()),
        "selected_received_signal_id": _target_received_signal_id(target),
        "selected_locator_entry_artifact": _target_locator_entry_artifact(target),
        "selected_orientation_view_artifact": _target_orientation_view_artifact(target),
    }


def _empty_basis(path_value: Any = "", declared_lookup_key: Any = "") -> dict[str, Any]:
    return {
        "selected_local_relevance_medium_read_only_orientation_index_artifact": (
            _string_or_empty(path_value)
        ),
        "basis_read_only_orientation_index_system_outcome": None,
        "basis_read_only_orientation_index_system_result_version": None,
        "basis_read_only_orientation_index_system_failed_check_count": None,
        "local_relevance_medium_read_only_orientation_index_present": False,
        "basis_orientation_index_type": None,
        "basis_orientation_index_system_type": None,
        "basis_orientation_index_scope": None,
        "declared_lookup_key": _string_or_empty(declared_lookup_key),
        "lookup_table_keys": [],
        "selected_received_signal_id": None,
        "selected_locator_entry_artifact": None,
        "selected_orientation_view_artifact": None,
    }


def _validate_declared_non_claims(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not isinstance(declared_non_claims, MappingABC):
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


def _append_shortcut_checks(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for shortcut, block_code in REQUEST_SHORTCUT_FAILURES.items():
        value = declared.get(shortcut)
        _append_check(
            checks,
            f"shortcut {shortcut} not asserted",
            value is not True,
            False,
            value if value is True else False,
            block_code,
        )


def _validate_declared_request(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get(
        "local_relevance_medium_read_only_orientation_lookup_result_question"
    )
    _append_check(
        checks,
        "read-only orientation lookup result question declared",
        _present(question),
        "declared read-only orientation lookup result question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_QUESTION_UNDECLARED",
    )

    intent = declared.get(
        "local_relevance_medium_read_only_orientation_lookup_result_intent"
    )
    if intent == BLOCK_INTENT:
        _append_check(
            checks,
            "read-only orientation lookup result block intent not requested",
            False,
            "record or do-not-record intent",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_BLOCK_REQUESTED",
        )
    else:
        _append_check(
            checks,
            "read-only orientation lookup result intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_INTENT_UNSUPPORTED",
        )

    declared_lookup_key = declared.get("declared_lookup_key")
    _append_check(
        checks,
        "declared lookup key present",
        _present(declared_lookup_key),
        "one declared lookup key",
        declared_lookup_key,
        "DECLARED_LOOKUP_KEY_MISSING",
    )
    _append_check(
        checks,
        "declared lookup key supported",
        declared_lookup_key in SUPPORTED_LOOKUP_KEYS,
        SUPPORTED_LOOKUP_KEYS,
        declared_lookup_key,
        "DECLARED_LOOKUP_KEY_UNSUPPORTED",
    )

    lookup_result_type = declared.get("lookup_result_type")
    if not _present(lookup_result_type):
        _append_check(
            checks,
            "lookup result type present",
            False,
            LOOKUP_RESULT_TYPE,
            lookup_result_type,
            "LOOKUP_RESULT_TYPE_MISSING",
        )
    else:
        _append_check(
            checks,
            "lookup result type exact",
            lookup_result_type == LOOKUP_RESULT_TYPE,
            LOOKUP_RESULT_TYPE,
            lookup_result_type,
            "LOOKUP_RESULT_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT",
        )

    lookup_result_scope = declared.get("lookup_result_scope")
    if not _present(lookup_result_scope):
        _append_check(
            checks,
            "lookup result scope present",
            False,
            LOOKUP_RESULT_SCOPE,
            lookup_result_scope,
            "LOOKUP_RESULT_SCOPE_MISSING",
        )
    else:
        _append_check(
            checks,
            "lookup result scope one declared lookup key only",
            lookup_result_scope == LOOKUP_RESULT_SCOPE,
            LOOKUP_RESULT_SCOPE,
            lookup_result_scope,
            "LOOKUP_RESULT_SCOPE_NOT_ONE_DECLARED_ORIENTATION_LOOKUP_KEY_ONLY",
        )

    _append_shortcut_checks(declared, checks)
    _validate_declared_non_claims(declared, checks)


def _extract_orientation_index_basis(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[dict[str, Any], Mapping[str, Any], Mapping[str, Any]]:
    path_text = _string_or_empty(
        declared.get("selected_local_relevance_medium_read_only_orientation_index_artifact")
    )
    _append_check(
        checks,
        "selected read-only orientation index artifact path declared",
        _present(path_text),
        "declared selected read-only orientation index artifact path",
        path_text,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_PATH_MISSING",
    )
    artifact, read_error = _read_json_object(path_text)
    if read_error:
        _append_check(
            checks,
            "selected read-only orientation index artifact readable JSON object",
            False,
            "readable JSON object",
            read_error,
            read_error,
        )
        return _empty_basis(path_text, declared.get("declared_lookup_key")), {}, {}

    _append_check(
        checks,
        "selected read-only orientation index artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )

    artifact_outcome = artifact.get("outcome")
    artifact_version = _artifact_result_version(artifact)
    artifact_failed_count = _artifact_failed_check_count(artifact)
    orientation_index = _orientation_index_from_artifact(artifact)

    _append_check(
        checks,
        "selected read-only orientation index artifact outcome recorded",
        artifact_outcome == ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        ORIENTATION_INDEX_SYSTEM_RECORDED_OUTCOME,
        artifact_outcome,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "selected read-only orientation index artifact result version 0.1.0",
        artifact_version == RESULT_VERSION,
        RESULT_VERSION,
        artifact_version,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "selected read-only orientation index artifact failed check count zero",
        artifact_failed_count == 0,
        0,
        artifact_failed_count,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _append_check(
        checks,
        "local relevance medium read-only orientation index object present",
        bool(orientation_index),
        "local_relevance_medium_read_only_orientation_index object",
        "present" if orientation_index else "missing",
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_OBJECT_MISSING",
    )

    basis = _basis_dict(path_text, artifact, _string_or_empty(declared.get("declared_lookup_key")))
    return basis, artifact, orientation_index


def _validate_orientation_index(
    orientation_index: Mapping[str, Any],
    declared_lookup_key: str,
    checks: list[dict[str, Any]],
) -> Mapping[str, Any]:
    lookup_table = _lookup_table_from_index(orientation_index)
    lookup_table_has_two_entries = (
        isinstance(lookup_table, MappingABC)
        and len(lookup_table) == 2
        and set(lookup_table.keys()) == set(SUPPORTED_LOOKUP_KEYS)
    )
    lookup_key_count = _safe_int(orientation_index.get("lookup_key_count"))
    lookup_target_count = _safe_int(orientation_index.get("lookup_target_count"))
    lookup_order = orientation_index.get("lookup_order")
    target = _target_for_key(lookup_table, declared_lookup_key)
    received_signal_id = _target_received_signal_id(target)
    locator_entry_artifact = _target_locator_entry_artifact(target)
    orientation_view_artifact = _target_orientation_view_artifact(target)

    _append_check(
        checks,
        "orientation index type exact",
        orientation_index.get("orientation_index_type") == ORIENTATION_INDEX_TYPE,
        ORIENTATION_INDEX_TYPE,
        orientation_index.get("orientation_index_type"),
        "ORIENTATION_INDEX_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX",
    )
    _append_check(
        checks,
        "orientation index system type exact",
        orientation_index.get("orientation_index_system_type")
        == ORIENTATION_INDEX_SYSTEM_TYPE,
        ORIENTATION_INDEX_SYSTEM_TYPE,
        orientation_index.get("orientation_index_system_type"),
        "ORIENTATION_INDEX_SYSTEM_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX_SYSTEM",
    )
    _append_check(
        checks,
        "orientation index scope read-only deterministic lookup only",
        orientation_index.get("orientation_index_scope") == ORIENTATION_INDEX_SCOPE,
        ORIENTATION_INDEX_SCOPE,
        orientation_index.get("orientation_index_scope"),
        "ORIENTATION_INDEX_SCOPE_NOT_READ_ONLY_TWO_ORIENTATION_LOCATORS_DETERMINISTIC_LOOKUP_ONLY",
    )
    _append_check(
        checks,
        "lookup table has exactly two entries",
        lookup_table_has_two_entries and lookup_key_count == 2,
        "two supported lookup entries",
        {
            "lookup_table_keys": list(lookup_table.keys()),
            "lookup_key_count": lookup_key_count,
        },
        "LOOKUP_TABLE_NOT_TWO_ENTRIES",
    )
    _append_check(
        checks,
        "lookup table target count exactly two",
        lookup_target_count == 2,
        2,
        lookup_target_count,
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
        orientation_index.get("accepted_new_entries_count") == 0,
        0,
        orientation_index.get("accepted_new_entries_count"),
        "ACCEPTED_NEW_ENTRIES_COUNT_NOT_ZERO",
    )
    _append_check(
        checks,
        "deterministic local lookup preserved",
        orientation_index.get("deterministic_local_lookup_enabled") is True,
        True,
        orientation_index.get("deterministic_local_lookup_enabled"),
        "DETERMINISTIC_LOCAL_LOOKUP_NOT_PRESERVED",
    )
    _append_check(
        checks,
        "lookup target found",
        bool(target),
        "one existing lookup target for declared key",
        "found" if target else "missing",
        "LOOKUP_TARGET_NOT_FOUND",
    )
    _append_check(
        checks,
        "selected received signal id preserved",
        _present(received_signal_id),
        "selected received signal id",
        received_signal_id,
        "SELECTED_RECEIVED_SIGNAL_ID_MISSING",
    )
    _append_check(
        checks,
        "selected locator entry artifact preserved",
        _present(locator_entry_artifact),
        "selected locator entry artifact path",
        locator_entry_artifact,
        "SELECTED_LOCATOR_ENTRY_ARTIFACT_MISSING",
    )
    _append_check(
        checks,
        "selected orientation view artifact preserved",
        _present(orientation_view_artifact),
        "selected orientation view artifact path",
        orientation_view_artifact,
        "SELECTED_ORIENTATION_VIEW_ARTIFACT_MISSING",
    )
    return target


def _build_lookup_result_object(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
    artifact: Mapping[str, Any],
    orientation_index: Mapping[str, Any],
    declared_lookup_key: str,
    target: Mapping[str, Any],
) -> dict[str, Any]:
    lookup_result: dict[str, Any] = {
        "lookup_result_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_orientation_lookup_result_id")
        )
        or DEFAULT_LOOKUP_RESULT_ID,
        "lookup_result_type": LOOKUP_RESULT_TYPE,
        "lookup_result_version": RESULT_VERSION,
        "lookup_result_scope": LOOKUP_RESULT_SCOPE,
        "basis_read_only_orientation_index_artifact": basis.get(
            "selected_local_relevance_medium_read_only_orientation_index_artifact"
        ),
        "basis_read_only_orientation_index_system_outcome": artifact.get("outcome"),
        "basis_read_only_orientation_index_system_result_version": (
            _artifact_result_version(artifact)
        ),
        "basis_read_only_orientation_index_system_failed_check_count": (
            _artifact_failed_check_count(artifact)
        ),
        "basis_orientation_index_type": orientation_index.get("orientation_index_type"),
        "basis_orientation_index_system_type": orientation_index.get(
            "orientation_index_system_type"
        ),
        "basis_orientation_index_scope": orientation_index.get(
            "orientation_index_scope"
        ),
        "declared_lookup_key": declared_lookup_key,
        "lookup_key_supported": declared_lookup_key in SUPPORTED_LOOKUP_KEYS,
        "lookup_target_found": bool(target),
        "selected_received_signal_id": _target_received_signal_id(target),
        "selected_locator_entry_artifact": _target_locator_entry_artifact(target),
        "selected_orientation_view_artifact": _target_orientation_view_artifact(target),
        "lookup_table_key_count": orientation_index.get("lookup_key_count"),
        "lookup_table_target_count": orientation_index.get("lookup_target_count"),
        "lookup_order": list(orientation_index.get("lookup_order") or []),
        "accepted_new_entries_count": orientation_index.get(
            "accepted_new_entries_count"
        ),
        "deterministic_local_lookup_preserved": (
            orientation_index.get("deterministic_local_lookup_enabled") is True
        ),
        "read_only_lookup_result_recorded": True,
    }
    lookup_result.update({field: False for field in OBJECT_FALSE_FIELDS})
    return lookup_result


def _build_statement(
    lookup_result: Mapping[str, Any],
    non_claims: Mapping[str, bool],
) -> dict[str, bool]:
    recorded = bool(lookup_result)
    statement = {
        "local_relevance_medium_read_only_orientation_lookup_result_recorded": (
            recorded
            and lookup_result.get("read_only_lookup_result_recorded") is True
        ),
        "basis_read_only_orientation_index_artifact_preserved": (
            recorded
            and _present(lookup_result.get("basis_read_only_orientation_index_artifact"))
        ),
        "declared_lookup_key_preserved": (
            recorded and lookup_result.get("declared_lookup_key") in SUPPORTED_LOOKUP_KEYS
        ),
        "lookup_key_supported": recorded
        and lookup_result.get("lookup_key_supported") is True,
        "lookup_target_found": recorded
        and lookup_result.get("lookup_target_found") is True,
        "selected_received_signal_id_preserved": (
            recorded and _present(lookup_result.get("selected_received_signal_id"))
        ),
        "selected_locator_entry_artifact_preserved": (
            recorded and _present(lookup_result.get("selected_locator_entry_artifact"))
        ),
        "selected_orientation_view_artifact_preserved": (
            recorded and _present(lookup_result.get("selected_orientation_view_artifact"))
        ),
        "lookup_table_has_two_entries": (
            recorded and lookup_result.get("lookup_table_key_count") == 2
        ),
        "lookup_order_is_deterministic": (
            recorded and lookup_result.get("lookup_order") == LOOKUP_ORDER
        ),
        "lookup_key_count_is_two": (
            recorded and lookup_result.get("lookup_table_key_count") == 2
        ),
        "lookup_target_count_is_two": (
            recorded and lookup_result.get("lookup_table_target_count") == 2
        ),
        "accepted_new_entries_count_is_zero": (
            recorded and lookup_result.get("accepted_new_entries_count") == 0
        ),
        "deterministic_local_lookup_preserved": (
            recorded
            and lookup_result.get("deterministic_local_lookup_preserved") is True
        ),
        "result_level_non_claims_canonical_false": all(
            value is False for value in non_claims.values()
        ),
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_not_repaired": True,
        "predecessor_failure_not_hidden": True,
        "predecessor_failure_not_claimed_passed": True,
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
    }
    return statement


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_registry": True,
        "not_search": True,
        "not_ranking": True,
        "not_query_surface": True,
        "not_scoring": True,
        "not_priority": True,
        "not_validity_truth_authority_or_currentness_judgment": True,
        "not_repeated_reception_permission": True,
        "not_arbitrary_reception": True,
        "not_feed": True,
        "not_source_transfer_or_source_receipt": True,
        "not_authority_currentness_truth_action_or_synchronization": True,
        "not_participation_runtime_api_interface_or_distributed_behavior": True,
        "not_operation_permission": True,
        "not_follow_on_work": True,
    }


def _what_remains_open() -> list[str]:
    return [
        "second lookup result, if separately selected",
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


def _finalize_result(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
    basis: Mapping[str, Any],
    lookup_result: Mapping[str, Any],
    outcome: str,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    block_code = _first_failed_code(checks)
    block = {
        "blocked": outcome == OUTCOME_BLOCKED,
        "code": block_code if outcome == OUTCOME_BLOCKED else None,
        "block_code": block_code if outcome == OUTCOME_BLOCKED else None,
        "reason": block_code if outcome == OUTCOME_BLOCKED else None,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_orientation_lookup_result_metadata": {
            "local_relevance_medium_read_only_orientation_lookup_result_id": (
                _string_or_empty(
                    declared.get(
                        "local_relevance_medium_read_only_orientation_lookup_result_id"
                    )
                )
                or DEFAULT_LOOKUP_RESULT_ID
            ),
            "local_relevance_medium_read_only_orientation_lookup_result_type": (
                LOOKUP_RESULT_TYPE
            ),
            "local_relevance_medium_read_only_orientation_lookup_result_version": (
                RESULT_VERSION
            ),
            "generated_at": _utc_timestamp(),
            "resolver_module": RESOLVER_MODULE,
        },
        "declared_local_relevance_medium_read_only_orientation_lookup_result_question": {
            "question": declared.get(
                "local_relevance_medium_read_only_orientation_lookup_result_question"
            ),
            "intent": declared.get(
                "local_relevance_medium_read_only_orientation_lookup_result_intent"
            ),
            "declared_lookup_key": declared.get("declared_lookup_key"),
        },
        "selected_local_relevance_medium_read_only_orientation_index_artifact_basis": dict(
            basis
        ),
        "local_relevance_medium_read_only_orientation_lookup_result": dict(
            lookup_result
        ),
        "local_relevance_medium_read_only_orientation_lookup_result_checks": checks,
        "local_relevance_medium_read_only_orientation_lookup_result_statement": (
            _build_statement(lookup_result, non_claims)
        ),
        "local_relevance_medium_read_only_orientation_lookup_result_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": (
            [_sanitize(declared.get("additional_basis_context"))]
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            and declared.get("additional_basis_context") is not None
            else []
        ),
        "not_recorded_basis": (
            [_sanitize(declared.get("not_recorded_basis"))]
            if outcome == OUTCOME_NOT_RECORDED
            and declared.get("not_recorded_basis") is not None
            else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": non_claims,
        "outcome": outcome,
        "block": block,
    }
    result["local_relevance_medium_read_only_orientation_lookup_result_summary"] = (
        build_local_relevance_medium_read_only_orientation_lookup_result_v0_min_summary(
            result
        )
    )
    return _sanitize(result)


def _blocked_request_result(code: str, path_value: Any = "") -> dict:
    checks = [
        _make_check(
            "declared read-only orientation lookup result request readable mapping",
            False,
            "readable JSON object request mapping",
            path_value,
            code,
        )
    ]
    return _finalize_result(
        {},
        checks,
        _empty_basis(path_value),
        {},
        OUTCOME_BLOCKED,
    )


def resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
    declared_local_relevance_medium_read_only_orientation_lookup_result: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one declared read-only orientation lookup result request."""

    if declared_local_relevance_medium_read_only_orientation_lookup_result is None:
        declared = (
            build_declared_local_relevance_medium_read_only_orientation_lookup_result_v0_min_request()
        )
    elif not isinstance(
        declared_local_relevance_medium_read_only_orientation_lookup_result,
        MappingABC,
    ):
        return _blocked_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
            type(
                declared_local_relevance_medium_read_only_orientation_lookup_result
            ).__name__,
        )
    else:
        declared = copy.deepcopy(
            dict(declared_local_relevance_medium_read_only_orientation_lookup_result)
        )

    checks: list[dict[str, Any]] = []
    _validate_declared_request(declared, checks)

    basis, artifact, orientation_index = _extract_orientation_index_basis(
        declared, checks
    )
    declared_lookup_key = _string_or_empty(declared.get("declared_lookup_key"))
    target: Mapping[str, Any] = {}
    if orientation_index:
        target = _validate_orientation_index(orientation_index, declared_lookup_key, checks)

    intent = declared.get(
        "local_relevance_medium_read_only_orientation_lookup_result_intent"
    )
    can_record_before_recorded_check = (
        not any(check.get("passed") is False for check in checks)
        and intent == RECORD_INTENT
        and bool(target)
    )

    lookup_result: Mapping[str, Any] = {}
    if can_record_before_recorded_check:
        lookup_result = _build_lookup_result_object(
            declared,
            basis,
            artifact,
            orientation_index,
            declared_lookup_key,
            target,
        )

    if intent == RECORD_INTENT:
        _append_check(
            checks,
            "read-only lookup result recorded",
            bool(lookup_result)
            and lookup_result.get("read_only_lookup_result_recorded") is True,
            True,
            lookup_result.get("read_only_lookup_result_recorded"),
            "READ_ONLY_LOOKUP_RESULT_NOT_RECORDED",
        )

    failed_count = sum(1 for check in checks if check.get("passed") is False)
    requested_outcome = declared.get(
        "requested_local_relevance_medium_read_only_orientation_lookup_result_outcome"
    )
    if failed_count:
        outcome = OUTCOME_BLOCKED
        lookup_result = {}
    elif requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        lookup_result = {}
    elif intent == DO_NOT_RECORD_INTENT:
        outcome = OUTCOME_NOT_RECORDED
        lookup_result = {}
    else:
        outcome = OUTCOME_RECORDED

    return _finalize_result(declared, checks, basis, lookup_result, outcome)


def resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min_from_path(
    declared_local_relevance_medium_read_only_orientation_lookup_result_path: Path | str,
) -> dict:
    """Load a declared request JSON object from path and resolve it."""

    path = Path(declared_local_relevance_medium_read_only_orientation_lookup_result_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            data = json.load(handle)
    except Exception:
        return _blocked_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_UNREADABLE",
            path,
        )
    if not isinstance(data, MappingABC):
        return _blocked_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT_REQUEST_MALFORMED",
            path,
        )
    return resolve_local_relevance_medium_read_only_orientation_lookup_result_v0_min(
        data
    )


def build_local_relevance_medium_read_only_orientation_lookup_result_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for one lookup-result resolver artifact."""

    checks = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result_checks", []
    )
    check_list = checks if isinstance(checks, list) else []
    passed_count, failed_count = _check_counts(check_list)
    block = result.get("block") if isinstance(result.get("block"), MappingABC) else {}
    lookup_result = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result"
    )
    if not isinstance(lookup_result, MappingABC):
        lookup_result = {}
    metadata = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result_metadata"
    )
    if not isinstance(metadata, MappingABC):
        metadata = {}
    statement = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result_statement"
    )
    if not isinstance(statement, MappingABC):
        statement = {}
    question = result.get(
        "declared_local_relevance_medium_read_only_orientation_lookup_result_question"
    )
    if not isinstance(question, MappingABC):
        question = {}
    non_claims = result.get("non_claims")
    if not isinstance(non_claims, MappingABC):
        non_claims = {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "lookup_result_id": lookup_result.get("lookup_result_id")
        or metadata.get("local_relevance_medium_read_only_orientation_lookup_result_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "declared_lookup_key": question.get("declared_lookup_key")
        or lookup_result.get("declared_lookup_key"),
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "read_only_lookup_result_recorded": statement.get(
            "local_relevance_medium_read_only_orientation_lookup_result_recorded",
            False,
        ),
        "basis_read_only_orientation_index_artifact_preserved": statement.get(
            "basis_read_only_orientation_index_artifact_preserved", False
        ),
        "declared_lookup_key_preserved": statement.get(
            "declared_lookup_key_preserved", False
        ),
        "lookup_key_supported": statement.get("lookup_key_supported", False),
        "lookup_target_found": statement.get("lookup_target_found", False),
        "selected_received_signal_id_preserved": statement.get(
            "selected_received_signal_id_preserved", False
        ),
        "selected_locator_entry_artifact_preserved": statement.get(
            "selected_locator_entry_artifact_preserved", False
        ),
        "selected_orientation_view_artifact_preserved": statement.get(
            "selected_orientation_view_artifact_preserved", False
        ),
        "lookup_table_has_two_entries": statement.get(
            "lookup_table_has_two_entries", False
        ),
        "lookup_order_is_deterministic": statement.get(
            "lookup_order_is_deterministic", False
        ),
        "lookup_key_count_is_two": statement.get("lookup_key_count_is_two", False),
        "lookup_target_count_is_two": statement.get(
            "lookup_target_count_is_two", False
        ),
        "accepted_new_entries_count_is_zero": statement.get(
            "accepted_new_entries_count_is_zero", False
        ),
        "deterministic_local_lookup_preserved": statement.get(
            "deterministic_local_lookup_preserved", False
        ),
        "lookup_result_object_summary": {
            "lookup_result_type": lookup_result.get("lookup_result_type"),
            "lookup_result_scope": lookup_result.get("lookup_result_scope"),
            "basis_orientation_index_type": lookup_result.get(
                "basis_orientation_index_type"
            ),
            "basis_orientation_index_system_type": lookup_result.get(
                "basis_orientation_index_system_type"
            ),
            "basis_orientation_index_scope": lookup_result.get(
                "basis_orientation_index_scope"
            ),
            "declared_lookup_key": lookup_result.get("declared_lookup_key"),
            "selected_received_signal_id": lookup_result.get(
                "selected_received_signal_id"
            ),
            "selected_locator_entry_artifact": lookup_result.get(
                "selected_locator_entry_artifact"
            ),
            "selected_orientation_view_artifact": lookup_result.get(
                "selected_orientation_view_artifact"
            ),
            "lookup_table_key_count": lookup_result.get("lookup_table_key_count"),
            "lookup_table_target_count": lookup_result.get(
                "lookup_table_target_count"
            ),
            "accepted_new_entries_count": lookup_result.get(
                "accepted_new_entries_count"
            ),
        },
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            non_claims.get("new_signal_accepted") is False
            and non_claims.get("new_entry_accepted") is False
            and non_claims.get("new_relevance_object_created") is False
            and non_claims.get("new_index_entry_created") is False
        ),
        "filesystem_discovery_not_performed": (
            non_claims.get("filesystem_discovery_performed") is False
        ),
        "registry_search_ranking_not_created": (
            non_claims.get("registry_created") is False
            and non_claims.get("search_surface_created") is False
            and non_claims.get("ranking_surface_created") is False
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            non_claims.get("scoring_surface_created") is False
            and non_claims.get("priority_surface_created") is False
            and non_claims.get("validity_judgment_created") is False
            and non_claims.get("truth_judgment_created") is False
            and non_claims.get("authority_judgment_created") is False
            and non_claims.get("currentness_judgment_created") is False
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": (
            non_claims.get("repeated_reception_permission_created") is False
            and non_claims.get("arbitrary_reception_created") is False
            and non_claims.get("feed_created") is False
        ),
        "source_authority_currentness_truth_action_synchronization_participation_runtime_not_created": (
            non_claims.get("source_transfer_occurred") is False
            and non_claims.get("source_receipt_occurred") is False
            and non_claims.get("authority_created") is False
            and non_claims.get("currentness_created") is False
            and non_claims.get("truth_created") is False
            and non_claims.get("action_created") is False
            and non_claims.get("synchronization_created") is False
            and non_claims.get("participation_authorized") is False
            and non_claims.get("participant_role_created") is False
            and non_claims.get("runtime_permission_created") is False
        ),
        "public_api_interface_distributed_behavior_not_created": (
            non_claims.get("public_api_created") is False
            and non_claims.get("participant_facing_interface_created") is False
            and non_claims.get("distributed_network_behavior_created") is False
        ),
        "operation_permission_follow_on_not_created": (
            non_claims.get("operation_permission_created") is False
            and non_claims.get("follow_on_work_authorized") is False
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "new_signal_accepted",
                "new_entry_accepted",
                "new_relevance_object_created",
                "new_index_entry_created",
                "filesystem_discovery_performed",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": statement.get(
            "predecessor_failure_evidence_preserved", True
        ),
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def write_local_relevance_medium_read_only_orientation_lookup_result_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write one lookup-result resolver artifact with stable JSON formatting."""

    if not isinstance(result, MappingABC):
        raise LocalRelevanceMediumReadOnlyOrientationLookupResultV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result_metadata"
    )
    lookup_result = result.get(
        "local_relevance_medium_read_only_orientation_lookup_result"
    )
    result_id = DEFAULT_LOOKUP_RESULT_ID
    if isinstance(metadata, MappingABC):
        result_id = (
            _string_or_empty(
                metadata.get(
                    "local_relevance_medium_read_only_orientation_lookup_result_id"
                )
            )
            or result_id
        )
    if isinstance(lookup_result, MappingABC):
        result_id = _string_or_empty(lookup_result.get("lookup_result_id")) or result_id

    if output_path is None:
        candidate = OUTPUT_ROOT / (
            f"{result_id}__"
            "local_relevance_medium_read_only_orientation_lookup_result_v0_min_result.json"
        )
    else:
        candidate = Path(output_path)

    candidate.parent.mkdir(parents=True, exist_ok=True)
    final_path = candidate
    if final_path.exists():
        suffix = final_path.suffix
        stem = final_path.stem
        parent = final_path.parent
        counter = 1
        while final_path.exists():
            final_path = parent / f"{stem}_{counter:03d}{suffix}"
            counter += 1

    with final_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, indent=2, sort_keys=True)
        handle.write("\n")
    return final_path


def build_declared_local_relevance_medium_read_only_orientation_lookup_result_v0_min_request(
    *,
    local_relevance_medium_read_only_orientation_lookup_result_id: str = DEFAULT_LOOKUP_RESULT_ID,
    selected_local_relevance_medium_read_only_orientation_index_artifact: Path
    | str = DEFAULT_READ_ONLY_ORIENTATION_INDEX_ARTIFACT,
    declared_lookup_key: str = "first_orientation_locator",
    lookup_result_type: str = LOOKUP_RESULT_TYPE,
    lookup_result_scope: str = LOOKUP_RESULT_SCOPE,
    local_relevance_medium_read_only_orientation_lookup_result_intent: str = RECORD_INTENT,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared read-only orientation lookup result request."""

    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims = dict(declared_non_claims)
    request: dict[str, Any] = {
        "local_relevance_medium_read_only_orientation_lookup_result_id": (
            local_relevance_medium_read_only_orientation_lookup_result_id
        ),
        "local_relevance_medium_read_only_orientation_lookup_result_question": (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_INDEX, "
            "may one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_ORIENTATION_LOOKUP_RESULT "
            "be recorded for one declared lookup key, returning exactly one "
            "already-standing local orientation locator target, without "
            "accepting new entries, accepting new signals, discovering "
            "artifacts, creating registry, search, ranking, scoring, priority, "
            "validity judgment, truth judgment, authority, currentness, action, "
            "synchronization, participation authorization, participant role, "
            "runtime permission, public API, participant-facing interface, "
            "distributed network behavior, operation permission, repeated "
            "reception permission, arbitrary reception, feed, source transfer, "
            "source receipt, or follow-on work?"
        ),
        "local_relevance_medium_read_only_orientation_lookup_result_intent": (
            local_relevance_medium_read_only_orientation_lookup_result_intent
        ),
        "selected_local_relevance_medium_read_only_orientation_index_artifact": str(
            selected_local_relevance_medium_read_only_orientation_index_artifact
        ),
        "declared_lookup_key": declared_lookup_key,
        "lookup_result_type": lookup_result_type,
        "lookup_result_scope": lookup_result_scope,
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return request
