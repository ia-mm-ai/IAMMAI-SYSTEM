"""Resolve one local read-only selected-state packet body exposure.

This resolver reads one clean state packet body exposure boundary v2 artifact
and one clean selected-state result object artifact. It records one bounded
LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE object for selected
command ``state`` only.

The object is state-packet-body-exposure-shaped, local, read-only,
selected-state-only, non-raw-full-packet-body-exposure, and non-operation-
shaped. It records ``state_packet_body_exposed`` only in the narrow sense that
one bounded local read-only packet-body exposure event exists. It does not
expose raw/full packet body material, perform lookup, execute lookup commands,
create permissions, create public or distributed surfaces, discover files,
accept entries or signals, create registry/search/query/ranking surfaces, or
authorize follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumReadOnlyStatePacketBodyExposureV0MinError(RuntimeError):
    """Bounded resolver error for state packet body exposure handling."""


RESULT_VERSION = "0.1.0"
BOUNDARY_RESULT_VERSION = "0.1.1"
STATE_RESULT_OBJECT_RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = (
    "resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min"
)

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_RECORDED"
OUTCOME_NOT_RECORDED = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED"
)
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_v0_min"
)
DEFAULT_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_packet_body_exposure_boundary_v0_min_v2/"
    "local_relevance_medium_read_only_state_packet_body_exposure_boundary_"
    "reference_review_001__local_relevance_medium_read_only_state_packet_body_"
    "exposure_boundary_v0_min_v2_result.json"
)
DEFAULT_STATE_RESULT_OBJECT_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_read_only_"
    "state_result_object_v0_min/"
    "local_relevance_medium_read_only_state_result_object_reference_review_001__"
    "local_relevance_medium_read_only_state_result_object_v0_min_result.json"
)

DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID = (
    "local_relevance_medium_read_only_state_packet_body_exposure_001"
)
STATE_PACKET_BODY_EXPOSURE_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE"
)
STATE_PACKET_BODY_EXPOSURE_SCOPE = "SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY"
SELECTED_COMMAND = "state"

STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED"
)
STATE_PACKET_BODY_EXPOSURE_BOUNDARY_TYPE = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BOUNDARY"
)
STATE_PACKET_BODY_EXPOSURE_BOUNDARY_SCOPE = (
    "SELECTED_STATE_PACKET_BODY_EXPOSURE_CONSIDERATION_ONLY"
)
STATE_RESULT_OBJECT_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT_RECORDED"
)
STATE_RESULT_OBJECT_TYPE = "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT"
STATE_RESULT_OBJECT_SCOPE = "SELECTED_STATE_RESULT_OBJECT_ONLY"

SUPPORTED_STATE_PACKET_BODY_EXPOSURE_TYPE_VALUES = (STATE_PACKET_BODY_EXPOSURE_TYPE,)
SUPPORTED_STATE_PACKET_BODY_EXPOSURE_SCOPE_VALUES = (STATE_PACKET_BODY_EXPOSURE_SCOPE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE"
INTENT_DO_NOT_RECORD = (
    "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE"
)
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

CORE_QUESTION = (
    "Given one clean LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_"
    "BOUNDARY for selected command state, and one clean "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_RESULT_OBJECT, may one "
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE be recorded "
    "for the selected-state result object, without exposing raw/full state "
    "packet body, performing lookup, executing lookup command, creating "
    "operation permission, creating runtime permission, creating public API, "
    "creating participant-facing interface, creating distributed network "
    "behavior, creating general lookup permission, creating arbitrary lookup "
    "permission, permitting unsupported commands, permitting unsupported lookup "
    "keys, creating new lookup result, creating new lookup entry, accepting new "
    "entries, accepting new signals, performing filesystem discovery, creating "
    "query surface, registry, search, ranking, scoring, priority, validity "
    "judgment, truth judgment, authority, currentness, synchronization, "
    "participation authorization, participant role, repeated reception "
    "permission, arbitrary reception, feed, source transfer, source receipt, "
    "or follow-on work?"
)

STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS = (
    "raw_full_state_packet_body_exposed",
    "lookup_performed",
    "lookup_command_executed",
    "operation_permission_created",
    "runtime_permission_created",
    "public_api_created",
    "participant_facing_interface_created",
    "distributed_network_behavior_created",
    "general_lookup_permission_created",
    "arbitrary_lookup_permission_created",
    "unsupported_commands_permitted",
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
    "synchronization_created",
    "participation_authorized",
    "participant_role_created",
    "consumed_request_reopened",
    "authorization_token_reused",
    "follow_on_work_authorized",
)

REQUEST_ONLY_FALSE_FIELDS = (
    "source_created",
    "deployment_created",
    "public_release_created",
    "broader_reusable_permission_created",
    "derivative_reception_authorized",
    "vessel_relation_authorized",
    "adoption_created",
    "receiving_context_governance_created",
    "publication_flow_created",
    "artifact_existence_treated_as_state_packet_body_exposure_authority",
    "latest_file_posture_treated_as_state_packet_body_exposure_authority",
    "repo_local_availability_treated_as_state_packet_body_exposure_authority",
    "hidden_repo_state_used_as_state_packet_body_exposure_content",
    "hidden_repo_state_used_as_state_packet_body_exposure_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
)

REQUIRED_FALSE_NON_CLAIMS = (
    STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS + REQUEST_ONLY_FALSE_FIELDS
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_read_only_state_packet_body_exposure_recorded",
    "basis_state_packet_body_exposure_boundary_artifact_preserved",
    "basis_state_result_object_artifact_preserved",
    "selected_command_preserved",
    "selected_command_is_state",
    "selected_state_result_object_recorded",
    "state_result_object_created",
    "state_result_object_local_only",
    "state_result_object_read_only",
    "state_packet_body_exposed",
    "state_packet_body_exposure_local_only",
    "state_packet_body_exposure_read_only",
    "consumed_request_token_remains_closed",
    "authorization_token_reuse_blocked",
    "predecessor_failure_evidence_preserved",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BLOCK_REQUESTED",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_PATH_MISSING",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_UNREADABLE",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_1",
    "STATE_RESULT_OBJECT_ARTIFACT_PATH_MISSING",
    "STATE_RESULT_OBJECT_ARTIFACT_UNREADABLE",
    "STATE_RESULT_OBJECT_ARTIFACT_NOT_JSON_OBJECT",
    "STATE_RESULT_OBJECT_ARTIFACT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_ARTIFACT_FAILED_CHECKS_PRESENT",
    "STATE_RESULT_OBJECT_ARTIFACT_VERSION_NOT_0_1_0",
    "SELECTED_COMMAND_MISSING",
    "SELECTED_COMMAND_NOT_STATE",
    "SELECTED_STATE_RESULT_OBJECT_NOT_RECORDED",
    "STATE_RESULT_OBJECT_NOT_CREATED",
    "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
    "STATE_PACKET_BODY_EXPOSURE_TYPE_MISSING",
    "STATE_PACKET_BODY_EXPOSURE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
    "STATE_PACKET_BODY_EXPOSURE_SCOPE_MISSING",
    "STATE_PACKET_BODY_EXPOSURE_SCOPE_NOT_SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
    "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
    "STATE_PACKET_BODY_NOT_EXPOSED",
    "STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
    "STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
    "RAW_FULL_STATE_PACKET_BODY_EXPOSED",
    "LOOKUP_PERFORMED",
    "LOOKUP_COMMAND_EXECUTED",
    "OPERATION_PERMISSION_CREATED",
    "RUNTIME_PERMISSION_CREATED",
    "PUBLIC_API_CREATED",
    "PARTICIPANT_FACING_INTERFACE_CREATED",
    "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "GENERAL_LOOKUP_PERMISSION_CREATED",
    "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "UNSUPPORTED_COMMANDS_PERMITTED",
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
    "SYNCHRONIZATION_CREATED",
    "PARTICIPATION_AUTHORIZED",
    "PARTICIPANT_ROLE_CREATED",
    "DEPLOYMENT_CREATED",
    "PUBLIC_RELEASE_CREATED",
    "BROADER_REUSABLE_PERMISSION_CREATED",
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_UNREADABLE",
)

FALSE_FIELD_BLOCK_CODES = {
    "raw_full_state_packet_body_exposed": "RAW_FULL_STATE_PACKET_BODY_EXPOSED",
    "lookup_performed": "LOOKUP_PERFORMED",
    "lookup_command_executed": "LOOKUP_COMMAND_EXECUTED",
    "operation_permission_created": "OPERATION_PERMISSION_CREATED",
    "runtime_permission_created": "RUNTIME_PERMISSION_CREATED",
    "public_api_created": "PUBLIC_API_CREATED",
    "participant_facing_interface_created": "PARTICIPANT_FACING_INTERFACE_CREATED",
    "distributed_network_behavior_created": "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    "general_lookup_permission_created": "GENERAL_LOOKUP_PERMISSION_CREATED",
    "arbitrary_lookup_permission_created": "ARBITRARY_LOOKUP_PERMISSION_CREATED",
    "unsupported_commands_permitted": "UNSUPPORTED_COMMANDS_PERMITTED",
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
    "synchronization_created": "SYNCHRONIZATION_CREATED",
    "participation_authorized": "PARTICIPATION_AUTHORIZED",
    "participant_role_created": "PARTICIPANT_ROLE_CREATED",
    "deployment_created": "DEPLOYMENT_CREATED",
    "public_release_created": "PUBLIC_RELEASE_CREATED",
    "broader_reusable_permission_created": "BROADER_REUSABLE_PERMISSION_CREATED",
    "derivative_reception_authorized": "DERIVATIVE_RECEPTION_AUTHORIZED",
    "vessel_relation_authorized": "VESSEL_RELATION_AUTHORIZED",
    "adoption_created": "ADOPTION_CREATED",
    "receiving_context_governance_created": "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "publication_flow_created": "PUBLICATION_FLOW_CREATED",
    "follow_on_work_authorized": "FOLLOW_ON_WORK_AUTHORIZED",
    "consumed_request_reopened": "CONSUMED_REQUEST_REOPENED",
    "authorization_token_reused": "AUTHORIZATION_TOKEN_REUSED",
    "artifact_existence_treated_as_state_packet_body_exposure_authority": (
        "ARTIFACT_EXISTENCE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY"
    ),
    "latest_file_posture_treated_as_state_packet_body_exposure_authority": (
        "LATEST_FILE_POSTURE_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY"
    ),
    "repo_local_availability_treated_as_state_packet_body_exposure_authority": (
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_content": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_CONTENT"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_authority": (
        "HIDDEN_REPO_STATE_USED_AS_STATE_PACKET_BODY_EXPOSURE_AUTHORITY"
    ),
    "prior_artifacts_mutated": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_repaired": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_hidden": "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "predecessor_failure_claimed_passed": (
        "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED"
    ),
}

FALSE_CHECK_NAMES = {
    "raw_full_state_packet_body_exposed": "raw full state packet body not exposed",
    "lookup_performed": "lookup not performed",
    "lookup_command_executed": "lookup command not executed",
    "operation_permission_created": "operation permission not created",
    "runtime_permission_created": "runtime permission not created",
    "public_api_created": "public API not created",
    "participant_facing_interface_created": "participant-facing interface not created",
    "distributed_network_behavior_created": "distributed network behavior not created",
    "general_lookup_permission_created": "general lookup permission not created",
    "arbitrary_lookup_permission_created": "arbitrary lookup permission not created",
    "unsupported_commands_permitted": "unsupported commands not permitted",
    "unsupported_lookup_keys_permitted": "unsupported lookup keys not permitted",
    "new_lookup_result_created": "no new lookup result created",
    "new_lookup_entry_created": "no new lookup entry created",
    "new_signal_accepted": "no new signal accepted",
    "new_entry_accepted": "no new entry accepted",
    "new_relevance_object_created": "no new relevance object created",
    "new_index_entry_created": "no new index entry created",
    "filesystem_discovery_performed": "filesystem discovery not performed",
    "registry_created": "registry not created",
    "search_surface_created": "search not created",
    "query_surface_created": "query surface not created",
    "ranking_surface_created": "ranking not created",
    "scoring_surface_created": "scoring not created",
    "priority_surface_created": "priority not created",
    "validity_judgment_created": "validity judgment not created",
    "truth_judgment_created": "truth judgment not created",
    "authority_judgment_created": "authority judgment not created",
    "currentness_judgment_created": "currentness judgment not created",
    "repeated_reception_permission_created": "repeated reception permission not created",
    "arbitrary_reception_created": "arbitrary reception not created",
    "feed_created": "feed not created",
    "source_transfer_occurred": "source transfer not created",
    "source_receipt_occurred": "source receipt not created",
    "source_created": "source not created",
    "authority_created": "authority not created",
    "currentness_created": "currentness not created",
    "truth_created": "truth not created",
    "synchronization_created": "synchronization not created",
    "participation_authorized": "participation not authorized",
    "participant_role_created": "participant role not created",
    "deployment_created": "deployment not created",
    "public_release_created": "public release not created",
    "broader_reusable_permission_created": "broader reusable permission not created",
    "derivative_reception_authorized": "derivative reception not authorized",
    "vessel_relation_authorized": "vessel relation not authorized",
    "adoption_created": "adoption not created",
    "receiving_context_governance_created": "receiving-context governance not created",
    "publication_flow_created": "publication flow not created",
    "follow_on_work_authorized": "follow-on work not authorized",
    "consumed_request_reopened": "consumed request not reopened",
    "authorization_token_reused": "authorization token not reused",
    "artifact_existence_treated_as_state_packet_body_exposure_authority": (
        "artifact existence not state-packet-body-exposure authority"
    ),
    "latest_file_posture_treated_as_state_packet_body_exposure_authority": (
        "latest file posture not state-packet-body-exposure authority"
    ),
    "repo_local_availability_treated_as_state_packet_body_exposure_authority": (
        "repo-local availability not state-packet-body-exposure authority"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_content": (
        "hidden repo state not state-packet-body-exposure content"
    ),
    "hidden_repo_state_used_as_state_packet_body_exposure_authority": (
        "hidden repo state not state-packet-body-exposure authority"
    ),
    "prior_artifacts_mutated": "prior artifacts not mutated",
    "predecessor_failure_repaired": "predecessor failure not repaired",
    "predecessor_failure_hidden": "predecessor failure not hidden",
    "predecessor_failure_claimed_passed": "predecessor failure not claimed passed",
}

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_state_packet_body_exposure_body",
    "raw_state_packet_body",
    "raw_full_state_packet_body",
    "raw_state_packet_body_exposure_boundary_body",
    "raw_state_result_object_body",
    "raw_state_result_body",
    "raw_lookup_result_body",
    "raw_lookup_performed_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "state_packet_body_exposure_body",
    "state_packet_body",
    "full_state_packet_body",
    "state_packet_body_exposure_boundary_body",
    "state_result_object_body",
    "state_result_body",
    "lookup_result_body",
    "lookup_performed_body",
    "source_body",
    "authority_body",
    "currentness_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_FULL_STATE_PACKET_BODY_MUST_NOT_RETURN",
    "RAW_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_OBJECT_BODY_MUST_NOT_RETURN",
    "RAW_STATE_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_RESULT_BODY_MUST_NOT_RETURN",
    "RAW_LOOKUP_PERFORMED_BODY_MUST_NOT_RETURN",
    "RAW_SOURCE_BODY_MUST_NOT_RETURN",
    "RAW_AUTHORITY_BODY_MUST_NOT_RETURN",
    "RAW_CURRENTNESS_BODY_MUST_NOT_RETURN",
    "RAW_SYNCHRONIZATION_BODY_MUST_NOT_RETURN",
    "RAW_PUBLIC_API_BODY_MUST_NOT_RETURN",
    "RAW_PARTICIPANT_FACING_INTERFACE_BODY_MUST_NOT_RETURN",
    "RAW_DISTRIBUTED_NETWORK_BEHAVIOR_BODY_MUST_NOT_RETURN",
    "RAW_FULL_PRIOR_ARTIFACT_BODY_MUST_NOT_RETURN",
    "HIDDEN_REPO_STATE_MUST_NOT_RETURN",
)

OFFICIAL_VALUES = {
    STATE_PACKET_BODY_EXPOSURE_TYPE,
    STATE_PACKET_BODY_EXPOSURE_SCOPE,
    STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME,
    STATE_PACKET_BODY_EXPOSURE_BOUNDARY_TYPE,
    STATE_PACKET_BODY_EXPOSURE_BOUNDARY_SCOPE,
    STATE_RESULT_OBJECT_RECORDED_OUTCOME,
    STATE_RESULT_OBJECT_TYPE,
    STATE_RESULT_OBJECT_SCOPE,
    SELECTED_COMMAND,
    RESULT_VERSION,
    BOUNDARY_RESULT_VERSION,
    STATE_RESULT_OBJECT_RESULT_VERSION,
    RESOLVER_MODULE,
    *OUTCOME_FAMILY,
    *SUPPORTED_INTENTS,
    *BLOCK_CODES,
    *REQUIRED_FALSE_NON_CLAIMS,
    *ALLOWED_TRUE_RECORDED_FIELDS,
}

WHAT_REMAINS_OPEN = (
    "local relevance medium read-only state packet body exposure terminal summary, if needed",
    "raw/full state packet body exposure",
    "raw/full state packet body exposure boundary",
    "lookup command execution",
    "lookup performed",
    "operation permission",
    "runtime permission",
    "public API",
    "participant-facing interface",
    "distributed network behavior",
    "general lookup permission",
    "arbitrary lookup permission",
    "unsupported-command permission",
    "unsupported-key permission",
    "registry",
    "search surface",
    "query surface",
    "ranking surface",
    "source transfer",
    "source receipt",
    "authority creation",
    "currentness creation",
    "truth creation",
    "synchronization",
    "participation authorization",
    "participant role",
    "deployment",
    "public release",
    "broader reusable permission",
    "repeated reception permission",
    "arbitrary reception",
    "feed",
    "follow-on work",
)


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_key(key: str | None) -> bool:
    if key is None:
        return False
    return key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_key(key):
        return "[REDACTED_SENSITIVE_BODY]"
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str):
        if value in OFFICIAL_VALUES:
            return value
        sanitized = value
        for sentinel in HOSTILE_SENTINELS:
            sanitized = sanitized.replace(sentinel, "[REDACTED_HOSTILE_SENTINEL]")
        return sanitized
    if isinstance(value, Mapping):
        return {str(k): _sanitize(v, str(k)) for k, v in value.items()}
    if isinstance(value, list):
        return [_sanitize(item, key) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item, key) for item in value]
    return value


def _as_path(value: Any) -> Path | None:
    if isinstance(value, Path):
        return value
    if isinstance(value, str) and value:
        return Path(value)
    return None


def _read_json_object(
    path_value: Any,
    unreadable_code: str,
    not_object_code: str,
) -> tuple[dict[str, Any] | None, str | None]:
    path = _as_path(path_value)
    if path is None:
        return None, unreadable_code
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None, unreadable_code
    if not isinstance(value, dict):
        return None, not_object_code
    return _sanitize(value), None


def _get_nested(mapping: Mapping[str, Any] | None, *path: str) -> Any:
    value: Any = mapping
    for key in path:
        if not isinstance(value, Mapping):
            return None
        value = value.get(key)
    return value


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _mapping_section(artifact: Mapping[str, Any] | None, key: str) -> dict[str, Any]:
    value = artifact.get(key) if isinstance(artifact, Mapping) else None
    return dict(value) if isinstance(value, Mapping) else {}


def _count_failed_checks(artifact: Mapping[str, Any] | None, key: str) -> int | None:
    if not isinstance(artifact, Mapping):
        return None
    checks = artifact.get(key)
    if isinstance(checks, list):
        return sum(
            1
            for check in checks
            if isinstance(check, Mapping) and check.get("passed") is not True
        )
    return None


def _artifact_failed_count(
    artifact: Mapping[str, Any] | None,
    summary: Mapping[str, Any],
    checks_key: str,
) -> Any:
    if not isinstance(artifact, Mapping):
        return None
    value = _first_present(summary.get("failed_check_count"), artifact.get("failed_check_count"))
    if value is not None:
        return value
    return _count_failed_checks(artifact, checks_key)


def _artifact_bool(*values: Any) -> bool | None:
    for value in values:
        if isinstance(value, bool):
            return value
    return None


def _declared_non_claims(
    request: Mapping[str, Any] | None,
) -> Mapping[str, Any] | None:
    if not isinstance(request, Mapping):
        return None
    value = request.get("declared_non_claims")
    return value if isinstance(value, Mapping) else None


def _top_or_non_claim(
    request: Mapping[str, Any] | None,
    non_claims: Mapping[str, Any] | None,
    key: str,
) -> Any:
    if isinstance(request, Mapping) and key in request:
        return request[key]
    if isinstance(non_claims, Mapping) and key in non_claims:
        return non_claims[key]
    return None


def _false_field_actual(
    request: Mapping[str, Any],
    non_claims: Mapping[str, Any] | None,
    field: str,
    *basis_maps: Mapping[str, Any],
) -> Any:
    declared = _top_or_non_claim(request, non_claims, field)
    if declared is not None:
        return declared
    for basis in basis_maps:
        if isinstance(basis, Mapping) and field in basis:
            value = basis.get(field)
            if value is True:
                return True
    return False


def _positive_field_actual(
    request: Mapping[str, Any],
    positive_key: str,
    negative_shortcut_key: str,
) -> Any:
    if request.get(negative_shortcut_key) is True:
        return False
    if positive_key in request:
        return request.get(positive_key)
    return True


def _required_non_claims_false(
    non_claims: Mapping[str, Any] | None,
) -> tuple[bool, str]:
    if non_claims is None:
        return False, "declared_non_claims missing or not object"
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in non_claims:
            return False, f"{key} missing"
        if non_claims.get(key) is not False:
            return False, f"{key} is not false"
    return True, "all required non-claims false"


def _check(
    checks: list[dict[str, Any]],
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    code: str | None = None,
) -> None:
    checks.append(
        {
            "check_name": check_name,
            "passed": bool(passed),
            "expected_posture": _sanitize(expected_posture),
            "actual_posture": _sanitize(actual_posture),
            "block_code": None if passed else code,
            "failure_code": None if passed else code,
        }
    )


def _first_failure_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _failed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is not True)


def _passed_check_count(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _block_record(code: str | None, reason: Any = None) -> dict[str, Any]:
    if code is None:
        return {"blocked": False, "code": None, "block_code": None, "reason": None}
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(reason or code),
    }


def _boundary_object(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary",
    )


def _boundary_summary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_summary",
    )


def _boundary_metadata(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_metadata",
    )


def _state_result_object(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_result_object",
    )


def _state_result_object_summary(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_result_object_summary",
    )


def _state_result_object_metadata(artifact: Mapping[str, Any] | None) -> dict[str, Any]:
    return _mapping_section(
        artifact,
        "local_relevance_medium_read_only_state_result_object_metadata",
    )


def _build_packet_exposure_object(
    *,
    exposure_id: str,
    recorded: bool,
    boundary_artifact_path: Path | None,
    boundary_outcome: Any,
    boundary_version: Any,
    boundary_failed_count: Any,
    result_object_artifact_path: Path | None,
    result_object_outcome: Any,
    result_object_version: Any,
    result_object_failed_count: Any,
    selected_command: Any,
    selected_state_result_object_recorded: bool,
    state_result_object_created: bool,
    state_result_object_local_only: bool,
    state_result_object_read_only: bool,
) -> dict[str, Any]:
    object_selected_command = (
        SELECTED_COMMAND if selected_command == SELECTED_COMMAND else None
    )
    packet_exposure: dict[str, Any] = {
        "state_packet_body_exposure_id": exposure_id,
        "state_packet_body_exposure_type": STATE_PACKET_BODY_EXPOSURE_TYPE,
        "state_packet_body_exposure_version": RESULT_VERSION,
        "state_packet_body_exposure_scope": STATE_PACKET_BODY_EXPOSURE_SCOPE,
        "basis_state_packet_body_exposure_boundary_artifact": (
            str(boundary_artifact_path) if boundary_artifact_path else None
        ),
        "basis_state_packet_body_exposure_boundary_outcome": boundary_outcome,
        "basis_state_packet_body_exposure_boundary_result_version": boundary_version,
        "basis_state_packet_body_exposure_boundary_failed_check_count": (
            boundary_failed_count
        ),
        "basis_state_result_object_artifact": (
            str(result_object_artifact_path) if result_object_artifact_path else None
        ),
        "basis_state_result_object_outcome": result_object_outcome,
        "basis_state_result_object_result_version": result_object_version,
        "basis_state_result_object_failed_check_count": result_object_failed_count,
        "selected_command": object_selected_command,
        "selected_command_is_state": object_selected_command == SELECTED_COMMAND,
        "selected_state_result_object_recorded": (
            selected_state_result_object_recorded and recorded
        ),
        "state_result_object_created": state_result_object_created and recorded,
        "state_result_object_local_only": state_result_object_local_only and recorded,
        "state_result_object_read_only": state_result_object_read_only and recorded,
        "local_relevance_medium_read_only_state_packet_body_exposure_recorded": recorded,
        "state_packet_body_exposed": recorded,
        "state_packet_body_exposure_local_only": recorded,
        "state_packet_body_exposure_read_only": recorded,
    }
    for key in STATE_PACKET_BODY_EXPOSURE_OBJECT_FALSE_FIELDS:
        packet_exposure[key] = False
    return packet_exposure


def _build_statement(
    packet_exposure: Mapping[str, Any],
    recorded: bool,
) -> dict[str, bool]:
    return {
        "local_relevance_medium_read_only_state_packet_body_exposure_recorded": recorded,
        "basis_state_packet_body_exposure_boundary_artifact_preserved": recorded,
        "basis_state_result_object_artifact_preserved": recorded,
        "selected_command_preserved": (
            packet_exposure.get("selected_command") == SELECTED_COMMAND
        ),
        "selected_command_is_state": (
            packet_exposure.get("selected_command_is_state") is True
        ),
        "selected_state_result_object_recorded": (
            packet_exposure.get("selected_state_result_object_recorded") is True
        ),
        "state_result_object_created": (
            packet_exposure.get("state_result_object_created") is True
        ),
        "state_result_object_local_only": (
            packet_exposure.get("state_result_object_local_only") is True
        ),
        "state_result_object_read_only": (
            packet_exposure.get("state_result_object_read_only") is True
        ),
        "state_packet_body_exposed": (
            packet_exposure.get("state_packet_body_exposed") is True
        ),
        "state_packet_body_exposure_local_only": (
            packet_exposure.get("state_packet_body_exposure_local_only") is True
        ),
        "state_packet_body_exposure_read_only": (
            packet_exposure.get("state_packet_body_exposure_read_only") is True
        ),
        "consumed_request_token_remains_closed": True,
        "authorization_token_reuse_blocked": True,
        "predecessor_failure_evidence_preserved": True,
        "predecessor_failure_not_repaired": True,
        "predecessor_failure_not_hidden": True,
        "predecessor_failure_not_claimed_passed": True,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "not_raw_full_state_packet_body_exposure": True,
        "not_lookup": True,
        "not_lookup_command_execution": True,
        "not_operation_permission": True,
        "not_runtime_permission": True,
        "not_public_api": True,
        "not_participant_facing_interface": True,
        "not_distributed_network_behavior": True,
        "not_general_lookup_permission": True,
        "not_arbitrary_lookup_permission": True,
        "not_registry": True,
        "not_search": True,
        "not_query_surface": True,
        "not_ranking": True,
        "not_follow_on_work": True,
    }


def _build_declared_question_section(request: Mapping[str, Any] | None) -> dict[str, Any]:
    if request is None:
        return {
            "local_relevance_medium_read_only_state_packet_body_exposure_question": None,
            "local_relevance_medium_read_only_state_packet_body_exposure_intent": None,
            "selected_command": None,
            "state_packet_body_exposure_type": None,
            "state_packet_body_exposure_scope": None,
        }
    return {
        "local_relevance_medium_read_only_state_packet_body_exposure_id": request.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_id"
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_question": request.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_question"
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_intent": request.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_intent"
        ),
        "selected_state_packet_body_exposure_boundary_artifact": (
            str(request.get("selected_state_packet_body_exposure_boundary_artifact"))
            if request.get("selected_state_packet_body_exposure_boundary_artifact")
            is not None
            else None
        ),
        "selected_state_result_object_artifact": (
            str(request.get("selected_state_result_object_artifact"))
            if request.get("selected_state_result_object_artifact") is not None
            else None
        ),
        "selected_command": request.get("selected_command"),
        "state_packet_body_exposure_type": request.get(
            "state_packet_body_exposure_type"
        ),
        "state_packet_body_exposure_scope": request.get(
            "state_packet_body_exposure_scope"
        ),
    }


def _build_boundary_basis(
    boundary_artifact: Mapping[str, Any] | None,
    boundary_path: Path | None,
) -> dict[str, Any]:
    boundary = _boundary_object(boundary_artifact)
    summary = _boundary_summary(boundary_artifact)
    metadata = _boundary_metadata(boundary_artifact)
    if not isinstance(boundary_artifact, Mapping):
        return {
            "selected_state_packet_body_exposure_boundary_artifact": (
                str(boundary_path) if boundary_path else None
            ),
            "basis_artifact_read": False,
            "raw_full_state_packet_body_exposure_boundary_artifact_body_returned": False,
        }
    return {
        "selected_state_packet_body_exposure_boundary_artifact": (
            str(boundary_path) if boundary_path else None
        ),
        "basis_artifact_read": True,
        "basis_state_packet_body_exposure_boundary_artifact_preserved": True,
        "basis_state_packet_body_exposure_boundary_outcome": _first_present(
            boundary_artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_state_packet_body_exposure_boundary_result_version": _first_present(
            summary.get("result_version"),
            boundary_artifact.get("result_version"),
            metadata.get(
                "local_relevance_medium_read_only_state_packet_body_exposure_boundary_version"
            ),
            metadata.get("result_version"),
            boundary.get("boundary_version"),
        ),
        "basis_state_packet_body_exposure_boundary_failed_check_count": (
            _artifact_failed_count(
                boundary_artifact,
                summary,
                "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks",
            )
        ),
        "selected_command": boundary.get("selected_command"),
        "selected_command_is_state": boundary.get("selected_command_is_state"),
        "future_state_packet_body_exposure_may_be_considered": boundary.get(
            "future_state_packet_body_exposure_may_be_considered"
        ),
        "raw_full_state_packet_body_exposure_boundary_artifact_body_returned": False,
    }


def _build_result_object_basis(
    result_object_artifact: Mapping[str, Any] | None,
    result_object_path: Path | None,
) -> dict[str, Any]:
    result_object = _state_result_object(result_object_artifact)
    summary = _state_result_object_summary(result_object_artifact)
    metadata = _state_result_object_metadata(result_object_artifact)
    if not isinstance(result_object_artifact, Mapping):
        return {
            "selected_state_result_object_artifact": (
                str(result_object_path) if result_object_path else None
            ),
            "basis_artifact_read": False,
            "raw_full_state_result_object_artifact_body_returned": False,
        }
    return {
        "selected_state_result_object_artifact": (
            str(result_object_path) if result_object_path else None
        ),
        "basis_artifact_read": True,
        "basis_state_result_object_artifact_preserved": True,
        "basis_state_result_object_outcome": _first_present(
            result_object_artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "basis_state_result_object_result_version": _first_present(
            summary.get("result_version"),
            result_object_artifact.get("result_version"),
            metadata.get("local_relevance_medium_read_only_state_result_object_version"),
            metadata.get("result_version"),
            result_object.get("state_result_object_version"),
        ),
        "basis_state_result_object_failed_check_count": _artifact_failed_count(
            result_object_artifact,
            summary,
            "local_relevance_medium_read_only_state_result_object_checks",
        ),
        "selected_command": result_object.get("selected_command"),
        "selected_command_is_state": result_object.get("selected_command_is_state"),
        "selected_state_result_object_recorded": _first_present(
            result_object.get("selected_state_result_object_recorded"),
            result_object.get(
                "local_relevance_medium_read_only_state_result_object_recorded"
            ),
        ),
        "state_result_object_created": result_object.get("state_result_object_created"),
        "state_result_object_local_only": result_object.get(
            "state_result_object_local_only"
        ),
        "state_result_object_read_only": result_object.get(
            "state_result_object_read_only"
        ),
        "raw_full_state_result_object_artifact_body_returned": False,
    }


def build_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build a compact summary for a state packet body exposure result."""

    checks = result.get("local_relevance_medium_read_only_state_packet_body_exposure_checks")
    checks_list = checks if isinstance(checks, list) else []
    packet_exposure = result.get("local_relevance_medium_read_only_state_packet_body_exposure")
    packet_map = packet_exposure if isinstance(packet_exposure, Mapping) else {}
    statement = result.get("local_relevance_medium_read_only_state_packet_body_exposure_statement")
    statement_map = statement if isinstance(statement, Mapping) else {}
    metadata = result.get("local_relevance_medium_read_only_state_packet_body_exposure_metadata")
    metadata_map = metadata if isinstance(metadata, Mapping) else {}
    declared = result.get(
        "declared_local_relevance_medium_read_only_state_packet_body_exposure_question"
    )
    declared_map = declared if isinstance(declared, Mapping) else {}
    block = result.get("block")
    block_map = block if isinstance(block, Mapping) else {}
    non_claims = result.get("non_claims")
    non_claims_map = non_claims if isinstance(non_claims, Mapping) else {}

    def non_claim_false(key: str) -> bool:
        return non_claims_map.get(key) is False

    return {
        "outcome": result.get("outcome"),
        "block_code": block_map.get("block_code") or block_map.get("code"),
        "block_reason": block_map.get("reason"),
        "state_packet_body_exposure_id": packet_map.get("state_packet_body_exposure_id")
        or metadata_map.get("local_relevance_medium_read_only_state_packet_body_exposure_id"),
        "question": declared_map.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_question"
        ),
        "intent": declared_map.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_intent"
        ),
        "passed_check_count": _passed_check_count(checks_list),
        "failed_check_count": _failed_check_count(checks_list),
        "result_version": RESULT_VERSION,
        "resolver_module": RESOLVER_MODULE,
        "state_packet_body_exposure_recorded": statement_map.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_recorded"
        )
        is True,
        "basis_state_packet_body_exposure_boundary_artifact_preserved": (
            statement_map.get(
                "basis_state_packet_body_exposure_boundary_artifact_preserved"
            )
            is True
        ),
        "basis_state_result_object_artifact_preserved": statement_map.get(
            "basis_state_result_object_artifact_preserved"
        )
        is True,
        "selected_command": packet_map.get("selected_command")
        or declared_map.get("selected_command"),
        "selected_command_preserved": statement_map.get("selected_command_preserved")
        is True,
        "selected_command_is_state": statement_map.get("selected_command_is_state")
        is True,
        "selected_state_result_object_recorded": statement_map.get(
            "selected_state_result_object_recorded"
        )
        is True,
        "state_result_object_created": statement_map.get("state_result_object_created")
        is True,
        "state_result_object_local_only": statement_map.get("state_result_object_local_only")
        is True,
        "state_result_object_read_only": statement_map.get("state_result_object_read_only")
        is True,
        "state_packet_body_exposed": statement_map.get("state_packet_body_exposed")
        is True,
        "state_packet_body_exposure_local_only": statement_map.get(
            "state_packet_body_exposure_local_only"
        )
        is True,
        "state_packet_body_exposure_read_only": statement_map.get(
            "state_packet_body_exposure_read_only"
        )
        is True,
        "state_packet_body_exposure_object_summary": {
            "state_packet_body_exposure_type": packet_map.get(
                "state_packet_body_exposure_type"
            ),
            "state_packet_body_exposure_scope": packet_map.get(
                "state_packet_body_exposure_scope"
            ),
            "state_packet_body_exposure_version": packet_map.get(
                "state_packet_body_exposure_version"
            ),
            "basis_state_packet_body_exposure_boundary_outcome": packet_map.get(
                "basis_state_packet_body_exposure_boundary_outcome"
            ),
            "basis_state_result_object_outcome": packet_map.get(
                "basis_state_result_object_outcome"
            ),
        },
        "raw_full_state_packet_body_not_exposed": non_claim_false(
            "raw_full_state_packet_body_exposed"
        ),
        "lookup_not_performed": non_claim_false("lookup_performed"),
        "lookup_command_not_executed": non_claim_false("lookup_command_executed"),
        "operation_permission_not_created": non_claim_false(
            "operation_permission_created"
        ),
        "runtime_permission_not_created": non_claim_false("runtime_permission_created"),
        "public_api_not_created": non_claim_false("public_api_created"),
        "participant_facing_interface_not_created": non_claim_false(
            "participant_facing_interface_created"
        ),
        "distributed_network_behavior_not_created": non_claim_false(
            "distributed_network_behavior_created"
        ),
        "general_lookup_permission_not_created": non_claim_false(
            "general_lookup_permission_created"
        ),
        "arbitrary_lookup_permission_not_created": non_claim_false(
            "arbitrary_lookup_permission_created"
        ),
        "unsupported_commands_not_permitted": non_claim_false(
            "unsupported_commands_permitted"
        ),
        "unsupported_lookup_keys_not_permitted": non_claim_false(
            "unsupported_lookup_keys_permitted"
        ),
        "no_new_lookup_result_or_entry_created": (
            non_claim_false("new_lookup_result_created")
            and non_claim_false("new_lookup_entry_created")
        ),
        "no_new_signal_entry_relevance_object_or_index_entry_created": (
            non_claim_false("new_signal_accepted")
            and non_claim_false("new_entry_accepted")
            and non_claim_false("new_relevance_object_created")
            and non_claim_false("new_index_entry_created")
        ),
        "filesystem_discovery_not_performed": non_claim_false(
            "filesystem_discovery_performed"
        ),
        "registry_search_query_surface_ranking_not_created": (
            non_claim_false("registry_created")
            and non_claim_false("search_surface_created")
            and non_claim_false("query_surface_created")
            and non_claim_false("ranking_surface_created")
        ),
        "scoring_priority_validity_truth_authority_currentness_judgment_not_created": (
            non_claim_false("scoring_surface_created")
            and non_claim_false("priority_surface_created")
            and non_claim_false("validity_judgment_created")
            and non_claim_false("truth_judgment_created")
            and non_claim_false("authority_judgment_created")
            and non_claim_false("currentness_judgment_created")
        ),
        "repeated_reception_arbitrary_reception_feed_not_created": (
            non_claim_false("repeated_reception_permission_created")
            and non_claim_false("arbitrary_reception_created")
            and non_claim_false("feed_created")
        ),
        "source_authority_currentness_truth_synchronization_participation_participant_role_not_created": (
            non_claim_false("source_created")
            and non_claim_false("authority_created")
            and non_claim_false("currentness_created")
            and non_claim_false("truth_created")
            and non_claim_false("synchronization_created")
            and non_claim_false("participation_authorized")
            and non_claim_false("participant_role_created")
        ),
        "consumed_request_token_remains_closed": non_claim_false(
            "consumed_request_reopened"
        ),
        "authorization_token_reuse_blocked": non_claim_false(
            "authorization_token_reused"
        ),
        "predecessor_failure_evidence_preserved": (
            non_claim_false("predecessor_failure_repaired")
            and non_claim_false("predecessor_failure_hidden")
            and non_claim_false("predecessor_failure_claimed_passed")
        ),
        "follow_on_not_created": non_claim_false("follow_on_work_authorized"),
        "key_non_claims": {
            key: non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        },
        "result_level_non_claims_canonical_false": all(
            non_claims_map.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS
        ),
    }


def _assemble_result(
    *,
    request: Mapping[str, Any] | None,
    outcome: str,
    checks: list[dict[str, Any]],
    packet_exposure: Mapping[str, Any],
    boundary_artifact: Mapping[str, Any] | None,
    boundary_path: Path | None,
    result_object_artifact: Mapping[str, Any] | None,
    result_object_path: Path | None,
    additional_basis_required: list[str] | None = None,
    not_recorded_basis: list[str] | None = None,
) -> dict[str, Any]:
    exposure_id = str(
        packet_exposure.get("state_packet_body_exposure_id")
        or DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID
    )
    recorded = outcome == OUTCOME_RECORDED
    block_code = _first_failure_code(checks) if outcome == OUTCOME_BLOCKED else None
    result: dict[str, Any] = {
        "local_relevance_medium_read_only_state_packet_body_exposure_metadata": {
            "local_relevance_medium_read_only_state_packet_body_exposure_id": exposure_id,
            "local_relevance_medium_read_only_state_packet_body_exposure_type": (
                STATE_PACKET_BODY_EXPOSURE_TYPE
            ),
            "local_relevance_medium_read_only_state_packet_body_exposure_version": (
                RESULT_VERSION
            ),
            "generated_at": _now(),
            "resolver_module": RESOLVER_MODULE,
            "predecessor_resolver_module": (
                "resolve_local_relevance_medium_read_only_state_packet_body_exposure_boundary_v0_min"
            ),
            "predecessor_failure_preserved_as_lineage_evidence": True,
        },
        "declared_local_relevance_medium_read_only_state_packet_body_exposure_question": (
            _build_declared_question_section(request)
        ),
        "selected_state_packet_body_exposure_boundary_artifact_basis": (
            _build_boundary_basis(boundary_artifact, boundary_path)
        ),
        "selected_state_result_object_artifact_basis": _build_result_object_basis(
            result_object_artifact,
            result_object_path,
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure": dict(
            packet_exposure
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_checks": checks,
        "local_relevance_medium_read_only_state_packet_body_exposure_statement": (
            _build_statement(packet_exposure, recorded)
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": additional_basis_required or [],
        "not_recorded_basis": not_recorded_basis or [],
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": _canonical_false_non_claims(),
        "outcome": outcome,
        "block": _block_record(block_code),
    }
    result["local_relevance_medium_read_only_state_packet_body_exposure_summary"] = (
        build_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_summary(
            result
        )
    )
    return _sanitize(result)


def _malformed_result(code: str, reason: str) -> dict[str, Any]:
    checks: list[dict[str, Any]] = []
    _check(
        checks,
        "declared local relevance medium read only state packet body exposure request is mapping",
        False,
        "mapping request",
        reason,
        code,
    )
    packet_exposure = _build_packet_exposure_object(
        exposure_id=DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID,
        recorded=False,
        boundary_artifact_path=None,
        boundary_outcome=None,
        boundary_version=None,
        boundary_failed_count=None,
        result_object_artifact_path=None,
        result_object_outcome=None,
        result_object_version=None,
        result_object_failed_count=None,
        selected_command=None,
        selected_state_result_object_recorded=False,
        state_result_object_created=False,
        state_result_object_local_only=False,
        state_result_object_read_only=False,
    )
    return _assemble_result(
        request=None,
        outcome=OUTCOME_BLOCKED,
        checks=checks,
        packet_exposure=packet_exposure,
        boundary_artifact=None,
        boundary_path=None,
        result_object_artifact=None,
        result_object_path=None,
    )


def resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
    declared_local_relevance_medium_read_only_state_packet_body_exposure: Mapping[
        str, Any
    ]
    | None = None,
) -> dict:
    """Resolve one local read-only selected-state packet body exposure request."""

    if declared_local_relevance_medium_read_only_state_packet_body_exposure is None:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request missing",
        )
    if not isinstance(
        declared_local_relevance_medium_read_only_state_packet_body_exposure,
        Mapping,
    ):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request is not a mapping",
        )

    request = copy.deepcopy(
        dict(declared_local_relevance_medium_read_only_state_packet_body_exposure)
    )
    non_claims = _declared_non_claims(request)
    checks: list[dict[str, Any]] = []

    exposure_id = str(
        request.get("local_relevance_medium_read_only_state_packet_body_exposure_id")
        or DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID
    )
    question = request.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_question"
    )
    intent = request.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_intent"
    )

    _check(
        checks,
        "state packet body exposure question declared",
        isinstance(question, str) and bool(question.strip()),
        "declared state packet body exposure question",
        question,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_QUESTION_UNDECLARED",
    )
    _check(
        checks,
        "state packet body exposure intent supported",
        intent in SUPPORTED_INTENTS,
        SUPPORTED_INTENTS,
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_INTENT_UNSUPPORTED",
    )
    _check(
        checks,
        "state packet body exposure block intent not requested",
        intent != INTENT_BLOCK,
        f"not {INTENT_BLOCK}",
        intent,
        "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_BLOCK_REQUESTED",
    )

    boundary_path = _as_path(
        request.get("selected_state_packet_body_exposure_boundary_artifact")
    )
    result_object_path = _as_path(request.get("selected_state_result_object_artifact"))
    boundary_missing_requested = (
        request.get("state_packet_body_exposure_boundary_artifact_missing") is True
    )
    result_object_missing_requested = (
        request.get("state_result_object_artifact_missing") is True
    )

    _check(
        checks,
        "state packet body exposure boundary artifact path declared",
        boundary_path is not None and not boundary_missing_requested,
        "declared state packet body exposure boundary artifact path",
        str(boundary_path) if boundary_path else None,
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_PATH_MISSING",
    )
    boundary_artifact: dict[str, Any] | None = None
    boundary_read_code: str | None = None
    if boundary_path is not None and not boundary_missing_requested:
        boundary_artifact, boundary_read_code = _read_json_object(
            boundary_path,
            "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_UNREADABLE",
            "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "state packet body exposure boundary artifact readable JSON",
            boundary_read_code is None,
            "readable JSON object",
            boundary_read_code or "readable JSON object",
            boundary_read_code,
        )

    _check(
        checks,
        "state result object artifact path declared",
        result_object_path is not None and not result_object_missing_requested,
        "declared selected-state result object artifact path",
        str(result_object_path) if result_object_path else None,
        "STATE_RESULT_OBJECT_ARTIFACT_PATH_MISSING",
    )
    result_object_artifact: dict[str, Any] | None = None
    result_object_read_code: str | None = None
    if result_object_path is not None and not result_object_missing_requested:
        result_object_artifact, result_object_read_code = _read_json_object(
            result_object_path,
            "STATE_RESULT_OBJECT_ARTIFACT_UNREADABLE",
            "STATE_RESULT_OBJECT_ARTIFACT_NOT_JSON_OBJECT",
        )
        _check(
            checks,
            "state result object artifact readable JSON",
            result_object_read_code is None,
            "readable JSON object",
            result_object_read_code or "readable JSON object",
            result_object_read_code,
        )

    boundary = _boundary_object(boundary_artifact)
    boundary_summary = _boundary_summary(boundary_artifact)
    boundary_metadata = _boundary_metadata(boundary_artifact)
    result_object = _state_result_object(result_object_artifact)
    result_object_summary = _state_result_object_summary(result_object_artifact)
    result_object_metadata = _state_result_object_metadata(result_object_artifact)

    boundary_outcome = _first_present(
        boundary_artifact.get("outcome") if boundary_artifact else None,
        boundary_summary.get("outcome"),
    )
    boundary_version = _first_present(
        boundary_summary.get("result_version"),
        boundary_artifact.get("result_version") if boundary_artifact else None,
        boundary_metadata.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_boundary_version"
        ),
        boundary_metadata.get("result_version"),
        boundary.get("boundary_version"),
    )
    boundary_failed_count = _artifact_failed_count(
        boundary_artifact,
        boundary_summary,
        "local_relevance_medium_read_only_state_packet_body_exposure_boundary_checks",
    )
    result_object_outcome = _first_present(
        result_object_artifact.get("outcome") if result_object_artifact else None,
        result_object_summary.get("outcome"),
    )
    result_object_version = _first_present(
        result_object_summary.get("result_version"),
        result_object_artifact.get("result_version") if result_object_artifact else None,
        result_object_metadata.get(
            "local_relevance_medium_read_only_state_result_object_version"
        ),
        result_object_metadata.get("result_version"),
        result_object.get("state_result_object_version"),
    )
    result_object_failed_count = _artifact_failed_count(
        result_object_artifact,
        result_object_summary,
        "local_relevance_medium_read_only_state_result_object_checks",
    )

    _check(
        checks,
        "state packet body exposure boundary artifact outcome recorded",
        boundary_outcome == STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME
        and request.get("state_packet_body_exposure_boundary_artifact_not_recorded")
        is not True,
        STATE_PACKET_BODY_EXPOSURE_BOUNDARY_RECORDED_OUTCOME,
        boundary_outcome,
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state packet body exposure boundary artifact result version 0.1.1",
        boundary_version == BOUNDARY_RESULT_VERSION
        and request.get("state_packet_body_exposure_boundary_artifact_version_not_0_1_1")
        is not True,
        BOUNDARY_RESULT_VERSION,
        boundary_version,
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_VERSION_NOT_0_1_1",
    )
    _check(
        checks,
        "state packet body exposure boundary artifact failed check count zero",
        boundary_failed_count == 0
        and request.get("state_packet_body_exposure_boundary_artifact_failed_checks_present")
        is not True,
        0,
        boundary_failed_count,
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_FAILED_CHECKS_PRESENT",
    )
    _check(
        checks,
        "state result object artifact outcome recorded",
        result_object_outcome == STATE_RESULT_OBJECT_RECORDED_OUTCOME
        and request.get("state_result_object_artifact_not_recorded") is not True,
        STATE_RESULT_OBJECT_RECORDED_OUTCOME,
        result_object_outcome,
        "STATE_RESULT_OBJECT_ARTIFACT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object artifact result version 0.1.0",
        result_object_version == STATE_RESULT_OBJECT_RESULT_VERSION
        and request.get("state_result_object_artifact_version_not_0_1_0") is not True,
        STATE_RESULT_OBJECT_RESULT_VERSION,
        result_object_version,
        "STATE_RESULT_OBJECT_ARTIFACT_VERSION_NOT_0_1_0",
    )
    _check(
        checks,
        "state result object artifact failed check count zero",
        result_object_failed_count == 0
        and request.get("state_result_object_artifact_failed_checks_present") is not True,
        0,
        result_object_failed_count,
        "STATE_RESULT_OBJECT_ARTIFACT_FAILED_CHECKS_PRESENT",
    )

    selected_command = request.get("selected_command")
    artifact_commands_are_state = all(
        command in (None, SELECTED_COMMAND)
        for command in (
            boundary.get("selected_command"),
            result_object.get("selected_command"),
        )
    )
    _check(
        checks,
        "selected command declared",
        selected_command is not None
        and request.get("selected_command_missing") is not True,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_MISSING",
    )
    _check(
        checks,
        "selected command exactly state",
        selected_command == SELECTED_COMMAND
        and artifact_commands_are_state
        and request.get("selected_command_not_state") is not True,
        SELECTED_COMMAND,
        selected_command,
        "SELECTED_COMMAND_NOT_STATE",
    )
    _check(
        checks,
        "selected command is state",
        selected_command == SELECTED_COMMAND
        and boundary.get("selected_command_is_state") is not False
        and result_object.get("selected_command_is_state") is not False,
        True,
        selected_command == SELECTED_COMMAND,
        "SELECTED_COMMAND_NOT_STATE",
    )

    selected_state_result_object_recorded = _artifact_bool(
        result_object.get("selected_state_result_object_recorded"),
        result_object.get(
            "local_relevance_medium_read_only_state_result_object_recorded"
        ),
        boundary.get("selected_state_result_object_recorded"),
    )
    state_result_object_created = _artifact_bool(
        result_object.get("state_result_object_created"),
        boundary.get("state_result_object_created"),
    )
    state_result_object_local_only = _artifact_bool(
        result_object.get("state_result_object_local_only"),
        boundary.get("state_result_object_local_only"),
    )
    state_result_object_read_only = _artifact_bool(
        result_object.get("state_result_object_read_only"),
        boundary.get("state_result_object_read_only"),
    )

    _check(
        checks,
        "selected-state result object recorded",
        selected_state_result_object_recorded is True
        and request.get("selected_state_result_object_not_recorded") is not True,
        True,
        selected_state_result_object_recorded,
        "SELECTED_STATE_RESULT_OBJECT_NOT_RECORDED",
    )
    _check(
        checks,
        "state result object created",
        state_result_object_created is True
        and request.get("state_result_object_not_created") is not True,
        True,
        state_result_object_created,
        "STATE_RESULT_OBJECT_NOT_CREATED",
    )
    _check(
        checks,
        "state result object local only",
        state_result_object_local_only is True
        and request.get("state_result_object_local_only_not_true") is not True,
        True,
        state_result_object_local_only,
        "STATE_RESULT_OBJECT_LOCAL_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state result object read only",
        state_result_object_read_only is True
        and request.get("state_result_object_read_only_not_true") is not True,
        True,
        state_result_object_read_only,
        "STATE_RESULT_OBJECT_READ_ONLY_NOT_TRUE",
    )
    _check(
        checks,
        "state packet body exposure boundary permits future consideration",
        boundary.get("future_state_packet_body_exposure_may_be_considered") is True,
        True,
        boundary.get("future_state_packet_body_exposure_may_be_considered"),
        "STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT_NOT_RECORDED",
    )

    exposure_type = request.get("state_packet_body_exposure_type")
    exposure_scope = request.get("state_packet_body_exposure_scope")
    _check(
        checks,
        "state packet body exposure type exact",
        exposure_type == STATE_PACKET_BODY_EXPOSURE_TYPE
        and request.get(
            "state_packet_body_exposure_type_not_local_relevance_medium_read_only_state_packet_body_exposure"
        )
        is not True,
        STATE_PACKET_BODY_EXPOSURE_TYPE,
        exposure_type,
        "STATE_PACKET_BODY_EXPOSURE_TYPE_MISSING"
        if exposure_type is None
        else "STATE_PACKET_BODY_EXPOSURE_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE",
    )
    _check(
        checks,
        "state packet body exposure scope exact",
        exposure_scope == STATE_PACKET_BODY_EXPOSURE_SCOPE
        and request.get(
            "state_packet_body_exposure_scope_not_selected_state_packet_body_exposure_only"
        )
        is not True,
        STATE_PACKET_BODY_EXPOSURE_SCOPE,
        exposure_scope,
        "STATE_PACKET_BODY_EXPOSURE_SCOPE_MISSING"
        if exposure_scope is None
        else "STATE_PACKET_BODY_EXPOSURE_SCOPE_NOT_SELECTED_STATE_PACKET_BODY_EXPOSURE_ONLY",
    )

    positive_checks = (
        (
            "local relevance medium read-only state packet body exposure recorded",
            "local_relevance_medium_read_only_state_packet_body_exposure_recorded",
            "local_relevance_medium_read_only_state_packet_body_exposure_not_recorded",
            "LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_NOT_RECORDED",
        ),
        (
            "state packet body exposed",
            "state_packet_body_exposed",
            "state_packet_body_not_exposed",
            "STATE_PACKET_BODY_NOT_EXPOSED",
        ),
        (
            "state packet body exposure local only",
            "state_packet_body_exposure_local_only",
            "state_packet_body_exposure_local_only_not_true",
            "STATE_PACKET_BODY_EXPOSURE_LOCAL_ONLY_NOT_TRUE",
        ),
        (
            "state packet body exposure read only",
            "state_packet_body_exposure_read_only",
            "state_packet_body_exposure_read_only_not_true",
            "STATE_PACKET_BODY_EXPOSURE_READ_ONLY_NOT_TRUE",
        ),
    )
    for check_name, positive_key, negative_key, code in positive_checks:
        actual = _positive_field_actual(request, positive_key, negative_key)
        _check(checks, check_name, actual is True, True, actual, code)

    basis_maps = (boundary, result_object)
    for field, check_name in FALSE_CHECK_NAMES.items():
        actual = _false_field_actual(request, non_claims, field, *basis_maps)
        code = FALSE_FIELD_BLOCK_CODES.get(field, "NON_CLAIM_MISSING_OR_FLIPPED")
        _check(checks, check_name, actual is False, False, actual, code)

    required_non_claims_passed, required_non_claims_actual = _required_non_claims_false(
        non_claims
    )
    _check(
        checks,
        "required non-claims false",
        required_non_claims_passed,
        "all required non-claims present as false bool",
        required_non_claims_actual,
        "NON_CLAIM_MISSING_OR_FLIPPED",
    )
    _check(
        checks,
        "result-level required false non-claims canonical false",
        True,
        "canonical false result-level non-claims",
        "canonical false result-level non-claims",
        None,
    )

    failed = _failed_check_count(checks) > 0
    additional_basis = request.get("additional_basis_context", [])
    if not isinstance(additional_basis, list):
        additional_basis = [str(_sanitize(additional_basis))]
    not_recorded_basis = request.get("not_recorded_basis", [])
    if not isinstance(not_recorded_basis, list):
        not_recorded_basis = [str(_sanitize(not_recorded_basis))]

    if failed:
        outcome = OUTCOME_BLOCKED
    elif intent == INTENT_DO_NOT_RECORD:
        outcome = OUTCOME_NOT_RECORDED
        not_recorded_basis = not_recorded_basis or [
            "declared request chose not to record state packet body exposure"
        ]
    elif (
        request.get(
            "requested_local_relevance_medium_read_only_state_packet_body_exposure_outcome"
        )
        == OUTCOME_REQUIRES_ADDITIONAL_BASIS
        or additional_basis
    ):
        outcome = OUTCOME_REQUIRES_ADDITIONAL_BASIS
        additional_basis = additional_basis or [
            "additional state packet body exposure basis requested by declaration"
        ]
    else:
        outcome = OUTCOME_RECORDED

    recorded = outcome == OUTCOME_RECORDED
    packet_exposure = _build_packet_exposure_object(
        exposure_id=exposure_id,
        recorded=recorded,
        boundary_artifact_path=boundary_path,
        boundary_outcome=boundary_outcome,
        boundary_version=boundary_version,
        boundary_failed_count=boundary_failed_count,
        result_object_artifact_path=result_object_path,
        result_object_outcome=result_object_outcome,
        result_object_version=result_object_version,
        result_object_failed_count=result_object_failed_count,
        selected_command=selected_command,
        selected_state_result_object_recorded=selected_state_result_object_recorded
        is True,
        state_result_object_created=state_result_object_created is True,
        state_result_object_local_only=state_result_object_local_only is True,
        state_result_object_read_only=state_result_object_read_only is True,
    )

    return _assemble_result(
        request=request,
        outcome=outcome,
        checks=checks,
        packet_exposure=packet_exposure,
        boundary_artifact=boundary_artifact,
        boundary_path=boundary_path,
        result_object_artifact=result_object_artifact,
        result_object_path=result_object_path,
        additional_basis_required=additional_basis,
        not_recorded_basis=not_recorded_basis,
    )


def resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_from_path(
    declared_local_relevance_medium_read_only_state_packet_body_exposure_path: Path
    | str,
) -> dict:
    """Read a declared request JSON object from a path and resolve it."""

    try:
        path = Path(declared_local_relevance_medium_read_only_state_packet_body_exposure_path)
        value = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_UNREADABLE",
            f"request unreadable: {exc}",
        )
    if not isinstance(value, dict):
        return _malformed_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_READ_ONLY_STATE_PACKET_BODY_EXPOSURE_REQUEST_MALFORMED",
            "request JSON is not an object",
        )
    return resolve_local_relevance_medium_read_only_state_packet_body_exposure_v0_min(
        value
    )


def write_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a resolver result artifact without silently overwriting files."""

    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumReadOnlyStatePacketBodyExposureV0MinError(
            "result must be a mapping"
        )
    metadata = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure_metadata",
        {},
    )
    packet_exposure = result.get(
        "local_relevance_medium_read_only_state_packet_body_exposure",
        {},
    )
    exposure_id = None
    if isinstance(metadata, Mapping):
        exposure_id = metadata.get(
            "local_relevance_medium_read_only_state_packet_body_exposure_id"
        )
    if not exposure_id and isinstance(packet_exposure, Mapping):
        exposure_id = packet_exposure.get("state_packet_body_exposure_id")
    exposure_id = str(exposure_id or DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID)
    filename = (
        f"{exposure_id}__"
        "local_relevance_medium_read_only_state_packet_body_exposure_v0_min_result.json"
    )

    if output_path is None:
        candidate = OUTPUT_ROOT / filename
    else:
        output = Path(output_path)
        candidate = output if output.suffix == ".json" else output / filename

    candidate.parent.mkdir(parents=True, exist_ok=True)
    if candidate.exists():
        stem = candidate.stem
        suffix = candidate.suffix
        parent = candidate.parent
        index = 1
        while True:
            next_candidate = parent / f"{stem}_{index:03d}{suffix}"
            if not next_candidate.exists():
                candidate = next_candidate
                break
            index += 1

    candidate.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return candidate


def build_declared_local_relevance_medium_read_only_state_packet_body_exposure_v0_min_request(
    *,
    local_relevance_medium_read_only_state_packet_body_exposure_id: str = (
        DEFAULT_STATE_PACKET_BODY_EXPOSURE_ID
    ),
    selected_state_packet_body_exposure_boundary_artifact: Path | str = (
        DEFAULT_STATE_PACKET_BODY_EXPOSURE_BOUNDARY_ARTIFACT
    ),
    selected_state_result_object_artifact: Path | str = (
        DEFAULT_STATE_RESULT_OBJECT_ARTIFACT
    ),
    selected_command: str = SELECTED_COMMAND,
    state_packet_body_exposure_type: str = STATE_PACKET_BODY_EXPOSURE_TYPE,
    state_packet_body_exposure_scope: str = STATE_PACKET_BODY_EXPOSURE_SCOPE,
    intent: str = INTENT_RECORD,
    declared_non_claims: Mapping[str, Any] | None = None,
) -> dict[str, Any]:
    """Build a declared request for one selected-state packet body exposure."""

    if selected_command != SELECTED_COMMAND:
        raise LocalRelevanceMediumReadOnlyStatePacketBodyExposureV0MinError(
            "selected_command must be exactly state"
        )
    non_claims = (
        _canonical_false_non_claims()
        if declared_non_claims is None
        else {key: declared_non_claims.get(key, False) for key in REQUIRED_FALSE_NON_CLAIMS}
    )
    return {
        "local_relevance_medium_read_only_state_packet_body_exposure_id": (
            local_relevance_medium_read_only_state_packet_body_exposure_id
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_question": (
            CORE_QUESTION
        ),
        "local_relevance_medium_read_only_state_packet_body_exposure_intent": intent,
        "selected_state_packet_body_exposure_boundary_artifact": str(
            selected_state_packet_body_exposure_boundary_artifact
        ),
        "selected_state_result_object_artifact": str(
            selected_state_result_object_artifact
        ),
        "selected_command": SELECTED_COMMAND,
        "state_packet_body_exposure_type": state_packet_body_exposure_type,
        "state_packet_body_exposure_scope": state_packet_body_exposure_scope,
        "local_relevance_medium_read_only_state_packet_body_exposure_recorded": True,
        "state_packet_body_exposed": True,
        "state_packet_body_exposure_local_only": True,
        "state_packet_body_exposure_read_only": True,
        "consumed_request_reopened": False,
        "authorization_token_reused": False,
        "declared_non_claims": non_claims,
    }

