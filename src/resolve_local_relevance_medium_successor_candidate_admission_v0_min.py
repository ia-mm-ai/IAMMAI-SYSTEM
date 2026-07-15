"""Resolve one local relevance medium successor candidate admission object.

This resolver reads one clean local relevance medium successor reception
request artifact and records one candidate-admission object only. It admits the
declared successor candidate as candidate only; it does not create the second
bounded relevance reception, candidate reception, reception authorization,
repeated reception permission, arbitrary reception, feed, relation view,
comparison view, index system, registry, search, ranking, source, authority,
currentness, action, synchronization, runtime permission, public API,
distributed behavior, operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumSuccessorCandidateAdmissionV0MinError(Exception):
    """Bounded error for candidate-admission resolver path loading."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_successor_candidate_admission_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min"
)
DEFAULT_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_reception_request_v0_min/"
    "local_relevance_medium_successor_reception_request_reference_review_001__"
    "local_relevance_medium_successor_reception_request_v0_min_result.json"
)

ADMISSION_TYPE = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
ADMISSION_SCOPE = "ONE_SUCCESSOR_CANDIDATE_ADMISSION_ONLY"
CANDIDATE_ADMISSION_STATUS = "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY"
FUTURE_SECOND_RECEPTION_SCOPE = "FUTURE_SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY"
SUCCESSOR_CANDIDATE_SCOPE = "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY"
MULTIPLICITY_PURPOSE = "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY"
SUCCESSOR_RECEPTION_REQUEST_TYPE = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST"
SUCCESSOR_RECEPTION_REQUEST_SCOPE = "ONE_SUCCESSOR_RECEPTION_REQUEST_ONLY"
SUCCESSOR_RECEPTION_REQUEST_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST_RECORDED"
)

SUPPORTED_ADMISSION_SCOPE_VALUES = (ADMISSION_SCOPE,)
SUPPORTED_ADMISSION_TYPE_VALUES = (ADMISSION_TYPE,)
SUPPORTED_CANDIDATE_ADMISSION_STATUS_VALUES = (CANDIDATE_ADMISSION_STATUS,)
SUPPORTED_FUTURE_SECOND_RECEPTION_SCOPE_VALUES = (FUTURE_SECOND_RECEPTION_SCOPE,)
SUPPORTED_SUCCESSOR_CANDIDATE_SCOPE_VALUES = (SUCCESSOR_CANDIDATE_SCOPE,)
SUPPORTED_MULTIPLICITY_PURPOSE_VALUES = (MULTIPLICITY_PURPOSE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REQUIRED_FALSE_NON_CLAIMS = (
    "second_reception_created",
    "candidate_received",
    "reception_authorization_created",
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "relation_view_created",
    "comparison_view_created",
    "index_system_created",
    "registry_created",
    "search_surface_created",
    "ranking_surface_created",
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
    "artifact_existence_treated_as_admission_authority",
    "latest_file_posture_treated_as_admission_authority",
    "repo_local_availability_treated_as_admission_authority",
    "hidden_repo_state_used_as_admission_content",
    "hidden_repo_state_used_as_admission_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_successor_candidate_admission_recorded",
    "basis_successor_reception_request_artifact_preserved",
    "basis_index_entry_artifact_preserved",
    "existing_orientation_view_artifact_preserved",
    "existing_source_receipt_artifact_preserved",
    "existing_referenced_reception_artifact_preserved",
    "existing_received_signal_id_preserved",
    "existing_received_relevance_basis_id_preserved",
    "existing_received_relevance_scope_id_preserved",
    "existing_received_carrier_context_id_preserved",
    "existing_received_reception_envelope_id_preserved",
    "successor_candidate_id_preserved",
    "successor_candidate_differs_from_existing_signal",
    "successor_candidate_scope_bounded_only",
    "admission_scope_one_candidate_only",
    "candidate_admission_status_candidate_only",
    "future_second_reception_scope_bounded_only",
    "multiplicity_purpose_local_only",
    "max_local_orientation_objects_after_future_reception_is_two",
    "successor_candidate_admitted_as_candidate",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_BLOCK_REQUESTED",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_PATH_MISSING",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_UNREADABLE",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_JSON_OBJECT",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_RECORDED",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_VERSION_NOT_0_1_0",
    "SUCCESSOR_RECEPTION_REQUEST_OBJECT_MISSING",
    "REQUEST_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST",
    "REQUEST_SCOPE_NOT_ONE_SUCCESSOR_ONLY",
    "BASIS_INDEX_ENTRY_ARTIFACT_MISSING",
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
    "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY",
    "ADMISSION_SCOPE_MISSING",
    "ADMISSION_SCOPE_NOT_ONE_CANDIDATE_ONLY",
    "ADMISSION_TYPE_MISSING",
    "ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION",
    "CANDIDATE_ADMISSION_STATUS_MISSING",
    "CANDIDATE_ADMISSION_STATUS_NOT_CANDIDATE_ONLY",
    "FUTURE_SECOND_RECEPTION_SCOPE_MISSING",
    "FUTURE_SECOND_RECEPTION_SCOPE_NOT_BOUNDED_ONLY",
    "MULTIPLICITY_PURPOSE_MISSING",
    "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
    "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO",
    "SUCCESSOR_CANDIDATE_NOT_ADMITTED_AS_CANDIDATE",
    "SECOND_RECEPTION_CREATED",
    "CANDIDATE_RECEIVED",
    "RECEPTION_AUTHORIZATION_CREATED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "RELATION_VIEW_CREATED",
    "COMPARISON_VIEW_CREATED",
    "INDEX_SYSTEM_CREATED",
    "REGISTRY_CREATED",
    "SEARCH_SURFACE_CREATED",
    "RANKING_SURFACE_CREATED",
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
    "ARTIFACT_EXISTENCE_TREATED_AS_ADMISSION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_ADMISSION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_ADMISSION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_ADMISSION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_ADMISSION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_admission_body",
    "raw_successor_candidate_admission_body",
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
    "admission_body",
    "successor_candidate_admission_body",
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

HOSTILE_SENTINELS = (
    "RAW_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
    "RAW_SUCCESSOR_CANDIDATE_ADMISSION_BODY_MUST_NOT_RETURN",
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

FALSE_POSTURE_CHECKS = (
    ("second_reception_created", "second reception not created", "SECOND_RECEPTION_CREATED"),
    ("candidate_received", "candidate not received", "CANDIDATE_RECEIVED"),
    (
        "reception_authorization_created",
        "reception authorization not created",
        "RECEPTION_AUTHORIZATION_CREATED",
    ),
    (
        "repeated_reception_permission_created",
        "repeated reception permission not created",
        "REPEATED_RECEPTION_PERMISSION_CREATED",
    ),
    ("arbitrary_reception_created", "arbitrary reception not created", "ARBITRARY_RECEPTION_CREATED"),
    ("feed_created", "feed not created", "FEED_CREATED"),
    ("relation_view_created", "relation view not created", "RELATION_VIEW_CREATED"),
    ("comparison_view_created", "comparison view not created", "COMPARISON_VIEW_CREATED"),
    ("index_system_created", "index system not created", "INDEX_SYSTEM_CREATED"),
    ("registry_created", "registry not created", "REGISTRY_CREATED"),
    ("search_surface_created", "search not created", "SEARCH_SURFACE_CREATED"),
    ("ranking_surface_created", "ranking not created", "RANKING_SURFACE_CREATED"),
    ("source_transfer_occurred", "source transfer not created", "SOURCE_TRANSFER_OCCURRED"),
    ("source_receipt_occurred", "source receipt not created", "SOURCE_RECEIPT_OCCURRED"),
    ("source_created", "source not created", "SOURCE_CREATED"),
    ("authority_created", "authority not created", "AUTHORITY_CREATED"),
    ("currentness_created", "currentness not created", "CURRENTNESS_CREATED"),
    ("truth_created", "truth not created", "TRUTH_CREATED"),
    ("action_created", "action not created", "ACTION_CREATED"),
    ("synchronization_created", "synchronization not created", "SYNCHRONIZATION_CREATED"),
    ("participation_authorized", "participation not authorized", "PARTICIPATION_AUTHORIZED"),
    ("participant_role_created", "participant role not created", "PARTICIPANT_ROLE_CREATED"),
    ("runtime_permission_created", "runtime permission not created", "RUNTIME_PERMISSION_CREATED"),
    ("public_api_created", "public API not created", "PUBLIC_API_CREATED"),
    (
        "participant_facing_interface_created",
        "participant-facing interface not created",
        "PARTICIPANT_FACING_INTERFACE_CREATED",
    ),
    (
        "distributed_network_behavior_created",
        "distributed network behavior not created",
        "DISTRIBUTED_NETWORK_BEHAVIOR_CREATED",
    ),
    ("deployment_created", "deployment not created", "DEPLOYMENT_CREATED"),
    ("public_release_created", "public release not created", "PUBLIC_RELEASE_CREATED"),
    ("operation_permission_created", "operation permission not created", "OPERATION_PERMISSION_CREATED"),
    (
        "broader_reusable_permission_created",
        "broader reusable permission not created",
        "BROADER_REUSABLE_PERMISSION_CREATED",
    ),
    ("follow_on_work_authorized", "follow-on work not authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        "artifact_existence_treated_as_admission_authority",
        "artifact existence not admission authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_ADMISSION_AUTHORITY",
    ),
    (
        "latest_file_posture_treated_as_admission_authority",
        "latest file posture not admission authority",
        "LATEST_FILE_POSTURE_TREATED_AS_ADMISSION_AUTHORITY",
    ),
    (
        "repo_local_availability_treated_as_admission_authority",
        "repo-local availability not admission authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_ADMISSION_AUTHORITY",
    ),
    (
        "hidden_repo_state_used_as_admission_content",
        "hidden repo state not admission content",
        "HIDDEN_REPO_STATE_USED_AS_ADMISSION_CONTENT",
    ),
    (
        "hidden_repo_state_used_as_admission_authority",
        "hidden repo state not admission authority",
        "HIDDEN_REPO_STATE_USED_AS_ADMISSION_AUTHORITY",
    ),
    ("consumed_request_reopened", "consumed request not reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "authorization token not reused", "AUTHORIZATION_TOKEN_REUSED"),
)

WHAT_REMAINS_OPEN = (
    "second_bounded_relevance_reception",
    "candidate_reception",
    "reception_authorization",
    "local_medium_multiplicity_result",
    "relation_view",
    "comparison_view",
    "local_relevance_orientation_index_system_if_separately_selected",
    "registry",
    "search_surface",
    "ranking_surface",
    "source_transfer",
    "source_receipt",
    "derivative_reception",
    "vessel_relation",
    "adoption",
    "authority_creation",
    "currentness_creation",
    "truth_creation",
    "action",
    "synchronization",
    "participation_authorization",
    "participant_role",
    "runtime_permission",
    "public_api",
    "participant_facing_interface",
    "distributed_network_behavior",
    "operation_permission",
    "receiving_context_governance",
    "deployment",
    "public_release",
    "publication_flow",
    "broader_reusable_permission",
    "admission_reuse",
    "follow_on_work",
)


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def _as_mapping(value: Any) -> dict[str, Any]:
    if isinstance(value, Mapping):
        return dict(value)
    return {}


def _is_declared(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _first_present(*values: Any) -> Any:
    for value in values:
        if value is not None:
            return value
    return None


def _coerce_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _canonical_false_non_claims() -> dict[str, bool]:
    return {key: False for key in REQUIRED_FALSE_NON_CLAIMS}


def _declared_non_claims_are_canonical_false(declared: Any) -> bool:
    if not isinstance(declared, Mapping):
        return False
    for key in REQUIRED_FALSE_NON_CLAIMS:
        if key not in declared or declared[key] is not False:
            return False
    return True


def _contains_hostile_sentinel(value: Any) -> bool:
    if isinstance(value, str):
        return any(sentinel in value for sentinel in HOSTILE_SENTINELS)
    if isinstance(value, Mapping):
        return any(_contains_hostile_sentinel(item) for item in value.values())
    if isinstance(value, (list, tuple)):
        return any(_contains_hostile_sentinel(item) for item in value)
    return False


def _sanitize(value: Any, key: str | None = None) -> Any:
    if key is not None and (key in SENSITIVE_CONTENT_KEYS or key.endswith("_body")):
        return "[REDACTED_RAW_BODY]"
    if isinstance(value, str):
        if any(sentinel in value for sentinel in HOSTILE_SENTINELS):
            return "[REDACTED_RAW_BODY]"
        return value
    if isinstance(value, Mapping):
        return {str(item_key): _sanitize(item_value, str(item_key)) for item_key, item_value in value.items()}
    if isinstance(value, list):
        return [_sanitize(item) for item in value]
    if isinstance(value, tuple):
        return [_sanitize(item) for item in value]
    return value


def _check(
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
        "block_code": None,
        "failure_code": None,
    }
    if not passed and code:
        record["block_code"] = code
        record["failure_code"] = code
    return record


def _first_failed_code(checks: list[dict[str, Any]]) -> str | None:
    for check in checks:
        if check.get("passed") is False:
            code = check.get("block_code") or check.get("failure_code")
            if isinstance(code, str):
                return code
    return None


def _read_json_object(path_value: Any) -> tuple[dict[str, Any] | None, str | None]:
    if not _is_declared(path_value):
        return None, "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_PATH_MISSING"
    path = Path(str(path_value))
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None, "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_UNREADABLE"
    if not isinstance(payload, Mapping):
        return None, "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_JSON_OBJECT"
    return dict(payload), None


def _extract_failed_check_count_from_artifact(artifact: Mapping[str, Any]) -> int | None:
    metadata = _as_mapping(artifact.get("local_relevance_medium_successor_reception_request_metadata"))
    summary = _as_mapping(artifact.get("local_relevance_medium_successor_reception_request_summary"))
    value = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        artifact.get("failed_check_count"),
    )
    if value is None:
        checks = artifact.get("local_relevance_medium_successor_reception_request_checks")
        if isinstance(checks, list):
            return sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False)
    return _coerce_int(value)


def _extract_successor_reception_request_facts(
    artifact: Mapping[str, Any] | None,
    selected_artifact_path: Any,
) -> dict[str, Any]:
    if artifact is None:
        return {
            "basis_successor_reception_request_artifact": str(selected_artifact_path)
            if _is_declared(selected_artifact_path)
            else None,
            "request_object_present": False,
        }

    metadata = _as_mapping(artifact.get("local_relevance_medium_successor_reception_request_metadata"))
    summary = _as_mapping(artifact.get("local_relevance_medium_successor_reception_request_summary"))
    request_object = _as_mapping(artifact.get("successor_reception_request_object"))

    result_version = _first_present(
        metadata.get("local_relevance_medium_successor_reception_request_version"),
        metadata.get("result_version"),
        summary.get("result_version"),
        request_object.get("request_version"),
        artifact.get("result_version"),
    )
    failed_check_count = _extract_failed_check_count_from_artifact(artifact)

    return {
        "basis_successor_reception_request_artifact": str(selected_artifact_path)
        if _is_declared(selected_artifact_path)
        else None,
        "basis_successor_reception_request_outcome": artifact.get("outcome"),
        "basis_successor_reception_request_result_version": result_version,
        "basis_successor_reception_request_failed_check_count": failed_check_count,
        "request_object_present": bool(request_object),
        "successor_reception_request_object": _sanitize(request_object),
        "request_type": request_object.get("request_type"),
        "request_scope": request_object.get("request_scope"),
        "basis_index_entry_artifact": request_object.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": request_object.get("existing_orientation_view_artifact"),
        "existing_source_receipt_artifact": request_object.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": request_object.get("existing_referenced_reception_artifact"),
        "existing_received_signal_id": request_object.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": request_object.get("existing_received_relevance_basis_id"),
        "existing_received_relevance_scope_id": request_object.get("existing_received_relevance_scope_id"),
        "existing_received_carrier_context_id": request_object.get("existing_received_carrier_context_id"),
        "existing_received_reception_envelope_id": request_object.get("existing_received_reception_envelope_id"),
        "successor_candidate_id": request_object.get("successor_candidate_id"),
        "successor_candidate_scope": request_object.get("successor_candidate_scope"),
        "multiplicity_purpose": request_object.get("multiplicity_purpose"),
        "max_local_orientation_objects_after_successor": request_object.get(
            "max_local_orientation_objects_after_successor"
        ),
    }


def _build_successor_candidate_admission_object(facts: Mapping[str, Any]) -> dict[str, Any]:
    return {
        "admission_id": "local_relevance_medium_successor_candidate_admission_001",
        "admission_type": ADMISSION_TYPE,
        "admission_version": RESULT_VERSION,
        "admission_scope": ADMISSION_SCOPE,
        "basis_successor_reception_request_artifact": facts.get(
            "basis_successor_reception_request_artifact"
        ),
        "basis_successor_reception_request_outcome": facts.get(
            "basis_successor_reception_request_outcome"
        ),
        "basis_successor_reception_request_result_version": facts.get(
            "basis_successor_reception_request_result_version"
        ),
        "basis_successor_reception_request_failed_check_count": facts.get(
            "basis_successor_reception_request_failed_check_count"
        ),
        "basis_index_entry_artifact": facts.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": facts.get("existing_orientation_view_artifact"),
        "existing_source_receipt_artifact": facts.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": facts.get("existing_referenced_reception_artifact"),
        "existing_received_signal_id": facts.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": facts.get("existing_received_relevance_basis_id"),
        "existing_received_relevance_scope_id": facts.get("existing_received_relevance_scope_id"),
        "existing_received_carrier_context_id": facts.get("existing_received_carrier_context_id"),
        "existing_received_reception_envelope_id": facts.get("existing_received_reception_envelope_id"),
        "successor_candidate_id": facts.get("successor_candidate_id"),
        "successor_candidate_scope": SUCCESSOR_CANDIDATE_SCOPE,
        "candidate_admission_status": CANDIDATE_ADMISSION_STATUS,
        "future_second_reception_scope": FUTURE_SECOND_RECEPTION_SCOPE,
        "multiplicity_purpose": MULTIPLICITY_PURPOSE,
        "max_local_orientation_objects_after_future_reception": 2,
        "successor_candidate_admitted_as_candidate": True,
        "second_reception_created": False,
        "candidate_received": False,
        "reception_authorization_created": False,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "relation_view_created": False,
        "comparison_view_created": False,
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


def _build_checks(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    artifact_payload: Mapping[str, Any] | None,
    artifact_read_error: str | None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("local_relevance_medium_successor_candidate_admission_question")
    intent = request.get("local_relevance_medium_successor_candidate_admission_intent")
    artifact_path = request.get("selected_successor_reception_request_artifact")
    admission_scope = request.get("admission_scope")
    admission_type = request.get("admission_type")
    candidate_status = request.get("candidate_admission_status")
    future_scope = request.get("future_second_reception_scope")
    multiplicity_purpose = request.get("multiplicity_purpose")
    max_after_future = request.get("max_local_orientation_objects_after_future_reception")
    declared_non_claims = request.get("declared_non_claims")

    checks.append(
        _check(
            "admission question declared",
            _is_declared(question),
            "declared admission question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block intent not requested",
            intent != INTENT_BLOCK,
            "intent other than explicit block",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "selected successor reception request artifact path declared",
            _is_declared(artifact_path)
            and request.get("selected_successor_reception_request_artifact_missing") is not True,
            "declared successor reception request artifact path",
            artifact_path,
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected successor reception request artifact readable JSON",
            artifact_read_error not in {
                "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_UNREADABLE",
                "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_PATH_MISSING",
            },
            "readable JSON object",
            artifact_read_error or "readable",
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "selected successor reception request artifact JSON object",
            artifact_read_error != "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_JSON_OBJECT",
            "JSON object",
            artifact_read_error or ("JSON object" if artifact_payload is not None else None),
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "successor reception request artifact outcome recorded",
            facts.get("basis_successor_reception_request_outcome")
            == SUCCESSOR_RECEPTION_REQUEST_RECORDED_OUTCOME
            and request.get("selected_successor_reception_request_artifact_not_recorded") is not True,
            SUCCESSOR_RECEPTION_REQUEST_RECORDED_OUTCOME,
            facts.get("basis_successor_reception_request_outcome"),
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "successor reception request artifact result version 0.1.0",
            facts.get("basis_successor_reception_request_result_version") == RESULT_VERSION
            and request.get("selected_successor_reception_request_artifact_version_not_0_1_0") is not True,
            RESULT_VERSION,
            facts.get("basis_successor_reception_request_result_version"),
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "successor reception request artifact failed check count zero",
            facts.get("basis_successor_reception_request_failed_check_count") == 0
            and request.get("selected_successor_reception_request_artifact_failed_checks_present") is not True,
            0,
            facts.get("basis_successor_reception_request_failed_check_count"),
            "SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "successor reception request object present",
            facts.get("request_object_present") is True
            and request.get("successor_reception_request_object_missing") is not True,
            "successor_reception_request_object present",
            facts.get("request_object_present"),
            "SUCCESSOR_RECEPTION_REQUEST_OBJECT_MISSING",
        )
    )
    checks.append(
        _check(
            "request type exact",
            facts.get("request_type") == SUCCESSOR_RECEPTION_REQUEST_TYPE
            and request.get("request_type_not_successor_reception_request") is not True,
            SUCCESSOR_RECEPTION_REQUEST_TYPE,
            facts.get("request_type"),
            "REQUEST_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST",
        )
    )
    checks.append(
        _check(
            "request scope one successor only",
            facts.get("request_scope") == SUCCESSOR_RECEPTION_REQUEST_SCOPE
            and request.get("request_scope_not_one_successor_only") is not True,
            SUCCESSOR_RECEPTION_REQUEST_SCOPE,
            facts.get("request_scope"),
            "REQUEST_SCOPE_NOT_ONE_SUCCESSOR_ONLY",
        )
    )

    basis_presence = (
        ("basis index entry artifact present", "basis_index_entry_artifact", "basis_index_entry_artifact_missing", "BASIS_INDEX_ENTRY_ARTIFACT_MISSING"),
        ("existing orientation view artifact present", "existing_orientation_view_artifact", "existing_orientation_view_artifact_missing", "EXISTING_ORIENTATION_VIEW_ARTIFACT_MISSING"),
        ("existing source receipt artifact present", "existing_source_receipt_artifact", "existing_source_receipt_artifact_missing", "EXISTING_SOURCE_RECEIPT_ARTIFACT_MISSING"),
        ("existing referenced reception artifact present", "existing_referenced_reception_artifact", "existing_referenced_reception_artifact_missing", "EXISTING_REFERENCED_RECEPTION_ARTIFACT_MISSING"),
        ("existing received signal id present", "existing_received_signal_id", "existing_received_signal_id_missing", "EXISTING_RECEIVED_SIGNAL_ID_MISSING"),
        ("existing received relevance basis id present", "existing_received_relevance_basis_id", "existing_received_relevance_basis_id_missing", "EXISTING_RECEIVED_RELEVANCE_BASIS_ID_MISSING"),
        ("existing received relevance scope id present", "existing_received_relevance_scope_id", "existing_received_relevance_scope_id_missing", "EXISTING_RECEIVED_RELEVANCE_SCOPE_ID_MISSING"),
        ("existing received carrier context id present", "existing_received_carrier_context_id", "existing_received_carrier_context_id_missing", "EXISTING_RECEIVED_CARRIER_CONTEXT_ID_MISSING"),
        ("existing received reception envelope id present", "existing_received_reception_envelope_id", "existing_received_reception_envelope_id_missing", "EXISTING_RECEIVED_RECEPTION_ENVELOPE_ID_MISSING"),
    )
    for check_name, fact_key, shortcut_key, code in basis_presence:
        checks.append(
            _check(
                check_name,
                _is_declared(facts.get(fact_key)) and request.get(shortcut_key) is not True,
                "present non-empty value",
                facts.get(fact_key),
                code,
            )
        )

    successor_candidate_id = facts.get("successor_candidate_id")
    existing_signal_id = facts.get("existing_received_signal_id")
    checks.append(
        _check(
            "successor candidate id present",
            _is_declared(successor_candidate_id) and request.get("successor_candidate_id_missing") is not True,
            "declared successor candidate id",
            successor_candidate_id,
            "SUCCESSOR_CANDIDATE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "successor candidate differs from existing signal",
            _is_declared(successor_candidate_id)
            and _is_declared(existing_signal_id)
            and successor_candidate_id != existing_signal_id
            and request.get("successor_candidate_id_equals_existing_signal") is not True,
            "successor candidate id distinct from existing received signal id",
            {"successor_candidate_id": successor_candidate_id, "existing_received_signal_id": existing_signal_id},
            "SUCCESSOR_CANDIDATE_ID_EQUALS_EXISTING_SIGNAL",
        )
    )
    checks.append(
        _check(
            "successor candidate scope bounded only",
            facts.get("successor_candidate_scope") == SUCCESSOR_CANDIDATE_SCOPE,
            SUCCESSOR_CANDIDATE_SCOPE,
            facts.get("successor_candidate_scope"),
            "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY",
        )
    )
    checks.append(
        _check(
            "admission type declared",
            _is_declared(admission_type),
            "declared admission type",
            admission_type,
            "ADMISSION_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "admission type exact",
            admission_type == ADMISSION_TYPE,
            ADMISSION_TYPE,
            admission_type,
            "ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION",
        )
    )
    checks.append(
        _check(
            "admission scope declared",
            _is_declared(admission_scope),
            "declared admission scope",
            admission_scope,
            "ADMISSION_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "admission scope one candidate only",
            admission_scope == ADMISSION_SCOPE,
            ADMISSION_SCOPE,
            admission_scope,
            "ADMISSION_SCOPE_NOT_ONE_CANDIDATE_ONLY",
        )
    )
    checks.append(
        _check(
            "candidate admission status declared",
            _is_declared(candidate_status),
            "declared candidate admission status",
            candidate_status,
            "CANDIDATE_ADMISSION_STATUS_MISSING",
        )
    )
    checks.append(
        _check(
            "candidate admission status candidate only",
            candidate_status == CANDIDATE_ADMISSION_STATUS,
            CANDIDATE_ADMISSION_STATUS,
            candidate_status,
            "CANDIDATE_ADMISSION_STATUS_NOT_CANDIDATE_ONLY",
        )
    )
    checks.append(
        _check(
            "future second reception scope declared",
            _is_declared(future_scope),
            "declared future second reception scope",
            future_scope,
            "FUTURE_SECOND_RECEPTION_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "future second reception scope bounded only",
            future_scope == FUTURE_SECOND_RECEPTION_SCOPE,
            FUTURE_SECOND_RECEPTION_SCOPE,
            future_scope,
            "FUTURE_SECOND_RECEPTION_SCOPE_NOT_BOUNDED_ONLY",
        )
    )
    checks.append(
        _check(
            "multiplicity purpose declared",
            _is_declared(multiplicity_purpose),
            "declared multiplicity purpose",
            multiplicity_purpose,
            "MULTIPLICITY_PURPOSE_MISSING",
        )
    )
    checks.append(
        _check(
            "multiplicity purpose local only",
            multiplicity_purpose == MULTIPLICITY_PURPOSE
            and facts.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE,
            MULTIPLICITY_PURPOSE,
            {
                "declared_multiplicity_purpose": multiplicity_purpose,
                "request_artifact_multiplicity_purpose": facts.get("multiplicity_purpose"),
            },
            "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
        )
    )
    checks.append(
        _check(
            "max local orientation objects after future reception is two",
            _coerce_int(max_after_future) == 2
            and _coerce_int(facts.get("max_local_orientation_objects_after_successor")) == 2,
            2,
            {
                "declared_max_local_orientation_objects_after_future_reception": max_after_future,
                "request_artifact_max_local_orientation_objects_after_successor": facts.get(
                    "max_local_orientation_objects_after_successor"
                ),
            },
            "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO",
        )
    )
    checks.append(
        _check(
            "successor candidate admitted as candidate only",
            candidate_status == CANDIDATE_ADMISSION_STATUS
            and request.get("successor_candidate_not_admitted_as_candidate") is not True
            and request.get("successor_candidate_admitted_as_candidate", True) is not False,
            "candidate admitted as candidate only",
            {
                "candidate_admission_status": candidate_status,
                "successor_candidate_not_admitted_as_candidate": request.get(
                    "successor_candidate_not_admitted_as_candidate"
                ),
            },
            "SUCCESSOR_CANDIDATE_NOT_ADMITTED_AS_CANDIDATE",
        )
    )

    for field_name, check_name, code in FALSE_POSTURE_CHECKS:
        checks.append(
            _check(
                check_name,
                request.get(field_name, False) is not True,
                False,
                request.get(field_name, False),
                code,
            )
        )

    predecessor_preserved = (
        request.get("predecessor_failure_repaired") is not True
        and request.get("predecessor_failure_hidden") is not True
        and request.get("predecessor_failure_claimed_passed") is not True
    )
    checks.append(
        _check(
            "predecessor failure evidence preserved",
            predecessor_preserved,
            "predecessor failure evidence preserved without repair, hiding, or passed claim",
            {
                "predecessor_failure_repaired": request.get("predecessor_failure_repaired", False),
                "predecessor_failure_hidden": request.get("predecessor_failure_hidden", False),
                "predecessor_failure_claimed_passed": request.get(
                    "predecessor_failure_claimed_passed", False
                ),
            },
            "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
        )
    )
    checks.append(
        _check(
            "result-level required false non-claims canonical false",
            all(value is False for value in _canonical_false_non_claims().values()),
            "all result-level required non-claims false",
            _canonical_false_non_claims(),
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    checks.append(
        _check(
            "required non-claims false",
            _declared_non_claims_are_canonical_false(declared_non_claims),
            "declared required non-claims all present and false",
            declared_non_claims,
            "NON_CLAIM_MISSING_OR_FLIPPED",
        )
    )
    return checks


def _build_statement(recorded: bool, result_non_claims_canonical_false: bool) -> dict[str, bool]:
    statement = {key: bool(recorded) for key in ALLOWED_TRUE_RECORDED_FIELDS}
    statement["result_level_non_claims_canonical_false"] = bool(result_non_claims_canonical_false)
    if not recorded:
        for key in ALLOWED_TRUE_RECORDED_FIELDS:
            if key != "result_level_non_claims_canonical_false":
                statement[key] = False
    return statement


def _build_block(outcome: str, code: str | None, reason: str | None) -> dict[str, Any]:
    blocked = outcome == OUTCOME_BLOCKED
    return {
        "blocked": blocked,
        "code": code if blocked else None,
        "block_code": code if blocked else None,
        "reason": reason if blocked else None,
    }


def _select_outcome_and_block(
    request: Mapping[str, Any],
    checks: list[dict[str, Any]],
) -> tuple[str, str | None, str | None]:
    first_code = _first_failed_code(checks)
    if first_code is not None:
        return OUTCOME_BLOCKED, first_code, "candidate admission request blocked by failed check"

    requested_outcome = request.get("requested_local_relevance_medium_successor_candidate_admission_outcome")
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
    if requested_outcome == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None, None
    if request.get("local_relevance_medium_successor_candidate_admission_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None, None
    return OUTCOME_RECORDED, None, None


def _build_non_meaning() -> dict[str, Any]:
    return {
        "admission_is_not": (
            "second_bounded_relevance_reception",
            "candidate_reception",
            "reception_authorization",
            "repeated_reception_permission",
            "arbitrary_reception",
            "feed",
            "relation_view",
            "comparison_view",
            "index_system",
            "registry",
            "search",
            "ranking",
            "authority",
            "currentness",
            "truth",
            "action",
            "synchronization",
            "runtime_permission",
            "public_api",
            "participant_facing_interface",
            "distributed_network_behavior",
            "operation_permission",
            "follow_on_work",
        ),
        "candidate_admission_only": True,
    }


def _build_artifact_basis(facts: Mapping[str, Any], artifact_read_error: str | None) -> dict[str, Any]:
    return {
        "selected_successor_reception_request_artifact": facts.get(
            "basis_successor_reception_request_artifact"
        ),
        "read_error": artifact_read_error,
        "basis_successor_reception_request_outcome": facts.get(
            "basis_successor_reception_request_outcome"
        ),
        "basis_successor_reception_request_result_version": facts.get(
            "basis_successor_reception_request_result_version"
        ),
        "basis_successor_reception_request_failed_check_count": facts.get(
            "basis_successor_reception_request_failed_check_count"
        ),
        "successor_reception_request_object_present": facts.get("request_object_present"),
        "request_type": facts.get("request_type"),
        "request_scope": facts.get("request_scope"),
        "basis_index_entry_artifact": facts.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": facts.get("existing_orientation_view_artifact"),
        "existing_source_receipt_artifact": facts.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": facts.get("existing_referenced_reception_artifact"),
        "existing_received_signal_id": facts.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": facts.get("existing_received_relevance_basis_id"),
        "existing_received_relevance_scope_id": facts.get("existing_received_relevance_scope_id"),
        "existing_received_carrier_context_id": facts.get("existing_received_carrier_context_id"),
        "existing_received_reception_envelope_id": facts.get("existing_received_reception_envelope_id"),
        "successor_candidate_id": facts.get("successor_candidate_id"),
        "successor_candidate_scope": facts.get("successor_candidate_scope"),
        "multiplicity_purpose": facts.get("multiplicity_purpose"),
        "max_local_orientation_objects_after_successor": facts.get(
            "max_local_orientation_objects_after_successor"
        ),
    }


def _facts_are_sufficient(facts: Mapping[str, Any]) -> bool:
    required_keys = (
        "basis_successor_reception_request_artifact",
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
    )
    if any(not _is_declared(facts.get(key)) for key in required_keys):
        return False
    return (
        facts.get("basis_successor_reception_request_outcome")
        == SUCCESSOR_RECEPTION_REQUEST_RECORDED_OUTCOME
        and facts.get("basis_successor_reception_request_result_version") == RESULT_VERSION
        and facts.get("basis_successor_reception_request_failed_check_count") == 0
        and facts.get("request_type") == SUCCESSOR_RECEPTION_REQUEST_TYPE
        and facts.get("request_scope") == SUCCESSOR_RECEPTION_REQUEST_SCOPE
        and facts.get("successor_candidate_scope") == SUCCESSOR_CANDIDATE_SCOPE
        and facts.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE
        and _coerce_int(facts.get("max_local_orientation_objects_after_successor")) == 2
        and facts.get("successor_candidate_id") != facts.get("existing_received_signal_id")
    )


def _admission_shape_supported(request: Mapping[str, Any]) -> bool:
    return (
        request.get("admission_type") == ADMISSION_TYPE
        and request.get("admission_scope") == ADMISSION_SCOPE
        and request.get("candidate_admission_status") == CANDIDATE_ADMISSION_STATUS
        and request.get("future_second_reception_scope") == FUTURE_SECOND_RECEPTION_SCOPE
        and request.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE
        and _coerce_int(request.get("max_local_orientation_objects_after_future_reception")) == 2
        and request.get("successor_candidate_not_admitted_as_candidate") is not True
        and request.get("successor_candidate_admitted_as_candidate", True) is not False
    )


def _assemble_result(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    checks: list[dict[str, Any]],
    outcome: str,
    block_code: str | None,
    block_reason: str | None,
    artifact_read_error: str | None,
) -> dict[str, Any]:
    failed_check_count = sum(1 for check in checks if check.get("passed") is False)
    passed_check_count = sum(1 for check in checks if check.get("passed") is True)
    recorded = outcome == OUTCOME_RECORDED and failed_check_count == 0
    result_non_claims = _canonical_false_non_claims()
    result_non_claims_canonical_false = all(value is False for value in result_non_claims.values())

    admission_id = request.get(
        "local_relevance_medium_successor_candidate_admission_id",
        "local_relevance_medium_successor_candidate_admission_reference_review_001",
    )
    metadata = {
        "local_relevance_medium_successor_candidate_admission_id": admission_id,
        "local_relevance_medium_successor_candidate_admission_type": ADMISSION_TYPE,
        "local_relevance_medium_successor_candidate_admission_version": RESULT_VERSION,
        "local_relevance_medium_successor_candidate_admission_intent": request.get(
            "local_relevance_medium_successor_candidate_admission_intent"
        ),
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_successor_candidate_admission_metadata": metadata,
        "declared_local_relevance_medium_successor_candidate_admission_question": _sanitize(
            request.get("local_relevance_medium_successor_candidate_admission_question")
        ),
        "selected_successor_reception_request_artifact_basis": _sanitize(
            _build_artifact_basis(facts, artifact_read_error)
        ),
        "successor_candidate_admission_object": _sanitize(
            _build_successor_candidate_admission_object(facts)
            if _facts_are_sufficient(facts) and _admission_shape_supported(request)
            else {}
        ),
        "local_relevance_medium_successor_candidate_admission_checks": _sanitize(checks),
        "local_relevance_medium_successor_candidate_admission_statement": _build_statement(
            recorded, result_non_claims_canonical_false
        ),
        "local_relevance_medium_successor_candidate_admission_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": result_non_claims,
        "outcome": outcome,
        "block": _build_block(outcome, block_code, block_reason),
    }
    result["local_relevance_medium_successor_candidate_admission_summary"] = (
        build_local_relevance_medium_successor_candidate_admission_v0_min_summary(result)
    )
    return _sanitize(result)


def _malformed_request_result(code: str, reason: str, actual: Any) -> dict[str, Any]:
    request = {
        "local_relevance_medium_successor_candidate_admission_id": (
            "local_relevance_medium_successor_candidate_admission_malformed_001"
        ),
        "local_relevance_medium_successor_candidate_admission_question": None,
        "local_relevance_medium_successor_candidate_admission_intent": None,
        "selected_successor_reception_request_artifact": None,
        "declared_non_claims": {},
    }
    facts = _extract_successor_reception_request_facts(None, None)
    checks = [
        _check(
            "declared local relevance medium successor candidate admission request mapping",
            False,
            "mapping request",
            type(actual).__name__,
            code,
        )
    ]
    return _assemble_result(request, facts, checks, OUTCOME_BLOCKED, code, reason, None)


def resolve_local_relevance_medium_successor_candidate_admission_v0_min(
    declared_local_relevance_medium_successor_candidate_admission: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one successor candidate admission request into a bounded result."""

    if declared_local_relevance_medium_successor_candidate_admission is None:
        request = build_declared_local_relevance_medium_successor_candidate_admission_v0_min_request()
    elif not isinstance(declared_local_relevance_medium_successor_candidate_admission, Mapping):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_REQUEST_MALFORMED",
            "declared candidate admission request was not a mapping",
            declared_local_relevance_medium_successor_candidate_admission,
        )
    else:
        request = copy.deepcopy(dict(declared_local_relevance_medium_successor_candidate_admission))

    if _contains_hostile_sentinel(request):
        request = _sanitize(request)

    artifact_path = request.get("selected_successor_reception_request_artifact")
    artifact_payload, artifact_read_error = _read_json_object(artifact_path)
    if artifact_payload is not None and _contains_hostile_sentinel(artifact_payload):
        artifact_payload = _sanitize(artifact_payload)
    facts = _extract_successor_reception_request_facts(artifact_payload, artifact_path)
    checks = _build_checks(request, facts, artifact_payload, artifact_read_error)
    outcome, block_code, block_reason = _select_outcome_and_block(request, checks)
    return _assemble_result(request, facts, checks, outcome, block_code, block_reason, artifact_read_error)


def resolve_local_relevance_medium_successor_candidate_admission_v0_min_from_path(
    declared_local_relevance_medium_successor_candidate_admission_path: Path | str,
) -> dict:
    """Load a declared candidate admission request from JSON and resolve it."""

    path = Path(declared_local_relevance_medium_successor_candidate_admission_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise LocalRelevanceMediumSuccessorCandidateAdmissionV0MinError(
            "declared local relevance medium successor candidate admission request unreadable"
        ) from exc
    if not isinstance(payload, Mapping):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_REQUEST_MALFORMED",
            "declared candidate admission request JSON was not an object",
            payload,
        )
    return resolve_local_relevance_medium_successor_candidate_admission_v0_min(payload)


def build_local_relevance_medium_successor_candidate_admission_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the compact public summary for a candidate admission result."""

    metadata = _as_mapping(result.get("local_relevance_medium_successor_candidate_admission_metadata"))
    statement = _as_mapping(
        result.get("local_relevance_medium_successor_candidate_admission_statement")
    )
    admission_object = _as_mapping(result.get("successor_candidate_admission_object"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    checks = result.get("local_relevance_medium_successor_candidate_admission_checks", [])
    if not isinstance(checks, list):
        checks = []

    failed_check_count = metadata.get(
        "failed_check_count",
        sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False),
    )
    passed_check_count = metadata.get(
        "passed_check_count",
        sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is True),
    )

    return {
        "outcome": result.get("outcome"),
        "block_code": block.get("code") or block.get("block_code"),
        "block_reason": block.get("reason"),
        "admission_id": metadata.get("local_relevance_medium_successor_candidate_admission_id"),
        "question": result.get("declared_local_relevance_medium_successor_candidate_admission_question"),
        "intent": metadata.get("local_relevance_medium_successor_candidate_admission_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("local_relevance_medium_successor_candidate_admission_version"),
        "resolver_module": metadata.get("resolver_module"),
        "local_relevance_medium_successor_candidate_admission_recorded": statement.get(
            "local_relevance_medium_successor_candidate_admission_recorded", False
        ),
        "basis_successor_reception_request_artifact_preserved": statement.get(
            "basis_successor_reception_request_artifact_preserved", False
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
        "successor_candidate_id_preserved": statement.get("successor_candidate_id_preserved", False),
        "successor_candidate_differs_from_existing_signal": statement.get(
            "successor_candidate_differs_from_existing_signal", False
        ),
        "successor_candidate_scope_bounded_only": statement.get(
            "successor_candidate_scope_bounded_only", False
        ),
        "admission_scope_one_candidate_only": statement.get(
            "admission_scope_one_candidate_only", False
        ),
        "candidate_admission_status_candidate_only": statement.get(
            "candidate_admission_status_candidate_only", False
        ),
        "future_second_reception_scope_bounded_only": statement.get(
            "future_second_reception_scope_bounded_only", False
        ),
        "multiplicity_purpose_local_only": statement.get("multiplicity_purpose_local_only", False),
        "max_local_orientation_objects_after_future_reception_is_two": statement.get(
            "max_local_orientation_objects_after_future_reception_is_two", False
        ),
        "successor_candidate_admitted_as_candidate": statement.get(
            "successor_candidate_admitted_as_candidate", False
        ),
        "admission_object_summary": {
            "admission_type": admission_object.get("admission_type"),
            "admission_scope": admission_object.get("admission_scope"),
            "successor_candidate_id": admission_object.get("successor_candidate_id"),
            "successor_candidate_scope": admission_object.get("successor_candidate_scope"),
            "candidate_admission_status": admission_object.get("candidate_admission_status"),
            "future_second_reception_scope": admission_object.get("future_second_reception_scope"),
            "multiplicity_purpose": admission_object.get("multiplicity_purpose"),
            "max_local_orientation_objects_after_future_reception": admission_object.get(
                "max_local_orientation_objects_after_future_reception"
            ),
            "successor_candidate_admitted_as_candidate": admission_object.get(
                "successor_candidate_admitted_as_candidate"
            ),
            "existing_received_signal_id": admission_object.get("existing_received_signal_id"),
        },
        "second_reception_created": non_claims.get("second_reception_created", False),
        "candidate_received": non_claims.get("candidate_received", False),
        "reception_authorization_created": non_claims.get(
            "reception_authorization_created", False
        ),
        "repeated_reception_permission_created": non_claims.get(
            "repeated_reception_permission_created", False
        ),
        "arbitrary_reception_created": non_claims.get("arbitrary_reception_created", False),
        "feed_created": non_claims.get("feed_created", False),
        "relation_view_created": non_claims.get("relation_view_created", False),
        "comparison_view_created": non_claims.get("comparison_view_created", False),
        "index_system_created": non_claims.get("index_system_created", False),
        "registry_created": non_claims.get("registry_created", False),
        "search_surface_created": non_claims.get("search_surface_created", False),
        "ranking_surface_created": non_claims.get("ranking_surface_created", False),
        "source_transfer_occurred": non_claims.get("source_transfer_occurred", False),
        "source_receipt_occurred": non_claims.get("source_receipt_occurred", False),
        "source_created": non_claims.get("source_created", False),
        "authority_created": non_claims.get("authority_created", False),
        "currentness_created": non_claims.get("currentness_created", False),
        "truth_created": non_claims.get("truth_created", False),
        "action_created": non_claims.get("action_created", False),
        "synchronization_created": non_claims.get("synchronization_created", False),
        "participation_authorized": non_claims.get("participation_authorized", False),
        "participant_role_created": non_claims.get("participant_role_created", False),
        "runtime_permission_created": non_claims.get("runtime_permission_created", False),
        "public_api_created": non_claims.get("public_api_created", False),
        "participant_facing_interface_created": non_claims.get(
            "participant_facing_interface_created", False
        ),
        "distributed_network_behavior_created": non_claims.get(
            "distributed_network_behavior_created", False
        ),
        "deployment_created": non_claims.get("deployment_created", False),
        "public_release_created": non_claims.get("public_release_created", False),
        "operation_permission_created": non_claims.get("operation_permission_created", False),
        "broader_reusable_permission_created": non_claims.get(
            "broader_reusable_permission_created", False
        ),
        "follow_on_work_authorized": non_claims.get("follow_on_work_authorized", False),
        "consumed_request_reopened": non_claims.get("consumed_request_reopened", False),
        "authorization_token_reused": non_claims.get("authorization_token_reused", False),
        "key_non_claims": {
            key: non_claims.get(key, False)
            for key in (
                "second_reception_created",
                "candidate_received",
                "reception_authorization_created",
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
                "relation_view_created",
                "comparison_view_created",
                "index_system_created",
                "registry_created",
                "search_surface_created",
                "ranking_surface_created",
                "source_transfer_occurred",
                "source_receipt_occurred",
                "authority_created",
                "currentness_created",
                "truth_created",
                "action_created",
                "synchronization_created",
                "public_api_created",
                "distributed_network_behavior_created",
                "operation_permission_created",
                "follow_on_work_authorized",
                "consumed_request_reopened",
                "authorization_token_reused",
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


def write_local_relevance_medium_successor_candidate_admission_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a candidate admission resolver result without overwriting existing files."""

    metadata = _as_mapping(result.get("local_relevance_medium_successor_candidate_admission_metadata"))
    admission_id = metadata.get(
        "local_relevance_medium_successor_candidate_admission_id",
        "local_relevance_medium_successor_candidate_admission_reference_review_001",
    )
    if output_path is None:
        output_dir = Path(OUTPUT_ROOT)
        base_path = output_dir / (
            f"{admission_id}__local_relevance_medium_successor_candidate_admission_v0_min_result.json"
        )
    else:
        base_path = Path(output_path)
        output_dir = base_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)

    candidate_path = base_path
    if candidate_path.exists():
        stem = base_path.stem
        suffix = base_path.suffix
        parent = base_path.parent
        index = 1
        while True:
            candidate_path = parent / f"{stem}_{index:03d}{suffix}"
            if not candidate_path.exists():
                break
            index += 1

    with candidate_path.open("w", encoding="utf-8") as handle:
        json.dump(_sanitize(dict(result)), handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
    return candidate_path


def build_declared_local_relevance_medium_successor_candidate_admission_v0_min_request(
    *,
    local_relevance_medium_successor_candidate_admission_id: str = (
        "local_relevance_medium_successor_candidate_admission_reference_review_001"
    ),
    local_relevance_medium_successor_candidate_admission_question: str | None = None,
    local_relevance_medium_successor_candidate_admission_intent: str = INTENT_RECORD,
    selected_successor_reception_request_artifact: Path | str = DEFAULT_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT,
    admission_scope: str = ADMISSION_SCOPE,
    admission_type: str = ADMISSION_TYPE,
    candidate_admission_status: str = CANDIDATE_ADMISSION_STATUS,
    future_second_reception_scope: str = FUTURE_SECOND_RECEPTION_SCOPE,
    multiplicity_purpose: str = MULTIPLICITY_PURPOSE,
    max_local_orientation_objects_after_future_reception: int = 2,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared admission request with canonical false non-claims."""

    if local_relevance_medium_successor_candidate_admission_question is None:
        local_relevance_medium_successor_candidate_admission_question = (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_RECEPTION_REQUEST, may one "
            "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION be recorded that admits "
            "exactly one declared successor candidate as eligible for a future second bounded "
            "relevance reception, without creating second reception, candidate reception, "
            "reception authorization, repeated reception permission, arbitrary reception, feed, "
            "relation view, comparison view, index system, registry, search, ranking, source "
            "transfer, source receipt, authority, currentness, truth, action, synchronization, "
            "participation authorization, participant role, runtime permission, public API, "
            "participant-facing interface, distributed network behavior, operation permission, "
            "or follow-on work?"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))

    request: dict[str, Any] = {
        "local_relevance_medium_successor_candidate_admission_id": (
            local_relevance_medium_successor_candidate_admission_id
        ),
        "local_relevance_medium_successor_candidate_admission_question": (
            local_relevance_medium_successor_candidate_admission_question
        ),
        "local_relevance_medium_successor_candidate_admission_intent": (
            local_relevance_medium_successor_candidate_admission_intent
        ),
        "selected_successor_reception_request_artifact": str(
            selected_successor_reception_request_artifact
        ),
        "admission_scope": admission_scope,
        "admission_type": admission_type,
        "candidate_admission_status": candidate_admission_status,
        "future_second_reception_scope": future_second_reception_scope,
        "multiplicity_purpose": multiplicity_purpose,
        "max_local_orientation_objects_after_future_reception": (
            max_local_orientation_objects_after_future_reception
        ),
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return request
