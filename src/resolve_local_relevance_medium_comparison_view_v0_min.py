"""Resolve one local relevance medium comparison view.

This module records one small LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW from one
clean LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW artifact. It preserves the upstream
relation, multiplicity, locator, orientation, receipt, reception, successor, and
received identifier lineage while keeping result-level non-claims canonical
false. It does not create an index system, registry, search, ranking, scoring,
priority, validity judgment, truth judgment, authority, currentness, action,
synchronization, participation, runtime permission, API, distributed behavior,
or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumComparisonViewV0MinError(Exception):
    """Bounded resolver error for comparison-view request handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_comparison_view_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min"
)

DEFAULT_RELATION_VIEW_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min/"
    "local_relevance_medium_relation_view_reference_review_001__"
    "local_relevance_medium_relation_view_v0_min_result.json"
)

DEFAULT_COMPARISON_VIEW_ID = "local_relevance_medium_comparison_view_001"

COMPARISON_VIEW_TYPE = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
COMPARISON_VIEW_SCOPE = "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY"
COMPARISON_FRAME = "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY"

RELATION_VIEW_TYPE = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
RELATION_VIEW_SCOPE = "TWO_LOCAL_ORIENTATION_OBJECTS_RELATION_VIEW_ONLY"
RELATION_FRAME = "BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY"
RELATION_VIEW_RECORDED_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED"

RECORD_INTENT = "RECORD_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
BLOCK_INTENT = "BLOCK_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
SUPPORTED_INTENTS = (RECORD_INTENT, DO_NOT_RECORD_INTENT, BLOCK_INTENT)

SUPPORTED_COMPARISON_VIEW_SCOPE_VALUES = (COMPARISON_VIEW_SCOPE,)
SUPPORTED_COMPARISON_VIEW_TYPE_VALUES = (COMPARISON_VIEW_TYPE,)
SUPPORTED_COMPARISON_FRAME_VALUES = (COMPARISON_FRAME,)

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

REQUIRED_FALSE_NON_CLAIMS = (
    "ranking_surface_created",
    "scoring_surface_created",
    "priority_surface_created",
    "validity_judgment_created",
    "truth_judgment_created",
    "authority_judgment_created",
    "currentness_judgment_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_created",
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
    "artifact_existence_treated_as_comparison_view_authority",
    "latest_file_posture_treated_as_comparison_view_authority",
    "repo_local_availability_treated_as_comparison_view_authority",
    "hidden_repo_state_used_as_comparison_view_content",
    "hidden_repo_state_used_as_comparison_view_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_comparison_view_recorded",
    "basis_local_relevance_medium_relation_view_artifact_preserved",
    "basis_local_relevance_medium_multiplicity_result_artifact_preserved",
    "basis_first_local_relevance_orientation_index_entry_artifact_preserved",
    "basis_second_local_relevance_orientation_index_entry_artifact_preserved",
    "first_orientation_view_artifact_preserved",
    "second_orientation_view_artifact_preserved",
    "first_receipt_artifact_preserved",
    "second_receipt_artifact_preserved",
    "first_reception_artifact_preserved",
    "second_reception_artifact_preserved",
    "successor_candidate_admission_artifact_preserved",
    "successor_reception_request_artifact_preserved",
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
    "comparison_view_scope_local_only",
    "comparison_frame_bounded_non_ranking_only",
    "comparison_pair_count_is_one",
    "relation_readable_co_presence_preserved",
    "comparison_readable_distinctions_recorded",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_OBJECT_MISSING",
    "RELATION_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
    "RELATION_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "RELATION_FRAME_NOT_BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "MULTIPLICITY_COUNT_NOT_TWO",
    "RELATION_PAIR_COUNT_NOT_ONE",
    "RELATION_VIEW_ARTIFACT_MISSING",
    "BASIS_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_MISSING",
    "FIRST_LOCATOR_ARTIFACT_MISSING",
    "SECOND_LOCATOR_ARTIFACT_MISSING",
    "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "FIRST_RECEIPT_ARTIFACT_MISSING",
    "SECOND_RECEIPT_ARTIFACT_MISSING",
    "FIRST_RECEPTION_ARTIFACT_MISSING",
    "SECOND_RECEPTION_ARTIFACT_MISSING",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_MISSING",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_MISSING",
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
    "COMPARISON_VIEW_SCOPE_MISSING",
    "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "COMPARISON_VIEW_TYPE_MISSING",
    "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW",
    "COMPARISON_FRAME_MISSING",
    "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
    "COMPARISON_PAIR_COUNT_NOT_ONE",
    "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED",
    "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED",
    "COMPARISON_VIEW_NOT_RECORDED",
    "RANKING_SURFACE_CREATED",
    "SCORING_SURFACE_CREATED",
    "PRIORITY_SURFACE_CREATED",
    "VALIDITY_JUDGMENT_CREATED",
    "TRUTH_JUDGMENT_CREATED",
    "AUTHORITY_JUDGMENT_CREATED",
    "CURRENTNESS_JUDGMENT_CREATED",
    "INDEX_SYSTEM_CREATED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_COMPARISON_VIEW_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_COMPARISON_VIEW_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMPARISON_VIEW_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_COMPARISON_VIEW_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_COMPARISON_VIEW_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_UNREADABLE",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "PRIOR_ARTIFACTS_MUTATED",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = (
    COMPARISON_VIEW_TYPE,
    COMPARISON_VIEW_SCOPE,
    COMPARISON_FRAME,
    RELATION_VIEW_TYPE,
    RELATION_VIEW_SCOPE,
    RELATION_FRAME,
    RELATION_VIEW_RECORDED_OUTCOME,
    RESULT_VERSION,
    RESOLVER_MODULE,
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
    *OUTCOME_FAMILY,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
)

FALSE_POSTURE_TO_BLOCK_CODE = {
    "ranking_surface_created": "RANKING_SURFACE_CREATED",
    "scoring_surface_created": "SCORING_SURFACE_CREATED",
    "priority_surface_created": "PRIORITY_SURFACE_CREATED",
    "validity_judgment_created": "VALIDITY_JUDGMENT_CREATED",
    "truth_judgment_created": "TRUTH_JUDGMENT_CREATED",
    "authority_judgment_created": "AUTHORITY_JUDGMENT_CREATED",
    "currentness_judgment_created": "CURRENTNESS_JUDGMENT_CREATED",
    "index_system_created": "INDEX_SYSTEM_CREATED",
    "registry_created": "REGISTRY_CREATED",
    "search_surface_created": "SEARCH_SURFACE_CREATED",
    "ranking_created": "RANKING_CREATED",
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
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_comparison_view_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_COMPARISON_VIEW_AUTHORITY"
    ),
    "latest_file_posture_treated_as_comparison_view_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_COMPARISON_VIEW_AUTHORITY"
    ),
    "repo_local_availability_treated_as_comparison_view_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_COMPARISON_VIEW_AUTHORITY"
    ),
    "hidden_repo_state_used_as_comparison_view_content": (
        "HIDDEN_REPO_STATE_USED_AS_COMPARISON_VIEW_CONTENT"
    ),
    "hidden_repo_state_used_as_comparison_view_authority": (
        "HIDDEN_REPO_STATE_USED_AS_COMPARISON_VIEW_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PRIOR_ARTIFACTS_MUTATED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
}

REQUEST_SHORTCUT_FAILURES = {
    "selected_local_relevance_medium_relation_view_artifact_missing": (
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_PATH_MISSING"
    ),
    "local_relevance_medium_relation_view_artifact_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_NOT_RECORDED"
    ),
    "local_relevance_medium_relation_view_artifact_failed_checks_present": (
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "local_relevance_medium_relation_view_artifact_version_not_0_1_0": (
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "local_relevance_medium_relation_view_object_missing": (
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_OBJECT_MISSING"
    ),
    "relation_view_type_not_local_relevance_medium_relation_view": (
        "RELATION_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW"
    ),
    "relation_view_scope_not_two_local_orientation_objects_only": (
        "RELATION_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY"
    ),
    "relation_frame_not_bounded_co_present_local_orientation_objects_only": (
        "RELATION_FRAME_NOT_BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY"
    ),
    "multiplicity_count_not_two": "MULTIPLICITY_COUNT_NOT_TWO",
    "relation_pair_count_not_one": "RELATION_PAIR_COUNT_NOT_ONE",
    "relation_view_artifact_missing": "RELATION_VIEW_ARTIFACT_MISSING",
    "basis_local_relevance_medium_multiplicity_result_artifact_missing": (
        "BASIS_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_MISSING"
    ),
    "first_locator_artifact_missing": "FIRST_LOCATOR_ARTIFACT_MISSING",
    "second_locator_artifact_missing": "SECOND_LOCATOR_ARTIFACT_MISSING",
    "first_orientation_view_artifact_missing": "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "second_orientation_view_artifact_missing": "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "first_receipt_artifact_missing": "FIRST_RECEIPT_ARTIFACT_MISSING",
    "second_receipt_artifact_missing": "SECOND_RECEIPT_ARTIFACT_MISSING",
    "first_reception_artifact_missing": "FIRST_RECEPTION_ARTIFACT_MISSING",
    "second_reception_artifact_missing": "SECOND_RECEPTION_ARTIFACT_MISSING",
    "successor_candidate_admission_artifact_missing": (
        "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_MISSING"
    ),
    "successor_reception_request_artifact_missing": (
        "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_MISSING"
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
    "second_reception_envelope_id_missing": "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
    "comparison_view_type_not_local_relevance_medium_comparison_view": (
        "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
    ),
    "comparison_view_scope_not_two_local_orientation_objects_only": (
        "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY"
    ),
    "comparison_frame_not_bounded_non_ranking_local_comparison_only": (
        "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY"
    ),
    "comparison_pair_count_not_one": "COMPARISON_PAIR_COUNT_NOT_ONE",
    "relation_readable_co_presence_not_preserved": (
        "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED"
    ),
    "comparison_readable_distinctions_not_recorded": (
        "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED"
    ),
    "comparison_view_not_recorded": "COMPARISON_VIEW_NOT_RECORDED",
}


def _utc_timestamp() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str) -> bool:
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _is_official_string(value: str) -> bool:
    return value in OFFICIAL_STRINGS


def _contains_hostile_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in HOSTILE_SENTINELS)


def _sanitize(value: Any, parent_key: str | None = None) -> Any:
    if parent_key and _is_sensitive_key(parent_key):
        return "[REDACTED_RAW_CONTENT]"
    if isinstance(value, Mapping):
        return {str(key): _sanitize(item, str(key)) for key, item in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, parent_key) for item in value]
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if _is_official_string(value):
            return value
        if _contains_hostile_sentinel(value):
            return "[REDACTED_RAW_CONTENT]"
        return value
    return value


def _string_or_empty(value: Any) -> str:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        return value
    return ""


def _present(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _safe_int(value: Any, default: int | None = None) -> int | None:
    if isinstance(value, bool):
        return default
    if isinstance(value, int):
        return value
    return default


def _make_check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
    }
    if not passed:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _append_check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(
        _make_check(
            check_name=check_name,
            passed=passed,
            expected_posture=expected_posture,
            actual_posture=actual_posture,
            code=code,
        )
    )


def _check_counts(checks: list[Mapping[str, Any]]) -> tuple[int, int]:
    passed = sum(1 for check in checks if check.get("passed") is True)
    failed = sum(1 for check in checks if check.get("passed") is not True)
    return passed, failed


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str) and code:
                return code
    return None


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    path_text = _string_or_empty(path_value)
    if not path_text:
        return None, "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_PATH_MISSING"
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_UNREADABLE"
    if not isinstance(loaded, dict):
        return None, "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_NOT_JSON_OBJECT"
    return loaded, None


def _artifact_result_version(artifact: Mapping[str, Any]) -> Any:
    summary = artifact.get("local_relevance_medium_relation_view_summary")
    if isinstance(summary, Mapping) and "result_version" in summary:
        return summary.get("result_version")
    metadata = artifact.get("local_relevance_medium_relation_view_metadata")
    if isinstance(metadata, Mapping):
        for key in (
            "local_relevance_medium_relation_view_version",
            "result_version",
            "relation_view_version",
        ):
            if key in metadata:
                return metadata.get(key)
    relation_view = artifact.get("local_relevance_medium_relation_view")
    if isinstance(relation_view, Mapping) and "relation_view_version" in relation_view:
        return relation_view.get("relation_view_version")
    return artifact.get("result_version")


def _artifact_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    summary = artifact.get("local_relevance_medium_relation_view_summary")
    if isinstance(summary, Mapping):
        value = _safe_int(summary.get("failed_check_count"))
        if value is not None:
            return value
    value = _safe_int(artifact.get("failed_check_count"))
    if value is not None:
        return value
    checks = artifact.get("local_relevance_medium_relation_view_checks")
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _extract_relation_basis(
    artifact: Mapping[str, Any],
    artifact_path: str,
) -> dict[str, Any]:
    relation_view = artifact.get("local_relevance_medium_relation_view")
    if not isinstance(relation_view, Mapping):
        relation_view = {}
    return {
        "relation_artifact": artifact,
        "relation_view": relation_view,
        "basis_local_relevance_medium_relation_view_artifact": artifact_path,
        "basis_local_relevance_medium_relation_view_outcome": artifact.get("outcome"),
        "basis_local_relevance_medium_relation_view_result_version": (
            _artifact_result_version(artifact)
        ),
        "basis_local_relevance_medium_relation_view_failed_check_count": (
            _artifact_failed_check_count(artifact)
        ),
        "relation_view_type": relation_view.get("relation_view_type"),
        "relation_view_scope": relation_view.get("relation_view_scope"),
        "relation_frame": relation_view.get("relation_frame"),
        "basis_local_relevance_medium_multiplicity_result_artifact": relation_view.get(
            "basis_local_relevance_medium_multiplicity_result_artifact"
        ),
        "basis_first_local_relevance_orientation_index_entry_artifact": relation_view.get(
            "basis_first_local_relevance_orientation_index_entry_artifact"
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": relation_view.get(
            "basis_second_local_relevance_orientation_index_entry_artifact"
        ),
        "first_orientation_view_artifact": relation_view.get(
            "first_orientation_view_artifact"
        ),
        "second_orientation_view_artifact": relation_view.get(
            "second_orientation_view_artifact"
        ),
        "first_receipt_artifact": relation_view.get("first_receipt_artifact"),
        "second_receipt_artifact": relation_view.get("second_receipt_artifact"),
        "first_reception_artifact": relation_view.get("first_reception_artifact"),
        "second_reception_artifact": relation_view.get("second_reception_artifact"),
        "successor_candidate_admission_artifact": relation_view.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": relation_view.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": relation_view.get("first_received_signal_id"),
        "second_received_signal_id": relation_view.get("second_received_signal_id"),
        "first_relevance_basis_id": relation_view.get("first_relevance_basis_id"),
        "second_relevance_basis_id": relation_view.get("second_relevance_basis_id"),
        "first_relevance_scope_id": relation_view.get("first_relevance_scope_id"),
        "second_relevance_scope_id": relation_view.get("second_relevance_scope_id"),
        "first_carrier_context_id": relation_view.get("first_carrier_context_id"),
        "second_carrier_context_id": relation_view.get("second_carrier_context_id"),
        "first_reception_envelope_id": relation_view.get(
            "first_reception_envelope_id"
        ),
        "second_reception_envelope_id": relation_view.get(
            "second_reception_envelope_id"
        ),
        "multiplicity_count": relation_view.get("multiplicity_count"),
        "relation_pair_count": relation_view.get("relation_pair_count"),
        "first_and_second_signals_distinct": relation_view.get(
            "first_and_second_signals_distinct"
        ),
        "two_local_orientation_objects_preserved": relation_view.get(
            "two_local_orientation_objects_preserved"
        ),
        "relation_readable_co_presence_recorded": relation_view.get(
            "relation_readable_co_presence_recorded"
        ),
        "relation_view_recorded": relation_view.get("relation_view_recorded"),
    }


def _build_comparison_view(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "comparison_view_id": _string_or_empty(
            declared.get("local_relevance_medium_comparison_view_id")
        )
        or DEFAULT_COMPARISON_VIEW_ID,
        "comparison_view_type": COMPARISON_VIEW_TYPE,
        "comparison_view_version": RESULT_VERSION,
        "comparison_view_scope": COMPARISON_VIEW_SCOPE,
        "comparison_frame": COMPARISON_FRAME,
        "basis_local_relevance_medium_relation_view_artifact": basis.get(
            "basis_local_relevance_medium_relation_view_artifact"
        ),
        "basis_local_relevance_medium_relation_view_outcome": basis.get(
            "basis_local_relevance_medium_relation_view_outcome"
        ),
        "basis_local_relevance_medium_relation_view_result_version": basis.get(
            "basis_local_relevance_medium_relation_view_result_version"
        ),
        "basis_local_relevance_medium_relation_view_failed_check_count": basis.get(
            "basis_local_relevance_medium_relation_view_failed_check_count"
        ),
        "basis_local_relevance_medium_multiplicity_result_artifact": basis.get(
            "basis_local_relevance_medium_multiplicity_result_artifact"
        ),
        "basis_first_local_relevance_orientation_index_entry_artifact": basis.get(
            "basis_first_local_relevance_orientation_index_entry_artifact"
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": basis.get(
            "basis_second_local_relevance_orientation_index_entry_artifact"
        ),
        "first_orientation_view_artifact": basis.get("first_orientation_view_artifact"),
        "second_orientation_view_artifact": basis.get(
            "second_orientation_view_artifact"
        ),
        "first_receipt_artifact": basis.get("first_receipt_artifact"),
        "second_receipt_artifact": basis.get("second_receipt_artifact"),
        "first_reception_artifact": basis.get("first_reception_artifact"),
        "second_reception_artifact": basis.get("second_reception_artifact"),
        "successor_candidate_admission_artifact": basis.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": basis.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": basis.get("first_received_signal_id"),
        "second_received_signal_id": basis.get("second_received_signal_id"),
        "first_relevance_basis_id": basis.get("first_relevance_basis_id"),
        "second_relevance_basis_id": basis.get("second_relevance_basis_id"),
        "first_relevance_scope_id": basis.get("first_relevance_scope_id"),
        "second_relevance_scope_id": basis.get("second_relevance_scope_id"),
        "first_carrier_context_id": basis.get("first_carrier_context_id"),
        "second_carrier_context_id": basis.get("second_carrier_context_id"),
        "first_reception_envelope_id": basis.get("first_reception_envelope_id"),
        "second_reception_envelope_id": basis.get("second_reception_envelope_id"),
        "multiplicity_count": 2,
        "relation_pair_count": 1,
        "comparison_pair_count": 1,
        "first_and_second_signals_distinct": True,
        "two_local_orientation_objects_preserved": True,
        "relation_readable_co_presence_preserved": True,
        "comparison_readable_distinctions_recorded": True,
        "comparison_view_recorded": True,
        "ranking_surface_created": False,
        "scoring_surface_created": False,
        "priority_surface_created": False,
        "validity_judgment_created": False,
        "truth_judgment_created": False,
        "authority_judgment_created": False,
        "currentness_judgment_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_created": False,
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


def _empty_comparison_view(declared: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "comparison_view_id": _string_or_empty(
            declared.get("local_relevance_medium_comparison_view_id")
        )
        or DEFAULT_COMPARISON_VIEW_ID,
        "comparison_view_type": _sanitize(declared.get("comparison_view_type")),
        "comparison_view_version": RESULT_VERSION,
        "comparison_view_scope": _sanitize(declared.get("comparison_view_scope")),
        "comparison_frame": _sanitize(declared.get("comparison_frame")),
        "comparison_view_recorded": False,
        "comparison_readable_distinctions_recorded": False,
    }


def _recorded_statement() -> dict[str, bool]:
    return {
        "local_relevance_medium_comparison_view_recorded": True,
        "basis_local_relevance_medium_relation_view_artifact_preserved": True,
        "basis_local_relevance_medium_multiplicity_result_artifact_preserved": True,
        "basis_first_local_relevance_orientation_index_entry_artifact_preserved": True,
        "basis_second_local_relevance_orientation_index_entry_artifact_preserved": True,
        "first_orientation_view_artifact_preserved": True,
        "second_orientation_view_artifact_preserved": True,
        "first_receipt_artifact_preserved": True,
        "second_receipt_artifact_preserved": True,
        "first_reception_artifact_preserved": True,
        "second_reception_artifact_preserved": True,
        "successor_candidate_admission_artifact_preserved": True,
        "successor_reception_request_artifact_preserved": True,
        "first_received_signal_id_preserved": True,
        "second_received_signal_id_preserved": True,
        "first_and_second_signals_distinct": True,
        "first_relevance_basis_id_preserved": True,
        "second_relevance_basis_id_preserved": True,
        "first_relevance_scope_id_preserved": True,
        "second_relevance_scope_id_preserved": True,
        "first_carrier_context_id_preserved": True,
        "second_carrier_context_id_preserved": True,
        "first_reception_envelope_id_preserved": True,
        "second_reception_envelope_id_preserved": True,
        "comparison_view_scope_local_only": True,
        "comparison_frame_bounded_non_ranking_only": True,
        "comparison_pair_count_is_one": True,
        "relation_readable_co_presence_preserved": True,
        "comparison_readable_distinctions_recorded": True,
        "result_level_non_claims_canonical_false": True,
    }


def _blocked_statement() -> dict[str, bool]:
    return {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _non_meaning() -> dict[str, bool]:
    non_claims = _canonical_non_claims()
    return {
        "ranking_scoring_priority_validity_truth_authority_currentness_not_created": True,
        "index_system_registry_search_ranking_not_created": True,
        "repeated_reception_permission_arbitrary_reception_feed_not_created": True,
        "source_transfer_source_receipt_not_created": True,
        "runtime_api_distributed_follow_on_not_created": True,
        **non_claims,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium comparison view resolver successor work, if separately selected",
        "local relevance orientation index system",
        "registry",
        "search surface",
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


def _selected_basis_summary(basis: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "basis_local_relevance_medium_relation_view_artifact": basis.get(
            "basis_local_relevance_medium_relation_view_artifact"
        ),
        "basis_local_relevance_medium_relation_view_outcome": basis.get(
            "basis_local_relevance_medium_relation_view_outcome"
        ),
        "basis_local_relevance_medium_relation_view_result_version": basis.get(
            "basis_local_relevance_medium_relation_view_result_version"
        ),
        "basis_local_relevance_medium_relation_view_failed_check_count": basis.get(
            "basis_local_relevance_medium_relation_view_failed_check_count"
        ),
        "relation_view_type": basis.get("relation_view_type"),
        "relation_view_scope": basis.get("relation_view_scope"),
        "relation_frame": basis.get("relation_frame"),
        "multiplicity_count": basis.get("multiplicity_count"),
        "relation_pair_count": basis.get("relation_pair_count"),
    }


def _resolve_declared_non_claims(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    declared_non_claims = declared.get("declared_non_claims")
    if not isinstance(declared_non_claims, Mapping):
        _append_check(
            checks,
            "required declared non-claims mapping present",
            False,
            "mapping with all required false non-claims",
            type(declared_non_claims).__name__,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
        return

    for key in REQUIRED_FALSE_NON_CLAIMS:
        value = declared_non_claims.get(key)
        passed = value is False
        _append_check(
            checks,
            f"declared non-claim {key} is false",
            passed,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_request(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get("local_relevance_medium_comparison_view_question")
    intent = declared.get("local_relevance_medium_comparison_view_intent")

    _append_check(
        checks,
        "comparison view question declared",
        _present(question),
        "declared comparison view question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "comparison view intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_INTENT_UNSUPPORTED",
    )
    _append_check(
        checks,
        "comparison view block intent not requested",
        intent != BLOCK_INTENT,
        f"not {BLOCK_INTENT}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_BLOCK_REQUESTED",
    )

    artifact = declared.get("selected_local_relevance_medium_relation_view_artifact")
    _append_check(
        checks,
        "selected local relevance medium relation view artifact path declared",
        _present(_string_or_empty(artifact)),
        "declared path",
        artifact,
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_PATH_MISSING",
    )

    comparison_view_type = declared.get("comparison_view_type")
    _append_check(
        checks,
        "comparison view type declared",
        _present(_string_or_empty(comparison_view_type)),
        COMPARISON_VIEW_TYPE,
        comparison_view_type,
        "COMPARISON_VIEW_TYPE_MISSING",
    )
    _append_check(
        checks,
        "comparison view type exact",
        comparison_view_type == COMPARISON_VIEW_TYPE,
        COMPARISON_VIEW_TYPE,
        comparison_view_type,
        "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW",
    )

    comparison_view_scope = declared.get("comparison_view_scope")
    _append_check(
        checks,
        "comparison view scope declared",
        _present(_string_or_empty(comparison_view_scope)),
        COMPARISON_VIEW_SCOPE,
        comparison_view_scope,
        "COMPARISON_VIEW_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "comparison view scope two local orientation objects only",
        comparison_view_scope == COMPARISON_VIEW_SCOPE,
        COMPARISON_VIEW_SCOPE,
        comparison_view_scope,
        "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    )

    comparison_frame = declared.get("comparison_frame")
    _append_check(
        checks,
        "comparison frame declared",
        _present(_string_or_empty(comparison_frame)),
        COMPARISON_FRAME,
        comparison_frame,
        "COMPARISON_FRAME_MISSING",
    )
    _append_check(
        checks,
        "comparison frame bounded non-ranking local comparison only",
        comparison_frame == COMPARISON_FRAME,
        COMPARISON_FRAME,
        comparison_frame,
        "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
    )

    _resolve_declared_non_claims(declared, checks)


def _validate_relation_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    artifact_path = _string_or_empty(
        declared.get("selected_local_relevance_medium_relation_view_artifact")
    )
    artifact, read_error = _read_json_object(artifact_path)
    if read_error:
        _append_check(
            checks,
            "selected local relevance medium relation view artifact readable JSON object",
            False,
            "readable JSON object",
            read_error,
            read_error,
        )
        return _extract_relation_basis({}, artifact_path)

    _append_check(
        checks,
        "selected local relevance medium relation view artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )
    basis = _extract_relation_basis(artifact, artifact_path)

    _append_check(
        checks,
        "local relevance medium relation view artifact outcome recorded",
        basis.get("basis_local_relevance_medium_relation_view_outcome")
        == RELATION_VIEW_RECORDED_OUTCOME,
        RELATION_VIEW_RECORDED_OUTCOME,
        basis.get("basis_local_relevance_medium_relation_view_outcome"),
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "local relevance medium relation view artifact result version 0.1.0",
        basis.get("basis_local_relevance_medium_relation_view_result_version")
        == RESULT_VERSION,
        RESULT_VERSION,
        basis.get("basis_local_relevance_medium_relation_view_result_version"),
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "local relevance medium relation view artifact failed check count zero",
        basis.get("basis_local_relevance_medium_relation_view_failed_check_count") == 0,
        0,
        basis.get("basis_local_relevance_medium_relation_view_failed_check_count"),
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    relation_view = basis.get("relation_view")
    _append_check(
        checks,
        "local relevance medium relation view object present",
        isinstance(relation_view, Mapping) and bool(relation_view),
        "local_relevance_medium_relation_view object",
        bool(relation_view) if isinstance(relation_view, Mapping) else type(relation_view).__name__,
        "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_OBJECT_MISSING",
    )
    return basis


def _validate_relation_basis(
    basis: Mapping[str, Any],
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "relation view type exact",
        basis.get("relation_view_type") == RELATION_VIEW_TYPE,
        RELATION_VIEW_TYPE,
        basis.get("relation_view_type"),
        "RELATION_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
    )
    _append_check(
        checks,
        "relation view scope two local orientation objects only",
        basis.get("relation_view_scope") == RELATION_VIEW_SCOPE,
        RELATION_VIEW_SCOPE,
        basis.get("relation_view_scope"),
        "RELATION_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    )
    _append_check(
        checks,
        "relation frame bounded co-present local orientation objects only",
        basis.get("relation_frame") == RELATION_FRAME,
        RELATION_FRAME,
        basis.get("relation_frame"),
        "RELATION_FRAME_NOT_BOUNDED_CO_PRESENT_LOCAL_ORIENTATION_OBJECTS_ONLY",
    )
    _append_check(
        checks,
        "multiplicity count exactly two",
        basis.get("multiplicity_count") == 2,
        2,
        basis.get("multiplicity_count"),
        "MULTIPLICITY_COUNT_NOT_TWO",
    )
    _append_check(
        checks,
        "relation pair count exactly one",
        basis.get("relation_pair_count") == 1,
        1,
        basis.get("relation_pair_count"),
        "RELATION_PAIR_COUNT_NOT_ONE",
    )

    required_paths = (
        (
            "basis local relevance medium relation view artifact preserved",
            "basis_local_relevance_medium_relation_view_artifact",
            "RELATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "basis local relevance medium multiplicity result artifact preserved",
            "basis_local_relevance_medium_multiplicity_result_artifact",
            "BASIS_LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_ARTIFACT_MISSING",
        ),
        (
            "first locator artifact preserved",
            "basis_first_local_relevance_orientation_index_entry_artifact",
            "FIRST_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "second locator artifact preserved",
            "basis_second_local_relevance_orientation_index_entry_artifact",
            "SECOND_LOCATOR_ARTIFACT_MISSING",
        ),
        (
            "first orientation view artifact preserved",
            "first_orientation_view_artifact",
            "FIRST_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "second orientation view artifact preserved",
            "second_orientation_view_artifact",
            "SECOND_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        ("first receipt artifact preserved", "first_receipt_artifact", "FIRST_RECEIPT_ARTIFACT_MISSING"),
        (
            "second receipt artifact preserved",
            "second_receipt_artifact",
            "SECOND_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "first reception artifact preserved",
            "first_reception_artifact",
            "FIRST_RECEPTION_ARTIFACT_MISSING",
        ),
        (
            "second reception artifact preserved",
            "second_reception_artifact",
            "SECOND_RECEPTION_ARTIFACT_MISSING",
        ),
        (
            "successor candidate admission artifact preserved",
            "successor_candidate_admission_artifact",
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_MISSING",
        ),
        (
            "successor reception request artifact preserved",
            "successor_reception_request_artifact",
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_MISSING",
        ),
    )
    for check_name, key, code in required_paths:
        _append_check(checks, check_name, _present(basis.get(key)), "present path", basis.get(key), code)

    expected_identifiers = (
        (
            "first received signal id preserved",
            "first_received_signal_id",
            FIRST_RECEIVED_SIGNAL_ID,
            "FIRST_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "second received signal id preserved",
            "second_received_signal_id",
            SECOND_RECEIVED_SIGNAL_ID,
            "SECOND_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "first relevance basis id preserved",
            "first_relevance_basis_id",
            FIRST_RELEVANCE_BASIS_ID,
            "FIRST_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "second relevance basis id preserved",
            "second_relevance_basis_id",
            SECOND_RELEVANCE_BASIS_ID,
            "SECOND_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "first relevance scope id preserved",
            "first_relevance_scope_id",
            FIRST_RELEVANCE_SCOPE_ID,
            "FIRST_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "second relevance scope id preserved",
            "second_relevance_scope_id",
            SECOND_RELEVANCE_SCOPE_ID,
            "SECOND_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "first carrier context id preserved",
            "first_carrier_context_id",
            FIRST_CARRIER_CONTEXT_ID,
            "FIRST_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "second carrier context id preserved",
            "second_carrier_context_id",
            SECOND_CARRIER_CONTEXT_ID,
            "SECOND_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "first reception envelope id preserved",
            "first_reception_envelope_id",
            FIRST_RECEPTION_ENVELOPE_ID,
            "FIRST_RECEPTION_ENVELOPE_ID_MISSING",
        ),
        (
            "second reception envelope id preserved",
            "second_reception_envelope_id",
            SECOND_RECEPTION_ENVELOPE_ID,
            "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
        ),
    )
    for check_name, key, expected, code in expected_identifiers:
        _append_check(checks, check_name, basis.get(key) == expected, expected, basis.get(key), code)

    first_signal = basis.get("first_received_signal_id")
    second_signal = basis.get("second_received_signal_id")
    _append_check(
        checks,
        "first and second received signal ids distinct",
        first_signal == FIRST_RECEIVED_SIGNAL_ID
        and second_signal == SECOND_RECEIVED_SIGNAL_ID
        and first_signal != second_signal
        and basis.get("first_and_second_signals_distinct") is True,
        "distinct first and second received signal ids",
        {
            "first_received_signal_id": first_signal,
            "second_received_signal_id": second_signal,
            "first_and_second_signals_distinct": basis.get(
                "first_and_second_signals_distinct"
            ),
        },
        "FIRST_AND_SECOND_RECEIVED_SIGNAL_IDS_NOT_DISTINCT",
    )

    _append_check(
        checks,
        "relation-readable co-presence preserved",
        basis.get("relation_readable_co_presence_recorded") is True,
        True,
        basis.get("relation_readable_co_presence_recorded"),
        "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED",
    )

    _append_check(
        checks,
        "comparison pair count exactly one",
        declared.get("comparison_pair_count", 1) == 1,
        1,
        declared.get("comparison_pair_count", 1),
        "COMPARISON_PAIR_COUNT_NOT_ONE",
    )
    _append_check(
        checks,
        "comparison-readable distinctions recorded",
        declared.get("comparison_readable_distinctions_recorded", True) is True,
        True,
        declared.get("comparison_readable_distinctions_recorded", True),
        "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED",
    )
    _append_check(
        checks,
        "comparison view recorded",
        declared.get("comparison_view_recorded", True) is True,
        True,
        declared.get("comparison_view_recorded", True),
        "COMPARISON_VIEW_NOT_RECORDED",
    )


def _validate_false_postures(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key, code in REQUEST_SHORTCUT_FAILURES.items():
        value = declared.get(key, False)
        _append_check(
            checks,
            f"shortcut {key} not asserted",
            value is False,
            False,
            value,
            code,
        )

    for key, code in FALSE_POSTURE_TO_BLOCK_CODE.items():
        value = declared.get(key, False)
        _append_check(
            checks,
            f"{key} not created",
            value is False,
            False,
            value,
            code,
        )

    _append_check(
        checks,
        "predecessor failure evidence preserved",
        declared.get("predecessor_failure_repaired", False) is False
        and declared.get("predecessor_failure_hidden", False) is False
        and declared.get("predecessor_failure_claimed_passed", False) is False,
        "predecessor failure evidence preserved",
        {
            "predecessor_failure_repaired": declared.get(
                "predecessor_failure_repaired", False
            ),
            "predecessor_failure_hidden": declared.get(
                "predecessor_failure_hidden", False
            ),
            "predecessor_failure_claimed_passed": declared.get(
                "predecessor_failure_claimed_passed", False
            ),
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


def _requested_outcome(declared: Mapping[str, Any]) -> str | None:
    value = declared.get("requested_local_relevance_medium_comparison_view_outcome")
    if value in OUTCOME_FAMILY:
        return str(value)
    return None


def _build_block(outcome: str, checks: list[Mapping[str, Any]]) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }
    code = _first_failed_code(checks) or "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_MALFORMED"
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": "local relevance medium comparison view was blocked by bounded validation",
    }


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    _, failed_count = _check_counts(checks)
    if failed_count:
        return OUTCOME_BLOCKED
    intent = declared.get("local_relevance_medium_comparison_view_intent")
    requested = _requested_outcome(declared)
    if requested == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if requested == OUTCOME_NOT_RECORDED or intent == DO_NOT_RECORD_INTENT:
        return OUTCOME_NOT_RECORDED
    if declared.get("additional_basis_context"):
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS
    if declared.get("not_recorded_basis"):
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _assemble_result(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
    comparison_view: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    passed_count, failed_count = _check_counts(checks)
    statement = _recorded_statement() if outcome == OUTCOME_RECORDED else _blocked_statement()
    metadata = {
        "local_relevance_medium_comparison_view_id": comparison_view.get(
            "comparison_view_id", DEFAULT_COMPARISON_VIEW_ID
        ),
        "local_relevance_medium_comparison_view_type": COMPARISON_VIEW_TYPE,
        "local_relevance_medium_comparison_view_version": RESULT_VERSION,
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_comparison_view_metadata": metadata,
        "declared_local_relevance_medium_comparison_view_question": {
            "question": _sanitize(
                declared.get("local_relevance_medium_comparison_view_question")
            ),
            "intent": _sanitize(
                declared.get("local_relevance_medium_comparison_view_intent")
            ),
        },
        "selected_local_relevance_medium_relation_view_artifact_basis": _sanitize(
            _selected_basis_summary(basis)
        ),
        "local_relevance_medium_comparison_view": _sanitize(dict(comparison_view)),
        "local_relevance_medium_comparison_view_checks": _sanitize(checks),
        "local_relevance_medium_comparison_view_statement": statement,
        "local_relevance_medium_comparison_view_non_meaning": _non_meaning(),
        "additional_basis_required": _sanitize(
            declared.get("additional_basis_context", [])
            if outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS
            else []
        ),
        "not_recorded_basis": _sanitize(
            declared.get("not_recorded_basis", []) if outcome == OUTCOME_NOT_RECORDED else []
        ),
        "what_remains_open": _what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": _build_block(outcome, checks),
    }
    result["local_relevance_medium_comparison_view_summary"] = (
        build_local_relevance_medium_comparison_view_v0_min_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_comparison_view_v0_min(
    declared_local_relevance_medium_comparison_view: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded local relevance medium comparison view result."""

    checks: list[dict[str, Any]] = []
    if declared_local_relevance_medium_comparison_view is None:
        declared: Mapping[str, Any] = {}
        _append_check(
            checks,
            "declared local relevance medium comparison view request present",
            False,
            "request mapping",
            None,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_MALFORMED",
        )
        basis = _extract_relation_basis({}, "")
        comparison_view = _empty_comparison_view(declared)
        return _assemble_result(declared, basis, comparison_view, checks, OUTCOME_BLOCKED)

    if not isinstance(declared_local_relevance_medium_comparison_view, Mapping):
        declared = {}
        _append_check(
            checks,
            "declared local relevance medium comparison view request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_comparison_view).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_MALFORMED",
        )
        basis = _extract_relation_basis({}, "")
        comparison_view = _empty_comparison_view(declared)
        return _assemble_result(declared, basis, comparison_view, checks, OUTCOME_BLOCKED)

    declared_copy = copy.deepcopy(dict(declared_local_relevance_medium_comparison_view))
    _validate_request(declared_copy, checks)
    basis = _validate_relation_artifact(declared_copy, checks)
    _validate_relation_basis(basis, declared_copy, checks)
    _validate_false_postures(declared_copy, checks)

    provisional_outcome = _determine_outcome(declared_copy, checks)
    if provisional_outcome == OUTCOME_RECORDED:
        comparison_view = _build_comparison_view(declared_copy, basis)
    else:
        comparison_view = _empty_comparison_view(declared_copy)
    return _assemble_result(
        declared_copy,
        basis,
        comparison_view,
        checks,
        provisional_outcome,
    )


def resolve_local_relevance_medium_comparison_view_v0_min_from_path(
    declared_local_relevance_medium_comparison_view_path: Path | str,
) -> dict:
    """Read a declared comparison-view request JSON object and resolve it."""

    try:
        with Path(declared_local_relevance_medium_comparison_view_path).open(
            "r", encoding="utf-8"
        ) as handle:
            request = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local relevance medium comparison view request readable",
                False,
                "readable JSON object",
                "unreadable",
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_UNREADABLE",
            )
        ]
        declared: dict[str, Any] = {}
        basis = _extract_relation_basis({}, "")
        return _assemble_result(
            declared,
            basis,
            _empty_comparison_view(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    if not isinstance(request, Mapping):
        checks = [
            _make_check(
                "declared local relevance medium comparison view request object",
                False,
                "JSON object",
                type(request).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_REQUEST_MALFORMED",
            )
        ]
        declared = {}
        basis = _extract_relation_basis({}, "")
        return _assemble_result(
            declared,
            basis,
            _empty_comparison_view(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    return resolve_local_relevance_medium_comparison_view_v0_min(request)


def build_local_relevance_medium_comparison_view_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary from a comparison-view resolver result."""

    metadata = result.get("local_relevance_medium_comparison_view_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    statement = result.get("local_relevance_medium_comparison_view_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    question = result.get("declared_local_relevance_medium_comparison_view_question", {})
    if not isinstance(question, Mapping):
        question = {}
    comparison_view = result.get("local_relevance_medium_comparison_view", {})
    if not isinstance(comparison_view, Mapping):
        comparison_view = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {"blocked": False, "code": None, "block_code": None, "reason": None}
    checks = result.get("local_relevance_medium_comparison_view_checks", [])
    if not isinstance(checks, list):
        checks = []
    passed_count, failed_count = _check_counts(
        [check for check in checks if isinstance(check, Mapping)]
    )
    non_claims = result.get("non_claims", {})
    if not isinstance(non_claims, Mapping):
        non_claims = {}

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("block_code") or block.get("code"),
        "block_reason": block.get("reason"),
        "comparison_view_id": comparison_view.get("comparison_view_id")
        or metadata.get("local_relevance_medium_comparison_view_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_count or metadata.get("passed_check_count", 0),
        "failed_check_count": failed_count or metadata.get("failed_check_count", 0),
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "comparison_view_recorded": bool(
            statement.get("local_relevance_medium_comparison_view_recorded")
        ),
        "relation_view_artifact_preserved": bool(
            statement.get("basis_local_relevance_medium_relation_view_artifact_preserved")
        ),
        "multiplicity_result_artifact_preserved": bool(
            statement.get(
                "basis_local_relevance_medium_multiplicity_result_artifact_preserved"
            )
        ),
        "first_locator_artifact_preserved": bool(
            statement.get(
                "basis_first_local_relevance_orientation_index_entry_artifact_preserved"
            )
        ),
        "second_locator_artifact_preserved": bool(
            statement.get(
                "basis_second_local_relevance_orientation_index_entry_artifact_preserved"
            )
        ),
        "first_orientation_view_artifact_preserved": bool(
            statement.get("first_orientation_view_artifact_preserved")
        ),
        "second_orientation_view_artifact_preserved": bool(
            statement.get("second_orientation_view_artifact_preserved")
        ),
        "first_receipt_artifact_preserved": bool(
            statement.get("first_receipt_artifact_preserved")
        ),
        "second_receipt_artifact_preserved": bool(
            statement.get("second_receipt_artifact_preserved")
        ),
        "first_reception_artifact_preserved": bool(
            statement.get("first_reception_artifact_preserved")
        ),
        "second_reception_artifact_preserved": bool(
            statement.get("second_reception_artifact_preserved")
        ),
        "successor_candidate_admission_artifact_preserved": bool(
            statement.get("successor_candidate_admission_artifact_preserved")
        ),
        "successor_reception_request_artifact_preserved": bool(
            statement.get("successor_reception_request_artifact_preserved")
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
        "comparison_view_scope_local_only": bool(
            statement.get("comparison_view_scope_local_only")
        ),
        "comparison_frame_bounded_non_ranking_only": bool(
            statement.get("comparison_frame_bounded_non_ranking_only")
        ),
        "comparison_pair_count_is_one": bool(
            statement.get("comparison_pair_count_is_one")
        ),
        "relation_readable_co_presence_preserved": bool(
            statement.get("relation_readable_co_presence_preserved")
        ),
        "comparison_readable_distinctions_recorded": bool(
            statement.get("comparison_readable_distinctions_recorded")
        ),
        "comparison_view_object_summary": {
            "comparison_view_type": comparison_view.get("comparison_view_type"),
            "comparison_view_scope": comparison_view.get("comparison_view_scope"),
            "comparison_frame": comparison_view.get("comparison_frame"),
            "multiplicity_count": comparison_view.get("multiplicity_count"),
            "relation_pair_count": comparison_view.get("relation_pair_count"),
            "comparison_pair_count": comparison_view.get("comparison_pair_count"),
        },
        "ranking_scoring_priority_validity_truth_authority_currentness_not_created": all(
            non_claims.get(key) is False
            for key in (
                "ranking_surface_created",
                "scoring_surface_created",
                "priority_surface_created",
                "validity_judgment_created",
                "truth_judgment_created",
                "authority_judgment_created",
                "currentness_judgment_created",
            )
        ),
        "index_system_registry_search_ranking_not_created": all(
            non_claims.get(key) is False
            for key in (
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_created",
            )
        ),
        "repeated_reception_permission_arbitrary_reception_feed_not_created": all(
            non_claims.get(key) is False
            for key in (
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
            )
        ),
        "source_authority_currentness_truth_action_synchronization_participation_runtime_not_created": all(
            non_claims.get(key) is False
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
        "public_api_participant_interface_distributed_not_created": all(
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
        "key_non_claims": _canonical_non_claims(),
        "predecessor_failure_evidence_preserved": True,
        "result_level_non_claims_canonical_false": all(
            non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _next_available_path(path: Path) -> Path:
    if not path.exists():
        return path
    stem = path.stem
    suffix = path.suffix
    parent = path.parent
    index = 1
    while True:
        candidate = parent / f"{stem}_{index:03d}{suffix}"
        if not candidate.exists():
            return candidate
        index += 1


def write_local_relevance_medium_comparison_view_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a comparison-view result JSON without overwriting existing files."""

    if output_path is None:
        comparison_view = result.get("local_relevance_medium_comparison_view", {})
        if not isinstance(comparison_view, Mapping):
            comparison_view = {}
        comparison_view_id = _string_or_empty(comparison_view.get("comparison_view_id"))
        if not comparison_view_id:
            comparison_view_id = DEFAULT_COMPARISON_VIEW_ID
        output_path = (
            OUTPUT_ROOT
            / f"{comparison_view_id}__local_relevance_medium_comparison_view_v0_min_result.json"
        )
    else:
        output_path = Path(output_path)

    path = _next_available_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_comparison_view_v0_min_request(
    *,
    local_relevance_medium_comparison_view_id: str = DEFAULT_COMPARISON_VIEW_ID,
    selected_local_relevance_medium_relation_view_artifact: Path | str = DEFAULT_RELATION_VIEW_ARTIFACT,
    comparison_view_type: str = COMPARISON_VIEW_TYPE,
    comparison_view_scope: str = COMPARISON_VIEW_SCOPE,
    comparison_frame: str = COMPARISON_FRAME,
    local_relevance_medium_comparison_view_intent: str = RECORD_INTENT,
    declared_non_claims: Mapping[str, Any] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a declared request for one local relevance medium comparison view."""

    non_claims = (
        copy.deepcopy(dict(declared_non_claims))
        if isinstance(declared_non_claims, Mapping)
        else _canonical_non_claims()
    )
    request: dict[str, Any] = {
        "local_relevance_medium_comparison_view_id": local_relevance_medium_comparison_view_id,
        "local_relevance_medium_comparison_view_question": (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW, may one "
            "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW be recorded that records "
            "bounded comparison-readable distinctions between exactly two locally "
            "discoverable orientation objects without creating index system, "
            "registry, search, ranking, scoring, priority, validity judgment, "
            "truth judgment, authority, currentness, action, synchronization, "
            "participation authorization, participant role, runtime permission, "
            "public API, participant-facing interface, distributed network "
            "behavior, operation permission, repeated reception permission, "
            "arbitrary reception, feed, source transfer, source receipt, or "
            "follow-on work?"
        ),
        "local_relevance_medium_comparison_view_intent": (
            local_relevance_medium_comparison_view_intent
        ),
        "selected_local_relevance_medium_relation_view_artifact": str(
            selected_local_relevance_medium_relation_view_artifact
        ),
        "comparison_view_scope": comparison_view_scope,
        "comparison_view_type": comparison_view_type,
        "comparison_frame": comparison_frame,
        "comparison_pair_count": 1,
        "comparison_readable_distinctions_recorded": True,
        "comparison_view_recorded": True,
        "declared_non_claims": non_claims,
    }
    request.update(extra_fields)
    return request
