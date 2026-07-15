"""Resolve one local relevance medium second bounded relevance reception object.

This resolver reads one clean local relevance medium successor candidate
admission artifact and records one second bounded relevance reception object
only. It receives the admitted successor candidate once as bounded relevance
material; it does not create repeated reception permission, arbitrary
reception, feed, second receipt, second orientation view, second index entry,
local medium multiplicity result, relation view, comparison view, index system,
registry, search, ranking, source, authority, currentness, action,
synchronization, runtime permission, public API, distributed behavior,
operation permission, or follow-on work.
"""

from __future__ import annotations

import copy
import json
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class LocalRelevanceMediumSecondBoundedRelevanceReceptionV0MinError(Exception):
    """Bounded error for second-reception resolver path loading."""


RESULT_VERSION = "0.1.0"
RESOLVER_MODULE = "resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min"

OUTCOME_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_RECORDED"
OUTCOME_NOT_RECORDED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED"
OUTCOME_REQUIRES_ADDITIONAL_BASIS = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUIRES_ADDITIONAL_BASIS"
)
OUTCOME_BLOCKED = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BLOCKED"
OUTCOME_FAMILY = (
    OUTCOME_RECORDED,
    OUTCOME_NOT_RECORDED,
    OUTCOME_REQUIRES_ADDITIONAL_BASIS,
    OUTCOME_BLOCKED,
)

OUTPUT_ROOT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_second_bounded_relevance_reception_v0_min"
)
DEFAULT_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT = Path(
    "artifacts/"
    "integrity_host_v0_min_coexistence_local_relevance_medium_successor_candidate_admission_v0_min/"
    "local_relevance_medium_successor_candidate_admission_reference_review_001__"
    "local_relevance_medium_successor_candidate_admission_v0_min_result.json"
)

SECOND_RECEPTION_TYPE = "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
SECOND_RECEPTION_SCOPE = "SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY"
SUCCESSOR_CANDIDATE_ADMISSION_TYPE = "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION"
SUCCESSOR_CANDIDATE_ADMISSION_SCOPE = "ONE_SUCCESSOR_CANDIDATE_ADMISSION_ONLY"
SUCCESSOR_CANDIDATE_ADMISSION_RECORDED_OUTCOME = (
    "LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION_RECORDED"
)
SUCCESSOR_CANDIDATE_SCOPE = "BOUNDED_RELEVANCE_RECEPTION_CANDIDATE_ONLY"
CANDIDATE_ADMISSION_STATUS = "ADMITTED_AS_SUCCESSOR_RECEPTION_CANDIDATE_ONLY"
FUTURE_SECOND_RECEPTION_SCOPE = "FUTURE_SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY"
MULTIPLICITY_PURPOSE = "LOCAL_MEDIUM_MULTIPLICITY_TEST_ONLY"

DEFAULT_SECOND_RECEIVED_SIGNAL_ID = "bounded_relevance_signal_002"
DEFAULT_SECOND_RELEVANCE_BASIS_ID = "bounded_relevance_basis_002"
DEFAULT_SECOND_RELEVANCE_SCOPE_ID = "bounded_relevance_scope_002"
DEFAULT_SECOND_CARRIER_CONTEXT_ID = "bounded_relevance_signal_carrier_context_002"
DEFAULT_SECOND_RECEPTION_ENVELOPE_ID = "bounded_relevance_reception_envelope_002"

SUPPORTED_SECOND_RECEPTION_SCOPE_VALUES = (SECOND_RECEPTION_SCOPE,)
SUPPORTED_SECOND_RECEPTION_TYPE_VALUES = (SECOND_RECEPTION_TYPE,)
SUPPORTED_SUCCESSOR_CANDIDATE_SCOPE_VALUES = (SUCCESSOR_CANDIDATE_SCOPE,)
SUPPORTED_CANDIDATE_ADMISSION_STATUS_VALUES = (CANDIDATE_ADMISSION_STATUS,)
SUPPORTED_MULTIPLICITY_PURPOSE_VALUES = (MULTIPLICITY_PURPOSE,)

INTENT_RECORD = "RECORD_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
INTENT_DO_NOT_RECORD = "DO_NOT_RECORD_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
INTENT_BLOCK = "BLOCK_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION"
SUPPORTED_INTENTS = (INTENT_RECORD, INTENT_DO_NOT_RECORD, INTENT_BLOCK)

REQUIRED_FALSE_NON_CLAIMS = (
    "repeated_reception_permission_created",
    "arbitrary_reception_created",
    "feed_created",
    "second_receipt_created",
    "second_orientation_view_created",
    "second_index_entry_created",
    "local_medium_multiplicity_result_created",
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
    "artifact_existence_treated_as_second_reception_authority",
    "latest_file_posture_treated_as_second_reception_authority",
    "repo_local_availability_treated_as_second_reception_authority",
    "hidden_repo_state_used_as_second_reception_content",
    "hidden_repo_state_used_as_second_reception_authority",
    "prior_artifacts_mutated",
    "predecessor_failure_repaired",
    "predecessor_failure_hidden",
    "predecessor_failure_claimed_passed",
    "consumed_request_reopened",
    "authorization_token_reused",
)

ALLOWED_TRUE_RECORDED_FIELDS = (
    "local_relevance_medium_second_bounded_relevance_reception_recorded",
    "basis_successor_candidate_admission_artifact_preserved",
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
    "admitted_successor_candidate_id_preserved",
    "second_received_signal_id_declared",
    "second_received_signal_differs_from_existing_signal",
    "second_relevance_basis_id_declared",
    "second_relevance_scope_id_declared",
    "second_carrier_context_id_declared",
    "second_reception_envelope_id_declared",
    "second_reception_scope_second_only",
    "multiplicity_purpose_local_only",
    "max_local_orientation_objects_after_second_reception_is_two",
    "result_level_non_claims_canonical_false",
)

BLOCK_CODES = (
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
    "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BLOCK_REQUESTED",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_PATH_MISSING",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_UNREADABLE",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_RECORDED",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
    "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_VERSION_NOT_0_1_0",
    "SUCCESSOR_CANDIDATE_ADMISSION_OBJECT_MISSING",
    "ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION",
    "ADMISSION_SCOPE_NOT_ONE_CANDIDATE_ONLY",
    "BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_MISSING",
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
    "CANDIDATE_ADMISSION_STATUS_NOT_CANDIDATE_ONLY",
    "FUTURE_SECOND_RECEPTION_SCOPE_NOT_BOUNDED_ONLY",
    "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
    "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO",
    "SECOND_RECEPTION_SCOPE_MISSING",
    "SECOND_RECEPTION_SCOPE_NOT_SECOND_ONLY",
    "SECOND_RECEPTION_TYPE_MISSING",
    "SECOND_RECEPTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
    "ADMITTED_SUCCESSOR_CANDIDATE_ID_MISSING",
    "ADMITTED_SUCCESSOR_CANDIDATE_ID_DIFFERS_FROM_SUCCESSOR_CANDIDATE_ID",
    "SECOND_RECEIVED_SIGNAL_ID_MISSING",
    "SECOND_RECEIVED_SIGNAL_ID_EQUALS_EXISTING_SIGNAL",
    "SECOND_RELEVANCE_BASIS_ID_MISSING",
    "SECOND_RELEVANCE_SCOPE_ID_MISSING",
    "SECOND_CARRIER_CONTEXT_ID_MISSING",
    "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
    "SECOND_BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED",
    "REPEATED_RECEPTION_PERMISSION_CREATED",
    "ARBITRARY_RECEPTION_CREATED",
    "FEED_CREATED",
    "SECOND_RECEIPT_CREATED",
    "SECOND_ORIENTATION_VIEW_CREATED",
    "SECOND_INDEX_ENTRY_CREATED",
    "LOCAL_MEDIUM_MULTIPLICITY_RESULT_CREATED",
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
    "DERIVATIVE_RECEPTION_AUTHORIZED",
    "VESSEL_RELATION_AUTHORIZED",
    "ADOPTION_CREATED",
    "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    "PUBLICATION_FLOW_CREATED",
    "FOLLOW_ON_WORK_AUTHORIZED",
    "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    "LATEST_FILE_POSTURE_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_CONTENT",
    "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_AUTHORITY",
    "PREDECESSOR_FAILURE_EVIDENCE_HIDDEN_OR_REPAIRED",
    "CONSUMED_REQUEST_REOPENED",
    "AUTHORIZATION_TOKEN_REUSED",
    "PRIOR_ARTIFACTS_MUTATED",
    "NON_CLAIM_MISSING_OR_FLIPPED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
    "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_UNREADABLE",
)

SENSITIVE_CONTENT_KEYS = {
    "raw_body",
    "raw_full_body",
    "full_body",
    "artifact_body",
    "raw_second_reception_body",
    "raw_second_bounded_relevance_reception_body",
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
    "second_reception_body",
    "second_bounded_relevance_reception_body",
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
    "RAW_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BODY_MUST_NOT_RETURN",
    "RAW_SECOND_RECEPTION_BODY_MUST_NOT_RETURN",
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
    (
        "repeated_reception_permission_created",
        "repeated reception permission not created",
        "REPEATED_RECEPTION_PERMISSION_CREATED",
    ),
    ("arbitrary_reception_created", "arbitrary reception not created", "ARBITRARY_RECEPTION_CREATED"),
    ("feed_created", "feed not created", "FEED_CREATED"),
    ("second_receipt_created", "second receipt not created", "SECOND_RECEIPT_CREATED"),
    ("second_orientation_view_created", "second orientation view not created", "SECOND_ORIENTATION_VIEW_CREATED"),
    ("second_index_entry_created", "second index entry not created", "SECOND_INDEX_ENTRY_CREATED"),
    (
        "local_medium_multiplicity_result_created",
        "local medium multiplicity result not created",
        "LOCAL_MEDIUM_MULTIPLICITY_RESULT_CREATED",
    ),
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
    (
        "derivative_reception_authorized",
        "derivative reception not authorized",
        "DERIVATIVE_RECEPTION_AUTHORIZED",
    ),
    ("vessel_relation_authorized", "vessel relation not authorized", "VESSEL_RELATION_AUTHORIZED"),
    ("adoption_created", "adoption not created", "ADOPTION_CREATED"),
    (
        "receiving_context_governance_created",
        "receiving-context governance not created",
        "RECEIVING_CONTEXT_GOVERNANCE_CREATED",
    ),
    ("publication_flow_created", "publication flow not created", "PUBLICATION_FLOW_CREATED"),
    ("follow_on_work_authorized", "follow-on work not authorized", "FOLLOW_ON_WORK_AUTHORIZED"),
    (
        "artifact_existence_treated_as_second_reception_authority",
        "artifact existence not second-reception authority",
        "ARTIFACT_EXISTENCE_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    ),
    (
        "latest_file_posture_treated_as_second_reception_authority",
        "latest file posture not second-reception authority",
        "LATEST_FILE_POSTURE_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    ),
    (
        "repo_local_availability_treated_as_second_reception_authority",
        "repo-local availability not second-reception authority",
        "REPO_LOCAL_AVAILABILITY_TREATED_AS_SECOND_RECEPTION_AUTHORITY",
    ),
    (
        "hidden_repo_state_used_as_second_reception_content",
        "hidden repo state not second-reception content",
        "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_CONTENT",
    ),
    (
        "hidden_repo_state_used_as_second_reception_authority",
        "hidden repo state not second-reception authority",
        "HIDDEN_REPO_STATE_USED_AS_SECOND_RECEPTION_AUTHORITY",
    ),
    ("consumed_request_reopened", "consumed request not reopened", "CONSUMED_REQUEST_REOPENED"),
    ("authorization_token_reused", "authorization token not reused", "AUTHORIZATION_TOKEN_REUSED"),
    ("prior_artifacts_mutated", "prior artifacts not mutated", "PRIOR_ARTIFACTS_MUTATED"),
)

WHAT_REMAINS_OPEN = (
    "second_bounded_relevance_receipt",
    "second_relevance_orientation_view",
    "second_local_relevance_orientation_index_entry",
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
    "repeated_reception_permission",
    "arbitrary_reception",
    "feed",
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
        return None, "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_PATH_MISSING"
    path = Path(str(path_value))
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError):
        return None, "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_UNREADABLE"
    if not isinstance(payload, Mapping):
        return None, "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT"
    return dict(payload), None


def _extract_failed_check_count_from_artifact(artifact: Mapping[str, Any]) -> int | None:
    metadata = _as_mapping(artifact.get("local_relevance_medium_successor_candidate_admission_metadata"))
    summary = _as_mapping(artifact.get("local_relevance_medium_successor_candidate_admission_summary"))
    value = _first_present(
        metadata.get("failed_check_count"),
        summary.get("failed_check_count"),
        artifact.get("failed_check_count"),
    )
    if value is None:
        checks = artifact.get("local_relevance_medium_successor_candidate_admission_checks")
        if isinstance(checks, list):
            return sum(1 for check in checks if isinstance(check, Mapping) and check.get("passed") is False)
    return _coerce_int(value)


def _extract_successor_candidate_admission_facts(
    artifact: Mapping[str, Any] | None,
    selected_artifact_path: Any,
) -> dict[str, Any]:
    if artifact is None:
        return {
            "basis_successor_candidate_admission_artifact": str(selected_artifact_path)
            if _is_declared(selected_artifact_path)
            else None,
            "admission_object_present": False,
        }

    metadata = _as_mapping(artifact.get("local_relevance_medium_successor_candidate_admission_metadata"))
    summary = _as_mapping(artifact.get("local_relevance_medium_successor_candidate_admission_summary"))
    admission_object = _as_mapping(artifact.get("successor_candidate_admission_object"))

    result_version = _first_present(
        metadata.get("local_relevance_medium_successor_candidate_admission_version"),
        metadata.get("result_version"),
        summary.get("result_version"),
        admission_object.get("admission_version"),
        artifact.get("result_version"),
    )
    failed_check_count = _extract_failed_check_count_from_artifact(artifact)

    return {
        "basis_successor_candidate_admission_artifact": str(selected_artifact_path)
        if _is_declared(selected_artifact_path)
        else None,
        "basis_successor_candidate_admission_outcome": artifact.get("outcome"),
        "basis_successor_candidate_admission_result_version": result_version,
        "basis_successor_candidate_admission_failed_check_count": failed_check_count,
        "admission_object_present": bool(admission_object),
        "successor_candidate_admission_object": _sanitize(admission_object),
        "admission_type": admission_object.get("admission_type"),
        "admission_scope": admission_object.get("admission_scope"),
        "basis_successor_reception_request_artifact": admission_object.get(
            "basis_successor_reception_request_artifact"
        ),
        "basis_index_entry_artifact": admission_object.get("basis_index_entry_artifact"),
        "existing_orientation_view_artifact": admission_object.get("existing_orientation_view_artifact"),
        "existing_source_receipt_artifact": admission_object.get("existing_source_receipt_artifact"),
        "existing_referenced_reception_artifact": admission_object.get("existing_referenced_reception_artifact"),
        "existing_received_signal_id": admission_object.get("existing_received_signal_id"),
        "existing_received_relevance_basis_id": admission_object.get("existing_received_relevance_basis_id"),
        "existing_received_relevance_scope_id": admission_object.get("existing_received_relevance_scope_id"),
        "existing_received_carrier_context_id": admission_object.get("existing_received_carrier_context_id"),
        "existing_received_reception_envelope_id": admission_object.get(
            "existing_received_reception_envelope_id"
        ),
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
    }


def _build_second_bounded_relevance_reception_object(
    facts: Mapping[str, Any],
    request: Mapping[str, Any],
) -> dict[str, Any]:
    return {
        "second_reception_id": "local_relevance_medium_second_bounded_relevance_reception_001",
        "second_reception_type": SECOND_RECEPTION_TYPE,
        "second_reception_version": RESULT_VERSION,
        "second_reception_scope": SECOND_RECEPTION_SCOPE,
        "basis_successor_candidate_admission_artifact": facts.get(
            "basis_successor_candidate_admission_artifact"
        ),
        "basis_successor_candidate_admission_outcome": facts.get(
            "basis_successor_candidate_admission_outcome"
        ),
        "basis_successor_candidate_admission_result_version": facts.get(
            "basis_successor_candidate_admission_result_version"
        ),
        "basis_successor_candidate_admission_failed_check_count": facts.get(
            "basis_successor_candidate_admission_failed_check_count"
        ),
        "basis_successor_reception_request_artifact": facts.get(
            "basis_successor_reception_request_artifact"
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
        "admitted_successor_candidate_id": facts.get("successor_candidate_id"),
        "admitted_successor_candidate_scope": SUCCESSOR_CANDIDATE_SCOPE,
        "candidate_admission_status": CANDIDATE_ADMISSION_STATUS,
        "second_received_signal_id": request.get("second_received_signal_id"),
        "second_relevance_basis_id": request.get("second_relevance_basis_id"),
        "second_relevance_scope_id": request.get("second_relevance_scope_id"),
        "second_carrier_context_id": request.get("second_carrier_context_id"),
        "second_reception_envelope_id": request.get("second_reception_envelope_id"),
        "multiplicity_purpose": MULTIPLICITY_PURPOSE,
        "max_local_orientation_objects_after_second_reception": 2,
        "second_bounded_relevance_reception_recorded": True,
        "repeated_reception_permission_created": False,
        "arbitrary_reception_created": False,
        "feed_created": False,
        "second_receipt_created": False,
        "second_orientation_view_created": False,
        "second_index_entry_created": False,
        "local_medium_multiplicity_result_created": False,
        "relation_view_created": False,
        "comparison_view_created": False,
        "index_system_created": False,
        "registry_created": False,
        "search_surface_created": False,
        "ranking_surface_created": False,
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


def _build_checks(
    request: Mapping[str, Any],
    facts: Mapping[str, Any],
    artifact_payload: Mapping[str, Any] | None,
    artifact_read_error: str | None,
) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []
    question = request.get("local_relevance_medium_second_bounded_relevance_reception_question")
    intent = request.get("local_relevance_medium_second_bounded_relevance_reception_intent")
    artifact_path = request.get("selected_successor_candidate_admission_artifact")
    second_scope = request.get("second_reception_scope")
    second_type = request.get("second_reception_type")
    second_signal_id = request.get("second_received_signal_id")
    second_basis_id = request.get("second_relevance_basis_id")
    second_scope_id = request.get("second_relevance_scope_id")
    second_carrier_id = request.get("second_carrier_context_id")
    second_envelope_id = request.get("second_reception_envelope_id")
    multiplicity_purpose = request.get("multiplicity_purpose")
    max_after_second = request.get("max_local_orientation_objects_after_second_reception")
    declared_non_claims = request.get("declared_non_claims")

    checks.append(
        _check(
            "second reception question declared",
            _is_declared(question),
            "declared second reception question",
            question,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_QUESTION_UNDECLARED",
        )
    )
    checks.append(
        _check(
            "intent supported",
            intent in SUPPORTED_INTENTS,
            SUPPORTED_INTENTS,
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_INTENT_UNSUPPORTED",
        )
    )
    checks.append(
        _check(
            "block intent not requested",
            intent != INTENT_BLOCK,
            "intent other than explicit block",
            intent,
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_BLOCK_REQUESTED",
        )
    )
    checks.append(
        _check(
            "selected successor candidate admission artifact path declared",
            _is_declared(artifact_path)
            and request.get("selected_successor_candidate_admission_artifact_missing") is not True,
            "declared successor candidate admission artifact path",
            artifact_path,
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_PATH_MISSING",
        )
    )
    checks.append(
        _check(
            "selected successor candidate admission artifact readable JSON",
            artifact_read_error
            not in {
                "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_UNREADABLE",
                "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_PATH_MISSING",
            },
            "readable JSON object",
            artifact_read_error or "readable",
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_UNREADABLE",
        )
    )
    checks.append(
        _check(
            "selected successor candidate admission artifact JSON object",
            artifact_read_error != "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
            "JSON object",
            artifact_read_error or ("JSON object" if artifact_payload is not None else None),
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_JSON_OBJECT",
        )
    )
    checks.append(
        _check(
            "successor candidate admission artifact outcome recorded",
            facts.get("basis_successor_candidate_admission_outcome")
            == SUCCESSOR_CANDIDATE_ADMISSION_RECORDED_OUTCOME
            and request.get("selected_successor_candidate_admission_artifact_not_recorded") is not True,
            SUCCESSOR_CANDIDATE_ADMISSION_RECORDED_OUTCOME,
            facts.get("basis_successor_candidate_admission_outcome"),
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_NOT_RECORDED",
        )
    )
    checks.append(
        _check(
            "successor candidate admission artifact result version 0.1.0",
            facts.get("basis_successor_candidate_admission_result_version") == RESULT_VERSION
            and request.get("selected_successor_candidate_admission_artifact_version_not_0_1_0")
            is not True,
            RESULT_VERSION,
            facts.get("basis_successor_candidate_admission_result_version"),
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_VERSION_NOT_0_1_0",
        )
    )
    checks.append(
        _check(
            "successor candidate admission artifact failed check count zero",
            facts.get("basis_successor_candidate_admission_failed_check_count") == 0
            and request.get("selected_successor_candidate_admission_artifact_failed_checks_present")
            is not True,
            0,
            facts.get("basis_successor_candidate_admission_failed_check_count"),
            "SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT_FAILED_CHECKS_PRESENT",
        )
    )
    checks.append(
        _check(
            "successor candidate admission object present",
            facts.get("admission_object_present") is True
            and request.get("successor_candidate_admission_object_missing") is not True,
            "successor_candidate_admission_object present",
            facts.get("admission_object_present"),
            "SUCCESSOR_CANDIDATE_ADMISSION_OBJECT_MISSING",
        )
    )
    checks.append(
        _check(
            "admission type exact",
            facts.get("admission_type") == SUCCESSOR_CANDIDATE_ADMISSION_TYPE
            and request.get("admission_type_not_successor_candidate_admission") is not True,
            SUCCESSOR_CANDIDATE_ADMISSION_TYPE,
            facts.get("admission_type"),
            "ADMISSION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION",
        )
    )
    checks.append(
        _check(
            "admission scope one candidate only",
            facts.get("admission_scope") == SUCCESSOR_CANDIDATE_ADMISSION_SCOPE
            and request.get("admission_scope_not_one_candidate_only") is not True,
            SUCCESSOR_CANDIDATE_ADMISSION_SCOPE,
            facts.get("admission_scope"),
            "ADMISSION_SCOPE_NOT_ONE_CANDIDATE_ONLY",
        )
    )

    basis_presence = (
        (
            "basis successor reception request artifact present",
            "basis_successor_reception_request_artifact",
            "basis_successor_reception_request_artifact_missing",
            "BASIS_SUCCESSOR_RECEPTION_REQUEST_ARTIFACT_MISSING",
        ),
        (
            "basis index entry artifact present",
            "basis_index_entry_artifact",
            "basis_index_entry_artifact_missing",
            "BASIS_INDEX_ENTRY_ARTIFACT_MISSING",
        ),
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
            facts.get("successor_candidate_scope") == SUCCESSOR_CANDIDATE_SCOPE
            and request.get("successor_candidate_scope_not_bounded_only") is not True,
            SUCCESSOR_CANDIDATE_SCOPE,
            facts.get("successor_candidate_scope"),
            "SUCCESSOR_CANDIDATE_SCOPE_NOT_BOUNDED_ONLY",
        )
    )
    checks.append(
        _check(
            "candidate admission status candidate only",
            facts.get("candidate_admission_status") == CANDIDATE_ADMISSION_STATUS
            and request.get("candidate_admission_status_not_candidate_only") is not True,
            CANDIDATE_ADMISSION_STATUS,
            facts.get("candidate_admission_status"),
            "CANDIDATE_ADMISSION_STATUS_NOT_CANDIDATE_ONLY",
        )
    )
    checks.append(
        _check(
            "future second reception scope bounded only",
            facts.get("future_second_reception_scope") == FUTURE_SECOND_RECEPTION_SCOPE
            and request.get("future_second_reception_scope_not_bounded_only") is not True,
            FUTURE_SECOND_RECEPTION_SCOPE,
            facts.get("future_second_reception_scope"),
            "FUTURE_SECOND_RECEPTION_SCOPE_NOT_BOUNDED_ONLY",
        )
    )
    checks.append(
        _check(
            "multiplicity purpose local only",
            facts.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE
            and multiplicity_purpose == MULTIPLICITY_PURPOSE,
            MULTIPLICITY_PURPOSE,
            {
                "declared_multiplicity_purpose": multiplicity_purpose,
                "admission_artifact_multiplicity_purpose": facts.get("multiplicity_purpose"),
            },
            "MULTIPLICITY_PURPOSE_NOT_LOCAL_ONLY",
        )
    )
    checks.append(
        _check(
            "max local orientation objects after future reception is two",
            _coerce_int(facts.get("max_local_orientation_objects_after_future_reception")) == 2,
            2,
            facts.get("max_local_orientation_objects_after_future_reception"),
            "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO",
        )
    )
    checks.append(
        _check(
            "second reception type declared",
            _is_declared(second_type),
            "declared second reception type",
            second_type,
            "SECOND_RECEPTION_TYPE_MISSING",
        )
    )
    checks.append(
        _check(
            "second reception type exact",
            second_type == SECOND_RECEPTION_TYPE,
            SECOND_RECEPTION_TYPE,
            second_type,
            "SECOND_RECEPTION_TYPE_NOT_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION",
        )
    )
    checks.append(
        _check(
            "second reception scope declared",
            _is_declared(second_scope),
            "declared second reception scope",
            second_scope,
            "SECOND_RECEPTION_SCOPE_MISSING",
        )
    )
    checks.append(
        _check(
            "second reception scope second only",
            second_scope == SECOND_RECEPTION_SCOPE,
            SECOND_RECEPTION_SCOPE,
            second_scope,
            "SECOND_RECEPTION_SCOPE_NOT_SECOND_ONLY",
        )
    )

    declared_admitted_candidate_id = request.get("admitted_successor_candidate_id", successor_candidate_id)
    checks.append(
        _check(
            "admitted successor candidate id preserved",
            _is_declared(declared_admitted_candidate_id)
            and request.get("admitted_successor_candidate_id_missing") is not True,
            "admitted successor candidate id declared from admission artifact",
            declared_admitted_candidate_id,
            "ADMITTED_SUCCESSOR_CANDIDATE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "admitted successor candidate id corresponds to successor candidate id",
            _is_declared(declared_admitted_candidate_id)
            and declared_admitted_candidate_id == successor_candidate_id
            and request.get("admitted_successor_candidate_id_differs_from_successor_candidate_id")
            is not True,
            "admitted successor candidate id equals successor candidate id",
            {
                "admitted_successor_candidate_id": declared_admitted_candidate_id,
                "successor_candidate_id": successor_candidate_id,
            },
            "ADMITTED_SUCCESSOR_CANDIDATE_ID_DIFFERS_FROM_SUCCESSOR_CANDIDATE_ID",
        )
    )
    checks.append(
        _check(
            "second received signal id declared",
            _is_declared(second_signal_id) and request.get("second_received_signal_id_missing") is not True,
            "declared second received signal id",
            second_signal_id,
            "SECOND_RECEIVED_SIGNAL_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second received signal differs from existing signal",
            _is_declared(second_signal_id)
            and _is_declared(existing_signal_id)
            and second_signal_id != existing_signal_id
            and request.get("second_received_signal_id_equals_existing_signal") is not True,
            "second received signal id distinct from existing received signal id",
            {"second_received_signal_id": second_signal_id, "existing_received_signal_id": existing_signal_id},
            "SECOND_RECEIVED_SIGNAL_ID_EQUALS_EXISTING_SIGNAL",
        )
    )
    checks.append(
        _check(
            "second relevance basis id declared",
            _is_declared(second_basis_id) and request.get("second_relevance_basis_id_missing") is not True,
            "declared second relevance basis id",
            second_basis_id,
            "SECOND_RELEVANCE_BASIS_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second relevance scope id declared",
            _is_declared(second_scope_id) and request.get("second_relevance_scope_id_missing") is not True,
            "declared second relevance scope id",
            second_scope_id,
            "SECOND_RELEVANCE_SCOPE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second carrier context id declared",
            _is_declared(second_carrier_id) and request.get("second_carrier_context_id_missing") is not True,
            "declared second carrier context id",
            second_carrier_id,
            "SECOND_CARRIER_CONTEXT_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "second reception envelope id declared",
            _is_declared(second_envelope_id) and request.get("second_reception_envelope_id_missing") is not True,
            "declared second reception envelope id",
            second_envelope_id,
            "SECOND_RECEPTION_ENVELOPE_ID_MISSING",
        )
    )
    checks.append(
        _check(
            "max local orientation objects after second reception is two",
            _coerce_int(max_after_second) == 2,
            2,
            max_after_second,
            "MAX_LOCAL_ORIENTATION_OBJECTS_AFTER_FUTURE_RECEPTION_NOT_TWO",
        )
    )
    checks.append(
        _check(
            "second bounded relevance reception recorded",
            request.get("second_bounded_relevance_reception_not_recorded") is not True
            and facts.get("successor_candidate_admitted_as_candidate") is True,
            "second bounded relevance reception recorded from admitted candidate",
            {
                "second_bounded_relevance_reception_not_recorded": request.get(
                    "second_bounded_relevance_reception_not_recorded"
                ),
                "successor_candidate_admitted_as_candidate": facts.get(
                    "successor_candidate_admitted_as_candidate"
                ),
            },
            "SECOND_BOUNDED_RELEVANCE_RECEPTION_NOT_RECORDED",
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
        return OUTCOME_BLOCKED, first_code, "second bounded relevance reception request blocked by failed check"

    requested_outcome = request.get("requested_local_relevance_medium_second_bounded_relevance_reception_outcome")
    if requested_outcome == OUTCOME_REQUIRES_ADDITIONAL_BASIS:
        return OUTCOME_REQUIRES_ADDITIONAL_BASIS, None, None
    if requested_outcome == OUTCOME_NOT_RECORDED:
        return OUTCOME_NOT_RECORDED, None, None
    if request.get("local_relevance_medium_second_bounded_relevance_reception_intent") == INTENT_DO_NOT_RECORD:
        return OUTCOME_NOT_RECORDED, None, None
    return OUTCOME_RECORDED, None, None


def _build_non_meaning() -> dict[str, Any]:
    return {
        "second_reception_is_not": (
            "repeated_reception_permission",
            "arbitrary_reception",
            "feed",
            "second_receipt",
            "second_orientation_view",
            "second_index_entry",
            "local_medium_multiplicity_result",
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
        "second_reception_only": True,
    }


def _build_artifact_basis(facts: Mapping[str, Any], artifact_read_error: str | None) -> dict[str, Any]:
    return {
        "selected_successor_candidate_admission_artifact": facts.get(
            "basis_successor_candidate_admission_artifact"
        ),
        "read_error": artifact_read_error,
        "basis_successor_candidate_admission_outcome": facts.get(
            "basis_successor_candidate_admission_outcome"
        ),
        "basis_successor_candidate_admission_result_version": facts.get(
            "basis_successor_candidate_admission_result_version"
        ),
        "basis_successor_candidate_admission_failed_check_count": facts.get(
            "basis_successor_candidate_admission_failed_check_count"
        ),
        "successor_candidate_admission_object_present": facts.get("admission_object_present"),
        "admission_type": facts.get("admission_type"),
        "admission_scope": facts.get("admission_scope"),
        "basis_successor_reception_request_artifact": facts.get(
            "basis_successor_reception_request_artifact"
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
        "successor_candidate_scope": facts.get("successor_candidate_scope"),
        "candidate_admission_status": facts.get("candidate_admission_status"),
        "future_second_reception_scope": facts.get("future_second_reception_scope"),
        "multiplicity_purpose": facts.get("multiplicity_purpose"),
        "max_local_orientation_objects_after_future_reception": facts.get(
            "max_local_orientation_objects_after_future_reception"
        ),
    }


def _facts_are_sufficient(facts: Mapping[str, Any]) -> bool:
    required_keys = (
        "basis_successor_candidate_admission_artifact",
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
        facts.get("basis_successor_candidate_admission_outcome")
        == SUCCESSOR_CANDIDATE_ADMISSION_RECORDED_OUTCOME
        and facts.get("basis_successor_candidate_admission_result_version") == RESULT_VERSION
        and facts.get("basis_successor_candidate_admission_failed_check_count") == 0
        and facts.get("admission_type") == SUCCESSOR_CANDIDATE_ADMISSION_TYPE
        and facts.get("admission_scope") == SUCCESSOR_CANDIDATE_ADMISSION_SCOPE
        and facts.get("successor_candidate_scope") == SUCCESSOR_CANDIDATE_SCOPE
        and facts.get("candidate_admission_status") == CANDIDATE_ADMISSION_STATUS
        and facts.get("future_second_reception_scope") == FUTURE_SECOND_RECEPTION_SCOPE
        and facts.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE
        and _coerce_int(facts.get("max_local_orientation_objects_after_future_reception")) == 2
        and facts.get("successor_candidate_admitted_as_candidate") is True
        and facts.get("successor_candidate_id") != facts.get("existing_received_signal_id")
    )


def _second_reception_shape_supported(request: Mapping[str, Any], facts: Mapping[str, Any]) -> bool:
    return (
        request.get("second_reception_type") == SECOND_RECEPTION_TYPE
        and request.get("second_reception_scope") == SECOND_RECEPTION_SCOPE
        and _is_declared(request.get("second_received_signal_id"))
        and request.get("second_received_signal_id") != facts.get("existing_received_signal_id")
        and _is_declared(request.get("second_relevance_basis_id"))
        and _is_declared(request.get("second_relevance_scope_id"))
        and _is_declared(request.get("second_carrier_context_id"))
        and _is_declared(request.get("second_reception_envelope_id"))
        and request.get("multiplicity_purpose") == MULTIPLICITY_PURPOSE
        and _coerce_int(request.get("max_local_orientation_objects_after_second_reception")) == 2
        and request.get("second_bounded_relevance_reception_not_recorded") is not True
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

    second_reception_id = request.get(
        "local_relevance_medium_second_bounded_relevance_reception_id",
        "local_relevance_medium_second_bounded_relevance_reception_reference_review_001",
    )
    metadata = {
        "local_relevance_medium_second_bounded_relevance_reception_id": second_reception_id,
        "local_relevance_medium_second_bounded_relevance_reception_type": SECOND_RECEPTION_TYPE,
        "local_relevance_medium_second_bounded_relevance_reception_version": RESULT_VERSION,
        "local_relevance_medium_second_bounded_relevance_reception_intent": request.get(
            "local_relevance_medium_second_bounded_relevance_reception_intent"
        ),
        "generated_at": _utc_now(),
        "resolver_module": RESOLVER_MODULE,
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
    }

    result: dict[str, Any] = {
        "local_relevance_medium_second_bounded_relevance_reception_metadata": metadata,
        "declared_local_relevance_medium_second_bounded_relevance_reception_question": _sanitize(
            request.get("local_relevance_medium_second_bounded_relevance_reception_question")
        ),
        "selected_successor_candidate_admission_artifact_basis": _sanitize(
            _build_artifact_basis(facts, artifact_read_error)
        ),
        "second_bounded_relevance_reception_object": _sanitize(
            _build_second_bounded_relevance_reception_object(facts, request)
            if _facts_are_sufficient(facts) and _second_reception_shape_supported(request, facts)
            else {}
        ),
        "local_relevance_medium_second_bounded_relevance_reception_checks": _sanitize(checks),
        "local_relevance_medium_second_bounded_relevance_reception_statement": _build_statement(
            recorded, result_non_claims_canonical_false
        ),
        "local_relevance_medium_second_bounded_relevance_reception_non_meaning": _build_non_meaning(),
        "additional_basis_required": _sanitize(request.get("additional_basis_context", [])),
        "not_recorded_basis": _sanitize(request.get("not_recorded_basis", [])),
        "what_remains_open": list(WHAT_REMAINS_OPEN),
        "non_claims": result_non_claims,
        "outcome": outcome,
        "block": _build_block(outcome, block_code, block_reason),
    }
    result["local_relevance_medium_second_bounded_relevance_reception_summary"] = (
        build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(result)
    )
    return _sanitize(result)


def _malformed_request_result(code: str, reason: str, actual: Any) -> dict[str, Any]:
    request = {
        "local_relevance_medium_second_bounded_relevance_reception_id": (
            "local_relevance_medium_second_bounded_relevance_reception_malformed_001"
        ),
        "local_relevance_medium_second_bounded_relevance_reception_question": None,
        "local_relevance_medium_second_bounded_relevance_reception_intent": None,
        "selected_successor_candidate_admission_artifact": None,
        "declared_non_claims": {},
    }
    facts = _extract_successor_candidate_admission_facts(None, None)
    checks = [
        _check(
            "declared local relevance medium second bounded relevance reception request mapping",
            False,
            "mapping request",
            type(actual).__name__,
            code,
        )
    ]
    return _assemble_result(request, facts, checks, OUTCOME_BLOCKED, code, reason, None)


def resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(
    declared_local_relevance_medium_second_bounded_relevance_reception: Mapping[str, Any] | None = None,
) -> dict:
    """Resolve one second bounded relevance reception request into a bounded result."""

    if declared_local_relevance_medium_second_bounded_relevance_reception is None:
        request = build_declared_local_relevance_medium_second_bounded_relevance_reception_v0_min_request()
    elif not isinstance(declared_local_relevance_medium_second_bounded_relevance_reception, Mapping):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
            "declared second bounded relevance reception request was not a mapping",
            declared_local_relevance_medium_second_bounded_relevance_reception,
        )
    else:
        request = copy.deepcopy(dict(declared_local_relevance_medium_second_bounded_relevance_reception))

    if _contains_hostile_sentinel(request):
        request = _sanitize(request)

    artifact_path = request.get("selected_successor_candidate_admission_artifact")
    artifact_payload, artifact_read_error = _read_json_object(artifact_path)
    if artifact_payload is not None and _contains_hostile_sentinel(artifact_payload):
        artifact_payload = _sanitize(artifact_payload)
    facts = _extract_successor_candidate_admission_facts(artifact_payload, artifact_path)
    checks = _build_checks(request, facts, artifact_payload, artifact_read_error)
    outcome, block_code, block_reason = _select_outcome_and_block(request, checks)
    return _assemble_result(request, facts, checks, outcome, block_code, block_reason, artifact_read_error)


def resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min_from_path(
    declared_local_relevance_medium_second_bounded_relevance_reception_path: Path | str,
) -> dict:
    """Load a declared second bounded relevance reception request from JSON and resolve it."""

    path = Path(declared_local_relevance_medium_second_bounded_relevance_reception_path)
    try:
        with path.open("r", encoding="utf-8") as handle:
            payload = json.load(handle)
    except (OSError, json.JSONDecodeError) as exc:
        raise LocalRelevanceMediumSecondBoundedRelevanceReceptionV0MinError(
            "declared local relevance medium second bounded relevance reception request unreadable"
        ) from exc
    if not isinstance(payload, Mapping):
        return _malformed_request_result(
            "DECLARED_LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION_REQUEST_MALFORMED",
            "declared second bounded relevance reception request JSON was not an object",
            payload,
        )
    return resolve_local_relevance_medium_second_bounded_relevance_reception_v0_min(payload)


def build_local_relevance_medium_second_bounded_relevance_reception_v0_min_summary(
    result: Mapping[str, Any],
) -> dict:
    """Build the compact public summary for a second bounded relevance reception result."""

    metadata = _as_mapping(result.get("local_relevance_medium_second_bounded_relevance_reception_metadata"))
    statement = _as_mapping(
        result.get("local_relevance_medium_second_bounded_relevance_reception_statement")
    )
    second_reception_object = _as_mapping(result.get("second_bounded_relevance_reception_object"))
    block = _as_mapping(result.get("block"))
    non_claims = _as_mapping(result.get("non_claims"))
    checks = result.get("local_relevance_medium_second_bounded_relevance_reception_checks", [])
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
        "second_reception_id": metadata.get("local_relevance_medium_second_bounded_relevance_reception_id"),
        "question": result.get(
            "declared_local_relevance_medium_second_bounded_relevance_reception_question"
        ),
        "intent": metadata.get("local_relevance_medium_second_bounded_relevance_reception_intent"),
        "passed_check_count": passed_check_count,
        "failed_check_count": failed_check_count,
        "result_version": metadata.get("local_relevance_medium_second_bounded_relevance_reception_version"),
        "resolver_module": metadata.get("resolver_module"),
        "local_relevance_medium_second_bounded_relevance_reception_recorded": statement.get(
            "local_relevance_medium_second_bounded_relevance_reception_recorded", False
        ),
        "basis_successor_candidate_admission_artifact_preserved": statement.get(
            "basis_successor_candidate_admission_artifact_preserved", False
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
        "admitted_successor_candidate_id_preserved": statement.get(
            "admitted_successor_candidate_id_preserved", False
        ),
        "second_received_signal_id_declared": statement.get(
            "second_received_signal_id_declared", False
        ),
        "second_received_signal_differs_from_existing_signal": statement.get(
            "second_received_signal_differs_from_existing_signal", False
        ),
        "second_relevance_basis_id_declared": statement.get(
            "second_relevance_basis_id_declared", False
        ),
        "second_relevance_scope_id_declared": statement.get(
            "second_relevance_scope_id_declared", False
        ),
        "second_carrier_context_id_declared": statement.get(
            "second_carrier_context_id_declared", False
        ),
        "second_reception_envelope_id_declared": statement.get(
            "second_reception_envelope_id_declared", False
        ),
        "second_reception_scope_second_only": statement.get(
            "second_reception_scope_second_only", False
        ),
        "multiplicity_purpose_local_only": statement.get("multiplicity_purpose_local_only", False),
        "max_local_orientation_objects_after_second_reception_is_two": statement.get(
            "max_local_orientation_objects_after_second_reception_is_two", False
        ),
        "second_reception_object_summary": {
            "second_reception_type": second_reception_object.get("second_reception_type"),
            "second_reception_scope": second_reception_object.get("second_reception_scope"),
            "admitted_successor_candidate_id": second_reception_object.get(
                "admitted_successor_candidate_id"
            ),
            "admitted_successor_candidate_scope": second_reception_object.get(
                "admitted_successor_candidate_scope"
            ),
            "candidate_admission_status": second_reception_object.get("candidate_admission_status"),
            "second_received_signal_id": second_reception_object.get("second_received_signal_id"),
            "second_relevance_basis_id": second_reception_object.get("second_relevance_basis_id"),
            "second_relevance_scope_id": second_reception_object.get("second_relevance_scope_id"),
            "second_carrier_context_id": second_reception_object.get("second_carrier_context_id"),
            "second_reception_envelope_id": second_reception_object.get(
                "second_reception_envelope_id"
            ),
            "multiplicity_purpose": second_reception_object.get("multiplicity_purpose"),
            "max_local_orientation_objects_after_second_reception": second_reception_object.get(
                "max_local_orientation_objects_after_second_reception"
            ),
            "second_bounded_relevance_reception_recorded": second_reception_object.get(
                "second_bounded_relevance_reception_recorded"
            ),
            "existing_received_signal_id": second_reception_object.get("existing_received_signal_id"),
        },
        "repeated_reception_permission_created": non_claims.get(
            "repeated_reception_permission_created", False
        ),
        "arbitrary_reception_created": non_claims.get("arbitrary_reception_created", False),
        "feed_created": non_claims.get("feed_created", False),
        "second_receipt_created": non_claims.get("second_receipt_created", False),
        "second_orientation_view_created": non_claims.get("second_orientation_view_created", False),
        "second_index_entry_created": non_claims.get("second_index_entry_created", False),
        "local_medium_multiplicity_result_created": non_claims.get(
            "local_medium_multiplicity_result_created", False
        ),
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
                "repeated_reception_permission_created",
                "arbitrary_reception_created",
                "feed_created",
                "second_receipt_created",
                "second_orientation_view_created",
                "second_index_entry_created",
                "local_medium_multiplicity_result_created",
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


def write_local_relevance_medium_second_bounded_relevance_reception_v0_min_result(
    result: Mapping[str, Any],
    output_path: Path | str | None = None,
) -> Path:
    """Write a second bounded relevance reception result without overwriting files."""

    metadata = _as_mapping(result.get("local_relevance_medium_second_bounded_relevance_reception_metadata"))
    second_reception_id = metadata.get(
        "local_relevance_medium_second_bounded_relevance_reception_id",
        "local_relevance_medium_second_bounded_relevance_reception_reference_review_001",
    )
    if output_path is None:
        output_dir = Path(OUTPUT_ROOT)
        base_path = output_dir / (
            f"{second_reception_id}__local_relevance_medium_second_bounded_relevance_reception_v0_min_result.json"
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


def build_declared_local_relevance_medium_second_bounded_relevance_reception_v0_min_request(
    *,
    local_relevance_medium_second_bounded_relevance_reception_id: str = (
        "local_relevance_medium_second_bounded_relevance_reception_reference_review_001"
    ),
    local_relevance_medium_second_bounded_relevance_reception_question: str | None = None,
    local_relevance_medium_second_bounded_relevance_reception_intent: str = INTENT_RECORD,
    selected_successor_candidate_admission_artifact: Path | str = (
        DEFAULT_SUCCESSOR_CANDIDATE_ADMISSION_ARTIFACT
    ),
    second_reception_scope: str = SECOND_RECEPTION_SCOPE,
    second_reception_type: str = SECOND_RECEPTION_TYPE,
    second_received_signal_id: str = DEFAULT_SECOND_RECEIVED_SIGNAL_ID,
    second_relevance_basis_id: str = DEFAULT_SECOND_RELEVANCE_BASIS_ID,
    second_relevance_scope_id: str = DEFAULT_SECOND_RELEVANCE_SCOPE_ID,
    second_carrier_context_id: str = DEFAULT_SECOND_CARRIER_CONTEXT_ID,
    second_reception_envelope_id: str = DEFAULT_SECOND_RECEPTION_ENVELOPE_ID,
    multiplicity_purpose: str = MULTIPLICITY_PURPOSE,
    max_local_orientation_objects_after_second_reception: int = 2,
    declared_non_claims: Mapping[str, Any] | None = None,
    **overrides: Any,
) -> dict[str, Any]:
    """Build a declared second reception request with canonical false non-claims."""

    if local_relevance_medium_second_bounded_relevance_reception_question is None:
        local_relevance_medium_second_bounded_relevance_reception_question = (
            "Given one clean LOCAL_RELEVANCE_MEDIUM_SUCCESSOR_CANDIDATE_ADMISSION, may one "
            "LOCAL_RELEVANCE_MEDIUM_SECOND_BOUNDED_RELEVANCE_RECEPTION be recorded that "
            "receives exactly one admitted successor candidate as bounded relevance material "
            "under SECOND_BOUNDED_RELEVANCE_RECEPTION_ONLY, without creating repeated "
            "reception permission, arbitrary reception, feed, second receipt, second "
            "orientation view, second index entry, local medium multiplicity result, relation "
            "view, comparison view, index system, registry, search, ranking, source transfer, "
            "source receipt, authority, currentness, truth, action, synchronization, "
            "participation authorization, participant role, runtime permission, public API, "
            "participant-facing interface, distributed network behavior, operation permission, "
            "or follow-on work?"
        )
    non_claims = _canonical_false_non_claims()
    if declared_non_claims is not None:
        non_claims.update(dict(declared_non_claims))

    request: dict[str, Any] = {
        "local_relevance_medium_second_bounded_relevance_reception_id": (
            local_relevance_medium_second_bounded_relevance_reception_id
        ),
        "local_relevance_medium_second_bounded_relevance_reception_question": (
            local_relevance_medium_second_bounded_relevance_reception_question
        ),
        "local_relevance_medium_second_bounded_relevance_reception_intent": (
            local_relevance_medium_second_bounded_relevance_reception_intent
        ),
        "selected_successor_candidate_admission_artifact": str(
            selected_successor_candidate_admission_artifact
        ),
        "second_reception_scope": second_reception_scope,
        "second_reception_type": second_reception_type,
        "second_received_signal_id": second_received_signal_id,
        "second_relevance_basis_id": second_relevance_basis_id,
        "second_relevance_scope_id": second_relevance_scope_id,
        "second_carrier_context_id": second_carrier_context_id,
        "second_reception_envelope_id": second_reception_envelope_id,
        "multiplicity_purpose": multiplicity_purpose,
        "max_local_orientation_objects_after_second_reception": (
            max_local_orientation_objects_after_second_reception
        ),
        "declared_non_claims": non_claims,
    }
    request.update(overrides)
    return request
