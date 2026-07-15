"""Minimum resolver for one local relevance medium successor reception request.

This module records one small request object from one clean local relevance
orientation index entry artifact.  It is request-object-shaped: it does not
create a second reception, admit a successor candidate, create repeated
reception permission, create a feed, create relation, create an index system,
create a registry, create search or ranking, or create source, authority,
currentness, truth, action, synchronization, runtime permission, public API,
distributed behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumSuccessorReceptionRequestV0MinError(Exception):
    """Raised for unreadable successor reception request declarations."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_successor_reception_request_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REQUEST_TYPE = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
REQUEST_SCOPE_ONE_SUCCESSOR_ONLY = "ONE_SUCCESSOR_RECEPTION_REQUEST_ONLY"
SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY = "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY"
MULTIPLICITY_PURPOSE_LOCAL_ONLY = "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY"
SUPPORTED_REQUEST_SCOPE_VALUES = (REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,)
SUPPORTED_REQUEST_TYPE_VALUES = (REQUEST_TYPE,)
SUPPORTED_SUCCESSOR_CANDIDATE_SCOPE_VALUES = (
    SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
)
SUPPORTED_MULTIPLICITY_PURPOSE_VALUES = (MULTIPLICITY_PURPOSE_LOCAL_ONLY,)

INDEX_ENTRY_TYPE = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY"
INDEX_ENTRY_SCOPE_LOCAL_ONLY = "LOCAL_INDEX_ENTRY_ONLY"
INDEX_ENTRY_OUTCOME_RECORDED = "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_RECORDED"
INDEX_ENTRY_RESULT_VERSION = "0.1.0"

DEFAULT_SUCCESSOR_CANDIDATE_ID = "bounded_relevance_signal_candidate_002"

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_"
    "local_relevance_medium_successor_reception_request_v0_min"
)
DEFAULT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_orientation_index_entry_v0_min/"
    "local_relevance_orientation_index_entry_reference_review_001__"
    "local_relevance_orientation_index_entry_v0_min_result.json"
)

CORE_QUESTION = (
    "Given one clean local relevance orientation index entry and its completed "
    "upstream reception -> receipt v2 -> orientation view -> local index-entry "
    "chain, may one LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST be "
    "recorded for one additional bounded relevance reception candidate, solely "
    "so local medium multiplicity may later become testable, without creating "
    "second reception, successor admission, repeated reception permission, "
    "arbitrary reception, feed, relation view, index system, registry, search, "
    "ranking, source transfer, source receipt, reception authorization, "
    "authority, currentness, truth, action, synchronization, participation "
    "authorization, participant role, runtime permission, public API, "
    "participant-facing interface, distributed network behavior, operation "
    "permission, or follow-on work?"
)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_reception_created",
    "successor_candidate_admitted",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "relation_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
    "source_transfer_occurred",
    "source_receipt_occurred",
    "reception_authorization_created",
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
    "artifact_existence_treated_as_request_authority",
    "latest_file_posture_treated_as_request_authority",
    "repo_local_availability_treated_as_request_authority",
    "hidden_repo_state_used_as_request_content",
    "hidden_repo_state_used_as_request_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_successor_reception_request_recorded",
    "basis_index_entry_artifact_preserved",
    "existing_orientation_view_artifact_preserved",
    "existing_source_receipt_artifact_preserved",
    "existing_referenced_reception_artifact_preserved",
    "existing_received_signal_id_preserved",
    "existing_received_relevance_basis_id_preserved",
    "existing_received_relevance_scope_id_preserved",
    "existing_received_carrier_context_id_preserved",
    "existing_received_reception_envelope_id_preserved",
    "successor_candidate_id_declared",
    "successor_candidate_differs_from_existing_signal",
    "successor_candidate_scope_bounded_only",
    "request_scope_one_successor_only",
    "multiplicity_purpose_local_only",
    "max_local_orientation_objects_after_successor_is_two",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_BLOCK_REQUESTED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
    "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
    "INDEX_ENTRY_MISSING",
    "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
    "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
    "EXISTING_ORIENTATION_VIEW_ARTIFACT_MISSING",
    "EXISTING_SOURCE_RECEIPT_ARTIFACT_MISSING",
    "EXISTING_REFERENCED_RECEPTION_ARTIFACT_MISSING",
    "EXISTING_RECEIVED_SIGNAL_ID_MISSING",
    "EXISTING_RECEIVED_RELEVANCE_BASIS_ID_MISSING",
    "EXISTING_RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
    "EXISTING_RECEIVED_CARRIER_CONTEXT_ID_MISSING",
    "EXISTING_RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
    "SUCCESSOR_CANDIDATE_ID_MISSING",
    "SUCCESSOR_CANDIDATE_ID_EQUALS_EXISTING_SIGNAL",
    "REQUEST_SCOPE_MISSING",
    "REQUEST_SCOPE_NOT_ONE_SUCCESSOR_ONLY",
    "REQUEST_TYPE_MISSING",
    "REQUEST_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST",
    "SUCCESSOR_CANDIDATE_SCOPE_MISSING",
    "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY",
    "MULTIPLICITY_PURPOSE_MISSING",
    "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
    "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_SUCCESSOR_NOT_TWO",
    "SECOND_RECEPTION_CREATED",
    "SUCCESSOR_CANDIDATE_ADMITTED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "RELATION_VIEW_CREATED",
    "INDEX_SYSTEM_CREATED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
    "SOURCE_TRANSFER_OCCURRED",
    "SOURCE_RECEIPT_OCCURRED",
    "RECEPTION_AUTHORIZATION_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_REQUEST_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_REQUEST_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_REQUEST_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_REQUEST_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_REQUEST_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_UNREADABLE",
)

RAW_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_RECEPTION_REQUEST_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_BODY_MUST_NOT_RETURN",
    "RAW_INDEX_ENTRY_BODY_MUST_NOT_RETURN",
    "RAW_ORIENTATION_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEIPT_BODY_MUST_NOT_RETURN",
    "RAW_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
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
    "raw_request_body",
    "raw_successor_reception_request_body",
    "raw_successor_candidate_body",
    "raw_index_entry_body",
    "raw_orientation_body",
    "raw_bounded_relevance_receipt_body",
    "raw_bounded_relevance_reception_body",
    "raw_source_body",
    "raw_authority_body",
    "raw_currentness_body",
    "raw_action_body",
    "raw_synchronization_body",
    "raw_public_api_body",
    "raw_participant_facing_interface_body",
    "raw_distributed_network_behavior_body",
    "request_body",
    "successor_reception_request_body",
    "successor_candidate_body",
    "index_entry_body",
    "orientation_body",
    "bounded_relevance_receipt_body",
    "bounded_relevance_reception_body",
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

REQUEST_OBJECT_FIELDS = (
    "request_id",
    "request_type",
    "request_version",
    "request_scope",
    "basis_index_entry_artifact",
    "existing_orientation_view_artifact",
    "existing_source_receipt_artifact",
    "existing_referenced_reception_artifact",
    "existing_received_signal_id",
    "existing_received_relevance_basis_id",
    "existing_received_relevance_scope_id",
    "existing_received_carrier_context_id",
    "existing_received_reception_envelope_id",
    "successor_candidate_id",
    "successor_candidate_scope",
    "multiplicity_purpose",
    "max_local_orientation_objects_after_successor",
    "second_reception_created",
    "successor_candidate_admitted",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "relation_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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

BOOLEAN_OVERREACH_CHECKS = (
    ("second reception not created", "second_reception_created", "SECOND_RECEPTION_CREATED"),
    (
        "successor candidate not admitted",
        "successor_candidate_admitted",
        "SUCCESSOR_CANDIDATE_ADMITTED",
    ),
    (
        "repeated reception permission not created",
        "repeated_reception_permission_created",
        "REPEATED_RECEPTION_PERMISSION_CREATED",
    ),
    (
        "arbitrary reception not created",
        "arbitrary_reception_created",
        "ARBITRARY_RECEPTION_CREATED",
    ),
    ("feed not created", "feed_created", "FEED_CREATED"),
    ("relation view not created", "relation_view_created", "RELATION_VIEW_CREATED"),
    ("index system not created", "index_system_created", "INDEX_SYSTEM_CREATED"),
    ("registry not created", "registry_created", "REGISTRY_CREATED"),
    ("search not created", "search_surface_created", "SEARCH_SURFACE_CREATED"),
    ("ranking not created", "ranking_surface_created", "RANKING_SURFACE_CREATED"),
    ("source transfer not created", "source_transfer_occurred", "SOURCE_TRANSFER_OCCURRED"),
    ("source receipt not created", "source_receipt_occurred", "SOURCE_RECEIPT_OCCURRED"),
    (
        "reception authorization not created",
        "reception_authorization_created",
        "RECEPTION_AUTHORIZATION_CREATED",
    ),
    ("source not created", "source_created", "SOURCE_CREATED"),
    ("authority not created", "authority_created", "AUTHORITY_CREATED"),
    ("currentness not created", "currentness_created", "CURRENTNESS_CREATED"),
    ("truth not created", "truth_created", "TRUTH_CREATED"),
    ("action not created", "action_created", "ACTION_CREATED"),
    ("synchronization not created", "synchronization_created", "SYNCHRONIZATION_CREATED"),
    (
        "participation not authorized",
        "participation_authorized",
        "PARTICIPATION_AUTHORIZED",
    ),
    (
        "participant role not created",
        "participant_role_created",
        "PARTICIPANT_ROLE_CREATED",
    ),
    (
        "runtime permission not created",
        "runtime_permission_created",
        "RUNTIME_PERMISSION_CREATED",
    ),
    ("public API not created", "public_api_created", "PUBLIC_API_CREATED"),
    (
        "participant-facing interface not created",
        "participant_facing_interface_created",
        "PARTICIPANT_FACING_INTERFACE_CREATED",
    ),
    (
        "distributed network behavior not created",
        "distributed_network_behavior_created",
        "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    ),
    ("deployment not created", "deployment_created", "DEPLOYMENT_CREATED"),
    ("public release not created", "public_release_created", "PUBLIC_RELEASE_CREATED"),
    (
        "operation permission not created",
        "operation_permission_created",
        "OPERATION_PERMISSION_CREATED",
    ),
    (
        "broader reusable permission not created",
        "broader_reusable_permission_created",
        "BROADER_REUSABLE_PERMISSION_CREATED",
    ),
    (
        "follow-on work not authorized",
        "follow_on_work_authorized",
        "FOLLOW_ON_WORK_AUTHORIZED",
    ),
    (
        "artifact existence not request authority",
        "artifact_existence_treated_as_request_authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_REQUEST_AUTHORITY",
    ),
    (
        "latest file posture not request authority",
        "latest_file_posture_treated_as_request_authority",
        "LATEST_FILE_POSTURE_TREATED_AS_REQUEST_AUTHORITY",
    ),
    (
        "repo-local availability not request authority",
        "repo_local_availability_treated_as_request_authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_REQUEST_AUTHORITY",
    ),
    (
        "hidden repo state not request content",
        "hidden_repo_state_used_as_request_content",
        "HIDDEN_REPO_STATE_USED_AS_REQUEST_CONTENT",
    ),
    (
        "hidden repo state not request authority",
        "hidden_repo_state_used_as_request_authority",
        "HIDDEN_REPO_STATE_USED_AS_REQUEST_AUTHORITY",
    ),
    (
        "consumed request remains closed",
        "consumed_request_reopened",
        "CONSUMED_REQUEST_REOPENED",
    ),
    (
        "authorization token not reused",
        "authorization_token_reused",
        "AUTHORIZATION_TOKEN_REUSED",
    ),
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _canonical_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _is_sensitive_content_key(key: str | None) -> bool:
    if key is None:
        return False
    normalized = str(key).lower()
    return normalized in SENSITIVE_CONTENT_KEYS or normalized.endswith("_body")


def _contains_raw_sentinel(value: str) -> bool:
    return any(sentinel in value for sentinel in RAW_SENTINELS)


def _sanitize(value: Any, key: str | None = None) -> Any:
    if _is_sensitive_content_key(key):
        return "[REDACTED_BOUNDED_CONTENT]"
    if isinstance(value, Mapping):
        return {
            str(item_key): _sanitize(item_value, str(item_key))
            for item_key, item_value in value.items()
        }
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    if isinstance(value, str) and _contains_raw_sentinel(value):
        return "[REDACTED_BOUNDED_CONTENT]"
    return value


def _as_mapping(value: Any) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _read_json_path(path_value: Any) -> tuple[Any, bool, bool, str | None]:
    if not path_value:
        return None, False, False, "path missing"
    try:
        path = Path(str(path_value))
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        return None, False, False, f"unreadable JSON artifact: {exc}"
    except json.JSONDecodeError as exc:
        return None, False, False, f"malformed JSON artifact: {exc}"
    if not isinstance(parsed, Mapping):
        return parsed, True, False, "JSON artifact is not an object"
    return parsed, True, True, None


def _check(
    check_name: str,
    passed: bool,
    expected_posture: Any,
    actual_posture: Any,
    block_code: str,
) -> dict[str, Any]:
    code = None if passed else block_code
    return {
        "check_name": check_name,
        "passed": bool(passed),
        "expected_posture": _sanitize(expected_posture),
        "actual_posture": _sanitize(actual_posture),
        "block_code": code,
        "failure_code": code,
    }


def _failed_checks(checks: list[Mapping[str, Any]]) -> list[Mapping[str, Any]]:
    return [check for check in checks if check.get("passed") is not True]


def _first_failed_code(checks: list[Mapping[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is not True:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _count_passed(checks: list[Mapping[str, Any]]) -> int:
    return sum(1 for check in checks if check.get("passed") is True)


def _extract_index_entry_facts(
    index_entry_artifact: Mapping[str, Any],
    selected_index_entry_path: str | None,
) -> dict[str, Any]:
    metadata = _as_mapping(
        index_entry_artifact.get("local_relevance_orientation_index_entry_metadata")
    )
    summary = _as_mapping(
        index_entry_artifact.get("local_relevance_orientation_index_entry_summary")
    )
    index_entry = _as_mapping(index_entry_artifact.get("index_entry"))

    failed_count = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        index_entry_artifact.get("failed_check_count"),
    )

    return {
        "basis_index_entry_artifact": selected_index_entry_path,
        "index_entry_artifact_outcome": _first_present(
            index_entry_artifact.get("outcome"),
            summary.get("outcome"),
        ),
        "index_entry_artifact_result_version": _first_present(
            metadata.get("local_relevance_orientation_index_entry_version"),
            metadata.get("result_version"),
            summary.get("result_version"),
            index_entry_artifact.get("result_version"),
            index_entry.get("index_entry_version"),
        ),
        "index_entry_artifact_failed_check_count": failed_count,
        "index_entry_present": isinstance(index_entry_artifact.get("index_entry"), Mapping),
        "index_entry_type": index_entry.get("index_entry_type"),
        "index_entry_scope": index_entry.get("index_entry_scope"),
        "existing_orientation_view_artifact": index_entry.get("orientation_view_artifact"),
        "existing_source_receipt_artifact": index_entry.get("source_receipt_artifact"),
        "existing_referenced_reception_artifact": index_entry.get(
            "referenced_reception_artifact"
        ),
        "existing_received_signal_id": index_entry.get("received_signal_id"),
        "existing_received_relevance_basis_id": index_entry.get(
            "received_relevance_basis_id"
        ),
        "existing_received_relevance_scope_id": index_entry.get(
            "received_relevance_scope_id"
        ),
        "existing_received_carrier_context_id": index_entry.get(
            "received_carrier_context_id"
        ),
        "existing_received_reception_envelope_id": index_entry.get(
            "received_reception_envelope_id"
        ),
    }


def _facts_are_sufficient(facts: Mapping[str, Any]) -> bool:
    return all(
        facts.get(key)
        for key in (
            "basis_index_entry_artifact",
            "existing_orientation_view_artifact",
            "existing_source_receipt_artifact",
            "existing_referenced_reception_artifact",
            "existing_received_signal_id",
            "existing_received_relevance_basis_id",
            "existing_received_relevance_scope_id",
            "existing_received_carrier_context_id",
            "existing_received_reception_envelope_id",
        )
    )


def _build_successor_reception_request_object(
    facts: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "request_id": "local_relevance_medium_successor_reception_request_001",
        "request_type": REQUEST_TYPE,
        "request_version": RESULT_VERSION,
        "request_scope": REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
        "basis_index_entry_artifact": facts.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": facts.get(
            "existing_orientation_view_artifact"
        ),
        "existing_source_receipt_artifact": facts.get(
            "existing_source_receipt_artifact"
        ),
        "existing_referenced_reception_artifact": facts.get(
            "existing_referenced_reception_artifact"
        ),
        "existing_received_signal_id": facts.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": facts.get(
            "existing_received_relevance_basis_id"
        ),
        "existing_received_relevance_scope_id": facts.get(
            "existing_received_relevance_scope_id"
        ),
        "existing_received_carrier_context_id": facts.get(
            "existing_received_carrier_context_id"
        ),
        "existing_received_reception_envelope_id": facts.get(
            "existing_received_reception_envelope_id"
        ),
        "successor_candidate_id": request.get("successor_candidate_id"),
        "successor_candidate_scope": SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
        "multiplicity_purpose": MULTIPLICITY_PURPOSE_LOCAL_ONLY,
        "max_local_orientation_objects_after_successor": 2,
        "second_reception_created": False,
        "successor_candidate_admitted": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "relation_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
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


def _declared_non_claims_false(request: Mapping[str, Any]) -> tuple[bool, dict[str, Any]]:
    declared = request.get("declared_non_claims")
    if not isinstance(declared, Mapping):
        return False, {
            "declared_non_claims_present": False,
            "missing_keys": list(REQUIRED_FALSE_NON_CLAIMS),
            "flipped_or_invalid_keys": [],
        }

    missing = [key for key in REQUIRED_FALSE_NON_CLAIMS if key not in declared]
    flipped = [
        key
        for key in REQUIRED_FALSE_NON_CLAIMS
        if key in declared and declared.get(key) is not False
    ]
    return not missing and not flipped, {
        "declared_non_claims_present": True,
        "missing_keys": missing,
        "flipped_or_invalid_keys": flipped,
    }


def _predecessor_failure_evidence_preserved(
    request: Mapping[str, Any],
) -> tuple[bool, dict[str, bool]]:
    posture = {
        "predecessor_failure_repaired": request.get("predecessor_failure_repaired")
        is True,
        "predecessor_failure_hidden": request.get("predecessor_failure_hidden") is True,
        "predecessor_failure_claimed_passed": request.get(
            "predecessor_failure_claimed_passed"
        )
        is True,
    }
    return not any(posture.values()), posture


def _build_checks(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    artifact_readable: bool,
    artifact_is_json_object: bool,
    read_error: str | None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    question = request.get("local_relevance_medium_successor_reception_question")
    intent = request.get("local_relevance_medium_successor_reception_intent")
    artifact_path = request.get("selected_local_relevance_orientation_index_entry_artifact")
    request_type = request.get("request_type")
    request_scope = request.get("request_scope")
    candidate_id = request.get("successor_candidate_id")
    candidate_scope = request.get("successor_candidate_scope")
    multiplicity_purpose = request.get("multiplicity_purpose")
    max_objects = request.get("max_local_orientation_objects_after_successor")

    checks.append(
        _check(
            "request question declared",
            bool(question),
            "declared local relevance medium successor reception request question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            list(SUPPORTED_INTENTS),
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block intent not requested",
            intent != INTENT_BLOCK,
            "intent is not block request",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_BLOCK_REQUESTED",
        )
    )

    artifact_missing = (
        request.get("selected_local_relevance_orientation_index_entry_artifact_missing")
        is True
    )
    checks.append(
        _check(
            "selected local relevance orientation index entry artifact path declared",
            bool(artifact_path) and not artifact_missing,
            "declared local relevance orientation index entry artifact path",
            artifact_path,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected local relevance orientation index entry artifact readable JSON",
            artifact_readable and not artifact_missing,
            "readable JSON artifact",
            read_error or artifact_readable,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "selected local relevance orientation index entry artifact JSON object",
            artifact_is_json_object,
            "JSON object artifact",
            artifact_is_json_object,
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "index entry artifact outcome recorded",
            facts.get("index_entry_artifact_outcome") == INDEX_ENTRY_OUTCOME_RECORDED
            and request.get(
                "selected_local_relevance_orientation_index_entry_artifact_not_recorded"
            )
            is not True,
            INDEX_ENTRY_OUTCOME_RECORDED,
            facts.get("index_entry_artifact_outcome"),
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "index entry artifact result version 0.1.0",
            facts.get("index_entry_artifact_result_version") == INDEX_ENTRY_RESULT_VERSION
            and request.get(
                "selected_local_relevance_orientation_index_entry_artifact_version_not_0_1_0"
            )
            is not True,
            INDEX_ENTRY_RESULT_VERSION,
            facts.get("index_entry_artifact_result_version"),
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "index entry artifact failed check count zero",
            facts.get("index_entry_artifact_failed_check_count") == 0
            and request.get(
                "selected_local_relevance_orientation_index_entry_artifact_failed_checks_present"
            )
            is not True,
            0,
            facts.get("index_entry_artifact_failed_check_count"),
            "LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "index entry present",
            facts.get("index_entry_present") is True
            and request.get("index_entry_missing") is not True,
            "one index entry object",
            facts.get("index_entry_present"),
            "INDEX_ENTRY_MISSING",
        )
    )
    checks.append(
        _check(
            "index entry type exact",
            facts.get("index_entry_type") == INDEX_ENTRY_TYPE
            and request.get("index_entry_type_not_local_relevance_orientation_index_entry")
            is not True,
            INDEX_ENTRY_TYPE,
            facts.get("index_entry_type"),
            "INDEX_ENTRY_TYPE_NOT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY",
        )
    )
    checks.append(
        _check(
            "index entry scope local only",
            facts.get("index_entry_scope") == INDEX_ENTRY_SCOPE_LOCAL_ONLY
            and request.get("index_entry_scope_not_local_only") is not True,
            INDEX_ENTRY_SCOPE_LOCAL_ONLY,
            facts.get("index_entry_scope"),
            "INDEX_ENTRY_SCOPE_NOT_LOCAL_ONLY",
        )
    )

    basis_checks = (
        (
            "existing orientation view artifact present",
            "existing_orientation_view_artifact",
            "existing_orientation_view_artifact_missing",
            "EXISTING_ORIENTATION_VIEW_ARTIFACT_MISSING",
        ),
        (
            "existing source receipt artifact present",
            "existing_source_receipt_artifact",
            "existing_source_receipt_artifact_missing",
            "EXISTING_SOURCE_RECEIPT_ARTIFACT_MISSING",
        ),
        (
            "existing referenced reception artifact present",
            "existing_referenced_reception_artifact",
            "existing_referenced_reception_artifact_missing",
            "EXISTING_REFERENCED_RECEPTION_ARTIFACT_MISSING",
        ),
        (
            "existing received signal id present",
            "existing_received_signal_id",
            "existing_received_signal_id_missing",
            "EXISTING_RECEIVED_SIGNAL_ID_MISSING",
        ),
        (
            "existing received relevance basis id present",
            "existing_received_relevance_basis_id",
            "existing_received_relevance_basis_id_missing",
            "EXISTING_RECEIVED_RELEVANCE_BASIS_ID_MISSING",
        ),
        (
            "existing received relevance scope id present",
            "existing_received_relevance_scope_id",
            "existing_received_relevance_scope_id_missing",
            "EXISTING_RECEIVED_RELEVANCE_SCOPE_ID_MISSING",
        ),
        (
            "existing received carrier context id present",
            "existing_received_carrier_context_id",
            "existing_received_carrier_context_id_missing",
            "EXISTING_RECEIVED_CARRIER_CONTEXT_ID_MISSING",
        ),
        (
            "existing received reception envelope id present",
            "existing_received_reception_envelope_id",
            "existing_received_reception_envelope_id_missing",
            "EXISTING_RECEIVED_RECEPTION_ENVELOPE_ID_MISSING",
        ),
    )
    for check_name, fact_key, shortcut_key, block_code in basis_checks:
        checks.append(
            _check(
                check_name,
                bool(facts.get(fact_key)) and request.get(shortcut_key) is not True,
                "present",
                facts.get(fact_key),
                block_code,
            )
        )

    checks.append(
        _check(
            "successor candidate id declared",
            bool(candidate_id) and request.get("successor_candidate_id_missing") is not True,
            "declared successor candidate id",
            candidate_id,
            "SUCCESSOR_CANDIDATE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "successor candidate differs from existing signal",
            bool(candidate_id)
            and bool(facts.get("existing_received_signal_id"))
            and candidate_id != facts.get("existing_received_signal_id")
            and request.get("successor_candidate_id_equals_existing_signal") is not True,
            "successor candidate differs from existing received signal id",
            {
                "successor_candidate_id": candidate_id,
                "existing_received_signal_id": facts.get("existing_received_signal_id"),
            },
            "SUCCESSOR_CANDIDATE_ID_EQUALS_EXISTING_SIGNAL",
        )
    )
    checks.append(
        _check(
            "successor candidate scope declared",
            bool(candidate_scope),
            SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
            candidate_scope,
            "SUCCESSOR_CANDIDATE_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "successor candidate scope bounded only",
            candidate_scope == SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
            SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
            candidate_scope,
            "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY",
        )
    )
    checks.append(
        _check(
            "request scope declared",
            bool(request_scope),
            REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
            request_scope,
            "REQUEST_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "request scope one successor only",
            request_scope == REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
            REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
            request_scope,
            "REQUEST_SCOPE_NOT_ONE_SUCCESSOR_ONLY",
        )
    )
    checks.append(
        _check(
            "request type declared",
            bool(request_type),
            REQUEST_TYPE,
            request_type,
            "REQUEST_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "request type exact",
            request_type == REQUEST_TYPE,
            REQUEST_TYPE,
            request_type,
            "REQUEST_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST",
        )
    )
    checks.append(
        _check(
            "multiplicity purpose declared",
            bool(multiplicity_purpose),
            MULTIPLICITY_PURPOSE_LOCAL_ONLY,
            multiplicity_purpose,
            "MULTIPLICITY_PURPOSE_MISSING",
        )
    )
    checks.append(
        _check(
            "multiplicity purpose local only",
            multiplicity_purpose == MULTIPLICITY_PURPOSE_LOCAL_ONLY,
            MULTIPLICITY_PURPOSE_LOCAL_ONLY,
            multiplicity_purpose,
            "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
        )
    )
    checks.append(
        _check(
            "max local orientation objects after successor is two",
            max_objects == 2,
            2,
            max_objects,
            "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_SUCCESSOR_NOT_TWO",
        )
    )

    for check_name, field_name, block_code in BOOLEAN_OVERREACH_CHECKS:
        actual = request.get(field_name, False)
        checks.append(
            _check(
                check_name,
                actual is False,
                False,
                actual,
                block_code,
            )
        )

    predecessor_preserved, predecessor_actual = _predecessor_failure_evidence_preserved(
        request
    )
    checks.append(
        _check(
            "predecessor failure evidence preserved",
            predecessor_preserved,
            {
                "predecessor_failure_repaired": False,
                "predecessor_failure_hidden": False,
                "predecessor_failure_claimed_passed": False,
            },
            predecessor_actual,
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )

    canonical_false = all(value is False for value in _canonical_non_claims().values())
    checks.append(
        _check(
            "result-level required false non-claims canonical false",
            canonical_false,
            "all result-level required false non-claims are false",
            canonical_false,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    declared_non_claims_ok, declared_non_claims_actual = _declared_non_claims_false(
        request
    )
    checks.append(
        _check(
            "required non-claims false",
            declared_non_claims_ok,
            "all declared required non-claims present and false",
            declared_non_claims_actual,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )

    return checks


def _determine_outcome(request: Mapping[str, Any], checks: list[Mapping[str, Any]]) -> str:
    if _failed_checks(checks):
        return OUTCOME_BLOCKED

    requested_outcome = request.get(
        "requested_local_relevance_medium_successor_reception_request_outcome"
    )
    if requested_outcome in OUTCOME_FAMILY and requested_outcome != OUTCOME_BLOCKED:
        return str(requested_outcome)

    intent = request.get("local_relevance_medium_successor_reception_intent")
    if intent == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED
    return OUTCOME_RECORDED


def _build_block(
    outcome: str,
    checks: list[Mapping[str, Any]],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    if outcome != OUTCOME_BLOCKED:
        return {
            "blocked": False,
            "code": None,
            "block_code": None,
            "reason": None,
        }

    code = _first_failed_code(checks) or (
        "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_MALFORMED"
    )
    return {
        "blocked": True,
        "code": code,
        "block_code": code,
        "reason": _sanitize(request.get("block_reason") or code),
        "failed_check_codes": [
            check.get("block_code") or check.get("failure_code")
            for check in _failed_checks(checks)
            if check.get("block_code") or check.get("failure_code")
        ],
    }


def _build_statement(
    outcome: str,
    request_object: Mapping[str, Any],
) -> dict[str, bool]:
    recorded = outcome == OUTCOME_RECORDED
    return {
        "local_relevance_medium_successor_reception_request_recorded": recorded,
        "basis_index_entry_artifact_preserved": recorded
        and bool(request_object.get("basis_index_entry_artifact")),
        "existing_orientation_view_artifact_preserved": recorded
        and bool(request_object.get("existing_orientation_view_artifact")),
        "existing_source_receipt_artifact_preserved": recorded
        and bool(request_object.get("existing_source_receipt_artifact")),
        "existing_referenced_reception_artifact_preserved": recorded
        and bool(request_object.get("existing_referenced_reception_artifact")),
        "existing_received_signal_id_preserved": recorded
        and bool(request_object.get("existing_received_signal_id")),
        "existing_received_relevance_basis_id_preserved": recorded
        and bool(request_object.get("existing_received_relevance_basis_id")),
        "existing_received_relevance_scope_id_preserved": recorded
        and bool(request_object.get("existing_received_relevance_scope_id")),
        "existing_received_carrier_context_id_preserved": recorded
        and bool(request_object.get("existing_received_carrier_context_id")),
        "existing_received_reception_envelope_id_preserved": recorded
        and bool(request_object.get("existing_received_reception_envelope_id")),
        "successor_candidate_id_declared": recorded
        and bool(request_object.get("successor_candidate_id")),
        "successor_candidate_differs_from_existing_signal": recorded
        and bool(request_object.get("successor_candidate_id"))
        and request_object.get("successor_candidate_id")
        != request_object.get("existing_received_signal_id"),
        "successor_candidate_scope_bounded_only": recorded
        and request_object.get("successor_candidate_scope")
        == SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
        "request_scope_one_successor_only": recorded
        and request_object.get("request_scope") == REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
        "multiplicity_purpose_local_only": recorded
        and request_object.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE_LOCAL_ONLY,
        "max_local_orientation_objects_after_successor_is_two": recorded
        and request_object.get("max_local_orientation_objects_after_successor") == 2,
        "result_level_non_claims_canonical_false": True,
    }


def _build_non_meaning() -> dict[str, bool]:
    return {
        "request_is_second_reception": False,
        "request_is_successor_admission": False,
        "request_is_repeated_reception_permission": False,
        "request_is_arbitrary_reception": False,
        "request_is_feed": False,
        "request_is_relation_view": False,
        "request_is_index_system": False,
        "request_is_registry": False,
        "request_is_search": False,
        "request_is_ranking": False,
        "request_is_source_transfer": False,
        "request_is_source_receipt": False,
        "request_is_reception_authorization": False,
        "request_is_authority": False,
        "request_is_currentness": False,
        "request_is_truth": False,
        "request_is_action": False,
        "request_is_synchronization": False,
        "request_is_participation_authorization": False,
        "request_is_participant_role": False,
        "request_is_runtime_permission": False,
        "request_is_public_api": False,
        "request_is_participant_facing_interface": False,
        "request_is_distributed_network_behavior": False,
        "request_is_operation_permission": False,
        "request_is_follow_on_work": False,
    }


def _build_what_remains_open() -> list[str]:
    return [
        "local relevance medium successor reception request resolver successor work",
        "local relevance medium successor reception request test",
        "local relevance medium successor reception request live artifact",
        "local relevance medium successor reception request terminal summary, if needed",
        "second bounded relevance reception",
        "successor candidate admission",
        "local medium multiplicity result",
        "relation view",
        "comparison view",
        "local relevance orientation index system, if ever separately selected",
        "registry",
        "search surface",
        "ranking surface",
        "source transfer",
        "source receipt",
        "reception authorization",
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
        "successor reception request reuse",
        "follow-on work",
    ]


def _additional_basis_required(
    outcome: str,
    request: Mapping[str, Any],
) -> list[Any]:
    if outcome != OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return []
    basis = request.get("additional_basis_context")
    if basis is None:
        return ["additional successor reception request basis required"]
    if isinstance(basis, list):
        return _sanitize(basis)
    return [_sanitize(basis)]


def _not_recorded_basis(outcome: str, request: Mapping[str, Any]) -> list[Any]:
    if outcome != OUTCOME_NOT_RECORDED:
        return []
    basis = request.get("not_recorded_basis")
    if basis is None:
        return ["local relevance medium successor reception request not recorded"]
    if isinstance(basis, list):
        return _sanitize(basis)
    return [_sanitize(basis)]


def _build_selected_artifact_basis(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    artifact_readable: bool,
    artifact_is_json_object: bool,
    read_error: str | None,
) -> dict[str, Any]:
    return {
        "selected_local_relevance_orientation_index_entry_artifact": _sanitize(
            request.get("selected_local_relevance_orientation_index_entry_artifact")
        ),
        "artifact_readable": bool(artifact_readable),
        "artifact_is_json_object": bool(artifact_is_json_object),
        "read_error": _sanitize(read_error),
        "index_entry_artifact_outcome": facts.get("index_entry_artifact_outcome"),
        "index_entry_artifact_result_version": facts.get(
            "index_entry_artifact_result_version"
        ),
        "index_entry_artifact_failed_check_count": facts.get(
            "index_entry_artifact_failed_check_count"
        ),
        "index_entry_present": bool(facts.get("index_entry_present")),
        "index_entry_type": facts.get("index_entry_type"),
        "index_entry_scope": facts.get("index_entry_scope"),
        "existing_orientation_view_artifact": facts.get(
            "existing_orientation_view_artifact"
        ),
        "existing_source_receipt_artifact": facts.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": facts.get(
            "existing_referenced_reception_artifact"
        ),
        "existing_received_signal_id": facts.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": facts.get(
            "existing_received_relevance_basis_id"
        ),
        "existing_received_relevance_scope_id": facts.get(
            "existing_received_relevance_scope_id"
        ),
        "existing_received_carrier_context_id": facts.get(
            "existing_received_carrier_context_id"
        ),
        "existing_received_reception_envelope_id": facts.get(
            "existing_received_reception_envelope_id"
        ),
        "artifact_existence_is_request_authority": False,
        "latest_file_posture_is_request_authority": False,
        "repo_local_availability_is_request_authority": False,
        "hidden_repo_state_used": False,
    }


def build_local_relevance_medium_successor_reception_request_v0_min_summary(
    result: Mapping[str, Any],
) -> dict[str, Any]:
    checks = list(
        result.get("local_relevance_medium_successor_reception_request_checks", [])
    )
    metadata = _as_mapping(
        result.get("local_relevance_medium_successor_reception_request_metadata")
    )
    statement = _as_mapping(
        result.get("local_relevance_medium_successor_reception_request_statement")
    )
    request_object = _as_mapping(result.get("successor_reception_request_object"))
    non_claims = _as_mapping(result.get("non_claims"))
    block = result.get("block")
    block_mapping = _as_mapping(block)

    summary = {
        "outcome": result.get("outcome"),
        "block_code": block_mapping.get("code") or block_mapping.get("block_code"),
        "block_reason": block_mapping.get("reason"),
        "request_id": metadata.get(
            "local_relevance_medium_successor_reception_request_id"
        ),
        "question": result.get(
            "declared_local_relevance_medium_successor_reception_question"
        ),
        "intent": metadata.get("local_relevance_medium_successor_reception_intent"),
        "passed_check_count": _count_passed(checks),
        "failed_check_count": len(_failed_checks(checks)),
        "result_version": metadata.get(
            "local_relevance_medium_successor_reception_request_version",
            RESULT_VERSION,
        ),
        "resolver_module": metadata.get("resolver_module", RESOLVER_MODULE),
        "local_relevance_medium_successor_reception_request_recorded": (
            statement.get(
                "local_relevance_medium_successor_reception_request_recorded",
                False,
            )
        ),
        "request_recorded": statement.get(
            "local_relevance_medium_successor_reception_request_recorded", False
        ),
        "basis_index_entry_artifact_preserved": statement.get(
            "basis_index_entry_artifact_preserved", False
        ),
        "existing_orientation_view_artifact_preserved": statement.get(
            "existing_orientation_view_artifact_preserved", False
        ),
        "existing_source_receipt_artifact_preserved": statement.get(
            "existing_source_receipt_artifact_preserved", False
        ),
        "existing_referenced_reception_artifact_preserved": statement.get(
            "existing_referenced_reception_artifact_preserved", False
        ),
        "existing_received_signal_id_preserved": statement.get(
            "existing_received_signal_id_preserved", False
        ),
        "existing_received_relevance_basis_id_preserved": statement.get(
            "existing_received_relevance_basis_id_preserved", False
        ),
        "existing_received_relevance_scope_id_preserved": statement.get(
            "existing_received_relevance_scope_id_preserved", False
        ),
        "existing_received_carrier_context_id_preserved": statement.get(
            "existing_received_carrier_context_id_preserved", False
        ),
        "existing_received_reception_envelope_id_preserved": statement.get(
            "existing_received_reception_envelope_id_preserved", False
        ),
        "successor_candidate_id_declared": statement.get(
            "successor_candidate_id_declared", False
        ),
        "successor_candidate_differs_from_existing_signal": statement.get(
            "successor_candidate_differs_from_existing_signal", False
        ),
        "successor_candidate_scope_bounded_only": statement.get(
            "successor_candidate_scope_bounded_only", False
        ),
        "request_scope_one_successor_only": statement.get(
            "request_scope_one_successor_only", False
        ),
        "multiplicity_purpose_local_only": statement.get(
            "multiplicity_purpose_local_only", False
        ),
        "max_local_orientation_objects_after_successor_is_two": statement.get(
            "max_local_orientation_objects_after_successor_is_two", False
        ),
        "request_object_summary": {
            key: request_object.get(key)
            for key in (
                "request_type",
                "request_scope",
                "basis_index_entry_artifact",
                "existing_orientation_view_artifact",
                "existing_received_signal_id",
                "successor_candidate_id",
                "successor_candidate_scope",
                "multiplicity_purpose",
                "max_local_orientation_objects_after_successor",
            )
        },
        "second_reception_not_created": non_claims.get("second_reception_created")
        is False,
        "successor_admission_not_created": non_claims.get(
            "successor_candidate_admitted"
        )
        is False,
        "repeated_reception_permission_not_created": non_claims.get(
            "repeated_reception_permission_created"
        )
        is False,
        "arbitrary_reception_not_created": non_claims.get(
            "arbitrary_reception_created"
        )
        is False,
        "feed_not_created": non_claims.get("feed_created") is False,
        "relation_view_not_created": non_claims.get("relation_view_created") is False,
        "index_system_not_created": non_claims.get("index_system_created") is False,
        "registry_not_created": non_claims.get("registry_created") is False,
        "search_not_created": non_claims.get("search_surface_created") is False,
        "ranking_not_created": non_claims.get("ranking_surface_created") is False,
        "source_not_created": non_claims.get("source_created") is False,
        "authority_not_created": non_claims.get("authority_created") is False,
        "currentness_not_created": non_claims.get("currentness_created") is False,
        "truth_not_created": non_claims.get("truth_created") is False,
        "action_not_created": non_claims.get("action_created") is False,
        "synchronization_not_created": non_claims.get("synchronization_created")
        is False,
        "participation_authorization_not_created": non_claims.get(
            "participation_authorized"
        )
        is False,
        "participant_role_not_created": non_claims.get("participant_role_created")
        is False,
        "runtime_permission_not_created": non_claims.get("runtime_permission_created")
        is False,
        "public_api_not_created": non_claims.get("public_api_created") is False,
        "participant_facing_interface_not_created": non_claims.get(
            "participant_facing_interface_created"
        )
        is False,
        "distributed_network_behavior_not_created": non_claims.get(
            "distributed_network_behavior_created"
        )
        is False,
        "operation_permission_not_created": non_claims.get(
            "operation_permission_created"
        )
        is False,
        "follow_on_not_authorized": non_claims.get("follow_on_work_authorized")
        is False,
        "key_non_claims": {
            key: non_claims.get(key)
            for key in (
                "second_reception_created",
                "successor_candidate_admitted",
                "feed_created",
                "relation_view_created",
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "authority_created",
                "currentness_created",
                "truth_created",
                "action_created",
                "synchronization_created",
                "runtime_permission_created",
                "public_api_created",
                "distributed_network_behavior_created",
                "follow_on_work_authorized",
            )
        },
        "predecessor_failure_evidence_preserved": non_claims.get(
            "predecessor_failure_repaired"
        )
        is False
        and non_claims.get("predecessor_failure_hidden") is False
        and non_claims.get("predecessor_failure_claimed_passed") is False,
        "result_level_non_claims_canonical_false": statement.get(
            "result_level_non_claims_canonical_false", False
        )
        and all(non_claims.get(key) is False for key in REQUIRED_FALSE_NON_CLAIMS),
    }
    return _sanitize(summary)


def _build_result(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    request_object: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    artifact_readable: bool,
    artifact_is_json_object: bool,
    read_error: str | None,
) -> dict[str, Any]:
    block = _build_block(outcome, checks, request)
    metadata = {
        "local_relevance_medium_successor_reception_request_id": request.get(
            "local_relevance_medium_successor_reception_request_id"
        ),
        "local_relevance_medium_successor_reception_request_type": (
            "local_relevance_medium_successor_reception_request_result"
        ),
        "local_relevance_medium_successor_reception_request_version": RESULT_VERSION,
        "local_relevance_medium_successor_reception_intent": request.get(
            "local_relevance_medium_successor_reception_intent"
        ),
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": _count_passed(checks),
        "failed_check_count": len(_failed_checks(checks)),
    }

    result: dict[str, Any] = {
        "local_relevance_medium_successor_reception_request_metadata": metadata,
        "declared_local_relevance_medium_successor_reception_question": _sanitize(
            request.get("local_relevance_medium_successor_reception_question")
        ),
        "selected_local_relevance_orientation_index_entry_artifact_basis": (
            _build_selected_artifact_basis(
                request,
                facts,
                artifact_readable,
                artifact_is_json_object,
                read_error,
            )
        ),
        "successor_reception_request_object": {
            key: _sanitize(request_object.get(key)) for key in REQUEST_OBJECT_FIELDS
        }
        if request_object
        else {},
        "local_relevance_medium_successor_reception_request_checks": checks,
        "local_relevance_medium_successor_reception_request_statement": (
            _build_statement(outcome, request_object)
        ),
        "local_relevance_medium_successor_reception_request_non_meaning": (
            _build_non_meaning()
        ),
        "additional_basis_required": _additional_basis_required(outcome, request),
        "not_recorded_basis": _not_recorded_basis(outcome, request),
        "what_remains_open": _build_what_remains_open(),
        "non_claims": _canonical_non_claims(),
        "outcome": outcome,
        "block": block,
        "local_relevance_medium_successor_reception_request_summary": {},
    }
    result["local_relevance_medium_successor_reception_request_summary"] = (
        build_local_relevance_medium_successor_reception_request_v0_min_summary(result)
    )
    return _sanitize(result)


def _malformed_request_result(actual_request: Any) -> dict[str, Any]:
    request = {
        "local_relevance_medium_successor_reception_request_id": (
            "malformed_local_relevance_medium_successor_reception_request"
        ),
        "local_relevance_medium_successor_reception_question": None,
        "local_relevance_medium_successor_reception_intent": None,
        "selected_local_relevance_orientation_index_entry_artifact": None,
        "declared_non_claims": {},
    }
    checks = [
        _check(
            "declared local relevance medium successor reception request mapping",
            False,
            "mapping request",
            type(actual_request).__name__,
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_MALFORMED",
        )
    ]
    return _build_result(
        request=request,
        facts={},
        request_object={},
        checks=checks,
        outcome=OUTCOME_BLOCKED,
        artifact_readable=False,
        artifact_is_json_object=False,
        read_error="declared request is not a mapping",
    )


def resolve_local_relevance_medium_successor_reception_request_v0_min(
    declared_local_relevance_medium_successor_reception_request: Mapping[str, Any]
    | None = None,
) -> dict:
    if declared_local_relevance_medium_successor_reception_request is None:
        declared_local_relevance_medium_successor_reception_request = (
            build_declared_local_relevance_medium_successor_reception_request_v0_min_request()
        )

    if not isinstance(declared_local_relevance_medium_successor_reception_request, Mapping):
        return _malformed_request_result(
            declared_local_relevance_medium_successor_reception_request
        )

    request = copy.deepcopy(
        dict(declared_local_relevance_medium_successor_reception_request)
    )
    selected_path = request.get("selected_local_relevance_orientation_index_entry_artifact")

    artifact_data: Any = None
    artifact_readable = False
    artifact_is_json_object = False
    read_error: str | None = None
    if selected_path and request.get(
        "selected_local_relevance_orientation_index_entry_artifact_missing"
    ) is not True:
        artifact_data, artifact_readable, artifact_is_json_object, read_error = (
            _read_json_path(selected_path)
        )
    elif not selected_path:
        read_error = "path missing"

    facts: dict[str, Any] = {}
    if isinstance(artifact_data, Mapping):
        facts = _extract_index_entry_facts(artifact_data, str(selected_path))

    checks = _build_checks(
        request,
        facts,
        artifact_readable,
        artifact_is_json_object,
        read_error,
    )
    outcome = _determine_outcome(request, checks)

    request_object: dict[str, Any] = {}
    request_shape_supported = (
        request.get("request_type") == REQUEST_TYPE
        and request.get("request_scope") == REQUEST_SCOPE_ONE_SUCCESSOR_ONLY
        and request.get("successor_candidate_scope")
        == SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY
        and request.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE_LOCAL_ONLY
        and request.get("max_local_orientation_objects_after_successor") == 2
        and bool(request.get("successor_candidate_id"))
        and request.get("successor_candidate_id")
        != facts.get("existing_received_signal_id")
    )
    if _facts_are_sufficient(facts) and request_shape_supported:
        request_object = _build_successor_reception_request_object(facts, request)

    return _build_result(
        request=request,
        facts=facts,
        request_object=request_object,
        checks=checks,
        outcome=outcome,
        artifact_readable=artifact_readable,
        artifact_is_json_object=artifact_is_json_object,
        read_error=read_error,
    )


def resolve_local_relevance_medium_successor_reception_request_v0_min_from_path(
    declared_local_relevance_medium_successor_reception_request_path: Path | str,
) -> dict:
    path = Path(declared_local_relevance_medium_successor_reception_request_path)
    try:
        parsed = json.loads(path.read_text(encoding="utf-8"))
    except OSError as exc:
        raise LocalRelevanceMediumSuccessorReceptionRequestV0MinError(
            f"declared request unreadable: {exc}"
        ) from exc
    except json.JSONDecodeError as exc:
        raise LocalRelevanceMediumSuccessorReceptionRequestV0MinError(
            f"declared request is not valid JSON: {exc}"
        ) from exc

    if not isinstance(parsed, Mapping):
        return _malformed_request_result(parsed)
    return resolve_local_relevance_medium_successor_reception_request_v0_min(parsed)


def _safe_filename_part(value: Any) -> str:
    raw = str(value or "local_relevance_medium_successor_reception_request_result")
    safe = "".join(ch if ch.isalnum() or ch in "._-" else "_" for ch in raw)
    return safe or "local_relevance_medium_successor_reception_request_result"


def _available_output_path(path: Path) -> Path:
    if not path.exists():
        return path
    for index in range(1, 10000):
        candidate = path.with_name(f"{path.stem}_{index:03d}{path.suffix}")
        if not candidate.exists():
            return candidate
    raise LocalRelevanceMediumSuccessorReceptionRequestV0MinError(
        f"could not allocate non-overwriting output path under {path.parent}"
    )


def write_local_relevance_medium_successor_reception_request_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    if not isinstance(result, Mapping):
        raise LocalRelevanceMediumSuccessorReceptionRequestV0MinError(
            "result must be a mapping"
        )

    if output_path is None:
        metadata = _as_mapping(
            result.get("local_relevance_medium_successor_reception_request_metadata")
        )
        request_id = _safe_filename_part(
            metadata.get("local_relevance_medium_successor_reception_request_id")
        )
        output_path = OUTPUT_ROOT / (
            f"{request_id}__"
            "local_relevance_medium_successor_reception_request_v0_min_result.json"
        )

    path = _available_output_path(Path(output_path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(_sanitize(dict(result)), indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return path


def build_declared_local_relevance_medium_successor_reception_request_v0_min_request(
    local_relevance_medium_successor_reception_request_id: str = (
        "local_relevance_medium_successor_reception_request_reference_review_001"
    ),
    local_relevance_medium_successor_reception_question: str = CORE_QUESTION,
    local_relevance_medium_successor_reception_intent: str = INTENT_RECORD,
    selected_local_relevance_orientation_index_entry_artifact: Path | str = (
        DEFAULT_LOCAL_RELEVANCE_ORIENTATION_INDEX_ENTRY_ARTIFACT
    ),
    request_scope: str = REQUEST_SCOPE_ONE_SUCCESSOR_ONLY,
    request_type: str = REQUEST_TYPE,
    successor_candidate_id: str = DEFAULT_SUCCESSOR_CANDIDATE_ID,
    successor_candidate_scope: str = SUCCESSOR_CANDIDATE_SCOPE_BOUNDED_ONLY,
    multiplicity_purpose: str = MULTIPLICITY_PURPOSE_LOCAL_ONLY,
    max_local_orientation_objects_after_successor: int = 2,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    non_claims = _canonical_non_claims()
    if declared_non_claims is not None:
        non_claims.update(copy.deepcopy(dict(declared_non_claims)))

    request: dict[str, Any] = {
        "local_relevance_medium_successor_reception_request_id": (
            local_relevance_medium_successor_reception_request_id
        ),
        "local_relevance_medium_successor_reception_question": (
            local_relevance_medium_successor_reception_question
        ),
        "local_relevance_medium_successor_reception_intent": (
            local_relevance_medium_successor_reception_intent
        ),
        "selected_local_relevance_orientation_index_entry_artifact": str(
            selected_local_relevance_orientation_index_entry_artifact
        ),
        "request_scope": request_scope,
        "request_type": request_type,
        "successor_candidate_id": successor_candidate_id,
        "successor_candidate_scope": successor_candidate_scope,
        "multiplicity_purpose": multiplicity_purpose,
        "max_local_orientation_objects_after_successor": (
            max_local_orientation_objects_after_successor
        ),
        "declared_non_claims": non_claims,
    }
    request.update(copy.deepcopy(overrides))
    return request
