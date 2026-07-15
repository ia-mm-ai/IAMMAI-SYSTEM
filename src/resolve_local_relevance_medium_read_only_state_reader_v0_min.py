"""Resolve one local relevance medium read-only state reader result.

This resolver reads one clean LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW artifact
as primary basis and records one LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET.
It reconstructs the known local medium artifact chain, preserves selected paths,
standing identifiers, comparison-readability, relation-readability, and local
multiplicity standing, while keeping result-level non-claims canonical false.

It is read-only state reconstruction only. It accepts no new signal, creates no
new relevance object, reception, receipt, orientation view, index entry,
multiplicity result, relation view, comparison view, index system, registry,
search, ranking, scoring, priority, validity judgment, truth judgment,
authority judgment, currentness judgment, repeated reception permission,
arbitrary reception, feed, source, runtime permission, API, distributed
behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping


class LocalRelevanceMediumReadOnlyStateReaderV0MinError(Exception):
    """Bounded resolver error for read-only state reader request handling."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_read_only_state_reader_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_state_reader_v0_min"
)

DEFAULT_COMPARISON_VIEW_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_comparison_view_v0_min/"
    "local_relevance_medium_comparison_view_reference_review_001__"
    "local_relevance_medium_comparison_view_v0_min_result.json"
)

DEFAULT_STATE_READER_ID = "local_relevance_medium_read_only_state_reader_001"
DEFAULT_STATE_PACKET_ID = "local_relevance_medium_read_only_state_packet_001"

STATE_PACKET_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET"
STATE_READER_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
STATE_READER_SCOPE = "READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY"

COMPARISON_VIEW_TYPE = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
COMPARISON_VIEW_SCOPE = "TWO_LOCAL_ORIENTATION_OBJECTS_COMPARISON_VIEW_ONLY"
COMPARISON_FRAME = "BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY"
COMPARISON_VIEW_RECORDED_OUTCOME = "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_RECORDED"

RECORD_INTENT = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
DO_NOT_RECORD_INTENT = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
BLOCK_INTENT = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER"
SUPPORTED_INTENTS = (RECORD_INTENT, DO_NOT_RECORD_INTENT, BLOCK_INTENT)

SUPPORTED_STATE_PACKET_TYPE_VALUES = (STATE_PACKET_TYPE,)
SUPPORTED_STATE_READER_TYPE_VALUES = (STATE_READER_TYPE,)
SUPPORTED_STATE_READER_SCOPE_VALUES = (STATE_READER_SCOPE,)

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

DEFAULT_VALIDATED_STANDING_ARTIFACTS = {
    "bounded_relevance_reception": (
        "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_reception_v0_min/"
        "bounded_relevance_reception_reference_review_001__"
        "bounded_relevance_reception_v0_min_result.json"
    ),
    "bounded_relevance_receipt_v2": (
        "artifacts/integrity_host_v0_min_coexistence_bounded_relevance_receipt_v0_min_v2/"
        "bounded_relevance_receipt_reference_review_001__"
        "bounded_relevance_receipt_v0_min_v2_result.json"
    ),
    "relevance_orientation_view": (
        "artifacts/integrity_host_v0_min_coexistence_relevance_orientation_view_v0_min/"
        "relevance_orientation_view_reference_review_001__"
        "relevance_orientation_view_v0_min_result.json"
    ),
    "local_relevance_orientation_index_entry": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
        "local_relevance_orientation_index_entry_reference_review_001__"
        "local_relevance_orientation_index_entry_v0_min_result.json"
    ),
    "local_relevance_medium_successor_reception_request": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min/"
        "local_relevance_medium_successor_reception_request_reference_review_001__"
        "local_relevance_medium_successor_reception_request_v0_min_result.json"
    ),
    "local_relevance_medium_successor_candidate_admission": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
        "local_relevance_medium_successor_candidate_admission_reference_review_001__"
        "local_relevance_medium_successor_candidate_admission_v0_min_result.json"
    ),
    "local_relevance_medium_second_bounded_relevance_reception": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min/"
        "local_relevance_medium_second_bounded_relevance_reception_reference_review_001__"
        "local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
    ),
    "local_relevance_medium_second_bounded_relevance_receipt": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_receipt_v0_min/"
        "local_relevance_medium_second_bounded_relevance_receipt_reference_review_001__"
        "local_relevance_medium_second_bounded_relevance_receipt_v0_min_result.json"
    ),
    "local_relevance_medium_second_relevance_orientation_view": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_relevance_orientation_view_v0_min/"
        "local_relevance_medium_second_relevance_orientation_view_reference_review_001__"
        "local_relevance_medium_second_relevance_orientation_view_v0_min_result.json"
    ),
    "local_relevance_medium_second_local_relevance_orientation_index_entry": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min/"
        "local_relevance_medium_second_local_relevance_orientation_index_entry_reference_review_001__"
        "local_relevance_medium_second_local_relevance_orientation_index_entry_v0_min_result.json"
    ),
    "local_relevance_medium_multiplicity_result": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_multiplicity_result_v0_min/"
        "local_relevance_medium_multiplicity_result_reference_review_001__"
        "local_relevance_medium_multiplicity_result_v0_min_result.json"
    ),
    "local_relevance_medium_relation_view": (
        "artifacts/integrity_host_v0_min_coexistence_local_relevance_medium_relation_view_v0_min/"
        "local_relevance_medium_relation_view_reference_review_001__"
        "local_relevance_medium_relation_view_v0_min_result.json"
    ),
    "local_relevance_medium_comparison_view": str(DEFAULT_COMPARISON_VIEW_ARTIFACT),
}

EXPECTED_ARTIFACT_OUTCOMES = {
    "bounded_relevance_reception": "BOUNDED_RELEVANCE_RECEPTION_RECORDED",
    "bounded_relevance_receipt_v2": "BOUNDED_RELEVANCE_RECEIPT_RECORDED",
    "relevance_orientation_view": "RELEVANCE_ORIENTATION_VIEW_RECORDED",
    "local_relevance_orientation_index_entry": (
        "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
    ),
    "local_relevance_medium_successor_reception_request": (
        "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_RECORDED"
    ),
    "local_relevance_medium_successor_candidate_admission": (
        "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED"
    ),
    "local_relevance_medium_second_bounded_relevance_reception": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_RECORDED"
    ),
    "local_relevance_medium_second_bounded_relevance_receipt": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT_RECORDED"
    ),
    "local_relevance_medium_second_relevance_orientation_view": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW_RECORDED"
    ),
    "local_relevance_medium_second_local_relevance_orientation_index_entry": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
    ),
    "local_relevance_medium_multiplicity_result": (
        "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT_RECORDED"
    ),
    "local_relevance_medium_relation_view": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW_RECORDED",
    "local_relevance_medium_comparison_view": COMPARISON_VIEW_RECORDED_OUTCOME,
}

EXPECTED_ARTIFACT_RESULT_VERSIONS = {
    key: RESULT_VERSION for key in KNOWN_ARTIFACT_CHAIN
}
EXPECTED_ARTIFACT_RESULT_VERSIONS["bounded_relevance_receipt_v2"] = "0.2.0"

EXPECTED_ARTIFACT_OBJECT_TYPES = {
    "bounded_relevance_reception": "BOUNDED_RELEVANCE_RECEPTION",
    "bounded_relevance_receipt_v2": "BOUNDED_RELEVANCE_RECEIPT",
    "relevance_orientation_view": "RELEVANCE_ORIENTATION_VIEW",
    "local_relevance_orientation_index_entry": "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
    "local_relevance_medium_successor_reception_request": (
        "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
    ),
    "local_relevance_medium_successor_candidate_admission": (
        "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
    ),
    "local_relevance_medium_second_bounded_relevance_reception": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
    ),
    "local_relevance_medium_second_bounded_relevance_receipt": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEIPT"
    ),
    "local_relevance_medium_second_relevance_orientation_view": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_RELEVANCE_ORIENTATION_VIEW"
    ),
    "local_relevance_medium_second_local_relevance_orientation_index_entry": (
        "LOCAL_RELEVANCE_MEDIUM_SECOND_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
    ),
    "local_relevance_medium_multiplicity_result": (
        "LOCAL_RELEVANCE_MEDIUM_MULTIPLICITY_RESULT"
    ),
    "local_relevance_medium_relation_view": "LOCAL_RELEVANCE_MEDIUM_RELATION_VIEW",
    "local_relevance_medium_comparison_view": COMPARISON_VIEW_TYPE,
}

REQUIRED_FALSE_NON_CLAIMS = (
    "new_signal_accepted",
    "new_relevance_object_created",
    "new_reception_created",
    "new_receipt_created",
    "new_orientation_view_created",
    "new_index_entry_created",
    "new_multiplicity_result_created",
    "new_relation_view_created",
    "new_comparison_view_created",
    "index_system_created",
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
    "artifact_existence_treated_as_read_only_state_authority",
    "latest_file_posture_treated_as_read_only_state_authority",
    "repo_local_availability_treated_as_read_only_state_authority",
    "hidden_repo_state_used_as_read_only_state_content",
    "hidden_repo_state_used_as_read_only_state_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_packet_recorded",
    "local_relevance_medium_read_only_state_reader_recorded",
    "basis_comparison_view_artifact_preserved",
    "known_artifact_chain_preserved",
    "validated_standing_artifacts_preserved",
    "standing_object_types_preserved",
    "standing_outcomes_preserved",
    "standing_result_versions_preserved",
    "standing_failed_check_counts_preserved",
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
    "chain_validated",
    "state_reconstruction_read_only",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_OBJECT_MISSING",
    "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW",
    "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
    "REQUIRED_ARTIFACT_PATH_MISSING",
    "REQUIRED_ARTIFACT_UNREADABLE",
    "REQUIRED_ARTIFACT_NOT_JSON_OBJECT",
    "REQUIRED_ARTIFACT_OUTCOME_NOT_RECORDED",
    "REQUIRED_ARTIFACT_FAILED_CHECKS_PRESENT",
    "REQUIRED_ARTIFACT_RESULT_VERSION_NOT_0_1_0",
    "REQUIRED_OBJECT_MISSING",
    "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    "LINEAGE_MISMATCH_ACROSS_SELECTED_ARTIFACTS",
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
    "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED",
    "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED",
    "STATE_PACKET_TYPE_MISSING",
    "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    "STATE_READER_TYPE_MISSING",
    "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    "STATE_READER_SCOPE_MISSING",
    "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    "STATE_RECONSTRUCTION_NOT_READ_ONLY",
    "NEW_SIGNAL_ACCEPTED",
    "NEW_RELEVANCE_OBJECT_CREATED",
    "NEW_RECEPTION_CREATED",
    "NEW_RECEIPT_CREATED",
    "NEW_ORIENTATION_VIEW_CREATED",
    "NEW_INDEX_ENTRY_CREATED",
    "NEW_MULTIPLICITY_RESULT_CREATED",
    "NEW_RELATION_VIEW_CREATED",
    "NEW_COMPARISON_VIEW_CREATED",
    "INDEX_SYSTEM_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_STATE_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_STATE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_STATE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_STATE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_STATE_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_UNREADABLE",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BODY_MUST_NOT_RETURN",
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_MUST_NOT_RETURN",
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

OFFICIAL_STRINGS = (
    STATE_PACKET_TYPE,
    STATE_READER_TYPE,
    STATE_READER_SCOPE,
    COMPARISON_VIEW_TYPE,
    COMPARISON_VIEW_SCOPE,
    COMPARISON_FRAME,
    COMPARISON_VIEW_RECORDED_OUTCOME,
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
    *KNOWN_ARTIFACT_CHAIN,
    *OUTCOME_FAMILY,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
    *EXPECTED_ARTIFACT_OUTCOMES.values(),
    *EXPECTED_ARTIFACT_OBJECT_TYPES.values(),
)

FALSE_POSTURE_TO_BLOCK_CODE = {
    "new_signal_accepted": "NEW_SIGNAL_ACCEPTED",
    "new_relevance_object_created": "NEW_RELEVANCE_OBJECT_CREATED",
    "new_reception_created": "NEW_RECEPTION_CREATED",
    "new_receipt_created": "NEW_RECEIPT_CREATED",
    "new_orientation_view_created": "NEW_ORIENTATION_VIEW_CREATED",
    "new_index_entry_created": "NEW_INDEX_ENTRY_CREATED",
    "new_multiplicity_result_created": "NEW_MULTIPLICITY_RESULT_CREATED",
    "new_relation_view_created": "NEW_RELATION_VIEW_CREATED",
    "new_comparison_view_created": "NEW_COMPARISON_VIEW_CREATED",
    "index_system_created": "INDEX_SYSTEM_CREATED",
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
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "artifact_existence_treated_as_read_only_state_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_READ_ONLY_STATE_AUTHORITY"
    ),
    "latest_file_posture_treated_as_read_only_state_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_READ_ONLY_STATE_AUTHORITY"
    ),
    "repo_local_availability_treated_as_read_only_state_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_READ_ONLY_STATE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_read_only_state_content": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_STATE_CONTENT"
    ),
    "hidden_repo_state_used_as_read_only_state_authority": (
        "HIDDEN_REPO_STATE_USED_AS_READ_ONLY_STATE_AUTHORITY"
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
    "selected_comparison_view_artifact_missing": (
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_PATH_MISSING"
    ),
    "selected_comparison_view_artifact_not_recorded": (
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_NOT_RECORDED"
    ),
    "selected_comparison_view_artifact_failed_checks_present": (
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT"
    ),
    "selected_comparison_view_artifact_version_not_0_1_0": (
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_VERSION_NOT_0_1_0"
    ),
    "local_relevance_medium_comparison_view_object_missing": (
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_OBJECT_MISSING"
    ),
    "comparison_view_type_not_local_relevance_medium_comparison_view": (
        "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW"
    ),
    "comparison_view_scope_not_two_local_orientation_objects_only": (
        "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY"
    ),
    "comparison_frame_not_bounded_non_ranking_local_comparison_only": (
        "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY"
    ),
    "required_artifact_path_missing": "REQUIRED_ARTIFACT_PATH_MISSING",
    "required_artifact_unreadable": "REQUIRED_ARTIFACT_UNREADABLE",
    "required_artifact_not_json_object": "REQUIRED_ARTIFACT_NOT_JSON_OBJECT",
    "required_artifact_outcome_not_recorded": "REQUIRED_ARTIFACT_OUTCOME_NOT_RECORDED",
    "required_artifact_failed_checks_present": "REQUIRED_ARTIFACT_FAILED_CHECKS_PRESENT",
    "required_artifact_result_version_not_0_1_0": (
        "REQUIRED_ARTIFACT_RESULT_VERSION_NOT_0_1_0"
    ),
    "required_object_missing": "REQUIRED_OBJECT_MISSING",
    "known_artifact_chain_not_canonical": "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    "lineage_mismatch_across_selected_artifacts": (
        "LINEAGE_MISMATCH_ACROSS_SELECTED_ARTIFACTS"
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
    "multiplicity_count_not_two": "MULTIPLICITY_COUNT_NOT_TWO",
    "relation_pair_count_not_one": "RELATION_PAIR_COUNT_NOT_ONE",
    "comparison_pair_count_not_one": "COMPARISON_PAIR_COUNT_NOT_ONE",
    "relation_readable_co_presence_not_preserved": (
        "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED"
    ),
    "comparison_readable_distinctions_not_recorded": (
        "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED"
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
    "state_reconstruction_not_read_only": "STATE_RECONSTRUCTION_NOT_READ_ONLY",
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


def _read_json_object(
    path_value: Any,
    missing_code: str,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    path_text = _string_or_empty(path_value)
    if not path_text:
        return None, missing_code
    try:
        with Path(path_text).open("r", encoding="utf-8") as handle:
            loaded = json.load(handle)
    except Exception:
        return None, unreadable_code
    if not isinstance(loaded, dict):
        return None, not_object_code
    return loaded, None


def _artifact_summary(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_summary") and isinstance(value, Mapping):
            return value
    return {}


def _artifact_metadata(artifact: Mapping[str, Any]) -> Mapping[str, Any]:
    for key, value in artifact.items():
        if isinstance(key, str) and key.endswith("_metadata") and isinstance(value, Mapping):
            return value
    return {}


def _artifact_result_version(artifact: Mapping[str, Any]) -> Any:
    summary = _artifact_summary(artifact)
    if "result_version" in summary:
        return summary.get("result_version")
    metadata = _artifact_metadata(artifact)
    if "result_version" in metadata:
        return metadata.get("result_version")
    for value in artifact.values():
        if isinstance(value, Mapping):
            for key, item in value.items():
                if isinstance(key, str) and key.endswith("_version"):
                    return item
    return artifact.get("result_version")


def _artifact_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    summary = _artifact_summary(artifact)
    value = _safe_int(summary.get("failed_check_count"))
    if value is not None:
        return value
    value = _safe_int(artifact.get("failed_check_count"))
    if value is not None:
        return value
    for key, checks in artifact.items():
        if isinstance(key, str) and key.endswith("_checks") and isinstance(checks, list):
            return sum(
                1
                for check in checks
                if isinstance(check, Mapping) and check.get("passed") is not True
            )
    return None


def _artifact_object_type(artifact: Mapping[str, Any]) -> str | None:
    for value in artifact.values():
        if isinstance(value, Mapping):
            for key, item in value.items():
                if isinstance(key, str) and key.endswith("_type") and isinstance(item, str):
                    return item
    return None


def _comparison_artifact_result_version(artifact: Mapping[str, Any]) -> Any:
    summary = artifact.get("local_relevance_medium_comparison_view_summary")
    if isinstance(summary, Mapping) and "result_version" in summary:
        return summary.get("result_version")
    metadata = artifact.get("local_relevance_medium_comparison_view_metadata")
    if isinstance(metadata, Mapping):
        for key in (
            "local_relevance_medium_comparison_view_version",
            "result_version",
            "comparison_view_version",
        ):
            if key in metadata:
                return metadata.get(key)
    comparison_view = artifact.get("local_relevance_medium_comparison_view")
    if isinstance(comparison_view, Mapping) and "comparison_view_version" in comparison_view:
        return comparison_view.get("comparison_view_version")
    return _artifact_result_version(artifact)


def _comparison_artifact_failed_check_count(artifact: Mapping[str, Any]) -> int | None:
    summary = artifact.get("local_relevance_medium_comparison_view_summary")
    if isinstance(summary, Mapping):
        value = _safe_int(summary.get("failed_check_count"))
        if value is not None:
            return value
    value = _safe_int(artifact.get("failed_check_count"))
    if value is not None:
        return value
    checks = artifact.get("local_relevance_medium_comparison_view_checks")
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _extract_comparison_basis(
    artifact: Mapping[str, Any],
    artifact_path: str,
) -> dict[str, Any]:
    comparison_view = artifact.get("local_relevance_medium_comparison_view")
    if not isinstance(comparison_view, Mapping):
        comparison_view = {}
    return {
        "comparison_artifact": artifact,
        "comparison_view": comparison_view,
        "basis_comparison_view_artifact": artifact_path,
        "basis_comparison_view_outcome": artifact.get("outcome"),
        "basis_comparison_view_result_version": _comparison_artifact_result_version(
            artifact
        ),
        "basis_comparison_view_failed_check_count": (
            _comparison_artifact_failed_check_count(artifact)
        ),
        "comparison_view_type": comparison_view.get("comparison_view_type"),
        "comparison_view_scope": comparison_view.get("comparison_view_scope"),
        "comparison_frame": comparison_view.get("comparison_frame"),
        "basis_local_relevance_medium_relation_view_artifact": comparison_view.get(
            "basis_local_relevance_medium_relation_view_artifact"
        ),
        "basis_local_relevance_medium_multiplicity_result_artifact": comparison_view.get(
            "basis_local_relevance_medium_multiplicity_result_artifact"
        ),
        "basis_first_local_relevance_orientation_index_entry_artifact": (
            comparison_view.get(
                "basis_first_local_relevance_orientation_index_entry_artifact"
            )
        ),
        "basis_second_local_relevance_orientation_index_entry_artifact": (
            comparison_view.get(
                "basis_second_local_relevance_orientation_index_entry_artifact"
            )
        ),
        "first_orientation_view_artifact": comparison_view.get(
            "first_orientation_view_artifact"
        ),
        "second_orientation_view_artifact": comparison_view.get(
            "second_orientation_view_artifact"
        ),
        "first_receipt_artifact": comparison_view.get("first_receipt_artifact"),
        "second_receipt_artifact": comparison_view.get("second_receipt_artifact"),
        "first_reception_artifact": comparison_view.get("first_reception_artifact"),
        "second_reception_artifact": comparison_view.get("second_reception_artifact"),
        "successor_candidate_admission_artifact": comparison_view.get(
            "successor_candidate_admission_artifact"
        ),
        "successor_reception_request_artifact": comparison_view.get(
            "successor_reception_request_artifact"
        ),
        "first_received_signal_id": comparison_view.get("first_received_signal_id"),
        "second_received_signal_id": comparison_view.get("second_received_signal_id"),
        "first_relevance_basis_id": comparison_view.get("first_relevance_basis_id"),
        "second_relevance_basis_id": comparison_view.get("second_relevance_basis_id"),
        "first_relevance_scope_id": comparison_view.get("first_relevance_scope_id"),
        "second_relevance_scope_id": comparison_view.get("second_relevance_scope_id"),
        "first_carrier_context_id": comparison_view.get("first_carrier_context_id"),
        "second_carrier_context_id": comparison_view.get("second_carrier_context_id"),
        "first_reception_envelope_id": comparison_view.get(
            "first_reception_envelope_id"
        ),
        "second_reception_envelope_id": comparison_view.get(
            "second_reception_envelope_id"
        ),
        "multiplicity_count": comparison_view.get("multiplicity_count"),
        "relation_pair_count": comparison_view.get("relation_pair_count"),
        "comparison_pair_count": comparison_view.get("comparison_pair_count"),
        "first_and_second_signals_distinct": comparison_view.get(
            "first_and_second_signals_distinct"
        ),
        "two_local_orientation_objects_preserved": comparison_view.get(
            "two_local_orientation_objects_preserved"
        ),
        "relation_readable_co_presence_preserved": comparison_view.get(
            "relation_readable_co_presence_preserved"
        ),
        "comparison_readable_distinctions_recorded": comparison_view.get(
            "comparison_readable_distinctions_recorded"
        ),
        "comparison_view_recorded": comparison_view.get("comparison_view_recorded"),
    }


def _chain_artifacts_from_basis(basis: Mapping[str, Any]) -> dict[str, str]:
    artifacts = dict(DEFAULT_VALIDATED_STANDING_ARTIFACTS)
    mapping = {
        "bounded_relevance_reception": "first_reception_artifact",
        "bounded_relevance_receipt_v2": "first_receipt_artifact",
        "relevance_orientation_view": "first_orientation_view_artifact",
        "local_relevance_orientation_index_entry": (
            "basis_first_local_relevance_orientation_index_entry_artifact"
        ),
        "local_relevance_medium_successor_reception_request": (
            "successor_reception_request_artifact"
        ),
        "local_relevance_medium_successor_candidate_admission": (
            "successor_candidate_admission_artifact"
        ),
        "local_relevance_medium_second_bounded_relevance_reception": (
            "second_reception_artifact"
        ),
        "local_relevance_medium_second_bounded_relevance_receipt": (
            "second_receipt_artifact"
        ),
        "local_relevance_medium_second_relevance_orientation_view": (
            "second_orientation_view_artifact"
        ),
        "local_relevance_medium_second_local_relevance_orientation_index_entry": (
            "basis_second_local_relevance_orientation_index_entry_artifact"
        ),
        "local_relevance_medium_multiplicity_result": (
            "basis_local_relevance_medium_multiplicity_result_artifact"
        ),
        "local_relevance_medium_relation_view": (
            "basis_local_relevance_medium_relation_view_artifact"
        ),
        "local_relevance_medium_comparison_view": "basis_comparison_view_artifact",
    }
    for chain_key, basis_key in mapping.items():
        value = basis.get(basis_key)
        if _present(value):
            artifacts[chain_key] = str(value)
    return artifacts


def _build_state_packet(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
    chain_facts: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    standing_object_types = {
        key: fact.get("object_type")
        for key, fact in chain_facts.items()
        if _present(fact.get("object_type"))
    }
    standing_outcomes = {
        key: fact.get("outcome")
        for key, fact in chain_facts.items()
        if _present(fact.get("outcome"))
    }
    standing_result_versions = {
        key: fact.get("result_version")
        for key, fact in chain_facts.items()
        if _present(fact.get("result_version"))
    }
    standing_failed_check_counts = {
        key: fact.get("failed_check_count")
        for key, fact in chain_facts.items()
        if fact.get("failed_check_count") is not None
    }
    comparison_key = "local_relevance_medium_comparison_view"
    standing_object_types[comparison_key] = COMPARISON_VIEW_TYPE
    standing_outcomes[comparison_key] = COMPARISON_VIEW_RECORDED_OUTCOME
    standing_result_versions[comparison_key] = RESULT_VERSION
    standing_failed_check_counts[comparison_key] = 0

    return {
        "state_packet_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_state_packet_id")
        )
        or DEFAULT_STATE_PACKET_ID,
        "state_packet_type": STATE_PACKET_TYPE,
        "state_packet_version": RESULT_VERSION,
        "state_reader_type": STATE_READER_TYPE,
        "state_reader_version": RESULT_VERSION,
        "state_reader_scope": STATE_READER_SCOPE,
        "basis_comparison_view_artifact": basis.get("basis_comparison_view_artifact"),
        "basis_comparison_view_outcome": basis.get("basis_comparison_view_outcome"),
        "basis_comparison_view_result_version": basis.get(
            "basis_comparison_view_result_version"
        ),
        "basis_comparison_view_failed_check_count": basis.get(
            "basis_comparison_view_failed_check_count"
        ),
        "known_artifact_chain": copy.deepcopy(KNOWN_ARTIFACT_CHAIN),
        "validated_standing_artifacts": _chain_artifacts_from_basis(basis),
        "standing_object_types": standing_object_types,
        "standing_outcomes": standing_outcomes,
        "standing_result_versions": standing_result_versions,
        "standing_failed_check_counts": standing_failed_check_counts,
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
        "comparison_readability_stands": True,
        "relation_readability_stands": True,
        "multiplicity_result_stands": True,
        "two_local_orientation_objects_stand": True,
        "chain_validated": True,
        "state_reconstruction_read_only": True,
        "new_signal_accepted": False,
        "new_relevance_object_created": False,
        "new_reception_created": False,
        "new_receipt_created": False,
        "new_orientation_view_created": False,
        "new_index_entry_created": False,
        "new_multiplicity_result_created": False,
        "new_relation_view_created": False,
        "new_comparison_view_created": False,
        "index_system_created": False,
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


def _empty_state_packet(declared: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "state_packet_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_state_packet_id")
        )
        or DEFAULT_STATE_PACKET_ID,
        "state_packet_type": _sanitize(declared.get("state_packet_type")),
        "state_packet_version": RESULT_VERSION,
        "state_reader_type": _sanitize(declared.get("state_reader_type")),
        "state_reader_version": RESULT_VERSION,
        "state_reader_scope": _sanitize(declared.get("state_reader_scope")),
        "known_artifact_chain": _sanitize(declared.get("known_artifact_chain", [])),
        "chain_validated": False,
        "state_reconstruction_read_only": False,
    }


def _recorded_statement() -> dict[str, bool]:
    return {key: True for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _blocked_statement() -> dict[str, bool]:
    return {key: False for key in ALLOWED_TRUE_RECORDED_FIELDS}


def _non_meaning() -> dict[str, bool]:
    non_claims = _canonical_non_claims()
    return {
        "read_only_state_packet_is_not_index_system": True,
        "read_only_state_packet_is_not_registry_search_or_ranking": True,
        "read_only_state_packet_accepts_no_new_signal": True,
        "read_only_state_packet_creates_no_new_relevance_object": True,
        "read_only_state_packet_creates_no_runtime_permission_api_or_distributed_behavior": True,
        **non_claims,
    }


def _what_remains_open() -> list[str]:
    return [
        "local relevance medium read-only state reader resolver successor work, if separately selected",
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


def _selected_basis_summary(
    basis: Mapping[str, Any],
    chain_facts: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    return {
        "basis_comparison_view_artifact": basis.get("basis_comparison_view_artifact"),
        "basis_comparison_view_outcome": basis.get("basis_comparison_view_outcome"),
        "basis_comparison_view_result_version": basis.get(
            "basis_comparison_view_result_version"
        ),
        "basis_comparison_view_failed_check_count": basis.get(
            "basis_comparison_view_failed_check_count"
        ),
        "comparison_view_type": basis.get("comparison_view_type"),
        "comparison_view_scope": basis.get("comparison_view_scope"),
        "comparison_frame": basis.get("comparison_frame"),
        "known_artifact_chain": copy.deepcopy(KNOWN_ARTIFACT_CHAIN),
        "validated_standing_artifacts": _chain_artifacts_from_basis(basis),
        "standing_object_types": {
            key: fact.get("object_type") for key, fact in chain_facts.items()
        },
        "standing_outcomes": {
            key: fact.get("outcome") for key, fact in chain_facts.items()
        },
        "standing_result_versions": {
            key: fact.get("result_version") for key, fact in chain_facts.items()
        },
        "standing_failed_check_counts": {
            key: fact.get("failed_check_count") for key, fact in chain_facts.items()
        },
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
        _append_check(
            checks,
            f"declared non-claim {key} is false",
            value is False,
            False,
            value,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )


def _validate_request(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    question = declared.get("local_relevance_medium_read_only_state_reader_question")
    intent = declared.get("local_relevance_medium_read_only_state_reader_intent")
    _append_check(
        checks,
        "read-only state reader question declared",
        _present(question),
        "declared read-only state reader question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_QUESTION_UNDECLARED",
    )
    _append_check(
        checks,
        "read-only state reader intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_INTENT_UNSUPPORTED",
    )
    _append_check(
        checks,
        "read-only state reader block intent not requested",
        intent != BLOCK_INTENT,
        f"not {BLOCK_INTENT}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_BLOCK_REQUESTED",
    )
    artifact = declared.get("selected_local_relevance_medium_comparison_view_artifact")
    _append_check(
        checks,
        "selected comparison view artifact path declared",
        _present(_string_or_empty(artifact)),
        "declared path",
        artifact,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_PATH_MISSING",
    )

    packet_type = declared.get("state_packet_type")
    _append_check(
        checks,
        "state packet type declared",
        _present(_string_or_empty(packet_type)),
        STATE_PACKET_TYPE,
        packet_type,
        "STATE_PACKET_TYPE_MISSING",
    )
    _append_check(
        checks,
        "state packet type exact",
        packet_type == STATE_PACKET_TYPE,
        STATE_PACKET_TYPE,
        packet_type,
        "STATE_PACKET_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET",
    )

    reader_type = declared.get("state_reader_type")
    _append_check(
        checks,
        "state reader type declared",
        _present(_string_or_empty(reader_type)),
        STATE_READER_TYPE,
        reader_type,
        "STATE_READER_TYPE_MISSING",
    )
    _append_check(
        checks,
        "state reader type exact",
        reader_type == STATE_READER_TYPE,
        STATE_READER_TYPE,
        reader_type,
        "STATE_READER_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER",
    )

    reader_scope = declared.get("state_reader_scope")
    _append_check(
        checks,
        "state reader scope declared",
        _present(_string_or_empty(reader_scope)),
        STATE_READER_SCOPE,
        reader_scope,
        "STATE_READER_SCOPE_MISSING",
    )
    _append_check(
        checks,
        "state reader scope read existing local relevance medium state only",
        reader_scope == STATE_READER_SCOPE,
        STATE_READER_SCOPE,
        reader_scope,
        "STATE_READER_SCOPE_NOT_READ_EXISTING_LOCAL_RELEVANCE_MEDIUM_STATE_ONLY",
    )

    _append_check(
        checks,
        "known artifact chain canonical",
        declared.get("known_artifact_chain") == KNOWN_ARTIFACT_CHAIN,
        KNOWN_ARTIFACT_CHAIN,
        declared.get("known_artifact_chain"),
        "KNOWN_ARTIFACT_CHAIN_NOT_CANONICAL",
    )
    _resolve_declared_non_claims(declared, checks)


def _validate_comparison_artifact(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, Any]:
    artifact_path = _string_or_empty(
        declared.get("selected_local_relevance_medium_comparison_view_artifact")
    )
    artifact, read_error = _read_json_object(
        artifact_path,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_PATH_MISSING",
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_UNREADABLE",
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_NOT_JSON_OBJECT",
    )
    if read_error:
        _append_check(
            checks,
            "selected comparison view artifact readable JSON object",
            False,
            "readable JSON object",
            read_error,
            read_error,
        )
        return _extract_comparison_basis({}, artifact_path)

    _append_check(
        checks,
        "selected comparison view artifact readable JSON object",
        True,
        "readable JSON object",
        "readable JSON object",
    )
    basis = _extract_comparison_basis(artifact, artifact_path)
    _append_check(
        checks,
        "selected comparison view artifact outcome recorded",
        basis.get("basis_comparison_view_outcome") == COMPARISON_VIEW_RECORDED_OUTCOME,
        COMPARISON_VIEW_RECORDED_OUTCOME,
        basis.get("basis_comparison_view_outcome"),
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_NOT_RECORDED",
    )
    _append_check(
        checks,
        "selected comparison view artifact result version 0.1.0",
        basis.get("basis_comparison_view_result_version") == RESULT_VERSION,
        RESULT_VERSION,
        basis.get("basis_comparison_view_result_version"),
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _append_check(
        checks,
        "selected comparison view artifact failed check count zero",
        basis.get("basis_comparison_view_failed_check_count") == 0,
        0,
        basis.get("basis_comparison_view_failed_check_count"),
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    comparison_view = basis.get("comparison_view")
    _append_check(
        checks,
        "local relevance medium comparison view object present",
        isinstance(comparison_view, Mapping) and bool(comparison_view),
        "local_relevance_medium_comparison_view object",
        bool(comparison_view)
        if isinstance(comparison_view, Mapping)
        else type(comparison_view).__name__,
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW_OBJECT_MISSING",
    )
    return basis


def _validate_comparison_basis(
    basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    _append_check(
        checks,
        "comparison view type exact",
        basis.get("comparison_view_type") == COMPARISON_VIEW_TYPE,
        COMPARISON_VIEW_TYPE,
        basis.get("comparison_view_type"),
        "COMPARISON_VIEW_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW",
    )
    _append_check(
        checks,
        "comparison view scope two local orientation objects only",
        basis.get("comparison_view_scope") == COMPARISON_VIEW_SCOPE,
        COMPARISON_VIEW_SCOPE,
        basis.get("comparison_view_scope"),
        "COMPARISON_VIEW_SCOPE_NOT_TWO_LOCAL_ORIENTATION_OBJECTS_ONLY",
    )
    _append_check(
        checks,
        "comparison frame bounded non-ranking local comparison only",
        basis.get("comparison_frame") == COMPARISON_FRAME,
        COMPARISON_FRAME,
        basis.get("comparison_frame"),
        "COMPARISON_FRAME_NOT_BOUNDED_NON_RANKING_LOCAL_COMPARISON_ONLY",
    )

    required_paths = _chain_artifacts_from_basis(basis)
    _append_check(
        checks,
        "preserved relation/multiplicity/locator/orientation/receipt/reception artifact paths present",
        all(_present(required_paths.get(key)) for key in KNOWN_ARTIFACT_CHAIN),
        "all known artifact chain paths present",
        required_paths,
        "REQUIRED_ARTIFACT_PATH_MISSING",
    )

    expected_identifiers = (
        ("first received signal id preserved", "first_received_signal_id", FIRST_RECEIVED_SIGNAL_ID, "FIRST_RECEIVED_SIGNAL_ID_MISSING"),
        ("second received signal id preserved", "second_received_signal_id", SECOND_RECEIVED_SIGNAL_ID, "SECOND_RECEIVED_SIGNAL_ID_MISSING"),
        ("first relevance basis id preserved", "first_relevance_basis_id", FIRST_RELEVANCE_BASIS_ID, "FIRST_RELEVANCE_BASIS_ID_MISSING"),
        ("second relevance basis id preserved", "second_relevance_basis_id", SECOND_RELEVANCE_BASIS_ID, "SECOND_RELEVANCE_BASIS_ID_MISSING"),
        ("first relevance scope id preserved", "first_relevance_scope_id", FIRST_RELEVANCE_SCOPE_ID, "FIRST_RELEVANCE_SCOPE_ID_MISSING"),
        ("second relevance scope id preserved", "second_relevance_scope_id", SECOND_RELEVANCE_SCOPE_ID, "SECOND_RELEVANCE_SCOPE_ID_MISSING"),
        ("first carrier context id preserved", "first_carrier_context_id", FIRST_CARRIER_CONTEXT_ID, "FIRST_CARRIER_CONTEXT_ID_MISSING"),
        ("second carrier context id preserved", "second_carrier_context_id", SECOND_CARRIER_CONTEXT_ID, "SECOND_CARRIER_CONTEXT_ID_MISSING"),
        ("first reception envelope id preserved", "first_reception_envelope_id", FIRST_RECEPTION_ENVELOPE_ID, "FIRST_RECEPTION_ENVELOPE_ID_MISSING"),
        ("second reception envelope id preserved", "second_reception_envelope_id", SECOND_RECEPTION_ENVELOPE_ID, "SECOND_RECEPTION_ENVELOPE_ID_MISSING"),
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
    _append_check(checks, "multiplicity count exactly two", basis.get("multiplicity_count") == 2, 2, basis.get("multiplicity_count"), "MULTIPLICITY_COUNT_NOT_TWO")
    _append_check(checks, "relation pair count exactly one", basis.get("relation_pair_count") == 1, 1, basis.get("relation_pair_count"), "RELATION_PAIR_COUNT_NOT_ONE")
    _append_check(checks, "comparison pair count exactly one", basis.get("comparison_pair_count") == 1, 1, basis.get("comparison_pair_count"), "COMPARISON_PAIR_COUNT_NOT_ONE")
    _append_check(checks, "relation-readable co-presence preserved", basis.get("relation_readable_co_presence_preserved") is True, True, basis.get("relation_readable_co_presence_preserved"), "RELATION_READABLE_CO_PRESENCE_NOT_PRESERVED")
    _append_check(checks, "comparison-readable distinctions recorded", basis.get("comparison_readable_distinctions_recorded") is True, True, basis.get("comparison_readable_distinctions_recorded"), "COMPARISON_READABLE_DISTINCTIONS_NOT_RECORDED")


def _read_available_chain_artifacts(
    chain_paths: Mapping[str, str],
    checks: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    facts: dict[str, dict[str, Any]] = {}
    for chain_key in KNOWN_ARTIFACT_CHAIN:
        path_text = chain_paths.get(chain_key, "")
        expected_outcome = EXPECTED_ARTIFACT_OUTCOMES.get(chain_key)
        expected_version = EXPECTED_ARTIFACT_RESULT_VERSIONS.get(chain_key)
        expected_type = EXPECTED_ARTIFACT_OBJECT_TYPES.get(chain_key)
        fact: dict[str, Any] = {
            "path": path_text,
            "outcome": expected_outcome,
            "result_version": expected_version,
            "failed_check_count": 0,
            "object_type": expected_type,
            "readable_json_object": False,
        }

        if not _present(path_text):
            _append_check(
                checks,
                f"required artifact path present for {chain_key}",
                False,
                "present path",
                path_text,
                "REQUIRED_ARTIFACT_PATH_MISSING",
            )
            facts[chain_key] = fact
            continue

        path = Path(path_text)
        if not path.exists():
            _append_check(
                checks,
                f"required selected artifact path retained for {chain_key}",
                True,
                "path retained as comparison-view lineage basis",
                path_text,
            )
            facts[chain_key] = fact
            continue

        artifact, read_error = _read_json_object(
            path_text,
            "REQUIRED_ARTIFACT_PATH_MISSING",
            "REQUIRED_ARTIFACT_UNREADABLE",
            "REQUIRED_ARTIFACT_NOT_JSON_OBJECT",
        )
        if read_error:
            _append_check(
                checks,
                f"required selected artifact readable JSON object for {chain_key}",
                False,
                "readable JSON object",
                read_error,
                read_error,
            )
            facts[chain_key] = fact
            continue

        outcome = artifact.get("outcome")
        version = _artifact_result_version(artifact)
        failed_count = _artifact_failed_check_count(artifact)
        object_type = _artifact_object_type(artifact)
        fact = {
            "path": path_text,
            "outcome": outcome,
            "result_version": version,
            "failed_check_count": failed_count,
            "object_type": object_type or expected_type,
            "readable_json_object": True,
        }
        _append_check(
            checks,
            f"required selected artifact readable JSON object for {chain_key}",
            True,
            "readable JSON object",
            "readable JSON object",
        )
        _append_check(
            checks,
            f"required selected artifact recorded for {chain_key}",
            outcome == expected_outcome,
            expected_outcome,
            outcome,
            "REQUIRED_ARTIFACT_OUTCOME_NOT_RECORDED",
        )
        _append_check(
            checks,
            f"required selected artifact result version expected for {chain_key}",
            version == expected_version,
            expected_version,
            version,
            "REQUIRED_ARTIFACT_RESULT_VERSION_NOT_0_1_0",
        )
        _append_check(
            checks,
            f"required selected artifact failed check count zero for {chain_key}",
            failed_count == 0,
            0,
            failed_count,
            "REQUIRED_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
        _append_check(
            checks,
            f"required selected artifact object present for {chain_key}",
            _present(object_type) or _present(expected_type),
            expected_type or "artifact object type",
            object_type,
            "REQUIRED_OBJECT_MISSING",
        )
        facts[chain_key] = fact
    return facts


def _validate_chain_lineage(
    declared: Mapping[str, Any],
    basis: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    chain_paths = _chain_artifacts_from_basis(basis)
    declared_paths = declared.get("validated_standing_artifacts")
    if isinstance(declared_paths, Mapping):
        declared_projection = {key: declared_paths.get(key) for key in KNOWN_ARTIFACT_CHAIN}
        expected_projection = {key: chain_paths.get(key) for key in KNOWN_ARTIFACT_CHAIN}
        matches = all(
            not _present(declared_projection[key])
            or declared_projection[key] == expected_projection[key]
            for key in KNOWN_ARTIFACT_CHAIN
        )
        _append_check(
            checks,
            "chain lineage matches across preserved paths and identifiers",
            matches,
            expected_projection,
            declared_projection,
            "LINEAGE_MISMATCH_ACROSS_SELECTED_ARTIFACTS",
        )
    else:
        _append_check(
            checks,
            "validated standing artifacts mapping declared",
            False,
            "mapping of known artifact chain paths",
            type(declared_paths).__name__,
            "REQUIRED_ARTIFACT_PATH_MISSING",
        )
    return _read_available_chain_artifacts(chain_paths, checks)


def _validate_state_packet_posture(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    expected_true_defaults = {
        "comparison_readability_stands": True,
        "relation_readability_stands": True,
        "multiplicity_result_stands": True,
        "two_local_orientation_objects_stand": True,
        "chain_validated": True,
        "state_reconstruction_read_only": True,
    }
    true_check_codes = {
        "state_reconstruction_read_only": "STATE_RECONSTRUCTION_NOT_READ_ONLY",
    }
    for key, expected in expected_true_defaults.items():
        actual = declared.get(key, expected)
        _append_check(
            checks,
            f"{key} posture preserved",
            actual is expected,
            expected,
            actual,
            true_check_codes.get(key, "LINEAGE_MISMATCH_ACROSS_SELECTED_ARTIFACTS"),
        )


def _validate_false_postures(
    declared: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> None:
    for key, code in REQUEST_SHORTCUT_FAILURES.items():
        value = declared.get(key, False)
        _append_check(checks, f"shortcut {key} not asserted", value is False, False, value, code)

    for key, code in FALSE_POSTURE_TO_BLOCK_CODE.items():
        value = declared.get(key, False)
        _append_check(checks, f"{key} not created", value is False, False, value, code)

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
    value = declared.get("requested_local_relevance_medium_read_only_state_reader_outcome")
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
    code = (
        _first_failed_code(checks)
        or "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_MALFORMED"
    )
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": "local relevance medium read-only state reader was blocked by bounded validation",
    }


def _determine_outcome(
    declared: Mapping[str, Any],
    checks: list[Mapping[str, Any]],
) -> str:
    _, failed_count = _check_counts(checks)
    if failed_count:
        return OUTCOME_BLOCKED
    intent = declared.get("local_relevance_medium_read_only_state_reader_intent")
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
    chain_facts: Mapping[str, Mapping[str, Any]],
    state_packet: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
) -> dict[str, Any]:
    passed_count, failed_count = _check_counts(checks)
    statement = _recorded_statement() if outcome == OUTCOME_RECORDED else _blocked_statement()
    metadata = {
        "local_relevance_medium_read_only_state_reader_id": _string_or_empty(
            declared.get("local_relevance_medium_read_only_state_reader_id")
        )
        or DEFAULT_STATE_READER_ID,
        "local_relevance_medium_read_only_state_reader_type": STATE_READER_TYPE,
        "local_relevance_medium_read_only_state_reader_version": RESULT_VERSION,
        "generated_at": _utc_timestamp(),
        "resolver_module": RESOLVER_MODULE,
        "result_version": RESULT_VERSION,
        "passed_check_count": passed_count,
        "failed_check_count": failed_count,
    }
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_reader_metadata": metadata,
        "declared_local_relevance_medium_read_only_state_reader_question": {
            "question": _sanitize(
                declared.get("local_relevance_medium_read_only_state_reader_question")
            ),
            "intent": _sanitize(
                declared.get("local_relevance_medium_read_only_state_reader_intent")
            ),
        },
        "selected_local_relevance_medium_comparison_view_artifact_basis": _sanitize(
            _selected_basis_summary(basis, chain_facts)
        ),
        "local_relevance_medium_read_only_state_packet": _sanitize(dict(state_packet)),
        "local_relevance_medium_read_only_state_reader_checks": _sanitize(checks),
        "local_relevance_medium_read_only_state_reader_statement": statement,
        "local_relevance_medium_read_only_state_reader_non_meaning": _non_meaning(),
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
    result["local_relevance_medium_read_only_state_reader_summary"] = (
        build_local_relevance_medium_read_only_state_reader_v0_min_summary(result)
    )
    return _sanitize(result)


def resolve_local_relevance_medium_read_only_state_reader_v0_min(
    declared_local_relevance_medium_read_only_state_reader: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one bounded local relevance medium read-only state reader result."""

    checks: list[dict[str, Any]] = []
    if declared_local_relevance_medium_read_only_state_reader is None:
        declared: Mapping[str, Any] = {}
        _append_check(
            checks,
            "declared local relevance medium read-only state reader request present",
            False,
            "request mapping",
            None,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_MALFORMED",
        )
        basis = _extract_comparison_basis({}, "")
        chain_facts: dict[str, dict[str, Any]] = {}
        return _assemble_result(
            declared,
            basis,
            chain_facts,
            _empty_state_packet(declared),
            checks,
            OUTCOME_BLOCKED,
        )

    if not isinstance(declared_local_relevance_medium_read_only_state_reader, Mapping):
        declared = {}
        _append_check(
            checks,
            "declared local relevance medium read-only state reader request mapping",
            False,
            "mapping",
            type(declared_local_relevance_medium_read_only_state_reader).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_MALFORMED",
        )
        basis = _extract_comparison_basis({}, "")
        chain_facts = {}
        return _assemble_result(
            declared,
            basis,
            chain_facts,
            _empty_state_packet(declared),
            checks,
            OUTCOME_BLOCKED,
        )

    declared_copy = copy.deepcopy(dict(declared_local_relevance_medium_read_only_state_reader))
    _validate_request(declared_copy, checks)
    basis = _validate_comparison_artifact(declared_copy, checks)
    _validate_comparison_basis(basis, checks)
    chain_facts = _validate_chain_lineage(declared_copy, basis, checks)
    _validate_state_packet_posture(declared_copy, checks)
    _validate_false_postures(declared_copy, checks)

    provisional_outcome = _determine_outcome(declared_copy, checks)
    if provisional_outcome == OUTCOME_RECORDED:
        state_packet = _build_state_packet(declared_copy, basis, chain_facts)
    else:
        state_packet = _empty_state_packet(declared_copy)
    return _assemble_result(
        declared_copy,
        basis,
        chain_facts,
        state_packet,
        checks,
        provisional_outcome,
    )


def resolve_local_relevance_medium_read_only_state_reader_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_reader_path: Path | str,
) -> dict:
    """Read a declared read-only state reader request JSON object and resolve it."""

    try:
        with Path(declared_local_relevance_medium_read_only_state_reader_path).open(
            "r", encoding="utf-8"
        ) as handle:
            request = json.load(handle)
    except Exception:
        checks = [
            _make_check(
                "declared local relevance medium read-only state reader request readable",
                False,
                "readable JSON object",
                "unreadable",
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_UNREADABLE",
            )
        ]
        declared: dict[str, Any] = {}
        basis = _extract_comparison_basis({}, "")
        return _assemble_result(
            declared,
            basis,
            {},
            _empty_state_packet(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    if not isinstance(request, Mapping):
        checks = [
            _make_check(
                "declared local relevance medium read-only state reader request object",
                False,
                "JSON object",
                type(request).__name__,
                "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER_REQUEST_MALFORMED",
            )
        ]
        declared = {}
        basis = _extract_comparison_basis({}, "")
        return _assemble_result(
            declared,
            basis,
            {},
            _empty_state_packet(declared),
            checks,
            OUTCOME_BLOCKED,
        )
    return resolve_local_relevance_medium_read_only_state_reader_v0_min(request)


def build_local_relevance_medium_read_only_state_reader_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary from a read-only state reader resolver result."""

    metadata = result.get("local_relevance_medium_read_only_state_reader_metadata", {})
    if not isinstance(metadata, Mapping):
        metadata = {}
    statement = result.get("local_relevance_medium_read_only_state_reader_statement", {})
    if not isinstance(statement, Mapping):
        statement = {}
    question = result.get("declared_local_relevance_medium_read_only_state_reader_question", {})
    if not isinstance(question, Mapping):
        question = {}
    state_packet = result.get("local_relevance_medium_read_only_state_packet", {})
    if not isinstance(state_packet, Mapping):
        state_packet = {}
    block = result.get("block")
    if not isinstance(block, Mapping):
        block = {"blocked": False, "code": None, "block_code": None, "reason": None}
    checks = result.get("local_relevance_medium_read_only_state_reader_checks", [])
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
        "state_packet_id": state_packet.get("state_packet_id"),
        "question": question.get("question"),
        "intent": question.get("intent"),
        "passed_check_count": passed_count or metadata.get("passed_check_count", 0),
        "failed_check_count": failed_count or metadata.get("failed_check_count", 0),
        "result_version": metadata.get("result_version", RESULT_VERSION),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "read_only_state_packet_recorded": bool(
            statement.get("local_relevance_medium_read_only_state_packet_recorded")
        ),
        "read_only_state_reader_recorded": bool(
            statement.get("local_relevance_medium_read_only_state_reader_recorded")
        ),
        "basis_comparison_view_artifact_preserved": bool(
            statement.get("basis_comparison_view_artifact_preserved")
        ),
        "known_artifact_chain_preserved": bool(
            statement.get("known_artifact_chain_preserved")
        ),
        "validated_standing_artifacts_preserved": bool(
            statement.get("validated_standing_artifacts_preserved")
        ),
        "standing_object_types_preserved": bool(
            statement.get("standing_object_types_preserved")
        ),
        "standing_outcomes_preserved": bool(
            statement.get("standing_outcomes_preserved")
        ),
        "standing_result_versions_preserved": bool(
            statement.get("standing_result_versions_preserved")
        ),
        "standing_failed_check_counts_preserved": bool(
            statement.get("standing_failed_check_counts_preserved")
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
            statement.get("multipity_result_stands")
            or statement.get("multiplicity_result_stands")
        ),
        "two_local_orientation_objects_stand": bool(
            statement.get("two_local_orientation_objects_stand")
        ),
        "chain_validated": bool(statement.get("chain_validated")),
        "state_reconstruction_read_only": bool(
            statement.get("state_reconstruction_read_only")
        ),
        "state_packet_object_summary": {
            "state_packet_type": state_packet.get("state_packet_type"),
            "state_reader_type": state_packet.get("state_reader_type"),
            "state_reader_scope": state_packet.get("state_reader_scope"),
            "known_artifact_chain_count": len(
                state_packet.get("known_artifact_chain", [])
            )
            if isinstance(state_packet.get("known_artifact_chain"), list)
            else 0,
        },
        "no_new_medium_content_created": all(
            non_claims.get(key) is False
            for key in (
                "new_signal_accepted",
                "new_relevance_object_created",
                "new_reception_created",
                "new_receipt_created",
                "new_orientation_view_created",
                "new_index_entry_created",
                "new_multiplicity_result_created",
                "new_relation_view_created",
                "new_comparison_view_created",
            )
        ),
        "index_system_registry_search_ranking_not_created": all(
            non_claims.get(key) is False
            for key in (
                "index_system_created",
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
        "runtime_api_distributed_follow_on_not_created": all(
            non_claims.get(key) is False
            for key in (
                "runtime_permission_created",
                "public_api_created",
                "participant_facing_interface_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            )
        ),
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "new_signal_accepted",
                "new_relevance_object_created",
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "runtime_permission_created",
                "public_api_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": (
            non_claims.get("predecessor_failure_repaired") is False
            and non_claims.get("predecessor_failure_hidden") is False
            and non_claims.get("predecessor_failure_claimed_passed") is False
        ),
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


def write_local_relevance_medium_read_only_state_reader_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a read-only state reader resolver result without overwriting."""

    result_copy = _sanitize(copy.deepcopy(dict(result)))
    if output_path is None:
        state_packet = result_copy.get("local_relevance_medium_read_only_state_packet", {})
        if not isinstance(state_packet, Mapping):
            state_packet = {}
        state_packet_id = _string_or_empty(state_packet.get("state_packet_id")) or DEFAULT_STATE_PACKET_ID
        output_path = (
            OUTPUT_ROOT
            / f"{state_packet_id}__local_relevance_medium_read_only_state_reader_v0_min_result.json"
        )
    path = _next_available_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(result_copy, handle, indent=2, sort_keys=True)
        handle.write("\n")
    return path


def build_declared_local_relevance_medium_read_only_state_reader_v0_min_request(
    *,
    local_relevance_medium_read_only_state_reader_id: str = DEFAULT_STATE_READER_ID,
    local_relevance_medium_read_only_state_packet_id: str = DEFAULT_STATE_PACKET_ID,
    local_relevance_medium_read_only_state_reader_question: str | None = None,
    local_relevance_medium_read_only_state_reader_intent: str = RECORD_INTENT,
    selected_local_relevance_medium_comparison_view_artifact: Path | str = DEFAULT_COMPARISON_VIEW_ARTIFACT,
    state_packet_type: str = STATE_PACKET_TYPE,
    state_reader_type: str = STATE_READER_TYPE,
    state_reader_scope: str = STATE_READER_SCOPE,
    known_artifact_chain: list[str] | None = None,
    validated_standing_artifacts: Mapping[str, str] | None = None,
    declared_non_claims: Mapping[str, bool] | None = None,
    **extra_fields: Any,
) -> dict[str, Any]:
    """Build a declared request for one read-only state reader resolution."""

    question = local_relevance_medium_read_only_state_reader_question or (
        "Given the known local relevance medium artifact roots through one clean "
        "LOCAL_RELEVANCE_MEDIUM_COMPARISON_VIEW, may one "
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_READER record one "
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET that reads existing "
        "artifacts, validates the standing local medium lineage, and emits one "
        "read-only local medium state packet showing what currently stands, "
        "without accepting new signals, creating new relevance objects, creating "
        "index system, registry, search, ranking, scoring, priority, validity "
        "judgment, truth judgment, authority, currentness, action, "
        "synchronization, participation authorization, participant role, runtime "
        "permission, public API, participant-facing interface, distributed "
        "network behavior, operation permission, repeated reception permission, "
        "arbitrary reception, feed, source transfer, source receipt, or follow-on "
        "work?"
    )
    artifacts = copy.deepcopy(dict(validated_standing_artifacts or DEFAULT_VALIDATED_STANDING_ARTIFACTS))
    artifacts["local_relevance_medium_comparison_view"] = _string_or_empty(
        selected_local_relevance_medium_comparison_view_artifact
    )
    request = {
        "local_relevance_medium_read_only_state_reader_id": (
            local_relevance_medium_read_only_state_reader_id
        ),
        "local_relevance_medium_read_only_state_packet_id": (
            local_relevance_medium_read_only_state_packet_id
        ),
        "local_relevance_medium_read_only_state_reader_question": question,
        "local_relevance_medium_read_only_state_reader_intent": (
            local_relevance_medium_read_only_state_reader_intent
        ),
        "selected_local_relevance_medium_comparison_view_artifact": _string_or_empty(
            selected_local_relevance_medium_comparison_view_artifact
        ),
        "state_packet_type": state_packet_type,
        "state_reader_type": state_reader_type,
        "state_reader_scope": state_reader_scope,
        "known_artifact_chain": copy.deepcopy(known_artifact_chain or KNOWN_ARTIFACT_CHAIN),
        "validated_standing_artifacts": artifacts,
        "declared_non_claims": dict(declared_non_claims or _canonical_non_claims()),
    }
    request.update(extra_fields)
    return _sanitize(request)
